## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: ???

# Package Register
register coffee_shop_pregame 1 in core as "Sundollars"

# Pregame
label coffee_shop_pregame:
  python:
  ## Constants
    ## Character Definition
    # Other Characters
    # Dark Teal
    barista_manager = Character("Barista Manager", who_color="#004949", what_color="#004949", window_background = gui.dialogue_background_dark_font_color)
    # N/A

    ## Actions
    # N/A

    ## Tags
    # Common Character Tags
    # N/A

    # Character Specific Tags
    # N/A

    ## Locations
    # Coffee Shop i.e. Sundollars
    coffee_shop = Location("Sundollars", 'cs', cut_portrait = True, enter_break_labels = ['cs_no_access'], enter_labels = ['cs_enter'], exit_labels = ['cs_exit'], area = 'downtown', unseen = False)
    # note: condition results in Buy Coffee icon appearing only if no barista (Samantha or Taylor or otherwise) is in the coffee shop
    coffee_shop.button_order_coffee = coffee_shop.add_button("Order Coffee", label = "_buy_coffee", condition = "coffee_shop.is_empty", auto_image = "gui/button/coffee_%s.png")
    coffee_shop.connection_do = coffee_shop.add_connection(downtown)
    downtown.connection_cs = downtown.add_connection(coffee_shop)

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
label cs_examine:
  "It's your basic busy, downtown coffee shop."
  return

# Prevent Access to Store
label cs_no_access:
  return

# Enter Store
label cs_enter:
  return

# Exit Store
label cs_exit:
  return

# Buy Coffee
label cs_buy_coffee:
  # Sam serves you
  if samantha.new_barista_switch < 2 and not samantha.conversation_event == 16:
    $ samantha.location = coffee_shop
    call samantha_talk from _call_samantha_talk
  # Taylor serves you
  elif samantha.new_barista_switch == 2:
    $ taylor.location = coffee_shop
    call taylor_talk from _call_taylor_talk
  # Store Manager or generic barista serves you
  else:
    if player.energy == player.max_energy:
      "You don't need another coffee."
    else:
      if player.money - player.min_money < 10:
        "You can't afford their overpriced swill."
      else:
        if not player.has_tag('first_coffee_message'):
          add tags 'first_coffee_message' to player
          "[player.first_coffee_message_text]"
        $ title = "Pay 10 to regain 10 Energy?"
        menu:
          "Pay up (costs 10)":
            if samantha.conversation_event == 16:
              wt_image barista_manager_serving
              #"There's no sign of Sam here today. The store manager is handing out the coffee. He notices you come in."
              "The store manager is handing out the coffee. He notices you come in."
              barista_manager "Hey, you're buddies with Sam. Any idea where she is? She hasn't shown up for her shift and no one can reach her. Probably just left town without giving notice, leaving us short staffed."
              $ samantha.new_barista_switch = 1
              # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
              # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
              # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
              # in this case, safer to use simple status change
              #$ call convert(samantha,'unavailable')
              #$ samantha.status = 'unavailable'
              $ tracy.opp = 2
              $ samantha.conversation_event = 17 # moves to 18 at the end of the day in samantha_end_day label
            elif samantha.conversation_event == 17:
              wt_image barista_manager_serving
              "The manager gets you another coffee, but doesn't have time to chat."
            else:
              "An efficient but nondescript barista quickly gets you your coffee and gets you on your way."
            change player energy by 10
            change player money by -10 notify
          "No":
            pass
  return

################################### NOTES ###################################
# N/A
