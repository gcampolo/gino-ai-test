## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
## register_package chelsea name "Chelsea, The Chubby" description "Allows Chelsea to be client." dependencies core
register chelsea_pregame 10 in core as "Chelsea the Chubby"

# Pregame
label chelsea_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Chelsea the Chubby (Alex Chance)")]
    model_credits += [('bit', "Adriana the Lesbian (Adriana Chechik)")]
    # model_credits += [('bit', "Savannah the Lesbian (??)")] ## NEED add once figure out who she is

    ## Character Definition
    # chelsea = Person(Character("Chelsea", who_color="#400040", what_color="#400040", window_background = "#FFFFFFAA"), "chelsea", cut_portrait = True, prefix = "", suffix = "the Chubby", resistance = 70, training_period = 9)
    # chelsea = Person(Character("Chelsea", who_color="#bf00bf", what_color="#bf00bf", window_background=gui.dialogue_background_medium_font_color), "chelsea", cut_portrait = True, prefix = "", suffix = "the Chubby", resistance = 70, training_period = 10, hypno_trigger_resistance_threshold = 20, min_reputation = 0)
    ## new colours for chelsea:
    chelsea = Person(Character("Chelsea", who_color="#00cdcd", what_color="#00cdcd"), "chelsea", cut_portrait = True, prefix = "", suffix = "the Chubby", resistance = 70, training_period = 10, hypno_trigger_resistance_threshold = 20, hypno_trigger_sessions_threshold = 7, min_reputation = 0)
    chelsea.trigger_phrase = "Fat girls do as they're told"
    chelsea.your_name = "Big Guy"

    # Other Characters
    # note: Characters only appear in dialogue, Persons can be interacted with
    # note: character dialogue just uses name, while person dialogue uses name.c
    # note: all persons must have a _portait image, while characters do not

    # Navy
    husband_chelsea = Character("[chelsea.name]'s Husband", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)

    ## Actions
    # Training Actions
    chelsea.action_talk = chelsea.add_action("Talk to her", label = "_talk", condition = "chelsea.can_be_interacted and chelsea.has_tag('first_visit') and chelsea.status == 'on_training'")
    chelsea.action_glory_hole = chelsea.add_action("Take her to a glory hole", label = "_glory", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and chelsea.status == 'on_training'")
    chelsea.action_discipline = chelsea.add_action("Break her resistance with discipline", label = "_discipline", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and not chelsea.has_tag('no_spanking') and chelsea.status == 'on_training'")
    chelsea.action_seduce = chelsea.add_action("Seduce her", label = "_seduce", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and chelsea.status == 'on_training'")
    chelsea.action_work_out = chelsea.add_action("Have her work out", label = "_work_out", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and chelsea.status == 'on_training'")
    chelsea.action_diet = chelsea.add_action("Work on her diet", label = "_diet", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and not chelsea.has_tag('diet_shopping_complete') and chelsea.status == 'on_training'")
    chelsea.action_model = chelsea.add_action("Have her model lingerie for you", label = "_model", condition = "chelsea.can_be_interacted and not chelsea.has_tag('first_visit') and chelsea.status == 'on_training'")
    # Girlfriend Actions
    #chelsea.action_girlfriend_hypnosis = chelsea.add_action("Hypnotize Her",label="_hypnosis_start_girlfriend", condition="chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend')) and player.test('hypnosis_level', 0) and chelsea.status == 'post_training'")
    chelsea.action_girlfriend_actions = chelsea.add_action("Spend time with her",label="_girlfriend_actions", condition="chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend')) and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    chelsea.action_girlfriend_actions = chelsea.add_action("Take her on a date",label="_girlfriend_date", condition="chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend')) and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    chelsea.action_girlfriend_butt_play = chelsea.add_action("Butt play",label="_girlfriend_butt_play", condition="chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend')) and chelsea.anal_status > 2 and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    chelsea.action_dominate = chelsea.add_action("Dominate her",label="_dominate", condition="chelsea.can_be_interacted and chelsea.has_any_tag('girlfriend', 'hypno_girlfriend') and chelsea.dominate_status > 0 and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    # Lesbian Action
    chelsea.action_arrange_lesbian = chelsea.add_action("Arrange lesbian session", label="_lesbian", condition="chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend') or chelsea.has_tag('continuing_actions')) and (chelsea.has_tag('likes_girls') or chelsea.lesbian_status > 0) and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    # Slavegirl Actions
    chelsea.action_rename = chelsea.add_action("Rename her", label="_rename", condition="chelsea.has_tag('slavegirl')")
    chelsea.action_your_name = chelsea.add_action("Tell her how to address you", label="_your_name", condition="chelsea.has_tag('slavegirl')")
    chelsea.action_slavegirl = chelsea.add_action("Spend time with her", label="_slavegirl_actions", condition="chelsea.can_be_interacted and chelsea.has_tag('slavegirl') and chelsea.in_area('house')")
    chelsea.action_sg_elsa = None # note: purposefully none until converted to slave to avoid circle issue with Elsa's name in the action

    # chelsea.action_dismiss = chelsea.add_action("Dismiss her", label="_dismiss", condition="chelsea.has_tag('continuing_actions')")
    chelsea.action_lend_to_master_m = chelsea.add_action("Lend her to Master M", label="_lend_to_master_m", condition="chelsea.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave') and chelsea.in_area('house')")

    # Continuing Actions
    chelsea.action_spend_time = chelsea.add_action("Spend time with her",label="_spend_time", condition="chelsea.can_be_interacted and chelsea.has_tag('continuing_actions') and not chelsea.has_tag('frozen') and chelsea.in_area('house')")
    # Other
    chelsea.action_end_session = chelsea.add_action("Send her home", label="_end_session", condition = "not chelsea.has_any_tag('first_visit', 'post_continuing_actions', 'shut_off_end_session') and chelsea.in_area('house')")
    # Relation Status
    chelsea.relationship_action = bedroom.add_action("[chelsea.full_name]", label = chelsea.short_name + "_relationship_status", context = "_relationship_status", condition = "chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend') or chelsea.has_tag('continuing_actions')")


    ## Tags
    # Common Character Tags
    chelsea.add_tags('es_store_content', 'first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    chelsea.change_status("available_to_be_client")
    jewelry_chelsea = Item('Jewelry', 'jwc', with_examine = True, with_give = True)

    # Remove Default Desire Stat and Create Custom Desire Stat
    chelsea.add_stat('desire_c')
    chelsea.remove_stat('desire')
    chelsea.show_in_statblock.remove('desire')
    chelsea.show_in_statblock.remove('submission')
    chelsea.show_in_statblock.insert(1, 'desire_c')
    stats['desire_c'] = 'Desire to Change'
    pb.tags.add("show_desire_c")
    recorded_stats['desire_c'] = 'desire'

    # Add Hypno Actions
    chelsea.add_hypno_actions(['sos', 'desire_c', 'resistance'],implant = False)
    chelsea.dominating_her_hypno_action = chelsea.add_action("Dominating her", label = "_dominating_her_hypnosis", context = "_hypnosis", condition = "chelsea.has_tag('girlfriend') and chelsea.dominate_status > 1 and chelsea.hypno_re_dominate < 2")
    chelsea.anal_sex_hypno_action = chelsea.add_action("Anal sex", label = "_anal_hypnosis", context = "_hypnosis", condition = "chelsea.has_tag('girlfriend') and chelsea.anal_status > 1 and chelsea.hypno_re_anal < 2")
    chelsea.sex_with_women_hypno_action = chelsea.add_action("Sex with women", label = "_lesbian_hypnosis", context = "_hypnosis", condition = "chelsea.has_tag('girlfriend') and not chelsea.has_tag('likes_girls') and chelsea.lesbian_status > 1 and chelsea.hypno_re_lesbian < 2")
    chelsea.your_relationship_hypno_action = chelsea.add_action("Your relationship", label = "_your_relationship_hypnosis", context = "_hypnosis", condition = "chelsea.has_tag('girlfriend') or chelsea.has_tag('continuing_actions')")


    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('chelsea_start_day_early_events', priority = -25) # runs earlier than other start day events
    start_day_labels.append('chelsea_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    chelsea.add_stats_with_value('club_outfit', 'event_week', 'gf_event', 'gf_outfit', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_titfuck_count', 'hypno_swallow_count', 'random_number', 'visit_outfit')

    # Character Specific Variables
    chelsea.add_stats_with_value('anal_fingering_count', 'anal_status', 'bra_fitting_status', 'club_date_count', 'cum_lick_count', 'discipline_count', 'exercise_count', 'glory_hole_count', 'hypno_re_anal', 'hypno_re_dominate', 'hypno_re_lesbian', 'lee_event_status')
    chelsea.add_stats_with_value('lesbian_club_count', 'lesbian_outfit', 'lesbian_status', 'lesbian_threesome_count', 'mood', 'relationship_counter', 'relationship_warnings_shut_off', 'sex_status', 'shock_count', 'spanked', 'visit_sex_count', 'visit_talk_count', 'weekend_boot_camp_status', 'seduce_action_status', 'youth_skirt_spanking', 'youth_status')
    # sex_status key: 1: gave BJ or TJ, 2: had sexual intercourse
    chelsea.add_stats_with_value('dominate_status',value=1)


    ######## EXPANDABLE MENUS #######
    ## Weekend Training
    chelsea_weekend_training_menu = ExpandableMenu("What do you have in mind for [chelsea.name] this weekend?", pre_label = 'chelsea_pre_weekend', post_label = 'chelsea_post_weekend')
    # note: these don't have to be defined in pregame, can be added in game
    chelsea.choice_weekend_hypnotize =  chelsea_weekend_training_menu.add_choice("Hypnosis Therapy", "chelsea_weekend_training_hypnotize", condition = "player.can_hypno(chelsea)")
    chelsea.choice_weekend_boot_camp =  chelsea_weekend_training_menu.add_choice("Boot Camp", "chelsea_weekend_training_boot_camp")
    chelsea.choice_weekend_sex_therapy =  chelsea_weekend_training_menu.add_choice("Sexual Self-esteem Therapy", "chelsea_weekend_training_sex_therapy")
    chelsea.choice_weekend_shock_therapy =  chelsea_weekend_training_menu.add_choice("Shock Therapy", "chelsea_weekend_training_shock_therapy", condition = "chelsea.shock_count < 2")

    chelsea_girlfriend_date_menu = ExpandableMenu("Where do you take her?", cancelable = True)
    chelsea.choice_girlfriend_date_club = chelsea_girlfriend_date_menu.add_choice("To the Club (costs 10)", "chelsea_girlfriend_date_club", condition ="player.has_tag('club_access') and player.has_tag('club_first_visit_complete') and player.money - player.min_money >= 10")
    chelsea.choice_girlfriend_date_restuarant = chelsea_girlfriend_date_menu.add_choice("To a normal restaurant (costs 10)", "chelsea_girlfriend_date_restaurant", condition ="player.money - player.min_money >= 10")
    chelsea.choice_girlfriend_date_boat = chelsea_girlfriend_date_menu.add_choice("Boating (costs 20)", "chelsea_girlfriend_date_boat", condition ="chelsea.has_tag('toned') and player.money - player.min_money >= 20")
    chelsea.choice_girlfriend_date_massage = chelsea_girlfriend_date_menu.add_choice("Treat her to a massage", "chelsea_girlfriend_date_massage", condition ="chelsea.has_tag('bbw')")

  return

# Initial Contact Message
# OBJECT: Check Messages
label chelsea_message:
  husband_chelsea "{i}I love my wife, [chelsea.name], and I'm reaching out to you in the hopes that you can help her.{/i}"
  husband_chelsea "{i}[chelsea.name] is a beautiful woman, but she doesn't feel beautiful. She's struggled with weight issues her whole life. She goes on diets, then she goes off diets.{/i}"
  husband_chelsea "{i}She starts an exercise program, then she stops it. Then she tries another one. Then she spends a week on the couch overeating and crying herself to sleep.{/i}"
  husband_chelsea "{i}We've tried a personal trainer, but it didn't help. When I read your profile I realized I must really be getting desperate to think about sending her to you. But there you go. I am desperate.{/i}"
  husband_chelsea "{i}If you can help focus her desire to be fit so that she actually loses the weight, and is ready to do what she needs to keep it off, then I will try and not think about what you may be doing with her when the two of you are together.{/i}"
  husband_chelsea "{i}What I want out of this is a happy wife who feels good about herself and who's not ashamed to have sex with me because she feels bad about the way she looks.{/i}"
  call consider_contract(chelsea, "Reply to [chelsea.full_name]'s Husband") from _call_consider_contract_4
  if yesno == True:
    sys "You accept the assignment.  You have until the end of week [chelsea.training_limit] to complete it."
    if not player.has_tag('tutorial_message'):
      add tags 'tutorial_message' to player
      sys "You may hold one evening session each week to complete her training. If you have at least [energy_long.value] Energy left on Friday, you may also schedule a weekend session with a client of your choice."
  return

# Client Rejected
label chelsea_rejected:
  sys "You can no longer train [chelsea.full_name]."
  return

# Arrange Client Session
# OBJECT: Schedule Client Session
label chelsea_calling:
  # Check if client has already been trained this week
  if not chelsea.can_be_interacted:
    "You had an evening session with [chelsea.name] earlier this week. You need to wait until the weekend or next week for another session."
  else:
    call forced_movement(living_room) from _call_forced_movement_83
    summon chelsea
    $ chelsea.visit_count += 1
    call chelsea_update_media from _call_chelsea_update_media_1
    wt_image chelsea.image
    "You show [chelsea.name] to your living room."
    if 'first_visit' in chelsea.tags:
      sys "[chelsea.name]'s behavior is less likely to be influenced by the room she is in than most clients, as her Desire stat is her desire to change, and her Submission stat is not tracked."
  return

# Display Portrait
# CHARACTER: Display Portrait
label chelsea_update_media:
  if chelsea.has_tag('frozen'):
    pass
  elif chelsea.has_tag('slavegirl'):
    if chelsea.has_any_tag('slave_tied_now', 'slave_suspended_now', 'slave_decoration_now', 'slave_dildo_now' 'slave_plugged_now'):
      pass
    else:
      $ chelsea.change_image('chubby_slave_18')
  elif chelsea.has_tag('bound_inside_now'):
    $ chelsea.change_image('chubby_dominate_5_5')
  elif chelsea.has_tag('bound_outside_now'):
    $ chelsea.change_image('chubby_dominate_6_1')
  else:
    if chelsea.status == "post_training":
      if chelsea.has_tag('little_girl'):
        if chelsea.has_item(jewelry_chelsea):
          $ chelsea.change_image('chubby_youth_4_1')
        else:
          $ chelsea.change_image('chubby_youth_portrait_1')
      elif chelsea.has_tag('toned'):
        if chelsea.has_item(jewelry_chelsea):
          $ chelsea.change_image('chubby_toned_portrait_2')
        else:
          $ chelsea.change_image('chubby_toned_portrait_1')
      else:
        if chelsea.has_item(jewelry_chelsea):
          $ chelsea.change_image('chubby_bbw_portrait_2_1')
        else:
          $ chelsea.change_image('chubby_bbw_portrait_1_1')
    else:
      call chelsea_mood_test from _call_chelsea_mood_test
      if chelsea.has_tag('motivated'):
        $ chelsea.change_image('chubby_motivated_1')
      elif chelsea.has_tag('happy'):
        $ chelsea.change_image('chubby_happy_1')
      elif chelsea.has_tag('conflicted'):
        $ chelsea.change_image('chubby_conflicted_1')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label chelsea_examine:
    if chelsea.has_any_tag('frozen', 'bound_inside_now', 'bound_outside_now'):
        "[chelsea.name] waits where you left her."
    else:
        call chelsea_description_display from _call_chelsea_description_display
    return

# Talk to Character
label chelsea_talk:
    if 'first_visit' in chelsea.tags:
        wt_image chubby_conflicted_1
        player.c "I'm sure this is all quite new to you, [chelsea.name].  How were you feeling, coming over here tonight?"
        chelsea.c "Embarrassed. Stupid."
        player.c "Why do you say that?"
        wt_image chubby_conflicted_2
        "[chelsea.name] takes a deep breath."
        chelsea.c "I have a weight problem. I can't keep it off. I try sometimes, and I look and feel better for a little while, but I never stick with it. I end up back like this, fat and ugly. I can't bear to have my husband even look at me or touch me while I'm like this."
        player.c "Are you willing to work with me, [chelsea.name], to see if we can do something about that?"
        wt_image chubby_conflicted_1
        chelsea.c "I guess. I mean, yes. Yes, I am. That's why I'm here.  But no touching me, okay?  I know my husband said you could, but I'm not comfortable with that."
        $ title = "How do you respond?"
        menu:
            "That's a shame, you're extremely beautiful":
                wt_image chubby_conflicted_3
                player.c "That's a shame. You're extremely beautiful. I'm looking forward to getting to know you better - mentally and physically."
                player.c "I won't make you do anything you're not comfortable with. But I will insist that we become intimate. The only way this will work is if you turn yourself over to me, and trust me."
                wt_image chubby_conflicted_2
                player.c "I want to make love to you, [chelsea.name]. I've wanted that as soon as I set eyes on you at my doorway. If you agree to work with me, then you must also agree that we will be making love together, you and I. Do you agree?"
                "[chelsea.name] takes another deep breath before responding."
                wt_image chubby_conflicted_3
                chelsea.c "Okay. Yes, I agree, in principle. But, I may need a bit of time before I'm ready to take that step."
                change chelsea sos by 5
                change chelsea resistance by -5
            "We'll talk about this again, once we've made some progress":
                player.c "I understand. But you must understand, the only way this will work is if you trust me. I'll help you to become the woman you want to be, but you must allow me to decide how to keep you focussed on that task."
                wt_image chubby_conflicted_2
                player.c "As you start to make progress, I may expect you to please with your new and improved body. I think you'll enjoy that as well. The pleasure will be our mutual reward for the progress you're making, a positive feedback system to help keep you focused. That's the agreement I have with your husband. I want you to agree to it as well."
                "[chelsea.name] takes another deep breath before answering."
                wt_image chubby_conflicted_1
                chelsea.c "Okay. Yes, I agree."
                change chelsea desire_c by 5
            "For this to work, you need to let me make those decisions":
                player.c "Starting now, [chelsea.name], you need to let me make those decisions. The only way this will work is if you turn yourself over to me, and trust me. I won't make you do anything you're not comfortable with. But I will insist that you follow my instructions. If I don't have your obedience, I can't help you.  Do you agree to follow my instructions?"
                wt_image chubby_conflicted_2
                "[chelsea.name] takes another deep breath before answering."
                chelsea.c "Okay. Yes, I agree."
                change chelsea resistance by -10
        notify
        rem tags 'no_hypnosis' 'first_visit' from chelsea
    return

# Hypno Actions
label chelsea_hypnosis_start:
    if chelsea.has_tag('girlfriend') and current_location == bedroom:
        $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_1
        elif chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_2_7
        else:
            wt_image chubby_hypno_gf_toned_6
        player.c "Come here for a minute."
        chelsea.c "What is it?"
        call focus_image from _call_focus_image_50
        player.c "Look at this for me. Look at this and listen to me, [chelsea.name]. Listen to me. Listen to my voice and nothing else, [chelsea.name].  Only my voice.  Only my voice now."
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_6
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_6
        else:
            wt_image chubby_hypno_gf_toned_1
        "She quickly falls under your trance."
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_2
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_2
        else:
            wt_image chubby_hypno_gf_toned_2
        player.c "I want you to get comfortable for our talk. Show me your breasts, [chelsea.name]."
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_3
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_4
        else:
            wt_image chubby_hypno_gf_toned_3
        "[chelsea.name] exposes her ample bosom."
    elif chelsea.has_tag('continuing_actions') and current_location == living_room:
        $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        wt_image chubby_hypno_weekend_1
        chelsea.c "It's good to see you again."
        player.c "It's good to see you, too. Please look at this for me, [chelsea.name]."
        call focus_image from _call_focus_image_70
        player.c "Look at this and listen to me. Listen to me. Listen to my voice and nothing else, [chelsea.name]. Only my voice. Only my voice now."
        wt_image chubby_hypno_weekend_2
        "She soon falls under your trance."
        wt_image chubby_hypno_weekend_strip
        player.c "I want you to get comfortable for our talk. Show me your breasts, [chelsea.name]."
        wt_image chubby_hypno_weekend_breasts
        "[chelsea.name] proudly shows you her breasts."
        $ title = "Do you want her to pleasure you while you talk?"
        menu:
            "Yes, have her pleasure you":
                player.c "Put your tits to work while I talk to you, [chelsea.name]."
                wt_image chubby_hypno_weekend_3
                "She kneels downs and wraps her soft mounds around you, pumping them up and down your shaft as she listens to you."
                add tags 'hypno_sex_now' to chelsea
            "No, proceed like this":
                pass
    elif chelsea.has_tag('continuing_actions') and chelsea.visit_outfit == 4:
        $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        call forced_movement(outdoors) from _call_forced_movement_177  ## note: need to do this BEFORE charging hypno energy through hypno_session command
        summon chelsea no_follows
        change player energy by -10 # extra for travelling
        wt_image chubby_visit_bbw_4_2
        "You surprise [chelsea.name] in her lunchroom as she just finishes eating.  She's alone and the office is quiet, so this should be safe."
        chelsea.c "What are you doing here?"
        player.c "Since you were too busy to come see me, I thought I'd come see you. I have something I want you to look at."
        wt_image chubby_visit_bbw_4_39
        chelsea.c "What is ..."
        call focus_image from _call_focus_image_71
        player.c "It's this, [chelsea.name]. Look at this for me, [chelsea.name]. Look at this and listen to me. Listen to me. Listen to my voice and nothing else, [chelsea.name]. Only my voice. Only my voice now."
        wt_image chubby_visit_bbw_4_40
        "She soon falls under your trance."
        wt_image chubby_visit_bbw_4_5
        player.c "I want you to get comfortable for our talk, [chelsea.name].  Show me your breasts."
        wt_image chubby_visit_bbw_4_15
        $ title = "Do you want her to pleasure you while you talk?"
        menu:
            "Yes, have her pleasure you":
                player.c "Put your mouth to work while I talk to you, [chelsea.name]."
                wt_image chubby_visit_bbw_4_28
                "She kneels downs and wraps her lips around you as she listens to you."
                add tags 'hypno_sex_now' to chelsea
            "No, proceed like this":
                pass
        call character_location_return(chelsea) from _call_character_location_return_22
    elif chelsea.status == 'on_training':
        $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        summon chelsea
        if is_weekend():
            wt_image chubby_hypno_weekend_1
            "[chelsea.name] arrives for your weekend session uncertain as to what you have planned for her."
            player.c "Come in [chelsea.name], I want you to look at something for me."
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_motivated_3
            elif chelsea.has_tag('happy'):
                wt_image chubby_happy_1
            else:
                wt_image chubby_conflicted_2
            player.c "[chelsea.name], I want you to look at something for me."
        call focus_image from _call_focus_image_52
        player.c "[chelsea.name], I am going to talk with you and you are going to listen to me. Listen to me now, [chelsea.name]. Listen to me. Listen to my voice and nothing else, [chelsea.name]. Only my voice. Only my voice now."
        if is_weekend():
            wt_image chubby_hypno_weekend_2
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_hypno_motivated
            elif chelsea.has_tag('happy'):
                wt_image chubby_hypno_happy
            else:
                wt_image chubby_hypno_conflicted
        "She soon falls under your trance."
        if is_weekend():
            wt_image chubby_hypno_weekend_strip
        elif chelsea.has_tag('motivated'):
            wt_image chubby_hypno_motivated_strip
        player.c "[chelsea.name], you want me to be comfortable while we talk. You want to comfortable for our talk. If you bare your breasts, we will both be comfortable. Bare your breasts so we will both be comfortable, [chelsea.name]."
        if is_weekend():
            wt_image chubby_hypno_weekend_breasts
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_hypno_motivated_breasts
            elif chelsea.has_tag('happy'):
                wt_image chubby_hypno_happy_breasts
            else:
                wt_image chubby_hypno_conflicted_breasts
        if not player.has_tag('first_hypno_breasts_message'):
            add tags 'first_hypno_breasts_message' to player
            "[player.first_hypno_breasts_message_text]"
        "She exposes her ample chest to you."
    elif chelsea.has_tag('slavegirl'):
        add tags 'no_hypnosis' to chelsea
        "Hypnosis will no longer affect her in her current state."
        $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    else:
        "Not here."
        $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    # system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    return

label chelsea_desire_c_hypnosis:
    if chelsea.status != 'on_training':
        "You don't need to work on this through hypnosis any more. Try something else."
        $ chelsea.desire_c_hypno_action.backtrack = True ## this and the next two commands back you up to the menu of hypnosis options
        $ context = "chelsea_hypnosis"
        break_sequence
    else:
        if is_weekend():
            wt_image chubby_hypno_weekend_desire_c
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_hypno_motivated_desire_c
            elif chelsea.has_tag('happy'):
                wt_image chubby_hypno_happy_desire_c
            else:
                wt_image chubby_hypno_conflicted_desire_c
        "You work on [chelsea.name]'s desire to change, and in particular her motivation to stick to an exercise and healthy-diet regime."
        "When you've taken her as far as you can for today, you have her dress, then send her home. She doesn't exactly remember what the two of you did, but she feels an increased determination to change her body shape."
    # system now applies the stat gain and then goes on to the _desire_c_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    return

label chelsea_resistance_hypnosis:
    if chelsea.has_tag('girlfriend'):
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_4
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_3
        else:
            wt_image chubby_hypno_gf_toned_4
        "You work on lowering [chelsea.name]'s resistance to you. When you've taken her as far as you can for today, you let her rest. The suggestions you've made will take time to fully affect her thinking."
    elif chelsea.has_tag('continuing_actions') and current_location == living_room:
        if chelsea.has_tag('hypno_sex_now'):
            wt_image chubby_hypno_weekend_4
        else:
            wt_image chubby_hypno_weekend_resistance
        "You work on lowering [chelsea.name]'s resistance to you."
    elif chelsea.has_tag('continuing_actions') and chelsea.visit_outfit == 4:
        if chelsea.has_tag('hypno_sex_now'):
            wt_image chubby_visit_bbw_4_8
        else:
            wt_image chubby_visit_bbw_4_41
        "You work on lowering [chelsea.name]'s resistance to you."
    else:
        if is_weekend():
            wt_image chubby_hypno_weekend_resistance
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_hypno_motivated_resistance
            elif chelsea.has_tag('happy'):
                wt_image chubby_hypno_happy_resistance
            else:
                wt_image chubby_hypno_conflicted_resistance
            "You work on [chelsea.name]'s confidence in you, and reinforce the need for her to follow your instructions."
            "When you've taken her as far as you can for today, you have her dress, then send her home. She doesn't exactly remember what the two of you did, but she trusts you more and is more comfortable with the idea of consenting to whatever you may ask of her."
    # system now applies the stat gain and then goes on to the _resistance_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    return

label chelsea_sos_hypnosis:
    if chelsea.status != 'on_training':
        "You don't need to work on this through hypnosis any more. Try something else."
        $ chelsea.sos_hypno_action.backtrack = True ## this and the next two commands back you up to the menu of hypnosis options
        $ context = "chelsea_hypnosis"
        break_sequence
    else:
        if is_weekend():
            wt_image chubby_hypno_weekend_sense_of_self
        else:
            if chelsea.has_tag('motivated'):
                wt_image chubby_hypno_motivated_sense_of_self
            elif chelsea.has_tag('happy'):
                wt_image chubby_hypno_happy_sense_of_self
            else:
                wt_image chubby_hypno_conflicted_sense_of_self
        "You work on how [chelsea.name] feels about herself, and in particular raise her confidence in her own beauty and sexiness."
        "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she feels happier and more beautiful."
    return

label chelsea_your_relationship_hypnosis:
    if chelsea.has_tag('girlfriend'):
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_5
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_5
        else:
            wt_image chubby_hypno_gf_toned_5
        "You work on increasing [chelsea.name]'s satisfaction with her relationship with you."
        "When you've done as much as you can for today, you let her rest. The suggestions you've made will take time to fully affect her thinking."
    elif chelsea.has_tag('continuing_actions') and current_location == living_room:
        if chelsea.has_tag('hypno_sex_now'):
            wt_image chubby_hypno_weekend_8
        else:
            wt_image chubby_hypno_weekend_sense_of_self
        "You work on [chelsea.name]'s reservations about her relationship with you. Subtly, you reinforce concerns she has about her marriage and, more importantly, reinforce positive feelings she has about you."
    elif chelsea.has_tag('continuing_actions') and chelsea.visit_outfit == 4:
        if chelsea.has_tag('hypno_sex_now'):
            wt_image chubby_visit_bbw_4_7
        else:
            wt_image chubby_visit_bbw_4_42
        "You work on [chelsea.name]'s reservations about her relationship with you. Subtly, you reinforce concerns she has about her marriage and, more importantly, reinforce positive feelings she has about you."
    sys "[chelsea.name] is happier with your relationship."
    if player.has_tag('hypnotist') or player.hypnosis_level > 10:
        $ chelsea.relationship_counter += 1
    else:
        $ chelsea.relationship_counter += 0.5
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_20
    return

label chelsea_dominating_her_hypnosis:
    if chelsea.has_tag('girlfriend'):
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_4
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_3
        else:
            wt_image chubby_hypno_gf_toned_4
        "You work on increasing [chelsea.name]'s comfort level with being sexually dominated by you."
        if player.has_tag('hypnotist') or chelsea.hypno_re_dominate == 1:
          "She'll never be completely comfortable with you dominating her, but she'll be less opposed to the idea going forward, so it will impact her relationship with you less if you insist on this."
          $ chelsea.hypno_re_dominate = 2
        else:
          "It will take another session before you're able to make progress on lowering her objection to this idea."
          $ chelsea.hypno_re_dominate = 1
        "When you've done as much as you can for today, you let her rest. The suggestions you've made will take time to fully affect her thinking."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_21
    return

label chelsea_anal_hypnosis:
    if chelsea.has_tag('girlfriend'):
        if chelsea.has_tag('little_girl'):
            wt_image chubby_hypno_gf_youth_4
        elif chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_3
        else:
            wt_image chubby_hypno_gf_toned_4
        "You work on increasing [chelsea.name]'s comfort level with anal play."
        if player.has_tag('hypnotist') or chelsea.hypno_re_anal == 1:
          "She'll never be completely comfortable with anal sex, but she'll be less opposed to the idea going forward, so it will impact her relationship with you less if you insist on this."
          $ chelsea.hypno_re_anal = 2
        else:
          "It will take another session before you're able to make progress on lowering her objection to this idea."
          $ chelsea.hypno_re_anal = 1
        "When you've done as much as you can for today, you let her rest. The suggestions you've made will take time to fully affect her thinking."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_22
    return

label chelsea_lesbian_hypnosis:
    if chelsea.has_tag('girlfriend'):
        "You work on increasing [chelsea.name]'s comfort level with having sex with women."
        if player.has_tag('hypnotist') or chelsea.hypno_re_lesbian == 1:
            if chelsea.has_tag('little_girl'):
                wt_image chubby_hypno_gf_youth_5
            elif chelsea.has_tag('bbw'):
                wt_image chubby_hypno_gf_bbw_5
            else:
                wt_image chubby_hypno_gf_toned_5
            "She'll be more open to the idea going forward, although you may still need to do some non-hypnosis work before she'll sleep with women."
            $ chelsea.lesbian_status += 1
            $ chelsea.hypno_re_lesbian = 2
        else:
            if chelsea.has_tag('little_girl'):
                wt_image chubby_hypno_gf_youth_4
            elif chelsea.has_tag('bbw'):
                wt_image chubby_hypno_gf_bbw_3
            else:
                wt_image chubby_hypno_gf_toned_4
            "It will take another session before you're able to make progress on lowering her objection to this idea."
            $ chelsea.hypno_re_lesbian = 1
        "When you've done as much as you can for today, you let her rest.  The suggestions you've made will take time to fully affect her thinking."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_23
    return

label chelsea_implant_trigger:
    # note test is against unmodified stat
    if player.has_tag('hypnotist'):
        if chelsea.resistance < chelsea.hypno_trigger_resistance_threshold:
            add tags 'trigger_implanted' to chelsea
            "[chelsea.name]'s mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
            $ title = "What trigger phrase do you want to use?"
            menu menu_chelsea_implant_trigger:
                "[chelsea.trigger_phrase]":
                    pass
                "Choose something else":
                    $ chelsea.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
                    jump menu_chelsea_implant_trigger
            player.c "[chelsea.name], I have something important to tell you."
            player.c "When you hear the phrase, \"[chelsea.trigger_phrase]\", you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
            chelsea.c "Yes. When I hear, \"[chelsea.trigger_phrase]\", I will fall into a trance and do everything I am told."
            player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it. You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
            chelsea.c "Yes. I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
            sys "There are limited opportunities to use [chelsea.name]'s trigger. You'll be informed if one arises."
        else:
            "You've been working on implanting a hypnotic trigger in [chelsea.name]'s mind, but she's still too resistant to you. You need to lower her resistance to you before you can implant the trigger."
    return

label chelsea_hypno_trigger:
  player.c "Listen to me, [chelsea.name]. I have something important to tell you. [chelsea.trigger_phrase]. Are you listening to me?"
  chelsea.c "Yes"
  player.c "You are my girlfriend [chelsea.name]. You are my girlfriend and you are happy. Do you understand?"
  chelsea.c "I ..."
  player.c "[chelsea.trigger_phrase]. You are my girlfriend, [chelsea.name], and you are happy."
  chelsea.c "Yes. I am your girlfriend. I am very happy to be your girlfriend!"
  player.c "You can move into my bedroom now."
  chelsea.c "Okay!"
  add tags 'trigger_invoked' to chelsea
  call chelsea_convert_hypno_girlfriend from _call_chelsea_convert_hypno_girlfriend
  return

label chelsea_hypnosis_end:
    $ chelsea.hypno_session() # this deducts energy and records she was hypno'd
    if chelsea.has_tag('girlfriend'):
        call character_location_return(chelsea) from _call_character_location_return_23
    elif chelsea.has_tag('continuing_actions') and current_location == living_room:
        if chelsea.has_tag('hypno_sex_now'):
            rem tags 'hypno_sex_now' from chelsea
            "[chelsea.name]'s tits sliding up and down your cock during her hypnosis have built up a pressure in your balls you can no longer ignore."
            $ title = "How do you want to cum?"
            menu:
                "Have her suck you":
                    wt_image chubby_hypno_weekend_3
                    player.c "Suck me off now, [chelsea.name]."
                    wt_image chubby_hypno_weekend_7
                    "She removes her breasts from around your cock and replaces them with her mouth. Taking hold of her hair, you guide her head up and down ..."
                    wt_image chubby_exercise_motivated_8
                    "... until you relieve the pressure on your balls by filling her waiting mouth."
                    $ chelsea.hypno_blowjob_count += 1
                    $ chelsea.hypno_swallow_count += 1
                "Take over fucking her tits":
                    wt_image chubby_hypno_weekend_3
                    player.c "Put your hands down, [chelsea.name].  I'm going to fuck your tits properly."
                    wt_image chubby_hypno_weekend_6
                    "As she lowers her hands, you squeeze her boobs tightly against your cock and start fucking the valley between them..."
                    wt_image chubby_cum_tits_3
                    "... a process that soon leaves her breasts covered in your jizz."
                    $ chelsea.hypno_titfuck_count += 1
                "Just like this":
                    wt_image chubby_hypno_weekend_3
                    player.c "Finish me off with your tits, [chelsea.name]."
                    wt_image chubby_hypno_weekend_5
                    "The hypnotized woman slides her soft boobs faster and faster up and down your shaft ..."
                    wt_image chubby_cum_tits_2
                    "... until you empty your balls on her chest as she looks on, happy to have complied with your instructions."
                    $ chelsea.hypno_titfuck_count += 1
            player.c "[player.orgasm_text]"
            "You have her clean up and dress."
            orgasm
        wt_image chubby_hypno_weekend_1
        $ title = "What do you want [chelsea.name] to think the two of you did together?"
        menu:
            "Had sex":
                chelsea.c "Wow!  That was fun.  I can't even remember exactly what we did, but the next time you feel like doing that again, let me know!"
                $ chelsea.visit_sex_count += 1
            "Just talked":
                chelsea.c "You came all the way down here just to talk?  You surprise me sometimes."
                "She may be disappointed that you didn't fuck her, but she seems pleased to think that you were interested in getting to know her better."
                $ chelsea.visit_talk_count += 1
        call chelsea_continuing_actions_end_of_visit from _call_chelsea_continuing_actions_end_of_visit
        call character_location_return(chelsea) from _call_character_location_return_24
        notify
    elif chelsea.has_tag('continuing_actions') and chelsea.visit_outfit == 4:
        if chelsea.has_tag('hypno_sex_now'):
            wt_image chubby_visit_bbw_4_28
            "With the business of influencing her out of the way with, you can now relax and release the pressure the hypnotized woman's mouth has built up in your balls."
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image chubby_visit_bbw_4_43
                    $ chelsea.hypno_swallow_count += 1
                "On her":
                    wt_image chubby_visit_bbw_4_44
                    $ chelsea.hypno_facial_count += 1
            player.c "[player.orgasm_text]"
            "When your balls have finished pumping, you have her clean up and dress."
            rem tags 'hypno_sex_now' from chelsea
            $ chelsea.hypno_blowjob_count += 1
            orgasm
        wt_image chubby_visit_bbw_4_2
        $ title = "What do you want [chelsea.name] to think the two of you did together?"
        menu:
            "Had sex":
                wt_image chubby_visit_bbw_4_26
                chelsea.c "Thanks for the fun work break!  I need to get back to my desk, now."
                $ chelsea.visit_sex_count += 1
            "Just talked":
                wt_image chubby_visit_bbw_4_26
                chelsea.c "You came all the way down here just to talk?  You surprise me sometimes."
                $ chelsea.visit_talk_count += 1
        "You leave her and get on with your day."
        call forced_movement(living_room) from _call_forced_movement_178
        call chelsea_continuing_actions_end_of_visit from _call_chelsea_continuing_actions_end_of_visit_1
        call character_location_return(chelsea) from _call_character_location_return_25
        notify
    else:
        call character_location_return(chelsea) from _call_character_location_return_26
        end_day
    return

# End Session
label chelsea_end_session:
  if chelsea.status == "on_training":
    $ chelsea.training_session()
    "You're unable to find an activity that both you and [chelsea.name] are willing to proceed with, so you end today's session here."
    $ player.extra_clients_fee_this_week -= chelsea.pay # so you don't get paid for training her this week
    add tags 'failed_regular_training_this_week' to chelsea
    call character_location_return(chelsea) from _call_character_location_return_27
    end_day
  elif chelsea.has_tag('continuing_actions'):
    $ chelsea.training_session()
    "You've spent enough time with [chelsea.name] for today. You send her home."
    call character_location_return(chelsea) from _call_character_location_return_28
    wt_image current_location.image
  else:
    add tags 'shut_off_end_session' to chelsea
  return

# Weekend Actions
label chelsea_pre_weekend:
    # summon chelsea ## some labels may not want her summoned right at the beginning
    add tags 'checking_for_weekend' to chelsea
    return

label chelsea_post_weekend:
    # call character_location_return(chelsea) ## safest only to send her ack after a successful summon, otherwise may conflict with other coding
    if chelsea.has_tag('checking_for_weekend'):
        rem tags 'checking_for_weekend' from chelsea
    else:
        if chelsea.has_tag('failed_regular_training_this_week'):
            rem tags 'failed_regular_training_this_week' from chelsea
            $ player.extra_clients_fee_this_week += chelsea.pay
    return

label chelsea_weekend:
    if player.energy >= energy_long.value:
        if not player.has_tag('chelsea_weekend_message_today'):
            add tags 'chelsea_weekend_message_today' to player
            "If you want to keep [chelsea.name] focused on sticking with making changes to her lifestyle, you can create a mini boot camp for her this weekend. If you prefer to help her work on feeling good about herself, some sex therapy may help."
            if player.can_hypno(chelsea):
                extend " Or you could always hypnotize her and work on her that way."
        call expandable_menu(chelsea_weekend_training_menu) from _call_expandable_menu_22
    else:
        sys "You don't have enough energy for this action, choose something else."
    return

## note: instead of expandable menu calling _training_ labels which in turn call a second label, could have been done in one step but this format was added later and built on existing content instead of re-coding it
label chelsea_weekend_training_hypnotize:
    summon chelsea
    rem tags 'checking_for_weekend' from chelsea
    call chelsea_weekend_hypno_therapy from _call_chelsea_weekend_hypno_therapy
    return

label chelsea_weekend_training_boot_camp:
    summon chelsea
    call chelsea_weekend_boot_camp from _call_chelsea_weekend_boot_camp
    return

label chelsea_weekend_training_sex_therapy:
    call chelsea_weekend_sex_therapy from _call_chelsea_weekend_sex_therapy
    return

label chelsea_weekend_training_shock_therapy:
    summon chelsea
    call chelsea_weekend_shock_therapy from _call_chelsea_weekend_shock_therapy
    return

label chelsea_weekend_hypno_therapy:
    # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
    $ queue_action(chelsea.hypno_action)
    return

label chelsea_weekend_boot_camp:
  summon chelsea
  $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  rem tags 'checking_for_weekend' from chelsea
  $ chelsea.temporary_count = 0
  wt_image chubby_boot_camp_1
  "Your plan for [chelsea.name] for the weekend is comprised of two parts. Part one is an exercise regime. She comes dressed prepared."
  # check to see if she strips
  if chelsea.weekend_boot_camp_status > 0 or chelsea.sex_status > 0 or chelsea.test('resistance', 60):
    if chelsea.weekend_boot_camp_status == 0:
      $ chelsea.weekend_boot_camp_status = 1
      $ chelsea.temporary_count += 5
      change chelsea resistance by -5
    wt_image chubby_boot_camp_2
    "You don't, however, see any need for her to wear her outfit, since she'll be working out indoors today."
    # if has given BJ or TJ previously, she takes you in her mouth
    if chelsea.sex_status > 0:
      if chelsea.weekend_boot_camp_status == 1:
        $ chelsea.weekend_boot_camp_status = 2
        $ chelsea.temporary_count += 5
        change chelsea resistance by -5
      wt_image chubby_boot_camp_16
      "When she's finished her work out, you have her lie down and relax."
      wt_image chubby_boot_camp_3
      "She's a bit tired and a bit sweaty, but you can still put her to good use while she's here."
      wt_image chubby_boot_camp_12
      "When she gets too lethargic, a quick pinch of her nipple improves her alertness."
      # next check to see if she'll have sex with you
      if chelsea.sex_status == 2 or chelsea.test('resistance',25):
        if chelsea.weekend_boot_camp_status == 2:
          $ chelsea.weekend_boot_camp_status = 3
          $ chelsea.temporary_count += 5
          change chelsea resistance by -5
        wt_image chubby_boot_camp_4
        "Once she's rested enough, it's time for the remainder of her work out."
        wt_image chubby_boot_camp_14
        "Sex is one of the better ways to burn calories ..."
        wt_image chubby_boot_camp_5
        "... so you put her to work pleasing you ..."
        wt_image chubby_boot_camp_13
        "... in as many different positions as she can."
        if chelsea.sex_status == 1:
          $ chelsea.sex_status = 2
          "Your continued sexual interest in [chelsea.name] confirms in her mind that she's on the right track with the exercises."
          $ chelsea.temporary_count += 5
        if chelsea.sex_count == 0:
          "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
          change chelsea resistance by -10
        $ chelsea.sex_count += 1
      else:
        if chelsea.blowjob_count == 0:
          "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
          change chelsea resistance by -10
        $ chelsea.blowjob_count += 1
      wt_image chubby_boot_camp_6
      player.c "[player.orgasm_text]"
      orgasm
    else:
      wt_image chubby_boot_camp_16
      "It's a good workout for her, and a fun one for you as you watch her."
  else:
    wt_image chubby_boot_camp_15
    "It's a good workout for her, and a fun one for you as you watch her."
  wt_image chubby_boot_camp_7
  # check again if she'll strip for part two
  if chelsea.weekend_boot_camp_status > 0:
    "Part two of your weekend plans is working on her diet in the kitchen. She changes into something nice ..."
    wt_image chubby_boot_camp_8
    "... not realizing that you have no intentions of leaving her clothed for this part of the program, either."
    wt_image chubby_boot_camp_9
    "You do let her wear an apron near the stove."
    # check to see if she will blow you
    if chelsea.sex_status > 0 or chelsea.test('sos', 20) or chelsea.test('resistance', 40):
      wt_image chubby_boot_camp_10
      "She has to take it off, however, while the food is cooking, and attend to more important matters until it's time to finish the meal."
      player.c "[player.orgasm_text]"
      if chelsea.sex_status == 0:
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the changes in her body."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
      if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
      $ chelsea.blowjob_count += 1
      $ chelsea.swallow_count += 1
      orgasm
  else:
    "Part two of your weekend plans is working on her diet in the kitchen. She changes into something nice."
    change chelsea resistance by -5
  wt_image chubby_boot_camp_11
  "By the time the food is ready, [chelsea.name] is exhausted and ready to dig in. The time you spent with [chelsea.name] this weekend helps motivate her to stick to a healthy exercise and diet regime."
  $ chelsea.temporary_count += 5
  change chelsea desire_c by chelsea.temporary_count notify
  call character_location_return(chelsea) from _call_character_location_return_29
  end_day  #note: this will also end_week since day == 5
  return

label chelsea_weekend_sex_therapy:
  if chelsea.has_tag('motivated'):
    "[chelsea.name] is trying hard to stick to a smart diet and workout routine. Don't let up on her now. You might even be able to work sex into her weekend boot camp, when she's ready."
  else:
    summon chelsea
    rem tags 'checking_for_weekend' from chelsea
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    wt_image chubby_sex_therapy_1
    "[chelsea.name] looks nervous as she takes a seat on your sofa."
    if chelsea.sex_status > 0 or chelsea.test('sos', 20) or chelsea.test('resistance', 40):
      wt_image chubby_sex_therapy_3
      "Despite her nervousness, she lets you pull her close and kiss her."
      wt_image chubby_sex_therapy_11
      "After the two of you make out for a while ..."
      wt_image chubby_sex_therapy_2
      "... you convince her to pull down her top ..."
      wt_image chubby_sex_therapy_4
      "... and lay her back on the sofa."
      # titjob first
      if chelsea.sex_status == 0:
        wt_image chubby_sex_therapy_13
        "As you straddle her chest, [chelsea.name] wraps her soft mounds around your dick."
        wt_image chubby_sex_therapy_14
        "You're not the first to show an interest in her chest.  Every boyfriend she's had has likely wanted to use her breasts this way from time-to-time."
        wt_image chubby_sex_therapy_15
        "It's an activity she's comfortable with and a part of her body she's confident in.  It's therefore a good place to start in order to remind her that she's a sexy and desirable woman, just the way she is ..."
        wt_image chubby_sex_therapy_16
        "... a point you punctuate by covering her with your spunk."
        wt_image chubby_cum_tits_7
        player.c "[player.orgasm_text]"
        wt_image chubby_cum_tits_8
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        change chelsea sos by 10
        if chelsea.titfuck_count == 0:
          "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
          change chelsea resistance by -10
        $ chelsea.titfuck_count += 1
      elif chelsea.sex_status == 1:
        # if already given BJ and resistance low enough, then first sex, no orgasm
        if chelsea.blowjob_count > 0 and chelsea.test('resistance',25):
          wt_image chubby_sex_therapy_22
          "[chelsea.name] lets you pull off her panties ..."
          wt_image chubby_sex_therapy_6
          "... then she rolls over onto her knees so you can enter her from behind."
          wt_image chubby_sex_therapy_23
          "Her body responds to you, getting wetter and wetter as you fuck her, but she's not relaxed enough to cum today."
          wt_image chubby_sex_therapy_24
          "You have no such problem."
          player.c "[player.orgasm_text]"
          wt_image chubby_sex_therapy_25
          "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
          $ chelsea.sex_status = 2
          change chelsea sos by 10
          if chelsea.sex_count == 0:
            "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
            change chelsea resistance by -10
          $ chelsea.sex_count += 1
        # else blowjob
        else:
          wt_image chubby_sex_therapy_17
          "As you lean over to massage her chest, [chelsea.name] grabs your cock and opens her mouth."
          # first BJ
          if chelsea.blowjob_count == 0:
            wt_image chubby_sex_therapy_18
            "That's as clear an indication as you're likely to get that she's ready to take you in her mouth, so you put her on her knees and have her blow you ..."
            wt_image chubby_sex_therapy_9
            "... until you fill her mouth with cum."
            player.c "[player.orgasm_text]"
            wt_image chubby_sex_therapy_21
            $ chelsea.swallow_count += 1
          # subsequent BJs
          else:
            wt_image chubby_sex_therapy_5
            "Curious to see how far she'll go, you wait and are rewarded with the sensation of her taking your balls into her mouth."
            wt_image chubby_sex_therapy_19
            "You let her suckle your balls until they feel like they will burst ..."
            wt_image chubby_sex_therapy_9
            "... then put her on her knees ..."
            wt_image chubby_sex_therapy_10
            "... and cover her face in jizz."
            player.c "[player.orgasm_text]"
            wt_image chubby_sex_therapy_20
            $ chelsea.facial_count += 1
          if chelsea.blowjob_count == 0:
            "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
            change chelsea resistance by -10
          $ chelsea.blowjob_count += 1
          "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
          change chelsea sos by 5
      # if sex previously, then sex again, with orgasm
      else:
        wt_image chubby_sex_therapy_22
        "You pull off [chelsea.name]'s panties ..."
        wt_image chubby_sex_therapy_26
        "... then spread her legs and push into her."
        wt_image chubby_sex_therapy_27
        "She moans as your cock strokes in and out of her.  She's enjoying this, but you're not sure she's enjoying it enough."
        wt_image chubby_sex_therapy_7
        player.c "I want you to cum, [chelsea.name].  What position's best for you?"
        wt_image chubby_sex_therapy_28
        "She scrambles up on top, then to your surprise, she faces away from you.  Perhaps her lingering body issues make it easier for her to focus on her own pleasure if she can't scrutinize your face for signs of displeasure?"
        wt_image chubby_sex_therapy_29
        "Regardless, she definitely enjoys this position and soon rides herself to climax, bringing you with her."
        wt_image chubby_sex_therapy_8
        chelsea.c "Aahhhhhh"
        wt_image chubby_sex_therapy_30
        player.c "[player.orgasm_text]"
        wt_image chubby_sex_therapy_25
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        change chelsea sos by 5
        if chelsea.sex_count == 0:
          "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
          change chelsea resistance by -10
        if chelsea.orgasm_count == 0:
          "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
          change chelsea resistance by -10
        $ chelsea.sex_count += 1
        $ chelsea.orgasm_count += 1
      orgasm notify
    else:
      if chelsea.test('sos', 15):
        wt_image chubby_sex_therapy_11
        "Despite your best efforts, you aren't able to get [chelsea.name] to go further than a short make-out session ..."
        wt_image chubby_sex_therapy_3
        "... during which she lets you fondle her giant boobs."
      elif chelsea.test('sos', 10):
        wt_image chubby_sex_therapy_11
        "Despite your best efforts, you aren't able to get [chelsea.name] to go further than a short make-out session."
      else:
        "Despite your best efforts, you aren't able to convince [chelsea.name] to fool around with you."
      wt_image chubby_sex_therapy_12
      if chelsea.seduce_action_status == 0:
        "Although you didn't get far, you did convince [chelsea.name] of the sincerity of your attraction to her.  If you could lower her resistance more or improve her comfort with the current state of her body, you might get a chance to show her how strong that attraction is."
        change chelsea sos by 10
        $ chelsea.seduce_action_status = 1
      elif chelsea.seduce_action_status == 1:
        "Although you didn't get far, you did convince [chelsea.name] of the sincerity of your attraction to her.  If you could lower her resistance more or improve her comfort with the current state of her body, you might get a chance to show her how strong that attraction is."
        change chelsea sos by 5
        $ chelsea.seduce_action_status = 2
      else:
        "[chelsea.name]'s still too unhappy with herself and too resistant to your instructions for you to get any farther with her. The time you spent with her this weekend, however, helps to break down her resistance."
      change chelsea resistance by -5 notify
    call character_location_return(chelsea) from _call_character_location_return_30
    end_day #note: this will also end_week since day == 5
  return

label chelsea_weekend_shock_therapy:
  rem tags 'checking_for_weekend' from chelsea
  $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  $ chelsea.shock_count += 1
  if chelsea.shock_count == 1:
    "You let [chelsea.name]'s husband know beforehand what you have planned for [chelsea.name] for this weekend. He agrees she needs to be shaken out of her current pattern of yo-yo dieting, and consents to your plan."
    call forced_movement(outdoors) from _call_forced_movement_118
    summon chelsea
    wt_image chubby_jail_1
    "You take [chelsea.name] on a drive out of town, and bring her to a rural police station, where you turn her over for 'obedience training'."
    wt_image chubby_jail_2
    "He starts by patting her down and informs her she'll be strip searched, like all new jail birds."
    wt_image chubby_jail_3
    "This isn't a real police station, it's a studio set.  And this isn't a real police officer, it's an actor.  But [chelsea.name] doesn't know that."
    wt_image chubby_jail_4
    "One thing that is real is the strip search examination."
    wt_image chubby_jail_6
    "He's very thorough, to [chelsea.name]'s dismay."
    wt_image chubby_jail_10
    "At this point, he's supposed to put [chelsea.name] in the jail cell, naked, and leave her there until you come to get her."
    wt_image chubby_jail_7
    "His payment was supposed to be getting to feel her up.  You didn't tell him he could demand a blow job from her while she's there, but then you didn't tell him not to, either."
    wt_image chubby_jail_8
    "Apparently [chelsea.name]'s in no mood to say 'no' to him, either.  She doesn't mention this part of her ordeal when you come by later that night to ask if she's ready to do what it takes to never end up back here."
    wt_image chubby_jail_9
    "It's only when you review the security tapes you put in place to protect her that you discover the liberties he took.  Her husband had told her that sex could be part of her training, and since she seems none the worse for wear, mentally and physically, you let it lie."
  elif chelsea.shock_count == 2:
    summon chelsea
    wt_image chubby_shock_4
    "[chelsea.name]'s understandably nervous when you tell her to get in the car."
    chelsea.c "Please don't take me back to that jail."
    player.c "I'm not.  But your husband and I agree that you need to be shaken out of the rut you're in, and he's agreed that what I've arranged is for your own good."
    call forced_movement(outdoors) from _call_forced_movement_119
    summon chelsea
    wt_image chubby_shock_5
    "You drive [chelsea.name] to a private bar fuction outside of town. The participants have been carefully chosen, as you don't want a repeat of the overstepping of boundaries from the previous episode."
    wt_image chubby_shock_6
    "[chelsea.name], of course, has no idea what to expect. You told them to be rough on her, and they are."
    wt_image chubby_shock_1
    "Her breasts are exposed ..."
    wt_image chubby_shock_7
    "... and roughly abused."
    wt_image chubby_shock_8
    "Then she's stripped naked ..."
    wt_image chubby_shock_9
    "... with her arms pulled back and tied behind her back ..."
    wt_image chubby_shock_10
    "... and her breasts trussed up."
    wt_image chubby_shock_2
    "After everyone in the crowd has had their fun groping her exposed body, they leave her tied there, her breasts red and sore from the rough fondling."
    wt_image chubby_shock_3
    "You can't resist giving her tender breasts a hard smack when you come to get her ... *SMACK*"
    chelsea.c "OWWWW!!"
    player.c "I'm sorry we had to put you through this, [chelsea.name], but your husband and I are serious about shaking you out of your cycle of self-loathing.  Are you serious, too, about following my instructions without question, so that I can help you?"
    chelsea.c "Yes, anything!  You've made your point, I'm ready to change, and you're in charge."
  change chelsea resistance by -10 notify
  call forced_movement(living_room) from _call_forced_movement_120
  call character_location_return(chelsea) from _call_character_location_return_31
  end_day  #note: this will also end_week since day == 5
  return

## Character Specific Actions
# Glory Hole Actions
label chelsea_glory:
  $ chelsea.temporary_count = 1
  if chelsea.glory_hole_count >= 4:
    "[chelsea.name] has gotten as much out of the visits to the glory hole as she can."
    $ title = "Do you still want to take her?"
    menu:
      "Yes":
        pass
      "No, do something else":
        $ chelsea.temporary_count = 0
  if chelsea.temporary_count == 1:
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ chelsea.temporary_count = 0
    $ chelsea.glory_hole_count += 1
    if chelsea.glory_hole_count == 1:
      wt_image chelsea.image
      "You hand [chelsea.name] some old clothes. They won't fit her very well, but that's not going to matter."
      player.c "Change into these and meet me at the car.  I don't want you to get your good clothes dirty."
      chelsea.c "Where are we going?"
      player.c "Somewhere no one will see you."
      call forced_movement(outdoors) from _call_forced_movement_85
      summon chelsea
      wt_image chubby_glory_12
      "When you arrive at the park washroom, she looks at you in disbelief."
      if chelsea.test('resistance',60):
        wt_image chubby_glory_13
        chelsea.c "You want me to go in here?  Dressed like this?"
        wt_image chubby_glory_1
        player.c "Nobody can see you here except me.  Go on in."
        wt_image chubby_glory_11
        chelsea.c "I'm not really comfortable with this.  What if someone comes in?  Can't we do whatever this is at your house?"
        player.c "No one is coming in.  I'm going to watch the door.  And I'm not the one you're going to be looking after. You're going to take care of whatever cocks come through those holes, and when they're satisfied, then I'll take you home."
        wt_image chubby_glory_14
        chelsea.c "Okay, now I know you're joking.  'Filth hole'?  Seriously."
        wt_image chubby_glory_15
        player.c "Just have a seat and wait."
        wt_image chubby_glory_16
        "She doesn't have to wait long.  [chelsea.name] gasps when the first cock comes through the hole."
        chelsea.c "You were you serious??  How is this supposed to help me?"
        wt_image chubby_glory_17
        player.c "By reminding you of your place in this relationship. You agreed to follow my instructions. This is a test, to show me you meant what you said. Plus, you're going to learn something this evening. Enough back talk, start sucking."
        wt_image chubby_glory_18
        "She surprises herself by doing exactly that.  She's presumably not surprised to find that soon earns her a mouthful of cum."
        wt_image chubby_glory_19
        player.c "There'll be another man along soon, I expect, if you'd like to wait?"
        chelsea.c "No!  Let's go!!"
        wt_image chubby_glory_11
        chelsea.c "What was I supposed to learn from that?"
        player.c "That you're a sexual woman, plus something else I hope you figure out on your own."
        wt_image chubby_glory_12
        chelsea.c "That I'm willing to follow your instructions, I guess."
        "That wasn't what you were thinking of, but she's right, her resistance to you is falling."
        change chelsea resistance by -10
        change player energy by -energy_long notify
      else:
        chelsea.c "You want me to go in here?  Dressed like this?  No way.  Whatever disgusting thing you have planned, I want nothing to do with it"
        "She takes off, unwilling to do anything more with you today. You need to lower her Resistance to your instructions before you can get her to proceed on this path."
        $ chelsea.glory_hole_count = 0
        change player energy by -energy_very_short notify
    elif chelsea.glory_hole_count == 2:
      wt_image chelsea.image
      player.c "Put these old clothes on.  We're going back to the glory hole."
      call forced_movement(outdoors) from _call_forced_movement_86
      summon chelsea
      wt_image chubby_glory_1
      chelsea.c "You really want me to do this again?  There's nothing more I can learn here."
      wt_image chubby_glory_11
      player.c "Clearly there is.  I don't think you figured out the last lesson, yet."
      wt_image chubby_glory_15
      chelsea.c "That I'll listen to you?  Yes, I did."
      wt_image chubby_glory_20
      player.c "That wasn't it.  But since you mention it, take your top and bra off.  I'll enjoy this more if I can look at you."
      wt_image chubby_glory_2
      "[chelsea.name] is just finishing exposing herself when a cock appears in the glory hole."
      wt_image chubby_glory_3
      player.c "Get it nice and hard for him."
      wt_image chubby_glory_21
      "Tentatively at first, [chelsea.name] takes him in her hand. She watches you, wondering where this is going, when a second cock appears through the other hole."
      wt_image chubby_glory_5
      player.c "You're taking too long.  You've got a backlog forming."
      wt_image chubby_glory_4
      player.c "Gentle licks aren't going to get the job done.  You're here to get these men off so they can go on with their day.  Get to it."
      wt_image chubby_glory_7
      "[chelsea.name] stops dividing her attention and focuses on getting the first man off ..."
      wt_image chubby_glory_6
      "... then she looks after the other."
      wt_image chubby_glory_2
      chelsea.c "Let's get out of here before anyone else shows up."
      player.c "Why?  You seem to be popular.  Those men were certainly happy with you."
      wt_image chubby_glory_20
      chelsea.c "I don't want to sit here and give blow jobs the rest of the day."
      player.c "I suppose you might attract a long line up.  That's probably because they find you so sexy to look at."
      wt_image chubby_glory_11
      chelsea.c "What do you mean?  They couldn't even see me."
      player.c "Want to take another shot at figuring out what you were supposed to learn here?"
      wt_image chubby_glory_12
      chelsea.c "I can give good blowjobs no matter how much I weigh?"
      player.c "You're getting closer."
      change chelsea resistance by -10
      change chelsea sos by 10
      change player energy by -energy_long notify
    elif chelsea.glory_hole_count == 3:
      call forced_movement(outdoors) from _call_forced_movement_121
      summon chelsea
      wt_image chubby_glory_1
      chelsea.c "Are we going to keep doing this?"
      wt_image chubby_glory_2
      player.c "Yes, for as many more times as it takes for you to learn the lesson."
      wt_image chubby_glory_4
      "[chelsea.name] shows no hesitation getting to work on the cocks that soon appear."
      player.c "No, not like that. Not this time."
      wt_image chubby_glory_5
      chelsea.c "What do you mean?"
      player.c "I mean this time you're going to use your cunt to please these men."
      wt_image chubby_glory_22
      "For a moment you wonder if [chelsea.name] is going to balk."
      wt_image chubby_glory_8
      "Then she fingers herself wet ..."
      wt_image chubby_glory_9
      "... slides the condoms you brought over the waiting cocks ..."
      wt_image chubby_glory_10
      "... and fucks them until she's brought all the men on the other side of the wall to orgasm."
      wt_image chubby_glory_15
      chelsea.c "I've figured it out.  What I do with my body is more important to men than how much it weighs.  At least some men.  That's what you were trying to teach me.  I can be a good sex partner, no matter how much I weigh."
      wt_image chubby_glory_23
      "Whether that was your intended message or not, [chelsea.name]'s become more comfortable with the idea that she can be a good sex partner, regardless of her size"
      change chelsea resistance by -10
      change chelsea sos by 10
      change player energy by -energy_long notify
    elif chelsea.glory_hole_count >= 4:
      call forced_movement(outdoors) from _call_forced_movement_87
      summon chelsea
      wt_image chubby_glory_1
      chelsea.c "Here again?"
      wt_image chubby_glory_2
      chelsea.c "Do you think there'll be many men this time?"
      wt_image chubby_glory_6
      "There are, but [chelsea.name] doesn't let things get backed up.  She quickly blows the first cock that appears ..."
      wt_image chubby_glory_10
      "... then without prompting fucks the second cock to climax."
      wt_image chubby_glory_24
      "She has a few more men show up today, but she gets them in and out of there quickly, using whichever body part they respond to best to get them off."
      if chelsea.glory_hole_count == 4:
        "[chelsea.name]'s feeling good about her ability to please men, regardless of what her body looks like. She's learned as much from this activity as she can."
        change chelsea sos by 5
      else:
        "[chelsea.name] may not be learning anything more from this activity, but she's certainly won some admirers on the other side of the wall, even if they wouldn't recognize her from Eve."
      change player energy by -energy_long notify
    call forced_movement(living_room) from _call_forced_movement_88
    summon chelsea
    end_day
  return

# Discipline Actions
label chelsea_discipline:
  $ chelsea.discipline_count += 1
  if chelsea.discipline_count == 1:
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    call forced_movement(backyard) from _call_forced_movement_122
    summon chelsea no_follows
    wt_image chubby_discipline_1_1
    "You have [chelsea.name] remove her outer clothes and follow you into the backyard. She giggles as you wind the rope around her"
    wt_image chubby_discipline_1_2
    "The giggles stop as you bind her to the post."
    wt_image chubby_discipline_1_3
    chelsea.c "What happens now?  Are you just going to leave me like this?"
    player.c "Not exactly like this, no."
    wt_image chubby_discipline_1_4
    "You finish the tie with a rope across her mouth, effectively silencing her."
    call forced_movement(living_room) from _call_forced_movement_124
    "Then you leave her alone with her thoughts."
    call forced_movement(backyard) from _call_forced_movement_125
    wt_image chubby_discipline_1_4
    "You check on her periodically over the next few hours. When you think she's ready, you address her."
    wt_image chubby_discipline_1_5
    player.c "[chelsea.name], I'm in charge of your training.  If I'm not satisfied with your progress, you'll find yourself out here again.  Is that understood?"
    "She nods emphatically.  The lesson has made it's point.  You untie her and send her home, confident that she'll be more pliable on her next visit"
    change chelsea resistance by -10
    change player energy by -energy_long notify
    call forced_movement(living_room) from _call_forced_movement_126
    end_day
  elif chelsea.discipline_count == 2:
    if dungeon.has_item(floggers):
      call chelsea_discipline_spank_first from _call_chelsea_discipline_spank_first
    else:
      "If you had a proper flogger, you could further [chelsea.name]'s discipline with some corporal punishment. Until then, you'll let the ropes do their trick."
      call chelsea_discipline_spank_second_tie from _call_chelsea_discipline_spank_second_tie
  elif chelsea.discipline_count >= 3:
    $ title = "How do you want to discipline her?"
    menu menu_chelsea_discipline_count_3:
      "Flog her":
        if dungeon.has_item(floggers):
          if chelsea.spanked > 0:
            call chelsea_discipline_spank_second_spank from _call_chelsea_discipline_spank_second_spank
          else:
            call chelsea_discipline_spank_first from _call_chelsea_discipline_spank_first_1
        else:
          "You need to buy a flogger first."
          jump menu_chelsea_discipline_count_3
      "Tie her up":
        call chelsea_discipline_spank_second_tie from _call_chelsea_discipline_spank_second_tie_1
      "Try something else":
        pass
  return

label chelsea_discipline_spank_first:
  $ chelsea.temporary_count = 1
  $ chelsea.spanked = 1
  wt_image chubby_discipline_2_1
  "You tie [chelsea.name] up indoors this time, and select one of your floggers from the dungeon. When she feels the leather against her skin, she starts to panic."
  chelsea.c "No, please!!  I'll listen to you.  I'll do as you say!  You don't have to do this.  I promised I'll follow your instructions.  I will!!"
  $ title = "What do you do?"
  menu:
    "Agree not to spank her":
      add tags 'no_spanking' to chelsea
      wt_image chelsea.image
      "You've made your point. [chelsea.name] scrambles to her feet and dresses as you untie her. You can still do something else today, if you want."
      chelsea.c "I promise I'll obey you. I will."
      change chelsea resistance by -5
      change player energy by -energy_very_short notify
      $ chelsea.temporary_count = 0
    "Agree not to spank her if she blows you" if chelsea.sex_status > 0 or chelsea.test('resistance', 60):
      add tags 'no_spanking' to chelsea
      player.c "Prove it. Get up here and blow me."
      wt_image chubby_discipline_2_3
      "To her credit, [chelsea.name] is as good as her word.  She immediately takes you into her mouth and eagerly bobs her head up and down on your hardening cock. To slow things down, you take control by grabbing her by the back of her hair."
      wt_image chubby_discipline_2_8
      $ title = "Where do you want to cum?"
      menu:
        "Hair":
          wt_image chubby_discipline_2_4
          "Still gripping her by the hair at the back of her head, you hold her head down and shoot your load on top of her. Despite your grip, she manages to look up at you, getting some of your cum on her face in the process."
          $ chelsea.facial_count += 1
        "Tits":
          wt_image chubby_discipline_2_5
          "[chelsea.name]'s tits are a difficult target to miss. She seems comfortable having your cum on them."
        "Face":
          wt_image chubby_discipline_2_6
          "As the first spurts of your cum hit her face, [chelsea.name] opens her mouth. You can't resist depositing the rest of your load on the back of her tongue."
          $ chelsea.facial_count += 1
        "Mouth":
          wt_image chubby_discipline_2_3
          "[chelsea.name] slurps down your cum as fast as your balls can pump it into her."
          $ chelsea.swallow_count += 1
      player.c "[player.orgasm_text]"
      if chelsea.sex_status == 0:
        $ chelsea.sex_status = 1
      if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -15
      else:
        change chelsea resistance by -5
      $ chelsea.blowjob_count += 1
      orgasm notify
    "Flog her":
      $ chelsea.spanked = 2
      wt_image chubby_discipline_2_2
      "[chelsea.name] has a low pain tolerance.  That's obvious from the first sting of the leather against her skin ... *slappp*"
      chelsea.c "Noooo!!"
      "*slappp*"
      chelsea.c "Ow!!  Please ... I'll be good."
      "*slappp*"
      chelsea.c "Owww!  I promise.  I'll do as you say."
      "*slappp*"
      chelsea.c "Owww!!!  I will!!!"
      "*slappp*"
      chelsea.c "OWWWW!!!!  PLEASE!!!!"
      wt_image chubby_discipline_2_1
      "You've made your point. No need to continue to torture her. Not today, anyway."
      add tags 'discipline_flogging' to chelsea
      change chelsea resistance by -5
      change player energy by -energy_short notify
  if chelsea.temporary_count == 1:
    $ chelsea.temporary_count = 0
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    end_day
  return

label chelsea_discipline_spank_second_spank:
  $ chelsea.temporary_count = 1
  wt_image chubby_discipline_2_1
  "Once again you tie [chelsea.name] up and run the flogger along her skin."
  chelsea.c "No!  Not again!!  Please, it's not necessary.  I'll listen to you!  I'll do as you say.  You don't have to do this.  I'll follow your instructions.  I will!"
  $ title = "What do you do?"
  menu:
    "Let her off without a spanking for today":
      "You've made your point. [chelsea.name] scrambles to her feet and dresses as you untie her. You can still do something else today, if you want."
      wt_image chelsea.image
      chelsea.c "I promise I'll obey you. I will. You don't have to keep spanking me."
      change chelsea resistance by -5
      change player energy by -energy_very_short notify
      $ chelsea.temporary_count = 0
    "Let her off with a blow job for today" if chelsea.sex_status > 0 or chelsea.test('resistance', 60):
      player.c "Prove it. Get up here and blow me."
      wt_image chubby_discipline_2_3
      "To her credit, [chelsea.name] is as good as her word. She immediately sucks you into her mouth and eagerly starts bobbing her head up and down on your hardening cock. To slow things down, you take control by grabbing her by the back of her hair."
      wt_image chubby_discipline_2_8
      $ title = "Where do you want to cum?"
      menu:
        "Hair":
          wt_image chubby_discipline_2_4
          "Still gripping her by the hair at the back of her head, you hold her head down and shoot your load on top of her. Despite your grip, she manages to look up at you, getting some of your cum on her face in the process."
          $ chelsea.facial_count += 1
        "Tits":
          wt_image chubby_discipline_2_5
          "[chelsea.name]'s tits are a difficult target to miss. She seems comfortable having your cum on them."
        "Face":
          wt_image chubby_discipline_2_6
          "As the first spurts of your cum hit her face, [chelsea.name] opens her mouth. You can't resist depositing the rest of your load on the back of her tongue."
          $ chelsea.facial_count += 1
        "Mouth":
          wt_image chubby_discipline_2_3
          "[chelsea.name] slurps down your cum as fast as your balls can pump it into her."
          $ chelsea.swallow_count += 1
      player.c "[player.orgasm_text]"
      if chelsea.sex_status == 0:
        $ chelsea.sex_status = 1
      if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -15
      else:
        change chelsea resistance by -5
      $ chelsea.blowjob_count += 1
      orgasm notify
    "Flog her":
      $ chelsea.spanked = 2
      wt_image chubby_discipline_2_2
      "[chelsea.name] has a low pain tolerance.  That's obvious from the first sting of the leather against her skin ... *slappp*"
      chelsea.c "Noooo!!"
      "*slappp*"
      chelsea.c "Ow!!  Please ... I'll be good."
      "*slappp*"
      chelsea.c "Owww!  I promise.  I'll do as you say."
      "*slappp*"
      chelsea.c "Owww!!!  I will!!!"
      "*slappp*"
      chelsea.c "OWWWW!!!!  PLEASE!!!!"
      wt_image chubby_discipline_2_1
      "You've made your point. No need to continue to torture her. Not today, anyway."
      if chelsea.has('discipline_flogging'):
        change chelsea resistance by -5
      else:
        add tags 'discipline_flogging' to chelsea
        change chelsea resistance by -10
      change player energy by -energy_long notify
  if chelsea.temporary_count == 1:
    $ chelsea.temporary_count = 0
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    end_day
  return

label chelsea_discipline_spank_second_tie:
  $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  call forced_movement(backyard) from _call_forced_movement_127
  wt_image chubby_discipline_1_2
  "Once again you bind [chelsea.name] firmly to the post and leave her there until the discomfort and helplessness has worked it's magic on her mood."
  wt_image chubby_discipline_1_4
  player.c "Ready to start listening to my instructions, [chelsea.name]?"
  wt_image chubby_discipline_1_5
  "She nods her head emphatically."
  change chelsea resistance by -5
  change player energy by -energy_short notify
  call forced_movement(living_room) from _call_forced_movement_128
  end_day
  return

# Seduce Actions
label chelsea_seduce:
    $ chelsea.temporary_count = 0
    if chelsea.has_tag('motivated'):
        wt_image chubby_motivated_1
        player.c "You know I want you, don't you, [chelsea.name]?"
        if chelsea.sex_status > 0 or chelsea.test('resistance',55):
            wt_image chubby_motivated_2
            chelsea.c "Really?  Feeling frisky are you?  I'm supposed to follow your instructions, so if you're intent on seducing me, I guess I have to go along."
            wt_image chubby_visit_toned_3_2
            "[chelsea.name] pulls off her little dress and sits on the sofa, waiting for you. She seems proud of her now slimmer body."
            wt_image chubby_visit_toned_3_3
            chelsea.c "So what were you planning on doing with me today?"
            if chelsea.sex_status == 0:
                "This is your first time having sex with [chelsea.name], so you decide to stick with something you're certain - based on her assets - she's used to men wanting from her."
                call chelsea_seduce_tf_motivated from _call_chelsea_seduce_tf_motivated
            else:
                $ title = "What do you want to do with her?"
                menu:
                    "Tit fuck":
                        call chelsea_seduce_tf_motivated from _call_chelsea_seduce_tf_motivated_1
                    "Blow job":
                        call chelsea_seduce_bj_motivated from _call_chelsea_seduce_bj_motivated
                    "Sex":
                        call chelsea_seduce_sex_motivated from _call_chelsea_seduce_sex_motivated
        else:
            wt_image chubby_motivated_2
            chelsea.c "Slow down there, [chelsea.your_name] ... I'm flattered, but I'm not sure I'm ready to go that far with you yet."
            wt_image chubby_motivated_3
            "[chelsea.name]'s saying 'no', but you can tell she's thinking about it. You should have her resistance worn down soon."
            change chelsea resistance by -5 notify
    elif chelsea.has_tag('happy'):
        wt_image chubby_happy_1
        player.c "You know I want you, don't you, [chelsea.name]?"
        if chelsea.sex_status > 0 or chelsea.test('resistance',55):
            wt_image chubby_seduce_happy_15
            chelsea.c "Really?  Feeling frisky are you?  I guess I should get these clothes off, then."
            wt_image chubby_seduce_happy_1
            "She starts to strip off her clothes as she makes her way towards the boudoir."
            call forced_movement(bathroom) from _call_forced_movement_129
            summon chelsea
            wt_image chubby_seduce_happy_2
            "You strip off your own clothes and go catch up to her. At the bathroom, she surprises you by stopping and tackling you."
            wt_image chubby_seduce_happy_3
            "As you twist around underneath her she plants a big kiss on you."
            wt_image chubby_seduce_happy_17
            chelsea.c "So what were you planning on doing with me today?"
            if chelsea.sex_status == 0:
                "This is your first time having sex with [chelsea.name], so you decide to stick with something you're certain - based on her assets - she's used to men wanting from her."
                call chelsea_seduce_tf_happy from _call_chelsea_seduce_tf_happy
            else:
                $ title = "What do you want from her?"
                menu:
                    "Hand job":
                        call chelsea_seduce_hj_happy from _call_chelsea_seduce_hj_happy
                    "Tit fuck":
                        call chelsea_seduce_tf_happy from _call_chelsea_seduce_tf_happy_1
                    "Blow job":
                        call chelsea_seduce_bj_happy from _call_chelsea_seduce_bj_happy
                    "Sex":
                        call chelsea_seduce_sex_happy from _call_chelsea_seduce_sex_happy
            call forced_movement(living_room) from _call_forced_movement_130
        else:
            wt_image chubby_hypno_happy
            chelsea.c "Slow down there, [chelsea.your_name] ... I'm flattered, but I'm not sure I'm ready to go that far with you yet."
            wt_image chubby_seduce_happy_14
            "[chelsea.name]'s saying 'no', but you can tell that she's thinking about it.  You should have her resistance worn down soon."
            change chelsea resistance by -5 notify
    else:
        wt_image chubby_conflicted_3
        player.c "You know I want you, don't you, [chelsea.name]?  Come with me and let's get you out of that dress.  I want to look at you, and touch you."
        if chelsea.sex_status > 0 or chelsea.test('sos', 20) or chelsea.test('resistance', 40):
            if boudoir.is_here:
                wt_image chubby_seduce_conflicted_1
                "You lead her over to the bed and help her out of her dress.  She's wearing a girdle underneath."
            else:
                call forced_movement(boudoir) from _call_forced_movement_89
                summon chelsea
                wt_image chubby_seduce_conflicted_1
                "You lead her into the boudoir and help her out of her dress.  She's wearing a girdle underneath."
            wt_image chubby_seduce_conflicted_2
            chelsea.c "It's worse than you may have guessed, that's why I wear the girdle.  I hope you're not too disappointed?"
            wt_image chubby_seduce_conflicted_3
            "To [chelsea.name]'s surprise, your only answer is to tackle her."
            wt_image chubby_seduce_conflicted_4
            "A moan escapes her throat as you squeeze her enormous tits and whisper in her ear."
            player.c "You are so fucking sexy."
            wt_image chubby_seduce_conflicted_5
            "Your words, the feel of your hands caressing her breasts, and your cock hardening against her ass has [chelsea.name]'s body responding despite her mental reservations."
            if chelsea.sex_status == 0:
                "This is your first time having sex with [chelsea.name], so you decide to stick with something you're certain - based on her assets - she's used to men wanting from her."
                call chelsea_seduce_tf_conflicted from _call_chelsea_seduce_tf_conflicted
            else:
                $ title = "What do you want?"
                menu:
                    "Tit fuck":
                        call chelsea_seduce_tf_conflicted from _call_chelsea_seduce_tf_conflicted_1
                    "Blow job":
                        call chelsea_seduce_bj_conflicted from _call_chelsea_seduce_bj_conflicted
                    "Sex":
                        call chelsea_seduce_sex_conflicted from _call_chelsea_seduce_sex_conflicted
        else:
            wt_image chubby_conflicted_2
            "She shakes her head."
            if chelsea.test('sos', 10):
                chelsea.c "No, I don't want you to see what I look like under this dress. And I don't want you to touch me while my body's like this.  I'm flattered by the interest, but can we do something else, instead?"
                $ chelsea.temporary_count = 1
            else:
                chelsea.c "No, I don't want you to see what I look like under this dress. And I don't want you to touch me while my body's like this."
                "She knows she's disappointed you, and she's disappointed in herself, too.  She's not up to doing anything more today."
                if chelsea.seduce_action_status == 0:
                    "Although you didn't get far, you did convince [chelsea.name] of the sincerity of your attraction to her. If you could lower her resistance more or improve her comfort with her body, you might get a chance to show her how strong that attraction is."
                    change chelsea sos by 10
                    $ chelsea.seduce_action_status = 1
                elif chelsea.seduce_action_status == 1:
                    "Although you didn't get far, you did convince [chelsea.name] of the sincerity of your attraction to her. If you could lower her resistance more or improve her comfort with her body, you might get a chance to show her how strong that attraction is."
                    change chelsea sos by 5
                    $ chelsea.seduce_action_status = 2
                sys "You need to get her feeling better about her body before she'll let you proceed, or perhaps lower her Resistance to your instructions."
    change player energy by -energy_short notify
    if chelsea.temporary_count > 0:
        $ chelsea.temporary_count = 0
    else:
        $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        end_day
    return

label chelsea_seduce_hj_happy:
    wt_image chubby_seduce_happy_18
    "[chelsea.name] grabs some oil from your toiletries ..."
    wt_image chubby_seduce_happy_19
    "... and applies it to your member ..."
    wt_image chubby_seduce_happy_4
    "... before jerking you off."
    wt_image chubby_seduce_happy_20
    player.c "[player.orgasm_text]"
    wt_image chubby_seduce_happy_5
    chelsea.c "Did that feel good?"
    player.c "Can't you tell?"
    "She giggles."
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.handjob_count == 0:
        "[chelsea.name] likes knowing that she can pleasure you with just her hand.  It helps her feel like she can be a good sex partner, no matter how big her body may be."
        $ chelsea.temporary_count += 10
    else:
        $ chelsea.temporary_count += 5
    change chelsea sos by chelsea.temporary_count
    $ chelsea.temporary_count = 0
    $ chelsea.handjob_count += 1
    orgasm notify
    return

label chelsea_seduce_tf_conflicted:
    player.c "Lie down on your back, [chelsea.name]."
    wt_image chubby_seduce_conflicted_15
    "She knows immediately what you want.  Undoubtedly her husband - and probably every past boyfriend - has taken her like this many times.  It's also a body part she's confident in, and therefore a good way to remind her that she's a sexy and desirable woman, just the way she is."
    wt_image chubby_seduce_conflicted_6
    "She holds her soft mounds tight against your cock and watches intently as you fuck them.  She's enjoying seeing how much pleasure you can get from her body."
    wt_image chubby_seduce_conflicted_7
    "You both groan as you climax and your hot cum spurts onto her breasts."
    wt_image chubby_seduce_conflicted_16
    player.c "[player.orgasm_text]"
    chelsea.c "Oohhh"
    wt_image chubby_seduce_conflicted_8
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        change chelsea sos by 10
    else:
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        change chelsea sos by 5
    if chelsea.titfuck_count == 0:
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    orgasm notify
    return

label chelsea_seduce_tf_motivated:
    wt_image chubby_visit_toned_3_30
    "[chelsea.name] has lost some weight ..."
    wt_image chubby_visit_toned_3_31
    "... but she still has large, amazing tits ..."
    wt_image chubby_visit_toned_3_32
    "... and she seems content to let you fuck them until you cum on her tits, neck and chin."
    wt_image chubby_seduce_motivated_3
    player.c "[player.orgasm_text]"
    wt_image chubby_cum_tits_6
    chelsea.c "Oohhh"
    if chelsea.sex_status == 0:
        "[chelsea.name] interprets your sexual interest in her as validation of the sexiness of her now slimmer body.  It furthers her resolve to continue to get, and remain, in shape."
        $ chelsea.sex_status = 1
        change chelsea desire_c by 10
    else:
        "[chelsea.name] interprets your continued sexual interest in her as validation of the sexiness of her now slimmer body.  It furthers her resolve to continue to get, and remain, in shape."
        change chelsea desire_c by 5
    if chelsea.titfuck_count == 0:
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    orgasm notify
    return

label chelsea_seduce_tf_happy:
    wt_image chubby_seduce_happy_18
    "[chelsea.name] grabs some oil from your toiletries ..."
    wt_image chubby_seduce_happy_21
    "... applies it liberally to her breasts ..."
    wt_image chubby_seduce_happy_6
    "... and then presses her breasts around your cock, letting you fuck the valley in between them."
    wt_image chubby_seduce_happy_7
    "It's an unconventional way to give a tit job, but it works."
    wt_image chubby_seduce_happy_8
    "Just before you cum, [chelsea.name] wraps her soft lips wrap around the head of your cock and swallows each spurt."
    player.c "[player.orgasm_text]"
    wt_image chubby_seduce_happy_9
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        change chelsea sos by 10
    else:
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        change chelsea sos by 5
    if chelsea.titfuck_count == 0:
        wt_image chubby_seduce_happy_6
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    $ chelsea.swallow_count += 1
    orgasm notify
    return

label chelsea_seduce_bj_conflicted:
    wt_image chubby_seduce_conflicted_17
    "[chelsea.name] makes no objection as you guide her head to your cock."
    wt_image chubby_seduce_conflicted_18
    "As she sucks you off, she plays with her breasts ..."
    wt_image chubby_seduce_conflicted_19
    "... and squeezes them extra hard and moans as you cum in her mouth - that's a good sign."
    player.c "[player.orgasm_text]"
    wt_image chubby_seduce_conflicted_10
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        change chelsea sos by 10
    else:
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        change chelsea sos by 5
    if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm notify
    return

label chelsea_seduce_bj_motivated:
    wt_image chubby_visit_toned_3_30
    "[chelsea.name] smiles and removes her remaining clothes as sit beside her and take out your cock."
    wt_image chubby_visit_toned_3_7
    "She makes no objection as you pull her forward, into your lap."
    wt_image chubby_visit_toned_3_8
    "Wrapping her soft lips around your cock, she blows you as you examine her body with your hands."
    wt_image chubby_visit_toned_3_33
    "Between the sight of her naked body, the feeling of her smooth skin under your hand, and her warm wet lips and tongue ..."
    wt_image chubby_seduce_motivated_4
    "... you soon fill her mouth with your jizz."
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_toned_3_33
    if chelsea.sex_status == 0:
        "[chelsea.name] interprets your sexual interest in her as validation of the sexiness of her now slimmer body.  It furthers her resolve to continue to get, and remain, in shape."
        $ chelsea.sex_status = 1
        change chelsea desire_c by 10
    else:
        "[chelsea.name] interprets your continued sexual interest in her as validation of the sexiness of her now slimmer body.  It furthers her resolve to continue to get, and remain, in shape."
        change chelsea desire_c by 5
    if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm notify
    return

label chelsea_seduce_bj_happy:
    wt_image chubby_seduce_happy_9
    "[chelsea.name] gives you a playful lick ..."
    wt_image chubby_seduce_happy_22
    "... then takes your hardening cock into her mouth."
    wt_image chubby_seduce_happy_10
    "She keeps it there, her eyes locked on yours, as she bobs her pretty head up-and-down ..."
    wt_image chubby_seduce_happy_11
    "... until you fill her mouth with cum"
    wt_image chubby_seduce_happy_8
    player.c "[player.orgasm_text]"
    wt_image chubby_seduce_happy_9
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        change chelsea sos by 10
    else:
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        change chelsea sos by 5
    if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm notify
    return

label chelsea_seduce_sex_conflicted:
    if chelsea.sex_status == 2 or chelsea.test('resistance',25):
        wt_image chubby_seduce_conflicted_11
        "[chelsea.name] gasps in surprise as you push yourself into her, but doesn't object. She's already wet, and you slide inside easily."
        wt_image chubby_seduce_conflicted_20
        chelsea.c "Oh!"
        wt_image chubby_seduce_conflicted_12
        "Rolling her onto her side, you're able to change your angle of penetration."
        wt_image chubby_seduce_conflicted_21
        "She bites her lip as your cock strokes in and out of her.  She's enjoying this, but you're not sure she's enjoying it enough."
        wt_image chubby_seduce_conflicted_13
        player.c "I want you to cum, [chelsea.name].  What position's best for you?"
        wt_image chubby_seduce_conflicted_25
        "She scrambles up on top, then to your surprise, she faces away from you. Perhaps her lingering body issues make it easier for her to focus on her own pleasure if she can't scrutinize your face for signs of displeasure?"
        wt_image chubby_seduce_conflicted_14
        "Regardless, she definitely enjoys this position, and she soon cums.  So do you."
        wt_image chubby_seduce_conflicted_24
        chelsea.c "Aahhhhhh"
        wt_image chubby_seduce_conflicted_23
        player.c "[player.orgasm_text]"
        wt_image chubby_seduce_conflicted_22
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        if chelsea.sex_status == 1:
            $ chelsea.sex_status = 2
            change chelsea sos by 10
        else:
            change chelsea sos by 5
        if chelsea.sex_count == 0:
            "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
            change chelsea resistance by -10
        else:
            "Your continued interest in her, sexually, leaves [chelsea.name] feeling good about herself."
        $ chelsea.sex_count += 1
        if chelsea.orgasm_count == 0:
            "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
            change chelsea resistance by -10
        $ chelsea.orgasm_count += 1
        orgasm notify
    else:
        wt_image chubby_seduce_conflicted_3
        chelsea.c "No ... no, I'm not ready for that."
        "You can try again after you lower [chelsea.name]'s resistance. For now, choose another option."
        $ title = "What do you want from her instead?"
        menu:
            "Tit fuck":
                call chelsea_seduce_tf_conflicted from _call_chelsea_seduce_tf_conflicted_2
            "Blow job":
                call chelsea_seduce_bj_conflicted from _call_chelsea_seduce_bj_conflicted_1
            "Nothing":
                "You have her dress.  Maybe you can do something else with her, instead."
                $ chelsea.temporary_count = 1
    return

label chelsea_seduce_sex_motivated:
    if chelsea.sex_status == 2 or chelsea.test('resistance',25):
        wt_image chubby_visit_toned_3_26
        "[chelsea.name] undresses nervously as she watches you do the same."
        wt_image chubby_visit_toned_3_16
        "Her nerves appear to be the result of excitement, rather than apprehension, as she's already wet, making it easy to slide inside her."
        wt_image chubby_seduce_motivated_7
        chelsea.c "Oh!"
        wt_image chubby_visit_toned_3_14
        "She closes her eyes as your cock strokes in and out of her.  She's enjoying this, but you're not sure she's enjoying it enough."
        wt_image chubby_visit_toned_3_13
        player.c "I want you to cum, [chelsea.name].  What position's best for you?"
        wt_image chubby_seduce_motivated_8
        "She scrambles up on top, then to your surprise, she faces away from you.  Perhaps her long-standing body issues make it easier for her to focus on her own pleasure if she can't scrutinize your face for signs of displeasure?"
        wt_image chubby_visit_toned_3_37
        "Regardless, she definitely enjoys this position, and she soon cums.  So do you."
        chelsea.c "Aahhhhhh"
        wt_image chubby_visit_toned_3_36
        player.c "[player.orgasm_text]"
        "[chelsea.name] interprets your continued sexual interest in her as validation of the sexiness of her now slimmer body.  It furthers her resolve to continue to get, and remain, in shape."
        if chelsea.sex_status == 1:
            $ chelsea.sex_status = 2
            change chelsea desire_c by 10
        else:
            change chelsea desire_c by 5
        if chelsea.sex_count == 0:
            "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
            change chelsea resistance by -10
        if chelsea.orgasm_count == 0:
            "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
            change chelsea resistance by -10
        $ chelsea.sex_count += 1
        $ chelsea.orgasm_count += 1
        orgasm notify
    else:
        wt_image chubby_visit_toned_3_4
        chelsea.c "No ... no, I'm not ready for that."
        sys "You can try again after you lower [chelsea.name]'s resistance.  For now, choose another option."
        $ title = "What do you want from her instead?"
        menu:
            "Tit fuck":
                call chelsea_seduce_tf_motivated from _call_chelsea_seduce_tf_motivated_2
            "Blow job":
                call chelsea_seduce_bj_motivated from _call_chelsea_seduce_bj_motivated_1
            "Nothing":
                wt_image chubby_motivated_2
                "You have her dress.  Maybe you can do something else with her, instead."
                $ chelsea.temporary_count = 1
    return

label chelsea_seduce_sex_happy:
    if chelsea.sex_status == 2 or chelsea.test('resistance',25):
        if boudoir.is_here:
            wt_image chubby_seduce_happy_12
            "You lead [chelsea.name] to the bed where it'll be a little more comfortable.  She offers no objections as you move to enter her.  She's already wet, making it easy to slide inside."
        else:
            call forced_movement(boudoir) from _call_forced_movement_90
            summon chelsea
            wt_image chubby_seduce_happy_12
            "You lead [chelsea.name] into the boudoir and to the bed, where it'll be a little more comfortable.  She offers no objections as you move to enter her.  She's already wet, making it easy to slide inside."
        wt_image chubby_seduce_happy_23
        chelsea.c "Oh!"
        wt_image chubby_seduce_happy_24
        player.c "I want you to cum, [chelsea.name].  What position's best for you?"
        wt_image chubby_seduce_happy_13
        "She scrambles up on top, then to your surprise, she faces away from you. Perhaps her lingering body issues make it easier for her to focus on her own pleasure if she can't scrutinize your face for signs of displeasure?"
        wt_image chubby_seduce_happy_25
        "Regardless, she definitely enjoys this position, and she soon cums.  So do you."
        wt_image chubby_seduce_happy_26
        chelsea.c "Aahhhhhh"
        wt_image chubby_seduce_happy_27
        player.c "[player.orgasm_text]"
        "Your continued interest in [chelsea.name], sexually, reinforces to her that men can find her sexy just the way she is."
        if chelsea.sex_status == 1:
            $ chelsea.sex_status = 2
            change chelsea sos by 10
        else:
            change chelsea sos by 5
        if chelsea.sex_count == 0:
            "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
            change chelsea resistance by -10
        $ chelsea.sex_count += 1
        if chelsea.orgasm_count == 0:
            "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
            change chelsea resistance by -10
        $ chelsea.orgasm_count += 1
        orgasm notify
    else:
        wt_image chubby_seduce_happy_16
        chelsea.c "No ... no, I'm not ready for that."
        sys "You can try again after you lower [chelsea.name]'s resistance.  For now, choose another option."
        $ title = "What do you want from her instead?"
        menu:
            "Hand job":
                call chelsea_seduce_hj_happy from _call_chelsea_seduce_hj_happy_1
            "Tit fuck":
                call chelsea_seduce_tf_happy from _call_chelsea_seduce_tf_happy_2
            "Blow job":
                call chelsea_seduce_bj_happy from _call_chelsea_seduce_bj_happy_1
            "Nothing":
                "You have her dress.  Maybe you can do something else with her, instead."
                $ chelsea.temporary_count = 1
    return

# Work Out Actions
label chelsea_work_out:
  $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  $ chelsea.exercise_count += 1
  wt_image chelsea.image
  if not chelsea.has_tag('motivated'):
    wt_image chubby_exercise_conflicted_1
    "You have [chelsea.name] change into suitable clothes for working out, and take her outside."
    wt_image chubby_exercise_conflicted_2
    "You start her off with some stretches ..."
    wt_image chubby_exercise_conflicted_3
    "... then run her through a series of exercises."
    wt_image chubby_exercise_conflicted_4
    "Back in the house, you walk her through the numbers on how she's done."
    if chelsea.exercise_count == 1:
      "They don't mean much to her after her first exercise session, but you hope they will soon."
      change chelsea desire_c by 5 notify
    elif chelsea.exercise_count == 2:
      "[chelsea.name] is surprised to see she's made progress after only two work outs."
      change chelsea desire_c by 10 notify
    elif chelsea.exercise_count == 3:
      "[chelsea.name] is really pleased to see how much better she's doing. Seeing results helps to solidify her resolve."
      change chelsea desire_c by 15 notify
    elif chelsea.exercise_count >= 4:
      "[chelsea.name] is getting a little tired of the workout routine. Continuing to show her the results helps to keep up her motivation."
      change chelsea desire_c by 5 notify
    $ title = "Do you want to conduct a hands on assessment?"
    menu:
      "Yes":
        if chelsea.sex_status > 0 or chelsea.test('desire_c', 20) or chelsea.test('resistance', 60):
          wt_image chubby_exercise_conflicted_5
          "You stand [chelsea.name] up and conduct a physical examination of the changes in her body."
          wt_image chubby_exercise_conflicted_14
          "You include a visual as well as a tactile component to your exam. "
          wt_image chubby_exercise_conflicted_6
          "Amongst other things, the exam gets [chelsea.name] used to being touched by you."
          change chelsea resistance by -5 notify
          if chelsea.exercise_count >= 2:
            $ title = "Go further?"
            menu:
              "Yes, make this sexual":
                if chelsea.sex_status > 0 or chelsea.test('resistance',40):
                  wt_image chubby_exercise_conflicted_15
                  if chelsea.sex_status == 0:
                    "[chelsea.name] seems open to you taking greater liberties with her body today.  In her mind, your arousal is an affirmation of the progress she's making with the exercises.  You haven't had sex with her yet, so you decide to take it slow, with something you're certain - based on her assets - that she's used to men wanting from her."
                    call chelsea_work_out_tf_conflicted from _call_chelsea_work_out_tf_conflicted
                  else:
                    if chelsea.sex_status == 1:
                      "[chelsea.name] seems happy to see you take an interest in her body. In her mind, it confirms the positive progress she's making with the exercises."
                    elif chelsea.sex_status == 2:
                      "Your continued sexual interest in [chelsea.name] confirms in her mind that she's on the right track with the exercises."
                    $ title = "What do you want from her today?"
                    menu:
                      "Tit fuck":
                        call chelsea_work_out_tf_conflicted from _call_chelsea_work_out_tf_conflicted_1
                      "Blow job":
                        call chelsea_work_out_bj_conflicted from _call_chelsea_work_out_bj_conflicted
                      "Sex":
                        call chelsea_work_out_sex_conflicted from _call_chelsea_work_out_sex_conflicted
                else:
                  wt_image chubby_exercise_conflicted_5
                  "That's as far as [chelsea.name] lets you go for now. You could try again when her resistance to you is lower."
                  change player energy by -energy_long notify
              "No, not today":
                change player energy by -energy_long notify
          else:
            "That's far enough for today. You may be able to go further after a future workout."
            change player energy by -energy_long notify
        else:
          chelsea.c "I'm not comfortable with that."
          "You can try again when she's feeling better about showing off or her resistance to you is lower. For now, you'll need to end the session here."
          change player energy by -energy_short notify
      "No":
        "You leave things there for today."
        change player energy by -energy_short notify
  elif chelsea.has_tag('motivated'):
    wt_image chubby_exercise_motivated_12
    "[chelsea.name] is feeling motivated to change her body image. She's working out regularly on her own now, and happily hits the treadmill on your suggestion.  When you check in on her after an hour, she looks tired but happy."
    wt_image chubby_exercise_motivated_13
    player.c "How was the work out?"
    wt_image chubby_exercise_motivated_14
    chelsea.c "Good.  Very good."
    wt_image chubby_exercise_motivated_2
    chelsea.c "I'm a little sticky now, though."
    wt_image chubby_exercise_motivated_3
    player.c "I think the effort is paying off.  Let's chart your progress."
    wt_image chubby_exercise_motivated_15
    "It's easy to chart her progress these days ..."
    wt_image chubby_exercise_motivated_4
    "... as she happily submits to a thorough examination ..."
    wt_image chubby_exercise_motivated_16
    "... of the changes in her body."
    change chelsea desire_c by 5
    change chelsea resistance by -5 notify
    $ title = "Do you want to go further?"
    menu:
      "Go further":
        if chelsea.sex_status > 0 or chelsea.test('resistance',55):
          wt_image chubby_exercise_motivated_18
          if chelsea.sex_status == 0:
            "[chelsea.name] seems open to you taking greater liberties with her body today. In her mind, your arousal is an affirmation of the progress she's making with the exercises. You haven't had sex with her yet, so you decide to take it slow, with something you're certain - based on her assets - that she's used to men wanting from her."
            call chelsea_work_out_tf_motivated from _call_chelsea_work_out_tf_motivated
          else:
            if chelsea.sex_status == 1:
              "[chelsea.name] seems happy to see you take an interest in her body. In her mind, it confirms the positive progress she's making with the exercises."
            elif chelsea.sex_status == 2:
              "Your continued interest in [chelsea.name] sexually confirms in her mind that she is on the right track with the exercises."
            $ title = "What do you want from her today?"
            menu:
              "Tit fuck":
                call chelsea_work_out_tf_motivated from _call_chelsea_work_out_tf_motivated_1
              "Blow job":
                call chelsea_work_out_bj_motivated from _call_chelsea_work_out_bj_motivated
              "Sex":
                call chelsea_work_out_sex_motivated from _call_chelsea_work_out_sex_motivated
        else:
          wt_image chubby_exercise_motivated_17
          "That's as far as [chelsea.name] lets you go for now. You could try again when her resistance to you is lower."
          change player energy by -energy_short notify
      "Stop there":
        "You leave things there for today."
        change player energy by -energy_short notify
  end_day
  return

label chelsea_work_out_tf_conflicted:
    wt_image chubby_exercise_conflicted_16
    "She knows immediately what you want.  No doubt her husband has taken her like this many times."
    if chelsea.blowjob_count > 0:
        wt_image chubby_exercise_conflicted_7
        "She seems to enjoy the experience, too."
        wt_image chubby_exercise_conflicted_17
        "She even licks the head of your cock on the up-thrusts as you tit fuck her."
        wt_image chubby_exercise_conflicted_7
        "You both groan as you climax and your hot cum spurts onto her breasts."
    else:
        wt_image chubby_exercise_conflicted_7
        "She seems to enjoy the experience, too.  You both groan as you climax and your hot cum spurts onto her breasts."
    wt_image chubby_exercise_conflicted_8
    player.c "[player.orgasm_text]"
    chelsea.c "Oohhh"
    if chelsea.sex_status == 0:
        $ chelsea.sex_status = 1
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        change chelsea desire_c by 10
    else:
        "Your continued interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        change chelsea desire_c by 5
    if chelsea.titfuck_count == 0:
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    orgasm
    change player energy by -energy_long notify
    return

label chelsea_work_out_bj_conflicted:
    wt_image chubby_exercise_conflicted_13
    "[chelsea.name] lets you pull her head to your lap.  She opens her mouth and wraps her soft lips around your cock."
    wt_image chubby_exercise_conflicted_9
    "You guide her to her knees and with your hand in her hair, show her how you like your cock sucked."
    wt_image chubby_exercise_conflicted_18
    "When she's done a good enough job, you show your appreciation by emptying your load in her mouth.  She makes no objection, slurping down every drop."
    player.c "[player.orgasm_text]"
    if chelsea.sex_status == 0:
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        $ chelsea.sex_status = 1
        change chelsea desire_c by 10
    else:
        "Your continued interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        change chelsea desire_c by 5
    if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm
    change player energy by -energy_long notify
    return

label chelsea_work_out_sex_conflicted:
  if chelsea.sex_status == 2 or chelsea.test('resistance',25):
    wt_image chubby_exercise_conflicted_10
    "[chelsea.name] gasps in surprise as you push her onto her knees, but doesn't object.   She uses her fingers on herself to help get wet, and you're able soon able to slide inside easily."
    chelsea.c "Oh!"
    wt_image chubby_exercise_conflicted_12
    chelsea.c "Mmmmm ... That feels nice, but can we change positions?  I'd like to be on top."
    $ title = "Change position?"
    menu:
      "Yes, let her be on top":
          wt_image chubby_exercise_conflicted_19
          "[chelsea.name] extricates herself while making sure you stay hard."
          wt_image chubby_exercise_conflicted_11
          "To your surprise, she faces away from you after getting up on top.  It's a position she seems to love, as she's soon cumming, and bringing you along with her."
          wt_image chubby_exercise_conflicted_20
          chelsea.c "Aahhhhhh"
          wt_image chubby_exercise_conflicted_11
          player.c "[player.orgasm_text]"
          if chelsea.orgasm_count == 0:
              "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
              change chelsea resistance by -10
              $ chelsea.orgasm_count += 1
      "No, she's too sexy for you to wait":
        player.c "You're too beautiful.  I can't wait for that."
        wt_image chubby_exercise_conflicted_10
        "You fuck her harder and faster.  She doesn't cum, but you certainly do."
        player.c "[player.orgasm_text]"
        if not chelsea.has_tag('training_exercise_refused_position_change'):
          add tags 'training_exercise_refused_position_change' to chelsea
          change chelsea desire_c by 5
          "She would have preferred to have been in a position where she could have cum, too, but the idea that you found her too sexy to resist reaffirms in her mind that she's on the right track with her exercising."
    "Your continued sexual interest in [chelsea.name] confirms in her mind that she's on the right track with the exercises."
    if chelsea.sex_status == 1:
      $ chelsea.sex_status = 2
      change chelsea desire_c by 10
    else:
      change chelsea desire_c by 5
    if chelsea.sex_count == 0:
      "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
      change chelsea resistance by -10
    $ chelsea.sex_count += 1
    orgasm
    change player energy by -energy_long notify
  else:
    chelsea.c "No ... no, I'm not ready for that."
    "You can try again after you lower [chelsea.name]'s resistance.  For now, choose another option."
    $ title = "What do you want instead?"
    menu:
      "Tit fuck":
        call chelsea_work_out_tf_conflicted from _call_chelsea_work_out_tf_conflicted_2
      "Blow job":
        call chelsea_work_out_bj_conflicted from _call_chelsea_work_out_bj_conflicted_1
      "Nothing":
        pass
  return

label chelsea_work_out_tf_motivated:
  player.c "Come here, [chelsea.name]."
  wt_image chubby_exercise_motivated_19
  "She understands immediately what you want.  Undoubtedly her husband has taken her like this many times."
  wt_image chubby_exercise_motivated_20
  "The exercise she's been doing hasn't reduced the size, or the softness, of her breasts, which feel great wrapped around your cock."
  wt_image chubby_exercise_motivated_7
  "You both groan as you climax and your hot cum spurts onto her breasts."
  wt_image chubby_exercise_motivated_21
  player.c "[player.orgasm_text]"
  chelsea.c "Oohhh"
  if chelsea.sex_status == 0:
      "Your interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
      $ chelsea.sex_status = 1
      change chelsea desire_c by 10
  else:
      "Your continued interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
      change chelsea desire_c by 5
  if chelsea.titfuck_count == 0:
    "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
    change chelsea resistance by -10
  $ chelsea.titfuck_count += 1
  orgasm
  change player energy by -energy_short notify
  return

label chelsea_work_out_bj_motivated:
    wt_image chubby_exercise_motivated_23
    "[chelsea.name] makes no objection as you guide her head onto your hard cock ..."
    wt_image chubby_exercise_motivated_8
    "... and use her mouth for your pleasure."
    wt_image chubby_exercise_motivated_22
    "She also makes no objection when you cum in her mouth ..."
    player.c "[player.orgasm_text]"
    wt_image chubby_exercise_motivated_24
    "... slurping down every drop."
    wt_image chubby_exercise_motivated_5
    "Even the little bit that escapes onto her chin is scooped back up with her finger and swallowed."
    if chelsea.sex_status == 0:
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        $ chelsea.sex_status = 1
        change chelsea desire_c by 10
    else:
        "Your continued interest in her, sexually, leaves [chelsea.name] feeling good about the exercise she's been doing."
        change chelsea desire_c by 5
    if chelsea.blowjob_count == 0:
       "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
       change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm
    change player energy by -energy_short notify
    return

label chelsea_work_out_sex_motivated:
  if chelsea.sex_status == 2 or chelsea.test('resistance',30):
    wt_image chubby_exercise_motivated_6
    "Far from offering resistance, [chelsea.name] provides you an open invitation."
    wt_image chubby_exercise_motivated_9
    "It's not an invitation you're likely to decline."
    chelsea.c "Oh!"
    wt_image chubby_exercise_motivated_10
    "She seems happy to have you inside her.  It doesn't take her long to cum, nor does it take you long to follow her."
    wt_image chubby_exercise_motivated_25
    chelsea.c "Aahhhhhh"
    player.c "[player.orgasm_text]"
    "Your continued sexual interest in [chelsea.name] confirms in her mind that she's on the right track with the exercises."
    if chelsea.sex_status == 1:
      $ chelsea.sex_status = 2
      change chelsea desire_c by 10
    else:
      change chelsea desire_c by 5
    if chelsea.sex_count == 0:
      "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
      change chelsea resistance by -10
    $ chelsea.sex_count += 1
    if chelsea.orgasm_count == 0:
      "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
      change chelsea resistance by -10
    $ chelsea.orgasm_count += 1
    orgasm
    change player energy by -energy_short notify
  else:
    wt_image chubby_exercise_motivated_17
    chelsea.c "No ... no, I'm not ready for that."
    "You can try again after you lower [chelsea.name]'s resistance.  For now, choose another option."
    $ title = "What do you want instead?"
    menu:
      "Tit fuck":
        call chelsea_work_out_tf_motivated from _call_chelsea_work_out_tf_motivated_2
      "Blow job":
        call chelsea_work_out_bj_motivated from _call_chelsea_work_out_bj_motivated_1
      "Nothing":
        pass
  return

# Diet actions
label chelsea_diet:
  $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  call forced_movement(outdoors) from _call_forced_movement_91
  summon chelsea
  wt_image chubby_shopping_2
  "You set [chelsea.name] up for a shopping trip with Candace. Candace is a bit of a ditz, but as a nutritionist one thing she knows about is food."
  wt_image chubby_shopping_1
  "Candace talks to [chelsea.name] about how to choose foods. She focuses the conversation on the topic you asked her to address with [chelsea.name]."
  wt_image chubby_shopping_4
  $ title = "What do you want [chelsea.name] to learn?"
  menu:
    "How to structure a tasty weight loss diet":
      wt_image chubby_shopping_3
      "Candace helps [chelsea.name] to choose tasty foods that are good for her. She also helps her structure a diet that, together with regular work outs, should let her gradually lose weight and keep it off. [chelsea.name] feels encouraged. This is the sort of diet she believes she can stick with."
      change chelsea desire_c by 15
    "How to select sensible portions of her favorite comfort foods":
      wt_image chubby_shopping_3
      "Candace helps [chelsea.name] to figure out what a sensible portion size is for her favorite foods. [chelsea.name] feels good about the process.  Learning how to enjoy her favorite foods in a healthy way helps her feel better about her current lifestyle."
      change chelsea sos by 5
  add tags 'diet_shopping_complete' to chelsea
  call forced_movement(living_room) from _call_forced_movement_92
  summon chelsea
  change player energy by -energy_short notify
  end_day
  return

# Model Actions
label chelsea_model:
  if chelsea.has_tag('lingerie_motivated'):
    if chelsea.has_tag('motivated'):
      $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
      wt_image chubby_lingerie_motivate_1
      if not chelsea.has_tag('lingerie_modelled'):
        "[chelsea.name] is proud to show off how she looks in the lingerie you bought her.  The purple leggings were her own addition, a nod perhaps to the amount of working out she's been doing lately."
        add tags 'lingerie_modelled' to chelsea
        $ chelsea.temporary_count = 10
      else:
        "[chelsea.name] is surprised you want to see her in the lingerie again, but she's happy to comply."
        $ chelsea.temporary_count = 5
      wt_image chubby_lingerie_motivate_18
      "She seems to assume that 'modelling' the lingerie for you means taking it off while you watch ..."
      wt_image chubby_lingerie_motivate_2
      "... so you sit back and enjoy the show."
      wt_image chubby_lingerie_motivate_19
      "She still has some booty that she doesn't mind showing off ..."
      wt_image chubby_lingerie_motivate_20
      "And she still has amazing tits ..."
      wt_image chubby_lingerie_motivate_3
      "... which she also doesn't mind showing off to you."
      wt_image chubby_lingerie_motivate_11
      $ title = "What do you want to do?"
      menu:
        "Make a move":
          if chelsea.sex_status > 0 or chelsea.test('resistance',60):
            wt_image chubby_lingerie_motivate_21
            if chelsea.sex_status == 0:
              "[chelsea.name]'s feeling comfortable enough and sexy enough that she doesn't resist your advances. You haven't had sex with her yet, so you decide to take it slow, with something you're certain - based on her assets - that she's used to men wanting from her."
              call chelsea_model_tf_motivated from _call_chelsea_model_tf_motivated
            else:
              "[chelsea.name]'s feeling comfortable enough and sexy enough that she doesn't resist your advances."
              $ title = "What do you want?"
              menu:
                "Tit fuck":
                  call chelsea_model_tf_motivated from _call_chelsea_model_tf_motivated_1
                "Blow job":
                  call chelsea_model_bj_motivated from _call_chelsea_model_bj_motivated
                "Sex":
                  call chelsea_model_sex_motivated from _call_chelsea_model_sex_motivated
          else:
            wt_image chubby_lingerie_motivate_18
            chelsea.c "Slow down there, Romeo ... I'm flattered, but I'm not sure I'm ready to go that far with you yet."
            wt_image chubby_lingerie_motivate_22
            "[chelsea.name]'s saying 'no', but you can tell that she's thinking about it.  You should have her resistance worn down soon."
            change chelsea resistance by -5
        "End things there":
          "That's enough for today.  You end the session while [chelsea.name] is feeling good about herself."
          change chelsea resistance by -5
      $ chelsea.stripped_count += 1
      change chelsea desire_c by chelsea.temporary_count
      change player energy by -energy_short notify
      $ chelsea.temporary_count = 0
      end_day
    else:
      "[chelsea.name] can't fit into the lingerie you bought her yet. Select another action for today."
  elif chelsea.has_tag('lingerie_happy'):
    if chelsea.has_tag('conflicted') or chelsea.has_tag('happy'):
      $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
      wt_image chubby_lingerie_flattering_1
      if not chelsea.has_tag('lingerie_modelled'):
        "[chelsea.name] has been hoping you would give her a chance to wear her new lingerie."
        add tags 'lingerie_modelled' to chelsea
        $ chelsea.temporary_count = 5
      else:
        "[chelsea.name] is surprised you want to see her in the lingerie again, but she's happy to comply."
        $ chelsea.temporary_count = 0
      wt_image chubby_lingerie_flattering_7
      "It makes her feel sexy - sexy enough that she doesn't mind showing her body off to you."
      $ title = "What do you want to do?"
      menu:
        "Make a move":
          if chelsea.sex_status > 0 or chelsea.test('resistance', 60):
            if chelsea.sex_status == 0:
              wt_image chubby_lingerie_flattering_2
              "[chelsea.name]'s feeling comfortable enough and sexy enough that she doesn't resist your advances. You haven't had sex with [chelsea.name] yet, so you decide to take it slow, with something you're certain - based on her assets - that she's used to men wanting from her."
              call chelsea_model_tf_happy from _call_chelsea_model_tf_happy
            else:
              wt_image chubby_lingerie_flattering_2
              "[chelsea.name]'s feeling comfortable enough and sexy enough that she doesn't resist your advances."
              $ title = "What do you want?"
              menu:
                "Hand job":
                  call chelsea_model_hj_happy from _call_chelsea_model_hj_happy
                "Tit fuck":
                  call chelsea_model_tf_happy from _call_chelsea_model_tf_happy_1
                "Blow job":
                  call chelsea_model_bj_happy from _call_chelsea_model_bj_happy
                "Sex":
                  call chelsea_model_sex_happy from _call_chelsea_model_sex_happy
          else:
            wt_image chubby_lingerie_flattering_1
            chelsea.c "Slow down there, [chelsea.your_name] - I'm flattered, but I'm not sure I'm ready to go that far with you yet."
            wt_image chubby_lingerie_flattering_8
            "[chelsea.name]'s saying no, but you can tell that she's thinking about it.  You should have her resistance worn down soon."
            change chelsea resistance by -5
        "End things there":
          "That's enough for today. You end the session while [chelsea.name] is feeling good about herself."
          change chelsea resistance by -5
      $ chelsea.stripped_count += 1
      if chelsea.temporary_count > 0:
        change chelsea sos by chelsea.temporary_count
        $ chelsea.temporary_count = 0
      change player energy by -energy_short notify
      end_day
    else:
      "The lingerie you bought her is too big for [chelsea.name]'s new, slimmer figure.  Select another action for today."
  else:
    "You need to give [chelsea.name] some lingerie first. You can try this again once you have done so. For now, make another choice."
  return

label chelsea_model_hj_happy:
    wt_image chubby_lingerie_flattering_14
    "You decide not to push [chelsea.name] too far today. You simply have her kneel in front of you and jerk you off.  She does so with enthusiasm ..."
    wt_image chubby_lingerie_flattering_24
    "... even tickling the tip of your cock with her tongue as she does so ..."
    wt_image chubby_lingerie_flattering_6
    "... laughing as she feels your hot cum splatter on her tits."
    player.c "[player.orgasm_text]"
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.handjob_count == 0:
        "[chelsea.name] likes knowing that she can pleasure you with just her hand.  It helps her feel like she can be a good sex partner, no matter how big her body may be."
        $ chelsea.temporary_count += 5
    $ chelsea.handjob_count += 1
    orgasm
    return

label chelsea_model_tf_motivated:
    player.c "Come here, [chelsea.name]."
    wt_image chubby_lingerie_motivate_15
    "She knows immediately what you want - undoubtedly her husband has taken her like this many times."
    wt_image chubby_lingerie_motivate_23
    "It's an experience she seems to enjoy ..."
    wt_image chubby_lingerie_motivate_16
    "... even tickling the tip of your cock with her tongue as she tit fucks you."
    wt_image chubby_lingerie_motivate_24
    player.c "[player.orgasm_text]"
    wt_image chubby_lingerie_motivate_25
    chelsea.c "Oohhh"
    if chelsea.sex_status == 0:
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the changes in her body."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.titfuck_count == 0:
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    orgasm
    return

label chelsea_model_bj_motivated:
    player.c "Come here, [chelsea.name], and kneel in front of me."
    wt_image chubby_lingerie_motivate_26
    "For a moment she thinks you may want her breasts, but she makes no objection as you guide her mouth onto your hard cock."
    wt_image chubby_lingerie_motivate_8
    "Wrapping her soft lips tightly around your cock, she bobs her head back-and-forth along your shaft ..."
    wt_image chubby_lingerie_motivate_30
    "... and willingly accepts the consequences of her actions ..."
    wt_image chubby_lingerie_motivate_27
    player.c "[player.orgasm_text]"
    wt_image chubby_lingerie_motivate_28
    "... capturing your load and swallowing every drop."
    if chelsea.sex_status == 0:
        "Your interest in her, sexually, leaves [chelsea.name] feeling good about the changes in her body."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.blowjob_count == 0:
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.facial_count += 1
    orgasm
    return

label chelsea_model_sex_motivated:
    if chelsea.test('resistance',30) or chelsea.sex_status > 0:
        wt_image chubby_lingerie_motivate_12
        "[chelsea.name] makes no objection as you lay her back on the sofa and lift her legs, giving you access to her sex.  She's already wet, and you slide into her easily."
        wt_image chubby_lingerie_motivate_39
        chelsea.c "Ahhhh"
        wt_image chubby_lingerie_motivate_40
        "Wearing the lingerie seems to have put [chelsea.name] in the mood.  She rubs her clit as you fuck her ..."
        wt_image chubby_lingerie_motivate_7
        "... soon strokes herself to orgasm just before you stroke yourself to orgasm inside her."
        wt_image chubby_lingerie_motivate_41
        chelsea.c "Aahhhhhh"
        wt_image chubby_lingerie_motivate_42
        player.c "[player.orgasm_text]"
        if chelsea.sex_status == 1:
            "Your continued sexual interest in [chelsea.name] confirms in her mind that she's on the right track with her body changes."
            $ chelsea.sex_status = 2
            $ chelsea.temporary_count += 5
        if chelsea.sex_count == 0:
            wt_image chubby_lingerie_motivate_48
            "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
            change chelsea resistance by -10
        $ chelsea.sex_count += 1
        if chelsea.orgasm_count == 0:
            wt_image chubby_lingerie_motivate_48
            "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
            change chelsea resistance by -10
        $ chelsea.orgasm_count += 1
        orgasm notify
    else:
        wt_image chubby_lingerie_motivate_11
        chelsea.c "No ... no, I'm not ready for that."
        "You can try again after you lower [chelsea.name]'s resistance. For now, choose another option."
        $ title = "What do you want instead?"
        menu:
            "Tit fuck":
                call chelsea_model_tf_motivated from _call_chelsea_model_tf_motivated_2
            "Blow job":
                call chelsea_model_bj_motivated from _call_chelsea_model_bj_motivated_1
            "Nothing":
                pass
    return

label chelsea_model_tf_happy:
    player.c "Come here, [chelsea.name]."
    wt_image chubby_lingerie_flattering_3
    "She knows immediately what you want.  Undoubtedly her husband has taken her like this many times ..."
    wt_image chubby_lingerie_flattering_9
    "... an experience she seems to enjoy, though likely not nearly so much as you do."
    wt_image chubby_lingerie_flattering_21
    player.c "[player.orgasm_text]"
    wt_image chubby_lingerie_flattering_11
    chelsea.c "Oohhh"
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.titfuck_count == 0:
        "Letting you use her breasts like this for the first time causes [chelsea.name] to think of you in more intimate terms."
        change chelsea resistance by -10
    $ chelsea.titfuck_count += 1
    orgasm
    return

label chelsea_model_bj_happy:
    player.c "Come here, [chelsea.name], and kneel in front of me."
    wt_image chubby_lingerie_flattering_4
    "For a moment she thinks you may want her breasts, but she makes no objection as you guide her mouth onto your hard cock."
    wt_image chubby_lingerie_flattering_17
    "Wrapping her soft lips tightly around your cock, she bobs her head back-and-forth along your shaft ..."
    wt_image chubby_lingerie_flattering_22
    "... and willingly accepts the consequences of her actions ..."
    player.c "[player.orgasm_text]"
    wt_image chubby_lingerie_flattering_10
    "... capturing your load and swallowing every drop."
    if chelsea.sex_status == 0:
        "If she had reason to doubt your attraction to her before, she has no reason to do so any longer."
        $ chelsea.sex_status = 1
        $ chelsea.temporary_count += 5
    if chelsea.blowjob_count == 0:
        wt_image chubby_lingerie_flattering_16
        "Being willing to take you into her mouth for the first time demonstrates to [chelsea.name] that she's ready to drop her boundaries for you."
        change chelsea resistance by -10
    $ chelsea.blowjob_count += 1
    $ chelsea.swallow_count += 1
    orgasm
    return

label chelsea_model_sex_happy:
    if chelsea.test('resistance',30) or chelsea.sex_status > 0:
        wt_image chubby_lingerie_flattering_13
        "[chelsea.name] makes no objection as you lay her down on her back and spread her legs. She's already wet, and you slide into her easily."
        chelsea.c "Ahhhh"
        wt_image chubby_lingerie_flattering_5
        "Modeling the lingerie seems to have put [chelsea.name] in the mood. She plays with herself as you fuck her, and cums shortly before you do."
        wt_image chubby_lingerie_flattering_23
        chelsea.c "Aahhhhhh"
        player.c "[player.orgasm_text]"
        if chelsea.sex_status == 1:
            "Your continued sexual interest in [chelsea.name] confirms in her mind that she's sexy just the way she is."
            $ chelsea.sex_status = 2
            $ chelsea.temporary_count += 5
        if chelsea.sex_count == 0:
          "Having you inside her for the first time puts your relationship with [chelsea.name] into a new category in her mind.  You're now one of the few men she's trusted enough to become intimate with."
          change chelsea resistance by -10
        $ chelsea.sex_count += 1
        if chelsea.orgasm_count == 0:
          "Cumming with you for the first time has [chelsea.name] feeling more favorably disposed towards you."
          change chelsea resistance by -10
        $ chelsea.orgasm_count += 1
        orgasm
    else:
        wt_image chubby_lingerie_flattering_2
        chelsea.c "No ... no, I'm not ready for that."
        "You can try again after you lower [chelsea.name]'s resistance. For now, choose another option."
        $ title = "What do you want instead?"
        menu:
            "Hand job":
                call chelsea_model_hj_happy from _call_chelsea_model_hj_happy_1
            "Tit fuck":
                call chelsea_model_tf_happy from _call_chelsea_model_tf_happy_2
            "Blow job":
                call chelsea_model_bj_happy from _call_chelsea_model_bj_happy_1
            "Nothing":
                pass
    return

## Post-Training Character Actions
# Continuing actions spend time with her
label chelsea_spend_time:
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags, this also advances visit_count by 1 in end_day label
    if chelsea.has_tag('bbw'):
        if chelsea.visit_outfit == 1:
            wt_image chubby_visit_bbw_1_6
            "[chelsea.name] arrives looking and feeling great. She's happy with her looks and body and feeling confident - sexually confident."
            wt_image chubby_visit_bbw_1_1
            "She slides onto the sofa beside you and aggressively grabs your crotch."
            chelsea.c "I don't imagine you called me over here just to talk.  So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_1_bbw:
                "You're going to pleasure her":
                    wt_image chubby_visit_bbw_1_34
                    player.c "Today, we're going to focus on making you feel good."
                    wt_image chubby_visit_bbw_1_23
                    "[chelsea.name] moans as you squeeze her breasts ..."
                    wt_image chubby_visit_bbw_1_35
                    chelsea.c "Aahhh"
                    wt_image chubby_visit_bbw_1_36
                    "... and then again, louder, as you pinch and roll her nipples between your fingers."
                    wt_image chubby_visit_bbw_1_24
                    chelsea.c "Aahhhh"
                    wt_image chubby_visit_bbw_1_37
                    "And when you replace your fingers with your lips, teeth, and tongue, you can tell she's close to orgasm even before you've touched her slit."
                    wt_image chubby_visit_bbw_1_38
                    $ title = "How do you want to finish her off?"
                    menu:
                        "Head between her legs":
                            wt_image chubby_visit_bbw_1_39
                            "Working over her tits has [chelsea.name] so turned on, you barely have time to lick up-and-down her slit twice before she's cumming at the end of your tongue."
                        "Have her ride your face":
                            wt_image chubby_visit_bbw_1_40
                            "At first, [chelsea.name]'s confused by the change in position ..."
                            wt_image chubby_visit_bbw_1_41
                            "... but when you turn her around and jab your tongue inside her, she soon covers your face with her cum-juice."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_bbw_1_42
                    chelsea.c "Wow, that was amazing, [chelsea.your_name].  My girl-parts have rarely felt so good!"
                    $ chelsea.orgasm_count += 1
                    $ chelsea.pleasure_her_count += 1
                    change player energy by -energy_short notify
                "Blow job":
                    wt_image chubby_visit_bbw_1_43
                    player.c "Well since you're down there, we may as well put you to work."
                    wt_image chubby_visit_bbw_1_44
                    "As she licks your cock, [chelsea.name] plays with her nipple."
                    chelsea.c "I'm horny, too, [chelsea.your_name].  How about you finger me while I blow you?"
                    $ title = "What do you think?"
                    menu:
                        "Sounds fair":
                            wt_image chubby_visit_bbw_1_45
                            "As [chelsea.name] pleasures your cock, you push your fingers in-and-out of her rapidly wetting snatch."
                            wt_image chubby_visit_bbw_1_46
                            "It's not long before you're both ready to cum.  You push her head down firmly on your cock and are rewarded with the muffled sounds of her own orgasm as you fill her mouth with sperm."
                            player.c "[player.orgasm_text]"
                            chelsea.c "nnnnnnn"
                            wt_image chubby_visit_bbw_1_6
                            chelsea.c "That was fun, [chelsea.your_name]."
                            $ chelsea.pleasure_her_count += 1
                            $ chelsea.orgasm_count += 1
                        "Just fuck her mouth":
                            wt_image chubby_visit_bbw_1_47
                            "You're not concerned that she's horny right now.  You're just concerned that you want to cum, and that you want to use her mouth to do so."
                            player.c "[player.orgasm_text]"
                            wt_image chubby_visit_bbw_1_6
                            chelsea.c "I guess you needed that bad, huh?  Maybe next time we can think about my needs, too?"
                            if player.has_tag('dominant') and chelsea.spanked > 1:
                                pass
                            else:
                                $ chelsea.relationship_counter -= 0.5
                    $ chelsea.swallow_count += 1
                    $ chelsea.blowjob_count += 1
                    orgasm notify
                "Tit fuck":
                    wt_image chubby_visit_bbw_1_10
                    chelsea.c "My tits?  Really?  Do you like them that much, [chelsea.your_name]?"
                    wt_image chubby_visit_bbw_1_11
                    player.c "Yes, I do, actually."
                    wt_image chubby_visit_bbw_1_23
                    chelsea.c "Do you like them enough to get hard at the thought of fucking them"
                    wt_image chubby_visit_bbw_1_24
                    chelsea.c "Oh!  Never mind, I can feel that you do."
                    wt_image chubby_visit_bbw_1_12
                    chelsea.c "Okay, then, [chelsea.your_name]."
                    wt_image chubby_visit_bbw_1_2
                    chelsea.c "Fuck away."
                    wt_image chubby_visit_bbw_1_25
                    "You're happy to do exactly that, plowing away as she holds her soft mounds into a valley for you. She moans softly as you rub your hard cock back and forth against her. She likes that you enjoy using her body this way ..."
                    chelsea.c "Aahhhh"
                    wt_image chubby_visit_bbw_1_3
                    "... and you soon show her exactly how much you like it, shooting your load over her chest, neck, and chin."
                    wt_image chubby_cum_tits_1
                    player.c "[player.orgasm_text]"
                    chelsea.c "Mmmm.  Glad I could be of service, [chelsea.your_name]."
                    $ chelsea.titfuck_count += 1
                    orgasm notify
                "On her back":
                    call chelsea_spend_time_bbw_1_missionary from _call_chelsea_spend_time_bbw_1_missionary
                "Doggy style":
                    wt_image chubby_visit_bbw_1_7
                    "You lift [chelsea.name] up by her ample bosom ..."
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_bbw_1_8
                    "... bend her over the sofa ..."
                    wt_image chubby_visit_bbw_1_4
                    "... and pull up her dress."
                    wt_image chubby_visit_bbw_1_9
                    "She gasps as you enter her..."
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_bbw_1_5
                    "... and then again, louder, as you both cum."
                    wt_image chubby_visit_bbw_1_26
                    chelsea.c "Ahhhhhh"
                    wt_image chubby_visit_bbw_1_5
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_bbw_1_6
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    wt_image chubby_visit_bbw_1_19
                    player.c "Get up here and sit on me."
                    wt_image chubby_visit_bbw_1_20
                    "One thing about a big woman like [chelsea.name], when she sits on you, you can feel it.  And the weight of her soft ass grinding into your hard cock feels incredible."
                    chelsea.c "Like this?"
                    wt_image chubby_visit_bbw_1_29
                    player.c "Sort of, but with less clothes on."
                    wt_image chubby_visit_bbw_1_30
                    "She moans as you squeeze her breast."
                    chelsea.c "Aahhhh"
                    wt_image chubby_visit_bbw_1_21
                    "You help her undress, and vice versa, which is all the foreplay either of you need.  As she settles her weight down onto your hard dick straining against your jeans, it's your turn to moan."
                    chelsea.c "Like this then?"
                    player.c "Almost.  Just a bit more clothing to remove."
                    wt_image chubby_visit_bbw_1_31
                    "A moment later, she sinks down onto you, your shaft buried to the hilt in her wetness, her weight pressing into you."
                    wt_image chubby_visit_bbw_1_32
                    "Then she starts to ride you, her warm, wet snatch gripping your cock as she moves up-and-down your shaft."
                    wt_image chubby_visit_bbw_1_33
                    "You're almost at the edge, and so is she, when she suddenly spins around and finishes you both off."
                    wt_image chubby_visit_bbw_1_22
                    chelsea.c "Aahhhhhh"
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_bbw_1_6
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_visit_bbw_1_6
                    chelsea.c "Really?  Well, aren't you full of surprises."
                    "You thought talking to her was a good idea, but it's clear she's ready to spread her legs for you. All you have to do is ask."
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            "You spend an enjoyable couple of hours chatting with [chelsea.name]. She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger
                        "Change your mind and fuck her":
                            call chelsea_spend_time_bbw_1_missionary from _call_chelsea_spend_time_bbw_1_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift
                        "Ask her to be your girlfriend":
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend
        elif chelsea.visit_outfit == 2:
            wt_image chubby_visit_bbw_2_15
            "[chelsea.name] is all smiles when she arrives."
            wt_image chubby_visit_bbw_2_1
            chelsea.c "Hi, [chelsea.your_name].  Were you missing me ..."
            wt_image chubby_visit_bbw_2_8
            chelsea.c "... or these?"
            wt_image chubby_visit_bbw_2_21
            "Seemingly pleased with herself at catching you off guard, she pulls her top back in place."
            chelsea.c "I don't imagine you called me over here just to talk.  So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_2_bbw:
                "You're going to finger her":
                    wt_image chubby_visit_bbw_2_47
                    "Stepping behind her, you kiss her as you fondle her boobs."
                    wt_image chubby_visit_bbw_2_48
                    player.c "You sound like you're already worked up.  I think I'd better look after that."
                    wt_image chubby_visit_bbw_2_49
                    "Standing [chelsea.name] up, you pull off her clothes ..."
                    wt_image chubby_visit_bbw_2_50
                    "... kiss her belly ..."
                    wt_image chubby_visit_bbw_2_51
                    "... and then pull her back down so she's sitting in front of you."
                    wt_image chubby_visit_bbw_2_52
                    "She's already slick with arousal as you run your fingers along her sex ..."
                    wt_image chubby_visit_bbw_2_53
                    "... and she gets wetter still as you slide your finger inside her."
                    wt_image chubby_visit_bbw_2_54
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_bbw_2_55
                    "[chelsea.name]'s enjoying this, and tries to hold out for as long as she can, but the sensation of your hand thumping against her clit as your finger slides in-and-out of her eventually overwhelms her."
                    wt_image chubby_visit_bbw_2_56
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_bbw_2_12
                    chelsea.c "Wow, that felt great, [chelsea.your_name].  Not as good as your cock does, but still really nice."
                    $ chelsea.orgasm_count += 1
                    $ chelsea.pleasure_her_count += 1
                    change player energy by -energy_short notify
                "Blow job":
                    player.c "I want your mouth."
                    wt_image chubby_visit_bbw_2_24
                    chelsea.c "My mouth, huh?  I guess I can guess where you want it, [chelsea.your_name]."
                    wt_image chubby_visit_bbw_2_25
                    "Removing your cock from your pants ..."
                    wt_image chubby_visit_bbw_2_26
                    "... she kisses and licks up-and-down the shaft ..."
                    wt_image chubby_visit_bbw_2_4
                    "... then she successfully guesses exactly where you want her mouth."
                    wt_image chubby_visit_bbw_2_27
                    "The blowjob is a nice, leisurely one."
                    wt_image chubby_visit_bbw_2_28
                    "[chelsea.name] takes her time, and seems to derive pleasure, herself, from the process of bringing you pleasure."
                    wt_image chubby_visit_bbw_2_29
                    "As drawn out as it may be, though, eventually you need to cum."
                    wt_image chubby_visit_bbw_2_30
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image chubby_visit_bbw_2_31
                            player.c "[player.orgasm_text]"
                            wt_image chubby_visit_bbw_2_32
                            "The slow, teasing build-up stimulated an unusually strong response in you.  Watching [chelsea.name] struggle to swallow the copious load of cum your balls pump into her is almost as enjoyable as the blowjob itself."
                            wt_image chubby_visit_bbw_2_30
                            $ chelsea.swallow_count += 1

                        "On her":
                            wt_image chubby_visit_bbw_2_5
                            player.c "[player.orgasm_text]"
                            wt_image chubby_visit_bbw_2_33
                            "She's torn between finding the feeling of your sticky jizz dripping down her face a bit icky, and feeling pleased at the evidence of how much she turned you on."
                            wt_image chubby_visit_bbw_2_34
                            $ chelsea.facial_count += 1
                    chelsea.c "Wow, I guess I know that was appreciated!"
                    $ chelsea.blowjob_count += 1
                    orgasm notify
                "On her back":
                    wt_image chubby_visit_bbw_2_41
                    player.c "You're flaunting your tits, so I know they're ready to fuck, but what about the rest of you?"
                    wt_image chubby_visit_bbw_2_10
                    player.c "Is your pussy ready for a fucking?"
                    call chelsea_spend_time_bbw_2_missionary from _call_chelsea_spend_time_bbw_2_missionary
                "From behind":
                    player.c "Get naked and bend over."
                    wt_image chubby_visit_bbw_2_16
                    chelsea.c "Gee, aren't you the sweet talker?"
                    wt_image chubby_visit_bbw_2_18
                    "Despite her teasing, she scrambles quickly out of her clothes and turns around."
                    wt_image chubby_visit_bbw_2_2
                    "Once she's naked you step behind her ..."
                    wt_image chubby_visit_bbw_2_23
                    "... and plunge into her already wet pussy."
                    wt_image chubby_visit_bbw_2_6
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_bbw_2_19
                    "She came here hoping to get fucked, and a fucking is exactly what you give her.  She gasps in pleasure as you pound into her, and as she cums, she brings you along with her."
                    wt_image chubby_visit_bbw_2_22
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_bbw_2_20
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_bbw_2_18
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    wt_image chubby_visit_bbw_2_35
                    player.c "I'm not going to fuck you, but if you're as horny as you seem, I'll let you fuck me."
                    wt_image chubby_visit_bbw_2_36
                    "[chelsea.name] pretty much throws herself on you."
                    wt_image chubby_visit_bbw_2_37
                    "She must truly be horny, as she doesn't even bother to turn around to face away from you."
                    wt_image chubby_visit_bbw_2_38
                    "Instead, with her weight pressing down on you, she rides you facing forward until you both cum."
                    wt_image chubby_visit_bbw_2_39
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_bbw_2_7
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_bbw_2_40
                    chelsea.c "Mmmmm, that was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_visit_bbw_2_16
                    chelsea.c "Really?  Are you sure you want to talk when you could be playing with these instead?"
                    wt_image chubby_visit_bbw_2_17
                    "She pulls her top back down.  Just chatting while she's sitting there bare-breasted is going to take some willpower."
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            "You spend an enjoyable couple of hours chatting with [chelsea.name]. She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_1
                        "Change your mind and fuck her":
                            wt_image chubby_visit_bbw_2_11
                            player.c "You're flaunting your tits, so I know they're ready to fuck, but what about the rest of you?"
                            wt_image chubby_visit_bbw_2_42
                            player.c "Is your pussy ready for a fucking?"
                            call chelsea_spend_time_bbw_2_missionary from _call_chelsea_spend_time_bbw_2_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_1
                        "Ask her to be your girlfriend":
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_1
        elif chelsea.visit_outfit == 3 and chelsea.has_item(lingerie) and chelsea.visit_sex_count >= chelsea.visit_talk_count:
            wt_image chubby_gf_bbw_2_7
            "[chelsea.name] arrives looking perky and happy."
            chelsea.c "Hi [chelsea.your_name]!  Just give me a minute and I'll be right with you."
            wt_image current_location.image
            "She ducks into your bathroom, reappearing a few minutes later wearing decidedly less clothes."
            wt_image chubby_gf_bbw_2_8
            chelsea.c "You were sweet enough to buy me lingerie, so I figured you might want to see me in some."
            wt_image chubby_gf_bbw_2_9
            chelsea.c "Or maybe you'd like to do more than just see me in it?  I don't imagine you called me over here just to talk.  So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_3_bbw:
                "Foot job":
                    player.c "I want to fuck your feet."
                    wt_image chubby_gf_bbw_2_1
                    chelsea.c "My feet?  That's kind of kinky."
                    "She sits down on the sofa ..."
                    wt_image chubby_gf_bbw_2_23
                    "... sliding over to make room for you as you sit down beside her.  Placing first one, then the other, against your cock, she creates a hollow between her feet and starts sliding her soles up and down."
                    wt_image chubby_gf_bbw_2_14
                    "It feels good ... really good ... and [chelsea.name] seems to be enjoying her self, too, as she places a hand between her legs and plays with herself as she fucks you with her feet."
                    chelsea.c "Ahhhh"
                    wt_image chubby_gf_bbw_2_4
                    "Whether it's the kinkiness of the situation, or watching you get turned on by a different part of her body, or her just enjoying the feel of your cock against her feet as she plays with herself, [chelsea.name] ends up enjoying the foot job almost as much as you do, and as your hot sperm shoots up and onto her feet, she cums, too."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_gf_bbw_2_24
                    player.c "[player.orgasm_text]"
                    chelsea.c "I see you liked the lingerie, or my feet, or both!"
                    $ chelsea.footjob_count += 1
                    $ chelsea.masturbation_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Tit fuck":
                    player.c "I want to fuck those big mounds of yours."
                    wt_image chubby_gf_bbw_2_10
                    "She pulls the top of her negligee down."
                    chelsea.c "These mounds?"
                    player.c "Those are the ones."
                    wt_image chubby_gf_bbw_2_2
                    "[chelsea.name] kneels down and pushes her tits together around your cock, trapping it in her soft flesh and creating a nice, warm valley for you to fuck."
                    wt_image chubby_gf_bbw_2_26
                    "She moans as you start thrusting back and forth, not so much because it feels good to her, but because it turns her on to see how turned on you are by her body."
                    chelsea.c "Oh"
                    wt_image chubby_gf_bbw_2_25
                    "After a few minutes of fucking her tits, you show her exactly how turned on you are, adoring her chest with the contents of your balls as she looks on, pleased with herself."
                    player.c "[player.orgasm_text]"
                    chelsea.c "Mmmmm.  That was fun, [chelsea.your_name]."
                    $ chelsea.titfuck_count += 1
                    orgasm notify
                "Blow job":
                    player.c "I want you to blow me."
                    wt_image chubby_gf_bbw_2_10
                    chelsea.c "Sure [chelsea.your_name], I'll do that for you. Consider it a 'thank you' for the lingerie."
                    "She pulls down the top of the negligee, revealing her massive boobs ..."
                    wt_image chubby_gf_bbw_2_11
                    "... then she kneels down and takes your cock into her mouth."
                    wt_image chubby_gf_bbw_2_27
                    "It's a pretty good blow job. Her tongue darts back and forth, flicking along your cock as her warm, wet lips and her soft hand caress both your balls and your shaft."
                    wt_image chubby_gf_bbw_2_12
                    "She keeps looking up at you as she blows you, checking to make sure that you're enjoying her 'thank you'."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image chubby_gf_bbw_2_3
                            "You are, and you provide your 'you're welcome' in the form of your jizz, spurting into and down the back of throat as she struggles to swallow it all without spilling any."
                            player.c "[player.orgasm_text]"
                            wt_image chubby_gf_bbw_2_12
                            $ chelsea.swallow_count += 1
                        "On her":
                            wt_image chubby_gf_bbw_2_28
                            "You are, and you provide your 'you're welcome' in the form of your warm jizz, spurting up and onto her waiting breasts."
                            player.c "[player.orgasm_text]"
                            $ chelsea.facial_count += 1
                    chelsea.c "Mmmmm, I guess I know that was appreciated!"
                    $ chelsea.blowjob_count += 1
                    orgasm notify
                "On her back":
                    player.c "You fucking tease, you came here to get your pussy pounded, didn't you?"
                    wt_image chubby_gf_bbw_2_15
                    chelsea.c "Yes"
                    "She pulls her panties down, a big grin on her face."
                    call chelsea_spend_time_bbw_3_missionary from _call_chelsea_spend_time_bbw_3_missionary
                "Doggy style":
                    player.c "You won't need those panties on for what I have in mind."
                    wt_image chubby_gf_bbw_2_15
                    chelsea.c "Oh, good!"
                    "She grins at you as she pulls down her underpants, giving you easy access to her sex."
                    wt_image chubby_gf_bbw_2_16
                    "Without another word, you turn [chelsea.name] around and plunge into her already wet pussy. She gasps in pleasure as you enter her..."
                    chelsea.c "Ahhhh"
                    wt_image chubby_gf_bbw_2_17
                    "... and then again a few minutes later, as you fuck the both of you to climax."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_gf_bbw_2_16
                    player.c "[player.orgasm_text]"
                    wt_image chubby_gf_bbw_2_10
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    player.c "I don't want to fuck you.  I want you to fuck me."
                    wt_image chubby_gf_bbw_2_10
                    chelsea.c "That can be arranged."
                    wt_image chubby_gf_bbw_2_5
                    "She climbs on top of you as you sit down ..."
                    wt_image chubby_gf_bbw_2_6
                    "... settling the full weight of her body down on you as she impales herself on your hard dick."
                    wt_image chubby_gf_bbw_2_5
                    "Then she starts riding you, her body crashing down, pressing you into the sofa as her warm, wet cunt slides up and down your cock until she fucks you both to orgasm."
                    wt_image chubby_gf_bbw_2_18
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_gf_bbw_2_29
                    player.c "[player.orgasm_text]"
                    wt_image chubby_gf_bbw_2_10
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_gf_bbw_2_8
                    chelsea.c "Really? I'm dressed like this and you just want to talk?"
                    wt_image chubby_gf_bbw_2_1
                    "She sits down across from you, a twinkle in her eye.  She's ready to chat with you, but it's clear she'd rather spread her legs for you"
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            wt_image chubby_gf_bbw_2_31
                            "You spend an enjoyable couple of hours chatting with [chelsea.name]. She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_2
                        "Change your mind and fuck her":
                            player.c "You'd rather fuck than talk, wouldn't you?"
                            wt_image chubby_gf_bbw_2_31
                            chelsea.c "Yes"
                            call chelsea_spend_time_bbw_3_missionary from _call_chelsea_spend_time_bbw_3_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            wt_image chubby_gf_bbw_2_1
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_2
                        "Ask her to be your girlfriend":
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_2
    elif chelsea.has_tag('toned'):
        if chelsea.visit_outfit == 1:
            wt_image chubby_visit_toned_1_1
            "[chelsea.name] arrives looking amazing."
            wt_image chubby_visit_toned_1_2
            "She comes over and gives you a quick kiss."
            wt_image chubby_visit_toned_1_28
            chelsea.c "I don't imagine you called me over here just to talk.  So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_1_toned:
                "You're going to pleasure her":
                    call forced_movement(boudoir) from _call_forced_movement_131
                    summon chelsea no_follows
                    wt_image chubby_visit_toned_1_9
                    "You bring [chelsea.name] into the boudoir and pull her on top of you ..."
                    wt_image chubby_visit_toned_1_36
                    "... then help yourself to a mouthful of her luscious tits."
                    wt_image chubby_visit_toned_1_37
                    chelsea.c "Aahhh"
                    wt_image chubby_visit_toned_1_38
                    "By the time you pull off her panties, you can smell her arousal."
                    player.c "How long do you think you're going to last?"
                    wt_image chubby_visit_toned_1_24
                    chelsea.c "At what?"
                    wt_image chubby_visit_toned_1_39
                    player.c "At this."
                    wt_image chubby_visit_toned_1_40
                    "She finds herself too busy biting her lip and trying to make the sensation last as long she can to actually answer you ..."
                    wt_image chubby_visit_toned_1_41
                    "... but then, the fluids flowing out of her as nibble, lick and probe along her sex and clit are the only answer you need."
                    wt_image chubby_visit_toned_1_42
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_1_43
                    chelsea.c "That felt great, [chelsea.your_name]!  As I guess you could tell from how long I didn't last."
                    $ chelsea.orgasm_count += 1
                    $ chelsea.pleasure_her_count += 1
                    change player energy by -energy_short notify
                "Tit fuck":
                    wt_image chubby_visit_toned_1_35
                    chelsea.c "Really?  You aren't tired of fucking my tits?"
                    call forced_movement(boudoir) from _call_forced_movement_132
                    summon chelsea no_follows
                    wt_image chubby_visit_toned_1_14
                    player.c "Not really, no."
                    wt_image chubby_visit_toned_1_15
                    "You're not going to get tired of it, either ..."
                    wt_image chubby_visit_toned_1_17
                    "... if she keeps providing your cock this treatment."
                    wt_image chubby_visit_toned_1_18
                    "She seems to be enjoying herself ..."
                    wt_image chubby_visit_toned_1_16
                    "... but you're enjoying her more."
                    wt_image chubby_visit_toned_1_48
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_1_49
                    chelsea.c "I guess you really aren't tired of my tits."
                    $ chelsea.titfuck_count += 1
                    orgasm notify
                "Blow job":
                    wt_image chubby_visit_toned_1_11
                    chelsea.c "A blow job, huh?  I suppose that could be arranged."
                    call forced_movement(boudoir) from _call_forced_movement_146
                    summon chelsea no_follows
                    wt_image chubby_visit_toned_1_30
                    "[chelsea.name]'s arrangement is pretty straight forward."
                    wt_image chubby_visit_toned_1_19
                    "She brings you inside and sits you on the bed ..."
                    wt_image chubby_visit_toned_1_20
                    "... where your cock comes out of your pants ..."
                    wt_image chubby_visit_toned_1_44
                    "... and goes into her mouth."
                    wt_image chubby_visit_toned_1_45
                    "With the careful attention she pays to your member ..."
                    wt_image chubby_visit_toned_1_7
                    "... you're soon ready to arrange something equally straight forward for her."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image chubby_visit_toned_1_8
                            "... a mouthful of sperm for a blow well done."
                            wt_image chubby_visit_toned_1_21
                            player.c "[player.orgasm_text]"
                            wt_image chubby_visit_toned_1_35
                            $ chelsea.swallow_count += 1
                        "On her":
                            wt_image chubby_visit_toned_1_47
                            "... a faceful of sperm for a blow well done."
                            wt_image chubby_cum_face_3
                            player.c "[player.orgasm_text]"
                            $ chelsea.facial_count += 1
                    chelsea.c "Mmmm, I guess I know that was appreciated!"
                    $ chelsea.blowjob_count += 1
                    orgasm notify
                "On her back":
                    call chelsea_spend_time_toned_1_missionary from _call_chelsea_spend_time_toned_1_missionary
                "Doggy style":
                    call forced_movement(boudoir) from _call_forced_movement_165
                    summon chelsea no_follows
                    wt_image chubby_visit_toned_1_30
                    "[chelsea.name] follows you inside to the boudoir ..."
                    wt_image chubby_visit_toned_1_12
                    "... where she lets you bend her over and gasps in pleasure as you enter her."
                    wt_image chubby_visit_toned_1_13
                    chelsea.c "Aahhh"
                    wt_image chubby_visit_toned_1_31
                    "Her gasps intensify as you fuck her ..."
                    wt_image chubby_visit_toned_1_32
                    "... culminating in a noisy orgasm that just precedes your own."
                    wt_image chubby_visit_toned_1_33
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_1_34
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_1_30
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    wt_image chubby_visit_toned_1_30
                    player.c "You look like you've been keeping up with your exercises.  Instead of me fucking you, how about you show off those legs muscles as you fuck me?"
                    wt_image chubby_visit_toned_1_9
                    "[chelsea.name] smiles and happily climbs up on top of you ..."
                    wt_image chubby_visit_toned_1_19
                    "... before removing your pants"
                    wt_image chubby_visit_toned_1_57
                    "Then she spins around to face away from you as she mounts you."
                    wt_image chubby_visit_toned_1_10
                    "She shows off her new fitness level by rising higher ..."
                    wt_image chubby_visit_toned_1_54
                    "... and slamming down harder and faster than she used to be able to do."
                    wt_image chubby_visit_toned_1_55
                    "Up-and-down she goes, up-and-down..."
                    wt_image chubby_visit_toned_1_22
                    "... to the not-so-quiet satisfaction of you both."
                    wt_image chubby_visit_toned_1_56
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_1_54
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_1_30
                    chelsea.c "Thanks for the fun workout, [chelsea.your_name]!"
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_visit_toned_1_29
                    chelsea.c "Really?  I guess I should get comfortable, then."
                    wt_image chubby_visit_toned_1_3
                    "She lifts her leg and pulls up the hem of her dress to give you a clear view of her panties and a clear indication that she'd rather fuck than talk."
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            wt_image chubby_visit_toned_1_29
                            "You spend an enjoyable couple of hours chatting with [chelsea.name]. She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_3
                        "Change your mind and fuck her":
                            call chelsea_spend_time_toned_1_missionary from _call_chelsea_spend_time_toned_1_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            wt_image chubby_visit_toned_1_11
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_3
                        "Ask her to be your girlfriend":
                            wt_image chubby_visit_toned_1_11
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_3
        elif chelsea.visit_outfit == 2:
            wt_image chubby_visit_toned_2_45
            "[chelsea.name] shows up looking amazing.  She's happy with her looks and body and feeling confident - sexually confident."
            wt_image chubby_visit_toned_2_40
            chelsea.c "I don't imagine you called me over here just to talk. So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_2_toned:
                "Tit fuck":
                    wt_image chubby_visit_toned_2_44
                    chelsea.c "Really?  You aren't tired of fucking my tits?"
                    wt_image chubby_visit_toned_2_14
                    player.c "Not really, no."
                    wt_image chubby_visit_toned_2_15
                    "Not while her tits feel this good squeezed around your cock as you fuck them."
                    wt_image chubby_visit_toned_2_3
                    "A point you make quite clearly to [chelsea.name]."
                    wt_image chubby_visit_toned_2_46
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_2_16
                    chelsea.c "Mmmm, I guess you really aren't tired of my tits."
                    $ chelsea.titfuck_count += 1
                    orgasm notify
                "Blow job":
                    wt_image chubby_visit_toned_2_17
                    "You don't say anything.  You just take out your cock and hold it up in front of her."
                    wt_image chubby_visit_toned_2_18
                    "She gets your point, and leans over to give your cock a kiss ..."
                    wt_image chubby_visit_toned_2_19
                    "... before taking you into her mouth ..."
                    wt_image chubby_visit_toned_2_20
                    "... and sucking you off."
                    wt_image chubby_visit_toned_2_5
                    "Soon she gets more than just your point..."
                    wt_image chubby_visit_toned_2_48
                    "... she gets a mouthful of sperm for a blow well done."
                    wt_image chubby_visit_toned_2_49
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_2_47
                    chelsea.c "Mmmm, I guess I know that was appreciated!"
                    $ chelsea.blowjob_count += 1
                    $ chelsea.swallow_count += 1
                    orgasm notify
                "On her back":
                    call chelsea_spend_time_toned_2_missionary from _call_chelsea_spend_time_toned_2_missionary
                "Doggy style":
                    wt_image chubby_visit_toned_2_9
                    player.c "Get out of your clothes and on your knees."
                    wt_image chubby_visit_toned_2_50
                    "She grins at you as she removes her dress ..."
                    wt_image chubby_visit_toned_2_10
                    "... and pulls down her panties."
                    wt_image chubby_visit_toned_2_11
                    chelsea.c "You wanted me like this?"
                    wt_image chubby_visit_toned_2_21
                    player.c "Almost.  Turn around."
                    wt_image chubby_visit_toned_2_58
                    "She gasps as the head of your dick enters her ..."
                    wt_image chubby_visit_toned_2_12
                    chelsea.c "Ahhh"
                    wt_image chubby_visit_toned_2_59
                    ".. and then again, more loudly, as you push yourself inside her."
                    wt_image chubby_visit_toned_2_60
                    chelsea.c "Ahhhhh"
                    wt_image chubby_visit_toned_2_13
                    "Soon you're both being noisy as you fuck the two of you to climax."
                    wt_image chubby_visit_toned_2_6
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_2_57
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_2_42
                    chelsea.c "That was fun, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    wt_image chubby_visit_toned_2_9
                    player.c "I don't want to fuck you.  Considering what good shape you're in these days, I want you to get up here and fuck me."
                    wt_image chubby_visit_toned_2_14
                    "She pulls off her clothes..."
                    wt_image chubby_visit_toned_2_7
                    "... climbs on top of you ..."
                    wt_image chubby_visit_toned_2_22
                    "... and moans as she impales herself on your hard dick."
                    wt_image chubby_visit_toned_2_61
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_toned_2_62
                    "Then she begins to ride you."
                    wt_image chubby_visit_toned_2_23
                    "She must be enjoying this, as she plays with herself ..."
                    wt_image chubby_visit_toned_2_63
                    "... before spinning around ..."
                    wt_image chubby_visit_toned_2_64
                    "... and bouncing up and down on your cock."
                    wt_image chubby_visit_toned_2_8
                    "She shows off her new fitness by riding you faster and faster ..."
                    wt_image chubby_visit_toned_2_24
                    "... until you both cum."
                    wt_image chubby_visit_toned_2_25
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_2_65
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_2_66
                    chelsea.c "Mmmm, that was a fun workout, [chelsea.your_name]."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_visit_toned_2_41
                    chelsea.c "Really?  Well, aren't you full of surprises."
                    "You thought talking to her was a good idea, but it's clear she's ready to spread her legs for you.  All you have to do is ask."
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            wt_image chubby_visit_toned_2_43
                            "You spend an enjoyable couple of hours chatting with [chelsea.name].  She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_4
                        "Change your mind and fuck her":
                            call chelsea_spend_time_toned_2_missionary from _call_chelsea_spend_time_toned_2_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            wt_image chubby_visit_toned_2_37
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_4
                        "Ask her to be your girlfriend":
                            wt_image chubby_visit_toned_2_37
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_4
        elif chelsea.visit_outfit == 3 and chelsea.has_item(lingerie) and chelsea.visit_sex_count >= chelsea.visit_talk_count:
            wt_image chubby_visit_toned_3_1
            "[chelsea.name] bustles past you as she arrives."
            chelsea.c "Don't look!  You'll ruin the surprise."
            wt_image current_location.image
            "It's hard to believe she could be hiding any surprises, considering how little she's wearing, but when she calls out for you to turn around, she's wearing even less."
            wt_image chubby_visit_toned_3_2
            chelsea.c "Okay, [chelsea.your_name], you can look now.  Ta da!"
            wt_image chubby_visit_toned_3_22
            chelsea.c "You were sweet enough to buy me lingerie, so I figured you might want to see me in some.  Not that this is lingerie exactly, it's just a matching bra and panty set, but I thought it looked nice, and shows off the new body I have, thanks to you."
            wt_image chubby_visit_toned_3_3
            chelsea.c "Unless, of course, you'd like me to get rid of the lingerie altogether, and you could just do something with my body?  I don't imagine you called me over here just to talk.  So, how do you want to fuck me?"
            $ title = "What do you tell her?"
            menu chelsea_visit_menu_3_toned:
                "Tit fuck":
                    wt_image chubby_visit_toned_3_30
                    player.c "I want to fuck those big mounds of yours."
                    wt_image chubby_visit_toned_3_31
                    chelsea.c "These mounds?"
                    player.c "Those are the ones."
                    wt_image chubby_seduce_motivated_5
                    "Kneeling in front of you, she gives your cock a playful lick ..."
                    wt_image chubby_visit_toned_3_32
                    "... then wraps her soft boobs around you.  She keeps her eyes on your face as she pumps her breasts up and down your cock, as if seeking confirmation that you're enjoying this."
                    wt_image chubby_seduce_motivated_3
                    "You are, as you demonstrate by depositing a load of hot jizz on her chest."
                    wt_image chubby_cum_tits_6
                    player.c "[player.orgasm_text]"
                    chelsea.c "I guess you liked my outfit."
                    $ chelsea.titfuck_count += 1
                    orgasm notify
                "Blow job":
                    wt_image chubby_visit_toned_3_30
                    player.c "I want you to blow me."
                    wt_image chubby_visit_toned_3_31
                    chelsea.c "Sure, [chelsea.your_name], I'll do that for you.  Consider it a 'thank you' for the lingerie."
                    wt_image chubby_visit_toned_3_7
                    "You take a seat on the sofa beside her and examine her now svelte body as she leans over and gives your cock a kiss."
                    wt_image chubby_visit_toned_3_33
                    "Then she begins the blow job proper, complete with darting tongue dancing up and down your dick, her soft hand caressing your shaft and balls as her warm lips slide up and down with her bobbing head."
                    wt_image chubby_visit_toned_3_8
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image chubby_seduce_motivated_4
                            "You provide the 'you're welcome' to her 'thank you' blowjob in the form of your jizz, spurting into and down the back of throat as she struggles to swallow it all without spilling any."
                            player.c "[player.orgasm_text]"
                            wt_image chubby_visit_toned_3_33
                            chelsea.c "I guess you liked my outfit."
                            $ chelsea.swallow_count += 1
                        "On her":
                            wt_image chubby_cum_tits_9
                            "You provide the 'you're welcome' to her 'thank you' blowjob in the form of your jizz, spurting onto her face and tits."
                            player.c "[player.orgasm_text]"
                            chelsea.c "I guess you liked my outfit."
                            $ chelsea.facial_count += 1
                    $ chelsea.blowjob_count += 1
                    orgasm notify
                "On her back":
                    player.c "You fucking tease, you came here to get your pussy pounded, didn't you?"
                    chelsea.c "Yes"
                    player.c "Get those panties off and show me.  Show me you want my cock inside you."
                    call chelsea_spend_time_toned_3_missionary from _call_chelsea_spend_time_toned_3_missionary
                "Doggy style":
                    wt_image chubby_visit_toned_3_26
                    player.c "You'll look better once you're out of the lingerie and on your hands and knees."
                    wt_image chubby_visit_toned_3_31
                    chelsea.c "Like this?"
                    wt_image chubby_seduce_motivated_2
                    player.c "Almost.  Turn around."
                    wt_image chubby_seduce_motivated_6
                    "She moans as the tip of your dick penetrates her ..."
                    chelsea.c "Ahhhh"
                    wt_image chubby_visit_toned_3_18
                    "... and then again, more loudly, as you fuck her, your cock pistoning in-and-out of her ..."
                    wt_image chubby_visit_toned_3_17
                    "... resulting in orgasms from both of you in quick succession."
                    wt_image chubby_visit_toned_3_34
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_3_18
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_3_31
                    chelsea.c "I'm glad you liked my outfit."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Cowgirl":
                    wt_image chubby_visit_toned_3_26
                    player.c "How about you climb up here and show me how well you can fuck me?"
                    wt_image chubby_visit_toned_3_19
                    "Stripping quickly out of her remaining clothes, she crawls into your lap and slides down onto your hard cock."
                    wt_image chubby_visit_toned_3_35
                    "She moans as you lick and suckle her breast ..."
                    wt_image chubby_visit_toned_3_20
                    chelsea.c "Ahhhh"
                    wt_image chubby_seduce_motivated_8
                    "... then turns around to her preferred reverse cowgirl position."
                    wt_image chubby_visit_toned_3_36
                    "There she rides you, showing off her newfound fitness by bouncing up and down, faster and faster on your hard cock."
                    wt_image chubby_visit_toned_3_37
                    "Her warm, wet pussy sliding up and down your dick feels incredibly good and soon triggers your climax.  [chelsea.name] gasps as she feels you let go inside her."
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_3_21
                    "[chelsea.name]'s not far behind you.  She may even have been waiting for you to finish.  Your hard cock still pumping semen inside her, she falls forward and rubs herself between her legs, pushing her over the edge."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_visit_toned_3_31
                    chelsea.c "I'm glad you liked my outfit."
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                "Actually, I do want to talk":
                    wt_image chubby_visit_toned_3_4
                    chelsea.c "Really?  I'm dressed like this and you just want to talk?"
                    wt_image chubby_visit_toned_3_23
                    chelsea.c "Guess I better make myself comfortable."
                    wt_image chubby_seduce_motivated_1
                    "She pulls off her top and settles down across from you, a twinkle in her eye.  She's ready to chat with you, but it's clear she'd rather spread her legs for you."
                    $ title = "What do you want to do?"
                    menu:
                        "Just talk":
                            "You spend an enjoyable couple of hours chatting with [chelsea.name]. She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                            add tags 'talked' to chelsea
                            change player energy by -energy_short notify
                        "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                            add tags 'trigger_invoked_this_visit' to chelsea
                            call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_5
                        "Change your mind and fuck her":
                            player.c "You fucking tease, you came here to get your pussy pounded, didn't you?"
                            wt_image chubby_visit_toned_3_25
                            chelsea.c "Yes"
                            wt_image chubby_visit_toned_3_26
                            player.c "Get those panties off and show me.  Show me you want my cock inside you."
                            call chelsea_spend_time_toned_3_missionary from _call_chelsea_spend_time_toned_3_missionary_1
                        "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                            wt_image chubby_visit_toned_3_4
                            call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_5
                        "Ask her to be your girlfriend":
                            wt_image chubby_visit_toned_3_4
                            call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_5
    if chelsea.has_tag('talked'):
        rem tags 'talked' from chelsea
        $ chelsea.visit_talk_count += 1
    else:
        $ chelsea.visit_sex_count += 1
    if chelsea.has_tag('trigger_invoked_this_visit'):
        rem tags 'trigger_invoked_this_visit' from chelsea
    if not chelsea.has_tag('girlfriend') and not chelsea.has_tag('hypno_girlfriend'):
        call chelsea_continuing_actions_end_of_visit from _call_chelsea_continuing_actions_end_of_visit_2
    return

label chelsea_spend_time_bbw_1_missionary:
    wt_image chubby_visit_bbw_1_13
    player.c "I'm going to stick my hard cock into your hot, wet pussy."
    chelsea.c "Whoa, [chelsea.your_name].  Do you think I'm wet already?"
    player.c "Yes, I do.  I think you came here hoping I'd put my hard dick inside you and your pussy is ready and waiting for a hard poking."
    wt_image chubby_visit_bbw_1_14
    "She gasps as you kiss her breast and run your fingers along her sex, the dampness soaking through her panties proving that if she wasn't ready when she came over, she is now."
    chelsea.c "Ahhhhh"
    wt_image chubby_visit_bbw_1_15
    player.c "Still want me to 'whoa'?"
    chelsea.c "No"
    player.c "What do you want?"
    chelsea.c "I want you to fuck me."
    wt_image chubby_visit_bbw_1_27
    "Holding her legs wide open, she moans as you begin to do just that, sliding first the tip of your cock ..."
    chelsea.c "Ahhhhh"
    wt_image chubby_visit_bbw_1_28
    "... then your whole cock inside."
    chelsea.c "Ahhhh"
    wt_image chubby_visit_bbw_1_17
    "Soon there's more than just your cock inside her, as the two of you climax at almost the same time."
    wt_image chubby_visit_bbw_1_18
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_bbw_1_16
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_bbw_1_6
    chelsea.c "That was fun, [chelsea.your_name]."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_spend_time_bbw_2_missionary:
    wt_image chubby_visit_bbw_2_44
    "Pulling off her panties, she lays back and opens herself for you."
    wt_image chubby_visit_bbw_2_12
    chelsea.c "Yup, [chelsea.your_name].  My pussy's ready to fuck, too."
    wt_image chubby_visit_bbw_2_13
    "She's right.  You enter her easily ..."
    wt_image chubby_visit_bbw_2_14
    chelsea.c "Ahhh"
    wt_image chubby_visit_bbw_2_45
    "... and almost as easily, quickly fuck both you and her to climax."
    wt_image chubby_visit_bbw_2_46
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_bbw_2_43
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_bbw_2_35
    chelsea.c "That was fun, [chelsea.your_name]."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_spend_time_bbw_3_missionary:
    wt_image chubby_gf_bbw_2_19
    "She spreads her legs as you push her back onto the sofa.  Her pussy is wet and waiting for you, and she moans as you shove yourself into her."
    chelsea.c "Ahhhh"
    wt_image chubby_gf_bbw_2_20
    "Her moans get louder and she clutches her tits as you fuck her ..."
    chelsea.c "Ahhhh  ... Ahhhhh"
    wt_image chubby_gf_bbw_2_21
    "... then she reaches between her legs and frigs herself to climax right before you reach yours."
    chelsea.c "Aahhhhhh"
    wt_image chubby_gf_bbw_2_30
    player.c "[player.orgasm_text]"
    wt_image chubby_gf_bbw_2_10
    chelsea.c "That was fun, [chelsea.your_name]."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_visit_bbw_4_missionary:
    player.c "Which of these tables do you normally eat at?"
    wt_image chubby_visit_bbw_4_10
    chelsea.c "This one.  Why?"
    player.c "I didn't want to fuck you on the wrong table. You are ready for me to lean you over your lunchroom table and fuck your brains out, aren't you?"
    wt_image chubby_visit_bbw_4_20
    chelsea.c "Yes"
    player.c "Show me."
    wt_image chubby_visit_bbw_4_22
    "She lifts her skirt and pulls aside her panties, revealing a pussy that is indeed wet and ready for you."
    wt_image chubby_visit_bbw_4_23
    "She moans as you push yourself inside her ..."
    chelsea.c "Ahhhh"
    wt_image chubby_visit_bbw_4_24
    "... and plays with her own nipples as you fuck her."
    wt_image chubby_visit_bbw_4_32
    chelsea.c "Ahhhh"
    wt_image chubby_visit_bbw_4_33
    "Just before you're ready to cum, she wets her fingers and reaches down between her legs ..."
    wt_image chubby_visit_bbw_4_34
    "... and frigs herself to climax a moment before you reach yours."
    wt_image chubby_visit_bbw_4_25
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_bbw_4_38
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_bbw_4_3
    chelsea.c "Thanks for the fun break!  I need to get back to work, now."
    "You leave her and get on with your day."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_spend_time_toned_1_missionary:
    call forced_movement(boudoir) from _call_forced_movement_166
    summon chelsea no_follows
    wt_image chubby_visit_toned_1_30
    player.c "You want my hard dick in you that bad, get in here and get your legs up."
    wt_image chubby_visit_toned_1_38
    chelsea.c "Whoa, [chelsea.your_name].  Do you think I'm ready that quickly?"
    wt_image chubby_visit_toned_1_23
    player.c "Yes, I do. I think you came here hoping for a hard poke, and you've been getting wet thinking about it on your drive over."
    wt_image chubby_visit_toned_1_24
    "She grins as you run your fingers along her sex, the dampness proving that if she wasn't ready when she came over, she is now."
    wt_image chubby_visit_toned_1_25
    "When you put the head of your dick into her she moans ..."
    wt_image chubby_visit_toned_1_26
    chelsea.c "Aahhhh"
    wt_image chubby_visit_toned_1_50
    "... then again, louder, as you bury yourself fully inside her."
    wt_image chubby_visit_toned_1_51
    chelsea.c "Aahhhhh"
    wt_image chubby_visit_toned_1_27
    "Soon you're both being loud, as you fuck the two of you to climax."
    wt_image chubby_visit_toned_1_52
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_toned_1_51
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_toned_1_53
    chelsea.c "That was fun, [chelsea.your_name]."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_spend_time_toned_2_missionary:
    player.c "You look good in that dress, but you'll look better without it."
    wt_image chubby_visit_toned_2_9
    chelsea.c "Really?  I guess I should get it off, then."
    wt_image chubby_visit_toned_2_50
    "Stripping quickly, she strikes a seductive pose for you."
    wt_image chubby_visit_toned_2_26
    chelsea.c "Is this better?"
    wt_image chubby_visit_toned_2_27
    player.c "It will be once you spread your legs."
    wt_image chubby_visit_toned_2_52
    "It seems she's been looking forward to this, as she's already wet and moans as you enter her."
    wt_image chubby_visit_toned_2_51
    chelsea.c "Ahhhhh"
    wt_image chubby_visit_toned_2_53
    "Reaching down between her legs, she rubs her clit while you fuck her ..."
    wt_image chubby_visit_toned_2_54
    "... bringing herself to a noisy climax just before you reach yours."
    wt_image chubby_visit_toned_2_55
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_toned_2_56
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_toned_2_42
    chelsea.c "That was fun, [chelsea.your_name]."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_spend_time_toned_3_missionary:
    wt_image chubby_visit_toned_3_12
    "She pulls the panties off and spreads her legs, her wetness obvious even from a distance."
    wt_image chubby_visit_toned_3_27
    "You push her backwards onto the sofa and she lifts her leg to give you easy access, moaning as you push the tip of your dick inside her ..."
    wt_image chubby_visit_toned_3_13
    chelsea.c "Ahhhh"
    wt_image chubby_visit_toned_3_14
    "... then moaning louder as you pump in and out of her."
    chelsea.c "Ahhhhh"
    wt_image chubby_visit_toned_3_15
    "Gripping her firmly by the tit, you fuck her faster and faster, harder and deeper on each stroke ..."
    wt_image chubby_visit_toned_3_16
    "... until both of you explode, one after the other."
    wt_image chubby_seduce_motivated_7
    chelsea.c "Aahhhhhh"
    wt_image chubby_visit_toned_3_28
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_toned_3_29
    chelsea.c "I'm glad you liked my outfit."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

label chelsea_visit_toned_4_pile_driver:
    wt_image chubby_visit_toned_4_2
    player.c "You know what?  You could use a quick distraction from work.  I'm going to pile drive you."
    chelsea.c "You're going to what??"
    wt_image chubby_visit_toned_4_15
    player.c "Come here and lie down on the floor and I'll show you."
    wt_image chubby_visit_toned_4_16
    "As she lies down, you lift her hips until her feet fall back over her head. Then you push yourself into her as she moans."
    chelsea.c "Ahhhh"
    wt_image chubby_visit_toned_4_17
    "It's a vulnerable, helpless position, and as you pound into her, it feels like you might split her in half."
    chelsea.c "Ahhhh"
    wt_image chubby_visit_toned_4_18
    "Despite that, she responds well to the fucking, and as you stroke your hand along her open and exposed sex, she moans even louder ..."
    chelsea.c "Ahhhhh"
    wt_image chubby_visit_toned_4_19
    "... before shuddering to a climax just a moment before you do."
    wt_image chubby_visit_toned_4_17
    chelsea.c "Aahhhhhh"
    player.c "[player.orgasm_text]"
    wt_image chubby_visit_toned_4_30
    chelsea.c "Thanks for the fun experience!  I need to get back to work, now."
    "You leave her and get on with your day."
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    orgasm notify
    return

# # Post-Training Dismissal
# label chelsea_dismiss:
#     add tags 'trained_this_week' to chelsea
#     "You change your mind and send her home."
#     call character_location_return(chelsea)
#     wt_image current_location.image
#     return

# Girlfriend Actions
label chelsea_girlfriend_actions:
  $ chelsea.temporary_count = 1 # tracks whether you spend time with her
  $ chelsea.gf_outfit += 1
  if chelsea.gf_outfit >= 9:
    $ chelsea.gf_outfit = 1
  if chelsea.gf_outfit == 1:
    # bj lesson
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_bj_1_1
      "[chelsea.name] seems happy to see you."
      chelsea.c "Hi!  You're just in time to help me with my homework."
      player.c "You have homework?"
      wt_image chubby_gf_bj_1_20
      chelsea.c "Uh huh.  I was told that a big girl should be good at pleasing her boyfriend with her mouth, so I had better learn how to do that.  Can I practice on you?"
      $ title = "What do you tell her?"
      menu:
        "Kneel in front of me":
          wt_image chubby_gf_bj_1_2
          player.c "Okay, [chelsea.name].  You can practice on me.  Kneel in front of me."
          wt_image chubby_gf_bj_1_23
          chelsea.c "Thanks!  I hope I do a good job."
          wt_image chubby_gf_bj_1_3
          "[chelsea.name] takes your cock in her hand ..."
          wt_image chubby_gf_bj_1_4
          "... licks the tip of it ..."
          wt_image chubby_gf_bj_1_5
          "... then slides her lips along the side."
          $ title = "What do you want her to do?"
          menu:
            "Put it between her breasts":
              wt_image chubby_gf_bj_1_24
              player.c "Put my cock between your tits, [chelsea.name]."
              wt_image chubby_gf_bj_1_6
              chelsea.c "Like this?"
              player.c "Yes, now rub your boobs up and down over it."
              wt_image chubby_gf_bj_1_7
              chelsea.c "This won't teach me how to please a boy with my mouth."
              player.c "It'll still please him."
              wt_image chubby_gf_bj_1_25
              "Just how much it will please a boy, you soon demonstrate."
              wt_image chubby_cum_tits_2
              player.c "[player.orgasm_text]"
              chelsea.c "Oh!  I guess that was good practice."
              $ chelsea.titfuck_count += 1
            "Suck it":
              wt_image chubby_gf_bj_1_24
              player.c "That's enough teasing, [chelsea.name]. Put my cock in your mouth and start sucking."
              wt_image chubby_gf_bj_1_8
              "She wraps her lips around the head of your cock ..."
              wt_image chubby_gf_bj_1_26
              "... and bobs her head up and down, your cock sliding back and forth between her soft lips until you're ready to cum."
              wt_image chubby_gf_bj_1_27
              $ title = "Where do you want to cum?"
              menu:
                "In her":
                  wt_image chubby_gf_bj_1_9
                  player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
                  chelsea.c "nnnnn nnn"
                  "You think that was 'thank you', but it's hard to make her out with her mouth full of jizz and cock."
                  $ chelsea.swallow_count += 1
                "On her":
                  wt_image chubby_gf_bj_1_28
                  player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
                  wt_image chubby_gf_bj_1_29
                  chelsea.c "Thanks!  I like it when you let me practice with you."
                  $ chelsea.facial_count += 1
              $ chelsea.blowjob_count += 1
          orgasm notify
        "Kneel on that foot stool":
          wt_image chubby_gf_bj_1_2
          player.c "Okay, [chelsea.name].  You can practice on me.  Get on that foot stool."
          wt_image chubby_gf_bj_1_23
          chelsea.c "Thanks!  I hope I do a good job."
          wt_image chubby_gf_bj_1_10
          chelsea.c "Did you want me like this?"
          player.c "No, get on your hands and knees."
          wt_image chubby_gf_bj_1_11
          "As she gets into position, you place your dick in front of her face.  You don't have to explain what to do next.  She opens her mouth and wraps her lips around the head of your cock ..."
          wt_image chubby_gf_bj_1_30
          "... and sucks you off as best she can in this position ..."
          wt_image chubby_gf_bj_1_12
          "... while you enjoy the view."
          wt_image chubby_gf_bj_1_13
          "This is more about her letting you fuck her face than it is her giving a blow job, but it's none-the-less pleasurable for that."
          wt_image chubby_gf_bj_1_31
          $ title = "Where do you want to cum?"
          menu:
            "In her":
              wt_image chubby_gf_bj_1_32
              player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
              chelsea.c "nnnnn nnn"
              "You think that was 'thank you', but it's hard to make her out with her mouth full of jizz and cock."
              $ chelsea.swallow_count += 1
            "On her":
              wt_image chubby_gf_bj_1_33
              player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
              wt_image chubby_gf_bj_1_34
              chelsea.c "Thanks!  I like it when you let me practice with you."
              $ chelsea.facial_count += 1
          $ chelsea.blowjob_count += 1
          orgasm notify
        "Lie down on that foot stool":
          wt_image chubby_gf_bj_1_2
          player.c "Okay, [chelsea.name].  You can practice on me.  Get on that foot stool."
          wt_image chubby_gf_bj_1_23
          chelsea.c "Thanks!  I hope I do a good job."
          wt_image chubby_gf_bj_1_10
          player.c "Not like that. Roll over on your back."
          wt_image chubby_gf_bj_1_35
          "As she gets into position, you straddle her chest, placing your dick in front of her face. You don't have to explain what to do next. She takes your cock in her hand and licks the head ..."
          wt_image chubby_gf_bj_1_15
          "... swirling her tongue around and around it."
          $ title = "What do you want her to do?"
          menu:
            "Suck it":
              wt_image chubby_gf_bj_1_14
              player.c "That's enough teasing, [chelsea.name].  Put my cock in your mouth and start sucking."
              wt_image chubby_gf_bj_1_17
              "She wraps her lips around the head of your cock ..."
            "Lick your balls":
              wt_image chubby_gf_bj_1_14
              player.c "Lick my balls, too, [chelsea.name].  Then take them in your mouth and suckle them."
              chelsea.c "Do boys like it when girls do that?"
              wt_image chubby_gf_bj_1_16
              player.c "This boy does."
              "You have her suckle your balls until they need relief ..."
              wt_image chubby_gf_bj_1_17
              "... then direct your cock back to her mouth.  She wraps her lips around the head ..."
          wt_image chubby_gf_bj_1_18
          "... and bobs her head up and down as best she can in this position, your cock sliding back and forth between her soft lips until you're ready to cum."
          wt_image chubby_gf_bj_1_36
          $ title = "Where do you want to cum?"
          menu:
            "In her":
              wt_image chubby_gf_bj_1_19
              player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
              chelsea.c "nnnnn nnn"
              "You think that was 'thank you', but it's hard to make her out with her mouth full of jizz and cock."
              $ chelsea.swallow_count += 1
            "On her":
              wt_image chubby_cum_tits_8
              player.c "[player.orgasm_text] ... That's enough homework for today, [chelsea.name].  Keep practicing what you learned and you'll do great pleasing boys with your mouth."
              chelsea.c "Thanks!  I like it when you let me practice with you."
              $ chelsea.facial_count += 1
          $ chelsea.blowjob_count += 1
          $ chelsea.swallow_count += 1
          orgasm notify
        "Not today":
          wt_image chubby_gf_bj_1_22
          player.c "Not today, [chelsea.name]. You don't need the practice anyway."
          wt_image chubby_gf_bj_1_21
          chelsea.c "I don't?  Thanks!  Still, I hope I get to practice on you soon, anyway.  Just so I don't forget how."
          $ chelsea.visit_count -= 1 # to offset gain, later
    else:
      # sofa
      if chelsea.has_tag('bbw'):
        call forced_movement(living_room) from _call_forced_movement_167
        summon chelsea no_follows
        wt_image chubby_gf_bbw_4_1
        "You find [chelsea.name] sitting on the sofa, watching TV. She greets you with a big kiss as you sit down beside her."
        wt_image chubby_gf_bbw_4_14
        chelsea.c "Did you want to watch TV with me, or did you have something else in mind?"
        $ title = "What do you have in mind?"
        menu:
          "Just watch TV":
            wt_image chubby_gf_bbw_4_2
            "The two of you snuggle up together on the sofa. The show is terrible, but you help keep the two of you amused by playing with [chelsea.name]'s nipple through her dress and keeping it erect the whole time the show is running."
            change player energy by -energy_very_short notify
          "Blow job":
            wt_image chubby_gf_bbw_4_15
            "She pulls open the top of her dress, exposing her massive boobs, and drops to her knees in front of you.  She starts pleasuring your dick, but keeps an eye on her show as she does so."
            $ title = "What do you want?"
            menu:
              "Tell her to get naked":
                wt_image chubby_gf_bbw_4_20
                "She strips, then goes back to sucking you off while watching her show."
                $ title = "What now?"
                menu:
                  "Tell her to pay attention to your balls":
                    wt_image chubby_gf_bbw_4_22
                    player.c "Pay attention to my balls, [chelsea.name]."
                    wt_image chubby_gf_bbw_4_23
                    player.c "My balls, [chelsea.name], not the television."
                    wt_image chubby_gf_bbw_4_24
                    chelsea.c "Sorry, [chelsea.your_name]."
                    wt_image chubby_gf_bbw_4_25
                    "She suckles your sack with enthusiasm, a sensation that feels great ..."
                    wt_image chubby_gf_bbw_4_21
                    "... and which not at all coincidentally gets you off quickly when she puts your cock back in her mouth, before she misses much of her show."
                    wt_image chubby_gf_bbw_4_27
                  "This is fine":
                    wt_image chubby_gf_bbw_4_26
                    "It's kind of cute, watching [chelsea.name] pleasure you while also watching her show."
                    wt_image chubby_gf_bbw_4_21
                    "She's a bit distracted, but not so much that can't enjoy the sensation of her lips and tongue on you."
                    wt_image chubby_gf_bbw_4_27
                    "And she definitely pays attention when you fill her mouth with jizz."
              "Tell her to pay attention to you":
                wt_image chubby_gf_bbw_4_18
                chelsea.c "Sorry, [chelsea.your_name].  I'll give you my undivided attention."
                wt_image chubby_gf_bbw_4_19
                "She does so with an intense and vigorous blow job ..."
                wt_image chubby_gf_bbw_4_17
                "... which not at all coincidentally gets you off before she misses much of her show."
              "This is fine":
                wt_image chubby_gf_bbw_4_16
                "It's kind of cute, watching [chelsea.name] pleasure you while also watching her show.  She's a bit distracted, but not so much that can't enjoy the sensation of her lips and tongue on you."
                wt_image chubby_gf_bbw_4_17
                "And she definitely pays attention when you fill her mouth with jizz."
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_bbw_4_3
            "You got what you came here for.  You leave her to finish her show - after she finishes swallowing your load - and go on with your day."
            $ chelsea.blowjob_count += 1
            $ chelsea.swallow_count += 1
            orgasm notify
          "Tit job":
            wt_image chubby_gf_bbw_4_28
            player.c "I was hoping to fuck your tits."
            wt_image chubby_gf_bbw_4_5
            "[chelsea.name] lies down on the floor and you straddle her chest, burying your cock between her soft mounds."
            wt_image chubby_gf_bbw_4_4
            "As you fuck her chest, [chelsea.name] pays as much attention, if not more, to her show as she does to you pleasuring yourself with her body ..."
            wt_image chubby_gf_bbw_4_29
            "... but you don't really need her attention to enjoy the sensation of sliding your dick back and forth in her soft valley.  At least, not until you have a reason to want her to look at you."
            wt_image chubby_gf_bbw_4_30
            player.c "[chelsea.name]"
            wt_image chubby_gf_bbw_4_5
            chelsea.c "Hmmm?  What is it?"
            wt_image chubby_gf_bbw_4_31
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_bbw_4_32
            player.c "I didn't want you to miss the climactic ending."
            wt_image chubby_gf_bbw_4_6
            "She giggles and licks up the sperm she can reach. The rest she'll clean off later, after her show ends."
            $ chelsea.titfuck_count += 1
            $ chelsea.facial_count += 1
            orgasm notify
          "Cowgirl":
            wt_image chubby_gf_bbw_4_7
            player.c "I want you to climb up on me and ride my hard cock."
            "You pull down the front of her dress and use your mouth on her nipples to warm her up."
            wt_image chubby_gf_bbw_4_8
            "When her body's ready for you, you guide her onto your cock.  She faces away from you as you enter her."
            wt_image chubby_gf_bbw_4_33
            chelsea.c "Ahhhh"
            wt_image chubby_gf_bbw_4_34
            "This is her preferred orientation at any time, but today you suspect she's also taking advantage of facing towards the TV to keep watching her show, not that you can tell for certain from behind her."
            wt_image chubby_gf_bbw_4_9
            "It doesn't matter, anyway. The feel of her body bouncing up and down on your hard cock soon brings you to orgasm."
            wt_image chubby_gf_bbw_4_35
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_bbw_4_33
            "And if she is watching her show, it doesn't distract her from reaching her own climax, just a moment after you reach yours."
            wt_image chubby_gf_bbw_4_36
            chelsea.c "Aahhhhhh"
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
          "From behind":
            wt_image chubby_gf_bbw_4_7
            "You pull down the front of her dress and use your mouth on her nipples to warm her up."
            wt_image chubby_gf_bbw_4_37
            "Once her body's ready for you, you turn her around and push yourself into her warm, waiting cunt."
            chelsea.c "Ahhhh"
            wt_image chubby_gf_bbw_4_10
            "She seems to be as interested in watching her show on TV as she is in the sex."
            wt_image chubby_gf_bbw_4_11
            "Not that it matters.  Her pussy still feels great as you fuck her ..."
            wt_image chubby_gf_bbw_4_38
            "... and she still cums as you pound into her, just a moment before you reach your own orgasm."
            wt_image chubby_gf_bbw_4_39
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_bbw_4_40
            player.c "[player.orgasm_text]"
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
          "On her back":
            wt_image chubby_gf_bbw_4_7
            "You pull down the front of her dress and use your mouth on her nipples to warm her up."
            wt_image chubby_gf_bbw_4_41
            "Once her body's ready for you, you lay her on the floor and push yourself into her warm, waiting cunt."
            chelsea.c "Ahhhh"
            wt_image chubby_gf_bbw_4_42
            "As you fuck her, you catch her sneaking glances at the TV, to keep up with what's going o with her show."
            $ title = "What do you want?"
            menu:
              "Get her attention":
                wt_image chubby_gf_bbw_4_12
                "Hooking your fingers into her mouth, you turn her head back towards you."
                wt_image chubby_gf_bbw_4_45
                player.c "Hey, I'm fucking you here.  Are you paying attention?"
                wt_image chubby_gf_bbw_4_13
                "She nods her head vigorously ..."
                wt_image chubby_gf_bbw_4_46
                "... and promptly cums while sucking on your finger as you fuck her ..."
                chelsea.c "Mmhhhhhh"
                wt_image chubby_gf_bbw_4_47
                "... triggering an orgasm for you, too."
              "This is fine":
                wt_image chubby_gf_bbw_4_43
                "Who cares if she's watching her show?  Her naked body's still sexy and her pussy still feels great ..."
                wt_image chubby_gf_bbw_4_44
                "... and she still cums as you pound into her, just a moment before you reach your own orgasm."
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_bbw_4_41
            player.c "[player.orgasm_text]"
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
        call character_location_return(chelsea) from _call_character_location_return_32
      # pool or dominate
      elif chelsea.has_tag('toned'):
        call forced_movement(living_room) from _call_forced_movement_168
        summon chelsea no_follows
        wt_image chubby_gf_pool_1_toned_10
        "You spot [chelsea.name] just as she's heading outside."
        chelsea.c "I'm about to go for a swim.  Want to join me?"
        $ title = "Go with her?"
        menu:
          "Tag along":
            call forced_movement(backyard) from _call_forced_movement_171
            summon chelsea no_follows
            wt_image chubby_gf_pool_1_toned_12
            "You go along with her and watch as she swims laps."
            chelsea.c "Are you going to join me?"
            player.c "I'm fine here."
            wt_image chubby_gf_pool_1_toned_14
            "When she's finished her workout, she pulls herself out of the water and wraps a towel around herself to dry off."
            wt_image chubby_gf_pool_1_toned_16
            chelsea.c "I should get going.  I only have a few minutes left before I need to go to work."
            $ title = "What do you want?"
            menu:
              "Fuck her from the front":
                wt_image chubby_gf_pool_1_toned_15
                player.c "Watching you swimming in that bikini has me turned on. I want to fuck you."
                chelsea.c "I don't have a lot of time."
                wt_image chubby_gf_pool_1_toned_17
                "Your lips at her ear and a hand down the front of her bikini bottoms forestalls any further objections.  She grasps your hard cock in her hand as you whisper to her."
                player.c "I can be fast.  Can you?"
                wt_image chubby_gf_pool_1_toned_18
                chelsea.c "Oh!  I think so."
                wt_image chubby_gf_pool_1_toned_20
                "She lets you guide her backwards and remove her bikini."
                wt_image chubby_gf_pool_1_toned_21
                "She's already wet and moans as you penetrate her."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_pool_1_toned_22
                player.c "You want this fast. Do you want it hard, too?"
                chelsea.c "Oh!!  Yes!"
                wt_image chubby_gf_pool_1_toned_23
                "You pound into her, her hair and tits bouncing back and forth as you fuck her."
                wt_image chubby_gf_pool_1_toned_24
                "You're a little rough, but it doesn't keep her from cumming quickly.  Or you, either."
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_pool_1_toned_25
                player.c "[player.orgasm_text]"
                wt_image chubby_gf_pool_1_toned_26
                "You send her off to work, tired and happy after her double work out."
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Fuck her from behind":
                wt_image chubby_gf_pool_1_toned_15
                player.c "Watching you swimming in that bikini has me turned on. I want to fuck you."
                chelsea.c "I don't have a lot of time."
                wt_image chubby_gf_pool_1_toned_17
                "Your lips at her ear and a hand down the front of her bikini bottoms forestalls any further objections.  She grasps your hard cock in her hand as you whisper to her."
                player.c "I can be fast.  Can you?"
                wt_image chubby_gf_pool_1_toned_18
                chelsea.c "Oh!  I think so."
                wt_image chubby_gf_pool_1_toned_19
                "Turn her around, you pull off her bikini and bend her over."
                wt_image chubby_gf_pool_1_toned_27
                "She's already wet and moans as you enter her."
                wt_image chubby_gf_pool_1_toned_28
                chelsea.c "Ahhhh"
                wt_image chubby_gf_pool_1_toned_29
                player.c "You want this fast.  Do you want it hard, too?"
                chelsea.c "Oh!!  Yes!"
                wt_image chubby_gf_pool_1_toned_30
                "You pound into her, her hair and tits bouncing back and forth as you fuck her.  You're a little rough, but it doesn't keep her from cumming quickly.  Or you, either."
                wt_image chubby_gf_pool_1_toned_31
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_pool_1_toned_32
                player.c "[player.orgasm_text]"
                wt_image chubby_gf_pool_1_toned_33
                "You send her off to work, tired and happy after her double work out."
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Hanging out with her was enough":
                player.c "Hanging out with you was fun."
                wt_image chubby_gf_pool_1_toned_15
                chelsea.c "Thanks!  I like spending time with you, too, [chelsea.your_name]."
                change player energy by -energy_short notify
            call forced_movement(living_room) from _call_forced_movement_172
          "Not today":
            player.c "Not today.  Why don't you stay here and we'll spend some time together?"
            wt_image chubby_gf_pool_1_toned_1
            chelsea.c "I need to get some exercise in. I've been putting on weight again."
            player.c "I can think of some work outs we can do together."
            "She laughs."
            wt_image chubby_gf_pool_1_toned_10
            chelsea.c "I'll take you up on that some other time. I really need to get some laps in today."
            $ title = "What do you want?"
            menu:
              "Use her trigger" if chelsea.has_tag('trigger_implanted'):
                player.c "Don't be silly. You're not going anywhere. Squat down."
                wt_image chubby_gf_pool_1_toned_1
                chelsea.c "What?"
                player.c "You heard me. [chelsea.trigger_phrase], [chelsea.name]. Lower yourself."
                wt_image chubby_gf_pool_1_toned_34
                player.c "Eyes down."
                wt_image chubby_gf_pool_1_toned_35
                $ title = "What now?"
                menu:
                  "Have her blow you":
                    player.c "Since you're down there, suck my cock."
                    wt_image chubby_gf_pool_1_toned_36
                    "The hypnotized woman wraps her lips around the head of your cock and starts sucking you."
                    wt_image chubby_gf_pool_1_toned_37
                    "She doesn't stop sucking you, not even as you blow your load into her mouth."
                    wt_image chubby_gf_pool_1_toned_38
                    player.c "[player.orgasm_text]"
                    "She keeps on sucking your dick until you tell her to stop, which you don't do until she's extracted every drop of semen pulsing from your balls."
                    $ chelsea.hypno_blowjob_count += 1
                    $ chelsea.hypno_swallow_count += 1
                    $ chelsea.visit_count -= 1
                    orgasm notify
                  "Leave her there":
                    "You can't leave her there too long. She has work later today. But for the moment it amuses you to see your independent minded girlfriend squatting mindlessly, simply because you told her to, and haven't yet told her she can get up."
                    $ chelsea.visit_count -= 1 # to offset gain, later
              "Dominate her" if chelsea.dominate_status == 8:
                player.c "I said I wanted you here, fucktoy. Get on your knees and suck my cock."
                wt_image chubby_gf_pool_1_toned_1
                chelsea.c "But ..."
                player.c "No 'buts'. Wrap your mouth around my dick, fucktoy. And pull down your top while you're at it. I want to see your titties while you suck me."
                wt_image chubby_gf_pool_1_toned_39
                "She decides not to push you any further. Freeing her breasts from her top, she kneels in front of you and takes your cock into her mouth."
                wt_image chubby_gf_pool_1_toned_40
                "Wrapping her hair around your hand, you pull her head back and forth along your cock, controlling the pace of the blow job as she struggles to keep up with you."
                player.c "Deeper, fucktoy.  Suck my cock like you mean it."
                wt_image chubby_gf_pool_1_toned_41
                player.c "You're not going to gag, are you fucktoy?"
                "She shakes her head 'no' as you push your cock as far down her throat as you can."
                $ title = "Where do you want to cum?"
                menu:
                  "In her":
                    wt_image chubby_gf_pool_1_toned_38
                    player.c "See that you don't ... [player.orgasm_text]"
                    wt_image chubby_gf_pool_1_toned_42
                    $ chelsea.swallow_count += 1
                  "On her":
                    wt_image chubby_gf_pool_1_toned_43
                    "Pulling her head off your cock, you unload onto her face."
                    player.c "Let's not take any chances ... [player.orgasm_text]"
                    wt_image chubby_gf_pool_1_toned_44
                    $ chelsea.facial_count += 1
                player.c "That's better. If you want to go for a swim now, fucktoy, you can."
                chelsea.c "I'm not sure I still have time before work?"
                player.c "Well, at least you looked after the important things, first."
                "She doesn't like that you put your needs ahead of hers, but as long as she enjoys the rest of your relationship enough, she'll put up with it when you get in these moods."
                $ chelsea.blowjob_count += 1
                $ chelsea.visit_count -= 1 # to offset relationship gain from auto-visit count
                orgasm notify
              "Let her go":
                player.c "Have fun."
                wt_image chubby_gf_pool_1_toned_1
                chelsea.c "You, too!"
                $ chelsea.visit_count -= 1 # to offset gain, later
        call character_location_return(chelsea) from _call_character_location_return_33
  # CANCELLED date night - moved to separate action on its own
  if chelsea.gf_outfit == 2:
    $ chelsea.gf_outfit += 1
  # displaying herself and ass fingering options
  if chelsea.gf_outfit == 3:
    call forced_movement(living_room) from _call_forced_movement_214
    summon chelsea no_follows
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_youth_3_2
      "You find [chelsea.name] crossing the house in flip-flops and a pair of very short shorts."
      chelsea.c "Hi. I'm about to go to work. I was just on my way to the kitchen to pack a lunch before I change into my 'pretend to be an adult' work clothes."
      $ title = "What do you tell her?"
      menu:
        "You look hot":
          wt_image chubby_gf_youth_3_4
          chelsea.c "Thank you, [chelsea.your_name]!"
          $ title = "What else do you tell her?"
          menu:
            "Take off the shorts":
                call chelsea_gf_action_3_youth_take_off_shorts from _call_chelsea_gf_action_3_youth_take_off_shorts
            "Get to work":
              call chelsea_gf_action_3_youth_get_to_work from _call_chelsea_gf_action_3_youth_get_to_work
        "Those are very short shorts":
          wt_image chubby_gf_youth_3_4
          player.c "Those are very short shorts, young lady."
          wt_image chubby_gf_youth_3_3
          chelsea.c "I know!  Do they turn you on, [chelsea.your_name]?"
          $ title = "What do you tell her?"
          menu:
            "Yes, you look hot":
              wt_image chubby_gf_youth_3_4
              chelsea.c "Thank you!"
              $ title = "What else do you tell her?"
              menu:
                "Take off the shorts":
                  call chelsea_gf_action_3_youth_take_off_shorts from _call_chelsea_gf_action_3_youth_take_off_shorts_1
                "Get to work":
                  call chelsea_gf_action_3_youth_get_to_work from _call_chelsea_gf_action_3_youth_get_to_work_1
            "You need to be punished":
              player.c "I can't let you get away with that behavior, young lady."
              wt_image chubby_gf_youth_3_25
              chelsea.c "What?  What did I do wrong??"
              player.c "Prancing around showing off your body in immodest clothes, knowing that you don't have time to look after me after getting me worked up."
              wt_image chubby_gf_youth_3_24
              chelsea.c "No!  I wasn't trying ..."
              player.c "You weren't trying to tease me?"
              wt_image chubby_gf_youth_3_23
              chelsea.c "Well, maybe a little, but ..."
              player.c "No 'buts', other than the one you're going to present to me.  Turn around and face the wall."
              wt_image chubby_gf_youth_3_25
              chelsea.c "Please don't punish me.  I was only trying to make you feel good."
              player.c "You were trying to give me an erection, weren't you?"
              wt_image chubby_gf_youth_3_23
              chelsea.c "Yes"
              player.c "Knowing that you had to go to work."
              wt_image chubby_gf_youth_3_24
              chelsea.c "I guess, yes."
              player.c "Without any plans to look after my erection until after you finished work."
              wt_image chubby_gf_youth_3_25
              chelsea.c "I guess not.  I didn't think of that."
              player.c "Do you understand now why I'm going to punish you?"
              wt_image chubby_gf_youth_3_5
              chelsea.c "Yes, [chelsea.your_name]."
              "She turns around and places her hand on the wall to steady herself as she presents her ass to you."
              wt_image chubby_gf_youth_3_6
              "You're not even entirely sure you want her to stop prancing around and teasing you in short shorts, even if it is naughty behavior that can't be condoned. You make it a light spanking, through the offending shorts hard enough for her to feel it and want it to stop, but not particularly painful ... *smack* ... *smack* ... *smack*"
              chelsea.c "ow"
              $ chelsea.temporary_count = 3
              $ title = "Spank her again?"
              menu menu_chelsea_gf_event_3_spank_menu:
                "Yes":
                    $ chelsea.temporary_count += 1
                    "*smack*"
                    if chelsea.temporary_count < 5:
                        chelsea.c "Ow!"
                    elif chelsea.temporary_count < 10:
                        chelsea.c "Oww!"
                    elif chelsea.temporary_count < 15:
                        chelsea.c "Oww!!"
                    if chelsea.temporary_count < 15:
                        jump menu_chelsea_gf_event_3_spank_menu
                    else:
                        wt_image chubby_gf_youth_3_7
                        chelsea.c "Oww!!!  I'm sorry!!  I'm sorry!!!"
                        "She rubs her sore bottom and pouts."
                        player.c "What are you sorry about?  Being a tease or being punished for it?"
                        wt_image chubby_gf_youth_3_24
                        chelsea.c "Both?"
                "That's enough":
                  wt_image chubby_gf_youth_3_7
                  "She rubs her sore bottom and pouts."
                  chelsea.c "I'm sorry, [chelsea.your_name]."
                  player.c "What are you sorry about?  Being a tease or being punished for it?"
                  wt_image chubby_gf_youth_3_24
                  chelsea.c "Both?"
              $ chelsea.spank_count += 1
              $ chelsea.temporary_count = 0
            "Get to work":
              call chelsea_gf_action_3_youth_get_to_work from _call_chelsea_gf_action_3_youth_get_to_work_2
        "Have fun at work":
          wt_image chubby_gf_youth_3_24
          chelsea.c "Don't be silly, [chelsea.your_name]. I'm not allowed to have fun at work. I can't even bring my teddy. I have to pretend to be all grown up."
          $ chelsea.temporary_count = 0
    else:
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_bbw_3_1
        "You find [chelsea.name] crossing the house wearing just her underwear and a stylish support girdle."
        $ title = "Tell her she looks good?"
        menu:
          "Yes, compliment her":
            player.c "Did you dress up for me?"
            chelsea.c "Umm, yes?"
            "She laughs."
            wt_image chubby_gf_bbw_3_14
            chelsea.c "Okay, no.  I'm about to go to work and decided to pack a lunch.  I didn't want to get my clothes messed up in the kitchen.  Do you like how I'm dressed?  Or not dressed, I guess?"
            player.c "Absolutely.  You can prance around the house in just your undergarments anytime you like."
            wt_image chubby_gf_bbw_3_2
            chelsea.c "Ahh, you're sweet, [chelsea.your_name]!"
            $ title = "What do you tell her?"
            menu:
              "Ask her to sit":
                player.c "Have a seat."
                wt_image chubby_gf_bbw_3_14
                chelsea.c "I need to get ready for work."
                player.c "This won't take long."
                wt_image chubby_gf_bbw_3_4
                chelsea.c "Okay. What did you want?"
                $ title = "Now what?"
                menu:
                  "Tell her to touch herself":
                    player.c "Touch yourself, [chelsea.name]."
                    wt_image chubby_gf_bbw_3_15
                    chelsea.c "What?  Are you kidding??"
                    wt_image chubby_gf_bbw_3_16
                    player.c "No. I want to watch you play with yourself before you go to work."
                    wt_image chubby_gf_bbw_3_5
                    chelsea.c "You're bad!  This is just going to send me to work horny.  I don't have time to get off right now."
                    wt_image chubby_gf_bbw_3_17
                    "Despite her words, she touching herself, and you can soon smell and hear the sounds of her arousal."
                    chelsea.c "Ahhhh"
                    $ title = "What now?"
                    menu:
                      "Tell her to finger her ass" if chelsea.anal_status > 3:
                        player.c "Get your panties off and roll over."
                        wt_image chubby_gf_bbw_3_18
                        chelsea.c "Why?"
                        wt_image chubby_gf_bbw_3_19
                        player.c "Because I want you to stick a finger in your ass."
                        if chelsea.anal_status == 4:
                          chelsea.c "What?"
                          player.c "Go on, it won't hurt."
                          chelsea.c "I know but ..."
                          player.c "Come on, it'll turn me on to see you fingering yourself like that."
                          wt_image chubby_gf_bbw_3_20
                          call chelsea_anal_fingering from _call_chelsea_anal_fingering
                        else:
                          wt_image chubby_gf_bbw_3_20
                          "[chelsea.name]'s become used to putting things in her ass.  She doesn't question your instruction.  She just slides a finger into her butt."
                        wt_image chubby_gf_bbw_3_6
                        chelsea.c "Okay, you've had your fun. I need to wash my finger and get to work."
                        $ chelsea.masturbation_count += 1
                        $ chelsea.temporary_count = 0
                      "Tell her to cum quickly":
                        player.c "I bet you can cum for me before you need to go to work.  Get your panties off so I can watch you finger fuck yourself."
                        wt_image chubby_gf_bbw_3_18
                        chelsea.c "You think I'll be able to cum with you staring at me like this?"
                        player.c "Yes"
                        wt_image chubby_gf_bbw_3_13
                        "[chelsea.name] half-closes her eyes. She's well aware that you're watching her, but not looking at you helps her get into things.  After that, her pleasure builds quickly, until her body starts trembling, a sure sign that her climax is near."
                        chelsea.c "Ahhhhh"
                        player.c "Look at me when you cum, [chelsea.name]."
                        wt_image chubby_gf_bbw_3_12
                        "She opens her eyes as the orgasm rolls over her."
                        chelsea.c "Aahhhhhh"
                        wt_image chubby_gf_bbw_3_7
                        chelsea.c "Mmmmm.  I'm going to be late for work now, but I guess that was worth it."
                        player.c "You don't seem to be rushing out of here."
                        chelsea.c "I need to wait till my legs are no longer rubber."
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.masturbation_count += 1
                        $ chelsea.orgasm_count += 1
                        $ chelsea.relationship_counter += 0.5
                      "Send her to work horny":
                        player.c "You can stop, now.  I like the idea of you being horny at work."
                        wt_image chubby_gf_bbw_3_6
                        chelsea.c "You are so bad.  Well, you get your wish.  I'm going to be thinking about your big dick all day. I can't wait to have it where my fingers just were."
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        $ chelsea.temporary_count = 0
                    change player energy by -energy_very_short notify
                  "Jerk off while you look at her":
                    "Removing your cock from your pants, you stroke yourself while staring at her."
                    wt_image chubby_gf_bbw_3_16
                    chelsea.c "Are you ... you are!"
                    wt_image chubby_gf_bbw_3_5
                    chelsea.c "Oh, that is so hot!  I can't believe my body turns you on that much.  Did you want to see more of it?"
                    $ title = "What do you want to look at?"
                    menu:
                      "Her tits":
                        wt_image chubby_gf_bbw_3_6
                        "[chelsea.name] quickly disrobes..."
                        wt_image chubby_gf_bbw_3_7
                        "... then leans forward to give you a good look at her giant boobs as you pump yourself."
                      "Her ass":
                        wt_image chubby_gf_bbw_3_6
                        "[chelsea.name] quickly disrobes ..."
                        wt_image chubby_gf_bbw_3_8
                        "... then turns herself around so you can stare at her ass as you pump yourself."
                      "Her face":
                        wt_image chubby_gf_bbw_3_15
                        "[chelsea.name] watches with fascination as you pump yourself while staring at her."
                    $ title = "Where do you want to cum?"
                    menu:
                      "On her":
                        wt_image chubby_gf_toned_3_10
                        "You step up close to [chelsea.name].  She moans as you place your cock directly above her face."
                        chelsea.c "Ohh!!"
                        wt_image chubby_gf_toned_3_11
                        player.c "[player.orgasm_text]"
                        "[chelsea.name] grins at you and laughs."
                        chelsea.c "Well, I can't go to the office like this!  Good thing I hadn't put my clothes on yet, or I'd have a lot bigger clean-up job before work."
                        $ chelsea.facial_count += 1
                        orgasm notify
                      "On the floor":
                        wt_image chubby_gf_bbw_3_10
                        player.c "[player.orgasm_text]"
                        "[chelsea.name] groans at the sight of your sperm arcing up and over the floor between you and her."
                        chelsea.c "Ohh!!  That was so hot!  I'm going to be touching myself all day at work, thinking about that."
                        orgasm notify
                        $ title = "What next?"
                        menu:
                          "Tell her to clean it up":
                            if chelsea.cum_lick_count > 3:
                              wt_image chubby_gf_bbw_3_11
                              "She hesitates a moment, then falls to the floor, looking up at you."
                              player.c "That's right.  Use your tongue."
                              wt_image chubby_gf_toned_3_30
                              "She does a thorough job of cleaning the floor..."
                              wt_image chubby_gf_toned_3_14
                              "... making sure to get every last drop before getting up."
                              $ chelsea.cum_lick_count += 1
                            else:
                              wt_image chubby_gf_bbw_3_15
                              if chelsea.cum_lick_count > 1:
                                "She hesitates before replying."
                                chelsea.c "I need to get dressed and get going."
                              else:
                                chelsea.c "What?  Hey, I appreciate the tribute, but you made the mess.  You clean it up.  Besides, I need to get dressed and get going."
                              $ title = "What do you do?"
                              menu:
                                "Use her trigger" if chelsea.has_tag('trigger_implanted'):
                                  player.c "You're going to clean my sperm up, [chelsea.name]."
                                  chelsea.c "What?  Why?"
                                  wt_image chubby_gf_bbw_3_10
                                  player.c "Because I told you to. [chelsea.trigger_phrase], [chelsea.name].  Get on the floor and clean up my sperm."
                                  wt_image chubby_gf_bbw_3_11
                                  "The entranced women gets down on the floor, then looks up at you."
                                  player.c "With your tongue, [chelsea.name].  Lick it up with your tongue."
                                  wt_image chubby_gf_toned_3_30
                                  "[chelsea.name] has no aversion to eating your cum, and in her triggered state, she willing does so off the floor as she kneels in front of you."
                                  wt_image chubby_gf_toned_3_14
                                  "She makes sure to get every last drop before she gets up. Your use of her complete, you release her from her trigger and send her off to work."
                                  $ chelsea.cum_lick_count += 1
                                "Dominate her" if chelsea.dominate_status == 8:
                                  wt_image chubby_gf_toned_3_15
                                  player.c "I said clean up my sperm, fucktoy."
                                  "Seizing her by the hair, you pull her off the sofa and onto the floor."
                                  wt_image chubby_gf_toned_3_30
                                  "Up until now, she's been enjoying this, but being forced to grovel at your feet and clean up your sperm with her tongue changes the whole experience for her.  She has no aversion to eating your cum, but licking it off the floor is a whole different matter."
                                  player.c "Get every drop, fucktoy.  Once you've licked up and swallowed every bit of my jizz, then you can go to work."
                                  sys "[chelsea.name] is less happy with your relationship."
                                  $ chelsea.visit_count -= 1
                                  $ chelsea.relationship_counter -= 1
                                  $ chelsea.cum_lick_count += 2
                                "Let her go to work":
                                  pass
                          "Let her go to work":
                            pass
                  "Change your mind (send her to work)":
                    player.c "Actually, maybe you should get to work. I'll be thinking about you while your gone."
                    wt_image chubby_gf_bbw_3_3
                    chelsea.c "Thanks.  Now I'll be thinking about you, too, [chelsea.your_name]."
                    "[chelsea.name] smiles and jiggles her boobs at you as she leaves."
                    sys "[chelsea.name] is happier with your relationship."
                    $ chelsea.relationship_counter += 0.5
                    $ chelsea.temporary_count = 0
              "Let her finish getting ready for work":
                player.c "Thanks for the show. I'll be thinking about you while you're at work."
                wt_image chubby_gf_bbw_3_3
                chelsea.c "Thanks.  Now I'll be thinking about you, too, [chelsea.your_name]."
                "[chelsea.name] smiles and jiggles her boobs at you as she leaves."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
                $ chelsea.temporary_count = 0
          "Not today":
            $ chelsea.temporary_count = 0
      else:
        wt_image chubby_gf_toned_3_1
        "You find [chelsea.name] crossing the house wearing just her underwear."
        $ title = "Tell her she looks good?"
        menu:
          "Yes, compliment her":
            player.c "Wow.  You look hot."
            wt_image chubby_gf_toned_3_21
            chelsea.c "Thank you!"
            player.c "Are you trying to tease me?"
            wt_image chubby_gf_toned_3_23
            chelsea.c "Umm, yes?"
            "She laughs."
            wt_image chubby_gf_toned_3_2
            chelsea.c "Okay, no.  I'm about to go to the office and decided to pack a light lunch for after my workout.  I didn't want to get my clothes messed up while I was packing my lunch in the kitchen."
            $ title = "What do you do?"
            menu:
              "Ask her to strip":
                player.c "Do you have a few minutes?"
                wt_image chubby_gf_toned_3_22
                chelsea.c "Just a few.  Why?"
                player.c "I'd love to see you out of that bra and panties."
                wt_image chubby_gf_toned_3_24
                chelsea.c "Well .... okay."
                wt_image chubby_gf_toned_3_3
                chelsea.c "I guess it won't take me that long to put them back on again."
                wt_image chubby_gf_toned_3_4
                chelsea.c "Now what?  You just ogle me until I have to go to work?"
                $ title = "Now what?"
                menu:
                  "Tell her to touch herself":
                    player.c "Touch yourself, [chelsea.name]."
                    wt_image chubby_gf_toned_3_9
                    chelsea.c "What?  Are you kidding??"
                    player.c "No.  I want to watch you play with yourself before you go to work."
                    wt_image chubby_gf_toned_3_16
                    chelsea.c "You're bad! This is just going to make me horny. I don't have time to get off right now."
                    $ title = "What now?"
                    menu:
                      "Tell her to finger her ass" if chelsea.anal_status > 3:
                        if chelsea.anal_status == 4:
                          wt_image chubby_gf_toned_3_17
                          chelsea.c "What?"
                          player.c "Go on. It won't hurt."
                          chelsea.c "I know but..."
                          player.c "Come on. It'll turn me on to see you fingering yourself like that."
                          wt_image chubby_gf_youth_3_1
                          call chelsea_anal_fingering from _call_chelsea_anal_fingering_3
                        else:
                          wt_image chubby_gf_youth_3_1
                          "[chelsea.name]'s become used to putting things in her ass. She doesn't question your instruction. She just slides a finger into her butt."
                        wt_image chubby_gf_toned_3_25
                        chelsea.c "Okay, you've had your fun. I need to wash my finger and get to work."
                        $ chelsea.temporary_count = 0
                      "Tell her she can cum quickly":
                        wt_image chubby_gf_toned_3_17
                        player.c "I bet you can cum for me before you need to go to work."
                        chelsea.c "With you staring at me like this?"
                        player.c "Yes"
                        wt_image chubby_gf_toned_3_18
                        "[chelsea.name] closes her eyes. She's well aware that you're watching her, but not being able to see you helps her get into things."
                        wt_image chubby_gf_toned_3_19
                        "It takes a few minutes, but eventually you see, hear and smell the first signs of her arousal."
                        chelsea.c "Ahhhhh"
                        wt_image chubby_gf_toned_3_26
                        "After that, her pleasure builds quickly.  Her body starts trembling and her head rolls back, a sure sign that her climax is near."
                        player.c "Look at me when you cum, [chelsea.name]."
                        wt_image chubby_gf_toned_3_20
                        "She opens her eyes as the orgasm rolls over her."
                        chelsea.c "Aahhhhhh"
                        wt_image chubby_gf_toned_3_25
                        chelsea.c "Mmmmm.  That was nice, but I'm going to be late for work now."
                        player.c "You don't seem to be rushing out of here."
                        wt_image chubby_gf_toned_3_4
                        chelsea.c "I need to wait till my legs are no longer rubber, first."
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        $ chelsea.masturbation_count += 1
                        $ chelsea.orgasm_count += 1
                        change player energy by -energy_short notify
                      "Send her to work horny":
                        wt_image chubby_gf_toned_3_18
                        "You wait until she's starting to get worked up before you say anything."
                        chelsea.c "Ahhhhh"
                        wt_image chubby_gf_toned_3_16
                        player.c "You can stop, now.  I like the idea of you being horny at work."
                        wt_image chubby_gf_toned_3_4
                        chelsea.c "You are so bad. Well, you get your wish. I'm going to be thinking about your big dick all day. I can't wait to have it where my fingers just were."
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        $ chelsea.temporary_count = 0
                  "Jerk off while you look at her":
                    player.c "Removing your cock from your pants, you stroke yourself while staring at her."
                    wt_image chubby_gf_toned_3_9
                    chelsea.c "Are you ... you are!"
                    wt_image chubby_gf_toned_3_6
                    chelsea.c" Oh, that is so hot! I can't believe my body turns you on that much.  Did you want to see more of it?"
                    $ title = "What do you want to look at?"
                    menu:
                      "Her tits":
                        wt_image chubby_gf_toned_3_7
                        "[chelsea.name] leans forward and gives you a good look at her breasts as you pump yourself."
                      "Her pussy":
                        wt_image chubby_gf_toned_3_8
                        "[chelsea.name] spread herself open and watches with fascination as you pump yourself."
                      "Her ass":
                        wt_image chubby_gf_toned_3_28
                        "[chelsea.name] turns around and gives you a good look at her butt as you pump yourself."
                    $ title = "Where do you want to cum?"
                    menu:
                      "On her":
                        wt_image chubby_gf_toned_3_10
                        "You step up close to [chelsea.name].  She moans as you place your cock directly above her face."
                        chelsea.c "Ohh!!"
                        player.c "[player.orgasm_text]"
                        wt_image chubby_gf_toned_3_11
                        "[chelsea.name] grins at you and laughs."
                        chelsea.c "Well, I can't go to the office like this!  Good thing I hadn't put my clothes on yet, or I'd have a lot bigger clean-up job before work."
                        $ chelsea.facial_count += 1
                      "On the floor":
                        "[chelsea.name] moans at the sight of your sperm arcing up and over the floor between you and her."
                        player.c "[player.orgasm_text]"
                        wt_image chubby_gf_toned_3_6
                        chelsea.c "Ohh!!  That was so hot!  I'm going to be touching myself all day at work, thinking about that."
                        $ title = "What next?"
                        menu:
                          "Tell her to clean it up":
                            if chelsea.cum_lick_count > 3:
                              wt_image chubby_gf_toned_3_12
                              "She hesitates a moment, then falls to the floor, looking up at you."
                              player.c "That's right, use your tongue."
                              wt_image chubby_gf_toned_3_30
                              "She does a thorough job of cleaning the floor ..."
                              wt_image chubby_gf_toned_3_14
                              "... making sure to get every last drop before getting up."
                              $ chelsea.cum_lick_count += 1
                            else:
                              wt_image chubby_gf_toned_3_25
                              if chelsea.cum_lick_count > 1:
                                "She hesitates before replying."
                                chelsea.c "I need to get dressed and get going."
                              else:
                                chelsea.c "What?  Hey, I appreciate the tribute, but you made the mess - you clean it up.  Besides, I need to get dressed and get going."
                              $ title = "What do you do?"
                              menu:
                                "Use her trigger" if chelsea.has_tag('trigger_implanted'):
                                  player.c "You're going to clean my sperm up, [chelsea.name]."
                                  wt_image chubby_gf_toned_3_9
                                  chelsea.c "What?  Why?"
                                  wt_image chubby_gf_toned_3_29
                                  player.c "Because I told you to. [chelsea.trigger_phrase], [chelsea.name].  Get on the floor and clean up my sperm."
                                  wt_image chubby_gf_toned_3_12
                                  "The hypnotized women gets down on the floor, then looks up at you."
                                  player.c "With your tongue, [chelsea.name]. Lick it up with your tongue."
                                  wt_image chubby_gf_toned_3_30
                                  "[chelsea.name] has no aversion to eating your cum, and in her triggered state, she willing does so off the floor as she kneels in front of you."
                                  wt_image chubby_gf_toned_3_14
                                  "She makes sure to get every last drop before she gets up.  Your use of her complete, you release her from her trigger and send her off to work."
                                  $ chelsea.cum_lick_count += 1
                                "Dominate her" if chelsea.dominate_status == 8:
                                  wt_image chubby_gf_toned_3_15
                                  player.c "I said clean up my sperm, fucktoy."
                                  "Seizing her by the hair, you pull her off the sofa and onto the floor."
                                  wt_image chubby_gf_toned_3_30
                                  player.c "Get every drop, fucktoy. Once you've licked up and swallowed every bit of my jizz, then you can go to work."
                                  "Up until now, she's been enjoying this, but being forced to grovel at your feet and clean up your sperm with her tongue changes the whole experience for her.  She has no aversion to eating your cum, but licking it off the floor is a whole different matter."
                                  sys "[chelsea.name] is less happy with your relationship."
                                  $ chelsea.visit_count -= 1
                                  $ chelsea.relationship_counter -= 1
                                  $ chelsea.cum_lick_count += 2
                                "Let her go to work":
                                  pass
                          "Let her go to work":
                            pass
                    orgasm notify
                  "Just ogle her":
                    player.c "That sounds like fun.  Let me drink you in."
                    wt_image chubby_gf_toned_3_5
                    "[chelsea.name] smiles shyly."
                    $ title = "What do you want to ogle?"
                    menu menu_chelsea_gf_toned_ogle_menu:
                      "Her tits":
                        wt_image chubby_gf_toned_3_7
                        jump menu_chelsea_gf_toned_ogle_menu
                      "Her pussy":
                        wt_image chubby_gf_toned_3_8
                        jump menu_chelsea_gf_toned_ogle_menu
                      "Her ass":
                        wt_image chubby_gf_toned_3_28
                        jump menu_chelsea_gf_toned_ogle_menu
                      "That's enough":
                        player.c "Thanks for giving me something to think about while you're at work."
                        wt_image chubby_gf_toned_3_6
                        chelsea.c "I'll be thinking about you, too, [chelsea.your_name]."
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        $ chelsea.temporary_count = 0
              "Let her finish getting ready for work":
                player.c "Thanks for the show.  I'll be thinking about you while you're at work."
                wt_image chubby_gf_toned_3_21
                "[chelsea.name] grins."
                chelsea.c "Thanks.  Now I'll be thinking about you, too, [chelsea.your_name]."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
                $ chelsea.temporary_count = 0
          "Not today":
            $ chelsea.temporary_count = 0
    call character_location_return(chelsea) from _call_character_location_return_34
  # lingerie show
  if chelsea.gf_outfit == 4:
    if chelsea.has_tag('bbw') and chelsea.has_tag('lingerie_happy'):
      call forced_movement(living_room) from _call_forced_movement_215
      summon chelsea no_follows
      wt_image chubby_lingerie_flattering_1
      if chelsea.has_tag('little_girl'):
        "You find [chelsea.name] in the living room wearing the skimpy negligee you bought her."
        chelsea.c "Hi there. I know these clothes are for big girls, but you were nice enough to buy them for me, so I thought I should put them on once in a while, in case you want to see me in them.  Care to spend some time with me while I wear them?"
      else:
        "You find [chelsea.name] in the living room wearing the skimpy negligee you bought her."
        chelsea.c "Hi there. You were nice enough to buy this for me, so I thought I should put it on once in a while, in case you'd like to see me in it.  Care to spend some time with me while I wear it?"
      wt_image chubby_lingerie_flattering_7
      chelsea.c "Maybe we could watch some TV together?  Or, you know, do something else?"
      $ title = "What do you want?"
      menu:
        "Hand Job":
          "[chelsea.name]'s eyes sparkle as you take your hard cock out of your pants."
          wt_image chubby_lingerie_flattering_20
          chelsea.c "For me?  Let me get ready for you."
          player.c "How about you jerk me off while we watch TV, [chelsea.name]?"
          wt_image chubby_lingerie_flattering_14
          "She kneels down in front of you and pumps you gently while watching the show."
          wt_image chubby_lingerie_flattering_24
          "Despite paying attention to the TV, she doesn't neglect your dick, maintaining a constant, steady gentle stroking with her soft hand and occasionally tickling the tip of your cock with her tongue."
          wt_image chubby_lingerie_flattering_6
          "Eventually this has the expected effect, although your climax catches [chelsea.name] by surprise, and she laughs as she feels your hot cum splatter on her tits."
          player.c "[player.orgasm_text]"
          chelsea.c "Oh!"
          $ chelsea.handjob_count += 1
          orgasm notify
        "Tit Job":
          "[chelsea.name]'s eyes sparkle as you take your hard cock out of your pants."
          wt_image chubby_lingerie_flattering_20
          chelsea.c "For me?  Let me get ready for you."
          player.c "Come here, [chelsea.name]."
          wt_image chubby_lingerie_flattering_3
          "She knows immediately what you want.  She smothers your dick between her soft breasts and tit fucks you."
          wt_image chubby_lingerie_flattering_9
          chelsea.c "Does that feel nice?"
          wt_image chubby_lingerie_flattering_21
          "You give her your answer in cum."
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_flattering_11
          chelsea.c "I'll take that as a yes."
          $ chelsea.titfuck_count += 1
          orgasm notify
        "Blow Job":
          "[chelsea.name]'s eyes sparkle as you take your hard cock out of your pants."
          wt_image chubby_lingerie_flattering_20
          chelsea.c "For me?  Let me get ready for you."
          player.c "Come here, [chelsea.name], and kneel in front of me."
          wt_image chubby_lingerie_flattering_15
          "For a moment, she's not sure whether you want her breasts or mouth, but as you guide her head forward, she happily licks the head of your hard cock ..."
          wt_image chubby_lingerie_flattering_16
          "... before taking you deep into her mouth."
          wt_image chubby_lingerie_flattering_4
          "She keeps her eyes on the TV as she blows you. It seems she's really interested in this show."
          wt_image chubby_lingerie_flattering_17
          "Despite that, she doesn't neglect your cock, licking, sucking and teasing it with her lips and tongue ..."
          wt_image chubby_lingerie_flattering_22
          "... until her efforts have the expected effect."
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_flattering_10
          "She wraps her lips tightly around you, happily accepting your seed and swallowing every drop, without missing a moment of her show."
          $ chelsea.blowjob_count += 1
          $ chelsea.swallow_count += 1
          orgasm notify
        "Missionary":
          "[chelsea.name]'s eyes sparkle as you take your hard cock out of your pants."
          wt_image chubby_lingerie_flattering_20
          chelsea.c "For me?  Let me get ready for you."
          wt_image chubby_lingerie_flattering_13
          "[chelsea.name] makes no objection as you lay her down on her back and spread her legs.  She's already wet, and you slide into her easily."
          chelsea.c "Ahhhh"
          wt_image chubby_lingerie_flattering_5
          "Wearing the lingerie seems to have put [chelsea.name] in the mood. She plays with herself as you fuck her, and cums shortly before you do."
          wt_image chubby_lingerie_flattering_23
          chelsea.c "Aahhhhhh"
          player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        "Doggy Style":
          "[chelsea.name]'s eyes sparkle as you take your hard cock out of your pants."
          wt_image chubby_lingerie_flattering_20
          chelsea.c "For me?  Let me get ready for you."
          wt_image chubby_lingerie_flattering_18
          "[chelsea.name] makes no objection as you turn her around and position her on her knees.  She's already wet, and you slide into her easily."
          chelsea.c "Ahhhh"
          wt_image chubby_lingerie_flattering_19
          "Wearing the lingerie seems to have put [chelsea.name] in the mood.  She moans loudly as you fuck her ..."
          chelsea.c "Ahhhhh"
          wt_image chubby_lingerie_flattering_12
          "... and cums just before you do."
          chelsea.c "Aahhhhhh"
          player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        "Just watch TV":
          player.c "Watching TV sounds good."
          wt_image chubby_lingerie_flattering_8
          chelsea.c "Okay!  You pick something to watch, I'm going to make myself comfy.  You could snuggle up beside me, if you want?  I have some nice soft pillows you can use to rest your head on."
          "The two of you enjoy watching a show snuggled up together on the sofa."
          change player energy by -energy_short notify
        "Nothing":
          "You leave her alone for now."
          $ chelsea.temporary_count = 0
      call character_location_return(chelsea) from _call_character_location_return_35
    elif chelsea.has_tag('toned') and chelsea.has_tag('lingerie_motivated'):
      call forced_movement(living_room) from _call_forced_movement_216
      summon chelsea no_follows
      wt_image chubby_lingerie_motivate_1
      "You find [chelsea.name] in the living room wearing the skimpy negligee you bought her."
      wt_image chubby_lingerie_motivate_17
      if chelsea.has_tag('little_girl'):
        chelsea.c "Hi, [chelsea.your_name].  I know these clothes are for big girls, but you were nice enough to buy them for me, so I thought I should put them on once in a while, in case you want to see me in them.  Care to spend some time with me while I wear them?"
      else:
        chelsea.c "Hi, [chelsea.your_name].  You were nice enough to buy this for me, so I thought I should put it on once in a while, in case you'd like to see me in it.  Care to spend some time with me while I wear it?"
      wt_image chubby_lingerie_motivate_10
      chelsea.c "If you want, we could work out together.  You know, the fun sort of workout."
      $ title = "What do you want?"
      menu:
        "Tit job":
          player.c "Remove your top, [chelsea.name]."
          wt_image chubby_lingerie_motivate_21
          "Her eyes sparkle as you take out your cock."
          wt_image chubby_lingerie_motivate_15
          "She knows immediately what you want. She smothers your dick in her ample bosom."
          wt_image chubby_lingerie_motivate_16
          "Playfully she licks your cock as she tit fucks you."
          wt_image chubby_lingerie_motivate_4
          chelsea.c "Does that feel nice?"
          wt_image chubby_lingerie_motivate_23
          "You give her your answer in the form of cum."
          wt_image chubby_lingerie_motivate_24
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_motivate_25
          chelsea.c "I'll take that as a 'yes'."
          $ chelsea.titfuck_count += 1
          orgasm notify
        "Blow job":
          wt_image chubby_lingerie_motivate_21
          player.c "Come here, [chelsea.name], and kneel in front of me."
          wt_image chubby_lingerie_motivate_5
          "For a moment, she's not sure whether you want her breasts or mouth.  As you guide her head forward, she happily licks the head of your hard cock ..."
          wt_image chubby_lingerie_motivate_26
          "... before taking you into her mouth."
          wt_image chubby_lingerie_motivate_8
          "She attends carefully to your dick, using her tongue, lips and hand to bring you pleasure."
          wt_image chubby_lingerie_motivate_29
          $ title = "Where do you want to cum?"
          menu:
            "In her":
              wt_image chubby_lingerie_motivate_30
              "When she feels your climax building, she wraps her lips around you ..."
              wt_image chubby_lingerie_motivate_27
              "... and happily swallows every drop."
              player.c "[player.orgasm_text]"
              wt_image chubby_lingerie_motivate_28
              $ chelsea.swallow_count += 1
            "On her":
              wt_image chubby_lingerie_motivate_31
              "When you feel your climax starting, you pull out while holding her in position."
              wt_image chubby_lingerie_motivate_9
              "She smiles, happily holding her breasts up as you shoot your load onto them and her waiting face."
              wt_image chubby_lingerie_motivate_32
              $ chelsea.facial_count += 1
          chelsea.c "I think you enjoyed that!"
          $ chelsea.blowjob_count += 1
          orgasm notify
        "Missionary":
          wt_image chubby_lingerie_motivate_12
          "[chelsea.name] makes no objection as you lay her back on the sofa and lift her legs, giving you access to her sex.  She's already wet, and you slide into her easily."
          wt_image chubby_lingerie_motivate_39
          chelsea.c "Ahhhh"
          wt_image chubby_lingerie_motivate_40
          "Wearing the lingerie seems to have put [chelsea.name] in the mood.  She rubs her clit as you fuck her ..."
          wt_image chubby_lingerie_motivate_7
          "... soon strokes herself to orgasm just before you stroke yourself to orgasm inside her."
          wt_image chubby_lingerie_motivate_41
          chelsea.c "Aahhhhhh"
          wt_image chubby_lingerie_motivate_42
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_motivate_21
          chelsea.c "Thanks for the workout, [chelsea.your_name]!  It was fun, even if you ended up doing most of the work."
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        "Doggy style":
          wt_image chubby_lingerie_motivate_19
          "[chelsea.name] grins and gets into position."
          wt_image chubby_lingerie_motivate_34
          "She's already wet, and you slide into her easily."
          wt_image chubby_lingerie_motivate_35
          chelsea.c "Ahhhh"
          wt_image chubby_lingerie_motivate_6
          "At first you're not sure if she's going to be able to cum in this position, today ..."
          wt_image chubby_lingerie_motivate_36
          "... but wearing the lingerie does seem to have put her in the mood, as she suddenly starts shaking, and climaxes just before you."
          wt_image chubby_lingerie_motivate_37
          chelsea.c "Aahhhhhh"
          wt_image chubby_lingerie_motivate_38
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_motivate_21
          chelsea.c "Thanks for the fun workout, [chelsea.your_name]!  It really made me work my core."
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        "Have her ride you":
          wt_image chubby_lingerie_motivate_43
          "[chelsea.name] makes no objection as you pull her onto your lap.  She's already wet, and settles down on you easily."
          wt_image chubby_lingerie_motivate_44
          chelsea.c "Ahhhh"
          wt_image chubby_lingerie_motivate_13
          "Twisting away from your grip, [chelsea.name] turns herself around and starts riding you."
          wt_image chubby_lingerie_motivate_14
          "[chelsea.name]'s work outs are paying off.  She rides swiftly up-and-down on shaft ..."
          wt_image chubby_lingerie_motivate_45
          "... and soon gets the both of you off."
          wt_image chubby_lingerie_motivate_46
          chelsea.c "Aahhhhhh"
          wt_image chubby_lingerie_motivate_47
          player.c "[player.orgasm_text]"
          wt_image chubby_lingerie_motivate_19
          chelsea.c "Thanks for the fun workout, [chelsea.your_name]!  It really made me work my legs."
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        "Just watch TV":
          # happy with relationship
          player.c "How about we just watch some TV together today?"
          if chelsea.relationship_counter > 4:
            wt_image chubby_lingerie_motivate_33
            chelsea.c "Okay, but I'm not sure how well you'll be able to focus on the television."
            wt_image chubby_lingerie_motivate_11
            "She settles onto the couch and pulls down her top.  The two of you watch a show together, with you a little distracted by her bare chest, and her a little distracted by trying to get you to look at her instead of the TV."
          else:
            wt_image chubby_lingerie_motivate_22
            "[chelsea.name]'s a little disappointed that she couldn't entice you do something more active with her, but only a little.  She settles down beside you and you both enjoy a show together."
            change player energy by -energy_very_short notify
        "Nothing":
          "You leave her alone for now."
          $ chelsea.temporary_count = 0
      call character_location_return(chelsea) from _call_character_location_return_36
    else:
      $ chelsea.gf_outfit += 1
  # back to "if" because of possible advancement from 4
  # pool
  if chelsea.gf_outfit == 5:
    call forced_movement(backyard) from _call_forced_movement_217
    summon chelsea no_follows
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_pool_2_23
    else:
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_pool_2_2
      else:
        wt_image chubby_gf_pool_2_3
    "You find [chelsea.name] outside, sunning herself by the pool."
    chelsea.c "Hi, [chelsea.your_name].  Did you want something?"
    $ title = "What do you want?"
    menu:
      "Tit job":
        wt_image chubby_gf_pool_2_11
        chelsea.c "Really?  Is your cock in need of relief?  Better come over here so my boobs can make it feel better."
        wt_image chubby_gf_pool_2_12
        "Pulling down her top, you run your fingers across her nipples, which immediately stiffen.  She reaches back as you do and grabs your cock, which is also quickly stiffening."
        wt_image chubby_gf_pool_2_13
        "Then she kneels down in front of you and places your dick between her breasts."
        wt_image chubby_gf_pool_2_27
        "Pressing her soft mounds around your dick ..."
        wt_image chubby_gf_pool_2_14
        "... she pumps them up and down your hard shaft.  It doesn't take much of this treatment before you're ready to cum ..."
        wt_image chubby_gf_pool_2_15
        "... emptying the contents of your balls onto her oversized mammaries."
        player.c "[player.orgasm_text]"
        wt_image chubby_gf_pool_2_16
        chelsea.c "Feel better now?"
        player.c "Much"
        chelsea.c "Glad I could help."
        $ chelsea.titfuck_count += 1
        orgasm notify
      "Blow job":
        wt_image chubby_gf_pool_2_6
        chelsea.c "Really?  Is your cock in need of sucking?  Better come over here and let me make it feel better."
        wt_image chubby_gf_pool_2_24
        "[chelsea.name] gives your cock a lick ..."
        wt_image chubby_gf_pool_2_7
        "... then wraps her lips around the head ..."
        wt_image chubby_gf_pool_2_25
        "... and takes it into her mouth."
        wt_image chubby_gf_pool_2_8
        "Then she starts bobbing her head up-and-down your hard shaft.  Between her lips wrapped tightly around you and her tongue playing and teasing along the sensitive underside of your cock, you're soon ready to cum."
        $ title = "Where do you want to cum?"
        menu:
          "In her":
            wt_image chubby_gf_pool_2_9
            "A few more bobs of her head and down your dick, and your balls empty their load into her mouth as she gulps and swallows, successfully avoiding spilling any of your jizz."
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_pool_2_6
            $ chelsea.swallow_count += 1
          "On her":
            wt_image chubby_gf_pool_2_26
            "As you pull your cock out of her mouth, she knows what you want.  Replacing her lips with her hand, she wraps her soft fist around your shaft.  After a few pumps, your balls empty their load over her."
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_pool_2_10
            $ chelsea.facial_count += 1
        chelsea.c "Feel better now?"
        player.c "Much"
        chelsea.c "Glad I could help."
        $ chelsea.blowjob_count += 1
        orgasm notify
      "Sex":
        wt_image chubby_gf_pool_2_6
        chelsea.c "Really?  Looking for some fun in the sun?"
        wt_image chubby_gf_pool_2_12
        "Pulling down her top, you run your fingers across her nipples, which immediately stiffen.  She reaches back as you do and grabs your cock, which is also quickly stiffening."
        wt_image chubby_gf_pool_2_18
        "It takes very little additional foreplay to get [chelsea.name] ready.  Laying her down on her back, you stroke your hard cock along her labia until she's wet enough for the head of your cock to slip inside her."
        wt_image chubby_gf_pool_2_21
        chelsea.c "Ahhhh"
        wt_image chubby_gf_pool_2_19
        "Penetration makes her even wetter.  You're able to immediately set a quick pace, thrusting in and out of her as her excitement grows."
        chelsea.c "Ahhhhh"
        wt_image chubby_gf_pool_2_20
        player.c "Enjoying yourself?"
        chelsea.c "Uh huh!!  I'm really close, [chelsea.your_name]!"
        wt_image chubby_gf_pool_2_28
        chelsea.c "Aahhhhhh"
        wt_image chubby_gf_pool_2_29
        player.c "[player.orgasm_text]"
        wt_image chubby_gf_pool_2_22
        "When your balls finally stop pumping semen into her, she cuddles up alongside you."
        chelsea.c "You can join me for 'fun in the sun' anytime!"
        $ chelsea.sex_count += 1
        $ chelsea.orgasm_count += 1
        orgasm notify
      "Just chat with her":
        player.c "I thought we could chat, if you don't mind me joining you?"
        if chelsea.has_tag('bbw'):
          wt_image chubby_gf_pool_2_4
        else:
          wt_image chubby_gf_pool_2_5
        chelsea.c "Of course I don't mind!"
        "[chelsea.name] lies down on the pool lounger and the two of you spend an enjoyable hour together chatting."
        change player energy by -energy_very_short notify
      "Nothing today":
        player.c "Not today, [chelsea.name].  Enjoy the sun."
        chelsea.c "Thanks!  I will."
        if chelsea.has_tag('little_girl'):
          player.c "And don't forget to put sun block on. You don't want to get burned."
          wt_image chubby_gf_pool_2_1
          chelsea.c "I won't forget, [chelsea.your_name]. I'll go put more on right now."
          $ chelsea.visit_count -= 1 # to offset gain, later
    call forced_movement(living_room) from _call_forced_movement_218
    call character_location_return(chelsea) from _call_character_location_return_37
  # sofa (or workout) and ass fingering opp
  if chelsea.gf_outfit == 6:
    call forced_movement(living_room) from _call_forced_movement_219
    summon chelsea no_follows
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_youth_1_1
      "You find [chelsea.name] sitting on the sofa. She's dressed like a schoolgirl, but you're pretty sure the file she's working on is one she's brought home from the office. She looks busy, but perhaps she'd like a distraction?"
      $ title = "What do you do?"
      menu:
        "Interrupt her":
          player.c "Busy?"
          wt_image chubby_gf_youth_1_2
          chelsea.c "Uh huh. Trying to get some work done."
          player.c "Work work or schoolwork?"
          wt_image chubby_gf_youth_1_31
          "She giggles."
          chelsea.c "Work work."
          wt_image chubby_gf_youth_1_3
          "You pull her up out of the sofa to take a better look at her."
          player.c "I wasn't sure, considering how you're dressed."
          wt_image chubby_gf_youth_1_32
          chelsea.c "What's wrong with the way I'm dressed?"
          player.c "Nothing. You just normally dress differently for the office."
          wt_image chubby_gf_youth_1_4
          chelsea.c "Like a big girl, you mean?  But look!  This outfit is great.  My boobies are nicely tucked away out of sight ..."
          wt_image chubby_gf_youth_1_5
          chelsea.c "... and if my skirt rides up, my bum is covered by these boring white panties."
          wt_image chubby_gf_youth_1_6
          chelsea.c "All perfectly respectable, even if I'm going to the office, instead of school."
          "You know she's teasing you and wouldn't actually wear this outfit to her work, but she seems to enjoy pretending that she would. You, on the other hand, have other things you might enjoy."
          $ title = "What do you want?"
          menu:
            "Blow job":
              player.c "A little too respectable for my tastes."
              wt_image chubby_gf_youth_1_32
              chelsea.c "You don't want me to look respectable?"
              player.c "Not unless you can look respectable while sucking my dick."
              wt_image chubby_gf_youth_1_13
              chelsea.c "Maybe I can."
              "She giggles and kneels in front of you, takes out your cock, and gently licks the underside of the tip ..."
              wt_image chubby_gf_youth_1_14
              "... before running her lips along the side of your cock."
              chelsea.c "Does this look respectable?"
              player.c "Not yet."
              wt_image chubby_gf_youth_1_15
              chelsea.c "How about now?"
              "She runs her tongue across and over your balls, getting them nice and warm and wet."
              player.c "Getting better.  Let me see how respectable your lips look wrapped around my dick."
              wt_image chubby_gf_youth_1_16
              chelsea.c "Like this?"
              player.c "Don't talk with your mouth full, little girl."
              wt_image chubby_gf_youth_1_17
              "She gets the message.  Dropping the banter, she devotes herself to pleasuring your dick.  It doesn't take her long to get you ready to cum."
              wt_image chubby_gf_youth_1_16
              $ title = "Where do you want to cum?"
              menu:
                "In her mouth":
                  wt_image chubby_gf_youth_1_17
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_1_19
                  "She looks up at you as you shoot your load, gulping down the cum you spurting into the back of her throat."
                  player.c "That's the respectable look I like, little girl."
                  $ chelsea.swallow_count += 1
                "On her":
                  wt_image chubby_gf_youth_1_33
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_1_18
                  chelsea.c "Do you like how respectable I look now?"
                  player.c "Perfect"
                  $ chelsea.facial_count += 1
              $ chelsea.blowjob_count += 1
              orgasm notify
            "Fuck her from behind":
              player.c "Respectable, maybe, but I don't like you wearing anything boring."
              wt_image chubby_gf_youth_1_32
              chelsea.c "Boring??"
              player.c "Your panties are.  You said so yourself.  Turn around and let me get another look."
              wt_image chubby_gf_youth_1_5
              "She giggles and turns around, lifting her skirt."
              chelsea.c "Okay, you're right.  These are kind of boring.  But I need to be respectable when I'm working."
              player.c "Not around the house, you'd don't, though.  Pull them off and bend over the sofa."
              wt_image chubby_gf_youth_1_6
              chelsea.c "But then I'll be showing you my bare bum!"
              player.c "That'll make it easier for me to fuck you from behind, won't it?"
              wt_image chubby_gf_youth_1_31
              chelsea.c "Hmmm, I guess it will."
              wt_image chubby_gf_youth_1_20
              "You need to warm her up before you can enter her, but that doesn't take too long.  A few strokes of your hard cock along her slit and she's soon wet enough for penetration."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_1_21
              "After a few hard thrusts, she goes from wet to sopping wet.  Reaching a hand back, she opens herself up more, giving you better access so you can fuck her even harder."
              chelsea.c "That feels so good, [chelsea.your_name]!"
              if chelsea.anal_status > 3:
                $ title = "Tell her to finger her ass?"
                menu:
                  "Yes":
                    player.c "Don't stop there."
                    chelsea.c "What do you mean?"
                    player.c "Your hand.  Don't stop there.  Reach down and put a finger in your ass."
                    if chelsea.anal_status == 4:
                      chelsea.c "Why??"
                      player.c "Because it'll turn me on to see you do that.  Don't worry, it won't hurt."
                      wt_image chubby_gf_youth_1_22
                      "Hesitantly, she reaches back until she finds the opening of her butt with one of her fingers, and slowly pushes it inside."
                      call chelsea_anal_fingering from _call_chelsea_anal_fingering_4
                    else:
                      wt_image chubby_gf_youth_1_22
                      "[chelsea.name]'s become used to you wanting to see her play with her ass.  She doesn't argue, just reaches back and shoves a finger up her butt."
                    wt_image chubby_gf_youth_1_35
                    "You enjoy the view until you're almost ready to cum ..."
                    wt_image chubby_gf_youth_1_23
                    "... then you let her remove her finger and focus on her own arousal."
                    chelsea.c "Ahhhh"
                    wt_image chubby_gf_youth_1_20
                    chelsea.c "Aahhhhhh"
                  "Not today":
                    wt_image chubby_gf_youth_1_23
                    "A few more hard thrusts take you both over the edge."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_gf_youth_1_20
              else:
                wt_image chubby_gf_youth_1_23
                "A few more hard thrusts take you both over the edge."
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_youth_1_20
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_1_4
              chelsea.c "Guess I'll get back to work, now.  Thanks for the fun diversion, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Have her ride you":
              player.c "You look respectable now, but how respectable are you going to look riding up and down on my hard cock?"
              wt_image chubby_gf_youth_1_4
              chelsea.c "Oh! I don't know, but I can't wait to find out."
              wt_image chubby_gf_youth_1_24
              "She pulls off her panties and climbs on top of you.  Gripping your cock in her hand, she rubs it back and forth along her sex until she's wet enough to get it inside her."
              wt_image chubby_gf_youth_1_36
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_1_37
              "After a few rides up and down your shaft, she goes from wet to sopping wet, taking you deeper and deeper inside her on each down-thrust."
              chelsea.c "This feels so good, [chelsea.your_name]!"
              if chelsea.anal_status > 3:
                $ title = "Tell her to finger her ass?"
                menu:
                  "Yes":
                    wt_image chubby_gf_youth_1_25
                    player.c "Reach back and put a finger in your ass."
                    if chelsea.anal_status == 4:
                      chelsea.c "What?  Why??"
                      player.c "Because it'll turn me on to see you do that.  Don't worry, it won't hurt."
                      wt_image chubby_gf_youth_1_26
                      "Hesitantly, she reaches back until she finds the opening of her butt with one of her fingers, and slowly pushes it inside."
                      call chelsea_anal_fingering from _call_chelsea_anal_fingering_5
                    else:
                      wt_image chubby_gf_youth_1_26
                      "[chelsea.name]'s become used to you wanting to see her play with her ass. She doesn't argue, just reaches back and shoves a finger up her butt."
                    wt_image chubby_gf_youth_1_27
                    "You enjoy the view until you're almost ready to cum, then you let her remove her finger and focus on her own arousal."
                    wt_image chubby_gf_youth_1_38
                    chelsea.c "Ahhhh"
                  "Not today":
                    wt_image chubby_gf_youth_1_38
                    "After a few more strokes she starts rubbing her clit, and keeps rubbing until she brings first herself, then you to climax."
                    chelsea.c "Ahhhhh"
              else:
                wt_image chubby_gf_youth_1_38
                "After a few more strokes she starts rubbing her clit, and keeps rubbing until she brings first herself, then you to climax."
                chelsea.c "Ahhhhh"
              wt_image chubby_gf_youth_1_39
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_youth_1_40
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_1_4
              chelsea.c "Guess I'll get back to work, now.  Thanks for the fun diversion, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Fuck her on her back":
              player.c "You look respectable now, but how respectable are you going to look lying on your back with your legs spread and my cock inside you?"
              wt_image chubby_gf_youth_1_4
              chelsea.c "Oh! I don't know, but I can't wait to find out."
              wt_image chubby_gf_youth_1_41
              "She pulls off her panties and lies down as you spread her legs and place the head of your cock against her sex.  You rub your cock up and down along her slit until she's wet enough for penetration."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_1_28
              "After a few hard thrusts, she goes from wet to sopping wet, and begins to pinch her own nipples in excitement."
              chelsea.c "Ahhhhh"
              wt_image chubby_gf_youth_1_42
              "Soon she drops her hands from her nipples to between her legs, and rubs her clit until she cums, bringing you along with her."
              wt_image chubby_gf_youth_1_30
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_youth_1_29
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_1_4
              chelsea.c "Guess I'll get back to work, now.  Thanks for the fun diversion, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Just a strip tease":
              player.c "You're right.  That is a perfectly respectable outfit.  Too respectable for sitting around the house."
              chelsea.c "You don't want me to be respectable around the house?"
              player.c "Not when I'm the only one who can see you."
              wt_image chubby_gf_youth_1_4
              chelsea.c "Hmmm, I guess I better get this off, then."
              wt_image chubby_gf_youth_1_7
              "She removes her sweater and pulls down her top."
              chelsea.c "Is this better?"
              wt_image chubby_gf_youth_1_43
              player.c "Better, but that skirt is still very respectable."
              wt_image chubby_gf_youth_1_8
              chelsea.c "What if I take the skirt off?"
              wt_image chubby_gf_youth_1_9
              chelsea.c "Does your little girl look better now?"
              player.c "I think you would if you weren't wearing those panties."
              wt_image chubby_gf_youth_1_10
              chelsea.c "Okay, I'll take them off, too."
              wt_image chubby_gf_youth_1_11
              chelsea.c "But now I'm completely naked.  Do you really want to see me naked?"
              $ title = "Do you?"
              menu:
                "Yes":
                  wt_image chubby_gf_youth_1_12
                  chelsea.c "Okay, here I am!"
                  "So she is. After a good look at her, you let her to get back to her work and you go on with your day."
                "No, this is good enough":
                  player.c "Actually, you look so cute right now, I think you should stay like that."
                  chelsea.c "Thanks, [chelsea.name]!  But I will need to get back to my work in a little while."
              $ chelsea.stripped_count += 1
              change player energy by -energy_very_short notify
        "Let her work":
          "This looks like something she needs to get done. You leave her to her work.  You can catch up with her another day."
          $ chelsea.visit_count -= 1 # to offset gain, later
    else:
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_bbw_1_12
        "A glazy eyed [chelsea.name] is sprawled out on the sofa watching TV."
        player.c "Tough day?"
        chelsea.c "Yes.  Watching TV now."
        $ title = "What do you do?"
        menu:
          "Let her veg":
            wt_image chubby_gf_bbw_1_13
            "She looks tired. You leave her alone with her show. When you pass by later, you see she's fallen asleep."
            $ title = "What now?"
            menu:
              "Wake her up for a quickie":
                wt_image chubby_gf_bbw_1_35
                player.c "Wakey wakey, sleepy head."
                wt_image chubby_gf_bbw_1_14
                "Snuggling in beside her, you run your fingers across her nipple, startling her awake."
                chelsea.c "Oh!  How long have I been asleep?"
                wt_image chubby_gf_bbw_1_36
                player.c "Long enough for me to get horny."
                wt_image chubby_gf_bbw_1_21
                chelsea.c "Ha!  That wouldn't have to be long."
                wt_image chubby_gf_bbw_1_15
                player.c "Look who's talking, Ms-already-wetting-her-panties."
                "[chelsea.name] moans as you stroke her sex.  Reaching back, she takes out your cock and strokes it hard."
                chelsea.c "Ahhhh  ...  What can I say, [chelsea.your_name]?  I love your big dick."
                wt_image chubby_gf_bbw_1_16
                player.c "Who am I to deny you what you love?"
                "Rolling her over onto her back, you pull off her panties ..."
                wt_image chubby_gf_bbw_1_17
                "... and sink your dick inside her."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_bbw_1_18
                player.c "And to think I almost let you sleep.  Aren't you glad I woke you up?"
                chelsea.c "Ahhhhh  ...  Yes!"
                wt_image chubby_gf_bbw_1_19
                "She shows exactly how glad she is a moment later, shuddering to orgasm while impaled on your big dick."
                chelsea.c "Aahhhhhh"
                player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Let her sleep":
                "You let her get caught up on her rest, making a mental note to remind her later to either cut back on her hours at work or start going to bed earlier."
                $ chelsea.temporary_count = 0
          "Interrupt her":
            wt_image chubby_gf_bbw_1_1
            player.c "Put the remote down for a minute."
            chelsea.c "Hey, no, I was watching that!"
            wt_image chubby_gf_bbw_1_34
            "As you wrestle the remote away from her, [chelsea.name] tumbles down onto the floor."
            wt_image chubby_gf_bbw_1_2
            "She scrambles back up onto her knees at your feet, she smiles up at you with a twinkle in her eye."
            player.c "Oh, you think that's going to get you what you want, do you?"
            $ title = "What do you want?"
            menu:
              "Tit job":
                wt_image chubby_gf_bbw_1_45
                player.c "Maybe if you weren't wearing so many clothes, you might be able to convince me to let you go back to watching TV."
                wt_image chubby_gf_bbw_1_9
                chelsea.c "You mean like this?"
                wt_image chubby_gf_bbw_1_7
                player.c "That's a good start, but your interesting parts are still too covered up."
                wt_image chubby_gf_bbw_1_37
                chelsea.c "Are these the parts of me you're interested in?"
                player.c "Those are the ones.  You can lie back on the sofa now."
                wt_image chubby_gf_bbw_1_23
                chelsea.c "I can't see the TV like this."
                wt_image chubby_gf_bbw_1_38
                player.c "Hopefully you find this more interesting that watching TV.  I know I will."
                wt_image chubby_gf_bbw_1_22
                "[chelsea.name] presses her soft tits firmly around your cock as you fuck them."
                wt_image chubby_gf_bbw_1_4
                chelsea.c "You're right, this is more fun than watching my show."
                player.c "Just wait, we're about to come to the best part."
                wt_image chubby_gf_bbw_1_39
                player.c "[player.orgasm_text]"
                $ chelsea.titfuck_count += 1
                orgasm notify
              "Blow job":
                wt_image chubby_gf_bbw_1_40
                player.c "I suppose since you're down there, you could make yourself useful."
                wt_image chubby_gf_bbw_1_24
                chelsea.c "You mean like this?"
                "She removes your cock and gives it a kiss."
                wt_image chubby_gf_bbw_1_20
                chelsea.c "If you move over a little, I can do this properly."
                wt_image chubby_gf_bbw_1_26
                "What she's doing already feels plenty good to you, but you move over and she climbs up on the sofa beside you."
                wt_image chubby_gf_bbw_1_25
                "It's only later you realize this position lets her keep watching her show while she blows you.  Not that you care, as she still provides your dick plenty of attention ..."
                wt_image chubby_gf_bbw_1_41
                "... including swallowing every drop of sperm you empty into her mouth when you cum."
                wt_image chubby_gf_bbw_1_5
                player.c "[player.orgasm_text]"
                $ chelsea.blowjob_count += 1
                $ chelsea.swallow_count += 1
                orgasm notify
              "Fuck her":
                wt_image chubby_gf_bbw_1_3
                player.c "Get out of those clothes and get back up here on the sofa. I'm going to fuck you from behind."
                wt_image chubby_gf_bbw_1_6
                "You need to warm her up before you can enter her, but that doesn't take too long.  A few strokes of your hard cock along her slit and she's soon wet enough for penetration."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_bbw_1_27
                "After a few hard thrusts, she goes from wet to sopping wet.  Reaching a hand back, she opens herself up more, giving you better access so you can fuck her even harder."
                chelsea.c "Ahhhhh"
                if chelsea.anal_status > 3:
                  player.c "Don't stop there."
                  chelsea.c "Wh .. what?"
                  player.c "Your hand. Don't stop there. Reach back and put a finger in your ass."
                  if chelsea.anal_status == 4:
                    chelsea.c "Wh ... why?"
                    player.c "Because it'll turn me on to see you do that.  Don't worry.  It won't hurt."
                    wt_image chubby_anal_finger_1
                    "Hesitantly, she reaches back until she finds the opening of her butt with one of her fingers, and slowly pushes it inside."
                    call chelsea_anal_fingering from _call_chelsea_anal_fingering_6
                  else:
                    wt_image chubby_anal_finger_1
                    "[chelsea.name]'s become used to you wanting to see her play with her ass.  She doesn't argue, just reaches back and shoves a finger up her butt."
                wt_image chubby_gf_bbw_1_28
                "After that, a few more thrusts takes you both over the edge."
                chelsea.c "Aahhhhhh"
                player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Pleasure her":
                player.c "I know something you'll enjoy more than watching that show."
                wt_image chubby_gf_bbw_1_44
                chelsea.c "What's that?"
                player.c "Come here and I'll show you."
                wt_image chubby_gf_bbw_1_29
                "As she gets up and sits beside you, you kiss her, cupping her breast in your hand."
                wt_image chubby_gf_bbw_1_30
                "Breaking the kiss, you take her nipple into your mouth, nibbling it gently as she moans."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_bbw_1_31
                "A few minutes later, she's naked except for her panties, which she holds to one side to allow access for your tongue."
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_bbw_1_32
                "She tries her best to make this last, but your tongue gently tracing across her clit and labia is too much, and she soon trembles to a fast, intense orgasm."
                chelsea.c "Aahhhhhhh"
                wt_image chubby_gf_bbw_1_33
                player.c "You can go back to watching your show now."
                wt_image chubby_gf_bbw_1_46
                chelsea.c "Mmmm.  Or I could lie here and just enjoy this feeling in my pussy for the next five days."
                $ chelsea.pleasure_her_count += 1
                $ chelsea.orgasm_count += 1
                change player energy by -energy_short notify
              "Talk":
                wt_image chubby_gf_bbw_1_40
                chelsea.c "Really?  You just want to talk, with me on the floor in front of you like this?"
                player.c "Not quite like that.  No."
                wt_image chubby_gf_bbw_1_7
                chelsea.c "Oh this is real mature. You sit on the sofa fully clothed and I'm supposed to talk with you on my knees in just my underwear?"
                "Despite her words, she enjoys your attention, and you both know it. If you bring her to your bed tonight, she'll be wet. She'll probably be wet every minute between now and then."
                change player energy by -energy_very_short notify
      else:
        call forced_movement(living_room) from _call_forced_movement_220
        wt_image current_location.image
        "[chelsea.name] hasn't returned from work yet, so you wait and watch some TV while you wait for her.  She appears a few minutes later."
        wt_image chubby_visit_toned_2_36
        player.c "Hi, [chelsea.name].  Care to do something together?"
        wt_image chubby_visit_toned_2_67
        chelsea.c "Not watch TV, if that's what you had in mind.  I've been sitting at a desk all morning, I need to get a workout in."
        wt_image chubby_visit_toned_2_32
        "Her hand on your crotch makes it clear what type of 'workout' she has in mind."
        $ title = "What do you have in mind?"
        menu:
          "Blow job":
            wt_image chubby_visit_toned_2_33
            player.c "How about I lie here and watch TV, and you get some exercise blowing me."
            wt_image chubby_visit_toned_2_68
            chelsea.c "That's not much of a workout. I'm liable to end up swallowing as many calories as I burn off."
            player.c "If you want, I could cum on your face, to save you from the extra calories."
            wt_image chubby_visit_toned_2_69
            chelsea.c "You're such a gentleman."
            wt_image chubby_visit_toned_2_18
            "Despite the teasing, [chelsea.name] gives your cock a kiss ..."
            wt_image chubby_visit_toned_2_19
            "... before wrapping her mouth around it ..."
            wt_image chubby_visit_toned_2_48
            "... and using her lips, tongue and hand to give you a thoroughly enjoyable blow job."
            wt_image chubby_visit_toned_2_20
            "... which like all good things must sadly eventually come to an end."
            wt_image chubby_visit_toned_2_5
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image chubby_visit_toned_2_49
                    player.c "[player.orgasm_text]"
                    wt_image chubby_visit_toned_2_47
                    chelsea.c "See!  That's what I was worried about, extra calories.  If you'll excuse me, I need to hit the weights."
                    $ chelsea.swallow_count += 1
                "On her":
                    wt_image chubby_cum_face_1
                    player.c "[player.orgasm_text]"
                    wt_image chubby_gf_toned_3_11
                    player.c "Wow, I really saved you from a lot of unnecessary calories there."
                    chelsea.c "Ha ha.  If you'll excuse me, I need to go wash up, and then hit the weights to burn off some real calories."
                    $ chelsea.facial_count += 1
            player.c "I hope you won't find that as fun as the exercise you just completed."
            chelsea.c "Not as much fun, no, but a bit better work out.  Enjoy the rest of your television show!"
            $ chelsea.blowjob_count += 1
            orgasm notify
          "Fuck her from behind":
            wt_image chubby_visit_toned_2_9
            player.c "Get those clothes off and I'll give you a workout."
            wt_image chubby_visit_toned_2_50
            chelsea.c "Mmmm, sounds good!  Where do you want me?"
            wt_image chubby_visit_toned_2_10
            player.c "On your hands and knees."
            wt_image chubby_visit_toned_2_21
            player.c "Now turn around."
            wt_image chubby_visit_toned_2_58
            "You need to warm her up before you can enter her, but that doesn't take too long.  A few strokes of your hard cock along her slit and she's soon wet enough for penetration."
            wt_image chubby_visit_toned_2_12
            chelsea.c "Ahhhh"
            wt_image chubby_visit_toned_2_59
            "After a few hard thrusts, she goes from wet to sopping wet. Reaching a hand back, she opens herself up more, giving you better access so you can fuck her even harder."
            wt_image chubby_visit_toned_2_60
            chelsea.c "Ahhhhh"
            if chelsea.anal_status > 3:
              $ title = "Tell her to finger her ass?"
              menu:
                "Yes":
                  $ chelsea.temporary_count = 2
                  player.c "Don't stop there."
                  wt_image chubby_visit_toned_2_57
                  chelsea.c "Wh .. what?"
                  player.c "Your hand.  Don't stop there.  Reach back and put a finger in your ass."
                  if chelsea.anal_status == 4:
                    wt_image chubby_visit_toned_2_70
                    chelsea.c "Wh ... why?"
                    player.c "Because it'll turn me on to see you do that.  Don't worry, it won't hurt."
                    wt_image chubby_visit_toned_2_71
                    "Hesitantly, she reaches back until she finds the opening of her butt with one of her fingers, and slowly pushes it inside."
                    wt_image chubby_visit_toned_2_72
                    call chelsea_anal_fingering from _call_chelsea_anal_fingering_7
                  else:
                    wt_image chubby_visit_toned_2_72
                    "[chelsea.name]'s become used to you wanting to see her play with her ass.  She doesn't argue, just reaches back and shoves a finger up her butt."
                    $ chelsea.anal_fingering_count += 1
                "No, not today":
                  pass
            # if didn't put finger in ass
            if chelsea.temporary_count == 1:
              wt_image chubby_visit_toned_2_13
              "After that, a few more hard thrusts take you both over the edge."
            # if did put finger in ass
            else:
              $ chelsea.temporary_count = 1 # back to 1 for energy calcs later
              wt_image chubby_visit_toned_2_71
              "Fucking [chelsea.name] is always fun.  Fucking her while she fingers her own butthole is even more fun"
              wt_image chubby_visit_toned_2_34
              "A few more hard thrusts take you both over the edge."
            wt_image chubby_visit_toned_2_6
            chelsea.c "Aahhhhhh"
            wt_image chubby_visit_toned_2_57
            player.c "[player.orgasm_text]"
            wt_image chubby_visit_toned_2_21
            chelsea.c "Well, that was a fun workout."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
          "Have her ride you":
            player.c "I have an exercise pole you can work out on."
            wt_image chubby_visit_toned_2_68
            chelsea.c "Oh?  Is it this one growing under my hand?  That's my favorite."
            wt_image chubby_visit_toned_2_35
            "She strips out of her clothes and climbs on top of you as you lie on the sofa. Positioning the head of your cock against her sex, she rubs it back and forth along her labia and clit until she's wet enough to get it inside her."
            wt_image chubby_visit_toned_2_7
            "After a few rides up and down your shaft, she goes from wet to sopping wet, taking you deeper and deeper inside you on each stroke ..."
            wt_image chubby_visit_toned_2_22
            "... until she's fully impaled on her shaft."
            wt_image chubby_visit_toned_2_61
            chelsea.c "Ahhhh"
            wt_image chubby_visit_toned_2_62
            "Then she begins to ride you faster."
            wt_image chubby_visit_toned_2_23
            "She must be enjoying this, as she plays with herself ..."
            wt_image chubby_visit_toned_2_63
            "... before spinning around ..."
            wt_image chubby_visit_toned_2_64
            "... and continuing to bounce up and down on your cock."
            wt_image chubby_visit_toned_2_8
            "She seems intent on making this a good workout, as she pounds into you faster and faster ..."
            wt_image chubby_visit_toned_2_24
            "... until you both cum."
            wt_image chubby_visit_toned_2_25
            chelsea.c "Aahhhhhh"
            wt_image chubby_visit_toned_2_65
            player.c "[player.orgasm_text]"
            wt_image chubby_visit_toned_2_66
            chelsea.c "Mmmm, that was good for my legs."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
          "Fuck her on her back":
            wt_image chubby_visit_toned_2_9
            player.c "Get those clothes off and I'll give you a workout."
            wt_image chubby_visit_toned_2_14
            chelsea.c "Mmmm, sounds good!"
            wt_image chubby_visit_toned_2_26
            chelsea.c "Where do you want me?"
            wt_image chubby_visit_toned_2_27
            player.c "On your back with your legs spread."
            wt_image chubby_visit_toned_2_28
            "You need to warm her up before you can enter her, but that doesn't take too long. A few strokes of your hard cock along her slit and she's soon wet enough for penetration."
            wt_image chubby_visit_toned_2_51
            chelsea.c "Ahhhh"
            wt_image chubby_visit_toned_2_53
            "After a few hard thrusts, she goes from wet to sopping wet. Reaching a hand down, she rubs her clit as you fuck her even harder."
            wt_image chubby_visit_toned_2_54
            "After that, a few more thrusts takes you both over the edge."
            wt_image chubby_visit_toned_2_55
            chelsea.c "Aahhhhhh"
            wt_image chubby_visit_toned_2_56
            player.c "[player.orgasm_text]"
            wt_image chubby_visit_toned_2_29
            chelsea.c "That wasn't much of a workout, being flat on my back like that, but it was fun!"
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
          "She work out while you watch":
            wt_image chubby_visit_toned_2_33
            player.c "In that case, why don't you exercise and I'll watch you."
            chelsea.c "How will that be fun?"
            wt_image chubby_visit_toned_2_40
            player.c "It'll be fun for me, and you'll get your workout in."
            wt_image chubby_exercise_gf_1_1
            "[chelsea.name] changes out of her work clothes and into her exercise duds.  She seems surprised when you join her."
            wt_image chubby_exercise_gf_1_8
            chelsea.c "You're really going to watch me work out?"
            wt_image chubby_exercise_gf_1_2
            chelsea.c "I can't imagine this is too exciting for you."
            player.c "You could make it more exciting."
            wt_image chubby_exercise_gf_1_9
            chelsea.c "How?"
            player.c "Pull down your top."
            wt_image chubby_exercise_gf_1_10
            chelsea.c "You want to watch my boobs get sweaty while I work out?"
            wt_image chubby_exercise_gf_1_3
            player.c "Not just your boobs. Turn around."
            wt_image chubby_exercise_gf_1_4
            chelsea.c "Why? I'm not going to sweat so much that you can see my bum through these gym pants."
            player.c "There's an easy solution for that."
            wt_image chubby_exercise_gf_1_5
            chelsea.c "You want me completely naked?"
            player.c "Almost always."
            wt_image chubby_exercise_gf_1_7
            chelsea.c "Even for working out?"
            player.c "Why not?"
            wt_image chubby_exercise_gf_1_6
            chelsea.c "I'm not in as a good a shape as I should be. I still struggle to keep the weight off, and working a desk job doesn't help."
            player.c "You look pretty good to me."
            wt_image chubby_exercise_gf_1_11
            chelsea.c "Thanks!"
            player.c "Now hit those weights."
            wt_image chubby_exercise_gf_1_12
            chelsea.c "Aye aye, boss!"
            "You spend the next hour with her, complimenting her as she works out. Spending time with you like this gives her motivation to keep up her exercise routine, and makes her feel like you really care about her - and enjoy her body."
            $ chelsea.exercise_count += 1
            change player energy by -energy_short notify
    call character_location_return(chelsea) from _call_character_location_return_38
  # bedroom
  if chelsea.gf_outfit == 7:
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_youth_5_1
      chelsea.c "Hi, [chelsea.your_name].  You were looking for me?"
    else:
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_bbw_5_1
        chelsea.c "Hi, [chelsea.your_name].  Did you want to join me on the bed?"
      else:
        wt_image chubby_gf_toned_1_1
        chelsea.c "Hi, [chelsea.your_name].  You were looking for me?"
    $ title = "What do you want to do with her?"
    menu:
      "Just talk":
        if chelsea.has_tag('little_girl'):
          wt_image chubby_gf_youth_5_2
          chelsea.c "Really?  You just came by to talk with your little girl?  How sweet."
          "You both enjoy your time together catching up."
          change player energy by -energy_very_short notify
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_5_2
            chelsea.c "Really?  I was hoping you were here to fuck me."
            $ title = "What do you want to do with her?"
            menu:
              "Fuck her":
                wt_image chubby_gf_bbw_5_3
                chelsea.c "That's what I was hoping you'd say."
                wt_image chubby_gf_bbw_5_5
                "[chelsea.name] makes herself available to you on the bed, and you happily plunge inside."
                wt_image chubby_gf_bbw_5_16
                chelsea.c "Ahhhh"
                wt_image chubby_gf_bbw_5_8
                "Reaching a hand down, [chelsea.name] rubs her clit as you fuck her ..."
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_bbw_5_26
                "... bringing herself to orgasm just before you reach yours."
                wt_image chubby_gf_bbw_5_9
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_bbw_5_7
                player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Just talk":
                wt_image chubby_gf_bbw_5_29
                "[chelsea.name] pretends to pout a little at first, but you both enjoy your time together catching up."
                change player energy by -energy_very_short notify
          else:
            wt_image chubby_gf_toned_1_2
            chelsea.c "Really? I was hoping you were here to fuck me."
            $ title = "What do you want to do with her?"
            menu:
              "Fuck her":
                wt_image chubby_gf_toned_1_21
                chelsea.c "That's what I was hoping you'd say"
                wt_image chubby_gf_toned_1_26
                "[chelsea.name] climbs up onto on the bed, making herself available to you ..."
                wt_image chubby_gf_toned_1_27
                "... and you happily plunge inside."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_toned_1_14
                if chelsea.dominate_status == 8:
                  $ title = "Dominate her?"
                  menu:
                    "Yes":
                      $ chelsea.temporary_count = 2
                    "Not today":
                      pass
                if chelsea.temporary_count == 2:
                  $ chelsea.temporary_count = 1
                  wt_image chubby_gf_toned_1_28
                  "Gripping her firmly by the hair, you slam yourself into her roughly."
                  player.c "Cum for me, fucktoy.  Cum while I fuck you."
                  wt_image chubby_gf_toned_1_29
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_toned_1_27
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_toned_1_28
                  "Once in a while, at times like this, she doesn't mind being used as your fucktoy."
                else:
                  "This isn't always the easiest position for her to cum in, but she manages ..."
                  wt_image chubby_gf_toned_1_10
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_toned_1_14
                  "... as do you."
                  wt_image chubby_gf_toned_1_27
                  player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Just talk":
                wt_image chubby_gf_toned_1_21
                "[chelsea.name] pretends to pout a little at first, but you both enjoy your time together catching up."
                change player energy by -energy_very_short notify
      "Ask her to strip":
        if chelsea.has_tag('little_girl'):
          wt_image chubby_gf_youth_5_3
          chelsea.c "A show?  I don't know if I'll be any good at that, [chelsea.your_name]."
          wt_image chubby_anal_youth_1_10
          chelsea.c "Do I just pull my sweater off?"
          wt_image chubby_gf_youth_5_4
          chelsea.c "And my training bra, too?"
          player.c "If that's your training bra, I can't imagine what cup size you'll need when you're a big girl."
          wt_image chubby_anal_youth_1_9
          chelsea.c "[chelsea.your_name]! Don't tease. You know I've developed early.  What am I supposed to do now?"
          wt_image chubby_gf_youth_5_5
          chelsea.c "If I pull down my pants, all I'll have on are my panties."
          wt_image chubby_gf_youth_5_6
          chelsea.c "And if I pull those aside, you'll be able to see all of me.  Is that the kind of show you were hoping for?"
          wt_image chubby_gf_youth_5_7
          "She runs off giggling before you can answer, seemingly pleased with herself, and with you for taking an interest in her body."
          $ chelsea.stripped_count += 1
          change player energy by -energy_very_short notify
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_5_2
            "[chelsea.name] looks a little shy at first."
            chelsea.c "You want me to put on a show for you?"
            wt_image chubby_gf_bbw_5_3
            chelsea.c "Like this?"
            wt_image chubby_gf_bbw_5_4
            chelsea.c "Or more like this?"
            wt_image chubby_gf_bbw_5_5
            chelsea.c "Or was it something more like this you were hoping to see?"
            wt_image chubby_gf_bbw_5_6
            "[chelsea.name] pulls her panties aside, exposing her sex. Then she looks up at you, seeking approval."
            $ chelsea.stripped_count += 1
            $ title = "What do you do now?"
            menu:
              "Fuck her":
                chelsea.c "That's what I was hoping you'd say."
                wt_image chubby_gf_bbw_5_16
                "[chelsea.name]'s happy when you plunge inside her."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_bbw_5_8
                "Reaching a hand down, she rubs her clit as you fuck her ..."
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_bbw_5_26
                "... bringing herself to orgasm just before you reach yours."
                wt_image chubby_gf_bbw_5_9
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_bbw_5_7
                player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Thank her for the show":
                wt_image chubby_gf_bbw_5_3
                player.c "Thanks, [chelsea.name]. That's exactly what I was hoping to see."
                wt_image chubby_gf_bbw_5_4
                "She giggles at you, pleased that you enjoyed looking at her body, and gets herself re-dressed."
                change player energy by -energy_very_short notify
          else:
            wt_image chubby_gf_toned_1_2
            "[chelsea.name] looks a little shy at first when you ask her to put on a show for you."
            wt_image chubby_gf_toned_1_3
            chelsea.c "Like this?"
            wt_image chubby_gf_toned_1_4
            chelsea.c "Or more like this?"
            wt_image chubby_gf_toned_1_5
            chelsea.c "Or was it something more like this you were hoping to see?"
            wt_image chubby_gf_toned_1_6
            "She sits up and grins at you."
            $ chelsea.stripped_count += 1
            $ title = "What do you do now?"
            menu:
              "Fuck her":
                wt_image chubby_gf_toned_1_26
                "[chelsea.name] climbs up onto on the bed, making herself available to you ..."
                wt_image chubby_gf_toned_1_27
                "... and you happily plunge inside."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_toned_1_14
                if chelsea.dominate_status == 8:
                  $ title = "Dominate her?"
                  menu:
                    "Yes":
                      $ chelsea.temporary_count = 2
                    "Not today":
                      pass
                if chelsea.temporary_count == 2:
                  $ chelsea.temporary_count = 1
                  wt_image chubby_gf_toned_1_28
                  "Gripping her firmly by the hair, you slam yourself into her roughly."
                  player.c "Cum for me, fucktoy.  Cum while I fuck you."
                  wt_image chubby_gf_toned_1_29
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_toned_1_27
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_toned_1_28
                  "Once in a while, at times like this, she doesn't mind being used as your fucktoy."
                else:
                  "This isn't always the easiest position for her to cum in, but she manages ..."
                  wt_image chubby_gf_toned_1_10
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_toned_1_14
                  "... as do you."
                  wt_image chubby_gf_toned_1_27
                  player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Thank her for the show":
                wt_image chubby_gf_toned_1_22
                player.c "Thanks, [chelsea.name]. That's exactly what I was hoping to see."
                wt_image chubby_gf_toned_1_21
                "She giggles at you, pleased that you enjoyed looking at her body, and gets herself re-dressed."
                change player energy by -energy_very_short notify
      "Tit job" if not chelsea.has_tag('bbw'):
        if chelsea.has_tag('little_girl'):
          wt_image chubby_anal_youth_1_10
          chelsea.c "Really?"
          wt_image chubby_gf_youth_5_8
          chelsea.c "Are my titties interesting enough that you want to put your dick between them, [chelsea.your_name]?"
          wt_image chubby_gf_youth_5_9
          player.c "Yes, [chelsea.name], they are."
          wt_image chubby_gf_youth_5_10
          "In case she was wondering if you were telling the truth, you leave no doubt."
          player.c "[player.orgasm_text]"
          wt_image chubby_gf_youth_5_11
          chelsea.c "Mmmmm.  I'm glad you like my boobies, [chelsea.your_name]."
        else:
          if chelsea.has_tag('toned'):
            wt_image chubby_gf_toned_1_23
            chelsea.c "Really?"
            wt_image chubby_gf_toned_1_8
            chelsea.c "You're still not tired of fucking my tits?"
            wt_image chubby_gf_toned_1_16
            player.c "No, not really."
            wt_image chubby_gf_toned_1_24
            "In case she was wondering if you were telling the truth ..."
            wt_image chubby_gf_toned_1_7
            "... you leave no doubt."
            wt_image chubby_cum_tits_3
            player.c "[player.orgasm_text]"
        $ chelsea.titfuck_count += 1
        orgasm notify
      "Blow job":
        if chelsea.has_tag('little_girl'):
          wt_image chubby_gf_youth_5_21
          chelsea.c "I can do that for you, [chelsea.your_name]."
          wt_image chubby_gf_youth_5_12
          "[chelsea.name] drops to her knees in front of you and takes off your pants."
          wt_image chubby_gf_youth_5_13
          "Taking your dick in her soft hand, she strokes it hard ..."
          wt_image chubby_gf_youth_5_14
          "... and licks the head of it ..."
          wt_image chubby_gf_youth_5_15
          "... before sucking on it, something she does very well, indeed."
          wt_image chubby_gf_youth_5_14
          $ title = "Where do you want to cum?"
          menu:
            "In her":
              wt_image chubby_gf_youth_5_16
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_5_14
              chelsea.c "I swallowed it all, [chelsea.your_name]."
              $ chelsea.swallow_count += 1
            "On her":
              wt_image chubby_gf_youth_5_23
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_5_24
              chelsea.c "That was a lot of cum, [chelsea.your_name].  I guess that means you like my blow job."
              $ chelsea.facial_count += 1
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_5_3
            chelsea.c "I suppose I won't say 'no' to that."
            wt_image chubby_gf_bbw_5_10
            "She takes out your cock and begins to lick it."
            $ title = "Let her blow you like this?"
            menu:
              "Yes":
                wt_image chubby_gf_bbw_5_17
                "[chelsea.name] lovingly sucks your cock ..."
                wt_image chubby_gf_bbw_5_18
                "... until you fill her mouth with jizz."
              "No, throat fuck her":
                wt_image chubby_gf_bbw_5_17
                player.c "What would you say to rolling over?"
                wt_image chubby_gf_bbw_5_11
                "She's confused about what you mean until you get her into position, then she opens her mouth and lets you fuck it."
                wt_image chubby_gf_bbw_5_19
                "With her head hanging over the edge of the bed like this, you can fuck her face like it's her pussy, your cock lodging deeper and deeper into the back of her throat each thrust."
                wt_image chubby_gf_bbw_5_20
                "Surprisingly, she doesn't gag, not even when you release your load and she needs to gulp rapidly to swallow the jizz your balls pump into her."
            player.c "[player.orgasm_text]"
            $ chelsea.swallow_count += 1
          else:
            wt_image chubby_gf_toned_1_17
            chelsea.c "I suppose I could do that for you."
            wt_image chubby_gf_toned_1_18
            "[chelsea.name] removes her robe as she kneels at your feet ..."
            wt_image chubby_gf_toned_1_25
            "... then attends to your dick, using her lips, tongue and hand to get you off."
            wt_image chubby_gf_toned_1_19
            $ title = "Where do you want to cum?"
            menu:
              "In her":
                wt_image chubby_gf_event_5_16
                $ chelsea.swallow_count += 1
              "On her":
                wt_image chubby_gf_toned_1_20
                $ chelsea.facial_count += 1
            player.c "[player.orgasm_text]"
        $ chelsea.blowjob_count += 1
        orgasm notify
      "Fuck her" if not chelsea.has_tag('little_girl'):
        if chelsea.has_tag('bbw'):
          wt_image chubby_gf_bbw_5_3
          chelsea.c "That's what I was hoping you'd say."
          wt_image chubby_gf_bbw_5_5
          "[chelsea.name] makes herself available to you on the bed, and you happily plunge inside."
          wt_image chubby_gf_bbw_5_16
          chelsea.c "Ahhhh"
          wt_image chubby_gf_bbw_5_8
          "Reaching a hand down, [chelsea.name] rubs her clit as you fuck her ..."
          chelsea.c "Ahhhhh"
          wt_image chubby_gf_bbw_5_26
          "... bringing herself to orgasm just before you reach yours."
          wt_image chubby_gf_bbw_5_9
          chelsea.c "Aahhhhhh"
          wt_image chubby_gf_bbw_5_7
          player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
        else:
          wt_image chubby_gf_toned_1_21
          chelsea.c "That's what I was hoping you'd say."
          wt_image chubby_gf_toned_1_26
          "[chelsea.name] climbs up onto on the bed, making herself available to you ..."
          wt_image chubby_gf_toned_1_27
          "... and you happily plunge inside."
          chelsea.c "Ahhhh"
          wt_image chubby_gf_toned_1_14
          if chelsea.dominate_status == 8:
            $ title = "Dominate her?"
            menu:
              "Yes":
                $ chelsea.temporary_count = 2
              "Not today":
                pass
          if chelsea.temporary_count == 2:
            $ chelsea.temporary_count = 1
            wt_image chubby_gf_toned_1_28
            "Gripping her firmly by the hair, you slam yourself into her roughly."
            player.c "Cum for me, fucktoy.  Cum while I fuck you."
            wt_image chubby_gf_toned_1_29
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_toned_1_27
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_toned_1_28
            "Once in a while, at times like this, she doesn't mind being used as your fucktoy."
          else:
            "This isn't always the easiest position for her to cum in, but she manages ..."
            wt_image chubby_gf_toned_1_10
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_toned_1_14
            "... as do you."
            wt_image chubby_gf_toned_1_27
            player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          orgasm notify
      "Have her ride you" if not chelsea.has_tag('little_girl'):
        if chelsea.has_tag('bbw'):
          wt_image chubby_gf_bbw_5_12
          "[chelsea.name] groans as you pull her up on top of you and slide into her.  She's already wet, making the entrance easy."
          chelsea.c "Ahhhh"
          if chelsea.anal_status > 3:
            $ title = "Tell her to finger her ass?"
            menu:
              "Yes":
                $ chelsea.temporary_count = 2
                wt_image chubby_gf_bbw_5_21
                chelsea.c "What?  Why??  You won't even be able to see it's there."
                player.c "I'll know it's there, and it'll excite me."
                if chelsea.anal_status == 4:
                  chelsea.c "But that's ..."
                  player.c "Something I want you to do for me.  It won't hurt.  Just take it nice and slow."
                  wt_image chubby_gf_bbw_5_22
                  call chelsea_anal_fingering from _call_chelsea_anal_fingering_2
                  "To reinforce for her how much you like this, you cum inside her as she fingers herself."
                else:
                  wt_image chubby_gf_bbw_5_22
                  "[chelsea.name]'s become used to your fascination with her ass.  Slowly she inserts a finger up her butt.  It does nothing for her, but it gets you off."
                  $ chelsea.anal_fingering_count += 1
              "No, not today":
                pass
          if chelsea.temporary_count == 1:
            wt_image chubby_gf_bbw_5_24
            "After a few rides up-and-down your shaft, she spins around to her preferred orientation to cum in ..."
            wt_image chubby_gf_bbw_5_13
            chelsea.c "Ahhhhh"
            wt_image chubby_gf_bbw_5_23
            "... something she does soon after."
            wt_image chubby_gf_bbw_5_25
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_bbw_5_14
            $ chelsea.orgasm_count += 1
          else:
            $ chelsea.temporary_count = 1
          player.c "[player.orgasm_text]"
        else:
          wt_image chubby_gf_toned_1_21
          chelsea.c "Gladly!"
          wt_image chubby_gf_toned_1_30
          "[chelsea.name] climbs on top of you and lowers herself carefully onto your waiting shaft."
          if chelsea.dominate_status == 8:
            $ title = "Dominate her?"
            menu:
              "Yes":
                $ chelsea.temporary_count = 2
              "Not today":
                pass
          if chelsea.temporary_count == 2:
            $ chelsea.temporary_count = 1
            wt_image chubby_gf_toned_1_31
            "You bring both hands down sharply on her ass, and she yelps in surprise ... *SMACK*"
            chelsea.c "Ow!!"
            player.c "Ride me, fucktoy."
            wt_image chubby_gf_toned_1_13
            "She does so, bucking her hips up-and-down your cock as you spank her ... *smack*  *smack*  *smack*"
            wt_image chubby_gf_toned_1_32
            "... until, punctuated with a sudden sharp slap, she suddenly shudders to climax, bringing you with her ... *SMACK*"
            chelsea.c "Aahhhhhh"
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_toned_1_30
            "Once in a while, at times like this, she doesn't mind being used as your fucktoy."
          else:
            wt_image chubby_gf_toned_1_33
            chelsea.c "Ahhhh"
            wt_image chubby_gf_toned_1_34
            "After a few rides up-and-down your shaft ..."
            wt_image chubby_gf_toned_1_35
            "... she spins around to her preferred orientation ..."
            wt_image chubby_gf_toned_1_36
            "... and rides you up-and-down even faster."
            wt_image chubby_gf_toned_1_11
            chelsea.c "Ahhhhh"
            wt_image chubby_gf_toned_1_37
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_toned_1_38
            player.c "[player.orgasm_text]"
          $ chelsea.orgasm_count += 1
        $ chelsea.sex_count += 1
        orgasm notify
      "Pleasure her" if chelsea.has_tag('little_girl') or chelsea.has_tag('bbw'):
        if chelsea.has_tag('little_girl'):
          wt_image chubby_anal_youth_1_4
          chelsea.c "You want me to take off my pants?  Okay, [chelsea.your_name].  But what happens then?"
          wt_image chubby_gf_youth_5_17
          "What happens then is she starts to moan even before your mouth touches her ..."
          chelsea.c "Ahhhh"
          wt_image chubby_gf_youth_5_22
          "... and when you start licking her she moans even louder, the juices flowing freely from her pussy."
          chelsea.c "Ahhhhh"
          wt_image chubby_gf_youth_5_18
          "After a few minutes of tongue lapping, her whole body tenses up."
          wt_image chubby_gf_youth_5_19
          chelsea.c "Oh, [chelsea.your_name]!  I'm going to  ..."
          wt_image chubby_gf_youth_5_20
          chelsea.c "Nnnnn!!!  ...  Aahhhhhh  ....  Nnnnnnnnnn!!"
          "Presumably 'cum' was how she was going to end that sentence, but it was lost in the sounds exploding from her throat as you press your lips directly on her clit and suck, triggering an orgasm that goes back and forth between intense and almost unbearably intense."
          wt_image chubby_gf_youth_5_22
          "You lick up the remaining juices flowing from her pussy, then let the exhausted girl recover from the experience while you go on with your day."
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_5_5
            player.c "Lie down on the bed and pull your panties aside."
            wt_image chubby_gf_bbw_5_6
            chelsea.c "Are you going to fuck me like this?"
            player.c "Not exactly."
            wt_image chubby_gf_bbw_5_27
            "She bites her lip at the intensity of the sensation as your wet tongue contacts her sex."
            wt_image chubby_gf_bbw_5_15
            "After a few minutes of tongue lapping, though, she's moaning loudly."
            chelsea.c "Ahhhhh"
            wt_image chubby_gf_bbw_5_28
            "A moment later, her whole body tenses up and she pulls your head towards her, seeking even more contact as she explodes in an intense orgasm."
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_bbw_5_30
            "You let the exhausted-but-satisfied woman dress and recover from the experience while you go on with your day."
        $ chelsea.pleasure_her_count += 1
        $ chelsea.orgasm_count += 1
        change player energy by -energy_short notify
  # other scenes
  if chelsea.gf_outfit == 8:
    # just leaving if youth
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_youth_4_11
      chelsea.c "Hi!  I was just going outside."
      player.c "To do what?"
      wt_image chubby_gf_youth_4_1
      chelsea.c "Play!"
      $ title = "What do you do?"
      menu:
        "Tell her to play inside with you":
          wt_image chubby_gf_youth_4_12
          chelsea.c "Ummm, what will we do inside, [chelsea.your_name]?"
          player.c "Follow me and I'll show you."
          wt_image chubby_gf_youth_4_14
          "You lead her to the bedroom ..."
          wt_image chubby_gf_youth_4_15
          "... kiss her ..."
          wt_image chubby_gf_youth_4_2
          "... and play with her body while undressing her."
          wt_image chubby_gf_youth_4_16
          chelsea.c "Mmmmm.  This is a fun game, [chelsea.your_name].  What do we do next?"
          $ title = "What do you want?"
          menu:
            "Blow job":
              wt_image chubby_gf_youth_4_3
              "[chelsea.name] happily takes your cock into her mouth ..."
              wt_image chubby_gf_youth_4_4
              "... and sucks you off ..."
              wt_image chubby_gf_youth_4_5
              "... bobbing her pretty head up-and-down your shaft until you're ready to cum."
              wt_image chubby_gf_youth_4_4
              $ title = "Where do you want to cum?"
              menu:
                "In her":
                  wt_image chubby_gf_youth_4_17
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_4_18
                  chelsea.c "Mmmm.  I think you enjoyed our playtime, [chelsea.your_name]."
                  $ chelsea.swallow_count += 1
                "On her":
                  wt_image chubby_cum_face_2
                  player.c "[player.orgasm_text]"
                  chelsea.c "Oh!  I think you enjoyed our playtime, [chelsea.your_name]."
                  $ chelsea.facial_count += 1
              $ chelsea.blowjob_count += 1
              orgasm notify
            "Have her ride you":
              wt_image chubby_gf_youth_4_6
              "[chelsea.name] gasps as you pull her up on top of you and slide into her.  She's already wet, making the entrance easy."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_4_19
              "After a few rides up and down your shaft ..."
              wt_image chubby_gf_youth_4_20
              "... she spins around to her preferred orientation to cum in ..."
              wt_image chubby_gf_youth_4_7
              "... something she does soon after."
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_youth_4_21
              "It doesn't take you much longer."
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_youth_4_8
              chelsea.c "Oh!  I think you enjoyed our playtime, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Fuck her on her back":
              wt_image chubby_gf_youth_4_9
              "[chelsea.name] lies back and helps you guide inside.  She's already wet, making the entrance easy."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_4_10
              $ title = "Kiss her feet as you fuck her?"
              menu:
                "Yes":
                  wt_image chubby_gf_youth_4_22
                  "[chelsea.name] moans as she feels your tongue on her foot."
                  chelsea.c "Ahhhhh"
                  wt_image chubby_gf_youth_4_23
                  "She seems to enjoy the sensation, and so do you."
                "No":
                  wt_image chubby_gf_youth_4_24
                  "In this position, you can pound deep into her.  She seems to enjoy the sensation, and so do you."
              wt_image chubby_gf_youth_4_25
              chelsea.c "Aahhhhhh"
              $ title = "Where do you want to cum?"
              menu:
                "In her":
                  wt_image chubby_gf_youth_4_28
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_4_29
                  chelsea.c "Mmmmm.  I think you enjoyed our playtime, [chelsea.your_name]."
                "On her":
                  wt_image chubby_gf_youth_4_26
                  "As you pull out, [chelsea.name] takes your cock in her hand and pumps your cum up and over her."
                  wt_image chubby_cum_pussy_2
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_4_27
                  chelsea.c "Mmmmm.  I think you enjoyed our playtime, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Fuck her from behind":
              wt_image chubby_gf_youth_4_30
              "[chelsea.name] gasps as gets on all fours and you push into her.  She's already wet, making the entrance easy."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_youth_4_31
              "She bites her lip as you thrust deeper and deeper into her."
              wt_image chubby_gf_youth_4_32
              "Her excitement is building, but it make take her a while to cum in this position."
              $ title = "Wait for her to cum?"
              menu:
                "Yes":
                  wt_image chubby_gf_youth_4_33
                  "Trying hard to think of anything other than how sexy she looks and how good her tight pussy feels on your cock, you continue to fuck her ..."
                  wt_image chubby_gf_youth_4_34
                  "... and are eventually rewarded by the signs of her pending orgasm."
                  wt_image chubby_gf_youth_4_35
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_youth_4_37
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_4_38
                  chelsea.c "Mmmmm.  I think you enjoyed our playtime, [chelsea.your_name].  Thanks for waiting long enough for me to enjoy it, too."
                  $ chelsea.orgasm_count += 1
                "No":
                  wt_image chubby_gf_youth_4_36
                  "She may not be ready to cum, yet, but you soon are."
                  wt_image chubby_gf_youth_4_37
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_youth_4_38
                  chelsea.c "Mmmmm.  I think you enjoyed our playtime, [chelsea.your_name]."
              $ chelsea.sex_count += 1
              orgasm notify
        "Wish her fun":
          wt_image chubby_gf_youth_4_13
          chelsea.c "Thanks, I will.  Bye!"
          $ chelsea.visit_count -= 1 # to offset gain, later
    else:
      # sofa again if bbw
      if chelsea.has_tag('bbw'):
        call forced_movement(living_room) from _call_forced_movement_221
        summon chelsea no_follows
        wt_image chubby_gf_bbw_2_22
        "You find [chelsea.name] on the sofa again.  This time she's not watching TV, she's watching you."
        wt_image chubby_gf_bbw_2_1
        chelsea.c "I was hoping you'd be able to spend some time with me."
        "From the way she's dressed, it's not hard to guess what she's hoping the two of you will do together."
        $ title = "What do you do?"
        menu:
          "Just talk":
            wt_image chubby_gf_bbw_2_22
            "If [chelsea.name]'s disappointed that you only want to talk, she doesn't show it. The two of you enjoy a pleasant time together chatting."
            change player energy by -energy_very_short notify
          "Foot job":
            wt_image chubby_gf_bbw_2_23
            "[chelsea.name] lies back and places her feet around your cock.  She grins as she feels it harden between her soles"
            wt_image chubby_gf_bbw_2_14
            "As her soft feet stroke your shaft, she plays with herself ..."
            wt_image chubby_gf_bbw_2_4
            "... soon bringing both of you to orgasm."
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_bbw_2_24
            player.c "[player.orgasm_text]"
            $ chelsea.orgasm_count += 1
            $ chelsea.footjob_count += 1
            orgasm notify
          "Tit job":
            wt_image chubby_gf_bbw_2_10
            chelsea.c "I love that you never seem to tire of fucking my tits."
            wt_image chubby_gf_bbw_2_2
            "That makes two of you.  Your cock disappears into the valley formed by [chelsea.name]'s massive breasts as she wraps them around you."
            wt_image chubby_gf_bbw_2_26
            "[chelsea.name] groans as you fuck her tits.  She enjoys knowing her body can excite you this much, and it turns her on, even if she won't cum from this.  You, of course, certainly will."
            chelsea.c "Oh"
            wt_image chubby_gf_bbw_2_25
            player.c "[player.orgasm_text]"
            chelsea.c "Mmmmm.  That was fun, [chelsea.your_name]."
            $ chelsea.titfuck_count += 1
            orgasm notify
          "Blow job":
            wt_image chubby_gf_bbw_2_11
            "[chelsea.name] happily takes your cock into her mouth ..."
            wt_image chubby_gf_bbw_2_27
            "... bobbing her head back-and-forth, her soft lips slide along your dick ..."
            wt_image chubby_gf_bbw_2_12
            "... until you're ready to cum."
            $ title = "Where do you want to cum?"
            menu:
              "In her":
                wt_image chubby_gf_bbw_2_3
                $ chelsea.swallow_count += 1
              "On her":
                wt_image chubby_gf_bbw_2_28
                $ chelsea.facial_count += 1
            player.c "[player.orgasm_text]"
            $ chelsea.blowjob_count += 1
            orgasm notify
          "Sex":
            wt_image chubby_gf_bbw_2_5
            "[chelsea.name] gasps as you pull her up on top of you and slide into her.  She's already wet, making the entrance easy."
            chelsea.c "Ahhhh"
            wt_image chubby_gf_bbw_2_6
            "After a few rides up and down your shaft, she tries to turn around, but with your hands on her hips you hold her in place ..."
            wt_image chubby_gf_bbw_2_18
            "... giving you a good look at her as she cums."
            chelsea.c "Aahhhhhh"
            wt_image chubby_gf_bbw_2_29
            player.c "[player.orgasm_text]"
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            orgasm notify
        call character_location_return(chelsea) from _call_character_location_return_39
      # seduction if toned
      else:
        wt_image chubby_gf_toned_2_15
        chelsea.c "Were you looking for me?"
        "[chelsea.name] normally wears a bit more clothing around the house.  You think she knew very well you were looking for her."
        wt_image chubby_gf_toned_2_14
        chelsea.c "You're staring.  Does that mean you like my outfit?"
        wt_image chubby_gf_toned_2_1
        $ title = "How do you reply?"
        menu:
          "I'd like to see a lot less of it":
            wt_image chubby_gf_toned_2_2
            chelsea.c "Really? There's not that much to it as it is."
            wt_image chubby_gf_toned_2_3
            chelsea.c "I guess I could take the bra off."
            wt_image chubby_gf_toned_2_4
            chelsea.c "Is that better?"
            wt_image chubby_gf_toned_2_5
            chelsea.c "Really? You think the panties should come off too?"
            wt_image chubby_gf_toned_2_6
            chelsea.c "There. Are you happier now?"
            $ title = "How do you reply?"
            menu:
              "Much better":
                player.c "Much better. You should stay like that."
                wt_image chubby_gf_toned_2_17
                "[chelsea.name] giggles then runs off.  She doesn't intend to spend the rest of the day with her panties pulled, but the twinkle in her eyes tells you that she enjoyed you suggesting she should."
                if chelsea.has_tag('trigger_implanted'):
                  $ title = "Trigger her?"
                  menu:
                    "Yes":
                      wt_image chubby_gf_toned_2_16
                      player.c "I was serious, [chelsea.name].  [chelsea.trigger_phrase].  I want you to stay like that."
                      wt_image chubby_gf_toned_2_6
                      "[chelsea.name] took the time to dress up for you.  The least you can do is enjoy the view for the remainder of the day."
                      $ chelsea.change_image('chubby_gf_toned_2_6')
                      add tags 'frozen' to chelsea
                    "Not today":
                      pass
              "I'd like to see your tits around my cock":
                call chelsea_gf_action_8_toned_tf from _call_chelsea_gf_action_8_toned_tf
              "I'd like to see your tongue licking my cock":
                call chelsea_gf_action_8_toned_bj from _call_chelsea_gf_action_8_toned_bj
          "I'd like to see your tits around my cock":
            wt_image chubby_gf_toned_2_18
            chelsea.c "I guess this needs to go, then."
            call chelsea_gf_action_8_toned_tf from _call_chelsea_gf_action_8_toned_tf_1
          "I'd like to see your tongue licking my cock":
            wt_image chubby_gf_toned_2_18
            chelsea.c "Hmmm.  I'd better take this off, then.  Sometimes my tongue on your cock ends with things getting messy."
            call chelsea_gf_action_8_toned_bj from _call_chelsea_gf_action_8_toned_bj_1
          "It's lovely (go on with your day)":
            wt_image chubby_gf_toned_2_13
            chelsea.c "Thanks.  I was hoping for a more enthusiastic response to the outfit, but I guess I'll take a compliment when I can get it."
            $ chelsea.visit_count -= 1 # to offset gain, later
  # record if spent time with her
  if chelsea.temporary_count == 1:
    # note: 'trained_today' also increases visit_count in end_day label; visit_count is used in end_week towards relationship maintenance
    $ chelsea.training_session()
    $ chelsea.temporary_count = 0
  return

label chelsea_gf_action_3_youth_get_to_work:
    player.c "Get to work, young lady, and stop teasing me when you don't have time to do anything about it."
    wt_image chubby_gf_youth_3_23
    chelsea.c "Okay, [chelsea.your_name].  I hope you'll be thinking about me while I'm at work.  I know I'll be thinking about you, and that bulge you're sporting in your pants right now."
    sys "[chelsea.name] is happier with your relationship."
    $ chelsea.relationship_counter += 0.5
    $ chelsea.temporary_count = 0
    return

label chelsea_gf_action_3_youth_take_off_shorts:
    player.c "Those shorts are not appropriate to wear to work."
    wt_image chubby_gf_youth_3_3
    chelsea.c "I know!  I'm going to change."
    wt_image chubby_gf_youth_3_25
    player.c "Get on with it, then.  No, you don't need to go back to the bedroom.  Change here."
    wt_image chubby_gf_youth_3_8
    chelsea.c "Okay"
    wt_image chubby_gf_youth_3_9
    "[chelsea.name] wriggles out of the shorts."
    $ title = "What now?"
    menu:
        "Touch yourself":
            player.c "Touch yourself, [chelsea.name]."
            wt_image chubby_gf_youth_3_23
            chelsea.c "What?  Umm, aren't little girls supposed to NOT touch themselves down there?"
            wt_image chubby_gf_youth_3_26
            player.c "It's okay when you have adult supervision."
            wt_image chubby_gf_youth_3_10
            "She gets into position to touch herself, then looks back at you."
            chelsea.c "This is going to make me horny.  Then I'll have trouble paying attention at work and want to touch myself again when you aren't there to supervise me."
            $ title = "What now?"
            menu:
                "Tell her to finger her ass" if chelsea.anal_status > 3:
                    player.c "I don't want you to play with your pussy.  Play with your ass, instead."
                    if chelsea.anal_status == 4:
                        wt_image chubby_gf_youth_3_18
                        chelsea.c "What?  Why??"
                        player.c "That won't make you horny, will it?"
                        chelsea.c "No, but ..."
                        player.c "And I'll enjoy watching it just as much."
                        chelsea.c "But that's ..."
                        player.c "Something I want you to do for me, [chelsea.name]."
                        wt_image chubby_gf_youth_3_21
                        "Tentatively, [chelsea.name] places a finger at her rear opening."
                        player.c "Push it all the way in, [chelsea.name].  Nice and slow and it won't hurt."
                        wt_image chubby_gf_youth_3_22
                        call chelsea_anal_fingering from _call_chelsea_anal_fingering_1
                    else:
                        wt_image chubby_gf_youth_3_21
                        "[chelsea.name]'s become used to putting things in her ass.  She reaches a hand back and places her finger against her rosebud ..."
                        wt_image chubby_gf_youth_3_22
                        "... then pushes it all the way in as you watch."
                    wt_image chubby_gf_youth_3_18
                    chelsea.c "I'd better get to work now."
                "Send her to work horny":
                    wt_image chubby_gf_youth_3_18
                    player.c "I like the idea of you being horny at work.  Start rubbing yourself."
                    wt_image chubby_gf_youth_3_19
                    "She reaches a hand back and rubs herself, tentatively at first, then gradually with more vigor. You wait until she starts moaning before you tell her she can stop."
                    chelsea.c "Ahhhh"
                    player.c "Okay, [chelsea.name].  You can go to work now."
                    wt_image chubby_gf_youth_3_20
                    chelsea.c "I'm going to be thinking about your big dick all day, [chelsea.your_name].  I can't wait to have it where my fingers just were."
                    sys "[chelsea.name] is happier with your relationship."
                    $ chelsea.relationship_counter += 0.5
                "Let her get up":
                    player.c "I'll let you go to work without playing with yourself, but you have to promise you'll be horny and ready to fuck the next time I come looking for you."
                    wt_image chubby_gf_youth_3_20
                    chelsea.c "I will be. I'll be looking forward to having your big dick inside me, [chelsea.your_name]! I'm going to be thinking about it all day."
                    sys "[chelsea.name] is happier with your relationship."
                    $ chelsea.relationship_counter += 0.5
            $ chelsea.temporary_count = 0
        "Stay there while I jerk off":
            wt_image chubby_gf_youth_3_23
            "She grins as you take out your cock and stroke yourself."
            wt_image chubby_gf_youth_3_20
            chelsea.c "Oh, did looking at my body get you that excited?  That is so hot!  Did you want to see more of me?"
            wt_image chubby_gf_youth_3_11
            $ title = "What do you want to look at?"
            menu:
                "Her tits":
                    wt_image chubby_gf_youth_3_27
                    "She finishes stripping ..."
                    wt_image chubby_gf_youth_3_12
                    "... then leans forward to give you a good look at her boobs as you pump yourself."
                "Her ass":
                    wt_image chubby_gf_youth_3_13
                    "She finishes stripping ..."
                    wt_image chubby_gf_youth_3_28
                    "... then turns herself around so you can stare at her ass as you pump yourself."
                "Her pussy":
                    wt_image chubby_gf_youth_3_29
                    "She finishes stripping ..."
                    wt_image chubby_gf_youth_3_30
                    "... then exposes her sex for you to stare at as you pump yourself."
            $ title = "Where do you want to cum?"
            menu:
                "On her":
                    wt_image chubby_gf_toned_3_10
                    "[chelsea.name] moans as step closer and places her face directly beneath your cock."
                    chelsea.c "Ohh!!"
                    player.c "[player.orgasm_text]"
                    wt_image chubby_gf_toned_3_11
                    "[chelsea.name] grins at you and laughs."
                    chelsea.c "Mmmm, I think you enjoyed my teasing."
                    $ chelsea.facial_count += 1
                "On the floor":
                    wt_image chubby_gf_youth_3_14
                    player.c "[player.orgasm_text]"
                    "[chelsea.name] gasps in surprise at the sight of your sperm arcing up and over the floor between you and her."
                    chelsea.c "Ohh!!  That was so hot!  I think you enjoyed my teasing."
                    $ title = "What next?"
                    menu:
                        "Tell her to clean it up":
                            if chelsea.cum_lick_count > 3:
                                wt_image chubby_gf_youth_3_17
                                "She hesitates a moment, then falls to the floor, looking up at you."
                                chelsea.c "Okay, [chelsea.your_name].  I guess my teasing was the reason for the mess."
                                wt_image chubby_gf_toned_3_30
                                "She does a thorough job of cleaning the floor..."
                                wt_image chubby_gf_toned_3_14
                                "... making sure to get every last drop before getting up."
                                $ chelsea.cum_lick_count += 1
                            else:
                                wt_image chubby_gf_youth_3_31
                                if chelsea.cum_lick_count > 1:
                                    "She hesitates before replying."
                                    chelsea.c "Ummm, [chelsea.your_name], you made that mess, not me.  Plus I have to get to work.  If you want, I'll wipe it up for you when I get home."
                                else:
                                    chelsea.c "Ummm, [chelsea.your_name], you made that mess, not me.  Plus I have to get to work."
                                $ title = "What do you do?"
                                menu:
                                    "Use her trigger" if chelsea.has_tag('trigger_implanted'):
                                        player.c "You're going to clean my sperm up, [chelsea.name]."
                                        chelsea.c "What?  Why?"
                                        wt_image chubby_gf_youth_3_15
                                        player.c "Because I told you to.  [chelsea.trigger_phrase], [chelsea.name].  Get on the floor and clean up my sperm."
                                        wt_image chubby_gf_youth_3_17
                                        "The hypnotized women gets down on the floor, then looks up at you."
                                        chelsea.c "I don't have a cloth, [chelsea.your_name]."
                                        player.c "Use your tongue, [chelsea.name]. Lick my sperm up with your tongue."
                                        wt_image chubby_gf_toned_3_30
                                        "[chelsea.name] has no aversion to eating your cum, and in her triggered state, she willing does so off the floor as she kneels in front of you."
                                        wt_image chubby_gf_toned_3_14
                                        "She makes sure to get every last drop before she gets up."
                                        wt_image chubby_gf_youth_3_16
                                        "Your use of her complete, you release her from her trigger and send her off to work."
                                        $ chelsea.cum_lick_count += 1
                                    "Dominate her" if chelsea.dominate_status == 8:
                                        wt_image chubby_gf_toned_3_15
                                        player.c "I said clean up my sperm, fucktoy."
                                        "Seizing her by the hair, you pull her off the sofa and onto the floor."
                                        wt_image chubby_gf_toned_3_30
                                        "Up until now, she's been enjoying this, but being forced to grovel at your feet and clean up your sperm with her tongue changes the whole experience for her.  She has no aversion to eating your cum, but licking it off the floor is a whole different matter."
                                        player.c "Get every drop, fucktoy.  Once you've licked up and swallowed every bit of my jizz, then you can go to work."
                                        sys "[chelsea.name] is less happy with your relationship."
                                        $ chelsea.visit_count -= 1
                                        $ chelsea.relationship_counter -= 1
                                        $ chelsea.cum_lick_count += 2
                                    "Let her go to work":
                                        wt_image chubby_gf_toned_3_16
                                        chelsea.c "Bye!"
                        "Let her go to work":
                            wt_image chubby_gf_toned_3_16
                            chelsea.c "Bye!"
            orgasm notify
        "Get to work":
            call chelsea_gf_action_3_youth_get_to_work from _call_chelsea_gf_action_3_youth_get_to_work_3
    return

label chelsea_gf_action_8_toned_tf:
    wt_image chubby_gf_toned_2_19
    chelsea.c "I love that you never seem to tire of fucking my tits."
    wt_image chubby_gf_toned_2_7
    "That makes two of you."
    wt_image chubby_gf_toned_2_11
    "You also love that [chelsea.name] never seems to tire of watching you splatter her with your jizz."
    wt_image chubby_cum_tits_7
    player.c "[player.orgasm_text]"
    $ chelsea.titfuck_count += 1
    orgasm notify
    return

label chelsea_gf_action_8_toned_bj:
    wt_image chubby_gf_toned_2_20
    chelsea.c "Was it just my tongue you wanted to feel?"
    wt_image chubby_gf_toned_2_8
    player.c "No, I think I should feel your lips around my cock, too."
    wt_image chubby_gf_toned_2_10
    "That soon leads to you wanting something else."
    $ title = "Where do you want to cum?"
    menu:
        "In her":
            wt_image chubby_gf_toned_2_21
            player.c "I also want to watch you swallow my load."
            wt_image chubby_gf_toned_2_22
            "She wraps her lips tight around you and rapidly swallows the burst of fluids you pump into her throat"
            $ chelsea.swallow_count += 1
        "On her":
            wt_image chubby_gf_toned_2_12
            player.c "I also want to see my cum on your face."
            wt_image chubby_gf_toned_2_9
            "She laughs and lets a spurt of your jizz splatter up and over her nose and forehead, before pointing the rest of it to land in her waiting mouth."
            $ chelsea.facial_count += 1
    player.c "[player.orgasm_text]"
    $ chelsea.blowjob_count += 1
    orgasm notify
    return

label chelsea_girlfriend_date:
    wt_image chelsea.image
    chelsea.c "A date?  That sounds like fun!"
    call expandable_menu(chelsea_girlfriend_date_menu) from _call_expandable_menu_12
    return

label chelsea_girlfriend_date_club:
    if day == 5 and gloria.has_tag('show_friday'):
        "Not today.  The Club is closed for a special event today."
    else:
        $ chelsea.temporary_count = 1 # tracks that you spent time with her
        player.c "Let's eat at the Club today."
        if chelsea.has_tag('little_girl'):
            chelsea.c "I guess I have to wear grown up clothes there?"
            player.c "That would be best."
            chelsea.c "Okay. I'll go change into one of my 'pretend to be an adult so I can go to work' outfits."
        else:
            chelsea.c "Sounds good. I'll go change."
            player.c "What you're wearing looks nice."
            chelsea.c "Don't be silly. I'll just be a minute."
        wt_image chubby_date_2_1
        "It takes a while, but eventually she reappears."
        chelsea.c "Okay. All set. Let's go."
        call forced_movement(club) from _call_forced_movement_222
        summon chelsea no_follows
        change player money by -10 notify
        if chelsea.club_date_count == 0:
            $ chelsea.club_date_count = 1
            wt_image chubby_date_2_2
            "You find a quiet table at the Club for you and [chelsea.name]."
            chelsea.c "This is nice! Everything on the menu looks scrumptious."
            player.c "So do you."
            chelsea.c "Ahh!  You're so sweet sometimes."
            wt_image chubby_date_2_12
            "After you eat, you take in one of the shows."
            player.c "You should try that sometime."
            wt_image chubby_date_2_3
            chelsea.c "Yeah, right.  One thing I'm not is an exhibitionist.  These big boobies of mine are staying under cover while we're out in public."
            player.c "I don't mind you showing them off."
            chelsea.c "I mind!"
            wt_image chubby_date_2_13
            chelsea.c "Oh!  This next show looks good to me."
            player.c "I bet it does."
            wt_image chubby_date_2_2
            chelsea.c "Hey! You should try that sometime. I wouldn't mind you getting up on stage to shake your big dick for the ladies."
            player.c "Touché"
        else:
            wt_image chubby_date_2_2
            "[chelsea.name] and you find a quiet table to enjoy your meal. The food is good, and so is the conversation. [chelsea.name] is having a good time."
            chelsea.c "This was a lot of fun! Thanks for bringing me here."
            wt_image chubby_date_2_3
            player.c "Sure I can't convince you to take a spin on stage?"
            chelsea.c "No way. Not unless you're joining me. Actually, not even then. I'm just not into the idea of showing off in front of an audience like that."
        $ title = "What now?"
        menu:
            "Take her to the Swingers Room" if player.sr_visit_count > 0:
                if player.test('energy', 10) or player.has_item(stamina_pills):
                    player.c "Since we're here, let's duck into the Swingers Room."
                    chelsea.c "Okay. I just need to go change."
                    player.c "You look fine."
                    chelsea.c "I know!  Too fine for the Swingers Room.  It can be a bit ... sticky.  Don't worry, I brought a change of clothing.  I'll meet you in there."
                    add tags 'club_date_night' 'in_swingers_room_now' to chelsea
                    change player energy by -10 notify
                    call character_location_return(chelsea) from _call_character_location_return_40
                    call forced_movement(swingers_room) from _call_forced_movement_223
                else:
                    "You'd like to take her to the Swingers Room, but you don't have the energy. You take her home instead."
                    change player energy by -10 notify
                    call character_location_return(chelsea) from _call_character_location_return_41
                    call forced_movement(living_room) from _call_forced_movement_224
            "Trigger her to display herself" if chelsea.has_tag('trigger_implanted'):
                wt_image chubby_date_2_4
                "You settle your bill and leave your table. Before leaving the Club, you stop and motion for [chelsea.name] to take a seat on a bench."
                player.c "I have something I want to do before we go. Wait for me here."
                chelsea.c "Okay"
                player.c "While you're waiting, show off your body. The other Club members will enjoy looking at it."
                chelsea.c "What?"
                wt_image chubby_date_2_5
                player.c "[chelsea.trigger_phrase], [chelsea.name]. Show off your body until I come to get you."
                wt_image chubby_date_2_14
                player.c "If anyone asks, you're waiting for me to return.  Any comments you get will make you feel good about exposing yourself."
                if chelsea.club_date_count >= 6:
                    wt_image chubby_date_2_11
                    "[chelsea.name] has fully embraced your command to expose herself. She couldn't get more exposed than she is now."
                    club_patron_9 "I heard she's one of those avant-garde performance artists."
                    club_patron_6 "Someone told me it's an ironic commentary on the nature of the Club and it's role in society."
                    club_patron_10 "I saw something like this in a Bodywerks pamphlet once. Dark stuff, but apparently the super-wealthy swear by them."
                elif chelsea.club_date_count == 5:
                    wt_image chubby_date_2_10
                    "Once again, [chelsea.name] pulls up her dress and pulls down her panties. This time, though, there's no protective hand to shield her sex from passersby."
                    club_patron_1 "Oh sweetie, you're in the wrong part of the Club. Take that to the Swingers Room."
                    club_patron_8 "I haven't been here in a while. The Club seem even more risqué than I remember it."
                    $ chelsea.club_date_count = 6
                elif chelsea.club_date_count == 4:
                    wt_image chubby_date_2_9
                    "[chelsea.name]'s getting into the hang of this exhibitionist thing. Shedding her panties, she pulls up her dress. Her sole nod to modesty is a hand placed strategically over her girl bits."
                    club_patron_2 "I think someone's auditioning to be our next showgirl."
                    club_patron_7 "Take your hand away, sweetheart. I know you want to."
                    $ chelsea.club_date_count = 5
                elif chelsea.club_date_count == 3:
                    wt_image chubby_date_2_8
                    "[chelsea.name]'s mind seems to have reconciled the imperative created by the trigger. She pulls up her dress and plays sneak-a-peek with her panties as people pass by."
                    club_patron_5 "Ignore her. She's just looking for attention."
                    club_patron_6 "Those panties don't even match your outfit.  'm not sure why you're so keen to show them off."
                    $ chelsea.club_date_count = 4
                elif chelsea.club_date_count == 2:
                    wt_image chubby_date_2_7
                    "The trigger hits her harder this time. Her mind zones out, trying to reconcile the need to expose herself with her basic personality. She still exposes only her breasts, but at least shows more leg."
                    club_patron_3 "Is she drunk? Should we get her help?"
                    club_patron_4 "Her boyfriend's around here somewhere. I don't know why he doesn't cover her up, though. She's making a spectacle of herself."
                    $ chelsea.club_date_count = 3
                elif chelsea.club_date_count < 2:
                    wt_image chubby_date_2_6
                    "She sits with only her breasts exposed, but its a start.  With breasts like hers, she soon attracts attention."
                    club_patron_1 "That's not really appropriate, dear. Not in this part of the Club."
                    club_patron_2 "We all enjoy the view, but you're distracting people from the show."
                    $ chelsea.club_date_count = 2
                change player energy by -10 notify
                call character_location_return(chelsea) from _call_character_location_return_42
                call forced_movement(living_room) from _call_forced_movement_225
            "Take her home for sex":
                if player.test('energy', 10) or player.has_item(stamina_pills):
                    call forced_movement(bedroom) from _call_forced_movement_226
                    summon chelsea no_follows
                    change player energy by -10
                    wt_image chubby_gf_toned_1_13
                    "When you get home, [chelsea.name] tackles you at almost the same time you try and tackle her.  Through a flurry of flying clothes, the two of you end up entangled on the bed, your cock finding its way into her wet and eager pussy."
                    wt_image chubby_gf_toned_1_14
                    "Wrestling her around, the two of you fuck noisily, as if in a race to see who can cum first."
                    chelsea.c "Ahhhh"
                    wt_image chubby_gf_toned_1_10
                    "It's a race you win. Barely."
                    player.c "[player.orgasm_text]"
                    chelsea.c "Aahhhhhh"
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                    call character_location_return(chelsea) from _call_character_location_return_43
                else:
                    "You're feeling amorous, but you don't have the energy to act on those feelings. By the time you get her home, you're ready to call it a night."
                    change player energy by -10 notify
                    call character_location_return(chelsea) from _call_character_location_return_44
                    call forced_movement(living_room) from _call_forced_movement_227
            "That's enough for today":
                "You and [chelsea.name] head home to finish your day."
                change player energy by -10 notify
                call character_location_return(chelsea) from _call_character_location_return_45
                call forced_movement(living_room) from _call_forced_movement_228
        $ chelsea.training_session()
        wt_image current_location.image
        sys "[chelsea.name] is happier with your relationship."
        $ chelsea.relationship_counter += 1
    return

label chelsea_girlfriend_date_restaurant:
    change player money by -10 notify
    if chelsea.has_tag('little_girl'):
        chelsea.c "I need to go change into something pretty!"
        wt_image chubby_date_1_11
        "She returns a few minutes later."
        chelsea.c "Does this look okay?"
        wt_image chubby_date_1_3
        player.c "It does, but you should probably keep your boobs inside your top when we're at te restaurant."
        wt_image chubby_date_1_4
        chelsea.c "That's just for you. I'll keep them covered for everyone else.  Let's go!"
    else:
        chelsea.c "I need to go change into something nice."
        wt_image current_location.image
        "You thought she looked nice already, but far be it for you to keep a woman from an opportunity to raid her closet for a change of clothing. You wait in the living room as she looks for something else to wear, until eventually she reappears."
        if chelsea.has_tag('bbw'):
            wt_image chubby_date_1_1
            chelsea.c "Okay.  Just zip me up and we'll go."
        else:
            wt_image chubby_date_1_13
            chelsea.c "Does this look okay?  It doesn't make me look fat, does it?"
            wt_image chubby_date_1_2
            player.c "You look great.  Let's go."
    call forced_movement(outdoors) from _call_forced_movement_229
    summon chelsea no_follows
    wt_image chubby_date_1_5
    "You find a cozy, intimate restaurant and are seated in a corner table where you can chat quietly to yourselves. you enjoy a lovely meal before heading home."
    call forced_movement(living_room) from _call_forced_movement_230
    summon chelsea no_follows
    if chelsea.has_tag('little_girl'):
        wt_image chubby_date_1_12
        chelsea.c "Thank you for the great date."
    else:
        if chelsea.has_tag('bbw'):
            wt_image chubby_date_1_7
            chelsea.c "Finally, I can get out of this dress!  I love it, but it's so scratchy.  Thank you for the great date."
        else:
            wt_image chubby_date_1_6
            chelsea.c "Thank you for the great date."
        $ title = "What do you say?"
        menu:
            "Ask for a proper thank you":
                player.c "You can do a better job than that of thanking me, can't you?"
                if chelsea.has_tag('little_girl'):
                    wt_image chubby_date_1_10
                else:
                    if chelsea.has_tag('bbw'):
                        wt_image chubby_date_1_8
                    else:
                        wt_image chubby_date_1_9
                chelsea.c "Of course."
                wt_image chubby_gf_toned_2_8
                chelsea.c "Thank you for the lovely date, [chelsea.your_name]."
                "She grins at you and licks the underside of your cock ..."
                wt_image chubby_gf_toned_2_10
                "... before devoting her mouth to a more direct and physical display of her thanks.  Soon it's your turn to thank her, for the pleasure she's provided to your dick."
                $ title = "Where do you want to thank her?"
                menu:
                    "In her mouth":
                        wt_image chubby_boot_camp_10
                        "She had a nice meal, but didn't get any dessert ... until now."
                        player.c "[player.orgasm_text]"
                        $ chelsea.swallow_count += 1
                    "On her face":
                        wt_image chubby_discipline_2_6
                        "She just had a nice meal and is probably full.  No need to give her something else to eat.  You pull your cock out of her mouth and graciously empty your load on her face, to her amusement."
                        player.c "[player.orgasm_text]"
                        $ chelsea.facial_count += 1
                $ chelsea.blowjob_count += 1
                orgasm notify
            "You're welcome":
                player.c "You're welcome. I had fun, too."
                "You leave her to get on with the rest of her day, and get on with yours."
                change player energy by -energy_short notify
    call character_location_return(chelsea) from _call_character_location_return_46
    $ chelsea.training_session()
    wt_image current_location.image
    sys "[chelsea.name] is happier with your relationship."
    $ chelsea.relationship_counter += 1
    return

label chelsea_girlfriend_date_boat:
    change player money by -20 notify
    call forced_movement(outdoors) from _call_forced_movement_231
    summon chelsea no_follows
    wt_image chubby_boat_1_1
    "Renting a boat for the day is expensive, but you figure [chelsea.name] is worth it."
    wt_image chubby_boat_1_2
    "Watching her sunbathe in her bikini is worth it, in any event."
    wt_image chubby_boat_1_3
    chelsea.c "This is so nice, [chelsea.your_name].  Thank you for doing this."
    wt_image chubby_boat_1_4
    $ title = "What now?"
    menu:
        "Suggest she sunbathe nude":
            wt_image chubby_boat_1_5
            chelsea.c "I guess no one can see me out here."
            wt_image chubby_boat_1_6
            player.c "You're not going to stop there, are you?"
            wt_image chubby_boat_1_7
            chelsea.c "It's a good thing I brought lots of sunblock."
            wt_image chubby_boat_1_8
            chelsea.c "Is this better?"
            if chelsea.has_tag('trigger_implanted'):
                $ title = "Use her trigger?"
                menu:
                    "Yes":
                        wt_image chubby_boat_1_10
                        player.c "Not quite.  [chelsea.trigger_phrase], [chelsea.name].  Get up on the side of the boat and expose yourself."
                        wt_image chubby_boat_1_11
                        "You pass a lovely few hours on the water.  [chelsea.name] doesn't remember much from the last part of your sail, but many of the other boaters you pass certainly do."
                    "No":
                        wt_image chubby_boat_1_9
                        "It is rather nice, and you and [chelsea.name] pass a lovely few hours on the water, with her naked for your enjoyment."
            else:
                wt_image chubby_boat_1_9
                "It is rather nice, and you and [chelsea.name] pass a lovely few hours on the water, with her naked for your enjoyment."
            change player energy by -energy_very_short
        "Ask for a blowjob":
            wt_image chubby_boat_1_12
            "[chelsea.name] takes a look around to confirm you're far enough offshore that no one can see her before she pulls off her bikini top ..."
            wt_image chubby_boat_1_13
            "... then she drops to her knees and takes out your cock ..."
            wt_image chubby_boat_1_14
            "... and begins to blow you."
            wt_image chubby_boat_1_15
            "It's a fairly quick blowjob, but none-the-less enjoyable for that."
            wt_image chubby_boat_1_16
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image chubby_boat_1_15
                    player.c "[player.orgasm_text]"
                    wt_image chubby_boat_1_13
                    chelsea.c "Mmmm, salty.  Kind of appropriate on a sailing boat, I guess."
                    $ chelsea.swallow_count += 1
                "On her":
                    wt_image chubby_boat_1_17
                    player.c "[player.orgasm_text]"
                    wt_image chubby_boat_1_18
                    chelsea.c "Guess I need to go for a swim, now, to clean up!"
            $ chelsea.blowjob_count += 1
            orgasm notify
        "Fuck her from behind":
            wt_image chubby_boat_1_19
            player.c "The nice thing about the privacy of being out on the water is no one can see what I'm about to do with you."
            wt_image chubby_boat_1_20
            chelsea.c "Oh, yeah?  What are you going to do with me, [chelsea.your_name]?"
            wt_image chubby_boat_1_21
            player.c "This"
            wt_image chubby_boat_1_22
            "You need to wait for her body to catch to up to you before you can really start fucking her ..."
            wt_image chubby_boat_1_23
            "... and even then, as much as she's enjoying this, she's not aroused enough to cum.  You, of course, very much are."
            wt_image chubby_boat_1_24
            player.c "[player.orgasm_text]"
            wt_image chubby_boat_1_7
            chelsea.c "Well this is turning out to be a fun sail!"
            $ chelsea.sex_count += 1
            orgasm notify
        "Fuck her on her back":
            wt_image chubby_boat_1_19
            player.c "The nice thing about the privacy of being out on the water is no one can see what I'm about to do with you."
            wt_image chubby_boat_1_20
            chelsea.c "Oh, yeah?  What are you going to do with me, [chelsea.your_name]?"
            wt_image chubby_boat_1_25
            player.c "This"
            wt_image chubby_boat_1_26
            "You need to wait for her body to catch to up to you before you can really start fucking her ..."
            wt_image chubby_boat_1_27
            "... and even then, as much as she's enjoying this, she's not aroused enough to cum.  You, of course, very much are."
            wt_image chubby_boat_1_28
            player.c "[player.orgasm_text]"
            wt_image chubby_boat_1_5
            chelsea.c "Well this is turning out to be a fun sail!"
            $ chelsea.sex_count += 1
            orgasm notify
        "Have her ride you":
            player.c "You should get some exercise while we're out here."
            wt_image chubby_boat_1_1
            chelsea.c "You mean like going for a swim?"
            wt_image chubby_boat_1_29
            player.c "I had another form of exercise in mind."
            wt_image chubby_boat_1_30
            "Settling down on your hard cock, she begins to ride you, faster and faster ..."
            wt_image chubby_boat_1_31
            "... getting both some exercise and an orgasm for her efforts ..."
            chelsea.c "Aahhhhhh"
            wt_image chubby_boat_1_32
            "... while you're happy to settle for the orgasm."
            player.c "[player.orgasm_text]"
            wt_image chubby_boat_1_7
            chelsea.c "And here I thought sailing was just for relaxing!"
            $ chelsea.orgasm_count += 1
            $ chelsea.sex_count += 1
            orgasm notify
        "Just enjoy the sailing":
            wt_image chubby_boat_1_1
            "You and [chelsea.name] pass a lovely few hours on the water."
            change player energy by -energy_very_short
    call forced_movement(living_room) from _call_forced_movement_232
    call character_location_return(chelsea) from _call_character_location_return_47
    $ chelsea.training_session()
    sys "[chelsea.name] is much happier with your relationship."
    $ chelsea.relationship_counter += 2
    return

label chelsea_girlfriend_date_massage:
    chelsea.c "A trip to a spa for a massage sounds great!"
    call forced_movement(outdoors) from _call_forced_movement_233
    summon chelsea no_follows
    wt_image chubby_massage_1_1
    player.c "Make yourself comfortable."
    wt_image chubby_massage_1_2
    chelsea.c "Where's the masseuse?"
    player.c "You're looking at him.  How am I supposed to massage you while you're still in your undies?"
    wt_image chubby_massage_1_3
    chelsea.c "I didn't know this was that sort of a massage place.  Don't I get a towel?"
    wt_image chubby_massage_1_4
    player.c "What do you need a towel for?  Were you planning on getting wet?"
    wt_image chubby_massage_1_5
    chelsea.c "I guess that depends on how you're planning to rub me."
    wt_image chubby_massage_1_6
    player.c "In that case, I'd better roll you over.  How does this feel?"
    wt_image chubby_massage_1_7
    chelsea.c "Ahhh"
    wt_image chubby_massage_1_8
    player.c "That good, huh?  How does it feel, then, when I rub you here?"
    wt_image chubby_massage_1_9
    chelsea.c "Aahhh ... It feels like I may need that towel, soon."
    wt_image chubby_massage_1_10
    $ title = "What now?"
    menu:
        "Eat her out":
            wt_image chubby_massage_1_12
            player.c "Not if I help you get rid of that wetness."
            wt_image chubby_massage_1_13
            "You actually help her create more wetness, so much that it's hard to lap it all up ..."
            wt_image chubby_massage_1_14
            "... especially when she cums."
            wt_image chubby_massage_1_15
            chelsea.c "Aahhhhhh"
            wt_image chubby_massage_1_16
            chelsea.c "Wow, that felt nice!"
            wt_image chubby_massage_1_17
            player.c "So I could tell.  So could everyone else in the spa, I'm sure.  We'd better get going before the staff come investigate what those sounds were that you were making."
            $ chelsea.pleasure_her_count += 1
            $ chelsea.orgasm_count += 1
            change player energy by -energy_short notify
        "Use her sextoy on her" if chelsea.has_item(dildo):
            wt_image chubby_massage_1_18
            player.c "How about the sextoy I bought you, instead?"
            "*bzzzzzzzzz*"
            wt_image chubby_massage_1_19
            chelsea.c "Aahhh"
            player.c "Roll over onto your hands and knees.  I want to look at your ass while you cum for me."
            wt_image chubby_massage_1_20
            "As [chelsea.name] scrambles into position, you press the vibrator against her sex ... *bzzzzzzzzz*"
            wt_image chubby_massage_1_21
            chelsea.c "Aahhhh"
            wt_image chubby_massage_1_22
            chelsea.c "Aahhhhhhh"
            wt_image chubby_massage_1_23
            chelsea.c "Wow, that felt good!  My legs are still shaking."
            wt_image chubby_massage_1_17
            player.c "So are the walls.  We'd better get going before the staff come investigate what those sounds were you were making."
            $ chelsea.orgasm_count += 1
            change player energy by -energy_very_short notify
        "Fuck her":
            wt_image chubby_massage_1_24
            "Instead of a towel, you give her something that'll only make her wetter."
            wt_image chubby_massage_1_25
            chelsea.c "Aahhh"
            wt_image chubby_massage_1_26
            "There's no reason to take things slow, she's riled up from the massage and ready to go.  You pound into her hard and fast, making this an intense but speedy quickie."
            wt_image chubby_massage_1_27
            chelsea.c "Aahhhhhhh"
            wt_image chubby_massage_1_28
            player.c "[player.orgasm_text]"
            wt_image chubby_massage_1_16
            chelsea.c "Wow, that felt nice!"
            wt_image chubby_massage_1_17
            player.c "So I could tell.  So could everyone else in the spa, I'm sure.  We'd better get going before the staff come investigate what we're up to."
            $ chelsea.orgasm_count += 1
            $ chelsea.sex_count += 1
            orgasm notify
        "Ask for a 'thank you' blowjob":
            if chelsea.has_tag('customary_post_massage_thankyou'):
                wt_image chubby_massage_1_29
                player.c "Time for the customary post-massage 'thank you'."
                wt_image chubby_massage_1_30
                chelsea.c "You seem to be a big fan of this custom, [chelsea.your_name]."
                wt_image chubby_massage_1_31
                chelsea.c "And getting bigger by the minute, I think."

            else:
                add tags 'customary_post_massage_thankyou' to chelsea
                wt_image chubby_massage_1_29
                player.c "I believe its customary to show appreciation to the masseuse after a particularly stimulating massage."
                wt_image chubby_massage_1_30
                chelsea.c "I'm pretty sure this type of 'thank you' isn't a custom anywhere, [chelsea.your_name]."
                wt_image chubby_massage_1_31
                player.c "In that case, let's start our own custom."
            wt_image chubby_massage_1_32
            "As customs go, this is a rather nice one ..."
            wt_image chubby_massage_1_33
            "... that definitely leaves you feeling appreciated."
            wt_image chubby_massage_1_34
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image chubby_massage_1_35
                    "You push your cock as far down her throat as it will fit, then let yourself go."
                    wt_image chubby_massage_1_36
                    player.c "[player.orgasm_text]"
                    wt_image chubby_massage_1_37
                    chelsea.c "Mmmm, I guess we both enjoyed our massage date."
                    $ chelsea.swallow_count += 1
                "On her":
                    wt_image chubby_massage_1_38
                    player.c "[player.orgasm_text]"
                    wt_image chubby_massage_1_
                    chelsea.c "Mmmm, I guess we both enjoyed our massage date.  I think I need that towel, now."
                    $ chelsea.facial_count += 1
            $ chelsea.blowjob_count += 1
            orgasm notify
        "Make it a non-sex massage":
            wt_image chubby_massage_1_5
            player.c "It might be embarrassing to return a towel to the spa in that condition.  We'd better stick to a normal massage."
            wt_image chubby_massage_1_11
            chelsea.c "Mmmm, okay.  But if you want to fuck me sometime soon, I won't object."
            change player energy by -energy_very_short notify
    call forced_movement(living_room) from _call_forced_movement_234
    call character_location_return(chelsea) from _call_character_location_return_48
    $ chelsea.training_session()
    sys "[chelsea.name] is happier with your relationship."
    $ chelsea.relationship_counter += 1
    return

# Anal Actions
label chelsea_girlfriend_butt_play:
  if chelsea.anal_status == 6:
    if chelsea.has_tag('little_girl'):
      wt_image chubby_gf_youth_5_7
      "You find [chelsea.name] in the bedroom getting ready for her day."
      chelsea.c "Are you watching me get dressed?"
      player.c "Mostly I was staring at your ass. Your ass looks good, [chelsea.name]."
      wt_image chubby_anal_youth_1_9
      chelsea.c "Really?"
      player.c "Really. I can think of something that would make it look even better, though."
      wt_image chubby_gf_youth_5_4
      chelsea.c "What's that?"
      player.c "My dick sticking out of it."
      wt_image chubby_anal_youth_1_10
      chelsea.c "Ha ha!  Please don't joke about that. You know I don't like anal."
      player.c "But you'll do it, for me, won't you?"
      wt_image chubby_gf_youth_5_3
      chelsea.c "Yes, but ... can't we do something else later, after I'm finished my work?  Something we'd both enjoy?"
      $ title = "Insist on anal?"
      menu:
        "With her looking at you":
          $ chelsea.training_session()
          if chelsea.hypno_re_anal > 1:
            $ chelsea.relationship_counter -= 0.5
          else:
            $ chelsea.relationship_counter -= 1
          wt_image chubby_anal_youth_1_5
          player.c "Lie down on your back. You may enjoy it more if you're able to watch me fuck your ass."
          "Nice thought, but unlikely given her aversion to anal. Still, she removes her pants and prepares herself, mentally and physically, as you apply lube to your hard cock."
          wt_image chubby_anal_youth_1_15
          "The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
          chelsea.c "Ow!"
          wt_image chubby_anal_youth_1_16
          "You'd facing like this would make a difference, but it didn't. It seems [chelsea.name]'s not going to enjoy this, so you focus simply on enjoying the moment.  That's not hard.  As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
          wt_image chubby_anal_youth_1_17
          "You'd like to make the fuck last forever, but as it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore. Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
          player.c "[player.orgasm_text]"
          chelsea.c "Oh finally!!"
          sys "[chelsea.name] is less happy with your relationship."
          $ chelsea.anal_count += 1
          orgasm notify
        "With her facing away from you":
          $ chelsea.training_session()
          if chelsea.hypno_re_anal > 1:
            $ chelsea.relationship_counter -= 0.5
          else:
            $ chelsea.relationship_counter -= 1
          wt_image chubby_anal_youth_1_11
          player.c "That's not like my little girl to act like a spoiled princess. A dick in your ass isn't going to hurt you. Not as long as I use lots of lube."
          player.c "Turn around."
          "She removes her pants and prepares herself, mentally and physically, as you apply lube to your hard cock."
          wt_image chubby_anal_youth_1_12
          "The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
          chelsea.c "Ow!"
          wt_image chubby_anal_youth_1_13
          "[chelsea.name]'s not going to enjoy this, so you don't bother trying to suggest she try. You focus simply on enjoying the moment. Gripping her by the hips, you flip her over onto her stomach to give you easier access."
          "As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
          wt_image chubby_anal_youth_1_14
          "You'd like to make the fuck last forever, but as it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore."
          "Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
          player.c "[player.orgasm_text]"
          chelsea.c "Oh finally!!"
          $ chelsea.anal_count += 1
          orgasm notify
        "Relent":
          player.c "Okay, [chelsea.name].  No anal for today."
          chelsea.c "Thanks!"
    else:
      if chelsea.has_tag('bbw'):
        player.c "Your ass looks good, [chelsea.name]."
        wt_image chubby_visit_bbw_4_10
        chelsea.c "Really?"
        player.c "Really. I can think of something that would make it look even better, though."
        chelsea.c "What's that?"
        player.c "My dick sticking out of it."
        chelsea.c "Ha ha! Don't even joke about that. You know I don't like anal."
        player.c "But you'll do it, for me, won't you?"
        chelsea.c "Yes, but ... can't we do something else later, after I've finished my work?  Something we'd both enjoy?"
        $ title = "Insist on anal?"
        menu:
          "With you on top":
            $ chelsea.training_session()
            if chelsea.hypno_re_anal > 1:
              $ chelsea.relationship_counter -= 0.5
            else:
              $ chelsea.relationship_counter -= 1
            player.c "Don't be such a princess. A dick in your ass isn't going to hurt you. Not as long as I use enough lube. Get yourself ready."
            wt_image chubby_anal_bbw_2_1
            "She pulls off her clothes and prepares herself, mentally and physically, as you apply lube to your hard cock. You contemplate tonguing her, as that seems to relax her, then decide she needs to learn to take your cock up her ass without that preamble."
            wt_image chubby_anal_bbw_2_2
            "The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
            chelsea.c "Ow!"
            $ title = "Suggest she play with herself?"
            menu:
              "Yes":
                wt_image chubby_anal_bbw_2_3
                player.c "Play with yourself, [chelsea.name]. It'll make this more enjoyable for you."
                "She reaches a hand back and starts stroking her sex. The look on her face, however, suggests that it isn't distracting her from the feel of your cock filling up her bum. For you, that exact same feeling is incredible. As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
                $ chelsea.masturbation_count += 1
              "Don't bother":
                "[chelsea.name]'s not going to enjoy this, so you don't bother trying to suggest she try. You focus simply on enjoying the moment."
                wt_image chubby_anal_bbw_2_4
                "That's not hard.  As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
            wt_image chubby_anal_bbw_2_5
            "You'd like to make the fuck last forever, but as it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore. Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
            player.c "[player.orgasm_text]"
            chelsea.c "Oh finally!!"
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.anal_count += 1
            orgasm notify
          "With her on top":
            $ chelsea.training_session()
            if chelsea.hypno_re_anal > 1:
              $ chelsea.relationship_counter -= 0.5
            else:
              $ chelsea.relationship_counter -= 1
            wt_image chubby_anal_bbw_2_6
            player.c "I'm going to let you be on top.  That way you can control the pace.  It'll be easier for you that way."
            "Less difficult, maybe, but still not easy.  She pulls off her clothes and prepares herself, mentally and physically, as you apply lube to your hard cock."
            "You contemplate tonguing her, as that seems to relax her, then decide she needs to learn to take your cock up her ass without that preamble."
            wt_image chubby_anal_bbw_2_7
            player.c "I'll get us started, then you can sit up and ride me."
            "The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
            chelsea.c "Ow!"
            $ title = "Suggest she play with herself?"
            menu:
              "Yes":
                wt_image chubby_anal_bbw_2_8
                player.c "Play with yourself, [chelsea.name]. It'll make this more enjoyable for you."
                "She reaches a hand between her legs and rubs her sex as she settles herself onto you. The look on her face, however, suggests that it isn't distracting her from the feel of your cock filling up her bum."
                "For you, that exact same feeling is incredible. As her ass stretches to accommodate your girth, it feels like you're being swallowed by the tightest pussy in the world."
                $ chelsea.masturbation_count += 1
              "Don't bother":
                wt_image chubby_anal_bbw_2_9
                "[chelsea.name]'s not going to enjoy this, so you don't bother trying to suggest she try. You focus simply on enjoying the moment."
                "That's not hard.  As her ass stretches to accommodate your girth, it feels like you're being swallowed by the tightest pussy in the world."
            wt_image chubby_anal_bbw_2_10
            "[chelsea.name] can't - or won't - ride you quickly with your dick up her ass, which prolongs the fuck, something you're quite pleased with. As it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore."
            "Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
            player.c "[player.orgasm_text]"
            chelsea.c "Oh finally!!"
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.anal_count += 1
            orgasm notify
          "Relent":
            player.c "Okay, [chelsea.name]. No anal for today."
            chelsea.c "Thanks!"
      else:
        wt_image chubby_anal_toned_1_1
        chelsea.c "I just finished exercising."
        player.c "I know. I was watching you. Your ass looks good, [chelsea.name]."
        wt_image chubby_anal_toned_1_2
        chelsea.c "Really?  This ass?"
        player.c "Yes, really. I can think of something that would make your ass look even better, though."
        chelsea.c "What's that?"
        player.c "My dick sticking out of it."
        wt_image chubby_anal_toned_1_1
        chelsea.c "Ha ha! Don't even joke about that. You know I don't like anal."
        player.c "But you'll do it, for me, won't you?"
        wt_image chubby_anal_toned_1_17
        chelsea.c "Yes, but ... can't we do something else later, after I get cleaned up?  Something we'd both enjoy?"
        $ title = "Insist on anal?"
        menu:
          "With her ass up":
            $ chelsea.training_session()
            if chelsea.hypno_re_anal > 1:
              $ chelsea.relationship_counter -= 0.5
            else:
              $ chelsea.relationship_counter -= 1
            wt_image chubby_anal_toned_1_3
            player.c "Don't be such a princess. A dick in your ass isn't going to hurt you. Not as long as you're well lubed.  Get your ass up."
            wt_image chubby_anal_toned_1_4
            "You apply a generous dollop of lube to your thumb, then press it deep into her ass, making sure to swirl extra around her sphincter. She groans as your thumb penetrates her..."
            chelsea.c "oh!"
            wt_image chubby_anal_toned_1_5
            "...then groans again, louder, as the head of your cock replaces your thumb. The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
            chelsea.c "Ow!"
            wt_image chubby_anal_toned_1_6
            "[chelsea.name]'s not going to enjoy this, so you don't bother trying to suggest she try. You focus simply on enjoying the moment. That's not hard. As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
            wt_image chubby_anal_toned_1_7
            "You'd like to make the fuck last forever, but as it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore. Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
            player.c "[player.orgasm_text]"
            chelsea.c "Oh finally!!"
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.anal_count += 1
            orgasm notify
          "With her face up":
            $ chelsea.training_session()
            if chelsea.hypno_re_anal > 1:
              $ chelsea.relationship_counter -= 0.5
            else:
              $ chelsea.relationship_counter -= 1
            wt_image chubby_anal_toned_1_8
            player.c "Lie down on your back.  You may enjoy it more if you're able to watch me fuck your ass."
            "Nice thought, but unlikely given her aversion to anal.  Still, she prepares herself, mentally and physically, as you apply lube to your hard cock."
            wt_image chubby_anal_toned_1_9
            "The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
            chelsea.c "Oh!"
            wt_image chubby_anal_toned_1_10
            player.c "Play with yourself, [chelsea.name].  It'll make this more enjoyable for you."
            "She reaches a hand down and starts stroking her sex.  No amount of touching herself, however, is going to distract her from the feel of your cock filling up her bum. For you, that exact same feeling is incredible.  As her ass stretches to accommodate your girth, you're able to stroke back and forth more freely, until eventually you're fucking her ass much the same way you would fuck her pussy ... if her pussy was as tight as a fist."
            wt_image chubby_anal_toned_1_11
            "You'd like to make the fuck last forever, but as it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore. Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
            player.c "[player.orgasm_text]"
            chelsea.c "Oh finally!!"
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.anal_count += 1
            orgasm notify
          "With her riding you":
            $ chelsea.training_session()
            if chelsea.hypno_re_anal > 1:
              $ chelsea.relationship_counter -= 0.5
            else:
              $ chelsea.relationship_counter -= 1
            player.c "I'm going to let you be on top. That way you can control the pace. It'll be easier for you that way."
            wt_image chubby_anal_toned_1_12
            "Less difficult, maybe, but still not easy. She prepares herself, mentally and physically, as you apply lube to your hard cock."
            wt_image chubby_anal_toned_1_13
            "Lifting her up, you position the head of your cock at her rosebud, then guide her as she slowly settles down, impaling herself on you. The entrance into her back door is tight, challenging, and from your perspective, extremely enjoyable. [chelsea.name], on the other hand, isn't enjoying it quite as much."
            chelsea.c "Oh!"
            $ title = "Rub her sex?"
            menu:
              "Yes":
                wt_image chubby_anal_toned_1_14
                "Reaching a hand between her legs, you rub her sex as she slowly rides up and down on your cock. Despite your best efforts, you can't distract her from the feel of your cock filling up her bum. For you, that exact same feeling is incredible. As her ass stretches to accommodate your girth, it feels like you're being swallowed by the tightest pussy in the world."
                $ chelsea.masturbation_count += 1
              "Don't bother":
                wt_image chubby_anal_toned_1_15
                "[chelsea.name]'s not going to enjoy this, so you don't bother trying to suggest she try. You focus simply on enjoying the moment. That's not hard. As her ass stretches to accommodate your girth, it feels like you're being swallowed by the tightest pussy in the world."
            wt_image chubby_anal_toned_1_16
            "[chelsea.name] can't - or won't - ride you quickly with your dick up her ass, which prolongs the fuck, something you're quite pleased with. As it continues, the lube wears away and her hole feels tighter and tighter as the friction gets warmer and warmer, and the pressure in your balls gets harder and harder to ignore. Eventually, to your disappointment and her relief, you can hold out no longer, and flood her insides with your load."
            player.c "[player.orgasm_text]"
            chelsea.c "Oh finally!!"
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.anal_count += 1
            orgasm notify
          "Relent":
            player.c "Okay, [chelsea.name]. No anal for today."
            chelsea.c "Thanks!"
  elif chelsea.anal_status == 5:
    if chelsea.relationship_counter > 4 or chelsea.has_tag('relationship_warnings_shut_off'):
      $ chelsea.training_session()
      call forced_movement(living_room) from _call_forced_movement_235
      summon chelsea no_follows
      wt_image chubby_anal_2_1
      "Finding [chelsea.name] on the sofa, you take a seat beside her and fondle her breast."
      chelsea.c "Feeling frisky?"
      wt_image chubby_anal_2_2
      player.c "Yes, how about you?"
      "Kissing and nuzzling her breast, you remove her top."
      wt_image chubby_anal_2_3
      chelsea.c "Getting there."
      "Stripping her naked, you suck hard on her breast, eliciting a deep moan."
      chelsea.c "Ahhhh  ...  Getting there quickly."
      wt_image chubby_anal_2_4
      player.c "Climb up on top of me and I think you'll get there even faster."
      chelsea.c "Ahhhh  ...  I think you're right."
      wt_image chubby_anal_2_5
      "You are right. Her breathing gets faster and her moans get louder as she rides up and down on your hard shaft."
      chelsea.c "Ahhhhh  ...  Ahhhhh"
      player.c "[chelsea.name], I'm going to stick my finger in your ass when you cum."
      chelsea.c "Do  .. do you have to?"
      player.c "No, but I want to.  Will you let me?"
      chelsea.c "O ... okay, if it turns you on that much."
      wt_image chubby_anal_2_6
      "You time the entry of your finger so it pierces her sphincter just as her climax hits her."
      chelsea.c "Oh!   Aahhhhhh"
      player.c "Feel good, [chelsea.name]?"
      chelsea.c "Still ... still weird."
      player.c "My tongue felt better, didn't it?"
      chelsea.c "Yes, but ..."
      wt_image chubby_anal_2_11
      player.c "No buts ... or more accurately, it's just your butt I want."
      "You lick and tease her rosebud, then slide your tongue into her, probing her anus back and forth as she groans."
      chelsea.c "Ahhh"
      player.c "You remember what I said I was going to do after the next time I tongued your ass?"
      chelsea.c "Y .. yes, but ... please, could you make use of one of my other holes instead? Use my cunt, or use my mouth. I'd enjoy that so much more."
      player.c "But you won't say 'no' if I tell you it's your ass that I want?"
      chelsea.c "I won't say 'no', no, not if it's that important to you. I just wish the rest of me was enough for you."
      $ chelsea.orgasm_count += 1
      $ title = "What do you do?"
      menu:
        "Fuck her mouth":
          wt_image chubby_anal_2_9
          "You roll her over onto her back."
          chelsea.c "Ohh!!  Thank you!!!"
          "She barely gets the words out before you fill her mouth, first with your cock, and then with the contents of your balls."
          player.c "[player.orgasm_text]"
          wt_image chubby_anal_2_13
          "Smiling up at you, she scoops up a trail of jizz that escaped down her chin and licks it up."
          chelsea.c "You can use my mouth anytime."
          "Would she still say that if you dipped your dick in her ass before putting it in her mouth, you wonder."
          sys "[chelsea.name] is happier with your relationship."
          $ chelsea.blowjob_count += 1
          $ chelsea.swallow_count += 1
          $ chelsea.relationship_counter += 1
          orgasm notify
        "Fuck her pussy":
          wt_image chubby_anal_2_12
          chelsea.c "Ohh!!  Thank you!!!"
          "She sighs in relief as she feels you cock penetrate her cunt, still wet from her orgasm."
          "After a few quick thrusts, you make it wetter still. As you cum, though, you can't help but stare at her asshole, gaping open for you after the treatment it received from your tongue."
          player.c "[player.orgasm_text]"
          sys "[chelsea.name] is happier with your relationship."
          $ chelsea.sex_count += 1
          $ chelsea.relationship_counter += 1
          orgasm notify
        "Fuck her ass":
          wt_image chubby_anal_2_14
          "It's taken you so long to get her to this point, you're not going to relent now."
          "Prepared by the ministrations of your tongue, the head of your cock pops easily past her sphincter as she cries out, more in shock than pain."
          chelsea.c "Oh!!!"
          wt_image chubby_anal_2_15
          "Working carefully but steadily, you get a bit more of your cock inside her ..."
          chelsea.c "Oh"
          wt_image chubby_anal_2_16
          "... and then a bit more, her whimpers becoming quieter and quieter ..."
          chelsea.c "oh"
          wt_image chubby_anal_2_17
          "... until her ass opens up wide enough to let you thrust in and out of her properly."
          "Stoically, she accepts her first anal fucking ... and first sperm enema, calling out again only when she feels your load flooding her insides."
          player.c "[player.orgasm_text]"
          chelsea.c "Oh!"
          sys "[chelsea.name] is less happy with your relationship."
          $ chelsea.anal_count += 1
          if chelsea.hypno_re_anal > 1:
            $ chelsea.relationship_counter -= 2
          else:
            $ chelsea.relationship_counter -= 3
          $ chelsea.anal_status = 6
          orgasm notify
    else:
      "You've laid the groundwork necessary to take [chelsea.name]'s anal cherry, but sticking your dick up her ass to claim your prize will still put a strain on your relationship. Better wait until she's feeling better about you and her."
  elif chelsea.anal_status == 4:
    if chelsea.anal_fingering_count == 4:
      $ chelsea.training_session()
      "[chelsea.name]'s starting to get used to having her own finger up her butt. She said she doesn't want your finger there, and she definitely doesn't want your cock there yet. But maybe she's ready to accept another body part there? Are you willing to put your tongue in her ass?"
      $ title = "Will you tongue her butthole?"
      menu:
        "Yes":
          wt_image chubby_anal_3_1
          "The things we'll do for love ... or for kinky sex. Cuddling [chelsea.name] from behind, you whisper in her ear."
          player.c "I want to do something with you."
          wt_image chubby_anal_3_2
          chelsea.c "Mmmmm, okay.  What did you want to do with me?"
          player.c "Something you're going to like, I hope."
          wt_image chubby_anal_3_3
          chelsea.c "Ahhhh ... I like that."
          player.c "You like the feel of my tongue on you?"
          chelsea.c "Yes"
          player.c "Would you like to feel my tongue somewhere else?"
          chelsea.c "You know I would!"
          wt_image chubby_anal_3_4
          player.c "I didn't mean on your pussy, [chelsea.name]."
          chelsea.c "You didn't?  Then ... oh!  Does my butthole interest you that much?"
          player.c "Yes.  I'm going to my tongue in it now, okay?"
          chelsea.c "Oh ... okay,  if you really want to.  Just for a moment."
          wt_image chubby_anal_3_5
          "Swirling your tongue along the edge of her rosebud, you circle closer and closer, until you're gently dipping the tip of your tongue inside her, penetrating her more and more on each probe.  When you finally push through her sphincter ring, you here a satisfying groan escape her throat."
          chelsea.c "Ahhhh"
          player.c "Does that feel good?"
          wt_image chubby_anal_3_6
          chelsea.c "Ahhh ... I don't know what that feels like.  Weird, but not unpleasant.  Ahhhh, get up here and fuck me!"
          player.c "In the ass?"
          chelsea.c "No!!  Normally."
          wt_image chubby_anal_3_7
          "She's sopping wet as you enter her and moaning loudly on every thrust.  It's not going to take her long to cum."
          chelsea.c "Ahhhhh  ...  Ahhhhh"
          wt_image chubby_anal_3_8
          player.c "The next time I tongue your ass, I'm going to take your anal virginity afterwards."
          chelsea.c "Aahhhhhh"
          "She didn't say yes, but she didn't say no, either, and she came hard with the idea of giving her anal cherry to you planted in her head.  For that matter, so did you."
          player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          $ chelsea.orgasm_count += 1
          $ chelsea.anal_status = 5
          orgasm notify
        "Not right now":
          "You're not about to lick your girlfriend's shithole without thinking about whether that's something you're really ready to do. As much fun as it would be to put your dick up [chelsea.name]'s ass, getting her over her hang-up about anal is proving to be a lot of work, and you're not sure you the effort is worth it."
        "Never (shuts this option off)":
          "As fun as it would be to put your dick up [chelsea.name]'s ass, getting her over her hang-up about anal is becoming too much work. Besides, you have your own hang-up about putting your tongue in her shithole, and you'll forego the former to avoid the latter."
          $ chelsea.anal_status = 1
    else:
      "[chelsea.name] needs to get accustomed to the feeling of taking things up her ass before you can proceed any further. Since she won't let you use the butt plug or your finger for that any more, you'll need to wait for opportunities when she'll accept something else instead."
  elif chelsea.anal_status == 3:
    if chelsea.relationship_counter > 4 or chelsea.has_tag('relationship_warnings_shut_off'):
      $ chelsea.training_session()
      call forced_movement(living_room) from _call_forced_movement_236
      summon chelsea no_follows
      if chelsea.hypno_re_anal > 1:
        $ chelsea.relationship_counter -= 1
      else:
        $ chelsea.relationship_counter -= 2
      wt_image chubby_anal_2_1
      "Finding [chelsea.name] on the sofa, you take a seat beside her and boldly extract her tit from under her top."
      chelsea.c "Hi!!  Did you want something?"
      wt_image chubby_anal_2_2
      player.c "You."
      "Kissing and nuzzling her breast, you remove her top completely ..."
      wt_image chubby_anal_2_3
      "... followed by the rest of her clothes."
      chelsea.c "Ahhhh"
      wt_image chubby_anal_2_4
      player.c "Get up here and fuck me."
      chelsea.c "Gladly."
      "She moans as she settles onto your hard cock ..."
      chelsea.c "Ahhhhh"
      wt_image chubby_anal_2_5
      "...and groans some more, louder, as she rides you, bucking up and down your hard shaft as you suckle at her teat."
      chelsea.c "Ahhhhh  ...   Ahhhhh"
      wt_image chubby_anal_2_6
      "Just as she's about to cum, you reach behind her and push a finger into her ass. It shocks her, but not enough to stop her impending climax that's washing over her."
      chelsea.c "Oh!   Aahhhhhh  ...  Oh, take it out!  Take it out!!"
      player.c "Why?  It didn't stop you from cumming.  Didn't it feel good?"
      chelsea.c "No ... I mean ... I don't know.  It just feels wrong!  Take it out!!"
      wt_image chubby_anal_2_7
      "She gasps at the small popping sound your finger makes as you extract it, then climbs off you."
      chelsea.c "Oh!"
      $ chelsea.sex_count += 1
      $ chelsea.orgasm_count += 1
      $ title = "She came but you didn't. Change that?"
      menu:
        "Fuck her pussy":
          wt_image chubby_anal_2_8
          "As she dismounts, you roll her onto her back and fuck her, remembering the feel of her ass gripping your finger as you plow her cunt."
          wt_image chubby_anal_2_10
          "As you're about to cum, you pull out, and spray your seed over her naked body."
          player.c "[player.orgasm_text]"
          "[chelsea.name], however, has other things on her mind besides the feel of your warm sperm wetting her body."
          $ chelsea.sex_count += 1
          orgasm notify
        "Fuck her mouth":
          wt_image chubby_anal_2_9
          "As she dismounts, you straddle her chest.  [chelsea.name] opens her mouth to receive you, and as her lips wrap around you, you can't help but imagine that your cock had just come from her ass, rather than her pussy."
          wt_image chubby_anal_2_10
          "As you're about to cum, you pull out, and spray your seed over her naked body."
          player.c "[player.orgasm_text]"
          "[chelsea.name], however, has other things on her mind besides the feel of your warm sperm wetting her body."
          $ chelsea.blowjob_count += 1
          orgasm notify
        "That's fine":
          change player energy by -energy_short notify
      chelsea.c "Don't stick your finger up my ass again."
      player.c "You just need to get used to it. It felt better than having a toy up there, didn't it?"
      chelsea.c "I don't care. It's weird having you do that to me."
      "Your finger is out, but perhaps her finger could go in? You'll need to be patient and wait for opportunities to get her used to having her ass penetrated, next time giving her more control over how that penetration takes place."
      sys "[chelsea.name] is less happy with your relationship."
      $ chelsea.anal_fingering_count += 1
      $ chelsea.anal_status = 4
    else:
      "[chelsea.name]'s not feeling good enough about your relationship for you to safely introduce her to more butt play. Try again later when she's feeling better about you and her."
  call character_location_return(chelsea) from _call_character_location_return_49
  return

# Dominate Actions
label chelsea_dominate:
  if chelsea.dominate_status == 8:
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    "[chelsea.name] doesn't enjoy it when you dominate her, but as long as the rest of your relationship remains strong, she'll put up with it, for you."
    $ title = "How do you want to dominate her?"
    menu menu_chelsea_dominate_1:
      "Rough blowjob":
        wt_image chubby_hypno_gf_toned_8
        "You find [chelsea.name] getting dressed for work."
        chelsea.c "I was just getting ready to head to the office."
        player.c "Not until I'm finished with you, fucktoy.  Get your tits out."
        wt_image chubby_hypno_gf_toned_9
        "She hesitates just a minute, then realizing you're probably not about to tie her up, it's faster to go along with you."
        player.c "Good, now get on your knees and open your mouth."
        wt_image chubby_hypno_gf_toned_10
        "She gets into position as you remove your pants."
        wt_image chubby_hypno_gf_toned_11
        "She offers no resistance as you penetrate her parted lips ..."
        wt_image chubby_hypno_gf_toned_12
        "... pushing yourself forward until your cockhead is firmly lodged in the back of her throat."
        wt_image chubby_hypno_gf_toned_13
        "Then gripping her by the hair, you pull her head back and forth along your shaft, masturbating yourself with her lips as she watches you silently."
        wt_image chubby_hypno_gf_toned_16
        "She stays like that, letting you use her for your pleasure, until the boiling in your balls can no longer be ignored."
        $ title = "Where do you cum?"
        menu:
          "In her mouth":
            wt_image chubby_hypno_gf_toned_14
            "Still jerking her head back and forth along your shaft, you rub her lips and tongue along your cock until you can hold out no longer, flooding her mouth with your seed."
            player.c "[player.orgasm_text] ... That's a good fucktoy.  You can go to work now."
            $ chelsea.swallow_count += 1
          "On her":
            wt_image chubby_hypno_gf_toned_15
            "Pulling her mouth off of your cock, you lean her backwards and release your load."
            player.c "[player.orgasm_text] ... That's a good fucktoy.  You can go to work now."
        $ chelsea.dommed_count += 1
        $ chelsea.blowjob_count += 1
        orgasm notify
      "Rough sex":
        wt_image chelsea.image
        player.c "Out of your clothes. On all fours, ass in the air, fucktoy."
        wt_image chubby_gf_toned_1_12
        "She scrambles out of her clothes and kneels naked in front of you, sneaking a quick look back, hoping that you'll be gentle."
        wt_image chubby_dominate_2_7
        "You aren't. She screams out as you penetrate her still mostly dry sex. It's not enough to tear her, but it is enough to hurt."
        chelsea.c "Oww!!!"
        wt_image chubby_dominate_2_8
        "The rest of the fuck is easier on her, but only because her body moistens quickly, more in self-defense than arousal. She never gets anywhere close to cumming, but this isn't about her, it's about you."
        "Grabbing her by the hair at the back of her head, you ride her, hard and fast, until you've taken your fill of pleasure from your fucktoy."
        player.c "[player.orgasm_text]"
        "She groans in relief as she feels your cum spurt inside her, knowing the fuck is over."
        chelsea.c "Oh!"
        $ chelsea.dommed_count += 1
        $ chelsea.sex_count += 1
        orgasm notify
      "Gag and fuck her":
        if dungeon.has_item(gags):
          $ chelsea.dommed_count += 1
          wt_image chubby_dominate_7_1
          "You catch [chelsea.name] just as she's arriving home from work."
          wt_image chubby_dominate_7_15
          player.c "It's about time you got back, fucktoy."
          wt_image chubby_dominate_7_16
          chelsea.c "Why, what ..."
          wt_image chubby_dominate_7_2
          chelsea.c "... mmphhh"
          "You cut her impending question short by inserting a ball gag in her mouth."
          wt_image chubby_dominate_7_3
          player.c "What am I going to do with you? Is that what you were about to ask? Anything I want, fucktoy."
          $ title = "What do you want to do with her?"
          menu:
            "Have her jerk you off":
              wt_image chubby_dominate_7_14
              player.c "Put your hand in my pants and make me feel good, fucktoy."
              "Her grip is firmer than you would have liked. Instead of sliding her soft hand along your shaft, she grabs you and squeezes your shaft hard, as if to forcibly extract the cum from your balls by hydraulic pressure. You're about to correct her, when you realize what she's doing is working."
              wt_image chubby_dominate_7_11
              "Straddling her belly, pull down her top as she keeps squeezing.  The pressure in your balls builds, then boils over, exploding over her in a jet of white cum."
              player.c "[player.orgasm_text]"
              $ chelsea.handjob_count += 1
              orgasm notify
            "Tit fuck her":
              wt_image chubby_dominate_7_12
              "Pushing her backwards you take a boob in each hand and push them together.  Inserting your dick between them, you fuck her breasts, slowly at first, then faster and faster, your hard shaft sliding along her soft flesh until ..."
              wt_image chubby_dominate_7_13
              "... you shower your fucktoy with a physical demonstration of how much you enjoy her tits."
              player.c "[player.orgasm_text]"
              $ chelsea.titfuck_count += 1
              orgasm notify
            "Fuck her":
              wt_image chubby_dominate_7_7
              "Stripping her naked, you position her on all fours and prepare to enter her from behind."
              wt_image chubby_dominate_7_8
              "Your fucktoy is a little wetter than she usually is when you take her this way.  Perhaps she was thinking about sex with you on her trip home from work?"
              $ title = "Wait for her to cum?"
              menu:
                "Wait for her":
                  wt_image chubby_dominate_7_9
                  "It takes some willpower, but you control the sensation building in your balls as her excitement slowly grows."
                  wt_image chubby_dominate_7_8
                  "Eventually you're rewarded for your efforts as [chelsea.name] leaves two pools of fluid on the sheets - one under her drooling mouth, the other under her pussy as her juices drip down off your cock as she cums."
                  chelsea.c "nnnnnnnn"
                  wt_image chubby_dominate_7_10
                  "You only leave one pool of fluid, deep inside her vagina."
                  player.c "[player.orgasm_text]"
                  wt_image chubby_dominate_7_9
                  "This type of domination she could get used to.  She enjoyed today's after-work fuck."
                  sys "[chelsea.name] is happier with your relationship."
                  $ chelsea.orgasm_count += 1
                  $ chelsea.relationship_counter += 0.5
                "Just worry about yourself":
                  wt_image chubby_dominate_7_9
                  "If she was, she's about to be disappointed. Her body may be responding, but not as quickly as yours, and this fuck is for your pleasure, not your toy's."
                  wt_image chubby_dominate_7_10
                  player.c "[player.orgasm_text]"
              $ chelsea.sex_count += 1
              orgasm notify
            "Pleasure her":
              wt_image chubby_dominate_7_4
              "Steadily and insistently you milk her tit, holding her breast in a tight grip as you firmly squeeze and pump her.  The sensation is uncomfortable at first, then gradually becoming more and more pleasurable, until you hear what sounds like a moan through her gag."
              chelsea.c "nnnnn"
              wt_image chubby_dominate_7_5
              "Pushing her backwards, you continue to milk her left tit with your hand while switching her right tit into your mouth.  Her hand at the back of your neck confirms that your treatment of her breasts has moved past the uncomfortable phase and is now well into the enjoyable phase."
              chelsea.c "nnnnn  ...  nnnnnn"
              wt_image chubby_dominate_7_17
              "Rolling her on top of you, you remove her gag so you can better hear her moans as you continue to both pleasure and abuse her breasts."
              wt_image chubby_dominate_7_18
              chelsea.c "Ahhhhh  ...  Ahhhhh"
              wt_image chubby_dominate_7_6
              "Then you flip her back onto her back and really give her something to moan about, lowering your lips and tongue directly onto her clit while she cums like a faucet, her whole body shaking."
              chelsea.c "Aahhhhhh"
              "This type of domination she could get used to.  Treat her like this everyday after work and she'll be a happy little fucktoy."
              sys "[chelsea.name] is happier with your relationship."
              $ chelsea.pleasure_her_count += 1
              $ chelsea.orgasm_count += 1
              $ chelsea.relationship_counter += 0.5
              change player energy by -energy_short
        else:
          "You need to buy ball gags for your dungeon before you can do this with her."
          jump menu_chelsea_dominate_1
      "Dress her up as a slut":
        if chelsea.has_tag('slutwear_gifted'):
          if chelsea.has_tag('little_girl'):
            wt_image chubby_youth_3_2
          elif chelsea.has_tag('bbw'):
            wt_image chubby_bbw_1_1
          else:
            wt_image chubby_visit_toned_3_1
          player.c "Is this how you're planning to dress today?"
          if chelsea.has_tag('little_girl'):
            wt_image chubby_youth_3_1
          elif chelsea.has_tag('bbw'):
            wt_image chubby_bbw_1_2
          else:
            wt_image chubby_toned_portrait_2
          chelsea.c "Is there something wrong with my clothes?"
          player.c "Entirely too respectable for my fucktoy. Go dress like a slut."
          wt_image current_location.image
          "She disappears for a few minutes, then returns wearing the outfit you bought her."
          if chelsea.has_tag('bbw'):
            wt_image chubby_slutwear_2_1
          else:
            wt_image chubby_slutwear_1_16
          chelsea.c "Is this better?"
          if chelsea.has_tag('bbw'):
            wt_image chubby_slutwear_2_2
          else:
            wt_image chubby_slutwear_1_17
          player.c "Much.  You look like a total slut, now, just the way I like my fucktoy."
        else:
          if player.has_item(lingerie) and not chelsea.has_tag('slutwear_gifted'):
            "Dressing your fucktoy up as a slut would be fun, but you'll need to give [chelsea.name] the right outfit to wear."
            $ title = "Gift her the lingerie as slutwear?"
            menu:
              "Yes":
                if chelsea.has_tag('little_girl'):
                  wt_image chubby_youth_3_2
                elif chelsea.has_tag('bbw'):
                  wt_image chubby_bbw_1_1
                else:
                  wt_image chubby_visit_toned_3_1
                player.c "I bought you something, [chelsea.name]."
                if chelsea.has_tag('little_girl'):
                  wt_image chubby_youth_3_8
                elif chelsea.has_tag('bbw'):
                  wt_image chubby_bbw_1_3
                else:
                  wt_image chubby_toned_portrait_2
                chelsea.c "A gift?  What is it?"
                player.c "Something special for my fucktoy to wear.  Go put it on."
                wt_image current_location.image
                "She disappears.  She's gone a long while, longer than should be required to change, but eventually returns wearing the outfit you bought her."
                if chelsea.has_tag('bbw'):
                  wt_image chubby_slutwear_2_1
                else:
                  wt_image chubby_slutwear_1_16
                chelsea.c "Is this how you want me to dress?  It's kinda slutty."
                player.c "Sometimes I want my fucktoy to look like a slut."
                if chelsea.has_tag('bbw'):
                  wt_image chubby_slutwear_2_2
                else:
                  wt_image chubby_slutwear_1_17
                chelsea.c "And act like a slut?"
                player.c "And act the way I tell you to act."
                add tags 'slutwear_gifted' to chelsea
                give 1 lingerie from player to chelsea
              "No":
                pass
        if chelsea.has_tag('slutwear_gifted'):
          $ chelsea.dommed_count += 1
          if chelsea.has_tag('bbw'):
            wt_image chubby_slutwear_2_3
            chelsea.c "What do you want me to do, now that I'm dressed this way?"
            $ title = "What do you want?"
            menu menu_chelsea_bbw_slutwear_menu:
              "Blow job":
                wt_image chubby_slutwear_2_23
                player.c "Open your mouth, fucktoy."
                wt_image chubby_slutwear_2_24
                "As she does, you fill it with your hard cock."
                wt_image chubby_slutwear_2_25
                "Her eyes locked on yours, she does her best to bring you pleasure with her hand, lips and tongue."
                wt_image chubby_slutwear_2_26
                "... until you fill her mouth with cum."
                player.c "[player.orgasm_text]"
                $ chelsea.blowjob_count += 1
                $ chelsea.swallow_count += 1
                orgasm notify
              "Have her dildo herself" if chelsea.has_item(dildo):
                wt_image chubby_slutwear_2_15
                "[chelsea.name] retrieves her dildo and hesitantly pushes it inside."
                wt_image chubby_slutwear_2_16
                "It's a bit difficult for her to relax with you watching her ..."
                wt_image chubby_slutwear_2_17
                "... but as she continues to toy herself, she warms to the eroticism of the situation ..."
                wt_image chubby_slutwear_2_18
                "... and drives the dildo in deeper ..."
                wt_image chubby_slutwear_2_19
                "... and deeper with every thrust."
                wt_image chubby_slutwear_2_20
                "After a while, she's moaning ..."
                chelsea.c "Ahhhh"
                wt_image chubby_slutwear_2_21
                "... and not longer after that, she's cumming."
                wt_image chubby_slutwear_2_22
                chelsea.c "Aahhhhhh"
                wt_image chubby_slutwear_2_20
                "This type of domination she could get used to."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.masturbation_count += 1
                $ chelsea.orgasm_count += 1
                $ chelsea.relationship_counter += 0.5
                change player energy by -energy_very_short notify
              "Have her bare her breasts while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                add tags 'bare_breasts_now' to chelsea
                wt_image chubby_slutwear_2_4
                "You could see her tits through the mesh anyway, but she looks even sluttier like this."
                $ title = "What now?"
                jump menu_chelsea_bbw_slutwear_menu
              "Have her bare her pussy while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                add tags 'bare_pussy_now' to chelsea
                wt_image chubby_slutwear_2_14
                "[chelsea.name] rolls over to give you a view of her sex through the conveniently placed hole in her slutwear."
                wt_image chubby_slutwear_2_5
                $ title = "What now?"
                jump menu_chelsea_bbw_slutwear_menu
              "Have her show you her ass while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                add tags 'showing_ass_now' to chelsea
                wt_image chubby_slutwear_2_6
                "[chelsea.name] slowly turns around ..."
                wt_image chubby_slutwear_2_7
                "... and gives you a good view of her plump ass through her mesh slutwear."
                $ title = "What now?"
                jump menu_chelsea_bbw_slutwear_menu
              "Have her kneel while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                add tags 'kneeling_now' to chelsea
                wt_image chubby_slutwear_2_8
                "[chelsea.name] grins as she kneels in front of you."
                $ title = "Should she get lower?"
                menu:
                  "No, this is good":
                    pass
                  "Yes, put her down on all fours":
                    wt_image chubby_slutwear_2_9
                    player.c "Lower, fucktoy.  I want my slut on her hands as well as her knees."
                    wt_image chubby_slutwear_2_10
                $ title = "What now?"
                jump menu_chelsea_bbw_slutwear_menu
              "Just look at her today" if chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                chelsea.c "Are you just going to stare at me?"
                player.c "Yes. Today I just want to enjoy the view of my slutty fucktoy displaying herself for me."
                "[chelsea.name] giggles. This type of domination she doesn't mind so much."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
                change player energy by -energy_very_short notify
              "Freeze her" if chelsea.has_tag('trigger_implanted') and not chelsea.has_any_tag('bare_breasts_now', 'showing_ass_now', 'bare_pussy_now', 'kneeling_now'):
                add tags 'frozen' to chelsea
                wt_image chubby_slutwear_2_2
                player.c "[chelsea.trigger_phrase], fucktoy.  Expose yourself and don't move again until I tell you."
                wt_image chubby_slutwear_2_11
                $ title = "Leave her like this?"
                menu menu_chelsea_bbw_slutwear_frozen_menu:
                  "Yes, this is good":
                    $ chelsea.change_image('chubby_slutwear_2_11')
                  "Tell her to expose her pussy":
                    wt_image chubby_slutwear_2_12
                    menu:
                      "Yes, this is good":
                        $ chelsea.change_image('chubby_slutwear_2_12')
                      "Tell her to spread herself open":
                        wt_image chubby_slutwear_2_13
                        menu:
                          "Yes, this is good":
                            $ chelsea.change_image('chubby_slutwear_2_13')
                          "Maybe kneeling was better after all":
                            wt_image chubby_slutwear_2_11
                            jump menu_chelsea_bbw_slutwear_frozen_menu
                "It's nice having a slutty fucktoy as a decoration.  She really pulls the rest of the room together."
          else:
            wt_image chubby_slutwear_1_18
            chelsea.c "What do you want me to do, now that I'm dressed this way?"
            $ title = "What do you want?"
            menu menu_chelsea_toned_slutwear_menu:
              "Tit job":
                wt_image chubby_slutwear_1_30
                "[chelsea.name]'s had guys sticking their dicks between her tits since her first boyfriend ..."
                wt_image chubby_slutwear_1_13
                "... so she's very familiar with the experience of being used as a fucktoy in this position ..."
                wt_image chubby_slutwear_1_31
                "... and doesn't seem to mind the inevitable outcome when you, like those other men, let yourself go over her chest."
                wt_image chubby_slutwear_1_14
                player.c "[player.orgasm_text]"
                $ chelsea.titfuck_count += 1
                orgasm notify
              "Blow job":
                player.c "Open your mouth, fucktoy."
                wt_image chubby_slutwear_1_29
                "As she does, you fill it with your hard cock."
                wt_image chubby_slutwear_1_11
                "Her eyes locked on yours, she does her best to bring you pleasure with her hand, lips and tongue."
                wt_image chubby_slutwear_1_29
                "And when she succeeds more quickly than she was expecting ..."
                player.c "[player.orgasm_text]"
                wt_image chubby_slutwear_1_12
                "... she opens her mouth to show you that your fucktoy has swallowed your entire offering."
                $ chelsea.blowjob_count += 1
                $ chelsea.swallow_count += 1
                orgasm notify
              "Fuck her":
                wt_image chubby_slutwear_1_24
                "Spreading her legs wide, [chelsea.name] helps guide you inside."
                wt_image chubby_slutwear_1_7
                "She's not particularly wet when you first penetrate her, but she gets progressively wetter as you fuck her."
                $ title = "Wait for her to cum?"
                menu:
                  "Wait for her":
                    wt_image chubby_slutwear_1_8
                    "You have to hold back your own impending orgasm to wait for her to catch up to you."
                    chelsea.c "Ahhhh"
                    wt_image chubby_slutwear_1_25
                    "Eventually your patience is rewarded.  As her climax washes over her, you let yourself go."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_slutwear_1_6
                    player.c "[player.orgasm_text]"
                    wt_image chubby_slutwear_1_26
                    "This type of domination she could get used to.  She appreciated you making sure your fucktoy also enjoyed the fuck."
                    sys "[chelsea.name] is happier with your relationship."
                    $ chelsea.orgasm_count += 1
                    $ chelsea.relationship_counter += 0.5
                  "Just worry about yourself":
                    wt_image chubby_slutwear_1_8
                    "This isn't about her today, it's about you.  She's your fucktoy, and her only purpose right now is to be a sheath for your cock - a purpose she fulfills very well."
                    wt_image chubby_slutwear_1_6
                    player.c "[player.orgasm_text]"
                $ chelsea.sex_count += 1
                orgasm notify
              "Rough sex":
                wt_image chubby_slutwear_1_9
                "She cries out as you flip her around and penetrate her roughly.  She's not completely wet, but she's wet enough not to harm her, and that's enough."
                chelsea.c "Oh!"
                wt_image chubby_slutwear_1_10
                "Gripping her firmly by the hair, you thrust into her, fast and hard."
                player.c "Don't just lie there, fucktoy, make yourself useful."
                wt_image chubby_slutwear_1_27
                "You punctuate your instructions with a hard slap on her ass ... *SMACK*"
                chelsea.c "Ow!!"
                wt_image chubby_slutwear_1_28
                "She gets the idea and starts moving her hips, trying to thrust back at you as hard as you're thrusting into her.  She doesn't quite succeed, but she does well enough to get you off."
                wt_image chubby_slutwear_1_10
                player.c "[player.orgasm_text]"
                "You were the only one who really enjoyed that fuck, but you enjoyed it a lot, and that's what counts."
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                orgasm notify
              "Pleasure her":
                player.c "Spread your legs."
                wt_image chubby_slutwear_1_15
                "Your instructions don't surprise her.  What you do after she complies does.  After a few strokes of your fingers and licks of your tongues, her juices flow freely."
                chelsea.c "Ahhhh"
                wt_image chubby_slutwear_1_32
                "After a few more, her hips are bucking up towards your face, seeking more and firmer contact."
                chelsea.c "Ahhhhh  ...  Ahhhhh"
                wt_image chubby_slutwear_1_33
                "From there, it's about keeping her on the edge as long as you can, before the teasing becomes too much and her body explodes, her whole being focused on the sensation provided by the tip of your tongue."
                chelsea.c "Aahhhhhh"
                wt_image chubby_slutwear_1_15
                "This type of domination she could get used to.  She'll happily be your fucktoy if it involves being teased into orgasm every time."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.pleasure_her_count += 1
                $ chelsea.orgasm_count += 1
                $ chelsea.relationship_counter += 0.5
                change player energy by -energy_short notify
              "Have her bare her breasts while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'on_back_now', 'kneeling_now'):
                add tags 'bare_breasts_now' to chelsea
                wt_image chubby_slutwear_1_1
                player.c "Get your tits out while I decide."
                wt_image chubby_slutwear_1_2
                player.c "Lose the top, too."
                wt_image chubby_slutwear_1_3
                "With a small smile, [chelsea.name] obliges, leaning over to give you a good view as she sits back down."
                wt_image chubby_slutwear_1_19
                $ title = "What now?"
                jump menu_chelsea_toned_slutwear_menu
              "Have her lie on her back while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'on_back_now', 'kneeling_now'):
                add tags 'on_back_now' to chelsea
                wt_image chubby_slutwear_1_22
                player.c "Fucktoys belong on their back.  Lie down."
                wt_image chubby_slutwear_1_23
                player.c "Show off your tits while you're down there."
                wt_image chubby_slutwear_1_5
                $ title = "What now?"
                jump menu_chelsea_toned_slutwear_menu
              "Have her kneel while you decide" if not chelsea.has_any_tag('bare_breasts_now', 'on_back_now', 'kneeling_now'):
                add tags 'kneeling_now' to chelsea
                wt_image chubby_slutwear_1_20
                player.c "Get on your knees while I decide."
                wt_image chubby_slutwear_1_21
                $ title = "Should she get lower?"
                menu:
                  "No, this is good":
                    pass
                  "Yes, put her down on all fours":
                    player.c "Lower, fucktoy.  I want my slut on her hands as well as her knees."
                    wt_image chubby_slutwear_1_4
                $ title = "What now?"
                jump menu_chelsea_toned_slutwear_menu
              "Just look at her today" if chelsea.has_any_tag('bare_breasts_now', 'on_back_now', 'kneeling_now'):
                chelsea.c "Are you just going to stare at me?"
                player.c "Yes. Today I just want to enjoy the view of my slutty fucktoy displaying herself for me."
                "[chelsea.name] giggles. This type of domination she doesn't mind so much."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
                change player energy by -energy_very_short notify
              "Freeze her" if chelsea.has_tag('trigger_implanted') and not chelsea.has_any_tag('bare_breasts_now', 'on_back_now', 'kneeling_now'):
                add tags 'frozen' to chelsea
                player.c "[chelsea.trigger_phrase], fucktoy.  Spread your legs and don't move again until I tell you."
                wt_image chubby_slutwear_1_34
                $ title = "Leave her like this?"
                menu menu_chelsea_toned_slutwear_frozen_menu:
                  "Yes, this is good":
                    $ chelsea.change_image('chubby_slutwear_1_34')
                  "Tell her to expose her breasts":
                    wt_image chubby_slutwear_1_35
                    menu:
                      "Yes, this is good":
                        $ chelsea.change_image('chubby_slutwear_1_35')
                      "Tell her to expose her pussy":
                        wt_image chubby_slutwear_1_36
                        menu:
                          "Yes, this is good":
                            $ chelsea.change_image('chubby_slutwear_1_36')
                          "Maybe clothed was better after all":
                            wt_image chubby_slutwear_1_34
                            jump menu_chelsea_toned_slutwear_frozen_menu
                "It's nice having a slutty fucktoy as a decoration.  She really pulls the rest of the room together."
          rem tags 'bare_breasts_now' 'showing_ass_now' 'bare_pussy_now' 'on_back_now' 'kneeling_now' from chelsea
        else:
          sys "Dressing your fucktoy up as a slut would be fun, but you'll need to get her the right outfit to wear.  Pick up some lingerie and wait to give it to her until you choose this action again."
          rem tags 'trained_today' 'trained_this_week' from chelsea
      "Discipline her":
        if chelsea.hypno_re_dominate > 1:
          $ chelsea.relationship_counter -= 0.5
        else:
          $ chelsea.relationship_counter -= 1
        $ chelsea.dommed_count += 1
        $ title = "How are you going to discipline her?"
        menu:
          "With a strap" if dungeon.has_item(floggers):
            wt_image chubby_discipline_2_7
            "As she bends over, you wrap some ropes around her. She knows it's going to hurt when you take the time to bind her arms, as it means you don't trust her to keep from reaching back otherwise."
            wt_image chubby_discipline_2_1
            "Finishing the binding of her arms, you lean her forward, head to the ground, lifting her ass up for easy access.  Then you run a strap along her bare flesh as she twitches, hating this moment, wanting you to start so that the strapping can get over, but not wanting you to start because she knows how much it will hurt."
            wt_image chubby_discipline_2_2
            "In the end, the strapping comes when you decide you're ready. [chelsea.name]'s screaming starts with the first sting of the leather against her bare ass ... *slappp*"
            chelsea.c "Owww!!"
            "*slappp*"
            chelsea.c "Owww!!!  Please ... I'll be good."
            "*slappp*"
            chelsea.c "Owww!  You don't have to do this.  I'll do as you say.  I promise!!"
            "*slappp*"
            chelsea.c "Owww!!!  I will!!!"
            "*slappp*"
            chelsea.c "OWWWW!!!!  Please!!!!  Let me show you!!"
            wt_image chubby_discipline_2_1
            "She wants to earn the end of the strapping, and while you might not condone letting her bargain like this, you're finished the strapping anyway.  You could find out how well it's motivated her."
            $ title = "End things now?"
            menu:
              "Have her blow you first":
                player.c "You want to show me?  Okay, fucktoy.  Show me what you can do with your mouth."
                wt_image chubby_discipline_2_3
                "[chelsea.name] scrambles to her knees and sucks you into her mouth, eagerly bobbing her head up and down on your hardening cock. To slow things down, you take control by grabbing her by the back of her hair."
                $ chelsea.blowjob_count += 1
                wt_image chubby_discipline_2_8
                $ title = "Where do you want to cum?"
                menu:
                  "Hair":
                    wt_image chubby_discipline_2_4
                    "Still gripping her by the hair at the back of her head, you hold her head down and shoot your load on top of her. Despite your grip, she manages to look up at you, getting some of your cum on her face in the process."
                    player.c "[player.orgasm_text]"
                    $ chelsea.facial_count += 1
                  "Tits":
                    wt_image chubby_discipline_2_5
                    "[chelsea.name]'s tits are a difficult target to miss.  She seems comfortable having your cum on them."
                    player.c "[player.orgasm_text]"
                  "Face":
                    wt_image chubby_discipline_2_6
                    "As the first spurts of your cum hit her face, [chelsea.name] opens her mouth. You can't resist depositing the rest of your load on the back of her tongue."
                    player.c "[player.orgasm_text]"
                    $ chelsea.facial_count += 1
                  "Mouth":
                    wt_image chubby_discipline_2_3
                    "[chelsea.name] slurps down your cum as fast as your balls can pump it into her."
                    $ chelsea.swallow_count += 1
                $ chelsea.blowjob_count += 1
                orgasm notify
              "Yes, you're done":
                wt_image chubby_discipline_2_2
                "You land a couple of more blows, just so she doesn't think her pleas dictated the timing of when the strapping stops ... *slappp*"
                chelsea.c "OWWW!!!"
                "*slappp*"
                chelsea.c "OWWWW!!!!"
                wt_image chubby_discipline_2_1
                "... then you let her go off alone to nurse her sore bottom and wounded spirit."
                change player energy by -energy_short notify
          "With your hand":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_spank_youth_1_6
            else:
              wt_image chubby_gf_bbw_1_11
            player.c "[chelsea.name], it's time for a spanking."
            if chelsea.has_tag('little_girl'):
              wt_image chubby_spank_youth_1_7
            else:
              wt_image chubby_gf_bbw_1_42
            chelsea.c "Why??"
            if chelsea.has_tag('little_girl'):
              wt_image chubby_spank_youth_1_1
            else:
              wt_image chubby_gf_bbw_1_43
            player.c "Because I said so."
            wt_image chubby_spank_youth_1_11
            "[chelsea.name] lies over some pillows and presents her ass to you."
            wt_image chubby_spank_youth_1_4
            "It takes all of her self-control, but she keeps her hands in front of her as you move into position to spank her.  Nervously, she looks back at you, hoping for pity."
            wt_image chubby_spank_youth_1_2
            "None comes until you've finished enjoying her punishment.  She twitches and squirms and eventually cries out as the stinging discomfort in her bum grows with each spank ... *smack* ... *smack* ... *smack*"
            wt_image chubby_spank_youth_1_12
            chelsea.c "ow!"
            "*smack*"
            wt_image chubby_spank_youth_1_2
            chelsea.c "Ow!"
            "*smack*"
            wt_image chubby_spank_youth_1_4
            chelsea.c "Oww!"
            "*smack*"
            wt_image chubby_spank_youth_1_2
            chelsea.c "Oww!!"
            "*smack*"
            wt_image chubby_spank_youth_1_12
            chelsea.c "Owww!!"
            "*smack*"
            wt_image chubby_spank_youth_1_4
            chelsea.c "Ow ow ow ow owww!!!"
            wt_image chubby_spank_youth_1_3
            "When you're done, she rubs her ass and looks at you forlornly, hoping you enjoyed this enough to make up for the pain you caused her."
            $ chelsea.spank_count += 1
            change player energy by -energy_short notify
        "This is one thing you do with her that [chelsea.name] really dislikes. You need to be careful how often you discipline her, as it erodes her comfort with your relationship."
        sys "[chelsea.name] is less happy with your relationship."
      "Tie her up inside":
        $ chelsea.dommed_count += 1
        wt_image chubby_dominate_5_1
        player.c "Getting dressed for work?"
        wt_image chubby_dominate_5_6
        chelsea.c "Yeah, but I don't have to be in the office for a couple of hours. I thought I'd get dressed and head downtown early to do some shopping, first."
        wt_image chubby_dominate_5_2
        chelsea.c "What are you doing with my arms?"
        wt_image chubby_dominate_5_3
        player.c "Getting you dressed and positioned for what I want you to be doing between now and when you need to go to work."
        wt_image chubby_dominate_5_7
        chelsea.c "Are you going to keep me company, at least?"
        wt_image chubby_dominate_5_4
        player.c "I may check in on you from time to time, but don't worry about what I'm going to be doing. You're where I want you, that's all you need to know."
        wt_image chubby_dominate_5_5
        $ chelsea.change_image('chubby_dominate_5_5')
        add tags 'bound_inside_now' to chelsea
      "Tie her up outside":
        $ chelsea.dommed_count += 1
        wt_image chelsea.image
        player.c "You're not working today?"
        chelsea.c "Nope, we have the whole day together, if you want to do something?"
        player.c "It's a beautiful day out. Let's do something outdoors."
        chelsea.c "Okay!"
        call forced_movement(backyard) from _call_forced_movement_237
        summon chelsea no_follows
        wt_image chubby_dominate_6_1
        "This wasn't what she had in mind, but it is what you had in mind, and she's learned to let you have your way when you're in this type of mood, for the good of your overall relationship."
        $ title = "What do you do with her?"
        menu:
          "Torment her":
            wt_image chubby_dominate_6_2
            "It's warm outside, so you make sure you bring [chelsea.name] some water to drink on a regular basis ..."
            wt_image chubby_dominate_6_3
            "... ice cold water right out of the freezer..."
            chelsea.c "oh!!"
            wt_image chubby_dominate_6_4
            "... perfectly suited to chilling off any sensitive body parts that have become warm..."
            chelsea.c "Ohh!!!"
            wt_image chubby_dominate_6_6
            "... the warmer and more sensitive the areas, the better."
            wt_image chubby_dominate_6_5
            chelsea.c "OOHH!!!!"
            wt_image chubby_dominate_6_1
            "It takes a lot of work to keep a staked girl well-watered on a hot day.  You need to re-apply multiple times as the day goes on."
            wt_image chubby_dominate_6_4
            "[chelsea.name] hates that the water torment is the only contact she gets from you ..."
            wt_image chubby_dominate_6_5
            "... and hates even more that she's desperate to feel your fingers on her after the water is applied."
            wt_image chubby_dominate_6_6
            "She wants to stay mad at you, but both of you know what when you finally let her go, what she's going to want to do first is fuck you."
            wt_image chubby_dominate_6_2
            "Overall, that's a wash as far as your relationship goes, and in the meantime you have fun attending to your lawn care."
            change player energy by -energy_short notify
          "Leave her like this":
            wt_image chubby_dominate_6_2
            "Other than making sure she has enough shade not to get burned, and bringing her the occasional drink of water, you leave [chelsea.name] alone to enjoy her quiet time outdoors ..."
            wt_image chubby_dominate_6_1
            "... after all, you have things you want to get done today, and the sight of her outside your window makes for a pleasant backdrop as you do them."
        $ chelsea.change_image('chubby_dominate_6_1')
        add tags 'bound_outside_now' to chelsea
        call forced_movement(living_room) from _call_forced_movement_238
        call character_location_return(chelsea) from _call_character_location_return_50
      "Make her serve her schoolmate Lee" if chelsea.lee_event_status > 2:
        # first, check if safe to proceed
        if chelsea.lee_event_status == 3:
          $ chelsea.temporary_count = 1
          if chelsea.relationship_counter < 6:
            "[chelsea.name] really doesn't want to spend time with Lee. Your relationship may not be strong enough to survive putting her through this. Do you still want to proceed?"
            menu:
              "Proceed to call Lee over anyway":
                pass
              "Do something else":
                $ chelsea.temporary_count = 0
                jump menu_chelsea_dominate_1
        else:
          $ chelsea.temporary_count = 2
          if chelsea.relationship_counter < 4:
            "[chelsea.name] hates having to spend time with Lee.  Your relationship may not be strong enough to survive putting her through this again.  Do you still want to proceed?"
            menu:
              "Proceed to call Lee over anyway":
                pass
              "Do something else":
                $ chelsea.temporary_count = 0
                jump menu_chelsea_dominate_1
        # then go to content if haven't jumped away
        # first sessions with Lee
        if chelsea.temporary_count == 1:
          $ chelsea.temporary_count = 0
          "It's not easy to convince [chelsea.name] to meet with Lee. It's even harder to get her to agree to let Lee do what she wants with [chelsea.name]."
          "If it wasn't for a lingering sense of guilt on [chelsea.name]'s part, she would never have gone along.  In the end, she agrees to do it for you, on the condition that you're present to watch over her."
          call forced_movement(dungeon) from _call_forced_movement_239
          summon chelsea no_follows
          wt_image chubby_lee_2_1
          "On your instructions, [chelsea.name] dresses like a slutty schoolgirl. She's going to make amends for acting like a whore back then, so she's going to dress the part today."
          summon lee no_follows
          wt_image chubby_lee_2_26
          "Lee's own attire could best be described as 'psycho bitch wear', which seems suitable, as you're pretty sure that's exactly what she is. When she sees [chelsea.name], a cold smile crosses her face."
          wt_image chubby_lee_2_2
          lee.c "You dirty tramp. You have no idea how often I've run though in my head what you did to me, and what I would do to you if I ever got my hands on you."
          wt_image chubby_lee_2_3
          "You wouldn't have guessed that she'd be strong enough to do it, but Lee wrestles [chelsea.name] down to the floor, then stands over."
          lee.c "That's where you belong, whore.  At my feet.  The feet of the woman whose boyfriend you fucked.  Or is that one of the women?  Have you been fucking other people's boyfriends, too?"
          chelsea.c "No"
          lee.c "No?  Just me, huh?  Or are you a lying slut as well as a tramp?  I doubt I'm the only woman you've wronged, but if I am, you wronged the wrong woman, bitch, and you're going to pay, starting now."
          wt_image chubby_lee_2_4
          "Lee pulls up [chelsea.name]'s skirt and begins slapping her ass ... *smack* ... *smack* ... *smack*"
          chelsea.c "Oww!!!"
          if dungeon.has_item(floggers):
            wt_image chubby_lee_2_5
            "There's no point in letting Lee hurt her hand, when you have a perfectly good paddle in your dungeon.  Lee's eyes sparkle coldly as she accepts the paddle from you and uses it on [chelsea.name].  *SMACK* ... *SMACK* ... *SMACK*"
            chelsea.c "OWW  OW  OWWW!!!"
          wt_image chubby_lee_2_27
          lee.c "Hurts, doesn't it whore?"
          wt_image chubby_lee_2_28
          chelsea.c "Yes!!"
          lee.c "Good, but I bet it doesn't hurt half as much as you hurt me."
          wt_image chubby_lee_2_6
          lee.c "All because you can't control your whore cunt.  Suck my fingers.  Get them sopping wet.  Not that I should worry.  Your whore cunt is probably sopping wet all the time."
          wt_image chubby_lee_2_7
          "It isn't, but surprisingly, it becomes wet fairly quickly after Lee shoves her fingers inside it."
          if chelsea.lesbian_status < 2:
            "That [chelsea.name] could get aroused by another woman's fingers in these circumstances makes you wonder about her sexuality."
            "If you're interested in encouraging this type of behavior, you should discuss her feelings about women with [chelsea.name] when the two of you are alone."
            $ chelsea.lesbian_status = 1
          elif not chelsea.has_tag('likes_girls'):
            "That [chelsea.name] could get aroused by another woman's fingers in these circumstances suggests there's hope that she'll someday accept embrace her body's response."
            $ chelsea.lesbian_status += 1
          wt_image chubby_lee_2_29
          lee.c "You fucking whore.  You'd cum all over my fingers if I let you.   Okay, you wanna show me how big of a whore you are?  Go on, then.  Show me.  Show me by cumming on my boot."
          wt_image chubby_lee_2_8
          "Lee rolls [chelsea.name] over and presses the toe of her boot against her sex."
          lee.c "Play with yourself, whore.  Fuck yourself to orgasm against my boot like the slut you are."
          wt_image chubby_lee_2_9
          lee.c "Go on, I know you want to.  Tramps like you will hump themselves against anything, whether it's a boot, a lamp post, or someone else's boyfriend.  I know you want to cum, whore, so go ahead."
          wt_image chubby_lee_2_10
          "[chelsea.name] doesn't actually want to cum like this, and in fact doesn't.  But she does leave a suspicious amount of fluids against Lee's boot before Lee tires of this game and rolls her back onto her knees."
          wt_image chubby_lee_2_30
          lee.c "You think you're too good to cum humping my boot, tramp?  I bet you'll cum when I shove my strap-on inside you."
          wt_image chubby_lee_2_11
          "Lee puts on her toy and then pushes the tip of it into [chelsea.name] ..."
          wt_image chubby_lee_2_12
          "... then promptly pulls it out."
          lee.c "But where would the fun be in that?  This is to punish you, so if you're going to cum from my strap-on, whore ..."
          wt_image chubby_lee_2_13
          lee.c "... you'll cum from taking it up the ass."
          chelsea.c "Noo!!!"
          "[chelsea.name] tries to wriggle away ..."
          wt_image chubby_lee_2_14
          "... but Lee follows, keeping her impaled on the dildo up her ass."
          lee.c "Yes!!  Yes, you will take this ass fucking, you fucking whore!  It hurts, doesn't it?"
          chelsea.c "Yes!"
          lee.c "Not as much as you hurt me, whore.  For that matter, not as much as it's going to hurt when I shove it all the way inside you ... now!"
          wt_image chubby_lee_2_15
          chelsea.c "OOWWW!!!!"
          lee.c "There, you could feel that, couldn't you, whore?"
          chelsea.c "YESSS!!!"
          if chelsea.anal_status == 0:
            "This isn't exactly the ideal introduction of anal play to [chelsea.name], but you could follow up with a gentler form of toy play to introduce her to more pleasurable ass fucking.  Anything you introduce her to after this will seem mild."
            $ chelsea.anal_status = 2
          elif chelsea.anal_status == 1:
            "You told [chelsea.name] you'd respect her wishes not to try anal play, but Lee's completely uninterested in what [chelsea.name] wants or doesn't want.  [chelsea.name] doesn't know it, but her ass wouldn't hurt quite so much if she'd let you be the one to introduce it to butt fucking."
          else:
            "The butt plug you bought [chelsea.name] has at least prepared her to take a toy up her ass, but Lee makes sure she's fucking her in a brutal enough manner that it hurts like hell anyway."
          wt_image chubby_lee_2_16
          "Maybe it's the satisfaction of getting revenge after all these years.  Maybe it's the feeling of the strap on between her legs.  Or maybe she just likes fucking women in the ass.  Whatever it is, Lee suddenly throws back her head and climaxes."
          lee.c "MMMMMM"
          wt_image chubby_lee_2_14
          lee.c "Time to say thank you, whore.  Show me how grateful you are for the ass fucking by licking out my sopping wet cunt."
          wt_image chubby_lee_2_17
          "Lee flips [chelsea.name] onto her back and straddles her face before [chelsea.name] can react."
          if chelsea.has_tag('likes_girls') or chelsea.lesbian_status > 7:
            wt_image chubby_lee_2_18
            lee.c "Shit, that feels good, tramp!  You're a good cunt licker, aren't you?"
            wt_image chubby_lee_2_20
            "She wasn't always, but under your influence, she's become one.  She may not like Lee, but faced with Lee's wet pussy in her face and the prospect of further punishment if she doesn't service it, she licks, sucks, and nibbles away ..."
            wt_image chubby_lee_2_19
            "... bringing her tormenter to her second orgasm of her visit and sending her home happy."
            lee.c "MMMMMM"
            "Lee wasn't going to forget this visit anyway.  Now she definitely won't."
            $ chelsea.lee_event_status = 6
          elif chelsea.lesbian_status < 4:
            lee.c "I guess being a tramp only extends to fucking other girls' boyfriends, not the girls themselves.  You're not much of a cunt licker are you?"
            wt_image chubby_lee_2_18
            "She's right, [chelsea.name] isn't much of a cunt licker.  But maybe you can change that, as [chelsea.name]'s willingly working her tongue up and down Lee's wet slit, even if she seems disgusted by the whole procedure.  After a while, Lee's finished with her fun, and let's [chelsea.name] go."
            $ chelsea.lee_event_status = 4
          else:
            lee.c "Mmmm. That feels good, tramp.  Mine isn't the first cunt you've licked, is it?  With a little more effort, you might get me off again. Since you seem to be a bit hesitant, you can stay there till you've cleaned up all my juices."
            wt_image chubby_lee_2_18
            "That takes a while, as [chelsea.name]'s tongue stimulates almost as must fluids from Lee as it cleans off.  [chelsea.name] doesn't look happy about having Lee's cunt in her face, but she licks away anyway until Lee's had enough and finally let's her go."
            $ chelsea.lee_event_status = 5
          if not chelsea.has_tag('likes_girls'):
            if chelsea.hypno_re_lesbian == 2:
              $ chelsea.relationship_counter -= 1
            else:
              $ chelsea.relationship_counter -= 2
          if chelsea.hypno_re_dominate == 2:
            $ chelsea.relationship_counter -= 2
          else:
            $ chelsea.relationship_counter -= 3
          sys "[chelsea.name] is less happy with your relationship."
          $ chelsea.dommed_count += 1
        # additional sessions with Lee (can vary based on lesbian status)
        elif chelsea.temporary_count == 2:
          $ chelsea.temporary_count = 0
          call forced_movement(dungeon) from _call_forced_movement_240
          summon chelsea no_follows
          wt_image chubby_lee_2_1
          if chelsea.has_tag('little_girl'):
            chelsea.c "Why? Why do you want to let her do that to me again, [chelsea.your_name]?"
            player.c "Because it turns me on to dominate my little girl, you know that. Watching your old classmate control you is just another form of domination, and fun for me in a whole different way."
          else:
            chelsea.c "Why? Why do you want to let her do that to me again?  Wearing these stupid clothes, no less."
            player.c "Because it turns me on to dominate you, you know that. Watching your old classmate control you is just another form of domination, and fun for me in a whole different way."
            player.c "Wearing those clothes just shows how far you'll go to please me. And Lee."
          summon lee no_follows
          wt_image chubby_lee_2_30
          "Lee seems to find it fun, too, in a borderline psychotic way.  She investigates your dungeon before turning her attention to [chelsea.name]."
          if dungeon.has_item(floggers):
            wt_image chubby_lee_2_31
            "Picking up one of your canes, Lee flexes it while [chelsea.name] cringes."
          else:
            wt_image chubby_lee_2_2
          lee.c "I'm going to hurt you bad today, whore. Then you're going to thank me with your tongue for teaching a cheating whore like you some manners."
          if dungeon.has_item(suspension_gear):
            wt_image chubby_lee_2_4
            lee.c "Get down on your knees, whore, while I try these ropes out on you."
            wt_image chubby_lee_2_21
            "Lee strips [chelsea.name] and fastens the suspension gear to her, then hoists her into the air."
            if chelsea.has_tag('motivated'):
              lee.c "Good thing you lost that weight. I doubt I ever could've got the fat piggy girl you were in high school up in the air like this."
            else:
              lee.c "This equipment's pretty impressive, to get a fat cow like you up in the air like this."
            if dungeon.has_item(floggers):
              lee.c "Let me hear you scream, whore."
              wt_image chubby_lee_2_22
              "Picking up one of your floggers, Lee twirls it menacingly ... then brings it down sharply on [chelsea.name]'s exposed ass ... *THWAPPP* ... *THWAPPP* ... *THWAPPP*"
              chelsea.c "OWW  OW  OWWW!!!"
              wt_image chubby_lee_2_23
              lee.c "Shit, what a pussy you are.  That barely tickled you and you're squealing like a stuck pig.  Which is what I'm going to make you now.  Get my toy good and wet ..."
            else:
              wt_image chubby_lee_2_23
              lee.c "Get my toy good and wet ..."
            wt_image chubby_lee_2_24
            lee.c "... just don't get your hopes up, whore.  This isn't going in your slutty cunt.  It's going into the one hole I know you can't get off on."
            wt_image chubby_lee_2_25
            "Not like that, she isn't. There's probably no way [chelsea.name]'s ever getting off on having something shoved up her ass, but definitely not the way Lee does it, jamming it in with no preparation other than the bare minimum to keep from tearing her."
            chelsea.c "OOWWWW!!!!"
            wt_image chubby_lee_2_21
          else:
            wt_image chubby_lee_2_3
            lee.c "Get down on your knees, whore, so I can smack that fat ass of yours."
            if dungeon.has_item(floggers):
              wt_image chubby_lee_2_28
              lee.c "Let me hear you scream, whore."
              wt_image chubby_lee_2_5
              "Picking up one of your paddles, Lee brings it down sharply on [chelsea.name]'s ass ... *SMACK* ... *SMACK* ... *SMACK*"
              chelsea.c "OWW  OW  OWWW!!!"
            else:
              wt_image chubby_lee_2_4
              "Lee pulls up [chelsea.name]'s skirt and begins slapping her ass ... *smack*"
              chelsea.c "Ow!"
              "*smack*"
              chelsea.c "Ow!!"
              "*smack*"
              chelsea.c "Oww!!!"
              $ chelsea.spank_count += 1
            wt_image chubby_lee_2_12
            lee.c "Shit, what a pussy you are. That barely tickled you and you're squealing like a stuck pig. Which is what I'm going to make you now."
            wt_image chubby_lee_2_13
            lee.c "Just don't get your hopes up, whore. My strap on isn't going in your slutty cunt. It's going into the one hole I know you can't get off on."
            wt_image chubby_lee_2_14
            "Not like that, she isn't. There's probably no way [chelsea.name]'s ever getting off on having something shoved up her ass, but definitely not the way Lee does it, jamming it in with no preparation other than the bare minimum to keep from tearing her."
            wt_image chubby_lee_2_15
            chelsea.c "OOWWWW!!!!"
            wt_image chubby_lee_2_14
          lee.c "Show me how grateful you are for the ass fucking, whore. Thank me for punishing you, you cheating slut."
          wt_image chubby_lee_2_17
          if chelsea.has_tag('likes_girls') or chelsea.lesbian_status > 7:
            wt_image chubby_lee_2_18
            lee.c "Shit, that feels good, tramp!  You're a good cunt licker, aren't you?"
            wt_image chubby_lee_2_20
            "She wasn't always, but under your influence, she's become one. She may not like Lee, but faced with Lee's wet pussy in her face, she licks, sucks, and nibbles away ..."
            wt_image chubby_lee_2_19
            "... bringing her tormenter to orgasm and sending her home happy."
            lee.c "MMMMMM"
            if chelsea.lee_event_status < 6:
              ## first time at enthusiastic level?
              "Lee wasn't going to forget this visit anyway.  Now she definitely won't."
              $ chelsea.lee_event_status = 6
              $ chelsea.lesbian_status += 1
          elif chelsea.lesbian_status < 4:
            lee.c "I guess being a tramp only extends to fucking other girls' boyfriends, not the girls themselves. You're not much of a cunt licker are you?"
            wt_image chubby_lee_2_18
            "She's right, [chelsea.name] isn't much of a cunt licker. But maybe you can change that, as [chelsea.name]'s willingly working her tongue up and down Lee's wet slit, even if she seems disgusted by the whole procedure.  After a while, Lee's finished with her fun, and let's [chelsea.name] go."
          else:
            lee.c "Mmmm.  That feels good, tramp.  Mine isn't the only cunt you've licked, is it?  With a little more effort, you might get me off again.  Since you seem to be a bit hesitant, you can stay there till you've cleaned up all my juices."
            wt_image chubby_lee_2_18
            "That takes a while, as [chelsea.name]'s tongue stimulates almost as must fluids from Lee as it cleans off. [chelsea.name] doesn't look happy about having Lee's cunt in her face, but she licks away anyway until Lee's had enough and finally let's her go."
            if chelsea.lee_event_status < 5:
              ## first time at reluctant level?
              wt_image chubby_lee_2_17
              lee.c "That's a better effort than last time, tramp.  Show a little more enthusiasm and maybe next time I'll reward you with a nice big load of cunt juice."
              $ chelsea.lee_event_status = 5
              $ chelsea.lesbian_status += 1
          if not chelsea.has_tag('likes_girls') and chelsea.hypno_re_lesbian < 2:
            $ chelsea.relationship_counter -= 1
          if chelsea.hypno_re_dominate == 2:
            $ chelsea.relationship_counter -= 1
          else:
            $ chelsea.relationship_counter -= 2
          sys "[chelsea.name] is less happy with your relationship."
          $ chelsea.dommed_count += 1
          call character_location_return(lee) from _call_character_location_return_51
        if lee.domme_you_status == 0:
            call lee_chelsea_domme_you_question from _call_lee_chelsea_domme_you_question
        call character_location_return(lee) from _call_character_location_return_52
        call character_location_return(chelsea) from _call_character_location_return_53
        call forced_movement(living_room) from _call_forced_movement_241
        change player energy by -energy_short notify
  elif chelsea.dominate_status == 7:
    $ chelsea.dommed_count += 1
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    wt_image chubby_spank_youth_1_6
    "You've been bringing [chelsea.name] along slowly, getting her used to being dominated. Time to finish that process."
    player.c "Ready to be my fucktoy?"
    wt_image chubby_spank_youth_1_1
    chelsea.c "I guess so."
    player.c "Don't just guess.  Get on your knees and open your mouth."
    wt_image chubby_spank_youth_1_8
    "You turn her around and aim a sharp slap on her ass ... *smack*"
    chelsea.c "Ow!"
    player.c "Quicker, fucktoy."
    wt_image chubby_lw_visit_16
    "She drops to her knees and gives you access to her wide open mouth."
    wt_image chubby_lw_visit_17
    "Gripping her by the back of the head and under her jaw, you skull fuck her. It's hard, rough, and impersonal, although she does her best to pleasure you within the limited range of motion you give her, keeping her soft lips wrapped tight against your shaft as you thrust in and out of her mouth."
    player.c "Good, fucktoy. That's getting me nice and hard for the rest of your fucking."
    wt_image chubby_lw_visit_15
    "Positioning on her belly, you tie her in place. Now she has no range of motion, and can't do anything to enhance your pleasure. All she can do is lie there and let you use her."
    wt_image chubby_lw_visit_14
    "A piece of tape over her mouth to muffle her sounds reinforces the situation.  You don't want to listen to her. You don't want her to be anything right now other than a warm hole, available for your use."
    wt_image chubby_lw_visit_15
    "If she stays with you after this, she'll be prepared to accept your dominance whenever you choose to exercise it. If she doesn't, at least you got a good fuck out of the experience."
    player.c "[player.orgasm_text]"
    $ chelsea.blowjob_count += 1
    $ chelsea.sex_count += 1
    $ chelsea.dominate_status = 8
    if chelsea.hypno_re_dominate > 1:
      $ chelsea.relationship_counter -= 2
    else:
      $ chelsea.relationship_counter -= 3
    sys "[chelsea.name] is less happy with your relationship."
    orgasm notify
  elif chelsea.dominate_status == 5:
    if chelsea.youth_skirt_spanking == 2:
      $ chelsea.dommed_count += 1
      "You've spanked [chelsea.name] seriously once she's become your girlfriend. That should be enough to have demonstrated your willingness to punish her corporally when she disobeys you. If you want, you could simply remind her of that or, if you prefer, you could provide a second demonstration."
      $ title = "Spank her anyway?"
      menu:
        "Yes":
          $ chelsea.training_session()
          $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_6
          else:
            wt_image chubby_gf_bbw_1_11
          player.c "I was glad to see you left your legs tied when I told you to.  I like it when you do as you're told."
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_9
          else:
            wt_image chubby_gf_bbw_1_8
          chelsea.c "Umm ... You're welcome, I guess."
          player.c "Do you know what happens if you don't obey me?"
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_10
          else:
            wt_image chubby_gf_bbw_1_42
          "She stares at you, uncertain as to how to respond, then quietly shakes her head no."
          player.c "Bend over, I'm going to show you."
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_7
          else:
            pass
          chelsea.c "Why??"
          player.c "Because I'm serious about wanting you to be my fucktoy. That means following my instructions, when I give them to you, without questioning me. You'll find that easier if you understand the consequences of not obeying me. Now, bend over. I'm not going to tell you again."
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_1
          else:
            wt_image chubby_gf_bbw_1_43
          chelsea.c "You really need this from me?"
          player.c "I want it from you.  I hope that's enough for you."
          if chelsea.has_tag('little_girl'):
            wt_image chubby_spank_youth_1_1
          else:
            pass
          "For the moment, it seems it is.  She hesitates, but eventually she nods."
          $ title = "How are you going to discipline her?"
          menu:
            "With a strap" if dungeon.has_item(floggers):
              wt_image chubby_discipline_2_7
              "As she bends over, you wrap some ropes around her."
              chelsea.c "Why are you tying me?"
              player.c "It's for your own good. It will keep your arms out of the way. If I don't, you'll reach back with your hands, and immediately regret that decision."
              "Finishing the binding of her arms, you lean her forward, head to the ground, lifting her ass up for easy access. Then you run a strap along her bare flesh."
              if chelsea.spanked > 1:
                "She immediately recognizes the feeling."
                chelsea.c "Oh no!!  No, no please!  Not that again!!"
              else:
                "When she feels the leather against her skin, she starts to panic."
                chelsea.c "Oh no!!  No, please!"
              if chelsea.has_tag('little_girl'):
                chelsea.c "Please! You wouldn't do that to your little girl, would you??"
              wt_image chubby_discipline_2_1
              player.c "This is an important lesson, [chelsea.name], I will discipline you to enforce my instructions. You'll find it easier to be my fucktoy when you understand that."
              wt_image chubby_discipline_2_2
              "[chelsea.name] has a low pain tolerance. That's obvious from the first sting of the leather against her bare ass ... *slappp*"
              chelsea.c "Noooo!!"
              "*slappp*"
              chelsea.c "Ow!!  Please ... I'll be good."
              "*slappp*"
              chelsea.c "Owww!  I promise.  I'll do as you say."
              "*slappp*"
              chelsea.c "Owww!!!  I will!!!"
              "*slappp*"
              chelsea.c "OWWWW!!!!  Please!!!!  Let me show you!!"
              "You've made it clear what you expect from her, and demonstrated how far you will go to enforce your will. In the moment, she's acquiesced to your authority, even begged you for the opportunity to show you she'll obey."
              "Now you need to give her some time to reflect and decide for herself if this is something she's really willing to do for you.  You should likely give her some time to think this over, and not rush her."
              $ chelsea.spanked = 2
            "With your hand":
              wt_image chubby_spank_youth_1_11
              "[chelsea.name] lies over some pillows and presents her ass to you."
              wt_image chubby_spank_youth_1_2
              "*smack* ... *smack* ... *smack*"
              wt_image chubby_spank_youth_1_12
              chelsea.c "ow"
              "*smack*"
              wt_image chubby_spank_youth_1_2
              chelsea.c "ow!"
              "*smack*"
              wt_image chubby_spank_youth_1_4
              chelsea.c "Ow!"
              wt_image chubby_spank_youth_1_3
              "She reaches a hand back to protect her sore bottom and turns her head to look at you."
              chelsea.c "That hurts!"
              wt_image chubby_spank_youth_1_14
              player.c "It's meant to. If I need to, I'll discipline you to enforce my instructions.  You'll find it easier to be my fucktoy when you understand that."
              if chelsea.has_tag('little_girl'):
                wt_image chubby_spank_youth_1_13
                chelsea.c "Your little girl will be good, [chelsea.your_name].  You don't need to spank me."
                player.c "You can show me that by taking your hand away and letting me finish my lesson."
              else:
                wt_image chubby_spank_youth_1_3
                player.c "Take your hand away and don't interrupt my discipline again, or it'll continue for far longer."
              wt_image chubby_spank_youth_1_12
              "Reluctantly, she takes her hand away and you resume the spanking.  She doesn't try to stop you again, but she can't help but cry out after each blow, hoping for pity ... *smack*"
              wt_image chubby_spank_youth_1_2
              chelsea.c "ow!"
              "*smack*"
              wt_image chubby_spank_youth_1_4
              chelsea.c "Ow!"
              "*smack*"
              wt_image chubby_spank_youth_1_2
              chelsea.c "Oww!"
              "*smack*"
              wt_image chubby_spank_youth_1_12
              chelsea.c "Oww!!"
              "*smack*"
              wt_image chubby_spank_youth_1_2
              chelsea.c "Owww!!"
              "*smack*"
              wt_image chubby_spank_youth_1_4
              chelsea.c "Ow ow ow ow owww!!!"
              wt_image chubby_spank_youth_1_5
              "When you finally finish, she curls up in a ball and looks at you, forlornly. You've made it clear what you expect from her. Now she has to decide for herself if this is something she's willing to do for you. You should likely give her some time to think this over, and not rush her."
              $ chelsea.spank_count += 1
          $ chelsea.dominate_status = 7
          if chelsea.hypno_re_dominate > 1:
            $ chelsea.relationship_counter -= 2
          else:
            $ chelsea.relationship_counter -= 3
          sys "[chelsea.name] is less happy with your relationship."
          change player energy by -energy_short notify
        "No, simply remind her":
          wt_image chubby_spank_youth_1_6
          player.c "[chelsea.name], do you remember when I spanked you?"
          wt_image chubby_spank_youth_1_9
          chelsea.c "Yes"
          player.c "Do you want me to spank you again?"
          wt_image chubby_spank_youth_1_7
          chelsea.c "No!"
          player.c "I will, if I need to.  I'll discipline you to enforce my instructions.  I want you to remember that.  You'll find it easier to be my fucktoy when you understand that."
          wt_image chubby_spank_youth_1_1
          "You leave [chelsea.name] alone to contemplate the implications. You've made it clear what you expect from her. Now she has to decide for herself if this is something she's willing to do for you.  You should likely give her some time to think this over, and not rush her."
          $ chelsea.training_session()
          $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
          $ chelsea.dominate_status = 7
          if chelsea.hypno_re_dominate > 1:
            $ chelsea.relationship_counter -= 1
          else:
            $ chelsea.relationship_counter -= 2
          sys "[chelsea.name] is less happy with your relationship."
    else:
      $ chelsea.dominate_status = 6
      if chelsea.spanked > 1:
        "You've given [chelsea.name] a serious spanking in the past and she's proven willing to take it. That, however. was part of her training as your client. It's different now. For her to fully accept your dominance, you need to demonstrate a willingness to punish her corporally when she disobeys you, even when she's your girlfriend."
      else:
        "For [chelsea.name] to fully accept your dominance, you need to demonstrate a willingness to punish her corporally when she disobeys you.  This may be the only time you spank her, but it's important for her to understand you're prepared to do so."
  # back to "if" and out of order to align with possible outcomes in 5
  if chelsea.dominate_status == 6:
    $ chelsea.dommed_count += 1
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_6
    else:
      wt_image chubby_gf_bbw_1_11
    player.c "I was glad to see you left your legs tied when I told you to. I like it when you do as you're told."
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_9
    else:
      wt_image chubby_gf_bbw_1_8
    chelsea.c "Umm ... You're welcome, I guess."
    player.c "Do you know what happens if you don't obey me?"
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_10
    else:
      wt_image chubby_gf_bbw_1_42
    "She stares at you, uncertain as to how to respond, then quietly shakes her head no."
    player.c "Bend over, I'm going to show you."
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_7
    else:
      pass
    chelsea.c "Why??"
    player.c "Because I'm serious about wanting you to be my fucktoy. That means following my instructions, when I give them to you, without questioning me. You'll find that easier if you understand the consequences of not obeying me. Now, bend over. I'm not going to tell you again."
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_1
    else:
      wt_image chubby_gf_bbw_1_43
    chelsea.c "You really need this from me?"
    player.c "I want it from you.  I hope that's enough for you."
    if chelsea.has_tag('little_girl'):
      wt_image chubby_spank_youth_1_1
    else:
      pass
    "For the moment, it seems it is. She hesitates, but eventually she nods."
    $ title = "How are you going to discipline her?"
    menu:
      "With a strap" if dungeon.has_item(floggers):
        wt_image chubby_discipline_2_7
        "As she bends over, you wrap some ropes around her."
        chelsea.c "Why are you tying me?"
        player.c "It's for your own good. It'll keep your arms out of the way. If I don't, you'll reach back with your hands, and immediately regret that decision."
        "Finishing the binding of her arms, you lean her forward, head to the ground, lifting her ass up for easy access. Then you run a strap along her bare flesh."
        if chelsea.spanked > 1:
          "She immediately recognizes the feeling."
          chelsea.c "Oh no!!  No, no please!  Not that again!!"
        else:
          "When she feels the leather against her skin, she starts to panic."
          chelsea.c "Oh no!!  No, please!"
        if chelsea.has_tag('little_girl'):
          chelsea.c "Please!  You wouldn't do that to your little girl, would you??"
        wt_image chubby_discipline_2_1
        player.c "This is an important lesson, [chelsea.name].  I will discipline you to enforce my instructions.  You'll find it easier to be my fucktoy when you understand that."
        wt_image chubby_discipline_2_2
        "[chelsea.name] has a low pain tolerance. That's obvious from the first sting of the leather against her bare ass ...*slappp*"
        wt_image chubby_discipline_2_1
        chelsea.c "Noooo!!"
        wt_image chubby_discipline_2_2
        "*slappp*"
        wt_image chubby_discipline_2_1
        chelsea.c "Ow!!  Please ... I'll be good."
        wt_image chubby_discipline_2_2
        "*slappp*"
        wt_image chubby_discipline_2_1
        chelsea.c "Owww!  I promise.  I'll do as you say."
        wt_image chubby_discipline_2_2
        "*slappp*"
        wt_image chubby_discipline_2_1
        chelsea.c "Owww!!!  I will!!!"
        wt_image chubby_discipline_2_2
        "*slappp*"
        wt_image chubby_discipline_2_1
        chelsea.c "OWWWW!!!!  Please!!!!  Stop!!  I promise I'll do as you say!"
        "You've made it clear what you expect from her, and demonstrated how far you will go to enforce your will. In the moment, she's acquiesced to your authority, even begged you for the opportunity to show you she'll obey.  Now you need to give her some time to reflect and decide for herself if this is something she's really willing to do for you. You should likely give her some time to think this over, and not rush her."
        $ chelsea.spanked = 2
      "With your hand":
        wt_image chubby_spank_youth_1_11
        "[chelsea.name] lies over some pillows and presents her ass to you."
        wt_image chubby_spank_youth_1_2
        "*smack* ... *smack* ... *smack*"
        wt_image chubby_spank_youth_1_12
        chelsea.c "oh!"
        "*smack*"
        wt_image chubby_spank_youth_1_2
        chelsea.c "ow"
        "*smack*"
        wt_image chubby_spank_youth_1_4
        chelsea.c "Ow!"
        wt_image chubby_spank_youth_1_3
        "She reaches a hand back to protect her sore bottom and turns her head to look at you."
        wt_image chubby_spank_youth_1_14
        chelsea.c "That hurts!"
        player.c "It's meant to. If I need to, I'll discipline you to enforce my instructions. You'll find it easier to be my fucktoy when you understand that. Take your hand away and don't interrupt my discipline again, or it'll continue for far longer."
        if chelsea.has_tag('little_girl'):
          wt_image chubby_spank_youth_1_13
          chelsea.c "Your little girl will be good. You don't need to spank me."
          player.c "You can show me that by taking your hand away and letting me finish my lesson."
        wt_image chubby_spank_youth_1_12
        "Reluctantly, she takes her hand away and you resume the spanking. She doesn't try to stop you again, but she can't help but cry out after each blow, looking back at you the whole time, hoping for pity ... *smack*"
        wt_image chubby_spank_youth_1_2
        chelsea.c "ow!"
        "*smack*"
        wt_image chubby_spank_youth_1_4
        chelsea.c "Ow!"
        "*smack*"
        wt_image chubby_spank_youth_1_2
        chelsea.c "Oww!"
        "*smack*"
        wt_image chubby_spank_youth_1_12
        chelsea.c "Oww!!"
        "*smack*"
        wt_image chubby_spank_youth_1_2
        chelsea.c "Owww!!"
        "*smack*"
        wt_image chubby_spank_youth_1_4
        chelsea.c "Ow ow ow ow owww!!!"
        wt_image chubby_spank_youth_1_5
        "When you finally finish, she curls up in a ball and looks at you, forlornly.  You've made it clear what you expect from her. Now she has to decide for herself if this is something she's willing to do for you. You should likely give her some time to think this over, and not rush her."
        $ chelsea.spank_count += 1
    $ chelsea.dominate_status = 7
    if chelsea.hypno_re_dominate > 1:
      $ chelsea.relationship_counter -= 2
    else:
      $ chelsea.relationship_counter -= 3
    sys "[chelsea.name] is less happy with your relationship."
    change player energy by -energy_short notify
  elif chelsea.dominate_status == 4:
    $ chelsea.dommed_count += 1
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    wt_image chubby_dominate_4_4
    "You find [chelsea.name] just coming out of the bathroom."
    wt_image chubby_dominate_4_1
    player.c "All showered and ready for today?"
    chelsea.c "Yes, but I don't have to go in for a few hours. Did you want to do something?"
    wt_image chubby_dominate_4_2
    "She frowns slightly when she sees the ropes in your hand."
    chelsea.c "Do you want to tie my arms again?"
    wt_image chubby_dominate_4_5
    player.c "Not this time.  Get naked and then lie down on the sofa."
    wt_image chubby_dominate_4_6
    "She's too smart to take much relief from your answer, and her suspicions are confirmed as you bind her legs together, immobilizing her."
    wt_image chubby_dominate_4_3
    chelsea.c "I can't walk. I can't even crawl like this. Are you just going to leave me like this until work?"
    player.c "Yes"
    chelsea.c "Why??"
    player.c "Because I like having control over you, and I enjoy knowing that you'll be here until I'm ready to let you go elsewhere."
    chelsea.c "Are you going to fuck me afterwards?"
    player.c "Maybe, if I feel like it. Or I may just get off knowing that you can't leave until I'm ready for you to."
    chelsea.c "I could untie myself. You left me hands free."
    player.c "I know, but you won't, will you?"
    chelsea.c "No, I guess not."
    player.c "That's why I left your hands free. You're still immobilized and under my control, because you're letting yourself be."
    "She ponders that over the next few hours, thinking about why you want this from her, and whether she's willing to continue to give it to you."
    "She doesn't like this turn in your relationship, but she hasn't decided whether she enjoys the rest of the relationship enough to want to do this for you."
    $ chelsea.dominate_status = 5
    if chelsea.hypno_re_dominate > 1:
      $ chelsea.relationship_counter -= 1
    else:
      $ chelsea.relationship_counter -= 2
    sys "[chelsea.name] is less happy with your relationship."
    change player energy by -energy_short notify
  elif chelsea.dominate_status == 3:
    $ chelsea.dommed_count += 1
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    if chelsea.has_tag('little_girl'):
      wt_image chubby_youth_bbw_2_1
    else:
      wt_image chubby_gf_bbw_1_8
    player.c "[chelsea.name], do you need to go to work today?"
    chelsea.c "Not for a few hours. Why?"
    if chelsea.has_tag('little_girl'):
      player.c "Take down your dress."
      wt_image chubby_youth_bbw_2_12
      chelsea.c "Okay. Does this mean you're going to play with me?"
      player.c "Not the way you're thinking."
      wt_image chubby_youth_bbw_2_2
      chelsea.c "Why do you have those ropes?"
      player.c "To take your arms away."
      wt_image chubby_dominate_3_1
      chelsea.c "How long are you going to keep me like this?"
      player.c "Until you need to go to work."
      chelsea.c "Am I supposed to be doing something for you, so you'll untie me?"
      player.c "No, that would give you back power. The point of this exercise is take away your power."
      chelsea.c "But I can't move my arms! What am I supposed to do between now and work?"
      player.c "Whatever you want, within the restrictions I've placed on you. Or just sit there and look pretty for me, if you prefer, although for today I'm not forcing you to stay still. That comes later."
      if chelsea.discipline_count > 0:
        chelsea.c "When you tied me up before, it was to train me. I'm not in training anymore!"
        player.c "Apparently you still are. You're in training to become the little girl I want."
        "[chelsea.name]'s not sure what to make of this. It's not directly sexual the way your previous domination of her was, yet it's clearly sexual on another level."
        "It's also humiliating to have her arms taken away for no reason other than you wanted to take them away, but then she's experienced that before during her training. She just wasn't expecting to experience it again now that she's your little girl, not your client."
        $ chelsea.temporary_count = 2
      else:
        "You've never tied [chelsea.name] up before, and she's not sure what to make of it. It's not directly sexual the way your previous domination of her was, yet it's clearly sexual on another level."
        "It's also humiliating to have her arms taken away for no reason other than you wanted to take them away. It doesn't help that nothing in her past experience with you involved you tying her up for extended periods."
        $ chelsea.temporary_count = 3
    else:
      player.c "Take down your dress."
      wt_image chubby_gf_bbw_1_9
      chelsea.c "Okay. Does this mean you want to do something with me?"
      player.c "Not the way you're thinking."
      wt_image chubby_gf_bbw_1_10
      chelsea.c "Why do you have those ropes?"
      player.c "To take your arms away."
      wt_image chubby_dominate_3_2
      chelsea.c "How long are you going to keep me like this?"
      player.c "Until you need to go to work."
      chelsea.c "Am I supposed to be doing something for you, so you'll untie me?"
      player.c "No, that would give you back power.  The point of this exercise is take away your power."
      chelsea.c "But I can't move my arms!  What am I supposed to do between now and work?"
      player.c "Whatever you want, within the restrictions I've placed on you. Or just sit there and look pretty for me, if you prefer, although for today I'm not forcing you to stay still. That comes later."
      if chelsea.discipline_count > 0:
        chelsea.c "When you tied me up before, it was to train me. I'm not in training anymore!"
        player.c "Apparently you still are. You're in training to become the girlfriend I want."
        "[chelsea.name]'s not sure what to make of this. It's not directly sexual the way your previous domination of her was, yet it's clearly sexual on another level."
        "It's also humiliating to have her arms taken away for no reason other than you wanted to take them away, but then she's experienced that before during her training. She just wasn't expecting to experience it again now that she's your girlfriend, not your client."
        $ chelsea.temporary_count = 2
      else:
        "You've never tied [chelsea.name] up before, and she's not sure what to make of it. It's not directly sexual the way your previous domination of her was, yet it's clearly sexual on another level."
        "It's also humiliating to have her arms taken away for no reason other than you wanted to take them away. It doesn't help that nothing in her past experience with you involved you tying her up for extended periods."
        $ chelsea.temporary_count = 3
    "She's not sure she likes the direction this is going, but if she's otherwise feeling good enough about your relationship, she'll tolerate this for you. For the moment, you've left her a lot to think about and come to grips with as she struggles with the restriction imposed by the bonds."
    sys "[chelsea.name] is less happy with your relationship."
    $ chelsea.dominate_status = 4
    if chelsea.hypno_re_dominate > 1:
      $ chelsea.temporary_count -= 1
    $ chelsea.relationship_counter -= chelsea.temporary_count
    change player energy by -energy_short notify
  elif chelsea.dominate_status == 2:
    $ chelsea.training_session()
    $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
    wt_image chubby_dominate_2_1
    "You find [chelsea.name] dressing."
    player.c "You don't need to put that on."
    chelsea.c "My blouse? Yes, I do. I need to go into the office, I have to work today."
    wt_image chubby_dominate_2_9
    player.c "I'd rather you took it back off and showed me those sexy tits of yours."
    wt_image chubby_dominate_2_2
    chelsea.c "These ones?"
    player.c "Those are the ones.  Lie back."
    wt_image chubby_dominate_2_3
    chelsea.c "I'm not sure I have time for this."
    player.c "Yes, you do. You're my fuck toy, and you'll make time for me whenever I tell you to."
    chelsea.c "Your fucktoy?"
    player.c "Yes, my fucktoy.  That means you'll spread your legs for me when I say so.  Like now."
    wt_image chubby_dominate_2_4
    "She's not completely wet, but she's wet enough for you to enter her without hurting her. It's still a bit uncomfortable for her, though, and she gasps as you split her open."
    chelsea.c "Oh!"
    wt_image chubby_dominate_2_5
    "Your thrusts are hard and possessive, but after a while her body warms up and she starts to respond positively."
    chelsea.c "Ahhhh"
    player.c "I'll fuck you whenever I want, and I'll also fuck you however I want to fuck you, fucktoy.  Roll over."
    wt_image chubby_dominate_2_6
    player.c "All the way over and up on your knees."
    wt_image chubby_dominate_2_7
    "As you plow into her from behind, her cunt gets wetter and wetter, and she's soon moaning loudly."
    chelsea.c "Ahhhh  ...  Ahhhhh"
    wt_image chubby_dominate_2_8
    "Just as she's about to cum, you grip her tightly by the hair and pull her head back as you thrust into her hard."
    player.c "Cum for me, fucktoy."
    chelsea.c "Aahhhhhh"
    player.c "[player.orgasm_text]"
    wt_image chubby_dominate_2_9
    player.c "I hope you have a good day at work, [chelsea.name]."
    "[chelsea.name] is left confused by the experience. Her brain didn't like the way you treated her, but her body responded anyway, and afterwards you went back to treating her the same as you always have, as if nothing unusual had happened."
    sys "Unless you think your relationship is really strong, you should give her some time to process the experience before dominating her again. Spending time with her to improve your relationship with her before then may be a good idea, too."
    sys "[chelsea.name] is less happy with your relationship."
    if chelsea.hypno_re_dominate > 1:
      $ chelsea.relationship_counter -= 1
    else:
      $ chelsea.relationship_counter -= 2
    $ chelsea.dommed_count += 1
    $ chelsea.sex_count += 1
    $ chelsea.orgasm_count += 1
    $ chelsea.dominate_status = 3
    orgasm notify
  elif chelsea.dominate_status == 1:
    "[chelsea.name] signed up to be your girlfriend, not your submissive. If you want to dominate her sexually once in a while, you'll need to talk to her about it, but she may not respond well, especially if you haven't done anything to date to give her a clue that this is something you're interested in."
    $ title = "What do you do?"
    menu:
      "Talk about dominating her":
        $ chelsea.training_session()
        $ chelsea.visit_count -= 1 # to back out the auto-add of a visit
        if chelsea.has_tag('little_girl'):
          wt_image chubby_youth_toned_2_11
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_gf_bbw_2_7
          else:
            wt_image chubby_hypno_gf_toned_1
        player.c "[chelsea.name], I want to talk to you about something."
        chelsea.c "What is it?"
        player.c "Sometimes I enjoy taking control.  It excites me, sexually, to be rough with my partner, to spank her or restrict her freedom by tying her up or gagging her."
        if chelsea.has_tag('little_girl'):
          chelsea.c "Even your little girl?"
          player.c "Even my little girl."
          wt_image chubby_youth_toned_2_2
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_hypno_gf_bbw_6
          else:
            wt_image chubby_hypno_gf_toned_6
        if chelsea.youth_skirt_spanking == 2:
          chelsea.c "I knew you enjoyed spanking me before, so I'm not surprised. But that's not really the relationship I want. Is this that important to you?"
          $ chelsea.temporary_count = 2
        else:
          if chelsea.spanked > 1:
            if chelsea.hypno_re_dominate > 0:
              chelsea.c "I know you spanked me hard when you were training me. I thought that was just part of the training, although somehow I had a sense that you'd want to dominate me again. That's not really the relationship I want. Is this that important to you?"
            else:
              chelsea.c "I know you spanked me hard when you were training me, but I thought that was just part of the training. That's not really the relationship I want. Is this that important to you?"
            $ chelsea.temporary_count = 2
          else:
            if chelsea.hypno_re_dominate > 0:
              chelsea.c "Somehow I had a sense that you'd want to dominate me, so for some reason I'm not surprised. But that's not really the relationship I want. Is this that important to you?"
              $ chelsea.temporary_count = 2
            else:
              if chelsea.youth_skirt_spanking == 1:
                chelsea.c "Where is this coming from? When you spanked me before, I thought it was just some playful fun. Now all of a sudden you want to seriously dominate me?"
                chelsea.c "I know I let you take charge of me in some serious ways from time to time during my training, but that was when I was your client. That's not the relationship I want now. Is this that important to you?"
                $ chelsea.temporary_count = 4
              else:
                chelsea.c "Where is this coming from? I know I let you take charge of me in some serious ways from time to time during my training, but that was when I was your client. That's not the relationship I want now. Is this that important to you?"
                $ chelsea.temporary_count = 4
        sys "Warning: If her relationship with you isn't strong enough, this may prove too much for her, especially if you haven't laid the groundwork for it through your interactions with her in the past."
        $ title = "What do you tell her?"
        menu:
          "Yes, it's that important":
            player.c "Yes, [chelsea.name], it is. I'll bring you along slow, and give you a chance to get used to what I want."
            "She's not enthused about your intentions, but she didn't say no, at least not yet."
            sys "Unless you think your relationship with her is super strong, you may want to give her some time to get used to the idea and rebuild the strength of your relationship from any concerns she may have before you start dominating her."
            sys "[chelsea.name] is less happy with your relationship."
            $ chelsea.relationship_counter -= chelsea.temporary_count
            $ chelsea.dominate_status = 2
          "Not if you feel that way, no (turns this option off)":
            player.c "If that's how you feel, [chelsea.name], then no, it's not that important to me."
            if chelsea.has_tag('little_girl'):
              wt_image chubby_youth_toned_2_1
            else:
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_bbw_2_7
              else:
                wt_image chubby_hypno_gf_toned_7
            chelsea.c "Oh good! Thanks for respecting me and my wishes!!"
            sys "[chelsea.name] is happier with your relationship."
            $ chelsea.relationship_counter += 0.5
            $ chelsea.dominate_status = 0
          "Wait and maybe bring this up again later":
            player.c "I'm not sure, actually.  Let me think about it."
      "Wait for another time":
        pass
      "Forget the whole idea (turns this option off)":
        "There are a lot of things you can do with [chelsea.name] that she would enjoy. There's no point to putting a strain on your relationship by asking for something you know she won't enjoy."
        $ chelsea.dominate_status = 0
  return

# Lesbian Actions
label chelsea_lesbian:
  $ chelsea.temporary_count = 1
  if chelsea.has_tag('likes_girls'):
    $ chelsea.lesbian_outfit += 1
    if chelsea.lesbian_outfit > 4:
      $ chelsea.lesbian_outfit = 1
    if chelsea.lesbian_outfit == 1:
      call chelsea_lesbian_outfit_1 from _call_chelsea_lesbian_outfit_1
    if chelsea.lesbian_outfit == 2:
      call chelsea_lesbian_outfit_2 from _call_chelsea_lesbian_outfit_2
    if chelsea.lesbian_outfit == 3:
      call chelsea_lesbian_outfit_3 from _call_chelsea_lesbian_outfit_3
    if chelsea.lesbian_outfit == 4:
      call chelsea_lesbian_outfit_4 from _call_chelsea_lesbian_outfit_4
  else:
    wt_image chelsea.image
    if chelsea.lesbian_status == 1:
      player.c "[chelsea.name], I think we should find you a girl to play with."
      if chelsea.lesbian_club_count > 0:
        if chelsea.has_tag('little_girl'):
          chelsea.c "You mean a playmate?  Is there someone else who wants to be your little girl?  I'm not sure I want to share you."
          player.c "You don't need to share me.  I just want to watch you with another girl.  Playing."
          chelsea.c "Oh!  You mean, playing playing.  I'm not sure that's a great idea.  I'm into boys, not girls."
          player.c "Are you sure?  You seemed to enjoy that woman's attention at the Club."
          chelsea.c "No!  Not really.  She just surprised me and I didn't want to make a scene. I told you, I've kissed a girl before and it's just not my thing."
          player.c "I think it may be, if you let yourself accept what you're feeling."
        else:
          chelsea.c "What do you mean, play with?  You mean sexually?  I'm not sure that's a great idea.  I like dick, as you may have noticed."
          player.c "That doesn't mean you can't like pussy, too.  You seemed to enjoy that woman's attention at the Club."
          chelsea.c "No!  Not really.  She just surprised me and I didn't want to make a scene.  I told you, I've kissed a girl before and it's just not my thing."
          player.c "I think it may be, if you let yourself accept what you're feeling."
      else:
        if chelsea.bra_fitting_status == 4:
          if chelsea.has_tag('little_girl'):
            chelsea.c "You mean a playmate?  Is there someone else who wants to be your little girl?  I'm not sure I want to share you."
            player.c "You don't need to share me.  I just want to watch you with another girl.  Playing."
            chelsea.c "Oh!  You mean, 'playing' playing.  I'm not sure that's a great idea.  I'm into boys, not girls."
            player.c "Are you sure?  You seemed to enjoy Brenda's attention."
            chelsea.c "No, I didn't!"
            player.c "Sure you did.  Didn't your tits get all tingly when she squeezed them?"
            chelsea.c "That doesn't mean anything.  I admit, I've kissed a girl before, but it didn't do much for me.  It's just not my thing."
            player.c "I think it may be, if you let yourself accept what you're feeling."
          else:
            chelsea.c "What do you mean, play with?  You mean sexually?  I'm not sure that's a great idea.  I like dick, as you may have noticed."
            player.c "That doesn't mean you can't like pussy, too.  You seemed to enjoy Brenda's attention."
            chelsea.c "No I didn't!"
            player.c "Sure you did.  Didn't your nipples stiffen when she squeezed your breasts?"
            chelsea.c "That doesn't mean anything.  I admit, I've kissed a girl before, but it didn't do much for me.  It's just not my thing."
            player.c "I think it may be, if you let yourself accept what you're feeling."
      "She looks sceptical, even a little upset that you would even suggest this. You have some work to do if you want to convince her she's bi-sexual."
      sys "[chelsea.name] is less happy with your relationship."
      $ chelsea.lesbian_status = 2
      $ chelsea.relationship_counter -= 1
      $ chelsea.visit_count -= 1 # to offset gain from 'trained_today'
    else:
      if chelsea.lesbian_status > 7:
        player.c "[chelsea.name], are you finally ready to admit that you enjoy fucking girls?"
        chelsea.c "I guess.  Does that make me a lesbian?"
        player.c "Bi-sexual, I believe.  Unless you've given up on boys?"
        chelsea.c "No!  I like dick too much to ever give up on boys."
        player.c "But you like pussy enough to play with girls, too, if I bring one home for you?"
        chelsea.c "I guess.  Yes."
        player.c "Good.  I may arrange that for you one day."
        add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to chelsea
        call convert(chelsea,'lesbian') from _call_convert_65
        $ chelsea.visit_count -= 1 # to offset gain from 'trained_today'
      else:
        "[chelsea.name]'s not open to sleeping with other women, at least not yet."
        $ title = "What do you suggest?"
        menu:
          "Chat with [elsa.name]" if elsa.has_tag('girlfriend') and elsa.has_tag('likes_girls') and not chelsea.has_tag('lesbian_elsa_chat'):
            wt_image frigid_gf_discussion_1_16
            player.c "[elsa.name], could you join [chelsea.name] and I for a moment?"
            elsa.c "Sure. What's up?"
            player.c "[chelsea.name]'s not sure she's into girls, sexually, but I think she would be, if she just let herself accept her true feelings. You remember you and I had that conversation?"
            wt_image frigid_gf_discussion_1_15
            elsa.c "I sure do.  I wasn't sure I liked sex with anybody, even boys, before I met you. Then when you told me I'd like girls, too, I thought you were nuts. Turns out, though, you were right."
            player.c "Why don't you share your experience with [chelsea.name]?"
            wt_image frigid_gf_discussion_1_13
            elsa.c "Okay"
            wt_image current_location.image
            "[elsa.name] and [chelsea.name] chat by themselves for a while, then [chelsea.name] comes and finds you."
            wt_image chelsea.image
            chelsea.c "Well, [elsa.name]'s done her best to convince me I should become a carpet muncher like her, and I admit she made a compelling case, but I'm not sure this is the right thing for me, even if she seems to enjoy it."
            chelsea.c "One thing I need to make clear, though, is that under no circumstances are [elsa.name] and I ever getting it on for your amusement, nor am I going to have a threesome with you and her. It's weird enough being part of your harem. I'm not about to sleep with your other girlfriends."
            "There's a bit of progress there under all that defensiveness. Also, she's right about her and [elsa.name] not hooking up. There's no artwork for that yet, so don't pursue this hoping to see some."
            $ chelsea.lesbian_status += 1
            add tags 'lesbian_elsa_chat' to chelsea
            $ chelsea.visit_count -= 1 # to offset gain from 'trained_today'
          "Arrange a threesome" if chelsea.lesbian_club_count > 0:
            if chelsea.lesbian_threesome_count == 0:
              player.c "I enjoyed watching you with that couple at the Club.  How about we invite them over for an encore?"
              chelsea.c "They don't play outside the Club.  She told me that, and she seems to be really strict about her rules."
              player.c "Maybe there's somebody else from the Club we could invite over.  Did anyone else catch your eye?"
              chelsea.c "Not really.  Well, there was another woman I talked to while I was there, Faye, who told me her husband was into me."
              player.c "Was she into you, too?"
              chelsea.c "No!  I mean, I doubt it.  She didn't say.  She just said to let her know if I ever wanted to play with them."
              player.c "How about I invite them over, and you can play while I watch?"
              chelsea.c "Okay, if you want."
              call forced_movement(living_room) from _call_forced_movement_242
              summon chelsea no_follows
              summon faye no_follows
              wt_image chubby_threesome_1_1
              "You make arrangements for Faye and her husband to join you later that day. When they arrive, [chelsea.name] shows them around."
              chelsea.c "So this is our house.  Well, my boyfriend's house."
              faye.c "It's very nice."
              wt_image chubby_threesome_1_2
              faye_b "Everything here looks nice.  Your tits, for example."
              wt_image chubby_threesome_1_35
              faye_b "Faye's tits, too.  Don't you think they look nice?"
              if chelsea.lesbian_status > 4:
                wt_image chubby_threesome_1_3
                chelsea.c "Mmmm, yes they do."
                "[chelsea.name] runs her fingers idly across Faye's ample bosom. It's not a lot of contact, but the redhead's nipple stiffens noticeably"
              else:
                chelsea.c "I'm sure guys would find them very sexy."
              wt_image chubby_threesome_1_36
              faye_b "Let's compare."
              wt_image chubby_threesome_1_37
              "[chelsea.name] exposes herself as Faye's husband finishes exposing Faye."
              wt_image chubby_threesome_1_4
              faye_b "Wow, there's no losing here, is there?  Nothing but sexy all around."
              wt_image chubby_threesome_1_38
              chelsea.c "You're pretty sexy, too."
              wt_image chubby_threesome_1_39
              "[chelsea.name] drops to her knees and unbuckles the man's pants as his wife helps."
              wt_image chubby_threesome_1_5
              "Then she looks over at you ..."
              wt_image chubby_threesome_1_40
              "... then she starts to pleasure him, while Faye joins in."
              wt_image chubby_threesome_1_6
              "With [chelsea.name]'s mouth on his shaft and Faye's on his balls, he's not likely to last long, and it'd be nice if there was more opportunity for contact between Faye and [chelsea.name], like the boob-on-boob contact taking place while they blow him."
              wt_image chubby_threesome_1_42
              "[chelsea.name] helps the man finish getting undressed ..."
              wt_image chubby_threesome_1_7
              "... then she leads him and Faye to the sofa."
              wt_image chubby_threesome_1_10
            else:
              "You make arrangements for Faye and her husband to drop by later that day."
              call forced_movement(living_room) from _call_forced_movement_243
              summon chelsea no_follows
              summon faye no_follows
              if chelsea.lesbian_status > 4:
                wt_image chubby_threesome_1_3
                chelsea.c "It's good to see you again."
                "[chelsea.name] runs her fingers idly across Faye's ample bosom.  It's not a lot of contact, but the redhead's nipple stiffens noticeably."
              else:
                wt_image chubby_threesome_1_8
                "Ignoring Faye, [chelsea.name] flirts with her husband."
                chelsea.c "It's good to see you again."
              wt_image chubby_threesome_1_2
              faye_b "It's good to see you, too.  How about we all get comfortable?"
              wt_image chubby_threesome_1_43
            faye_b "Help me undress her."
            if chelsea.lesbian_status > 4:
              wt_image chubby_threesome_1_44
              "[chelsea.name] caresses Faye's legs as she helps strip Faye down."
            else:
              wt_image chubby_threesome_1_9
              "[chelsea.name] helps, but avoids any intimate contact with Faye."
            wt_image chubby_threesome_1_11
            faye_b "Faye's tits are so sexy."
            wt_image chubby_threesome_1_12
            faye_b "I love fucking them ..."
            wt_image chubby_threesome_1_45
            faye_b "... but I'd love it even more if you licked my dick while I do so.  Come closer."
            wt_image chubby_threesome_1_13
            "It seems he intended that as an order, not a request, as he grips [chelsea.name] firmly by the hair and pulls her over."
            if chelsea.lesbian_status > 4:
              wt_image chubby_threesome_1_46
              "[chelsea.name] does as he wants, licking up-and-down along his shaft ..."
              wt_image chubby_threesome_1_14
              "... but when he guides her head lower, she lets her tongue run along both his cock and Faye's boob, triggering a stiffening of Faye's nipple that [chelsea.name] can't help but feel as as her chin brushes across it, following the guidance of Faye's husband's hand."
              wt_image chubby_threesome_1_47
              faye_b "That was nice.  Put me inside her, now."
              wt_image chubby_threesome_1_16
              "As [chelsea.name] does so, she instinctively rubs Faye's genitals gently, as she knows how good that'll feel to Faye as she's being penetrated."
              faye.c "ohhhh"
              wt_image chubby_threesome_1_48
              "[chelsea.name] grins at you as you both watch Faye and her husband fuck."
              wt_image chubby_threesome_1_50
              player.c "Faye would like it if you licked her tit, [chelsea.name]."
              wt_image chubby_threesome_1_18
              "A surprised Faye looks up as see feels [chelsea.name]'s tongue lap against her nipple ..."
              wt_image chubby_threesome_1_52
              "... then cums loudly as [chelsea.name] surprises both of you by sucking hard on the redhead's teat."
              faye.c "ohhhh  ohhhhh  OHHH!!"
            else:
              wt_image chubby_threesome_1_46
              "[chelsea.name] does as he wants, but she's careful to avoid any contact with Faye's boobs as she runs her tongue up-and-down along his shaft, and she resists his efforts to push her head lower, onto Faye's boobs."
              wt_image chubby_threesome_1_47
              faye_b "That was nice.  Put me inside her, now."
              wt_image chubby_threesome_1_15
              "[chelsea.name] does so carefully, avoiding direct contact with Faye's genitals as best she can."
              wt_image chubby_threesome_1_48
              "[chelsea.name] grins at you as you both watch Faye and her husband fuck."
              wt_image chubby_threesome_1_49
              player.c "Faye would like it if you licked her tit, [chelsea.name]."
              wt_image chubby_threesome_1_17
              "As [chelsea.name] ignores you, Faye rubs herself between her legs and soon provides [chelsea.name] with a close up look of her orgasm."
              wt_image chubby_threesome_1_50
              faye.c "ohhhh  ohhhhh  OHHH!!"
            wt_image chubby_threesome_1_19
            "Now it's [chelsea.name]'s turn.  Faye puts her husband's still-hard cock inside your girlfriend ..."
            wt_image chubby_threesome_1_20
            "... then takes [chelsea.name]'s nipple between her lips."
            if chelsea.lesbian_status > 4:
              wt_image chubby_threesome_1_22
              "At first [chelsea.name] seems uncertain what to make of the sensation ..."
              wt_image chubby_threesome_1_54
              "... but when Faye starts to rub her clit ..."
              wt_image chubby_threesome_1_55
              "... [chelsea.name]'s resistance to accepting what her body's feeling erodes away ..."
              wt_image chubby_threesome_1_56
              "... and she finds herself to the combined sensation of Faye's mouth, fingers, and her husband's cock."
              wt_image chubby_threesome_1_57
              chelsea.c "Aahhhhhh"
              wt_image chubby_threesome_1_58
              "You're pretty sure Faye's husband came, too, filling your girlfriend's cunt with his jizz, but you're less concerned about that than you are with [chelsea.name]'s response to cumming with her nipple in another woman's mouth."
              wt_image chubby_threesome_1_24
              "[chelsea.name] evades any attempt to engage her in what happened today.  You know she's starting to enjoy touching and being touched by other women.  She's just not ready to admit it yet."
              if chelsea.lesbian_threesome_count < 2:
                $ chelsea.lesbian_threesome_count = 2
                $ chelsea.lesbian_status += 1
            else:
              wt_image chubby_threesome_1_53
              "[chelsea.name] seems shocked when Faye clamps down on her breast ..."
              wt_image chubby_threesome_1_23
              "... but before she can react, Faye's husband pulls her backward and rubs her clit."
              wt_image chubby_threesome_1_21
              "[chelsea.name]'s overwhelmed by the sensations - a cock in her cunt, a man's fingers on her clit, a woman's mouth on her nipple. The orgasm strikes her hard and fast."
              chelsea.c "Aahhhhhh"
              wt_image chubby_threesome_1_58
              "You're pretty sure Faye's husband came, too, filling your girlfriend's cunt with his jizz, but you're less concerned about that than you are with [chelsea.name]'s response to cumming with her nipple in another woman's mouth."
              wt_image chubby_threesome_1_24
              if chelsea.lesbian_threesome_count == 0:
                "[chelsea.name] evades any attempt to engage her in what happened today.  She knows you were right:  Faye was interested in her, and she did kind of enjoy the contact with Faye.  She's just not ready to admit it yet."
                $ chelsea.lesbian_threesome_count = 1
                $ chelsea.lesbian_status += 1
              else:
                "[chelsea.name] responded to the threesome today the same way she did the last time.  If you want her to change, you'll need to introduce her to new experiences to broaden her horizons and help her reflect on how she really feels about touching and being touched by another woman."
            call character_location_return(faye) from _call_character_location_return_54
            change player energy by -energy_very_short notify
          "Invite Brenda the Bra Fitter for a follow up?" if chelsea.bra_fitting_status > 3 and chelsea.bra_fitting_status < 6:
            wt_image chubby_bra_1_38
            player.c "[chelsea.name], how's your new bra working out.  Does it fit you well?"
            chelsea.c "Pretty good."
            player.c "Not perfect?"
            wt_image chubby_bra_1_39
            chelsea.c "Actually, it's quite comfortable ..."
            wt_image chubby_bra_1_40
            player.c "If it's not perfect, I'll call Brenda over to take a look at it."
            summon brenda
            wt_image chubby_bra_1_22
            brenda.c "Trouble with the new bra?"
            wt_image chubby_bra_1_40
            chelsea.c "It fits quite well."
            player.c "But it's not perfect."
            wt_image chubby_bra_1_41
            brenda.c "No problem.  Probably just a small weight-fluctuation thing.  I'll get that fixed up."
            wt_image chubby_bra_1_8
            brenda.c "Okay, there's a small difference from last time, although most of that seems to be because your nipples are stiffer. I hope I wasn't interrupting something between you and your boyfriend?"
            player.c "It wasn't me.  Perhaps it's you, Brenda?"
            if chelsea.lesbian_status > 4:
              chelsea.c "He's joking."
              player.c "Not at all.  Brenda's very beautiful."
              wt_image chubby_bra_1_23
              brenda.c "Thank you, that's very flattering, but I'm not into men. Besides, you have a beautiful girlfriend right here of your own."
              player.c "Did you hear that, [chelsea.name]?  She finds you beautiful and she doesn't like men, so I'm guessing that means you like girls, Brenda?"
              brenda.c "Yes, but ..."
              player.c "That's interesting, because [chelsea.name]'s recently been exploring her interest in girls."
              chelsea.c "I have not! Don't listen to him, he's just teasing."
              player.c "I am teasing, but I'm also telling the truth.  [chelsea.name]'s still quite shy about it, Brenda, but if you make a move on her, I don't think she'll resist you."
              wt_image chubby_bra_1_27
              brenda.c "Hey, I'm not interested in a threesome with you and your girlfriend.  Like I said ..."
              player.c "You're not into men. Got it. Which means if I stay here, you'll be too shy yourself to make a move on [chelsea.name]. So I'm going to go, and leave the two of you alone. Just know that whatever the two of you get up to, I'm cool with it."
              wt_image chubby_bra_1_28
              player.c "Oh, and Brenda - I meant it about [chelsea.name] being new at this and quite shy. So you'll really need to take charge and show her exactly what you want her to do."
              "You leave, but position yourself close enough to the room to overhear their conversation and peek in unobserved once in a while."
              chelsea.c "I'm sorry about that. I'm not sure what got into him. Did you want to go?"
              brenda.c "No, it's okay. Unless you want me to go?"
              chelsea.c "No ... maybe? I'm not sure. What do you want?"
              brenda.c "I think I want to find out what happens if I ask you to kiss me."
              chelsea.c "Brenda, I ... I'm not that way. Really."
              brenda.c "[chelsea.name], kiss me. I need to know if your boyfriend's right."
              wt_image chubby_bra_1_9
              "[chelsea.name] hesitates, then leans in and gives her a quick peck ..."
              wt_image chubby_bra_1_10
              "... before retreating, as Brenda pursues."
              brenda.c "Mmmm, your boyfriend was right. And you really are shy. I don't know why that's turning me on so much, but it is. Lie down on your back."
              chelsea.c "Why?"
              brenda.c "Just do it, okay?"
              wt_image chubby_bra_1_18
              "Brenda removes her clothes and lies on top of [chelsea.name], exploring her mouth with her tongue ..."
              wt_image chubby_bra_1_30
              "... before lifting her head and looking down at your nervous girlfriend."
              brenda.c "Do you want me to lick your pussy?"
              "[chelsea.name] shakes her head."
              chelsea.c "No"
              wt_image chubby_bra_1_42
              brenda.c "Okay, but I want you to lick mine."
              "Brenda straddles [chelsea.name]'s face, not giving her time to object."
              wt_image chubby_bra_1_31
              "With the two of them fully occupied, you can take a closer look, unobserved."
              wt_image chubby_bra_1_32
              "[chelsea.name]'s licks are tentative, her tongue caressing only the surface of Brenda's labia without ever penetrating it or seeking out her clit. It doesn't matter, though. It's still enough to get Brenda off."
              wt_image chubby_bra_1_33
              brenda.c "oooooooohh!!"
              "You make yourself scarce, knowing you gave them both an experience they'll never forget. For Brenda, you suspect this was a fulfillment of a fantasy she's likely had about every attractive client she's every fitted a bra for."
              wt_image chubby_bra_1_18
              "And for [chelsea.name], it's a demonstration that she doesn't mind girls as much as she thought she did."
              call character_location_return(brenda) from _call_character_location_return_55
              $ chelsea.bra_fitting_status = 6
              $ chelsea.lesbian_status += 1
            else:
              chelsea.c "Stop it, both of you! That's not funny."
              wt_image chubby_bra_1_24
              brenda.c "I'm sorry, I wasn't trying to embarrass you. I was just making a little joke. Let me make a small adjustment to the straps."
              player.c "You did a great job in finding a bra for [chelsea.name], Brenda. It looks fabulous on her."
              brenda.c "Thank you.  I'm sure its easy to find things that look good on [chelsea.name], I just made sure I got her a bra that fit her properly."
              player.c "It is easy to find things that look good on her. I think that's because she has such amazing breasts, but I'm an amateur when it comes to breasts. You're the professional. What do you think?"
              wt_image chubby_bra_1_25
              brenda.c "I'm not sure what you're getting at? Your girlfriend has beautiful breasts. Is that what you wanted to hear?"
              player.c "Not me. [chelsea.name]. I tell her that all the time, but I think it's different for her to hear it from another woman. Especially one who's an expert."
              "You leave them to finish up, but position yourself where you can spy on them."
              wt_image chubby_bra_1_26
              chelsea.c "I'm sorry about that. It's not like him to tease that way. I'm not sure what got into him."
              brenda.c "It's okay."
              "You can't help but notice that the two of them stay in physical contact far longer than is strictly needed to complete the strap adjustment.  Eventually, though, Brenda leaves."
              call character_location_return(brenda) from _call_character_location_return_56
              wt_image current_location.image
              if chelsea.bra_fitting_status == 4:
                "[chelsea.name] evades any attempt to engage her in what happened today. You know that's her way of admitting she knows Brenda was interested in her, and she did kind of enjoy the contact with Brenda. She's just not ready to admit it yet."
                $ chelsea.bra_fitting_status = 5
                $ chelsea.lesbian_status += 1
              else:
                "[chelsea.name] responded the same way to Brenda she did the last time.  If you want her to change, you'll need to introduce her to new experiences to broaden her horizons and help her reflect on how she really feels about being touched by another woman."
            $ chelsea.visit_count -= 1 # to offset gain from 'trained_today'
            change player energy by -energy_short notify
          "Nothing right now":
            "You have no ideas right now that you want to pursue to get [chelsea.name] used to the idea of sleeping with other women. Perhaps you should explore opportunities elsewhere?"
            $ chelsea.temporary_count = 0
  if chelsea.temporary_count == 1:
    $ chelsea.temporary_count = 0
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags, this also advance visit_count by 1 in end_day label
    call character_location_return(chelsea) from _call_character_location_return_57
  return

label chelsea_lesbian_outfit_1:
    wt_image chubby_lesbian_outfit_1_1
    "You pick up Savannah at an out-of-town lesbian bar. You know nothing about her other than she's young and surprisingly eager to pop another woman's lesbian cherry."
    wt_image chubby_lesbian_outfit_1_2
    "Oh, that and [chelsea.name] is totally into her."
    wt_image chubby_lesbian_outfit_1_3
    "When Savannah touches her breasts, [chelsea.name] suddenly gets nervous and looks at you."
    wt_image chubby_lesbian_outfit_1_4
    player.c "It's okay, [chelsea.name].  Just relax and enjoy yourself."
    wt_image chubby_lesbian_outfit_1_6
    "The experience of another woman undressing her seems to send [chelsea.name] into a dreamlike state."
    wt_image chubby_lesbian_outfit_1_5
    "She stays in that same state as Savannah licks her to first one, then a second, and finally a third body shaking orgasm.  Poor Savannah will need to make do with her own fingers, as [chelsea.name] is too exhausted by the experience to reciprocate."
    change player energy by -energy_very_short notify
    return

label chelsea_lesbian_outfit_2:
    wt_image chubby_lesbian_outfit_2_1
    "Once again you go trolling the lesbian bars, looking for a play partner for [chelsea.name]. Dark eyed Adriana catches [chelsea.name]'s eye."
    wt_image chubby_lesbian_outfit_2_2
    "[chelsea.name] wastes no time tackling the smaller woman as soon as she has her in private."
    wt_image chubby_lesbian_outfit_2_3
    "Adriana's breasts are many cup sizes smaller than [chelsea.name]'s. Despite this - or maybe because of this - [chelsea.name] seems fascinated with them."
    wt_image chubby_lesbian_outfit_2_4
    "She also shows a healthy interest in Adriana's pussy."
    wt_image chubby_lesbian_outfit_2_5
    "Just as Adriana is about to explode, [chelsea.name] cruelly slows things down and pulls the dark-haired woman in for a kiss."
    wt_image chubby_lesbian_outfit_2_6
    "Now that she's face to face with it, Adriana is plenty interested in [chelsea.name]'s chest too."
    wt_image chubby_lesbian_outfit_2_7
    "Soon both women are fingering each other to the brink of orgasm.  You think things are going to end that way when..."
    wt_image chubby_lesbian_outfit_2_8
    "... [chelsea.name] rolls the smaller woman on top of her. Adriana floods her mouth with pussy juice as she shakes to a violent orgasm. [chelsea.name] happily sucks up every drop."
    change player energy by -energy_very_short notify
    return

label chelsea_lesbian_outfit_3:
    wt_image chubby_lesbian_outfit_3_1
    "Flower girl Starr looked so innocent, [chelsea.name] couldn't resist inviting her back to your place."
    wt_image chubby_lesbian_outfit_3_2
    "Starr's not completely comfortable with your presence, and for a moment you're worried [chelsea.name] may ask you to leave so she can play with the young blonde on her own."
    wt_image chubby_lesbian_outfit_3_3
    "Fortunately, Starr's urge to touch your girlfriend becomes too insistent ..."
    wt_image chubby_lesbian_outfit_3_4
    "... and you're able to settle in to enjoy the show without objection."
    wt_image chubby_lesbian_outfit_3_5
    "Starr's not quite so innocent as she looks ..."
    wt_image chubby_lesbian_outfit_3_6
    "... as she demonstrates by pulling [chelsea.name]'s head roughly between her legs."
    wt_image chubby_lesbian_outfit_3_7
    "Sadly, her pending climax is derailed when she accidentally makes eye contact with you."
    wt_image chubby_lesbian_outfit_3_8
    "Starr's not willing to give up on her orgasm that easily, though.  She rolls a confused [chelsea.name] over ..."
    wt_image chubby_lesbian_outfit_3_9
    "... and buries her head between the brunette's legs."
    wt_image chubby_lesbian_outfit_3_10
    "In this position the two women are able to eat each other in peace ..."
    wt_image chubby_lesbian_outfit_3_11
    "... without either of their orgasms being impacted by your presence."
    change player energy by -energy_very_short notify
    return

label chelsea_lesbian_outfit_4:
    wt_image chubby_lesbian_outfit_4_1
    "Dylan seems a little young for [chelsea.name] ..."
    wt_image chubby_lesbian_outfit_4_2
    "... but [chelsea.name] doesn't seem to mind ..."
    wt_image chubby_lesbian_outfit_4_3
    "... and clearly Dylan doesn't, either."
    wt_image chubby_lesbian_outfit_4_4
    "The two of you hit it off ..."
    wt_image chubby_lesbian_outfit_4_5
    "Even when the young woman shocks [chelsea.name] by explaining, very matter-of-factly, what she intends to do to her with her strap-on."
    wt_image chubby_lesbian_outfit_4_6
    "[chelsea.name] very gamely goes along with the instructions provided to her ..."
    wt_image chubby_lesbian_outfit_4_7
    "... and exposes herself to the young woman's gaze as she makes the strap-on as wet as she can."
    wt_image chubby_lesbian_outfit_4_8
    "It's a good thing she got it wet, as Dylan displays the impatience of youth, roughly finishing [chelsea.name]'s undressing and ramming the phallus inside her."
    wt_image chubby_lesbian_outfit_4_9
    "It's a little rushed for [chelsea.name]'s taste, but it works for Dylan ...'"
    wt_image chubby_lesbian_outfit_4_10
    "... who cums quickly and loudly while fucking your girlfriend roughly from behind."
    wt_image chubby_lesbian_outfit_4_11
    "Her lust slaked, Dylan rolls [chelsea.name] over and takes some time to warm her up ..."
    wt_image chubby_lesbian_outfit_4_12
    "... before resuming the fucking ..."
    wt_image chubby_lesbian_outfit_4_13
    "... this time at a slower, more gentle pace ..."
    wt_image chubby_lesbian_outfit_4_14
    "... that's more to [chelsea.name]'s liking."
    wt_image chubby_lesbian_outfit_4_15
    chelsea.c "Aahhhhhh"
    wt_image chubby_lesbian_outfit_4_16
    "You thought that might be it, and it seems [chelsea.name] did, too ..."
    wt_image chubby_lesbian_outfit_4_17
    "... but Dylan's 'cock' isn't getting soft anytime soon, and she's not showing any signs of getting tired, or of getting tired of fucking your girlfriend."
    wt_image chubby_lesbian_outfit_4_18
    "You leave the two of them to enjoy the stamina of youth and quality silicone."
    change player energy by -energy_very_short notify
    return

# Events with Lee
label chelsea_lee_encounter_lauren_training:
    if chelsea.lee_event_status == 0:
        if chelsea.has_tag('slavegirl'):
            summon chelsea no_follows
            wt_image chelsea.image
            "On her way out, Lee spots [chelsea.name]."
            lee.c "[chelsea.name]??  What the fuck are you doing here?  Are you his submissive?  Oh this is perfect!  I didn't know he had a whole collection of cheating whores!!"
            wt_image cheater_revenge_3_2
            "Lee turns to look at you."
            lee.c "I don't know why you'd waste your time on a fat, stupid cow like her, but down on her knees is the right place for her.  Maybe I can punish her, next time?  She's even more deserving of a good beating. I'd love to fuck her ass and fuck her up at the same time, then watch her say 'sorry' with her face in my cunt."
            player.c "I take it you know her?"
            lee.c "We went to school together.  You don't want to hear about it."
            $ title = "Do you want to hear about it?"
            menu:
                "Yes, hear the story":
                    player.c "Yes, I do want to hear about it."
                    "Lee sighs."
                    lee.c "This stupid cow went to high school with me.  She was always jealous of me, always sniffing around my boyfriends, trying to interest them in her saggy tits.  Offering to suck them off when I wasn't around."
                    lee.c "Last year of high school was the worst. I was dating this really good looking, dumb as a post guy, and [chelsea.name] wouldn't leave him alone. She was always pestering him, trying to get him to leave me and go with her. Like any guy in his right mind would make that switch."
                    wt_image chubby_lee_1_1
                    lee.c "{i}Graduation day comes around and we're all in a good mood.  We're all like 'Fuck yeah!!  No more school!  Ever!!'{/i}"
                    wt_image chubby_lee_1_13
                    lee.c "{i}I'm hanging out, chilling with my friends, when I start hearing this 'Oh my god!  They aren't??  Shit, they are!  Come see!!'{/i}"
                    wt_image chubby_lee_1_14
                    lee.c "{i}I go see what the fuck is up ...{/i}"
                    wt_image chubby_lee_1_12
                    lee.c "{i}... and this fucking whore is sprawled over the hood of my boyfriend's car like a beached walrus ...{/i}"
                    wt_image chubby_lee_1_15
                    lee.c "{i}... just lying there like a dumb cunt as my moron now ex-boyfriend pumps his spunk over her.{/i}"
                    wt_image chubby_lee_1_16
                    lee.c "{i}I high tailed it out of there as she lay there with a glazed look on her face, no doubt amazed that any guy would stick his dick in her skank cunt.{/i}"
                    wt_image cheater_revenge_3_2
                    lee.c "I never saw my moron ex-boyfriend again.  And I never saw this whore again until today.  Next time I see her, I'll make sure she regrets what she did that day."
                    call character_location_return(lee) from _call_character_location_return_58
                    wt_image chelsea.image
                    "Lee turns and storms out.  It seems her issue with cheaters goes back a long way, and may even have started with [chelsea.name].  It's hard to know how much of what Lee said was true, but the embarrassed look on [chelsea.name]'s face tells you at least some of it was. Lee made it pretty clear she'd love to give [chelsea.name] the same treatment she just gave Lauren.  [chelsea.name] isn't likely to enjoy the experience, but you could set it up sometime, if you're interested."
                "No, you don't care":
                    "She's right, you don't want to hear about it.  You have the gist of the situation, anyway.  Lee knows [chelsea.name] from her past, and has some revenge fantasies she'd love to act out on her. Since they seem to include assplay, [chelsea.name] is sure to hate it.  If you're in the mood, you could set this up sometime."
                    call character_location_return(lee) from _call_character_location_return_59
            call character_location_return(chelsea) from _call_character_location_return_60
            $ chelsea.lee_event_status = 1
        elif chelsea.has_any_tag('girlfriend', 'hypno_girlfriend'):
            summon chelsea no_follows
            wt_image chelsea.image
            "[chelsea.name] arrives home from work just as Lee is leaving."
            call chelsea_lee_backstory from _call_chelsea_lee_backstory
        elif chelsea.has_tag('continuing_actions') and chelsea.relationship_counter > 0:
            summon chelsea no_follows
            wt_image chubby_dominate_7_1
            "[chelsea.name] drops by just as Lee is leaving.  She left something behind at her last visit, and is just stopping over to pick it up.  She arrives at the door at the same time as Lee."
            call chelsea_lee_backstory from _call_chelsea_lee_backstory_1
        else:
            if lee.domme_you_status == 0:
                $ title = "Ask Lee to treat you like she treated [lauren.name]?"
                menu:
                    "Yes":
                        wt_image cheater_revenge_3_10
                        player.c "Would you do that to me, sometime?"
                        lee.c "Do what?"
                        player.c "Punish me, like you just punished her."
                        lee.c "Why would I, I'm not mad at you."
                        player.c "But you enjoyed it.  And I'd enjoy you doing the same to me."
                        lee.c "You're sick.  That wasn't supposed to be fun for her."
                        player.c "And it wasn't.  But it was fun for you, and it'd be fun for me."
                        wt_image cheater_revenge_3_2
                        lee.c "What the fuck's wrong with you?  You want me to bust your balls and you think that'd be fun?  You're pathetic."
                        $ title = "What do you do?"
                        menu:
                            "Admit you're pathetic":
                                player.c "Yes, Mistress.  I'm pathetic."
                                lee.c "How pathetic are you?  I could use a little spending money.  Are you so pathetic that you'd pay me to bust your balls?"
                                $ title = "Are you that pathetic?"
                                menu:
                                    "Yes, Mistress, I'll pay you":
                                        $ lee.domme_you_status = 3
                                        lee.c "It'll cost you 10, but not today.  I'm tired after beating on that stupid whore.  But give me a call sometime and I'll take your money and kick your useless ass."
                                    "No, not that pathetic":
                                        $ lee.domme_you_status = 2
                                        wt_image cheater_revenge_3_10
                                        "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                            "Forget it":
                                $ lee.domme_you_status = 2
                                wt_image cheater_revenge_3_10
                                "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                    "Not now":
                        $ lee.domme_you_status = 2
                    "Never":
                        $ lee.domme_you_status = 1
            call character_location_return(lee) from _call_character_location_return_61
    else:
        if lee.domme_you_status == 0:
            $ title = "Ask Lee to treat you like she treated [lauren.name]?"
            menu:
                "Yes":
                    wt_image cheater_revenge_3_10
                    player.c "Would you do that to me, sometime?"
                    lee.c "Do what?"
                    player.c "Punish me, like you just punished her."
                    lee.c "Why would I, I'm not mad at you."
                    player.c "But you enjoyed it.  And I'd enjoy you doing the same to me."
                    lee.c "You're sick.  That wasn't supposed to be fun for her."
                    player.c "And it wasn't.  But it was fun for you, and it'd be fun for me."
                    wt_image cheater_revenge_3_2
                    lee.c "What the fuck's wrong with you?  You want me to bust your balls and you think that'd be fun?  You're pathetic."
                    $ title = "What do you do?"
                    menu:
                        "Admit you're pathetic":
                            player.c "Yes, Mistress.  I'm pathetic."
                            lee.c "How pathetic are you?  I could use a little spending money.  Are you so pathetic that you'd pay me to bust your balls?"
                            $ title = "Are you that pathetic?"
                            menu:
                                "Yes, Mistress, I'll pay you":
                                    $ lee.domme_you_status = 3
                                    lee.c "It'll cost you 10, but not today.  I'm tired after beating on that stupid whore.  But give me a call sometime and I'll take your money and kick your useless ass."
                                "No, not that pathetic":
                                    $ lee.domme_you_status = 2
                                    wt_image cheater_revenge_3_10
                                    "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                        "Forget it":
                            $ lee.domme_you_status = 2
                            wt_image cheater_revenge_3_10
                            "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                "Not now":
                    $ lee.domme_you_status = 2
                "Never":
                    $ lee.domme_you_status = 1
        call character_location_return(lee) from _call_character_location_return_62
    return

label chelsea_lee_backstory:
    chelsea.c "Lee?  Are you one of his clients??"
    if chelsea.has_tag('little_girl'):
        lee.c "[chelsea.name]? What the fuck are you wearing?? No, I'm not one of his clients. I was just punishing a stupid cheating bitch. I didn't know he had a collection of cheating whores here."
    elif chelsea.has_tag('toned') or chelsea.has_tag('motivated'):
        lee.c "[chelsea.name]? You're not as fat as I remember. You look just as stupid as ever, though. No, I'm not one of his clients. I was just punishing a stupid cheating bitch. I didn't know he had a collection of cheating whores here."
    else:
        lee.c "[chelsea.name]? You're as fat and stupid looking as ever. No, I'm not one of his clients. I was just punishing a stupid cheating bitch. I didn't know he had a collection of cheating whores here."
    wt_image cheater_revenge_3_2
    "Lee turns to look at you."
    lee.c  "Maybe I can punish her, next time?  She's even more deserving of a good beating.  I'd love to fuck her ass and fuck her up at the same time, then watch her say 'sorry' with her face in my cunt."
    if chelsea.has_any_tag('girlfriend', 'hypno_girlfriend'):
        wt_image chelsea.image
    else:
        wt_image chubby_dominate_7_1
    call character_location_return(lee) from _call_character_location_return_63
    "Lee departs, leaving you alone with [chelsea.name]."
    player.c "What was that about?"
    chelsea.c "Lee and I went to school together.  She's a total bitch.  She picked on me all the time."
    player.c "She called you a 'cheating whore'."
    "[chelsea.name] blushes."
    chelsea.c "You don't want to hear about it."
    $ title = "Do you want to hear about it?"
    menu:
        "Yes, hear the story":
            player.c "Yes, I do want to hear about it."
            "[chelsea.name] sighs."
            chelsea.c "I hated Lee.  She was always telling me how fat and ugly and stupid I was. Last year of high school, she was dating this guy.  A giant idiot of a boy, but he used to pay attention to me and flirted with me behind Lee's back."
            wt_image chubby_lee_1_1
            chelsea.c "{i}Graduation day, we're all in a good mood.  School's out, forever!{/i}"
            wt_image chubby_lee_1_2
            chelsea.c "{i}I see Lee's boyfriend and give him a big hug, and he's like 'Hey, where's my graduation present?'{/i}"
            chelsea.c "{i}I tell him, 'I didn't buy you one,' and he just grins and says, 'I didn't want something you can buy.'{/i}"
            chelsea.c "{i}Like I said, everybody's mood was running high, so I pucker up and say, 'Well, how about a kiss then?'{/i}"
            chelsea.c "{i}He says 'Nice, but I bet your kisses feel even better down here.'  And he takes out his cock.  Right there in the school parking lot!{/i}"
            chelsea.c "{i}Look, I was the fat chick in school. And Lee was the hot tramp that all the guys were always buzzing around. And like I said, he'd flirted with me before, behind Lee's back and I admit, I fingered myself to orgasm more than once thinking about him.{/i}"
            wt_image chubby_lee_1_3
            chelsea.c "{i}So, yeah, I knelt down and gave his dick a kiss.  And I swear, that's all I intended to do.{/i}"
            wt_image chubby_lee_1_4
            chelsea.c "{i}But now I'm kneeling there in front of this giant hulk of a boy and the smell of his dick is turning me on.  So I give it a playful lick after I kiss it and he says to me, 'Oh [chelsea.name], that feels amazing!'. 'Really?', I ask.  'Really,' he says.{/i}"
            wt_image chubby_lee_1_5
            chelsea.c "{i}So I start sucking him off.{/i}"
            wt_image chubby_lee_1_6
            chelsea.c "{i}And it occurs to me, 'Someone's going to see us.  Lee's going to find out!' And I realize, I don't care.  I want Lee to know that her boyfriend wanted head from me.{/i}"
            wt_image chubby_lee_1_7
            chelsea.c "{i}Turns out, though, he wanted more than just a blow job. He lifts me up onto the hood of his car, and I start looking around to see who's watching us. 'What are you doing?', I ask him.{/i}"
            wt_image chubby_lee_1_8
            chelsea.c "{i}'Something I've wanted to do for a while', he says.  And suddenly my panties are off and my legs are spread. 'You can't!', I tell him.{/i}"
            wt_image chubby_lee_1_9
            chelsea.c "{i}But then the head of his cock is pressing against me ...{/i}"
            wt_image chubby_lee_1_10
            chelsea.c "{i}... and then he's inside me ...{/i}"
            wt_image chubby_lee_1_11
            chelsea.c "{i}... and then he's fucking me on the hood of his car while my classmates and their parents are milling around ...{/i}"
            wt_image chubby_lee_1_12
            chelsea.c "{i}... and his cock feels so good inside me, I don't even care.{/i}"
            wt_image chubby_lee_1_13
            chelsea.c "{i}I don't remember who saw us first ...{/i}"
            wt_image chubby_lee_1_14
            chelsea.c "{i}... but pretty soon we had a crowd around us.  Some of them were cheering us on, guys were congratulating him on being such a stud ...{/i}"
            wt_image chubby_lee_1_15
            chelsea.c "{i}... and a thoroughly humiliated Lee showed up just in time to watch her boyfriend bust a nut over me in front of our friends and classmates.{/i}"
            wt_image chubby_lee_1_16
            chelsea.c "{i}I felt like shit and couldn't even look at Lee as she started bawling.  She's a total bitch and treated me like dirt all through high school, but I still felt bad, knowing that everyone would remember her as the girl whose boyfriend fucked the fat chick on graduation day.{/i}"
            if chelsea.has_any_tag('girlfriend', 'hypno_girlfriend'):
                wt_image chelsea.image
            else:
                wt_image chubby_dominate_7_1
            chelsea.c "I never saw him again, and didn't care.  He might be a big hulk of a guy, but he's also an idiot.  Plus, who'd want a guy who would fuck another girl in front of your friends like that?  I never saw Lee again, either.  Until today."
            "It seems Lee's issue with cheaters goes back a long way, and may even have started with [chelsea.name].  Lee made it pretty clear she'd love to give [chelsea.name] the same treatment she gave Lauren."
            if chelsea.has_tag('likes_girls'):
                "[chelsea.name] may be into girls, now, but she's unlikely to be interested in spending any time with Lee.  Not just because of the bad blood between them, either.  The threatened ass-fucking is a total turn off for [chelsea.name]."
            else:
                "[chelsea.name], on the other hand, is unlikely to be interested in spending any time with Lee.  She's not into girls period, and especially wouldn't be into Lee given the bad blood between them.  Plus the threatened ass-fucking is a total turn off for [chelsea.name]."
            "Still, you might be able to convince her, if your relationship is strong enough and you lay the groundwork properly."
        "No, you don't care":
            "She's right, you don't want to hear about it. You have the gist of the situation, anyway. Lee's issue with cheaters goes back a long way, and may even have started with [chelsea.name], and she'd love to give [chelsea.name] the same treatment she gave Lauren."
    call character_location_return(chelsea) from _call_character_location_return_64
    $ chelsea.lee_event_status = 3
    return

# Rename Character
label chelsea_rename:
    wt_image chelsea.image
    "As her owner, it's your prerogative to change [chelsea.full_name]'s name, if you want to."
    $ title = "Do you want to change her name?"
    menu:
        "Yes":
            $ title = "What would you like her name to be?"
            $ chelsea.name = renpy.input(_("What is her new name?"))
            $ chelsea.suffix = renpy.input(_("What is her new title, if you want to give her one?"))
            $ title = "Does she get a prefix?"
            menu:
                "Yes":
                    $ chelsea.prefix = renpy.input(_("What is her prefix?"))
                "No":
                    $ chelsea.prefix = ""
            $ chelsea.change_full_name(chelsea.prefix, chelsea.name, chelsea.suffix)
            $ title = "Are you sure you want her new name to be [chelsea.full_name]?"
            menu:
                "Yes":
                    pass
                "No, choose something else":
                    $ chelsea.change_full_name("", "[chelsea.name]", "the Chubby")
                    jump chelsea_rename
        "No":
            pass
    return

# Tell her how to address you
label chelsea_your_name:
    "[chelsea.name] currently refers to you as '[chelsea.your_name]'"
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            $ title = "How should she address you?"
            $ chelsea.your_name = renpy.input(_("What does she call you?"))
        "No":
            pass
    return

# Slavegirl Actions
label chelsea_slavegirl_actions:
    wt_image chelsea.image
    $ title = "What do you want to do with her?"
    menu:
        "Hurt her":
            if dungeon.has_item(gags):
                call forced_movement(dungeon) from _call_forced_movement_244
                summon chelsea no_follows
                wt_image chubby_slave_12
                "[chelsea.full_name]'s a screamer.  With the gag in place, however, you're able to keep the sounds she makes down to a dull roar."
                wt_image chubby_slave_13
                "Then you bind her arms, leaving her large, beautiful tits helpless to receive whatever attention you choose to inflict on them."
                wt_image chubby_slave_3
                "Today, the attention you choose is pain.  Fastening her arms above her head, [chelsea.name] can do nothing more than wait until you've satisfied your sadism for today.  That and scream - which she does loudly, although only muffled sounds escape her gag."
                chelsea.c "NNNNNNNNN!!!!"
                change player energy by -energy_very_short notify
                call character_location_return(chelsea) from _call_character_location_return_65
            else:
                "[chelsea.full_name] is a bit of a screamer. For the sake of the neighbors, you need to buy some gags before you start to seriously hurt her."
        "Tie her up":
            call forced_movement(dungeon) from _call_forced_movement_245
            summon chelsea no_follows
            wt_image chubby_slave_4
            "You spend some quality time with [chelsea.name], carefully binding her into an immovable position. She seems to enjoy the personal attention, especially the time you spend on her hair."
            rem tags 'slave_suspended_now' 'slave_decoration_now' 'slave_dildo_now' 'slave_plugged_now' from chelsea
            add tags 'slave_tied_now' to chelsea
            $ chelsea.change_image('chubby_slave_4')
            call character_location_return(chelsea) from _call_character_location_return_66
        "Suspend her":
            if dungeon.has_item(suspension_gear):
                wt_image chubby_slave_5
                "You carefully wind the ropes back and forth around [chelsea.name]."
                wt_image chubby_slave_6
                "When the ropes are in position, you slowly raise her into the air."
                wt_image chubby_slave_7
                "You finish the tie by binding her arms back to her legs. You let her hang there for some time, enjoying the view of her spinning helplessly in front of you."
                rem tags 'slave_tied_now' 'slave_decoration_now' 'slave_dildo_now' 'slave_plugged_now' from chelsea
                add tags 'slave_suspended_now' to chelsea
                $ chelsea.change_image('chubby_slave_7')
            else:
                "You need to buy suitable suspension gear first."
        "Fuck her":
            wt_image chubby_slave_2
            "You tie [chelsea.name] on her back with her arms pulled up over her head.  She has a hard time reaching orgasm in this position.  Sometimes you help her out by putting some contact on her clit.  Sometimes you don't.  You, on the other hand, always get to cum."
            wt_image chubby_slave_11
            player.c "[player.orgasm_text]"
            $ chelsea.sex_count += 1
            orgasm notify
        "Anal":
            if chelsea.anal_status > 5:
                wt_image chubby_anal_slave_1
                "[chelsea.name] used to have an intense aversion to anal sex.  You've taught her to see things differently."
                wt_image chubby_anal_slave_2
                player.c "Open your ass."
                wt_image chubby_anal_slave_3
                "She still doesn't like having your dick shoved up her butt hole, but she no longer complains about it.  Quite the opposite, actually."
                wt_image chubby_anal_slave_4
                player.c "What do you say, [chelsea.name]?"
                wt_image chubby_anal_slave_5
                chelsea.c "Thank you for using my ass for your pleasure, [chelsea.your_name].  Please fill it with cum."
                wt_image chubby_anal_slave_6
                player.c "[player.orgasm_text]"
                $ chelsea.anal_count += 1
                orgasm notify
            else:
                if player.has_item(butt_plug) and not chelsea.has_item(butt_plug):
                    "[chelsea.name] has an intense aversion to anal, but using a butt plug on her should get her ready to someday accept your cock back there."
                    $ title = "Set the butt plug aside for her anal training?"
                    menu:
                        "Yes":
                            give 1 butt_plug from player to chelsea
                        "No":
                            jump chelsea_slavegirl_actions
                if chelsea.has_item(butt_plug):
                    wt_image chubby_slave_10
                    "[chelsea.name] is so scared of anal penetration you need to tie her down before you can get her butt plug inside her, and then tie the plug in place so she doesn't squirm it out of her ass."
                    "Once you have it firmly inserted, you leave her for a few hours to get used to the sensation. It may take a few sessions, but eventually she'll learn to take things up her ass without fighting it - including your dick."
                    $ chelsea.anal_status += 2
                    change player energy by -energy_very_short notify
                else:
                    "[chelsea.name] has an intense aversion to anal. You'll never get your dick inside her ass until you train her to take things back there. A butt plug would help, or there may be other options."
        "Use her mouth":
            wt_image chubby_discipline_2_3
            "[chelsea.name] dutifully kneels in front of you and lets you use her mouth for your own pleasure."
            wt_image chubby_discipline_2_8
            $ title = "Where do you want to cum?"
            menu:
                "Hair":
                    wt_image chubby_discipline_2_4
                    $ chelsea.facial_count += 1
                "Tits":
                    wt_image chubby_discipline_2_5
                "Face":
                    wt_image chubby_discipline_2_6
                    $ chelsea.facial_count += 1
                "Mouth":
                    wt_image chubby_discipline_2_3
                    $ chelsea.swallow_count += 1
            player.c "[player.orgasm_text]"
            $ chelsea.blowjob_count += 1
            orgasm notify
        "Put her butt plug in her" if chelsea.has_item(butt_plug) and chelsea.anal_status > 5:
            wt_image chubby_slave_10
            "Tying [chelsea.name] up with her butt plug firmly in place reminds her that she belongs to you, now.  All of her."
            rem tags 'slave_tied_now' 'slave_suspended_now' 'slave_decoration_now' 'slave_dildo_now' from chelsea
            add tags 'slave_plugged_now' to chelsea
            $ chelsea.change_image('chubby_slave_10')
        "Put her dildo in her" if chelsea.has_item(dildo):
            wt_image chubby_slave_15
            "When you bought the dildo for her, [chelsea.name] thought it would be to help her get herself off more easily at times when you weren't around.  Now [chelsea.name] only gets to use it when you're around ..."
            wt_image chubby_slave_14
            "... and even then only very rarely to get off.  She gets aroused, yes, anytime you work the dildo in and out of her tied frame.  But getting an orgasm?  Only when you feel like giving her one, and you very rarely do."
            wt_image chubby_slave_8
            "The rest of the time she's left whimpering and moaning and pleading with you with her eyes for the relief she'd so desperately love."
            chelsea.c "Ahhhh  ...  Ahhhh"
            rem tags 'slave_tied_now' 'slave_suspended_now' 'slave_decoration_now' 'slave_plugged_now' from chelsea
            add tags 'slave_dildo_now' to chelsea
            $ chelsea.change_image('chubby_slave_8')
        "Lend her to her schoolmate Lee" if chelsea.lee_event_status > 0:
            if chelsea.lee_event_status == 1:
                call forced_movement(dungeon) from _call_forced_movement_246
                summon chelsea no_follows
                wt_image chubby_lee_2_1
                "You dress [chelsea.name] up like a slutty schoolgirl for Lee's visit.  [lee.name] wants amends for [chelsea.name] acting like a whore in school, so [chelsea.name] may as well be dressed for the part."
                summon lee
                wt_image chubby_lee_2_26
                "Lee's own attire could best be described as 'psycho bitch wear', which seems suitable, as you're pretty sure that's exactly what she is.  When she sees [chelsea.name], a cold smile crosses her face."
                wt_image chubby_lee_2_2
                lee.c "You dirty slut.  You have no idea how often I've run though in my head what you did to me, and what I would do to you if I ever got my hands on you."
                wt_image chubby_lee_2_3
                "You wouldn't have guessed that she'd be strong enough to do it, but Lee wrestles [chelsea.name] down to the floor, then stands over."
                lee.c "That's where you belong, whore.  At my feet.  The feet of the woman whose boyfriend you fucked.  I've waited for this a long time, and now you're going to pay for what you did to me."
                wt_image chubby_lee_2_4
                "Lee pulls up [chelsea.name]'s skirt and begins slapping her ass ... *smack* ... *smack* ... *smack*"
                chelsea.c "Oww!!!"
                if dungeon.has_item(floggers):
                    wt_image chubby_lee_2_5
                    "There's no point in letting Lee hurt her hand, when you have a perfectly good paddle in your dungeon.  Lee's eyes sparkle coldly as she accepts the paddle from you and uses it on [chelsea.name] ... *SMACK* ... *SMACK* ... *SMACK*"
                    chelsea.c "OWW  OW  OWWW!!!"
                wt_image chubby_lee_2_27
                lee.c "Hurts, doesn't it whore?"
                wt_image chubby_lee_2_28
                chelsea.c "Yes!!"
                lee.c "Good, but I bet it doesn't hurt half as much as you hurt me."
                wt_image chubby_lee_2_6
                lee.c "All because you can't control your whore cunt.  Suck my fingers.  Get them sopping wet.  Not that I should worry.  Your whore cunt is probably sopping wet all the time."
                wt_image chubby_lee_2_7
                "It isn't, but surprisingly it becomes wet fairly quickly after Lee shoves her fingers inside it."
                wt_image chubby_lee_2_29
                lee.c "You fucking whore.  You'd cum all over my fingers if I let you.  Taste how wet you are!  You wanna show me how big of a whore you are?  Go on, then, show me.  Show me by cumming on my boot."
                wt_image chubby_lee_2_8
                "Lee rolls [chelsea.name] over and presses the toe of her boot against [chelsea.name]'s sex."
                lee.c "Play with yourself, whore.  Fuck yourself to orgasm against my boot like the dumb cunt whore you are."
                wt_image chubby_lee_2_9
                lee.c "Go on, I know you want to. Tramps like you will hump themselves against anything, whether it's a boot, a lamp post, or someone else's boyfriend.  I know you want to cum, whore, so go ahead."
                wt_image chubby_lee_2_10
                "[chelsea.name] doesn't actually want to cum like this, and in fact doesn't. But she does leave a suspicious amount of fluids against Lee's boot before Lee tires of this game and rolls her back onto her knees."
                wt_image chubby_lee_2_30
                lee.c "You think you're too good to cum humping my boot, tramp?  I bet you'll cum when I shove my strap-on inside you."
                wt_image chubby_lee_2_11
                "Lee puts on her toy and then pushes the tip of it into [chelsea.name] ..."
                wt_image chubby_lee_2_12
                "... then promptly pulls it out."
                lee.c "But where would the fun be in that?  This is to punish you, so if you're going to cum from my strap-on, whore ..."
                wt_image chubby_lee_2_13
                lee.c "... you'll cum from taking it up the ass."
                chelsea.c "Noo!!!"
                "[chelsea.name] tries to wriggle away ..."
                wt_image chubby_lee_2_14
                "... but Lee follows, keeping her impaled on the dildo up her ass."
                lee.c "Yes!!  Yes, you will take this ass fucking, you fucking whore!  It hurts, doesn't it?"
                chelsea.c "Yes!"
                lee.c "Not as much as you hurt me, whore. For that matter, not as much as it's going to hurt when I shove it all the way inside you ... now!"
                wt_image chubby_lee_2_15
                chelsea.c "OOWWW!!!!"
                lee.c "There, you could feel that, couldn't you, whore?"
                chelsea.c "YESSS!!!"
                if chelsea.anal_status < 2:
                    "As introductions to anal play go, this is a rough one. Much more of this treatment, and she'll take your cock up her ass without blinking an eye."
                    $ chelsea.anal_status = 2
                elif chelsea.anal_status == 6:
                    "Taking your cock up her butt is child's play compared to what Lee is putting her through."
                elif chelsea.has_item(butt_plug):
                    "The butt plug you bought [chelsea.name] has at least prepared her to take a toy up her ass, but Lee's fucking her in a brutal enough manner that it hurts like hell anyway."
                    $ chelsea.anal_status += 1
                else:
                    "If Lee keeps fucking [chelsea.name]'s' butt like this, she'll take your cock up her ass without blinking an eye."
                    $ chelsea.anal_status += 2
                wt_image chubby_lee_2_16
                "Maybe it's the satisfaction of getting revenge after all these years.  Maybe it's the feeling of the strap on between her legs.  Or maybe she just likes fucking women in the ass.  Whatever it is, Lee suddenly throws back her head and climaxes."
                lee.c "MMMMMM"
                wt_image chubby_lee_2_14
                lee.c "Time to say thank you, whore.  Show me how grateful you are for the ass fucking by licking out my sopping wet cunt."
                wt_image chubby_lee_2_17
                "Lee flips [chelsea.name] onto her back and straddles her face before [chelsea.name] can react."
                wt_image chubby_lee_2_18
                lee.c "Shit that feels good, tramp!  You're a good cunt licker, aren't you?"
                wt_image chubby_lee_2_20
                "She may not like Lee, but faced with Lee's wet pussy in her face and the prospect of more punishment if she doesn't service it, [chelsea.name] licks, sucks, and nibbles away ..."
                wt_image chubby_lee_2_19
                "... bringing her tormenter to her second orgasm of her visit, and sending her home happy."
                lee.c "MMMMMM"
                "Lee wasn't going to forget this visit anyway.  Now she definitely won't."
                $ chelsea.lee_event_status = 2
            else:
                wt_image chubby_lee_2_1
                "You put [chelsea.name] back into slutty schoolgirl clothes for a follow up session with her old classmate, Lee. It's fun to watch her expression when she sees the clothes come out, as it tells her what's coming next."
                call forced_movement(dungeon) from _call_forced_movement_247
                summon chelsea no_follows
                summon lee no_follows
                wt_image chubby_lee_2_30
                "Lee seems to find it fun, too, in a borderline psychotic way.  She investigates your dungeon before turning her attention to [chelsea.name]."
                if dungeon.has_item(floggers):
                    wt_image chubby_lee_2_31
                    "Picking up one of your canes, Lee flexes it while [chelsea.name] cringes."
                else:
                    wt_image chubby_lee_2_2
                lee.c "I'm going to hurt you bad today, whore.  Then you're going to thank me with your tongue for teaching a cheating whore like you some manners."
                if dungeon.has_item(suspension_gear):
                    wt_image chubby_lee_2_4
                    lee.c "Get down on your knees, whore, while I try these ropes out on you."
                    wt_image chubby_lee_2_21
                    "Lee strips [chelsea.name] and fastens the suspension gear to her, then hoists her into the air."
                    if chelsea.has_tag('toned') or chelsea.has_tag('motivated'):
                        lee.c "Good thing you lost that weight. I doubt I ever could've got the fat piggy girl you were in high school up in the air like this."
                    else:
                        lee.c "This equipment's pretty impressive, to get a fat cow like you up in the air like this."
                    if dungeon.has_item(floggers):
                        lee.c "Let me hear you scream, whore."
                        wt_image chubby_lee_2_22
                        "Picking up one of your floggers, Lee twirls it menacingly ... then brings it down sharply on [chelsea.name]'s exposed ass ... *THWAPPP* ... *THWAPPP* ... *THWAPPP*"
                        chelsea.c "OWW  OW  OWWW!!!"
                        wt_image chubby_lee_2_23
                        lee.c "Shit, what a pussy you are. That barely tickled you and you're squealing like a stuck pig. Which is what I'm going to make you now. Get my toy good and wet ..."
                    else:
                        wt_image chubby_lee_2_23
                        lee.c "Get my toy good and wet ..."
                    wt_image chubby_lee_2_24
                    lee.c "... just don't get your hopes up, whore. This isn't going in your slutty cunt. It's going into the one hole I know you can't get off on."
                    wt_image chubby_lee_2_25
                    "Not like that, she isn't. There's probably no way [chelsea.name]'s ever getting off on having something shoved up her ass, but definitely not the way Lee does it, jamming it in with no preparation other than the bare minimum to keep from tearing her."
                    chelsea.c "OOWWWW!!!!"
                    wt_image chubby_lee_2_21
                else:
                    wt_image chubby_lee_2_3
                    lee.c "Get down on your knees, whore, so I can smack that fat ass of yours."
                    if dungeon.has_item(floggers):
                        wt_image chubby_lee_2_28
                        lee.c "Let me hear you scream, whore."
                        wt_image chubby_lee_2_5
                        "Picking up one of your paddles, Lee brings it down sharply on [chelsea.name]'s ass ... *SMACK* ... *SMACK* ... *SMACK*"
                        chelsea.c "OWW  OW  OWWW!!!"
                    else:
                        wt_image chubby_lee_2_4
                        "Lee pulls up [chelsea.name]'s skirt and begins slapping her ass ... *smack* ... *smack* ... *smack*"
                        chelsea.c "Oww!!!"
                        $ chelsea.spank_count += 1
                    wt_image chubby_lee_2_12
                    lee.c "Shit, what a pussy you are.  That barely tickled you and you're squealing like a stuck pig.  Which is what I'm going to make you now."
                    wt_image chubby_lee_2_13
                    lee.c "Just don't get your hopes up, whore.  My strap-on isn't going in your slutty cunt.  It's going into the one hole I know you can't get off on."
                    wt_image chubby_lee_2_14
                    "Not like that, she isn't.  There's probably no way [chelsea.name]'s ever getting off on having something shoved up her ass, but definitely not the way Lee does it, jamming it in with no preparation other than the bare minimum to keep from tearing her."
                    wt_image chubby_lee_2_15
                    chelsea.c "OOWWWW!!!!"
                    wt_image chubby_lee_2_14
                lee.c "Show me how grateful you are for the ass fucking, whore. Thank me for punishing you, you cheating slut."
                wt_image chubby_lee_2_17
                "Lee positions [chelsea.name] on her back and straddles her face."
                wt_image chubby_lee_2_18
                lee.c "Shit, that feels good, tramp!  You're a good cunt licker, aren't you?"
                wt_image chubby_lee_2_20
                "She may not like Lee, but faced with Lee's wet pussy in her face, [chelsea.name] licks, sucks, and nibbles away ..."
                wt_image chubby_lee_2_19
                "... bringing her tormenter to orgasm and sending her home happy."
                lee.c "MMMMMM"
            if lee.domme_you_status == 0:
                call lee_chelsea_domme_you_question from _call_lee_chelsea_domme_you_question_1
            call character_location_return(lee) from _call_character_location_return_67
            change player energy by -energy_short notify
            call character_location_return(chelsea) from _call_character_location_return_68
        "Use her as a decoration":
            wt_image chubby_slave_9
            "Art is such a subjective matter. Not everyone would like the way you've chosen to decorate the living room, but you like it."
            "Of course, it takes a while to get [chelsea.name] tied in the proper position, and she can't physically maintain the position for too long. So this isn't your every day decor. But for special occasions and holidays, she makes a lovely centerpiece."
            rem tags 'slave_tied_now' 'slave_suspended_now' 'slave_plugged_now' 'slave_dildo_now' from chelsea
            add tags 'slave_decoration_now' to chelsea
            $ chelsea.change_image('chubby_slave_9')
    return

label chelsea_elsa_sg:
    wt_image frigid_chubby_1_168
    player.c "Follow me, [chelsea.name]."
    if current_location != bedroom:
        call forced_movement(bedroom) from _call_forced_movement_248
    summon elsa no_follows
    summon chelsea no_follows
    wt_image frigid_chubby_1_169
    "You bring her to where [elsa.name] waits."
    wt_image frigid_chubby_1_148
    call elsa_chelsea_sg_content from _call_elsa_chelsea_sg_content
    return

# Lend to Master M
label chelsea_lend_to_master_m:
  wt_image chubby_hypno_motivated_breasts
  player.c "[chelsea.full_name], get dressed. I'm sending you to another man."
  chelsea.c "Another man?  But, I belong to you, [chelsea.your_name]."
  player.c "And you are mine to do what I want with.  Today, what I want is for you to go visit Master M and let him do whatever he wants with you. Until he sends you back to me, you will obey him as you would me."
  chelsea.c "Yes, [chelsea.your_name]."
  wt_image chubby_dominate_7_1
  "It's a few hours later before she returns and undresses."
  player.c "How did it go?"
  wt_image chubby_dominate_7_15
  chelsea.c "Good, I think, [chelsea.your_name]."
  player.c "Was he pleased with you?"
  wt_image chubby_dominate_7_16
  chelsea.c "I hope so."
  $ title = "Ask for details?"
  menu:
    "Yes":
      player.c "What did he do with you?"
      wt_image chubby_mm_10
      chelsea.c "{i}When I  got there, he told me to take off my coat and top ...{/i}"
      wt_image chubby_mm_1
      chelsea.c "{i}... and kneel in front of him so he could examine my breasts.  I think he liked them.{/i}"
      wt_image chubby_mm_1
      chelsea.c "{i}Then he tied my hair back and told me to open my mouth ...{/i}"
      wt_image chubby_mm_3
      chelsea.c "{i}... and put his dick in it.{/i}"
      wt_image chubby_mm_11
      player.c "{i}What happened next?{/i}"
      wt_image chubby_mm_5
      chelsea.c "{i}Nothing, [chelsea.your_name].  At least, not for a long, long time.{/i}"
      wt_image chubby_mm_8
      chelsea.c "{i}He just kept me there, sucking his cock.{/i}"
      wt_image chubby_mm_12
      chelsea.c "{i}He kept me there so long my jaw ached and the muscles in my neck and shoulders were screaming at me.{/i}"
      wt_image chubby_mm_6
      chelsea.c "{i}Then he kept me there some more ... and some more.{/i}"
      wt_image chubby_mm_7
      chelsea.c "{i}Eventually, I tried to switch to using my tits to please him, but he would have none of it.{/i}"
      wt_image chubby_mm_8
      chelsea.c "{i}He pushed my mouth back onto his dick and told me to keep sucking. It was torture, [chelsea.your_name]. I didn't think he would ever cum. I lost all track of time. I think I may even have spaced out.{/i}"
      wt_image chubby_mm_9
      chelsea.c "{i}The next thing I remember, he was lifting me up and impaling me on his cock, shooting his load inside me as he entered me.{/i}"
      player.c "{i}Did you cum, too?{/i}"
      wt_image chubby_mm_13
      chelsea.c "{i}I might have, [chelsea.your_name], if my jaw hadn't been in such agony.  As it was, all I felt was relief as he came inside me, because I knew it meant I wouldn't have to keep sucking his dick.{/i}"
      wt_image chubby_seduce_motivated_2
      chelsea.c "I did my best to please your friend, [chelsea.your_name].  I hope he was happy with me."
      $ title = "What do you do?"
      menu:
        "Fuck her":
          player.c "Turn around, I'm going to fuck you."
          chelsea.c "Yes, [chelsea.your_name]!"
          wt_image chubby_visit_toned_3_18
          "She may have been in too much pain to enjoy Master M's cock inside her, but she's recovered since then, and responds well to the feeling of yours penetrating her rapidly wetting snatch."
          chelsea.c "Ahhhh"
          $ title = "Let her cum?"
          menu:
            "Yes":
              wt_image chubby_visit_toned_3_17
              player.c "Be a good girl and cum for my amusement, [chelsea.full_name]."
              chelsea.c "Ahhhh ... Yes, [chelsea.your_name]!"
              wt_image chubby_seduce_motivated_6
              "Maybe her time with Master M did turn her on after all.  She climaxes quickly as you fuck her, even without any stimulation of her clit."
              chelsea.c "Aahhhhhh"
              wt_image chubby_visit_toned_3_17
              "You don't take much longer, filling her with her second load of jizz for the day."
              $ chelsea.orgasm_count += 1
            "No":
              wt_image chubby_seduce_motivated_6
              player.c "No orgasm for you, [chelsea.full_name].  This is just for me."
              chelsea.c "Ahhhh ... Yes, [chelsea.your_name]."
              wt_image chubby_visit_toned_3_17
              "She digs her fingers into herself, perhaps using the pain to lower her own excitement.  You feel no such need for self-restraint, and soon fill her with her second load of jizz for the day."
          wt_image chubby_visit_toned_3_18
          player.c "[player.orgasm_text]"
          $ chelsea.sex_count += 1
          orgasm notify
        "Make her blow you":
          player.c "Kneel here beside me and pleasure my cock. I'm going to watch some TV while you blow me."
          wt_image chubby_visit_toned_3_7
          chelsea.c "Yes, [chelsea.your_name]."
          wt_image chubby_visit_toned_3_8
          "Her jaw has had some rest, but you know it must still be very sore.  Despite that, she obediently takes you into her mouth."
          wt_image chubby_visit_toned_3_33
          "She's in agony, and no matter how hard she tries not to let that show, the simple act of sucking you off after the ordeal Master M put her through may be the most intense torture you've inflicted on her.  Before long, her whole body is trembling as her muscles rebel against overuse."
          wt_image chubby_visit_toned_3_8
          "Fortunately for her, you can't hold out very long, not while watching her try to ignore the tremors in her own body and focus exclusively on pleasuring your cock, no matter how much it hurts."
          wt_image chubby_seduce_motivated_4
          player.c "[player.orgasm_text]"
          "As you release your load into her mouth, she slips into a state of deep subspace.  She's spent most of the day as a mouth for fucking, first by M, then by you, and she's rarely if ever been happier."
          $ chelsea.blowjob_count += 1
          $ chelsea.swallow_count += 1
          orgasm notify
        "Go on with your day":
          player.c "I'm sure you did fine, [chelsea.full_name].  I'll let you know when I need you for something else."
          chelsea.c "Yes, [chelsea.your_name]."
    "No, just go on with your day":
      player.c "I'm sure you did fine, [chelsea.full_name].  I'll let you know when I need you for something else."
      chelsea.c "Yes, [chelsea.your_name]."
  $ master_m.experience_with_your_slave = "I enjoyed making use of her, although there was something a bit ... off with her. I couldn't quite put my finger on it. Anyway, I enjoyed myself."
  $ master_m.name_of_your_slave_loaned = chelsea.name
  $ chelsea.training_session()
  add tags 'master_m_visit' to chelsea
  call master_m_lend from _call_master_m_lend_2
  return

########### OBJECTS ###########
## Common Objects
# Contact Former Client
label chelsea_contact:
    #$ chelsea.training_session() # this also advance visit_count by 1 in end_day label ## only added after do something with her
    # Will she accept continuing actions?
    if chelsea.has_tag('satisfied') and not chelsea.has_tag('continuing_actions') and not chelsea.has_tag('post_continuing_actions'):
        wt_image chelsea.image
        chelsea.c "Hi. I wasn't expecting to hear from you again, now that my training is finished."
        player.c "[chelsea.name], I'd like you to continue to visit me.  Without your husband's knowledge."
        # note: must be against unmodded stat, so don't use the "test" function
        if chelsea.resistance <= 0:
            "[chelsea.name] has become used to following your instructions. Even though she knows this is wrong, she can't say no."
            chelsea.c "All right.  If that's what you think is best.  I'll be right over."
            add tags 'continuing_actions' to chelsea
        else:
            chelsea.c "I don't think that would be a good idea. I love my husband, and we're happy together. Please don't contact me again."
            if chelsea.has_tag('trigger_implanted'):
                player.c "[chelsea.trigger_phrase], [chelsea.name]. Are you listening to me?"
                chelsea.c "Yes, I'm listening to you."
                player.c "You want to visit me."
                chelsea.c "No, I ..."
                player.c "[chelsea.trigger_phrase]. You want to visit me, [chelsea.name]."
                chelsea.c "Yes, I want to visit you."
                player.c "You will not remember this conversation. From now on, however, when I contact you and ask you to visit, you will do so. You will not tell your husband. You will visit me in secret, whenever I ask you to, starting now.  Do you understand?"
                chelsea.c "Yes, I understand.  I'll be right over."
                add tags 'continuing_actions' to chelsea
            else:
                rem tags 'continuing_actions' from chelsea
                $ living_room.remove_action(chelsea.current_client_action)
    # check to see if available to come over
    if chelsea.has_tag('continuing_actions'):
        $ chelsea.visit_outfit += 1
        if chelsea.visit_outfit >= 5:
            $ chelsea.visit_outfit = 1
        if chelsea.visit_outfit == 3:
            if chelsea.visit_talk_count > chelsea.visit_sex_count:
                $ chelsea.visit_outfit += 1
            else:
                if chelsea.has_tag('toned') and not chelsea.has_tag('lingerie_motivated'):
                    $ chelsea.visit_outfit += 1
                if chelsea.has_tag('bbw') and not chelsea.has_tag('lingerie_happy'):
                    $ chelsea.visit_outfit += 1
        if chelsea.visit_outfit < 4:
            summon chelsea no_follows
        else:
            add tags 'trained_this_week' to chelsea
            if chelsea.has_tag('bbw'):
                wt_image chubby_visit_bbw_4_1
            else:
                wt_image chubby_visit_toned_4_1
            "You reach [chelsea.name] at her office."
            chelsea.c "Hi, [chelsea.your_name]. Sorry, I won't be able to make it. Work is crazy right now. I'm just trying to find something to eat at the office, because I'm going to be here all night. This whole week looks shot. Maybe another time?"
            "Sounds like a visit from [chelsea.name] is out for this week. On the other hand, you could always go see her. It would take a little more energy, but you might still be able to do something with her."
            $ title = "Visit her at her office?"
            menu:
                "Yes, to hypnotize her (costs 10 extra energy)" if player.can_hypno(chelsea) and player.energy >= energy_hypnosis.value + 10:
                    #call forced_movement(outdoors)  ## moved these two commands to hypnosis_start
                    #summon chelsea no_follows
                    # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
                    $ queue_action(chelsea.hypno_action)
                "Yes (costs 10 extra energy)":
                    $ chelsea.training_session()
                    call forced_movement(outdoors) from _call_forced_movement_95
                    summon chelsea no_follows
                    change player energy by -10
                    if chelsea.has_tag('bbw'):
                        wt_image chubby_visit_bbw_4_2
                        "You surprise [chelsea.name] in her lunchroom as she just finishes eating."
                        chelsea.c "What are you doing here?"
                        player.c "Since you were too busy to come see me, I thought I'd come see you."
                        wt_image chubby_visit_bbw_4_26
                        chelsea.c "Ah, that's kind of sweet, [chelsea.your_name]. I don't have a lot of time to spare, but since you made the effort, I guess I can give you a few minutes. I don't imagine you came all the way down here to just talk with me.  So, how do you want to fuck me?"
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5 # bonus for visiting at office
                        wt_image chubby_visit_bbw_4_3
                        $ title = "What do you tell her?"
                        menu chelsea_visit_menu_4_bbw:
                            "Pleasure her":
                                player.c "Actually, I'm just here to look after you. I felt bad when I heard how busy you were, and thought I'd drop by to see if I could offer some stress relief, to help you get through your hectic day."
                                wt_image chubby_visit_bbw_4_18
                                chelsea.c "Are you serious?"
                                player.c "Very.  Wouldn't your breasts enjoy some attention?"
                                wt_image chubby_visit_bbw_4_19
                                "You cup and squeeze her tit as you kiss her neck, feeling her nipple gradually stiffen against your palm."
                                chelsea.c "Ahhhh ... I guess so."
                                player.c "What about your other body parts?  Can you think of any place else that would like attention?"
                                wt_image chubby_visit_bbw_4_20
                                chelsea.c "Um, here?"
                                "She pulls up her skirt and strokes her pussy."
                                wt_image chubby_visit_bbw_4_21
                                "Pulling her panties aside, you give her needy twat the attention it was seeking."
                                chelsea.c "Ahhhh"
                                wt_image chubby_visit_bbw_4_35
                                "It takes a little bit of effort, but eventually she cums prettily at the end of your tongue."
                                wt_image chubby_visit_bbw_4_31
                                chelsea.c "Aahhhhhh"
                                wt_image chubby_visit_bbw_4_3
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                # adjustments to normal sex - talk impacts
                                if chelsea.visit_talk_count > chelsea.visit_sex_count:
                                    pass
                                else:
                                    if chelsea.visit_sex_count > chelsea.visit_talk_count:
                                        $ chelsea.visit_sex_count -= 1
                                        $ chelsea.visit_talk_count += 1
                                    else:
                                        $ chelsea.visit_sex_count -= 1
                                $ chelsea.pleasure_her_count += 1
                                $ chelsea.orgasm_count += 1
                                change player energy by -energy_short notify
                            "Tit fuck":
                                wt_image chubby_visit_bbw_4_14
                                "Stepping forward, you squeeze her bosom as you kiss her neck, popping her boobs out of her top."
                                player.c "What I want is to fuck these sexy tits of yours."
                                chelsea.c "Ahhhh ... I think that can be arranged."
                                wt_image chubby_visit_bbw_4_15
                                "Kneeling down, she pushes her boobs together, creating a valley ..."
                                wt_image chubby_visit_bbw_4_16
                                "... one you promptly fill with your hard dick.  Back and forth you thrust as she holds her soft mounds tightly against you, until ..."
                                wt_image chubby_visit_bbw_4_36
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_bbw_4_17
                                "... you cover her tits, and even her chin, with the evidence of how much you enjoy her sexy tits."
                                wt_image chubby_visit_bbw_4_3
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.titfuck_count += 1
                                $ chelsea.facial_count += 1
                                orgasm notify
                            "Blow job":
                                wt_image chubby_visit_bbw_4_5
                                chelsea.c "You came all the way across town for a blow job from me?  I guess that's kind of flattering."
                                "She removes her top and bra ..."
                                wt_image chubby_visit_bbw_4_6
                                "... then lowers her head to take your cock in her mouth."
                                wt_image chubby_visit_bbw_4_7
                                "Dropping to her knees, she uses her tongue and hand to tease you ..."
                                wt_image chubby_visit_bbw_4_28
                                "... before the blow job proper begins.  She has a lot of work to do tonight and she attacks your cock with vigor, making this an enjoyable blowjob, but a quick one."
                                wt_image chubby_visit_bbw_4_7
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her":
                                        wt_image chubby_visit_bbw_4_8
                                        $ chelsea.swallow_count += 1
                                    "On her":
                                        wt_image chubby_visit_bbw_4_9
                                        $ chelsea.facial_count += 1
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_bbw_4_3
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.blowjob_count += 1
                                orgasm notify
                            "Throat fuck":
                                player.c "These tables have given me an idea."
                                chelsea.c "These tables?  What's so special about them?"
                                wt_image chubby_visit_bbw_4_10
                                player.c "Their height.  Climb up on one and I'll show you."
                                wt_image chubby_visit_bbw_4_11
                                "[chelsea.name] kneels on the table and smiles when you present your cock to her."
                                chelsea.c "Is this what you wanted?  For me to suck you off while I kneel up here?"
                                wt_image chubby_visit_bbw_4_29
                                player.c "Almost, but not quite.  Roll over and lie on your back."
                                wt_image chubby_visit_bbw_4_30
                                "As she settles onto her back, you expose her breasts and push your hard dick into her mouth. She needs to let her head fall backwards off the edge of the table to open her jaw enough to accept you, a position that gives you a clear pathway to the back of her throat."
                                wt_image chubby_visit_bbw_4_12
                                "She moans around your shaft and reaches down between her legs, running her fingers across her sex as you thrust in and out, probing her throat with the head of your cock."
                                chelsea.c "nnnnn"
                                wt_image chubby_visit_bbw_4_13
                                "Maybe it's the novelty of the position, maybe she's horny and needs relief from the stress of work, or maybe she just loves the feeling of your cock penetrating her throat, but she plays with herself the whole time you throat fuck her, and while you can't tell for certain, you're pretty sure she cums when you shoot your load down her gullet."
                                chelsea.c "nnnnnnnn"
                                wt_image chubby_visit_bbw_4_37
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_bbw_4_3
                                chelsea.c "Mmmmm.  Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.blowjob_count += 1
                                $ chelsea.swallow_count += 1
                                $ chelsea.orgasm_count += 1
                                orgasm notify
                            "On her back":
                                call chelsea_visit_bbw_4_missionary from _call_chelsea_visit_bbw_4_missionary
                            "Actually, I do want to talk":
                                wt_image chubby_visit_bbw_4_4
                                chelsea.c "Really?  You came all the way down here and you just want to talk to me?  Is it anything important?"
                                "She sits down, a little worried that maybe something is wrong, and maybe a little disappointed that she missed out on an office booty call based on the amount of leg and cleavage she shows "
                                $ title = "What do you want to do?"
                                menu:
                                    "Just talk":
                                        wt_image chubby_visit_bbw_4_27
                                        "You spend an enjoyable few minutes chatting with [chelsea.name], after which she needs to get back to her work.  She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                                        add tags 'talked' to chelsea
                                        change player energy by -energy_short notify
                                    "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                                        add tags 'trigger_invoked_this_visit' to chelsea
                                        call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_6
                                    "Change your mind and fuck her":
                                        call chelsea_visit_bbw_4_missionary from _call_chelsea_visit_bbw_4_missionary_1
                                    "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                                        call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_6
                                    "Ask Her to be your girlfriend":
                                        call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_6
                    else:
                        wt_image chubby_visit_toned_4_2
                        "You find [chelsea.name] working alone in her office."
                        chelsea.c "What are you doing here?"
                        player.c "Since you were too busy to come see me, I thought I'd come see you."
                        wt_image chubby_visit_toned_4_3
                        chelsea.c "Ah, that's kind of sweet, [chelsea.your_name].  I don't have a lot of time to spare, but since you made the effort, I guess I can give you a few minutes. I don't imagine you came all the way down here to just talk with me.  So, how do you want to fuck me?"
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5 # bonus for visiting her
                        $ title = "What do you tell her?"
                        menu chelsea_visit_menu_4_toned:
                            "Pleasure her":
                                player.c "Actually, I'm just here to look after you. I felt bad when I heard how busy you were, and thought I'd drop by to see if I could offer some stress relief, to help you get through your hectic day."
                                wt_image chubby_visit_toned_4_2
                                chelsea.c "Are you serious?"
                                player.c "Very.  Come here and lie down and I'll show you."
                                wt_image chubby_visit_toned_4_15
                                "Somewhat nervously, [chelsea.name] comes out from behind her desk."
                                wt_image chubby_visit_toned_4_28
                                "As she lies down, you lift her hips until her feet fall back over her head.  Then you lower your mouth and lick and suckle her sex as she moans."
                                chelsea.c "Ahhhh"
                                wt_image chubby_visit_toned_4_29
                                "You tease and explore her labia until the juices flow freely from her.  Then you enjoy a few minutes lapping up her secretions as she moans.  After that, a few hard flicks against her clit and she cums prettily at the end of your tongue."
                                chelsea.c "Ahhhh  ...  Ahhhh  ...  Aahhhhhh"
                                wt_image chubby_visit_toned_4_30
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                # adjustments to normal sex - talk impacts
                                if chelsea.visit_talk_count > chelsea.visit_sex_count:
                                    pass
                                else:
                                    if chelsea.visit_sex_count > chelsea.visit_talk_count:
                                        $ chelsea.visit_sex_count -= 1
                                        $ chelsea.visit_talk_count += 1
                                    else:
                                        $ chelsea.visit_sex_count -= 1
                                $ chelsea.pleasure_her_count += 1
                                $ chelsea.orgasm_count += 1
                                change player energy by -energy_short notify
                            "Tit fuck":
                                wt_image chubby_visit_toned_4_2
                                player.c "I want to fuck those sexy tits of yours."
                                wt_image chubby_visit_toned_4_4
                                chelsea.c "I guess that could be arranged."
                                wt_image chubby_visit_toned_4_11
                                "She lies down, letting you put your cock between her boobs."
                                wt_image chubby_visit_toned_4_12
                                "Pressing her soft flesh around your cock, she creates a warm valley for you to slide your cock back and forth ..."
                                wt_image chubby_visit_toned_4_13
                                "... her tongue flicking and licking at the head on your cock on every forward stroke ..."
                                wt_image chubby_visit_toned_4_14
                                "... until she slides down onto the floor, her tongue still flicking against the head of your cock as you cover her breasts with jizz."
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_toned_4_30
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.titfuck_count += 1
                                orgasm notify
                            "Blow job":
                                wt_image chubby_visit_toned_4_4
                                chelsea.c "You came all the way across town for a blow job from me?  I guess that's kind of flattering."
                                wt_image chubby_visit_toned_4_5
                                "She sits in front of you and takes out your dick."
                                wt_image chubby_visit_toned_4_6
                                "She licks you playfully ..."
                                wt_image chubby_visit_toned_4_7
                                "... until, wanting more than a teasing, you pull her head onto your cock."
                                wt_image chubby_visit_toned_4_8
                                "Your hand on her head, she blows you properly, using her lips, tongue, and hand to pleasure you from the head of your cock to the base of balls."
                                wt_image chubby_visit_toned_4_9
                                "You're not the only one enjoying the blow job.  [chelsea.name] reaches down between her legs and rubs herself while she's sucking on you ..."
                                wt_image chubby_visit_toned_4_10
                                "... frigging herself to orgasm as you fill her mouth with your seed."
                                chelsea.c "nnnnnnnn"
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_toned_4_30
                                chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.blowjob_count += 1
                                $ chelsea.swallow_count += 1
                                $ chelsea.orgasm_count += 1
                                $ chelsea.masturbation_count += 1
                                orgasm notify
                            "Pile driver":
                                call chelsea_visit_toned_4_pile_driver from _call_chelsea_visit_toned_4_pile_driver
                            "Doggy style":
                                wt_image chubby_visit_toned_4_2
                                player.c "I want you on your hands and knees."
                                wt_image chubby_visit_toned_4_4
                                chelsea.c "Okay"
                                wt_image chubby_visit_toned_4_20
                                "She kneels down, presenting herself to you.  You position yourself behind her, teasing the head of your cock against her rapidly wetting opening ..."
                                wt_image chubby_visit_toned_4_21
                                "... and then pushing yourself forward, impaling her on your cock as you start to fuck her."
                                chelsea.c "Ahhhh"
                                wt_image chubby_visit_toned_4_32
                                "In-and-out you thrust, back and forth, faster and faster, ploughing her wet sex. She's enjoying this, but you're enjoying this more, and you're ready to cum."
                                $ title = "What do you do?"
                                menu:
                                    "Let yourself cum":
                                        wt_image chubby_visit_toned_4_22
                                        "You pull out and release your load, splattering her sex with your jizz. She looks back, happy that her newly fit body was able to please you so much. If she's disappointed that she didn't cum, too, she tries not to let it show."
                                        wt_image chubby_visit_toned_4_31
                                        player.c "[player.orgasm_text]"
                                        wt_image chubby_visit_toned_4_30
                                        chelsea.c "I hope you enjoyed your visit.  I need to get back to work, now."
                                    "Help her finish first":
                                        wt_image chubby_visit_toned_4_33
                                        "Reaching underneath her, you flick your fingers across her sex and clit ..."
                                        wt_image chubby_visit_toned_4_34
                                        "... while you pinch and twist her nipple with the fingers of your other hand."
                                        chelsea.c "Ahhhhh"
                                        wt_image chubby_visit_toned_4_35
                                        "Her orgasm builds quickly and as she shudders to climax you finally let yourself go, flooding her insides with your seed."
                                        wt_image chubby_visit_toned_4_23
                                        chelsea.c "Aahhhhhh"
                                        wt_image chubby_visit_toned_4_36
                                        player.c "[player.orgasm_text]"
                                        $ chelsea.orgasm_count += 1
                                        wt_image chubby_visit_toned_4_30
                                        chelsea.c "Thanks for the fun break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.sex_count += 1
                                orgasm notify
                            "Cowgirl":
                                wt_image chubby_visit_toned_4_2
                                player.c "You've been cooped up in the office all day, I bet you haven't had a chance to get a proper workout in."
                                chelsea.c "And are you going to give me a proper workout?"
                                wt_image chubby_visit_toned_4_4
                                player.c "I've got a personal exercise pole for you to ride that'll burn off calories and stress.  Come try it out."
                                wt_image chubby_visit_toned_4_37
                                chelsea.c "Mmmm, going to the gym in the morning would be so much more fun if they installed these exercise devices."
                                wt_image chubby_visit_toned_4_24
                                "She lowers herself onto you as you guide your hardness inside her."
                                wt_image chubby_visit_toned_4_25
                                chelsea.c "Ahhhh"
                                wt_image chubby_visit_toned_4_38
                                "Once she's fully impaled on your 'personal exercise pole' she starts working it, up and down, getting a good workout for her legs and core muscles."
                                wt_image chubby_visit_toned_4_39
                                "You want her to enjoy her workout and you want to encourage her to put her all into it, so you run your fingers across her pussy and clit as she rides you."
                                wt_image chubby_visit_toned_4_26
                                "The faster she bounces up and down on you, the more attention your fingers give her throbbing button ..."
                                wt_image chubby_visit_toned_4_40
                                "... until she earns the reward for her workout, and rewards your pole at the same time."
                                wt_image chubby_visit_toned_4_41
                                chelsea.c "Aahhhhhh"
                                wt_image chubby_visit_toned_4_27
                                player.c "[player.orgasm_text]"
                                wt_image chubby_visit_toned_4_30
                                chelsea.c "Thanks for fun exercise break!  I need to get back to work, now."
                                "You leave her and get on with your day."
                                $ chelsea.sex_count += 1
                                $ chelsea.orgasm_count += 1
                                orgasm notify
                            "Actually, I do just want to talk":
                                wt_image chubby_visit_toned_4_2
                                chelsea.c "Really?  You came all the way down here and you just want to talk to me?  Is it anything important?"
                                "She sits down, a little worried that maybe something is wrong, and maybe a little disappointed that you aren't here for an office booty call."
                                $ title = "What do you want to do?"
                                menu:
                                    "Just talk":
                                        wt_image chubby_visit_toned_4_3
                                        "You spend an enjoyable few minutes chatting with [chelsea.name], after which she needs to get back to her work.  She may be disappointed that she wasn't able to seduce you into fucking her, but she appreciated you wanting to get to know her better."
                                        add tags 'talked' to chelsea
                                        change player energy by -energy_short notify
                                    "Change your mind and fuck her":
                                        call chelsea_visit_toned_4_pile_driver from _call_chelsea_visit_toned_4_pile_driver_1
                                    "Invoke her hypno trigger to make her your girlfriend" if chelsea.has_tag('trigger_implanted') and not chelsea.has_tag('trigger_invoked'):
                                        add tags 'trigger_invoked_this_visit' to chelsea
                                        call chelsea_hypno_trigger from _call_chelsea_hypno_trigger_7
                                    "Offer her a gift" if not chelsea.has_item(jewelry_chelsea):
                                        wt_image chubby_visit_toned_4_2
                                        call chelsea_contact_former_client_gift from _call_chelsea_contact_former_client_gift_7
                                    "Ask her to be your girlfriend":
                                        wt_image chubby_visit_toned_4_2
                                        call chelsea_contact_former_client_ask_girlfriend from _call_chelsea_contact_former_client_ask_girlfriend_7
                    if chelsea.has_tag('talked'):
                        rem tags 'talked' from chelsea
                        $ chelsea.visit_talk_count += 1
                    else:
                        $ chelsea.visit_sex_count += 1
                    if chelsea.has_tag('trigger_invoked_this_visit'):
                        rem tags 'trigger_invoked_this_visit' from chelsea
                    call forced_movement(living_room) from _call_forced_movement_96
                    if not chelsea.has_tag('girlfriend') and not chelsea.has_tag('hypno_girlfriend'):
                        call chelsea_continuing_actions_end_of_visit from _call_chelsea_continuing_actions_end_of_visit_3
                    call character_location_return(chelsea) from _call_character_location_return_69
                "No, wait for next week":
                    pass
    wt_image current_location.image
    return

# Continuing actions end of visit calculation
label chelsea_continuing_actions_end_of_visit:
    if chelsea.has_tag('love_potion_used'):
        $ chelsea.relationship_counter += 2
    if chelsea.visit_talk_count > chelsea.visit_sex_count:
        $ chelsea.temporary_count = chelsea.visit_sex_count*2
        if chelsea.visit_talk_count > chelsea.temporary_count:
            pass
        else:
            $ chelsea.relationship_counter += 1
    else:
        $ chelsea.temporary_count = chelsea.visit_talk_count*2
        if chelsea.visit_sex_count > chelsea.temporary_count:
            pass
        else:
            $ chelsea.relationship_counter += 1
    if player.has_tag('dominant') and chelsea.spanked > 1:
        $ chelsea.relationship_counter += 0.5
    if player.has_tag('supersexy'):
        $ chelsea.relationship_counter += 0.5
    if chelsea.has_item(jewelry_chelsea):
        $ chelsea.relationship_counter += 1
    call character_location_return(chelsea) from _call_character_location_return_70
    wt_image current_location.image
    return

# Ask Former Client To Become Girlfriend
label chelsea_contact_former_client_ask_girlfriend:
  player.c "[chelsea.name], I want more from our relationship.  This is fun, but I'd like you to be my girlfriend and move in with me."
  if chelsea.relationship_counter >= 9:
    if chelsea.visit_talk_count > chelsea.visit_sex_count:
      $ chelsea.temporary_count = chelsea.visit_sex_count*2
      if chelsea.visit_talk_count > chelsea.temporary_count:
        chelsea.c "Hey, I admit it, I like you, [chelsea.your_name]. You've really grown on me."
        chelsea.c "But I didn't think you saw me that way.  You've almost become my best friend, which is great. My husband's still turned on by me, though, and we have great sex together. As much as I like you, I couldn't give that up."
        chelsea.c "I hope I didn't hurt your feelings.  How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
      else:
        chelsea.c "Really?  Do you really feel that way about me?"
        chelsea.c "I admit it, I like you, [chelsea.your_name].  You've really grown on me.  I wasn't sure if you felt the same."
        chelsea.c "It's been weird, getting to know you and having these feelings for you, knowing what you do for a living. I can't even guess how many sex partners you've had."
        chelsea.c "Don't say anything. I get who you are. I love sex, too, and I'm not going to freak out when I find some other woman in our bed. It's just been weird to get my head around why I'd even think about being with someone who isn't going to see me as his everything, when I have a man at home who loves me and who as far as I know has always been faithful to me."
        chelsea.c "That I could even be having these thoughts tells me there's something wrong with my marriage. Somehow I'm getting something I need or want or whatever coming here to be with you that I'm not getting at home."
        chelsea.c "I'm probably the dumbest girl ever, but okay, yes. I'll be your girlfriend. I think I need to try this out, even if it costs me my marriage. I'll talk to my husband and let him know I need a break to sort things out.  I'll keep your name out of it.  He doesn't need to know how I'm sorting things out."
        chelsea.c "Who knows, maybe some time away from him will make me appreciate him more. Don't take me for granted, okay, boyfriend? I'll give this an honest shot to try and make a relationship work with you, but I need you to do the same."
        "She gives you a kiss on the cheek, then leaves to have a chat with her husband."
        call chelsea_convert_girlfriend from _call_chelsea_convert_girlfriend
    else:
      if chelsea.visit_sex_count > chelsea.visit_talk_count:
        $ chelsea.temporary_count = chelsea.visit_talk_count*2
        if chelsea.visit_sex_count > chelsea.temporary_count:
          chelsea.c "Hey, I admit it, I like you, [chelsea.your_name]. You've really grown on me."
          chelsea.c "But this is all about sex, right? I mean we hardly know each other.  We pretty much just fuck every time we get together. I love the sex with you, it's great. It's pretty good with my husband, too, though, and he's more than just a fuck buddy for me, he's my partner.  As much as I like you, I couldn't give that up."
          chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
        else:
          chelsea.c "Really?  Do you really feel that way about me?"
          chelsea.c "I admit it, I like you, [chelsea.your_name]. You've really grown on me. I wasn't sure if you felt the same."
          chelsea.c "It's been weird, getting to know you and having these feelings for you, knowing what you do for a living. I can't even guess how many sex partners you've had."
          chelsea.c "Don't say anything. I get who you are. I love sex, too, and I'm not going to freak out when I find some other woman in our bed. It's just been weird to get my head around why I'd even think about being with someone who isn't going to see me as his everything, when I have a man at home who loves me and who as far as I know has always been faithful to me."
          chelsea.c "That I could even be having these thoughts tells me there's something wrong with my marriage. Somehow I'm getting something I need or want or whatever coming here to be with you that I'm not getting at home."
          chelsea.c "I'm probably the dumbest girl ever, but okay, yes. I'll be your girlfriend. I think I need to try this out, even if it costs me my marriage. I'll talk to my husband and let him know I need a break to sort things out.  I'll keep your name out of it.  He doesn't need to know how I'm sorting things out."
          chelsea.c "Who knows, maybe some time away from him will make me appreciate him more. Don't take me for granted, okay, boyfriend? I'll give this an honest shot to try and make a relationship work with you, but I need you to do the same."
          "She gives you a kiss on the cheek, then leaves to have a chat with her husband."
          call chelsea_convert_girlfriend from _call_chelsea_convert_girlfriend_1
      else:
        chelsea.c "Really?  Do you really feel that way about me?"
        chelsea.c "I admit it, I like you, [chelsea.your_name]. You've really grown on me. I wasn't sure if you felt the same."
        chelsea.c "It's been weird, getting to know you and having these feelings for you, knowing what you do for a living. I can't even guess how many sex partners you've had."
        chelsea.c "Don't say anything. I get who you are. I love sex, too, and I'm not going to freak out when I find some other woman in our bed. It's just been weird to get my head around why I'd even think about being with someone who isn't going to see me as his everything, when I have a man at home who loves me and who as far as I know has always been faithful to me."
        chelsea.c "That I could even be having these thoughts tells me there's something wrong with my marriage. Somehow I'm getting something I need or want or whatever coming here to be with you that I'm not getting at home."
        chelsea.c "I'm probably the dumbest girl ever, but okay, yes. I'll be your girlfriend. I think I need to try this out, even if it costs me my marriage. I'll talk to my husband and let him know I need a break to sort things out.  I'll keep your name out of it.  He doesn't need to know how I'm sorting things out."
        chelsea.c "Who knows, maybe some time away from him will make me appreciate him more. Don't take me for granted, okay, boyfriend? I'll give this an honest shot to try and make a relationship work with you, but I need you to do the same."
        "She gives you a kiss on the cheek, then leaves to have a chat with her husband."
        call chelsea_convert_girlfriend from _call_chelsea_convert_girlfriend_2
  else:
    if chelsea.relationship_counter >= 6:
      if chelsea.visit_talk_count > chelsea.visit_sex_count:
        $ chelsea.temporary_count = chelsea.visit_sex_count*2
        if chelsea.visit_talk_count > chelsea.temporary_count:
          chelsea.c "Hey, I admit it, you're starting to grow on me, [chelsea.your_name]. I won't lie to you, I've been thinking about our relationship a lot.  But I have a husband. Let's try not to forget that, okay?"
          chelsea.c "Anyway, I didn't think you saw me that way. Usually you only want to talk when I come over. You've become a good friend, which is great, but I don't think we're really in boyfriend-girlfriend territory here."
          chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here?  Something other than talk about boyfriend-girlfriend foolishness."
        else:
          chelsea.c "Hey, I admit it, you're starting to grow on me, [chelsea.your_name]. I won't lie to you, I've been thinking about our relationship a lot. But I have a husband. Let's try not to forget that, okay?"
          chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
      else:
        if chelsea.visit_sex_count > chelsea.visit_talk_count:
          $ chelsea.temporary_count = chelsea.visit_talk_count*2
          if chelsea.visit_sex_count > chelsea.temporary_count:
            chelsea.c "Hey, I admit it, you're starting to grow on me, [chelsea.your_name]. I won't lie to you, I've been thinking about our relationship a lot. But I have a husband. Let's try not to forget that, okay?"
            chelsea.c "Anyway, this is just about sex, right? I think that's a safe ground for us.  e get together, fool around and have a bit of fun, then go back to our real lives."
            chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
          else:
            chelsea.c "Hey, I admit it, you're starting to grow on me, [chelsea.your_name]. I won't lie to you, I've been thinking about our relationship a lot. But I have a husband. Let's try not to forget that, okay?"
            chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
        else:
          chelsea.c "Hey, I admit it, you're starting to grow on me, [chelsea.your_name].  I won't lie to you, I've been thinking about our relationship a lot.  But I have a husband.  Let's try not to forget that, okay?"
          chelsea.c "I hope I didn't hurt your feelings.  How about we do something together while we're here?  Something other than talk about boyfriend-girlfriend foolishness."
    else:
      if chelsea.relationship_counter >= 3:
        if chelsea.visit_talk_count > chelsea.visit_sex_count:
          $ chelsea.temporary_count = chelsea.visit_sex_count*2
          if chelsea.visit_talk_count > chelsea.temporary_count:
            chelsea.c "Shit, why'd you have to go and say something like that, [chelsea.your_name]? I'm already feeling guilty about the amount of time I've been spending with you. I'm a married woman.  Don't make me feel any worse about what we're doing than I already am."
            chelsea.c "Anyway, I didn't think you saw me that way. Usually you only want to talk when I come over. You've become a friend, which is great, but I don't think we're really in boyfriend-girlfriend territory here."
            chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
          else:
            chelsea.c "Shit, why'd you have to go and say something like that, [chelsea.your_name]? I'm already feeling guilty about the amount of time I've been spending with you. I'm a married woman.  Don't make me feel any worse about what we're doing than I already am."
            chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
        else:
          if chelsea.visit_sex_count > chelsea.visit_talk_count:
            $ chelsea.temporary_count = chelsea.visit_talk_count*2
            if chelsea.visit_sex_count > chelsea.temporary_count:
              chelsea.c "Shit, why'd you have to go and say something like that, [chelsea.your_name]? I'm already feeling guilty about the amount of time I've been spending with you. I'm a married woman.  Don't make me feel any worse about what we're doing than I already am."
              chelsea.c "Anyway, this is just about sex, right? I think that's a safe ground for us. We get together, fool around and have a bit of fun, then go back to our real lives."
              chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
            else:
              chelsea.c "Shit, why'd you have to go and say something like that, [chelsea.your_name]? I'm already feeling guilty about the amount of time I've been spending with you. I'm a married woman.  Don't make me feel any worse about what we're doing than I already am."
              chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
          else:
            chelsea.c "Shit, why'd you have to go and say something like that, [chelsea.your_name]? I'm already feeling guilty about the amount of time I've been spending with you. I'm a married woman.  Don't make me feel any worse about what we're doing than I already am."
            chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
      else:
        if chelsea.relationship_counter >= 1:
          if chelsea.visit_talk_count > chelsea.visit_sex_count:
            $ chelsea.temporary_count = chelsea.visit_sex_count*2
            if chelsea.visit_talk_count > chelsea.temporary_count:
              chelsea.c "What? Where did that come from? I appreciate the attention you give me, [chelsea.your_name], but I'm a happily married woman."
              chelsea.c "Anyway, I didn't think you saw me that way. I thought you were trying to become my friend, which is great, but I don't think we're really in boyfriend-girlfriend territory here."
              chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
            else:
              chelsea.c "What? Where did that come from? I appreciate the attention you give me, [chelsea.your_name], but I'm a happily married woman."
              chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
          else:
            if chelsea.visit_sex_count > chelsea.visit_talk_count:
              $ chelsea.temporary_count = chelsea.visit_talk_count*2
              if chelsea.visit_sex_count > chelsea.temporary_count:
                chelsea.c "What?  Where did that come from? I appreciate the attention you give me, [chelsea.your_name], but I'm a happily married woman."
                chelsea.c "Anyway, this is just about sex, right? I think that's a safe ground for us. We get together, fool around and have a bit of fun, then go back to our real lives."
                chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
              else:
                chelsea.c "What?  Where did that come from? I appreciate the attention you give me, [chelsea.your_name], but I'm a happily married woman."
                chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
            else:
              chelsea.c "What? Where did that come from? I appreciate the attention you give me, [chelsea.your_name], but I'm a happily married woman."
              chelsea.c "I hope I didn't hurt your feelings. How about we do something together while we're here? Something other than talk about boyfriend-girlfriend foolishness."
        else:
          "She laughs."
          chelsea.c "Are you trying to become a comedian, [chelsea.your_name]?  We don't have a relationship."
          chelsea.c "How about we do something together while we're here?  Something other than talk about boyfriend-girlfriend foolishness."
  if not chelsea.has_tag('girlfriend'):
    $ title = "What do you tell her?"
    if chelsea.has_tag('toned'):
      jump expression "chelsea_visit_menu_" + str(chelsea.visit_outfit) + "_toned"
    elif chelsea.has_tag('bbw'):
      jump expression "chelsea_visit_menu_" + str(chelsea.visit_outfit) + "_bbw"
  return

# Give Gift to Former Client
label chelsea_contact_former_client_gift:
  if chelsea.has_item(lingerie):
    if player.has(jewelry_chelsea):
      player.c "I bought something for you."
      chelsea.c "Oh yeah?  What is it?  Did you get me more lingerie?"
      player.c "No.  Something else.  I hope you like it."
      "You pass over the neatly wrapped box with the necklace in it."
      chelsea.c "What is this?  Is this ... did you buy me jewelry??"
      "[chelsea.name] hesitates, as if trying to decide if she should open it."
      wt_image chubby_jewelry_1
      "Eventually, her curiosity gets the better of her, and she unwraps the gift and picks up the necklace."
      chelsea.c "Oh!  Wow!!  Oh, this is beautiful.  I ... I'm not sure what to say?"
      player.c "Thank you would be nice."
      wt_image chubby_kiss_1
      "She leans over and kisses you warmly."
      chelsea.c "Thank you. I love it. But I'm sure you don't want to just talk about how much I liked it. How about I show you instead?"
      give 1 jewelry_chelsea from player to chelsea notify
    else:
      "If you want her to think of you as a potential boyfriend, you should give her something a boyfriend might give his girl to tell her he's serious about her. You don't have anything suitable to give her right now."
  else:
    if player.has(lingerie):
      "[chelsea.name] would likely be flattered to receive lingerie from you."
      $ title = "Gift her the lingerie?"
      menu:
        "Yes":
          chelsea.c "Oh wow!  this is really nice.  I might have to try this on with you sometime.  Thank you!"
          "She leans over and gives you a peck on the cheek."
          chelsea.c "So, what did you want to do today?  I don't imagine you called me over here just to talk about what a nice guy you are for giving me a sweet gift."
          sys "[chelsea.name] is happier with your relationship."
          $ chelsea.relationship_counter += 1
          if chelsea.has_tag('toned'):
            add tags 'lingerie_motivated' to chelsea
          elif chelsea.has_tag('bbw'):
            add tags 'lingerie_happy' to chelsea
          give 1 lingerie from player to chelsea notify
        "No":
          pass
    else:
      "[chelsea.name] might like some clothing to show off her new-found confidence in her body.  Unfortunately, you have nothing suitable to give her right now."
  $ title = "What do you tell her?"
  if chelsea.has_tag('toned'):
    jump expression "chelsea_visit_menu_" + str(chelsea.visit_outfit) + "_toned"
  elif chelsea.has_tag('bbw'):
    jump expression "chelsea_visit_menu_" + str(chelsea.visit_outfit) + "_bbw"
  return

# View Relationship Status
label chelsea_relationship_status:
    call chelsea_description_display from _call_chelsea_description_display_1
    wt_image current_location.image
    return

# Review Files
label chelsea_review_files:
    call chelsea_description_display from _call_chelsea_description_display_2
    wt_image current_location.image
    return

## Character Specific Objects
# Watch Chelsea Fuck In Club
# OBJECT: Watch Your Girlfriend
label chelsea_watch:
  $ chelsea.club_outfit += 1
  if not chelsea.can_be_interacted and not chelsea.has_tag('club_date_night'):
    "[chelsea.name] is not available today."
    $ chelsea.club_outfit -= 1
  elif chelsea.club_outfit == 3 or chelsea.club_outfit > 5:
    rem tags 'club_date_night' from chelsea
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    summon chelsea no_follows
    wt_image chubby_club_1_1
    "Brooklyn and her husband aren't around today, but [chelsea.name] seems comfortable mingling with the crowd."
    $ title = "What do you so?"
    menu:
      "Watch her":
        wt_image chubby_club_1_2
        "With her attributes, you're not surprised that she soon attracts a crowd."
        if chelsea.club_outfit == 3:
          wt_image chubby_club_1_3
          "The other women step back and watch with you as [chelsea.name] becomes the center of attention ..."
          wt_image chubby_club_1_4
          if chelsea.glory_hole_count > 1:
            "... showing off the skills she learned at the glory-hole ..."
          else:
            "... showing off her multi-tasking skills ..."
          wt_image chubby_club_1_5
          "... and considerable stamina ..."
          wt_image chubby_club_1_6
          "... not to mention a willingness to get sticky."
          $ title = "Add your own load?"
          menu:
            "Yes, jerk off on her":
              wt_image chubby_club_1_7
              "[chelsea.name] is surprised, but not at all disappointed when you join in."
              player.c "[player.orgasm_text]"
              wt_image chubby_club_1_10
              orgasm
            "Not today":
              wt_image chubby_club_1_11
              change player energy by -energy_very_short
          chelsea.c "Mmmmm, that was a lot of fun!"
          notify
        else:
          wt_image chubby_club_1_8
          "Before long, [chelsea.name] finds herself bent over with a cock in her mouth ..."
          wt_image chubby_club_1_9
          "... and another entering her from behind."
          wt_image chubby_club_1_12
          "The cocks change ..."
          wt_image chubby_club_1_13
          "... but the double-teaming remains."
          $ title = "Take your turn?"
          menu:
            "Yes, fuck her":
              wt_image chubby_club_1_14
              "It'd be nice to think that [chelsea.name] would recognize your cock as you enter her ..."
              wt_image chubby_club_1_15
              "... but then your girlfriends have always found it strangely difficult to get a firm sense of the size and shape of your cock.  And in any event, [chelsea.name] is too preoccupied with the cock stretching open her mouth ..."
              wt_image chubby_club_1_16
              "... to pay as much attention as she otherwise would to who's cumming inside her other end."
              player.c "[player.orgasm_text]"
              $ chelsea.sex_count += 1
              orgasm
            "Not today":
              change player energy by -energy_very_short
          wt_image chubby_club_1_17
          "Eventually some of the men decide they want to see [chelsea.name] cum, so turn her over ..."
          wt_image chubby_club_1_18
          "... and watch her do just that."
          chelsea.c "Aahhhhhh"
          wt_image chubby_club_1_19
          "Once she recovers, a couple of the men help the shaky-legged [chelsea.name] to her feet."
          chelsea.c "Oh, hey [chelsea.your_name].  I'm having fun, how about you?"
          notify
      "Find something else to do":
        pass
    if chelsea.club_outfit > 5:
      $ chelsea.club_outfit = 0
    call character_location_return(chelsea) from _call_character_location_return_71
    wt_image swingers_room.image
  else:
    rem tags 'club_date_night' from chelsea
    $ chelsea.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    summon chelsea no_follows
    summon brooklyn no_follows
    if chelsea.lesbian_club_count == 4:
      wt_image chubby_swinging_1
      "[chelsea.name] spots her favorite couple and starts to head over..."
      wt_image chubby_swinging_26
      "... when Brooklyn stops her."
      wt_image chubby_swinging_57
      brooklyn.c "He doesn't get to play, today.  I want you all to myself.  Is that okay?"
      wt_image chubby_swinging_58
      chelsea.c "Yes"
      wt_image chubby_swinging_27
      "Her husband is relegated to watching as Brooklyn and [chelsea.name] make out."
      $ title = "What now?"
      menu menu_chelsea_swinging_bisexual_menu:
        "Ask him to suck your cock":
          add tags 'bi_bj' to brooklyn
          wt_image chubby_swinging_59
          brooklyn.c "Is your guy allowed to have his cock sucked?"
          chelsea.c "Sure"
          wt_image chubby_swinging_60
          brooklyn.c "Suck him off, honey.  Do a good job and he may cum in time for you to see what I'm doing with his girlfriend."
          wt_image chubby_swinging_28
          "With the man's lips around your dick, you settle in to watch his woman and your girlfriend finish undressing each other."
          wt_image chubby_swinging_29
          "[chelsea.name] seems fascinated by the sight of a man sucking your cock ..."
          wt_image chubby_swinging_30
          "... until Brooklyn distracts her with something she finds even more interesting."
          wt_image chubby_swinging_31
          chelsea.c "Aahhhhhh"
          wt_image chubby_swinging_61
          "Just as Brooklyn is making [chelsea.name] cum, her husband is doing the same for you."
          player.c "[player.orgasm_text]"
          wt_image chubby_swinging_33
          brooklyn.c "Your guy just filled my guy's mouth full of cum."
          chelsea.c "I know.  That was hot!"
          $ club_swingers.blowjob_count += 1
          $ club_swingers.swallow_count += 1
          orgasm notify
        "Offer to suck his cock" if not brooklyn.has_tag('no_bi_bj'):
          add tags 'no_bi_bj' to brooklyn
          wt_image chubby_swinging_14
          brooklyn.c "Sorry, he's only allowed to watch today.  No stimulation for his cock until later - if he's good.  He'll suck your cock for you, though, if you want.  If that's okay with your girlfriend?"
          jump menu_chelsea_swinging_bisexual_menu
        "Just watch the two women":
          wt_image chubby_swinging_28
          "You and the other man settle in to watch your women undress each other."
          wt_image chubby_swinging_62
          "Brooklyn seems as interested in the reaction she's getting from you and her husband as she is in the reaction she's getting from [chelsea.name] ..."
          wt_image chubby_swinging_30
          "... which is a pretty strong reaction ..."
          wt_image chubby_swinging_31
          "... especially when she stops playing to the audience and focuses on the task - and pussy - at hand."
          chelsea.c "Aahhhhhh"
          wt_image chubby_swinging_32
          "[chelsea.name] seems sated, and Brooklyn seems pleased with herself."
          $ title = "What do you do?"
          menu:
            "Approach them":
              wt_image chubby_swinging_33
              "[chelsea.name] smiles and whispers to the other woman as she sees you approach."
              chelsea.c "I know your husband isn't allowed to cum in the Club, but my man isn't under that restriction, and I think watching us has him worked up.  Would you like to help me give him some relief?"
              wt_image chubby_swinging_37
              brooklyn.c "Sure"
              "[chelsea.name]'s pussy juice still glistening on her chin, the woman joins [chelsea.name] in pleasuring your cock."
              wt_image chubby_swinging_34
              "Any former jealousy you had for her husband fades away as you receive the ladies' undivided attention. And unlike him, you'll get to enjoy the fruits of their labor."
              wt_image chubby_swinging_35
              "Or so you think.  The woman pulls away and whispers to [chelsea.name]."
              brooklyn.c "Are you sure you want to let him cum?  He'll be so much more fun and receptive to you if you send him home like this and make him earn an orgasm from you later."
              "[chelsea.name] looks up at you, searching your face."
              $ title = "What does your face show her?"
              menu:
                "You hate the idea":
                  "[chelsea.name] can tell you're not impressed by the idea."
                  chelsea.c "That's not how our relationship works. Let's get him off."
                  brooklyn.c "Suit yourself."
                  wt_image chubby_swinging_36
                  "Whether or not it suits [chelsea.name], it certainly suits you.  Under the attention of the ladies' tongues and lips, you soon get your relief.  Brooklyn looks over at her husband, enjoying the jealous look on his face as you get to cum, when he didn't."
                  player.c "[player.orgasm_text]"
                  $ chelsea.blowjob_count += 1
                  $ chelsea.facial_count += 1
                  orgasm notify
                "You hate it but it turns you on":
                  wt_image chubby_swinging_37
                  "You don't exactly enjoy being blue balled, but the idea of [chelsea.name] denying you an orgasm turns you on, and it shows."
                  chelsea.c "That's a great idea."
                  wt_image chubby_swinging_39
                  chelsea.c "Put it back in your pants.  Maybe I'll take pity on you later and let you cum - if you're good that is and treat me right."
                  sys "Note: If you're hoping [chelsea.name] will take charge in your relationship, sorry. Blue balling you is as far as [chelsea.name] will go in domming you."
                "You're wondering what [chelsea.name] thinks":
                  "[chelsea.name] thinks for a minute before responding."
                  $ chelsea.relationship_counter += 1
                  if chelsea.relationship_counter >= 4:
                    chelsea.c "I'm feeling really good about our relationship. I don't want anything to change. I think he deserves a reward right now for being such an attentive boyfriend."
                    wt_image chubby_swinging_36
                    "With their tongues and lips, the ladies provide you with your reward, and you provide them with theirs.  Brooklyn looks over at her husband, enjoying the jealous look on his face as you get to cum, when he didn't."
                    player.c "[player.orgasm_text]"
                    $ chelsea.blowjob_count += 1
                    $ chelsea.facial_count += 1
                    orgasm notify
                  else:
                    wt_image chubby_swinging_37
                    chelsea.c "I have been feeling a little uncertain about our relationship, and would definitely like it if he gave me some more attention.  Maybe I should try your technique?"
                    wt_image chubby_swinging_39
                    chelsea.c "That's all for now.  If you want relief, come spend some time with me later, at home, just the two of us, and maybe afterwards we can finish this."
            "Leave them to cuddle":
              wt_image chubby_swinging_12
              "You leave [chelsea.name] alone with her friend to bask in the glow of her expanded sexuality."
        "Find something else to do":
          add tags 'did_not_watch' to brooklyn
    elif chelsea.has_tag('likes_girls') and chelsea.lesbian_club_count == 0:
      wt_image chubby_swinging_1
      "You expected [chelsea.name] might be a bit nervous entering the swingers room, but she isn't.  She spots an attractive couple sitting by themselves on a sofa, and heads right over."
      wt_image chubby_swinging_2
      chelsea.c "Do you mind if I join you?"
      wt_image chubby_swinging_10
      "The woman provides her answer in the form of a kiss."
      wt_image chubby_swinging_11
      "Not to leave the man feeling left out, [chelsea.name] kisses him, too, while his wife feels her up."
      wt_image chubby_swinging_38
      brooklyn.c "You have incredible, sexy tits."
      wt_image chubby_swinging_41
      chelsea.c "Thanks!  I love yours, too."
      wt_image chubby_swinging_3
      "Unsurprisingly, the man seems to enjoy both sets of tits, though he shows more interest in [chelsea.name]'s' new-to-him pair."
      wt_image chubby_swinging_4
      "You can't help but feel a twinge of jealousy as the two ladies work together on the lucky fellow."
      wt_image chubby_swinging_5
      "The ladies show no such signs of jealousy.  [chelsea.name] continues to suck the guy off as the other woman gets into position."
      wt_image chubby_swinging_51
      "Then she helps put him inside her. [chelsea.name]'s surprised at how quickly the other woman cums, perhaps not realizing it's the feel of [chelsea.name]'s own fingers, more than her partner's cock, that brings her to a fast climax."
      wt_image chubby_swinging_6
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_18
      "Now it's the other woman's turn to return the favor, putting [chelsea.name] into position and guiding her partner's cock inside her, before planting another kiss on [chelsea.name]."
      wt_image chubby_swinging_7
      "Between the kissing and the fucking, [chelsea.name]'s excitement ramps quickly."
      wt_image chubby_swinging_20
      "Brooklyn seems to be getting excited again, too.  She offers her pussy to [chelsea.name] ..."
      wt_image chubby_swinging_23
      "... then moans in delight as [chelsea.name] kisses and licks it."
      wt_image chubby_swinging_49
      "Her moans are soon joined by [chelsea.name]'s, who brings herself to orgasm while she licks Brooklyn's pussy, her own fingers on her clit as the man's cock drives in and out of her."
      wt_image chubby_swinging_48
      chelsea.c "Aahhhhhh"
      wt_image chubby_swinging_21
      "A few minutes later, both ladies are riding their way to their second orgasm of the night."
      wt_image chubby_swinging_44
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_45
      chelsea.c "Aaahhhhhh"
      wt_image chubby_swinging_32
      chelsea.c "Doesn't he get to cum?"
      wt_image chubby_swinging_38
      brooklyn.c "Not yet. I let him fuck other women, but the deal is I have to be part of it, and he doesn't get to cum until he thanks me properly at home.  I'm Brooklyn, by the way.  Hope I see you again, soon."
      wt_image chubby_swinging_10
      "You're not sure if you're quite as jealous of him now, but you're still somewhat jealous."
      $ chelsea.lesbian_club_count = 4
    elif chelsea.lesbian_status > 7 and chelsea.lesbian_club_count > 0:
      wt_image chubby_swinging_1
      "[chelsea.name] spots her favorite couple and heads right over."
      wt_image chubby_swinging_40
      "Ignoring the man, [chelsea.name] leans in and nuzzles Brooklyn."
      wt_image chubby_swinging_13
      chelsea.c "Do you mind if I join you?"
      wt_image chubby_swinging_40
      brooklyn.c "You've changed."
      wt_image chubby_swinging_41
      chelsea.c "Uh huh"
      wt_image chubby_swinging_14
      "Brooklyn smiles as [chelsea.name] pulls down her bra ..."
      wt_image chubby_swinging_3
      "... then moves around to plant a full tongued kiss on her."
      wt_image chubby_swinging_4
      "You can't help but feel a twinge of jealousy as the two ladies work together on the lucky fellow."
      wt_image chubby_swinging_5
      "The ladies show no such signs of jealousy. [chelsea.name] continues to suck the guy off as Brooklyn gets into position."
      wt_image chubby_swinging_17
      "[chelsea.name] plants a kiss on Brooklyn as her husband enters her.  Then she reaches a hand down and plays with herself while exploring the other woman's mouth as Brooklyn gets fucked to orgasm."
      wt_image chubby_swinging_53
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_18
      "Now it's Brooklyn's turn to return the favor, putting [chelsea.name] into position and guiding her husband's cock inside her."
      wt_image chubby_swinging_7
      "[chelsea.name] eagerly seeks out Brooklyn's mouth as the woman's fingers tweak and play with [chelsea.name]'s nipple while the man pistons his hard cock in and out of [chelsea.name]'s rapidly wettening pussy."
      wt_image chubby_swinging_20
      "Once again Brooklyn offers her pussy to [chelsea.name] ..."
      wt_image chubby_swinging_23
      "... then moans in delight as [chelsea.name] kisses and licks it."
      wt_image chubby_swinging_50
      "Her moans are soon joined by [chelsea.name]'s, who brings herself to orgasm soon after she gets Brooklyn off, her own fingers on her clit as the man's cock drives in and out of her."
      wt_image chubby_swinging_49
      brooklyn.c "ooooo"
      wt_image chubby_swinging_48
      chelsea.c "Aahhhhhh"
      wt_image chubby_swinging_54
      "This time Brooklyn leaves [chelsea.name] on her back, and as her partner pulls out of [chelsea.name], reciprocates for the pleasure [chelsea.name] just provided to her by lowering her head between [chelsea.name]'s legs ..."
      wt_image chubby_swinging_55
      "... as her partner moves his cock from [chelsea.name]'s pussy to hers."
      wt_image chubby_swinging_24
      "It seems instead of the man's tongue, [chelsea.name] will be riding his wife's tongue to her second orgasm of the night."
      wt_image chubby_swinging_56
      chelsea.c "Aaahhhhhh"
      wt_image chubby_swinging_25
      brooklyn.c "oooooooo"
      "If you had any doubts about whether [chelsea.name] had embraced bi-sexuality, this puts them to rest."
      $ chelsea.lesbian_club_count = 4
    elif chelsea.lesbian_status > 4 and chelsea.lesbian_status < 8 and chelsea.lesbian_club_count > 0:
      wt_image chubby_swinging_1
      "[chelsea.name] spots her favorite couple and heads right over."
      wt_image chubby_swinging_2
      chelsea.c "Do you mind if I join you?"
      wt_image chubby_swinging_38
      brooklyn.c "Not at all."
      wt_image chubby_swinging_12
      "She leans in to kiss [chelsea.name], and at first you think [chelsea.name] is going to accept the kiss ..."
      wt_image chubby_swinging_11
      "... then she turns and kisses the man instead. Undeterred, Brooklyn uses the opportunity to squeeze [chelsea.name]'s breast."
      wt_image chubby_swinging_4
      "You can't help but feel a twinge of jealousy as the two ladies work together on the lucky fellow."
      wt_image chubby_swinging_5
      "The ladies show no such signs of jealousy. [chelsea.name] continues to suck the guy off as the other woman gets into position."
      wt_image chubby_swinging_16
      "[chelsea.name] tries to move away as the man enters his partner, but Brooklyn grabs her and pulls her close. This time, [chelsea.name] accepts the woman's kiss, and explores her mouth with her tongue as Brooklyn is fucked to orgasm."
      wt_image chubby_swinging_43
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_18
      "Now it's Brooklyn's turn to return the favor, putting [chelsea.name] into position and guiding her partner's cock inside her."
      wt_image chubby_swinging_7
      "[chelsea.name] resigns herself to receiving the woman's kiss, and her nipple stiffens involuntarily as Brooklyn's fingers tweak and play with it while the man pistons his hard cock in and out of [chelsea.name]'s rapidly wettening pussy."
      wt_image chubby_swinging_8
      "Once again Brooklyn offers her pussy to [chelsea.name], and once again [chelsea.name] ignores it.  Brooklyn contents herself with playing with [chelsea.name]'s breasts and receiving a thank you kiss from her partner, who's having a lot of fun. Almost as much fun as [chelsea.name], who shudders to orgasm, her own fingers on her clit as the man's cock drives in and out of her."
      wt_image chubby_swinging_48
      chelsea.c "Aahhhhhh"
      wt_image chubby_swinging_9
      "Brooklyn positions herself and [chelsea.name] facing each other as they ride her husband to their second orgasm of the night, each.  This time, [chelsea.name] consents to another kiss.  She even places a hand on the other woman's breast as they kiss, an innocent touch, but one that helps take Brooklyn over the edge."
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_42
      "[chelsea.name]'s not far behind her.  You figure the man has earned the right to cum, too, but it seems he's going to hold off until his woman tells him he can, and it seems that permission isn't coming while the two of them are at the Club."
      chelsea.c "Aaahhhhhh"
      if chelsea.lesbian_club_count == 2:
        "[chelsea.name]'s still reluctant to let herself go with the flow and accept her body's response to another woman, and other women's responses to her, but she's not shutting them down completely..  That's progress, and may affect her thinking once she's had a chance to absorb the experience."
        $ chelsea.lesbian_status += 1
        $ chelsea.lesbian_club_count = 3
      else:
        "[chelsea.name] responded to the woman exactly the same way she did the last time. If you want her to change, you'll need to introduce her to new experiences to broaden her horizons and help her reflect on how she really feels about touching and being touched by another woman."
    elif chelsea.lesbian_status > 1 and chelsea.lesbian_status < 5 and chelsea.lesbian_club_count > 0:
      wt_image chubby_swinging_1
      "[chelsea.name] spots the couple from her last visit sitting on a sofa and heads right over."
      wt_image chubby_swinging_2
      chelsea.c "Do you mind if I join you?"
      wt_image chubby_swinging_38
      brooklyn.c "Not at all."
      wt_image chubby_swinging_11
      "She leans in to kiss [chelsea.name], but [chelsea.name] avoids her by turning her head and kissing her partner instead. Undeterred, the woman uses the opportunity to squeeze [chelsea.name]'s breast."
      wt_image chubby_swinging_4
      "You can't help but feel a twinge of jealousy as the two ladies work together on the lucky fellow."
      wt_image chubby_swinging_5
      "The ladies show no such signs of jealousy. [chelsea.name] continues to suck the guy off as Brooklyn gets into position."
      wt_image chubby_swinging_51
      "[chelsea.name] might have realized that it was her touch that set Brooklyn off so quickly last time, as she moves her hand away after she helps guide the man into his partner."
      wt_image chubby_swinging_52
      "She seems paralyzed with shock, however, as Brooklyn pulls her close and wraps her lips around [chelsea.name]'s nipple, suckling it as her husband fucks her to orgasm."
      wt_image chubby_swinging_15
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_19
      "Now it's Brooklyn's turn to return the favor, putting [chelsea.name] into position and guiding her husband's cock inside your girlfriend.  This time [chelsea.name] avoids the woman's kiss, but can't evade the woman's hand cupping her breast."
      wt_image chubby_swinging_20
      "As soon as she rolls over, however, [chelsea.name] removes Brooklyn's hand.  The look of disappointment on Brooklyn's face is palpable as [chelsea.name] ignores her offered pussy, but she respects [chelsea.name] decision and contents herself with watching as [chelsea.name] shudders to orgasm, her own fingers on her clit as the man's cock drives in and out of her."
      wt_image chubby_swinging_48
      chelsea.c "Aahhhhhh"
      wt_image chubby_swinging_22
      "Brooklyn then positions herself and [chelsea.name] facing each other on top of the man.  It's clear she's hoping for contact with [chelsea.name], but [chelsea.name] avoids her gaze and concentrates exclusively on the man's tongue working it's way back and forth, in and out of her sex as she rides his face."
      wt_image chubby_swinging_47
      "Brooklyn contains her disappointment and contents herself with the feeling of her husband's cock thrusting in and out of her as he eats [chelsea.name] to another climax."
      chelsea.c "Aaahhhhhh"
      wt_image chubby_swinging_46
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_22
      "You figure the man has earned the right to cum, but it seems he's going to hold off until his woman tells him he can, and that permission doesn't seem to be coming while the two of them are at the Club."
      if chelsea.lesbian_club_count == 1:
        "[chelsea.name] didn't respond the way you'd hoped she would, but she demonstrated an awareness of what the woman was looking for, as opposed to being completely oblivious to it like she was last time.  That's progress, in a way, and may affect her thinking once she's had a chance to absorb her own feelings about the woman's attraction to her."
        $ chelsea.lesbian_status += 1
        $ chelsea.lesbian_club_count = 2
      else:
        "[chelsea.name] responded to the woman exactly the same way she did the last time. If you want her to change, you'll need to introduce her to new experiences to broaden her horizons and help her reflect on how she really feels about touching and being touched by another woman."
    else:
      wt_image chubby_swinging_1
      "You expected [chelsea.name] might be a bit nervous entering the swingers room, but she isn't.  She spots an attractive couple sitting by themselves on a sofa, and heads right over."
      wt_image chubby_swinging_2
      chelsea.c "Do you mind if I join you?"
      wt_image chubby_swinging_10
      "The woman provides her answer in the form of a kiss. [chelsea.name] will tell you later that'd she'd kissed a girl before, when she was younger, and it 'just isn't her thing'."
      wt_image chubby_swinging_38
      chelsea.c "{i}She just surprised me.  I wasn't interested in kissing her.{/i}"
      wt_image chubby_swinging_4
      "You can't help but feel a twinge of jealousy as the two ladies work together on the lucky fellow."
      wt_image chubby_swinging_5
      "The ladies show no such signs of jealousy.  [chelsea.name] continues to suck the guy off as the other woman gets into position."
      wt_image chubby_swinging_51
      "Then she helps put him inside her. [chelsea.name]'s surprised at how quickly the other woman cums, perhaps not realizing it's the feel of [chelsea.name]'s own fingers, more than her partner's cock, that brings her to a fast climax."
      wt_image chubby_swinging_6
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_18
      "Now it's the other woman's turn to return the favor, putting [chelsea.name] into position and guiding her partner's cock inside her, before surprising [chelsea.name] with another unexpected kiss."
      wt_image chubby_swinging_7
      "If [chelsea.name] objects to the woman's hand on her breast, she doesn't say anything. After all, the woman is letting her husband fuck her, and [chelsea.name] wouldn't want to appear unappreciative."
      wt_image chubby_swinging_20
      "And if the other woman is disappointed that [chelsea.name] doesn't make use of her open and available pussy, she doesn't say anything either."
      wt_image chubby_swinging_8
      "She contents herself with playing with [chelsea.name]'s breasts and receiving a 'thank you' kiss from her partner, who's having a lot of fun. Almost as much fun as [chelsea.name], who shudders to orgasm, her own fingers on her clit as the man's cock drives in and out of her."
      wt_image chubby_swinging_48
      chelsea.c "Aahhhhhh"
      wt_image chubby_swinging_21
      "Soon both ladies are riding their way to their second orgasm of the night."
      wt_image chubby_swinging_44
      brooklyn.c "oooooooo"
      wt_image chubby_swinging_45
      chelsea.c "Aaahhhhhh"
      wt_image chubby_swinging_32
      chelsea.c "Doesn't he get to cum?"
      brooklyn.c "Not yet. I let him fuck other women, but the deal is I have to be part of it, and he doesn't get to cum until he thanks me properly at home.  I'm Brooklyn, by the way.  Hope I see you again, soon."
      "You're not sure if you're quite as jealous of him now, but you're still somewhat jealous."
      if chelsea.lesbian_club_count > 0:
        "[chelsea.name] responded to the woman exactly the same way she did the last time. If you want her to change, you should discuss that with her at home."
      elif chelsea.lesbian_status == 0:
        "[chelsea.name] seemed surprised by the woman's forwardness, but not totally repulsed. If you're interested in encouraging that type of behavior, you should discuss her feelings about women with [chelsea.name] when you get home."
        $ chelsea.lesbian_club_count = 1
        $ chelsea.lesbian_status = 1
      else:
        "[chelsea.name] seemed surprised at the woman's forwardness.  A threesome is a new experience for her and she didn't seem prepared for the idea of making love to both of them at the same time.  Perhaps you should try this experience with her again later."
        $ chelsea.lesbian_club_count = 1
    if not brooklyn.has_tag('did_not_watch'):
      change player energy by -energy_very_short notify
    rem tags 'no_bi_bj' 'bi_bj' 'did_not_watch' from brooklyn
    call character_location_return(chelsea) from _call_character_location_return_72
    call character_location_return(brooklyn) from _call_character_location_return_73
    wt_image swingers_room.image
  return

## Items
# Give Butt Plug
label give_bp_chelsea:
  if chelsea.has_item(butt_plug):
    "You've already given her a butt plug. She doesn't need another."
  else:
    if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
      if chelsea.anal_status == 0:
        "[chelsea.name] won't let you near her asshole. If you want that to change, you should mention your interest in anal to her sometime when the opportunity arises."
      elif chelsea.anal_status == 1:
        "[chelsea.name] doesn't want you anywhere near her anus, and you've decided you're happy to use her other holes. For the health of your relationship with her, better stick to that decision."
      else:
        if chelsea.relationship_counter >= 4 or chelsea.has_tag('relationship_warnings_shut_off'):
          "[chelsea.name] doesn't want you anywhere near her anus. Your relationship with her is strong enough that she will likely accept the gift if you insist, but it may impact how she feels about you."
          $ title = "Gift her the butt plug anyway?"
          menu:
            "Yes":
              if chelsea.hypno_re_anal > 1:
                $ chelsea.relationship_counter -= 2
              else:
                $ chelsea.relationship_counter -= 3
              if chelsea.has_tag('little_girl'):
                wt_image chubby_anal_youth_1_1
                player.c "I bought a gift for you, [chelsea.name]."
                chelsea.c "A gift??  What is it?"
                wt_image chubby_anal_youth_1_2
                player.c "It goes in your butt."
                chelsea.c "Ewwww!!  Why would you buy me that?"
                player.c "Because you're scared about trying anal sex, and I thought this would help you get comfortable with the idea."
                wt_image chubby_anal_youth_1_3
                chelsea.c "But I don't want you sticking anything up my bum.  That's gross."
                player.c "You don't know until you try it.  You may find you like it.  Won't you try it, for me?"
                wt_image chubby_anal_youth_1_4
                chelsea.c "Okay.  I'll try it.  For you."
                wt_image chubby_anal_youth_1_5
                "[chelsea.name] lies down on the bed as you lube up the toy."
                wt_image chubby_anal_youth_1_6
                "Slowly and carefully you push your gift inside her virgin ass."
                wt_image chubby_anal_youth_1_7
                player.c "How does that feel?"
                chelsea.c "Weird.  I'm not supposed to have something in there, certainly not something coming from that direction."
                player.c "Give it a few minutes to let your body get used to the sensation.  It may help if I move it back and forth."
                chelsea.c "No!  It feels weird enough as it is.  Leave it like that and I'll see if I can get used to it."
                wt_image chubby_anal_youth_1_8
                chelsea.c "Okay, I tried, but it still feels icky.  I'm going to take it out now."
              else:
                if chelsea.has_tag('bbw'):
                  wt_image chubby_anal_bbw_1_1
                  player.c "I bought a gift for you, [chelsea.name]."
                  chelsea.c "A gift??  What is it?"
                  wt_image chubby_anal_bbw_1_2
                  player.c "It goes in your butt."
                  chelsea.c "Ewwww!!  Why would you buy me that?"
                  player.c "Because you're scared about trying anal sex, and I thought this would help you get comfortable with the idea."
                  chelsea.c "But I don't want you sticking anything up my bum.  That's gross."
                  player.c "You don't know until you try it.  You may find you like it.  Won't you try it, for me?"
                  wt_image chubby_anal_bbw_1_3
                  chelsea.c "Okay.  I'll try it.  For you."
                  "[chelsea.name] removes her clothes as you get her some lube to put on the toy."
                else:
                  wt_image chubby_visit_toned_2_36
                  player.c "I bought a gift for you, [chelsea.name]."
                  wt_image chubby_visit_toned_2_37
                  chelsea.c "A gift??  What is it?"
                  player.c "It goes in your butt."
                  wt_image chubby_visit_toned_2_39
                  chelsea.c "Ewwww!!  Why would you buy me that?"
                  player.c "Because you're scared about trying anal sex, and I thought this would help you get comfortable with the idea."
                  wt_image chubby_visit_toned_2_31
                  chelsea.c "But I don't want you sticking anything up my bum.  That's gross."
                  player.c "You don't know until you try it.  You may find you like it.  Won't you try it, for me?"
                  wt_image chubby_visit_toned_2_38
                  chelsea.c "Okay, I'll try it.  For you."
                  wt_image chubby_visit_toned_2_10
                  "[chelsea.name] removes her clothes as you get her some lube to put on the toy."
                wt_image chubby_anal_bbw_1_4
                "[chelsea.name] insists on inserting the toy herself.  Slowly and cautiously she pushes your gift into her ass."
                player.c "How does that feel?"
                wt_image chubby_anal_bbw_1_5
                chelsea.c "Weird. I'm not supposed to have something in there, certainly not something coming from that direction."
                player.c "Give it a few minutes to let your body get used to the sensation. It may help if I move it back and forth."
                chelsea.c "No! It feels weird enough as it is. Leave it like that and I'll see if I can get used to it."
                wt_image chubby_anal_bbw_1_6
                chelsea.c "Okay, I tried, but it still feels icky. I'm taking it out now."
              "That was progress.  She let something be put in her butt for the first time.  Next time you can try something more personable than a toy.  She's still not ready for your dick, but she may accept another body part, if her relationship with you is strong enough."
              sys "[chelsea.name] is less happy with your relationship."
              change player energy by -energy_very_short
              $ chelsea.anal_count += 1
              $ chelsea.anal_status = 3
              give 1 butt_plug from player to chelsea notify
            "Not right now":
              pass
        else:
          "[chelsea.name] doesn't want you anywhere near her anus, and your relationship with her isn't strong enough right now to push her on this subject. Maybe try to give the plug to her later, when she's feeling better about you and her."
    else:
      "[chelsea.name] won't let you near her asshole. At least not right now"
  return

# Give Chastity Belt
label give_cb_chelsea:
    if chelsea.status == 'on_training':
        "[chelsea.name]'s too ashamed of her body to sleep with anyone, not even her husband. This isn't going to help."
    else:
        "Save this for someone else"
    return

# Give Dildo
label give_di_chelsea:
  if chelsea.has_item(dildo):
    "You've already given her a dildo.  You don't need to give her another."
  else:
    if chelsea.status == "post_training":
      wt_image chelsea.image
      if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
        if chelsea.has_tag('little_girl'):
          player.c "I bought something for you."
          chelsea.c "What is it?"
          player.c "A new toy for you."
          chelsea.c "Will I like it as much as the teddy bear you bought me?"
          player.c "I hope so."
          "She eagerly opens up the package, then pauses in shock when she sees what's inside."
          chelsea.c "Umm, am I old enough to play with one of these?"
          player.c "Of course you are.  You're growing up so fast."
          "[chelsea.name] hesitates, as if trying to decide what message you're sending, then decides you mean well and gives you a sweet kiss."
          chelsea.c "Thank you!"
        else:
          player.c "I bought something for you."
          chelsea.c "What is it?"
          player.c "A gift, for you."
          "She eagerly opens up the package, then pauses in shock when she sees what's inside."
          chelsea.c "Uh, wow!  Are you going away or something?"
          player.c "No, but sometimes you may have urges when I'm not around."
          "[chelsea.name] hesitates, as if trying to decide what message you're sending, then decides you mean well and gives you a sweet kiss."
          chelsea.c "Thank you!"
        sys "[chelsea.name] is happier with your relationship."
        $ chelsea.relationship_counter += 1
        give 1 dildo from player to chelsea notify
      else:
        "Save this for someone else."
    else:
      "[chelsea.name] should be sex-exercising with her husband at home, not playing by herself."
  return

# Use Fetch Toy
label use_ft_chelsea:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_chelsea:
    if chelsea.in_area('house'):
        if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
            if chelsea.has_tag('little_girl'):
                wt_image chubby_youth_4_3
                player.c "I bought something for you."
                chelsea.c "What is it?"
                player.c "A gift, for you."
                wt_image chubby_youth_4_4
                chelsea.c "Will I like it as much as the plushie you bought me?"
                player.c "I hope so."
                "You pass over the neatly wrapped box with the necklace in it."
                chelsea.c "What is this?  Is this ... did you buy me jewelry??"
                "[chelsea.name] hesitates, as if trying to decide if she should open it, then rips it open."
                chelsea.c "Oh!  Wow!!  Oh, this is beautiful!!"
                player.c "Try it on."
                wt_image chubby_youth_4_5
                "She beams as she wears her present.  You've made her very happy.  Having the necklace will remind her of you, even when you can't spend as much time with her as she'd like."
            else:
                if chelsea.has_tag('toned'):
                    wt_image chubby_toned_portrait_2
                else:
                    wt_image chubby_bbw_portrait_2_2
                player.c "I bought something for you."
                chelsea.c "What is it?"
                wt_image gift_image
                player.c "A gift, for you."
                "You pass over the neatly wrapped box with the necklace in it."
                chelsea.c "What is this?  Is this ... did you buy me jewelry??"
                wt_image chubby_jewelry_1
                "[chelsea.name] hesitates, as if trying to decide if she should open it, then rips it open."
                if chelsea.has_tag('toned'):
                    pass
                else:
                    wt_image chubby_bbw_portrait_2_3
                chelsea.c "Oh!  Wow!!  Oh, this is beautiful!!"
                if chelsea.has_tag('toned'):
                    wt_image chubby_toned_portrait_2
                else:
                    wt_image chubby_bbw_portrait_2_1
                "She beams as she wears her present.  You've made her very happy.  Having the necklace will remind her of you, even when you can't spend as much time with her as she'd like."
            sys "[chelsea.name] is happier with your relationship."
            $ chelsea.relationship_counter += 2
            give 1 jewelry_chelsea from player to chelsea notify
        elif chelsea.has_tag('slavegirl'):
            wt_image chubby_slave_16
            player.c "I have something for you."
            "A sense of dread fills her when she hears your words, as that normally means a new toy to use on her."
            wt_image chubby_slave_17
            "Her confusion is palpable when she sees the jewelry.  It's beautiful and  ... it's for her?? from you???"
            chelsea.c "Th ... thank you, [chelsea.your_name]!"
            wt_image chubby_slave_1
            "You've made your slavegirl very happy today."
            give 1 jewelry_chelsea from player to chelsea notify
        elif chelsea.has_item(lingerie):
            if chelsea.has_tag('toned'):
                wt_image chubby_toned_portrait_2
            else:
                wt_image chubby_bbw_portrait_2_2
            player.c "I bought something for you."
            chelsea.c "Oh yeah?  What is it?  Did you get me more lingerie?"
            wt_image gift_image
            player.c "No.  Something else.  I hope you like it."
            "You pass over the neatly wrapped box with the necklace in it."
            chelsea.c "What is this?  Is this ... did you buy me jewelry??"
            wt_image chubby_jewelry_1
            "[chelsea.name] hesitates, as if trying to decide if she should open it.  Eventually, her curiosity gets the better of her, and she unwraps the gift and picks up the necklace."
            if chelsea.has_tag('toned'):
                pass
            else:
                wt_image chubby_bbw_portrait_2_3
            chelsea.c "Oh!  Wow!!  Oh, this is beautiful.  I ... I'm not sure what to say?"
            player.c "Thank you would be nice."
            if chelsea.has_tag('toned'):
                wt_image chubby_visit_toned_1_2
            elif chelsea.has_tag('bbw'):
                wt_image chubby_bbw_portrait_2_1
            "She leans over and kisses you warmly."
            chelsea.c "Thank you, I love it.  But I'm sure you don't want to just talk about how much I liked it.  How about I show you instead?"
            give 1 jewelry_chelsea from player to chelsea notify
        else:
            "She's not quite ready.  Get her another gift first."
    else:
        "Try offering this to [chelsea.name] as a gift the next time the two of you are at your house together."
    return

# Use Leash
label use_le_chelsea:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_chelsea:
  if chelsea.has_item(lingerie):
    "You've already gifted lingerie to [chelsea.name].  She has enough for now."
  elif chelsea.status == 'on_training':
    wt_image chelsea.image
    $ title = "What type of lingerie do you want to gift to [chelsea.name]?"
    menu:
      "Slim and inspirational":
        if chelsea.has_tag('motivated'):
          "[chelsea.name]'s eyes light up as she sees the small, slinky outfit you bought her. With the dieting and working out that she's been doing, she may be able to fit into it already."
        else:
          "[chelsea.name]'s eyes light up as she sees the small, slinky outfit you bought her.  She'll never fit into it right now, but she can see how good she would look if - no, when - she does fit into it."
        add tags 'lingerie_motivated' to chelsea
        change chelsea desire_c by 5
      "Large but flattering":
        if not chelsea.has_tag('motivated'):
          "[chelsea.name]'s eyes light up as she sees the sexy outfit you bought her.  She's surprised to find out she can fit into it now. She's even more surprised to find out how good she looks wearing it."
        else:
          "[chelsea.name] seems confused at the size of the lingerie.  It's a bit larger than she needs after the dieting and working out she has been doing."
          player.c "Don't worry, [chelsea.name].  You'll look great in it."
        add tags 'lingerie_happy' to chelsea
        if chelsea.desire_c == 0:
          pass
        elif chelsea.desire_c <= 10:
          change chelsea desire_c by -chelsea.desire_c
        else:
          change chelsea desire_c by -10
        change chelsea sos by 5
    give 1 lingerie from player to chelsea notify
  elif chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
    wt_image chelsea.image
    if chelsea.has_tag('toned'):
      "[chelsea.name]'s eyes light up as she sees the small, slinky outfit you bought her.  With the dieting and working out she's done, she should fit into it nicely. With any luck, she'll model it for you soon."
      add tags 'lingerie_motivated' to chelsea
    else:
      "[chelsea.name]'s eyes light up as she sees the sexy outfit you bought her.  She loves that you find her body sexy enough that you want to see her dress up for you. With any luck, she'll model it for you soon."
      add tags 'lingerie_happy' to chelsea
    give 1 lingerie from player to chelsea notify
  elif chelsea.in_area('house') and chelsea.has_tag('continuing_actions'):
    chelsea.c "Oh wow!  this is really nice.  I might have to try this on with you sometime.  Thank you!"
    "She leans over and gives you a peck on the cheek."
    chelsea.c "So, what did you want to do today?  I don't imagine you called me over here just to talk about what a nice guy you are for giving me a sweet gift."
    sys "[chelsea.name] is happier with your relationship."
    $ chelsea.relationship_counter += 1
    if chelsea.has_tag('toned'):
      add tags 'lingerie_motivated' to chelsea
    elif chelsea.has_tag('bbw'):
      add tags 'lingerie_happy' to chelsea
    give 1 lingerie from player to chelsea notify
  else:
    "You should save the lingerie for someone else, or at least for another time."
  return

# Give Love Potion
label give_lp_chelsea:
  if chelsea.has_tag('love_potion_used'):
    "You've already used a love potion on [chelsea.name].  Additional ones won't work."
  elif chelsea.status == 'on_training':
    "[chelsea.name] isn't a good candidate for the love potion. An infatuation with you isn't going to help her resolve her body issues."
  elif chelsea.has_tag('girlfriend'):
    "[chelsea.name] is already your girlfriend. Are you sure you want to give her the potion, and increase her infatuation with you?"
    $ title = "Use love potion on her?"
    menu:
      "Yes":
        wt_image chubby_transformation_potion_1
        player.c "I fixed you something to drink."
        chelsea.c "Oh!  My favorite.  Thank you."
        wt_image chubby_love_potion_2
        chelsea.c "Mmmmm. You are so sweet! I am so lucky to have you as my boyfriend!!"
        add tags 'love_potion_used' to chelsea
        sys "[chelsea.name] is happier with your relationship."
        $ chelsea.relationship_counter += 5
        rem 1 love_potion from player notify
      "No, save it for someone else":
        pass
  elif chelsea.has_tag('continuing_actions'):
    wt_image chubby_transformation_potion_1
    player.c "I fixed you something to drink."
    chelsea.c "Oh!  My favorite.  Thank you."
    wt_image chubby_love_potion_2
    chelsea.c "Mmmmm.  You are so sweet! I am so lucky to get to spend time with you!!"
    "Under the influence of the love potion, [chelsea.name] will greatly enjoy the time you spend together. If time goes by without her getting to spend time with you, however, her old self-esteem issues may creep back in, making her question whether you're really interested in her."
    sys "[chelsea.name] is happier with your relationship."
    add tags 'love_potion_used' to chelsea
    $ chelsea.relationship_counter += 5
    rem 1 love_potion from player notify
  else:
    "You should save the love potion for someone else, or at least for another time."
  return

# Give Transformation Potion
# OBJECT & TIMER
label give_tp_chelsea:
    if chelsea.has_tag('transformed'):
        "She has already been transformed. The potion can do nothing more to her."
    elif chelsea.status == "post_training":
        if current_location == bedroom or current_location == living_room:
            wt_image chubby_transformation_potion_1
            player.c "I fixed you something to drink."
            chelsea.c "Oh!  My favorite.  Thank you."
            wt_image chubby_transformation_potion_2
            "The potion takes effect almost immediately. Her eyes go dead and her jaw slackens, drool dripping from her mouth as the potion opens her up to the potential for great change."
            "You now need to spend some energy helping the potion realize a new potential for her."
            rem 1 transformation_potion from player
            change player energy by -energy_long notify
            $ title = "What do you want to transform her into?"
            menu:
                "Bi-sexual" if not chelsea.has_tag('likes_girls'):
                    "Like many young women of her generation, [chelsea.name] fooled around once with another girl when she was a young woman. It did nothing for her, and she never thought much ever again about being with another woman."
                    "The potion finds that long ago curiosity and twists it. Instead of being something she tried and didn't like, it becomes something she didn't try enough. Something she should have spent more time doing. Something she craves experiencing again."
                    player.c "[chelsea.name], would you like it if I helped you to find a woman who would want to sleep with you?"
                    chelsea.c "How did you know?  Yes ... yes, I would love it if you could do that."
                    "Once she recovers from the effect of the potion, you can arrange a lesbian tryst for [chelsea.name]."
                    $ chelsea.training_session()
                    $ chelsea.transformed_via_object = True
                    call convert(chelsea,'lesbian') from _call_convert_66
                    $ chelsea.lesbian_status = 8
                    add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to chelsea
                    call character_location_return(chelsea) from _call_character_location_return_74
                "Girlfriend" if not chelsea.has_tag('girlfriend') and not chelsea.has_tag('hypno_girlfriend'):
                    "After the amount of time [chelsea.name] has spent with you - and the things the two of you have done together - it's hardly surprising that [chelsea.name] has thought about what life would be like with you."
                    "The potion finds those thoughts and amplifies them, until she no longer just wonders about what it would be like, she longs to learn what it's like.  She needs to be with you."
                    chelsea.c "Do ... do you think I could move in with you?"
                    player.c "Leave your husband and move in with me?"
                    chelsea.c "Yes.  Yes ... I, I really want to be with you."
                    player.c "You know there are many women in my life."
                    chelsea.c "That's okay. I don't mind. As long as I can share some part of your life."
                    $ chelsea.training_session()
                    $ chelsea.transformed_via_object = True
                    call chelsea_convert_girlfriend from _call_chelsea_convert_girlfriend_3
                    call character_location_return(chelsea) from _call_character_location_return_75
                "Slavegirl" if chelsea.spanked > 1 and not chelsea.has_tag('slavegirl'):
                    "[chelsea.name] never had more than a mild curiosity about BDSM before she met you. The experience of writhing under your flogger as you beat her, however, has been one than she has re-lived in her mind over and over again.  It's not something she wants to do again, but alone in the dark, fantasizing about it, the intensity of the experience is enough to get her wet."
                    "The potion finds those feelings and amplifies them. It isn't just something she wants to remember and fantasize about. It's something she wants to feel again. Needs to feel again. Must feel again."
                    player.c "Slave, are you ready to give yourself to me?  Completely."
                    "She's too weak to speak.  She just nods and falls to her knees. You lead her into the bedroom."
                    $ chelsea.training_session()
                    $ chelsea.transformed_via_object = True
                    call chelsea_convert_slavegirl from _call_chelsea_convert_slavegirl
                    call character_location_return(chelsea) from _call_character_location_return_76
                "Nothing (undo)":
                    "Let's back that up and pretend you didn't try using the transformation potion on her.  That's easier than reloading an old save."
                    add 1 transformation_potion to player
                    change player energy by energy_long
        else:
            "Not here."
    else:
        "You shouldn't try this while [chelsea.name] is a client. Her husband knows she's here and may cause trouble."
    return

# Give Ring of Sexuality
label give_rs_chelsea:
    if chelsea.has_item(ring_sexuality):
        "You already gave her one."
    elif chelsea.has_tag('likes_girls'):
        "She's already into other women.  Save this for someone else."
    elif chelsea.has_any_tag('girlfriend', 'hypno_girlfriend'):
        if chelsea.in_area('house'):
            if chelsea.has_tag('little_girl'):
                wt_image chubby_youth_4_1
                player.c "I bought something for you."
                wt_image chubby_youth_4_2
                chelsea.c "Oh!  Wow!!  Oh, this ring is beautiful!!"
            else:
                wt_image rs_image
                player.c "I bought something for you."
                if chelsea.has_tag('toned'):
                    if chelsea.has_item(jewelry_chelsea):
                        wt_image chubby_toned_portrait_2
                    else:
                        wt_image chubby_toned_portrait_1
                else:
                    if chelsea.has_item(jewelry_chelsea):
                        wt_image chubby_bbw_portrait_2_1
                    else:
                        wt_image chubby_bbw_portrait_1_1
                chelsea.c "Oh!  Wow!!  Oh, this ring is beautiful!!"
            sys "[chelsea.name] is happier with your relationship."
            $ chelsea.relationship_counter += 2
            give 1 ring_sexuality from player to chelsea notify
            call convert(chelsea,'lesbian') from _call_convert_1
            $ chelsea.lesbian_status = 8
            add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to chelsea
        else:
            "Not here."
    else:
        "You don't have the type of relationship where giving her a ring is appropriate."
    return

# Use Water Bowl
label use_wb_chelsea:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
# OBJECT & TIMER
label use_wt_chelsea:
  if chelsea.has_tag('transformed'):
    "[chelsea.name] has already been transformed. The Will-Tamer can do nothing more to her now."
  else:
    if chelsea.has_tag('will_tamer_this_week'):
      "You have already used the Will-Tamer on [chelsea.name] this week. Let its effects continue to work on her brain for a few days, then you can try using it again next week."
    else:
      $ chelsea.temporary_count = 0
      if chelsea.test('resistance',30) and chelsea.will_tamer_count < 3:
        wt_image chelsea.image
        if chelsea.will_tamer_count == 0:
          "[chelsea.name] looks dubious as you approach with the collar. You can feel the warmth of the Will-Tamer as you snap it in place around her pretty neck."
          wt_image chubby_collar
          chelsea.c "Is this really necessary?"
          player.c "No, but I like the way you look in it."
          "Andv you think, I like what it does when you're in it. You don't leave her in it for long. Just enough for it to start to re-wire her brain. Those changes will become stronger over the coming week, at which point you could put her in it again."
          change chelsea resistance by -15 notify
          $ chelsea.will_tamer_count = 1
          add tags 'will_tamer_this_week' to chelsea
        elif chelsea.will_tamer_count == 1:
          player.c "[chelsea.name], I want you to wear your collar again."
          chelsea.c "My collar?"
          wt_image chubby_collar
          player.c "Well, that's what I think of it as when you're wearing it."
          if chelsea.test('resistance',30):
            chelsea.c "It's so strange ... I'm starting to enjoy the way this collar ... my collar ... feels."
          change chelsea resistance by -15 notify
          $ chelsea.will_tamer_count = 2
          add tags 'will_tamer_this_week' to chelsea
        elif chelsea.will_tamer_count == 2:
          player.c "[chelsea.name], it's time for you to wear your collar again."
          wt_image chubby_collar
          if chelsea.test('resistance', 0):
            "[chelsea.name] sighs contentedly as you snap the Will-Tamer in place around her neck."
            chelsea.c "Thank you for collaring me."
            player.c "Is that how you think you should be addressing me?"
            "[chelsea.name] hesitates for a moment."
            chelsea.c "Thank you for collaring me, Master."
            $ chelsea.will_tamer_count = 3
            "The Will-Tamer has re-programmed [chelsea.name]'s brain to the point that she's ready to undergo a more complete transformation. One more use will do it."
          else:
            chelsea.c "It's so strange ... I'm starting to enjoy the way this collar ... my collar ... feels."
            change chelsea resistance by -15 notify
          add tags 'will_tamer_this_week' to chelsea
      elif chelsea.has_tag('slavegirl'):
        "She's already your slave. The Will-Tamer will have no additional effect on her."
      elif chelsea.will_tamer_count == 3 and chelsea.status == 'on_training':
        "Wait until she finishes her training first. Her husband knows she's here and may become suspicious."
      elif chelsea.will_tamer_count == 3 and (current_location == bedroom or current_location == living_room):
        "If you let the Will-Tamer take its full effect, the [chelsea.name] you know now will be lost, permanently. You will also lose the Will-Tamer, which will become absorbed into [chelsea.name]'s very being."
        $ title = "Do you want the Will-Tamer to transform [chelsea.name]?"
        menu:
          "Yes (make her a slavegirl)":
            wt_image chelsea.image
            player.c "It's time to put your collar on."
            chelsea.c "Again?"
            wt_image chubby_collar
            player.c "This will be the last time."
            wt_image chubby_transformation_potion_2
            "You leave the Will-Tamer on a little longer today. Soon [chelsea.name]'s eyes go dead. Drool escapes from her slack jaw as her brain shuts down, overwhelmed by the influence of the Will-Tamer."
            "[chelsea.name]'s not naturally a submissive woman. Prior to meeting you, she would never have contemplated the idea of being anyone's slave."
            "Under the influence of the Will-Tamer, [chelsea.name]'s experiences following your instructions are amplified, until she can think of nothing other than a burning desire to do as you say and please you in any way she can"
            $ chelsea.training_session()
            $ chelsea.transformed_via_object = True
            rem 1 will_tamer from player
            call chelsea_convert_slavegirl from _call_chelsea_convert_slavegirl_1
          "No":
            pass
      elif chelsea.will_tamer_count == 3:
        "Not here. Wait until you get her home."
      else:
        chelsea.c "A collar? Really? I don't think I'm ready to be your slavegirl or whatever you're thinking."
        "Perhaps you should wait until her resistance to your instructions is lower."
  return

# Jewelry
label jwc_examine:
  wt_image chubby_jewelry_1
  "A beautiful necklace with a silver heart pendant. She should love this, and it will be a constant reminder about how you think of her. That by itself won't win her heart, but it will help."
  return

label give_jwc_fallback:
  "Save this for [chelsea.name]."
  return

########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Client Engagement Ends
label chelsea_end_training:
  # don't use .test in evaluating training success, use raw stats so as not to pick up temporary modifiers, room effects, etc.
  #if chelsea.test('desire_c', 60) and chelsea.test('desire_c', 'sos', -50):
  if chelsea.desire_c > 60 and chelsea.desire_c - chelsea.sos >= 50:
    add tags 'toned' to chelsea
    wt_image chubby_visit_toned_1_11
    "Your engagement to train [chelsea.name] the Chubby has now ended. You receive an email from her husband."
    husband_chelsea "{i}I can't thank you enough for how much you've helped [chelsea.name]. She's slimmer than she's ever been, and seems completely motivated to keep her new, hot toned body.{/i}"
    husband_chelsea "{i}Best of all, she's completely open to having sex now on a regular basis.{/i}"
    husband_chelsea "{i}I'll be leaving positive feedback for you.{/i}"
    "[chelsea.name] the Chubby has become [chelsea.name] the Toned"
    call convert(chelsea,"satisfied", False, True) from _call_convert_67
    rem tags 'conflicted' 'motivated' 'happy' from chelsea
    $ chelsea.suffix = "the Toned"
  #elif chelsea.test('sos', 50) and chelsea.test('sos', 'desire_c', -50):
  elif chelsea.sos > 50 and chelsea.sos - chelsea.desire_c >= 50:
    add tags 'bbw' to chelsea
    wt_image chubby_bbw_portrait_1_1
    "Your engagement to train [chelsea.name] the Chubby has now ended. You receive an email from her husband."
    husband_chelsea "{i}I can't thank you enough for how much you've helped [chelsea.name]. She's as big as she's ever been, but more importantly, she's happy.{/i}"
    husband_chelsea "{i}She seems comfortable with her body in a way she never was before she worked with you. Best of all, she's completely open to having sex now on a regular basis.{/i}"
    husband_chelsea "{i}I'll be leaving positive feedback for you.{/i}"
    "[chelsea.name] the Chubby has become [chelsea.name] the BBW."
    call convert(chelsea,"satisfied", False, True) from _call_convert_68
    rem tags 'conflicted' 'happy' 'motivated' from chelsea
    $ chelsea.suffix = "the BBW"
  else:
    wt_image chubby_nervous
    "Your engagement to train [chelsea.name] the Chubby has now ended."
    "Unfortunately,[chelsea.name] is still conflicted about her body image. Part of her wants to lose weight and stick to a workout routine. Part of her wants to stay as she is."
    "Despite her time with you, she hasn't been able to resolve that conflict. She and her husband will have to look for other solutions."
    call convert(chelsea,"unsatisfied", False, True) from _call_convert_69
  return

# Start Day
label chelsea_start_day_early_events:
    # Monday and Chubby GF Event?
    if day == 1 and week > chelsea.event_week and chelsea.event_week > 0:
        if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
            if chelsea.gf_event == 2:
                add tags 'early_event_today' to chelsea
                call chelsea_girlfriend_event from _call_chelsea_girlfriend_event
    return

label chelsea_start_day:
    ## Hypno Girlfriend Maintenance
    if day == 1 and chelsea.has_tag('hypno_girlfriend'):
        sys "It's time to maintain the hypnotic spell that keeps [chelsea.full_name] thinking that she's your girlfriend. If you don't maintain the hypnotic spell, you'll lose her and be unable to get her back."
        $ title = "Maintain [chelsea.full_name] as your hypno-girlfriend?"
        menu menu_chelsea_hypno_maintenance_menu:
            "Yes, maintain her (costs [energy_hypnosis.value] energy)":
                rem tags 'check_for_hypno_release' from chelsea
                if chelsea.has_tag('little_girl'):
                    wt_image chubby_hypno_gf_youth_1
                elif chelsea.has_tag('bbw'):
                    wt_image chubby_hypno_gf_bbw_6
                else:
                    wt_image chubby_hypno_gf_toned_1
                "You spend some energy maintaining your hypnotic control over [chelsea.full_name]."
                $ chelsea.relationship_counter = 5
                change player energy by -energy_hypnosis notify
            "No, let her go" if not chelsea.has_tag('check_for_hypno_release'):
                add tags 'check_for_hypno_release' to chelsea
                sys "Are you sure?  If you don't maintain the hypnotic spell, you will lose her permanently."
                jump menu_chelsea_hypno_maintenance_menu
            "No, really let her go" if chelsea.has_tag('check_for_hypno_release'):
                rem tags 'check_for_hypno_release' from chelsea
                wt_image chubby_confused_1
                "By not maintaining your hypnotic trance, your control over [chelsea.full_name] weakens. Confused as to where she is, she wanders off.  She will have no memories of her time with you. Hopefully she will get her life back in order, with no lingering effects from the black hole in her mind associated with her time under your control, "
                call convert(chelsea, "unavailable") from _call_convert_2
    # Monday and Chubby GF Event? (if not run during early star label)
    if day == 1 and week > chelsea.event_week and chelsea.event_week > 0 and not chelsea.has_tag('early_event_today'):
        if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend'):
            call chelsea_girlfriend_event from _call_chelsea_girlfriend_event_1
    return

# End Day
label chelsea_end_day:
  ## NOTE: this won't work if the automatic removals of 'trained_today' runs before Chelsea's end_day label, so need to watch this
  if chelsea.status == "post_training" and chelsea.has_tag('trained_today'):
    $ chelsea.visit_count += 1
  if chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend') or chelsea.has_tag('slavegirl'):
    $ chelsea.location = bedroom
    rem tags 'follows' 'bound_inside_now' 'bound_outside_now' 'early_event_today' 'frozen' 'slave_decoration_now' 'slave_tied_now' 'slave_suspended_now' 'slave_dildo_now' 'slave_plugged_now' from chelsea
  if chelsea.status == "on_training":
    call character_location_return(chelsea) from _call_character_location_return_77
  if player.has_tag('chelsea_weekend_message_today'):
    rem tags 'chelsea_weekend_message_today' from player
  if chelsea.has_tag('club_date_night'):
    rem tags 'club_date_night' from chelsea
  if chelsea.has_tag('likes_girls') and not chelsea.has_tag('marilyn_talk_option_possible'):
    add tags 'marilyn_talk_option_possible' 'janice_talk_option_possible' to chelsea
  return

# End Week
label chelsea_end_week:
  # Chubby Client?
  if chelsea.status == "on_training":
    if not chelsea.has_tag('trained_this_week') and chelsea.sos > 0:
      # "change" will pick up mods which you don't want, so adjust stats directly
      #change chelsea sos by -5 no_message
      $ chelsea.sos -= 5
    if chelsea.desire_c > 0:
      #change chelsea desire_c by -5 no_message
      $ chelsea.desire_c -= 5
    if chelsea.has_tag('failed_regular_training_this_week'):
      rem tags 'failed_regular_training_this_week' from chelsea
  # Chubby Relationship Counter
  # girlfriend maintenance
  if chelsea.has_tag('girlfriend'):
    if chelsea.visit_count == 0:
      sys "[chelsea.name] is less happy with your relationship."
      if chelsea.has_item(jewelry_chelsea):
        $ chelsea.relationship_counter -= 0.25
      else:
        $ chelsea.relationship_counter -= 0.5
    elif chelsea.visit_count < 2:
      sys "[chelsea.name] is happier with your relationship."
      if chelsea.has_tag('love_potion_used'):
        $ chelsea.relationship_counter += 1
      $ chelsea.relationship_counter += 1
    else:
      sys "[chelsea.name] is happier with your relationship."
      $ chelsea.relationship_counter += 2
  # Continuing actions maintenance
  if chelsea.has_tag('continuing_actions'):
    # notice about relationship changes - notice is only given after weeks when you didn't visit, this is easier than re-doing all the math around the gains/declines
    if chelsea.visit_count < 1 and chelsea.relationship_counter > 0:
      if chelsea.has_tag('love_potion_used'):
        sys "[chelsea.name] is much less happy with your relationship.  Under the influence of the love potion, she really misses you."
      else:
        sys "[chelsea.name] is less happy with your relationship."
    # math behind relationship changes; easier to leave than to
    if chelsea.has_tag('love_potion_used') and chelsea.visit_count < 1 and chelsea.relationship_counter >= 2:
      $ chelsea.relationship_counter -= 2
    elif chelsea.relationship_counter >= 1:
      $ chelsea.relationship_counter -= 1
    elif chelsea.relationship_counter > 0:
      $ chelsea.relationship_counter = 0
  ## Relationship Warnings
  if chelsea.has_tag('girlfriend') and not chelsea.has_tag('relationship_warnings_shut_off'):
    if chelsea.relationship_counter > 0 and chelsea.relationship_counter <= 1:
      if chelsea.has_tag('little_girl'):
        wt_image chubby_insecure_youth_3
        "A forlorn-looking [chelsea.name] comes to speak to you."
        wt_image chubby_insecure_youth_1
        chelsea.c "I don't feel very good, [chelsea.your_name]. I'm not sure I can be the little girl you want me to be. Maybe Teddy and I need to find a new home to live in?"
      else:
        if chelsea.has_tag('bbw'):
          wt_image chubby_insecure_bbw_1
          "A forlorn-looking [chelsea.name] comes to speak to you."
          wt_image chubby_insecure_bbw_5
          chelsea.c "This isn't really working out, is it [chelsea.your_name]?"
          wt_image chubby_insecure_bbw_2
          chelsea.c "I'm so fat.  You've probably become tired of having such a fat girlfriend.  Or maybe I just can't be the type of girlfriend you want."
        elif chelsea.has_tag('toned'):
          wt_image chubby_exercise_motivated_11
          "A forlorn-looking [chelsea.name] looks over at you from where she's exercising."
          chelsea.c "This isn't really working out, is it [chelsea.your_name]?"
          wt_image chubby_exercise_motivated_1
          chelsea.c "I'm trying so hard to make my body look good for you, but I'm just not as pretty or sexy as the other women you see. Or maybe I just can't be the type of girlfriend you want."
      sys "If you want to maintain your relationship with [chelsea.name], you'd better spend some time with her. And perhaps hold off for a while on asking for things she's not comfortable doing."
    if chelsea.relationship_counter <= 0:
      if chelsea.has_tag('love_potion_used') or chelsea.has_tag('transformed_girlfriend'):
        if chelsea.has_tag('little_girl'):
          wt_image chubby_insecure_youth_1
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_insecure_bbw_3
          elif chelsea.has_tag('toned'):
            wt_image chubby_exercise_motivated_11
        "A forlorn-looking [chelsea.name] watches you from across the room. She's miserable, but she's too much in love with you as a result of the potion to ever leave you."
        add tags 'relationship_warnings_shut_off' to chelsea
      else:
        "A forlorn-looking [chelsea.name] comes to speak to you."
        if chelsea.has_tag('little_girl'):
          wt_image chubby_insecure_youth_2
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_insecure_bbw_4
          elif chelsea.has_tag('toned'):
            wt_image chubby_exercise_motivated_1
        chelsea.c "This isn't working out. I hoped it would, and I gave it my best try, but this relationship just isn't right for me. I'm going back to my husband, assuming he'll take me back. Good bye, [chelsea.your_name]. I'll miss you!"
        rem tags 'continuing_actions' from chelsea
        $ chelsea.event_week = 0
        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
        call convert(chelsea, "unavailable") from _call_convert_71 ## note: watch for loss of history, as all chelsea tags will now be deleted, which may affect Lee, etc., depending on how past events were recorded
        dismiss chelsea
        wt_image current_location.image
  ## Reset Session Actions
  $ chelsea.visit_count_total += chelsea.visit_count
  $ chelsea.visit_count = 0
  call character_location_return(chelsea) from _call_character_location_return_78
  return

## Club and Stage Labels
label chelsea_swingers_room_call:
    if chelsea.can_be_interacted and (chelsea.has_tag('girlfriend') or chelsea.has_tag('hypno_girlfriend')):
        add tags 'in_swingers_room_now' to chelsea
    else:
        "[chelsea.name] is not available to join you right now."
    return

label chelsea_swingers_room_send_home:
    call character_location_return(chelsea) from _call_character_location_return_79
    rem tags 'in_swingers_room_now' from chelsea
    return

## Club President Wife Content
label chelsea_gloria_other_talk_option:
    if not gloria.has_tag('discussed_bra_fitter') and chelsea.bra_fitting_status > 0:
        player.c "My girlfriend's having a hard time finding bras to fit her. Where do you get your bras? [chelsea.name]'s rather well endowed. Not as big as you, but still big."
        gloria.c "Nobody's as big as me, but I understand her problem. I used to have a devil of a time finding a properly fitting bra in the stores. Even the highest end lingerie shops do a piss poor job of training their staff to fit their customers properly.  Don't know why it's so hard.  There should be plenty of budding college lesbians dying for a chance to handle boobs all day for retail wages."
        gloria.c "Anyway, the person you want to call is Brenda. She's the best bra fitter I've ever met. She's a little touchy feely, but what do you expect from a woman who picks a career working with breasts.  I just wish she'd cut her prices every time she cops a feel, but she's still worth it, even if she is expensive.  I'll send you her contact details."
        add tags 'discussed_bra_fitter' to gloria
        if chelsea.bra_fitting_status == 1:
            "Brenda the Bra Fitter. That should be easy to remember. And she's a lesbian to boot. Might be fun to send her [chelsea.name]'s way."
            $ chelsea.bra_fitting_status = 2
        else:
            "That's the same name you got previously. It seems Brenda the Bra Fitter's client list includes a lot of the town's wealthy and well-endowed clients."
    return

## Lawyer Content
label chelsea_janice_talk_option:
    if chelsea.has_tag('likes_girls') and janice.has_tag('asked_about_hiring') and not janice.has_tag('discuss_chubby_lesbian'):
        "You discuss [chelsea.name]'s newfound interest in other women with Janice."
        janice.c "Sorry. She doesn't sound like my type. Get back to me when you've found someone blonder."
        player.c "That's a strangely specific compulsion you have, you know?"
        add tags 'discuss_chubby_lesbian' to janice
        $ janice.temporary_count = 0
    return

## Marilyn Content
label chelsea_marilyn_talk_option:
    if chelsea.has_tag('likes_girls') and not marilyn.has_tag('discuss_chubby_lesbian'):
        "You discuss [chelsea.name]'s newfound interest in other women with Marilyn."
        marilyn.c "Close, but my staff will find me a more interesting bed warmer. Let me know when you've found a better, more fair skinned prospect."
        add tags 'discuss_chubby_lesbian' to marilyn
    return

## Loving Wife Content
label chelsea_sarah_positive_role_talk_girlfriend:
    if current_target.has_tag('girlfriend') and not sarah.has_tag(tag_expression):
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        "You ask [chelsea.name] to join you."
        chelsea.c "Hi!  What's up?  You normally want me out of the way when you're working with clients."
        wt_image lw_visit_2_2
        player.c "I'd like you to meet Sarah.  Sarah, this is my girlfriend [chelsea.name]."
        sarah.c "Hi.  Nice to meet you."
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        player.c "Sarah's husband wants her to have sex with his friends, but she has concerns.  I thought speaking to another woman could help her."
        chelsea.c "Sure!  So your husband wants you to get funky with his buddies.  Are they good looking?"
        wt_image lw_visit_2_12
        sarah.c "I guess so.  It's not just one or two guys, though.  I think he'd like me to sleep with any guy he brings over.  I feel like he wants to turn me into a slut, and I'm not sure how he'll feel about me afterwards."
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        chelsea.c "Yeah, guys can be funny.  They say they like women who like sex, but then some of them get jealous or start to look down at those who really do.  Is your boyfriend the jealous or controlling type?"
        wt_image lw_visit_2_12
        sarah.c "He doesn't seem to be, but what if that changes after he watches me have sex?"
        chelsea.c "Not everyone turns into a jealous freak.  My boyfriend has sex with other women all the time.  What does it matter, as long as he still spends time with me and treats me right?"
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        chelsea.c "If your guy wants you to have sex with his friends and then gets mad at you about it, well, he's a jerk and you're better off dumping him anyway.  If he doesn't get jealous, it sounds like you get the opportunity to fool around with some hotties.  He's not going to make you sleep with someone you don't want to, is he?"
        wt_image lw_visit_2_11
        sarah.c "I don't think so.  Right now I think he'd be happy if I slept with one or two."
        chelsea.c "So you could pick someone you find attractive, maybe somebody who likes to do sexy things your husband doesn't, and then he leaves and you don't need to worry about whether he's a total jerk outside of the bedroom?  And later you can snuggle up on the sofa with your hubbie and enjoy a movie and popcorn after Joe Fuckbuddy goes home.  That doesn't sound that bad."
        "The two of them get into a long conversation about casual sex and the importance of friendship inside a relationship and the differences between men and women."
        wt_image lw_visit_2_4
        "Eventually, it's time for Sarah to leave."
        sarah.c "Thanks for talking to me, [chelsea.name].  It helped a lot to get a woman's perspective."
        add tags 'met_girlfriend_chelsea' 'positive_girlfriend_resolution_today' to sarah
    elif current_target.has_tag('hypno_girlfriend') and not sarah.has_tag(tag_expression):
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        "You ask [chelsea.name] to join you."
        chelsea.c "Hi"
        wt_image lw_visit_2_2
        player.c "[chelsea.name], I'd like you to meet Sarah.  Sarah, this is my girlfriend [chelsea.name]."
        sarah.c "Hi.  Nice to meet you."
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        player.c "Sarah's husband wants her to have sex with his friends, but she has concerns.  I thought speaking to another woman could help her."
        chelsea.c "Okay.  I'll try."
        "In her hypnotized state, [chelsea.name] can't always relate or respond correctly to questions about Sarah's relationship.  Instead, she does her best to deliver the message she thinks you'd want her to give to Sarah about the importance of looking after her boyfriend's needs."
        wt_image lw_visit_2_2
        "Sarah listens, but finds it hard to relate to [chelsea.name]'s unquestioning approach to her relationship with you."
        ## remainder of hypno_girlfriend content is back in sarah's script
        add tags 'positive_girlfriend_resolution_today' 'met_girlfriend_chelsea' to sarah
    else:
        $ current_target = None
    return

label chelsea_sarah_positive_role_talk_slavegirl:
    if current_target.has_tag('slavegirl'):
        wt_image chubby_slave_18
        "You order [chelsea.full_name] to join you."
        chelsea.c "Yes, [chelsea.your_name]?"
        player.c "[chelsea.name], I'd like you to meet Sarah."
        wt_image lw_visit_2_2
        sarah.c "Hi.  Shouldn't you be dressed?"
        player.c "She doesn't need clothes to talk.  [chelsea.name], Sarah's husband wants her to have sex with his friends. She has concerns. I thought speaking to another woman could help her."
        wt_image chubby_slave_1
        chelsea.c "I'll try, [chelsea.your_name]."
        add tags 'positive_transformed_slavegirl_resolution_today' 'met_slavegirl_chelsea' to sarah
        ## remainder of transformed_slavegirl content is back in sarah's script
    else:
        $ current_target = None
    return

label chelsea_sarah_positive_role_sex_girlfriend:
    if current_target.has_tag('girlfriend') or current_target.has_tag('hypno_girlfriend'):
        player.c "[chelsea.name], could you join us for a moment?"
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        chelsea.c "Sure.  Hi, Sarah!"
        wt_image lw_visit_4_8
        sarah.c "Hi, [chelsea.name]."
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        player.c "[chelsea.name], I'd like you to help me help Sarah, again.  You know she's worried about having her husband watch her have sex."
        player.c "It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together.  I want to make love to you, while Sarah watches us."
        wt_image lw_visit_4_2
        sarah.c "Oh, no!  You don't have to do that, [chelsea.name].  I don't want to interfere with your love life."
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        chelsea.c "It's okay, Sarah. We're friends. If he thinks this could help you, I want to do it."
        wt_image lw_visit_4_6
        sarah.c "But I don't want to impose!"
        chelsea.c "If this could be good for your marriage, then I want to do it.  For you.  You've got a great guy, right?  And we should do whatever we can to help you keep him."
        wt_image lw_visit_4_3
        sarah.c "I guess. You really don't mind?"
        if chelsea.has_tag('toned'):
            wt_image chubby_lw_visit_toned_1
        else:
            wt_image chubby_hypno_weekend_1
        chelsea.c "For you, not at all. Just give me a moment to go freshen up."
        wt_image current_location.image
        "It takes a while, but eventually she rejoins you. She's more than just freshened up. It looks like she took a bath and changed into lingerie."
        wt_image chubby_lw_visit_2
        chelsea.c "Did I keep you waiting?"
        player.c "A little.  Come here."
        wt_image chubby_lw_visit_3
        chelsea.c "Oh dear!  Well, I guess I better make that up to you, huh?"
        player.c "I guess so."
        wt_image chubby_lw_visit_4
        chelsea.c "Maybe if I do this, you'll forgive me?"
        player.c "That's a nice start."
        wt_image lw_visit_4_6
        sarah.c "Maybe I should be going.  I don't want to disturb the two of you."
        wt_image chubby_lw_visit_5
        chelsea.c "It's okay, Sarah.  You being here isn't disturbing me.  I'm happy to help you."
        wt_image chubby_lw_visit_6
        chelsea.c "And she's certainly not disturbing you, is she [chelsea.your_name]?  Mmmmmmm."
        "[chelsea.name] kisses you, hard and passionately as she rubs your dick between her boobs."
        wt_image chubby_lw_visit_7
        "Eventually you break her kiss and roll her onto her back.  Spreading her legs, you lower your mouth onto her sex."
        chelsea.c "Aahhh"
        chelsea.c "ooohhhhh!"
        wt_image chubby_lw_visit_8
        chelsea.c "Ahhhhh  ...  I need you inside me!"
        wt_image chubby_lw_visit_9
        "You don't keep her waiting."
        chelsea.c "Yes!!  Just like that!"
        wt_image chubby_lw_visit_10
        "This time she doesn't keep you waiting, either. A few hard thrusts and she's over the edge."
        chelsea.c "Aahhhhhh!!!!"
        wt_image lw_visit_4_5
        sarah.c "You ... you were able to cum?  Even with me here?"
        wt_image chubby_lw_visit_18
        chelsea.c "Mmmm, did I ever! Give me a minute, Sarah.  Somebody's earned a reward."
        wt_image chubby_lw_visit_11
        "With her tits and tongue, [chelsea.name] returns the favour, bringing you to climax as thanks for the orgasm you just gave her."
        wt_image chubby_lw_visit_18
        player.c "[player.orgasm_text]"
        wt_image chubby_lw_visit_12
        chelsea.c "See?  He enjoyed it, too, even with you watching.  Heck, knowing him, he properly enjoyed it more knowing you were watching.  Anyway, hopefully I didn't look too silly in some of those positions?"
        wt_image lw_visit_4_9
        sarah.c "No, not at all.  You looked like you were having a lot of fun.  You both did.  I think you've made your point.  For some people, sex doesn't always have to be in private for it to be fun.  I need to go home and think about this."
        wt_image lw_visit_4_10
        "Sarah looks at you with more interest than she has before.  You can't help yourself from teasing her."
        player.c "You can take your panties off while you think about it, if you want."
        $ chelsea.sex_count += 1
        $ chelsea.orgasm_count += 1
        orgasm
        add tags 'watched_girlfriend_this_weekend' to sarah
    else:
        $ current_target = None
    return

label chelsea_sarah_positive_role_sex_slavegirl:
    if current_target.has_tag('slavegirl'):
        player.c "[chelsea.name], come here and join us."
        wt_image chubby_slave_18
        chelsea.c "Yes, [chelsea.your_name]."
        player.c "You remember Sarah?"
        wt_image chubby_slave_1
        chelsea.c "Yes, [chelsea.your_name]."
        player.c "You know Sarah's worried about having her husband watch her have sex. It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together."
        wt_image chubby_slave_17
        player.c "I'm going to fuck you, [chelsea.name], while Sarah watches us."
        chelsea.c "Yes, [chelsea.your_name]."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image chubby_lw_visit_13
        player.c "Let's get you prepared, [chelsea.name]."
        "You tie her hands and place a pair of panties in her mouth ..."
        wt_image chubby_lw_visit_14
        "... then you duct tape her mouth and secure her to a bench. She's warm and wet as you push into her, and you can just make out a groan through her gag as you enter her."
        chelsea.c "mmmmph"
        wt_image lw_visit_4_4
        sarah.c "Maybe I should go?  I don't want to be intruding on your personal time together."
        player.c "Nonsense.  [chelsea.name] doesn't mind you being here.  She's happy to service my cock anytime, regardless of whether anyone's watching.  Aren't you?"
        wt_image chubby_lw_visit_14
        chelsea.c "mmmpphh"
        player.c "I'm pretty sure that was a yes."
        wt_image chubby_lw_visit_15
        "In this position, [chelsea.name] can't do much more than take the fucking you give her, but she takes it very well, offering a wet and warm sheath for your dick as you thrust in and out of her."
        player.c "[player.orgasm_text]"
        chelsea.c "mmmmppphhhhh"
        wt_image lw_visit_4_5
        sarah.c "You've made your point.  Men can enjoy sex even when it's not in private. Some women, too, I guess ..."
        player.c "And did [chelsea.name] look ridiculous while I was fucking her?"
        wt_image lw_visit_4_8
        sarah.c "No.  No, I guess not.  I mean, the whole bondage thing is kinda weird."
        player.c "You should try it sometime."
        wt_image lw_visit_4_7
        sarah.c "I think I'll just go home and maybe think about this some more, later."
        player.c "Sure. And if your husband wants to borrow some of my equipment to use on you while you're thinking about it, just let me know."
        $ chelsea.sex_count += 1
        orgasm
        add tags 'watched_transformed_slavegirl_this_weekend' to sarah
    else:
        $ current_target = None
    return

## Store Content
label chelsea_es_store_enter:
    if chelsea.bra_fitting_status == 1 and not eros_store.chelsea_bra_message:
        "Looking around, you wonder briefly if [chelsea.name] could get a bra to fit her here. Then you realize everything they carry is off the shelf retail, the type of product [chelsea.name]'s been buying for herself."
        "And you can just tell that asking the store clerk to examine your girlfriend's boobs is not going to get you the response you want."
        $ eros_store.chelsea_bra_message = True
    return

label chelsea_es_store_exit:
    pass
    return


## Character Specific Timers
# Anal Fingering
label chelsea_anal_fingering:
    if chelsea.anal_fingering_count < 2:
        $ chelsea.anal_fingering_count += 1
        "[chelsea.name] finds the experience weird and uncomfortable, but she does it anyway, since this seems to be important to you. Still, she's not happy about it."
        sys "[chelsea.name] is less happy with your relationship."
        if chelsea.hypno_re_anal > 1:
            $ chelsea.relationship_counter -= 2
        else:
            $ chelsea.relationship_counter -= 3
    elif chelsea.anal_fingering_count == 2:
        $ chelsea.anal_fingering_count = 3
        "[chelsea.name]'s getting used to the feeling of her own finger in her ass, but she still doesn't like it. She does it anyway, since this seems to be important to you, but she's not happy about it."
        sys "[chelsea.name] is less happy with your relationship."
        if chelsea.hypno_re_anal > 1:
            $ chelsea.relationship_counter -= 1
        else:
            $ chelsea.relationship_counter -= 2
    elif chelsea.anal_fingering_count > 2:
        $ chelsea.anal_fingering_count = 4
        "[chelsea.name]'s finally getting, if not comfortable, then at least accepting of the feeling of her own finger in her ass. It's not something she'd do other than to please you, but it doesn't seem to bother her the way it used to."
        sys "She may be ready to take the next step in her anal training."
    return

# Girlfriend Events
label chelsea_girlfriend_event:
    $ chelsea.training_session()
    $ chelsea.gf_event += 1
    $ chelsea.temporary_count = 0
    if chelsea.gf_event > 13:
        $ chelsea.gf_event = 1
    # opens bra-fitting chain, else dildo event
    if chelsea.gf_event == 1:
        # bra-fitting
        if chelsea.bra_fitting_status == 0:
            call forced_movement(bedroom) from _call_forced_movement_249
            summon chelsea no_follows
            if chelsea.has_tag('bbw'):
                wt_image chubby_bra_1_2
            else:
                wt_image chubby_bra_1_1
            "You overhear [chelsea.name] muttering to herself as she dresses in the morning."
            chelsea.c "Ugghh. I hate my bras! I wish I could find some that fit me properly."
            "She can't be the only well-endowed woman who finds it hard to get properly fitting bras. I wonder what other women shaped like her do?"
            $ chelsea.bra_fitting_status = 1
            add tags 'something_to_discuss' to gloria
            add tags 'gloria_other_talk_option_possible' to chelsea
            call character_location_return(chelsea) from _call_character_location_return_80
            call forced_movement(living_room) from _call_forced_movement_250
            call character_location_return(chelsea) from _call_character_location_return_81
        # dildo scene
        else:
            if chelsea.has_item(dildo) and not chelsea.has_tag('no_dildo_shows'):
                $ chelsea.temporary_count = 1
                if chelsea.has_tag('little_girl'):
                  call forced_movement(bedroom) from _call_forced_movement_251
                  summon chelsea no_follows
                  wt_image chubby_dildo_1_youth_1
                  "[chelsea.name] is waiting for you, the dildo you bought her nestled in her bosom."
                  chelsea.c "Hey, I was thinking, [chelsea.your_name] ..."
                  wt_image chubby_dildo_1_youth_10
                  chelsea.c "... you bought this for me.  Did you want to see me use it?"
                  wt_image chubby_dildo_1_youth_2
                  "She takes the dildo out from between her breasts and, in what you assume is intended as a seductive gesture, sucks on it like it was a popsicle."
                  $ title = "What do you say?"
                  menu:
                    "Sure, that sounds like fun":
                      $ chelsea.training_session()
                      wt_image chubby_dildo_1_youth_3
                      "You find a comfortable seat and settle down to watch the show.  [chelsea.name] grins at you and removes her top ..."
                      wt_image chubby_dildo_1_youth_4
                      "... followed by her shorts."
                      wt_image chubby_dildo_1_youth_5
                      "Then she sinks to the floor and pops the toy back into her mouth."
                      wt_image chubby_dildo_1_youth_6
                      "When the dildo is sopping wet, she rolls onto her back and spreads her legs."
                      chelsea.c "I don't know if I'll be able to cum with you watching me, but I'll try."
                      wt_image chubby_dildo_1_youth_7
                      player.c "I have confidence in my little girl.  Put the toy in your pee-hole and make a sticky mess for me."
                      wt_image chubby_dildo_1_youth_11
                      "Slowly and gently she traces the head of the dildo around her sex. It takes a while, but eventually you can see and smell the signs of her budding arousal."
                      wt_image chubby_dildo_1_youth_8
                      "As her wetness increases, she thrusts the dildo inside her, further and deeper as her excitement grows.  Soon, you can sense her arousal not only by sight and smell, but by sound as well."
                      chelsea.c "Ahhhh"
                      wt_image chubby_dildo_1_youth_9
                      "After that, it takes only a few more strokes of the dildo for that arousal to peak."
                      chelsea.c "Ahhhhh  ...  Aahhhhhh"
                      wt_image chubby_dildo_1_youth_12
                      chelsea.c "Did I make a nice sticky mess for you, [chelsea.your_name]?"
                      player.c "The best.  I knew you could do it."
                      wt_image chubby_dildo_1_youth_13
                      "You kiss her gently, then go off to continue your day, leaving her to recover contentedly from her orgasm."
                      $ chelsea.masturbation_count += 1
                      $ chelsea.orgasm_count += 1
                      change player energy by -energy_very_short notify
                      call character_location_return(chelsea) from _call_character_location_return_82
                      call forced_movement(living_room) from _call_forced_movement_252
                    "Not today":
                      player.c "Not today, [chelsea.name]. Maybe some other time."
                      chelsea.c "Okay"
                      call character_location_return(chelsea) from _call_character_location_return_83
                      call forced_movement(living_room) from _call_forced_movement_253
                    "Never (shuts this event off)":
                      wt_image chubby_dildo_1_youth_1
                      player.c "I bought that for you to use in private, [chelsea.name]."
                      chelsea.c "Oh, okay.  I just thought you might like to ..."
                      player.c "I don't."
                      add tags 'no_dildo_shows' to chelsea
                      call character_location_return(chelsea) from _call_character_location_return_84
                      call forced_movement(living_room) from _call_forced_movement_254
                else:
                    if chelsea.has_tag('bbw'):
                        call forced_movement(living_room) from _call_forced_movement_255
                        summon chelsea no_follows
                        wt_image chubby_dildo_1_bbw_1
                        "A half naked [chelsea.name] is waiting for you."
                        chelsea.c "Hey, I was thinking, [chelsea.your_name] ..."
                        wt_image chubby_dildo_1_bbw_2
                        chelsea.c "... you bought this for me.  Did you want to see me use it?"
                        "She takes out the dildo you bought her and licks it seductively."
                        $ title = "What do you say?"
                        menu:
                            "Sure, that sounds like fun":
                                $ chelsea.training_session()
                                wt_image chubby_dildo_1_bbw_3
                                "You find a comfortable seat and settle down to watch the show.  [chelsea.name] rubs the head of the dildo against her nipple ..."
                                wt_image chubby_dildo_1_bbw_4
                                "... then spreads her legs and warms up her sex with gentle teasing caresses from her fingers."
                                wt_image chubby_dildo_1_bbw_7
                                chelsea.c "I don't know if I'll be able to cum with you watching me, but I'll try."
                                menu:
                                    "Tell her to put the dildo in and try":
                                        wt_image chubby_dildo_1_bbw_5
                                        player.c "I have confidence in you.  Put it and fuck yourself with it."
                                        "It takes a while, but eventually you can see and smell the signs of her budding arousal.  She dips the head of the dildo inside her, further and deeper as her excitement grows.  Soon, you can sense her arousal not only by sight and smell, but by sound as well."
                                        chelsea.c "Ahhhh"
                                        wt_image chubby_dildo_1_bbw_6
                                        "After that, it takes only a few more strokes of the dildo for that arousal to peak."
                                        chelsea.c "Ahhhhh  ...  Aahhhhhh"
                                        wt_image chubby_dildo_1_bbw_8
                                        player.c "I knew you could do it.  Thanks for the show."
                                        "You kiss her gently as she slumps to the floor after her orgasm.  Then you go off to continue your day, leaving her to recover contentedly."
                                    "Tell her to turn around and toy herself":
                                        wt_image chubby_dildo_1_bbw_10
                                        player.c "I have confidence in you.  Turn around and let me look at your sexy ass while you fuck yourself."
                                        "Excited by the confirmation that you're enjoying this, you can see and smell the signs of [chelsea.name]'s budding arousal.  She thrusts the head of the dildo inside her, further and deeper as her excitement grows.  Soon, you can sense her arousal not only by sight and smell, but by sound as well."
                                        wt_image chubby_dildo_1_bbw_
                                        "After that, it takes only a few more strokes of the dildo for that arousal to peak."
                                        chelsea.c "Ahhhhh  ...  Aahhhhhh"
                                        wt_image chubby_dildo_1_bbw_9
                                        player.c "I knew you could do it.  Thanks for the show."
                                        "You kiss her gently as she grins.  Then you go off to continue your day, leaving her to recover contentedly from her orgasm."
                                $ chelsea.masturbation_count += 1
                                $ chelsea.orgasm_count += 1
                                change player energy by -energy_very_short notify
                                call character_location_return(chelsea) from _call_character_location_return_85
                                call forced_movement(living_room) from _call_forced_movement_256
                            "Not today":
                                player.c "Not today, [chelsea.name]. Maybe some other time."
                                chelsea.c "Okay"
                                call character_location_return(chelsea) from _call_character_location_return_86
                                call forced_movement(living_room) from _call_forced_movement_257
                            "Never (shuts this event off)":
                                wt_image chubby_dildo_1_bbw_1
                                player.c "I bought that for you to use in private, [chelsea.name]."
                                chelsea.c "Oh. Okay. I just thought you might like to ..."
                                player.c "I don't."
                                add tags 'no_dildo_shows' to chelsea
                                call character_location_return(chelsea) from _call_character_location_return_87
                                call forced_movement(living_room) from _call_forced_movement_258
                    else:
                        call forced_movement(bedroom) from _call_forced_movement_259
                        summon chelsea no_follows
                        wt_image chubby_dildo_1_toned_1
                        "A half naked [chelsea.name] is waiting for you."
                        chelsea.c "Hey, I was thinking, [chelsea.your_name] ..."
                        wt_image chubby_dildo_1_toned_2
                        chelsea.c "... you bought this for me.  Did you want to see me use it?"
                        "She takes out the dildo you bought her and licks it seductively."
                        $ title = "What do you say?"
                        menu:
                            "Sure, that sounds like fun":
                                $ chelsea.training_session()
                                wt_image chubby_dildo_1_toned_3
                                "You find a comfortable seat and settle down to watch the show.  [chelsea.name] swirls her tongue around the head of the dildo ..."
                                wt_image chubby_dildo_1_toned_4
                                "... then pops it in her mouth for a quick faux blow job to get it sloppy wet."
                                wt_image chubby_dildo_1_toned_5
                                chelsea.c "I don't know if I'll be able to cum with you watching me, but I'll try."
                                wt_image chubby_dildo_1_toned_9
                                player.c "I have confidence in you.  Let me see you fuck your sexy pussy."
                                wt_image chubby_dildo_1_toned_6
                                "Slowly and gently she traces the head of the dildo around her sex.  It takes a while, but eventually you can see and smell the signs of her budding arousal."
                                wt_image chubby_dildo_1_toned_7
                                "As her wetness increases, she starts dipping the head of the dildo inside her, further and deeper as her excitement grows.  Soon, you can sense her arousal not only by sight and smell, but by sound as well."
                                chelsea.c "Ahhhh"
                                wt_image chubby_dildo_1_toned_8
                                "After that, it takes only a few more strokes of the dildo for that arousal to peak."
                                chelsea.c "Ahhhhh  ...  Aahhhhhh"
                                wt_image chubby_dildo_1_toned_9
                                player.c "I knew you could do it.  Thanks for the show."
                                wt_image chubby_dildo_1_toned_10
                                "You kiss her gently, then go off to continue your day, leaving her to recover contentedly."
                                $ chelsea.blowjob_count += 1
                                $ chelsea.masturbation_count += 1
                                $ chelsea.orgasm_count += 1
                                change player energy by -energy_very_short notify
                                call character_location_return(chelsea) from _call_character_location_return_88
                                call forced_movement(living_room) from _call_forced_movement_260
                            "Not today":
                                player.c "Not today, [chelsea.name],  Maybe some other time."
                                chelsea.c "Okay"
                            "Never (shuts this event off)":
                                wt_image chubby_dildo_1_toned_1
                                player.c "I bought that for you to use in private, [chelsea.name]."
                                chelsea.c "Oh.  Okay.  I just thought you might like to..."
                                player.c "I don't."
                                add tags 'no_dildo_shows' to chelsea
                        call forced_movement(living_room) from _call_forced_movement_261
                    call character_location_return(chelsea) from _call_character_location_return_89
            else:
                jump chelsea_girlfriend_event
    # opens youth chain
    elif chelsea.gf_event == 2:
        if chelsea.youth_status == 0:
          call forced_movement(living_room) from _call_forced_movement_262
          summon chelsea no_follows
          if chelsea.has_tag('bbw'):
            wt_image chubby_youth_bbw_1_5
            chelsea.c "Oops, you caught me wearing this old thing."
            wt_image chubby_youth_bbw_1_1
            chelsea.c "I've had this outfit since I was a schoolgirl.  It's silly, me wearing it now when I'm a grown woman."
          else:
            wt_image chubby_youth_toned_1_5
            chelsea.c "Oops, you caught me wearing this old thing."
            wt_image chubby_youth_toned_1_1
            chelsea.c "I've had this outfit since I was a schoolgirl.  It's silly, me wearing it now when I'm a grown woman."
            wt_image chubby_youth_toned_1_6
          $ title = "What do you say?"
          menu:
            "It looks good on you":
              if chelsea.has_tag('bbw'):
                wt_image chubby_youth_bbw_1_2
              else:
                wt_image chubby_youth_toned_1_2
              chelsea.c "Really?  Thanks!  Check out the panties ... they're so girly!!  Sometimes it's fun to dress up like a schoolgirl."
              if chelsea.has_tag('bbw'):
                pass
              else:
                wt_image chubby_youth_toned_1_7
              sys "[chelsea.name] is happier with your relationship."
              $ chelsea.relationship_counter += 1
              $ chelsea.youth_status = 1
              call character_location_return(chelsea) from _call_character_location_return_90
            "Wear whatever you want":
              if chelsea.has_tag('bbw'):
                wt_image chubby_youth_bbw_1_3
              else:
                wt_image chubby_youth_toned_1_8
              player.c "Wear whatever you want, [chelsea.name]. I'm not the fashion police. It doesn't matter to me how you dress."
              if chelsea.has_tag('bbw'):
                pass
              else:
                wt_image chubby_youth_toned_1_3
              "She looks as if she's going to say something, then thinks better of it.  You suspect this isn't the last time her choice of clothing is going to come up."
              call character_location_return(chelsea) from _call_character_location_return_91
            "Yes, it is silly":
              if chelsea.has_tag('bbw'):
                wt_image chubby_youth_bbw_1_4
              else:
                wt_image chubby_youth_toned_1_4
              player.c "Yes, it is silly. Wear something appropriate for your age."
              if chelsea.has_tag('bbw'):
                pass
              else:
                wt_image chubby_youth_toned_1_9
              chelsea.c "Okay, you're right.  I'll go get changed."
              "That should put an end to that nonsense."
              $ chelsea.youth_status = 5
              call character_location_return(chelsea) from _call_character_location_return_92
        else:
          # pool events
          call forced_movement(backyard) from _call_forced_movement_263
          summon chelsea no_follows
          if chelsea.has_tag('little_girl'):
            wt_image chubby_gf_pool_1_youth_1
            "A naked [chelsea.name] passes you on her way to the pool."
            $ title = "Join her?"
            menu:
              "Yes, spend time with her":
                $ chelsea.training_session()
                wt_image chubby_gf_pool_1_youth_3
                chelsea.c "Hi!  I was just about to play in the pool."
                wt_image chubby_gf_pool_1_youth_9
                player.c "Dressed like that?"
                wt_image chubby_gf_pool_1_youth_4
                chelsea.c "Umm, aren't little girls allowed to play naked in a splash pool?  Are you going to watch me and keep me safe?"
                wt_image chubby_gf_pool_1_youth_5
                "You find a comfortable place to sit and watch your little girl splash around beside the pool ..."
                wt_image chubby_gf_pool_1_youth_2
                "... and in the pool."
                wt_image chubby_gf_pool_1_youth_6
                "Eventually it seems she's done, and she crawls out of the water."
                wt_image chubby_gf_pool_1_youth_7
                player.c "Don't run near the pool.  You could slip and hurt yourself."
                chelsea.c "Sorry, [chelsea.your_name].  Thanks for watching over me and keeping me safe!"
                wt_image chubby_gf_pool_1_youth_8
                "[chelsea.name] enjoyed spending time with you like this, but play time is over.  Time to get on with your day."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
                change player energy by -energy_very_short notify
              "Not today":
                wt_image chubby_gf_pool_1_youth_2
                "You have things you want to get done today, so you leave her alone to play in the pool by herself."
          else:
            if chelsea.has_tag('bbw'):
                wt_image chubby_gf_pool_1_bbw_10
                chelsea.c "Hey, want to join me for some sun by the pool?"
                wt_image chubby_gf_pool_1_bbw_11
                $ title = "Join her?"
                menu:
                    "Yes, spend time with her":
                        $ chelsea.training_session()
                        wt_image chubby_gf_pool_1_bbw_2
                        chelsea.c "Great!  I'll just let these out, so they can get a little sun, too."
                        wt_image chubby_gf_pool_1_bbw_13
                        chelsea.c "Shit.  I seem to have a lot of me hanging out.  Maybe I shouldn't be prancing around in a bikini in my current shape?"
                        player.c "Your shape is great, [chelsea.name]."
                        wt_image chubby_gf_pool_1_bbw_3
                        chelsea.c "It is?  Thank you.  I'm so glad you think so."
                        wt_image chubby_gf_pool_1_bbw_4
                        $ title = "How do you want to chat with her?"
                        menu:
                            "Like this":
                                wt_image chubby_gf_pool_1_bbw_5
                                "[chelsea.name] lies back and tans while the two of you talk."
                            "Fully naked":
                                wt_image chubby_gf_pool_1_bbw_16
                                "[chelsea.name] watches in amusement as you strip out of your clothes."
                                chelsea.c "Oh, are we going nudist today?"
                                wt_image chubby_gf_pool_1_bbw_17
                                player.c "You're the one who said we should hang out."
                                wt_image chubby_gf_pool_1_bbw_6
                                chelsea.c "I didn't mean literally, but okay."
                                wt_image chubby_gf_pool_1_bbw_7
                                "She strips out of her bathing suit and joins you au naturel."
                                wt_image chubby_gf_pool_1_bbw_9
                                "Then she lies back down and the two of you talk."
                        wt_image chubby_gf_pool_1_bbw_14
                        "It's not long before you have her laughing.   She thoroughly enjoys spending time with you like this.  The two of you pass a pleasant hour together, then go on with your days."
                        wt_image chubby_gf_pool_1_bbw_15
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        change player energy by -energy_very_short notify
                    "Not today":
                        wt_image chubby_gf_pool_1_bbw_1
                        player.c "Not today.  I have some things I need to get done."
                        wt_image chubby_gf_pool_1_bbw_12
                        chelsea.c "Okay.  See you later!"
            else:
                wt_image chubby_gf_pool_1_toned_1
                chelsea.c "Hey, I'm about to go for a swim.  Want to join me?"
                wt_image chubby_gf_pool_1_toned_10
                $ title = "Join her?"
                menu:
                    "Yes, spend time with her":
                        $ chelsea.training_session()
                        wt_image chubby_gf_pool_1_toned_2
                        "Well, don't just stand there.  I'm not going to laze around the poolside all day.  Let's swim!"
                        player.c "You swim.  I'll watch."
                        wt_image chubby_gf_pool_1_toned_12
                        "You watch her swim laps.  When she finally finishes, she's out of breath, but happy looking."
                        wt_image chubby_gf_pool_1_toned_4
                        chelsea.c "That was fun.  Time to get a little sun and dry off.  I'll just let these out, so they can get a little sun, too."
                        $ title = "How do you want to chat with her?"
                        menu:
                            "Like this":
                                wt_image chubby_gf_pool_1_toned_5
                                "[chelsea.name] lies down beside you and the two of you talk."
                                wt_image chubby_gf_pool_1_toned_6
                                "It's not long before you have her laughing.   She thoroughly enjoys spending time with you like this.  The two of you pass a pleasant hour together, then go on with your days."
                            "Naked":
                                wt_image chubby_gf_pool_1_toned_3
                                "[chelsea.name] watches in amusement as you strip out of your clothes."
                                wt_image chubby_gf_pool_1_toned_13
                                chelsea.c "Oh, are we going nudist today?"
                                player.c "You're the one who said we should hang out."
                                wt_image chubby_gf_pool_1_toned_7
                                chelsea.c "I didn't mean literally, but okay."
                                wt_image chubby_gf_pool_1_toned_9
                                "[chelsea.name] sits down beside you and the two of you talk.  It's not long before you have her laughing.   She thoroughly enjoys spending time with you like this.  The two of you pass a pleasant hour together, then go on with your days."
                                wt_image chubby_gf_pool_1_toned_8
                        sys "[chelsea.name] is happier with your relationship."
                        $ chelsea.relationship_counter += 0.5
                        change player energy by -energy_very_short notify
                    "Not today":
                        wt_image chubby_gf_pool_1_toned_11
                        chelsea.c "Okay.  See you later!"
          call forced_movement(living_room) from _call_forced_movement_264
        call character_location_return(chelsea) from _call_character_location_return_93
    # early morning event
    elif chelsea.gf_event == 3:
        call forced_movement(bedroom) from _call_forced_movement_265
        summon chelsea no_follows
        # opens anal events
        if chelsea.anal_status == 0:
          wt_image chubby_gf_event_3_1
          "[chelsea.name] wakes you early in the morning."
          chelsea.c "Hey, I woke up horny.  Let's fuck."
          $ title = "What do you do?"
          menu:
            "Have sex with her":
              $ chelsea.training_session()
              wt_image chubby_gf_event_3_2
              "There are worse ways to start your day than having [chelsea.name] settle herself onto your morning wood ..."
              wt_image chubby_gf_event_3_12
              "... especially as it gives you a great view of her ass and rosebud."
              wt_image chubby_gf_event_3_3
              $ title = "Suggest anal?"
              menu:
                "Tell her you want to try anal":
                  wt_image chubby_gf_event_3_13
                  player.c "We should try anal sometime, [chelsea.name]."
                  wt_image chubby_gf_event_3_14
                  chelsea.c "What?  No, that's gross."
                  wt_image chubby_gf_event_3_12
                  "Seems you're going to have to do some work if you want her to 'open up' to this idea.  Putting something smaller than your cock in her ass might be a good first step."
                  wt_image chubby_gf_event_3_15
                  "In the meantime, you have the consolation of enjoying the feeling of [chelsea.name]'s wet, warm pussy sliding up and down your cock, faster and faster ..."
                  $ chelsea.anal_status = 2
                "You're not interested in her asshole, today":
                  wt_image chubby_gf_event_3_4
                  "As good as her pussy feels, you've no interest in plowing her rear hole today."
                  wt_image chubby_gf_event_3_15
                  "Up and down she rides on your cock, faster and faster ..."
                "You're not interested in her asshole, ever (shuts off event)":
                  wt_image chubby_gf_event_3_4
                  "As good as her pussy feels, you've no need to ever plow her rear hole."
                  wt_image chubby_gf_event_3_15
                  "Up and down she rides on your cock, faster and faster ..."
                  $ chelsea.anal_status = 1
              wt_image chubby_gf_event_3_16
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_3_17
              "... until she rides you both to climax."
              wt_image chubby_gf_event_3_5
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_3_16
              player.c "[player.orgasm_text]"
              $ chelsea.sex_count += 1
              $ chelsea.orgasm_count += 1
              orgasm notify
            "Go back to sleep":
              wt_image chubby_gf_event_3_18
              "You ignore her and roll over to face the other way, trying to get a few minutes more sleep."
              chelsea.c "Oh come on! Fine, I'll go get ready for work. I'll probably play with myself when I get to my desk. Try to sleep while you think about that."
        # morning sex
        else:
          wt_image chubby_gf_event_3_1
          "[chelsea.name] wakes you early in the morning."
          chelsea.c "Good morning!  I was just about to head to work when I noticed your, um ... morning erection.  Would you like me to do something about that before I leave?"
          $ title = "What do you tell her?"
          menu:
            "That'd be great":
              $ chelsea.training_session()
              wt_image chubby_gf_event_3_20
              player.c "That'd be great, [chelsea.name]"
              wt_image chubby_gf_event_3_6
              chelsea.c "I thought your not-so-little guy might like some attention."
              $ title = "What type of attention do you want?"
              menu:
                "Her hand is great":
                  wt_image chubby_gf_event_3_7
                  "She proceeds to give your cock plenty of manual attention, running her soft hand up and down your shaft ..."
                  wt_image chubby_gf_event_3_21
                  "... faster and faster..."
                  wt_image chubby_gf_event_3_22
                  "... until you surprise her, cumming quicker than she expected and shooting your jizz up and over her hand and face."
                  player.c "[player.orgasm_text]"
                  wt_image chubby_gf_event_3_8
                  chelsea.c "Oh!!"
                  if chelsea.has_tag('little_girl'):
                    wt_image chubby_gf_event_3_11
                    chelsea.c "Did your little girl do a good job of helping with your morning wood?"
                    player.c "You did great, [chelsea.name]."
                  else:
                    if chelsea.has_tag('bbw'):
                      wt_image chubby_gf_event_3_10
                      chelsea.c "Mmmm.  Tasty.  Not enough to tide me over to lunch, though.  I'm going to go get some breakfast."
                    else:
                      wt_image chubby_gf_event_3_9
                      chelsea.c "My workouts must be paying off.  Who knew my hands were strong enough to pump that much cum out of you that quickly?"
                  $ chelsea.handjob_count += 1
                  $ chelsea.facial_count += 1
                "Her mouth":
                  wt_image chubby_gf_event_3_23
                  "[chelsea.name] gives your cock a long lick."
                  wt_image chubby_gf_event_3_24
                  "Then she swirls her tongue around the head of your cock ..."
                  wt_image chubby_gf_event_3_25
                  "... before taking you into her mouth."
                  wt_image chubby_gf_event_3_26
                  "What follows is a quick but loving blow job ..."
                  wt_image chubby_gf_event_3_27
                  "... that soon has you ready to cum."
                  wt_image chubby_gf_event_3_28
                  $ title = "Where do you want to cum?"
                  menu:
                    "In her":
                      wt_image chubby_gf_event_3_29
                      player.c "[player.orgasm_text]"
                      if chelsea.has_tag('little_girl'):
                        wt_image chubby_gf_event_3_30
                        chelsea.c "Did your little girl do a good job of helping with your morning wood?"
                        player.c "You did great, [chelsea.name]."
                      else:
                        wt_image chubby_gf_event_3_31
                        if chelsea.has_tag('bbw'):
                          chelsea.c "Mmmm.  Tasty.  Not enough to tide me over to lunch, though.  I'm going to go get some breakfast."
                        else:
                          chelsea.c "Mmmm.  Protein.  The perfect pre-workout meal before I hit the gym during my lunch hour today."
                      $ chelsea.swallow_count += 1
                    "On her":
                      wt_image chubby_gf_event_3_32
                      player.c "[player.orgasm_text]"
                      wt_image chubby_gf_event_3_33
                      chelsea.c "Hey!  I was on my way to work, remember?  Now I have to get cleaned up again."
                      "The giggle in her voice as she leaves tells you she's not really mad"
                      $ chelsea.facial_count += 1
                  $ chelsea.blowjob_count += 1
                "Her pussy":
                  wt_image chubby_gf_event_3_21
                  player.c "You have time for a quickie, right?"
                  chelsea.c "Not really, but I guess this'll be a challenge to see how quick of a quickie it'll take for me to get you off."
                  wt_image chubby_gf_event_3_34
                  $ title = "Try and get her off quick, too?"
                  menu:
                    "Yes":
                      wt_image chubby_gf_event_3_35
                      "She normally turns around when she wants to cum ..."
                      wt_image chubby_gf_event_3_38
                      "... but the way she's leaning backwards as she rides you today lets you take matters into your hands ..."
                      wt_image chubby_gf_event_3_39
                      "... and stimulate an orgasm in her even when she's not expecting one."
                      chelsea.c "Ahhhhh"
                      wt_image chubby_gf_event_3_40
                      chelsea.c "Aahhhhhh"
                      player.c "[player.orgasm_text]"
                      wt_image chubby_gf_event_3_37
                      chelsea.c "Hey, we were both pretty quick!  That was fun, but I'd better get to work, now."
                      sys "[chelsea.name] is happier with your relationship."
                      $ chelsea.orgasm_count += 1
                      $ chelsea.relationship_counter += 0.5  # bonus for unexpected orgasm
                    "No":
                      wt_image chubby_gf_event_3_35
                      "[chelsea.name] rides your cock up-and-down ..."
                      wt_image chubby_gf_event_3_34
                      "... until her soft, warm pussy succeeds at milking an orgasm out of you."
                      wt_image chubby_gf_event_3_36
                      player.c "[player.orgasm_text]"
                      wt_image chubby_gf_event_3_37
                      if chelsea.has_tag('little_girl'):
                        chelsea.c "Hey, that was quick!  Did your little girl do a good job of helping with your morning wood?"
                        player.c "You did great, [chelsea.name]."
                      else:
                        wt_image chubby_gf_event_3_31
                        if chelsea.has_tag('bbw'):
                          chelsea.c "Hey, that was quick!  I worked up an appetite, though.  I'm going to go get some breakfast."
                        else:
                          chelsea.c "Hey, that was quick!  And a good exercise, too.  I won't need to work my legs at the gym, today."
                  $ chelsea.sex_count += 1
              orgasm notify
            "I just want some sleep":
              wt_image chubby_gf_event_3_19
              chelsea.c "Suit yourself, sleepy head."
        call forced_movement(living_room) from _call_forced_movement_266
        call character_location_return(chelsea) from _call_character_location_return_94
    # youth event
    elif chelsea.gf_event == 4:
        if chelsea.youth_status == 1 or chelsea.youth_status > 5:
          if chelsea.has_tag('bbw'):
            call forced_movement(living_room) from _call_forced_movement_267 #This isn't really needed as the event that follows for bbw chelsea happens in your living room and you are already in your living room, but I put this here as a precaution.
            summon chelsea no_follows
            wt_image chubby_youth_bbw_2_1
          else:
            call forced_movement(bedroom) from _call_forced_movement_268 #The text, images, and scene that follows is in your bedroom. This is put in place to make sure it happens in your bedroom.
            summon chelsea no_follows
            wt_image chubby_youth_toned_2_1
          "[chelsea.name] takes a seat in front of you, a mischievous look on her face."
          chelsea.c "Hey [chelsea.your_name], how do you like my pigtails?  I used to wear my hair like this all the time when I was a girl.  What do you think?"
          $ title = "What do you say?"
          menu:
            "It's hot":
              $ chelsea.relationship_counter += 1
              if chelsea.has_tag('bbw'):
                wt_image chubby_youth_bbw_2_3
              else:
                wt_image chubby_youth_toned_2_3
              chelsea.c "Really?  You think I look hot with my hair done up like a little girl?  You're naughty aren't you?  Is there anything you want this little girl to do for you?"
              $ title = "What do you tell her?"
              menu:
                "Show me what you can do":
                  player.c "I don't know.  What does a little girl like you know about looking after a man?"
                  chelsea.c "Oh, I know a few things.  I may look sweet and innocent, but I can do some things that would make you happy."
                  player.c "Okay, show me what you can do."
                  if chelsea.has_tag('bbw'):
                    wt_image chubby_youth_bbw_2_4
                    chelsea.c "I know I can make your thingie feel good by touching it."
                    player.c "You think so?  Come show me."
                    wt_image chubby_youth_bbw_2_5
                    chelsea.c "See?  All I have to do is run my fingers along it and rub your balls, and your thingie gets all stiff."
                    wt_image chubby_youth_bbw_2_6
                    chelsea.c "It's so stiff now I can't even push it down."
                    player.c "Do you know what you need to do to make it soft again?"
                    wt_image chubby_youth_bbw_2_7
                    chelsea.c "Maybe something like this?"
                    "Wrapping her soft hand around your shaft, she starts pumping you, up-and-down, slowly at first then gradually faster and faster."
                    player.c "Do you know what's going to happen if you keep doing that, little girl?"
                    wt_image chubby_youth_bbw_2_8
                    chelsea.c "I think so.  I think I'm going to make you feel happy."
                    player.c "Watch closely as I show you how happy."
                    wt_image chubby_youth_bbw_2_9
                    player.c "[player.orgasm_text]"
                    wt_image chubby_youth_bbw_2_10
                    chelsea.c "That was a lot of happiness.  I think you like this little girl."
                    $ chelsea.handjob_count += 1
                    $ chelsea.facial_count += 1
                  else:
                    wt_image chubby_youth_toned_2_4
                    chelsea.c "I know how to make your thingie hard.  I mean, even harder than it is now.  All I have to do is lick it."
                    wt_image chubby_youth_toned_2_5
                    chelsea.c "And I can put it in my mouth, and then it gets even harder."
                    wt_image chubby_youth_toned_2_6
                    player.c "Can you put the whole thing in your mouth?"
                    chelsea.c "mm hmm"
                    wt_image chubby_youth_toned_2_7
                    "When her nose touches your belly, she looks up at you."
                    player.c "Almost there.  If you really want to make a man feel good, you need to take all of him into your mouth."
                    wt_image chubby_youth_toned_2_8
                    "It takes some effort, but [chelsea.name] eventually gets your cockhead far enough down the back of her throat to fit your whole shaft into her mouth, her face pressed up against your stomach."
                    player.c "Good girl.  Now stay like that for a moment."
                    wt_image chubby_youth_toned_2_9
                    "The sensation of having your cock fully surrounded by her mouth, your cock head buried tightly in the back of her throat, is enough all by itself to take you over the edge."
                    player.c "[player.orgasm_text]"
                    wt_image chubby_youth_toned_2_10
                    player.c "Very good, little girl.  You did make me happy by taking my whole cock into your mouth."
                    chelsea.c "And I swallowed all of your happiness, too.  Not that I had any choice, the way your thingie was buried inside me."
                    $ chelsea.blowjob_count += 1
                    $ chelsea.swallow_count += 1
                  $ chelsea.visit_count += 1
                  $ chelsea.youth_status += 1
                  orgasm notify
                  $ chelsea.training_session()
                "That's not what I meant":
                  player.c "That's not what I meant, [chelsea.name].  I just meant you look really good, in this hair style or however you want to wear you're hair."
                  if chelsea.has_tag('bbw'):
                    wt_image chubby_youth_bbw_2_12
                  else:
                    wt_image chubby_youth_toned_2_13
                  chelsea.c "Ahh, you're sweet!  So is there something I can do for you?"
                  $ title = "What do you want?"
                  menu:
                    "You could help me with this":
                      if chelsea.has_tag('bbw'):
                        wt_image chubby_youth_bbw_2_4
                        "As you take out your cock, [chelsea.name] crawls over to you ..."
                        wt_image chubby_youth_bbw_2_5
                        "... and starts running her fingers along your shaft while she cups and plays with your balls with the other hand."
                        wt_image chubby_youth_bbw_2_6
                        "When you're fully hard ..."
                        wt_image chubby_youth_bbw_2_7
                        "... she wraps her soft hand around your shaft and starts pumping you, up-and-down, slowly at first ..."
                        wt_image chubby_youth_bbw_2_8
                        "... then gradually faster and faster."
                        wt_image chubby_youth_bbw_2_9
                        player.c "[player.orgasm_text]"
                        wt_image chubby_youth_bbw_2_11
                        chelsea.c "You liked that."
                        "It's an unnecessary observation, as the proof of it is all over her face."
                        $ chelsea.handjob_count += 1
                        $ chelsea.facial_count += 1
                      else:
                        wt_image chubby_youth_toned_2_4
                        "As you take out your cock, [chelsea.name] leans over and runs her tongue along the underside of your shaft."
                        chelsea.c "How would I do that? By licking it?"
                        player.c "That's nice, but I'd rather you put it in your mouth."
                        wt_image chubby_youth_toned_2_5
                        chelsea.c "Like this?"
                        "She takes the hard of your cock between her lips."
                        player.c "Deeper"
                        wt_image chubby_youth_toned_2_6
                        "She slides her wet lips forward, taking more of your cock inside her."
                        player.c "Deeper still."
                        wt_image chubby_youth_toned_2_7
                        "She pauses to control her gag reflex, then works more of you into her mouth. When her nose touches your belly, she looks up at you."
                        player.c "Almost there. Take everything."
                        wt_image chubby_youth_toned_2_8
                        "It requires some effort, but [chelsea.name] eventually gets your cockhead far enough down the back of her throat to fit your whole shaft into her mouth, her face pressed up against your stomach."
                        player.c "Good girl. Now stay like that for a moment."
                        wt_image chubby_youth_toned_2_9
                        "The sensation of having your cock fully surrounded by her mouth, your cock head buried tightly in the back of her throat, is enough all by itself to take you over the edge."
                        player.c "[player.orgasm_text]"
                        wt_image chubby_youth_toned_2_11
                        chelsea.c "Well if you ever want to make sure a girl swallows, shoving your cock that far down her throat sure forces the issue."
                        $ chelsea.blowjob_count += 1
                        $ chelsea.swallow_count += 1
                      orgasm notify
                      $ chelsea.training_session()
                    "Nothing right now":
                      player.c "I'm good right now, [chelsea.name]."
                      chelsea.c "Okay. Maybe another time."
                "Not right now":
                  player.c "Not right now."
                  if chelsea.has_tag('bbw'):
                    wt_image chubby_youth_bbw_2_12
                  else:
                    wt_image chubby_youth_toned_2_13
                  chelsea.c "Okay.  Maybe another time."
                  $ chelsea.youth_status += 1
              sys "[chelsea.name] is happier with your relationship."
            "I don't care about your hair":
              player.c "I don't care what your hair looks like, [chelsea.name].  I'm more interested in what you can do with your other body parts."
              chelsea.c "Oh, yeah?  Like what?  Like my mouth, maybe?"
              $ title = "What do you want?"
              menu:
                "A blowjob would be nice":
                  if chelsea.has_tag('bbw'):
                    player.c "You could help me with this."
                    wt_image chubby_youth_bbw_2_4
                    "As you take out your cock, [chelsea.name] crawls over to you ..."
                    wt_image chubby_youth_bbw_2_5
                    "... and starts running her fingers along your shaft while she cups and plays with your balls with the other hand."
                    wt_image chubby_youth_bbw_2_6
                    "When you're fully hard ..."
                    wt_image chubby_youth_bbw_2_7
                    "... she wraps her soft hand around your shaft and starts pumping you, up-and-down, slowly at first ..."
                    wt_image chubby_youth_bbw_2_8
                    "... then gradually faster and faster."
                    wt_image chubby_youth_bbw_2_9
                    player.c "[player.orgasm_text]"
                    wt_image chubby_youth_bbw_2_11
                    chelsea.c "You liked that."
                    "It's an unnecessary observation, as the proof of it is all over her face."
                    $ chelsea.handjob_count += 1
                    $ chelsea.facial_count += 1
                  else:
                    player.c "You could help me with this."
                    wt_image chubby_youth_toned_2_4
                    "As you take out your cock, [chelsea.name] leans over and runs her tongue along the underside of your shaft."
                    chelsea.c "How would I do that? By licking it?"
                    player.c "That's nice, but I'd rather you put it in your mouth."
                    wt_image chubby_youth_toned_2_5
                    chelsea.c "Like this?"
                    "She takes the hard of your cock between her lips."
                    player.c "Deeper"
                    wt_image chubby_youth_toned_2_6
                    "She slides her wet lips forward, taking more of your cock inside her."
                    player.c "Deeper still."
                    wt_image chubby_youth_toned_2_7
                    "She pauses to control her gag reflex, then works more of you into her mouth. When her nose touches your belly, she looks up at you."
                    player.c "Almost there. Take everything."
                    wt_image chubby_youth_toned_2_8
                    "It requires some effort, but [chelsea.name] eventually gets your cockhead far enough down the back of her throat to fit your whole shaft into her mouth, her face pressed up against your stomach."
                    player.c "Good girl. Now stay like that for a moment."
                    wt_image chubby_youth_toned_2_9
                    "The sensation of having your cock fully surrounded by her mouth, your cock head buried tightly in the back of her throat, is enough all by itself to take you over the edge."
                    player.c "[player.orgasm_text]"
                    wt_image chubby_youth_toned_2_11
                    chelsea.c "Well if you ever want to make sure a girl swallows, shoving your cock that far down her throat sure forces the issue."
                    $ chelsea.blowjob_count += 1
                    $ chelsea.swallow_count += 1
                  orgasm notify
                  $ chelsea.training_session()
                "Nothing right now":
                  player.c "I'm good right now, [chelsea.name]."
                  if chelsea.has_tag('bbw'):
                    wt_image chubby_youth_bbw_2_12
                  else:
                    wt_image chubby_youth_toned_2_13
                  chelsea.c "Okay. Maybe another time."
            "It looks ridiculous":
              if chelsea.has_tag('bbw'):
                wt_image chubby_youth_bbw_2_2
              else:
                wt_image chubby_youth_toned_2_2
              player.c "Pigtails?  What are you, ten?  It looks ridiculous."
              if chelsea.has_tag('bbw'):
                pass
              else:
                wt_image chubby_youth_toned_2_12
              chelsea.c "Really?  I guess.   I don't know what I was thinking."
              "That should put an end to this nonsense."
              $ chelsea.youth_status = 5
          call forced_movement(living_room) from _call_forced_movement_269
          call character_location_return(chelsea) from _call_character_location_return_95
        else:
          jump chelsea_girlfriend_event
    # kitchen events
    elif chelsea.gf_event == 5:
        call forced_movement(kitchen) from _call_forced_movement_270
        summon chelsea no_follows
        if chelsea.has_tag('little_girl'):
          wt_image chubby_kitchen_1_1
          "[chelsea.name]'s hanging out in the kitchen."
          chelsea.c "Hi"
          player.c "Hi, [chelsea.name]. Not working today?"
          wt_image chubby_kitchen_1_2
          chelsea.c "Nope. I haven't decided what I'm going to do today."
          $ title = "What do you say?"
          menu:
            "Suggest she put on a show for you":
              wt_image chubby_kitchen_1_3
              chelsea.c "A show?  What kind of show?"
              player.c "The sort where you climb up on the counter to start."
              wt_image chubby_kitchen_1_5
              chelsea.c "Okay.  I guess the show starts with a peek at my panties."
              wt_image chubby_kitchen_1_15
              player.c "Only for a moment.  Those need to come off."
              wt_image chubby_kitchen_1_6
              chelsea.c "I suppose my top should come off, too?"
              wt_image chubby_kitchen_1_7
              chelsea.c "Now what?"
              $ title = "What do you tell her?"
              menu:
                "Put a finger in your ass" if chelsea.anal_status > 3:
                  $ chelsea.visit_count -= 1
                  if chelsea.anal_status == 4:
                    player.c "I want to watch you put a finger in your ass."
                    wt_image chubby_kitchen_1_22
                    chelsea.c "Are you serious? Why??"
                    player.c "I'll enjoy watching it."
                    chelsea.c "But that's ..."
                    wt_image chubby_kitchen_1_21
                    player.c "Something I want you to do for me.  It won't hurt.  Wet your finger and just take it nice and slow."
                    wt_image chubby_kitchen_1_12
                    "[chelsea.name] makes a face as she reaches behind herself ..."
                    wt_image chubby_kitchen_1_13
                    "... and slowly inserts a digit up her butt."
                    wt_image chubby_kitchen_1_14
                    call chelsea_anal_fingering from _call_chelsea_anal_fingering_8
                    wt_image chubby_kitchen_1_12
                    chelsea.c "I think that's enough."
                  else:
                    wt_image chubby_kitchen_1_13
                    "[chelsea.name] doesn't particularly like it, but she's become used to your fascination with her ass. Sitting up, she reaches behind herself..."
                    wt_image chubby_kitchen_1_14
                    "... and slowly inserts a digit up her butt.  She keeps it there for a few minutes, then you both go on with your day."
                    $ chelsea.anal_fingering_count += 1
                "Show off your body":
                  wt_image chubby_kitchen_1_8
                  chelsea.c "Show off my body?  Okay, [chelsea.your_name]."
                  wt_image chubby_kitchen_1_9
                  chelsea.c "This is something I've been practicing."
                  wt_image chubby_kitchen_1_10
                  chelsea.c "Ouch.  Your little girl isn't as young as she used to be.  I think I need more practice making that shape."
                  wt_image chubby_kitchen_1_11
                  chelsea.c "This one I've learned to do perfectly, though!"
              $ chelsea.stripped_count += 1
              change player energy by -energy_short notify
            "Tell her not to waste this beautiful day":
              player.c "It's a beautiful day out there, young lady.  Don't waste it hanging around in the house."
              wt_image chubby_kitchen_1_1
              chelsea.c "Okay, I won't. You don't have to lecture me."
              player.c "Apparently I do, seeing as you're wasting time in here letting the day slip away from you."
              wt_image chubby_kitchen_1_2
              chelsea.c "Sheesh, I said I was going to find something to do."
              player.c "So, get on with it."
              wt_image chubby_kitchen_1_3
              chelsea.c "I am!"
              wt_image chubby_kitchen_1_20
              "She leaves with a small huff, but inside you know that she's secretly pleased about being treated like a young girl."
              sys "[chelsea.name] is happier with your relationship."
              $ chelsea.relationship_counter += 0.5
            "Wish her luck":
              player.c "Good luck figuring out what you want to do."
              chelsea.c "Thanks! Maybe I'll go back to bed. Or watch some tv. Or maybe listen to music. I can't decide."
              "You leave her to her youthful indecision."
        else:
          if chelsea.has_tag('bbw'):
            wt_image chubby_kitchen_2_10
            "[chelsea.name]'s hanging out in the kitchen."
            chelsea.c "Hi"
            player.c "Hi, [chelsea.name]. Not working today?"
            wt_image chubby_kitchen_2_1
            chelsea.c "Not today. I haven't decided what I'm going to do with my day off."
            $ title = "What do you say?"
            menu:
              "Suggest she put on a show for you":
                wt_image chubby_kitchen_2_12
                chelsea.c "A show?  What kind of show?"
                wt_image chubby_kitchen_2_3
                player.c "The sort where you climb up on the counter to start."
                wt_image chubby_kitchen_2_4
                chelsea.c "Okay.  Now what?"
                $ title = "What do you tell her?"
                menu:
                  "Put a finger in your ass" if chelsea.anal_status > 3:
                    $ chelsea.visit_count -= 1
                    if chelsea.anal_status == 4:
                      player.c "I want to watch you put a finger in your ass."
                      wt_image chubby_kitchen_2_13
                      chelsea.c "Are you serious?  Why??"
                      player.c "I'll enjoy watching it."
                      wt_image chubby_kitchen_2_14
                      chelsea.c "But that's ..."
                      wt_image chubby_kitchen_2_15
                      player.c "Something I want you to do for me.  It won't hurt.  Turn around and pull off your clothes to give you access, then just take it nice and slow."
                      wt_image chubby_kitchen_1_12
                      "[chelsea.name] makes a face as she reaches behind herself ..."
                      wt_image chubby_kitchen_1_13
                      "... and slowly inserts a digit up her butt."
                      wt_image chubby_kitchen_1_14
                      call chelsea_anal_fingering from _call_chelsea_anal_fingering_9
                      wt_image chubby_kitchen_1_12
                      chelsea.c "I think that's enough."
                    else:
                      wt_image chubby_kitchen_1_13
                      "[chelsea.name] doesn't particularly like it, but she's become used to your fascination with her ass.  Sitting up, she reaches behind herself ..."
                      wt_image chubby_kitchen_1_14
                      "... and slowly inserts a digit up her butt.  She keeps it there for a few minutes, then you both go on with your day."
                  "Show off your body":
                    chelsea.c "You want a strip tease from up here?"
                    player.c "Not necessarily.  There's a water faucet beside you."
                    wt_image chubby_kitchen_2_5
                    chelsea.c "What am I supposed to do with that?"
                    player.c "You're a bright girl. Use your imagination."
                    chelsea.c "I don't ...  oh!"
                    wt_image chubby_kitchen_2_16
                    "[chelsea.name] sits at the edge of the sink. After waiting for the water to warm up ..."
                    wt_image chubby_kitchen_2_6
                    "... she starts spraying it over herself."
                    wt_image chubby_kitchen_2_7
                    chelsea.c "Can you see me?  Through my clothes, I mean."
                    player.c "Yes. You look good."
                    wt_image chubby_kitchen_2_8
                    "Encouraged, [chelsea.name] starts hamming it up."
                    chelsea.c "Did you know they used to do this as a competition?  Wet t-shirt contests, I mean."
                    player.c "How do you know?  Did you ever enter one?  You're a natural."
                    wt_image chubby_kitchen_2_17
                    chelsea.c "No!  You won't catch me up on a stage."
                    player.c "Too bad.  You'd win for sure."
                    wt_image chubby_kitchen_2_9
                    chelsea.c "Thanks!"
                $ chelsea.stripped_count += 1
                change player energy by -energy_very_short notify
              "Suggest she do some baking":
                player.c "You're hanging out in the kitchen. You must be thinking about making something to eat. Why don't you bake up something tasty?"
                wt_image chubby_kitchen_2_11
                chelsea.c "I shouldn't. I don't need the extra calories."
                player.c "I'll help you eat whatever you bake up."
                wt_image chubby_kitchen_2_2
                chelsea.c "You will?  Okay, then!"
                wt_image chubby_kitchen_2_10
                chelsea.c "And thanks for not getting on my case about my weight. It's really nice that you find my curves sexy."
                "She busies herself with preparing her baking, a process that takes the remainder of the day."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
              "Wish her luck":
                player.c "Good luck figuring out what you want to do."
                chelsea.c "Thanks!"
                "You leave her to her indecision."
          else:
            wt_image chubby_kitchen_1_1
            "[chelsea.name]'s hanging out in the kitchen."
            chelsea.c "Hi."
            player.c "Hi, [chelsea.name]. Not working today?"
            wt_image chubby_kitchen_1_2
            chelsea.c "Not today. I haven't decided what I'm going to do with my day off. I should go for a run, but I haven't been able to motivate myself."
            $ title = "What do you say?"
            menu:
              "Suggest she put on a show for you":
                wt_image chubby_kitchen_1_4
                chelsea.c "A show?  What kind of show?"
                player.c "The sort where you climb up on the counter to start."
                wt_image chubby_kitchen_1_6
                chelsea.c "I don't suppose you'll want me clothed for this show."
                "She pulls off her top ..."
                wt_image chubby_kitchen_1_15
                "... and panties  ..."
                wt_image chubby_kitchen_1_16
                "... and climbs up on the counter."
                chelsea.c "Now what?"
                $ title = "What do you tell her?"
                menu:
                  "Put a finger in your ass" if chelsea.anal_status > 3:
                    $ chelsea.visit_count -= 1
                    if chelsea.anal_status == 4:
                      player.c "I want to watch you put a finger in your ass."
                      wt_image chubby_kitchen_1_22
                      chelsea.c "Are you serious?  Why??"
                      player.c "I'll enjoy watching it."
                      chelsea.c "But that's ..."
                      wt_image chubby_kitchen_1_21
                      player.c "Something I want you to do for me.  It won't hurt.  Wet your finger and just take it nice and slow."
                      wt_image chubby_kitchen_1_12
                      "[chelsea.name] makes a face as she reaches behind herself ..."
                      wt_image chubby_kitchen_1_13
                      "... and slowly inserts a digit up her butt."
                      wt_image chubby_kitchen_1_14
                      call chelsea_anal_fingering from _call_chelsea_anal_fingering_10
                      wt_image chubby_kitchen_1_12
                      chelsea.c "I think that's enough."
                    else:
                      wt_image chubby_kitchen_1_13
                      "[chelsea.name] doesn't particularly like it, but she's become used to your fascination with her ass.  Sitting up, she reaches behind herself ..."
                      wt_image chubby_kitchen_1_14
                      "... and slowly inserts a digit up her butt.  She keeps it there for a few minutes, then you both go on with your day."
                  "Show off your body":
                    wt_image chubby_kitchen_1_17
                    chelsea.c "Show off my body?  Okay.  Do you prefer me as a muse ..."
                    wt_image chubby_kitchen_1_18
                    chelsea.c "... or a pin-up ..."
                    wt_image chubby_kitchen_1_19
                    chelsea.c "... or something dirtier?"
                    player.c "You look good as any of them, [chelsea.name]."
                    wt_image chubby_kitchen_1_22
                    chelsea.c "Thanks!"
                $ chelsea.stripped_count += 1
                change player energy by -energy_short notify
              "Encourage her to go for the run":
                player.c "You should go for a run."
                wt_image chubby_kitchen_1_1
                chelsea.c "Thanks. That was unsubtle."
                player.c "It's a beautiful day out there. You'll feel better if you get out and make good use of it. If you don't go for a run, you'll be feeling bad about yourself tonight."
                wt_image chubby_kitchen_1_20
                chelsea.c "You're right. Thanks for keeping me motivated. And for coming up for a reason for your comment that didn't involve pointing out that I've let a few pounds creep back on."
                "She disappears to go put her running gear on."
                sys "[chelsea.name] is happier with your relationship."
                $ chelsea.relationship_counter += 0.5
              "Wish her luck":
                player.c "Good luck getting motivated. Or staying unmotivated, whichever you're more in the mood for."
                chelsea.c "Thanks! I haven't figured that out myself."
                "You leave her to her indecision."
        call forced_movement(living_room) from _call_forced_movement_271
        call character_location_return(chelsea) from _call_character_location_return_96
    # youth event
    elif chelsea.gf_event == 6:
        if chelsea.youth_status == 2 or chelsea.youth_status > 5:
          call forced_movement(living_room) from _call_forced_movement_272
          summon chelsea no_follows
          wt_image chubby_youth_3_31
          "[chelsea.name] bursts in, wearing an old schoolgirl's uniform."
          wt_image chubby_youth_3_1
          chelsea.c "Look what I found!  Can you believe I used to wear this everyday when I was a little girl in school?"
          $ title = "How do you reply?"
          menu:
            "Encourage her":
              $ chelsea.youth_status += 1
              wt_image chubby_youth_3_2
              player.c "You look very cute in that outfit, [chelsea.name].  Perhaps I should start treating you like a schoolgirl?"
              wt_image chubby_youth_3_8
              chelsea.c "I think I'd like it if you did that."
              $ title = "What do you do?"
              menu menu_chelsea_gf_6_encourage_her:
                "Take her to school":
                  if hannah.letter_re_terri < 2 or hannah.letter_re_terri > 7:
                    if hannah.letter_re_terri > 7:
                      "Principal Hannah won't be happy if you're caught on school grounds, but she's not really in any position to object."
                    else:
                      if hannah.letter_re_terri == 0:
                        $ hannah.letter_re_terri = 1
                        $ hannah.visit_week = week
                        if day == 1:
                          $ hannah.visit_day = 2
                        else:
                          if is_weekend():
                            $ hannah.visit_day = 4
                          else:
                            $ hannah.visit_day = day
                    wt_image chubby_youth_3_2
                    player.c "You're late for school, young lady."
                    chelsea.c "What do you mean?"
                    wt_image chubby_youth_3_31
                    player.c "No time to talk.  Come on, I'll give you a lift."
                    if hannah.location == school:
                      dismiss hannah # this is so Hannah isn't in the room when you go to the school
                    call forced_movement(school) from _call_forced_movement_273
                    summon chelsea no_follows
                    wt_image chubby_youth_3_20
                    "The school is open, but the students and teachers are all in class as you sneak in. Enrollment is down in the district, and many rooms are empty, including the gym.  After checking to make sure it's unoccupied, you lead [chelsea.name] into the boy's locker room."
                    chelsea.c "All the years I went to this school, I was never in here."
                    player.c "You never snuck into the boy's locker room?"
                    chelsea.c "Nope"
                    wt_image chubby_youth_3_21
                    player.c "What do you think would have happened if you had come in here?  Do you think one of the boys would have grabbed you?"
                    chelsea.c "Maybe?"
                    wt_image chubby_youth_3_22
                    player.c "Or maybe one of the teachers would've grabbed you, to investigate what kind of a slut he'd found sneaking into the boy's locker room?"
                    chelsea.c "Oh!"
                    wt_image chubby_youth_3_23
                    "Exposing her breasts, you reach a hand down and rub her between her legs."
                    chelsea.c "Ahhhh"
                    player.c "What would you have done, if your favorite teacher had felt you up and treated you like a slut, little girl?"
                    wt_image chubby_youth_3_24
                    "[chelsea.name]'s response is to turn her head and give you a dirty kiss."
                    player.c "That's what I thought.  You're a total slut.  Are you wet under that school skirt, little girl?"
                    chelsea.c "Yes"
                    wt_image chubby_youth_3_25
                    player.c "We both know what he'd do once he fond out you were wet.  Would you try to stop him?"
                    chelsea.c "No"
                    wt_image chubby_youth_3_26
                    player.c "No, you'd let him put his big adult dick inside your tight, schoolgirl pussy.  Would his have been the first dick inside you?"
                    "[chelsea.name] shakes her head."
                    wt_image chubby_youth_3_28
                    player.c "No, he'd figure that out as soon as he penetrated you.  You're not a virgin.  You've had dicks inside you before, probably lots of them.  That means he doesn't need to be gentle with you.  He can fuck you like the slut you are, as hard and as fast as he wants to fuck you."
                    chelsea.c "Ahhhhh"
                    wt_image chubby_youth_3_27
                    player.c "And the harder he fucked you, the faster you'd cum.  You'd probably cum before he did, wouldn't you, slut?"
                    wt_image chubby_youth_3_49
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_youth_3_50
                    player.c "He wouldn't cum inside you, though.  A slut like you might not be on birth control.  He'd find someplace else to spill his load."
                    wt_image chubby_youth_3_51
                    "Rolling her over, you aim at her face and tits."
                    wt_image chubby_youth_3_29
                    player.c "[player.orgasm_text]"
                    wt_image chubby_youth_3_30
                    chelsea.c "Mmmmm.  I like being a schoolgirl with you."
                    player.c "Better get yourself cleaned up, little girl, so we can get out of here.  Unless you want an encore with a real teacher."
                    $ chelsea.masturbation_count += 1
                    $ chelsea.sex_count += 1
                    $ chelsea.orgasm_count += 1
                    orgasm notify
                    sys "[chelsea.name] is happier with your relationship."
                    $ chelsea.relationship_counter += 1
                    $ chelsea.training_session()
                    call forced_movement(living_room) from _call_forced_movement_274
                    call character_location_return(hannah) from _call_character_location_return_97 #This is done to make sure Hannah is returned to the school after the scene with Chelsea.
                  else:
                    if hannah.letter_re_terri == 2:
                      "You'd like to take [chelsea.name] to school, but after the letter you received from the last time you entered school grounds, you decide it would be better not to."
                    else:
                      "You'd like to take [chelsea.name] to school, but if Principal Hannah catches you on school grounds again, it could get ugly.  Better not risk that."
                    jump menu_chelsea_gf_6_encourage_her
                "Spank her":
                  player.c "If you're going to be my little girl, then I'm going to have to keep you in line when you act up."
                  wt_image chubby_youth_3_2
                  chelsea.c "Oh no!  I'll be good."
                  player.c "Yes, you will.  That means no dressing like a slutty tease to get the boys hot and bothered."
                  wt_image chubby_youth_3_32
                  chelsea.c "This is just my school outfit."
                  player.c "Don't talk to back to me, young lady.  Bend over that desk and lift your skirt."
                  if chelsea.dominate_status == 8:
                    wt_image chubby_youth_3_33
                    "That sobered her up quick. Forlornly, she prepares for her spanking."
                    wt_image chubby_youth_3_34
                    player.c "Quit stalling and get your ass over that desk."
                    wt_image chubby_youth_3_35
                    $ title = "How do you want to spank her?"
                    menu:
                      "Hard":
                        call chelsea_gf_event_6_hard_spanking from _call_chelsea_gf_event_6_hard_spanking
                        wt_image chubby_youth_3_36
                        "When you finally finish, she looks back at you forlornly, hoping the enjoyment you got out of spanking her was worth the discomfort she went through."
                        $ chelsea.youth_skirt_spanking = 2
                        if chelsea.hypno_re_dominate == 2:
                          $ chelsea.relationship_counter -= 0.5
                        else:
                          $ chelsea.relationship_counter -= 1
                        sys "[chelsea.name] is less happy with your relationship."
                      "Gently":
                        "*smack*"
                        wt_image chubby_youth_3_39
                        chelsea.c "Oh!"
                        "She's not sure what to make of the first 'love tap' you give her.  She looks back at you and grins when she realizes exactly what type of spanking you have in mind for her today ... *smack*."
                        call chelsea_gf_event_6_playful_spanking from _call_chelsea_gf_event_6_playful_spanking
                  else:
                    if chelsea.dominate_status > 5:
                      wt_image chubby_youth_3_33
                      "Nervously, she picks at her clothing, uncertain about where you're going with this."
                      chelsea.c "Were you planning on ..."
                      wt_image chubby_youth_3_34
                      player.c "I said bend over the desk and present your ass to me, [chelsea.name]."
                    else:
                      wt_image chubby_youth_3_45
                      "She giggles as she turns around."
                      wt_image chubby_youth_3_41
                      chelsea.c "You wouldn't really hurt your little girl, would you?"
                      wt_image chubby_youth_3_11
                      "She's all set to take a playful 'spanking', and looks like she'll find that fun.  Or you could use this opportunity to exert your dominance over her, although won't like that and won't accept it unless she's otherwise feeling good about your relationship."
                    wt_image chubby_youth_3_35
                    $ title = "How do you want to spank her?"
                    menu:
                      "Seriously":
                        player.c "If you're going to be my little girl, you have to accept that I'll punish you as I see fit."
                        if chelsea.relationship_counter > 4 or chelsea.has_tag('relationship_warnings_shut_off'):
                          wt_image chubby_youth_3_32
                          chelsea.c "Hold on, are you serious?  Do you really mean that?  Is that what you want from me, to be able to punish me?"
                          player.c "Yes, it is, and I hope it's something you're willing to do for me, as my little girl."
                          wt_image chubby_youth_3_33
                          "[chelsea.name] hesitates, as if deciding whether she can go through with it.  Her silence tells you she can."
                          wt_image chubby_youth_3_34
                          player.c "Over the desk, ass in the air."
                          call chelsea_gf_event_6_hard_spanking from _call_chelsea_gf_event_6_hard_spanking_1
                          wt_image chubby_youth_3_36
                          "When you finally finish, she looks back at you, wondering if this is a one time deal or something you'll want from her again?"
                          $ chelsea.youth_skirt_spanking = 2
                          if chelsea.hypno_re_dominate == 2:
                            $ chelsea.relationship_counter -= 2
                          else:
                            $ chelsea.relationship_counter -= 3
                          sys "[chelsea.name] is less happy with your relationship."
                        else:
                          wt_image chubby_youth_3_32
                          chelsea.c "Whoa, hold on, [chelsea.your_name].  This was meant to be fun.  I'm not going to let you punish me."
                          sys "Your relationship with [chelsea.name] isn't strong enough for her to accept a serious spanking.  You'll have to make this a fun spanking, instead."
                          player.c "Relax and lean over the desk. You'll enjoy this."
                          wt_image chubby_youth_3_35
                          chelsea.c "Promise?"
                          player.c "Promise"
                          call chelsea_gf_event_6_playful_spanking from _call_chelsea_gf_event_6_playful_spanking_1
                      "Playfully":
                        call chelsea_gf_event_6_playful_spanking from _call_chelsea_gf_event_6_playful_spanking_2
                  $ chelsea.spank_count += 1
                  change player energy by -energy_short notify
                "Tell her to put on a show":
                  player.c "You look very sexy in that outfit.  I bet the boys liked looking at you when you wore that.  Did you like that?  Did you like to tease them and show off your legs?"
                  wt_image chubby_youth_3_46
                  chelsea.c "Maybe?"
                  player.c "How far did you go?  Did you flash your tits at boys?"
                  wt_image chubby_youth_3_9
                  chelsea.c "If I liked them.  I like you.  I might end up trying to tease you."
                  wt_image chubby_youth_3_3
                  "You settle back to enjoy the show."
                  wt_image chubby_youth_3_47
                  "[chelsea.name]'s a bit awkward ..."
                  wt_image chubby_youth_3_4
                  "... but nervously enthusiastic, just as an actual schoolgirl might be ..."
                  wt_image chubby_youth_3_48
                  "... although she's rather better developed than most real schoolgirls."
                  wt_image chubby_youth_3_5
                  player.c "You're not going to stop at just flashing your tits at me, are you?"
                  wt_image chubby_youth_3_6
                  "Sliding to the floor, [chelsea.name] pulls down her panties, giving you a view of her bare-as-a-schoolgirl kitty."
                  wt_image chubby_youth_3_7
                  "She's no showgirl, but she looks like she enjoyed either taking her clothes off for you or pretending to be a schoolgirl, or maybe both."
                  sys "[chelsea.name] is happier with your relationship."
                  $ chelsea.relationship_counter += 1
                  $ chelsea.stripped_count += 1
                  change player energy by -energy_very_short notify
            "Put an end to this":
              wt_image chubby_youth_3_32
              player.c "[chelsea.name], I appreciate the schoolgirl fantasy display, but I'm worried about where this is going."
              chelsea.c "Oh, don't get your knickers in a knot, [chelsea.your_name].  I'm just reminiscing.  I'm not about to start acting like a schoolgirl around you."
              wt_image chubby_youth_3_8
              chelsea.c "But since I went through the trouble of putting this on, do you want to see it come off?"
              $ chelsea.youth_status = 5
              $ title = "What do you do?"
              menu:
                "Watch her strip":
                  wt_image chubby_youth_3_3
                  "You settle back to enjoy the show."
                  wt_image chubby_youth_3_4
                  "[chelsea.name] grins as she pulls down her bra ..."
                  wt_image chubby_youth_3_5
                  "... exposing her massive boobs."
                  wt_image chubby_youth_3_6
                  "Then she sinks to the floor and pulls down her panties."
                  wt_image chubby_youth_3_7
                  "She's no showgirl, but she looks like she enjoyed herself."
                  $ chelsea.stripped_count += 1
                  change player energy by -energy_very_short notify
                "Decline":
                  player.c "Perhaps another time. I've got things I want to do today."
                  wt_image chubby_youth_3_31
                  chelsea.c "Your loss!"
          call character_location_return(chelsea) from _call_character_location_return_98
        else:
          jump chelsea_girlfriend_event
    # youth event and possible conversion
    elif chelsea.gf_event == 7:
        if chelsea.youth_status == 3:
          call forced_movement(living_room) from _call_forced_movement_275
          summon chelsea no_follows
          if chelsea.has_item(jewelry_chelsea):
            wt_image chubby_youth_4_1
            "[chelsea.name] appears, carrying a teddy bear."
          else:
            wt_image chubby_youth_4_3
            "[chelsea.name] is waiting for you on the sofa, curled up with  plush toy."
          chelsea.c "Can we chat?  I've been thinking - I really like acting like a little girl around you, and you seem to enjoy it, too."
          if terri.has_tag('adult_baby'):
            chelsea.c "Not like, Terri, though.  I don't want to wear a diaper and sit in a playpen.  I like it when you treat me like a school-age girl."
          chelsea.c "Could I be your little girl, all the time?"
          $ title = "What do you tell her?"
          menu:
            "Yes":
              player.c "I would love to have you as my little girl."
              if chelsea.has_item(jewelry_chelsea):
                wt_image chubby_youth_4_2
                chelsea.c "Yay!"
                "She hugs the teddy happily."
              else:
                wt_image chubby_youth_4_4
                chelsea.c "Yay!"
                "She squeezes the plush toy happily."
              chelsea.c "Umm, can I call you Daddy?"
              $ title = "What should she call you?"
              menu:
                "Daddy":
                  $ chelsea.relationship_counter += 3
                  $ chelsea.your_name = "Daddy"
                  player.c "Yes, you can call me Daddy, baby girl."
                  chelsea.c "Yay!  Thank you, Daddy.  I need to go get some clothes suitable for your baby girl to wear.  Bye!"
                "Stick with 'Big Guy'":
                  $ chelsea.relationship_counter += 1
                  player.c "Let's stick with Big Guy, okay little girl?"
                  chelsea.c "Okay, Big Guy.  I need to go get some clothes suitable for your baby girl to wear.  Bye!"
              sys "[chelsea.name] is happier with your relationship."
              $ chelsea.youth_status = 4
              $ chelsea.suffix = "the Little Girl"
              add tags 'little_girl' to chelsea
            "Only once in a while":
              player.c "You're right, [chelsea.name], I have enjoyed you role playing as my little girl, but I don't want that all the time.  Can we save that as a once in while thing?"
              chelsea.c "Okay. That's fine."
              "If she's disappointed, she keeps it well hidden."
              $ chelsea.youth_status = 6
            "No":
              player.c "Role playing has been fun, [chelsea.name], but I want you as my girlfriend, not a little girl."
              chelsea.c "Okay. That's fine. You seemed to be having fun, so I thought I would ask."
              "If she's disappointed, she keeps it well hidden."
              $ chelsea.youth_status = 5
          call character_location_return(chelsea) from _call_character_location_return_99
        else:
          jump chelsea_girlfriend_event
    # run or shower
    elif chelsea.gf_event == 8:
        # morning run
        if chelsea.has_tag('toned'):
          call forced_movement(backyard) from _call_forced_movement_276
          summon chelsea no_follows
          wt_image chubby_gf_event_7_1
          "As you step outside to check on the weather in the morning, [chelsea.name] almost runs over you."
          wt_image chubby_gf_event_7_2
          chelsea.c "Whoops.  Sorry, [chelsea.your_name].  I wanted to get a run in this morning, and I woke up later than I meant to.  I was rushing and not paying attention."
          $ title = "What do you do?"
          menu:
            "Use her trigger" if chelsea.has_tag('trigger_implanted'):
              $ chelsea.training_session()
              player.c "If you're in that much of a hurry, you shouldn't have wasted time putting your clothes on."
              wt_image chubby_gf_event_7_19
              chelsea.c "What?  I couldn't go for a run in the nude."
              player.c "Sure you could have. Try it."
              chelsea.c "Try what??"
              player.c "Take off your clothes and go for your run naked."
              wt_image chubby_gf_event_7_18
              chelsea.c "I can't do that."
              player.c "Yes, you can. [chelsea.trigger_phrase], [chelsea.name].  Take off your clothes and go for your run naked."
              wt_image chubby_gf_event_7_4
              chelsea.c "But ..."
              player.c "[chelsea.trigger_phrase].  You want to run naked this morning, [chelsea.name]."
              wt_image chubby_gf_event_7_20
              "The hypnotized woman pulls off her clothes ..."
              wt_image chubby_gf_event_7_6
              "... and takes off running.  As long as she runs fast enough, she should be able to stay out of trouble."
              $ chelsea.stripped_count += 1
            "Spank her" if chelsea.has_tag('little_girl') or chelsea.dominate_status == 8:
                $ chelsea.training_session()
                player.c "Sorry isn't going to cut it.  Pull your pants down and bend over that table."
                chelsea.c "What??  I'm about to go for a run!  Bumping into you was just an accident."
                if chelsea.has_tag('little_girl'):
                    wt_image chubby_gf_event_7_5
                    player.c "An accident caused by you rushing and not paying attention, young lady.  Get your pants down.  Maybe a spanking will help you remember to watch where you're going next time."
                    wt_image chubby_gf_event_7_8
                    chelsea.c "This isn't fair! I won't have time for my run now."
                    player.c "I'll decide what's fair, young lady. Let this be a lesson to you. Rushing isn't always faster."
                else:
                    wt_image chubby_gf_event_7_7
                    chelsea.c "A spanking? I'm not a child!"
                    player.c "Then you shouldn't have acted like one, sleeping in and then causing an accident by rushing.  Now present your ass to me for your punishment before you earn a longer one."
                    wt_image chubby_gf_event_7_5
                    "[chelsea.name]'s flustered and confused.  She doesn't want to be punished, and she's a little ticked at you for making a big deal out of a small thing.  But she's now also used to you dominating her sexually, so she's not completely surprised that you're turning her mistake into a spanking."
                    wt_image chubby_gf_event_7_8
                    "She would never have voluntarily sought out a relationship where she's subject to domestic discipline, but the nature of your relationship has evolved such that she finds herself meekly bending over the table and presenting her bare ass to you for her spanking."
                wt_image chubby_gf_event_7_21
                "*smack* ... *smack* ... *smack*"
                wt_image chubby_gf_event_7_15
                chelsea.c "ow"
                $ chelsea.temporary_count = 3
                $ title = "Spank her again?"
                menu menu_chelsea_gf_event_8_spank_menu:
                    "Yes":
                        $ chelsea.temporary_count += 1
                        wt_image chubby_gf_event_7_21
                        "*smack*"
                        wt_image chubby_gf_event_7_15
                        if chelsea.temporary_count < 5:
                            chelsea.c "Ow!"
                        elif chelsea.temporary_count < 10:
                            chelsea.c "Oww!"
                        elif chelsea.temporary_count < 15:
                            chelsea.c "Oww!!"
                        elif chelsea.temporary_count < 20:
                            chelsea.c "OWW!!"
                        if chelsea.temporary_count < 20:
                            jump menu_chelsea_gf_event_8_spank_menu
                        else:
                            chelsea.c "OW!  I'm sorry!!  I'm sorry, I've learned my lesson!!  I'll get up earlier from now on and not rush, [chelsea.your_name].  I promise."
                            player.c "See that you do."
                            wt_image chubby_gf_event_7_21
                            "*smack*"
                            wt_image chubby_gf_event_7_9
                            chelsea.c "oh ohh ohhhh!!!"
                            if chelsea.has_tag('little_girl'):
                                "She's upset at being disciplined, but secretly pleased at having you treat her like a naughty little girl."
                            else:
                                "She's upset at being disciplined, but with how you've conditioned her, she can't bring herself to blame you. Instead, she internalizes her displeasure with herself, for doing something that upset you enough that you felt the need to spank her."
                    "No":
                        wt_image chubby_gf_event_7_9
                        chelsea.c "I'm sorry, I've learned my lesson!!  I'll get up earlier from now on and not rush, [chelsea.your_name].  I promise."
                        player.c "See that you do."
                        if chelsea.has_tag('little_girl'):
                            "She's upset at being disciplined, but secretly pleased at having you treat her like a naughty little girl."
                        else:
                            "She's upset at being disciplined, but with how you've conditioned her, she can't bring herself to blame you. Instead, she internalizes her displeasure with herself, for doing something that upset you enough that you felt the need to spank her."
                $ chelsea.spank_count += 1
                $ chelsea.temporary_count = 0
                change player energy by -energy_short notify
            "Suggest she 'exercise' here":
              $ chelsea.training_session()
              player.c "Rushing's not good for you, [chelsea.name].  You're getting yourself stressed out.  Stay and exercise here, while I watch.  It'll help you relax."
              wt_image chubby_gf_event_7_18
              chelsea.c "Exercising while you watch will help me relax?"
              player.c "The exercise I have in mind for you will."
              wt_image chubby_gf_event_7_19
              chelsea.c "Will I need to change my clothes for this exercise?"
              player.c "You won't need that top, that's for sure."
              wt_image chubby_gf_event_7_10
              chelsea.c "Why am I not surprised?"
              wt_image chubby_gf_event_7_22
              chelsea.c "What about my bottoms?"
              wt_image chubby_gf_event_7_11
              player.c "Those can come down, too.  Then lean over the table, so I have a close up view of your work out."
              wt_image chubby_gf_event_7_23
              chelsea.c "What kind of work out can I do here?"
              player.c "One that involves your fingers."
              wt_image chubby_gf_event_7_12
              chelsea.c "That doesn't sound like much exercise."
              player.c "Done right, it'll engage every muscle in your body. And be far more relaxing than trying to go for a run you don't properly have time for."
              wt_image chubby_gf_event_7_13
              chelsea.c "I don't know if this is going to work with you watching me."
              player.c "Sure it will.  Like any exercise, it just takes practice to get good at it."
              wt_image chubby_gf_event_7_14
              "It does take a while, but soon you can see, smell, and hear the tell tale signs of her arousal."
              chelsea.c "Ahhhh"
              if chelsea.anal_status > 3:
                player.c "Don't forget your butt hole."
                wt_image chubby_gf_event_7_13
                chelsea.c "Wh ... what?"
                player.c "Your butt hole.  Stick a finger in it while you're masturbating."
                if chelsea.anal_status == 4:
                  wt_image chubby_gf_event_7_9
                  chelsea.c "I don't like that."
                  player.c "I'd like it, and I'd like you to get over your aversion to having things up your butt. That's never going to happen if you don't practice and get used to it."
                  wt_image chubby_gf_event_7_16
                  "Hesitantly, she slowly pushes a finger into her ass."
                  call chelsea_anal_fingering from _call_chelsea_anal_fingering_11
                  wt_image chubby_gf_event_7_24
                  player.c "Okay, [chelsea.name].  Start playing with your pussy, again."
                else:
                  wt_image chubby_gf_event_7_24
                  "[chelsea.name]'s become used to you wanting to see her play with her ass. She doesn't argue, just shoves a finger up her butt until you tell her she can go back to frigging herself."
                wt_image chubby_gf_event_7_14
                "It takes a while for her to re-ignite her body's arousal, but she gets there."
                chelsea.c "Ahhhh"
              wt_image chubby_gf_event_7_13
              "After that, it doesn't take her much longer to finish herself off."
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_7_8
              player.c "That was more relaxing than a run, wasn't it?"
              wt_image chubby_gf_event_7_25
              chelsea.c "Mmmmm, and my legs are trembling even more than they do after a good run, too."
              "You leave [chelsea.name] to get herself re-dressed and go about your day."
              $ chelsea.masturbation_count += 1
              $ chelsea.orgasm_count += 1
              change player energy by -energy_very_short notify
            "Wish her a good run":
              if chelsea.has_tag('little_girl'):
                player.c "Watch where you're going from now on, young lady."
                wt_image chubby_gf_event_7_18
                chelsea.c "I will, [chelsea.your_name]."
              player.c "Have a good run."
              wt_image chubby_gf_event_7_1
              chelsea.c "Thanks!"
              wt_image chubby_gf_event_7_3
              "You watch her bottom bouncing in her pink shorts as she heads off."
          call forced_movement(living_room) from _call_forced_movement_277
          call character_location_return(chelsea) from _call_character_location_return_100
        # shower scene for BBW
        elif chelsea.has_tag('bbw'):
            call forced_movement(bathroom) from _call_forced_movement_278
            summon chelsea no_follows
            wt_image chubby_shower_1_1
            "As you step into the bathroom, you see that [chelsea.name] is using the shower."
            wt_image chubby_shower_1_2
            chelsea.c "Hi, [chelsea.your_name].  I'm almost finished."
            wt_image chubby_shower_1_3
            $ title = "What do you do?"
            menu:
                "Suggest she gets off before she gets out":
                    $ chelsea.training_session()
                    wt_image chubby_shower_1_4
                    chelsea.c "Umm, what?"
                    player.c "You have the right idea, just spread your legs while you spray there."
                    wt_image chubby_shower_1_5
                    chelsea.c "This isn't going to do what you seem to think it will.  The water's too stingy."
                    player.c "Add your fingers."
                    wt_image chubby_shower_1_6
                    chelsea.c "Well, sure, that feels nice, but it'd be a lot less awkward on the bed."
                    wt_image chubby_shower_1_7
                    player.c "Keep fingering yourself, but use the spray directly on your nipples and clit while you do so."
                    wt_image chubby_shower_1_8
                    "You're not sure if its the intensity of the sensations or having you watching her, or both ..."
                    wt_image chubby_shower_1_9
                    "... but suddenly something triggers a response in [chelsea.name]."
                    wt_image chubby_shower_1_10
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_shower_1_11
                    chelsea.c "If I end up taking longer showers from now on, [chelsea.your_name], you have only yourself to blame."
                    $ chelsea.masturbation_count += 1
                    $ chelsea.orgasm_count += 1
                    change player energy by -energy_very_short notify
                "Go on with your day":
                    pass
            call forced_movement(living_room) from _call_forced_movement_279
            call character_location_return(chelsea) from _call_character_location_return_101
        # shouldn't be possible to get to here, but just in case
        else:
          jump chelsea_girlfriend_event
    # asleep in am event
    elif chelsea.gf_event == 9:
      $ chelsea.training_session()
      call forced_movement(living_room) from _call_forced_movement_280
      summon chelsea no_follows
      wt_image chubby_gf_event_4_1
      "In the morning, you find [chelsea.name] flaked out on the sofa."
      player.c "Good morning, sleepyhead."
      chelsea.c "Hmmm ... what?  Oh!  Good morning."
      wt_image chubby_gf_event_4_2
      chelsea.c "Ugghh.  I fell asleep watching TV last night."
      player.c "So I see."
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_event_4_13
      else:
        wt_image chubby_gf_event_4_4
      chelsea.c "How long have you been watching me?  I hope I wasn't doing anything embarrassing."
      "You decide to string her along."
      player.c "You put on quite a show."
      if chelsea.has_tag('bbw'):
        wt_image chubby_gf_event_4_3
      else:
        wt_image chubby_gf_event_4_14
      chelsea.c "I did??"
      $ title = "What do you say?"
      menu:
        "No, but you could now":
          wt_image chubby_gf_event_4_16
          chelsea.c "You want me to put on a show?  I seem to be showing a lot already."
          $ title = "What type of show do you want?"
          menu:
            "Put her finger in her ass" if chelsea.anal_status > 3:
              wt_image chubby_gf_event_4_17
              chelsea.c "What?  Why??"
              player.c "Because I'll enjoy watching it."
              if chelsea.anal_status == 4:
                chelsea.c "But ..."
                player.c "I'd like you to do this for me, [chelsea.name].  It won't hurt.  Just take your time and do it slowly."
                wt_image chubby_gf_event_4_10
                "Taking a deep breath, [chelsea.name] rolls onto her side and tentatively places her hand on her ass."
                wt_image chubby_gf_event_4_11
                "As you watch, her finger slowly disappears inside her butt hole."
                wt_image chubby_gf_event_4_12
                call chelsea_anal_fingering from _call_chelsea_anal_fingering_12
              else:
                wt_image chubby_gf_event_4_10
                "[chelsea.name]'s become used to you wanting to see things in her ass.  She rolls onto her side ..."
                wt_image chubby_gf_event_4_11
                "... and slowly pushes her finger up her butt hole."
                wt_image chubby_gf_event_4_12
                chelsea.c "If that's enough of a show for you, I should get dressed and ready for work."
              change player energy by -energy_very_short notify
            "Masturbate for me":
              wt_image chubby_gf_event_4_17
              chelsea.c "I just woke up!"
              player.c "So?"
              wt_image chubby_gf_event_4_16
              chelsea.c "I don't know if I can do that right now.  Especially with you looking at me."
              player.c "Lie back and try. I have confidence in you."
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_event_4_18
              else:
                wt_image chubby_gf_event_4_19
              chelsea.c "You have confidence that I'm always horny?"
              player.c "Those are your words."
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_event_4_5
              else:
                wt_image chubby_gf_event_4_20
              "Her eyes locked on you, [chelsea.name] begins rubbing herself."
              wt_image chubby_gf_event_4_6
              "It takes a while for her body to respond, but eventually she closes her eyes and a small moan escapes her lips."
              wt_image chubby_gf_event_4_21
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_4_7
              "Soon the sound, sight and smell of her excitement is unmistakable."
              wt_image chubby_gf_event_4_22
              chelsea.c "Ahhhhh"
              wt_image chubby_gf_event_4_23
              "Her orgasm follows shortly."
              wt_image chubby_gf_event_4_8
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_4_9
              chelsea.c "Okay, maybe I am ridiculously horny, [chelsea.your_name]."
              player.c "Again, those are your words."
              $ chelsea.masturbation_count += 1
              $ chelsea.orgasm_count += 1
              change player energy by -energy_very_short notify
            "Nothing":
              player.c "I'm kidding, silly.  Aren't you working today?  You'd better go get dressed."
              wt_image chubby_gf_event_4_15
              chelsea.c "Okay, [chelsea.your_name]. Thanks for waking me."
        "No silly, go get dressed":
          player.c "No, silly.  Aren't you working today?  You'd better go get dressed."
          wt_image chubby_gf_event_4_15
          chelsea.c "Okay, [chelsea.your_name]. Thanks for waking me."
      call character_location_return(chelsea) from _call_character_location_return_102
    # Elsa event, if possible
    elif chelsea.gf_event == 10:
        if elsa.has_tag('likes_girls') and elsa.has_tag('girlfriend') and chelsea.has_tag('likes_girls') and not elsa.has_tag('no_playing_with_chelsea_gf'):
            # NOTE: this series of events can be called from Chelsea's events, too, doubling the frequency they occur; this is on purpose given the multiple scenes
            call elsa_chelsea_gf_content from _call_elsa_chelsea_gf_content
        else:
            jump chelsea_girlfriend_event
    # bedroom sex
    elif chelsea.gf_event == 11:
        $ chelsea.training_session()
        call forced_movement(bedroom) from _call_forced_movement_281
        summon chelsea no_follows
        if chelsea.has_tag('little_girl'):
            wt_image chubby_gf_event_6_youth_24
            "You find [chelsea.name] still asleep in her bed."
            player.c "Morning, sleepyhead.  Don't you have work today?"
            wt_image chubby_gf_event_6_youth_25
            "She rolls over and looks at the clock."
            chelsea.c "Shit!  Is that the time?  I have to get going."
            wt_image chubby_gf_event_6_youth_26
            player.c "Watch your language, young lady."
            chelsea.c "Sorry, [chelsea.your_name].  I mean, I should have been up a while ago.  Thanks for waking me!"
        elif chelsea.has_tag('bbw'):
            wt_image chubby_gf_event_6_bbw_1
            "You find [chelsea.name] still asleep in her bed."
            player.c "Morning, sleepyhead.  Don't you have work today?"
            wt_image chubby_gf_event_6_bbw_2
            "She sits up and looks at the clock."
            chelsea.c "Shit!  Is that the time?  I have to get going."
            wt_image chubby_gf_event_6_bbw_23
            "[chelsea.name] hastily pulls on a t-shirt."
        else:
            wt_image chubby_gf_event_6_toned_1
            "You find [chelsea.name] still asleep in her bed."
            player.c "Morning, sleepyhead.  Don't you have work today?"
            wt_image chubby_gf_event_6_toned_27
            "She sits up and looks at the clock."
            chelsea.c "Shit!  Is that the time?  I have to get going."
        $ title = "What do you want?"
        menu menu_chelsea_gf_event_10:
          "Foot job" if chelsea.has_tag('little_girl'):
            wt_image chubby_gf_event_6_youth_1
            chelsea.c "Now, [chelsea.your_name]??  I'm late for work."
            player.c "My little girl's not going to run off without looking after me, is she?"
            wt_image chubby_gf_event_6_youth_3
            chelsea.c "I guess not, but we need to make this quick."
            wt_image chubby_gf_event_6_youth_13
            "She wasn't kidding about being quick.  She doesn't even take off her socks.  It feels weird, but also sexy ..."
            wt_image chubby_gf_event_6_youth_34
            "... and after a few pumps of her soles along your shaft, you start to cum."
            chelsea.c "Oh!"
            wt_image chubby_cum_pussy_1
            player.c "[player.orgasm_text]"
            wt_image chubby_gf_event_6_youth_28
            "As soon as your balls stop spurting jizz onto her, [chelsea.name] sits up and wipes herself off, then escapes the bed and bustles herself off to get ready for work while you recover."
            $ chelsea.footjob_count += 1
            $ chelsea.visit_count += 1
            orgasm notify
          "Tit job" if chelsea.has_tag('little_girl') or chelsea.has_tag('bbw'):
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "Now, [chelsea.your_name]??  I'm late for work."
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              wt_image chubby_gf_event_6_youth_8
              "You lie down on the bed beside her and she wraps her soft boobs tightly around your hard dick."
              wt_image chubby_gf_event_6_youth_9
              "Up and down she slides her tits along the shaft of your cock, fucking it in the deep valley of her cleavage."
              wt_image chubby_gf_event_6_youth_10
              "You promised her you would be fast, and you are.  After a few pumps of her tits along your shaft, you're ready to cum."
              wt_image chubby_gf_event_6_youth_29
              player.c "[player.orgasm_text]"
              chelsea.c "Oh!"
              wt_image chubby_gf_event_6_youth_30
              "As soon as your balls stop spurting jizz onto the air, [chelsea.name] gets herself cleaned off, escapes the bed, and bustles herself off to get ready for work while you recover."
            else:
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "Now?? I'm late for work."
                wt_image chubby_gf_event_6_bbw_25
                "You pull her t-shirt back off and pull her back onto the bed, fondling her boobs."
                player.c "Well, I did just wake you up, or you'd still be sleeping."
                wt_image chubby_gf_event_6_bbw_6
                chelsea.c "Fine, but do it quick, okay?"
                wt_image chubby_gf_event_6_bbw_26
                "[chelsea.name] lies down and forms a valley between her breasts ..."
                wt_image chubby_gf_event_6_bbw_7
                "... which you fill with your hard dick."
                wt_image chubby_gf_event_6_bbw_27
                "You promised her you'd be quick, and you are, pumping your dick rapidly back and forth between her soft mounds until you're ready to let go."
                wt_image chubby_gf_event_6_bbw_8
                player.c "[player.orgasm_text]"
                wt_image chubby_cum_tits_7
                chelsea.c "Oh good!  I'm going to go get ready for work now."
                player.c "You might want to wipe that off first."
            $ chelsea.titfuck_count += 1
            orgasm notify
          "Blow job":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "Now, [chelsea.your_name]??  I'm late for work."
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              player.c "I know a way to guarantee it'll be quick.  Lie down."
              wt_image chubby_gf_event_6_youth_5
              player.c "Put your head here, hanging over the edge of the bed."
              wt_image chubby_gf_event_6_youth_6
              "As her head falls back, you insert your cock into her mouth."
              wt_image chubby_gf_event_6_youth_7
              "You promised her fast, and you are.  She can't really blow you properly, but she uses her tongue along your cock in her mouth as best she can, and keeps her soft lips wrapped around you as you fuck her face."
              wt_image chubby_gf_event_6_youth_31
              "In this position you have a straight shot through to the back of her throat and you use it, pumping your hips forward and back, fucking her mouth the same way you'd fuck her pussy. You promised her you would be fast, and you are.  After only a few minutes, you empty your load into her as she gulps rapidly, trying to keep up with the stream of semen jetting out of your balls."
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_youth_32
              "As soon as your balls stop pulsing jizz into her mouth, [chelsea.name] escapes the bed and bustles herself off to get ready for work while you recover."
              $ chelsea.swallow_count += 1
            else:
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "Now??  I'm late for work."
                wt_image chubby_gf_event_6_bbw_25
                "You pull her t-shirt back off and pull her back onto the bed."
                player.c "Well, I did just wake you up, or you'd still be sleeping."
                wt_image chubby_gf_event_6_bbw_4
                "She drops to the floor in front of you and licks your cock."
                chelsea.c "Fine, but it needs to be quick."
                wt_image chubby_gf_event_6_bbw_5
                player.c "I guess that's up to you."
                wt_image chubby_gf_event_6_bbw_28
                "You'd like to make the sensation last, but unfortunately - fortunately? - she's too good with her mouth for you to last long when she's determined to get you to cum.  And right now, she's very determined.  After only a few minutes, you can't hold out any longer."
                $ title = "Where do you want to cum?"
                menu:
                  "In her":
                    wt_image chubby_gf_event_6_bbw_29
                    $ chelsea.swallow_count += 1
                  "On her":
                    wt_image chubby_gf_event_6_bbw_30
                    $ chelsea.facial_count += 1
                player.c "[player.orgasm_text]"
                "When your balls have finished pumping out their load, [chelsea.name] bustles herself off to get ready for work while you recover."
              else:
                wt_image chubby_gf_event_6_toned_28
                chelsea.c "Now??  I'm late for work."
                wt_image chubby_gf_event_6_toned_4
                player.c "Well, I did just wake you up, or you'd still be sleeping."
                chelsea.c "Okay, but it needs to be quick."
                wt_image chubby_gf_event_6_toned_5
                player.c "I guess that's up to you."
                wt_image chubby_gf_event_6_toned_29
                "[chelsea.name] pulls off her top, then pulls down your pants ..."
                wt_image chubby_gf_event_6_toned_30
                "... and takes your cock into her mouth."
                wt_image chubby_gf_event_6_toned_7
                "You'd like to make the sensation last, but unfortunately - fortunately? - she's too good with her mouth for you to last long when she's determined to get you to cum.  And right now, she's very determined."
                wt_image chubby_gf_event_6_toned_6
                "After only a few minutes, you can't hold out any longer."
                $ title = "Where do you want to cum?"
                menu:
                  "In her":
                    wt_image chubby_gf_event_6_toned_8
                    player.c "[player.orgasm_text]"
                    $ chelsea.swallow_count += 1
                  "On her":
                    wt_image chubby_gf_event_6_toned_9
                    player.c "[player.orgasm_text]"
                    $ chelsea.facial_count += 1
                "When your balls have finished pumping out their load, [chelsea.name] escapes the bed and bustles herself off to get ready for work while you recover."
            $ chelsea.blowjob_count += 1
            orgasm notify
          "Doggy style":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "[chelsea.your_name]!  I'm late for work!!"
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              wt_image chubby_gf_event_6_youth_15
              player.c "Get on your hands and knees.  I want to fuck my little girl from behind."
              wt_image chubby_gf_event_6_youth_33
              "She moans as you enter her.  You may have had to talk her into this quickie, but she's now fully engaged in it."
              wt_image chubby_gf_event_6_youth_16
              chelsea.c "Ahhhh  ... [chelsea.your_name], that feels so good!"
              wt_image chubby_gf_event_6_youth_17
              "You promised her fast, and you are.  So is she.  A few hard thrusts and you both shudder to climax, nearly simultaneously."
              chelsea.c "Aahhhhhh"
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_youth_12
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            else:
              if chelsea.has_tag('bbw'):
                player.c "Make love to me."
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "I don't have time to make love right now."
                wt_image chubby_gf_event_6_bbw_9
                "Wrapping your arms around her, you wrestle her into bed and insert a hand between her legs, caressing her sex."
                player.c "Okay, then.  How about we fuck instead?"
                chelsea.c "Oh!  Alright, but we have to be fast."
                wt_image chubby_gf_event_6_bbw_31
                "Rolling her over, you rip her clothes off her."
                wt_image chubby_gf_event_6_bbw_40
                "By the time she's naked, she's ready for you, her slit wet and waiting to be penetrated by your hard dick."
                wt_image chubby_gf_event_6_bbw_10
                chelsea.c "Ahhhh"
                "You promised her fast and you are.  So is she.  A few hard thrusts and you both shudder to climax, nearly simultaneously."
                wt_image chubby_gf_event_6_bbw_11
                chelsea.c "Aahhhhhh"
                player.c "[player.orgasm_text]"
                wt_image chubby_gf_event_6_bbw_24
                "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she dashes madly about trying to get ready for work as quickly as she can."
              else:
                wt_image chubby_gf_event_6_toned_28
                player.c "Make love to me."
                wt_image chubby_gf_event_6_toned_5
                chelsea.c "I don't have time to make love right now."
                wt_image chubby_gf_event_6_toned_10
                player.c "Okay then.  How about we fuck instead."
                wt_image chubby_gf_event_6_toned_31
                "You punctuate your comment by taking her nipple into her mouth and sucking it hard."
                wt_image chubby_gf_event_6_toned_11
                chelsea.c "Oh!  All right.  But we have to be fast."
                wt_image chubby_gf_event_6_toned_12
                "Rolling her onto her knees, you finish undressing her."
                wt_image chubby_gf_event_6_toned_32
                "By the time she's completely naked, she's ready for you, her slit wet and waiting to be penetrated by your hard dick."
                if chelsea.dominate_status == 8:
                  $ title = "Dominate her?"
                  menu:
                    "Yes":
                      $ chelsea.temporary_count = 1
                    "Not today":
                      pass
                if chelsea.temporary_count == 1:
                  $ chelsea.temporary_count = 0
                  wt_image chubby_gf_event_6_toned_33
                  chelsea.c "Ahhhh"
                  wt_image chubby_gf_event_6_toned_15
                  "Gripping her elbows firmly, you pull her arms back behind her back as you fuck her."
                  wt_image chubby_gf_event_6_toned_16
                  player.c "Okay, fucktoy.  You wanted this fast?  Show me how fast you can cum."
                  wt_image chubby_gf_event_6_toned_34
                  "Turns out the answer is pretty darn fast. A few hard thrusts and she shudders to climax, bringing you with her."
                  wt_image chubby_gf_event_6_toned_35
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_event_6_toned_34
                else:
                  wt_image chubby_gf_event_6_toned_13
                  chelsea.c "Ahhhh"
                  wt_image chubby_gf_event_6_toned_13
                  "You promised her fast, and you are.  So is she.  A few hard thrusts and she shudders to climax, bringing you with her."
                  wt_image chubby_gf_event_6_toned_36
                  chelsea.c "Aahhhhhh"
                  wt_image chubby_gf_event_6_toned_13
                player.c "[player.orgasm_text]"
                wt_image chubby_gf_event_6_toned_3
                "She enjoys the experience for less than a minute before scrambling off the bed. You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            $ chelsea.visit_count += 1
            orgasm notify
          "Missionary" if chelsea.has_tag('little_girl') or chelsea.has_tag('bbw'):
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "[chelsea.your_name]!  I'm late for work!!"
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              wt_image chubby_gf_event_6_youth_11
              player.c "Lie down on your back and spread your legs.  I want my little girl to watch me fuck her."
              wt_image chubby_gf_event_6_youth_36
              "She moans as you enter her.  You may have had to talk her into this quickie, but she's now fully engaged in it."
              wt_image chubby_gf_event_6_youth_35
              chelsea.c "Ahhhh!"
              wt_image chubby_gf_event_6_youth_37
              "Reaching a hand down between her legs, she rubs her clit as you fuck her. "
              wt_image chubby_gf_event_6_youth_19
              chelsea.c "Ahhhh  ... [chelsea.your_name], that feels so good!"
              wt_image chubby_gf_event_6_youth_37
              "You promised her fast, and you are.  So is she.  A few hard thrusts and you both shudder to climax, nearly simultaneously."
              wt_image chubby_gf_event_6_youth_20
              chelsea.c "Aahhhhhh"
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_youth_12
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she dashes madly about trying to get ready for work as quickly as she can."
            else:
              if chelsea.has_tag('bbw'):
                player.c "Make love to me."
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "I don't have time to make love right now."
                wt_image chubby_gf_event_6_bbw_9
                "Wrapping your arms around her, you wrestle her into bed and insert a hand between her legs, caressing her sex."
                player.c "Okay, then.  How about we fuck instead?"
                chelsea.c "Oh!  Alright, but we have to be fast."
                wt_image chubby_gf_event_6_bbw_32
                "Rolling her unto her back, you rip her clothes off her."
                wt_image chubby_gf_event_6_bbw_12
                "By the time she's naked, she's ready for you, her slit wet and waiting to be penetrated by your hard dick."
                wt_image chubby_gf_event_6_bbw_33
                "You promised her fast and you are, thrusting in-and-out of her as quick as you can."
                chelsea.c "Ahhhh"
                wt_image chubby_gf_event_6_bbw_13
                "Reaching down between her legs, [chelsea.name] rubs herself as you fuck her ..."
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_event_6_bbw_14
                "...and cums almost at the same time as you."
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_event_6_bbw_34
                player.c "[player.orgasm_text]"
                wt_image chubby_gf_event_6_bbw_24
                "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she dashes madly about trying to get ready for work as quickly as she can."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            $ chelsea.visit_count += 1
            orgasm notify
          "On her side":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "[chelsea.your_name]!  I'm late for work!!"
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              wt_image chubby_gf_event_6_youth_11
              player.c "Lie down on your side.  I want to snuggle up beside my little girl as I fuck her."
              wt_image chubby_gf_event_6_youth_39
              "She moans as you enter her."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_youth_40
              "You may have had to talk her into this quickie, but she's now fully engaged in it."
              wt_image chubby_gf_event_6_youth_41
              chelsea.c "Ahhhh  ... [chelsea.your_name], that feels so good!"
              wt_image chubby_gf_event_6_youth_42
              "You promised her fast, and you are.  So is she.  A few hard thrusts and she shudders to climax, bringing you with her."
              wt_image chubby_gf_event_6_youth_43
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_youth_44
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_youth_12
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            elif chelsea.has_tag('bbw'):
              player.c "Make love to me."
              wt_image chubby_gf_event_6_bbw_3
              chelsea.c "I don't have time to make love right now."
              wt_image chubby_gf_event_6_bbw_9
              "Wrapping your arms around her, you wrestle her into bed and insert a hand between her legs, caressing her sex."
              player.c "Okay, then.  How about we fuck instead?"
              chelsea.c "Oh!  Alright, but we have to be fast."
              wt_image chubby_gf_event_6_bbw_31
              "Rolling her onto her side, you rip her clothes off her."
              wt_image chubby_gf_event_6_bbw_35
              "By the time she's naked, she's ready for you, her slit wet and waiting to be penetrated by your hard dick."
              wt_image chubby_gf_event_6_bbw_36
              "You promised her fast and you are, thrusting in-and-out of her as quick as you can."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_bbw_37
              "Reaching down between her legs, [chelsea.name] rubs herself as you fuck her ..."
              chelsea.c "Ahhhhh"
              wt_image chubby_gf_event_6_bbw_38
              "... and cums almost at the same time as you."
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_bbw_39
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_bbw_24
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she dashes madly about trying to get ready for work as quickly as she can."
            else:
              wt_image chubby_gf_event_6_toned_28
              player.c "Make love to me."
              wt_image chubby_gf_event_6_toned_5
              chelsea.c "I don't have time to make love right now."
              wt_image chubby_gf_event_6_toned_10
              player.c "Okay then. How about we fuck instead."
              wt_image chubby_gf_event_6_toned_31
              "You punctuate your comment by taking her nipple into her mouth and sucking it hard."
              wt_image chubby_gf_event_6_toned_11
              chelsea.c "Oh!  All right.  But we have to be fast."
              wt_image chubby_gf_event_6_toned_17
              "Rolling her onto her side, you finish undressing her.  By the time she's completely naked, she's ready for you, her slit wet and waiting to be penetrated by your hard dick."
              wt_image chubby_gf_event_6_toned_18
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_toned_37
              "You promised her fast, and you are.  So is she.  A few hard thrusts and you're both ready to climax."
              wt_image chubby_gf_event_6_toned_38
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_toned_19
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_toned_3
              "She enjoys the experience for less than a minute before scrambling off the bed. You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            $ chelsea.visit_count += 1
            orgasm notify
          "Cowgirl":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              chelsea.c "[chelsea.your_name]!  I'm late for work!!"
              player.c "My little girl's not going to run off without looking after me, is she?"
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I guess not, but please be quick."
              wt_image chubby_gf_event_6_youth_11
              player.c "Get up on top of me.  I want to watch up my little girl make me feel good."
              wt_image chubby_gf_event_6_youth_45
              "A moment later, she settles onto your hard cock."
              wt_image chubby_gf_event_6_youth_46
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_youth_47
              "You may have had to talk her into this quickie, but she's now fully engaged in it.  She spins around while keeping you inside her ..."
              wt_image chubby_gf_event_6_youth_49
              "... then starts riding you up and down, faster and faster."
              wt_image chubby_gf_event_6_youth_48
              "You promised her fast, and you are.  So is she."
              wt_image chubby_gf_event_6_youth_50
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_youth_51
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_youth_12
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            elif chelsea.has_tag('bbw'):
              player.c "Make love to me."
              wt_image chubby_gf_event_6_bbw_3
              chelsea.c "I don't have time to make love right now."
              wt_image chubby_gf_event_6_bbw_9
              "Wrapping your arms around her, you wrestle her into bed and insert a hand between her legs, caressing her sex."
              player.c "Okay, then.  How about we fuck instead?"
              chelsea.c "Oh!  Alright, but we have to be fast."
              wt_image chubby_gf_event_6_bbw_19
              "Pulling her up on top of you, you rip her clothes off her."
              wt_image chubby_gf_event_6_bbw_15
              "By the time she's naked, she's ready for you.  Holding your cock steady with her hand, she settles down onto your hard dick."
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_bbw_41
              "Keeping your cock inside her, she spins around to face away from you ..."
              wt_image chubby_gf_event_6_bbw_42
              "... then starts riding you, up and down, faster and faster ..."
              wt_image chubby_gf_event_6_bbw_16
              "... her ass jiggling in front of your face as she fucks you."
              wt_image chubby_gf_event_6_bbw_17
              "She wanted this to be fast and she works hard to make that happen, slamming down on you hard, again and again."
              wt_image chubby_gf_event_6_bbw_43
              "Then [chelsea.name] reaches down between her legs and rubs herself as she fucks you ..."
              chelsea.c "Ahhhhh"
              wt_image chubby_gf_event_6_bbw_44
              "...and cums almost at the same time as you."
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_bbw_45
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_bbw_24
              "She enjoys the experience for less than a minute before scrambling off the bed.  You, on the other hand, get to take it easy and watch as she dashes madly about trying to get ready for work as quickly as she can."
            else:
              wt_image chubby_gf_event_6_toned_28
              player.c "Make love to me."
              wt_image chubby_gf_event_6_toned_5
              chelsea.c "I don't have time to make love right now."
              wt_image chubby_gf_event_6_toned_10
              player.c "Okay then. How about we fuck instead."
              wt_image chubby_gf_event_6_toned_31
              "You punctuate your comment by taking her nipple into her mouth and sucking it hard."
              wt_image chubby_gf_event_6_toned_11
              chelsea.c "Oh!  All right.  But we have to be fast."
              wt_image chubby_gf_event_6_toned_39
              "Pulling her up on top of you, you rip her clothes off her. By the time she's naked, she's ready for you. You help hold her steady as she settles down on you, penetrating her wet slit with your hard dick."
              wt_image chubby_gf_event_6_toned_20
              chelsea.c "Ahhhh"
              wt_image chubby_gf_event_6_toned_21
              "You promised her fast, and you are.  So is she."
              wt_image chubby_gf_event_6_toned_40
              "Up and down she goes on your cock, up and down, faster and faster, and before long you're both ready to climax ..."
              wt_image chubby_gf_event_6_toned_22
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_toned_41
              player.c "[player.orgasm_text]"
              wt_image chubby_gf_event_6_toned_3
              "She enjoys the experience for less than a minute before scrambling off the bed. You, on the other hand, get to take it easy and watch as she bustles about trying to get ready for work as quickly as she can."
            $ chelsea.sex_count += 1
            $ chelsea.orgasm_count += 1
            $ chelsea.visit_count += 1
            orgasm notify
          "Pleasure her":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_2
              chelsea.c "[chelsea.your_name], that's sweet, but I don't have time right now.  I'm late for work!!"
              player.c "Sure you do.  Let's get you out of those clothes."
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "I might take a while. I just woke up and I need to get going."
              player.c "Trust me, little girl.  It won't take you long."
              wt_image chubby_gf_event_6_youth_21
              "You may have had to talk her into this quickie, but by the time your fingers brush gently along her sex, she's fully engaged in it."
              chelsea.c "Ahhhh  ... [chelsea.your_name], that feels so good!  I love how hard your cock gets when you're teasing me."
              wt_image chubby_gf_event_6_youth_22
              "Her slit is wet and her clit sensitive as you turn her onto her knees and push a finger inside her ..."
              chelsea.c "Ahhhhh"
              wt_image chubby_gf_event_6_youth_23
              "... so sensitive that she soon proves you right, cumming quickly as you flick your tongue and fingers back and forth across her sex."
              chelsea.c "Aahhhhhh"
              wt_image chubby_gf_event_6_youth_38
              "She enjoys the experience for less than a minute before scrambling off the bed.  Still tasting her pussy juice on your tongue, you watch as she bustles about trying to get ready for work as quickly as she can."
            else:
              if chelsea.has_tag('bbw'):
                player.c "Let me make you feel good."
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "I don't have time right now."
                wt_image chubby_gf_event_6_bbw_9
                "Wrapping your arms around her, you wrestle her into bed and insert a hand between her legs, caressing her sex."
                player.c "Sure you do."
                chelsea.c "Oh!  I might take a while.  I just woke up and I need to get going."
                wt_image chubby_gf_event_6_bbw_46
                player.c "You're not going to take very long."
                chelsea.c "But ..."
                wt_image chubby_gf_event_6_bbw_18
                "You silence her with a kiss. All attempts at protest cease as you work a finger inside her, making her moan into your mouth."
                chelsea.c "nnnnn"
                wt_image chubby_gf_event_6_bbw_19
                "Sitting her upright, you remove her t-shirt and caress her tits as you kiss the back of her neck."
                chelsea.c "Oh!"
                wt_image chubby_gf_event_6_bbw_47
                "Then lying her down, you take a nipple into your mouth as you caress her her pussy through her panties before removing them."
                wt_image chubby_gf_event_6_bbw_20
                chelsea.c "Ahhhh"
                $ title = "How do you want to eat her out?"
                menu:
                  "On her back like this is good":
                    wt_image chubby_gf_event_6_bbw_21
                    "Pulling her panties off, you lower your head between her spread legs."
                    wt_image chubby_gf_event_6_bbw_48
                    "You were right, she does cum fast, her sex pressed hard against your mouth, your tongue buried deep inside her."
                  "Have her ride your face":
                    wt_image chubby_gf_event_6_bbw_22
                    "Rolling over on your back, you guide her up on top of you. She's confused at first, until using your hands on her ass, you pull her up closer, pressing her sex right against your face."
                    wt_image chubby_gf_event_6_bbw_49
                    "You were right, she does cum fast, as your tongue flicks in-and-out of her slit and back-and-forth against her hard clit."
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_event_6_bbw_24
                "She enjoys the experience for less than a minute before scrambling off the bed.  Her pussy juice still glistening on your mouth and chin, you watch as she dashes madly about trying to get ready for work as quickly as she can."
              else:
                wt_image chubby_gf_event_6_toned_28
                player.c "Let me make you feel good."
                wt_image chubby_gf_event_6_toned_5
                chelsea.c "That's sweet, but I don't have time right now."
                wt_image chubby_gf_event_6_toned_31
                player.c "Sure you do."
                chelsea.c "Oh!  I might take a while.  I just woke up and I need to get going."
                wt_image chubby_gf_event_6_toned_11
                player.c "You're not going to take very long."
                wt_image chubby_gf_event_6_toned_43
                chelsea.c "But ..."
                wt_image chubby_gf_event_6_toned_42
                "You put an end to her protests by flicking tongue across and then gently biting her erect nipple, making her throw her head back and moan."
                wt_image chubby_gf_event_6_toned_23
                chelsea.c "Ahhhh"
                wt_image chubby_gf_event_6_toned_24
                "You finish undressing her and spread her legs. Her slit is wet and her clit sensitive as you gently run your fingers across it ..."
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_event_6_toned_26
                "... so sensitive that she soon proves you right when you told her she wouldn't take long.  You bring her clit to attention with a few long licks along her slit ..."
                wt_image chubby_gf_event_6_toned_25
                chelsea.c "Ahhhhh"
                wt_image chubby_gf_event_6_toned_44
                "... then bring her to a quick orgasm at the end of your tongue as you flick it back and forth across her clit."
                wt_image chubby_gf_event_6_toned_45
                chelsea.c "Aahhhhhh"
                wt_image chubby_gf_event_6_toned_3
                "She enjoys the experience for less than a minute before scrambling off the bed.  Still tasting her pussy juice on your tongue, you watch as she bustles about trying to get ready for work as quickly as she can."
            $ chelsea.pleasure_her_count += 1
            $ chelsea.orgasm_count += 1
            $ chelsea.visit_count += 1
            change player energy by -energy_short notify
          "Suggest a few more minutes in bed" if not chelsea.has_tag('chelsea_gf_event_10_menu_choice'):
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_1
              player.c "No need to get up yet."
              wt_image chubby_gf_event_6_youth_27
              chelsea.c "Yes, there is.  I'm already late!  I'd better call the office."
              player.c "Okay, so if you're already 5 minutes late, does it really matter if you end up 15 minutes late?  Stay in bed for a few minutes."
              wt_image chubby_gf_event_6_youth_4
              chelsea.c "And do what?"
            else:
              if chelsea.has_tag('bbw'):
                player.c "What's the rush?"
                wt_image chubby_gf_event_6_bbw_24
                chelsea.c "I'm already late!  Shit, where'd I'd put my eyeliner?"
                player.c "Okay, so if you're already 5 minutes late, does it really matter if you end up 15 minutes late?  Come back to bed for a few minutes."
                wt_image chubby_gf_event_6_bbw_3
                chelsea.c "And do what?"
              else:
                wt_image chubby_gf_event_6_toned_28
                player.c "No need to get up yet."
                chelsea.c "Yes there is.  I'm already late!"
                wt_image chubby_gf_event_6_toned_2
                player.c "Okay, so if you're already 5 minutes late, does it really matter if you end up 15 minutes late?  Stay in bed for a few minutes."
                chelsea.c "And do what?"
            add tags 'chelsea_gf_event_10_menu_choice' to chelsea
            jump menu_chelsea_gf_event_10
          "Tell her to get more sleep" if chelsea.has_tag('chelsea_gf_event_10_menu_choice'):
            if chelsea.has_tag('little_girl'):
              player.c "You should get more sleep.  You've been working too much lately."
              wt_image chubby_gf_event_6_youth_3
              chelsea.c "Thanks for your concern, [chelsea.your_name], but I don't need more sleep.  I've already slept in.  I need to get showered, dressed and off to work ... Bye!"
            else:
              if chelsea.has_tag('bbw'):
                player.c "You should get more sleep.  You've been working too much lately."
                wt_image chubby_gf_event_6_bbw_24
                chelsea.c "I don't need more sleep, I've already slept in.  I need to get to the office.  Bye!"
                "She bustles off to get herself ready for work."
              else:
                player.c "You should get more sleep. You've been working too much lately."
                wt_image chubby_gf_event_6_toned_3
                chelsea.c "I don't need more sleep, I've already slept in.  I need to get showered, dressed and off to work ... Bye!"
          "Let her go to work":
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_6_youth_3
              "A flustered [chelsea.name] pulls off her sleep wear and bustles off to get to the office as quickly as she can."
            else:
              if chelsea.has_tag('bbw'):
                wt_image chubby_gf_event_6_bbw_24
                chelsea.c "Thanks for waking me!"
                "A flustered [chelsea.name] bustles off to get to the office as quickly as she can."
              else:
                wt_image chubby_gf_event_6_toned_3
                chelsea.c "Thanks for waking me!  I need to get showered, dressed and off to work."
                "A flustered [chelsea.name] pulls off her sleep wear and bustles off to get to the office as quickly as she can."
        call forced_movement(living_room) from _call_forced_movement_282
        call character_location_return(chelsea) from _call_character_location_return_103
    # lesbian threesome
    elif chelsea.gf_event == 12:
        if chelsea.lesbian_threesome_count == 2 or chelsea.lesbian_threesome_count == 3:
          call forced_movement(living_room) from _call_forced_movement_283
          summon chelsea no_follows
          summon faye no_follows
          wt_image chubby_threesome_1_25
          "As you enter the living room, you see [chelsea.name] sitting on the sofa with Faye."
          chelsea.c "Look who dropped by!"
          wt_image chubby_threesome_1_59
          if chelsea.lesbian_threesome_count == 2:
            chelsea.c "Faye and I were talking and I mentioned how unfair it was that I got to fuck her husband, but Faye didn't even get to see you naked."
          else:
            chelsea.c "Faye and I were talking and she mentioned how fun it was the last time when we blew you."
          wt_image chubby_threesome_1_26
          chelsea.c "So I suggested that if she wanted, I'd let her suck your fat dick with me.  What do you say, [chelsea.your_name]?  Will you let Faye and I blow you?"
          $ title = "Do you want them to suck your dick?"
          menu:
            "Absolutely":
              $ chelsea.lesbian_threesome_count = 3
              $ chelsea.training_session()
              wt_image chubby_threesome_1_60
              "The two women settle themselves on their knees in front of you and take out your cock."
              wt_image chubby_threesome_1_27
              " [chelsea.name] takes you into her mouth as Faye licks up your shaft ..."
              wt_image chubby_threesome_1_28
              "... and around your balls ..."
              wt_image chubby_threesome_1_61
              "... before tea bagging you as [chelsea.name] pleasures your cock."
              wt_image chubby_threesome_1_62
              "Then they switch positions ..."
              wt_image chubby_threesome_1_30
              "... and [chelsea.name] suckles your balls while Faye sucks your cock until you've taken as much of their teasing as you can tolerate."
              wt_image chubby_threesome_1_31
              $ title = "Where do you want to cum?"
              menu:
                "In Faye":
                  wt_image chubby_threesome_1_63
                  player.c "[player.orgasm_text]"
                  wt_image chubby_threesome_1_64
                  $ faye.blowjob_count += 1
                  $ faye.swallow_count += 1
                "In [chelsea.name]":
                  wt_image chubby_threesome_1_29
                  player.c "[player.orgasm_text]"
                  wt_image chubby_threesome_1_65
                  $ chelsea.blowjob_count += 1
                  $ chelsea.swallow_count += 1
                "On both of them":
                  wt_image chubby_threesome_1_32
                  "The two women take off their tops and present their breasts to you ..."
                  wt_image chubby_threesome_1_66
                  "... a four-set of giant targets you couldn't possibly miss."
                  wt_image chubby_threesome_1_33
                  player.c "[player.orgasm_text]"
                  wt_image chubby_threesome_1_34
              faye.c "Thanks for the fun time!"
              player.c "Likewise"
              if chelsea.has_tag('likes_girls'):
                wt_image chubby_threesome_1_67
                "On her way out, Faye leans in for a kiss that [chelsea.name] happily accepts.  It's nice that she's so comfortable with other women, and willing to share your cock with them."
              orgasm notify
            "Not today":
              player.c "Tempting offer, ladies, but I have an incredibly busy day ahead of me. Perhaps another time?"
            "Never (shuts this off)":
              if chelsea.lesbian_threesome_count == 2:
                "Faye's a Club member, so you have to be somewhat tactful, especially as [chelsea.name] invited her here to have sex with you."
                player.c "Sorry, ladies.  I have a crazy busy day ahead of me.  Thanks for the offer, though."
                "The next time you see [chelsea.name] alone, you tell her you don't want that woman anywhere near your dick.  No future invitations should be coming."
              else:
                "Getting blown by the two of them was fun, but it's getting tiring.  You tactfully decline their offer and later let [chelsea.name] know that you'd rather she not invite Faye over again."
              $ chelsea.lesbian_threesome_count += 2
          call character_location_return(chelsea) from _call_character_location_return_104
          call character_location_return(faye) from _call_character_location_return_105
        else:
          jump chelsea_girlfriend_event
    # bathroom event
    elif chelsea.gf_event == 13:
        call forced_movement(bathroom) from _call_forced_movement_284
        summon chelsea no_follows
        $ chelsea.training_session()
        wt_image chubby_gf_event_5_1
        "You hear [chelsea.name] calling from the bathroom."
        chelsea.c "Shit!!  The bathroom sink is clogged!"
        wt_image chubby_gf_event_5_2
        player.c "[chelsea.name], have you been washing your hair in the sink?"
        chelsea.c "What?  No ... maybe."
        player.c "Your hair is too long for that.  You can't wash it out in the sink.  The drain will keep clogging if you do."
        wt_image chubby_gf_event_5_21
        chelsea.c "Sometimes I don't have time to take a shower before going to work.  Can you fix it?"
        $ chelsea.gf_event_12_menu_choice = False
        $ title = "What do you do?"
        menu menu_chelsea_gf_event_12:
          "Spank her" if (chelsea.has_tag('little_girl') or chelsea.spanked == 2) and not chelsea.gf_event_12_menu_choice:
            if chelsea.has_tag('little_girl'):
              wt_image chubby_gf_event_5_25
              player.c "That was totally irresponsible, young lady.  You haven't been thinking, you've taken short cuts, and now you've made a big mess that's going to have to be fixed up."
              chelsea.c "I'm sorry, [chelsea.your_name]."
              wt_image chubby_gf_toned_1_3
              player.c "Sorry isn't good enough.  Get that robe off and lean over the dresser."
              wt_image chubby_gf_toned_1_4
              "As soon as she's in position, you begin the spanking ... *smack* ... *smack* ... *smack*"
            else:
              wt_image chubby_gf_event_5_23
              player.c "That was totally irresponsible, [chelsea.name]. You should know better, and now you've made a big mess that's going to have to be fixed up. Get that robe off and lean over the dresser."
              chelsea.c "What? Why??"
              wt_image chubby_gf_event_5_22
              player.c "I'm going to punish you by giving you a spanking."
              chelsea.c "Punish me?  I'm not a child!"
              wt_image chubby_gf_toned_1_3
              player.c "Then you shouldn't have acted like one, washing your hair in the sink when you're old enough to know better.  Now present your ass to me for your spanking before you earn a longer one."
              "[chelsea.name]'s flustered and confused. She doesn't want to be punished, but she knows she did mess up.  And she's used to you dominating her sexually, so she's not completely surprised that you're letting your anger manifest in a spanking."
              wt_image chubby_gf_toned_1_4
              "She would never have voluntarily sought out a relationship where she's subject to domestic discipline, but the nature of your relationship has evolved such that she finds herself meekly laying over the desk and presenting her bare ass to you ... *smack* ... *smack* ... *smack*"
            wt_image chubby_gf_event_5_26
            chelsea.c "ow"
            wt_image chubby_gf_toned_1_4
            $ chelsea.temporary_count = 3
            $ title = "Spank her again?"
            menu menu_chelsea_gf_event_12_spank_menu:
              "Yes":
                $ chelsea.temporary_count += 1
                wt_image chubby_gf_event_5_27
                "*smack*"
                wt_image chubby_gf_event_5_26
                if chelsea.temporary_count < 5:
                  chelsea.c "Ow!"
                elif chelsea.temporary_count < 10:
                  chelsea.c "Oww!"
                elif chelsea.temporary_count < 15:
                  chelsea.c "Owww!!"
                elif chelsea.temporary_count < 20:
                  chelsea.c "oh ... ooowwww!!"
                if chelsea.temporary_count < 20:
                  wt_image chubby_gf_toned_1_4
                  jump menu_chelsea_gf_event_12_spank_menu
                else:
                  chelsea.c "OOWWW!!!  I'm sorry!!  I'm sorry, I've learned my lesson!!  Please don't spank me anymore, [chelsea.your_name]!!"
                  wt_image chubby_gf_event_5_27
                  "*smack*"
                  wt_image chubby_gf_event_5_3
                  chelsea.c "OW OWW OOWWW!!!"
                  player.c "I hope you're telling the truth, and that you've learned your lesson and I don't have to do this again."
                  chelsea.c "I have.  I promise."
              "No, that's enough":
                  player.c "I hope you've learned your lesson and I don't have to do this again."
                  wt_image chubby_gf_event_5_3
                  chelsea.c "I have.  I promise."
            if chelsea.has_tag('little_girl'):
              "She's upset at being disciplined, but secretly pleased at having you treat her like a naughty little girl."
            else:
              "She's upset at being disciplined, but with how you've conditioned her, she can't bring herself to blame you. Instead, she internalizes her displeasure with herself, for doing something that upset you enough that you felt the need to spank her."
            $ chelsea.spank_count += 1
            $ chelsea.gf_event_12_menu_choice = True
            jump menu_chelsea_gf_event_12
          "Fix the plumbing (costs [energy_short.value] Energy)" if not chelsea.gf_event_12_menu_choice:
            wt_image chubby_gf_event_5_28
            "You collect your tools from the basement and take a look under the sink."
            wt_image chubby_gf_event_5_4
            chelsea.c "Is it going to be hard to fix?"
            player.c "I don't think so. It's just going to take some time. I need to shut off the water and get this drain apart to clear it."
            wt_image chubby_gf_event_5_5
            chelsea.c "Would it make the job more fun if I flashed you while you're working?"
            $ title = "What do you say?"
            menu:
              "Sure":
                player.c "Sure.  I won't say no to look at your body."
                wt_image chubby_gf_event_5_29
                "[chelsea.name] makes sure you have a nice view whenever you look up from you work.  It's her way of saying 'sorry' for getting the drain clogged up, but she also seems to be enjoying watching you work."
                chelsea.c "It's sweet of you to fix this, and it's kind of sexy that you know how."
              "No, but a blow job would":
                wt_image chubby_gf_event_5_14
                "She squats down as you stand up and removes your cock from your pants ..."
                wt_image chubby_gf_event_5_30
                "... gives it a playful lick ..."
                wt_image chubby_gf_event_5_31
                "... and pops it into her mouth."
                $ title = "Take control?"
                menu:
                  "No, let her pleasure you":
                    wt_image chubby_gf_event_5_15
                    "She was impressed by how well you could handle your plumbing tools.  Now she wants to show you how well she can handle your tool."
                    wt_image chubby_gf_event_5_42
                    "Pretty well, as it turns out.  Between her tongue, her lips, and her hand pleasuring your balls and cock, you're soon ready to cum."
                    wt_image chubby_gf_event_5_32
                  "Yes, fuck her face":
                    wt_image chubby_gf_event_5_33
                    "This meant to be an apology and a 'thank you', so you make sure [chelsea.name] knows you're going to enjoy her mouth the way you want to enjoy it.  Placing a hand on the back of her head you hold her still ..."
                    wt_image chubby_gf_event_5_34
                    "... and fuck her face until you're ready to cum."
                    wt_image chubby_gf_event_5_33
                $ title = "Where do you want to cum?"
                menu:
                  "In her mouth":
                    wt_image chubby_gf_event_5_16
                    player.c "[player.orgasm_text]"
                    "It's not easy, but [chelsea.name] gulps down your spunk as quickly as you spurt it into her."
                    $ chelsea.swallow_count += 1
                  "On her face":
                    wt_image chubby_gf_event_5_17
                    "As you remove your cock, she looks up at you expectantly, knowing what comes next."
                    wt_image chubby_gf_event_5_18
                    player.c "[player.orgasm_text]"
                    $ chelsea.facial_count += 1
                player.c "That was nice, [chelsea.name]. Time for me to get back to fixing the sink."
                "She pulls herself back together while you get back to the repairs.  She seems pleased and impressed that you took the time to fix the plumbing issue yourself, and that you wanted to enjoy her mouth before doing so."
                $ chelsea.blowjob_count += 1
                orgasm
              "No, but fucking you would":
                wt_image chubby_gf_event_5_35
                player.c "If you've going to flash that at me, I assume you're willing to let me use it."
                wt_image chubby_gf_event_5_7
                chelsea.c "I am!"
                $ title = "How do you position her?"
                menu:
                  "Facing you":
                    wt_image chubby_gf_event_5_36
                    "You pick her up and lift her onto the counter.  She immediately spreads her legs, letting you plow into her.  She was already aroused seeing how well you could use your plumbing tools ..."
                    wt_image chubby_gf_event_5_12
                    chelsea.c "Ahhhh"
                    wt_image chubby_gf_event_5_37
                    "... it takes you no time at all to bring her to the edge of climax, now that you're using your big tool ..."
                    wt_image chubby_gf_event_5_11
                    chelsea.c "Ahhhhh"
                    wt_image chubby_gf_event_5_38
                    "... and even less time to finish the job."
                    chelsea.c "Aahhhhhh"
                    wt_image chubby_gf_event_5_13
                    player.c "[player.orgasm_text]"
                  "Facing away":
                    wt_image chubby_gf_event_5_8
                    "Turning her around, you bend her over the counter and plow into her."
                    chelsea.c "Ahhhh"
                    if chelsea.dominate_status == 8:
                      $ title = "Dominate her?"
                      menu:
                        "Yes":
                          $ chelsea.temporary_count = 1
                        "Not today":
                          pass
                    if chelsea.temporary_count == 1:
                      $ chelsea.temporary_count = 0
                      wt_image chubby_gf_event_5_10
                      "Gripping her by the hair, you bring your hand down sharply on her butt ... *SMACK*"
                      chelsea.c "Ow!"
                      player.c "This is for creating extra work, fucktoy."
                      wt_image chubby_gf_event_5_40
                      "You spank her as you fuck her, her moans of discomfort turning quickly into moans of pleasure ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                      chelsea.c "Oww!!  Oowww!  Ow ahhh!  Ahhhhh"
                      wt_image chubby_gf_event_5_10
                      player.c "Cum for me, fucktoy.  Cum as I punish you."
                      "*SMACK*  *SMACK*  *SMACK*"
                      wt_image chubby_gf_event_5_41
                      chelsea.c "Aahhhhhh"
                      wt_image chubby_gf_event_5_40
                      player.c "[player.orgasm_text]"
                      "Once in a while, at times like this, she doesn't mind being used as your fucktoy."
                    else:
                      wt_image chubby_gf_event_5_9
                      "She was already aroused seeing how well you could use your plumbing tools ..."
                      chelsea.c "Ahhhhh"
                      wt_image chubby_gf_event_5_39
                      "... it takes you no time at all to get her to climax, now that you're using your big tool."
                      chelsea.c "Aahhhhhh"
                      wt_image chubby_gf_event_5_8
                      player.c "[player.orgasm_text]"
                wt_image chubby_gf_event_5_6
                "When you've finished spurting your seed inside her, you get back to the other plumbing work, and finish up the sink. It takes some effort, but [chelsea.name]'s impressed that you fix it yourself. That you did so while your cum was dripping out of her only makes the whole experience more arousing for her."
                $ chelsea.sex_count += 1
                $ chelsea.orgasm_count += 1
                $ chelsea.visit_count += 1
                orgasm
              "I'm trying to work":
                player.c "[chelsea.name], I'm trying to fix this mess you made.  Let me work."
                wt_image chubby_gf_event_5_4
                chelsea.c "I know.  Thank you.  Sorry I made extra work for you, [chelsea.your_name].  You're sweet to fix it, and it's kind of sexy that you know how."
                player.c "Working, [chelsea.name]."
                wt_image chubby_gf_event_5_6
                chelsea.c "I know.  I know.  I'll leave you alone.  You do look hot doing that, though."
            sys "[chelsea.name] is happier with your relationship."
            $ chelsea.relationship_counter += 0.5
            change player energy by -energy_short notify
          "Fix it yourself (costs [energy_short.value] Energy)" if chelsea.gf_event_12_menu_choice:
            player.c "Stay there and think about what you've done while I go fix up the mess you've made."
            wt_image chubby_gf_toned_1_4
            chelsea.c "Okay, [chelsea.your_name]. Thank you."
            "It won't take you too long to fix it, but it's still an annoying chore that takes up part of your day."
            change player energy by -energy_short notify
          "Pay for a plumber (costs 25)" if player.money - player.min_money >= 25:
            player.c "I'll call a plumber.  This is costing us money, you know."
            wt_image chubby_gf_event_5_22
            chelsea.c "I know. I'm sorry, [chelsea.your_name]. Thank you for looking after it!"
            sys "[chelsea.name] is happier with your relationship."
            change player money by -25 notify
            $ chelsea.relationship_counter += 0.5
          "Tell her to pay for a plumber":
            if chelsea.has_tag('little_girl'):
              player.c "I'll call a plumber, but you're paying for his service."
              wt_image chubby_gf_event_5_22
              chelsea.c "Me?"
              player.c "Yes you, young lady.  Take it out of your allowance."
              chelsea.c "You don't pay me an allowance!"
              player.c "Take it out of the money you make at work, then."
              wt_image chubby_gf_event_5_23
              chelsea.c "Fine"
            else:
              player.c "I'll call a plumber, but you're paying for his service."
              wt_image chubby_gf_event_5_22
              chelsea.c "Me?"
              player.c "Yes, you.  Unless you think he's going to find some reason why the clog was not related to your hair?"
              wt_image chubby_gf_event_5_23
              chelsea.c "Fine"
        call forced_movement(living_room) from _call_forced_movement_285
        call character_location_return(chelsea) from _call_character_location_return_106
    $ chelsea.event_week = week
    $ chelsea.random_number = renpy.random.randint(1, 10)
    if chelsea.random_number < 3:
        $ chelsea.event_week += 1
    elif chelsea.random_number < 7:
        $ chelsea.event_week += 2
    else:
        $ chelsea.event_week += 3
    # speed up event if anal training or youth events in progress or event skipped
    if chelsea.anal_status == 4 or chelsea.temporary_count == 1 or chelsea.youth_status < 4:
        $ chelsea.event_week -= 2
    $ chelsea.temporary_count = 0
    return

label chelsea_gf_event_6_playful_spanking:
    wt_image chubby_youth_3_11
    player.c "You've been a very naughty girl, showing off your sexy body this way."
    "*smack*"
    wt_image chubby_youth_3_40
    chelsea.c "I'm sorry. I promise I'll be good."
    "*smack*"
    wt_image chubby_youth_3_41
    player.c "This won't do.  Remove your top and pull down your panties."
    wt_image chubby_youth_3_42
    chelsea.c "Umm, you're making me show off more of my body."
    player.c "Don't talk back to me, young lady."
    wt_image chubby_youth_3_19
    chelsea.c "I'm sorry, I guess I do need this spanking."
    wt_image chubby_youth_3_43
    "She giggles as you resume the 'spanking' ... *smack*  ... *smack* ... *smack*"
    wt_image chubby_youth_3_44
    chelsea.c "Ouch!  Oh, please don't spank me any more, I promise I'll be good.  Really, I will."
    wt_image chubby_youth_3_14
    "She's still grinning as you finish."
    wt_image chubby_youth_3_15
    chelsea.c "Ohh, my bum is sore!"
    player.c "Not yet it isn't, but I could make it sore."
    wt_image chubby_youth_3_16
    chelsea.c "No!! You don't have to do that. I'll be a good little girl, I promise.  Thank you for loving me enough to spank me for dressing so slutty."
    sys "[chelsea.name] is happier with your relationship."
    $ chelsea.relationship_counter += 1
    $ chelsea.youth_skirt_spanking = 1
    return

label chelsea_gf_event_6_hard_spanking:
    wt_image chubby_youth_3_36
    "[chelsea.name]'s not surprised when you expose her before pushing her back over the desk.  She could tell from the look in your eye that you were planning on making this a serious punishment."
    wt_image chubby_youth_3_37
    "Pulling down her panties, you lay into her ..."
    wt_image chubby_youth_3_38
    "*SMACK* ... *SMACK* ... *SMACK* ... *SMACK* ... *SMACK*"
    wt_image chubby_youth_3_18
    "She holds out for a while, but eventually the pain from the spanking gets too much and she cries out, reaching back with her hands to shield her sore ass."
    chelsea.c "Oww ow ow!"
    wt_image chubby_youth_3_17
    player.c "Take your hands away."
    wt_image chubby_youth_3_38
    "When she reluctantly removes her hands.  Once they're out of the way, you resume the spanking ... *SMACK* ... *SMACK* ... *SMACK* ... *SMACK* ... *SMACK*"
    chelsea.c "OWWW  Owww  Owww  Owww !!!"
    # NOTE: finish is back from where label is called
    return

# Convert Character to Girlfriend
label chelsea_convert_girlfriend:
  call convert(chelsea,"girlfriend") from _call_convert_72
  ## this is just to avoid future potential problems if she becomes girlfriend without completing training
  if not chelsea.has_tag('toned') and not chelsea.has_tag('bbw'):
    if chelsea.has_tag('motivated'):
      add tags 'toned' to chelsea
    else:
      add tags 'bbw' to chelsea
  $ chelsea.training_regime = 'daily'
  $ chelsea.relationship_counter += 3
  $ chelsea.event_week = week
  add tags 'post_continuing_actions' 'swingers_room_possible' to chelsea
  rem tags 'continuing_actions' 'follows' from chelsea
  $ chelsea.fixed_location = bedroom
  $ chelsea.location = bedroom
  return

# Convert Character to Hypno-Girlfriend
label chelsea_convert_hypno_girlfriend:
  if chelsea.has_tag('girlfriend'):
    call unconvert (chelsea, 'girlfriend') from _call_unconvert_23
  call convert(chelsea,"hypno_girlfriend") from _call_convert_73
  ## this is just to avoid future potential problems if she becomes hypno_girlfriend without completing training
  if not chelsea.has_tag('toned') and not chelsea.has_tag('bbw'):
    if chelsea.has_tag('motivated'):
      add tags 'toned' to chelsea
    else:
      add tags 'bbw' to chelsea
  $ chelsea.training_regime = 'daily'
  $ chelsea.relationship_counter += 3
  $ chelsea.event_week = week
  $ chelsea.fixed_location = bedroom
  $ chelsea.location = bedroom
  rem tags 'continuing_actions' 'follows' from chelsea
  add tags 'post_continuing_actions' 'swingers_room_possible' to chelsea
  # give hypno-girlfriend the benefit of hypnosis-induced openness to various activities
  $ chelsea.hypno_re_anal = 2
  $ chelsea.hypno_re_dominate = 2
  $ chelsea.hypno_re_lesbian = 2
  return

# Convert Character to Slavegirl
label chelsea_convert_slavegirl:
  $ chelsea.training_regime = 'daily'
  if chelsea.has_tag('girlfriend'):
    call unconvert(chelsea,'girlfriend') from _call_unconvert_24
  if chelsea.has_tag('hypno_girlfriend'):
    call unconvert(chelsea,'hypno_girlfriend') from _call_unconvert_25
  call convert(chelsea,"slavegirl") from _call_convert_74
  $ chelsea.prefix = "Slave"
  $ chelsea.suffix = ""
  $ chelsea.fixed_location = bedroom
  $ chelsea.location = bedroom
  $ chelsea.action_sg_elsa = chelsea.add_action("Watch her play with [elsa.full_name]", label = "_elsa_sg", condition = "elsa.has_tag('slavegirl') and elsa.can_be_interacted and not elsa.has_tag('holding_position') and chelsea.in_area('house') and chelsea.has_tag('slavegirl') and chelsea.can_be_interacted")
  rem tags 'continuing_actions' 'follows' from chelsea
  add tags 'post_continuing_actions' to chelsea
  if chelsea.lee_event_status == 3:
    $ chelsea.lee_event_status = 1
  if chelsea.lee_event_status > 3:
    $ chelsea.lee_event_status = 2
  return

# Description Display
label chelsea_description_display:
    if chelsea.status == "post_training":
        call chelsea_update_media from _call_chelsea_update_media
        wt_image chelsea.image
        # main description
        if 'girlfriend' in chelsea.tags:
            if chelsea.has_tag('little_girl'):
                "[chelsea.name] the Chubby has become [chelsea.name] the Little Girl, at least when she's around your house. She's happy with her body and with herself, and enjoys an active sex life."
            elif chelsea.has_tag('toned'):
                "[chelsea.name] the Chubby has become [chelsea.name] the Toned, and your girlfriend. She's fit, healthy, happy with her body, and enjoys an active sex life."
            else:
                "[chelsea.name] the Chubby has become [chelsea.name] the BBW, and your girlfriend. She's happy with her body and with herself, and enjoys an active sex life.  Her weight still fluctuates, but she no longer worries about that."
        elif 'hypno_girlfriend' in chelsea.tags:
            "You've convinced [chelsea.name] that she's your girlfriend.  As you long as you invest energy each week, she'll continue to believe you."
        elif 'slavegirl' in chelsea.tags:
            "[chelsea.full_name] wasn't a particularly submissive woman when you met her. Under your influence, however, she's become your devoted slavegirl."
        elif chelsea.has_tag('continuing_actions'):
            if chelsea.has_tag('toned'):
                "[chelsea.name] the Chubby has become [chelsea.name] the Toned. She's fit, healthy, happy with her body, and enjoying an active sex life with her husband."
            elif chelsea.has_tag('bbw'):
                "[chelsea.name] the Chubby has become [chelsea.name] the BBW. She's happy with her body and with herself, and enjoying an active sex life with her husband.  Her weight still fluctuates, but she no longer worries about that."
        if chelsea.has_tag('likes_girls'):
            "When the mood strikes her or you, [chelsea.name] will sleep with other women while you watch."
        if chelsea.anal_status == 6:
            "She doesn't really enjoy it, but when the mood strikes you, she'll even let you put your dick in her ass, a big change for a woman who when she met you wouldn't let anyone anywhere near her butt."
        # relationship status
        if chelsea.has_tag('girlfriend'):
            if chelsea.relationship_counter > 4:
                "She's very happy with her relationship with you."
            elif chelsea.relationship_counter > 2:
                "She has some concerns about her relationship with you.  She worries about whether you're able - or want - to spend as much time with her as she'd like, and she wonders if she can really be the girlfriend you want her to be."
            else:
                "She's very concerned about her relationship with you.  She wonders if she made the right choice in becoming your girlfriend, and is contemplating making a change."
        elif chelsea.has_tag('continuing_actions'):
            if chelsea.relationship_counter > 9:
                if chelsea.visit_talk_count > chelsea.visit_sex_count:
                    $ chelsea.temporary_count = chelsea.visit_sex_count*2
                    if chelsea.visit_talk_count > chelsea.temporary_count:
                        "[chelsea.name] has fallen for you, but doesn't see you as a replacement for her husband."
                    else:
                        "[chelsea.name] has fallen for you."
                else:
                    if chelsea.visit_sex_count > chelsea.visit_talk_count:
                        $ chelsea.temporary_count = chelsea.visit_talk_count*2
                        if chelsea.visit_sex_count > chelsea.temporary_count:
                            "[chelsea.name] has fallen for you, but doesn't see you as a replacement for her husband."
                        else:
                            "[chelsea.name] has fallen for you."
                    else:
                        "[chelsea.name] has fallen for you."
            elif chelsea.relationship_counter > 6:
                "[chelsea.name] feels torn between her love for her husband and her growing feelings for you."
            elif chelsea.relationship_counter > 3:
                "[chelsea.name] is flattered by your attention and is starting to feel guilty about seeing you behind her husband's back."
            elif chelsea.relationship_counter > 0:
                "[chelsea.name] appreciates the attention you're giving her."
            elif chelsea.has_tag('love_potion_used'):
              "[chelsea.name] doesn't feel like she has a relationship with you. The lingering effects of the love potion make her very sad about that."
            else:
              "[chelsea.name] doesn't feel like she has a relationship with you. You're just a guy her husband hired to help her out once."
            if chelsea.relationship_counter > 0:
                if chelsea.visit_talk_count > chelsea.visit_sex_count:
                    $ chelsea.temporary_count = chelsea.visit_sex_count*2
                    if chelsea.visit_talk_count > chelsea.temporary_count:
                        "[chelsea.name] thinks you're only interested in being her friend. She's disappointed about that, as she'd rather you be interested in her as a sex partner."
                    else:
                        "[chelsea.name] thinks you're interested in her both as a person and a sex partner. That frightens her a little, as her husband is the only other person in her life who thinks of her like that."
                elif chelsea.visit_sex_count > chelsea.visit_talk_count:
                    $ chelsea.temporary_count = chelsea.visit_talk_count*2
                    if chelsea.visit_sex_count > chelsea.temporary_count:
                        "[chelsea.name] thinks you're only interested in her body. She's good with that, as any attention you give her feeds her self-confidence without feeling like a threat to her marriage."
                    else:
                        "[chelsea.name] thinks you're interested in her both as a person and a sex partner. That frightens her a little, as her husband is the only other person in her life who thinks of her like that."
                else:
                    "[chelsea.name] thinks you're interested in her both as a person and a sex partner. That frightens her a little, as her husband is the only other person in her life who thinks of her like that."
            if chelsea.has_item(jewelry_chelsea):
                "[chelsea.name] loves the necklace you bought her."
            if chelsea.has_item(lingerie):
                "[chelsea.name] appreciates the lingerie you gave her."
            if chelsea.has_tag('love_potion_used'):
                "Thanks to the love potion, [chelsea.name] is smitten with you and loves when the two of you spend time together. Unfortunately, she also misses you more if time goes by when she doesn't see you, and her old self-confidence issues creep back in, making her question whether you're really interested in her."
            if player.has_tag('supersexy'):
                "Like most women, [chelsea.name] finds you attractive and enjoys spending time with you."
            if player.has_tag('dominant') and chelsea.spanked > 1:
                "She might not admit it, but [chelsea.name] finds your natural dominance interesting, and occasionally thinks about the times when you spanked her."
    elif chelsea.status == "on_training":
        wt_image chelsea.image
        if chelsea.has_tag('motivated'):
            "[chelsea.name]'s self-esteem issues have undermined her sex life. Her husband has asked you to help boost her desire to change her body image, although there may be another way to improve their sex life."
            "[chelsea.name] is feeling motivated to get herself in shape. She is working out and watching what she eats. She's been down this road before, and could back slide. If she keeps on this path and sticks with it, however, her husband may find himself married to a changed woman."
        elif chelsea.has_tag('happy'):
            "[chelsea.name]'s self-esteem issues have undermined her sex life. Her husband has asked you to help boost her desire to change her body image, although there may be another way to improve their sex life."
            "[chelsea.name] is feeling better about herself. She is starting to believe that she can be big and sexy at the same time. This may not be the solution her husband envisioned, but if [chelsea.name] can get over her lingering doubts about her attractiveness, she may be willing to resume an active sex life."
        else:
            "[chelsea.name]'s self-esteem issues have undermined her sex life. Her husband has asked you to help boost her desire to change her body image, although there may be another way to improve their sex life."
            "[chelsea.name] is deeply conflicted.  Sometimes she feels motivated to get in shape, but she can't hold that motivation. At other times she feels good about her curvy shape, but that too doesn't last, and she wants to lose weight."
        "You have until the end of week [chelsea.training_limit] to complete this engagement."
    if not chelsea.has_any_tag():
        if chelsea.has_tag('trigger_implanted'):
            "You have implanted a hypnotic trigger in her."
        if chelsea.has_tag('love_potion_used'):
            "She is under the influence of a love potion."
        "[chelsea.statblock]"
        $ items = ", ".join(i.name for i in chelsea.get_items()) if chelsea.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    return

# Mood Test
label chelsea_mood_test:
    if chelsea.status == 'on_training':
        # Math/Logic taken directly from RAGS
        # if chelsea.test('desire_c', 'sos', -30): ## tests must be against unmodified stats
        if chelsea.desire_c - chelsea.sos >= 30:
            add tags 'motivated' to chelsea # this is the tag leading to 'toned' Chelsea
            rem tags 'conflicted' 'happy' from chelsea
        # elif chelsea.test('sos', 'desire_c', -30):
        elif chelsea.sos - chelsea.desire_c >= 30:
            add tags 'happy' to chelsea # this is the tag that leading to 'bbw' for Chelsea
            rem tags 'conflicted' 'motivated' from chelsea
        else:
            add tags 'conflicted' to chelsea
            rem tags 'happy' 'motivated' from chelsea
    return

########### ROOMS ###########
# N/A

################################### NOTES ###################################

## Character Status
#0 = not yet prospect
#1 = prospect, .status = "available_to_be_client" and .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = client, .status = "on_training"
#4 = unsatisfied former client, add tags 'unsatisfied' and .status = "post_training"
#5 = satisfied former client, add tags 'satisfied' and .status = "post_training"
#6 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#7 = satisfied former client not continuing, rem tags 'continuing_actions' and .status = "post_training"
#8 = post continuing actions, add tags 'post_continuing_actions' and .status = "post_training"
