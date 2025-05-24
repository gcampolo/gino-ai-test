## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Blank Subroutine, Blubblegum, and wifetrainer

# Package Register
#register_package jasmine name "Jasmine, The Exhibitionist" description "Allows Jasmine to be a client." dependencies core
register jasmine_pregame 10 in core as "Jasmine the Exhibitionist"

# Pregame
label jasmine_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Jasmine the Exhibitionist (Lacey Duvalle)")]

    ## Character Definition
    jasmine = Person(Character("Jasmine", who_color="#FF8000", what_color="#FF8000", window_background=gui.dialogue_background_medium_font_color), "jasmine", cut_portrait = True, prefix = "", suffix = "the Exhibitionist", resistance = 70, training_period = 14, min_reputation = 0, hypno_trigger_resistance_threshold = 5)

    # Other Characters
    # Navy
    husband_jasmine = Character("Jasmine's Husband", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)
    # Navy
    coworker_rob = Character("Rob", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)
    # Navy
    john_1_jasmine = Character("John", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)
    # Pink
    passerby_in_club_jasmine_1 = Character("Club Member", who_color="#FF0080", what_color="#FF0080")
    # Green
    coworker_unnamed_jasmine = Character("Co-worker", who_color="#00bb00", what_color="#00bb00")

    ## Actions
    jasmine.action_prepwork = None
    # Add Hypno Actions
    jasmine.action_barebreast_hypno = jasmine.add_action( "Wake her up with her breasts still out", label = "_bare_breasts_hypnosis", context = "_hypnosis", condition = "jasmine.privateshow_count == 0" )
    jasmine.action_barepussy_hypno = jasmine.add_action( "Have her show her pussy", label = "_bare_pussy_hypnosis", context = "_hypnosis", condition = "jasmine.privateshow_count == 1 and not jasmine.has_tag('bare_pussy')" )
    jasmine.action_barepussy_wake_hypno = jasmine.add_action( "Wake her up with her pussy still out", label = "_bare_pussy_wake_hypnosis", context = "_hypnosis", condition = "jasmine.privateshow_count == 1 and jasmine.has_tag('bare_pussy')" )
    jasmine.action_bj_hypno = jasmine.add_action( "Have her blow you", label = "_blowjob_hypnosis", context = "_hypnosis", condition = "jasmine.privateshow_count >= 2 and not jasmine.has_tag('hypno_bj_attempted_today') and jasmine.status == 'on_training'" )
    # Training actions
    jasmine.action_talk = jasmine.add_action( "Talk to her", label = '_talk', condition = "jasmine.can_be_interacted and jasmine.has_tag('first_visit') and jasmine.status == 'on_training' and jasmine.in_area('house')" )
    jasmine.action_prepwork = jasmine.add_action("Prep work", label = '_prepwork', condition = "jasmine.can_be_interacted and not jasmine.has_tag('first_visit') and jasmine.status == 'on_training' and jasmine.prepwork_count < 2 and jasmine.in_area('house')" )
    jasmine.action_publicshow = jasmine.add_action("Public show", label = '_publicshow', condition = "jasmine.can_be_interacted and not jasmine.has_tag('first_visit') and jasmine.status == 'on_training' and jasmine.in_area('house')")
    jasmine.action_officeshow = jasmine.add_action("Office show", label = '_officeshow', condition = "jasmine.can_be_interacted and not jasmine.has_any_tag('first_visit', 'shut_off_officeshow') and jasmine.status == 'on_training' and jasmine.in_area('house')")
    jasmine.action_privateshow = jasmine.add_action("Private show", label = '_privateshow', condition = "jasmine.can_be_interacted and not jasmine.has_tag('first_visit') and jasmine.status == 'on_training' and jasmine.in_area('house')")
    jasmine.action_end_session = jasmine.add_action("Send her home", label = "_end_session", condition = "not jasmine.has_any_tag('first_visit', 'shut_off_end_session') and jasmine.in_area('house')")
    # Continuing actions
    jasmine.action_watch_her_dance = jasmine.add_action("Watch her dance", label = '_watch_her_dance', condition = "jasmine.can_be_interacted and jasmine.status == 'post_training'")
    # note: private show seems no longer to be needed as Watch Her Dance covers this off now
    #jasmine.action_contact_visit_privateshow = jasmine.add_action("Private Show", label = '_contact_visit_privateshow', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_lingerieshow = jasmine.add_action("Lingerie show", label = '_contact_visit_lingerieshow', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_dildoshow = jasmine.add_action("Dildo show", label = '_contact_visit_dildoshow', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_blowjob = jasmine.add_action("Blow job", label = '_contact_visit_blowjob', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_footjob = jasmine.add_action("Foot job", label = '_contact_visit_footjob', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_titfuck = jasmine.add_action("Tit job", label = '_contact_visit_titfuck', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_sex = jasmine.add_action("Sex", label = '_contact_visit_sex', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and current_location == living_room")
    jasmine.action_contact_visit_girlfriend = jasmine.add_action("Ask her to be your girlfriend", label = '_contact_visit_girlfriend', condition = "jasmine.can_be_interacted and jasmine.has_tag('continuing_actions') and not jasmine.has_tag( 'gf_asked_today' ) and not jasmine.has_tag('girlfriend') and current_location == living_room")
    # Post-continuing actions
    jasmine.action_girlfriend = jasmine.add_action("Girlfriend Actions", label = '_gf_actions', condition = "jasmine.can_be_interacted and jasmine.has_tag('post_continuing_actions') and jasmine.has_tag('girlfriend') and bedroom.is_here")
    jasmine.action_dildo_show = jasmine.add_action("Dildo Show", label = '_dildoshow', condition = "jasmine.can_be_interacted and jasmine.has_tag('post_continuing_actions') and jasmine.has_item(dildo) and bedroom.is_here")
    jasmine.action_street_walking_roleplay = jasmine.add_action("Roleplay Street Walking", label = '_street_walking_roleplay', condition = "jasmine.can_be_interacted and jasmine.has_tag('girlfriend') and jasmine.has_tag('whore_roleplaying')") # note this action doesn't need to be limited by location as can be triggered from home or stage
    jasmine.action_check_bimbo = jasmine.add_action("Check on your bimbo", label = "_bimbo_actions", condition = "jasmine.can_be_interacted and jasmine.has_tag('bimbo') and bedroom.is_here")
    jasmine.relationship_action = bedroom.add_action("[jasmine.full_name]", label = jasmine.short_name + "_relationship_status", context = "_relationship_status", condition = "jasmine.has_tag('girlfriend') or jasmine.has_tag('continuing_actions')")


    ## Tags
    # Common Character Tags
    jasmine.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    dungeon.enter_break_labels.append('du_no_access_jasmine')
    downtown.enter_labels.append('jasmine_downtown_events')

    ## Other
    jasmine.change_status("available_to_be_client")
    nipple_rings_jasmine = Item('Nipple Rings', 'nrj', with_examine = True, with_give = True)

    # Start Day Events
    start_day_labels.append('jasmine_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    jasmine.add_stats_with_value('hypno_blowjob_count', 'hypno_swallow_count', 'random_number')

    # Character Specific Variables
    jasmine.add_stats_with_value('handjob_given', 'officeshow_count', 'officeshow_tempcount', 'prepwork_count', 'privateshow_count', 'privateshow_energy', 'publicshow_count', 'publicshow_level')
    #jasmine.add_stats_with_value( 'stripper_discussion' )    # 0: No discussion yet  1: Question asked, no club access  2: Refused  3: Agreed
    #jasmine.add_stats_with_value( 'gf_conversion_status' )         # Progress in converting Jasmine into a girlfriend.
    jasmine.add_stats_with_value( 'club_whore_event_week' ) # Different than RAGS name due to use in club.rpy
    jasmine.add_stats_with_value('lingerie_outfit_count',value=1)

    jasmine.add_stats_with_value('bimbo_outfit_count', 'bimbo_strip_count', 'club_sex_status', 'dildo_show_count', 'downtown_countdown', 'downtown_event_checked_today', 'downtown_flash_outfit', 'downtown_follow_count', 'downtown_outfit', 'downtown_sex', 'downtown_week', 'gf_conversion_status', 'gf_outfit_count', 'lingerie_show_status', 'maintain_week_gf', 'od_set_count', 'photod_in_public_week_for_event', 'private_expose_level')
    jasmine.add_stats_with_value('relationship_event', 'relationship_week', 'road_trip_count', 'sex_level', 'strip_outfit_count', 'stripper_discussion', 'whore_lost_countdown', 'whore_outfit', 'whore_play_status')

    # Others
    bedroom.enter_labels.append('jasmine_bedroom_enter')
    bedroom.exit_labels.append('jasmine_bedroom_exit')

    ######## EXPANDABLE MENUS #######
    ## Weekend Training
    jasmine_weekend_training_menu = ExpandableMenu("What do you want to do with [jasmine.name] this weekend?", pre_label = 'jasmine_pre_weekend', post_label = 'jasmine_post_weekend')
    # note: these don't have to be defined in pregame, can be added in game
    jasmine.choice_weekend_hypnotize =  jasmine_weekend_training_menu.add_choice("Hypnotize her", "jasmine_weekend_hypno", condition = "player.can_hypno(jasmine)")
    jasmine.choice_weekend_roadtrip =  jasmine_weekend_training_menu.add_choice("Road trip", "jasmine_weekend_roadtrip")

  return

# Initial Contact Message
# OBJECT: Check Messages
label jasmine_message:
  husband_jasmine "{i}Hey, do you think you could help my wife, [jasmine.name]? She's obsessed with the idea of exposing herself in public."
  husband_jasmine "{i}I've tried to support her. I've taken her out and gave her chances to flash people. She always chickened out. But she won't let it go. Keeps bringing it up, about how exciting it would be, how she wants to be able to do it."
  husband_jasmine "{i}Let me know if you can help. No funny business, though. If you can get her to flash her titties in public, great. But looking is as far as you can go.{/i}"
  call consider_contract(jasmine, "Reply to [jasmine.full_name]'s Husband") from _call_consider_contract_2
  if yesno == True:
    sys "You accept the assignment.  You have until the end of week [jasmine.training_limit] to complete it."
    if not player.has_tag('tutorial_message'):
      add tags 'tutorial_message' to player
      sys "You may hold one evening session each week to complete her training.  If you have at least [energy_long.value] Energy left on Friday, you may also schedule a weekend session with a client of your choice."
  return

# Client Rejected
label jasmine_rejected:
  sys "You can no longer train [jasmine.full_name]."
  return

# Arrange Client Session
# OBJECT: Schedule Client Session
label jasmine_calling:
  # Check if client has already been trained this week
  if not jasmine.can_be_interacted:
    "You had an evening session with [jasmine.name] earlier this week.  You need to wait until the weekend or next week for another session."
  else:
    call forced_movement(living_room) from _call_forced_movement_52
    summon jasmine
    $ jasmine.visit_count += 1
    wt_image exhi_leaving
    "You show [jasmine.name] in."
    wt_image exhi_portrait_1
    if 'first_visit' in jasmine.tags:
      player.c "Please have a seat."
      if not player.has_tag('first_client_visit_message'):
        add tags 'first_client_visit_message' to player
        sys "[player.first_client_visit_message_text]"
  return

# Display Portrait
# CHARACTER: Display Portrait
label jasmine_update_media:
    if jasmine.status == "on_training":
        $ jasmine.change_image( 'exhi_portrait_1' )
    else:
        if jasmine.has_tag('holding_position'):
            pass
        elif jasmine.has_tag('bimbo'):
            $ jasmine.change_image( 'exhi_bimbo_portrait' )
        elif jasmine.has_tag( 'showgirl' ) and current_location == stage:
            if jasmine.has_tag('watched_today'):
                # note the numbers here are offset by one so that examine shows outfit she will dance in next
                if jasmine.strip_outfit_count == 1:
                    $ jasmine.change_image( 'exhi_strip_1_1' )
                elif jasmine.strip_outfit_count == 2:
                    if jasmine.dildo_show_count > 1:
                        $ jasmine.change_image( 'exhi_strip_6_1' )
                    else:
                        $ jasmine.change_image( 'exhi_strip_3_1' )
                elif jasmine.strip_outfit_count == 3:
                    $ jasmine.change_image( 'exhi_strip_2_6' )
                elif jasmine.strip_outfit_count == 4:
                    $ jasmine.change_image( 'exhi_strip_4_1' )
                else:
                    $ jasmine.change_image( 'exhi_strip_5_1' )
            else:
                # note the numbers here are offset by one so that examine shows outfit she will dance in next
                if jasmine.strip_outfit_count == 1:
                    if jasmine.dildo_show_count > 1:
                        $ jasmine.change_image( 'exhi_strip_6_1' )
                    else:
                        $ jasmine.change_image( 'exhi_strip_3_1' )
                elif jasmine.strip_outfit_count == 2:
                    $ jasmine.change_image( 'exhi_strip_2_6' )
                elif jasmine.strip_outfit_count == 3:
                    $ jasmine.change_image( 'exhi_strip_4_1' )
                elif jasmine.strip_outfit_count == 4:
                    $ jasmine.change_image( 'exhi_strip_5_1' )
                else:
                    $ jasmine.change_image( 'exhi_strip_1_1' )
        elif jasmine.has_tag('girlfriend'):
            $ jasmine.change_image( 'exhi_gf_portrait' )
        elif jasmine.has_tag('whore'):
            $ jasmine.change_image( 'exhi_whore_4_1' )
        else:
            $ jasmine.change_image( 'exhi_portrait_2' )
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label jasmine_examine:
    # Holding Position Examine
    if jasmine.has_tag('holding_position'):
        "[jasmine.name]'s still where you left her earlier."
        jasmine.c "Is it still today?"
        player.c "Yes, it usually is."
        jasmine.c "Will you tell me when it's no longer today?"
        player.c "Okay"
    else:
        call jasmine_description_display from _call_jasmine_description_display
    return

# Talk to Character
label jasmine_talk:
  if 'first_visit' in jasmine.tags:
    wt_image exhi_portrait_1
    player.c  "I'm sure this is all quite new to you, [jasmine.name].  Tell me, how were you feeling, coming over here tonight?"
    jasmine.c "I don't know.  Uncertain, for sure.  I'm not sure exactly how this will work."
    player.c  "What do you mean by \"this\"?"
    jasmine.c "Me, taking my clothes off in public.  You helping me not be scared about doing so."
    player.c  "What do you think about, [jasmine.name], when you think about exposing yourself to strangers?  What is it that appeals to you about that?"
    jasmine.c "I don't know. The excitement of it, I guess. Being naughty. Doing something I shouldn't. It's kind of humiliating, the idea of being naked when other people aren't. But also empowering, because I chose to be naked."
    wt_image exhi_hypno_1
    "She pauses and shifts a bit before continuing."
    jasmine.c "Men like my body. Especially my tits. I like the idea of turning men on by showing my tits off. Especially when it's not safe. Especially if I may get caught by someone I know."
    wt_image exhi_portrait_1
    "She shifts in her seat again."
    jasmine.c "I don't want to put myself in danger. I don't want one of my friends or co-workers to catch me naked. But I love the idea that maybe they could. Pretty messed up, huh?"
    $ title = "How do you respond?"
    menu:
        "A bit yeah.  I guess that's why you need me.":
          player.c  "Yes, it is a bit messed up.  I guess that's why you need me."
          wt_image exhi_hypno_submission_8
          player.c  "It sounds like you're stuck wanting something, but you're not willing to take the actions you need to get it."
          player.c  "Do you want to know what that feels like, [jasmine.name], to expose yourself in public to strangers, or do you want to spend the rest of your life wondering about it?"
          jasmine.c "I want to know."
          player.c  "Good. Then what I expect is that you'll follow my instructions. If you don't want to spend the rest of your life stuck where you are now, trapped between obsession and inaction, then you'll do as I say."
          player.c "You'll take my lead, and I'll help you get over your fear, and let you have this experience that you've been fantasizing about for so long."
          change jasmine submission by 5
          change jasmine resistance by -10
        "Not really. Pretty normal compared to some clients.":
          player.c  "Not really.  Pretty normal compared to some of the clients I work with."
          wt_image exhi_hypno_submission_6
          player.c  "You're captivated by the fantasy, but you're smart enough to know that real life isn't fantasy."
          player.c "It's one thing to masturbate to the idea of a coworker catching you naked in the office, it's something else entirely to lose your reputation or your job because a coworker caught you naked in the office."
          "[jasmine.name] nods."
          player.c  "Let me work with you, and I'll do my best to keep you safe and to realize some of that fantasy.  Regardless of what we do, however, there are going to be risks."
          jasmine.c "I know. I accept that.  I'm ready to take some risk, to make this happen.  Thank you for being so understanding."
          change jasmine desire by 5
          change jasmine sos by 5
    notify
    rem tags 'first_visit' 'no_hypnosis' from jasmine
    $ jasmine.add_hypno_actions(implant = False) # this adds hypnosis_context actions for all stats associated with jasmine
  return

# Hypno Actions
label jasmine_hypnosis_start:
    $ jasmine.temporary_count = 1
    if jasmine.status == "on_training":
        if jasmine.has_tag( 'hypno_weekend' ): # note: I could have just used is_weekend() for the test instead of the 'hypno_weekend' tag, might have been cleaner
            summon jasmine
            wt_image exhi_weekend_hypno_1
            "When [jasmine.name] arrives, you bring her into your living room."
        else:
            wt_image jasmine.image
    else:
        if jasmine.has_tag('bimbo'):
            add tags 'no_hypnosis' to jasmine
            "There's not much point in trying to hypnotize an airhead."
            # this command breaks the hypnosis routine
            $ ignore_context_change = True
            $ jasmine.temporary_count = 0
        elif current_location != bedroom and current_location != living_room:
            "Wait until you're together at your home."
            # this command breaks the hypnosis routine
            $ ignore_context_change = True
            $ jasmine.temporary_count = 0
        if not jasmine.can_be_interacted:
            "You have already had fun with Jasmine today."
            # this command breaks the hypnosis routine
            $ ignore_context_change = True
            $ jasmine.temporary_count = 0
        else:
            wt_image exhi_weekend_hypno_1
    if jasmine.temporary_count == 1:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        $ jasmine.temporary_count = 0
        player.c "[jasmine.name], I want you to look at something for me."
        call focus_image from _call_focus_image_28
        player.c  "I'm going to talk with you, and you are going to listen to me. Listen to me now, [jasmine.name]. Listen to me. Listen to my voice and nothing else, [jasmine.name]. Only my voice. Only my voice now."
        if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
            wt_image exhi_hypno_1
        else:
            wt_image exhi_weekend_hypno_2
        "She soon falls under your trance."
        player.c "[jasmine.name], I want you to get comfortable for our talk.  Show me your breasts, [jasmine.name]."
        if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
            wt_image exhi_hypno_bare_breasts_1
        else:
            wt_image exhi_weekend_hypno_3
        if jasmine.hypno_count == 0:
            "As a budding exhibitionist, you're not surprised to see [jasmine.name] leap at the opportunity to expose herself under hypnosis."
        # system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    return

# Submission
label jasmine_submission_hypnosis:
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_submission_1
    else:
        wt_image exhi_weekend_hypno_5
    if jasmine.status == 'on_training':
        "You work on [jasmine.name]'s submission. If you can increase her willingness to follow your instructions, it may be easier to get her to act out her fantasies."
    else:
        "You work on [jasmine.name]'s submission to you."
    # system now applies the Submission gain and then goes on to the _submission_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label jasmine_submission_hypnosis_end:
    if not jasmine.has_tag('girlfriend'):
        # note: the below could have been done with the 'test' function
        if jasmine.modified_stat( 'submission' ) < 20:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_leaving
            else:
                wt_image exhi_leaving_2
            "When you've taken her as far as you can for today, you have her dress, then send her home. She doesn't exactly remember what the two of you did, but her respect for you is higher, not that you could tell from the look she gives you as she leaves."
        elif jasmine.modified_stat( 'submission' ) < 35:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_2
            else:
                wt_image exhi_dildo_1_18
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but her respect for you is higher."
            "She smiles at you and looks like she's about to say something, then thinks better of it and leaves."
        elif jasmine.modified_stat( 'submission' ) < 55:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_5
            else:
                wt_image exhi_weekend_hypno_13
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but her respect for you is higher."
            "She keeps her head lowered and looks like she wants to say something, then thinks better of it and leaves."
        elif jasmine.modified_stat( 'submission' ) < 70:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_6
            else:
                wt_image exhi_weekend_hypno_13
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but her respect for you is higher."
            "She keeps her head lowered and looks like she wants to say something.  Eventually she blurts it out."
            jasmine.c "Thank you for spending time with me."
        else:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_6
            else:
                wt_image exhi_weekend_hypno_13
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but her respect for you is higher."
            "She lowers her head and addresses you shyly."
            jasmine.c "Thank you for spending time with me.  Do I have permission to go now?"
            player.c "Not yet.  Sit there and look pretty for a while."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_5
            else:
                wt_image exhi_weekend_hypno_14
            "She sits quietly as you go about your business."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_7
                "Before long, her sweater has fallen down off her shoulders and her dress has ridden up, revealing her panties."
            else:
                wt_image exhi_weekend_hypno_15
                "Before long, her skirt has ridden up, revealing her panties."
            player.c "Not like that.  This isn't about you getting to expose yourself.  I want you to sit pretty for me like a respectable woman."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_8
                "She covers herself up and waits while you go about your day, seemingly ignoring her."
            else:
                wt_image exhi_weekend_hypno_16
                "She pulls her skirt back down and waits while you go about your day, seemingly ignoring her."
            "Eventually you address her."
            player.c "Good girl.  You can go now."
            jasmine.c "Thank you."
            "She disappears, feeling somewhat conflicted, uncertain as to whether she's happy to be let go, or disappointed that you didn't want something more from her."
            change jasmine resistance by -5 notify
    return

# Desire
label jasmine_desire_hypnosis:
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_desire_1
    else:
        wt_image exhi_weekend_hypno_6
    if jasmine.status == 'on_training':
        "You work on [jasmine.name]'s desire. If you can increase her sexual excitement, it may be easier to get her to act out her fantasies."
    else:
        "You work on [jasmine.name]'s desire for you."
    # system now applies the Desire gain and then goes on to the _desire_hypnisis_end label, if there is one, or else to _implant_trigger if there is one
    return

label jasmine_desire_hypnosis_end:
    if not jasmine.has_tag('girlfriend'):
        # note: the below could have been done with the 'test' function
        if jasmine.modified_stat( 'desire' ) < 25:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_leaving
            else:
                wt_image exhi_leaving_2
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she enjoyed your chat."
            "She doesn't, however, show any interest in you as she's leaving."
        elif jasmine.modified_stat( 'desire' ) < 50:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_2
            else:
                wt_image exhi_dildo_1_18
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she enjoyed your chat."
            "She smiles at you and looks like she's about to say something, then thinks better of it and leaves."
        elif jasmine.modified_stat( 'desire' ) < 75:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_2
            else:
                wt_image exhi_dildo_1_18
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she enjoyed your chat."
            "[jasmine.name] smiles at you as she's leaving."
            jasmine.c "I like spending time with you."
        elif jasmine.modified_stat( 'desire' ) < 100:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_2
            else:
                wt_image exhi_dildo_1_18
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she enjoyed your chat."
            "[jasmine.name] beams at you."
            jasmine.c "I really like you, you know?"
            "She escapes before you can reply."
        else:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_3
            else:
                wt_image exhi_weekend_hypno_12
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she enjoyed your chat."
            "[jasmine.name] gives you a seductive look as she's leaving."
            jasmine.c "I shouldn't say this, but I find you really hot."
            change jasmine resistance by -5 notify
    return

# Sense of Self
label jasmine_sos_hypnosis:
  "[jasmine.name]'s sense of self is currently completely tied up in her obsession about experiencing the thrill and danger of being an exhibitionist."
  "You cannot influence it directly through hypnosis.  You'll need to try and influence it indirectly by working on another aspect of her thinking."
  # add tags 'sos_hypno_attempted' to jasmine  # Tag that this action has been attempted so weekend hypnosis can also remove the option. ## no longer needed
  $ jasmine.sos_hypno_action.backtrack = True ## this and the next two commands back you up to the menu of hypnosis options
  $ jasmine.remove_action( jasmine.sos_hypno_action )  # Use the SOS hypno action reference instead of the "rem action" shortcut, because this is accessible via weekend hypnosis, as well. ## NEED make sure this works?
  $ context = "jasmine_hypnosis"
  break_sequence
  return

# Resistance
label jasmine_resistance_hypnosis:
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_resistance_1
    else:
        wt_image exhi_weekend_hypno_4
    if jasmine.status == 'on_training':
        "You work on [jasmine.name]'s resistance. If you can lower her resistance to you, it may be easier to get her to act out her fantasies."
    else:
        "You work on [jasmine.name]'s resistance to your instructions."
    # system now applies the resistance loss and then goes on to the _resistance_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    return

label jasmine_resistance_hypnosis_end:
    if not jasmine.has_tag('girlfriend'):
        # note: the below could have been done with the 'test' function
        if jasmine.modified_stat( 'resistance' ) > 55:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_leaving
            else:
                wt_image exhi_leaving_2
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she's more open to listening to you, not that you can tell from the look she gives you as she leaves."
        elif jasmine.modified_stat( 'resistance' ) > 40:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_desire_2
            else:
                wt_image exhi_dildo_1_18
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she's more open to listening to you."
            "She smiles at you and looks like she's about to say something, then thinks better of it and leaves."
        elif jasmine.modified_stat( 'resistance' ) > 20:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_2
            else:
                wt_image exhi_weekend_hypno_17
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she's more open to listening to you."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                "She clutches nervously at her dress and looks like she's about to say something, then thinks better of it and leaves."
            else:
                "She fidgets nervously with the hem of her skirt and looks like she's about to say something, then thinks better of it and leaves."
        elif jasmine.modified_stat( 'resistance' ) > 0:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_2
            else:
                wt_image exhi_weekend_hypno_17
                "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she's more open to listening to you."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                "She clutches nervously at her dress as she addresses you before leaving."
            else:
                "She fidgets nervously with the hem of her skirt as she addresses you before leaving."
            jasmine.c "Thank you for helping me."
        else:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_hypno_submission_3
            else:
                wt_image exhi_weekend_hypno_17
            "When you've taken her as far as you can for today, you have her dress, then send her home.  She doesn't exactly remember what the two of you did, but she's more open to listening to you."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                "She clutches nervously at her dress as she addresses you before leaving."
            else:
                "She fidgets nervously with the hem of her skirt as she addresses you before leaving."
            jasmine.c "Thank you for helping me.  Is there anything else you wanted me to do before I go?"
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                player.c "You seem to be having a hard time keeping your dress down.  Stop fighting the instinct to expose yourself and show me your panties."
                wt_image exhi_hypno_submission_4
                "She pulls up the hem of her dress to allow you to examine her."
            else:
                player.c "You seem to be having a hard time keeping your skirt in place.  Stop fighting the instinct to expose yourself and show me your ass."
                wt_image exhi_dildo_1_1
                "She pulls her skirt down ..."
                wt_image exhi_weekend_hypno_18
                "... and lets you examine her ass."
            player.c "That feels better, doesn't it?"
            jasmine.c "Yes"
            change jasmine sos by 5 notify
    return

# Bare Breasts
label jasmine_bare_breasts_hypnosis:
    # note: if girlfriend, will already have too high a privateshow_count to trigger this action
    if jasmine.status == 'on_training':
        "[jasmine.name] wants to be an exhibitionist. You decide to take a chance and show her how she has been happily exposing herself to you under hypnosis."
    player.c "[jasmine.name], you are going to come out of your trance now, and be aware of what you are doing."
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bare_breasts_2
    else:
        wt_image exhi_weekend_hypno_4
    "[jasmine.name] comes out of her trance, and suddenly realizes that her breasts are exposed."
    jasmine.c "What's going on?"
    player.c "I hypnotized you. While you were hypnotized, you showed me your breasts."
    if jasmine.status == 'on_training':
        jasmine.c "I showed you my breasts?  You made me do it!"
        player.c "I can't make you do anything with hypnosis that you don't want to do. You want to be an exhibitionist, but you're scared. Is this scary now?"
        jasmine.c "I ... I don't know what this is."
        player.c "Let me ask you this.  Why haven't you covered yourself up?"
        jasmine.c "I don't know.  Did you hypnotize me not to?"
        player.c "No, I didn't. I think you haven't covered yourself up because right now you are a bit humiliated, a bit scared, and a bit excited. Is that true?"
        jasmine.c "I guess.  A little.  Yes."
        player.c "You want to be an exhibitionist. This is what it feels like to expose yourself to a man. Minus only the memory of what it felt like when you took off your clothes."
        player.c "I'm going to lift the block on that memory now. I want you to remember opening your top to expose yourself to me, [jasmine.name]."
        if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
            wt_image exhi_hypno_bare_breasts_3
        else:
            wt_image exhi_weekend_hypno_6
        "[jasmine.name] moans slightly as you lift the block in her mind, and she remembers the act of opening her top to show you her breasts."
    player.c "How does it feel, [jasmine.name], exposing yourself to me like this?"
    jasmine.c "It feels right."
    $ jasmine.privateshow_count = 1  # Increment count of private shows.  This replaces the first private show action.
    change jasmine sos by 10 notify
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_12
    return

# Bare Pussy
label jasmine_bare_pussy_hypnosis:
    player.c "[jasmine.name], we should be more comfortable."
    player.c "You want to show me your pussy. You should show me your pussy. Show me your pussy so that we can both enjoy looking at it. It excites you to show your pussy to men. Show it to me now."
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bare_pussy_1
    else:
        wt_image exhi_weekend_hypno_7
    $ jasmine.add_tags( 'bare_pussy' )
    $ jasmine.action_barepussy_hypno.backtrack = True
    $ context = "jasmine_hypnosis"
    # break_sequence
    return

# Bare Pussy Wake
label jasmine_bare_pussy_wake_hypnosis:
    # note: if girlfriend, will already have too high a privateshow_count to trigger this action
    if jasmine.status == 'on_training':
        "[jasmine.name] wants to be an exhibitionist.  You decide to take a chance and show her how she has been happily exposing herself to you under hypnosis."
    player.c "[jasmine.name], you are going to come out of your trance now, and be aware of what you are doing."
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bare_pussy_2
        "[jasmine.name] comes out of her trance, and immediately realizes that her breasts and pussy are exposed.  She instinctively reaches for her sex, but doesn't quite cover it up, her hand resting protectively around it without obscuring your view."
    else:
        wt_image exhi_weekend_hypno_9
        "[jasmine.name] comes out of her trance, and immediately realizes that her breasts and pussy are exposed."
    jasmine.c "What's going on?"
    player.c "I hypnotized you.  While you were hypnotized, you showed me your breasts and pussy."
    if jasmine.status == 'on_training':
        jasmine.c "I showed you my pussy?  Did you make me do that?"
        player.c "I can't make you do anything with hypnosis that you don't want to do. You want to be an exhibitionist, but you're scared. Is this scary now?"
        jasmine.c "I... I don't know what this is."
        player.c "Let me ask you this, then.  Why haven't you covered yourself up?"
        jasmine.c "I don't know.  Did you hypnotize me not to?"
        player.c "No, I didn't.  I think you haven't covered yourself up because right now you are a bit humiliated, a bit scared, and a bit excited. Is that true?"
        jasmine.c "I guess.  A little.  Yes."
        player.c "You want to be an exhibitionist. This is what it feels like to expose yourself to a man. Minus only the memory of what it felt like when you took off your clothes."
        if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
            player.c "I'm going to lift the block on that memory now. I want you to remember pulling up your dress to expose yourself to me, [jasmine.name]."
            wt_image exhi_hypno_bare_pussy_3
            "[jasmine.name] smiles and removes her hand from between her legs as you lift the block in her mind, and she remembers the act of pulling up her dress and spreading her legs to show you her sex."
        else:
            player.c "I'm going to lift the block on that memory now. I want you to remember pulling up your clothes to expose yourself to me, [jasmine.name]."
            wt_image exhi_weekend_hypno_7
            "[jasmine.name] gasps as you lift the block in her mind and she remembers spreading her legs to show you her sex. Her hand reaching down and spreads her pussy lips again, duplicating the moment."
    player.c "How does it feel, [jasmine.name], exposing yourself to me like this?"
    jasmine.c "It feels right."
    $ jasmine.privateshow_count = 2  # Increment count of private shows.  This replaces the second private show action.
    change jasmine sos by 10 notify
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_13
    return

# Hypno Blowjob
label jasmine_blowjob_hypnosis:
    "[jasmine.name] gets quite excited when she exposes herself to you. You decide to act on that excitement."
    player.c "It feels good to expose yourself to me, [jasmine.name]. It excites you. It excites me, too. You'd like to see how excited you make me. You want to feel how excited I am."
    player.c " You want to thank me for giving you the chance to expose yourself. Come here now, [jasmine.name], and show me how thankful you are to me."
    if ( jasmine.sex_level > 0 ) or jasmine.test( 'resistance', 25 ) or jasmine.has_tag('girlfriend'):
        if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
            wt_image exhi_hypno_bj_1
            "Under the influence of your trance, [jasmine.name] comes over to you, takes out your cock, and opens her mouth."
            wt_image exhi_hypno_bj_2
            "Soon she's thanking you properly, just as you instructed."
        else:
            wt_image exhi_weekend_hypno_8
            "Under the influence of your trance, [jasmine.name] kneels in front of you and opens her mouth."
            "She looks so cute and vulnerable, you can't help yourself from giving her mouth a hard, rough fucking.  She simply kneels there, keeping her lips wrapped around your cock, and accepts the face fuck."
        $ title = "What do you do now?"
        menu:
            "Cum and then have her dress":
                call jasmine_blowjob_hypnosis_trance from _call_jasmine_blowjob_hypnosis_trance
            "Wake her from her trance now":
                "This is a dangerous action.  If she isn't sufficiently submissive to you or if her desire for you isn't high enough, she will likely react poorly to discovering that you've violated the agreement with her husband and are using her for sex.  Not to mention how she'll feel about you initiating sex when she's not aware of what you're doing."
                $ title = "What do you do?"
                menu:
                    "Cum and then have her dress":
                        call jasmine_blowjob_hypnosis_trance from _call_jasmine_blowjob_hypnosis_trance_1
                    "Proceed to wake her from her trance now":
                        call jasmine_blowjob_hypnosis_wake from _call_jasmine_blowjob_hypnosis_wake
    else:
        "[jasmine.name] is excited by the act of exposing herself to you, but she's not ready to have sex with you yet.  She knows that's wrong and would be cheating on her husband."
        "You can try again later, after you lower her resistance to you.  For now, make another choice."
        $ jasmine.add_tags( 'hypno_bj_attempted_today' )
        $ jasmine.action_bj_hypno.backtrack = True
    return

label jasmine_blowjob_hypnosis_trance:
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bj_4
    else:
        wt_image exhi_weekend_hypno_19
    "[jasmine.name] might react badly to coming out of a trance to discover your cock in her mouth, so you simply take your pleasure from her, emptying your load into her mouth."
    player.c "[player.orgasm_text].  Swallow it all, [jasmine.name] ..."
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bj_1
    else:
        wt_image exhi_weekend_hypno_20
    player.c "... and lick my cock clean."
    $ jasmine.hypno_swallow_count += 1
    $ jasmine.hypno_blowjob_count += 1
    orgasm notify
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_portrait_1
    else:
        wt_image exhi_weekend_hypno_1
    "Once she's done, you have her dress, then bring her out of the trance."
    jasmine.c "Did you want to do anything with me today?"
    player.c "I already have."
    jasmine.c "You mean you just wanted to talk with me?"
    player.c "Something like that."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_14
    return

label jasmine_blowjob_hypnosis_wake:
    if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
        wt_image exhi_hypno_bj_3
    else:
        wt_image exhi_weekend_hypno_11
        "You take your hands off [jasmine.name]'s head and wake her from the trance.  She immediately pulls herself off your cock."
    jasmine.c "Oh my god!  What are you doing!"
    if jasmine.status == 'on_training':
        player.c "I'm not doing anything, [jasmine.name]. You were the one doing something. Specifically, you were sucking my cock. Would you like to know why?"
        "She closes her eyes and covers her face with her hands."
        jasmine.c "You tricked me.  Oh, this is so messed up."
        player.c "I didn't trick you. I asked you to thank me while you were hypnotized. Sucking my cock was the way you decided to thank me."
        player.c "It turns you on to expose yourself to men. You like knowing that the sight of your body excites them."
        player.c "You like the thrill of being bad and the danger that comes with it. And you wanted to show me that you appreciate me helping you to finally experience what you've wanted for a long time."
        player.c "You could admit all of those things to yourself when you were hypnotized, [jasmine.name]. I want you to admit them now."
        if jasmine.test( 'submission', 30 ) or jasmine.test( 'desire', 70 ):
            jasmine.c "...I guess it's true."
            player.c "It is true, and it doesn't say anything bad about you. In fact, it says something good about you, that you're able to accept who you are and embrace it."
            player.c "What you and I do together stays between you and I. Your husband doesn't need to know anything other than that you are happy and are finally getting to experience what it's like to be an exhibitionist."
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                player.c "Now I want you to come over here and finish what you started."
                wt_image exhi_hypno_bj_4
                "She doesn't look at you, and she keeps her eyes closed.  But she gives you an enthusiastic blow job, and when you cum she silently swallows it all down without being asked."
                player.c "[player.orgasm_text]"
                wt_image exhi_hypno_bj_3
                "She goes home tonight conflicted about the change in your relationship, but you're certain she'll be back next week."
            else:
                player.c "Now I want you to finish what you started."
                wt_image exhi_weekend_hypno_10
                "Meekly [jasmine.name] nods her head and does what you say. She looks away from you as she sucks your cock, but she gives you an enthusiastic blow job, and when you cum she silently swallows it all down without being asked."
                player.c "[player.orgasm_text]"
                wt_image exhi_weekend_hypno_9
                "She goes home conflicted about the change in your relationship, but you're certain she'll be back next week."
            change jasmine submission by 15
            change jasmine resistance by -10
            $ jasmine.blowjob_count += 1
            $ jasmine.swallow_count += 1
            orgasm notify
            if jasmine.sex_level == 0:
                $ jasmine.sex_level = 1
        else:
            if jasmine.status == 'on_training' and not jasmine.has_tag( 'hypno_weekend' ):
                wt_image exhi_leaving
            else:
                wt_image exhi_leaving_2
            jasmine.c "No... no, I didn't sign up for this. I told my husband I wouldn't fool around on him, and I meant it."
            "She leaves.  You don't expect to see her again."
            # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unvailable'
            # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
            # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
            call convert(jasmine, "unavailable") from _call_convert_22
    else:
        player.c "I'm not doing anything, [jasmine.name]. You were the one doing something. Specifically, you were sucking my cock, and I'd like you to finish the job."
        wt_image exhi_weekend_hypno_10
        "Meekly [jasmine.name] nods her head and does what you say. She's confused about how your cock ended up in her mouth, but she pleasures it enthusiastically anyway."
        player.c "[player.orgasm_text]"
        $ jasmine.blowjob_count += 1
        $ jasmine.swallow_count += 1
        orgasm notify
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_15
    return

label jasmine_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
    if jasmine.has_tag('no_trigger_message_given'):
        pass
    elif player.has_tag('hypnotist'):
        "Although [jasmine.name] is susceptible to your suggestions while under hypnosis, she's unusually resistant to implanting post-hypnotic suggestions. You won't be able to install a trigger in her."
        add tags 'implant_trigger_failed' 'no_trigger_message_given' to jasmine
        # rem tags 'trained_today' 'trained_this_week' from jasmine  ##WT: not sure why this was here?  don't think these should be removed, as they allow additional training and cost you her fees this week
        # $ action.backtrack = True #WT: also not sure why this is here, as you shouldn't backtrack from here, you should proceed to the end of the hypnosis queue
        #$ jasmine.remove_action(jasmine.implant_action)
    return

label jasmine_hypnosis_end:
    # the following keeps track of how often you've hypnotized the client and subtracts the required energy; can be placed here for Lauren because at this point nothing will cancel the hypnosis session
    $ jasmine.hypno_session()
    call character_location_return(jasmine) from _call_character_location_return_307
    if jasmine.has_tag('hypno_weekend'):
        rem tags 'hypno_weekend' from jasmine
    if jasmine.status == 'on_training':
        end_day
    return

# End Session
label jasmine_end_session:
  if jasmine.status == "on_training":
    $ jasmine.training_session()
    "You're unable to find an activity that both you and Jasmine are willing to proceed with, so you end today's session here."
    $ player.extra_clients_fee_this_week -= jasmine.pay # so you don't get paid for training her this week
    add tags 'failed_regular_training_this_week' to jasmine
    call character_location_return(jasmine) from _call_character_location_return_308
    end_day
  elif jasmine.has_tag('continuing_actions'):
    $ jasmine.training_session()
    "You've spent enough time with Jasmine for today. You send her home."
    call character_location_return(jasmine) from _call_character_location_return_309
    wt_image current_location.image
  else:
    add tags 'shut_off_end_session' to jasmine
  return

# Weekend Actions
label jasmine_pre_weekend:
    add tags 'checking_for_weekend' to jasmine
    return

label jasmine_post_weekend:
    if jasmine.has_tag('checking_for_weekend'):
        rem tags 'checking_for_weekend' from jasmine
    else:
        if jasmine.has_tag('failed_regular_training_this_week'):
            rem tags 'failed_regular_training_this_week' from jasmine
            $ player.extra_clients_fee_this_week += jasmine.pay
    return

label jasmine_weekend:
    if player.energy >= energy_long.value:
        call expandable_menu(jasmine_weekend_training_menu) from _call_expandable_menu_11
    else:
        sys "You don't have enough energy for this action, choose something else."
    return

# Weekend Hypnosis
label jasmine_weekend_hypno:
    call forced_movement(living_room) from _call_forced_movement_53
    summon jasmine to living_room
    # the tags flags the artwork to be used during the hypnosis actions; in this instance, this was easier then testing against day
    rem tags 'checking_for_weekend' from jasmine
    add tags 'hypno_weekend' to jasmine # note: could have done this with the if is_weekend() command instead
    # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
    $ queue_action(jasmine.hypno_action)
    return

## deleted as no longer needed; replaced by queue_action command
# label jasmine_weekend_hypno_menu:
#  $ title = "What do you want to do with her?"
#  menu:
#    "Wake her up with her breasts still out" if jasmine.privateshow_count == 0:
#      call jasmine_bare_breasts_hypnosis
#    "Have her show her pussy" if jasmine.privateshow_count == 1 and not jasmine.has_tag( 'bare_pussy' ):
#      call jasmine_bare_pussy_hypnosis
#    "Wake her up with her pussy still out" if jasmine.privateshow_count == 1 and jasmine.has_tag( 'bare_pussy' ):
#      call jasmine_bare_pussy_wake_hypnosis
#    "Have her blow you" if jasmine.privateshow_count >= 2 and not jasmine.has_tag( 'hypno_bj_attempted_today' ):
#      call jasmine_blowjob_hypnosis
#    "Work on her Desire":
#      call jasmine_desire_hypnosis
#    "Work on her Submission":
#      call jasmine_submission_hypnosis
#    "Work on her Resistance":
#      call jasmine_resistance_hypnosis
#    "Work on her Sense of Self" if not jasmine.has_tag( 'sos_hypno_attempted' ):
#      call jasmine_sos_hypnosis
#  return

# Weekend Road Trip
label jasmine_weekend_roadtrip:
  rem tags 'checking_for_weekend' from jasmine
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  call forced_movement(outdoors) from _call_forced_movement_54
  summon jasmine to outdoors
  wt_image exhi_weekend_car_4
  if jasmine.has_tag( 'roadtrip' ):
    call jasmine_weekend_roadtrip_normal from _call_jasmine_weekend_roadtrip_normal
  else:
    add tags 'roadtrip' to jasmine
    call jasmine_weekend_roadtrip_first from _call_jasmine_weekend_roadtrip_first
  call forced_movement(living_room) from _call_forced_movement_55
  call character_location_return(jasmine) from _call_character_location_return_310
  end_day
  return

# Weekend Road Trip (First)
label jasmine_weekend_roadtrip_first:
  player.c "[jasmine.name], we're taking a little road trip."
  "You escort [jasmine.name] to your car."
  player.c "Make yourself comfortable, it's a long drive."
  jasmine.c "Where are we going?"
  player.c "Someplace women like you are appreciated properly."
  wt_image exhi_weekend_car_1
  "As you hit the road, [jasmine.name] settles in.  You're pleased to see her show off a little leg through the window."
  call jasmine_weekend_roadtrip_1 from _call_jasmine_weekend_roadtrip_1
  change jasmine resistance by -15 notify  # In RAGS, the first trip changes resistance by -10, then the strip club scene by another -5.  Here it's done all at once so the strip club can be reused.
  return

# Weekend Road Trip (Normal)
label jasmine_weekend_roadtrip_normal:
  player.c "Come on, [jasmine.name]. We're going on another road trip."
  jasmine.c "To the same strip club again?"
  player.c "It depends. I was thinking perhaps it would be better if you were the show?"
  "[jasmine.name] blushes."
  # Public exposure level 0-1
  if jasmine.publicshow_level <= 1:
    player.c "Let's give our fellow road travelers a nice view today, [jasmine.name]."
    if jasmine.test( 'resistance', 40 ):
      "[jasmine.name] hesitates a moment, then pulls off her bottoms."
      wt_image exhi_weekend_car_2
      jasmine.c "I think this is safest.  I can control who sees me and who doesn't."
      "You're not going to complain about her choice."
      call jasmine_weekend_roadtrip_2 from _call_jasmine_weekend_roadtrip_2
      if jasmine.publicshow_level == 0:
        change jasmine sos by 15 notify
      else:
        change jasmine sos by 10 notify
      change jasmine desire by 10 notify
      $ jasmine.publicshow_level = 2
    else:
      wt_image exhi_weekend_car_1
      jasmine.c "That doesn't seem safe.  Who knows who could see me driving by?"
      "[jasmine.name]'s still too resistant to you to be the show herself. You'll need to settle with taking her to watch other women strip naked in public."
      call jasmine_weekend_roadtrip_1 from _call_jasmine_weekend_roadtrip_1_1
      change jasmine resistance by -5 notify
  # Public exposure level 2
  elif jasmine.publicshow_level == 2:
    player.c "Let's give our fellow road travelers a nice view today, [jasmine.name]."
    "[jasmine.name] hesitates a moment, thinking about how far she wants to go."
    player.c "No need to overthink this, [jasmine.name].  You don't need any clothes on."
    if jasmine.test( 'resistance', 30 ):
      wt_image exhi_weekend_car_3
      "She nods and strips her clothes off. At your suggestion, she wraps a cloth around her face. Driving in the car, there's no way to be sure an acquaintance won't see her go by, so the cloth will help preserve her anonymity."
      call jasmine_weekend_roadtrip_3 from _call_jasmine_weekend_roadtrip_3
      change jasmine desire by 10 notify
      change jasmine sos by 10 notify
      $ jasmine.publicshow_level = 3
    else:
      wt_image exhi_weekend_car_2
      "At first you think she's going to comply, but her resistance to you is still a little high.  She gets in the car and pulls off just her bottoms."
      jasmine.c "I feel safer this way. I can control who sees me and who doesn't."
      call jasmine_weekend_roadtrip_2 from _call_jasmine_weekend_roadtrip_2_1
      change jasmine desire by 5 notify
  # Public exposure level 3+
  else:
    wt_image exhi_weekend_car_3
    "[jasmine.name] has become quite comfortable exposing herself in public.  She strips down before entering the car."
    call jasmine_weekend_roadtrip_3 from _call_jasmine_weekend_roadtrip_3_1
    change jasmine desire by 5 notify
  return

# Weekend Road Trip Destination 1
label jasmine_weekend_roadtrip_1:
  "About an hour outside town, you pull over."
  player.c "Let's get some snacks."
  wt_image exhi_weekend_store_1
  "You're disappointed to see her pull her clothes together. She doesn't show off anything as she picks up some items."
  wt_image exhi_weekend_strip_club_1
  "After another stretch of driving, you get to your destination. It isn't a fancy place, but it's insanely popular, and [jasmine.name] isn't the only woman in the crowd.  It's the perfect place for her to see women being appreciated for being naked in public."
  "You let [jasmine.name] take in the experience and imagine herself as one of the women exposed to the gaze of others, then drive her back home."
  return

# Weekend Road Trip Destination 2
label jasmine_weekend_roadtrip_2:
  player.c "Time to get some snacks, [jasmine.name]."
  "As she puts her pants and sweater back on, you hand her a pair of sunglasses. She looks at you, then realizes your intent."
  wt_image exhi_weekend_store_2
  "In the snack aisle, she looks around, then moons the store, giggling."
  "No need to take her anywhere else today, she got what she needed out of this trip.  The two of you head home."
  return

# Weekend Road Trip Destination 3
label jasmine_weekend_roadtrip_3:
  "After driving around a while, you find a quiet roadside store."
  player.c "Time for some snacks, [jasmine.name]."
  wt_image exhi_weekend_store_3
  "She hops out of the car and heads into the store."
  wt_image exhi_weekend_store_4
  "She picks out some water to take to the shocked clerk."
  jasmine.c "It sure is hot out today."
  "No need to take her anywhere else today, she got what she needed out of this trip.  The two of you head home."
  return

## Character Specific Actions
# Prep Work
label jasmine_prepwork:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  $ jasmine.prepwork_count += 1
  player.c "[jasmine.name], I'd like you to watch some videos for me."
  wt_image exhi_prep_work_1
  "You sit her down in front of a computer and show her a selection of videos of women taking off their clothes in public."
  "To reinforce the message, you intersperse some videos of the women's partners getting excited by the public displays, and giving the women a good fucking."
  "When the videos of the flashings play, you talk to [jasmine.name] about what the women must be feeling.  When the videos of the fuckings play, you say nothing."
  # First Time
  if jasmine.prepwork_count == 1:
    "[jasmine.name] may well have watched this type of porn before.  Watching it with you talking to her about how realistic each scenario is, what could or couldn't be achieved safely in real life ... well, that's a whole different experience."
    change jasmine desire by 10
    change jasmine resistance by -10
  # Second Time - action is shutoff when prepwork_count reaches 2
  else:
    "[jasmine.name] has done this with you before.  The effect of your conversation isn't as strong as the first time, but it still helps to prepare her mentally for the experience of being one of these women exposing themselves in public.  She won't, however, get anything out of any additional sessions."
    change jasmine desire by 5
    change jasmine resistance by -5
  call character_location_return(jasmine) from _call_character_location_return_311
  wt_image current_location.image
  change player energy by -energy_long notify
  "When you've watched as much exhibitionist porn with her as she can tolerate for one day, you send her home."
  end_day
  return

# Public Show
label jasmine_publicshow:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  if jasmine.publicshow_count > 0:
    call forced_movement(outdoors) from _call_forced_movement_554
  if jasmine.publicshow_count >= 8:
    call jasmine_publicshow_8 from _call_jasmine_publicshow_8
  elif jasmine.publicshow_count == 7:
    call jasmine_publicshow_7 from _call_jasmine_publicshow_7
  elif jasmine.publicshow_count == 6:
    call jasmine_publicshow_6 from _call_jasmine_publicshow_6
  elif jasmine.publicshow_count == 5:
    call jasmine_publicshow_5 from _call_jasmine_publicshow_5
  elif jasmine.publicshow_count == 4:
    call jasmine_publicshow_4 from _call_jasmine_publicshow_4
  elif jasmine.publicshow_count == 3:
    call jasmine_publicshow_3 from _call_jasmine_publicshow_3
  elif jasmine.publicshow_count == 2:
    call jasmine_publicshow_2 from _call_jasmine_publicshow_2
  else:
    call jasmine_publicshow_1 from _call_jasmine_publicshow_1

  call forced_movement(living_room) from _call_forced_movement_57
  change player energy by -energy_long
  call character_location_return(jasmine) from _call_character_location_return_312
  end_day
  return

# Public Show 1
label jasmine_publicshow_1:
  #Initial chat, first time only.
  if jasmine.publicshow_count == 0:
    wt_image jasmine.image
    player.c  "[jasmine.name], I'd like you to come with me."
    jasmine.c "Where are we going?"
    player.c  "To a part of town where no one should recognize you."
    jasmine.c "I'm not sure I'm ready for this."
    player.c  "This is practice.  I'll be there to keep you safe. Just small steps, to build you your confidence and your courage."
    $ jasmine.publicshow_count = 1
    call forced_movement(outdoors) from _call_forced_movement_555
  wt_image exhi_od_1_1
  "You bring [jasmine.name] to a rough part of town. It's not particularly dangerous, but it's not the sort of place her friends or coworkers are likely to frequent either.  Nervously, she starts to walk along the road. You stay close for now, to provide assurance."
  wt_image exhi_od_1_6
  player.c  "[jasmine.name], see that car pulling out of the parking lot back there?  Do you know the people in that car?"
  "She shakes her head 'no'."
  player.c  "I want you to go flash them."
  wt_image exhi_od_1_3
  "She turns around and places her hands on her top ..."
  if jasmine.test('resistance', 45) or jasmine.test('submission', 25):
    wt_image exhi_od_1_5
    "... for a moment you think she's going to balk.  Then she gathers her courage and pulls down her top."
    player.c  "How does that feel, [jasmine.name]?"
    wt_image exhi_od_1_7
    "She's too overwhelmed by the moment to respond.  You tell her to cover herself up and take her home.  She can't speak on the way back either.  She just sits in your car and trembles silently, trying to come to grips with the experience.  As she's leaving, she finally speaks."
    wt_image exhi_od_1_8
    jasmine.c "Thank you."
    change jasmine desire by 10
    change jasmine sos by 10
    $ jasmine.publicshow_level = 1
    $ jasmine.publicshow_count = 2
  else:
    wt_image exhi_od_1_4
    "... then she covers up and starts walking away."
    wt_image exhi_od_1_2
    jasmine.c "Sorry, I just couldn't do it."
    $ title = "What do you do?"
    menu:
      "Encourage her":
        call jasmine_publicshow_encourage from _call_jasmine_publicshow_encourage
      "Berate her":
        call jasmine_publicshow_berate from _call_jasmine_publicshow_berate
  return

# Public Show 2
label jasmine_publicshow_2:
  wt_image exhi_od_1_1
  "You bring [jasmine.name] out for another public session. As before, you stay close to her."
  wt_image exhi_od_2_2
  "She hasn't gone far when a man in a beat up old pickup truck whistles at her."
  wt_image exhi_od_2_1
  player.c  "Do you know him?"
  jasmine.c "No"
  wt_image exhi_od_2_3
  player.c  "Then we both know what you want to do."
  wt_image exhi_od_2_4
  "Much to the delight of the pickup truck driver, [jasmine.name] gives him a great show."
  wt_image exhi_od_2_3
  $ title = "What do you do now?"
  menu:
    "Tell her to flash her bottom":
      player.c  "Go on.  You want to show him more than that."
      wt_image exhi_od_2_5
      "With no hesitation, she spins around and pulls up her dress to show off her bare bottom. The driver of the pickup truck whistles louder as [jasmine.name] laughs."
      wt_image exhi_od_1_8
      "You get her out of there, before she can get herself into trouble."
      change jasmine desire by 5
      change jasmine sos by 5
      $ jasmine.publicshow_level = 2
      $ jasmine.publicshow_count = 3
    "Tell her to get closer and show him her bottom":
      player.c  "Go on, [jasmine.name].  Get closer so you can give him a better show."
      if jasmine.test('resistance', 35) or jasmine.test('submission', 35):
        wt_image exhi_od_2_6
        "Nervously, [jasmine.name] approaches the pickup truck.  You stay close to her."
        wt_image exhi_od_2_7
        player.c  "Turn around and give him a good look at your bottom."
        wt_image exhi_od_2_8
        "[jasmine.name] pulls up her dress to give him a good, close up look at her bare bottom. She says nothing, but the trembling in her legs tells you how excited she is."
        wt_image exhi_od_2_9
        "You get her home before she can get herself in trouble. Once again, it takes her a while before she can say anything."
        wt_image exhi_od_1_8
        jasmine.c "Thank you."
        change jasmine desire by 10
        change jasmine sos by 15
        $ jasmine.publicshow_level = 2
        $ jasmine.publicshow_count = 3
      else:
        "[jasmine.name] hesitates a moment, then bolts."
        jasmine.c "I'm sorry.  I couldn't.  I wanted to, but I just couldn't."
        $ title = "What do you do?"
        menu:
          "Encourage her":
            call jasmine_publicshow_encourage from _call_jasmine_publicshow_encourage_1
          "Berate her":
            call jasmine_publicshow_berate from _call_jasmine_publicshow_berate_1
  return

# Public Show 3
label jasmine_publicshow_3:
  wt_image exhi_od_3_1
  "[jasmine.name] is eager to begin her next public outing."
  wt_image exhi_od_3_2
  "Up ahead, she sees a man approach."
  wt_image exhi_od_3_3
  "A quick look around confirms there's no one else in sight."
  wt_image exhi_od_3_4
  "[jasmine.name] greets him with a big beaming smile, and a view of her big beaming breasts."
  wt_image exhi_od_3_5
  "The man reaches for his cell phone and prepares to take a photo of her."
  $ title = "What do you do?"
  menu:
    "Tell him no photos.":
      player.c  "Sorry dude.  No photos."
      "He puts the cell phone down."
      wt_image exhi_od_1_5
      "[jasmine.name] seems a little disappointed, but it's your responsibility to keep her safe, and there's no telling where those photos might have ended up."
      "She consoles herself - and the passerby - with a nice view as he continues on his way."
      "After he's gone, you take her home."
      jasmine.c "That was nice.  I wish ... I know it was dangerous, and thanks for keeping me safe. Part of me wanted that danger."
      jasmine.c "I wish there had been a way to let him take some pictures. The idea of him looking at my pictures in private ..."
      jasmine.c "I can't believe how much that idea turns me on."
      change jasmine sos by 5
    "Let him snap a few shots":
      wt_image exhi_od_3_6
      "You decide there's no harm in the man taking home some personal mementos. Certainly [jasmine.name] is not concerned. She walks up closer to him to let him have a closer look."
      wt_image exhi_od_3_7
      "The situation seems to be turning her on. She doesn't object when the man reaches out to her..."
      wt_image exhi_od_3_8
      "...and when he tweaks her nipple, she just smiles."
      wt_image exhi_od_3_9
      "She then turns around to let him take a picture of her bottom."
      wt_image exhi_od_3_10
      "She seems to be losing herself in the joy of the moment. He gives her a playful slap and she just laughs."
      # If she has exposed her bottom before
      if jasmine.publicshow_level > 1:
        wt_image exhi_od_3_11
        "Then she spins around to give him a great look at her pretty pussy."

        # If this is her first pussy exposure
        if jasmine.publicshow_level == 2:
          change jasmine desire by 10
          change jasmine sos by 15
          $ jasmine.publicshow_level = 3
        else:
          change jasmine desire by 10
          change jasmine sos by 10
      else:
        change jasmine desire by 5
        change jasmine sos by 5
        $ jasmine.publicshow_level = 2
      wt_image exhi_od_3_12
      "[jasmine.name] is too excited to speak on the drive home.  She sits in the passenger seat, trembling slightly from the experience.  When you drop her off, she gives you a big grin."
      jasmine.c "Thank you."

      add tags 'publicshow_photos' to jasmine
      $ jasmine.photod_in_public_week_for_event = week + 1

  $ jasmine.publicshow_count = 4
  return

# Public Show 4
label jasmine_publicshow_4:
  wt_image exhi_od_4_1
  "[jasmine.name] is eager to get back outdoors."
  wt_image exhi_od_4_2
  "She spots a car pulling out of a parking lot across the street."
  wt_image exhi_od_4_3
  "With no hesitation, she pulls down her top."
  wt_image exhi_od_4_4
  "Perhaps worried that they won't have a good enough view, she hustles closer to them, pulling up the bottom of her dress as she goes."

  # If she has exposed her bottom before
  if jasmine.publicshow_level > 1:
    wt_image exhi_od_4_5
    "To make sure she has their attention, she pulls the front of her dress up, giving them a great view of her bare pussy."

    # If she has exposed her pussy before
    if jasmine.publicshow_level == 2:
      change jasmine desire by 5
      change jasmine sos by 10
      $ jasmine.publicshow_level = 3
    else:
      change jasmine desire by 5
      change jasmine sos by 5
  else:
    change jasmine desire by 5
    change jasmine sos by 10
    $ jasmine.publicshow_level = 2

  wt_image exhi_od_4_6
  "She spins around and lets them get a good look at her bare behind."
  wt_image exhi_od_4_7
  "She sends them on their way with another view of her bare breasts."
  wt_image exhi_od_3_12
  jasmine.c "That was fun. I just wish it had been ... edgier. Do you know what I mean?"

  $ jasmine.publicshow_count = 5
  return

# Public Show 5
label jasmine_publicshow_5:
  wt_image exhi_od_5_1
  "You and [jasmine.name] head out for another round of public exhibitionism."
  "She hears some men talking at a storage center, and heads towards them."
  wt_image exhi_od_5_2
  "Up ahead a man is unloading his vehicle. [jasmine.name] gets ready to flash him."
  wt_image exhi_od_5_3
  "A catcall from behind her stops her. Two men are watching her from another storage unit."
  wt_image exhi_od_5_4
  jasmine.c "Were you interested in these, gentlemen?"
  "The men are drinking and whistle approvingly as [jasmine.name] begins to take down her top."
  $ title = "What do you do?"
  menu:
    "Get her out of there":
      "You hustle [jasmine.name] out of there and get her home before she can get into trouble."
      "She's disappointed, but thankful that you have her best interests at heart."
      change jasmine resistance by 10
    "Let her have some fun":
      wt_image exhi_od_5_5
      "[jasmine.name] gives her admirers a close up view."
      wt_image exhi_od_5_6
      "She's even happy to let them make a hands on assessment of her charms."
      wt_image exhi_od_5_7
      "And when they ask to inspect her bottom, she's happy to comply."
      wt_image exhi_od_5_8
      "Their inspection complete, [jasmine.name] laughs and walks away. The men return to their drinking. They have a new story to tell their buddies that none of them will believe."
      wt_image exhi_od_3_12
      jasmine.c "That was so much fun! Thank you helping me do this!"
      change jasmine desire by 10
      change jasmine sos by 10
  $ jasmine.publicshow_count = 6
  return

# Public Show 6
label jasmine_publicshow_6:
  wt_image exhi_od_6_1
  "You and [jasmine.name] spend some time looking for a good opportunity for her to expose herself, without any luck."
  wt_image exhi_od_6_14
  "Then she spots some men working in a garage."
  wt_image exhi_od_6_2
  "[jasmine.name] heads into the garage."
  $ title = "What do you do?"
  menu:
    "Don't let her enter the garage":
      wt_image exhi_od_1_5
      "You're not comfortable with [jasmine.name] going inside the garage. You stop her and lead her to a safe distance, then let her flash the men from there."
      wt_image exhi_od_3_12
      jasmine.c "That was fun.  I just wish it had been ... edgier. Do you know what I mean?"
      change jasmine desire by 5
      change jasmine resistance by -5
      $ jasmine.publicshow_count = 7
    "Let her have some fun":
      "It's closing time at the garage. Before you can follow her inside, one of the men has closed and locked the bay door."
      wt_image exhi_od_6_3
      "From outside, you see [jasmine.name] stroll up to one of the men. You're not sure she's noticed that you haven't been able to follow her."
      wt_image exhi_od_6_15
      "You look around, but can't see the other men. They must have left the garage after locking it, perhaps going out the side door to the garage office? [jasmine.name]'s by herself with the remaining mechanic. As she offers him a view of her breasts, he steps closer and caresses her."
      wt_image exhi_od_6_4
      "When he pulls up the front of her dress [jasmine.name] gasps, but doesn't object to him taking a close look at her pussy."
      wt_image exhi_od_6_5
      "The man says something to [jasmine.name], but from outside you can't hear what it is. Does he misinterpret why she's there, or does he not care? Either way, he helps himself to a mouthful of breast while sticking his fingers in her pussy."
      wt_image exhi_od_6_16
      "[jasmine.name] protests, and the man doesn't take kindly to it. His fingers have confirmed she's wet - she's always wet when exposing herself in public. Maybe he thinks she's just playing hard to get with her protests.  Maybe he doesn't care."
      wt_image exhi_od_6_17
      "Either way, he pulls the dress off her roughly and grabs her by the arms."
      wt_image exhi_od_6_6
      "He leads her across the garage ..."
      wt_image exhi_od_6_7
      "... and deposits her on a box."
      wt_image exhi_od_6_8
      "when he takes off his pants, you start banging on the garage door. He's either too occupied with [jasmine.name] to hear you, or he doesn't care."
      wt_image exhi_od_6_9
      "Poor [jasmine.name] seems in shock. She starts to cry as he enters her, but seems unable to offer any resistance to him."
      wt_image exhi_od_6_10
      "The best she can do is look away. Her face is blank, as if her mind is trying to pretend that this isn't happening."
      wt_image exhi_od_6_11
      "After what seems like an eternity, the man pulls out of [jasmine.name] and lifts her into a sitting up position."
      wt_image exhi_od_6_12
      "As [jasmine.name] looks on in disgust, the man empties his load over her breasts."
      wt_image exhi_od_6_13
      "The garage is part of a large industrial complex. You can't locate the exit the man uses to leave.  A shaken and silent [jasmine.name] eventually unlocks the bay door to let herself out."
      "You try and convince her to go to the police, but she just wants you to take her home to her husband."
      wt_image phone_1
      "You try to contact her the next morning, but she doesn't answer. You never hear from her again."
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unvailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      call convert(jasmine, "unavailable") from _call_convert_23
  return

# Public Show 7
label jasmine_publicshow_7:
  wt_image exhi_od_7_1
  "You and [jasmine.name] once again set out to find a chance for her to expose herself in public."
  "Across the street, [jasmine.name] spots a man closing up his shop."
  wt_image exhi_od_7_2
  "[jasmine.name] immediately drops her top and strolls up to him."
  wt_image exhi_od_7_3
  "As she gets closer, he pulls out a camera and prepares to take a photo."
  $ title = "What do you do?"
  menu:
    "Let him snap a few shots":
      wt_image exhi_od_7_4
      "You decide there's no harm in the man taking home some personal mementos."
      "Certainly [jasmine.name] is not concerned. She gives him a good look, front ..."
      wt_image exhi_od_7_5
      "... and back."
      wt_image exhi_od_3_12
      jasmine.c "Oh my god, that was so hot. When he pulled out that camera, I thought I was going to orgasm on the spot."
      change jasmine desire by 10
      change jasmine sos by 10
    "Tell him no photos":
      wt_image exhi_od_7_6
      player.c  "Sorry dude.  No photos."
      "He puts the camera down, and [jasmine.name] gives a nice view, front ..."
      wt_image exhi_od_7_7
      "... and back."
      wt_image exhi_od_3_12
      jasmine.c "That was nice, but I wish you had let him take the photos of me. I thought I was going to orgasm the moment I saw him bring out the camera."
      change jasmine desire by 5
  $ jasmine.publicshow_count = 8
  return

# Public Show 8
label jasmine_publicshow_8:
  wt_image exhi_od_8_6
  "[jasmine.name] smiles when she sees you've brought her to a restaurant. It's on the outskirts of town. She quickly scans the crowd."
  wt_image exhi_od_8_1
  jasmine.c "Nope.  No one I know here."
  wt_image exhi_od_8_2
  "After you're seated, she excuses herself to go to the washroom. She makes sure you get a nice view of her bottom on the way."
  wt_image exhi_od_8_7
  "You picked this restaurant in part because of its mostly male waiting staff.  [jasmine.name] thinks for a moment when she sees your waiter coming over to take your order."
  wt_image exhi_od_8_3
  "Then she ducks down and unfastens the front of her blouse."
  wt_image exhi_od_8_4
  "As you order for the both of you, [jasmine.name] gives the waiter something to remember about the evening."
  wt_image exhi_od_8_5
  jasmine.c "That was fun.  We should come here again!"
  # First time at restaurant
  if jasmine.publicshow_count == 8:
    change jasmine desire by 10
    change jasmine sos by 10
    $ jasmine.publicshow_count = 9
  # Subsequent visits to restaurant
  else:
    change jasmine desire by 5
  return

# Public Show Encourage
label jasmine_publicshow_encourage:
  player.c "Don't worry, [jasmine.name]. You did fine. I told you, we're going to take things slow. You're making progress."
  "She nods and give you a small smile, encouraged by your words."
  change jasmine resistance by -5
  return

# Public Show Berate
label jasmine_publicshow_berate:
  player.c "You told me you would submit to my instructions. Yet here you are, running away from what you want like a little girl. No wonder you're a mess of conflicting desires. You won't accept who and what you are.  I know what you are and what you need.  The sooner you start listening to me, the better."
  "[jasmine.name]'s cheeks flush. Your words hurt, but she recognizes some truth in them. It may not change her behavior today, but she's starting to see you as an authority figure."
  change jasmine submission by 5
  return

# Office Show
label jasmine_officeshow:
  # If Office Show has already been chosen today.
  if jasmine.officeshow_tempcount == 2:
    "You need to wait until next week to check in with [jasmine.name] again about this topic."

  # If Office Show has not already been chosen today.
  else:
    $ jasmine.officeshow_tempcount = 1  # Note that Office Show has been chosen.
    if jasmine.officeshow_count >= 3:
      call jasmine_officeshow_3 from _call_jasmine_officeshow_3
    elif jasmine.officeshow_count == 2:
      call jasmine_officeshow_2 from _call_jasmine_officeshow_2
    elif jasmine.officeshow_count == 1:
      call jasmine_officeshow_1 from _call_jasmine_officeshow_1
    elif jasmine.officeshow_count == 0:
      call jasmine_officeshow_0 from _call_jasmine_officeshow_0

    # If the temporary counter is still 1, an actual action was performed - end the day.
    if jasmine.officeshow_tempcount == 1:
      $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
      $ jasmine.officeshow_tempcount = 0
      change player energy by -energy_short
      call character_location_return(jasmine) from _call_character_location_return_313
      end_day
  return

# Office Show 0
label jasmine_officeshow_0:
  wt_image jasmine.image
  player.c  "[jasmine.name], I'd like to talk to you about your work. You said you've thought about the idea of exposing yourself in the office?"
  jasmine.c "Yes. It's crazy, I know, but I think about it all the time."
  player.c  "What is it that appeals to you?"
  jasmine.c "The complete inappropriateness of it. The danger that someone could see me."
  player.c  "Do you want someone to see you?"
  jasmine.c "In the office?  No.  No.  Oh my god. Think about the office gossip. What would everyone think about me? Or say about me? And I'd lose my job for sure."
  player.c  "So you want to be naked in the office, when people are around, but you don't want anyone to see you. You just want there to be a chance that someone could see you."
  jasmine.c "Yes, that's it exactly. Pretty stupid, huh?"
  $ title = "How do you respond?"
  menu:
    "Incredibly stupid":
      player.c  "Yes, incredibly stupid. Fantasies are one thing, real life is something else. You don't want to ruin your career or reputation messing around at your workplace."
      player.c  "You can masturbate to the idea of getting naked at work anytime you like, but I want you to put the idea of actually taking your clothes off in the office out of your head. Do you understand?"
      jasmine.c "Yes, I understand.  You're right."
      change jasmine submission by 10
      change jasmine resistance by -10
      $ jasmine.officeshow_tempcount = 0
      add tags 'shut_off_officeshow' to jasmine
    "Not stupid, but very dangerous.":
      player.c  "Not stupid, no, but very dangerous.  To have the risk of being caught there has to be just that - risk."
      player.c  "Is this urge important enough to you to risk your career and your reputation?"
      jasmine.c "I... I don't know.  Do you think I could do it, safely?"
      player.c  "If you're careful, yes, and don't let yourself get carried away, you should be able to do it without getting caught."
      player.c  "If you want the thrill of the risk, however, you will have to accept that you may get caught.  And have to pay the consequences that come with that."
      player.c  "Do you think you want to try?"
      "Jasmine thinks for a moment."
      jasmine.c "Perhaps I could think about it, and we can discuss more next week?"
      "You nod.  Choose another course of action for today."
      $ jasmine.officeshow_tempcount = 2
      $ jasmine.officeshow_count = 1
  return

# Office Show 1
label jasmine_officeshow_1:
  wt_image jasmine.image
  player.c  "[jasmine.name], have you thought more about the idea of exposing yourself in the office?"

  # If she has exposed herself elsewhere
  if jasmine.publicshow_level > 0:
    jasmine.c "I have.  I think I want to try it."
    player.c "You're willing to take the risk of getting caught?"
    jasmine.c "Yes ... yes, I am."
    player.c "Okay, but I don't want you to get caught. So I want you to do this in your office, when you're alone, and there's no reason to expect anyone to walk in on you."
    player.c "Don't get completely naked. Make sure you can quickly pull your clothes back together if someone drops by."
    "She nods."
    player.c "Do it tomorrow morning."
    player.c "If you're feeling brave, you can take some pictures of yourself to show me.  A way to make it more real, and a memento you can look back on later, if you want."
    player.c "Check in with me once you're done."
    wt_image exhi_office_1_1
    "The next morning, [jasmine.name] fills you in as promised. She even sets up the webcam on her computer to take some pictures for you."
    wt_image exhi_office_1_2
    "She pulls down the top of her dress before starting in on her paperwork."
    wt_image exhi_office_1_3
    "When the phone rings, she picks it up and has a conversation with her colleague, her breasts bare the whole time."
    jasmine.c "{i}That is one of the most amazing experiences I have ever had!{/i}"
    change jasmine desire by 10
    change jasmine sos by 10
    $ jasmine.officeshow_count = 2

  # If she has not yet exposed herself in public
  else:
    jasmine.c "I've thought about it, but I don't think I'm ready to try just yet."
    "Perhaps if she had more experience exposing herself in another environment, she might be open to trying it at work.  For today, choose another action."
    $ jasmine.officeshow_tempcount = 2
  return

# Office Show 2
label jasmine_officeshow_2:
  wt_image jasmine.image
  player.c  "[jasmine.name], are you ready to get naked at your office again?"
  jasmine.c "I was hoping you would suggest that!"
  player.c  "Same deal as last time. Only in your office and only when you're not expecting anyone else."
  player.c  "If you're feeling brave, you could expose your pussy this time, but make sure you're able to quickly cover yourself if someone comes by."
  wt_image exhi_office_2_1
  "The next morning, [jasmine.name] lets you know what she's done and shares more pictures with you.  She starts by climbing up on her desk."
  wt_image exhi_office_2_2
  "Then she spreads her legs.  She would've been safer doing this sitting in her chair, rather than on the desk, but she's clearly excited at her own boldness."
  wt_image exhi_office_2_3
  "Next she pulls her panties aside, giving the camera a good view of her pussy."
  wt_image exhi_office_2_4
  "Then to your shock, she pulls off her dress and leans back naked on her desk."
  jasmine.c "{i}You have no idea how amazing that felt!{/i}"
  player.c  "{i}And you seem to have no idea how much risk you took. If someone had walked in, you would never have been able to cover yourself up.{/i}"
  jasmine.c "{i}I know, but that's part of what made it so exciting!{/i}"
  change jasmine desire by 10
  change jasmine sos by 10
  $ jasmine.officeshow_count = 3
  return

# Office Show 3+
label jasmine_officeshow_3:
  # TODO: Remove location bonuses.
  wt_image jasmine.image
  player.c  "Are you ready to try exposing yourself in the office again?"
  jasmine.c "Yes, I am. But I don't want to stay in my office. I'd really like to expose myself in the public area of the office."
  $ title = "What do you tell her?"
  menu:
    "No, stick to somewhere private":
      "The next day, [jasmine.name] reports in on how she did."
      wt_image exhi_office_3_8
      "She found a board room that wasn't being used. To your surprise, she brought her laptop and set it up to take a webcam photos to share with you."
      wt_image exhi_office_3_1
      "Provocatively, she spreads her legs for the camera ..."
      wt_image exhi_office_3_2
      "... then pulls down her pants and turns around to let you get a good view of her bottom."
      wt_image exhi_office_3_3
      "You're not sure how she'll get her pants back on quickly if someone else enters the room, but [jasmine.name] doesn't seem concerned.  She pulls up her top ..."
      wt_image exhi_office_3_4
      "... and removes the rest of her clothes."
      wt_image exhi_office_3_5
      "As if to prove that she really is completely naked in her office boardroom, she lifts her leg to get a photo of her bare pussy."
      wt_image exhi_office_3_6
      "Then she climbs up on the boardroom table ..."
      wt_image exhi_office_3_7
      "... and poses there smiling while the webcam captures the moment."
      player.c  "{i}How would you have covered yourself up in time if someone had entered the room?{/i}"
      jasmine.c "{i}I couldn't have. That's what made it so exciting! I was so wet I was dripping pussy juice all over the table.{/i}"

      # 3rd Office Show
      if jasmine.officeshow_count == 3:
        change jasmine desire by 10
        change jasmine sos by 10
        $ jasmine.officeshow_count = 4
      # 4th+ Office Show
      else:
        "[jasmine.name] is still enjoying exposing herself in the office.  The novelty, however, is starting to wear off."
        change jasmine desire by 5

    "Okay, but be very careful":
      wt_image exhi_office_4_1
      "[jasmine.name] is unable to set up her laptop to take webcam photos in the common area of the office. You piece together what happens the next morning from what she tells you later that day."
      wt_image exhi_office_4_2
      "{i}[jasmine.name] takes up position outside of a common filing area, and lowers her top.{/i}"
      wt_image exhi_office_4_3
      "{i}She pulls up her skirt ...{/i}"
      wt_image exhi_office_4_4
      "{i}... and flaunts her bare bottom.{/i}"

      # TODO: RAGS has a note here that specifies "don't use CalcDesire" - Should this be handled differently?  ## Yes, by testing against raw score instead of using the 'test' function
      #if jasmine.test( 'desire',55):
      if jasmine.desire > 55:
        wt_image exhi_office_4_6
        "{i}Then the excitement of the moment overwhelms her. She strips her clothes off and starts touching herself.{/i}"
        wt_image exhi_office_4_15
        "{i}She hears her colleague approaching, but she doesn't have enough time. She grabs her clothes and ducks behind the desk. He finds her there, trying to get back into her clothes.{/i}"
        wt_image exhi_office_4_7
        coworker_rob "[jasmine.name]! What are you doing?"
        wt_image exhi_office_4_8
        "{i}[jasmine.name] scrambles back into her clothes.{/i}"
        jasmine.c "Please, Rob?  Don't tell anybody."
        coworker_rob "What are you doing running around naked in the office?"
        jasmine.c "You wouldn't believe me if I told you. Just don't say anything, okay? I'd die of embarrassment."
        "{i}If [jasmine.name] had been lucky, her coworker would have been a nice guy. She wasn't lucky.{/i}"
        coworker_rob "I'll keep quiet, [jasmine.name], but only if you keep me happy."
        jasmine.c "Rob?  What do you mean?"
        wt_image exhi_office_4_17
        coworker_rob "You know very well what I mean.  Use your mouth for something more useful than asking stupid questions."
        wt_image exhi_office_4_9
        "{i}Rob almost lets himself be carried away.{/i}"
        wt_image exhi_office_4_10
        "{i}Then, remembering they're still in a public part of the office, he leads [jasmine.name] to a boardroom that's not in use.{/i}"
        wt_image exhi_office_4_11
        "{i}If [jasmine.name] had hoped to get away with just a blow job, she soon learns otherwise.{/i}"
        wt_image exhi_office_4_12
        "{i}Rob has her in an awkward spot, and he's determined to take advantage of her predicament.{/i}"
        wt_image exhi_office_4_13
        jasmine.c "{i}I don't know what to do. I can't tell my husband.  I don't know how easily I can find another job.{/i}"
        wt_image exhi_office_4_16
        jasmine.c "{i}I do know this, however.  I can't see you again.  Not while I try and figure this out.  Until I can get out from underneath this, I'm Rob's bitch now.{/i}"
        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unvailable'
        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
        call convert(jasmine, "unavailable") from _call_convert_24
      else:
        wt_image exhi_office_4_14
        "{i}She hears a colleague coming and quickly ducks behind the desk. She pulls herself together and tries to look innocent.{i}"
        coworker_rob "Oh.  Hi, [jasmine.name].  What are you doing out here?"
        wt_image exhi_office_4_5
        jasmine.c "Just checking some paperwork. Is this the file you were looking for?"
        coworker_rob "Yes. Thanks."
        # 3rd Office Show
        if jasmine.officeshow_count == 3:
          jasmine.c "{i}It was one of the most exciting moments of my life!{/i}"
          change jasmine desire by 10
          change jasmine sos by 15
          $ jasmine.officeshow_count = 4
        # 4th+ Office Show
        else:
          "The more she exposes herself in the office, the less impact it has on her psyche. She's still getting quite a rush out of the experience, though."
          change jasmine desire by 5
          change jasmine sos by 10
  return

# Private Show
label jasmine_privateshow:
  $ jasmine.privateshow_energy = 0     # No energy use, by default.
  wt_image jasmine.image
  if jasmine.privateshow_count == 3:
    call jasmine_privateshow_3 from _call_jasmine_privateshow_3
  elif jasmine.privateshow_count == 2:
    call jasmine_privateshow_2 from _call_jasmine_privateshow_2
  elif jasmine.privateshow_count == 1:
    call jasmine_privateshow_1 from _call_jasmine_privateshow_1
  else:
    call jasmine_privateshow_0 from _call_jasmine_privateshow_0

  # If the privateshow_energy is not 0, an actual action was performed - end the day.
  if jasmine.privateshow_energy > 0:
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    change player energy by -jasmine.privateshow_energy notify
    call character_location_return(jasmine) from _call_character_location_return_314
    end_day

  return

# Private Show 0
label jasmine_privateshow_0:
  player.c  "[jasmine.name], I'd like you to practice exposing yourself by flashing me."
  jasmine.c "You?"
  player.c  "Yes, me.  Here.  Now."
  if jasmine.test('resistance', 40) or jasmine.test('desire', 60) or jasmine.test('submission', 20):
    wt_image exhi_private_show_1
    "For a moment it looks like [jasmine.name] is going to protest. Then she starts sliding her sweater off her shoulders."
    wt_image exhi_private_show_2
    "She grasps the front of her blouse ..."
    wt_image exhi_private_show_3
    "... and pulls it down, offering you a view of her spectacular breasts.  She watches you, uncertainty playing across her face as she waits for your reaction."
    player.c  "Very good, [jasmine.name]. And very nice.  How does it feel now?  Sitting here, exposing yourself to me."
    jasmine.c "Strangely ... right and yet completely and totally wrong at the same time."
    player.c  "And your cunt, Jasmine?  Tell the truth.  How does it feel?"
    "She glares at you, pissed at you for knowing and for making her say it."
    jasmine.c "Wet"
    player.c  "So you're wet and I'm hard, and you're getting your first taste of flashing a man in his own house. Maybe you could drop the skank face and enjoy the moment?"
    wt_image exhi_private_show_4
    "[jasmine.name] laughs.  It's nice to see her smile."
    jasmine.c "I guess.  Actually, this does feel kind of nice... and still oh so completely wrong.  Can I cover up and go?  I think that took about everything I had for today."
    "You nod."
    $ jasmine.privateshow_count = 1
    $ jasmine.privateshow_energy = energy_long.value
    change jasmine sos by 10
  else:
    jasmine.c "I don't know. That seems kinda ... intimate.  Me just showing you my tits here at your place.  It feels more like ... I don't know, not really exposing myself like being out in public would."
    "If her resistance was lower, she might go along with your instruction, but not now."
    $ title = "What do you do?"
    menu:
      "Chastise her":
        call jasmine_privateshow_chastise from _call_jasmine_privateshow_chastise
      "Leave it be it be and choose another action":
        call jasmine_privateshow_leaveit from _call_jasmine_privateshow_leaveit
  return

# Private Show 1
label jasmine_privateshow_1:
  player.c  "[jasmine.name], I'd like you to practice exposing yourself to me."
  jasmine.c "Again?"
  player.c  "Yes"
  wt_image exhi_private_show_4
  "[jasmine.name] shrugs and smiles, then removes her top."
  jasmine.c "Now what?"
  player.c  "Now you pull up your dress and show me your pussy."
  if jasmine.test( 'resistance', 30) or jasmine.test('desire', 70) or jasmine.test('submission', 30):
    wt_image exhi_private_show_5
    "For a moment you're not sure if [jasmine.name] is going to comply or not.  Then she starts to lift her skirt."
    wt_image exhi_private_show_6
    "She slips out of her panties.  Smiling, she turns around and lifts a leg, giving you as close to an up-the-skirt peek shot as she can in the circumstances."
    jasmine.c "Is this what you were hoping to see?"
    player.c  "It is.  Very nice, [jasmine.name]."
    player.c  "And how does it feel to you, letting me sneak a peek at your cute little pussy?"
    jasmine.c "Still completely wrong.  And deliciously right at the same time.  And don't bother asking me if I'm wet.  I know damn well that you can see that I am."
    "You chuckle and make her stay in that position for a few minutes, before sending her home feeling oddly satisfied by the experience."
    $ jasmine.privateshow_count = 2
    $ jasmine.privateshow_energy = energy_long.value
    change jasmine sos by 10
  else:
    jasmine.c "I don't know. With just you and me here at your place, it doesn't feel right."
    "Either lower her resistance, increase her desire, or increase her submission before trying again."
    $ title = "What do you do?"
    menu:
      "Chastise her":
        call jasmine_privateshow_chastise from _call_jasmine_privateshow_chastise_1
      "Leave it be":
        call jasmine_privateshow_leaveit from _call_jasmine_privateshow_leaveit_1
  return

# Private Show 2
label jasmine_privateshow_2:
  player.c  "[jasmine.name], I'd like you to expose yourself to me."
  jasmine.c "Again?"
  player.c  "Yes"
  wt_image exhi_private_show_6
  "[jasmine.name] stands up, removes her panties, and lifts her dress."
  jasmine.c "Like this?"
  player.c  "No.  Turn around and give me a better view."
  wt_image exhi_private_show_7
  "[jasmine.name] giggles and turns around."
  jasmine.c "Is this better?"
  player.c  "Yes.  Now, start touching yourself."
  if jasmine.test('resistance', 25) or jasmine.test('desire', 80) or jasmine.test('submission', 40):
    wt_image exhi_private_show_8
    "[jasmine.name] looks ready to protest, when her finger slips inside.  [jasmine.name] seems surprised herself, as if her body has betrayed her."
    "For the next few minutes you stay like that, you watching her masturbate, her watching you watching her, neither of you saying anything."
    $ jasmine.privateshow_count = 3
    $ jasmine.privateshow_energy = energy_long.value
    change jasmine sos by 5
    change jasmine desire by 5
    change jasmine submission by 5
    $ title = "What do you do?"
    menu:
      "End things there":
        "It's tempting to cross the line with [jasmine.name], but the deal with her husband was no funny business.  You're not ready to break that, at least not now."
        change jasmine resistance by -5
      "Tell her it's your turn":
        if jasmine.sex_level > 0 or jasmine.test('submission', 50) or jasmine.test('desire', 90) or jasmine.test('resistance',15):
          call jasmine_privateshow_sex from _call_jasmine_privateshow_sex
        else:
          jasmine.c "No.  No, we can't do that.  I promised my husband."
          "You could try again when her resistance is lower, or her submission or desire is higher. But not today. She dresses and leaves, a little upset about your suggestion, but not so upset that she won't come back."
          change jasmine resistance by 5
  else:
    jasmine.c "Whoa ... I'm not sure. I get it. That would be hot ... me touching myself while a stranger watches me.  But with just you and me here at your place ... it doesn't feel right."
    $ title = "What do you do?"
    menu:
      "Chastise her":
        call jasmine_privateshow_chastise from _call_jasmine_privateshow_chastise_2
      "Leave it be.":
        call jasmine_privateshow_leaveit from _call_jasmine_privateshow_leaveit_2
  return

# Private Show 3
label jasmine_privateshow_3:
  "[jasmine.name]'s exhibitionist desires are unlikely to be cultivated by more private shows, although there may be something else you want her to get out of them."
  $ title = "What do you do?"
  menu:
    "Choose a different action":
      pass
    "Continue with private show":
      player.c  "Take off your clothes and masturbate while I watch you, [jasmine.name]."
      wt_image exhi_private_show_8
      "She just nods and does as you say."
      $ jasmine.privateshow_energy = energy_short.value  # Have now used short energy
      $ title = "What do you do?"
      menu:
        "End things there":
          "It's tempting to cross the line with [jasmine.name], but the deal with her husband was no funny business. You're not ready to break that, at least not now."
        "Tell her it's your turn":
          if jasmine.sex_level > 0 or jasmine.test('submission', 50) or jasmine.test('desire', 90) or jasmine.test('resistance', 10):
            call jasmine_privateshow_sex from _call_jasmine_privateshow_sex_1
          else:
            jasmine.c "No.  No, we can't do that.  I promised my husband."
            "You could try again when her resistance is lower, or her submission or desire is higher.  But not today.  She dresses and leaves, a little upset about your suggestion, but not so upset that she won't come back."
            change jasmine resistance by 5 notify
  return

# Private Show - Chastise Her
label jasmine_privateshow_chastise:
  "[jasmine.name] may not be into D/s stuff, but she responds surprisingly strongly to being scolded. You remind her of the reason why she is here and the need for her to follow your instructions.  You may not get her to change her mind for today, but hopefully you've laid the groundwork for increased obedience in the future."
  $ jasmine.privateshow_energy = energy_short.value
  change jasmine submission by 5
  change jasmine resistance by -5
  return

# Private Show - Leave It Be
label jasmine_privateshow_leaveit:
  pass
  return

# Private Show - Sex
label jasmine_privateshow_sex:
  # Sex level 2
  if jasmine.sex_level == 2:
    player.c  "Time to pleasure me, [jasmine.name]."
    jasmine.c "If that's what you want.  How do you want me?"
    $ title = "What do you tell her?"
    menu:
      "Come here and blow me":
        wt_image exhi_private_show_13
        "[jasmine.name] seems happy to comply."
        wt_image exhi_private_show_14
        "A few minutes later you deposit your load down the back of her throat."
        player.c "[player.orgasm_text]"
        $ jasmine.blowjob_count += 1
        $ jasmine.swallow_count += 1
      "Climb up on me":
        wt_image exhi_private_show_15
        "[jasmine.name] seems happy to comply."
        wt_image exhi_private_show_16
        "A few minutes later she rides herself... and then you... to orgasm."
        jasmine.c "ooohhhhh!!!"
        player.c "[player.orgasm_text]"
        $ jasmine.sex_count += 1
        $ jasmine.orgasm_count += 1
    change jasmine submission by 5
    change jasmine resistance by -5
    orgasm

  # Sex level 1
  elif jasmine.sex_level == 1:
    # Has already given a handjob
    if jasmine.handjob_given == 1:
      player.c  "Time to pleasure me, [jasmine.name]."
      jasmine.c "Do you want me to jerk you off again?"
      $ title = "What do you tell her?"
      menu:
        "Yes, jerk me off":
          call jasmine_privateshow_sex_handjob from _call_jasmine_privateshow_sex_handjob
        "No, spread your legs":
          call jasmine_privateshow_sex_sex from _call_jasmine_privateshow_sex_sex
    else:
      player.c  "It's my turn now, [jasmine.name]."
      "She trembles as she understands your meaning, but doesn't object."
      jasmine.c "What ... what do you want me to do?"
      $ title = "What do you tell her?"
      menu:
        "Jerk me off":
          call jasmine_privateshow_sex_handjob from _call_jasmine_privateshow_sex_handjob_1
        "Spread your legs":
          call jasmine_privateshow_sex_sex from _call_jasmine_privateshow_sex_sex_1

  # Sex level 0
  else:
    player.c "It's my turn now, Jasmine."
    "She trembles as she understands your meaning, but doesn't object."
    jasmine.c "What ... what do you want me to do?"
    player.c "Touch me, to start."
    wt_image exhi_private_show_9
    "Jasmine's not displeased with what she finds.  As she strokes you in her soft hand, you know it won't take you long to climax."
    change jasmine submission by 15
    change jasmine resistance by -10
    $ jasmine.sex_level = 1
    $ jasmine.handjob_given = 1
    $ jasmine.handjob_count += 1
    call jasmine_privateshow_sex_cum from _call_jasmine_privateshow_sex_cum

  return

# Private Show - Sex - Handjob
label jasmine_privateshow_sex_handjob:
  wt_image exhi_private_show_9
  "[jasmine.name] seems happy to comply."
  $ jasmine.handjob_count += 1
  $ jasmine.handjob_given = 1
  change jasmine submission by 5
  change jasmine resistance by -5
  call jasmine_privateshow_sex_cum from _call_jasmine_privateshow_sex_cum_1
  return

# Private Show - Sex - Sex
label jasmine_privateshow_sex_sex:
  wt_image exhi_private_show_11
  "[jasmine.name] does as you say."
  "She keeps her head turned away from you as you enter her.  Despite not looking at you, her cunt is wet and ready for you."
  wt_image exhi_private_show_12
  "[jasmine.name] tries to keep up a steely exterior, but it's a struggle. Her fists clench and she bites her lip to try to avoid crying out as her body betrays her and responds to the situation and the feel of your body against and inside her."
  "Her betrayal of her husband complete, she gathers her clothes and leaves without saying a word. She's disappointed in herself, but you're sure she'll be back."
  $ jasmine.sex_count += 1
  change jasmine submission by 10
  change jasmine resistance by -10
  $ jasmine.sex_level = 2
  orgasm
  return

# Private Show - Sex - Cum
label jasmine_privateshow_sex_cum:
  $ title = "Where do you want to cum?"
  menu:
    "In her mouth":
      wt_image exhi_hypno_bj_4
      "[jasmine.name] wraps her lips around your cock and keeps them there as you pump your seed into her mouth."
      player.c "[player.orgasm_text]"
      "Silently she swallows down every drop."
      $ jasmine.swallow_count += 1
    "On her face":
      wt_image exhi_private_show_10
      "[jasmine.name] watches as your seed spurts up and onto her face.  Perhaps instinctively, she opens her mouth to catch some of your cum as the rest drips down her chin and onto the floor."
      player.c "[player.orgasm_text]"
      $ jasmine.facial_count += 1
  orgasm
  "Embarrassed by what she's just done and perhaps disappointed with herself for cheating on her husband, [jasmine.name] heads home."
  return

## Post-Training Character Actions
# Girlfriend Hypno Actions
# note: not needed as hypno action is automatically available and GF content is included in core action
#label jasmine_gf_hypno:
#  return

# Girlfriend Actions
label jasmine_gf_actions:
    if current_location == bedroom:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        $ jasmine.gf_outfit_count += 1
        if jasmine.gf_outfit_count > 6:
            $ jasmine.gf_outfit_count = 1
        if jasmine.gf_outfit_count == 1:
            call forced_movement(outdoors) from _call_forced_movement_556
            summon jasmine
            wt_image exhi_gf_outfit_1_1
            "You take Jasmine out to dinner to celebrate your relationship."
            wt_image exhi_gf_outfit_1_2
            "Afterwards, she leans over and gives you a kiss."
            wt_image exhi_gf_outfit_1_28
            jasmine.c "Thanks.  This was lovely."
            $ title = "What do you tell her?"
            menu:
                "You're welcome":
                    $ jasmine.temporary_count = 2
                    player.c "You're welcome."
                    "You kiss her good-bye, and go on with your day."
                    change player energy by -energy_very_short notify
                    call forced_movement(bedroom) from _call_forced_movement_557
                "We're not done yet":
                    player.c "We're not done yet."
                    wt_image exhi_gf_outfit_1_1
                    jasmine.c "We aren't?"
                    player.c "No.  Stand up."
                    wt_image exhi_gf_outfit_1_3
                    "As she stands up, you pull her top down, exposing one breast."
                    jasmine.c "People can see us!"
                    player.c "I know.  You like that, don't you?"
                    jasmine.c "Yes"
                    $ title = "What now?"
                    menu:
                        "End the date":
                            $ jasmine.temporary_count = 3
                            player.c "Should I cover you back up, or do you want to walk home like this?"
                            wt_image exhi_gf_outfit_1_29
                            jasmine.c "What do you think?"
                            change player energy by -energy_short notify
                            call forced_movement(bedroom) from _call_forced_movement_558
                        "Pleasure her":
                            $ jasmine.temporary_count = 4
                            wt_image exhi_gf_outfit_1_5
                            jasmine.c "What are you doing?"
                            player.c "Thanking you for being my girlfriend."
                            jasmine.c "People can see you!"
                            player.c "I know."
                            wt_image exhi_gf_outfit_1_6
                            "You lean over and take her stiffening nipple into your mouth as she looks around to see who's watching her get her tit sucked."
                            "Soon it's not just her nipple, but her whole body that's stiffening up."
                            jasmine.c "oooo  ...  ooooo  ...  oooohh!!"
                            wt_image exhi_gf_outfit_1_4
                            jasmine.c "Wow, that was ... surprising! I never thought I could cum just from having my nipple sucked."
                            player.c "Was it just from having your nipple sucked?"
                            jasmine.c "Hmmm ... maybe having our waitress give me the dirty eye the whole time had something to do with it."
                            player.c "She was probably just jealous.  Question is, was she jealous of you, or me?"
                            jasmine.c "Ha!"
                            $ jasmine.orgasm_count += 1
                            change player energy by -energy_long notify
                            call forced_movement(bedroom) from _call_forced_movement_559
                        "Have her thank you properly":
                            $ jasmine.temporary_count = 4
                            player.c "If you'd like to thank me properly for the dinner, now's the time."
                            wt_image exhi_gf_outfit_1_4
                            jasmine.c "Here?  With a restaurant full of people watching me?"
                            player.c "Yes"
                            wt_image exhi_gf_outfit_1_7
                            "She drops to her knees and takes out your cock, looking around to see who's watching her ..."
                            wt_image exhi_gf_outfit_1_8
                            "... before taking you into her mouth."
                            wt_image exhi_gf_outfit_1_9
                            "She keeps her eyes on you as she sucks you, but holds her bare tit out towards the restaurant staff and patrons, giving those who want to watch a good view of her ..."
                            wt_image exhi_gf_outfit_1_10
                            "... as you fill her mouth with your seed."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_gf_outfit_1_30
                            player.c "Finish drinking your dessert, then we'll get out of here, okay?"
                            jasmine.c "Mmm hmmm"
                            wt_image exhi_gf_outfit_1_11
                            "[jasmine.name] milks the last of the sperm out of your balls, a happy, glazy look on her face, as your waitress tries not to stare as she brings your bill."
                            $ jasmine.blowjob_count += 1
                            $ jasmine.swallow_count += 1
                            orgasm notify
                            call forced_movement(bedroom) from _call_forced_movement_560
                "Let's continue this at home":
                    player.c "Let's continue this at home, [jasmine.name]."
                    wt_image exhi_gf_outfit_1_1
                    jasmine.c "Oh?  What are we going to do there?"
                    $ title = "What are you going to do at home?"
                    menu:
                        "Watch some TV":
                            $ jasmine.temporary_count = 3
                            player.c "I thought we could watch some TV together?"
                            jasmine.c "Okay, sure.  That sounds nice."
                            wt_image exhi_visit_fj_1
                            call forced_movement(living_room) from _call_forced_movement_561
                            summon jasmine
                            "The two of you have a nice time on the sofa together after you get home."
                            change player energy by -energy_short notify
                        "Massage her":
                            player.c "I thought I might give you a massage."
                            jasmine.c "Okay.  That sounds nice."
                            call forced_movement(bedroom) from _call_forced_movement_562
                            summon jasmine
                            wt_image exhi_gf_outfit_1_12
                            "When you get home, Jasmine lies down and removes her top."
                            $ title = "What do you want to massage?"
                            menu:
                                "Just her back":
                                    $ jasmine.temporary_count = 3
                                    jasmine.c "Mmmmm.   That feels nice.  Thank you."
                                    player.c "You're welcome."
                                    "After rubbing her back for a little while, you get on with your day."
                                    change player energy by -energy_short notify
                                "Between her legs":
                                    $ jasmine.temporary_count = 4
                                    jasmine.c "Mmmmm.   That feels nice.  Thank you."
                                    player.c "I think I can make it feel even better.  Roll over."
                                    wt_image exhi_gf_outfit_1_13
                                    "As she rolls over, you rub your fingers over and into her wettening pussy."
                                    jasmine.c "oooo ... you're right, that does feel even better."
                                    wt_image exhi_gf_outfit_1_14
                                    player.c "What about this?  Better still?"
                                    "You lower your mouth and gently lick away the juices that flow out of her."
                                    jasmine.c "ooooo .... oooo, yes, that's even better!"
                                    wt_image exhi_gf_outfit_1_15
                                    "Her body agrees, and you're soon rewarded for your efforts with a flood of liquid from her pussy."
                                    jasmine.c "oooo  ...  oooohh!!"
                                    "[jasmine.name] seems quite happy with your date."
                                    $ jasmine.orgasm_count
                                    change player energy by -energy_long notify
                        "Fuck her":
                            player.c "I'm going to fuck you."
                            jasmine.c "Mmmm.   Then I guess we should settle up our bill and get going."
                            call forced_movement(bedroom) from _call_forced_movement_563
                            summon jasmine
                            wt_image exhi_gf_outfit_1_16
                            "As soon as you get home, you tackle her."
                            wt_image exhi_gf_outfit_1_17
                            "It doesn't take long for her to get wet.  You pound into her, harder and harder as she moans."
                            jasmine.c "oooo"
                            wt_image exhi_gf_outfit_1_18
                            jasmine.c "oooo  ...   that feels good!"
                            "She's enjoying this, but she's having a harder time than you getting ready to cum."
                            $ title = "What do you do?"
                            menu:
                                "Cum":
                                    $ jasmine.temporary_count = 2
                                    wt_image exhi_gf_outfit_1_19
                                    "You can't hold out any longer.  You thrust into her ... hard, harder, harder ... and empty your load inside her as she groans."
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_gf_outfit_1_16
                                    jasmine.c "oooo  ...  I'm glad that felt good for you."
                                    $ jasmine.sex_count += 1
                                    orgasm notify
                                "Wait for her to finish":
                                    $ jasmine.temporary_count = 4
                                    wt_image exhi_gf_outfit_1_20
                                    "You adjust your thrusts to a steady, rhythmic pace that her body seems to respond to and try to think about something ... anything ... besides how sexy her tits look bouncing back and forth as you thrust into her ..."
                                    jasmine.c "ooooo"
                                    wt_image exhi_gf_outfit_1_16
                                    "about something ... anything ... besides how pretty Jasmine is lying there as you fuck her ..."
                                    jasmine.c "oooooo"
                                    wt_image exhi_gf_outfit_1_18
                                    "about something ... anything ... besides how good her wet, warm cunt feels around your cock ..."
                                    jasmine.c "ooooooo"
                                    wt_image exhi_gf_outfit_1_20
                                    "... about something ... anything ... besides ..."
                                    wt_image exhi_gf_outfit_1_21
                                    jasmine.c "oooo  ...  oooohh!!"
                                    "Oh thank goodness she finally came!!  Which means you can, too."
                                    wt_image exhi_gf_outfit_1_19
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_gf_outfit_1_21
                                    jasmine.c "mmmmm ... thanks for waiting for me!"
                                    orgasm
                                    $ jasmine.sex_count += 1
                                    $ jasmine.orgasm_count += 1
                                    change player energy by -energy_short notify
                        "Do her from behind":
                            $ jasmine.temporary_count = 3
                            player.c "I'm going to put you on your knees and fuck you hard from behind, doggy-style."
                            jasmine.c "Mmmm.   Then I guess we should settle up our bill and get going."
                            call forced_movement(bedroom) from _call_forced_movement_564
                            summon jasmine
                            wt_image exhi_gf_outfit_1_22
                            "As soon as you get home, Jasmine, strips and kneels down on the bed, presenting herself to you.  She smiles back at you as you get into position behind her."
                            jasmine.c "Does my boyfriend like me like this?"
                            player.c "You know I do."
                            wt_image exhi_gf_outfit_1_23
                            "Gripping her firmly by the hips, you push into her as she moans."
                            jasmine.c "oooo"
                            wt_image exhi_gf_outfit_1_24
                            "You thrust into her ... harder and harder ... as she starts to tremble."
                            jasmine.c "ooooo  ...  ooooooo"
                            wt_image exhi_gf_outfit_1_25
                            "A moment later she cums, her cunt spasming around your cock."
                            jasmine.c "oooo  ...  oooohh!!"
                            "Now it's your turn."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image exhi_gf_outfit_1_24
                                    "You thrust into her hard - once, twice, three times .... and empty your load."
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_gf_outfit_1_26
                                    jasmine.c "Mmmm.  Thanks for the great date."
                                "On her":
                                    wt_image exhi_gf_outfit_1_27
                                    "You pull out and pump your load up and over her back and ass."
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_whore_1_34
                                    jasmine.c "Mmmmm.  Thanks for the great date."
                            $ jasmine.sex_count += 1
                            $ jasmine.orgasm_count += 1
                            orgasm notify
        elif jasmine.gf_outfit_count == 2:
            $ jasmine.temporary_count = 0
            wt_image exhi_gf_portrait
            "You find Jasmine just leaving the bedroom."
            jasmine.c "Hi"
            wt_image exhi_gf_outfit_2_1
            jasmine.c "Why are you looking at me like that?  Did you want something?"
            $ title = "Did you want something?"
            menu menu_jasmine_gf_outfit_2:
                "Just a kiss" if jasmine.temporary_count == 0:
                    $ jasmine.temporary_count = 2
                    player.c "Just a kiss from my girl."
                    wt_image exhi_gf_outfit_2_2
                    jasmine.c "Really?  You're looking at me like that and just thinking about kissing me?"
                    jasmine.c "You know, sometimes you can be kinda ... sweet."
                    wt_image exhi_gf_outfit_2_3
                    "She leans in and gives you a big kiss, then let's you go on with your day."
                    # note: no energy cost
                "Just to look at her" if jasmine.temporary_count == 0:
                    $ jasmine.temporary_count = 3
                    player.c "I just want to look at you."
                    wt_image exhi_gf_outfit_2_2
                    jasmine.c "Really?  Well, in that case, I guess I should give you something interesting to look at."
                    wt_image exhi_gf_outfit_2_18
                    "She lies down ..."
                    wt_image exhi_gf_outfit_2_19
                    "... then rolls over ..."
                    wt_image exhi_gf_outfit_2_20
                    "... making sure you get a good look under her dress ..."
                    wt_image exhi_gf_outfit_2_21
                    "... and between her legs."
                    wt_image exhi_gf_outfit_2_22
                    "She looks back at you, smiling, enjoying this private moment exposing herself to you."
                    wt_image exhi_gf_outfit_2_23
                    "After a moment, she sits up and grins."
                    jasmine.c "Enjoy your day!"
                    wt_image exhi_gf_outfit_2_24
                    "Then she flashes her tits at you and disappears."
                    change player energy by -energy_very_short
                "Blow job":
                    $ jasmine.temporary_count = 2
                    player.c "I'd love a blow job."
                    wt_image exhi_gf_outfit_2_2
                    jasmine.c "Hmmm.  Okay, I could do that."
                    wt_image exhi_gf_outfit_2_4
                    "Jasmine pulls down her top ..."
                    wt_image exhi_gf_outfit_2_5
                    "... lowers herself to her knees ..."
                    wt_image exhi_gf_outfit_2_6
                    "... takes out your cock ..."
                    wt_image exhi_gf_outfit_2_7
                    "... and proceeds to give you a blow job ..."
                    wt_image exhi_gf_outfit_2_8
                    "... that culminates with you filling her mouth with jizz as she bobs her head up and down your spurting cock."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_gf_outfit_2_3
                    "Afterwards she leans up, kisses you tenderly, and disappears, leaving you to continue your day."
                    $ jasmine.blowjob_count += 1
                    $ jasmine.swallow_count += 1
                    orgasm notify
                "Tit job":
                    $ jasmine.temporary_count = 2
                    player.c "I'd love a tit job."
                    wt_image exhi_gf_outfit_2_2
                    jasmine.c "Hmmm.  Okay, I could do that."
                    wt_image exhi_gf_outfit_2_4
                    "Jasmine pulls down her top ..."
                    wt_image exhi_gf_outfit_2_5
                    "... lowers herself to her knees ..."
                    wt_image exhi_gf_outfit_2_6
                    "... takes out your cock ..."
                    wt_image exhi_gf_outfit_2_9
                    "... rubs it against her right tit ..."
                    wt_image exhi_gf_outfit_2_10
                    "... then her left tit ..."
                    wt_image exhi_gf_outfit_2_11
                    "... before plunging your shaft into the deep valley between her breasts and holding it there, milking it between her soft mounds ..."
                    wt_image exhi_gf_outfit_2_12
                    "... until you dump your load over those soft, waiting mounds."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_gf_outfit_2_3
                    "Afterwards she leans up, kisses you tenderly, and disappears, leaving you to continue your day."
                    $ jasmine.titfuck_count += 1
                    orgasm notify
                "Hand job":
                    $ jasmine.temporary_count = 2
                    player.c "I'd love a hand job."
                    wt_image exhi_gf_outfit_2_2
                    jasmine.c "Hmmm.  Okay, I could do that."
                    wt_image exhi_gf_outfit_2_4
                    "Jasmine pulls down her top ..."
                    wt_image exhi_gf_outfit_2_5
                    "... lowers herself to her knees ..."
                    wt_image exhi_gf_outfit_2_6
                    "... takes out your cock ..."
                    wt_image exhi_gf_outfit_2_13
                    "... and runs her nails along it, teasing you until your shaft is rock hard."
                    wt_image exhi_gf_outfit_2_14
                    "Then she applies lubricant to your dick ..."
                    wt_image exhi_gf_outfit_2_15
                    "... and starts pumping you ..."
                    wt_image exhi_gf_outfit_2_16
                    "... faster and faster ..."
                    wt_image exhi_gf_outfit_2_17
                    "... until you spurt, drenching her soft hand with your cum."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_gf_outfit_2_3
                    "Afterwards she leans up, kisses you tenderly, and disappears, leaving you to continue your day."
                    $ jasmine.handjob_count += 1
                    orgasm notify
                "Sex" if jasmine.temporary_count == 0:
                    player.c "I was thinking about how nice it would be to fuck you right now."
                    jasmine.c "Hmmmm. It's that time of the month, and I don't really like doing that now. Maybe I could do something else for you?"
                    $ jasmine.temporary_count = 1
                    jump menu_jasmine_gf_outfit_2
                "Pleasure her" if jasmine.temporary_count == 0:
                    player.c "I was thinking I'd like to show how much I appreciate having you as my girlfriend."
                    jasmine.c "Hmmmm. It's that time of the month, and as much as I love the thought, I don't really like doing that now. Maybe I could do something for you instead?"
                    $ jasmine.temporary_count = 1
                    jump menu_jasmine_gf_outfit_2
                "Never mind" if jasmine.temporary_count == 1:
                    player.c "No problem. I'll wait until you're in the mood."
                    jasmine.c "Okay.  I'm sure I'll be feeling like doing you again soon!"
        elif jasmine.gf_outfit_count == 3:
            player.c "[jasmine.name], let's go get something to eat.  "
            wt_image exhi_gf_outfit_3_1
            jasmine.c "Okay!  Is this dress okay?  It's not too revealing, is it?"
            player.c "Not at all."
            call forced_movement(outdoors) from _call_forced_movement_565
            summon jasmine
            wt_image exhi_gf_outfit_3_2
            "You find the perfect restaurant to take her to.  Dark enough that she appears respectable walking in and getting a table with you ..."
            wt_image exhi_gf_outfit_3_3
            "... bright enough that the waiter can't stop staring at Jasmine's nipples showing through her dress as he takes your order."
            call forced_movement(living_room) from _call_forced_movement_566
            summon jasmine
            wt_image exhi_gf_outfit_3_4
            "After the meal, Jasmine kisses kisses you passionately when you return home."
            jasmine.c "Thanks for the date."
            $ title = "What do you say?"
            menu:
                "You're welcome":
                    $ jasmine.temporary_count = 2
                    player.c "You're welcome. The waiter thanks you, too."
                    wt_image exhi_gf_outfit_3_16
                    "[jasmine.name] giggles."
                    jasmine.c "Maybe he should have given me a tip?"
                    change player energy by -energy_very_short notify
                "How about a thank you blow job?":
                    $ jasmine.temporary_count = 2
                    wt_image exhi_gf_outfit_3_17
                    player.c "How about a thank you blow job?"
                    wt_image exhi_gf_outfit_3_6
                    "You pull up the top of her dress and give her tits a squeeze."
                    jasmine.c "Mmmmm.  Okay."
                    wt_image exhi_gf_outfit_3_18
                    "she sits down and removes your pants ..."
                    wt_image exhi_gf_outfit_3_7
                    "... licks your cock hard ..."
                    wt_image exhi_gf_outfit_3_19
                    "... and proceeds to give you her thank you.  Before long, you're ready to give her something in return."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her mouth":
                            wt_image exhi_gf_outfit_3_9
                            "Gripping her firmly by the back of the neck, you hold her head in place as you start to cum."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_gf_outfit_3_8
                            "Her lips wrapped tightly around your cock head, she contentedly milks the last drops of cum from your balls."
                            jasmine.c "mmmm"
                            $ jasmine.swallow_count += 1
                        "On her tits":
                            wt_image exhi_gf_outfit_3_20
                            "Removing your cock from her mouth ..."
                            wt_image exhi_gf_outfit_3_10
                            "... you aim it at her chest ..."
                            wt_image exhi_gf_outfit_3_11
                            "... and empty your load on her exposed mounds."
                            player.c "[player.orgasm_text]"
                            jasmine.c "oooo"
                    wt_image exhi_gf_outfit_3_5
                    jasmine.c "I hope you liked your thank you."
                    "She gives you a hug, then leaves you to continue your day."
                    $ jasmine.blowjob_count += 1
                    orgasm notify
                "I want to fuck you":
                    $ jasmine.temporary_count = 3
                    wt_image exhi_gf_outfit_3_21
                    player.c "I want to fuck you."
                    wt_image exhi_gf_outfit_3_22
                    "You pull up the bottom of her dress and give her ass a squeeze."
                    jasmine.c "oooo ... okay"
                    wt_image exhi_gf_outfit_3_23
                    "Teasing the waiter at the restaurant has Jasmine turned on."
                    wt_image exhi_gf_outfit_3_15
                    "Her wet snatch opens eagerly to accept your hard cock, and she moans as you push inside her"
                    jasmine.c "ooooo"
                    wt_image exhi_gf_outfit_3_14
                    "You pound into her as her excitement and yours grows ..."
                    jasmine.c "ooooo  ...  oooooo"
                    wt_image exhi_gf_outfit_3_12
                    "... then flip her over ..."
                    jasmine.c "oooooooo"
                    wt_image exhi_gf_outfit_3_13
                    "... and finish both of you off with a few hard thrusts."
                    jasmine.c "ooooooo  ...  oooohh!!"
                    player.c "[player.orgasm_text]"
                    wt_image exhi_gf_outfit_3_5
                    jasmine.c "Thanks again for the great date!"
                    "She gives you a hug, then leaves you to continue your day."
                    $ jasmine.sex_count += 1
                    orgasm notify
        elif jasmine.gf_outfit_count == 4:
            call forced_movement(backyard) from _call_forced_movement_567
            summon jasmine
            wt_image exhi_gf_outfit_4_1
            "You catch Jasmine just as she's going outside."
            jasmine.c "Hi.  I'm not working today, so I thought I'd spend some time at the pool."
            $ title = "What do you say?"
            menu:
                "I'll catch you another time":
                    $ jasmine.temporary_count = 0
                    player.c "I'll catch you another time.  Have fun!"
                "I'll tag along":
                    $ jasmine.temporary_count = 2
                    "I'll tag along."
                    wt_image exhi_gf_outfit_4_2
                    jasmine.c "Okay"
                    wt_image exhi_gf_outfit_4_3
                    "Jasmine finds a comfortable spot where she can see the pool, and you find find a comfortable spot where you can see her. She smiles at you as you settle into position."
                    wt_image exhi_gf_outfit_4_4
                    jasmine.c "It's really warm out today."
                    wt_image exhi_gf_outfit_4_5
                    "She stands up, making sure you get a good view ..."
                    wt_image exhi_gf_outfit_4_6
                    "... and removes her skirt."
                    wt_image exhi_gf_outfit_4_7
                    jasmine.c "Maybe this will be better."
                    wt_image exhi_gf_outfit_4_13
                    "She smiles at you and lies back down."
                    wt_image exhi_gf_outfit_4_8
                    "A moment later, she's up again."
                    wt_image exhi_gf_outfit_4_14
                    jasmine.c "Nope.  Still too hot."
                    wt_image exhi_gf_outfit_4_9
                    "The top of her swim suit comes off .."
                    wt_image exhi_gf_outfit_4_10
                    "... followed by the bottoms."
                    wt_image exhi_gf_outfit_4_11
                    jasmine.c "This is better."
                    wt_image exhi_gf_outfit_4_12
                    "You're inclined to agree. Jasmine just wants to tease and show herself off today, so you watch her wiggle her bum at you for a while, then continue on with your day."
                    change player energy by -energy_very_short
            call forced_movement(living_room) from _call_forced_movement_568
        elif jasmine.gf_outfit_count == 5:
            call forced_movement(living_room) from _call_forced_movement_569
            summon jasmine
            wt_image exhi_gf_outfit_5_1
            "You catch Jasmine just getting home from work."
            jasmine.c "What a day!  I so need to relax."
            $ title = "What do you do?"
            menu:
                "Leave her alone to relax":
                    $ jasmine.temporary_count = 0
                    player.c "I'll leave you alone and let you relax."
                    wt_image exhi_gf_outfit_5_2
                    jasmine.c "Thanks!  I'm just going to flake out here and do nothing for a few hours!"
                "Ask to watch her":
                    player.c "Relaxing sounds good.  Mind if I watch you relax?"
                    wt_image exhi_gf_outfit_5_3
                    jasmine.c "Hmmmm.  I suppose not."
                    wt_image exhi_gf_outfit_5_4
                    jasmine.c "Yawn ... oh, I am so tired!"
                    wt_image exhi_gf_outfit_5_5
                    jasmine.c "And I can't get comfortable in this dress."
                    wt_image exhi_gf_outfit_5_6
                    jasmine.c "Maybe if I take it off I can relax better?"
                    wt_image exhi_gf_outfit_5_24
                    jasmine.c "And these shoes, too."
                    wt_image exhi_gf_outfit_5_7
                    jasmine.c "That's a bit better ..."
                    wt_image exhi_gf_outfit_5_25
                    jasmine.c "... but something's still digging into me."
                    wt_image exhi_gf_outfit_5_9
                    jasmine.c "I guess I'll take these off, too."
                    wt_image exhi_gf_outfit_5_10
                    jasmine.c "There.  That's better!"
                    wt_image exhi_gf_outfit_5_11
                    jasmine.c "I'm just going to flake out here and do nothing for a few hours!"
                    $ title = "What do you do?"
                    menu:
                        "Let her relax":
                            $ jasmine.temporary_count = 2
                            "You leave her alone to relax. She seems happy to have had the chance to strip for you, and looks like she genuinely needs some time to recover from her shift at the office."
                            change player energy by -energy_very_short
                        "Fuck her":
                            $ jasmine.temporary_count = 3
                            wt_image exhi_gf_outfit_5_12
                            player.c "You can relax after I fuck you."
                            "She's genuinely tired from her day at work, but she's also excited from having stripped for you, and even more excited to see the erection the display of her body has inspired."
                            wt_image exhi_gf_outfit_1_24
                            "The combination arouses her enough that you can enter her without too much difficulty. You start fucking her, faster and faster as her body warms up."
                            jasmine.c "oooo"
                            wt_image exhi_gf_outfit_1_23
                            "You fuck her, hard and fast, and you can tell she's enjoying it, but she's not going to cum today, she really is that tired after work.  You, on the other hand, are going to have no trouble cumming."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image exhi_gf_outfit_1_24
                                    "You thrust deep into her, hard, as you empty your load."
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_gf_outfit_1_26
                                    jasmine.c "Mmmmm.  That was nice.  Can you let me relax now?"
                                    player.c "Sure"
                                "On her":
                                    wt_image exhi_whore_1_34
                                    "You pull out and pump your load up and over her back and ass."
                                    player.c "[player.orgasm_text]"
                                    jasmine.c "Mmmmm.  That was nice.  Can you let me relax now?"
                                    player.c "Sure.  You may want to clean that up, though, before you get it all over the furniture."
                            $ jasmine.sex_count += 1
                            orgasm notify
                "Ask for a foot job":
                    player.c "Your feet must be sore from walking around in heels all day. How about you rub them against my hard cock to help them feel better?"
                    wt_image exhi_gf_outfit_5_13
                    jasmine.c "What??  You want to feel my feet against you, after I've been wearing these shoes all day?"
                    wt_image exhi_gf_outfit_5_26
                    "She leans down and takes the shoes off."
                    wt_image exhi_gf_outfit_5_25
                    jasmine.c "See?  My feet are all hot and sweaty."
                    wt_image exhi_gf_outfit_5_14
                    jasmine.c "Do you really want me rubbing them against your cock?"
                    $ title = "Do you want her sweaty feet on your cock?"
                    menu:
                        "Absolutely":
                            $ jasmine.temporary_count = 2
                            wt_image exhi_gf_outfit_5_16
                            "You sit beside her and take out your cock.  She places her soft soles on either side of your erection and begins to gently stroke you."
                            wt_image exhi_gf_outfit_5_27
                            "Her feet are hot and sweaty ... and feel amazing."
                            wt_image exhi_gf_outfit_5_17
                            "It's not long before you're breathing heavily."
                            wt_image exhi_gf_outfit_5_18
                            jasmine.c "I need to get out of this dress before you make a mess on it."
                            wt_image exhi_gf_outfit_5_19
                            "She strips naked and resumes the foot job, rubbing her soft, warm feet over your cock and balls."
                            wt_image exhi_visit_fj_5
                            jasmine.c "You're going to cum from my feet alone, aren't you?"
                            wt_image exhi_visit_fj_6
                            "You provide your answer in the form of a jet of sperm, spurting up and over her tired, sweaty and yet oh so sexy feet."
                            player.c "[player.orgasm_text]"
                            jasmine.c "oooo"
                            wt_image exhi_visit_fj_7
                            jasmine.c "Mmmmm.  That was fun.  Can you let me relax now?"
                            player.c "Do your feet feel better now?"
                            jasmine.c "Hmmmm. I'm not sure your cum is the most soothing cream ever, but yeah ... I guess my feet do feel a little less sore."
                            jasmine.c "I'm still going to relax here, though, and recover from work for ... I don't know - maybe the next five or six hours?"
                            $ jasmine.footjob_count += 1
                            orgasm notify
                        "No, I guess not":
                            $ jasmine.temporary_count = 0
                            player.c "No, I guess not."
                            wt_image exhi_gf_outfit_5_15
                            "She laughs."
                            jasmine.c "See!  I told you they were nasty!!  I'll get washed up after I relax for ... I don't know, maybe five or six hours?"
                "Suggest a fuck":
                    $ jasmine.temporary_count = 2
                    player.c "I know just the thing to help you relax.  A good hard fuck."
                    wt_image exhi_gf_outfit_5_20
                    jasmine.c "Seriously?  You think I have the energy for that now?"
                    player.c "You don't need energy.  Just get your clothes off and kneel on the couch, and I'll do all the work."
                    wt_image exhi_visit_fj_2
                    jasmine.c "Wow.  Such a gentleman."
                    wt_image exhi_gf_outfit_5_11
                    jasmine.c "Okay.  Here you go.  Just don't expect me to do anything other than kneel here."
                    wt_image exhi_gf_outfit_5_12
                    jasmine.c "Wow.  How can you be so hard already?"
                    player.c "The sight of you naked always gets me hard."
                    jasmine.c "Really?  That's kinda  ... hot and sweet."
                    wt_image exhi_gf_outfit_1_24
                    "The sight of your erection arouses her enough that you can enter her without too much difficulty. You start fucking her, faster and faster as her body warms up."
                    jasmine.c "oooo"
                    wt_image exhi_gf_outfit_1_23
                    "Even though she's now enjoying it, you can tell she's not going to cum today, she really is that tired after work.You, on the other hand, are going to have no trouble cumming."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image exhi_gf_outfit_1_24
                            "You thrust deep into her, hard, as you empty your load."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_gf_outfit_1_26
                            jasmine.c "Mmmmm.  Can you let me relax now?"
                            player.c "Sure"
                        "On her":
                            wt_image exhi_whore_1_34
                            "You pull out and pump your load up and over her back and ass."
                            player.c "[player.orgasm_text]"
                            jasmine.c "Mmmmm.  Can you let me relax now?"
                            player.c "Sure.  You may want to clean that up, though, before you get it all over the furniture."
                    $ jasmine.sex_count += 1
                    orgasm notify
                "Offer to relax her":
                    $ jasmine.temporary_count = 3
                    player.c "Get your clothes off and I'll help you relax."
                    wt_image exhi_gf_outfit_5_6
                    jasmine.c "Oh?  How do you plan to do that?"
                    wt_image exhi_gf_outfit_5_21
                    "Lie back and take your panties off and I'll show you."
                    wt_image exhi_gf_outfit_5_9
                    jasmine.c "This is sweet of you, but I'm too tired to really enjoy this."
                    wt_image exhi_gf_sex_4_18
                    player.c "Are you sure?"
                    "Her sex moistens at the first touch of your tongue."
                    jasmine.c "ooooo  ...  ummm, maybe not?"
                    wt_image exhi_gf_sex_4_19
                    "Maybe not indeed.  Her arousal builds quickly, surprising both you and her by how quickly she climaxes."
                    jasmine.c "ooooo  ...  oooooo  ...  oooohh!!"
                    wt_image exhi_gf_outfit_5_22
                    jasmine.c "Mmmmm.  Maybe you do know how to relax me.  That was ... amazing."
                    player.c "Reinvigorated now?"
                    wt_image exhi_gf_outfit_5_7
                    jasmine.c "Hmmmm.  Let me reflect on that while I flake out here for, I don't know ... maybe the next five or six hours?"
                    $ jasmine.orgasm_count += 1
                    change player energy by -energy_short notify
        elif jasmine.gf_outfit_count == 6:
            call forced_movement(kitchen) from _call_forced_movement_570
            summon jasmine
            wt_image exhi_gf_outfit_6_1
            "You find Jasmine just leaving the kitchen."
            player.c "Going somewhere?"
            wt_image exhi_gf_outfit_6_2
            jasmine.c "Not if there's something you wanted to do together?"
            $ title = "What do you want?"
            menu:
                "Just hang out with her":
                    $ jasmine.temporary_count = 2
                    player.c "I thought maybe we could just hang out and chat?"
                    wt_image exhi_gf_outfit_6_11
                    jasmine.c "Okay.  Sure."
                    wt_image exhi_gf_outfit_6_5
                    jasmine.c "I'm going to take my clothes off, though."
                    wt_image exhi_gf_outfit_6_12
                    jasmine.c "I prefer chatting with you like this."
                    wt_image exhi_gf_outfit_6_13
                    "Life with an exhibitionist can be fun, even if you do have a harder time than normal maintaining an intelligent conversation with her over the next hour or so."
                    change player energy by -energy_very_short
                "Watch her undress":
                    player.c "I was hoping to see you undress."
                    wt_image exhi_gf_outfit_6_4
                    jasmine.c "Why?  Is there something wrong with my clothes?"
                    player.c "No, I just thought they'd look better on the floor."
                    wt_image exhi_gf_outfit_6_5
                    jasmine.c "Oh, aren't you the sweet talker?"
                    wt_image exhi_gf_outfit_6_6
                    jasmine.c "I wish I'd known you were going to want a show today, though."
                    wt_image exhi_gf_outfit_6_7
                    jasmine.c "I would have worn something other than these damn boots.  They're a bitch to get off."
                    wt_image exhi_bimbo_outfit_5_9
                    jasmine.c "There!  Off.  Thus ends the worst strip show, ever."
                    wt_image exhi_gf_outfit_6_8
                    player.c "Nah, your shows are always great, because at the end of them I get to look at you."
                    wt_image exhi_bimbo_outfit_5_3
                    jasmine.c "Wow, you really are laying it on thick today.  And I'm such a sucker, it's actually working."
                    wt_image exhi_bimbo_outfit_5_15
                    jasmine.c "Did you want to fuck me, or are you happy with just the show?"
                    $ title = "The show was enough?"
                    menu:
                        "The show was enough":
                            $ jasmine.temporary_count = 3
                            player.c "The show was great.  Thanks, Jasmine."
                            jasmine.c "Any time.  You know I love having your attention."
                            change player energy by -energy_very_short
                        "You want to fuck her":
                            $ jasmine.temporary_count = 4
                            player.c "How could I say no to that offer?"
                            wt_image exhi_gf_outfit_6_14
                            "Carefully, you insert your cock into her sexy, waiting twat."
                            jasmine.c "oooo"
                            wt_image exhi_bimbo_outfit_5_16
                            "She's wet and eager and thrusts her hips up to meet you are you stroke in and out of her."
                            jasmine.c "ooooo"
                            wt_image exhi_gf_outfit_6_15
                            jasmine.c "ooooo ... turn me over!"
                            wt_image exhi_gf_outfit_6_16
                            "She doesn't have to ask you twice.  You flip her over ..."
                            wt_image exhi_bimbo_outfit_5_13
                            "... and then finish you both off with a few hard, fast strokes from behind."
                            jasmine.c "ooooo  ...  oooohh!!"
                            player.c "[player.orgasm_text]"
                            wt_image exhi_bimbo_outfit_5_12
                            jasmine.c "I guess you did like my show."
                            player.c "Especially the ending.  You seemed to like it, too."
                            wt_image exhi_bimbo_outfit_5_10
                            jasmine.c "Mmmm ... I did."
                            $ jasmine.sex_count += 1
                            $ jasmine.orgasm_count += 1
                            orgasm notify
                "A blow job":
                    $ jasmine.temporary_count = 2
                    player.c "A blow job would be nice."
                    wt_image exhi_gf_outfit_6_1
                    jasmine.c "Hmmm.  That's a little one sided, but I suppose I could help you out."
                    wt_image exhi_gf_outfit_6_5
                    "She pulls off her top ..."
                    wt_image exhi_gf_outfit_6_17
                    "... kneels down and takes out your cock ..."
                    wt_image exhi_gf_outfit_6_18
                    "... licks you hard ..."
                    wt_image exhi_gf_outfit_6_9
                    "... then starts a blow job ..."
                    wt_image exhi_gf_outfit_6_19
                    "... that soon culminates with you filling her mouth with cum."
                    wt_image exhi_gf_outfit_6_10
                    player.c "[player.orgasm_text]"
                    wt_image exhi_gf_outfit_6_3
                    jasmine.c "I take it that satisfied you?"
                    player.c "Very nicely, yes."
                    wt_image exhi_gf_outfit_6_11
                    jasmine.c "Good.  Hate to think my boyfriend was walking around in need."
                    $ jasmine.blowjob_count += 1
                    $ jasmine.swallow_count += 1
                    orgasm notify
                "Sex":
                    $ jasmine.temporary_count = 3
                    player.c "I want to fuck you."
                    wt_image exhi_gf_outfit_6_11
                    jasmine.c "Hmmm.  I may need some warming up first."
                    wt_image exhi_gf_outfit_6_3
                    player.c "Get out of your clothes and lie down on your back."
                    wt_image exhi_gf_outfit_6_8
                    jasmine.c "Like this?"
                    wt_image exhi_bimbo_outfit_5_9
                    player.c "Now expose yourself to me."
                    wt_image exhi_bimbo_outfit_5_14
                    "She reaches both hands down and opens her sex up for your inspection."
                    player.c "Warmed up yet?"
                    jasmine.c "Maybe a little?"
                    if jasmine.whore_play_status > 4:
                        player.c "Don't lie to me, whore.  Your greedy whore cunt is dripping wet from the chance to expose itself. It's throbbing at the very thought of being filled by a hard cock, isn't it?"
                    else:
                        player.c "Don't lie to me, my little exhibitionist.  Your cunt is dripping wet from the chance to expose itself, isn't it?"
                    wt_image exhi_bimbo_outfit_5_15
                    jasmine.c "Yes"
                    wt_image exhi_gf_outfit_6_14
                    "You shove your cock inside her wet, waiting twat ..."
                    jasmine.c "Oh!"
                    wt_image exhi_gf_outfit_6_15
                    "... stroking it in and out of her ..."
                    jasmine.c "oooo"
                    wt_image exhi_gf_outfit_6_16
                    "... then flip her over ..."
                    wt_image exhi_bimbo_outfit_5_13
                    "... and finish off from behind."
                    player.c "[player.orgasm_text]"
                    jasmine.c "ooooo"
                    wt_image exhi_bimbo_outfit_5_11
                    player.c "Did you want a chance to cum now?"
                    "She shakes her head."
                    wt_image exhi_gf_outfit_6_5
                    jasmine.c "No, it was kinda fun just being used like that."
                    if not jasmine.has_tag('gf_used_for_sex'):
                        add tags 'gf_used_for_sex' to jasmine
                        change jasmine submission by 5
                    $ jasmine.sex_count += 1
                    orgasm notify
                "Nothing":
                    $ jasmine.temporary_count = 0
                    player.c "No, I was just curious what you were up to."
                    wt_image exhi_gf_outfit_6_1
                    jasmine.c "Not much.  See you later."
            call forced_movement(living_room) from _call_forced_movement_571
        else:
            sys "There's been an error with jasmine.gf_outfit_count in label jasmine_gf_actions"
        if jasmine.temporary_count > 0:
            $ jasmine.maintain_week_gf = week + jasmine.temporary_count
            $ jasmine.temporary_count = 0
        call character_location_return(jasmine) from _call_character_location_return_315
    else:
        "Wait until the two of you are at home in the bedroom together."
    return

# Bimbo Actions
label jasmine_bimbo_actions:
    if current_location == bedroom:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        $ jasmine.bimbo_outfit_count += 1
        if jasmine.bimbo_outfit_count > 4:
            $ jasmine.bimbo_outfit_count = 1
        if jasmine.bimbo_outfit_count == 1:
            call forced_movement(living_room) from _call_forced_movement_572
            summon jasmine
            wt_image exhi_bimbo_outfit_5_1
            "You find Jasmine sitting on the sofa, naked."
            player.c "Jasmine, did you forget to wear clothes today?"
            wt_image exhi_bimbo_outfit_5_2
            jasmine.c "Umm, maybe?  Was I supposed to wear clothes today?"
            $ title = "What do you do?"
            menu:
                "Tell her to dress":
                    player.c "It's normal to put on clothes when you get up in the morning."
                    jasmine.c "Is it?  I wonder why?"
                    wt_image exhi_bimbo_outfit_5_3
                    jasmine.c "Oh!  I know, so then you have clothes on to take off when someone is watching you!!"
                    wt_image exhi_bimbo_outfit_5_7
                    "She struggles to get into the pair of jeans you bring her ..."
                    wt_image exhi_bimbo_outfit_5_8
                    "... with limited success."
                    wt_image exhi_bimbo_outfit_5_9
                    "Eventually she gives up."
                    jasmine.c "Jeans are bad clothes.  Can I wear something easier to take off?"
                    player.c "You mean put on?"
                    wt_image exhi_bimbo_outfit_5_10
                    jasmine.c "Uhhh, no, i don't want to wear them!  I want to take them off!!"
                    "That may explain much of her struggle"
                "Sit with her":
                    player.c "It's normal to put on clothes when you get up in the morning, but it's okay if you didn't.  I'm happy to sit with you like this."
                    wt_image exhi_bimbo_outfit_5_4
                    jasmine.c "You are?  Great!!  Do you want to look at my pussy?"
                    wt_image exhi_bimbo_outfit_5_5
                    jasmine.c "Or my ass?"
                    player.c "How about we just sit and talk instead?"
                    wt_image exhi_bimbo_outfit_5_6
                    "She pouts."
                    jasmine.c "Do I have to talk?  What if you talk and I smile and show off my tits?"
                    "She seems to have a surprisingly firm grasp of what she does best these days."
                "Tell her to turn around":
                    player.c "It's normal to put on clothes when you get up in the morning, but since you didn't, how about you turn around?"
                    wt_image exhi_bimbo_outfit_5_11
                    jasmine.c "Like this?"
                    wt_image exhi_bimbo_outfit_5_21
                    jasmine.c "Are you going to fuck me?  I like it when you fuck me."
                    $ title = "Are you going to fuck her?"
                    menu:
                        "Yes":
                            wt_image exhi_bimbo_outfit_5_13
                            jasmine.c "Oh, you are fucking me! I like it when you fuck me, because then your hard cock is inside me."
                            "You and your hard cock are pretty fond of the experience as well. Jasmine's not much of a conversationalist these days, but she's a happy and willing fucktoy well-suited for sating your desire."
                            player.c "[player.orgasm_text]"
                            $ jasmine.sex_count += 1
                            orgasm notify
                        "No":
                            player.c "No, just stay there with your ass facing out today."
                            wt_image exhi_bimbo_outfit_5_5
                            jasmine.c "Okay.  How long should I stay this way?"
                            player.c "How about the whole day?"
                            jasmine.c "Okay!  I can do that.  Wait, will you tell me when today is over?"
                            player.c "Sure"
                            jasmine.c "Okay.  Thanks!"
                            add tags 'holding_position' to jasmine
                            $ jasmine.change_image( 'exhi_bimbo_outfit_5_5' )
                "Tell her to spread her legs":
                    player.c "It's normal to put on clothes when you get up in the morning, but since you didn't, how about you lie down and spread your legs?"
                    wt_image exhi_bimbo_outfit_5_14
                    jasmine.c "Like this?"
                    wt_image exhi_bimbo_outfit_5_15
                    jasmine.c "Are you going to fuck me?  I like it when you fuck me."
                    $ title = "Are you going to fuck her?"
                    menu:
                        "Yes":
                            wt_image exhi_bimbo_outfit_5_16
                            jasmine.c "Oh, you are fucking me! I like it when you fuck me, because then your hard cock is inside me."
                            "You and your hard cock are pretty fond of the experience as well. Jasmine's not much of a conversationalist these days, but she's a happy and willing fucktoy well-suited for sating your desire."
                            player.c "[player.orgasm_text]"
                            $ jasmine.sex_count += 1
                            orgasm notify
                        "No":
                            player.c "No, just stay there exposing your pussy today."
                            wt_image exhi_bimbo_outfit_5_4
                            jasmine.c "Okay.  How long should I stay this way?"
                            player.c "How about the whole day?"
                            jasmine.c "Okay!  I can do that.  Wait, will you tell me when today is over?"
                            player.c "Sure"
                            jasmine.c "Okay.  Thanks!"
                            add tags 'holding_position' to jasmine
                            $ jasmine.change_image( 'exhi_bimbo_outfit_5_4' )
                "Tell her to blow you":
                    player.c "It's normal to put on clothes when you get up in the morning, but since you didn't, how about you give me a blowjob?"
                    jasmine.c "Couldn't I give you a blow job if I was wearing clothes?"
                    wt_image exhi_bimbo_outfit_5_6
                    jasmine.c "Oh! Then you might get your sperm all over my pretty clothes!! You're right. This is better. You can get your sperm all over me and my clothes will still look good."
                    player.c "You're not wearing ... never mind, just suck my cock."
                    wt_image exhi_bimbo_outfit_5_17
                    jasmine.c "Okay"
                    "Jasmine's not much of a conversationalist these days, but her mouth has other, better uses than talking, and is well-suited for sating your desire."
                    wt_image exhi_bimbo_outfit_5_18
                    "When you're ready to cum, you pull your cock out of her mouth and pump your load over her. After all, it was her idea that this was the ideal time to get your sperm all over her."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_bimbo_outfit_5_19
                    jasmine.c "Should I go clean up now?"
                    $ title = "What do you tell her?"
                    menu:
                        "Clean my cock first":
                            player.c "Clean my cock first."
                            wt_image exhi_bimbo_outfit_5_20
                            jasmine.c "Okay"
                            "There are few things cuter than a woman sucking the last drops of cum out of your cock while your sperms drips down her face. Knowing that Jasmine will happily stay here until you tell her to go clean up makes it all the cuter."
                        "Stay like you are for today":
                            player.c "No, just stay there like that today."
                            jasmine.c "Okay.  How long should I stay this way?"
                            player.c "How about the whole day?"
                            jasmine.c "Okay!  I can do that.  Wait, will you tell me when today is over?"
                            player.c "Sure"
                            jasmine.c "Okay.  Thanks!"
                            add tags 'holding_position' to jasmine
                            $ jasmine.change_image( 'exhi_bimbo_outfit_5_19' )
                    $ jasmine.blowjob_count += 1
                    $ jasmine.facial_count += 1
                    orgasm notify
        elif jasmine.bimbo_outfit_count == 2:
            call forced_movement(kitchen) from _call_forced_movement_573
            summon jasmine
            wt_image exhi_bimbo_outfit_7_1
            "You find Jasmine in the kitchen."
            jasmine.c "I remembered to wear clothes today!"
            wt_image exhi_bimbo_outfit_7_2
            jasmine.c "But I don't remember why.  Maybe it would be better if I wore them like this?"
            $ title = "What do you tell her?"
            menu:
                "Show off her pussy, too":
                    player.c "You should show off your pussy, too."
                    wt_image exhi_bimbo_outfit_7_3
                    jasmine.c "Okay.  Maybe I'll hang around like this today."
                    player.c "That sounds like a good idea."
                    add tags 'holding_position' to jasmine
                    $ jasmine.change_image( 'exhi_bimbo_outfit_7_3' )
                "Show off more of her tits":
                    player.c "It'd be even better if you showed off more of your tits."
                    wt_image exhi_bimbo_outfit_7_4
                    jasmine.c "Okay.  How's this?"
                    player.c "Good"
                    wt_image exhi_bimbo_outfit_7_5
                    jasmine.c "Okay.  Maybe I'll hang around like this today."
                    player.c "That sounds like a good idea."
                    add tags 'holding_position' to jasmine
                    $ jasmine.change_image( 'exhi_bimbo_outfit_7_5' )
                "Turn around":
                    player.c "Turn around."
                    wt_image exhi_bimbo_outfit_7_6
                    jasmine.c "Okay, but in case you want to fuck me, I need to take my panties off."
                    wt_image exhi_bimbo_outfit_7_7
                    "She pulls off her panties and gets up on the counter, wiggling her bum at you."
                    jasmine.c "Are you going to fuck me?  I like it when you fuck me."
                    $ title = "Are you going to fuck her?"
                    menu:
                        "Yes":
                            wt_image exhi_bimbo_outfit_7_8
                            jasmine.c "Oh, you are fucking me!"
                            wt_image exhi_bimbo_outfit_7_9
                            jasmine.c "I like it when you fuck me, because then I can feel your prick inside me."
                            "You and your prick enjoy the sensation of being inside her, too. The only question is whether you want to stay inside her when you cum?"
                            $ title = "Where do you want to cum?"
                            menu:
                                "On her ass":
                                    wt_image exhi_whore_2_21
                                    "Her upturned ass looks just perfect for a load of cum.  You pull out and adorn her skin."
                                    player.c "[player.orgasm_text]"
                                "Inside her":
                                    wt_image exhi_bimbo_outfit_7_19
                                    "She likes you in her, you like being in her. Why ruin a good thing? You pump into her, deeper and harder with each thrust, until you empty your balls deep inside her."
                                    player.c "[player.orgasm_text]"
                                    "Cumming inside a ditz who likely can't remember to take birth control may not be the wisest idea, but Jasmine expresses no concerns. Then again, it's doubtful she understands the biological consequences of sperm inside her anyway."
                            $ jasmine.sex_count += 1
                            orgasm notify
                        "No":
                            player.c "No, I just want to look at you today"
                            jasmine.c "Okay.  Maybe I'll hang around like this today. In case you want to look at me again later."
                            player.c "That sounds like a good idea."
                            add tags 'holding_position' to jasmine
                            $ jasmine.change_image( 'exhi_bimbo_outfit_7_7' )
                "You want to fuck her":
                    player.c "Don't worry about your clothes, Jasmine.  Come here.  I want to fuck you."
                    wt_image exhi_bimbo_outfit_7_10
                    jasmine.c "Okay.  I like it when you fuck me."
                    wt_image exhi_bimbo_outfit_7_11
                    jasmine.c "Having a hard cock inside me feels nice.  Am I supposed to wait for you to cum first, or is it okay if I cum?"
                    player.c "It's okay, Jasmine.  You can cum."
                    wt_image exhi_bimbo_outfit_7_12
                    jasmine.c "Oh, good!"
                    jasmine.c "oooohh!!"
                    player.c "Did you just ...?"
                    jasmine.c "Uh huh, because I have a hard cock inside me, and it feels good."
                    "It's feeling pretty good on your end, too."
                    $ title = "Where do you want to cum?"
                    menu:
                        "On her face":
                            wt_image exhi_bimbo_outfit_7_13
                            "You remove your cock and position it in front of her face. She happily reaches up and strokes you to climax."
                            player.c "[player.orgasm_text]"
                            $ jasmine.facial_count += 1
                        "On her pussy":
                            wt_image exhi_creampie_2
                            "You pull out, showering her pussy with your cum as you do."
                            player.c "[player.orgasm_text]"
                        "Inside her":
                            wt_image exhi_whore_2_16
                            "You thrust deep inside her once, twice, three times ... then cum, filling her with your sperm."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_creampie_3
                            "Jasmine plays idly with the jizz that dribbles from her pussy after you pull out."
                            "Cumming inside a ditz who likely can't remember to take birth control may not be the wisest idea, but Jasmine expresses no concerns. Then again, it's doubtful she understands the biological consequences of sperm inside her anyway."
                    $ jasmine.sex_count += 1
                    $ jasmine.orgasm_count += 1
                    orgasm notify
                "You want a blow job":
                    player.c "Don't worry about that, Jasmine.  Come here.  I want a blow job."
                    wt_image exhi_bimbo_outfit_7_4
                    jasmine.c "Okay.  I'll take my clothes off."
                    player.c "You don't have to, I only want a blow job."
                    jasmine.c "Uh huh, that's why I'm getting naked."
                    player.c "But ... never mind.  Naked is fine."
                    wt_image exhi_bimbo_outfit_7_14
                    "The blow job is fine, too.  More than fine, and your balls are soon boiling and in need of release."
                    $ title = "Where do you want to cum?"
                    menu:
                        "On her face":
                            wt_image exhi_bimbo_outfit_7_15
                            "You pull back, out of her mouth, and Jasmine strokes your cock with her hand, depositing your load on her waiting face."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_bimbo_outfit_7_16
                            jasmine.c "Ooops.  All of your cum ended up on my face."
                            player.c "It looks nice there."
                            jasmine.c "Shouldn't I have put some on my tits?"
                            player.c "It's okay, some is dripping on your tits now."
                            jasmine.c "It is?  Oh, okay!!"
                            $ jasmine.facial_count += 1
                        "In her mouth":
                            wt_image exhi_bimbo_outfit_7_17
                            "As she continues to suckle and pleasure your cock, you let yourself go, releasing your load down the back of her throat."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_bimbo_outfit_7_18
                            jasmine.c "Shoot!  I forgot to have a coffee this morning."
                            player.c "Make yourself one now."
                            jasmine.c "No, I don't like coffee black, and I just finished drinking all the cream."
                            $ jasmine.swallow_count += 1
                    $ jasmine.blowjob_count += 1
                    orgasm notify
            call forced_movement(living_room) from _call_forced_movement_574
        elif jasmine.bimbo_outfit_count == 3:
            call forced_movement(bathroom) from _call_forced_movement_575
            summon jasmine
            wt_image exhi_bimbo_outfit_2_1
            "You find Jasmine in the shower. You assume she's showering. She seems to be spending most of her time pressing her boobs against the shower glass."
            wt_image exhi_bimbo_outfit_2_2
            "She smiles when she sees you."
            wt_image exhi_bimbo_outfit_2_3
            jasmine.c "Oh goody! There you are!"
            player.c "Did you have the towel on when you were in the shower?"
            wt_image exhi_bimbo_outfit_2_6
            jasmine.c "Uh huh, but I don't need it now."
            jasmine.c "I couldn't figure out a way to get the back of my throat clean in the shower, but now you're here!"
            $ title = "What do you do?"
            menu menu_jasmine_bimbo_outfit_3:
                "Let her clean her throat":
                    player.c "How are you going to ..."
                    wt_image exhi_bimbo_outfit_2_4
                    jasmine.c "Like this!"
                    "She drops to her knees and takes out your cock."
                    wt_image exhi_bimbo_outfit_2_7
                    "You're pretty sure this makes no sense, but she seems determined in her efforts."
                    wt_image exhi_bimbo_outfit_2_5
                    "You let her suck your cock until your cum washes over the back of her throat, presumably 'cleaning' it for her."
                    player.c "[player.orgasm_text]"
                    "She seems happy, and so are you."
                    $ jasmine.swallow_count += 1
                    $ jasmine.blowjob_count += 1
                    orgasm notify
                "Suggest she use her fingers":
                    player.c "Perhaps you could use your fingers?"
                    wt_image exhi_bimbo_outfit_2_8
                    jasmine.c "I tried, but I can't reach the back of my throat with them.  Besides, I already used my fingers to clean my pussy."
                    wt_image exhi_bimbo_outfit_2_9
                    jasmine.c "See?"
                    player.c "How did you manage that?"
                    wt_image exhi_bimbo_outfit_2_10
                    jasmine.c "Like this!  I put my finger inside and then ... ooooo"
                    jasmine.c "And then I, ummm  ...  ooooo"
                    wt_image exhi_bimbo_outfit_2_11
                    jasmine.c "Maybe I  ...  oooohh!!"
                    wt_image exhi_bimbo_outfit_2_12
                    jasmine.c "I think I need to take another shower."
                    "You leave her to finish her personal grooming."
                    $ jasmine.orgasm_count += 1
                "Suggest she use her dildo" if jasmine.has_item(dildo) or player.has_item(dildo):
                    if jasmine.has_item(dildo):
                        player.c "Perhaps you should use your dildo?"
                    else:
                        $ title = "Do you want to gift the dildo to [jasmine.name]?"
                        menu:
                            "Yes":
                                player.c "Perhaps this would help?"
                                give 1 dildo from player to jasmine notify
                            "No":
                                pass
                    if jasmine.has_item(dildo):
                        wt_image exhi_bimbo_outfit_2_13
                        jasmine.c "Good idea!  Maybe I can clean my throat with that."
                        wt_image exhi_bimbo_outfit_2_14
                        jasmine.c "I can't reach the back of my throat, and having a pretend cock in my mouth is making me horny."
                        player.c "Try a little lower down."
                        wt_image exhi_bimbo_outfit_2_15
                        jasmine.c "I can't reach the back of my throat this way, either, and the pretend cock is still making me horny."
                        player.c "Lower still."
                        wt_image exhi_bimbo_outfit_2_16
                        jasmine.c "Can I reach my throat this way? I'll need to push the pretend cock all the way in and ... ooooo"
                        wt_image exhi_bimbo_outfit_2_17
                        jasmine.c "I'm not sure it's going to reach and  ...  ooooo"
                        wt_image exhi_bimbo_outfit_2_18
                        jasmine.c "And ... and ... oooohh!!"
                        wt_image exhi_bimbo_outfit_2_19
                        jasmine.c "I think I need to take another shower."
                        "You leave her to finish her personal grooming."
                        $ jasmine.orgasm_count += 1
                    else:
                        jump menu_jasmine_bimbo_outfit_3
                "Just leave":
                    wt_image exhi_bimbo_outfit_2_20
                    "Some days you just don't have the energy to deal with her stupidity, regardless of how cute a body that stupidity comes packaged in. Who knows how long she'll spend in the bathroom trying to sort out her dilemma."
                    add tags 'holding_position' to jasmine
                    $ jasmine.change_image( 'exhi_bimbo_outfit_2_20' )
            call forced_movement(living_room) from _call_forced_movement_576
            call character_location_return(jasmine) from _call_character_location_return_316
        elif jasmine.bimbo_outfit_count == 4:
            wt_image exhi_bimbo_outfit_4_1
            "You find Jasmine in your bedroom."
            jasmine.c "Help!  I can't figure something out."
            player.c "What?"
            jasmine.c "Do my tits look better like this?"
            wt_image exhi_bimbo_outfit_4_2
            jasmine.c "Or like this?"
            wt_image exhi_bimbo_outfit_4_3
            jasmine.c "Or like this?"
            wt_image exhi_bimbo_outfit_4_4
            jasmine.c "I can't figure it out."
            $ title = "What do you tell her?"
            menu:
                "The first":
                    player.c "The first."
                    wt_image exhi_bimbo_outfit_4_10
                    jasmine.c "Thanks!"
                    wt_image exhi_bimbo_outfit_4_5
                    jasmine.c "Wait, which one was the first?"
                    "You leave her to try and sort it out."
                "The second":
                    player.c "The second."
                    wt_image exhi_bimbo_outfit_4_10
                    jasmine.c "Thanks!"
                    wt_image exhi_bimbo_outfit_4_5
                    jasmine.c "Wait, which one was the second?"
                    "You leave her to try and sort it out."
                "The third":
                    player.c "The third."
                    wt_image exhi_bimbo_outfit_4_10
                    jasmine.c "Thanks!"
                    wt_image exhi_bimbo_outfit_4_5
                    jasmine.c "Wait, which one was the third?"
                    "You leave her to try and sort it out."
                "Open your mouth":
                    player.c "Open your mouth."
                    wt_image exhi_bimbo_outfit_4_6
                    "As she does so, you take out your cock ..."
                    wt_image exhi_bimbo_outfit_4_8
                    "... and press it against her lips.  She opens her eyes and licks your cock."
                    wt_image exhi_bimbo_outfit_4_7
                    jasmine.c "Thanks!  I always think better with a cock in my mouth."
                    wt_image exhi_bimbo_outfit_4_9
                    "You let her think until her mouth is filled with your sperm."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_bimbo_outfit_4_10
                    "So what did you decide?"
                    jasmine.c "About what?"
                    player.c "Never mind."
                    $ jasmine.swallow_count += 1
                    $ jasmine.blowjob_count += 1
                    orgasm notify
        else:
            sys "There's been an error with jasmine.bimbo_outfit_count in label jasmine_bimbo_actions"
        call character_location_return(jasmine) from _call_character_location_return_317
    else:
        "Wait until the two of you are at home in the bedroom together."
    return

# Watch Her Dance
label jasmine_watch_her_dance:
    # girlfriend dance
    if current_location == bedroom and jasmine.has_tag('girlfriend'):
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        $ jasmine.lingerie_outfit_count += 1
        if jasmine.lingerie_outfit_count > 3:
            $ jasmine.lingerie_outfit_count = 1
        if jasmine.lingerie_outfit_count == 1:
            if jasmine.has_item(lingerie):
                wt_image exhi_gf_portrait
                player.c "[jasmine.name], how about you put on a show for me?"
                if jasmine.has_tag('showgirl'):
                    jasmine.c "Why, can't you come down to the Club and watch me with everyone else?"
                    player.c "I was hoping for a private performance."
                    jasmine.c "Oh, you want that kind of a show."
                else:
                    jasmine.c "Would I be wearing much clothes in this show?"
                    player.c "Hopefully not."
                wt_image exhi_lingerie_1
                "[jasmine.name] changes into the underwear you bought her."
                wt_image exhi_lingerie_2
                jasmine.c "Do I look nice?"
                player.c "Always"
                wt_image exhi_lingerie_3
                jasmine.c "Then I guess I should give you a little performance."
                wt_image exhi_lingerie_4
                jasmine.c "In case you want to see what my ass looks like in the outfit you bought me ..."
                wt_image exhi_lingerie_5
                "... or what my tits look like out of it."
                wt_image exhi_lingerie_6
                jasmine.c "And in case I forgot to mention it before  ...  thanks for the sexy lingerie."
                $ title = "What do you tell her?"
                menu:
                    "Thanks for the show":
                        player.c "I'm glad you like it.  Thanks for the show."
                        wt_image exhi_lingerie_7
                        jasmine.c "Thanks for watching me!"
                        if jasmine.maintain_week_gf < week + 2:
                            $ jasmine.maintain_week_gf = week + 2
                        change player energy by -energy_very_short
                    "Thank me properly":
                        player.c "I'm glad you like it.  Why don't you thank me properly for the gift?"
                        wt_image exhi_lingerie_8
                        "With a mischievous grin on her face, she sinks to her knees in front of you and fishes your hard cock out of your pants."
                        jasmine.c "Thank you properly?  I suppose you were hoping for something like this?"
                        wt_image exhi_lingerie_9
                        "Forming her soft hand into a fist, she pumps up and down gently on your cock."
                        wt_image exhi_lingerie_10
                        "Still pumping your shaft with her right hand, she start massaging your balls with her left."
                        wt_image exhi_lingerie_11
                        "As the pressure in your balls builds, she presses your cock between her tits."
                        wt_image exhi_lingerie_12
                        player.c "[player.orgasm_text]"
                        jasmine.c "Thanks for the sexy lingerie."
                        $ jasmine.handjob_count += 1
                        if jasmine.maintain_week_gf < week + 2:
                            $ jasmine.maintain_week_gf = week + 2
                        orgasm notify
            else:
                $ jasmine.lingerie_outfit_count = 2
        if jasmine.lingerie_outfit_count == 2:
            if jasmine.has_tag('bonus_lingerie'):
                wt_image exhi_gf_portrait
                player.c "[jasmine.name], how about you put on a show for me?"
                jasmine.c "A skimpy clothes show?"
                player.c "That'd be perfect."
                wt_image exhi_lingerie_bonus_1
                "[jasmine.name] re-appears a few minutes later, wearing barely there see through lingerie."
                wt_image exhi_lingerie_bonus_2
                jasmine.c "Do you like this?"
                wt_image exhi_lingerie_bonus_3
                jasmine.c "I found this on sale, and bought it with the money I earned being your 'whore'."
                wt_image exhi_lingerie_bonus_4
                jasmine.c "It looked like something we could both enjoy."
                $ title = "What do you tell her?"
                menu:
                    "It looks great":
                        player.c "It looks great, Jasmine."
                        wt_image exhi_lingerie_bonus_5
                        jasmine.c "Thanks!  That's what I thought.  On me or off me, it looks cute either way."
                        if jasmine.maintain_week_gf < week + 2:
                            $ jasmine.maintain_week_gf = week + 2
                        change player energy by -energy_very_short
                    "Bend over":
                        player.c "It'll look better when it's on the floor and you finish bending over all the way."
                        wt_image exhi_lingerie_bonus_6
                        "A small smile crossed her face as she finishes removing the lingerie and kneels down, facing away from you. You slide your hard dick along the crack of her ass ..."
                        wt_image exhi_lingerie_bonus_8
                        "... then push yourself into her wet snatch.  She moans as you enter her ..."
                        jasmine.c "ooooo"
                        wt_image exhi_lingerie_bonus_9
                        "... and then again, louder, as you start fucking her."
                        jasmine.c "oooooo"
                        "Maybe she's thinking about you using her as a whore or maybe she's just horny from showing off her lingerie ..."
                        wt_image exhi_lingerie_bonus_7
                        "... either way, she cums quickly, rocking back on your hard dick and bringing you to the brink of your own orgasm."
                        jasmine.c "oooooo  ...  oooohh!!"
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image exhi_bimbo_outfit_7_19
                                "You thrust into her, hard ... once, twice, three times ... burying your shaft as deep into her as it will go as you feel your balls boil over."
                                player.c "[player.orgasm_text]"
                                wt_image exhi_lingerie_bonus_10
                                "She closes her eyes and sighs as you finish pumping the last of your load inside her."
                                jasmine.c "Mmmmm. I'm glad you enjoyed the lingerie."
                            "On her":
                                wt_image exhi_lingerie_bonus_11
                                "She gasps in surprises as you pull out and spurt your hot seed over her ass."
                                player.c "[player.orgasm_text]"
                                jasmine.c "Oh!"
                                wt_image exhi_lingerie_bonus_12
                                "She stays in position as you finish pumping your jizz onto her and watch it drip down her ass."
                                jasmine.c "I'm glad you enjoyed the lingerie."
                        $ jasmine.maintain_week_gf = week + 3
                        $ jasmine.sex_count += 1
                        $ jasmine.orgasm_count += 1
                        orgasm notify
            else:
                $ jasmine.lingerie_outfit_count = 3
        if jasmine.lingerie_outfit_count == 3:
            wt_image exhi_gf_portrait
            player.c "[jasmine.name], how about you put on a show for me?"
            if jasmine.has_tag('showgirl'):
                jasmine.c "Hmmm.  There is a new routine I've been thinking about trying out.  Would you like to see it?"
            else:
                jasmine.c "Well, there was this idea I had for a stripper routine. I'm not sure I'll be any good, but would you like me to try?"
            player.c "Absolutely"
            wt_image exhi_strip_8_1
            "It takes [jasmine.name] a while before she changes and returns. She puts on some music, and then stands in front of you ..."
            wt_image exhi_strip_8_2
            "... and starts to sway ..."
            wt_image exhi_strip_8_3
            "... and gyrate ..."
            wt_image exhi_strip_8_4
            "... turning ..."
            wt_image exhi_strip_8_5
            "... and twisting to the music ..."
            wt_image exhi_strip_8_6
            "... as more ..."
            wt_image exhi_strip_8_7
            "... and more of her body ..."
            wt_image exhi_strip_8_8
            "... appears from underneath her clothes ..."
            wt_image exhi_strip_8_9
            "... and between her legs ..."
            wt_image exhi_strip_8_10
            "... for your inspection."
            if jasmine.has_tag('showgirl'):
                player.c "That's a good show.  You should definitely perform that at the Club."
                wt_image exhi_strip_8_11
                jasmine.c "Maybe.  Or maybe I'll save that as a private dance for my boyfriend."
            else:
                player.c "That's a good show.  You could definitely perform that on stage."
                wt_image exhi_strip_8_11
                jasmine.c "For real?  You think I could actually perform as a stripper?"
                player.c "To be honest, I'm not sure how you ended up as my girlfriend without being a showgirl."
            jasmine.c "Did you know it gets me wet, knowing that you'd like me to dance that way in front of a group of strangers?"
            player.c "I've noticed, yes."
            if jasmine.maintain_week_gf < week + 2:
                $ jasmine.maintain_week_gf = week + 2
            change player energy by -energy_very_short
    # bimbo dance
    elif current_location == bedroom and jasmine.has_tag('bimbo'):
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        $ jasmine.bimbo_strip_count += 1
        if jasmine.bimbo_strip_count > 3:
            $ jasmine.bimbo_strip_count = 1
        if jasmine.bimbo_strip_count == 1:
            wt_image exhi_strip_7_2
            player.c "[jasmine.name], how about you put on a show for me."
            wt_image exhi_strip_7_1
            jasmine.c "A show?  I don't think I know how to do that."
            player.c "Sure you do.  Show off your body for me."
            wt_image exhi_strip_7_2
            jasmine.c "My body?  But you can already see my body.  Can't you?  I'm not invisible, am I?"
            wt_image exhi_strip_7_3
            jasmine.c "Maybe it's the clothes that are invisible!  Can you see these?"
            player.c "Yes, they look very nice."
            wt_image exhi_strip_7_4
            jasmine.c "How about now, can you see all of me now?"
            player.c "Yes, I can see all of you."
            wt_image exhi_strip_7_5
            jasmine.c "Thank goodness!  Oh!  My pussy's no longer invisible, either.  Mmmmm."
        elif jasmine.bimbo_strip_count == 2:
            wt_image exhi_strip_7_2
            player.c "[jasmine.name], how about you put on a show for me."
            wt_image exhi_strip_7_1
            jasmine.c "A show?  I don't think I know how to do that."
            player.c "Sure you do.  Show off your body for me."
            wt_image exhi_strip_7_2
            jasmine.c "My body?  But you can already see my body.  Can't you?"
            wt_image exhi_strip_7_3
            jasmine.c "Wait!  I need to get these clothes off first!  Then you can see my body better."
            wt_image exhi_strip_7_4
            jasmine.c "There.  Is this a good show?"
            player.c "Yes, but I was hoping to watch you strip out of your clothes. Maybe a little slower and sexier?"
            wt_image exhi_strip_7_5
            jasmine.c "Mmmmm.  Strippers are sexy!  I like thinking about strippers."
            "[jasmine.name]'s too preoccupied thinking about strippers to be one for you right now."
        elif jasmine.bimbo_strip_count == 3:
            wt_image exhi_strip_7_2
            player.c "[jasmine.name], how about you put on a show for me."
            wt_image exhi_strip_7_1
            jasmine.c "A show?  I don't think I know how to do that."
            player.c "Sure you do.  Show off your body for me."
            wt_image exhi_strip_7_2
            jasmine.c "My body?  But you can already see my body.  Can't you?"
            wt_image exhi_strip_7_3
            jasmine.c "Wait!  You mean you want to watch me take my clothes off, right?"
            player.c "Right"
            wt_image exhi_strip_7_4
            "She rips off her clothes in record speed."
            jasmine.c "Was that a good show?"
            player.c "Perhaps next time you could go a little slower?"
            wt_image exhi_strip_7_5
            jasmine.c "That's a good idea.  This show has me worked up.  I need a moment to relax."
            "Relaxation appears to involve rubbing her fingers against her clit.  You spend a few minutes watching her relax herself before going on with your day."
    # stripper dances
    elif current_location == stage and jasmine.has_tag('showgirl'):
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        add tags 'watched_today' to jasmine
        $ jasmine.strip_outfit_count += 1
        if jasmine.strip_outfit_count > 5:
            $ jasmine.strip_outfit_count = 1
        if jasmine.strip_outfit_count == 1:
            wt_image exhi_strip_1_1
            "Jasmine looks stunning as she enters the stage."
            wt_image exhi_strip_1_2
            "Before long, the robe starts coming off..."
            wt_image exhi_strip_1_3
            "... not that you'd expect anything else from Jasmine."
            wt_image exhi_strip_1_4
            "Perhaps the wonder was that she kept her clothes on until she reached the stage."
            wt_image exhi_strip_1_5
            "Regardless, she soon rectifies the problem ..."
            wt_image exhi_strip_1_6
            "... much to the pleasure of her appreciative audience."
        elif jasmine.strip_outfit_count == 2:
            # dildo show
            if jasmine.dildo_show_count > 1:
                wt_image exhi_strip_6_1
                "[jasmine.name] has a sly look on her face as she steps out onto the stage, as if she's hiding a secret."
                wt_image exhi_strip_6_2
                "She fiddles with her skirt, as if she's going to pull it down ..."
                wt_image exhi_strip_6_3
                "... then she flips up the front of it instead."
                wt_image exhi_strip_6_4
                "She spins around, as if to confirm: no panties here."
                wt_image exhi_strip_6_5
                "No bra, either."
                wt_image exhi_strip_6_6
                "She has one more surprise hidden away in the sofa behind her, and she's pretty excited about it ..."
                wt_image exhi_strip_6_7
                "... as the people in the front row can clearly see."
                wt_image exhi_strip_6_8
                "From behind the pillow she pulls out a dildo ..."
                wt_image exhi_strip_6_9
                "... which she then pushes into herself."
                wt_image exhi_strip_6_10
                "She shows off her flexibility to make sure the audience gets a good view of her show ..."
                wt_image exhi_strip_6_11
                "... as she thrusts the toy in and out of herself faster and faster and faster ..."
                wt_image exhi_strip_6_12
                "... until she bucks to a climax that everyone in the audience, not just the people in the front row, can tell that she thoroughly enjoyed."
                jasmine.c "oooooohhh!!"
                wt_image exhi_strip_6_13
                "To the sounds of a standing ovation, an exhausted [jasmine.name] slumps to the floor of the stage, wondering who might have been in the crowd watching her fuck herself to orgasm?"
                add tags 'dildoed_on_stage' to jasmine
            # regular show
            else:
                wt_image exhi_strip_3_1
                "Jasmine struts onto the stage, ignoring the crowd.  Then she stops and looks over her shoulder, as if she's noticing them for the first time."
                wt_image exhi_strip_3_2
                "She stares out at the crowd, as if debating what to do ..."
                wt_image exhi_strip_3_3
                "... then pulls down her top."
                wt_image exhi_strip_3_4
                "She tries her best to look innocent about the whole thing ..."
                wt_image exhi_strip_3_5
                "... but she can't disguise her growing arousal for long."
                wt_image exhi_strip_3_6
                "She spins around ..."
                wt_image exhi_strip_3_7
                "... wiggles her butt ..."
                wt_image exhi_strip_3_8
                "... then squats down ..."
                wt_image exhi_strip_3_9
                "... and presents her forward assets for inspection."
                wt_image exhi_strip_3_10
                "[jasmine.name] makes sure the crowd also gets a good look at her rear assets on her way off the stage."
        elif jasmine.strip_outfit_count == 3:
            wt_image exhi_strip_2_6
            "Jasmine looks surprised as she steps out on the stage, as if she wasn't expecting anybody to be there."
            wt_image exhi_strip_2_7
            "She gives the crowd a look, as if to ask, 'What are you looking at ...'"
            wt_image exhi_strip_2_8
            "'... these?'"
            wt_image exhi_strip_2_1
            "She wasn't wearing much when she wandered onto the stage."
            wt_image exhi_strip_2_2
            "She promptly proceeds to lose even that."
            wt_image exhi_strip_2_3
            "She looks at the crowd, as if to ask 'Is this what you wanted to see?'"
            wt_image exhi_strip_2_4
            "'Or were you hoping for more?'"
            wt_image exhi_strip_2_5
            "'Or possibly nothing at all?'  [jasmine.name] seems happier naked on the stage than she was clothed.  The crowd's happier, too."
        elif jasmine.strip_outfit_count == 4:
            wt_image exhi_strip_4_1
            "[jasmine.name] enters the stage dressed more like the girl next door than a show girl, and you know that's no accident."
            wt_image exhi_strip_4_2
            "This show is for her.  Just a girl next door out for a walk ..."
            wt_image exhi_strip_4_3
            "... who shows off more than a 'good girl' should ..."
            wt_image exhi_strip_4_4
            "... who somehow loses her skirt ..."
            wt_image exhi_strip_4_5
            "... and her top ..."
            wt_image exhi_strip_4_6
            "... who ends up naked ..."
            wt_image exhi_strip_4_7
            "... and exposed ..."
            wt_image exhi_strip_4_8
            "... and likes it!"
            if jasmine.dildo_show_count > 1:
                wt_image exhi_strip_4_9
                "Likes it so much, in fact ..."
                wt_image exhi_strip_4_10
                "... that she starts fingering herself ..."
                wt_image exhi_strip_4_11
                "... and then dildoing herself ..."
                wt_image exhi_strip_4_12
                "... thrusting the toy in and out of her wet sex, faster and faster and faster ..."
                wt_image exhi_strip_4_13
                "... until she fucks herself to climax in front of a group of strangers."
                jasmine.c "ooooohhhh!!"
                add tags 'dildoed_on_stage' to jasmine
        elif jasmine.strip_outfit_count == 5:
            wt_image exhi_strip_5_1
            "[jasmine.name] enters the stage dressed as a schoolgirl."
            wt_image exhi_strip_5_2
            "It seems out of place for [jasmine.name], and makes you wonder how young she was when she first started having exhibitionist fantasies?"
            wt_image exhi_strip_5_3
            "Was she thinking about flashing her panties when she should have been listening to her lessons?"
            wt_image exhi_strip_5_4
            "Or perhaps she spent her time thinking about ..."
            wt_image exhi_strip_5_5
            "... flashing something more?"
            wt_image exhi_strip_5_6
            "Her actions wouldn't have been appropriate in school .."
            wt_image exhi_strip_5_7
            "... but they're a big hit on the stage of the Club."
            if jasmine.club_sex_status > 1:
                wt_image exhi_strip_5_8
                "Jasmine's a little slow leaving the stage.  She looks a bit flustered as she pulls her clothes back on while the crowd claps."
                $ title = "Join her on stage?"
                menu:
                    "Yes, help her finish her show properly":
                        add tags 'sex_on_stage_today' to jasmine
                        wt_image exhi_strip_5_9
                        "The crowd claps louder as you jump on stage, assuming this is part of the act."
                        jasmine.c "What are you doing??"
                        player.c "Helping you finish your act, properly."
                        jasmine.c "Are you crazy?"
                        player.c "No, but you're wet."
                        jasmine.c "Of course I'm wet, I've been exposing myself ..."
                        wt_image exhi_strip_5_10
                        jasmine.c "... ooooo"
                        "She moans as you shove two fingers into her."
                        player.c "Good.  That's going to make it easier to fuck you."
                        jasmine.c "With everyone watching?"
                        wt_image exhi_strip_5_11
                        player.c "Of course with everyone watching."
                        "She bites her lip to keep from crying out as you enter her."
                        jasmine.c "nnnnnnnn"
                        wt_image exhi_strip_5_12
                        "She's not able to keep silent for long.  She looks out at the crowd watching her getting fucked and starts to moan out load."
                        jasmine.c "oooooo"
                        wt_image exhi_strip_5_13
                        "You pull her up on top and have her ride you. With the bright lights on the stage, she can't see who's in the audience, but she knows they're there, and she keeps looking out towards them as she fucks up and down on your hard dick."
                        jasmine.c "oooooo"
                        wt_image exhi_strip_5_14
                        "It's the thought of the people out there, watching her, as much as it is the feel of your cock inside her, that takes her over the edge."
                        jasmine.c "ooooo  ...  ooooohhhh!!"
                        if jasmine.club_sex_status == 2:
                            $ jasmine.club_sex_status = 3
                            wt_image exhi_strip_5_15
                            "Now it's your turn.  The two of you get down off the desk and she jerks you off while rubbing your cock against her soft tit."
                            wt_image exhi_strip_5_16
                            "A moment later, you cover her tit with white goo."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_strip_5_17
                            "The applause from the crowd is thunderous."
                            jasmine.c "Do you think they can see this?"
                            player.c "Easily.  That's why they're clapping."
                            jasmine.c "This is so hot.  My husband would never do anything like this with me.  I can't imagine doing this with anybody but you."
                            player.c "Next time let's give them a real show.  I'll deposit my load on your face instead of your tit."
                            jasmine.c "Oh!"
                            "That wasn't a no."
                            $ jasmine.gf_conversion_status += 1
                        else:
                            wt_image exhi_strip_5_15
                            "Now it's your turn.  The two of you get down off the desk and she jerks you off."
                            player.c "Aim at your face, [jasmine.name]."
                            wt_image exhi_strip_5_18
                            "She does as she's told, and you release your load."
                            player.c "[player.orgasm_text]"
                            wt_image exhi_strip_5_19
                            "You walk away and leave her there. The crowd claps wildly as she stares out at them, your cum dripping down her face, marking her as yours."
                            if not jasmine.has_tag('stage_facial'):
                                add tags 'stage_facial' to jasmine
                                change jasmine submission by 5
                                $ jasmine.club_sex_status = 4
                            $ jasmine.facial_count += 1
                        $ jasmine.sex_count += 1
                        $ jasmine.orgasm_count += 1
                        if jasmine.has_tag('girlfriend'):
                            $ jasmine.maintain_week_gf = week + 3
                        orgasm notify
                    "Not today":
                        wt_image exhi_strip_5_2
                        "You wait with the crowd as Jasmine makes her exit from the stage."
        wt_image current_location.image
        if not jasmine.has_tag('sex_on_stage_today'):
            if jasmine.has_tag ('continuing_actions') or jasmine.has_tag ('girlfriend'):
                $ title = "What now?"
                menu:
                    "Search for [jasmine.name] back stage":
                        wt_image exhi_club_shower_1_1
                        "You sneak back stage and go looking for [jasmine.name]. Poking your head into the women's change room, you hear a shower running. It's definitely [jasmine.name], cleaning off after her show."
                        $ title = "What do you do?"
                        menu:
                            "Join her for a blow job":
                                if jasmine.club_sex_status == 0:
                                    $ jasmine.club_sex_status = 1
                                wt_image exhi_club_shower_1_2
                                "She startles as you open the shower door ..."
                                jasmine.c "Shit!  You scared me."
                                wt_image exhi_club_shower_1_8
                                jasmine.c "I guess I see why you're here. Do you really want to do this now? Someone could walk in on us."
                                player.c "Would you mind?"
                                jasmine.c "I'm not sure.  Maybe not."
                                player.c "Then quit talking and wrap that sexy mouth of yours around my cock."
                                wt_image exhi_club_shower_1_9
                                "Dropping to her knees, she licks and suckles your cock ..."
                                wt_image exhi_club_shower_1_10
                                "... until you empty your balls into her waiting mouth."
                                player.c "[player.orgasm_text]"
                                wt_image exhi_club_shower_1_11
                                player.c "Did anyone walk in on us?"
                                jasmine.c "Nope"
                                player.c "Disappointed?"
                                jasmine.c "Hmmm.  Not sure."
                                "She milks the last of the cum out of you, kisses the tip of your cock, then shoos you away so she can finish her shower."
                                $ jasmine.blowjob_count += 1
                                $ jasmine.swallow_count += 1
                                if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 2:
                                    $ jasmine.maintain_week_gf = week + 2
                                orgasm notify
                            "Join her for sex":
                                if jasmine.club_sex_status == 0:
                                    $ jasmine.club_sex_status = 1
                                wt_image exhi_club_shower_1_2
                                "She startles as you open the shower door ..."
                                jasmine.c "Shit!  You scared me."
                                wt_image exhi_club_shower_1_8
                                jasmine.c "I guess I see why you're here. Do you really want to do this now? Someone could walk in on us."
                                player.c "Would you mind?"
                                jasmine.c "I'm not sure.  Maybe not."
                                player.c "Then turn around."
                                wt_image exhi_club_shower_1_12
                                "She's wet, and not just from the shower.  You slide into her easily."
                                player.c "Keep your eyes on the door.  If anyone walks in on us, make sure they can see everything I'm doing with you."
                                jasmine.c "ooooo"
                                wt_image exhi_club_shower_1_13
                                "You begin pounding into her, and she starts trembling almost immediately. She's already worked up by her show, and between that and the thought of someone walking in and catching the two of you, she cums quickly as you fuck her."
                                jasmine.c "ooooo  ...   oooohh!!"
                                "You don't last much longer."
                                player.c "[player.orgasm_text]"
                                wt_image exhi_club_shower_1_7
                                player.c "Did anyone walk in on us?"
                                jasmine.c "Nope"
                                player.c "Disappointed?"
                                jasmine.c "Hmmm.  Not sure.  Now shoo.  I need to finish my shower."
                                $ jasmine.sex_count += 1
                                if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 3:
                                    $ jasmine.maintain_week_gf = week + 3
                                orgasm notify
                            "Go pleasure her":
                                if jasmine.club_sex_status == 0:
                                    $ jasmine.club_sex_status = 1
                                wt_image exhi_club_shower_1_2
                                "She startles as you open the shower door ..."
                                jasmine.c "Shit!  You scared me."
                                wt_image exhi_club_shower_1_4
                                "... then startles more as you wrap your lips around her nipple."
                                jasmine.c "Oh!  Wait!  Someone could walk in on us."
                                player.c "Let them."
                                jasmine.c "ooooo"
                                wt_image exhi_club_shower_1_5
                                jasmine.c "oooooo  ...   damn that feels good!"
                                wt_image exhi_club_shower_1_6
                                "It seems to feel even better when you lower your mouth to between her legs. She's already worked up by her show, and between that and the thought of someone walking in and catching the two of you, she cums quickly against your lapping tongue."
                                jasmine.c "ooooo  ...   oooohh!!"
                                wt_image exhi_club_shower_1_7
                                jasmine.c "Damn.  That felt good!  I hope that's your way of saying you enjoyed my show."
                                $ jasmine.orgasm_count += 1
                                if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 3:
                                    $ jasmine.maintain_week_gf = week + 3
                                change player energy by -energy_short notify
                            "Just watch her":
                                wt_image exhi_club_shower_1_2
                                "You're only able to spy on her for a few minutes before she spots you."
                                if jasmine.dildo_show_count > 1:
                                    jasmine.c "Shit!  I didn't hear you sneak in.  I guess I should let you watch me finish my show."
                                    wt_image exhi_club_shower_1_3
                                    "She redirects the water to spray directly between her legs, and plays with her tits as you watch her. She's worked up from the show, and cums quickly."
                                    jasmine.c "ooooo  ...   oooohh!!"
                                    $ jasmine.orgasm_count += 1
                                    if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 2:
                                        $ jasmine.maintain_week_gf = week + 2
                                else:
                                    jasmine.c "Shit!  I didn't hear you sneak in.  Show's over.  Let me finish my shower in private."
                                change player energy by -energy_very_short notify
                    "Wait for her to come out" if jasmine.club_sex_status > 0:
                        # no public club sex yet?
                        if jasmine.club_sex_status < 2:
                            wt_image exhi_club_sex_1_1
                            "You walk up behind [jasmine.name] when she returns from back stage, and place your hand on your breast."
                            jasmine.c "Hey!  What are you doing??"
                            wt_image exhi_club_sex_1_2
                            player.c "Starting something."
                            jasmine.c "Not here!"
                            player.c "Why not?  That's what the Club is for."
                            jasmine.c "Not here in the public area where everyone can see us."
                            player.c "Sure here.  People fuck where others can watch them all the time in the Club."
                            "That's only partially true. It happens in the swingers room, but otherwise people tend to retire to a private room. It's almost unheard of to have a couple fucking in the hallway where other members are coming and going, but it's not strictly against the rules."
                            if jasmine.has_tag('dildoed_on_stage') and jasmine.downtown_sex > 1:
                                $ jasmine.club_sex_status = 2
                                jasmine.c "You're making a spectacle of us."
                                player.c "So?  You liked it when people watched you fuck yourself with a dildo."
                                jasmine.c "That was part of a show."
                                player.c "I can take you up on the stage and fuck you there, if you prefer?"
                                jasmine.c "No!!"
                                player.c "Then let's do it here.  Maybe no one will see us?"
                                wt_image exhi_club_sex_1_4
                                jasmine.c "Lots of people will see us.  This hallway's busy."
                                player.c "That turns you on, doesn't it?  People you don't know walking by and seeing you getting fucked."
                                jasmine.c "Yes"
                                wt_image exhi_club_sex_1_5
                                "She offers no further resistance as you stand her up and pull down her panties."
                                wt_image exhi_club_sex_1_6
                                "She settles down on your cock and starts riding you while craning her head around to check is anyone's watching her."
                                player.c "Turn around.  You'll be able to see better."
                                wt_image exhi_club_sex_1_7
                                "She does so just as some people walk by you, eliciting a moan of excitement from Jasmine."
                                jasmine.c "ooooo"
                                "Most of the Club members ignore you, although a few chuckle as they pass by, and a couple take a close look before moving on."
                                wt_image exhi_club_sex_1_8
                                "It's only when one woman stops to tease Jasmine, though, that she really loses herself in the situation."
                                passerby_in_club_jasmine_1 "I see someone's too horny to get a room. Or are you just too much of a slut to know you shouldn't fuck where strangers can see you?"
                                jasmine.c "oooohh!!"
                                passerby_in_club_jasmine_1 "Did you just cum while I was talking to you?  You really are quite the whore exhibitionist."
                                wt_image exhi_club_sex_1_9
                                "Jasmine's had her fun.  Now it's your turn. You lay her on her back so you can control the pace and angle of entry to maximize your own pleasure."
                                "Jasmine pretty much ignores you as you're fucking her. She's too busy making eye contact with any Club member who happens by, which doesn't diminish your pleasure any."
                                player.c "[player.orgasm_text]"
                                wt_image exhi_club_sex_1_10
                                jasmine.c "That was ... edgy!"
                                player.c "Next time, how about we do it in front of a bigger audience?"
                                jasmine.c "Really?"
                                "Now you need to find the right time to introduce her to that experience."
                                $ jasmine.orgasm_count += 1
                                $ jasmine.sex_count += 1
                                if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 3:
                                    $ jasmine.maintain_week_gf = week + 3
                                orgasm notify
                            else:
                                wt_image exhi_club_sex_1_3
                                jasmine.c "No!  I'm not going to let you make a spectacle of us."
                                "If she got used to making more of a spectacle of herself, she might not be so adverse to the idea of doing so with you."
                        # if previous public club sex
                        else:
                            wt_image exhi_club_sex_1_1
                            "You walk up behind [jasmine.name] when she returns from back stage, and place your hand on your breast."
                            jasmine.c "Oh!"
                            wt_image exhi_club_sex_1_2
                            player.c "Ready to have people watch you fuck?"
                            jasmine.c "Again?"
                            "She's too turned on from her dance and the memory of the last time you fucked her in the public area of the Club to say no. She's putty in your hands - or at least a soft, ample boob-full in your hands."
                            $ title = "What do you want from her?"
                            menu:
                                "Blow job":
                                    wt_image exhi_club_sex_1_12
                                    player.c "I want a blow job, but lose the panties."
                                    jasmine.c "Why?"
                                    player.c "You'll see."
                                    wt_image exhi_club_sex_1_13
                                    "She takes off her underwear, then takes out your cock ..."
                                    wt_image exhi_club_sex_1_14
                                    "... then she looks around hopefully for an audience as she begins to lick you."
                                    $ title = "What do you do?"
                                    menu:
                                        "Tell her to spread her legs":
                                            wt_image exhi_club_sex_1_15
                                            player.c "Spread your legs.  Make sure everyone gets a good look at you while you blow me."
                                            "She moans in excitement at the instructions, and then again every time a Club member glances her way, regardless of whether the glance is one of interest or disapproval."
                                            jasmine.c "nnnnn  ...  nnnnn"
                                            "The feel of her moaning in arousal with your cock in her mouth has you at the brink in no time. You try to hold out as long as you can, to make her exposure last as long as you can, but that turns out not to be very long."
                                            player.c "[player.orgasm_text]"
                                        "Finger her while she blows you":
                                            wt_image exhi_club_sex_1_16
                                            "Holding her head down on your cock, you reach between her legs and finger her sopping wet snatch. She can't see people walking by in the position, but her imagination takes over."
                                            "She knows the spectacle she's making of herself and that, combined with the excitement of her just finished show and the feeling of your fingers working in and out of her sex take her quickly over the edge."
                                            jasmine.c "nnnnnn   nnnnnnn!!!"
                                            "The sound and feel of her cumming with your cock buried in her mouth triggers your climax, too, making this a short, if lewd, spectacle for the public area of the Club."
                                            player.c "[player.orgasm_text]"
                                            $ jasmine.orgasm_count += 1
                                    wt_image exhi_club_sex_1_3
                                    player.c "Was that as good as being fucked while people watched you?"
                                    jasmine.c "They were both kinda ... wrong and yet perfectly right."
                                    $ jasmine.blowjob_count += 1
                                    $ jasmine.swallow_count += 1
                                "Sex":
                                    wt_image exhi_club_sex_1_11
                                    "She stands up ..."
                                    wt_image exhi_club_sex_1_5
                                    "... and let's you pull down her panties."
                                    wt_image exhi_club_sex_1_6
                                    "You guide her onto your lap ..."
                                    wt_image exhi_club_sex_1_7
                                    "... but she immediately turns around to face out away from you, increasing her exposure to passing Club members."
                                    wt_image exhi_club_sex_1_8
                                    "She doesn't need anybody today to point out what an exhibitionist slut she's being. She knows that all too well, and after the excitement of giving her show, she's riding herself to climax in no time."
                                    jasmine.c "ooooo  ...  oooooo  ...  oooohh!!"
                                    wt_image exhi_club_sex_1_9
                                    "After she cums, Jasmine lies back and watches people passing by while you take your time and fuck her to your heart's content. She's seems happy to just lie there and make eye contact with as many Club members as she can, both those she knows and those she doesn't."
                                    "Some seem amused, others aroused or at least happy for her. And some clearly disapprove of the display. It's hard to say which reaction arouses Jasmine more."
                                    "The only thing you can say for certain is that when you finally cum, a pang of disappointment crosses Jasmine's face, as she knows the spectacle she's making of herself is about to come to an end."
                                    player.c "[player.orgasm_text]"
                                    $ jasmine.orgasm_count += 1
                                    $ jasmine.sex_count += 1
                            if jasmine.club_sex_status == 2:
                                wt_image exhi_club_sex_1_3
                                player.c "I still plan to fuck you in front of a larger audience one of these days."
                                jasmine.c "I don't know."
                                player.c "I do."
                                "You need to find the right time to introduce her to that experience."
                            if jasmine.has_tag('girlfriend') and jasmine.maintain_week_gf < week + 3:
                                $ jasmine.maintain_week_gf = week + 3
                            orgasm notify
                    "Go on with your day":
                        change player energy by -energy_very_short notify
            else:
                change player energy by -energy_very_short notify

    # continuing actions
    elif current_location == living_room and jasmine.has_tag('continuing_actions'):
        call jasmine_contact_visit_privateshow from _call_jasmine_contact_visit_privateshow
    else:
        "Not here."
    return

# Dildo Show
label jasmine_dildoshow:
    if current_location == bedroom:
        if jasmine.has_tag('girlfriend'):
            $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            # this command disables running into her downtown later today
            $ jasmine.downtown_event_checked_today = 2
            $ jasmine.dildo_show_count += 1
            # scroll 5 to 4 (events 1 and 2 are training only, 3 and 4 are repeatable)
            if jasmine.dildo_show_count > 4:
                $ jasmine.dildo_show_count = 3
            if jasmine.dildo_show_count == 1:
                call jasmine_contact_visit_dildoshow_1 from _call_jasmine_contact_visit_dildoshow_1_1
            elif jasmine.dildo_show_count == 2:
                call jasmine_contact_visit_dildoshow_2 from _call_jasmine_contact_visit_dildoshow_2_1
            elif jasmine.dildo_show_count == 3:
                call jasmine_contact_visit_dildoshow_3 from _call_jasmine_contact_visit_dildoshow_3_1
            else:
                call jasmine_gf_dildoshow_4 from _call_jasmine_gf_dildoshow_4
            if jasmine.maintain_week_gf < week + 2:
                $ jasmine.maintain_week_gf = week + 2
        elif jasmine.has_tag('bimbo'):
            $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            # this command disables running into her downtown later today
            $ jasmine.downtown_event_checked_today = 2
            wt_image exhi_dildo_2_8
            player.c "[jasmine.name], is your dildo working okay?  You haven't worn it out or broken it, have you?"
            jasmine.c "My pretend cock?  I think so.  Let me check."
            wt_image exhi_dildo_2_14
            jasmine.c "It tastes normal."
            $ title = "What do you suggest?"
            menu:
                "She try it standing up":
                    player.c "Why don't you try it standing up?"
                    wt_image exhi_dildo_2_1
                    jasmine.c "I am standing up!"
                    player.c "I meant, try it between your legs while you're standing up.  In your pussy."
                    wt_image exhi_dildo_2_2
                    jasmine.c "Oh, okay.  It fits in okay."
                    wt_image exhi_dildo_2_3
                    jasmine.c "Actually, it feels kinda good  ...  ooooo.  Maybe  ...  ooooo"
                    wt_image exhi_dildo_2_4
                    jasmine.c "Maybe real good?  ...  oooohh!!"
                    "It seems her dildo is functioning fine."
                "She try it sitting down":
                    player.c "Why don't you try it sitting down?"
                    wt_image exhi_dildo_2_5
                    jasmine.c "Okay.  It still tastes normal."
                    player.c "I meant, try it between your legs while you're sitting down.  In your pussy."
                    wt_image exhi_dildo_2_6
                    jasmine.c "Oh, okay.  It fits in okay."
                    wt_image exhi_dildo_2_7
                    jasmine.c "Actually, it feels kinda good  ...  ooooo.  Maybe  ...  ooooo"
                    wt_image exhi_dildo_2_11
                    jasmine.c "Maybe real good?  ...  oooohh!!"
                    "It seems her dildo is functioning fine."
                "She try it from behind":
                    player.c "Why don't you try it from behind?"
                    wt_image exhi_dildo_2_8
                    jasmine.c "I can't taste it when I hold it behind me."
                    player.c "I meant, try putting it between your legs from behind.  In your pussy."
                    wt_image exhi_dildo_2_9
                    jasmine.c "Oh, okay.  It fits in okay."
                    wt_image exhi_dildo_2_12
                    jasmine.c "Actually, it feels kinda good  ...  ooooo"
                    wt_image exhi_dildo_2_10
                    jasmine.c "Maybe  ...  oooooo"
                    wt_image exhi_dildo_2_13
                    jasmine.c "Maybe real good?  ...  oooohh!!"
                    "It seems her dildo is functioning fine."
        else:
            sys "We're not sure how [jasmine.name] made it to your bedroom with a dildo, but someone will need to add content for this new path."
    else:
        "Wait until the two of you are alone in the bedroom together, if you're expecting a special private show."
    return

# Additional Dildo Show only when GF = 4th
label jasmine_gf_dildoshow_4:
    wt_image exhi_dildo_3_1
    player.c "I want to watch you use your dildo on yourself again."
    jasmine.c "Okay"
    wt_image exhi_dildo_3_2
    "She gives the dildo a little lick ..."
    wt_image exhi_dildo_3_4
    "... slides it between her boobs ..."
    wt_image exhi_dildo_3_5
    "... and then into her welcoming snatch."
    wt_image exhi_dildo_3_6
    "She makes sure you have a good view ..."
    wt_image exhi_dildo_3_22
    "... then starts moving the dildo in and out ..."
    wt_image exhi_dildo_3_7
    jasmine.c "ooooo"
    wt_image exhi_dildo_3_21
    "... faster and faster ..."
    wt_image exhi_dildo_3_8
    jasmine.c "ooooo  ...   ooooooo"
    wt_image exhi_dildo_3_23
    "... until she bucks to climax at the end of the dildo, her eyes locked on yours, watching you watching her pleasure herself."
    jasmine.c "ooooo ....  ooohhhhh!!"
    $ jasmine.orgasm_count += 1
    if jasmine.test ('submission', 70):
        wt_image exhi_dildo_3_8
        "You don't have to say anything.  She knows you want to watch her lick her own juices, and she's feeling submissive enough to comply."
        wt_image exhi_dildo_3_24
        "She removes the dildo from between her legs ..."
        wt_image exhi_dildo_3_3
        "... and sucks it clean with her mouth as you watch."
        if not jasmine.has_tag( 'cleaned_dildo' ):
            change jasmine submission by 5 notify
            add tags 'cleaned_dildo' to jasmine
    else:
        wt_image exhi_dildo_3_10
        "When the orgasm subsides, she removes the dildo and puts it aside."
        jasmine.c "I hope you enjoyed the show."
    if jasmine.has_tag( 'showgirl' ):
        player.c "Who were you thinking about while you fucked yourself?  Me, or a club full of people watching you?"
        wt_image exhi_dildo_3_10
        jasmine.c "You're my boyfriend, so I'm supposed to say you, right?"
    $ title = "Tell her her boyfriend needs some attention?"
    menu:
        "Yes, have her blow you":
            player.c "Your boyfriend needs some attention after that show."
            wt_image exhi_dildo_3_10
            jasmine.c "Well, I wouldn't be much of a girlfriend if I didn't look after him, would I?"
            wt_image exhi_dildo_3_11
            "She squats down and unbuckles your pants."
            wt_image exhi_dildo_3_12
            "As your hardening cock springs free, she opens her mouth ..."
            wt_image exhi_dildo_3_13
            "... and accepts you inside."
            wt_image exhi_dildo_3_25
            "As she teases you with her talented lips and tongue, she holds up her breasts ..."
            wt_image exhi_dildo_3_14
            "... giving you a nice show to go along with the feel of her mouth pleasuring your cock.  It's not long before your balls are bubbling over."
            player.c "I'm going to cum, [jasmine.name]."
            wt_image exhi_dildo_3_15
            "She drops a hand between her legs and starts rubbing her clit furiously."
            $ title = "Where do you want to cum?"
            menu:
                "Wait until she finishes":
                    "You try and hold out until she's able to get herself off."
                    wt_image exhi_dildo_3_16
                    "Fortunately, it doesn't take her long."
                    jasmine.c "nnnnnnnnn"
                    "The sound of her moaning to a second orgasm, your cock buried in her mouth, takes you over the edge."
                    wt_image exhi_dildo_3_15
                    player.c "[player.orgasm_text]"
                    wt_image exhi_dildo_3_17
                    "It takes her a while to swallow your load, and even then some of it drips down her chin."
                    jasmine.c "Wow.  I can't believe how much jizz you shot in my mouth.  I think you liked watching that show almost as much as I liked doing it for you."
                    $ jasmine.orgasm_count += 1
                    $ jasmine.swallow_count += 1
                "Cum in her mouth":
                    wt_image exhi_dildo_3_18
                    "She wraps her lips tightly round your cock, ensuring none of your load escapes as you let go."
                    player.c "[player.orgasm_text]"
                    $ jasmine.swallow_count += 1
                "Cum on her tits":
                    wt_image exhi_dildo_3_19
                    "You pull out and aim your cock at her tits."
                    wt_image exhi_dildo_3_20
                    "Your load spurts out, coating her chest."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_dildo_3_26
                    jasmine.c "Wow!  I think you enjoyed my show."
            $ jasmine.blowjob_count += 1
            orgasm notify
        "No, end things there":
            change player energy by -energy_short notify
    return

# Roleplay Street Walking
label jasmine_street_walking_roleplay:
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    # this command disables running into her downtown later today
    $ jasmine.downtown_event_checked_today = 2
    call jasmine_update_media from _call_jasmine_update_media
    wt_image jasmine.image
    player.c "I'm in the mood to pick up a street walker, [jasmine.name]"
    if current_location == stage:
        jasmine.c "I was just about to start a show."
        player.c "I don't think they'll let a street walking whore like you on their stage, do you?"
        "She giggles."
        jasmine.c "Hmmmm.  Probably not.  Maybe I could find someplace where I can act like my true self?  I'll see you there in a few minutes."
    else:
        jasmine.c "Same corner as last time?"
        player.c "I'll see you there in a few minutes."
    call jasmine_contact_visit_streetwalking_roleplay from _call_jasmine_contact_visit_streetwalking_roleplay
    if jasmine.maintain_week_gf < week + 3:
        $ jasmine.maintain_week_gf = week + 3
    orgasm notify
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Client
label jasmine_contact:
    if jasmine.downtown_event_checked_today == 2:
        "You try to contact [jasmine.name], but can't reach her.  She must be up to something else today."
    else:
        # $ jasmine.add_tags( 'trained_today', 'trained_this_week' )  ## not yet: disables all actions
        # Jasmine has not yet agreed nor refused to be a showgirl
        if jasmine.stripper_discussion <= 1 and not jasmine.has_tag('showgirl'):
            if jasmine.has_tag('no_visits'):
                call jasmine_contact_showgirl from _call_jasmine_contact_showgirl
            else:
                $ title = "What do you want to talk to [jasmine.name] about?"
                menu:
                    "Becoming a showgirl":
                        call jasmine_contact_showgirl from _call_jasmine_contact_showgirl_1
                    "Coming to visit you":
                        call jasmine_contact_visit from _call_jasmine_contact_visit
        # Showgirl conversation has ended, only remaining option is coming to visit.
        else:
            call jasmine_contact_visit from _call_jasmine_contact_visit_1
        wt_image current_location.image
    return

# Contact - Showgirl
label jasmine_contact_showgirl:
  # if transformed and waiting for venue
  wt_image exhi_gf_conversation_2
  # First discussion
  if jasmine.stripper_discussion == 0:
    jasmine.c "Oh.  Hi.  What did you want to talk about?"
    player.c "[jasmine.name], I've been thinking about you.  In particular, I've been thinking we should find you a safe way to expose yourself in public whenever the mood strikes you."
    jasmine.c "I'm listening."
    if player.has_tag('club_first_visit_complete'):
      call jasmine_contact_showgirl_club from _call_jasmine_contact_showgirl_club
    else:
      player.c "I don't have the right venue picked out yet, but when I do, I will let you know."
      jasmine.c "Okay"
      $ jasmine.stripper_discussion = 1
      add tags 'waiting_for_club_access' to jasmine
  # Follow-up discussions
  elif jasmine.stripper_discussion == 1:
    jasmine.c "Hi. I don't suppose you've found a place I could work as a stripper yet, have you?"
    if player.has_tag('club_first_visit_complete') and not jasmine.has_tag('waiting_for_club_access'):
      player.c "As a matter of fact, I have."
      wt_image exhi_gf_conversation_1
      jasmine.c "Really?  Where??"
      if jasmine.has_tag('transformed_needs_location'):
        "You give [jasmine.name] directions to the Club. She'll do the rest."
        $ jasmine.transformed_via_object = True
        rem tags 'transformed_needs_location' from jasmine
        call jasmine_convert_showgirl from _call_jasmine_convert_showgirl
      else:
        call jasmine_contact_showgirl_club from _call_jasmine_contact_showgirl_club_1
    else:
      player.c "Not yet, but when I do, I will let you know."
      jasmine.c "Okay"
  return

# Contact - Showgirl - Explain Club
label jasmine_contact_showgirl_club:
  player.c "There's a private club that I'm a member of.  You never know exactly who you'll meet there.  Your boss may be there, or your husband's boss.  All club members, however, are sworn to secrecy."
  player.c "If anyone disclosed what they saw at the club... well, let's just say there would be unpleasant consequences."
  player.c "If you want the thrill of exposing yourself in a room full of clothed people, if you want the danger of not knowing who you know who may see you taking your clothes off, this may be the ideal place for you."
  if ( jasmine.modified_stat( 'sos' ) >= 70 ) or jasmine.test( 'desire', 100 ):
    wt_image exhi_gf_conversation_1
    jasmine.c "Wow.  That sounds... exactly perfect for me."
    "You make arrangements for [jasmine.name] to become a member of the Club."
    call jasmine_convert_showgirl from _call_jasmine_convert_showgirl_1
  else:
    wt_image exhi_gf_conversation_3
    jasmine.c "I don't know.  That sounds like being a stripper and I don't know if could do that. Thanks for the offer though. I think I'm happy just as I am."
    $ jasmine.stripper_discussion = 2
    if jasmine.has_tag( 'no_visits' ):
      jasmine.c "Thanks for all your help, but it's probably best if you don't contact me again."
      $ living_room.remove_action( jasmine.current_client_action )  # Disable contacting Jasmine.
  return

# Contact - Showgirl - Convince with Hypnosis
label jasmine_contact_showgirl_hypno:
  wt_image exhi_visit_strip_1
  "When [jasmine.name] shows up for her visit, you greet her with your focus in hand."
  player.c "[jasmine.name], look at this for me."
  call focus_image from _call_focus_image_29
  player.c "Listen to me, [jasmine.name]. Only me.  Only my words now.  Listen to and obey me, [jasmine.name]. I am your friend, and I want what is right for you. You will listen to and obey me."
  wt_image exhi_visit_strip_1
  player.c "Remove your top and show me your breasts while we talk, [jasmine.name]."
  wt_image exhi_visit_strip_2
  player.c "Taking your clothes off in public excites you, [jasmine.name]. You want to be a woman who takes her clothes off in public. It doesn't matter what other people think.  It's right for you. It feels good. It's what you want."
  player.c "I have a safe place for you [jasmine.name]. A place where you can take your clothes off while strangers watch you. Where you'll be safe. Where you can expose your body to strangers."
  player.c "That's what you want, isn't it [jasmine.name]?"
  wt_image exhi_visit_strip_3
  jasmine.c "Yes!"
  "In her excitement, she pulls up the front of her dress, seemingly unaware that she has done so."
  "[jasmine.name] will no longer object to working at The Club.  In fact, she'll relish it."
  call jasmine_convert_showgirl from _call_jasmine_convert_showgirl_2
  # this command tracks energy use and hypno counts
  $ jasmine.hypno_session()
  return

# Contact - Visit
label jasmine_contact_visit:
  # First contact
  if not jasmine.has_tag( 'continuing_actions' ):
    wt_image exhi_gf_conversation_2
    jasmine.c "Oh.  Hi.  What did you want to talk about?"
    player.c "[jasmine.name], I want you to continue to visit me, without your husband knowing."
    "For a moment, there's silence on the other end of the line."
    if jasmine.test( 'resistance', 1 ) or jasmine.test( 'submission', 70 ) or jasmine.test( 'desire', 95 ):
      "After the effects of your training, [jasmine.name] has a hard time saying no to you, even when she knows she should. Very quietly, she accedes to your request."
      jasmine.c "Okay"
      add tags 'continuing_actions' to jasmine
      call jasmine_contact_visit from _call_jasmine_contact_visit_2
    else:
      wt_image exhi_gf_conversation_3
      jasmine.c "I don't think that's a good idea."
      add tags 'no_visits' to jasmine  # Jasmine has refused to visit in the future.
  # Already agreed to visit
  else:
    summon jasmine
    # Offer hypnosis option if Jasmine refused to be a showgirl
    if player.can_hypno(jasmine) and jasmine.stripper_discussion == 2 and player.has_tag('club_first_visit_complete'):
      $ title = "Hypnotize her and resume showgirl discussion?"
      menu:
        "Yes, convince her under hypnosis":
          call jasmine_contact_showgirl_hypno from _call_jasmine_contact_showgirl_hypno
          call character_location_return(jasmine) from _call_character_location_return_318
        "Just have a regular visit with her":
          pass
          # call jasmine_contact_visit_menu
          #$ jasmine.location = living_room
        "Visit her at her house" if jasmine.has_item(lingerie) and jasmine.club_sex_status > 1 and jasmine.lingerie_show_status > 0:
          call jasmine_contact_visit_lingerieshow_hers from _call_jasmine_contact_visit_lingerieshow_hers
        "Have her act like a whore" if jasmine.whore_play_status != 9 and not jasmine.has_tag('discussed_streetwalking_today'):
          call jasmine_contact_visit_whore_training from _call_jasmine_contact_visit_whore_training
    # Otherwise just default to normal visit
    else:
      $ title = "What type of visit do you want?"
      menu jasmine_contact_visit_menu:
        "Have a regular visit with her":
          pass
          # call jasmine_contact_visit_menu
          #$ jasmine.location = living_room
        "Visit her at her house" if jasmine.has_item(lingerie) and jasmine.club_sex_status > 1 and jasmine.lingerie_show_status > 0:
          call jasmine_contact_visit_lingerieshow_hers from _call_jasmine_contact_visit_lingerieshow_hers_1
        "Have her act like a whore" if jasmine.whore_play_status != 9 and not jasmine.has_tag('discussed_streetwalking_today'):
          call jasmine_contact_visit_whore_training from _call_jasmine_contact_visit_whore_training_1
  return

## no longer needed
# Contact - Visit Menu
# label jasmine_contact_visit_menu:
#   ## NOTE: all of the below should be converted to normal actions
#   $ title = "What are you in the mood for?"
#   menu:
#     "Hypnotize her" if player.can_hypno(jasmine):
#       call jasmine_contact_visit_hypno
#     "Private show":
#       call jasmine_contact_visit_privateshow
#     "Lingerie show":
#       call jasmine_contact_visit_lingerieshow
#     "Dildo show":
#       call jasmine_contact_visit_dildoshow
#     "Blow job":
#       call jasmine_contact_visit_blowjob
#     "Foot job":
#       call jasmine_contact_visit_footjob
#     "Tit fuck":
#       call jasmine_contact_visit_titfuck
#     "Sex":
#       call jasmine_contact_visit_sex
#     "Have her act like a whore" if jasmine.whore_play_status != 9 and not jasmine.has_tag('discussed_streetwalking_today'):
#       call jasmine_contact_visit_whore_training
#     "Transform her with the potion" if player.has_item(transformation_potion) and not jasmine.has_tag('transformed'):
#       "You prepare a drink for when she arrives. A very special drink."
#       call jasmine_transformation_potion_timer
#     "Ask her to be your girlfriend" if not jasmine.has_tag( 'gf_asked_today' ) and not jasmine.has_tag('girlfriend'):
#       call jasmine_contact_visit_girlfriend
#   return

## no longer needed
# # Contact - Visit - Hypnosis
# label jasmine_contact_visit_hypno:
#   add tags 'hypno_alt' to jasmine   # This tag will enable the alternate (weekend and visit) set of hypnosis images. ## note: not sure this was actually done
#   add tags 'visiting' to jasmine    # This tag is used to distinguish visits from weekends in the hypnosis content. ## note: not sure this was actually done
#   #call jasmine_hypnosis_start
#   #call jasmine_contact_visit_hypno_menu
#   #$ jasmine.hypno_session()
#   # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
#   $ queue_action(jasmine.hypno_action)
#   rem tags 'visiting' from jasmine
#   rem tags 'hypno_alt' from jasmine
#   return

## no longer needed
# Contact - Visit - Hypnosis Menu
# label jasmine_contact_visit_hypno_menu:
#   $ title = "What do you want to do with her?"
#   menu:
#     "Have her blow you":
#       call jasmine_contact_visit_hypno_blowjob
#     "Work on her Desire":
#       call jasmine_desire_hypnosis
#     "Work on her Submission":
#       call jasmine_submission_hypnosis
#     "Work on her Resistance":
#       call jasmine_resistance_hypnosis
#   return

# # Contact - Visit - Hypnosis - Blow Job
# label jasmine_contact_visit_hypno_blowjob:
#   player.c "It feels good to expose yourself to me, [jasmine.name].  It excites you.  It excites me, too.  You'd like to see how excited you make me."
#   player.c "You want to feel how excited I am.  You want to thank me for giving you the chance to expose yourself."
#   player.c "Come here now, [jasmine.name], and show me how thankful you are to me."
#   wt_image exhi_weekend_hypno_8
#   "[jasmine.name] would blow you even if she wasn't hypnotized, but there's something special about watching her kneel in front of you and open her mouth while she's in a trance."
#   "She looks so cute and vulnerable, you can't help yourself from giving her mouth a hard, rough fucking."
#   "She simply kneels there, keeping her lips wrapped around your cock, and accepts the face fuck."
#   wt_image exhi_weekend_hypno_19
#   "You take your pleasure from her, emptying your load into her mouth."
#   player.c "[player.orgasm_text]"
#   player.c "Swallow it all, [jasmine.name]..."
#   wt_image exhi_weekend_hypno_20
#   player.c "...and lick my cock clean."
#   wt_image exhi_weekend_hypno_1
#   "Once she's done, you have her dress, then bring her out of the trance."
#   jasmine.c "Did you want to do anything with me today?"
#   player.c "I already have."
#   jasmine.c "You mean you just wanted to talk with me?"
#   player.c "Something like that."
#   change player energy by -energy_orgasm notify
#   return

# Contact - Visit - Private Show
label jasmine_contact_visit_privateshow:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  wt_image exhi_visit_strip_1
  player.c "Okay my little exhibitionist. Let's see what you have to show me."
  wt_image exhi_visit_strip_2
  "It's interesting that [jasmine.name] always seems more shy stripping in front of you than she does taking her clothes off in public."
  wt_image exhi_visit_strip_3
  "The intimacy of the one-on-one situation always leaves her emotionally off balance."
  wt_image exhi_visit_strip_4
  "She's exposing herself for your pleasure, not her own ... but that humiliation, combined with being naked while you are clothed, still stimulates her exhibitionist kink."
  wt_image exhi_visit_strip_5
  "And gives you a good show that even she enjoys by the end."
  change player energy by -energy_very_short notify
  call character_location_return(jasmine) from _call_character_location_return_319
  wt_image current_location.image
  return

# Contact - Visit - Lingerie Show
label jasmine_contact_visit_lingerieshow:
  if not jasmine.has_item( lingerie ):
    "You need to give her some lingerie first."
    if player.has_item( lingerie ):
      $ title = "Gift the lingerie to [jasmine.name]?"
      menu:
        "Yes":
          call jasmine_give_lingerie from _call_jasmine_give_lingerie
          player.c "Go show me how you look in it ... and out of it."
        "No":
          "You need to give her some lingerie first."
  if jasmine.has_item( lingerie ):
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if jasmine.lingerie_show_status == 0:
      $ jasmine.lingerie_show_status = 1
    call jasmine_contact_visit_lingerieshow_yours from _call_jasmine_contact_visit_lingerieshow_yours
    call character_location_return(jasmine) from _call_character_location_return_320
    wt_image current_location.image
  return

# Contact - Visit - Lingerie Show - Your House
label jasmine_contact_visit_lingerieshow_yours:
  $ jasmine.lingerie_outfit_count += 1
  if jasmine.lingerie_outfit_count == 2 and not jasmine.has_tag('bonus_lingerie'):
    $ jasmine.lingerie_outfit_count = 1 # only go to 2 if she bought herself more lingerie after you paid her to be your whore
  if jasmine.lingerie_outfit_count > 2:  # Loop back to one once all outfits have been shown.
    $ jasmine.lingerie_outfit_count = 1
  if jasmine.lingerie_outfit_count == 1:
    call jasmine_contact_visit_lingerieshow_yours_1 from _call_jasmine_contact_visit_lingerieshow_yours_1
  else:
    call jasmine_contact_visit_lingerieshow_yours_2 from _call_jasmine_contact_visit_lingerieshow_yours_2
  return

# Contact - Visit - Lingerie Show - Your House - Outfit 1
label jasmine_contact_visit_lingerieshow_yours_1:
  wt_image exhi_lingerie_1
  "[jasmine.name] changes into the underwear you bought her."
  wt_image exhi_lingerie_2
  jasmine.c "Do I look nice?"
  player.c "Always"
  wt_image exhi_lingerie_3
  jasmine.c "Then I guess I should give you a little show."
  wt_image exhi_lingerie_4
  jasmine.c "In case you want to see what my ass looks like in the outfit you bought me..."
  wt_image exhi_lingerie_5
  jasmine.c "... or what my tits look like out of it."
  wt_image exhi_lingerie_6
  jasmine.c "And if I forgot to mention it before - thanks for the sexy lingerie."
  $ title = "What do you tell her?"
  menu:
    "Thanks for the show":
      wt_image exhi_lingerie_7
      player.c "I'm glad you like it. Thanks for the show."
      change player energy by -energy_very_short notify
    "Thank me properly":
      player.c "I'm glad you like it.  Why don't you thank me properly for the gift?"
      wt_image exhi_lingerie_8
      "With a mischievous grin on her face, she sinks to her knees in front of you and fishes your hard cock out of your pants."
      jasmine.c "Thank you properly?  I suppose you were hoping for something like this."
      wt_image exhi_lingerie_9
      "Forming her soft hand into a fist, she pumps up and down gently on your cock."
      wt_image exhi_lingerie_10
      "Still pumping your shaft with her right hand, she starts massaging your balls with her left."
      wt_image exhi_lingerie_11
      "As the pressure in your balls builds, she presses your cock between her tits."
      wt_image exhi_lingerie_12
      player.c "[player.orgasm_text]"
      jasmine.c "Thanks for the sexy lingerie."
      orgasm notify
  return

# Contact - Visit - Lingerie Show - Your House - Outfit 2
label jasmine_contact_visit_lingerieshow_yours_2:
  wt_image exhi_lingerie_bonus_1
  "[jasmine.name] appears wearing barely there see through lingerie."
  wt_image exhi_lingerie_bonus_2
  jasmine.c "Do you like this?"
  wt_image exhi_lingerie_bonus_3
  jasmine.c "I found this on sale, and bought it with the money I earned being your \"whore.\""
  wt_image exhi_lingerie_bonus_4
  jasmine.c "It looked like something we could both enjoy."
  $ title = "What do you tell her?"
  menu:
    "It looks great":
      wt_image exhi_lingerie_bonus_5
      player.c "It looks great, [jasmine.name]."
      change player energy by -energy_very_short notify
    "Bend over":
      player.c "It'll look better when it's on the floor, and you finish bending over all the way."
      "A small smile crosses her face..."
      wt_image exhi_lingerie_bonus_6
      "...as she finishes removing the lingerie and kneels down, facing away from you. You slide your hard dick along the crack of her ass..."
      wt_image exhi_lingerie_bonus_8
      "Then push yourself into her wet snatch.  She moans as you enter her ..."
      jasmine.c "ooooo"
      wt_image exhi_lingerie_bonus_9
      "...and then again, louder, as you start fucking her."
      jasmine.c "oooooo"
      "Maybe she's thinking about you using her as a whore, or maybe she's just horny from showing off her lingerie..."
      wt_image exhi_lingerie_bonus_7
      "...either way, she cums quickly - rocking back on your hard dick and bringing you to the brink of your own orgasm."
      jasmine.c "oooooo  ...  oooohh!!"
      $ title = "Where do you want to cum?"
      menu:
        "In her":
          wt_image exhi_bimbo_outfit_7_19
          "You thrust into her, hard ... once, twice, three times ... burying your shaft as deep into her as it will go as you feel your balls boil over."
          player.c "[player.orgasm_text]"
          wt_image exhi_lingerie_bonus_10
          "She closes her eyes and sighs as you finish pumping the last of your load inside her."
          jasmine.c "Mmmmm. I'm glad you enjoyed the lingerie."
        "On her":
          wt_image exhi_lingerie_bonus_11
          "She gasps in surprises as you pull out and spurt your hot seed over her ass."
          player.c "[player.orgasm_text]"
          jasmine.c "Oh!"
          wt_image exhi_lingerie_bonus_12
          "She stays in position as you finish pumping your jizz onto her and watch it drip down her ass."
          jasmine.c "I'm glad you enjoyed the lingerie."
      orgasm notify
  return

# Contact - Visit - Lingerie Show - Her House
label jasmine_contact_visit_lingerieshow_hers:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  if jasmine.lingerie_show_status == 1:
    call jasmine_contact_visit_lingerieshow_hers_1 from _call_jasmine_contact_visit_lingerieshow_hers_1_1
  elif jasmine.lingerie_show_status == 2:
    call jasmine_contact_visit_lingerieshow_hers_2 from _call_jasmine_contact_visit_lingerieshow_hers_2
  elif jasmine.lingerie_show_status == 3:
    call jasmine_contact_visit_lingerieshow_hers_3 from _call_jasmine_contact_visit_lingerieshow_hers_3
  elif jasmine.lingerie_show_status == 4:
    call jasmine_contact_visit_lingerieshow_hers_4 from _call_jasmine_contact_visit_lingerieshow_hers_4
  call character_location_return(jasmine) from _call_character_location_return_321
  call forced_movement(living_room) from _call_forced_movement_577
  return

# Contact - Visit - Lingerie Show - Her House - 1st
label jasmine_contact_visit_lingerieshow_hers_1:
  wt_image exhi_gf_conversation_2
  player.c "I want to see you in your lingerie again, [jasmine.name]."
  jasmine.c "Okay, I'll be right over."
  player.c "Don't bother. I'll drop by your house."
  jasmine.c "What?  No!  My husband is home."
  player.c "He won't mind seeing you wearing your lingerie around the house, will he?"
  jasmine.c "No, he's used to me doing that, but he won't understand you coming over."
  player.c "Then don't tell him I'm there."
  jasmine.c "Are you kidding???  What if he catches us?"
  player.c "Exciting to think about, isn't it?"
  jasmine.c "No... yes, but..."
  player.c "I'll see you in a few minutes.  Make sure you're properly dressed for me."
  call forced_movement(outdoors) from _call_forced_movement_578
  summon jasmine
  wt_image exhi_lingerie_home_1
  "[jasmine.name] sees you coming and opens the door before you can knock."
  jasmine.c "You're insane!!  We shouldn't be doing this."
  player.c "Come on. You put your lingerie on for me.  You want to do this as much as I do."
  jasmine.c "I don't, I just want to get you out of here before you cause a scene.  Wait here a minute.  My husband's about to get in the shower."
  wt_image exhi_lingerie_home_2
  "A moment later she leads you into the kitchen."
  jasmine.c "We need to do this fast."
  player.c "Then get on with your show."
  wt_image exhi_lingerie_home_3
  "She begins to undress while you watch and her husband showers."
  wt_image exhi_lingerie_home_4
  "She's too much of a showgirl to go too quickly, even tough she knows she should rush."
  wt_image exhi_lingerie_home_5
  "And regardless of what she may say, she's enjoying this."
  wt_image exhi_lingerie_home_6
  "She likes taking her clothes off, especially in dangerous situations, and this is her most dangerous strip yet."
  player.c "Touch yourself."
  wt_image exhi_lingerie_home_7
  player.c "You're wet."
  jasmine.c "Yes"
  player.c "Show me."
  wt_image exhi_lingerie_home_8
  "She opens herself up so you can see how wet she is."
  player.c "Play with yourself."
  jasmine.c "No!  My husband..."
  player.c "The shower's still going."
  wt_image exhi_lingerie_home_9
  jasmine.c "Good!  Then you can get out of here before we get caught."
  player.c "Next time I want you to finger fuck yourself."
  jasmine.c "No ...  I ...  I'll think about it. There shouldn't be a next time. It's too dangerous! Just go!!"
  $ jasmine.lingerie_show_status = 2
  change player energy by -energy_short notify
  return

# Contact - Visit - Lingerie Show - Her House - 2nd
label jasmine_contact_visit_lingerieshow_hers_2:
  wt_image exhi_gf_conversation_2
  player.c "I want another show at your house, [jasmine.name]."
  jasmine.c "You're going to get us caught!"
  player.c "That's what makes it exciting.  It's exciting for you, too.  Don't deny it."
  jasmine.c "I'm not.  It's just ..."
  player.c "Good.  Then no shying away from that excitement.  After you strip for me, you're going to finger yourself."
  jasmine.c "I don't know ..."
  player.c "Yes you do.  I'll see you in a few minutes."
  call forced_movement(outdoors) from _call_forced_movement_579
  summon jasmine
  wt_image exhi_lingerie_home_1
  "[jasmine.name] greets you at the door again."
  jasmine.c "Shhh!  Just a minute.  I convinced my husband to go have a shower.   You can come in after he's showering."
  player.c "How'd you swing that?"
  jasmine.c "I told him I wanted to make love to him once he cleaned up."
  player.c "Naughty girl!  Did you tell him what you're doing for foreplay?"
  jasmine.c "No!!  Keep your voice down."
  wt_image exhi_lingerie_home_10
  "[jasmine.name] leads you back to the kitchen."
  wt_image exhi_lingerie_home_3
  "She seems a little nervous as she starts her show ..."
  wt_image exhi_lingerie_home_11
  "... but she eventually warms up ..."
  wt_image exhi_lingerie_home_5
  "... and enjoys herself."
  player.c "Play with yourself now."
  wt_image exhi_lingerie_home_7
  "She reaches a hand down between her legs."
  player.c "Not like that.  Lose the panties and open yourself up so I can watch."
  wt_image exhi_lingerie_home_12
  jasmine.c "I shouldn't ..."
  player.c "Yes you should.  Open your pussy up."
  wt_image exhi_lingerie_home_8
  player.c "See how wet your pussy is?  It wants something inside it."
  player.c "What's it going to be?  Your fingers or my cock?"
  jasmine.c "No!  I'll do it."
  wt_image exhi_lingerie_home_13
  "She puts two fingers inside herself and starts working them in and out."
  "The combination of exposing herself to you, and the danger of doing it in her home while her husband's here had her on the edge before she even touched herself."
  wt_image exhi_lingerie_home_14
  "A few hard strokes of her fingers and she's over the edge, cumming as quietly as she can, to avoid detection."
  jasmine.c "mmmmmm"
  wt_image exhi_lingerie_home_9
  jasmine.c "My husband!  I need to get to him before he comes looking for me."
  player.c "He's going to be impressed when he sees how wet you are for him."
  jasmine.c "Just go before he sees you!!"
  $ jasmine.lingerie_show_status = 3
  change player energy by -energy_short notify
  return

# Contact - Visit - Lingerie Show - Her House - 3rd
label jasmine_contact_visit_lingerieshow_hers_3:
  wt_image exhi_gf_conversation_2
  player.c "Time for you to provide me more home entertainment, [jasmine.name]."
  jasmine.c "Again?  Haven't you seen enough??"
  player.c "Yes, but we haven't done enough.  You seemed pretty excited by my last visit."
  player.c "I don't want you running off to fuck your husband when we're done this time."
  player.c "I want you to fuck me instead."
  jasmine.c "While my husband's in the house???  You're insane!"
  player.c "No.  Just horny.  You are, too, just at the thought of it.  The reality's going to be even better."
  jasmine.c "We can't!!  We shouldn't ..."
  player.c "I'll see you in a few minutes."
  call forced_movement(outdoors) from _call_forced_movement_580
  summon jasmine
  wt_image exhi_lingerie_home_1
  player.c "Where's your husband?  In the shower again?"
  jasmine.c "Just about to get in."
  player.c "You didn't tell him you were going to fuck him again?"
  jasmine.c "No, I ... I told him he smells from the yardwork he was doing earlier."
  player.c "Good. Hopefully his scrub down will give us plenty of time. Unless of course you want me to take my time, to make it more likely he catches us?"
  jasmine.c "No!!  Make it quick."
  wt_image exhi_lingerie_home_2
  player.c "Since you can't wait to get my cock inside you, I guess we can pass on the show for today, but your get your top down. I want to see your tits bouncing while I fuck you."
  wt_image exhi_lingerie_home_4
  "She pulls down her top and lies down on the kitchen table."
  wt_image exhi_lingerie_home_15
  "She's sopping wet, and probably has been since you told her you were coming over to fuck her. She said she wanted this quick, and given how wet she is, there's no reason to take things slow. You slide your cock inside her..."
  wt_image exhi_lingerie_home_16
  "...and begin pounding her."
  "The whole situation has her so turned on, she immediately begins moaning..."
  jasmine.c "ooooo"
  wt_image exhi_lingerie_home_17
  "...and you need to quickly cover her mouth to keep her from crying out as she climaxes in record time."
  jasmine.c "nnnnnnn"
  wt_image exhi_lingerie_home_15
  "Her excitement augments your own, and you silently empty your load inside her as she gazes up at you."
  jasmine.c "That was ... amazing!!  Edgy, dangerous, exciting ... like nothing I've ever done before. Not with my husband. Not with anyone."
  player.c "I better go. The shower just stopped."
  jasmine.c "Yeah, okay.  Maybe..."
  player.c "Yes?"
  jasmine.c "Maybe we can do this again?"
  $ jasmine.lingerie_show_status = 4
  $ jasmine.gf_conversion_status += 1
  orgasm notify
  return

# Contact - Visit - Lingerie Show - Her House - 4th
label jasmine_contact_visit_lingerieshow_hers_4:
  player.c "Ready for me to visit you at home again?"
  wt_image exhi_whore_1_24
  jasmine.c "I can't wait!"
  call forced_movement(outdoors) from _call_forced_movement_581
  summon jasmine
  wt_image exhi_lingerie_home_18
  player.c "Where's your husband?"
  jasmine.c "Shhh.  Puttering around in the bathroom, I think."
  player.c "He's not in the shower."
  jasmine.c "Nope"
  player.c "Want me to come by later?"
  jasmine.c "No, just be quiet."
  wt_image exhi_lingerie_home_19
  jasmine.c "Are you going to fuck me again?  You'll need to be quick.  He could come in here at any time."
  $ title = "What do you want?"
  menu:
    "Fuck her":
      wt_image exhi_lingerie_home_24
      jasmine.c "Good. I'm ready for you."
      wt_image exhi_lingerie_home_25
      "You turn her around and push into her. She is indeed ready for you."
      wt_image exhi_lingerie_home_26
      "In fact, she starts moaning as soon as you begin thrusting in and out of her."
      jasmine.c "ooooo"
      wt_image exhi_lingerie_home_27
      "You pull her off the table and wrap a hand around her mouth to keep her from calling out as she cums.  You do a better job of stifling your own sounds as the feel of her bouncing up and down to climax on your cock takes you over the edge."
      jasmine.c "nnnnnn"
      player.c "------"
      wt_image exhi_lingerie_home_28
      player.c "You need to stay quiet.  Are you trying to get caught?"
      jasmine.c "I ... I don't know."
      wt_image exhi_lingerie_home_35
      husband_jasmine "Jasmine, where'd you go?"
      jasmine.c "I'll be right there!"
      "You make your exit as [jasmine.name] distracts her husband."
      $ jasmine.sex_count += 1
      $ jasmine.orgasm_count += 1
      orgasm notify
    "Eat her out":
      player.c "Feeling horny?"
      wt_image exhi_lingerie_home_24
      jasmine.c "Yes!  Look how wet my pussy is."
      wt_image exhi_lingerie_home_36
      player.c "That pussy does look like it needs attention."
      wt_image exhi_lingerie_home_37
      "She starts to squirm and wriggle her hips from the moment your tongue touches her already sensitive sex ..."
      wt_image exhi_lingerie_home_38
      "... and when you start licking her properly, she begins to moan."
      jasmine.c "oooo"
      wt_image exhi_lingerie_home_39
      player.c "Shhh. You need to stay quiet."
      wt_image exhi_lingerie_home_40
      "She nods, and you resume lapping her now sopping slit.  Just then, her husband calls to her."
      husband_jasmine "Jasmine, where are you?"
      jasmine.c "Just a moment. I'm ...  I'm ...."
      wt_image exhi_lingerie_home_38
      jasmine.c "ooohh"
      husband_jasmine "Did you say you were coming?  Where are you, in the kitchen?"
      wt_image exhi_lingerie_home_41
      jasmine.c "No!  I mean, yes, but ... stay there!  I've finished here."
      wt_image exhi_lingerie_home_4
      "You make a discrete exit as Jasmine distracts her husband."
      husband_jasmine "Honey, are you feeling okay?  You look flushed."
      jasmine.c "I feel great!  Thanks for asking."
      $ jasmine.orgasm_count += 1
      change player energy by -energy_short notify
    "Have her blow you":
      player.c "How about you blow me instead?"
      wt_image exhi_lingerie_home_29
      jasmine.c "Okay"
      player.c "Uhh, maybe we shouldn't do this right in the doorway?"
      wt_image exhi_lingerie_home_21
      jasmine.c "Don't worry.  I can get you off quick."
      player.c "I know, but ..."
      wt_image exhi_lingerie_home_30
      jasmine.c "Shhhh.  You keep talking and we're going to get caught."
      wt_image exhi_lingerie_home_31
      "She's right, both about being able to get you off quick, and that it'd be safest if you simply shut up and let her do so."
      wt_image exhi_lingerie_home_22
      husband_jasmine "Jasmine, have you seen my white shirt?"
      wt_image exhi_lingerie_home_32
      jasmine.c "Just a second, I'll look in the laundry room."
      wt_image exhi_lingerie_home_23
      husband_jasmine "Did you find it?"
      jasmine.c "Yes.  Wait a minute and I'll bring it to you.  I'm just finishing something off first."
      wt_image exhi_lingerie_home_33
      player.c "[player.orgasm_text]"
      wt_image exhi_lingerie_home_34
      husband_jasmine "What about my grey socks?"
      jasmine.c "Yes, they're here too.  Just wait.  I'll bring them and the shirt.  I just need to clean up a little mess."
      husband_jasmine "Did you spill something?"
      jasmine.c "Sort of."
      "She motions for you to make your exit as she cleans herself off, grabs her husband's clothes, and goes off to distract him."
      $ jasmine.blowjob_count += 1
      $ jasmine.facial_count += 1
      orgasm notify
    "Just have her strip":
      player.c "Just put on a show for me."
      wt_image exhi_lingerie_home_5
      jasmine.c "Okay"
      wt_image exhi_lingerie_home_6
      jasmine.c "Do you like it so far?"
      player.c "Absolutely"
      wt_image exhi_lingerie_home_12
      jasmine.c "Then you'll probably love it ..."
      wt_image exhi_lingerie_home_8
      jasmine.c "... when I do this ..."
      wt_image exhi_lingerie_home_13
      jasmine.c "... and this."
      wt_image exhi_lingerie_home_14
      "[jasmine.name] certainly loves it, as she demonstrates by cumming just as her husband calls out looking for her."
      jasmine.c "oooohh!!"
      husband_jasmine "[jasmine.name]?"
      wt_image exhi_lingerie_home_9
      jasmine.c "Coming!"
      "Not quite true. More accurate would be she just came. You find your own way out as [jasmine.name] distracts her husband."
      husband_jasmine "Are you naked again?"
      jasmine.c "Sorry, you know how I get sometimes."
      $ jasmine.orgasm_count += 1
      change player energy by -energy_very_short notify
  return

# Contact - Visit - Dildo Show
label jasmine_contact_visit_dildoshow:
  if not jasmine.has_item( dildo ):
    "You need to give her a toy first."
    if player.has_item( dildo ):
      $ title = "Gift the dildo to [jasmine.name]?"
      menu:
        "Yes":
          jasmine.c "What do you expect me to do with that?"
          player.c "Can't you guess?"
          "She blushes."
          give 1 dildo from player to jasmine notify
        "No":
          "You need to give her a toy first."
  # If Jasmine already had a dildo, or the player gave her one above
  if jasmine.has_item( dildo ):
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ jasmine.dildo_show_count += 1
    if jasmine.dildo_show_count == 1:
      call jasmine_contact_visit_dildoshow_1 from _call_jasmine_contact_visit_dildoshow_1
    elif jasmine.dildo_show_count == 2:
      call jasmine_contact_visit_dildoshow_2 from _call_jasmine_contact_visit_dildoshow_2
    else:
      call jasmine_contact_visit_dildoshow_3 from _call_jasmine_contact_visit_dildoshow_3
    call character_location_return(jasmine) from _call_character_location_return_322
    wt_image current_location.image
  return

# Contact - Visit - Dildo Show - 1st
label jasmine_contact_visit_dildoshow_1:
  wt_image exhi_weekend_hypno_1
  player.c "I want to watch you use your dildo on yourself."
  jasmine.c "I don't know."
  player.c "Try it. It's just another form of exhibitionism. Get your clothes off."
  wt_image exhi_dildo_1_1
  "She doesn't look completely sold, but she does like removing her clothes in front of an audience. She unbuttons her skirt and slides it off her hips."
  player.c "That's it.  Show off that smoking hot body to me."
  wt_image exhi_weekend_hypno_3
  "Encouraged, she lifts her top."
  player.c "Nice. You have more than that to show me, don't you?"
  wt_image exhi_dildo_1_2
  "She sits down and takes hold of her panties ..."
  wt_image exhi_dildo_1_3
  "... pulling them to the side."
  player.c "Don't be shy. I want to see all of you, with nothing in the way."
  wt_image exhi_weekend_hypno_7
  "She removes her clothes completely and sits back down, offering you an unencumbered view."
  player.c "Good. Now show me what it looks like when your beautiful pussy takes something inside it."
  wt_image exhi_dildo_1_4
  "Slowly she slides a finger into herself. The ease with which it enters belies her body's excitement."
  if jasmine.private_expose_level > 2:
    player.c "I've seen you finger fuck yourself before. I want to see your pussy take something bigger.  Use the dildo on yourself."
  else:
    player.c "That's nice, but I want to see your pussy take something bigger. Use the dildo on yourself."
  wt_image exhi_dildo_1_5
  "She places the dildo between her legs and slowly pushes it inside. Despite the stoniness of her face, her body is turned on, and the dildo enters her as easily as her finger did."
  wt_image exhi_dildo_1_6
  player.c "Now fuck yourself with it while I watch."
  "She starts moving the dildo in and out."
  wt_image exhi_dildo_1_7
  "You watch her for a while, until it's clear she's hit a plateau. This is turning her on, but she's nervous, and she won't be able to cum from this, at least not today."
  wt_image exhi_dildo_1_8
  player.c "Thank you for the show, [jasmine.name]."
  jasmine.c "Was it okay?"
  player.c "It was great!  You're great."
  jasmine.c "Thanks. You wanted to see me cum, though, didn't you?"
  player.c "I did. The thought of fucking yourself while someone watches turns you on, doesn't it?"
  jasmine.c "It does. It's just so ... intimate.  I'm not sure I can."
  player.c "I'm sure you can. Just as I'm sure you can clean your juices off your toy with your mouth while I watch."
  if jasmine.test( 'submission', 70 ):
    wt_image exhi_dildo_1_9
    "She's feeling too submissive to you to say no, even though she finds it humiliating. She opens her mouth and cleans the dildo off with her tongue and lips while you watch."
    if not jasmine.has_tag( 'cleaned_dildo' ):
      change jasmine submission by 5 notify
      add tags 'cleaned_dildo' to jasmine
    $ title = "Tell her to blow you now?"
    menu:
      "Yes":
        player.c "Good girl.  Now you can put your mouth to another use."
        call jasmine_contact_visit_dildoshow_bj from _call_jasmine_contact_visit_dildoshow_bj
      "No, end things here":
        change player energy by -energy_short notify
        return
  else:
    "She shakes her head."
    jasmine.c "No, that would just be ... weird."
    $ title = "Ask her to blow you now?"
    menu:
      "Yes":
        player.c "Would it be weird if I told you I want you to blow me now?"
        jasmine.c "No"
        call jasmine_contact_visit_dildoshow_bj from _call_jasmine_contact_visit_dildoshow_bj_1
      "No, end things here":
        change player energy by -energy_short notify
        return
  return

# Contact - Visit - Dildo Show - 2nd
label jasmine_contact_visit_dildoshow_2:
  wt_image exhi_weekend_hypno_1
  player.c "I want to watch you use your dildo on yourself."
  jasmine.c "Again?  Did you like watching me that much?"
  player.c "I'm going to enjoy watching you even more this time.  This time I want you to relax and let yourself cum."
  wt_image exhi_dildo_1_1
  jasmine.c "I don't know if I'll be able to do that."
  player.c "You will.  This is just another form of exhibitionism.  Except instead of showing off your body, you're showing off your private pleasure for me to watch."
  wt_image exhi_weekend_hypno_7
  jasmine.c "Is that really the same?"
  player.c "Picture this: Instead of you sitting here in my living room, you're on a bench at the park."
  wt_image exhi_dildo_1_15
  player.c "You lift up your skirt and push your dildo inside you."
  wt_image exhi_dildo_1_7
  player.c "Two women walking down the path see what you're doing and stare at you as they pass."
  jasmine.c "ooooooo"
  wt_image exhi_dildo_1_16
  player.c "It gets better. An old man sits down on the bench beside you and watches as you fuck yourself to climax."
  jasmine.c "oooooo ... ooohhhhhh!!!"
  "That didn't take long."
  $ jasmine.orgasm_count += 1
  if jasmine.test( 'submission', 70 ):
     "You don't have to say anything this time. She knows you want to watch her lick her own juices, and she's feeling submissive enough to comply."
     "She removes the dildo from between her legs and sucks it clean with her mouth as you watch."
     wt_image exhi_dildo_1_17
     if not jasmine.has_tag( 'cleaned_dildo' ):
       change jasmine submission by 5 notify
       add tags 'cleaned_dildo' to jasmine
  else:
    wt_image exhi_dildo_1_18
    "You're disappointed to see her remove the dildo and put it aside. You'd like to watch her lick her own juices off the toy, but she's not feeling submissive enough to do that for you."
  player.c "You're thinking about where you can dildo yourself in front of an audience, aren't you?"
  if jasmine.has_tag( 'showgirl' ):
    jasmine.c "I know exactly where I can dildo myself in front of an audience."
  else:
    jasmine.c "Yes"
  $ title = "Tell her to thank this audience first?"
  menu:
    "Yes, have her blow you":
      player.c "I think you should thank this audience, before you go find another one."
      jasmine.c "Okay"
      call jasmine_contact_visit_dildoshow_bj from _call_jasmine_contact_visit_dildoshow_bj_2
    "No, end things there":
      change player energy by -energy_short notify
  return

# Contact - Visit - Dildo Show - 3rd+
label jasmine_contact_visit_dildoshow_3:
  wt_image exhi_weekend_hypno_1
  player.c "I want to watch you use your dildo on yourself again."
  jasmine.c "Okay"
  wt_image exhi_dildo_1_19
  "She crawls onto the sofa, her ass positioned towards you ..."
  wt_image exhi_dildo_1_20
  "... and pulls away her clothes ..."
  wt_image exhi_dildo_1_21
  "... before sliding the dildo into her already wet snatch."
  wt_image exhi_dildo_1_22
  "In and out she slides the dildo ..."
  wt_image exhi_dildo_1_23
  "... faster and faster ..."
  jasmine.c "ooooo"
  wt_image exhi_dildo_1_24
  "... then faster still..."
  jasmine.c "ooooo ... ooooooo"
  wt_image exhi_dildo_1_25
  "... until she bucks to climax at the end of the dildo, her eyes locked on yours, watching you watching her pleasure herself."
  jasmine.c "ooooo ... ooohhhhh!!"
  $ jasmine.orgasm_count += 1
  if jasmine.test( 'submission', 70 ):
    wt_image exhi_dildo_1_17
    "You don't have to say anything this time. She knows you want to watch her lick her own juices, and she's feeling submissive enough to comply."
    "She removes the dildo from between her legs and sucks it clean with her mouth as you watch."
    if not jasmine.has_tag( 'cleaned_dildo' ):
      change jasmine submission by 5 notify
      add tags 'cleaned_dildo' to jasmine
  else:
    wt_image exhi_dildo_1_18
    "You're disappointed to see her remove the dildo and put it aside. You'd like to watch her lick her own juices off the toy, but she's not feeling submissive enough to do that for you."
  if jasmine.has_tag( 'showgirl' ):
    player.c "Was that as fun as doing it on stage in front of an audience full of strangers?"
    jasmine.c "No, but it was still fun."
  $ title = "Tell her it's your turn?"
  menu:
    "Yes, have her blow you":
      player.c "Time for me to have my fun."
      jasmine.c "Okay"
      call jasmine_contact_visit_dildoshow_bj from _call_jasmine_contact_visit_dildoshow_bj_3
    "No, end things there":
      change player energy by -energy_short notify
  return

# Contact - Visit - Dildo Show - Blowjob (Used by all 3 contact_visit_dildoshow Sub-Events)
label jasmine_contact_visit_dildoshow_bj:
  wt_image exhi_dildo_1_10
  "She opens her mouth to accept your hard cock. As she sucks you, she holds up her breasts, giving you a nice show to go along with the feel of her mouth pleasuring your cock."
  wt_image exhi_dildo_1_11
  "It's not long before your balls are bubbling over."
  player.c "I'm going to cum, [jasmine.name]."
  "She drops her tits and starts rubbing her clit furiously."
  $ title = "Where do you want to cum?"
  menu:
    "Wait until she finishes":
      wt_image exhi_dildo_1_12
      "You try and hold out until she's able to get herself off."
      "Fortunately, it doesn't take her long."
      jasmine.c "nnnnnnnnn"
      if jasmine.dildo_show_count == 1: # The 2nd and 3rd+ dildo shows have an orgasm prior, and use the "second" modifier, here.
        "The sound of her moaning to an orgasm, your cock buried in her mouth, takes you over the edge."
      else:
        "The sound of her moaning to a second orgasm, your cock buried in her mouth, takes you over the edge."
      player.c "[player.orgasm_text]"
      wt_image exhi_dildo_1_13
      "It takes her a while to swallow your load, and even then some of it drips down her chin."
      jasmine.c "Mmmm. I guess I was turned on by dildoing myself for you. You were pretty turned on, too."
      $ jasmine.orgasm_count += 1
    "Cum in her mouth":
      wt_image exhi_dildo_1_13
      player.c "[player.orgasm_text]"
      "She does her best to swallow your load, but some of it escapes and drips down her chin."
      jasmine.c "I guess you enjoyed that."
    "Cum on her tits":
      wt_image exhi_dildo_1_14
      "You pull out and spray your load on her tits."
      player.c "[player.orgasm_text]"
      "Some of it lands on her chin, and drips down onto her chest."
      jasmine.c "I guess you enjoyed that."
  orgasm notify
  return

# Contact - Visit - Blow Job
label jasmine_contact_visit_blowjob:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  wt_image exhi_visit_bj_1
  "[jasmine.name] shows up wearing something simple and easy to remove."
  wt_image exhi_visit_bj_2
  "Which is good, because it means even less time before she's on her knees ..."
  wt_image exhi_visit_bj_8
  "... giving you a blow job."
  wt_image exhi_visit_bj_3
  "She seems unwilling - or unable - to get very much of your cock in her mouth today ..."
  wt_image exhi_visit_bj_4
  "... so you follow her lead and deposit most of your cum outside of her mouth as well."
  wt_image exhi_visit_bj_6
  "You stop her as she's about to get up and clean herself."
  wt_image exhi_visit_bj_5
  player.c "Not yet, my little exhibitionist. I'm deciding whether I should take you for a walk outside like this?"
  wt_image exhi_visit_bj_7
  "She starts to laugh, then freezes when she realizes she's not 100% certain you're joking."
  $ jasmine.blowjob_count += 1
  $ jasmine.facial_count += 1
  orgasm notify
  call character_location_return(jasmine) from _call_character_location_return_323
  wt_image current_location.image
  return

# Contact - Visit - Foot Job
label jasmine_contact_visit_footjob:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  wt_image exhi_visit_fj_1
  "You show [jasmine.name] to the sofa when she arrives."
  wt_image exhi_visit_fj_2
  "She's not surprised when you ask her to take off her clothes."
  wt_image exhi_visit_fj_3
  "She {i}is{/i} surprised when you tell her to place her feet on your cock."
  wt_image exhi_visit_fj_4
  jasmine.c "Does this feel good?"
  player.c "It does.  Lie back so you can tickle my balls as well as stroke my cock."
  wt_image exhi_visit_fj_5
  "Grinning, she does as you ask."
  wt_image exhi_visit_fj_6
  "When she feels your hot jizz landing on her feet she gasps in surprise.  Perhaps she thought the foot job was just foreplay."
  wt_image exhi_visit_fj_7
  "Surprised or not, she's not unhappy with the experience."
  $ jasmine.footjob_count += 1
  orgasm notify
  call character_location_return(jasmine) from _call_character_location_return_324
  wt_image current_location.image
  return

# Contact - Visit - Tit Fuck
label jasmine_contact_visit_titfuck:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  wt_image exhi_visit_bj_1
  "[jasmine.name] shows up wearing something simple and easy to remove."
  wt_image exhi_visit_sex_1
  "Which makes it quick to get her stripped and flat on her back."
  wt_image exhi_visit_tf_1
  player.c "Lie down, [jasmine.name].  Face up.  I'm going to fuck your tits."
  wt_image exhi_visit_tf_4
  "You lubricate your cock and begin to thrust back and forth between [jasmine.name]'s large tits."
  wt_image exhi_visit_tf_5
  "She smiles up at you ..."
  wt_image exhi_visit_tf_2
  "... and can't resist licking the head of your cock when your thrusts get it close enough to her mouth."
  if jasmine.has_tag('visit_tf_facial'):
    wt_image exhi_visit_tf_6
    "This time, she knows what's 'cumming', and opens her mouth ..."
    wt_image exhi_visit_tf_3
    "... to receive the results of her effort."
  else:
    add tags 'visit_tf_facial' to jasmine
    wt_image exhi_visit_tf_3
    "For her efforts, she gets an unexpected spurt of jizz in her mouth, as without warning your balls empty their load up and over her beautiful tits and face."
  player.c "[player.orgasm_text]"
  $ jasmine.titfuck_count += 1
  $ jasmine.facial_count += 1
  orgasm notify
  call character_location_return(jasmine) from _call_character_location_return_325
  wt_image current_location.image
  return

# Contact - Visit - Sex
label jasmine_contact_visit_sex:
  $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
  wt_image exhi_visit_bj_1
  "[jasmine.name] shows up wearing something simple and easy to remove."
  wt_image exhi_visit_sex_1
  "Which makes it easier for her to get naked when you tell her you want to fuck."
  wt_image exhi_visit_sex_2
  "She's surprisingly ready considering the absence of foreplay ..."
  wt_image exhi_visit_sex_6
  "... allowing you to enter her easily ..."
  wt_image exhi_visit_sex_7
  "... and completely."
  jasmine.c "oooo"
  wt_image exhi_visit_sex_8
  "A few minutes of manipulation with your fingers and thumb as you fuck her, and her clit is standing at attention."
  jasmine.c "ooooo"
  wt_image exhi_visit_sex_3
  "The combination of your cock in her cunt and your hands on her breasts and clit soon brings her to orgasm."
  jasmine.c "ooooo  ...  ooohh!!"
  wt_image exhi_visit_sex_4
  "You turn her over into a position that lets you fuck her even deeper and harder."
  wt_image exhi_visit_sex_9
  "Despite having just orgasmed, she hovers on the brink of another as you pound into her."
  wt_image exhi_visit_sex_10
  "With a deep growl, you pull out of her and release your seed over her ass. She grins back at you."
  player.c "[player.orgasm_text]"
  wt_image exhi_visit_sex_5
  jasmine.c "Wow"
  "Neither of you say anything more."
  $ jasmine.orgasm_count += 1
  $ jasmine.sex_count += 1
  orgasm notify
  call character_location_return(jasmine) from _call_character_location_return_326
  wt_image current_location.image
  return

# Contact - Visit - Girlfriend
label jasmine_contact_visit_girlfriend:
  add tags 'gf_asked_today' to jasmine
  player.c "[jasmine.name], I think you should move in with me and become my girlfriend."
  if jasmine.gf_conversion_status == 0:
    wt_image exhi_gf_conversation_1
    jasmine.c "You're joking, right? I love my husband. You're ... I'm not sure what you are, other than delusional if you think I'm looking to leave my husband."
  elif jasmine.gf_conversion_status == 1:
    wt_image exhi_gf_conversation_1
    jasmine.c "Are you nuts? I love my husband. This is just ... sex."
  elif jasmine.gf_conversion_status == 2:
    wt_image exhi_gf_conversation_2
    jasmine.c "You're kidding, right? You wouldn't even be faithful to me. I can't see you ever settling for one woman."
    jasmine.c "Although maybe that's what I deserve, considering what I'm doing to my husband.  I do wonder sometimes whether he'd be better off without me. He deserves a wife who's devoted to him, not one running around doing ... the things I do with you."
  elif jasmine.gf_conversion_status == 3:
    # note: this test should be against raw desire
    if jasmine.desire >= 100 or jasmine.has_tag('love_potion_used'):
      call jasmine_contact_visit_girlfriend_agree from _call_jasmine_contact_visit_girlfriend_agree
    else:
      wt_image exhi_gf_conversation_2
      jasmine.c "That's ... surprisingly tempting. I know you wouldn't be faithful to me. I can't see you ever settling for one woman, but I think maybe that's what I deserve, considering what I'm doing to my husband. And he'd probably be better off without me. He deserves a wife who's devoted to him, not one running around doing ... the things I do with you."
      jasmine.c "It's just ... I love him, you know? It's hard thinking about a future without him."
  elif jasmine.gf_conversion_status >= 4:
    call jasmine_contact_visit_girlfriend_agree from _call_jasmine_contact_visit_girlfriend_agree_1
  if not jasmine.has_tag( 'girlfriend' ):
    add tags 'gf_asked_today' to jasmine
  return

# Contact - Visit - Girlfriend - Agree
label jasmine_contact_visit_girlfriend_agree:
  wt_image exhi_gf_conversation_3
  jasmine.c "I... wow, this is so hard."
  jasmine.c "I love him, you know. It's hard thinking about a future without him.  But that's me being selfish."
  jasmine.c "He'd be better off without me. He deserves a wife who's devoted to him, not one running around doing... the things I do with you."
  jasmine.c "And you, I know you won't be faithful to me. I can't see you ever settling for one woman, but I guess I'm okay with that."
  jasmine.c "The time I've spent with you, when I'm supposed to be with my husband..."
  jasmine.c "I get now how you can feel things for two different people at the same time, and it doesn't take away from what you feel for each of them."
  jasmine.c "At least I know what I'm getting, unlike my husband, who never asked for this."
  jasmine.c "Or maybe that's just me rationalizing my hormones, because you get me off in ways no one else ever has."
  jasmine.c "I feel guilty every time I sleep with my husband now, knowing that he can't get me off the same way, and that's got nothing to do with him."
  jasmine.c "That's me, and my problem, and you're the only one who's ever understood it and made it better for me."
  jasmine.c "So yeah, I'll be your girlfriend. Just give me some time to tell my husband I'm leaving him, and try to explain why."
  jasmine.c "I won't mention your name. He doesn't need to know that the guy he hired is the reason I'm going."
  call jasmine_convert_girlfriend from _call_jasmine_convert_girlfriend
  return

# Contact - Visit - Whore Training
label jasmine_contact_visit_whore_training:
    wt_image exhi_gf_conversation_2
    if jasmine.whore_play_status == 10:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "Just because you can't be a street whore any more doesn't mean you can't be my whore, Jiggles. Get your whore tits over to my place."
        summon jasmine
        wt_image exhi_whore_3_3
        "She arrives quickly."
        player.c "Are you wearing them?"
        wt_image exhi_whore_3_4
        "She knows exactly what you're talking about.  She pulls down her top to show the rings clipped to her nipples."
        jasmine.c "Yes"
        player.c "Get me hard, whore, while I decide how I'm going to fuck you."
        wt_image exhi_whore_3_8
        "She licks your cock ..."
        wt_image exhi_whore_3_9
        "... and your balls, while you decide what you want from her today."
        $ title = "What do you want to do with her?"
        menu menu_jasmine_whore_training_10:
            "Call her names":
                player.c "You're a dirty fucking whore, aren't you? Just a worthless street walking tramp."
                "She nods."
                player.c "Such a stupid cunt, trying to be a housewife and hold down a respectable office job when what you need is to be half naked and taking dick from any man who'll pay to fuck you."
                "She nods again."
                jump menu_jasmine_whore_training_10
            "Spit on her" if not jasmine.has_tag('spit_on_today'):
                wt_image exhi_whore_3_10
                "Grabbing her by the hair, you spit on her ... *pptew*"
                wt_image exhi_whore_3_16
                "... then you tilt her face back and spit on her again ... *pptew* ... watching as your saliva drips down her cheek."
                player.c "Now you look like the worthless tramp you are."
                add tags 'spit_on_today' to jasmine
                $ title = "What now?"
                jump menu_jasmine_whore_training_10
            "Face fuck her":
                wt_image exhi_whore_3_11
                "Grabbing her by the back of the head, you hold her steady as you push your cock into her mouth ..."
                wt_image exhi_whore_3_12
                "... as deep as it will go."
                wt_image exhi_whore_3_13
                "You give her a moment to control her gag reflex and take a deep breath ..."
                wt_image exhi_whore_3_14
                "... then skull fuck her, hard, as tears flow involuntarily down her cheek."
                wt_image exhi_whore_3_15
                "When you eventually empty your load down the back of her throat, it comes as a relief to her."
                player.c "[player.orgasm_text]"
                player.c "That's a good whore, swallow it all.  Do you miss getting fucked like this on the street?"
                "She looks away, avoiding eye contact, and lets your question go unanswered."
                $ jasmine.blowjob_count += 1
                $ jasmine.swallow_count += 1
                orgasm notify
            "Rough sex":
                player.c "Get your whore ass over that chair."
                wt_image exhi_whore_3_18
                "As she bends over, you shove yourself inside her. It's a tight fit, but she's wet enough that you can work yourself in without hurting her."
                player.c "Did you lube up before coming to visit me, whore, or is your whore cunt wet at the prospect of getting fucked like the tramp you are?"
                "There's a hint of a blush on her cheeks as she looks back at you."
                wt_image exhi_whore_3_19
                "You thrust into her, as hard and as fast as you can, pinning her down with your hands on her shoulders. You make the fuck as brutal and rough as you can ..."
                jasmine.c "ooooo"
                wt_image exhi_whore_3_20
                "... and yet despite that - or maybe because of that? - you feel her climax underneath you just before you cum yourself."
                jasmine.c "ooooo  ...  ooohh!!"
                player.c "[player.orgasm_text]"
                wt_image exhi_whore_3_3
                player.c "You miss being treated like the whore you are, don't you?"
                "She doesn't say anything, just gathers up her stuff and leaves."
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                orgasm notify
            "Have her demonstrate her street skills" if not jasmine.has_tag('spit_on_today'):
                player.c "Show me what you learned on the streets, whore."
                wt_image exhi_whore_3_31
                "She takes you into her mouth and starts sucking you."
                wt_image exhi_whore_3_32
                "It's a professional, energetic blow job, clearly intended to get you off quickly."
                $ title = "Let her get you off?"
                menu:
                    "Yes, continue like this":
                        wt_image exhi_whore_3_33
                        "You sit back and let her show you what she learned, walking the streets. You don't know how many men she's serviced ..."
                        wt_image exhi_whore_3_34
                        "... but she's learned a few things about using her tongue, teeth, and lips to get cocks off quickly once she has them in her mouth."
                        wt_image exhi_whore_3_35
                        "Your cock proves to be no exception."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_whore_3_36
                        player.c "Not bad.  Too bad you had to give up the street walking.  You're a natural whore."
                        "She avoids eye contact and cleans the last drips of cum off your cock, saying nothing."
                        $ jasmine.blowjob_count += 1
                        $ jasmine.swallow_count += 1
                    "Have her fuck you first":
                        player.c "Don't rush.  I want you to fuck me, too."
                        wt_image exhi_whore_3_37
                        "She climbs up on top of you ..."
                        wt_image exhi_whore_3_38
                        "... then spins around with your cock inside her ..."
                        wt_image exhi_whore_3_40
                        "... and starts riding you."
                        wt_image exhi_whore_3_39
                        "She's not aroused enough to truly get off on what she's doing, but like any good whore, she acts like she is ..."
                        jasmine.c "ooooooo"
                        wt_image exhi_whore_3_21
                        "... which helps get you off faster."
                        jasmine.c "ooooooo"
                        player.c "[player.orgasm_text]"
                        wt_image exhi_whore_3_22
                        player.c "Not bad.  Too bad you had to give up the street walking.  You're a natural whore."
                        "She climbs off of you and glances up at you, but says nothing."
                        $ jasmine.sex_count += 1
                orgasm notify
            "Jerk off on her":
                player.c "Get on your back."
                wt_image exhi_whore_3_7
                "She lies down and spreads her legs."
                wt_image exhi_whore_3_5
                player.c "You can close your legs, unless your whore cunt is so wet you need to play with it while I dump my load on your face."
                wt_image exhi_whore_3_28
                player.c "[player.orgasm_text]"
                "Instinctively, she brings her hand up to cover her hair as you jerk off above her face."
                player.c "Remove your hand, whore."
                wt_image exhi_whore_3_29
                "She moves her arm back to her side, letting you finish emptying your load unimpeded."
                wt_image exhi_whore_3_30
                player.c "You must enjoy this, getting used as a whore again."
                "She keeps her eyes and mouth shut, making no response."
                $ jasmine.facial_count += 1
                orgasm notify
        call character_location_return(jasmine) from _call_character_location_return_327
    elif jasmine.whore_play_status == 8:
        "This will change your relationship with Jasmine permanently."
        $ title = "Do you want to proceed?"
        menu:
            "No, not right now":
                jump jasmine_contact_visit_menu
            "Yes, show her what a whore she is":
                $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                player.c "I want you at my place in 30 minutes, whore."
                jasmine.c "I told you ..."
                player.c "And I told you, I know what you are.  You don't think I'm right?  Get your whore ass over her and I'll show you, tramp."
                summon jasmine
                wt_image exhi_weekend_hypno_13
                "She arrives promptly."
                player.c "Get your clothes off."
                wt_image exhi_whore_3_1
                "She pulls off her dress, then hesitates at her underwear."
                player.c "You can leave your panties on for now.  It's your tits I want to talk about."
                wt_image exhi_whore_3_2
                jasmine.c "My tits?"
                player.c "Sit down."
                wt_image exhi_whore_3_3
                player.c "You got wet coming over here."
                "It's a statement, not a question, and she doesn't bother to deny it."
                player.c "Were you expecting a new john to service?"
                jasmine.c "I didn't know what to expect."
                player.c "But you knew I was going to show you what a whore you really are."
                jasmine.c "Yeah, but ..."
                player.c "No buts.  You're here because your pussy's been throbbing every time you've thought about me showing you what a whore you really are."
                "You take out the nipple clips and approach her."
                player.c "Pull down your top."
                wt_image exhi_whore_3_4
                "As she does so, you clip the nipple rings in place."
                jasmine.c "What the fuck?!"
                player.c "What do you think all the strangers you've been flashing have thought about your tits?  What type of tits do they look like to them?"
                jasmine.c "I dunno.  Normal tits."
                player.c "But that's not true.  They're not normal tits.  They're the tits of a whore.  Spread your legs, whore."
                wt_image exhi_whore_3_5
                player.c "See how eager you are to show your body off? I could bring 20 men through here right now to get a look at you, and you'd stay just like that, getting wetter and wetter for each man who stared at you and your whore tits."
                wt_image exhi_whore_3_6
                player.c "Take a good look at your whore tits, now.  Would anybody think those were the tits of a respectable housewife?"
                jasmine.c "I guess not."
                player.c "Can you picture yourself flashing those out in public, now?"
                jasmine.c "Yeah"
                player.c "Makes you hot, doesn't it? Knowing that anyone who saw your tits in this shape would think what a dirty tramp you must be, to let a guy do that to you. Spread your legs wider, tramp."
                wt_image exhi_whore_3_5
                player.c "Should I march you downtown to a piercing shop, and we'll get those rings put in permanently?"
                wt_image exhi_whore_3_7
                jasmine.c "No!  My husband ..."
                "You laugh."
                player.c "Listen to you. All you're worried about is what your husband would think. You're perfectly happy to have me do whatever I want with you, as long as I treat you like the whore you are."
                jasmine.c "That's not true."
                player.c "Yes, it is. Do you think being a whore is all fun and games and getting to cum on the end of a john's tongue? We're not role playing any more, Jiggles. Get over here. I'm going to show you what being a whore is really like."
                wt_image exhi_whore_3_8
                player.c "Lick my balls, whore."
                "She kneels in front of you and starts licking you gently."
                wt_image exhi_whore_3_9
                player.c "Take them right inside.  Get me rock hard before I fuck your whore face."
                "She takes your balls into her mouth, one at a time, suckling them as she strokes your cock with her hand."
                wt_image exhi_whore_3_10
                "When you're fully erect and your balls are slathered in her saliva, you push her head away from your testicles."
                player.c "Open up."
                wt_image exhi_whore_3_11
                player.c "This is how you're going to get fucked on the street, Jiggles ..."
                wt_image exhi_whore_3_12
                player.c "... as rough and as hard as the john wants to fuck you."
                "You embed your cock fully in her throat, holding her head in place so she can't pull back as she starts to gag."
                wt_image exhi_whore_3_13
                "Eventually you let her take a breath ..."
                wt_image exhi_whore_3_14
                "... before plunging your cock back into her throat as she starts to cry."
                player.c "This is what you are, Jiggles. A dirty whore whose only purpose is to show off her whore body to any man who wants to take a look at it ..."
                wt_image exhi_whore_3_15
                player.c "... and take a fucking from any man who pays to put his dick inside you, wherever and however he wants to fuck you.  Because that's what dirty whores are for. You know I'm right, don't you Jiggles?"
                "Almost imperceptibly, she nods."
                wt_image exhi_whore_3_16
                "You pull your cock out of her mouth and spit on her face  ...  *pptew*"
                player.c "Do dirty whores complain when a john spits on them, Jiggles?"
                "She shakes her head no."
                wt_image exhi_whore_3_17
                player.c "Are you going to complain when a john spits on your face, Jiggles?"
                "She shakes her head again, as your spittle runs down her face."
                player.c "Why not?"
                jasmine.c "{size=-5} Because I'm a dirty whore.{/size}"
                player.c "Bend over the chair, dirty whore."
                wt_image exhi_whore_3_18
                "She's undisguisedly wet, and you slip into her easily."
                player.c "Does a john have to ask you twice to spank your ass, Jiggles.?"
                "She shakes her head 'no'."
                player.c "Spank your ass, whore."
                "She brings her hand down on her butt cheek, as hard as she can ... *smackkk*"
                wt_image exhi_whore_3_19
                "It's not easy to make a fucking rough when the woman's as wet as Jiggles is, but you do your best ..."
                player.c "Do johns care about whether you like the way they fuck you, whore?"
                "Again she shakes her head 'no'."
                wt_image exhi_whore_3_20
                player.c "But you're such a fucking whore, you get off just knowing they're enjoying your body."
                jasmine.c "ooooo"
                wt_image exhi_whore_3_21
                "You pull her back and flick your fingers across her nipple rings."
                player.c "I bet you'll cum every time a john pays attention to your whore tits."
                jasmine.c "oooo  ...  oooohh!!"
                wt_image exhi_whore_3_22
                "As a shaken Jiggles recovers from her orgasm, you rummage through her purse, returning with her makeup kit and a mirror."
                jasmine.c "What are you doing?"
                player.c "Showing you what you are."
                wt_image exhi_whore_3_23
                "It's a rough makeup job, as you have no real idea what you're doing, but a rough, unfinished job is kind of the point. You hold up the mirror for her to look."
                player.c "What do you see?"
                jasmine.c "A whore."
                wt_image exhi_whore_3_24
                "You apply the lipstick to her forehead, then hold the mirror up close."
                player.c "Now what to do you see?"
                "She starts to tremble, and it takes her a moment to squeak out an answer."
                jasmine.c "{size=-5}A whore.{/size}"
                player.c "That's right. Not a housewife pretending to be a whore because it gets her off. Not a respectable office worker who turns tricks for fun on the side."
                player.c "A real whore who's finally starting to accept what she is.  Shall I take you outside for a walk like this?"
                "She trembles again."
                player.c "You'd let me do that, and you'd flash your whore tits with their shiny nipple rings at every john I told you to suck off, wouldn't you?"
                jasmine.c "{size=-5}Yes{/size}"
                player.c "I think we'll start with your office."
                jasmine.c "No!  Please!!"
                player.c "Don't you want your coworkers to know what you are?"
                jasmine.c "No"
                player.c "What about your husband, then?  Shall we go see him now?"
                "She's trembling like a leaf, but her voice is strong as she replies."
                jasmine.c "Please don't do that."
                player.c "Why not?  You want to try and maintain the illusion that you're a respectable woman? You want to hide who you are? Present a facade to those closest to you?"
                jasmine.c "Yes.  Please.  Please, they'd shun me, even hate me."
                "That fear may be too strong to overcome.  You'll need to work around it, or maybe even use it to control her."
                player.c "Okay, whore.  Since that's so important to you, I'll let you keep your old life, but you'll walk the streets and bring me 50 a week."
                player.c "The first week you let the rest of your life get in the way of my earnings, I'll march you over to your husband and have you show him what you really are."
                jasmine.c "Yes!  Yes, I'll do it!!  Thank you!"
                wt_image exhi_whore_3_25
                "You conclude your agreement by emptying your load on her face."
                player.c "[player.orgasm_text]"
                wt_image exhi_whore_3_26
                jasmine.c "May I clean up now?"
                player.c "Not until you've found a john or two to fuck you like this. Leave my cum on your face, too. Come back when you've earned 25. And that doesn't count against this week's take."
                "She returns a couple of hours later with your money, 'whore' still written across her forehead."
                give 1 nipple_rings_jasmine from player to jasmine
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                $ jasmine.facial_count += 1
                change player money by 25
                call jasmine_convert_whore from _call_jasmine_convert_whore
                call character_location_return(jasmine) from _call_character_location_return_328
                change player energy by -energy_short
                orgasm notify
    elif jasmine.whore_play_status == 7:
        "Jasmine needs to be shown in unmistakable terms what she really is, if you want her to whore for you.  Pick up nipple rings before proceeding with her training."
        add tags "discussed_streetwalking_today" to jasmine
        jump jasmine_contact_visit_menu
    elif jasmine.whore_play_status == 3 or jasmine.whore_play_status == 6:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "I'm in the mood to pick up a street walker, [jasmine.name]"
        jasmine.c "Same corner as last time?"
        player.c "I'll see you there in a few minutes."
        call jasmine_contact_visit_streetwalking_roleplay from _call_jasmine_contact_visit_streetwalking_roleplay_1
    elif jasmine.whore_play_status == 5:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "Ready to get back to work, Jiggles?"
        wt_image exhi_weekend_hypno_2
        "She grimaces."
        jasmine.c "No, I can't do that."
        jasmine.c "I admit, you pimping me out ... it was edgy, scary, dirty."
        jasmine.c "And yeah, I got off on it. I can even picture me playing around, pretending to be a whore from time to time, walking the streets, looking for a john, maybe even picking one up if I find someone nice."
        jasmine.c "But I'm not going to be a real whore, on call to fuck other guys anytime you tell me to. The role play is  ... kinky, and more enjoyable than I expected. But let's just leave it as role play."
        $ title = "What do you tell her?"
        menu:
            "Agree to keep this as role play":
                player.c "I knew you'd get off on that fantasy."
                jasmine.c "I did  It's scary.  It's like you know me better than I know myself.  Definitely better than my husband knows or understands me."
                jasmine.c "Sometimes I wonder if what we're doing is even fair to him?  He deserves a wife who doesn't get off on fucking strangers for money."
                jasmine.c "Can we skip getting together today?  I need time to clear my head and think through some things."
                player.c "Sure"
                call jasmine_contact_visit_whore_training_convert_to_roleplay from _call_jasmine_contact_visit_whore_training_convert_to_roleplay
            "Tell her she is your whore":
                player.c "You don't get it yet, do you? You're still trying to hold on to the fantasy that you're a respectable woman with a respectable job and a respectable husband, living a normal middle class life."
                player.c "That's not you. That's not who you are. If it were, you wouldn't be running around with me, fucking men for money behind your husband's back."
                player.c "I'm going to give you some time to think about things. About what you've done. About what your husband and friends and coworkers would think if they knew what you'd done. About going back to that old life you've been trying to escape from."
                player.c "I know what you are and what you need.  You're my whore."
                "[jasmine.name] doesn't reply.  She wants to argue, but she can't find the words."
                player.c "Until next time, whore."
                "You're going to need to give [jasmine.name] a push to get her to accept a new life as a street walker. That means preparing for a pretty intensive session to break down her resistance."
                "[jasmine.name]'s always been proud to show off her tits.  Some new jewelry to convert her tits to whore tits should be part of the process."
                $ jasmine.whore_play_status = 7
    elif jasmine.whore_play_status == 4:
        player.c "Ready to whore yourself out to a stranger, Jasmine?"
        wt_image exhi_weekend_hypno_2
        jasmine.c "I can't do this."
        player.c "Yes you can. It's just like fucking me for money. Except instead of it being someone you know, it'll be a complete stranger you expose your body to. And he'll show his appreciation by giving you money to put his dick inside you."
        jasmine.c "It's too dangerous."
        player.c "Tell you what. Just this once, while you're getting started, instead of exposing yourself on the street for whoever comes along, I'll find a guy for you, and I'll take you to him. Then I'll stay, and I'll watch you while he fucks you."
        wt_image exhi_weekend_hypno_13
        player.c "You like the idea of that, don't you? Getting watched while a stranger fucks you for money. I'll pick you up after I've set up your date."
        # proceed if she's had public sex at the Club or given multiple BJs in the park
        if jasmine.club_sex_status > 1 or jasmine.downtown_sex > 1:
            $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            jasmine.c "I ... I guess."
            call forced_movement(outdoors) from _call_forced_movement_582
            summon jasmine
            wt_image exhi_whore_2_1
            "When everything's arranged, you drive [jasmine.name] to a nice hotel. The john who contacted you online is just getting out of the shower when you arrive."
            john_1_jasmine "Hey there.  You must be Jiggles.  Come on in."
            jasmine.c "Jiggles?"
            player.c "Would you prefer I used your real name?"
            john_1_jasmine "I'll call you whatever you want, sweetheart.  Come in so I can see you better."
            wt_image exhi_whore_2_2
            john_1_jasmine "I can see why he called you Jiggles.  You've got some big bouncy ones."
            jasmine.c "Uh, thanks?"
            wt_image exhi_whore_2_25
            "He's a little grabby, but 'Jiggles' will need to get used to that when she's plying her wares on the street."
            wt_image exhi_whore_2_3
            "She can't disguise her disgust, though, when he tries to kiss her."
            john_1_jasmine "Ahh, don't you like me?"
            jasmine.c "No, it's just ... no kissing."
            player.c "Why don't you show him your tits, Jiggles?"
            wt_image exhi_whore_2_4
            jasmine.c "Okay"
            john_1_jasmine "Here, I'll do it."
            wt_image exhi_whore_2_5
            john_1_jasmine "Nice!"
            jasmine.c "Thanks"
            "Exposing herself always helps get 'Jiggles' in the mood ..."
            wt_image exhi_whore_2_26
            "... and his rough hands massaging her soft mounds doesn't hurt either, as her stiffening nipples attest."
            jasmine.c "mmmm"
            wt_image exhi_whore_2_27
            john_1_jasmine "As nice as your titties feel and look, I want to see your ass."
            player.c "Go ahead and look.  Jiggles won't mind.  She likes exposing herself.  Don't you?"
            wt_image exhi_whore_2_7
            jasmine.c "Yes"
            wt_image exhi_whore_2_8
            john_1_jasmine "Fuck!  That's an awesome ass!!"
            jasmine.c "Thanks"
            wt_image exhi_whore_2_9
            john_1_jasmine "Can I spank it?"
            "'Jiggles' jumps in with a reply before you can."
            jasmine.c "No!  No spanking!!"
            john_1_jasmine "Well, can I taste you then?"
            jasmine.c "Taste me?"
            wt_image exhi_whore_2_28
            john_1_jasmine "Yeah, you know."
            wt_image exhi_whore_2_10
            "He spreads her legs and shows her what he means."
            jasmine.c "Oh!"
            wt_image exhi_whore_2_11
            "His unexpected attention soon has her clit throbbing and standing at attention."
            jasmine.c "ooooo  ...  oooooo"
            wt_image exhi_whore_2_12
            "It's pretty much the perfect situation for her first real 'date', as 'Jiggles' discovers she's able to cum with a john."
            jasmine.c "ooooo ...  oooohh!!"
            wt_image exhi_whore_2_13
            john_1_jasmine "My turn now, sweetheart."
            wt_image exhi_whore_2_29
            "'Jiggles' looks genuinely curious as he removes his towel.  You realize you have no idea how many cocks she's seen in real life besides her husband's and yours.  Maybe not many?  If so, that's going to change."
            wt_image exhi_whore_2_14
            "She doesn't get much of a chance to examine his member before he shoves it in her mouth."
            wt_image exhi_whore_2_30
            "She'll need to learn to take a good skull fucking, but her john wants to go rougher and faster than she may be ready for.  You try to distract both of them."
            player.c "Show the man your tits while you're sucking him, Jiggles."
            wt_image exhi_whore_2_31
            "She does so, and the potential crisis is avoided. She enjoys putting herself on display, and he slows down to watch her show."
            wt_image exhi_whore_2_15
            john_1_jasmine "Lie back, sweetheart."
            "This is the last hurdle.  She looks at you uncertainly.  Sucking his dick was one thing.  Fucking a man for money is another."
            player.c "Show him your tits and spread your legs, Jiggles.  He's paying good money for you."
            wt_image exhi_whore_2_32
            "It's a special moment when a woman takes a cock inside her for money for the first time.  One she won't ever forget.  She holds up her tits for her john, but it's you she's looking at.  You're the reason she's doing this."
            wt_image exhi_whore_2_33
            player.c "You're a real whore now, Jiggles.  That dick inside you isn't your husband's or a lover's, it's a stranger's.  A man who was turned on by the sight of your body and paid you to spread your legs for him.  How does it feel, getting fucked by a stranger for money?"
            "She's unable to form a response.  She just stares at you, as you watch her get fucked by a john."
            wt_image exhi_whore_2_18
            "The silence is broken by the john, guiding her up on top."
            john_1_jasmine "I want to watch your ass while we fuck."
            player.c "Don't just let him look at it, Jiggles.  Let him spank it."
            wt_image exhi_whore_2_19
            player.c "Don't give me that look, whore.  The customer is always right."
            wt_image exhi_whore_2_20
            "She turns around to give him easier access."
            john_1_jasmine "Are you sure?"
            jasmine.c "Yes"
            wt_image exhi_whore_2_34
            "*smack*  ...  *smack*  ...  *smack*"
            jasmine.c "Ow!!"
            john_1_jasmine "Fuck, that feels good!"
            wt_image exhi_whore_2_35
            "As if to highlight the point, he pushes her off him and empties his load over her upturned ass."
            wt_image exhi_whore_2_21
            john_1_jasmine "Yeaaahhhh"
            wt_image exhi_whore_2_23
            john_1_jasmine "That was great, sweetheart.  He said you were new at this.  Was this really your first time?"
            jasmine.c "Yes"
            john_1_jasmine "Well, fuck!  I'd say you're a natural, Jiggles. Does your ass hurt?  I hope I didn't spank you too hard."
            wt_image exhi_whore_2_22
            jasmine.c "It's fine, thanks.  Can I go now?"
            john_1_jasmine "Sure, sure.  I'll get your money."
            player.c "I'll take it."
            wt_image exhi_whore_2_24
            "On the car ride hom, you give her her share."
            jasmine.c "You're keeping some of it?"
            player.c "Half, for the effort I went through to set this up for you.  When you're walking the street and finding johns on your own, I'll cut my take to a quarter."
            jasmine.c "I'm not going to do this on a regular basis."
            player.c "We'll talk about that later."
            change player money by 50
            $ jasmine.whore_play_status = 5
            change player energy by -energy_long notify
            call forced_movement(living_room) from _call_forced_movement_583
            call character_location_return(jasmine) from _call_character_location_return_329
        else:
            "You know the idea does excite her, but she's not ready to say yes."
            wt_image exhi_weekend_hypno_2
            jasmine.c "No.  I can't."
            "If you get her used to being watched while she fucks, you may get a different answer from her, but not today."
            add tags "discussed_streetwalking_today" to jasmine
            jump jasmine_contact_visit_menu
    elif jasmine.whore_play_status == 2:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "I'm in the mood to pick up a street walker, [jasmine.name].  Do you think you can help me?"
        wt_image exhi_gf_conversation_3
        jasmine.c "Well, I don't know.  I got stiffed the last time I was a street walker.  Think I'll have better luck this time?"
        player.c "If you're a dirty little whore for me, you're going to get something stiff."
        wt_image exhi_weekend_hypno_13
        jasmine.c "Same corner as last time?"
        player.c "I'll see you there in a few minutes."
        call forced_movement(outdoors) from _call_forced_movement_584
        summon jasmine
        wt_image exhi_whore_1_1
        "Jasmine is waiting on the corner when you arrive.  She gives you a little smile when she sees you ..."
        wt_image exhi_whore_1_3
        "... then shifts into 'professional' mode, showing off her wares."
        wt_image exhi_whore_1_4
        "You pull your car over beside her and she approaches."
        jasmine.c "Hey, there ..."
        wt_image exhi_whore_1_5
        jasmine.c "You wanna take me on a date?"
        player.c "Hop in."
        call forced_movement(living_room) from _call_forced_movement_585
        summon jasmine
        wt_image exhi_whore_1_8
        "You bring her home.  As soon as she's inside, she strips."
        jasmine.c "So whadda you want?  My mouth, my tits ..."
        wt_image exhi_whore_1_9
        jasmine.c "... my pussy?"
        player.c "All three, whore. I'm paying for that sexy body. Show me what it can do."
        wt_image exhi_whore_1_25
        "She smiles as she presses your cock between her tits ..."
        wt_image exhi_whore_1_26
        "... and then starts sucking on you."
        wt_image exhi_whore_1_27
        "When you're fully hard, she gets on all fours and turns around to look at you."
        jasmine.c "How do you want to fuck me?  Like this?"
        player.c "To start with. Shake that phat ass, whore. Let me see that booty jiggle."
        "You push inside her wet snatch with ease and she starts shaking and bouncing her hips, giving you a nice show as she rocks back and forth on your cock."
        wt_image exhi_whore_1_28
        player.c "Turn around, whore.  I want to see those whore tits of yours jiggle."
        "You lets out a small moan as you cup her breast while she rides you."
        jasmine.c "oooo"
        player.c "You like that, whore?  You like having your whore tits played with?"
        jasmine.c "Uh huh"
        wt_image exhi_whore_1_29
        player.c "Answer me properly, whore."
        "You pinch her nipple, eliciting another moan."
        jasmine.c "oooo  ... yes, I like having my whore tits played with!"
        wt_image exhi_whore_1_30
        player.c "No cumming on the job, whore. I'm the paying customer. That's my privilege. Lean back. I'm going to cum on that whore face of yours."
        wt_image exhi_whore_1_19
        "She lies back and pumps your seed over her waiting face."
        player.c "[player.orgasm_text]"
        $ title = "What do you do?"
        menu:
            "Thank her for the role play":
                player.c "Thanks for the role play, [jasmine.name]."
                wt_image exhi_whore_1_21
                jasmine.c "You're welcome! It was kinda fun. I like how you worked my kink about exposing myself in public into your own fantasy."
                jasmine.c "I wish my husband would do that sometimes. If he indulges my kink, it's always like some big favor he's doing me. He never turns it into something we can both enjoy, the way you did."
                call jasmine_contact_visit_whore_training_convert_to_roleplay from _call_jasmine_contact_visit_whore_training_convert_to_roleplay_1
            "Tell her you're stiffing her again":
                player.c "I was going to pay you, whore, but it seems I don't have enough money on me."
                wt_image exhi_whore_1_21
                "She laughs."
                jasmine.c "Again?  I might have to stop going on dates with you."
                "You get off her and she cleans herself up and leaves."
            "Pay her (costs 100)" if player.money - player.min_money >= 100:
                change player money by -100
                player.c "There you go, whore.  That should cover your services."
                "You throw 100 down on the bed beside her."
                wt_image exhi_whore_1_22
                jasmine.c "What? Are you serious?? Is that really how you see me? As a whore? I'm not a whore. We were just role-playing. You don't have to pay me."
                $ title = "What do you tell her?"
                menu:
                    "I know you're not":
                        player.c "I know you're not. I was just finishing up the role play. Thanks for playing along with me, [jasmine.name]."
                        wt_image exhi_whore_1_24
                        jasmine.c "You're welcome! It was kinda fun. I like how you worked my kink about exposing myself in public into your own fantasy. I wish my husband would do that sometimes."
                        jasmine.c "If he indulges my kink, it's always like some big favor he's doing me. He never turns it into something we can both enjoy, the way you did."
                        jasmine.c "And thanks for the 100!  Maybe I'll buy some barely there underwear with it that we can both enjoy."
                        add tags 'bonus_lingerie' to jasmine
                        call jasmine_contact_visit_whore_training_convert_to_roleplay from _call_jasmine_contact_visit_whore_training_convert_to_roleplay_2
                    "Sure you are":
                        call jasmine_contact_visit_whore_training_convert_to_whore from _call_jasmine_contact_visit_whore_training_convert_to_whore
        $ jasmine.sex_count += 1
        $ jasmine.facial_count += 1
        orgasm notify
        call character_location_return(jasmine) from _call_character_location_return_330
    elif jasmine.whore_play_status == 1:
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "Did you pick out an outfit?"
        jasmine.c "What outfit?"
        player.c "A street walker outfit.  I bet you'll be the sexiest whore on the strip."
        jasmine.c "I ... found a couple of things that might work."
        player.c "Great!  I can't wait to see you in them."
        jasmine.c "You're not going to leave me out on the street for long are you?"
        player.c "Just long enough for some potential johns to get a good look at you."
        wt_image exhi_weekend_hypno_2
        jasmine.c "But that could be anybody!  Friends, my husband's co-workers.  Cops!"
        player.c "The same people who could catch you whenever you're out flashing in public. Only now instead of thinking you're a slut, they'll think you're a whore. The sort of woman who'd take a guy into the park and blow him while other people are walking by."
        wt_image exhi_weekend_hypno_13
        jasmine.c "That's ... a bit exciting, I guess."
        player.c "I'll send you the address of the street corner I want you to work. Make sure you show me enough to want to pick you up. You wouldn't want me to drive on and give my business to someone else."
        call forced_movement(outdoors) from _call_forced_movement_586
        summon jasmine
        wt_image exhi_whore_1_1
        "Jasmine is standing on the street corner when you get there. You watch from a discrete distance as a few cars slow down to get a closer look at her. She beats a hasty retreat when she sees they aren't you, then returns after they're gone."
        "When you pull your car around, she walks over."
        jasmine.c "Finally!  Let's go."
        player.c "I'm still shopping, sweetheart.  I just wanted a closer look before I decide who I want to take on a date."
        "You pull away before she can reply."
        wt_image exhi_whore_1_2
        "You drive a couple of blocks, then circle back. This time when you pass, she smiles and gives you a little show. You slow down a bit, then keep going."
        wt_image exhi_whore_1_3
        "When you circle back again, she's much bolder, opening her top and spreading her legs. You pull the car over beside her."
        wt_image exhi_whore_1_4
        "This time when she approaches the car, she's into the roleplay."
        jasmine.c "You want a date?"
        player.c "Maybe.  Why should I pick you?"
        wt_image exhi_whore_1_5
        "She says nothing, just pulls open her top."
        player.c "Good enough.  Get in."
        call forced_movement(living_room) from _call_forced_movement_587
        summon jasmine
        wt_image exhi_whore_1_6
        "You drive her back to your place and bring her in."
        player.c "Get on the sofa, hands and knees, ass towards me."
        jasmine.c "I wasn't sure if you were taking me here, or to the park."
        player.c "I thought about the park, then decided I might want to be a little rougher with you, so thought it was better to be somewhere private."
        wt_image exhi_whore_1_7
        jasmine.c "Rougher?"
        player.c "Relax. You show me a good time, and everything will be okay. Why don't you give me a little show, to make sure I don't regret picking you for my date?"
        wt_image exhi_whore_1_8
        jasmine.c "I guess this is the danger of being a street whore, huh?  Having to please my john or he could get rough on me?"
        wt_image exhi_whore_1_9
        player.c "Him or your pimp."
        jasmine.c "I don't think I'd have a pimp.  I'd be an independent girl."
        wt_image exhi_whore_1_10
        player.c "I think you'd have a pimp. A strong man to keep you out on the street, exposing your body to as many prospective johns as possible."
        wt_image exhi_whore_1_11
        jasmine.c "Maybe I wouldn't need a pimp to make me do that? Maybe I'd be so excited seeing how many men were interested in my body that I'd walk the streets on my own, spending the whole day exposing myself."
        player.c "And finding men willing to pay for access to that body?"
        jasmine.c "Uh huh"
        player.c "Then you'd have to follow through for them. Get over here, whore, and suck my cock."
        wt_image exhi_whore_1_12
        "She kneels in front of you and licks your cock."
        player.c "You have nice tits, whore."
        wt_image exhi_whore_1_13
        jasmine.c "You like them?  Do they feel good against your hard dick?"
        player.c "Yeah, but I didn't say to stop sucking my cock."
        wt_image exhi_whore_1_14
        "She resumes licking your cock."
        player.c "I said suck me off, whore, not lick me."
        wt_image exhi_whore_1_15
        "Taking you in her mouth, she starts sucking.  Before long, you're fully hard."
        player.c "Better.  Turn around.  I want to fuck that phat ass of yours, whore."
        wt_image exhi_whore_1_16
        "She's surprisingly wet, letting you slide into her easily as she gets into position. Mentally she's not sure what she thinks about how you're treating her, but her body's responding anyway."
        player.c "Mmmm, you've got some booty on you, don't you whore?"
        wt_image exhi_whore_1_17
        "You bring your hand down hard on her upturned ass  ...  *SMACK*"
        jasmine.c "Ow!"
        player.c "I asked you a question, whore.  You've got some booty on you, don't you?"
        jasmine.c "Yes.  Yes, I have booty."
        player.c "There, that wasn't so hard.  Flip over."
        wt_image exhi_whore_1_18
        player.c "Do you know why I wanted to finish fucking you in this position, whore?"
        jasmine.c "No"
        player.c "So I can see your face ..."
        wt_image exhi_whore_1_19
        player.c "... when I dump my load on it. Pump every last drop out, whore."
        "She milks the sperm out of your cock and onto her upturned face."
        player.c "[player.orgasm_text]"
        wt_image exhi_whore_1_20
        "She lies there, covered in your sperm, uncertain as to what to do next."
        $ title = "What do you do?"
        menu:
            "Thank her for the role play":
                player.c "Thanks for the role play, [jasmine.name]."
                wt_image exhi_whore_1_21
                jasmine.c "You're welcome! It was kinda fun. I like how you worked my kink about exposing myself in public into your own fantasy."
                jasmine.c "I wish my husband would do that sometimes. If he indulges my kink, it's always like some big favor he's doing me. He never turns it into something we can both enjoy, the way you did."
                call jasmine_contact_visit_whore_training_convert_to_roleplay from _call_jasmine_contact_visit_whore_training_convert_to_roleplay_3
            "Stiff her":
                player.c "I was going to pay you, whore, but it seems I don't have enough money on me."
                wt_image exhi_whore_1_21
                "She laughs."
                jasmine.c "What, you're going to stiff me after you stiffed me?  Maybe I do need a pimp."
                "You get off her and she cleans herself up and leaves."
                $ jasmine.whore_play_status = 2
            "Pay her (costs 100)" if player.money - player.min_money >= 100:
                change player money by -100
                player.c "There you go, whore.  That should cover your services."
                "You throw 100 down on the bed beside her."
                wt_image exhi_whore_1_22
                jasmine.c "What? Are you serious?? Is that really how you see me? As a whore? I'm not a whore. We were just role-playing. You don't have to pay me."
                $ title = "What do you tell her?"
                menu:
                    "I know you're not":
                        player.c "I know you're not. I was just finishing up the role play. Thanks for playing along with me, [jasmine.name]."
                        wt_image exhi_whore_1_24
                        jasmine.c "You're welcome! It was kinda fun. I like how you worked my kink about exposing myself in public into your own fantasy. I wish my husband would do that sometimes."
                        jasmine.c "If he indulges my kink, it's always like some big favor he's doing me. He never turns it into something we can both enjoy, the way you did."
                        jasmine.c "And thanks for the 100!  Maybe I'll buy some barely there underwear with it that we can both enjoy."
                        add tags 'bonus_lingerie' to jasmine
                        call jasmine_contact_visit_whore_training_convert_to_roleplay from _call_jasmine_contact_visit_whore_training_convert_to_roleplay_4
                    "Sure you are":
                        call jasmine_contact_visit_whore_training_convert_to_whore from _call_jasmine_contact_visit_whore_training_convert_to_whore_1
        $ jasmine.sex_count += 1
        $ jasmine.facial_count += 1
        orgasm notify
        call character_location_return(jasmine) from _call_character_location_return_331
    elif jasmine.whore_play_status == 0:
        jasmine.c "I'll be right over."
        player.c "Let's do something different today.  How about you dress up and walk the streets, and I'll swing by and pick you up."
        jasmine.c "Dress up and walk the streets?  You mean pretend that I'm a whore?"
        player.c "With all your assets out for potential customers to see.  Yes.  And I'll swing by and pick you up ... after other potential customers get a good look at you, of course."
        # given you a BJ outside yet?
        wt_image exhi_weekend_hypno_2
        if jasmine.downtown_sex > 1:
            jasmine.c "No way. I don't mind dressing up for you and I like showing off in public, but I don't want people thinking I'm a whore."
            player.c "What do you think anybody who saw or heard us in the park would think?"
            jasmine.c "I don't know.  That we were having a little fun?"
            player.c "Come on, who sucks off guys in the park?"
            jasmine.c "Whores, I guess."
            wt_image exhi_weekend_hypno_13
            player.c "Cheap whores. Street walkers. Women who put their bodies out there for every passer by to see."
            player.c "Let's take that game a little further and have some fun with it.  Put on a sexy whore costume and go for a walk.  I'll pick you up and be your john for the day."
            jasmine.c "No. Not today. I don't even have the right outfit to wear."
            player.c "Next time, then."
            jasmine.c "Maybe. I'll think about it."
            player.c "Think about sucking me off in the park and how fun that was. This will be even more fun."
            $ jasmine.whore_play_status = 1
        else:
            jasmine.c "No way. I like showing off in public, but I don't want people thinking I'm a whore."
            "You'll need to get her used to some whore-like behavior in public before she'll consider this request."
        add tags "discussed_streetwalking_today" to jasmine
        jump jasmine_contact_visit_menu
    else:
        sys "Oops. There's been a problem with the jasmine_contact_visit_whore_training label."
    wt_image current_location.image
    call character_location_return(jasmine) from _call_character_location_return_332
    return

# Contact - Visit - Whore Training - End by converting to roleplay
label jasmine_contact_visit_whore_training_convert_to_roleplay:
    add tags 'whore_roleplaying' to jasmine
    $ jasmine.gf_conversion_status += 1
    if jasmine.whore_play_status > 3:
        # on status 6, you can find her walking the streets as a downtown event, as well as role-playing her being your whore
        $ jasmine.whore_play_status = 6
    else:
        # on status 3, she doesn't walk the streets, but you can role-play her being your whore
        $ jasmine.whore_play_status = 3
    return

# Contact - Visit - Whore Training - End by converting to whore
label jasmine_contact_visit_whore_training_convert_to_whore:
    player.c "Sure you are. I know your type. Respectable job, nice husband, nice house. Typical suburban middle class housewife. But you're not happy, because it's a mismatch with who you really are."
    wt_image exhi_whore_1_23
    player.c "You're a dirty girl and you've always known it. It's why you need to take your clothes off, so you can show the world, 'Hey, I'm not really a respectable woman.'"
    player.c "It's a cry for help, your way of saying, 'Please, treat me like the whore I am.'  So consider this the first step in having the world treat you the way you should be treated."
    player.c "There's your money, whore. You earned it. Put it in your purse and go home to your husband and fuck him to sleep. But when you're lying there beside him while he snores, you're not going to be thinking about the next time he makes love to you."
    player.c "You're going to be thinking about the next time I call you. Because it's not going to be me you expose yourself to next time. It's going to be some other guy. Some complete stranger."
    player.c "And if he likes what he sees, he's going to pay you to put his dick inside you, and you're going to take his money and let him do what he wants to you. Because that's the kind of girl you are, and your pussy knows it."
    "She's angry, yet she can't bring herself to respond. She gathers up her clothes and leaves, but not before putting your money in her purse."
    $ jasmine.whore_play_status = 4
    return

# Contact - Visit - Whore Training - Streetwalking Roleplay
label jasmine_contact_visit_streetwalking_roleplay:
    call forced_movement(outdoors) from _call_forced_movement_588
    summon jasmine
    wt_image exhi_whore_1_1
    "'Jiggles' is waiting on the corner when you arrive.  She gives you a little smile when she sees you ..."
    wt_image exhi_whore_1_3
    "... then shifts into 'professional' mode, showing off her wares."
    wt_image exhi_whore_1_4
    "You pull your car over beside her and she approaches."
    jasmine.c "Hey, there ..."
    wt_image exhi_whore_1_5
    jasmine.c "You wanna take me on a date?"
    player.c "Hop in."
    call forced_movement(living_room) from _call_forced_movement_589
    summon jasmine
    wt_image exhi_whore_1_8
    "You bring her home.  As soon as she's inside, she strips."
    jasmine.c "So whadda you want?  My mouth, my tits ..."
    wt_image exhi_whore_1_9
    jasmine.c "... my pussy?"
    $ title = "What do you want?"
    menu:
        "Blow job":
            player.c "Your mouth sounds good, whore."
            wt_image exhi_whore_1_14
            "She kneels down in front of you and licks your cock."
            jasmine.c "My mouth is good."
            wt_image exhi_whore_1_26
            player.c "Is that how you got into this business, whore?  Because you have a good cock sucking mouth?"
            jasmine.c "She shakes her head 'no'."
            wt_image exhi_whore_1_12
            jasmine.c "Nope.  It's because I can't keep my clothes on."
            player.c "So now you spend your days naked, sucking cock for money?"
            jasmine.c "Uh huh.  I'll show you."
            wt_image exhi_whore_1_15
            "She proceeds to put her mouth to good use ..."
            wt_image exhi_whore_1_31
            "... and soon has you ready to cum."
            $ title = "Where do you want to cum?"
            menu:
                "On her face":
                    wt_image exhi_facial_1
                    "She closes her eyes and tilts her head back as you adorn her face with your load."
                    wt_image exhi_facial_2
                    $ jasmine.facial_count += 1
                "In her mouth":
                    wt_image exhi_whore_1_26
                    "She wraps her lips tightly around your cock and swallows as you fill her mouth with your load."
                    $ jasmine.swallow_count += 1
            player.c "[player.orgasm_text]"
            $ jasmine.blowjob_count += 1
        "Tit job":
            player.c "Your tits sound good, whore."
            wt_image exhi_whore_1_13
            "She kneels down in front of you and rubs your cock against her soft breasts."
            jasmine.c "My tits are good."
            player.c "Is that how you got into this business, whore?  Because you couldn't keep your tits to yourself?"
            jasmine.c "Pretty much.  I just have to take them out and show them off."
            wt_image exhi_whore_1_25
            player.c "Well, now that they're out, put 'em to good use."
            "She nestles your cock in her ample bosom and starts tittie-fucking you ..."
            wt_image exhi_tits_1
            "... with predictable results."
            player.c "[player.orgasm_text]"
            $ jasmine.titfuck_count += 1
        "Missionary":
            player.c "Your pussy sounds good, whore.  Lie back and spread your legs."
            wt_image exhi_whore_1_32
            jasmine.c "My pussy is good."
            "She lies back and you slide easily into her already wet cunt."
            wt_image exhi_whore_1_18
            player.c "Is that how you got into this business, whore?  Your pussy likes cocks so much you needed to become a whore to get it filled?"
            jasmine.c "Nope.  I just can't keep my clothes on."
            player.c "I bet that gets you fucked on a regular basis."
            jasmine.c "Lately, yeah."
            "She doesn't sound unhappy about it ..."
            wt_image exhi_whore_1_33
            jasmine.c "ooooo"
            "... in fact, she soon sounds decidedly happy about it.  You're pretty happy about it, too."
            $ title = "Where do you want to cum?"
            menu:
                "On her face":
                    wt_image exhi_whore_1_19
                    "Pulling out of her, you move up and straddle her chest as she pumps the semen out of your balls and onto her waiting face."
                    player.c "[player.orgasm_text]"
                    $ jasmine.facial_count += 1
                "Inside her":
                    wt_image exhi_whore_1_18
                    "With a few, final hard thrusts ... once, twice, three times ... you cum, your cock buried deep inside her."
                    player.c "[player.orgasm_text]"
                    wt_image exhi_creampie_1
                    "As you pull out, the two of you watch your cum dribble out of her."
                    jasmine.c "That was a big load."
                    player.c "You were a good whore."
            $ jasmine.sex_count += 1
        "Doggy style":
            player.c "Your pussy sounds good, whore.  Turn around and get on your hands and knees."
            wt_image exhi_whore_1_10
            "She does so, exposing an already glistening cunt."
            player.c "Get your clothes all the way off, whore.  I don't want your panties getting in the way of seeing your phat booty jiggling."
            wt_image exhi_whore_1_17
            "Once she's naked, you push yourself inside her."
            player.c "Start shaking your booty, whore.  I want to watch you get me off."
            wt_image exhi_whore_1_27
            "That takes less time than you expect, as the view and feel of her wiggling, rocking, shaking, and sliding her hips up, down, along and around your hard shaft ..."
            wt_image exhi_whore_1_34
            "... has you exploding over her ass and back in no time."
            player.c "[player.orgasm_text]"
            $ jasmine.sex_count += 1
        "Cowgirl":
            player.c "Your pussy sounds good.  Climb up here and show me how well you can use that whore cunt of yours to get me off."
            wt_image exhi_whore_1_35
            "She lowers herself onto you, her cunt wet enough to impale herself easily on your hard shaft."
            wt_image exhi_whore_1_36
            "Then she starts riding you, up and down, back and forth, fucking your cock as she looks back at you. It's fun, but after a few minutes, you want more."
            player.c "Turn around, whore.  I want to watch those whore tits of yours bouncing up and down as you fuck me."
            wt_image exhi_whore_1_28
            "She does so, and her big boobs are soon bouncing up and down in front of you as she rides you.  You reach up and cup one of her tits as she moans."
            jasmine.c "ooooo"
            player.c "You like that, whore?  You like having your whore tits played with while you're fucking cock?"
            jasmine.c "ooooo ... yes!"
            wt_image exhi_whore_1_29
            player.c "I bet you like it even more when they're squeezed and slapped and pinched, don't you whore?"
            jasmine.c "oooooo  ....  oooooo"
            player.c "Answer me, whore."
            wt_image exhi_whore_1_30
            "She gives you her answer in the form of an orgasm."
            jasmine.c "ooooo ... yes!  oooohh!!"
            "Yours follows shortly after hers."
            player.c "[player.orgasm_text]"
            $ jasmine.sex_count += 1
            $ jasmine.orgasm_count += 1
    wt_image exhi_whore_1_2
    "She cleans herself up and dresses."
    jasmine.c "Guess I better get back to my street corner.  I can't spend all my time with one date, even if if he is my favorite regular."
    call character_location_return(jasmine) from _call_character_location_return_333
    orgasm notify
    return

# Check On Whore
label jasmine_check_whore:
  wt_image exhi_whore_4_1
  if not jasmine.has_tag('showgirl') and jasmine.stripper_discussion > 2 and not jasmine.has_tag('transformed'):
    player.c "How's life on the streets, Jiggles?"
    jasmine.c "Okay"
    player.c "Just as much fun as dancing on a stage?"
    jasmine.c "Some days, I guess."
    player.c "Getting to show off your whore tits to lots of men?"
    "She blushes."
    jasmine.c "Yes"
    player.c "Not holding out on my payments, are you?"
    jasmine.c "Of course not!"
    player.c "Good.  If you get into trouble, you let me know. I'll look out for you."
    jasmine.c "I know.  Thanks."
    player.c "That doesn't mean you get to say 'no' to the johns after they pay you, though."
    jasmine.c "I know."
  else:
    player.c "How's life on the streets, Jiggles?"
    jasmine.c "Okay"
    player.c "Getting to show off your whore tits to lots of men?"
    "She blushes."
    jasmine.c "Yes"
    player.c "Not holding out on my payments, are you?"
    jasmine.c "Of course not!"
    player.c "Good.  If you get into trouble, you let me know. I'll look out for you."
    jasmine.c "I know.  Thanks."
    player.c "That doesn't mean you get to say no to the johns after they pay you, though."
    jasmine.c "I know."
  $ jasmine.whore_lost_countdown = 5
  return

# View Relationship Status
label jasmine_relationship_status:
    call jasmine_description_display from _call_jasmine_description_display_1
    wt_image current_location.image
    return

# Review Files
label jasmine_review_files:
    call jasmine_description_display from _call_jasmine_description_display_2
    wt_image current_location.image
    return

## Character Specific Objects
# Watch Jasmine Fuck In Club
# OBJECT: Watch Your Girlfriend
label jasmine_watch:
    if not jasmine.can_be_interacted or jasmine.downtown_event_checked_today >= 2:
        "Jasmine is not available today."
    else:
        summon jasmine
        $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        # this command disables running into her downtown later today
        $ jasmine.downtown_event_checked_today = 2
        wt_image exhi_sr_1_1
        "For an exhibitionist, Jasmine seems oddly out of sorts amongst the debauchery of the swingers room."
        wt_image exhi_sr_1_2
        "She's used to taking off her clothes in front of a fully dressed audience.  She seems less comfortable walking fully clothed through a crowd of progressively more naked people ..."
        wt_image exhi_sr_1_3
        "... some of whom are up to some rather shocking things."
        wt_image exhi_sr_1_4
        "When she realizes you've been following her and watching her, however, her whole attitude changes. She grabs hold of the nearest available cock ..."
        wt_image exhi_sr_1_5
        "... and starts sucking and pleasuring it as if you weren't there to observe her."
        wt_image exhi_sr_1_7
        "Her clothes soon come off ..."
        wt_image exhi_sr_1_6
        "... and she mingles with the crowd ..."
        wt_image exhi_sr_1_10
        "... watching them as you watch her ..."
        wt_image exhi_sr_1_8
        "... observing the activities ..."
        wt_image exhi_sr_1_9
        "... seemingly enjoying herself ..."
        wt_image exhi_sr_1_11
        "... until unexpected attention gives her pause."
        wt_image exhi_sr_1_12
        "Her eyes meet yours across the room, and you can read the conflict on her face."
        wt_image exhi_sr_1_13
        "You stay exactly where you are, neither coming to her rescue, nor looking away."
        "She seems paralyzed, her eyes locked on yours, unable to move under the intensity of your gaze and her own awareness that 'he's watching this ... he's watching a ... a woman ... using her tongue on me'."
        wt_image exhi_sr_1_14
        "It lasts only a moment, but it seems longer, before Jasmine pushes away the unwanted attention of the women behind her ..."
        wt_image exhi_sr_1_15
        "... to have it replaced by attention more in keeping with her sexual orientation."
        wt_image exhi_sr_1_16
        "Once again you make eye contact with her, letting her know 'yes, I see you ...  I see you getting fucked by a stranger's cock' ..."
        wt_image exhi_sr_1_17
        "... then you wander away, content in the knowledge that Jasmine's exhibitionist kink has been sufficiently stimulated that she's now ready to let herself be fucked silly."
        if jasmine.maintain_week_gf < week + 2:
            $ jasmine.maintain_week_gf = week + 2
        change player energy by -energy_short notify
        call character_location_return(jasmine) from _call_character_location_return_334
    return

## Items
# Give Butt Plug
label give_bp_jasmine:
  "Jasmine isn't in to D/s or any of that kinky stuff. As fun as it would be to have her flash her ass with a butt plug in it, she's not going to go for that."
  return

# Give Chastity Belt
label give_cb_jasmine:
  "How is Jasmine supposed to flash her pussy at anyone wearing this?"
  return

# Give Dildo
label give_di_jasmine:
  if jasmine.has_item(dildo):
    "You've already gifted [jasmine.name] a dildo.  One is enough."
  else:
    wt_image jasmine.image
    if jasmine.status == "on_training":
      "You expect [jasmine.name] already has one.  Or several.  She's not about to fess up to that, though.  And she does like getting gifts."
      "For a moment it looks like she is going to ask you what she's supposed to do with this, then she thinks better of it, and accepts the gift in silence."
    else:
      if jasmine.has_tag('bimbo'):
        jasmine.c "For me?  You're so great!!  It's just like having my own cock!"
      else:
        jasmine.c "What do you expect me to do with that?"
        player.c "Can't you guess?"
        "She blushes."
    change jasmine resistance by -5
    give 1 dildo from player to jasmine notify
  return

# Use Fetch Toy
label use_ft_jasmine:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_jasmine:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_jasmine:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_jasmine:
  if jasmine.has_item(lingerie) and jasmine.status == "on_training":
    "You've already gifted lingerie to [jasmine.name].  She has enough for now."
  else:
    if jasmine.status == "on_training" or jasmine.has_tag('girlfriend') or jasmine.has_tag('continuing_actions'):
      call jasmine_give_lingerie from _call_jasmine_give_lingerie_1
    else:
      "You should save the lingerie for a current client."
  return

label jasmine_give_lingerie:
  "[jasmine.name] already has an extensive wardrobe, but she's a woman who likes her clothes.  And getting gifts."
  jasmine.c "Wow.  Thank you!"
  change jasmine resistance by -10
  if jasmine.has_item(lingerie):
    rem 1 lingerie from player
  else:
    give 1 lingerie from player to jasmine notify
  return

# Give Love Potion
label give_lp_jasmine:
  if jasmine.has_tag('love_potion_used'):
    "You've already used a love potion on Jasmine.  Additional ones won't work."
  else:
    if jasmine.status == "on_training" or jasmine.has_tag('girlfriend') or (jasmine.status == "post_training" and jasmine.has_tag('continuing_actions')) or (jasmine.status == "post_training" and jasmine.has_tag('satisfied')):
      wt_image exhi_love_potion_1
      player.c "Here [jasmine.name], I fixed you some tea."
      jasmine.c "What's in it?  It smells funny."
      player.c "Relax, it's just a special blend.  It's good for you."
      wt_image exhi_love_potion_2
      jasmine.c "Mmmm.  Hey, you were right.  This is good."
      "[jasmine.name] pauses for a minute, grinning at you."
      jasmine.c "You are a really good looking man, do you know that?  I'm very lucky to have you watching over me and helping me."
      change jasmine desire by 15
      change jasmine resistance by -10
      add tags 'love_potion_used' to jasmine
      rem 1 love_potion from player notify
    else:
      "You should save the love potion for current clients - or girlfriends, if you think one may be slipping away from you."
  return

# Give Transformation Potion
label give_tp_jasmine:
  call jasmine_transformation_potion_timer from _call_jasmine_transformation_potion_timer
  return

# Give Ring of Secuality
label give_rs_jasmine:
    "That may work, but there's no content for it, so you're better off saving this for someone else."
    return

# Use Water Bowl
label use_wb_jasmine:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_jasmine:
  "Jasmine isn't into whips or chains or any of that sort of stuff.  She'll never agree to wear a collar for you."
  return

# Nipple Rings
label nrj_examine:
  wt_image nipple_rings_1
  "These clip on nipple rings should dress up Jasmine's tits for her new line of work."
  return

label give_nrj_fallback:
  "Save these until the right time to give them to Jasmine."
  return

########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Client Engagement Ends
label jasmine_end_training:
  # use unmodded stat for these checks, as 'test' picks up temporary mods, room mods, etc.
    if jasmine.sos > 60 and (jasmine.publicshow_level >= 3 or jasmine.officeshow_count >= 3):
        wt_image jasmine.image
        "Your engagement to train Jasmine the Exhibitionist has now ended. You receive an email from her husband."
        husband_jasmine "{i}Great job working with [jasmine.name]. She's no longer obsessing about showing herself off in public anymore and feeling bad because she's not brave enough to try it.{/i}"
        husband_jasmine "{i}Thanks for helping my wife. I'll be leaving positive feedback for you online.{/i}"
        call convert( jasmine, "satisfied", False, True ) from _call_convert_25
        $ jasmine.downtown_week = week
        $ jasmine.random_number = renpy.random.randint(1, 10)
        if jasmine.random_number < 2:
            $ jasmine.downtown_countdown = 0
        elif jasmine.random_number < 4:
            $ jasmine.downtown_countdown = 1
        elif jasmine.random_number < 7:
            $ jasmine.downtown_countdown = 2
        elif jasmine.random_number < 9:
            $ jasmine.downtown_countdown = 3
        else:
            $ jasmine.downtown_countdown = 4
    else:
        wt_image exhi_leaving
        "Your engagement to train Jasmine the Exhibitionist has now ended."
        "Jasmine never reached the point of fully embracing her fantasies about public exposure and feeling good about herself for living them out. She and her husband will have to look for other solutions."
        call convert(jasmine,"unsatisfied", True, True) from _call_convert_26
    wt_image current_location.image
    return

# Start Day
label jasmine_start_day:
  ## Wed and Exhi Relationship Event
  if day == 3 and week > jasmine.relationship_week and jasmine.relationship_week > 0:
    if jasmine.has_tag('bimbo'):
      call jasmine_bimbo_events from _call_jasmine_bimbo_events
    elif jasmine.has_tag('girlfriend'):
      call jasmine_girlfriend_events from _call_jasmine_girlfriend_events
  return

# End Day
label jasmine_end_day:
    # Reset temporary counters
    $ jasmine.officeshow_tempcount = 0
    $ jasmine.downtown_event_checked_today = 0
    # Reset temporary tags
    rem tags 'hypno_bj_attempted_today' 'bare_pussy' 'gf_asked_today' 'holding_position' 'sex_on_stage_today' 'spit_on_today' 'discussed_streetwalking_today' 'watched_today' from jasmine
    if jasmine.status == 'on_training':
        if jasmine.has_tag('failed_regular_training_this_week'):
            rem tags 'failed_weekend_training_this_week' from jasmine
    if jasmine.whore_play_status == 3 or jasmine.whore_play_status == 6:
        add tags 'whore_roleplaying' to jasmine
    else:
        rem tags 'whore_roleplaying' from jasmine
    call character_location_return(jasmine) from _call_character_location_return_335
    return

# End Week
label jasmine_end_week:
    ## Exhi Photo
    if jasmine.has_tag('publicshow_photos') and week > jasmine.photod_in_public_week_for_event:
        wt_image phone_1
        "Your phone is ringing."
        wt_image exhi_gf_conversation_2
        "It's [jasmine.name]."
        jasmine.c "I can't believe someone saw the photos and sent them to my husband! They're all over the internet on amateur photo sites."
        player.c "What photos?"
        jasmine.c "The one that man took of me with his cell phone. I'm so embarrassed I could die. And my husband is furious. He says I've made him a laughingstock in front of his friends."
        jasmine.c "I don't know what I'm going to do. I can't see you anymore I need to figure out how to make this right."
        "You never see her again."
        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unvailable'
        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
        call convert(jasmine, "unavailable") from _call_convert_27
    # not sure following two commands are ever used
    $ jasmine.visit_count_total += jasmine.visit_count
    $ jasmine.visit_count = 0
    call character_location_return(jasmine) from _call_character_location_return_336
    ## Whore Lost or Income
    if jasmine.has_tag('whore'):
        $ jasmine.whore_lost_countdown -= 1
        if jasmine.whore_lost_countdown <= 0:
            "You haven't checked on 'Jiggles' for quite a while. She didn't send your cut this week and you can't find her. Whether her husband caught her whoring, or she decided to skip town, or something worse, you never find out."
            call convert(jasmine, 'unavailable') from _call_convert_28  # this automatically removes whore status, stripper status, etc.
        else:
            $ player.whore_income += 25
    return


## Club and Stage Labels

label jasmine_stage_notice:
    ## Exhi Swinger Discussion Not Complete?
    if jasmine.stripper_discussion <= 1:
        if jasmine.status == "post_training" and not jasmine.has_tag('unsatisfied') and jasmine.has_tag('waiting_for_club_access'):
            "As you look around, it occurs to you that this could be the ideal situation for Jasmine to let out her inner exhibitionist."
            rem tags 'waiting_for_club_access' from jasmine
    return

label jasmine_stage_call:
    # this runs when has tag 'showgirl' and you visit the Club
    if player.has_tag('stage_visited_today'):
        if jasmine.has_tag('on_stage_now') and jasmine.downtown_event_checked_today < 2:
            $ jasmine.location = stage
    else:
        if jasmine.downtown_event_checked_today < 2:
            $ jasmine.location = stage
            add tags 'on_stage_now' to jasmine
        ## Exhi Swinger Not Thanked?
        if jasmine.location == stage and jasmine.stripper_discussion == 3:
            call jasmine_update_media from _call_jasmine_update_media_1
            wt_image jasmine.image
            "As you approach the stage, you see [jasmine.name]. She spots you and approaches."
            jasmine.c "Hi! This place is amazing!! Thank you so much for setting this up. I hope you'll stay and watch. I'm about to start a show."
            $ jasmine.stripper_discussion = 4
    return

label jasmine_stage_send_home:
    call character_location_return(jasmine) from _call_character_location_return_337
    return

label jasmine_swingers_room_call:
    if jasmine.has_tag('girlfriend'):
        if jasmine.can_be_interacted and jasmine.downtown_event_checked_today < 2:
            add tags 'in_swingers_room_now' to jasmine
        else:
            "You can't find [jasmine.name], or you'd invite her to join you."
    return

label jasmine_swingers_room_send_home:
    call character_location_return(jasmine) from _call_character_location_return_338
    rem tags 'in_swingers_room_now' from jasmine
    return

## Loving Wife Content

label jasmine_sarah_positive_role_talk_girlfriend:
    if current_target.has_tag('girlfriend') and not sarah.has_tag(tag_expression):
        wt_image exhi_gf_portrait
        "You ask Jasmine to join you."
        jasmine.c "Is something wrong?  You don't usually ask me to get involved in a client session."
        wt_image lw_visit_2_2
        player.c "Nothing's wrong.  I'd like you to meet Sarah.  Sarah, this is my girlfriend Jasmine."
        sarah.c "Hi.  Nice to meet you."
        wt_image exhi_gf_portrait
        player.c "Sarah's husband wants her to have sex with his friends, but she has concerns. I thought speaking to another woman could help her."
        jasmine.c "Really??  Wow, he's ... open-minded, isn't he?"
        wt_image lw_visit_2_12
        sarah.c "I guess.  He says he wants this, but how will he feel afterwards?"
        wt_image exhi_gf_maintain_1
        jasmine.c "Have you guys tried doing something partway?  Maybe have you take your clothes off in front of his friends?"
        wt_image lw_visit_2_12
        sarah.c "No, not really.  At least, not that far.  He likes me to wear skimpy clothes.  The more of my body I show off, the happier he seems to be."
        wt_image exhi_gf_maintain_1
        jasmine.c "Does that get you excited?  Showing your body off to his friends?"
        wt_image lw_visit_2_13
        sarah.c "A little, I guess.  I mean who doesn't like some attention?"
        wt_image exhi_gf_maintain_1
        jasmine.c "I do!  That's for sure."
        wt_image lw_visit_2_11
        sarah.c "I guess I do, too.  But actually getting naked in front of his friends? Let alone having sex with them while my husband watches.  I just don't know how he'll really react to that?  Or how I will, for that matter."
        wt_image exhi_gf_maintain_1
        jasmine.c "I understand. I had these deep, intense fantasies, real ... obsessions. But I was terrified to actually act on them."
        wt_image lw_visit_2_11
        sarah.c "Did you?  Did you act on them?"
        wt_image exhi_gf_maintain_1
        jasmine.c "Yeah, yeah I did, and I do."
        wt_image lw_visit_2_11
        sarah.c "Were they as good in real life?  Did you regret it?"
        wt_image exhi_gf_maintain_1
        jasmine.c "I regret not acting on them earlier.  I used to regret that it cost me my marriage, but I realize now it wasn't the fantasies that made my marriage not work.  It was denying to myself how important they were to me."
        jasmine.c "I ended up with a wonderful guy who wasn't the right person for me ... and I wasn't the right person for him.  Because I kept denying who I was and what I really needed from a relationship."
        wt_image lw_visit_2_12
        sarah.c "That could be my husband, couldn't it?  If I can't help him fulfill his fantasies, he may end up realizing he married the wrong person."
        wt_image exhi_gf_maintain_1
        jasmine.c "Hey, sorry! I'm not trying to say that!! I don't know your husband. Maybe you're right. Maybe he'll find the reality doesn't live up to his fantasy, and he'll regret asking you to go through with it. I'm just telling you ..."
        wt_image lw_visit_2_11
        sarah.c "You're sharing your experience.  I understand.  I appreciate it.  I really do.  Why does love and sex have to be so complicated!  Why do men have to be so complicated?  And us women, too."
        "The two of them get into a long conversation about sexual fantasies and sexual reality and the differences between men and women."
        wt_image lw_visit_2_4
        "Eventually, it's time for Sarah to leave."
        sarah.c "Thanks for talking to me, Jasmine.  It helped a lot to get a woman's perspective."
        add tags 'positive_girlfriend_resolution_today' 'met_girlfriend_jasmine' to sarah
    else:
        $ current_target = None
    return

label jasmine_sarah_positive_role_talk_bimbo:
    if current_target.has_tag('bimbo') and not sarah.has_tag(tag_expression):
        wt_image exhi_bimbo_outfit_8_1
        "You ask Jasmine to join you."
        jasmine.c "I like to meet your friends.  Will she want to see my tits?"
        wt_image lw_visit_2_2
        player.c "Probably not, Jasmine.  This is Sarah."
        sarah.c "Hi.  Shouldn't you have more clothes on?"
        wt_image exhi_bimbo_outfit_8_2
        jasmine.c "But then you couldn't see my tits.  Maybe I should take these clothes off so you can see better?"
        player.c "That's not needed, Jasmine.  Sarah's here to talk.  Her husband wants her to have sex with his friends, but she has concerns.  I thought speaking to another woman could help her?"
        wt_image exhi_bimbo_outfit_8_3
        jasmine.c "Sex is good!  Will you get to suck their cocks?  Sucking cocks is fun.  Could I meet your husband's friends?  I could show them my tits."
        ## remainder of transformed_bimbo content is back in sarah's script
        add tags 'transformed_bimbo_resolution_today' 'met_bimbo_jasmine' to sarah
    else:
        $ current_target = None
    return

label jasmine_sarah_positive_role_sex_girlfriend:
    if current_target.has_tag('girlfriend') or current_target.has_tag('hypno_girlfriend'):
        player.c "Jasmine, could you join us for a moment?"
        wt_image exhi_visit_bj_1
        jasmine.c "Sure.  Hi, Sarah!"
        wt_image lw_visit_4_8
        sarah.c "Hi, Jasmine."
        wt_image exhi_visit_bj_1
        player.c "Jasmine, I'd like you to help me help Sarah again.  You know she's worried about having her husband watch her have sex."
        player.c "It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together.  I want to make love to you, while Sarah watches us."
        wt_image lw_visit_4_2
        sarah.c "Oh no! You don't have to do that, Jasmine.  I don't want to interfere with your love life."
        wt_image exhi_visit_bj_1
        jasmine.c "You're not.  You're actually ... enhancing it."
        wt_image lw_visit_4_3
        sarah.c "Is this ... is this your kink?"
        wt_image exhi_visit_bj_1
        jasmine.c "Sort of.  It's not all of it, but it's part of it.  Thinking about you watching me get fucked, it's ... exciting."
        wt_image exhi_visit_sex_1
        "She pulls off her dress, her erect nipples bearing witness to her excitement."
        wt_image exhi_lw_visit_2_3
        "There's no need for foreplay. An audience is the only warm up Jasmine needs. She gets herself into position ..."
        wt_image exhi_lw_visit_2_4
        "... and you shove yourself into her already wet snatch."
        jasmine.c "ooooo"
        wt_image lw_visit_4_6
        sarah.c "Are you sure you're okay with me being here?  I can go and leave the two of you alone, if you want?"
        wt_image exhi_lw_visit_2_5
        jasmine.c "Don't go!  Please ... ooooo ... having you here is ..."
        wt_image exhi_lw_visit_2_6
        sarah.c "oooohh!!"
        wt_image lw_visit_4_5
        sarah.c "Did you ... did you just cum, that quickly?  I didn't know it was even possible for a woman to orgasm that fast."
        wt_image lw_visit_4_9
        sarah.c "I think you've made your point.  For some people, sex doesn't always have to be in private for it to be fun. I need to go home and think about this."
        "Sarah looks at you with more interest than she has before.  You can't help yourself from teasing her."
        wt_image exhi_lw_visit_2_4
        player.c "You can join us, if you want.  Jasmine came, but I haven't yet.  Jasmine won't mind if you help out."
        jasmine.c "He's right.  It's okay, if you want to?"
        wt_image lw_visit_4_10
        "Sarah blushes."
        sarah.c "I'm sure Jasmine can take care of you."
        wt_image exhi_lw_visit_2_5
        "Jasmine does, but Sarah stays to watch you cum before she leaves, and her blush gets a little more red when you climax."
        wt_image exhi_lw_visit_2_6
        player.c "[player.orgasm_text]"
        $ jasmine.sex_count += 1
        $ jasmine.orgasm_count += 1
        orgasm
        add tags 'watched_girlfriend_this_weekend' to sarah
    else:
        $ current_target = None
    return

label jasmine_sarah_positive_role_sex_bimbo:
    if current_target.has_tag('bimbo'):
        player.c "Jasmine, Sarah's here. Come join us."
        wt_image exhi_bimbo_outfit_8_1
        jasmine.c "Hi! Is she here to look at my tits?"
        player.c "Soon. You remember Sarah's worried about having her husband watch her have sex."
        wt_image exhi_bimbo_outfit_8_2
        jasmine.c "Is she?  I don't remember many things."
        player.c "Well, it's hard for Sarah to imagine what it would be like to have someone watch her have sex, in part because she's never even seen two people have sex together.  So you and I are going to have sex, while Sarah watches us."
        wt_image exhi_bimbo_outfit_8_4
        jasmine.c "Sex is fun! I'll take my clothes off!"
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image exhi_bimbo_outfit_8_23
        "Jasmine wastes no time getting her top off and your pants down. Nuzzling your dick between her breasts, she looks over at Sarah as she licks at it."
        jasmine.c "Doesn't his cock look nice between my titties?  If you want, you could take your top off and put his cock between your titties for a while.  It's fun to be naked with a cock between your titties."
        wt_image lw_visit_4_4
        sarah.c "No, thank you!"
        wt_image exhi_bimbo_outfit_8_17
        jasmine.c "Okay.  You can put his cock in your pussy instead, if you like that better?  That's fun, too."
        wt_image lw_visit_4_8
        sarah.c "No, and I'm leaving now.  I don't want to intrude on your personal time together."
        wt_image exhi_bimbo_outfit_8_28
        jasmine.c "Don't go!  I'll turn around so you can see my titties bouncing as he fucks me.  Please stay and watch my titties."
        $ jasmine.sex_count += 1
        orgasm
        ## rest of content is back in sarah's script
        add tags 'watched_transformed_bimbo_this_weekend' to sarah
    else:
        $ current_target = None
    return


## Character Specific Timers
# Bimbo Events
# Custom Slaver Trade Dialogue
label jasmine_slaver_trade_custom:
    # intro is normal
    call samantha_standard_slaver_trade_introduction from _call_samantha_standard_slaver_trade_introduction
    # outcomes are also normal except for the trade itself, which uses different artwork
    if samantha.temporary_count == 1:
        wt_image slaver_trade_1
        "You spot him as you pull into the garage."
        wt_image slaver_trade_2
        player.c "This space is narrow.  Get out here while I park."
        "As she does so, she doesn't see him approaching from behind."
        wt_image slaver_trade_4
        "Her scream dies in her throat as he shows her the knife. She stares helplessly at you, waiting for you to come to her aid, until he pulls the sack over her head and everything goes dark."
        samantha_slaver "Keep your mouth shut. Nobody wants you hurt. Come with me and everything will be fine. You'll forget about all of this, even your boyfriend, soon enough."
        "She slumps to her knees as he injects her with something. He looks at you for just a moment."
        samantha_slaver "Get out of here. If she's healthy and functional you'll get your payment soon enough. Now get lost."
        "Then he turns his attention back to the disoriented hooded woman at his feet."
        samantha_slaver "Come on, unit. Follow my voice. Time to start your training."
        wt_image living_room.image
        "You head home. You've completed your side of the trade. Now you just need to wait for Sam to be returned to you."
        call convert(current_target, 'unavailable') from _call_convert_133
        $ current_target = samantha
        $ samantha.slaver_events = 10
        $ samantha.doll_return_week = week + 1
        change player energy by -energy_short
        $ samantha.temporary_count = 4
    return


label jasmine_bimbo_events:
    summon jasmine
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    # this command disables running into her downtown later today
    $ jasmine.downtown_event_checked_today = 2
    $ jasmine.relationship_event += 1
    # scroll from 1 through 4
    if jasmine.relationship_event > 4:
        $ jasmine.relationship_event = 1
    # skip event 3 if not gifted lingerie
    if jasmine.relationship_event == 3 and not jasmine.has_item(lingerie):
        $ jasmine.relationship_event = 4
    # First Bimbo relationship event
    if jasmine.relationship_event == 1:
        wt_image exhi_bimbo_outfit_1_1
        "Jasmine comes looking for you.  She's been trying on a white dress."
        jasmine.c "Hi!  Does this look too loose on me?"
        wt_image exhi_bimbo_outfit_1_2
        jasmine.c "It seems a little too long. I wish it came a little higher up my bum."
        wt_image exhi_bimbo_outfit_1_3
        jasmine.c "Maybe if I wore it like this it would look better?"
        if jasmine.has_item(dildo):
            wt_image exhi_bimbo_outfit_1_4
            "She pulls out the dildo you gave her."
            jasmine.c "Trying on clothes always gets me so stressed. I need to relax for a minute and collect my thoughts."
            wt_image exhi_bimbo_outfit_1_5
            jasmine.c "This pretend cock you gave me is perfect for helping me relax."
            "You leave her alone to finish her relaxing."
        else:
            "You assure her the dress looks great however she wants to wear it, and leave her to her wardrobe assessment."
    # Second Bimbo relationship event
    elif jasmine.relationship_event == 2:
        wt_image exhi_bimbo_outfit_6_1
        "You see [jasmine.name] heading for the door, completely nude."
        jasmine.c "Hi! I don't have anything I want to wear, so I'm going to go buy some new clothes."
        player.c "Like that?"
        jasmine.c "Uh huh"
        player.c "Where are going to put your money?"
        jasmine.c "Why do I need money?"
        player.c "To buy ... never mind.  Have fun shopping."
        jasmine.c "Thanks!  I will!!"
    # Third Bimbo relationship event (if has lingerie)
    elif jasmine.relationship_event == 3:
        wt_image exhi_bimbo_outfit_8_1
        jasmine.c "I remembered something!!"
        "Jasmine runs up to you, excited and clearly pleased with herself for succeeding at this mental feat."
        wt_image exhi_bimbo_outfit_8_2
        jasmine.c "You like seeing me in lingerie!!  That's why you bought me some!"
        wt_image exhi_bimbo_outfit_8_3
        jasmine.c "But I don't remember what I'm supposed to do now. I think I'm supposed to take it off, but I just put it on, so that doesn't make any sense. Unless it's so you can get a better look at my tits?"
        jasmine.c "Remind me what I'm supposed to do next?"
        $ title = "What should she do next?"
        menu:
            "Kneel in front of you":
                player.c "Now you kneel down in front of me."
                wt_image exhi_bimbo_outfit_8_21
                jasmine.c "Okay.  Are you going to fuck me?  I like it when you fuck me."
                $ title = "What do you tell her?"
                menu:
                    "I'm going to fuck your mouth":
                        player.c "Yes, I'm going to fuck your tits."
                        jasmine.c "Okay!"
                        wt_image exhi_bimbo_outfit_8_25
                        "She takes your cock in your hand and gently licks it as she opens her mouth."
                        jasmine.c "I like your hard cock in my mouth."
                        wt_image exhi_bimbo_outfit_8_26
                        "She demonstrates how much she likes it, sucking and worshiping your cock with enthusiasm, her lips wrapped tightly around your shaft."
                        wt_image exhi_bimbo_outfit_8_27
                        "A few minutes later, it's your turn to show how much you like it, by emptying your load down the back of her throat."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_bimbo_outfit_8_15
                        jasmine.c "Did I do a good job of wearing the lingerie?"
                        player.c "You did great."
                        jasmine.c "Should I wear it again tomorrow?"
                        player.c "If you can remember."
                        jasmine.c "Oh. How would I do that?"
                        $ jasmine.blowjob_count += 1
                        $ jasmine.swallow_count += 1
                        orgasm notify
                    "I'm going to fuck your tits":
                        player.c "Yes, I'm going to fuck your tits."
                        jasmine.c "Okay!"
                        wt_image exhi_bimbo_outfit_8_23
                        "She cups her tits together, creating a valley for you to plow.  On each upstroke, she licks the head of your cock."
                        jasmine.c "I like your hard cock between my tits."
                        wt_image exhi_bimbo_outfit_8_24
                        "Before long, your cock demonstrates that the feeling is mutual, emptying a load of jizz across her soft skin."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_bimbo_outfit_8_24
                        jasmine.c "Did I do a good job of wearing the lingerie?"
                        player.c "You did great."
                        jasmine.c "Should I wear it again tomorrow?"
                        player.c "If you can remember."
                        jasmine.c "Oh. How would I do that?"
                        $ jasmine.titfuck_count += 1
                        orgasm notify
                    "I'm just going to look at you":
                        player.c "Not today.  I just like seeing you on your knees."
                        wt_image exhi_bimbo_outfit_8_22
                        jasmine.c "Oh.  Okay.  Am I doing a good job of wearing the lingerie?"
                        player.c "You're doing great."
                        jasmine.c "Should I wear it again tomorrow?"
                        player.c "If you can remember."
                        wt_image exhi_bimbo_outfit_8_21
                        jasmine.c "Oh. How would I do that?"
            "Get on her hand and knees for doggy-style":
                player.c "Now you get on your hands and knees and I fuck you from behind."
                wt_image exhi_bimbo_outfit_8_16
                jasmine.c "Okay.  I like it when you fuck me."
                "She pulls off her panties and kneels on the sofa, offering herself to you."
                wt_image exhi_bimbo_outfit_8_17
                jasmine.c "Oh!  I like feeling your hard cock inside me!"
                wt_image exhi_bimbo_outfit_8_18
                jasmine.c "Is it okay to cum when you're wearing lingerie?"
                player.c "Sure"
                wt_image exhi_bimbo_outfit_8_19
                jasmine.c "Oh, good!  ...  oooohh!!"
                "That was fast."
                wt_image exhi_bimbo_outfit_8_20
                "Then again, you don't take much longer yourself."
                player.c "[player.orgasm_text]"
                wt_image exhi_bimbo_outfit_8_15
                jasmine.c "Did I do a good job of wearing the lingerie?"
                player.c "You did great."
                jasmine.c "Should I wear it again tomorrow?"
                player.c "If you can remember."
                jasmine.c "Oh.  How would I do that?"
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                orgasm notify
            "Fuck you cowgirl-style":
                player.c "Now you and I fuck."
                wt_image exhi_bimbo_outfit_8_9
                jasmine.c "Okay.  I like it when we fuck."
                "She pulls off her panties and pulls back her legs, offering herself to you."
                wt_image exhi_bimbo_outfit_8_10
                player.c "Tempting as that position is, why don't you climb up on top of me.  That way you can do the work."
                jasmine.c "Okay"
                wt_image exhi_bimbo_outfit_8_11
                jasmine.c "Oh!  I like feeling your hard cock inside me!"
                wt_image exhi_bimbo_outfit_8_12
                jasmine.c "Is it okay to cum when you're wearing lingerie?"
                player.c "Let's find out."
                wt_image exhi_bimbo_outfit_8_13
                "You flick your tongue across her hard nipples, but you're not sure it was necessary, as she seemed to be already in the process of cumming."
                jasmine.c "oooohh!!"
                wt_image exhi_bimbo_outfit_8_14
                "A moment later, it's your turn."
                player.c "[player.orgasm_text]"
                wt_image exhi_bimbo_outfit_8_15
                jasmine.c "Did I do a good job of wearing the lingerie?"
                player.c "You did great."
                jasmine.c "Should I wear it again tomorrow?"
                player.c "If you can remember."
                jasmine.c "Oh. How would I do that?"
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                orgasm notify
            "Just model the lingerie":
                player.c "Now you show me what your body looks like in the lingerie."
                wt_image exhi_bimbo_outfit_8_4
                jasmine.c "Oh!  Okay.  This is what my ass looks like."
                wt_image exhi_bimbo_outfit_8_5
                jasmine.c "And these are my legs."
                wt_image exhi_bimbo_outfit_8_6
                jasmine.c "This is my pussy, but you can't see it very well because I still have panties on."
                wt_image exhi_bimbo_outfit_8_7
                jasmine.c "These are my tits.  Wait, did I already show you my tits?"
                player.c "Don't worry, I'm always happy to see them regardless."
                wt_image exhi_bimbo_outfit_8_8
                jasmine.c "Oh, good! I think it would be easier, though, to show you what my body looks like in lingerie if I were naked. Is this okay?"
                player.c "Sure, [jasmine.name].  That looks just fine."
    # Fourth Bimbo relationship event
    elif jasmine.relationship_event == 4:
        call forced_movement(backyard) from _call_forced_movement_590
        summon jasmine
        wt_image exhi_bimbo_outfit_3_1
        "Jasmine is sitting naked outside, playing with a bottle of cream."
        wt_image exhi_bimbo_outfit_3_2
        "She seems fascinated with pouring the cream on her boobs ..."
        wt_image exhi_bimbo_outfit_3_3
        "... then rubbing it around."
        wt_image exhi_bimbo_outfit_3_4
        "She keeps this up for some time, until she notices you and looks up."
        jasmine.c "I can't get it to stay on."
        wt_image exhi_bimbo_outfit_3_5
        player.c "Maybe you should try putting more on?"
        jasmine.c "Okay, I'll try that."
        wt_image exhi_bimbo_outfit_3_6
        "You leave her to her efforts, making a mental note to buy more cream the next time you're at the grocery store."
        call forced_movement(living_room) from _call_forced_movement_591
    else:
        sys "There's been an error in the jasmine_bimbo_events label."
    # randomize when next event will occur
    $ jasmine.random_number = renpy.random.randint(1, 10)
    if jasmine.random_number < 3:
        $ jasmine.relationship_week = week + 2
    elif jasmine.random_number < 6:
        $ jasmine.relationship_week = week + 3
    elif jasmine.random_number < 9:
        $ jasmine.relationship_week = week + 4
    else:
        $ jasmine.relationship_week = week + 5
    call character_location_return(jasmine) from _call_character_location_return_339
    return

# Convert Character to Bimbo
label jasmine_convert_bimbo:
    if jasmine.has_tag('showgirl'):
        call unconvert(jasmine, 'showgirl') from _call_unconvert_62
        "[jasmine.name] won't be able to keep performing at the Club.  She'll never keep track of her schedule, or how to get there.  She might not even remember to wear clothes to take off."
    if jasmine.has_tag('whore'):
        call unconvert(jasmine, 'whore') from _call_unconvert_63
        "[jasmine.name]'s whoring days are behind her.  Or at least, the days when she brings you money are.  As a bimbo, she'll never remember to ask the johns for payment."
    if jasmine.has_tag('girlfriend'):
        call unconvert(jasmine, 'girlfriend') from _call_unconvert_64
    call convert( jasmine, "bimbo" , False, False, True ) from _call_convert_29
    add tags 'post_continuing_actions' 'shut_off_end_session' to jasmine
    rem tags 'continuing_actions' 'follows' from jasmine
    $ jasmine.fixed_location = bedroom
    $ jasmine.location = bedroom
    $ jasmine.relationship_event = 0
    $ jasmine.relationship_week = week + 3
    return

# Convert Character to Girlfriend
label jasmine_convert_girlfriend:
    call convert( jasmine, "girlfriend", False, False, True ) from _call_convert_30
    add tags 'post_continuing_actions' 'swingers_room_possible' 'shut_off_end_session' to jasmine
    rem tags 'continuing_actions' 'follows' from jasmine
    $ jasmine.fixed_location = bedroom
    $ jasmine.location = bedroom
    $ jasmine.relationship_week = week + 1
    $ jasmine.maintain_week_gf = week + 2
    # next command is to provide the right options for hypnosis when your girlfriend
    $ jasmine.privateshow_count = 3
    return

# Convert Character to Showgirl
label jasmine_convert_showgirl:
    $ jasmine.stripper_discussion = 3
    call convert( jasmine, "showgirl", False, False, True ) from _call_convert_31
    return

# Convert Character to Whore
label jasmine_convert_whore:
    $ jasmine.whore_play_status = 9
    call convert( jasmine, "whore", False, False, True ) from _call_convert_32
    add tags 'post_continuing_actions' to jasmine
    rem tags 'continuing_actions' 'follows' 'shut_off_end_session' from jasmine
    $ jasmine.fixed_location = bedroom
    $ jasmine.location = bedroom
    $ jasmine.downtown_week = week
    $ jasmine.whore_lost_countdown = 5
    if jasmine.has_tag('showgirl'):
        $ jasmine.club_whore_event_week = week + 4
    else:
        $ jasmine.change_full_name(name =  "Jiggles", suffix = "the Streetwalker")
    return

# Description Display
label jasmine_description_display:
    wt_image jasmine.image
    if jasmine.status == 'post_training':
        # main description
        if jasmine.has_tag('bimbo'):
            "[jasmine.name] used to spend a lot of time thinking about showing off her body in public. Now she happily shows off her body without thinking very much at all."
        elif jasmine.has_tag('girlfriend'):
            if jasmine.has_tag('showgirl'):
                "When she came to you, [jasmine.name] had no safe outlet for her exhibitionist urges. Now she's a happy and popular show girl at the most exclusive Club in town, and your own personal private dancer."
            else:
                "When she came to you, [jasmine.name] had no safe outlet for her exhibitionist urges. Now she's your own personal private dancer."
        elif jasmine.has_tag('whore'):
            if jasmine.has_tag('showgirl'):
                "When she came to you, [jasmine.name] was afraid to take her top off in public. Now she proudly displays her tits on the stage to the applause of crowds and on the streets for the more personal thanks of her johns."
            else:
                "When she came to you, [jasmine.name] thought she just wanted to be an exhibitionist.  You helped her find her true calling as an 'available to anyone' street walker."
        elif jasmine.has_tag( 'showgirl' ):
            "When she came to you, [jasmine.name] had no safe outlet for her exhibitionist urges. Now she's a happy and popular show girl at the most exclusive Club in town."
        elif jasmine.has_tag('continuing_actions'):
            "Jasmine the Exhibitionist wasn't much of an exhibitionist until she met you, just a woman afraid to act on her desires. Now she's an experienced - and happy - public flasher."
        # relationship status
        if jasmine.has_tag('girlfriend'):
            $ jasmine.temporary_count = jasmine.maintain_week_gf - week
            if jasmine.temporary_count >= 2:
                "She is happy with your relationship."
            elif jasmine.temporary_count > 0:
                "She wishes you would spend more time with her."
            elif jasmine.has_tag('love_potion_used'):
                "She feels like she never gets to spend time with you, but the lingering effects of the love potion make it impossible for her to contemplate leaving and not seeing you again."
            elif jasmine.temporary_count >-2:
                "She's unhappy with your lack of attention and is considering leaving you."
            else:
                "She feels ignored and plans to leave you unless you do something with her soon."
        elif jasmine.has_tag('bimbo'):
            "She's happy being your mindless bimbo."
        elif jasmine.has_tag('continuing_actions'):
            if jasmine.whore_play_status == 5 or jasmine.whore_play_status == 7 or jasmine.whore_play_status == 8:
                "She's horrified by your efforts to turn her into 'Jiggles', and even more horrified to find she can't bring herself to shut the whole whore subject down completely."
            if jasmine.gf_conversion_status == 0:
                if jasmine.has_tag('love_potion_used'):
                    "She loves spending time with you, but that's the effect of the potion. She doesn't otherwise see you as anyone special."
                else:
                    "She isn't quite sure why she's agreed to spend time with you. She doesn't see you as anyone special."
            elif jasmine.gf_conversion_status == 1:
                if jasmine.has_tag('love_potion_used'):
                    "She loves spending time with you, but that's the effect of the potion. She otherwise see you as a fuck buddy, and rationalizes the time she spends with you as being just about sex, and not important."
                else:
                    "She sees you as a fuck buddy, but nothing else. She rationalizes the time she spends with you as being just about sex, and not important."
            elif jasmine.gf_conversion_status == 2:
                "She feels guilty about spending time with you behind her husband's back. She can't quite bring herself to admit that she's starting to think about you as more than just a fuck buddy."
            elif jasmine.gf_conversion_status == 3:
                "She's a conflicted mess of guilt and desire. She's questioning everything in her life right now, but finds it easier to talk about how unfair she's being to her husband rather than what's best for her."
            elif jasmine.gf_conversion_status == 4:
                "She's convinced herself that her husband would be better off without her. She still has a hard time admitting that she wants something he can't give her."
    elif jasmine.status == "on_training":
        "[jasmine.name] is obsessed with the idea of exposing herself in public. She longs to experience the naughtiness and danger of exposing herself in inappropriate places, but isn't confident enough to act on those desires."
        "You have until the end of week [jasmine.training_limit] to complete this engagement."
    # note whore purposefully excluded from below as it is a special state for Jasmie
    if not jasmine.has_any_tag('bimbo', 'degraded', 'doll', 'petgirl', 'transformed_slavegirl'):
        if jasmine.has_tag('trigger_implanted'):
            "You have implanted a hypnotic trigger in her."
        if jasmine.has_tag('love_potion_used'):
            "She is under the influence of a love potion."
        "[jasmine.statblock]"
        $ items = ", ".join(i.name for i in jasmine.get_items()) if jasmine.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    return

# Girlfriend Events
label jasmine_girlfriend_events:
    $ jasmine.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    # this command disables running into her downtown later today
    $ jasmine.downtown_event_checked_today = 2
    $ jasmine.relationship_event += 1
    # scroll from 1 through 6
    if jasmine.relationship_event > 6:
        $ jasmine.relationship_event = 1
    # skip event 4 if not gifted lingerie
    if jasmine.relationship_event == 4 and not jasmine.has_item(lingerie):
        $ jasmine.relationship_event = 5
    # First GF Event
    if jasmine.relationship_event == 1:
        wt_image phone_1
        "Your phone is ringing."
        wt_image exhi_office_1_3
        jasmine.c "It's me.  I'm at work and ... my clothes seem to be coming off.  Wanna come by and see?"
        $ title = "Do you want to go see her?"
        menu:
            "I'll be right over":
                call forced_movement(outdoors) from _call_forced_movement_592
                summon jasmine
                wt_image exhi_office_1_1
                "Jasmine is waiting for you, fully dressed, at least until you close her office door behind you."
                wt_image exhi_office_5_1
                jasmine.c "I'm glad you dropped by."
                wt_image exhi_office_5_2
                jasmine.c "I've been having a hard time keeping these under wraps ..."
                wt_image exhi_office_5_3
                jasmine.c "... waiting for the right audience. Now that you're here ..."
                wt_image exhi_office_5_4
                jasmine.c "... is there anything you wanted?"
                $ title = "What do you want?"
                menu:
                    "Just a show":
                        player.c "A show would be nice."
                        wt_image exhi_office_5_3
                        jasmine.c "A show, huh?  You can already see my tits ..."
                        wt_image exhi_office_5_20
                        jasmine.c "... so it must be this you want a closer look at."
                        wt_image exhi_office_2_3
                        jasmine.c "Is this better?"
                        wt_image exhi_office_2_4
                        jasmine.c "Or would you prefer ..."
                        wt_image exhi_office_5_16
                        jasmine.c "... to see me like this?"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        jasmine.c "Hang on!  I'm just finishing something up."
                        wt_image exhi_office_5_21
                        coworker_unnamed_jasmine "I want to talk to you about this file."
                        jasmine.c "Okay, just let me put this away and I'll come find you."
                        "That's your cue to find your way out."
                        change player energy by -energy_short notify
                    "Tit job":
                        player.c "Now that those are out, why don't you put them to good use?"
                        wt_image exhi_office_5_5
                        jasmine.c "Okay"
                        "She pulls down your pants ..."
                        wt_image exhi_office_5_6
                        "... and nestles your cock in her ample bosom, stroking it up and down her soft mounds until ..."
                        wt_image exhi_office_5_7
                        "... she dips her head to capture the explosion of jizz she's coaxed from your balls."
                        player.c "[player.orgasm_text]"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        wt_image exhi_office_5_8
                        jasmine.c "Hang on!  I'm just finishing something up."
                        coworker_unnamed_jasmine "I want to talk to you about this file."
                        jasmine.c "Okay, just let me put this away and I'll come find you."
                        "That's your cue to find your way out."
                        $ jasmine.titfuck_count += 1
                        orgasm notify
                    "Blow job":
                        player.c "How about a blow job?"
                        wt_image exhi_office_5_5
                        jasmine.c "Okay"
                        "She pulls down your pants ..."
                        wt_image exhi_office_5_9
                        "... and takes your cock in her mouth, licking, suckling and pleasuring it until ..."
                        wt_image exhi_office_5_10
                        "... she coaxes an explosion of jizz from your balls and into her mouth."
                        player.c "[player.orgasm_text]"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        wt_image exhi_office_5_8
                        jasmine.c "Hang on!  I'm just finishing something up."
                        coworker_unnamed_jasmine "I want to talk to you about this file."
                        jasmine.c "Okay, just let me put this away and I'll come find you."
                        "That's your cue to find your way out."
                        $ jasmine.blowjob_count += 1
                        $ jasmine.swallow_count += 1
                        orgasm notify
                    "Sex":
                        player.c "Get out of that dress and up on your desk."
                        wt_image exhi_office_2_4
                        jasmine.c "Oh yeah?  What are you going to do with me up here?"
                        wt_image exhi_office_5_11
                        player.c "This"
                        "You slide your dick into her wet and waiting pussy and start fucking her."
                        jasmine.c "ooooo"
                        wt_image exhi_office_5_12
                        player.c "You try to wait for her, but her cunt feels too good around your cock, and she doesn't seem to be quite able to cum this way today. You, on the other hand, have no such problem."
                        player.c "[player.orgasm_text]"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        jasmine.c "oooo!  hang on!  I'm just ... just finishing ... just finishing ..."
                        wt_image exhi_office_5_13
                        jasmine.c "oooohh!!"
                        coworker_unnamed_jasmine "Are you okay? I want to talk to you about this file."
                        jasmine.c "I'm ... really good.  Let me get my thoughts in order and I'll come find you."
                        "That's your cue to find your way out."
                        $ jasmine.orgasm_count += 1
                        $ jasmine.sex_count += 1
                        orgasm notify
                    "Take her from behind":
                        player.c "Get out of that dress and turn around on your desk."
                        wt_image exhi_office_5_16
                        jasmine.c "Oh yeah?  What are you going to do with me up here?"
                        wt_image exhi_office_5_17
                        player.c "This"
                        "You slide your dick into her wet and waiting pussy and start fucking her."
                        jasmine.c "ooooo"
                        wt_image exhi_office_5_18
                        player.c "You try to wait for her, but her cunt feels too good around your cock, and she doesn't seem to be quite able to cum this way today. You, on the other hand, have no such problem."
                        player.c "[player.orgasm_text]"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        jasmine.c "oooo!  hang on!  I'm just ... just finishing ... just finishing ..."
                        wt_image exhi_office_5_19
                        jasmine.c "oooohh!!"
                        coworker_unnamed_jasmine "Are you okay? I want to talk to you about this file."
                        jasmine.c "I'm ... really good.  Let me get my thoughts in order and I'll come find you."
                        "That's your cue to find your way out."
                        $ jasmine.orgasm_count += 1
                        $ jasmine.sex_count += 1
                        orgasm notify
                    "Pleasure her":
                        player.c "Get out of that dress and up on your desk."
                        wt_image exhi_office_2_4
                        jasmine.c "Oh yeah?  What are you going to do with me up here?"
                        wt_image exhi_office_5_14
                        player.c "This"
                        "She moans as you rub her already wet pussy with your fingers ..."
                        jasmine.c "ooooo"
                        wt_image exhi_office_5_15
                        "... then moans again, louder, as your tongue laps her."
                        jasmine.c "ooooo  ...  oooooo"
                        "*knock*  *knock*  *knock*"
                        coworker_unnamed_jasmine "[jasmine.name], are you in there?"
                        jasmine.c "oooo!  hang on!  I'm just ... just finishing ... just finishing ..."
                        jasmine.c "oooohh!!"
                        coworker_unnamed_jasmine "Are you okay? I want to talk to you about this file."
                        jasmine.c "I'm ... really good.  Let me get my thoughts in order and I'll come find you."
                        "That's your cue to find your way out."
                        $ jasmine.orgasm_count += 1
                        change player energy by -energy_short notify
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                call forced_movement(living_room) from _call_forced_movement_593
            "Not today":
                player.c "Busy day, today.  Some other time."
                jasmine.c "Aw.  Now I have to do  ...  work."
    # Second GF Event
    elif jasmine.relationship_event == 2:
        call forced_movement(living_room) from _call_forced_movement_594
        summon jasmine
        wt_image exhi_gf_sex_1_1
        "[jasmine.name] is sitting naked on the sofa.  She beckons when she sees you."
        jasmine.c "Come here."
        wt_image exhi_gf_sex_1_2
        "As you approach, she strokes your cock through your pants."
        jasmine.c "I have to go to work in a few minutes.  Want to send me there happy?"
        $ title = "What do you say?"
        menu:
            "Sure":
                wt_image exhi_gf_sex_1_4
                player.c "Sure. How do you want to do this?"
                wt_image exhi_gf_sex_1_8
                jasmine.c "Have a seat.  I want a ride on that big, beautiful cock of yours."
                wt_image exhi_gf_sex_1_9
                "You sit on the sofa and she climbs on top of you, rubbing the tip of your hard cock against her clit ..."
                jasmine.c "oooo"
                wt_image exhi_gf_sex_1_10
                "... and then settles down with your hard shaft inside her slick snatch."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_1_11
                "Up and down she rides you, faster and faster and faster ..."
                jasmine.c "oooo  ...  oooooo"
                wt_image exhi_gf_sex_1_12
                "... until the feeling of her cunt sliding up and down your cock brings both of you over the edge, first her, then you before her orgasm subsides."
                jasmine.c "ooooo  ...  oooohh!!"
                player.c "[player.orgasm_text]"
                wt_image exhi_gf_sex_1_8
                jasmine.c "Mmmm.  I'm going to have a good day at work today."
                "She gives you a light kiss, then disappears."
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                orgasm notify
            "How about a blow job?":
                player.c "How about a blow job?"
                wt_image exhi_gf_sex_1_4
                jasmine.c "Hmmmm.  That wasn't what I was thinking of ..."
                wt_image exhi_gf_sex_1_5
                jasmine.c "... but your cock does look delicious."
                wt_image exhi_gf_sex_1_6
                "She takes you into her mouth ..."
                wt_image exhi_visit_bj_8
                "... and gives you an intense, arousing blow job that soon has you on the brink of orgasm."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image exhi_visit_bj_3
                        "Jasmine wraps her lips tightly around your cock, swallowing every spurt of your load as it shoots into her mouth and down her throat."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_gf_sex_1_13
                        jasmine.c "Guess I won't be thirsty at the office this morning."
                        wt_image exhi_gf_sex_1_7
                        "She opens her mouth to demonstrate that she swallowed your whole load, then heads off to get ready for work."
                        $ jasmine.swallow_count += 1
                    "On her face":
                        wt_image exhi_visit_bj_4
                        "You pull out of her mouth and shoot your load over her upturned face."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_visit_bj_5
                        jasmine.c "Mmmm.  I wonder if I should clean up, or go into the office like this?"
                        player.c "Up to you."
                        $ jasmine.facial_count += 1
                $ jasmine.blowjob_count += 1
                $ jasmine.maintain_week_gf += 1
                orgasm notify
            "Not today":
                wt_image exhi_gf_sex_1_14
                player.c "Not today.  I've got things I need to do."
                wt_image exhi_gf_sex_1_15
                jasmine.c "That's too bad. I was so going to make it worth your while."
                wt_image exhi_gf_sex_1_8
                jasmine.c "Guess I may as well head to the office.  Should I dress, or go like this?"
                player.c "Up to you."
    # Third GF Event
    elif jasmine.relationship_event == 3:
        call forced_movement(living_room) from _call_forced_movement_595
        summon jasmine
        wt_image exhi_strip_9_1
        "[jasmine.name] is sitting in the living room. She smiles as you walk by ..."
        wt_image exhi_strip_9_2
        "... and pulls up her top."
        wt_image exhi_strip_9_3
        "Having caught your attention, she pulls down her sweats ..."
        wt_image exhi_strip_9_4
        "... cups her tits ..."
        wt_image exhi_strip_9_5
        "... and removes her panties."
        "She sits there for a few minutes, until you take a step towards her, then she smiles, gets up, and disappears, shooting you a little grin as she goes."
        wt_image living_room.image
        "Seems she was just in the mood to be a tease today."
    # Fourth GF Event, if has lingerie
    elif jasmine.relationship_event == 4:
        wt_image current_location.image
        "[jasmine.name] calls to you from the bedroom."
        jasmine.c "Could you come in her for a moment?"
        call forced_movement(bedroom) from _call_forced_movement_596
        summon jasmine
        wt_image exhi_gf_sex_4_29
        "When you enter, she's dressed in a skimpy negligee."
        wt_image exhi_gf_sex_4_1
        jasmine.c "I thought you might like seeing me in this outfit. Maybe even like it enough to give me something in return?"
        player.c "What would that be?"
        wt_image exhi_gf_sex_4_30
        jasmine.c "A hot fuck that makes me cum."
        $ title = "What do you do?"
        menu menu_jasmine_gf_event_4:
            "Tell her you need to see more of the outfit to decide":
                player.c "I'm not sure.  I'd have to check the outfit out some more."
                wt_image exhi_gf_sex_4_31
                jasmine.c "Really?  Because there's not that much of it to see."
                wt_image exhi_gf_sex_4_32
                jasmine.c "Which is a big reason why I thought you might find seeing it on me ... sexy."
                wt_image exhi_gf_sex_4_2
                jasmine.c "So what do you think?  Do I look good enough to fuck until I cum?"
                jump menu_jasmine_gf_event_4
            "Tell her you're too busy today":
                player.c "I don't have time today."
                wt_image exhi_gf_sex_4_10
                jasmine.c "Really?  That's ... too bad."
                wt_image exhi_gf_sex_4_3
                jasmine.c "I guess this didn't look as nice as I'd hoped."
                wt_image exhi_gf_sex_4_33
                if jasmine.has_item(dildo):
                    jasmine.c "I suppose I'll have to use the dildo you gave me."
                else:
                    jasmine.c "I suppose I'll have to use my fingers."
                wt_image exhi_gf_sex_4_4
                jasmine.c "Too bad you're too busy to stay around and watch. Bye bye!"
            "Pleasure her":
                wt_image exhi_gf_sex_4_34
                player.c "I suppose I have time to look after my girl."
                jasmine.c "Mmmmm"
                wt_image exhi_gf_sex_4_11
                "She melts into your kiss, then groans softly as your thumb traces the outline of her stiffening nipple through the negligee."
                jasmine.c "oooo"
                wt_image exhi_gf_sex_4_12
                player.c "Are your nipples hard already?"
                jasmine.c "Yes"
                player.c "Because of our kiss, or because you were showing off in this outfit?"
                jasmine.c "Both?"
                wt_image exhi_gf_sex_4_13
                player.c "Let's see if I can get them even harder, without tapping into your exhibitionist fantasies."
                wt_image exhi_gf_sex_4_15
                "They soon do under the attention of your tongue."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_4_14
                player.c "Can you get off on just my tongue?"
                jasmine.c "ooooo  ...  I ... I'm not sure."
                wt_image exhi_gf_sex_4_16
                player.c "What if I move tongue to somewhere else?"
                "Turning her around, you pull her negligee down over her soft bottom ..."
                wt_image exhi_gf_sex_4_17
                "... and then remove her panties."
                jasmine.c "ooooo  ...  in that case, yes, yes, I'm sure I can."
                wt_image exhi_gf_sex_4_18
                "She lies back and spreads her legs as you lean forward ..."
                wt_image exhi_gf_sex_4_35
                "... and gently lick her glistening snatch."
                jasmine.c "ooooooo"
                wt_image exhi_gf_sex_4_36
                "Before long, she tenses up ..."
                jasmine.c "ooooo  ...  ooooooo"
                wt_image exhi_gf_sex_4_37
                "... and climaxes against your tongue."
                jasmine.c "ooooo  ...  oooohh!!"
                wt_image exhi_gf_sex_4_9
                jasmine.c "Mmmmm.  Thank you."
                "One task complete for the day.  Time to move on to the next"
                $ jasmine.orgasm_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                change player energy by -energy_short notify
            "Have her ride you":
                player.c "In that case, get the negligee off and climb on board."
                wt_image exhi_gf_sex_4_20
                jasmine.c "Are you hard already?"
                player.c "When looking at you, I'm always hard."
                wt_image exhi_gf_sex_4_21
                jasmine.c "That's so ... fucking sweet."
                "She wastes no time getting naked ..."
                wt_image exhi_gf_sex_4_22
                "... or climbing on top of you, impaling herself on your hard dick."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_4_23
                "You turn her around and with your hands under her ass ..."
                wt_image exhi_gf_sex_4_38
                "... guide her as she rides you ..."
                jasmine.c "oooo"
                wt_image exhi_gf_sex_4_39
                "... up and down ..."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_4_40
                "... faster and faster ..."
                jasmine.c "oooooo"
                wt_image exhi_gf_sex_4_24
                "... until she cums, the feeling of her spasming around your hard dick triggering your own climax."
                jasmine.c "oooooo  ...  oooohh!!"
                player.c "[player.orgasm_text]"
                wt_image exhi_gf_sex_4_9
                jasmine.c "Mmmmm.  Thank you."
                "One task complete for the day.  Time to move on to the next"
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                orgasm notify
            "Fuck her from behind":
                player.c "In that case, get the negligee off and your ass in the air."
                wt_image exhi_gf_sex_4_32
                jasmine.c "Okay"
                wt_image exhi_gf_sex_4_41
                "She crawls onto the bed and strips out of her clothes ..."
                wt_image exhi_gf_sex_4_42
                "... and waits eagerly for you to mount her.  She's dripping wet, letting you slide inside her easily."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_4_25
                "You start pistoning in and out of her ..."
                jasmine.c "oooo"
                wt_image exhi_gf_sex_4_43
                "... back and forth ..."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_4_26
                "... faster and faster ..."
                jasmine.c "oooooo"
                wt_image exhi_gf_sex_4_27
                "... until she cums, her hips bucking wildly as she orgasms."
                jasmine.c "oooooo  ...  oooohh!!"
                "Now it's your turn."
                $ title = "Where do you want to cum?"
                menu:
                    "In her":
                        wt_image exhi_gf_sex_4_28
                        "With one more hard thrust, you pump your load inside her."
                        player.c "[player.orgasm_text]"
                        jasmine.c "oooo"
                        wt_image exhi_creampie_3
                        jasmine.c "Mmmmm.  Thank you for getting me off."
                        "She plays idly with the sperm dripping out of her slit. It's hard to tell exactly what she's thinking."
                    "On her":
                        wt_image exhi_whore_2_21
                        "You pull out and pump your load over her upturned ass."
                        player.c "[player.orgasm_text]"
                        jasmine.c "oooo"
                        wt_image exhi_whore_2_22
                        jasmine.c "Mmmmm.  Thank you for getting me off."
                        "One task complete for the day.  Time to move on to the next"
                $ jasmine.orgasm_count += 1
                $ jasmine.sex_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                orgasm notify
            "Tell her to finger herself":
                player.c "Take your clothes off, lie on the bed, and finger fuck yourself."
                wt_image exhi_gf_sex_4_31
                jasmine.c "I wanted you to get me off."
                player.c "I am getting you off. Lie on the bed and do as you're told."
                if jasmine.test('submission', 50):
                    wt_image exhi_gf_sex_4_5
                    "She hesitates, then submissively gets onto the bed ..."
                    wt_image exhi_gf_sex_4_6
                    "... and removes her negligee and panties."
                    player.c "Spread yourself open."
                    wt_image exhi_gf_sex_4_7
                    "This wasn't what she had in mind, but being 'forced' to expose herself like this is making her wet."
                    wt_image exhi_gf_sex_4_4
                    if jasmine.whore_play_status > 4:
                        player.c "Your little whore cunt is wet.  It can't wait to show me what a greedy whore cunt it is.  Go on then, feed your fingers into your greedy whore cunt.  Show me how a whore fucks herself when she can't find a john to fill her greedy cunt with cock."
                    else:
                        player.c "Now finger yourself.  You said you want an orgasm.  Show me how bad you want it.  Finger fuck yourself."
                    wt_image exhi_gf_sex_4_8
                    "Breathing deeply, she does as she's told.  She's more than a little turned on ..."
                    wt_image exhi_gf_sex_4_45
                    "... and her finger is soon moving quickly in and out and up and down her slit."
                    jasmine.c "ooooo"
                    wt_image exhi_gf_sex_4_46
                    "As her pace quickens, she inserts a second digit ..."
                    wt_image exhi_dildo_3_9
                    "... and frigs herself to climax."
                    jasmine.c "oooo  ...  oooohh!!"
                    wt_image exhi_gf_sex_4_8
                    player.c "See how much fun you have when you follow instructions?"
                    "She says nothing, but you can see she's still gently rubbing her still throbbing pussy."
                    if not jasmine.has_tag('fingering_under_orders'):
                        add tags 'fingering_under_orders' to jasmine
                        change jasmine submission by 5
                    $ jasmine.orgasm_count += 1
                    if jasmine.maintain_week_gf < week + 2:
                        $ jasmine.maintain_week_gf = week + 2
                    change player energy by -energy_short notify
                else:
                    wt_image exhi_gf_sex_4_10
                    jasmine.c "No way.  If I have to play with myself to get off, I'll do it in private.  No show today."
                    jump menu_jasmine_gf_event_4
        call forced_movement(living_room) from _call_forced_movement_597
    # Fifth GF Event
    elif jasmine.relationship_event == 5:
        call forced_movement(bathroom) from _call_forced_movement_598
        summon jasmine
        wt_image exhi_gf_sex_2_1
        "Jasmine's just finishing up her shower as you're getting ready in the morning."
        wt_image exhi_gf_sex_2_2
        "She sneaks up behind you ..."
        wt_image exhi_gf_sex_2_3
        "... and pulls away your towel."
        player.c "Hey!"
        wt_image exhi_gf_sex_2_4
        "Kissing you gently, she takes your cock in her soft hand and strokes you hard."
        jasmine.c "Are you very busy today, or do you have some time?"
        $ title = "What do you tell her?"
        menu:
            "I have time for a blow job":
                player.c "I have time for a blow job."
                wt_image exhi_gf_sex_2_11
                jasmine.c "Okay"
                "She leans down and gives your cock a lick ..."
                wt_image exhi_gf_sex_2_12
                "... drops to her knees ..."
                wt_image exhi_bimbo_outfit_2_7
                "... and gives you a loving and enthusiastic blow job that soon has your balls ready to explode."
                $ title = "Where do you want to cum?"
                menu:
                    "On her face":
                        wt_image exhi_bimbo_outfit_2_16
                        player.c "Take my cock out of your mouth, [jasmine.name]"
                        wt_image exhi_facial_3
                        "She tilts her head back as you aim at her face."
                        wt_image exhi_facial_1
                        player.c "[player.orgasm_text]"
                        wt_image exhi_facial_2
                        "She starts laughing as the jizz coats her face."
                        jasmine.c "Shoot!  Next time remind me to start things before I have a shower.  Now I need to clean up again!"
                        $ jasmine.facial_count += 1
                    "In her mouth":
                        wt_image exhi_bimbo_outfit_2_5
                        "Placing a hand on her head to hold her still, you release your load into her."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_gf_sex_2_17
                        "She pumps your shaft, milking every last drop from your balls and into her waiting mouth as she squeezes her own tit."
                        wt_image exhi_gf_sex_2_15
                        "With a twinkle in her eye, she grins up at you."
                        jasmine.c "Hope you have a great day!"
                        player.c "I will now."
                        $ jasmine.swallow_count += 1
                $ jasmine.blowjob_count += 1
                if jasmine.maintain_week_gf < week + 2:
                    $ jasmine.maintain_week_gf = week + 2
                orgasm notify
            "I have time to pleasure you":
                player.c "Of course I've got time to look after my girl.  Hop up."
                wt_image exhi_bimbo_outfit_2_6
                jasmine.c "Okay!"
                wt_image exhi_gf_sex_2_13
                "As she settles down, you place your mouth between her legs ..."
                wt_image exhi_gf_sex_2_6
                "... and begin gently licking her."
                jasmine.c "ooooo"
                wt_image exhi_gf_sex_2_14
                "Her juices seep out of her in a steadily increasing flow ..."
                wt_image exhi_gf_sex_2_7
                jasmine.c "oooo  ...  ooooo"
                wt_image exhi_gf_sex_2_8
                "... and her clit emerges to stand at attention, eager for the touch of your tongue ..."
                jasmine.c "ooooo  ...  oooooo"
                wt_image exhi_gf_sex_2_9
                "... a few flicks from which are enough to send her over the edge."
                jasmine.c "ooooo  ...  oooohh!!"
                wt_image exhi_gf_sex_2_10
                "She stands up and kisses you."
                jasmine.c "That felt great.  Oh!!  I can taste me on your lips!"
                player.c "Tastes good, doesn't it?"
                jasmine.c "I'm glad you think so."
                "She gives you a shy smile, kisses you once again quickly, then runs off, leaving you to continue your day."
                $ jasmine.orgasm_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                change player energy by -energy_short notify
            "I'm too busy right now":
                player.c "Sorry, [jasmine.name], I really am too busy right now."
                wt_image exhi_gf_sex_2_5
                jasmine.c "Ahhh, that's too bad.  Maybe next time."
                "She gives you a quick hug, then disappears, leaving you to your busy day."
        call forced_movement(living_room) from _call_forced_movement_599
    # Sixth GF Event
    elif jasmine.relationship_event == 6:
        call forced_movement(kitchen) from _call_forced_movement_600
        summon jasmine
        wt_image exhi_gf_sex_3_1
        "A nearly naked Jasmine wanders into the kitchen, catching you by surprise."
        player.c "Hi?"
        jasmine.c "Hi"
        wt_image exhi_gf_sex_3_2
        "Just in case you're feeling slow witted this morning, she makes her intentions clear."
        jasmine.c "Fuck me?"
        $ title = "What do you tell her?"
        menu:
            "Sure, I'll fuck you":
                player.c "Okay, let's go to the bedroom."
                wt_image exhi_gf_sex_3_11
                jasmine.c "Why?  We can do it right here."
                player.c "In the kitchen?"
                jasmine.c "Uh huh, it'll be ... naughty."
                wt_image exhi_gf_sex_3_12
                "Slightly unhygienic, too, but you can deal with that with a thorough cleaning later.  Right now, [jasmine.name]'s pussy has your full attention, as she lifts her leg onto the counter.  As promised, she's ready and eager to fuck, and you penetrate her already wet snatch with ease."
                jasmine.c "oooo"
                wt_image exhi_gf_sex_3_13
                "[jasmine.name] made it clear she's horny, so you try to control your own pleasure long enough for her to reach hers."
                jasmine.c "ooooo  ...  oooooo"
                wt_image exhi_gf_sex_3_14
                "That proves to be no problem, as she cums quickly, grinding her clit against the counter top as your cock thrusts in and out of her."
                wt_image exhi_gf_sex_3_22
                jasmine.c "ooooo  ...  oooohh!!"
                wt_image exhi_gf_sex_3_15
                "Now it's your turn. You thrust into her, deeper and deeper, harder and harder, until you let go, flooding her insides with your spunk."
                player.c "[player.orgasm_text]"
                wt_image exhi_gf_sex_3_23
                jasmine.c "Mmmm.  Thanks for that.  I hope it felt good for you, too?"
                player.c "It did."
                $ jasmine.sex_count += 1
                $ jasmine.orgasm_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                orgasm notify
            "No, but you can blow me":
                player.c "No, but you can blow me."
                wt_image exhi_gf_sex_3_4
                jasmine.c "Hmmm.  That wasn't exactly what I was thinking of, but your cock is ... pretty sexy."
                wt_image exhi_gf_sex_3_5
                jasmine.c "And while I'd rather have it in my pussy, I'm horny enough that the thought of having it my mouth is turning me on, too."
                wt_image exhi_gf_sex_3_16
                "Into her mouth it goes."
                wt_image exhi_gf_sex_3_6
                "She may be disappointed you wouldn't fuck her, but that doesn't stop her from giving you a loving and attentive blow job, her eyes locked on yours, watching the pleasure she's bringing you reflected in your face."
                $ title = "Where do you want to cum?"
                menu:
                    "On her":
                        wt_image exhi_gf_sex_3_17
                        player.c "Take my cock out of your mouth."
                        wt_image exhi_gf_sex_3_18
                        "She leans back, her outh still open as you aim your cock at her ..."
                        wt_image exhi_gf_sex_3_7
                        "... showering her with sperm as you cum."
                        player.c "[player.orgasm_text]"
                        wt_image exhi_gf_sex_3_8
                        jasmine.c "Mmmm.  I can see you were horny, too.  Only now you're satisfied, and I'm still horny."
                        wt_image exhi_gf_sex_3_19
                        jasmine.c "Just for that, I'm not going to let you watch while I frig myself, but I will tell you this  ..."
                        wt_image exhi_gf_sex_3_20
                        jasmine.c "...  I'm going to leave your cum on my face while I get myself of."
                        $ jasmine.facial_count += 1
                    "In her mouth":
                        wt_image exhi_gf_sex_3_9
                        player.c "[player.orgasm_text]"
                        "Wrapping her lips tightly around you, she pumps your shaft, milking every last drop from your balls and into her waiting mouth."
                        wt_image exhi_gf_sex_3_17
                        "As she finishes swallowing, she looks up at you, a twinkle in her eye."
                        wt_image exhi_gf_sex_3_10
                        jasmine.c "Mmmm.  Based on that mouthful, I'd say you were horny, too.  Only now you're satisfied, and I'm still horny."
                        wt_image exhi_gf_sex_3_21
                        jasmine.c "Just for that, I'm not going to let you watch while I frig myself, but I will tell you this  ...  I'm going to be thinking about your cock filling my mouth with cum while I get myself off."
                        $ jasmine.swallow_count += 1
                $ jasmine.blowjob_count += 1
                $ jasmine.maintain_week_gf += 1
                orgasm notify
            "No, but I'll lick you out":
                player.c "Horny are you?  Lie down and I'll look after you."
                wt_image exhi_gf_sex_3_24
                jasmine.c "Mmmmm.  I'm ready for your cock."
                wt_image exhi_gf_sex_3_25
                player.c "What about my mouth?  Are you ready for that instead?"
                jasmine.c "Oh!"
                wt_image exhi_gf_sex_3_26
                jasmine.c "oooo ... yes, that'll do nicely!"
                wt_image exhi_gf_sex_3_27
                player.c "Are you sure?  Because if my tongue's not enough, I could use my fingers, too."
                jasmine.c "ooooo ... yes!  yes, just like that!!"
                wt_image exhi_gf_sex_3_28
                "With your tongue teasing her clit, it only takes a few strokes of your fingers in and out of her slit to gther off."
                jasmine.c "ooooo  ...  oooohh!!"
                wt_image exhi_gf_sex_3_29
                jasmine.c "Wow!  That was amazing and ... fast."
                player.c "Did you want another round?"
                jasmine.c "No.  It's going to take all day just to recover from that one orgasm.  It scares me sometimes how easily you can push my buttons."
                $ jasmine.orgasm_count += 1
                if jasmine.maintain_week_gf < week + 3:
                    $ jasmine.maintain_week_gf = week + 3
                change player energy by -energy_short notify
            "Not today":
                player.c "Not today, [jasmine.name].  I have a lot to do."
                wt_image exhi_gf_sex_3_3
                jasmine.c "Ahhh, that's too bad.  I would have made it feel good for you, too."
                "She gives your cock a squeeze through you pants, then leaves you to your busy day."
        call forced_movement(living_room) from _call_forced_movement_601
    else:
        sys "There's been an error in the jasmine_girlfriend_events label."
    # randomize when next event will occur
    $ jasmine.random_number = renpy.random.randint(1, 10)
    if jasmine.random_number < 3:
        $ jasmine.relationship_week = week + 1
    elif jasmine.random_number < 6:
        $ jasmine.relationship_week = week + 2
    elif jasmine.random_number < 9:
        $ jasmine.relationship_week = week + 3
    else:
        $ jasmine.relationship_week = week + 4
    call character_location_return(jasmine) from _call_character_location_return_340
    return

# Transformation Potion Timer
label jasmine_transformation_potion_timer:
    if jasmine.has_tag('transformed'):
        "[jasmine.name] has already been transformed.  The potion can do nothing more to her."
    elif jasmine.has_tag('transformed_needs_location'):
        "[jasmine.name] has already been transformed.  You just need to find her a place where she can safely take her clothes off."
    elif jasmine.status == "on_training":
        "You shouldn't use this on Jasmine while she's still a client. Her husband knows she's with you and may become suspicious."
    else:
        $ jasmine.temporary_count = 1
        wt_image exhi_transformation_potion_1
        player.c "Here [jasmine.name].  I got you a drink."
        jasmine.c "Oh.  Thank you."
        wt_image exhi_transformation_potion_2
        "It only takes a moment for the potion to take effect. [jasmine.name]'s head slumps back and her mouth falls open as the potion opens her up to the potential for great changes."
        "You now need to spend some energy helping the potion realize a new potential for her."
        $ title = "What do you want her to become?"
        menu:
            "Showgirl" if not jasmine.has_tag('showgirl'):
                "[jasmine.name] has spent most of her adult life fantasizing about showing her body off to strangers. It's an easy step for the potion to make that the most important thing in her life."
                wt_image exhi_gf_conversation_2
                "She needs to be a stripper.  It's the only job that makes any sense to her."
                jasmine.c "Listen, there's something I've been meaning to ask you, and it's really, really important. Do you know anywhere I could get work as ... a stripper?"
                $ jasmine.training_session()
                if player.has_tag('club_first_visit_complete'):
                    player.c "I do.  Would you like me to get work for you there?"
                    wt_image exhi_gf_conversation_1
                    jasmine.c "Could you!  That would be my dream job!!"
                    player.c "I'll let them know to expect you."
                    $ jasmine.transformed_via_object = True
                    call jasmine_convert_showgirl from _call_jasmine_convert_showgirl_3
                else:
                    player.c "No, I don't."
                    jasmine.c "Oh.  If you find a place, could you tell me? I really, really need a new job, and strippings the only that really makes sense, you know?"
                    $ jasmine.stripper_discussion = 1
                    add tags 'waiting_for_club_access' 'transformed_needs_location' to jasmine
            "Bimbo":
                "Jasmine has spent much of her adult life thinking about what it would be like to show her body off to strangers. The potion latches on to those thoughts and amplifies them, until all other thoughts are pushed out of her mind."
                wt_image exhi_gf_conversation_1
                "Then it simplifies the thoughts, until the only thing left in Jasmine's head is the idea that she has a nice body and she should show it everyone.  You had better keep her and take care of her.  She's not likely to be able to take care of herself anymore."
                player.c "Come [jasmine.name], you will live with me now."
                jasmine.c "Okay"
                $ jasmine.training_session()
                $ jasmine.transformed_via_object = True
                call jasmine_convert_bimbo from _call_jasmine_convert_bimbo
            "Nothing (undo)":
                $ jasmine.temporary_count = 0
                "Let's pretend that didn't happen.  That's easier than reloading an old save."
        if jasmine.temporary_count == 1:
            $ jasmine.temporary_count = 0
            call character_location_return(jasmine) from _call_character_location_return_341
            rem 1 transformation_potion from player
            change player energy by -energy_long notify
    return

# Relationship Maintenance
label jasmine_relationship_maintenance:
    if jasmine.maintain_week_gf == week and not jasmine.has_tag('love_potion_threatened_to_leave'):
        wt_image exhi_gf_maintain_1
        jasmine.c "Can we talk for a minute? I'm not mad or anything. I knew coming into this that I wasn't going to be the only woman in your life, maybe not even the most important woman."
        if jasmine.has_tag('showgirl') and jasmine.has_tag('whore'):
            jasmine.c "And I get lots of attention from the dancing, and you know ... other things that you've encouraged me to do."
        elif jasmine.has_tag('showgirl'):
            jasmine.c "And I get lots of attention from the dancing at the Club."
        jasmine.c "But I'd like to have more of your attention. This not doing things with you for weeks at a time ... it makes me feel like I'm not really your girlfriend. And if I'm not that, then ... well, it feels like I'm just taking up space in your house for no reason."
    else:
        $ jasmine.temporary_count = jasmine.maintain_week_gf + 2
        if jasmine.temporary_count >= week:
            if jasmine.has_tag('love_potion_used'):
                add tags 'love_potion_threatened_to_leave' to jasmine
                wt_image exhi_gf_maintain_2
                "A naked Jasmine plunks herself down in front of you."
                jasmine.c "I want to apologize for my little speech the other week. I realized afterwards that I could never leave you.  You have some ... weird hold over me that I don't really understand."
                jasmine.c "But for whatever the reason, whenever I thought about leaving, I realized I couldn't bear the thought of not being near you."
                jasmine.c "So these titties of mine - and the rest of my body parts, too, for that matter - will be here and available for you to look at whenever you're in the mood, which I hope is soon."
            else:
                wt_image exhi_portrait_2
                jasmine.c "I wanted to say good bye before I left. No hard feelings, I hope? I'll always appreciate what you did for me, helping me to understand myself better and giving me the confidence to be true to myself."
                jasmine.c "I just can't stay here any more. I feel like I'm just taking up space. I love the attention of strangers, but I guess I also need a special guy in my life to pay attention to me, too."
                jasmine.c "Hopefully I'll see you at the Club sometime.  Or maybe downtown?  Bye!"
                rem tags 'continuing_actions' 'post_continuing_actions' from jasmine
                call unconvert(jasmine, 'girlfriend') from _call_unconvert_65
    return

########### ROOMS ###########
# Bedroom Enter Check
label jasmine_bedroom_enter:
  call character_location_return(jasmine) from _call_character_location_return_342
  if jasmine.fixed_location is not None:
    $ jasmine.change_image( 'exhi_gf_portrait' )
  return

# Bedroom Exit Check
label jasmine_bedroom_exit:
  if jasmine.has_tag('showgirl') and jasmine.downtown_event_checked_today < 2:
    $ jasmine.change_image( 'exhi_strip_1_1' )
    summon jasmine to stage no_follows
  return

# Club Whore Event
label jasmine_club_whore_event:
  summon gloria
  wt_image gloria.image
  gloria.c "Oh there you are!  Good, I've been hoping you'd drop by.  I have something I need to share with you."
  gloria.c "You know that little dancer you sent to us?  Well, I saw her the other day, and you won't believe what she was up to!"
  wt_image exhi_whore_4_2
  gloria.c "{i}I was just finishing some shopping and taking a short cut back home through one of the less savory neighborhoods when I saw her, standing on a street making eyes at all the passing cars.{/i}"
  wt_image exhi_whore_4_4
  gloria.c "{i}Then a car pulled over, and she did more than just make eye contact with him.{/i}"
  wt_image exhi_whore_4_3
  gloria.c "{i}He drove away ... I have no idea why!  But as soon as he left I pulled over to get to the bottom of things.{/i}"
  summon jasmine
  wt_image exhi_whore_7_1
  gloria.c "Jasmine!  Jasmine, it's me Gloria, from the Club."
  jasmine.c "Uh ... hi, Gloria."
  gloria.c "Are you turning tricks?"
  jasmine.c "What?  No!"
  gloria.c "Yes, you are!  You're walking the streets like a common whore.  Are you in trouble?  Do you need money?"
  jasmine.c "No!  No, it's not like that."
  gloria.c "Oh sweetie, I've known lots of whores.  You don't have to lie to me.  I just never knew you were available on pay for access.  You are, aren't you?  That's what you're doing out here."
  gloria.c "{i}She just shrugged.{/i}"
  gloria.c "Well, come with me.  I want to hire you for an hour."
  wt_image exhi_whore_7_2
  jasmine.c "What??  No!"
  gloria.c "Oh sweetie, not for me!  For my husband.  It's been a while since I brought a paid tramp home to him.  He loves your show!  He'll be so surprised when he finds out you'll spread your legs on payment."
  jasmine.c "Still no!!"
  wt_image exhi_whore_7_3
  gloria.c "Listen, you little tart.  I don't know what your game is, but if my money's no good with you, then I'm going to have to have a talk with my husband about letting you up on our stage."
  gloria.c "You've seen my husband.  He's a good looking man.  Lots of girls enjoy sucking his cock.  A whore like you shouldn't have any problem doing so."
  gloria.c "That's what you want, isn't it?  To be treated like a whore?  You said you weren't doing this because you're in money trouble, so I assume this is just what you are."
  gloria.c "So what's it going to be, whore?  Am I telling my husband that you're his paid slut for the evening, or that one of his showgirls is a whore who thinks she's too good for to suck his cock for money?"
  wt_image exhi_whore_7_4
  gloria.c "{i}She didn't answer, but when I handed over my money, she took it.{/i}"
  gloria.c "Come on, my car's right here.  Oh, this is going to be so much fun!"
  wt_image exhi_whore_7_6
  gloria.c "Honey!  Come see who I've brought home for you!"
  club_president.c "Jasmine?  This is a surprise."
  gloria.c "Oh, it gets better.  I found Jasmine walking the streets, picking up johns."
  club_president.c "Seriously?"
  gloria.c "Seriously.  What's your street name, sweetie?"
  jasmine.c "Jiggles"
  gloria.c "Jiggles!!  Oh that is so perfect!  Jiggles, bend over and let my husband take a look at your ass."
  club_president.c "Nice!  This is a great gift, Gloria.  Thanks for picking her up for me."
  wt_image exhi_whore_7_5
  gloria.c "I remembered how much you liked watching her dance.  When I found out she was a whore, I figured you'd like to a chance to fuck her.  What hole do you want to use first?"
  club_president.c "Wow, I don't know.  She has a nice cock sucker's mouth, but this ass is so soft, I think I want to fuck her from behind to start."
  wt_image exhi_whore_7_7
  gloria.c "{i}I got him hard with my mouth, which didn't take long.{/i}"
  wt_image exhi_whore_7_8
  gloria.c "{i}I didn't have to do anything to get Jiggles ready.  The little tramp was already sopping wet as I put my husband's dick inside her ...{/i}"
  wt_image exhi_whore_7_9
  gloria.c "{i}... and she started moaning as soon as he began to fuck her.{/i}"
  jasmine.c "ooooo"
  wt_image exhi_whore_7_10
  gloria.c "{i}My husband's pretty good with his dick, but even I was surprised by how quickly he got her to cum.{/i}"
  jasmine.c "ooooo  ...  oooohh!!"
  wt_image exhi_whore_7_11
  gloria.c "{i}When the little whore stopped shaking, my husband turned her around and lifted her onto him ...{/i}"
  wt_image exhi_whore_7_12
  gloria.c "{i}... where she started bouncing up and down on his cock.{/i}"
  gloria.c "Oh, honey!  I love watching you make the whores cum.  Could you save some of that hard on for me?"
  club_president.c "Of course, Gloria."
  wt_image exhi_whore_7_13
  club_president.c "Jasmine ... sorry, Jiggles ... could you get my wife ready to be fucked?"
  jasmine.c "I don't do women."
  gloria.c "Don't be ridiculous, you fucking whore.  You took my money, you'll do anybody my husband tells you to, including me."
  wt_image exhi_whore_7_14
  gloria.c "{i}She didn't like it, but she did as she was told, and put her tongue between my legs.{/i}"
  wt_image exhi_whore_7_15
  gloria.c "{i}I must admit, I kept her there far longer than I needed to.  I was already wet from watching my husband fuck her, and didn't really need any help getting ready for my husband's cock.{/i}"
  wt_image exhi_whore_7_14
  gloria.c "{i}But I hate attitude from the paid help, and hearing her talk back to my husband made me determined to keep her tongue on me for as long as I could until the need for my husband's dick grew too intense.{/i}"
  wt_image exhi_whore_7_16
  club_president.c "Let me taste my wife's juices on you ... mmmm, that's nice.  Gloria loves having her nipples sucked wile she's getting fucked.  Why don't you do that?"
  wt_image exhi_whore_7_17
  gloria.c "{i}This time the whore had the good sense not to talk back.  She licked my nipples hard ...{/i}"
  wt_image exhi_whore_7_18
  gloria.c "{i}... then started sucking them.  Between her mouth and my husband's hard dick working its way in and out of me, I was soon cumming like a fountain.{/i}"
  gloria.c "Oohhhh!!!   OOHHHHH!!!!    OHHH  YEESSSSSS!!!!"
  wt_image exhi_whore_7_19
  gloria.c "{i}My dear husband had been so patient.  I couldn't keep him waiting any longer.  I took out his cock and pumped his jizz out over the whore's face.{/i}"
  wt_image gloria.image
  gloria.c "Suffice to say, my husband was pleased with Jiggles' work.  But we have a problem."
  gloria.c "We can't have common whores in our Club.  It sends the wrong message, not to mention lowers the exclusiveness and prestige of our operation."
  gloria.c "If she wants to keep dancing here, she's going to have to give up whoring.  I'm sure you understand."
  player.c "I'll talk to her."
  call character_location_return(gloria) from _call_character_location_return_343
  wt_image jasmine.image
  "You find Jasmine/Jiggles near the stage."
  player.c "We have a problem.  I understand you Gloria picked you up."
  jasmine.c "Yeah.  I didn't want to go with her, but she paid me, and ..."
  player.c "It wouldn't have mattered.  Might have been worse if you'd refused her."
  $ jasmine.club_whore_event_week = 0
  $ title = "What do you tell her?"
  menu:
    "She has to give up dancing":
      player.c "You're going to have to give up your show."
      wt_image exhi_strip_1_7
      jasmine.c "No!!!   No, please!!  Don't make me do that!!!  I can't ... I can't image life again without access to the stage."
      jasmine.c "Please, if I promise to give up whoring, I'm sure Gloria will let me keep performing my show."
      player.c "Wouldn't you miss the whoring?"
      jasmine.c "A little, but not like I'd miss taking my clothes off for the public.  Please???  Please can't I keep my shows?"
      $ title = "What do you tell her?"
      menu:
        "Whoring is more important":
          player.c "Whoring is more important.  If your show's getting in the way of that, your show has to go."
          jasmine.c "No!  Please???"
          player.c "Keep it up and I'll make you give up your husband and job, too."
          jasmine.c "No!!!  No, don't do that.  I'm sorry, it's just ... I love it here."
          player.c "Maybe, but you belong on the street.  Now you'll have more time to spend there.  Not having a stage to show your whore tits off on might be good for you.  You should be more desperate to show them off to prospective customers, now, and a desperate whore gets lots of attention."
          "She can tell you won't be swayed.  Sobbing, she goes and clears out her locker.  Jasmine's showgirl days are over, but Jiggles' street walking days will continue."
          $ jasmine.change_full_name("", "Jiggles", "the Street Walking Whore")
          $ jasmine.change_image( 'exhi_whore_4_1' )
          $ jasmine.description = "She thought she just wanted to be an exhibitionist.  You helped her find her true calling as an available to anyone street walker."
          call unconvert(jasmine, 'showgirl') from _call_unconvert_66
        "She can keep her show":
          player.c "Okay, fine.  If it means that much to you, you can keep your show.  I'll tell Gloria you're going to give up the whoring."
          wt_image exhi_strip_1_8
          jasmine.c "Oh, thank you!!  Thank you!!!  I'll come over and be your private whore anytime you ask me. "
          "She gives you a big hug before running off."
          if not jasmine.has_tag('continuing_actions'):
            add tags 'continuing_actions' to jasmine
          $ jasmine.change_status("post_training")
          $ jasmine.whore_play_status = 10
          $ jasmine.description = "When she came to you, Jasmine had no safe outlet for her exhibitionist urges.  Now she's a happy and popular show girl at the most exclusive Club in town."
          call unconvert(jasmine, 'whore') from _call_unconvert_67
    "She has to give up whoring":
      player.c "You're going to have to give up the whoring."
      jasmine.c "But, will I be able to keep doing my show?"
      player.c "Yes, as long as you stop street walking, she said you can keep your show."
      wt_image exhi_strip_1_8
      jasmine.c "Oh, thank goodness.  I need to go find her and thank her.  I'll still come over and be your private whore anytime you ask me.  As long as you don't pay me, I'm sure Glora won't mind."
      "She gives you a big hug before running off."
      if not jasmine.has_tag('continuing_actions'):
        add tags 'continuing_actions' to jasmine
      $ jasmine.change_status("post_training")
      $ jasmine.whore_play_status = 10
      $ jasmine.description = "When she came to you, Jasmine had no safe outlet for her exhibitionist urges.  Now she's a happy and popular show girl at the most exclusive Club in town."
      call unconvert(jasmine, 'whore') from _call_unconvert_68
  call character_location_return(jasmine) from _call_character_location_return_344
  return

# Dungeon, Prevent from Entering
label du_no_access_jasmine:
  if jasmine in living_room.people:
    jasmine.c "Okay, it kinda freaks me out that you even have a dungeon. I'm not into whips and chains and that shit, and I'm not going in there with you."
    break_movement
  return

## replaced by newer club summons process
# # Stage Events
# label jasmine_stage_events:
#   ## Exhi Swinger Not Thanked?
#   if jasmine.location == stage and jasmine.stripper_discussion == 3:
#     call jasmine_update_media
#     wt_image jasmine.image
#     "As you approach the stage, you see [jasmine.name]. She spots you and approaches."
#     jasmine.c "Hi!  This place is amazing!!  Thank you so much for setting this up."
#     jasmine.c "I hope you'll stay and watch.  I'm about to start a show."
#     $ jasmine.stripper_discussion = 4
#   return

# Downtown Events
label jasmine_downtown_events:
    if jasmine.downtown_week < week and jasmine.downtown_week > 0 and jasmine.has_tag('satisfied') and not jasmine.has_tag("bimbo") and jasmine.downtown_event_checked_today == 0 and jasmine.downtown_countdown < 1:
        summon jasmine
        $ jasmine.random_number = renpy.random.randint(1, 10)
        if jasmine.random_number < 3:
            $ jasmine.downtown_countdown = 0
        elif jasmine.random_number < 5:
            $ jasmine.downtown_countdown = 1
        elif jasmine.random_number < 8:
            $ jasmine.downtown_countdown = 2
        elif jasmine.random_number < 10:
            $ jasmine.downtown_countdown = 3
        else:
            $ jasmine.downtown_countdown = 4
        $ jasmine.downtown_event_checked_today = 2
        # whore events take precedence
        if jasmine.has_tag('whore'):
            $ jasmine.whore_outfit += 1
            # scroll from 1 to 6
            if jasmine.whore_outfit > 6:
                $ jasmine.whore_outfit = 1
            # set photo for subsequent events
            if jasmine.whore_outfit == 1 or jasmine.whore_outfit == 3 or jasmine.whore_outfit == 5:
                wt_image exhi_whore_5_21
                "You spot Jiggles peddling her wares in a quiet alley downtown."
            elif jasmine.whore_outfit == 2:
                wt_image exhi_whore_4_2
                "You spot Jiggles downtown, smiling at every passing car with only a lone man in it."
            elif jasmine.whore_outfit == 4 or jasmine.whore_outfit == 6:
                wt_image exhi_whore_6_10
                "You spot Jiggles walking near the park."
            else:
                sys "There's been an error in the label jasmine_downtown_events."
            $ title = "Check on your whore?"
            menu:
                "Yes":
                    $ jasmine.downtown_week = week
                    if jasmine.whore_outfit == 1:
                        wt_image exhi_whore_5_1
                        "She seems to be having trouble drumming up interest."
                        wt_image exhi_whore_5_3
                        "Eventually she decides to make her assets more easily available for inspection."
                        wt_image exhi_whore_5_4
                        "That seems to work, as before too long a man approaches. She talks to him for a couple of minutes, then leads him down the alley. You follow at a discrete distance."
                        wt_image exhi_whore_5_22
                        "When you turn the corner, she's already straddling the john."
                        wt_image exhi_whore_5_5
                        "She smiles when she sees you and turns around ..."
                        wt_image exhi_whore_5_6
                        "... blocking his view of you, while giving you a perfect view of her."
                        wt_image exhi_whore_5_7
                        "You're not sure if she would have cum without an audience ..."
                        jasmine.c "ooooo"
                        wt_image exhi_whore_5_23
                        "... but she certainly does with one."
                        jasmine.c "oooohh!!"
                        wt_image exhi_whore_5_8
                        "Jiggles seems to be adjusting well to life on the street. You leave her to finish up with her john."
                    elif jasmine.whore_outfit == 2:
                        wt_image exhi_whore_4_3
                        "You follow her down the street ..."
                        wt_image exhi_whore_4_4
                        "... until a car pulls over and she stops to chat. You think she flashes her tits to the driver, but you can't tell for sure from your angle. Not that the view is bad from here."
                        wt_image exhi_whore_4_5
                        "When she gets in the car, you step closer to get a better look. He can't see you from where you're standing, but she does."
                        wt_image exhi_whore_4_6
                        "She looks up at you as she licks his dick ..."
                        wt_image exhi_whore_4_7
                        "... then gets to work."
                        wt_image exhi_whore_4_8
                        "She looks up at you again as her john fills her mouth with cum, as if to say 'see what a dirty whore I am?'."
                        "You leave her to finish up before he spots you lurking."
                    elif jasmine.whore_outfit == 3:
                        wt_image exhi_whore_5_9
                        "A man approaches Jiggles almost at the same time you stop to watch her."
                        wt_image exhi_whore_5_10
                        "She leads him down the alley ..."
                        wt_image exhi_whore_5_11
                        "... to a small park, where he wastes no time bending her over."
                        wt_image exhi_whore_5_12
                        "You maintain a discrete distance while the john fucks her."
                        wt_image exhi_whore_5_13
                        "You're too far away to tell if you watching her whore herself out is getting her off ..."
                        wt_image exhi_whore_5_14
                        "... but you're pretty sure it is. Her john, of course, thinks her excitement is just from his masterful dick-work, and he soon cums, too.  You beat a hasty retreat, before he sees you."
                    elif jasmine.whore_outfit == 4:
                        wt_image exhi_whore_6_1
                        "You follow her as she enters the park."
                        wt_image exhi_whore_6_11
                        "She finds a secluded spot close to the path ..."
                        wt_image exhi_whore_6_2
                        "... and removes her top."
                        wt_image exhi_whore_6_3
                        "Before long, a man comes along to take a closer look.  She leads him deeper into the park."
                        wt_image exhi_whore_6_12
                        "It takes you a while to navigate through the trees and figure out where she's gone."
                        wt_image exhi_whore_6_4
                        "By the time you spot her, kneeling between some dense bushes, her mouth is already full of cock. You can't see very much, but you find a spot that at least gives you a view through the branches of her face ..."
                        wt_image exhi_whore_6_5
                        "... just as she receives a mouthful of sperm.  She seems to have things under control, so you leave her to finish up with her john."
                    elif jasmine.whore_outfit == 5:
                        wt_image exhi_whore_5_2
                        "Jiggles seems impatient today.  Perhaps she's been waiting a long time, with no customers."
                        wt_image exhi_whore_5_15
                        "After a while, she loses her top ..."
                        wt_image exhi_whore_5_24
                        "... and starts strutting back and forth, more and more brazenly, seeking attention."
                        wt_image exhi_whore_5_25
                        "Finally a man stops to chat with her."
                        wt_image exhi_whore_5_16
                        "After a few minutes, she takes him down the alley ..."
                        wt_image exhi_whore_5_17
                        "... to the small park, where she starts sucking him off."
                        wt_image exhi_whore_5_18
                        "You keep your distance, but she spots you anyway, as she keeps looking around as she sucks him, checking to see if anybody is watching her fuck a stranger in public for money."
                        wt_image exhi_whore_5_19
                        "When she realizes she has an audience, she starts licking and sucking him with greater enthusiasm, giving you a good angle of view so you can watch everything she's doing."
                        wt_image exhi_whore_5_26
                        "The john seems oblivious to the show she's giving you, not that you can blame him. It'd be hard to notice anything else with an eager minx of a whore worshiping your cock with gusto."
                        wt_image exhi_whore_5_20
                        "Her efforts soon reward Jiggles with a mouthful of cum.  She locks eyes on you as he climaxes, making a show of noisily swallowing every spurt.  You slip away while the john recovers."
                    elif jasmine.whore_outfit == 6:
                        wt_image exhi_whore_6_3
                        "Jiggles is either in a rush, or in need of feeling totally and humiliatingly exposed today. As soon as she reaches a secluded part of the park,  She strips off all her clothes as she walks into the park, putting everything she has on display for passers by."
                        wt_image exhi_whore_6_6
                        "She makes  no effort to hide herself as a pair of women, followed by a couple walking a dog, pass by.  Instead, she drops a hand between her legs and opens herself up for even greater exposure."
                        wt_image exhi_whore_6_13
                        "From the glistening between her labia, you suspect the first stranger who stops and stares at her is going to trigger a climax."
                        wt_image exhi_whore_6_7
                        "You begin to worry about whether someone may call security on her, when a man approaches. You can't hear what he says to her, but you can lipread her response, 'absolutely'."
                        wt_image exhi_whore_6_12
                        "You hurry to catch up as Jiggles leads her john deeper into the park."
                        wt_image exhi_whore_6_9
                        "You find her hidden in the same secluded bushes as before, this time with a cock buried inside her."
                        wt_image exhi_whore_6_8
                        "You're not sure if she knows you're there or not, as you can't get a good look at her face. What you can see, through a gap in the branches, though, is enough to tell you that's she's going to cum, whether she knows she's being watched or not. A fact verified by the sounds of her moans through the bushes a moment later."
                        jasmine.c "oooohh!!"
                        wt_image exhi_whore_6_14
                        "There's a rustling in the bushes as the john flips her over onto her knees and finishes himself off by fucking her from behind.  Afterwards, you leave while her john is pulling his pants back up."
                    $ jasmine.whore_lost_countdown = 5
                    change player energy by -energy_very_short
                "Not today":
                    pass
                "Not this week":
                    $ jasmine.downtown_week = week
                "Never":
                    $ title = "Really stop any future encounters with Jasmine outside?"
                    menu:
                        "Yes, don't report future sightings":
                            $ jasmine.downtown_week = 0
                        "No, I've reconsidered":
                            pass
        # otherwise flashing events
        else:
            # set initial photo and subsequent set
            if jasmine.downtown_follow_count < 2:
                wt_image exhi_downtown_1_1
                "You spot [jasmine.name] downtown."
            else:
                $ jasmine.downtown_outfit += 1
                # scroll from 1 to 4
                if jasmine.downtown_outfit > 4:
                    $ jasmine.downtown_outfit = 1
                # if not streetwalking roleplay, skip 3
                if jasmine.downtown_outfit == 3 and jasmine.whore_play_status != 6:
                    $ jasmine.downtown_outfit = 4
                if jasmine.downtown_outfit == 1:
                    wt_image exhi_downtown_2_1
                    "You spot [jasmine.name] downtown, just entering a park."
                elif jasmine.downtown_outfit == 2 or jasmine.downtown_outfit == 4:
                    wt_image exhi_downtown_2_1
                    "You spot [jasmine.name] downtown, just entering a park."
                elif jasmine.downtown_outfit == 3:
                    wt_image exhi_whore_4_2
                    "You spot 'Jiggles' downtown, smiling at every passing car with only a lone man in it."
                else:
                    sys "There's been an error in the label jasmine_downtown_events."
            $ title = "Follow her?"
            menu:
                "Yes":
                    $ jasmine.downtown_week = week
                    $ jasmine.downtown_follow_count += 1
                    if jasmine.downtown_follow_count == 1:
                        wt_image exhi_downtown_1_15
                        "When she sees you, she looks like she's about to say hello ..."
                        wt_image exhi_downtown_1_2
                        "... then thinks better of it, and keeps going, looking behind to see if you're following her."
                        wt_image exhi_downtown_1_4
                        "You follow her around to the back of a building ..."
                        wt_image exhi_downtown_1_5
                        "... where she pulls down her pants ..."
                        wt_image exhi_downtown_1_6
                        "... hesitates a moment ..."
                        wt_image exhi_downtown_1_7
                        "... then pulls down her top with a mischievous grin."
                        wt_image exhi_downtown_1_8
                        "Before you can approach her, she pulls her clothes together and flees up a nearby stairs, turning to flash you a big smile as she goes."
                    elif jasmine.downtown_follow_count == 2:
                        wt_image exhi_downtown_1_9
                        "[jasmine.name] takes a quick look over her shoulder to check if you're following her."
                        wt_image exhi_downtown_1_3
                        "When she sees that you are, she walks out across a parking lot ..."
                        wt_image exhi_downtown_1_10
                        "... then turns ..."
                        wt_image exhi_downtown_1_11
                        "... and flashes her tits at you as a car drives by."
                        wt_image exhi_downtown_1_12
                        "She covers herself up and darts into a store before you can approach her, shooting you a big grin as she goes."
                    else:
                        if jasmine.downtown_outfit == 1:
                            wt_image exhi_downtown_2_2
                            "She grins when she sees you're following her, and leads you towards a wooded area of the park."
                            wt_image exhi_downtown_2_3
                            "There she turns and lets the dress slip off of her."
                            wt_image exhi_downtown_2_4
                            "Naked, she walks further into the park ..."
                            wt_image exhi_downtown_2_5
                            "... making sure you get a good look at her on her stroll."
                            $ title = "What do you do?"
                            menu:
                                "Take out your cock" if jasmine.downtown_sex == 0:
                                    $ jasmine.downtown_sex = 1
                                    wt_image exhi_downtown_2_7
                                    "[jasmine.name] looks at you uncertainly as you take out your cock."
                                    "You can see her debating ..."
                                    wt_image exhi_downtown_2_4
                                    "... then she turns and flees the park before you can catch up to her again."
                                "Take your cock out again" if jasmine.downtown_sex == 1:
                                    wt_image exhi_downtown_2_7
                                    "[jasmine.name] looks at you uncertainly as you take out your cock ..."
                                    if jasmine.has_tag('girlfriend') or jasmine.has_tag('continuing_actions'):
                                        $ jasmine.downtown_sex = 2
                                        wt_image exhi_downtown_2_8
                                        "... then she steps closer."
                                        jasmine.c "Someone might see you."
                                        player.c "Not if you deal with this first."
                                        jasmine.c "Then they'd see ..."
                                        player.c "You, sucking my cock.  Do you like the idea of that?"
                                        jasmine.c "I don't know."
                                        player.c "Get on your knees and let's find out."
                                        wt_image exhi_downtown_2_9
                                        "She kneels down and looks around as she licks the head of your cock."
                                        player.c "Anybody here?"
                                        jasmine.c "No"
                                        player.c "Don't worry.  Someone may come before I do."
                                        wt_image exhi_downtown_2_10
                                        "Clearly excited at the risk she's taking, she sucks your cock with abandon, all the time looking around to see if you're being observed."
                                        "It's one of her better cocksucking efforts, and you soon show your appreciation by emptying a load of jizz in her mouth."
                                        player.c "[player.orgasm_text]"
                                        wt_image exhi_downtown_2_11
                                        player.c "Did anyone see us?"
                                        jasmine.c "Nope"
                                        player.c "Disappointed?"
                                        jasmine.c "I ... Wow, I think maybe I am disappointed?  What have you done to me?"
                                        player.c "I haven't done anything to you.  Just helped you to understand your true nature."
                                        jasmine.c "That I like to suck cock in public?"
                                        player.c "You do, don't you?"
                                        if jasmine.has_tag('girlfriend'):
                                            jasmine.c "I guess so. You amaze me sometimes, the way you seem to understand my kinks better than I do."
                                            if jasmine.maintain_week_gf < week + 3:
                                                $ jasmine.maintain_week_gf = week + 3
                                        else:
                                            jasmine.c "I guess so. You scare me sometimes, the way you seem to understand my kinks better than I do. And way better than my husband does, that's for sure."
                                            $ jasmine.gf_conversion_status += 1
                                        $ jasmine.blowjob_count += 1
                                        $ jasmine.swallow_count += 1
                                        orgasm notify
                                    else:
                                        wt_image exhi_downtown_2_4
                                        "... then she turns and flees the park before you can catch up to her again."
                                        "In her fantasies, she's the one naked, not her observers, and while she appreciates the confirmation of how excited her show is making you, her relationship with you is not one where she's going to do anything about your excitement."
                                "Have her blow you" if jasmine.downtown_sex > 1:
                                    wt_image exhi_downtown_2_8
                                    "She steps closer as she sees you take your cock out."
                                    jasmine.c "Again?"
                                    player.c "Absolutely.  This time maybe we'll have an audience."
                                    wt_image exhi_downtown_2_9
                                    "She kneels down and licks your cock as she looks around."
                                    player.c "See anyone?"
                                    jasmine.c "Not yet, but I hear somebody on the next path over."
                                    player.c "Maybe you should make this a noisy sloppy blow job, and they'll come over to see what type of wild animal's making that noise?"
                                    wt_image exhi_downtown_2_10
                                    "She stifles a laugh and starts sucking you properly.  It may be your imagination, but it seems like she is making this a noisier, sloppier blow job than usual."
                                    "It's also a damn good one, and she soon coaxes your seed out of your balls and into her waiting mouth."
                                    player.c "[player.orgasm_text]"
                                    wt_image exhi_downtown_2_11
                                    player.c "Did anyone see us?"
                                    jasmine.c "I'm not telling."
                                    if jasmine.has_tag('girlfriend'):
                                        if jasmine.maintain_week_gf < week + 2:
                                            $ jasmine.maintain_week_gf = week + 2
                                    $ jasmine.blowjob_count += 1
                                    $ jasmine.swallow_count += 1
                                    orgasm notify
                                "Pleasure her" if jasmine.downtown_sex > 1:
                                    wt_image exhi_downtown_2_8
                                    "She smiles as she sees you approach."
                                    jasmine.c "Are you in need of relief again?"
                                    player.c "Not today. Today I'm going to offer you some relief. I bet you're all worked up from strutting around here naked."
                                    wt_image exhi_downtown_2_12
                                    jasmine.c "Oh!"
                                    "She gasps and looks around as you lick her immediately erect nipple."
                                    player.c "I'll take that as a yes.  Turn around."
                                    wt_image exhi_downtown_2_13
                                    "She leans against the path rail, her head on a swivel, checking to see if anybody is near as you spread her legs and lick her already dripping snatch."
                                    wt_image exhi_downtown_2_14
                                    "Walking naked through the park had her turned on before you even touched her. Having you lick her pussy in public where anyone could walk by and see has her over the edge in no time."
                                    "She floods your mouth with her juices as she calls out, seemingly not even trying to stifle her moans of pleasure."
                                    jasmine.c "ooooo  ...  oooooo  ...  oooohh!!"
                                    wt_image exhi_downtown_2_11
                                    player.c "Did anyone see us?"
                                    jasmine.c "I'm not telling."
                                    $ jasmine.orgasm_count += 1
                                    if jasmine.has_tag('girlfriend'):
                                        if jasmine.maintain_week_gf < week + 3:
                                            $ jasmine.maintain_week_gf = week + 3
                                    change player energy by -energy_short
                                "Just watch her":
                                    wt_image exhi_downtown_2_4
                                    "You're enjoying the show, and she gives you a nice one as she makes a circuit of the park ..."
                                    wt_image exhi_downtown_2_6
                                    "... and gives you a big smile before putting her dress back on and leaving."
                                    if jasmine.has_tag('girlfriend'):
                                        if jasmine.maintain_week_gf < week + 2:
                                            $ jasmine.maintain_week_gf = week + 2
                                "Leave":
                                    wt_image downtown.image
                                    "You leave [jasmine.name] to her public exhibitionism and get back to your day."
                        elif jasmine.downtown_outfit == 2 or jasmine.downtown_outfit == 4:
                            $ jasmine.downtown_flash_outfit += 1
                            # scroll from 1 to 3:
                            if jasmine.downtown_flash_outfit > 3:
                                $ jasmine.downtown_flash_outfit = 1
                            if jasmine.downtown_flash_outfit == 1:
                                wt_image exhi_downtown_1_3
                                "You don't have to follow Jasmine too far ..."
                                wt_image exhi_downtown_1_13
                                "... before she turns and gives you a good view of her tits before covering up and hurrying on her way."
                            elif jasmine.downtown_flash_outfit == 2:
                                wt_image exhi_downtown_1_9
                                "You don't have to follow Jasmine too far ..."
                                wt_image exhi_downtown_1_14
                                "... before she turns and gives you a good view of her tits before covering up and hurrying on her way."
                            elif jasmine.downtown_flash_outfit == 3:
                                wt_image exhi_downtown_1_4
                                "You don't have to follow Jasmine too far ..."
                                wt_image exhi_downtown_1_11
                                "... before she turns and gives you a good view of her tits before covering up and hurrying on her way."
                            if jasmine.has_tag('girlfriend'):
                                $ jasmine.maintain_week_gf += 1
                        elif jasmine.downtown_outfit == 3:
                            wt_image exhi_whore_4_3
                            "You follow her down the street ..."
                            wt_image exhi_whore_4_4
                            "... until a car pulls over and she stops to chat. You think she flashes her tits to the driver, but you can't tell for sure from your angle. Not that the view is bad from here."
                            wt_image exhi_whore_4_5
                            "When she gets in the car, you step closer to get a better look. He can't see you from where you're standing, but she does."
                            wt_image exhi_whore_4_6
                            "She looks up at you as she licks his dick ..."
                            wt_image exhi_whore_4_7
                            "... then gets to work."
                            wt_image exhi_whore_4_8
                            "She looks up at you again as her john fills her mouth with cum, as if to say 'see what a dirty whore I am?'."
                            "You leave her to finish up before he spots you lurking."
                            if jasmine.has_tag('girlfriend'):
                                if jasmine.maintain_week_gf < week + 2:
                                    $ jasmine.maintain_week_gf = week + 2
                "Not today":
                    pass
                "Not this week":
                    $ jasmine.downtown_week = week
                "Never":
                    $ title = "Really stop any future encounters with Jasmine outside?"
                    menu:
                        "Yes, don't report future sightings":
                            $ jasmine.downtown_week = 0
                        "No, I've reconsidered":
                            pass
        call character_location_return(jasmine) from _call_character_location_return_345
        wt_image current_location.image
    elif jasmine.downtown_event_checked_today == 0:
        $ jasmine.downtown_event_checked_today = 1
        $ jasmine.downtown_countdown -= 1
    return

################################### NOTES ###################################
##################### TODO #####################
## FIGURE OUT HOW TO DO THE MATH BEHIND LOSING SHOWGIRLS WHORES AND GFS  #####################################
## CHANGE ALL COUNTS LINES PREFERABLE WITH UNCONVERT COMMAND #################################################

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
