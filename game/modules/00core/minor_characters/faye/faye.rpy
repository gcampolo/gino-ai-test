## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package faye name "Faye" description "Allows Faye to be a minor character" dependencies core chelsea
register faye_pregame 15 in core as "Faye"

# NOTE: her content is currently excluvisely in Chelsea's script

label faye_pregame:
  python:
    ## Credits
    model_credits += [('bit', 'Faye (Felicia Clover)')]

  ## Constants
    ## Character Definition
    faye = Person(Character("Faye", who_color="#FF0000", what_color="#FF0000", window_background=gui.dialogue_background_medium_font_color), "faye", cut_portrait = True, prefix = "", suffix = "")

    # Other Characters
    faye_b = Character("Faye's Boyfriend", who_color="#890000", what_color="#890000", window_background = gui.dialogue_background_dark_font_color)

    ## Actions


    ## Tags
    # Common Character Tags
    faye.add_tags('no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    faye.change_status("minor_character")

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
label faye_update_media:
  $ faye.change_image('chubby_threesome_1_26')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label faye_examine:
  "A friend [chelsea.name] met at the Club."
  #"[faye.statblock]"
  #$ items = ", ".join(i.name for i in faye.get_items()) if faye.get_items() != [] else ' Nothing'
  #"You have given her: [items]"
  return

# Talk to Character
label faye_talk:
    "You have nothing to talk to her about."
    return

## Character Specific Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
#label faye_contact:  # not needed
#    pass
#    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_faye:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_faye:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_faye:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_faye:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_faye:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_faye:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_faye:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_faye:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_faye:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_faye:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_faye:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label faye_start_day:
    pass
    return

# End Day
label faye_end_day:
    pass
    return

# End Week
label faye_end_week:
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
