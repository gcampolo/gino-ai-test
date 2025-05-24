## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou & Subli & Wifetrainer

# Package  Register
# register_package lauren name "Lauren, The Cheater" description "Allows Lauren to be client." dependencies core
register lauren_pregame 10 in core as "Lauren the Cheater"

label lauren_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Lauren the Cheater (Dani Daniels)")]
    model_credits += [('bit', "Victoria (Veronica Avluv)")]
    # note: credits for Leigh are listed in Chelsea's script

    ## Character Definition
    lauren = Person(Character("Lauren", who_color="#F90095", what_color="#F90095"), "lauren", cut_portrait = True, prefix = "", suffix = "the Cheater", resistance = 70, training_period = 12, hypno_trigger_resistance_threshold = 5, hypno_trigger_sessions_threshold = 7, min_reputation = 2)
    lauren.trigger_phrase = "Cheaters can't say no"
    lauren.your_respect_name = "Sir"

    # Other Characters
    # note: Characters only appear in dialogue, Persons can be interacted with
    # note: character dialogue just uses name, while person dialogue uses name.c


    # NOTE: Sophie is now defined in her own script. and her actions are activated their
    # sophie = Person(Character("Receptionist", who_color="#424284", what_color="#424284"), "sophie", cut_portrait = True, prefix = "", suffix = "")

    # 128,64,64
    new_receptionist_lauren = Person(Character("New Receptionist", who_color="#804040", what_color="#804040", window_background = gui.dialogue_background_dark_font_color), "new_receptionist_lauren", cut_portrait = True, prefix = "", suffix = "")

    # Navy
    husband_lauren = Character("Lauren's Husband", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 800000 = Maroon
    lauren_victoria = Character("Victoria", who_color="#800000", what_color="#800000", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    lauren_gym_instructor = Character("Paul the Gym Instructor", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 0,0,160
    lauren_whore_client_1 = Character("Wealthy Man", who_color="#0000A0", what_color="#0000A0", window_background = gui.dialogue_background_dark_font_color)
    # Navy
    lauren_whore_client_2 = Character("Business Man", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 0,0,160
    lauren_whore_client_3 = Character("Traveling Business Man", who_color="#0000A0", what_color="#0000A0", window_background = gui.dialogue_background_dark_font_color)
    # 128,128,255
    shareen_lauren = Character("Shareen", who_color="#8080FF", what_color="#8080FF")

    ## Actions
    # Lauren Actions
    lauren.add_hypno_actions(implant = False) # this adds standard stat based _hypnosis_context actions
    lauren.blowjob_hypno_action = lauren.add_action("Have her blow you", label = "_blowjob_hypnosis", context = "_hypnosis", condition = "lauren.blowjob_count > 0 or lauren.resistance < 60 or lauren.desire > 10")
    lauren.fuck_hypno_action = lauren.add_action("Fuck her", label = "_fuck_hypnosis", context = "_hypnosis", condition = "lauren.status == 'post_training' and lauren.location == lauren_office")
    lauren.action_talk = lauren.add_action("Talk to her", label = '_talk', condition = "lauren.can_be_interacted and lauren.has_tag('first_visit') and lauren.status == 'on_training' and lauren.in_area('house')")
    lauren.action_fuck_machine = lauren.add_action("Use the Fuck Machine on her", label = '_fuck_machine', condition = "lauren.can_be_interacted and not lauren.has_tag('first_visit') and dungeon.has_item(fuck_machine) and lauren.status == 'on_training' and lauren.in_area('house')")
    lauren.action_display = lauren.add_action("Have her display herself", label = '_display', condition = "lauren.can_be_interacted and not lauren.has_tag('first_visit') and lauren.status == 'on_training'")
    lauren.action_workout = lauren.add_action("Have her workout", label = '_workout', condition = "lauren.can_be_interacted and not lauren.has_tag('first_visit') and lauren.status == 'on_training' and lauren.workout_count < 4")
    lauren.action_revenge = lauren.add_action("Lend her out for revenge", label = '_revenge', condition = "lauren.can_be_interacted and not lauren.has_tag('first_visit') and not lauren.has_tag('revenge_discussion_this_week') and lauren.status == 'on_training' and lauren.in_area('house')")
    lauren.action_punish = lauren.add_action("Punish her", label = '_punish', condition = "lauren.can_be_interacted and not lauren.has_tag('first_visit') and lauren.status == 'on_training' and lauren.in_area('house') and not lauren.has_tag('no_punishment')")
    lauren.action_end_session = lauren.add_action("Send her home", label="_end_session", condition = "not lauren.has_any_tag('first_visit', 'shut_off_end_session') and lauren.in_area('house')")
    lauren.action_bimbo_spend_time = lauren.add_action("Spend time with her", label = '_bimbo_spend_time', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('bimbo')")
    lauren.action_bimbo_sex = lauren.add_action("Have sex with her", label = '_bimbo_sex', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('bimbo')")
    lauren.action_watch_her_dance = lauren.add_action("Watch her dance", label = '_watch_her_dance', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and stage.is_here and lauren.has_tag('showgirl') and not lauren.has_tag('watched_today')")
    lauren.action_rename = lauren.add_action("Rename her", label = "_rename", condition = "lauren.status == 'post_training' and lauren.has_tag('slavegirl')")
    lauren.action_slavegirl_choose_position = lauren.add_action("Choose her position", label = '_slavegirl_choose_position', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('slavegirl')")
    lauren.action_slavegirl_punish = lauren.add_action("Punish her", label = '_slavegirl_punish', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('slavegirl')")
    lauren.action_slavegirl_use = lauren.add_action("Slavegirl - Use her", label = '_slavegirl_use', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('slavegirl')")
    lauren.action_lend_to_master_m = lauren.add_action("Lend to Master M", label="_lend_to_master_m", condition="lauren.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave')")
    lauren.action_your_name = lauren.add_action("Tell her how to address you", label="_your_name", condition="lauren.has_tag('slavegirl')")
    lauren.action_contact_arrange_meeting = None
    lauren.action_contact_fire_sophie = None
    lauren.action_contact_pimp = living_room.add_action("Pimp Lauren out", label = lauren.short_name + '_contact_pimp', context = "_contact_other", condition = "lauren.can_be_interacted and lauren.has_tag('whore') and lauren.whore_count < 3")
    lauren.action_continuing_visit = lauren.add_action("Spend time with her", label = '_continuing_visit', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('continuing_actions') and living_room.is_here")
    lauren.action_blackmail_her = lauren.add_action("Blackmail her", label = '_blackmail_her', condition = "lauren.can_be_interacted and lauren.status == 'post_training' and lauren.has_tag('continuing_actions') and living_room.is_here and lauren.cheated == 1")

    lauren.relationship_action = bedroom.add_action("[lauren.full_name]", label = lauren.short_name + "_relationship_status", context = "_relationship_status", condition = "lauren.has_tag('continuing_actions')")

    # New Receptionist Actions
    new_receptionist_lauren.action_ask_lauren = new_receptionist_lauren.add_action("Ask for Lauren", label = '_ask_lauren', condition = "new_receptionist_lauren.location == lauren_office")

    ## Tags
    # Common Character Tags
    lauren.add_tags('first_visit', 'no_hypnosis', 'likes_boys')
    new_receptionist_lauren.add_tag('no_hypnosis')
    #sophie.add_tags('first_visit', 'no_hypnosis')

    # Character Specific Tags
    # N/A

    ## Locations
    # Lauren's Office
    # note: can't visit until connections added after first visit
    lauren_office = Location("Lauren the Cheater's Office", 'lco', cut_portrait = True, enter_break_labels = ['lco_no_access'], enter_labels = ['lco_enter'], exit_labels = ['lco_exit'],  area = 'offices')
    lauren_office.connection_ot = lauren_office.add_connections(office_tower)

    ## Other
    lauren.change_status("available_to_be_client")
    new_receptionist_lauren.change_status("minor_character")

    # Start Day Events
    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('lauren_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    lauren.add_stats_with_value('hypno_blowjob_count', 'hypno_sex_count', 'hypno_swallow_count')

    # Character Specific Variables
    lauren.add_stats_with_value('bimbo_count_outfit', 'caress_her_count', 'cheated', 'discipline_punish_count', 'display_count_clothed', 'display_count_lingerie', 'display_count_office', 'fuck_machine_count', 'fuck_machine_orgasm_count', 'maid_count', 'office_outfit', 'office_visit_count', 'office_spank_count', 'office_visit_count', 'open_her_count', 'position', 'punishment_count', 'revenge_count')
    lauren.add_stats_with_value('spank_count', 'strip_outfit_count', 'swallow_desire_count', 'wait_count', 'weekend_discipline_count', 'weekend_dildo_count', 'weekend_sex_ask_count', 'whore_count', 'whore_lost_countdown', 'workout_count', 'bimbo_outfit_count')
    # note: code for lauren.cheated: 0 = not cheated, 1 = cheated, not resolved, 2 = blackmailed, 3 = post-blackmailed

    ######## EXPANDABLE MENUS #######
    ## Weekend Training
    lauren_weekend_training_menu = ExpandableMenu("What do you want to do with Lauren this weekend?", pre_label = 'lauren_pre_weekend', post_label = 'lauren_post_weekend')
    # note: these don't have to be defined in pregame, can be added in game
    lauren.choice_weekend_hypnotize =  lauren_weekend_training_menu.add_choice("Hypnotize her", "lauren_weekend_hypno_therapy", condition = "player.can_hypno(lauren)")
    lauren.choice_weekend_maid =  lauren_weekend_training_menu.add_choice("Maid training", "lauren_weekend_maid_training")
    lauren.choice_weekend_dildo =  lauren_weekend_training_menu.add_choice("Dildo training", "lauren_weekend_dildo_training_start")
    lauren.choice_weekend_discipline =  lauren_weekend_training_menu.add_choice("Discipline training", "lauren_weekend_discipline_training", condition = "lauren.punishment_count > 1")


  return

# Initial Contact Message
# RAGS OBJECT: Check Messages
label lauren_message:
    husband_lauren "{i}I recently discovered that my wife Lauren has been cheating on me. At first I was torn as to what to do.{/i}"
    husband_lauren "{i}My initial inclination was to divorce her and take her money. She's always been rather career and money focused, and the thought of depriving her of her wealth was somewhat satisfying.{/i}"
    husband_lauren "{i}Letting her just walk away from this with nothing more than a financial fine, however, just didn't seem enough.{/i}"
    husband_lauren "{i}The thought of her giving it up to another man - or men, I don't know how long this has been going on - when I was always left hanging is galling.{/i}"
    husband_lauren "{i}I always had to wait until she was in the mood, not too tired from work, not ditching me for an evening with her friends ... not too exhausted, apparently, from fucking some other guy.{/i}"
    husband_lauren "{i}No more. From now on, she's going to be my little slut. Ready and willing to do what I ask of her, when I ask her. I want you to train her, so that when I tell her to get on her knees, I don't get a big fight, I get an obedient little cocksucker.{/i}"
    husband_lauren "{i}And the running around on me has to stop. You can make whatever use of her you want, either as part of her training or for your own amusement. But when you're finished, I expect a docile wife who won't step out on me behind my back.{/i}"
    sys "Some of Lauren's artwork still needs to be upgraded from the older Rags version artwork."
    call consider_contract(lauren, "Reply to [lauren.full_name]'s Husband") from _call_consider_contract_5
    if yesno == True:
        sys "You accept the assignment.  You have until the end of week [lauren.training_limit] to complete it."
    if not player.has_tag('tutorial_message'):
        add tags 'tutorial_message' to player
        sys "You may hold one evening session each week to complete her training.  If you have at least [energy_long.value] Energy left on Friday, you may also schedule a weekend session with a client of your choice."
    return

# Character Rejected
label lauren_rejected:
  sys "You can no longer train [lauren.full_name]."
  return

# Arrange Character Session
# RAGS OBJECT: Schedule Character Session
label lauren_calling:
  # Check if character has already been trained this week
  if not lauren.can_be_interacted:
    "You've already had a session with Lauren this week. You need to wait until the weekend or next week to set up another."
  else:
    call forced_movement(living_room) from _call_forced_movement_147
    summon lauren
    $ lauren.visit_count += 1
    if 'first_visit' in lauren.tags:
      # note: don't remove the first_visit tag from her until you talk to her, as it's also used to control which actions are available
      wt_image cheater_initial_1
      "Lauren arrives promptly for her training."
      player.c "Come in and sit down."
      wt_image cheater_portrait_initially
      "As you directed, Lauren takes a seat across from you.  She settles in the chair awkwardly, as the short dress she's wearing rides up as she sits down."
      if not player.has_tag('first_client_visit_message'):
        add tags 'first_client_visit_message' to player
        sys "[player.first_client_visit_message_text]"
    elif lauren.has_tag('love_potion_used'):
      wt_image cheater_hypno_1_11
      lauren.c "Thanks for inviting me over again!  I love getting to spend time with you, even if it involves getting 'trained'."
      wt_image cheater_initial_8
      "Lauren takes a seat and waits to find out what you have planned for her today."
      if player.test('hypnosis_level', 0):
        rem tags 'no_hypnosis' from lauren
    else:
      wt_image cheater_portrait_initially
      "Lauren takes a seat and waits to find out what you have planned for her today."
      if player.test('hypnosis_level', 0):
        rem tags 'no_hypnosis' from lauren
  return

# Display Portrait
## NEED REVIEW ALL PORTRAIT ARTWORK FOR COLOUR ETC  #####################
label lauren_update_media:
    if lauren.status == "post_training":
        if lauren.has_tag('petgirl') and lauren.has_tag('leash_used'):
            $ lauren.change_image('cheater_cage_2')
        elif lauren.has_tag('petgirl'):
            $ lauren.change_image('cheater_cage_1')
        elif lauren.has_tag('slavegirl'):
            if lauren.position == 1:
                $ lauren.change_image('cheater_slave_position_1')
            elif lauren.position == 2:
                $ lauren.change_image('cheater_slave_position_2')
            elif lauren.position == 3:
                $ lauren.change_image('cheater_slave_position_3')
            elif lauren.position == 4:
                $ lauren.change_image('cheater_slave_position_4')
            elif lauren.position == 5:
                $ lauren.change_image('cheater_slave_position_5')
            elif lauren.position == 6:
                $ lauren.change_image('cheater_slave_position_6')
            elif lauren.position == 8:
                $ lauren.change_image('cheater_slave_position_8')
            else:
                $ lauren.change_image('cheater_slave_position_7')
        elif current_location == stage:
            if lauren.has_tag('watched_today'):
                if lauren.strip_outfit_count == 1:
                    $ lauren.change_image('cheater_showgirl_portrait_1')
                elif lauren.strip_outfit_count == 2:
                    $ lauren.change_image('cheater_strip_4_2')
                elif lauren.strip_outfit_count == 3:
                    $ lauren.change_image('cheater_strip_5_3')
                elif lauren.strip_outfit_count == 4:
                    $ lauren.change_image('cheater_strip_2_1')
                else:
                    $ lauren.change_image('cheater_showgirl_portrait_2')
            else:
                # note: outfits offset from dance count by 1 as examine will happen prior to next dance
                if lauren.strip_outfit_count == 1:
                    $ lauren.change_image('cheater_strip_4_2')
                elif lauren.strip_outfit_count == 2:
                    $ lauren.change_image('cheater_strip_5_3')
                elif lauren.strip_outfit_count == 3:
                    $ lauren.change_image('cheater_strip_2_1')
                elif lauren.strip_outfit_count == 4:
                    $ lauren.change_image('cheater_showgirl_portrait_2')
                else:
                    $ lauren.change_image('cheater_showgirl_portrait_1')
        elif lauren.has_tag('bimbo'):
            $ lauren.change_image('cheater_bimbo_portrait')
        #elif lauren.has_tag('whore'):
        #  $ lauren.change_image('cheater_')
        elif current_location == living_room:
            if lauren.has_tag('blackmailed'):
                $ lauren.change_image('cheater_continuing_18')
            elif lauren.has_tag('love_potion_used'):
                $ lauren.change_image('cheater_continuing_16')
            else:
                $ lauren.change_image('cheater_continuing_18')
        elif lauren.has_tag('satisfied'):
            $ lauren.change_image('cheater_continuing_18')
    else:
        $ lauren.change_image('cheater_portrait_initially')
    return

label new_receptionist_lauren_update_media:
  $ new_receptionist_lauren.change_image('new_receptionist_lauren_1')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label lauren_examine:
  if lauren.status == "post_training":
    if lauren.has_tag('petgirl') and lauren.has_tag('fetch_toy_used'):
      "Lauren the Cheater is now [lauren.full_name], although Lauren the She-Wolf might be a better description."
      "She's not yet domesticated and will bite if you get too close. For her safety and the safety of those around her, you need to keep her locked up in her cage at all times, except when she's playing with her fetch toy."
    elif lauren.has_tag('petgirl'):
      "Lauren the Cheater is now [lauren.full_name], although Lauren the She-Wolf might be a better description."
      "She's not yet domesticated and will bite if you get too close. For her safety and the safety of those around her, you need to keep her locked up in her cage at all times."
    elif lauren.has_tag('slavegirl'):
      "[lauren.full_name] waits for you in the position you placed her in."
      "Once she was Lauren the Cheater, a successful business woman struggling to balance the needs of her marriage, her career, and her own sexual libido.  Now she is your property, and happy."
    elif current_location == stage:
      "Lauren the Cheater has become Lauren the Showgirl. It's the perfect way for her to combine her love of money with her inner slut."
    elif lauren.has_tag('bimbo'):
      "Lauren the Cheater was an intelligent, successful businesswoman who cheated on her husband.  In order to keep him, she agreed to be trained by you."
      "Now she's Lauren the Bimbo. She lost her husband, her career, and her brain. But she doesn't worry about those things. All she worries about is whether she's allowed to fuck you?"
      "If she is, she's happy. If she isn't, she tries to amuse herself until she's allowed to fuck you again."
    #if lauren.has_tag('whore'):
    #  ""
    elif current_location == living_room:
      if lauren.has_tag('blackmailed'):
        "Lauren the Cheater is none too happy with you blackmailing her."
      elif lauren.has_tag('love_potion_used'):
        "Lauren the Cheater is besotted by the love potion and is happy to fool around with you, even though she's supposed to be an Obedient Slut for her husband."
      else:
        "Lauren the Cheater wants to be an Obedient Slut for her husband, but can't help herself from fooling around with you when you demand that of her."
    elif lauren.has_tag('satisfied'):
      "Lauren the Cheater used to fool around on her husband.  Now she's an Obedient Slut who caters to his every sexual whim and, as far as he knows, is loyal to him alone."
  elif lauren.status == "on_training":
    "Lauren's husband expects two things as his conditions for not divorcing her: that she stop cheating on him, and that she become his obedient little slut.  To do that, you'll need to help change her view of herself so that she accepts her new relationship with her husband."
  if lauren.status == "on_training":
    "You have until the end of week [lauren.training_limit] to complete this engagement."
  "[lauren.statblock]"
  $ items = ", ".join(i.name for i in lauren.get_items()) if lauren.get_items() != [] else ' Nothing'
  "You have given her: [items]"
  return

label new_receptionist_lauren_examine:
  "An attractive young man sits at the reception desk."
  return

# Talk to Character
label lauren_talk:
  wt_image cheater_portrait_initially
  player.c "Why are you here?"
  wt_image cheater_initial_2
  lauren.c "I cheated on my husband.  He told me that unless I wanted him to divorce me, I had to come here and let you \"train\" me."
  player.c "That's fine, but it doesn't explain why you agreed to come here."
  wt_image cheater_initial_3
  "Lauren looks away for a moment, then looks back at you."
  lauren.c "I wasn't faithful to my husband and he deserves better.  He wants me to subject myself to ... whatever it is you're going to do with me.  That seems rather extreme to me, but if it makes him feel better, I'm willing to do it."
  player.c "And what did your husband tell you the goal of my training was going to be?"
  "Lauren hesitates a moment before answering."
  wt_image cheater_initial_2
  lauren.c "To turn me into a proper wife for him."
  player.c "Is that how he worded it?  That I was to train you to become a proper wife?  What did he tell you he wanted you to become?"
  wt_image cheater_portrait_initially
  "Very quietly, Lauren responds."
  lauren.c "{size=-5}A proper little slut.{/size}"
  player.c "I couldn't hear that."
  lauren.c "A proper little slut.  He said he wanted me to become his slut."
  player.c "Is that why you're wearing that dress?"
  wt_image cheater_initial_3
  "Lauren looks away again, then back at you."
  lauren.c "Yes.  He told me to dress like a slut for my training."
  wt_image cheater_initial_5
  lauren.c "I don't think you know how humiliating this is for me. I'm a successful businesswoman. I have a good career managing an office downtown. This ... outfit ... is less than my receptionist would wear and she's barely half my age."
  wt_image cheater_initial_6
  lauren.c "I'm doing this for my husband because I think I owe him this, but I'm not happy about it."
  player.c "That's kind of the point, Lauren.  Your husband doesn't just want you to be a slut.  He wants you to be his slut.  No more running around behind his back."
  player.c "This training is supposed to be unpleasant, to remind you that cheating comes with consequences, so that you'll think twice before cheating again."
  wt_image cheater_initial_7
  player.c "You still, however, haven't fully explained why you've agreed to subject yourself to this training.  So I'll tell you why I think you're here."
  $ title = "What do you suggest?"
  menu:
    "This is about money":
      player.c "You don't like the idea of losing a big chunk of the money you've worked so hard for.  And that's what would happen, isn't it Lauren, if your husband divorces you?"
      wt_image cheater_initial_6
      "Lauren nods, sullenly."
      player.c "So you're going to follow my instructions, and you're going to fuck your husband any way he wants to fuck you, for the money."
      player.c "You know what they call women who fuck for money, don't you Lauren?  It isn't slut.  What is it?"
      "Lauren stays silent."
      player.c "I'll help you out  It's whore, Lauren.  And for the amount of money involved here, Lauren, you're going to need to be a very obedient and compliant whore. Is that understood?"
      wt_image cheater_portrait_initially
      "Lauren nods again, even more sullenly."
      change lauren resistance by -10
    "You like the idea of being humiliated":
      wt_image cheater_initial_6
      player.c "I think you like the idea of being humiliated.  Maybe it turns you on, maybe it's just what you think you deserve.  Maybe its even part of the reason you cheated or let yourself get caught, knowing that you would have to pay the consequences of your actions."
      player.c "Regardless, no woman would agree to your husband's conditions, and present herself to a stranger for slut training in that dress unless she was willing to be humiliated."
      player.c "Are you ready for me to start humiliating you, Lauren?"
      wt_image cheater_portrait_initially
      "She nods, sullenly."
      change lauren submission by 10
    "You love sex":
      wt_image cheater_initial_4
      player.c "You love sex. That's why you cheated. That's why you can accept the thought of being your husband's slut. Regardless of what you think of the word, a slut enjoys sex and you like the idea of your husband making your sex life interesting. Some part of you is even happy he sent you to me.  It means there's a chance you may get to have sex with another man without your husband considering it cheating."
      wt_image cheater_initial_8
      player.c "You don't want your husband's hands to be the only ones that touch you for the rest of your life, do you Lauren? You're hoping that somehow you can navigate this process, keep your husband happy, and still have a varied and exciting sex life, don't you, Lauren?"
      wt_image cheater_initial_9
      "Quietly, perhaps not quite believing what's she's heard, Lauren nods."
      change lauren desire by 10
  # this opens up access to visit Lauren in her office
  $ office_tower.action_visit_lauren = office_tower.add_action("Visit Lauren the Cheater's Office", context = '_elevator', label = "lauren_office_visit")
  rem tags 'first_visit' 'no_hypnosis' from lauren
  notify
  return

label new_receptionist_lauren_ask_lauren:
    wt_image new_receptionist_lauren_1
    player.c "Is Lauren in?"
    new_receptionist_lauren.c "She's just finishing up a meeting.  I'll let you know when she's available."
    "After a few minutes, a call comes through on the intercom."
    wt_image new_receptionist_lauren_2
    new_receptionist_lauren.c "Lauren will see you now.  Follow me."
    wt_image cheater_office_door
    "The receptionist leads you to Lauren's office."
    call lauren_in_office from _call_lauren_in_office_3
    return

# Hypno Actions
label lauren_hypnosis_start:
    # the _hypnosis_start label runs when the Hypnotize Her action is selected
    if lauren.status == "on_training":
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        if is_weekend():
            summon lauren
            wt_image cheater_weekend_hypno_15
            "Lauren's choice of 'slut clothes' for this weekend is a bit subdued, but does display a lot of bra-less cleavage."
            call focus_image from _call_focus_image_43
            player.c "Look at this for me, Lauren.  Look and listen."
            wt_image cheater_weekend_hypno_16
            player.c "Lauren, I'm going to talk with you.  You're going to sit down and listen to me."
            wt_image cheater_weekend_hypno_17
            player.c "Listen to me now, Lauren.  Listen to me.  Only to me now."
            wt_image cheater_weekend_hypno_18
            player.c "Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            wt_image cheater_weekend_hypno_19
            "She soon falls under your trance."
            player.c "Now Lauren, I want you to get comfortable for our talk.  Show me your breasts, Lauren."
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            wt_image cheater_weekend_hypno_20
            "Lauren reaches up and takes hold of the front of her dress ..."
            wt_image cheater_weekend_hypno_21
            "... then pulls it down to bare her breasts, as you requested, to continue your 'chat'."
        elif lauren.location == lauren_office:
            call focus_image from _call_focus_image_44
            player.c "Just look at this, Lauren.  That's all I want from you.  Look and listen.  I'm going to talk with you, and you're going to come here and listen to me."
            wt_image cheater_office_hypno_1
            player.c "Listen to me now, Lauren.  Listen to me.  Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            wt_image cheater_office_hypno_3
            "She soon falls under your trance."
            wt_image cheater_office_hypno_2
            player.c "Now Lauren, I want you to get comfortable for our talk.  Show me your breasts, Lauren."
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            wt_image cheater_office_hypno_4
            "Lauren takes hold of the front of her dress and pulls it down to bare her breasts, as you requested, to continue your 'chat'."
        else:
            call focus_image from _call_focus_image_45
            player.c "Look at this, Lauren. I'm going to talk with you while you look at this."
            wt_image cheater_hypno_1_23
            player.c "You're going to take off your coat and listen to me.  Look and listen."
            wt_image cheater_hypno_1_8
            player.c "Listen to me now, Lauren.  Listen to me.  Only to me now."
            wt_image cheater_hypno_1_9
            player.c "Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            wt_image cheater_hypno_1_1
            "She soon falls under your trance."
            player.c "Now Lauren, I want you to get comfortable for our talk.  Show me your breasts, Lauren."
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            wt_image cheater_hypno_1_2
            "Lauren reaches up and takes hold of the front of her dress ..."
            wt_image cheater_hypno_1_3
            "... then pulls it down to bare her breasts, as you requested, to continue your 'chat'."
    elif lauren.has_tag('petgirl'):
        "Hypnosis might help you domesticate her, but you haven't learned the art of hypnotizing animals yet."
        add tags 'no_hypnosis' to lauren
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    elif lauren.has_tag('slavegirl'):
        "It's less work now just to tell her what to think."
        add tags 'no_hypnosis' to lauren
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    elif lauren.has_tag('bimbo'):
        "Best not to spend any time exploring Lauren's mind these days.  You might get lonely in that wasteland."
        add tags 'no_hypnosis' to lauren
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    elif lauren.has_tag('blackmailed'):
        "Lauren is now too wary of you to allow you to hypnotize her."
        add tags 'no_hypnosis' to lauren
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        call focus_image from _call_focus_image_46
        player.c "Look at this, Lauren.  Look and listen.  I'm going to talk with you, and you're going to listen to me."
        if lauren.has_tag('tits_out_today'):
            wt_image cheater_office_3_106
            player.c "Listen to me.  Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            wt_image cheater_office_3_102
            "She soon falls under your trance."
        else:
            wt_image cheater_office_3_103
            player.c "Listen to me.  Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            wt_image cheater_office_3_104
            "She soon falls under your trance."
            wt_image cheater_office_3_105
            player.c "You want me to be comfortable for our talk, Lauren. You want me to be comfortable and you want to be comfortable. Remove your top and bra so we can both be comfortable."
            wt_image cheater_office_3_102
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        call focus_image from _call_focus_image_47
        player.c "Look at this, Lauren.  Look and listen.  I'm going to talk with you, and you're going to listen to me."
        if lauren.has_tag('tits_out_today'):
            wt_image cheater_office_4_61
            player.c "Listen to me.  Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            "She soon falls under your trance."
        else:
            wt_image cheater_office_4_3
            player.c "Listen to me.  Listen to my voice and nothing else, Lauren.  Only my voice.  Only my voice now."
            "She soon falls under your trance."
            player.c "You want me to be comfortable for our talk, Lauren. You want me to be comfortable and you want to be comfortable. Remove your top and bra so we can both be comfortable."
            wt_image cheater_office_4_61
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # $ lauren.training_session() ## added in hypnosis_end  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        call focus_image from _call_focus_image_48
        player.c "Look at this, Lauren.  Look and listen.  I'm going to talk with you and you're going to listen."
        wt_image cheater_continuing_20
        player.c "Listen to me, Lauren. Listen to me. Only to me now. Listen to my voice and nothing else, Lauren. Only my voice. Only my voice now."
        wt_image cheater_continuing_hypno_1
        "She soon falls under your trance."
        player.c "Now Lauren, I want you to get comfortable for our talk.  Show me your breasts, Lauren."
        wt_image cheater_continuing_hypno_2
        if not player.has_tag('first_hypno_breasts_message'):
            add tags 'first_hypno_breasts_message' to player
            "[player.first_hypno_breasts_message_text]"
    else:
        "You can't hypnotize Lauren in this location."
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    # if not cancelled, system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    return

label lauren_submission_hypnosis:
    # runs when Submission is selected from the hypnosis menu
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_22
        elif lauren.location == lauren_office:
            wt_image cheater_office_hypno_5
        else:
            wt_image cheater_hypno_1_7
        "You work on raising Lauren's Submission towards you. If she's willing to obey you, it'll be easier to train her to accept her new role."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        wt_image cheater_office_3_107
        "You work on raising Lauren's Submission towards you. Even with her official training over, it might be fun to increase her deference to you."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        wt_image cheater_office_4_62
        "You work on raising Lauren's Submission towards you. Even with her official training over, it might be fun to increase her deference to you."
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        wt_image cheater_continuing_hypno_3
        "You work on raising Lauren's Submission towards you. Even with her official training over, it might be fun to increase her deference to you."
    # system now applies the Submission gain and then goes on to the _submission_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label lauren_submission_hypnosis_end:
    # runs after Submission change applied
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_26
        elif lauren.location == lauren_office:
            wt_image cheater_office_1_10
        else:
            wt_image cheater_hypno_1_11
        if lauren.location == lauren_office:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and let her get on with her day."
        else:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and send her home."
        "She doesn't exactly remember what the two of you talked about, but her deference to you has grown."
    # continues to _implant_trigger or _hypnosis_end
    return

label lauren_desire_hypnosis:
    # runs when Desire is selected from the hypnosis menu
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_23
        elif lauren.location == lauren_office:
            wt_image cheater_office_hypno_6
        else:
            wt_image cheater_hypno_1_5
        "You work on raising Lauren's Desire towards you. If she's attracted to you, it will be easier to train her to accept her new role."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        wt_image cheater_office_3_108
        "You work on raising Lauren's Desire towards you. Even with her official training over, it can't hurt to increase her attraction to you."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        wt_image cheater_office_4_63
        "You work on raising Lauren's Desire towards you. Even with her official training over, it can't hurt to increase her attraction to you."
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        wt_image cheater_continuing_hypno_4
        "You work on raising Lauren's Desire towards you. Even with her official training over, it can't hurt to increase her attraction to you."
    # system now applies the Desire gain and then goes on to the _desire_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label lauren_desire_hypnosis_end:
    # runs after Desire change applied
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_27
        elif lauren.location == lauren_office:
            wt_image cheater_office_1_10
        else:
            wt_image cheater_hypno_1_12
        if lauren.location == lauren_office:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and let her get on with her day."
        else:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and send her home."
    # continues to _implant_trigger or _hypnosis_end
    return

label lauren_sos_hypnosis:
    # runs when Sos is selected from the hypnosis menu
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_24
        elif lauren.location == lauren_office:
            wt_image cheater_office_hypno_7
        else:
            wt_image cheater_hypno_1_6
        "You work on raising Lauren's Sense of Self, and in particular her acceptance of her new role. This can be the most difficult trait to affect directly, but it goes directly to the goal of her training."
    ## note: considering changing these to
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        wt_image cheater_office_3_109
        "With her official training over, raising her Sense of Self isn't going to do much, but I guess it doesn't hurt to have her embrace being the woman she's become."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        wt_image cheater_office_4_64
        "With her official training over, raising her Sense of Self isn't going to do much, but I guess it doesn't hurt to have her embrace being the woman she's become."
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        wt_image cheater_continuing_hypno_5
        "With her official training over, raising her Sense of Self isn't going to do much, but I guess it doesn't hurt to have her embrace being the woman she's become."
    # system now applies the sos gain and then goes on to the _sos_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label lauren_sos_hypnosis_end:
    # runs after SOS change applied
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_28
        elif lauren.location == lauren_office:
            wt_image cheater_office_1_10
        else:
            wt_image cheater_hypno_1_13
        if lauren.location == lauren_office:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and let her get on with her day."
        else:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and send her home."
        "She doesn't exactly remember what the two of you talked about, but she feels good about the chat."
    # continues to _implant_trigger or _hypnosis_end
    return

label lauren_resistance_hypnosis:
    # runs when Resistance is selected from the hypnosis menu
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_25
        elif lauren.location == lauren_office:
            wt_image cheater_office_hypno_8
        else:
            wt_image cheater_hypno_1_10
        "You work on reducing Lauren's Resistance to you. If she's willing to go along with your instructions without questioning you, it'll be easier to train her to accept her new role."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        wt_image cheater_office_3_110
        "You work on reducing Lauren's Resistance to you. With her official training over, this is only important for planting a hypno trigger in her, should you wish to do so."
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        wt_image cheater_office_4_65
        "You work on reducing Lauren's Resistance to you. With her official training over, this is only important for planting a hypno trigger in her, should you wish to do so."
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        wt_image cheater_continuing_hypno_6
        "You work on reducing Lauren's Resistance to you. With her official training over, this is only important for planting a hypno trigger in her, should you wish to do so."
    # system now applies the resistance loss and then goes on to the _resistance_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label lauren_resistance_hypnosis_end:
    # runs after Resistance change applied
    if lauren.status == "on_training":
        if is_weekend():
            wt_image cheater_weekend_hypno_29
        elif lauren.location == lauren_office:
            wt_image cheater_office_1_10
        else:
            wt_image cheater_hypno_1_14
        if lauren.location == lauren_office:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and let her get on with her day."
        else:
            "When you've gone as far as you can for this session, you instruct her to dress, bring her out of the trance and send her home."
        "She doesn't exactly remember what the two of you talked about, but her trust in you has grown."
        # continues to _implant_trigger or _hypnosis_end
    return

label lauren_blowjob_hypnosis:
    if lauren.status == "on_training":
        # note: hypno_ sex stats not used as this is part of her training and she's brought out of it and therefore remembers
        if is_weekend():
            wt_image cheater_weekend_hypno_4
            player.c "Lauren, you are an obedient slut. That's what your husband expects of you. That's what you are."
            wt_image cheater_weekend_hypno_7
            player.c "Your husband sent you here to be trained by me. To be trained on how to be an obedient slut. On how to make him happy. On how to make me happy."
            wt_image cheater_weekend_hypno_8
            player.c "You will make me happy now, Lauren. You will be an obedient slut and take out my cock and suck it, Lauren."
            wt_image cheater_weekend_hypno_9
            player.c "Show me how well you can suck my cock, Lauren. Show me how an obedient slut pleases her man."
            $ lauren.blowjob_count += 1
            if lauren.blowjob_count == 1:
                wt_image cheater_weekend_hypno_10
                "The hypnotized woman begins to bob her head up and down on your cock. You'll need to train her to pleasure your balls, too. That'll come later. She needs more basic lessons first."
                wt_image cheater_weekend_hypno_30
                player.c "Not like that.  Use more of your tongue. Back and forth along the underside of my cock."
                wt_image cheater_weekend_hypno_31
                player.c "Slow down.  I'll tell you when it's time to speed up. Lips only for now."
                wt_image cheater_weekend_hypno_32
                player.c "Swallow me, right down to the base."
                wt_image cheater_weekend_hypno_33
                player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth. Then start another stroke. Deeper this time, and hold it at the end.  Now repeat."
                wt_image cheater_weekend_hypno_36
                "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
                wt_image cheater_weekend_hypno_38
                "Like most women, she's never had her cock sucking technique critiqued before. Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
                wt_image cheater_weekend_hypno_37
                player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
            elif lauren.blowjob_count == 2:
                wt_image cheater_weekend_hypno_10
                call lauren_second_blowjob from _call_lauren_second_blowjob
                wt_image cheater_weekend_hypno_34
                player.c "Now you can go back to sucking my cock. Keep my balls warm with your hand as you suck me."
            elif lauren.blowjob_count == 3:
                wt_image cheater_ball_lick_1
                "Lauren takes your balls into her mouth and warms them up ..."
                wt_image cheater_weekend_hypno_11
                "... before shifting attention to your cock."
                wt_image cheater_weekend_hypno_37
                call lauren_third_blowjob from _call_lauren_third_blowjob
            elif lauren.blowjob_count == 4:
                wt_image cheater_ball_lick_1
                "You're pleased to see the hypnotized woman remembers her training."
                wt_image cheater_weekend_hypno_11
                "She warms up your balls nicely, then continues to play with them as she sucks your cock."
                wt_image cheater_weekend_hypno_34
                call lauren_fourth_blowjob from _call_lauren_fourth_blowjob
            else:
                wt_image cheater_ball_lick_1
                "You're pleased to see the hypnotized woman remembers her training."
                wt_image cheater_weekend_hypno_11
                "She warms up your balls nicely, then continues to play with them as she sucks your cock."
            wt_image cheater_weekend_hypno_33
            "You relax and enjoy the rest of the blowjob ..."
            wt_image cheater_weekend_hypno_32
            "... as she uses her mouth ..."
            wt_image cheater_weekend_hypno_31
            "... with the occasional stroke of her hand ..."
            wt_image cheater_weekend_hypno_30
            "... to get you ready."
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    wt_image cheater_weekend_hypno_39
                    player.c "Look at me, Lauren.  Come out of your trance and be aware of where you are."
                    wt_image cheater_weekend_hypno_37
                    lauren.c "What the ..."
                    player.c "Swallow my cum, Lauren."
                    wt_image cheater_weekend_hypno_35
                    "Instinctively she wraps her mouth back around your cock as it starts to spurt."
                    player.c "[player.orgasm_text]"
                    if lauren.blowjob_count > 3:
                        "Lauren squirms and moans slightly as your load strikes the back of her throat.  The act of receiving and swallowing your jizz is turning her on."
                    wt_image cheater_weekend_hypno_40
                "On her face" if lauren.blowjob_count > 3:
                    wt_image cheater_weekend_hypno_12
                    "You position the hypnotized woman on her knees in front of you."
                    player.c "Use both hands and your lips, Lauren.  Jerk me off while you suck me.  Now look up at me."
                    wt_image cheater_weekend_hypno_43
                    player.c "Come out of your trance, Lauren, and be aware of where you are."
                    wt_image cheater_weekend_hypno_13
                    "She wakes from the hypnosis as the first spurts of your cum enter her mouth.  She pulls back, succeeding only in receiving the next spurts on her face and chin."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_weekend_hypno_14
                    add tags 'facial_today' to lauren
            lauren.c "What the fuck???  What are you doing?"
            player.c "I'm not doing anything, other than cumming, which is the natural result of what you were doing - sucking my cock."
            if lauren.has_tag('facial_today'):
                pass
            else:
                wt_image cheater_weekend_hypno_41
            lauren.c "What do you mean ... why?  how?"
            if lauren.blowjob_count < 4:
                player.c "Why, because I asked you to. How, not very well, at least at first. I've been instructing you, to help you get better at this very basic skill every slut needs to excel in."
            else:
                player.c "Why, possibly because you're having a hard time staying away from my cock.  How, not too bad.  You're getting better at cock sucking."
            player.c "I want you to remember taking my cock out and everything that's happened since, Lauren."
            if lauren.has_tag('facial_today'):
                wt_image cheater_weekend_hypno_44
            else:
                wt_image cheater_weekend_hypno_42
            "Lauren's eyes go wide as the memories become available to her conscious mind."
            if lauren.has_tag('facial_today'):
                if lauren.facial_count == 0:
                    player.c "You were having so much fun, you didn't even mind me cumming on your face.  Clean yourself up, slut, then go home."
                elif lauren.facial_count == 1:
                    wt_image cheater_weekend_hypno_14
                    player.c "Get yourself dressed and go home, slut.  No, don't touch your face.  Leave the cum there."
                    lauren.c "You can't expect me to go home like this?"
                    wt_image cheater_weekend_hypno_44
                    player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make, not yours. Is that understood?"
                    lauren.c "Yes"
                else:
                    player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a load on your face."
            elif lauren.blowjob_count < 4:
                player.c "Remember those lessons, slut.  Practice them on your husband, if he gives you the opportunity."
            else:
                player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a dick in your mouth."
        elif lauren.location == lauren_office:
            wt_image cheater_office_hypno_8
            player.c "Lauren, you are an obedient slut. That's what your husband expects of you. That's what you are."
            wt_image cheater_office_hypno_3
            player.c "Your husband sent you here to be trained by me. To be trained on how to be an obedient slut.  On how to make him happy.  On how to make me happy."
            wt_image cheater_office_hypno_5
            player.c "You will make me happy now, Lauren.  You will be an obedient slut and get down on your knees in front of me, Lauren."
            wt_image cheater_office_hypno_5
            player.c "Show me how well you can suck my cock, Lauren.  Show me how an obedient slut pleases her man."
            $ lauren.blowjob_count += 1
            if lauren.blowjob_count == 1:
                wt_image cheater_office_2_5
                "The hypnotized woman wraps her lips around your cock. You'll need to train her to pleasure your balls, too. That'll come later. She needs more basic lessons first."
                wt_image cheater_office_2_23
                player.c "Not like that.  Use more of your tongue. Back and forth along the underside of my cock."
                wt_image cheater_office_2_25
                player.c "Swallow me, right down to the base, then slide back up to the tip. Tongue against my head, flick it back and forth. Then start another stroke. Deeper this time, and hold it at the end."
                wt_image cheater_office_2_24
                "You guide her mouth back and forth along your cock, instructing her on how you like your cock sucked. Like most women, she's never had her cock sucking technique critiqued before."
                wt_image cheater_office_2_5
                "Most men are too happy to get a blow job, even a bad one, to risk offending the provider. You, on the other hand, aren't the least bit concerned about offending Lauren."
                player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
                wt_image cheater_office_2_24
                "When she's learned as much as she's going to for today, you bring her out of her trance."
                wt_image cheater_office_2_23
                player.c "Look at me, Lauren. Come out of your trance and be aware of where you are."
                wt_image cheater_office_2_26
                lauren.c "What the ..."
                player.c "Swallow my cum, Lauren."
                wt_image cheater_office_2_23
                "Instinctively she wraps her mouth back around your cock as it starts to spurt."
                player.c "[player.orgasm_text]"
                wt_image cheater_office_1_15
            else:
                if lauren.blowjob_count == 2:
                    call lauren_second_blowjob from _call_lauren_second_blowjob_1
                    wt_image cheater_office_2_24
                    player.c "Now you can go back to sucking my cock. Keep my balls warm with your hand as you suck me."
                elif lauren.blowjob_count == 3:
                    wt_image cheater_ball_lick_1
                    "Lauren takes your balls into her mouth and warms them up ..."
                    wt_image cheater_office_2_24
                    "... before shifting attention to your cock."
                    call lauren_third_blowjob from _call_lauren_third_blowjob_1
                elif lauren.blowjob_count == 4:
                    wt_image cheater_ball_lick_1
                    "You're pleased to see the hypnotized woman remembers her training."
                    wt_image cheater_office_2_24
                    "She warms up your balls nicely, then continues to play with them as she sucks your cock."
                    call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_1
                else:
                    wt_image cheater_ball_lick_1
                    "You're pleased to see the hypnotized woman remembers her training."
                    wt_image cheater_office_2_24
                    "She warms up your balls nicely, then continues to play with them as she sucks your cock."
                wt_image cheater_office_2_25
                "You relax and enjoy the rest of the blowjob as she uses her lips, tongue, hand and mouth to get you ready."
                wt_image cheater_office_2_5
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image cheater_office_2_23
                        player.c "Look at me, Lauren.  Come out of your trance and be aware of where you are."
                        wt_image cheater_office_2_26
                        lauren.c "What the ..."
                        player.c "Swallow my cum, Lauren."
                        wt_image cheater_office_2_23
                        "Instinctively she wraps her mouth back around your cock as it starts to spurt."
                        player.c "[player.orgasm_text]"
                        if lauren.blowjob_count > 3:
                            "Lauren squirms and moans slightly as your load strikes the back of her throat.  The act of receiving and swallowing your jizz is turning her on."
                        wt_image cheater_office_1_15
                    "On her face" if lauren.blowjob_count > 3:
                        wt_image cheater_office_2_23
                        player.c "Look at me, Lauren.  Come out of your trance and be aware of where you are."
                        wt_image cheater_office_2_26
                        lauren.c "Wh ..."
                        wt_image cheater_facial_1
                        player.c "[player.orgasm_text]"
                        wt_image cheater_facial_2
                        add tags 'facial_today' to lauren
            lauren.c "What the fuck???  What are you doing?"
            player.c "I'm not doing anything, other than cumming, which is the natural result of what you were doing - sucking my cock."
            if lauren.has_tag('facial_today'):
                pass
            else:
                wt_image cheater_office_1_11
            lauren.c "What do you mean ... why?  how?"
            if lauren.blowjob_count < 4:
                player.c "Why, because I asked you to. How, not very well, at least at first. I've been instructing you, to help you get better at this very basic skill every slut needs to excel in."
            else:
                player.c "Why, possibly because you're having a hard time staying away from my cock.  How, not too bad.  You're getting better at cock sucking."
            player.c "I want you to remember taking my cock out and everything that's happened since, Lauren."
            if lauren.has_tag('facial_today'):
                wt_image cheater_facial_4
            else:
                wt_image cheater_office_1_4
            "Lauren's eyes go wide as the memories become available to her conscious mind."
            if lauren.has_tag('facial_today'):
                if lauren.facial_count == 0:
                    player.c "You were having so much fun, you didn't even mind me cumming on your face.  Clean yourself up, slut, then you can go back to work."
                elif lauren.facial_count == 1:
                    player.c "Time to go back to work, slut.  No, don't touch your face.  Leave the cum there."
                    wt_image cheater_facial_2
                    lauren.c "You can't expect me to work like this?"
                    player.c "Video call your husband and tell him what's on your face. He'll tell you when you can clean up. That'll be his decision to make. Not yours. Is that understood?"
                    lauren.c "Yes"
                else:
                    player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a load on your face."
            elif lauren.blowjob_count < 4:
                player.c "Remember those lessons, slut.  Practice them on your husband, if he gives you the opportunity."
            else:
                player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a dick in your mouth."
        else:
            wt_image cheater_hypno_1_4
            player.c "Lauren, you are an obedient slut. That's what your husband expects of you. That's what you are."
            wt_image cheater_hypno_1_7
            player.c "Your husband sent you here to be trained by me. To be trained on how to be an obedient slut.  On how to make him happy.  On how to make me happy."
            wt_image cheater_posing_1_8
            player.c "You will make me happy now, Lauren.  You will be an obedient slut, remove your clothes, and get down on your knees in front of me, Lauren."
            wt_image cheater_hypno_1_16
            player.c "Show me how well you can suck my cock, Lauren.  Show me how an obedient slut pleases her man."
            $ lauren.blowjob_count += 1
            if lauren.blowjob_count == 1:
                wt_image cheater_hypno_1_15
                "The hypnotized woman wraps her lips around your cock.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
                wt_image cheater_posing_1_16
                player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                wt_image cheater_posing_1_27
                player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now."
                wt_image cheater_posing_1_28
                player.c "Swallow me, right down to the base."
                wt_image cheater_posing_1_29
                player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
                wt_image cheater_posing_1_17
                "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
                wt_image cheater_posing_1_27
                "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, are not the least bit concerned about offending Lauren."
                wt_image cheater_posing_1_16
                player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
            elif lauren.blowjob_count == 2:
                wt_image cheater_hypno_1_15
                call lauren_second_blowjob from _call_lauren_second_blowjob_2
                wt_image cheater_posing_1_26
                player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you suck me."
            elif lauren.blowjob_count == 3:
                wt_image cheater_ball_lick_1
                "Lauren takes your balls into her mouth and warms them up ..."
                wt_image cheater_posing_1_30
                "... before shifting attention to your cock."
                wt_image cheater_posing_1_31
                call lauren_third_blowjob from _call_lauren_third_blowjob_2
            elif lauren.blowjob_count == 4:
                wt_image cheater_ball_lick_1
                "You're pleased to see the hypnotized woman remembers her training."
                wt_image cheater_posing_1_26
                "She warms up your balls nicely, then continues to play with them as she sucks your cock."
                wt_image cheater_posing_1_30
                call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_2
            else:
                wt_image cheater_ball_lick_1
                "You're pleased to see the hypnotized woman remembers her training."
                wt_image cheater_posing_1_26
                "She warms up your balls nicely, then continues to play with them as she sucks your cock."
            wt_image cheater_posing_1_27
            "You relax and enjoy the rest of the blowjob ..."
            wt_image cheater_posing_1_28
            "... as she uses her mouth ..."
            wt_image cheater_posing_1_17
            "... to get you ready."
            wt_image cheater_posing_1_30
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    wt_image cheater_hypno_1_15
                    player.c "Look at me, Lauren.  Come out of your trance and be aware of where you are."
                    wt_image cheater_hypno_1_17
                    lauren.c "What the ..."
                    player.c "Swallow my cum, Lauren."
                    wt_image cheater_hypno_1_18
                    "Instinctively she wraps her mouth back around your cock as it starts to spurt."
                    wt_image cheater_posing_1_28
                    player.c "[player.orgasm_text]"
                    if lauren.blowjob_count > 3:
                        "Lauren squirms and moans slightly as your load strikes the back of her throat.  The act of receiving and swallowing your jizz is turning her on."
                    wt_image cheater_hypno_1_17
                "On her face" if lauren.blowjob_count > 3:
                    wt_image cheater_hypno_1_21
                    player.c "Look at me, Lauren.  Come out of your trance and be aware of where you are."
                    wt_image cheater_hypno_1_22
                    lauren.c "Wh ..."
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_2
                    add tags 'facial_today' to lauren
            lauren.c "What the fuck???  What are you doing?"
            player.c "I'm not doing anything, other than cumming, which is the natural result of what you were doing - sucking my cock."
            if lauren.has_tag('facial_today'):
                pass
            else:
                wt_image cheater_hypno_1_19
            lauren.c "What do you mean ... why?  how?"
            if lauren.blowjob_count < 4:
                player.c "Why, because I asked you to. How, not very well, at least at first. I've been instructing you, to help you get better at this very basic skill every slut needs to excel in."
            else:
                player.c "Why, possibly because you're having a hard time staying away from my cock.  How, not too bad.  You're getting better at cock sucking."
            player.c "I want you to remember taking my cock out and everything that's happened since, Lauren."
            if lauren.has_tag('facial_today'):
                wt_image cheater_facial_4
            else:
                wt_image cheater_hypno_1_20
            "Lauren's eyes go wide as the memories become available to her conscious mind."
            if lauren.has_tag('facial_today'):
                if lauren.facial_count == 0:
                    player.c "You were having so much fun, you didn't even mind me cumming on your face.  Clean yourself up, slut, then go home."
                elif lauren.facial_count == 1:
                    player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                    wt_image cheater_facial_2
                    lauren.c "You can't expect me to go home like this?"
                    player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Is that understood?"
                    lauren.c "Yes"
                else:
                    player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a load on your face."
            elif lauren.blowjob_count < 4:
                player.c "Remember those lessons, slut.  Practice them on your husband, if he gives you the opportunity."
            else:
                player.c "Perhaps you just can't resist my cock any more? You'd best get control over those urges, slut. Your husband expects you to be faithful. No spontaneously sucking men's cocks just because you want a dick in your mouth."
        call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes
        orgasm notify
    elif lauren.has_tag('continuing_office_hypnosis_outfit_1'):
        wt_image cheater_office_3_70
        "You didn't have to hypnotize her to get her to suck your dick, but it's fun to watch her do so in a tranced state."
        wt_image cheater_office_3_67
        player.c "[player.orgasm_text]"
        $ lauren.hypno_blowjob_count += 1
        $ lauren.hypno_swallow_count += 1
        orgasm
    elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
        wt_image cheater_office_4_24
        "You didn't have to hypnotize her to get her to suck your dick ..."
        wt_image cheater_office_4_27
        "... but it's fun to watch her do so in a tranced state."
        wt_image cheater_office_4_26
        player.c "[player.orgasm_text]"
        $ lauren.hypno_blowjob_count += 1
        $ lauren.hypno_swallow_count += 1
        orgasm
    elif lauren.has_tag('continuing_actions') and current_location == living_room:
        wt_image cheater_continuing_7
        "You didn't have to hypnotize her to get her to suck your dick, but it's fun to watch her do so in a tranced state."
        wt_image cheater_continuing_25
        player.c "[player.orgasm_text]"
        $ lauren.hypno_blowjob_count += 1
        $ lauren.hypno_swallow_count += 1
        orgasm
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_16
    return

label lauren_fuck_hypnosis:
    if current_location == lauren_office and lauren.status == 'post_training':
        if lauren.has_tag('continuing_office_hypnosis_outfit_1'):
            wt_image cheater_office_3_112
            player.c "Spread your legs and offer me your pussy, Lauren.  You're looking forward to having me fuck you."
            wt_image cheater_office_3_74
            player.c "This feels good to you, but you're not to make a sound while I fuck you."
            wt_image cheater_office_3_77
            "She nods.  Her sex swells with blood and becomes dripping wet as you fuck her, but she stays silent."
            wt_image cheater_office_3_75
            player.c "You're not to cum while I'm fucking you, Lauren.  Do you understand?"
            lauren.c "Yes.  I'm not to cum while you fuck me, even though it feels so good."
            wt_image cheater_office_3_78
            "You take your time, keeping her hovering between the conflicting commands to enjoy being fucked and not to cum.  Eventually, you enjoy yourself too much to extend things any longer."
            wt_image cheater_office_3_81
            player.c "[player.orgasm_text]"
            wt_image cheater_office_3_82
            player.c "After I release you from the trance and leave, you'll discover my semen seeping through your panties.  When you do, you'll remember me fucking you and how much you enjoyed it."
            player.c "As soon as you can, you'll go somewhere private and masturbate.  Until you make yourself cum, the feel of my jizz dripping out of your pussy will make you hornier than you've ever felt in your entire life.  Do you understand, Lauren?"
            lauren.c "Yes, I understand."
        elif lauren.has_tag('continuing_office_hypnosis_outfit_2'):
            player.c "Turn around and bend over the desk, Lauren.  You're looking forward to having me fuck you."
            wt_image cheater_office_4_52
            player.c "This feels good to you, but you're not to make a sound while I fuck you."
            wt_image cheater_office_4_54
            "She nods.  Her sex swells with blood and becomes dripping wet as you fuck her, but she stays silent."
            wt_image cheater_office_4_55
            player.c "You're not to cum while I'm fucking you, Lauren.  Do you understand?"
            lauren.c "Yes.  I'm not to cum while you fuck me, even though it feels so good."
            wt_image cheater_office_4_57
            "You take your time, keeping her hovering between the conflicting commands to enjoy being fucked and not to cum.  Eventually, you enjoy yourself too much to extend things any longer."
            wt_image cheater_office_4_54
            player.c "[player.orgasm_text]"
            wt_image cheater_office_4_53
        if lauren.has_item('chastity_belt'):
            $ title = "Torment her?"
            menu:
                "Yes, make her need an orgasm she can't have":
                    player.c "After I release you from the trance and leave, you'll discover my semen seeping through your panties.  When you do, you'll remember me fucking you and how much you enjoyed it."
                    player.c "As soon as you can, you'll go somewhere private and masturbate.  Until you make yourself cum, the feel of my jizz dripping out of your pussy will make you hornier than you've ever felt in your entire life.  Do you understand, Lauren?"
                    lauren.c "Yes, I understand."
                    player.c "Since you'll be wearing your chastity belt, you won't be able to touch yourself.  The burning need will be so intense, you'll have to make it stop."
                    player.c "You'll reach out to me, Lauren.  You'll ask me to remove the belt.  The burning need won't go away until you cum, and you won't be able to cum until you can play with yourself, or you start to cry.  Understood?"
                    lauren.c "Yes.  I'll feel a burning need to cum, and I won't be able to cum until I touch myself or I start to cry."
                    add tags 'chastity_belt_call_pending' to lauren
                "No, take pity on her":
                    pass
        else:
            player.c "After I release you from the trance and leave, you'll discover my semen seeping through your panties.  When you do, you'll remember me fucking you and how much you enjoyed it."
            player.c "As soon as you can, you'll go somewhere private and masturbate.  Until you make yourself cum, the feel of my jizz dripping out of your pussy will make you hornier than you've ever felt in your entire life.  Do you understand, Lauren?"
            lauren.c "Yes, I understand."
            "That's one way to increase her Desire for you."
            change lauren desire by 5 notify
        $ lauren.hypno_sex_count += 1
        orgasm
        call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_32
    else:
        sys "There's been an error.  You shouldn't be able to access this option outside of Lauren's office."
    return

label lauren_implant_trigger:
    if player.has_tag('hypnotist'):
        # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
        if lauren.resistance < lauren.hypno_trigger_resistance_threshold:
            add tags 'trigger_implanted' to lauren
            "Lauren's mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
            $ title = "What trigger phrase do you want to use?"
            menu menu_lauren_trigger_phrase:
                "[lauren.trigger_phrase]":
                    pass
                "Choose something else":
                    $ lauren.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
                    jump menu_lauren_trigger_phrase
            player.c "Lauren, I have something important to tell you."
            player.c "When you hear the phrase \"[lauren.trigger_phrase]\" you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
            lauren.c "Yes.  When I hear \"[lauren.trigger_phrase]\" I will fall into a trance and do everything I am told."
            player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it."
            player.c "You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
            lauren.c "Yes.  I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
            "There are limited opportunities to use Lauren's trigger. You'll be informed if one arises."
        else:
            "You've been working on implanting a hypnotic trigger in Lauren's mind, but she's still too resistant to you. You need to lower her resistance before you can implant the trigger."
    return

label lauren_hypnosis_end:
    $ lauren.hypno_session()
    if lauren.has_tag('office_hypno_now'):
        notify
        rem tags 'office_hypno_now' from lauren
        # bring receptionist back
        if sophie.relationship_status < 6:
            summon sophie to lauren_office no_follows
        else:
            summon new_receptionist_lauren to lauren_office no_follows
        call character_location_return(lauren) from _call_character_location_return_460
        call forced_movement(office_tower) from _call_forced_movement_709
        wt_image current_location.image
    elif lauren.status == 'on_training':
        notify
        if is_weekend():
            call character_location_return(lauren) from _call_character_location_return_461
            end_day
        elif lauren.location != lauren_office:
            call character_location_return(lauren) from _call_character_location_return_462
            end_day
    elif lauren.has_tag('continuing_actions'):
        if lauren.has_tag('continuing_office_hypnosis_outfit_2'):
            if lauren.has_tag('tits_out_today'):
                wt_image cheater_office_4_5
                rem tags 'tits_out_today' from lauren
            else:
                wt_image cheater_office_4_3
            "You bring her out of her trance."
            lauren.c "Are we finished talking?  I have work I need to look after."
            player.c "That's all for today, yes."
            rem tags 'continuing_office_hypnosis_outfit_2' from lauren
            call lauren_in_office_end from _call_lauren_in_office_end
            notify
        else:
            wt_image cheater_continuing_19
            "When you're finished, you bring Lauren out of the trance and send her home."
            notify
            call character_location_return(lauren) from _call_character_location_return_463
    else:
        call character_location_return(lauren) from _call_character_location_return_464
    return

# End Session
label lauren_end_session:
  if lauren.status == "on_training":
    $ lauren.training_session()
    "You're unable to find an activity that both you and Lauren are willing to proceed with, so you end today's session here."
    $ player.extra_clients_fee_this_week -= lauren.pay # so you don't get paid for training her this week
    add tags 'failed_regular_training_this_week' to lauren
    call character_location_return(lauren) from _call_character_location_return_465
    end_day
  elif lauren.has_tag('continuing_actions'):
    $ lauren.training_session()
    "You've spent enough time with Lauren for today. You send her home."
    call character_location_return(lauren) from _call_character_location_return_466
    wt_image current_location.image
  else:
    add tags 'shut_off_end_session' to lauren
  return

# Weekend Actions
label lauren_pre_weekend:
    add tags 'checking_for_weekend' to lauren
    return

label lauren_post_weekend:
    if lauren.has_tag('checking_for_weekend'):
        rem tags 'checking_for_weekend' from lauren
    else:
        if lauren.has_tag('failed_regular_training_this_week'):
            rem tags 'failed_regular_training_this_week' from lauren
            $ player.extra_clients_fee_this_week += lauren.pay
    return

label lauren_weekend:
    if player.energy >= energy_long.value:
        call expandable_menu(lauren_weekend_training_menu) from _call_expandable_menu_13
    else:
        sys "You do not have enough energy for this action, choose something else."
    return

label lauren_weekend_hypno_therapy:
    rem tags 'checking_for_weekend' from lauren
    # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
    $ queue_action(lauren.hypno_action)
    return

label lauren_weekend_dildo_training_start:
    if player.has_item(dildo) and not lauren.has_item(dildo):
        $ title = "Set a dildo aside for Lauren's use?"
        menu:
            "Yes":
                call give_di_lauren from _call_give_di_lauren
                # NEED confirm artwork works for both?
            "No":
                pass
    if lauren.has_item(dildo):
        $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        rem tags 'checking_for_weekend' from lauren
        call lauren_weekend_dildo_training from _call_lauren_weekend_dildo_training
        notify
        end_day
    else:
        "You need to provide a dildo to Lauren to do this training."
    return

label lauren_weekend_dildo_training:
    summon lauren
    $ lauren.weekend_dildo_count += 1
    # first dildo training
    if lauren.weekend_dildo_count == 1:
        wt_image cheater_weekend_dildo_21
        "Lauren's choice of slut wear for this weekend looks like some sort of short-skirted prom gown."
        player.c "Showing off your legs today, are you?  Well okay, then.  Show them off."
        wt_image cheater_weekend_dildo_1
        "Tentatively, she lifts the hem of the short dress even higher."
        player.c "What about your ass?  Turn around."
        wt_image cheater_weekend_dildo_13
        player.c "I can't see you from way over there.  Come closer and bend over."
        wt_image cheater_weekend_dildo_14
        lauren.c "Slutty enough for you?"
        player.c "I'm not sure.  Bend over further."
        wt_image cheater_weekend_dildo_15
        "Lauren bends over, showing off panties the same color as her dress."
        wt_image cheater_weekend_dildo_2
        player.c "That won't do.  What's the point of a short dress if you can't flash someone properly in it?  Take the dress off."
        wt_image cheater_weekend_dildo_3
        player.c "At least you aren't wearing a bra.  There's hope for you yet.  Okay, let's get a look at these panties that you're so proud of you wore them to see me in."
        wt_image cheater_weekend_dildo_17
        player.c "I can't enjoy them properly like that.  Drop your hands and show them off to me like a proper slut."
        wt_image cheater_weekend_dildo_4
        player.c "Better.  Seen like that they do look rather slutty.  However, today's not a day you need panties.  Pull them down."
        wt_image cheater_weekend_dildo_6
        player.c "No need to pull them down all the way.  Half way down is enough to give easy access to your cunt, which I understand has never been a problem with you.  Today we're going to work on your fucking skills."
        if lauren.sex_count > 0:
            wt_image cheater_weekend_dildo_19
            player.c "Don't get your hopes up, though.  You don't get another go on my cock today.  You need to learn how to fuck a man properly.  I'm not going to have you thrashing about on me for hours trying to figure it out."
        else:
            wt_image cheater_weekend_dildo_18
            lauren.c "No ... wait ..."
            player.c "Don't worry, you're not going to be fucking me. You need to learn how to fuck a man properly, first. I'm not going to have you thrashing about on my cock for hours trying to figure it out."
        wt_image cheater_weekend_dildo_22
        "You get the dildo you set aside for Lauren, a large silicon one with a suction cup, and fix it to the top of the piano."
        player.c "You'll practice on this today and hopefully learn a few things your husband will appreciate."
        wt_image cheater_weekend_dildo_24
        player.c "First, though, you need to get yourself ready.  Let's see how fast you can get yourself wet.  Assuming the sight of that dildo doesn't already have you creaming yourself."
        wt_image cheater_weekend_dildo_5
        "Awkwardly, Lauren reaches back and places a finger inside herself."
        wt_image cheater_weekend_dildo_25
        "You watch as she goes through the motions of faking masturbation.  It isn't very convincing, but to her surprise, her body starts to respond."
        if lauren.test('desire',20):
            wt_image cheater_weekend_dildo_26
            "As the unexpected pleasure builds, Lauren lets out a small moan.  You smile, amused at her responsiveness."
            lauren.c "oooo"
            player.c "You're wet now, aren't you slut?  A good little slut getting herself ready.  Turn around and show me how wet you are."
            wt_image cheater_weekend_dildo_27
            "She spreads herself open for your inspection, the smell of her arousal filling your nose."
        else:
            wt_image cheater_weekend_dildo_5
        player.c "That's enough touching yourself.  Your cunt's ready for your partner, now it's time for you to get your partner ready for your cunt."
        wt_image cheater_weekend_dildo_28
        "Lauren crawls up on the piano to reach the dildo."
        wt_image cheater_weekend_dildo_29
        player.c "You can't get the dildo excited by flaunting your body at it.  Just imagine this dick is your husband's and he's getting bored with you, so you're going to have to work long and hard to earn his cum."
        wt_image cheater_weekend_dildo_7
        if lauren.blowjob_count > 0:
            player.c "You remember how I taught you to suck cock.  This is the perfect opportunity for you to practice."
        else:
            player.c "Let me see how you suck cock.  No no no.  Not like that.  I can see you need instructions in basic fellatio.  Try to suck dick like a grown slut, not like an awkward schoolgirl."
        "You leave her there to work the dildo over with her mouth.  From time to time you stop back to correct her or complement her on technique, depending on how well she's doing."
        wt_image cheater_weekend_dildo_30
        player.c "That's enough practice with your mouth.  A slut needs to be able to please a man with her cunt, too.  Turn around."
        wt_image cheater_weekend_dildo_31
        player.c "I hope your cunt is still wet.  If not, at least your spit has the dildo nice and sloppy."
        wt_image cheater_weekend_dildo_10
        "Lauren settles down onto the dildo.  She lets out a small groan as the large head pushes its way into her."
        lauren.c "oooo"
        wt_image cheater_weekend_dildo_32
        player.c "Don't just look at me.  Get to work.  You've got a dick inside you.  Time to pleasure it like an obedient slut."
        wt_image cheater_weekend_dildo_33
        if lauren.sex_count > 2:
            player.c "You remember my instructions on how to fuck cock.  Work it up and down.  Don't let it slip out!  Stop looking at me.  Focus on the cock you need to please, slut."
        else:
            player.c "Up and down, use your legs.  Right up to the tip on your way up, then slam down hard at the bottom of the stroke.  Use your hips too.  Rock them back and forth to change the angle of pressure."
    else:
        if lauren.test('sos',20):
            wt_image cheater_weekend_dildo_37
            "Lauren seems comfortable showing off her legs today."
            wt_image cheater_weekend_dildo_14
            "There's a flirtiness to the way she shows off her legs ..."
            wt_image cheater_weekend_dildo_16
            "... and she happily removes the dress when you tell her to."
        else:
            wt_image cheater_weekend_dildo_12
            "Lauren doesn't seem overly happy to be here."
            wt_image cheater_weekend_dildo_38
            "But she shows off her legs on demand ..."
            wt_image cheater_weekend_dildo_23
            "... and removes the dress when you tell her to without making a fuss."
        wt_image cheater_weekend_dildo_4
        lauren.c "Do these stay on today?"
        wt_image cheater_weekend_dildo_39
        player.c "No, they look better around your knees when you're finger fucking yourself."
        wt_image cheater_weekend_dildo_5
        "Lauren's not enthusiastic about touching herself while you watch ..."
        wt_image cheater_weekend_dildo_25
        "... but she's a highly sexual woman, and her body responds despite - or maybe because of - having an audience."
        if lauren.test('desire',20):
            wt_image cheater_weekend_dildo_26
            "As the unexpected pleasure builds, Lauren lets out a small moan.  You smile, amused at her responsiveness."
            lauren.c "oooo"
            player.c "You're wet now, aren't you slut?  A good little slut getting herself ready.  Turn around and show me how wet you are."
            wt_image cheater_weekend_dildo_27
            "She spreads herself open for your inspection, the smell of her arousal filling your nose."
        wt_image cheater_weekend_dildo_40
        player.c "That's enough unearned fun, slut.  Get the panties the rest of the way off, then get back up on the piano."
        wt_image cheater_weekend_dildo_28
        player.c "I know, you're disappointed that you don't get access to my cock today, but you need more practice before you get that opportunity."
        wt_image cheater_weekend_dildo_7
        if lauren.blowjob_count > 0:
            player.c "Don't forget your lessons.  This is a good opportunity for you to practice sucking dick the way I showed you."
        else:
            player.c "For a slut, you really are crap at giving head.  At least try to show the dildo a good time."
        wt_image cheater_weekend_dildo_30
        player.c "All right, the dildo is wet enough and I assume your slut cunt is still wet from your finger fucking.  Time to climb on board."
        wt_image cheater_weekend_dildo_31
        "Lauren positions herself above the tip of the toy ..."
        wt_image cheater_weekend_dildo_10
        "... then lowers herself onto it."
        lauren.c "oooo"
        wt_image cheater_weekend_dildo_32
        player.c "You do like being penetrated, don't you, slut?  Just remember, fucking isn't for your pleasure.  It's for your man's pleasure.  Get to work."
        wt_image cheater_weekend_dildo_33
        if lauren.sex_count > 2:
            player.c "That's it.  Up and down.  Right to the tip but don't let it slip out!  Then back down hard on the downstroke.  Stop looking at me.  Focus on the cock you need to please, slut."
        else:
            player.c "Up and down, use your legs.  Right up to the tip on your way up, then slam down hard at the bottom of the stroke.  Use your hips too.  Rock them back and forth to change the angle of pressure."
    wt_image cheater_weekend_dildo_34
    "You leave her there to work the dildo over with her cunt.  From time to time you stop back to scold her or praise her, depending on how much effort she's putting into it."
    if lauren.test('desire',40):
        wt_image cheater_weekend_dildo_35
        "Lauren tries very hard to concentrate on your instructions.  Despite herself, the combination of the dildo inside her and your attention as she rides it triggers a response in her body."
        lauren.c "oooooo"
        wt_image cheater_weekend_dildo_34
        player.c "You're almost ready to cum, aren't you slut?  That's an occupational hazard with sluts.  They like cock in them so much, they just can't help themselves."
        wt_image cheater_weekend_dildo_9
        player.c "Go ahead then, but don't you stop riding that cock.  Don't even pause.  This isn't about your pleasure, slut, it's about the man you're serving.  You don't let your orgasms interfere with pleasuring your man's cock, is that understood?"
        wt_image cheater_weekend_dildo_35
        lauren.c "Y ... yes ...  aaahhhh!"
        call lauren_masturbation_stat_changes from _call_lauren_masturbation_stat_changes
    wt_image cheater_weekend_dildo_11
    "When you think she's learned as much as she can for today, you let Lauren get off the dildo. Her legs trembling, the exhausted woman lies down on the piano top and rubs between her legs."
    player.c "Your cunt is sore from that workout, isn't it?"
    wt_image cheater_weekend_dildo_42
    lauren.c "A little."
    player.c "Despite that, you'd like a real cock in there right now, wouldn't you?"
    if lauren.test('sos',40) and lauren.sex_count > 1:
        $ lauren.weekend_sex_ask_count += 1
        wt_image cheater_weekend_dildo_43
        lauren.c "Yes, I do."
        wt_image cheater_weekend_dildo_44
        player.c "And when do obedient sluts get to fuck real cocks?"
        wt_image cheater_weekend_dildo_45
        lauren.c "When my husband - or you - tell me I can."
        "Now's a good opportunity to reinforce Lauren's subordinate role when it comes to sexual matters.  Or you could further her sex education."
        $ title = "What do you do?"
        menu:
            "Send her home":
                player.c "That's right.  Perhaps if you're lucky, your husband will be in a mood to plow your cunt before the weekend's over."
                wt_image cheater_weekend_dildo_3
                "You have her dress and send her home with a sore but needy pussy.  You wonder if she'll ask her husband to fuck her tonight?"
                if lauren.weekend_sex_ask_count == 1:
                    change lauren submission by 10
                elif lauren.weekend_sex_ask_count == 2:
                    change lauren submission by 5
            "Have sex with her":
                call lauren_weekend_dildo_fuck from _call_lauren_weekend_dildo_fuck
    else:
        wt_image cheater_weekend_dildo_36
        "She closes her legs, which isn't exactly the same thing as a denial."
    if lauren.weekend_dildo_count == 1:
        change lauren desire by 10
    elif lauren.weekend_dildo_count == 2:
        change lauren desire by 5
    if lauren.weekend_dildo_count > 1:
        if lauren.has_tag('masturbated_to_orgasm') and lauren.weekend_sex_ask_count > 1:
            "Lauren's not going to get any additional benefit from more dildo training."
        elif not lauren.has_tag('masturbated_to_orgasm') and lauren.weekend_sex_ask_count == 0:
            "Lauren's only going to benefit from additional dildo training when she's ready to accept and admit how her body's responding."
    call character_location_return(lauren) from _call_character_location_return_467
    return

label lauren_weekend_maid_training:
    rem tags 'checking_for_weekend' from lauren
    $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ lauren.maid_count += 1
    $ lauren.temporary_count = 0
    summon lauren
    if lauren.maid_count == 1:
        wt_image cheater_weekend_hypno_15
        "Lauren's choice of 'slut clothes' for this weekend is a bit subdued, but does display a lot of bra-less cleavage."
        player.c "Very nice, but I have a different outfit in mind for you this weekend."
        wt_image cheater_weekend_hypno_1
        "You hand her a small pile of clothes."
        player.c "Go get changed."
        wt_image cheater_weekend_maid_28
        "She returns, dressed in the maid outfit you bought her.  It's not even a nice uniform.  It's a cheap one, bought from a novelty store, which makes it all the more humiliating for Lauren to wear."
        lauren.c "You expect me to role play for you?"
        player.c "No, I expect you to clean my house and serve me, just as you'll be serving your husband whenever the two of you are together."
        wt_image cheater_weekend_maid_1
        lauren.c "You've got to be kidding?  I don't clean.  Do you have any idea how much money I make?"
        player.c "Enough that losing half of it in a divorce would be expensive.  Time to learn the joy of domestic service.  Go fetch me a glass of water."
        wt_image cheater_weekend_maid_2
        player.c "Wait.  That outfit's not quite right for you.  A slut maid shouldn't be covering so much of herself."
        wt_image cheater_weekend_maid_3
        player.c "Strip down to your underwear, then go get me my drink."
        wt_image cheater_weekend_maid_4
        "Lauren rinses out a glass, then fills it and brings it to you."
        wt_image cheater_weekend_maid_29
        "You examine her as you sip your drink."
        player.c "That's still too much covering for a slut servant like you.  Take off the bra."
        wt_image cheater_weekend_maid_5
        "She removes her top and stands in front of you with her breasts exposed.  You take another couple of sips of your drink before issuing her next instructions."
        player.c "Get to work.  I want this house spotless."
        wt_image cheater_weekend_maid_6
        "Bare breasted and in high heels, with the maid's cap still on her head, she tackles the dishes, the dusting, and the vacuuming.  You sit in your chair, enjoying your drink as you watch her."
        wt_image cheater_weekend_maid_5
        "When she's finally finished, she returns and stands in front of you."
        lauren.c "What now?"
        player.c "That's not how you present yourself when you're ready for new instructions.  You kneel down first."
        wt_image cheater_weekend_maid_7
        "Reluctantly, she sinks to her knees in front of you."
        player.c "You had something you wanted to ask me?"
        "A little more quietly this time, she repeats her question."
        lauren.c "What now?"
        player.c "Considering your role right now, you can ask that with more respect."
        "She hesitates only a moment."
        if lauren.test('submission',50):
            lauren.c "What now, Sir?"
        else:
            lauren.c "What now?  Sir."
        player.c "Now you wait until I finish watching this game."
    elif lauren.maid_count == 2:
        wt_image cheater_weekend_maid_28
        "Lauren changes into the maid's outfit as soon as she arrives, but she's still not happy about it."
        lauren.c "Why don't you let me hire a maid crew for you?  If I pay them enough, they'll all wear these outfits for you while they clean your house."
        player.c "Just because you have money doesn't mean you get to shirk your domestic duties.  An obedient slut is happy to do menial work for her man whenever it pleases him."
        wt_image cheater_weekend_maid_1
        player.c "On which note, go get me a glass of water."
        wt_image cheater_weekend_maid_2
        player.c "Not like that."
        wt_image cheater_weekend_maid_3
        player.c "That's better."
        wt_image cheater_weekend_maid_4
        "Lauren rinses out a glass, then fills it and brings it to you."
        wt_image cheater_weekend_maid_29
        "You examine her as you sip your drink."
        player.c "You could be more pleasing for me right now."
        wt_image cheater_weekend_maid_5
        "She removes her top and stands in front of you with her breasts exposed.  You take another couple of sips of your drink before issuing her next instructions."
        player.c "Get to work.  I want this house spotless."
        wt_image cheater_weekend_maid_6
        "Bare breasted and in high heels, with the maid's cap still on her head, she tackles the dishes, the dusting, and the vacuuming.  You sit in your chair, enjoying your drink as you watch her."
        wt_image cheater_weekend_maid_5
        "When she's finally finished, she returns and stands in front of you."
        lauren.c "What now?"
        "You ignore her."
        wt_image cheater_weekend_maid_7
        "After a moment, she reluctantly sinks to her knees in front of you."
        lauren.c "What now?"
        player.c "Ask properly if you expect an answer."
        "She hesitates only a moment."
        if lauren.test('submission',50):
            lauren.c "What now, Sir?"
        else:
            lauren.c "What now?  Sir."
        player.c "Now you wait until I finish watching this game."
    elif lauren.maid_count == 3:
        wt_image cheater_weekend_maid_28
        "Lauren changes into the maid's outfit as soon as she arrives."
        wt_image cheater_weekend_maid_1
        lauren.c "Did you want some water?"
        player.c "You can ask better than that."
        if lauren.test('submission',50):
            lauren.c "Do you want some water, Sir?"
        else:
            lauren.c "Do you want some water?  Sir."
        player.c "Yes"
        wt_image cheater_weekend_maid_2
        lauren.c "Should I ...?"
        wt_image cheater_weekend_maid_3
        player.c "Yes"
        wt_image cheater_weekend_maid_4
        "Lauren rinses out a glass, then fills it and brings it to you."
        wt_image cheater_weekend_maid_29
        lauren.c "Should I ...?"
        player.c "Yes"
        wt_image cheater_weekend_maid_5
        "She removes her top and stands in front of you with her breasts exposed.  You take another couple of sips of your drink before issuing her next instructions."
        player.c "Get to work.  I want this house spotless."
        wt_image cheater_weekend_maid_6
        "Bare breasted and in high heels, with the maid's cap still on her head, she tackles the dishes, the dusting, and the vacuuming.  You sit in your chair, enjoying your drink as you watch her."
        wt_image cheater_weekend_maid_5
        "When she's finally finished, she returns and stands in front of you.  She hesitates for a moment ..."
        wt_image cheater_weekend_maid_7
        "... then sinks to her knees in front of you."
        if lauren.test('submission',50):
            lauren.c "What now, Sir?"
        else:
            lauren.c "What now?  Sir."
        player.c "Now you wait until I finish watching this game."
    else:
        wt_image cheater_weekend_maid_28
        "Lauren changes into the maid's outfit as soon as she arrives."
        wt_image cheater_weekend_maid_1
        if lauren.test('submission',50):
            lauren.c "Do you want some water, Sir?"
        else:
            lauren.c "Do you want some water?  Sir."
        player.c "Yes"
        wt_image cheater_weekend_maid_3
        "Remembering your prior instructions, she strips to her bra ..."
        wt_image cheater_weekend_maid_4
        "... rinses out a glass, fills it and brings it to you ..."
        wt_image cheater_weekend_maid_30
        "... then pulls off her bra ..."
        wt_image cheater_weekend_maid_5
        "... and waits as you sip your drink."
        player.c "Get to work.  I want this house spotless."
        wt_image cheater_weekend_maid_6
        "Bare breasted and in high heels, with the maid's cap still on her head, she tackles the dishes, the dusting, and the vacuuming.  You sit in your chair, enjoying your drink as you watch her."
        wt_image cheater_weekend_maid_5
        "When she's finally finished, she returns ... "
        wt_image cheater_weekend_maid_7
        "... and sinks to her knees in front of you.  She doesn't ask you what you want.  She now understands the rules."
    $ title = "How do you want her to wait?"
    menu:
        "Kneeling in front of you":
            wt_image cheater_weekend_maid_8
            "You turn the TV on to the sports channel.  It's not an important game and you're only mildly interested in the outcome."
            "Your enjoyment of the game, however, is enhanced by the sight of Lauren kneeling on all fours in front of you.  You keep her there, waiting, until the game is finished."
        "As a footstool":
            wt_image cheater_weekend_maid_31
            "You position Lauren sideways in front of you, on all fours and turn the TV on to the sports channel."
            wt_image cheater_weekend_maid_9
            "Then you rest your feet on her ass.  She looks up at you in disbelief, but says nothing."
            "It's not an important game and you're only mildly interested in the outcome.  Your enjoyment of the game, however, is enhanced by your new furniture. You keep her there until the game is finished."
        "Legs spread":
            wt_image cheater_weekend_maid_10
            "You order Lauren to sit back and spread her legs.  Then you turn the TV on to the sports channel."
            "It's not an important game and you're only mildly interested in the outcome.  Your enjoyment of the game, however, is enhanced by the sight of Lauren displaying her charms in front of you.  You keep her there until the game is finished."
    $ title = "What now?"
    menu menu_lauren_weekend_maid_1:
        "Use her for sex":
            if lauren.blowjob_count == 0:
                if lauren.test('desire', 10) or lauren.test('resistance', 50):
                    player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
                    wt_image cheater_weekend_maid_7
                    "Lauren hesitates only a moment before crouching down in front of you.  Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
                    wt_image cheater_weekend_maid_14
                    "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
                    wt_image cheater_weekend_maid_36
                    player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                    wt_image cheater_weekend_maid_13
                    player.c "Slow down.  I'll tell you when it's time to speed up."
                    wt_image cheater_weekend_maid_36
                    player.c "Swallow me, right down to the base."
                    wt_image cheater_weekend_maid_37
                    player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
                    wt_image cheater_weekend_maid_14
                    "You guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
                    wt_image cheater_weekend_maid_36
                    "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
                    wt_image cheater_weekend_maid_13
                    player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
                    wt_image cheater_weekend_maid_37
                    "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
                    wt_image cheater_weekend_maid_38
                    "When she's learned as much as she can from one session, you empty your load in her."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_weekend_maid_39
                    player.c "Swallow it all."
                    lauren.c "I did."
                    player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
                    $ lauren.blowjob_count += 1
                    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_1
                    orgasm
                else:
                    wt_image cheater_resisting_6
                    lauren.c "No.  I'm not going to have sex with you.  I don't care what my husband thinks."
                    "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off."
                    jump menu_lauren_weekend_maid_1
            else:
                $ title = "What do you want to do with her?"
                menu:
                    "Test her oral skills":
                        call lauren_weekend_maid_oral from _call_lauren_weekend_maid_oral
                    "Fuck her" if lauren.sex_count == 0:
                        call lauren_weekend_maid_fuck from _call_lauren_weekend_maid_fuck
                    "Test her fucking skills" if lauren.sex_count >= 1:
                        call lauren_weekend_maid_fuck from _call_lauren_weekend_maid_fuck_1
                    "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
                        call lauren_weekend_maid_anal from _call_lauren_weekend_maid_anal
                    "Use the asswhore" if 'accepts_anal' in lauren.tags:
                        call lauren_weekend_maid_anal from _call_lauren_weekend_maid_anal_1
                    "Never mind":
                        jump menu_lauren_weekend_maid_1
        "Pleasure her":
            $ lauren.pleasure_her_count += 1
            player.c "You've been a good servant today, Lauren, and good service should be rewarded."
            wt_image cheater_weekend_maid_32
            if lauren.pleasure_her_count == 1:
                if lauren.sex_count == 0:
                    lauren.c "Wait, I'm not ..."
                    wt_image cheater_weekend_maid_33
                    "She doesn't have a chance to complete her objection before you surprise her by placing your mouth between her legs."
                else:
                    lauren.c "What are you ..."
                    wt_image cheater_weekend_maid_33
                    lauren.c "Oh!"
                wt_image cheater_weekend_maid_34
                "Whatever she was expecting you to do with her, this wasn't it."
            else:
                "Lauren might be wet as soon as she opens her legs ..."
                wt_image cheater_weekend_maid_34
                "... if she wasn't, she certainly is by the time your tongue touches her."
            lauren.c "oooo"
            if lauren.test('desire', 30):
                wt_image cheater_weekend_maid_11
                "The feel of your lips and tongue on her sex soon overwhelms Lauren."
                lauren.c "oooooo"
                wt_image cheater_weekend_maid_12
                "She groans as she climaxes and fills your mouth with her sticky juices."
                lauren.c "Y ... yes ... aaahhhh!"
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change
            else:
                wt_image cheater_weekend_maid_33
                "Her mind and body never fully relax enough for her to cum, but her sex is becomes sopping wet from your ministrations."
            wt_image cheater_weekend_maid_35
            "Her legs are trembling by the time you finish.  You send her home feeling good about her visit with you."
            call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes
        # check for possible spanking scene here?
        "Send her home":
            "You have no more use for Lauren's services for today.  You let her dress and send her home."
    if lauren.maid_count == 1:
        $ lauren.temporary_count += 10
    elif lauren.maid_count == 2:
        $ lauren.temporary_count += 5
    if lauren.temporary_count > 0:
        change lauren submission by lauren.temporary_count
        $ lauren.temporary_count = 0
    notify
    call character_location_return(lauren) from _call_character_location_return_468
    end_day # end_day used instead of end_week unless it happens on day != 5
    return

label lauren_weekend_discipline_training:
    call forced_movement(dungeon) from _call_forced_movement_710
    summon lauren
    rem tags 'checking_for_weekend' from lauren
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    wt_image cheater_weekend_discipline_25
    "As instructed, Lauren arrives for her training in 'slut clothes'.  She's chosen a tight skirt and an even tighter top which is just see through enough to show off her nipples."
    player.c "Time for additional discipline training, slut."
    wt_image cheater_weekend_discipline_1
    "Her face falls.  This is easily her least favorite form of training."
    if lauren.test('submission', 75):
        wt_image cheater_weekend_discipline_16
        lauren.c "Maybe you'd like to spank me, Sir?"
        player.c "That's a good girl for offering, but I have something more intense in mind for you today."
    $ lauren.weekend_discipline_count += 1
    if lauren.weekend_discipline_count == 1:
        wt_image cheater_weekend_discipline_26
        player.c "I like the see through top, Lauren.  Very appropriate for a slut when out in public.  When in private, however, it hides entirely too much of your nipples."
        wt_image cheater_weekend_discipline_2
        "You tie her to a pole, hands above her head.  Then picking up a pair of scissors, you improve her top."
        wt_image cheater_weekend_discipline_27
        player.c "There, that's more appropriate, don't you agree?"
        wt_image cheater_weekend_discipline_28
        lauren.c "Owww!!"
        wt_image cheater_weekend_discipline_3
        "You pull up her skirt and play with her sex while you continue to pinch one of her exposed nipples.  To her surprise, she gets wet quickly from your touch."
        player.c "I didn't hear you answer my question.  Isn't this look more appropriate for a little slut?"
        lauren.c "If you think so, then yes."
        wt_image cheater_weekend_discipline_29
        player.c "What does your cunt think, Lauren?"
        "You stab two fingers inside her, making her gasp."
        lauren.c "Oh!"
        wt_image cheater_weekend_discipline_3
        player.c "That's wetness, slut.  Which means your cunt agrees, doesn't it?"
        lauren.c "Yes, this is an appropriate look for a slut."
        if dungeon.has_item(floggers):
            wt_image cheater_weekend_discipline_4
            player.c "Let's see if your nipples also agree."
            "You pick up one of your floggers and begin to rhythmically strike her exposed chest ... *thwack*  *thwack*  *thwack* ..."
            wt_image cheater_weekend_discipline_30
            "After a few blows, her nipples are fully erect, having bounced out of the holes in the front of her blouse to peak over the top of the neckline."
            player.c "Your nipples agree, too, don't they slut?  They like being exposed to the leather striking against their bareness."
            lauren.c "Oowww!!  That hurts!"
            wt_image cheater_weekend_discipline_31
            "*thwack*  *thwack*  *thwack*"
            player.c "It hurts and what, slut?"
            lauren.c "Shit.  Yes, it hurts and it feels good, too.  Yes, my nipples like this."
            change lauren desire by 5
        else:
            wt_image cheater_weekend_discipline_17
            "Taking her public hairs between your fingers, you give them a firm tug."
            lauren.c "Ow!"
            player.c "Don't get greedy, cunt.  That's as much of my fingers as you get today."
        wt_image cheater_weekend_discipline_32
        player.c "Since it enjoys having it's nipples exposed so much, perhaps your body would like to be completely naked?"
        wt_image cheater_weekend_discipline_33
        lauren.c "nnnnn"
        wt_image cheater_weekend_discipline_5
        player.c "Shhh.  No words.  I'm going to listen to what your body tells me, slut, not what your mouth is saying.  And your hard little nipples are saying I'm right."
        wt_image cheater_weekend_discipline_7
        lauren.c "NNNNNNNN"
        player.c "Even when I squeeze your tits roughly, feel what your nipples are doing.  They're getting even harder."
        wt_image cheater_weekend_discipline_6
        player.c "You greedy little cunt, you're dripping wetness all over my fingers again."
        lauren.c "nnnnnnn"
        wt_image cheater_weekend_discipline_34
        player.c "I'm going to leave you here for a while, slut, to give you time to contemplate what your body's telling you.  About how much it likes being helpless and exposed."
        wt_image cheater_weekend_discipline_5
        player.c "If you're lucky, I might tease your nipples once in a while."
        wt_image cheater_weekend_discipline_7
        player.c "If you're really lucky, I might even treat your tits and nipples the way they love to be treated."
        lauren.c "NNNNNNNN"
        wt_image cheater_weekend_discipline_6
        player.c "Unfortunately, cunt, you don't get my fingers inside you again.  I don't care how much you drip all over the floor."
        add tags 'disciplined_now' to lauren
        while lauren.has_tag('disciplined_now'):
            wt_image cheater_weekend_discipline_34
            $ title = "What now?"
            menu:
                "Tease her nipples":
                    wt_image cheater_weekend_discipline_5
                    lauren.c "nnnnn"
                "Tease her pussy":
                    wt_image cheater_weekend_discipline_6
                    lauren.c "nnnnn!!"
                "Hurt her breasts":
                    wt_image cheater_weekend_discipline_7
                    lauren.c "NNNNN"
                "Flog her" if dungeon.has_item(floggers):
                    wt_image cheater_weekend_discipline_35
                    "*THWACCKK*"
                    wt_image cheater_weekend_discipline_36
                    lauren.c "NNNNNNNN!!"
                "That's enough":
                    rem tags 'disciplined_now' from lauren
        wt_image cheater_punishment_1_8
        "By the time you let her down, she's exhausted, sore, and very, very aroused."
        change lauren desire by 5
        change lauren submission by 5
        change lauren resistance by -10
    # NEED finish artwork review from here down
    elif lauren.weekend_discipline_count == 2:
        wt_image cheater_weekend_discipline_34
        player.c "You remember this, don't you slut?"
        wt_image cheater_weekend_discipline_5
        player.c "Your body remembers, too.  See how hard your nipples are already?"
        lauren.c "nnnnnn"
        wt_image cheater_weekend_discipline_6
        player.c "I know.  You're worried because last time your body got all excited but didn't get to cum.  I think I have a solution."
        wt_image cheater_weekend_discipline_8
        "Lauren watches in fear as you tie a rope between her legs, loop it over a pulley in the ceiling, and tie the other end to a large rock."
        wt_image cheater_weekend_discipline_37
        player.c "I've rigged up a little device to distract your cunt from the excitement of being exposed like this.  Can you guess how it works?"
        "You lift the rock into position, check to make sure that the ropes are not cutting off her circulation, then let the rock fall."
        wt_image cheater_weekend_discipline_9
        lauren.c "NNNNNNNN"
        player.c "I'll be back in an hour or so to check on you. In the meantime, you can spend some time thinking about your cunt and how important it is for you to control the feelings you're receiving from it."
        "Time soon has no meaning for her.  You don't really leave her there for a full hour, but to her it feels like you've been gone for five by the time you finally check on her."
        if player.has_item(dildo) and not lauren.has_item(dildo):
            $ title = "Do you want to set a dildo aside for use on Lauren?"
            menu:
                "Yes":
                    give 1 dildo from player to lauren notify
                "No":
                    pass
        wt_image cheater_weekend_discipline_37
        player.c "Not wet now I see.  I suppose you think it'd be impossible to be wet with those ropes cutting into your cunt from the weight of this rock?"
        "Lauren nods vigorously."
        if lauren.has_item(dildo):
            wt_image cheater_weekend_discipline_19
            player.c "Let me demonstrate how wrong you are."
            "You place the sex toy against Lauren's sore and swollen pussy lips and set it to vibrate ... *bzzzzzzz*"
            wt_image cheater_weekend_discipline_38
            lauren.c "NNNNN  ...  NNNNN  ...  NNNNNNN"
            "First her hips, then her legs start trembling ..."
            wt_image cheater_weekend_discipline_18
            "... then her whole body spasms as the toy vibrates her to orgasm ... *bzzzzzzz*"
            lauren.c "NNNNNNNN"
            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_1
            wt_image cheater_weekend_discipline_6
            player.c "You don't understand your body at all, do you slut?  It's a good thing you have me to teach you what you really need."
            "You rub her sensitive, post-orgasm pussy as she whimpers, then untie her and send her home."
            change lauren desire by 5
            change lauren submission by 5
            change lauren resistance by -10
            add tags 'came_from_weekend_bondage_dildo' to lauren
        else:
            wt_image cheater_weekend_discipline_6
            player.c "Maybe sometime I'll get a toy for you and show you how wrong you are."
            wt_image cheater_punishment_1_8
            "A shaken Lauren takes a few minutes to recover from her ordeal before she can head home."
            change lauren submission by 5
            change lauren resistance by -5
    else:
        $ title = "What do you have in mind for her today?"
        menu menu_lauren_weekend_discipline_1:
            "Pussy rope ordeal":
                wt_image cheater_weekend_discipline_5
                player.c "You remember this, don't you slut?  Your body remembers, too.  The only question is what happens next?"
                wt_image cheater_weekend_discipline_8
                "Lauren groans dejectedly as you tie the rope between her legs again."
                lauren.c "nnnnnn"
                wt_image cheater_weekend_discipline_37
                player.c "Was that an excited moan, slut?  It's hard to tell through the rope gag.  I guess I'll have to check your body's responses to find out. Let's just get this in position first."
                wt_image cheater_weekend_discipline_9
                lauren.c "NNNNNNNN"
                player.c "I'll be back in an hour or so to check and see what your body has to tell me. In the meantime, you can spend some time thinking about your cunt and how important it is for you to control the feelings you're receiving from it."
                "Time soon has no meaning for her.  You don't really leave her there for a full hour, but to her it feels like you've been gone for five by the time you finally check on her."
                if player.has_item(dildo) and not lauren.has_item(dildo):
                    $ title = "Do you want to set a dildo aside for use on Lauren?"
                    menu:
                        "Yes":
                            give 1 dildo from player to lauren notify
                        "No":
                            pass
                if lauren.has_item(dildo):
                    if lauren.has_tag('came_from_weekend_bondage_dildo'):
                        wt_image cheater_weekend_discipline_37
                        player.c "You're wet, cunt.  Despite the rope biting into you, you remember how this ended before and you're eagerly waiting for relief again."
                        $ title = "Give let her have the relief?"
                        menu:
                            "Yes, let her orgasm":
                                wt_image cheater_weekend_discipline_19
                                "You place the sex toy against Lauren's sore and swollen pussy lips and set it to vibrate ... *bzzzzzzz*"
                                wt_image cheater_weekend_discipline_38
                                lauren.c "NNNNN  ...  NNNNN  ...  NNNNNNN"
                                "First her hips, then her legs start trembling ..."
                                wt_image cheater_weekend_discipline_18
                                "... then her whole body spasms as the toy vibrates her to orgasm ... *bzzzzzzz*"
                                lauren.c "NNNNNNNN"
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_3
                                wt_image cheater_punishment_1_8
                                player.c "What do you think?  Was the ordeal beforehand worth the orgasm afterwards?"
                                lauren.c "I'm not sure."
                                player.c "Still not in tune with your cunt, then, because it doesn't have any doubts."
                                change lauren desire by 5
                                change lauren resistance by -5
                            "No, just take her down":
                                wt_image cheater_weekend_discipline_8
                                "Lauren groans in frustration as you untie her."
                                lauren.c "nnnnn"
                                player.c "Is there something you want?"
                                wt_image cheater_weekend_discipline_6
                                "Lauren shakes her head."
                                player.c "Still not in tune with your cunt, then, because it's giving me a completely different answer.  Why don't you go home and think about what that answer is?"
                                change lauren submission by 5
                                change lauren resistance by -5
                    else:
                        wt_image cheater_weekend_discipline_37
                        player.c "Not wet now I see.  I suppose you think it'd be impossible to be wet with those ropes cutting into your cunt?"
                        "Lauren nods vigorously."
                        wt_image cheater_weekend_discipline_19
                        player.c "Let me demonstrate how wrong you are."
                        "You place the sex toy against Lauren's sore and swollen pussy lips and set it to vibrate ... *bzzzzzzz*"
                        wt_image cheater_weekend_discipline_38
                        lauren.c "NNNNN  ...  NNNNN  ...  NNNNNNN"
                        "First her hips, then her legs start trembling ..."
                        wt_image cheater_weekend_discipline_18
                        "... then her whole body spasms as the toy vibrates her towards orgasm ... *bzzzzzzz*"
                        lauren.c "NNNNNNNN"
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_2
                        wt_image cheater_weekend_discipline_6
                        player.c "You don't understand your body at all, do you slut?  It's a good thing you have me to teach you what you really need."
                        "You rub her sensitive, post-orgasm pussy as she whimpers, then untie her and send her home."
                        change lauren desire by 5
                        change lauren submission by 5
                        change lauren resistance by -5
                        add tags 'came_from_weekend_bondage_dildo' to lauren
                else:
                    wt_image cheater_weekend_discipline_37
                    player.c "Not wet now I see.  I suppose you think it'd be impossible to be wet with those ropes cutting into your cunt?"
                    "Lauren nods vigorously."
                    wt_image cheater_weekend_discipline_6
                    player.c "Maybe sometime I'll get a toy for you and show you how wrong you are."
                    wt_image cheater_punishment_1_8
                    "A shaken Lauren takes a few minutes to recover from her ordeal before she can head home."
                    change lauren resistance by -5
            "Bondage sex":
                if lauren.blowjob_count == 0:
                    if lauren.test('desire', 10) or lauren.test('resistance', 50):
                        wt_image cheater_bondage_sex_11
                        "You tie Lauren into a kneeling position and take out your cock."
                        player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
                        "Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
                        wt_image cheater_bondage_sex_12
                        "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
                        wt_image cheater_bondage_sex_13
                        player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                        wt_image cheater_bondage_sex_14
                        player.c "Slow down.  I'll tell you when it's time to speed up."
                        wt_image cheater_bondage_sex_15
                        player.c "Swallow me, right down to the base."
                        wt_image cheater_bondage_sex_17
                        player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
                        wt_image cheater_bondage_sex_16
                        "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
                        wt_image cheater_bondage_sex_15
                        "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
                        wt_image cheater_bondage_sex_13
                        player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now."
                        wt_image cheater_bondage_sex_18
                        player.c "Start again, at the beginning."
                        wt_image cheater_bondage_sex_19
                        "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
                        wt_image cheater_bondage_sex_20
                        "When she's learned as much as she can from one session, you empty your load in her."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_bondage_sex_21
                        player.c "Swallow it all."
                        wt_image cheater_bondage_sex_13
                        lauren.c "I did."
                        player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
                        $ lauren.blowjob_count += 1
                        call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_2
                        orgasm
                        change player energy by -energy_long notify
                    else:
                        wt_image cheater_punishment_1_1
                        lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
                        "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off."
                        jump menu_lauren_weekend_discipline_1
                else:
                    $ title = "What do you want to do with her?"
                    menu menu_lauren_weekend_discipline_2:
                        "Test her oral skills":
                            call lauren_punish_bondage_sex_oral from _call_lauren_punish_bondage_sex_oral
                        "Fuck her" if lauren.sex_count == 0:
                            call lauren_punish_bondage_sex_fuck from _call_lauren_punish_bondage_sex_fuck
                        "Test her fucking skills" if lauren.sex_count >= 1:
                            call lauren_punish_bondage_sex_fuck from _call_lauren_punish_bondage_sex_fuck_1
                        "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
                            call lauren_punish_bondage_sex_anal from _call_lauren_punish_bondage_sex_anal
                        "Use the asswhore" if 'accepts_anal' in lauren.tags:
                            call lauren_punish_bondage_sex_anal from _call_lauren_punish_bondage_sex_anal_1
                        "Never mind":
                          jump menu_lauren_weekend_discipline_1
            "Bondage punishment":
                $ lauren.discipline_punish_count += 1
                wt_image cheater_weekend_discipline_39
                "You lay her on the floor and tie one leg to the pole, spreading her legs again in nearly the same position as her first punishment."
                player.c "Does this position remind you of something?"
                wt_image cheater_weekend_discipline_10
                lauren.c "It's like what you did the first time you punished me."
                player.c "That's right.  And what did I tell you that position was good for?"
                lauren.c "Punishing a slut.  Are you going to punish me again?"
                player.c "Yes.  Do you know why?"
                lauren.c "No"
                wt_image cheater_weekend_discipline_40
                player.c "Because you haven't been paying attention to what your cunt wants. You'll never control your cunt until you understand it."
                wt_image cheater_weekend_discipline_11
                "The elastics on her feet are every bit as effective this time as they were the first time you punished her.  She's soon screaming at the top of her lungs."
                lauren.c "OOOOWWWWWW!!!!!"
                wt_image cheater_weekend_discipline_20
                "You continue the punishment for a long time, much longer than her first session.  You take her to that state where it hurts almost too much to bear, but not quite. And you keep her there until she's a writhing sobbing mess on the floor in front of you."
                lauren.c "oooohhhh ... oohhh oohhh oohhh!!!"
                wt_image cheater_weekend_discipline_41
                "She knows now that she can put up with the pain, that as much as it hurts, it won't kill her."
                if player.has_item(dildo) and not lauren.has_item(dildo):
                    $ title = "Do you want to set a dildo aside for use on Lauren?"
                    menu:
                        "Yes":
                            give 1 dildo from player to lauren notify
                        "No":
                            pass
                $ title = "What now?"
                menu:
                    "Offer her an orgasm" if lauren.has_item(dildo):
                        wt_image cheater_weekend_discipline_41
                        player.c "Would this cunt like an orgasm now?"
                        if lauren.test('sos', 40):
                            wt_image cheater_weekend_discipline_24
                            lauren.c "{size=-5}yesss{/size}"
                            player.c "I couldn't hear you."
                            wt_image cheater_weekend_discipline_42
                            lauren.c "Yes, this cunt would like an orgasm.  Please."
                            wt_image cheater_weekend_discipline_22
                            "You place her toy between Lauren's legs and set it to vibrate ... *bzzzzzzz*.  It only takes a few seconds for her to orgasm, bucking and writhing on the floor."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_weekend_discipline_21
                            "You keep the toy in place, and a few minutes after that, she cums again, this time making almost no sound as the orgasm almost slips out of her, a form of relief for her tortured body."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_weekend_discipline_23
                            "Even resuming the torture of the elastics snapping against her feet can't keep her from shaking and howling to a third, long drawn out orgasm."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_weekend_discipline_12
                            player.c "This is what it feels like to be an obedient slut, Lauren.  You feel pain when you're told to feel pain, pleasure when you're allowed to feel pleasure, and provide service on demand.  Remember this feeling, Lauren."
                            "Through the shaking of her fourth, body-wracking orgasm, she tries to nod.  When her tremors subside, you untie her and let her go home."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_4
                            if lauren.has_tag('weekend_punishment_orgasm'):
                                change lauren desire by 5
                            else:
                                add tags 'weekend_punishment_orgasm' to lauren
                                change lauren submission by 10
                                if lauren.has_tag('weekend_punishment_reinforced_submission'):
                                    change lauren sos by 5
                                else:
                                    change lauren sos by 10
                        else:
                            wt_image cheater_weekend_discipline_42
                            "Lauren hasn't yet embraced her inner slut enough to admit how much she wants to cum right now.  She keeps her mouth shut, but you know the truth."
                            wt_image cheater_punishment_1_8
                            "You have her dress and send her home, once she's recovered from the ordeal."
                    "Reinforce her submission":
                        wt_image cheater_weekend_discipline_41
                        player.c "I want you to think about how you feel right now, Lauren."
                        wt_image cheater_weekend_discipline_42
                        player.c "If I put my hands between your legs, you'd cum for me. If I told you to service me, you'd take my cock in your mouth without question. If I told you I was going to punish you some more, you'd close your eyes and accept it.  This is what obedience feels like, Lauren. You're feeling very obedient right now, aren't you slut?"
                        wt_image cheater_weekend_discipline_24
                        lauren.c "yesss"
                        if lauren.has_tag('weekend_punishment_reinforced_submission'):
                            change lauren submission by 5
                        else:
                            add tags 'weekend_punishment_reinforced_submission' to lauren
                            change lauren submission by 10
                            if not lauren.has_tag('weekend_punishment_orgasm'):
                                change lauren sos by 5
                if lauren.discipline_punish_count == 1:
                    change lauren resistance by -10
                elif lauren.discipline_punish_count == 2:
                    change lauren resistance by -5
    notify
    call character_location_return(lauren) from _call_character_location_return_469
    end_day
    return

## Character Specific Actions
# Have Her Display Herself
label lauren_display:
    if lauren.display_count_clothed == 0:
        $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        call lauren_display_clothes from _call_lauren_display_clothes
        change player energy by -energy_long notify
        end_day
    else:
        $ title = "Have her change clothes?"
        menu:
            "No":
                $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                call lauren_display_clothes from _call_lauren_display_clothes_1
                change player energy by -energy_long notify
                end_day
            "Yes, into lingerie":
                if not lauren.has_item(lingerie) and player.has_item(lingerie):
                    $ title = "Do you want to gift Lauren the lingerie?"
                    menu:
                        "Yes":
                            call give_li_lauren from _call_give_li_lauren
                        "No":
                            "You need to gift lingerie to Lauren before you can choose this option.  For now, choose another action."
                if lingerie in lauren.items:
                    $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    call lauren_display_lingerie from _call_lauren_display_lingerie
                    change player energy by -energy_long notify
                    end_day
                else:
                    "You need to gift lingerie to Lauren before you can choose this option.  For now, choose another action."
    return

label lauren_display_clothes:
  $ lauren.display_count_clothed += 1
  # first display action
  if lauren.display_count_clothed == 1:
    wt_image cheater_initial_3
    player.c "Stand up, Lauren, and take off your jacket.  If you're going to become an obedient slut, you need to learn to follow directions."
    wt_image cheater_posing_1_1
    player.c "Now bend over that table and show me your ass."
    wt_image cheater_posing_1_2
    "Slowly Lauren turns and leans over, resting her hands on the table while looking back at you."
    player.c "Not like that.  Spread your legs when you're showing me your ass."
    wt_image cheater_posing_1_3
    player.c "A little better.  Now, turn around and pull down your dress to show me your tits."
    wt_image cheater_posing_1_32
    lauren.c "Just like that?"
    player.c "Just like that.  Obedient sluts disrobe on command."
    wt_image cheater_posing_1_34
    "She stares at you in a battle of wills.  You wait."
    wt_image cheater_posing_1_33
    "Eventually she rolls her eyes and turns around.  Even then, she hesitates."
    player.c "Shy?"
    if lauren.visit_count_total == 0:
        lauren.c "I don't even know you."
        player.c "Obedient sluts don't need an introduction.  You've been told to display your tits.  Do so."
    elif lauren.blowjob_count == 0 and lauren.sex_count == 0:
        lauren.c "I barely even know you."
        player.c "Obedient sluts don't need an introduction.  You've been told to display your tits.  Do so."
    else:
        lauren.c "After what we've done together, I guess not."
    wt_image cheater_posing_1_35
    "With a look that suggests she's still trying to do this on her terms, she pulls down the front of her dress."
    wt_image cheater_posing_1_36
    player.c "They're tits, Lauren.  Neither the biggest nor the perkiest I've seen.  Don't act like you've done me some great favor by revealing them.  Pull up the bottom of your dress now."
    wt_image cheater_posing_1_37
    player.c "No panties?  That's the first proper slut behavior I've seen from you.  Good girl.  Bend back over the table to show me your ass again."
    wt_image cheater_posing_1_5
    "Trembling slightly, Lauren does as she's told, then looks back at you, wondering what comes next."
  # second clothed display
  elif lauren.display_count_clothed == 2:
    wt_image cheater_initial_3
    player.c "Get up.  Let me have a look at you."
    wt_image cheater_posing_1_1
    player.c "Not like that.  Bend over the table."
    wt_image cheater_posing_1_2
    player.c "Have you forgotten what I told you already?"
    wt_image cheater_posing_1_3
    player.c "Better.  Do it again.  This time without the dress covering up so much of you."
    wt_image cheater_posing_1_33
    lauren.c "I thought my tits weren't interesting?"
    wt_image cheater_posing_1_36
    player.c "All tits are interesting.  Yours just aren't particularly special.  Are you wearing panties today?"
    wt_image cheater_posing_1_37
    player.c "Good.  Back over the table."
    wt_image cheater_posing_1_5
    "Trembling slightly, Lauren does as she's told, then looks back at you, wondering what comes next."
  # subsequent displays
  else:
    wt_image cheater_initial_3
    player.c "Get up.  Let me have a look at you."
    wt_image cheater_posing_1_43
    "She lets you have a look at her in the dress ..."
    wt_image cheater_posing_1_32
    "... then turns around ..."
    wt_image cheater_posing_1_3
    "... and spreads her legs."
    wt_image cheater_posing_1_35
    "After a moment she turns back and pulls down the front of the dress ..."
    wt_image cheater_posing_1_4
    "... waits as you inspect her breasts ..."
    wt_image cheater_posing_1_44
    "... then turns back around and pulls up the bottom of her dress."
    wt_image cheater_posing_1_5
  # first set of training options
  $ title = "What do you do next?"
  menu:
    "Spank her":
      $ lauren.spank_count += 1
      wt_image cheater_spank_1
      "Without a word you lift up your hand and bring it down sharply on Lauren's bare bottom ... *smack*"
      lauren.c "Ow!"
      if lauren.spank_count == 1:
        wt_image cheater_resisting_2
        "She knew her training was intended as a punishment, but she didn't know she would be literally punished."
        wt_image cheater_posing_1_41
        player.c "Get back in position.  Yes, you're being spanked like a naughty girl.  That's what happens when you're not obedient to your husband."
      else:
        wt_image cheater_posing_1_41
        player.c "Yes, you're being spanked again.  Get back in position."
      wt_image cheater_spank_1
      "*smack*"
      wt_image cheater_posing_1_42
      lauren.c "Ow!"
      wt_image cheater_spank_1
      "*smack*"
      wt_image cheater_posing_1_42
      lauren.c "Oww!"
      wt_image cheater_spank_1
      "*smack*"
      wt_image cheater_posing_1_42
      lauren.c "Owww!!"
      call lauren_spank_stat_changes from _call_lauren_spank_stat_changes
      add tags 'spanked_today' to lauren
    "Caress her":
      $ lauren.caress_her_count += 1
      wt_image cheater_posing_1_7
      "As you stroke your fingers along her sex, Lauren starts to stand up.  A hand at the back of her neck guides her back onto the table."
      wt_image cheater_posing_1_38
      "You keep her there until you can tell - and she knows you can tell - that her body is responding to your caress."
      lauren.c "oooo"
      wt_image cheater_posing_1_39
      player.c "See how easy it is to be an obedient slut?  Just accept that your man can touch you when and how he wants."
      call lauren_caress_stat_changes from _call_lauren_caress_stat_changes
      add tags 'pleasured_today' to lauren
    "Have her touch herself" if lauren.caress_her_count > 0:
      if not lauren.has_tag('touched_herself'):
        add tags 'touched_herself' 'pleasured_today' to lauren
        player.c "Show me how you get yourself off."
        wt_image cheater_posing_1_44
        lauren.c "What?"
        player.c "Turn around and play with yourself, slut."
        wt_image cheater_posing_1_45
        lauren.c "While you watch?"
        player.c "Of course while I watch.  Lose the dress and get up higher so I have a good view."
        wt_image cheater_posing_1_46
        lauren.c "I'm not going to be able to ... you know.  Not with you watching."
        player.c "Not going to be able to cum like an obedient slut?  Not if you don't start rubbing yourself you won't."
        wt_image cheater_posing_1_11
        "Awkwardly, Lauren goes through the motions of faking masturbation.  It isn't very convincing, but to her surprise, her body starts to respond."
        wt_image cheater_posing_1_12
        player.c "You're wet now, aren't you slut?"
        "She doesn't respond, but her hand shields her sex from your prying eyes."
        change lauren desire by 5 notify
      else:
        player.c "Play with yourself while I watch"
        wt_image cheater_posing_1_45
        "She turns around and gives you a look that lets you know she's reluctant to do this."
        wt_image cheater_posing_1_48
        "Despite that - or maybe because of that - she's embarrassed to find her body responding."
        if lauren.test('desire', 50):
          player.c "That's a good slut.  Go ahead.  Cum on your fingers while I watch."
          wt_image cheater_posing_1_48
          lauren.c "Y ... yes ...  aaahhhh!"
          call lauren_masturbation_stat_changes from _call_lauren_masturbation_stat_changes_1
          add tags 'orgasm_today' to lauren
        else:
          player.c "You're wet now, aren't you slut?  You don't think you want to do this, but your slut body knows better.  You just need to accept what your body already knows."
          add tags 'pleasured_today' to lauren
          change lauren desire by 5 notify
    "Have her open herself up more":
      $ lauren.open_her_count += 1
      if lauren.open_her_count == 1:
        player.c "You're awfully modest for a slut-in-training, Lauren.  When you lean over, I expect you to show off what you have to offer."
        wt_image cheater_posing_1_6
        "Tentatively, Lauren reaches back with one hand to spread her cheeks.  It's not much, but it's a start."
      elif lauren.open_her_count == 2:
        player.c "I can't see enough of you.  Open yourself up more."
        wt_image cheater_posing_1_6
        "Tentatively, Lauren reaches back with one hand to spread her cheeks."
        player.c "Wider than that.  Roll over and show me what you to offer."
        wt_image cheater_posing_1_50
        if lauren.test('sos', 15):
          player.c "Wider still."
          wt_image cheater_posing_1_13
          player.c "That's how an obedient slut presents herself to her man."
        else:
          "That's as much as she's willing to do right now."
      else:
        player.c "Open yourself up to me, slut."
        wt_image cheater_posing_1_50
        "She rolls over and gives you a good view."
        if lauren.test('sos',15):
          wt_image cheater_posing_1_13
          "Then she demonstrates that she's starting to accept her new role as obedient slut."
      call lauren_open_her_stat_changes from _call_lauren_open_her_stat_changes
    "Have her wait for you" if lauren.display_count_clothed > 1:
      $ lauren.wait_count += 1
      # first wait session
      if lauren.wait_count == 1:
        player.c "Stand up and remove the dress completely."
        wt_image cheater_posing_1_8
        player.c "Now crawl up on the table."
        wt_image cheater_posing_1_9
        player.c "You heard me."
        wt_image cheater_posing_1_10
        player.c "Turn around and face me."
        wt_image cheater_posing_1_14
        player.c "Wait there until I'm ready."
        wt_image cheater_posing_1_52
        "You go about your business, leaving the naked woman on your table waiting.  At first she's confused about why you're ignoring her."
        wt_image cheater_posing_1_53
        "Eventually she gets frustrated."
        lauren.c "Are you planning on leaving me here all night?"
        wt_image cheater_posing_1_52
        player.c "Do you know what an obedient slut is?  She's eye candy.  She's to be seen and not heard.  When I want you, I'll let you know.  Until then, stay there and look pretty."
        wt_image cheater_posing_1_53
        lauren.c "I'm a successful businesswoman ..."
        player.c "So you've told me.  And I'm sure you're used to speaking your mind.  We'll break you of that bad habit.  Stay girl."
        "She wants to tell you off.  She wants to get up and leave and never come back."
        wt_image cheater_posing_1_14
        "But she doesn't.  It's been another battle of wills and you won.  She knows it, and so do you."
      # second wait session
      elif lauren.wait_count == 2:
        player.c "I want you fully naked and on the table."
        wt_image cheater_posing_1_8
        "Lauren slides the dress off, keeping her eyes locked on you ..."
        wt_image cheater_posing_1_10
        "... then she gets up on the table, nervously awaiting your next instruction."
        wt_image cheater_posing_1_14
        player.c "Turn around and face me.  Now wait there."
        wt_image cheater_posing_1_52
        "She stays there while you go about your business.  She's not happy about it, but she stays quiet.  At least until you address her."
        wt_image cheater_posing_1_53
        player.c "Finally embracing the role of decoration?"
        lauren.c "No!"
        player.c "Why not?  Do you think we should be having an intellectual conversation while you kneel there?  Would that be more suited for the type of woman you are?"
        lauren.c "Ignoring your flawed premise that I should be kneeling at all, no I'm not interested in talking to you.  But I'm not used to being ignored, either."
        player.c "That's too bad, because when you're here, you're a decoration.  I don't care what's going on in your head.  I don't care if there's anything going on in there."
        lauren.c "Women are just objects to you?"
        wt_image cheater_posing_1_52
        player.c "Obedient sluts are just objects.  What gave you the idea I see you as a woman right now?  You're a slut-in-training, and I'll mold you into a pretty decoration yet."
        wt_image cheater_posing_1_14
        "She waits there quietly, feeling slightly sick to her stomach, fully aware that by obeying, she's giving you the power to potentially do exactly that."
      # third wait session
      elif lauren.wait_count == 3:
        player.c "Get yourself up on the table like a good decoration."
        wt_image cheater_posing_1_10
        "Lauren crawls up on the table ..."
        wt_image cheater_posing_1_14
        "... then turns around to face you.  You ignore her, as she knew you would."
        wt_image cheater_posing_1_52
        "She's nobody to you right now.  Just a table centerpiece for you to look at, should you want to.  She has no other purpose or role until you choose one for her."
        "No one's ever treated her like this ..."
        wt_image cheater_posing_1_53
        "... and she's shocked when she realizes she's getting wet from the experience."
        wt_image cheater_posing_1_14
        "She puts on a stoic face, trying to ignore you while you ignore her, and hoping desperately that you don't realize that being a decoration is turning her on."
        wt_image cheater_posing_1_53
        player.c "It's okay, slut.  Don't be embarrassed.  Being aroused just makes the waiting to be used more enjoyable."
      # additional sessions
      else:
        player.c "Up on the table and wait for me, slut."
        wt_image cheater_posing_1_8
        "Lauren strips ..."
        wt_image cheater_posing_1_14
        "... and gets into position."
        "You can take your time getting back to her.  She'll wait.  You know it and she knows it.  If you enjoy looking at her while she's waiting, she's okay with that, too."
      call lauren_wait_for_you_stat_changes from _call_lauren_wait_for_you_stat_changes
    "Nothing just yet" if lauren.display_count_clothed > 2:
        pass
  if lauren.display_count_clothed == 1:
    if lauren.has_tag('orgasm_today'):
      wt_image cheater_posing_1_40
      player.c "Go home now, Lauren.  Tell your husband you were a good obedient slut and came when I told you to."
    elif lauren.has_tag('pleasured_today'):
      wt_image cheater_posing_1_40
      player.c "Go home now, Lauren.  If you're lucky, your husband will do for you what you're wishing I would do right now."
    elif lauren.has_tag('spanked_today'):
      wt_image cheater_posing_1_49
      player.c "It's confusing, isn't it?  Your ass is sore, but your sex is warm and tingly.  Go home and see if you can figure it out, slut."
    else:
      wt_image cheater_posing_1_51
      player.c "Go home now, Lauren, and reflect on what you've learned about how to be a good slut."
  else:
    # second set of training options
    $ title = "What do you do with her now?"
    menu menu_lauren_display_clothes_1:
      "Use her for sex":
        if lauren.blowjob_count == 0:
          if lauren.test('desire', 10) or lauren.test('resistance', 50):
            player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
            wt_image cheater_posing_1_59
            "Lauren hesitates only a moment before crouching down in front of you.  Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
            wt_image cheater_posing_1_30
            "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
            wt_image cheater_posing_1_16
            player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
            wt_image cheater_posing_1_27
            player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now."
            wt_image cheater_posing_1_28
            player.c "Swallow me, right down to the base."
            wt_image cheater_posing_1_29
            player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
            wt_image cheater_posing_1_17
            "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
            wt_image cheater_posing_1_27
            "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
            wt_image cheater_posing_1_16
            player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
            wt_image cheater_posing_1_17
            "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
            wt_image cheater_posing_1_27
            "When she's learned as much as she can from one session, you empty your load in her."
            wt_image cheater_posing_1_28
            player.c "[player.orgasm_text]"
            wt_image cheater_posing_1_29
            player.c "Swallow it all."
            lauren.c "I did."
            wt_image cheater_posing_1_60
            player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
            $ lauren.blowjob_count += 1
            call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_3
            orgasm
          else:
            wt_image cheater_resisting_1
            lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
            wt_image cheater_initial_1
            "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
        else:
          $ title = "What do you want to do with her?"
          menu:
            "Test her oral skills":
              call lauren_display_clothes_oral from _call_lauren_display_clothes_oral
            "Fuck her" if lauren.sex_count == 0:
              call lauren_display_clothes_fuck from _call_lauren_display_clothes_fuck
            "Test her fucking skills" if lauren.sex_count >= 1:
              call lauren_display_clothes_fuck from _call_lauren_display_clothes_fuck_1
            "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
              call lauren_display_clothes_anal from _call_lauren_display_clothes_anal
            "Use the asswhore" if 'accepts_anal' in lauren.tags:
              call lauren_display_clothes_anal from _call_lauren_display_clothes_anal_1
            "Never mind":
              jump menu_lauren_display_clothes_1
      "Pleasure her":
        $ lauren.pleasure_her_count += 1
        player.c "Lean back and spread your legs."
        wt_image cheater_posing_1_45
        if lauren.pleasure_her_count == 1:
          if lauren.sex_count == 0:
            lauren.c "Wait, I'm not ..."
            wt_image cheater_posing_1_15
            "She doesn't have a chance to complete her objection before you surprise her by placing your mouth between her legs."
          else:
            lauren.c "What are you ..."
            wt_image cheater_posing_1_15
            lauren.c "Oh!"
          wt_image cheater_posing_1_57
          "Whatever she was expecting you to do with her, this wasn't it."
        else:
          "Lauren might be wet as soon as she opens her legs ..."
          wt_image cheater_posing_1_54
          "... if she wasn't, she certainly is by the time your mouth touches her."
          lauren.c "oooo"
        wt_image cheater_posing_1_25
        lauren.c "oooooo"
        if lauren.test('desire', 30):
          wt_image cheater_posing_1_56
          "The feel of your lips and tongue on her sex soon overwhelms Lauren."
          lauren.c "oooooo"
          wt_image cheater_posing_1_57
          "She groans as she climaxes and fills your mouth with her sticky juices."
          lauren.c "Y ... yes ... aaahhhh!"
          call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_6
        else:
          wt_image cheater_posing_1_55
          "Her mind and body never fully relax enough for her to cum, but her sex becomes sopping wet from your ministrations."
        wt_image cheater_hypno_1_12
        "You send Lauren home feeling happy about the way her training session ended."
        call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_1
        change player energy by -energy_short
      "Send her home":
        if lauren.has_tag('orgasm_today'):
          wt_image cheater_posing_1_40
          player.c "Go home now, Lauren.  Tell your husband you were a good obedient slut and came when I told you to."
        elif lauren.has_tag('pleasured_today'):
          wt_image cheater_posing_1_40
          player.c "Go home now, Lauren.  If you're lucky, your husband will do for you what you're wishing I would do right now."
        elif lauren.has_tag('spanked_today'):
          wt_image cheater_posing_1_49
          player.c "It's confusing, isn't it?  Your ass is sore, but your sex is warm and tingly.  Go home and see if you can figure it out, slut."
        else:
          wt_image cheater_posing_1_51
          player.c "Go home now, Lauren, and reflect on what you've learned about how to be a good slut."
  $ lauren.remove_tags('orgasm_today', 'pleasured_today', 'spanked_today')
  return

label lauren_display_lingerie:
  # if Lauren was given "classy" lingerie
  if lauren.has_tag('lingerie_classy'):
    $ lauren.display_count_lingerie += 1
    # first lingerie display (only happens after at least one clothed display)
    if lauren.display_count_lingerie == 1:
      player.c "Go change into the lingerie I bought you, Lauren."
      wt_image cheater_posing_2_17
      "A few minutes later, she reappears.  She looks good in these clothes and she knows it.  And she's rather pleased with you that you would see this and think of her."
      change lauren desire by 5 notify
      wt_image cheater_posing_2_1
      "She's still nervous, however, to be showing her body off to you in this way.  Her eyes search your face, looking for approval."
      player.c "Turn around and show me your ass."
      wt_image cheater_posing_2_19
      "Slowly Lauren turns, looking back at you over her shoulder."
      wt_image cheater_posing_2_2
      player.c "Not like that.  Get up on the table."
      wt_image cheater_posing_2_18
      "Nervously she climbs up."
      wt_image cheater_posing_2_3
      player.c "Now, turn around and show me your tits."
      wt_image cheater_posing_2_10
      "Lauren pulls down her top ..."
      if lauren.test('submission',20):
        wt_image cheater_posing_2_21
        "... and demurely drops her eyes as you inspect her bare breasts."
      else:
        wt_image cheater_posing_2_4
        "... and with a look that's part sulk, part scowl, waits as you inspect her breasts."
      player.c "Lose the corset, Lauren."
      wt_image cheater_posing_2_22
      "Lauren does as she's told ..."
      wt_image cheater_posing_2_5
      "... then waits for further instructions."
      player.c "Don't close your knees when I'm inspecting you, slut."
      wt_image cheater_posing_2_23
      player.c "Better, but lose the panties."
      wt_image cheater_posing_2_6
      player.c "Back on your knees, and turn around."
      wt_image cheater_posing_2_7
      "Trembling slightly, Lauren looks back at you, wondering what comes next."
    # subsequent lingerie display for classy
    else:
      player.c "Go change into your lingerie again, Lauren, then come back here.  I want to see that you remember how to follow directions."
      wt_image cheater_posing_2_26
      player.c "Do a turn."
      wt_image cheater_posing_2_19
      player.c "All the way, show off your ass."
      wt_image cheater_posing_2_2
      player.c "And your tits."
      wt_image cheater_posing_2_10
      "Lauren pulls down her top ..."
      if lauren.test('submission',20):
        wt_image cheater_posing_2_21
        "... and demurely drops her eyes as you inspect her bare breasts."
        player.c "Remove the corset."
        wt_image cheater_posing_2_23
      else:
        wt_image cheater_posing_2_4
        "... and with a look that's part sulk, part scowl, waits as you inspect her breasts."
        player.c "Remove the corset."
        wt_image cheater_posing_2_22
      player.c "And the panties."
      wt_image cheater_posing_2_6
      player.c "On your knees, facing away from me."
      wt_image cheater_posing_2_7
      "Nervously, Lauren waits for your next instructions."
    # first set of training options for classy
    $ title = "What do you do with her now?"
    menu:
      "Spank her":
        $ lauren.spank_count += 1
        wt_image cheater_spank_1
        "Without a word you lift up your hand and bring it down sharply on Lauren's bare bottom."
        lauren.c "Ow!"
        if lauren.spank_count == 1:
          wt_image cheater_posing_2_8
          "She knew her training was intended as a punishment, but she didn't know she would be literally punished."
          wt_image cheater_posing_2_24
          player.c "Get back in position.  Yes, you're being spanked like a naughty girl.  That's what happens when you're not obedient to your husband.  Tilt that ass up."
        else:
          wt_image cheater_posing_2_8
          player.c "Yes, you're being spanked again."
          wt_image cheater_posing_2_24
          player.c "Get back your ass back up."
        wt_image cheater_posing_2_25
        "*smack*"
        wt_image cheater_posing_2_37
        lauren.c "Ow!"
        wt_image cheater_posing_2_25
        "*smack*"
        wt_image cheater_posing_2_37
        lauren.c "Oww!"
        wt_image cheater_posing_2_25
        "*smack*"
        wt_image cheater_posing_2_37
        lauren.c "Owww!!"
        call lauren_spank_stat_changes from _call_lauren_spank_stat_changes_1
        add tags 'spanked_today' to lauren
      "Caress her":
        $ lauren.caress_her_count += 1
        wt_image cheater_posing_2_15
        "As you stroke your fingers along her sex, Lauren startles and sits up."
        player.c "Oh no you don't.  Get back into position."
        wt_image cheater_posing_2_24
        player.c "Further.  Tilt that ass right up."
        wt_image cheater_posing_2_7
        player.c "Now stay still."
        wt_image cheater_posing_2_27
        "You keep her there until you can tell - and she knows you can tell - that her body is responding to your caress."
        if lauren.test('desire',50):
          lauren.c "oooo"
        wt_image cheater_posing_2_28
        player.c "See how easy it is to be an obedient slut?  Just accept that your man can touch you when and how he wants."
        call lauren_caress_stat_changes from _call_lauren_caress_stat_changes_1
        add tags 'pleasured_today' to lauren
      "Have her touch herself" if lauren.caress_her_count > 0:
        if not lauren.has_tag('touched_herself'):
          add tags 'touched_herself' 'pleasured_today' to lauren
          player.c "Show me how you get yourself off."
          wt_image cheater_posing_2_1
          lauren.c "What?"
          player.c "Turn around and play with yourself, slut."
          wt_image cheater_posing_2_5
          lauren.c "While you watch?"
          player.c "Of course while I watch.  Get those legs up high so I have a clear view."
          wt_image cheater_posing_2_32
          lauren.c "I'm not going to be able to ... you know.  Not with you watching."
          player.c "Not going to be able to cum like an obedient slut?  Not if you don't start rubbing yourself you won't."
          wt_image cheater_posing_2_11
          "Awkwardly, Lauren goes through the motions of faking masturbation.  It isn't very convincing, but to her surprise, her body starts to respond."
          wt_image cheater_posing_2_12
          player.c "You're wet now, aren't you slut?"
          "She doesn't respond, but her hand shields her sex from your prying eyes."
          change lauren desire by 5 notify
        else:
          player.c "Play with yourself while I watch"
          wt_image cheater_posing_2_32
          "She turns around and gives you a look that lets you know she's reluctant to do this."
          wt_image cheater_posing_2_11
          "Despite that - or maybe because of that - she's embarrassed to find her body responding."
          if lauren.test('desire', 50):
            player.c "That's a good slut.  Go ahead.  Cum on your fingers while I watch."
            wt_image cheater_posing_2_33
            lauren.c "Y ... yes ...  aaahhhh!"
            call lauren_masturbation_stat_changes from _call_lauren_masturbation_stat_changes_2
            add tags 'orgasm_today' to lauren
          else:
            wt_image cheater_posing_2_12
            player.c "You're wet now, aren't you slut?  You don't think you want to do this, but your slut body knows better.  You just need to accept what your body already knows."
            add tags 'pleasured_today' to lauren
            change lauren desire by 5 notify
      "Have her open herself up more":
        $ lauren.open_her_count += 1
        if lauren.open_her_count == 1:
          player.c "You're awfully modest for a slut-in-training, Lauren.  When you lean over, I expect you to show off what you have to offer."
          wt_image cheater_posing_2_9
          "Tentatively, Lauren reaches back with one hand to spread her cheeks.  It's not much, but it's a start."
        elif lauren.open_her_count == 2:
          player.c "I can't see enough of you.  Open yourself up more."
          wt_image cheater_posing_2_9
          "Tentatively, Lauren reaches back with one hand to spread her cheeks."
          player.c "Wider than that.  Roll over and show me what you to offer."
          wt_image cheater_posing_2_13
          if lauren.test('sos',15):
            player.c "Wider still."
            wt_image cheater_posing_2_14
            player.c "That's how an obedient slut presents herself to her man."
          else:
            "That's as much as she's willing to do right now."
        else:
          player.c "Open yourself up to me, slut."
          wt_image cheater_posing_2_13
          "She rolls over and gives you a good view."
          if lauren.test('sos',15):
            wt_image cheater_posing_2_14
            "Then she demonstrates that she's starting to accept her new role as obedient slut."
        call lauren_open_her_stat_changes from _call_lauren_open_her_stat_changes_1
      "Have her wait for you" if lauren.display_count_clothed > 1:
        $ lauren.wait_count += 1
        # first wait session
        if lauren.wait_count == 1:
          player.c "Kneel there and wait until I'm ready."
          wt_image cheater_posing_2_24
          "You go about your business, leaving the naked woman on your table waiting.  At first she's confused about why you're ignoring her."
          wt_image cheater_posing_2_35
          "Eventually she gets frustrated."
          lauren.c "Are you planning on leaving me here all night?"
          player.c "Do you know what an obedient slut is?  She's eye candy.  She's to be seen and not heard.  When I want you, I'll let you know.  Until then, stay there and look pretty."
          wt_image cheater_posing_2_34
          lauren.c "I'm a successful businesswoman ..."
          player.c "So you've told me.  And I'm sure you're used to speaking your mind.  We'll break you of that bad habit.  Stay girl."
          wt_image cheater_posing_2_36
          "She wants to tell you off.  She wants to get up and leave and never come back."
          wt_image cheater_posing_2_15
          "But she doesn't.  It's been another battle of wills and you won.  She knows it, and so do you."
        # second wait session
        elif lauren.wait_count == 2:
          player.c "Kneel there and wait until I'm ready."
          wt_image cheater_posing_2_24
          "She stays there while you go about your business.  She's not happy about it, but she stays quiet.  At least until you address her."
          player.c "Finally embracing the role of decoration?"
          wt_image cheater_posing_2_34
          lauren.c "No!"
          player.c "Why not?  Do you think we should be having an intellectual conversation while you kneel there?  Would that be more suited for the type of woman you are?"
          lauren.c "Ignoring your flawed premise that I should be kneeling at all, no I'm not interested in talking to you.  But I'm not used to being ignored, either."
          player.c "That's too bad, because when you're here, you're a decoration.  I don't care what's going on in your head.  I don't care if there's anything going on in there."
          lauren.c "Women are just objects to you?"
          wt_image cheater_posing_2_35
          player.c "Obedient sluts are just objects.  What gave you the idea I see you as a woman right now?  You're a slut-in-training, and I'll mold you into a pretty decoration yet."
          wt_image cheater_posing_2_24
          "She waits there quietly, feeling slightly sick to her stomach, fully aware that by obeying, she's giving you the power to potentially do exactly that."
        # third wait session
        elif lauren.wait_count == 3:
          player.c "Wait there for me like a good decoration."
          wt_image cheater_posing_2_24
          "You ignore her, as she knew you would."
          wt_image cheater_posing_2_15
          "She's nobody to you right now.  Just a table centerpiece for you to look at, should you want to.  She has no other purpose or role until you choose one for her."
          "No one's ever treated her like this ..."
          wt_image cheater_posing_2_36
          "... and she's shocked when she realizes she's getting wet from the experience."
          wt_image cheater_posing_2_25
          "She puts on a stoic face, trying to ignore you while you ignore her, and hoping desperately that you don't realize that being a decoration is turning her on."
          wt_image cheater_posing_2_37
          player.c "It's okay, slut.  Don't be embarrassed.  Being aroused just makes the waiting to be used more enjoyable."
        # additional sessions
        else:
          player.c "Kneel there and wait for me like a good decoration, slut."
          wt_image cheater_posing_2_25
          "You can take your time getting back to her.  She'll wait.  You know it and she knows it."
          wt_image cheater_posing_2_36
          "If you enjoy looking at her while she's waiting, she's okay with that, too."
        call lauren_wait_for_you_stat_changes from _call_lauren_wait_for_you_stat_changes_1
      "Nothing just yet" if lauren.display_count_clothed > 1 or lauren.display_count_lingerie > 1 or lauren.display_count_office > 1:
        pass
    # second set of training options for classy
    $ title = "What do you do next?"
    menu menu_lauren_display_lingerie_classy_1:
      "Use her for sex":
        if lauren.blowjob_count == 0:
          if lauren.test('desire', 10) or lauren.test('resistance', 50):
            player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
            wt_image cheater_blow_job_9
            "Lauren hesitates only a moment before crouching down in front of you.  Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
            wt_image cheater_blow_job_10
            "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
            wt_image cheater_blow_job_11
            player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
            wt_image cheater_blow_job_13
            player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now."
            wt_image cheater_blow_job_12
            player.c "Swallow me, right down to the base."
            wt_image cheater_blow_job_3
            player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth."
            wt_image cheater_blow_job_12
            player.c "Start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
            wt_image cheater_blow_job_4
            "With your hand on her head, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
            wt_image cheater_blow_job_3
            "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
            wt_image cheater_blow_job_2
            player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
            wt_image cheater_blow_job_14
            "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
            wt_image cheater_blow_job_6
            "When she's learned as much as she can from one session, you empty your load in her."
            wt_image cheater_blow_job_15
            player.c "[player.orgasm_text]"
            wt_image cheater_blow_job_14
            player.c "Swallow it all."
            wt_image cheater_blow_job_16
            lauren.c "I did."
            wt_image cheater_blow_job_9
            player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
            $ lauren.blowjob_count += 1
            call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_4
            orgasm
          else:
            wt_image cheater_posing_2_38
            lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
            wt_image cheater_posing_2_31
            "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
        else:
          $ title = "What do you want to do with her?"
          menu:
            "Test her oral skills":
              call lauren_display_lingerie_oral from _call_lauren_display_lingerie_oral
            "Fuck her" if lauren.sex_count == 0:
              call lauren_display_lingerie_fuck from _call_lauren_display_lingerie_fuck
            "Test her fucking skills" if lauren.sex_count >= 1:
              call lauren_display_lingerie_fuck from _call_lauren_display_lingerie_fuck_1
            "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
              call lauren_display_lingerie_anal from _call_lauren_display_lingerie_anal
            "Use the asswhore" if 'accepts_anal' in lauren.tags:
              call lauren_display_lingerie_anal from _call_lauren_display_lingerie_anal_1
            "Never mind":
              jump menu_lauren_display_lingerie_classy_1
      "Pleasure her":
        $ lauren.pleasure_her_count += 1
        player.c "Lean back and open your legs."
        wt_image cheater_posing_2_43
        if lauren.pleasure_her_count == 1:
          if lauren.sex_count == 0:
            lauren.c "Wait, I'm not ..."
            wt_image cheater_fingered_2
            "She doesn't have a chance to complete her objection before you surprise her by placing your fingers inside her.  Whatever she was expecting, this wasn't it."
          else:
            lauren.c "What are you ..."
            wt_image cheater_fingered_2
          lauren.c "Oh!"
        else:
          "Lauren might be wet as soon as she leans back ..."
          wt_image cheater_fingered_2
          "... if she wasn't, she certainly is by the time your fingers touch her."
          lauren.c "oooo"
        wt_image cheater_fingered_3
        lauren.c "oooooo"
        if lauren.test('desire', 30):
          wt_image cheater_fingered_1
          "The feel of your fingers insider her soon overwhelms Lauren and she cums hard, bucking her hips against your hand."
          lauren.c "Y ... yes ... aaahhhh!"
          call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_7
        else:
          "Her mind and body never fully relax enough for her to cum, but her sex becomes sopping wet from your ministrations."
        wt_image cheater_posing_2_21
        "You send Lauren home feeling happy about the way her training session ended."
        call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_2
        change player energy by -energy_short
      "Send her home":
        if lauren.has_tag('orgasm_today'):
          wt_image cheater_posing_2_17
          player.c "Go home now, Lauren.  Tell your husband you were a good obedient slut and came when I told you to."
        elif lauren.has_tag('pleasured_today'):
          wt_image cheater_posing_2_30
          player.c "Go home now, Lauren.  If you're lucky, your husband will do for you what you're wishing I would do right now."
        elif lauren.has_tag('spanked_today'):
          wt_image cheater_posing_2_29
          player.c "It's confusing, isn't it?  Your ass is sore, but your sex is warm and tingly.  Go home and see if you can figure it out, slut."
        else:
          wt_image cheater_posing_2_31
          player.c "Go home now, Lauren, and reflect on what you've learned about how to be a good slut."
  # if Lauren was given "classy" lingerie
  elif lauren.has_tag('lingerie_slutty'):
    $ lauren.display_count_lingerie += 1
    # first lingerie display (only happens after at least one clothed display)
    if lauren.display_count_lingerie == 1:
      player.c "Go change into the lingerie I bought you, Lauren."
      wt_image cheater_posing_3_1
      "A few minutes later, she reappears.  She looks like a whore in these clothes and she knows it.  She also knows that's how you and her husband expect her to look."
      player.c "You're looking the part of an obedient slut now, Lauren.  Are you feeling the part?"
      "She says nothing, but inside she knows that just be willing to wear this outfit for you means that she's turning into an obedient slut."
      change lauren sos by 5 notify
      player.c "Turn around and show me your ass."
      wt_image cheater_posing_3_38
      "Slowly Lauren turns, looking back at you over her shoulder."
      player.c "Come on slut, show your ass off."
      wt_image cheater_posing_3_39
      player.c "Not like that.  Stick it out so I get a good look."
      wt_image cheater_posing_3_2
      player.c "Get down on the floor.  And spread your knees when you're showing me your ass."
      wt_image cheater_posing_3_3
      player.c "A little better.  Now, turn around and show me your tits."
      wt_image cheater_posing_3_41
      "Lauren turns around ..."
      wt_image cheater_posing_3_40
      "... and pulls down her top."
      wt_image cheater_posing_3_4
      "With a look that's part sulk, part scowl, she waits as you inspect her breasts."
      player.c "Quit scowling and pull down your panties, slut."
      wt_image cheater_posing_3_5
      player.c "Back on your knees, ass up."
      wt_image cheater_posing_3_6
      "Trembling slightly, Lauren looks back at you, wondering what comes next."
    # subsequent lingerie display for slutty
    else:
      player.c "Go change into your lingerie again, Lauren, then come back here.  I want to see that you remember how to follow directions."
      wt_image cheater_posing_3_1
      player.c "Do a turn."
      wt_image cheater_posing_3_38
      player.c "All the way, show off your ass."
      wt_image cheater_posing_3_2
      player.c "And your tits."
      wt_image cheater_posing_3_40
      "Lauren pulls down her top ..."
      wt_image cheater_posing_3_4
      "... so you can inspect her breasts."
      player.c "Lose the panties, too."
      wt_image cheater_posing_3_5
      player.c "On your knees, facing away from me."
      wt_image cheater_posing_3_6
      "Nervously, Lauren waits for your next instructions."
    # first set of training options for slutty
    $ title = "What do you do with her now?"
    menu:
      "Spank her":
        $ lauren.spank_count += 1
        wt_image cheater_spank_1
        "Without a word you lift up your hand and bring it down sharply on Lauren's bare bottom."
        lauren.c "Ow!"
        if lauren.spank_count == 1:
          wt_image cheater_posing_3_8
          "She knew her training was intended as a punishment, but she didn't know she would be literally punished."
          player.c "Yes, you're being spanked like a naughty girl.  That's what happens when you're not obedient to your husband.  Tilt that ass up."
        else:
          wt_image cheater_posing_3_8
          player.c "Yes, you're being spanked again."
        wt_image cheater_posing_3_42
        "*smack*"
        lauren.c "Ow!"
        "*smack*"
        lauren.c "Oww!"
        "*smack*"
        lauren.c "Owww!!"
        call lauren_spank_stat_changes from _call_lauren_spank_stat_changes_2
        add tags 'spanked_today' to lauren
      "Caress her":
        $ lauren.caress_her_count += 1
        wt_image cheater_posing_3_43
        "You turn Lauren over and run your fingers along her sex.  She gasps in surprise and tries to close her legs, but a hand on her knee opens her up again and pins her in position."
        wt_image cheater_posing_3_7
        "You keep her there until you can tell - and she knows you can tell - that her body is responding to your caress."
        if lauren.test('desire',50):
          lauren.c "oooo"
          wt_image cheater_posing_3_10
        player.c "See how easy it is to be an obedient slut?  Just accept that your man can touch you when and how he wants."
        call lauren_caress_stat_changes from _call_lauren_caress_stat_changes_2
        add tags 'pleasured_today' to lauren
      "Have her touch herself" if lauren.caress_her_count > 0:
        if not lauren.has_tag('touched_herself'):
          add tags 'touched_herself' 'pleasured_today' to lauren
          player.c "Show me how you get yourself off."
          wt_image cheater_posing_3_12
          lauren.c "What?"
          player.c "Turn around and play with yourself, slut."
          lauren.c "While you watch?"
          player.c "Of course while I watch.  Get those legs spread wide so I have a clear view."
          wt_image cheater_masturbating_1
          lauren.c "I'm not going to be able to ... you know.  Not with you watching."
          player.c "Not going to be able to cum like an obedient slut?  Not if you don't start rubbing yourself you won't."
          wt_image cheater_masturbating_2
          "Awkwardly, Lauren goes through the motions of faking masturbation.  It isn't very convincing, but to her surprise, her body starts to respond."
          wt_image cheater_masturbating_3
          player.c "You're wet now, aren't you slut?"
          "She doesn't respond, but her hand shields her sex from your prying eyes."
          change lauren desire by 5 notify
        else:
          wt_image cheater_posing_3_12
          player.c "Play with yourself while I watch"
          wt_image cheater_masturbating_1
          "She turns around and gives you a look that lets you know she's reluctant to do this."
          wt_image cheater_masturbating_2
          "Despite that - or maybe because of that - she's embarrassed to find her body responding."
          if lauren.test('desire', 50):
            wt_image cheater_masturbating_4
            player.c "That's a good slut.  Go ahead.  Cum on your fingers while I watch."
            wt_image cheater_masturbating_5
            lauren.c "Y ... yes ...  aaahhhh!"
            call lauren_masturbation_stat_changes from _call_lauren_masturbation_stat_changes_3
            add tags 'orgasm_today' to lauren
          else:
            wt_image cheater_masturbating_3
            player.c "You're wet now, aren't you slut?  You don't think you want to do this, but your slut body knows better.  You just need to accept what your body already knows."
            add tags 'pleasured_today' to lauren
            change lauren desire by 5 notify
      "Have her open herself up more":
        $ lauren.open_her_count += 1
        if lauren.open_her_count == 1:
          wt_image cheater_posing_3_12
          player.c "You're awfully modest for a slut-in-training, Lauren.  When you model for me, I expect you to show off everything you have to offer."
          wt_image cheater_posing_3_9
          "Tentatively, Lauren reaches down and spreads her labia.  It's a start."
        elif lauren.open_her_count == 2:
          wt_image cheater_posing_3_12
          player.c "Let's see what you have to offer, slut."
          wt_image cheater_posing_3_9
          player.c "You can do better than that.  All the way open, this time.  I want to see all three holes at once."
          if lauren.test('sos',15):
            wt_image cheater_posing_3_44
            player.c "That's how an obedient slut presents herself to her man."
          else:
            wt_image cheater_posing_3_11
            "That's as much as she's willing to do right now."
        else:
          wt_image cheater_posing_3_12
          player.c "Open yourself up to me, slut."
          wt_image cheater_posing_3_9
          "She turns around and gives you a good view ..."
          if lauren.test('sos',15):
            wt_image cheater_posing_3_44
            "... then she demonstrates that she's starting to accept her new role as obedient slut."
          else:
            wt_image cheater_posing_3_11
            "... then tentatively opens herself a little wider."
        call lauren_open_her_stat_changes from _call_lauren_open_her_stat_changes_2
      "Have her wait for you" if lauren.display_count_clothed > 1:
        $ lauren.wait_count += 1
        # first wait session
        if lauren.wait_count == 1:
          player.c "Kneel there and wait until I'm ready."
          wt_image cheater_posing_3_6
          "You go about your business, leaving the naked woman waiting.  At first she's confused about why you're ignoring her."
          wt_image cheater_posing_3_12
          "Eventually she gets frustrated."
          lauren.c "Are you planning on leaving me here all night?"
          player.c "Do you know what an obedient slut is?  She's eye candy.  She's to be seen and not heard.  When I want you, I'll let you know.  Until then, stay there and look pretty."
          wt_image cheater_posing_3_45
          lauren.c "I'm a successful businesswoman ..."
          player.c "So you've told me.  And I'm sure you're used to speaking your mind.  We'll break you of that bad habit.  Back down on the ground and stay girl."
          "She wants to tell you off.  She wants to get up and leave and never come back."
          wt_image cheater_posing_3_6
          "But she doesn't.  It's been another battle of wills and you won.  She knows it, and so do you."
        # second wait session
        elif lauren.wait_count == 2:
          player.c "Kneel there and wait until I'm ready."
          wt_image cheater_posing_3_6
          "She stays there while you go about your business.  She's not happy about it, but she stays quiet.  At least until you address her."
          player.c "Finally embracing the role of decoration?"
          wt_image cheater_posing_3_12
          lauren.c "No!"
          player.c "Why not?  Do you think we should be having an intellectual conversation while you kneel there?  Would that be more suited for the type of woman you are?"
          wt_image cheater_posing_3_45
          lauren.c "Ignoring your flawed premise that I should be kneeling at all, no I'm not interested in talking to you.  But I'm not used to being ignored, either."
          player.c "That's too bad, because when you're here, you're a decoration.  I don't care what's going on in your head.  I don't care if there's anything going on in there."
          lauren.c "Women are just objects to you?"
          wt_image cheater_posing_3_12
          player.c "Obedient sluts are just objects.  What gave you the idea I see you as a woman right now?  You're a slut-in-training, and I'll mold you into a pretty decoration yet."
          player.c "Head down and ass up, decoration."
          wt_image cheater_posing_3_6
          "She waits there quietly, feeling slightly sick to her stomach, fully aware that by obeying, she's giving you the power to potentially do exactly that."
        # third wait session
        elif lauren.wait_count == 3:
          player.c "Wait there for me like a good decoration."
          wt_image cheater_posing_3_6
          "You ignore her, as she knew you would.  She's nobody to you right now.  Just an object to look at, should you want to.  She has no other purpose or role until you choose one for her.  No one's ever treated her like this ..."
          wt_image cheater_posing_3_37
          "... and she's shocked when she realizes she's getting wet from the experience."
          wt_image cheater_posing_3_12
          "She puts on a stoic face, hoping desperately that you don't realize that being a decoration is turning her on."
          wt_image cheater_posing_3_6
          player.c "Ass up, head down.  Don't be embarrassed, object.  Being aroused just makes the waiting to be used more enjoyable."
        # additional sessions
        else:
          player.c "Kneel there and wait for me like a good decoration, slut."
          wt_image cheater_posing_3_6
          "You can take your time getting back to her.  She'll wait.  You know it and she knows it."
          wt_image cheater_posing_3_37
          "If you enjoy looking at her while she's waiting, she's okay with that, too."
        call lauren_wait_for_you_stat_changes from _call_lauren_wait_for_you_stat_changes_2
      "Nothing just yet" if lauren.display_count_clothed > 1 or lauren.display_count_lingerie > 1 or lauren.display_count_office > 1:
        pass
    # second set of training options for slutty
    $ title = "What do you do next?"
    menu menu_lauren_display_lingerie_slutty_1:
      "Use her for sex":
        if lauren.blowjob_count == 0:
          if lauren.test('desire', 10) or lauren.test('resistance', 50):
            player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
            wt_image cheater_posing_3_49
            "Lauren hesitates only a moment before taking your cock in her hand.  Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
            wt_image cheater_posing_3_14
            "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
            wt_image cheater_posing_3_50
            player.c "Not like that.  Use more of your tongue.  Back and forth along the head of my cock."
            wt_image cheater_posing_3_51
            player.c "Slow down.  I'll tell you when it's time to speed up."
            wt_image cheater_posing_3_16
            player.c "Swallow me, right down to the base."
            wt_image cheater_posing_3_15
            player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth."
            wt_image cheater_posing_3_51
            player.c "Start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
            wt_image cheater_posing_3_15
            "With your hand on her head, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
            wt_image cheater_posing_3_14
            "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
            wt_image cheater_posing_3_16
            player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now. Start again, at the beginning."
            wt_image cheater_posing_3_15
            "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
            wt_image cheater_posing_3_51
            "When she's learned as much as she can from one session, you empty your load in her."
            wt_image cheater_posing_3_52
            player.c "[player.orgasm_text]"
            player.c "Swallow it all."
            wt_image cheater_posing_3_53
            lauren.c "I did."
            player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
            $ lauren.blowjob_count += 1
            call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_5
            orgasm
          else:
            wt_image cheater_posing_3_4
            lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
            wt_image cheater_posing_3_1
            "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
        else:
          $ title = "What do you want to do with her?"
          menu:
            "Test her oral skills":
              call lauren_display_lingerie_oral from _call_lauren_display_lingerie_oral_1
            "Fuck her" if lauren.sex_count == 0:
              call lauren_display_lingerie_fuck from _call_lauren_display_lingerie_fuck_2
            "Test her fucking skills" if lauren.sex_count >= 1:
              call lauren_display_lingerie_fuck from _call_lauren_display_lingerie_fuck_3
            "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
              call lauren_display_lingerie_anal from _call_lauren_display_lingerie_anal_2
            "Use the asswhore" if 'accepts_anal' in lauren.tags:
              call lauren_display_lingerie_anal from _call_lauren_display_lingerie_anal_3
            "Never mind":
              jump menu_lauren_display_lingerie_slutty_1
      "Pleasure her":
        $ lauren.pleasure_her_count += 1
        player.c "Lean back and open your legs."
        if lauren.pleasure_her_count == 1:
          wt_image cheater_posing_3_4
          if lauren.sex_count == 0:
            lauren.c "Wait, I'm not ..."
            wt_image cheater_posing_3_47
            "She doesn't have a chance to complete her objection before you surprise her by placing your fingers on her.  Whatever she was expecting, this wasn't it."
          else:
            lauren.c "What are you ..."
            wt_image cheater_posing_3_47
          lauren.c "Oh!"
        else:
          wt_image cheater_posing_3_10
          "Lauren might be wet as soon as she leans back ..."
          wt_image cheater_posing_3_47
          "... if she wasn't, she certainly is by the time your fingers touch her."
          lauren.c "oooo"
        wt_image cheater_posing_3_22
        lauren.c "oooooo"
        if lauren.test('desire', 30):
          wt_image cheater_posing_3_23
          "The feel of your fingers insider her soon overwhelms Lauren and she cums hard, bucking her hips and surprising both of you by squirting over your hand."
          lauren.c "Y ... yes ... aaahhhh!"
          wt_image cheater_posing_3_46
          lauren.c "OH!  I'm so sorry!!  I don't normally do that."
          player.c "Do what?  Make a mess all over the floor when you cum?  Maybe you should wear slutty clothes more often.  It seems to excite you."
          call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_8
          wt_image cheater_posing_3_48
          "You send Lauren home feeling happy, if a bit embarrassed, about the way her training session ended."
        else:
          "Her mind and body never fully relax enough for her to cum, but her sex becomes sopping wet from your ministrations."
          wt_image cheater_posing_3_48
          "You send Lauren home feeling happy about the way her training session ended."
        call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_3
        change player energy by -energy_short
      "Send her home":
        if lauren.has_tag('orgasm_today'):
          wt_image cheater_posing_3_48
          player.c "Go home now, Lauren.  Tell your husband you were a good obedient slut and came when I told you to."
        elif lauren.has_tag('pleasured_today'):
          wt_image cheater_posing_3_48
          player.c "Go home now, Lauren.  If you're lucky, your husband will do for you what you're wishing I would do right now."
        elif lauren.has_tag('spanked_today'):
          wt_image cheater_posing_3_39
          player.c "It's confusing, isn't it?  Your ass is sore, but your sex is warm and tingly.  Go home and see if you can figure it out, slut."
        else:
          wt_image cheater_posing_3_38
          player.c "Go home now, Lauren, and reflect on what you've learned about how to be a good slut."
  # error as no lingerie tag identified
  else:
    sys "There's been an error in the lauren_display_lingerie label.  Lauren was not identified as having an appropriate lingerie tag."
  $ lauren.remove_tags('orgasm_today', 'pleasured_today', 'spanked_today')
  return

# Punish Her
label lauren_punish:
    $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    # note: temp count 1 is to flag that day ends at completion of this action; reset to 0 if choices lead to action being cancelled
    $ lauren.temporary_count = 1
    if current_location != dungeon:
        call forced_movement(dungeon) from _call_forced_movement_148
    if lauren.punishment_count == 0:
        wt_image cheater_punishment_1_1
        lauren.c "What is this?"
        player.c "The place I take naughty girls to be punished."
        wt_image cheater_punishment_1_14
        lauren.c "You want to punish me?"
        player.c "Yes.  First, for cheating on your husband. Then, when I think you've suffered enough for that, I'll continue to punish you until you're ready to be obedient to your husband. Truly obedient."
        wt_image cheater_punishment_1_1
        lauren.c "You think that hurting me will make me obedient?"
        player.c "As a matter of fact, I do."
        # note: test is on unmodified
        if lauren.submission > 0:
            $ lauren.punishment_count = 1
            "Lauren holds your gaze steadily, but her voice wavers a little as she replies."
            lauren.c "What are you going to do with me?"
            player.c "Whatever I want."
            "Seeing the fear in her eyes, you decide to continue, before she balks."
            player.c "I will hurt you, Lauren, but I won't harm you. You won't be cut or injured, although you may be bruised. You won't be raped. Today you won't even be fucked, because today is about punishment."
            player.c "You will offer your body to me for my pleasure on another day. Today you'll offer it to me so that I may punish you as a lesson in what happens to sluts who aren't obedient to their husband."
            player.c "Is that understood?"
            lauren.c "I guess so."
            player.c "Good.  Get undressed."
            wt_image cheater_punishment_1_2
            "You adjust the lights and rearrange the equipment in the room as she strips.  She watches you nervously."
            player.c "Come over here, these fittings should be just about right for you, but I may need to adjust a few of them."
            wt_image cheater_punishment_1_3
            "In a few minutes you have her immobilized and are able to step back and examine her."
            player.c "That seems like an appropriate punishment position for a cheating slut, wouldn't you say Lauren?"
            player.c "Spreading your legs got you into this predicament, so it only seems fair that your punishment involve you keeping your legs open."
            "She says nothing and avoids your gaze, trying hard to keep herself from crying."
            player.c "Answering my questions isn't optional, Lauren."
            wt_image cheater_punishment_1_4
            "You pinch her nipple hard while shoving two fingers into her sex.  She cries out in surprise and pain."
            lauren.c "Ow!"
            player.c "Let's try again.  Wouldn't you say this is an appropriate position to punish a cheating slut, Lauren?"
            lauren.c "Y ..  y ..  yess"
            player.c "Good, I'm glad we have that established."
            if dungeon.has_item(floggers):
                wt_image cheater_punishment_1_5
                "You take one of your floggers and begin to whip her vulnerable breasts.  She cries out in pain even though the beating is quite mild.  Ironically, the endorphins you stimulate will make the rest of the punishment easier for her, although she's in no position to appreciate that."
                lauren.c "Ow!!  Ow!!!"
            player.c "Let's move on to the main event now, shall we? ... I said shall we, Lauren?"
            lauren.c "Y ..  y .. yess"
            wt_image cheater_punishment_1_10
            "You slip two heavy rubber bands over each of Lauren's feet.  At first she's not sure what you're doing."
            wt_image cheater_punishment_1_6
            "Then, when she sees you stretch the bands out, she starts to cry, even before you let the bands go."
            wt_image cheater_punishment_1_7
            "When you do let the bands go, they strike the soles of her feet with a hard *THWAPPP* that is followed immediately by the sounds of Lauren's screaming."
            lauren.c "Aaaahhhhhh!!!!!  No ... No ... please, I'm begging you!  Don't do this.  I've learned my lesson.  I'll be good!  I'll be obedient!!  I won't cheat on my husband.  I promise!"
            lauren.c "I'll follow your orders.  I'll do whatever you tell me to.  Just please don't hurt me anymore!!"
            $ title = "What do you do?"
            menu:
                "Let her go, she's learned her lesson":
                    wt_image cheater_punishment_1_8
                    "You release Lauren from her bonds and she slumps to the floor at your feet."
                    lauren.c "Thank you.  Thank you.  I promise I'll be good.  No more punishments."
                    if lauren.blowjob_count > 0:
                        wt_image cheater_punishment_1_12
                        "To your surprise, Lauren takes out your cock and through her tears proceeds to lick you."
                        lauren.c "See?  I can be an obedient slut.  Tell me how you want me to suck your cock and I'll do it."
                        $ title = "Give her a blow job lesson?"
                        menu:
                            "Yes":
                                $ lauren.blowjob_count += 1
                                if lauren.blowjob_count == 2:
                                    call lauren_second_blowjob from _call_lauren_second_blowjob_3
                                    wt_image cheater_punishment_1_12
                                    player.c "Now you can go back to sucking my cock."
                                elif lauren.blowjob_count == 3:
                                    wt_image cheater_ball_lick_1
                                    "Lauren takes your balls into her mouth and warms them up ..."
                                    wt_image cheater_punishment_1_13
                                    "... before shifting attention to your cock."
                                    wt_image cheater_punishment_1_12
                                    call lauren_third_blowjob from _call_lauren_third_blowjob_3
                                elif lauren.blowjob_count == 4:
                                    wt_image cheater_ball_lick_1
                                    "Lauren seems to have mastered her training."
                                    wt_image cheater_punishment_1_13
                                    "She warms up your balls nicely before she sucks your cock."
                                    wt_image cheater_punishment_1_12
                                    call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_3
                                else:
                                    wt_image cheater_ball_lick_1
                                    "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
                                    wt_image cheater_punishment_1_12
                                    "... then sucks your cock."
                                wt_image cheater_punishment_1_13
                                "You relax and enjoy the rest of the blowjob ..."
                                wt_image cheater_punishment_1_9
                                "... as she uses her mouth ..."
                                wt_image cheater_punishment_1_12
                                "... and tongue ..."
                                wt_image cheater_punishment_1_13
                                "... to get you ready."
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her mouth":
                                        wt_image cheater_punishment_1_9
                                        "You hold her head in place as you unload your cum down the back of her throat."
                                        player.c "[player.orgasm_text]"
                                        if lauren.blowjob_count > 3:
                                            call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change
                                        player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
                                    "On her face" if lauren.blowjob_count > 3:
                                        add tags 'facial_today' to lauren
                                        if lauren.facial_count == 1:
                                            wt_image cheater_punishment_1_12
                                            "Lauren looks up in surprise as you pull your cock out of her mouth, then quickly closes her eyes as she realizes what you're doing."
                                            wt_image cheater_facial_1
                                            player.c "[player.orgasm_text]"
                                            wt_image cheater_facial_2
                                            "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                                            wt_image cheater_facial_4
                                            player.c "Clean yourself up, slut, then go home."
                                        elif lauren.facial_count == 2:
                                            wt_image cheater_punishment_1_12
                                            "As you pull out of her mouth, Lauren knows what to expect."
                                            wt_image cheater_facial_1
                                            player.c "[player.orgasm_text]"
                                            wt_image cheater_facial_2
                                            "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                                            wt_image cheater_facial_4
                                            player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                                            wt_image cheater_facial_2
                                            lauren.c "You can't expect me to go home like this?"
                                            player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                                            lauren.c "Yes"
                                        else:
                                            wt_image cheater_punishment_1_12
                                            "As you pull out of her mouth, Lauren licks the underside of your cock while offering her face as a target."
                                            wt_image cheater_facial_1
                                            player.c "[player.orgasm_text]"
                                            wt_image cheater_facial_5
                                            "She doesn't try to clean herself this time."
                                            wt_image cheater_facial_6
                                            "She does, however, clean off the tip of your cock as she looks up at you."
                                            wt_image cheater_facial_3
                                            "You leave her like that for a while, licking your cock and wearing your cum as she kneels on your floor, waiting to be dismissed and sent home to her husband."
                                        add tags 'facial_today' to lauren
                                call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_6
                                orgasm
                            "No":
                                wt_image cheater_punishment_1_8
                                player.c "Not today, slut.  Obedient means you get my cock when I tell you you can have it."
                    add tags 'no_punishment' to lauren
                    change lauren desire by 5
                    change lauren resistance by -10
                    change player energy by -energy_short notify
                "Continue her punishment":
                    player.c "Don't be silly, Lauren.  Your punishment has just begun, and it'll continue until I'm satisfied that you've learned as much of your lesson as you can absorb for today."
                    wt_image cheater_punishment_1_10
                    "You pull back the rubber bands, much further this time."
                    wt_image cheater_punishment_1_7
                    "*TTHHHWWAAAAPPPP!!!!*"
                    lauren.c "AAAARRRGGGHHHHHHHH!!!!!!!!"
                    wt_image cheater_punishment_1_6
                    "As you prepare the bands again, this time there's no pleading, no begging.  Just a loud, long guttural groan as Lauren tries to deal with the pain radiating from her feet."
                    wt_image cheater_punishment_1_7
                    "*TTHHHWWAAAPPPP!!!!*"
                    lauren.c "AAAARRRGGGHHHHHHHH!!!!!!!!"
                    wt_image cheater_punishment_1_6
                    "For the peace of the neighborhood, you'll need to consider using a gag on her in the future.  For today, you want her to hear the sounds of her own agony."
                    wt_image cheater_punishment_1_7
                    "You continue to abuse her exposed feet until you decide she can take no more of the rubber bands ... *TTHHHWWAAAPPPP!!!!*"
                    lauren.c "AAAARRRGGGHHHHHHHH!!!!!!!!"
                    if dungeon.has_item(floggers):
                        wt_image cheater_punishment_1_11
                        "You switch to a leather strap from your collection of crops and floggers, and continue to abuse the soles of her feet until she reaches the limit of endurance to that sensation, too."
                        lauren.c "ow ... ow ... ow .... oooo owwww!!!"
                        change lauren submission by 10
                    else:
                        change lauren submission by 5
                    change lauren resistance by -10
                    wt_image cheater_punishment_1_8
                    "When you let her out of her bonds, she slumps to the floor at your feet, fighting to control and stop her tears."
                    player.c "You did very well.  That was hard, I know.  You accepted your punishment like a woman."
                    player.c "I may choose to hurt you again.  That's part of becoming the obedient slut your husband expects you to be.  You know now that you can take it, if you have to."
                    player.c "You know, too, that you don't want to be punished if you can avoid it.  If you listen to me, we can avoid punishments for punishment's sake."
                    player.c "I may still discipline you to teach you a lesson, or even just for my own amusement, but being disciplined and being punished are different things."
                    player.c "I hope the next time I bring you in here, it can be to discipline you, and not because I have to punish you for another transgression."
                    "Through her sniffles, she nods.  When she's pulled herself together, you let her get dressed and go home."
                    change player energy by -energy_long notify
                    $ lauren.action_punish.name = "Discipline her"
        else:
            $ lauren.remove_tags('trained_today', 'trained_this_week')
            lauren.c "No.  No, I'm not going to let you hurt me."
            "Try increasing her submission to you before trying again.  In the meantime, choose another option."
            $ lauren.temporary_count = 0
    elif lauren.punishment_count == 1:
        "Lauren starts to tremble nervously as she remembers her last session in your dungeon."
        wt_image cheater_punishment_1_1
        lauren.c "Why are we here?"
        player.c "It's not for punishment this time.  It's for discipline."
        wt_image cheater_punishment_1_14
        lauren.c "What do you mean by discipline?  Do you want to hurt me again?"
        player.c "Yes, but it'll be different this time. It's not because you did anything wrong. It's because this is something else you can give me to please me and your husband, if he chooses to use you for this purpose.  And it'll help you to better accept your role as obedient slut."
        if lauren.test('submission', 50):
            $ lauren.punishment_count = 2
            wt_image cheater_punishment_1_2
            "Lauren hangs her head and strips.  She may not agree with you, but her submission to you is high enough that she's not going to argue."
            wt_image cheater_punishment_2_5
            "You tie her on her back, her legs spread."
            player.c "Do you like being in this position. slut?  On your back with your legs open?  Let's check."
            player.c "Not wet yet.  But what happens when you get a good finger fucking?"
            wt_image cheater_punishment_2_1
            "You start to ram your fingers in and out of her."
            lauren.c "aahhhh!"
            "She cries out, first in pain, then in humiliation.  Despite the roughness of your approach, you're familiar enough with the female body to adjust your touch until her body starts to respond, despite herself."
            player.c "Ah, there we are.  That's the wetness I was expecting to feel in you."
            wt_image cheater_punishment_2_6
            player.c "Betrayed by your cunt again, weren't you, cunt?  That's always been a problem for you, hasn't it?"
            wt_image cheater_punishment_2_2
            player.c "This little cunt just likes to get fucked so much, she leads you to make bad decisions, stepping out on your husband, being a bad girl and a bad wife."
            player.c "This cunt needs discipline. You might think she doesn't, but I know better.  You've never had your cunt spanked, have you, cunt?"
            "Lauren shakes her head frantically."
            wt_image cheater_punishment_2_6
            player.c "It hurts."
            wt_image cheater_punishment_2_3
            "*SMACK*"
            lauren.c "OWWW!!!!"
            "You give her a long, hard, protracted spanking on her exposed pussy. She wails in pain, and even rolls her head into you, nuzzling against your chest seeking comfort as you discipline her naughty cunt."
            if dungeon.has_item(floggers):
                wt_image cheater_punishment_2_7
                "You finally stop spanking her and Lauren thinks her ordeal is over.  When she sees you pick up a flogger, she lets out a wail."
                lauren.c "nooooo!!!"
                "*THWACCKK*"
                lauren.c "OH!  oohhhh!!"
                wt_image cheater_punishment_2_4
                "*THWACCKK*"
                lauren.c "oooooo!!"
                "*THWACCKK*"
                lauren.c "ooooooooo!!"
                "The feel of the flogger striking her private parts is different than the feel of your hand striking her. It hurts, yes. But it also resonates inside her, a heavy rhythmic thumping vibrating her whole sex combined with sharp stings that set her entire labia and clit on fire."
                player.c "You're close to cumming, aren't you cunt? This dirty little cunt is so bad it even wants to cum when it's being punished."
                wt_image cheater_punishment_2_6
                "You stop the flogging,and Lauren wails again."
                player.c "No orgasm for you today, cunt. You need to learn discipline, and that includes controlling your orgasms.  If I keep flogging, you're going to cum despite yourself."
                change lauren submission by 10
            wt_image cheater_punishment_1_8
            "When you're finished with her, you untie her and let her recover.  She soon dresses and heads home, shaken by your demonstration of the responses you can trigger in her body."
            sys "You can now discipline Lauren on weekends, too."
            change lauren resistance by -10
            change player energy by -energy_long notify
        else:
            wt_image cheater_punishment_1_1
            lauren.c "No.  I put up with your punishment last time because maybe I did deserve it, for cheating on my husband.  But I've been faithful since then and I'm trying hard to follow your training, at least the parts that aren't completely insane.  But I'm not going to let you 'discipline' me anytime you feel the urge to see me in pain. My husband isn't a sadist, you are. This isn't needed for me to be the woman he wants me to be."
            $ title = "What do you do?"
            menu:
                "Drop it":
                    $ lauren.remove_tags('trained_today', 'trained_this_week')
                    "Lauren seems very set and she's right, this isn't necessary to complete her training.  You decide to drop it and try something different for today."
                    call forced_movement(living_room) from _call_forced_movement_149
                    wt_image cheater_initial_9
                    "Lauren seems satisfied to have a won a little victory."
                    change lauren resistance by 5 notify
                    $ lauren.temporary_count = 0
                "Spank her":
                    wt_image cheater_spank_3
                    "You grab Lauren and before she can react bend her over, flipping up her dress and pulling down her panties."
                    wt_image cheater_spank_6
                    player.c "I'll decide what's needed, not you.  You agreed to accept my training and this is a part of it."
                    wt_image cheater_spank_1
                    "*smack*  *smack*  *smack*"
                    wt_image cheater_spank_7
                    "Lauren tries not to cry out, but as you continue to spank her, it gets harder and harder for her to control herself."
                    wt_image cheater_spank_1
                    "*SMACK*  *SMACK*  *SMACK*"
                    wt_image cheater_spank_2
                    "Eventually, the cries come out involuntarily."
                    lauren.c "ow!  Ow!!  OW!!"
                    wt_image cheater_spank_7
                    "When you think she's taken as much as she can, you let her gather herself up and go home, suitably chastened.  If you continue to increase her submission to you, she'll eventually accept your right to discipline her fully."
                    change lauren submission by 5
                    change player energy by -energy_short notify
    elif lauren.punishment_count == 2:
        wt_image cheater_punishment_1_1
        player.c "Remove your clothes."
        wt_image cheater_punishment_1_2
        "She does as you say, then waits to find out what you have in mind for her today."
        $ title = "What do you have in mind for her today?"
        menu menu_lauren_punish_1:
            "Physical Discipline":
                if dungeon.has_item(gags) and dungeon.has_item(floggers):
                    wt_image cheater_punishment_3_1
                    "You don't trust Lauren's legs to support her when you're finished with her discipline.  So you tie her down on a bare spring mattress, and silence her with a ball gag."
                    wt_image cheater_punishment_3_12
                    "She strains her head to see what you're doing as you select the first instrument you want to use on her from amongst your collection of floggers."
                    wt_image cheater_punishment_3_2
                    "Her eyes follow you in fear as you circle her, your chosen flogger in hand."
                    wt_image cheater_punishment_3_3
                    "Without warning, you stop circling her and start beating her ... *THWACCKK*  *THWACCKK*  *THWACCKK*"
                    lauren.c "NNNNNNNNNNNNNNNNN"
                    wt_image cheater_punishment_3_9
                    "The ball gag does it's job.  You strike her, again and again, each blow harder than the last ... *THWACCKK*  *THWACCKK*  *THWACCKK*"
                    wt_image cheater_punishment_3_13
                    "No matter how loud she screams, only a muffled whine comes out of her mouth."
                    lauren.c "NNNNNNNNNNNNNNNNN"
                    wt_image cheater_punishment_3_4
                    "You pay particular attention to her open and exposed pussy. You alternate pounding the weight of the flogger down on it and letting the tips snap against her most sensitive parts."
                    lauren.c "NNNNNNNNNNNNNNNNN"
                    wt_image cheater_punishment_3_5
                    "Eventually she screams herself hoarse and is reduced to pleading with you silently with her eyes as the flogger strikes her ... *THWACCKK*  *THWACCKK*  *THWACCKK*"
                    wt_image cheater_punishment_3_14
                    "You put down the flogger and place your hand between her legs."
                    wt_image cheater_punishment_3_7
                    "It only takes a few strokes of your fingers along her clit and her sore, sensitized pussy is flowing wet."
                    $ title = "What do you do next?"
                    menu menu_lauren_punish_physical_discipline_1:
                        "Crop her" if not lauren.has_tag('cropped_her'):
                            add tags 'cropped_her' to lauren
                            wt_image cheater_punishment_3_10
                            "When you take your hand away, she curls her toes and groans in frustration.  If she didn't have the gag in, you're sure she'd be begging you not to stop."
                            wt_image cheater_punishment_3_2
                            "Unfortunately for her, what's not going to stop is her beating.  You select a crop from your collection as she watches in dismay."
                            wt_image cheater_punishment_3_11
                            "You sit down beside her and begin striking her as she flinches and tries futilely to escape ... *THWAPPP*  *THWAPPP*  *THWAPPP*"
                            "In this position, you could keep the beating up all night.  You don't actually spend the whole night at it, but to Lauren it feels like you do."
                            wt_image cheater_punishment_3_14
                            "When you put your hand back between her legs, you find she's still turned on, despite her discomfort ..."
                            wt_image cheater_punishment_3_7
                            "... and with a few quick strokes of your fingers, she's soon writhing for a different reason."
                            jump menu_lauren_punish_physical_discipline_1
                        "Strap her feet" if lauren.has_tag('cropped_her') and not lauren.has_tag('strapped_her'):
                            add tags 'strapped_her' to lauren
                            wt_image cheater_punishment_3_10
                            "Lauren groans again when you take your hand away, curling her toes in frustration."
                            wt_image cheater_punishment_3_16
                            "You've worked her over pretty good this session, but so far you've left her feet alone."
                            wt_image cheater_punishment_3_17
                            "Your fingers on her sensitive soles soon has her curling her toes again."
                            wt_image cheater_punishment_3_2
                            "She doesn't start to panic, though, until you pick up the elastics and the strap."
                            wt_image cheater_punishment_1_11
                            "She has unusually sensitive feet, as you discovered in her first dungeon session ... *slappp*  *slappp*  *slappp*"
                            wt_image cheater_punishment_3_13
                            "However difficult she found the flogging and the cropping, it was nothing compared to ordeal of having her feet strapped."
                            wt_image cheater_punishment_3_14
                            "When you put your hand back between her legs this time, she's completely off balance ..."
                            wt_image cheater_punishment_3_7
                            "... and quickly brought to a state of high arousal."
                            jump menu_lauren_punish_physical_discipline_1
                        "Let her cum":
                            wt_image cheater_punishment_3_6
                            "You decide to take mercy on her.  She starts wiggling her hips as soon as you begin fingering her."
                            wt_image cheater_punishment_3_8
                            "As the first orgasm rips through her, she arches her back and strains against the limits of her bonds. She tries to scream, but only the faintest whine escapes through the ball gag."
                            lauren.c "nnnn ... nnnn ... nnnnnnnnnnnn"
                            wt_image cheater_punishment_3_15
                            "The second orgasm follows shortly, and is no less intense.  It leaves her twitching uncontrollably on the metal springs."
                            lauren.c "nnnn ... nnnn ... nnnnnnnnnnnn"
                            wt_image cheater_punishment_3_5
                            "You leave her like that to recover."
                            wt_image cheater_punishment_1_8
                            "When she's able to stand, you untie her and take the gag out.  It takes her a few minutes to dress and go home, shaken by the control you have to trigger responses in her body."
                            if lauren.has_tag('came_after_flogging'):
                                change lauren resistance by -5
                            else:
                                add tags 'came_after_flogging' to lauren
                                change lauren resistance by -10
                            change lauren desire by 5
                        "Deny her the orgasm":
                            wt_image cheater_punishment_3_18
                            "After a few more caresses of her clit, she's breathing hard and straining to create more pressure on the tender nub."
                            wt_image cheater_punishment_3_10
                            "When you pull your hand away, Lauren groans and curls her toes in frustration."
                            wt_image cheater_punishment_3_5
                            "She's physically and emotionally drained.  You let her rest in her bonds for a while ..."
                            wt_image cheater_punishment_1_8
                            "... then you untie her and take the gag out.  It takes her a few minutes to dress and go home, shaken by the control you have to trigger responses in her body."
                            if lauren.has_tag('denied_orgasm_after_flogging'):
                                change lauren resistance by -5
                            else:
                                add tags 'denied_orgasm_after_flogging' to lauren
                                change lauren resistance by -10
                            change lauren submission by 5
                    change player energy by -energy_long notify
                    rem tags 'cropped_her' 'strapped_her' from lauren
                else:
                    if dungeon.has_item(gags):
                        "If you picked up some floggers, you could subject Lauren to a more effective physical discipline.  As it is, you'll make do with your hands."
                    elif dungeon.has_item(floggers):
                        "Lauren is a bit of a screamer.  If you picked up some effective gags, you'd be able to discipline her more effectively without disturbing the peace of the neighborhood.  As it is, you'll need to take it somewhat easy on her."
                    else:
                        "If you picked up some floggers and an effective gag, you could subject Lauren to a more effective physical discipline.  As it is, you'll have to take it easy on her using your hands."
                    wt_image cheater_punishment_2_2
                    "You tie Lauren on her back, legs spread apart."
                    player.c "It's been too long since we disciplined this greedy cunt.  We don't want it to forget what happens to naughty cunts who aren't obedient."
                    wt_image cheater_punishment_2_3
                    "You use your hand to spank Lauren's pussy ...  *smack*  *smack*  *smack*"
                    lauren.c "Ow!  OW!!   Ow!!!"
                    "The longer the spanking goes, the harder you slap her, and the more she cries ... *SMACK*  *SMACK*  *SMACK*"
                    lauren.c "OW!!  Ow!!!  OWWW!!!!"
                    if dungeon.has_item(floggers):
                        wt_image cheater_punishment_2_7
                        "When she's taken as much of the spanking as you think she can handle, you switch to the flogger ...  *THWACCKK*  *THWACCKK*  *THWACCKK*"
                        lauren.c "oohhhh!!"
                        wt_image cheater_punishment_2_4
                        "You can't beat her as hard as you'd like.  Without a proper gag, her screams would bother the neighbors.  But you beat her enough that her pussy feels like its on fire."
                        lauren.c "ooooooo!!"
                        wt_image cheater_punishment_2_7
                        "Despite the pain, the feeling of the flogger pounding away at her triggers a response in her sex that both excites and dismays her."
                    wt_image cheater_punishment_2_6
                    player.c "The cunt's all hot and bothered now, isn't it?  If it does as it's told, maybe someday it'll get relief."
                    change lauren resistance by -5
                    change player energy by -energy_long notify
            "Suspension Ordeal" if dungeon.has_item(suspension_gear):
                wt_image cheater_suspension_10
                "You carefully wind the ropes around Lauren, forming a secure harness to support her weight, then connect it to the pulley.  As you winch her up off the ground, she gasps in surprise."
                wt_image cheater_suspension_1
                "You leave her there, floating in the air, as you go back to your other business."
                wt_image cheater_suspension_10
                "When you return, you check her extremities to make sure her blood flow and nerves haven't been disrupted by the pressure of the ropes holding her up."
                wt_image cheater_suspension_2
                "Remembering how sensitive her feet are, you can't help but jab her soles more sharply than is strictly necessary."
                lauren.c "OW!!"
                wt_image cheater_suspension_11
                "The pretty little cries she makes as you jab her sensitive feet convince you to take out her old favorites, the elastic bands."
                wt_image cheater_suspension_3
                "The ones you choose won't hurt as much as the ones you used when punishing her ..."
                wt_image cheater_suspension_4
                "... but from her cries, it's not apparent that she appreciates the difference."
                lauren.c "OOWWWW!!!"
                wt_image cheater_suspension_12
                "To take her mind off the pain in her feet, you give her a demonstration of how easily she gets wet after being disciplined now."
                wt_image cheater_suspension_5
                "In only a moment, your fingers slide smoothly in and out of her well lubricated pussy as she moans."
                lauren.c "oooooo"
                $ title = "What do you do now?"
                menu:
                    "Let her cum":
                        wt_image cheater_suspension_12
                        "It takes very little for Lauren to cum when she's in this state, something you're happy to point out to her."
                        player.c "That's a good slut. Cum for me after your discipline. Show me what an obedient little slut you are, taking my pain, my pleasure, whatever I choose to give you."
                        lauren.c "ooooooooo!!"
                        wt_image cheater_suspension_6
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_punishment_1_2
                        if lauren.has_tag('suspension_cum'):
                            change lauren desire by 5
                            change lauren resistance by -5
                            "You let her down from her suspension after her orgasm subsides.  She goes home shaken by the reminder of the response you can trigger in her body, and feeling a bit turned on."
                        else:
                            add tags 'suspension_cum' to lauren
                            change lauren desire by 10
                            change lauren resistance by -10
                            "You let her down from her suspension after her orgasm subsides. She goes home shaken by the responses you can trigger in her body, and more than a bit turned on by you."
                        change player energy by -energy_short notify
                    "Leave her hanging":
                        wt_image cheater_suspension_12
                        "You get Lauren completely worked up ..."
                        wt_image cheater_suspension_10
                        lauren.c "ooooooooo!!"
                        "...  then pull your fingers out of her.  She moans in disappointment at the sudden emptiness between her legs."
                        lauren.c "Ooohhh!!"
                        wt_image cheater_suspension_1
                        player.c "No orgasm today, slut.  Just hang here and remember that your husband or I decide when and whether you cum."
                        "You leave her there for a while as you go about your business."
                        wt_image cheater_punishment_1_8
                        if lauren.has_tag('suspension_left_hanging'):
                            change lauren submission by 5
                            change lauren resistance by -5
                        else:
                            add tags 'suspension_left_hanging' to lauren
                            change lauren submission by 10
                            change lauren resistance by -10
                        "Then you lower her down and let her dress and go home, shaken by the responses you can trigger in her body."
                        change player energy by -energy_short notify
                    "Have her blow you" if lauren.blowjob_count > 2:
                        wt_image cheater_suspension_10
                        "You pull your fingers out of her.  She moans in disappointment at the sudden emptiness between her legs."
                        lauren.c "Ooohhh!!"
                        wt_image cheater_suspension_13
                        player.c "No orgasm today, slut.  Remember your husband or I decide when and whether you cum.  We also decide when and where we cum.  Today, it's going to be in your mouth."
                        wt_image cheater_suspension_14
                        "She opens her mouth obediently as you pull her head onto your cock."
                        wt_image cheater_suspension_15
                        if lauren.blowjob_count == 3:
                            call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_4
                        "She doesn't have a lot of freedom to show off her skills, dangling from the ceiling as she is ..."
                        wt_image cheater_suspension_7
                        "... but she does her best to please you."
                        wt_image cheater_suspension_14
                        "Eventually, she succeeds."
                        wt_image cheater_suspension_16
                        player.c "[player.orgasm_text]"
                        wt_image cheater_punishment_1_2
                        "You let her down from her suspension after she swallows your load. She goes home shaken by the responses you can trigger in her body."
                        $ lauren.blowjob_count += 1
                        call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_1
                        call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_7
                        change lauren submission by 5
                        change lauren resistance by -5
                        change player energy by -energy_very_short
                        orgasm notify
                    "Fuck her" if lauren.sex_count > 2:
                        wt_image cheater_suspension_10
                        "You pull your fingers out of her.  She moans in disappointment at the sudden emptiness between her legs."
                        lauren.c "Ooohhh!!"
                        wt_image cheater_suspension_8
                        "Her disappointment doesn't last long.  You swing her around and replace your fingers with your hard cock."
                        lauren.c "OH!!!"
                        wt_image cheater_suspension_17
                        "There's no opportunity for Lauren to show off her new sex skills in this position.  All she can do is hang there while you fuck her as fast or as slow as you like."
                        wt_image cheater_suspension_18
                        "It's more fun, though, when she moans as you fuck her ... which she does every time you stroke her clit."
                        lauren.c "oooooo"
                        if lauren.test('desire', 60):
                            wt_image cheater_suspension_19
                            "The feeling of your cock inside her and your fingers against her clit soon triggers a response."
                            lauren.c "oooooo!!"
                            wt_image cheater_suspension_9
                            "Quick and intense, the orgasm ripples through her.  She lets out a scream as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_suspension_17
                            player.c "Quit thrashing about. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with my pleasure, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_9
                        wt_image cheater_suspension_8
                        "After a few hard thrusts, pulling her suspended body back and forth along your cock, you're ready to cum."
                        wt_image cheater_suspension_20
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_punishment_1_2
                        "She seems comfortable heading home, carrying your load inside her."
                        call lauren_sex_stat_changes from _call_lauren_sex_stat_changes
                        change lauren desire by 5
                        change lauren resistance by -5
                        change player energy by -energy_very_short
                        orgasm notify
            "Bondage Sex":
                if lauren.blowjob_count == 0:
                    if lauren.test('desire', 10) or lauren.test('resistance', 50):
                        wt_image cheater_bondage_sex_11
                        "You tie Lauren into a kneeling position and take out your cock."
                        player.c "Time to work on your skills, slut.  Let's start with you showing me what you know how to do with your mouth."
                        "Either you've worn down her resistance to your instructions, or some part of her wants to feel your body inside her."
                        wt_image cheater_bondage_sex_12
                        "The end result is the same.  She opens her mouth and accepts your cock inside.  You'll need to train her to pleasure your balls, too.  That'll come later.  She needs more basic lessons first."
                        wt_image cheater_bondage_sex_13
                        player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                        wt_image cheater_bondage_sex_14
                        player.c "Slow down.  I'll tell you when it's time to speed up."
                        wt_image cheater_bondage_sex_15
                        player.c "Swallow me, right down to the base."
                        wt_image cheater_bondage_sex_17
                        player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
                        wt_image cheater_bondage_sex_16
                        "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
                        wt_image cheater_bondage_sex_15
                        "Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
                        wt_image cheater_bondage_sex_13
                        player.c "Pay attention. We're going to keep doing this until you get it right. Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now."
                        wt_image cheater_bondage_sex_18
                        player.c "Start again, at the beginning."
                        wt_image cheater_bondage_sex_19
                        "You let her pleasure you with her mouth, correcting her from time to time when she's not doing it quite right."
                        wt_image cheater_bondage_sex_20
                        "When she's learned as much as she can from one session, you empty your load in her."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_bondage_sex_21
                        player.c "Swallow it all."
                        wt_image cheater_bondage_sex_13
                        lauren.c "I did."
                        player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught.  You can go home now, and show your husband what you've learned."
                        $ lauren.blowjob_count += 1
                        call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_8
                        orgasm
                        change player energy by -energy_long notify
                    else:
                        wt_image cheater_punishment_1_1
                        lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
                        "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off."
                        jump menu_lauren_punish_1
                else:
                    $ title = "What do you want to do with her?"
                    menu menu_lauren_punish_bondage_sex_1:
                        "Test her oral skills":
                            call lauren_punish_bondage_sex_oral from _call_lauren_punish_bondage_sex_oral_1
                        "Fuck her" if lauren.sex_count == 0:
                            call lauren_punish_bondage_sex_fuck from _call_lauren_punish_bondage_sex_fuck_2
                        "Test her fucking skills" if lauren.sex_count >= 1:
                            call lauren_punish_bondage_sex_fuck from _call_lauren_punish_bondage_sex_fuck_3
                        "Use her ass" if 'accepts_anal' not in lauren.tags and 'no_anal' not in lauren.tags and lauren.sex_count >= 1:
                            call lauren_punish_bondage_sex_anal from _call_lauren_punish_bondage_sex_anal_2
                        "Use the asswhore" if 'accepts_anal' in lauren.tags:
                            call lauren_punish_bondage_sex_anal from _call_lauren_punish_bondage_sex_anal_3
                        "Never mind":
                          jump menu_lauren_punish_1
    else:
        sys "There was a problem with 'label lauren_punish' and the lauren.punishment_count variable."
        $ lauren.temporary_count = 0
    if lauren.temporary_count == 1:
        $ lauren.temporary_count = 0
        end_day
    return

# Have Her Workout
label lauren_workout:
    $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if lauren.workout_count == 0:
        call lauren_first_workout from _call_lauren_first_workout
    elif lauren.workout_count == 1:
        call lauren_second_workout from _call_lauren_second_workout
    elif lauren.workout_count == 2:
        call lauren_third_workout from _call_lauren_third_workout
    elif lauren.workout_count == 3:
        call lauren_photoshoot from _call_lauren_photoshoot
    notify
    end_day
    return

label lauren_first_workout:
    $ lauren.workout_count = 1
    player.c "Come with me."
    wt_image cheater_portrait_initially
    lauren.c "Where are we going?"
    player.c "To get you in better shape."
    wt_image cheater_initial_2
    lauren.c "What?"
    player.c "You heard me.  Your husband wants an obedient little slut, and an obedient little slut keeps herself in good shape."
    wt_image cheater_initial_6
    lauren.c "I am in good shape!"
    player.c "Not good enough.  You're going to be spending a lot of time fucking, and I don't want you running out of energy when you should be enthusiastically fucking cock."
    wt_image cheater_initial_1
    player.c "I also want you toned.  You're starting to get on in years, and you don't want your husband to get tired of you and start thinking about trading you in for a younger model."
    "Lauren's face turns red, but she says nothing."
    call forced_movement(gym) from _call_forced_movement_150
    wt_image cheater_workout_1
    "You bring Lauren to a private gym, where she changes into workout clothes."
    wt_image cheater_workout_2
    "Then you run her through a series of exercises to improve on her endurance and muscle tone."
    wt_image cheater_workout_14
    player.c "Okay, Lauren.  Let's see if you've been giving this your all.  Take off your top."
    if lauren.display_count_clothed > 0:
        wt_image cheater_workout_3
        "She has been.  Her skin is drenched with sweat."
        wt_image cheater_workout_22
        player.c "Looks to me like this workout was long overdue.  You're soaked, and that was only a light workout."
        wt_image cheater_workout_15
        player.c "What about your cunt, slut?  Is it soaking wet too?  Does exercising turn you on?  Show me and let's see."
        if lauren.open_her_count > 0:
            wt_image cheater_workout_23
            "It isn't, but the act of demonstrating this to you is humiliating."
            wt_image cheater_workout_24
            player.c "Are you sure you aren't enjoying this?  I see some dampness down there.  Let's have a closer look."
            wt_image cheater_workout_4
            "Once you've confirmed that her pussy lips are coated only with sweat, and no other liquids, you let her cover up and go home."
        else:
            wt_image cheater_workout_1
            lauren.c "No way!"
            "You'll need to get her used to opening herself up to you first."
    else:
        wt_image cheater_workout_1
        lauren.c "No way!"
        "You'll need to get her used to displaying her body to you first."
    change lauren resistance by -5
    change lauren submission by 5
    change player energy by -energy_long
    call forced_movement(living_room) from _call_forced_movement_151
    return

label lauren_second_workout:
    wt_image cheater_initial_1
    player.c "Come with me, Lauren, we're going back to the gym."
    call forced_movement(gym) from _call_forced_movement_152
    wt_image cheater_workout_1
    "As before, Lauren changes into the workout clothes you provide to her."
    wt_image cheater_workout_5
    "Then you turn her over to Paul, who owns the gym."
    wt_image cheater_workout_17
    "With Paul instructing Lauren, you can relax and enjoy the work out."
    wt_image cheater_workout_6
    "Some exercises are more fun to watch than others."
    wt_image cheater_workout_7
    "And some seem intended as much for your benefit as Lauren's."
    wt_image cheater_workout_18
    "By the time Paul is finished with her, she's exhausted."
    player.c "Time to show Paul that you gave it your all for him, Lauren."
    wt_image cheater_workout_25
    lauren.c "But, he knows I did.  He's been right here beside me the whole time."
    player.c "Seeing is believing, Lauren."
    wt_image cheater_workout_26
    lauren.c "You can't honestly expect me to ... I don't even know him."
    player.c "Show him, Lauren."
    if lauren.display_count_clothed > 0:
        wt_image cheater_workout_3
        lauren.c "Fine.  Paul, I gave it my all for you today.  See?"
        wt_image cheater_workout_27
        "She makes no move to remove her bottoms, and given the glare on her face, you decide not to push it.  After Paul has had a good look, you let Lauren dress and go home."
        change lauren submission by 5
        $ lauren.workout_count = 2
    else:
        wt_image cheater_workout_1
        lauren.c "No way!"
        "You'll need to get her used to displaying her body to you first, before she'll display it to someone else."
    change lauren resistance by -5
    change player energy by -energy_short
    call forced_movement(living_room) from _call_forced_movement_153
    return

label lauren_third_workout:
    call forced_movement(gym) from _call_forced_movement_154
    wt_image cheater_workout_5
    "You bring Lauren back to Paul's gym and hand her over to Paul for another work out session."
    wt_image cheater_workout_17
    "As before, you relax and watch the work out while Lauren and Paul do all the work."
    wt_image cheater_workout_7
    "You're tempted to suggest to Paul that he take a more hands on approach with Lauren, but he's a professional, so you let him finish taking Lauren through her exercises before you intervene."
    wt_image cheater_workout_18
    player.c "Lauren, it's time you reimbursed Paul for his time and the use of his gym."
    wt_image cheater_workout_16
    "She starts to pull down her top."
    player.c "Not that.  Paul's time is far more valuable than you can pay for with a simple flash."
    wt_image cheater_workout_25
    lauren.c "I have money with me, in my purse."
    player.c "That's not how sluts pay for things, Lauren.  Paul's apartment is upstairs, over the gym.  We can go there so you can pay him in full."
    if lauren.test('resistance', 35):
        $ lauren.workout_count = 3
        wt_image cheater_workout_26
        lauren.c "Fine.  Let's get this over with."
        "You've worn down Lauren's resistance to the point where she's willing to pay a stranger with her body.  Her husband may not want to share her like this, but he'll be happy to have a slut to command around who's willing to let him lend her out if he wants to do so."
        wt_image cheater_workout_28
        "You and Paul escort Lauren upstairs, where Paul demonstrates that he's a good guy at heart."
        lauren_gym_instructor "Are you sure you want to do this?  I like where this is going, but not if you're feeling pressured."
        wt_image cheater_workout_29
        lauren.c "This isn't easy for me.  Can you make sure I don't regret it?"
        wt_image cheater_workout_30
        lauren_gym_instructor "I'll do my best."
        wt_image cheater_workout_31
        "Paul kisses her as the two of them help each other out of their clothes."
        wt_image cheater_workout_20
        "Then he pulls her on top of him ..."
        wt_image cheater_workout_21
        "... makes sure she's suitably warmed up ..."
        wt_image cheater_workout_9
        "... and sets her to work riding his cock."
        wt_image cheater_workout_10
        "Even Paul's fuck sessions are designed like a work out.  He soon has her stretching and using new muscles as she works hard to coax an orgasm out of him."
        wt_image cheater_workout_11
        "By the time he takes pity on the exhausted woman and takes over the physical work, she's as fully and thoroughly stimulated, physically, as she's ever been from sex ..."
        wt_image cheater_workout_32
        "... even if mentally she's not yet ready to let herself cum from the experience of fucking a stranger as payment-for-service."
        wt_image cheater_workout_12
        "When Paul deposits his load on her well-fucked pussy, Lauren looks up at him with a mixture of admiration and satisfaction.  If being an obedient slut means she gets to fuck men like Paul from time to time, perhaps it won't be too bad?"
        $ title = "Have her suck you off?"
        menu:
            "Yes":
                wt_image cheater_workout_35
                player.c "Don't be in such a rush to clean up and get dressed, slut.  While Paul recovers, let's entertain him by working on your other skills.  Show him what you can do with your mouth."
                wt_image cheater_workout_36
                "Lauren hesitates only a moment before kneeling down in front of you.  She just fucked another man in front of you.  She finds herself unable to deny giving you pleasure, too.  Keeping her eyes on you, she opens her mouth to take your hard cock."
                $ lauren.blowjob_count += 1
                if lauren.blowjob_count == 1:
                    wt_image cheater_workout_37
                    "Paul may have given Lauren a work out of one type.  Now it's time for you to give her a different type of exercise."
                    player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                    wt_image cheater_workout_38
                    player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now."
                    wt_image cheater_workout_39
                    player.c "Swallow me, right down to the base, then slide back up to the tip.  Tongue against my head, flick it back and forth."
                    wt_image cheater_workout_40
                    player.c "Start another stroke.  Deeper this time, and hold it at the end, then repeat."
                    wt_image cheater_workout_41
                    "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked.  Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, aren't the least bit concerned about offending Lauren."
                    player.c "Pay attention.  We're going to keep doing this until you get it right.  Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now.  Start again, at the beginning."
                    wt_image cheater_workout_39
                    "You make her work for it, but eventually she earns a mouthful of your cum before you send her home."
                    wt_image cheater_workout_42
                    player.c "[player.orgasm_text]"
                    $ lauren.swallow_count += 1
                    change lauren submission by 5
                elif lauren.blowjob_count == 2:
                    wt_image cheater_workout_39
                    player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
                    wt_image cheater_photoshoot_40
                    player.c "First though, we're gong to add some new wrinkles ... excuse the pun."
                    wt_image cheater_ball_lick_1
                    player.c "Get your tongue down there on my balls, Lauren.  Give them a good washing, then get your mouth around them.  Gently.  Let them warm up in your mouth.  I'll tell you when I'm ready for you to start sucking my cock again.  Until then, use your hand to gently stroke me until your mouth takes its place."
                    wt_image cheater_photoshoot_43
                    "Once you're satisfied with the way she's pleasuring your balls, you let her go back to your cock ..."
                    wt_image cheater_workout_37
                    "... where she works hard to earn a mouthful of your cum to swallow before you send her home."
                    wt_image cheater_workout_42
                    player.c "[player.orgasm_text]"
                    $ lauren.swallow_count += 1
                    change lauren resistance by -5
                elif lauren.blowjob_count == 3:
                    wt_image cheater_workout_38
                    "Lauren gets straight to work, pleasuring your cock ..."
                    wt_image cheater_ball_lick_1
                    "... and your balls."
                    wt_image cheater_workout_43
                    player.c "You're starting to get the hang of this, slut.  Good technique with my balls, getting them nice and warm.  Nice responsiveness to my hand in your hair, slowing down and speeding up as soon as I shift my grip.  No need for me to pull your head around like a pumpkin anymore before you figure out what I want."
                    wt_image cheater_workout_39
                    player.c "You're on your way to becoming a fine little cocksucker, slut.  Does that feel good, knowing that you're finally able to please a man properly with your mouth?"
                    wt_image cheater_workout_37
                    "Meekly, she nods her head as you give her a mouthful of your cum to swallow before she heads home."
                    wt_image cheater_workout_42
                    player.c "[player.orgasm_text]"
                    $ lauren.swallow_count += 1
                    change lauren sos by 5
                else:
                    wt_image cheater_workout_38
                    "Lauren knows what she's doing now.  She gets your cock standing at attention ..."
                    wt_image cheater_ball_lick_1
                    "... then concentrates her efforts on your balls until your shaft is throbbing in her hand."
                    wt_image cheater_workout_41
                    "There's no need to correct her technique.  That doesn't mean, however, that you can't have a little fun with her situation."
                    wt_image cheater_workout_43
                    player.c "Does this feel good, little slut, sucking my cock while Paul watches?  Which did you like better, fucking Paul while I watched or showing off your cock-sucking skills while Paul watches?"
                    wt_image cheater_workout_39
                    player.c "Don't bother answering that.  A good slut is happy to be fucked at any time, regardless of who is watching her.  And you are a good slut now, aren't you?"
                    wt_image cheater_workout_37
                    "Perhaps it was just part of the blow job she's giving you, but Lauren definitely nods her head in response to your question.  For her honesty, you reward her with a mouthful of your cum to swallow before she heads home."
                    wt_image cheater_workout_42
                    player.c "[player.orgasm_text]"
                    $ lauren.swallow_count += 1
                orgasm
            "No, send her home":
                wt_image cheater_workout_33
                player.c "Rather than wiping that off, slut, why don't you wear it home, as proof to your husband that you're ready to spread your legs for payment, if he ever wants that from you."
                wt_image cheater_workout_34
                "She's not willing to go that far today, but maybe next time you can send her home with evidence to her husband - and herself - of her new attitude."
        change lauren sos by 10
    else:
        wt_image cheater_workout_26
        lauren.c "No way, I don't care what you or my husband expect, I'm not a whore."
        wt_image cheater_workout_1
        "She grabs some money from her purse and throws it on the floor, then stomps away."
        "You'll need to lower her resistance before she'll agree to pay for the work out with her body.  For tonight, she's in no mood to continue her session, so you send her home."
    change player energy by -energy_short
    call forced_movement(living_room) from _call_forced_movement_155
    return

label lauren_photoshoot:
    $ lauren.workout_count = 4
    wt_image cheater_initial_3
    player.c "Those work outs have been paying off, Lauren.  You're definitely better toned now than when you first came to me.  In fact, your body is downright hot now."
    wt_image cheater_initial_9
    "Despite herself, Lauren blushes slightly at the compliment."
    wt_image cheater_initial_4
    player.c "I think we should capture this look. Some photos for your husband will make a nice gift, and set the standard for what you should look like, in case you try to slack off after your training is finished."
    call forced_movement(outdoors) from _call_forced_movement_156
    wt_image cheater_photoshoot_12
    "You bring Lauren to Ian, a professional photographer.  He dresses her in a classy, but revealing tight blue dress ..."
    wt_image cheater_photoshoot_1
    "... and takes some standard glamour shots of her."
    wt_image cheater_photoshoot_15
    "Aware of the purpose of these photos, Ian coaxes her to lift her dress ..."
    wt_image cheater_photoshoot_13
    "... and moves on to more revealing shots"
    wt_image cheater_photoshoot_2
    "Lauren cooperates fully ..."
    wt_image cheater_photoshoot_3
    "... as Ian makes this intimate."
    wt_image cheater_photoshoot_4
    "She lets him remove her panties ..."
    wt_image cheater_photoshoot_14
    "... then after a few bottom-less snaps ..."
    wt_image cheater_photoshoot_17
    "... she strips completely while he shoots her."
    wt_image cheater_photoshoot_18
    "Lauren assumes this is as far as the photoshoot goes ..."
    wt_image cheater_photoshoot_31
    "... but Ian has other ideas."
    wt_image cheater_photoshoot_31
    "He hasn't finished exploring his model ..."
    wt_image cheater_photoshoot_19
    "... or his artistic vision."
    wt_image cheater_photoshoot_5
    "By the time he's finished ..."
    wt_image cheater_photoshoot_20
    "... she has a portfolio of photos that are sure to impress her husband."
    wt_image cheater_photoshoot_33
    player.c "Lauren, Ian's done an incredible job capturing the essence of who and what you are.  Be a good slut and let him play with you to show how thankful you are for the nice gift he made for your husband."
    wt_image cheater_photoshoot_34
    "Maybe it's because of the interest he showed in her body ..."
    wt_image cheater_photoshoot_21
    "... maybe it's because being photographed turned her on ..."
    wt_image cheater_photoshoot_22
    "... or maybe she's just embracing the role of obedient slut ..."
    wt_image cheater_photoshoot_35
    "... but whatever her reason, she throws herself fully into her 'thank you' ..."
    wt_image cheater_photoshoot_23
    "... taking Ian's cock out of his pants and stroking it hard as he feels her up."
    wt_image cheater_photoshoot_24
    "Hand jobs are a valuable skill for obedient sluts, but it's best for her training not to let Lauren get away with too easy a payment."
    wt_image cheater_photoshoot_25
    player.c "Ian's earned more than a hand job, Lauren.  Offer him something else."
    wt_image cheater_photoshoot_7
    lauren.c "Would you like me to blow you?"
    wt_image cheater_photoshoot_8
    "Of course he would, but it would be better for Lauren's training if she went ever further."
    wt_image cheater_photoshoot_26
    player.c "Make sure he knows he doesn't have to settle for a blow job, either."
    wt_image cheater_photoshoot_27
    lauren.c "I could also fuck you, if you want?"
    wt_image cheater_photoshoot_28
    "It turns out Ian wants that very much."
    wt_image cheater_photoshoot_29
    "He even has her hold her pussy lips open for him as she rides him, mimicking her pose from the photoshoot."
    wt_image cheater_photoshoot_30
    "Lauren's husband may not want her fucking other men behind his back, but knowing that she's willing to fuck other men on his instructions may be useful to him.  You pick up one of Ian's cameras and start taking some shots."
    wt_image cheater_photoshoot_9
    "Your photos won't be as nice as Ian's, but you figure Lauren's husband may like the photographic evidence of her change in attitude.  Plus they make a nice addition to the photo set, showing how they were paid for."
    wt_image cheater_photoshoot_29
    "The photos get better, still, when you realize that Lauren is starting to enjoy this as much as Ian is.  The combination of his cock inside her, her own fingers on her sex, and the knowledge that you're taking pictures of her fucking a stranger soon brings her over the edge."
    wt_image cheater_photoshoot_9
    "Her eyes close and a deep groan escapes her throat as her body shudders to a climax around Ian's hard cock, bringing Ian to orgasm with her."
    wt_image cheater_photoshoot_10
    lauren.c "Aaahhhh!!"
    wt_image cheater_photoshoot_36
    "Now she's not only fucking strangers for services, she's cumming while doing so.  The idea of being her husband's obedient slut is becoming more palatable to her."
    $ title = "Have her suck you off?"
    menu:
        "Yes":
            wt_image cheater_photoshoot_33
            player.c "Since you made such a quick job of paying for your photoshoot, we still have a little time left to work on your skills, slut.   Your cunt just got some practice at pleasing a man, let's get your mouth some more practice, too."
            wt_image cheater_photoshoot_37
            "Lauren hesitates only a moment before kneeling down in front of you.  She just fucked another man in front of you.  She finds herself unable to deny giving you pleasure, too.  Keeping her eyes on you, she opens her mouth to take your hard cock."
            $ lauren.blowjob_count += 1
            if lauren.blowjob_count == 1:
                wt_image cheater_photoshoot_11
                player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
                wt_image cheater_photoshoot_38
                player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now.  Swallow me, right down to the base."
                wt_image cheater_photoshoot_39
                player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end."
                wt_image cheater_photoshoot_40
                "Ian may have given Lauren a work out of one type.  Now it's time for you to give her a different type of exercise."
                wt_image cheater_photoshoot_41
                "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked.  Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, are not the least bit concerned about offending Lauren."
                wt_image cheater_photoshoot_42
                player.c "Pay attention.  We're going to keep doing this until you get it right.  Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now.  Start again, at the beginning."
                wt_image cheater_photoshoot_43
                "You make her work for it, but eventually she earns a mouthful of your cum to swallow before she heads home to hubbie with her photos."
                wt_image cheater_photoshoot_44
                player.c "[player.orgasm_text]"
                $ lauren.swallow_count += 1
                change lauren submission by 5
            elif lauren.blowjob_count == 2:
                wt_image cheater_photoshoot_42
                player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
                wt_image cheater_photoshoot_39
                player.c "First though, we're gong to add some new wrinkles ... excuse the pun."
                wt_image cheater_ball_lick_1
                player.c "Get your tongue down there on my balls, Lauren.  Give them a good washing, then get your mouth around them.  Gently.  Let them warm up in your mouth.  I'll tell you when I'm ready for you to start sucking my cock again.  Until then, use your hand to gently stroke me until your mouth takes its place."
                wt_image cheater_photoshoot_38
                "Once you're satisfied with the way she's pleasuring your balls, you let her go back to your cock ..."
                wt_image cheater_photoshoot_43
                "... where she works hard to earn a mouthful of your cum to swallow before she heads home to hubbie with her photos."
                wt_image cheater_photoshoot_44
                player.c "[player.orgasm_text]"
                $ lauren.swallow_count += 1
                change lauren resistance by -5
            elif lauren.blowjob_count == 3:
                wt_image cheater_photoshoot_40
                "Lauren gets straight to work, pleasuring your cock ..."
                wt_image cheater_ball_lick_1
                "... and your balls."
                wt_image cheater_photoshoot_41
                player.c "You're starting to get the hang of this, slut.  Good technique with my balls, getting them nice and warm.  Nice responsiveness to my hand in your hair, slowing down and speeding up as soon as I shift my grip.  No need for me to pull your head around like a pumpkin anymore before you figure out what I want."
                wt_image cheater_photoshoot_43
                player.c "You're on your way to becoming a fine little cocksucker, slut.  Does that feel good, knowing that you're finally able to please a man properly with your mouth?"
                wt_image cheater_photoshoot_38
                "Meekly, she nods her head as you give her a mouthful of your cum to swallow before she heads home to hubbie with her photos."
                wt_image cheater_photoshoot_44
                player.c "[player.orgasm_text]"
                $ lauren.swallow_count += 1
                change lauren sos by 5
            else:
                wt_image cheater_photoshoot_40
                "Lauren knows what she's doing now.  She gets your cock standing at attention ..."
                wt_image cheater_ball_lick_1
                "... then concentrates her efforts on your balls until your shaft is throbbing in her hand."
                wt_image cheater_photoshoot_38
                "There's no need to correct her technique.  That doesn't mean, however, that you can't have a little fun with her situation."
                wt_image cheater_photoshoot_41
                player.c "Does this feel good, little slut, sucking my cock while Ian watches?  Which did you like better, fucking Ian while I took pictures of you or showing off your cock-sucking skills while Ian watches?"
                wt_image cheater_photoshoot_39
                player.c "Don't bother answering that.  A good slut is happy to be fucked at any time, regardless of who is watching her.  And you are a good slut now, aren't you?"
                wt_image cheater_photoshoot_43
                "Perhaps it was just part of the blow job she's giving you, but Lauren definitely nods her head in response to your question.  For her honesty, you reward her with a mouthful of your cum to swallow before she heads home to hubbie with her photos."
                player.c "[player.orgasm_text]"
                $ lauren.swallow_count += 1
            orgasm
        "No, just send her home with her photos":
            wt_image cheater_photoshoot_33
            player.c "You should be pleased with your photos and how you paid for them, slut.  I'm sure your husband will be pleased, too.  The role he has in mind for you suits you.  I think you're starting to realize that, even if you struggle to admit it."
    change lauren sos by 15
    change player energy by -energy_short
    call forced_movement(living_room) from _call_forced_movement_157
    return

label lauren_workout_blowjob:
    $ lauren.blowjob_count += 1
    if lauren.blowjob_count == 1:
        player.c "Not like that.  Use more of your tongue.  Back and forth along the underside of my cock."
        player.c "Slow down.  I'll tell you when it's time to speed up.  Lips only for now.  Swallow me, right down to the base.  Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
        "Paul may have given Lauren a work out of one type.  Now it's time for you to give her a different type of exercise."
        "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked.  Like most women, she's never had her cock sucking technique critiqued before.  Most men are too happy to get a blow job, even a bad one, to risk offending the provider.  You, on the other hand, are not the least bit concerned about offending Lauren."
        player.c "Pay attention.  We're going to keep doing this until you get it right.  Your husband is paying me good money to train you, and I'm going to send you back to him as a proper cock sucker, not the pathetic amateur you are now.  Start again, at the beginning."
        "You make her work for it, but eventually she earns a mouthful of your cum."
        player.c "[player.orgasm_text]"
        $ lauren.swallow_count += 1
        change lauren submission by 5
    elif lauren.blowjob_count == 2:
        player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
        player.c "First though, we're gong to add some new wrinkles ... excuse the pun."
        wt_image cheater_ball_lick_1
        player.c "Get your tongue down there on my balls, Lauren.  Give them a good washing, then get your mouth around them.  Gently.  Let them warm up in your mouth.  I'll tell you when I'm ready for you to start sucking my cock again.  Until then, use your hand to gently stroke me until your mouth takes its place."
        player.c "[player.orgasm_text]"
        $ lauren.swallow_count += 1
        change lauren resistance by -5
    elif lauren.blowjob_count == 3:
        player.c "You're starting to get the hang of this, slut.  Good technique with my balls, getting them nice and warm before you started sucking my cock.  Nice responsiveness to my hand in your hair, slowing down and speeding up as soon as I shift my grip.  No need for me to pull your head around like a pumpkin anymore before you figure out what I want."
        player.c "You're on your way to becoming a fine little cocksucker, slut.  Does that feel good, knowing that you're finally able to please a man properly with your mouth?"
        player.c "[player.orgasm_text]"
        $ lauren.swallow_count += 1
        change lauren sos by 5
    else:
        "Lauren knows what she's doing now.  There's no need to correct her technique.  That doesn't mean, however, that you can't have a little fun with her situation."
        if lauren.workout_count == 3:
            player.c "Does this feel good, little slut, sucking my cock while Paul watches?  Which did you like better, fucking Paul while I watched, or showing off your cock sucking skills while Paul watches?"
        else:
            player.c "Does this feel good, little slut, sucking my cock while Ian watches?  Which did you like better, fucking Ian while I took pictures of you, or showing off your cock sucking skills while Ian watches?"
        player.c "Don't bother answering that.  A good slut is happy to be fucked at any time, regardless of who is watching her.  And you are a good slut now, aren't you?"
        "Perhaps it was just part of the blow job she's giving you, but Lauren definitely nods her head in response to your question."
        player.c "[player.orgasm_text]"
        $ lauren.swallow_count += 1
    orgasm
    return

# Lend Her Out For Revenge
label lauren_revenge:
    if lauren.revenge_count == 0 or lauren.revenge_count == 1:
        call lauren_revenge_discussion from _call_lauren_revenge_discussion
    elif lauren.revenge_count == 2:
        call lauren_revenge_first from _call_lauren_revenge_first
    elif lauren.revenge_count == 3:
        if geri.g_status == 2:
            call lauren_revenge_geri from _call_lauren_revenge_geri
        elif lauren.punishment_count > 1:
            call lauren_revenge_lee from _call_lauren_revenge_lee
        else:
            $ lauren.remove_tags('trained_today', 'trained_this_week')
            "The next woman you've located who wants revenge on a cheater wants to tie Lauren up and beat her. You'll need Lauren to be used to taking punishments before setting up that encounter.  For today, try another activity."
    elif lauren.revenge_count == 4:
        if lauren.punishment_count > 1:
            call lauren_revenge_lee from _call_lauren_revenge_lee_1
        else:
            "The next woman you've located who wants revenge on a cheater wants to tie Lauren up and beat her. You'll need Lauren to be used to taking punishments before setting up that encounter.  For today, try another activity."
    elif lauren.revenge_count == 5:
        if geri.g_status == 2:
            call lauren_revenge_geri from _call_lauren_revenge_geri_1
        else:
            "There's no one for you to lend Lauren out to right now.  Try another activity."
    elif lauren.revenge_count == 6:
        "You've lent Lauren out for revenge to as many women as are available to lend her to.  Try another activity."
    return

label lauren_revenge_discussion:
    add tags 'revenge_discussion_this_week' to lauren
    if lauren.revenge_count == 0:
        player.c "The man you cheated on your husband with ... the one you were caught cheating with, I mean ... he had a wife, didn't he?"
        lauren.c "Yes"
        player.c "In fact, she was the one who uncovered your cheating, and told your husband, wasn't she?"
        lauren.c "Yes"
        player.c "You didn't just hurt your husband by fooling around with him, you hurt her too, didn't you?"
        wt_image cheater_initial_2
        lauren.c "Do you have a point?"
        player.c "Yes.  You need to pay for your past transgressions. Good, caring wives are constantly being hurt by hussies like you luring away their husbands. It's time for you to make amends."
        lauren.c "You didn't contact her?"
        player.c "I did, actually. Sadly, she wants to put the whole sordid affair behind her and forget about it and you."
        player.c "Other women, however, are not so forgiving. I put an ad online, advertising that I had a cheating slut available for use by women who've been cheated on and would like revenge."
        if geri.g_status == 2:
            "You also have your real estate agent, Geri, in mind, but you'll disclose that to Lauren at the proper time."
    else:
        player.c "Lauren, are you ready to submit yourself to punishment by another woman as a way to pay for your transgressions?"
    if lauren.test('resistance', 25):
        $ lauren.revenge_count = 2
        wt_image cheater_initial_2
        lauren.c "How will you know I'll be safe?"
        player.c "I'll be there, to supervise your punishment."
        wt_image cheater_hypno_1_23
        "Lauren hangs her head. Her resistance to you is low enough that she's ready to accept this part of her training. You'll just need to set it up first, which you can do on any future session."
        "For today, choose another activity."
    else:
        if lauren.revenge_count == 0:
            wt_image cheater_initial_6
            lauren.c "You're insane.  I'm not going to let you lend me out to some crazed woman you found online who wants revenge on other women.  I didn't hurt her."
            player.c "No, but you did hurt someone else.  And part of your training, to make sure you don't hurt another woman again in the future, will be for you to submit to punishment by another woman for your transgressions."
        else:
            wt_image cheater_initial_6
            "She shakes her head no."
            player.c "That's a shame.  It seems I've been failing in my training of you.  I'll need to rectify that."
        "Lauren isn't ready to accept this part of her training yet.  You'll need to lower her resistance to you first.  For today, choose another activity."
        $ lauren.revenge_count = 1
    return

label lauren_revenge_first:
    $ lauren.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ lauren.revenge_count = 3
    if geri.g_status == 2:
        "Lauren would be the perfect offering to your real estate agent, Geri, to help Geri realize her fantasy about getting revenge on the woman who slept with her husband."
        "You're worried, however, that as much as Lauren has agreed to do this, she's still resentful and may balk if she isn't treated with a firm hand."
    "You've selected a woman who replied to your online ad and who, from subsequent correspondence, you feel confident is more than capable of handling Lauren."
    player.c "Strip down to your underwear and wait on the sofa, Lauren.  It's time for you to make amends for your cheating ways."
    wt_image cheater_revenge_1_1
    lauren_victoria "Is this the cheating whore who's been fucking other women's husbands?"
    player.c "Yes, Victoria. This is Lauren, the little slut I was telling you about. Lauren, this is Victoria. She was a faithful wife, whose husband of 25 years ran away on her with his secretary."
    player.c "She's upset about that.  I told her you would be happy to let her work out her frustrations on you."
    "Lauren's posture and eye roll tells both of you she is anything but happy about the situation."
    wt_image cheater_revenge_1_2
    lauren_victoria "Is that true, whore?  Are you ready to pay for your sin of fucking another man's wife?"
    "Lauren keeps her arms crossed and says nothing."
    player.c "Lauren."
    lauren.c "Fine.  Yes, I'm ready for you to work out your petty revenge fantasy on me."
    wt_image cheater_revenge_1_3
    lauren_victoria "You're not remorseful at all, are you?  You don't really care about the women you hurt by sleeping around with their men."
    lauren_victoria "And you know what?  I'm glad.  Because if you had been sorry, I might have gone easy on you.  And I didn't want to go easy on you."
    lauren_victoria "I want to make you suffer, the way I've suffered.  The way the wives of the men you slept with suffered when they found out they'd been cheated on."
    wt_image cheater_revenge_1_4
    lauren_victoria "This dirty cunt of yours has been causing pain and suffering to other women, whore.  We've been paying because you can't keep your legs closed."
    lauren.c "Ow!"
    lauren_victoria "Well guess what, whore?  Tonight it's your turn to pay."
    if dungeon.has_item(floggers):
        wt_image cheater_revenge_1_5
        "You decide to be helpful, and fetch Victoria a riding crop from your dungeon.  When you return, you're surprised to see her stripped down and sporting a strap on."
        wt_image cheater_revenge_1_6
        "She gladly accepts the crop and turns her attention back to Lauren."
        lauren_victoria "You like fucking cocks so much, let's see how you do with this one."
        wt_image cheater_revenge_1_16
        lauren_victoria "You like being on your knees?  Well go on then."
        wt_image cheater_revenge_1_8
        lauren_victoria "Show me how a whore sucks cock."
    else:
        wt_image cheater_revenge_1_15
        "Victoria strips out of her clothes.  To yours and Lauren's surprise she pulls a strap on out of her purse and attaches it to the harness she's already wearing."
        lauren_victoria "You like fucking cocks so much, let's see how you do with this one."
        wt_image cheater_revenge_1_17
        lauren_victoria "You like being on your knees?  Well go on then.  Show me how a whore sucks cock."
    wt_image cheater_revenge_1_7
    lauren_victoria "Show me how your cheating mouth gets another woman's man hard and horny to fuck you, whore."
    wt_image cheater_revenge_1_18
    lauren_victoria "Well there was nothing special about that display. Maybe it's your cunt that's special? Is that it? Is your dirty little cunt irresistible? Let's try it out."
    wt_image cheater_revenge_1_19
    lauren_victoria "Come on, whore.  Show me how you use your cunt to please the men of other women."
    wt_image cheater_revenge_1_10
    "Victoria leans forward and slaps Lauren hard across the face."
    lauren.c "Ow!"
    lauren_victoria "I said fuck me, whore!  Show me!  Show me what's so special about this dirty little cunt!!"
    wt_image cheater_revenge_1_9
    lauren_victoria "Is that it?  Is that all you can do with your cunt?"
    wt_image cheater_revenge_1_20
    lauren_victoria "There's nothing special about you.  Men don't cheat on their wives with you because you're special.  Do you know what you are?"
    lauren_victoria "Available.  That's all you are.  A warm piece of meat for them to stick their dick in because you don't have the decency to keep your legs closed around men who don't belong to you."
    wt_image cheater_revenge_1_21
    lauren_victoria "And do you know who you're available to now? Me. I'm going to use you the way those other women's men used you. As a warm piece of meat to get their jollies off on."
    lauren_victoria "And you're going to matter as much to me as you did to them, which is to say, not at all."
    if dungeon.has_item(floggers):
        wt_image cheater_revenge_1_14
        "Victoria removes the strap on and picks up the riding crop.  She lies back on the sofa and pulls Lauren's head into her crotch."
        lauren_victoria "Go on, you available piece of meat. I want to cum.  That's what you're for, isn't it?  Do it, and make it good."
        wt_image cheater_revenge_1_13
        lauren_victoria "I'm going to stay here and crop your sorry ass until I'm satisfied."
        "*thwappp*  *thwappp*  *thwappp*"
        lauren.c "nnnnnn"
        wt_image cheater_revenge_1_22
        "True to her word, Victoria keeps Lauren on her knees until she's licked her pussy to not one, but two orgasms, critiquing her efforts and cropping her ass all the way."
        wt_image cheater_revenge_1_23
    else:
        wt_image cheater_revenge_1_11
        "Victoria removes the strap on and straddles Lauren, pulling the trapped woman's head up and into her crotch."
        lauren_victoria "Go on, you available piece of meat. I want to cum.  That's what you're for, isn't it?  Do it, and make it good.  I'm going to stay on here until I'm satisfied."
        wt_image cheater_revenge_1_12
        "True to her word, Victoria rides Lauren's face to not one, but two orgasms, critiquing her efforts all the way."
        wt_image cheater_revenge_1_24
    lauren_victoria "Finally, that one was a little better.  If you ever cheat again, whore, I want you to remember this."
    lauren_victoria "I want you to remember to tell the man you're cheating with that you're available to lick his wife's cunt, if she wants, as a way to pay her back for the betrayal of sleeping with her husband."
    change lauren resistance by -5
    change lauren submission by 5
    change player energy by -energy_short notify
    end_day
    return

label lauren_revenge_geri:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    "Now that you know Lauren will accept being punished by another woman, it's time to deliver her to your real estate agent, Geri."
    wt_image phone_1
    if geri.has_tag('discussed_cheater'):
        "You've already told Geri you may have a solution to her problem.  You contact her again and ask her to drop by."
    else:
        "You give Geri a quick call."
        player.c "Geri, I may have a solution to your problem."
        geri.c "My problem?"
        player.c "The issue you've been obsessing over.  Swing by my house.  You'll be glad you did."
    if current_location != boudoir:
        call forced_movement(boudoir) from _call_forced_movement_158
    wt_image cheater_revenge_2_18
    player.c "Lauren, get into bed.  Wait there."
    summon geri
    wt_image cheater_revenge_2_1
    "A few minutes later, you hear Geri at the door."
    geri.c "Hello?"
    player.c "We're in here."
    wt_image cheater_revenge_2_2
    summon geri to boudoir no_follows
    "Lauren covers herself up as Geri steps into the room."
    geri.c "What's this?"
    player.c "This is Lauren.  She was caught having sex with the husband of another woman.  Now she's paying for her mistake by accepting punishment from other women who've been wronged."
    "For a moment, Geri hesitates. Then she remembers the sight of another woman, in her bed, having just fucked her husband. She remembers all the things she's imagined doing with that woman since then."
    wt_image cheater_revenge_2_3
    "She takes Lauren by the chin and pulls her face around to look at her."
    geri.c "Is this true?"
    lauren.c "I didn't mean to hurt anybody.  I'm sorry I did.  I'm sorry someone hurt you."
    geri.c "We'll see how sorry you'll be in a few minutes."
    wt_image cheater_revenge_2_4
    "Geri pushes Lauren down on the bed and pulls down her panties."
    wt_image cheater_revenge_2_5
    "Roughly she shoves two fingers into Lauren's pussy."
    lauren.c "Ow!"
    geri.c "You cheating cunt.  Do you still have my husband's cum inside you?"
    lauren.c "I'm not ..."
    geri.c "Shut up, you dirty cunt.  I'm going to do with you what I should have done with her.  And what the woman you hurt should have done to you."
    wt_image cheater_revenge_2_6
    "Geri lifts her hand ..."
    wt_image cheater_revenge_2_7
    "... then brings it down hard on Lauren's bare ass ... *SMACKKK*"
    lauren.c "OW!!"
    wt_image cheater_revenge_2_8
    "Geri keeps up the spanking until her hand and Lauren's ass are both red ... *SMACKKK*  *SMACKKK*  *SMACKKK*  *SMACKKK*  *SMACKKK*"
    lauren.c "OOWWW!!  OW!!  OW!!  OW!!  OOOWWWWW!!!"
    wt_image cheater_revenge_2_9
    "Then to yours and Lauren's surprise, Geri strips off her own clothes."
    geri.c "I've regretted not doing that ever since I found that bitch in my bed.  Do you know what else I regret?"
    "Lauren shakes her head no."
    wt_image cheater_revenge_2_19
    geri.c "I regret not pulling her ugly face down into my snatch and making her lick me out while my husband watches."
    wt_image cheater_revenge_2_10
    "Deep in her revenge fantasy now, Geri addresses her ex husband as if he was in the room."
    geri.c "Is this who you wanted to cheat on me with? Some little slut who'll fuck whatever cock or cunt is put in front of her? Look at your little hussy now."
    wt_image cheater_revenge_2_20
    geri.c "She's not yours, she's mine now, and I'm going to fill her mouth with my cunt juices."
    wt_image cheater_revenge_2_11
    "True to her word, Geri is soon coating Lauren's lips and tongue with her fluids as she bucks her hips against the younger woman's mouth."
    geri.c "Mmmmmm ... that's it, whore. Show my husband how much you love licking my cunt. Show him you're my bitch, not his."
    wt_image cheater_revenge_2_21
    geri.c "Aaaaaaaaaa!!"
    wt_image cheater_revenge_2_12
    "Then to your surprise, the two women hug tenderly."
    geri.c "Thank you for letting me do that.  I've needed to get that out of my system ever since that woman and my husband hurt me."
    lauren.c "I deserved it.  I think, maybe, some part of me needed to be treated like that, as reparations for the hurt I caused others.  So thank you, too."
    if lauren.blowjob_count > 0:
        $ title = "What do you do?"
        menu:
            "Let them go home":
                pass
            "Ask for your own thank you":
                wt_image cheater_revenge_2_13
                player.c "And what about me? Do I get a thank you for setting this up?"
                "The two women look at you."
                wt_image cheater_revenge_2_14
                "Then without a word they both kneel down in front of you and start licking your cock."
                if lauren.blowjob_count > 1:
                    wt_image cheater_revenge_2_23
                    "You're pleased at Lauren for remembering her instructions.  She lowers her head to take your balls into her mouth, and gently licks them with her tongue."
                    wt_image cheater_revenge_2_22
                    "It's the perfect complement to the sensation of Geri's lips wrapping around your cock for the first time."
                    wt_image cheater_revenge_2_15
                    "Between Lauren suckling your balls and Geri sliding her mouth up and down your shaft, the two women show you they are truly thankful ..."
                else:
                    wt_image cheater_revenge_2_16
                    "If Lauren were better trained, she'd be focusing on your balls, and leave your shaft for Geri to pleasure.  You'll need to correct that with a future lesson."
                    wt_image cheater_revenge_2_26
                    "For now, you're content to let both women lick, kiss and suck your cock, showing you they are truly thankful ..."
                wt_image cheater_revenge_2_16
                "... and you now have the opportunity to show them how much you enjoyed their 'thank you'."
                wt_image cheater_revenge_2_24
                player.c "Lie down, ladies.  I don't want to play favorites."
                wt_image cheater_revenge_2_17
                "You don't.  You deposit an equal amount of cum on each woman."
                player.c "[player.orgasm_text]"
                wt_image cheater_revenge_2_25
                player.c "I'm so glad you were able to drop by, Geri."
                geri.c "You said it would be worth my time, and you were right."
    if lauren.revenge_count == 3:
        $ lauren.revenge_count = 4
    else:
        $ lauren.revenge_count = 6
    $ geri.g_status = 3  ## triggers rewards from Geri
    change lauren sos by 10
    change player energy by -energy_short notify
    call character_location_return(geri) from _call_character_location_return_470
    end_day
    return

label lauren_revenge_lee:
    if lauren.revenge_count == 3:
        $ lauren.revenge_count = 5
    else:
        "The touching display between Lauren and Geri was nice, but you're not sure Lauren has fully learned her lesson about the consequences of cheating on other women."
        $ lauren.revenge_count = 6
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if current_location != dungeon:
        call forced_movement(dungeon) from _call_forced_movement_159
    summon lee
    wt_image cheater_revenge_3_1
    "You found Lee online.  She provided a very detailed, if largely misspelled, description of the things she wanted to do to a cheating woman.  You prepare a frightened Lauren for her arrival."
    wt_image cheater_revenge_3_10
    "Lee's a little rough around the edges. A biker chick, she's used to a rough-and-tumble world where scores are settled face-to-face. Her old man cheated on her once with a secretary, who wisely disappeared shortly thereafter. Ever since, Lee's been looking for an opportunity to take out her frustrations on a clean cut office girl."
    wt_image cheater_revenge_3_2
    "Lauren's a corporate executive, not a secretary, but there's no value to pointing that out to Lee."
    lee.c "Well look what we have here.  A slutty little office bitch knocked off her high horse and stuck down here in the dirt with the rest of us."
    wt_image cheater_revenge_3_11
    "Lee strips off her clothes and gets right to work."
    lauren.c "Ow!!  OW!!!"
    wt_image cheater_revenge_3_3
    lee.c "I've been waiting a long time to make a girl like you suffer.  Scream louder for me, office tart?"
    "With the sensation of the clothespins biting into her flesh, all Lauren can muster is a groan that may be masking a hint of stimulation."
    lauren.c "oohhhhhh"
    wt_image cheater_revenge_3_12
    lee.c "Ahh, no more screams? You think you're so much better than the rest of us. So special with your fancy office job. I bet you think you're too good to scream for a low life like me."
    wt_image cheater_revenge_3_13
    "But you're just a dirty, cheating bitch, and I'm going to wash that air of superiority off you."
    wt_image cheater_revenge_3_4
    lauren.c "aaaaaaa!!"
    lee.c "Not so special and superior now, are you tramp?"
    wt_image cheater_revenge_3_14
    lee.c "You're just a drowned rat down here in the gutter with the rest of us. In the gutter, I own your fancy ass. And I told you I want to hear you scream."
    wt_image cheater_revenge_3_5
    "Lee re-ties Lauren into an ass up position and prepares a surprise for her."
    lee.c "Are you scared, little office girl?"
    lauren.c "Yes"
    wt_image cheater_revenge_3_15
    lee.c "You should be.  I own your dirty tramp ass ..."
    wt_image cheater_revenge_3_16
    lee.c "... and I want you to scream."
    "*SMACKKK*"
    lauren.c "Ow!"
    wt_image cheater_revenge_3_17
    "*SMACKKK*  *SMACKKK*  *SMACKKK*"
    lauren.c "OW!!  OOWWW!!!  OOOWWWWW!!!"
    if dungeon.has_item(floggers):
        "Wanting to be helpful, you retrieve a flogger and hand it to Lee as Lauren stares at you in disbelief."
        player.c "Try this.  It'll save your hands."
        wt_image cheater_revenge_3_7
        "*THWAPPP*"
        lauren.c "OOWWWWWWW!!!!"
        lee.c "That's better.  Scream for me."
        wt_image cheater_revenge_3_6
        "*THWAPPP*  *THWAPPP*  *THWAPPP*"
        lauren.c "OOOOOWWWWWWWW!!!"
    else:
        lauren.c "That's better.  Scream for me."
        "*SMACKKK*  *SMACKKK*  *SMACKKK*"
        lauren.c "OOOOOWWWWWWWW!!!"
    wt_image cheater_revenge_3_19
    "You're a little worried Lee's sadism will take Lauren too far, but she eventually halts in order to finally show off to Lauren the surprise she prepared for her. Between her legs, Lee sports the longest strap on dildo you've ever seen.  She pushes just the first few inches of it inside her bound victim."
    lee.c "Can you guess what that is?  I bet a smart office girl like you knows."
    wt_image cheater_revenge_3_20
    lee.c "Who owns your ass, tramp?"
    lauren.c "You do."
    wt_image cheater_revenge_3_21
    lee.c "That's right.  And now I'm going to show you how a real woman fucks a cheating whore."
    wt_image cheater_revenge_3_8
    "Tied as she is, Lauren's helpless to protect herself as Lee fucks her. The oversized dildo rams into her, slamming into the back of her vagina and the opening of her uterus, battering and bruising her with every stroke."
    lauren.c "nnnnnnn"
    wt_image cheater_revenge_3_22
    lee.c "You think you're sore, now?  You ain't seen nothing, whore."
    wt_image cheater_revenge_3_23
    "Lee climbs on top of lauren and starts thrusting deeper and harder, ramming into her vagina from every angle."
    lauren.c "NNNNNNN"
    lee.c "This is how a real woman fucks, bitch. Next time you keep your prissy little ass away from another woman's man or you'll get fucked over real bad."
    wt_image cheater_revenge_3_9
    lee.c "Time to say you're sorry now, bitch."
    "Lauren starts licking Lee's pussy without hesitation."
    wt_image cheater_revenge_3_24
    "She's becoming an accomplished carpet muncher, and Lee soon rewards her with a gush of pussy fluid as she comes on the end of Lauren's tongue."
    lee.c "MMMMMM"
    wt_image cheater_revenge_3_9
    "That's better, bitch.  Don't let me catch you cheating again.  If I get my hands on you a second time, I'll make today seem like a walk in the park."
    change lauren submission by 5
    change lauren resistance by -5
    change player energy by -energy_short notify
    call character_location_return(lauren) from _call_character_location_return_471
    call chelsea_lee_encounter_lauren_training from _call_chelsea_lee_encounter_lauren_training
    end_day
    return

# Use Fuck Machine on Her
label lauren_fuck_machine:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ lauren.fuck_machine_count += 1
    if lauren.fuck_machine_count == 1:
        "You have Lauren wait for you while you set the machine up on your desk.  When you're ready, you come get her."
        player.c "Strip"
        lauren.c "Just like that?"
        player.c "Yes"
        wt_image cheater_machine_1
        "You lay the naked woman down on her back while you move the machine into position."
        lauren.c "What is this supposed to do, exactly?"
        player.c "Help tame sluts who let their greedy little pussies lead them astray.  Scooch your hips up to the edge of the desk."
        wt_image cheater_machine_12
        "You fit the dildo head into Lauren's snatch, then turn on the machine ..."
        wt_image cheater_machine_2
        "She gasps as the machine starts pistoning in and out of her ... *wuppp*  *wuppp* *wuppp*"
        lauren.c "Oh!"
        player.c "Ingenious device, isn't it?  I expect the inventor had a woman like you in mind.  Someone whose greedy little cunt leads her astray.  You'll see it has two effects."
        player.c "First, it gives your cunt a good fucking.  That should help keep it satisfied and less likely to send you running off cheating behind your husband's back."
        wt_image cheater_machine_13
        lauren.c "oooo  ...  oooooo ...  ow!"
        wt_image cheater_machine_10
        player.c "Second, as you're discovering, it delivers quite a pounding.  One that can quickly become uncomfortable without ever stopping being pleasurable."
        player.c "That's a good lesson for your cunt to learn.  Fucking comes at a price, and a greedy cunt needs to suffer the consequences."
        lauren.c "oooo  ...  oooooo ..."
        wt_image cheater_machine_3
        lauren.c "... ow!"
        wt_image cheater_machine_9
        player.c "It looks like you've got too much room to move.  You'll never get the full lesson if you keep backing up like that."
        wt_image cheater_machine_14
        "You reposition the machine on the desk itself, and use the opportunity to change the dildo head to a larger size."
        wt_image cheater_machine_4
        player.c "There.  If you try backing up again, you'll fall off the edge of the desk.  Don't do that."
        "One advantage of the fuck machine is that it does the work of training Lauren for you while you attend to other matters ... *wuppp*  *wuppp*  *wuppp*"
        lauren.c "ooooo"
        wt_image cheater_machine_11
        "Before long, you catch the telltale sign of an orgasm building up in Lauren."
        player.c "Oh no you don't.  No orgasms for this greedy little cunt until its lesson is over.  And not until it learns how to ask nicely."
        wt_image cheater_machine_18
        "She groans in frustration as you shut off the machine and remove the dildo head from her."
        lauren.c "oohhh"
        wt_image cheater_machine_6
        "You turn Lauren around and reposition the fuck machine so that it drives into her at a different angle."
        player.c "Stay like that until I tell you you can move.  And don't let me catch you trying to sneak an orgasm in without permission."
        "You turn the machine back on and return to your work. In the background the wuppp-wuppp-wuppp of the machine is interspersed with Lauren's moans and groans as her poor tortured pussy hovers on the brink of orgasm."
        lauren.c "oooooo"
        if lauren.test('submission', 20):
            wt_image cheater_machine_15
            "Lauren doesn't want to admit that she needs to cum, but the burning sensation between her legs is becoming too much and her submission to you is high enough that she's not above begging."
            lauren.c "I need to cum.  Please.  Am I allowed to cum?"
            player.c "Does this greedy little cunt admit how much it needs to be fucked and cum?"
            lauren.c "Yes"
            player.c "Make me believe you."
            lauren.c "Yes!  I admit I need to be fucked and to cum!"
            player.c "Does this greedy little cunt understand that it only gets to fuck and cum when it's husband or I allow it to fuck and cum?"
            lauren.c "Oohhhh ... Yes!  Yes, I understand.  Please let me cum.  Please??"
            player.c "I think you should ask the machine, too, since it's the one that has to do the work."
            wt_image cheater_machine_16
            lauren.c "Oohhhh ... Machine, may I please cum?"
            player.c "You're in luck.  The machine says 'yes'."
            wt_image cheater_machine_7
            lauren.c "Aaahhhh!!!!"
            player.c "Would you like another?"
            lauren.c "Y ... yesss ... pleaassse"
            wt_image cheater_machine_17
            "You turn Lauren on her side to adjust the angle of entry, then turn up the speed of the machine to increase the pace at which it slams in and out of her ... *wuppp*  *wuppp*  *wuppp*"
            wt_image cheater_machine_5
            "Within seconds she experiences one of the most intense orgasms of her life."
            lauren.c "AAAAAHHHHHH!!!!!!!"
            "As her orgasm subsides, you turn the speed of the machine up yet another notch.  To her shock, Lauren's body immediately begins a third orgasm, even more intense than the last."
            wt_image cheater_machine_5
            lauren.c "Oh God  ...  No!  ...  OH SHIT!!  ... AAAAGGGHHHH!!!!!!"
            wt_image cheater_machine_9
            "When the second wave of tremors cease, you turn the machine off."
            wt_image cheater_machine_19
            "Lauren lies in a pool on your desk for a full fifteen minutes before she can move.  When she's finally recovered, you let her dress and send her home."
            $ lauren.fuck_machine_orgasm_count += 1
            change lauren desire by 10
            change lauren submission by 10
            change lauren resistance by -10
        else:
            wt_image cheater_machine_16
            "Despite the burning need building between her legs, Lauren is too proud to ask you for permission to cum."
            wt_image cheater_machine_18
            "She successfully fights her urges until you release her.  She groans in relief when you finally turn the machine off."
            lauren.c "oohhh"
            wt_image cheater_machine_19
            "Deep inside, though, she wishes that she hadn't been so proud.  She wanted to cum, and she can't help feeling that begging you to let her cum would have been worth it."
            "It takes her a few minutes before her trembling legs are able to support her weight again.  When they are, you let her dress and send her home."
            change lauren submission by 10
            change lauren resistance by -5
    else:
        "Lauren knows what's coming when she sees you set up the machine."
        if lauren.fuck_machine_orgasm_count == 0:
            lauren.c "No.  Not again."
            player.c "Yes, again.  The purpose of a fuck machine is to fuck a slut into submission.  We're going to keep doing this until the machine does it's job."
        wt_image cheater_machine_1
        player.c "Get into position."
        if lauren.fuck_machine_orgasm_count == 0:
            wt_image cheater_machine_12
            "You slide the head of the dildo inside her while she tries to think about anything other than what's about to happen."
        else:
            wt_image cheater_machine_20
            player.c "You're already wet, slut.  You're going to be begging in no time."
        wt_image cheater_machine_2
        "She begins to moan as soon as the machine is turned on ... *wuppp*  *wuppp*  *wuppp*"
        lauren.c "oooo"
        wt_image cheater_machine_13
        "... but the pleasure is soon mixed with pain."
        lauren.c "oooo ... ow!"
        wt_image cheater_machine_3
        "She backs away from the relentless pounding ..."
        lauren.c "oooo ... ow! ... oooooo ... ow!"
        wt_image cheater_machine_16
        "You stop her and re-position her on her knees facing away from the machine."
        wt_image cheater_machine_6
        "She seems to be better able to control the build up of pleasure between her legs in this position, which means the machine has longer to do its work of teasing her on the brink between pleasure and pain."
        lauren.c "oooooo"
        player.c "You know the rules. No moving until I turn the machine off.  No cumming without permission."
        if lauren.test('submission', 20):
            if lauren.fuck_machine_orgasm_count == 0:
                wt_image cheater_machine_15
                "Lauren doesn't want to admit that she needs to cum, but the burning sensation between her legs is becoming too much and her submission to you is high enough that she's not above begging."
                lauren.c "I need to cum.  Please.  Am I allowed to cum?"
                player.c "Does this greedy little cunt admit how much it needs to be fucked and cum?"
                lauren.c "Yes"
                player.c "Make me believe you."
                lauren.c "Yes!  I admit I need to be fucked and to cum!"
                player.c "Does this greedy little cunt understand that it only gets to fuck and cum when it's husband or I allow it to fuck and cum?"
                lauren.c "Oohhhh ... Yes!  Yes, I understand.  Please let me cum.  Please??"
                player.c "I think you should ask the machine, too, since it's the one that has to do the work."
                wt_image cheater_machine_16
                lauren.c "Oohhhh ... Machine, may I please cum?"
                player.c "You're in luck.  The machine says 'yes'."
                wt_image cheater_machine_7
                lauren.c "Aaahhhh!!!!"
                player.c "Would you like another?"
                lauren.c "Y ... yesss ... pleaassse"
                wt_image cheater_machine_17
                "You turn Lauren on her side to adjust the angle of entry, then turn up the speed of the machine to increase the pace at which it slams in and out of her ... *wuppp*  *wuppp*  *wuppp*"
                wt_image cheater_machine_5
                "Within seconds she experiences one of the most intense orgasms of her life."
                lauren.c "AAAAAHHHHHH!!!!!!!"
                "As her orgasm subsides, you turn the speed of the machine up yet another notch.  To her shock, Lauren's body immediately begins a third orgasm, even more intense than the last."
                wt_image cheater_machine_8
                lauren.c "Oh God  ...  No!  ...  OH SHIT!!  ... AAAAGGGHHHH!!!!!!"
                wt_image cheater_machine_9
                "When the second wave of tremors cease, you turn the machine off."
                wt_image cheater_machine_19
                "Lauren lies in a pool on your desk for a full fifteen minutes before she can move.  When she's finally recovered, you let her dress and send her home."
                change lauren desire by 10
                change lauren submission by 10
                change lauren resistance by -10
            elif lauren.fuck_machine_orgasm_count == 1:
                wt_image cheater_machine_16
                "Lauren bears the mechanical fucking quite well.  Eventually, though, the sensation between her legs is too much, and she's reduced to begging you again for another orgasm."
                wt_image cheater_machine_15
                lauren.c "Please.  I need to cum."
                player.c "What needs to cum?"
                lauren.c "This greedy little cunt."
                player.c "And how many times would this greedy cunt like to cum?  Once, twice, three times ... five?"
                lauren.c "I ... I'm not sure ... I just need to cum."
                player.c "Let's find out, shall we?  You can have your first orgasm."
                wt_image cheater_machine_7
                lauren.c "Aaahhhh!!!!"
                player.c "Would you like another?"
                lauren.c "Y ... yesss ... pleaassse"
                wt_image cheater_machine_17
                "You turn Lauren on her side to adjust the angle of entry, then turn up the speed of the machine to increase the pace at which it slams in and out of her ... *wuppp*  *wuppp*  *wuppp*"
                wt_image cheater_machine_5
                "Within seconds she's cumming again."
                lauren.c "AAAAAHHHHHH!!!!!!!"
                wt_image cheater_machine_8
                "Without giving her any time to recover, you turn the machine up another notch and watch as it pounds one, then two, then more orgasms out of her."
                lauren.c "AAAA ...  AAAA ....  AAAAGGGHHHH!!!!!!"
                wt_image cheater_machine_9
                "After the third climax, the screams stop, replaced by a continual deep guttural moan. Her brain is no longer functioning properly, and has no idea whether you pull three, or five, or ten orgasms out of her tortured sex before you turn off the machine."
                wt_image cheater_machine_19
                "You let her rest until her legs are able to support her again, then let her dress and go home."
                change lauren desire by 5
                change lauren submission by 5
                change lauren resistance by -5
            else:
                "Lauren starts trembling almost as soon as the machine starts fucking her from behind."
                "The memory of what it can do to her has her on the brink of climax right from the get go, and you need to turn the machine down to a slower and slower pace to keep her from reaching orgasm without permission."
                wt_image cheater_machine_16
                "Eventually, the hunger between her legs is too strong for her to resist, and she's reduced to begging again."
                wt_image cheater_machine_15
                lauren.c "Please.  Turn it up faster.  I need to cum."
                player.c "What needs to cum?"
                lauren.c "This greedy little cunt."
                player.c "And how many times would this greedy cunt like to cum, Once, twice, three times ... five?"
                lauren.c "Oohhh  ...  Just once.  That's all.  Please??"
                player.c "I suppose you can have one orgasm."
                wt_image cheater_machine_7
                lauren.c "Aaahhhh!!!!"
                "She said she only wanted one orgasm, but where would the fun be in that?  As she stops cumming, you bump up the machine to the next higher speed ...  *wuppp*  *wuppp*  *wuppp*"
                wt_image cheater_machine_5
                lauren.c "AAAAHHHHH!!!!!!!"
                "Then the next highest speed...  *wuppp*  *wuppp*  *wuppp*."
                wt_image cheater_machine_8
                lauren.c "AAAA ...  AAAA ....  AAAAGGGHHHH!!!!!!"
                wt_image cheater_machine_9
                "After that, the screams stop, replaced by a continual deep guttural moan.  Her brain is no longer functioning right, and she has no idea how many orgasms you pull out of her."
                wt_image cheater_machine_19
                "To be honest, neither do you.  You stop counting and simply let the machine fuck her until her exhausted body can no longer register another climax."
                "You let her rest until her legs are able to support her again, then let her dress and go home."
                change lauren submission by 5
                change lauren resistance by -5
            $ lauren.fuck_machine_orgasm_count += 1
        else:
            wt_image cheater_machine_16
            "Despite the burning need building between her legs, Lauren is too proud to ask you for permission to cum."
            wt_image cheater_machine_18
            "She successfully fights her urges until you release her.  She groans in relief when you finally turn the machine off."
            lauren.c "oohhh"
            wt_image cheater_machine_19
            "Deep inside, though, she wishes that she hadn't been so proud.  She wanted to cum, and she can't help feeling that begging you to let her cum would have been worth it."
            "It takes her a few minutes before her trembling legs are able to support her weight again.  When they are, you let her dress and send her home."
            change lauren submission by 10
            change lauren resistance by -5
    change player energy by -energy_short notify
    end_day
    return

## SEX SKILLS
label lauren_display_clothes_anal:
    if lauren.anal_count == 0:
        wt_image cheater_posing_1_82
        "As you turn Lauren around, she thinks you're going to take her vaginally from behind."
        wt_image cheater_posing_1_83
        "She's surprised to see you put the lubricant on your cock, but she's not really wet yet and just assumes you're trying to go easy on her poor pussy."
        wt_image cheater_resisting_2
        "It's only when you place the tip of your cock against her anus that she realizes your true intention."
        wt_image cheater_resisting_5
        call lauren_anal_question from _call_lauren_anal_question
        # finishers for anal question
        if lauren.has_tag('no_anal'):
            wt_image cheater_happy_1
            lauren.c "Yes.  Yes, I understand.  Thank you."
            wt_image cheater_posing_1_30
            "Unprompted, she drops to her knees and kisses your cock, trying to show you that she can be the obedient slut you and her husband want her to be."
            wt_image cheater_hypno_1_13
            "She heads home as happy as you've seen her, pleased that you were willing to allow her at least one limit."
        elif lauren.anal_count == 1:
            wt_image cheater_posing_1_40
            "When you're finished, she's unusually quiet getting ready to go home, lost in her own thoughts. Will she tell her husband tonight what she did with you?"
            wt_image cheater_initial_1
            "You'll let her decide for today.  You'll send him home the evidence after your next session, once she's had a chance to get used to the idea of her new availability."
        elif lauren.has_tag('failed_training'):
            wt_image cheater_resisting_1
            "Lauren twists out from underneath you and stands up."
            wt_image cheater_resisting_3
            "She grabs up her clothes and runs to the door, stopping only long enough to pull on enough covering to be decent."
            wt_image current_location.image
            "Then she's gone.  She won't be answering your calls in the future."
        elif lauren.has_tag('anal_postponed_today'):
            rem tags 'anal_postponed_today' from lauren
        else:
            wt_image cheater_resisting_1
            "Lauren twists out from underneath you and stands up.  She's angry, but it seems she's not ready to call things off just yet."
            wt_image cheater_initial_1
            "That's it for tonight, however.  You send her home, unhappy.  She knows she's failed in your eyes, and in her eyes, you have too."
    elif lauren.anal_count == 1:
        wt_image cheater_nervous_1
        call lauren_second_anal from _call_lauren_second_anal
    elif lauren.anal_count > 1:
        call lauren_additional_anal from _call_lauren_additional_anal
    call lauren_anal_stat_changes from _call_lauren_anal_stat_changes
    return

label lauren_display_clothes_fuck:
    # first sex scene
    if lauren.sex_count == 0:
        if lauren.test('desire', 30) or lauren.test('resistance', 40):
            $ lauren.sex_count += 1
            wt_image cheater_resisting_1
            lauren.c "No, wait ... my husband ..."
            player.c "Your husband told me I'm free to use you however I want.  He wants an obedient slut who spreads her legs on command and that's what you're going to become.  Now open yourself up and show me what a good little slut you can be."
            wt_image cheater_posing_1_61
            "Whether it's because you've worn down her resistance to your instructions, or she secretly just wants to feel you inside her, her protests stop and she spreads her legs."
            wt_image cheater_posing_1_18
            "As you position your cock at her opening, her eyes lock on yours."
            wt_image cheater_posing_1_19
            "She cringes slightly as you push inside her, but holds your gaze."
            wt_image cheater_posing_1_63
            "She's been dreading this, dreading what it makes her: a woman who'll fuck other men on her husband's instructions."
            $ title = "How do you want to fuck her?"
            menu:
                "Make it pleasurable for her":
                    wt_image cheater_posing_1_64
                    "Recognizing her resistance, you take your time with her, going slowly and letting her body get used to the feel of you inside her."
                    wt_image cheater_posing_1_65
                    "At heart, she's a woman who loves sex.  Watching her carefully, you explore her body to discover what she responds to, and are eventually rewarded with a moan."
                    lauren.c "ooooo"
                    wt_image cheater_posing_1_66
                    "As the lubrication between her legs increases, you can fuck her faster and faster to the sound of her growing stimulation."
                    lauren.c "ooooo ... ooooooo"
                    wt_image cheater_posing_1_67
                    "She won't cum today, but she doesn't have to.  She's enjoyed it, and she knows you know she's enjoyed it."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_posing_1_65
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_68
                        "On her":
                            wt_image cheater_posing_1_69
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_70
                    add tags 'pleasurable_fuck_today' to lauren
                "Make it rough":
                    wt_image cheater_posing_1_71
                    "There's no point in pretending this is something it isn't.  She's a fuck toy for your use.  She knows it and you know it."
                    wt_image cheater_posing_1_63
                    "So you use her as exactly that.  You're not so rough as to really hurt her, but it's uncomfortable for her, and you don't bother with any lubrication."
                    wt_image cheater_posing_1_64
                    "If she's going to be ready for her husband on his terms, she needs to accept her role as fuck toy and learn how to get herself into the right head space to take this type of fucking on demand."
                    wt_image cheater_posing_1_19
                    "Her fingers rubbing herself as you fuck her tells you she understands this. It's not enough to get her anywhere close to climax, but that plus the feel of your cock inside her is enough to get her wet."
                    wt_image cheater_posing_1_71
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_posing_1_20
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_18
                        "On her":
                            wt_image cheater_posing_1_21
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_70
                    add tags 'rough_fuck_today' to lauren
            "There'll be no more protests when you tell her it's time to fuck."
            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_1
            orgasm
        # failed attempt
        else:
            wt_image cheater_resisting_1
            lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
            wt_image cheater_initial_1
            "You either need to reduce her resistance or raise her desire before Lauren will have intercourse with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
    # subsequent sex scenes
    elif lauren.sex_count >= 1:
        $ lauren.sex_count += 1
        # second sex scene
        if lauren.sex_count == 2:
            wt_image cheater_posing_1_59
            player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work. A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth.  Get up on here and show me what you can do with your cunt, slut."
            wt_image cheater_posing_1_72
            "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
            wt_image cheater_posing_1_73
            player.c "All right then, get to work.  Up and down, use your legs."
            wt_image cheater_posing_1_23
            player.c "Right up to the tip on your way up."
            wt_image cheater_posing_1_74
            player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
            wt_image cheater_posing_1_72
            player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
            wt_image cheater_posing_1_24
            player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
            wt_image cheater_posing_1_75
            "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
            if lauren.test('desire', 60):
                wt_image cheater_posing_1_72
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                lauren.c "oooooo"
                wt_image cheater_posing_1_76
                "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_posing_1_73
                player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_10
            wt_image cheater_posing_1_23
            "When she's learned as much as she's going to learn today, you let yourself cum."
            wt_image cheater_posing_1_24
            player.c "[player.orgasm_text]"
            lauren.c "Oh!"
            wt_image cheater_posing_1_74
            player.c "Remember to practice your lessons at home, slut.  Once your legs have recovered from the workout."
        # third sex scene
        elif lauren.sex_count == 3:
            player.c "Let's see if you're getting any better at fucking, Lauren."
            wt_image cheater_posing_1_18
            "You push her back against the table and position yourself at her entrance."
            player.c "I'm going to pin you down and shove myself inside you.  After that, you're going to do the work."
            wt_image cheater_posing_1_63
            lauren.c "Oh!"
            player.c  "You're not going to be able to move very much with me holding you in place. You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
            "Lauren nods."
            player.c "Good.  Then get at it."
            wt_image cheater_posing_1_71
            "You don't say anything more.  You just hold yourself and her in place on the table and watch her as she struggles to pleasure your cock within the limited range of movement you give her."
            if lauren.test('desire', 60):
                wt_image cheater_posing_1_65
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                lauren.c "oooooo"
                wt_image cheater_posing_1_66
                "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_posing_1_67
                player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_11
            wt_image cheater_posing_1_65
            "Eventually she succeeds in her appointed task, and you feel your orgasm building."
            wt_image cheater_posing_1_64
            "You pull yourself out of her ..."
            wt_image cheater_posing_1_21
            "... and let your cum spurt over her pussy and inner thighs"
            player.c "[player.orgasm_text]"
            wt_image cheater_posing_1_70
            "As she reaches a finger down to wipe it away, you stop her."
            player.c "Don't touch that.  Put your dress back on and be careful not to let any of the material soak up my cum.  You're going home like this."
            wt_image cheater_posing_1_77
            lauren.c "It'll drip down my legs!"
            player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
        # additional sex scene
        else:
            $ title = "How do you want to fuck her?"
            menu:
                "Hard from behind":
                    wt_image cheater_posing_1_22
                    "Roughly you turn Lauren around and shove yourself inside her."
                    lauren.c "Ow!"
                    player.c "Just because I'm behind you, slut, doesn't mean you don't have work to do.  Start moving those hips."
                    wt_image cheater_posing_1_78
                    "She gets wet now when you enter her, even when you're being rough, and is soon wiggling and rocking her hips back against you."
                    wt_image cheater_posing_1_79
                    "She fucks you as best she can with the limited range of motion you allow her.  There's not enough stimulus on her clit in this position for her to cum, but her pleasure isn't the point anyway."
                    wt_image cheater_posing_1_80
                    "Her role is to be a cum receptacle, and she does a fine job at that."
                    wt_image cheater_posing_1_81
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_posing_1_8
                    "Once she's finished serving her role, you send her home, carrying your jizz inside her."
                    add tags 'rough_fuck_today' to lauren
                "Gently on the table":
                    wt_image cheater_posing_1_68
                    "You lean Lauren back over the table and spread her legs, inserting just the tip of your cock inside her."
                    player.c "Give me a good fuck this time, little slut."
                    wt_image cheater_posing_1_65
                    "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you.  It feels nice for you, and it feels nice to her, too."
                    if lauren.test('desire', 60):
                        wt_image cheater_posing_1_67
                        "The feeling of your cock inside her and your body against her soon triggers a response."
                        wt_image cheater_posing_1_66
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_posing_1_67
                        player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_12
                    wt_image cheater_posing_1_63
                    "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                    wt_image cheater_posing_1_64
                    "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_posing_1_65
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_68
                            "You hold her there until your balls finish pumping their load into her well fucked pussy."
                        "On her":
                            wt_image cheater_posing_1_69
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_posing_1_70
                            "She knows better now than to clean it up."
                    wt_image cheater_posing_1_43
                    "She seems comfortable bringing home the sticky results of her efforts."
                    add tags 'pleasurable_fuck_today' to lauren
                "Her on top":
                    wt_image cheater_posing_1_72
                    "You sit down on the chair and pull Lauren on top of you."
                    wt_image cheater_posing_1_75
                    "You don't need to tell her what to do this time.  She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                    if lauren.test('desire', 60):
                        wt_image cheater_posing_1_24
                        "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                        lauren.c "ooooo"
                        wt_image cheater_posing_1_76
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_posing_1_73
                        player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_13
                    wt_image cheater_posing_1_23
                    "With an ever increasing pace she rides your cock, up to the tip ..."
                    wt_image cheater_posing_1_74
                    "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                    wt_image cheater_posing_1_73
                    "You make her work for it as long as you can ..."
                    wt_image cheater_posing_1_74
                    "... but you can only hold out so long under this treatment."
                    wt_image cheater_posing_1_24
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_posing_1_74
                    "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                    wt_image cheater_posing_1_43
                    "She seems comfortable heading home, carrying your load inside her."
                    add tags 'ride_fuck_today' to lauren
        call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_2
        orgasm
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_display_clothes_oral:
    $ lauren.blowjob_count += 1
    player.c "Have you been practicing, Lauren?"
    "She looks at you uncertainly for a moment."
    wt_image cheater_posing_1_59
    player.c "Your cock sucking skills, Lauren.  Have you been practicing?  Never mind answering, just get on your knees and show me."
    if lauren.blowjob_count == 2:
        wt_image cheater_posing_1_31
        call lauren_second_blowjob from _call_lauren_second_blowjob_4
        wt_image cheater_posing_1_26
        player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
    elif lauren.blowjob_count == 3:
        wt_image cheater_ball_lick_1
        "Lauren takes your balls into her mouth and warms them up ..."
        wt_image cheater_posing_1_30
        "... before shifting attention to your cock."
        wt_image cheater_posing_1_31
        call lauren_third_blowjob from _call_lauren_third_blowjob_4
    elif lauren.blowjob_count == 4:
        wt_image cheater_ball_lick_1
        "Lauren seems to have mastered her training."
        wt_image cheater_posing_1_26
        "She warms up your balls nicely, then continues to play with them as she sucks your cock."
        wt_image cheater_posing_1_30
        call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_5
    else:
        wt_image cheater_ball_lick_1
        "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
        wt_image cheater_posing_1_26
        "... then continues to play with them as she sucks your cock."
    wt_image cheater_posing_1_27
    "You relax and enjoy the rest of the blowjob ..."
    wt_image cheater_posing_1_28
    "... as she uses her mouth ..."
    wt_image cheater_posing_1_17
    "... to get you ready."
    wt_image cheater_posing_1_30
    $ title = "Where do you want to cum?"
    menu:
        "In her mouth":
            wt_image cheater_posing_1_62
            "You hold her head in place as you unload your cum down the back of her throat."
            player.c "[player.orgasm_text]"
            if lauren.blowjob_count > 3:
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_2
            wt_image cheater_posing_1_31
            player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
        "On her face" if lauren.blowjob_count > 3:
            add tags 'facial_today' to lauren
            if lauren.facial_count == 1:
                wt_image cheater_hypno_1_21
                "Lauren looks up in surprise as you pull your cock out of her mouth, then quickly closes her eyes as she realizes what you're doing."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                wt_image cheater_facial_4
                player.c "Clean yourself up, slut, then go home."
            elif lauren.facial_count == 2:
                wt_image cheater_hypno_1_21
                "As you pull out of her mouth, Lauren knows what to expect."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                wt_image cheater_facial_4
                player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                wt_image cheater_facial_2
                lauren.c "You can't expect me to go home like this?"
                player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                lauren.c "Yes"
            else:
                wt_image cheater_hypno_1_22
                "As you pull out of her mouth, Lauren licks the underside of your cock while offering her face as a target."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_5
                "She doesn't try to clean herself this time."
                wt_image cheater_facial_6
                "She does, however, clean off the tip of your cock as she looks up at you."
                wt_image cheater_facial_3
                "You leave her like that for a while, licking your cock and wearing your cum as she kneels on your floor, waiting to be dismissed and sent home to her husband."
            add tags 'facial_today' to lauren
    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_9
    orgasm
    return

label lauren_display_lingerie_oral:
    $ lauren.blowjob_count += 1
    player.c "Have you been practicing, Lauren?"
    "She looks at you uncertainly for a moment."
    # content for classy lingerie
    if lauren.has_tag('lingerie_classy'):
        wt_image cheater_blow_job_9
        player.c "Your cock sucking skills, Lauren.  Have you been practicing?  Never mind answering, just get on your knees and show me."
        if lauren.blowjob_count == 2:
            wt_image cheater_blow_job_5
            call lauren_second_blowjob from _call_lauren_second_blowjob_5
            wt_image cheater_blow_job_17
            player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
        elif lauren.blowjob_count == 3:
            wt_image cheater_ball_lick_1
            "Lauren takes your balls into her mouth and warms them up ..."
            wt_image cheater_blow_job_17
            "... before shifting attention to your cock."
            wt_image cheater_blow_job_14
            call lauren_third_blowjob from _call_lauren_third_blowjob_5
        elif lauren.blowjob_count == 4:
            wt_image cheater_ball_lick_1
            "Lauren seems to have mastered her training."
            wt_image cheater_blow_job_18
            "She warms up your balls nicely, then continues to play with them as she sucks your cock."
            wt_image cheater_blow_job_19
            call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_6
        else:
            wt_image cheater_ball_lick_1
            "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
            wt_image cheater_blow_job_18
            "... then continues to play with them as she sucks your cock."
        wt_image cheater_blow_job_10
        "You relax and enjoy the rest of the blowjob ..."
        wt_image cheater_blow_job_19
        "... as she uses her mouth ..."
        wt_image cheater_blow_job_5
        "... and tongue to get you ready."
        wt_image cheater_blow_job_18
        $ title = "Where do you want to cum?"
        menu:
            "In her mouth":
                wt_image cheater_blow_job_3
                "You hold her head in place as you unload your cum down the back of her throat."
                wt_image cheater_blow_job_15
                player.c "[player.orgasm_text]"
                if lauren.blowjob_count > 3:
                    wt_image cheater_blow_job_7
                    call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_3
                wt_image cheater_blow_job_18
                player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
            "On her face" if lauren.blowjob_count > 3:
                add tags 'facial_today' to lauren
                if lauren.facial_count == 1:
                    wt_image cheater_blow_job_8
                    "Lauren looks up in surprise as you pull your cock out of her mouth."
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_2
                    "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                    wt_image cheater_facial_4
                    player.c "Clean yourself up, slut, then go home."
                elif lauren.facial_count == 2:
                    wt_image cheater_blow_job_8
                    "As you pull out of her mouth, Lauren knows what to expect."
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_2
                    "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                    wt_image cheater_facial_4
                    player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                    wt_image cheater_facial_2
                    lauren.c "You can't expect me to go home like this?"
                    player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                    lauren.c "Yes"
                else:
                    wt_image cheater_blow_job_20
                    "As you pull out of her mouth, Lauren strokes your cock while offering her face as a target."
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_5
                    "She doesn't try to clean herself this time."
                    wt_image cheater_facial_6
                    "She does, however, clean off the tip of your cock as she looks up at you."
                    wt_image cheater_facial_3
                    "You leave her like that for a while, licking your cock and wearing your cum as she kneels on your floor, waiting to be dismissed and sent home to her husband."
                add tags 'facial_today' to lauren
    # content for slutty lingerie
    elif lauren.has_tag('lingerie_slutty'):
        wt_image cheater_posing_3_13
        player.c "Your cock sucking skills, Lauren.  Have you been practicing?  Never mind answering, just get on your knees and show me."
        if lauren.blowjob_count == 2:
            wt_image cheater_posing_3_16
            call lauren_second_blowjob from _call_lauren_second_blowjob_6
            wt_image cheater_posing_3_17
            player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
        elif lauren.blowjob_count == 3:
            wt_image cheater_ball_lick_1
            "Lauren takes your balls into her mouth and warms them up ..."
            wt_image cheater_posing_3_17
            "... before shifting attention to your cock."
            wt_image cheater_posing_3_51
            call lauren_third_blowjob from _call_lauren_third_blowjob_6
        elif lauren.blowjob_count == 4:
            wt_image cheater_ball_lick_1
            "Lauren seems to have mastered her training."
            wt_image cheater_posing_3_17
            "She warms up your balls nicely, then continues to play with them as she sucks your cock."
            wt_image cheater_posing_3_14
            call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_7
        else:
            wt_image cheater_ball_lick_1
            "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
            wt_image cheater_posing_3_17
            "... then continues to play with them as she sucks your cock."
        wt_image cheater_posing_3_18
        "You relax and enjoy the rest of the blowjob ..."
        wt_image cheater_posing_3_17
        "... as she uses her mouth ..."
        wt_image cheater_posing_3_14
        "... and tongue to get you ready."
        wt_image cheater_posing_3_16
        $ title = "Where do you want to cum?"
        menu:
            "In her mouth":
                wt_image cheater_posing_3_52
                "You hold her head in place as you unload your cum down the back of her throat."
                player.c "[player.orgasm_text]"
                if lauren.blowjob_count > 3:
                    wt_image cheater_posing_3_17
                    call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_4
                    if lauren.blowjob_count > 4 and lauren.has_tag('cum_arousal'):
                        wt_image cheater_posing_3_19
                        "She's squirming her hips so much you reach a hand between her legs and find your fingers slide into her easily as she moans around your cock."
                        lauren.c "mmmmmmmm"
                wt_image cheater_posing_3_54
                player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
            "On her face" if lauren.blowjob_count > 3:
                add tags 'facial_today' to lauren
                if lauren.facial_count == 1:
                    wt_image cheater_posing_3_55
                    "Lauren looks up in surprise as you pull your cock out of her mouth."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_posing_3_21
                    "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                    player.c "Clean yourself up, slut, then go home."
                elif lauren.facial_count == 2:
                    wt_image cheater_blow_job_8
                    "As you pull out of her mouth, Lauren knows what to expect."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_posing_3_21
                    "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                    player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                    lauren.c "You can't expect me to go home like this?"
                    player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                    lauren.c "Yes"
                else:
                    wt_image cheater_posing_3_55
                    "As you pull out of her mouth, Lauren licks the underside of your cockhead while offering her face as a target."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_posing_3_56
                    "She doesn't try to clean herself this time.  She does, however, clean off the tip of your cock as your cum drips down her cheek and chin."
                    wt_image cheater_posing_3_20
                    "You leave her like that for a while, licking your cock and wearing your cum as she kneels at your feet, waiting to be dismissed and sent home to her husband."
                add tags 'facial_today' to lauren
    # error as no lingerie tag identified
    else:
        sys "There's been an error in the lauren_display_lingerie_oral label.  Lauren was not identified as having an appropriate lingerie tag."
    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_10
    orgasm
    return

label lauren_display_lingerie_fuck:
    # classy lingerie content
    if lauren.has_tag('lingerie_classy'):
        # first sex scene
        if lauren.sex_count == 0:
            if lauren.test('desire', 30) or lauren.test('resistance', 40):
                $ lauren.sex_count += 1
                wt_image cheater_posing_2_39
                lauren.c "No, wait ... my husband ..."
                player.c "Your husband told me I'm free to use you however I want. He wants an obedient slut who spreads her legs on command, and that's what you're going to become. Now open yourself up and show me what a good little slut you can be."
                wt_image cheater_sex_12
                "Whether it's because you've worn down her resistance to your instructions, or she secretly just wants to feel you inside her, her protests stop and she spreads her legs."
                wt_image cheater_sex_1
                "Lauren watches as you position your cock at her opening."
                wt_image cheater_sex_13
                "She cringes slightly as you push inside her. She's been dreading this, dreading what it makes her: a woman who'll fuck other men on her husband's instructions."
                $ title = "How do you want to fuck her?"
                menu:
                    "Make it pleasurable for her":
                        wt_image cheater_sex_14
                        "Recognizing her resistance, you take your time with her, going slowly and letting her body get used to the feel of you inside her."
                        wt_image cheater_sex_15
                        "At heart, she's a woman who loves sex.  Watching her carefully, you explore her body to discover what she responds to, and are eventually rewarded with a moan."
                        lauren.c "ooooo"
                        wt_image cheater_sex_7
                        "As the lubrication between her legs increases, you can fuck her faster and faster to the sound of her growing stimulation."
                        lauren.c "ooooo ... ooooooo"
                        wt_image cheater_sex_15
                        "She won't cum today, but she doesn't have to.  She's enjoyed it, and she knows you know she's enjoyed it."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image cheater_sex_16
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_sex_14
                            "On her":
                                wt_image cheater_sex_1
                                lauren.c "What ..."
                                wt_image cheater_cum_1
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_sex_8
                        add tags 'pleasurable_fuck_today' to lauren
                    "Make it rough":
                        wt_image cheater_sex_14
                        "There's no point in pretending this is something it isn't.  She's a fuck toy for your use.  She knows it and you know it."
                        wt_image cheater_sex_2
                        "So you use her as exactly that.  You're not so rough as to really hurt her, but it's uncomfortable for her, and you don't bother with any lubrication."
                        wt_image cheater_sex_18
                        "If she's going to be ready for her husband on his terms, she needs to accept her role as fuck toy and learn how to get herself into the right head space to take this type of fucking on demand."
                        wt_image cheater_sex_19
                        "Her efforts to please you even when you slap her face tells you she understands this ... *slappp*  *slappp*  *slappp*"
                        wt_image cheater_sex_2
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image cheater_sex_4
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_sex_14
                            "On her":
                                wt_image cheater_sex_1
                                lauren.c "What ..."
                                wt_image cheater_cum_1
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_sex_8
                        add tags 'rough_fuck_today' to lauren
                "There'll be no more protests when you tell her it's time to fuck."
                call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_3
                orgasm
            # failed attempt
            else:
                wt_image cheater_posing_2_38
                lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
                wt_image cheater_posing_2_31
                "You either need to reduce her resistance or raise her desire before Lauren will have intercourse with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
        # subsequent sex scenes
        elif lauren.sex_count >= 1:
            $ lauren.sex_count += 1
            # second sex scene
            if lauren.sex_count == 2:
                player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
                wt_image cheater_posing_2_40
                player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
                player.c "Get up on here and show me what you can do with your cunt, slut."
                wt_image cheater_sex_5
                "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
                wt_image cheater_sex_22
                player.c "All right then, get to work.  Up and down, use your legs."
                wt_image cheater_sex_5
                player.c "Right up to the tip on your way up."
                wt_image cheater_sex_20
                player.c "Slam down hard at the bottom of the stroke.  Get him all the way inside you."
                wt_image cheater_sex_22
                player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
                wt_image cheater_sex_21
                player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
                wt_image cheater_sex_20
                "With your hands holding her wrists, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
                if lauren.test('desire', 60):
                    wt_image cheater_sex_21
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                    wt_image cheater_sex_6
                    "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_sex_21
                    player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_14
                wt_image cheater_sex_5
                "When she's learned as much as she's going to learn today, you let yourself cum."
                wt_image cheater_sex_22
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                wt_image cheater_sex_21
                player.c "Remember to practice your lessons at home, slut.  Once your legs have recovered from the workout."
            # third sex scene
            elif lauren.sex_count == 3:
                wt_image cheater_sex_12
                player.c "Let's see if you're getting any better at fucking, Lauren.  On your back, legs spread wide."
                wt_image cheater_sex_1
                "As she opens her legs, you position yourself at her entrance."
                wt_image cheater_sex_19
                player.c "I'm going to pin you down and shove myself inside you.  After that, you're going to do the work."
                wt_image cheater_sex_2
                lauren.c "Oh!"
                player.c  "You're not going to be able to move very much with me holding you in place. You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
                "Lauren nods."
                player.c "Good.  Then get at it."
                wt_image cheater_sex_7
                "You don't say anything more.  You just hold yourself and her in place and watch her as she struggles to pleasure your cock with the limited range of movement you give her."
                if lauren.test('desire', 60):
                    wt_image cheater_sex_15
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                    wt_image cheater_sex_3
                    "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_sex_16
                    player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_15
                wt_image cheater_sex_4
                "Eventually she succeeds in her appointed task, and you feel your orgasm building."
                wt_image cheater_sex_1
                "You pull yourself out of her ..."
                wt_image cheater_posing_1_17
                "... and let your cum spurt over her pussy."
                player.c "[player.orgasm_text]"
                wt_image cheater_sex_8
                "As she reaches a finger down to wipe it away, you stop her."
                player.c "Don't touch that.  Put your dress back on and be careful not to let any of the material soak up my cum.  You're going home like this."
                wt_image cheater_cum_1
                lauren.c "It'll drip down my legs!"
                wt_image cheater_posing_2_40
                player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
            # additional sex scene
            else:
                $ title = "How do you want to fuck her?"
                menu:
                    "Hard from behind":
                        wt_image cheater_sex_23
                        "Roughly you turn Lauren around and shove yourself inside her."
                        wt_image cheater_sex_24
                        lauren.c "Ow!"
                        wt_image cheater_sex_26
                        player.c "Just because I'm behind you, slut, doesn't mean you don't have work to do.  Start moving those hips."
                        wt_image cheater_sex_25
                        "She gets wet now when you enter her, even when you're being rough, and is soon wiggling and rocking her hips back against you."
                        wt_image cheater_sex_27
                        "She fucks you as best she can with the limited range of motion you allow her."
                        wt_image cheater_sex_10
                        "There's not enough stimulus on her clit in this position for her to cum, but her pleasure isn't the point anyway."
                        wt_image cheater_sex_26
                        "Her role is to be a cum receptacle, and she does a fine job at that."
                        wt_image cheater_sex_28
                        player.c "[player.orgasm_text]"
                        wt_image cheater_sex_29
                        lauren.c "Oh!"
                        wt_image cheater_sex_25
                        "Once she's finished serving her role, you send her home, carrying your jizz inside her."
                        add tags 'rough_fuck_today' to lauren
                    "Gently on the table":
                        wt_image cheater_sex_1
                        "You lean Lauren backwards and spread her legs, inserting just the tip of your cock inside her."
                        player.c "Give me a good fuck this time, little slut."
                        wt_image cheater_sex_7
                        "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you.  It feels nice for you, and it feels nice to her, too."
                        if lauren.test('desire', 60):
                            wt_image cheater_sex_15
                            "The feeling of your cock inside her and your body against her soon triggers a response."
                            wt_image cheater_sex_3
                            "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_sex_14
                            player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_16
                        wt_image cheater_sex_13
                        "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                        wt_image cheater_sex_7
                        "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image cheater_sex_16
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_sex_15
                                "You hold her there until your balls finish pumping their load into her well fucked pussy."
                            "On her":
                                wt_image cheater_sex_17
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_cum_1
                                "She knows better now than to clean it up."
                        wt_image cheater_posing_2_41
                        "Lauren seems comfortable bringing home the sticky results of her efforts."
                        add tags 'pleasurable_fuck_today' to lauren
                    "Her on top":
                        wt_image cheater_sex_5
                        "You sit down on a chair and pull Lauren on top of you."
                        wt_image cheater_sex_22
                        "You don't need to tell her what to do this time.  She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                        if lauren.test('desire', 60):
                            wt_image cheater_sex_20
                            "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                            lauren.c "ooooo"
                            wt_image cheater_sex_6
                            "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_sex_21
                            player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_17
                        wt_image cheater_sex_5
                        "With an ever increasing pace she rides your cock, up to the tip ..."
                        wt_image cheater_sex_22
                        "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                        wt_image cheater_sex_20
                        "You make her work for it as long as you can, but you can only hold out so long under this treatment."
                        wt_image cheater_sex_22
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_sex_21
                        "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                        wt_image cheater_posing_2_42
                        "She seems comfortable heading home, carrying your load inside her."
                        add tags 'ride_fuck_today' to lauren
            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_4
            orgasm
    # slutty lingerie content
    elif lauren.has_tag('lingerie_slutty'):
        # first sex scene
        if lauren.sex_count == 0:
            if lauren.test('desire', 30) or lauren.test('resistance', 40):
                $ lauren.sex_count += 1
                wt_image cheater_posing_3_13
                lauren.c "No, wait ... my husband ..."
                player.c "Your husband told me I'm free to use you however I want. He wants an obedient slut who spreads her legs on command, and that's what you're going to become."
                wt_image cheater_posing_3_24
                "Whether it's because you've worn down her resistance to your instructions, or she secretly just wants to feel you inside her, her protests stop as you position the head of your cock at her opening."
                wt_image cheater_posing_3_25
                "She grimaces as you push inside her. She's been dreading this, dreading what it makes her: a woman who'll fuck other men on her husband's instructions."
                $ title = "How do you want to fuck her?"
                menu:
                    "Make it pleasurable for her":
                        "Recognizing her resistance, you take your time with her, going slowly and letting her body get used to the feel of you inside her."
                        wt_image cheater_posing_3_26
                        "At heart, she's a woman who loves sex.  Watching her carefully, you explore her body to discover what she responds to, and are eventually rewarded with a moan."
                        lauren.c "oooo"
                        wt_image cheater_posing_3_57
                        player.c "That's a good slut.  You're enjoying this, aren't you?"
                        lauren.c "ooooo ... yes, that feels good."
                        wt_image cheater_posing_3_26
                        "She won't cum today, but she doesn't have to.  She's enjoyed it, and she knows you know she's enjoyed it.  You've enjoyed it, too."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_posing_3_57
                        lauren.c "Oh!"
                        add tags 'pleasurable_fuck_today' to lauren
                    "Make it rough":
                        wt_image cheater_posing_3_58
                        "There's no point in pretending this is something it isn't.  She's a fuck toy for your use.  She knows it and you know it."
                        lauren.c "Ow!"
                        wt_image cheater_posing_3_59
                        "So you use her as exactly that.  You're not so rough as to really hurt her, but it's uncomfortable for her, and you don't bother with any lubrication."
                        wt_image cheater_posing_3_27
                        "If she's going to be ready for her husband on his terms, she needs to accept her role as fuck toy and learn how to get herself into the right head space to take this type of fucking on demand."
                        wt_image cheater_posing_3_60
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        add tags 'rough_fuck_today' to lauren
                "There'll be no more protests when you tell her it's time to fuck."
                call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_5
                orgasm
            # failed attempt
            else:
                wt_image cheater_posing_3_4
                lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
                wt_image cheater_posing_3_1
                "You either need to reduce her resistance or raise her desire before Lauren will have intercourse with you. If you try to push this now, she's going to call the whole arrangement off. You have her dress and send her home."
        # subsequent sex scenes
        elif lauren.sex_count >= 1:
            $ lauren.sex_count += 1
            # second sex scene
            if lauren.sex_count == 2:
                player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
                wt_image cheater_posing_3_13
                player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
                player.c "Get up on here and show me what you can do with your cunt, slut."
                wt_image cheater_posing_3_28
                "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
                wt_image cheater_posing_3_61
                player.c "All right then, get to work.  Up and down, use your legs."
                wt_image cheater_posing_3_28
                player.c "Right up to the tip on your way up."
                wt_image cheater_posing_3_62
                player.c "Slam down hard at the bottom of the stroke.  Get him all the way inside you."
                wt_image cheater_posing_3_63
                player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
                wt_image cheater_posing_3_64
                player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
                lauren.c "Oh!"
                wt_image cheater_posing_3_28
                "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
                if lauren.test('desire', 60):
                    wt_image cheater_posing_3_29
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                    lauren.c "ooooo"
                    wt_image cheater_posing_3_65
                    "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_posing_3_61
                    player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_18
                wt_image cheater_posing_3_29
                "When she's learned as much as she's going to learn today, you let yourself cum."
                wt_image cheater_posing_3_62
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                wt_image cheater_posing_3_63
                player.c "Remember to practice your lessons at home, slut.  Once your legs have recovered from the workout."
            # third sex scene
            elif lauren.sex_count == 3:
                wt_image cheater_posing_3_13
                player.c "Let's see if you're getting any better at fucking, Lauren.  Climb on top of me."
                wt_image cheater_posing_3_66
                "You guide her down onto your cock, facing you."
                wt_image cheater_posing_3_30
                player.c "You're not going to be able to move very much with my arms holding you tight against me. You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
                "Lauren nods."
                player.c "Good.  Then get at it."
                wt_image cheater_posing_3_67
                "You don't say anything more.  You just hold yourself and her in place and watch her as she struggles to pleasure your cock with the limited range of movement you give her."
                if lauren.test('desire', 60):
                    wt_image cheater_posing_3_30
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                    wt_image cheater_posing_3_31
                    "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_posing_3_30
                    player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_19
                wt_image cheater_posing_3_30
                "Eventually she succeeds in her appointed task, and you feel your orgasm building."
                wt_image cheater_posing_3_68
                "To her surprise, you pull yourself out of her ..."
                wt_image cheater_cum_2
                "... and spurt your cum over her belly and pussy."
                player.c "[player.orgasm_text]"
                wt_image cheater_sex_8
                "As she reaches a finger down to wipe it away, you stop her."
                player.c "Don't touch that.  Put your dress back on and be careful not to let any of the material soak up my cum.  You're going home like this."
                wt_image cheater_cum_3
                lauren.c "It'll drip down my legs!"
                player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
            # additional sex scene
            else:
                $ title = "How do you want to fuck her?"
                menu:
                    "Roughly":
                        wt_image cheater_posing_3_69
                        player.c "Pull your legs up and open your cunt."
                        wt_image cheater_posing_3_70
                        "Roughly you jam your fingers into her."
                        lauren.c "Ow!"
                        player.c "Get wet, slut.  You're about to be fucked."
                        wt_image cheater_posing_3_32
                        "To her own surprise, she does get wet now whenever you enter her, even when you're being rough."
                        wt_image cheater_posing_3_33
                        "Before long, you're able to slide in and out of her easily as you fuck her hard and fast."
                        wt_image cheater_posing_3_35
                        player.c "Just because you're being used as a fucktoy, slut, doesn't mean you don't have work to do.  Start moving those hips."
                        wt_image cheater_posing_3_71
                        "She fucks you as best she can with the limited range of motion you allow her.  She won't cum with your hand gripping her throat, but her pleasure isn't the point anyway."
                        wt_image cheater_posing_3_35
                        "Her role is to be a cum receptacle, and she does a fine job at that."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image cheater_posing_3_71
                                player.c "[player.orgasm_text]"
                                wt_image cheater_posing_3_33
                                lauren.c "Oh!"
                                "You hold her there until your balls have finished pumping their load into her well fucked pussy."
                                wt_image cheater_posing_3_37
                                "Once she's finished serving her role, you send her home, carrying your jizz inside her."
                            "On her":
                                wt_image cheater_posing_3_68
                                "You pull out of her ..."
                                wt_image cheater_cum_2
                                "... and spurt your cum over her belly and pussy."
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_cum_3
                                "She knows better now than to clean it up."
                        add tags 'rough_fuck_today' to lauren
                    "Gently":
                        wt_image cheater_posing_3_22
                        "You lean Lauren backwards and spread her legs.  She moans as you caress her sex with your fingers."
                        lauren.c "oooo"
                        player.c "Give me a good fuck this time, little slut."
                        "She nods."
                        wt_image cheater_posing_3_32
                        "She moans again, louder, as you enter her."
                        lauren.c "oooooo"
                        wt_image cheater_posing_3_33
                        "She's thoroughly wet, and you're able to slide in and out of her easily."
                        wt_image cheater_posing_3_34
                        "Lauren does her best to wiggle her hips and and pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you.  It feels nice for you, and it feels nice to her, too."
                        if lauren.test('desire', 60):
                            wt_image cheater_posing_3_72
                            "The feeling of your cock inside her and your body against her soon triggers a response.  Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_posing_3_34
                            player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_20
                        wt_image cheater_posing_3_32
                        "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                        wt_image cheater_posing_3_34
                        "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image cheater_posing_3_33
                                player.c "[player.orgasm_text]"
                                wt_image cheater_posing_3_72
                                lauren.c "Oh!"
                                "You hold her there until your balls finish pumping their load into her well fucked pussy."
                            "On her":
                                wt_image cheater_posing_3_68
                                "You pull out of her ..."
                                wt_image cheater_cum_2
                                "... and spurt your cum over her belly and pussy."
                                player.c "[player.orgasm_text]"
                                lauren.c "Oh!"
                                wt_image cheater_cum_3
                                "She knows better now than to clean it up."
                        wt_image cheater_posing_3_48
                        "Lauren seems comfortable bringing home the sticky results of her efforts."
                        add tags 'pleasurable_fuck_today' to lauren
                    "Her on top":
                        wt_image cheater_posing_3_28
                        "You sit down on a chair and pull Lauren on top of you."
                        wt_image cheater_posing_3_63
                        "You don't need to tell her what to do this time.  She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                        if lauren.test('desire', 60):
                            wt_image cheater_posing_3_29
                            "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                            lauren.c "ooooo"
                            wt_image cheater_posing_3_65
                            "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_posing_3_61
                            player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_21
                        wt_image cheater_posing_3_28
                        "With an ever increasing pace she rides your cock, up to the tip ..."
                        wt_image cheater_posing_3_29
                        "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                        wt_image cheater_posing_3_63
                        "You make her work for it as long as you can, but you can only hold out so long under this treatment."
                        wt_image cheater_posing_3_62
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_posing_3_61
                        "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                        wt_image cheater_posing_3_48
                        "She seems comfortable heading home, carrying your load inside her."
                        add tags 'ride_fuck_today' to lauren
            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_6
            orgasm
    # error as no lingerie tag identified
    else:
        sys "There's been an error in the lauren_display_lingerie_fuck label.  Lauren was not identified as having an appropriate lingerie tag."
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_display_lingerie_anal:
    # classy lingerie content
    if lauren.has_tag('lingerie_classy'):
        if lauren.anal_count == 0:
            wt_image cheater_posing_2_36
            "As you turn Lauren around, she thinks you're going to take her vaginally from behind."
            wt_image cheater_posing_2_28
            "She's surprised to see you put the lubricant on your cock, but she's not really wet yet and just assumes you're trying to go easy on her poor pussy."
            wt_image cheater_posing_2_8
            "It's only when you place the tip of your cock against her anus that she realizes your true intention."
            call lauren_anal_question from _call_lauren_anal_question_1
            # finishers for anal question
            if lauren.has_tag('no_anal'):
                wt_image cheater_posing_2_39
                lauren.c "Yes.  Yes, I understand.  Thank you."
                wt_image cheater_blow_job_18
                "Unprompted, she drops to her knees and kisses your cock, trying to show you that she can be the obedient slut you and her husband want her to be."
                wt_image cheater_posing_2_17
                "She heads home happy, pleased that you were willing to allow her at least one limit."
            elif lauren.anal_count == 1:
                wt_image cheater_posing_2_21
                "When you're finished, she's unusually quiet getting ready to go home, lost in her own thoughts.  Will she tell her husband tonight what she did with you?"
                wt_image cheater_posing_2_29
                "You'll let her decide for today.  You'll send him home the evidence after your next session, once she's had a chance to get used to the idea of her new availability."
            elif lauren.has_tag('failed_training'):
                wt_image cheater_posing_2_38
                "Lauren twists out from underneath you and stands up."
                wt_image cheater_posing_2_10
                "She pulls on just enough clothes to be decent, before heading to the door."
                wt_image current_location.image
                "Then she's gone.  She won't be answering your calls in the future."
            elif lauren.has_tag('anal_postponed_today'):
                rem tags 'anal_postponed_today' from lauren
            else:
                wt_image cheater_posing_2_38
                "Lauren twists out from underneath you and stands up.  She's angry, but it seems she's not ready to call things off just yet."
                wt_image cheater_posing_2_31
                "That's it for tonight, however.  You send her home, unhappy.  She knows she's failed in your eyes, and in her eyes, you have too."
        elif lauren.anal_count == 1:
            wt_image cheater_nervous_1
            call lauren_second_anal from _call_lauren_second_anal_1
        elif lauren.anal_count > 1:
            call lauren_additional_anal from _call_lauren_additional_anal_1
    # slutty lingerie content
    elif lauren.has_tag('lingerie_slutty'):
        if lauren.anal_count == 0:
            wt_image cheater_posing_3_36
            "As you turn Lauren around, she thinks you're going to take her vaginally from behind.  She's surprised to see you put the lubricant on your cock, but she's not really wet yet and just assumes you're trying to go easy on her poor pussy."
            wt_image cheater_posing_3_8
            "It's only when you place the tip of your cock against her anus that she realizes your true intention."
            wt_image cheater_posing_3_36
            call lauren_anal_question from _call_lauren_anal_question_2
            # finishers for anal question
            if lauren.has_tag('no_anal'):
                wt_image cheater_posing_3_73
                lauren.c "Yes.  Yes, I understand.  Thank you."
                wt_image cheater_posing_3_17
                "Unprompted, she drops to her knees and kisses your cock, trying to show you that she can be the obedient slut you and her husband want her to be."
                wt_image cheater_posing_3_48
                "She heads home happy, pleased that you were willing to allow her at least one limit."
            elif lauren.anal_count == 1:
                wt_image cheater_posing_3_12
                "When you're finished, she's unusually quiet getting ready to go home, lost in her own thoughts.  Will she tell her husband tonight what she did with you?"
                wt_image cheater_posing_3_1
                "You'll let her decide for today.  You'll send him home the evidence after your next session, once she's had a chance to get used to the idea of her new availability."
            elif lauren.has_tag('failed_training'):
                wt_image cheater_posing_3_5
                "Lauren twists out from underneath you and stands up.  She pulls on just enough clothes to be decent, before heading to the door."
                wt_image current_location.image
                "Then she's gone.  She won't be answering your calls in the future."
            elif lauren.has_tag('anal_postponed_today'):
                rem tags 'anal_postponed_today' from lauren
            else:
                wt_image cheater_posing_3_5
                "Lauren twists out from underneath you and stands up.  She's angry, but it seems she's not ready to call things off just yet."
                wt_image cheater_posing_3_38
                "That's it for tonight, however.  You send her home, unhappy.  She knows she's failed in your eyes, and in her eyes, you have too."
        elif lauren.anal_count == 1:
            wt_image cheater_nervous_1
            call lauren_second_anal from _call_lauren_second_anal_2
        elif lauren.anal_count > 1:
            call lauren_additional_anal from _call_lauren_additional_anal_2
    # error as no lingerie tag identified
    else:
        sys "There's been an error in the lauren_display_lingerie_anal label.  Lauren was not identified as having an appropriate lingerie tag."
    call lauren_anal_stat_changes from _call_lauren_anal_stat_changes_1
    return

label lauren_punish_bondage_sex_oral:
    $ lauren.blowjob_count += 1
    player.c "Have you been practicing, Lauren?"
    "She looks at you uncertainly for a moment."
    player.c "Your cock sucking skills, Lauren.  Have you been practicing?"
    wt_image cheater_bondage_sex_11
    player.c "Never mind answering, let's get you tied up on your knees and you can show me."
    if lauren.blowjob_count == 2:
        wt_image cheater_bondage_sex_18
        call lauren_second_blowjob from _call_lauren_second_blowjob_7
        wt_image cheater_bondage_sex_22
        player.c "Now you can go back to sucking my cock."
        wt_image cheater_bondage_sex_16
        player.c "Keep my balls warm with your hand as you blow me."
    elif lauren.blowjob_count == 3:
        wt_image cheater_bondage_sex_22
        "Lauren takes your balls in her hand ..."
        wt_image cheater_ball_lick_1
        "... then puts them in her mouth to warm them up ..."
        wt_image cheater_bondage_sex_14
        "... before shifting attention to your cock."
        wt_image cheater_bondage_sex_16
        call lauren_third_blowjob from _call_lauren_third_blowjob_7
    elif lauren.blowjob_count == 4:
        wt_image cheater_bondage_sex_22
        "Lauren seems to have mastered her training."
        wt_image cheater_ball_lick_1
        "She warms up your balls nicely ..."
        wt_image cheater_bondage_sex_23
        "... then continues to play with them as she sucks your cock."
        wt_image cheater_bondage_sex_17
        call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_8
    else:
        wt_image cheater_bondage_sex_22
        "Lauren blows you exactly the way you trained her."
        wt_image cheater_ball_lick_1
        "She licks and suckles your balls first ..."
        wt_image cheater_bondage_sex_23
        "... then continues to play with them as she sucks your cock."
    wt_image cheater_bondage_sex_23
    "You relax and enjoy the rest of the blowjob ..."
    wt_image cheater_bondage_sex_12
    "... as she uses her mouth ..."
    wt_image cheater_bondage_sex_14
    "... tongue ..."
    wt_image cheater_bondage_sex_19
    "... lips ..."
    wt_image cheater_bondage_sex_17
    "... and hand to get you ready."
    wt_image cheater_bondage_sex_18
    $ title = "Where do you want to cum?"
    menu:
        "In her mouth":
            wt_image cheater_bondage_sex_16
            "You hold her head in place as you unload your cum down the back of her throat."
            player.c "[player.orgasm_text]"
            if lauren.blowjob_count > 3:
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_5
            wt_image cheater_bondage_sex_15
            player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
        "On her face" if lauren.blowjob_count > 3:
            add tags 'facial_today' to lauren
            if lauren.facial_count == 1:
                wt_image cheater_bondage_sex_15
                "Lauren looks up in surprise as you pull your cock out of her mouth ..."
                wt_image cheater_bondage_sex_24
                "... then quickly closes her eyes as she realizes what you're doing."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                wt_image cheater_facial_4
                player.c "Clean yourself up, slut, then go home."
            elif lauren.facial_count == 2:
                wt_image cheater_bondage_sex_24
                "As you pull out of her mouth, Lauren knows what to expect."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                wt_image cheater_facial_4
                player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                wt_image cheater_facial_2
                lauren.c "You can't expect me to go home like this?"
                player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                lauren.c "Yes"
            else:
                wt_image cheater_bondage_sex_25
                "As you pull out of her mouth, Lauren opens her mouth wide while offering her face as a target."
                wt_image cheater_facial_1
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_5
                "She doesn't try to clean herself this time."
                wt_image cheater_facial_6
                "She does, however, clean off the tip of your cock as she looks up at you."
                wt_image cheater_facial_3
                "You leave her like that for a while, licking your cock and wearing your cum as she kneels on your floor, waiting to be dismissed and sent home to her husband."
            add tags 'facial_today' to lauren
    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_11
    orgasm
    change player energy by -energy_long notify
    return

label lauren_punish_bondage_sex_fuck:
    # first sex scene
    if lauren.sex_count == 0:
        if lauren.test('desire', 30) or lauren.test('resistance', 40):
            $ lauren.sex_count += 1
            wt_image cheater_punishment_1_1
            lauren.c "No, wait ... my husband ..."
            player.c "Your husband told me I'm free to use you however I want. He wants an obedient slut who spreads her legs on command, and that's what you're going to become."
            wt_image cheater_bondage_sex_26
            "Whether it's because you've worn down her resistance to your instructions, or she secretly just wants to feel you inside her, her protests stop and she let's you tie her and roll her onto her back."
            wt_image cheater_bondage_sex_4
            "She looks away as you spread her pussy lips ..."
            wt_image cheater_bondage_sex_27
            "... then cries out as you enter her.  She's been dreading this, dreading what it makes her: a woman who'll fuck other men on her husband's instructions."
            lauren.c "Ohhh"
            $ title = "How do you want to fuck her?"
            menu:
                "Make it pleasurable for her":
                    wt_image cheater_bondage_sex_28
                    "Recognizing her resistance, you take your time with her, going slowly and letting her body get used to the feel of you inside her."
                    "At heart, she's a woman who loves sex.  Watching her carefully, you explore her body to discover what she responds to, and are eventually rewarded with a moan."
                    lauren.c "ooooo"
                    wt_image cheater_bondage_sex_5
                    "As the lubrication between her legs increases, you can fuck her faster and faster to the sound of her growing stimulation."
                    lauren.c "ooooo ... ooooooo"
                    "She won't cum today, but she doesn't have to.  She's enjoyed it, and she knows you know she's enjoyed it."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_bondage_sex_27
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_bondage_sex_28
                        "On her":
                            wt_image cheater_cum_2
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_cum_3
                    add tags 'pleasurable_fuck_today' to lauren
                "Make it rough":
                    "There's no point in pretending this is something it isn't.  She's a fuck toy for your use.  She knows it and you know it."
                    wt_image cheater_bondage_sex_29
                    "So you use her as exactly that.  You're not so rough as to really hurt her, but it's uncomfortable for her, and you don't bother with any lubrication."
                    "If she's going to be ready for her husband on his terms, she needs to accept her role as fuck toy and learn how to get into the right head space to take this type of fucking on demand."
                    wt_image cheater_bondage_sex_6
                    "Even if she's tied up and getting fucked hard into a pretzel shape."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_bondage_sex_27
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_bondage_sex_29
                        "On her":
                            wt_image cheater_cum_2
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_cum_3
                    add tags 'rough_fuck_today' to lauren
            "There'll be no more protests when you tell her it's time to fuck."
            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_7
            orgasm
        # failed attempt
        else:
            wt_image cheater_punishment_1_1
            lauren.c "No, wait ... I'm not going to have sex with you.  I don't care what my husband thinks."
            "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off."
            if is_weekend():
                jump menu_lauren_weekend_discipline_2
            else:
                jump menu_lauren_punish_1
    # subsequent sex scenes
    elif lauren.sex_count >= 1:
        $ lauren.sex_count += 1
        # second sex scene
        if lauren.sex_count == 2:
            wt_image cheater_bondage_sex_31
            player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
            wt_image cheater_bondage_sex_32
            player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
            wt_image cheater_bondage_sex_30
            player.c "Get up on here and show me what you can do with your cunt, slut."
            wt_image cheater_bondage_sex_33
            player.c "All right then, get to work.  Up and down, use your legs."
            wt_image cheater_bondage_sex_34
            player.c "Right up to the tip on your way up."
            wt_image cheater_bondage_sex_35
            player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
            wt_image cheater_bondage_sex_36
            player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
            wt_image cheater_bondage_sex_37
            player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
            wt_image cheater_bondage_sex_34
            "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
            if lauren.test('desire', 60):
                wt_image cheater_bondage_sex_38
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                lauren.c "oooooo"
                wt_image cheater_bondage_sex_39
                "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_bondage_sex_36
                player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_22
            wt_image cheater_bondage_sex_35
            "When she's learned as much as she's going to learn today, you let yourself cum."
            wt_image cheater_bondage_sex_38
            player.c "[player.orgasm_text]"
            lauren.c "Oh!"
            wt_image cheater_bondage_sex_33
            player.c "Remember to practice your lessons at home, slut.  Once your legs have recovered from the workout."
        # third sex scene
        elif lauren.sex_count == 3:
            player.c "Let's see if you're getting any better at fucking, Lauren."
            wt_image cheater_bondage_sex_40
            "You tie her face down, ass up and use ropes to limit the movement of her hips."
            player.c "You're not going to be able to move very much in this position, so you'll need to rock your hips and squeeze my cock with your cunt to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, don't you slut?"
            "Lauren nods."
            wt_image cheater_bondage_sex_41
            player.c "Good.  Then get at it."
            lauren.c "Oh!"
            "You hold yourself and her in place and watch her as she struggles to pleasure your cock with the limited range of movement you give her."
            if lauren.test('desire', 30):
                wt_image cheater_bondage_sex_8
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                lauren.c "ooooo"
                wt_image cheater_bondage_sex_42
                "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_bondage_sex_41
                player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_23
            wt_image cheater_bondage_sex_8
            "Eventually she succeeds in her appointed task, and you feel your orgasm building."
            wt_image cheater_cum_1
            "You release the ropes, flip her over and let your cum spurt on to her pussy and inner thighs."
            player.c "[player.orgasm_text]"
            wt_image cheater_sex_8
            "As she reaches a finger down to wipe it away, you stop her."
            player.c "Don't touch that.  Put your dress back on and be careful not to let any of the material soak up my cum.  You're going home like this."
            wt_image cheater_cum_3
            lauren.c "It'll drip down my legs!"
            player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
        # additional sex scene
        else:
            $ title = "How do you want to fuck her?"
            menu:
                "Rough":
                    wt_image cheater_bondage_sex_26
                    "Roughly you tie Lauren up and toss her on the bed."
                    wt_image cheater_bondage_sex_27
                    lauren.c "Ow!"
                    player.c "Just because I'm on top, slut, doesn't mean you don't have work to do.  Start moving those hips."
                    wt_image cheater_bondage_sex_29
                    "She gets wet now when you enter her, even when you're being rough, and is soon wiggling and rocking her hips back against you."
                    "She fucks you as best she can with the limited range of motion you allow her.  There's not enough stimulus on her clit in this position for her to cum, but her pleasure isn't the point anyway."
                    wt_image cheater_bondage_sex_6
                    "Her role is to be a cum receptacle, and she does a fine job at that."
                    wt_image cheater_bondage_sex_5
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_punishment_1_2
                    "Once she's finished serving her role, you send her home, carrying your jizz inside her."
                    add tags 'rough_fuck_today' to lauren
                "Gently":
                    wt_image cheater_bondage_sex_4
                    "You tie Lauren up and place her on her back, gently spreading her pussy lips with your fingers as she moans."
                    lauren.c "oooo"
                    player.c "Give me a good fuck this time, little slut."
                    wt_image cheater_bondage_sex_28
                    "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you.  It feels nice for you, and it feels nice to her, too."
                    if lauren.test('desire', 60):
                        wt_image cheater_bondage_sex_4
                        "The feeling of your cock inside her and your body against her soon triggers a response."
                        wt_image cheater_bondage_sex_27
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_bondage_sex_5
                        player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_24
                    wt_image cheater_bondage_sex_5
                    "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                    wt_image cheater_bondage_sex_28
                    "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                    wt_image cheater_bondage_sex_27
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_bondage_sex_5
                    "You hold her there until your balls finish pumping their load into her well fucked pussy."
                    wt_image cheater_punishment_1_2
                    "She seems comfortable heading home, carrying your load inside her."
                    add tags 'pleasurable_fuck_today' to lauren
                "Her on top":
                    wt_image cheater_bondage_sex_32
                    "You turn Lauren around ..."
                    wt_image cheater_bondage_sex_30
                    "... and lift her up to place her on top of you."
                    wt_image cheater_bondage_sex_33
                    "You don't need to tell her what to do this time."
                    wt_image cheater_bondage_sex_37
                    "She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                    if lauren.test('desire', 60):
                        wt_image cheater_bondage_sex_38
                        "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                        lauren.c "ooooo"
                        wt_image cheater_bondage_sex_39
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_posing_1_73
                        wt_image cheater_bondage_sex_33
                        player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_25
                    wt_image cheater_bondage_sex_34
                    "With an ever increasing pace she rides your cock, up to the tip ..."
                    wt_image cheater_bondage_sex_35
                    "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                    wt_image cheater_bondage_sex_37
                    "You make her work for it as long as you can ..."
                    wt_image cheater_bondage_sex_35
                    "... but you can only hold out so long under this treatment."
                    wt_image cheater_bondage_sex_38
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_bondage_sex_35
                    "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                    wt_image cheater_punishment_1_2
                    "She seems comfortable heading home, carrying your load inside her."
                    add tags 'ride_fuck_today' to lauren
        call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_8
        orgasm
        change player energy by -energy_long notify
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_punish_bondage_sex_anal:
    if lauren.anal_count == 0:
        wt_image cheater_bondage_sex_40
        "As you tie Lauren on her knees, she thinks you're going to take her vaginally from behind.  She's surprised to see you put the lubricant on your cock, but she's not really wet yet and just assumes you're trying to go easy on her poor pussy."
        wt_image cheater_bondage_sex_43
        "It's only when you place the tip of your cock against her anus that she realizes your true intention."
        # note: the following duplicates the content normally included in lauren_anal_question, but with different images and associated text changes
        lauren.c "No!  Stop ... don't do that."
        player.c "Why not?"
        lauren.c "I've never done that."
        player.c "Really?  Your husband never asked?"
        lauren.c "Once, a long time ago.  But it's not something I want to try.  And he hasn't asked me since.  It isn't something he wants from me."
        player.c "When your husband sent you to me, he said he wanted you trained to be his perfect little fuck toy.  He didn't say make her a perfect little fuck toy but don't bother with the anal."
        lauren.c "I swear, he doesn't care about anal.  He really doesn't."
        player.c "Every man wants to fuck his wife's ass, Lauren. Maybe he just didn't want to push this. Things have changed, though, haven't they? You want to please him, don't you? Isn't that why you're here?"
        "She nods and starts to sob softly."
        lauren.c "Yes, but can't we do other things?  I can please him in so many different ways.  Does it have to be this?"
        "Her resistance on this topic is different than her past objections.  She seems truly distraught at the prospect of taking your cock in her ass.  If you relent, it may increase her trust in you."
        "On the other hand, there may be no better way to break down the mental barriers that prevent her from seeing herself as a happy obedient slut than to push through and past this taboo."
        "Her resistance to you will have to be quite low to accept anal considering how strongly she feels on this topic.  Gifting a butt plug to her would help."
        "If her resistance isn't low enough, it may be better to wait, because if you insist and she balks, her trust will be gone.  She might even call an end to this arrangement."
        $ title = "What do you do?"
        menu:
            "Relent and accept anal as limit for her":
                add tags 'no_anal' to lauren
                player.c "Very well. I'll accept that anal is a limit for you. You realize, however, that means you're going to have to work even harder in every other way to make up for the pleasure he's not getting from your ass."
                change lauren desire by 10
                change lauren resistance by -10
                lauren.c "Yes.  Yes, I understand.  Thank you."
                wt_image cheater_happy_2
                "She's as happy as you've seen her, pleased that you were willing to allow her at least one limit.  She seems ready to do something else with you, if you want."
                if is_weekend():
                    jump menu_lauren_weekend_discipline_2
                else:
                    jump menu_lauren_punish_bondage_sex_1
            "Wait":
                player.c "We'll discuss this again later."
                wt_image cheater_punishment_1_1
                "Lauren is silent as you untie.  Clearly this is not something she wants to discuss again, ever.  However, she seems ready to do something else with you, if you want."
                add tags 'anal_postponed_today' to lauren
                if is_weekend():
                    jump menu_lauren_weekend_discipline_2
                else:
                    jump menu_lauren_punish_bondage_sex_1
            "Insist on anal now":
                player.c "Yes, slut, it has to be this. Your husband wants you to be his personal little whore. That includes being his asswhore."
                "Now relax. This won't hurt as much as you're afraid it will.  You may even grow to enjoy it."
                if butt_plug in lauren.items:
                    $ lauren.open_temp_group('Gifted Butt Plug', duration = 1, duration_unit = 'check')
                    $ lauren.add_temp_mod('resistance', -20, with_message = False)
                    $ lauren.close_temp_group(with_notify = False)
                if lauren.test('resistance', 25):
                    add tags 'accepts_anal' to lauren
                    $ lauren.anal_count += 1
                    wt_image cheater_bondage_sex_44
                    lauren.c "No. Please."
                    "Her voice is no more than a whimper as she feels the head of your cock pressing against her anus."
                    player.c "That's the wrong response, slut.  I'm going to fuck you in the ass and you're going to accept that.  Do you understand?"
                    "Tears start to fall down her face as she nods quietly."
                    player.c "Say it, slut.  Say that I can fuck you in the ass."
                    "She takes two deep breathes before she responds, even more quietly than before."
                    "{size=-5}Yes.  You can fuck me in the ass.{/size}"
                    wt_image cheater_bondage_sex_45
                    "You're not as gentle as you could have been, but having won her surrender, there's no need to be gracious in victory.  She screams as you push yourself into her."
                    lauren.c "OWWW!!!!"
                    "You can take it more slowly next time, work yourself in more gradually, and give her a chance to potentially enjoy the sensation."
                    wt_image cheater_bondage_sex_10
                    "That's for next time.  This time is isn't about enjoyment.  It's about conquest.  You conquering her, her conquering her inhibitions and accepting her new life."
                    player.c "You're an asswhore now, aren't you slut?"
                    "Meekly, she nods."
                    player.c "Say it."
                    lauren.c "I'm an asswhore!"
                    player.c "Good girl."
                    wt_image cheater_bondage_sex_46
                    player.c "[player.orgasm_text]"
                    orgasm
                    wt_image cheater_punishment_1_8
                    "When you're finished, she's unusually quiet getting ready to go home, lost in her own thoughts. Will she tell her husband tonight what she did with you?"
                    wt_image cheater_initial_1
                    "You'll let her decide for today.  You'll send him home the evidence after your next session, once she's had a chance to get used to the idea of her new availability."
                elif lauren.test('resistance', 35) or lauren.has_tag('love_potion_used'):
                    wt_image cheater_bondage_sex_44
                    lauren.c "Noooo!!!!  I said no, and I meant it."
                    change lauren resistance by 10
                    change lauren sos by -5
                    "If you let her up now, not all may be lost.  If you push it, it'll be rape.  You suspect Lauren won't hesitate to go to the cops, and she'll be a credible witness."
                    $ title = "What do you do?"
                    menu:
                        "Untie her":
                            wt_image cheater_punishment_1_1
                            "Lauren's angry as you untie her, but she's not ready to call things off just yet."
                            wt_image cheater_initial_1
                            "That's it for tonight, however.  You send her home, unhappy.  She knows she's failed in your eyes, and in her eyes, you have too."
                            change player energy by -energy_short notify
                        "Anally rape her":
                            call lauren_punish_bondage_sex_anal_rape from _call_lauren_punish_bondage_sex_anal_rape
                else:
                    wt_image cheater_bondage_sex_44
                    lauren.c "Noooo!!!!  I said no, and I meant it."
                    $ office_tower.remove_connection(lauren_office)
                    $ office_tower.remove_action(office_tower.action_visit_lauren)
                    rem tags 'trained_this_week' from lauren # So she won't pay us this session
                    add tags 'failed_training' to lauren
                    call convert(lauren, 'unsatisfied', True, True) from _call_convert_149
                    "Lauren's really angry.  If you let her up now, not all may be lost.  If you push it, it'll be rape.  You suspect Lauren won't hesitate to go to the cops, and she'll be a credible witness."
                    $ title = "What do you do?"
                    menu:
                        "Untie her":
                            wt_image cheater_resisting_3
                            "Once you've untied her, she grabs up her clothes and runs to the door, stopping only long enough to pull on enough covering to be decent."
                            wt_image current_location.image
                            "Then she's gone.  She won't be answering your calls in the future."
                            change player energy by -energy_short notify
                        "Anally rape her":
                            call lauren_punish_bondage_sex_anal_rape from _call_lauren_punish_bondage_sex_anal_rape_1
    elif lauren.anal_count == 1:
        # note: the following duplicates the content normally included in lauren_second_anal, but with different images and associated text changes
        $ lauren.anal_count += 1
        wt_image cheater_bondage_sex_40
        "Lauren lets you tie her into position, but starts to tremble nervously when she sees you pick up the lubricant."
        wt_image cheater_bondage_sex_43
        player.c "It's okay, little asswhore.  No need to worry about your lack of experience.  I'm going to give you lots of time to learn how to please me with your ass."
        "You stroke your cock, coating it with lubricant. Then you drizzle the lubricant onto her rosebud, a soft gasp escaping her mouth as its coolness lands on her skin."
        lauren.c "Oh!"
        wt_image cheater_bondage_sex_44
        "The coolness of the lubricant is replaced by the warmth of the head of your cock, eliciting a groan."
        lauren.c "Ah!"
        player.c "Time to start your lesson, asswhore.  Work yourself back on to me.  That's it, push back.  Your ass will open itself naturally."
        wt_image cheater_bondage_sex_45
        "With the amount of lubricant you applied, you actually slide into her rather easily.  She gasps again, this time in surprise, as she feels the head of your cock slide pass the anal rim."
        lauren.c "OHHH!"
        wt_image cheater_bondage_sex_10
        player.c "Good.  Now you fuck me just like you do with your cunt when I'm behind you.  Rock your hips back and forth.  Take me deeper inside you with every thrust."
        "It's not a difficult technique, and she gets it easily."
        wt_image cheater_bondage_sex_46
        "It takes some time for her ass to stretch enough to take all of you inside her, and you need to re-apply some lubricant before she can get to that point."
        wt_image cheater_bondage_sex_10
        "Soon after, though, she's fucking her rectum up and down the full length of your cock, her ass slamming back into you hard on every back thrust."
        wt_image cheater_bondage_sex_46
        "When you're satisfied she has the hang of it, you let yourself go.  You hold her hips still, the tip of your cock just barely inside her ass as your balls unload into her."
        player.c "[player.orgasm_text]"
        wt_image cheater_anal_8
        "As you pull out, most of your sperm flows out of her ass and drips down over her pussy."
        player.c "Look over here, asswhore."
        wt_image cheater_anal_4
        "You position her hips so that she can see your cum on her in the mirror."
        player.c "That's what you're taking home tonight.  You're going to show this to your husband and explain how it got there.  Then you're going to let him know that from now on, you're his little asswhore, whenever he wants.  Do you understand?"
        lauren.c "Yes"
        wt_image cheater_punishment_1_2
        player.c "He's going to fuck you in the ass tonight, isn't he?"
        "She nods."
        player.c "Take the lubricant.  He may not use it, but at least you can offer it to him, in case he doesn't want to hurt you too much."
        orgasm
    elif lauren.anal_count > 1:
        # note: the following duplicates the content normally included in lauren_additional_anal, but with different images and associated text changes
        $ lauren.anal_count += 1
        wt_image cheater_bondage_sex_40
        "You tie Lauren into position and lubricate first your cock ..."
        wt_image cheater_bondage_sex_43
        "... then her anus, as you enjoy the sight of the married businesswoman waiting to take your cock in her ass."
        wt_image cheater_bondage_sex_45
        "She gets your full length inside her more easily now, as she's learned to relax and let her body stretch to accommodate you."
        wt_image cheater_bondage_sex_46
        "As she moves her hips back and forth fucking you, you try to stimulate her, flicking your fingers against her clit to see if you can coax an anal orgasm out of her."
        "It's no use.  She just doesn't enjoy anal enough to get excited, even with your fingers playing with her."
        wt_image cheater_bondage_sex_10
        "This is just a service for her, something she provides to please her man, not her.  Which was the point of her training all along."
        wt_image cheater_bondage_sex_45
        "When she's pleased you enough, you thrust forward into her, hard, releasing your seed deep inside her."
        player.c "[player.orgasm_text]"
        wt_image cheater_anal_11
        "She'll feel the cum dripping out of her butt all the way home tonight."
        orgasm
    if lauren.anal_count > 0:
        call lauren_anal_stat_changes from _call_lauren_anal_stat_changes_2
        change player energy by -energy_long notify
    elif lauren.has_tag('anal_postponed_today'):
        rem tags 'anal_postponed_today' from lauren
    return

label lauren_punish_bondage_sex_anal_rape:
    wt_image cheater_bondage_sex_40
    "She may be saying no, but she's in no position to prevent you from doing what you want."
    lauren.c "No!  No!!  No!!!"
    wt_image cheater_bondage_sex_45
    lauren.c "Nooooooo!!!"
    wt_image cheater_bondage_sex_10
    player.c "Yes, Lauren.  You're an asswhore now.  My asswhore."
    "She's silent for the remainder of the rape."
    wt_image cheater_bondage_sex_46
    "She takes the ass-pounding quietly, and doesn't react, even when you fill her bowels with your seed."
    player.c "[player.orgasm_text]"
    wt_image cheater_punishment_1_8
    "She says nothing after you finish and untie her, but you're not fooled."
    wt_image cheater_unhappy_2
    "She can't look at you as she cleans herself up and leaves.  She won't find it easy to tell anyone what happened, either, but you're pretty sure she'll eventually work herself up to that."
    wt_image airport_1
    "Best to be somewhere far away when that happens.  You can always restart in a new country."
    $ lauren.temporary_count = 0
    jump end_game
    return

label lauren_office_oral:
    $ lauren.blowjob_count += 1
    if lauren.blowjob_count == 2:
        call lauren_second_blowjob from _call_lauren_second_blowjob_8
        wt_image cheater_office_2_23
        player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
    elif lauren.blowjob_count == 3:
        wt_image cheater_ball_lick_1
        "Lauren takes your balls into her mouth and warms them up ..."
        wt_image cheater_office_2_23
        "... before shifting attention to your cock."
        call lauren_third_blowjob from _call_lauren_third_blowjob_8
    elif lauren.blowjob_count == 4:
        wt_image cheater_ball_lick_1
        "Lauren seems to have mastered her training."
        wt_image cheater_office_2_23
        "She warms up your balls nicely, then continues to play with them as she sucks your cock."
        call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_9
    else:
        wt_image cheater_ball_lick_1
        "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
        wt_image cheater_office_2_23
        "... then continues to play with them as she sucks your cock."
    wt_image cheater_office_2_24
    "You relax and enjoy the rest of the blowjob ..."
    wt_image cheater_office_2_5
    "... as she uses her hand, mouth, tongue and lips to get you ready."
    wt_image cheater_office_2_23
    $ title = "Where do you want to cum?"
    menu:
        "In her mouth":
            wt_image cheater_office_2_25
            "You place a hand on the top of her head to hold her steady as you unload your cum down the back of her throat."
            player.c "[player.orgasm_text]"
            if lauren.blowjob_count > 3:
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_6
            wt_image cheater_office_2_5
            player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go back to your very important job."
        "On her face" if lauren.blowjob_count > 3:
            add tags 'facial_today' to lauren
            if lauren.facial_count == 1:
                wt_image cheater_facial_1
                "Lauren looks up in surprise as you pull your cock out of her mouth, then quickly closes her eyes as she realizes what you're doing."
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                wt_image cheater_facial_4
                player.c "Clean yourself up, slut, then you can get back to your important job."
            elif lauren.facial_count == 2:
                wt_image cheater_facial_1
                "As you pull out of her mouth, Lauren knows what to expect."
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_2
                "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                wt_image cheater_facial_4
                player.c "No, don't touch your face.  Leave the cum there."
                wt_image cheater_facial_2
                lauren.c "I can't be seen in the office like this!"
                player.c "No, but you can video call your husband and tell him what's on your face. He can decide how long you need to wait to clean up. That's his decision to make. Not yours. Understood?"
                lauren.c "Yes"
            else:
                wt_image cheater_office_2_23
                "As you pull out of her mouth, Lauren strokes your cock while offering her face as a target."
                wt_image cheater_office_2_6
                player.c "[player.orgasm_text]"
                wt_image cheater_facial_5
                "She doesn't try to clean herself this time."
                wt_image cheater_facial_6
                "She does, however, clean off the tip of your cock as she looks up at you."
                wt_image cheater_facial_3
                "You leave her like that for a while, licking your cock and wearing your cum as she kneels on her office floor, waiting to be allowed to return to her work."
            add tags 'facial_today' to lauren
    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_12
    if not lauren.has_tag('office_blowjob'):
        add tags 'office_blowjob' to lauren
        "Being required to give you head in her own office reinforces in Lauren her subservience to you."
        change lauren submission by 5
    orgasm notify
    return

label lauren_office_fuck:
    $ lauren.sex_count += 1
    # second sex scene
    if lauren.sex_count == 2:
        player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
        player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
        player.c "Get up on here and show me what you can do with your cunt, slut."
        wt_image cheater_office_2_35
        "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
        wt_image cheater_office_2_36
        player.c "All right then, get to work.  Up and down, use your legs."
        wt_image cheater_office_2_12
        player.c "Right up to the tip on your way up."
        wt_image cheater_office_2_13
        player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
        wt_image cheater_office_2_35
        player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
        wt_image cheater_office_2_37
        player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
        wt_image cheater_office_2_35
        "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
        if lauren.test('desire', 60):
            wt_image cheater_office_2_36
            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
            lauren.c "oooooo"
            wt_image cheater_office_2_38
            "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
            lauren.c "Aaahhhh!!!!"
            wt_image cheater_office_2_35
            player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
            lauren.c "Y ... yes."
            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_26
        wt_image cheater_office_2_12
        "You let her ride you for a little while."
        wt_image cheater_office_2_13
        "When she's learned as much as she's going to learn today, you let yourself cum."
        wt_image cheater_office_2_37
        player.c "[player.orgasm_text]"
        lauren.c "Oh!"
        wt_image cheater_office_2_13
        player.c "You can get dressed and go back to your very important job, slut.  Once your legs have recovered from the workout."
    # third sex scene
    elif lauren.sex_count == 3:
        player.c "Let's see if you're getting any better at fucking."
        wt_image cheater_office_2_39
        "Turn around and get on your knees, slut."
        wt_image cheater_office_2_40
        "You insert just the tip of your cock inside her."
        lauren.c "Oh!"
        wt_image cheater_office_2_14
        player.c "That's as much as I'm doing. You're doing the rest of the work."
        player.c  "You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
        "Lauren nods."
        player.c "Good.  Then get at it."
        wt_image cheater_office_2_40
        "You don't say anything more.  You just hold yourself in place on the table and watch her as she struggles to pleasure your cock within the limited range of movement you give her."
        if lauren.test('desire', 60):
            wt_image cheater_office_2_14
            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
            lauren.c "oooooo"
            wt_image cheater_office_2_41
            "*smack*"
            lauren.c "Ow!"
            player.c "Focus on my pleasure, slut."
            lauren.c "Y ... yesss ... oooooo"
            wt_image cheater_office_2_45
            "Despite your admonishment, the sensations are too much.   Quick and intense, the orgasm rips through her.  She lets out a moan as her body shudders around your cock."
            lauren.c "Aaahhhh!!!!"
            wt_image cheater_office_2_41
            "*smack*"
            lauren.c "Ow!"
            player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
            lauren.c "Y ... yes."
            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_27
        wt_image cheater_office_2_14
        "Eventually she succeeds in her appointed task, and you feel your orgasm building."
        wt_image cheater_office_2_42
        "You pull yourself out of her and flip her over ..."
        wt_image cheater_cum_2
        "... and let your cum spurt over her belly and pussy."
        player.c "[player.orgasm_text]"
        wt_image cheater_sex_8
        "As she reaches a finger down to wipe it away, you stop her."
        wt_image cheater_cum_3
        player.c "Don't touch that.  Put your business suit back on and be careful not to let any of the material soak up my cum.  You're going to pay your husband a surprise mid-day visit."
        wt_image cheater_office_2_39
        lauren.c "It'll drip down my legs!"
        wt_image cheater_office_2_29
        player.c "Yes, it will.  Get to your husband quick and show him what a mess you are under your skirt.  He can decide what to do with you."
    # additional sex scene
    else:
        $ title = "How do you want to fuck her?"
        menu:
            "Hard from behind":
                wt_image cheater_office_2_39
                "Turn around and get on your knees, slut."
                wt_image cheater_office_2_40
                "Roughly you shove yourself inside her."
                lauren.c "Ow!"
                player.c "Just because I'm behind you, slut, doesn't mean you don't have work to do.  Start moving those hips."
                wt_image cheater_office_2_14
                "She gets wet now when you enter her, even when you're being rough, and is soon wiggling and rocking her hips back against you."
                wt_image cheater_office_2_40
                "She fucks you as best she can with the limited range of motion you allow her."
                wt_image cheater_office_2_41
                "You don't make this enjoyable enough for her to cum ... *smack*  *smack*  *smack*"
                wt_image cheater_office_2_45
                lauren.c "Ow!"
                wt_image cheater_office_2_41
                player.c "Fuck me, slut.  Harder.  Faster."
                wt_image cheater_office_2_14
                "Her pleasure isn't the point anyway.  Her role is to be a cum receptacle, and she does a fine job at that."
                wt_image cheater_office_2_15
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                wt_image cheater_office_2_29
                "Once she's finished serving her role, you have her dress and get back to work, carrying your jizz inside her."
                add tags 'rough_fuck_today' to lauren
            "Gently on the desk":
                player.c "Lie back and spread your legs."
                wt_image cheater_office_2_42
                "She gets wet just from the realization she's about to be fucked ..."
                wt_image cheater_office_2_43
                "... but she gets a whole lot wetter when you place your mouth between her legs and suckle her."
                lauren.c "Oh!  OH!  ...  ooooooo"
                wt_image cheater_office_2_44
                "Once her juices are flowing freely, you insert just the tip of your cock inside her."
                player.c "Give me a good fuck this time, little slut."
                wt_image cheater_office_2_46
                "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you."
                wt_image cheater_office_2_47
                "It feels nice for you, and it feels nice to her, too."
                lauren.c "oooo"
                if lauren.test('desire', 60):
                    wt_image cheater_office_2_48
                    "The feeling of your cock inside her and your body against her soon triggers a response."
                    lauren.c "oooooo"
                    wt_image cheater_office_2_49
                    "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_office_2_47
                    player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_28
                wt_image cheater_office_2_46
                "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                wt_image cheater_office_2_44
                "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                wt_image cheater_office_2_48
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                "You hold her there until your balls finish pumping their load into her well fucked pussy."
                wt_image cheater_office_2_50
                "She seems comfortable going back to work, carrying your load inside her."
                add tags 'pleasurable_fuck_today' to lauren
            "Her on top":
                wt_image cheater_office_2_35
                "You pull Lauren on top of you, guiding her onto your hard pole."
                wt_image cheater_office_2_36
                "You don't need to tell her what to do this time.  She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                if lauren.test('desire', 60):
                    wt_image cheater_office_2_35
                    "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                    lauren.c "ooooo"
                    wt_image cheater_office_2_38
                    "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_29
                wt_image cheater_office_2_12
                "With an ever increasing pace she rides your cock, up to the tip ..."
                wt_image cheater_office_2_13
                "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                wt_image cheater_office_2_12
                "You make her work for it as long as you can ..."
                wt_image cheater_office_2_13
                "... but you can only hold out so long under this treatment."
                wt_image cheater_office_2_37
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                wt_image cheater_office_2_50
                "She seems comfortable going back to work, carrying your load inside her."
                add tags 'ride_fuck_today' to lauren
    call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_9
    if not lauren.has_tag('office_sex'):
        add tags 'office_sex' to lauren
        "Being unable to refuse you sex, even at her place of work, reinforces in Lauren her inability to say 'no' to you."
        change lauren resistance by -5
    orgasm notify
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_weekend_dildo_fuck:
    # note: only get to here if already had at least two sex scenes with Lauren
    $ lauren.sex_count += 1
    player.c "Lucky for you, I'm in the mood to find out what your cunt has learned today."
    wt_image cheater_sex_31
    "Her legs are so tired from riding the dildo, she can barely hold herself up.  You take pity on her, and lay her on her side as you push yourself in."
    lauren.c "Oh!"
    # third sex scene
    if lauren.sex_count == 3:
        wt_image cheater_sex_32
        player.c "I know you're tired, but you don't let that interfere with pleasuring me.  I may be behind you, but you're going to do all the work.  You're not going to be able to move very much with me holding you in place. You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
        "Lauren nods."
        wt_image cheater_sex_34
        player.c "Good.  Then get at it."
        "You don't say anything more. You just hold yourself and her in place and watch her as she struggles to pleasure your cock within the limited range of movement you give her."
        wt_image cheater_sex_32
        "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
        lauren.c "oooooo"
        wt_image cheater_sex_33
        "As sensitive as she is after the toy play, she soon climaxes."
        lauren.c "Aaaggghhhh!!"
        wt_image cheater_sex_11
        "She leans back and nuzzles into you after her orgasm, a rare show of tender affection towards you as she continues to milk your cock with her cunt."
        wt_image cheater_sex_34
        "Eventually she succeeds in her appointed task, and you feel your orgasm building."
        wt_image cheater_cum_2
        "You pull yourself out of her and let your cum spurt over her belly and pussy."
        player.c "[player.orgasm_text]"
        wt_image cheater_sex_8
        "As she reaches a finger down to wipe it away, you stop her."
        player.c "Don't touch that.  Put your dress back on and be careful not to let any of the material soak up my cum.  You're going home like this."
        wt_image cheater_cum_3
        lauren.c "It'll drip down my legs!"
        wt_image cheater_weekend_dildo_23
        player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
    # additional sex scenes
    else:
        wt_image cheater_sex_32
        "As tired as her cunt is, she tries her hardest to milk your cock as you thrust steadily into her."
        lauren.c "oooooo"
        wt_image cheater_sex_33
        "As sensitive as she is after the toy play, it doesn't take long for her to climax."
        lauren.c "Aaaggghhhh!!"
        wt_image cheater_sex_11
        "She leans back and nuzzles into you after her orgasm, a rare show of tender affection towards you as she continues to milk your cock with her cunt."
        wt_image cheater_sex_34
        "She seems genuinely happy when you cum a few minutes later, unloading your sperm into her sore pussy."
        player.c "[player.orgasm_text]"
        wt_image cheater_weekend_dildo_41
        "She seems comfortable heading home, carrying your load inside her."
        add tags 'pleasurable_fuck_today' to lauren
    orgasm
    call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_10
    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_30
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_weekend_maid_oral:
    $ lauren.blowjob_count += 1
    player.c "Have you been practicing, Lauren?"
    wt_image cheater_weekend_maid_40
    "She looks at you uncertainly for a moment."
    wt_image cheater_weekend_maid_7
    player.c "Your cock sucking skills, Lauren.  Have you been practicing?  Never mind answering, just get on your knees and show me."
    if lauren.blowjob_count == 2:
        wt_image cheater_weekend_maid_36
        call lauren_second_blowjob from _call_lauren_second_blowjob_9
        wt_image cheater_weekend_maid_41
        player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
    elif lauren.blowjob_count == 3:
        wt_image cheater_ball_lick_1
        "Lauren takes your balls into her mouth and warms them up ..."
        wt_image cheater_weekend_maid_41
        "... before shifting attention to your cock."
        wt_image cheater_weekend_maid_15
        call lauren_third_blowjob from _call_lauren_third_blowjob_9
    elif lauren.blowjob_count == 4:
        wt_image cheater_ball_lick_1
        "Lauren seems to have mastered her training."
        wt_image cheater_weekend_maid_41
        "She warms up your balls nicely, then continues to play with them as she sucks your cock."
        wt_image cheater_weekend_maid_15
        call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_10
    else:
        wt_image cheater_ball_lick_1
        "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
        wt_image cheater_weekend_maid_41
        "... then continues to play with them as she sucks your cock."
    wt_image cheater_weekend_maid_15
    "You relax and enjoy the rest of the blowjob ..."
    wt_image cheater_weekend_maid_13
    "... as she uses her tongue ..."
    wt_image cheater_weekend_maid_36
    "... and mouth to get you ready."
    wt_image cheater_weekend_maid_41
    $ title = "Where do you want to cum?"
    menu:
        "In her mouth":
            wt_image cheater_weekend_maid_38
            "She wraps her lips rightly around your cock as you unload your cum down the back of her throat."
            player.c "[player.orgasm_text]"
            if lauren.blowjob_count > 3:
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_7
            wt_image cheater_weekend_maid_39
            player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go home."
        "On her face" if lauren.blowjob_count > 3:
            add tags 'facial_today' to lauren
            if lauren.facial_count == 1:
                wt_image cheater_weekend_maid_13
                "Lauren looks up in surprise as you pull your cock out of her mouth, then turns her head as she realizes what you're doing."
                wt_image cheater_weekend_maid_42
                player.c "[player.orgasm_text]"
                wt_image cheater_weekend_maid_43
                "Silently she waits as your cum drips down her face.  You've taken her far enough for now."
                player.c "Clean yourself up, slut, then go home."
            elif lauren.facial_count == 2:
                wt_image cheater_weekend_maid_13
                "As you pull out of her mouth, Lauren knows what to expect."
                wt_image cheater_weekend_maid_42
                player.c "[player.orgasm_text]"
                wt_image cheater_weekend_maid_43
                "As the cum drips down her chin, she waits for you to let her clean up.  She's in for a new surprise."
                wt_image cheater_weekend_maid_16
                player.c "Get yourself dressed and go home,slut.  No, don't touch your face.  Leave the cum there."
                wt_image cheater_weekend_maid_43
                lauren.c "You can't expect me to go home like this?"
                player.c "That's exactly what I expect. When you get home you'll tell your husband what's on your face. He may let you clean up. He may decide to deposit his own load on you. That'll be his decision to make. Not yours. Understood?"
                lauren.c "Yes"
            else:
                wt_image cheater_weekend_maid_39
                "As you pull out of her mouth, Lauren licks the underside of your cock while offering her face as a target."
                wt_image cheater_weekend_maid_42
                player.c "[player.orgasm_text]"
                wt_image cheater_weekend_maid_43
                "She doesn't try to clean herself this time."
                wt_image cheater_weekend_maid_44
                "She does, however, clean off the tip of your cock as she looks up at you."
                "You leave her like that for a while, licking your cock and wearing your cum as she kneels on your floor, waiting to be dismissed and sent home to her husband."
            add tags 'facial_today' to lauren
    call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_13
    orgasm
    return

label lauren_weekend_maid_fuck:
    # first sex scene
    if lauren.sex_count == 0:
        if lauren.test('desire', 30) or lauren.test('resistance', 40):
            $ lauren.sex_count += 1
            wt_image cheater_weekend_maid_45
            lauren.c "No, wait ... my husband ..."
            player.c "Your husband told me I'm free to use you however I want. He wants an obedient slut who spreads her legs on command, and that's what you're going to become. Now open yourself up and show me what a good little slut you can be."
            wt_image cheater_weekend_maid_17
            "Whether it's because you've worn down her resistance to your instructions, or she secretly just wants to feel you inside her, her protests stop.  She cringes slightly as you push inside her, but holds your gaze."
            "She's been dreading this, dreading what it makes her: a woman who'll fuck other men on her husband's instructions."
            $ title = "How do you want to fuck her?"
            menu:
                "Make it pleasurable for her":
                    wt_image cheater_weekend_maid_46
                    "Recognizing her resistance, you take your time with her, going slowly and letting her body get used to the feel of you inside her."
                    wt_image cheater_weekend_maid_19
                    "At heart, she's a woman who loves sex.  Watching her carefully, you explore her body to discover what she responds to, and are eventually rewarded with a moan."
                    lauren.c "ooooo"
                    wt_image cheater_weekend_maid_47
                    "As the lubrication between her legs increases, you can fuck her faster and faster to the sound of her growing stimulation.  She even rubs her clit as you fuck her."
                    lauren.c "ooooo ... ooooooo"
                    wt_image cheater_weekend_maid_19
                    "She won't cum today, but she doesn't have to.  She's enjoyed it, and she knows you know she's enjoyed it."
                    wt_image cheater_weekend_maid_48
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    add tags 'pleasurable_fuck_today' to lauren
                "Make it rough":
                    wt_image cheater_weekend_maid_50
                    "There's no point in pretending this is something it isn't.  She's a fuck toy for your use.  She knows it and you know it."
                    wt_image cheater_weekend_maid_49
                    "So you use her as exactly that.  You're not so rough as to really hurt her, but it's uncomfortable for her, and you don't bother with any lubrication."
                    wt_image cheater_weekend_maid_20
                    "If she's going to be ready for her husband on his terms, she needs to accept her role as fuck toy and learn how to get herself into the right head space to take this type of fucking on demand."
                    wt_image cheater_weekend_maid_18
                    "Her squeezing her legs together to apply pressure to her clit tells you she understands this. It's doesn't get her anywhere close to climax, but that plus the feel of your cock inside her is enough to get her wet."
                    wt_image cheater_weekend_maid_51
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    add tags 'rough_fuck_today' to lauren
            wt_image cheater_weekend_maid_45
            "There'll be no more protests when you tell her it's time to fuck."
            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_11
            orgasm
        # failed attempt
        else:
            wt_image cheater_resisting_6
            lauren.c "No.  I'm not going to have sex with you.  I don't care what my husband thinks."
            "You either need to reduce her resistance or raise her desire before Lauren will consent to sex with you. If you try to push this now, she's going to call the whole arrangement off."
            jump menu_lauren_weekend_maid_1
    # subsequent sex scenes
    elif lauren.sex_count >= 1:
        $ lauren.sex_count += 1
        # second sex scene
        if lauren.sex_count == 2:
            player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
            wt_image cheater_weekend_maid_53
            player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
            wt_image cheater_weekend_maid_52
            player.c "Get up on here and show me what you can do with your cunt, slut."
            wt_image cheater_weekend_maid_22
            player.c "All right then, get to work.  Up and down, use your legs."
            wt_image cheater_weekend_maid_21
            player.c "Right up to the tip on your way up."
            wt_image cheater_weekend_maid_54
            player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
            wt_image cheater_weekend_maid_55
            player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
            wt_image cheater_weekend_maid_56
            player.c "If your cunt gets too dry, play with your clit.  You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
            wt_image cheater_weekend_maid_55
            "With your hands on her body, you guide her to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
            if lauren.test('desire', 60):
                wt_image cheater_weekend_maid_57
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her, and your words in her ear triggers a response in her body."
                lauren.c "ooooo"
                wt_image cheater_weekend_maid_58
                "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_weekend_maid_55
                player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_31
            wt_image cheater_weekend_maid_54
            "When she's learned as much as she's going to learn today, you let yourself cum."
            player.c "[player.orgasm_text]"
            lauren.c "Oh!"
            wt_image cheater_weekend_maid_45
            player.c "Remember to practice your lessons at home, slut.  Once your legs have recovered from the workout."
        # third sex scene
        elif lauren.sex_count == 3:
            player.c "Let's see if you're getting any better at fucking, Lauren."
            wt_image cheater_weekend_maid_26
            "You position her on her knees in front of you ..."
            wt_image cheater_weekend_maid_59
            "... and insert the head of your cock into her."
            lauren.c "Oh!"
            wt_image cheater_weekend_maid_25
            player.c "I'm going to pin you down and shove myself inside you.  After that, you're going to do the work."
            player.c  "You're not going to be able to move very much with me holding you in place. You'll need to buck your hips and squeeze my cock to milk an orgasm out of me. You know how to use your Kegel muscles to squeeze a cock, slut?"
            wt_image cheater_weekend_maid_24
            "Lauren nods."
            player.c "Good.  Then let's get at it."
            wt_image cheater_weekend_maid_60
            "She groans as you shove yourself inside, impaling her."
            lauren.c "oooo"
            wt_image cheater_weekend_maid_61
            "After that, you just hold yourself in place and watch as she struggles to pleasure your cock within the limited range of movement you give her."
            if lauren.test('desire', 60):
                wt_image cheater_weekend_maid_62
                "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                lauren.c "oooooo"
                wt_image cheater_weekend_maid_63
                "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_weekend_maid_61
                player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                lauren.c "Y ... yes."
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_32
            wt_image cheater_weekend_maid_64
            "Eventually she succeeds in her appointed task, and you feel your orgasm building."
            wt_image cheater_cum_2
            "You pull yourself out and flip her over, letting your cum spurt over her belly and pussy."
            player.c "[player.orgasm_text]"
            wt_image cheater_sex_8
            "As she reaches a finger down to wipe it away, you stop her."
            wt_image cheater_cum_3
            player.c "Don't touch that.  Put your uniform back on and be careful not to let any of the material soak up my cum.  You're going home like this."
            wt_image cheater_weekend_maid_65
            lauren.c "It'll drip down my legs!"
            player.c "Yes, it will.  When you get home, you'll show your husband what a mess you are.  He can decide what to do with you."
        # additional sex scene
        else:
            $ title = "How do you want to fuck her?"
            menu:
                "Roughly":
                    wt_image cheater_weekend_maid_49
                    "Roughly you toss Lauren onto her back and shove yourself inside her."
                    lauren.c "Ow!"
                    wt_image cheater_weekend_maid_50
                    "She gets wet now when you enter her, even when you're being rough, and is soon wiggling and rocking her hips back against you."
                    wt_image cheater_weekend_maid_18
                    "She fucks you as best she can with the limited range of motion you allow her.  There's not enough stimulus on her clit in this position for her to cum, but her pleasure isn't the point anyway."
                    wt_image cheater_weekend_maid_51
                    "Her role is to be a cum receptacle, and she does a fine job at that."
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_weekend_maid_65
                    "Once she's finished serving her role, you send her home, carrying your jizz inside her."
                    add tags 'rough_fuck_today' to lauren
                "Gently":
                    wt_image cheater_weekend_maid_17
                    "You lay Lauren on her back and spread her legs, inserting just the tip of your cock inside her."
                    player.c "Give me a good fuck this time, little slut."
                    wt_image cheater_weekend_maid_19
                    "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you. It feels nice for you, and it feels nice to her, too."
                    if lauren.test('desire', 60):
                        wt_image cheater_weekend_maid_47
                        "The feeling of your cock inside her and your body against her soon triggers a response."
                        lauren.c "ooooooo"
                        wt_image cheater_weekend_maid_46
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        wt_image cheater_weekend_maid_66
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_weekend_maid_19
                        player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_33
                    wt_image cheater_weekend_maid_46
                    "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                    wt_image cheater_weekend_maid_17
                    "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_weekend_maid_48
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_weekend_maid_19
                            "You hold her there until your balls finish pumping their load into her well fucked pussy."
                        "On her":
                            wt_image cheater_cum_1
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_cum_3
                            "She knows better now than to clean it up."
                    wt_image cheater_weekend_maid_35
                    "She seems comfortable bringing home the sticky results of her efforts."
                    add tags 'pleasurable_fuck_today' to lauren
                "Her on top":
                    wt_image cheater_weekend_maid_53
                    "You stand Lauren up ..."
                    wt_image cheater_weekend_maid_52
                    "... and pull her on top of you."
                    wt_image cheater_weekend_maid_54
                    "You don't need to tell her what to do this time.  She immediately starts riding your cock and rocking her hips, remembering your past instructions."
                    if lauren.test('desire', 60):
                        wt_image cheater_weekend_maid_57
                        "Lauren tries very hard to concentrate on your pleasure.  Despite herself, the feeling of your cock inside her and your body against her triggers a response."
                        lauren.c "ooooo"
                        wt_image cheater_weekend_maid_58
                        "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_weekend_maid_54
                        player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                        lauren.c "Y ... yes."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_34
                    wt_image cheater_weekend_maid_52
                    "With an ever increasing pace she rides your cock, up to the tip ..."
                    wt_image cheater_weekend_maid_54
                    "... then down hard to the base, rocking her hips back and forth to increase the stimulation for you."
                    wt_image cheater_weekend_maid_55
                    "You make her work for it as long as you can ..."
                    wt_image cheater_weekend_maid_52
                    "... but you can only hold out so long under this treatment."
                    wt_image cheater_weekend_maid_54
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_weekend_maid_57
                    "You hold her on your lap until your balls finish pumping their load into her well fucked pussy."
                    wt_image cheater_weekend_maid_35
                    "She seems comfortable heading home, carrying your load inside her."
                    add tags 'ride_fuck_today' to lauren
        call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_12
        orgasm
    $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
    return

label lauren_weekend_maid_anal:
    if lauren.anal_count == 0:
        wt_image cheater_weekend_maid_26
        "As you turn Lauren around, she thinks you're going to take her vaginally from behind."
        wt_image cheater_weekend_maid_67
        "She's surprised to see you put the lubricant on your cock, but she's not really wet yet and just assumes you're trying to go easy on her poor pussy."
        wt_image cheater_weekend_maid_68
        "It's only when you place the tip of your cock against her anus that she realizes your true intention."
        call lauren_anal_question from _call_lauren_anal_question_3
        # finishers for anal question
        if lauren.has_tag('no_anal'):
            wt_image cheater_happy_3
            lauren.c "Yes.  Yes, I understand.  Thank you."
            wt_image cheater_weekend_maid_39
            "Unprompted, she drops to her knees and kisses your cock, trying to show you that she can be the obedient slut you and her husband want her to be."
            wt_image cheater_weekend_maid_35
            "She heads home as happy as you've seen her, pleased that you were willing to allow her at least one limit."
        elif lauren.anal_count == 1:
            wt_image cheater_weekend_maid_3
            "When you're finished, she's unusually quiet getting ready to go home, lost in her own thoughts. Will she tell her husband tonight what she did with you? You'll let her decide for today.  You'll send him home the evidence after your next session, once she's had a chance to get used to the idea of her new availability."
        elif lauren.has_tag('failed_training'):
            wt_image cheater_weekend_maid_69
            "Lauren twists out from underneath you and stands up."
            wt_image cheater_weekend_maid_3
            "She grabs up her clothes and runs to the door, stopping only long enough to pull on enough covering to be decent."
            wt_image current_location.image
            "Then she's gone.  She won't be answering your calls in the future."
        elif lauren.has_tag('anal_postponed_today'):
            rem tags 'anal_postponed_today' from lauren
        else:
            wt_image cheater_weekend_maid_69
            "Lauren twists out from underneath you and stands up.  She's angry, but it seems she's not ready to call things off just yet."
            wt_image cheater_weekend_maid_3
            "That's it for today, however.  You send her home, unhappy.  She knows she's failed in your eyes, and in her eyes, you have too."
    elif lauren.anal_count == 1:
        wt_image cheater_weekend_maid_40
        call lauren_second_anal from _call_lauren_second_anal_3
    elif lauren.anal_count > 1:
        call lauren_additional_anal from _call_lauren_additional_anal_3
    call lauren_anal_stat_changes from _call_lauren_anal_stat_changes_3
    return

label lauren_continuing_oral:
    $ lauren.blowjob_count += 1
    if lauren.blowjob_count == 1:
        player.c "How'd we get this far without you sucking my cock yet, slut?  Show me what you know about giving head."
        wt_image cheater_continuing_5
        "Lauren pulls off her pants, drops to her knees and takes out your cock.  She looks up at you as she strokes you ..."
        wt_image cheater_continuing_23
        "... then she starts playing with herself as she takes you into her mouth."
        if lauren.has_item(chastity_belt):
            "Locked into the chastity belt, the only time she gets to touch herself is when you or her husband let her out, but she needs to get better at giving head before you'll allow her the opportunity for self pleasure."
        else:
            "That explains why she took off her pants, but she needs to get better at giving head before you'll allow her the opportunity for self pleasure."
        wt_image cheater_continuing_24
        player.c "Get your hand away from your pussy.  You need to learn how to pleasure me, first."
        wt_image cheater_continuing_8
        player.c "Use more of your tongue.  Back and forth along the underside of my cock."
        wt_image cheater_continuing_7
        player.c "Swallow me, right down to the base, then slide back up to the tip. Tongue against my head, flick it back and forth. Then start another stroke, deeper this time, and hold it at the end, and repeat."
        wt_image cheater_continuing_24
        player.c "We're going to keep doing this until you get it right, slut.  If you want to earn the right to touch yourself, you'd better pay attention."
        wt_image cheater_continuing_25
        "It's not the best blow job you've ever received, but eventually she follows your instructions well enough to earn a throatload of jizz."
        player.c "[player.orgasm_text]"
        player.c "Swallow it all."
        wt_image cheater_continuing_5
        lauren.c "I did."
        player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught."
        $ lauren.swallow_count += 1
    elif lauren.blowjob_count == 2:
        wt_image cheater_continuing_5
        "Lauren pulls off her pants, drops to her knees and takes out your cock.  She looks up at you as she strokes you ..."
        wt_image cheater_continuing_23
        "... then she starts playing with herself as she takes you into her mouth."
        if lauren.has_item(chastity_belt):
            "Locked into the chastity belt, the only time she gets to touch herself is when you or her husband let her out, but she needs to get better at giving head before you'll allow her the opportunity for self pleasure."
        else:
            "That explains why she took off her pants, but she needs to get better at giving head before you'll allow her the opportunity for self pleasure."
        wt_image cheater_continuing_24
        player.c "Get your hand away from your pussy.  You need to learn how to pleasure me, first.  Next lesson.  You need to pleasure my balls, not just my cock."
        ## note doesn't use lauren_second_blowjob because of different art
        wt_image cheater_continuing_6
        player.c "Give them a good washing with your tongue, then get your mouth around them and let them warm up in your mouth. "
        wt_image cheater_continuing_8
        player.c "Now you can go back to sucking my cock."
        wt_image cheater_continuing_24
        "You need to correct her frequently ..."
        wt_image cheater_continuing_25
        "... but eventually she follows your instructions well enough to earn a throatload of jizz."
        player.c "[player.orgasm_text]"
        $ lauren.swallow_count += 1
        player.c "You did a little better that time, slut.  If you keep improving, I eventually let you play with yourself while you suck me."
    else:
        wt_image cheater_continuing_5
        "Lauren pulls off her pants, drops to her knees and takes out your cock.  She looks up at you as she strokes you."
        wt_image cheater_continuing_6
        "Remembering her training, she warms up your balls with her mouth and tongue ..."
        wt_image cheater_continuing_8
        "... before taking your cock into her mouth."
        wt_image cheater_continuing_23
        "Reaching a hand between her legs, she starts playing with herself as she blows you.  That explains why she took off her pants."
        if lauren.has_item(chastity_belt):
            "Locked into the chastity belt, the only time she gets to touch herself is when you or her husband let her out.  It's no wonder she seeks opportunities for self pleasure."
        $ title = "Let her touch herself while she blows you?"
        menu:
            "Yes":
                "She's doing a good job, so you allow her the indulgence of pleasuring herself as she pleasures you."
                wt_image cheater_continuing_8
                "You're rewarded with some soft whimpers of pleasure as she sucks you ..."
                lauren.c "mmmm  ...  mmmm"
                wt_image cheater_continuing_25
                "... which become even deeper as she swallows your load."
                lauren.c "MMMMMMM"
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_8
                extend " In fact, you're pretty sure she just came while swallowing your cum."
                $ lauren.swallow_desire_count += 1
                if lauren.swallow_desire_count == 1:
                    change lauren desire by 15
                elif lauren.swallow_desire_count == 2:
                    change lauren desire by 10
                else:
                    change lauren desire by 5
            "No":
                player.c "Get your hand out of there, slut.  This blow job is for my pleasure, not yours."
                wt_image cheater_continuing_24
                "She whimpers in disappointment, but removes her hand."
                wt_image cheater_continuing_7
                "Despite her disappointment, she does a good job sucking your cock ..."
                wt_image cheater_continuing_8
                "... and you're soon ready to cum."
                $ title = "Where do you cum?"
                menu:
                    "On her face":
                        wt_image cheater_facial_5
                        player.c "[player.orgasm_text]"
                        wt_image cheater_facial_6
                        player.c "That's a good slut.  Once you've licked my dick clean you can clean yourself up and go."
                        $ lauren.facial_count += 1
                        if lauren.facial_count == 1:
                            change lauren submission by 5
                    "In her mouth":
                        # note: purposefully no desire swallow changes because of not allowing her to touch herself
                        wt_image cheater_continuing_25
                        player.c "[player.orgasm_text]"
                        wt_image cheater_continuing_8
                        player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go."
    return

label lauren_continuing_office_1_oral:
    $ lauren.blowjob_count += 1
    if lauren.has_tag('tits_out_today'):
        if lauren.blowjob_count == 1:
            player.c "How'd we get this far without you sucking my cock yet, slut?"
            wt_image cheater_office_3_67
            player.c "Show me what you know about giving head."
            wt_image cheater_office_3_68
            player.c "Not much, apparently."
            wt_image cheater_office_3_69
            player.c "Use more of your tongue.  Back and forth along the underside of my cock."
            wt_image cheater_office_3_70
            player.c "Swallow me, right down to the base, then slide back up to the tip. Tongue against my head, flick it back and forth. Then start another stroke, deeper this time, and hold it at the end, and repeat."
            wt_image cheater_office_3_68
            "It's not the best blow job you've ever received, but eventually she follows your instructions well enough to earn a throatload of jizz."
            wt_image cheater_office_3_67
            player.c "[player.orgasm_text]"
            player.c "Swallow it all."
            wt_image cheater_office_3_69
            lauren.c "I did."
            player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught."
            $ lauren.swallow_count += 1
        elif lauren.blowjob_count == 2:
            wt_image cheater_office_3_68
            call lauren_second_blowjob from _call_lauren_second_blowjob_10
            wt_image cheater_office_3_71
            player.c "Now you can go back to sucking my cock."
            wt_image cheater_office_3_68
            "You need to correct her frequently ..."
            wt_image cheater_office_3_70
            "... but eventually she follows your instructions well enough to earn a throatload of jizz."
            wt_image cheater_office_3_67
            player.c "[player.orgasm_text]"
            $ lauren.swallow_count += 1
            player.c "You did a little better that time, slut.  When you've finished swallowing, you can go back to work."
        else:
            wt_image cheater_office_3_71
            "Lauren accepts your dick as you feed it into her mouth ..."
            wt_image cheater_ball_lick_1
            "... and your balls, when you feed her those."
            wt_image cheater_office_3_68
            "She knows what she's doing now when she gives head ..."
            wt_image cheater_office_3_69
            "... and uses her tongue ..."
            wt_image cheater_office_3_70
            "... hand, lips and mouth ..."
            wt_image cheater_office_3_68
            "... to get you ready to cum."
            $ title = "Where do you cum?"
            menu:
                "On her face":
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_6
                    player.c "That's a good slut.  Once you've licked my dick clean you can clean yourself up and go back to your very important job."
                    $ lauren.facial_count += 1
                    if lauren.facial_count == 1:
                        change lauren submission by 5
                "In her mouth":
                    wt_image cheater_office_3_67
                    player.c "[player.orgasm_text]"
                    call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_9
                    $ lauren.swallow_desire_count += 1
                    if lauren.swallow_desire_count == 1:
                        change lauren desire by 10
                    elif lauren.swallow_desire_count == 2:
                        change lauren desire by 5
                    wt_image cheater_office_3_70
                    player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go back to your very important job."
    else:
        if lauren.blowjob_count == 1:
            player.c "How'd we get this far without you sucking my cock yet, slut?  Show me what you know about giving head."
            wt_image cheater_office_3_61
            player.c "Not much, apparently."
            wt_image cheater_office_3_60
            player.c "Use more of your tongue.  Back and forth along the underside of my cock."
            wt_image cheater_office_3_24
            player.c "Swallow me, right down to the base."
            wt_image cheater_office_3_62
            player.c "Now slide back up to the tip.  Tongue against my head, flick it back and forth.  Then start another stroke.  Deeper this time, and hold it at the end.  Now repeat."
            wt_image cheater_office_3_24
            "It's not the best blow job you've ever received, but eventually she follows your instructions well enough to earn a throatload of jizz."
            player.c "[player.orgasm_text]"
            player.c "Swallow it all."
            wt_image cheater_office_3_60
            lauren.c "I did."
            player.c "Good.  I'm glad you know something about giving blow jobs without having to be taught."
            $ lauren.swallow_count += 1
        elif lauren.blowjob_count == 2:
            wt_image cheater_office_3_61
            call lauren_second_blowjob from _call_lauren_second_blowjob_11
            wt_image cheater_office_3_64
            player.c "Now you can go back to sucking my cock.  Keep my balls warm with your hand as you blow me."
            wt_image cheater_office_3_62
            "You need to correct her frequently ..."
            wt_image cheater_office_3_24
            "... but eventually she follows your instructions well enough to earn a throatload of jizz."
            player.c "[player.orgasm_text]"
            $ lauren.swallow_count += 1
            wt_image cheater_office_3_66
            player.c "You did a little better that time, slut.  When you've finished swallowing, you can go back to work."
        else:
            wt_image cheater_office_3_61
            "Lauren accepts your dick as you feed it into her mouth ..."
            wt_image cheater_ball_lick_1
            "... and your balls, when you feed her those."
            wt_image cheater_office_3_64
            "She knows what she's doing now when she gives head ..."
            wt_image cheater_office_3_60
            "... and uses her tongue ..."
            wt_image cheater_office_3_65
            "... hand ..."
            wt_image cheater_office_3_66
            "... lips and mouth ..."
            wt_image cheater_office_3_62
            "... to get you ready to cum."
            $ title = "Where do you cum?"
            menu:
                "On her face":
                    wt_image cheater_facial_1
                    player.c "[player.orgasm_text]"
                    wt_image cheater_facial_3
                    player.c "That's a good slut.  Once you've licked my dick clean you can clean yourself up and go back to your very important job."
                    $ lauren.facial_count += 1
                "In her mouth":
                    wt_image cheater_office_3_24
                    player.c "[player.orgasm_text]"
                    call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_10
                    $ lauren.swallow_desire_count += 1
                    if lauren.swallow_desire_count == 1:
                        change lauren desire by 10
                    elif lauren.swallow_desire_count == 2:
                        change lauren desire by 5
                    wt_image cheater_office_3_62
                    player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go back to your very important job."
    return

label lauren_continuing_office_1_tied_up_oral:
    $ lauren.blowjob_count += 1
    wt_image cheater_office_3_41
    if lauren.blowjob_count == 1:
        player.c "How'd we get this far without you sucking my cock yet, slut?  Show me what you know about giving head."
        wt_image cheater_office_3_42
        player.c "Not much, apparently."
        wt_image cheater_office_3_7
        player.c "Use more of your tongue.  Back and forth along the underside of my cock."
        wt_image cheater_office_3_42
        player.c "Swallow me, right down to the base."
        wt_image cheater_office_3_43
        "It's not the best blow job you've ever received, but eventually she follows your instructions well enough to earn a throatload of jizz."
    elif lauren.blowjob_count == 2:
        # note: alternate text and photos to normal lauren_second_blowjob label
        player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
        wt_image cheater_office_3_42
        player.c "First though, we're going to add some new wrinkles ... excuse the pun.  Get your tongue down there on my balls, Lauren."
        wt_image cheater_ball_lick_2
        player.c "Give them a good washing, then get your mouth around them. Gently. Let them warm up in your mouth. I'll tell you when I'm ready for you to start sucking my cock again."
        wt_image cheater_office_3_7
        player.c "Now go back to sucking my cock, slut."
        wt_image cheater_office_3_42
        "You need to correct her frequently ..."
        wt_image cheater_office_3_43
        "... but eventually she follows your instructions well enough to earn a throatload of jizz."
    else:
        "Lauren accepts your dick as you feed it into her mouth ..."
        wt_image cheater_ball_lick_2
        "... and your balls, when you feed her those."
        wt_image cheater_office_3_7
        "She knows what she's doing now when she gives head ..."
        wt_image cheater_office_3_42
        "... and even tied up like this ..."
        wt_image cheater_office_3_43
        "... is soon able to earn a throatload of jizz."
    $ lauren.swallow_count += 1
    player.c "[player.orgasm_text]"
    return

label lauren_continuing_office_2_oral:
    $ lauren.blowjob_count += 1
    player.c "Take off your clothes and kneel down."
    wt_image cheater_office_4_7
    if lauren.blowjob_count == 1:
        player.c "How'd we get this far without you sucking my cock yet, slut?  Time for you to show me what you know about giving head."
        wt_image cheater_office_4_24
        player.c "Not much, apparently."
        wt_image cheater_office_4_25
        player.c "Use more of your tongue.  Back and forth along the underside of my cock."
        wt_image cheater_office_4_26
        player.c "Swallow me, right down to the base."
        wt_image cheater_office_4_27
        player.c "Now slide back up to the tip. Tongue against my head, flick it back and forth. Then start another stroke, deeper this time, hold it at the end, and repeat."
        wt_image cheater_office_4_26
        "With your hand in her hair, you guide her mouth back and forth along your cock, instructing her on how you like your cock sucked."
        wt_image cheater_office_4_24
        "It's not the best blow job you've ever received, but eventually she follows your instructions well enough to earn a throatload of jizz."
        wt_image cheater_office_4_31
        player.c "[player.orgasm_text]"
        player.c "Swallow it all."
        wt_image cheater_office_4_29
        lauren.c "I did.  Oops.  Well, most of it."
        player.c "Swallow all of it next time.  If I want a mess on your face, I'll put it there myself."
        $ lauren.swallow_count += 1
    elif lauren.blowjob_count == 2:
        # note: doesn't use the lauren_second_blowjob label in order to use scene specific art
        player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
        player.c "First though, we're going to add some new wrinkles ... excuse the pun.  Get your tongue down there on my balls, Lauren."
        wt_image cheater_office_4_28
        player.c "Give them a good washing, then get your mouth around them. Gently. Let them warm up in your mouth. I'll tell you when I'm ready for you to start sucking my cock again. Until then, use your hand to stroke me until your mouth takes its place."
        wt_image cheater_office_4_25
        player.c "Now you can go back to sucking my cock."
        wt_image cheater_office_4_26
        "You need to correct her frequently ..."
        wt_image cheater_office_4_24
        "... but eventually she follows your instructions well enough to earn a throatload of jizz."
        wt_image cheater_office_4_31
        player.c "[player.orgasm_text]"
        wt_image cheater_office_4_29
        player.c "You did a little better that time, slut.  When you've finished swallowing, you can go back to work."
        $ lauren.swallow_count += 1
    else:
        wt_image cheater_office_4_26
        "Lauren accepts your dick as you feed it into her mouth ..."
        wt_image cheater_office_4_28
        "... and your balls, when you feed her those."
        wt_image cheater_office_4_25
        "She knows what she's doing now when she gives head ..."
        wt_image cheater_office_4_27
        "... and uses her tongue ..."
        wt_image cheater_office_4_24
        "... lips and mouth ..."
        wt_image cheater_office_4_25
        "... to get you ready to cum."
        $ title = "Where do you cum?"
        menu:
            "On her face":
                wt_image cheater_office_4_30
                player.c "[player.orgasm_text]"
                player.c "That's a good slut.  Once you've licked my dick clean you can clean yourself up and go back to your very important job."
                $ lauren.facial_count += 1
                if lauren.facial_count == 1:
                    change lauren submission by 5
            "In her mouth":
                wt_image cheater_office_4_31
                player.c "[player.orgasm_text]"
                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_11
                $ lauren.swallow_desire_count += 1
                if lauren.swallow_desire_count == 1:
                    change lauren desire by 10
                elif lauren.swallow_desire_count == 2:
                    change lauren desire by 5
                wt_image cheater_office_4_29
                player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go back to your very important job."
    return

label lauren_anal_question:
    # NEED update to add proper artwork when referred from posing 3 artwork
    # note: this content is duplicated in lauren_punish_bondage_anal due to photo differences
    lauren.c "No!  Stop ... don't do that."
    player.c "Why not?"
    lauren.c "I've never done that."
    player.c "Really?  Your husband never asked?"
    lauren.c "Once, a long time ago.  But it's not something I want to try.  And he hasn't asked me since.  It isn't something he wants from me."
    player.c "When your husband sent you to me, he said he wanted you trained to be his perfect little fuck toy.  He didn't say make her a perfect little fuck toy but don't bother with the anal."
    lauren.c "I swear, he doesn't care about anal.  He really doesn't."
    player.c "Every man wants to fuck his wife's ass, Lauren. Maybe he just didn't want to push this. Things have changed, though, haven't they? You want to please him, don't you? Isn't that why you're here?"
    "She nods and starts to sob softly."
    lauren.c "Yes, but can't we do other things?  I can please him in so many different ways.  Does it have to be this?"
    "Her resistance on this topic is different than her past objections.  She seems truly distraught at the prospect of taking your cock in her ass.  If you relent, it may increase her trust in you."
    "On the other hand, there may be no better way to break down the mental barriers that prevent her from seeing herself as a happy obedient slut than to push through and past this taboo."
    "Her resistance to you will have to be quite low to accept anal considering how strongly she feels on this topic.  Gifting a butt plug to her would help."
    "If her resistance isn't low enough, it may be better to wait, because if you insist and she balks, her trust will be gone.  She might even call an end to this arrangement."
    $ title = "What do you do?"
    menu:
        "Relent and accept anal as limit for her":
            add tags 'no_anal' to lauren
            player.c "Very well. I'll accept that anal is a limit for you. You realize, however, that means you're going to have to work even harder in every other way to make up for the pleasure he's not getting from your ass."
            change lauren desire by 10
            change lauren resistance by -10
            # finishing text and photos to be included in the referring label
        "Wait":
            player.c "We'll discuss this again later."
            "Lauren is silent.  Clearly this is not something she wants to discuss again, ever.  There's too much tension between you to do anything further tonight.  You let her dress and go home."
            add tags 'anal_postponed_today' to lauren
        "Insist on anal now":
            player.c "Yes, slut, it has to be this. Your husband wants you to be his personal little whore. That includes being his asswhore."
            player.c "Now relax. This won't hurt as much as you're afraid it will.  You may even grow to enjoy it."
            if butt_plug in lauren.items:
                $ lauren.open_temp_group('Gifted Butt Plug', duration = 1, duration_unit = 'check')
                $ lauren.add_temp_mod('resistance', -20, with_message = False)
                $ lauren.close_temp_group(with_notify = False)
            if lauren.test('resistance', 25):
                add tags 'accepts_anal' to lauren
                $ lauren.anal_count += 1
                wt_image cheater_anal_5
                lauren.c "No. Please."
                "Her voice is no more than a whimper as she feels the head of your cock pressing against her anus."
                wt_image cheater_anal_6
                player.c "That's the wrong response, slut.  I'm going to fuck you in the ass and you're going to accept that.  Do you understand?"
                "Tears start to fall down her face as she nods quietly."
                player.c "Say it, slut.  Say that I can fuck you in the ass."
                "She takes two deep breathes before she responds, even more quietly than before."
                lauren.c "{size=-5}Yes.  You can fuck me in the ass.{/size}"
                wt_image cheater_anal_1
                "You're not as gentle as you could have been, but having won her surrender, there's no need to be gracious in victory.  She screams as you push yourself into her."
                lauren.c "OWWW!!!!"
                "You can take it more slowly next time, work yourself in more gradually, and give her a chance to potentially enjoy the sensation."
                wt_image cheater_anal_7
                "That's for next time.  This time is isn't about enjoyment.  It's about conquest.  You conquering her, her conquering her inhibitions and accepting her new life."
                player.c "You're an asswhore now, aren't you slut?"
                "Meekly, she nods."
                player.c "Say it."
                wt_image cheater_anal_1
                lauren.c "I'm an asswhore!"
                player.c "Good girl."
                wt_image cheater_anal_3
                player.c "[player.orgasm_text]"
                orgasm
                # finishing text and photos to be included in the referring label
            elif lauren.test('resistance', 35) and lauren.has_tag('love_potion_used'):
                lauren.c "Noooo!!!!  I said no, and I meant it."
                change lauren resistance by 10
                change lauren sos by -5
                # finishing text and photos to be included in the referring label
            else:
                lauren.c "Noooo!!!!  I said no, and I meant it."
                $ office_tower.remove_connection(lauren_office)
                $ office_tower.remove_action(office_tower.action_visit_lauren)
                rem tags 'trained_this_week' from lauren # So she won't pay us this session
                add tags 'failed_training' to lauren
                call convert(lauren, 'unsatisfied', True, True) from _call_convert_150
                # finishing text and photos to be included in the referring label
    return

label lauren_second_anal:
    # note: this content is duplicated in lauren_punish_bondage_anal due to photo differences
    # initial photo to be set in referring label
    $ lauren.anal_count += 1
    "Lauren starts to tremble nervously when she sees you pick up the lubricant."
    player.c "It's okay, little asswhore.  No need to worry about your lack of experience.  I'm going to give you lots of time to learn how to please me with your ass."
    "You lead her over to a soft mattress.  She'll have enough discomfort getting used to your dick in her ass.  No need to have her knees killing her, too."
    wt_image cheater_anal_2
    player.c "Get into position for me, asswhore."
    "You stroke your cock, coating it with lubricant as she supplicates herself in front of you. Then you drizzle the lubricant onto her rosebud, a soft gasp escaping her mouth as its coolness lands on her skin."
    lauren.c "Oh!"
    wt_image cheater_anal_5
    "The coolness of the lubricant is replaced by the warmth of the head of your cock, eliciting another gasp."
    lauren.c "Ah!"
    player.c "Time to start your lesson, asswhore.  Work yourself back on to me.  That's it, push back.  Your ass will open itself naturally."
    wt_image cheater_anal_3
    "With the amount of lubricant you applied, you actually slide into her rather easily.  She gasps again, this time in surprise, as she feels the head of your cock slide pass the anal rim."
    lauren.c "OHHH!"
    wt_image cheater_anal_6
    player.c "Good.  Now you fuck me just like you do with your cunt when I'm behind you.  Rock your hips back and forth.  Take me deeper inside you with every thrust."
    wt_image cheater_anal_7
    "It's not a difficult technique, and she gets it easily."
    wt_image cheater_anal_3
    "It takes some time for her ass to stretch enough to take all of you inside her, and you need to re-apply some lubricant before she can get to that point."
    wt_image cheater_anal_5
    "Soon after, though, she's fucking her rectum up and down the full length of your cock, her ass slamming back into you hard on every back thrust."
    wt_image cheater_anal_1
    "When you're satisfied she has the hang of it, you let yourself go.  You hold her hips still, the tip of your cock just barely inside her ass as your balls unload into her."
    player.c "[player.orgasm_text]"
    wt_image cheater_anal_8
    "As you pull out, most of your sperm flows out of her ass and drips down over her pussy."
    player.c "Look over here, asswhore."
    wt_image cheater_anal_4
    "You position her hips so that she can see your cum on her in the mirror."
    player.c "That's what you're taking home tonight.  You're going to show this to your husband and explain how it got there.  Then you're going to let him know that from now on, you're his little asswhore, whenever he wants.  Do you understand?"
    lauren.c "Yes"
    wt_image cheater_nervous_1
    player.c "He's going to fuck you in the ass tonight, isn't he?"
    "She nods."
    wt_image cheater_initial_1
    player.c "Take the lubricant.  He may not use it, but at least you can offer it to him, in case he doesn't want to hurt you too much."
    orgasm
    return

label lauren_additional_anal:
    # note: this content is duplicated in lauren_punish_bondage_anal due to photo differences
    $ lauren.anal_count += 1
    player.c "Get into position, asswhore."
    "You motion her towards the mattress."
    wt_image cheater_anal_2
    "Lauren drops into position position for you."
    player.c "Open wide."
    wt_image cheater_anal_9
    "You lubricate first your cock, then her anus, as you enjoy the sight of the married businesswoman waiting to take your cock in her ass."
    wt_image cheater_anal_10
    "She gets your full length inside her more easily now, as she's learned to relax and let her body stretch to accommodate you."
    wt_image cheater_anal_5
    "As she moves her hips back and forth fucking you, you try to stimulate her, flicking your fingers against her clit to see if you can coax an anal orgasm out of her."
    wt_image cheater_anal_3
    "It's no use.  She just doesn't enjoy anal enough to get excited, even with your fingers playing with her."
    wt_image cheater_anal_6
    "This is just a service for her, something she provides to please her man, not her.  Which was the point of her training all along."
    wt_image cheater_anal_1
    "When she's pleased you enough, you thrust forward into her, hard, releasing your seed deep inside her."
    player.c "[player.orgasm_text]"
    wt_image cheater_anal_11
    "She'll feel the cum dripping out of her butt all the way home tonight."
    orgasm
    return

label lauren_anal_stat_changes:
    if lauren.anal_count == 1:
        change lauren sos by 10
    elif lauren.anal_count == 2:
        change lauren sos by 10
        "Lauren won't learn anything more from additional anal sex, but she won't say no, either, if you choose to take her that way again."
    return

label lauren_cum_arousal_stat_change:
    # note: actual stat changes moved to blowjob_stat_changes, so this is now just flavour text
    if lauren.has_tag('cum_arousal'):
        "Lauren squirms and moans slightly as your load strikes the back of her throat."
    else:
        add tags 'cum_arousal' to lauren
        "Lauren squirms and moans slightly as your load strikes the back of her throat. The act of receiving and swallowing your jizz is turning her on."
    return

label lauren_wait_for_you_stat_changes:
    if lauren.wait_count == 1:
        change lauren resistance by -10
    elif lauren.wait_count == 2:
        change lauren resistance by -5
    elif lauren.wait_count == 3:
        change lauren sos by 5
        "Having Lauren wait for you again won't have any further impact on her training."
    else:
        "Having Lauren continue to wait for you is no longer having an impact on her training.  It's still fun, though."
    return

label lauren_open_her_stat_changes:
    if lauren.open_her_count == 1:
        change lauren resistance by -5
    elif lauren.open_her_count == 2:
        change lauren resistance by -10
        "Having Lauren open herself up again won't have any additional impact."
    else:
        "Having Lauren open herself up is no longer having an impact on her training.  It's still fun, though."
    return

label lauren_caress_stat_changes:
    if lauren.caress_her_count == 1:
        change lauren desire by 10
    elif lauren.caress_her_count == 2:
        change lauren desire by 5
        "Lauren's becoming familiar to the feel of your fingers on her.  Continuing to touch her in this way won't have any additional impact."
    else:
        "Lauren's become used to the feel of your fingers on her.  Continuing to touch her in this way won't have any additional impact."
    return

label lauren_masturbation_stat_changes:
    if lauren.has_tag('masturbated_to_orgasm'):
        pass
    else:
        add tags 'masturbated_to_orgasm' to lauren
        "Bringing herself to orgasm while you watch helps Lauren accept that she can be an obedient slut."
        change lauren resistance by -5
        change lauren sos by 5
    return

label lauren_spank_stat_changes:
    if lauren.spank_count == 1:
        if lauren.location == lauren_office:
            add tags 'spanked_in_office' to lauren
            change lauren submission by 15
            "Being spanked is humiliating enough.  Being spanked in her own office with her receptionist waiting just outside the door is even more humiliating."
        else:
            change lauren submission by 10
    elif lauren.spank_count == 2:
        if lauren.location == lauren_office and not lauren.has_tag('spanked_in_office'):
            add tags 'spanked_in_office' to lauren
            change lauren submission by 10
            "Being spanked is humiliating enough.  Being spanked in her own office with her receptionist waiting just outside the door is even more humiliating."
        else:
            change lauren submission by 5
            "Lauren's become as submissive as she's going to be from spanking alone."
    elif lauren.location == lauren_office and not lauren.has_tag('spanked_in_office'):
        add tags 'spanked_in_office' to lauren
        change lauren submission by 5
        "Being spanked is humiliating enough.  Being spanked in her own office with her receptionist waiting just outside the door is even more humiliating."
    else:
        "You'll need to do more than spank Lauren to increase her submission to you further."
    return

label lauren_pleasure_her_stat_changes:
    if lauren.pleasure_her_count == 1:
        change lauren desire by 10
    elif lauren.pleasure_her_count == 2:
        change lauren desire by 5
        if lauren.orgasm_count > 0:
            "Lauren's becoming used to being pleasured by you.  Continuing to do so won't have any additional impact on her training."
    else:
        if lauren.orgasm_count > 0:
            "Lauren's become used to being pleasured by you.  She likes it, but it's not furthering her training."
    return

label lauren_orgasm_stat_change:
    $ lauren.orgasm_count += 1
    if lauren.orgasm_count == 1:
        "Being brought to orgasm by you affects how Lauren sees you."
        change lauren desire by 10
    return

label lauren_blowjob_stat_changes:
    # note: must run after increasing her blowjob_count
    if lauren.has_tag('facial_today'):
        $ lauren.facial_count += 1
    else:
        $ lauren.swallow_count += 1
    if lauren.blowjob_count == 1:
        change lauren submission by 5
    elif lauren.blowjob_count == 2:
        change lauren resistance by -5
    elif lauren.blowjob_count == 3:
        change lauren sos by 5
    else:
        if lauren.has_tag('facial_today'):
            # note: facials not available until blowjob_count >3
            if lauren.facial_count == 1:
                change lauren resistance by -5
            elif lauren.facial_count == 2:
                change lauren sos by 10
        else:
            $ lauren.swallow_desire_count += 1
            if lauren.swallow_desire_count == 1:
                change lauren desire by 10
            elif lauren.swallow_desire_count == 2:
                change lauren desire by 5
    rem tags 'facial_today' from lauren
    return

label lauren_second_blowjob:
    player.c "Not bad.  You remember some of your lesson.  Not all of it.  We'll go through it again."
    player.c "First though, we're going to add some new wrinkles ... excuse the pun.  Get your tongue down there on my balls, slut."
    wt_image cheater_ball_lick_1
    player.c "Give them a good washing, then get your mouth around them. Gently. Let them warm up in your mouth. I'll tell you when I'm ready for you to start sucking my cock again. Until then, use your hand to stroke me until your mouth takes its place."
    return

label lauren_third_blowjob:
    player.c "You're starting to get the hang of this, slut.  Good technique with my balls, getting them nice and warm before you started sucking my cock."
    player.c "Nice responsiveness to my hand in your hair, slowing down and speeding up as soon as I shift my grip.  No need for me to pull your head around like a pumpkin anymore before you figure out what I want."
    player.c "You're on your way to becoming a fine little cocksucker, slut.  Does that feel good, knowing that you're finally able to please a man properly with your mouth?"
    return

label lauren_fourth_blowjob:
    "Lauren knows what's she's doing now.  There's no need for you to correct her, or even speak.  She's embraced being a good little obedient cocksucker."
    return

label lauren_sex_stat_changes:
    if lauren.has_tag('pleasurable_fuck_today') and not lauren.has_tag('pleasure_fucked'):
        add tags 'pleasure_fucked' to lauren
        "Being fucked gently by you for the first time has a positive impact on how Lauren sees you."
        change lauren desire by 5
    elif lauren.has_tag('rough_fuck_today') and not lauren.has_tag('rough_fucked'):
        add tags 'rough_fucked' to lauren
        "Willingly accepting you treating her like this for the first time erodes Lauren's ability to say no to you."
        change lauren resistance by -5
    elif lauren.has_tag('ride_fuck_today') and not lauren.has_tag('ride_fucked'):
        add tags 'ride_fucked' to lauren
        "Being in charge of your sexual satisfaction when you've decided you want her to fuck you helps Lauren see herself as an obedient slut."
        change lauren sos by 5
    if lauren.sex_count == 1:
        change lauren sos by 5
    elif lauren.sex_count == 2:
        change lauren sos by 5
    elif lauren.sex_count == 3:
        change lauren sos by 10
    if lauren.sex_count > 2 and lauren.has_tag('pleasure_fucked') and lauren.has_tag('rough_fucked') and lauren.has_tag('ride_fucked'):
        "Lauren probably won't learn anything more from fucking you.  She also won't say no if you want her to do so as part of her training, anyway."
    return

## Post-Training Character Actions
# Bimbo - Spend Time With Her
label lauren_bimbo_spend_time:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ lauren.bimbo_outfit_count += 1
    if lauren.bimbo_outfit_count > 4:
        $ lauren.bimbo_outfit_count = 1
    if lauren.bimbo_outfit_count == 1:
        wt_image cheater_bimbo_3_7
        "You left clothes out for Lauren to wear this morning.  Skimpy clothes, just a see through wrap."
        wt_image cheater_bimbo_3_1
        "When you check in on her, she seems confused by the feeling of the material against her skin."
        wt_image cheater_bimbo_3_6
        "You watch as she pulls back the wrap and touches her nipple ..."
        wt_image cheater_bimbo_3_8
        "... then slides her hand down her body ..."
        wt_image cheater_bimbo_3_2
        "... as if to confirm that the strange sensation isn't because something's wrong with her skin."
        wt_image cheater_bimbo_3_9
        "Satisfied that the wrap was the problem, she pulls it off."
        wt_image cheater_bimbo_3_3
        "That's when she notices you watching her."
        wt_image cheater_bimbo_3_4
        "She drops to the floor and spreads her legs."
        lauren.c "Hi!  Is it time for us to fuck again?"
        player.c "I just wanted to see how you were doing, Lauren."
        wt_image cheater_bimbo_3_5
        lauren.c "I'm happy. I didn't like being covered up. It made my skin feel funny. But now I'm good. How long is it until we fuck again?"
    elif lauren.bimbo_outfit_count == 2:
        wt_image cheater_bimbo_2_1
        lauren.c "I'm cold."
        player.c "Maybe you should do what naked people normally do when they get cold?"
        wt_image cheater_bimbo_2_2
        lauren.c "Start a fire?"
        wt_image cheater_bimbo_2_3
        lauren.c "This one's too cold.  And not pretty."
        player.c "There's no fire in the fireplace right now, Lauren."
        wt_image cheater_bimbo_2_4
        lauren.c "Maybe this will help?"
        wt_image cheater_bimbo_2_5
        player.c "Lauren, that's just a poker."
        wt_image cheater_bimbo_2_6
        lauren.c "I like things that poke me!"
        wt_image cheater_bimbo_2_7
        lauren.c "Maybe I need to rub it to get it to work?"
        wt_image cheater_bimbo_2_8
        lauren.c "mmmmm"
        wt_image cheater_bimbo_2_9
        lauren.c "It's working!  I can feel warmth!!"
        wt_image cheater_bimbo_2_10
        lauren.c "Most of the warmth's on the inside.  I should rub the poker there."
        wt_image cheater_bimbo_2_11
        player.c "Lauren, you can't start a fire by fucking yourself with a poker."
        wt_image cheater_bimbo_2_12
        lauren.c "What if I use two pokers?"
        wt_image cheater_bimbo_2_13
        lauren.c "And rub them together ..."
        wt_image cheater_bimbo_2_14
        lauren.c "... like this!"
        wt_image cheater_bimbo_2_15
        "You leave her to her firestarter experiments. You just hope she has the sense to get under a blanket before she catches a cold."
    elif lauren.bimbo_outfit_count == 3:
        wt_image cheater_bimbo_1_2
        "You don't let Lauren have a dildo. You're worried that she'd use it so much, she might hurt herself. But sometime when you weren't looking, she found a banana in the kitchen."
        wt_image cheater_bimbo_1_1
        "She's looking at it as if she's trying to decide something."
        wt_image cheater_bimbo_1_7
        "Eventually, she makes up her mind.  She places the banana against her sex ..."
        wt_image cheater_bimbo_1_8
        "... and pushes it inside her."
        wt_image cheater_bimbo_1_4
        "As the banana penetrates her, she lets out a big grin. Was that what she was trying to decide, whether the banana would fit inside her or not?"
        wt_image cheater_bimbo_1_5
        "Seemingly pleased with her own cleverness, she celebrates by pumping the banana in and out of her swelling and aroused pussy."
        wt_image cheater_bimbo_1_9
        "With the banana in her cunt and her fingers on her clit, she soon jills herself to one, two, three orgasms in short succession."
        lauren.c "Aaahhhh!!  ...  Aaahhhh!!!  ...  Aaahhhh!!!!"
        wt_image cheater_bimbo_1_10
        "You leave her there to fuck herself silly."
        lauren.c "Aaahhhh!!  ...  Aaahhhh!!!  ...  Aaahhhh!!!!"
        wt_image cheater_bimbo_1_6
        "After a few more orgasms she'll pass out from exhaustion, and you'll be able to take the banana away from her without her begging you to replace it with your cock."
        lauren.c "Aaaaaaaaahhhhhhhh ..."
    elif lauren.bimbo_outfit_count == 4:
        call forced_movement(bathroom) from _call_forced_movement_711
        summon lauren
        wt_image cheater_bimbo_4_1
        "You find Lauren in the bathroom, staring at the mirror."
        wt_image cheater_bimbo_4_6
        "She moves back and forth ..."
        wt_image cheater_bimbo_4_2
        "... watching her image in the mirror move at the same time."
        wt_image cheater_bimbo_4_7
        "She does know that's her, right?  She starts smiling at and flirting with the mirror."
        wt_image cheater_bimbo_4_3
        "When the mirror makes the same responses back, her nipples harden noticeably."
        wt_image cheater_bimbo_4_4
        "Aroused by her own reflection, she starts playing with herself."
        wt_image cheater_bimbo_4_8
        "She finally notices you standing there."
        wt_image cheater_bimbo_4_5
        lauren.c "I think that woman wants to fuck me."
        wt_image cheater_bimbo_4_9
        player.c "Finish yourself off, Lauren, then go back to the bedroom and leave that nice woman alone."
        call forced_movement(living_room) from _call_forced_movement_712
        call character_location_return(lauren) from _call_character_location_return_472
    else:
        sys "Oops.  There's been an error with the lauren.bimbo_outfit_count variable."
    return

# Bimbo - Sex
label lauren_bimbo_sex:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ title = "How do you want to use her?"
    menu:
        "Blow job":
            call forced_movement(kitchen) from _call_forced_movement_713
            summon lauren
            wt_image cheater_bimbo_bj_1
            "Blow jobs from Lauren are easy to work into your daily routine.  Do you want head while preparing breakfast?  No problem."
            wt_image cheater_bimbo_bj_2
            "Of course, it'd be nice if Lauren could make breakfast sometimes while you sleep in, but the risk of food poisoning or burning down the kitchen is too great."
            wt_image cheater_bimbo_bj_4
            "Truth is, she can't even remember your instructions on how you like your cock sucked any more."
            wt_image cheater_bimbo_bj_5
            "She'll happily do anything you say right now ..."
            wt_image cheater_bimbo_bj_6
            "... but by tomorrow, she'll have forgotten everything you've taught her."
            wt_image cheater_bimbo_bj_2
            "It can be frustrating dealing with her stupidity ..."
            wt_image cheater_bimbo_bj_7
            "... but the big doe eyes she makes as she fellates you makes it hard to stay mad at her."
            wt_image cheater_bimbo_bj_8
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    wt_image cheater_bimbo_bj_2
                    player.c "[player.orgasm_text]"
                    wt_image cheater_blow_job_1
                    "She waits contentedly until your balls finish emptying themselves down her throat. In fact, she'd wait here all day if you let her."
                    $ lauren.swallow_count += 1
                "On her face":
                    wt_image cheater_bimbo_bj_5
                    "She waits happily for your load ..."
                    wt_image cheater_facial_7
                    "... and is even happier when she receives it."
                    player.c "[player.orgasm_text]"
                    wt_image cheater_bimbo_bj_3
                    "She'll wear your cum for the remainder of the day.  She'd lick the head of your cock for the rest of the day, too, if you let her."
                    $ lauren.facial_count += 1
            $ lauren.blowjob_count += 1
            orgasm notify
            call character_location_return(lauren) from _call_character_location_return_473
            call forced_movement(bedroom) from _call_forced_movement_714
        "Fuck her":
            wt_image cheater_bimbo_sex_1_1
            "Fucking your bimbo can be surprisingly tricky at times."
            wt_image cheater_bimbo_sex_1_2
            "Simply penetrating her triggers a flood of wetness between her legs ..."
            lauren.c "oooooo"
            wt_image cheater_bimbo_sex_1_3
            "... and it's almost never possible to get your dick all the way inside her before she cums."
            lauren.c "Aaahhhh!!"
            wt_image cheater_bimbo_sex_1_4
            "You've taken to pulling her hair to try and focus her on pleasuring you."
            wt_image cheater_bimbo_sex_1_5
            "Unfortunately, even when you pull it HARD it barely dims her pleasure ..."
            lauren.c "Ow!  ....  oooooo"
            wt_image cheater_bimbo_sex_1_6
            "... or slows her orgasms."
            lauren.c "Ow!  ...  Aaahhhh!!"
            wt_image cheater_bimbo_sex_1_7
            "She ends up collapsing in a heap, exhausted by a string of orgasm after orgasm from the feeling of your cock inside her, while you do all the hard work of plowing into her until you finally climax yourself."
            lauren.c "Aaahhhh  ...  Aaahhhh  ...  Aaahhhh"
            player.c "[player.orgasm_text]"
            orgasm notify
        "Fuck her ass":
            wt_image cheater_bimbo_anal_3
            player.c "Get my dick hard for your ass, stupid."
            wt_image cheater_bimbo_anal_4
            "Lauren can vaguely recall a time when she didn't like having cocks up her butt, though she can't understand why she ever felt that way."
            wt_image cheater_bimbo_anal_2
            "Any hole is a good hole to have a cock in it.  Well lubed, barely lubed or no lube, it doesn't matter as long as there's a chance to feel your hard cock inside her."
            wt_image cheater_bimbo_anal_1
            "She doesn't cum from anal, but she doesn't seem to care about that.  Having a cock inside her is more important.  And when you shoot your load up her ass, she giggles."
            player.c "[player.orgasm_text]"
            lauren.c "Hee hee!  That tickles.  Can you do it again?"
            orgasm notify
        "Have her ride you":
            wt_image cheater_bimbo_sex_2_1
            "Lauren pretty much tackles you when you tell her she's allow to ride you."
            wt_image cheater_bimbo_sex_2_2
            "Unfortunately it doesn't feel as good as she was expecting, though she can't figure out why."
            player.c "It works better if you take my cock out of my pants first, stupid."
            wt_image cheater_bimbo_sex_2_3
            "Back on track, Lauren takes out your cock and sucks it hard ..."
            wt_image cheater_bimbo_sex_2_4
            "... then just keeps sucking it."
            player.c "You're supposed to be riding my cock, not sucking it."
            lauren.c "nn nnn nnn"
            player.c "Don't talk with your mouth full."
            wt_image cheater_bimbo_sex_2_5
            "Back on track - again - Lauren finally succeeds in mounting you ..."
            wt_image cheater_bimbo_sex_2_6
            "... triggering an almost immediate orgasm ..."
            lauren.c "Aaahhhh!!"
            wt_image cheater_bimbo_sex_2_7
            "... followed by a series of additional orgasms ..."
            lauren.c "Aaahhhh  ...  Aaahhhh  ...  Aaahhhh"
            wt_image cheater_bimbo_sex_2_6
            "... which wouldn't be so bad if she was getting you off, too."
            player.c "Keep moving!  You're supposed to be riding me, not sitting on me."
            lauren.c "oooo  ...  okay  ...  Aaahhhh!!"
            wt_image cheater_bimbo_sex_2_8
            "Eventually you have to move her to a position where you can lift her up and down on your cock as she cums."
            lauren.c "Aaahhhh  ...  Aaahhhh  ...  Aaahhhh"
            wt_image cheater_bimbo_sex_2_9
            "She's a blithering, drooly mess by the time you succeed in using her to get an orgasm of your own."
            lauren.c "Aaaa ... aaa ... aaahhhhhhhhhhh"
            player.c "[player.orgasm_text]"
            orgasm notify
        "Have her lick your ass":
            wt_image cheater_bimbo_ass_lick_2
            "Sometimes Lauren just wears you out. Her sex drive is insatiable. Fortunately, you've discovered a little trick that helps."
            wt_image cheater_bimbo_ass_lick_3
            "Instead of offering her your cock, you turn around and offer her your ass."
            wt_image cheater_bimbo_ass_lick_4
            "Licking your butt hole keeps her happy and occupied, and gives your balls a chance to recuperate while you watch TV or check your messages."
            wt_image cheater_bimbo_ass_lick_1
            "If your clients knew how many of their visits were scheduled while Lauren's tongue was up your ass, they'd be shocked."
    return

# Slavegirl - Rename
label lauren_rename:
    wt_image lauren.image
    "As her owner, it's your prerogative to change [lauren.full_name]'s name, if you want to."
    $ title = "Do you want to change her name?"
    menu:
        "Yes":
            $ title = "What would you like her name to be?"
            $ lauren.name = renpy.input(_("What is her new name?"))
            $ lauren.suffix = renpy.input(_("What is her new title, if you want to give her one?"))
            $ title = "Does she get a prefix?"
            menu:
                "Yes":
                    $ lauren.prefix = renpy.input(_("What is her prefix?"))
                "No":
                    $ lauren.prefix = ""
            $ lauren.change_full_name(lauren.prefix, lauren.name, lauren.suffix)
            $ title = "Are you sure you want her new name to be [lauren.full_name]?"
            menu:
                "Yes":
                    pass
                "No, choose something else":
                    $ lauren.change_full_name("", "Lauren", "the Cheater")
                    jump lauren_rename
        "No":
            pass
    return

# Tell her how to address you
label lauren_your_name:
    "[lauren.name] currently refers to you as '[lauren.your_respect_name]'"
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            $ title = "How should she address you?"
            $ lauren.your_respect_name = renpy.input(_("What does she call you?"))
        "No":
            pass
    return

# Slavegirl - Choose Position For Her
label lauren_slavegirl_choose_position:
    $ title = "How do you want [lauren.name] to wait for you?"
    menu:
        "Cuffed":
            wt_image cheater_slave_position_1
            "You bind [lauren.name]'s arms and ankles with leather cuffs. It's a deceptively difficult position to maintain, standing in high heels with her feet crossed. She happily bears it, waiting for you to return."
            $ lauren.change_image('cheater_slave_position_1')
            $ lauren.position = 1
        "In latex":
            wt_image cheater_slave_position_2
            "The latex suit was bought with [lauren.name]'s own money that was in her purse when she offered herself to you. It's the only money she had that didn't go to her husband."
            "You're tempted to send him a picture of his former bride, but that might be seen as taunting, and you don't want to seem ungrateful to him after he so kindly sent her to you."
            $ lauren.change_image('cheater_slave_position_2')
            $ lauren.position = 2
        "In armbinders":
            wt_image cheater_slave_position_8
            "There was enough money left in [lauren.name]'s purse after buying a latex suit for her that you bought some armbinders, too. She looks best in them locked in the basement, where it's dark except when you turn on the light to visit."
            $ lauren.change_image('cheater_slave_position_8')
            $ lauren.position = 8
        "Ready for use":
            wt_image cheater_slave_position_3
            "As [lauren.name] so eloquently stated, she has nothing to offer you except her body. You tie her in a position that displays each of her available orifices, then you leave her. You'll come back later, when you're ready to use one of the holes."
            $ lauren.change_image('cheater_slave_position_3')
            $ lauren.position = 3
        "Ready for punishment" if dungeon.has_item(floggers):
            wt_image cheater_slave_position_4
            "[lauren.name] is an exceptionally happy slavegirl. The only thing she doesn't enjoy about servitude are the times you choose to punish her.  When the punishment is over, she goes right back to being content."
            "Providing her a reminder of a pending punishment is one of the few ways you can keep her anxious for an extended period.  As you place the cane between her teeth, she remembers how much it hurts, and wonders whether you will use it on her when you return."
            "Those thoughts should keep her mind racing until you return."
            $ lauren.change_image('cheater_slave_position_4')
            $ lauren.position = 4
        "Hogtied" if dungeon.has_item(gags):
            wt_image cheater_slave_position_5
            "You dress [lauren.name] up in some nice stockings, the sort she wore when she was a successful business woman. Then you hogtie her and leave her on a table to wait for your return."
            "The ball gag is completely unnecessary. [lauren.name] is an exceptionally obedient slavegirl and never makes a sound without permission.  The sight of the red gag in her mouth, however, completes the look."
            "As you lift her head to examine her face before leaving, you wonder how often her husband or colleagues at her work place wanted to see her gagged like this."
            $ lauren.change_image('cheater_slave_position_5')
            $ lauren.position = 5
        "Suspended" if dungeon.has_item(gags) and dungeon.has_item(suspension_gear):
            wt_image cheater_slave_position_6
            "You dress [lauren.name] up in some nice stockings, the sort she wore when she was a successful business woman. Then you connect her to the suspension gear and hoist her into the air."
            "With a gag in her mouth and no contact with the ground, [lauren.name] is completely helpless. There's literally nothing she can do except hang there until you return."
            "Her eyes go vacant and her mind drifts off into a deep subspace as soon as she leaves the ground. She's a happy slavegirl at the best of times, but she's never more intensely content to the core of her being as when she left alone like this to wait for you."
            $ lauren.change_image('cheater_slave_position_6')
            $ lauren.position = 6
        "Kneeling":
            wt_image cheater_slave_position_7
            "It's a simple, classic position for a former corporate executive who's now a simple, classic slavegirl. The heels remind you of what she was. The collar reminds her of what she is."
            $ lauren.change_image('cheater_slave_position_7')
            $ lauren.position = 7

    return

# Slavegirl - Punish Her
label lauren_slavegirl_punish:
    call forced_movement(dungeon) from _call_forced_movement_715
    summon lauren to dungeon
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    # if left in latex and you own floggers
    if lauren.position == 2 and dungeon.has_item(floggers):
        wt_image cheater_slave_position_2
        "[lauren.name] watches in resignation as you sort through your selection of floggers. She loves everything about being a slave, except this part.  But even this she accepts."
        wt_image cheater_slave_punish_1
        "Locked in her latex cocoon, she can do nothing more than close her eyes as you flog her exposed breasts ... *thwackkk*  *thwackkk*  *thwackkk*"
        wt_image cheater_slave_punish_10
        "Suitably warmed up, her breasts are ready for the next part of their ordeal."
        wt_image cheater_slave_punish_9
        "[lauren.name] watches in fear as you pick up the pinwheel and approach."
        wt_image cheater_slave_punish_11
        "Small sounds that are likely 'no, no, no' barely escape from her enclosed mouth as you touch the torture device to her skin."
        wt_image cheater_slave_punish_12
        "The pinwheel hurts a lot on any skin."
        wt_image cheater_slave_punish_3
        "Already sensitized by the flogging, the sting of the needles biting into her soon enflame the nerves of her exposed nipples."
        wt_image cheater_slave_punish_13
        "Inside her casing, Lauren alternates between screams and cries as you run the torture device back and forth, each passage increasing the fire in her breasts."
        wt_image cheater_slave_punish_14
        "Once she gets to the point of uncontrollable whimpering, you put down the pinwheel and adjust her breasts."
        wt_image cheater_slave_punish_2
        "Then you pick up the flogger, and begin a more intense, heavy beating as her whimpers turn to screams ... *THWACKK* *THWACKK* *THWACKK*"
        wt_image cheater_slave_punish_1
        "[lauren.name] floats off into subspace as the pounding and sting of the flogger mixes with the fire left behind by the pinwheel, her entire being reduced to the sensations washing through and across her breasts."
        change player energy by -energy_short notify
    # if left waiting to be punished
    elif lauren.position == 4:
        $ lauren.temporary_count = 1
        wt_image cheater_slave_position_4
        "[lauren.name] shakes as she sees you approach. She's become quite adept at reading your moods and can tell by the way you're approaching that the time for waiting for her punishment has ended, and the time for experiencing that punishment has arrived."
        wt_image cheater_slave_punish_16
        player.c "You look scared. Aren't you looking forward to serving me?"
        "She nods, and it's true: she does want to serve you. She's just terrified about what that service will entail."
        wt_image cheater_slave_punish_17
        player.c "You're a lucky slavegirl, getting to serve me by having your tits hurt."
        "*THWAPPP*"
        lauren.c "OWW!!!  Y ... yesss, [lauren.your_respect_name]!"
        wt_image cheater_slave_punish_18
        player.c "I'm also going to let you serve me by having your cunt hurt."
        "*THWAPPP*"
        lauren.c "OWW!!!  Thank you, [lauren.your_respect_name]!"
        wt_image cheater_slave_punish_15
        player.c "Isn't there something more you wanted to say to me?"
        "Through her tears, she chokes out the words. For her poor, re-wired brain, they're even heartfelt."
        lauren.c "Thank you for letting this worthless cunt amuse you with it's pain, [lauren.your_respect_name]."
        wt_image cheater_slave_punish_7
        "Hurting her does turn you on and there's no need to hide it. You let out your cock as you lower her onto the ground. She knows better than to beg with words, but she can't help but beg with her eyes at the sight of your dick."
        $ title = "Let her touch your cock before you punish her?"
        menu:
            "Yes":
                player.c "You want my cock, don't you cunt?"
                lauren.c "She nods, vigorously."
                wt_image cheater_slave_punish_19
                player.c "I'm still going to hurt you."
                "She knows, and she seeks your cock for comfort like a child seeking a security blanket."
                wt_image cheater_slave_punish_20
                "Or perhaps a baby with a soother, considering how desperately she suckles you."
                wt_image cheater_slave_punish_21
                "More than just the comfort of your cock, though, she wants the comfort of your cum and knowing she was able to serve you with her mouth."
                $ title = "Let her make you cum?"
                menu:
                    "Yes":
                        wt_image cheater_slave_punish_22
                        player.c "Show me how much you appreciate the opportunity to suffer for me."
                        lauren.c "Oh!  Thank you, [lauren.your_respect_name]!!!"
                        wt_image cheater_slave_punish_23
                        "She does her best to ignore the cane and focus on you as she gets you off with her mouth."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_slave_punish_24
                        "There's a hopefulness to her eyes as she swallows your load, her gaze still locked on yours."
                        $ title = "What now?"
                        menu:
                            "Punish her":
                                $ lauren.temporary_count = 2
                                wt_image cheater_slave_punish_25
                                player.c "Open your mouth. You've finished swallowing?"
                                wt_image cheater_slave_punish_26
                                player.c "Nothing left to keep you from suffering for me, is there?"
                                orgasm
                            "Let her go back to waiting":
                                $ lauren.temporary_count = 0
                                wt_image cheater_slave_position_4
                                player.c "Since you did such a good job serving me with your mouth, I think I'll delay your punishment for a little while longer."
                                lauren.c "'ank 'ou, 'ir!"
                                orgasm notify
                    "No":
                        wt_image cheater_slave_punish_26
                        player.c "Off.  You want my cum, maybe you'll earn it with your screams?"
            "No":
                player.c "No, cunt. You only get me to amuse me with your pain today."
                "She nods, trying her best to pretend that she's okay with your decision."
        # temp count test shuts off punishment if you let her go back to waiting after blowing you
        if lauren.temporary_count > 0:
            wt_image cheater_slave_punish_27
            "She breaks down in tears. Since you first put the cane in her mouth and told her to wait, she's been contemplating how much it will hurt when the punishment comes."
            wt_image cheater_slave_punish_8
            if lauren.temporary_count == 2:
                "She's a sobbing mess before the first blow lands. It says something about you that her crying helplessness gets you hard again as you lift the cane into the air."
            else:
                "She's a sobbing mess before the first blow lands. It says something about you that her crying helplessness gets you even harder as you lift the cane into the air."
            player.c "Time to give you something to cry about."
            wt_image cheater_slave_punish_28
            "*THWAPPP*  *THWAPPP*  *THWAPPP*"
            lauren.c "OWW!!!  OOWWW!!!  OOOOWWWWWW!!!!"
            wt_image cheater_slave_punish_29
            "She's an obedient slave. Her re-wired brain won't let her be anything but. The pain, however, speaks to an even more primitive part of her brain, one that needs to be brought in line."
            player.c "Stop flinching. Ass up and face down, slave. Don't you dare move again without permission."
            wt_image cheater_slave_punish_30
            "The rest of the beating is easier on you and harder on her. Just as things should be ... *THWAPPP*  *THWAPPP*  *THWAPPP*"
            lauren.c "OOOOWWWWWW!!!!  OOOOOWWWWWWW!!!!  OOOOOOWWWWWWWWW!!!!!"
            "When you tire of listening to her scream, you can deposit whatever bodily fluids you want on her. She'll be ecstatic to receive anything other than another blow from the cane."
            $ lauren.change_image('cheater_slave_position_1')
            $ lauren.position = 1
            $ lauren.temporary_count = 0
            change player energy by -energy_short notify
    # hogtied
    elif lauren.position == 5 and dungeon.has_item(floggers):
        wt_image cheater_slave_position_5
        "The position you left [lauren.name] in doesn't easily lend itself to punishment."
        wt_image cheater_slave_punish_42
        "Fortunately, she has excessively sensitive feet.  Her body tenses up and she starts whimpering as soon as you touch them."
        lauren.c "nnn  nnn  nnn"
        player.c "What's that?  You're happy that I'm going to amuse myself by making you suffer?  That's nice, but all that really matters is that I'm happy about it."
        "You pick up a strap ..."
        wt_image cheater_slave_punish_43
        "... and bring it down hard on the sole of her foot ... *SLAPPP*  *SLAPPP*  *SLAPPP*"
        lauren.c "NNNNNN   NNNNNNN   NNNNNNNNN"
        "You continue the punishment until she's a blubbery, tearful mess.  Which doesn't take much effort or all that long, given how strongly she reacts to having her feet tortured"
        wt_image cheater_slave_punish_44
        player.c "I'm going to give you some time to cry it out while I watch some TV.  If there's nothing good on, I'll work on your other foot."
        change player energy by -energy_very_short notify
    # if left in suspension gear
    elif lauren.position == 6:
        wt_image cheater_slave_position_6
        "The position you left [lauren.name] in is fine for waiting ..."
        wt_image cheater_slave_suspend_8
        "... and for the occasional spanking ... *smack* ..."
        lauren.c "nnnn"
        wt_image cheater_slave_suspend_9
        "... but needs adjustment for proper punishment."
        wt_image cheater_slave_suspend_1
        "You re-tie her, upside down, giving you easier access to her vulnerable parts. But it's only when you place her old friends, the elastic bands, on her feet, that she starts to cry."
        wt_image cheater_slave_suspend_2
        "You check her pussy and confirm it's dry. Despite her re-wired brain, she's never become excited by pain. That's fine with you. It means her tortures are pure torture, undiluted by any sense of masochistic pleasure."
        wt_image cheater_slave_suspend_3
        "The pain from the elastic bands is something else she's never learned to adjust to. Maybe it was all those years wearing business heels, but she has exceedingly sensitive feet ... *THWAPPP*"
        lauren.c "NNNNNNN"
        wt_image cheater_slave_suspend_6
        "It's such a simple system: pull the bands back ..."
        wt_image cheater_slave_suspend_3
        "... then release them ... *TTHHHWWAAAAPPPP!!!!*  Yet it leaves her thrashing in her bonds, screaming into the ball gag as the tears run down her face. "
        lauren.c "NNNNNNNNNNNN!!!!"
        wt_image cheater_slave_suspend_6
        "It takes so little effort, you could keep this up for hours ... *TTHHHWWAAAAPPPP!!!!*"
        wt_image cheater_slave_suspend_3
        "... and amazingly, she can scream just as long."
        lauren.c "NNNNNNNNNNNN!!!!"
        wt_image cheater_slave_suspend_7
        "When you tire of the sounds that escape her ball-gagged mouth, you place your hands on her throat."
        wt_image cheater_slave_suspend_4
        "The panic she experiences as you grip her in this way brings the crying and the screaming to a halt."
        wt_image cheater_slave_suspend_5
        "She takes the rest of her punishment in relative quiet. She covers the floor with her tears and drool, but tries hard to suppress the screams of agony ... *TTHHHWWAAAAPPPP!!!!* *TTHHHWWAAAAPPPP!!!!* *TTHHHWWAAAAPPPP!!!!*"
        lauren.c "nnnnnnnnn  nnnnnnnnn  nnnnnnnnn"
        change player energy by -energy_short notify
    # if in armbinders
    elif lauren.position == 8 and dungeon.has_item(floggers):
        wt_image cheater_slave_punish_45
        player.c "Have you been lonely, waiting here for a chance to serve me?"
        lauren.c "Oh yes, [lauren.your_respect_name]!!"
        player.c "Would you like a chance to serve me now?"
        lauren.c "Yes, [lauren.your_respect_name]!!  Please, [lauren.your_respect_name]!!!"
        player.c "You're in luck. I'm in the mood to punish you.  Does that make you happy?"
        wt_image cheater_slave_punish_46
        lauren.c "Yes, [lauren.your_respect_name].  Thank you, [lauren.your_respect_name]."
        player.c "You look disappointed.  When I asked if you'd like to serve me, you didn't think I meant sexually, did you?"
        lauren.c "Yes, [lauren.your_respect_name], I did.  I'm sorry, [lauren.your_respect_name].  This worthless cunt can be very stupid, [lauren.your_respect_name]."
        wt_image cheater_slave_punish_47
        player.c "I'll give you a chance to redeem yourself.  Which of these instruments do you think I should use on you?"
        lauren.c "Whichever one would amuse you the most, [lauren.your_respect_name]."
        player.c "And what one do you think that would be?"
        wt_image cheater_slave_punish_46
        lauren.c "The one that causes me the most pain, [lauren.your_respect_name]?"
        wt_image cheater_slave_punish_45
        player.c "Very good.  You're not always a stupid cunt, are you?"
        lauren.c "Thank you for saying so, [lauren.your_respect_name]."
        wt_image cheater_slave_punish_48
        "*THWAPPP*  *THWAPPP*  *THWAPPP*"
        lauren.c "OWW!!!  OOWWW!!!  OOOOWWWWWW!!!!"
        wt_image cheater_slave_punish_50
        "*THWAPPP*  *THWAPPP*  *THWAPPP*"
        lauren.c "OOOOWWWWWW!!!!  OOOOOWWWWWWW!!!!  OOOOOOWWWWWWWWW!!!!!"
        wt_image cheater_slave_punish_49
        player.c "You're a lucky slavegirl, being allowed to serve me like this.  Maybe if you're really lucky, I'll amuse myself with you like this again tomorrow."
        lauren.c "Ooowwww  ...  yes, [lauren.your_respect_name].  Thank you, [lauren.your_respect_name]."
        change player energy by -energy_short notify
    # for other positions, if have flogger
    elif dungeon.has_item(floggers):
        wt_image cheater_slave_punish_31
        "The way you left [lauren.name] doesn't lend itself to any particular form of punishment, so you re-position her. She's learned to read you very well, and begins to cry as you re-arrange her."
        wt_image cheater_slave_punish_4
        "She cries even more as you bring out the cane. At least you didn't make her wait for the punishment. She hopes that means you haven't spent too much time contemplating her beating, and won't make her hurt too much this time."
        $ title = "How much do you want to make her hurt?"
        menu:
            "A lot":
                $ lauren.temporary_count = 0
                wt_image cheater_slave_punish_32
                "She enjoys every part of bring a slave except this. She starts to shake and cries out as you cane her back ... *THWAPPP*  *THWAPPP*  *THWAPPP*"
                lauren.c "OWW!!!"
                wt_image cheater_slave_punish_33
                player.c "Don't you like it when I hurt you?"
                "She doesn't, but her re-wired brain won't admit that, even to itself."
                lauren.c "Y ... yes, [lauren.your_respect_name]. Thank you for letting me amuse you with my pain."
                wt_image cheater_slave_punish_34
                player.c "You're welcome."
                "It hurts when you bring the cane down on her ass ... *THWAPPP*"
                lauren.c "OOWWW!!!"
                wt_image cheater_slave_punish_35
                "... and even more when you strike her belly ... *THWAPPP*"
                lauren.c "OOOWWWW!!!"
                wt_image cheater_slave_punish_37
                "... but it's when you cane her inner thighs that she completely loses it ... *THWAPPP*"
                lauren.c "OOOOWWWWWW!!!!"
                player.c "Did you say something?"
                wt_image cheater_slave_punish_36
                "*THWAPPP*"
                lauren.c "OOOOOWWWWWWWW!!!!"
                wt_image cheater_slave_punish_38
                player.c "What was that?"
                wt_image cheater_slave_punish_6
                "*THWAPPP*"
                lauren.c "OOOOOWWWWWWWW!!!!  THANK YOU SIRRRR!!"
                wt_image cheater_slave_punish_37
                "You continue to beat her and she continues to scream, but eventually all good things must come to an end ..."
                wt_image cheater_slave_punish_36
                "Eventually she screams herself hoarse, leaving only her tears to tell to give evidence to how much pain she's in."
                wt_image cheater_slave_punish_40
            "A little":
                wt_image cheater_slave_punish_33
                player.c "Are you ready to amuse me?"
                lauren.c "Y ... yes, [lauren.your_respect_name]."
                wt_image cheater_slave_spank_2
                "She cries out in surprise - and joy - when she feels your hand on her instead of the cane ... *smack*"
                lauren.c "Oh!  Oh, thank you, [lauren.your_respect_name]!!"
                wt_image cheater_slave_spank_3
                "She's a little less happy as you pick up the intensity ... *SMACK* *SMACK* *SMACK*"
                wt_image cheater_slave_spank_4
                lauren.c "Ow! Ow!! Oww!!"
                wt_image cheater_slave_spank_6
                "But even at your hardest, your hand can't hurt her as much as the cane.  Not that you don't try ... *SMACK* *SMACK* *SMACK*"
                lauren.c "OW!  OW!  OOWWW!!"
                wt_image cheater_slave_spank_5
            "You'll figure it out as you go":
                $ lauren.temporary_count = 1
                player.c "Count the strokes for me.  Let's see how high I go before I tire of hearing you scream."
                lauren.c "Y .. yes, [lauren.your_respect_name]."
                wt_image cheater_slave_punish_5
                lauren.c "OWW!!  1 [lauren.your_respect_name]!"
                wt_image cheater_slave_punish_39
                $ title = "Cane her again?"
                menu menu_lauren_slave_punish_caning_menu:
                    "Give her another":
                        $ lauren.temporary_count += 1
                        wt_image cheater_slave_punish_5
                        lauren.c "OWW!!  [lauren.temporary_count] [lauren.your_respect_name]!"
                        wt_image cheater_slave_punish_39
                        jump menu_lauren_slave_punish_caning_menu
                    "That's enough":
                        wt_image cheater_slave_punish_4
                        player.c "There.  Only [lauren.temporary_count]. That wasn't too many, was it?"
                        lauren.c "No, [lauren.your_respect_name].  Thank you, [lauren.your_respect_name]."
        $ title = "What now?"
        menu:
            "Let her know another punishment is coming soon":
                wt_image cheater_slave_punish_41
                player.c "That's it for today, but don't fret.  I'll be back to punish you more, soon."
                $ lauren.change_image('cheater_slave_position_4')
                $ lauren.position = 4
            "Let her recover":
                wt_image cheater_slave_punish_33
                player.c "That's it for today.  When you've recovered, you can go back to waiting obediently for me."
                lauren.c "Yes, [lauren.your_respect_name].  Thank you, [lauren.your_respect_name]."
                $ lauren.change_image('cheater_slave_position_1')
                $ lauren.position = 1
        $ lauren.temporary_count = 0
        change player energy by -energy_short notify
    # for other positions, if no floggers
    else:
        wt_image cheater_slave_spank_1
        "You should pick up some equipment if you want to punish [lauren.name] properly. In the meantime, your hand will do."
        wt_image cheater_slave_spank_2
        "She doesn't like to be punished, but she loves physical contact with you, and she's clearly appreciating the spanking ... *smack*  *smack*  *smack*"
        lauren.c "oooo"
        wt_image cheater_slave_spank_3
        "You pick up the intensity until there's a change in her exclamations ... *SMACK*  *SMACK*  *SMACK*"
        wt_image cheater_slave_spank_4
        lauren.c "Ow! Ow!! Oww!!"
        wt_image cheater_slave_spank_6
        "After that, she experiences the punishment side of her punishment ... *SMACK*  *SMACK*  *SMACK*"
        lauren.c "OW!  OW!  OOWWW!!"
        wt_image cheater_slave_spank_5
        "When you finish, she's both happy that the ordeal is over, and disappointed that she now needs to wait for her next opportunity to serve - and be touched by - you."
        change player energy by -energy_short notify
    call character_location_return(lauren) from _call_character_location_return_474
    return

# Slavegirl - Use Her
## note: consider adding an ass lick option
label lauren_slavegirl_use:
    call forced_movement(dungeon) from _call_forced_movement_716
    summon lauren to dungeon
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ title ="How do you want to use her?"
    menu:
        "In her mouth":
            $ lauren.temporary_count = 1
            # in latex
            if lauren.position == 2:
                wt_image cheater_slave_position_2
                "You need to remove the outer layer of [lauren.name]'s suit to give you access to her mouth."
                wt_image cheater_slave_bj_4
                "You're never sure whether she's pleased or disappointed when you pull down the top part of her cocoon."
                wt_image cheater_slave_bj_5
                "However, there's no question that she's pleased to see your cock. She leans forward greedily to take you into her mouth as soon as you unzip your pants."
                wt_image cheater_slave_bj_6
                player.c "Stop"
                wt_image cheater_slave_bj_7
                player.c "Why was your mouth on my cock?"
                lauren.c "Oh, [lauren.your_respect_name] ... I wanted to please you, [lauren.your_respect_name]."
                player.c "You'll please me by being obedient. Why did you put your mouth on my cock before I told you to?"
                lauren.c "[lauren.your_respect_name] ... this greedy cunt loves to feel your cock in it's mouth and so wanted to pleasure you, it forgot it's place, [lauren.your_respect_name]."
                $ title = "What do you do?"
                menu:
                    "Let her suck you":
                        wt_image cheater_slave_bj_8
                        player.c "You're going to get to suck my cock, because I want to use your mouth right now. But I'm not happy about you forgetting your place."
                        wt_image cheater_slave_bj_9
                        "[lauren.name] hates disappointing you. She's so distraught she can barely enjoy the feel of your dick in her mouth. She tries desperately to give you the best blow job she can to make up for her transgression."
                        wt_image cheater_slave_bj_10
                        "Even as you empty your load down her throat, she worries about whether she's done enough to deserve to be your slave."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_slave_position_2
                        "She'll fret about that for hours, zipped back up in the outer layer of her latex suit."
                        $ lauren.swallow_count += 1
                    "Flog her while she sucks you" if dungeon.has_item(floggers):
                        wt_image cheater_slave_bj_8
                        player.c "You're going to get to suck my cock, because I want to use your mouth right now. But for forgetting your place, I'm going to punish you while I use your mouth."
                        wt_image cheater_slave_bj_9
                        "It's a perfectly sensible decision from her perspective. And while she hates being punished, she knows she deserves it, and sticks her bum out to receive the lashes from the flogger you pick up."
                        wt_image cheater_slave_bj_11
                        "Even though it hurts, she's careful not to bite down as you flog her ass .... *thwackkk*  *thwackkk*  *thwackkk*"
                        wt_image cheater_slave_bj_12
                        "And in between each lash, she uses her mouth, lips and tongue to give you the best blow job she can."
                        wt_image cheater_slave_bj_13
                        "It's what slaves are for - to suffer and to serve. She feels so much more fulfilled than she ever did in that former nightmare world when she had to make decisions about the fate of a corporation ... *thwackkk*  *thwackkk*  *thwackkk*"
                        wt_image cheater_slave_bj_10
                        "Now she gets to focus on important things, like the pleasure of feeling your hard dick in her mouth, and holding still as you empty your load down her throat."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_slave_position_2
                        "She'll think about that for hours, zipped back up in the outer layer of her latex suit. Did she suck you as well as she could have? Did she take her punishment the best way a slave can? How could she serve you better?"
                        $ lauren.swallow_count += 1
                    "Take your cock away":
                        $ lauren.temporary_count = 0
                        wt_image cheater_slave_bj_4
                        "It's the worst punishment you could inflict on her."
                        wt_image cheater_slave_position_2
                        "As you zip her back into the outer layer of latex, she knows that not only has she lost the opportunity to feel your cock inside her, she's lost the opportunity to please you, too."
            # ready for use
            elif lauren.position == 3:
                wt_image cheater_slave_position_3
                "From the moment you put her in this position, [lauren.name]'s cunt has been drenching itself in anticipation of receiving your cock. The smell of her arousal is almost overpowering as you approach her."
                wt_image cheater_slave_bj_3
                "As amusing as the o-ring is to look at, she does a better job of sucking your cock when she can close her mouth around it."
                wt_image cheater_slave_bj_14
                "If she has any disappointment that you ignore her dripping cunt as you remove her gag, she tries not to show it."
                wt_image cheater_slave_bj_15
                "Mouth open and tongue out, she leans forward eagerly, as far as her bonds allow her."
                wt_image cheater_slave_bj_16
                "Eventually you move close enough to let her reach you."
                wt_image cheater_slave_bj_17
                "Considering how aroused she is, you're shocked she's able to control herself from closing her mouth around you. She can't, however, keep from licking the underside of your cockhead as she begs you with her eyes."
                player.c "You want to suck me cock, don't you?"
                lauren.c "Yes, [lauren.your_respect_name].  Please, [lauren.your_respect_name]?"
                player.c "Have you done anything to deserve to get to suck my cock?"
                lauren.c "No, [lauren.your_respect_name]. I'm a worthless cunt. I just hope you want to use this worthless cunt's worthless mouth, [lauren.your_respect_name]?"
                $ title = "Do you still want to use her mouth?"
                menu:
                    "Tease her, then let her suck you":
                        player.c "Did I tell you you could lick my cock?"
                        wt_image cheater_slave_bj_15
                        lauren.c "No, [lauren.your_respect_name]!  I'm sorry, [lauren.your_respect_name]!!"
                        player.c "Did I tell you to stop licking my cock?"
                        wt_image cheater_slave_bj_17
                        lauren.c "No, [lauren.your_respect_name]!  I'm sorry, [lauren.your_respect_name]!!"
                        player.c "Did I tell you you could look at me?"
                        wt_image cheater_slave_bj_16
                        lauren.c "No, [lauren.your_respect_name]!  This worthless cunt is so sorry, [lauren.your_respect_name]!!"
                        player.c "Then I think it should make it up to me."
                        lauren.c "Yes, [lauren.your_respect_name]!  Thank you, [lauren.your_respect_name].  What should I do, [lauren.your_respect_name]??"
                        player.c "Sucking my cock would be a good start."
                        wt_image cheater_slave_bj_17
                        lauren.c "Oh!!!  Yes, [lauren.your_respect_name]!  Thank you, [lauren.your_respect_name]!!"
                        wt_image cheater_slave_bj_2
                        "It's possible she experiences a mini-orgasm as soon as she's allowed to wrap her lips around your dick. It's certain she experiences an intense one when she succeeds in coaxing your sperm out of your balls and down her throat."
                        player.c "[player.orgasm_text]"
                        lauren.c "nnnnnnnn"
                        $ lauren.orgasm_count += 1
                        $ lauren.swallow_count += 1
                    "No, take your cock away":
                        $ lauren.temporary_count = 0
                        wt_image cheater_slave_bj_14
                        player.c "Not today, cunt. Maybe some other day, if I'm feeling generous."
                        wt_image cheater_slave_bj_3
                        "You put the o-ring back in place and leave her alone to think about how close she was to getting to feel your dick in her mouth."
            # hogtied
            elif lauren.position == 5:
                wt_image cheater_slave_position_5
                "You can't use her mouth with that ball gag in it."
                wt_image cheater_slave_bj_18
                "Once you remove the gag, however, she happily worships your balls ..."
                wt_image cheater_slave_bj_19
                "... and your cock."
                wt_image cheater_slave_bj_20
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_position_5
                "Then the gag goes back in until the next time you want her mouth."
                $ lauren.swallow_count += 1
            # suspended
            elif lauren.position == 6:
                wt_image cheater_slave_bj_21
                "First you need to remove her ball gag ..."
                wt_image cheater_suspension_7
                "... then you can put her to work pleasuring your cock."
                wt_image cheater_suspension_14
                "[lauren.name] loves the opportunity to feel you in her mouth ..."
                wt_image cheater_suspension_16
                "... even if you sometimes cut off her air supply to watch her struggle as you cum."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_bj_21
                "Then the gag goes back in until the next time you want her mouth."
                wt_image cheater_slave_position_6
                "And she goes back to waiting."
                $ lauren.swallow_count += 1
            # any other position
            else:
                wt_image cheater_slave_bj_22
                "You bind [lauren.name]'s arms behind her and place her on the floor between your feet. She gazes longingly at your cock as you unzip your pants."
                $ title = "How do you want to use her mouth?"
                menu:
                    "Allow her to pleasure you":
                        wt_image cheater_slave_bj_23
                        "[lauren.name] stretches out happily for your cock as you step close."
                        wt_image cheater_slave_bj_24
                        "She looks up at you in adoration as she sucks you with an endearing combination of tenderness and abandon."
                        wt_image cheater_slave_bj_25
                        "Even when you pull her hair to the point of hurting, she never stops looking at you with her big, adoring puppy dog eyes."
                    "Tease her before she can suck it":
                        wt_image cheater_slave_bj_22
                        player.c "Are you looking at something?"
                        lauren.c "Your cock, [lauren.your_respect_name]."
                        player.c "Why?"
                        wt_image cheater_slave_bj_26
                        lauren.c "This worthless cunt is hoping you're going to put it in my worthless mouth, [lauren.your_respect_name].  Please?"
                        player.c "What will you do if I put it in your mouth?"
                        wt_image cheater_slave_bj_27
                        "Instead of answering, she shows you, using your finger as a proxy."
                        wt_image cheater_slave_bj_28
                        player.c "Are you going to make that much of a slobbery mess on my cock?"
                        lauren.c "Yes, [lauren.your_respect_name].  If you'll let me, [lauren.your_respect_name]?  Please??"
                        player.c "I'm going to put my cock in your mouth, but no sucking it until I give you permission."
                        lauren.c "Oh!  Thank you, [lauren.your_respect_name]!!"
                        wt_image cheater_slave_bj_29
                        "You wouldn't think this would be difficult, but for [lauren.name], having your cock right there but not being allowed to suck it is nearly torture."
                        wt_image cheater_slave_bj_30
                        "And when you stroke your cock along her lips, she trembles and shakes from the strain of having your cock so close but off limits."
                        wt_image cheater_slave_bj_31
                        "When you finally give her permission to close her mouth, she trembles and shakes for a new reason, as a small orgasm ripples through her from the pleasure of finally being allowed to give you pleasure."
                        wt_image cheater_slave_bj_24
                        "She doesn't let her  orgasm interfere with her dedication to bringing you that pleasure. She suckles your cock with joyful abandon, her eyes locked on yours."
                        $ lauren.orgasm_count += 1
                    "Use it as a fuck hole":
                        wt_image cheater_slave_bj_26
                        player.c "Are you looking at something?"
                        lauren.c "Your cock, [lauren.your_respect_name]."
                        player.c "Why?"
                        lauren.c "This worthless cunt is hoping you're going to put it in my worthless mouth, [lauren.your_respect_name]. Please?"
                        wt_image cheater_slave_bj_32
                        player.c "This worthless mouth? I don't think this worthless mouth knows how to please a cock."
                        lauren.c "Oh!  No, Thir.  But thith worthleth mouth will twy very hard to pleathe you, Thir!!"
                        wt_image cheater_slave_bj_33
                        player.c "What this worthless mouth will do is hold itself open while I use it as a fuck hole, which is more than it deserves."
                        lauren.c "Oh!  Yeth, Thir!  Thank you, Thir!!"
                        wt_image cheater_slave_bj_34
                        "[lauren.name] aches to be able to close her mouth and blow you properly, but if the feel of your cock thrusting deep into her throat and along her tongue is all she's allowed, she's content with that."
                        wt_image cheater_slave_bj_35
                        "And when you cut off her air supply and pull her hair till it hurts, she's even more content that you found a way to amuse yourself with her."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image cheater_slave_bj_36
                        "[lauren.name] closes her in joy and savors the taste of your sperm filling her mouth and dripping down the back of her throat."
                        player.c "[player.orgasm_text]"
                        $ lauren.swallow_count += 1
                    "On her face":
                        wt_image cheater_facial_8
                        "[lauren.name] loves the feeling of your cum in her mouth, so you know she's disappointed when you release your seed onto her face."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_facial_9
                        "She hides her disappointment well, though, looking up at you in contentment as your cum drips down her cheek. It feels good to be of use, and she bites her lip as a quiver of excitement throbs through her."
                        $ lauren.facial_count += 1
            # trigger stat changes if action not interrupted
            if lauren.temporary_count == 1:
                $ lauren.temporary_count = 0
                $ lauren.blowjob_count += 1
                orgasm notify
        "From behind":
            $ lauren.temporary_count = 1
            # in latex
            if lauren.position == 2:
                wt_image cheater_slave_position_2
                "You need to strip off the outer layer of her latex suit before you can even access her sex."
                wt_image cheater_slave_behind_4
                "As you do, you find her already wet and moaning at your touch."
                lauren.c "oooo"
                wt_image cheater_slave_behind_5
                "She moans even louder as you push yourself inside her."
                lauren.c "oooooo  ...  Thank you, [lauren.your_respect_name]!!"
                wt_image cheater_slave_behind_6
                "The feeling of being used by you and filled by you is intensely satisfying, and a few hard slaps on her ass don't cool her ardor ... *smack*  *smack*"
                lauren.c "oooooo"
                wt_image cheater_slave_behind_7
                "And if anything, pulling hard on her hair just makes it worse."
                lauren.c "oooooooo"
                wt_image cheater_slave_behind_8
                "Despite the lack of contact on her clit, she's so aroused by the experience of serving as your fuck toy that she climaxes loudly."
                lauren.c "Aaahhhh!!!!"
                "You're not far behind her."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_punish_9
                "When you're done, you zip her back up, your fluids safely sealed up inside her."
                $ lauren.orgasm_count += 1
            # ready for use
            elif lauren.position == 3:
                wt_image cheater_slave_position_3
                "From the moment you put her in this position, [lauren.name]'s cunt has been drenching itself in anticipation of receiving your cock."
                wt_image cheater_slave_bj_3
                "The smell of her arousal is almost overpowering as you approach her."
                wt_image cheater_slave_behind_3
                "As you position yourself behind her, her hips twitch at the prospect of getting fucked. If you put your dick inside her right now, she'll likely cum immediately."
                wt_image cheater_slave_behind_20
                "So you rebind her in a new position in an effort to cool her ardor."
                $ title = "What now?"
                menu:
                    "Fuck her in this position":
                        wt_image cheater_slave_behind_21
                        player.c "Try not to cum as soon as I put my cock into you?"
                        "She nods, and you're sure she means it."
                        wt_image cheater_slave_behind_22
                        "But she's moaning through her gag as she watches you take your dick out ..."
                        lauren.c "nnnnnn"
                        wt_image cheater_slave_behind_16
                        "... and her ass is wiggling as you step behind her ..."
                        wt_image cheater_slave_behind_2
                        "... and if she doesn't cum as soon as you penetrate her, it's pretty darn close."
                        lauren.c "NNNNNNN"
                        wt_image cheater_slave_behind_17
                        "She was kept in such an aroused state, waiting to be used, that the whole fuck becomes almost one, continuous orgasm from her."
                        lauren.c "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
                        wt_image cheater_slave_behind_19
                        "It's not long before the continual spasming of her body around your cock gets you off, too."
                        player.c "[player.orgasm_text]"
                        $ lauren.orgasm_count += 1
                    "Hurt her before you fuck her":
                        wt_image cheater_slave_behind_21
                        player.c "I was thinking about fucking you, but your cunt is so soppy wet, I couldn't possibly enjoy myself.  If I hurt you, though, it might take your mind off of sex.  Should we try?"
                        wt_image cheater_slave_behind_20
                        "She nods vigorously."
                        wt_image cheater_slave_behind_25
                        "You do your best to distract her from the thought of getting fucked ..."
                        lauren.c "nnnnnnn"
                        wt_image cheater_slave_behind_26
                        "... but there's only so much you can do to hurt her with your hands and the items close at hand."
                        wt_image cheater_slave_behind_16
                        "She was left anticipating sex for so long her hips twitch every time you move behind her ..."
                        wt_image cheater_slave_behind_2
                        "... so eventually you give up and put your dick in her, to the sound of her immediate orgasm."
                        lauren.c "NNNNNNN"
                        wt_image cheater_slave_behind_17
                        "She keeps orgasming as you fuck her, and it's impossible to tell if it's a series of orgasms or just one long drawn out climax."
                        lauren.c "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
                        wt_image cheater_slave_behind_19
                        "Either way, the continual spasming of her body around your cock soon gets you off, too."
                        player.c "[player.orgasm_text]"
                        $ lauren.orgasm_count += 1
                    "Cane her before you fuck her" if dungeon.has_item(floggers):
                        wt_image cheater_slave_behind_21
                        player.c "I was thinking about fucking you, but your cunt is so soppy wet, I couldn't possibly enjoy myself.  If I hurt you, though, it might take your mind off of sex.  Would you like me to get a cane and hurt you with it?"
                        wt_image cheater_slave_behind_20
                        "She nods vigorously."
                        player.c "You would?  You want me to hurt you and see if we can dry up your greedy cunt to the point I'd want to fuck it?"
                        lauren.c "nnn, nnnn!!"
                        wt_image cheater_slave_behind_23
                        "Part of the plan works well.  The cane does hurt ..."
                        wt_image cheater_slave_behind_24
                        "... *THWAPPP*  *THWAPPP*  *THWAPPP*"
                        lauren.c "NNNNNNN  ...  NNNNNNN  ...  NNNNNNN"
                        wt_image cheater_slave_behind_27
                        "Before long, she's a crying, sobbing mess and you can no longer smell any arousal from between her legs."
                        lauren.c "NNNN  NNNNN  NNNNN"
                        wt_image cheater_slave_behind_22
                        "As soon as she sees you take your dick out, though, she gets wet again."
                        wt_image cheater_slave_behind_16
                        "At least she's only excited now, not sloppy drippy."
                        wt_image cheater_slave_behind_2
                        "She still cums almost as soon as you penetrate her. She was left anticipating sex for so long that the caning barely took the edge off her need."
                        lauren.c "NNNNNNN"
                        wt_image cheater_slave_behind_17
                        "But at least you can enjoy fucking her in this state."
                        wt_image cheater_slave_behind_19
                        player.c "[player.orgasm_text]"
                        $ lauren.orgasm_count += 1
                    "Change your mind and leave her like this without fucking her":
                        wt_image cheater_slave_behind_21
                        player.c "I was thinking about fucking you, but your cunt is so soppy wet, I couldn't possibly enjoy myself."
                        wt_image cheater_slave_behind_22
                        "She groans in frustration and self-loathing as she watches you go. She failed to please you and lost an opportunity to feel your cock in her, and she knows it's all her fault."
                        wt_image cheater_slave_behind_20
                        "When she's had a few hours to despise herself for having such a greedy cunt, you'll put her back in the ready for use position so she can get overstimulated again."
                        $ lauren.temporary_count = 0
                # finish text if fucked her
                if lauren.temporary_count == 1:
                    wt_image cheater_slave_position_1
                    "You stand her back up before you go. Leaving her in a state of constant arousal can't be good for her long-term health."
                    $ lauren.change_image('cheater_slave_position_1')
                    $ lauren.position = 1
            # suspended
            elif lauren.position == 6:
                wt_image cheater_slave_behind_9
                "[lauren.name]'s not sure what you intend when you spin her around."
                wt_image cheater_slave_bj_21
                "Or when you remove her ball gag."
                wt_image cheater_slave_behind_10
                "So she's exceedingly happy when she feels you penetrate her."
                lauren.c "Oh, [lauren.your_respect_name]!  Thank you, [lauren.your_respect_name]!!"
                wt_image cheater_slave_behind_11
                "And even more happy when she shudders to a quick climax as you fuck her."
                lauren.c "Aaahhhh!!!!"
                wt_image cheater_slave_behind_12
                "The trembling of her suspended body around your cock as she cums helps make your own orgasm feel all that much better"
                player.c "[player.orgasm_text]"
                lauren.c "oooo"
                wt_image cheater_slave_position_6
                "She sways gently back and forth after you put the gag back in and leave her, basking in her post-orgasm glow and a sense of contentment that she was able to serve you."
                $ lauren.orgasm_count += 1
            # in armbinders
            elif lauren.position == 8:
                wt_image cheater_slave_punish_45
                player.c "Have you been lonely, waiting here for a chance to serve me?"
                lauren.c "Oh!  Yes, [lauren.your_respect_name]!!"
                player.c "Would you like a chance to serve me now?"
                lauren.c "Yes, [lauren.your_respect_name]!!  Please, [lauren.your_respect_name]!!!"
                wt_image cheater_slave_behind_13
                "Her hips start twitching in anticipation even before you slide the tip of your dick into her rapidly wetting sex."
                lauren.c "oooo  ...  thank you, [lauren.your_respect_name]!"
                wt_image cheater_slave_behind_14
                "It's not as easy for her to cum in this position, with no pressure on her clit, and you pulling her hair to try and make her think about that instead of the feeling of your cock inside her."
                lauren.c "oooooo"
                wt_image cheater_slave_behind_15
                "Despite that, the joy of being used by you this way is so great she still cums before you do.  Not a lot before you do, though."
                lauren.c "Aaahhhh!!!!"
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_position_8
                "She's a very content slavegirl when you leave her."
                $ lauren.orgasm_count += 1
            # any other position
            else:
                wt_image cheater_slave_behind_1
                "You lock [lauren.name] into position, ass up, head down. The smell of her arousal fills the room, as her pussy swells and wets in anticipation of the fucking to come."
                wt_image cheater_slave_behind_16
                "Her hips tremble as you step behind her ..."
                wt_image cheater_slave_behind_17
                "... and she lets out a loud moan when the head of your cock penetrates her."
                lauren.c "oooo  ...  thank you, [lauren.your_respect_name]!"
                wt_image cheater_slave_behind_2
                "She can't quite see you from this position, but she tries her best to look at you. Despite the lack of contact on her clit, the feeling of being used by you, and filled by you, is so intensely satisfying that she quickly builds towards orgasm."
                wt_image cheater_slave_behind_18
                "Sharp slaps on her ass bring her down from the brink a couple of times, but they soon lose their effectiveness ... *smack*  *smack*  *smack*"
                lauren.c "Ow!  ...  Ow!  ...  oooooo"
                wt_image cheater_slave_behind_2
                "When the orgasm hits her, its like a long continuing wave.  With no pain to distract her from the pleasure, she becomes a quivering, shaking climax machine.  It's impossible to say whether she experiences one long, extended orgasm or a series of orgasms back to back to back."
                lauren.c "Aaahhhh  ...  Aaahhhh  ...  Aaahhhh!!!!"
                wt_image cheater_slave_behind_19
                "Regardless, her body throbs and clenches around your cock as you empty your load inside her. "
                player.c "[player.orgasm_text]"
                $ lauren.orgasm_count += 1
            # trigger stat changes if action not interrupted
            if lauren.temporary_count == 1:
                $ lauren.temporary_count = 0
                $ lauren.sex_count += 1
                orgasm notify
        "On her back":
            wt_image cheater_slave_sex_12
            "As you tie [lauren.name] into position, legs spread, her body trembles in anticipation.  She loves the feeling of your cock inside her cunt."
            wt_image cheater_slave_sex_3
            $ title = "What now?"
            menu:
                "Just fuck her":
                    wt_image cheater_slave_sex_1
                    "She watches excitedly as you take out your cock ..."
                    wt_image cheater_slave_sex_13
                    "... and by the time you press the head of your dick against her, she's sopping wet."
                    wt_image cheater_slave_sex_4
                    "You've tied her hands to her thighs to prevent her from touching herself while you fuck her, but you know that'll only delay her orgasm, not prevent it."
                    wt_image cheater_slave_sex_5
                    lauren.c "Oh, [lauren.your_respect_name]!  Thank you, [lauren.your_respect_name]!!  Oooohh!!"
                    wt_image cheater_slave_sex_14
                    "Sure enough, she quickly cums like a banshee, screaming and bucking against her bonds.  Fortunately, that feels pretty good for you, too."
                    lauren.c "AAAHHHH!!!"
                    wt_image cheater_slave_sex_5
                    player.c "[player.orgasm_text]"
                "Cane her first" if dungeon.has_item(floggers):
                    wt_image cheater_slave_sex_15
                    player.c "You're wet."
                    lauren.c "Yes, [lauren.your_respect_name].  This greedy cunt is eager to serve you, [lauren.your_respect_name]."
                    wt_image cheater_slave_sex_6
                    player.c "This greedy cunt needs discipline."
                    "*smack*"
                    lauren.c "Ow!  Yes, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_16
                    "*THWAPPP*  *THWAPPP*  *THWAPPP*"
                    lauren.c "Ooowww!!  Thank you for discipling me, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_17
                    player.c "I'm not sure that discipline will be enough.  Maybe these clamps will keep you from getting excited before I tell you to?"
                    wt_image cheater_slave_sex_7
                    lauren.c "Nnnnn  ...  yes, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_11
                    player.c "Well that didn't work, you're soaked again.  Perhaps we need to apply the discipline directly to the offending area and remind this greedy cunt what happens when it gets wet without permission."
                    wt_image cheater_slave_sex_9
                    "*THWAPPP*  *THWAPPP*  *THWAPPP*"
                    lauren.c "OOOOWWWWWW!!!!  OOOOOWWWWWWW!!!!  OOOOOOWWWWWWWWW!!!!!"
                    wt_image cheater_slave_sex_18
                    player.c "That didn't dry you up much, but at least the greedy cunt is too sore to cum while it's being fucked now, isn't it?"
                    lauren.c "Nnnnn ... [lauren.your_respect_name]??  Please, [lauren.your_respect_name]????"
                    wt_image cheater_slave_sex_8
                    player.c "The sore greedy cunt still wants to cum?"
                    lauren.c "Yes, [lauren.your_respect_name]!!  Please let this greedy cunt cum, [lauren.your_respect_name]??"
                    wt_image cheater_slave_sex_18
                    player.c "Okay, but only when I say now."
                    "Gripping the clamps, you pull them apart, stretching her labia painfully."
                    wt_image cheater_slave_sex_2
                    player.c "Now"
                    lauren.c "OOWWWWWAAHHHHHHH!!!"
                    wt_image cheater_slave_sex_19
                    "Between the pain and the orgasm, you're not even sure she realizes you're pumping your load into her as she's cumming."
                    player.c "[player.orgasm_text]"
                "Toy her first" if lauren.has_item(dildo):
                    wt_image cheater_slave_sex_15
                    player.c "You're wet."
                    lauren.c "Yes, [lauren.your_respect_name].  This greedy cunt is eager to serve you, [lauren.your_respect_name]."
                    wt_image cheater_slave_sex_6
                    player.c "This greedy cunt could be even wetter, couldn't it?"
                    lauren.c "oooo ... yes, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_17
                    player.c "Even a bit of pain from these clamps won't keep the greedy cunt from getting excited for me, will it?"
                    wt_image cheater_slave_sex_7
                    lauren.c "nnnnn  ...  no, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_10
                    player.c "Especially not when the greedy cunt has it's toy pressed against it's clit."
                    lauren.c "OOOOOOO"
                    wt_image cheater_slave_sex_20
                    player.c "The greedy cunt wasn't going to cum without permission, was it?"
                    "She grits her teeth together and shakes her head vigorously, if somewhat unconvincingly."
                    wt_image cheater_slave_sex_10
                    player.c "That's good, because you're very, very wet now, aren't you?"
                    lauren.c "OOOOOOO  ... yes, [lauren.your_respect_name], this cunt is very, very wet now!"
                    wt_image cheater_slave_sex_21
                    player.c "I can slide into this wet, wet cunt so easily it probably can't even feel me enter it?"
                    lauren.c "OOOOOOO, [lauren.your_respect_name]???  Please, [lauren.your_respect_name]??"
                    player.c "Please, what?"
                    lauren.c "Please, [lauren.your_respect_name], this greedy cunt needs to cum so so so bad, [lauren.your_respect_name]!!!"
                    wt_image cheater_slave_sex_18
                    player.c "Show me how badly you need to cum.  Cum when I say 'now'."
                    "Gripping the clamps, you pull them apart, stretching her labia painfully."
                    wt_image cheater_slave_sex_2
                    player.c "Now"
                    lauren.c "OOWWWWWAAHHHHHHH!!!"
                    wt_image cheater_slave_sex_19
                    "Between the pain and the orgasm, you're not even sure she realizes you're pumping your load into her as she's cumming."
                    player.c "[player.orgasm_text]"
                "Clamp her then fuck her":
                    wt_image cheater_slave_sex_6
                    player.c "You're wet."
                    lauren.c "Yes, [lauren.your_respect_name].  This greedy cunt is eager to serve you, [lauren.your_respect_name]."
                    wt_image cheater_slave_sex_15
                    player.c "Looking at how wet you are, I think this greedy cunt is going to cum as soon as I put my cock in it."
                    lauren.c "Ohh!  Yes, [lauren.your_respect_name]!!"
                    wt_image cheater_slave_sex_17
                    player.c "I don't want that.  Maybe these clamps will keep you from cumming until I say you can?"
                    wt_image cheater_slave_sex_7
                    lauren.c "NNNNN ... yes, [lauren.your_respect_name]!"
                    wt_image cheater_slave_sex_8
                    "It would be easier on her if you didn't play with her clit while you fuck her, but where would the fun be in making it easy?  She struggles to control her building orgasm ..."
                    wt_image cheater_slave_sex_18
                    "... then you help her out by pulling hard on the clamps just as she gets to the brink of cumming."
                    wt_image cheater_slave_sex_2
                    lauren.c "OOWWWWW!!!"
                    wt_image cheater_slave_sex_18
                    "The first two times it works ... "
                    wt_image cheater_slave_sex_2
                    "... as the pain brings her back from the brink of orgasm."
                    lauren.c "OOWWWWW!!!"
                    wt_image cheater_slave_sex_18
                    "The third time, it doesn't."
                    wt_image cheater_slave_sex_19
                    "She still screams from the pain, but climaxes at the same time ... and brings you along with her."
                    lauren.c "OOWWWWWAAHHHHHHH!!!"
                    player.c "[player.orgasm_text]"
            $ lauren.orgasm_count += 1
            $ lauren.sex_count += 1
            orgasm notify
        "Anally":
            # in latex
            if lauren.position == 2:
                wt_image cheater_slave_position_2
                "You need to strip off the outer layer of her latex suit before you can even access her ass."
                wt_image cheater_slave_behind_4
                "As you do, you find her already wet and moaning at your touch."
                lauren.c "oooo"
                wt_image cheater_slave_anal_5
                if lauren.has_tag('no_anal'):
                    "She's disappointed that you shove your cock up her dry asshole instead, but she understands that all three of her holes belong to you, regardless of what rules applied before she became your slave."
                else:
                    "She's disappointed that you shove your cock up her dry asshole instead, but she understands that all three of her holes belong to you, and she has no say in which one gets used when."
                lauren.c "Ow!!!"
                "She's your possession, and if she's a little torn and bloody after you've finished using her, the important thing is that you have fun."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_punish_9
                "She'll have plenty of time to heal after you zip her back up, your fluids safely sealed up inside her bowels."
            # ready for use
            elif lauren.position == 3:
                wt_image cheater_slave_position_3
                "From the moment you put her in this position, [lauren.name]'s cunt has been drenching itself in anticipation of receiving your cock."
                wt_image cheater_slave_bj_3
                "The smell of her arousal is almost overpowering as you approach her."
                wt_image cheater_slave_behind_3
                "As you position yourself behind her, her hips twitch at the prospect of getting fucked."
                wt_image cheater_slave_anal_3
                if lauren.has_tag('no_anal'):
                    "She groans, as much out of disappointment as pain, when you shove your dick up her once forbidden butt hole instead, but it's a tighter and more enjoyable experience right now than her wet, sloppy sex."
                else:
                    "She groans, as much out of disappointment as pain, when you shove your dick up her butt hole instead, but it's a tighter and more enjoyable experience right now than her wet, sloppy sex."
                lauren.c "nnnn"
                "She can't get off this way, but you can, and that's all that matters."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_bj_3
                "She can wait a while longer for the prospect of serving you with one of her other holes."
            # hogtied
            elif lauren.position == 5:
                wt_image cheater_slave_position_5
                "It's not really possible to reach her pussy while she's tied up like this ..."
                wt_image cheater_slave_anal_4
                "... but with a few adjustments, you can reach her back hole."
                lauren.c "nnnnnn"
                player.c "Just a second. I can't hear you.  Let me get this gag out."
                wt_image cheater_slave_anal_7
                player.c "I think you were about to tell me how much you want me to fuck you ass."
                lauren.c "Y ... yes, [lauren.your_respect_name].  Please fuck my worthless ass."
                player.c "You want to feel my cock up your butt hole?"
                lauren.c "Yes, [lauren.your_respect_name].  If that's something you would like."
                if lauren.has_tag('no_anal'):
                    player.c "Even though you once asked me to never fuck your ass?"
                    lauren.c "[lauren.your_respect_name]??  [lauren.your_respect_name], I don't know what this worthless cunt was thinking to make her ever ask that of you. I'm so sorry, [lauren.your_respect_name]!"
                player.c "I think I should make it a painful ass fuck, don't you?"
                lauren.c "Yes, [lauren.your_respect_name].  If it would amuse you to hurt me as you fuck my ass, please make this a painful ass fuck."
                wt_image cheater_slave_anal_14
                lauren.c "OOOOOWWWWWWW!!!!"
                wt_image cheater_slave_anal_8
                "For her, it is a painful ass fuck ..."
                wt_image cheater_slave_anal_15
                "... for you, it's just a fun one."
                wt_image cheater_slave_anal_9
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_punish_44
                "She'll have plenty of time to recover from her ordeal, re-gagged and tied back into position on your coffee table."
            # suspended
            elif lauren.position == 6:
                wt_image cheater_slave_behind_9
                "[lauren.name]'s not sure what you intend when you spin her around."
                wt_image cheater_slave_suspend_9
                "As much as she loves the feel of your cock against her, she wishes it wasn't pressed against that hole."
                wt_image cheater_slave_bj_21
                "She already knows what's coming, but trembles when you confirm it for her as you remove her gag."
                wt_image cheater_slave_anal_6
                player.c "Scream for me, slave.  Let me know how it feels to take my cock in your ass."
                lauren.c "OOOOOWWWWWWW!!!!"
                if lauren.has_tag('no_anal'):
                    "It wouldn't feel so bad to her if you weren't ripping her open, but you stopped caring about using lube about the time you stopped caring that you once promised not to take her anally."
                else:
                    "It wouldn't feel so bad to her if you used some lube, but the dry penetration amplifies her pain and her screams, making the whole experience that much more exciting for you."
                "Between her screams and her tight, dry asshole moving up and down your cock as you swing her forward and back, you don't last long, but you enjoy it while you can."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_position_6
                "She sways gently back and forth after you put the gag back in and leave her. Her ass hurts like hell, but the feel of your cum back there reminds her that she pleased you, which makes all the pain worthwhile."
            # in armbinders
            elif lauren.position == 8:
                wt_image cheater_slave_punish_45
                player.c "Have you been lonely, waiting here for a chance to serve me?"
                lauren.c "Oh!  Yes, [lauren.your_respect_name]!!"
                player.c "Would you like a chance to serve me now?"
                lauren.c "Yes, [lauren.your_respect_name]!!  Please, [lauren.your_respect_name]!!!"
                wt_image cheater_slave_anal_1
                "Her hips start twitching in anticipation as you step behind her, then she tenses up as she feels you apply a dab of lube to her rosebud."
                player.c "Disappointed?"
                lauren.c "[lauren.your_respect_name]??"
                wt_image cheater_slave_anal_10
                if lauren.has_tag('no_anal'):
                    player.c "I know you like to amuse me with your pain. Especially when I'm fucking the ass you once foolishly asked me not to fuck. But sometimes you squirm so much when I fuck you dry that it's hard to enjoy myself."
                else:
                    player.c "I know you like to amuse me with your pain. But sometimes you squirm so much when I fuck your dry ass that it's hard to enjoy myself."
                lauren.c "Yes, [lauren.your_respect_name]. I'm sorry, [lauren.your_respect_name]."
                player.c "Don't be sorry. I think I put just enough lube on to make it feel better for me, and still be uncomfortable for you."
                wt_image cheater_slave_anal_2
                lauren.c "nnnn"
                "You're right. Your hard dick stretching her barely-lubricated rear entrance is uncomfortable for her, and thoroughly enjoyable for you."
                player.c "[player.orgasm_text]"
                wt_image cheater_slave_position_8
                "Her ass is a little sore when you leave her, and your cum dripping out of it tickles a bit, she's a pretty content slavegirl, knowing that you appreciate all of the holes she has to offer."
            # any other position
            else:
                wt_image cheater_slave_behind_1
                "You lock [lauren.name] into position, ass up, head down. The smell of her arousal fills the room, as her pussy swells and wets in anticipation of what she hopes is to come."
                wt_image cheater_slave_behind_16
                "Her hips tremble as you step behind her ..."
                wt_image cheater_slave_anal_11
                "... but it's not her wet sex you're interested in."
                wt_image cheater_slave_anal_12
                if lauren.has_tag('no_anal'):
                    "When she first came to you for training, you agreed not to fuck her in the ass. Neither she nor you have any expectation that just a silly agreement would still apply."
                else:
                    "It's her drier and tighter back door."
                lauren.c "nnnnn"
                wt_image cheater_slave_anal_13
                "You don't need to worry about tearing or bleeding. You can apply as much or as little lube as you want, and be as rough or gentle as you choose. She doesn't complain. Possessions never do."
                player.c "[player.orgasm_text]"
            $ lauren.anal_count += 1
            orgasm notify
    call character_location_return(lauren) from _call_character_location_return_475
    return

# Watch Her Dance
label lauren_watch_her_dance:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ lauren.strip_outfit_count += 1
    if lauren.strip_outfit_count > 5:
        $ lauren.strip_outfit_count = 1
    if lauren.strip_outfit_count == 1:
        wt_image cheater_strip_1_1
        "Lauren wears very little as she steps up onto the stage."
        wt_image cheater_strip_1_5
        "The top barely covers her breasts, and the bottom doesn't even cover her ass."
        wt_image cheater_strip_1_2
        "She pays no attention to the audience as she circles the pole, but she's having an effect on them."
        wt_image cheater_strip_1_3
        "It's not a particularly interesting routine, but it achieves objective number one in the show business world ..."
        wt_image cheater_strip_1_4
        "... capture their attention and leave them wanting more."
    elif lauren.strip_outfit_count == 2:
        wt_image cheater_strip_4_1
        "Lauren's dressed in basic black for today's dance."
        wt_image cheater_strip_4_2
        "Well, barely dressed."
        wt_image cheater_strip_4_3
        "Her outfit hides very little"
        wt_image cheater_strip_4_4
        "Just because she's wearing very little, however ..."
        wt_image cheater_strip_4_5
        "... doesn't mean she couldn't be wearing even less."
        wt_image cheater_strip_4_6
        "She didn't dance topless the last time ..."
        wt_image cheater_strip_4_7
        "... yet today she seems prepared to go even further."
        wt_image cheater_strip_4_8
        "At first you thought she was building up her courage."
        wt_image cheater_strip_4_9
        "But perhaps she was simply building up audience anticipation?"
        wt_image cheater_strip_4_10
        "Because she seems to have no lack of courage today."
        wt_image cheater_strip_4_11
        "Only an intent to give the audience a good show."
    elif lauren.strip_outfit_count == 3:
        wt_image cheater_strip_5_1
        "Lauren arrives on stage wearing both more and less than she wore last time."
        wt_image cheater_strip_5_2
        "On the one hand she's covered from her shoulders down ..."
        wt_image cheater_strip_5_3
        "On the other hand, she's hiding exactly nothing."
        wt_image cheater_strip_5_5
        "She doesn't strip today ..."
        wt_image cheater_strip_5_4
        "... just dance."
        wt_image cheater_strip_5_6
        "And through that dancing, she seems to turn on not only the audience, but also herself."
        if lauren.has_tag('transformed'):
            wt_image cheater_strip_5_7
            "In fact, you think she's not just dancing herself to arousal ..."
            wt_image cheater_strip_5_8
            "... you're pretty sure her poor, transformed mind managed to dance itself to orgasm."
            wt_image cheater_strip_5_9
            "There's a 'did she or didn't she' buzz as a glassy-eyed Lauren finishes her dance."
        else:
            wt_image cheater_strip_5_9
            "She gives the audience a look that suggests not only are they left wanting more ..."
            wt_image cheater_strip_5_10
            "... she is, too."
        $ title = "Check on Lauren after her dance?"
        menu:
            "No":
                "You return to your business."
            "Yes":
                wt_image cheater_strip_5_11
                "When you get backstage, the Club President is already there."
                wt_image cheater_strip_5_12
                "You can't make out what he's saying to her.  When she presents her butt to him, you think perhaps he's about to chastise her."
                wt_image cheater_strip_5_13
                "Then you realize he's actually giving her dancing tips."
                wt_image cheater_strip_5_14
                if lauren.has_tag('transformed'):
                    wt_image cheater_strip_5_14
                    "Which given the state of her befuddled, transformed mind, turns her on to no end."
                    wt_image cheater_strip_5_15
                    "You can hear her thanking the Club President for the pointers."
                    wt_image cheater_strip_5_16
                    "And then asking if she can thank him thoroughly?"
                    wt_image cheater_strip_5_17
                    "Presumably he said 'yes', or at least didn't object, as Lauren sucks him hard ..."
                    wt_image cheater_strip_5_21
                    "... and then climbs aboard."
                    wt_image cheater_strip_5_22
                    "You assume he enjoys her 'thank you'. You can certainly tell that she does."
                    wt_image cheater_strip_5_23
                    "She spots you just as she's orgasming. She might be a bit embarrassed, but she was just dancing in public. Who can be obedient under those circumstances?"
                else:
                    wt_image cheater_strip_5_15
                    "Lauren, however, is more interested in another form of assistance from him. Possibly it's the lingering arousal from her dance."
                    wt_image cheater_strip_5_17
                    "More likely it's rebellion against being restricted to only having sex with you or her husband."
                    wt_image cheater_strip_5_16
                    "You can't hear what she says to him ..."
                    wt_image cheater_strip_5_18
                    "... but it seems she was using her business negotiating skills to get what she wants."
                    wt_image cheater_strip_5_19
                    "And what she wants most right now is sex."
                    wt_image cheater_strip_5_20
                    "The Club President's role appears limited to supplying her with a hard dick."
                    wt_image cheater_strip_5_21
                    "But perhaps remembering that it's important to have good relations with your suppliers, she at least turns around to face him ..."
                    wt_image cheater_strip_5_22
                    "... even if she never actually looks at him."
                    wt_image cheater_strip_5_23
                    if lauren.has_tag('blackmailed'):
                        "She does look at you, though, spotting you just as she orgasms. She might be a bit embarrassed, but you're already blackmailing her. What more could you do?"
                    else:
                        "She does look at you, though, spotting you just as she orgasms. She might be a bit embarrassed, but likes sex, and your obedience training only went so far."
    elif lauren.strip_outfit_count == 4:
        wt_image cheater_strip_2_1
        "Lauren appears on stage wearing less clothing than ever before."
        wt_image cheater_strip_2_2
        "... and proceeds to bare what little the outfit is actually hiding."
        wt_image cheater_strip_2_12
        "It's not a subtle approach, but it's a popular one, and she's surprised to find herself the recipient of a tip."
        if lauren.workout_count > 0:
            wt_image cheater_strip_2_3
            "Emboldened, she tries a classic stripper pole dance maneuver. You're happy to see the workout training you provided her put to a practical purpose."
            wt_image cheater_strip_2_13
            "She follows that up with a classic - if not classy - stripper floor routine, when the source of her tips makes himself known."
        else:
            wt_image cheater_strip_2_13
            "Emboldened, she performs a classic - if not classy - stripper floor routine, when the source of her tips makes himself known."
        wt_image cheater_strip_2_14
        "Two things Lauren has always appreciated are money and expressions of sexual interest.  She backs up towards her admirer ..."
        wt_image cheater_strip_2_15
        "... who surprises her by depositing his tip on her."
        wt_image cheater_strip_2_16
        "That earns him a brief lap dance ..."
        wt_image cheater_strip_2_6
        "... that she allows him to end with an even briefer, but very firm, butt squeeze and examination."
        wt_image cheater_strip_2_11
        "She climbs back on the stage to give everyone the same view ..."
        wt_image cheater_strip_2_5
        "... but her admirer wants her to go further."
        wt_image cheater_strip_2_4
        "At his suggestion, she plays with herself - while positioned directly in front of him of course."
        wt_image cheater_strip_2_17
        "He wants one more thing from her, though.  She looks at his money, and nods."
        wt_image cheater_strip_2_18
        "They say money provides access. In this case, it provides access for his fingers to her pussy."
        wt_image cheater_strip_2_19
        "Even he's surprised, though, when she kneels in front of him ..."
        wt_image cheater_strip_2_7
        "... and removes his pants."
        if lauren.blowjob_count > 1:
            wt_image cheater_strip_2_8
            "You feel a warped sense of pride when you see she remembers your lessons, and starts the man off by gently licking and sucking his balls."
        wt_image cheater_strip_2_20
        "Performer-patron contact is vaguely frowned upon at the Club, but not expressly forbidden. During her show, it's her stage, and her rules."
        wt_image cheater_strip_2_9
        "If she wants to suck a cock, neither her husband nor you can tell her she can't. She need only ensure that the audience is entertained, and they are."
        wt_image cheater_strip_2_14
        "This isn't just about the audience, though. It's also about satisfying her urges. She wanted to fuck him from the time he brazenly dropped his money on top of her."
        wt_image cheater_strip_2_21
        "As the audience cheers, she impales herself on him ..."
        wt_image cheater_strip_2_22
        "... and rides him to first her orgasm ..."
        wt_image cheater_strip_2_10
        "... then his, to the sound of applause."
    elif lauren.strip_outfit_count == 5:
        wt_image cheater_showgirl_portrait_2
        "If Lauren's previous act was one of the raunchiest ever performed on this stage, today's promises to be one of the catchiest."
        wt_image cheater_strip_3_8
        "Perhaps to prove that she can entertain without sucking and fucking, she starts with a dance routine ..."
        wt_image cheater_strip_3_9
        "... that ends like an act straight out of vaudeville, with her tossing her hat into the audience."
        wt_image cheater_strip_3_1
        "The vest soon follows the hat ..."
        wt_image cheater_strip_3_10
        "... a part of the act critical only for it's role in disappearing."
        wt_image cheater_strip_3_2
        "Lauren continues to dance .."
        wt_image cheater_strip_3_3
        "... now in only her bowtie, sheer bodysuit, and fake garters."
        wt_image cheater_strip_3_4
        "The bodysuit is the next to go."
        wt_image cheater_strip_3_5
        "Lauren keeps dancing ..."
        wt_image cheater_strip_3_6
        "... as her clothes continue to disappear ..."
        wt_image cheater_strip_3_11
        "... until only the bowtie remains."
        wt_image cheater_strip_3_12
        "In the end, her act turns out to be more burlesque than vaudeville ..."
        wt_image cheater_strip_3_13
        "... complete with a finishing flair that would have made Blaze Starr proud."
    else:
        sys "There's been an error with the lauren.strip_outfit_count variable."
    add tags 'watched_today' to lauren
    change player energy by -energy_very_short
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label lauren_contact:
    # waiting for club access?
    if lauren.has_tag('waiting_for_club_access') and lauren.has_tag('stage_message_given') and player.has_tag('club_first_visit_complete'):
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        wt_image cheater_office_phone_2
        player.c "Lauren, I've found the right situation for you.  I've become a member of a private Club.  You're going to dance there."
        player.c "And by dance, I mean take off your clothes and entertain the audience."
        player.c "It won't get back to your husband. The Club is very strict about privacy.  You may even come to thank me some day."
        player.c "Access to the Club may give you opportunities to satisfy your urges. Because you know as well as I that no matter how much you want to, you'll never be able to stay faithful to your husband."
        "She doesn't say anything, but you know she agrees."
        player.c "They'll be waiting for you tomorrow.  Buy something even sluttier than normal to wear for your first shift.  You want to make a good impression."
        call lauren_convert_showgirl from _call_lauren_convert_showgirl
    # love potion initial contact
    elif lauren.has_tag('love_potion_used') and lauren.desire > 30 and not lauren.has_tag('continuing_actions'):
        wt_image cheater_office_phone_3
        lauren.c "I'm so glad you called! Please tell me you'll keep seeing me? I know I'm supposed to be an obedient slut to my husband, but I can't bear the thought of not seeing you again."
        $ title = "What do you tell her?"
        menu:
            "Yes":
                player.c "Yes, Lauren.  You may come see me.  In fact, now is the ideal time."
                lauren.c "Oh thank you!  I'll be right over."
                add tags 'continuing_actions' to lauren
                summon lauren to living_room
            "No":
                player.c "I'm sorry, Lauren, but this has to end."
                lauren.c "But ..."
                player.c "No buts. I told your husband I would turn you into an obedient slut. An obedient slut doesn't run around on her husband. Not with anyone, including me."
                lauren.c "Can't we just ..."
                wt_image phone_1
                "You cut her off. She emails and calls you every day for the next few weeks, then the contacts cease. Perhaps the effects of the love potion finally wore off. Perhaps she still pines for you, but has accepted her fate."
                $ living_room.remove_action(lauren.current_client_action)
                call convert(lauren,'unavailable') from _call_convert_78
            "No, and tell her husband":
                player.c "I'm sorry, Lauren, but I've failed your husband."
                lauren.c "My husband?"
                player.c "Yes. I promised him I would turn you into an obedient slut.  Yet here you are, trying to cheat on him with me."
                lauren.c "No, that's not what this is!"
                player.c "I'm afraid it is. I have no choice but to send your earlier email to him.  I know he'll be disappointed, but it's better that he know we failed and divorce you now."
                player.c "With the proof that I provide him, he will get a very favorable result from the divorce proceedings.  I'm sure you won't be as happy."
                lauren.c "I don't care about that! I just want to see you!!"
                player.c "That too is impossible. Goodbye, Lauren."
                wt_image phone_1
                "That was harsh. After the love potion you gave her, she couldn't help herself from contacting you. In the end, she lost her husband, her money, and her old life."
                "All she's left with is a burning desire to be with you. And she can't even have that."
                $ living_room.remove_action(lauren.current_client_action)
                call convert(lauren,'unavailable') from _call_convert_79
    # Will she accept continuing actions?
    elif not lauren.has_tag('continuing_actions'):
        wt_image cheater_office_phone_2
        lauren.c "I wasn't expecting to hear from you again, now that my training is finished."
        player.c "Lauren, I want you to continue to visit me.  Without your husband's knowledge."
        if lauren.desire > 90:
            "Lauren is quiet for a moment before she replies."
            wt_image cheater_office_phone_1
            lauren.c "Okay.  I'll be right over."
            add tags 'continuing_actions' to lauren
            summon lauren to living_room
        elif lauren.submission > 100:
            "Lauren is quiet for a moment before she replies."
            lauren.c "Yes, Sir.  I'll be right over."
            add tags 'continuing_actions' to lauren
            summon lauren to living_room
        else:
            lauren.c "I can't do that. I promised my husband I'd be faithful to him.  Please don't contact me again."
            "It seems your training was successful, and Lauren is on the path to being a proper obedient slut for her husband."
            if lauren.has_tag('trigger_implanted'):
                "However, your training also included implanting a trigger in Lauren's mind."
                player.c "[lauren.trigger_phrase], Lauren.  Are you listening to me?"
                lauren.c "Yes, I'm listening to you."
                player.c "You want to visit me."
                lauren.c "No, I ..."
                player.c "[lauren.trigger_phrase].  You want to visit me."
                lauren.c "Yes, I want to visit you."
                player.c "You will not remember this conversation.  From now on, however, when I contact you and ask you to visit, you will do so."
                player.c "You will not tell your husband.  You will meet with me in secret, whenever I ask you to.  Do you understand?"
                lauren.c "Yes, I understand.  I will meet you in secret whenever you ask."
                player.c "Good.  Come over now."
                add tags 'continuing_actions' to lauren
                summon lauren to living_room
            else:
                call convert(lauren,'unavailable') from _call_convert_80
                $ living_room.remove_action(lauren.current_client_action)
    # additional visits
    else:
        if lauren.has_tag('whore'):
            if lauren.has_tag('transformed'):
                wt_image cheater_office_phone_1
                player.c "How's my favorite professional cock sucker?"
                lauren.c "Pretty good, according to the customers."
            else:
                wt_image cheater_office_phone_2
                player.c "How's my favorite professional cock sucker?"
                lauren.c "You're disgusting."
            player.c "Not holding out on me, are you?"
            lauren.c "Of course not!"
            player.c "Good.  Get yourself over here.  I want to do some quality control."
            $ lauren.whore_lost_countdown = 5
        elif lauren.has_tag('blackmailed'):
            wt_image cheater_office_phone_2
            player.c "I'd like you to come visit me."
            lauren.c "Do I have a choice?"
            player.c "No"
        else:
            wt_image cheater_office_phone_1
            player.c "I'd like you to come visit me."
            lauren.c "Okay.  I'll be right over."
        summon lauren to living_room
    return

# Continuing Actions
# Regular Visit - Note: this is an action with a
## note: consider adding a take her to the dungeon option
label lauren_continuing_visit:
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if lauren.cheated == 0:
        if lauren.has_tag('love_potion_used'):
            wt_image cheater_continuing_16
            "Lauren arrives promptly.  Her clothing demonstrates that she's fully embraced her role as slut.  She seems happy to get to spend time with you."
        else:
            wt_image cheater_continuing_18
            "Lauren arrives promptly.  Her clothing demonstrates that she's fully embraced her role as slut."
    else:
        if lauren.has_tag('blackmailed'):
            wt_image cheater_continuing_20
            "Lauren's not happy about being here, but she's here anyway."
        elif lauren.has_tag('love_potion_used'):
            wt_image cheater_continuing_17
            "Lauren's happy she gets to spend more time with you."
        else:
            wt_image cheater_continuing_19
            "Lauren waits to find out what you have planned for her today."
    $ title = "What do you want?"
    menu:
        "Watch her masturbate":
            wt_image cheater_continuing_1
            "Lauren removes her top and pulls down her pants"
            if lauren.has_item(chastity_belt):
                lauren.c "Thank you for letting me do this."
                "Locked into the chastity belt, the only time she can masturbate is when you or her husband let her out."
            wt_image cheater_continuing_2
            "When she's completely naked, she leans back, spreads her legs, and starts to play with herself as you watch."
            wt_image cheater_masturbating_6
            "Her fingers explore her body.  Before long, she's breathing heavily and emitting soft moans."
            lauren.c "oooo  ... oooo"
            if lauren.test('desire',40) or lauren.has_item(chastity_belt):
                wt_image cheater_continuing_3
                "As her excitement builds, she turns around and finger fucks herself as she grinds her pubic bone into the edge of the sofa as the smell of her arousal fills the room."
                lauren.c "oooooo  ...  aaahhhh!"
                wt_image cheater_continuing_4
                "Still pressing her clit against the edge of the sofa, she licks off her fingers as she recovers from the orgasm."
                call lauren_masturbation_stat_changes from _call_lauren_masturbation_stat_changes_4
            else:
                wt_image cheater_continuing_2
                "She's not able to cum today, at least not with you watching, but she still gets sticky wet and the smell of her arousal fills the room."
                change lauren desire by 5
            if lauren.has_item(chastity_belt):
                wt_image cheater_chastity_2
                "As you lock her back into her chastity belt, she bows her head submissively."
                lauren.c "Thank you again for letting me touch myself."
                change lauren submission by 5
            change player energy by -energy_very_short notify
        "Pleasure her":
            wt_image cheater_continuing_21
            "Lauren's not entirely sure what to expect as you remove her pants."
            wt_image cheater_continuing_22
            "She lets out a soft sigh of surprise as you lean her back and spread her legs, and then another of excitement as your tongue reaches her sex."
            lauren.c "Oh  ...  oooo"
            if lauren.test('desire', 30):
                wt_image cheater_continuing_9
                "It doesn't take long for the first orgasm to wash over her.  She groans as she climaxes and floods your mouth with her juices."
                lauren.c "oooooo ... y ... yes ... aaahhhh!"
                wt_image cheater_continuing_10
                "As you continue to lick her now highly sensitized clit, she bites her lip.  Post orgasm, the feeling is almost as much torture as pleasure."
                "She knows better than to try and move your head away.  You watch her face as you lick her, enjoying the sight of her trying to process the conflicting sensations."
                wt_image cheater_continuing_9
                "Soon the pleasure wins out, and she bucks her hips against your face as a second orgasm, more intense than the first, rocks through her."
                lauren.c "Aaahhhh!!"
                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_35
                wt_image cheater_continuing_16
                lauren.c "Wow!"
                player.c "You can go home now, slut."
                lauren.c "Okay.  Thanks for inviting me over!"
            else:
                wt_image cheater_continuing_10
                "She's not able to relax enough to cum today, but she gets very, very wet as you lap her."
            $ lauren.pleasure_her_count += 1
            call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_4
            change player energy by -energy_short notify
        "Put her on the fuck machine" if dungeon.has_item(fuck_machine) and lauren.has_item(dildo):
            $ lauren.fuck_machine_count += 1
            if lauren.fuck_machine_count == 1:
                wt_image cheater_continuing_18
                "Lauren looks at you with suspicion as you set up the fuck machine."
                lauren.c "What is that?"
                player.c "A slut training device.  Remove your clothes and I'll show you how it works."
            else:
                wt_image cheater_continuing_20
                "Lauren gives you and the fuck machine a look as you set the device up. It's hard to tell exactly what she's feeling. Fear? Excitement?  A bit of both?"
            wt_image cheater_machine_21
            "You place Lauren in front of the machine and insert the dildo head into her."
            if lauren.fuck_machine_orgasm_count == 0:
                wt_image cheater_machine_12
                "She's not wet yet, but she soon will be."
            else:
                wt_image cheater_machine_20
                "She's already wet even before you turn the device on."
            wt_image cheater_machine_21
            if lauren.fuck_machine_count == 1:
                add tags 'machine_dildo_explained' to lauren
                player.c "Let me explain how this works.  This machine is going to fuck you.  It's going to fuck you long and hard."
                player.c "It's going to feel good and it's going to feel painful at the same time.  And as it fucks you, despite the discomfort, you're going to feel the urge to cum."
                player.c "I'm going to give you your toy.  When you're ready to cum, you'll set it to vibrate and press it against your clit."
                player.c "You're not allowed to use your toy, though, until I give you permission.  And you're definitely not allowed to cum until I give you permission."
                player.c "Can you guess how you get permission?"
                lauren.c "I need to ask?"
                player.c "Beg, actually.  Do you think you can do that?"
                if lauren.submission > 125:
                    lauren.c "Yes, Sir."
                else:
                    "She bites her lip, uncertain as to whether she can, and more importantly, whether she wants to."
            elif not lauren.has_tag('machine_dildo_explained'):
                add tags 'machine_dildo_explained' to lauren
                player.c "You know what this is and what's going to happen, don't you, slut?"
                "Lauren nods."
                player.c "Today I'm going to give you your toy to hold while the machine fucks you.  When you want to cum, you'll set it to vibrate and press it against your clit."
                player.c "You're not allowed to use your toy, though, until I give you permission.  And you're definitely not allowed to cum until I give you permission."
                player.c "Can you guess how you get permission?"
                lauren.c "I need to ask?"
                player.c "Beg, actually.  Do you think you can do that?"
                if lauren.submission > 125:
                    lauren.c "Yes, Sir."
                else:
                    "She bites her lip, uncertain as to whether she can, and more importantly, whether she wants to."
            else:
                player.c "I'm sure you don't need to be reminded of the rules, do you, slut?"
                "Lauren shakes her head.  She knows what's going to happen, and what's expected of her."
            wt_image cheater_machine_22
            "You hand Lauren her toy and step back to watch the show as you flip the machine to 'on' ...  *wuppp*  *wuppp*  *wuppp*"
            lauren.c "oooo ... ow!"
            wt_image cheater_machine_23
            "Despite the discomfort caused by the relentless, mechanical pounding, she's ready to cum in a ridiculously short amount of time."
            lauren.c "oooo ... ow! ... oooooo"
            if lauren.test('submission', 20):
                if lauren.fuck_machine_orgasm_count == 0:
                    lauren.c "I need to cum.  Please.  Am I allowed to cum?"
                    player.c "Does this greedy little cunt admit how much it needs to be fucked and cum?"
                    lauren.c "Yes"
                    player.c "Make me believe you."
                    lauren.c "Yes!  I admit I need to be fucked and to cum!"
                    player.c "Then the greedy cunt is allowed to use it's toy."
                    wt_image cheater_machine_24
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_machine_22
                    "As the orgasm subsides, she removes the vibrator."
                    player.c "Oh no you don't.  You asked to use your toy.  Put it back."
                    lauren.c "But ..."
                    player.c "You heard me."
                    wt_image cheater_machine_25
                    "As she presses the vibrator back against her sex, you turn up the speed of the machine ... *wuppp*  *wuppp*  *wuppp*"
                    lauren.c "AAAAAHHHHHH!!!!!!!"
                    wt_image cheater_machine_26
                    "As her second orgasm subsides, you turn the speed of the machine up yet another notch. To her shock, Lauren's body immediately begins a third orgasm, even more intense than the last."
                    lauren.c "Oh God  ...  No!  ...  OH SHIT!!  ... AAAAGGGHHHH!!!!!!"
                    wt_image cheater_machine_25
                    "When the second wave of tremors cease, you turn the machine off."
                    wt_image cheater_machine_21
                    "Lauren sits slumped, impaled by the now quiet machine, for a full fifteen minutes before she can move.  When she's finally recovered, you let her dress and send her home."
                    change lauren desire by 10
                    change lauren submission by 10
                    change lauren resistance by -10
                elif lauren.fuck_machine_orgasm_count == 1:
                    lauren.c "Please.  I need to cum."
                    player.c "What needs to cum?"
                    lauren.c "This greedy little cunt."
                    player.c "And how many times would this greedy cunt like to cum?  Once, twice, three times ... five?"
                    lauren.c "I ... I'm not sure ... I just need to cum."
                    player.c "Let's find out, shall we?  You can have your first orgasm."
                    wt_image cheater_machine_24
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_machine_22
                    player.c "Would you like another?"
                    lauren.c "Y ... yesss ... pleaassse"
                    wt_image cheater_machine_25
                    lauren.c "AAAAAHHHHHH!!!!!!!"
                    wt_image cheater_machine_26
                    "Without giving her any time to recover, you turn the machine up another notch and watch as it pounds one, then two, then more orgasms out of her."
                    lauren.c "AAAA ...  AAAA ....  AAAAGGGHHHH!!!!!!"
                    wt_image cheater_machine_25
                    "After the third climax, the screams stop, replaced by a continual deep guttural moan. Her brain is no longer functioning properly, and has no idea whether you pull three, or five, or ten orgasms out of her tortured sex before you turn off the machine."
                    wt_image cheater_machine_21
                    "You let her rest until her legs are able to support her again, then let her dress and go home."
                    change lauren desire by 5
                    change lauren submission by 5
                    change lauren resistance by -5
                else:
                    lauren.c "Please.  I need to cum."
                    player.c "What needs to cum?"
                    lauren.c "This greedy little cunt."
                    player.c "And how many times would this greedy cunt like to cum, Once, twice, three times ... five?"
                    lauren.c "Oohhh  ...  Just once.  That's all.  Please??"
                    player.c "I suppose you can have one orgasm."
                    wt_image cheater_machine_24
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_machine_22
                    player.c "Put the toy back."
                    lauren.c "But ..."
                    player.c "You heard me."
                    wt_image cheater_machine_25
                    "She said she only wanted one orgasm, but where would the fun be in that?  As she places the vibrator back against her, you bump up the machine to the next higher speed ...  *wuppp*  *wuppp*  *wuppp*"
                    lauren.c "AAAAHHHHH!!!!!!!"
                    wt_image cheater_machine_26
                    "Then the next highest speed...  *wuppp*  *wuppp*  *wuppp*."
                    lauren.c "AAAA ...  AAAA ....  AAAAGGGHHHH!!!!!!"
                    wt_image cheater_machine_25
                    "After that, the screams stop, replaced by a continual deep guttural moan.  Her brain is no longer functioning right, and she has no idea how many orgasms you pull out of her."
                    wt_image cheater_machine_21
                    "To be honest, neither do you  You stop counting and simply let the machine fuck her until her exhausted body can no longer register another climax."
                    "You let her rest until her legs are able to support her again, then let her dress and go home."
                    change lauren submission by 5
                    change lauren resistance by -5
                $ lauren.fuck_machine_orgasm_count += 1
            else:
                "Despite the burning need building between her legs, Lauren is too proud to ask you for permission to cum."
                wt_image cheater_machine_22
                "She successfully fights her urges until you release her.  She groans in relief when you finally turn the machine off."
                lauren.c "oohhh"
                wt_image cheater_machine_21
                "Deep inside, though, she wishes that she hadn't been so proud.  She wanted to cum, and she can't help feeling that begging you to let her cum would have been worth it."
                "It takes her a few minutes before her trembling legs are able to support her weight again.  When they are, you let her dress and send her home."
                change lauren submission by 10
                change lauren resistance by -5
            change player energy by -energy_very_short
        "Blow job":
            if lauren.cheated == 0:
                $ lauren.cheated = 1
            call lauren_continuing_oral from _call_lauren_continuing_oral
            orgasm notify
        "Fuck her on the ottoman" if lauren.sex_count != 1 and lauren.sex_count != 2:
            if lauren.cheated == 0:
                $ lauren.cheated = 1
            wt_image cheater_continuing_1
            "Lauren removes her clothes ..."
            wt_image cheater_continuing_27
            "... and spreads her legs as you insert the head of your cock into her."
            lauren.c "Oh!"
            if lauren.sex_count == 0:
                wt_image cheater_continuing_28
                "She knew this day was coming, when you'd use her for sex.  She'd been dreading it, but she knew she wouldn't be able to tell you 'no' when the time came."
                player.c "Don't look so sad, slut.  You may even enjoy being my personal fuck toy."
                lauren.c "I don't want to enjoy it."
                player.c "You might enjoy it anyway."
                wt_image cheater_continuing_29
                "She doesn't really enjoy herself. Not today, anyway. But despite her reservations, her body does get wet as you fuck her. She knows it, and she knows you know it."
                player.c "It's okay if you cum, as long as it doesn't interfere with my pleasure."
                lauren.c "I'm not going to cum.  I don't even want to cum."
                wt_image cheater_continuing_27
                "The same cannot be said of you."
                $ title = "Where do you want to cum?"
                menu:
                    "In her":
                        wt_image cheater_continuing_28
                    "On her":
                        wt_image cheater_continuing_30
                player.c "[player.orgasm_text]"
                wt_image cheater_continuing_1
                "She dresses quietly, avoiding eye contact with you"
                player.c "Don't you want to say something to me?"
                lauren.c "What?"
                player.c "Shouldn't you be thanking me for letting you have sex with me?"
                lauren.c "Are you kidding me?"
                if lauren.has_tag('whore'):
                    player.c "No. Your husband and I are your only sources of sex from here out, other than your johns. And I can cut you off from whoring anytime I want. You should be grateful for access to my cock."
                else:
                    player.c "No.  Your husband and I are your only sources of sex from here out.  You should be grateful for access to my cock."
                "She can't bring herself to thank you and you don't push it, as that may be a step too far for her right now.  But you've made your point."
                change lauren submission by 10
            else:
                wt_image cheater_continuing_29
                player.c "Give me a good fuck this time, slut."
                "She nods."
                player.c "What do you say, slut?"
                if lauren.test('submission', 125):
                    lauren.c "Thank you for the opportunity to be fucked by you, Sir."
                    player.c "Show me how thankful you are."
                    wt_image cheater_continuing_27
                    "She does her best, bucking her hips up towards you as you fuck her, and squeezing your cock as it slides in and out of her."
                    lauren.c "oooo"
                    if lauren.test('desire', 60):
                        wt_image cheater_continuing_31
                        "She's obviously enjoying this, too, as she reaches a quick, intense climax as you fuck her."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_continuing_29
                        "It doesn't take you much longer."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_36
                    else:
                        wt_image cheater_continuing_29
                        "She doesn't get aroused enough to cum, but she gets close.  You, on the other hand, have no trouble getting aroused enough to cum.  The only question is where?"
                        change lauren desire by 10
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_continuing_27
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_continuing_33
                            "She seems comfortable going back to her husband carrying your load inside her."
                        "On her":
                            wt_image cheater_continuing_30
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_continuing_32
                            player.c "No cleaning yourself up, slut.  You'll wear my cum for the remainder of the day."
                            lauren.c "Yes, Sir."
                elif lauren.test('desire', 60):
                    lauren.c "It feels good having you inside me."
                    player.c "And?"
                    lauren.c "I'm glad you decided to fuck me."
                    player.c "Show me how thankful you are."
                    wt_image cheater_continuing_27
                    "She does her best, bucking her hips up towards you as you fuck her, and squeezing your cock as it slides in and out of her."
                    lauren.c "oooo"
                    wt_image cheater_continuing_31
                    "She's obviously enjoying this, too, as she reaches a quick, intense climax as you fuck her."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_continuing_29
                    "It doesn't take you much longer."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_continuing_27
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_continuing_33
                            "She seems comfortable going back to her husband carrying your load inside her."
                        "On her":
                            wt_image cheater_continuing_30
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_continuing_32
                            player.c "No cleaning yourself up, slut.  You'll wear my cum for the remainder of the day."
                            "She seems comfortable with your instructions."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_37
                else:
                    lauren.c "About what?"
                    player.c "About having the opportunity to be fucked by me.  You should thank me."
                    wt_image cheater_continuing_27
                    "She can't bring herself to say it, but she still tries to make this pleasurable for you, bucking her hips up towards you and squeezing your cock as it slides in and out of her."
                    wt_image cheater_continuing_28
                    "Part of her is trying to remain disengaged, the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                    wt_image cheater_continuing_29
                    "She may not be going to cum, but you certainly are.  The only question is where?"
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image cheater_continuing_27
                        "On her":
                            wt_image cheater_continuing_30
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_1
                    "She dresses quietly, trying to avoid eye contact with you again."
                    player.c "You enjoyed that, slut.  Why not admit it?"
                    if lauren.has_tag('blackmailed'):
                        wt_image cheater_first_strip_3
                        lauren.c "You're blackmailing me.  See if you can figure out why I don't want to have sex with you."
                    else:
                        "She did, but she won't.  Not yet, anyway."
                    change lauren desire by 5
            $ lauren.sex_count += 1
            orgasm notify
        "Fuck her from behind" if lauren.sex_count > 1:
            if lauren.cheated == 0:
                $ lauren.cheated = 1
            wt_image cheater_continuing_13
            player.c "Hands and knees, slut. Face away from me and pull down your pants."
            ## NEED FINISH
            wt_image cheater_continuing_43
            "As she does, you slip the head of your cock into her."
            lauren.c "Oh!"
            if lauren.sex_count == 2:
                wt_image cheater_continuing_44
                player.c "Let's see if you're getting any better at fucking, Lauren. I'm going to hold myself here you're going to do the work."
                player.c  "You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
                "Lauren nods."
                player.c "Good.  Then get at it."
                wt_image cheater_continuing_45
                "You don't say anything more.  You just hold yourself and her in place and watch as she struggles to pleasure your cock within the limited range of movement you give her."
                if lauren.test('desire', 60):
                    wt_image cheater_continuing_14
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your hands on her hips her triggers a response."
                    lauren.c "oooooo"
                    wt_image cheater_continuing_46
                    "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_continuing_44
                    player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_38
                wt_image cheater_continuing_43
                "Lauren tries very hard to pleasure your cock, but it's not easy within the limited range of motion you allow her."
                wt_image cheater_continuing_47
                "She start to worry that the squeezing and hip rolls won't be enough to get you off. Fortunately for her, the sight of her working so hard to extract your cum is itself a big turn on, and you feel your orgasm building."
                wt_image cheater_continuing_44
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                wt_image cheater_continuing_45
                player.c "That felt good, didn't it?  Working to earn my cum."
                if lauren.submission > 125:
                    wt_image cheater_continuing_43
                    lauren.c "Yes, Sir"
                    if lauren.desire <= 60:
                        change lauren desire by 10
                elif lauren.desire > 60:
                    wt_image cheater_continuing_44
                    lauren.c "Yes"
                    change lauren submission by 5
                else:
                    wt_image cheater_continuing_47
                    "She seems offended by your question, but the wetness of her cunt around your cock tells you she's turned on."
                    change lauren submission by 5
                    change lauren desire by 5
            else:
                player.c "Does that feel good, slut?"
                if lauren.test('submission', 125):
                    lauren.c "Yes, Sir."
                    player.c "What do you want, slut?"
                    lauren.c "I want you to fuck me, Sir.  Please fuck me?"
                    player.c "No, slut, I won't.  But I'll let you fuck me."
                    wt_image cheater_continuing_45
                    "She starts to wiggle and buck her hips, slowly at first ..."
                    wt_image cheater_continuing_44
                    "... then faster and faster, doing her best to pleasure you within the limited range of motion you allow her."
                    if lauren.test('desire', 60):
                        wt_image cheater_continuing_14
                        "It turns out that she turns herself on, too ..."
                        lauren.c "oooooo"
                        wt_image cheater_continuing_46
                        "... as before long she's climaxing around around your cock."
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_continuing_44
                        player.c "Keep moving your hips, slut.  The goal is my pleasure, not yours."
                        lauren.c "Y ...  yes, Sir."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_39
                    else:
                        change lauren desire by 10
                    wt_image cheater_continuing_47
                    "She starts to worry that you're not letting her move enough to get you off ..."
                    wt_image cheater_continuing_46
                    "... but the combination of her milking your cock with her cunt and and wiggling her hips back and forth turns out to be enough to earn your seed."
                    wt_image cheater_continuing_44
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_33
                    "She seems comfortable going home to her husband carrying your load inside her."
                elif lauren.test('desire', 60):
                    lauren.c "Yes"
                    player.c "What do you want, slut?"
                    lauren.c "I want you to fuck me until I cum."
                    player.c "No, slut, I won't.  But I'll let you fuck me until I cum."
                    wt_image cheater_continuing_45
                    "She starts to wiggle and buck her hips, slowly at first ..."
                    wt_image cheater_continuing_44
                    "... then faster and faster, doing her best to pleasure you within the limited range of motion you allow her."
                    wt_image cheater_continuing_14
                    "It turns out that she turns herself on, too ..."
                    lauren.c "oooooo"
                    wt_image cheater_continuing_46
                    "... and she soon gives herself the orgasm she was craving."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_continuing_44
                    player.c "Keep moving your hips, slut.  The goal is my pleasure, not yours."
                    lauren.c "Y ...  yes, Sir."
                    wt_image cheater_continuing_47
                    "She starts to worry that you're not letting her move enough to get you off ..."
                    wt_image cheater_continuing_46
                    "... but the combination of her milking your cock with her cunt and and wiggling her hips back and forth turns out to be enough to earn your seed."
                    wt_image cheater_continuing_44
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_33
                    "She seems comfortable going home to her husband carrying your load inside her."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_40
                else:
                    wt_image cheater_continuing_47
                    player.c "Don't look so concerned about the question, slut. The important thing is whether it feels good to me. Make it feel good for me, slut."
                    wt_image cheater_continuing_45
                    "She starts to wiggle and buck her hips, slowly at first ..."
                    wt_image cheater_continuing_44
                    "... then faster and faster, doing her best to pleasure you within the limited range of motion you allow her."
                    wt_image cheater_continuing_14
                    "She may not want to let herself enjoy this, but she lets out a few moans anyway as she pleasures herself while trying to pleasure you."
                    lauren.c "oooo"
                    wt_image cheater_continuing_47
                    "After a while, she becomes concerned that you're not letting her move enough to get you off ..."
                    wt_image cheater_continuing_46
                    "... but the combination of her milking your cock with her cunt and and wiggling her hips back and forth turns out to be enough to earn your seed."
                    wt_image cheater_continuing_44
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_1
                    "She dresses quietly, avoiding eye contact with you again."
                    player.c "You enjoyed that, slut.  Why not admit it?"
                    "She did, but she won't.  Not yet, anyway."
                    change lauren desire by 5
                $ lauren.sex_count += 1
                orgasm notify
        "Have her ride you" if lauren.sex_count > 0 and lauren.sex_count != 2:
            if lauren.cheated == 0:
                $ lauren.cheated = 1
            if lauren.sex_count == 1:
                player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
                player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
                wt_image cheater_continuing_34
                player.c "Get up on here and show me what you can do with your cunt, slut."
                "Nervously, Lauren climbs up on top of you."
                lauren.c "Oh!"
                wt_image cheater_continuing_35
                player.c "All right then, get to work.  Up and down, use your legs."
                wt_image cheater_continuing_36
                player.c "Right up to the tip on your way up."
                wt_image cheater_continuing_37
                player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you.  Use your hips too.  Rock them back and forth to change the angle of pressure."
                wt_image cheater_continuing_38
                player.c "If your cunt gets too dry, play with your clit. You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
                wt_image cheater_continuing_37
                "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
                if lauren.test('desire', 60):
                    wt_image cheater_continuing_11
                    "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                    lauren.c "oooooo"
                    wt_image cheater_continuing_39
                    "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_continuing_12
                    player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                    lauren.c "Y ... yes"
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_41
                wt_image cheater_continuing_36
                "When she's learned as much as she's going to learn today, you let yourself cum."
                wt_image cheater_continuing_35
                player.c "[player.orgasm_text]"
                lauren.c "Oh!"
                wt_image cheater_continuing_34
                player.c "You can go home now, slut.  Once your legs have recovered from the workout."
            else:
                player.c "You're in luck, slut.  You get to ride my pole today."
                wt_image cheater_continuing_34
                "Lauren moans as you guide her down onto your dick."
                lauren.c "Oh!"
                player.c "What do you say, slut?"
                if lauren.test('submission', 125):
                    wt_image cheater_continuing_38
                    lauren.c "Thank you, Sir. Thank you for letting me ride your hard cock."
                    player.c "Do a good job of it , slut."
                    wt_image cheater_continuing_36
                    lauren.c "Yes, Sir"
                    if lauren.test('desire', 60):
                        wt_image cheater_continuing_34
                        "She gets excited as soon as she starts riding you ..."
                        lauren.c "oooo"
                        wt_image cheater_continuing_11
                        "... and is soon moaning loudly as she bounces up and down on your shaft."
                        lauren.c "oooo  ...  ooooooo"
                        wt_image cheater_continuing_39
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_continuing_12
                        player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                        lauren.c "Y ...  yes, Sir."
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_42
                    else:
                        wt_image cheater_continuing_35
                        "She's not excited enough to get off herself ..."
                        wt_image cheater_continuing_34
                        ".. but she rides you up and down ..."
                        wt_image cheater_continuing_36
                        "... faster and faster ..."
                        wt_image cheater_continuing_34
                        "... making sure that you're more than excited enough to get off."
                        wt_image cheater_continuing_35
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        change lauren desire by 10
                    wt_image cheater_continuing_hypno_4
                    "She seems comfortable going home carrying your load inside her."
                elif lauren.test('desire', 60):
                    wt_image cheater_continuing_38
                    lauren.c "That feels good."
                    player.c "And?"
                    lauren.c "Thank you for letting me ride you."
                    player.c "Do a good job of it , slut."
                    wt_image cheater_continuing_11
                    "She begins moaning loudly as soon as she starts riding you ..."
                    lauren.c "oooo  ...  ooooooo"
                    wt_image cheater_continuing_39
                    "... and cums rapidly."
                    lauren.c "Aaahhhh!!!!"
                    wt_image cheater_continuing_12
                    player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                    wt_image cheater_continuing_34
                    "With Lauren riding you up and down ..."
                    wt_image cheater_continuing_36
                    "... faster and faster ..."
                    wt_image cheater_continuing_34
                    "... it doesn't take you long to cum, either."
                    wt_image cheater_continuing_35
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_hypno_4
                    "She seems comfortable going home carrying your load inside her."
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_43
                else:
                    wt_image cheater_continuing_35
                    lauren.c "About what?"
                    wt_image cheater_continuing_37
                    player.c "About having the opportunity to ride up and down my hard cock."
                    wt_image cheater_continuing_36
                    "She can't bring herself to say anything, but she can bring herself to ride you ..."
                    wt_image cheater_continuing_34
                    "... up and down ..."
                    wt_image cheater_continuing_36
                    "... faster and faster."
                    wt_image cheater_continuing_34
                    "She's turned on, but enough to cum ..."
                    lauren.c "oooo"
                    wt_image cheater_continuing_35
                    "... unlike you."
                    wt_image cheater_continuing_37
                    player.c "[player.orgasm_text]"
                    lauren.c "Oh!"
                    wt_image cheater_continuing_hypno_6
                    "She dresses quietly, avoiding eye contact with you again."
                    player.c "You enjoyed that, slut.  Why not admit it?"
                    "She did, but she won't.  Not yet, anyway."
                    change lauren desire by 5
            $ lauren.sex_count += 1
            orgasm notify
        "Anal" if lauren.sex_count >= 1 and (lauren.has_tag('blackmailed') or not lauren.has_tag('no_anal')):
            if lauren.cheated == 0:
                $ lauren.cheated = 1
            wt_image cheater_continuing_13
            player.c "Hands and knees, slut. Face away from me and pull down your pants."
            if lauren.has_tag('accepts_anal'):
                wt_image cheater_continuing_40
                "She knows what's coming as soon as she sees you apply the lube to your cock."
                if lauren.test('submission', 125):
                    player.c "It must feel good, knowing you can please me using all three holes."
                    lauren.c "Yes, Sir."
                    player.c "You should thank me for giving you this opportunity."
                    wt_image cheater_continuing_42
                    lauren.c "Thank you for using me as your asswhore, Sir."
                    wt_image cheater_continuing_15
                    "She doesn't really enjoy being taken this way, but that doesn't make the experience any less enjoyable for you."
                else:
                    wt_image cheater_continuing_41
                    player.c "It must feel good, knowing you can please me using all three holes."
                    wt_image cheater_continuing_15
                    "It doesn't actually feel good for her. She's a woman who loves sex, but not this type of sex. Still, she puts up with it as you enjoy yourself with her butt."
                player.c "[player.orgasm_text]"
                wt_image cheater_continuing_26
                player.c "If you're going to sit like that to put your shoes on, get your pants all the way up first.  I don't want the mess in your ass dripping out on my furniture."
            elif lauren.has_tag('blackmailed'):
                add tags 'accepts_anal' to lauren
                wt_image cheater_continuing_40
                lauren.c "What are you doing?"
                player.c "Putting lube on my cock.  Do you think you need it?"
                lauren.c "I'm not sure.  It's not usually needed."
                if lauren.has_tag('no_anal'):
                    rem tags 'no_anal' from lauren
                    player.c "What if I told you that whole agreement where I wouldn't take you anally is out the window now that you're my bitch. Now do you think you need it?"
                else:
                    player.c "I think you'll want it for where I'm putting my cock today."
                wt_image cheater_continuing_15
                "She does her best not to cry out as you claim her ass, but a low guttural groan escapes anyway."
                lauren.c "nnnnnn"
                if lauren.has_tag('whore') or lauren.has_tag('whore_in_training'):
                    player.c "Make sure to collect extra from your clients when they take you this way, asswhore. I'm the only one you give this up for free to."
                "You'd like to make this last, but her butt is so tight and the sounds she makes as you ream her are so enjoyable that her bowels are soon flooded with your seed."
                player.c "[player.orgasm_text]"
                wt_image cheater_continuing_1
                player.c "Don't look so sad. Just because you're my asswhore now doesn't mean I'll always use you this way. I'll likely want you to serve me with one of your other holes once in a while."
            else:
                add tags 'accepts_anal' to lauren
                wt_image cheater_continuing_40
                lauren.c "What are you doing?"
                player.c "Putting lube on my cock."
                lauren.c "Why?  I don't need that."
                player.c "You will for where I'm putting my cock."
                wt_image cheater_continuing_15
                "She's too much the obedient slut to object as you claim her ass, but the low guttural groans she emits are a clue to how difficult she finds accepting this."
                lauren.c "nnnnnn"
                if lauren.has_tag('whore') or lauren.has_tag('whore_in_training'):
                    player.c "Make sure to collect extra from your clients when they take you this way, asswhore. I'm the only one you give this up for free to."
                "You'd like to make this last, but her butt is so tight and the sounds she makes as you ream her are so enjoyable that her bowels are soon flooded with your seed."
                player.c "[player.orgasm_text]"
                wt_image cheater_continuing_1
                player.c "Don't look so sad. Just because you're my asswhore now doesn't mean I'll always use you this way. I'll likely want you to serve me with one of your other holes once in a while."
            $ lauren.anal_count += 1
            orgasm notify
        #"Take her to the dungeon" if lauren.punishment_count > 1 or lauren.submission > 100 or lauren.has_tag('blackmailed'):
            ## NEED ADD WHEN HAVE TIME
        "Nothing today":
            wt_image cheater_continuing_19
            "You speak briefly with Lauren then send her away. She's a bit confused - maybe even a bit disappointed? - that you dismiss her without touching her."
    call character_location_return(lauren) from _call_character_location_return_476
    return

# Blackmail
label lauren_blackmail_her:
    "Lauren's husband wouldn't be very happy about her continuing to see you now that her training's over.  If you told him about what she's been doing with you, he'd divorce her for sure."
    $ title = "What do you do?"
    menu:
        "Ignore for now":
            "You decide to ignore her indiscretion for the time being."
        "Ignore permanently":
            "Blackmailing Lauren would mess up your current relationship with her. You discard the idea."
            $ lauren.cheated = 3
        "Threaten to inform her husband":
            player.c "I have bad news for your husband."
            wt_image cheater_continuing_19
            lauren.c "My husband?"
            player.c "Yes, I failed in my training of you."
            lauren.c "What do you mean?"
            player.c "He wanted you to be a proper obedient slut for him."
            lauren.c "I have been!"
            player.c "An obedient slut doesn't run around on him with other men."
            lauren.c "But I haven't ..."
            player.c "Yes, you have.  With me."
            wt_image cheater_continuing_20
            "Lauren goes cold."
            lauren.c "Everything we've done, you told me to do."
            player.c "A test.  One you failed."
            lauren.c "What do you want from me?"
            $ title = "What do you want?"
            menu:
                "Blackmail her":
                    call lauren_blackmail_choices from _call_lauren_blackmail_choices
                    call character_location_return(lauren) from _call_character_location_return_477
                "Ruin her":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "I wanted you to be obedient to your husband, as you were trained to be."
                    wt_image cheater_first_strip_1
                    player.c "Since you weren't, I have no choice but to tell him.  Unlike you, I'm loyal to your husband.  Goodbye, Lauren."
                    "Her husband is angry when you call him, but soon settles down and thanks you for letting him know about Lauren's transgression.  With your evidence, he's able to win a favorable divorce result."
                    "Things are less rosy for Lauren.  She lost her husband, her money, and her old life.  Cheating doesn't pay."
                    # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
                    # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
                    # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
                    call convert(lauren,'unavailable') from _call_convert_81
                    #$ lauren.status = "lost"  ## not needed given above
                    #rem tags 'satisfied' from lauren  ## not needed as all tags removed during convert)unavailable)
                    #rem tags 'continuing_actions' from lauren
                    dismiss lauren
                    wt_image current_location.image
    return

label lauren_blackmail_choices:
    $ lauren.cheated = 2
    add tags 'blackmailed' 'swingers_room_possible' to lauren
    $ title = "What do you want from her?"
    menu:
        "Pimp her out" if not lauren.has_tag('whore'):
            player.c "You've been a whore for a while, Lauren, running around on your husband.  It's time to graduate from amateur to professional."
            lauren.c "What do you mean?"
            player.c "I mean you're going to have sex with men for money. Men I select for you. The money you will bring to me, although you can keep the tips, if you earn any."
            lauren.c "You're going to be my pimp?"
            player.c "And you're going to be my whore.  Are we clear?"
            "She nods, sullenly."
            player.c "Then get over here and show me how a whore thanks her pimp for getting her work."
            if lauren.blowjob_count < 2:
                wt_image cheater_continuing_5
                "You have to teach her how to suck a cock properly ..."
                wt_image cheater_continuing_6
                "... including how to pleasure a man's balls."
                wt_image cheater_continuing_24
                "You can't have an unskilled laborer working for you."
            wt_image cheater_continuing_6
            "Lauren acquiesced relatively easily, and you think you can guess why."
            wt_image cheater_continuing_8
            "Selling her body may be repulsive to her, but it provides an opportunity to have sex with men other than her husband - or you."
            wt_image cheater_continuing_7
            "She'd much rather explore her sexual urges with men of her choosing, but she's learned with you that she can make do with men not of her choosing, if those are the only ones available."
            wt_image cheater_continuing_25
            player.c "[player.orgasm_text]"
            wt_image cheater_continuing_24
            player.c "I'll let you know when your first john is lined up. I know you'll be excited anticipating meeting him, but no playing with yourself until then. The hornier you are, the happier your client is likely to be."
            call lauren_convert_whore from _call_lauren_convert_whore
            $ lauren.blowjob_count += 1
            $ lauren.swallow_count += 1
            orgasm notify
        "Have her work as a showgirl" if not lauren.has_tag('showgirl') and not lauren.has_tag('waiting_for_club_access'):
            player.c "Let's face it, Lauren.  You're too big a slut to be restricted to your husband, or even your husband and me.  You need to share your talents with the world."
            lauren.c "What the hell are you talking about?"
            if player.has_tag('club_first_visit_complete'):
                player.c "I'm a member of a private Club.  You're going to dance there.  And by dance, I mean take off your clothes and entertain the audience."
                player.c "It won't get back to your husband.  The Club is very strict about privacy.  You may even come to thank me some day."
                player.c "Access to the Club may give you opportunities to satisfy your urges.  Because you know as well as I that no matter how much you want to, you'll never be able to stay faithful to your husband."
                "She doesn't say anything, but you know she agrees."
                player.c "They'll be waiting for you tomorrow.  Buy something even sluttier than normal to wear for your first shift.  You want to make a good impression."
                call lauren_convert_showgirl from _call_lauren_convert_showgirl_1
            else:
                player.c "I'm going to find the right situation for you, a woman who can't keep her clothes on.  I'm not sure what it will be yet, but once I do I'll let you know."
                add tags 'waiting_for_club_access' to lauren
            player.c "In the meantime, you can practice your strip tease act with me.  Now."
            wt_image cheater_first_strip_1
            "Lauren's used to following your commands.  With a sigh, she spins around."
            wt_image cheater_first_strip_2
            "When she turns back, she pulls down her top to display her breasts."
            wt_image cheater_first_strip_3
            "Then she loses the top and starts to pull down her pants."
            player.c "Stop. You're not enjoying this and I know you're not enjoying this. The secret to entertaining is to make the audience believe you're enjoying yourself, even when you're not."
            player.c "Make me believe you want to be taking your clothes off for me."
            wt_image cheater_first_strip_4
            "Lauren strikes a pose and puts on a fake smile."
            player.c "Better, but the idea is to arouse your audience.  To do that, you need to look like you're aroused, too."
            wt_image cheater_first_strip_5
            player.c "That's it. Try again, from the beginning. We're going to keep at this until you know how to work a crowd."
            wt_image cheater_first_strip_6
            "You make her dance and strip for you over and over again, until you're comfortable she won't embarrass herself - or you - when she gets up on stage."
            change player energy by -energy_long notify
        "Ask for 1000":
            player.c "I'll ignore your indiscretion in return for monetary compensation. 1000 should do it."
            lauren.c "I can't lay my hands on that much money right now."
            player.c "Sure you can. Just think about how much money your husband will be laying his hands on if he divorces you."
            lauren.c "Fine. But this is the only money I'm giving you."
            player.c "Plus you'll make yourself available to me sexually any time I want."
            lauren.c "You're kidding?"
            player.c "That's the deal. Take it or go through a divorce. Your choice."
            "Lauren storms out, but the money arrives before the end of the day."
            change player money by 1000 notify
    return

# Contact - Arrange Meeting Lauren and Sophie
label lauren_contact_arrange_meeting:
  if sophie.relationship_status > 6 and not lauren.has_tag('transformed') and (lauren.status == "post_training" and lauren.has_tag('continuing_actions')):
    summon lauren
    summon sophie
    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ sophie.training_session()
    wt_image cheater_sorry_1
    lauren.c "What's so important I needed to come here right away?  I have a board meeting to prepare for."
    player.c "There's someone here for you to apologize to."
    wt_image cheater_sorry_19
    lauren.c "Apologize?  To who?"
    if lauren.revenge_count > 1:
      lauren.c "Is this for something I did, or am I standing in as a revenge double again for some other woman's transgression?"
      player.c "This time the wrong is all yours.  Lucky for you, I've arranged an opportunity for you to say you're sorry."
      lauren.c "To who?"
    player.c "You'll find out in a moment.  Get down on all fours and follow me."
    wt_image cheater_sorry_20
    lauren.c "On all fours?"
    player.c "Yes.  It's called crawling.  Its a sign of humility, and a nice gesture of respect when you want your apology to seem sincere."
    lauren.c "I still don't know who..."
    player.c "Get on the ground now."
    wt_image cheater_sorry_2
    "Lauren stops arguing and gets down on her hands and knees."
    player.c "Eyes down towards the floor. Follow me."
    "She crawls beside you as you lead her down the hallway."
    wt_image cheater_sorry_3
    "As instructed, she keeps her eyes down as crawls along beside you.  She doesn't stop until a pair of expensive pink shoes enter her line of vision."
    wt_image cheater_sorry_21
    "Sophie sits where you asked her to, on the floor at the end of the hallway. She's been watching you lead Lauren towards her on all fours."
    wt_image cheater_sorry_4
    "She's breathing more heavily than when you left her, suggesting she's enjoyed the sight of her former boss crawling towards her."
    wt_image cheater_sorry_6
    player.c "We have a bit of a problem here. Your head's almost level with Sophie's. It's traditional when asking forgiveness for the supplicant's head to be lower than the woman she wronged."
    wt_image cheater_sorry_7
    "Lauren lowers herself down to her belly."
    wt_image cheater_sorry_22
    "Sophie's eyes narrow as her former boss prostrates herself in front of her.  Despite herself, Lauren can't help but look as Sophie opens her legs."
    sophie.c "You were a real bitch to me, you know? Not just the firing, either. You were never happy with my work. You never made me feel appreciated. You were a real cunt."
    wt_image cheater_sorry_23
    sophie.c "I want to see you get even lower.  I want you eye level with my cunt when you apologize."
    wt_image cheater_sorry_8
    player.c "Eyes down, Lauren.  No one said you could look up."
    wt_image cheater_sorry_9
    lauren.c "I'm sorry."
    player.c "How's she supposed to hear you from over there?  She wants you to address her cunt, cunt.  Get closer."
    wt_image cheater_sorry_24
    "The corporate executive places her head directly between her former employee's knees."
    lauren.c "I'm sorry I was a cunt to you."
    wt_image cheater_sorry_10
    "You didn't discuss this next part with Sophie beforehand, but Lauren's ex-receptionist is breathing hard and you're pretty sure she'll follow your lead."
    player.c "Lauren, show Sophie that she's appreciated, and that you mean it when you say you're sorry.  This is your chance to make amends."
    wt_image cheater_sorry_11
    "Sophie gasps in surprise as Lauren starts licking her pussy.  She knew Lauren would apologize to her in a humiliating position, but not that the apology would be physical."
    wt_image cheater_sorry_12
    "Her face is a mass of confusion, but she makes no effort to push Lauren away.  Within minutes, you can both smell and hear the sounds of Sophie's arousal."
    sophie.c "oh .. oh ... oh ... ohhhh ...."
    wt_image cheater_sorry_25
    sophie.c "ohhhh .... ohhhhh  ..... OH!  I'm not a lesbian!!"
    "You fight hard to stifle a laugh at the timing of Sophie's declaration as she bucks to orgasm at the end of her former boss' decidedly female tongue."
    wt_image cheater_sorry_10
    player.c "Lauren's not a lesbian either Sophie.  Yet she licked your cunt to orgasm."
    player.c "I think that demonstrates better than any words could that she is, indeed, sorry that she let you feel unappreciated when you worked for her, and that she's sorry for the trouble she caused by firing you."
    $ title = "What do you do now?"
    menu:
      "Ask for your own appreciation" if lauren.blowjob_count > 1:
        wt_image cheater_sorry_26
        player.c "Now that Sophie's feeling appreciated, it's time for me to feel appreciated, too.  Get over here and suck my cock."
        wt_image cheater_sorry_27
        "You knew Lauren would comply."
        wt_image cheater_sorry_13
        "It's a happy surprise to see Sophie act as if the instruction was directed to her, too."
        wt_image cheater_sorry_28
        "The two women coordinate their actions very smoothly.  Perhaps its because they used to work together?"
        wt_image cheater_sorry_29
        "You know this is a one time event, so you stretch it out as long as you can, using every technique you can think of to delay your orgasm."
        wt_image cheater_sorry_30
        "The former boss-receptionist team also have some techniques clearly intended to overcome your self-restraint."
        "Despite their best efforts, you're pleased with yourself that you're able to keep the two of them working on your cock and balls for a good half-an-hour."
        wt_image cheater_sorry_31
        "Sophie receives the bulk of your sperm when you finally let yourself go."
        wt_image cheater_sorry_32
        player.c "[player.orgasm_text]"
        wt_image cheater_sorry_16
        "From the look on Lauren's face, she's jealous.  Maybe she's always been jealous of Sophie?  That might explain a lot."
        $ lauren.blowjob_count += 1
        $ sophie.blowjob_count += 1
        orgasm
      "Fuck Lauren while Sophie watches" if lauren.sex_count > 1:
        wt_image cheater_sorry_26
        player.c "Now that Sophie's feeling appreciated, it's time for me to feel appreciated, too.  Get over here and sit on my cock."
        wt_image cheater_sorry_33
        "Sophie watches with interest as her ex boss begins to strip. The definitely-not-a-lesbian former receptionist is clearly finding the whole situation arousing."
        wt_image cheater_sorry_34
        player.c "Sophie, when Lauren gets on top of me, could you please put my cock inside her? I won't be able to reach."
        wt_image cheater_sorry_40
        sophie.c "That's a lame way to ask me to put my hand on your cock, you know."
        wt_image cheater_sorry_36
        "You know. It's possibly the lamest thing you've ever said. But it offers Sophie an opportunity to participate and she takes it."
        wt_image cheater_sorry_17
        "As Lauren rides you, you feel a hand caressing and teasing your balls. You can't see what's going on, but you're pretty sure Lauren's hands are accounted for ..."
        wt_image cheater_sorry_18
        "... and you know for certain Lauren's tongue can't reach that far."
        wt_image cheater_sorry_38
        "Maybe its a quid-pro-quo for you providing Lauren's cunt licking apology. Maybe she's so consumed with lust she can't help herself."
        wt_image cheater_sorry_37
        "Whatever the reason, Sophie makes this the best fuck Lauren's ever given you."
        player.c "[player.orgasm_text]"
        wt_image cheater_sorry_39
        $ lauren.sex_count += 1
        orgasm
      "Let them go home":
        "Lauren's demonstrated her obedience to you and Sophie's received her apology (along with what was - presumably - her first orgasm from another woman). That's a good day's work."
        wt_image cheater_sorry_4
    "The two women seem a little awkward around each other afterwards, so you let them both go home."
    add tags 'receptionist_sex_complete' to lauren
    change player energy by -energy_short notify
    call character_location_return(lauren) from _call_character_location_return_478
    call character_location_return(sophie) from _call_character_location_return_479
  else:
    "You can no longer arrange this meeting."
    add tags 'shut_off_receptionist_sex' to lauren
  return

# Contact - Ask Lauren about Firing Sophie
label lauren_contact_fire_sophie:
  if lauren.has_tag('transformed') or (lauren.status == "post_training" and lauren.has_tag('unsatisfied')) or (lauren.status == "post_training" and lauren.has_tag('satisfied') and not lauren.has_tag('continuing_actions')) or lauren.status == "unavailable":
    "You can no longer have this conversation with Lauren."
  else:
    wt_image cheater_office_phone_1
    "You give Lauren a call."
    player.c "What's up with firing Sophie?"
    wt_image cheater_office_phone_2
    lauren.c "You should know.  I can't have her finding out about our relationship over pillow talk with you and blabbing it all over the office."
    player.c "And if she finds out now, what keeps her from telling everyone?"
    lauren.c "Who would believe her now?  A bitter ex-employee spreading crazy rumors."
    player.c "So to protect yourself, you'd ruin her career?"
    lauren.c "Her career?  She's a lousy receptionist.  I should have fired her months ago, and likely would have fired her soon regardless."
    wt_image cheater_office_phone_1
    lauren.c "So no, before you ask, you can't make me rehire her. I don't care what threats you make. I'll go to the wall on this one. Anyway, with her looks, she'll find another job in a couple of weeks."
    wt_image current_location.image
    "You'll need to think of another way to help Sophie, if you want to."
  add tags 'shut_off_fire_receptionist' to lauren
  return

# Contact - Pimp Out Cheater
label lauren_contact_pimp:
  $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
  $ lauren.whore_count += 1
  if lauren.whore_count == 1:
    if lauren.has_tag('blackmailed'):
      wt_image cheater_office_phone_2
      player.c "Lauren, I have your first john lined up. He's a successful business person, much like yourself. I'm sure the two of you have a lot in common, but remember to talk about him, not you. He's paying for your time. Make it special for him."
      player.c "I'm sending you the address of the restaurant where you're to meet him. Dress conservatively. Bring the money to me once you're done. You can keep any tips."
      lauren.c "Do I have to do this?  What if I just pay you, instead?"
      player.c "Don't be silly. You're worth more to me on your back than you are behind that desk. Plus this way you get to have a day career and a night career."
      wt_image cheater_pimp_1_1
      "Lauren waits nervously for her 'date' to arrive. She feels sick to her stomach, and though she keeps telling herself she can do this, she's not sure she can."
    elif lauren.has_tag('transformed'):
      wt_image cheater_office_phone_1
      player.c "Lauren, I have your john lined up. He's a successful business person. Act like you're one yourself. Hell, maybe play it shy, like you haven't fucked a man for money before."
      player.c "I'm sending you the address of the restaurant where you're to meet him. Dress conservatively. Bring my share of the money to me once you're done.  You can keep any tips."
      wt_image cheater_pimp_1_1
      "Lauren waits for her 'date' to arrive. To her surprise, she feels nervous. She's not sure why that is? Hasn't she always been a whore? She shouldn't be worried about whether she knows him or whether he'll recognize her."
      "She keeps telling herself that, but it doesn't make the butterflies in her stomach go away."
    else:
      sys "We're not sure how you're pimping Lauren out if she wasn't blackmailed or transformed. Need to add content for this new route."
    wt_image cheater_pimp_1_2
    "A quick look at his suit and cuff links when he arrives tells her he's not just a successful business person - he's way out of her league wealthy. That explains his choice of restaurant - one of the most expensive and exclusive in the city."
    if lauren.has_tag('blackmailed'):
      "To her relief, she's never met him before."
    wt_image cheater_pimp_1_3
    lauren_whore_client_1 "So tell me about yourself."
    "Lauren looks away, embarrassed."
    wt_image cheater_pimp_1_14
    lauren.c "I'd rather not talk about me."
    wt_image cheater_pimp_1_4
    lauren_whore_client_1 "Okay.  How about we order something to eat.  What looks good to you?"
    lauren.c "I don't feel like eating."
    wt_image cheater_pimp_1_15
    "Being a whore for the first time can take away a girl's appetite, but her date doesn't know that."
    lauren_whore_client_1 "You don't want to talk. You don't want to eat. Am I wasting your time, or are you here to waste mine?"
    wt_image cheater_pimp_1_14
    lauren.c "I'm not ... I'm not trying to waste your time."
    wt_image cheater_pimp_1_5
    "Annoyed, he moves his chair closer to her."
    lauren_whore_client_1 "Prove it. Pull up your skirt. You can do that, can't you? Or is that something else you don't feel like doing?"
    wt_image cheater_pimp_1_15
    "Lauren pulls her skirt up, exposing her bare thighs above her stockings.  As she does, her 'date' places his hand on her leg."
    lauren_whore_client_1 "Higher"
    wt_image cheater_pimp_1_6
    lauren.c "The waitress ..."
    lauren_whore_client_1 "Works for me. This is my restaurant. Shareen, please close this section. My guest and I would like some privacy. I'll call you when we're ready for you to take our orders."
    wt_image cheater_pimp_1_5
    lauren_whore_client_1 "You don't want to talk and you don't want to eat, so I assume you want to get right to the fucking? So get to it. Make me want to fuck you."
    wt_image cheater_pimp_1_7
    "Lauren reaches over and takes out his cock.  His voice may be annoyed with her, but his cock is happy.  It's already rock hard as she takes it out of his pants."
    lauren_whore_client_1 "Pull your skirt up higher.  I don't like having to ask for things twice."
    wt_image cheater_pimp_1_17
    lauren_whore_client_1 "Play with yourself while you stroke me."
    "To Lauren's surprise, he's not the only one getting excited."
    wt_image cheater_pimp_1_8
    "He stands up and tilts her head up by the chin."
    lauren_whore_client_1 "Since you don't use your mouth to talk or to eat, I assume you have something else you prefer to do with it?"
    wt_image cheater_pimp_1_9
    "Without a word, Lauren wraps her lips around his cock."
    wt_image cheater_pimp_1_18
    "If she thought she was going to get away with just a blow job, she soon learns otherwise.  He lets her suck him for a while ..."
    wt_image cheater_pimp_1_10
    "... then roughly pulls her to her feet and tosses her on to the table, sending the dishes flying."
    wt_image cheater_pimp_1_19
    "From behind the privacy screen, the waitress calls in."
    shareen_lauren "Is everything all right in there?"
    lauren_whore_client_1 "Everything's fine, Shareen.  My guest and I are just about to conclude a business transaction."
    wt_image cheater_pimp_1_20
    "The man pulls Lauren's panties aside and slams into her, hard."
    wt_image cheater_pimp_1_21
    "He fucks her roughly as she does her best to keep either of them from making any sounds that could be overheard in the rest of the restaurant."
    wt_image cheater_pimp_1_22
    "Just as she thinks he's about to cum, he pulls her upright ..."
    wt_image cheater_pimp_1_12
    "... and pulls up her blouse."
    wt_image cheater_pimp_1_23
    lauren_whore_client_1 "I didn't get a dinner date or a conversation out of you, but I will see those tits of yours as I cum on you."
    wt_image cheater_pimp_1_13
    "Her tits displayed above her bra, Lauren kneels down and accepts his load on her face, tongue and chest."
    wt_image cheater_pimp_1_24
    lauren_whore_client_1 "Not bad.  The reluctant business woman act was kind of cute, once I realized what you were doing."
    lauren_whore_client_1 "You should have asked me what I wanted first, though. I was more in the mood for a foot job under the table while we ate, followed by a blow job over dessert."
    lauren_whore_client_1 "You're pretty, though, and not a bad fuck.  Money well spent, I think.  Do you take Visa?"
    lauren.c "What?  No ..."
    lauren_whore_client_1 "I'm just teasing you. Here you go, our agreed on fee, in cash, plus a little tip. I'm surprised you didn't want that upfront. Most girls do."
    $ player.whore_income += 50
  elif lauren.whore_count == 2:
    wt_image cheater_pimp_2_1
    "For her second 'date', you send Lauren to an upscale hotel to meet with a business man from out of town."
    wt_image cheater_pimp_2_2
    "Remembering the advice she was given, she sits down and introduces herself to tonight's boyfriend."
    lauren.c "So, what would you like to do tonight?"
    lauren_whore_client_2 "Well, I'd definitely like to see more of you.  Then perhaps you could suck my cock before I fuck you?"
    wt_image cheater_pimp_2_3
    if lauren.has_tag('blackmailed'):
      "Nothing too shocking there. Lauren collects her payment, and counts it in the bathroom, trying - unsuccessfully - not to think about how she's now a woman who sells her body for money."
    elif lauren.has_tag('transformed'):
      "Nothing too shocking there. Lauren collects her payment, and counts it in the bathroom as she tries to figure why she's still nervous about doing the thing she loves most - selling her body for money."
    else:
      sys "We're not sure how you're pimping Lauren out if she wasn't blackmailed or transformed. Need to add content for this new route."
    wt_image cheater_pimp_2_4
    "She tries to ignore the sickening feeling in her stomach ..."
    wt_image cheater_pimp_2_10
    "... as she gets herself ready for the man she's supposed to entertain."
    wt_image cheater_pimp_2_5
    "In true whore fashion, she puts on a smiling face as she makes an impressive entrance."
    wt_image cheater_pimp_2_6
    "At his request, she pulls off her bra before sucking his cock. This part doesn't feel too difficult, though she finds it easier when she focuses on his penis, rather than his face."
    wt_image cheater_pimp_2_11
    if lauren.has_tag('blackmailed'):
      "She finds it more difficult when he's ready to fuck her.  A wave of shame floods over her as she let's him penetrate her."
    elif lauren.has_tag('transformed'):
      "She finds it more difficult when he's ready to fuck her.  Even though she knows this is what whores do, a wave of shame floods over her as she let's him penetrate her."
    else:
      sys "We're not sure how you're pimping Lauren out if she wasn't blackmailed or transformed. Need to add content for this new route."
    wt_image cheater_pimp_2_7
    "When he starts fucking her from behind, though, she can feel her body getting excited. He's excited, too, and it doesn't take him long to cum. Lauren tells herself she can't possibly be disappointed."
    wt_image cheater_pimp_2_7
    lauren_whore_client_2 "We still have some time.  I'm pretty sure I can go another round.  How about you ride me?"
    wt_image cheater_pimp_2_8
    "Having just cum, he's able to control himself longer this time.  Lauren begins to feel the familiar sensation of a pending orgasm building up inside her, when he suddenly groans and cums first."
    wt_image cheater_pimp_2_9
    "'Oh my god!' she thinks to herself as she cleans up in the bathroom. Did I almost cum fucking a stranger for money???"
    if lauren.cheated != 2:
      extend " No wonder I've always wanted to be a whore!"
    $ player.whore_income += 50
  elif lauren.whore_count == 3:
    wt_image cheater_pimp_3_9
    "Lauren has quickly become an 'old pro' at the prostitution game.  You set her up for another hotel visit with a travelling business man."
    wt_image cheater_pimp_3_1
    "She collects her money upfront with a smile, after checking to see what he wants."
    lauren_whore_client_3 "Entertain me for a bit, will you?  Then I'd like to feel your body against mine."
    lauren.c "No problem."
    wt_image cheater_pimp_3_10
    if lauren.has_tag('showgirl'):
      "Lauren's become quite adept at removing her clothes."
      wt_image cheater_pimp_3_2
      "There's no music or lightshow here, but she dances as she strips for him just as if she were on stage."
      wt_image cheater_pimp_3_3
      "Then she gives him a lap dance just as if he had taken her to a private booth after her show."
    else:
      "Lauren slips out of her dress as her date watches."
      wt_image cheater_pimp_3_2
      "She doesn't put on my much of a show, but he seems happy anyway."
      wt_image cheater_pimp_3_3
      "She proceeds to give him her best attempt at a lap dance. It's something new for her, but she understands the principal easily enough, and he seems to enjoy it."
    wt_image cheater_pimp_3_11
    "His body has the expected response to her gyrations. Flattered by the bulge in his pants, she unzips him and gently licks his cock."
    lauren.c "Would you like me to suck you now?"
    wt_image cheater_pimp_3_4
    lauren_whore_client_3 "Yes, please."
    wt_image cheater_pimp_3_12
    "Such a gentleman, saying please."
    wt_image cheater_pimp_3_13
    "She rewards his politeness with an enthusiastic blowjob."
    wt_image cheater_pimp_3_14
    lauren_whore_client_3 "Could you deepthroat me, too, please?  My wife isn't very good at that."
    wt_image cheater_pimp_3_5
    "Deepthroating isn't Lauren's best skill, either, but she's competitive."
    wt_image cheater_pimp_3_15
    "And if she's being honest with herself, she's also turned on by being able to please this man in a way his wife can't."
    wt_image cheater_pimp_3_16
    "So turned on, that she doesn't wait for him to ask to fuck her.  She climbs on top of him and starts to ride him."
    wt_image cheater_pimp_3_6
    "The feeling of him inside her, his chest under her hands, his pubic bone striking against her clit on every downstroke, soon has her moaning."
    lauren.c "oooo"
    wt_image cheater_pimp_3_17
    "Noticing her excitement, he holds back his own orgasm while teasing her, licking her nipples ..."
    lauren.c "oooo"
    wt_image cheater_pimp_3_18
    "... and squeezing her breasts as she rides him faster and faster ..."
    lauren.c "oooooo"
    wt_image cheater_pimp_3_19
    "... to a body shaking climax."
    lauren.c "Aaahhhh!!!!"
    wt_image cheater_pimp_3_16
    lauren_whore_client_3 "Did that feel good?"
    lauren.c "Yes!  What can I do for you so you feel good, too?"
    lauren_whore_client_3 "Can I fuck you from behind and then cum on your face?"
    wt_image cheater_pimp_3_20
    lauren.c "Okay"
    wt_image cheater_pimp_3_21
    "His hard cock thrusting in and out of her feels good ... really good."
    lauren.c "oooooo"
    wt_image cheater_pimp_3_22
    "And when it occurs to her that he's happy to be getting to fuck her right now, instead of his wife, the thought puts her over the edge."
    lauren.c "Aaahhhh!!!!"
    wt_image cheater_pimp_3_23
    lauren_whore_client_3 "Are you sure it's okay if I cum on your face?"
    wt_image cheater_pimp_3_24
    "How could she refuse?  He's a gentleman and she's a pro."
    wt_image cheater_pimp_3_8
    sys "Lauren knows what she's doing now, and has developed a nice reputation online. The website you set up for her will provide a steady stream of customers."
    sys "You no longer need to spend any time or Energy to pimp her out. She'll keep working tricks for you and provide your cut at the end of each week. You can take a smaller cut now that it requires no Energy to pimp her out."
    sys "You should check in with her once and a while, however, to make sure she's doing okay."
    $ lauren.whore_lost_countdown = 5
    $ player.whore_income += 25
  change player energy by -energy_short notify
  return

# Check On Whore
label lauren_check_whore:
  ## Transformed?
  if lauren.has_tag('transformed'):
    wt_image cheater_pimp_3_9
    player.c "How's my favorite professional cock sucker?"
    lauren.c "Pretty good, according to the customers."
    player.c "Not holding out on me, are you?"
    "She hesitates just long enough to let you know she probably is, but not too much, based on the income she's bringing in for you."
    lauren.c "Of course not!"
    player.c "Good. If you get into trouble, you let me know. I'll look out for you."
    lauren.c "How sweet!"
    player.c "Just looking after my favorite professional."
    $ lauren.whore_lost_countdown = 7
  ## Blackmailed?
  elif lauren.has_tag('blackmailed'):
    wt_image cheater_office_phone_2
    player.c "How's my favorite professional cock sucker?"
    lauren.c "You're disgusting."
    player.c "Not holding out on me, are you?"
    lauren.c "Of course not!"
    player.c "Good. If you get into trouble, you let me know. I'll look out for you."
    lauren.c "How sweet."
    "Her sarcasm is obvious."
    player.c "Just looking after my assets. I don't have many corporate executives whoring for me. I'd hate to lose you."
    $ lauren.whore_lost_countdown = 5
  else:
    sys "Lauren's not blackmailed or transformed, but she's your whore anyway. You should add some content here for this new path."
    $ lauren.whore_lost_countdown = 5
  return

# View Relationship Status
label lauren_relationship_status:
    call lauren_description_display from _call_lauren_description_display
    wt_image current_location.image
    return

# Review Files
label lauren_review_files:
    call lauren_description_display from _call_lauren_description_display_1
    wt_image current_location.image
    return

# Description Display
label lauren_description_display:
    wt_image lauren.image
    if lauren.status == "post_training":
        ## main description
        if lauren.has_tag('petgirl') and lauren.has_tag('fetch_toy_used'):
            "Lauren the Cheater is now [lauren.full_name], although Lauren the She-Wolf might be a better description."
            "She's not domesticated and will bite if you get too close.  For her safety and the safety of those around her, you need to keep her locked up in her cage at all times, except when she's playing with her fetch toy."
        elif lauren.has_tag('petgirl'):
            "Lauren the Cheater is now [lauren.full_name], although Lauren the She-Wolf might be a better description."
            "She's not yet domesticated and will bite if you get too close.  For her safety and the safety of those around her, you need to keep her locked up in her cage at all times."
        elif lauren.has_tag('slavegirl'):
            "[lauren.full_name] waits for you in the position you placed her in."
            "Once she was Lauren the Cheater, a successful business woman struggling to balance the needs of her marriage, her career, and her own sexual libido.  Now she is your property, and happy."
        elif current_location == stage:
            "Lauren the Cheater has become Lauren the Showgirl. It's the perfect way for her to combine her love of money with her inner slut."
        elif lauren.has_tag('bimbo'):
            "Lauren the Cheater was an intelligent, successful businesswoman who cheated on her husband.  In order to keep him, she agreed to be trained by you."
            "Now she's Lauren the Bimbo. She lost her husband, her career, and her brain. But she doesn't worry about those things. All she worries about is whether she's allowed to fuck you?"
            "If she is, she's happy. If she isn't, she tries to amuse herself until she's allowed to fuck you again."
        elif lauren.has_tag('blackmailed'):
            "Lauren the Cheater is none too happy with you blackmailing her."
        elif lauren.has_tag('love_potion_used'):
            "Lauren the Cheater is besotted by the love potion and is happy to fool around with you, even though she's supposed to be an Obedient Slut for her husband."
        elif lauren.has_tag('continuing_actions'):
            "Lauren the Cheater wants to be an Obedient Slut for her husband, but can't help herself from fooling around with you when you demand that of her."
        elif lauren.has_tag('satisfied'):
            "Lauren the Cheater used to fool around on her husband.  Now she's an Obedient Slut who caters to his every sexual whim and, as far as he knows, is loyal to him alone."
        ## relationship status
        if lauren.has_tag('continuing_actions') and not lauren.has_tag('relationship_status_action_removed'):
            add tags 'relationship_status_action_removed' to lauren
            "Lauren will visit you when you call, but that's as much of a relationship as you have."
            $ bedroom.remove_action(lauren.relationship_action)
    elif lauren.status == "on_training":
        "Lauren's husband expects two things as his conditions for not divorcing her: that she stop cheating on him, and that she become his obedient little slut.  To do that, you'll need to help change her view of herself so that she accepts her new relationship with her husband."
        "You have until the end of week [lauren.training_limit] to complete this engagement."
    if not lauren.has_any_tag('bimbo', 'degraded', 'doll', 'petgirl', 'transformed_slavegirl', 'whore'):
        if lauren.has_tag('trigger_implanted'):
            "You have implanted a hypnotic trigger in her."
        if lauren.has_tag('love_potion_used'):
            "She is under the influence of a love potion."
        "[lauren.statblock]"
        $ items = ", ".join(i.name for i in lauren.get_items()) if lauren.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    return

## Character Specific Objects
# Watch Lauren Fuck In Club
# OBJECT: Watch Your Girlfriend - or blackmailed girlfriend in Lauren's case
label lauren_watch:
    if not lauren.can_be_interacted or lauren.cheated != 2:
        "Lauren is not available today."
    else:
        summon lauren
        $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
        wt_image cheater_swing_1_12
        "Lauren's not exactly your girlfriend, but she's also not in any position to refuse you when you tell her to accompany you - barely dressed - to the Swingers Room as your 'girlfriend'."
        wt_image cheater_swing_1_10
        "You have her dress in a too-short skirt with revealing top.  Far from humiliating her, she fits right in, particularly with the younger, hipper members of the crowd."
        wt_image cheater_swing_1_1
        "She joins the dance floor and immediately begins to mix with the crowd."
        wt_image cheater_swing_1_2
        "Lauren's a woman who loves sex.  She takes to the environment of the swinging room like a duck to water.  It doesn't take her long for someone - and something - to catch her eye."
        wt_image cheater_swing_1_3
        "She makes it blatantly obvious to him that she's interested ..."
        wt_image cheater_swing_1_4
        "... and he lets her know he's willing to be a good partner."
        wt_image cheater_swing_1_5
        "After bringing her to a swingers event, you can't complain about her having sex with someone. She takes advantage of the freedom the evening provides to thoroughly enjoy herself."
        wt_image cheater_swing_1_6
        "After all, she doesn't often get to choose whose cock goes into her these days ..."
        wt_image cheater_swing_1_11
        "... or who brings her to orgasm."
        wt_image cheater_swing_1_7
        "For that matter, she rarely gets to decide whose cock she sucks ..."
        wt_image cheater_swing_1_8
        "... or whose cum splats on her face."
        wt_image cheater_swing_1_9
        "Cum dripping down her breasts as she scoops it off her chin and licks it, she notices you watching her."
        lauren.c "Hi.  Having fun?"
        change player energy by -energy_short notify
        call character_location_return(lauren) from _call_character_location_return_480
    return

# Lend to Master M
# OBJECT: Select who you're lending to Master M
label lauren_lend_to_master_m:
    wt_image cheater_kneel_2
    player.c "[lauren.name], get dressed.  I'm sending you to another man."
    wt_image cheater_kneel_3
    lauren.c "Another man?  But, I belong to you, [lauren.your_respect_name]."
    player.c "And you are mine to do what I want with. Today, what I want is for you to go visit Master M and let him do whatever he wants with you. Until he sends you back to me, you will obey him as you would me."
    wt_image cheater_kneel_4
    lauren.c "Yes, [lauren.your_respect_name]"
    wt_image cheater_mm_1
    "It's a few hours later before she returns and undresses."
    player.c "How did it go?"
    lauren.c "Good, I think, [lauren.your_respect_name]."
    player.c "Was he pleased with you?"
    lauren.c "I hope so."
    $ title = "Ask for details?"
    menu:
        "Yes":
            player.c "What did he do with you?"
            wt_image cheater_mm_2
            lauren.c "{i}First he instructed me to strip down to my underwear. He had me stand there, waiting, for some time.{/i}"
            wt_image cheater_mm_3
            lauren.c "{i}Then he made me strip him naked.{/i}"
            player.c "{i}'Made you'?  That sounds like something you'd enjoy doing.{/i}"
            wt_image cheater_mm_4
            lauren.c "{i}I ... I was only following orders, [lauren.your_respect_name]. You told me to obey him as I would you. I wasn't thinking about anything except serving him.{/i}"
            player.c "{i}And how did you serve him?{/i}"
            wt_image cheater_mm_24
            lauren.c "{i}I was required to display my tits for him.{/i}"
            wt_image cheater_mm_25
            lauren.c "{i}Then he sat down in front of me ...{/i}"
            wt_image cheater_mm_5
            lauren.c "{i}... and made me suck his dick, [lauren.your_respect_name].{/i}"
            wt_image cheater_mm_26
            player.c "{i}Another odious task for you, no doubt.  Was that all he wanted from you?{/i}"
            wt_image cheater_mm_6
            lauren.c "{i}For a very long time, yes [lauren.your_respect_name].  He kept me there, pleasuring his cock with my mouth for what seemed like hours.{/i}"
            wt_image cheater_mm_7
            lauren.c "{i}My jaw began to ache and the muscles in my shoulders and neck were screaming at me. Sill he kept me there to suck his cock some more. And some more.{/i}"
            wt_image cheater_mm_8
            lauren.c "{i}I tried to switch to using my hands to pleasure him, but he wouldn't allow it.{/i}"
            wt_image cheater_mm_9
            lauren.c "{i}He made me put my hands down and use only my mouth on him.{/i}"
            wt_image cheater_mm_27
            lauren.c "{i}It was torture, [lauren.your_respect_name]. I didn't think he would ever cum. I lost all track of time. I think I may even have spaced out.{/i}"
            wt_image cheater_mm_10
            "{i}The next thing I remember, he was lifting me up and impaling me on his cock, shooting his load inside me as he entered me.{/i}"
            player.c "{i}Did you cum, too?{/i}"
            wt_image cheater_mm_28
            lauren.c "{i}[lauren.your_respect_name] ... [lauren.your_respect_name], this greedy cunt wanted to cum so bad.  The feel of his cock inside me ...{/i}"
            wt_image cheater_mm_11
            lauren.c "{i}... then the feel of his cum dripping out of me, I thought I would explode. But he told me I wasn't allowed to cum without your permission.{/i}"
            wt_image cheater_kneel_8
            lauren.c "I did my best to please your friend, [lauren.your_respect_name]. I hope I did okay. And if I did do okay, I hope it would amuse you, [lauren.your_respect_name], to let this greedy cunt have an orgasm?"
            $ title = "What do you do?"
            menu:
                "Go on with your day":
                    player.c "I'm sure you did fine, [lauren.name], but I have better things to do than watch you exercise your insatiable libido. And no, you can't touch yourself while I'm not watching, either."
                    wt_image cheater_kneel_10
                    "She's disappointed but not surprised by your response."
                    lauren.c "Yes, [lauren.your_respect_name]"
                    player.c "No 'accidentally' brushing your hands against your cunt while you wait for me, either, cunt."
                    wt_image cheater_kneel_11
                    lauren.c "Yes, [lauren.your_respect_name]"
                "Deny her, cruelly":
                    player.c "No.  Thank me for denying your request."
                    wt_image cheater_kneel_12
                    "She groans in frustration before complying."
                    lauren.c "nnnnnn ... Thank you, [lauren.your_respect_name], for denying my request and reminding this worthless cunt that what it wants does not matter."
                    player.c "Beg me never to let you orgasm again."
                    wt_image cheater_kneel_10
                    lauren.c "[lauren.your_respect_name]??"
                    player.c "You heard me."
                    wt_image cheater_kneel_11
                    "It takes her a moment to collect herself and reply.  When she does, she can barely squeak out the words."
                    lauren.c "{size=-5}[lauren.your_respect_name], if it amuses you, leave this worthless cunt always horny and never let it have an orgasm ever again.{/size}"
                    player.c "I'll think about it."
                "Let her play with herself":
                    player.c "Go on, then.  Make yourself cum for my amusement."
                    wt_image cheater_mm_15
                    lauren.c "Oh!  Thank you, [lauren.your_respect_name]!!"
                    "She rips off her bra and slides a hand into her panties. She's already trembling and you can smell her arousal. You're pretty sure the only thing keeping her from cumming immediately is the knowledge she may not be allowed to play with herself again for a very long time. She wants to make this last as long as she can, but that's not going to be very long."
                    wt_image cheater_mm_16
                    player.c "Look at me while you're touching yourself, [lauren.name]."
                    lauren.c "oooooo .... Yes, [lauren.your_respect_name]."
                    $ title = "Instruct her?"
                    menu:
                        "Use only the panties, no fingers":
                            player.c "Take away your fingers.  Make yourself cum with just the touch of your panties."
                            lauren.c "nnnnn ... Yes, [lauren.your_respect_name]"
                            wt_image cheater_mm_17
                            "You thought that would slow down her orgasm, but it has the opposite effect. Perhaps the humiliation of being reduced to playing with herself this way was more arousing than the feel of her fingers on her clit."
                            lauren.c "oooo ... oooooo ... AAAHHHH!!!"
                            $ lauren.orgasm_count += 1
                        "Remove the panties so you can see":
                            player.c "Take off your panties so I can better."
                            wt_image cheater_mm_19
                            "She rips them off as quick as she can ..."
                            wt_image cheater_mm_20
                            "... and resumes touching herself."
                            lauren.c "oooooo"
                            wt_image cheater_mm_21
                            "She's exhausted her limited store of self-control, and comes quickly and noisily at the end of her own fingers while you watch."
                            lauren.c "oooooo ... AAAAHHH!!!"
                            $ lauren.orgasm_count += 1
                        "Stop, you've changed your mind":
                            player.c "Take your fingers away."
                            lauren.c "[lauren.your_respect_name]??  I haven't cum yet, [lauren.your_respect_name]."
                            player.c "I know, I changed my mind.  You don't get to cum today."
                            wt_image cheater_mm_29
                            lauren.c "[lauren.your_respect_name]!!!??????"
                            player.c "You heard me.  Thank me for letting you get sexually aroused and for letting you think you would get to cum."
                            wt_image cheater_mm_30
                            "That was excessively cruel. If her transformation hadn't so completely re-wired her brain to favor your orders over her own wants, she might storm out and you'd never see her again."
                            "Even with the re-wiring, enough of who she was remains for her to contemplate disobeying ..."
                            wt_image cheater_mm_31
                            "... but those rebellious parts of her brain aren't in control of her physical responses to your orders ... or her tongue."
                            wt_image cheater_mm_22
                            "With tears welling up in her eyes, she squeaks out her thank you."
                            lauren.c "{size=-5}Thank you, [lauren.your_respect_name], for allowing this worthless cunt to get wet and think that it would be allowed to cum.{/size}"
                            player.c "You're welcome."
                        "Let her continue":
                            wt_image cheater_mm_15
                            "You sit back to watch the show your slave is putting on, but it doesn't continue much longer. She lacks the self-control needed to delay her orgasm any further."
                            lauren.c "oooooo"
                            wt_image cheater_mm_18
                            "Using her finger and thumb she happily frigs herself to a noisy climax."
                            lauren.c "oooooo ... AAAAHHH!!!"
                            $ lauren.orgasm_count += 1
                "Fuck her":
                    player.c "Open yourself for my use."
                    wt_image cheater_mm_23
                    lauren.c "Yes, [lauren.your_respect_name]!!  Thank you, [lauren.your_respect_name]!!!"
                    wt_image cheater_office_2_41
                    "You were debating whether or not to deny her an orgasm and just having one yourself, but she's so worked up from her ordeal with Master M that she cums noisily as soon as you penetrate her."
                    wt_image cheater_office_2_15
                    lauren.c "AAAAHHH!!!  THANK YOU, [lauren.your_respect_name]!!"
                    wt_image cheater_office_2_14
                    "You don't last much longer."
                    player.c "[player.orgasm_text]"
                    $ lauren.sex_count += 1
                    $ lauren.orgasm_count += 1
                    orgasm notify
                "Make her blow you":
                    player.c "Pleasure my cock with your mouth while I think about it."
                    wt_image cheater_blow_job_5
                    "Her jaw has had some rest, but you know it must still be very sore. Despite that, she obediently takes you into her mouth."
                    wt_image cheater_blow_job_19
                    "She's in agony. The simple act of sucking you off after the ordeal Master M put her through may be the most intense torture you've inflicted on her. Before long, her whole body is trembling as her muscles rebel against overuse."
                    wt_image cheater_blow_job_6
                    "Despite that - or maybe because of it? - she looks up at you longingly and silently begs with her eyes for permission to touch herself."
                    $ title = "What do you do?"
                    menu:
                        "Let the tortured creature touch herself":
                            player.c "Play with yourself, but no cumming until I do."
                            wt_image cheater_blow_job_7
                            "She squeezes her tit and starts frigging herself as she sucks on you, distracting herself from the pain with the feeling of her own hands on her body."
                            wt_image cheater_blow_job_17
                            "If anything, she's even more motivated to pleasure you, desperately trying to bring you to orgasm so she can have one, too."
                            wt_image cheater_blow_job_15
                            "Before long, she succeeds."
                            player.c "[player.orgasm_text]"
                            wt_image cheater_blow_job_14
                            "Your cum has no sooner splattered on the back of her throat when her own orgasm rips through her."
                            lauren.c "NNNNNNN!!!"
                            $ lauren.orgasm_count += 1
                            $ lauren.swallow_count += 1
                        "Have her focus on your own pleasure":
                            wt_image cheater_blow_job_3
                            "It's always fun using her mouth, and it's even more fun when she's suffering while you do so."
                            wt_image cheater_blow_job_15
                            "The capper is knowing that despite the pain, she's turned on by the feeling of your cock between her lips, and will spend the rest of the day frustrated by an arousal she's not allowed to quench."
                            wt_image cheater_blow_job_12
                            "If you cum in her mouth, she might climax even without any other stimulation, so you pull her head off your cock as you unload."
                            wt_image cheater_blow_job_8
                            player.c "[player.orgasm_text]"
                            "Desperately she reaches for your sperm with her tongue, her eyes locked on yours, happy that you took the time to use her, no matter how painful and frustrating that use turned out to be."
                            $ lauren.facial_count += 1
                    $ lauren.blowjob_count += 1
                    orgasm notify
        "No, just go on with your day":
            wt_image cheater_kneel_8
            lauren.c "Should I be naked again, [lauren.your_respect_name]?"
            player.c "Keep the shoes and stockings on, [lauren.name], while you crawl back to my room. It amuses me to think you used to wear those daily once."
            wt_image cheater_kneel_9
            lauren.c "Yes, [lauren.your_respect_name]. Thank you for letting me amuse you, [lauren.your_respect_name]."
    $ master_m.experience_with_your_slave = "I enjoyed making use of her, although there was something a bit .. off with her. I couldn't quite put my finger on it. Anyway, I enjoyed myself."
    $ master_m.name_of_your_slave_loaned = lauren.name
    $ lauren.training_session()
    add tags 'master_m_visit' to lauren
    call master_m_lend from _call_master_m_lend
    return

## Items
## Lauren
# Give Butt Plug
label give_bp_lauren:
    if lauren.has_item(butt_plug):
        "You've already gifted Lauren a butt plug.  She only needs one."
    elif lauren.has_tag('accepts_anal'):
        "Lauren already accepts anal sex with you.  Giving her a butt plug won't have any effect.  Save it for someone else."
    elif lauren.status == "on_training":
        wt_image cheater_suspicious_1
        "Lauren looks at the butt plug with scepticism."
        wt_image cheater_surprised_1
        if lauren.anal_count == 0:
            lauren.c "This isn't going to lead to what you think it is."
        else:
            lauren.c "I'm not going to let you keep sticking your thing in my ass, just because you gave me this."
        wt_image cheater_unhappy_1
        player.c "We'll see Lauren.  For now, you'll wear this to each visit.  I'll inspect you on arrival and remove it - or not - at that time.  Is that understood?"
        "She nods."
        give 1 butt_plug from player to lauren notify
    else:
        "You should save the butt plug for someone else."
    return

# Give Chastity Belt
label give_cb_lauren:
  if lauren.has_item(chastity_belt):
    wt_image cheater_chastity_2
    "You've already fitted Lauren with a chastity belt.  A second one isn't going to help."
  else:
    if lauren.status == "on_training":
      player.c "Turn around, Lauren, and present your bare ass to me."
      wt_image cheater_posing_1_44
      "She looks at you suspiciously as you approach carrying a bag."
      lauren.c "What the hell is that thing!"
      wt_image cheater_chastity_2
      "She starts to stand up but you hold in her place as you buckle the chastity belt in place."
      player.c "The perfect device for a woman like you, Lauren."
      wt_image cheater_resisting_2
      lauren.c "You can't expect me to wear this?"
      player.c "Actually, you don't really have any choice. It's locked in place and the whole point of the chastity belt is that it can't be removed by the wearer."
      wt_image cheater_shock_1
      player.c "There are two keys. I couriered one to your husband. I kept the other one here, for me.  I'll take the belt off you when you visit me. I'll put it back on you before you leave.  Your husband can decide for himself whether or when to let you out of it when you're at home."
      wt_image cheater_resisting_1
      lauren.c "But if I need to go to the bathroom?"
      player.c "There are holes you can pee out of. You'll need to schedule your bowel movements with your husband. This is who you are now, Lauren. You'll need to accept that."
      change lauren submission by 5
      change lauren sos by 5
      give 1 chastity_belt from player to lauren notify
    else:
      "Save this for a current client."
  return

# Give Dildo
label give_di_lauren:
  if lauren.has_item(dildo):
    "You've already set aside a dildo for Lauren to use when visiting you.  One is enough."
  else:
    if lauren.status == "on_training":
      "Lauren's pussy is for her husband's pleasure now, not hers. Giving her a dildo of her own to play with would be sending the wrong message."
      "On the other hand, this might come in handy as part of her training. You set it aside for use with her when the opportunity arises."
      give 1 dildo from player to lauren notify
    else:
      "[lauren.full_name] doesn't need a sex toy from you now that her training has finished. Do you want to set one aside for her anyway?"
      $ title = "Set the dildo aside for her anyway?"
      menu:
        "Yes":
          give 1 dildo from player to lauren notify
        "No":
          pass
  return

# Use Fetch Toy
label use_ft_lauren:
  if lauren.has_tag('petgirl'):
    wt_image cheater_cage_4
    "The fetch toy is the first thing to catch [lauren.full_name]'s interest since she became a puppy girl. She wants to play, and she'll stop trying to bite you long enough for you to let her out of the cage to do so."
    "She hops up on the sofa and waits for you to throw the toy. You don't dare take her outside yet, for fear that she might take the toy and just keep running."
    wt_image cheater_cage_5
    "Inside the house, with no way to escape, she always grabs the toy and brings it back to you to throw again."
    "She loves the game so much, she'll even let you mount her, as long as you show her the toy while you do so."
    "She knows that once you've finished pushing your hard stick inside her, you'll throw the toy again, and she'll be able to fetch it once more."
    add tags 'fetch_toy_used' to lauren
  else:
    "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_lauren:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_lauren:
  if lauren.has_tag('petgirl'):
    wt_image cheater_cage_2
    "You manage to get the leash on [lauren.full_name], but she's too wild to take on a walk.  You leave the leash on her, in the hopes she'll get used to it, but she never does."
    add tags 'leash_used' to lauren
  else:
    "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_lauren:
  if lauren.has_item(lingerie):
    "You've already gifted lingerie to Lauren.  She has enough for now."
  else:
    if lauren.status == "on_training":
      $ title = "What type of lingerie do you want to gift to Lauren?"
      menu:
        "Something Classy":
          wt_image cheater_suspicious_1
          "Lauren looks at you suspiciously as you pass her the package, but she's somewhat pleased when she opens it up.  This is something she would look good in, and feel good in."
          wt_image cheater_pleased_1
          lauren.c "Thank you."
          add tags 'lingerie_classy' to lauren
        "Something Slutty":
          wt_image cheater_suspicious_1
          "Lauren looks at you suspiciously as you pass her the package.  Her jaw drops open when she sees what you've bought her."
          wt_image cheater_surprised_1
          lauren.c "You expect me to wear this?"
          player.c "Yes, I do.  This is what a slut wears to please a man."
          wt_image cheater_unhappy_1
          "Lauren has absolutely no interest in wearing this, but she knows you're going to tell her to do so, and she knows she won't say no when you do."
          add tags 'lingerie_slutty' to lauren
      give 1 lingerie from player to lauren notify
    else:
      "[lauren.full_name] doesn't need sexy underwear right now."
  return

# Give Love Potion
label give_lp_lauren:
  if lauren.has_tag('love_potion_used'):
    "You've already used a love potion on Lauren.  Additional ones won't do anything more."
  else:
    if lauren.status == "post_training":
      "You should save the love potion for current clients."
    elif lauren.status == "on_training":
      wt_image cheater_love_potion_1
      player.c "Here Lauren, I made you an herbal tea."
      "She looks at it and you in surprise.  She's a smart woman.  Something about this doesn't quite add up for her."
      "However, when she looks in the cup and smells it, it does indeed look and smell like an herbal tea."
      lauren.c "Thank you."
      wt_image cheater_love_potion_2
      "She keeps her eyes on you as she tentatively takes a sip.  It is an herbal tea - a very special blend - and it tastes good."
      "She takes a deeper drink."
      wt_image cheater_love_potion_3
      "As the potion takes effect, her eyes close and her head rolls back ..."
      wt_image cheater_love_potion_7
      "... as her brain struggles to adjust to the changes the potion is making to it."
      wt_image cheater_love_potion_5
      "When she opens her eyes again, she's all grin."
      lauren.c "Mmmm.  This is good.  Thank you!"
      wt_image cheater_love_potion_6
      lauren.c "Have I told you how lucky I am to be trained by you?  I'm so glad my husband sent me to you.  Getting to spend time with you is the best part of my week!"
      "With a little bit of positive reinforcement during your time together, and you might make a friend for life."
      change lauren desire by 20
      add tags 'love_potion_used' to lauren
      rem 1 love_potion from player notify
  return

# Give Transformation Potion
label give_tp_lauren:
  call lauren_transformation_potion_timer from _call_lauren_transformation_potion_timer
  return

# Use Water Bowl
label use_wb_lauren:
  if lauren.has_tag('petgirl'):
    wt_image cheater_cage_7
    "[lauren.full_name] watches warily as you set the bowl of water in front of her."
    wt_image cheater_cage_8
    "She sniffs it suspiciously, then she lowers her head ..."
    wt_image cheater_cage_3
    "... and drinks greedily."
    wt_image cheater_cage_9
    "She keeps a wary eye on you as she laps up the water.  An animal is vulnerable when it's drinking, and she doesn't trust you, even if you do bring her cold, delicious water."
  else:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_lauren:
  call lauren_will_tamer_timer from _call_lauren_will_tamer_timer
  return

## New Receptionist
# Give Butt Plug
label give_bp_new_receptionist_lauren:
  "Exactly what message are you trying to send?"
  return

# Chastity Belt
label give_cb_new_receptionist_lauren:
  "How is this conversation not going to get very awkward?"
  return

# Give Dildo
label give_di_new_receptionist_lauren:
  "I don't think that's going to work with him."
  return

# Use Fetch Toy
label use_ft_new_receptionist_lauren:
  "You'll look like an idiot."
  return

# Give Jewelry
label give_jwc_new_receptionist_lauren:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_new_receptionist_lauren:
  if new_receptionist_lauren.location == lauren_office:
    "At least wait until you have privacy to ask him."
  return

# Give Lingerie
label give_li_new_receptionist_lauren:
  "What if he accepts it?  What will you do then?"
  return

# Give Love Potion
label give_lp_new_receptionist_lauren:
  "What are you hoping to accomplish, exactly?"
  return

# Give Transformation Potion
label give_tp_new_receptionist_lauren:
  if new_receptionist_lauren.location == lauren_office:
    "Not with all the other people coming and going in this location."
  return

# Use Water Bowl
label use_wb_new_receptionist_lauren:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_new_receptionist_lauren:
  if new_receptionist_lauren.location == lauren_office:
    "Even ignoring for the moment all the other people coming and going in the busy office, how exactly do you intend to explain why you want him to wear your collar?"
  return

########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Character Engagement Ends
label lauren_end_training:
    if lauren.sos >= 60:
        wt_image lauren.image
        call convert(lauren,"satisfied", False, True) from _call_convert_82
        "Your engagement to train Lauren the Cheater has now ended. You receive an email from her husband."
        husband_lauren "{i}My compliments on your success with Lauren. I can't believe what a change you've made in her attitude.{/i}"
        husband_lauren "{i}It's too early to know whether she's put her cheating ways behind her, but her behavior with me is now exemplary. I need only say a word, and she caters to my every whim.{/i}"
        husband_lauren "{i}I had wondered whether I was doing the right thing in not divorcing her, but the work you've done with her has convinced me I made the right decision.{/i}"
        husband_lauren "{i}As long as I don't hear about her sleeping with other men without my permission, I'll keep her as my wife.{/i}"
        husband_lauren "{i}I'll be leaving positive feedback for you online.{/i}"
        if lauren.has_tag('love_potion_used') and lauren.desire > 30:
            "A little while later, you get an email from Lauren."
            lauren.c "{i}I have to see you. I know my training with you is finished, and I'm supposed to be an obedient slut to my husband.  But I can't bear the thought of not seeing you again.{/i}"
            lauren.c "{i}Please contact me as soon as possible.  Yours obediently, ~ Lauren{/i}"
    else:
        call convert(lauren,"unsatisfied", False, True) from _call_convert_83
        wt_image cheater_initial_4
        "Your engagement to train Lauren the Cheater has now ended.  Unfortunately, Lauren never became truly comfortable with being an obedient slut.  She and her husband will have to look for other solutions."
    return

# Start Day
label lauren_start_day:
    # if lauren.has_tag('showgirl'):
    #     summon lauren to stage no_follows
    #     # NEED: check to make sure this isn't done automatically at the stage itself? ## yes, it does
    pass
    return

label new_receptionist_lauren_start_day:
    pass
    return

# End Day
label lauren_end_day:
    rem tags 'leash_used' 'watched_today' 'on_stage_now' from lauren
    call character_location_return(lauren) from _call_character_location_return_481
    return

label new_receptionist_lauren_end_day:
    pass
    return

# End Week
label lauren_end_week:
  ## TIMER: Love Potion Weekly Actions
  if lauren.has_tag('love_potion_used') and lauren.visit_count == 0 and lauren.status == "on_training":
    wt_image phone_1
    "Your phone is ringing."
    wt_image cheater_office_phone_1
    lauren.c "Hi, it's me.  Lauren."
    wt_image cheater_office_phone_2
    lauren.c "You didn't train me this week.  I'm trying to be an obedient slut and not act needy, but I so look forward to getting to visit you."
    wt_image cheater_office_phone_3
    lauren.c "I hope I'm not doing anything wrong by asking for this, but please call me to your house again soon.  I'm okay with you training me if it means I get to spend time with you."
    wt_image room_living_room
  ## End Week: Whores Lost
  if lauren.has_tag('whore') and lauren.whore_count > 2:
    $ lauren.whore_lost_countdown -= 1
    if lauren.whore_lost_countdown <= 0:
      "You haven't checked on Lauren for quite a while.  She didn't send your cut this week and you can't find her.  Whether she skipped town or got into trouble, you never find out."
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      call convert(lauren, "unavailable") from _call_convert_84
  ## End Week: Whores Income
  if lauren.has_tag('whore') and lauren.whore_count > 2:
    $ player.whore_income += 25
  ## End Week: Cheater Receptionist Meeting Possible?
  if not lauren.has_tag('sophie_encounter_possible') and sophie.relationship_status > 6 and not lauren.has_tag('transformed') and not lauren.has_tag('receptionist_sex_complete') and lauren.status == "post_training" and lauren.has_tag('continuing_actions'):
    add tags 'sophie_encounter_possible' to lauren
    $ lauren.action_contact_arrange_meeting = living_room.add_action("Arrange Meeting Lauren and Sophie", label = lauren.short_name + '_contact_arrange_meeting', context = "_contact_other", condition = "lauren.can_be_interacted and lauren.status == 'post_training' and not lauren.has_any_tag('receptionist_sex_complete', 'shut_off_receptionist_sex')")
  if lauren.has_tag('revenge_discussion_this_week'):
    rem tags 'revenge_discussion_this_week' from lauren
  if lauren.has_tag('failed_regular_training_this_week'):
    rem tags 'failed_regular_training_this_week' from lauren
  $ lauren.visit_count_total += lauren.visit_count
  $ lauren.visit_count = 0
  return

label new_receptionist_lauren_end_week:
    pass
    return


## Club and Stage Labels

label lauren_stage_notice:
    # this runs when has tag 'waiting_for_club_access'
    if lauren.has_tag('waiting_for_club_access') and not lauren.has_tag('stage_message_given') and not lauren.has_tag('showgirl'):
        add tags 'stage_message_given' to lauren
        "This could be the right venue for Lauren to start showing off her attributes."
    return

label lauren_stage_call:
    # this runs when has tag 'showgirl' and you visit the Club
    if player.has_tag('stage_visited_today'):
        pass # as doesn't get dismissed from Club when you leave it, only at end of day
    else:
        $ lauren.location = stage
        add tags 'on_stage_now' to lauren
    return

label lauren_stage_send_home:
    call character_location_return(lauren) from _call_character_location_return_482
    return


label lauren_swingers_room_call:
    if lauren.can_be_interacted:
        add tags 'in_swingers_room_now' 'girlfriend' to lauren ## this is to allow the _watch label to activate
    else:
        "You can't find Lauren right now, or you'd make her join you."
    return

label lauren_swingers_room_send_home:
    call character_location_return(lauren) from _call_character_location_return_483
    rem tags 'in_swingers_room_now' 'girlfriend' from lauren
    return


## Loving Wife Content
label lauren_sarah_positive_role_talk_slavegirl:
    if current_target.has_tag('slavegirl') and not sarah.has_tag(tag_expression):
        wt_image cheater_lw_visit_1
        "You order [lauren.full_name] to join you."
        lauren.c "Yes, [lauren.your_respect_name]?"
        wt_image lw_visit_2_2
        player.c "[lauren.name], I'd like you to meet Sarah."
        sarah.c "Hi.  Shouldn't she, be dressed?"
        wt_image cheater_lw_visit_1
        player.c "She doesn't need clothes to talk.  [lauren.name], Sarah's husband wants her to have sex with his friends.  She has concerns.  I thought speaking to another woman could help her."
        lauren.c "I'll try, [lauren.your_respect_name]."
        add tags 'met_slavegirl_lauren' 'positive_transformed_slavegirl_resolution_today' to sarah
        ## remainder of transformed_slavegirl content is back in sarah's script
    else:
        $ current_target = None
    return

label lauren_sarah_positive_role_talk_bimbo:
    if current_target.has_tag('bimbo') and not sarah.has_tag(tag_expression):
        wt_image cheater_lw_visit_2
        "You ask Lauren to join you."
        lauren.c "Hi!  Are you here for sex?"
        wt_image lw_visit_2_2
        player.c "This is Sarah.  She's not here for sex, but her husband does wants her to have sex with his friends.  She has concerns about that.  I thought speaking to another woman could help her."
        sarah.c "Hi.  Nice to meet you."
        wt_image cheater_lw_visit_2
        lauren.c "Mmmmm ... nice to meet you, too!  I love sex!!  Sex is the best.  I hope you get to suck your husband's friends' cocks.  I love sucking cocks.  I love everything about cocks.  Do you think your husband's friends would let me suck their cocks?"
        add tags 'met_bimbo_lauren' 'transformed_bimbo_resolution_today' to sarah
        ## remainder of transformed_bimbo content is back in sarah's script
    else:
        $ current_target = None
    return

# NEED upgrade Rags photos to better quality for Lauren's LW content
label lauren_sarah_positive_role_sex_slavegirl:
    if current_target.has_tag('slavegirl'):
        player.c "[lauren.name], come here and join us."
        wt_image cheater_lw_visit_1
        lauren.c "Yes, [lauren.your_respect_name]."
        player.c "You remember Sarah?"
        lauren.c "Yes, [lauren.your_respect_name]."
        wt_image cheater_lw_visit_3
        player.c "You know Sarah's worried about having her husband watch her have sex.  It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together.  I'm going to fuck you, [lauren.name], while Sarah watches us."
        lauren.c "Yes, [lauren.your_respect_name]."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image cheater_lw_visit_4
        player.c "Let's get you prepared, [lauren.name]."
        lauren.c "Yes, [lauren.your_respect_name]."
        "You wrap her in a rope harness and bind her hands behind her back."
        wt_image cheater_lw_visit_5
        player.c "Now get me hard."
        wt_image lw_visit_4_4
        sarah.c "Maybe I should go?  I don't want to be intruding on your personal time together."
        player.c "Nonsense. [lauren.name] doesn't mind you being here.  She's happy to service me anytime, regardless of whether anyone's watching.  Aren't you?"
        wt_image cheater_lw_visit_5
        lauren.c "Of course, [lauren.your_respect_name]."
        wt_image cheater_lw_visit_6
        "She suckles your dick until you're fully erect, then you push her face down on the sofa and shove yourself into her roughly."
        lauren.c "ooohhhh"
        player.c "Excuse me for being so perfunctory, Sarah, but [lauren.name] responds best to hard use.  Don't you, girl?"
        lauren.c "Yes, [lauren.your_respect_name]."
        wt_image cheater_lw_visit_7
        lauren.c "Aaahhhh!!"
        player.c "[player.orgasm_text]"
        wt_image lw_visit_4_5
        sarah.c "You've made your point.  Men can enjoy sex even when it's not in private.  Some women, too, I guess."
        player.c "And did [lauren.full_name] look ridiculous while I was fucking her?"
        wt_image lw_visit_4_8
        sarah.c "No.  No, I guess not.  I mean, the whole bondage thing is kinda weird."
        player.c "You should try it sometime."
        wt_image lw_visit_4_7
        sarah.c "I think I'll just go home and maybe think about this some more, later."
        player.c "Sure.  And if your husband wants to borrow some of my equipment to use on you while you're thinking about it, just let me know."
        $ lauren.sex_count += 1
        $ lauren.orgasm_count += 1
        orgasm
        add tags 'watched_slavegirl_this_weekend' to sarah
    else:
        $ current_target = None
    return

label lauren_sarah_positive_role_sex_bimbo:
    if current_target.has_tag('bimbo'):
        player.c "Lauren, Sarah's here. Come join us."
        wt_image cheater_lw_visit_9
        lauren.c "Mmmmmm.  Is she here to have sex with us today?"
        player.c "Close.  You remember Sarah's worried about having her husband watch her have sex."
        wt_image cheater_lw_visit_8
        lauren.c "Is she? I don't remember many things, except for sex. I never forget sex."
        player.c "Well, it's hard for Sarah to imagine what it would be like to have someone watch her have sex, in part because she's never even seen two people have sex together.  So you and I are going to have sex, while Sarah watches us."
        wt_image cheater_lw_visit_9
        lauren.c "Fun!  I'll get my clothes off!"
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image cheater_lw_visit_10
        "Lauren wastes no time getting her dress off, your pants down, and your cock in her mouth. She looks over at Sarah."
        lauren.c "You can help me suck it, if you want?"
        wt_image lw_visit_4_4
        sarah.c "No, thank you!"
        wt_image cheater_lw_visit_11
        lauren.c "Okay.  I don't think you can help me fuck his cock.  At least, I haven't figured out a way for two girls to do that at the same time for one guy.  Do you know how to do that?"
        wt_image lw_visit_4_8
        sarah.c "No, and I'm leaving now.  I don't want to intrude on your personal time together."
        wt_image cheater_lw_visit_12
        lauren.c "Don't go!  If you don't want to just watch, I have a mouth and two hands you can use while he's fucking my kitty."
        $ lauren.sex_count += 1
        orgasm
        ## rest of content is back in sarah's script
        add tags 'watched_transformed_bimbo_this_weekend' to sarah
    else:
        $ current_target = None
    return

## Character Specific Timers
# Lauren In Office
label lauren_in_office:
    if sophie.location == lauren_office:
        $ sophie.dismiss(False)
    if new_receptionist_lauren.location == lauren_office:
        $ new_receptionist_lauren.dismiss(False)
    $ lauren.location = lauren_office
    if lauren.status == "on_training":
        $ lauren.office_visit_count += 1
        if lauren.office_visit_count == 1:
            wt_image cheater_office_1_1
            "Lauren seems none too pleased to see you.  When the receptionist leaves, she snaps at you."
            if lauren.has_tag('love_potion_used'):
                lauren.c "You know I love spending time with you, but not here.  You shouldn't be here."
            else:
                lauren.c "What are you doing here?"
            player.c "Is that how you greet your husband when he pays you a visit?"
            lauren.c "You're not my husband."
            player.c "No, I'm the man he's paying to train you to be a better wife for him.  You could start with a better attitude when you're visited at your office."
            lauren.c "I have work to do."
            player.c "Indeed you do.  Starting with making your man happy, so that you can then get back to your other, less important work."
            "She's fuming inside, but she can't easily get you out of here.  She decides the fastest way to have you leave is to play along."
            lauren.c "What do you want me to do?"
        $ title = "What do you want from Lauren today?"
        menu:
            "Hypnotize her" if player.can_hypno(lauren):
                $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                $ lauren.visit_count += 1
                if lauren.office_visit_count > 1:
                    wt_image cheater_office_1_1
                    lauren.c "What is it you want this time?"
                call lauren_office_hypno from _call_lauren_office_hypno
            "Have her display herself" if lauren.display_count_clothed > 0:
                $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                $ lauren.visit_count += 1
                $ lauren.display_count_office += 1
                if lauren.office_visit_count == 1:
                    player.c "You can start by coming around to this side of the desk so you're closer to me and taking off your jacket."
                    wt_image cheater_office_hypno_2
                    "Slowly, she gets up and does as you say."
                    wt_image cheater_office_1_2
                    player.c "Good.  Now, when your husband visits you at work he will expect to find you welcoming him.  Showing him your breasts would be a start."
                    lauren.c "You can't be serious.  We're at my work.  Someone could come in."
                    player.c "Your receptionist knows I'm in here with you.  She's not going to let someone barge in without letting you know."
                    wt_image cheater_office_hypno_4
                    lauren.c "Fine."
                    "She lowers her top, baring her breasts as she glares at you."
                    wt_image cheater_office_1_3
                    player.c "That's how you should greet him when he drops by your work to visit you, Lauren.  Minus the attitude.  Then you wait until he tells you what else he wants from you."
                    "Lauren's still fuming and you can tell she wants to make a smart remark. She holds her tongue, however, and waits."
                    player.c "It's possible he may just want to see his wife completely naked.  Let's practice that.  Take off your top, pull down your pants, and bend over your desk."
                    wt_image cheater_office_hypno_9
                    "Reluctantly, Lauren removes her top ..."
                    wt_image cheater_office_1_11
                    "... unbuttons her pants ..."
                    wt_image cheater_office_1_12
                    "... and slides them down."
                    wt_image cheater_office_1_4
                    player.c "Not like that, bend over to give me a good view of your ass."
                    "She looks back at you inn astonishment, wondering how far you're going to go with this."
                    wt_image cheater_office_1_5
                    "You can't go too far with Lauren's receptionist just outside her office. Next visit, you may have to tell Lauren to take you to a quieter office. But you can still have a little fun with her."
                else:
                    if lauren.test('submission', 20):
                        wt_image cheater_office_1_1
                        "Lauren is sitting behind her desk as the receptionist shows you in."
                        wt_image cheater_office_hypno_2
                        "After the receptionist leaves, she comes around to sit in front of you.  Without saying a word, she removes her jacket ..."
                        wt_image cheater_office_1_3
                        "... and lowers her top, baring her breasts."
                        player.c "I'm glad to see you're remembering and following your instructions."
                    else:
                        wt_image cheater_office_1_1
                        lauren.c "What is it you want this time?"
                        player.c "For you to remember your instructions would be a start."
                        "Lauren glares at you for a moment. She doesn't want to do this, especially not here, but she knows she's going to, and so do you."
                        wt_image cheater_office_hypno_2
                        "You wait, and eventually she moves from around the desk, removing her jacket ..."
                        wt_image cheater_office_1_3
                        "... and lowering her top, baring her breasts as she glares at you."
                    player.c "Let's see the rest of you now."
                    wt_image cheater_office_hypno_9
                    "Lauren removes her top ..."
                    wt_image cheater_office_1_11
                    "... unbuttons her pants ..."
                    wt_image cheater_office_1_12
                    if lauren.test('submission', 20):
                        "... and slides them down ..."
                        wt_image cheater_office_1_5
                        "... remembering to lean forward and push out her ass for your inspection."
                    else:
                        "... and slides them down."
                        wt_image cheater_office_1_4
                        player.c "You remember what to do next.  Get on with it."
                        wt_image cheater_office_1_5
                        "Reluctantly, she leans forward and pushes out her ass for your inspection."
                $ title = "What next?"
                menu:
                    "Spank her":
                        $ lauren.spank_count += 1
                        wt_image cheater_spank_1
                        "Without a word you lift up your hand and bring it down sharply on Lauren's bare bottom ... *smack*"
                        wt_image cheater_spank_2
                        lauren.c "Ow!"
                        if lauren.spank_count == 1:
                            wt_image cheater_office_1_13
                            "She knew her training was intended as a punishment, but she didn't know she would be literally punished."
                            wt_image cheater_office_1_5
                            player.c "Get back in position.  Yes, you're being spanked like a naughty girl.  That's what happens when you're not obedient to your husband."
                        else:
                            wt_image cheater_office_1_13
                            player.c "Yes, you're being spanked again.  Get back in position."
                            wt_image cheater_office_1_5
                        "With her receptionist on the other side of the door, you can't spank Lauren as hard as you'd like to ... *smack*  *smack*  *smack*"
                        wt_image cheater_office_1_6
                        "What the spanking lacks in force, however, it more than makes up for in humiliation, as Lauren submits to your punishment in her own office, desperately trying to suppress her cries so her receptionist can't hear her."
                        wt_image cheater_office_1_14
                        call lauren_spank_stat_changes from _call_lauren_spank_stat_changes_3
                    "Have her open herself up more":
                        $ lauren.open_her_count += 1
                        if lauren.open_her_count == 1:
                            player.c "You're awfully modest for a slut-in-training, Lauren.  When you lean over, I expect you to show off what you have to offer.  Turn around and show me everything you've got."
                            wt_image cheater_office_1_15
                            lauren.c "You can already see all of me."
                            player.c "Not what's between your legs.  Get up on your desk and show me."
                            wt_image cheater_office_1_9
                            "Lauren sits on the desk with her knees open, her pussy at eye level with you.  It's not much, but it's a start."
                        elif lauren.open_her_count == 2:
                            player.c "I can't see enough of you.  Get up on the desk and open yourself up more for me."
                            wt_image cheater_office_1_9
                            "Lauren sits on the desk with her knees open, her pussy at eye level with you."
                            player.c "More than that.  Show off your assets, slut."
                            wt_image cheater_office_1_16
                            "Tentatively, she reaches down with one hand and pulls her labia open."
                            if lauren.test('sos', 15):
                                player.c "Wider still."
                                wt_image cheater_office_1_8
                                player.c "That's how an obedient slut presents herself to her man."
                            else:
                                "That's as much as she's willing to do right now."
                        else:
                            player.c "Open yourself up to me, slut."
                            wt_image cheater_office_1_9
                            "She sits on the desk with her knees open, her pussy at eye level with you."
                            if lauren.test('sos',15):
                                wt_image cheater_office_1_8
                                "Then she demonstrates that she's starting to accept her new role as obedient slut."
                            else:
                                wt_image cheater_office_1_16
                                "With a bit of prompting, she improves the view a little."
                        call lauren_open_her_stat_changes from _call_lauren_open_her_stat_changes_3
                "Lauren has accepted your instructions well so far. As tempting as it is to push further, the current location limits your options."
                wt_image cheater_office_1_11
                "Besides, taking things slowly will give her time to get used to your control.  You let her dress and get back to her work."
                player.c "Next time I may expect more from you, slut.  I suggest you make arrangements to host me with greater privacy the next time I drop by to check in on you."
                add tags 'office_display_complete' to lauren
                change player energy by -energy_long notify
            "Blow job" if lauren.blowjob_count > 0 and lauren.has_tag('office_display_complete'):
                $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                $ lauren.visit_count += 1
                wt_image cheater_office_2_16
                if lauren.has_tag('love_potion_used'):
                    lauren.c "As much as I love seeing you, I wish you'd just called me to your house. I asked you not to visit me here."
                else:
                    lauren.c "I asked you not to bother me here."
                player.c "I came to check on whether you've been practicing?"
                if lauren.has_tag('office_blowjob'):
                    wt_image cheater_office_2_1
                    lauren.c "You want me to blow you again?"
                    player.c "Just like you would your husband, to thank him for visiting you at work."
                    wt_image cheater_office_2_19
                    lauren.c "Should I undress?"
                    $ title = "How do you want her to blow you?"
                    menu:
                        "Clothes on" if lauren.blowjob_count > 2:
                            wt_image cheater_office_2_16
                            player.c "You keep telling me what a successful businesswoman you are. You think you do such good work in your suit. Let's see if you're a good enough cocksucker to get me off in it."
                            $ lauren.blowjob_count += 1
                            if lauren.blowjob_count == 4:
                                wt_image cheater_ball_lick_1
                                "Lauren seems to have mastered her training.  She warms up your balls nicely ..."
                                wt_image cheater_office_2_2
                                "... then continues to play with them as she sucks your cock."
                                call lauren_fourth_blowjob from _call_lauren_fourth_blowjob_11
                            else:
                                wt_image cheater_ball_lick_1
                                "Lauren blows you exactly the way you trained her.  She licks and suckles your balls first ..."
                                wt_image cheater_office_2_2
                                "... then continues to play with them as she sucks your cock."
                            wt_image cheater_office_2_22
                            "You relax and enjoy the rest of the blowjob ..."
                            wt_image cheater_office_2_17
                            "... as she uses her hand, mouth, tongue and lips to get you ready."
                            wt_image cheater_office_2_2
                            "As tempting as it is to spray her with your seed while she's wearing her business suit, she's not ready to wear your cum around the office and has no easy way to get your sperm out of her clothes."
                            wt_image cheater_office_2_22
                            "So you empty your load down her throat."
                            player.c "[player.orgasm_text]"
                            if lauren.blowjob_count > 3:
                                call lauren_cum_arousal_stat_change from _call_lauren_cum_arousal_stat_change_12
                            wt_image cheater_office_2_17
                            player.c "That's a good slut.  Once you've finished swallowing and have licked my dick clean you can go back to doing all your important boss woman things."
                            call lauren_blowjob_stat_changes from _call_lauren_blowjob_stat_changes_14
                            if not lauren.has_tag('office_blowjob'):
                                add tags 'office_blowjob' to lauren
                                "Being required to give you head in her own office reinforces in Lauren her subservience to you."
                                change lauren submission by 5
                            if not lauren.has_tag('clothed_office_blowjob'):
                                add tags 'clothed_office_blowjob' to lauren
                                wt_image cheater_office_2_3
                                "Sucking you off in her work clothes has helped Lauren reconcile the idea of being both a businesswoman and an obedient slut."
                                change lauren sos by 5
                            orgasm notify
                        "Clothes off":
                            wt_image cheater_office_2_20
                            player.c "Yes, get your tits out, slut, so I can look at them while you suck me."
                            wt_image cheater_office_2_21
                            "The businesswoman removes her suit coat and top ..."
                            wt_image cheater_office_2_18
                            "... then kneels bare chested in front of you ..."
                            wt_image cheater_office_2_5
                            "... and takes your cock in her mouth"
                            call lauren_office_oral from _call_lauren_office_oral
                else:
                    wt_image cheater_office_2_1
                    "She looks at you uncertainly."
                    player.c "Your cock sucking skills, Lauren.  Have you been practicing?  Never mind answering, just get on your knees and show me."
                    lauren.c "You want me to blow you here?"
                    player.c "Assuming you can control your excitement and not to make so much noise that your receptionist comes to check on you.  Or maybe you'd like that?"
                    wt_image cheater_office_2_16
                    "You can see her debating whether to fight you on this."
                    wt_image cheater_office_2_2
                    "Eventually she decides it's easier just to get you off and get you out of here.  She drops to her knees and takes out your cock."
                    wt_image cheater_office_2_17
                    player.c "As much as I appreciate the enthusiasm, slut, you forgot the part where you take off your top to show off your tits."
                    wt_image cheater_office_2_18
                    "Lauren bares her breasts ..."
                    wt_image cheater_office_2_5
                    "... then goes back to your cock."
                    call lauren_office_oral from _call_lauren_office_oral_1
            "Sex" if lauren.sex_count > 0 and lauren.has_tag('office_display_complete'):
                $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                $ lauren.visit_count += 1
                wt_image cheater_office_2_1
                "As soon as Lauren's receptionist leaves, you address Lauren."
                player.c "Find us a quiet location, slut.  Somewhere we won't be disturbed."
                if lauren.has_tag('office_sex'):
                    wt_image cheater_office_2_27
                    "She leads you back to the isolated office ..."
                    wt_image cheater_office_2_29
                    "... and locks the door behind you."
                    lauren.c "Should I undress?"
                    $ title = "How do you want to fuck her?"
                    menu:
                        "Clothes on" if lauren.sex_count > 2:
                            wt_image cheater_office_2_7
                            player.c "You're a busy woman.  Just slip your skirt off."
                            wt_image cheater_office_2_8
                            player.c "I can access what I need like this."
                            wt_image cheater_office_2_32
                            "Lauren groans as you push yourself inside her."
                            lauren.c "Oh!"
                            player.c "Just because I'm behind you, slut, doesn't mean you don't have work to do.  Start moving those hips."
                            wt_image cheater_office_2_9
                            "She gets wet now when you enter her, and is soon wiggling and rocking her hips back against you."
                            if lauren.test('desire', 60) and not lauren.has_tag('clothed_office_sex'):
                                wt_image cheater_office_2_10
                                "There's not much stimulus on Lauren's clit, but the novelty of being fucked in her office partially clothed is turning her on and triggers a response."
                                lauren.c "ooooo"
                                wt_image cheater_office_2_11
                                "Quick and intense, the orgasm ripples through her.  She lets out a moan as her body shudders around your cock."
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_2_34
                                player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                                lauren.c "Y ... yes."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_44
                            wt_image cheater_office_2_10
                            "Lauren does her best to pleasure your cock as you alternate between thrusting into her and holding yourself still as she milks you."
                            wt_image cheater_office_2_33
                            "You make her work hard for your cum, and she starts to worry about if she can do enough in this position to get you off."
                            wt_image cheater_office_2_34
                            "Fortunately for her, watching her trying so hard to please you breaks down the last of your resolve."
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            add tags 'ride_fuck_today' to lauren
                            call lauren_sex_stat_changes from _call_lauren_sex_stat_changes_13
                            if not lauren.has_tag('office_sex'):
                                add tags 'office_sex' to lauren
                                wt_image cheater_office_2_31
                                "Being unable to refuse you sex, even at her place of work, reinforces in Lauren her inability to say 'no' to you."
                                change lauren resistance by -5
                            if not lauren.has_tag('clothed_office_sex'):
                                add tags 'clothed_office_sex' to lauren
                                wt_image cheater_office_2_7
                                "Satisfying you sexually in her work clothes has helped Lauren reconcile the idea of being both a businesswoman and an obedient slut."
                                change lauren sos by 5
                            $ lauren.remove_tags('pleasurable_fuck_today', 'rough_fuck_today', 'ride_fuck_today')
                            orgasm notify
                        "Clothes off":
                            wt_image cheater_office_2_30
                            player.c "Yes, slut, let's see everything you have to offer."
                            wt_image cheater_office_2_31
                            "The business woman removes her clothes ..."
                            wt_image cheater_office_2_4
                            "... and stands naked in front of you, waiting for further instructions."
                            call lauren_office_fuck from _call_lauren_office_fuck
                else:
                    wt_image cheater_office_2_27
                    "It's likely she's had this location scouted out since your first visit. She doesn't want you training her with her receptionist right outside her door. She leads you to an empty office at the end of a quiet hallway ..."
                    wt_image cheater_office_2_28
                    "... and locks the door behind you as you take a seat."
                    lauren.c "Make yourself at home."
                    player.c "Thank you.  I'll be more comfortable when I'm out of this tie and you're naked.  Or did you forget the part where you're to display your tits when your husband or I visit you?"
                    wt_image cheater_office_2_29
                    player.c "No need to stop with your tits, Lauren, assuming you ever get them out.  Are you wearing panties today?"
                    wt_image cheater_office_2_21
                    lauren.c "Yes"
                    wt_image cheater_office_2_30
                    player.c "Show me."
                    wt_image cheater_office_2_31
                    player.c "You can lose those, slut.  In fact, you can lose everything except the stockings and shoes."
                    wt_image cheater_office_2_4
                    player.c "Now I'm feeling more at home.  This is your workplace, though, so we should put you to work.  Let's work on your sex skills, slut."
                    call lauren_office_fuck from _call_lauren_office_fuck_1
            "Nothing today":
                player.c "I don't want anything from you today, Lauren.  I just dropped by to say hello."
                wt_image cheater_office_1_10
                lauren.c "Hello.  Good-bye.  I have work to do.  Please don't bother me here again."
    elif lauren.status == "post_training" and lauren.has_tag('continuing_actions'):
        $ lauren.office_outfit += 1
        if lauren.office_outfit > 2:
            $ lauren.office_outfit = 1
        if lauren.office_outfit == 1:
            if lauren.has_tag('blackmailed'):
                wt_image cheater_office_3_19
                lauren.c "Must you bother me at work?  What do you want now?"
            elif lauren.has_tag('love_potion_used'):
                wt_image cheater_office_3_114
                lauren.c "Hello! I'm glad you dropped by to visit."
                wt_image cheater_office_3_13
                if lauren.test('submission', 125):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out, Sir?"
                elif lauren.test('submission', 75):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out?"
            else:
                wt_image cheater_office_3_19
                player.c "Hello, slut."
                wt_image cheater_office_3_13
                if lauren.test('submission', 125):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Hello, Sir.  Should my tits be out?"
                elif lauren.test('submission', 75):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out?"
                else:
                    lauren.c "Hello.  What can I do for you?"
            wt_image cheater_office_3_12
            $ title = "What do you want?"
            menu menu_lauren_office_visit_1_menu_1:
                "Yes, tits out" if lauren.has_tag('offered_tits_today') and not lauren.has_tag('tits_out_today'):
                    add tags 'tits_out_today' to lauren
                    wt_image cheater_office_3_15
                    player.c "Yes, slut."
                    wt_image cheater_office_3_16
                    "She quickly disrobes."
                    wt_image cheater_office_3_14
                    if lauren.submission > 125:
                        lauren.c "Can I do anything else for you, Sir?"
                    jump menu_lauren_office_visit_1_menu_1
                "Get your tits out" if not lauren.has_any_tag('offered_tits_today','tits_out_today'):
                    add tags 'tits_out_today' to lauren
                    wt_image cheater_office_3_15
                    player.c "You can start by showing me your tits so I know you're grateful for my visit."
                    wt_image cheater_office_3_16
                    if lauren.has_tag('blackmailed'):
                        "She quickly disrobes, then addresses you sarcastically."
                        wt_image cheater_office_3_17
                        lauren.c "It's so great you visited.  Are you going now?"
                    else:
                        "She quickly disrobes."
                        wt_image cheater_office_3_14
                        lauren.c "Was there anything else?"
                    jump menu_lauren_office_visit_1_menu_1
                "No, just bend over the desk" if lauren.submission > 75 and not lauren.has_tag('tits_out_today'):
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "No need.  You can keep your top on.  Just bend over the desk."
                    wt_image cheater_office_3_18
                    $ title = "What now?"
                    menu:
                        "Spanking ordeal":
                            wt_image cheater_office_3_25
                            player.c "Remove your skirt."
                            wt_image cheater_office_3_26
                            "As she does, you tie her hands behind her back and give her ass a slap ... *smack*"
                            lauren.c "Oh!"
                            player.c "Now, now, slut. I'm sure you're getting wet at the thought of a spanking, but I bet you don't want your staff knowing you're being disciplined, so you'll need to be quiet."
                            wt_image cheater_office_3_3
                            "Spotting an old metal cup on the desk, you fill it with left over coffee and place it on her bare ass."
                            player.c "This should help you concentrate."
                            "*smack*"
                            lauren.c "Oh"
                            player.c "I suggest you focus on keeping your hips still. If you let this cup spill, you'll have coffee all over yourself and the carpet."
                            player.c "Worry about that and maybe you won't enjoy this so much you can't stay quiet."
                            wt_image cheater_office_3_2
                            "It's an effort, but Lauren manages to take the spanking without crying out or spilling the coffee."
                            "*smack*  ...  *smack*   ... *smack*"
                            lauren.c "nnnnnnnn"
                            wt_image cheater_office_3_27
                            player.c "You're not going to spill that coffee, are you, slut?"
                            lauren.c "No!"
                            player.c "I hope not, because your hips are starting to twitch.  I told you to keep your hips still."
                            if lauren.submission > 125:
                                lauren.c "I'm sorry, Sir!"
                            $ title = "Keep spanking her?"
                            menu menu_lauren_office_spanking_ordeal_1:
                                "That's enough":
                                    wt_image cheater_office_3_26
                                    player.c "That's enough for today, slut.  I know you're sopping wet, but you don't need to cum today, do you?"
                                    if lauren.submission > 125:
                                        lauren.c "Ohhhh  ... I'd like to, Sir!"
                                        player.c "Don't be silly.  If you didn't have that itching between your legs, you'd have nothing to distract you from the soreness of your ass."
                                    else:
                                        "She bites her lip.  You get the sense she wants to say something, but can't bring herself to do so."
                                        change lauren submission by 5
                                "Keep spanking her" if not lauren.has_tag('kept_spanking_her'):
                                    add tags 'kept_spanking_her' to lauren
                                    wt_image cheater_office_3_2
                                    "With every slap you land on her ass, it gets harder and harder for Lauren to keep from moving her hips."
                                    "*smack*  ...  *smack*   ... *smack*"
                                    lauren.c "nnnnnnnn"
                                    jump menu_lauren_office_spanking_ordeal_1
                                "Spank her some more" if lauren.has_tag('kept_spanking_her'):
                                    "*smack*  ...  *smack*   ... *smack*"
                                    wt_image cheater_office_3_27
                                    "Eventually it's too much, and she cries out as she feels the liquid on her ass."
                                    lauren.c "No!"
                                    wt_image cheater_office_3_28
                                    player.c "You're in luck, slut.  It's water today, not coffee.  No stains on your clothes.  No stains on the carpet."
                                    wt_image cheater_office_3_27
                                    player.c "Next time it'll be coffee, though.  Are you going to be more obedient next time?"
                                    if lauren.test('submission', 125):
                                        lauren.c "Yes, Sir!  Thank you, Sir."
                                        player.c "Why are you thanking me, slut?"
                                        lauren.c "I'm not sure, Sir.  I'm sorry, Sir."
                                    else:
                                        lauren.c "Yes!  I'll try to."
                                        player.c "Don't try.  Do."
                                        change lauren submission by 5
                            wt_image cheater_office_3_25
                            player.c "You can get back to your very important job now, slut."
                            lauren.c "Thank you, Sir.  I have a meeting with the CEO of one of our biggest suppliers.  I need to get our costs down and it may be a tough negotiation."
                            wt_image cheater_office_3_29
                            lauren.c "It's a good thing the conference room has soft chairs."
                            rem tags 'kept_spanking_her' from lauren
                            change player energy by -energy_short notify
                        "Spanking blowjob" if lauren.blowjob_count > 2:
                            wt_image cheater_office_3_20
                            "Lauren accepts your cock as it's offered to her ..."
                            wt_image cheater_office_3_54
                            "... and blows you as you provide remedial lessons on giving head."
                            wt_image cheater_office_3_21
                            "She makes no objection as you lift up her skirt ..."
                            wt_image cheater_office_3_22
                            "... and knows better than to stop pleasuring your cock as you start to rain spanks down on her upturned ass ... *smack*  *smack*  *smack*"
                            wt_image cheater_office_3_23
                            "Even when the blows sting enough for her to cry out, she keeps at least her tongue in contact with your cock at all times ... *smack*  *smack*  *smack*"
                            lauren.c "Ow!"
                            player.c "Keeps sucking me, slut."
                            if lauren.submission > 125:
                                lauren.c "Yes, Sir."
                            wt_image cheater_office_3_22
                            "*smack*  *smack*  *smack*"
                            wt_image cheater_office_3_63
                            "Eventually she earns your cum."
                            player.c "[player.orgasm_text]"
                            wt_image cheater_office_3_25
                            player.c "You can get back to your very important job now, slut."
                            if lauren.submission > 125:
                                lauren.c "Thank you, Sir.  I have a meeting with the CEO of one of our biggest suppliers.  I need to get our costs down and it may be a tough negotiation."
                            else:
                                lauren.c "Just in time.  I have a meeting with the CEO of one of our biggest suppliers.  I need to get our costs down and it may be a tough negotiation."
                            player.c "Maybe you could offer him a blowjob for a discount?"
                            "She looks at you incredulously as you leave, chuckling to yourself."
                            if lauren.cheated == 0:
                                $ lauren.cheated = 1
                            $ lauren.blowjob_count += 1
                            $ lauren.swallow_count += 1
                            orgasm notify
                "Hypnotize her" if player.can_hypno(lauren):
                    if lauren.has_tag('blackmailed'):
                        add tags 'no_hypnosis' to lauren
                        "With you blackmailing her, Lauren is too wary around you to lower her guard enough for you to hypnotize her."
                        jump menu_lauren_office_visit_1_menu_1
                    else:
                        add tags 'continuing_office_hypnosis_outfit_1' to lauren
                        # note: this causes the normal weekday Hypnotize Her action to now run; artwork is handled in _hypnosis_start, etc.
                        $ queue_action(lauren.hypno_action)
                        if lauren.has_tag('tits_out_today'):
                            if lauren.has_tag('blackmailed'):
                                wt_image cheater_office_3_17
                            else:
                                wt_image cheater_office_3_39
                        else:
                            wt_image cheater_office_3_33
                        "You bring her out of her trance."
                        lauren.c "Are we finished talking?  I have work I need to look after."
                        player.c "That's all for today, yes."
                        rem tags 'continuing_office_hypnosis_outfit_1' from lauren
                        notify
                "Spank her" if lauren.submission <= 75:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('blackmailed'):
                        player.c "You need an attitude adjustment.  Turn around and bend over the desk."
                    else:
                        player.c "I shouldn't have to remind you to bare your breasts to thank me for visiting you at work.  Turn around and bend over the desk."
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            wt_image cheater_office_3_34
                            player.c "Lose the skirt, first."
                        wt_image cheater_office_3_36
                        "You land the first few spanks on her as she's bent over the desk ... *smack*  *smack*  *smack*"
                        wt_image cheater_office_3_37
                        "... then you tie her hands together and finish the spanking with harder blows as she tries, not entirely successfully, to keep from crying out."
                        lauren.c "nnnnnn  ...  ow!  ...  nnnnnnn  ...   ow!"
                    else:
                        wt_image cheater_office_3_18
                        player.c "Not like that.  Take your top off."
                        wt_image cheater_office_3_15
                        "She pulls off her blouse ..."
                        wt_image cheater_office_3_30
                        "... and gets back in position."
                        wt_image cheater_office_3_31
                        "You tie her hands together, pull down her skirt, and start spanking her as she tries, not entirely successfully, to keep from crying out ... *smack*  *smack*  *smack*"
                        lauren.c "nnnnnn  ...  ow!  ...  nnnnnnn  ...   ow!"
                    change lauren submission by 5
                    if lauren.has_tag('blackmailed'):
                        wt_image cheater_office_3_33
                        player.c "I hope these remedial lessons in obedience aren't going to be needed in the future, slut."
                        lauren.c "You're blackmailing me. I'm not about to forget that."
                    else:
                        wt_image cheater_office_3_32
                        player.c "I hope these remedial lessons in obedience aren't going to be needed in the future, slut."
                        # these next tests use 'test' instead of base stat
                        if lauren.test('submission', 125):
                            lauren.c "I hope not, too, Sir.  I'll try to remember to greet you properly next time."
                        elif lauren.test('submission', 75):
                            lauren.c "I'll try to remember to greet you properly next time."
                    change player energy by -energy_short notify
                "Tie her up" if lauren.punishment_count > 1 or lauren.submission > 100:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            wt_image cheater_office_3_34
                            player.c "Lose the skirt."
                        else:
                            player.c "Stand up."
                    else:
                        wt_image cheater_office_3_15
                        player.c "Strip"
                    wt_image cheater_office_3_39
                    player.c "Squat down in front of your desk."
                    wt_image cheater_office_3_38
                    "You take some rope out of your pocket ..."
                    wt_image cheater_office_3_4
                    "... and tie her to her desk."
                    wt_image cheater_office_3_5
                    player.c "You don't have anything important you need to be doing, do you, slut?"
                    lauren.c "I have a meeting with the CEO of a supplier shortly.  I need to get our costs down and it may be a tough negotiation."
                    wt_image cheater_office_3_4
                    player.c "If you like, I could get your receptionist to bring him in here when he arrives. Though I suppose it might be tough to negotiate if he knew your hands were tied, so to speak."
                    if lauren.submission <= 125:
                        wt_image cheater_office_3_5
                        lauren.c "I'd like time to prepare for the meeting.  It's important to me."
                        player.c "You're already prepared.  You're not the type to leave something like that to the last minute.  You just don't like being tied up."
                        wt_image cheater_office_3_4
                        change lauren submission by 5
                    "She turns her head away and stays silent."
                    $ title = "What now?"
                    menu:
                        "Let her earn her release with a blow job":
                            wt_image cheater_office_3_6
                            player.c "Open your mouth, slut.  Put your mouth to good use, and I'll let you get ready for your meeting.  Will you do a good job sucking my cock?"
                            "She nods."
                            call lauren_continuing_office_1_tied_up_oral from _call_lauren_continuing_office_1_tied_up_oral
                            wt_image cheater_office_3_16
                            player.c "Hopefully you'll do as good a job satisfying your supplier, and maybe he'll let you have your price reduction. Do you think you'll finish that negotiation on your knees, too?"
                            if lauren.cheated == 0:
                                $ lauren.cheated = 1
                            orgasm notify
                        "Keep her tied up":
                            "You can't keep her tied up here too long.  You know how important her work is to her, and if you screw it up on her, she'll call the whole arrangement off."
                            wt_image cheater_office_3_5
                            "You push it, though, to the point where she's worried that you are going to make her miss her meeting."
                            wt_image cheater_office_3_6
                            player.c "I guess I should let you go to your very important meeting, slut."
                            wt_image cheater_office_3_44
                            lauren.c "It's about time!  If you messed up this negotiation ..."
                            wt_image cheater_office_3_6
                            player.c "Don't try to blame me for you issues, slut. I just gave you lots of quiet time to reflect on how to handle your discussion. If you mess up, that's your fault."
                            wt_image cheater_office_3_5
                            player.c "Or maybe you need some more time down on your knees to think through your negotiating strategy?"
                            lauren.c "No, please!  Please, I really need to go!!"
                            wt_image cheater_office_3_16
                            player.c "You're cute when you beg, slut.  Maybe you should try getting on your knees and begging your supplier for that price reduction you want, too?"
                            change player energy by -energy_short notify
                "Tie her up for sex" if lauren.sex_count > 0 and (lauren.punishment_count > 1 or lauren.submission > 100):
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            player.c "Lose the skirt."
                            wt_image cheater_office_3_34
                        else:
                            pass
                    else:
                        player.c "Strip"
                        wt_image cheater_office_3_15
                    player.c "Lie down on your desk."
                    wt_image cheater_office_3_45
                    "You take some rope out of your pocket ..."
                    wt_image cheater_office_3_8
                    "... and tie her to her desk."
                    wt_image cheater_office_3_9
                    player.c "Is this turning you on, slut?"
                    # note: test is purposefully against unmodified stat
                    if lauren.submission > 125:
                        lauren.c "Yes, Sir."
                        wt_image cheater_office_3_46
                        player.c "That's good.  So I don't need to be gentle, do I, slut?"
                        lauren.c "No, Sir."
                    elif lauren.desire > 60:
                        player.c "Never mind answering, I can see it is.  You're already wet for me."
                        wt_image cheater_office_3_46
                        "You slide into her easily as she groans."
                        lauren.c "oooo"
                    else:
                        "She holds her tongue.  She's not exactly wet, but after a few strokes of your fingers along her sex, she's not exactly dry, either."
                        wt_image cheater_office_3_46
                        "You press the head of your cock against her opening. She's a woman who loves sex, and despite the circumstances, her body yields to your slow approach and accepts you inside."
                    wt_image cheater_office_3_10
                    "The location limits how fast and hard you can fuck her, but you pound into her as aggressively as you can without creating so much noise as to alert the rest of the office."
                    if lauren.desire > 60:
                        wt_image cheater_office_3_11
                        "Lauren's also struggling to stay quiet, and not always succeeding."
                        lauren.c "oooooo  ...  oooooooo"
                        wt_image cheater_office_3_47
                        lauren.c "Aaahhhh!!!!"
                        wt_image cheater_office_3_10
                        player.c "If you can't control yourself, slut, I may have to gag you next time I tie you up and fuck you. Or are you trying to get your staff to come see what you're up to?"
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_45
                        add tags 'office_tied_orgasm' to lauren
                    wt_image cheater_office_3_11
                    "You prolong the fuck as long as you can, enjoying the sight and feel of the helpless businesswoman surrendering herself to you in her own office."
                    wt_image cheater_office_3_10
                    "Eventually, the pressure in your balls can be denied no longer."
                    wt_image cheater_office_3_11
                    player.c "[player.orgasm_text]"
                    wt_image cheater_office_3_16
                    "She dresses and gets back to work, carrying your load inside her."
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    $ lauren.sex_count += 1
                    orgasm notify
                "Gag her and tie her up for sex" if lauren.has_tag('office_tied_orgasm') and dungeon.has_item(gags):
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            wt_image cheater_office_3_34
                            player.c "Lose the skirt."
                        else:
                            player.c "Stand up."
                            pass
                    else:
                        wt_image cheater_office_3_15
                        player.c "Strip"
                    wt_image cheater_office_3_39
                    player.c "You couldn't seem to control yourself before, so I'm going to make today easier for you, slut."
                    wt_image cheater_office_3_48
                    "You tie her hands behind her back and strap a ballgag into place."
                    lauren.c "nnnnn"
                    wt_image cheater_office_3_49
                    player.c "Feel how excited you are, slut.  Helpless and about to be fucked.  You're so turned on you're dripping."
                    wt_image cheater_office_3_50
                    player.c "Let's get you into position.  Flat on the desk with you."
                    wt_image cheater_office_3_51
                    player.c "Time for honesty, slut.  What do you want right now?"
                    if lauren.test('submission', 75):
                        lauren.c "nn nnnn nnn nnn nnnnnnn nnnn"
                    else:
                        "She just looks at you."
                        player.c "Go on.  Tell me."
                        lauren.c "nn nnnn nnn nnn nnnnnnn"
                        if lauren.has_tag('office_tied_asked_for_fuck'):
                            change lauren submission by 5
                        else:
                            add tags 'office_tied_asked_for_fuck' to lauren
                            change lauren submission by 10
                    player.c "You want to be fucked?"
                    "She nods."
                    player.c "And I don't have to be gentle, do I?"
                    "She shakes her head, no."
                    wt_image cheater_office_3_52
                    "You thrust into her hard, ramming her against her desk as she screams into her gag."
                    lauren.c "NNNNNN"
                    wt_image cheater_office_3_53
                    "It doesn't take her long to cum.  It doesn't take you much longer."
                    lauren.c "NNNNNN!!!!"
                    player.c "[player.orgasm_text]"
                    wt_image cheater_office_3_32
                    "She goes back to work, a little shaken, but not unhappy."
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    $ lauren.sex_count += 1
                    call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_46
                    orgasm notify
                "Eat her out":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            player.c "Lose the skirt."
                            wt_image cheater_office_3_34
                        else:
                            pass
                    else:
                        player.c "Strip"
                        wt_image cheater_office_3_15
                    player.c "Lie down on your desk."
                    wt_image cheater_office_3_45
                    "She's not quite sure what you're up to ..."
                    wt_image cheater_office_3_55
                    "... but she's pleasantly surprised when she finds out."
                    lauren.c "Oh!"
                    wt_image cheater_office_3_57
                    "You can smell Lauren's arousal after only a few licks ..."
                    wt_image cheater_office_3_58
                    "... and taste it after a few licks more."
                    lauren.c "oooo"
                    $ lauren.pleasure_her_count += 1
                    if lauren.test('desire', 30):
                        wt_image cheater_office_3_56
                        "The feel of your lips and tongue on her sex soon overwhelms Lauren.  She groans as she climaxes and fills your mouth with her sticky juices."
                        lauren.c "oooooo ... y ... yes ... aaahhhh!"
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_47
                    else:
                        wt_image cheater_office_3_55
                        "Her mind and body never fully relax enough for her to cum, but her sex becomes sopping wet from your ministrations."
                    call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_5
                    wt_image cheater_office_3_59
                    "Lauren goes back to work feeling good about your visit."
                    change player energy by -energy_short notify
                "Blow job":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    call lauren_continuing_office_1_oral from _call_lauren_continuing_office_1_oral
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Fuck her on her desk" if lauren.sex_count != 1 and lauren.sex_count != 2:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            player.c "Lose the skirt."
                            wt_image cheater_office_3_34
                        else:
                            pass
                    else:
                        player.c "Strip"
                        wt_image cheater_office_3_15
                    player.c "Lie down on your desk."
                    wt_image cheater_office_3_45
                    player.c "Don't be shy, slut.  Spread your legs wide."
                    wt_image cheater_office_3_72
                    "As she does, you slip the head of your cock into her."
                    lauren.c "Oh!"
                    if lauren.sex_count == 0:
                        wt_image cheater_office_3_73
                        "She knew this day was coming, when you'd use her for sex.  She'd been dreading it, but she knew she wouldn't be able to tell you 'no' when the time came."
                        player.c "Don't look so sad, slut.  You may even enjoy being my personal fuck toy."
                        wt_image cheater_office_3_74
                        lauren.c "I don't want to enjoy it."
                        player.c "You might enjoy it anyway."
                        wt_image cheater_office_3_75
                        "She doesn't really enjoy herself. Not today, anyway. But despite her reservations, her body does get wet as you fuck her. She knows it, and she knows you know it."
                        wt_image cheater_office_3_74
                        player.c "It's okay if you cum, as long as it doesn't interfere with my pleasure."
                        lauren.c "I'm not going to cum.  I don't even want to cum."
                        wt_image cheater_office_3_76
                        "The same cannot be said of you."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_office_3_32
                        "She dresses quietly, avoiding eye contact with you"
                        wt_image cheater_office_3_33
                        player.c "Don't you want to say something to me?"
                        lauren.c "What?"
                        player.c "Shouldn't you be thanking me for letting you have sex with me?"
                        lauren.c "Are you kidding me?"
                        if lauren.has_tag('whore'):
                            player.c "No. Your husband and I are your only sources of sex from here out, other than your johns. And I can cut you off from whoring anytime I want. You should be grateful for access to my cock."
                        else:
                            player.c "No.  Your husband and I are your only sources of sex from here out.  You should be grateful for access to my cock."
                        "She can't bring herself to thank you and you don't push it, as that may be a step too far for her right now.  But you've made your point."
                        change lauren submission by 10
                    else:
                        if lauren.test('submission', 125):
                            wt_image cheater_office_3_77
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes, Sir."
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me, Sir.  Please fuck me?"
                            "You're almost tempted to say 'no' just to enforce her submission, but you want to fuck her, too, and she's already obedient enough you don't need to deny yourself in order to train her."
                            wt_image cheater_office_3_78
                            "So you start to fuck her, slowly at first, then faster and faster, as her moans increase."
                            lauren.c "oooo ... oooooo"
                            if lauren.test('desire', 60):
                                wt_image cheater_office_3_75
                                "Her excitement ramps up quickly ..."
                                wt_image cheater_office_3_83
                                "... and she soon shudders to orgasm around your cock."
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_3_80
                                "It doesn't take you much longer."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_48
                            else:
                                wt_image cheater_office_3_75
                                "She doesn't get aroused enough to cum, but she gets close."
                                wt_image cheater_office_3_80
                                "You, on the other hand, have no trouble getting aroused enough to cum.  The only question is where?"
                                change lauren desire by 10
                            wt_image cheater_office_3_78
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image cheater_office_3_79
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_3_59
                                    "She seems comfortable going back to work with our load inside her."
                                "On her":
                                    wt_image cheater_office_3_81
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_82
                                    player.c "No cleaning yourself up, slut.  You can wear my cum for the remainder of the work day."
                        elif lauren.test('desire', 60):
                            wt_image cheater_office_3_77
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes"
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me until I cum."
                            wt_image cheater_office_3_78
                            "You start to fuck her, slowly at first, then faster and faster, as her moans increase."
                            lauren.c "oooo ... oooooo"
                            wt_image cheater_office_3_75
                            "Her excitement ramps up quickly ..."
                            wt_image cheater_office_3_83
                            "... and she soon shudders to orgasm around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_3_80
                            "It doesn't take you much longer."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image cheater_office_3_79
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_3_59
                                    "She seems comfortable going back to work with our load inside her."
                                "On her":
                                    wt_image cheater_office_3_81
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_3_82
                                    player.c "No cleaning yourself up, slut.  You can wear my cum for the remainder of the work day."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_49
                        else:
                            wt_image cheater_office_3_74
                            player.c "Does that feel good, slut?"
                            "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                            wt_image cheater_office_3_75
                            "She may not want to let herself enjoy this, but you certainly enjoy it."
                            wt_image cheater_office_3_77
                            "It's not long before you're ready to empty your load.  The only question is where?"
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image cheater_office_3_76
                                    player.c "[player.orgasm_text]"
                                "On her":
                                    wt_image cheater_office_3_81
                                    player.c "[player.orgasm_text]"
                                    wt_image cheater_office_3_82
                                    player.c "No cleaning yourself up, slut.  You can wear my cum for the remainder of the work day."
                            wt_image cheater_office_3_32
                            "She dresses quietly, avoiding eye contact with you again."
                            wt_image cheater_office_3_33
                            player.c "You enjoyed that, slut.  Why not admit it?"
                            if lauren.has_tag('blackmailed'):
                                lauren.c "If you can't figure that out, then I really am being blackmailed by the biggest idiot in the city."
                            else:
                                "She did, but she won't.  Not yet, anyway."
                            change lauren desire by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Fuck her from behind" if lauren.sex_count > 1:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            player.c "Lose the skirt."
                            wt_image cheater_office_3_34
                        else:
                            pass
                    else:
                        player.c "Strip"
                        wt_image cheater_office_3_15
                    player.c "Turn around and bend over."
                    wt_image cheater_office_3_35
                    player.c "Don't be shy, slut.  Spread your legs wide."
                    wt_image cheater_office_3_84
                    "As she does, you slip the head of your cock into her."
                    lauren.c "Oh!"
                    if lauren.sex_count == 2:
                        wt_image cheater_office_3_85
                        player.c "Let's see if you're getting any better at fucking, Lauren. I'm going to hold myself here you're going to do the work."
                        player.c  "You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
                        "Lauren nods."
                        player.c "Good.  Then get at it."
                        wt_image cheater_office_3_86
                        "You don't say anything more.  You just hold yourself and her in place and watch as she struggles to pleasure your cock within the limited range of movement you give her."
                        if lauren.test('desire', 60):
                            wt_image cheater_office_3_91
                            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your hands on her hips her triggers a response."
                            lauren.c "oooooo"
                            wt_image cheater_office_3_89
                            "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_3_91
                            player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_50
                        wt_image cheater_office_3_87
                        "Lauren tries very hard to pleasure your cock, but it's not easy within the limited range of motion you allow her."
                        wt_image cheater_office_3_86
                        "She start to worry that the squeezing and hip rolls won't be enough to get you off."
                        wt_image cheater_office_3_85
                        "Fortunately for her, the sight of her working so hard to extract your cum is itself a big turn on, and you feel your orgasm building."
                        wt_image cheater_office_3_92
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_office_3_84
                        player.c "That felt good, didn't it?  Working to earn my cum."
                        if lauren.submission > 125:
                            lauren.c "Yes, Sir"
                            if lauren.desire <= 60:
                                change lauren desire by 10
                        elif lauren.desire > 60:
                            lauren.c "Yes"
                            change lauren submission by 5
                        else:
                            "She says nothing, but the pace of her breathing tells you she's turned on."
                            change lauren submission by 5
                            change lauren desire by 5
                    else:
                        if lauren.test('submission', 125):
                            wt_image cheater_office_3_85
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes, Sir."
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me, Sir.  Please fuck me?"
                            "You're almost tempted to say 'no' just to enforce her submission, but you want to fuck her, too, and she's already obedient enough you don't need to deny yourself in order to train her."
                            wt_image cheater_office_3_86
                            "So you start to fuck her, slowly at first ..."
                            wt_image cheater_office_3_87
                            "... then faster and faster, as her moans increase."
                            lauren.c "oooo ... oooooo"
                            if lauren.test('desire', 60):
                                wt_image cheater_office_3_88
                                "Her excitement ramps up quickly ..."
                                wt_image cheater_office_3_89
                                "... and she soon shudders to orgasm around your cock."
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_3_90
                                player.c "Keep moving your hips, slut.  The goal is my pleasure, not yours."
                                lauren.c "Y ...  yes, Sir."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_51
                            else:
                                wt_image cheater_office_3_90
                                "She's not stimulated enough to be able to cum in this position, but she does her best to make it pleasurable for you."
                                change lauren desire by 10
                            wt_image cheater_office_3_91
                            "With Lauren milking your cock and bucking her hips back against you, it's not long before your balls need relief."
                            wt_image cheater_office_3_88
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_3_59
                            "She seems comfortable going back to work with your load inside her."
                        elif lauren.test('desire', 60):
                            wt_image cheater_office_3_92
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes"
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me until I cum."
                            wt_image cheater_office_3_86
                            "You start to fuck her, slowly at first ..."
                            wt_image cheater_office_3_87
                            "... then faster and faster, as her moans increase."
                            lauren.c "oooo ... oooooo"
                            wt_image cheater_office_3_88
                            "Her excitement ramps up quickly ..."
                            wt_image cheater_office_3_89
                            "... and she soon shudders to orgasm around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_3_90
                            player.c "Keep moving your hips, slut.  The goal is my pleasure, not yours."
                            wt_image cheater_office_3_91
                            "With Lauren milking your cock and bucking her hips back against you, it's not long before your balls need relief."
                            wt_image cheater_office_3_88
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_3_59
                            "She seems comfortable going back to work with your load inside her."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_52
                        else:
                            wt_image cheater_office_3_85
                            player.c "Does that feel good, slut?"
                            "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                            wt_image cheater_office_3_86
                            "She may not want to let herself enjoy this, but you certainly enjoy it as you fuck her ..."
                            wt_image cheater_office_3_91
                            "... faster and faster ..."
                            wt_image cheater_office_3_90
                            "... before emptying your load inside her."
                            player.c "[player.orgasm_text]"
                            wt_image cheater_office_3_32
                            "She dresses quietly, avoiding eye contact with you again."
                            wt_image cheater_office_3_33
                            player.c "You enjoyed that, slut.  Why not admit it?"
                            "She did, but she won't.  Not yet, anyway."
                            change lauren desire by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Have her ride you" if lauren.sex_count > 0 and lauren.sex_count != 2:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    if lauren.has_tag('tits_out_today'):
                        if lauren.has_tag('blackmailed'):
                            wt_image cheater_office_3_34
                            player.c "Lose the skirt."
                        else:
                            player.c "Stand up."
                            pass
                    else:
                        wt_image cheater_office_3_15
                        player.c "Strip"
                    wt_image cheater_office_3_39
                    if lauren.sex_count == 1:
                        player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
                        player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
                        wt_image cheater_office_3_93
                        player.c "Get up on here and show me what you can do with your cunt, slut."
                        "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
                        lauren.c "Oh!"
                        wt_image cheater_office_3_94
                        player.c "All right then, get to work.  Up and down, use your legs."
                        wt_image cheater_office_3_95
                        player.c "Right up to the tip on your way up."
                        wt_image cheater_office_3_96
                        player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
                        wt_image cheater_office_3_94
                        player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
                        wt_image cheater_office_3_97
                        player.c "If your cunt gets too dry, play with your clit. You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
                        wt_image cheater_office_3_96
                        "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
                        if lauren.test('desire', 60):
                            wt_image cheater_office_3_98
                            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                            lauren.c "oooooo"
                            wt_image cheater_office_3_99
                            "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_3_94
                            player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes"
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_53
                        wt_image cheater_office_3_95
                        "When she's learned as much as she's going to learn today, you let yourself cum."
                        wt_image cheater_office_3_100
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_office_3_94
                        player.c "You can go back to work now, slut.  Once your legs have recovered from the workout."
                    else:
                        player.c "Lucky you.  You get to ride my pole today, slut."
                        wt_image cheater_office_3_93
                        "Lauren moans as you guide her down onto your dick."
                        lauren.c "Oh!"
                        if lauren.test('submission', 125):
                            wt_image cheater_office_3_94
                            player.c "Feels good, doesn't it, slut?"
                            lauren.c "Yes, Sir."
                            player.c "What should you say?"
                            lauren.c "Thank you for letting me ride your pole, Sir."
                            wt_image cheater_office_3_95
                            player.c "Get to it, then."
                            lauren.c "Yes, Sir"
                            if lauren.test('desire', 60):
                                wt_image cheater_office_3_96
                                "She starts moaning as soon as she starts riding you ..."
                                lauren.c "oooo"
                                wt_image cheater_office_3_98
                                "... and she's soon panting excitedly."
                                lauren.c "oooo  ...  ooooooo"
                                wt_image cheater_office_3_99
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_3_94
                                player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                                wt_image cheater_office_3_95
                                lauren.c "Y ...  yes, Sir."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_54
                            else:
                                wt_image cheater_office_3_101
                                "Even with the occasional rub of her clit, she's not stimulated enough to be able to cum, but she does her best to make it pleasurable for you."
                                change lauren desire by 10
                            wt_image cheater_office_3_96
                            "With Lauren riding faster and faster up and down your shaft, it's not long before your balls need relief."
                            wt_image cheater_office_3_100
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_3_59
                            "She seems comfortable going back to work with your load inside her."
                        elif lauren.test('desire', 60):
                            wt_image cheater_office_3_100
                            player.c "Feels good, doesn't it, slut?"
                            lauren.c "Yes"
                            player.c "What should you be doing now, slut?"
                            lauren.c "Riding your cock."
                            wt_image cheater_office_3_95
                            player.c "Get to it, then."
                            wt_image cheater_office_3_96
                            "She starts moaning as soon as she starts riding you ..."
                            lauren.c "oooo"
                            wt_image cheater_office_3_98
                            "... and she's soon panting excitedly."
                            lauren.c "oooo  ...  ooooooo"
                            wt_image cheater_office_3_99
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_3_94
                            player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                            wt_image cheater_office_3_95
                            "With Lauren riding faster and faster up and down your shaft ..."
                            wt_image cheater_office_3_96
                            "... it's not long before your balls need relief."
                            wt_image cheater_office_3_100
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_3_59
                            "She seems comfortable going back to work with your load inside her."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_55
                        else:
                            wt_image cheater_office_3_94
                            player.c "Feels good, doesn't it, slut?"
                            "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                            wt_image cheater_office_3_95
                            "She may not want to let herself enjoy this, but you certainly enjoy it as you guide her up ..."
                            wt_image cheater_office_3_96
                            "... and down your shaft."
                            wt_image cheater_office_3_97
                            "She even forgets herself and plays with her clit ..."
                            wt_image cheater_office_3_101
                            "... triggering a small moan as she rides you."
                            lauren.c "oooo"
                            wt_image cheater_office_3_96
                            "It's not enough for her to cum ..."
                            wt_image cheater_office_3_95
                            "... but it makes it more enjoyable for you as you do."
                            wt_image cheater_office_3_94
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_3_32
                            "She dresses quietly, avoiding eye contact with you again."
                            wt_image cheater_office_3_33
                            player.c "You enjoyed that, slut.  Why not admit it?"
                            "She did, but she won't.  Not yet, anyway."
                            change lauren desire by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Use her hypno trigger to ruin her" if lauren.has_tag('trigger_implanted'):
                    $ title = "Do you want to use the hypno trigger to embarrass Lauren in her office?"
                    menu:
                        "Yes, ruin her reputation":
                            player.c "This is a special visit, Lauren."
                            lauren.c "It must be very special if you're using my name."
                            player.c "It is.  I have something very important to tell you."
                            lauren.c "What is it?"
                            player.c "[lauren.trigger_phrase]"
                            if lauren.has_tag('tits_out_today'):
                                wt_image cheater_office_3_106
                            else:
                                wt_image cheater_office_3_103
                            lauren.c "Wh ... ?"
                            player.c "[lauren.trigger_phrase]"
                            if lauren.has_tag('tits_out_today'):
                                pass
                            else:
                                wt_image cheater_office_3_104
                                player.c "Remove your clothes, Lauren."
                                wt_image cheater_office_3_105
                                "She quickly gets naked."
                            wt_image cheater_office_3_102
                            player.c "Crawl over to the intercom and let your receptionist know there's an all staff meeting here in 15 minutes."
                            wt_image cheater_office_3_111
                            "*bzzzz*"
                            lauren.c "I want everyone in my office in 15 minutes."
                            if sophie.location == lauren_office:
                                sophie.c "Yes, Ma'am."
                            else:
                                new_receptionist_lauren.c "Yes, Ma'am."
                            sys "If you follow through on this, Lauren's reputation will be ruined. She'll lose her job, and you'll lose your hold over her. This will be the last time you get to have any fun with Lauren."
                            $ title = "Do you follow through with this?"
                            menu:
                                "Not now":
                                    player.c "Lauren, put your clothes back on."
                                    wt_image cheater_office_3_105
                                    player.c "Call your receptionist and cancel the meeting.  It turned out to be nothing important.  All you will remember about my visit is that we chatted about the weather."
                                    wt_image cheater_office_3_19
                                    "You leave as she gets herself back together.  At least you know her trigger works."
                                "Yes, humiliate her":
                                    player.c "Do you have a file with all of your staff's names?"
                                    lauren.c "Yes"
                                    player.c "Get it out."
                                    wt_image cheater_office_3_40
                                    player.c "Place the file beside you on your desk.  Then spread your legs and expose yourself."
                                    wt_image cheater_office_3_112
                                    player.c "[lauren.trigger_phrase]. You will stay like this until your staff arrive.  When they do, you will tell them it's bonus time."
                                    player.c "Read off their names, one by one. Offer each of the men their choice of either a blow job or a fuck. Offer each of the women the opportunity to lick your pussy or to have you lick theirs."
                                    player.c "If any of them take you up on your offer, you will honor it.  Either here and now, or at a spot and time of their choosing.  Make sure they understand they can collect their bonus at any time."
                                    player.c "[lauren.trigger_phrase]. Do you understand your instructions?"
                                    lauren.c "Yes, I understand. As a staff bonus, I will fuck or blow each employee if they are a man, and lick their pussy or let them lick mine if they are a woman. Either now or whenever they choose."
                                    $ title = "Make it even worse?"
                                    menu:
                                        "Yes, ruin her future opportunities, too":
                                            "This will cost Lauren this job, but she'll rebound and get another job somewhere else, possibly in a different field, likely in a different city. You decide to limit her options."
                                            player.c "[lauren.trigger_phrase]. From now on, Lauren, whenever you enter an office building, you will get intensely horny."
                                            player.c "The feeling of entering the lobby of an office tower, the feeling of entering any office, will be the most arousing sensation you have ever felt in your life."
                                            player.c "If you are ever offered a job interview that takes place in an office, you will be so aroused, and so thankful at the opportunity, you will offer oral sex to every one of the interviewers."
                                            player.c "You will suck the cock or lick the pussy of any interviewer who accepts your offer. Do you understand?"
                                            wt_image cheater_office_3_113
                                            lauren.c "Yes. Offices make me horny. I'm getting crazy horny right now just standing in one."
                                            lauren.c "If I get an interview for a job in an office, I will be so thankful I will let the interviewers know I will happily blow or lick them."
                                            player.c "[lauren.trigger_phrase]. Don't forget these important instructions I've given you, Lauren."
                                            lauren.c "I won't.  Not ever."
                                        "No, losing this job is enough":
                                            pass
                                    "There's a limit to what you can get someone to do, even under hypnosis.  That this is working means that Lauren, at some level, has contemplated fucking her coworkers.  Possibly she's even had sex with some of them.  Never, of course, like this."
                                    if sophie.location == lauren_office:
                                        wt_image cheater_office_humiliate_6
                                        "You'd like to stick around to see if Lauren's receptionist makes her eat her out ..."
                                        wt_image cheater_office_humiliate_7
                                        "... or maybe prefers to taste the boss' pussy."
                                    else:
                                        wt_image cheater_office_humiliate_8
                                        "You'd like to stick around to see if Lauren's new receptionist makes use of her mouth ..."
                                        wt_image cheater_office_humiliate_9
                                        "... or maybe prefers to fuck the boss' pussy."
                                    wt_image cheater_office_3_112
                                    "But the prudent thing is to make yourself scarce before the festivities begin."
                                    call convert(lauren,'unavailable') from _call_convert_151
                                    add tags 'humiliated_in_office' to lauren
                        "No":
                            jump menu_lauren_office_visit_1_menu_1
                "Nothing more today":
                    if lauren.has_tag('tits_out_today'):
                        wt_image cheater_office_3_40
                    else:
                        wt_image cheater_office_3_19
                    lauren.c "That's good, because I have a negotiation I need to prepare for.  I trust you can find your own way out?"
        # second outfit
        else:
            if lauren.has_tag('blackmailed'):
                wt_image cheater_office_4_1
                lauren.c "You again?  What do you want now?"
            elif lauren.has_tag('love_potion_used'):
                wt_image cheater_office_4_2
                lauren.c "Hello! I'm glad you dropped by to visit."
                if lauren.test('submission', 125):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out, Sir?"
                elif lauren.test('submission', 75):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out?"
            else:
                wt_image cheater_office_4_1
                player.c "Hello, slut."
                if lauren.test('submission', 125):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Hello, Sir.  Should my tits be out?"
                elif lauren.test('submission', 75):
                    add tags 'offered_tits_today' to lauren
                    lauren.c "Should my tits be out?"
                else:
                    lauren.c "Hello.  What can I do for you?"
            wt_image cheater_office_4_3
            if lauren.has_tag('offered_tits_today'):
                $ title = "What do you want?"
                menu:
                    "Yes, tits out":
                        add tags 'tits_out_today' to lauren
                        wt_image cheater_office_4_4
                        "She removes her suit coat and pulls open her top."
                        wt_image cheater_office_4_5
                        if lauren.test('submission', 125):
                            lauren.c "Can I do anything else for you, Sir?"
                        else:
                            lauren.c "Is that all you wanted?"
                    "No, lift your skirt":
                        wt_image cheater_office_4_6
                        if lauren.test('submission', 125):
                            lauren.c "Can I do anything else for you, Sir?"
                        else:
                            lauren.c "Is that all you wanted?"
            wt_image cheater_office_4_3
            $ title = "What do you want?"
            menu menu_lauren_office_visit_2_menu_1:
                "Get your tits out" if not lauren.has_any_tag('offered_tits_today','tits_out_today'):
                    add tags 'tits_out_today' to lauren
                    player.c "You can start by showing me your tits so I know you're grateful for my visit."
                    wt_image cheater_office_4_4
                    if lauren.has_tag('blackmailed'):
                        "She removes her suit coat and pulls open her top as she addresses you sarcastically."
                        lauren.c "It's so great you visited.  Are you going now?"
                    else:
                        "She removes her suit coat and pulls open her top."
                        wt_image cheater_office_4_5
                        lauren.c "Was there anything else?"
                    jump menu_lauren_office_visit_2_menu_1
                "Lift your skirt" if not lauren.has_any_tag('offered_tits_today','tits_out_today'):
                    player.c "You can start by demonstrating that you're grateful for my visit.  Lift up your skirt."
                    wt_image cheater_office_4_6
                    if lauren.has_tag('blackmailed'):
                        lauren.c "I'm so grateful you visited my panties are completely dry.  Feel free to leave at any time."
                    else:
                        lauren.c "Was there anything else?"
                    jump menu_lauren_office_visit_2_menu_1
                "Hypnotize her" if player.can_hypno(lauren):
                    if lauren.has_tag('blackmailed'):
                        add tags 'no_hypnosis' to lauren
                        "With you blackmailing her, Lauren is too wary around you to lower her guard enough for you to hypnotize her."
                        jump menu_lauren_office_visit_2_menu_1
                    else:
                        add tags 'continuing_office_hypnosis_outfit_2' to lauren
                        # note: this causes the normal weekday Hypnotize Her action to now run; artwork is handled in _hypnosis_start, etc.
                        $ queue_action(lauren.hypno_action)
                "Spank her":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    wt_image cheater_office_4_7
                    if lauren.has_tag('blackmailed'):
                        player.c "You need a reminder of your place in this relationship, slut.  Remove your top and bend over the desk."
                    elif lauren.submission > 75:
                        player.c "I feel like spanking you today, slut.  Remove your top and bend over the desk."
                    else:
                        player.c "I shouldn't have to remind you to bare your breasts to thank me for visiting you at work.  Remove your top and bend over the desk."
                    wt_image cheater_office_4_8
                    "*smack*  *smack*  *smack*"
                    lauren.c "nnnnnn"
                    player.c "Your skirt's in the way.  Lose it, and stick your ass out more."
                    wt_image cheater_office_4_9
                    if lauren.has_tag('blackmailed'):
                        lauren.c "Gee, I hope this makes it easier for you."
                        player.c "That attitude makes it a lot easier, yes.  So will you climbing on the desk to present your ass to me."
                    elif lauren.submission > 125:
                        lauren.c "Is this better, Sir?"
                        player.c "A bit.  Climb up on the desk and present your ass to me."
                    else:
                        player.c "Climb right up on the desk and present your ass to me."
                    wt_image cheater_office_4_13
                    "*smack*  *smack*  *smack*"
                    lauren.c "nnnnnn"
                    wt_image cheater_office_4_10
                    "As the spanking continues she tries, not entirely successfully, to keep from crying out ... *smack*  *smack*  *smack*"
                    lauren.c "nnnnnn  ...  ow!  ...  nnnnnnn  ...   ow!"
                    change lauren submission by 5
                    wt_image cheater_office_4_7
                    if lauren.has_tag('blackmailed'):
                        player.c "I hope these remedial lessons in obedience aren't going to be needed in the future, slut."
                        lauren.c "I guess even blackmailers can't get everything their own way."
                    # note: next test is against 70 to align with prior test before submission was changed
                    elif lauren.submission > 70:
                        player.c "You don't object to me spanking you just because I want to, do you slut?"
                        if lauren.test('submission', 125):
                            lauren.c "No, Sir.  Thank you for not making it too painful."
                        else:
                            lauren.c "I guess not."
                    # these next tests use 'test' instead of base stat
                    else:
                        player.c "I hope these remedial lessons in obedience aren't going to be needed in the future, slut."
                        if lauren.test('submission', 125):
                            lauren.c "I hope not, too, Sir.  I'll try to remember to greet you properly next time."
                        elif lauren.test('submission', 75):
                            lauren.c "I'll try to remember to greet you properly next time."
                    change player energy by -energy_short notify
                "Test her obedience":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "I want you naked.  When you've finished undressing, get me a cup of coffee."
                    wt_image cheater_office_4_11
                    lauren.c "I can't do that.  The coffee station is off the main hallway."
                    player.c "I thought you were supposed to be a good businesswoman, and you don't even know how to get a guest a cup of coffee?"
                    wt_image cheater_office_phone_5
                    "Lauren thinks for a bit, then gets on the phone and places a few intercom calls, giving out tasks to various employees."
                    wt_image cheater_office_4_12
                    "A couple of minutes later she takes a cautious peek out into the hallway ..."
                    wt_image cheater_office_4_14
                    "... then bolts."
                    wt_image cheater_office_4_15
                    "While she's gone, you have time to look through the files on her desk, but at least for this version of the game, you can't find anything interesting."
                    wt_image cheater_office_4_16
                    "She's not gone very long, anyway."
                    if lauren.has_tag('blackmailed'):
                        lauren.c "Here's your damn coffee."
                        player.c "Feels good to follow instructions, doesn't it?"
                        lauren.c "It feels like I'm being blackmailed by an idiot.  What if I'd been spotted?"
                    elif lauren.test('submission', 125):
                        lauren.c "Here's your coffee, Sir."
                        player.c "Feels good to follow instructions, doesn't it?"
                        lauren.c "I was worried I'd be spotted, Sir.  I don't think we should do that again."
                    else:
                        lauren.c "I managed to get your coffee without being spotted."
                        player.c "Feels good to follow instructions, doesn't it?"
                        lauren.c "That seemed like a real risk.  I don't think we should do that again."
                    player.c "A clever executive like you?  I knew you could handle a coffee order.  Did you remember to add cream and sugar?"
                    if not lauren.has_tag('office_brought_coffee_naked'):
                        add tags 'office_brought_coffee_naked' to lauren
                        change lauren submission by 10 notify
                    "The office brew is too weak to restore your energy, but at least having fun with Lauren didn't cost you any energy, either."
                "Eat her out":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "Get up on your desk."
                    if lauren.has_tag('tits_out_today'):
                        pass
                    else:
                        wt_image cheater_office_4_19
                    player.c "Don't look so nervous.  You'll enjoy this."
                    wt_image cheater_office_4_21
                    lauren.c "Oh!"
                    wt_image cheater_office_4_22
                    "After the shock of you latching onto her pussy, it takes a bit of time before she does actually enjoy this."
                    wt_image cheater_office_4_20
                    "Eventually, though, the steady lapping of your tongue extracts both a moan and a trickle of juices."
                    lauren.c "oooo"
                    if lauren.test('desire', 30):
                        wt_image cheater_office_4_21
                        "The trickle soon becomes a flood, and before long she's bucking her hips up against your mouth in orgasm."
                        lauren.c "oooooo ... y ... yes ... aaahhhh!"
                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_56
                    else:
                        wt_image cheater_office_4_22
                        "Her mind and body never fully relax enough for her to cum, but the steady stream of liquid seeping out of her lets you know she enjoyed herself anyway."
                        lauren.c "oooooo"
                    $ lauren.pleasure_her_count += 1
                    call lauren_pleasure_her_stat_changes from _call_lauren_pleasure_her_stat_changes_6
                    wt_image cheater_office_4_23
                    "Lauren seems happy as she gets back to work.  Your visit was indeed more enjoyable than she expected."
                    change player energy by -energy_short notify
                "Blow job":
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    call lauren_continuing_office_2_oral from _call_lauren_continuing_office_2_oral
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Fuck her on her desk" if lauren.sex_count != 1:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "Get up on your desk."
                    if lauren.has_tag('tits_out_today'):
                        pass
                    else:
                        wt_image cheater_office_4_19
                        player.c "Don't be shy, slut.  Spread your legs wide."
                    if lauren.sex_count == 0:
                        lauren.c "You're not going to ..."
                        player.c "Yes, slut.  That's exactly what I'm going to do."
                        wt_image cheater_office_4_34
                        "You rip her panties off and slip the head of your cock into her."
                        lauren.c "nnnnn"
                        wt_image cheater_office_4_32
                        "She knew this day was coming, when you'd use her for sex.  She'd been dreading it, but she knew she wouldn't be able to tell you 'no' when the time came."
                        player.c "Don't look so sad, slut.  You may even enjoy being my personal fuck toy."
                        lauren.c "I don't want to enjoy it."
                        player.c "You might enjoy it anyway."
                        wt_image cheater_office_4_35
                        "She doesn't really enjoy herself.  Not today, anyway."
                        wt_image cheater_office_4_34
                        "But despite her reservations, her body does get wet as you fuck her.  She knows it, and she knows you know it."
                        wt_image cheater_office_4_32
                        player.c "It's okay if you cum, as long as it doesn't interfere with my pleasure."
                        lauren.c "I'm not going to cum.  I don't even want to cum."
                        wt_image cheater_office_4_36
                        "The same cannot be said of you."
                        player.c "[player.orgasm_text]"
                        wt_image cheater_office_4_3
                        "She dresses quietly, avoiding eye contact with you"
                        player.c "Don't you want to say something to me?"
                        lauren.c "What?"
                        player.c "Shouldn't you be thanking me for letting you have sex with me?"
                        lauren.c "Are you kidding me?"
                        if lauren.has_tag('whore'):
                            player.c "No. Your husband and I are your only sources of sex from here out, other than your johns. And I can cut you off from whoring anytime I want. You should be grateful for access to my cock."
                        else:
                            player.c "No.  Your husband and I are your only sources of sex from here out.  You should be grateful for access to my cock."
                        "She can't bring herself to thank you and you don't push it, as that may be a step too far for her right now.  But you've made your point."
                        change lauren submission by 10
                    else:
                        # note: test is purposefully against unmodified stat
                        if lauren.desire > 60 and not lauren.has_tag('blackmailed'):
                            wt_image cheater_office_4_33
                            "A little smile crosses her face as you take out your cock and step between her legs."
                        wt_image cheater_office_4_34
                        "You rip her panties off and slip the head of your cock into her."
                        lauren.c "Oh!"
                        wt_image cheater_office_4_32
                        if lauren.test('submission', 125):
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes, Sir."
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me, Sir.  Please fuck me?"
                            player.c "Maybe I've changed my mind.  Maybe I'm not going to fuck you today?"
                            lauren.c "Please don't do that, Sir.  I want to be fucked by you.  Please fuck me, Sir.  Please?"
                            player.c "Gentle or rough?"
                            lauren.c "However you want to fuck me, Sir."
                            $ title = "How do you want to fuck her?"
                            menu:
                                "Gently":
                                    wt_image cheater_office_4_39
                                    player.c "What if I slowly strip you naked as I fuck you?"
                                    lauren.c "Oh!  Yes, Sir!  That feels amazing."
                                    if lauren.test('desire', 60):
                                        wt_image cheater_office_4_40
                                        "Her excitement builds quickly, so you try and slow things down."
                                        "You stop thrusting and just hold her close to you, but the feel of your body against her, your cock impaled, deep inside her just seems to excite her more ..."
                                        lauren.c "oooooo  ...  ooooooo"
                                        wt_image cheater_office_4_41
                                        ".. and she orgasms as soon as you start moving again."
                                        lauren.c "Aaahhhh!!!!"
                                        wt_image cheater_office_4_39
                                        "She's not the only one finding it hard to control herself."
                                        call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_57
                                    else:
                                        wt_image cheater_office_4_40
                                        "You take your time, and while she gets very, very wet, she doesn't quite get excited enough to cum."
                                        lauren.c "oooo"
                                        wt_image cheater_office_4_39
                                        "You, on the other hand, soon need relief from the pressure slowly building in your balls."
                                        change lauren desire by 10
                                    $ title = "Where do you want to cum?"
                                    menu:
                                        "In her":
                                            wt_image cheater_office_4_40
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                            wt_image cheater_office_4_7
                                            lauren.c "Your cum is going to be dripping out of me all day."
                                        "On her":
                                            wt_image cheater_cum_1
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                            wt_image cheater_office_4_7
                                            lauren.c "Your cum is going to be sticking to my belly and skirt all day."
                                    player.c "Is that a complaint, slut?"
                                    wt_image cheater_office_4_23
                                    lauren.c "Definitely not, Sir.  Just an observation."
                                "Rough":
                                    wt_image cheater_office_4_36
                                    player.c "Rough it is."
                                    lauren.c "Oh!  Thank you, Sir!!"
                                    if lauren.test('desire', 60):
                                        wt_image cheater_office_4_37
                                        "Her excitement builds quickly, so you fuck her harder and harder, trying to hurt her with your cock ..."
                                        lauren.c "oooooo  ...  ooooooo"
                                        wt_image cheater_office_4_38
                                        "... which succeeds only in getting her off faster."
                                        lauren.c "Aaahhhh!!!!"
                                        wt_image cheater_office_4_36
                                        "You can't control yourself after that display.  Your balls release your seed inside her."
                                        player.c "[player.orgasm_text]"
                                        lauren.c "Oh!"
                                    else:
                                        wt_image cheater_office_4_37
                                        "She doesn't get aroused enough to cum, but she's clearly enjoying this."
                                        lauren.c "oooo"
                                        wt_image cheater_office_4_36
                                        "You're enjoying it even more."
                                        lauren.c "Oh!"
                                        change lauren desire by 10
                                    wt_image cheater_office_4_11
                                    lauren.c "My cunt's going to be sore all day."
                                    player.c "Is that a complaint, slut?"
                                    wt_image cheater_office_4_18
                                    lauren.c "No, Sir.  A compliment, I think."
                        elif lauren.test('desire', 60):
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes"
                            player.c "What do you want, slut?"
                            lauren.c "I want you to fuck me until I cum."
                            $ title = "How do you want to fuck her?"
                            menu:
                                "Gently":
                                    wt_image cheater_office_4_39
                                    player.c "What if I slowly strip you naked as I fuck you?"
                                    lauren.c "Oh!  Fuck, that feels amazing."
                                    wt_image cheater_office_4_40
                                    "Her excitement builds quickly, so you try and slow things down."
                                    "You stop thrusting and just hold her close to you, but the feel of your body against her, your cock impaled, deep inside her just seems to excite her more ..."
                                    lauren.c "oooooo  ...  ooooooo"
                                    wt_image cheater_office_4_41
                                    ".. and she orgasms as soon as you start moving again."
                                    lauren.c "Aaahhhh!!!!"
                                    wt_image cheater_office_4_39
                                    "She's not the only one finding it hard to control herself."
                                    $ title = "Where do you want to cum?"
                                    menu:
                                        "In her":
                                            wt_image cheater_office_4_40
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                            wt_image cheater_office_4_7
                                            lauren.c "Your cum is going to be dripping out of me all day."
                                        "On her":
                                            wt_image cheater_cum_1
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                            wt_image cheater_office_4_7
                                            lauren.c "Your cum is going to be sticking to my belly and skirt all day."
                                    player.c "Is that a complaint, slut?"
                                    wt_image cheater_office_4_23
                                    lauren.c "Not really."
                                "Rough":
                                    wt_image cheater_office_4_36
                                    player.c "Even if I pound you hard and rough?"
                                    lauren.c "Oh!  Y ... yess!"
                                    wt_image cheater_office_4_37
                                    "Her excitement builds quickly, so you fuck her harder and harder, trying to hurt her with your cock ..."
                                    lauren.c "oooooo  ...  ooooooo"
                                    wt_image cheater_office_4_38
                                    "... which succeeds only in getting her off faster."
                                    lauren.c "Aaahhhh!!!!"
                                    wt_image cheater_office_4_36
                                    "You can't control yourself after that display.  Your balls release your seed inside her."
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_4_11
                                    lauren.c "My cunt's going to be sore all day."
                                    player.c "Is that a complaint, slut?"
                                    wt_image cheater_office_4_18
                                    lauren.c "Not a major one."
                                    change lauren submission by 5
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_58
                        else:
                            player.c "Does that feel good, slut?"
                            "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                            $ title = "How do you want to fuck her?"
                            menu:
                                "Gently":
                                    wt_image cheater_office_4_39
                                    player.c "What if I slowly strip you naked as I fuck you?  Maybe then you'd admit you like this?"
                                    lauren.c "Oh! "
                                    wt_image cheater_office_4_40
                                    "You take your time, and while she gets very, very wet, she doesn't quite get excited enough to cum."
                                    lauren.c "oooo"
                                    wt_image cheater_office_4_39
                                    "You, on the other hand, soon need relief from the pressure slowly building in your balls."
                                    $ title = "Where do you want to cum?"
                                    menu:
                                        "In her":
                                            wt_image cheater_office_4_40
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                        "On her":
                                            wt_image cheater_cum_1
                                            player.c "[player.orgasm_text]"
                                            lauren.c "Oh!"
                                    wt_image cheater_office_4_7
                                    player.c "You enjoyed that, slut.  Why not admit it?"
                                    if lauren.has_tag('blackmailed'):
                                        lauren.c "Gee, why wouldn't I want to have sex with my blackmailer?  I wonder??"
                                        wt_image cheater_office_4_42
                                        "She returns to her work.  It seems she wants to pretend this didn't just happen."
                                    else:
                                        wt_image cheater_office_4_42
                                        "She did, but she won't.  Not yet, anyway.  She ignores you and returns to her work.  It seems she wants to pretend this didn't just happen."
                                    change lauren desire by 5
                                "Rough":
                                    wt_image cheater_office_4_36
                                    "If she's not going to enjoy herself anyway, there's no need to try and make this pleasurable for her."
                                    lauren.c "Oh!"
                                    wt_image cheater_office_4_38
                                    "You thrust into her harder and harder, using her like a fuck doll ... only one that cries out when you hurt it."
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_36
                                    "And like any good fuck doll, you fill it with cum when you're finished abusing it."
                                    wt_image cheater_office_4_34
                                    player.c "[player.orgasm_text]"
                                    wt_image cheater_office_4_7
                                    player.c "Is your cunt sore?"
                                    wt_image cheater_office_4_42
                                    "She ignores you and returns to her work.  It seems she wants to pretend she didn't just let you use her like a sex toy."
                                    change lauren submission by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Fuck her from behind" if lauren.sex_count > 1:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "Turn around and bend over your desk."
                    wt_image cheater_office_4_52
                    "As she does, you lift her skirt and insert the head of your cock inside her."
                    lauren.c "Oh!"
                    if lauren.sex_count == 2:
                        wt_image cheater_office_4_53
                        player.c "Let's see if you're getting any better at fucking, Lauren. I'm going to hold myself here you're going to do the work."
                        player.c  "You'll need to buck your hips and squeeze my cock to milk an orgasm out of me.  You know how to use your Kegel muscles to squeeze a cock, slut?"
                        "Lauren nods."
                        player.c "Good.  Then get at it."
                        wt_image cheater_office_4_54
                        "You don't say anything more.  You just hold yourself and her in place and watch as she struggles to pleasure your cock within the limited range of movement you give her."
                        if lauren.test('desire', 60):
                            wt_image cheater_office_4_55
                            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her and your hands on her hips her triggers a response."
                            lauren.c "oooooo"
                            wt_image cheater_office_4_56
                            "Quick and intense, the orgasm rips through her, catching her by surprise.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_4_53
                            player.c "Don't you stop. Don't even pause. This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_59
                        wt_image cheater_office_4_57
                        "Lauren tries very hard to pleasure your cock, but it's not easy within the limited range of motion you allow her."
                        wt_image cheater_office_4_54
                        "She start to worry that the squeezing and hip rolls won't be enough to get you off."
                        wt_image cheater_office_4_53
                        "Fortunately for her, the sight of her working so hard to extract your cum is itself a big turn on, and you feel your orgasm building."
                        wt_image cheater_office_4_55
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_office_4_53
                        player.c "That felt good, didn't it?  Working to earn my cum."
                        if lauren.submission > 125:
                            lauren.c "Yes, Sir"
                            if lauren.desire <= 60:
                                change lauren desire by 10
                        elif lauren.desire > 60:
                            lauren.c "Yes"
                            change lauren submission by 5
                        else:
                            "She says nothing, but the pace of her breathing tells you she's turned on."
                            change lauren submission by 5
                            change lauren desire by 5
                    else:
                        if lauren.test('submission', 75):
                            wt_image cheater_office_4_53
                            player.c "Does that feel good, slut?"
                            lauren.c "Yes, Sir."
                            wt_image cheater_office_4_58
                            lauren.c "Ow!"
                            player.c "Even when I fuck you rough?"
                            lauren.c "Yes, Sir!!"
                            wt_image cheater_office_4_55
                            "You pound her as fast and as hard as you can."
                            lauren.c "oooo"
                            wt_image cheater_office_4_58
                            "Hurting her with your cock as much as you can."
                            lauren.c "Ow!"
                            if lauren.test('desire', 60):
                                wt_image cheater_office_4_57
                                "She still gets excited ..."
                                wt_image cheater_office_4_56
                                "... and starts climaxing on your cock."
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_4_53
                                player.c "Keep moving your hips, slut.  The goal is my pleasure, not yours."
                                lauren.c "Y ...  yes, Sir."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_60
                            else:
                                wt_image cheater_office_4_57
                                "She gets surprisingly wet considering the rough treatment you give her, though it's not enough for her to cum."
                                lauren.c "ooooooo"
                                change lauren desire by 10
                            wt_image cheater_office_4_54
                            "Lauren's legs start to tremble from the constant, unrelenting battering ..."
                            wt_image cheater_office_4_58
                            "... but she otherwise takes the assault well, considering how tender her sex must be getting."
                            lauren.c "oooo ... ow! ... ow! ... oooo"
                            wt_image cheater_office_4_56
                            "Fortunately for her, there's only so much of this treatment you can give her before your need to cum becomes overwhelming."
                            lauren.c "oooo ... ow! ... ow! ... oooo"
                            wt_image cheater_office_4_55
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_4_59
                            player.c "Are you okay, slut?"
                            lauren.c "Yes, Sir.  I'm just really sore between my legs right now."
                            player.c "Is that a complaint, slut?"
                            lauren.c "Definitely not, Sir."
                        else:
                            $ title = "How do you want to fuck her?"
                            menu:
                                "Gently":
                                    wt_image cheater_office_4_53
                                    player.c "Does that feel good, slut?"
                                    if lauren.test('desire', 60):
                                        lauren.c "Yes"
                                        player.c "Maybe you should tell me what you want, then?"
                                        lauren.c "Ohhh ... I want you to fuck me until I cum."
                                        wt_image cheater_office_4_54
                                        player.c "I don't know, slut.  It may take you a while for you to cum."
                                        lauren.c "oooo ... no, no it won't."
                                        wt_image cheater_office_4_53
                                        player.c "You can't expect me to worry about whether you're going to cum, when this is supposed to be about my pleasure?"
                                        lauren.c "oooooo ... I'll make it feel good for you.  See?  I'll squeeze you and fuck you while you're fucking me."
                                        wt_image cheater_office_4_57
                                        player.c "I like that, slut.  Make this feel good for me.  Maybe it'll take your mind off your own arousal?"
                                        wt_image cheater_office_4_56
                                        "Seems not."
                                        lauren.c "Aaahhhh!!!!"
                                        wt_image cheater_office_4_57
                                        player.c "Don't stop moving, slut.  You're supposed to be making this feel nice for me, remember?"
                                        lauren.c "Y ... yess"
                                        wt_image cheater_office_4_54
                                        "It doesn't take her long to make that happen."
                                        wt_image cheater_office_4_55
                                        player.c "[player.orgasm_text]"
                                        lauren.c "Oh!"
                                        wt_image cheater_office_4_60
                                        player.c "Is there something you want to say to me?"
                                        if lauren.has_tag('blackmailed'):
                                            lauren.c "About what?  We both know I didn't have a choice.  Don't pretend like this is consensual."
                                            player.c "I had a choice.  I didn't need to make that something you'd enjoy."
                                            wt_image cheater_office_4_18
                                            lauren.c "Then thank you for not being a complete asshole, I guess."
                                        else:
                                            lauren.c "Thank you for that.  It felt nice."
                                    else:
                                        "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                                        wt_image cheater_office_4_52
                                        "Slowly and carefully you start to slide in and out of her ..."
                                        wt_image cheater_office_4_54
                                        "... until you're rewarded with a little moan."
                                        lauren.c "oooo"
                                        wt_image cheater_office_4_53
                                        player.c "Are you sure this isn't feeling good, slut?  Because you seem to be rather wet."
                                        wt_image cheater_office_4_54
                                        "She stays quiet until the next thrust, which elicits another soft moan."
                                        lauren.c "oooo"
                                        wt_image cheater_office_4_57
                                        player.c "That's what I thought.  You like this, slut.  You're allowed to admit it."
                                        lauren.c "oooo"
                                        wt_image cheater_office_4_53
                                        "As much as her body does like this, yours likes it even more."
                                        wt_image cheater_office_4_54
                                        player.c "[player.orgasm_text]"
                                        lauren.c "Oh!"
                                        wt_image cheater_office_4_6
                                        player.c "Stop pretending like you didn't get turned on by that.  We both know you did."
                                        wt_image cheater_office_4_42
                                        "She ignores you and goes back to work, but she knows you're right."
                                        change lauren desire by 5
                                "Rough":
                                    wt_image cheater_office_4_58
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_53
                                    player.c "I know you were hoping I was going to make this enjoyable for you."
                                    wt_image cheater_office_4_58
                                    lauren.c "Ow!"
                                    player.c "But we both know that this about my pleasure, not yours."
                                    wt_image cheater_office_4_55
                                    player.c "So if I want to fuck you hard and rough ..."
                                    wt_image cheater_office_4_52
                                    player.c "... and slap your ass as I fuck you ..."
                                    "*smack*"
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_56
                                    player.c "... are you going to say anything?"
                                    lauren.c "nnnnn"
                                    wt_image cheater_office_4_55
                                    player.c "... or are you going to be an obedient slut and take it however I choose to give it to you?"
                                    wt_image cheater_office_4_53
                                    player.c "Tell me I can use you like my fuck doll, slut."
                                    wt_image cheater_office_4_58
                                    lauren.c "Ow!"
                                    player.c "Tell me, because I'm not going to cum until you do."
                                    wt_image cheater_office_4_53
                                    lauren.c "Yes"
                                    player.c "Yes, what?"
                                    wt_image cheater_office_4_58
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_53
                                    lauren.c "Yes, you can fuck me like a fuck doll."
                                    wt_image cheater_office_4_52
                                    "*smack*"
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_56
                                    player.c "Move your ass, fuck doll, unless you want me here all afternoon."
                                    wt_image cheater_office_4_57
                                    "She moves her hips back and forth, milking your cock as you spank her ... *smack*  *smack*  *smack* ..."
                                    lauren.c "Ow!"
                                    wt_image cheater_office_4_56
                                    "... until you fill her with your load."
                                    player.c "[player.orgasm_text]"
                                    lauren.c "Oh!"
                                    wt_image cheater_office_4_19
                                    player.c "That was good, slut.  I'll let you be my fuck doll again sometime soon."
                                    change lauren submission by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Have her ride you" if lauren.sex_count > 0:
                    $ lauren.training_session() ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "Take your top off."
                    wt_image cheater_office_4_7
                    if lauren.sex_count == 1:
                        player.c "Last time you showed me you could take a fucking, Lauren, but I had to do all the work."
                        player.c "A good little slut doesn't just spread her legs on command.  She needs to be able to please a man with her cunt, at least as well as she can please him with her mouth."
                        player.c "Get up on here and show me what you can do with your cunt, slut."
                        wt_image cheater_office_4_43
                        "Nervously, Lauren climbs up on top of you.  You guide her down onto your dick."
                        lauren.c "Oh!"
                        wt_image cheater_office_4_44
                        player.c "All right, slut, get to work.  Show my cock a good time."
                        wt_image cheater_office_4_45
                        player.c "Up and down, use your legs.  Right up to the tip on your way up."
                        wt_image cheater_office_4_46
                        player.c "Slam down hard at the bottom of the stroke.  Get my cock all the way inside you."
                        wt_image cheater_office_4_44
                        player.c "Use your hips too.  Rock them back and forth to change the angle of pressure."
                        wt_image cheater_office_4_47
                        player.c "If your cunt gets too dry, play with your clit. You need to train your body to get wet when you need it wet, or these fuck sessions are going to get very uncomfortable, very fast."
                        wt_image cheater_office_4_43
                        "With your hands on her hips, you guide her body to follow along with your instructions.  Lauren's never before had anyone tell her how he wants to be fucked."
                        if lauren.test('desire', 60):
                            wt_image cheater_office_4_48
                            "Lauren tries very hard to concentrate on your instructions.  Despite herself, the feeling of your cock inside her, your hands on her hips and your words in her ear triggers a response in her body."
                            lauren.c "oooooo"
                            wt_image cheater_office_4_49
                            "It's not her biggest orgasm ever, but it's fast and intense and catches her by surprise.  She lets out a moan as her body shudders around your cock."
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_4_48
                            player.c "Don't you stop.  Don't even pause.  This isn't about your pleasure, slut, it's about mine. You don't let your orgasms interfere with pleasuring my cock, is that understood?"
                            lauren.c "Y ... yes"
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_61
                        wt_image cheater_office_4_50
                        "When she's learned as much as she's going to learn today, you let yourself cum."
                        wt_image cheater_office_4_47
                        player.c "[player.orgasm_text]"
                        lauren.c "Oh!"
                        wt_image cheater_office_4_44
                        player.c "You can go back to work now, slut.  Once your legs have recovered from the workout."
                    else:
                        player.c "I'm going to let you have another ride on my pole today, slut."
                        wt_image cheater_office_4_43
                        "Lauren moans as you guide her down onto your dick."
                        lauren.c "Oh!"
                        if lauren.test('submission', 125):
                            wt_image cheater_office_4_44
                            player.c "Feels good, doesn't it, slut?"
                            lauren.c "Yes, Sir."
                            player.c "What should you say?"
                            lauren.c "Thank you for letting me ride your pole, Sir."
                            wt_image cheater_office_4_46
                            player.c "Get to it, then."
                            lauren.c "Yes, Sir"
                            if lauren.test('desire', 60):
                                wt_image cheater_office_4_45
                                "She starts moaning as soon as she starts riding you ..."
                                lauren.c "oooo"
                                wt_image cheater_office_4_48
                                "... and before long she's unable to control her excitement."
                                lauren.c "oooo  ...  ooooooo"
                                wt_image cheater_office_4_49
                                lauren.c "Aaahhhh!!!!"
                                wt_image cheater_office_4_48
                                player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                                lauren.c "Y ...  yes, Sir."
                                call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_62
                            else:
                                wt_image cheater_office_4_45
                                "She's clearly enjoying the ride ..."
                                lauren.c "oooo"
                                wt_image cheater_office_4_43
                                "... but not enough to get off today."
                                wt_image cheater_office_4_46
                                "She makes sure you're not going to have the same problem, though."
                                change lauren desire by 10
                            wt_image cheater_office_4_45
                            "She rides you up to the tip of your cock ..."
                            wt_image cheater_office_4_46
                            "... then back down ..."
                            wt_image cheater_office_4_43
                            "... faster and faster ..."
                            wt_image cheater_office_4_46
                            "... until she earns your spunk."
                            wt_image cheater_office_4_51
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_4_18
                            "She seems comfortable going back to work with your load inside her."
                        elif lauren.test('desire', 60):
                            wt_image cheater_office_4_44
                            player.c "Feels good, doesn't it, slut?"
                            lauren.c "Yes"
                            player.c "The ride isn't free, slut.  You're only allowed on here in order to get me off.  Get to work."
                            wt_image cheater_office_4_46
                            lauren.c "Okay"
                            wt_image cheater_office_4_45
                            "She starts moaning as soon as she starts riding you ..."
                            lauren.c "oooo"
                            wt_image cheater_office_4_48
                            "... and before long she's unable to control her excitement."
                            lauren.c "oooo  ...  ooooooo"
                            wt_image cheater_office_4_49
                            lauren.c "Aaahhhh!!!!"
                            wt_image cheater_office_4_48
                            player.c "Keep riding my cock, slut.  The goal is my pleasure, not yours."
                            lauren.c "Y ...  yess"
                            wt_image cheater_office_4_45
                            "She rides you up to the tip of your cock ..."
                            wt_image cheater_office_4_46
                            "... then back down ..."
                            wt_image cheater_office_4_43
                            "... faster and faster ..."
                            wt_image cheater_office_4_46
                            "... until she successfully pays for her ride."
                            wt_image cheater_office_4_51
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_4_18
                            "She seems comfortable going back to work with your load inside her."
                            call lauren_orgasm_stat_change from _call_lauren_orgasm_stat_change_63
                        else:
                            wt_image cheater_office_4_44
                            player.c "Feels good, doesn't it, slut?"
                            "She holds her tongue, but the moistening of her sex around your cock tells you her body is starting to accept the situation even if her mind isn't."
                            wt_image cheater_office_4_43
                            "She may not want to let herself enjoy this, but you certainly enjoy it as you guide her up ..."
                            wt_image cheater_office_4_46
                            "... and down your shaft."
                            wt_image cheater_office_4_45
                            "Despite her reservations, eventually she lets out a small moan."
                            lauren.c "oooo"
                            wt_image cheater_office_4_46
                            "She might by unwilling to let herself relax enough to cum ..."
                            wt_image cheater_office_4_43
                            "... but she does more than enough to get you ready."
                            wt_image cheater_office_4_51
                            player.c "[player.orgasm_text]"
                            lauren.c "Oh!"
                            wt_image cheater_office_4_51
                            "She dresses quietly and goes back to work as if nothing had happened."
                            player.c "You enjoyed that, slut.  Why not admit it?"
                            "She did, but she won't.  Not yet, anyway.  For now, she seems intent on ignoring you and whatever her body was feeling when you were inside her."
                            change lauren desire by 5
                    $ lauren.sex_count += 1
                    if lauren.cheated == 0:
                        $ lauren.cheated = 1
                    orgasm notify
                "Nothing more today":
                    if lauren.has_tag('tits_out_today'):
                        wt_image cheater_office_4_17
                    else:
                        wt_image cheater_office_4_18
                    lauren.c "That's good, because I have some performance reviews I need to complete.  I trust you can find your own way out?"
        rem tags 'offered_tits_today' 'tits_out_today' from lauren
    call lauren_in_office_end from _call_lauren_in_office_end_1
    return

label lauren_in_office_end:
    if not lauren.has_tag('office_hypno_now'):
      # bring receptionist back if didn't do anything with Lauren
      if sophie.relationship_status < 6:
          summon sophie to lauren_office no_follows
      else:
          summon new_receptionist_lauren to lauren_office no_follows
      call character_location_return(lauren) from _call_character_location_return_484
      call forced_movement(office_tower) from _call_forced_movement_160
      wt_image current_location.image
    if lauren.has_tag('chastity_belt_call_pending'):
        rem tags 'chastity_belt_call_pending' from lauren
        "You haven't gone far when the call comes in on your phone.  There's no video, Lauren seems to be somewhere dark."
        lauren.c "It's me.  I need you to come take the chastity belt off.  Please?"
        player.c "What's wrong, Lauren?"
        lauren.c "It's your cum.  It's burning my pussy.  I've never been so horny in my whole life.  I need to play with myself.  Please come take the chastity belt off?"
        player.c "Where are you?"
        lauren.c "I'm in a storage room.  I need to cum, but I can't.  I've tried pinching my nipples, grinding my chastity belt against a cabinet.  Nothing works.  I need to get the belt off so I can touch myself."
        player.c "I'm busy now, Lauren.  I can't see you again until tomorrow."
        lauren.c "No!  Please!!  I'll come see you, wherever you are.  If I don't cum, I'm going to go insane.  You don't understand, my pussy feels like it's on fire!  I'm begging you!!  Please, please take the belt off me?  Please???"
        player.c "I'm not going to do that, Lauren.  You'll need to find a different way to cum."
        lauren.c "Nooo!!  I've tried everything!  I need to touch myself.  I need this damn belt off!!"
        "She starts to sob, then suddenly moans."
        lauren.c "Oh ... ooohhh!!  Oh my Gawdddd ... AAAHHHH!!!!"
        "You should have instructed Lauren to stay quiet when she came after crying.  Hopefully the storage room she was in was sound proof.  Assuming she hasn't embarrassed herself too much in the office, she'll be more compliant going forward."
        change lauren desire by 5
        change lauren submission by 5
        change lauren resistance by -5
        notify
    return

label lauren_office_hypno:
    if lauren.office_visit_count > 1:
        # intro only needed for subsequent visits; handled prior to menu choice on first visit
        wt_image cheater_office_1_1
        lauren.c "What is it you want me to do?"
    # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
    $ sophie.dismiss(False)
    $ new_receptionist_lauren.dismiss(False)
    add tags 'office_hypno_now' to lauren
    $ queue_action(lauren.hypno_action)
    return

# Transformation Potion Timer
label lauren_transformation_potion_timer:
  if lauren.has_tag('transformed'):
    "Lauren has already been transformed. There's nothing more the potion can do to her."
  elif lauren.has_tag('waiting_for_club_access') and lauren.transformed_via_object and not lauren.has_tag('stage_message_given'):
    "Lauren has already been transformed. You just need to find her a place where she can safely take her clothes off."
  else:
    if lauren.status == "on_training":
      "You shouldn't try this while Lauren is a client.  Her husband knows she's here, and may become suspicious."
    else:
      $ lauren.temporary_count = 1
      if current_location != living_room:
        "You convince Lauren to join you at home on the pretext of having something important to share with her."
        call forced_movement(living_room) from _call_forced_movement_161
      wt_image cheater_love_potion_1
      if lauren.has_tag('love_potion_used'):
        player.c "Here Lauren, I made you an herbal tea."
        lauren.c "Another one?  Great!"
        wt_image cheater_love_potion_2
        "She takes a deep drink."
      else:
        player.c "Here Lauren, I made you an herbal tea."
        "She looks at it and you in surprise.  She's a smart woman.  Something about this doesn't quite add up for her."
        "However, when she looks in the cup and smells it, it does indeed look and smell like an herbal tea."
        lauren.c "Thank you."
        wt_image cheater_love_potion_2
        "She keeps her eyes on you as she tentatively takes a sip.  It is an herbal tea - a very special blend - and it tastes good."
        "She takes a deeper drink."
      wt_image cheater_love_potion_3
      "It doesn't take long for the potion to take effect.  Lauren's head rolls back and her eyes close as her mind shuts down and the potion opens her up to the potential for great change."
      "You now need to spend some energy helping the potion realize a new potential for her."
      $ lauren.temporary_count = lauren.display_count_clothed + lauren.display_count_lingerie + lauren.display_count_office
      $ title = "What do you want the potion to change her into?"
      menu:
        "Whore" if not lauren.has_tag('whore') and lauren.sex_count > 0:
          "When Lauren agreed to accept your training, money was a part of it.  She didn't want to lose the money her husband would be able to take from her in a divorce."
          "The first time you fucked her, the thought kept going through her mind, if I'm letting a man fuck me to keep my money, does that make me a whore?"
          wt_image cheater_love_potion_7
          "The potion latches on to those thoughts and twists them, until in her mind Lauren doesn't just wonder if she's a whore.  She is a whore.  She fucks men for money and she likes it.  It's all she's ever wanted to be."
          wt_image cheater_love_potion_8
          "When she opens her eyes, she looks at you in confusion at first, then smiles and pulls down her top."
          lauren.c "Are you my date tonight?"
          player.c "No, silly. I'm your pimp."
          wt_image cheater_love_potion_9
          lauren.c "Oh.  Sorry.  I'm feeling a little out of it at the moment."
          "The transformation potion will do that."
          wt_image cheater_love_potion_10
          player.c "Go find a hotel and rest.  I'll let you know when your next date is lined up."
          player.c "Oh, and your husband's an unnecessary complication.  Would you please contact him and tell him to divorce you already?"
          lauren.c "Will he get my money?"
          player.c "Not your working money.  Not the money you earn on your knees, my professional little cock sucker."
          "She nods."
          lauren.c "Okay"
          $ lauren.transformed_via_object = True
          call lauren_convert_whore from _call_lauren_convert_whore_1
        "Showgirl" if not lauren.has_tag('showgirl') and lauren.temporary_count > 5:
          "Under your training, Lauren has become used to displaying her body for your examination."
          "You've made her do it often enough that it's not surprising that her mind has sometimes wondered what it would be like taking her clothes off for a bigger audience?"
          wt_image cheater_love_potion_7
          "The potion latches on to those fleeting thoughts and twists them, until in her mind Lauren doesn't just wonder about what it would be like to take her clothes off in public.  She craves it.  It's the only work she's ever wanted."
          wt_image cheater_love_potion_8
          "As she comes around, she smiles and pulls down her top."
          lauren.c "Can ... can I please dance for you?"
          wt_image cheater_love_potion_11
          lauren.c "This is something I've always wanted to do."
          wt_image cheater_love_potion_12
          lauren.c "I don't know why I've always been too afraid to try it."
          wt_image cheater_love_potion_13
          lauren.c "It's so freeing!"
          wt_image cheater_love_potion_14
          lauren.c "Do you think I would be any good at it?"
          $ title = "What do you tell her?"
          menu:
            "With some practice, yes":
              wt_image cheater_love_potion_15
              player.c "With some practice and the right instruction, yes.  Let's see you try that again from the beginning, and I'll give you some pointers."
              lauren.c "Oh, thank you!"
              if player.has_tag('club_first_visit_complete'):
                wt_image cheater_love_potion_13
                "When you think she's learned enough not to embarrass herself or you, you give her instructions on how to find The Club."
                wt_image cheater_love_potion_15
                lauren.c "Really!  A job so quickly.  Thank you so much!!! I'll be sure to tell them you made me the dancer I am."
                "She has no idea how true that is."
                $ lauren.transformed_via_object = True
                call lauren_convert_showgirl from _call_lauren_convert_showgirl_2
              else:
                wt_image cheater_love_potion_13
                "You help her with her dancing skills as best you can.  You wish you had a place to send her, but unfortunately you don't know of the right place for her just yet."
                wt_image cheater_love_potion_15
                "That doesn't deter her."
                lauren.c "Thank you for the pointers. If you find me some work, I'll be sure to tell them that you made me the dancer I am."
                "She has no idea how true that is."
                $ lauren.transformed_via_object = True
                add tags 'waiting_for_club_access' to lauren
              wt_image cheater_love_potion_16
              "It wasn't a lot of dancing, but coming on the heels of an exhausting transformation, she collapses in a heap to sleep off the effects of the potion."
              "You'll send her on her way in the morning.  And if you choose to use her in the meantime, she'll be too out of it to know, let alone object."
              if lauren.has_tag('whore'):
                "With her new obsession about being a showgirl, Lauren neglects her work as a whore.  You are no longer her pimp."
                call unconvert(lauren, 'whore') from _call_unconvert_57
            "You're hopeless":
              "You shake your head."
              wt_image cheater_love_potion_17
              player.c "Not really.  You're a lot older than most dancers, and you have no sense of rhythm.  I suggest you try a different career, like business."
              wt_image cheater_love_potion_18
              "She breaks out in tears."
              lauren.c "No!  I don't want to be a business woman.  I want to be a stripper!  It's all I've ever wanted."
              lauren.c "And now I've waited too late and it's hopeless and I'm no good at the only thing I ever wanted to do!!"
              wt_image cheater_love_potion_19
              "Crying and pulling at her hair in frustration, she runs off, still half naked.  You don't know where she goes or what she does, but you never see her again."
              # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
              # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
              # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
              call convert(lauren, "unavailable") from _call_convert_85
        "Bimbo" if not lauren.has_tag('bimbo') and lauren.sos > 10:
          "Lauren's a smart woman. Since she's been forced to endure your training and behave like a slut for you and her husband, she's wondered whether this is what life is like for stupid women?"
          "She's even wondered whether would things would be easier if she was an airhead with no thoughts other than to have sex and please the men in her life?"
          wt_image cheater_love_potion_7
          "The potion latches on to those thoughts and twists them, until in her mind Lauren is an airhead. A happy airhead with no thoughts in her head except being a good obedient slut."
          wt_image cheater_love_potion_9
          "As the transformation takes hold, you can almost see the intelligence drain out of Lauren's eyes.  She scratches her head, confused, as she pulls down her top."
          wt_image cheater_love_potion_20
          "When she opens her eyes again, she stares at you, as if trying to decide who you are.  Or maybe who she is?"
          wt_image cheater_love_potion_21
          "Then she examines herself ..."
          wt_image cheater_love_potion_15
          "... and grins."
          wt_image cheater_love_potion_4
          $ lauren.transformed_via_object = True
          call lauren_convert_bimbo from _call_lauren_convert_bimbo
        "Slavegirl" if not lauren.has_tag('slavegirl') and lauren.punishment_count > 1 and lauren.submission > 20:
          "Lauren has always appreciated strong men who know what they want. If she wasn't attracted to that dynamic, she would never have accepted her husband's insistence on becoming his slut, nor would she have accepted your training."
          "Under your training, she's experienced sessions of intense domination, and learned to accept the feeling of submitting to the will of another."
          wt_image cheater_love_potion_7
          "The potion latches on to that feeling and twists it, until in her mind Lauren doesn't just accept being dominated, she craves it. She can't imagine a life in which she isn't ordered around and forced to cater to the whim of her Owner."
          wt_image cheater_love_potion_17
          "As she comes to, she instinctively pulls down her top, exposing her breasts as she lowers her eyes."
          lauren.c "May ... may this worthless slut please have permission to speak?"
          player.c "Go ahead."
          lauren.c "Would you accept ownership of this worthless slut? I have nothing to offer you except my body, but you may have my body, to do with whatever you please."
          lauren.c "I promise I'll be obedient and faithful and grateful for the opportunity to serve you in any way you command of me."
          $ title = "What do you do?"
          menu:
            "Accept her":
              player.c "I accept.  Take off your clothes and get down on the floor."
              wt_image cheater_love_potion_15
              lauren.c "Thank you!  Oh, thank you Master!"
              wt_image cheater_love_potion_22
              "She tries to crawl down to the floor, but the effect of the transformation has left her exhausted."
              wt_image cheater_love_potion_16
              "She falls asleep, managing only to get into an all-fours position before drifting off. When she wakes, you'll have her quit her job and explain to her husband that she's leaving him."
              "Then you'll move her into the bedroom where she'll begin her new life as a cuffed and collared 24/7 house slave. She should find that more satisfying than life as a corporate executive."
              $ lauren.transformed_via_object = True
              call lauren_convert_slavegirl_accept from _call_lauren_convert_slavegirl_accept
            "Reject her":
              player.c "I have no use for a worthless slut like you."
              wt_image cheater_love_potion_18
              lauren.c "Please ... please, I'm begging you. I have no value. I know that.  But I'll be your most grateful slave, if only you'll take pity on me and let me serve you?"
              $ title = "Do you relent?"
              menu:
                "Accept her":
                  player.c "I accept.  Take off your clothes and get down on the floor."
                  wt_image cheater_love_potion_15
                  lauren.c "Thank you!  Oh, thank you Master!"
                  wt_image cheater_love_potion_22
                  "She tries to crawl down to the floor, but the effect of the transformation has left her exhausted."
                  wt_image cheater_love_potion_16
                  "She falls asleep, managing only to get into an all-fours position before drifting off. When she wakes, you'll have her quit her job and explain to her husband that she's leaving him."
                  "Then you'll move her into the bedroom where she'll begin her new life as a cuffed and collared 24/7 house slave. She should find that more satisfying than life as a corporate executive."
                  $ lauren.transformed_via_object = True
                  call lauren_convert_slavegirl_accept from _call_lauren_convert_slavegirl_accept_1
                "Send her away":
                  player.c "Leave.  Go offer yourself to your husband, see if he wants a worthless slut like you for a slave."
                  player.c "Or offer yourself to the first person you meet in the street.  I don't care.  Just get away from me, and don't come back."
                  "She gets up, crying, and flees."
                  $ lauren.transformed_via_object = True
                  call lauren_convert_slavegirl_reject from _call_lauren_convert_slavegirl_reject
        "Nothing (undo)":
          $ lauren.temporary_count = 0
          "Let's pretend that didn't happen.  That's easier than reloading an old save."
    if lauren.temporary_count == 1:
      $ lauren.temporary_count = 0
      $ lauren.training_session()
      call character_location_return(lauren) from _call_character_location_return_485
      rem 1 transformation_potion from player
      change player energy by -energy_long notify
  return

# Will-Tamer Timer
label lauren_will_tamer_timer:
  if lauren.has_tag('transformed'):
    "Lauren has already been transformed.  The Will-Tamer can do nothing more to her now."
  else:
    if lauren.has_tag('will_tamer_this_week'):
      "You've already used the Will-Tamer on Lauren this week.  Let its effects continue to work on her brain for a few days, then you can try using it again next week."
    else:
      if lauren.test('submission', 10):
        $ lauren.temporary_count = 1
        if lauren.will_tamer_count == 0:
          wt_image cheater_collar_3
          "Lauren looks at you sceptically as you collar her.  You can feel the warmth of the Will-Tamer as you snap it in place around her pretty neck."
          lauren.c "Is this really necessary?"
          player.c "No, but I like the way you look in it."
          wt_image cheater_collar_5
          "And, you think, I like what it does when you're in it."
          wt_image cheater_collar_6
          "You don't leave her in it for long.  Just enough for it to start to re-wire her brain.  She fights it, of course.  She's a strong willed woman.  At least for now."
          wt_image cheater_collar_4
          "She also loses.  The changes the Will-Tamer has made will become stronger over the coming week, at which point you could put her in it again."
          if lauren.status == "on_training":
            player.c "Shall we continue your training?"
          else:
            player.c "That's enough for now.  I'll let you wear your collar again later."
          wt_image cheater_collar_7
          "She nods, meekly, as you remove the Will-Tamer."
        elif lauren.will_tamer_count == 1:
          player.c "Time to wear your collar again."
          lauren.c "My collar?"
          wt_image cheater_collar_3
          player.c "Well, that's what I think of it as when you're wearing it."
          if lauren.test('resistance', 40):
            wt_image cheater_collar_7
            lauren.c "It's so strange ... I'm starting to enjoy the way this collar ... my collar ... feels."
            wt_image cheater_collar_9
            "Lauren doesn't so much fight the changes the Will-Tamer makes to her brain this time as accept them, though not without a few tears that suggest some part of her knows it is being lost."
          else:
            wt_image cheater_collar_5
            "She fights the collar again ..."
            wt_image cheater_collar_8
            "... and this time the fight is harder and more intense."
            wt_image cheater_collar_9
            "The outcome, however, is never in doubt."
          wt_image cheater_collar_10
          player.c "You've been allowed to wear your collar long enough for today."
          lauren.c "Thank you!"
          "Whether she's thanking you for taking it off, or having put it on in the first place, isn't immediately clear to you, and possibly not to her either."
        elif lauren.will_tamer_count == 2:
          player.c "Time for you to wear your collar again."
          if lauren.test('resistance', 1):
            wt_image cheater_collar_7
            "Lauren sighs contentedly as you snap the Will-Tamer in place around her neck."
            lauren.c "Thank you for collaring me."
            player.c "Is that how you think you should be addressing me?"
            lauren.c "Thank you for collaring me, Sir."
            wt_image cheater_collar_11
            "Lauren is unable to offer any resistance to the Will-Tamer.  Her eyes glaze over as it continues to re-wire her brain.  One more session, and it will claim her."
          elif lauren.test('resistance', 40):
            wt_image cheater_collar_7
            lauren.c "It's so strange ... I'm starting to enjoy the way this collar ... my collar ... feels."
            wt_image cheater_collar_9
            "Lauren doesn't so much fight the changes the Will-Tamer makes to her brain this time as accept them, though not without a few tears that suggest some part of her knows it is being lost."
            wt_image cheater_collar_10
            player.c "You've been allowed to wear your collar long enough for today."
            lauren.c "Thank you!"
            "Whether she's thanking you for taking it off, or having put it on in the first place, isn't immediately clear to you, and possibly not to her either."
          else:
            wt_image cheater_collar_5
            "She fights the collar again ..."
            wt_image cheater_collar_8
            "... and this time the fight is harder and more intense."
            wt_image cheater_collar_9
            "The outcome, however, is never in doubt."
            player.c "You've been allowed to wear your collar long enough for today."
            wt_image cheater_collar_10
            lauren.c "Thank you!"
            "Whether she's thanking you for taking it off, or having put it on in the first place, isn't immediately clear to you, and possibly not to her either."
        else:
          "The Will-Tamer has re-programmed Lauren's brain to the point that she's ready to undergo a more complete transformation."
          if lauren.status == "on_training":
            "You should wait, however, until you complete her assignment before taking this step.  Otherwise, her husband is too likely to cause trouble."
            $ lauren.temporary_count = 0
          else:
            "If you let the Will-Tamer take its full effect, the Lauren you know now will be lost, permanently."
            "You will also lose the Will-Tamer, which will become absorbed into Lauren's very being."
            $ title = "Use the Will-Tamer on her again?"
            menu:
              "No, not right now":
                $ lauren.temporary_count = 0
              "Yes, collar her again (loses the Will-Tamer)":
                if current_location != living_room:
                  player.c "Come with me."
                  lauren.c "Why?"
                  player.c "It's time for you to wear your collar again."
                  call forced_movement(living_room) from _call_forced_movement_162
                if lauren.test('resistance', 1):
                  wt_image cheater_collar_7
                  "Lauren sighs contentedly as you snap the Will-Tamer in place around her neck."
                  lauren.c "Thank you for collaring me."
                  player.c "Is that how you think you should be addressing me?"
                  lauren.c "Thank you for collaring me, Sir."
                  wt_image cheater_collar_11
                  "Lauren is unable to offer any resistance to the Will-Tamer. Her eyes glaze over as it completes the re-wiring of her brain."
                  $ lauren.temporary_count = 2
                  $ title = "What do you instruct the Will-Tamer to transform Lauren into?"
                  menu:
                    "Slavegirl" if not lauren.has_tag('slavegirl') and lauren.punishment_count > 1 and lauren.submission > 20:
                      "Lauren has always appreciated strong men who know what they want. If she wasn't attracted to that dynamic, she would never have accepted her husband's insistence on becoming his slut, nor would she have accepted your training. Under your training, she's experienced sessions of intense domination and learned to accept the feeling of submitting to the will of another."
                      "The Will-Tamer latches on to that feeling and augments it, until in her mind Lauren doesn't just accept being dominated, she craves it. She can't imagine a life in which she isn't ordered around and forced to cater to the whim of her Owner."
                      wt_image cheater_kneel_3
                      "As the Will-Tamer completes her transformation and is absorbed into her, she pulls off her clothes and drops to her knees in front of you."
                      wt_image cheater_kneel_4
                      lauren.c "May ... may this worthless slut please have permission to speak?"
                      player.c "Go ahead."
                      wt_image cheater_kneel_2
                      lauren.c "Would you accept ownership of this worthless slut? I have nothing to offer you except my body, but you may have my body, to do with whatever you please.  I promise I'll be obedient and faithful and grateful for the opportunity to serve you in any way you command of me."
                      $ title = "What do you do?"
                      menu:
                        "Accept her":
                          player.c "I accept.  Crawl to the bedroom."
                          wt_image cheater_kneel_5
                          lauren.c "Thank you!  Oh, thank you Sir!"
                          player.c "Shut your mouth.  You will never speak again unless I give you permission."
                          wt_image cheater_kneel_6
                          "She nods and scampers towards the bedroom."
                          wt_image cheater_kneel_7
                          player.c "Wait. Get your phone, first, and call your husband. Tell him you're leaving him. Then call your office and let them know you quit. That'll be your last contact with the outside world."
                          wt_image cheater_kneel_5
                          "She grins and crawls off, eager to begin her life as a 24/7 slave. She should find that more satisfying than life as a corporate executive."
                          $ lauren.transformed_via_object = True
                          call lauren_convert_slavegirl_accept from _call_lauren_convert_slavegirl_accept_2
                        "Reject her":
                          player.c "I have no use for a worthless slut like you."
                          wt_image cheater_kneel_4
                          lauren.c "Please ... please, I'm begging you. I have no value. I know that.  But I'll be your most grateful slave, if only you'll take pity on me and let me serve you?"
                          $ title = "Do you relent?"
                          menu:
                            "Accept her":
                              player.c "I accept.  Crawl to the bedroom."
                              wt_image cheater_kneel_5
                              lauren.c "Thank you!  Oh, thank you Sir!"
                              player.c "Shut your mouth.  You will never speak again unless I give you permission."
                              wt_image cheater_kneel_6
                              "She nods and scampers towards the bedroom."
                              wt_image cheater_kneel_7
                              player.c "Wait. Get your phone, first, and call your husband. Tell him you're leaving him. Then call your office and let them know you quit.  That'll be your last contact with the outside world."
                              wt_image cheater_kneel_5
                              "She grins and crawls off, eager to begin her life as a 24/7 slave. She should find that more satisfying than life as a corporate executive."
                              $ lauren.transformed_via_object = True
                              call lauren_convert_slavegirl_accept from _call_lauren_convert_slavegirl_accept_3
                            "Send her away":
                              player.c "Leave.  Go offer yourself to your husband, see if he wants a worthless slut like you for a slave."
                              player.c "Or offer yourself to the first person you meet in the street.  I don't care.  Just get away from me, and don't come back."
                              "She gets up, crying, and flees."
                              $ lauren.transformed_via_object = True
                              call lauren_convert_slavegirl_reject from _call_lauren_convert_slavegirl_reject_1
                    "Petgirl":
                      "Since she was caught cheating, Lauren has often felt like a trapped animal.  Unwilling to suffer the consequences of divorce, she's been forced to submit to her husband's demands and your training. Being forced to wear a collar brought those feelings of being treated like a captured animal to the fore."
                      "The Will-Tamer latches on to those feelings and augments them, until in her mind Lauren no longer feels like a trapped animal, she is a trapped animal. Captured by humans and subjected to their rules and training, but no longer one of them."
                      $ lauren.transformed_via_object = True
                      call lauren_convert_petgirl from _call_lauren_convert_petgirl
                    "Nothing (undo)":
                      $ lauren.temporary_count = 0
                      "Let's just pretend that didn't happen.  That's easier than reloading an old save."
                  if lauren.temporary_count == 2:
                    $ lauren.training_session()
                    $ lauren.cheated = 3
                    rem 1 will_tamer from player
                else:
                  wt_image cheater_collar_7
                  lauren.c "It's so strange ... I'm starting to enjoy the way this collar ... my collar ... feels."
                  wt_image cheater_collar_9
                  "Lauren doesn't so much fight the changes the Will-Tamer makes to her brain this time as accept them, though not without a few tears that suggest some part of her knows it is being lost."
                  player.c "You've been allowed to wear your collar long enough for today."
                  wt_image cheater_collar_10
                  lauren.c "Thank you!"
                  "Whether she's thanking you for taking it off, or having put it on in the first place, isn't immediately clear to you, and possibly not to her either. The Will-Tamer didn't claim her this time, but once her Resistance is low enough, it will."
        if lauren.temporary_count == 1:
          $ lauren.temporary_count = 0
          $ lauren.will_tamer_count += 1
          change lauren submission by 10
          change lauren resistance by -15 notify
          add tags 'will_tamer_this_week' to lauren
      else:
        lauren.c "A collar?  Really?  I'm not about to act like your slavegirl or whatever it is you're thinking."
        "You need to wait until she's more submissive to you."
  return

# Convert Character to Bimbo
label lauren_convert_bimbo:
  lauren.c "Should I be sucking your cock now?"
  wt_image cheater_blow_job_21
  "You nod, and she drops to her knees and happily starts slurping on your dick, her big eyes locked on yours. As she sucks you, you need to decide what to do with her. She's not actually doing a good job. Either she's now too stupid to give head properly, or she's simply forgotten and you'll need to teach her."
  $ title = "What should you do with her?"
  menu:
    "Keep her":
      "Lauren's not going to be much use to you in her new, airhead state. She won't be able to keep her current profession, and there isn't anything in the way of paying work she could do.  Even if you try to pimp her out, she's not likely to remember to take the men's money."
      "On the other hand, she's kind of cute, and as long as she's around, you'll always have someone to suck your cock while you're watching TV, eating supper, or falling to sleep. She can't keep up a conversation, but if her mouth is filled that doesn't matter much."
      player.c "You understand that when my cock spurts in your mouth, you swallow it all, right?"
      "She nods."
      wt_image cheater_blow_job_1
      player.c "[player.orgasm_text]"
      "When you've released your load into her waiting mouth, you take her into your bedroom and let her rest.  She's had a difficult day, but all her future days will be much simpler."
      "Tomorrow you'll type out a message for her to send to her husband, explaining that she can't accept her new role, so go ahead and divorce her, she's leaving him anyways. She won't understand what you're written for her, but it won't matter.  She's dependent on you now for food, shelter, and if you decide to give her any, clothes."
      if lauren.has_tag('whore'):
        "In her new, ditzy state, Lauren never remembers to collect money from men for sex.  Her career as a working girl is over."
        call unconvert(lauren, 'whore') from _call_unconvert_58
      if lauren.has_tag('showgirl'):
        "In her new, ditzy state, Lauren never remembers when she's supposed to be dancing at The Club.  Her career as a showgirl is over."
        call unconvert(lauren, 'showgirl') from _call_unconvert_59
      $ lauren.training_regime = 'daily'
      call convert(lauren,"bimbo") from _call_convert_86
      $ lauren.prefix = ""
      $ lauren.suffix = "the Bimbo"
      $ lauren.fixed_location = bedroom
      $ lauren.location = bedroom
      rem tags 'follows' from lauren
    "Send her to her husband":
      "Lauren's not going to be much use to you in her new, airhead state. She won't be able to keep her current profession, and there isn't anything in the way of paying work she could do. Even if you try to pimp her out, she's not likely to remember to take the men's money."
      player.c "You're too stupid to be of use to me, bimbo, so I'm not going to be able to keep you. I'm going to send you home to your husband instead."
      player.c "Would you like me to shoot a load of sperm down your throat before I send you back to your husband?"
      "She nods."
      wt_image cheater_blow_job_1
      player.c "[player.orgasm_text]"
      "When you've released your load into her waiting mouth, you explain that she belongs to her husband, and needs to go home and make him happy."
      wt_image cheater_house_1
      "When it's clear she doesn't remember the way home, you drop her off on her street and point out her house."
      "You're not sure what her husband will do with her, but he was the one who wanted a proper little slut.  Now he has one, more mindlessly obedient than he could ever have dreamed. Whether life with her now will be a dream or a nightmare will depend on how he likes seeing his intelligent, independent wife in her new docile state."
      "You assume he knows that you must be involved in this latest change, but he never messages you to ask, so you never find out how much he likes this last stage in her training."
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      call convert(lauren, "unavailable") from _call_convert_87
  $ lauren.change_image('cheater_bimbo_portrait')
  add tags 'post_continuing_actions' to lauren
  rem tags 'follows' 'continuing_actions' 'waiting_for_club_access' from lauren
  $ lauren.cheated = 3
  orgasm
  return

# Convert Character to petgirl
label lauren_convert_petgirl:
  wt_image cheater_cage_6
  "As Lauren reverts to a feral animal state, you lead her into a cage.  She looks back at you warily as you lock the door behind her."
  "You move her into your room.  You'll need to keep her locked up until she's domesticated."
  if lauren.has_tag('whore'):
    call unconvert(lauren, 'whore') from _call_unconvert_60
  if lauren.has_tag('showgirl'):
    call unconvert(lauren, 'showgirl') from _call_unconvert_61
  $ lauren.training_regime = 'daily'
  call convert(lauren, "petgirl") from _call_convert_88
  $ lauren.prefix = ""
  $ lauren.suffix = "the Puppygirl"
  $ lauren.fixed_location = bedroom
  $ lauren.location = bedroom
  add tags 'post_continuing_actions' to lauren
  rem tags 'follows' 'continuing_actions' 'waiting_for_club_access' from lauren
  $ lauren.cheated = 3
  return

# Convert Character to Showgirl
label lauren_convert_showgirl:
  $ lauren.training_regime = 'daily'
  call convert(lauren, "showgirl") from _call_convert_89
  $ lauren.prefix = ""
  $ lauren.suffix = "the Showgirl"
  rem tags 'waiting_for_club_access' from lauren
  return

# Convert Character to Slavegirl
label lauren_convert_slavegirl_accept:
  if lauren.has_tag('whore'):
    "In her new, obedient state, it's not safe to send Lauren out to turn tricks for you.  She may accept any instructions she's given, no matter how dangerous they may be to her."
    call unconvert(lauren, 'whore') from _call_unconvert_69
  if lauren.has_tag('showgirl'):
    "In her new, obedient state, you can't trust Lauren to continue dancing at The Club.  She may wander off with the first person who claims to be her new Master or Mistress."
    call unconvert(lauren, 'showgirl') from _call_unconvert_70
  $ lauren.training_regime = 'daily'
  call convert(lauren, "slavegirl") from _call_convert_90
  $ lauren.prefix = "Slave"
  $ lauren.suffix = ""
  $ lauren.fixed_location = bedroom
  $ lauren.location = bedroom
  add tags 'post_continuing_actions' to lauren
  rem tags 'follows' 'continuing_actions' 'waiting_for_club_access' from lauren
  $ lauren.cheated = 3
  return

label lauren_convert_slavegirl_reject:
    # if lauren.has_tag('whore'):  ## none of this is needed as handled by convert(unavailable)
    #     call unconvert(lauren, 'whore')
    # if lauren.has_tag('showgirl'):
    #     call unconvert(lauren, 'showgirl')
    # $ lauren.cheated = 3
    # rem tags 'waiting_for_club_access' from lauren
    call convert(lauren, "unavailable") from _call_convert_91
    return

# Convert Character to Whore
label lauren_convert_whore:
  $ lauren.training_regime = 'weekly'
  call convert(lauren, "whore") from _call_convert_92
  $ lauren.prefix = ""
  $ lauren.suffix = "the Whore"
  return

########### ROOMS ###########
# Lauren's Office Action on Elevator Button
label lauren_office_visit:
    call move_to(lauren_office) from _call_move_to_4
    return

# Lauren's Office - Examine
label lco_examine:
  "A tasteful and somewhat artsy reception area."
  return

# Lauren's Office - Prevent Access
label lco_no_access:
    if lauren.status == "on_training" and lauren.has_tag('trained_this_week'):
        "You had a session with [lauren.name] earlier this week.  You'll need to wait until the weekend or next week for another session."
        break_movement
    elif lauren.has_any_tag('transformed','humiliated_in_office') or lauren.status == 'unavailable':
        "[lauren.full_name] doesn't work here anymore."
        break_movement
    elif lauren.status == "post_training" and not lauren.has_tag('continuing_actions'):
        "Lauren will not see you any more."
        break_movement
    elif lauren.status == "post_training" and lauren.has_tag('continuing_actions') and not lauren.can_be_interacted:
        "You already saw Lauren earlier this week.  Wait until next week to visit her at her office."
        break_movement
    return

# Lauren's Office - Enter
label lco_enter:
    if sophie.location == lauren_office:
        add tags 'no_hypnosis' to sophie
    if sophie.relationship_status == 3 and sophie.location == lauren_office:
        call sophie_upset_no_call from _call_sophie_upset_no_call
    elif sophie.relationship_status == 4 and sophie.location == lauren_office:
        call sophie_post_date_office_events from _call_sophie_post_date_office_events
    return

# Lauren's Office - Exit
label lco_exit:
  return

## changed to standard club coding
# label lauren_stage_events:
#   if lauren.has_tag('waiting_for_club_access') and not lauren.has_tag('stage_message_given'):
#     add tags 'stage_message_given' to lauren
#     "This might be the right venue for Lauren to start showing off her attributes."
#   return

################################### NOTES ###################################
##################### TODO #####################
# complete conditional o weekend to ensure can't hypno twice in the same week

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
