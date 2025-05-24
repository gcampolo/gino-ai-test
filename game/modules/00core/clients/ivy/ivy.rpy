## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Wifetrainer

## Package Register
# This registers the modded client to the initialized package above
register ivy_pregame 10 in core as "Ivy the Intro Wife"

# Pregame
label ivy_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Ivy the Intro Wife (Asa Akira)")]

    ## Client Definition
    # FFFFFF is the color of the character's text in Hexadecimal
    # Must have an client_name_image.jpg and an client_name_portrait.jpg files associated with this character
    # Note: min_reputation handles at which wave this character can be trained:
      # -1: Ivy
      # 0: Chelsea, Elsa, Jasmine
      # 1: Donna, Lauren, Terri
      # 2: Alexis, Becky Sue, Sarah
      # 3: Wife Trainer 3 Planned Clients
      # 4: Unknown
    #old white font color: ivy = Person(Character("Ivy", who_color="#FFFFFF", what_color="#FFFFFF"), "ivy", cut_portrait = True, prefix = "", suffix = "the Intro Wife", resistance = 80, training_period = 5, hypno_trigger_resistance_threshold = 20, hypno_trigger_sessions_threshold = 2, min_reputation = -1)
    ivy = Person(Character("Ivy", who_color="#e5d999", what_color="#e5d999"), "ivy", cut_portrait = True, prefix = "", suffix = "the Intro Wife", resistance = 80, training_period = 5, hypno_trigger_resistance_threshold = 20, hypno_trigger_sessions_threshold = 2, min_reputation = -1)
    ivy.trigger_phrase = "Trained wives do as they're told"

    # Other Characters
    ### Note: When adding tertiary characters, be careful not to use an already existing name
    ### try adding _client_name to the end of their definition as to not conflict with other characters that might share that name

    ### This is left as an example tertiary character definition ###
    ## Navy
    husband_ivy = Character("Ivy's Husband", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)
    ### This is left as an example tertiary character definition ###

    ## Actions
    # Hypno Action Definition
    ivy.add_hypno_actions(implant = False) # this adds all the standard options

    # Add Hypno Actions
    ivy.crawling_hypno_action = ivy.add_action("Crawling", label = "_crawling_hypnosis", context = "_hypnosis", condition = "ivy.status == 'on_training' and ivy.has_tag('discussed_crawling') and not ivy.has_tag('hypno_re_crawling') and ivy.crawl_count == 0")
    ivy.anal_hypno_action = ivy.add_action("Anal sex", label = "_anal_hypnosis", context = "_hypnosis", condition = "ivy.status == 'on_training' and ivy.has_tag('discussed_anal') and not ivy.has_tag('hypno_re_anal') and ivy.anal_count == 0")
    ivy.stripping_hypno_action = ivy.add_action("Stripping", label = "_stripping_hypnosis", context = "_hypnosis", condition = "ivy.status == 'on_training' and ivy.has_tag('discussed_stripping') and not ivy.has_tag('hypno_re_stripping') and not ivy.has_tag('stripped_for_you')")
    ivy.domme_hypno_action = ivy.add_action("Taking charge", label = "_domme_hypnosis", context = "_hypnosis", condition = "ivy.status == 'on_training' and ivy.has_tag('discussed_taking_charge') and ivy.domme_comfort < 3 and not ivy.has_tag('hypno_re_domme')")

    # Training Action Definitions
    ivy.action_talk = ivy.add_action("Talk to her", label = "_talk", condition = "ivy.can_be_interacted and not ivy.has_tag('successful_talk_today')")
    ivy.action_train_her = ivy.add_action("Train her", label = "_train_her", condition = "ivy.can_be_interacted and not ivy.has_tag('first_visit') and ivy.status == 'on_training' and current_location in session_locations")
    ivy.action_seduce = ivy.add_action("Seduce her", label = "_seduce", condition = "ivy.can_be_interacted and not ivy.has_tag('first_visit') and ivy.status == 'on_training' and current_location in session_locations")
    ivy.action_discipline = ivy.add_action("Discipline her", label = "_discipline", condition = "ivy.can_be_interacted and not ivy.has_tag('first_visit') and ivy.status == 'on_training' and current_location in session_locations")
    # note that in addition to the above, Ivy also has a "Train Her" expandable menu

    # Default exit action
    ivy.action_end_session = ivy.add_action("Send her home", label = "_end_session", condition = "not ivy.has_any_tag('first_visit', 'shut_off_end_session') and ivy.in_area('house')")

    # Post-Training Action Definitions
    ivy.action_watch_her_dance = ivy.add_action("Watch her dance", label = '_watch_her_dance', condition = "ivy.status == 'post_training' and stage.is_here and ivy.has_tag('showgirl') and not ivy.has_tag('watched_today')")
    ivy.action_domme_visit = ivy.add_action("Submit to her", label = '_domme_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('domme_visit_now')")
    ivy.action_submissive_visit = ivy.add_action("Dominate her", label = '_submissive_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('submissive_visit_now')")
    ivy.action_sex_visit = ivy.add_action("Have sex with her", label = '_sex_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('sex_visit_now')")
    ivy.action_strip_visit = ivy.add_action("Watch her strip for you", label = '_strip_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('strip_visit_now')")
    ivy.action_strip_lingerie_visit = ivy.add_action("Ask her to strip out of her lingerie", label = '_strip_lingerie_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('strip_visit_now') and ivy.has_tag('gave_her_sexy_lingerie')")
    ivy.action_crawl_visit = ivy.add_action("Tell her to crawl for you", label = '_crawl_visit', condition = "ivy.can_be_interacted and ivy.status == 'post_training' and current_location in session_locations and ivy.has_tag('crawl_visit_now')")
    ivy.action_use_trigger = ivy.add_action("Use her trigger", label = '_trigger_used', condition = "ivy.can_be_interacted and ivy.has_tag('continuing_actions') and ivy.has_tag('trigger_implanted') and current_location in session_locations")
    #ivy.action_send_home = ivy.add_action("Send her home", label = '_send_home', condition = "ivy.status == 'post_training' and current_location in session_locations")

    ######## EXPANDABLE MENUS #######
    ## Training Menu Definitions
    ivy_regular_training_menu = ExpandableMenu("What do you want to train her to do?")
    ivy.choice_regular_training_receive_pleasure = ivy_regular_training_menu.add_choice("Receive pleasure", "ivy_train_experience_pleasure")
    ivy.choice_regular_training_blowjobs = ivy_regular_training_menu.add_choice("Give pleasure", "ivy_train_blowjobs", condition = "not ivy.has_tag('bj_training')")
    ivy.choice_regular_training_new_positions = ivy_regular_training_menu.add_choice("Have sex in adventurous positions", "ivy_train_new_positions", condition = "not ivy.has_tag('had_adventurous_sex')")
    ivy.choice_regular_training_crawl = ivy_regular_training_menu.add_choice("Crawl", "ivy_train_crawl", condition = "ivy.has_tag('discussed_crawling')")
    ivy.choice_regular_training_strip = ivy_regular_training_menu.add_choice("Strip", "ivy_train_strip", condition = "ivy.has_tag('discussed_stripping') and not ivy.has_tag('stripped_for_you') and not ivy.has_tag('already_strip_trained_today') and not ivy.has_tag('will_not_strip')")
    ivy.choice_regular_training_anal = ivy_regular_training_menu.add_choice("Do anal", "ivy_train_anal", condition = "ivy.has_tag('discussed_anal') and ivy.anal_count == 0")
    ivy.choice_regular_training_serve = ivy_regular_training_menu.add_choice("Serve", "ivy_train_serve")
    ivy.choice_regular_training_take_charge = ivy_regular_training_menu.add_choice("Take charge", "ivy_train_take_charge", condition = "ivy.has_tag('discussed_taking_charge')")
    ## below not needed as Cancel is active
    #ivy.choice_regular_training_nothing = ivy_regular_training_menu.add_choice("None of these", "ivy_train_nothing")

    ## Weekend Action Definitions
    ivy_weekend_training_menu = ExpandableMenu("What do you have in mind for Ivy this weekend?", pre_label = 'ivy_pre_weekend', post_label = 'ivy_post_weekend')
    # Note: decided against allowing weekend hypnosis for her
    #ivy.choice_weekend_hypnotize = ivy_weekend_training_menu.add_choice("Hypnotize her", "ivy_weekend_hypnosis", condition = "player.can_hypno(ivy)")
    ivy.choice_weekend_strip_club = ivy_weekend_training_menu.add_choice("Take her to a strip club", "ivy_weekend_strip_club")
    ivy.choice_weekend_sex_show = ivy_weekend_training_menu.add_choice("Take her to a sex show", "ivy_weekend_sex_show")
    ivy.choice_weekend_date = ivy_weekend_training_menu.add_choice("Take her on a date", "ivy_weekend_date")

    ## Continuing Visit Action Definitions
    ivy_continuing_actions_visit_menu = ExpandableMenu("What do you want to do during her visit?")
    ivy.choice_continuing_actions_visit_domme = ivy_continuing_actions_visit_menu.add_choice("Have her Domme you", "ivy_visit_domme_start", condition = "ivy.has_tag('dommed_you')")
    ivy.choice_continuing_actions_visit_dungeon = ivy_continuing_actions_visit_menu.add_choice("Take her to your dungeon", "ivy_visit_dungeon_start", condition = "ivy.has_tag('ready_for_dungeon')")
    ivy.choice_continuing_actions_visit_submissive = ivy_continuing_actions_visit_menu.add_choice("Have her submit to you", "ivy_visit_submissive_start", condition = "ivy.submission > 40")
    ivy.choice_continuing_actions_visit_crawl = ivy_continuing_actions_visit_menu.add_choice("Have her crawl", "ivy_visit_crawl_start", condition = "ivy.crawl_count > 0")
    ivy.choice_continuing_actions_visit_strip = ivy_continuing_actions_visit_menu.add_choice("Have her strip for you", "ivy_visit_strip_start", condition = "ivy.has_tag('stripped_for_you')")
    ivy.choice_continuing_actions_visit_sex = ivy_continuing_actions_visit_menu.add_choice("Have sex with her", "ivy_visit_sex_start")
    # not needed as Cancel is active
    #ivy.choice_continuing_actions_visit_nothing = ivy_continuing_actions_visit_menu.add_choice("Nothing (cancel request)", "ivy_visit_nothing")

    ## Tags
    # Common Character Tags

    ### Note: The tag 'no_hypnosis' prevents all hypnotism until the tag is removed
    ### Note: The tag 'likes_boys' can also be accompanied by 'likes_girls' if the character is bi-sexual
    ivy.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    ### This is left as an example location definition ###
    # Lauren's Office
    # Note: Player can't visit this location until connections are added
    #lauren_office = Location("Lauren the Cheater's Office", 'lco', cut_portrait = True, enter_break_labels = ['lco_no_access'], enter_labels = ['lco_enter'], exit_labels = ['lco_exit'], area = 'offices')
    # Note: These connections link the new location to an existing location; in this case, the office_tower
    #lauren_office.add_connections(office_tower)
    #office_tower.add_connections(lauren_office)
    ### This is left as an example location definition ###
    living_room.exit_break_labels.append('ivy_check_messages_first')

    ## Other
    # Note: Lets this character be a Major Client
    ivy.change_status("available_to_be_client")

    # Start Day Events
    start_day_labels.append('ivy_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    ivy.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_masturbation_count', 'hypno_orgasm_count', 'hypno_sex_count','hypno_swallow_count', 'random_number')
    ### These are left as example variable definitions ###
    #client_name.add_stats_with_value('maintain_week_gf', 'maintain_week_sg', 'random_number')
    ### These are left as example variable definitions ###

    # Character Specific Variables
    ivy.add_stats_with_value('crawl_count', 'domme_boots_outfit', 'domme_comfort', 'domme_you_outfit_count', 'facesitting_outfit', 'goodgirlspanking_outfit', 'normal_sex_show_outfit', 'ordered_food_for_her_count', 'seduction_count', 'serve_count', 'sex_show_count', 'sex_training_count', 'show_count', 'showgirl_outfit', 'strapon_outfit', 'strapon_bj_outfit', 'strip_show_count', 'stripper_discussion', 'submissive_visit_timer', 'weekend_training_sessions')
    # stripper_discussion key: 0: not started; 1: suggested and waiting for Club access; 2: discussion over, not stripper; 3: discussion over, stripper but not yet chatted; 4: chatted with her at Club

    # Special variables for first wave client selection
    ivy.add_stats_with_value('tier2',value = 3)
    ivy.add_stats_with_value('tier3',value = 3)

  return

# Initial Contact Message
label ivy_message:
    wt_image current_location.image
    husband_ivy "{i}I saw your profile online and I admire your confidence.  Offering to train other men's wives is an audacious proposition.{/i}"
    husband_ivy "{i}I don't think my wife, Ivy, requires any training, but when I told her about your service, the idea of me sending her to be trained got her quite excited.{/i}"
    husband_ivy "{i}So I'm going to 'make' her spend time with you for the next four weeks.  If she enjoys herself or learns something new, I'll post good things about you.  Maybe that'll jump-start your business.{/i}"
    husband_ivy "{i}PS We have an open relationship, so whatever she agrees to do with you is fine with me.  Don't think this is an easy booty-call, though.  It was the idea of being trained that got her excited, so you'll need to prove you can actually be a wife trainer.{/i}"
    sys "Ivy's an introductory client and her training can be skipped. If you want to jump directly to the next tier of clients, simply reject her husband's offer."
    call ivy_message_finish from _call_ivy_message_finish
    return

label ivy_message_finish:
    call consider_contract(ivy, "Reply to [ivy.full_name]'s Husband") from _call_consider_contract_9
    if yesno == 'wait_reply':
        sys "Normal clients allow you some time to accept or reject their offer, but Ivy is handled differently.  Either agree to train her or reject her husband's offer to skip to the next group of clients."
        jump ivy_message_finish
    if yesno == True:
        sys "You accept the assignment.  You have until the end of week [ivy.training_limit] to complete it."
        if not player.has_tag('tutorial_message'):
            add tags 'tutorial_message' to player
            sys "You may hold one evening session each week with each client, which can be any day from Monday to Thursday, but only one client per day.  If you have at least [energy_long.value] Energy left on Friday, you may also schedule a weekend session with a client of your choice."
    else:
        "You skip the introductory wife and go straight to the first wave of clients. Your money has been increased."
        $ player.reputation = 0
        $ player.money += 100
        $ week = 0
        end_week
    # call ivy_first_wave_client_choice
    $ living_room.exit_break_labels.remove('ivy_check_messages_first')
    return

label ivy_first_wave_client_choice:
    if yesno == True:
        $ title = "Which clients do you want in the first wave after Ivy?"
    else:
        $ title = "Which clients do you want in the first wave?"
    menu:
        "Standard (Chelsea, Elsa, Jasmine)":
            pass
        "Customize":
            $ ivy.temporary_count = 3
            while ivy.temporary_count > 0:
                $ title = "Pick [ivy.temporary_count] more for the first wave"
                menu:
                    "Chelsea" if not chelsea.has_tag('wave1'):
                        add tags 'wave1' to chelsea
                    "Elsa" if not elsa.has_tag('wave1'):
                        add tags 'wave1' to elsa
                    "Jasmine" if not jasmine.has_tag('wave1'):
                        add tags 'wave1' to jasmine
                    "Becky Sue" if not becky_sue.has_tag('wave1'):
                        add tags 'wave1' to becky_sue
                        $ ivy.tier2 -= 1
                        $ becky_sue.min_reputation = 0
                    "Donna" if not donna.has_tag('wave1'):
                        add tags 'wave1' to donna
                        $ ivy.tier2 -= 1
                        $ donna.min_reputation = 0
                    "Terri" if not terri.has_tag('wave1'):
                        add tags 'wave1' to terri
                        $ ivy.tier2 -= 1
                        $ terri.min_reputation = 0
                    "Alexis" if not alexis.has_tag('wave1'):
                        add tags 'wave1' to alexis
                        $ ivy.tier3 -= 1
                        $ alexis.min_reputation = 0
                    "Lauren" if not lauren.has_tag('wave1'):
                        add tags 'wave1' to lauren
                        $ ivy.tier3 -= 1
                        $ lauren.min_reputation = 0
                    "Sarah" if not sarah.has_any_tag('wave1', 'wave2'):
                        sys "Sarah's training is more challenging before you have other relations.  If you start with her, you'll likely want Club access and a teaching aide as soon as you can.  You can have 2 extra weeks to train her to help make up for this."
                        $ title = "Add Sarah to the first wave anyway?"
                        menu:
                            "Yes add her to wave one (2 extra weeks training)":
                                add tags 'wave1' to sarah
                                $ ivy.tier3 -= 1
                                $ sarah.min_reputation = 0
                                $ sarah.training_period += 2
                            "Add her to wave two instead (1 extra week training)":
                                add tags 'wave2' to sarah
                                $ ivy.tier3 -= 1
                                $ ivy.tier2 += 1
                                $ sarah.min_reputation = 1
                                $ sarah.training_period += 1
                                $ ivy.temporary_count += 1
                            "Reconsider":
                                $ ivy.temporary_count += 1
                $ ivy.temporary_count -= 1
            # move normal first wave clients to a later wave if not selected
            if not chelsea.has_tag('wave1'):
                if ivy.tier3 < 3:
                    $ ivy.tier3 += 1
                    $ chelsea.min_reputation = 2
                else:
                    $ ivy.tier2 += 1
                    $ chelsea.min_reputation = 1
            if not elsa.has_tag('wave1'):
                if ivy.tier3 < 3:
                    $ ivy.tier3 += 1
                    $ elsa.min_reputation = 2
                else:
                    $ ivy.tier2 += 1
                    $ elsa.min_reputation = 1
            if not jasmine.has_tag('wave1'):
                if ivy.tier3 < 3:
                    $ ivy.tier3 += 1
                    $ jasmine.min_reputation = 2
                else:
                    $ ivy.tier2 += 1
                    $ jasmine.min_reputation = 1
            # bump someone to third wave if Sarah moved to first wave
            if sarah.has_tag('wave2') and ivy.tier2 > 3:
                if donna.min_reputation == 1:
                    $ donna.min_reputation = 2
                elif becky_sue.min_reputation == 1:
                    $ becky_sue.min_reputation = 2
                elif terri.min_reputation == 1:
                    $ terri.min_reputation = 2
                else:
                    $ chelsea.min_reputation = 2
    return

label ivy_check_messages_first:
  sys "Check your message first."
  break_movement
  return

# Client Rejected
label ivy_rejected:
  sys "You can no longer train [ivy.full_name]."
  return

# Arrange Client Session
label ivy_calling:
    # Check if client has already been trained this week
    if not ivy.can_be_interacted:
        "You had an evening session with Ivy earlier this week.  You need to wait until the weekend or next week for another session."
    else:
        call forced_movement(living_room) from _call_forced_movement_944
        summon ivy
        $ ivy.visit_count += 1
        if 'first_visit' in ivy.tags:
            wt_image intro_wife_visit_1_1
            "Ivy arrives wearing a large pair of sunglasses, presumably to hide her appearance. You show her to your living room."
            if not player.has_tag('first_client_visit_message'):
                add tags 'first_client_visit_message' to player
                sys "[player.first_client_visit_message_text]"
            sys "You'll notice this text box may overlay the photo art.  If you ever want to see details of the image under the text box, press 'h' or the middle mouse button to make the text box appear or disappear.  Try it now, if you'd like."
        elif ivy.sos < 1:
            wt_image intro_wife_visit_1_1
            "Ivy arrives wearing her sunglasses again, to avoid recognition."
        else:
            wt_image intro_wife_visit_1_60
            "Ivy's no longer hiding behind her sunglasses when she arrives for today's session."
        if ivy.has_tag('considering_stripping'):
            $ ivy.temporary_count = 4
            call ivy_strip_proceed_test from _call_ivy_strip_proceed_test
            # offers to strip
            if ivy.temporary_count < 1:
                wt_image intro_wife_visit_1_11
                ivy.c "Okay, I'm ready to do it!"
                player.c "Great.  I'll get my clothes off."
                wt_image intro_wife_visit_1_13
                ivy.c "What?  No.  I mean, I'm ready to try giving you a strip tease.  That is, if you want me to?"
                $ title = "Let her strip for you?"
                menu:
                    "Yes, use today to finish her strip training":
                        call ivy_first_strip from _call_ivy_first_strip
                    "No, do something else for today":
                        player.c "Great, but I have something else planned for you today."
                        ivy.c "Oh.  Okay."
            $ ivy.temporary_count = 0
        else:
            pass
    return

# Display Portrait
label ivy_update_media:
    if ivy.has_tag('first_visit'):
        $ ivy.change_image('intro_wife_visit_1_2')
    elif ivy.status == 'on_training' and current_location in session_locations:
        $ ivy.change_image('intro_wife_visit_1_6')
    elif stage.is_here and ivy.has_tag('showgirl'):
        if ivy.has_tag('watched_today'):
            if ivy.showgirl_outfit == 1:
                $ ivy.change_image('intro_wife_strip_outfit_1_1')
            elif ivy.showgirl_outfit == 2:
                $ ivy.change_image('intro_wife_strip_outfit_2_1')
            elif ivy.showgirl_outfit == 3:
                $ ivy.change_image('intro_wife_strip_outfit_3_1')
            else:
                $ ivy.change_image('intro_wife_strip_outfit_4_1')
        else:
            if ivy.showgirl_outfit == 1:
                $ ivy.change_image('intro_wife_strip_outfit_2_1')
            elif ivy.showgirl_outfit == 2:
                $ ivy.change_image('intro_wife_strip_outfit_3_1')
            elif ivy.showgirl_outfit == 3:
                $ ivy.change_image('intro_wife_strip_outfit_4_1')
            else:
                $ ivy.change_image('intro_wife_strip_outfit_1_1')
    elif ivy.has_tag('crawl_visit_now'):
        $ ivy.change_image('intro_wife_visit_2_1')
    elif ivy.has_tag('domme_visit_now'):
        $ ivy.change_image('intro_wife_visit_4_1')
    elif ivy.has_tag('sex_visit_now'):
        $ ivy.change_image('intro_wife_visit_3_2')
    elif ivy.has_tag('strip_visit_now'):
        $ ivy.change_image('intro_wife_visit_2_1')
    elif ivy.has_tag('submissive_visit_now'):
        $ ivy.change_image('intro_wife_visit_3_2')
    elif ivy.has_tag('unsatisfied'):
        $ ivy.change_image('intro_wife_visit_1_2')
    elif ivy.has_tag('satisfied'):
        $ ivy.change_image('intro_wife_visit_1_6')
    else:
        pass
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Action
label ivy_examine:
    if ivy.has_tag('first_visit'):
        "Ivy seems a little nervous behind her large, identity-obscuring sunglasses."
    elif ivy.status == 'on_training' and current_location in session_locations:
        "Ivy the Introductory Wife is here for her training."
    elif stage.is_here and ivy.has_tag('showgirl'):
        if ivy.has_tag('watched_today'):
            "Ivy's finished her show for today."
        else:
            "Ivy's getting ready to start her show."
    call ivy_description_display from _call_ivy_description_display
    return

# NOTE: make description display and review files part of the standard template if not already there

# Description Display
label ivy_description_display:
    if ivy.status == "on_training":
        "You have until the end of week [ivy.training_limit] to complete this engagement."
    elif ivy.has_tag('satisfied'):
        "Ivy feels like a well trained wife."
        if ivy.has_tag('domme'):
            extend " She now thinks of herself as a Domme."
        elif ivy.has_tag('dommed_you'):
            extend " She's learned to be comfortable taking control in the bedroom."
        if ivy.has_tag('showgirl'):
            extend " She enjoys turning men on by stripping for them on stage."
        elif ivy.has_tag('stripped_for_you'):
            extend " She enjoys stripping for her husband."
        if ivy.anal_count > 0:
            extend " She's now able to please her husband with anal sex."
        if ivy.has_tag('bj_training'):
            extend " She thinks of herself as a 'well-trained cocksucker'."
        if ivy.has_tag('had_adventurous_sex'):
            extend " She's become very adventurous with the sexual positions she'll try."
        if ivy.serve_count > 0:
            extend " She's learned to enjoy being subservient."
        if ivy.has_tag('spanking_orgasm'):
            extend " She's can now enjoy being spanked."
        if ivy.crawl_count > 0:
            extend " She both loves and hates but mostly loves being ordered to crawl."
    if not ivy.has_any_tag('bimbo', 'degraded', 'doll', 'petgirl', 'transformed_slavegirl', 'whore'):
        if ivy.has_tag('trigger_implanted'):
            "You have implanted a hypnotic trigger in her."
        if ivy.has_tag('love_potion_used'):
            "She is under the influence of a love potion."
        "[ivy.statblock]"
        $ items = ", ".join(i.name for i in ivy.get_items()) if ivy.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    # Note: special help section just for Ivy
    if ivy.status == 'on_training':
        $ title = "Do you want help understanding what her stats mean?"
        menu menu_ivy_description_help_menu:
            "Sense of Self":
                call concept_description_sos from _call_concept_description_sos
                jump menu_ivy_description_help_menu
            "Desire":
                call concept_description_desire from _call_concept_description_desire
                jump menu_ivy_description_help_menu
            "Submission":
                call concept_description_submission from _call_concept_description_submission
                jump menu_ivy_description_help_menu
            "Resistance":
                call concept_description_resistance from _call_concept_description_resistance
                jump menu_ivy_description_help_menu
            "No thanks":
                pass
    return

# Review Files
label ivy_review_files:
    call ivy_update_media from _call_ivy_update_media
    wt_image ivy.image
    call ivy_description_display from _call_ivy_description_display_1
    wt_image current_location.image
    return

# Talk to Character
label ivy_talk:
    if ivy.has_tag('first_visit'):
        wt_image intro_wife_visit_1_2
        player.c "What's with the glasses?"
        ivy.c "I didn't want anyone I know to see me coming over here.  I wasn't sure what sort of place this would be."
        player.c "Were you expecting a flashing neon 'Wife Training Facility' sign out front?"
        ivy.c "I wasn't sure what to expect.  This is really nerve-wracking, you know."
        player.c "Your husband said you were looking forward to being trained."
        ivy.c "That's an exaggeration!  I don't even know what being 'trained' even means."
        $ title = "What does it mean?"
        menu ivy_first_talk_menu:
            "It means you learn to be obedient":
                player.c "It means I teach you to be more obedient.  The thought of that excites you, doesn't it?"
                wt_image intro_wife_visit_1_3
                ivy.c "I am NOT a submissive woman.  My husband and I have an equal marriage."
                player.c "So he's told me.  He also told me the thought of being trained excited you.  I think you want to be taught to obey."
                ivy.c "That's not something my husband would be interested in.  He loves me the way I am."
                player.c "He saw an advertisement for a wife-training service and told you about it.  Are you sure he's not interested in having you trained to be more obedient?"
                wt_image intro_wife_visit_1_4
                ivy.c "If that's what he wanted, wouldn't he have told me himself?"
                player.c "I think it's what you both want, even if it's hard to admit.  Fortunately, I'm here to help you get in touch with your submissive side."
                change ivy submission by 5
                sys "That resonated with her.  She's starting to think about whether you're someone she might want to obey."
            "It means you and I have some fun together" if not ivy.has_tag('not_fun_together_choice'):
                add tags 'not_fun_together_choice' to ivy
                player.c "It means you and I get to spend some time together and have some fun."
                ivy.c "You were just trying to pick me up?  I don't think my husband knew that.  We do have an open marriage, but usually we both find a play partner before either of us fools around."
                sys "Her husband told you she wasn't coming over for a booty call.  Try a different approach."
                jump ivy_first_talk_menu
            "It means I help you to lose some inhibitions":
                player.c "It means I help you to lose some inhibitions, so you can be happier and enjoy a happier marriage."
                wt_image intro_wife_visit_1_5
                ivy.c "What makes you think I'm not happy or happy with my marriage?"
                player.c "There's always room for improvement, isn't there?  I don't think you would have signed up for training if you weren't hoping to spice your sex life up a bit, would you?"
                wt_image intro_wife_visit_1_6
                ivy.c "You're going to teach me how to spice up my sex life?"
                player.c "I think I can teach you a few new tricks, yes.  Maybe something you've wanted to do, but haven't been able to bring yourself to try."
                change ivy desire by 5
                sys "That resonated with her.  She's starting to think about you in a sexual way."
            "It means I help you to be a better wife for your husband":
                player.c "It means I help you to become more like the wife your husband wants, so that he's happier and you enjoy a happier marriage together."
                wt_image intro_wife_visit_1_7
                ivy.c "What makes you think he's not happy with me or our marriage?"
                player.c "There's always room for improvement, isn't there?  I don't think he would have brought a wife-training service to your attention if he wasn't hoping for some sort of change, would he?"
                wt_image intro_wife_visit_1_8
                ivy.c "You think my husband's getting bored with me?"
                player.c "I think he's hoping I teach you some new tricks to spice up your sex life.  Maybe something he's wanted you to do, but you haven't been able to bring yourself to try."
                change ivy resistance by -5
                sys "That resonated with her.  She's starting to think that she should listen to what you tell her."
            "It means I train you, so you can train your husband":
                player.c "It means I teach you some new sexual tricks, then you can take what you learn and teach your husband."
                wt_image intro_wife_visit_1_6
                "She laughs."
                ivy.c "That sounds like it might be fun.  Not sure it's what my husband thought we'd be up to, though."
                player.c "Do you think he'd object?"
                ivy.c "To me learning something new?  No.  I think it's what he's hoping will happen from me coming here."
                player.c "And what about you training him?"
                wt_image intro_wife_visit_1_9
                ivy.c "I'm not sure I'd be up to that, but I don't think he'd object if I did, no."
                change ivy resistance by -5
                $ ivy.domme_comfort += 1
                sys "That resonated with her.  She's a little more willing to listen to you now.  There's also been a hidden change take place, one not related to her main stats."
        notify
        sys "The initial conversation with a client will often give you a chance to nudge their stats in one direction or other."
        sys "Often, you still need to know more about them for the training to be as effective as possible, but you may feel like you know enough now to get started on her training."
        rem tags 'first_visit' 'no_hypnosis' from ivy
    elif ivy.status == 'on_training' and current_location in session_locations:
        $ ivy.temporary_count = 1
        wt_image intro_wife_visit_1_9
        $ title = "What would you like to talk to her about?"
        menu:
            "Her fantasies" if not ivy.has_tag('discussed_stripping'):
                player.c "Tell me about yourself, Ivy.  What do you enjoy, sexually?"
                ivy.c "Lots of things.  I love being with my husband.  I love that he lets me be with other men without getting jealous."
                player.c "And what sort of things do you do with your husband and these other men?"
                if ivy.test('resistance', 70):
                    wt_image intro_wife_visit_1_7
                    ivy.c "I'm not sure ladies are supposed to talk about that sort of thing."
                    wt_image intro_wife_visit_1_6
                    ivy.c "But I guess it's all right, since you're here to help.  I love to 'suck and fuck', if you'll excuse my vernacular."
                    player.c "And what do you do to spice things up, while you're sucking and fucking?"
                    wt_image intro_wife_visit_1_8
                    ivy.c "Well, I do enjoy teasing.  It's fun to get a guy excited. I enjoy that a lot.  I wish ..."
                    player.c "You wish what?"
                    add tags 'discussed_stripping' to ivy
                    #rem tags 'failed_stripping_discussion' from ivy
                    $ ivy.temporary_count = 0
                    wt_image intro_wife_visit_1_11
                    ivy.c "This is going to sound stupid, but I love the idea of turning a guy on using just my body, without even touching him.  The idea that just looking at me would get him hard is really hot."
                    player.c "Have you ever given your husband a strip tease?"
                    ivy.c "No!  Never. I wouldn't ... I couldn't ..."
                    player.c "Why not?"
                    ivy.c "Because I'd look stupid.  I'm his wife.  He's seen my body a million times, and it's not what it used to be.  I'm not some hot bodied college student dancing her way through school.  I'd just look ridiculous."
                    sys "This opened up new opportunities to train her."
                elif ivy.test('resistance', 75) or ivy.test('desire', 10):
                    wt_image intro_wife_visit_1_7
                    ivy.c "I'm not sure ladies are supposed to talk about that sort of thing."
                    wt_image intro_wife_visit_1_6
                    ivy.c "But I guess it's all right, since you're here to help.  I love to 'suck and fuck', if you'll excuse my vernacular."
                    player.c "And what do you do to spice things up, while you're sucking and fucking?"
                    wt_image intro_wife_visit_1_8
                    ivy.c "Well, I do enjoy teasing.  It's fun to get a guy excited. I enjoy that a lot.  I wish ..."
                    player.c "You wish what?"
                    #add tags 'failed_stripping_discussion' to ivy
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_10
                    ivy.c "Nothing.  That's all."
                    sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                else:
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_7
                    ivy.c "I'm not sure ladies are supposed to talk about that sort of thing.  And besides, I hardly know you."
            "Her husband's fantasies" if not ivy.has_tag('discussed_anal'):
                player.c "Tell me about your husband, Ivy.  What does he enjoy, sexually?"
                ivy.c "Lots of things.  He loves being with me.  He also loves being with other women, and loves that I let him do so without getting jealous."
                player.c "And what does he do with these other women that he doesn't do with you?"
                if ivy.test('resistance', 65):
                    ivy.c "My husband isn't sleeping with other women because I can't satisfy him.  He just likes variety, as do I."
                    player.c "I'm sure he does.  And I'm sure some of those women enjoy doing things that you don't.  Does your husband talk to you about what sort of sex he has with his other partners."
                    ivy.c "Yes, we both shares notes after we've been with someone else.  And usually we fuck like bunnies after we do."
                    player.c "And when he shares notes, is there anything you've noticed that he seems to particularly enjoy doing with other women that he doesn't do with you?"
                    add tags 'discussed_anal' to ivy
                    #rem tags 'failed_anal_discussion' from ivy
                    $ ivy.temporary_count = 0
                    wt_image intro_wife_visit_1_12
                    ivy.c "Well ... I mean ... I guess he does always sound extra excited after he's been with a woman who lets him put it up her butt.  Like a kid who found some candy."
                    player.c "You don't enjoy anal sex?"
                    ivy.c "I'm not even sure.  We tried a few times, back when we were first going out together and it ... well, it didn't go well."
                    player.c "Why not?"
                    ivy.c "The first time I panicked, and he felt bad for asking.  Then we tried again, but it felt weird to me and he could tell, so he suggested we do things normally instead, so I agreed."
                    wt_image intro_wife_visit_1_12
                    ivy.c "I knew he wanted this, so later I suggested we try again and we did try, but I was so nervous, he could only get himself partway inside me before I tensed up.  Again he tried to make me feel better by suggesting I jerk him off instead, and he told me anal wasn't important to him."
                    player.c "Is it important to him?"
                    ivy.c "I don't think so.  I'm sure he enjoys the sex we do have.  But I do get a little jealous when he tells me about his anal conquests, and ..."
                    player.c "You know it would make him happy if he conquered your ass, too?"
                    "She just nods."
                    sys "This opened up new opportunities to train her."
                elif ivy.test('resistance', 75):
                    ivy.c "My husband isn't sleeping with other women because I can't satisfy him.  He just likes variety, as do I."
                    player.c "I'm sure he does.  And I'm sure some of those women enjoy doing things that you don't.  Does your husband talk to you about what sort of sex he has with his other partners."
                    ivy.c "Yes, we both shares notes after we've been with someone else.  And usually we fuck like bunnies after we do."
                    player.c "And when he shares notes, is there anything you've noticed that he seems to particularly enjoy doing with other women that he doesn't do with you?"
                    #add tags 'failed_anal_discussion' to ivy
                    wt_image intro_wife_visit_1_6
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_10
                    ivy.c "Well ... I mean ....  No, not really.  Nothing comes to mind."
                    sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                else:
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_7
                    ivy.c "I can satisfy my husband quite nicely, thank you.  He's not sleeping with other women to get something I can't give him.  He just likes variety, as do I.  I'm very good for him."
                    "She's too defensive to get anywhere on this topic until she trusts you more. This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
            "Obedience" if not ivy.has_tag('discussed_crawling'):
                player.c "Do you obey your husband, Ivy?"
                ivy.c "That's not the type of relationship we have.  We're equal partners.  Neither of us obeys the other."
                player.c "Doesn't he ever boss you around?"
                ivy.c "No.  Never.  He's a perfect gentleman.  That's part of what I love about him."
                player.c "What about in bed?  Does he ever take charge, sexually?"
                ivy.c "No.  He's not that type.  He's always very polite and considerate.  Sometimes ..."
                player.c "Sometimes too considerate?"
                ivy.c "I didn't say that.  I like the way my husband makes love to me."
                player.c "And what about your other partners.  Do they all make love to you gently?  Or do some of them expect you to obey them?"
                if ivy.test('resistance', 60):
                    wt_image intro_wife_visit_1_8
                    ivy.c "I guess some of them have enjoyed taking charge."
                    player.c "Did you enjoy that?"
                    ivy.c "Not when they got rough."
                    player.c "What about when they told you what they wanted you to do?"
                    ivy.c "Sometimes ... sometimes that was okay."
                    player.c "What have you been ordered to do that turned you on the most?"
                    add tags 'discussed_crawling' to ivy
                    rem tags 'failed_crawling_discussion' from ivy
                    $ ivy.temporary_count = 0
                    wt_image intro_wife_visit_1_12
                    ivy.c "There's ... Well ... This didn't turn me on, but something that did stick with me once was ..."
                    player.c "Spit it out."
                    ivy.c "A guy once told me to crawl over to him if I wanted his cock."
                    player.c "And did you?"
                    wt_image intro_wife_visit_1_10
                    ivy.c "NO!  Of course, not.  I was repulsed.  I told him he had a huge ego."
                    player.c "What did he say?"
                    wt_image intro_wife_visit_1_12
                    ivy.c "He said he also had a huge cock, but I needed to get down on all fours if I wanted to taste it.  I laughed at him, of course, and left.  I'm not the crawling type."
                    player.c "Not even for your husband?"
                    wt_image intro_wife_visit_1_10
                    ivy.c "My husband wouldn't want me to crawl to him."
                    sys "Maybe not, but maybe some part of her would like to crawl for him.  This opened up new opportunities to train her."
                elif ivy.test('resistance', 75) or ivy.test('submission', 10):
                    wt_image intro_wife_visit_1_8
                    ivy.c "I guess some of them have enjoyed taking charge."
                    player.c "Did you enjoy that?"
                    ivy.c "Not when they got rough."
                    player.c "What about when they told you what they wanted you to do?"
                    ivy.c "Sometimes ... sometimes that was okay."
                    player.c "What have you been ordered to do that turned you on the most?"
                    add tags 'failed_crawling_discussion' to ivy
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_10
                    ivy.c "There's ... Well ... Nothing really.  It's nice to know what the guy wants, of course.  That's all."
                    sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                else:
                    $ ivy.temporary_count = 1
                    wt_image intro_wife_visit_1_4
                    ivy.c "I am NOT a submissive woman.  I don't seek out partners who are into that sort of thing."
                    "She's too defensive to get anywhere on this topic until she trusts you more. This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
            "Taking charge" if not ivy.has_tag('discussed_taking_charge'):
                add tags 'discussed_taking_charge' to ivy
                $ ivy.temporary_count = 0
                player.c "Does your husband do what you tell him, Ivy?"
                wt_image intro_wife_visit_1_7
                ivy.c "What?  No.  That's not the type of relationship we have.  We're equal partners."
                player.c "What about in bed?  Do you ever take charge, sexually?"
                wt_image intro_wife_visit_1_8
                ivy.c "Should I?"
                player.c "You tell me.  Do you ever direct his actions in bed?  Show him what you want him to do?"
                ivy.c "Well ... I mean ... sometimes when ... you know."
                player.c "When his mouth is between your legs?  Do you show him how you like to be licked?"
                wt_image intro_wife_visit_1_11
                ivy.c "Sometimes"
                player.c "And how does he react?"
                ivy.c "Well, like any husband would, I think.  He wants me to enjoy myself."
                player.c "So you wrap your fingers in his hair and direct his tongue to where you want it?"
                wt_image intro_wife_visit_1_10
                ivy.c "Not in a mean way."
                player.c "There's nothing mean about showing a man how you want him to please you.  Your husband enjoys pleasing you, doesn't he?"
                ivy.c "He's not submissive, if that's what you're suggesting."
                player.c "Are you sure?  Have you tried dominating him?"
                ivy.c "No ... I mean, wouldn't he have asked if that's what he wanted?"
                player.c "Maybe not.  When you agreed to come here to be trained, did you ask your husband how he wanted you to be trained?"
                ivy.c "No ... he just wanted ..."
                player.c "You didn't actually ask what he wanted.  Once he was onside with the idea, you ran with it.  Who suggested that your marriage be an open one?"
                ivy.c "We both discussed it."
                player.c "After you suggested it."
                ivy.c "Yes, but he's happy about it."
                player.c "I'm sure he is. I think he's always happy when you take charge of your sexual adventures.  I bet he'd like it if you did it more often."
                wt_image intro_wife_visit_1_11
                ivy.c "I'm not sure I want to take charge of him, sexually."
                sys "She may not be sure about herself, but she seems sure he'd let her if she was.  This opened up new opportunities to train her."
            "Nothing right now":
                $ ivy.temporary_count = 2
        if ivy.temporary_count == 2:
            $ ivy.temporary_count = 0
        elif ivy.temporary_count == 1:
            $ ivy.temporary_count = 0
            $ title = "Spend the rest of the session talking to her?"
            menu:
                "Yes":
                    $ ivy.training_session()
                    wt_image intro_wife_visit_1_13
                    "You spend the rest of the session chatting with her and getting to know her better.  Spending this time with her helps her to trust you more."
                    change ivy resistance by -5
                    change player energy by -energy_long
                    notify
                    end_day
                "No":
                    add tags 'successful_talk_today' to ivy
        else:
            add tags 'successful_talk_today' to ivy
    elif stage.is_here and ivy.has_tag('showgirl'):
        call ivy_update_media from _call_ivy_update_media_1
        wt_image ivy.image
        if ivy.has_tag('watched_today'):
            ivy.c "I hope you enjoyed the show!"
        else:
            ivy.c "I'm going up on stage soon.  Why don't you stay and watch?"
    elif ivy.has_tag('crawl_visit_now'):
        call ivy_update_media from _call_ivy_update_media_2
        wt_image ivy.image
        ivy.c "I'm not sure this was a good idea.  Maybe I should go?"
    elif ivy.has_tag('domme_visit_now'):
        call ivy_update_media from _call_ivy_update_media_3
        wt_image ivy.image
        if ivy.has_tag('second_domme_scene'):
            ivy.c "Don't keep me waiting, boy.  Offer yourself to me."
        else:
            ivy.c "I'm ready when you are."
    elif ivy.has_tag('sex_visit_now'):
        call ivy_update_media from _call_ivy_update_media_4
        wt_image ivy.image
        ivy.c "Are you coming over to join me?"
    elif ivy.has_tag('strip_visit_now'):
        call ivy_update_media from _call_ivy_update_media_5
        wt_image ivy.image
        ivy.c "Let me know when you're ready for me to get started."
    elif ivy.has_tag('submissive_visit_now'):
        call ivy_update_media from _call_ivy_update_media_6
        wt_image ivy.image
        ivy.c "Are you ready for me now, Sir?"
    else:
        "You can't speak to her right now."
    return

# Hypno Actions
label ivy_hypnosis_start:
    if ivy.status == "on_training" and current_location in session_locations:
        $ ivy.training_session()
        player.c "Ivy, I am going to talk with you, and you are going to listen to me."
        call focus_image from _call_focus_image_96
        player.c "Listen to me, Ivy. Listen to my voice and nothing else, Ivy. Only my voice. Only my voice now."
        wt_image intro_wife_visit_1_45
        "She soon falls under your trance."
        wt_image intro_wife_visit_1_46
        player.c "You want us to be comfortable together, Ivy.  You want me to be comfortable while we talk.  You want to be comfortable, too.  It's uncomfortable to be covered up.  Don't keep yourself so covered up, Ivy."
        wt_image intro_wife_visit_1_47
        player.c "We'll both be more comfortable once you stop hiding, Ivy.  Bare your breasts.  Bare your breasts so that you'll be open and we can both be comfortable for our talk."
        wt_image intro_wife_visit_1_48
        "Under your influence she removes her top and bra."
        wt_image intro_wife_visit_1_49
        if not player.has_tag('first_hypno_breasts_message'):
            add tags 'first_hypno_breasts_message' to player
            "[player.first_hypno_breasts_message_text]"
            "Now you have to decide what to work on with her."
        else:
            extend "  Now you have to decide what to work on with her."
        if ivy.hypno_count == 1:
            sys "Hypnosis has multiple purposes.  It can directly target a client's stat, which is useful when you know what you're trying to accomplish with her.  For some clients, special hypno options help overcome particular concerns."
            sys "For some clients, if you hypnotize them enough and lower their resistance sufficiently, you can place a trigger that opens new content."
            sys "Hypnosis by itself, however, is rarely enough.  It usually works best to use hypnosis as a supplement to regular training. The hypnotist trait is the most challenging one early on, because it can take time to figure out how best to use hypnosis for each client."
        # system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    elif ivy.in_area('house'):
        if ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
            $ ivy.training_session()
            wt_image intro_wife_visit_2_1
            player.c "Before we get started, Ivy, I'd like you to look at this for me."
            call focus_image from _call_focus_image_97
            player.c "Listen to me, Ivy. Listen to my voice and nothing else, Ivy.  Only my voice.  Only my voice now."
            wt_image intro_wife_visit_2_2
            "She soon falls under your trance."
            wt_image intro_wife_visit_2_35
            player.c "You want us to be comfortable together, Ivy.  You want me to be comfortable while we talk.  You want to be comfortable, too.  It's uncomfortable to be covered up.  Don't keep yourself so covered up, Ivy."
            wt_image intro_wife_visit_2_5
            player.c "We'll both be more comfortable once you stop hiding, Ivy.  Bare your breasts.  Bare your breasts so that you'll be open and we can both be comfortable for our talk."
            wt_image intro_wife_visit_2_36
        elif ivy.has_tag('domme_visit_now'):
            $ ivy.training_session()
            wt_image intro_wife_visit_4_1
            player.c "Before we get started, Mistress, I'd like you to look at this for me."
            call focus_image from _call_focus_image_98
            player.c "Listen to me, Ivy. Listen to my voice and nothing else, Ivy.  Only my voice.  Only my voice now."
            wt_image intro_wife_visit_4_2
            "She soon falls under your trance."
            wt_image intro_wife_visit_4_3
            player.c "You want us to be comfortable together, Ivy.  You want me to be comfortable while we talk.  You want to be comfortable, too.  It's uncomfortable to be covered up.  Don't keep yourself so covered up, Ivy."
            wt_image intro_wife_visit_4_4
            player.c "We'll both be more comfortable once you stop hiding, Ivy.  Bare your breasts.  Bare your breasts so that you'll be open and we can both be comfortable for our talk."
            wt_image intro_wife_visit_4_5
        elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
            $ ivy.training_session()
            wt_image intro_wife_visit_3_3
            player.c "Before we get started, Ivy, I'd like you to look at this for me."
            call focus_image from _call_focus_image_99
            player.c "Listen to me, Ivy. Listen to my voice and nothing else, Ivy.  Only my voice.  Only my voice now."
            wt_image intro_wife_visit_3_2
            "She soon falls under your trance."
            wt_image intro_wife_visit_3_15
            player.c "You want us to be comfortable together, Ivy.  You want me to be comfortable while we talk.  You want to be comfortable, too.  It's uncomfortable to be covered up.  Don't keep yourself so covered up, Ivy."
            wt_image intro_wife_visit_3_85
            player.c "We'll both be more comfortable once you stop hiding, Ivy.  Bare your breasts.  Bare your breasts so that you'll be open and we can both be comfortable for our talk."
            wt_image intro_wife_visit_3_86
        else:
            "You can't hypnotize her right now."
            $ ignore_context_change = True
    else:
        "You can't hypnotize her right now."
        $ ignore_context_change = True
    return

label ivy_desire_hypnosis:
    if ivy.status == "on_training" and current_location in session_locations:
        wt_image intro_wife_visit_1_50
        "You work on raising Ivy's Desire for you."
        # system now applies the stat gain and then goes on to the _desire_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    elif ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
        wt_image intro_wife_visit_2_37
        "You work on raising Ivy's Desire for you.  With her training complete, this may not have any impact, but it can't hurt for her to view you with increased interest."
    elif ivy.has_tag('domme_visit_now'):
        wt_image intro_wife_visit_4_6
        "You work on raising Ivy's Desire for you.  With her training complete, this may not have any impact, but it can't hurt for her to view you with increased interest."
    elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
        wt_image intro_wife_visit_3_87
        "You work on raising Ivy's Desire for you.  With her training complete, this may not have any impact, but it can't hurt for her to view you with increased interest."
    else:
        sys "How'd you get here?  Coding error in Ivy Hypnosis Desire Action"
    return

label ivy_submission_hypnosis:
    if ivy.status == "on_training" and current_location in session_locations:
        wt_image intro_wife_visit_1_51
        "You work on raising Ivy's Submission towards you."
        # system now applies the stat gain and then goes on to the _submission_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    elif ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
        wt_image intro_wife_visit_2_38
        "You work on raising Ivy's Submission towards you.  With her training complete, this may not have any impact, but it can't hurt for her to be more deferential to you."
    elif ivy.has_tag('domme_visit_now'):
        wt_image intro_wife_visit_4_7
        "You work on raising Ivy's Submission towards you.  Why you'd want your Mistress to be more submissive towards you isn't immediately clear, but presumably you have a plan."
    elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
        wt_image intro_wife_visit_3_81
        "You work on raising Ivy's Submission towards you.  With her training complete, this may not have any impact, but it can't hurt for her to be more deferential to you."
    else:
        sys "How'd you get here?  Coding error in Ivy Hypnosis Submission Action"
    return

label ivy_sos_hypnosis:
    if ivy.status == "on_training" and current_location in session_locations:
        wt_image intro_wife_visit_1_52
    "Sense of Self can be the most difficult trait to affect, and in Ivy's case it's too tied to being trained for you to influence it directly through hypnosis.  You'll need to try and influence it indirectly by working on another aspect of her thinking in order to help you train her."
    $ ivy.sos_hypno_action.backtrack = True ## this and the next two commands back you up to the menu of hypnosis options
    $ ivy.remove_action( ivy.sos_hypno_action )  # Use the SOS hypno action reference instead of the "rem action" shortcut, because this is accessible via weekend hypnosis, as well. ## NEED make sure this works?
    $ context = "ivy_hypnosis"
    break_sequence
    return

label ivy_resistance_hypnosis:
    if ivy.status == "on_training" and current_location in session_locations:
        wt_image intro_wife_visit_1_53
        "You work on lowering Ivy's Resistance to your suggestions."
        # system now applies the stat change and then goes on to the _resistance_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    elif ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
        wt_image intro_wife_visit_2_39
        if not ivy.has_tag('trigger_implanted') and player.has_tag('hypnotist'):
            "You work on lowering Ivy's Resistance to your suggestions.  If you lower it enough, you may be able to plant a trigger, which may occasionally allow you to modify her behavior in other ways."
        else:
            "You work on lowering Ivy's Resistance to your suggestions.  With her training complete and her trigger implanted, this may not have any impact, but it can't hurt for her to be more inclined to listen to you."
    elif ivy.has_tag('domme_visit_now'):
        wt_image intro_wife_visit_4_8
        if not ivy.has_tag('trigger_implanted'):
            "You work on lowering Ivy's Resistance to your suggestions.  If you lower it enough, you may be able to plant a trigger, which may occasionally allow you to modify her behavior in other ways."
        else:
            "You work on lowering Ivy's Resistance to your suggestions.  With her training complete and her trigger implanted, this may not have any impact, but it can't hurt for her to be more inclined to listen to you."
    elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
        wt_image intro_wife_visit_3_74
        if not ivy.has_tag('trigger_implanted'):
            "You work on lowering Ivy's Resistance to your suggestions.  If you lower it enough, you may be able to plant a trigger, which may occasionally allow you to modify her behavior in other ways."
        else:
            "You work on lowering Ivy's Resistance to your suggestions.  With her training complete and her trigger implanted, this may not have any impact, but it can't hurt for her to be more inclined to listen to you."
    else:
        sys "How'd you get here?  Coding error in Ivy Hypnosis Resistance Action"
    return

label ivy_crawling_hypnosis:
    add tags 'hypno_re_crawling' to ivy
    player.c "Crawling for a man excites you, Ivy."
    wt_image intro_wife_visit_1_54
    ivy.c "Yes, but it's humiliating.  I couldn't do that."
    player.c "Yes, you could.  It would turn him on.  It would turn you on.  You'd both enjoy it if you crawled when you were told to crawl."
    wt_image intro_wife_visit_1_55
    "You spend some time working on making her more receptive to the idea of this activity.  It won't be enough on it's own to overcome her resistance, but it'll help."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_35
    return

label ivy_anal_hypnosis:
    add tags 'hypno_re_anal' to ivy
    player.c "You don't need to be scared of anal sex, Ivy."
    wt_image intro_wife_visit_1_56
    ivy.c "But I am scared of it.  I'm a disaster at it.  I make my husband feel bad when he even tries to have anal with me."
    player.c "You just need to relax.  He'd enjoy taking you in the rear.  You'd enjoy it, too, and you'd enjoy making him happy.  Your body is capable of taking a man's cock back there, you just need to relax and let it happen."
    wt_image intro_wife_visit_1_57
    "You spend some time working on making her more receptive to the idea of this activity.  It won't be enough on it's own to overcome her resistance, but it'll help."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_36
    return

label ivy_stripping_hypnosis:
    add tags 'hypno_re_stripping' to ivy
    player.c "Stripping for a man excites you, Ivy."
    wt_image intro_wife_visit_1_58
    ivy.c "Yes, but it'd be embarrassing.  I'd look stupid.  I couldn't do that."
    player.c "Yes you could.  He'd enjoy it.  You'd enjoy.  You wouldn't look stupid, you'd look sexy.  You're a beautiful woman and watching you take or clothes off would get a man very, very hard."
    wt_image intro_wife_visit_1_59
    "You spend some time working on making her more receptive to the idea of this activity.  It won't be enough on it's own to overcome her resistance, but it'll help."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_37
    return

label ivy_domme_hypnosis:
    add tags 'hypno_re_domme' to ivy
    $ ivy.domme_comfort += 1
    player.c "You'd enjoy taking charge of your husband, sexually, Ivy.  He'd enjoy it if you took charge and told him what to do."
    wt_image intro_wife_visit_1_52
    ivy.c "I don't know if that's appropriate.  He's my husband.  I shouldn't be demanding.  I should ask him what he wants."
    player.c "It's okay to be demanding when you're role-playing.  It's all in fun, and you'd both enjoy it.  You'd like to tell him what to do, and he'd enjoy pleasing you."
    wt_image intro_wife_visit_1_50
    "You spend some time working on making her more receptive to the idea of this activity.  It won't be enough on it's own to overcome her resistance, but it'll help."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_38
    return

label ivy_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
    if player.has_tag('hypnotist'):
        # note test is against unmodified stat
        if ivy.resistance < ivy.hypno_trigger_resistance_threshold:
            add tags 'trigger_implanted' to ivy
            "Ivy's mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
            $ ivy.temporary_count = 1
            while ivy.temporary_count == 1:
                $ title = "What trigger phrase do you want to use?"
                menu menu_ivy_implant_trigger:
                    "[ivy.trigger_phrase]":
                        $ ivy.temporary_count = 0
                    "Choose something else":
                        $ ivy.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
            player.c "Ivy, I have something important to tell you."
            player.c "When you hear the phrase, \"[ivy.trigger_phrase]\", you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
            ivy.c "Yes. When I hear, \"[ivy.trigger_phrase]\", I will fall into a trance and do everything I am told."
            player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it. You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
            ivy.c "Yes. I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
            notify "{}'s trigger has been implanted.".format(ivy.name)
        else:
            "You've been working on implanting a hypnotic trigger in Ivy's mind, but she's still too resistant to you. You need to lower her resistance to you before you can implant the trigger."
    return

label ivy_hypnosis_end:
    if ivy.status == "on_training" and current_location in session_locations:
        $ ivy.hypno_session()
        wt_image intro_wife_visit_1_15
        "When you've taken her as far as you can for this week, you have her dress, release her from your trance, and send her home.  The suggestions you've made will take time to fully affect her thinking."
        call character_location_return(ivy) from _call_character_location_return_648
        end_day
    elif ivy.status == "post_training" and current_location in session_locations:
        $ ivy.hypno_session()
        if ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
            wt_image intro_wife_visit_2_35
        elif ivy.has_tag('domme_visit_now'):
            wt_image intro_wife_visit_4_2
        elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
            wt_image intro_wife_visit_3_30
        ivy.c "Wow!  How'd it get so late?  I need to get going."
        call character_location_return(ivy) from _call_character_location_return_649
        wt_image current_location.image
        notify
    else:
        sys "How'd you get here?  Coding error in Ivy Hypnosis End label."
    return

## Character Specific Actions
# Training Actions
label ivy_train_her:
    call expandable_menu(ivy_regular_training_menu) from _call_expandable_menu_111
    return

label ivy_train_experience_pleasure:
    if current_location != boudoir:
        sys "This type of action may work better in the boudoir, if you've added items to it.  Take her there?"
        $ title = "Take her to the boudoir?"
        menu:
            "Yes":
                call forced_movement(boudoir) from _call_forced_movement_945
            "No, stay here":
                pass
    player.c "To be the best sex partner you can be, Ivy, you need to be able to truly enjoy sex."
    wt_image intro_wife_visit_1_6
    ivy.c "You don't think I do?"
    player.c "Let's find out.  I'd like you to spend the rest of our time together this evening lying back and relaxing while I give you an orgasm."
    $ ivy.temporary_count = 1
    call ivy_sex_proceed_test from _call_ivy_sex_proceed_test
    if ivy.temporary_count < 1:
        $ ivy.training_session()
        if ivy.sex_count > 0 or ivy.blowjob_count > 0 or ivy.anal_count > 0:
            wt_image intro_wife_visit_1_43
            ivy.c "Really?  You're going to make this all about me today?"
        else:
            wt_image intro_wife_visit_1_16
            ivy.c "This is just about you pleasing me?"
        wt_image intro_wife_visit_1_23
        player.c "Absolutely.  Come here and I'll show you."
        wt_image intro_wife_visit_1_66
        $ title = "How do you want to do this?"
        menu:
            "Encourage her to take charge" if ivy.has_tag('discussed_taking_charge'):
                wt_image intro_wife_pleasure_her_1_1
                player.c "You're a beautiful woman, Ivy.  It's an honor to be allowed to service you."
                wt_image intro_wife_pleasure_her_1_2
                ivy.c "'An honor' seems a little much, but I'm glad you're looking forward to it."
                player.c "I am, but I want to do it right.  I want to do it exactly the way you want me to do it.  Tell me what I should do to please you."
                wt_image intro_wife_pleasure_her_1_3
                ivy.c "I'm sure I'm no more complicated than other women you've been with.  I don't need to explain how to get me off, do I?"
                player.c "I want you to explain.  I want you to tell me exactly what will get you off.  I want you to tell me where my mouth should be and what it should be doing for."
                wt_image intro_wife_pleasure_her_1_4
                ivy.c "And if I tell you I want your mouth between my legs?"
                player.c "Then all you need to do is take my head in your hand and make sure my mouth is exactly where you want it to be, doing exactly what you want it to do."
                wt_image intro_wife_pleasure_her_1_5
                ivy.c "I want your mouth right here."
                wt_image intro_wife_pleasure_her_1_6
                ivy.c "Slower.  Just tease me."
                wt_image intro_wife_pleasure_her_1_7
                ivy.c "Ohhh ... enough teasing!  Go faster, use your tongue on my clit.  Faster ... harder ..."
                wt_image intro_wife_pleasure_her_1_8
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_pleasure_her_1_4
                ivy.c "You didn't mind me telling you what I wanted you to do?"
                player.c "I enjoyed it.  It was hot being a toy for you to pleasure yourself with.  You're a natural at it.  You should take charge more often."
                if not ivy.has_tag('instructed_you_on_pussy_licking'):
                    add tags 'instructed_you_on_pussy_licking' to ivy
                    $ ivy.domme_comfort += 1
            "Use your tongue on her asshole" if ivy.has_tag('discussed_anal'):
                wt_image intro_wife_pleasure_her_2_1
                player.c "You're a beautiful woman, Ivy.  I'm looking forward to tasting your body."
                wt_image intro_wife_pleasure_her_2_2
                ivy.c "Mmmm.  I'm looking forward to that, too."
                wt_image intro_wife_pleasure_her_2_3
                player.c "Every part of your body is so sexy.  Climb up here so I can access it."
                wt_image intro_wife_pleasure_her_3_1
                ivy.c "Shouldn't I be turned over?"
                player.c "This is perfect.  I can reach all of you this way."
                wt_image intro_wife_pleasure_her_3_2
                ivy.c "What are you doing???"
                wt_image intro_wife_pleasure_her_3_3
                player.c "Tonguing your ass.  Doesn't it feel nice?"
                ivy.c "No!  I mean ... I don't know what it feels like."
                wt_image intro_wife_pleasure_her_3_4
                if ivy.anal_count > 0:
                    player.c "The anus is a very erogenous zone, Ivy.  My tongue is a lot smaller than my cock, but it'll help you enjoy the sensation of having your butt penetrated.  Relax and let me make you cum with my tongue in your ass."
                elif ivy.has_item(butt_plug):
                    player.c "The anus is a very erogenous zone, Ivy.  My tongue is a lot smaller than the butt plug, but it'll help you enjoy the sensation of having your butt penetrated.  Relax and let me make you cum with my tongue in your ass."
                else:
                    player.c "The anus is a very erogenous zone, Ivy.  It can feel really nice having something penetrate it back there.  Relax and let me make you cum with my tongue in your ass."
                wt_image intro_wife_pleasure_her_3_5
                ivy.c "Wow.  That's not unpleasant, but it feels too weird.  I won't be able to cum this way.  Lick me normally."
                wt_image intro_wife_pleasure_her_2_5
                "She won't relax enough to cum with your tongue up her ass, but she's turned on enough that she cums quickly when you push your tongue into her snatch."
                wt_image intro_wife_pleasure_her_2_4
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_pleasure_her_2_6
                ivy.c "Mmmmm.  That felt good, even if the whole ass-play stuff was kinda weird."
                add tags 'anal_tongued_her' to ivy
            "Just let her lie back and relax":
                wt_image intro_wife_pleasure_her_2_1
                player.c "You're a beautiful woman, Ivy.  I'd like you to lie back and relax and let me make you feel good."
                wt_image intro_wife_pleasure_her_2_6
                ivy.c "Okay.  That sounds good."
                wt_image intro_wife_pleasure_her_2_7
                ivy.c "Mmmmm ... and that feels even better."
                wt_image intro_wife_pleasure_her_2_5
                "Ivy's a sexually responsive woman, comfortable with her body and how it responds to being touched."
                wt_image intro_wife_pleasure_her_2_8
                "It can take some women a while before they can relax into such intimate contact, especially with a new partner."
                wt_image intro_wife_pleasure_her_2_9
                "There's no such delay with Ivy, whose sex provides a steadily increasing stream of fluid for you to lap up as she builds towards a quick, but intense orgasm."
                wt_image intro_wife_pleasure_her_2_4
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_pleasure_her_2_6
                ivy.c "Mmmmm.  That felt great!  Thank you."
        change ivy desire by 10
        $ ivy.orgasm_count += 1
        $ ivy.pleasure_her_count += 1
        change player energy by -energy_short
        notify
        end_day
    else:
        wt_image intro_wife_visit_1_4
        ivy.c "I'm not letting you touch me."
        call ivy_sex_failed_proceed from _call_ivy_sex_failed_proceed
    return

label ivy_train_blowjobs:
    if current_location != boudoir:
        sys "This type of action may work better in the boudoir, if you've added items to it.  Take her there?"
        $ title = "Take her to the boudoir?"
        menu:
            "Yes":
                call forced_movement(boudoir) from _call_forced_movement_946
            "No, stay here":
                pass
    player.c "Being able to give pleasure to someone else is a pretty important skill, wouldn't you agree, Ivy?"
    wt_image intro_wife_visit_1_8
    ivy.c "I suppose.  What's your point?"
    player.c "I'm going to train you to please a man."
    $ ivy.temporary_count = 2
    call ivy_sex_proceed_test from _call_ivy_sex_proceed_test_1
    if ivy.temporary_count < 1:
        wt_image intro_wife_visit_1_6
        ivy.c "I already know how to please a man."
        player.c "What makes you think so?"
        wt_image intro_wife_visit_1_41
        if ivy.blowjob_count > 0:
            ivy.c "Are you getting forgetful?  I seem to recall you enjoying what I did before.  Shall I give you a reminder?"
        else:
            ivy.c "I have some experience in the area.  Shall I show you?"
        player.c "As long as you're ready to take instructions."
        wt_image intro_wife_visit_1_16
        ivy.c "What?"
        player.c "I'm going to train you to suck a cock properly."
        ivy.c "I already know how to give head."
        player.c "How do you know?  Who's told you what to do, when you're doing things wrong, what you should be doing differently?"
        wt_image intro_wife_visit_1_15
        if ivy.blowjob_count > 0:
            ivy.c "Nobody's ever complained about my oral skills.  You certainly didn't before."
        else:
            ivy.c "Nobody's ever complained about my oral skills."
        player.c "Men don't tend to complain about a woman giving them head.  That doesn't mean you know what you're doing."
        if ivy.test('resistance', 70):
            $ ivy.training_session()
            wt_image intro_wife_visit_1_23
            ivy.c "You think my husband and other men have just been pretending to like what I do?"
            player.c "I'm sure they love what you do, but that doesn't mean you can't be better.  Would you like me to turn you into a well-trained cocksucker?"
            wt_image intro_wife_visit_1_44
            ivy.c "Wow.  You know that's triggering every feminist bone in my body, right?"
            player.c "Get on your knees, feminist, and take out my dick so I can show you how to suck it properly."
            wt_image intro_wife_bj_1_1
            player.c "Not like that.  Put your hand away and use your mouth only to start."
            wt_image intro_wife_bj_1_7
            player.c "Better, but start lower.  Warm up my balls before you start on the dick."
            wt_image intro_wife_bj_1_8
            ivy.c "Like this?"
            wt_image intro_wife_bj_1_9
            player.c "No, like this.  Good cocksuckers suckle and lick balls with enthusiasm"
            wt_image intro_wife_bj_1_8
            player.c "Okay, now you can use your hands to keep my balls warm while you turn your attention to my shaft."
            wt_image intro_wife_bj_1_10
            player.c "Up and down, just your tongue.  Lap at it like it's your favorite flavor lollipop."
            wt_image intro_wife_bj_1_11
            player.c "Good!  Paying extra attention to the underside of my cockhead is exactly what you should be doing there."
            wt_image intro_wife_bj_1_12
            ivy.c "So I'm not hopeless at cocksucking?"
            player.c "Not at all.  You just need some pointers to get you out of 'wife zone' and into 'head I'll never forget' zone."
            wt_image intro_wife_bj_1_6
            ivy.c "I like the sounds of that.  What else do I need to know to get out of 'wife zone'?"
            wt_image intro_wife_bj_1_13
            player.c "Keep your eyes on mine as you take me into your mouth."
            wt_image intro_wife_bj_1_14
            player.c "Don't break eye contact.  Keep working your tongue along the underside of my cock as you bob your head up and down.  If you can't get me all the way into your mouth yet without gagging, use your hands to substitute until you can."
            wt_image intro_wife_bj_1_15
            player.c "That's it.  That's a very good cocksucker.  Now show me how you're going to finish the blowjob so I never forget it."
            wt_image intro_wife_bj_1_16
            player.c "Eye contact, Ivy.  It's even more important at this stage than ever."
            wt_image intro_wife_bj_1_6
            player.c "Much better."
            wt_image intro_wife_bj_1_17
            player.c "[player.orgasm_text]"
            wt_image intro_wife_bj_1_18
            ivy.c "So is that how the porn stars do it?"
            player.c "I'm not sure you're at the porn star level, Ivy.  Not even experienced whore, really.  But definitely a talented amateur."
            wt_image intro_wife_bj_1_19
            ivy.c "That's okay.  I don't want to be a professional cocksucker.  I'm happy to be a trained amateur.  I think my husband's going to be really happy, too."
            "Well done.  Ivy's feeling like she's learned something from your training."
            add tags 'bj_training' to ivy
            $ ivy.blowjob_count += 1
            $ ivy.facial_count += 1
            $ ivy.sex_training_count += 1
            change ivy sos by 10
            orgasm
            change player energy by -energy_short
            notify
            end_day
        else:
            ivy.c "Look, I don't know what kind of weird playing hard to get this is.  I'll blow you if you want me to, but I'll do it my way."
            sys "She's too resistant to listen to your instructions.  Try something else if you still want to train her today.  Or let her blow you, if you don't."
            $ title = "What now?"
            menu:
                "Try something else":
                    wt_image intro_wife_visit_1_12
                    "Ivy re-dressed while you think about what to do next."
                "Let her blow you":
                    $ ivy.training_session()
                    player.c "Okay.  You win.  Show me what you can do."
                    wt_image intro_wife_visit_1_42
                    ivy.c "You won't be disappointed.  Make yourself comfortable."
                    wt_image intro_wife_bj_1_1
                    "Ivy's right that she knows her way around a man's cock ..."
                    wt_image intro_wife_bj_1_2
                    "... but then again, her blowjob is no different than the typical blowjob given by a wife or girlfriend."
                    wt_image intro_wife_bj_1_3
                    "There's a bit of eye contact and a lot of sucking and stroking with her hand ..."
                    wt_image intro_wife_bj_1_4
                    "... with the occasional attention to the underside of your cock head thrown in."
                    wt_image intro_wife_bj_1_1
                    "There's nothing special about it, but it's more than sufficient to bring you over the edge ..."
                    wt_image intro_wife_bj_1_5
                    "... as she suctions your load out of your balls and into her waiting mouth."
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_bj_1_6
                    ivy.c "See?  Told you I know how to suck a man's cock.  And I swallow, too."
                    wt_image intro_wife_visit_1_43
                    "Ivy didn't learn anything today, but there are worse ways to spend your evening than being paid to receive a blowjob from another man's wife."
                    orgasm
                    $ ivy.blowjob_count += 1
                    $ ivy.swallow_count += 1
                    notify
                    end_day
    else:
        wt_image intro_wife_visit_1_7
        ivy.c "Ha!  You're not going to get me to have sex with you under the guise of pretending I don't already know how to please a man."
        call ivy_sex_failed_proceed from _call_ivy_sex_failed_proceed_1
    return

label ivy_train_new_positions:
    if current_location != boudoir:
        sys "This type of action may work better in the boudoir, if you've added items to it.  Take her there?"
        $ title = "Take her to the boudoir?"
        menu:
            "Yes":
                call forced_movement(boudoir) from _call_forced_movement_947
            "No, stay here":
                pass
    if ivy.has_tag('watched_acrobatic_sex_show'):
        $ ivy.temporary_count = 2
        player.c "Have you been thinking about the acrobatic show we watched?"
        wt_image intro_wife_visit_1_6
        ivy.c "The one where it looked like the woman might get dropped on her head?  Why do you ask?"
        player.c "I thought we practice something similar, that you could then teach your husband."
    else:
        $ ivy.temporary_count = 4
        player.c "Let's impress your husband by teaching you some new sex positions.  I have an idea for some aerial sex that I think you'll both enjoy."
    call ivy_sex_proceed_test from _call_ivy_sex_proceed_test_2
    if ivy.temporary_count < 1:
        $ ivy.training_session()
        wt_image intro_wife_visit_1_9
        ivy.c "You're not going to drop me, are you?  I'm heavier than I look."
        if ivy.spank_count > 0:
            player.c "If I felt like hurting you, I'd just give you another spanking.  You'll be safe, I'll be right underneath you."
        else:
            player.c "You'll be safe, I'll be right underneath you."
        wt_image intro_wife_visit_1_16
        ivy.c "Is this something you've done before, or are you making this up?"
        player.c "Did you think I became a wife trainer without extensive study and practice?"
        wt_image intro_wife_visit_1_40
        ivy.c "I didn't realize your profession had such rigorous industry standards.  Where do we do this?"
        player.c "Come closer.  I won't bite.  Maybe just nibble a little bit."
        wt_image intro_wife_sex_1_1
        ivy.c "Mmmm.  That's nice."
        wt_image intro_wife_sex_1_2
        player.c "Ready for something else that'll feel nice?"
        ivy.c "As long as I don't fall down."
        wt_image intro_wife_sex_1_3
        player.c "I'll hold on to you.  Give me your leg, I'm going to put it on my shoulder."
        wt_image intro_wife_sex_1_4
        ivy.c "OH!!"
        wt_image intro_wife_sex_1_5
        player.c "You okay?"
        if ivy.has_tag('watched_acrobatic_sex_show'):
            ivy.c "Yes.  Just surprised.  You're not going to spin me upside down now, are you?"
        else:
            ivy.c "Yes.  Just surprised.  What happens next?"
        wt_image intro_wife_sex_1_6
        player.c "For starters, how about I just fuck you for a while?"
        wt_image intro_wife_sex_1_7
        ivy.c "Mmmmm.   That feels great.  Don't think I'll be able to cum in this position, though."
        wt_image intro_wife_sex_1_8
        player.c "That's just the warm up.  Let me put you down on top of me."
        ivy.c "So I can touch myself?"
        wt_image intro_wife_sex_1_9
        player.c "So I can get you airborne."
        ivy.c "OOHH!!!"
        wt_image intro_wife_sex_1_10
        ivy.c "Oh wow!!!  I can actually fuck you like this!"
        wt_image intro_wife_sex_1_11
        player.c "You can, and if you keep sliding up and down my cock like that, you're going to get me to cum, too.  But I'm not sure you will like this?"
        wt_image intro_wife_sex_1_10
        ivy.c "That's okay.  As long as it's feeling good for you, I don't mind."
        wt_image intro_wife_sex_1_11
        player.c "I'm not going to teach you a new sex position you can't cum in.  Time for the part you've been worried about ..."
        wt_image intro_wife_sex_1_12
        player.c " ... where I drop you on your head."
        wt_image intro_wife_sex_1_13
        ivy.c "OHHH!!"
        "You're actually gentle laying her head on the floor, doing so carefully, and not at all dropping her.  But you're also not at all gentle in how you fuck her once you get her in position."
        wt_image intro_wife_sex_1_14
        ivy.c "OHH WOW!!!!  You can get into me so deep like this!!"
        wt_image intro_wife_sex_1_15
        player.c "Wait 'til I turn around."
        wt_image intro_wife_sex_1_16
        ivy.c "Oh my god, I can watch you fuck me.  This is so weird, but hot, too!"
        wt_image intro_wife_sex_1_19
        ivy.c "OHHHH ... It feels like you're going to split me in two!"
        wt_image intro_wife_sex_1_17
        player.c "Do you need me to go slower?"
        ivy.c "No!  Keep pounding me!!"
        wt_image intro_wife_sex_1_18
        ivy.c "OH ... I'M CUMMINNGGG!!!"
        wt_image intro_wife_sex_1_19
        "She's not the only one."
        player.c "[player.orgasm_text]"
        wt_image intro_wife_visit_1_68
        if ivy.has_tag('watched_acrobatic_sex_show'):
            ivy.c "When you suggested doing something like that sex show act, I didn't think I'd be able to, or that I'd enjoy it even I could, but boy was I wrong!"
        else:
            ivy.c "When you said you wanted to teach me something new, I was skeptical you'd actually come up with something my husband and I hadn't done together, but boy was I wrong!"
        "Congratulations!  Ivy feels like she learned something."
        add tags 'had_adventurous_sex' to ivy
        change ivy sos by 10
        change ivy resistance by -5
        change ivy desire by 5
        $ ivy.sex_training_count += 1
        $ ivy.sex_count += 1
        $ ivy.orgasm_count += 1
        orgasm
        change player energy by -energy_short
        notify
        end_day
    else:
        wt_image intro_wife_visit_1_7
        if ivy.has_tag('watched_acrobatic_sex_show') and ivy.sex_training_count == 0 and ivy.sex_count == 0:
            ivy.c "Nice try, but you're not going to talk me into sleeping with you by promising to spin me around like a pinwheel."
        elif ivy.has_tag('watched_acrobatic_sex_show'):
            ivy.c "I don't think so.  That still sounds more dangerous than fun."
        elif ivy.sex_training_count == 0 and ivy.sex_count == 0:
            ivy.c "Nice try, but you're not going to talk me into sleeping with you by promising to do something that sounds dangerous."
        else:
            ivy.c "I don't think so.  That sounds more dangerous than fun."
        call ivy_sex_failed_proceed from _call_ivy_sex_failed_proceed_2
    return

label ivy_train_crawl:
    # requires 60 resistance to get here
    if current_location != dungeon:
        sys "This type of action may work better in the dungeon, if you've added items to it.  Take her there?"
        $ title = "Take her to the dungeon?"
        menu:
            "Yes":
                call forced_movement(dungeon) from _call_forced_movement_948
            "No, stay here":
                pass
    # first crawling
    if ivy.crawl_count == 0:
        if ivy.serve_count > 0:
            if ivy.serve_count  > 1:
                player.c "I enjoyed having you serve me, Ivy, and I'm sure your husband enjoyed it, too.  You also enjoyed it.  It's time to take the next step, so to speak."
            else:
                player.c "I enjoyed having you serve me, Ivy, and I think you enjoyed it, too.  It's time to take the next step, so to speak."
            wt_image intro_wife_visit_1_10
            ivy.c "Next step?"
            player.c "Figuratively speaking.  It's not really a step when you're on your hands and knees.  But crawling is an excellent way to show subservience."
        else:
            player.c "Let's work on you doing something special for your husband."
            wt_image intro_wife_visit_1_9
            ivy.c "Like what?"
            player.c "Like you getting down on all fours and crawling over to him to suck his cock."
        # initial test
        $ ivy.temporary_count = 5
        if ivy.has_tag('hypno_re_crawling'):
            $ ivy.temporary_count =- 2
        if ivy.has_tag('watched_crawling_sex_show'):
            $ ivy.temporary_count =- 1
        if ivy.has_tag('modelled_fishnet_lingerie'):
            if ivy.has_item(butt_plug):
                $ ivy.temporary_count =- 2
            else:
                $ ivy.temporary_count =- 1
        if ivy.serve_count > 0:
            $ ivy.temporary_count =- 1
        if ivy.has_tag('dommed_you'):
            $ ivy.temporary_count =- 1
        if ivy.temporary_count > 0:
            if ivy.test('submission', 25):
                $ ivy.temporary_count -= 3
            elif ivy.test('submission', 20):
                $ ivy.temporary_count -= 2
            elif ivy.test('submission', 15):
                $ ivy.temporary_count -= 1
        if ivy.temporary_count > 0:
            if ivy.test('resistance', 50):
                $ ivy.temporary_count -= 2
            elif ivy.test('resistance', 55):
                $ ivy.temporary_count -= 1
        # options to influence test and initial set up
        if ivy.temporary_count == 2:
            if ivy.has_tag('modelled_fishnet_lingerie') or ivy.has_tag('gave_her_sexy_lingerie'):
                pass
            elif ivy.has_tag('gave_her_fishnet_lingerie'):
                if not ivy.has_item(butt_plug) and player.has_item(butt_plug):
                    "You may be able to get her over her resistance by equipping her appropriately."
                    $ title = "Gift butt plug to Ivy?"
                    menu:
                        "Yes":
                            call ivy_crawl_preamble_owns_fishnets_giving_buttplug from _call_ivy_crawl_preamble_owns_fishnets_giving_buttplug
                        "No":
                            pass
                elif ivy.has_item(butt_plug):
                    call ivy_crawl_preamble_owns_fishnets_and_buttplug from _call_ivy_crawl_preamble_owns_fishnets_and_buttplug
            elif player.has_item(lingerie):
                if ivy.has_item(butt_plug):
                    "You may be able to get her over her resistance by equipping her appropriately."
                    $ title = "Gift lingerie to Ivy?"
                    menu:
                        "Yes":
                            call ivy_crawl_preamble_giving_fishnets_owns_buttplug from _call_ivy_crawl_preamble_giving_fishnets_owns_buttplug
                        "No":
                            pass
                elif player.has_item(butt_plug):
                    "You may be able to get her over her resistance by equipping her appropriately."
                    $ title = "Gift lingerie and butt plug to Ivy?"
                    menu:
                        "Yes":
                            call ivy_crawl_preamble_giving_fishnets_giving_buttplug from _call_ivy_crawl_preamble_giving_fishnets_giving_buttplug
                        "No":
                            pass
                else:
                    pass
        elif ivy.temporary_count == 1:
            if ivy.has_tag('modelled_fishnet_lingerie'):
                if player.has_item(butt_plug) and not ivy.has_item(butt_plug):
                    "You may be able to get her over her resistance by equipping her appropriately."
                    $ title = "Gift butt plug to Ivy?"
                    menu:
                        "Yes":
                            call ivy_crawl_preamble_modelled_fishnets_giving_buttplug from _call_ivy_crawl_preamble_modelled_fishnets_giving_buttplug
                        "No":
                            pass
            elif ivy.has_tag('gave_her_fishnet_lingerie'):
                call ivy_crawl_preamble_owns_fishnets from _call_ivy_crawl_preamble_owns_fishnets
            elif player.has_item(lingerie) and not ivy.has_item(lingerie):
                "You may be able to get her over her resistance by equipping her appropriately."
                $ title = "Gift lingerie to Ivy?"
                menu:
                    "Yes":
                        call ivy_crawl_preamble_giving_fishnets from _call_ivy_crawl_preamble_giving_fishnets
                    "No":
                        pass
            else:
                pass
        elif ivy.temporary_count < 1:
            call ivy_crawl_preamble_passed_test_initially from _call_ivy_crawl_preamble_passed_test_initially
        # proceed or fail
        if ivy.temporary_count < 1:
            # note: this picks up after the crawl_preamble labels content
            $ ivy.training_session()
            if ivy.has_tag('gave_her_fishnet_lingerie') and ivy.has_item(butt_plug):
                add tags 'crawled_wearing_tail' to ivy
                player.c "Do you feel like a respectable woman right now?"
                ivy.c "No"
                wt_image intro_wife_lingerie_2_41
                player.c "You don't look like one, either.  Get down on the floor.  Animals with tails shouldn't be standing up like respectable women, they should be on all fours."
                wt_image intro_wife_lingerie_2_44
                player.c "That's better.  You're nobody's wife, right now.  You're just a dumb animal learning her place.  Start moving."
                wt_image intro_wife_lingerie_2_42
                player.c "You heard me.  Put one hand in front of the other and start moving."
                wt_image intro_wife_lingerie_2_43
                player.c "You've got four legs, use them.  This shouldn't be complicated, even for a stupid bitch like you."
                wt_image intro_wife_lingerie_2_45
                player.c "Now you're moving.  Is that what it takes to get you crawling?  Remind you that you're a just a stupid bitch who belongs on the floor?"
                wt_image intro_wife_lingerie_2_46
                player.c "That's it.  Run around in circles."
                wt_image intro_wife_lingerie_2_47
                player.c "It's no surprise you've got so much energy.  You've needed someone to take you for a run for a long time."
                wt_image intro_wife_lingerie_2_48
                player.c "Good girl.  Show me how fast you can run."
                wt_image intro_wife_lingerie_2_49
                player.c "Getting tired, girl?  You're slowing down."
                wt_image intro_wife_lingerie_2_50
                player.c "Feisty bitch, aren't you?  Keep going, then.  Show me you're not getting tired."
                wt_image intro_wife_lingerie_2_51
                player.c "That's enough running.  Just crawl, now.  Crawl around in circles and show me what a good bitch you are."
                wt_image intro_wife_lingerie_2_52
                player.c "How does that feel, crawling in circles like a good bitch?"
                ivy.c "Humiliating.  Erotic.  I hope I can keep my nerve up enough to do this for my husband."
                $ title = "What now?"
                menu:
                    "Finish up the session":
                        wt_image intro_wife_lingerie_2_49
                        player.c "I'm sure you can.  Do you see the bulge in my pants?"
                        ivy.c "Yes"
                        wt_image intro_wife_lingerie_2_53
                        player.c "Your husband will be just as turned on watching you crawl around and wiggle your tail at him."
                        wt_image intro_wife_lingerie_2_50
                        player.c "What happens when he tells you to crawl over to him and ask for the opportunity to suck his cock?"
                        wt_image intro_wife_lingerie_2_47
                        ivy.c "I'll suck his cock like a wanton bitch."
                        wt_image intro_wife_lingerie_2_48
                        "Possibly yours, too, next time.  Ivy seems to be finding crawling therapeutic, so you let her continue for a while longer."
                        wt_image intro_wife_lingerie_2_52
                        ivy.c "Thanks for breaking through the walls my feminist side had built up.  Can I stop now?  My knees are starting to hurt and I want to do this again for my husband as soon as I get home."
                        sys "Congratulations, Ivy is feeling very trained."
                    "Tell her to suck your cock":
                        wt_image intro_wife_lingerie_2_44
                        player.c "Stop.  Crawl over here and ask for the opportunity to suck on my thick cock."
                        if ivy.test('desire', 15):
                            wt_image intro_wife_lingerie_2_51
                            player.c "Didn't you hear me, you stupid bitch?  I said crawl over to me like the the stupid bitch you are and ask for the opportunity to suck on my thick cock."
                            wt_image intro_wife_lingerie_2_25
                            "She crawls over closer to you, and closes her eyes while making an 'o' with her mouth."
                            wt_image intro_wife_lingerie_2_31
                            ivy.c "This stupid bitch would like your thick cock in her mouth."
                            player.c "Will you do a good job for me?"
                            if ivy.has_tag('bj_training'):
                                if ivy.serve_count > 1:
                                    ivy.c "Yes, Sir.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                                else:
                                    ivy.c "Yes.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                            else:
                                if ivy.serve_count > 1:
                                    ivy.c "Yes, Sir.  I may be a dumb bitch, but I know how to suck dick, Sir."
                                else:
                                    ivy.c "I may be a dumb bitch, but I know how to suck dick."
                            call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets
                        else:
                            wt_image intro_wife_lingerie_2_42
                            ivy.c "I am turned on right now, and feeling very, very trained.  But if I'm going to crawl to a man and ask for his cock, I'd like it to be my husband, first."
                            sys "Perhaps she'll do that for you, too, on another occasion.  For now, you should be happy that Ivy's feeling very well trained."
            elif ivy.has_tag('gave_her_fishnet_lingerie'):
                add tags 'crawled_as_slut' to ivy
                wt_image intro_wife_lingerie_2_6
                player.c "Right down, here, close to me."
                wt_image intro_wife_lingerie_2_20
                player.c "Turn around."
                wt_image intro_wife_lingerie_2_21
                player.c "I think you're right, Ivy.  That outfit does make you look like a slut."
                wt_image intro_wife_lingerie_2_22
                player.c "You don't look like a respectable woman.  You certainly don't look like someone's wife.  In fact, I don't even think you deserve to be at eye level with me, dressed the way you are.  Squat down."
                wt_image intro_wife_lingerie_2_23
                player.c "That's better, slut.  Looking up at a man's the right place for a slut like you.  You're nobody's wife, right now.  You're just a slut learning her place."
                wt_image intro_wife_lingerie_2_24
                player.c "Get lower, slut.  Get right down on the ground at my feet where a slut like you belongs."
                wt_image intro_wife_lingerie_2_25
                player.c "Now you're in your proper place, slut.  Follow me."
                wt_image intro_wife_lingerie_2_26
                player.c "One hand after the other, slut.  This shouldn't be complicated, even for a stupid slut like you."
                wt_image intro_wife_lingerie_2_27
                player.c "Now you're moving.  Is that all it takes to get you crawling is to remind you that you're a stupid slut?"
                wt_image intro_wife_lingerie_2_28
                player.c "Faster, you stupid slut.  Keep up with me."
                wt_image intro_wife_lingerie_2_29
                player.c "Better.  Keep going, right around in circles."
                wt_image intro_wife_lingerie_2_30
                player.c "And you didn't think you could crawl for a man."
                wt_image intro_wife_lingerie_2_26
                ivy.c "I really didn't think I could.  Thanks for breaking through the walls my feminist side had built up."
                $ title = "What now?"
                menu:
                    "End the session there":
                        wt_image intro_wife_lingerie_2_23
                        player.c "How did it feel, breaking through those walls and letting yourself be treated like a stupid slut?"
                        ivy.c "Humiliating.  Erotic.  I hope I can keep my nerve up enough to do that for my husband."
                        player.c "I'm sure you can.  Do you see the bulge in my pants?"
                        ivy.c "Yes"
                        player.c "Your husband will be just as turned on when you crawl over to him and ask for the opportunity to suck his cock."
                        ivy.c "Thank you.  I think I'm actually ready to do that for him."
                        sys "Possibly for you, too, next time.  Congratulations, Ivy is feeling very trained."
                    "Tell her to suck your cock":
                        player.c "Now that we're through those walls, crawl over here you stupid slut and ask for the opportunity to suck on my thick cock."
                        if ivy.test('desire', 15):
                            wt_image intro_wife_lingerie_2_25
                            "She hesitates for just a moment ..."
                            wt_image intro_wife_lingerie_2_27
                            "... then she crawls over beside you, and closes her eyes while making an 'o' with her mouth."
                            wt_image intro_wife_lingerie_2_31
                            ivy.c "This stupid slut would like your thick cock in her mouth."
                            player.c "Will you do a good job for me?"
                            if ivy.has_tag('bj_training'):
                                if ivy.serve_count > 1:
                                    ivy.c "Yes, Sir.  I may be a dumb slut, but I'm a well-trained cocksucker."
                                else:
                                    ivy.c "Yes.  I may be a dumb slut, but I'm a well-trained cocksucker."
                            else:
                                if ivy.serve_count > 1:
                                    ivy.c "Yes, Sir.  I may be a dumb slut, but I know how to suck dick, Sir."
                                else:
                                    ivy.c "YI may be a dumb slut, but I know how to suck dick"
                            call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets_1
                        else:
                            wt_image intro_wife_lingerie_2_23
                            ivy.c "I am turned on right now, and feeling very, very trained.  But if I'm going to crawl to a man and ask for his cock, I'd like it to be my husband, first."
                            sys "Perhaps she'll do that for you, too, on another occasion.  For now, you should be happy that Ivy's feeling very well trained."
            else:
                wt_image intro_wife_naked_1_1
                player.c "Turn around."
                wt_image intro_wife_naked_1_2
                player.c "Don't look at me.  Spread your legs and look at the floor."
                wt_image intro_wife_naked_1_3
                player.c "Good girl.  Now kneel down, keeping your knees apart."
                wt_image intro_wife_naked_1_4
                player.c "Very good.  You can look at me again."
                wt_image intro_wife_naked_1_5
                player.c "You're doing really well.  The next part's easy.  Reach out and put your hands on the floor."
                wt_image intro_wife_naked_1_6
                ivy.c "I'm not sure I can."
                player.c "Of course you can.  To please your husband, you can do a little thing like putting your hands on the floor."
                wt_image intro_wife_naked_1_7
                player.c "That's a good girl.  Now shift your weight onto your elbows."
                wt_image intro_wife_naked_1_8
                player.c "See how easy that was?  The next part's just as easy.  Put one hand in front of the other."
                wt_image intro_wife_naked_1_9
                player.c "That's it.  Keep going."
                wt_image intro_wife_naked_1_10
                player.c "Good girl.  Follow me over here."
                wt_image intro_wife_naked_1_11
                player.c "You're doing it, Ivy.  You're crawling for me."
                $ title = "What now?"
                menu:
                    "End the session there":
                        wt_image intro_wife_naked_1_12
                        player.c "How does that feel?"
                        ivy.c "Humiliating.  Erotic.  I hope I can keep my nerve up enough to do that for my husband."
                        player.c "I'm sure you can.  Do you see the bulge in my pants?"
                        ivy.c "Yes"
                        player.c "Your husband will be just as turned on when you crawl over to him and ask for the opportunity to suck his cock."
                        ivy.c "Thank you.  I think I'm actually ready to do that for him."
                        sys "Possibly for you, too, next time.  Congratulations, Ivy is feeling very trained."
                    "Tell her to suck your cock":
                        wt_image intro_wife_naked_1_8
                        player.c "Now crawl over here and ask for the opportunity to suck on my thick cock."
                        if ivy.test('desire', 15):
                            call ivy_crawl_blowjob_naked from _call_ivy_crawl_blowjob_naked
                        else:
                            ivy.c "I am turned on right now, and feeling very, very trained.  But if I'm going to crawl to a man and ask for his cock, I'd like it to be my husband, first."
                            sys "Perhaps she'll do that for you, too, on another occasion.  For now, you should be happy that Ivy's feeling very well trained."
            $ ivy.crawl_count = 1
            change ivy desire by 10
            change ivy submission by 10
            change ivy sos by 10
            change player energy by -energy_long
            notify
            end_day
        else:
            wt_image intro_wife_visit_1_7
            ivy.c "When I told you about that guy who wanted me to crawl for him, I told you I was repulsed by it.  I don't want to crawl for my husband."
            sys "This won't be an easy activity to train her in.  She's too Resistant to your suggestions and not Submissive enough to try this activity.  The right items would help, too.  Choose something else for today."
    # subsequent crawling
    else:
        $ ivy.training_session()
        wt_image intro_wife_visit_1_46
        player.c "You've spent all of your adult life on two feet.  You need more practice being down on all fours.  Strip."
        wt_image intro_wife_visit_1_25
        if ivy.has_tag('crawled_wearing_tail'):
            player.c "Go change into your fishnets while I get your tail ready, bitch."
            wt_image intro_wife_lingerie_2_2
            "She changes quickly ..."
            wt_image intro_wife_lingerie_2_20
            "... and gets into position."
            wt_image intro_wife_lingerie_2_15
            ivy.c "I still can't believe how much this turns me on."
            wt_image intro_wife_lingerie_2_18
            player.c "Stop talking and stop playing with your tail, you stupid bitch.  Get off the sofa and on the floor where you belong."
            wt_image intro_wife_lingerie_2_44
            player.c "Eager to run?"
            ivy.c "Yes"
            wt_image intro_wife_lingerie_2_42
            player.c "No talking.  Women talk.  A dumb bitch like you barks if she wants to communicate."
            ivy.c "But I couldn't ..."
            wt_image intro_wife_lingerie_2_43
            "*SMACK*"
            ivy.c "OW!"
            player.c "You heard me.  Are you eager to run, bitch?"
            wt_image intro_wife_lingerie_2_44
            ivy.c "Woof"
            player.c "I don't believe you.  Make me believe you."
            wt_image intro_wife_lingerie_2_52
            ivy.c "WOOF ... WOOF ... WOOF"
            player.c "Good girl, off you go."
            wt_image intro_wife_lingerie_2_45
            "She takes off running as fast as she can on all fours ..."
            wt_image intro_wife_lingerie_2_47
            "... running around in circles like before ..."
            wt_image intro_wife_lingerie_2_48
            "... fully embracing the humiliation of being treated like an animal."
            wt_image intro_wife_lingerie_2_53
            "You let her enjoy her time spent humiliating herself ..."
            wt_image intro_wife_lingerie_2_51
            "... until she starts to tire out."
            if not ivy.has_tag('barked'):
                add tags 'barked' to ivy
                change ivy sos by 10
                change ivy submission by 15
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_lingerie_2_52
                    player.c "Just one more lap, girl, then it's time to go home."
                    ivy.c "WOOF"
                    wt_image intro_wife_lingerie_2_47
                    "You're not sure what the bark meant, but she fairly sprints around the room for her final lap, before heading home to a husband who you expect will get very well fucked tonight."
                "Tell her to suck your cock":
                    wt_image intro_wife_lingerie_2_52
                    player.c "That's enough laps, girl.  Come over here and beg for the taste of my cock."
                    wt_image intro_wife_lingerie_2_25
                    ivy.c "woof?"
                    player.c "Crawl closer."
                    wt_image intro_wife_lingerie_2_31
                    ivy.c "woof?"
                    player.c "Now beg using human words."
                    ivy.c "This stupid bitch would like your thick cock in her mouth."
                    player.c "Will you do a good job for me?"
                    if ivy.has_tag('bj_training'):
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                        else:
                            ivy.c "Yes.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                    else:
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb bitch, but I know how to suck dick, Sir."
                        else:
                            ivy.c "I may be a dumb bitch, but I know how to suck dick."
                    call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets_2
        elif ivy.has_tag('crawled_as_slut'):
            player.c "Go change into your fishnets, slut.  You're going to crawl to me wearing them."
            wt_image intro_wife_lingerie_2_2
            "She changes quickly ..."
            wt_image intro_wife_lingerie_2_6
            "... and approaches."
            player.c "Did you miss the part where I said you're to crawl to me, you stupid slut?"
            wt_image intro_wife_lingerie_2_23
            ivy.c "I didn't know where you wanted me to start."
            player.c "What should a stupid slut like you do if she's not sure?"
            wt_image intro_wife_lingerie_2_24
            ivy.c "Get on my knees?"
            wt_image intro_wife_lingerie_2_25
            player.c "That's the best place for you, isn't it?"
            wt_image intro_wife_lingerie_2_28
            ivy.c "Yes"
            player.c "Yes, what?"
            wt_image intro_wife_lingerie_2_29
            ivy.c "Yes, this stupid slut should be made to crawl on her knees."
            wt_image intro_wife_lingerie_2_27
            player.c "Keep going, slut.  You don't mind spending the whole evening crawling, do you?"
            wt_image intro_wife_lingerie_2_26
            ivy.c "No, Sir.  This stupid slut is happy to crawl for your amusement."
            wt_image intro_wife_lingerie_2_28
            player.c "And how does your inner feminist feel about that, slut?"
            wt_image intro_wife_lingerie_2_29
            ivy.c "This stupid feminist slut is incredibly turned on to be humiliating herself for a man's amusement."
            wt_image intro_wife_lingerie_2_27
            "You let her enjoy her time spent humiliating herself until she starts to tire out."
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_lingerie_2_25
                    player.c "How are your knees?"
                    ivy.c "Sore"
                    player.c "I think that's enough for tonight."
                    wt_image intro_wife_lingerie_2_24
                    ivy.c "Thank you."
                    player.c "Are you going to crawl for you husband when you get home?"
                    wt_image intro_wife_lingerie_2_23
                    ivy.c "No.  I think I'm just going to tackle him."
                "Tell her to suck your cock":
                    wt_image intro_wife_lingerie_2_26
                    player.c "That's enough crawling in circles.  You can crawl over by my feet now ask for the opportunity to suck on my thick cock."
                    wt_image intro_wife_lingerie_2_25
                    player.c "Didn't you hear me, you stupid slut?  Get over here and beg for my cock."
                    wt_image intro_wife_lingerie_2_27
                    "She fairly dashed over to you, then closes her eyes while making an 'o' with her mouth."
                    wt_image intro_wife_lingerie_2_31
                    ivy.c "This stupid slut would like your thick cock in her mouth."
                    player.c "Will you do a good job for me?"
                    if ivy.has_tag('bj_training'):
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb slut, but I'm a well-trained cocksucker."
                        else:
                            ivy.c "Yes.  I may be a dumb slut, but I'm a well-trained cocksucker."
                    else:
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb slut, but I know how to suck dick, Sir."
                        else:
                            ivy.c "I may be a dumb slut, but I know how to suck dick."
                    call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets_3
        else:
            player.c "Don't just stand there like a deer in the headlights.  Come over here in front of me."
            wt_image intro_wife_naked_1_1
            player.c "You remember how this works.  I don't want to be looking at you standing up.  I want you to lower yourself for me, literally."
            wt_image intro_wife_naked_1_2
            player.c "You don't have to turn around."
            ivy.c "I find it easier like this."
            wt_image intro_wife_naked_1_3
            player.c "Did you face away from your husband before kneeling for him?"
            wt_image intro_wife_naked_1_4
            ivy.c "Yes.  It was even harder to do this for him than it is for you."
            wt_image intro_wife_naked_1_5
            player.c "Let me try and make it easier for you.  I don't want to looking at you kneeling up, either.  I want to see you crawling on the ground for my amusement."
            wt_image intro_wife_naked_1_7
            ivy.c "What was easier was when you walked me through the steps.  Somehow it felt more acceptable to being doing things in small stages."
            wt_image intro_wife_naked_1_8
            player.c "If this was acceptable, it wouldn't be as exciting.  You're a smart feminist.  You know each of those steps lead you to here, don't you?"
            ivy.c "Yes"
            player.c "And you know what's expected of you once you get here, don't you?"
            ivy.c "Yes, but ..."
            player.c "Crawl, Ivy, and do it now. "
            wt_image intro_wife_naked_1_10
            player.c "That's it.  Humiliate yourself for my enjoyment."
            wt_image intro_wife_naked_1_11
            player.c "Come this way.  Follow me."
            wt_image intro_wife_naked_1_13
            player.c "How does your inner feminist feel about following me on your hands and knees?"
            wt_image intro_wife_naked_1_12
            ivy.c "I'm incredibly turned on."
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_naked_1_8
                    player.c "Are you going to crawl for you husband when you get home?"
                    ivy.c "Yes, and I'm going to beg him for his cock, too.  Thank you for training me to do this."
                "Tell her to suck your cock":
                    wt_image intro_wife_naked_1_8
                    player.c "Stay there."
                    wt_image intro_wife_naked_1_9
                    player.c "Now crawl over here and ask for the opportunity to suck on my thick cock."
                    call ivy_crawl_blowjob_naked from _call_ivy_crawl_blowjob_naked_1
        $ ivy.crawl_count += 1
        change player energy by -energy_short
        notify
        end_day
    return

label ivy_crawl_preamble_owns_fishnets_giving_buttplug:
    add tags 'modelled_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 2
    ivy.c "I'm not comfortable crawling for a man."
    player.c "I know, but I think we can work on that.  At least go change into that lingerie I bought you."
    ivy.c "I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    wt_image intro_wife_lingerie_2_6
    player.c "Don't be shy, come over here and turn around."
    wt_image intro_wife_lingerie_2_14
    ivy.c "What's that?"
    player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
    wt_image intro_wife_lingerie_2_15
    ivy.c "What are you doing with it?"
    wt_image intro_wife_lingerie_2_16
    player.c "That's a silly question."
    change ivy submission by 5
    give 1 butt_plug from player to ivy
    wt_image intro_wife_lingerie_2_17
    ivy.c "OH!  That feels weird!!"
    player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
    wt_image intro_wife_lingerie_2_18
    ivy.c "What did you tie to it?"
    player.c "It's a tail, to help put you in the right frame of mind."
    wt_image intro_wife_lingerie_2_19
    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_owns_fishnets_owns_buttplug:
    add tags 'modelled_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 2
    ivy.c "I'm not comfortable crawling for a man."
    player.c "I know, but I think we can work on that.  Do you have your butt plug?"
    ivy.c "I'm not wearing it, but I have it in my purse."
    player.c "Hand it to me, then go change into that lingerie I bought you."
    ivy.c "I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    wt_image intro_wife_lingerie_2_6
    player.c "Don't be shy, come over here and turn around."
    wt_image intro_wife_lingerie_2_14
    player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
    wt_image intro_wife_lingerie_2_15
    ivy.c "What did you do with it?"
    wt_image intro_wife_lingerie_2_16
    player.c "Added something special to it."
    wt_image intro_wife_lingerie_2_18
    ivy.c "You tied something to it?"
    player.c "It's a tail, to help put you in the right frame of mind."
    wt_image intro_wife_lingerie_2_19
    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_giving_fishnets_owns_buttplug:
    add tags 'modelled_fishnet_lingerie' 'gave_her_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 2
    ivy.c "I'm not comfortable crawling for a man."
    player.c "I know, but I think we can work on that.  Do you have your butt plug?"
    ivy.c "I'm not wearing it, but I have it in my purse."
    player.c "Hand it to me, and in return I have something for you."
    give 1 lingerie from player to ivy
    ivy.c "Is there even anything to this outfit?  I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    wt_image intro_wife_lingerie_2_6
    player.c "Don't be shy, come over here and turn around."
    wt_image intro_wife_lingerie_2_14
    player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
    wt_image intro_wife_lingerie_2_15
    ivy.c "What did you do with it?"
    wt_image intro_wife_lingerie_2_16
    player.c "Added something special to it."
    wt_image intro_wife_lingerie_2_18
    ivy.c "You tied something to it?"
    player.c "It's a tail, to help put you in the right frame of mind."
    wt_image intro_wife_lingerie_2_19
    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_giving_fishnets_giving_buttplug:
    add tags 'modelled_fishnet_lingerie' 'gave_her_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 2
    ivy.c "I'm not comfortable crawling for a man."
    player.c "I know, but I think we can work on that.  Go change into this outfit I bought you."
    give 1 lingerie from player to ivy
    ivy.c "Is there even anything to this outfit?  I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    wt_image intro_wife_lingerie_2_6
    player.c "Don't be shy, come over here and turn around."
    wt_image intro_wife_lingerie_2_14
    ivy.c "What's that?"
    player.c "It's another gift for you.  It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
    wt_image intro_wife_lingerie_2_15
    ivy.c "What are you doing with it?"
    wt_image intro_wife_lingerie_2_16
    player.c "That's a silly question."
    change ivy submission by 5
    give 1 butt_plug from player to ivy
    wt_image intro_wife_lingerie_2_17
    ivy.c "OH!  That feels weird!!"
    player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
    wt_image intro_wife_lingerie_2_18
    ivy.c "What did you tie to it?"
    player.c "It's a tail, to help put you in the right frame of mind."
    wt_image intro_wife_lingerie_2_19
    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_modelled_fishnets_giving_buttplug:
    $ ivy.temporary_count -= 1
    ivy.c "I'm not comfortable crawling for a man."
    player.c "I know, but I think we can work on that.  Go change into your lingerie."
    wt_image current_location.image
    "Ivy ducks into the bathroom ..."
    wt_image intro_wife_lingerie_2_1
    "... reappearing few minutes later, wearing her fishnets again."
    wt_image intro_wife_lingerie_2_6
    player.c "Come over here and turn around."
    wt_image intro_wife_lingerie_2_14
    ivy.c "What's that?"
    player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
    wt_image intro_wife_lingerie_2_15
    ivy.c "What are you doing with it?"
    wt_image intro_wife_lingerie_2_16
    player.c "That's a silly question."
    change ivy submission by 5
    give 1 butt_plug from player to ivy
    wt_image intro_wife_lingerie_2_17
    ivy.c "OH!  That feels weird!!"
    player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
    wt_image intro_wife_lingerie_2_18
    ivy.c "What did you tie to it?"
    player.c "It's a tail, to help put you in the right frame of mind."
    wt_image intro_wife_lingerie_2_19
    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_owns_fishnets:
    add tags 'modelled_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 1
    ivy.c "I'm not comfortable crawling for a man."
    if ivy.has_item(butt_plug):
        player.c "I know, but I think we can work on that.  Do you have your butt plug?"
        ivy.c "I'm not wearing it, but I have it in my purse."
        player.c "Hand it to me, then go change into that lingerie I bought you."
    else:
        player.c "I know, but I think we can work on that.  At least go change into that lingerie I bought you."
    ivy.c "I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    if not ivy.has_item(butt_plug) and player.has_item(butt_plug):
        $ title = "Give her a butt plug, too?"
        menu:
            "Yes":
                wt_image intro_wife_lingerie_2_6
                player.c "Don't be shy, come over here and turn around."
                wt_image intro_wife_lingerie_2_14
                ivy.c "What's that?"
                player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
                wt_image intro_wife_lingerie_2_15
                ivy.c "What are you doing with it?"
                wt_image intro_wife_lingerie_2_16
                player.c "That's a silly question."
                change ivy submission by 5
                give 1 butt_plug from player to ivy
                wt_image intro_wife_lingerie_2_17
                ivy.c "OH!  That feels weird!!"
                player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
                wt_image intro_wife_lingerie_2_18
                ivy.c "What did you tie to it?"
                player.c "It's a tail, to help put you in the right frame of mind."
                wt_image intro_wife_lingerie_2_19
                ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
            "No":
                wt_image intro_wife_lingerie_2_2
                player.c "Don't be shy, come over here."
    elif ivy.has_item(butt_plug):
        wt_image intro_wife_lingerie_2_6
        player.c "Don't be shy, come over here and turn around."
        wt_image intro_wife_lingerie_2_14
        player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
        wt_image intro_wife_lingerie_2_15
        ivy.c "What did you do with it?"
        wt_image intro_wife_lingerie_2_16
        player.c "Added something special to it."
        wt_image intro_wife_lingerie_2_18
        ivy.c "You tied something to it?"
        player.c "It's a tail, to help put you in the right frame of mind."
        wt_image intro_wife_lingerie_2_19
        ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    else:
        wt_image intro_wife_lingerie_2_2
        player.c "Don't be shy, come over here."
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_giving_fishnets:
    $ ivy.temporary_count -= 1
    add tags 'modelled_fishnet_lingerie' 'gave_her_fishnet_lingerie' to ivy
    $ ivy.temporary_count -= 1
    ivy.c "I'm not comfortable crawling for a man."
    if ivy.has_item(butt_plug):
        player.c "I know, but I think we can work on that.  Do you have your butt plug?"
        ivy.c "I'm not wearing it, but I have it in my purse."
        player.c "Hand it to me, and in return I have something for you."
    else:
        player.c "I know, but I think we can work on that.  Go change into this outfit I bought you."
    give 1 lingerie from player to ivy
    ivy.c "Is there even anything to this outfit?  I'll just look like a slut wearing that."
    player.c "Trust me.  Go change and see how you feel."
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_2_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This makes me look like even more of a slut than I expected."
    if not ivy.has_item(butt_plug) and player.has_item(butt_plug):
        $ title = "Give her a butt plug, too?"
        menu:
            "Yes":
                wt_image intro_wife_lingerie_2_6
                player.c "Don't be shy, come over here and turn around."
                wt_image intro_wife_lingerie_2_14
                ivy.c "What's that?"
                player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
                wt_image intro_wife_lingerie_2_15
                ivy.c "What are you doing with it?"
                wt_image intro_wife_lingerie_2_16
                player.c "That's a silly question."
                change ivy submission by 5
                give 1 butt_plug from player to ivy
                wt_image intro_wife_lingerie_2_17
                ivy.c "OH!  That feels weird!!"
                player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
                wt_image intro_wife_lingerie_2_18
                ivy.c "What did you tie to it?"
                player.c "It's a tail, to help put you in the right frame of mind."
                wt_image intro_wife_lingerie_2_19
                ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
            "No":
                wt_image intro_wife_lingerie_2_2
                player.c "Don't be shy, come over here."
    elif ivy.has_item(butt_plug):
        wt_image intro_wife_lingerie_2_6
        player.c "Don't be shy, come over here and turn around."
        wt_image intro_wife_lingerie_2_14
        player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
        wt_image intro_wife_lingerie_2_15
        ivy.c "What did you do with it?"
        wt_image intro_wife_lingerie_2_16
        player.c "Added something special to it."
        wt_image intro_wife_lingerie_2_18
        ivy.c "You tied something to it?"
        player.c "It's a tail, to help put you in the right frame of mind."
        wt_image intro_wife_lingerie_2_19
        ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
    else:
        wt_image intro_wife_lingerie_2_2
        player.c "Don't be shy, come over here."
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_passed_test_initially:
    wt_image intro_wife_visit_1_11
    ivy.c "I'm not comfortable crawling for a man."
    if not ivy.has_item(lingerie) and player.has_item(lingerie):
        "She's not comfortable, but you can tell she's ready to do it.  Do you want to dress her up beforehand?"
        $ title = "Gift her lingerie to crawl in?"
        menu:
            "Yes":
                if ivy.has_item(butt_plug):
                    player.c "I know, but I think we can work on that.  Do you have your butt plug?"
                    ivy.c "I'm not wearing it, but I have it in my purse."
                    player.c "Hand it to me, and in return I have something for you."
                else:
                    player.c "I know, but I think we can work on that.  Go change into this outfit I bought you."
                give 1 lingerie from player to ivy
                add tags 'gave_her_fishnet_lingerie' 'modelled_fishnet_lingerie' to ivy
                ivy.c "Is there even anything to this outfit?  I'll just look like a slut wearing that."
                player.c "Trust me.  Go change and see how you feel."
                wt_image current_location.image
                "Ivy disappears into the bathroom to change.  She's gone a long time."
                wt_image intro_wife_lingerie_2_1
                "Eventually, she timidly steps back into the room."
                ivy.c "This makes me look like even more of a slut than I expected."
                if not ivy.has_item(butt_plug) and player.has_item(butt_plug):
                    $ title = "Give her a butt plug, too?"
                    menu:
                        "Yes":
                            wt_image intro_wife_lingerie_2_6
                            player.c "Don't be shy, come over here and turn around."
                            wt_image intro_wife_lingerie_2_14
                            ivy.c "What's that?"
                            player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
                            wt_image intro_wife_lingerie_2_15
                            ivy.c "What are you doing with it?"
                            wt_image intro_wife_lingerie_2_16
                            player.c "That's a silly question."
                            change ivy submission by 5
                            give 1 butt_plug from player to ivy
                            wt_image intro_wife_lingerie_2_17
                            ivy.c "OH!  That feels weird!!"
                            player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
                            wt_image intro_wife_lingerie_2_18
                            ivy.c "What did you tie to it?"
                            player.c "It's a tail, to help put you in the right frame of mind."
                            wt_image intro_wife_lingerie_2_19
                            ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
                        "No":
                            wt_image intro_wife_lingerie_2_2
                            player.c "Don't be shy, come over here."
                elif ivy.has_item(butt_plug):
                    wt_image intro_wife_lingerie_2_6
                    player.c "Don't be shy, come over here and turn around."
                    wt_image intro_wife_lingerie_2_14
                    player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
                    wt_image intro_wife_lingerie_2_15
                    ivy.c "What did you do with it?"
                    wt_image intro_wife_lingerie_2_16
                    player.c "Added something special to it."
                    wt_image intro_wife_lingerie_2_18
                    ivy.c "You tied something to it?"
                    player.c "It's a tail, to help put you in the right frame of mind."
                    wt_image intro_wife_lingerie_2_19
                    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
                else:
                    wt_image intro_wife_lingerie_2_2
                    player.c "Don't be shy, come over here."
            "No":
                call ivy_crawl_preamble_no_lingerie from _call_ivy_crawl_preamble_no_lingerie
    elif ivy.has_tag('modelled_fishnet_lingerie'):
        if ivy.has_item(butt_plug):
            player.c "I know, but I think we can work on that.  Do you have your butt plug?"
            ivy.c "I'm not wearing it, but I have it in my purse."
            player.c "Hand it to me, then go change into the lingerie I bought you."
        else:
            player.c "I know, but I think we can work on that.  Go change into your lingerie."
        wt_image current_location.image
        "Ivy ducks into the bathroom ..."
        wt_image intro_wife_lingerie_2_1
        "... reappearing few minutes later, wearing her fishnets again."
        if ivy.has_item(butt_plug):
            wt_image intro_wife_lingerie_2_6
            player.c "Come over here and turn around."
            wt_image intro_wife_lingerie_2_14
            player.c "Lean forward against the sofa.  I'm going to put your butt plug in."
            wt_image intro_wife_lingerie_2_15
            ivy.c "What did you do with it?"
            wt_image intro_wife_lingerie_2_16
            player.c "Added something special to it."
            wt_image intro_wife_lingerie_2_18
            ivy.c "You tied something to it?"
            player.c "It's a tail, to help put you in the right frame of mind."
            wt_image intro_wife_lingerie_2_19
            ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
        elif player.has_item(butt_plug):
            $ title = "Give her a butt plug?"
            menu:
                "Yes":
                    wt_image intro_wife_lingerie_2_6
                    player.c "Don't be shy, come over here and turn around."
                    wt_image intro_wife_lingerie_2_14
                    ivy.c "What's that?"
                    player.c "It's a butt plug.  I've added something special to it to help get you in the mood.  Lean forward against the sofa."
                    wt_image intro_wife_lingerie_2_15
                    ivy.c "What are you doing with it?"
                    wt_image intro_wife_lingerie_2_16
                    player.c "That's a silly question."
                    change ivy submission by 5
                    give 1 butt_plug from player to ivy
                    wt_image intro_wife_lingerie_2_17
                    ivy.c "OH!  That feels weird!!"
                    player.c "Relax.  It's in there snug and secure. It can't slip further in and won't fall out, either.  Practise wearing it at home, and it won't feel so weird."
                    wt_image intro_wife_lingerie_2_18
                    ivy.c "What did you tie to it?"
                    player.c "It's a tail, to help put you in the right frame of mind."
                    wt_image intro_wife_lingerie_2_19
                    ivy.c "Dressing me up like a slut and giving me a tail is supposed to put me in the right frame of mind?"
                "No":
                    wt_image intro_wife_lingerie_2_2
                    player.c "Don't be shy, come over here."
        else:
            wt_image intro_wife_lingerie_2_2
            player.c "Don't be shy, come over here."
    elif ivy.has_tag('gave_her_fishnet_lingerie'):
        call ivy_crawl_preamble_owns_fishnets from _call_ivy_crawl_preamble_owns_fishnets_1
    else:
        call ivy_crawl_preamble_no_lingerie from _call_ivy_crawl_preamble_no_lingerie_1
    # now returns to train_crawl label
    return

label ivy_crawl_preamble_no_lingerie:
    wt_image intro_wife_visit_1_12
    player.c "I know, but I think we can work on that.  It'll help if you take off your clothes."
    wt_image intro_wife_visit_1_16
    ivy.c "I'm really not comfortable with the idea of humiliating myself."
    wt_image intro_wife_visit_1_24
    player.c "You just need the right frame of mind.  Finish getting your clothes off, then come stand here in front of me."
    # now returns to train_crawl label
    return

label ivy_crawl_blowjob_naked:
    wt_image intro_wife_naked_1_9
    "She hesitates for a moment ..."
    wt_image intro_wife_naked_1_13
    "... then she crawls up between your legs."
    wt_image intro_wife_naked_1_14
    if ivy.serve_count > 1:
        ivy.c "May I please be allowed to suck your thick cock, Sir?"
    else:
        ivy.c "May I please be allowed to suck your thick cock?"
    player.c "Will you do a good job for me?"
    if ivy.has_tag('bj_training'):
        if ivy.serve_count > 1:
            ivy.c "Yes, Sir.  I'm a well-trained cocksucker."
        else:
            ivy.c "Yes.  I'm a well-trained cocksucker."
    else:
        if ivy.serve_count > 1:
            ivy.c "I'll do my absolute best to please your cock, Sir."
        else:
            ivy.c "I'll do my absolute best to please your cock."
    if ivy.has_tag('bj_training'):
        wt_image intro_wife_bj_1_9
        "She remembers her training, and starts with your balls."
        wt_image intro_wife_bj_1_8
        if ivy.serve_count > 1:
            ivy.c "Would you like me to move to your cock now, Sir?"
        else:
            ivy.c "Would you like me to move to your cock now?"
        player.c "A little longer on my balls."
        wt_image intro_wife_bj_1_9
        if ivy.serve_count > 1:
            ivy.c "Yes, Sir."
        else:
            ivy.c "Okay"
        wt_image intro_wife_bj_1_8
        player.c "Okay, you can pleasure my shaft now."
        wt_image intro_wife_bj_1_10
        if ivy.serve_count > 1:
            ivy.c "Yes, Sir."
        else:
            ivy.c "Okay"
        wt_image intro_wife_bj_1_11
        "She licks you up and down, paying extra attention to the underside of your cockhead."
        wt_image intro_wife_bj_1_12
        if ivy.serve_count > 1:
            ivy.c "May I please be allowed to suck on you now, Sir?"
        else:
            ivy.c "May I please be allowed to suck on you now?"
        player.c "Yes, but take your time.  I'm worked up from watching you crawl at my feet, and don't want to cum too quickly in that talented cocksucking mouth of yours."
        wt_image intro_wife_bj_1_12
        if ivy.serve_count > 1:
            ivy.c "The feminist in me is surprised by how aroused I am by your compliments, Sir."
        else:
            ivy.c "The feminist in me is surprised by how aroused I am by your compliments."
        wt_image intro_wife_bj_1_14
        player.c "You enjoy being a submissive, crawling cocksucker, don't you, Ivy?"
        wt_image intro_wife_bj_1_15
        "She nods without stopping the blowjob or breaking eye contact.  Her submissive behavior overwhelms your remaining resolve."
        player.c "Finish me off like the submissive cocksucker you are, Ivy."
        wt_image intro_wife_bj_1_6
        ivy.c "Yes, Sir."
        wt_image intro_wife_bj_1_17
        player.c "[player.orgasm_text]"
        wt_image intro_wife_bj_1_18
        if ivy.status == "on_training":
            ivy.c "Thank you for training me to crawl."
            "She seems to genuinely mean it.  Her husband will appreciate it, too."
            change ivy submission by 5
        else:
            if ivy.serve_count > 1:
                ivy.c "I trust this cocksucker humiliated herself to your satisfaction, Sir."
            else:
                ivy.c "I trust this cocksucker humiliated herself to your satisfaction."
            "She cleans herself up, then gets dressed and goes home, leaving you to continue your day."
        $ ivy.facial_count += 1
    else:
        wt_image intro_wife_bj_1_1
        "Ivy wraps her lips around your cock head ..."
        wt_image intro_wife_bj_1_2
        "... and begins to blow you."
        wt_image intro_wife_bj_1_3
        "There's a bit of eye contact and a lot of sucking and stroking with her hand ..."
        wt_image intro_wife_bj_1_4
        "... with the occasional attention to the underside of your cock head thrown in."
        wt_image intro_wife_bj_1_1
        "As turned on as you are from watching her crawl at your feet, it's more than sufficient to quickly bring you over the edge ..."
        wt_image intro_wife_bj_1_5
        "... as she suctions your load out of your balls and into her waiting mouth."
        player.c "[player.orgasm_text]"
        wt_image intro_wife_bj_1_6
        if ivy.status == "on_training":
            ivy.c "Thank you for letting me suck your cock.  I swallowed your whole load.  And thank you for training me to crawl."
            "She seems to genuinely mean it.  Her husband will appreciate it, too."
        else:
            "She shows off that she swallowed your load, then gets dressed and goes home, leaving you to go on with her day."
        $ ivy.swallow_count += 1
    $ ivy.blowjob_count += 1
    orgasm
    return

label ivy_crawl_blowjob_fishnets:
    if ivy.has_tag('bj_training'):
        wt_image intro_wife_lingerie_2_32
        "She remembers her training and begins by warming up your balls."
        wt_image intro_wife_lingerie_2_33
        "Then she licks up and down your shaft from base to tip ..."
        wt_image intro_wife_lingerie_2_34
        "... then wraps her lips around the head of your cock and begins to suckle."
        wt_image intro_wife_lingerie_2_35
        "Between watching her crawl and the feel of her talented mouth, it's not long before you're ready to cum."
        wt_image intro_wife_lingerie_2_33
        if ivy.has_item(butt_plug):
            player.c "Get into position, bitch."
        else:
            player.c "Get into position, slut."
        wt_image intro_wife_lingerie_2_37
        player.c "[player.orgasm_text]"
    else:
        wt_image intro_wife_lingerie_2_34
        "Ivy takes your cock into her mouth ..."
        if ivy.has_item(butt_plug):
            wt_image intro_wife_lingerie_2_40
        else:
            wt_image intro_wife_lingerie_2_39
        "... and begins to suck on it."
        wt_image intro_wife_lingerie_2_33
        "Between her tongue ..."
        wt_image intro_wife_lingerie_2_34
        "... her lips ..."
        wt_image intro_wife_lingerie_2_35
        ".. and her hand, she soon has you ready to cum."
        wt_image intro_wife_lingerie_2_33
        if ivy.has_item(butt_plug):
            player.c "Remove your mouth.  I'm going to show you how a man enjoys using a bitch."
        else:
            player.c "Remove your mouth.  I'm going to show you how a man enjoys using a slut."
        wt_image intro_wife_lingerie_2_36
        player.c "[player.orgasm_text]"
    wt_image intro_wife_lingerie_2_38
    if ivy.status == "on_training":
        if ivy.has_item(butt_plug):
            ivy.c "Thank you for training me to behave like a stupid bitch who'll crawl to a man's cock."
        else:
            ivy.c "Thank you for training me to act like a stupid slut who'll crawl to a man's cock."
        "She seems to genuinely mean it.  Her husband will appreciate her training, too."
        change ivy submission by 5
    else:
        ivy.c "I really don't like that you can call me up and I'll humiliate myself like this, and yet I also love it, too."
    $ ivy.facial_count += 1
    $ ivy.blowjob_count += 1
    orgasm
    return

label ivy_train_strip:
    # can't get here unless resistance < 70 and discussed
    # hypno, strip club, and lingerie all impact, plus desire and resistance
    player.c "I think your husband would love to get a strip tease from you, Ivy.  And I know you'd love using your body to tease him and get him hard. Let's get you comfortable with the idea by practicing for me."
    $ ivy.temporary_count = 4
    call ivy_strip_proceed_test from _call_ivy_strip_proceed_test_1
    if ivy.temporary_count > 2:
        wt_image intro_wife_visit_1_10
        ivy.c "I couldn't.  I'd look too stupid.  He'd probably laugh at me."
        if not ivy.has_item(lingerie) and player.has_item(lingerie):
            "She's still too resistant to the idea to even really consider it.  If you gave her some sexy lingerie, though, you might be able to loosen her up by convincing her to show it off for you."
            $ title = "Gift her the lingerie?"
            menu:
                "Yes, give her sexy lingerie":
                    give 1 lingerie from player to ivy notify
                    add tags 'gave_her_sexy_lingerie' to ivy
                    player.c "Why don't you at least try this on and show me how you look in it?"
                    wt_image intro_wife_visit_1_13
                    ivy.c "What's this?"
                    player.c "A gift.  For you."
                    ivy.c "You saw this and thought it would look good on me?"
                    player.c "Yes.  Go on.  Change into it and prove me right."
                    ivy.c "Well ... It's pretty revealing, but ...  Okay.  Since you paid for it, I guess I could let you see me wear it."
                    change ivy desire by 5
                    call ivy_model_sexy_lingerie from _call_ivy_model_sexy_lingerie
                "No, do something else":
                    pass
        elif ivy.has_tag('gave_her_sexy_lingerie') and not ivy.has_tag('modelled_sexy_lingerie'):
            player.c "Why don't you at least change into that lingerie I bought you and show me how you look in it?"
            wt_image intro_wife_visit_1_13
            ivy.c "Well ... It's pretty revealing, but ...  Okay.  Since you paid for it, I guess I could let you see me wear it."
            call ivy_model_sexy_lingerie from _call_ivy_model_sexy_lingerie_1
        else:
            "She's still too resistant to the idea to even really consider it.  Better do something else with her today."
    elif ivy.temporary_count > 0:
        wt_image intro_wife_visit_1_11
        ivy.c "I appreciate your confidence in me, but I'd be too embarrassed.  This suit is hiding a lot of flaws.  I don't have the body I used to, and I'm sure my husband would think I was being ridiculous if I started trying to dance sexy for him."
        player.c "Ivy, you're a beautiful and sexy woman and you could get any guy excited by showing off your body.  Try with me.  I'm not going to laugh or think you're ridiculous."
        wt_image intro_wife_visit_1_9
        ivy.c "Thanks for the vote of confidence.  I'll think about it."
        add tags 'considering_stripping' 'already_strip_trained_today' to ivy
        if not ivy.has_item(lingerie) and player.has_item(lingerie):
            "She's getting more comfortable with the idea of stripping.  If you gave her some sexy lingerie, you might be able to loosen her up some more by convincing her to show it off for you."
            $ title = "Gift her the lingerie?"
            menu:
                "Yes, give her sexy lingerie":
                    give 1 lingerie from player to ivy notify
                    add tags 'gave_her_sexy_lingerie' to ivy
                    player.c "Why don't you at least try this on and show me how you look in it?"
                    wt_image intro_wife_visit_1_13
                    ivy.c "What's this?"
                    player.c "A gift.  For you."
                    ivy.c "You saw this and thought it would look good on me?"
                    player.c "Yes.  Go on.  Change into it and prove me right."
                    ivy.c "Well ... It's pretty revealing, but ...  Okay.  Since you paid for it, I guess I could let you see me wear it."
                    change ivy desire by 5
                    call ivy_model_sexy_lingerie from _call_ivy_model_sexy_lingerie_2
                "No, do something else":
                    pass
        elif ivy.has_tag('gave_her_sexy_lingerie') and not ivy.has_tag('modelled_sexy_lingerie'):
            player.c "Why don't you at least change into that lingerie I bought you and show me how you look in it?"
            wt_image intro_wife_visit_1_13
            ivy.c "Well ... It's pretty revealing, but ...  Okay.  Since you paid for it, I guess I could let you see me wear it."
            call ivy_model_sexy_lingerie from _call_ivy_model_sexy_lingerie_3
    else:
        wt_image intro_wife_visit_1_9
        ivy.c "You know what?  You may be right.  Okay.  I'll try, but please don't laugh at me."
        call ivy_first_strip from _call_ivy_first_strip_1
    $ ivy.temporary_count = 0
    return

label ivy_model_sexy_lingerie:
    $ ivy.training_session()
    add tags 'modelled_sexy_lingerie' to ivy
    wt_image current_location.image
    "Ivy disappears into the bathroom to change.  She's gone a long time."
    wt_image intro_wife_lingerie_1_1
    "Eventually, she timidly steps back into the room."
    ivy.c "This is showing off more of my middle-age spread than I expected."
    player.c "Don't be silly.  You like great."
    wt_image intro_wife_lingerie_1_2
    ivy.c "I'm sucking in my belly so much I can barely breathe.  Are you sure I look okay?"
    player.c "You look fabulous.  Very sexy.  I'd like to see more.  Why don't you start taking some of the lingerie off for me?"
    wt_image intro_wife_lingerie_1_3
    ivy.c "I'm embarrassed to be showing off even this much of my body.  I'm not going to expose any more of my flaws."
    player.c "I don't see flaws.  I see a sexy woman.  At least turn around for me."
    wt_image intro_wife_lingerie_1_4
    ivy.c "I won't be able to suck in the saggy parts this exposes."
    wt_image intro_wife_lingerie_1_5
    player.c "You don't have to suck in anything.  Your butt is very cute, and very sexy."
    wt_image intro_wife_lingerie_1_6
    ivy.c "It used to be a lot sexier, and a lot tighter."
    player.c "It looks great to me.  All of you does.  Keep turning, give me a show."
    wt_image intro_wife_lingerie_1_7
    ivy.c "A show?  I couldn't.  I'd be too embarrassed."
    player.c "Sure you can.  At least strike a pose.  You've seen models do that."
    wt_image intro_wife_lingerie_1_1
    ivy.c "Yeah, but they look like models, and I look like me."
    player.c "From where I'm standing, you can model that lingerie as well as any professional could."
    wt_image intro_wife_lingerie_1_8
    ivy.c "Okay, that's just silly, but thank you for saying so, anyway.  What did you want me to do?  Something like this?"
    player.c "That's great, Ivy.  Keep going.  You're so sexy and look so good right now.  Feel it, and show me."
    wt_image intro_wife_lingerie_1_9
    "She continues to pose for you until it's time to go home.  She may not be ready to give a strip tease, yet, but she's getting closer.  And she's flattered both by the gift and the attention you paid to her in it."
    change ivy desire by 5
    change player energy by -energy_short
    notify
    end_day
    return

label ivy_first_strip:
    $ ivy.training_session()
    rem tags 'considering_stripping' from ivy
    wt_image intro_wife_visit_1_43
    ivy.c "Okay.  Here goes."
    wt_image intro_wife_visit_1_61
    "She gives you a seductive look ..."
    wt_image intro_wife_visit_1_62
    "... as she removes her suit coat ..."
    wt_image intro_wife_visit_1_16
    "... followed by her blouse ..."
    wt_image intro_wife_visit_1_63
    "... and skirt."
    wt_image intro_wife_visit_1_64
    "She does a little turn ..."
    wt_image intro_wife_visit_1_42
    "... and looks back over her shoulder at you as she removes her bra."
    wt_image intro_wife_visit_1_24
    "Just one article of clothing left.  Ivy's nerve falters ..."
    wt_image intro_wife_visit_1_27
    "... then she gathers her courage ..."
    wt_image intro_wife_visit_1_65
    "... and slides her panties down, too."
    wt_image intro_wife_visit_1_57
    ivy.c "Did I look ridiculous?"
    $ title = "What do you tell her?"
    menu:
        "You did look ridiculous":
            player.c "Yeah, you did a bit."
            wt_image intro_wife_visit_1_16
            ivy.c "Shit!  I knew it!!"
            wt_image intro_wife_visit_1_2
            ivy.c "I'm so embarrassed.  I don't why I thought a man would ever want to watch me take my clothes off.  I'm sorry I subjected you to that."
            add tags 'will_not_strip' to ivy
            change ivy submission by 5
            change ivy resistance by -5
            call character_location_return(ivy) from _call_character_location_return_650
            wt_image current_location.image
            "And with that she's gone.  A little humbled, and feeling no more trained than she was when she got here."
        "You looked sexy":
            player.c "No, you didn't look ridiculous.  You looked beautiful, and sexy."
            wt_image intro_wife_visit_1_66
            ivy.c "Did I really?  You're not just saying that to make me feel good are you?  Did you really enjoy that."
            player.c "I can show you how much I enjoyed it, if you'd like?"
            wt_image intro_wife_visit_1_67
            ivy.c "Oh, wow!  That's okay.  I can see from the bulge in your pants that you're telling the truth.  Well, that's flattering.  I'm so glad you convinced me to do this!!"
            change ivy sos by 10
            call character_location_return(ivy) from _call_character_location_return_651
            wt_image current_location.image
            "Ivy's so excited she rushes home to her husband, presumably to give him the same show she just gave you."
            add tags 'stripped_for_you' to ivy
    change player energy by -energy_short
    notify
    end_day
    return

label ivy_train_anal:
    # can't get here unless resistance < 65 and discussed
    # hypno, butt plug, and having sex with her all impact, plus resistance and submission
    player.c "I want to help you get over your fear of anal, Ivy.  You'll be much happier if you can please your husband in that way, and he'll be happier, too."
    wt_image intro_wife_visit_1_9
    ivy.c "How do you propose to do that?"
    player.c "By showing you that you can do anal sex, Ivy."
    $ ivy.temporary_count = 3
    if ivy.has_tag('anal_tongued_her'):
        $ ivy.temporary_count -= 1
    if ivy.has_tag('hypno_re_anal'):
        $ ivy.temporary_count -= 1
    if ivy.has_tag('used_butt_plug'):
        $ ivy.temporary_count -= 2
    if ivy.sex_count > 0:
        $ ivy.temporary_count -= 1
    if ivy.temporary_count > 0 and ivy.test('resistance', 50):
        $ ivy.temporary_count -= 2
    elif ivy.temporary_count > 0 and ivy.test('resistance', 55):
        $ ivy.temporary_count -= 1
    if ivy.temporary_count > 0 and ivy.test('submission', 20):
        $ ivy.temporary_count -= 2
    elif ivy.temporary_count > 0 and ivy.test('submission', 15):
        $ ivy.temporary_count -= 1
    if ivy.temporary_count > 0:
        wt_image intro_wife_visit_1_7
        ivy.c "I'm not letting you stick your dick up my butt!"
        if ivy.has_item(butt_plug):
            player.c "Have you been wearing your butt plug?"
            if ivy.has_tag('used_butt_plug'):
                ivy.c "Yes.  It feels weird, but I've been using it, to try and get used to the sensation back there.  But I'm not ready to replace it with a cock."
                "The butt plug by itself isn't enough.  Try lowering her Resistance or increasing her Submission or something else to make her more open to the idea."
            else:
                ivy.c "Not yet.  You just gave it to me.  But I will."
                "She needs to wear the butt plug a few times to get any benefit from it.  Try something else for today."
        elif player.has_item(butt_plug):
            "Gifting her the butt plug might help her get over her anxiety about anal."
            $ title = "Gift her the butt plug?"
            menu:
                "Yes":
                    player.c "How about something else, then, to help you get used to the sensation of having something back there."
                    wt_image intro_wife_visit_1_6
                    ivy.c "What are you talking about?"
                    player.c "This.  It's a butt plug.  It'll help you realize it's not that bad to take something in your rear.  It can even feel good.  Pull up your skirt and I'll show you how it goes in."
                    if ivy.test('submission', 20):
                        wt_image intro_wife_spank_1_7
                        ivy.c "I can't believe I'm letting you do this."
                        player.c "It's to help you and your marriage.  Pull your panties down, too."
                        wt_image intro_wife_butt_plug_1_1
                        ivy.c "Holy fuck!  Did you have to get such a large one?  That thing feels like it's trying to split me in two."
                        player.c "Don't be dramatic, Ivy.  It's a normal size plug for a normal sized hole, like yours."
                        wt_image intro_wife_visit_1_12
                        ivy.c "What happens now?  I go around with this thing up my ass?"
                    else:
                        wt_image intro_wife_visit_1_7
                        ivy.c "I'll put it in myself, thank you!  When I get home.  What happens then?  I go around with this thing up my ass?"
                    player.c "Not all the time, unless you find you like it and want to wear it all the time.  Just use it every couple of days, until it no longer feels strange."
                    wt_image intro_wife_visit_1_6
                    ivy.c "I can't believe it'll ever not feel strange to have something shoved up my butt, but okay, I'll try."
                    change ivy submission by 5
                    give 1 butt_plug from player to ivy notify
                "No":
                    pass
        else:
            "She's not ready to have anal with you, or anyone else.  She might never be ready, but buying a butt plug for her might help."
    else:
        $ ivy.training_session()
        wt_image intro_wife_visit_1_12
        ivy.c "Is this going to hurt?"
        if ivy.has_tag('used_butt_plug'):
            extend "  Your cock is going to go in a lot deeper than that butt plug did."
        player.c "I'll go slow, Ivy.  Your body will stretch to accommodate it."
        wt_image intro_wife_visit_1_16
        ivy.c "I'm going to panic.  I know I am."
        player.c "I'm not your husband, Ivy.  I'm not going to feel bad and call it off just because you're scared."
        wt_image intro_wife_visit_1_27
        ivy.c "So you're going to be a jerk and make me go through with this even though I'm frightened?"
        player.c "It seems that's what you need.  Come here and lie down on your back."
        wt_image intro_wife_anal_1_1
        ivy.c "You're putting it in me like this?  Isn't anal normally done doggy style?"
        player.c "Yes, but if you can't see what's going on, it's a lot easier to lose the connection with your partner and panic.  This position's more awkward, but I want to watch you and I want you to watch me as I'm entering you."
        wt_image intro_wife_anal_1_2
        player.c "No, no, no!  No squirming away."
        ivy.c "But it feels like you're splitting me in two!!"
        player.c "I'm not.  I used plenty of lube, you're not tearing.  That's your body slowly stretching to let my cock head inside you."
        wt_image intro_wife_seduce_1_40
        player.c "That's it, take deep breaths.  Get yourself under control.  You're doing great."
        ivy.c "I'm scared!"
        player.c "I know, but we're going to keep doing this.  I'm not going to let you be a failure.  You don't want to be a failure, do you?"
        ivy.c "No.  I want to be able to do this for my husband."
        player.c "Good.  So we're going to continue, okay?"
        ivy.c "Okay"
        wt_image intro_wife_anal_1_3
        ivy.c "HOLY FUCK!!"
        player.c "It's okay, Ivy.  That's my cock head passing through your sphincter ring.  That's as wide as your body needs to stretch.  Stay still and let your body get used to the feeling."
        wt_image intro_wife_anal_1_1
        ivy.c "Is that it?  Is it over?"
        player.c "No, I'm just pulling out so I can apply more lube and you can turn over.  You've taken my width, now I want you to take my length.  This part'll be easier for you if I'm entering you from behind."
        wt_image intro_wife_anal_1_4
        ivy.c "This part's really going to hurt, isn't it?"
        player.c "No, Ivy.  You've got plenty of room to take my full length.  Other than stretching to accommodate my width, the only discomfort is from the friction.  That's what the lube is for."
        wt_image intro_wife_anal_1_5
        player.c "There.  Feel how easily I'm moving in and out of you?  It feels good, doesn't it?"
        ivy.c "I don't know what it feels like.  My ass hurts."
        player.c "A little pain can be exciting.  Get up on your knees.  I want you to take control and fuck me with your ass."
        wt_image intro_wife_anal_1_6
        ivy.c "Oh, wow!  I'm doing it!!  I'm fucking you with my ass!"
        player.c "Doesn't that feel nice, feeling me back there, penetrating you?"
        ivy.c "It feels like I have a telephone pole shoved up my butt.  Can you please cum soon?  I think the lube has worn off because the friction's getting warmer."
        wt_image intro_wife_anal_1_5
        "The same friction that was making things warmer for her was also making things feel even better for you.  That plus the thrill of taking her anal virginity take you over the edge.  You shove yourself deep inside her, your body weight collapsing her down onto the ground as you cum."
        player.c "[player.orgasm_text]"
        wt_image intro_wife_visit_1_41
        ivy.c "This seems really weird to say, considering how raw and tender my ass is right now, and how icky your cum feels dripping out of it ... but thank you for that.  My husband's going to be thankful, too ... in a few days, after my ass recovers and I feel up to offering it to him."
        "Congratulations.  Ivy's feeling great about her training, and her husband's going to get one of his fantasies fulfilled.  That's some good work."
        change ivy sos by 20
        $ ivy.sex_training_count += 1
        $ ivy.anal_count += 1
        orgasm
        notify
        end_day
    return

label ivy_train_serve:
    if current_location != dungeon:
        sys "This type of action may work better in the dungeon, if you've added items to it.  Take her there?"
        $ title = "Take her to the dungeon?"
        menu:
            "Yes":
                call forced_movement(dungeon) from _call_forced_movement_949
            "No, stay here":
                pass
    if ivy.serve_count == 0:
        player.c "Men enjoy the company of subservient women, Ivy, who obey and serve them."
        wt_image intro_wife_visit_1_7
        ivy.c "Oh, I'm well aware that some men do.  I've run into plenty of jerks who think Asian women are all eager to wait on a man hand and foot."
        wt_image intro_wife_visit_1_6
        ivy.c "Fortunately for me, that's not what my husband wants.  Fortunate for him, too, as that's not who I am."
        player.c "I'm not suggesting you give up your job and become a full time housewife if that's not right for you and your husband, but whatever he may say, he'd enjoy seeing you act subservient to him from time to time. And you coming for training tells me you'd enjoy it, too."
        $ ivy.temporary_count = 3
        if ivy.crawl_count > 0:
            $ ivy.temporary_count -= 2
        if ivy.has_tag('dommed_you'):
            $ ivy.temporary_count =- 1
        if ivy.temporary_count > 0:
            if ivy.test('submission', 25):
                $ ivy.temporary_count -= 3
            elif ivy.test('submission', 20):
                $ ivy.temporary_count -= 2
            elif ivy.test('submission', 15):
                $ ivy.temporary_count -= 1
        if ivy.temporary_count > 0:
            if ivy.test('resistance', 60):
                $ ivy.temporary_count -= 2
            elif ivy.test('resistance', 65):
                $ ivy.temporary_count -= 1
        if ivy.temporary_count > 2:
            wt_image intro_wife_visit_1_9
            ivy.c "I'm just not the subservient type."
            sys "Her submission is too low and resistance too high to allow you to train her like this today.  Choose something else to do with her."
        elif ivy.temporary_count > 0:
            wt_image intro_wife_visit_1_9
            ivy.c "I'm just not the subservient type."
            if ivy.has_tag('gave_her_fishnet_lingerie'):
                player.c "At least change into the lingerie I bought you and show yourself off to your husband in it."
                wt_image intro_wife_visit_1_10
                ivy.c "I'll look like a slut wearing that."
                player.c "You'll look like eye candy.  Surely you don't mind the idea of your husband looking at you?"
                ivy.c "I guess not, but ..."
                player.c "I'm sure dressing trashy is the least you can do for him, even if you're not otherwise willing to be subservient.  Go change and practice with me, so you'll be more comfortable wearing it for your husband."
                call ivy_model_fishnet_lingerie from _call_ivy_model_fishnet_lingerie
            elif player.has_item(lingerie) and not ivy.has_item(lingerie):
                $ title = "Try to change her mind?"
                menu:
                    "Yes, give her some slutty lingerie to wear (gifts Lingerie to her)":
                        player.c "At least change into this lingerie I bought you and show yourself off to your husband in it."
                        wt_image intro_wife_visit_1_10
                        ivy.c "I'll look like a slut wearing that."
                        player.c "You'll look like eye candy.  Surely you don't mind the idea of your husband looking at you?"
                        ivy.c "I guess not, but ..."
                        player.c "I'm sure dressing trashy is the least you can do for him, even if you're not otherwise willing to be subservient.  Go change and practice with me, so you'll be more comfortable wearing it for your husband."
                        give 1 lingerie from player to ivy
                        add tags 'gave_her_fishnet_lingerie' to ivy
                        call ivy_model_fishnet_lingerie from _call_ivy_model_fishnet_lingerie_1
                    "No":
                        sys "Her submission is still too low to allow you to train her like this today.  Getting her the right lingerie might also help.  For today, choose something else to do with her."
            else:
                sys "Her submission is still too low to allow you to train her like this today.  Getting her the right lingerie might also help.  For today, choose something else to do with her."
        else:
            wt_image intro_wife_visit_1_10
            ivy.c "I'm really not the subservient type."
            if ivy.has_tag('gave_her_fishnet_lingerie'):
                player.c "I know, but I can train you to get over that.  Go change into the lingerie I bought you and practice how you'll show yourself off to your husband in it."
                ivy.c "I'll look like a slut wearing that."
                player.c "You'll look like eye candy.  Surely you don't mind the idea of your husband looking at you?"
                ivy.c "I guess not, but ..."
                player.c "I'm sure dressing trashy is the least you can do for him, even if you're not otherwise willing to be subservient.  Go change and practice with me, so you'll be more comfortable wearing it for your husband."
                call ivy_model_fishnet_lingerie from _call_ivy_model_fishnet_lingerie_2
            else:
                $ ivy.training_session()
                player.c "I know, but I can train you to get over that.  Take off your clothes."
                wt_image intro_wife_visit_1_12
                ivy.c "Just like that?"
                wt_image intro_wife_visit_1_15
                player.c "Just like that.  You're going to practice offering yourself to your husband."
                wt_image intro_wife_visit_1_16
                ivy.c "I don't need to be naked to do that."
                wt_image intro_wife_visit_1_17
                player.c "You shouldn't be clothed, either.  Not if you're offering to serve in a suitably subservient manner.  Unless you have an outfit that says 'I belong to you', going naked is your best option."
                wt_image intro_wife_visit_1_23
                ivy.c "So you think I should get naked first, and then seduce him?"
                wt_image intro_wife_visit_1_24
                player.c "Not quite.  You're offering yourself to him, not seducing him.  Seducing him puts pressure on him to respond the same.  You're simply making it clear that you're available to him if he wants you.  He may not be in the mood, and that'll be his choice."
                wt_image intro_wife_visit_1_25
                ivy.c "That's okay.  He has a stressful and tiring job.  So do I.  We both understand that sometimes we're just not in the mood.  I'd just get dressed, I wouldn't be offended."
                player.c "No, you shouldn't dress.  Even if he's tired, he'd could still enjoy looking at you."
                wt_image intro_wife_visit_1_66
                ivy.c "But I couldn't just go around the house naked."
                player.c "While you're serving your husband you can.  Making yourself available means accepting whatever he wants to do with you.  If he's tired, maybe he just wants you to hang out like that while he eats his supper."
                wt_image intro_wife_visit_1_25
                ivy.c "You want me to stay naked while he ignores me?"
                player.c "I doubt he'll completely ignore you, but yes, that's the idea behind being available.  It includes being eye candy and waiting in case he changes his mind.  Let's practice.  Sit down and lift your leg in the air and be eye candy."
                wt_image intro_wife_visit_1_69
                ivy.c "I look ridiculous."
                player.c "You look like eye candy, which is an excellent way for you to serve your husband until he's ready to make use of you in other ways.  Stay there and practice."
                wt_image intro_wife_visit_1_70
                ivy.c "Does it actually require practice to be eye candy?"
                player.c "Emotionally, yes.  You're used to being his equal partner.  Learning to subordinate yourself takes a different head space."
                wt_image intro_wife_visit_1_69
                ivy.c "This is humiliating, holding this position while you just stare at me."
                player.c "This is you doing something special for your husband, Ivy.  Giving yourself to him.  Truly giving yourself.  Think of your body as an ornament for your husband's enjoyment.  Right now you exist to make your house a more beautiful and comfortable place for your husband."
                wt_image intro_wife_visit_1_70
                ivy.c "I don't want him to think of me as just an ornament."
                player.c "He won't.  He'll still think of you just as he does now, but with the added joy of knowing that you can be everything for him you already are, plus serve him like this from time to time."
                wt_image intro_wife_visit_1_69
                ivy.c "So do I just stay like this until he tells me what he wants me to do?"
                player.c "Yes"
                wt_image intro_wife_visit_1_70
                ivy.c "My leg's getting tired."
                wt_image intro_wife_visit_1_71
                player.c "You can support it with your hand, as long as you keep yourself open for your husband's viewing pleasure."
                wt_image intro_wife_visit_1_26
                "You leave her like that for as long as you think she can hold the position, by which time she should have internalized the experience as much as she's going to."
                wt_image intro_wife_visit_1_71
                player.c "You can put your leg down.  Stand up and step closer to me, Ivy."
                wt_image intro_wife_visit_1_66
                "It takes a moment for her to be get her legs ready to move again, then she approaches."
                wt_image intro_wife_visit_1_49
                player.c "Your nipples are hard."
                wt_image intro_wife_visit_1_57
                ivy.c "It's cold in here when you're not wearing any clothes."
                "It might be, but Ivy's body is also more comfortable with serving than her mind is, although her mind is starting to get there.  She's not trained yet, but she's getting close."
                $ ivy.serve_count = 1
                change ivy submission by 10
                change player energy by -energy_short
                notify
                end_day
    else:
        $ ivy.training_session()
        if ivy.serve_count == 1:
            player.c "Now that you've practiced waiting to serve your husband, show me you can play the full, subservient wife role."
            wt_image intro_wife_visit_1_11
            ivy.c "Okay, but as an act only.  This is just role-playing."
            player.c "That's between you and your husband.  I expect you to convince me that you really are subservient to me and here to serve me, not just acting."
            if ivy.has_tag('modelled_fishnet_lingerie'):
                wt_image intro_wife_visit_1_12
                ivy.c "Should I change into the lingerie again?"
                player.c "You can save that for special occasions.  Getting naked for him also sets the right tone."
                wt_image intro_wife_visit_1_16
                ivy.c "Okay"
            else:
                wt_image intro_wife_visit_1_16
                ivy.c "Okay.  I'll try."
            wt_image intro_wife_visit_1_23
            ivy.c "Hello, dear.  I want you to know that I'm available for you."
            wt_image intro_wife_visit_1_24
            player.c "Not like that.  Get completely naked, first."
            wt_image intro_wife_visit_1_66
            ivy.c "Hello, dear.  I want you to know that I'm available for you."
            player.c "Better.  But 'dear' isn't a subservient way to address your husband, is it?"
            wt_image intro_wife_visit_1_52
            ivy.c "I guess not.  Should I call him 'sir'?"
            player.c "Try it and see how it sounds."
            wt_image intro_wife_visit_1_25
            ivy.c "Hello, Sir. I want you to know that I'm available for you."
            player.c "Good.  That sounds much more obedient.  Go to the kitchen and bring me something to drink."
            wt_image intro_wife_visit_1_52
            ivy.c "For real?"
            player.c "Yes.  If you're going to serve your husband, serve him.  Bringing him a drink when he tells you to is the least you can do.  I'll just have a water for now."
            wt_image intro_wife_visit_1_72
            player.c "Put a slice of lemon in it, for me.  You'll find them in a bowl on the counter.  Glasses are in the left most cupboard when you're facing the sink."
            wt_image intro_wife_visit_1_66
            "She returns a few minutes later, and hands you your water with lemon."
            ivy.c "Here you go."
            player.c "No, that's not nearly subservient enough.  Address me properly when you pass the glass to me."
            wt_image intro_wife_visit_1_25
            ivy.c "Here's your drink, Sir."
            player.c "Much better.  Come over here and get down on the floor in front of me while I drink it."
            wt_image intro_wife_visit_1_57
            ivy.c "Get on the floor?"
            player.c "Yes, Ivy.  That's a suitable place for a wife who's waiting to find out how her husband wants her to serve him."
            wt_image intro_wife_visit_1_50
            ivy.c "My husband likes that I'm a strong, confident woman.  If I humiliate myself too much ..."
            player.c "Your husband will love that his strong, confident wife is turned on by humbling herself for him.  It's okay that you find this equal parts scary and sexy.  Once you're on the ground staring up at him, the scary part drops away and it's only sexy."
            wt_image intro_wife_visit_1_59
            "She stares at you for over a minute ..."
            wt_image intro_wife_serve_1_1
            "... then walks over ..."
            wt_image intro_wife_serve_1_2
            "... lowers herself, figuratively and literally, before you."
            player.c "That's nice, but this drink would be more enjoyable with a view of your ass."
            wt_image intro_wife_serve_1_3
            "She stares at you again ..."
            wt_image intro_wife_serve_1_4
            "... then turns around."
            wt_image intro_wife_serve_1_5
            player.c "You know what?  This is too impersonal.  Turn around and face me again ..."
            wt_image intro_wife_serve_1_3
            player.c "... but keep your legs spread."
            wt_image intro_wife_serve_1_7
            player.c "Wider"
            wt_image intro_wife_serve_1_8
            ivy.c "This is ..."
            player.c "Shush.  I'm enjoying my drink.  Don't interrupt.  You could open your pussy lips, though."
            wt_image intro_wife_serve_1_9
            "You take your time finishing your drink as Ivy waits quietly and tries not to let on that she's actually enjoying this."
            $ title = "What now?"
            menu:
                "Let her go home":
                    player.c "Ready to go home and serve your husband?"
                    wt_image intro_wife_serve_1_10
                    ivy.c "Yes.  He's going to be surprised."
                    player.c "Have I lost my term of respect already?"
                    wt_image intro_wife_serve_1_11
                    ivy.c "No, Sir.  Thank you for teaching me that I can enjoy subordinating myself to a man, Sir.  I hope my husband appreciates my training, Sir."
                    "You're sure he will, and Ivy does, too."
                "Tell her to blow you":
                    player.c "Ready to go home and serve your husband?"
                    wt_image intro_wife_serve_1_10
                    ivy.c "Yes.  He's going to be surprised."
                    player.c "Have I lost my term of respect already?"
                    wt_image intro_wife_serve_1_11
                    ivy.c "No, Sir.  Thank you for teaching me that I can enjoy subordinating myself to a man, Sir.  I hope my husband appreciates my training, Sir."
                    player.c "You're welcome.  Before you go, you can complete your service to me by blowing me."
                    if ivy.sex_training_count > 0 or ivy.sex_count > 0 or ivy.blowjob_count > 0:
                        wt_image intro_wife_serve_1_10
                        ivy.c "Yes, Sir."
                        call ivy_serve_blowjob from _call_ivy_serve_blowjob
                    elif ivy.test('desire', 10) or ivy.test('submission', 40):
                        wt_image intro_wife_serve_1_7
                        ivy.c "But you're not my husband.  We were just practicing."
                        player.c "I want your mouth around my cock anyway."
                        wt_image intro_wife_serve_1_6
                        ivy.c "Yes, Sir."
                        call ivy_serve_blowjob from _call_ivy_serve_blowjob_1
                    else:
                        wt_image intro_wife_serve_1_6
                        ivy.c "I'll gladly do that for my husband, Sir, when I subordinate myself to him.  Thank you again for the training."
                        "Seems neither her Desire for you nor her Submission to you were high enough to convince her to finish the session with a blowjob, but she still appreciated her training.  Her husband will, too."
            change player energy by -energy_long
            change ivy sos by 10
            change ivy desire by 5
            change ivy submission by 5
            $ ivy.serve_count = 2
        else:
            player.c "Show me you remember how to serve a man, Ivy."
            wt_image intro_wife_visit_1_16
            ivy.c "Yes, Sir."
            wt_image intro_wife_visit_1_66
            ivy.c "I'm available to serve you, Sir.  Is there anything I could do for you?  Get you a drink, perhaps?"
            player.c "Yes, a glass of water would be nice."
            wt_image intro_wife_visit_1_72
            player.c "Don't forget a slice of lemon."
            ivy.c "I won't, Sir."
            wt_image intro_wife_visit_1_52
            ivy.c "Here's your drink, Sir.  I hope you enjoy it.  Would you like ..."
            player.c "Would I like what?"
            wt_image intro_wife_visit_1_58
            ivy.c "Would you like me to be somewhere in particular for you?"
            player.c "You don't have to be shy about it.  Spit it out."
            wt_image intro_wife_visit_1_50
            ivy.c "Would you like me on the ground at your feet while you enjoy your drink, Sir?"
            wt_image intro_wife_serve_1_1
            player.c "Yes, I do.  Come closer and kneel down here."
            wt_image intro_wife_serve_1_2
            ivy.c "How would you like me to face, Sir?"
            wt_image intro_wife_serve_1_4
            player.c "Turn around."
            wt_image intro_wife_serve_1_5
            ivy.c "Is this good, Sir?"
            wt_image intro_wife_serve_1_7
            player.c "It is, but turn around so I can look at your pussy and compare."
            wt_image intro_wife_serve_1_8
            ivy.c "How's this, Sir?"
            player.c "Better, but open your pussy lips, too."
            wt_image intro_wife_serve_1_9
            player.c "Yes, I like that.  How about you, Ivy?  How's your inner feminist handling this position?"
            ivy.c "I'm surprisingly aroused at doing this for you, Sir."
            $ title = "What now?"
            menu:
                "Let her go home":
                    player.c "Good. You should be all set to serve your husband, then, when you get home."
                    wt_image intro_wife_serve_1_11
                    ivy.c "Yes, Sir.  Thank you.  And thank you on behalf of my husband, too."
                "Tell her to blow you":
                    player.c "So am I.  Since you're the subservient one, I'm sending you home horny, but I want you to look after my erection before you go."
                    if ivy.sex_training_count > 0 or ivy.sex_count > 0 or ivy.blowjob_count > 0:
                        wt_image intro_wife_serve_1_10
                        ivy.c "Yes, Sir."
                        call ivy_serve_blowjob from _call_ivy_serve_blowjob_2
                    else:
                        wt_image intro_wife_serve_1_7
                        ivy.c "But you're not my husband.  We were just practicing."
                        player.c "I want your mouth around my cock anyway."
                        wt_image intro_wife_serve_1_6
                        ivy.c "Yes, Sir."
                        call ivy_serve_blowjob from _call_ivy_serve_blowjob_3
            change ivy desire by 10
            change player energy by -energy_short
        notify
        end_day
    return

label ivy_model_fishnet_lingerie:
    $ ivy.training_session()
    if ivy.has_tag('modelled_fishnet_lingerie'):
        wt_image current_location.image
        "Ivy ducks into the bathroom to change ..."
        wt_image intro_wife_lingerie_2_1
        "... reappearing few minutes later, wearing her fishnets again."
    else:
        add tags 'modelled_fishnet_lingerie' to ivy
        wt_image current_location.image
        "Ivy disappears into the bathroom to change.  She's gone a long time."
        wt_image intro_wife_lingerie_2_1
        "Eventually, she timidly steps back into the room."
        ivy.c "This makes me look like even more of a slut than I expected."
    player.c "Don't be shy.  Come closer."
    wt_image intro_wife_lingerie_2_2
    player.c "Not like that."
    ivy.c "Pardon?"
    player.c "When you're dressed like that, do you feel like your normal self?"
    ivy.c "No.  Not at all."
    player.c "Then don't walk like you normally walk.  If you were your husband, how would you want to be approached by a woman dressed like you are?"
    wt_image intro_wife_lingerie_2_3
    "Ivy thinks for a moment, then adopts a catwalk gait as she approaches."
    wt_image intro_wife_lingerie_2_4
    ivy.c "I'm dressed as if I'm available, so I guess I may as well act the same way."
    player.c "That's right, and it's the first lesson in serving.  Make yourself available to him in a way that let's him choose whether and how to make use of you.  Can you do that?"
    ivy.c "Sure.  It's just another way of seducing him, right?"
    player.c "Not quite the same.  What if he's not in the mood to make love to you?"
    ivy.c "That's okay.  He has a stressful and tiring job.  So do I.  We both understand that sometimes we're just not in the mood.  I'd just go change, I wouldn't be offended."
    player.c "No, you shouldn't go change.  Even if he's tired, he'd could still enjoy looking at you."
    wt_image intro_wife_lingerie_2_5
    ivy.c "But I couldn't just wear this around the house."
    player.c "While you're serving your husband you can.  Making yourself available means accepting whatever he wants to do with you.  If he's tired, maybe he just wants you to hang out like that while he eats his supper."
    ivy.c "You want me to stay dressed like this while he ignores me?"
    player.c "I doubt he'll completely ignore you, but yes, that's the idea behind being available.  It includes being eye candy and waiting in case he changes his mind.  Let's practice.  Go be eye candy up against that wall."
    wt_image intro_wife_lingerie_2_6
    ivy.c "Does it actually require practice to be eye candy?"
    player.c "Emotionally, yes.  You're used to being his equal partner.  Learning to subordinate yourself takes a different head space.  It'll be easier if you turn and face the wall."
    wt_image intro_wife_lingerie_2_7
    "Even from a distance, you can hear the pace of her breathing quicken as she turns."
    wt_image intro_wife_lingerie_2_8
    ivy.c "This is humiliating."
    player.c "This is you doing something special for your husband, Ivy.  Giving yourself to him.  Truly giving yourself."
    wt_image intro_wife_lingerie_2_9
    player.c "Face the wall and think of your body as a gift-wrapped present you've provided to your husband.  Like that vase on the table beside you, right now you exist to make your house a more beautiful and comfortable place for your husband."
    ivy.c "I don't want him to think of me as just a vase."
    player.c "He won't.  He'll still think of you just as he does now, but with the added joy of knowing that you can be everything for him you already are, plus serve him like this from time to time."
    wt_image intro_wife_lingerie_2_10
    ivy.c "So do I just stay like this until he tells me what he wants me to do?"
    player.c "Yes"
    wt_image intro_wife_lingerie_2_8
    ivy.c "Seriously???"
    player.c "Seriously.  Eyes towards the wall."
    wt_image intro_wife_lingerie_2_10
    "You leave her like that for half an hour, by which time she should have internalized the experience as much as she's going to."
    player.c "Come closer to me now, Ivy."
    wt_image intro_wife_lingerie_2_11
    "It takes a moment for her to be get her legs ready to move again, then she approaches you with downcast eyes."
    wt_image intro_wife_lingerie_2_12
    player.c "Your nipples are hard."
    wt_image intro_wife_lingerie_2_13
    ivy.c "It's cold in this outfit."
    "It might be, but Ivy's body is also more comfortable with serving than her mind is, although her mind is starting to get there.  She's not trained yet, but she's getting close."
    $ ivy.serve_count = 1
    change ivy submission by 10
    change player energy by -energy_short
    notify
    end_day
    return

label ivy_serve_blowjob:
    if ivy.has_tag('bj_training'):
        wt_image intro_wife_bj_1_9
        "She remembers her training, and starts with your balls."
        wt_image intro_wife_bj_1_8
        ivy.c "Would you like me to move to your cock now, Sir?"
        player.c "A little longer on my balls."
        wt_image intro_wife_bj_1_9
        ivy.c "Yes, Sir."
        wt_image intro_wife_bj_1_8
        player.c "Okay, you can pleasure my shaft now."
        wt_image intro_wife_bj_1_10
        ivy.c "Yes, Sir."
        wt_image intro_wife_bj_1_11
        "She licks you up and down, paying extra attention to the underside of your cockhead."
        wt_image intro_wife_bj_1_12
        ivy.c "May I please you by sucking you now, Sir?"
        wt_image intro_wife_bj_1_13
        player.c "Yes, but take your time.  I'm worked up from looking at your body, and don't want to cum too quickly in that talented cocksucking mouth of yours."
        wt_image intro_wife_bj_1_12
        ivy.c "This feminist is surprisingly aroused by your compliments, Sir."
        wt_image intro_wife_bj_1_14
        player.c "You enjoy being a cocksucker serving on your knees, don't you, Ivy?"
        wt_image intro_wife_bj_1_15
        "She nods without stopping the blowjob or breaking eye contact.  Her submissive behavior overwhelms your remaining resolve."
        player.c "Finish me off like the submissive cocksucker you are, Ivy."
        wt_image intro_wife_bj_1_6
        ivy.c "Yes, Sir."
        wt_image intro_wife_bj_1_17
        player.c "[player.orgasm_text]"
        wt_image intro_wife_bj_1_18
        if ivy.status == 'on_training':
            ivy.c "Thank you again, Sir, for training me to serve my husband."
            "She seems to genuinely mean it.  Her husband will appreciate it, too."
            change ivy submission by 5
        $ ivy.facial_count += 1
    else:
        wt_image intro_wife_bj_1_1
        "Ivy wraps her lips around your cock head ..."
        wt_image intro_wife_bj_1_2
        "... and begins to blow you."
        wt_image intro_wife_bj_1_3
        "There's a bit of eye contact and a lot of sucking and stroking with her hand ..."
        wt_image intro_wife_bj_1_4
        "... with the occasional attention to the underside of your cock head thrown in."
        wt_image intro_wife_bj_1_1
        "As turned on as you are from watching her supplicate herself in front of you, it's more than sufficient to quickly bring you over the edge ..."
        wt_image intro_wife_bj_1_5
        "... as she suctions your load out of your balls and into her waiting mouth."
        player.c "[player.orgasm_text]"
        wt_image intro_wife_bj_1_6
        if ivy.status == 'on_training':
            ivy.c "I swallowed for you, Sir.  Thank you again for training me to serve my husband."
            "She seems to genuinely mean it.  Her husband will appreciate it, too."
        $ ivy.swallow_count += 1
    orgasm
    $ ivy.blowjob_count += 1
    return

label ivy_train_take_charge:
    # Domme comfort sources: initial talk, hypno, pussy licking, fuck through seduce action, sex show
    if not ivy.has_tag('dommed_you'):
        $ ivy.temporary_count = 3
        call ivy_sex_proceed_test from _call_ivy_sex_proceed_test_3
    if ivy.has_tag('dommed_you') or ivy.temporary_count < 1:
        if ivy.domme_comfort == 0:
            player.c "Ivy, I think you'd be really great at taking charge.  I know you're uncomfortable ordering your husband around, but with a bit of practice, I think you could learn to enjoy it, and he would, too."
            wt_image intro_wife_visit_1_9
            ivy.c "I'm not sure that's the sort of relationship I want to have with my husband.  Bossing him around just sounds like me being a bad wife."
            sys "You need to find an activity or two that will get her comfortable with the idea of taking charge.  Until then, try something else."
        elif ivy.domme_comfort < 2:
            player.c "Ivy, I think you'd be really great at taking charge.  I know you're uncomfortable ordering your husband around, but with a bit of practice, I think you could learn to enjoy it, and he would, too."
            wt_image intro_wife_visit_1_10
            ivy.c "I don't know how he'd feel if I started bossing him around.  Even to bring it up would put pressure on him to try something he may be uncomfortable with.  I don't want to make him feel bad, or to make him think badly of me."
            if ivy.serve_count > 0 or ivy.crawl_count > 0:
                if ivy.serve_count > 0:
                    player.c "You remember how it felt when I trained you to serve.  You remember the thrill it gave you, taking a subservient role and focusing on pleasing another.  I'm sure your husband will enjoy serving you every bit as much."
                else:
                    player.c "You remember how it felt when I trained you to break through your inhibitions and crawl.  You remember the thrill it gave you, being humiliated in order to give pleasure to someone else.  I'm sure your husband will enjoy serving you every bit as much."
                ivy.c "My husband's not me."
                player.c "No, but you know that he enjoys pleasing you, don't you?"
                wt_image intro_wife_visit_1_9
                "She nods, thoughtfully for a moment before responding."
                ivy.c "You're going to do what I tell you?"
                player.c "Yes, Ma'am."
                wt_image intro_wife_visit_1_61
                ivy.c "Follow me."
                $ ivy.domme_comfort = 3
                call ivy_take_charge_proceed from _call_ivy_take_charge_proceed
            else:
                $ title = "Do you want to spend time working on this topic with her?"
                menu:
                    "Yes":
                        $ ivy.training_session()
                        if ivy.test('resistance',60):
                            wt_image intro_wife_visit_1_11
                            "You spend the evening talking to her, and convince her to become more comfortable with the idea of taking charge in the bedroom.  It may or may not be enough, but it's progress."
                            $ ivy.domme_comfort += 1
                        else:
                            wt_image intro_wife_visit_1_9
                            "You spend the evening talking to her, and she comes to trust you more in general, but you don't make much headway on this particular topic.  You'll need to keep lowering her Resistance or find another activity to help her become comfortable taking charge."
                            change ivy resistance by -5
                        change player energy by -energy_long
                        notify
                        end_day
                    "No, do something else today":
                        pass
        elif ivy.has_tag('dommed_you'):
            player.c "Ivy, I'd like you keep practicing, so you get even more comfortable taking charge."
            if not ivy.has_tag('second_domme_scene'):
                wt_image intro_wife_visit_1_11
                ivy.c "I was hoping you'd say that.  Take off your clothes and wait here.  I'll be right back."
                call ivy_take_charge_proceed from _call_ivy_take_charge_proceed_1
            else:
                wt_image intro_wife_visit_1_9
                ivy.c "I need you to understand something, first.  If you want me to do this again, I'm going to put your leash back on."
                ivy.c "The last time I did that, I was so turned on by leaving you with a throbbing erection, I went home and had amazing sex with my husband, cumming three times."
                ivy.c "So maybe this time I'll feel more like watching you cum afterwards, but there's a very high chance that I'll feel more like leaving you hanging, while I go home and have sex with my husband, again."
                ivy.c "Are you sure you want to go through that again?"
                $ title = "What do you tell her?"
                menu:
                    "Yes, Mistress":
                        player.c "Yes, Mistress.  I want to please you in whatever way you choose."
                        wt_image intro_wife_visit_1_13
                        ivy.c "Okay, boy.  Remove your clothes and wait for me while I go get your leash."
                        call ivy_take_charge_proceed from _call_ivy_take_charge_proceed_2
                    "Maybe we should do something else":
                        wt_image intro_wife_visit_1_6
                        player.c "Thanks for the open communication, Ivy.  I'm not really in the mood to be blue balled again."
        else:
            player.c "Ivy, I think you'd be really great at taking charge.  I know you're uncomfortable ordering your husband around, but with a bit of practice, I think you could learn to enjoy it, and he would, too."
            wt_image intro_wife_visit_1_10
            ivy.c "Do you really think I can do this and not sound ridiculous or bossy?"
            player.c "I'm sure you'll be great at it, and not ridiculous at all.  As for bossy, I'd like you to sound bossy.  You're in charge, embrace it."
            wt_image intro_wife_visit_1_9
            "She looks thoughtfully at you for a moment before responding."
            ivy.c "You're going to do what I tell you?"
            player.c "Yes, Ma'am."
            wt_image intro_wife_visit_1_61
            ivy.c "Follow me."
            call ivy_take_charge_proceed from _call_ivy_take_charge_proceed_3
    else:
        player.c "Ivy, I think you'd be really great at taking charge.  I know you're uncomfortable ordering your husband around, but with a bit of practice, I think you could learn to enjoy it, and he would, too."
        wt_image intro_wife_visit_1_4
        ivy.c "Practice?  You mean with you?"
        player.c "Yes, to get you comfortable telling a man how you want him to serve you, sexually."
        wt_image intro_wife_visit_1_7
        ivy.c "That's a lame way to try and get me to sleep with you."
        call ivy_sex_failed_proceed from _call_ivy_sex_failed_proceed_3
    return

label ivy_take_charge_proceed:
    $ ivy.training_session()
    # first session
    if not ivy.has_tag('dommed_you'):
        add tags 'dommed_you' to ivy
        wt_image intro_wife_spank_1_3
        ivy.c "Take your clothes off."
        wt_image intro_wife_spank_1_11
        ivy.c "Mmmm.  That's a nice big hard cock you have.  Are you excited by me telling you what to do?"
        player.c "Yes, Ma'am."
        wt_image intro_wife_spank_1_12
        ivy.c "Turn around.  I'll let you know when you can look at me again."
        wt_image current_location.image
        "You can hear her undressing, even though you're not allowed to look at her while she does so."
        ivy.c "Okay.  You can turn around to face me."
        wt_image intro_wife_spank_1_13
        if ivy.has_tag('instructed_you_on_pussy_licking'):
            ivy.c "You did an okay job of licking my pussy before, once I showed you how, but I think you can learn to do it even better.  Get your mouth between my legs."
        elif ivy.pleasure_her_count > 0:
            ivy.c "You did an okay job of licking my pussy before, but now I'm going to show you how to do a much better job.  Get your mouth between my legs."
        else:
            ivy.c "Men are crap at eating pussy, but lucky for you I'm going to teach you how to do it well.  Get your mouth between my legs."
        wt_image intro_wife_spank_1_14
        "You do your best to follow her instructions as she tells you exactly where and how to use your lips and tongue on her."
        wt_image intro_wife_spank_1_15
        "You must do a good job, as her instructions slow and her moans increase."
        wt_image intro_wife_spank_1_16
        ivy.c "Stop!!  Remove your mouth!"
        wt_image intro_wife_spank_1_17
        ivy.c "I want to feel your big, hard cock inside me."
        wt_image intro_wife_spank_1_18
        ivy.c "OH!!  That's it!  Fill me up!"
        wt_image intro_wife_spank_1_19
        ivy.c "Mmmm ... that big, hard cock of yours feels great.  Stay still, I just want to feel you filling me up."
        wt_image intro_wife_spank_1_20
        ivy.c "Fuck me now, and fuck me hard, but don't you dare cum or you'll never be allowed inside my pussy again."
        wt_image intro_wife_spank_1_21
        player.c "Yes, Ma'am."
        wt_image intro_wife_spank_1_22
        "It takes a lot of will-power to ignore her moaning and how good her cunt feels and concentrate on being her personal fuck machine."
        wt_image intro_wife_spank_1_23
        "Fortunately, she's enjoying the boning you give her enough that you shouldn't have to hold out much longer."
        wt_image intro_wife_spank_1_24
        ivy.c "Harder!  Faster!!  Come on, give it to me!!"
        wt_image intro_wife_spank_1_25
        ivy.c "OH ... I'M CUMMINNGGG!!!"
        wt_image intro_wife_spank_1_26
        ivy.c "Stop!  Stop moving.  Pull out."
        wt_image intro_wife_spank_1_27
        ivy.c "Let me turn around, then I want you to show me how excited you got, fucking me."
        wt_image intro_wife_spank_1_28
        player.c "[player.orgasm_text]"
        ivy.c "OH WOW!!  You really did enjoy yourself!"
        wt_image intro_wife_spank_1_29
        ivy.c "Lie down and cuddle me, and don't call me 'Ma'am', just tell me how you're feeling?"
        player.c "I'm feeling great, Ivy, and I'm very proud of you.  You're really good at taking charge."
        ivy.c "You're so sweaty, I made you work really hard to please me.  You're sure you didn't mind?"
        player.c "You're worth it.  I'm sure your husband feels the same way."
        ivy.c "You don't think he'll mind?   He won't think I'm a bitch if I start bossing him around, will he?"
        player.c "Don't worry about that.  Just focus on making him your bitch."
        ivy.c "Oh wow!  The thought of that turns me on so much."
        sys "Congratulations!  Ivy's feeling well trained.  You suspect her husband's going to feel well trained soon, too."
        change ivy sos by 15
        change ivy desire by 10
        $ ivy.orgasm_count += 1
        $ ivy.sex_count += 1
        orgasm
    elif not ivy.has_tag('second_domme_scene'):
        call ivy_domme_session_two from _call_ivy_domme_session_two
        "Ivy's feeling even better about taking control, sexually.  You should feel good about that, even if you have a case of blue balls for your effort."
        change ivy sos by 10
        change ivy desire by 10
        change player energy by -energy_short
    else:
        call ivy_domme_session_three from _call_ivy_domme_session_three
        "Congratulations!  You've thoroughly stimulated Ivy's dominant side, and her trust in you continues to grow."
        change ivy resistance by -5
        change player energy by -energy_short
    notify
    end_day
    return

label ivy_domme_session_two:
    add tags 'second_domme_scene' to ivy
    wt_image current_location.image
    "Ivy disappears into the bathroom while you strip.  You wait for her, naked, for a few minutes ..."
    wt_image intro_wife_domme_1_1
    "... until she reappears wearing a latex dress."
    ivy.c "I dropped into a BDSM store downtown, the Steel Trap, and was chatting with the clerk there.  She suggested this outfit to me.  What do you think?"
    player.c "I think you look amazing, Ma'am."
    wt_image intro_wife_domme_1_2
    ivy.c "We also talked about titles and terms of respect.  I think I prefer 'Mistress' to 'Ma'am'.  What do you think about that?"
    player.c "I'll call you whatever you tell me to, Mistress."
    ivy.c "Good.  And I'm going to call you 'boy'."
    player.c "Yes, Mistress."
    wt_image intro_wife_domme_1_3
    ivy.c "Do you like the view of Mistress' ass when I turn around, boy?"
    player.c "Yes, Mistress.  Very much."
    wt_image intro_wife_domme_1_4
    ivy.c "Good. Keep staring at it, boy, and get your cock nice and hard while I go get the other thing the nice lady at the Steel Trap suggested to me."
    wt_image intro_wife_domme_1_5
    ivy.c "How does that feel around your cock, boy?"
    wt_image intro_wife_domme_1_6
    player.c "It feels great, Mistress."
    wt_image intro_wife_domme_1_7
    ivy.c "Follow me."
    wt_image intro_wife_domme_1_8
    ivy.c "You're not going to be able to cum with this cock leash on, are you boy?"
    wt_image intro_wife_domme_1_9
    player.c "No, Mistress.  I don't think so."
    wt_image intro_wife_domme_1_10
    ivy.c "Which means I get to enjoy sucking on your fat, hard cock for as long as I want without worrying about your erection going away."
    wt_image intro_wife_domme_1_11
    "She proceeds to suck on your cock for what seems like a very, very long time, until your balls are aching."
    wt_image intro_wife_domme_1_12
    ivy.c "You'd like to cum now, wouldn't you, boy?"
    player.c "Yes, Mistress.  Please!"
    wt_image intro_wife_domme_1_13
    ivy.c "But I don't feel like letting you cum today.  I like the thought of just enjoying the taste of your cock, then going home and leaving you horny.  What do you think about that?"
    wt_image intro_wife_domme_1_10
    player.c "Ugghhh ... You're in charge, Mistress.  If that's what you want, then I'm glad I've been able to be a hard cock for you to enjoy sucking on."
    wt_image intro_wife_domme_1_9
    ivy.c "Oh wow!!  You're amazing!"
    wt_image intro_wife_domme_1_14
    "She stands up and kisses you, hard and passionately."
    wt_image intro_wife_domme_1_15
    ivy.c "That response makes me want to reward you by letting you cum bucket loads, but also makes me even more turned on by the thought of leaving you horny.  Don't call me 'Mistress' anymore.  Just tell me what I should do?"
    player.c "When you're in charge, Ivy, you should give the submissive what he needs, but take whatever you want."
    wt_image intro_wife_domme_1_5
    ivy.c "You don't really need to cum, do you?"
    wt_image intro_wife_domme_1_6
    player.c "No.  I'm blue balled, but I'll survive that without any psychological or physical problems.  And I enjoyed myself, even if being sucked on without being able to cum was a type of torture."
    wt_image intro_wife_domme_1_14
    "She kisses you again, every bit as passionately as before."
    wt_image intro_wife_domme_1_3
    ivy.c "Thank you for teaching me how to domme a man.  I'll take the leash off your cock after I change.  Hopefully you'll have cooled off enough by then that you won't accidentally cum from the feeling of me taking it off."
    return

label ivy_domme_session_three:
    add tags 'third_domme_session' to ivy
    wt_image current_location.image
    "You strip naked and wait for Mistress to reappear."
    wt_image intro_wife_domme_1_1
    ivy.c "Your cock's already hard."
    wt_image intro_wife_domme_1_4
    ivy.c "You didn't even need to look at my body to get an erection."
    wt_image intro_wife_domme_1_2
    ivy.c "Are you enjoying the thought of being blue balled?"
    player.c "I'm enjoying the thought of pleasing you, Mistress."
    wt_image intro_wife_domme_1_5
    ivy.c "Well, getting a nice big erection for me certainly pleases me, boy."
    wt_image intro_wife_domme_1_8
    ivy.c "A nice fat cock for me to enjoy."
    wt_image intro_wife_domme_1_9
    ivy.c "One I can lick and taste ..."
    wt_image intro_wife_domme_1_10
    ivy.c "... and suck on for as long as I feel like."
    wt_image intro_wife_domme_1_11
    "Fortunately ... or unfortunately ... that turns out to be a very, very long time."
    wt_image intro_wife_domme_1_12
    "Every once in a while she looks up at you and teases the underside of your cock, and you think she's going to stop things there."
    wt_image intro_wife_domme_1_11
    "... then she goes right back to sucking on your dick like it's her favorite flavor lollipop."
    wt_image intro_wife_domme_1_10
    "Finally, there's a reprieve."
    wt_image intro_wife_domme_1_12
    ivy.c "How do your balls feel?"
    wt_image intro_wife_domme_1_13
    player.c "They're absolutely aching, Mistress."
    wt_image intro_wife_domme_1_5
    ivy.c "Mmmmm ... that's exactly how I was hoping you'd feel."
    wt_image intro_wife_domme_1_14
    "Her kiss lasts even longer than last time, the feeling of her lips and hot little tongue in your mouth doing nothing to ease the discomfort in your testicles."
    wt_image intro_wife_domme_1_15
    ivy.c "You are absolutely amazing.  I'm going home to fuck my husband until we both cum at least twice.  I'd like to say I'm sorry to be leaving you worked up, but I'm not.  I'm absolutely loving leaving you like this."
    wt_image intro_wife_domme_1_16
    ivy.c "Thank you for being such a good submissive."
    call ivy_convert_domme from _call_ivy_convert_domme
    return

# Not needed as Cancel is active
# label ivy_train_nothing:
#     pass
#     return

label ivy_sex_proceed_test:
    $ ivy.temporary_count -= ivy.sex_training_count
    $ ivy.temporary_count -= ivy.orgasm_count
    if ivy.temporary_count > 0:
        if ivy.test('desire', 20):
            $ ivy.temporary_count -= 2
        elif ivy.test('desire', 15):
            $ ivy.temporary_count -= 1
        if ivy.temporary_count > 0:
            if ivy.test('resistance', 60):
                $ ivy.temporary_count -= 2
            elif ivy.test('resistance', 65):
                $ ivy.temporary_count -= 1
    return

label ivy_sex_failed_proceed:
    $ ivy.temporary_count = 0
    sys "She's not ready to have this type of sex with you.  Either suggest something else, or try a different course of action."
    #ADD TEXT RE WHAT YOU SHOULD DO NOW
    return

label ivy_strip_proceed_test:
    if ivy.has_tag('watched_milf_stripper'):
        $ ivy.temporary_count -= 1
    if ivy.has_tag('hypno_re_stripping'):
        $ ivy.temporary_count -= 2
    if ivy.has_tag('modelled_sexy_lingerie'):
        $ ivy.temporary_count -= 1
    if ivy.has_tag('considering_stripping'):
        $ ivy.temporary_count -= 1
    if ivy.temporary_count > 0 and ivy.test('desire', 10):
        $ ivy.temporary_count -= 1
    if ivy.temporary_count > 0 and ivy.test('resistance', 60):
        $ ivy.temporary_count -= 2
    elif ivy.temporary_count > 0 and ivy.test('resistance', 65):
        $ ivy.temporary_count -= 1
    return

label ivy_seduce:
    if current_location != boudoir:
        sys "This type of action may work better in the boudoir, if you've added items to it.  Take her there?"
        $ title = "Take her to the boudoir?"
        menu:
            "Yes":
                call forced_movement(boudoir) from _call_forced_movement_950
            "No, stay here":
                pass
    $ ivy.training_session()
    $ ivy.seduction_count += 1
    if ivy.seduction_count == 1:
        player.c "You're a beautiful woman, Ivy."
        wt_image intro_wife_visit_1_6
        ivy.c "Am I now?  I thought I was here to be trained, not flattered."
        player.c "Can't we do both?  Make yourself comfortable while I put some music on."
        wt_image intro_wife_visit_1_7
        ivy.c "Now it sounds like you're planning on seducing me."
        player.c "Maybe.  Or maybe I just want to train you to be a better dancer.  At least take off your coat."
        wt_image intro_wife_visit_1_14
        ivy.c "Are you seriously going to give me a dancing lesson?"
        player.c "Why not?  You enjoy dancing, don't you?"
        wt_image intro_wife_seduce_1_1
        ivy.c "I do, but my husband's not really the dancing type."
        player.c "Then you could probably use the practice."
    else:
        wt_image intro_wife_visit_1_7
        ivy.c "You're putting the music back on.  Does that mean I get another dance lesson?"
        player.c "Has your husband taken you dancing recently?"
        wt_image intro_wife_visit_1_14
        ivy.c "No.  Like I said, he's not the dancing type."
        wt_image intro_wife_seduce_1_1
        player.c "Then you probably still need more practice."
    if not ivy.test('desire', 10):
        "You don't get any further than dancing with her, but it's a fun way to spend the evening.  Ivy enjoyed herself, and is now more romantically inclined towards you."
        change ivy desire by 5
    else:
        wt_image intro_wife_seduce_1_2
        "Ivy gets closer and closer to you as you dance."
        if ivy.domme_comfort > 0:
            ivy.c "Kiss me."
        $ title = "Kiss her?"
        menu:
            "Yes":
                wt_image intro_wife_seduce_1_3
                "Ivy offers no resistance as you lean her head back and kiss her."
                if not ivy.test('desire', 20):
                    wt_image intro_wife_seduce_1_2
                    "Kissing is as far as you get with her today, but you're confident she'll be ready to go further soon."
                    change ivy desire by 10
                else:
                    wt_image intro_wife_seduce_1_2
                    if ivy.domme_comfort > 0:
                        ivy.c "Don't stop."
                    else:
                        ivy.c "You don't have to stop."
                    wt_image intro_wife_seduce_1_4
                    "You pull down Ivy's top ..."
                    wt_image intro_wife_seduce_1_5
                    "... leaving both of you breathing heavily."
                    if ivy.domme_comfort > 2:
                        ivy.c "I want you to fuck me now."
                    elif ivy.has_tag('bj_training'):
                        ivy.c "If you want, I'll show you what a well-trained cocksucker I've become."
                    $ title = "What do you want?"
                    menu:
                        "Be submissive to her" if ivy.has_tag('discussed_taking_charge'):
                            wt_image intro_wife_seduce_1_6
                            player.c "Tell me how I can please you."
                            if ivy.domme_comfort < 3:
                                ivy.c "Oh!  Ummm ... You could eat me out."
                                wt_image intro_wife_seduce_1_7
                                ivy.c "OH!"
                                "You reinforce her sense of control by immediately burying your face in her snatch ..."
                                wt_image intro_wife_seduce_1_8
                                "... then you back off, help her undress, and encourage to exert greater control."
                            else:
                                ivy.c "Oh! Ummm ... Would it excite you to lick my feet before you eat me out?"
                                player.c "Would it excite you?  If it would, I'll happily show you how much it turns me on to worship you."
                                ivy.c "Okay.  Let's do that."
                                wt_image intro_wife_seduce_1_11
                                ivy.c "Oh wow!  That is surprisingly hot.  Your dick is so hard.  Do you need me to take care of that for you?"
                                player.c "I'd rather you tell me what I can do to help you feel good."
                                ivy.c "Well, okay.  In that case, stop licking my feet and start eating me out."
                                "You reinforce her sense of control by immediately burying your face in her snatch ..."
                                wt_image intro_wife_seduce_1_8
                                "... then you back off and encourage to exert greater control."
                            player.c "How do you want me to eat you out?"
                            ivy.c "Mmmm ... run your tongue up and down my slit."
                            wt_image intro_wife_seduce_1_9
                            "You do your best to follow her instructions ..."
                            wt_image intro_wife_seduce_1_10
                            "... and seem to succeed."
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            wt_image intro_wife_seduce_1_12
                            ivy.c "Wow.  That felt great."
                            if ivy.domme_comfort < 3:
                                extend "  You didn't mind following my instructions?"
                                player.c "I enjoyed it.  You're good at it.  You should take charge more often"
                            else:
                                extend "  Show me your cock again."
                                wt_image intro_wife_seduce_1_13
                                player.c "You don't have to ..."
                                wt_image intro_wife_seduce_1_14
                                ivy.c "I'm not going to.  I just wanted to know I was leaving you turned on."
                                "She's starting to get the hang of this."
                            if not ivy.has_tag('instructed_you_on_pussy_licking'):
                                add tags 'instructed_you_on_pussy_licking' to ivy
                                $ ivy.domme_comfort += 1
                            $ ivy.orgasm_count += 1
                            $ ivy.pleasure_her_count += 1
                            change ivy desire by 15
                            change player energy by -energy_short
                        "Pleasure her":
                            wt_image intro_wife_seduce_1_15
                            "You guide her onto the bed and have her wet your fingers ..."
                            wt_image intro_wife_seduce_1_16
                            "... then you use your fingers and your tongue to pleasure her as you undress her ..."
                            wt_image intro_wife_seduce_1_17
                            "... and bring her to orgasm."
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            wt_image intro_wife_seduce_1_12
                            ivy.c "Wow.  That was nice.  Thank you!!"
                            $ ivy.orgasm_count += 1
                            $ ivy.pleasure_her_count += 1
                            change ivy desire by 15
                            change player energy by -energy_short
                        "Fuck her":
                            if ivy.domme_comfort > 2:
                                wt_image intro_wife_seduce_1_18
                                ivy.c "Before I let you fuck me, I want you to show me how much you want to please me."
                                wt_image intro_wife_seduce_1_11
                                "You show her your already hard cock and worship Ivy's shoe as she extends her foot towards you."
                                ivy.c "Wow, that is so hot!  Okay.  You get to fuck me now.  Lie down."
                                wt_image intro_wife_seduce_1_19
                                "Ivy climbs on top of you ..."
                                wt_image intro_wife_seduce_1_20
                                "... and rides you both to orgasm."
                                ivy.c "OH ... I'M CUMMINNGGG!!!"
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_seduce_1_21
                                ivy.c "You really don't mind me taking charge?"
                                player.c "I don't, and I'm sure your husband won't either.  You're good at it."
                                if not ivy.has_tag('instructed_you_to_fuck_her'):
                                    $ ivy.domme_comfort += 1
                                    add tags 'instructed_you_to_fuck_her' to ivy
                            elif ivy.has_tag('had_adventurous_sex'):
                                wt_image intro_wife_seduce_1_22
                                player.c "Where are you going?"
                                ivy.c "To get on the bed.  Didn't you say you wanted to fuck?"
                                player.c "I can do that right where you are."
                                wt_image intro_wife_seduce_1_23
                                "It's a little awkward, but Ivy loves the position and cums quickly.  So do you."
                                ivy.c "OH ... I'M CUMMINNGGG!!!"
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_seduce_1_24
                                ivy.c "I wasn't sure what I was getting into when I agreed to let you train me."
                                wt_image intro_wife_seduce_1_25
                                ivy.c "But I'd never have guessed that I'd start thinking of window sills as suitable places to have sex!"
                            else:
                                wt_image intro_wife_seduce_1_26
                                "As Ivy climbs onto the bed ..."
                                wt_image intro_wife_seduce_1_27
                                "... you take her from behind."
                                wt_image intro_wife_seduce_1_28
                                "She's already wet, and after a few strokes she's even wetter."
                                wt_image intro_wife_seduce_1_29
                                "A few strokes more takes her over the edge."
                                ivy.c "OH ... I'M CUMMINNGGG!!!"
                                "Now it's your turn."
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her":
                                        wt_image intro_wife_seduce_1_30
                                        "You flip her over ..."
                                        wt_image intro_wife_seduce_1_31
                                        "... and empty your load inside her."
                                        player.c "[player.orgasm_text]"
                                        wt_image intro_wife_seduce_1_12
                                        ivy.c "Mmmm.  That was nice."

                                    "On her":
                                        wt_image intro_wife_seduce_1_30
                                        "As you flip her over and pull out ..."
                                        wt_image intro_wife_seduce_1_32
                                        "... she takes your cock in her hand and pumps your load onto her waiting belly."
                                        player.c "[player.orgasm_text]"
                                        wt_image intro_wife_seduce_1_12
                                        ivy.c "Mmmm.  That was nice.  Messy, but nice."
                            change ivy desire by 10
                            orgasm
                            $ ivy.orgasm_count += 1
                            $ ivy.sex_count += 1
                        "Have her blow you":
                            if ivy.domme_comfort > 2:
                                player.c "I'd rather you blow me."
                                wt_image intro_wife_seduce_1_43
                                ivy.c "Okay, but lie back.  We're doing this my way."
                                wt_image intro_wife_seduce_1_44
                                "She tackles your cock with enthusiasm, nuzzling and licking and teasing it ..."
                                wt_image intro_wife_seduce_1_45
                                "... before extracting the sperm from your balls through suction and sheer determination."
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_seduce_1_3
                                ivy.c "Good boy.  Your sperm tasted delicious."
                                $ ivy.swallow_count += 1
                            elif ivy.has_tag('bj_training'):
                                wt_image intro_wife_seduce_1_18
                                player.c "Okay.  Come here and show me what you can do with that talented cocksucking mouth of yours."
                                wt_image intro_wife_seduce_1_43
                                "She warms your balls up through your shorts ..."
                                wt_image intro_wife_seduce_1_46
                                "... and waits for permission to start pleasuring your shaft with her tongue and lips."
                                wt_image intro_wife_seduce_1_14
                                "She maintains eye contact as she suckles you, looking to you for an indication of how you want to finish."
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her":
                                        wt_image intro_wife_seduce_1_47
                                        "She keeps her lips firmly wrapped around your cock ..."
                                        wt_image intro_wife_seduce_1_13
                                        "... and swallows every spurt as you unload in her mouth."
                                        player.c "[player.orgasm_text]"
                                        wt_image intro_wife_seduce_1_3
                                        $ ivy.swallow_count += 1
                                    "On her":
                                        wt_image intro_wife_seduce_1_46
                                        "She closes her eyes briefly as you remove your cock ..."
                                        wt_image intro_wife_bj_1_20
                                        "... then remembers to open them as you unload."
                                        player.c "[player.orgasm_text]"
                                        wt_image intro_wife_seduce_1_48
                                        $ ivy.facial_count += 1
                                ivy.c "Was I a good cocksucker for you?"
                                player.c "You did great."
                            else:
                                player.c "I want your mouth on me."
                                wt_image intro_wife_seduce_1_18
                                "Ivy moves closer ..."
                                wt_image intro_wife_seduce_1_46
                                "... opens her mouth as you take out your cock ..."
                                wt_image intro_wife_seduce_1_13
                                "... and then wraps her lips around it as you place it in her."
                                wt_image intro_wife_seduce_1_14
                                "It's a sweet and seductive blow job, with lots of eye contact ..."
                                wt_image intro_wife_seduce_1_47
                                "... and as you start to cum ..."
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_seduce_1_13
                                "... she swallows down every spurt."
                                wt_image intro_wife_seduce_1_3
                                ivy.c "Thank you for the dancing lesson."
                                player.c "Thank you."
                                $ ivy.swallow_count += 1
                            $ ivy.blowjob_count += 1
                            change ivy desire by 10
                            orgasm
                        "Anal" if ivy.anal_count > 0:
                            wt_image intro_wife_seduce_1_33
                            ivy.c "My ass again?  Wouldn't you rather fuck my pussy?"
                            player.c "Tempting, but no.  Clearly you still need practice.  I don't want you hesitating like this when your husband's in the mood for anal."
                            wt_image intro_wife_seduce_1_34
                            "She may have hesitated, but you're pleased to see her rosebud is already opening up in anticipation of what's to come."
                            wt_image intro_wife_seduce_1_35
                            "Slowly and carefully you complete the process of opening her up enough to accept your cock head."
                            player.c "That's it, Ivy.  Just relax.  You'll have my full cock inside you in no time."
                            wt_image intro_wife_seduce_1_36
                            player.c "There. That's as wide as you need to stretch. Is this starting to feel good?"
                            ivy.c "I wouldn't say good.  It's uncomfortable, but bearable."
                            player.c "Turn over.  Carefully.  I want you to show me your pussy again."
                            wt_image intro_wife_seduce_1_37
                            player.c "Your body's enjoying this more than you're letting yourself realize, Ivy.  Your pussy's wet and your clit is standing at attention."
                            ivy.c "But my ass is sore."
                            player.c "Sore can still be exciting. I want you to ride my cock, up and down as fast as you can.  Don't judge, just go with the sensation, then rub your clit, hard."
                            wt_image intro_wife_seduce_1_38
                            "Gamely she does her best to ride you.  Not exactly fast, but you didn't tell her how long to ride you, and she keeps at it longer than you expected.  It's everything you can do to hold back your orgasm until she finally stops ..."
                            wt_image intro_wife_seduce_1_39
                            "... and rubs her clit, bringing herself to a quick orgasm that she doesn't even try to hold back."
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            "Now it's your turn."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image intro_wife_seduce_1_38
                                    "When her orgasm subsides, Ivy resumes riding you.  You couldn't hold yourself back any longer if you wanted to."
                                    player.c "[player.orgasm_text]"
                                    wt_image intro_wife_seduce_1_12
                                    ivy.c "Wow.  Now both my ass and my pussy are tender, though in very different ways."
                                "On her":
                                    wt_image intro_wife_seduce_1_40
                                    "Ivy's confused when she feels you pull out."
                                    ivy.c "Did you cum already?"
                                    player.c "Not yet.  But you can help me with that."
                                    wt_image intro_wife_seduce_1_41
                                    "It takes only a few strokes of her soft hand to finish the job her tight ass started."
                                    player.c "[player.orgasm_text]"
                                    wt_image intro_wife_seduce_1_42
                                    ivy.c "Wow.  A sore ass and a face full of cum.  You sure know how to show a girl a good time."
                            player.c "You're welcome.  You forgot to mention I also taught you to orgasm with a dick up your ass.  Are you feeling trained yet?"
                            ivy.c "Very"
                            if not ivy.has_tag('anal_orgasm'):
                                add tags 'anal_orgasm' to ivy
                                change ivy sos by 10
                                change ivy resistance by -5
                            $ ivy.orgasm_count += 1
                            $ ivy.anal_count += 1
                            change ivy desire by 10
                            orgasm
                        "End the evening there":
                            player.c "I think that's enough for today."
                            ivy.c "Seriously?  You're sending me home now?"
                            "Ivy's confused by your rejection of her.  If she were a more challenging client, she might suffer a stat decline, but since she isn't, she just heads home."
            "No, just spend the evening dancing":
                wt_image intro_wife_seduce_1_1
                "If Ivy's disappointed, she tries not to show it.  She enjoyed the time you spent dancing with her, and is now more romantically inclined towards you."
                change ivy desire by 5
    change player energy by -energy_long notify
    end_day
    return

label ivy_discipline:
    if current_location != dungeon:
        sys "This type of action may work better in the dungeon, if you've added items to it.  Take her there?"
        $ title = "Take her to the dungeon?"
        menu:
            "Yes":
                call forced_movement(dungeon) from _call_forced_movement_951
            "No, stay here":
                pass
    if ivy.spank_count == 0:
        player.c "Your training will go better once you have the right attitude.  Corporal discipline should help."
        wt_image intro_wife_visit_1_4
        ivy.c "What do you mean by 'corporal discipline'?"
        player.c "I mean a spanking, Ivy.  To put you in the right frame of mind to learn."
        if not ivy.test('submission', 1):
            ivy.c "No way.  You can teach me whatever it is you plan to teach me without hitting me."
            sys "You either need to be naturally dominant, equip your dungeon with items that inspire submission, or otherwise increase her submission before she'll accept a spanking."
        else:
            $ ivy.training_session()
            wt_image intro_wife_visit_1_10
            ivy.c "You can teach me without hitting me."
            player.c "Spanking's a very specialized form of hitting, Ivy.  It's been used for centuries to help train the spankee.  You're about to find out why.  Remove your coat and come here."
            wt_image intro_wife_visit_1_12
            ivy.c "Will it hurt?"
            player.c "It wouldn't be nearly as effective for training if it didn't.  Come closer."
            wt_image intro_wife_spank_1_1
            ivy.c "I guess I'll let you try it once, but if it's too painful I'm calling this off.  What am I supposed to do?"
            player.c "Turn around and present your ass to me."
            wt_image intro_wife_spank_1_2
            ivy.c "Like this?"
            player.c "Yes.  Now lift your skirt."
            wt_image intro_wife_spank_1_3
            ivy.c "Hang on!  You didn't say anything about me being naked."
            player.c "Lifting your skirt is hardly the same as you being naked.  Do you have panties on?"
            wt_image intro_wife_spank_1_4
            ivy.c "Of course I have panties on, but still ..."
            player.c "Would you be exposing anything more of your butt cheeks than you do when you go to the beach?"
            wt_image intro_wife_spank_1_5
            ivy.c "No, but it feels different."
            player.c "More vulnerable.  I know, that's intended.  It'll also sting more.  That's also intended.  There's no point in me spanking you if you're not going to get the full benefit from it, is there?"
            wt_image intro_wife_spank_1_6
            ivy.c "That's a really weird form of logic."
            wt_image intro_wife_spank_1_7
            ivy.c "Well?  What are you waiting for?"
            player.c "Impatient?"
            ivy.c "No, but I did what you asked and you're just standing there.  I'm sure my butt's not that mesmerizing."
            player.c "I'm giving you a moment to enjoy the anticipation.  And yes, I'm enjoying looking at your butt while you wait.  It'll be a lot redder in a moment, you realize?"
            ivy.c "Please, can't we just get this over with?"
            player.c "Asking for a spanking already?  You may need less training than I realized.  Okay, since you asked nicely, turn a little more to your right."
            wt_image intro_wife_spank_1_8
            ivy.c "Like this?"
            "*smack*"
            wt_image intro_wife_spank_1_9
            ivy.c "Ow!  That stung!  Shouldn't you have given me a warning or something that you were going to start?"
            wt_image intro_wife_spank_1_8
            player.c "Now who's using weird logic?  Okay, I'm going to spank you again, Ivy, and it's going to sting just as much as the first."
            "*smack*"
            wt_image intro_wife_spank_1_9
            ivy.c "Ow!  Okay, I think that's enough."
            wt_image intro_wife_spank_1_8
            player.c "That's certainly enough of you squealing like a schoolgirl.  Bite your tongue and take your spanking like a woman."
            wt_image intro_wife_spank_1_10
            "Ivy wriggles her hips involuntarily, but manages to avoid crying out as you finish her spanking ... *smack*  *smack*  *smack*  *smack*  *smack*"
            wt_image intro_wife_spank_1_6
            ivy.c "That hurt.  You didn't need to do that."
            wt_image intro_wife_spank_1_5
            player.c "It stung, it didn't hurt anything, other than maybe your pride.  You're here to be trained, and I'll decide what I need to do to put you in the right attitude for training."
            "Whatever else she may have felt about the experience, letting you spank her has left Ivy more submissively inclined towards you."
            $ ivy.spank_count += 1
            change ivy submission by 10
            change player energy by -energy_long
            end_day
    elif ivy.spank_count == 1:
        $ ivy.training_session()
        player.c "Time for another attitude adjustment, Ivy.  Present your ass for a spanking."
        wt_image intro_wife_visit_1_10
        ivy.c "But you've already done that."
        player.c "And I think you need another, as part of your training.  Remove your clothes."
        wt_image intro_wife_visit_1_14
        ivy.c "Don't you mean lift my skirt?"
        player.c "No, I mean remove your skirt. And your top."
        wt_image intro_wife_visit_1_15
        ivy.c "Why?  That isn't needed to spank me."
        player.c "It's part of the attitude adjustment, Ivy.  That business suit is very nice, but it's the wrong attire for you to be wearing for training."
        wt_image intro_wife_visit_1_16
        ivy.c "You think stripping me down to my underwear is the right attire?"
        player.c "I think it better reflects the nature of our relationship."
        wt_image intro_wife_visit_1_17
        ivy.c "A relationship in which you get to stay fully clothed while I'm left feeling exposed and vulnerable?"
        player.c "And subservient.  Present your ass to me."
        wt_image intro_wife_visit_1_18
        ivy.c "I can't figure out which is worse.  Waiting like this while you ogle me or asking you to start spanking me already."
        player.c "Depends on what type of submissive you are.  Some enjoy begging, others prefer the anticipation of waiting."
        ivy.c "I'm not submissive."
        player.c "Of course not.  You're just waiting to be spanked by the man your husband hired to train you.  Which is it going to be?  Are you going to beg or wait?"
        ivy.c "I ... I don't know.  Which do you want?"
        player.c "That's the right attitude."
        "*smack*"
        wt_image intro_wife_visit_1_19
        ivy.c "Ow!"
        player.c "You need to stop crying out like that.  How am I supposed to judge what you're really feeling if you yelp after every love tap?"
        wt_image intro_wife_visit_1_20
        "She controls herself and keeps silent for the spanking, until you give her an extra sharp swat at the end ... *smack*  *smack*  *smack*  *smack*  *smack*  *SMACK*"
        wt_image intro_wife_visit_1_19
        ivy.c "Ow!  That one really did sting.  Honest!!"
        player.c "I believe you, but that was mostly because it caught you by surprise.  The next five will feel the same.  Stay silent during them."
        wt_image intro_wife_visit_1_20
        "Ivy's butt wriggles uncontrollably, but she manages to stay quiet until the last swat ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
        wt_image intro_wife_visit_1_19
        ivy.c "Ow!  Sorry, but my butt's really sore now."
        player.c "I know.  Would you like me to keep going?"
        ivy.c "Why would I want you to keep spanking me?"
        player.c "Because of the warmth radiating from butt through to between your legs.  You've done very well.  I'll give you have a 'good girl spanking' as a reward if you'd like?"
        wt_image intro_wife_visit_1_18
        ivy.c "Some submissives actually want to be spanked?"
        player.c "When it's not a punishment, yes.  Spanked properly, some of them can cum just from the spanking, though most need a finger or two or something to grind against to help them over the edge.  Did you want to try?"
        wt_image intro_wife_visit_1_21
        ivy.c "No!  Can I get dressed now?"
        "You're not sure if her reticence is out of fear of the continued spanking or out of fear of discovering she may enjoy it.  Either way, you send her home feeling more submissively inclined towards you."
        $ ivy.spank_count += 1
        change ivy submission by 10
        change player energy by -energy_long
        end_day
    elif ivy.has_tag('spanking_orgasm'):
        "Ivy's learned as much from this activity as she's going to learn."
        $ title = "What do you do?"
        menu:
            "Spank her to another orgasm anyway":
                $ ivy.training_session()
                player.c "I'm going to spank you again, Ivy."
                wt_image intro_wife_visit_1_14
                ivy.c "Is this a punishment or ..."
                wt_image intro_wife_visit_1_16
                player.c "What type of spanking would you like it to be?"
                wt_image intro_wife_visit_1_23
                ivy.c "I'd prefer a good girl spanking."
                wt_image intro_wife_visit_1_25
                player.c "What should you do then?"
                wt_image intro_wife_visit_1_35
                ivy.c "May I please have a good girl spanking, Sir?"
                player.c "Will you cum for me if I let you have a spanking?"
                ivy.c "Yes, Sir.  As embarrassing as it is, I'd still enjoy cumming for you while you spank me."
                wt_image intro_wife_visit_1_36
                "Ivy's training seems to have come along nicely ... *smack*  *smack*  *smack*  *smack*  *smack*"
                wt_image intro_wife_visit_1_37
                "You take your time and stretch the spanking out ... *smack*  *smack*  *smack*  *smack*  *smack*"
                wt_image intro_wife_visit_1_38
                "... which makes her subsequent orgasm all the more intense."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_visit_1_40
                ivy.c "I didn't know what to expect when I agreed to be trained, but I didn't think I'd ever end up asking for a spanking."
                $ ivy.spank_count += 1
                $ ivy.orgasm_count += 1
                change player energy by -energy_long
                end_day
            "Try something else":
                pass
    else:
        $ ivy.training_session()
        player.c "I'm going to spank you again, Ivy."
        wt_image intro_wife_visit_1_14
        ivy.c "Seriously?  Do you really feel like my attitude still needs to be adjusted?"
        wt_image intro_wife_visit_1_16
        player.c "We're about to find out.  You're going to be completely naked for today's spanking."
        if ivy.has_tag('received_punishment_spanking') or ivy.test('submission', 40):
            $ ivy.training_session()
            wt_image intro_wife_visit_1_23
            ivy.c "Is this to humiliate me more?"
            wt_image intro_wife_visit_1_27
            player.c "Yes, although I admit I'm also enjoying the view of your body."
            wt_image intro_wife_visit_1_28
            ivy.c "I might be flattered by that under other circumstances."
            player.c "Don't you want me to enjoy spanking you?"
            ivy.c "Please stop teasing me and just spank me."
            player.c "Does that mean you're in the mood to beg?"
            ivy.c "If that's what you want.  Please, Sir, I'm ready to be spanked."
            "*SMACK*"
            wt_image intro_wife_visit_1_29
            ivy.c "OW!  Shoot, I wasn't expecting you to start so rough."
            player.c "Begging tends to inspire a more vigorous swatting.  Put your hands down."
            wt_image intro_wife_visit_1_30
            "Ivy holds her hands away as you tan her shapely behind ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
            wt_image intro_wife_visit_1_31
            ivy.c "Ohhh ... my butt's stinging even more than after the last spanking."
            player.c "And yet you took it without making hardly a sound.  Good girl.  Get down on the floor."
            wt_image intro_wife_visit_1_32
            ivy.c "Wasn't it humiliating enough that I was naked?  I need to be on all fours, too?"
            "*SMACK*"
            wt_image intro_wife_visit_1_33
            ivy.c "OWW!!  Sorry, but my butt's really sore right now."
            player.c "You feel like you need to be rubbing it?"
            ivy.c "Yes"
            player.c "I'm going to continue spanking you, Ivy, but I don't want you rubbing your butt.  I want you to rub between your legs."
            wt_image intro_wife_visit_1_34
            ivy.c "More humiliation?"
            player.c "You being on the floor and touching yourself isn't to humiliate you, Ivy.  It's so you can enjoy your good girl spanking."
            ivy.c "I ... I don't think I want that type of 'reward'."
            player.c "I'm going to keep spanking you, Ivy.  If your hand is between your legs, it'll be a good girl spanking.  If it isn't, it'll be a punishment spanking.  Which is it going to be?"
            wt_image intro_wife_visit_1_35
            player.c "That's a good girl.  Now you can rub with your hand as much as you need to to alleviate the sting of the spanking."
            wt_image intro_wife_visit_1_36
            "You make it a sensual spanking.  As sore as her butt is, even the lightest swats are uncomfortable, but the heat of each blow goes directly to her pussy, and she rubs herself more and more vigorously as you spank her ... *smack*  *smack*  *smack*"
            wt_image intro_wife_visit_1_37
            "*smack*  *smack*  *smack* ... Her hand moves faster and faster, her fingers sliding over her clit and into her rapidly wetting slit until  ..."
            wt_image intro_wife_visit_1_38
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_1_39
            player.c "Shall I tell your husband about the new trick you've learned, or would you rather do it?"
            ivy.c "I'll tell him, but not until my bum's less sore.  Wow, I can't believe how the heat from the spanking is still making my pussy throb."
            "Ivy's feeling trained, and more submissive towards you.  Not to mention turned on."
            change ivy sos by 10
            change ivy submission by 10
            change ivy desire by 10
            $ ivy.spank_count += 1
            $ ivy.orgasm_count += 1
            add tags 'spanking_orgasm' to ivy
            change player energy by -energy_long
            end_day
        else:
            wt_image intro_wife_visit_1_15
            ivy.c "What??  No way!  Being spanked in my underwear is humiliating enough."
            $ title = "What do you do?"
            menu:
                "Spank her in her underwear":
                    $ ivy.training_session()
                    wt_image intro_wife_visit_1_17
                    player.c "Then I guess we have our answer.  Turn around and present your ass to me."
                    wt_image intro_wife_visit_1_20
                    "*SMACK*"
                    ivy.c "Ow!  That was harder than before."
                    player.c "Indeed it was.  These will be harder still."
                    wt_image intro_wife_visit_1_19
                    "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    ivy.c "Ow!  Ow!!  OW!!!  OWWW!!!  That's really hurting!"
                    wt_image intro_wife_visit_1_18
                    player.c "That's because this is a punishment spanking, Ivy."
                    ivy.c "Punishment?  Just because I said 'no'?"
                    player.c "That's exactly why.  I didn't ask anything of you that you aren't capable of doing.  Had you listened, you'd be getting a good girl spanking right now.  Since you didn't, it's a punishment."
                    wt_image intro_wife_visit_1_19
                    "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    ivy.c "OW!!!  OWWW!!!  OWWW!!!  OWWW!!!  I'M SORRY!!!"
                    wt_image intro_wife_visit_1_22
                    player.c "Good.  Is there something you'd like to do now to demonstrate that you learned your lesson?"
                    wt_image intro_wife_visit_1_23
                    ivy.c "Is this enough?"
                    player.c "No"
                    wt_image intro_wife_visit_1_24
                    player.c "Are you finding this humiliating?"
                    ivy.c "Very"
                    wt_image intro_wife_visit_1_25
                    player.c "Are you going to survive the humiliation?"
                    ivy.c "I guess."
                    player.c "Would you like your good girl spanking now?"
                    "She hesitates, then shakes her head."
                    ivy.c "May I please just go home?"
                    "This was an intense experience for her, and she learned some things about herself she needs time to process. You can let her have that time, or you can intensify the experience."
                    $ title = "What do you do?"
                    menu:
                        "Let her go home":
                            player.c "Yes, Ivy.  You can dress and go home.  You did very well today."
                            wt_image intro_wife_visit_1_16
                            ivy.c "Did I?  I'm sorry I disappointed you at the start."
                            player.c "Submissives are always disappointed in themselves when they need to be punished, but sometimes it's necessary to help them deepen their submission."
                            wt_image intro_wife_visit_1_10
                            ivy.c "I really don't think I'm a submissive, although I guess that's stupid of me to say after how I let you treat me."
                            if ivy.test('sos', 1):
                                "She was already feeling trained.  Now she's more favorably disposed to you on multiple levels."
                            else:
                                "She's still conflicted and doesn't feel properly trained yet, but she's more favorably disposed to you on multiple levels."
                            change ivy submission by 10
                            change ivy desire by 10
                            change ivy resistance by -10
                        "Have her expose herself more":
                            player.c "Not until you expose yourself more.  Lie down and give me a show to make it up to me for disobeying me earlier."
                            wt_image intro_wife_visit_1_26
                            "Ivy's surprised to find she's willing to subject herself to the humiliation of exposing herself like this while you're fully clothed.  You let her process the feelings while you enjoy the few for half-an-hour, then send her home."
                            change ivy submission by 15
                    add tags 'received_punishment_spanking' to ivy
                    $ ivy.spank_count += 1
                    change player energy by -energy_long
                    end_day
                "Try something else":
                    wt_image intro_wife_visit_1_12
                    "Ivy re-dresses as you re-consider her training for today."
    return

# End Session
label ivy_end_session:
    if ivy.status == "on_training":
        $ title = "WARNING: This will end your training session with her."
        menu:
            "Yes, end session":
                $ ivy.training_session()
                "You're unable to find an activity that both you and Ivy are willing to proceed with, so you end today's session here."
                $ player.extra_clients_fee_this_week -= ivy.pay # so you don't get paid for training her this week
                add tags 'failed_regular_training_this_week' to ivy
                call character_location_return(ivy) from _call_character_location_return_652
                end_day
            "Oops, never mind":
                pass
    elif ivy.has_tag('continuing_actions'):
        $ ivy.training_session()
        "You've spent enough time with Ivy for today. You send her home."
        call character_location_return(ivy) from _call_character_location_return_653
        wt_image current_location.image
    else:
        # If somehow the character still has this action when the action is no longer relevant, remove this action
        add tags 'shut_off_end_session' to ivy
    return

# Weekend Actions
label ivy_pre_weekend:
    add tags 'checking_for_weekend' to ivy
    return

label ivy_post_weekend:
    if ivy.has_tag('checking_for_weekend'):
        rem tags 'checking_for_weekend' from ivy
        wt_image current_location.image
    else:
        $ ivy.training_session()
        $ ivy.weekend_training_sessions += 1
        if ivy.has_tag('failed_regular_training_this_week'):
            rem tags 'failed_regular_training_this_week' from ivy
            $ player.extra_clients_fee_this_week += ivy.pay
    return

label ivy_weekend:
    if player.energy >= energy_long.value:
        wt_image intro_wife_phone_1_1
        if ivy.weekend_training_sessions == 0:
            ivy.c "Oh, hi!  I wasn't expecting to hear from you on the weekend. My husband said this arrangement was going to be at most once a week at your house."
            player.c "I know, but I have some free time this weekend, and I'd like to continue your training.  How about I take you somewhere?"
            ivy.c "Where did you have in mind?"
        else:
            ivy.c "Oh, hi!  Did you want to take me somewhere again this weekend?"
        call expandable_menu(ivy_weekend_training_menu) from _call_expandable_menu_112
    else:
        sys "You don't have enough energy for this action, choose something else."
    return

label ivy_weekend_strip_club:
    if not ivy.resistance < 75:
        wt_image intro_wife_phone_1_3
        ivy.c "A strip club?  No way am I going to a strip club with you."
        sys "You need to lower her resistance to you before you can convince her to do this.  Try something else."
    else:
        $ ivy.strip_show_count += 1
        rem tags 'checking_for_weekend' from ivy
        if ivy.strip_show_count == 1 and ivy.sex_show_count == 0:
            ivy.c "A strip club?  Why would I want to go there?"
            player.c "It's part of your training."
            wt_image intro_wife_phone_1_2
            ivy.c "Okay.  Send me the address and I'll meet you there."
        elif ivy.strip_show_count == 1 and ivy.sex_show_count > 0:
            wt_image intro_wife_phone_1_2
            ivy.c "A strip club?  I guess that's a little more respectable than than visiting a sex show.  Send me the address and I'll meet you there."
        else:
            wt_image intro_wife_phone_1_2
            ivy.c "The strip club again?  Okay, I'll meet you there."
        call forced_movement(outdoors) from _call_forced_movement_952
        summon ivy
        if ivy.strip_show_count == 1:
            wt_image intro_wife_weekend_strip_club_2
            ivy.c "I can't believe you're taking me in here."
            wt_image intro_wife_weekend_strip_club_3
            player.c "It'll be fun.  Come on."
        else:
            wt_image intro_wife_weekend_strip_club_3
            "With some trepidation, Ivy follows you back into the strip joint."
        wt_image intro_wife_weekend_strip_club_1
        "A number of dancers are performing on different stages.  Who did you want to take her to watch?"
        $ ivy.strip_show_count += 1
        $ title = "What show do you take her to watch?"
        menu:
            "Male Stripper":
                wt_image intro_wife_weekend_strip_club_4
                ivy.c "Do we have to sit so close to the stage?"
                player.c "You'll appreciate the close up view in a moment."
                wt_image intro_wife_weekend_strip_club_12
                "Ivy laughs as she sees the man step onto the stage."
                wt_image intro_wife_weekend_strip_club_5
                ivy.c "Oh my god!  I can't believe you brought me to watch this."
                wt_image intro_wife_weekend_strip_club_13
                player.c "Did you think taking your clothes off was for women only?"
                wt_image intro_wife_weekend_strip_club_14
                ivy.c "Not at all.  I'm totally in favor of this sort of men's liberation."
                wt_image intro_wife_weekend_strip_club_15
                player.c "See the benefit of sitting close, now?  You get a better look at his liberation."
                ivy.c "Mmmmm.  Thanks for that!"
                wt_image intro_wife_weekend_strip_club_16
                if ivy.has_tag('discussed_taking_charge') and not ivy.has_tag('strip_show_taking_charge_conversation'):
                    add tags 'strip_show_taking_charge_conversation' to ivy
                    player.c "Maybe you could tell your husband to dance like that for you."
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "Oh my god!  That would be so funny.  Do you think he would?"
                    player.c "If you told him to do so to please you."
                    ivy.c "He'd be embarrassed."
                    player.c "That would add to his fun."
                    "Ivy tries not to let on that she's giving the idea some thought.  Try working on other activities to help her get comfortable taking charge."
                    $ ivy.domme_comfort += 1
                    change ivy desire by 5
                elif ivy.has_tag('discussed_taking_charge') and ivy.has_tag('strip_show_taking_charge_conversation'):
                    player.c "Have you told your husband to dance for you, yet?"
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "No.  I couldn't do that."
                    "Not yet, maybe, but in time she could."
                    change ivy resistance by -5
                    change ivy desire by 5
                else:
                    "Ivy enjoyed herself, and associated becoming turned on with spending time with you. She's now a little more sexually inclined towards you."
                    change ivy desire by 5
            "Female Stripper":
                if not ivy.has_tag('watched_female_stripper'):
                    wt_image intro_wife_weekend_strip_club_8
                    "You settle down in front of a stage where a young brunette woman is dancing."
                else:
                    wt_image intro_wife_weekend_strip_club_8
                    "The young dancer is just starting her routine again as you find a seat."
                wt_image intro_wife_weekend_strip_club_9
                player.c "She looks good up there, isn't she?"
                wt_image intro_wife_weekend_strip_club_7
                ivy.c "Don't remind me.  I used to have a body like that, once."
                wt_image intro_wife_weekend_strip_club_10
                ivy.c "Well, maybe not as good as hers.  But better than I have now."
                wt_image intro_wife_weekend_strip_club_7
                player.c "You'd look good up there, too."
                wt_image intro_wife_weekend_strip_club_11
                if ivy.has_tag('watched_milf_stripper'):
                    ivy.c "I don't know.  I'd look so old compared to her."
                    wt_image intro_wife_weekend_strip_club_6
                    player.c "You're a beautiful woman, Ivy.  You've seen for yourself that beautiful women look good taking off their clothes, no matter what their age."
                    "She doesn't reply, but she's contemplating what you said."
                else:
                    ivy.c "Oh please.  I'd look ridiculous compared to her."
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "Thanks for reminding me what the competition looks like, though.  If I'm going to keep my husband happy with my middle-aged body, I guess I really do need to learn new tricks."
                    "That may or may not have been the impression you intended to leave, but she's become more open to listening to your suggestions."
                if not ivy.has_tag('watched_female_stripper'):
                    add tags 'watched_female_stripper' to ivy
                    change ivy resistance by -10
                else:
                    change ivy resistance by -5
            "Older Female Stripper" if ivy.has_tag('discussed_stripping'):
                if ivy.has_tag('watched_milf_stripper'):
                    wt_image intro_wife_weekend_strip_club_18
                    "The woman is just starting her routine again as you find a seat."
                    wt_image intro_wife_weekend_strip_club_20
                    "Ivy watches quietly as she dances."
                    wt_image intro_wife_weekend_strip_club_21
                    "Like the dancer, Ivy seems most interested by the reactions of the men in the audience ..."
                    wt_image intro_wife_weekend_strip_club_22
                    "... and like the dancer, Ivy can tell that young or old, the men's reactions consist of a tightening in their pants."
                elif ivy.has_tag('watched_female_stripper'):
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "You want me to watch another stripper?  I know college girls look good taking off their clothes."
                    player.c "This one's different.  Watch."
                    wt_image intro_wife_weekend_strip_club_17
                    player.c "I don't think she's in college, do you?"
                    wt_image intro_wife_weekend_strip_club_18
                    ivy.c "No.  She looks to be around my age."
                    wt_image intro_wife_weekend_strip_club_20
                    player.c "How's she doing at entertaining the crowd?"
                    wt_image intro_wife_weekend_strip_club_19
                    ivy.c "The men do seem to be enjoying her act.  Even some younger men are watching."
                    wt_image intro_wife_weekend_strip_club_21
                    player.c "They're not just watching.  They're getting turned on.  Check out their crotches."
                    wt_image intro_wife_weekend_strip_club_22
                    ivy.c "Oh my god!  That's what she's doing.  She's checking you out to see if you're hard."
                else:
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "You want me to watch a stripper?  I already know college girls look good taking off their clothes."
                    player.c "They do, but they're not the only ones who look good taking off their clothes.  Watch."
                    wt_image intro_wife_weekend_strip_club_17
                    player.c "I don't think she's in college, do you?"
                    wt_image intro_wife_weekend_strip_club_18
                    ivy.c "No.  She looks to be around my age."
                    wt_image intro_wife_weekend_strip_club_20
                    player.c "How's she doing at entertaining the crowd?"
                    wt_image intro_wife_weekend_strip_club_19
                    ivy.c "The men do seem to be enjoying her act.  Even some younger men are watching."
                    wt_image intro_wife_weekend_strip_club_21
                    player.c "They're not just watching.  They're getting turned on.  Check out their crotches."
                    wt_image intro_wife_weekend_strip_club_22
                    ivy.c "Oh my god!  That's what she's doing.  She's checking you out to see if you're hard."
                wt_image intro_wife_weekend_strip_club_22
                player.c "You'd enjoy using your body that way to make men hard, too."
                if ivy.has_tag('stripped_for_you'):
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "When I took my clothes off for you, did you think I was as good as she was?"
                    player.c "Better.  My cock was rock solid after you stripped for me.  You're a natural seductress, Ivy."
                    "She's more than a bit flattered at the complement."
                    change ivy desire by 5
                elif ivy.has_tag('watched_milf_stripper'):
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "She does look like she's enjoying herself.  I'd like to be able to tease a man like that."
                    "Hopefully that's the reaction you wanted her to have."
                    change ivy resistance by -5
                else:
                    wt_image intro_wife_weekend_strip_club_6
                    ivy.c "I'm not as bold as her.  I'd look awkward and ridiculous."
                    player.c "Not with a bit of practice, you wouldn't.  You don't have to start in front of a room full of people.  You can start by using your body to turn one guy on at a time."
                    "She doesn't reply, but she's contemplating what you said."
                    add tags 'considering_stripping' to ivy
                    change ivy resistance by -5
                if not ivy.has_tag('watched_milf_stripper'):
                    add tags 'watched_milf_stripper' to ivy
        notify
        call character_location_return(ivy) from _call_character_location_return_654
        call forced_movement(living_room) from _call_forced_movement_953
        end_day
    return

label ivy_weekend_sex_show:
    if not ivy.resistance < 70:
        wt_image intro_wife_phone_1_3
        ivy.c "A sex show?  No way am I going to a sex show with you."
        sys "You need to lower her resistance to you before you can convince her to do this.  Try something else."
    else:
        rem tags 'checking_for_weekend' from ivy
        if ivy.sex_show_count == 0:
            if ivy.strip_show_count == 0:
                ivy.c "A sex show?  You can't be serious??"
            else:
                ivy.c "A sex show?  That's sounds even seedier than dragging me to a strip club."
            if ivy.has_tag('discussed_taking_charge') or ivy.submission > 0:
                player.c "It's part of your training, Ivy.  With luck, we might catch a BDSM act where you can meet some well trained people."
                wt_image intro_wife_phone_1_2
                ivy.c "I'm not sure I like the sound of that, but okay.  Send me the address and I'll meet you there."
            else:
                player.c "It's part of your training, Ivy.  With luck, you might learn a trick or two from the performers."
                wt_image intro_wife_phone_1_2
                ivy.c "Okay.  Send me the address and I'll meet you there."
        else:
            wt_image intro_wife_phone_1_2
            ivy.c "Another sex show?  Okay, I'll meet you there."
        call forced_movement(outdoors) from _call_forced_movement_954
        summon ivy
        wt_image intro_wife_weekend_sex_show_1
        if ivy.sex_show_count == 0:
            player.c "You look nice."
            wt_image intro_wife_weekend_sex_show_2
            ivy.c "I didn't know what to wear.  How are you supposed to dress to watch other people have sex?"
            player.c "In as little or as much as you like.  That dress looks good on you, but it might get messy in here.  Did you want to take it off before we go in?"
            wt_image intro_wife_weekend_sex_show_3
            ivy.c "Are you serious?"
            player.c "Of course not.  You can wait until we're inside to remove your dress.  I'm still kidding.  Come on."
        else:
            ivy.c "Come on.  Let's go."
            player.c "Anxious to see the show?"
            ivy.c "I'm anxious to get inside before someone sees me."
        wt_image intro_wife_weekend_sex_show_4
        "The place is crowded.  A number of stages have been set up around the converted warehouse, each with a different scene playing out on it."
        $ ivy.sex_show_count += 1
        $ title = "What show do you take her to watch?"
        menu:
            "Sex show":
                $ ivy.normal_sex_show_outfit += 1
                if ivy.normal_sex_show_outfit > 2:
                    $ ivy.normal_sex_show_outfit = 1
                if ivy.normal_sex_show_outfit == 1:
                    wt_image intro_wife_weekend_normal_sex_show_1_1
                    "A good looking couple is getting comfortable on stage."
                    wt_image intro_wife_weekend_normal_sex_show_1_2
                    "They seem to be into each other ..."
                    wt_image intro_wife_weekend_normal_sex_show_1_3
                    "... and pay no attention to the audience as they strip each other down."
                    wt_image intro_wife_weekend_normal_sex_show_1_4
                    "There's nothing unusual about their sex act ..."
                    wt_image intro_wife_weekend_normal_sex_show_1_5
                    "... it's a straight suck-and-fuck-fest ..."
                    wt_image intro_wife_weekend_normal_sex_show_1_6
                    "... but they both appear to cum, and they leave many in their audience ready to cum, too."
                    wt_image intro_wife_weekend_sex_show_10
                    "Because there's nothing in the act to think about except the sex, Ivy's able to relax and enjoy the show, and associated becoming turned on with spending time with you. She's now a little more romantically inclined towards you."
                else:
                    wt_image intro_wife_weekend_normal_sex_show_2_1
                    "A woman waits on stage for her partner to approach."
                    wt_image intro_wife_weekend_normal_sex_show_2_2
                    "There's no preamble to her greeting.  She simply pulls down his pants and takes his cock in her mouth."
                    wt_image intro_wife_weekend_normal_sex_show_2_3
                    "When he's fully hard, she sits up.  You can lip read her telling him to 'fuck me'."
                    wt_image intro_wife_weekend_normal_sex_show_2_4
                    "She lies down and he does ..."
                    wt_image intro_wife_weekend_normal_sex_show_2_5
                    "... banging her to a noisy orgasm as the crowd looks on."
                    wt_image intro_wife_weekend_normal_sex_show_2_6
                    "Now it's his turn.  She rolls him onto his back ..."
                    wt_image intro_wife_weekend_normal_sex_show_2_7
                    "... and begins jerking him off ..."
                    wt_image intro_wife_weekend_normal_sex_show_2_8
                    "... giving the crowd a good view as she pumps his load up into the air and onto his chest."
                    wt_image intro_wife_weekend_normal_sex_show_2_9
                    "An appreciative crowd applauds the performers and vice versa as they leave the stage."
                    wt_image intro_wife_weekend_sex_show_10
                    "It was bit animalistic and impersonal compared to the prior act, but that just left the focus even more on the pure sex.  Ivy's becoming even more inclined to associate you with sex."
                change ivy desire by 5
            "Sex show with a submissive woman" if not ivy.has_tag('watched_spanking_sex_show'):
                add tags 'watched_spanking_sex_show' to ivy
                wt_image intro_wife_weekend_submissive_sex_show_1_1
                "On one of the stages, a man is showing his partner a blindfold."
                wt_image intro_wife_weekend_submissive_sex_show_1_2
                "You guide Ivy over and you both watch as he blindfolds the woman, then beings to caress and undress her."
                wt_image intro_wife_weekend_submissive_sex_show_1_3
                "She can't see the handcuffs he produces next, but she can hear them ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_4
                "... and as he locks them into place, she can feel them binding her wrists."
                wt_image intro_wife_weekend_submissive_sex_show_1_5
                "He finishes undressing her ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_6
                "... then produces one more surprise, a bottle of oil that he drizzles across her most sensitive bits while she bites her lip."
                wt_image intro_wife_weekend_submissive_sex_show_1_7
                "She's panting heavily as he massages the oil into her skin ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_8
                "... then pushes her forward ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_9
                "... laying her on her belly with her bare bottom facing the audience."
                wt_image intro_wife_weekend_submissive_sex_show_1_10
                "Then he spanks her bare bottom to applause from the more dominant members of the audience - and likely some of the more submissive ones, too."
                wt_image intro_wife_weekend_submissive_sex_show_1_11
                "You assume the spanking's over when he pulls off her blindfold and rolls her onto her back ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_12
                "... but he tells her to watch and then lands a couple of more swats directly on her wet and swollen pussy lips ..."
                wt_image intro_wife_weekend_submissive_sex_show_1_13
                "... an experience that leads her to an intense, body-shaking orgasm."
                player.c "Looks like giving up control can be fun once in a while, wouldn't you say, Ivy?"
                wt_image intro_wife_weekend_sex_show_5
                ivy.c "I think I'd prefer to have my fun without the spanking."
                if ivy.spank_count > 0:
                    player.c "Maybe I just need to spank you between the legs, next time."
                    wt_image intro_wife_weekend_sex_show_6
                    ivy.c "No!  Don't you dare!!"
                    player.c "Why not?  Wouldn't you like to cum as intensely as she did?"
                else:
                    player.c "That's the fun part of giving up control.  You don't know what will be done with you - or how much you'll enjoy it."
                wt_image intro_wife_weekend_sex_show_9
                "She says nothing, but you know she's wondering how far you intend to push her - and how far she'll let you."
                change ivy submission by 5
            "Sex show with a deeply submissive woman" if ivy.has_tag('discussed_crawling') and not ivy.has_tag('watched_crawling_sex_show'):
                add tags 'watched_crawling_sex_show' to ivy
                wt_image intro_wife_weekend_submissive_sex_show_2_1
                "You spot a man leading a leashed woman onto a stage, and steer Ivy in that direction."
                wt_image intro_wife_weekend_sex_show_6
                ivy.c "I can't watch that!  Look how he's treating her."
                wt_image intro_wife_weekend_submissive_sex_show_2_2
                player.c "Like a prized possession?  What's wrong with that?  Looks like he's going to have her show off her assets."
                ivy.c "She's a woman, not a possession!"
                wt_image intro_wife_weekend_submissive_sex_show_2_3
                player.c "She's showing us clearly that she's definitely a woman.  What type of woman do you think she is?  Doctor?  Lawyer?  Maybe a teacher?"
                ivy.c "Right now she's just acting like a ..."
                wt_image intro_wife_weekend_submissive_sex_show_2_4
                ivy.c "OH!!"
                "Ivy gasps as the man places his hand on the back of his submissive's head and guides her onto all fours."
                wt_image intro_wife_weekend_sex_show_8
                player.c "What's wrong, Ivy?"
                ivy.c "She's ...  she's ...  she's not actually going to ... oh, she is!"
                wt_image intro_wife_weekend_submissive_sex_show_2_5
                player.c "Going to what?  Crawl for him?  It appears so."
                wt_image intro_wife_weekend_submissive_sex_show_2_6
                player.c "He's petting her, so he must be happy with her.  What do you think she's feeling right now, knowing that we've all watched her crawling to please him?"
                wt_image intro_wife_weekend_sex_show_9
                ivy.c "I ... I don't know what she's feeling."
                wt_image intro_wife_weekend_submissive_sex_show_2_7
                player.c "Looks like he's checking by going right to the source.  If she's wet between her legs from crawling, I bet she earns another reward beside being petted.  And she is."
                wt_image intro_wife_weekend_submissive_sex_show_2_8
                ivy.c "How is sucking his cock a reward for her?"
                player.c "She pleased him.  Now she gets to feel how much she pleased him."
                wt_image intro_wife_weekend_sex_show_10
                ivy.c "He must be a jerk to treat her that way."
                wt_image intro_wife_weekend_submissive_sex_show_2_9
                "Ivy seems completely unaware that she's rubbing her hard nipple as the woman on stage shows off to the audience the mouthful of jizz she earned from the 'jerk'."
                change ivy submission by 10
            "Sex show with a dominant woman" if not ivy.has_tag('watched_domme_show'):
                add tags 'watched_domme_show' to ivy
                wt_image intro_wife_weekend_domme_sex_show_1_1
                "You find a good spot right in front for Ivy to watch a Domme lead a naked man onto the stage on a leash."
                wt_image intro_wife_weekend_domme_sex_show_1_2
                ivy.c "Why is she doing that?"
                player.c "Doing what?  Spanking him, or making him lick her shoe?"
                ivy.c "Both.  What's the point?"
                player.c "To establish their relationship.  She's in charge.  He does what she tells him, and accepts her punishment whenever she wants to punish him."
                wt_image intro_wife_weekend_domme_sex_show_1_3
                ivy.c "What does he get out of this?  What does she get out of it, for that matter?"
                wt_image intro_wife_weekend_domme_sex_show_1_4
                player.c "He gets to please her, and to experience whatever pleasure she decides to give him, if any.  She gets to enjoy his body, and to enjoy having the power to please him or not, at her discretion.  Right now, it seems she's not happy with the state of his erection.  No pleasure for him right now."
                wt_image intro_wife_weekend_domme_sex_show_1_5
                ivy.c "Now what's she's doing??"
                wt_image intro_wife_weekend_domme_sex_show_1_6
                player.c "It's fairly obvious, isn't it?  She wasn't happy with the state of his erection, so she's reminding him of his role by getting him to lick something more intimate than her shoe."
                wt_image intro_wife_weekend_domme_sex_show_1_7
                ivy.c "Is that part of putting him in his place, too?"
                wt_image intro_wife_weekend_domme_sex_show_1_8
                player.c "I don't think so.  I think she just wanted him to eat her out.  The nice thing about taking control of a man is you get to cum on the end of his tongue whenever the mood strikes you."
                wt_image intro_wife_weekend_domme_sex_show_1_9
                player.c "She seems happier with the state of his erection, now.  Do you think she'll let him cum?"
                wt_image intro_wife_weekend_sex_show_9
                ivy.c "Well, yeah.  I mean, he just got her off."
                player.c "So?  Maybe she wants to leave him horny so he'll be hard when she decides to ride him later tonight?"
                wt_image intro_wife_weekend_sex_show_7
                ivy.c "Well, this is a sex show, so I'm sure she's going to let the audience see him ejaculate, but I can see the appeal in having him ready to ride when she's ready for another orgasm."
                "Ivy's so lost in her thoughts she almost misses the Domme ending the show exactly as Ivy predicted, with her sub's seed splattering the stage floor in front of him."
                change ivy desire by 5
                change ivy resistance by -5
                $ ivy.domme_comfort += 1
            "Sex show with acrobatic performers" if not ivy.has_tag('watched_acrobatic_sex_show'):
                add tags 'watched_acrobatic_sex_show' to ivy
                wt_image intro_wife_weekend_acrobatic_sex_show_1_1
                "A large crowd has gather around one of the stages."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_2
                "There's nothing unusual about the start of their show ..."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_3
                "... until the man grasps his partner around the waist ..."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_4
                "... and flips her into the air."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_5
                "The two of them fellate each other ..."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_6
                "... as he spins her around on the stage."
                wt_image intro_wife_weekend_sex_show_6
                ivy.c "What the fuck?  that looks dangerous."
                player.c "Fun, though."
                ivy.c "Fun if you don't get dropped on your head."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_7
                "Eventually he deposits her back on the couch ..."
                wt_image intro_wife_weekend_acrobatic_sex_show_1_8
                "... and fucks them both to orgasm as the crowd watches."
                wt_image intro_wife_weekend_sex_show_7
                ivy.c "Well, that was interesting, I guess.  I prefer my foreplay without the threat of head injury, though.  Still, it's interesting to see what some people can do with their bodies."
                player.c "Does it make you wonder what else you might be able to do with your body?"
                ivy.c "Maybe a little."
                "She'll be more open to new ideas, now.  Especially those involving unusual sex positions."
                change ivy resistance by -5
        notify
        call character_location_return(ivy) from _call_character_location_return_655
        call forced_movement(living_room) from _call_forced_movement_955
        end_day
    return

label ivy_weekend_date:
    rem tags 'checking_for_weekend' from ivy
    call forced_movement(outdoors) from _call_forced_movement_956
    summon ivy
    if ivy.submission > 0 and ivy.ordered_food_for_her_count == 0:
        wt_image intro_wife_weekend_restaurant_1_1
        "You bring Ivy to a nice restaurant.  It'll give the two of you a chance to chat over your meal."
        $ title = "Do you want to order for her?"
        menu:
            "Yes, it will set the right mood":
                $ ivy.ordered_food_for_her_count = 1
            "No, it might interfere with your conversation":
                pass
    elif ivy.ordered_food_for_her_count == 1:
        $ ivy.ordered_food_for_her_count += 1
        wt_image intro_wife_weekend_restaurant_1_1
        "Ivy sits quietly as you order her meal and yours.  You can see that being treated this way is still affecting her, but today it doesn't prevent the two of you from having a conversation while you eat."
        change ivy submission by 5
    elif ivy.ordered_food_for_her_count > 1:
        $ ivy.ordered_food_for_her_count += 1
        wt_image intro_wife_weekend_restaurant_1_1
        "Ivy sits quietly as you order her meal and yours.  She's become used to this treatment, and it's no longer shaping her thinking, although it does put her in a subservient mood for your conversation."
    else:
        wt_image intro_wife_weekend_restaurant_1_2
        "You bring Ivy to a nice restaurant.  It'll give the two of you a chance to chat over your meal."
    # obedience conversation if first time ordering for for her
    if ivy.ordered_food_for_her_count == 1:
        wt_image intro_wife_weekend_restaurant_1_10
        ivy.c "You're ordering for me?"
        player.c "Do you have any food allergies?"
        ivy.c "No, but ..."
        player.c "Then yes, I'm ordering for you."
        ivy.c "Why?  I can pick out what I want."
        player.c "You'll enjoy what I ordered for you.  And I enjoy making the decision for you."
        wt_image intro_wife_weekend_restaurant_1_1
        ivy.c "That doesn't make any sense.  Why would you care what I eat?  I could understand you telling me what you want me to get you, but wouldn't you prefer that I get what I want, too?"
        player.c "Obedience isn't just about you letting your man take you in his favorite position.  It's about a voluntary transfer of power.  It's about letting him decide not only what he gets, but what you get, too."
        ivy.c "That seems very one-sided."
        player.c "Is your meal good?"
        wt_image intro_wife_weekend_restaurant_1_8
        ivy.c "Yes, but ..."
        player.c "No 'buts'.  Yes, you're enjoying the meal I ordered you.  Giving up control is a matter of trust.  Trust that he'll use that control to make the experience a good one for both of you."
        ivy.c "Why should I trust you to order what I want, when I could just say what I want?"
        player.c "Because maybe you find you enjoy what I ordered more than what you thought you wanted.  Because maybe it's nice just to relax and not have to decide.  But mostly because maybe you enjoy how it feels to give up control and trust another to decide what you experience."
        wt_image intro_wife_weekend_restaurant_1_5
        "Ivy chews quietly for the rest of the meal, lost in her own thoughts.  She doesn't speak again until your plates are empty."
        wt_image intro_wife_weekend_restaurant_1_1
        ivy.c "I don't want to be subservient to my husband."
        player.c "I know.  But it would spice up your sex life.  And it's an easy form of foreplay, giving up control in public in anticipation of giving up control in the bedroom when you get home."
        "She doesn't answer you, but you've given her a lot to think about."
        change ivy submission by 5
    # else normal conversation choices
    else:
        $ title = "How do you steer the conversation?"
        menu:
            "Towards getting to know her better":
                $ title = "What would you like to talk to her about?"
                menu:
                    "Her fantasies" if not ivy.has_tag('discussed_stripping'):
                        player.c "Tell me about yourself, Ivy.  What do you enjoy, sexually?"
                        ivy.c "Lots of things.  I love being with my husband.  I love that he lets me be with other men without getting jealous."
                        player.c "And what sort of things do you do with your husband and these other men?"
                        if ivy.test('resistance', 70):
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "I'm not sure ladies are supposed to talk about that sort of thing."
                            wt_image intro_wife_weekend_restaurant_1_3
                            ivy.c "But I guess it's all right, since you're here to help.  I love to 'suck and fuck', if you'll excuse my vernacular."
                            player.c "And what do you do to spice things up, while you're sucking and fucking?"
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "Well, I do enjoy teasing.  It's fun to get a guy excited. I enjoy that a lot.  I wish ..."
                            player.c "You wish what?"
                            add tags 'discussed_stripping' to ivy
                            wt_image intro_wife_weekend_restaurant_1_3
                            ivy.c "This is going to sound stupid, but I love the idea of turning a guy on using just my body, without even touching him.  The idea that just looking at me would get him hard is really hot."
                            player.c "Have you ever given your husband a strip tease?"
                            ivy.c "No!  Never. I wouldn't ... I couldn't ..."
                            player.c "Why not?"
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "Because I'd look stupid.  I'm his wife.  He's seen my body a million times, and it's not what it used to be.  I'm not some hot bodied college student dancing her way through school.  I'd just look ridiculous."
                            sys "This opened up new opportunities to train her."
                        elif ivy.test('resistance', 75) or ivy.test('desire', 10):
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "I'm not sure ladies are supposed to talk about that sort of thing."
                            wt_image intro_wife_weekend_restaurant_1_3
                            ivy.c "But I guess it's all right, since you're here to help.  I love to 'suck and fuck', if you'll excuse my vernacular."
                            player.c "And what do you do to spice things up, while you're sucking and fucking?"
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "Well, I do enjoy teasing.  It's fun to get a guy excited. I enjoy that a lot.  I wish ..."
                            player.c "You wish what?"
                            wt_image intro_wife_weekend_restaurant_1_6
                            ivy.c "Nothing.  That's all."
                            sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                        else:
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "I'm not sure ladies are supposed to talk about that sort of thing.  And besides, I hardly know you."
                    "Her husband's fantasies" if not ivy.has_tag('discussed_anal'):
                        player.c "Tell me about your husband, Ivy.  What does he enjoy, sexually?"
                        ivy.c "Lots of things.  He loves being with me.  He also loves being with other women, and loves that I let him do so without getting jealous."
                        player.c "And what does he do with these other women that he doesn't do with you?"
                        if ivy.test('resistance', 65):
                            wt_image intro_wife_weekend_restaurant_1_7
                            ivy.c "My husband isn't sleeping with other women because I can't satisfy him.  He just likes variety, as do I."
                            player.c "I'm sure he does.  And I'm sure some of those women enjoy doing things that you don't.  Does your husband talk to you about what sort of sex he has with his other partners."
                            ivy.c "Yes, we both shares notes after we've been with someone else.  And usually we fuck like bunnies after we do."
                            player.c "And when he shares notes, is there anything you've noticed that he seems to particularly enjoy doing with other women that he doesn't do with you?"
                            add tags 'discussed_anal' to ivy
                            wt_image intro_wife_weekend_restaurant_1_8
                            ivy.c "Well ... I mean ... I guess he does always sound extra excited after he's been with a woman who lets him put it up her butt.  Like a kid who found some candy."
                            player.c "You don't enjoy anal sex?"
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "I'm not even sure.  We tried a few times, back when we were first going out together and it ... well, it didn't go well."
                            player.c "Why not?"
                            ivy.c "The first time I panicked, and he felt bad for asking.  Then we tried again, but it felt weird to me and he could tell, so he suggested we do things normally instead, so I agreed."
                            wt_image intro_wife_weekend_restaurant_1_6
                            ivy.c "I knew he wanted this, so later I suggested we try again and we did try, but I was so nervous, he could only get himself partway inside me before I tensed up.  Again he tried to make me feel better by suggesting I jerk him off instead, and he told me anal wasn't important to him."
                            player.c "Is it important to him?"
                            wt_image intro_wife_weekend_restaurant_1_5
                            ivy.c "I don't think so.  I'm sure he enjoys the sex we do have.  But I do get a little jealous when he tells me about his anal conquests, and ..."
                            player.c "You know it would make him happy if he conquered your ass, too?"
                            "She just nods."
                            sys "This opened up new opportunities to train her."
                        elif ivy.test('resistance', 75):
                            wt_image intro_wife_weekend_restaurant_1_7
                            ivy.c "My husband isn't sleeping with other women because I can't satisfy him.  He just likes variety, as do I."
                            player.c "I'm sure he does.  And I'm sure some of those women enjoy doing things that you don't.  Does your husband talk to you about what sort of sex he has with his other partners."
                            ivy.c "Yes, we both shares notes after we've been with someone else.  And usually we fuck like bunnies after we do."
                            player.c "And when he shares notes, is there anything you've noticed that he seems to particularly enjoy doing with other women that he doesn't do with you?"
                            wt_image intro_wife_weekend_restaurant_1_6
                            ivy.c "Well ... I mean ....  No, not really.  Nothing comes to mind."
                            sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                        else:
                            wt_image intro_wife_weekend_restaurant_1_7
                            ivy.c "I can satisfy my husband quite nicely, thank you.  He's not sleeping with other women to get something I can't give him.  He just likes variety, as do I.  I'm very good for him."
                            "She's too defensive to get anywhere on this topic until she trusts you more. This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                    "Obedience" if not ivy.has_tag('discussed_crawling'):
                        player.c "Do you obey your husband, Ivy?"
                        ivy.c "That's not the type of relationship we have.  We're equal partners.  Neither of us obeys the other."
                        player.c "Doesn't he ever boss you around?"
                        ivy.c "No.  Never.  He's a perfect gentleman.  That's part of what I love about him."
                        player.c "What about in bed?  Does he ever take charge, sexually?"
                        wt_image intro_wife_weekend_restaurant_1_5
                        ivy.c "No.  He's not that type.  He's always very polite and considerate.  Sometimes ..."
                        player.c "Sometimes too considerate?"
                        wt_image intro_wife_weekend_restaurant_1_2
                        ivy.c "I didn't say that.  I like the way my husband makes love to me."
                        player.c "And what about your other partners.  Do they all make love to you gently?  Or do some of them expect you to obey them?"
                        if ivy.test('resistance', 75) or ivy.test('submission', 10):
                            ivy.c "I guess some of them have enjoyed taking charge."
                            player.c "Did you enjoy that?"
                            ivy.c "Not when they got rough."
                            player.c "What about when they told you what they wanted you to do?"
                            ivy.c "Sometimes ... sometimes that was okay."
                            player.c "What have you been ordered to do that turned you on the most?"
                            if ivy.test('resistance', 60):
                                add tags 'discussed_crawling' to ivy
                                wt_image intro_wife_visit_1_12
                                wt_image intro_wife_weekend_restaurant_1_5
                                ivy.c "There's ... Well ... This didn't turn me on, but something that did stick with me once was ..."
                                player.c "Spit it out."
                                wt_image intro_wife_weekend_restaurant_1_6
                                ivy.c "A guy once told me to crawl over to him if I wanted his cock."
                                player.c "And did you?"
                                wt_image intro_wife_weekend_restaurant_1_7
                                ivy.c "NO!  Of course, not.  I was repulsed.  I told him he had a huge ego."
                                player.c "What did he say?"
                                ivy.c "He said he also had a huge cock, but I needed to get down on all fours if I wanted to see it.  I laughed at him, of course, and left.  I'm not the crawling type."
                                player.c "Not even for your husband?"
                                wt_image intro_wife_weekend_restaurant_1_8
                                ivy.c "My husband wouldn't want me to crawl to him."
                                sys "Maybe not, but maybe some part of her would like to crawl for him.  This opened up new opportunities to train her."
                            else:
                                wt_image intro_wife_weekend_restaurant_1_6
                                ivy.c "There's ... Well ... Nothing really.  It's nice to know what the guy wants, of course.  That's all."
                                sys "There's more she wants to tell you, but isn't ready to yet.  This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                        else:
                            wt_image intro_wife_weekend_restaurant_1_7
                            ivy.c "I am NOT a submissive woman.  I don't seek out partners who are into that sort of thing."
                            "She's too defensive to get anywhere on this topic until she trusts you more. This is related to her Resistance stat, which you could lower by spending the rest of the evening talking to her."
                    "Taking charge" if not ivy.has_tag('discussed_taking_charge'):
                        add tags 'discussed_taking_charge' to ivy
                        player.c "Does your husband do what you tell him, Ivy?"
                        wt_image intro_wife_weekend_restaurant_1_7
                        ivy.c "What?  No.  That's not the type of relationship we have.  We're equal partners."
                        player.c "What about in bed?  Do you ever take charge, sexually?"
                        wt_image intro_wife_weekend_restaurant_1_2
                        ivy.c "Should I?"
                        player.c "You tell me.  Do you ever direct his actions in bed?  Show him what you want him to do?"
                        wt_image intro_wife_weekend_restaurant_1_5
                        ivy.c "Well ... I mean ... sometimes when ... you know."
                        player.c "When his mouth is between your legs?  Do you show him how you like to be licked?"
                        wt_image intro_wife_weekend_restaurant_1_6
                        ivy.c "Sometimes"
                        player.c "And how does he react?"
                        ivy.c "Well, like any husband would, I think.  He wants me to enjoy myself."
                        player.c "So you wrap your fingers in his hair and direct his tongue to where you want it?"
                        wt_image intro_wife_weekend_restaurant_1_8
                        ivy.c "Not in a mean way."
                        player.c "There's nothing mean about showing a man how you want him to please you.  Your husband enjoys pleasing you, doesn't he?"
                        ivy.c "He's not submissive, if that's what you're suggesting."
                        player.c "Are you sure?  Have you tried dominating him?"
                        wt_image intro_wife_weekend_restaurant_1_6
                        ivy.c "No ... I mean, wouldn't he have asked if that's what he wanted?"
                        player.c "Maybe not.  When you agreed to come here to be trained, did you ask your husband how he wanted you to be trained?"
                        ivy.c "No ... he just wanted ..."
                        player.c "You didn't actually ask what he wanted.  Once he was onside with the idea, you ran with it.  Who suggested that your marriage be an open one?"
                        ivy.c "We both discussed it."
                        player.c "After you suggested it."
                        wt_image intro_wife_weekend_restaurant_1_8
                        ivy.c "Yes, but he's happy about it."
                        player.c "I'm sure he is. I think he's always happy when you take charge of your sexual adventures.  I bet he'd like it if you did it more often."
                        wt_image intro_wife_weekend_restaurant_1_5
                        ivy.c "I'm not sure I want to take charge of him, sexually."
                        sys "She may not be sure about herself, but she seems sure he'd let her if she was.  This opened up new opportunities to train her."
                    "Nothing in particular":
                        pass
                wt_image intro_wife_weekend_restaurant_1_9
                "You spend the rest of the meal chatting with her and getting to know her better.  By the end, she's come to trust you more."
                change ivy resistance by -5
            "Towards flirting with her":
                wt_image intro_wife_weekend_restaurant_1_3
                "Your efforts aren't subtle, but they don't have to be.  Ivy's flattered by your attention and efforts to charm her."
                wt_image intro_wife_weekend_restaurant_1_4
                ivy.c "Thank you for this.  I had fun."
                "Ivy's now more romantically inclined towards you."
                change ivy desire by 5
    notify
    call character_location_return(ivy) from _call_character_location_return_656
    call forced_movement(living_room) from _call_forced_movement_957
    end_day
    return


## Post-Training Character Actions

# Watch Her Dance - Showgirl content on stage
label ivy_watch_her_dance:
    #$ ivy.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ ivy.showgirl_outfit += 1
    if ivy.showgirl_outfit > 4:
        $ ivy.showgirl_outfit = 1
    if ivy.showgirl_outfit == 1:
        if not ivy.has_tag('first_stage_strip'):
            wt_image intro_wife_strip_outfit_1_2
            "You're not sure if the 'cupcakes' motif is just supposed to represent that's she's a married woman, but Ivy steps out on stage wearing a full length apron ..."
            wt_image intro_wife_strip_outfit_1_3
            "... which covers a blue skirt that is decidedly not full length."
            wt_image intro_wife_strip_outfit_1_4
            "Ivy appears to have a touch of stage fright as she unties her apron strings ..."
            wt_image intro_wife_strip_outfit_1_5
            "... but she gamely pulls it down."
            wt_image intro_wife_strip_outfit_1_6
            "She's still fully dressed under the apron ..."
            wt_image intro_wife_strip_outfit_1_7
            "... and you're worried she may not be brave enough to continue."
            wt_image intro_wife_strip_outfit_1_8
            "But she gathers the courage needed to turn around ..."
            wt_image intro_wife_strip_outfit_1_9
            "... flashing her butt cheeks again as she does so."
            wt_image intro_wife_strip_outfit_1_10
            "And when she returns to face the audience, she grasps the hem of her skirt ..."
            wt_image intro_wife_strip_outfit_1_11
            "... and slowly pulls it up."
            wt_image intro_wife_strip_outfit_1_12
            "She still hasn't shown anything, but she has the crowd's attention, and they're patient with her ..."
            wt_image intro_wife_strip_outfit_1_13
            "... and wait for her to gather her courage again."
            wt_image intro_wife_strip_outfit_1_14
            "When she does, she does another turn ..."
            wt_image intro_wife_strip_outfit_1_15
            "... and pulls off her top."
            wt_image intro_wife_strip_outfit_1_16
            "She still isn't really showing anything, and some cads in the audience are getting restless.  Fortunately there are enough women watching the show - plus enough men enjoying the awkwardness of her nervous strip - to shush the others and provide Ivy with positive encouragement."
            wt_image intro_wife_strip_outfit_1_17
            "Ivy finally loses the skirt ..."
            wt_image intro_wife_strip_outfit_1_18
            "... completes another turn ..."
            wt_image intro_wife_strip_outfit_1_19
            "... and unsnaps her bra."
            wt_image intro_wife_strip_outfit_1_20
            "As the crowd calls our encouragement, Ivy slowly lets the bra fall ..."
            wt_image intro_wife_strip_outfit_1_21
            "... and bare her breasts for the arousal of strangers for the first time."
            wt_image intro_wife_strip_outfit_1_22
            "Just one thing left to do."
            wt_image intro_wife_strip_outfit_1_23
            "Encouraged by the applause from onlookers, Ivy pulls down her panties ..."
            wt_image intro_wife_strip_outfit_1_24
            "... strikes a naked pose ..."
            wt_image current_location.image
            "... then pretty much bolts from the stage."
            wt_image intro_wife_strip_outfit_1_1
            "A few minutes later, now fully re-dressed except for the apron, she rushes up to you."
            ivy.c "Did you see me??  I did it!  It wasn't much of a show, even with the props I set up, but I took my clothes off up there AND some of the men were getting excited watching me, too!"
            player.c "I dare say all of the men were, and some of the women, as well."
            ivy.c "I'm not sure I'd go that far, but I turned some of the men on, I know I did, and that feels so good!"
            "There's a pretty good chance Ivy will give more shows in the future, if you care to drop by and watch them.  That's it for today, though."
        else:
            wt_image intro_wife_strip_outfit_1_2
            "Ivy trots back onto stage, wearing her apron again."
            wt_image intro_wife_strip_outfit_1_3
            "She's still wearing the short blue skirt under the apron ..."
            wt_image intro_wife_strip_outfit_1_4
            "... but there's no hesitation today as she unties the apron strings ..."
            wt_image intro_wife_strip_outfit_1_25
            "... and slips out of housewife mode."
            wt_image intro_wife_strip_outfit_1_9
            "She does a little turn ..."
            wt_image intro_wife_strip_outfit_1_10
            "... then grabs the front of her skirt ..."
            wt_image intro_wife_strip_outfit_1_26
            "... and seductively pulls it up."
            wt_image intro_wife_strip_outfit_1_14
            "After another little turn ..."
            wt_image intro_wife_strip_outfit_1_15
            "... she loses her top ..."
            wt_image intro_wife_strip_outfit_1_27
            "... and her skirt."
            wt_image intro_wife_strip_outfit_1_28
            "Neither the bra ..."
            wt_image intro_wife_strip_outfit_1_23
            "... nor the panties ..."
            wt_image intro_wife_strip_outfit_1_29
            "... last much longer, either."
            wt_image intro_wife_strip_outfit_1_30
            "After one more turn ..."
            wt_image intro_wife_strip_outfit_1_24
            "... she strikes a pose ..."
            if ivy.crawl_count > 0:
                wt_image intro_wife_strip_outfit_1_32
                ".. then with just the slightest tremble to betray her nervousness, she drops down to the stage floor ..."
                wt_image intro_wife_strip_outfit_1_33
                "... gets on all fours ..."
                wt_image intro_wife_strip_outfit_1_34
                "... and crawls off the stage, to the disapproval of some members of the audience, and the amusement of many more."
            else:
                wt_image intro_wife_strip_outfit_1_31
                "... then slowly exits the stage, with a noticeable wiggle to her bum as she exits."
        add tags 'first_stage_strip' to ivy
    elif ivy.showgirl_outfit == 2:
        wt_image intro_wife_strip_outfit_2_2
        "Ivy steps on to the stage wearing a white dress ..."
        wt_image intro_wife_strip_outfit_2_3
        "... and begins to dance ..."
        wt_image intro_wife_strip_outfit_2_4
        "... but she seems to prefer dancing in her underwear, as she loses the dress on her first spin around the pole."
        wt_image intro_wife_strip_outfit_2_5
        "Dancing like a 'real' stripper is clearly turning Ivy on."
        if not ivy.has_tag('second_stage_strip') or ivy.domme_comfort < 3:
            wt_image intro_wife_strip_outfit_2_6
            "She removes her bra ..."
            if ivy.crawl_count > 0:
                wt_image intro_wife_strip_outfit_2_7
                "... crawls around on stage ..."
            wt_image intro_wife_strip_outfit_2_8
            "... then rolls onto her back ..."
            wt_image intro_wife_strip_outfit_2_9
            "... and removes her panties, too."
            if ivy.crawl_count > 0:
                wt_image intro_wife_strip_outfit_2_10
                "Now completely naked, she crawls back to the pole ..."
            else:
                wt_image intro_wife_strip_outfit_2_11
                "Now completely naked, she sneaks a peek at the audience before turning back to the pole ..."
            wt_image intro_wife_strip_outfit_2_12
            "... where she resumes her dance, only now naked and on her knees."
            wt_image intro_wife_strip_outfit_2_13
            "She enjoys herself at least as much this way ..."
            wt_image intro_wife_strip_outfit_2_14
            "... as she makes quite clear to her audience."
            wt_image intro_wife_strip_outfit_2_15
            "When the music stops, Ivy stares out at the crowd, as if shocked by the lewdness of her display.  She makes no attempt to cover herself up, however, until their applause ends."
        else:
            wt_image intro_wife_strip_outfit_2_16
            "You encouraged her to take charge, and she does, reaching out to a member of the audience ..."
            wt_image intro_wife_strip_outfit_2_17
            "... and convincing him to join her act."
            wt_image intro_wife_strip_outfit_2_18
            "Performers at the Club don't normally turn their dances into sex shows ..."
            wt_image intro_wife_strip_outfit_2_19
            ".. but there's nothing specific in the rules to say they can't, and nobody in the audience complains ..."
            if ivy.has_tag('had_adventurous_sex'):
                wt_image intro_wife_strip_outfit_2_20
                "... as Ivy teaches the audience member how to fuck her in a Kama Sutra-like position that may or may not be safe to try at home."
            else:
                wt_image intro_wife_strip_outfit_2_21
                "... as Ivy relieves her sexual tension with the help of her audience member's hard tool."
        add tags 'second_stage_strip' to ivy
    elif ivy.showgirl_outfit == 3:
        wt_image intro_wife_strip_outfit_3_2
        "Ivy's arranged a surprisingly elaborate light show for her dance."
        wt_image intro_wife_strip_outfit_3_3
        "She even arranged for bubbles."
        wt_image intro_wife_strip_outfit_3_4
        "It's not all that easy to see her as she starts dancing ..."
        wt_image intro_wife_strip_outfit_3_5
        "... although maybe that's on purpose ..."
        wt_image intro_wife_strip_outfit_3_6
        "... as today's show is light on stripping ..."
        wt_image intro_wife_strip_outfit_3_7
        "... and heavy on tease."
        if ivy.has_tag('third_stage_strip') and ivy.domme_comfort > 2:
            wt_image intro_wife_strip_outfit_3_14
            "Even the audience member Ivy picks out of the crowd to join her on stage ..."
            wt_image intro_wife_strip_outfit_3_15
            "... gets only a teasing lap dance, not a fuck ..."
            wt_image intro_wife_strip_outfit_3_16
            "... while some of the more generous Club patrons shower them with signs of their appreciation."
        elif ivy.crawl_count > 0:
            wt_image intro_wife_strip_outfit_3_8
            "There's some floor work, too ..."
            wt_image intro_wife_strip_outfit_3_9
            "... as Ivy drops to her knees and crawls seductively ..."
            wt_image intro_wife_strip_outfit_3_10
            "... while some of the more generous Club patrons shower her signs of their appreciation."
        else:
            wt_image intro_wife_strip_outfit_3_11
            "There's some floor work, too ..."
            wt_image intro_wife_strip_outfit_3_12
            "... as Ivy drops onto her back and rolls around seductively ..."
            wt_image intro_wife_strip_outfit_3_13
            "... while some of the more generous Club patrons shower her signs of their appreciation."
        wt_image intro_wife_strip_outfit_3_17
        "And then Ivy's gone, lost in her own thoughts as she slips away.  It seems anyone hoping for a better view of her body will need to wait for another show."
        add tags 'third_stage_strip' to ivy # NOTE: must be at end of show re test for this tag above
    else:
        wt_image intro_wife_strip_outfit_4_2
        "Ivy opens her show seating on a stool."
        if ivy.has_tag('fourth_stage_strip') and ivy.has_tag('bought_strap_on'):
            wt_image intro_wife_strip_outfit_4_14
            "Then she beckons for another woman to join her on stage."
            wt_image intro_wife_strip_outfit_4_15
            "Ivy quickly establishes who's the star of this show and who's the supporting actress."
            wt_image intro_wife_strip_outfit_4_16
            "That she puts the other woman on her knees is a small surprise ..."
            wt_image intro_wife_strip_outfit_4_17
            "... that she then produces her strap-on for the blonde to suck on is a much bigger surprise."
            if ivy.has_tag('likes_girls'):
                wt_image intro_wife_strip_outfit_4_20
                "That Ivy should combine her recently discovered interest in women, domination and showmanship is a testament to how comfortable she's become with her own sexuality."
                wt_image intro_wife_strip_outfit_4_21
                "She uses her sexuality - and the strap-on - to make sure the other woman is more than just comfortable ..."
                wt_image intro_wife_strip_outfit_4_22
                "... before allowing herself to fully enjoy it herself."
                wt_image intro_wife_strip_outfit_4_23
                "The applause from the audience indicates it wasn't just the performers who enjoyed themselves."
            else:
                wt_image intro_wife_strip_outfit_4_18
                "As far as you know, Ivy is only into boys.  So the fucking she gives the other woman is presumably just another way of amusing herself by turning on the men who are watching ..."
                wt_image intro_wife_strip_outfit_4_19
                "... although the blonde also clearly enjoys the fucking intensely."
                wt_image intro_wife_strip_outfit_4_17
                "And if Ivy doesn't get at least a little turned on watching the blonde woman lick her own juices off the strap-on, she at least gets turned on hearing how much the audience enjoyed the display."
        else:
            wt_image intro_wife_strip_outfit_4_3
            "Still seated, she slowly turns around ..."
            wt_image intro_wife_strip_outfit_4_4
            "... all the way round ..."
            wt_image intro_wife_strip_outfit_4_5
            "... and unfastens her top."
            wt_image intro_wife_strip_outfit_4_6
            "With a glazy, lustful look, she leans over ..."
            wt_image intro_wife_strip_outfit_4_7
            "... and lewdly displays her attributes."
            wt_image intro_wife_strip_outfit_4_8
            "Still bent over, she pulls down the bottom half of her outfit ..."
            wt_image intro_wife_strip_outfit_4_9
            "... then resumes turning and posing."
            wt_image intro_wife_strip_outfit_4_10
            "Is she on a pedestal?"
            wt_image intro_wife_strip_outfit_4_11
            "Are all women?"
            wt_image intro_wife_strip_outfit_4_12
            "Or does she just enjoy teasing men with the sight of her body?"
            wt_image intro_wife_strip_outfit_4_13
            "Whatever her message, if she's even intending to send one, she ends her show as still as a statue, as if she were artwork.  Very sexy artwork."
        add tags 'fourth_stage_strip' to ivy
    add tags 'watched_today' to ivy
    change player energy by -energy_very_short
    wt_image current_location.image
    return

# Crawl visit content
label ivy_crawl_visit:
    $ ivy.training_session()
    wt_image intro_wife_visit_2_1
    ivy.c "Look, I know I came over here, but I don't think this is a good idea.  I don't mind crawling for my husband from time to time to turn him on, but I'm really not in the mood to be humiliated right now."
    player.c "That's the fun thing about humiliation.  It happens on my terms, not yours.  You've been thinking about being down on all fours your whole drive over here."
    wt_image intro_wife_visit_2_2
    ivy.c "Yes, but that's not what I want right now.  You shouldn't feel like you can just call me up and I'll come running over here to humiliate myself for your enjoyment.  What do you even think of me to expect that of me?"
    player.c "A better question is what do you think of yourself"
    wt_image intro_wife_visit_2_35
    ivy.c "I don't know.  Pathetic, I guess?  I'm a modern, liberated woman most of the time, and then you treat me like something else, and my insides turn to goo."
    player.c "I treat you like 'something else'?  Like what, exactly?  Like a dumb cunt whose place is down on the floor?"
    wt_image intro_wife_visit_2_2
    ivy.c "Oh, wow!!  See, that's exactly what I mean.  I want to slap you right now."
    player.c "You also want to get down on the floor, where you belong."
    wt_image intro_wife_visit_2_1
    ivy.c "I don't really want to do that. It's just ..."
    player.c "It's just your insides have turned to goo, and the modern, liberated feminist is getting ready to turn into a dumb animal for my amusement."
    "She's having trouble breathing, so can't respond.  She just nods, instead."
    $ title = "How do you want her to crawl for you?"
    menu:
        "Put her tail in" if ivy.has_tag('crawled_wearing_tail'):
            player.c "Go change into your fishnets while I get your tail ready, bitch."
            wt_image intro_wife_lingerie_2_2
            "She changes quickly ..."
            wt_image intro_wife_lingerie_2_20
            "... and gets into position."
            wt_image intro_wife_lingerie_2_15
            ivy.c "I still can't believe how much this turns me on."
            wt_image intro_wife_lingerie_2_18
            player.c "Stop talking and stop playing with your tail, you stupid bitch.  Get off the sofa and on the floor where you belong."
            wt_image intro_wife_lingerie_2_44
            player.c "Eager to run?"
            ivy.c "Yes"
            wt_image intro_wife_lingerie_2_42
            player.c "No talking.  Women talk.  A dumb bitch like you barks if she wants to communicate."
            if not ivy.has_tag('barked'):
                ivy.c "But I couldn't ..."
                wt_image intro_wife_lingerie_2_43
                "*SMACK*"
                ivy.c "OW!"
                player.c "You heard me.  Are you eager to run, bitch?"
                add tags 'barked' to ivy
            wt_image intro_wife_lingerie_2_44
            ivy.c "Woof"
            player.c "I don't believe you.  Make me believe you."
            wt_image intro_wife_lingerie_2_52
            ivy.c "WOOF ... WOOF ... WOOF"
            player.c "Good girl, off you go."
            wt_image intro_wife_lingerie_2_45
            "She takes off running as fast as she can on all fours ..."
            wt_image intro_wife_lingerie_2_47
            "... running around in circles like before ..."
            wt_image intro_wife_lingerie_2_48
            "... fully embracing the humiliation of being treated like an animal."
            wt_image intro_wife_lingerie_2_53
            "You let her enjoy her time spent humiliating herself ..."
            wt_image intro_wife_lingerie_2_51
            "... until she starts to tire out."
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_lingerie_2_52
                    player.c "Just one more lap, girl, then it's time to go home."
                    ivy.c "WOOF"
                    wt_image intro_wife_lingerie_2_47
                    "You're not sure what the bark meant, but she fairly sprints around the room for her final lap, before heading home and leaving you to get on with your day."
                    change player energy by -energy_very_short
                "Tell her to suck your cock":
                    wt_image intro_wife_lingerie_2_52
                    player.c "That's enough laps, girl.  Come over here and beg for the taste of my cock."
                    wt_image intro_wife_lingerie_2_25
                    ivy.c "woof?"
                    player.c "Crawl closer."
                    wt_image intro_wife_lingerie_2_31
                    ivy.c "woof?"
                    player.c "Now beg using human words."
                    ivy.c "This stupid bitch would like your thick cock in her mouth."
                    player.c "Will you do a good job for me?"
                    if ivy.has_tag('bj_training'):
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                        else:
                            ivy.c "Yes.  I may be a dumb bitch, but I'm a well-trained cocksucker."
                    else:
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb bitch, but I know how to suck dick, Sir."
                        else:
                            ivy.c "I may be a dumb bitch, but I know how to suck dick."
                    call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets_4
                    "She goes to change and heads home, leaving you to get on with your day."
        "Have her wear her fishnets" if ivy.has_tag('crawled_as_slut'):
            player.c "Go change into your fishnets, slut.  You're going to crawl to me wearing them."
            wt_image intro_wife_lingerie_2_2
            "She changes quickly ..."
            wt_image intro_wife_lingerie_2_6
            "... and approaches."
            player.c "Did you miss the part where I said you're to crawl to me, you stupid slut?"
            wt_image intro_wife_lingerie_2_23
            ivy.c "I didn't know where you wanted me to start."
            player.c "What should a stupid slut like you do if she's not sure?"
            wt_image intro_wife_lingerie_2_24
            ivy.c "Get on my knees?"
            wt_image intro_wife_lingerie_2_25
            player.c "That's the best place for you, isn't it?"
            wt_image intro_wife_lingerie_2_28
            ivy.c "Yes"
            player.c "Yes, what?"
            wt_image intro_wife_lingerie_2_29
            ivy.c "Yes, this stupid slut should be made to crawl on her knees."
            wt_image intro_wife_lingerie_2_27
            player.c "Keep going, slut.  You don't mind spending the whole evening crawling, do you?"
            wt_image intro_wife_lingerie_2_26
            ivy.c "No, Sir.  This stupid slut is happy to crawl for your amusement."
            wt_image intro_wife_lingerie_2_28
            player.c "And how does your inner feminist feel about that, slut?"
            wt_image intro_wife_lingerie_2_29
            ivy.c "This stupid feminist slut is incredibly turned on to be humiliating herself for a man's amusement."
            wt_image intro_wife_lingerie_2_27
            "You let her enjoy her time spent humiliating herself until she starts to tire out."
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_lingerie_2_25
                    player.c "How are your knees?"
                    ivy.c "Sore"
                    player.c "I think that's enough for tonight."
                    wt_image intro_wife_lingerie_2_24
                    ivy.c "Thank you."
                    wt_image intro_wife_lingerie_2_23
                    player.c "Are you thanking me for humiliating you, or for letting you stop?"
                    ivy.c "Both?"
                    change player energy by -energy_very_short
                "Tell her to suck your cock":
                    wt_image intro_wife_lingerie_2_26
                    player.c "That's enough crawling in circles.  You can crawl over by my feet now ask for the opportunity to suck on my thick cock."
                    wt_image intro_wife_lingerie_2_25
                    player.c "Didn't you hear me, you stupid slut?  Get over here and beg for my cock."
                    wt_image intro_wife_lingerie_2_27
                    "She fairly dashed over to you, then closes her eyes while making an 'o' with her mouth."
                    wt_image intro_wife_lingerie_2_31
                    ivy.c "This stupid slut would like your thick cock in her mouth."
                    player.c "Will you do a good job for me?"
                    if ivy.has_tag('bj_training'):
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb slut, but I'm a well-trained cocksucker."
                        else:
                            ivy.c "Yes.  I may be a dumb slut, but I'm a well-trained cocksucker."
                    else:
                        if ivy.serve_count > 1:
                            ivy.c "Yes, Sir.  I may be a dumb slut, but I know how to suck dick, Sir."
                        else:
                            ivy.c "I may be a dumb slut, but I know how to suck dick."
                    call ivy_crawl_blowjob_fishnets from _call_ivy_crawl_blowjob_fishnets_5
            "She goes to change and heads home, leaving you to get on with your day."
        "Naked":
            player.c "Don't just stand there like a deer in the headlights.  Remove your clothes."
            wt_image intro_wife_visit_2_6
            player.c "Hurry up and come stand over here."
            wt_image intro_wife_naked_1_1
            player.c "I don't want to be looking at you standing up.  I want you to lower yourself for me, literally."
            wt_image intro_wife_naked_1_2
            player.c "You don't have to turn around."
            ivy.c "I find it easier like this."
            wt_image intro_wife_naked_1_3
            player.c "Spread your legs, then.  Does that make it even easier to humiliate yourself, you stupid cunt?"
            wt_image intro_wife_naked_1_4
            ivy.c "Maybe.  Do you have to call me that?"
            wt_image intro_wife_naked_1_5
            player.c "Why shouldn't I call you a stupid cunt?  That's what you are, aren't you?  Why are you kneeling up?  What did I say I would have you do when you got here?"
            wt_image intro_wife_naked_1_7
            ivy.c "You said I would get down on all fours and crawl at your feet."
            player.c "Are you on all fours, you stupid cunt?"
            wt_image intro_wife_naked_1_8
            player.c "That's a start, but you're still not moving.  Ivy, could you please start crawling for me?  I'm really looking forward to watching you humiliate yourself."
            player.c "Why aren't you moving?"
            ivy.c "I ... I'm not sure I can ..."
            player.c "I said move your fucking ass you stupid cunt.  Now!"
            wt_image intro_wife_naked_1_10
            player.c "There.  That's why I called you a stupid cunt.  Because you need to be reminded of what you are before you'll degrade yourself for my amusement."
            wt_image intro_wife_naked_1_11
            player.c "This way.  Follow me.  Keep up.  Animals are supposed to move faster on four legs than I can on two."
            wt_image intro_wife_naked_1_13
            player.c "How does the modern, independent feminist feel about following me around on her hands and knees?"
            wt_image intro_wife_naked_1_12
            ivy.c "I feel like a stupid cunt.  A very turned on, stupid cunt."
            player.c "Get down lower and grovel, cunt."
            wt_image intro_wife_naked_1_9
            ivy.c "Thank you for putting me at your feet and treating me like the stupid cunt I am."
            $ title = "What now?"
            menu:
                "Send her home":
                    player.c "You're welcome.  Crawl over to where your clothes are, then get dressed and crawl out the door."
                    wt_image intro_wife_naked_1_13
                    ivy.c "But ..."
                    player.c "If you don't want to crawl out dressed and then be allowed to stand up, you can crawl out the door naked and get dressed on my front step."
                    wt_image intro_wife_naked_1_10
                    ivy.c "I'll crawl out dressed.  What if someone sees me?"
                    player.c "You can tell them what you are, if you'd like.  Just in case they can't guess."
                    change player energy by -energy_very_short
                "Tell her to suck your cock":
                    player.c "You're welcome.  Crawl over here and ask for the opportunity to suck on my thick cock."
                    call ivy_crawl_blowjob_naked from _call_ivy_crawl_blowjob_naked_2
        "In the slutty clothes she brought":
            player.c "Did you forget to bring something slutty to wear, you stupid cunt?"
            wt_image intro_wife_visit_2_2
            "She shakes her head."
            player.c "Get out of those respectable clothes and let's see what you've brought."
            wt_image intro_wife_visit_2_6
            "Hurry up.  That matching underwear set better not be what you meant.  It's too nice for you.  Get changed and follow me."
            wt_image intro_wife_crawl_1_1
            "She strips naked and pulls on a tiny one-piece outfit she takes out of her purse, then hurries outside to follow you."
            call forced_movement(backyard) from _call_forced_movement_958
            summon ivy
            wt_image intro_wife_crawl_1_2
            player.c "I thought a dumb animal like you might appreciate getting some fresh air.  Show me how you dressed to amuse me."
            wt_image intro_wife_crawl_1_3
            player.c "Not bad.  I can see why you thought this was humiliating enough that I might let you stay on your feet if you wore it.  Pull the top down."
            wt_image intro_wife_crawl_1_4
            player.c "Good girl.  Bend over."
            wt_image intro_wife_crawl_1_5
            player.c "No panties.  Good.  Stupid cunts and animals don't wear panties.  I'm glad you recognized that.  Get down on the ground."
            wt_image intro_wife_crawl_1_6
            player.c "Legs wide open?  Are you trying to distract me before I take you for your walk?  Bark twice if you'd like me to walk you around the neighborhood, three times if you just want want to walk you inside."
            if not ivy.has_tag('barked'):
                ivy.c "Bark?  I couldn't ..."
                player.c "No talking.  Women talk.  A dumb bitch like you barks if she wants to communicate."
                add tags 'barked' to ivy
            wt_image intro_wife_crawl_1_7
            ivy.c "WOOF ... WOOF ... WOOF"
            player.c "Are you sure?  If I walk you outside, you'll get to meet new people.  I'm sure some of the neighbors would love to pet you.  I can see the idea's making you wet."
            ivy.c "WOOF ... WOOF ... WOOF"
            wt_image intro_wife_crawl_1_8
            player.c "Okay, inside the house it is.  Go for a run and I'll follow you."
            call forced_movement(living_room) from _call_forced_movement_959
            summon ivy
            wt_image intro_wife_crawl_1_9
            player.c "Tired so soon?  Your legs are shaking.  I think the idea of being walked around the neighborhood really got to you."
            $ title = "What now?"
            menu:
                "Send her home":
                    wt_image intro_wife_crawl_1_1
                    ivy.c "My legs really are shaking."
                    wt_image intro_wife_visit_2_8
                    ivy.c "I still can't figure out why I let you treat me like that."
                    wt_image intro_wife_visit_2_6
                    player.c "It's because you're a good bitch, aren't you?  Show me me you're a good bitch."
                    wt_image intro_wife_visit_2_2
                    ivy.c "{size=-5}woof{/size}"
                    player.c "That's a good girl.  Go pretend to be a modern, liberated woman.  I'll let you know when you're allowed to crawl for me again."
                    change player energy by -energy_very_short
                "Tell her to suck your cock":
                    player.c "Lie down on the floor.  I have something for you."
                    wt_image intro_wife_crawl_1_10
                    player.c "No, don't move.  You're not allowed to have this until you show me you really want it."
                    "She hesitates for a while, staring at your erection."
                    ivy.c "I ..."
                    player.c "No.  No talking, bitch.  Communicate like the stupid animal you are."
                    ivy.c "woof"
                    player.c "That doesn't show me anything.  Show me the modern, liberated woman who walked in here understands what she really is."
                    ivy.c "WOOF! ... WOOF! ... WOOF!"
                    player.c "You're just a stupid bitch who wants nothing else in the world right now than to be able to suck my cock, aren't you?"
                    ivy.c "WOOF!! ... WOOF!! ... WOOF!!"
                    player.c "Crawl over here in front of me and tell me again."
                    wt_image intro_wife_crawl_1_11
                    ivy.c "WOOF! ... WOOF! ... WOOF!"
                    player.c "It's a real honor for a stupid animal like you to be allowed to suck my cock, isn't it?"
                    ivy.c "WOOF!! ... WOOF!! ... WOOF!!"
                    player.c "Okay, girl.  Come get your treat."
                    wt_image intro_wife_crawl_1_12
                    player.c "You like being allowed to lick me, don't you?"
                    wt_image intro_wife_crawl_1_13
                    ivy.c "WOOF"
                    player.c "You like being treated like a stupid bitch whose only purpose is to please a man whenever she's allowed to, don't you?"
                    wt_image intro_wife_crawl_1_14
                    "She nods as she wraps her lips around you cock."
                    player.c "I didn't hear you.  Tell me who likes to be treated as a stupid bitch?"
                    wt_image intro_wife_crawl_1_13
                    ivy.c "WOOF!"
                    wt_image intro_wife_crawl_1_15
                    player.c "And who wants a load of cum on her face to make her look like the slutty stupid bitch she is?"
                    wt_image intro_wife_crawl_1_13
                    ivy.c "WOOF!"
                    wt_image intro_wife_bj_1_21
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_bj_1_22
                    player.c "This is a good look for a dumb cunt, isn't it?  Crawling on all fours with a load of cum on her face, barking like a dog."
                    ivy.c "{size=-5}woof{/size}"
                    player.c "That's a good girl.  Go pretend to be a modern, liberated woman.  I'll let you know when you're allowed to crawl for me again."
                    $ ivy.blowjob_count += 1
                    $ ivy.facial_count += 1
                    orgasm
    wt_image current_location.image
    call character_location_return(ivy) from _call_character_location_return_657
    notify
    return

#Domme visit content
label ivy_domme_visit:
    $ ivy.training_session()
    if not ivy.has_tag('second_domme_scene'):
        ivy.c "Remove your clothes and wait for me."
        call ivy_domme_session_two from _call_ivy_domme_session_two_1
        wt_image intro_wife_visit_4_1
        "After she changes, she unhooks the leash from your cock and leaves, letting you go on with your day."
        change player energy by -energy_short
    elif not ivy.has_tag('third_domme_session'):
        ivy.c "I need you to understand something, first.  If you want me to do this again, I'm going to put your leash back on."
        ivy.c "The last time I did that, I was so turned on by leaving you with a throbbing erection, I went home and had amazing sex with my husband, cumming three times."
        ivy.c "So maybe this time I'll feel more like watching you cum afterwards, but there's a very high chance that I'll feel more like leaving you hanging, while I go home and have sex with my husband, again."
        ivy.c "Are you sure you want to go through that again?"
        $ title = "What do you tell her?"
        menu:
            "Yes, Mistress":
                player.c "Yes, Mistress.  I want to please you in whatever way you choose."
                ivy.c "Okay, boy.  Remove your clothes and wait for me while I go get your leash."
                call ivy_domme_session_three from _call_ivy_domme_session_three_1
                "She unhooks the leash from your cock and leaves, letting you go on with your day."
                change player energy by -energy_short
            "No, end the visit":
                player.c "Thanks for the open communication, Ivy.  I'm not really in the mood to be blue balled again.  I guess I'm not really in the mood to let you take charge right now."
                ivy.c "That's okay.  I wasn't sure I'm really ready to do this anyway.  I'll be going."
    else:
        $ ivy.domme_you_outfit_count += 1
        if ivy.domme_you_outfit_count > 6:
            $ ivy.domme_you_outfit_count = 1
        # tied sex
        if ivy.domme_you_outfit_count == 1:
            add tags 'bought_crop' to ivy
            wt_image intro_wife_visit_4_1
            ivy.c "Remove your clothes, boy.  I'll be right back."
            wt_image current_location.image
            "You strip as she disappears into the bathroom ..."
            wt_image intro_wife_domme_2_1
            "... re-appearing a few minutes later, carrying a crop."
            ivy.c "Good, you're naked.  As you can see, I've brought something for you.  I wonder which you're more in the mood for?"
            wt_image intro_wife_domme_2_2
            ivy.c "A taste of this?"
            wt_image intro_wife_domme_2_3
            ivy.c "Or a taste of this?"
            player.c "I ..."
            wt_image intro_wife_domme_2_4
            ivy.c "Quiet!  I'll decide.  Let's keep things a mystery for you until I do."
            "She slips a blindfold over your eyes as she bites your lip, silencing you ..."
            wt_image intro_wife_domme_2_5
            "... then backs you up against the stairs and ties you to the railing."
            ivy.c "I'm disappointed in you, boy."
            wt_image intro_wife_domme_2_6
            ivy.c "I like seeing this big dick of yours completely hard, not semi-hard."
            wt_image intro_wife_domme_2_5
            "The next thing you feel is the crop striking your cock ... *thwapp*"
            player.c "Ow!"
            ivy.c "Bad dick, bad!"
            "*thwapp*  *thwapp*  *thwapp*"
            player.c "Ow!  Ow!!  OW!!"
            wt_image intro_wife_domme_2_16
            "The sensation after that is much more pleasant, as you feel Mistress' soft lips wrap around your cock."
            ivy.c "Mmmm.  Seems this naughty cock was looking forward to getting a taste of the crop."
            wt_image intro_wife_domme_2_7
            "The next sensation is almost as pleasant, as the warmth and smell of Mistress' pussy descends on your face."
            ivy.c "Now for the other taste.  Make it up to me for having such a naughty cock, boy.  Work your tongue right into me.  Mmmmm ... that's nice.  You're a good cunt licker."
            wt_image intro_wife_domme_2_8
            "When she eventually removes her pussy from your mouth, you feel the ropes loosen around your wrists.  Then as she pushes your blindfold away, you feel the ropes tighten around much more sensitive body parts."
            player.c "Ow!"
            ivy.c "This is a bit better.  Your naughty cock is starting to behave."
            wt_image intro_wife_domme_2_9
            ivy.c "No cumming while Mistress gets your cock ready, boy.  Not that you'd be able to with these ropes pulled tight, anyway."
            wt_image intro_wife_domme_2_10
            ivy.c "I want to feel your cock inside me, fucking me.  But don't you dare cum, boy, or you'll never feel the inside of Mistress' pussy again."
            wt_image intro_wife_domme_2_11
            ivy.c "Come on, fuck me!  Harder!  Faster!!  Show me you know how to use that big dick of yours."
            wt_image intro_wife_domme_2_12
            ivy.c "Mmmmm.  that's better.  You're not getting deep enough into me, though.  Lie down."
            wt_image intro_wife_domme_2_13
            ivy.c "That's a good fucktoy.  Lie there while Mistress gets herself off riding your cock."
            wt_image intro_wife_domme_2_14
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_domme_2_15
            ivy.c "That's a good boy, holding back your orgasm while Mistress made use of your hard cock.  I didn't let you cum the last time I domme'd you.  What do you think I should do today, boy?  Do you think I should reward you with an orgasm?"
            $ title = "What do you say?"
            menu:
                "Yes please, Mistress":
                    player.c "Yes, Mistress.  Please, Mistress?  May I please be allowed to cum, Mistress?"
                    wt_image intro_wife_domme_2_9
                    ivy.c "That's nice, boy.  I enjoy hearing you beg.  When I loosen the ropes, I want you to give me your cum."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_domme_2_17
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_domme_2_18
                    ivy.c "Mmmm.  That's a good boy, showing Mistress how much you appreciate her by giving me such a nice big load of your cum.  I hope you enjoyed your reward, boy?"
                    player.c "Yes, Mistress, very much.  Thank you!"
                    $ ivy.blowjob_count += 1
                    $ ivy.facial_count += 1
                    orgasm
                    "She cleans herself up then heads out, letting you go on with your day."
                "No, Mistress":
                    player.c "No, Mistress.  My cock disappointed you by not being hard when you wanted it to be.  I don't deserve to cum."
                    wt_image intro_wife_domme_2_9
                    ivy.c "That's a good point, boy.  You really don't deserve to cum.  I'm going to tie this rope tight around your nut sack to remind you about how you disappointed me.  No removing it until after I'm gone."
                    player.c "Yes, Mistress.  Thank you, Mistress."
                    change player energy by -energy_short
                    "She heads out, leaving you and your blue balls to go on with your day."
                "Whatever would please you most, Mistress":
                    ivy.c "That's the right answer, boy.  Very good!"
                    wt_image intro_wife_domme_2_9
                    ivy.c "I want you to show me how much you enjoyed getting to be inside my pussy today.  When I loosen the ropes, I want you to give me your cum."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_domme_2_17
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_domme_2_18
                    ivy.c "Mmmm.  That's a good boy, showing Mistress how much you appreciate her by giving me such a nice big load of your cum.  I hope you enjoyed this privilege, boy?"
                    player.c "Yes, Mistress, very much.  Thank you!"
                    $ ivy.blowjob_count += 1
                    $ ivy.facial_count += 1
                    orgasm
                    "She cleans herself up then heads out, letting you go on with your day."
        # note: these are all ifs to facilitate scrolling through options
        # smothering scene
        if ivy.domme_you_outfit_count == 2:
            if not ivy.has_tag('no_facesitting'):
                $ ivy.facesitting_outfit += 1
                if ivy.facesitting_outfit > 3:
                    $ ivy.facesitting_outfit = 1
                if not ivy.has_tag('discussed_smothering'):
                    wt_image intro_wife_visit_4_1
                    add tags 'discussed_smothering' to ivy
                    ivy.c "I've been reading up on some of the things Domme's do with their submissives, and something that caught my interest was facesitting.  I like the idea of you being pinned under my weight and forced to orally service me."
                    wt_image intro_wife_visit_4_2
                    ivy.c "Some submissives even enjoy having their breathing restricted by their Mistress' body while they're servicing her, and the idea of doing that to you also turns me on.  What do you say?"
                    $ title = "What do you say?"
                    menu:
                        "Yes, Mistress":
                            player.c "Yes, Mistress.  If that would please you, I'll do that for you."
                            wt_image intro_wife_visit_4_3
                            ivy.c "What a good boy you are.  Get down on the floor ..."
                            wt_image intro_wife_facesitting_1_1
                            ivy.c "... you can pleasure Mistress through her panties to start."
                            wt_image intro_wife_facesitting_1_2
                            "She presses her pantied sex into your face, sliding back and forth, alternating between cutting off your air and letting you breath while you work your tongue on her as best you can."
                            wt_image intro_wife_facesitting_1_3
                            ivy.c "Good boy.  For being so obedient, I'm going to let you put your tongue inside me now."
                            wt_image intro_wife_facesitting_1_4
                            "As she descends again, your breathing is completely cut off.  She lifts her hips just enough from time to time to let you gasp for air, then settles back down, her ass covering your nose, her sex covering your face as you work your tongue frantically inside her."
                            wt_image intro_wife_facesitting_1_5
                            "Eventually your efforts work, and she shifts around.  You can breath more easily in this position, at least most of the time, as you slide your tongue from her anus to her clit and back again, repeating again and again as she grinds her sex into your face, getting wetter and wetter."
                            wt_image intro_wife_facesitting_1_6
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            "It's an intense, long-lasting orgasm that floods your mouth, cutting off your breath once again as she twitches and grinds down onto your nose and face."
                            wt_image intro_wife_facesitting_1_7
                            ivy.c "How did that feel, boy?  Would you do that again to please me?"
                            $ title = "Do you want her to do this again sometime?"
                            menu:
                                "Yes, Mistress":
                                    player.c "Yes, Mistress.  If that's something you'd like."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "You are such a good submissive.  I really appreciate getting to spend time with you this way."
                                "Facesitting is okay, but not smothering":
                                    add tags 'no_smothering' to ivy
                                    player.c "The only thing I didn't like was having my air cut off, Mistress."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay.  Thank you for letting me know.  I won't restrict your breathing in the future.  Thank you for trying it once for me.  I really appreciate that!"
                                "I'll worship your ass, but not with you on top of me":
                                    add tags 'ass_worship_only' to ivy
                                    player.c "I'll happily worship your ass, Mistress, but not with you on top of me.  I wasn't in to that at all."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay, we won't do it like that again.  Thank you for letting me know how you felt.  And thank you for trying the facesitting once for me. I really appreciate that!"
                                "I'm not into this at all":
                                    add tags 'no_facesitting' to ivy
                                    player.c "I'm not really into this type of play, Mistress."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay, we won't do this again.  Thank you for letting me know how you felt.  And thank you for trying it once for me. I really appreciate that!"
                            $ ivy.pleasure_her_count += 1
                            $ ivy.orgasm_count += 1
                            change player energy by -energy_short
                        "Facesitting is okay, but not smothering":
                            add tags 'no_smothering' to ivy
                            player.c "I'm okay with you sitting on my face, Mistress, but not with having my air cut off."
                            wt_image intro_wife_visit_4_3
                            ivy.c "I understand.  I won't restrict your breathing.  Get down on the floor ..."
                            wt_image intro_wife_facesitting_1_1
                            ivy.c "... you can pleasure Mistress through her panties to start."
                            wt_image intro_wife_facesitting_1_2
                            "She presses her pantied sex into your face, sliding back and forth, but being careful always to allow you to breathe through either your mouth or your nose while you work your tongue on her as best you can."
                            wt_image intro_wife_facesitting_1_3
                            ivy.c "Good boy.  For being so obedient, I'm going to let you put your tongue inside me now."
                            wt_image intro_wife_facesitting_1_5
                            "She descends again, her warm, musty smell assaulting your nose as her moist sex slides across your face.  You run your tongue from her anus to her clit and back again, repeating again and again as she grinds her sex into your face, getting wetter and wetter."
                            wt_image intro_wife_facesitting_1_6
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            "It's an intense orgasm that floods your face as she twitches and grinds into you."
                            wt_image intro_wife_facesitting_1_7
                            ivy.c "How did that feel, boy?  Would you do that again to please me?"
                            $ title = "Do you want her to do this again sometime?"
                            menu:
                                "Yes, Mistress":
                                    player.c "Yes, Mistress.  If that's something you'd like."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "You are such a good submissive.  I really appreciate getting to spend time with you this way."
                                "I'll worship your ass, but not with you on top of me":
                                    add tags 'ass_worship_only' to ivy
                                    player.c "I'll happily worship your ass, Mistress, but not with you on top of me.  I wasn't in to that at all."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay, we won't do it like that again.  Thank you for letting me know how you felt.  And thank you for trying the facesitting once for me. I really appreciate that!"
                                "I'm not into this at all":
                                    add tags 'no_facesitting' to ivy
                                    player.c "I'm not really into this type of play, Mistress."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay, we won't do this again.  Thank you for letting me know how you felt.  And thank you for trying it once for me. I really appreciate that!"
                            $ ivy.pleasure_her_count += 1
                            $ ivy.orgasm_count += 1
                            change player energy by -energy_short
                        "I'll worship your ass, but not with you on top of me":
                            add tags 'ass_worship_only' to ivy
                            player.c "I'll happily worship your ass, Mistress, but not with you on top of me.  I wasn't in to that at all."
                            wt_image intro_wife_visit_4_3
                            ivy.c "I understand.  No facesitting.  You worshiping my ass sounds fun, though.  Get down on your knees, head down."
                            wt_image intro_wife_facesitting_1_8
                            ivy.c "You'd happily worship my ass, would you?  Okay then ..."
                            wt_image intro_wife_facesitting_1_9
                            ivy.c "... start worshiping."
                            wt_image intro_wife_facesitting_1_10
                            "You bury your nose between her butt cheeks and work your tongue from her anus to her clit and then back again, continually repeating as she bucks her hips, grinding her sex up and down along your face as she gets wetter and wetter."
                            wt_image intro_wife_facesitting_1_11
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            "She holds your head firmly in place as she thrusts her hips back into you, coating your face with her juices as she cums."
                            wt_image intro_wife_facesitting_1_7
                            ivy.c "How did that feel, boy?  Would you do that again to please me?"
                            $ title = "Do you want her to do this again sometime?"
                            menu:
                                "Yes, Mistress":
                                    player.c "Yes, Mistress.  If that's something you'd like."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "You are such a good submissive.  I really appreciate getting to spend time with you this way."
                                "I'm not into this at all":
                                    add tags 'no_facesitting' to ivy
                                    player.c "I'm not really into this type of play, Mistress."
                                    wt_image intro_wife_visit_4_3
                                    ivy.c "Okay, we won't do this again.  Thank you for letting me know how you felt.  And thank you for trying it once for me. I really appreciate that!"
                            $ ivy.pleasure_her_count += 1
                            $ ivy.orgasm_count += 1
                            change player energy by -energy_short
                        "I'm not into this at all":
                            add tags 'no_facesitting' to ivy
                            player.c "I'm not really into that type of play, Mistress."
                            ivy.c "I understand.  I did sort of just spring it on you.  That's okay.  There are other fun things we can do together.  I'll think of something different for our next session."
                    "She heads out, letting you go on with your day."
                elif ivy.has_tag('ass_worship_only'):
                    wt_image intro_wife_visit_4_1
                    ivy.c "I have a problem with you, boy."
                    player.c "What is it, Mistress?"
                    wt_image intro_wife_visit_4_3
                    ivy.c "Get on your knees, head bowed, when you ask me a question, boy."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_facesitting_1_8
                    "You kneel as she undresses, head down."
                    wt_image intro_wife_facesitting_1_7
                    "When she cups your chin in her hand and lifts your face, you ask again."
                    player.c "What is your problem with me, Mistress?"
                    ivy.c "It's a simple one, boy.  It's been too long since you worshiped my ass properly."
                    wt_image intro_wife_facesitting_1_9
                    ivy.c "Correct that, boy."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_facesitting_1_10
                    "You bury your nose between her butt cheeks and work your tongue from her anus to her clit and then back again, continually repeating as she bucks her hips, grinding her sex up and down along your face as she gets wetter and wetter."
                    wt_image intro_wife_facesitting_1_11
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    "She holds your head firmly in place as she thrusts her hips back into you, coating your face with her juices as she cums."
                    wt_image intro_wife_visit_4_3
                    ivy.c "That's much better.  Now I feel appreciated."
                    player.c "Yes, Mistress.  Thank you for letting me worship your ass, Mistress."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    change player energy by -energy_short
                elif ivy.facesitting_outfit == 3:
                    wt_image intro_wife_visit_4_1
                    ivy.c "I've been wondering something, boy."
                    player.c "What is it, Mistress?"
                    wt_image intro_wife_visit_4_3
                    ivy.c "Get on your knees, head bowed, when you ask me a question, boy."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_facesitting_1_8
                    "You kneel as she undresses, head down."
                    wt_image intro_wife_facesitting_1_7
                    "When she cups your chin in her hand and lifts your face, you ask again."
                    player.c "What have you been wondering, Mistress?"
                    ivy.c "What it will feel like to have you worship my ass without my bodyweight on you holding your head in place."
                    wt_image intro_wife_facesitting_1_9
                    ivy.c "Show me what it feels like, boy."
                    player.c "Yes, Mistress."
                    wt_image intro_wife_facesitting_1_10
                    "You bury your nose between her butt cheeks and work your tongue from her anus to her clit and then back again, continually repeating as she bucks her hips, grinding her sex up and down along your face as she gets wetter and wetter."
                    wt_image intro_wife_facesitting_1_11
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    "She holds your head firmly in place as she thrusts her hips back into you, coating your face with her juices as she cums."
                    wt_image intro_wife_visit_4_3
                    if ivy.has_tag('no_smothering'):
                        ivy.c "Mmmm.  That was nice.  Not as nice as watching you struggle to please me with my ass smothering your face, but fun for a change."
                    else:
                        ivy.c "Mmmm.  That was nice.  Not as nice as riding your face, but fun for a change."
                    player.c "Yes, Mistress.  I'm glad you enjoyed yourself."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    change player energy by -energy_short
                elif ivy.has_tag('no_smothering'):
                    wt_image intro_wife_visit_4_3
                    ivy.c "Lie down on the floor, boy."
                    wt_image intro_wife_facesitting_1_1
                    ivy.c "Mistress is going to go for a ride on your face."
                    wt_image intro_wife_facesitting_1_2
                    "She presses her pantied sex into your face, sliding back and forth, but being careful always to allow you to breathe through either your mouth or your nose while you work your tongue on her as best you can."
                    wt_image intro_wife_facesitting_1_3
                    ivy.c "Good boy.  I'm going to let you put your tongue inside me now."
                    wt_image intro_wife_facesitting_1_5
                    "She descends again, her warm, musty smell assaulting your nose as her moist sex slides across your face.  You run your tongue from her anus to her clit and back again, repeating again and again as she grinds her sex into your face, getting wetter and wetter."
                    wt_image intro_wife_facesitting_1_6
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    "It's an intense orgasm that floods your face as she twitches and grinds into you."
                    wt_image intro_wife_visit_4_3
                    ivy.c "That felt really nice."
                    player.c "Thank you, Mistress.  I'm glad you were able to riding my face."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    change player energy by -energy_short
                else:
                    wt_image intro_wife_visit_4_3
                    ivy.c "Lie down on the floor, boy."
                    wt_image intro_wife_facesitting_1_1
                    ivy.c "Mistress is going to go for a ride on your face."
                    wt_image intro_wife_facesitting_1_2
                    "She presses her pantied sex into your face, sliding back and forth, alternating between cutting off your air and letting you breath while you work your tongue on her as best you can."
                    wt_image intro_wife_facesitting_1_3
                    ivy.c "Good boy.  I'm going to let you put your tongue inside me now."
                    wt_image intro_wife_facesitting_1_4
                    "As she descends again, your breathing is completely cut off.  She lifts her hips just enough from time to time to let you gasp for air, then settles back down, her ass covering your nose, her sex covering your face as you work your tongue frantically inside her."
                    wt_image intro_wife_facesitting_1_5
                    "Eventually your efforts work, and she shifts around.  You can breath more easily in this position, at least most of the time, as you slide your tongue from her anus to her clit and back again, repeating again and again as she grinds her sex into your face, getting wetter and wetter."
                    wt_image intro_wife_facesitting_1_6
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    "It's an intense, long-lasting orgasm that floods your mouth, cutting off your breath once again as she twitches and grinds down onto your nose and face."
                    wt_image intro_wife_visit_4_3
                    ivy.c "That felt really nice.  I love watching you squirm when your oxygen supply is cut off.  Your tongue works so frantically inside me when you can't breathe, it's an incredible turn on."
                    player.c "Thank you, Mistress.  I'm glad I'm able to please you like that."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    change player energy by -energy_short
            else:
                $ ivy.domme_you_outfit_count += 1
        # spanking scene with possible orgasm/no orgasm outcome
        if ivy.domme_you_outfit_count == 3:
            wt_image intro_wife_visit_4_1
            ivy.c "Remove your clothes, boy.  I'll be right back."
            wt_image current_location.image
            "You strip as she disappears into the bathroom ..."
            wt_image intro_wife_domme_3_1
            "... re-appearing a few minutes later, carrying a crop."
            wt_image intro_wife_domme_3_2
            ivy.c "On your knees.  Head down, ass up."
            wt_image intro_wife_domme_3_3
            ivy.c "Count, and thank me after each one."
            wt_image intro_wife_domme_3_4
            "She doesn't hold back, swinging the crop with all her strength, striking you across your raised and exposed buttocks ... *THWAPP*"
            player.c "OW!  That's one.  Thank you, Mistress!"
            wt_image intro_wife_domme_3_5
            ivy.c "Keep counting."
            wt_image intro_wife_domme_3_4
            "*THWAPP*"
            wt_image intro_wife_domme_3_5
            player.c "OW!  That's two.  Thank you, Mistress!"
            wt_image intro_wife_domme_3_4
            "*THWAPP*"
            $ ivy.temporary_count = 3
            wt_image intro_wife_domme_3_5
            player.c "OW!  That's three.  "
            $ title = "What do you say?"
            menu menu_ivy_domme_spanking_count_menu:
                "Thank you, Mistress":
                    extend "Thank you, Mistress."
                    if ivy.temporary_count == 20:
                        pass
                    else:
                        $ ivy.temporary_count += 1
                        wt_image intro_wife_domme_3_4
                        "*THWAPP*"
                        wt_image intro_wife_domme_3_5
                        $ ivy.count = ivy.temporary_count.to_s
                        # note: !c should capitalizes the first letter, but isn't, so added "That's" in front of it
                        player.c "OW!  That's [ivy.count!c].  "
                        jump menu_ivy_domme_spanking_count_menu
                "Mercy, Mistress":
                    extend "Mercy, Mistress!!  Mercy, please!!!"
            wt_image intro_wife_domme_3_6
            if ivy.temporary_count == 20:
                ivy.c "Good boy, taking so many strokes for me."
                wt_image intro_wife_domme_3_7
                ivy.c "Come get your reward."
            elif ivy.temporary_count < 10:
                ivy.c "Is that all you can take?  I thought you were made of tougher stuff than that."
                wt_image intro_wife_domme_3_7
                ivy.c "I hope you demonstrate better endurance for your next task."
            else:
                ivy.c "Had enough have you?  Okay then."
                wt_image intro_wife_domme_3_7
                ivy.c "Time to put you to other uses."
            wt_image intro_wife_domme_3_8
            "In case you weren't sure what she meant, her hand at the back of your head makes it clear, guiding your mouth onto her already wet sex."
            wt_image intro_wife_domme_3_9
            ivy.c "That's it.  Work your tongue right inside me.  Does this excite you, boy, getting to lick Mistress' wet slit?"
            wt_image intro_wife_domme_3_10
            player.c "Yes, Mistress."
            ivy.c "Show me."
            wt_image intro_wife_domme_3_11
            ivy.c "That's the state I like to see your cock in, boy."
            wt_image intro_wife_domme_3_12
            ivy.c "Mmmm.  I'm going to enjoy making use of this erection.  Lie down, boy."
            wt_image intro_wife_domme_3_13
            ivy.c "No cumming, boy.  Right ow this erection is for my pleasure, not yours."
            wt_image intro_wife_domme_3_14
            "She does indeed seem to enjoy your erection ..."
            wt_image intro_wife_domme_3_15
            "... bouncing up and down on your pole, faster and faster ..."
            wt_image intro_wife_domme_3_16
            "... until she suddenly slumps forward onto your chest."
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_domme_3_11
            ivy.c "Such a good boy, holding back your orgasm for me.  Your balls are aching now, aren't they?"
            player.c "Yes, Mistress."
            wt_image intro_wife_domme_3_17
            ivy.c "I wonder if I should pump your shaft and give these sore, frustrated testicles the relief they desire?"
            $ ivy.random_number = renpy.random.randint(1, 25)
            if ivy.temporary_count > ivy.random_number:
                # orgasm scene
                wt_image intro_wife_domme_3_12
                if ivy.temporary_count > 10:
                    ivy.c "You took quite a few strokes of the crop for me.  I think I'll give your balls some relief.  Besides, I'm turned on by the thought of you spilling your seed for me.  Not until I give you permission, though."
                else:
                    ivy.c "Your balls are in luck.  I'm turned on by the thought of you spilling your seed for me.  Not until I give you permission, though."
                wt_image intro_wife_domme_3_18
                "She starts stroking your shaft with her soft hand, slowly and gently at first, then faster and faster.  You're not sure you're going to be able to hold back, when she finally speaks."
                ivy.c "Spill your seed for me, boy."
                wt_image intro_wife_domme_3_19
                player.c "[player.orgasm_text]"
                wt_image intro_wife_domme_3_20
                ivy.c "Mmmm.  Mistress is very pleased with you today, boy."
                "After playing with your cock for a few minutes longer, she cleans herself up and heads out."
                $ ivy.handjob_count += 1
                orgasm
            else:
                # denial scene
                wt_image intro_wife_domme_3_21
                ivy.c "It's tempting to watch you spill your seed for me, but I'm even more turned on by the idea of leaving you sore and swollen and frustrated."
                wt_image intro_wife_domme_3_22
                ivy.c "No touching yourself after I'm gone.  And no inviting some other woman over to give you relief.  I want you to go to bed horny tonight in order to please me."
                "With those final instructions, she changes and heads home."
                change player energy by -energy_short
            $ ivy.orgasm_count += 1
        # strap on scene
        if ivy.domme_you_outfit_count == 4:
            if not ivy.has_tag('bought_strap_on'):
                add tags 'bought_strap_on' to ivy
                wt_image intro_wife_visit_4_2
                ivy.c "I bought a special surprise for you.  Undress and wait here while I go change."
                wt_image current_location.image
                "You strip and wait for her the return."
                wt_image intro_wife_strapon_1_1
                "When she does, she coyly hides what she had.  Or at least, as coyly as is possible with her bare ass and breasts on display."
                ivy.c "Can you guess what I have for you?"
                wt_image intro_wife_strapon_1_2
                ivy.c "What do you say?  Will you be my blushing bride and let me take your anal virginity?  Assuming you're not a slut who's already given it away to someone else."
                $ title = "What do you tell her?"
                menu:
                    "Yes, Mistress":
                        wt_image intro_wife_strapon_1_4
                        ivy.c "Don't be shy.  Come over here and do what all good girls do to get a dick ready to fuck them."
                        wt_image intro_wife_strapon_1_5
                        ivy.c "That's a good cocksucker.  Show me how much you love my dick and how much you want it inside you.  Make it nice and wet ..."
                        wt_image intro_wife_strapon_2_1
                        ivy.c "... because your pussy doesn't get as wet as mine ..."
                        wt_image intro_wife_strapon_2_2
                        ivy.c "... so we need to give it all the help it can get."
                        wt_image intro_wife_strapon_1_6
                        ivy.c "In fact, to show you how happy I am you agreed to take my dick in your pussy for the first time, I'll let you feel Mistress' tongue to get you ready."
                        wt_image intro_wife_strapon_1_7
                        ivy.c "That's got you excited, I can tell.  I think this tight wet pussy is ready to have it's cherry popped.  Roll over ..."
                        wt_image intro_wife_strapon_1_8
                        ivy.c "... I want to look at you when I make you my bitch."
                        "Without another word, she pushes the thick strap-on phallus into your well-lubed anus."
                        wt_image intro_wife_strapon_1_9
                        ivy.c "That's a good girl.  It feels so good sliding my big dick in and out of your tight, virgin pussy."
                        wt_image intro_wife_strapon_1_10
                        ivy.c "Finish me off now, girl.  Use your mouth to finish what your pussy started."
                        wt_image intro_wife_strapon_1_11
                        ivy.c "OH ... I'M CUMMINNGGG!!!"
                        wt_image intro_wife_strapon_1_12
                        ivy.c "Don't worry, I'm not going to take a girl's cherry without making sure she gets to cum."
                        wt_image intro_wife_strapon_1_13
                        ivy.c "You need to play with my dick while I suck you, though."
                        wt_image intro_wife_strapon_1_14
                        ivy.c "That's it.  Stroke my dick with your hand.  Feel my big fat cock between your fingers while you cum."
                        wt_image intro_wife_strapon_1_15
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_strapon_1_3
                        ivy.c "How did you enjoy that?  Are you willing to let me stick my dick in you again the next time the mood strikes me?"
                        $ title = "What do you tell her?"
                        menu:
                            "Yes, Mistress":
                                wt_image intro_wife_strapon_1_16
                                ivy.c "Good.  I'll look forward fucking my girl again sometime soon."
                            "I didn't really enjoy it":
                                add tags 'no_strap_on_play' to player
                                player.c "I didn't really enjoy that.  Except for being allowed to cum at the end, obviously.  But I didn't enjoy having the strap-on inside me."
                                wt_image intro_wife_strapon_1_2
                                ivy.c "Oh.  That's too bad.  Well, thank you for trying it once for me."
                                wt_image intro_wife_strapon_1_1
                                ivy.c "I'll think of something else for us to do, next time."
                        $ ivy.blowjob_count += 1
                        $ ivy.swallow_count += 1
                        $ ivy.orgasm_count += 1
                        orgasm
                        "She leaves you to go on with your day, a little more sore in the rear than you were before she arrived."
                    "I'm not into this":
                        add tags 'no_strap_on_play' to player
                        player.c "I'm not into the idea of you using a strap-on on me."
                        wt_image intro_wife_strapon_1_3
                        ivy.c "Really?  I thought you'd enjoy getting to be on the receiving end of a hard dick for a change."
                        player.c "That's not my thing."
                        wt_image intro_wife_strapon_1_1
                        ivy.c "Your loss.  I hadn't really planned anything else for today.  I'll think of something else for my next visit."
                        "She leaves you to go on with your day, your anal virginity still intact."
            elif not player.has_tag('no_strap_on_play'):
                $ ivy.strapon_outfit += 1
                if ivy.strapon_outfit > 3:
                    $ ivy.strapon_outfit = 1
                $ ivy.strapon_bj_outfit += 1
                if ivy.strapon_bj_outfit > 2:
                    $ ivy.strapon_bj_outfit = 1
                wt_image intro_wife_visit_4_1
                ivy.c "Take your clothes off.  I'll be right back."
                wt_image intro_wife_strapon_1_17
                ivy.c "Don't just stand there.  Do what all dirty girls do when someone presents them with a huge, thick cock.  Get down on your knees and crawl over and beg to be allowed to suck it."
                wt_image intro_wife_strapon_1_4
                player.c "Please may I be allowed to suck your cock, Mistress?"
                ivy.c "Are you going to do a good job for me, girl?"
                player.c "Yes, Mistress.  I'll make your cock feel really good."
                wt_image intro_wife_strapon_1_5
                ivy.c "Mmmm.  Not bad, but where I really want my cock is inside your super-tight pussy."
                if ivy.strapon_outfit == 1:
                    wt_image intro_wife_strapon_2_1
                    ivy.c "My fingers should be enough to get you ready today."
                    wt_image intro_wife_strapon_2_2
                    ivy.c "There.  That's good.  You're opening right up for me."
                    wt_image intro_wife_strapon_1_18
                    ivy.c "Stay right where you are while I work my dick into your tight hole."
                    wt_image intro_wife_strapon_1_19
                    ivy.c "Good girl.  You've taken my whole cock inside you."
                    wt_image intro_wife_strapon_1_20
                    ivy.c "Now I can give you a proper fucking."
                    wt_image intro_wife_strapon_1_21
                    "She does, reaming your ass so fast and hard it's all you can do not to scream out from the intensity of it."
                    wt_image intro_wife_strapon_1_18
                    ivy.c "Good girl, taking such a rough, hard fucking.  You deserve a reward."
                    if ivy.strapon_bj_outfit == 1:
                        extend "  Sit up"
                    else:
                        extend "  Roll over."
                elif ivy.strapon_outfit == 2:
                    wt_image intro_wife_strapon_1_6
                    ivy.c "Lucky you, getting to feel my tongue on your pussy today."
                    wt_image intro_wife_strapon_1_7
                    ivy.c "I can feel how excited that's making you."
                    wt_image intro_wife_strapon_1_18
                    ivy.c "Let's see if having my dick in you makes you just as excited?"
                    wt_image intro_wife_strapon_1_19
                    ivy.c "I think it is.  Look how quickly your tight hole stretched to take my dick today."
                    wt_image intro_wife_strapon_1_20
                    ivy.c "Mmmm.  I love fucking my girls' tight pussy."
                    wt_image intro_wife_strapon_1_21
                    ivy.c "Get me off, girl.  Buck those hips.  Work your ass back onto me.  Fuck me with your tight hole and get me off."
                    wt_image intro_wife_strapon_1_10
                    "Your ass proves unequal to the task, but she shifts to your mouth with has more success."
                    wt_image intro_wife_strapon_1_11
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_strapon_1_10
                    ivy.c "Mmmm.  Now you get your reward for letting me fuck you, girl."
                    if ivy.strapon_bj_outfit == 1:
                        extend "  Sit up"
                    $ ivy.orgasm_count += 1
                else:
                    wt_image intro_wife_strapon_2_1
                    ivy.c "My fingers should be enough to get you ready today."
                    wt_image intro_wife_strapon_2_2
                    ivy.c "There.  That's good.  You're opening right up for me.  Roll over on your back ..."
                    wt_image intro_wife_strapon_1_8
                    ivy.c "... I want to look at my bitch while I fuck her today.  You're enjoying this, aren't you?  I can feel how hard your dick is getting."
                    wt_image intro_wife_strapon_1_9
                    "The harder your dick gets, the faster she fucks your ass, and the faster she fucks your ass, the harder your dick gets.  It's a dangerous circle that soon leaves you raw and sore and ready to cum."
                    wt_image intro_wife_strapon_1_8
                    ivy.c "I think my girl's ready for her reward."
                    if ivy.strapon_bj_outfit == 1:
                        extend "  Sit up."
                if ivy.strapon_bj_outfit == 1:
                    wt_image intro_wife_strapon_1_22
                    ivy.c "Let's perk those little nipples of yours up, girl, while you get your reward.  Do those clothespins feel nice on your tiny tits, girl?"
                    player.c "Yes, Mistress."
                    wt_image intro_wife_strapon_1_23
                    ivy.c "Do they feel as good as my mouth does?"
                    player.c "No, Mistress.  Your mouth feels better."
                    ivy.c "Mmmm.  How sweet.  Would you like permission to cum?"
                    player.c "Yes, Mistress.  Please, may I please cum, Mistress?"
                    ivy.c "Okay, girl.  You can cum for me."
                    wt_image intro_wife_strapon_1_24
                    player.c "[player.orgasm_text]"
                else:
                    wt_image intro_wife_strapon_1_13
                    ivy.c "Mmmm.  I think your dick is even firmer than mine."
                    wt_image intro_wife_strapon_1_12
                    ivy.c "Play with my dick while I suck you, girl.  Make my dick hard."
                    wt_image intro_wife_strapon_1_14
                    ivy.c "That's it.  Stroke my dick with your hand.  Feel my big fat cock between your fingers while you cum."
                    wt_image intro_wife_strapon_1_15
                    player.c "[player.orgasm_text]"
                wt_image intro_wife_strapon_1_1
                ivy.c "I'm so glad you like taking my dick, because I love sticking it in you."
                "She disappears to change, then leaves to let you and your pleasantly sore butt get on with your day."
                $ ivy.blowjob_count += 1
                $ ivy.swallow_count += 1
                orgasm
            else:
                $ ivy.domme_you_outfit_count += 1
        # dungeon boots scene with foot worship and optional smothering scene
        if ivy.domme_you_outfit_count == 5:
            wt_image intro_wife_visit_4_1
            ivy.c "Get undressed.  I'll let you know when I'm ready for you."
            dismiss ivy
            wt_image current_location.image
            "You strip as she disappears.  A few minutes later, she calls to you from your dungeon."
            call forced_movement(dungeon) from _call_forced_movement_960
            summon ivy
            wt_image intro_wife_domme_4_1
            ivy.c "In here, boy."
            if not ivy.has_tag('bought_boots'):
                add tags 'bought_boots' to ivy
                extend "  I thought this room was the right setting to show off my new boots."
                wt_image intro_wife_domme_4_2
                ivy.c "Do you like them?"
                player.c "Yes, Mistress."
                wt_image intro_wife_domme_4_3
                ivy.c "Come show me."
                wt_image intro_wife_domme_4_4
                "You take her boot in your hand and start worshiping it..."
                wt_image intro_wife_domme_4_11
                "... sucking on the heel ..."
                wt_image intro_wife_domme_4_5
                "... and licking the sole and toe."
                wt_image intro_wife_domme_4_6
                ivy.c "That's enough.  I've got a better place for you to use your tongue."
                if ivy.has_tag('no_facesitting') or ivy.has_tag('ass_worship_only'):
                    wt_image intro_wife_domme_4_7
                    "She lies down and you put your head between her legs ..."
                    wt_image intro_wife_domme_4_8
                    "... and start licking her erect clit and sticky labia."
                    wt_image intro_wife_domme_4_9
                    "She doesn't keep you licking long."
                    wt_image intro_wife_domme_4_10
                elif ivy.has_tag('no_smothering'):
                    wt_image intro_wife_domme_4_12
                    ivy.c "Lie down."
                    wt_image intro_wife_domme_4_17
                    "As you do, she lowers herself onto your face."
                    wt_image intro_wife_domme_4_18
                    "You work your tongue back and forth along her sex, lapping up the steady flow of juices as her hips buck into you, more and more insistently."
                    wt_image intro_wife_domme_4_19
                else:
                    wt_image intro_wife_domme_4_12
                    ivy.c "Lie down."
                    wt_image intro_wife_domme_4_13
                    "As you do, she lowers herself onto your face."
                    wt_image intro_wife_domme_4_14
                    "The weight of her sex crushing into your mouth and her ass smothering your nose makes it almost impossible to breathe."
                    wt_image intro_wife_domme_4_15
                    "You work your tongue into her as fast and as hard as you can, trying desperately to get her to shift her hips to allow you a breath of air."
                    wt_image intro_wife_domme_4_16
                    "Eventually you succeed and she lifts her hips for a moment, only to grind down even harder into your face."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_domme_4_20
                ivy.c "Keep licking my cunt, boy, while Mistress rewards you."
                wt_image intro_wife_domme_4_21
                ivy.c "Cum for me, boy.  Cum for me with your tongue in my cunt."
                wt_image intro_wife_domme_4_22
                player.c "[player.orgasm_text]"
                wt_image intro_wife_domme_4_20
                ivy.c "Good boy.  That was a tasty big load of cum you gave me.  Make me cum again and then I'll be going."
                wt_image intro_wife_domme_4_19
                "It takes a little longer than her first orgasm, but a not a lot longer."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_domme_4_23
                ivy.c "I hope you don't mind that I took up more of your time than normal today.  Your tongue just felt extra good."
                "She hurries off, letting you go on with your day."
                $ ivy.pleasure_her_count += 2
                $ ivy.orgasm_count += 2
                $ ivy.blowjob_count += 1
                $ ivy.swallow_count += 1
                change player energy by -energy_short
                orgasm
            else:
                $ ivy.domme_boots_outfit += 1
                if ivy.domme_boots_outfit > 3:
                    $ ivy.domme_boots_outfit = 1
                # foot worship
                if ivy.domme_boots_outfit == 1:
                    wt_image intro_wife_domme_4_24
                    ivy.c "I've discovered something about these boots."
                    wt_image intro_wife_domme_4_25
                    ivy.c "They make my feet sweaty."
                    wt_image intro_wife_domme_4_26
                    ivy.c "Clean them, boy."
                    wt_image intro_wife_domme_4_27
                    player.c "Yes, Mistress."
                    wt_image intro_wife_domme_4_28
                    "You kiss and lick every inch of her smelly, sweaty feet ..."
                    wt_image intro_wife_domme_4_29
                    "... making sure to clean her toes and suckle each one."
                    wt_image intro_wife_domme_4_30
                    ivy.c "Mmmm.  That felt nice.  Let's find out if you did a good job.  Lie down."
                    wt_image intro_wife_domme_4_31
                    ivy.c "How do my feet seem now?"
                    wt_image intro_wife_domme_4_33
                    ivy.c "Do they feel nice on your cock and balls?"
                    player.c "Yes, Mistress."
                    wt_image intro_wife_domme_4_32
                    ivy.c "Do they feel nice on your face?"
                    player.c "Nnn, Nnnnnnn."
                    if ivy.has_tag('no_facesitting'):
                        wt_image intro_wife_domme_4_7
                        ivy.c "It seems you did a good job licking them clean.  Let's see if you can do an equally good job licking my pussy clean."
                        wt_image intro_wife_domme_4_8
                        "That proves to be a longer task, as her pussy leaks fluids almost as quickly as you can lap them up."
                        wt_image intro_wife_domme_4_9
                        "You keep at it, though, and eventually feel her shake and tremble under you."
                        wt_image intro_wife_domme_4_10
                    elif ivy.has_tag('ass_worship_only'):
                        wt_image intro_wife_domme_4_39
                        ivy.c "It seems you did a good job licking them clean.  Let's see if you can do an equally good job licking my pussy clean."
                        wt_image intro_wife_domme_4_40
                        "That proves to be a longer task, as her pussy leaks fluids almost as quickly as you can lap them up."
                        wt_image intro_wife_domme_4_41
                        "The task isn't made any easier when she uses her hand to make it clear she wants your nose all the way up her butt hole while you lick her.  You keep at it, though, and eventually feel her shake and tremble above you."
                        wt_image intro_wife_domme_4_42
                    elif ivy.has_tag('no_smothering'):
                        wt_image intro_wife_domme_4_34
                        ivy.c "It seems you did a good job licking them clean.  Let's see if you can do an equally good job licking my pussy clean."
                        wt_image intro_wife_domme_4_35
                        "That proves to be a longer task, as her pussy leaks fluids almost as quickly as you can lap them up."
                        wt_image intro_wife_domme_4_36
                        "You keep at it, though, and eventually feel her shake and tremble above you."
                        wt_image intro_wife_domme_4_38
                        "She shifts forward, cutting you off from all access to air.  You jab your tongue up into her as she grinds down hard on your face."
                    else:
                        wt_image intro_wife_domme_4_34
                        ivy.c "It seems you did a good job licking them clean.  Let's see if you can do an equally good job licking my pussy clean."
                        wt_image intro_wife_domme_4_35
                        "That proves to be a longer task, as her pussy leaks fluids almost as quickly as you can lap them up."
                        wt_image intro_wife_domme_4_36
                        "You keep at it, though, and eventually feel her shake and tremble above you."
                        wt_image intro_wife_domme_4_37
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_domme_4_20
                    ivy.c "You're getting an extra special treat today, boy.  I'm going to let you cum in Mistress' pussy."
                    wt_image intro_wife_domme_4_43
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_domme_4_34
                    ivy.c "Oops.  That means one more mess you need to clean up."
                    wt_image intro_wife_domme_4_36
                    "If you have to drink your own sperm, at least it tastes better coming out of Mistress' pussy."
                    wt_image intro_wife_domme_4_23
                    "When you've finished, she heads out, letting you go on with your day."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    $ ivy.sex_count += 1
                    orgasm
                # ass worship
                if ivy.domme_boots_outfit == 2:
                    if not ivy.has_tag('no_facesitting'):
                        wt_image intro_wife_domme_4_12
                        ivy.c "Down on your knees ..."
                        wt_image intro_wife_domme_4_44
                        ivy.c "... make Mistress feel appreciated."
                        wt_image intro_wife_domme_4_45
                        "You do your best ..."
                        wt_image intro_wife_domme_4_46
                        "... and before long, it seems you succeed."
                        wt_image intro_wife_domme_4_47
                        "She presses her butt against you more and more insistently."
                        wt_image intro_wife_domme_4_48
                        "You're forced to back up, until you reach the wall and can retreat no further."
                        wt_image intro_wife_domme_4_49
                        "She pins you there, your head pressed between the wall and her ass ..."
                        wt_image intro_wife_domme_4_50
                        "... until she feels fully appreciated."
                        ivy.c "OH ... I'M CUMMINNGGG!!!"
                        wt_image intro_wife_domme_4_51
                        ivy.c "Mmmm.  That was nice, boy."
                        wt_image intro_wife_domme_4_52
                        ivy.c "Don't get too excited about me teasing your cock and balls.  You're not going to cum today.  Leaving you with a hard on is just my way of showing that I appreciate you, too."
                        player.c "Thank you, Mistress."
                        "When she's finished teasing you, she leaves, letting you go on with your day."
                        $ ivy.pleasure_her_count += 1
                        $ ivy.orgasm_count += 1
                        change player energy by -energy_short
                    else:
                        $ ivy.domme_boots_outfit += 1
                # boot worship
                if ivy.domme_boots_outfit == 3:
                    wt_image intro_wife_domme_4_2
                    ivy.c "Come show me how much you like my boots."
                    wt_image intro_wife_domme_4_3
                    player.c "Yes, Mistress."
                    wt_image intro_wife_domme_4_4
                    "You take her boot in your hand and start worshiping it..."
                    wt_image intro_wife_domme_4_11
                    "... sucking on the heel ..."
                    wt_image intro_wife_domme_4_5
                    "... and licking the sole and toe."
                    wt_image intro_wife_domme_4_6
                    ivy.c "That's enough.  I've got a better place for you to use your tongue."
                    if ivy.has_tag('no_facesitting') or ivy.has_tag('ass_worship_only'):
                        wt_image intro_wife_domme_4_7
                        "She lies down and you put your head between her legs ..."
                        wt_image intro_wife_domme_4_8
                        "... and start licking her erect clit and sticky labia."
                        wt_image intro_wife_domme_4_9
                        "She doesn't keep you licking long."
                        wt_image intro_wife_domme_4_10
                    elif ivy.has_tag('no_smothering'):
                        wt_image intro_wife_domme_4_12
                        ivy.c "Lie down."
                        wt_image intro_wife_domme_4_17
                        "As you do, she lowers herself onto your face."
                        wt_image intro_wife_domme_4_18
                        "You work your tongue back and forth along her sex, lapping up the steady flow of juices as her hips buck into you, more and more insistently."
                        wt_image intro_wife_domme_4_19
                    else:
                        wt_image intro_wife_domme_4_12
                        ivy.c "Lie down."
                        wt_image intro_wife_domme_4_13
                        "As you do, she lowers herself onto your face."
                        wt_image intro_wife_domme_4_14
                        "The weight of her sex crushing into your mouth and her ass smothering your nose makes it almost impossible to breathe."
                        wt_image intro_wife_domme_4_15
                        "You work your tongue into her as fast and as hard as you can, trying desperately to get her to shift her hips to allow you a breath of air."
                        wt_image intro_wife_domme_4_16
                        "Eventually you succeed and she lifts her hips for a moment, only to grind down even harder into your face."
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_domme_4_20
                    ivy.c "Keep licking my cunt, boy, while Mistress rewards you."
                    wt_image intro_wife_domme_4_21
                    ivy.c "Cum for me, boy.  Cum for me with your tongue in my cunt."
                    wt_image intro_wife_domme_4_22
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_domme_4_20
                    ivy.c "Good boy.  That was a tasty big load of cum you gave me.  Make me cum again and then I'll be going."
                    wt_image intro_wife_domme_4_19
                    "It takes a little longer than her first orgasm, but a not a lot longer."
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_domme_4_23
                    ivy.c "I hope you don't mind that I took up more of your time than normal today.  Your tongue just felt extra good."
                    "She hurries off, letting you go on with your day."
                    $ ivy.pleasure_her_count += 2
                    $ ivy.orgasm_count += 2
                    $ ivy.blowjob_count += 1
                    $ ivy.swallow_count += 1
                    change player energy by -energy_short
                    orgasm
            call forced_movement(living_room) from _call_forced_movement_961
        # blue-balling scene
        if ivy.domme_you_outfit_count == 6:
            wt_image intro_wife_visit_4_1
            ivy.c "Remove your clothes and wait for me, boy."
            wt_image current_location.image
            "You strip naked and wait for Mistress to reappear."
            wt_image intro_wife_domme_1_1
            ivy.c "Your cock's already hard.  You didn't even need to look at my body to get an erection."
            wt_image intro_wife_domme_1_4
            ivy.c "Was it anticipation of seeing it that turned you on?  I hope so, because that's very flattering."
            wt_image intro_wife_domme_1_2
            ivy.c "I'm going to blue-ball you today, boy.  It'll turn me on to leave you excited but frustrated.  What do you think about that, boy?"
            player.c "If that's what you want, Mistress, then I'm happy to please you."
            wt_image intro_wife_domme_1_5
            ivy.c "Well, getting a nice big erection for me certainly pleases me, boy."
            wt_image intro_wife_domme_1_8
            ivy.c "I like it when you provide me with a nice fat cock to enjoy."
            wt_image intro_wife_domme_1_9
            ivy.c "One I can lick and taste ..."
            wt_image intro_wife_domme_1_10
            ivy.c "... and suck on for as long as I feel like."
            wt_image intro_wife_domme_1_11
            "Fortunately ... or unfortunately ... that turns out to be a very, very long time."
            wt_image intro_wife_domme_1_12
            "Every once in a while she looks up at you and teases the underside of your cock, and you think she's going to stop things there."
            wt_image intro_wife_domme_1_11
            "... then she goes right back to sucking on your dick like it's her favorite flavor lollipop."
            wt_image intro_wife_domme_1_10
            "Finally, there's a reprieve."
            wt_image intro_wife_domme_1_12
            ivy.c "How do your balls feel?"
            wt_image intro_wife_domme_1_13
            player.c "They're absolutely aching, Mistress."
            wt_image intro_wife_domme_1_5
            ivy.c "Mmmmm ... that's exactly how I was hoping you'd feel."
            wt_image intro_wife_domme_1_14
            "She kisses you long and passionately, the feeling of her lips and hot little tongue in your mouth doing nothing to ease the discomfort in your testicles."
            wt_image intro_wife_domme_1_15
            ivy.c "You are absolutely amazing.  I'm going home to fuck my husband until we both cum at least twice.  I'd like to say I'm sorry to be leaving you worked up, but I'm not.  I'm absolutely loving leaving you like this."
            wt_image intro_wife_domme_1_16
            ivy.c "Thank you for being such a good submissive."
            "She unhooks the leash from your cock and leaves, letting you go on with your day."
            change player energy by -energy_short
    wt_image current_location.image
    call character_location_return(ivy) from _call_character_location_return_658
    notify
    return

#Dungeon visit content
label ivy_dungeon_visit:
    $ ivy.training_session()
    wt_image intro_wife_dungeon_1_1
    "She hurries straight past you when she arrives, and goes directly to your dungeon."
    call forced_movement(dungeon) from _call_forced_movement_962
    summon ivy
    wt_image intro_wife_dungeon_1_1
    player.c "In a hurry?"
    ivy.c "If we don't do this immediately, I'll lose my nerve."
    if not ivy.has_tag('first_dungeon_visit_complete'):
        add tags 'first_dungeon_visit_complete' to ivy
        player.c "Okay, then.  Take off your clothes."
        wt_image intro_wife_dungeon_1_2
        ivy.c "Is this going to hurt a lot?  I mean, a lot more than the spankings?"
        player.c "Maybe.  I haven't decided yet.  Finish stripping then get down on the floor and offer yourself to me."
        wt_image intro_wife_dungeon_1_3
        ivy.c "I'm yours, Sir, to do with what you want.  I'm also very, very scared.  I hope you don't want to hurt me very much, Sir."
        player.c "That's only partially true, Ivy.  You wouldn't be here unless some part of you is wondering what it'll feel like if I hurt you very, very much."
        "Her mouth goes dry and her throat tightens, leaving her barely able to squeak out a response."
        ivy.c "Is that what you're going to do with me?"
        player.c "Maybe.  First I'm going to introduce you to some of the fun things I keep in here.  Have you ever been tied up?"
        "Wide-eyed, she shakes her head 'no' as you approach with ropes."
        wt_image intro_wife_dungeon_1_4
        player.c "Now you have.  Let's see what else I have around here to introduce you to."
        if dungeon.has_item(gags):
            wt_image intro_wife_dungeon_1_5
            player.c "How about a ball gag?  Has this pretty mouth of yours ever been silenced with a good gag before?  Don't bother trying to answer, you won't be able to speak in proper words again anyway until I let you."
            wt_image intro_wife_dungeon_1_15
            player.c "Feeling helpless?  You're nodding, that's so cute.  I already knew the answer, but thank you for being obedient and answering even when you can't talk."
            if dungeon.has_item(floggers):
                wt_image intro_wife_dungeon_1_12
                player.c "Do you know what's on the wall behind you?  You do?  Did you see them when you came in?  You did?  Have you been wondering what they'll feel like?  Ahhh, no more nodding?  You're not shaking your head, either, though, so I think maybe you were.  I'll show you."
                wt_image intro_wife_dungeon_1_6
                player.c "Isn't that soft, Ivy?  Now now, I can hear you crying.  Don't worry.  I'm not going to use it on your face, silly.  I'm not even going to use it on your body.  Not today, anyway. "
                wt_image intro_wife_dungeon_1_13
                player.c "I don't need to use a flogger on you to hurt you, do I?"
            else:
                wt_image intro_wife_dungeon_1_11
                player.c "Some dungeons have instruments specially designed to cause pain. Don't be too disappointed that I don't have that type of equipment. I don't need fancy equipment to hurt you, do I?"
            wt_image intro_wife_dungeon_1_14
            "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
            ivy.c "Nn!!  Nn!!  NN!!!"
            wt_image intro_wife_dungeon_1_13
            player.c "Oh come on.  We're in a dungeon, and you're gagged.  No one can hear you anyway.  You may as well scream louder than that into the gag."
            wt_image intro_wife_dungeon_1_14
            "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
            ivy.c "NNNN!!!!  NNNN!!!!  NNNNN!!!!!!"
            wt_image intro_wife_dungeon_1_8
            player.c "That's better.  See how much you can take?  I told you you're made of tough stuff.  Wet stuff, too.  You're aroused enough you can take another set."
            wt_image intro_wife_dungeon_1_14
            "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
            ivy.c "NNNNNNNNNNNNNNN!!!!!!!"
            wt_image intro_wife_dungeon_1_8
            player.c "That's it, let the tears out.  Let me rub between your legs while they flow, you'll feel better."
            wt_image intro_wife_dungeon_1_5
            player.c "No more tears?  I think you're ready for me to take this gag out.  Then when you're up to it, roll over.  I have something for you."
        else:
            if dungeon.has_item(floggers):
                wt_image intro_wife_dungeon_1_6
                player.c "Isn't that soft, Ivy?  Now now, I can hear you crying.  Don't worry.  I'm not going to use it on your face, silly.  I'm not even going to use it on your body.  Not today, anyway.  I don't need to use this on you to hurt you, do I?"
            else:
                extend "  Nothing, really, not anything that I'm ready to use on you, anyway.  I really should invest in some nice basic equipment.  Fortunately, I don't need any fancy equipment to hurt you, do I?"
            wt_image intro_wife_dungeon_1_7
            "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
            ivy.c "Ow!!  OW!!  OW!!!"
            player.c "Oh come on.  We're in a dungeon.  You can scream louder than that."
            "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
            ivy.c "OWWW!!!!  OWWW!!!!  OOWWWW!!!!!!"
            wt_image intro_wife_dungeon_1_8
            player.c "That's better.  See how much you can take?  I told you you're made of tough stuff.  Wet stuff, too.  You're aroused enough you can take another set."
            wt_image intro_wife_dungeon_1_7
            "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
            ivy.c "OOOOWWWWWWWWWWW!!!!!!!"
            wt_image intro_wife_dungeon_1_8
            player.c "That's it, let the tears out.  Let me rub between your legs while they flow, you'll feel better.  When you're up to it, roll over.  I have something for you."
        wt_image intro_wife_dungeon_1_10
        player.c "Good girl.  See how excited you made me?  Doesn't that feel good, knowing how much pleasure you gave me by taking that spanking?"
        wt_image intro_wife_dungeon_1_9
        player.c "That's it, take my cock in your mouth and finish me off."
        wt_image intro_wife_dungeon_1_16
        player.c "[player.orgasm_text]"
        wt_image intro_wife_dungeon_1_4
        player.c "Rest now.  You've been through a lot.  When you're ready, I'll untie you."
        wt_image intro_wife_dungeon_1_2
        "She lies there for a while before rising to her knees.  You remove her ropes and she puts her clothes back on."
        ivy.c "That was intense."
        player.c "Are you sorry you came over?"
        wt_image intro_wife_dungeon_1_1
        ivy.c "No.  I was ... curious is the right word, I guess.  Curious to know what you'd do, how it'd feel, how I'd react."
        player.c "I might do the same thing the next time you come over.  Or I might do something else.  Will you come when I call?"
        ivy.c "I'll think about it."
        "She heads out, leaving you to go on with your day"
        $ ivy.blowjob_count += 1
        $ ivy.swallow_count += 1
        change player energy by -energy_short
        orgasm
        $ ivy.submissive_visit_timer = 5
    else:
        player.c "I thought you had fun last time?"
        wt_image intro_wife_dungeon_1_2
        ivy.c "'Fun' isn't the word I would have used."
        player.c "Yet you're already undressing?"
        wt_image intro_wife_dungeon_1_3
        ivy.c "I know I'm not going to be clothed for this."
        player.c "So undressing and offering yourself to me is your way of staying in control for a few minutes longer?"
        ivy.c "I guess.  I'm not going to have much control in a moment, am I?"
        player.c "None whatsoever.  Does that make you wet?"
        ivy.c "Mostly just scared.  Maybe a little wet.  What are you going to do with me?"
        wt_image intro_wife_dungeon_1_4
        "You truss her up and push her flat on the floor while you decide."
        $ title = "What do you want to do with her?"
        menu:
            "Spank her":
                if dungeon.has_item(gags):
                    wt_image intro_wife_dungeon_1_5
                    player.c "I think you're going to need this in a moment.  Does that scare you?"
                    wt_image intro_wife_dungeon_1_11
                    player.c "You're nodding, that's so cute.  It's okay to be scared.  This is going to hurt, but you'll get through it."
                    wt_image intro_wife_dungeon_1_14
                    "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    ivy.c "Nn!!  Nn!!  NN!!!"
                    wt_image intro_wife_dungeon_1_13
                    player.c "Oh come on.  We're in a dungeon, and you're gagged.  No one can hear you anyway.  You may as well scream louder than that into the gag."
                    wt_image intro_wife_dungeon_1_14
                    "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
                    ivy.c "NNNN!!!!  NNNN!!!!  NNNNN!!!!!!"
                    wt_image intro_wife_dungeon_1_8
                    player.c "That's better.  See how much you can take?  I told you you're made of tough stuff.  Wet stuff, too.  You're aroused enough you can take another set."
                    wt_image intro_wife_dungeon_1_14
                    "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
                    ivy.c "NNNNNNNNNNNNNNN!!!!!!!"
                    wt_image intro_wife_dungeon_1_8
                    player.c "That's it, let the tears out.  Let me rub between your legs while they flow, you'll feel better."
                else:
                    player.c "You have a very cute butt, Ivy.  You know what I like to do with cute butts, don't you?  Only nodding?  Can't you articulate right now?  It's okay, you'll be making sounds in a moment."
                    wt_image intro_wife_dungeon_1_7
                    "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    ivy.c "Ow!!  OW!!  OW!!!"
                    player.c "Oh come on.  We're in a dungeon.  You can scream louder than that."
                    "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
                    ivy.c "OWWW!!!!  OWWW!!!!  OOWWWW!!!!!!"
                    wt_image intro_wife_dungeon_1_8
                    player.c "That's better.  See how much you can take?  I told you you're made of tough stuff.  Wet stuff, too.  You're aroused enough you can take another set."
                    wt_image intro_wife_dungeon_1_7
                    "*SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*  *SMACK!!*"
                    ivy.c "OOOOWWWWWWWWWWW!!!!!!!"
                    wt_image intro_wife_dungeon_1_8
                    player.c "That's it, let the tears out.  Let me rub between your legs while they flow, you'll feel better.  When you're up to it, roll over.  I have something for you."
                $ title = "What now?"
                menu:
                    "Send her home":
                        pass
                    "Have her blow you":
                        wt_image intro_wife_dungeon_1_10
                        player.c "Good girl.  See how excited you made me?  Doesn't that feel good, knowing how much pleasure you gave me by taking that spanking?"
                        wt_image intro_wife_dungeon_1_9
                        player.c "That's it, take my cock in your mouth and finish me off."
                        wt_image intro_wife_dungeon_1_16
                        player.c "[player.orgasm_text]"
                        $ ivy.blowjob_count += 1
                        $ ivy.swallow_count += 1
                        orgasm
                wt_image intro_wife_dungeon_1_4
                player.c "Rest now.  You've been through a lot.  When you're ready, I'll untie you."
                wt_image intro_wife_dungeon_1_2
                "She lies there for a while before rising to her knees.  You remove her ropes and she puts her clothes back on."
                ivy.c "It's always so intense when you do that."
                player.c "Are you sorry you came over?"
                wt_image intro_wife_dungeon_1_1
                ivy.c "No.  I knew you might be hard on me again.  It's a weird thing.  I hate it, but I also ... I'm not sure what the right word is?  Not 'love', not even 'like'.  'Appreciate' maybe, the intensity of how it feels?"
                "She heads out, leaving you to go on with your day"
                change player energy by -energy_short
                $ ivy.submissive_visit_timer = 5
            "Flog her" if dungeon.has_item(floggers):
                wt_image intro_wife_dungeon_2_1
                "You re-tie her into a position that makes it easier to flog her."
                player.c "You see the instruments on the wall behind you?"
                ivy.c "Yes, Sir."
                if not ivy.has_tag('flogged_before'):
                    add tags 'flogged_before' to ivy
                    player.c "It's time you learn what they feel like.  You've been thinking about that, haven't you?"
                    ivy.c "Yes, Sir.  I just hope they don't hurt much more than your hand."
                    wt_image intro_wife_dungeon_2_3
                    "They don't actually.  At least not the floggers.  But you can continue to hit her with the flogger long after your hand gets too sore to keep spanking here, as she's about to find out ... *thwapp*  *thwapp*  *thwapp*"
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "Oh!"
                    player.c "Feels good, doesn't it?"
                    ivy.c "Not good, exactly.  Stingy ... warm ... weird"
                    player.c "I'm sure we can do better than 'weird'."
                    wt_image intro_wife_dungeon_2_3
                    "*thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*"
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "OOOHHHHH"
                    player.c "Now does it feel good?"
                    ivy.c "No!  Yes?  The only thing that exists right now is my ass and ..."
                    player.c "Your ass and pussy?"
                    "She nods."
                    wt_image intro_wife_dungeon_2_3
                    "*THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*"
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "AAHHHHH!!!  THAT  .. THAT ..."
                    player.c "That what, Ivy?  Is the sensation becoming intense?"
                    ivy.c "YES!!!"
                    wt_image intro_wife_dungeon_2_3
                    "*THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*"
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "AAAAHHHHHHH!!!  AAAHHHHH!!!!  PLEASE!!!!"
                    player.c "Please what, Ivy?  Please continue?  Or did you maybe mean 'harder please'?"
                    wt_image intro_wife_dungeon_2_3
                    "*THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*"
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "AAAAHHHHHHH!!!  NOOOO!!!!!"
                    player.c "Had enough?"
                    ivy.c "YESSSSS!!!!!"
                    wt_image intro_wife_dungeon_2_3
                    player.c "Are you sure?  Your pussy still looks wet.  I think you could take another set."
                    wt_image intro_wife_dungeon_2_4
                    ivy.c "NOOOO!!!!!  NO PLEASE!!!  I can't!  I really can't!!  My ass is completely on fire!!!"
                    wt_image intro_wife_dungeon_2_5
                    player.c "And what about your pussy?  Is it also on fire?  Does it need some attention?"
                    ivy.c "OOHHH  ... Yes, please!!"
                    wt_image intro_wife_dungeon_2_6
                    player.c "You want me to fuck this wet, sore, burning pussy of yours?"
                    ivy.c "Yes, Sir!  Please fuck me!!"
                    wt_image intro_wife_dungeon_2_7
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    "That was fast.  Not that you take much longer."
                    player.c "[player.orgasm_text]"
                    wt_image intro_wife_dungeon_1_2
                    player.c "How was that?"
                    ivy.c "Close to both the worst and the best I've ever felt in my life.  When you first entered me it was close to both at almost the same time."
                    $ ivy.orgasm_count += 1
                    $ ivy.sex_count += 1
                    orgasm
                    change player energy by -energy_very_short
                    $ ivy.submissive_visit_timer = 5
                else:
                    player.c "What do you think I should do now?"
                    wt_image intro_wife_dungeon_2_2
                    player.c "That's cute.  You think I should simply let you pleasure me and dispense with the flogging?"
                    ivy.c "Yes, Sir.  The anticipation's been enough.  I don't need you to actually hurt me.  Why don't you just fuck me instead?"
                    $ title = "What do you do?"
                    menu:
                        "Fuck her":
                            wt_image intro_wife_dungeon_2_5
                            player.c "Are you sure you don't want me to use the flogger on you?  It would warm your pussy right up."
                            ivy.c "No, Sir.  Please just fuck me, Sir?  I'm begging you, Sir.  Please use me like your fucktoy and fuck me hard for as long as it amuses you."
                            wt_image intro_wife_dungeon_2_6
                            "It's tough to deny her after such earnest begging."
                            player.c "As long and as hard as I want?  Are you sure that's preferable to the flogger?"
                            ivy.c "Yes, Sir!!  My pussy's yours, Sir.  You use it however you want."
                            wt_image intro_wife_dungeon_2_7
                            "The whole scenario is clearly highly stimulating to Ivy, as you've barely able to start fucking her before she orgasms."
                            ivy.c "OH ... I'M CUMMINNGGG!!!"
                            wt_image intro_wife_dungeon_2_6
                            player.c "Are you finished?  I'd like to start using this pussy that's been given to me."
                            ivy.c "Sorry, Sir!  Yes, Sir.  Please continue, and I'll try to control myself."
                            wt_image intro_wife_dungeon_2_7
                            "You can't be certain, but you think she sneaks a couple of silent orgasms in there while you're fucking her, before you finally reach your own."
                            player.c "[player.orgasm_text]"
                            wt_image intro_wife_dungeon_1_2
                            ivy.c "Thank you for not flogging me, Sir.  Knowing that you might have made the whole experience almost as intense as being flogged, and far more enjoyable."
                            player.c "You know I might flog you next time?"
                            wt_image intro_wife_dungeon_1_1
                            ivy.c "Yes, Sir.  That's a chance I'll just have to take, I guess."
                            $ ivy.orgasm_count += 1
                            $ ivy.sex_count += 1
                            orgasm
                            $ ivy.submissive_visit_timer = 3
                        "Flog her":
                            wt_image intro_wife_dungeon_2_3
                            player.c "I think you're overstating the value of anticipation compared to feeling the real thing"
                            "*thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*  *thwapp*"
                            wt_image intro_wife_dungeon_2_4
                            ivy.c "OOOHHHHH"
                            player.c "See.  That feels nice, doesn't it?"
                            ivy.c "Sort of.  Are you going to stop there?"
                            $ title = "Stop?"
                            menu:
                                "Keep flogging her":
                                    player.c "Don't be silly, Ivy.  We're just getting started."
                                    wt_image intro_wife_dungeon_2_3
                                    "*THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*"
                                    wt_image intro_wife_dungeon_2_4
                                    ivy.c "AAHHHHH!!!  THAT  .. THAT ..."
                                    player.c "That what, Ivy?  Is the sensation becoming intense?"
                                    ivy.c "YES!!!"
                                    wt_image intro_wife_dungeon_2_3
                                    "*THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*  *THWAPP*"
                                    wt_image intro_wife_dungeon_2_4
                                    ivy.c "AAAAHHHHHHH!!!  AAAHHHHH!!!!  PLEASE!!!!"
                                    player.c "Please what, Ivy?  Please continue?  Or did you maybe mean 'harder please'?"
                                    $ title = "What do you think she meant?"
                                    menu:
                                        "Flog her harder":
                                            player.c "I think you want to be flogged harder."
                                            wt_image intro_wife_dungeon_2_3
                                            "*THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*  *THWAPP!!*"
                                            wt_image intro_wife_dungeon_2_4
                                            ivy.c "AAAAHHHHHHH!!!  NOOOO!!!!!"
                                            player.c "Had enough?"
                                            ivy.c "YESSSSS!!!!!"
                                            wt_image intro_wife_dungeon_2_3
                                            player.c "Are you sure?  Your pussy still looks wet.  I think you could take another set."
                                            wt_image intro_wife_dungeon_2_4
                                            ivy.c "NOOOO!!!!!  NO PLEASE!!!  I can't!  I really can't!!  My ass is completely on fire!!!"
                                            "She's reach her limit.  What now?"
                                            $ title = "What now?"
                                            menu:
                                                "Fuck her":
                                                    player.c "And what about your pussy?  Is it also on fire?  Does it need some attention?"
                                                    ivy.c "OOHHH  ... Yes, please!!"
                                                    wt_image intro_wife_dungeon_2_6
                                                    player.c "You want me to fuck this wet, sore, burning pussy of yours?"
                                                    ivy.c "Yes, Sir!  Please fuck me!!"
                                                    wt_image intro_wife_dungeon_2_7
                                                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                                                    "That was fast.  Not that you take much longer."
                                                    player.c "[player.orgasm_text]"
                                                    wt_image intro_wife_dungeon_1_2
                                                    player.c "How do feel?"
                                                    ivy.c "Like you took me to hell and then to heaven and now I want to punch you and kiss you and tell you to 'fuck off, asshole' and also say 'thank you, Sir'."
                                                    player.c "I'll take the kiss and the thank you."
                                                    wt_image intro_wife_dungeon_1_1
                                                    ivy.c "Yes, Sir!  Thank you for the heaven part of that round trip, Sir.  Here's your kiss, you asshole."
                                                    $ ivy.orgasm_count += 1
                                                    $ ivy.sex_count += 1
                                                    orgasm
                                                    change player energy by -energy_very_short
                                                    $ ivy.submissive_visit_timer = 4
                                                "Let her go":
                                                    wt_image intro_wife_dungeon_1_2
                                                    player.c "How do feel?"
                                                    ivy.c "Like I wish that I'd begged you to fuck me before you untied.  Now I just feel drained, like I need to go sleep for a week to recover."
                                                    change player energy by -energy_very_short
                                                    $ ivy.submissive_visit_timer = 6
                                        "Stop flogging her and start fucking her":
                                            player.c "Did you want me to stop flocking you and start fucking you?"
                                            wt_image intro_wife_dungeon_2_5
                                            ivy.c "YES!!!  Yes please, Sir!!  Please fuck me now, Sir!"
                                            wt_image intro_wife_dungeon_2_6
                                            ivy.c "OHH!!  Thank you, Sir!"
                                            "Despite her thank you, it takes a while for Ivy to really warm up to the fucking.  Her body is still processing the flogging, and needs to deal with that before she can really enjoy the post-flogging sex."
                                            wt_image intro_wife_dungeon_2_7
                                            "Even at that, she never manages to cum, although she does groan loudly when you eventually do."
                                            player.c "[player.orgasm_text]"
                                            ivy.c "OHH!!!"
                                            wt_image intro_wife_dungeon_1_2
                                            ivy.c "Wow.  That one left me feeling ... I'm not sure what.  It was like I was on a tipping point and just left hanging there."
                                            player.c "Are you disappointed?"
                                            wt_image intro_wife_dungeon_1_1
                                            ivy.c "No, Sir.  I'm just feeling a lot of things right now that I need time to process, I think."
                                            $ ivy.sex_count += 1
                                            orgasm
                                            $ ivy.submissive_visit_timer = 5
                                        "Stop and let her go":
                                            ivy.c "Wow.  That one left me feeling ... I'm not sure what.  It was like I was on a tipping point and just left hanging there."
                                            player.c "Are you disappointed?"
                                            wt_image intro_wife_dungeon_1_1
                                            ivy.c "No, Sir.  I'm just feeling a lot of things right now that I need time to process, I think."
                                            change player energy by -energy_very_short
                                            $ ivy.submissive_visit_timer = 5
                                "Stop and fuck her":
                                    wt_image intro_wife_dungeon_2_5
                                    player.c "Do you want me to stop?"
                                    ivy.c "Yes, Sir.  I'd like you to stop flogging me and start fucking me."
                                    wt_image intro_wife_dungeon_2_6
                                    ivy.c "Oh!  That feels good, Sir!"
                                    wt_image intro_wife_dungeon_2_7
                                    "Having her bum warmed up with a light flogging is clearly highly stimulating to Ivy, as you've barely able to start fucking her before she orgasms."
                                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                                    wt_image intro_wife_dungeon_2_6
                                    player.c "That was quick.  Maybe I should flog you before every fuck?"
                                    ivy.c "Whatever you want to do with me is fine by me, Sir."
                                    wt_image intro_wife_dungeon_2_7
                                    "That's more earnestly submissive than Ivy normally gets.  The sound of her submission combined with the warm tightness of her pussy quickly takes you over the edge."
                                    player.c "[player.orgasm_text]"
                                    wt_image intro_wife_dungeon_1_2
                                    ivy.c "Thank you for only flogging me gently, Sir."
                                    player.c "You know I might flog you much harder and much longer next time?"
                                    wt_image intro_wife_dungeon_1_1
                                    ivy.c "Yes, Sir.  That's a chance I'll just have to take, I guess."
                                    $ ivy.orgasm_count += 1
                                    $ ivy.sex_count += 1
                                    orgasm
                                    $ ivy.submissive_visit_timer = 3
                                "Stop and let her go":
                                    wt_image intro_wife_dungeon_1_2
                                    ivy.c "Thank you for only flogging me gently, Sir."
                                    player.c "You know I might flog you much harder and much longer next time?"
                                    wt_image intro_wife_dungeon_1_1
                                    ivy.c "Yes, Sir.  That's a chance I'll just have to take, I guess."
                                    change player energy by -energy_very_short
                                    $ ivy.submissive_visit_timer = 3
            "Have her blow you":
                player.c "Sit up."
                wt_image intro_wife_dungeon_1_17
                player.c "Get your mouth on my cock."
                wt_image intro_wife_dungeon_1_10
                player.c "Should I hurt you first, before you suck me off?"
                ivy.c "No, Sir!  Thank you for not hurting me first.  I'll happily suck your cock for you."
                wt_image intro_wife_dungeon_1_17
                player.c "Do a good job.  If I get bored, I might have to hurt you to amuse myself."
                wt_image intro_wife_dungeon_1_9
                "She sucks your dick with enthusiasm.  You alternate between letting her pleasure your dick as best she can from her tied position ..."
                wt_image intro_wife_dungeon_1_17
                "... and holding her head still as you face-fuck her."
                wt_image intro_wife_dungeon_1_9
                "You alternate back and forth until you're ready to cum."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image intro_wife_dungeon_1_16
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_dungeon_1_2
                        $ ivy.swallow_count += 1
                    "On her face":
                        wt_image intro_wife_dungeon_1_10
                        player.c "Hold still."
                        wt_image intro_wife_bj_1_20
                        player.c "[player.orgasm_text]"
                        $ ivy.facial_count += 1
                player.c "Are you maybe a little bit disappointed I wasn't harder on you?"
                ivy.c "Not at all!  The anticipation that you might hurt me was almost as intense as you actually hurting me, put without the discomfort.  I'd prefer being treated like your personal fucktoy anytime."
                $ ivy.submissive_visit_timer = 3
                $ ivy.blowjob_count += 1
                orgasm
            "Gag and play with her" if dungeon.has_item(gags):
                wt_image intro_wife_dungeon_1_5
                player.c "You look cute tied up, but you look even cuter and more helpless gagged."
                wt_image intro_wife_dungeon_1_18
                player.c "How does it feel, being tied up and helpless?  I can do anything I want to you right now.  For example, I could squeeze your tit, nice and hard.  Do you like that?"
                ivy.c "Nnnn"
                player.c "Is that a yes?  It's so hard to tell after I've taken your voice away.  It's almost like what you like or don't like no longer matters."
                wt_image intro_wife_dungeon_1_19
                player.c "Take tickling.  Do you love it?  Do you hate it?  I don't know, and it doesn't matter.  I can tickle you as long as I like."
                ivy.c "Nnnnnn"
                wt_image intro_wife_dungeon_1_20
                player.c "On the other hand, when I tickle you down here, I can tell you love it even when you can't talk.  Your sopping pussy gives your secret away, and it's not just from being touched there, is it?  It's from being helpless."
                wt_image intro_wife_dungeon_1_13
                player.c "So what should I do with you, helpless?"
                ivy.c "Nnnn"
                player.c "That's cute.  I could guess what you just asked for, but I think it's more fun if I just do whatever I want with you."
                $ title = "What do you do with her?"
                menu:
                    "Tickle her":
                        wt_image intro_wife_dungeon_1_18
                        player.c "Which feels better to you, I wonder?  Having your tit squeezed ..."
                        ivy.c "Nnnn"
                        wt_image intro_wife_dungeon_1_19
                        player.c "... or your tummy tickled."
                        ivy.c "Nnnnnn"
                        wt_image intro_wife_dungeon_1_18
                        player.c "Maybe if I do it harder?"
                        ivy.c "NNNNN"
                        wt_image intro_wife_dungeon_1_19
                        ivy.c "NNNNNNNNN"
                        wt_image intro_wife_dungeon_1_5
                        player.c "That's a pretty strong reaction.  I think I have my answer, don't I, helpless?"
                        wt_image intro_wife_dungeon_1_19
                        ivy.c "NNNNNNNNN  ...  NNNNNNNNN  ...  NNNNNNNNN"
                        "You continue to tickle her until you've had enough fun watching her squirm and listening to her futile attempts to communicate through her gag."
                        wt_image intro_wife_dungeon_1_2
                        ivy.c "Oh, wow!!  That was torture!"
                        player.c "I guess that means you hated it."
                        wt_image intro_wife_dungeon_1_1
                        ivy.c "Why should I tell you know, since you didn't care before?  Whichever I say you'll just use against me next time, anyway."
                        $ ivy.submissive_visit_timer = 4
                        change player energy by -energy_very_short
                    "Finger her":
                        wt_image intro_wife_dungeon_1_20
                        "You slide your thumb inside her and stroke gently in and out, gradually picking up pace and alternating the strokes with little flicks of your fingers against her sex and clit."
                        "The increased flow of fluids, the flush on her face, and the pace of her breathing all tell you she's getting very close."
                        player.c "Be a good girl, Ivy, and tell me exactly what you're doing on the end of my fingers."
                        ivy.c "NN ... NNN NNNNNNNNNN!!!"
                        wt_image intro_wife_dungeon_1_15
                        player.c "Such a good girl.  You can rest and enjoy your bonds for a little while.  Sit up when you're ready and I'll untie you."
                        wt_image intro_wife_dungeon_1_2
                        ivy.c "Thank you for that, Sir.  That felt amazing."
                        player.c "I may not be as gentle with you next time."
                        wt_image intro_wife_dungeon_1_1
                        ivy.c "I know, Sir.  I'll take my chances!"
                        $ ivy.pleasure_her_count += 1
                        $ ivy.orgasm_count += 1
                        $ ivy.submissive_visit_timer = 3
                        change player energy by -energy_very_short
                    "Fuck her":
                        wt_image intro_wife_dungeon_1_8
                        player.c "Although I think it's pretty clear what your body wants me to do with you."
                        wt_image intro_wife_dungeon_1_21
                        player.c "Something like this, I think."
                        ivy.c "NNN"
                        wt_image intro_wife_dungeon_1_22
                        "She bucks her hips back against you as you enter her, behavior you encourage with a few hard swats to her flank ... *SMACK*  *SMACK*  *SMACK*"
                        ivy.c "NNN  NNN  NNNNN"
                        wt_image intro_wife_dungeon_1_23
                        "Before long, her whole body is shuddering against you as she screams into her gag."
                        ivy.c "NN ... NNN NNNNNNNNNN!!!"
                        wt_image intro_wife_dungeon_1_24
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_dungeon_1_11
                        "You leave your well-fucked submissive to enjoy the feeling of her bonds for a little while longer.  When she looks like she's recovered from her fucking, you untie her."
                        wt_image intro_wife_dungeon_1_2
                        ivy.c "Thank you for that, Sir.  That felt amazing."
                        player.c "I may not be as gentle with you next time."
                        wt_image intro_wife_dungeon_1_1
                        ivy.c "I know, Sir.  I'll take my chances!"
                        $ ivy.sex_count += 1
                        $ ivy.orgasm_count += 1
                        orgasm
                        $ ivy.submissive_visit_timer = 3
            "Bind and fuck her":
                if dungeon.has_item(gags):
                    wt_image intro_wife_dungeon_1_5
                    player.c "You look so cute helpless, I can't help but want to make you even more helpless.  Like taking your voice away."
                    wt_image intro_wife_dungeon_3_1
                    player.c "Or tying you spread-eagled."
                    wt_image intro_wife_dungeon_3_2
                    player.c "I imagine you feel extremely vulnerable right now."
                    ivy.c "Nn nnn"
                    wt_image intro_wife_dungeon_3_1
                    player.c "I'll leave you alone to enjoy the experience."
                    "You let her wait there for a while, wondering what you're going to do with her when you return."
                    wt_image intro_wife_dungeon_3_2
                    player.c "Let's see how you're doing, Ivy."
                    wt_image intro_wife_dungeon_3_3
                    player.c "You're wet.  Whatever you've been thinking about, it probably wasn't this."
                    "*smack*"
                    ivy.c "NNN"
                    player.c "Or maybe it was?  Have you been thinking about how much you hoped I'd come back and spank your pussy?"
                    "*smack*"
                    ivy.c "NNNN"
                    player.c "That's so cute.  I think you have been."
                    $ ivy.temporary_count = 0
                    $ ivy.random_number = 0
                    $ title = "Keep spanking her?"
                    menu menu_ivy_dungeon_bound_gagged_spank_menu:
                        "Yes":
                            "*smack*"
                            ivy.c "NNNN"
                            $ ivy.temporary_count += 1
                            $ ivy.random_number = ivy.temporary_count
                            while ivy.random_number > 0:
                                extend "N"
                                $ ivy.random_number -= 1
                        "That's enough":
                            pass
                    wt_image intro_wife_dungeon_3_4
                    player.c "I think that's enough pleasure for your pussy for one day.  Time for me to have my fun.  Let's get your gag out."
                    ivy.c "That ..."
                    wt_image intro_wife_dungeon_3_5
                    player.c "Shush.  You don't need to thank me for spanking your pussy before I fuck you.  Getting to fuck such a well-lubed cunt is thanks enough."
                else:
                    wt_image intro_wife_dungeon_1_6
                    player.c "Let's get you feeling more vulnerable."
                    wt_image intro_wife_dungeon_3_4
                    "You keep her head covered until you've bound her spreadeagle, then remove the hood."
                    player.c "How does this feel?"
                    ivy.c "Scary.  Like you can do anything you want to me."
                    player.c "What are you hoping I do?"
                    ivy.c "I want you to fuck me, Sir.  Please fuck me.  Please stick your big dick in me and fuck me silly, Sir."
                    wt_image intro_wife_dungeon_3_5
                    player.c "Shhh.  You had me at 'big dick'."
                wt_image intro_wife_dungeon_3_6
                player.c "Are you going to cum for me, from being fucked in this position, Ivy?"
                ivy.c "I ... I'm not sure ..."
                player.c "What if I rub your clit while I fuck you?"
                ivy.c "OH FUCK YES!!!"
                wt_image intro_wife_dungeon_3_7
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                wt_image intro_wife_dungeon_3_6
                player.c "Such a good girl.  You can have my cum now, if you want it?"
                ivy.c "Yes!  Yes, please!!"
                wt_image intro_wife_dungeon_3_8
                "You pull out and shoot your load up and over her."
                player.c "[player.orgasm_text]"
                wt_image intro_wife_dungeon_3_9
                ivy.c "Wow!  I just need a moment to recover, Sir."
                wt_image intro_wife_dungeon_1_2
                "When she's had her moment, you unbind her and she cleans up and gets back into her clothes."
                ivy.c "Thank you for fucking me, Sir.  I enjoyed that."
                if dungeon.has_item(gags):
                    player.c "What about the pussy spanking?  Are you going to thank me for that?"
                    "She thinks about it, but stays silent."
                $ ivy.orgasm_count += 1
                $ ivy.sex_count += 1
                orgasm
                $ ivy.submissive_visit_timer = 3
            "Nothing more today (send her home)":
                "You busy yourself with other things as she waits.  When you decide you have other things you'd rather do than play with her, you untie her."
                wt_image intro_wife_dungeon_1_3
                "She's confused as you send her home, both by your reaction and hers.  She's relieved that you didn't hurt her, and disappointed at the same time."
                change player energy by -energy_very_short
                $ ivy.submissive_visit_timer = 1
    call character_location_return(ivy) from _call_character_location_return_659
    call forced_movement(living_room) from _call_forced_movement_963
    wt_image current_location.image
    notify
    return

#Sex visit content
label ivy_sex_visit:
    $ ivy.temporary_count = 1
    wt_image intro_wife_visit_3_2
    $ title = "What type of sex do you want?"
    menu:
        "Pleasure her":
            wt_image intro_wife_visit_3_5
            player.c "You look very tasty today, Ivy."
            wt_image intro_wife_visit_3_6
            ivy.c "Thank you!  You look pretty good yourself."
            wt_image intro_wife_visit_3_7
            player.c "You misunderstood.  You literally look tasty ..."
            wt_image intro_wife_visit_3_8
            player.c " ... tasty enough to nibble on."
            wt_image intro_wife_visit_3_9
            ivy.c "Oh!  Mmmmmm."
            wt_image intro_wife_visit_3_10
            player.c "Turns out you're too tasty just to nibble on ..."
            wt_image intro_wife_visit_3_11
            player.c "... I'm going to eat you, instead."
            if ivy.has_tag('dommed_you'):
                wt_image intro_wife_visit_3_14
                ivy.c "Mmmmm.  That's it!  Eat me the way I've taught you to."
            wt_image intro_wife_visit_3_12
            "As you eat, her body supplies you with a steadily increasing stream of sticky juices to drink ..."
            wt_image intro_wife_visit_3_13
            "... followed by a gush."
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_15
            ivy.c "Invite me over for a booty call anytime!"
            wt_image intro_wife_visit_3_30
            "She finishes re-dressing, then heads out, leaving you to go on with your day."
            $ ivy.pleasure_her_count += 1
            $ ivy.orgasm_count += 1
            change player energy by -energy_short
        "Blow job":
            wt_image intro_wife_visit_3_15
            "Ivy watches as you take out your cock."
            wt_image intro_wife_visit_3_16
            if ivy.has_tag('bj_training'):
                ivy.c "I suppose you'd like me to deal with that ..."
                wt_image intro_wife_visit_3_17
                ivy.c "... the way a well-trained cocksucker should?"
                wt_image intro_wife_visit_3_22
                "She drops to her knees and opens her mouth ..."
                wt_image intro_wife_visit_3_23
                "... then puts your balls in it."
                wt_image intro_wife_visit_3_24
                "She continues to suckle your sack, waiting for a sign that you're ready for her to move on."
                wt_image intro_wife_visit_3_25
                "When you are, she pleasures the sides of your shaft with her lips and tongue ..."
                wt_image intro_wife_visit_3_26
                "... before taking your cock into her mouth."
                wt_image intro_wife_visit_3_27
                "Her pretty head bobbing up and down your shaft as her tongue licks the sensitive underside of your cockhead soon has you ready to cum."
                wt_image intro_wife_visit_3_22
                "Sensing your pending orgasm, Ivy removes her mouth from your cock and waits to see where you want to cum."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image intro_wife_visit_3_21
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_3_15
                        $ ivy.swallow_count += 1

                    "On her face":
                        wt_image intro_wife_visit_3_28
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_3_29
                        $ ivy.facial_count += 1
            else:
                ivy.c "I suppose you'd like me to deal with that?"
                wt_image intro_wife_visit_3_18
                "She drops to her knees and takes your cock in her mouth."
                wt_image intro_wife_visit_3_17
                "With her hand, lips and tongue ..."
                wt_image intro_wife_visit_3_20
                "... she soon coaxes the sperm from your balls."
                wt_image intro_wife_visit_3_21
                player.c "[player.orgasm_text]"
                wt_image intro_wife_visit_3_15
                $ ivy.swallow_count += 1
            ivy.c "Maybe next time we can do something else with that big dick of yours?"
            wt_image intro_wife_visit_3_30
            "She pulls herself together, then heads out, leaving you to go on with your day."
            $ ivy.blowjob_count += 1
            orgasm
        "Missionary":
            wt_image intro_wife_visit_3_31
            if ivy.has_tag('domme'):
                player.c "Lie back, Mistress.  I'd like permission to fuck you."
            else:
                player.c "Lie back, sexy.  I want to fuck you."
            wt_image intro_wife_visit_3_32
            ivy.c "Absolutely!"
            wt_image intro_wife_visit_3_33
            "She gasps as you enter her ..."
            ivy.c "Oh!"
            wt_image intro_wife_visit_3_34
            "... and then moans as you start to fuck her rapidly wetting snatch."
            ivy.c "Mmmmmmm"
            wt_image intro_wife_visit_3_35
            ivy.c "Mmmm ... that feels so good!"
            if ivy.domme_comfort > 1:
                wt_image intro_wife_visit_3_36
                ivy.c "Faster!  Fuck me faster!!"
            else:
                wt_image intro_wife_visit_3_37
                ivy.c "Oh!  What you're doing feels so nice.  Could you please go faster?"
            wt_image intro_wife_visit_3_38
            "You do, and soon bring you both over the edge."
            wt_image intro_wife_visit_3_39
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            player.c "[player.orgasm_text]"
            wt_image intro_wife_visit_3_6
            ivy.c "Mmmmm.  That felt great!"
            wt_image intro_wife_visit_3_30
            "When she's pulled herself together, she heads out and leaves you to continue your day."
            $ ivy.sex_count += 1
            $ ivy.orgasm_count += 1
            orgasm
        "Doggy style":
            wt_image intro_wife_visit_3_31
            if ivy.has_tag('domme'):
                player.c "Mistress, could I please look at your naked body while I fuck you from behind?"
            else:
                player.c "You look great, but you'd look even better naked and facing away from me."
            wt_image intro_wife_visit_3_40
            ivy.c "Okay"
            wt_image intro_wife_visit_3_41
            "She's a little tight, and you need to be slow and careful as you push into her ..."
            wt_image intro_wife_visit_3_42
            "... but she soon moistens and stretches as you slide your cock in and out of her."
            if ivy.domme_comfort > 1:
                wt_image intro_wife_visit_3_43
                ivy.c "Mmmm.  That's good.  Faster now!  Fuck me faster!!"
            else:
                wt_image intro_wife_visit_3_44
                ivy.c "Mmmm.  That feels so nice.  You can go faster, if you want?"
            wt_image intro_wife_visit_3_45
            "You do, and you can feel her passion growing."
            wt_image intro_wife_visit_3_46
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_42
            "So are you."
            player.c "[player.orgasm_text]"
            wt_image intro_wife_visit_3_40
            ivy.c "Well, that was fun!"
            wt_image intro_wife_visit_3_30
            "After a quick kiss, she heads out and leaves you to continue your day."
            $ ivy.sex_count += 1
            $ ivy.orgasm_count += 1
            orgasm
        "Cowgirl":
            wt_image intro_wife_visit_3_31
            if ivy.has_tag('domme'):
                player.c "I've got a nice hard pole from looking at you, if Mistress would like to ride it?"
            else:
                player.c "How about you perch this sexy body of yours on top of me?"
            wt_image intro_wife_visit_3_10
            ivy.c "Mmmm.  Sounds nice!"
            wt_image intro_wife_visit_3_47
            "You guide her onto your shaft, facing towards you ..."
            wt_image intro_wife_visit_3_48
            "... enjoying the feeling of her warm, tight snatch stretching to accommodate your girth."
            wt_image intro_wife_visit_3_49
            "In this position, Ivy's able to control the pace of the fucking ..."
            wt_image intro_wife_visit_3_50
            "... lifting up to the very tip of your cock ..."
            wt_image intro_wife_visit_3_51
            "... then slamming down hard to the base."
            wt_image intro_wife_visit_3_52
            "Steadily quickening the speed at which she rides your cock, she soon fucks first herself ..."
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_53
            "... then you to orgasm."
            player.c "[player.orgasm_text]"
            wt_image intro_wife_visit_3_6
            ivy.c "Thanks for the ride!"
            wt_image intro_wife_visit_3_30
            "She heads out and leaves you to continue your day."
            $ ivy.sex_count += 1
            $ ivy.orgasm_count += 1
            orgasm
        "Reverse Cowgirl":
            wt_image intro_wife_visit_3_31
            if ivy.has_tag('domme'):
                player.c "I've got a nice hard pole from looking at you, if Mistress would like to ride it?"
            else:
                player.c "How about you perch this sexy body of yours on top of me?"
            wt_image intro_wife_visit_3_10
            ivy.c "Mmmm.  Sounds nice!"
            wt_image intro_wife_visit_3_54
            "You guide her onto your shaft, facing away from you ..."
            wt_image intro_wife_visit_3_55
            "... enjoying the feeling of her warm, tight snatch stretching to accommodate your girth."
            wt_image intro_wife_visit_3_56
            "In this position, Ivy's able to control the pace of the fucking ..."
            wt_image intro_wife_visit_3_57
            "... riding your cock up and down ..."
            wt_image intro_wife_visit_3_58
            "... faster and faster ..."
            wt_image intro_wife_visit_3_59
            "... until she fucks first herself ..."
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_60
            "... then you to orgasm."
            player.c "[player.orgasm_text]"
            wt_image intro_wife_visit_3_6
            ivy.c "Thanks for the ride!"
            wt_image intro_wife_visit_3_30
            "She heads out and leaves you to continue your day."
            $ ivy.sex_count += 1
            $ ivy.orgasm_count += 1
            orgasm
        "Adventurous sex" if ivy.has_tag('had_adventurous_sex'):
            wt_image intro_wife_visit_3_3
            player.c "Feeling adventurous, Ivy?"
            wt_image intro_wife_visit_3_16
            ivy.c "Sure!  Feeling strong enough to hold me up?"
            wt_image intro_wife_sex_1_1
            player.c "I'll take my lead from your hard nipples.  I think they're firm enough you could balance on them."
            wt_image intro_wife_sex_1_2
            ivy.c "Mmmm.  If you keep that up, I'll be cumming before you even get your cock in me."
            wt_image intro_wife_sex_1_3
            player.c "I'd rather feel you cumming with my cock inside you.  Hold on."
            wt_image intro_wife_sex_1_4
            ivy.c "OH!!"
            wt_image intro_wife_sex_1_6
            player.c "Ready?"
            wt_image intro_wife_sex_1_5
            ivy.c "Yes!"
            wt_image intro_wife_sex_1_7
            player.c "Here we go."
            wt_image intro_wife_sex_1_9
            ivy.c "OOHH!!!"
            wt_image intro_wife_sex_1_10
            ivy.c "Oh wow!!!  I love fucking you like this!"
            wt_image intro_wife_sex_1_11
            "You hold her in position as she does just that, moving her hips up and down your shaft, faster and faster."
            wt_image intro_wife_sex_1_10
            player.c "This feels great, but you aren't going to cum in this position, are you?"
            wt_image intro_wife_sex_1_11
            ivy.c "That's okay.  As long as it's feeling good for you, I don't mind."
            $ title = "What do you do?"
            menu:
                "Cum like this":
                    wt_image intro_wife_sex_1_9
                    ivy.c "Oh wow!!  Hold me just like that.  I'm going to make you cum!!"
                    wt_image intro_wife_sex_1_11
                    player.c "[player.orgasm_text]"
                "Change to a position she can cum in, too":
                    wt_image intro_wife_sex_1_12
                    player.c "No way.  I want to feel you climax on my cock.  Get ready.  Down you go."
                    wt_image intro_wife_sex_1_13
                    ivy.c "OHHH!!"
                    wt_image intro_wife_sex_1_14
                    ivy.c "OHH WOW!!!!  It's crazy how deep you get into me like this!!"
                    wt_image intro_wife_sex_1_15
                    player.c "Wait 'til I turn around."
                    wt_image intro_wife_sex_1_16
                    ivy.c "Oh my god.  This is so weird, but hot, too!"
                    wt_image intro_wife_sex_1_19
                    ivy.c "OHHHH ... It feels like you're going to split me in two!"
                    wt_image intro_wife_sex_1_17
                    player.c "Do you need me to go slower?"
                    ivy.c "No!  Keep pounding me!!"
                    wt_image intro_wife_sex_1_18
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_sex_1_19
                    "She's not the only one."
                    player.c "[player.orgasm_text]"
                    $ ivy.orgasm_count += 1
            wt_image intro_wife_visit_3_61
            ivy.c "You're a lot of fun!  This was like a booty call and yoga session in one!"
            wt_image intro_wife_visit_3_30
            "She heads out and let's you get on with your day."
            $ ivy.sex_count += 1
            orgasm
        "Anal" if ivy.anal_count > 0:
            wt_image intro_wife_visit_3_3
            player.c "Show me your tits, Ivy."
            wt_image intro_wife_visit_3_73
            ivy.c "Okay.  Like what you see?"
            wt_image intro_wife_visit_3_74
            player.c "I do.  Let me see your ass now."
            wt_image intro_wife_visit_3_75
            player.c "There's your problem."
            wt_image intro_wife_visit_3_76
            ivy.c "What problem?"
            wt_image intro_wife_visit_3_77
            player.c "Your ass is so cute, it's irresistible."
            wt_image intro_wife_visit_3_78
            ivy.c "Is that your way of telling me I'm going home with a sore butt?"
            wt_image intro_wife_anal_1_7
            "She is, but it's best she not go home too sore, so you lube her rosebud up well before inserting your cock ..."
            wt_image intro_wife_anal_1_8
            "... and pushing yourself inside."
            ivy.c "Oh!"
            wt_image intro_wife_anal_1_9
            if ivy.has_tag('anal_orgasm'):
                "When her butthole has stretched enough to accommodate your girth, you lift her up and position her on top of you."
                wt_image intro_wife_anal_1_10
                "She shoves some fingers into her snatch and frigs herself as you bounce her tight ass up and down your shaft until you both cum."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
                $ ivy.orgasm_count += 1
            else:
                "When her butthole has stretched enough to accommodate your girth, you lift her up and bounce her tight ass up and down your shaft until you cum."
            player.c "[player.orgasm_text]"
            wt_image intro_wife_visit_3_61
            ivy.c "Maybe fuck my pussy next time?  I'm going to be walking funny for the rest of the day after having your big tool back there."
            wt_image intro_wife_visit_3_30
            "With a slightly awkward gait, she leaves, letting you go on with your day."
            $ ivy.anal_count += 1
            orgasm
        "Watch her masturbate" if ivy.test('submission', 20):
            wt_image intro_wife_visit_3_2
            player.c "You still have your clothes on."
            wt_image intro_wife_visit_3_40
            ivy.c "So do you."
            wt_image intro_wife_visit_3_72
            ivy.c "And you still have your clothes on?"
            player.c "I'm just watching today."
            if ivy.masturbation_count > 0:
                if ivy.has_tag('stripped_for_you'):
                    wt_image intro_wife_visit_3_63
                    ivy.c "You wanted me to do a strip tease?  You didn't tell me."
                    player.c "Not that.  I want to watch you touch yourself."
                wt_image intro_wife_visit_3_62
                ivy.c "What do you mean?"
                player.c "I want you to sit down, spread your legs, and play with yourself until you make yourself cum."
            wt_image intro_wife_visit_3_64
            ivy.c "I could have stayed at home and played with myself."
            wt_image intro_wife_visit_3_61
            player.c "That wouldn't have been nearly as much fun for me.  Or for you."
            if ivy.masturbation_count > 0:
                wt_image intro_wife_visit_3_65
                ivy.c "It'll be embarrassing to touch myself while you watch."
                player.c "That makes it even more fun."
                wt_image intro_wife_visit_3_66
                ivy.c "I'm not sure I can even make myself cum with you watching."
                player.c "Just keep thinking about how embarrassing it is to be touching yourself with an audience."
            else:
                wt_image intro_wife_visit_3_66
                ivy.c "I still find this embarrassing."
                player.c "That makes it even more fun."
            wt_image intro_wife_visit_3_67
            "Ivy rubs her fingers across her sex, gently at first, then gradually with more intensity."
            wt_image intro_wife_visit_3_68
            "In time, she closes her eyes and slips her fingers inside.  The smell of her arousal wafts over to you as her fingers move faster and faster, and you know she's getting close."
            player.c "Ivy, look at me."
            wt_image intro_wife_visit_3_69
            player.c "Make yourself cum for me, Ivy."
            wt_image intro_wife_visit_3_70
            ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_71
            ivy.c "Okay, that felt nice.  But I'd still rather have your fingers in me than mine.  Maybe next time you can do more than watch?"
            wt_image intro_wife_visit_3_30
            "She pulls herself together and leaves you to continue your day."
            $ ivy.masturbation_count += 1
            change player energy by -energy_very_short
        "Nothing right now":
            $ ivy.temporary_count = 0
    if ivy.temporary_count == 1:
        $ ivy.temporary_count = 0
        call ivy_send_home from _call_ivy_send_home
    return

# Strip visit content
label ivy_strip_visit:
    $ ivy.training_session()
    wt_image intro_wife_visit_2_2
    ivy.c "Part of me is still surprised that you and my husband still like watching me do this."
    wt_image intro_wife_visit_2_3
    ivy.c "Not that I'm complaining."
    wt_image intro_wife_visit_2_4
    if ivy.has_tag('first_stage_strip'):
        ivy.c "In some ways, it's even more flattering than the applause of the crowd when I'm up on stage."
    else:
        ivy.c "It's very flattering."
    wt_image intro_wife_visit_2_5
    ivy.c "You've both seen my middle-aged body up close and personal."
    wt_image intro_wife_visit_2_6
    ivy.c "It's not like I'm revealing anything secret."
    wt_image intro_wife_visit_2_7
    ivy.c "Or like this is a teenager body that you wouldn't mind looking at no matter how many times you see it."
    wt_image intro_wife_visit_2_8
    ivy.c "So the fact that you're watching intently as I strip for you ..."
    wt_image intro_wife_visit_2_9
    ivy.c "... and that you seem to enjoy what you see ..."
    wt_image intro_wife_visit_2_10
    ivy.c "... makes me want to keep stripping ..."
    wt_image intro_wife_visit_2_11
    ivy.c "... and teasing ..."
    wt_image intro_wife_visit_2_12
    ivy.c "... and showing you more."
    call ivy_strip_visit_end from _call_ivy_strip_visit_end
    return

label ivy_strip_visit_end:
    $ ivy.temporary_count = 1
    wt_image intro_wife_visit_2_13
    ivy.c "Did you like that?"
    wt_image intro_wife_visit_2_14
    $ title = "What do you tell her?"
    menu:
        "You were okay":
            wt_image intro_wife_visit_2_10
            ivy.c "Ha!"
            wt_image intro_wife_visit_2_4
            ivy.c "Just okay?"
            wt_image intro_wife_visit_2_15
            ivy.c "I think I believe this bulge between your legs more than I believe you."
            wt_image intro_wife_visit_2_3
            ivy.c "No kiss for you today.  I save those for appreciative audiences.  Call me again when you're ready to be one.  Bye!"
        "You're amazing":
            wt_image intro_wife_visit_2_8
            ivy.c "Thank you.  That was the right answer!"
            wt_image intro_wife_visit_2_15
            ivy.c "That earns you another show the next time you want to call me over."
            wt_image intro_wife_visit_2_16
            "She leans in for a passionate kiss before disappearing to let you get on with your day."
        "Come her and I'll show you how much I liked it":
            wt_image intro_wife_visit_2_17
            ivy.c "Mmmmm.  I can see and feel that.  I do love an appreciative audience."
            wt_image intro_wife_visit_2_18
            "She leans in for a passionate kiss ..."
            wt_image intro_wife_pleasure_her_1_2
            "... then turns back around and wiggles her butt against you."
            ivy.c "Did you want to do something with that before I go?"
            $ title = "what do you want?"
            menu:
                "Pleasure her":
                    wt_image intro_wife_visit_2_17
                    player.c "Not with that, but I have other body parts I thought I might use on you."
                    wt_image intro_wife_pleasure_her_1_4
                    ivy.c "Mmmmm.  I won't say no to that."
                    if ivy.domme_comfort > 2:
                        wt_image intro_wife_pleasure_her_1_5
                        "She holds you firmly by the back of the head ..."
                        wt_image intro_wife_pleasure_her_1_6
                        "... showing you exactly how she wants you to please her."
                        wt_image intro_wife_pleasure_her_1_7
                        "You do your best, and soon succeed."
                    else:
                        wt_image intro_wife_pleasure_her_1_5
                        "She caresses the back of your head as you gently lick ..."
                        wt_image intro_wife_pleasure_her_1_6
                        "... and nibble ..."
                        wt_image intro_wife_pleasure_her_1_7
                        "... and lick some more."
                    wt_image intro_wife_pleasure_her_1_8
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    wt_image intro_wife_pleasure_her_1_4
                    ivy.c "Wow.  I will take my clothes off for you anytime."
                    wt_image intro_wife_pleasure_her_1_9
                    "She kisses you passionately, then disappears to let you get on with your day."
                    $ ivy.pleasure_her_count += 1
                    $ ivy.orgasm_count += 1
                    $ ivy.temporary_count = 0
                    change player energy by -energy_short
                "Blow job":
                    wt_image intro_wife_visit_2_17
                    player.c "I thought maybe you could do something about that for me?"
                    wt_image intro_wife_visit_2_19
                    if ivy.has_tag('bj_training'):
                        ivy.c "Of course, I can.  I'm a well-trained cocksucker, you know?  Sit back."
                        wt_image intro_wife_visit_2_20
                        "She's impatient today, warming your balls up with just her hand before taking you into her mouth."
                        wt_image intro_wife_visit_2_21
                        "No doubt it's because she's excited from the strip tease.  You're pretty excited, too ..."
                        wt_image intro_wife_visit_2_22
                        "... and the feel of her fingers stroking your balls as her tongue and lips work your shaft soon have you ready to cum."
                        wt_image intro_wife_bj_2_1
                        "Sensing that you're close, Ivy drops to her knees and waits."
                        $ title = "Where do you want to cum?"
                        menu:
                            "On her face":
                                wt_image intro_wife_bj_3_1
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_bj_3_2
                                $ ivy.facial_count += 1
                            "In her mouth":
                                wt_image intro_wife_visit_2_22
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_bj_2_2
                                $ ivy.swallow_count += 1
                        "She gives your dick a quick kiss, then disappears to let you get on with your day."
                    else:
                        ivy.c "Of course, I can.  Sit back."
                        wt_image intro_wife_visit_2_20
                        "She sits beside you and leans over, taking your cock in her mouth."
                        wt_image intro_wife_visit_2_21
                        "She's impatient today, sucking hard on your tool, as if she's trying to extract the sperm from your balls with suction alone.  No doubt it's because she's worked up from the strip tease."
                        wt_image intro_wife_visit_2_22
                        "You're pretty worked up from watching her strip, too, and it's not long before you fill her mouth with the load she's been working for."
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_2_24
                        "She sits up and gives you a quick kiss, then disappears to let you get on with your day."
                        $ ivy.swallow_count += 1
                    $ ivy.blowjob_count += 1
                    orgasm
                "Sex":
                    wt_image intro_wife_visit_2_17
                    player.c "It would be a shame to let this nice erection you created go to waste."
                    wt_image intro_wife_visit_2_18
                    ivy.c "Mmmmm.  It certainly would be."
                    wt_image intro_wife_visit_2_25
                    "She's wet and sensitive and gasps as you slide into her."
                    if ivy.has_tag('domme'):
                        wt_image intro_wife_visit_2_26
                        "You try to go slow to make it last, but she wants nothing of that ..."
                        wt_image intro_wife_visit_2_27
                        "... and leans up and bites your lip."
                        ivy.c "Fuck me, boy, hard and fast.  I'll tell you if you're allowed to slow down."
                    else:
                        wt_image intro_wife_visit_2_26
                        "You try to go slow to make it last, but she wants nothing of that."
                        ivy.c "Faster!  Fuck me harder!!"
                    wt_image intro_wife_visit_2_28
                    "You begin thrusting harder, and Ivy's pleasure peaks quickly."
                    wt_image intro_wife_visit_2_29
                    ivy.c "OH ... I'M CUMMINNGGG!!!"
                    if ivy.has_tag('domme'):
                        wt_image intro_wife_visit_2_30
                        "When she finishes cumming, Ivy reaches down and removes your cock, then pumps your load onto her waiting belly."
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_2_34
                        ivy.c "Mmmmm.  That was hot.  Clean us up, then I'll get out of here and you can go on with your day."
                    else:
                        wt_image intro_wife_visit_2_26
                        "Now it's your turn."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image intro_wife_visit_2_31
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_visit_2_32
                                ivy.c "Mmmmm.  That was nice."
                                "When she finishes kissing you, she disappears, letting you go on with your day."
                            "On her":
                                wt_image intro_wife_visit_2_33
                                player.c "[player.orgasm_text]"
                                wt_image intro_wife_visit_2_34
                                ivy.c "Mmmmm.  That was hot."
                                "After a moment to catch her breath, she cleans herself, then disappears, letting you go on with your day."
                    $ ivy.sex_count += 1
                    $ ivy.orgasm_count += 1
                    orgasm
                "Anal" if ivy.anal_count > 0:
                    wt_image intro_wife_visit_2_17
                    player.c "Indeed I do.  I want to stick it in that cute butt that you've been wiggling at me."
                    wt_image intro_wife_pleasure_her_1_2
                    ivy.c "Really?  My butt's responsible for this big hard on?  Then I guess my butt should look after it."
                    if ivy.has_tag('anal_orgasm'):
                        wt_image intro_wife_seduce_1_40
                        "She lies back and let's you slowly push your cock into her well-lubed back door."
                        wt_image intro_wife_anal_1_3
                        ivy.c "That's it.  I can feel your entire cock head in me.  You can start fucking me, now."
                        wt_image intro_wife_anal_1_2
                        "You don't need any more encouragement.  Her tight butt hole feels great as you stroke in and out of her."
                        wt_image intro_wife_seduce_1_39
                        "It must feel pretty good to her, too."
                        ivy.c "OH ... I'M CUMMINNGGG!!!"
                        wt_image intro_wife_anal_1_3
                        "She's not the only one."
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_2_12
                        ivy.c "Mmmm.  I'll be feeling the effects of that strip tease for the rest of the day.  Not that I'm complaining."
                        $ ivy.orgasm_count += 1
                    else:
                        wt_image intro_wife_seduce_1_49
                        "She kneels down and you slowly push your cock into her well-lubed back door."
                        wt_image intro_wife_seduce_1_35
                        ivy.c "Oh!  I think I can feel your entire cock head in me.  You can start fucking me, now."
                        wt_image intro_wife_seduce_1_36
                        "You don't need any more encouragement.  Her tight butt hole feels great as you stroke in and out of her, your excitement quickly building."
                        wt_image intro_wife_anal_2_1
                        "As she feels you pull out, she reaches back and pumps your load onto her upturned ass."
                        player.c "[player.orgasm_text]"
                        wt_image intro_wife_visit_2_12
                        ivy.c "I'll be feeling the effects of that strip tease for the rest of the day, but at least I have no doubts that you enjoyed it."
                    wt_image intro_wife_visit_2_3
                    "She gets herself dressed and heads out, leaving you to go on with your day."
                    $ ivy.anal_count += 1
                    orgasm
                "Nothing today":
                    wt_image intro_wife_visit_2_17
                    player.c "The strip tease was enough for today, thank you."
                    ivy.c "You're welcome!  Anytime you want a repeat, just call me."
                    wt_image intro_wife_visit_2_18
                    "After another quick kiss, she disappears to let you get on with your day."
        "You should do this for a bigger audience" if ivy.resistance < 60 and not ivy.has_tag('showgirl') and not ivy.stripper_discussion == 1:
            player.c "You're really good at this, Ivy.  You shouldn't just be teasing one man with your body.  You should be making a whole crowd of men hard."
            ivy.c "Do you mean on stage?"
            player.c "Exactly.  Think of all the men in the audience lusting after you."
            ivy.c "I couldn't do that in public.  People who know me may see me."
            if player.has_tag('club_first_visit_complete'):
                player.c "Not in public, no.  But how about at a private club with strict confidentiality rules?  I can get you some time on stage and you can see how you like it?"
                wt_image intro_wife_visit_2_8
                ivy.c "Do you really think I give a good enough strip tease to be on stage?"
                player.c "I really do."
                wt_image intro_wife_visit_2_2
                ivy.c "Okay, if you don't think I'll make a fool of myself, I guess I could try it.  Let me write down the address."
                sys "You should be able to find Ivy at the Club's Stage the next time you visit."
                call ivy_convert_showgirl from _call_ivy_convert_showgirl
            else:
                wt_image intro_wife_visit_2_8
                "Maybe not in public she couldn't, but a private club with strict confidentiality rules may be a different story."
                wt_image intro_wife_visit_2_2
                "You'll be able to discuss this with her again later once you find a suitable location."
                $ ivy.stripper_discussion = 1
    # only triggers if didn't have sex, to deduct energy
    if ivy.temporary_count == 1:
        $ ivy.temporary_count = 0
        change player energy by -energy_very_short
    call ivy_send_home from _call_ivy_send_home_1
    return

label ivy_strip_lingerie_visit:
    wt_image intro_wife_visit_2_3
    ivy.c "If I change into my lingerie first, there won't be much to strip out of.  But give me a sec and I'll go change."
    wt_image intro_wife_lingerie_1_4
    ivy.c "Is this better?"
    wt_image intro_wife_lingerie_1_8
    ivy.c "Like I said, it doesn't leave much to the imagination"
    wt_image intro_wife_lingerie_1_9
    ivy.c "But I'm glad you like looking at me in it anyway."
    wt_image intro_wife_lingerie_1_6
    ivy.c "I guess it does dress up this middle-aged body of mine."
    wt_image intro_wife_lingerie_1_10
    ivy.c "Maybe that makes it more interesting to look at me again?"
    wt_image intro_wife_lingerie_1_11
    ivy.c "Since you're still looking, I suppose I could take off my panties."
    wt_image intro_wife_lingerie_1_12
    ivy.c "Does that improve the view?"
    wt_image intro_wife_lingerie_1_13
    ivy.c "I hope so, because once I remove these garters and stockings ..."
    wt_image intro_wife_visit_2_12
    ivy.c "... all you have left to look at is plain old me."
    call ivy_strip_visit_end from _call_ivy_strip_visit_end_1
    return

# Submissive visit content
label ivy_submissive_visit:
    $ ivy.temporary_count = 1
    wt_image intro_wife_visit_3_2
    $ title = "What do you want to do with her?"
    menu:
        "Have her serve you":
            player.c "Undress"
            wt_image intro_wife_visit_3_81
            player.c "When you're naked, we'll begin."
            wt_image intro_wife_visit_1_25
            if ivy.serve_count == 0:
                ivy.c "What should I do now?"
                player.c "Offer yourself to me."
            ivy.c "Sir, I'm ready to serve you."
            player.c "Good.  Go to the kitchen and bring me something to drink."
            if ivy.serve_count < 2:
                wt_image intro_wife_visit_1_52
                ivy.c "For real?"
                player.c "Yes.  I'll just have a water for now."
                wt_image intro_wife_visit_1_72
                player.c "Put a slice of lemon in it, for me.  You'll find them in a bowl on the counter.  Glasses are in the left most cupboard when you're facing the sink."
                wt_image intro_wife_serve_1_1
                "She returns a few minutes later, and hands you your water with lemon."
                ivy.c "Here's your drink, Sir."
                player.c "Get down on the floor in front of me while I drink it."
                ivy.c "Get on the floor?"
                player.c "You heard me."
                wt_image intro_wife_serve_1_2
                "She lowers herself, figuratively and literally, before you."
                player.c "That's nice, but this drink would be more enjoyable with a view of your ass."
                wt_image intro_wife_serve_1_3
                "She stares at you again ..."
                wt_image intro_wife_serve_1_4
                "... then turns around."
                wt_image intro_wife_serve_1_5
                player.c "You know what?  This is too impersonal.  Turn around and face me again ..."
                wt_image intro_wife_serve_1_3
                player.c "... but keep your legs spread."
                wt_image intro_wife_serve_1_7
                player.c "Wider"
                wt_image intro_wife_serve_1_8
                ivy.c "This is ..."
                player.c "Shush.  I'm enjoying my drink.  Don't interrupt.  You could open your pussy lips, though."
                wt_image intro_wife_serve_1_9
                "You take your time finishing your drink as Ivy waits quietly and tries not to let on that she's actually enjoying this."
                $ ivy.serve_count = 2
            else:
                wt_image intro_wife_visit_1_72
                player.c "Don't forget a slice of lemon."
                ivy.c "I won't, Sir."
                wt_image intro_wife_visit_1_52
                ivy.c "Here's your drink, Sir.  I hope you enjoy it.  Would you like ..."
                player.c "Would I like what?"
                wt_image intro_wife_visit_1_58
                ivy.c "Would you like me to be somewhere in particular for you?"
                player.c "You don't have to be shy about it.  Spit it out."
                wt_image intro_wife_visit_1_50
                ivy.c "Would you like me on the ground at your feet while you enjoy your drink, Sir?"
                wt_image intro_wife_serve_1_1
                player.c "Yes, I do.  Come closer and kneel down here."
                wt_image intro_wife_serve_1_2
                ivy.c "How would you like me to face, Sir?"
                wt_image intro_wife_serve_1_4
                player.c "Turn around."
                wt_image intro_wife_serve_1_5
                ivy.c "Is this good, Sir?"
                wt_image intro_wife_serve_1_7
                player.c "It is, but turn around so I can look at your pussy and compare."
                wt_image intro_wife_serve_1_8
                ivy.c "How's this, Sir?"
                player.c "Better, but open your pussy lips, too."
                wt_image intro_wife_serve_1_9
                "You take your time finishing your drink as Ivy waits quietly and tries not to let on that she's actually enjoying this."
            $ title = "What now?"
            menu:
                "Let her go home":
                    player.c "That's all for today, Ivy."
                    wt_image intro_wife_serve_1_11
                    ivy.c "That's all, Sir?  Okay.  Thank you."
                    wt_image intro_wife_visit_3_81
                    "She tries hard to not to let on that's she's disappointed you didn't ask her to do more for you."
                    change player energy by -energy_very_short
                "Tell her to blow you":
                    call ivy_serve_blowjob from _call_ivy_serve_blowjob_4
                    # note: orgasm is handled in the label above
                    ivy.c "I'm glad I was able to be of service to you today, Sir."
            wt_image intro_wife_visit_3_30
            "She gets herself together and leaves quietly, letting you get on with your day."
            $ ivy.submissive_visit_timer = 2
        "Have her serve you in her fishnets" if ivy.has_tag('gave_her_fishnet_lingerie') and ivy.serve_count > 1:
            if ivy.has_tag('modelled_fishnet_lingerie'):
                player.c "Go change into your fishnets."
                wt_image current_location.image
                "Ivy ducks into the bathroom to change ..."
                wt_image intro_wife_lingerie_2_1
                "... reappearing few minutes later, wearing her fishnets again."
                player.c "Don't be shy.  Come closer."
                wt_image intro_wife_lingerie_2_3
                "Ivy adopts a catwalk gait as she approaches."
            else:
                add tags 'modelled_fishnet_lingerie' to ivy
                player.c "I want to see what you look like in those fishnets I gave you."
                wt_image current_location.image
                "Ivy disappears into the bathroom to change.  She's gone a long time."
                wt_image intro_wife_lingerie_2_1
                "Eventually, she timidly steps back into the room."
                ivy.c "This makes me look like even more of a slut than I expected."
                player.c "Don't be shy.  Come closer."
                wt_image intro_wife_lingerie_2_2
                player.c "Not like that."
                ivy.c "Pardon?"
                player.c "Entertain me as you walk over to me."
                wt_image intro_wife_lingerie_2_3
                "Ivy thinks for a moment, then adopts a catwalk gait as she approaches."
            wt_image intro_wife_lingerie_2_4
            ivy.c "Sir, I'm ready to serve you.  May I get you something to drink to start?  A glass of water with a slice of lemon, maybe?"
            wt_image intro_wife_lingerie_2_11
            player.c "Be quick about it."
            wt_image intro_wife_lingerie_2_12
            ivy.c "Here you are, Sir."
            wt_image intro_wife_lingerie_2_13
            ivy.c "Should I ...  That is, would you like if I ..."
            player.c "Spit it out, Ivy."
            wt_image intro_wife_lingerie_2_5
            ivy.c "Should I be down on the ground at your feet while you drink it, Sir?"
            $ title = "What do you want?"
            menu:
                "Yes, tell her to get down in front of you" if ivy.has_tag('modelled_fishnet_lingerie'):
                    wt_image intro_wife_lingerie_2_24
                    player.c "Yes, and look pretty while you're down there."
                    wt_image intro_wife_lingerie_2_25
                    player.c "Not pretty enough.  Give me a proper show."
                    wt_image intro_wife_lingerie_2_23
                    player.c "That's better."
                    "She stays like that as you finish your drink, trying hard not to let on how much being putting on this display is turning her on."
                    $ title = "What now?"
                    menu:
                        "Let her go home":
                            player.c "That's all for today, Ivy."
                            wt_image intro_wife_lingerie_2_20
                            ivy.c "Yes, Sir.  Thank you, Sir."
                            change player energy by -energy_very_short
                        "Tell her to blow you":
                            player.c "Looking at you is making me hard.  Deal with that."
                            wt_image intro_wife_lingerie_2_24
                            ivy.c "Yes, Sir.  With pleasure, Sir."
                            call ivy_submissive_blowjob_fishnets from _call_ivy_submissive_blowjob_fishnets
                            # note: orgasm is in label above
                "No, tell her to pose against the wall instead":
                    player.c "No, you'd look better up against the wall."
                    if not ivy.has_tag('modelled_fishnet_lingerie'):
                        wt_image intro_wife_lingerie_2_6
                        ivy.c "The wall?"
                        wt_image intro_wife_lingerie_2_7
                        player.c "Yes.  I want to see if you can be more attractive artwork than the vase beside you."
                        wt_image intro_wife_lingerie_2_8
                        ivy.c "You're comparing me to ..."
                        player.c "So far you're losing.  The vase at least is silent."
                        wt_image intro_wife_lingerie_2_9
                        ivy.c "Yes, Sir.  Sorry, Sir."
                        add tags 'modelled_fishnet_lingerie' to ivy
                    else:
                        wt_image intro_wife_lingerie_2_7
                        ivy.c "Yes, Sir."
                        wt_image intro_wife_lingerie_2_9
                        "She can't help but steal a glance at the vase, which is what she's being treated like."
                    wt_image intro_wife_lingerie_2_10
                    "She tries hard not to let on how much the humiliation of being objectified like this is turning her on.  From across the room, you can hear her breathing getting heavy as you finish your drink."
                    $ title = "What now?"
                    menu:
                        "Let her go home":
                            player.c "That's all for today, Ivy."
                            wt_image intro_wife_lingerie_2_9
                            ivy.c "Yes, Sir.  Was I ..."
                            player.c "Were you what?"
                            wt_image intro_wife_lingerie_2_5
                            ivy.c "Nothing, Sir.  Forget it."
                            player.c "Did you want to know if I found you as interesting to look at as the vase beside you?"
                            wt_image intro_wife_lingerie_2_20
                            ivy.c "I was just being stupid for a moment, Sir.  Forget I said anything.  Please?"
                            change player energy by -energy_very_short
                        "Tell her to blow you":
                            player.c "It's pretty close between you and the vase as to which I prefer looking at, but I've thought of a way you could please me more."
                            wt_image intro_wife_lingerie_2_9
                            ivy.c "What would you like me to do, Sir?"
                            player.c "Come over here and suck my cock."
                            wt_image intro_wife_lingerie_2_6
                            ivy.c "Yes, Sir.  With pleasure, Sir."
                            call ivy_submissive_blowjob_fishnets from _call_ivy_submissive_blowjob_fishnets_1
                            # note: orgasm is in label above
            wt_image intro_wife_visit_3_30
            "She changes and heads home, leaving you to get on with your day."
            $ ivy.submissive_visit_timer = 2
        "Spank her":
            player.c "Undress"
            wt_image intro_wife_visit_3_81
            player.c "All the way.  Then turn around and present your butt to me."
            if ivy.spank_count == 0:
                wt_image intro_wife_visit_3_62
                ivy.c "My butt?  Why?"
                player.c "Because I'm going to spank it."
                wt_image intro_wife_visit_3_64
                ivy.c "You want to start hitting me now?"
                player.c "Spanking's a very specialized form of hitting, Ivy.  It's been used for centuries to help reinforce submission."
                wt_image intro_wife_visit_3_62
                ivy.c "I've already agreed to obey you.  What more do you want?"
                player.c "What I want is to enjoy the feel of my palm smacking on your cute butt cheeks.  For someone who says they've agreed to obey, you seem to be taking your sweet time following my instructions.  Turn around and present your butt to me."
                wt_image intro_wife_visit_3_61
                ivy.c "Will it hurt?"
                wt_image intro_wife_visit_3_82
                player.c "Yes.  I wouldn't enjoy it nearly so much if it doesn't leave you squirming around.  Don't worry, though, I'm not going to traumatize you.  I'll want you to come back for future spankings, too.  Put your hand down."
            elif ivy.has_tag('spanking_orgasm'):
                wt_image intro_wife_visit_3_75
                ivy.c "Is this going to be a ..."
                player.c "No, it's not a good girl spanking today."
                wt_image intro_wife_visit_3_61
                ivy.c "Did I do something to deserve a punishment spanking?"
                wt_image intro_wife_visit_3_82
                player.c "Just having a cute ass I enjoy smacking is cause enough.  Put your hand down."
            else:
                wt_image intro_wife_visit_3_61
                ivy.c "Did I do something to deserve another spanking?"
                wt_image intro_wife_visit_3_82
                player.c "Just having a cute ass I enjoy smacking is cause enough.  Put your hand down."
            wt_image intro_wife_spank_2_1
            "You swat her perk butt until she calls out "
            $ ivy.temporary_count = ivy.spank_count + 3
            while ivy.temporary_count > 0:
                extend "  *smack*"
                $ ivy.temporary_count -= 1
            wt_image intro_wife_visit_3_83
            ivy.c "Ow!!  My butt's really sore now."
            $ title = "What now?"
            menu:
                "Keep spanking her":
                    player.c "Get back in position."
                    wt_image intro_wife_spank_2_1
                    "*smack*"
                    ivy.c "Ow!"
                    menu menu_ivy_visit_spanking_menu_1:
                        "Give her another":
                            $ ivy.temporary_count += 1
                            "*smack*"
                            if ivy.temporary_count > 3:
                                wt_image intro_wife_visit_3_83
                                ivy.c "Ow!!  Those are really starting to hurt!"
                                menu menu_ivy_visit_spanking_menu_2:
                                    "Give her another":
                                        $ ivy.temporary_count += 1
                                        wt_image intro_wife_spank_2_1
                                        "*SMACK*"
                                        if ivy.temporary_count > 7:
                                            wt_image intro_wife_visit_3_83
                                            ivy.c "OWW!!!!  My butt's completely bruised!!"
                                            menu menu_ivy_visit_spanking_menu_3:
                                                "Give her another":
                                                    $ ivy.temporary_count += 1
                                                    wt_image intro_wife_spank_2_1
                                                    "*SMACK!!*"
                                                    if ivy.temporary_count > 10:
                                                        wt_image intro_wife_visit_3_83
                                                        ivy.c "OOWWW!!!!  PLEASE!!!  Please stop now.  I can't take any more!!"
                                                        menu:
                                                            "Tell her one more":
                                                                player.c "Back in position, you can take one more."
                                                                ivy.c "Please, no.  I really can't."
                                                                player.c "Back in position."
                                                                wt_image intro_wife_spank_2_1
                                                                "Trembling, she lowers her hand and presents her butt to you."
                                                                "*SMACK!!!*"
                                                                wt_image intro_wife_visit_3_83
                                                                ivy.c "OOWWWWW!!!!!"
                                                                player.c "See, you could take one more."
                                                                wt_image intro_wife_visit_3_64
                                                                ivy.c "I didn't want to, though.  I felt like I was at my limit."
                                                                wt_image intro_wife_visit_3_65
                                                                player.c "I think I've got a better sense of your true limit than you do.  Next time, I might show you just how tough you really are."
                                                                $ ivy.submissive_visit_timer = 5
                                                            "Stop":
                                                                wt_image intro_wife_visit_3_61
                                                                ivy.c "That was crazy intense.  My butt must be completely bruised."
                                                                wt_image intro_wife_visit_3_65
                                                                player.c "Just red, not bruised.  You're tougher than you know.  Next time, I might show you just how tough."
                                                                $ ivy.submissive_visit_timer = 4
                                                        add tags 'ready_for_dungeon' to ivy
                                                    else:
                                                        ivy.c "OWW!!!"
                                                        jump menu_ivy_visit_spanking_menu_3
                                                "Stop":
                                                    wt_image intro_wife_visit_3_62
                                                    ivy.c "You said you wouldn't traumatize me!  My butt feels traumatized."
                                                    wt_image intro_wife_visit_3_84
                                                    player.c "Just toughening you up to get you ready for intense play later."
                                                    $ ivy.submissive_visit_timer = 4
                                        else:
                                            ivy.c "OW!"
                                            jump menu_ivy_visit_spanking_menu_2
                                    "Switch to a 'good girl spanking'" if ivy.spank_count > 1 and not ivy.has_tag('spanking_orgasm'):
                                        player.c "I think you're ready for your reward."
                                        ivy.c "What do you mean reward?"
                                        player.c "You've earned a 'good girl spanking'.  Put your hand between your legs.  I'm going to let you touch yourself while I continue to spank you."
                                        wt_image intro_wife_visit_3_82
                                        ivy.c "I ... I don't think I want that type of 'reward'."
                                        player.c "I'm going to keep spanking you, Ivy.  If your hand is between your legs, it'll be a good girl spanking.  If it isn't, it'll be a punishment spanking.  Which is it going to be?"
                                        wt_image intro_wife_spank_2_2
                                        player.c "That's a good girl.  Now you can rub with your hand as much as you need to to alleviate the sting of the spanking."
                                        wt_image intro_wife_spank_2_3
                                        "You make it a sensual spanking.  As sore as her butt is, even the lightest swats are uncomfortable, but the heat of each blow goes directly to her pussy, and she rubs herself more and more vigorously as you spank her ... *smack*  *smack*  *smack*"
                                        wt_image intro_wife_spank_2_4
                                        "*smack*  *smack*  *smack* ... Her hand moves faster and faster, her fingers sliding over her clit and into her rapidly wetting slit until  ..."
                                        wt_image intro_wife_spank_2_5
                                        ivy.c "OH ... I'M CUMMINNGGG!!!"
                                        wt_image intro_wife_spank_2_3
                                        ivy.c "Wow, I can't believe how the heat from the spanking is still making my pussy throb."
                                        player.c "And you thought you didn't like to be spanked."
                                        $ ivy.orgasm_count += 1
                                        add tags 'spanking_orgasm' to ivy
                                        $ ivy.submissive_visit_timer = 2
                                    "Stop":
                                        wt_image intro_wife_visit_3_61
                                        ivy.c "I won't be able to sit comfortably for a week!"
                                        wt_image intro_wife_visit_3_84
                                        player.c "After only a few love taps?  I'll need to spank you harder and longer next time to toughen you up."
                                        $ ivy.submissive_visit_timer = 3
                            else:
                                ivy.c "Ow!"
                                jump menu_ivy_visit_spanking_menu_1
                        "Stop":
                            wt_image intro_wife_visit_3_61
                            ivy.c "I won't be able to sit comfortably all day."
                            wt_image intro_wife_visit_3_84
                            player.c "After only a few love taps?  I'll need to spank you harder and longer next time to toughen you up."
                            $ ivy.submissive_visit_timer = 2
                "Stop there":
                    wt_image intro_wife_visit_3_61
                    ivy.c "I won't be able to sit comfortably all day."
                    wt_image intro_wife_visit_3_83
                    player.c "After only a few love taps?  I'll need to spank you harder and longer next time to toughen you up."
                    $ ivy.submissive_visit_timer = 3
            wt_image intro_wife_visit_3_30
            "She leaves quietly, letting you go on with your day."
            $ ivy.spank_count += 1
            $ ivy.temporary_count = 1
        "Give her a 'good girl spanking'" if ivy.has_tag('spanking_orgasm'):
            $ ivy.goodgirlspanking_outfit += 1
            if ivy.goodgirlspanking_outfit > 2:
                $ ivy.goodgirlspanking_outfit = 1
            if ivy.goodgirlspanking_outfit == 1:
                player.c "I'm going to spank you again, Ivy."
                wt_image intro_wife_visit_3_75
                ivy.c "Is this a punishment or ..."
                player.c "What type of spanking would you like it to be?"
                wt_image intro_wife_visit_3_61
                ivy.c "I'd prefer a good girl spanking."
                player.c "What should you do then?"
                wt_image intro_wife_visit_3_82
                ivy.c "May I please have a good girl spanking, Sir?"
                wt_image intro_wife_spank_2_2
                player.c "Will you cum for me if I let you have a spanking?"
                wt_image intro_wife_spank_2_3
                ivy.c "Yes, Sir.  As embarrassing as it is, I'd still enjoy cumming for you while you spank me."
                wt_image intro_wife_spank_2_4
                "You take your time and stretch the spanking out ... *smack*  *smack*  *smack*  *smack*  *smack*"
                wt_image intro_wife_spank_2_5
                "... which makes her subsequent orgasm all the more intense."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
            else:
                player.c "For being such a good, obedient girl, you're getting a reward."
                wt_image intro_wife_visit_3_3
                ivy.c "What type of reward?"
                player.c "The sort where you're naked and your head is down and your ass is up."
                wt_image intro_wife_visit_3_63
                ivy.c "That could be a variety of things."
                wt_image intro_wife_visit_3_61
                player.c "You'll be enjoying the warmth that comes from a well-spanked bum.  Can you guess now?"
                wt_image intro_wife_visit_3_82
                ivy.c "I could guess from the beginning.  I was just hoping maybe for a reward that didn't leave me sitting uncomfortably on the drive home."
                wt_image intro_wife_spank_2_2
                player.c "Tell the truth.  That discomfort will keep your pussy wet the whole drive home, won't it?"
                wt_image intro_wife_spank_2_3
                ivy.c "I refuse to answer, Sir, on the grounds that I'm afraid you'll make my bum even more uncomfortable if I admit the truth."
                wt_image intro_wife_spank_2_4
                "She needn't have worried.  You've every intention of making her bum sore regardless ... *smack*  *smack*  *smack*  *smack*  *smack*"
                wt_image intro_wife_spank_2_5
                "... which makes her subsequent orgasm all the more intense."
                ivy.c "OH ... I'M CUMMINNGGG!!!"
            wt_image intro_wife_visit_3_81
            ivy.c "Thank you for the good girl spanking, Sir.  I'm glad you chose to make me serve you like that, even if cumming during it embarrassed the hell out of me."
            $ ivy.orgasm_count += 1
            $ ivy.submissive_visit_timer = 1
        "Nothing right now":
            $ ivy.temporary_count = 0
    if ivy.temporary_count == 1:
        $ ivy.temporary_count = 0
        change player energy by -energy_short
        call ivy_send_home from _call_ivy_send_home_2
    return

label ivy_submissive_blowjob_fishnets:
    if ivy.has_tag('bj_training'):
        wt_image intro_wife_lingerie_2_32
        "She remembers her training and begins by warming up your balls."
        wt_image intro_wife_lingerie_2_33
        "Then she licks up and down your shaft from base to tip ..."
        wt_image intro_wife_lingerie_2_34
        "... then wraps her lips around the head of your cock and begins to suckle."
        wt_image intro_wife_lingerie_2_35
        "Between watching her while you enjoyed your drink and the feel of her talented mouth, it's not long before you're ready to cum."
        wt_image intro_wife_lingerie_2_33
        player.c "Get into position."
        wt_image intro_wife_lingerie_2_37
        player.c "[player.orgasm_text]"
    else:
        wt_image intro_wife_lingerie_2_34
        "Ivy takes your cock into her mouth ..."
        wt_image intro_wife_lingerie_2_39
        "... and begins to suck on it."
        wt_image intro_wife_lingerie_2_33
        "Between her tongue ..."
        wt_image intro_wife_lingerie_2_34
        "... her lips ..."
        wt_image intro_wife_lingerie_2_35
        ".. and her hand, she soon has you ready to cum."
        wt_image intro_wife_lingerie_2_33
        player.c "Remove your mouth."
        wt_image intro_wife_lingerie_2_36
        "Holding her by the hair, you position her face in front of your cock as you cum."
        player.c "[player.orgasm_text]"
    wt_image intro_wife_lingerie_2_38
    ivy.c "Thank yo for letting me be of service to you today, Sir."
    $ ivy.facial_count += 1
    $ ivy.blowjob_count += 1
    orgasm
    return

# Send home
label ivy_send_home:
    $ ivy.training_session()
    call character_location_return(ivy) from _call_character_location_return_660
    wt_image current_location.image
    notify
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Client
label ivy_contact:
    wt_image intro_wife_phone_2_1
    if ivy.has_tag('first_post_training_contact_complete'):
        ivy.c "Hi again!"
    else:
        add tags 'first_post_training_contact_complete' to ivy
        if ivy.has_tag('love_potion_used'):
            ivy.c "Hi there!  I was hoping you'd call!"
            add tags 'continuing_actions' to ivy
        else:
            ivy.c "Hi there!  I wasn't expecting to here from you after my training was over.  What did you want?"
    # If showgirl conversation possible
    if ivy.has_tag('stripped_for_you') and ivy.stripper_discussion <= 1 and not ivy.has_tag('showgirl'):
        if ivy.has_tag('no_visits'):
            call ivy_contact_showgirl from _call_ivy_contact_showgirl
        else:
            $ title = "What do you want to talk to [ivy.name] about?"
            menu:
                "Becoming a showgirl":
                    call ivy_contact_showgirl from _call_ivy_contact_showgirl_1
                "Coming to visit you":
                    call ivy_contact_visit from _call_ivy_contact_visit
    # If Showgirl conversation not possible, only remaining option is coming to visit.
    else:
        call ivy_contact_visit from _call_ivy_contact_visit_1
    return

label ivy_contact_showgirl:
    if ivy.stripper_discussion == 0:
        player.c "I was thinking about how much you enjoy teasing men with your body and making them hard.  I think we should find you a place to do that more often."
        wt_image intro_wife_phone_2_2
        ivy.c "Do you mean on stage?"
        player.c "Exactly.  Think of all the men in the audience lusting after you."
        if ivy.resistance >= 60:
            ivy.c "I don't think that's a good idea.  I think it's better if I stick to teasing my husband in the safety of our house."
            sys "Ivy's resistance to you was too high at the end of her training for her to give your suggestion serious consideration."
            $ ivy.stripper_discussion = 2
        else:
            ivy.c "I couldn't do that in public.  People who know me may see me."
            if player.has_tag('club_first_visit_complete'):
                player.c "Not in public, no.  But how about at a private club with strict confidentiality rules?  I can get you some time on stage and you can see how you like it?"
                wt_image intro_wife_phone_2_1
                ivy.c "Do you really think I give a good enough strip tease to be on stage?"
                player.c "I really do."
                wt_image intro_wife_phone_2_4
                ivy.c "Okay, if you don't think I'll make a fool of myself, I guess I could try it.  Let me write down the address."
                sys "You should be able to find Ivy at the Club's Stage the next time you visit."
                call ivy_convert_showgirl from _call_ivy_convert_showgirl_1
            else:
                "Maybe not in public she couldn't, but a private club with strict confidentiality rules may be a different story."
                add tags 'waiting_for_club_access' to ivy
                $ ivy.stripper_discussion = 1
    elif ivy.stripper_discussion == 1 and player.has_tag('club_first_visit_complete'):
        player.c "Remember our conversation about you teasing a group of guys at once?"
        wt_image intro_wife_phone_2_2
        ivy.c "Yes, but I wouldn't be comfortable doing that in public.  People who know me might see me."
        player.c "Not in public, no.  But how about at a private club with strict confidentiality rules?  I can get you some time on stage and you can see how you like it?"
        wt_image intro_wife_phone_2_1
        ivy.c "Do you really think I give a good enough strip tease to be on stage?"
        player.c "I really do."
        wt_image intro_wife_phone_2_4
        ivy.c "Okay, if you don't think I'll make a fool of myself, I guess I could try it.  Let me write down the address."
        sys "You should be able to find Ivy at the Club's Stage the next time you visit."
        call ivy_convert_showgirl from _call_ivy_convert_showgirl_2
    else:
        "You don't have anything to talk to her about this, yet.  You need to find a safe, private stage for her to perform on."
    if ivy.has_tag('no_visits') and ivy.stripper_discussion != 1:
        $ living_room.remove_action(ivy.current_client_action)
    return

label ivy_contact_visit:
    # Determine if Character wants to continue Visiting
    if not ivy.has_tag("continuing_actions"):
        player.c "I'd like you to continue to come see me."
        # tests are purposefully against unmodified stats
        if ivy.desire > 20:
            wt_image intro_wife_phone_2_3
            ivy.c "I did enjoy spending time with you.  I'll let my husband know that we're going to keep seeing each other.  As you know, we have an open marriage, and I'm sure he'll be fine with that."
            add tags 'continuing_actions' to ivy
        else:
            wt_image intro_wife_phone_2_2
            ivy.c "I don't think that's a good idea."
            sys "Ivy's Desire for you at the end of her training wasn't high enough for her to want to continue to spend time with you."
            if ivy.has_tag('trigger_implanted'):
                player.c "[ivy.trigger_phrase], Ivy.  Whenever I ask you to come see me, you will want to visit me, Ivy."
                wt_image intro_wife_phone_2_4
                ivy.c "Oh right.  Of course.  Now that I've thought about, I do want to come visit you again."
                add tags 'continuing_actions' to ivy
            else:
                add tags 'no_visits' to ivy
    else:
        player.c "I'd like you to come visit me again."
    if ivy.has_tag('continuing_actions'):
        ivy.c "What are we going to do when I get there?"
        call expandable_menu(ivy_continuing_actions_visit_menu) from _call_expandable_menu_113
    elif ivy.has_tag('stripped_for_you') and ivy.stripper_discussion < 2:
        pass
    else:
        $ living_room.remove_action(ivy.current_client_action)
    return

label ivy_visit_crawl_start:
    if ivy.has_tag('crawled_wearing_tail'):
        player.c "You're going to get down on all fours and crawl at my feet like the stupid bitch you are."
    elif ivy.has_tag('crawled_as_slut'):
        player.c "You're going to get down on all fours and crawl at my feet like the stupid slut you are."
    else:
        player.c "You're going to humiliate yourself for my amusement by getting down on all fours and crawling at my feet."
    wt_image intro_wife_phone_2_4
    ivy.c "Wow, I don't know why that gets to me as much as it does.  I really want to tell you to 'fuck off'."
    player.c "And what are you actually going to do?"
    ivy.c "I'll be over as soon as I get my nerve up, and I then I guess we'll see."
    player.c "Bring something slutty to wear and maybe I'll have enough fun humiliating you in that I may forget to make your crawl."
    wt_image current_location.image
    "It takes her a bit to gather her nerve, but eventually she arrives."
    summon ivy
    wt_image intro_wife_visit_2_1
    ivy.c "I had to take a shower and think about whether I really wanted to come over."
    add tags 'crawl_visit_now' to ivy
    return

label ivy_visit_domme_start:
    player.c "I was hoping you'd take charge."
    wt_image intro_wife_phone_2_3
    if ivy.has_tag('second_domme_scene'):
        ivy.c "Okay, boy.  Wait for me.  I'll be over when I'm ready."
    else:
        ivy.c "Okay.  I'll be over in a bit."
    summon ivy
    wt_image intro_wife_visit_4_1
    "It's about an hour before she arrives, carrying a large bag."
    summon ivy
    add tags 'domme_visit_now' to ivy
    return

label ivy_visit_dungeon_start:
    if not ivy.has_tag('first_dungeon_visit_complete'):
        player.c "You've shown me that you're tough enough to take a decent spanking, Ivy.  It's time to take the next step.  I'm going to give you the full experience of being in my dungeon."
        wt_image intro_wife_phone_2_2
        ivy.c "I'm not sure that's something I ..."
        player.c "I didn't ask, Ivy.  I expect you here shortly."
        wt_image intro_wife_phone_2_3
        ivy.c "Yes, Sir."
        call ivy_dungeon_visit from _call_ivy_dungeon_visit
    else:
        player.c "It's time for another visit to my dungeon, Ivy."
        if ivy.submissive_visit_timer == 0:
            wt_image intro_wife_phone_2_3
            ivy.c "Yes, Sir.  I'll be right over."
            call ivy_dungeon_visit from _call_ivy_dungeon_visit_1
        else:
            wt_image intro_wife_phone_2_2
            ivy.c "I only enjoy that sort of thing once in a while.  Did you want to do something else instead?"
            call expandable_menu(ivy_continuing_actions_visit_menu) from _call_expandable_menu_114
    return

label ivy_visit_sex_start:
    player.c "I thought we'd both get naked and do what comes natural after that."
    wt_image intro_wife_phone_2_3
    ivy.c "Sounds good to me!  I'll be right over."
    wt_image current_location.image
    "She doesn't keep you waiting long."
    summon ivy
    wt_image intro_wife_visit_3_1
    ivy.c "I had a quick shower to change and freshen up."
    wt_image intro_wife_visit_3_4
    ivy.c "I'm all ready to start our booty call."
    wt_image intro_wife_visit_3_3
    "She has a seat and waits for you."
    add tags 'sex_visit_now' to ivy
    return

label ivy_visit_strip_start:
    player.c "I'd like you to tease me by taking your clothes off for me."
    wt_image intro_wife_phone_2_3
    ivy.c "You really want to see my body again?  Okay, I'll be there soon.  I just need to get ready."
    wt_image current_location.image
    "She doesn't keep you waiting long."
    summon ivy
    wt_image intro_wife_visit_2_2
    ivy.c "I had to change into something easier to take off, but I'm here now."
    add tags 'strip_visit_now' to ivy
    return

label ivy_visit_submissive_start:
    player.c "I'll find some way to amuse myself with you.  All you need to know is that I expect you to obey me when you get here."
    wt_image intro_wife_phone_2_2
    if ivy.submissive_visit_timer == 0:
        ivy.c "Yes, Sir.  I'll be right there."
        wt_image current_location.image
        "She doesn't keep you waiting long."
        summon ivy
        wt_image intro_wife_visit_3_79
        ivy.c "I cleaned myself up quickly and came right over."
        wt_image intro_wife_visit_3_80
        if ivy.serve_count > 1:
            ivy.c "Should I get naked to serve you, Sir?"
            player.c "I expect you'll be so soon enough.  Go have a seat until I'm ready for you."
        else:
            player.c "Come in and take a seat.  I'll let you know when I'm ready for you."
        wt_image current_location.image
        add tags 'submissive_visit_now' to ivy
    else:
        ivy.c "I only enjoy that sort of thing once in a while.  Did you want to do something else instead?"
        $ ivy_continuing_actions_visit_menu.reopen_once()
    return

## not needed as Cancel is active
# label ivy_visit_nothing:
#     player.c "Now's not a good time."
#     ivy.c "Okay.  Maybe another time."
#     return

## Character Specific Objects
## Items
# Give Butt Plug
label give_bp_ivy:
    if ivy.has_item(butt_plug):
        sys "You've already given her one.  She doesn't need another."
    elif ivy.status == "on_training":
        if ivy.has_tag('discussed_anal'):
            player.c "I bought you something, to help you get used to the sensation of having something in your back door."
            wt_image intro_wife_visit_1_6
            ivy.c "What are you talking about?"
            player.c "This.  It's a butt plug.  It'll help you realize it's not that bad to take something in your rear.  It can even feel good.  Pull up your skirt and I'll show you how it goes in."
            if ivy.test('submission', 20):
                wt_image intro_wife_spank_1_7
                ivy.c "I can't believe I'm letting you do this."
                player.c "It's to help you and your marriage.  Pull your panties down, too."
                wt_image intro_wife_butt_plug_1_1
                ivy.c "Holy fuck!  Did you have to get such a large one?  That thing feels like it's trying to split me in two."
                player.c "Don't be dramatic, Ivy.  It's a normal size plug for a normal sized hole, like yours."
                wt_image intro_wife_visit_1_12
                ivy.c "What happens now?  I go around with this thing up my ass?"
            else:
                wt_image intro_wife_visit_1_7
                ivy.c "I'll put it in myself, thank you!  When I get home.  What happens then?  I go around with this thing up my ass?"
            player.c "Not all the time, unless you find you like it and want to wear it all the time.  Just use it every couple of days, until it no longer feels strange."
            wt_image intro_wife_visit_1_6
            ivy.c "I can't believe it'll ever not feel strange to have something shoved up my butt, but okay, I'll try."
            change ivy submission by 5
            give 1 butt_plug from player to ivy notify
        else:
            "You've no reason to give her this, yet."
    else:
        "You should save this for a current client."
    return

# Give Chastity Belt
label give_cb_ivy:
    if ivy.status == "on_training":
        "This wasn't the type of trick her husband wanted her to learn."
    else:
        "You should save this for someone else."
    return

# Give Dildo
label give_di_ivy:
    if ivy.status == "on_training":
        "This item won't help with her training."
    else:
        "You should save this for someone else."
    return

# Use Fetch Toy
label use_ft_ivy:
    "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_ivy:
    "Save this as a gift for [chelsea.name]."
    return

# Use Leash
label use_le_ivy:
    "You shouldn't try to take someone for a walk who isn't your pet."
    return

# Give Lingerie
label give_li_ivy:
    if ivy.has_item(lingerie):
        sys "You've already gifted lingerie to Ivy.  She has enough for now."
    elif ivy.status == "on_training":
        sys "Some clients will get a stat boost from receiving some items as gifts. Items can also help with some types of training."
        sys "Most clients only get one type of lingerie, but for Ivy you get to choose between one of two types, each of which helps a different type of training.  You also get opportunities to give her the lingerie during her training, if you want to wait."
        $ title = "What type of lingerie do you want to give her?"
        menu:
            "Sexy":
                wt_image intro_wife_visit_1_9
                ivy.c "What's this?"
                player.c "A gift.  For you."
                wt_image intro_wife_visit_1_13
                ivy.c "You saw this and thought it would look good on me?"
                add tags 'gave_her_sexy_lingerie' to ivy
                change ivy desire by 5
                give 1 lingerie from player to ivy notify
            "Slutty":
                add tags 'gave_her_fishnet_lingerie' to ivy
                wt_image intro_wife_visit_1_9
                ivy.c "What's this?"
                player.c "A gift.  For you."
                wt_image intro_wife_visit_1_4
                ivy.c "I'll look like a slut wearing that."
                give 1 lingerie from player to ivy notify
            "Nothing right now":
                pass
    else:
        sys "You should save the lingerie for someone else."
    return

# Give Love Potion
label give_lp_ivy:
    if ivy.has_tag('love_potion_used'):
        "You've already used a love potion on Ivy.  Additional ones won't do anything more."
    elif current_location in session_locations:
        call ivy_update_media from _call_ivy_update_media_7
        wt_image ivy.image
        if ivy.test('resistance', 50):
            player.c "How about a drink before we get started?"
            ivy.c "I probably shouldn't."
            player.c "It's just one drink.  I think it'll be good for you.  It'll help loosen you up."
            wt_image intro_wife_drink_1_1
            ivy.c "Well ... okay, then."
            wt_image intro_wife_drink_1_2
            "She spaces out briefly as she drinks the potion."
            wt_image intro_wife_drink_1_3
            ivy.c "I don't tell you nearly often enough how happy I am that I get to spend time with you!"
            change ivy desire by 20
            add tags 'love_potion_used' to ivy
            rem 1 love_potion from player notify
        else:
            ivy.c "A drink?  No thank you."
            sys "She doesn't trust you enough to accept drinks from you.  Lower her Resistance first."
    else:
        "She doesn't want a drink from you here."
    return

# Give Transformation Potion
label give_tp_ivy:
    if ivy.has_tag('transformed'):
        "She's already been transformed.  The potion can do nothing more to her."
    elif ivy.status == 'on_training':
        "You shouldn't try this while Ivy is a client.  Her husband knows she's here and may cause trouble."
    elif ivy.status == "post_training" and ivy.in_area('house'):
        "Ivy's husband knows she's here and may cause trouble.  Better safe the transformation potion for someone else."
    else:
        "She doesn't want a drink from you here."
    return

# Use Water Bowl
label use_wb_ivy:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
    return

# Use Will Tamer
label use_wt_ivy:
    if ivy.has_tag('transformed'):
        "She's already been transformed.  The Will-Tamer can do nothing more to her now."
    elif ivy.in_area('house'):
        if ivy.has_tag('will_tamer_this_week'):
            "You've already used the Will-Tamer on Ivy this week.  Let its effects continue to work on her brain for a few days.  You can try using it again next week."
        elif ivy.will_tamer_count == 0:
            call ivy_update_media from _call_ivy_update_media_8
            wt_image ivy.image
            if ivy.has_tag('domme_visit_now'):
                ivy.c "A collar?  Did you want me to put that on you?"
                player.c "I think it would look nice on you, Mistress."
                wt_image intro_wife_visit_4_3
                ivy.c "It's not normal for a submissive to collar their Domme, is it?"
                wt_image intro_wife_collar_1_1
                player.c "No, but would you mind trying it on for me anyway?  I think it'll look great on you."
            elif ivy.has_tag('crawl_visit_now') and ivy.has_tag('crawled_wearing_tail'):
                ivy.c "A collar?  Please don't make me wear that.  Wearing a tail was humiliating enough."
                wt_image intro_wife_collar_1_1
                player.c "If you can wear a tail for me, you can certainly wear a collar."
            elif ivy.has_tag('crawl_visit_now'):
                ivy.c "A collar?  Don't you think expecting me to crawl is humiliating enough?"
                wt_image intro_wife_collar_1_1
                player.c "I haven't yet decided how much I want to humiliate me.  Put this on while I decide."
            elif ivy.has_tag('submissive_visit_now'):
                ivy.c "A collar?  Do you want me to look like a slavegirl?"
                wt_image intro_wife_collar_1_1
                player.c "Why not?  It's a good look for you."
            else:
                ivy.c "A collar?  Are we role-playing today?"
                player.c "Sort of.  Try it on."
                wt_image intro_wife_collar_1_1
                ivy.c "Okay, but I'm not going to pretend to be your slavegirl, if that's what you're expecting."
            wt_image intro_wife_collar_1_2
            "She claws briefly at the Will-Tamer, as she feels it worm it's way into her brain ..."
            wt_image intro_wife_collar_1_3
            "... then after a final, accusatory look in your direction she stops ..."
            wt_image intro_wife_collar_1_4
            "... and stares vacantly as the Will-Tamer re-wires her into a more docile, compliant version of herself."
            wt_image ivy.image
            "You remove the collar before it can make too much of a mess of her brain.  She seems to want to ignore having worn it."
            $ ivy.will_tamer_count = 1
            add tags 'will_tamer_this_week' to ivy
            change ivy submission by 10
            change ivy resistance by -15 notify
        elif ivy.will_tamer_count == 1:
            call ivy_update_media from _call_ivy_update_media_9
            wt_image ivy.image
            if ivy.has_tag('domme_visit_now'):
                player.c "Time to wear your collar again, Mistress."
                wt_image intro_wife_visit_4_3
            else:
                player.c "Time to wear your collar again, Ivy."
            ivy.c "I don't want to wear that again.  Yet for some reason I feel like I should.  Why is that?"
            wt_image intro_wife_collar_1_1
            player.c "Don't think about it too much.  It's easier if you just do what the collar wants you to."
            wt_image intro_wife_collar_1_2
            "She only claws the Will-Tamer for a moment, as she feels the now familiar sensation of it worming it's way into her brain ..."
            wt_image intro_wife_collar_1_3
            "... then with a brief, accusatory look in your direction she stops ..."
            wt_image intro_wife_collar_1_4
            "... and stares vacantly as the Will-Tamer resumes re-wiring her into a more docile, compliant version of herself."
            wt_image ivy.image
            "You remove the collar before it can make too much of a mess of her brain.  She seems to want to ignore having worn it."
            $ ivy.will_tamer_count = 2
            add tags 'will_tamer_this_week' to ivy
            change ivy submission by 10
            change ivy resistance by -15 notify
        else:
            "Better not.  Any more time in the Will-Tamer and it's likely to claim Ivy.  Her husband knows she's here and may cause trouble if that happens."
    else:
        "You shouldn't try putting a collar on her here."
    return

########### TIMERS ###########
## Common Timers
# End Training Permanently
label ivy_end_training:
    ## NOTE: use unmodded stats, not 'test' function, so don't pick up temporary modifiers, etc.
    if ivy.sos > 0:
        wt_image intro_wife_visit_1_2
        "Your engagement to train [ivy.full_name] has ended. You receive an email from her husband."
        husband_ivy "{i}I'm impressed!.  You actually managed to train my wife.{/i}"
        if ivy.anal_count > 0:
            extend "{i} She was always so nervous about anal, I didn't even want to mention it.  Now she's offering her ass to me regularly.{/i}"
        if ivy.has_tag('dommed_you'):
            extend "{i} Her willingness to take control in the bedroom is a real turn on.{/i}"
        if ivy.has_tag('stripped_for_you'):
            extend "{i} I love the way she likes to tease me now with strip teases.{/i}"
        if ivy.has_tag('bj_training'):
            extend "{i} She was always good at giving head, but the attention she pays my cock is quite amazing.{/i}"
        if ivy.has_tag('had_adventurous_sex'):
            extend "{i} Some of the things she's been getting us to try must be right out of the Kama Sutra.{/i}"
        if ivy.serve_count > 0:
            extend "{i} Having her spend the whole evening serving me is even more fun than it sounds.{/i}"
        if ivy.has_tag('spanking_orgasm'):
            extend "{i} It's so sexy when she asks to be spanked.{/i}"
        if ivy.crawl_count > 0:
            extend "{i} I don't know how you discovered her kink for crawling, but it really revs her up, and me, too.{/i}"
        extend "{i} I'll leave a positive review for you!{/i}"
        sys "The boost to your reputation from successfully training Ivy will attract new prospective clients next week.  You can spend the time before then doing other things."
        call convert(ivy,"satisfied", False, True) from _call_convert_185
    elif ivy.orgasm_count > 0:
        wt_image intro_wife_visit_1_2
        "Your engagement to train [ivy.full_name] has ended. You receive an email from her husband."
        husband_ivy "{i}I don't think Ivy learned anything, but she seemed to have fun visiting you, at least some of the time.  I'll leave a positive review for you.  Good luck with the wife training business.{/i}"
        if player.reputation < 0:
            sys "You didn't successfully train her, but the boost to your reputation from showing her a good time will attract new prospective clients next week.  You can spend the time before then doing other things."
            $ player.reputation = 0
        $ living_room.remove_action(ivy.current_client_action)
    else:
        wt_image intro_wife_visit_1_2
        "Your engagement to train [ivy.full_name] has ended. You didn't successfully train her, and she didn't enjoy her time with you enough to get a reputation boost from her husband."
        if player.reputation < 0:
            $ title = "What now?"
            menu:
                "End game and try again":
                    jump end_game
                "Go on to the next group of clients":
                    sys "You'll be presented with new prospective clients next week.  You can spend the time before then doing other things."
                    $ player.reputation = 0
        call convert(ivy,"unsatisfied", True, True) from _call_convert_186
    if ivy.has_tag('love_potion_used') and not ivy.has_tag('unsatisfied'):
        "A little while later you get a message from Ivy, too."
        ivy.c "{i}I hope I can still see you even though my training's over.  I so love spending time with you!  My husband and I have an open relationship, and he's okay with me still seeing you.  I hope you are, too?  Please call!  ~ XOXO Ivy"
    wt_image current_location.image
    return

# Start Day
label ivy_start_day:
    # At Start of Day, Relocate Character to Proper Location if they have been converted or Dismiss
    call character_location_return(ivy) from _call_character_location_return_661
    if 'ivy_check_messages_first' in living_room.exit_break_labels:
        "You move to a new city and set up an online profile advertising your services.  You get your first inquiry quickly.  Check your messages."
    if day == 5 and ivy.status == 'on_training' and not ivy.has_tag('first_friday_message_given'):
        add tags 'first_friday_message_given' to ivy
        sys "Today is Friday.  You can't hold regular training sessions on Fridays, but you can choose one client each week for a special weekend training session.  You need 15 Energy to arrange a weekend training session."
    if day == 1 and ivy.status == 'on_training' and not ivy.has_tag('new_week_message_given'):
        add tags 'new_week_message_given' to ivy
        sys "Today's Monday and the start of a new week.  Your Energy has been restored to full.  You can now arrange another regular training session with Ivy, either today or any day this week up until Thursday."
        sys "Training can sometimes be helped by gifting items to the client.  Lingerie (from the Eros Store) and a butt plug (from the Steel Trap) are items that could affect Ivy's training, depending on how that training is going."
    return

# End Day
label ivy_end_day:
    if ivy.status == "on_training":
        rem tags 'successful_talk_today' 'already_strip_trained_today' from ivy
        call character_location_return(ivy) from _call_character_location_return_662
    if ivy.has_tag('on_stage_now'):
        rem tags 'on_stage_now' 'watched_today' from ivy
    if ivy.has_tag('trained_today') and not ivy.has_tag('first_training_message_given'):
        add tags 'first_training_message_given' to ivy
        if day!= 4:
            sys "You can only arrange one regular training session with a client each week, so that's it for regular evening sessions with Ivy for this week. You can use the remaining days from now to Thursday to explore or rest or work some odd jobs to earn money."
        else:
            sys "You can only arrange one regular training session with a client each week, so that's it for regular evening sessions with Ivy for this week."
        sys "Your next opportunity to train Ivy will be this coming Friday, when weekend training sessions become available.  Make sure you have 15 Energy left by Friday in order to arrange a weekend training session."
    if ivy.status == 'post_training':
        rem tags 'domme_visit_now' 'submissive_visit_now' 'crawl_visit_now' 'strip_visit_now' 'sex_visit_now' 'watched_today' from ivy
    return

# End Week
label ivy_end_week:
    $ ivy.visit_count_total += ivy.visit_count
    $ ivy.visit_count = 0
    if ivy.has_item(butt_plug) and not ivy.has_tag('used_butt_plug'):
        add tags 'used_butt_plug' to ivy
    if ivy.submissive_visit_timer > 0:
        $ ivy.submissive_visit_timer -= 1
    return

## Club Labels
label ivy_stage_notice:
    ## Exhi Swinger Discussion Not Complete?
    if ivy.stripper_discussion == 1 and ivy.status == "post_training" and not ivy.has_tag('unsatisfied'):
        "This private location with strict confidentiality rules would be a safe place for Ivy to tease an audience full of men."
    return

label ivy_stage_call:
    # this runs when has tag 'showgirl' and you visit the Club
    if player.has_tag('stage_visited_today'):
        if ivy.has_tag('on_stage_now'):
            $ ivy.location = stage
    else:
        $ ivy.location = stage
        add tags 'on_stage_now' to ivy
        if ivy.stripper_discussion == 3:
            call ivy_update_media from _call_ivy_update_media_10
            wt_image intro_wife_strip_outfit_1_1
            "As you approach the stage, you see [ivy.name]. She spots you and approaches."
            ivy.c "Wow!  I love this place!!  Thanks for getting me in here.  I'm about to start my first show soon, if you'd like to stick around and watch?  I just need to change into my apron."
            player.c "Apron?"
            ivy.c "Watch the show and you'll see."
            $ ivy.stripper_discussion = 4
    return

label ivy_stage_send_home:
    call character_location_return(ivy) from _call_character_location_return_663
    return

label ivy_swingers_room_call:
    # NOTE: not possible to convert Ivy to your girlfriend yet; this is just placeholder coding
    if ivy.can_be_interacted:
        add tags 'in_swingers_room_now' to ivy
    else:
        "You can't find Ivy right now, or you'd ask her to join you."
    return

label ivy_swingers_room_send_home:
    # NOTE: not possible to convert Ivy to your girlfriend yet; this is just placeholder coding
    rem tags 'in_swingers_room_now' from ivy
    call character_location_return(ivy) from _call_character_location_return_664
    return

## Client Specific Timers
label ivy_trigger_used:
    if ivy.has_tag('crawl_visit_now') or ivy.has_tag('strip_visit_now'):
        wt_image intro_wife_visit_2_1
        player.c "Before we get started, Ivy.  There's something important I need to say."
        ivy.c "What is it?"
        player.c "[ivy.trigger_phrase]."
        wt_image intro_wife_visit_2_35
        ivy.c "Oh!  That is important."
        $ title = "What now?"
        menu:
            "Have her bark like a dog":
                player.c "Bark like a dog for me, Ivy."
                wt_image intro_wife_visit_2_2
                ivy.c "Of course!  I'd love to bark for you.  WOOF!  WOOF!  WOOF!!"
            "Be eye candy":
                player.c "You'd like to be eye candy for me, Ivy.  A nice decoration for around my house."
                wt_image intro_wife_visit_2_3
                ivy.c "Of course.  I was hoping today I could be a decoration for your house.  Do I look okay like this?"
                add tags 'trigger_clothed_now' to ivy
                $ title = "Is this good?"
                menu menu_ivy_trigger_menu_1:
                    "Take her top off" if ivy.has_tag('trigger_clothed_now'):
                        rem tags 'trigger_clothed_now' from ivy
                        add tags 'trigger_top_off_now' to ivy
                        wt_image intro_wife_visit_2_40
                        player.c "Let me help get your top off."
                        wt_image intro_wife_visit_2_5
                        ivy.c "Am I a nice decoration now?"
                        jump menu_ivy_trigger_menu_1
                    "Take the skirt off" if ivy.has_tag('trigger_top_off_now'):
                        rem tags 'trigger_top_off_now' from ivy
                        add tags 'trigger_skirt_off_now' to ivy
                        wt_image intro_wife_visit_2_6
                        player.c "You'd look better with your skirt off."
                        wt_image intro_wife_visit_2_7
                        ivy.c "Am I a nice decoration now?"
                        jump menu_ivy_trigger_menu_1
                    "Take the bra off" if ivy.has_tag('trigger_skirt_off_now'):
                        rem tags 'trigger_skirt_off_now' from ivy
                        add tags 'trigger_bra_off_now' to ivy
                        wt_image intro_wife_visit_2_8
                        player.c "You'd look better with your bra off."
                        wt_image intro_wife_visit_2_9
                        ivy.c "Am I a nice decoration now?"
                        jump menu_ivy_trigger_menu_1
                    "Take the panties off" if ivy.has_tag('trigger_bra_off_now'):
                        rem tags 'trigger_bra_off_now' from ivy
                        add tags 'trigger_panties_off_now'to ivy
                        wt_image intro_wife_visit_2_10
                        player.c "You'd look better with your panties off."
                        wt_image intro_wife_visit_2_41
                        ivy.c "Am I a nice decoration now?"
                        jump menu_ivy_trigger_menu_1
                    "Put your clothes back on" if not ivy.has_tag('trigger_clothed_now'):
                        rem tags 'trigger_top_off_now' 'trigger_skirt_off_now' 'trigger_bra_off_now' 'trigger_panties_off_now' from ivy
                        add tags 'trigger_clothed_now' to ivy
                        player.c "Let me see you clothed again."
                        if ivy.has_tag('trigger_top_off_now'):
                            wt_image intro_wife_visit_2_40
                        elif ivy.has_tag('trigger_skirt_off_now'):
                            wt_image intro_wife_visit_2_6
                        else:
                            wt_image intro_wife_visit_2_8
                        ivy.c "Okay"
                        wt_image intro_wife_visit_2_3
                        ivy.c "Am I a nice decoration now?"
                        jump menu_ivy_trigger_menu_1
                    "That's fine":
                        player.c "Yes, you look good like that, Ivy.  Stay like that."
                        ivy.c "I feel like staying like this for as long as you'd enjoy looking at me."
                        if ivy.has_tag('trigger_clothed_now'):
                            "You look at her for a while, then eventually release her from her trigger."
                        else:
                            "You look at her for a while, then eventually have her put her clothes back on and release her from her trigger."
                rem tags 'trigger_clothed_now' 'trigger_top_off_now' 'trigger_skirt_off_now' 'trigger_bra_off_now' 'trigger_panties_off_now' from ivy
            "Nothing":
                player.c "I just wanted to make sure that worked."
                ivy.c "You wanted to make sure what worked?"
                player.c "Nothing.  You're released now."
        notify
    elif ivy.has_tag('domme_visit_now'):
        wt_image intro_wife_visit_4_1
        player.c "Before we get started, Mistress.  There's something important I need to say."
        ivy.c "What is it?"
        player.c "[ivy.trigger_phrase]."
        wt_image intro_wife_visit_4_2
        ivy.c "Oh!  That is important."
        $ title = "What now?"
        menu:
            "Have her bark like a dog":
                player.c "Bark like a dog for me, Mistress."
                ivy.c "Of course!  I'd love to bark for you.  WOOF!  WOOF!  WOOF!!"
            "Have her suck you off":
                player.c "Instead of going through the whole domination thing today, just get on your knees and suck my cock until I cum, Mistress."
                wt_image intro_wife_visit_4_9
                ivy.c "Of course.  That's exactly what I should do."
                wt_image intro_wife_bj_4_1
                "There's no need to fear being blue balled today ..."
                wt_image intro_wife_bj_4_3
                "... Mistress' only thought right now is to make your cock and balls feel good ..."
                wt_image intro_wife_bj_4_2
                "... a task she's quite adept at when she sets her mind - and lips and tongue and hands - to."
                wt_image intro_wife_bj_4_4
                player.c "[player.orgasm_text]"
                wt_image intro_wife_visit_4_9
                ivy.c "That wasn't what I was planning on doing coming over here, but once I got here I knew that sucking you off was exactly what I should do."
                $ ivy.hypno_blowjob_count += 1
                $ ivy.hypno_swallow_count += 1
                orgasm
            "Nothing":
                player.c "I just wanted to make sure that worked."
                ivy.c "You wanted to make sure what worked?"
                player.c "Nothing.  You're released now."
        notify
    elif ivy.has_tag('sex_visit_now') or ivy.has_tag('submissive_visit_now'):
        wt_image intro_wife_visit_3_3
        player.c "Before we get started, Ivy.  There's something important I need to say."
        ivy.c "What is it?"
        player.c "[ivy.trigger_phrase]."
        wt_image intro_wife_visit_3_2
        ivy.c "Oh!  That is important."
        $ title = "What now?"
        menu:
            "Have her bark like a dog":
                player.c "Bark like a dog for me, Ivy."
                wt_image intro_wife_visit_3_15
                ivy.c "Of course!  I'd love to bark for you.  WOOF!  WOOF!  WOOF!!"
            "Have her pose pretty":
                add tags 'trigger_neutral_now' to ivy
                player.c "Pull your top down and pose pretty for me."
                wt_image intro_wife_visit_3_15
                ivy.c "Of course.  That's exactly what I want to do for you."
                wt_image intro_wife_visit_3_74
                ivy.c "Is this pretty enough for you?"
                $ title = "Is this position good?"
                menu menu_ivy_trigger_menu_3:
                    "Sluttier" if not ivy.has_tag('trigger_slutty_now'):
                        rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
                        add tags 'trigger_slutty_now' to ivy
                        player.c "Act sluttier."
                        wt_image intro_wife_visit_3_73
                        ivy.c "I'm a dirty girl who likes to suck and fuck!"
                        jump menu_ivy_trigger_menu_3
                    "Even sluttier" if ivy.has_tag('trigger_slutty_now') and not ivy.has_tag('trigger_sluttier_now'):
                        rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
                        add tags 'trigger_sluttier_now' to ivy
                        player.c "Behave even sluttier."
                        wt_image intro_wife_visit_3_16
                        ivy.c "My nipples are hard because I'm a dirty slut who's hoping she'll be allowed to suck your cock."
                        jump menu_ivy_trigger_menu_3
                    "More submissive" if not ivy.has_tag('trigger_submissive_now'):
                        rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
                        add tags 'trigger_submissive_now' to ivy
                        player.c "Behave more submissively."
                        wt_image intro_wife_visit_3_81
                        ivy.c "Like this, Sir?"
                        jump menu_ivy_trigger_menu_3
                    "Even more submissive" if not ivy.has_tag('trigger_submissive_now') and not ivy.has_tag('trigger_more_submissive_now'):
                        rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
                        add tags 'trigger_more_submissive_now' to ivy
                        player.c "No, be even more submissive.  Like a traditional Asian housewife.  You know how they behave, don't you?"
                        wt_image intro_wife_visit_3_88
                        ivy.c "Yes, Sir.  That's exactly how I feel like behaving in your presence right now."
                        jump menu_ivy_trigger_menu_3
                    "Go back to the start" if not ivy.has_tag('trigger_neutral_now'):
                        rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
                        player.c "Go back to the way you started."
                        wt_image intro_wife_visit_3_74
                        ivy.c "Like this?"
                        jump menu_ivy_trigger_menu_3
                    "That's fine":
                        player.c "That's nice.  Stay like that."
                        ivy.c "I feel like staying just like this."
                        "You look at her for a while, then eventually have her cover herself up and release her from her trigger."
                rem tags 'trigger_neutral_now' 'trigger_slutty_now' 'trigger_sluttier_now' 'trigger_submissive_now' 'trigger_more_submissive_now' from ivy
            "Have her play with herself":
                player.c "You're feeling horny, Ivy.  Touch yourself."
                wt_image intro_wife_visit_3_17
                ivy.c "I'm so glad you don't mind me touching myself!  I'm so horny right now."
                wt_image intro_wife_visit_3_63
                ivy.c "I was afraid I would soak through my panties."
                wt_image intro_wife_visit_3_67
                ivy.c "Mmmm.  This feels so nice."
                wt_image intro_wife_visit_3_66
                ivy.c "I probably shouldn't be doing this while you're watching, though.  That's embarrassing."
                $ title = "What do you tell her?"
                menu:
                    "She's too horny to stop":
                        player.c "You're too horny to stop, Ivy, no matter how inappropriately you're behaving."
                        wt_image intro_wife_visit_3_67
                        ivy.c "This is humiliating.  I can't stop touching myself."
                        wt_image intro_wife_visit_3_68
                        ivy.c "I need to feel my fingers inside me."
                        wt_image intro_wife_visit_3_69
                        ivy.c "I shouldn't be doing this while you're watching, but I can't help myself."
                        wt_image intro_wife_visit_3_70
                        ivy.c "OH ... I'M CUMMINNGGG!!!"
                        wt_image intro_wife_visit_3_66
                        ivy.c "I'm sorry about that.  I don't know why I was so horny all of a sudden."
                        $ ivy.hypno_masturbation_count += 1
                        $ ivy.hypno_orgasm_count += 1
                        change player energy by -energy_very_short
                    "She's feeling very embarrassed":
                        player.c "You're feeling very embarrassed, Ivy, and keep doing embarrassing things."
                        wt_image intro_wife_visit_3_67
                        ivy.c "This is humiliating.  I want you to see me touching myself."
                        wt_image intro_wife_visit_3_78
                        ivy.c "I want to show you my ass, and even my asshole."
                        wt_image intro_wife_visit_3_83
                        ivy.c "I shouldn't be treated like a woman, men should treat me like a dirty fucking slut!!"
                        wt_image intro_wife_visit_3_88
                        ivy.c "Oh, wow!  I don't know why I'm being such a stupid cunt and embarrassing myself like this??"
                "That was fun, but it's time to release her from her trigger now."
            "Nothing":
                player.c "I just wanted to make sure that worked."
                ivy.c "You wanted to make sure what worked?"
                player.c "Nothing.  You're released now."
        notify
    return


# Convert Character to Domme
label ivy_convert_domme:
    call convert(ivy,"domme") from _call_convert_187
    sys "Ivy now thinks of herself as a Domme.  Future sessions with her may become more intense."
    return


# Convert Character to Showgirl
label ivy_convert_showgirl:
    rem tags 'waiting_for_club_access' from ivy
    $ ivy.stripper_discussion = 3
    call convert(ivy, 'showgirl') from _call_convert_188
    return


################################### NOTES ###################################
# Trainer Type: Playboy     is      player.has_tag('supersexy')
# Trainer Type: Hypnotist     is      player.has_tag('hypnotist')
# Trainer Type: Dominant     is      player.has_tag('dominant')


## Client Status
#0 = not yet prospect
#1 = prospect, .status = "available_to_be_client" and .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = client, .status = "on_training"
#4 = unsatisfied former client, add tags 'unsatisfied' and .status = "post_training"
#5 = satisfied former client, add tags 'satisfied' and .status = "post_training"
#6 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#7 = satisfied former client not continuing, rem tags 'continuing_actions' and .status = "post_training"
#8 = post continuing actions, add tags 'post_continuing_actions' and .status = "post_training"

## Minor Client Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
