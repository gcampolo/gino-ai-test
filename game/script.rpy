# Default Characters
define narrator = Character(None, what_font = 'fonts/SpecialElite-Regular.ttf', what_size = 30)
# below is a high contrast black on white colour-scheme for Sys boxes, used during playtesting
# define sys = Character("System", who_color="#000000", what_color="#000000", window_background = "#FFFFFFAA")
# below was the original setting for the Sys box, insufficient readibility
#define sys = Character("System", who_color="#993300", what_color="#993300")
# this Sys setting works and meshes with colour-scheme but is a bit bland
# define sys = Character("System", who_color="#333333", what_color="#333333", window_background = "#6F645ADD")
# this Sys setting works and meshes with colout-scheme and pops a bit more
define sys = Character("System", who_color="#FFFFFF", what_color="#FFFFFF", window_background = "#934742DD")

define sys_nvl = Character("System", nvl, who_color="#993300", what_color="#993300")

# Callbacks
define config.history_callbacks = [scroll_to_bottom]
define config.interact_callbacks = [run_delayed_labels]
define config.python_callbacks = [run_delayed_labels]
define config.after_load_callbacks = [versioning_compatibility]

# The game starts here.
label start:
  ###
  # Starting Variables
  ###

  python:
  # Versioning compatibility
    current_version_core = '0_7r'

  # all objects lists
    all_short_names = []
    all_actionables = []
    all_minor_characters = []
    all_clients = []
    all_items = []
    all_trainer_categories = []
    all_locations = []
    all_convertions = ['whore', 'slavegirl', 'girlfriend', 'hypno_girlfriend', 'domme', 'lesbian', 'petgirl', 'showgirl', 'bimbo','assistant', 'teaching_aide', 'degraded', 'adult_baby', 'doll', 'new_people']
    package_actions = []
    expandable_menues = []

  # Day Labels to check
    start_day_labels = LabelListWithPriority()
    end_day_labels = LabelListWithPriority()
    end_day_break_labels = LabelListWithPriority()

  # UI
    notify_block = False
    global_notify_block = False
    notify_messages = NotifyList()
    exempt_contexts = []
    menu_data = []
    menu_shown = False
    current_contexts_list = []
    sticky_image = False
    title = None
    locked_menu = False
    say_y_anchor = 1.0
    nvl_y_anchor = 0.0
    calendar = Actionable('ca')
    calendar.name = "calendar"
    calendar_dict = {}
    calendar_current_id = 0
    model_credits = []

  # Loop variables
    action = None
    action_queue = []
    repeated_action = None
    repeating_action = False
    target_day = None
    break_advance_time = False
    hide_tag = None
    show_screen = None
    advancing_time = False
    consolidated_costs = None
    running_scene = False
    break_condition = False
    break_end_day = False
    ignore_context_change = False
    end_day = False
    end_week = False
    current_target = None
    current_location = None
    current_store = None
    empty_action = Action(None, "", "", "", "", 0, -100, 'False', False, None, -100, False, False, False, dict())
    delayed_labels = []
    bubbled_loops = []

  # Time
    total_days = 1
    day = 1
    week = ext_int(0)

  # Energy
    energy_orgasm = VariableNumber(ext_int(15))
    energy_hypnosis = VariableNumber(ext_int(15))
    energy_very_long = VariableNumber(ext_int(20))
    energy_long = VariableNumber(ext_int(15))
    energy_short = VariableNumber(ext_int(10))
    energy_very_short = VariableNumber(ext_int(5))
    energy_free = VariableNumber(ext_int(0))

  # Stat Handling
    inverse_stats = ['resistance', 'resistance_mod']
    stats = {'sos' : "Sense of Self", 'submission': 'Submission', 'desire': 'Desire', "resistance": 'Resistance', 'sos_mod': 'Sense of Self Modifier', 'desire_mod':'Desire Modifier', 'submission_mod': 'Submission Modifier', 'resistance_mod':'Resistance Modifier', 'money':'Money', 'energy':'Energy', 'reputation':'Reputation' }
    recorded_stats = {'sos' : 'sos', 'resistance': 'resistance', 'desire': 'desire', 'submission':'submission'}
    hypno_ratios = { 'sos' : 0.5 }

  # UI Say Text Breakpoints
    narrator_say_text_breakpoints = { 390: 30, 5000: 28 }
    people_say_text_breakpoints = { 390: 30, 5000: 28 }

  # Translations
    days = { 1 : 'Monday', 2 : ' Tuesday', 3: 'Wednesday', 4 : 'Thursday', 5: 'Friday', 6: 'Weekend' }

  # Client Selections Types
    selection_types = [("Random within Reputation (Default)", "default"), ("Full Random", "random"), ("Player Choice", "choice")]
    custom_selection = False

label package_selection:

  # Topological sort for dependencies
  python:
    # Preparing dependency dict and sorting
    persist.ordered_packages_by_dependencies = toposort_flatten(dict([(p.name, p.dependencies) for p in persist.packages if p.active == True]))

    # Cleaning Actions
    package_actions = []

    # Check broken dependencies and reactivating needed ones
    for package_name in persist.ordered_packages_by_dependencies:

      if package_name not in [p.name for p in persist.packages]:
        raise ValueError("Package {} is not defined!".format(package_name))

      else:
        current_package = next((package for package in persist.packages if package.name == package_name))
        for dependency_name in current_package.dependencies:
          if dependency_name not in [p.name for p in persist.packages]:
            raise ValueError("Dependency {} of Package {} is not defined!".format(dependency_name, package_name))

          current_dependency = next((dependency for dependency in persist.packages if dependency.name == dependency_name))
          if not current_dependency.active:
            package_actions.append("{} depends on {}. Enabling dependency.".format(current_package.full_name, current_dependency.full_name))
            current_dependency.active = True

        for conflict_name in current_package.conflicts:
          if conflict_name not in [p.name for p in persist.packages]:
            raise ValueError("Conflict {} of Package {} is not defined!".format(dependency_name, package_name))

          current_conflict = next((conflict for conflict in persist.packages if conflict.name == conflict_name))
          if current_conflict.active:
            package_actions.append("{} conflicts with {}. Disabling conflict.".format(current_package.full_name, current_conflict.full_name))
            current_conflict.active = False

  # Call module select screen and wait for interaction
  call screen package_select(persist.packages)

  jump package_selection

label after_package_selection:
  python:
    # Calling pregame chain
    pregame_items = []
    for package_name in persist.ordered_packages_by_dependencies:
      package = next((package for package in persist.packages if package.name == package_name))
      package.pregame_labels.sort(key = lambda label: label[1])
      pregame_items.extend(package.pregame_labels)

  call for_call_labels(label_list = [l[0] for l in pregame_items]) from _call_for_call_labels

  # One time update media run
  call for_call_labels(label_list = [actionable.short_name + "_update_media" for actionable in all_actionables], show_errors = False) from _call_for_call_labels_10

  # Pregame is done. We stop user from rolling back the pregame.
  $ renpy.block_rollback()

  # Dev Stuff

  # Background
  show screen static_background
  show screen wt_static_ui

label client_choice_type:
  # Locking button intereaction
  $ running_scene = True

  # Choose client choice type
  $ title = "Client Selection Type:"
  $ selection_type = renpy.display_menu(selection_types, interact=True, screen='choice')

label protagonist_category:
  # Choose protagonist type
  $ title = "Pick your Trainer Type:"
  $ trainer = renpy.display_menu([(t.name, t) for t in all_trainer_categories], interact=True, screen='choice')

  # Call the type introduction
  if renpy.has_label(trainer.label):
    call expression trainer.label from _call_expression_6
  else:
    call fallback_introduction from _call_fallback_introduction

  $ title = "Are you sure you want to be the " + trainer.name + '?'
  $ is_sure = renpy.display_menu([('Yes', True), ('No', False)])

  if is_sure:
    $ player.assign_category(trainer)

    # Call chosen category label
    call safe_call(player.short_name + '_chosen', False, False) from _call_safe_call

    $ running_scene = False
  else:
    jump protagonist_category

  # Start game locations. Current location should have been defined in the pregrame_labels.
  # Core drops you in living_room, but any pregame label can override that.
  $ context = current_location.short_name + "_top_menu"
  call forced_movement(current_location) from _call_forced_movement_62

  # Start actual game :D
  call day_loop from _call_day_loop

  return

# Day loop
label day_loop:

  # Call start of day labels.
  call for_call_labels(label_list = start_day_labels.label_list) from _call_for_call_labels_1

  # We call the core loop to wait for actions
  call core_loop from _call_core_loop

  # Call end of the day labels.
  call for_call_labels(label_list = end_day_labels.label_list) from _call_for_call_labels_2

  # Loop!
  jump day_loop

  return

# Main game loop
label core_loop:

  # Moving the queue
  $ action  = next_action()

  # Basically Black Voodoo Magic
label wait_for_input_loop:
  if action is None:
    call screen wait_for_input
    jump wait_for_input_loop

  # The UI gave us something to look at
  if action is not None:

    # Hide current ui
    call hide_menu from _call_hide_menu

    if isinstance(action, Action):
      # If the action we got can be paid by the player we move forwards
      if action.can_charge(player):

        # We change our target to the owner of the action
        $ current_target = action.owner

        # We only take positivite notify blocks cases. We don't remove existing blocks.
        if action.blocks_notify:
          $ notify_block = True

        # If the UI return a connection, we try to move to the destination calling the move_to label
        # This will check all enter and exit label chains an perform them
        if isinstance(action, Connection):
          $ destination = action.location
          call move_to pass (destination = destination, action = action) from _call_move_to

        else:
          # If the action we are calling has an actual consolidated cost. We charge it.
          if not action.is_zero_charge():
            $ action.charge_costs(player)

          # Let's capture mouse position here in case we need to sho a menu after running a label
          $ mouse_pos = renpy.get_mouse_pos()

          # The action we got has a label to execute
          if action.label != "":
            $ running_scene = True
            $ renpy.block_rollback()
            $ label = action.label

            # Hide menu for scene
            call hide_menu from _call_hide_menu_1

            # Mark this action label as seen
            $ action.seen_result = True
            $ action.make_seen()

            # This is the fallback label section
            # For a label elsa_some_action, the system will try first the label, then a fallback_some_action label.
            # For a label some_action, the system will try first the label, then a fallback_some_action label
            if renpy.has_label(label):

                # If this is an examine label we try to show the actionable's image
                if label.endswith('_examine') and action.owner is not None:
                    if renpy.has_label(action.owner.short_name + "_update_media"):
                        call expression action.owner.short_name + '_update_media' from _call_expression_7
                    wt_image action.owner.image sticky

                call expression label from _call_expression
            else:
                call safe_call(label) from _call_safe_call_1

            # Scene Done. Remove leftover menus if we are not gonna use them.
            # Also check if the action backtracks or ignores contexts
            $ running_scene = False
            $ renpy.block_rollback()
            if ignore_context_change:
                reset_menu
            elif action is not None:
                if action.backtrack:
                    $ action = None
                    call show_menu from _call_show_menu
                    jump wait_for_input_loop
                elif action.context == "":
                    reset_menu

          if ignore_context_change == True:
            $ ignore_context_change = False
          elif action.new_context != "":
            # Show menus in case he hid them
            call show_menu from _call_show_menu_1

            # Assemble data
            $ predicted_last_context = (current_target.short_name + action.context) if action.context.startswith('_') else action.context
            $ predicted_new_context = (current_target.short_name + action.new_context) if action.new_context.startswith('_') else action.new_context

            if action.new_context in ['inventory', 'store']:
              if action.new_context == 'store':
                $ current_store = action.owner

              if action.new_context in current_contexts_list:
                $ menu_data = []
                $ current_contexts_list = []
              else:
                $ menu_data = [(mouse_pos, action.new_context, True, action.locked_menu)]
                $ current_contexts_list = [action.new_context]

            elif predicted_new_context in current_contexts_list:
              # We are going backwards on the menu
              $ index = current_contexts_list.index(predicted_new_context)
              $ menu_data = menu_data[:index]
              $ current_contexts_list = current_contexts_list[:index]

            elif current_contexts_list != [] and predicted_last_context == current_contexts_list[-1]:
              # We are building on the current menu
              $ menu_data.append((mouse_pos, predicted_new_context, False, action.locked_menu))
              $ current_contexts_list.append(predicted_new_context)

            else:
              $ menu_data = [(mouse_pos, predicted_new_context, False, action.locked_menu)]
              $ current_contexts_list = [predicted_new_context]

          else:
            $ menu_data = []
            $ current_contexts_list = []

        # We remove the action notify block (and only the action notify block)
        if not global_notify_block:
          $ notify_block = False

      # Well, the player can't pay for this action so we
      else:
        notify action.fail_costs_to_words(player)
        notify

    # If we got a person or item, we move into her/his/its menu
    elif isinstance(action, Person):
        if action.short_name + "_top_menu" in current_contexts_list:
          $ menu_data = menu_data[:-1]
          $ current_contexts_list = current_contexts_list[:-1]
        else:
          $ current_target = action
          $ context = current_target.short_name + "_top_menu"
          $ menu_data = [(renpy.get_mouse_pos(), context, False, False)]
          $ current_contexts_list = [context]
          # show screen actions_menu_container

    elif isinstance(action, Item):
      if action.short_name + "_top_menu" in current_contexts_list:
        $ menu_data = menu_data[:-1]
        $ current_contexts_list = current_contexts_list[:-1]
      else:
        $ current_target = action
        $ context = current_target.short_name + "_top_menu"

        if current_target.has_portrait_image and 'inventory' not in current_contexts_list:
          $ menu_data = [(renpy.get_mouse_pos(), context, False, False)]
          $ current_contexts_list = [context]
        else:
          $ menu_data = menu_data + [(renpy.get_mouse_pos(), context, False, False)]
          $ current_contexts_list = current_contexts_list + [context]
        # show screen actions_menu_container

    elif isinstance(action, ItemInStore):
      $ current_target = action
      $ context = current_target.short_name + "_top_menu"
      if 'store' in current_contexts_list:
        $ menu_data = menu_data[:1] + [(renpy.get_mouse_pos(), context, False, False)]
        $ current_contexts_list = current_contexts_list[:1] + [context]
      else:
        $ menu_data = [(renpy.get_mouse_pos(), context, False, False)]
        $ current_contexts_list = [context]
      # show screen actions_menu_container

    call show_menu from _call_show_menu_2

  # if we are out of energy we end the day
  if player.energy <= 0:
    reset_menu
    end_day

  # If the day is not over we loop back
  if end_day and not action_queue:
    call for_call_labels(label_list = end_day_break_labels.label_list) from _call_for_call_labels_25

    if break_end_day:
        $ break_end_day = False

        if repeating_action or 'repeating_action' in start_day_labels.label_list:
          $ break_advance_time = True
          call repeating_action from _call_repeating_action

        notify
        $ end_day = False
        jump core_loop

  else:
    jump core_loop

  return

# Safe label call label
label safe_call(call_label, messages = True, fallback = True, override = None):
    if renpy.has_label(call_label):
        call expression call_label from _call_expression_8
    else:
        if fallback:
            if override:
                if renpy.has_label(override):
                    call expression override from _call_expression_38
                elif messages:
                    call fallback_error pass(call_label, override) from _call_fallback_error_3
            else:
                $ short_name = next((sn for sn in all_short_names if call_label.startswith(sn + "_")), None)
                if short_name:
                    $ fallback_label = "fallback" + call_label.replace(short_name, '')
                    if renpy.has_label(fallback_label):
                        call expression fallback_label pass(action.owner) from _call_expression_9
                    elif messages:
                        call fallback_error pass(call_label, fallback_label) from _call_fallback_error
                elif renpy.has_label("fallback_" + call_label):
                    call expression "fallback_" + call_label pass(action.owner) from _call_expression_10
                elif messages:
                    call fallback_error pass(call_label, "fallback_" + call_label) from _call_fallback_error_1
        elif messages:
            call fallback_error pass(call_label, "None") from _call_fallback_error_2
    return

# Note that this will stop at the start of the given day
label repeat_action_until_day(action_to_repeat, until_day, modal = True, starting_action = None, screen_hide_tag = None, screen_show = None):
    # Sanity
    if total_days >= until_day:
        return

    # Stop all input!
    if modal:
        show screen advance_time

    $ repeated_action = action_to_repeat
    $ target_day = int(until_day)
    $ break_advance_time = False
    $ hide_tag = screen_hide_tag
    $ show_screen = screen_show
    $ block_notify()
    $ player.consolidating_changes = True

    # Add repeating label
    if 'repeating_action' not in start_day_labels.label_list:
        $ start_day_labels.append("repeating_action", priority = 'last')

    # Start things up! In case somehow we called this from code while at waiting for input.
    end_day
    if action:
        if starting_action:
            $ queue_action(starting_action, priority = 'last')
        else:
            $ queue_action(action_to_repeat, priority = 'last')
    else:
        $ action = starting_action if starting_action else action_to_repeat
    return

label repeating_action:
    # End condition
    if total_days >= target_day or break_advance_time:
        if break_advance_time:
            notify "Your actions were interrupted."
        day_label rem from start repeating_action
        $ break_advance_time = False
        hide screen advance_time
        if hide_tag:
            $ renpy.hide_screen(hide_tag)
        if show_screen:
            $ renpy.show_screen(show_screen)
        $ repeating_action = False
        $ player.consolidating_changes = False
        $ player.consolidated_change_messages()
        $ notify(True)
        return

    else:
        # Making end day flag True and adding the action at the end of the queue
        $ repeating_action = True
        end_day
        $ queue_action(repeated_action, priority = 'last')

    return

# Repeat action hook for actions
#Acton must be given common_action, alternate_action and stop_day (in string form)
label skip_to_day_with_action:
    call repeat_action_until_day(action.common_action, eval(action.stop_day), starting_action = action.alternate_action if action.condition_tag is not None and player.has_tag(action.condition_tag) else action.common_action, screen_hide_tag = action.screen_hide_tag, screen_show = action.screen_show) from _call_repeat_action_until_day
    return

# Shows the corresponding menu screens to the menu_data given
label show_menu:
    python:
        menu_shown = True
        for i in xrange(0, 6):
            if i < len(menu_data):
                if menu_data[i][3]:
                    renpy.show_screen('menu_holder_modal', menu_position = menu_data[i][0], menu_context = menu_data[i][1], is_item_menu = menu_data[i][2])
                    #back_menu()
                else:
                    renpy.show_screen('menu_holder_' + str(i), menu_position = menu_data[i][0], menu_context = menu_data[i][1], is_item_menu = menu_data[i][2])
                    renpy.hide_screen('menu_holder_modal')
            else:
                renpy.hide_screen('menu_holder_' + str(i))
    return

# Hide all menu screns
label hide_menu(mark_menu_as_hidden = True):
    python:
        menu_shown = not mark_menu_as_hidden
        for i in xrange(0, 6):
            renpy.hide_screen('menu_holder_' + str(i))
        renpy.hide_screen('menu_holder_modal')
    return

# This iterates a list of labels calling them one by one -DB
# It is necessry to do it like this because renpy.call breaks python loops
# Do not change first_call when calling for_call_label or you could cause a crash
label for_call_labels(for_call_initial_index=0, label_list = [], suffix = "", show_errors = False, show_labels = False, first_call = True, uuid = None):

    # Break Condition
    if for_call_initial_index >= len(label_list) or break_condition:
        if uuid in bubbled_loops:
            $ bubbled_loops.remove(uuid)
        return

    if not uuid:
        $ import uuid
        $ uuid = uuid.uuid4()
        $ bubbled_loops.append(uuid)

    if first_call:
        $ label_list = label_list[:]

    # Call current label
    python:
        try:
            for_call_label = label_list[for_call_initial_index] + suffix
        except:
            if uuid in bubbled_loops:
                bubbled_loops.remove(uuid)
            renpy.error("for_call_labels error, label_list: {}, index: {}".format(label_list, for_call_initial_index))
    if show_labels:
        $ print "{} - {}".format(for_call_label, uuid)

    if renpy.has_label(for_call_label):
        call expression for_call_label from _call_expression_1
    elif show_errors:
        sys "Missing label: [label]"

    # Advance index and call next label
    call for_call_labels(for_call_initial_index = for_call_initial_index + 1, label_list = label_list, suffix = suffix, show_errors = show_errors, show_labels = show_labels, first_call = False, uuid = uuid) from _call_for_call_labels_5

    return

# This iterates over a specific dictionary created to check availability of clients
label for_labels_dictionary_check(check_dict, label_keys, uuid = None):

  if not uuid:
        $ import uuid
        $ uuid = uuid.uuid4()
        $ bubbled_loops.append(uuid)

  # Break Condition
  if len(label_keys) == 0:
    if uuid in bubbled_loops:
        $ bubbled_loops.remove(uuid)
    return

  # Check availability conditions
  $ return_value = None
  $ dict_key = label_keys.pop(0)
  if check_dict[dict_key] != True:
    call expression check_dict[dict_key] from _call_expression_11

    if not return_value:
      $ del check_dict[dict_key]

  # Call the function again now that we tested and removed this client/key
  call for_labels_dictionary_check(check_dict = check_dict, label_keys = label_keys, uuid = uuid) from _call_for_labels_dictionary_check_2

  return

label examine_self:
  call examine_self_action_counts from _call_examine_self_action_counts
  show screen examine_self
  return

label examine_self_action_counts:
    python:
        # Makes a list for player's total action counts in game
        player_action_count_list = [player.handjob_count_total, player.blowjob_count_total, player.titfuck_count_total, player.sex_count_total, player.anal_count_total, player.orgasm_count_total, player.swallow_count_total, player.facial_count_total, player.hypno_handjob_count_total, player.hypno_blowjob_count_total, player.hypno_titfuck_count_total, player.hypno_sex_count_total, player.hypno_anal_count_total, player.hypno_orgasm_count_total, player.hypno_swallow_count_total, player.hypno_facial_count_total]
        # Needs a way to keep values from endlessly adding values onto previous Examine calls
        player_action_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Get list of characters in game
        for person in get_people():
            # Makes a list for each character's action counts
            character_action_count_list = [person.handjob_count, person.blowjob_count, person.titfuck_count, person.sex_count, person.anal_count, person.orgasm_count, person.swallow_count, person.facial_count, person.hypno_handjob_count, person.hypno_blowjob_count, person.hypno_titfuck_count, person.hypno_sex_count, person.hypno_anal_count, person.hypno_orgasm_count, person.hypno_swallow_count, person.hypno_facial_count]
            for character_action_count in range(len(character_action_count_list)):
                # Adds player's total action counts from character's action counts
                player_action_count_list[character_action_count] += character_action_count_list[character_action_count]


        #player_action_count_list_names = ['handjob_count_total', 'blowjob_count_total', 'titfuck_count_total', 'sex_count_total', 'anal_count_total', 'orgasm_count_total', 'swallow_count_total', 'facial_count_total']
       # for player_action_count in range(len(player_action_count_list_names)):
           # = 'player.' + player_action_count_list_names[player_action_count]
            #player.player_action_count_list_names = player_action_count_list[player_action_count]
        player.handjob_count_total = player_action_count_list[0]
        player.blowjob_count_total = player_action_count_list[1]
        player.titfuck_count_total = player_action_count_list[2]
        player.sex_count_total = player_action_count_list[3]
        player.anal_count_total = player_action_count_list[4]
        player.orgasm_count_total = player_action_count_list[5]
        player.swallow_count_total = player_action_count_list[6]
        player.facial_count_total = player_action_count_list[7]
        player.hypno_handjob_count_total = player_action_count_list[8]
        player.hypno_blowjob_count_total = player_action_count_list[9]
        player.hypno_titfuck_count_total = player_action_count_list[10]
        player.hypno_sex_count_total = player_action_count_list[11]
        player.hypno_anal_count_total = player_action_count_list[12]
        player.hypno_orgasm_count_total = player_action_count_list[13]
        player.hypno_swallow_count_total = player_action_count_list[14]
        player.hypno_facial_count_total = player_action_count_list[15]
return

label splashscreen:
  # Background and Initial wait
  show black
  pause 0.8

  # Call timed Warning
  call screen warning with dissolve
  with dissolve
  pause 1.0

  # Show WT logo
  show text 'A community project based on original work by' with dissolve:
      xalign 0.5
      yalign 0.2
  pause 1.0
  show wtlogo with dissolve:
    xalign 0.5
    yalign 0.5
  pause 2.0

  # Hide WT Logo
  hide wtlogo
  hide text
  with dissolve
  pause 0.8

  # Show DB Logo
  show text "in association with" with dissolve:
    xpos 560
    yalign 0.2
  pause 1.0
  show digitalbonsai with dissolve:
    xalign 0.5
    yalign 0.5
  pause 1.0

  # Middle animation
  show interdiction:
      xpos 1065
      ypos 830
  with dissolve
  pause 1.0
  show text "... This one!":
    xpos 1350
    ypos 900
  with dissolve
  pause 2.0

  # Hide DB Logo
  hide digitalbonsai
  hide interdiction
  hide text
  with dissolve
  pause 1.0
  return

# This label handles normal movement
label move_to(destination, check_exit_breaks = True, check_enter_breaks = True, check_enter_labels = True, check_exit_labels = True, action = None):
  if not isinstance(destination, Location):
    return

  # Check Exit Breaks
  if check_exit_breaks:
    python:
      exit_break_labels = list(current_location.exit_break_labels)
      exit_break_labels.extend(itertools.chain.from_iterable(p.exit_break_labels for p in current_location.people))
    call for_call_labels(label_list = exit_break_labels) from _call_for_call_labels_6

  # Check if the chain was broken
  if break_condition == True:
    $ break_condition = False
    return

  # Check Enter Breaks
  if check_enter_breaks:
    python:
      enter_break_labels = list(destination.enter_break_labels)
      enter_break_labels.extend(itertools.chain.from_iterable(p.enter_break_labels for p in destination.people))
    call for_call_labels(label_list = enter_break_labels) from _call_for_call_labels_7

  # Check if the chain was broken
  if break_condition == True:
    $ break_condition = False
    return

    # We notify costs use
  if action is not None and not action.is_zero_charge():
    $ action.charge_costs(player)

  # and we reset the menu
  reset_menu

  # Check Exit Labels
  if check_exit_labels:
    python:
      exit_labels = list(current_location.exit_labels)
      exit_labels.extend(itertools.chain.from_iterable(p.exit_labels for p in current_location.people))
    call for_call_labels(label_list = exit_labels) from _call_for_call_labels_8

  # If we didn't break movement ...
  # ... people following moves there
  python:
    for person in [p for p in current_location.people if p.has_tag("follows")]:
      destination.bring_person_here(person)

  # Hide images
  wt_image clear

  # ...we move
  $ last_location = current_location
  $ current_location = destination
  $ player.location = current_location

  # We always show and if this is the first time we see this location we also tell
  if current_location.image is not None:
      wt_image current_location.image
  if current_location.unseen:
      $ current_location.unseen = False
      if renpy.has_label(current_location.short_name + '_examine'):
          call expression current_location.short_name + '_examine' from _call_expression_12
      else:
          sys "Missing label: [current_location.short_name]_examine"

  # Check Enter Labels
  if check_enter_labels:
    python:
      enter_labels = list(destination.enter_labels)
      enter_labels.extend(itertools.chain.from_iterable(p.enter_labels for p in destination.people))
    call for_call_labels(label_list = enter_labels) from _call_for_call_labels_9

  # Mark this connection as seen
  if action is not None:
    $ action.seen_result = True
    if isinstance(action, Action):
      $ action.make_seen()

  return

# Special movement that doesn't check anything. It still carries following people along with you.
label forced_movement(destination):
  call move_to(destination, False, False, False, False) from _call_move_to_1
  return

# Return to last location
label return_previous_location:
  call move_to(last_location, False, False, False, False) from _call_move_to_3
  return

# Calls a menu object created from wt expandable class ExpandableMenu
label expandable_menu(expandable_menu):
    # Menu calling conditions
    $ expandable_menues.append(expandable_menu)

    # Show Expandable Menu Screen
    python:
        title = expandable_menu.title
        expandable_menu.selected_choice = renpy.display_menu(items = [(choice.name, choice) for choice in expandable_menu.choices if choice.eval_condition] + ([(expandable_menu.cancel_text if expandable_menu.cancel_text else ('Nothing' if expandable_menu.parent is None else 'Something Else'), "cancel")] if expandable_menu.cancelable else []) + ([(expandable_menu.chain_cancel_text if expandable_menu.chain_cancel_text else 'Nothing', "chain_cancel")] if expandable_menu.chain_cancelable else []))

    # Selected a valid choice
    if expandable_menu.selected_choice not in ("cancel", "chain_cancel"):

        # Remove choice if is one shot
        if expandable_menu.selected_choice.one_shot:
            $ expandable_menu.remove_choice(expandable_menu.selected_choice)

        # Running pre label
        if expandable_menu.pre_label:
            call safe_call(expandable_menu.pre_label) from _call_safe_call_8

        # Call new expandable menu if choice is that
        if isinstance(expandable_menu.selected_choice.to, ExpandableMenu):
            call expandable_menu(expandable_menu.selected_choice.to) from _call_expandable_menu_1

        # Run choice if is that
        else:
            call expression expandable_menu.selected_choice.to pass (**expandable_menu.selected_choice.variables) from _call_safe_call_2

        # Popping last expandable menu of the list, cuz it must be this instance
        $ expandable_menu = expandable_menues.pop()

        # Run post label
        if expandable_menu.post_label:
            call safe_call(expandable_menu.post_label) from _call_safe_call_9

        if expandable_menu.reopens_once:
            $ expandable_menu.reopens_once = False
            call expandable_menu(expandable_menu) from _call_expandable_menu_2

    # Selected cancel option
    elif expandable_menu.selected_choice == "cancel" and expandable_menu.parent is not None:
        $ expandable_menues.pop()
        call expandable_menu(expandable_menu.parent) from _call_expandable_menu_3

    else:
        $ expandable_menues.pop()

    return

# Call a choice list of people from a given list
label choose_people(people_list, menu_title = "Choose a person"):
  $ title = menu_title
  $ selected_person = renpy.display_menu(items = [(p.name, p) for p in people_list] + [('Cancel', False)])

  if selected_person:
    $ current_target = selected_person
  return

# Calls a choice list of people that contain all the tags passed into the input
label choose_person_with_tags(tagged_with_any = [], not_tagged_with_any = [], tagged_with_all = []):
  $ title = "Choose Person"
  $ selected_persons = renpy.display_menu(items = [(p.name, p) for p in get_people(tagged_with_all = tagged_with_all, tagged_with_any = tagged_with_any, not_tagged_with_any = not_tagged_with_any)] + [('Cancel', False)])

  if selected_persons:
    $ current_target = selected_persons
  return

# Get a random choice from a list people with tag selection
label random_person_with_tags(tagged_with_any = [], not_tagged_with_any = [], tagged_with_all = []):
  $ current_target = renpy.random.choice(get_people(tagged_with_all = tagged_with_all, tagged_with_any = tagged_with_any, not_tagged_with_any = not_tagged_with_any))
  return

# Returns character to fixed_location or dismisses them
label character_location_return(character):
  if character.fixed_location is not None and not character.status == 'unavailable':
    $ character.location = character.fixed_location
    rem tags 'follows' from character
  else:
    $ character.dismiss(False)
  return

# Adds tag and adds count to player whenever a character is converted. Can also remove all previous actions and change status to 'post_training', if desired.
label convert(character, conversion_type, remove_actions = False, status_to_post_training = False, change_to_daily_regime = False, keep_current_client_action = False):

    $ conversion_type_name = str(conversion_type)
    $ character.tags.add(conversion_type_name)

    if status_to_post_training:
        $ character.change_status("post_training")

    if keep_current_client_action:
        $ temp_current_client_action = character.current_client_action

    if remove_actions:
        $ character.actions = []
        $ character.tags.add("no_hypnosis")
        $ character.examine_action = character.add_action("^'Examine ' + character.name", label="_examine", character = character)

    if change_to_daily_regime:
        $ character.training_regime = 'daily'

    if character.transformed_via_object:
        $ character.transformed_via_object = False
        $ temp_expression = 'transformed_' + conversion_type_name
        $ character.tags.add(temp_expression)
        $ character.tags.add("transformed")
        $ temp_expression = None

    if conversion_type_name == "lesbian":
        $ character.tags.add("likes_girls")

    if conversion_type_name in ["degraded", "doll", "petgirl"]:
        $ character.tags.add("no_hypnosis")

    if conversion_type_name == "whore" and not player.has_tag('whores_once'):
        add tags 'whores_once' to player

    if conversion_type_name == "satisfied":
        change player conversion_type_name + '_client_count' by 1 no_message
        call reputation_gain_check(character) from _call_reputation_gain_check

    elif conversion_type_name == "unsatisfied":
        $ living_room.remove_action(character.current_client_action)

    elif conversion_type_name == "unavailable":
        $ convertion_index = 0
        while convertion_index < len(all_convertions):
            if character.has_tag(all_convertions[convertion_index]):
                call unconvert(character, all_convertions[convertion_index]) from _call_unconvert_26
            $ convertion_index += 1

        $ character.actions = []
        $ character.tags.add("no_hypnosis")
        $ character.tags = set(tag for tag in character.story_tags)
        $ character.fixed_location = None
        $ character.change_status("unavailable")
        $ character.dismiss(False)

    else:
        change player conversion_type_name + '_count' by 1 no_message

    if keep_current_client_action:
        $ character.current_client_action = temp_current_client_action

    return

label unconvert(character, conversion_type):
  $ conversion_type_name = str(conversion_type)

  if character.fixed_location is not None:
    $ character.fixed_location = None

  if conversion_type_name == "lesbian":
    $ character.tags.remove("likes_girls")

  $ temp_expression = 'transformed_' + conversion_type_name
  if character.has_tag(temp_expression):
    $ character.remove_tag(temp_expression)
  $ temp_expression = None

  if (character.remove_tag(conversion_type)):
    change player conversion_type + '_count' by -1 no_message
  else:
    $ print "{} is not a {}".format(character.name, conversion_type)
  return

# Checks for reputation gain, usually after a convert to 'satisfied'
label reputation_gain_check(character):
    if player.reputation <= character.min_reputation:
        change player reputation by 1 notify
    return

label buy:
  if not current_target.can_add_store_item():
    "You have as many of those as you need right."
    #"You can't carry any more [current_target.item.name]!"
    return

  $ actual_price = current_target.final_price()
  if actual_price > (player.money - player.min_money):
    notify "You don't have enough money."
    notify
    return

  $ title = "Buy {}{} for {}?".format(current_target.item.name, "(x{})".format(current_target.single_buy_amount) if current_target.single_buy_amount > 1 else "", actual_price)
  $ yesno = renpy.display_menu(items = [("Yes", True), ("No", False)])

  if yesno:
    change player money by -actual_price

    if current_target.send_to is None:
      add current_target.single_buy_amount current_target.item to player

    else:
      add current_target.single_buy_amount current_target.item to current_target.send_to

    # Call specific bought label
    if renpy.has_label(current_target.short_name + "_bought"):
      call expression current_target.short_name + "_bought" from _call_expression_13

    # Call generic bought label
    if renpy.has_label(current_target.item.short_name + "_bought"):
      call expression current_target.item.short_name + "_bought" from _call_expression_14

    # Call store bought label
    if renpy.has_label(current_store.short_name + "_bought"):
      call expression current_store.short_name + "_bought" from _call_expression_15

    $ current_target.available_quantity -= 1
    notify
  return

label reset_menu:
    reset_menu
    return

label end_day:
    end_day
    return

label end_week:
    end_week
    return

label add_calendar_actions(clicked_day = None):
    python:
        del calendar.actions[:]
        calendar.action_rest_until = calendar.add_action('Rest Until Day ' + str(clicked_day) , context = "_actions_day_" + str(clicked_day), label = "skip_to_day_with_action", common_action = player.rest_action, alternate_action = player.end_day_action, stop_day = str(clicked_day), unseen = False, ends_day_icon = True, condition_tag = 'used_energy', screen_hide_tag = 'calendar')

        calendar.action_work_until = calendar.add_action('Work Until Day ' + str(clicked_day) , context = "_actions_day_" + str(clicked_day), label = "skip_to_day_with_action", common_action = player.work_action, alternate_action = player.end_day_action, stop_day = str(clicked_day), unseen = False, ends_day_icon = True, condition_tag = 'used_energy', screen_hide_tag = 'calendar')

        if action:
            queue_action(calendar.add_action("Calendar Daily Context", new_context = "_actions_day_" + str(clicked_day)))
        else:
            action = calendar.add_action("Calendar Daily Context", new_context = "_actions_day_" + str(clicked_day))
    return

####
# Hypnosis
####
label intro_hypnosis(stat):
    # Call specific label if is present
    if renpy.has_label(current_target.short_name + "_" + stat + "_hypnosis"):
      call expression current_target.short_name + "_" + stat + "_hypnosis" from _call_expression_16

    # Call a default label giving it our stat
    elif renpy.has_label(current_target.short_name + "_default_hypnosis"):
      call expression current_target.short_name + "_default_hypnosis" pass (stat) from _call_expression_17

    return

label change_stat_hypnosis(stat):
    # Calculating ratio
    # Character ratios take precedence over general ratios
    if stat in current_target.hypno_ratios:
      $ ratio = current_target.hypno_ratios[stat]
    else:
      $ ratio = hypno_ratios[stat] if stat in hypno_ratios else 1

    if stat in inverse_stats:
        $ ratio *= -1

    # Standard Effect
    change current_target stat by (player.modified_stat('hypnosis_level') * ratio)
    return

label implant_hypnosis_selection(custom_implant = True):
    if custom_implant:
      call custom_implant_hypnosis from _call_custom_implant_hypnosis
    else:
      call implant_hypnosis from _call_implant_hypnosis
    return

label implant_hypnosis_action_label(custom_implant = True):
    call implant_hypnosis_selection(custom_implant) from _call_implant_hypnosis_selection
    call hypnosis_end from _call_hypnosis_end_1
    return

label implant_hypnosis:

    # Implant check
    $ check_trigger = current_target.can_receive_trigger
    if current_target.hypno_count >= current_target.hypno_trigger_sessions_threshold and not 'implanted' in check_trigger[1] and not 'failed' in check_trigger[1]:

      if check_trigger[0]:
        "[current_target.name]'s mind is very open to you now.  She's ready to receive a hypnotic trigger that may allow you to influence her behavior in the future."

        # Compatibility with old system fix
        if current_target.trigger_phrase and current_target.trigger_phrase not in current_target.available_trigger_phrases:
          $ current_target.available_trigger_phrases.append(current_target.trigger_phrase)

        # New multi selection system
        $ title = "Which trigger phrase do you want to use?"
        $ selected_trigger = renpy.display_menu([(trigger, trigger) for trigger in current_target.available_trigger_phrases] + [("Use custom phrase", False)])
        if not selected_trigger:

          $ current_target.trigger_phrase = renpy.input("Which trigger phrase do you want to use?")
        else:
          $ current_target.trigger_phrase = selected_trigger

        call expression current_target.short_name + "_implant_trigger" from _call_expression_18
        add tags 'trigger_implanted' to current_target
        notify "{}'s trigger has been implanted.".format(current_target.name)
      else:
        "You have now hypnotized [current_target.name] [current_target.hypno_count.to_s] times.{nw}"
        if 'label' in check_trigger[1]:
          extend "\n[current_target.name] seems to be specially resistant to triggers. You won't be able to implant one in her.{nw}"
        else:
          if "sessions" in check_trigger[1]:
            extend "\nYou may need a few more sessions to be able to implant a trigger in [current_target.name].{nw}"

          if "resistance" in check_trigger[1]:
            extend "\nYou need to lower [current_target.name]'s resistance if you want to implant a trigger in her.{nw}"

          if "level" in check_trigger[1]:
            extend "\nYou are not good enough as an hypnotist to be able to implant a trigger on [current_target.name].{nw}"

        extend ""

    return

label custom_implant_hypnosis:
    # Implant Check
    $ check_trigger = current_target.can_receive_trigger

    # Check minimal conditions and call label from there
    if 'implanted' not in check_trigger[1] and 'sessions' not in check_trigger[1] and 'failed' not in check_trigger[1]:
        call safe_call(current_target.short_name + "_implant_trigger", fallback = False) from _call_safe_call_3
    return

label hypnosis_end(stat = None):
    if stat is not None and renpy.has_label(current_target.short_name + "_" + stat + "_hypnosis_end"):
      call expression current_target.short_name + "_" + stat + "_hypnosis_end" from _call_expression_20

    if renpy.has_label(current_target.short_name + "_hypnosis_end"):
      call expression current_target.short_name + "_hypnosis_end" from _call_expression_21
    reset_menu
    return

# Label stat has priority over action.stat
label hypnosis(stat = None, custom_implant = True):
  # Set stat
  if 'stat' not in action.__dict__ and not stat:
    return

  $ stat = stat if stat else action.stat
  $ custom_implant = custom_implant if custom_implant else action.custom_implant

  call intro_hypnosis(stat) from _call_intro_hypnosis

  # If the called label asked us to stop, we do.
  # This is used so they can simply add flavor text to the session and then apply the standard effect
  # Or handle the whole logic on their side
  if break_condition == True:
    $ break_condition = False
    return

  call change_stat_hypnosis(stat) from _call_change_stat_hypnosis

  call implant_hypnosis_selection(custom_implant) from _call_implant_hypnosis_selection_1

  call hypnosis_end(stat) from _call_hypnosis_end

  return

label custom_hypnosis_action_end(custom_implant = True):
    $ custom_implant = custom_implant if custom_implant else action.custom_implant

    if custom_implant:
        call custom_implant_hypnosis from _call_custom_implant_hypnosis_1
    else:
        call implant_hypnosis from _call_implant_hypnosis_1

    if renpy.has_label(current_target.short_name + "_hypnosis_end"):
        call expression current_target.short_name + "_hypnosis_end" from _call_expression_4
    reset_menu
    return


label focus_image:
    if player.has_item(old_hypnotic_focus):
        wt_image hypnotizing_2
    else:
        wt_image hypnotizing_1
    return

###
# Item labels
###

label action_on_person:
    $ title = None
    $ selected_person = renpy.display_menu(items = [(p.name, p) for p in player.other_people_in_room] + [('Cancel', False)])

    if selected_person:
      $ label = "{}_{}_{}".format(action.verb, current_target.short_name, selected_person.short_name)
      $ fallback_label = "{}_{}_fallback".format(action.verb, current_target.short_name)
      if renpy.has_label(label):
        call expression label from _call_expression_22
      elif renpy.has_label(fallback_label):
        call expression fallback_label from _call_expression_23
      else:
        sys "Missing label: [label]\nMissing label: [fallback_label]"
    return

####
# FALLBACK LABELS
####

label fallback_examine(target):
  if isinstance(target, ItemInStore):
    $ target.name = target.short_name
  $ current_stats = ", ".join(["{0} : {1}".format(stat, value) for (stat, value) in target.stats.items()])
  $ current_items = ", ".join(["{0} : {1}".format(item.name, amount) for (item, amount) in target.items.items()])
  $ current_tags = ", ".join(target.tags)
  sys "Fallback Examine -> Target: [target.name]\nStats: [current_stats]"
  sys "Fallback Examine -> Target: [target.name]\nItems: [current_items]"
  sys "Fallback Examine -> Target: [target.name]\nTags: [current_tags]"
  return

label fallback_introduction:
  sys "[trainer.name] needs an introduction!"
  return

label fallback_error(label, fallback_label):
  sys "Missing label: [label]\nMissing fallback label: [fallback_label]"
  return

label kickout:
    if player.location not in renpy.store.session_locations:
            return

    python:
        problem_cases = []
        for person in player.other_people_in_room:
            if len([a for a in person.actions if a.eval_action() and a.context == person.short_name + "_top_menu" and a is not person.examine_action]) <= 0:
                problem_cases.append((person.full_name, person))

    if len(problem_cases) >=1:
        sys "It looks like you're stuck with someone you can't otherwise get rid of. You can kick the person out in a sec. Please consider submitting a bug report at our discord. Thanks!"
        $ title = "Who do you want to kickout?"
        $ who = renpy.display_menu(items = problem_cases)
        if who:
            dismiss who
            wt_image current_location.image
    else:
        sys "No one seems to be causing troubles at the moment."

    return

###
# END GAME
###
label end_game:
  # # call player_examine
  # # call player_achievements
  show screen black_overlay
  $ renpy.pause(0.5, hard=True)
  call hide_menu from _call_hide_menu_2
  hide screen wt_static_ui
  hide screen static_background
  hide screen wait_for_input
  hide screen actions_menu
  $ renpy.set_return_stack([])
  $ renpy.pause(0.5, hard=True)
  return

###
# VERSIONING COMPATIBILY
###

label after_load_callback:
    $ versions_keys = versions.keys()
    $ versions_index = 0
    while(versions_index < len(versions_keys)):
        $ package = versions_keys[versions_index]
        $ versions_index =+ 1
        while (versions[package][-1] != store.__dict__['current_version_' + package]):
            $ target_version = versions[package][versions[package].index(store.__dict__['current_version_' + package]) + 1]
            call for_call_labels(label_list = [l for l in renpy.get_all_labels() if l.endswith('_' + package + '_' + target_version)], show_labels = True) from _call_for_call_labels_26
            $ store.__dict__['current_version_' + package] = target_version

    return

label bubbled_loops_0_7h:
    if 'bubbled_loops' not in renpy.store.__dict__:
        $ bubbled_loops = []
    return


###
# DEV LABELS
###
label check_actions_conditions:
    python:
        for actionable in all_actionables:
            for action in actionable.actions:
                action.eval_action()
