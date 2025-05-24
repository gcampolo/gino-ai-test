## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: ???

# Package Register
register critter_emporium_pregame 1 in core as "Critter Emporium"

# Pregame
label critter_emporium_pregame:
  python:
  ## Constants
    ## Character Definition
    # N/A

    ## Actions
    # N/A

    ## Tags
    # Common Character Tags
    # N/A

    # Character Specific Tags
    # N/A

    ## Locations
    # Pet Store
    pet_store = Location("The Critter Emporium", 'tce', cut_portrait = True, enter_break_labels = ['tce_no_access'], enter_labels = ['tce_enter'], exit_labels = ['tce_exit'], area = ['downtown', 'stores'], unseen = False)
    pet_store.add_store_item(fetch_toy, price = 50, with_examine = True, seen = True)
    pet_store.add_store_item(leash, price = 50, with_examine = True, seen = True)
    pet_store.add_store_item(water_bowl, price = 50, with_examine = True, seen = True)
    pet_store.open_store("The Critter Emporium")
    downtown.connection_tce = downtown.add_connections(pet_store)
    pet_store.connection_do = pet_store.add_connections(downtown)

    ## Other
    # N/A

    # Start Day Events
    # N/A

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    # N/A
  return

########### CHARACTER ACTIONS ###########
# N/A

########### OBJECTS ###########
# N/A

########### TIMERS ###########
## Common Timers
# N/A

########### ROOMS ###########
# Examine
label tce_examine:
  "A quaint little store with a nice selection of toys and supplies for pampering your pet. There's a steady flow of customers coming and going. It seems a lot of people like to keep pets."
  return

label ft_tce_examine:
  wt_image fetch_toys_store
  "The store sells fetch toys of every size and shape. There should be at least one here that your pet would enjoy playing with."
  return

label le_tce_examine:
  wt_image leash_store
  "The collars in this store appear to be hand made. No doubt your pet will appreciate the extra quality when you take her for a walk."
  return

label wb_tce_examine:
  wt_image waterbowls_store
  "A selection of water bowls is neatly displayed on the store shelf."
  return

label tce_no_access:
    pass # no current restrictions
    return

label tce_enter:
    call for_call_labels(label_list = [p.short_name + '_tce_store_enter' for p in get_people(tagged_with_all=['tce_store_content'])]) from _call_for_call_labels_41
    return

label tce_exit:
    call for_call_labels(label_list = [p.short_name + '_tce_store_exit' for p in get_people(tagged_with_all=['tce_store_content'])]) from _call_for_call_labels_42
    return

################################### NOTES ###################################
# N/A
