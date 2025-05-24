## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Digital Bonsai

# Package Register
register_package db_choice name "Client Selection Example" author "Digital Bonsai" description "Custom Client Selection example. It selects exactly as default." disabled dependencies core
register db_choice_pregame 1 in db_choice as "DB Choice"

# We add the selection type to the choice dialog here
label db_choice_pregame:
  $ selection_types.append(("DB's Choice", "db_choice"))
  return

# We add to the availability_check_dict here in whatever way we want (It was already created as ab empty dict for us)
label db_choice_availability_check:
  python:
    for client in available_client_list:
      # If we have a label that can check availability we add it to the check dict
      if renpy.has_label(client.short_name + "_availability_check"):
        availability_check_dict[client] = client.short_name + "_availability_check"
      # If we don't dont we do a simply reputation check and add that to the dict
      elif client.min_reputation <= player.reputation:
        availability_check_dict[client] = True
  return

# This is the method that ultimately gets called to select what client to add
# It needs to store the client into the renpy store and select from the availability_check_dict as shown in this example
init 1 python:
    def db_choice_selection_type():
      renpy.store.client = renpy.random.choice(renpy.store.availability_check_dict.keys())