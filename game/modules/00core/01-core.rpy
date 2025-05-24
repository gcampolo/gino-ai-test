# Registering package
register_package core name "WT Core" author "WT Team" description "This package contains the main game components"
register core_pregame 0 in core as "Core"

label core_pregame:
  # Add day labels
  day_label add to start core_start_day priority first
  day_label add to end core_end_day priority last

  python:
    ####
    # PLAYER
    ####

    # Player Object
    player = Player(Character("You", who_color = "#FFF"))

    # Player Variables
    player.add_stats_with_value('odd_job_fee', 'client_visits_count', 'client_visits_this_week', 'male_sex_count')
    player.odd_job_fee = 15

    # Player Tags
    player.add_tag('player')
    player.remove_tags_daily.add('used_energy')

    # Player Actions
    player.action_return_living_room = player.add_action("Return to living room", label = "player_return_living_room", condition = "'ivy_check_messages_first' in living_room.exit_break_labels")

    ####
    # PEOPLE
    ####

    # N/A

    ####
    # ITEMS & ACTIONS
    ####

    ## NOTE: all Items must have a _portrait image
    ## Eros Store
    dildo = Item("Dildo", 'di', max_quantity = 100, with_examine = True, with_give = True)
    lingerie = Item("Lingerie", 'li', max_quantity = 100, with_examine = True, with_give = True)
    ceiling_mirror = Item("Ceiling Mirror", 'cm', with_examine = True, desire_mod = 10)
    fluffy_cuffs = Item("Fluffy Cuffs", 'fc', with_examine = True, desire_mod = 5, submission_mod = 10)
    scented_oils = Item("Scented Oils", 'so', with_examine = True, desire_mod = 10)
    silk_sheets = Item("Silk Sheets", 'ss', with_examine = True, desire_mod = 10)

    ## Bondage Store
    butt_plug = Item("Butt Plug", 'bp', max_quantity = 100, with_examine = True, with_give = True)
    chastity_belt = Item('Chastity Belt', 'cb', max_quantity = 100, with_examine = True, with_give = True)
    floggers = Item('Floggers and Paddles', 'fl', with_examine = True, submission_mod = 10)
    fuck_machine = Item('Fuck Machine', 'fm', with_examine = True, desire_mod = 10, submission_mod = 5)
    gags = Item('Ball and Ring Gags', 'ga', with_examine = True, submission_mod = 10)
    suspension_gear = Item('Suspension Gear', 'sg', with_examine = True, submission_mod = 10)
    domme_whip = Item('Domme Whip', 'dw', max_quantity = 100, with_examine = True, with_give = True)

    ## Dark Art Store
    love_potion = Item('Love Potion', 'lp', max_quantity = 100, with_examine = True, with_give = True)

    ## Pet Store
    fetch_toy = Item('Fetch Toy', 'ft', max_quantity = 1, with_examine = True, with_use = True)
    leash = Item('Leash', 'le', max_quantity = 1, cut_portrait = True, with_examine = True, with_use = True)
    water_bowl = Item('Water Bowl', 'wb', max_quantity = 1, cut_portrait = True, with_examine = True, with_use = True)

    ## Bank
    bank_pen = Item('Bank Pen', 'bap', with_examine = True)
    bank_pen.action_throw_away = bank_pen.add_action("Throw It Away", label = '_throw_away')

    ## Jewelry Store
    # N/A

    ## Other

    ####
    # LOCATIONS, ACTIONS & CONNECTIONS
    ####

    ## NOTE: all locations must have a _portrait image

    # Living Room
    living_room = Location("Living Room", 'lr', cut_portrait = True, enter_break_labels = ['lr_no_access'], enter_labels = ['lr_enter'], exit_labels = ['lr_exit'], area = 'house', unseen = False)

    ## Phone Button
    living_room.button_phone = living_room.add_button("Your Phone", new_context = "_phone", condition = "living_room.is_empty", auto_image = "gui/button/phone_%s.png")
    living_room.action_check_messages = living_room.add_action("Check Messages", context = '_phone', new_context = "_check_messages")
    living_room.action_arrange_session_client = living_room.add_action("Arrange Session with Client", context = '_phone', new_context = "_call_clients", condition = "living_room.is_empty and any_client(with_status = 'on_training') and not is_weekend()", ends_day_icon = True)
    living_room.action_contact_former_client = living_room.add_action("Contact Former Client", context = '_phone', new_context = "_post_training", condition = "living_room.is_empty and any_client(with_status = 'post_training', not_tagged_with_any = ['post_continuing_actions'])")
    living_room.action_contact_other = living_room.add_action("Contact Other People", context = '_phone', new_context = "_contact_other", condition = "living_room.is_empty")
    living_room.action_check_whores = living_room.add_action("Check On Your Whores", label = 'check_whores', context = '_phone', condition = "living_room.is_empty and any_person(tagged_with_all = ['whore'])")
    living_room.action_arrange_weekend = living_room.add_action("Arrange Weekend", label = "arrange_weekend", context = '_phone', condition = "living_room.is_empty and any_client(with_status = 'on_training') and is_weekend() and player.test('energy', (energy_long.value - 1))", ends_day_icon = True)

    ## Review Files Button
    living_room.button_review_files = living_room.add_button("Review Files", new_context ='_review_files', condition = "living_room.has_action_of_context('_review_files') and living_room.is_empty", auto_image = "gui/button/review_files_%s.png")

    ## End day Button
    living_room.button_end_day = living_room.add_button("End Day", new_context = "end_day", condition = "living_room.is_empty and not 'ivy_check_messages_first' in living_room.exit_break_labels", auto_image = 'gui/button/time_%s.png', button_weight = 999, unseen = False, seen_result = True)
    player.end_day_action = living_room.add_action("End the day", context = 'end_day', label = "end_day", condition = "player.has_tag('used_energy')", ends_day_icon = True, blocks_notify = True, unseen = False, seen_result = True)
    player.rest_action = living_room.add_action("Rest for the day", context = 'end_day', label = "end_day", gains = 15, condition = "not player.has_tag('used_energy')", ends_day_icon = True, blocks_notify = True, unseen = False, seen_result = True)
    player.work_action = living_room.add_action("Find some work", context = 'end_day', label = "end_day", costs = 20, gains = { 'money' : player.odd_job_fee }, ends_day_icon = True, blocks_notify = True, unseen = False, seen_result = True)
    living_room.action_rest_until_weekend = living_room.add_action("Rest until Weekend", context = 'end_day', label = "skip_to_day_with_action", condition = "day < 5", ends_day_icon = True, common_action = player.rest_action, alternate_action = player.end_day_action, stop_day = 'ceil(total_days / 5.0) * 5', condition_tag = 'used_energy', unseen = False, seen_result = True)
    living_room.action_rest_until_monday = living_room.add_action("Rest until Monday", context = 'end_day', label = "skip_to_day_with_action", ends_day_icon = True, common_action = player.rest_action, alternate_action = player.end_day_action, stop_day = 'ceil(total_days / 5.0) * 5 + 1', condition_tag = 'used_energy', unseen = False, seen_result = True)
    living_room.action_work_until_weekend = living_room.add_action("Work until Weekend", context = 'end_day', label = "skip_to_day_with_action", condition = "day < 5", ends_day_icon = True, common_action = player.work_action, stop_day = 'ceil(total_days / 5.0) * 5', condition_tag = None, unseen = False, seen_result = True)
    living_room.action_work_until_monday = living_room.add_action("Work until Monday", context = 'end_day', label = "skip_to_day_with_action", ends_day_icon = True, common_action = player.work_action, stop_day = 'ceil(total_days / 5.0) * 5 + 1', condition_tag = None, unseen = False, seen_result = True)

    ## House Locations
    # Backyard
    ## note: the backyard does not have connection to the rest of the house; it's just for teleporting into and out of during location related scenes
    backyard = Location ("Backyard", 'byd', cut_portrait = True, area = 'house', unseen = True)

    # Basement
    basement = Location("Basement", 'ba', cut_portrait = True, enter_break_labels = ['ba_no_access'], enter_labels = ['ba_enter'], exit_labels = ['ba_exit'], area = 'house', unseen = False)

    # Bathroom
    ## note: the bathroom does not have connection to the rest of the house; it's just for teleporting into and out of during location related scenes
    bathroom = Location ("Bathroom", 'bth', cut_portrait = True, area = 'house', unseen = True)

    # Bedroom
    bedroom = Location("Bedroom" , 'be', cut_portrait = True, enter_break_labels = ['be_no_access'], enter_labels = ['be_enter'], exit_labels = ['be_exit'], area = 'house', unseen = False)
    ## Relationship Status Button
    bedroom.button_view_relationship_status = bedroom.add_button("View Relationship Status", new_context = '_relationship_status', condition = "bedroom.has_action_of_context('_relationship_status')", auto_image = 'gui/button/relationship_%s.png')
    ## Computer Button
    bedroom.button_use_computer = bedroom.add_button("Use Computer", new_context ='_use_computer', condition = "bedroom.has_action_of_context('_use_computer')", auto_image = "gui/button/laptop_%s.png")
    bedroom.action_view_images = bedroom.add_action("View Saved Images", context = '_use_computer', new_context = "_computer_view_images", condition = "bedroom.has_action_of_context('_computer_view_images')")

    # Boudoir
    boudoir = Location ("Boudoir", 'bo', cut_portrait = True, enter_break_labels = ['bo_no_access'], enter_labels = ['bo_enter'], exit_labels = ['bo_exit'], desire_mod = 0, area = 'house', unseen = False)

    # Dungeon
    dungeon = Location("Dungeon", 'du', cut_portrait = True, enter_break_labels = ['du_no_access'], enter_labels = ['du_enter'], exit_labels = ['du_exit'], submission_mod = 0, area = 'house', unseen = False)
    dungeon.change_portrait(1)
    dungeon.change_image(1)

    # Garage
    ## note: the garage does not have connection to the rest of the house; it's just for teleporting into and out of during location related scenes
    garage = Location ("Garage", 'gar', cut_portrait = True, area = 'house', unseen = True)

    # Kitchen
    ## note: the kitchen does not have connection to the rest of the house; it's just for teleporting into and out of during location related scenes
    kitchen = Location ("Kitchen", 'ki', cut_portrait = True, area = 'house', unseen = True)


    ## Other Locations
    # Downtown
    downtown = Location("Downtown", 'do', cut_portrait = True, enter_break_labels = ['do_no_access'], enter_labels = ['do_enter'], exit_labels = ['do_exit'], area = 'downtown', unseen = False)

    # Office Tower
    office_tower = Location("Office Tower", 'ot', cut_portrait = True, enter_break_labels = ['ot_no_access'], enter_labels = ['ot_enter'], exit_labels = ['ot_exit'], area = 'offices', unseen = False)
    office_tower.button_elevator = office_tower.add_button("Elevator", new_context = '_elevator', auto_image = "gui/button/elevator_%s.png")

    # Outdoors
    # note: outdoors has no connections; script needs to dictate when you enter and leave
    outdoors = Location("Outdoors", 'od', cut_portrait = True, enter_break_labels = ['od_no_access'], enter_labels = ['od_enter'], exit_labels = ['od_exit'])

    # Gym
    # note: gym has no connections; script needs to dictate when you enter and leave
    gym = Location("Gym", 'gym', cut_portrait = True, enter_break_labels = ['gym_no_access'], enter_labels = ['gym_enter'], exit_labels = ['gym_exit'])

    # Connections
    living_room.connection_bo_du = living_room.add_connections(boudoir, dungeon)
    living_room.connection_be = living_room.add_connection(bedroom, condition = "living_room.is_empty")
    living_room.connection_ba = living_room.add_connection(basement, condition = "living_room.is_empty")
    living_room.connection_do = living_room.add_connection(downtown, costs = 10, condition = "living_room.is_empty")
    boudoir.connection_lr = boudoir.add_connection(living_room)
    dungeon.connection_lr = dungeon.add_connection(living_room)
    bedroom.connection_lr = bedroom.add_connection(living_room)
    basement.connection_lr = basement.add_connection(living_room)
    downtown.connection_lr = downtown.add_connection(living_room, name = "Go Home", order = 79.9)
    office_tower.connection_do = office_tower.add_connection(downtown, order = 79.9)
    downtown.connection_ot = downtown.add_connections(office_tower)

    ####
    ## PLAYER MESSAGES & STUFF
    ####
    player.first_client_visit_message_text = "You may conduct your session here, or you can take your client into your boudoir or dungeon. Items in each room may impact the success of some training activities."
    player.first_hypno_breasts_message_text = "The suggestion to bare her breasts is a simple one. You find it fascinating how easily women comply with it. Some are just comfortable with their bodies, some are proud of their breasts, others are insecure but hoping for approval. Whatever their reasons, it makes the rest of the session more enjoyable for you."
    player.first_coffee_message_text = "The prices here are ridiculous, but they seem to have a monopoly."

    # Examine Phrases
    player.add_examine_phrase("player.has_tag('das_bonus_to_sos_results')", "You have become better at helping clients feel good about themselves.")
    player.add_examine_phrase("player.sp_use_count >= 2", "Your balls seem smaller now.", "player.sp_use_count >= 3", "Your balls seem smaller. You start to feel like a whole new you.")

    ####
    ## MINOR CHARACTERS & ACTIONS
    ####
    # included in their .rpy files

    ####
    ## CLIENTS & ACTIONS
    ####
    # included in their .rpy files

    ####
    ## OTHER
    ####
    session_locations = [living_room, boudoir, dungeon]

    starting_location = living_room
    current_location = living_room
    last_location = living_room

    ####
    ## EXPANDIBLE MENUS
    ####
    ## GAME CONCEPTS
    # CLIENT STATS
    game_concepts_client_stats_menu = ExpandableMenu("What would you like to learn more about?", cancelable = True, chain_cancelable = True)
    player.choice_game_concepts_client_stats_menu_sos = game_concepts_client_stats_menu.add_choice("Sense of Self", "concept_description_sos")
    player.choice_game_concepts_client_stats_menu_desire = game_concepts_client_stats_menu.add_choice("Desire", "concept_description_desire")
    player.choice_game_concepts_client_stats_menu_submission = game_concepts_client_stats_menu.add_choice("Submission", "concept_description_submission")
    player.choice_game_concepts_client_stats_menu_resistance = game_concepts_client_stats_menu.add_choice("Resistance", "concept_description_resistance")

    # PLAYER STATS
    game_concepts_player_stats_menu = ExpandableMenu("What would you like to learn more about?", cancelable = False)
    player.choice_game_concepts_player_stats_menu_money = game_concepts_player_stats_menu.add_choice("Money", "concept_description_money")
    player.choice_game_concepts_player_stats_menu_energy = game_concepts_player_stats_menu.add_choice("Energy", "concept_description_energy")
    player.choice_game_concepts_player_stats_menu_reputation = game_concepts_player_stats_menu.add_choice("Reputation", "concept_description_reputation")
    player.choice_game_concepts_player_stats_menu_something_else = game_concepts_player_stats_menu.add_choice("Something else", "concepts_menu_something_else")
    player.choice_game_concepts_player_stats_menu_nothing = game_concepts_player_stats_menu.add_choice("Nothing", "concepts_menu_nothing")
    # OTHER CONCEPTS
    game_concepts_other_concepts_menu = ExpandableMenu("What would you like to learn more about?", cancelable = False)
    player.choice_game_concepts_other_concepts_menu_minor_clients = game_concepts_other_concepts_menu.add_choice("Minor Clients", "concept_description_minor_clients")
    player.choice_game_concepts_other_concepts_menu_modifiers = game_concepts_other_concepts_menu.add_choice("Modifiers", "concept_description_modifiers")
    player.choice_game_concepts_other_concepts_menu_boosts = game_concepts_other_concepts_menu.add_choice("Boosts", "concept_description_boosts")
    player.choice_game_concepts_other_concepts_menu_something_else = game_concepts_other_concepts_menu.add_choice("Something else", "concepts_menu_something_else")
    player.choice_game_concepts_other_concepts_menu_nothing = game_concepts_other_concepts_menu.add_choice("Nothing", "concepts_menu_nothing")

    # MAIN MENU
    game_concepts_main_menu = ExpandableMenu("What do you want to learn more about?", cancelable = True)
    player.choice_game_concepts_client_stats = game_concepts_main_menu.add_choice("Client stats", game_concepts_client_stats_menu)
    player.choice_game_concepts_player_stats = game_concepts_main_menu.add_choice("Player stats", game_concepts_player_stats_menu)
    player.choice_game_concepts_other_concepts = game_concepts_main_menu.add_choice("Other Concepts", game_concepts_other_concepts_menu)
  return

####
# PLAYER LABELS
####

label player_return_living_room:
    if current_location == downtown:
        change player energy by 10
    call forced_movement(living_room) from _call_forced_movement_59
    return

####
# CONCEPT LABELS
####

# used to populate Help and Tip content, when and as developed
# NEED: create a way to call these from a Help section
# need to figure out where to locate it - on Player icon?  Or Options icon?
# need to figure out how to structure it?  maybe as an expandable menu so new concepts intro'd by a mod can be added too?
label concepts_help_menu:
    call expandable_menu(game_concepts_main_menu) from _call_expandable_menu_4
    return

label concepts_menu_something_else:
    jump concepts_help_menu
    return

label concepts_menu_nothing:
    pass
    return

label concept_description_sos:
    sys "Sense of Self is a measure of how comfortable the client is being the person they, or their partner, want them to be.  The more internal conflict they feel, the lower this stat will be.  This stat will rise the more they come to feel like the way they behave, or are expected to behave, is the person they really are."
    sys "Sense of Self is usually the key stat for a successful training.  Typically, it will rise as the client learns they can accept or enjoy embracing the type of changes needed to achieve their training objective."
    return

label concept_description_desire:
    sys "Desire is, for most clients, a measure of how sexually attracted they are to you ([chelsea.name] is an exception).  Some training options only become available after a client’s Desire for you reaches certain thresholds.  It is typically associated with seduction-style activities."
    sys "Desire is usually the key stat in order to maintain a relationship with the client after their training is finished."
    return

label concept_description_submission:
    sys "Submission is a measure of how willing the client is to let you do what you want with her, simply because she knows it’s what you want.  Some training options only become available after a client’s Submission to you reaches certain thresholds.  It is typically associated with BDSM-style activities, which only some clients will ever be interested in."
    sys "Submission can sometimes allow you to maintain a relationship with a client after their training is finished.  It can also influence the nature of your on-going relationship."
    sys "For a few clients, a high Submission can help you to encourage them to take a Dominant role in your relationship, as their comfort with submission themselves makes it easier for them to accept and understand how and why you want to be submissive to them."
    return

label concept_description_resistance:
    sys "Resistance is a measure of how likely the client is to listen to your advice.  It’s a reverse stat, which declines as the client becomes more likely to trust you."
    sys "Some training options only become available after a client’s Resistance to you falls before certain thresholds.  In some cases, Resistance is compared to either Desire or Submission to determine whether training can proceed."
    sys "Resistance is usually used as a “gateway” to new training options, i.e. as an initial barrier that must be overcome for the training to proceed.  Occasionally it can affect whether a client will accept an on-going relationship with you."
    sys "For the Hypnotist, Resistance takes on greater importance, as some clients can be given an hypnotic trigger once their Resistance is low enough."
    return

label concept_description_money:
    sys "Money is mostly used to buy items.  Some actions also require Money."
    return

label concept_description_energy:
    sys "Energy is required for most actions.  Energy is reset to 100 at the start of each week.  If it ever hits 0, the week ends.  As a rule of thumb, you should have more than 15 energy before starting a training session with a client, and more than 30 energy if you think you may have sex with her during her training."
    sys "To engage in a Weekend training session, you need to have at least 25 Energy on Friday."
    return

label concept_description_reputation:
    sys "Reputation is required to attract new major and minor clients.  Major clients are organized into “waves”.  Only the first major client successfully trained each wave increases your Reputation, opening up access to the next wave."
    sys "The game is designed around the expectation that you should be able to succeed with one client per wave.  Success with 2, or even all 3, is possible, but very difficult. "
    return

label concept_description_minor_clients:
    sys "Minor clients provide the opportunity for some extra money and can open up access to new game content.  For example, the first two minor clients both offer the opportunity to gain access to the Club, although Club access can also be gained in a number of other ways, as well."
    sys "Minor clients usually don’t increase your Reputation, although a couple of them provide “fall back” Reputation that will kick in if you fail to successfully train any of the 3 major clients in a particular wave."
    return

label concept_description_modifiers:
    sys "When testing against a stat to see whether an action can proceed, some room items and player traits provide a bonus to the likelihood of success.  These ‘modifiers’ can facilitate training by opening up certain options earlier."
    return

label concept_description_boosts:
    sys "Player traits can provide bonuses that kick in when an action changes a stat, boosting the amount of the stat change.  These ‘boosts’ allow you to modify a stat more quickly, so that it takes fewer actions to reach critical thresholds."
    return

####
# CORE LABELS
####

# This label is called at the stat of each day.
# If you want to add stuff to start of the day add your own label to start_day_labels using 'day_label add to start your_label_here'.
label core_start_day:

  # Hide previous pics. Show location.
  reset_menu
  wt_image current_location.image

  # Week starting
  # Check clients training, hypnotic sessions and the like
  if day == 1:

    # Client visits
    python:
      player.client_visits_this_week = 0
      for c in all_clients:
        if c.status == 'on_training' and c.has_tag('trained_this_week'):
          player.client_visits_this_week += 1
      player.client_visits_count += player.client_visits_this_week

    # Money
    $ gained_money = sum(c.pay for c in all_clients if c.status == 'on_training' and c.has_tag('trained_this_week')) + player.extra_clients_fee_this_week
    $ player.extra_clients_fee_this_week = 0
    if gained_money > 0:
      $ notify_messages.append('You earned {} from your clients'.format(gained_money))
      $ player.money += gained_money

    if player.whore_income > 0:
      if player.has_tag('marilyn_whore_cut'):
        $ marilyn.temporary_count = player.whore_income * marilyn.whore_cut_percentage
        $ player.whore_income = marilyn.temporary_count
        $ marilyn.temporary_count = 0
        $ notify_messages.append('You earned {} from being a pimp after paying Marilyn her cut'.format(player.whore_income))
      else:
        $ notify_messages.append('You earned {} from being a pimp'.format(player.whore_income))
      $ player.money += player.whore_income
      # $ player.whore_income = 0  ## later, after notify
    if player.domme_income > 0:
      $ notify_messages.append('You earned {} from managing a Domme'.format(player.domme_income))
      $ player.money += player.domme_income
      # $ player.domme_income = 0
    if player.investment_income > 0:
      $ notify_messages.append('You earned {} from your investments'.format(player.investment_income))
      $ player.money += player.investment_income
      # $ player.investment_income = 0

  # Check daily tags
  python:
    for person in all_clients + all_minor_characters + [player]:
      person.tags -= person.remove_tags_daily

  # Cheking available clients and messages
    # Initial variables
    active_client_list = []
    available_client_list = []
    availability_check_dict = {}
    prospect_list = []
    prospect_check_dict = {}
    player.messages = 0

    # Filling out necessary lists
    for c in all_clients:
      if c.status == 'available_to_be_client':
        available_client_list.append(c)
      elif c.status == "on_training" or (c.status == "waiting_on_message" and not c.is_prospect):
        active_client_list.append(c)
      elif c.status == 'prospect':
        prospect_list.append(c)
    prospect_list.extend([mc for mc in all_minor_characters if mc.status == "prospect"])

    # Checking messages
  if day == 1:
    python:
      for prospect in prospect_list:
        # If we have a label that can check prospect availability we run it
        if renpy.has_label(prospect.short_name + "_prospect_check"):
          prospect_check_dict[prospect] = prospect.short_name + "_prospect_check"
        # If we don't we do a simply reputation check and add that to the dict
        elif week + 1 >= prospect.week_available and prospect.prospect_min_reputation <= player.reputation:
          prospect_check_dict[prospect] = True

    # Check if there are open training slots and clients that can use them
      for client in available_client_list:

        # Making clients avaialable depending on selection type (Exception for Rep 0 to allow for Ivy)
        if selection_type == "default" or player.reputation < 0:
          # If we have a label that can check availability we add it to the check dict
          if renpy.has_label(client.short_name + "_availability_check"):
            availability_check_dict[client] = client.short_name + "_availability_check"
          # If we don't dont we do a simply reputation check and add that to the dict
          elif client.min_reputation <= player.reputation:
            availability_check_dict[client] = True

        elif selection_type == "random" or selection_type == "choice":
          availability_check_dict[client] = True

        else:
          custom_selection = True

    # Calling Custom Avalability Check Process
    if custom_selection:
      call safe_call(selection_type + '_availability_check', fallback = False) from _call_safe_call_5

    # We call all the labels in the check dict an keep only the results that are oked
    call for_labels_dictionary_check(prospect_check_dict, list(prospect_check_dict.keys())) from _call_for_labels_dictionary_check
    call for_labels_dictionary_check(availability_check_dict, list(availability_check_dict.keys())) from _call_for_labels_dictionary_check_1

    python:
      # If we have messages on the prospect side we activate them
      for prospect in prospect_check_dict.keys():
        player.messages += 1
        prospect.change_status("waiting_on_message")
        prospect.current_client_action.name = "New Message"

      # While we have more slots than clients and at least one available client we move them to the active pool
      while len(active_client_list) < player.training_slots and len(availability_check_dict) > 0:
        # player.messages += 1 # think this is giving false new message notifications, moved below to under if client
        client = None

        # Selecting clients depending on selection type (Exception for Rep 0 to allow for Ivy)
        if selection_type == "default" or player.reputation < 0:
          client = renpy.random.choice(availability_check_dict.keys())

        elif selection_type == "random":
          if len([c for c in all_clients if c.status == "on_training"]) > 0:
            active_client_list = [None] * player.training_slots
          else:
            client = renpy.random.choice(availability_check_dict.keys())

        elif selection_type == "choice":
          renpy.hide_screen('advance_time') # NOTE: required because otherwise Advancing time screen blocks access to the following menu

          if len([c for c in all_clients if c.status == "on_training"]) > 0:
            active_client_list = [None] * player.training_slots

          else:
            while True:
              title = "Add Client to Wave:"
              client = renpy.display_menu(items = [(p.full_name, p) for p in availability_check_dict.keys()])

              title = "Are you sure you want to add {} to this wave?".format(client.name)
              if renpy.display_menu(items = [("Yes", True), ("No", False)]):
                break

        else:
          # It's a kind of magic - Queen
          globals()[selection_type + "_selection_type"]()

        if client:
          client.change_status("waiting_on_message")
          player.messages += 1
          del availability_check_dict[client]
          active_client_list.append(client)

      # if we run out of clients and avaialble client then we probably need rep.
      if len(active_client_list) + len(availability_check_dict) == 0:
        renpy.call('core_rep_check')

  # Notify things in the calendar
  if total_days in calendar_dict:
    python:
      for note in calendar_dict[total_days]:
        notify_messages.append("- " + note[1])

  # Week starting part 2
  # Checks clients training, hypnotic sessions and the like
  if day == 1:
    python:
      for person in all_clients + all_minor_characters + [player]:

        person.stats['hypno_sessions_this_week'] = 0
        person.tags -= person.remove_tags_weekly

      end_training_labels = []
      reject_client_labels = []
      for client in all_clients:
        if client.status == "on_training":
          client.training_period -= 1

          if client.training_period <= 0:
            client.change_status("post_training")
            end_training_labels.append(client.short_name + "_end_training")

        elif client.status == "waiting_on_message":
          client.wait_for_message_period -= 1

          if client.wait_for_message_period < 0:
            client.change_status("rejected")
            reject_client_labels.append(client.short_name + "_rejected")

    call for_call_labels(label_list = end_training_labels) from _call_for_call_labels_3
    call for_call_labels(label_list = reject_client_labels) from _call_for_call_labels_4

    # Time & Energy
    $ week += 1
    $ player.energy = player.max_energy

  # then we set variables back to 0
  $ player.whore_income = 0
  $ player.domme_income = 0
  $ player.investment_income = 0
  # note: don't need to reset gained income because of the way's it's calc'd, and extra client income lareay reset because it doesn't get displayed

  # Notify Messages
  if player.messages == 1:
    notify "You received a new message today."
  elif player.messages > 1:
    notify "You received new messages today."
  $ player.messages = 0

  if repeating_action or 'repeating_action' in start_day_labels.label_list:
      notify
  else:
      $ notify(True)
  return

# This label is called at the end of each day.
# If you want to add stuff to end of the day add your own label to using 'day_label add to end your_label_here'.
label core_end_day:

  # End day label calling
  call for_call_labels(label_list = [person.short_name + '_end_day' for person in get_people()], show_labels = False) from _call_for_call_labels_18
  call for_call_labels(label_list = [l.short_name + '_end_day' for l in all_locations], show_errors = False) from _call_for_call_labels_19

  # If we are out of energy or we were asked to, we end the week
  if player.energy <= 0 or end_week:
    if player.energy <= 0:
      sys "You have run out of energy for the week. You spend the rest of the week recovering."
    $ end_week = False
    $ total_days += 5 - day
    $ day = 5

  # End week label calling
  if day == 5 and week > 0:
    call for_call_labels(label_list = [person.short_name + '_end_week' for person in get_people()]) from _call_for_call_labels_20
    call for_call_labels(label_list = [l.short_name + '_end_week' for l in all_locations], show_errors = False) from _call_for_call_labels_21

  # Check temp modifiers
  python:
      for a in all_actionables:
          a.resolve_temp_mod()

  # Day is over
  $ end_day = False
  $ day += 1
  $ total_days += 1

  # Move Player to Living Room Every Day
  call forced_movement(living_room) from _call_forced_movement_1

  # Week over
  if day == 6:
    notify 'Week has ended'
    $ day = 1
  else:
    notify 'Day has ended'
  notify

  # Adding a delay to resolve delayed labels
  # if delayed_labels:
  #     pause 0.1 + 0.1 * len(delayed_labels)
  return

# This label is called when the player runs out of ways to obtain reputation.
# Player can obtain new ways to gain rep, continue playing as is, or end the game.
label core_rep_check:
  # Currently, only the 3rd wave of clients are available, so the max_reputation is 3
  #$ player.max_reputation = 4
  $ player.max_reputation = 3
  if player.reputation < player.max_reputation:
    if tracy.reference == 1:
      sys "You've run out of clients and prospects."
      sys "Fortunately, Tracy's husband offered to provide you a reference if you need one.  You take him up on his offer, boosting your reputation."
      $ tracy.reference = 2
      change player reputation by 1 notify
    else:
      add tags 'rep_needed' to player
      # if not player.has_tag("rep_from_marilyn"):
      #   if marilyn.orgasm_count > 0 or marilyn.favour > 0:
      #     add tags 'rep_needed' to player
      if not player.has_tag("rep_from_club_wife") and gloria.session > 4:
        add tags 'something_to_discuss' to gloria
        # add tags 'rep_needed' to player
      # if not player.has_tag("rep_from_lawyer") and player.has_tag("lawyer_on_retainer"):
      #   add tags 'rep_needed' to player
      # if player.has_tag("rep_needed"):
      #   sys "You've run out of clients and prospects."
      #   sys "To increase your reputation further, you could try checking on your network of contacts."
      else:
        if not player.has_tag('no_rep_left'):
          sys "You've run out of clients and prospects.  If you're lucky, though, you may figure out a way to earn more reputation from your network of contacts."
          sys "Otherwise, your career as a Wife Trainer is over.  You can still continue to explore your existing relationships, however."
          # sys "You've run out of clients and prospects, and have no way to increase your reputation further.  Your career as a Wife Trainer has come to an end, although you can continue to explore your existing relationships."
          # sys "If you're lucky, you may even figure out a way to earn some new reputation and get your career going again."
          add tags 'no_rep_left' to player
        # $ title = "Keep playing?"
        # menu:
          # "Yes":
            # pass
          # "No (End Game)":
            # jump end_game
  ################ REMOVE THE FOLLOWING CONTENT WHEN GAME IS COMPLETED ################
  elif player.reputation == 3 and not player.has_tag('no_rep_left'):
    sys "Congratulations!  You've reached the maximum current reputation in the game and there are no additional major clients to work with!"
    sys "You may continue the game to explore continuing content with existing characters."
    add tags 'no_rep_left' to player
    # $ title = "Keep playing?"
    # menu:
      # "Yes":
        # pass
      # "No (End Game)":
        # jump end_game
  return

label consider_contract(client, new_name):
  $ title = "Do you agree to train [client.full_name]?"
  $ yesno = renpy.display_menu(items = [("Yes", True), ("Wait to Reply", 'wait_reply'), ("No", False)])

  if yesno == 'wait_reply' and not client == ivy:
    $ client.current_client_action.name = new_name
    if not get_note(client.current_note) or get_note(client.current_note)[1] != "{} offer ends".format(client.name):
      $ client.current_note = add_note((client.wait_for_message_period + 1) * 5, "{} offer ends".format(client.name), exact = True)
    sys "You have until the end of week [client.accept_limit] to accept the assignment."
  elif yesno:
    $ client.change_status("on_training")
  else:
    $ client.change_status("rejected")
    call expression (client.short_name + "_rejected") from _call_expression_5

  if not any_client(with_status = 'waiting_on_message'):
    reset_menu

  return

label arrange_weekend:

  $ title = "Who are you going to train during the weekend?"
  $ selected_client = renpy.display_menu(items = [(p.name, p) for p in get_people(with_status = "on_training", not_tagged_with_any = ['first_visit']) if p.can_be_interacted] + [('Cancel', False)])

  if selected_client:
    $ current_target = selected_client
    #summon current_target
    call expression (current_target.short_name + "_weekend") from _call_expression_2
    #if current_target.status == 'on_training':
    #  dismiss current_target
    #end_day

  return

# label watch_girlfriend:
#   $ title = "Watch Your Girlfriend"
#   $ selected_girlfriend = renpy.display_menu(items = [(p.name, p) for p in get_people(tagged_with_any = ['girlfriend', 'hypno_girlfriend'])] + [('Cancel', False)])
#
#   if selected_girlfriend:
#     $ current_target = selected_girlfriend
#     call expression (current_target.short_name + "_watch") from _call_expression_3
#   return

label check_whores:
  call for_call_labels(label_list = [whore.short_name + "_check_whore" for whore in get_people(tagged_with_all = ['whore'])]) from _call_for_call_labels_22
  wt_image current_location.image
  return

## Player Labels

# Player Other
# Energy Label
label player_energy_negative_change:
  add tags 'used_energy' to player
  return

label player_energy_positive_change:
  return

label player_energy_no_change:
  return

## LOCATION LABELS
# BACKYARD
label byd_examine:
    return

# BASEMENT
label ba_examine:
  "{nw}"
  if "dead_bonsai" in basement.tags:
    "The housewarming gift from your neighbor, Nicole, used to be down here, but it died from lack of sunshine.{nw}"
  extend "It's dark and gloomy down here."
  return

label ba_no_access:
  return

label ba_enter:
  return

label ba_exit:
  return

# BATHROOM
label bth_examine:
    return

# BEDROOM
label be_examine:
  "Your bedroom is reserved for your private life.  You entertain clients in the other rooms of your house."
  return

label be_no_access:
  return

label be_enter:
  return

label be_exit:
  return

# BOUDOIR
label bo_examine:
  "You've set this room up to inspire the romantic sentiments of your clients."
  $ boudoir.submission_total = boudoir.moded_stat('submission_mod')
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.added_by_items('desire_mod')
  if boudoir.added_desire >= 30:
    "The room is looking very nice."
  elif boudoir.added_desire >= 20:
    "You've made a nice start on setting up the room."
  elif boudoir.added_desire >= 5:
    "You've just started to fix the room up."
  elif boudoir.added_desire >= 0:
    "Unfortunately, the room is currently devoid of inspirational items."
  "Being in this room will temporarily increase client Desire by [boudoir.desire_total] and Submission by [boudoir.submission_total]."
  return

label bo_no_access:
    return

label bo_enter:
    # $ boudoir.desire_mod = 0 if boudoir.added_by_items('desire_mod') > 0 else 5
    return

label bo_exit:
  return

# DARK ARTS STORE
# See dark_arts_store.rpy

# DOWNTOWN
label do_examine:
    "It's not the busiest city in the world, but there's still enough traffic to make getting in and out of the downtown a time consuming venture."
    return

label do_no_access:
  return

label do_enter:
  return

label do_exit:
  return

# DUNGEON
label du_examine:
  "It's fun to watch your guests the first time you show them this room."
  $ dungeon.desire_total = dungeon.moded_stat('desire_mod')
  $ dungeon.submission_total = dungeon.moded_stat('submission_mod')
  $ dungeon.added_submission = dungeon.added_by_items('submission_mod')
  if dungeon.added_submission >= 30:
    "The room is deliciously terrifying."
  elif dungeon.added_submission >= 15:
    "The room is starting to come together."
  elif dungeon.added_submission >= 5:
    "You're just started setting this room up."
  elif dungeon.added_submission >= 0:
    "Unfortunately, the room is currently devoid of inspirational items."
  "Being in this room will temporarily increase client Desire by [dungeon.desire_total] and Submission by [dungeon.submission_total]."
  return

label du_no_access:
    return

label du_enter:
    # $ dungeon.submission_mod = 0 if dungeon.added_by_items('submission_mod') > 0 else 5
    return

label du_exit:
    return

# EROS STORE
# See eros_store.rpy

# GARAGE
label gar_examine:
    return

# GYM
label gym_examine:
  return

label gym_no_access:
  return

label gym_enter:
  return

label gym_exit:
  return

# JEWELRY STORE
# See julia.rpy

# KITCHEN
label ki_examine:
    return


# LIVING ROOM
label lr_examine:
    #$ living_room.resistance_total = living_room.moded_stat('resistance_mod')
    #"Your tastefully decorated living room.  Clients tend to be more at ease during sessions here.  Being in this room will temporarily decrease client Resistance by [living_room.resistance_total]."
    "Your tastefully decorated living room."
    return

label lr_no_access:
    return

label lr_enter:
    return

label lr_exit:
    return

# OFFICE TOWER
label ot_examine:
    "A busy downtown office tower.{nw}"
    if week >= 12 and bank.status == 1:
        extend " A branch of Global Trust Bank is located on the main floor."
    elif bank.status == 2:
        extend " The old Global Trust Bank branch has a new sign:  'First Nationalized Bailout Bank'"
    else:
        extend " "
    return

label ot_no_access:
  return

label ot_enter:
  return

label ot_exit:
  return

# OUTDOORS
label od_examine:
  return

label od_no_access:
  return

label od_enter:
  return

label od_exit:
  return

# THE CLUB
# See club.rpy

# THE CRITTER EMPORIUM
# See critter_emporium.rpy

# THE STEEL TRAP
# See steel_trap.rpy

## ITEM LABELS
# Bank Pen
label bap_examine:
  wt_image pen
  "A nice gift from Bethany the Banker for being an elite customer.  It writes super great!"
  sys "And is super useless - at least at this point in the game."
  return

label bap_throw_away:
  $ title = "Do you really want to get rid of this nice pen?"
  menu:
    "Yes, throw it away":
      rem 1 bank_pen from player notify
    "No":
      pass
  return

# Book
## moved to DAS script
# label boo_examine:
#     "You pick up the book from the shelf.  It looks old, but someone has recently added a new chapter.  The title page reads \"Tales of the Drunken Cowboy\".  Sounds like a really bad western."
#     player.c "Does this have any power?"
#     das_proprietor.c "You'd be amazed at how much time it can make disappear."
#     "You put it back.  You've been making plenty of time go away as it is.  The woman behind the counter smiles."
#     das_proprietor.c "It will be waiting for you when you're finished with this reality."
#     "You're not sure whether you're unnerved or comforted by that thought."
#     # reset_menu
#     # rem 1 book from dark_arts_store no_message
#     return

# Butt Plug
label bp_examine:
  if player.has_item(butt_plug):
    wt_image butt_plug_inventory
    "A brand new butt plug. You just need to find the right woman to give it to."
  return

label give_bp_fallback:
    "Save this for someone else."
    return

# Ceiling Mirror
label cm_examine:
  if boudoir.has_item(ceiling_mirror):
    "What you see depends on the company you keep."
  return

# Chastity Belt
label cb_examine:
  if player.has_item(chastity_belt):
    wt_image chastity_belt_inventory
    "The perfect accessory for the right woman."
  return

label give_cb_fallback:
    "Save this for someone else."
    return


# Dildo
label di_examine:
    if player.has_item(dildo):
        wt_image dildo_inventory
        "A brand new dildo. You just need to find the right woman to give it to."
    return

label give_di_fallback:
    "Save this for someone else."
    return

# Domme Whip
label dw_examine:
    if player.has_item(domme_whip):
        wt_image dw_image
        "This looks like it will hurt.  The Domme in your life will likely enjoy using this on you.  Whether you enjoy it, too, will probably depend on her mood when she's using it on you."
    return

label give_dw_fallback:
    "Wait for the right time and person to give this to.  Then be ready to scream."
    return


# Fetch Toy
label ft_examine:
  if current_location == bedroom:
    wt_image fetch_toy_bedroom
  if player.has_item(fetch_toy):
    "Your pet will be so excited the next time you let her play with this."
  return

label use_ft_fallback:
    "You shouldn't try to play fetch with someone who isn't your pet."
    return


# Floggers and Paddles
label fl_examine:
  if dungeon.has_item(floggers):
    "You've acquired a wide variety of means to hurt someone."
  return

# Fluffy Cuffs
label fc_examine:
  if boudoir.has_item(fluffy_cuffs):
    "They look innocent, but they're surprisingly effective."
  return

# Fuck Machine
label fm_examine:
  if dungeon.has_item(fuck_machine):
    "It does what it says it does, and it does it well."
  return


# Gags
label ga_examine:
  if dungeon.has_item(gags):
    "Physical restraints are fun, but taking away the power of speech creates a whole different feel of helplessness."
  return

# Leash
label le_examine:
    if current_location == bedroom:
        wt_image leash_bedroom
    if player.has_item(leash):
        if lee.has_tag('accepted_leash') and lee.has_tag('domme'):
            "The leash that [lee.her_respect_name] sometimes uses on you"
        else:
            "Your pet is no doubt eagerly awaiting her next walk."
    return

label use_le_fallback:
    "Someone else may enjoy this more."
    return


# Lingerie
label li_examine:
  if player.has_item(lingerie):
    wt_image lingerie_inventory
    "You're looking forward to seeing this on the right woman."
  return

label give_li_fallback:
    "Save this for someone else."
    return

# Love Potion
## moved to DAS
# label lp_examine:
#     if current_location == dark_arts_store and dark_arts_store.has_item(love_potion):
#         wt_image love_potion_store_1
#         "The little bottle of red fluid is mesmerizing. Smoke rises around it as tiny heart shape lights float upwards."
#         sys "Item is now available for purchase."
#         rem 1 love_potion from dark_arts_store no_message
#         $ dark_arts_store.add_store_item(love_potion, price = 500, send_to = player, with_examine = True, seen = True)
#     elif player.has_item(love_potion):
#         "Number of Love Potions: [player.love_potion]"
#     return

# Scented Oils
label so_examine:
  if boudoir.has_item(scented_oils):
    "With your collection, you can set just the right mood for any visitor."
  return

# Silk Sheets
label ss_examine:
  if boudoir.has_item(silk_sheets):
    "They aren't practical, but they look great and feel even better against the skin."
  return

# Suspension Gear
label sg_examine:
  if dungeon.has_item(suspension_gear):
    "Good for when you want your companion to hang out for a while."
  return

# Water Bowl
label wb_examine:
  if current_location == bedroom:
    wt_image water_bowl_bedroom
  if player.has_item(water_bowl):
    "Your pet should be able to drink comfortably from this."
  return

label use_wb_fallback:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
    return


# Beer labels
# label bob_find:
#   if renpy.random.randint(0, 99) < 0:
#     "A friend sees you walking around Downtown and invites you a beer."
#     add 1 beer to player notify
#     $ renpy.say('Friend', "Here, take one for the way.")
#     $ downtown.enter_labels.remove('bob_find')
#   return
#
# label bob_drink:
#   change player energy by energy_short notify
#   "The beer is incredibly refreshing!"
#   rem 1 beer from player notify
#   return
#
# label bob_bonsai:
#   wt_image housewarming_gift
#   "You 'water' the bonsai with beer. You see it growing stronger before your very eyes.\nSuddenly a holographic image projects from it!"
#   rem 1 beer from player
#   wt_image tree_alone
#   db "Your sacrifice is accepted, traveler!\nThis surely will make the next update come faster."
#   change player energy by 30 notify
#   wt_image housewarming_gift
#   "Just as fast as it appeared the image disappear and the bonsai goes back to normal. Clearly an hallucination caused for playing video games until late hours of the night."
#   wt_image clear
#   return

label image_size_test:
  wt_image 300x300
  "Wait"
  wt_image 700x700
  "Wait"
  wt_image 800x700
  "Wait"
  wt_image 800x800
  "Wait"
  wt_image 800x900
  "Wait"
  wt_image 1000x600
  "Wait"
  wt_image 1000x700
  "Wait"
  wt_image 1000x800
  "Wait"
  wt_image 1000x900
  "Wait"
  wt_image 1000x1000
  "Wait"
  wt_image 1100x700
  "Wait"
  wt_image 1100x800
  "Wait"
  wt_image 1100x900
  "Wait"
  wt_image 1100x1000
  "Wait"
  wt_image 1100x1100
  "Wait"
  return
