python early:

  # Shared parses
  def parse_empty(lex):
    return

  def parse_one_name(lex):
    what = lex.require(lex.name)
    return what

  def parse_one_optional_name(lex):
    what = None

    if not lex.eol():
      what = lex.name()

    return what

  def parse_one_expression(lex):
    what = lex.require(lex.simple_expression)
    return what

  # Image handling
  # Parse the wt_image statement
  def parse_image_shortcut(lex):
    what = ""
    sticky = False
    image_only = False

    while not lex.eol() and not sticky:
      if lex.match('sticky'):
        sticky = True
      elif lex.match('image_only'):
        image_only = True
      else:
        what += lex.require(lex.simple_expression)

    return (what, sticky, image_only)

  # Show image in screen shotcut
  def execute_image_shortcut(o):
    what, sticky, image_only = o
    displayable = None

    if what == 'clear':
      if sticky or not store.sticky_image:
        renpy.hide_screen(tag='trainee_image', layer='screens')

    else:
      try:
        what = eval(what)
      except:
        what = Text(what).text[0]
      
      if not image_only:
        displayable = renpy.get_registered_image(what + '_movie')
        if displayable:
            what += '_movie'
    
      if not displayable:
        displayable = renpy.get_registered_image(what)        

      store.sticky_image = sticky

      if displayable:
        if isinstance(displayable, Movie):
          is_video = True
          image_size = (0,0)
        else:
          is_video = False
          image_size = renpy.image_size(displayable)
      else:
        is_video = False
        image_size = (0,0)

      renpy.show_screen(_screen_name = "trainee_image", ti = what, w = image_size[0], h = image_size[1], is_video = is_video)

  renpy.register_statement("wt_image", parse = parse_image_shortcut, execute = execute_image_shortcut)

  # Package registering system
  # register "label" "priority" in "package"
  def parse_register(lex):
    label = lex.require(lex.name)
    priority = lex.require(lex.integer)
    lex.require(str('in'))
    package = lex.require(lex.name)
    name = None

    if lex.match('as'):
      name = lex.require(lex.string)

    return (label, priority, package, name)

  def execute_init_register(o):
    label, priority, package, name = o

    p = next((p for p in persist.packages if p.name == package), None)
    if p is None:
      renpy.error("Package {} is not registered!".format(package))
      return
    else:
      p.pregame_labels.append((label, priority, name))

  renpy.register_statement("register", parse = parse_register, execute_init = execute_init_register )

  # register_package "package" name "full_name" author u"author(s)" description u"description"| enabled/disabled |dependencies "package" "package"
  def parse_register_package(lex):
    package = lex.require(lex.name)
    lex.require(str('name'))
    full_name = lex.require(lex.string)
    lex.require(str('author'))
    author = lex.require(lex.string)
    lex.require(str('description'))
    description = lex.require(lex.string)
    enabled = True
    dependencies = set()
    conflicts = set()

    if lex.match('enabled'):
      enabled = True

    if lex.match('disabled'):
      enabled = False

    has_dependencies = False
    has_conflicts = False
    while not lex.eol():
        candidate = lex.require(lex.name)
        print candidate
        if candidate == 'dependencies':
            has_dependencies = True
            has_conflicts = False

        elif candidate == 'conflicts':
            has_dependencies = False
            has_conflicts = True

        elif has_dependencies:
            dependencies.add(candidate)

        elif has_conflicts:
            conflicts.add(candidate)

    return (package, full_name, author, description, enabled, dependencies, conflicts)

  def execute_init_register_package(o):
    package, full_name, author, description, enabled, dependencies, conflicts = o
    # print o
    if package in [p.name for p in persist.packages]:
      renpy.error("Package {} is already registered!".format(package))
      return
    else:
      persist.packages.append(Package(enabled, package, full_name, author, description, [], dependencies, conflicts))

  renpy.register_statement("register_package", parse = parse_register_package, execute_init = execute_init_register_package )

  # Set a stat
  # set who what to X
  # The set statement takes no flags and emits no notifications
  def parse_set_stat(lex):
    who = lex.require(lex.simple_expression)
    what = lex.require(lex.simple_expression)
    lex.require(str('to'))
    amount = lex.require(lex.simple_expression)

    return (who, what, amount)

  def execute_set_stat(o):
    who, what, amount = o

    who = eval(who)

    if what not in who.stats:
      try:
        what = eval(what)
      except:
        pass

    if amount.startswith('-'):
      negative = True
      amount = amount[1:]
    else:
      negative = False

    amount = eval(amount)
    if isinstance(amount, VariableNumber):
      amount = amount.value

    if negative:
      amount = -amount

    who.set_stat(what, int(round(amount)))

  renpy.register_statement("set", parse = parse_set_stat, execute = execute_set_stat)

  # Changes a stat
  # change who what by X
  def parse_change_stat(lex):
    who = lex.require(lex.simple_expression)
    what = lex.require(lex.simple_expression)
    lex.require(str('by'))
    amount = lex.require(lex.simple_expression)
    message = True
    notify = False
    reason = None

    # And tags = no_message, notify
    while not lex.eol():
      conditional = lex.require(lex.name)

      if conditional == 'no_message':
        message = False
      elif conditional == 'notify':
        notify = True
      else:
        reason = conditional

    return (who, what, amount, message, notify, reason)

  def execute_change_stat(o):
    who, what, amount, message, notify, reason = o

    who = eval(who)

    if what not in who.stats:
      try:
        what = eval(what)
      except:
        pass

    # Process amount taking into account variable numbers (energy costs mostly)
    if amount.startswith('-'):
      negative = True
      amount = amount[1:]
    else:
      negative = False

    amount = eval(amount)
    if isinstance(amount, VariableNumber):
      amount = amount.value

    if negative:
      amount = -amount

    who.change_stat(what, int(round(amount)), False, message, notify, reason)

  renpy.register_statement("change", parse = parse_change_stat, execute = execute_change_stat)

  # Notify command
  def parse_notify(lex):
    what  = lex.simple_expression()

    return what

  def execute_notify(o):
    what = o

    if what is None:
      notify()
    elif what =="clear":
      del notify_messages[:]
    else:
      notify_messages.append(eval(what))

  renpy.register_statement("notify", parse = parse_notify, execute = execute_notify)

  # End Day command
  def execute_end_day(o):
    store.end_day = True

  renpy.register_statement("end_day", parse = parse_empty, execute = execute_end_day)

  # End Day command
  def execute_break_end_day(o):
    store.break_end_day = True

  renpy.register_statement("break_end_day", parse = parse_empty, execute = execute_break_end_day)

  # End Day command
  def execute_end_week(o):
    store.end_week = True
    store.end_day = True

  renpy.register_statement("end_week", parse = parse_empty, execute = execute_end_week)

  # Break Movement Command
  def execute_break_movement(o):
    store.break_condition = True

  renpy.register_statement("break_loop", parse = parse_empty, execute = execute_break_movement)
  renpy.register_statement("break_movement", parse = parse_empty, execute = execute_break_movement)
  renpy.register_statement("break_sequence", parse = parse_empty, execute = execute_break_movement)

  #  Command
  def execute_dismiss(o):
    who = o

    eval(who).dismiss()

  renpy.register_statement("dismiss", parse = parse_one_name, execute = execute_dismiss)

  # Summon Command
  def parse_summon(lex):
    where = ""
    follows = True
    who = lex.require(lex.name)

    connector = lex.name()
    if connector == 'to':
      where = lex.require(lex.name)
      if lex.name() == 'no_follows':
        follows = False
    elif connector == 'no_follows':
      follows = False


    return (who, where, follows)

  def execute_summon(o):
    who, where, follows = o
    if where == "":
      current_location.bring_person_here(eval(who), follows = follows)
    else:
      eval(where).bring_person_here(eval(who), follows = follows)

  renpy.register_statement("summon", parse = parse_summon, execute = execute_summon)

  # Add command
  # add 1 lingerie to player
  # add tag 'has_a_tag' to player
  # add tag 'has_a_tag' to lingerie on player
  # add tags 'tag1' 'tag2' 'tag3' to lingerie on player
  def parse_add(lex):
    amount = 0
    who = None
    on_who = None
    what = None
    which = None
    partial = False
    message = True
    notify = False

    start_point = lex.checkpoint()
    what = lex.name()

    if what == 'tags':
      which = []
      while not lex.match('to') and not lex.eol():
        which.append(lex.require(lex.string))

      who = lex.require(lex.simple_expression)

      if lex.match('on'):
        on_who = lex.require(lex.simple_expression)

    elif what == 'tag':
      which = lex.require(lex.string)
      lex.require(str('to'))
      who = lex.require(lex.simple_expression)

      if lex.match('on'):
        on_who = lex.require(lex.simple_expression)

    else:
      lex.revert(start_point)
      amount = lex.require(lex.simple_expression)
      which = lex.require(lex.simple_expression)
      lex.require(str('to'))
      who = lex.require(lex.simple_expression)

    # And conditionals = inverse, no_message, notify
    while not lex.eol():
      conditional = lex.require(lex.name)

      if conditional == 'no_message':
        message = False
      elif conditional == 'notify':
        notify = True
      elif conditional == 'partial':
        partial = True

    return (amount, what, which, who, on_who, partial, message, notify)

  def execute_add(o):
    (amount, what, which, who, on_who, partial, message, notify) = o

    try:
      amount = eval(amount)
    except:
      pass

    if who:
      who = eval(who)

    if on_who:
      on_who = eval(on_who)

    if what == 'tag':

      if on_who:
        on_who.items.internal_item(who).add_tag(which)
      else:
        who.add_tag(which)

    elif what == 'tags':

        if on_who:
          on_who.items.internal_item(who).add_tags(*which)
        else:
          who.add_tags(*which)

    else:
      who.add_item(eval(which), int(amount), partial, message, notify)

  renpy.register_statement("add", parse = parse_add, execute = execute_add)

  # Add command
  # rem 1 lingerie from player
  # rem tag 'has_a_tag' from player
  def parse_rem(lex):
    amount = 0
    who = None
    what = None
    on_who = None
    which = None
    partial = False
    message = True
    notify = False

    if lex.match('tags'):
      what = 'tags'
      which = []
      while not lex.match('from') and not lex.eol():
        which.append(lex.require(lex.string))

      who = lex.require(lex.simple_expression)

      if lex.match('on'):
        on_who = lex.require(lex.simple_expression)

    elif lex.match('tag'):
      what = 'tag'
      which = lex.require(lex.string)
      lex.require(str('from'))
      who = lex.require(lex.name)

      if lex.match('on'):
        on_who = lex.require(lex.simple_expression)

    elif lex.match('action'):
      what = 'action'
      who = None
      which = None

      if lex.match('from'):
        who = lex.require(lex.name)
      elif not lex.eol():
        which = lex.require(lex.name)
        if lex.match('from'):
          who = lex.require(lex.name)

    else:
      what = None
      amount = lex.require(lex.integer)
      which = lex.require(lex.name)
      lex.require(str('from'))
      who = lex.require(lex.name)

    # And conditionals = inverse, no_message, notify
    while not lex.eol():
      conditional = lex.require(lex.name)

      if conditional == 'no_message':
        message = False
      elif conditional == 'notify':
        notify = True
      elif conditional == 'partial':
        partial = True

    return (amount, what, which, who, on_who, partial, message, notify)

  def execute_rem(o):
    (amount, what, which, who, on_who, partial, message, notify) = o

    if who:
      who = eval(who)

    if on_who:
      on_who = eval(on_who)

    if what == 'tag':
      if on_who:
        on_who.items.internal_item(who).remove_tag(which)
      else:
        who.remove_tag(which)

    elif what == 'tags':
      if on_who:
        on_who.items.internal_item(who).remove_tags(*which)
      else:
        who.remove_tags(*which)


    elif what == 'action':
      if who is None:
        if which is None:
          action.owner.remove_action(action)
        else:
          eval(which).owner.remove_action(eval(which))
      else:
        if which is None:
          who.remove_action(action)
        else:
          who.remove_action(eval(which))

    else:
      who.remove_item(eval(which), int(amount), partial, message, notify)

  renpy.register_statement("rem", parse = parse_rem, execute = execute_rem)

  # Give item to someone
  # give number what from who to who
  def parse_give(lex):
    amount = lex.require(lex.integer)
    what = lex.require(lex.simple_expression)
    lex.require(str('from'))
    giver = lex.require(lex.simple_expression)
    lex.require(str('to'))
    receiver = lex.require(lex.simple_expression)

    partial = False
    message = True
    notify = False
    always_remove = False
    # And tags = no_message, notify
    while not lex.eol():
      conditional = lex.require(lex.name)

      if conditional == 'no_message':
        message = False
      elif conditional == 'notify':
        notify = True
      elif conditional == 'partial':
        partial = True
      elif conditional == 'always_remove':
        always_remove = True

    return (amount, what, giver, receiver, partial, message, notify, always_remove)

  def execute_give(o):
    amount, what, giver, receiver, partial, message, notify, always_remove = o
    amount = eval(amount)
    what = eval(what)
    giver = eval(giver)
    receiver = eval(receiver)

    giver.give_item(what, receiver, amount, partial, message, notify, always_remove)

  renpy.register_statement("give", parse = parse_give, execute = execute_give)

  # Display select people menu
  # target = current_location.display_people_menu() -> select person as target
  def parse_display_people(lex):
    what = lex.require(lex.name)
    lex.require(str('as'))
    return_value = lex.require(lex.name)

    return (what, return_value)

  def execute_display_people(o):
    what, return_value = o

    if what == 'person':
      store.__dict__[return_value] = current_location.display_people_menu()

  renpy.register_statement("select", parse = parse_display_people, execute = execute_display_people)

  # Start and End day labels
  def parse_day_labels(lex):
    what = lex.require(lex.name)
    priority = 0.0
    if what == 'add':
        lex.require(str('to'))
    else:
        lex.require(str('from'))
    target = lex.require(lex.name)

    labels = []
    while not lex.eol():
      if lex.match('priority'):
        priority = lex.require(lex.simple_expression)
        if priority not in ('first', 'last'):
          try:
            priority = float(priority)
          except ValueError:
            raise ValueError("Priority " + priority + "cannot be converted to float")
        break
      else:
        labels.append(lex.require(lex.name))

    return (what, target, labels, priority)

  def execute_day_labels(o):
    what, target, labels, priority = o

    if what == 'add':
        if target == 'start':
            start_day_labels.extend(labels, priority)
        elif target == 'end':
                end_day_labels.extend(labels, priority)
        elif target == 'break':
              end_day_break_labels.extend(labels, priority)
    elif what == 'rem':
        if target == 'start':
            for label in labels:
                try:
                    start_day_labels.remove(label)
                except:
                    pass
        elif target == 'end':
            for label in labels:
                try:
                    end_day_labels.remove(label)
                except:
                    pass
        elif target == 'break':
            for label in labels:
                try:
                    end_day_break_labels.remove(label)
                except:
                    pass

  renpy.register_statement("day_label", parse = parse_day_labels, execute = execute_day_labels)

  # Reset menu statement
  def execute_reset_menu(o):
      reset_menu()

  renpy.register_statement("reset_menu", parse = parse_empty, execute = execute_reset_menu)

  # Back menu statement
  def execute_back_menu(o):
      back_menu()

  renpy.register_statement("back_menu", parse = parse_empty, execute = execute_back_menu)

  # Orgasm statement
  def exec_orgasm(o):
    if o == 'notify':
      notify = True
    else:
      notify = False

    player.change_stat('orgasm_count', 1, with_message = False)
    player.change_stat('energy', -energy_orgasm.value, with_notify = notify, reason = 'Orgasm')

  renpy.register_statement("orgasm", parse = parse_one_optional_name, execute = exec_orgasm)

  # hypno_session statement
  def parse_hypno_session(lex):
    if not lex.eol():
      who = lex.require(lex.name)
    else:
      who = None

    return who

  def exec_hypno_session(o):
    who = o

    try:
      who = eval(who)
    except:
      who = None

    if who is None:
      current_target.hypno_session()
    else:
      who.current_target.hypno_session()

  renpy.register_statement("hypno_session", parse = parse_hypno_session, execute = exec_hypno_session)
