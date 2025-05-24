## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: ???

# Package Register
register steel_trap_pregame 1 in core as "The Steel Trap"

# Pregame
label steel_trap_pregame:
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
    # Bondage Store
    steel_trap = Location("The Steel Trap", 'tst', cut_portrait = True, enter_break_labels = ['tst_no_access'], enter_labels = ['tst_enter'], exit_labels = ['tst_exit'], area = ['downtown', 'stores'], unseen = False)
    steel_trap.add_store_item(butt_plug, price = 100, with_examine = True, seen = True)
    steel_trap.add_store_item(chastity_belt, price = 200, with_examine = True, seen = True)
    steel_trap.add_store_item(floggers, available_quantity = 1, price = 200, send_to = dungeon, with_examine = True, seen = True)
    steel_trap.add_store_item(gags, available_quantity = 1, price = 200, send_to = dungeon, with_examine = True, seen = True)
    steel_trap.add_store_item(fuck_machine, available_quantity = 1, price = 400, send_to = dungeon, with_examine = True, seen = True)
    steel_trap.add_store_item(suspension_gear, available_quantity = 1, price = 400, send_to = dungeon, with_examine = True, seen = True)
    tst_dw = steel_trap.add_store_item(domme_whip, available_quantity = 0, price = 200, with_examine = True, seen = True)

    steel_trap.open_store("The Steel Trap")
    downtown.connection_tst = downtown.add_connections(steel_trap)
    steel_trap.connection_do = steel_trap.add_connections(downtown)

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
# Prevent Access to the Steel Trap if Barred
label tst_no_access:
  if 'tst_barred' in player.tags:
    "You're no longer permitted to shop at The Steel Trap."
    break_movement
  else:
    pass
  return

# Check for content on entrance if Applicable
label tst_enter:
    call for_call_labels(label_list = [p.short_name + '_tst_store_enter' for p in get_people(tagged_with_all=['tst_store_content'])]) from _call_for_call_labels_43
    return

# Check for content on Exit
label tst_exit:
    call for_call_labels(label_list = [p.short_name + '_tst_store_exit' for p in get_people(tagged_with_all=['tst_store_content'])]) from _call_for_call_labels_44
    return

# Examine
label tst_examine:
    "A store for the serious BDSM practitioner.  It smells of leather, latex, and steel."
    return

label bp_tst_examine:
    wt_image bondage_store_butt_plugs_store
    "If it can fit safely in your ass, they carry one.  This item can be gifted to some people."
    return

label cb_tst_examine:
    wt_image bondage_store_chastity_belt_store
    "You are shown their impressive collection.  This item can be gifted to some people."
    return

label fl_tst_examine:
    wt_image bondage_store_floggers_store
    "You are shown a selection of some of their finest instruments to examine.  This item will temporarily increase Submission while people are in your Dungeon."
    return

label fl_tst_bought:
  ## NEED: move these image changes to room_enter label
  if dungeon.has_item(gags):
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(14)
        $ dungeon.change_image(14)
      else:
        $ dungeon.change_portrait(13)
        $ dungeon.change_image(13)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(6)
        $ dungeon.change_image(6)
  else:
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(7)
        $ dungeon.change_image(7)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(8)
        $ dungeon.change_image(8)
      else:
        $ dungeon.change_portrait(3)
        $ dungeon.change_image(3)
  return

label ga_tst_examine:
    wt_image bondage_store_gags_store
    "Your choice of ways to silence your partner.  This item will temporarily increase Submission while people are in your Dungeon."
    return

label ga_tst_bought:
  ## NEED: move these image changes to room_enter label
  if dungeon.has_item(floggers):
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(14)
        $ dungeon.change_image(14)
      else:
        $ dungeon.change_portrait(13)
        $ dungeon.change_image(13)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(6)
        $ dungeon.change_image(6)
  else:
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(9)
        $ dungeon.change_image(9)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(10)
        $ dungeon.change_image(10)
      else:
        $ dungeon.change_portrait(2)
        $ dungeon.change_image(2)
  return

label fm_tst_examine:
    wt_image bondage_store_machine_store
    "It does what it says it does, and it does it well.  This item will temporarily increase Submission and Desire while people are in your Dungeon."
    return

label fm_tst_bought:
  ## NEED: move these image changes to room_enter label
  if dungeon.has_item(gags):
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(floggers):
        $ dungeon.change_portrait(14)
        $ dungeon.change_image(14)
      else:
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
    else:
      if dungeon.has_item(floggers):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(10)
        $ dungeon.change_image(10)
  else:
    if dungeon.has_item(suspension_gear):
      if dungeon.has_item(floggers):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(11)
        $ dungeon.change_image(11)
    else:
      if dungeon.has_item(floggers):
        $ dungeon.change_portrait(8)
        $ dungeon.change_image(8)
      else:
        $ dungeon.change_portrait(5)
        $ dungeon.change_image(5)
  return

label sg_tst_examine:
    wt_image bondage_store_suspension_gear_store
    "This is their simplest system. Use with suspension cuffs and the sky's - or the ceiling's - your limit.  This item will temporarily increase Submission while people are in your Dungeon."
    return

label sg_tst_bought:
  ## NEED: move these image changes to room_enter label
  if dungeon.has_item(gags):
    if dungeon.has_item(floggers):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(14)
        $ dungeon.change_image(14)
      else:
        $ dungeon.change_portrait(13)
        $ dungeon.change_image(13)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(9)
        $ dungeon.change_image(9)
  else:
    if dungeon.has_item(floggers):
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(12)
        $ dungeon.change_image(12)
      else:
        $ dungeon.change_portrait(7)
        $ dungeon.change_image(7)
    else:
      if dungeon.has_item(fuck_machine):
        $ dungeon.change_portrait(11)
        $ dungeon.change_image(11)
      else:
        $ dungeon.change_portrait(4)
        $ dungeon.change_image(4)
  return

label dw_tst_examine:
    wt_image dw_image
    "This looks like it will hurt.  The Domme in your life will likely enjoy using this on you.  Whether you enjoy it, too, will probably depend on her mood when she's using it on you."
    return
################################### NOTES ###################################
# N/A
