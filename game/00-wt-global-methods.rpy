init 0 python:
    def autosize_say(who, what, *args, **kwargs):
        if who is None or not hasattr(who, '__call__'):
            who = renpy.store.narrator
            breakpoints = store.narrator_say_text_breakpoints
        else:
            breakpoints = store.people_say_text_breakpoints

        for breakpoint in sorted(breakpoints.keys()):
            if len(what) <= breakpoint:
                kwargs['what_size'] = breakpoints[breakpoint]
                break

        who(what, *args, **kwargs)
    renpy.exports.say = autosize_say

  # Special functions
    def notify(force = False):
        if force:
            unblock_notify()

        if not store.notify_block and len(store.notify_messages) > 0 and not renpy.get_screen('notify'):
            s = "\n".join(notify_messages)

            if persistent.notify_to_history_box:
                renpy.say(None, s, interact = False)

            if persistent.notify_to_popup:
                renpy.notify(message = s)

            del store.notify_messages[:]

    def notify_transform(trans, st, at):
        notify()

    def block_notify():
        store.notify_block = True
        store.global_notify_block = True

    def unblock_notify():
        store.notify_block = False
        store.global_notify_block = False

    def reset_menu():
        renpy.store.menu_data = []
        renpy.store.current_contexts_list = []
        renpy.call('hide_menu')

    def back_menu():
        if len(renpy.store.menu_data) > 0 and len(renpy.store.current_contexts_list) > 0:
            renpy.store.menu_data = renpy.store.menu_data[:-1]
            renpy.store.current_contexts_list = renpy.store.current_contexts_list [:-1]
            renpy.call('show_menu')

    def get_people(include_clients = True, include_minor_characters = True, with_status = None, tagged_with_all = [], tagged_with_any = [], not_tagged_with_any = [], at_location = None):

      people_list = (all_clients if include_clients else []) + (all_minor_characters if include_minor_characters else [])
      return [p for p in people_list if
      (p.location == at_location if at_location is not None else True) and
      (p.status == with_status if with_status is not None else True) and
      (set(tagged_with_all) <= set(p.tags) if tagged_with_all != [] else True) and
      (set(tagged_with_any) & set(p.tags) if tagged_with_any != [] else True) and
      (not(set(not_tagged_with_any) & set(p.tags)) if not_tagged_with_any != [] else True)
      ]

    def any_person(include_clients = True, include_minor_characters = True, with_status = None, tagged_with_all = [], tagged_with_any = [], not_tagged_with_any = []):
      return len(get_people(include_clients = include_clients, include_minor_characters = include_minor_characters, with_status = with_status, tagged_with_all = tagged_with_all, tagged_with_any = tagged_with_any, not_tagged_with_any = not_tagged_with_any)) > 0

    def any_client(with_status = None, tagged_with_all = [], tagged_with_any = [], not_tagged_with_any = []):
      return len(get_people(include_minor_characters = False, with_status = with_status, tagged_with_all = tagged_with_all, tagged_with_any = tagged_with_any, not_tagged_with_any = not_tagged_with_any)) > 0

    def get_non_empty_actions(action_list, context = "_top_menu"):

      result_list =[]
      for action in action_list:
        if inspect_action_tree(action, predicted_context = context):
          result_list.append(action)
      return result_list

    def inspect_action_tree(action,  predicted_context, predicted_target = None,  previous_context = "None"):

      if predicted_target is None:
        predicted_target = current_target
      predicted_context = predicted_target.short_name + predicted_context if predicted_context.startswith("_") else predicted_context

      if isinstance(action, (Connection, Text)):
        return True

      elif isinstance(action, (Person, Item)):
        for predicted_action in action.actions:
          if inspect_action_tree(predicted_action, predicted_target = action, predicted_context = "_top_menu", previous_context = predicted_context):
            return True
        return False

      elif isinstance(action, Action):

        # This is a with content label or exempt label
        if action.label != "" or (action.context == store.context and action.new_context == 'location') or action.context in exempt_contexts:
          return True

        # This is a back
        elif action.new_context == previous_context:
          return False

        else:
        # This is a context change we need to check the new context
          for predicted_action in predicted_target.get_menu_objects(action.new_context):
            if inspect_action_tree(predicted_action, predicted_target = predicted_target, predicted_context = action.new_context, previous_context = predicted_context):
              return True
          return False

    def is_weekend():
        return renpy.store.day == 5

    def add_to_history(s):
        if s is not None:
            renpy.say(None, s, interact = False)

    def scroll_to_bottom(history_entry):
        renpy.store.y_adj.value = float("inf")

    def run_delayed_labels():
        if 'delayed_labels' in renpy.store.__dict__ and renpy.store.delayed_labels is not None and 'bubbled_loops' in renpy.store.__dict__ and len(renpy.store.bubbled_loops) == 0:
            inner_labels = renpy.store.delayed_labels[:]
            renpy.store.delayed_labels = []
            if len(inner_labels) > 0:
                renpy.call_in_new_context('for_call_labels', label_list = inner_labels)

    # Calendar STUFF
    def add_note(day, text, weight = 0, exact = False):
        note = (renpy.store.calendar_current_id, text, weight)
        date =  day if exact else day + total_days
        if date in renpy.store.calendar_dict:
            renpy.store.calendar_dict[date].append(note)
            renpy.store.calendar_dict[date].sort(key = lambda l: l[2])
        else:
            renpy.store.calendar_dict[date] = [note]
        renpy.store.calendar_current_id += 1
        return (date, note[0])

    def remove_note(t):
        if not t:
            return

        notes_list = renpy.store.calendar_dict[t[0]]
        for note in notes_list:
            if note[0] == t[1]:
                notes_list.remove(note)
                break

    def get_note(t):
        if not t:
            return

        notes_list = renpy.store.calendar_dict[t[0]]
        for note in notes_list:
            if note[0] == t[1]:
                return note

        return None

    def get_notes(day):
        if day in calendar_dict:
            return [note[1] for note in calendar_dict[day]]
        else:
            return []

    def get_calendar_range_days():
        first_day_week = int(ceil(total_days / 5.0) - 1) * 5 + 1
        return xrange(first_day_week, first_day_week + 150)

    def get_calendar_range_weeks():
        first_week = int(ceil(total_days / 5.0))
        return xrange(first_week, first_week + 30)

    # Action Queue
    def queue_action(action, priority = 0):
        if isinstance(priority, basestring):
            priority_list = [action_tuple[1] for action_tuple in renpy.store.action_queue]
            if priority == 'last':
                if not priority_list:
                    priority_list.append(-1)
                renpy.store.action_queue.append((action, max(priority_list) + 1))
            elif priority == 'first':
                if not priority_list:
                    priority_list.append(1)
                renpy.store.action_queue.append((action, min(priority_list) - 1))
        else:
            renpy.store.action_queue.append((action, priority))
        sort_action_queue()

    def unqueue_actions(action):
        if action in renpy.store.action_queue:
            renpy.store.action_queue.remove(action, reverse = True)

    def sort_action_queue():
        renpy.store.action_queue.sort(key=lambda pa: pa[1])

    def next_action():
        return renpy.store.action_queue.pop()[0] if renpy.store.action_queue else None

    def locations_in_area(area):
        return [l for l in all_locations if (area in l.area if isinstance(l.area, list) else area == l.area)]

    def items_in_area(area):
        return [item for locations in locations_in_area(area) for item in locations.items]

    def client_in_fallback_condition():
        if player.location not in renpy.store.session_locations:
            return False

        for person in player.other_people_in_room:
            if len([a for a in person.actions if a.eval_action() and a.context == person.short_name + "_top_menu" and a is not person.examine_action]) <= 0:
                return True

        return False

    ####
    # DUMMY VERSIONING COMPATIBILITY
    ###
    def versioning_compatibility():
        renpy.call('after_load_callback')