## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package brooklyn name "Brooklyn" description "Allows Brooklyn to be a minor character" dependencies core club
register brooklyn_pregame 10 in core as 'Brooklyn'

label brooklyn_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('bit', 'Brooklyn (Brooklyn Chase)')]

    ## Character Definition
    brooklyn = Person(Character("Brooklyn", who_color="#FF0080", what_color="#FF0080"), "brooklyn", cut_portrait = True, prefix = "", suffix = "")

    # Other Characters
    # N/A

    ## Actions


    ## Tags
    # Common Character Tags
    brooklyn.add_tags('no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    brooklyn.change_status("minor_character")

    # Start Day Events
    # N/A

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    # N/A
  return

# Display Portrait
# CHARACTER: Display Portrait
label brooklyn_update_media:
  $ brooklyn.change_image('brooklyn_portrait_1')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label brooklyn_examine:
    if current_location == swingers_room:
        "A woman at the Club who seems interested in [chelsea.name]. Or at least interested in having [chelsea.name] play with her husband."
    else:
        ""
        "[brooklyn.statblock]"
        $ items = ", ".join(i.name for i in brooklyn.get_items()) if brooklyn.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    return

# Talk to Character
label brooklyn_talk:
    "You have nothing to say to her."
    return

## Character Specific Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
#label brooklyn_contact: #not needed
#  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_brooklyn:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_brooklyn:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_brooklyn:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_brooklyn:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_brooklyn:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_brooklyn:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_brooklyn:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_brooklyn:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_brooklyn:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_brooklyn:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_brooklyn:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
#label brooklyn_start_day: # not needed
#  return

# End Day
label brooklyn_end_day:
    pass
    return

# End Week
label brooklyn_end_week:
    pass
    return

## Character Specific Timers
# N/A

########### ROOMS ###########
# N/A

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
