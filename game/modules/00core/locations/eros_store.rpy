## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: ???

# Package Register
register eros_store_pregame 1 in core as "Eros Store"

# Pregame
label eros_store_pregame:
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
    # Eros Store
    eros_store = Location("Eros Store",'es', cut_portrait = True, enter_break_labels = ['es_no_access'], enter_labels = ['es_enter'], exit_labels = ['es_exit'], area = ['downtown', 'stores'], unseen = False)
    eros_store.add_store_item(dildo, price = 100, with_examine = True, seen = True)
    eros_store.add_store_item(lingerie, price = 200, with_examine = True, seen = True)
    eros_store.add_store_item(ceiling_mirror, available_quantity = 1, price = 300, send_to = boudoir, with_examine = True, seen = True)
    eros_store.add_store_item(fluffy_cuffs, available_quantity = 1, price = 100, send_to = boudoir, with_examine = True, seen = True)
    eros_store.add_store_item(scented_oils, available_quantity = 1, price = 100, send_to = boudoir, with_examine = True, seen = True)
    eros_store.add_store_item(silk_sheets, available_quantity = 1, price = 200, send_to = boudoir, with_examine = True, seen = True)
    eros_store.open_store("Eros Store")
    downtown.connection_es = downtown.add_connections(eros_store)
    eros_store.connection_do = eros_store.add_connections(downtown)

    ## Other
    eros_store.chelsea_bra_message = False

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
label es_examine:
  "A classy looking sex shop. They have a large selection of lingerie and other fine items."
  return

# Prevent Access to Store
label es_no_access:
    return

# Enter Store
label es_enter:
    call for_call_labels(label_list = [p.short_name + '_es_store_enter' for p in get_people(tagged_with_all=['es_store_content'])]) from _call_for_call_labels_45
    return

# Exit Store
label es_exit:
    call for_call_labels(label_list = [p.short_name + '_es_store_exit' for p in get_people(tagged_with_all=['es_store_content'])]) from _call_for_call_labels_46
    return

label di_es_examine:
  wt_image eros_store_dildo_store
  "They have nearly every color and shape you can imagine.  This item can be gifted to some people."
  return

label li_es_examine:
  wt_image eros_store_lingerie_store
  "An extensive selection of lingerie.  This item can be gifted to some people."
  return

label cm_es_examine:
  wt_image eros_store_ceiling_mirror_store
  "The store will arrange for delivery and installation.  This item will temporarily increase Desire while people are in your Boudoir."
  return

label cm_es_bought:
  ## NEED: move these image changes to room_enter label
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
  if boudoir.has_item(candles_avon):
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire < 30:
        $ boudoir.change_portrait(5)
        $ boudoir.change_image(5)
      else:
        $ boudoir.change_portrait(7)
        $ boudoir.change_image(7)
    else:
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(1)
        $ boudoir.change_image(1)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(2)
          $ boudoir.change_image(2)
        else:
          $ boudoir.change_portrait(3)
          $ boudoir.change_image(3)
  else:
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire < 30:
        $ boudoir.change_portrait(10)
        $ boudoir.change_image(10)
      else:
        $ boudoir.change_portrait(7)
        $ boudoir.change_image(7)
    else:
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(12)
        $ boudoir.change_image(12)
      else:
        $ boudoir.change_portrait(13)
        $ boudoir.change_image(13)
  return

label fc_es_examine:
  wt_image eros_store_fluffy_cuffs_store
  "They look innocent, but they're surprisingly effective.  This item will temporarily increase Desire and Submission while people are in your Boudoir."
  return

label fc_es_bought:
  ## NEED: move these image changes to room_enter label
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
  if boudoir.has_item(candles_avon):
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(4)
        $ boudoir.change_image(4)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(5)
          $ boudoir.change_image(5)
        else:
          if boudoir.has_item(ceiling_mirror):
            $ boudoir.change_portrait(7)
            $ boudoir.change_image(7)
          else:
            $ boudoir.change_portrait(6)
            $ boudoir.change_image(6)
    else:
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(1)
        $ boudoir.change_image(1)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(2)
          $ boudoir.change_image(2)
        else:
          $ boudoir.change_portrait(3)
          $ boudoir.change_image(3)
  else:
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire == 15:
        $ boudoir.change_portrait(9)
        $ boudoir.change_image(9)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(10)
          $ boudoir.change_image(10)
        else:
          $ boudoir.change_portrait(7)
          $ boudoir.change_image(7)
    else:
      if boudoir.added_desire == 5:
        $ boudoir.change_portrait(14)
        $ boudoir.change_image(14)
      else:
        if boudoir.has_item(ceiling_mirror):
          if boudoir.added_desire < 20:
            $ boudoir.change_portrait(12)
            $ boudoir.change_image(12)
          else:
            $ boudoir.change_portrait(13)
            $ boudoir.change_image(13)
        else:
          if boudoir.added_desire == 15:
            $ boudoir.change_portrait(9)
            $ boudoir.change_image(9)
  return

label so_es_examine:
  wt_image eros_store_scented_oils_store
  "A selection of fragrances to set just the right mood.  This item will temporarily increase Desire while people are in your Boudoir."
  return

label so_es_bought:
  ## NEED: move these image changes to room_enter label
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
  if boudoir.has_item(candles_avon):
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(4)
        $ boudoir.change_image(4)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(5)
          $ boudoir.change_image(5)
        else:
          if boudoir.has_item(ceiling_mirror):
            $ boudoir.change_portrait(7)
            $ boudoir.change_image(7)
          else:
            $ boudoir.change_portrait(6)
            $ boudoir.change_image(6)
    else:
      if boudoir.added_desire < 20:
        $ boudoir.change_portrait(1)
        $ boudoir.change_image(1)
      else:
        if boudoir.added_desire < 30:
          $ boudoir.change_portrait(2)
          $ boudoir.change_image(2)
        else:
          $ boudoir.change_portrait(3)
          $ boudoir.change_image(3)
  else:
    if boudoir.has_item(silk_sheets):
      if boudoir.added_desire == 10:
        $ boudoir.change_portrait(8)
        $ boudoir.change_image(8)
      else:
        if boudoir.added_desire == 15:
          $ boudoir.change_portrait(9)
          $ boudoir.change_image(9)
        else:
          if boudoir.added_desire < 30:
            $ boudoir.change_portrait(10)
            $ boudoir.change_image(10)
          else:
            $ boudoir.change_portrait(7)
            $ boudoir.change_image(7)
    else:
      if boudoir.has_item(ceiling_mirror):
        if boudoir.added_desire < 20:
          $ boudoir.change_portrait(12)
          $ boudoir.change_image(12)
        else:
          $ boudoir.change_portrait(13)
          $ boudoir.change_image(13)
      else:
        if boudoir.added_desire == 10:
          $ boudoir.change_portrait(11)
          $ boudoir.change_image(11)
        elif boudoir.added_desire == 15:
          $ boudoir.change_portrait(9)
          $ boudoir.change_image(9)
  return

label ss_es_examine:
  wt_image eros_store_silk_sheets_store
  "Beautiful silk sheets add a touch of class to any boudoir.  This item will temporarily increase Desire while people are in your Boudoir."
  return

label ss_es_bought:
  ## NEED: move these image changes to room_enter label
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
  if boudoir.has_item(candles_avon):
    if boudoir.added_desire < 20:
      $ boudoir.change_portrait(4)
      $ boudoir.change_image(4)
    else:
      if boudoir.added_desire < 30:
        $ boudoir.change_portrait(5)
        $ boudoir.change_image(5)
      else:
        if boudoir.has_item(ceiling_mirror):
          $ boudoir.change_portrait(7)
          $ boudoir.change_image(7)
        else:
          $ boudoir.change_portrait(6)
          $ boudoir.change_image(6)
  else:
    if boudoir.added_desire == 10:
      $ boudoir.change_portrait(8)
      $ boudoir.change_image(8)
    elif boudoir.added_desire == 15:
      $ boudoir.change_portrait(9)
      $ boudoir.change_image(9)
    elif boudoir.added_desire < 30:
      $ boudoir.change_portrait(10)
      $ boudoir.change_image(10)
    else:
      $ boudoir.change_portrait(7)
      $ boudoir.change_image(7)
  return

################################### NOTES ###################################
# N/A
