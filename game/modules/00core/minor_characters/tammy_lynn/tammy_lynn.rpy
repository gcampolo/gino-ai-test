## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: wifetrainer

# Package Register
# register_package tammy_lynn; note, priority must be after Becky Sue's due to the way her name is set up
register tammy_lynn_pregame 15 in core as "Tammy-Lynn"

label tammy_lynn_pregame:
  python:
    ## Credits
    model_credits += [('support', "Tammy-Lynn, friend of Becky Sue (Riley Reid)")]

  ## Constants
    ## Character Definition
    # Red
    tammy_lynn = Person(Character("Becky Sue's Friend", who_color="#FF0000", what_color="#FF0000", window_background = gui.dialogue_background_medium_font_color), "tammy_lynn", cut_portrait = True, prefix = "", suffix = "", hypno_trigger_sessions_threshold = 7)

    # Other Characters
    # Pink
    coworker_tammy_lynn = Character("Co-worker", who_color="#FF0080", what_color="#FF0080")

    ## Actions
    # Living with you actions
    tammy_lynn.action_check_on_her = tammy_lynn.add_action("Check on her", label = "_check_on_her", condition = "tammy_lynn.can_be_interacted and tammy_lynn.has_tag('living_with_you') and tammy_lynn.in_area('house')")
    tammy_lynn.action_release_her = tammy_lynn.add_action("Release her", label = "_release_her", condition = "tammy_lynn.has_tag('posing_now') and tammy_lynn.in_area('house')")

    ## Tags
    # Common Character Tags
    tammy_lynn.add_tags('no_hypnosis', 'likes_becky_sue') # note:  Tammy-Lynn doesn't get either the "likes_boys" or "likes_girls" tags

    # Character Specific Tags
    # N/A

    ## Locations
    # Tammy Lynn's Room
    # Note: no connections to this room, those are added when she moves in
    tammy_lynn_room = Location("Tammy-Lynn's Room", 'tlr', cut_portrait = True, enter_break_labels = ['tlr_no_access'], enter_labels = ['tlr_enter'], exit_labels = ['tlr_exit'], area = 'house')

    ## Other
    tammy_lynn.change_status("minor_character")

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('tammy_lynn_start_day', priority = 10)

    ## Hypnosis
    tammy_lynn.trigger_phrase = "Bumming friends don't get to choose."
    # hypno_trigger_sessions_threshold sets when the _implant_trigger label runs
    tammy_lynn.hypno_trigger_sessions_threshold = 5
    # hypno actionss
    tammy_lynn.resistance_hypno_action = tammy_lynn.add_action("Resistance", label = "_resistance_hypnosis", context = "_hypnosis")
    tammy_lynn.exhibitionist_hypno_action = tammy_lynn.add_action("Exhibitionism", label = "_exhibitionism_hypnosis", context = "_hypnosis", condition = "not tammy_lynn.has_tag('hypno_re_exhibitionism') and not tammy_lynn.has_tag('exhibitionist_for_you') and tammy_lynn.caught_you_watching > 0")
    tammy_lynn.peeing_hypno_action = tammy_lynn.add_action("Peeing", label = "_peeing_hypnosis", context = "_hypnosis", condition = "tammy_lynn.has_tag('hypno_re_exhibitionism') and not tammy_lynn.has_tag('accepts_watersports') and not tammy_lynn.has_tag('hypno_re_peeing') and tammy_lynn.toilet_count > 1")
    tammy_lynn.pee_drinking_hypno_action = tammy_lynn.add_action("Drinking pee", label = "_pee_drinking_hypnosis", context = "_hypnosis", condition = "tammy_lynn.has_tag('accepts_watersports') and not tammy_lynn.has_tag('accepts_watersports') and not tammy_lynn.has_tag('peed_on_her') and not tammy_lynn.has_tag('hypno_re_pee_drinking')")
    tammy_lynn.naked_walk_hypno_action = tammy_lynn.add_action("Walking naked", label = "_naked_walk_hypnosis", context = "_hypnosis", condition = "tammy_lynn.has_tag('hypno_on_walk') and tammy_lynn.has_tag('hypno_re_exhibitionism')")


    ########### VARIABLES ###########
    # Common Character Variables
    tammy_lynn.add_stats_with_value('hypno_anal_count', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_swallow_count', 'hypno_sex_count', 'event_week', 'random_number')

    # Character Specific Variables
    tammy_lynn.add_stats_with_value('caught_you_watching', 'check_outfit', 'event_outfit', 'food_outfit', 'kitchen_outfit', 'pee_outfit', 'phone_outfit', 'toilet_count', 'watched_her_do_yoga', 'weeks_with_you')
    tammy_lynn.add_stats_with_value('weekly_cost',value = 10)

    tammy_lynn.job = "job"
    tammy_lynn.your_respect_name = "Sir"

    ######## EXPANDABLE MENUS #######
    # check on her talk options
    tammy_lynn_check_on_her_options_menu = ExpandableMenu("What do you want?", cancelable = False)
    tammy_lynn.choice_check_on_her_settling_in = tammy_lynn_check_on_her_options_menu.add_choice("Ask if she has everything she needs", "tammy_lynn_check_on_her_settling_in", condition = "not tammy_lynn.has_tag('discussed_settling_in')")
    tammy_lynn.choice_check_on_her_hypnosis = tammy_lynn_check_on_her_options_menu.add_choice("Hypnotize her", "tammy_lynn_check_on_her_hypnosis", condition = "player.can_hypno(tammy_lynn)")
    ## action below added when moves in, to avoid problems with dynamic name for Becky Sue
    # tammy_lynn.choice_check_on_her_becky_sue = tammy_lynn_check_on_her_options_menu.add_choice("Talk about [becky_sue.name]", "tammy_lynn_check_on_her_becky_sue")
    tammy_lynn.choice_check_on_her_getting_work = tammy_lynn_check_on_her_options_menu.add_choice("Talk about her getting work", "tammy_lynn_check_on_her_getting_work", condition = "not tammy_lynn.has_tag('earning_keep')")
    tammy_lynn.choice_check_on_her_paying_rent = tammy_lynn_check_on_her_options_menu.add_choice("Talk about her paying her rent", "tammy_lynn_check_on_her_paying_rent", condition = "not tammy_lynn.has_tag('rent_conversation_off')")
    tammy_lynn.choice_check_on_her_threesomes = tammy_lynn_check_on_her_options_menu.add_choice("Tell her you expect her to start sleeping with you", "tammy_lynn_check_on_her_threesomes", condition = "becky_sue.has_tag('sleeping_with_friend') and not tammy_lynn.has_tag('accepts_threesomes')")
    tammy_lynn.choice_check_on_her_discuss_photos = tammy_lynn_check_on_her_options_menu.add_choice("Ask about her online photo posting", "tammy_lynn_check_on_her_discuss_photos", condition = "tammy_lynn.has_tag('caught_on_phone') and not tammy_lynn.has_tag('discussed_photos')")
    tammy_lynn.choice_check_on_her_discuss_work = tammy_lynn_check_on_her_options_menu.add_choice("Ask how her work is going", "tammy_lynn_check_on_her_discuss_work", condition = "tammy_lynn.has_tag('earning_keep')")
    tammy_lynn.choice_check_on_her_tied_bed = tammy_lynn_check_on_her_options_menu.add_choice("Tie her to the bed", "tammy_lynn_check_on_her_tied_bed", condition = "tammy_lynn.has_tag('sub_for_you')")
    tammy_lynn.choice_check_on_her_machine = tammy_lynn_check_on_her_options_menu.add_choice("Put her on the fuck machine", "tammy_lynn_check_on_her_machine", condition = "tammy_lynn.has_tag('sub_for_you') and dungeon.has_item(fuck_machine)")
    tammy_lynn.choice_check_on_her_suspension = tammy_lynn_check_on_her_options_menu.add_choice("Put her in suspension gear", "tammy_lynn_check_on_her_suspension", condition = "tammy_lynn.has_tag('sub_for_you') and dungeon.has_item(suspension_gear)")
    tammy_lynn.choice_check_on_her_trigger = tammy_lynn_check_on_her_options_menu.add_choice("Use her trigger", "tammy_lynn_trigger_used", condition = "tammy_lynn.has_tag('trigger_implanted')")

    # work options
    tammy_lynn_work_options_menu = ExpandableMenu("What type of work should she consider?", cancelable = False)
    tammy_lynn.choice_work_options_masseuse = tammy_lynn_work_options_menu.add_choice("Masseuse", "tammy_lynn_work_options_masseuse", condition = "becky_sue.has_tag('masseuse') and not tammy_lynn.has_tag('discussed_masseuse_job')")
    tammy_lynn.choice_work_options_studying = tammy_lynn_work_options_menu.add_choice("Go back to school", "tammy_lynn_work_options_studying", condition = "(becky_sue.has_tag('studying') or becky_sue.has_tag('graduated')) and not tammy_lynn.has_tag('discussed_studying')")
    tammy_lynn.choice_work_options_avalon = tammy_lynn_work_options_menu.add_choice("Avalon Lady", "tammy_lynn_work_options_avalon", condition = "not tammy_lynn.has_tag('discussed_avalon_job')")
    tammy_lynn.choice_work_options_pizza = tammy_lynn_work_options_menu.add_choice("Pizza Delivery", "tammy_lynn_work_options_pizza", condition = "tammy_lynn.has_tag('pizza_job_option_open')")
    tammy_lynn.choice_work_options_yoga = tammy_lynn_work_options_menu.add_choice("Yoga Instructor", "tammy_lynn_work_options_yoga", condition = "tammy_lynn.watched_her_do_yoga > 0")
    tammy_lynn.choice_work_options_retail = tammy_lynn_work_options_menu.add_choice("Retail", "tammy_lynn_work_options_retail", condition = "not tammy_lynn.has_tag('discussed_retail_job')")
    tammy_lynn.choice_work_options_maid = tammy_lynn_work_options_menu.add_choice("Maid", "tammy_lynn_work_options_maid", condition = "tammy_lynn.has_tag('watched_her_clean') and not tammy_lynn.has_tag('discussed_maid_job')")
    tammy_lynn.choice_work_options_bar = tammy_lynn_work_options_menu.add_choice("Bar Server", "tammy_lynn_work_options_bar")
    tammy_lynn.choice_work_options_nothing = tammy_lynn_work_options_menu.add_choice("Nothing right now", "tammy_lynn_work_options_nothing")


  return

# Display Portrait
# CHARACTER: Display Portrait
label tammy_lynn_update_media:
    if tammy_lynn.has_tag('posing_now'):
        pass
    elif tammy_lynn.has_tag('living_with_you'):
        $ tammy_lynn.change_image('ttf_initial_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label tammy_lynn_examine:
    if tammy_lynn.has_tag('living_with_you'):
        if tammy_lynn.has_tag('threesomes_with_you'):
            "[tammy_lynn.full_name] is [becky_sue.name]'s childhood friend.  She's also now yours and [becky_sue.name]'s lover."
        elif becky_sue.has_tag('sleeping_with_friend'):
            "[tammy_lynn.full_name] is [becky_sue.name]'s childhood friend.  She's also now [becky_sue.name]'s lover."
        elif tammy_lynn.has_tag('earning_keep'):
            "[tammy_lynn.full_name] is [becky_sue.name]'s childhood friend.  She's living with the two of you."
            call safe_call('tammy_lynn_description_' + tammy_lynn.job, override = 'tammy_lynn_description_job') from _call_safe_call_6
        else:
            "[tammy_lynn.full_name] is [becky_sue.name]'s childhood friend.  She's staying with the two of you while she figures out what she wants to do with her life."
    else:
        "[tammy_lynn.full_name] is [becky_sue.name]'s childhood friend."
    # NEED reactivate if content changed to allow her to receive gifts
    # $ items = ", ".join(i.name for i in tammy_lynn.get_items()) if tammy_lynn.get_items() != [] else ' Nothing'
    # "You have given her: [items]"
    if tammy_lynn.has_tag('trigger_implanted'):
        "You have implanted a hypnotic trigger in her."
    return

label tammy_lynn_description_job:
    "[tammy_lynn.name] is earning her keep, now, but the description of what she does hasn't been coded properly."
    return

label tammy_lynn_description_pizza:
    wt_image ttf_pizza_1_1
    "Thanks to your help, she has a job now, delivering pizza.  She doesn't make a lot of money, but it's enough that you no longer need to support her."
    return

label tammy_lynn_description_yoga:
    wt_image ttf_yoga_2_1
    "Thanks to your help, she has a job now, leading yoga classes.  Yoga purists don't think much of her 'drunken possum' or 'rusty Chevy' positions, but that's just water off a 'water-logged snake's back to [tammy_lynn.name].  She doesn't make a lot of money, but it's enough that you no longer need to support her."
    return

label tammy_lynn_description_bar:
    if tammy_lynn.has_tag('visited_her_at_bar'):
        wt_image ttf_bar_1_3
        "With your encouragement, she's taken a job as a server for an 'interesting' bar.  She drinks away most of her tips, but manages to bring home enough that you no longer need to support her."
    else:
        "With your encouragement, she's taken a job as a server for some bar you've never been to.  She drinks away most of her tips, but manages to bring home enough that you no longer need to support her."
    return

# Talk to Character
label tammy_lynn_talk:
    if tammy_lynn.has_tag('living_with_you'):
        "Check on her first."
    else:
        "You have nothing to talk to her about."
    return

label tammy_lynn_talk_job_job:
    "There's been an error.  The talk job label for [tammy_lynn.name]'s current job has not been properly defined."
    return

label tammy_lynn_talk_job_pizza:
    wt_image ttf_bedroom_1_28
    tammy_lynn.c "It's going great!!"
    wt_image ttf_pizza_1_2
    tammy_lynn.c "You know how the company has a promise where the pizza's there in 30 minutes or it's free?  Well, if I get it there in less than 20 minutes, I ask for a big tip!"
    player.c "Doesn't it take about 15 minutes for the pizza to be prepared and cooked?"
    wt_image ttf_pizza_1_3
    tammy_lynn.c "It does!  Which is why customers are always so surprised by my great driving, and willing to pay a tip!!"
    player.c "You must be making a fair bit of money, then."
    wt_image ttf_bedroom_1_11
    tammy_lynn.c "I would be, if it weren't for all the speeding tickets.  But as soon as I get better at avoiding the cops, I'll be raking in the big dough!"
    return

label tammy_lynn_talk_job_yoga:
    wt_image ttf_bedroom_1_28
    tammy_lynn.c "It's going great!!"
    wt_image ttf_yoga_2_2
    tammy_lynn.c "Some of the students tried to tell me that 'morning hangover' wasn't a real yoga pose, but whatever."
    wt_image ttf_yoga_2_3
    tammy_lynn.c "I'm not getting a lot of people out to my classes, but the ones who do come out watch me really closely.  I like to make a game of trying to catch them when they're staring at me, which is kinda fun!"
    player.c "I take it you're not making much money, then?"
    wt_image ttf_bedroom_1_6
    tammy_lynn.c "Not yet, but sometimes people come back for more than one class, so that's good sign, right?"
    return

label tammy_lynn_talk_job_bar:
    if tammy_lynn.has_tag('visited_her_at_bar'):
        wt_image ttf_bedroom_1_9
        tammy_lynn.c "It's going great!!  Lots of the guys say nice things about my uniform and I catch almost all of them admiring it.  I only had to punch out three guys for grabbing me last week, and all three of them ended up on the street on their asses after our bouncer threw them out!"
    else:
        wt_image ttf_bedroom_1_8
        tammy_lynn.c "It's going great!!  You should come visit me at work some weekend."
        if tammy_lynn.has_tag('no_visiting_her_at_bar'):
            $ title = "Consider a trip to her bar some weekend?"
            menu:
                "Yes (reactivate opportunity)":
                    rem tags 'no_visiting_her_at_bar' from tammy_lynn
                    player.c "Maybe one of these days."
                "No":
                    pass
        else:
            player.c "Maybe one of these days."
    return

# Hypno Actions
label tammy_lynn_hypnosis_start:
    if tammy_lynn.has_tag('hypno_in_bedroom_1'):
        wt_image ttf_bedroom_1_24
        player.c "I have something to show you, [tammy_lynn.name].  Take a look at this."
        call focus_image from _call_focus_image_87
        player.c "We're going to have a chat, [tammy_lynn.name].  I'm going to talk, and you're going to listen to me."
        player.c "Listen to me, [tammy_lynn.name]. Listen to my voice. Listen to my voice and nothing else, [tammy_lynn.name]. Only my voice. Only my voice now."
        wt_image ttf_bedroom_1_5
        "She soon falls under your trance."
        player.c "I want you to get comfortable for our talk.  You want me to be comfortable for our talk.  Bare your breasts, [tammy_lynn.name], so that we can both be comfortable and enjoy our talk."
        wt_image ttf_bedroom_1_25
        if tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.has_tag('exhibitionist_for_you'):
            "That would suffice, but hypnotized [tammy_lynn.name] seems intent on giving you a good show ..."
            wt_image ttf_bedroom_1_26
            "... removing her top and her bra ..."
            wt_image ttf_bedroom_1_27
            "... as she stares glazily at you."
        else:
            "She bares her breasts, a hypnotized glazy look on her face."
        # system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    elif tammy_lynn.has_tag('hypno_on_walk'):
        wt_image ttf_walk_1_2
        player.c "Hang on a sec, [tammy_lynn.name].  I have something I want you to look at."
        call focus_image from _call_focus_image_88
        player.c "We're going to have a chat, [tammy_lynn.name].  I'm going to talk, and you're going to listen to me."
        player.c "Listen to me, [tammy_lynn.name]. Listen to my voice. Listen to my voice and nothing else, [tammy_lynn.name]. Only my voice. Only my voice now."
        wt_image ttf_walk_1_5
        "She soon falls under your trance."
        player.c "I want you to get comfortable for our talk.  You want me to be comfortable for our talk.  Bare your breasts, [tammy_lynn.name], so that we can both be comfortable and enjoy our talk."
        wt_image ttf_walk_1_6
        "She bares her breasts, a hypnotized glazy look on her face."
    elif tammy_lynn.has_tag('hypno_at_pool'):
        wt_image ttf_pool_1_4
        tammy_lynn.c "Oh, hey!  What's that you have?"
        wt_image ttf_pool_1_26
        player.c "Something I want you to look at."
        call focus_image from _call_focus_image_89
        player.c "We're going to have a chat, [tammy_lynn.name].  I'm going to talk, and you're going to listen to me."
        player.c "Listen to me, [tammy_lynn.name]. Listen to my voice. Listen to my voice and nothing else, [tammy_lynn.name]. Only my voice. Only my voice now."
        wt_image ttf_pool_1_11
        "She soon falls under your trance."
        player.c "I want you to get comfortable for our talk.  You want me to be comfortable for our talk.  Bare your breasts, [tammy_lynn.name], so that we can both be comfortable and enjoy our talk."
        wt_image ttf_pool_1_27
        "She bares her breasts, a hypnotized glazy look on her face."
    else:
        "You can't hypnotize her right now."
        $ ignore_context_change = True
    return

label tammy_lynn_resistance_hypnosis:
    "You work on lowering [tammy_lynn.name]'s resistance to you."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_27
    return

label tammy_lynn_exhibitionism_hypnosis:
    add tags 'hypno_re_exhibitionism' to tammy_lynn
    player.c "You don't mind it when I watch you, [tammy_lynn.name].  You don't mind it when I look at your body.  You like it when I look at you.  You like showing off your body."
    tammy_lynn.c "Yes, I like it when people can see me but can't touch me."
    "That was surprisingly easy.  Hypnosis alone, however, won't turn her into an exhibitionist.  You'll need to encourage that behavior when she's not hypnotized, too."
    # counts as spying on her, once
    $ tammy_lynn.caught_you_watching += 1
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_28
    return

label tammy_lynn_peeing_hypnosis:
    add tags 'hypno_re_peeing' to tammy_lynn
    player.c "It feels good to pee, doesn't it [tammy_lynn.name]?  It feels good to let your bladder go and pressure building up inside you."
    tammy_lynn.c "Y ... yes??"
    player.c "No one should be embarassed to pee, [tammy_lynn.name].  You shouldn't be embarrassed to pee, [tammy_lynn.name].  It's natural.  It's natural and it feels good."
    player.c "You should be comfortable peeing while people watch you, [tammy_lynn.name].  It feels good to pee, [tammy_lynn.name].  It feels great to pee while someone's watching you, [tammy_lynn.name]."
    "That may not be enough on it's own, but it's as much as you can do through hypnosis"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_29
    return

label tammy_lynn_pee_drinking_hypnosis:
    add tags 'hypno_re_pee_drinking' to tammy_lynn
    player.c "It feels good to pee while I'm watching, doesn't it [tammy_lynn.name]?"
    tammy_lynn.c "Yes!"
    player.c "As good as that feels, it'll feel even better when I pee on you, [tammy_lynn.name].  It'll feel warm and natural and wonderful to have my urine sprayed across your body and into my mouth."
    tammy_lynn.c "That's disgusting."
    player.c "A wonderful form of disgusting, [tammy_lynn.name].  The type of disgusting you crave, the type you can't get enough of.  You want me to pee on you.  You want me to mark you with my urine.  You can't wait to feel it and taste it."
    "Maybe that'll work and maybe it won't, but it's as much as you can do through hypnosis"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_30
    return

label tammy_lynn_naked_walk_hypnosis:
    player.c "It's a beautiful day for a walk, [tammy_lynn.name]. You don't mind it when I look at your body.  You like showing off your body.  You should show it off while we enjoy our walk."
    # first time
    if not tammy_lynn.has_tag('hypno_re_naked_walk') and not tammy_lynn.has_tag('exhibitionist_for_you'):
        add tags 'hypno_re_naked_walk' to tammy_lynn
        wt_image ttf_walk_1_19
        player.c "That's good, [tammy_lynn.name].  Now you feel more comfortable.  Now I'm more comfortable.  Now we can enjoy our walk."
        wt_image ttf_walk_1_10
        "And enjoy it you do, as the two of you walk silently ..."
        wt_image ttf_walk_1_11
        "... and enjoy the sights."
    # subsequent
    else:
        if not tammy_lynn.has_tag('hypno_re_naked_walk'):
            add tags 'hypno_re_naked_walk' to tammy_lynn
        wt_image ttf_walk_1_20
        player.c "Don't worry about whether someone else can see you.  As long as I can see your body, you feel good, and happy, and comfortable."
        wt_image ttf_walk_1_21
        player.c "That's good, [tammy_lynn.name].  Now you feel more comfortable.  Now I'm more comfortable.  Now we can enjoy our walk."
        wt_image ttf_walk_1_22
        "And enjoy it you so, as [tammy_lynn.name] struts shamelessly along beside you ..."
        wt_image ttf_walk_1_23
        "... stopping only occasionally to give you time to admire the sights."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_31
    return

label tammy_lynn_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
    if player.has_tag('hypnotist'):
        # note test is against unmodified stat
        add tags 'trigger_implanted' to tammy_lynn
        "[tammy_lynn.name]'s mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
        $ title = "What trigger phrase do you want to use?"
        menu menu_tammy_lynn_implant_trigger:
            "[tammy_lynn.trigger_phrase]":
                pass
            "Choose something else":
                $ tammy_lynn.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
                jump menu_tammy_lynn_implant_trigger
        player.c "[tammy_lynn.name], I have something important to tell you."
        player.c "When you hear the phrase, \"[tammy_lynn.trigger_phrase]\", you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
        tammy_lynn.c "Yes. When I hear, \"[tammy_lynn.trigger_phrase]\", I will fall into a trance and do everything I am told."
        player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it. You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
        tammy_lynn.c "Yes. I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
        #sys "There are currently no opportunities to use [tammy_lynn.name]'s trigger, but you'll be informed if one arises."
    return

label tammy_lynn_hypnosis_end:
    # the following keeps track of how often you've hypnotized the client and subtracts the required energy; can be placed here for Becky Sue because at this point nothing will cancel the hypnosis session
    $ tammy_lynn.hypno_session()
    if tammy_lynn.has_tag('hypno_in_bedroom_1'):
        "When you've done as much as you can for this session, you release [tammy_lynn.name] from her trance and get on with your day."
        rem tags 'hypno_in_bedroom_1' from tammy_lynn
        call forced_movement(living_room) from _call_forced_movement_519
    elif tammy_lynn.has_tag('hypno_on_walk'):
        wt_image ttf_walk_1_5
        "When it's time to head home, you have [tammy_lynn.name] cover herself back up and release her from her trance."
        wt_image ttf_walk_1_1
        tammy_lynn.c "Thanks for the great walk!"
        # now the walk event finishes up by moving you and Tammy Lynn back home
        rem tags 'hypno_on_walk' from tammy_lynn
    elif tammy_lynn.has_tag('hypno_at_pool'):
        wt_image ttf_pool_1_11
        "When you've done as much as you can for this session, you release [tammy_lynn.name] from her trance and get on with your day."
        # now the pool event finishes up by moving you and Tammy Lynn where you belong
        rem tags 'hypno_at_pool' from tammy_lynn
    else:
        "When you've done as much as you can for this session, you release [tammy_lynn.name] from her trance and get on with your day."
        call character_location_return(tammy_lynn) from _call_character_location_return_296
        call forced_movement(living_room) from _call_forced_movement_520
    return

## Character Specific Actions
# Check on her
label tammy_lynn_check_on_her:
    if tammy_lynn.has_tag('first_day'):
        wt_image ttf_unpacking_1
        "She's trying to get unpacked.  Leave her alone for today."
    else:
        $ tammy_lynn.training_session()
        $ tammy_lynn.check_outfit += 1
        # skip watersports unless active
        if tammy_lynn.check_outfit == 5 and not tammy_lynn.has_tag('accepts_watersports'):
            $ tammy_lynn.check_outfit += 1
        # skip phone content under some circumstances
        if tammy_lynn.check_outfit == 6:
            # haven't been spying on her or shut event off
            if tammy_lynn.caught_you_watching < 3 or tammy_lynn.has_tag('phone_events_off'):
                $ tammy_lynn.check_outfit += 2 # +2 to carry it past the scroll number, making the next event a non-chat event
            # confronted her and haven't received sofa phone event yet
            elif tammy_lynn.has_tag('confronted_over_phone') and not tammy_lynn.has_tag('caught_on_phone'):
                $ tammy_lynn.check_outfit += 2
        if tammy_lynn.check_outfit > 7:
            $ tammy_lynn.check_outfit = 1
        # sleeping in
        if tammy_lynn.check_outfit == 1:
            wt_image ttf_sleeping_1_1
            "[tammy_lynn.name] is sleeping in this morning."
            $ title = "What do you do?"
            menu:
                "Watch her":
                    wt_image ttf_sleeping_1_2
                    "She's having a good snooze ..."
                    wt_image ttf_sleeping_1_3
                    "... but eventually she rouses ..."
                    wt_image ttf_sleeping_1_4
                    "... sits up ..."
                    wt_image ttf_sleeping_1_5
                    "... and stretches."
                    wt_image ttf_sleeping_1_6
                    $ title = "What now?"
                    menu:
                        "Leave before she sees you":
                            "You slip away quietly.  You don't spot [tammy_lynn.name] when she eventually leaves, later.  Presumably she's doing something out of the house, today."
                        "Keep watching":
                            # full exhibitionist
                            if tammy_lynn.has_tag('exhibitionist_for_you'):
                                wt_image ttf_sleeping_1_16
                                "As she gets out of bed, [tammy_lynn.name] grins back at you and climbs up on the table by her window ..."
                                wt_image ttf_sleeping_1_13
                                "... to start her yoga routine."
                                wt_image ttf_sleeping_1_17
                                "There's an exuberance to her movement today ..."
                                wt_image ttf_sleeping_1_18
                                "... and she takes her time ..."
                                wt_image ttf_sleeping_1_19
                                "... as she moves through her poses ..."
                                wt_image ttf_sleeping_1_15
                                "... holding them longer ..."
                                wt_image ttf_sleeping_1_20
                                "... and extending herself further into them."
                                wt_image ttf_sleeping_1_16
                                "When she's done, she again grins at you ..."
                                wt_image ttf_sleeping_1_21
                                "... and removes her underwear.  She gives you time to take a good look ..."
                                wt_image ttf_sleeping_1_22
                                "... before moving off to get changed into her clothes, while you go on with your day."
                            # partial show
                            elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                                wt_image ttf_sleeping_1_12
                                "As she gets out of bed, [tammy_lynn.name] takes a peek over her shoulder.  Did she know you were watching, or is she checking in case you are?"
                                wt_image ttf_sleeping_1_13
                                "Either way, she climbs up on a table in front of the window ..."
                                wt_image ttf_sleeping_1_14
                                "... and begins to stretch ..."
                                wt_image ttf_sleeping_1_15
                                "... and move through her yoga poses."
                                wt_image ttf_sleeping_1_12
                                "When she's done, she looks back over her shoulder once more, before moving off slowly to get changed, giving you time to discreetly disappear."
                            else:
                                wt_image ttf_sleeping_1_7
                                "She finishes stretching and gets up."
                                wt_image ttf_sleeping_1_8
                                "It seem like yoga is part of her waking up routine ..."
                                wt_image ttf_sleeping_1_9
                                "... even if the time that she wakes up ..."
                                wt_image ttf_sleeping_1_10
                                "... makes this more of an afternoon routine than a morning routine."
                                wt_image ttf_sleeping_1_11
                                "When she moves into her next position, she looks back over her shoulder and catches you looking.  She freezes, as if in shock."
                                call forced_movement(living_room) from _call_forced_movement_521
                                "You slip away without saying anything, and [tammy_lynn.name] never mentions it, either."
                            $ tammy_lynn.caught_you_watching += 1
                            change player energy by -energy_very_short
                "Discipline her" if tammy_lynn.has_tag('sub_for_you'):
                    wt_image ttf_sleeping_1_23
                    player.c "Wake up!"
                    wt_image ttf_sleeping_1_24
                    tammy_lynn.c "Wh ... what time is it?"
                    wt_image ttf_sleeping_1_25
                    player.c "Past time you got your ass out of bed."
                    wt_image ttf_sleeping_1_26
                    if tammy_lynn.has_tag('late_night_job'):
                        tammy_lynn.c "I was working late last night."
                    elif tammy_lynn.has_tag('earning_keep'):
                        tammy_lynn.c "I was up late last night."
                    else:
                        tammy_lynn.c "I was out late last night."
                    wt_image ttf_sleeping_1_27
                    player.c "Don't talk back to me."
                    $ title = "What are you going to do with her?"
                    menu:
                        "Spank her on her pantied behind":
                            wt_image ttf_sleeping_1_28
                            player.c "Go kneel on the table by the window and present your ass to me."
                            wt_image ttf_sleeping_1_32
                            $ title = "How are you going to do this?"
                            menu:
                                "Make her count":
                                    add tags 'sub_counting' to tammy_lynn
                                "Just spank her":
                                    pass
                            $ tammy_lynn.temporary_count = 0
                            while tammy_lynn.temporary_count < 3:
                                $ tammy_lynn.temporary_count += 1
                                wt_image ttf_sleeping_1_33
                                "*SMACK*"
                                wt_image ttf_sleeping_1_34
                                if tammy_lynn.has_tag('sub_counting'):
                                    tammy_lynn.c "OW!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                else:
                                    tammy_lynn.c "OW!"
                            wt_image ttf_sleeping_1_32
                            $ title = "Spank her again?"
                            menu menu_tammy_lynn_sleeping_spanking_menu:
                                "Again":
                                    $ tammy_lynn.temporary_count += 1
                                    wt_image ttf_sleeping_1_33
                                    "*SMACK*"
                                    wt_image ttf_sleeping_1_34
                                    if tammy_lynn.temporary_count < 5:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "OW!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                        else:
                                            tammy_lynn.c "OW!"
                                    elif tammy_lynn.temporary_count < 15:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "OWWW!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                        else:
                                            tammy_lynn.c "OWWW!!"
                                    else:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "SHIT OWWW!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name].  I'll be good, I promise, [tammy_lynn.your_respect_name]!"
                                        else:
                                            tammy_lynn.c "SHIT OWWW!!  I'll be good, I promise, [tammy_lynn.your_respect_name]!"
                                    if tammy_lynn.temporary_count < 25:
                                        wt_image ttf_sleeping_1_32
                                        jump menu_tammy_lynn_sleeping_spanking_menu
                                    else:
                                        "Your hand is stinging too much to continue the spanking."
                                "That's enough":
                                    pass
                            wt_image ttf_sleeping_1_35
                            if tammy_lynn.temporary_count < 15:
                                tammy_lynn.c "I'm sorry I slept in, and I'm sorry I talked back to you, [tammy_lynn.your_respect_name]."
                                change player energy by -energy_very_short
                            else:
                                tammy_lynn.c "I'm sorry I slept in, and I'm sorry I talked back to you, [tammy_lynn.your_respect_name].  You tanned my ass pretty good for a hand spanking."
                                change player energy by -energy_short
                            rem tags 'sub_counting' from tammy_lynn
                            $ tammy_lynn.temporary_count = 0
                        "Belt her bare ass":
                            wt_image ttf_sleeping_1_28
                            player.c "Go strip out of your underwear and kneel on the table by the window, ass up."
                            wt_image ttf_sleeping_1_36
                            "She trembles when she sees you undo your buckle."
                            tammy_lynn.c "Does it have t be the belt?!"
                            player.c "Head down, ass up."
                            wt_image ttf_sleeping_1_37
                            $ title = "How are you going to do this?"
                            menu:
                                "Make her count":
                                    add tags 'sub_counting' to tammy_lynn
                                "Just belt her":
                                    pass
                            $ tammy_lynn.temporary_count = 0
                            while tammy_lynn.temporary_count < 3:
                                $ tammy_lynn.temporary_count += 1
                                wt_image ttf_sleeping_1_38
                                "*cracckkk*"
                                wt_image ttf_sleeping_1_39
                                if tammy_lynn.has_tag('sub_counting'):
                                    tammy_lynn.c "OOWWW!!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                else:
                                    tammy_lynn.c "OOWWW!!!"
                            wt_image ttf_sleeping_1_37
                            $ title = "Belt her again?"
                            menu menu_tammy_lynn_sleeping_belting_menu:
                                "Again":
                                    $ tammy_lynn.temporary_count += 1
                                    wt_image ttf_sleeping_1_38
                                    "*cracckkk*"
                                    if tammy_lynn.temporary_count < 20:
                                        wt_image ttf_sleeping_1_39
                                    else:
                                        wt_image ttf_sleeping_1_41
                                    if tammy_lynn.temporary_count < 5:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "OOWWW!!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                        else:
                                            tammy_lynn.c "OOWWW!!!"
                                    elif tammy_lynn.temporary_count < 10:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "SHIT OOWWW!!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                                        else:
                                            tammy_lynn.c "SHIT OOWWW!!!"
                                    elif tammy_lynn.temporary_count == 10:
                                        if tammy_lynn.has_tag('sub_counting'):
                                            tammy_lynn.c "OOOO OOOWWWW!!!"
                                            "She seems to have lost the capacity to count."
                                        else:
                                            tammy_lynn.c "OOOO OOOWWWW!!!"
                                    elif tammy_lynn.temporary_count < 15:
                                        tammy_lynn.c "OOOO OOOWWWW!!!"
                                    elif tammy_lynn.temporary_count == 15:
                                        tammy_lynn.c "OOOO OOOWWWW!!!"
                                        wt_image ttf_sleeping_1_40
                                        "She's started to cry, so you check in with her."
                                        tammy_lynn.c "*sniff*  ...  It's okay, a hard beating has always made me cry.  I can take it."
                                    elif tammy_lynn.temporary_count < 20:
                                        tammy_lynn.c "OOOO OOWW OOOOWWWWW!!!"
                                    else:
                                        "Her mouth is open, but she's lost the capacity to scream."
                                    if tammy_lynn.temporary_count < 15:
                                        wt_image ttf_sleeping_1_37
                                    else:
                                        wt_image ttf_sleeping_1_40
                                    jump menu_tammy_lynn_sleeping_belting_menu
                                "That's enough":
                                    pass
                            # end photo
                            if tammy_lynn.temporary_count < 20:
                                wt_image ttf_sleeping_1_36
                            else:
                                wt_image ttf_sleeping_1_42
                            # end dialogue
                            if tammy_lynn.temporary_count < 10:
                                tammy_lynn.c "I'm sorry I slept in, and I'm sorry I talked back to you, [tammy_lynn.your_respect_name]."
                            elif tammy_lynn.temporary_count < 15:
                                "When she can talk again, [tammy_lynn.name] looks back at you."
                                tammy_lynn.c "Wow, I guess you taught me a lesson today, [tammy_lynn.your_respect_name].  My ass will be sore for a week."
                            elif tammy_lynn.temporary_count < 20:
                                "When she can talk again, a still slightly teary-eyed [tammy_lynn.name] looks back at you."
                                tammy_lynn.c "I'm sorry I started crying, [tammy_lynn.your_respect_name].  You'll think I'm a wuss.  Thanks for teaching me a lesson I won't soon forget."
                            else:
                                "When she can talk again, a still teary-eyed [tammy_lynn.name] looks back at you, grinning though her pain."
                                tammy_lynn.c "*sniff* *sniff*  I guess I was wrong, [tammy_lynn.your_respect_name].  You whooped me harder than even my Daddy ever did."
                            if tammy_lynn.temporary_count < 15:
                                change player energy by -energy_very_short
                            else:
                                tammy_lynn.c "I'm sorry I slept in, and I'm sorry I talked back to you, [tammy_lynn.your_respect_name].  You tanned my ass pretty good for a hand spanking."
                            rem tags 'sub_counting' from tammy_lynn
                            $ tammy_lynn.temporary_count = 0
                        "Make her hold a pose":
                            wt_image ttf_sleeping_1_28
                            player.c "Go kneel on the table by the window and face the wall."
                            wt_image ttf_sleeping_1_29
                            player.c "Stay there until I tell you you can move."
                            wt_image ttf_sleeping_1_30
                            tammy_lynn.c "But ..."
                            wt_image ttf_sleeping_1_31
                            player.c "No talking.  And no doing yoga.  You're on a time out, and you're going to stay there until your knees remind you why you need to listen to me.  If I catch you moving a muscle, I'll the start the timer over."
                            wt_image ttf_sleeping_1_11
                            tammy_lynn.c "Yes, [tammy_lynn.your_respect_name]."
                            player.c "Face forward."
                            wt_image ttf_sleeping_1_29
                            "She does as she's told.  By the time you come back and release her, her knees are screaming at her, but there's no sign that she moved, not even to relieve the aching in her legs."
                            add tags 'posing_now' 'posing_discipline' to tammy_lynn
                            $ tammy_lynn.change_image('ttf_sleeping_1_29')
                "Leave":
                    "You don't spot [tammy_lynn.name] when she eventually leaves, later.  Presumably she's doing something out of the house, today."
        # note: 2 is skipped because that falls into "else"
        # major yoga content
        elif tammy_lynn.check_outfit == 3:
            call forced_movement(living_room) from _call_forced_movement_522
            summon tammy_lynn
            wt_image ttf_yoga_1_1
            "You find [tammy_lynn.name] in the living room"
            tammy_lynn.c "Oh, hey!  I'm busy at the moment.  I was just getting started on some yoga."
            $ title = "What do you do?"
            menu:
                "Stay and watch":
                    # if first watching
                    if tammy_lynn.watched_her_do_yoga == 0:
                        wt_image ttf_yoga_1_3
                        "[tammy_lynn.name] waits for a couple of minutes, until it sets in that you're not planning on leaving."
                        wt_image ttf_yoga_1_4
                        "Perhaps cognizant that this is your house and she's just a guest, she tries to ignore you ..."
                        wt_image ttf_yoga_1_5
                        "... and proceeds with her routine."
                        wt_image ttf_yoga_1_6
                        "'Graceful' isn't an adjective that would commonly come to mind when thinking about [tammy_lynn.name], but when doing yoga, she almost is."
                        wt_image ttf_yoga_1_7
                        player.c "What's that pose called?"
                        wt_image ttf_yoga_1_8
                        tammy_lynn.c "No idea.  I learned yoga from a VHS tape played on an old TV with busted sound.  Half the moves I made up, anyway."
                        wt_image ttf_yoga_1_9
                        tammy_lynn.c "I call this one 'rusty Chevy', but Becky Sue insists it looks more like 'rusty Ford'."
                        "You assume she's pulling your leg, but it's disturbingly plausible that this is an argument the two of them could have had."
                        wt_image ttf_yoga_1_10
                        "As [tammy_lynn.name] finishes up and heads to the shower, you go on with your day."
                    # full exhibitionism
                    elif tammy_lynn.has_tag('exhibitionist_for_you'):
                        wt_image ttf_yoga_1_22
                        "[tammy_lynn.name] strips down ..."
                        wt_image ttf_yoga_1_23
                        "... removing not only her top ..."
                        wt_image ttf_yoga_1_33
                        "... but her panties as well."
                        wt_image ttf_yoga_1_34
                        "Now fully naked ..."
                        wt_image ttf_yoga_1_35
                        "... she begins her routine."
                        wt_image ttf_yoga_1_36
                        "She moves confidently though her standing positions ..."
                        wt_image ttf_yoga_1_37
                        "... flowing smoothly from one pose ..."
                        wt_image ttf_yoga_1_38
                        "... to the next."
                        wt_image ttf_yoga_1_39
                        "And when she moves on to her floor positions ..."
                        wt_image ttf_yoga_1_40
                        "... she throws in a 'rusty Chevy', just for you."
                        wt_image ttf_yoga_1_41
                        player.c "Can you do the splits?"
                        wt_image ttf_yoga_1_42
                        tammy_lynn.c "Almost"
                        wt_image ttf_yoga_1_43
                        tammy_lynn.c "Whew!  I'm ready for the shower."
                        player.c "Me, too."
                        wt_image ttf_yoga_1_44
                        if tammy_lynn.has_tag('sub_for_you'):
                            tammy_lynn.c "No touching, remember?  Not when we're doing this, and not the discipline thing."
                        elif tammy_lynn.has_tag('accepts_threesomes') or tammy_lynn.has_tag('threesomes_with_you'):
                            tammy_lynn.c "No touching, remember?  Not when Becky Sue's not around."
                        else:
                            tammy_lynn.c "No touching, remember?"
                        "Maybe not her, but you're seriously contemplating touching yourself."
                    # partial exhibitionism
                    elif tammy_lynn.has_tag('ready_to_take_top_off_yoga'):
                        wt_image ttf_yoga_1_22
                        tammy_lynn.c "It's warm in here again today."
                        wt_image ttf_yoga_1_21
                        tammy_lynn.c "I wouldn't want to get too sweaty.  I should probably get more comfortable."
                        wt_image ttf_yoga_1_23
                        tammy_lynn.c "It's not like I need this on for support."
                        wt_image ttf_yoga_1_24
                        "Now dressed only in her panties ..."
                        wt_image ttf_yoga_1_25
                        "... [tammy_lynn.name] begins her routine."
                        wt_image ttf_yoga_1_26
                        "That routine seems to be equal parts watching you, watching her ..."
                        wt_image ttf_yoga_1_27
                        "... and enjoying the yoga, itself."
                        wt_image ttf_yoga_1_28
                        "When you move closer to have a better look, she freezes in place ..."
                        wt_image ttf_yoga_1_29
                        "... holding the position as you slowly circle her ..."
                        wt_image ttf_yoga_1_30
                        "... observing her body from different angles."
                        wt_image ttf_yoga_1_31
                        if tammy_lynn.has_tag('sub_for_you'):
                            tammy_lynn.c "Just don't touch.  Not when we're doing this, and not the discipline thing."
                        elif tammy_lynn.has_tag('accepts_threesomes') or tammy_lynn.has_tag('threesomes_with_you'):
                            tammy_lynn.c "Just don't touch.  Not when Becky Sue's not around."
                        else:
                            tammy_lynn.c "Just don't touch.  Don't ever touch."
                        wt_image ttf_yoga_1_32
                        "Her warning issued, she pulls herself together and heads to the shower, while you go on with your day."
                    # hesitant exhibitionism
                    elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                        add tags 'ready_to_take_top_off_yoga' to tammy_lynn
                        wt_image ttf_yoga_1_4
                        "[tammy_lynn.name] hesitates, as if debating something."
                        wt_image ttf_yoga_1_3
                        tammy_lynn.c "It's bit warm."
                        wt_image ttf_yoga_1_15
                        tammy_lynn.c "I think I'll take these off."
                        wt_image ttf_yoga_1_16
                        tammy_lynn.c "This isn't any different than you seeing me wear a bikini at the pool."
                        wt_image ttf_yoga_1_17
                        "You're not sure if she's trying to convince you, herself, or an absent [becky_sue.name] ..."
                        wt_image ttf_yoga_1_18
                        "... but she seems to be less interested in her yoga today ..."
                        wt_image ttf_yoga_1_19
                        "... and more interested in watching to see if you're watching her."
                        wt_image ttf_yoga_1_20
                        "Even her 'rusty Chevy' seems brighter today."
                        wt_image ttf_yoga_1_21
                        "As she heads to the shower, [tammy_lynn.name] doesn't even try to hide that she enjoyed this experience."
                        # count as spying on her, once
                        if tammy_lynn.watched_her_do_yoga == 1:
                            $ tammy_lynn.caught_you_watching += 1
                    # other
                    else:
                        wt_image ttf_yoga_1_11
                        "[tammy_lynn.name] seems torn as she starts her routine ..."
                        wt_image ttf_yoga_1_2
                        "... as if she can't decide whether to ignore your presence ..."
                        wt_image ttf_yoga_1_12
                        "... or acknowledge it."
                        # count as spying on her, once
                        if tammy_lynn.watched_her_do_yoga == 1:
                            $ tammy_lynn.caught_you_watching += 1
                            wt_image ttf_yoga_1_14
                            "And when her back is turned, she keeps peeking back at you, as if to confirm you're still watching her, while being uncertain how she feels when she finds that you are."
                        else:
                            wt_image ttf_yoga_1_13
                            "In the end, she seems to decide she doesn't mind having you an audience."
                        wt_image ttf_yoga_1_5
                        "She finishes her routine in silence ..."
                        wt_image ttf_yoga_1_6
                        "... showing off her flexibility ..."
                        wt_image ttf_yoga_1_7
                        "... as you watch, appreciately."
                        wt_image ttf_yoga_1_9
                        player.c "I think that looks more like a rusty Dodge."
                        wt_image ttf_yoga_1_8
                        tammy_lynn.c "Don't even start."
                        wt_image ttf_yoga_1_10
                        "That's it for the show.  [tammy_lynn.name] goes to shower, and you go on with your day."
                    $ tammy_lynn.watched_her_do_yoga += 1
                    change player energy by -energy_very_short
                "Check on her tomorrow":
                    wt_image ttf_yoga_1_2
                    "[tammy_lynn.name] goes on with her stretches, and you go on with your day."
        # note: 4 is skipped because that falls into "else"
        # waterspots - only reach this if pass test above, which will typically only happen once 6 below is no longer active
        elif tammy_lynn.check_outfit == 5:
            $ tammy_lynn.pee_outfit += 1
            if tammy_lynn.pee_outfit > 2:
                $ tammy_lynn.pee_outfit = 1
            wt_image current_location.image
            "You don't see [tammy_lynn.name], but she hears you, and calls to you from the bathroom."
            tammy_lynn.c "I'm in here!"
            call forced_movement(bathroom) from _call_forced_movement_523
            summon tammy_lynn
            if tammy_lynn.pee_outfit == 1:
                wt_image ttf_toilet_3_1
                tammy_lynn.c "I was just about to 'you know what'."
                $ title = "What do you do?"
                menu:
                    "Watch her pee":
                        wt_image ttf_toilet_3_2
                        "She takes a seat ..."
                        wt_image ttf_toilet_3_3
                        "... giving you a clear view as she prepares to do her business."
                        wt_image ttf_toilet_3_4
                        "Holding herself like this ..."
                        wt_image ttf_toilet_3_5
                        "... only the first few dribbles go into the bowl."
                        wt_image ttf_toilet_3_6
                        "The majority arcs out, over the seat, and onto the floor ..."
                        wt_image ttf_toilet_3_7
                        "... as she empties her bladder in front of you."
                        wt_image ttf_toilet_3_8
                        "Once she's finished ..."
                        wt_image ttf_toilet_3_9
                        "... she squats on the toilet to avoid stepping in the mess on the floor ..."
                        wt_image ttf_toilet_3_10
                        "... wipes herself off ..."
                        wt_image ttf_toilet_3_11
                        "... and then cleans the toilet and floor."
                        tammy_lynn.c "I am so filthy."
                        $ title = "What do you say?"
                        menu:
                            "I like you like this":
                                wt_image ttf_toilet_3_12
                                tammy_lynn.c "That's because you're just as filthy."
                            "You're absolutely disgusting":
                                wt_image ttf_toilet_3_12
                                if tammy_lynn.has_tag('sub_for_you'):
                                    tammy_lynn.c "I really am, [tammy_lynn.your_respect_name].  I was before I met you, and you've trained me to be even worse."
                                else:
                                    tammy_lynn.c "I really am.  I was before I met you, and you've made me even worse."
                            "At least you clean up after yourself":
                                wt_image ttf_toilet_3_12
                                tammy_lynn.c "Please tell me that's not a comparison to Becky Sue, because if she does this for you, too, I really don't want to know!"
                        change player energy by -energy_very_short
                    "Pee on her" if tammy_lynn.has_tag('sub_for_you') or tammy_lynn.has_tag('hypno_re_pee_drinking') or tammy_lynn.has_tag('peed_on_her'):
                        wt_image ttf_toilet_1_1
                        "As she sits down to relieve herself, you take out your cock and aim it at her."
                        if tammy_lynn.has_tag('peed_on_her'):
                            tammy_lynn.c "Shit!!  That again??"
                            player.c "Yes.  Put your hand down."
                            wt_image ttf_toilet_1_5
                            tammy_lynn.c "I can't believe I do this for you."
                            player.c "Just keep your mouth open."
                            wt_image ttf_toilet_1_6
                            "She does, and she keeps her eyes fixed on yours as you empty your bladder over and into her  ...  pzzzzzzzzzzzzzzzzzzzzzzz"
                            wt_image ttf_toilet_1_7
                            tammy_lynn.c "I'm totally disgusting, aren't I?"
                            $ title = "What do you say?"
                            menu:
                                "In the best possible way":
                                    pass
                                "You're worthless garbage":
                                    pass
                            "She doesn't reply, just listens intently, revelling in your reaction."
                        else:
                            add tags 'peed_on_her' to tammy_lynn
                            tammy_lynn.c "Wait!!  What are you doing?!"
                            if tammy_lynn.toilet_count == 3:
                                player.c "What I told you I was going to do before."
                            elif tammy_lynn.has_tag('sub_for_you'):
                                player.c "Disciplining you."
                            else:
                                player.c "Relax, you'll enjoy this."
                            if tammy_lynn.has_tag('sub_for_you'):
                                tammy_lynn.c "But I haven't agreed to that type of discipline."
                                player.c "You're about to agree now.  Get on the floor in front of me."
                                wt_image ttf_toilet_1_2
                                tammy_lynn.c "What are you going to think about me from now on, everytime you see me?"
                                $ title = "What do you say?"
                                menu:
                                    "How special you are":
                                        player.c "The only thing I'm going to think is about how special you are, to be willing to offer this to me."
                                    "How disgustng you are":
                                        player.c "I'm going to think about what a disgusting pig you are, with no better use than to serve as my toilet."
                            else:
                                wt_image ttf_toilet_1_2
                                "She's surprised to find herself on her knees in front of you, ready to do something she didn't think she was capable of doing."
                            wt_image ttf_toilet_1_3
                            "She recoils as the stream hits her, and you need to hold the back of her head to keep her face in place as you piss on her  ...  pzzzzzzzzzzzzzzzzzzzzzzz"
                            wt_image ttf_toilet_1_4
                            tammy_lynn.c "SHIT!!  I DID IT!  I even drank some of it!!"
                            player.c "And you'll do it again, when I want you to."
                            "You don't need to wait to see her nodding to know the answer's yes."
                        change player energy by -energy_very_short
                    "Leave":
                        pass
            else:
                wt_image ttf_toilet_5_1
                tammy_lynn.c "I was just finishing up my bath."
                wt_image ttf_toilet_5_2
                tammy_lynn.c "Do you think there's anything I should do before I get out?"
                $ title = "What do you think?"
                menu:
                    "Tell her to pee":
                        wt_image ttf_toilet_5_3
                        "She spreads herself wide ..."
                        wt_image ttf_toilet_5_4
                        "... and concentrates ..."
                        wt_image ttf_toilet_5_5
                        "... until she releases an arc of golden fluid ..."
                        wt_image ttf_toilet_5_6
                        "... into the bathwater she just washed in."
                        wt_image ttf_toilet_5_7
                        tammy_lynn.c "I'm going to be rinsing off in water I just peed in."
                        "There's a huskiness to her voice that belies a strong reaction to the prospect."
                        wt_image ttf_toilet_5_1
                        "As she slides back into the water, she looks up at you, and asks a question with that same huskiness in her voice."
                        tammy_lynn.c "Am I disgusting?"
                        $ title = "What do you say?"
                        menu:
                            "Wonderfully so":
                                pass
                            "You're a filthy, worthless pig":
                                pass
                        wt_image ttf_toilet_5_8
                        "She just watches you, saying nothing, as she stands up and dries herself off.  You're not sure she cared what you said, as long as she elicited a strong reaction from you."
                        change player energy by -energy_very_short
                    "Pee on her" if tammy_lynn.has_tag('peed_on_her'):
                        wt_image ttf_toilet_5_9
                        tammy_lynn.c "I just finished getting cleaned up!"
                        player.c "Open your mouth wide enough and you'll be fine."
                        wt_image ttf_toilet_5_10
                        tammy_lynn.c "Don't miss."
                        "She closes her eyes, leans her head back ..."
                        wt_image ttf_toilet_5_11
                        "... and opens her mouth as you empty your bladder  ...  pzzzzzzzzzzzzzzzzzzzzzzz"
                        wt_image ttf_toilet_5_9
                        tammy_lynn.c "You got some on me!"
                        player.c "You should have opened your mouth wider."
                        wt_image ttf_toilet_5_1
                        "As she slides back into the water, there's a huskiness to her voice as she asks you a question."
                        tammy_lynn.c "Am I the most disgusting person you know?"
                        $ title = "What do you say?"
                        menu:
                            "And all the more special for that":
                                pass
                            "It's hard to even think of you as a person when you're drinking my piss":
                                pass
                        wt_image ttf_toilet_5_8
                        "She just watches you, saying nothing, as she stands up and dries herself off.  You're not sure she cared what you said, as long as she elicited a strong reaction from you."
                        change player energy by -energy_very_short
                    "Nothing for today":
                        pass
            call forced_movement(living_room) from _call_forced_movement_524
        # on her phone content - only reach this if pass test above
        elif tammy_lynn.check_outfit == 6:
            # previously confronted
            if tammy_lynn.has_tag('caught_on_phone'):
                add tags 'phone_events_off' to tammy_lynn
                wt_image ttf_bedroom_2_6
                "[tammy_lynn.name] is spamming the internet again with photos of her genitalia."
                if tammy_lynn.has_tag('sub_for_you'):
                    $ title = "What do you do?"
                    menu:
                        "Tell her this stops":
                            add tags 'no_porn_selfies' to tammy_lynn
                            wt_image ttf_bedroom_2_12
                            tammy_lynn.c "What are you doing in here?!"
                            player.c "Putting an end to this.  Show me your tablet."
                            wt_image ttf_bedroom_2_8
                            player.c "Look at these comments, [tammy_lynn.name].  Most of them are calling you down to the lowest."
                            tammy_lynn.c "Some are complementary."
                            player.c "Those aren't the ones you're drawn to, though, are they?  You don't post the photos to be told how pretty you are.  You post them for comments like arealman736's, 'What a dirty skank cunt u hav. I'd rape you til u bleed'."
                            wt_image ttf_bedroom_2_11
                            tammy_lynn.c "I'm disgusting, aren't I?"
                            $ title = "What do you tell her?"
                            menu:
                                "Yes, she's disgusting":
                                    player.c "Yes, you are.  This is a filthy, whorish behavior and I won't have it under my roof."
                                    wt_image ttf_bedroom_2_9
                                    tammy_lynn.c "Yes, [tammy_lynn.your_respect_name].  I'll stop it."
                                "No, she isn't":
                                    player.c "No, you're not.  But this isn't good for you.  I'm not going to allow you to post these photos any more.  Not while you're under my roof."
                                    wt_image ttf_bedroom_2_9
                                    tammy_lynn.c "Yes, [tammy_lynn.your_respect_name].  Thank you.  This is a really bad habit.  I'll stop it."
                            "You're not sure she'll be completely able to do so, but she seems heartfelt about wanting to try."
                        "Let her have her silly fun":
                            wt_image ttf_bedroom_2_7
                            "She doesn't have a lot of sexual outlets.  If reading comments from strangers about her bodyparts brings her some guilty joy, there doesn't seem to be any harm in it."
                else:
                    wt_image ttf_bedroom_2_7
                    "She's an odd duck in a lot of ways, not least of all her sexuality.  Even she would be hard-pressed to explain why reading comments from strangers about her most intimate bodyparts gives her such guilty pleasure."
            # previously seen
            elif tammy_lynn.has_tag('saw_on_phone'):
                wt_image ttf_bedroom_2_1
                "[tammy_lynn.name] is working on her hair ..."
                wt_image ttf_bedroom_2_9
                "... but seems to be thinking about something else."
                wt_image ttf_bedroom_2_10
                "She finishes her hair ..."
                wt_image ttf_bedroom_2_5
                "... picks up her tablet ..."
                wt_image ttf_bedroom_2_11
                "... and then puts it back down.  She sits there for a while, staring at it, seemingly debating what to do."
                wt_image ttf_bedroom_2_5
                "Eventually, she picks the table up again ..."
                wt_image ttf_bedroom_2_6
                "... and takes a photo of an intimate area."
                wt_image ttf_bedroom_2_7
                "You presume the smile means the photo came out well."
                wt_image ttf_bedroom_2_8
                $ title = "What do you do?"
                menu:
                    "Leave her for today":
                        "You may be able to confront her about this some other time.  For today, you leave her alone and go on with your day."
                    "Ignore her (shuts these events off)":
                        add tags 'phone_events_off' to tammy_lynn
                        "Whatever's she up to is of no interest to you.  You leave her alone and go on with your day."
                    "Confront her":
                        wt_image ttf_bedroom_2_12
                        tammy_lynn.c "Shit!!  What are you doing in here?!"
                        player.c "Trying to figure out what you're doing."
                        wt_image ttf_bedroom_2_13
                        tammy_lynn.c "Nothing.  I was just looking at my phone."
                        player.c "You weren't looking at your phone, you were using your tablet."
                        wt_image ttf_bedroom_2_14
                        tammy_lynn.c "No I wasn't.  I was looking up today's forecast on my phone.  Here, I'll show you."
                        player.c "Why don't you show me what's on the tablet you shoved into the dresser drawer when I walked in."
                        wt_image ttf_bedroom_2_15
                        tammy_lynn.c "You have to go!!  I'm getting dressed!"
                        "She shoves you out of her room, demonstrating surprising strength for her size."
                        wt_image ttf_bedroom_2_16
                        "Whatever she's up to, she's not going to disclose it voluntarily.  You'll need to catch her at it, preferably somewhere outside the privacy protection of her room.  It may take some time for the right opportunity to arise."
                        add tags 'confronted_over_phone' to tammy_lynn
            # first time
            else:
                add tags 'saw_on_phone' to tammy_lynn
                wt_image ttf_bedroom_2_1
                "[tammy_lynn.name] is up ..."
                wt_image ttf_bedroom_2_2
                "... and getting ready for her day."
                wt_image ttf_bedroom_2_3
                "With her hair in place, she pauses, and seems to deliberate."
                wt_image ttf_bedroom_2_4
                "A mischievous look on her face ..."
                wt_image ttf_bedroom_2_5
                "... she picks up her tablet ..."
                wt_image ttf_bedroom_2_6
                "... and takes a rather intimate photo."
                wt_image ttf_bedroom_2_7
                "Other than her fascination with [becky_sue.name], [tammy_lynn.name]'s sexuality is a bit of a mystery.  It's not immediately obvious what she's up to, but whatever it is, she seems pleased with the results."
                wt_image ttf_bedroom_2_8
                "While she's engrossed with her tablet, you slip away.  You might catch her at this again and get the opportunity to find out more about what she's up to."
        # available for a chat - usually happens every 2nd time you check on her
        else:
            $ tammy_lynn.training_session()
            rem tags 'no_hypnosis' from tammy_lynn
            wt_image ttf_bedroom_1_1
            tammy_lynn.c "Oh, hey!  Did you want something?"
            $ title = "What do you want?"
            call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_34
            add tags 'no_hypnosis' to tammy_lynn #to restrict timing of when she can be hypnotized
        if tammy_lynn.has_tag('posing_now'):
            call character_location_return(tammy_lynn) from _call_character_location_return_297
        else:
            dismiss tammy_lynn
        call forced_movement(living_room) from _call_forced_movement_525
        notify
    return

label tammy_lynn_check_on_her_settling_in:
    add tags 'discussed_settling_in' to tammy_lynn
    wt_image ttf_bedroom_1_2
    tammy_lynn.c "Yes, thanks!  Becky Sue has me all settled in.  This place is awesome!  Thanks again for letting me stay here!!"
    call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_35
    return

label tammy_lynn_check_on_her_hypnosis:
    add tags 'hypno_in_bedroom_1' to tammy_lynn
    $ queue_action(tammy_lynn.hypno_action)
    return

label tammy_lynn_check_on_her_becky_sue:
    wt_image ttf_bedroom_1_3
    tammy_lynn.c "Isn't she great?"
    $ title = "What do you say?"
    menu:
        "Stay away from her" if not becky_sue.has_tag('sleeping_with_friend'):
            player.c "Yes, she is, and she's my mine.  I'm letting you stay here so I can keep an eye on you.  Keep your hands off her, understand?"
            if tammy_lynn.has_tag('seducing_friend'):
                rem tags 'seducing_friend' from tammy_lynn
                wt_image ttf_bedroom_1_5
                tammy_lynn.c "But you said ..."
                player.c "I know what I said before, but I've changed my mind.  The only one who gets to sleep with [becky_sue.name] is me."
            else:
                pass
            wt_image ttf_bedroom_1_4
            tammy_lynn.c "Totally!!  Becky Sue and I are just friends, nothing else.  I wouldn't ever try to get between you.  I promise!"
        "I want to help the two of you get closer" if not tammy_lynn.has_tag('seducing_friend') and not becky_sue.has_tag('sleeping_with_friend'):
            add tags 'seducing_friend' to tammy_lynn
            wt_image ttf_bedroom_1_6
            tammy_lynn.c "What do you mean?  We're already best friends."
            player.c "I know.  But it's pretty clear to me that you'd like to be more than that.  You're in love, or at least in lust, with her."
            wt_image ttf_bedroom_1_5
            tammy_lynn.c "I'm ... that's not ...  I wouldn't ..."
            player.c "It's okay. I don't mind.  I'd like to help [becky_sue.name] to see you the same way you see her, as a possible sex partner, not just a childhood friend.  You'd like that, wouldn't you?"
            wt_image ttf_bedroom_1_7
            "If the look on her face wasn't confirmation enough, her stiffening nipples certainly are."
            tammy_lynn.c "But why??"
            player.c "I know you're from the country, but you're not that naive, are you?  I just need to know one more thing: if I help you to have a more intimate relationship with [becky_sue.name], you'll be grateful to me, won't you?"
            wt_image ttf_bedroom_1_8
            tammy_lynn.c "Well, yeah.  I guess.  But she's not into girls."
            wt_image ttf_bedroom_1_9
            player.c "Between the two of us, we may be able to change that."
        "Yes, she is":
            wt_image ttf_bedroom_1_6
            tammy_lynn.c "I know, right?  We're so lucky to have her!"
    call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_36
    return

label tammy_lynn_check_on_her_getting_work:
    if tammy_lynn.weeks_with_you < 5 and not tammy_lynn.has_tag('earning_keep'):
        wt_image ttf_bedroom_1_6
        tammy_lynn.c "I haven't even been here a month!  Give me some time to get used to the city, okay?  I'm sure I'll figure out something I can do as a job soon."
        call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_37
    elif not becky_sue.has_tag('studying') and not becky_sue.has_tag('earning_keep'):
        tammy_lynn.c "[becky_sue.name] and I have both been kicking ideas around, but we haven't come up with anything, yet."
        "You may need to deal with [becky_sue.name]'s lack of contribution to the household, before you can deal with tag-along [tammy_lynn.name]."
        call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_38
    else:
        if becky_sue.has_tag('studying') and becky_sue.has_tag('discussed_police_job') and not tammy_lynn.has_tag('discussed_police_job'):
            add tags 'discussed_police_job' to tammy_lynn
            wt_image ttf_bedroom_1_28
            tammy_lynn.c "I wanna become a police officer, like Becky Sue!!"
            player.c "[becky_sue.name] isn't a police officer."
            wt_image ttf_bedroom_1_9
            tammy_lynn.c "Not yet, but she said that after she gets her diploma, you're going to help her join the police."
            player.c "I am NOT going to help [becky_sue.name] join the police."
            wt_image ttf_police_1_1
            tammy_lynn.c "But she'd be a great cop!  We both would!!  After Becky Sue shoots the bad guys and makes them fall down, I'll shoot 'em again ... BANG! BANG!"
            player.c "Why would you ...  "
            wt_image ttf_bedroom_1_10
            player.c "You know what?  Never mind.  Neither you nor [becky_sue.name] are going to be police officers."
            tammy_lynn.c "Awwwww.  Well, what else could I do, if I can't be a cop?"
        else:
            wt_image ttf_bedroom_1_10
            tammy_lynn.c "I know I need to do something, but I can't figure out what.  What do you think I should do?"
        call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_39
    return

label tammy_lynn_check_on_her_paying_rent:
    if tammy_lynn.weeks_with_you < 5 and not tammy_lynn.has_tag('earning_keep'):
        wt_image ttf_bedroom_1_6
        tammy_lynn.c "I haven't even been here a month!  Give me some time to get used to the city, okay?  I'm sure I'll figure out something I can do as a job soon, and then I'll be out of your hair."
        call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_40
    else:
        if tammy_lynn.has_tag('earning_keep'):
            wt_image ttf_bedroom_1_6
            tammy_lynn.c "I am pitching in with expenses now!  Buying food and stuff.  That's something, right?."
            player.c "You could be doing more."
            wt_image ttf_bedroom_1_5
            tammy_lynn.c "But you know my job doesn't pay that much.  I don't have any extra to give you."
        else:
            wt_image ttf_bedroom_1_5
            tammy_lynn.c "You know I don't have a job, yet.  I don't have any money to give you."
        player.c "Then you'd better find some other way to 'pay' for the roof over your head."
        if tammy_lynn.has_tag('threesomes_with_you'):
            wt_image ttf_bedroom_1_5
            tammy_lynn.c "I know you don't mean sleeping with me, because you're already doing that.  So what more could you want?"
        elif tammy_lynn.has_tag('accepts_threesomes'):
            wt_image ttf_bedroom_1_5
            tammy_lynn.c "I know you don't mean sleeping with me, because I already told you I'll do that as long as Becky Sue's part of it.  So what more could you want?"
        elif tammy_lynn.has_tag('seducing_friend'):
            wt_image ttf_bedroom_1_4
            tammy_lynn.c "I know you don't mean sleeping with me, because I'm sure you wouldn't do that to Becky Sue.  Besides, I'm not into you, or anybody, really, other than Becky Sue.  So what could you want?"
        else:
            wt_image ttf_bedroom_1_4
            tammy_lynn.c "I know you don't mean sleeping with me, because I'm sure you wouldn't do that to Becky Sue.  Besides, I'm not into you, or anybody, really.  So what could you want?"
        player.c "Something that makes it worthwhile for me to have you in the house."
        wt_image ttf_bedroom_1_8
        tammy_lynn.c "I clean up sometimes.  Does that count?"
        player.c "You can do better than that."
        # check for conditions
        if tammy_lynn.has_tag('threesomes_with_you') and becky_sue.has_tag('accepts_domestic_discipline'):
            add tags 'ready_for_bondage' to tammy_lynn
        if tammy_lynn.caught_you_watching > 4 and (tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.has_tag('caught_on_phone')):
            add tags 'ready_for_exhibitionism' to tammy_lynn
        # intros
        if tammy_lynn.has_tag('ready_for_bondage') and tammy_lynn.has_tag('ready_for_exhibitionism'):
            wt_image ttf_bedroom_1_7
            tammy_lynn.c "I guess I have a couple of ideas of things you might like."
        elif tammy_lynn.has_tag('ready_for_bondage') or tammy_lynn.has_tag('ready_for_exhibitionism'):
            wt_image ttf_bedroom_1_7
            tammy_lynn.c "I guess I have one idea you might like."
        # if applicable, offers exhibitionism
        if tammy_lynn.has_tag('ready_for_exhibitionism'):
            wt_image ttf_bedroom_1_11
            if tammy_lynn.has_tag('caught_on_phone'):
                tammy_lynn.c "I know you like to look at my body.  And you know I've got a little bit of an exhibitionist streak.  What if I let you see a bit more of my body sometimes, when I'm around the house?"
            else:
                tammy_lynn.c "I know you like to look at my body.  You probably don't know this, but I've got a little bit of an exhibitionist streak.  What if I let you see a bit more of my body sometimes, when I'm around the house?"
            $ title = "Pick this?"
            menu:
                "Yes":
                    add tags 'exhibitionist_for_you' 'rent_conversation_off' to tammy_lynn
                    player.c "Prove it."
                    wt_image ttf_bedroom_1_9
                    tammy_lynn.c "You mean prove that I'll take my clothes off for you?  I'm not a fucking stripper.  You'll never get me on the pole, and I'm not doing any strip teases for you."
                    wt_image ttf_bedroom_1_12
                    tammy_lynn.c "But if it starts to get hot around the house, I may need to take my shirt off ..."
                    wt_image ttf_bedroom_1_13
                    tammy_lynn.c "... and if Becky Sue isn't around to catch us, I may not wear a bra, either."
                    wt_image ttf_bedroom_1_14
                    player.c "What about your pussy?"
                    wt_image ttf_bedroom_1_15
                    tammy_lynn.c "I kinda have a thing about people being able to see my pussy but not touch it ..."
                    wt_image ttf_bedroom_1_16
                    tammy_lynn.c "So, yeah, this sorta thing will probably happen."
                    wt_image ttf_bedroom_1_17
                    tammy_lynn.c "This is gonna be fun!"
                    wt_image ttf_bedroom_1_18
                    "She's not the only one who thinks so."
                "Not right now":
                    rem tags 'ready_for_exhibitionism' from tammy_lynn
                    player.c "Come up with something else."
        # if applicable, offers submission
        if tammy_lynn.has_tag('ready_for_bondage'):
            wt_image ttf_bedroom_1_7
            tammy_lynn.c "I know you like to boss Becky Sue around.  If you want, I'll let you do a little bit of that with me, too."
            player.c "You want me to dominate you?"
            wt_image ttf_bedroom_1_9
            tammy_lynn.c "Not really, but I'll let you do a bit of that, as a way to pay my rent.  I'll even call you [becky_sue.your_respect_name]."
            $ title = "Pick this?"
            menu:
                "Yes":
                    add tags 'sub_for_you' 'rent_conversation_off' to tammy_lynn
                    $ title = "Do you want her to call you [becky_sue.your_respect_name]?"
                    menu:
                        "Yes":
                            $ tammy_lynn.your_respect_name = becky_sue.your_respect_name
                            player.c "You want to submit to me, prove it."
                        "No":
                            player.c "Don't call me that.  That's what [becky_sue.name] calls me."
                            tammy_lynn.c "What should I call you?"
                            $ tammy_lynn.temporary_count = 1
                            while tammy_lynn.temporary_count == 1:
                                $ title = "How should she address you?"
                                $ tammy_lynn.your_respect_name = renpy.input(_("What should she call you?"))
                                $ title = "Do you want her to call you [tammy_lynn.your_respect_name]?"
                                menu:
                                    "Yes":
                                        $ tammy_lynn.temporary_count = 0
                                    "No":
                                        pass
                    wt_image ttf_bedroom_1_8
                    tammy_lynn.c "What do you want me to do, [tammy_lynn.your_respect_name]?"
                    player.c "Remove your clothes."
                    wt_image ttf_bedroom_1_12
                    tammy_lynn.c "Yes, [tammy_lynn.your_respect_name]."
                    wt_image ttf_bedroom_1_19
                    player.c "Once you're naked, kneel."
                    wt_image ttf_bedroom_1_20
                    player.c "Do you think this is funny?"
                    wt_image ttf_bedroom_1_21
                    tammy_lynn.c "Maybe a little?"
                    wt_image ttf_bedroom_1_22
                    player.c "You might not find it so funny the first time I take my belt off and use it on you."
                    wt_image ttf_bedroom_1_23
                    tammy_lynn.c "My ass won't, that's for darn sure.  But I doubt you'll whoop me any harder than my Daddy used to, so I think I can take it."
                    "Sounds like she has some idea, at least, of what she's gotten herself into."
                    # reset phone event, if applicable
                    if tammy_lynn.has_tag('caught_on_phone') and tammy_lynn.has_tag('phone_events_off'):
                        rem tags 'phone_events_off' from tammy_lynn
                "Not right now":
                    rem tags 'ready_for_bondage' from tammy_lynn
                    player.c "Come up with something else."
        # if neither offered or accepted
        if not tammy_lynn.has_tag('ready_for_exhibitionism') and not tammy_lynn.has_tag('ready_for_bondage'):
            wt_image ttf_bedroom_1_10
            tammy_lynn.c "I'm sorry, I can't think of anything right now."
            "As she gets to know what you like, maybe she'll come up with something."
            call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_41
    return

label tammy_lynn_check_on_her_threesomes:
    player.c "You're enjoying your new relationship with [becky_sue.name], aren't you?"
    wt_image ttf_bedroom_1_2
    tammy_lynn.c "Am I ever!!  Thank you so much for helping this to happen!"
    player.c "I told you that once we succeeded, I expect you to be grateful."
    wt_image ttf_bedroom_1_28
    tammy_lynn.c "And I am!!  So grateful, you can't believe!"
    player.c "Great!  So you won't mind sleeping with me, going forward."
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "What?!"
    player.c "Having sex with me, [tammy_lynn.name].  You get to fuck [becky_sue.name], I get to fuck you.  It's a fair trade."
    wt_image ttf_bedroom_1_8
    tammy_lynn.c "You're pulling my leg!  I don't like boys.  Or girls, really, other than Becky Sue.  You know that!"
    player.c "And now you get to sleep with her, thanks to my help.  And you're supposedly grateful for that.  This is your way to show it."
    wt_image ttf_bedroom_1_5
    tammy_lynn.c "You're fucking serious, aren't you?  You expect me to put out for you."
    player.c "Yes, I do."
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "How about this?  I'll let you touch me if Becky Sue is okay with that, but only when she's around.  If I'm making love with her, I guess I can get my head around the idea of you joining in.  You are her boyfriend, after all.  But only if Becky Sue agrees to the arrangement."
    add tags 'accepts_threesomes' to tammy_lynn
    if becky_sue.has_tag('accepts_threesomes'):
        "The two women have now both agreed.  When you're ready, you can take them both on a date to consumate your new, happier household relationships."
    else:
        "Once you get [becky_sue.name] onside with threesomes as well, you can add a new dimension to yours and Becky Sue's relationship."
    return

label tammy_lynn_check_on_her_discuss_photos:
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "I figured you'd bring that up again.  It's nothing, really.  It's just something I do once in a while."
    player.c "Seems to me you do it fairly often."
    tammy_lynn.c "I guess it's become a habit.  It started when I was fairly young.  The boys back home are frigging idiots, so I didn't trust any of the compliments they paid me after I hit puberty.  I wanted to know what more worldly men thought."
    player.c "Now you're hooked on the flattery?"
    wt_image ttf_bedroom_1_5
    tammy_lynn.c "What?  No.  I mean, yes.  The compliments are really nice."
    player.c "It's not the compliments you're after, then.  Is it the insults?"
    wt_image ttf_bedroom_1_4
    tammy_lynn.c "Why would people insult me?  Do you think there's something wrong with my body?"
    player.c "It's the internet.  You don't post nude photos without getting some insulting comments."
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "A lot, actually.  These sites are absolutely toxic.  Some of the trolls are really creative, though.  I get a kick out of getting a reaction out of them, and reading the filth they spew."
    player.c "Does it get you off?  Do you masturbate to the comments?"
    wt_image ttf_bedroom_1_4
    tammy_lynn.c "Eewww.  No, why would I do that?  That's gross."
    wt_image ttf_bedroom_1_11
    tammy_lynn.c "But what's fun is knowing they can see my pussy and they're all worked up thinking about nasty things they want to do to it and me, but they can't ever, never touch it!!"
    "Even [tammy_lynn.name]'s kink seems to be strangely asexual to her, although it clearly inspires strong reactions in her.  You're sure she must be getting a sexual charge out of having her body viewed and discussed, but that doesn't seem to manifest the way it does for most people."
    call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_42
    return

label tammy_lynn_check_on_her_discuss_work:
    call safe_call('tammy_lynn_talk_job_' + tammy_lynn.job, override = 'tammy_lynn_talk_job_job') from _call_safe_call_7
    call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_43
    return

label tammy_lynn_check_on_her_tied_bed:
    wt_image ttf_bedroom_1_30
    player.c "Remove your clothes, then lie down on the bed."
    wt_image ttf_bondage_1_1
    "As she lays on her back, you secure her firmly to the bedframe."
    if dungeon.has_item(gags):
        $ title = "Gag her?"
        menu:
            "Yes":
                add tags 'gagged_now' to tammy_lynn
                wt_image ttf_bondage_1_2
                "Despite what [becky_sue.name] sometimes claims, [tammy_lynn.name] doesn't have a big mouth.  After some serching, though, you find a gag that fits her perfectly."
                wt_image ttf_bondage_1_3
            "No":
                pass
    $ title = "What now?"
    menu menu_tammy_lynn_bondage_menu:
        "Leave her there" if not tammy_lynn.has_tag('bondage_left'):
            add tags 'bondage_left' to tammy_lynn
            "With [tammy_lynn.name] securely tied in place, you leave."
            call forced_movement(living_room) from _call_forced_movement_526
            wt_image current_location.image
            if tammy_lynn.has_tag('clamped_now'):
                "You wouldn't leave [tammy_lynn.name] for long with the clamps digging into her flesh and cutting off blood flow, but [tammy_lynn.name] doesn't know that."
                call forced_movement(dungeon) from _call_forced_movement_527
                wt_image ttf_bondage_1_7
                "When you return, you can see the panic subside from her face, as she realizes her ordeal will soon come to an end."
                wt_image ttf_bondage_1_8
            elif tammy_lynn.has_tag('gagged_now'):
                "You leave her alone for about an hour."
                call forced_movement(dungeon) from _call_forced_movement_528
                wt_image ttf_bondage_1_5
                "When you return, [tammy_lynn.name] lifts her head eagerly, relieved to see you."
                wt_image ttf_bondage_1_3
            else:
                "You leave her alone for about an hour."
                call forced_movement(dungeon) from _call_forced_movement_529
                wt_image ttf_bondage_1_4
                "By the time you return, there's an audible sigh of relief from [tammy_lynn.name]."
                wt_image ttf_bondage_1_1
            $ title = "What now?"
            jump menu_tammy_lynn_bondage_menu
        "Put clamps on her" if tammy_lynn.has_tag('gagged_now') and not tammy_lynn.has_tag('clamped_now'):
            wt_image ttf_bondage_1_6
            "The clamps bite cruelly into the tender flesh of her labia ..."
            wt_image ttf_bondage_1_7
            "... and nipples ..."
            wt_image ttf_bondage_1_8
            "... the ballgag stiffling her cries of pains as you securely fasten them in place."
            $ title = "What now?"
            jump menu_tammy_lynn_bondage_menu
        "Remove the clamps" if tammy_lynn.has_tag('clamped_now'):
            rem tags 'clamped_now' from tammy_lynn
            wt_image ttf_bondage_1_7
            "When she's worn the clamps long enough, you move closer to remove them.  [tammy_lynn.name] trembles with relief when she realizes the clamps are coming off ..."
            wt_image ttf_bondage_1_6
            "... and then shakes in agony, screaming into her gag, as the blood rushes back into her tortured flesh."
            wt_image ttf_bondage_1_9
            "She's panting heavily, and you give her a moment to recover before doing anything else."
            wt_image ttf_bondage_1_3
            $ title = "What now?"
            jump menu_tammy_lynn_bondage_menu
        "Flog her" if dungeon.has_item(floggers) and not tammy_lynn.has_tag('bondage_flogged') and not tammy_lynn.has_tag('clamped_now'):
            if tammy_lynn.has_tag('gagged_now'):
                wt_image ttf_bondage_1_9
                "You pick up a narrow leather strap as [tammy_lynn.name] stares wide-eyed at you."
                wt_image ttf_bondage_1_10
                "*thwaackkk*  ...  You land a preliminary swat on her buttocks that she barely reacts to know.  She knows full well that tied in this position, it's not her butt that's going to be the target."
                wt_image ttf_bondage_1_11
                "The target is her wide open and vulnerable sex, and that's where the next blow lands  ...  *thwaackkk*"
                wt_image ttf_bondage_1_12
                "This one she does react to, half-groaning, half-screaming into her gag."
                tammy_lynn.c "nnnnnnn"
                $ tammy_lynn.temporary_count = 1
                while tammy_lynn.temporary_count < 3:
                    $ tammy_lynn.temporary_count += 1
                    wt_image ttf_bondage_1_11
                    "*thwaackkk*"
                    wt_image ttf_bondage_1_12
                    tammy_lynn.c "nnnnnnn"
                $ title = "Strap her again?"
                menu menu_tammy_lynn_bondage_strapping_gagged_menu:
                    "Again":
                        $ tammy_lynn.temporary_count += 1
                        wt_image ttf_bondage_1_11
                        "*thwaackkk*"
                        wt_image ttf_bondage_1_12
                        if tammy_lynn.temporary_count < 10:
                            tammy_lynn.c "nnnnnnn"
                        elif tammy_lynn.temporary_count == 10:
                            tammy_lynn.c "NNNNNNNNN"
                            "She's no long half-groaning.  Those are now full throated screams into her gag, as much from the terror of where she's being strapped, as from the pain itself."
                        elif tammy_lynn.temporary_count == 20:
                            tammy_lynn.c "NNNNNNNNN"
                            "As uncomfortable as each blow is, it isn't doing her any actual harm.  With her pain tolerance, you could probably stand here strapping her pussy all day, if you wanted to."
                        else:
                            tammy_lynn.c "NNNNNNNNN"
                        jump menu_tammy_lynn_bondage_strapping_gagged_menu
                    "That's enough":
                        wt_image ttf_bondage_1_10
                        "*thwaackkk*  ...  The smack on her butt cheek almost feels good to [tammy_lynn.name], especially when she realizes it marks the end of having her pussy strapped."
                        tammy_lynn.c "mmmmmhh"
                        wt_image ttf_bondage_1_3
                        if tammy_lynn.temporary_count < 15:
                            change player energy by -energy_very_short
                        else:
                            change player energy by -energy_short
                        $ tammy_lynn.temporary_count = 0
                        jump menu_tammy_lynn_bondage_menu
            else:
                wt_image ttf_bondage_1_1
                "[tammy_lynn.name] looks at you in terror as you pick up a narrow leather strap."
                wt_image ttf_bondage_1_13
                tammy_lynn.c "Oh, no!!  Not there?!"
                wt_image ttf_bondage_1_14
                $ title = "How are you going to do this?"
                menu:
                    "Make her count":
                        add tags 'sub_counting' to tammy_lynn
                    "Just strap her pussy":
                        pass
                $ tammy_lynn.temporary_count = 0
                while tammy_lynn.temporary_count < 3:
                    $ tammy_lynn.temporary_count += 1
                    wt_image ttf_bondage_1_15
                    "*thwaackkk*"
                    wt_image ttf_bondage_1_16
                    if tammy_lynn.has_tag('sub_counting'):
                        tammy_lynn.c "OH OH OH OOOOOO!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                    else:
                        tammy_lynn.c "OH OH OH OOOOOO!!"
                wt_image ttf_bondage_1_14
                $ title = "Strap her again?"
                menu menu_tammy_lynn_bondage_strapping_menu:
                    "Again":
                        $ tammy_lynn.temporary_count += 1
                        wt_image ttf_bondage_1_15
                        "*thwaackkk*"
                        wt_image ttf_bondage_1_16
                        if tammy_lynn.temporary_count < 5:
                            if tammy_lynn.has_tag('sub_counting'):
                                tammy_lynn.c "OH OH OH OOOOOO!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                            else:
                                tammy_lynn.c "OH OH OH OOOOOO!!"
                        elif tammy_lynn.temporary_count == 5:
                            if tammy_lynn.has_tag('sub_counting'):
                                tammy_lynn.c "OH OH OH OOOOOO!!"
                                "She seems to have lost the ability to count.  That didn't take long."
                            else:
                                tammy_lynn.c "OH OH OH OOOOOO!!"
                        elif tammy_lynn.temporary_count < 10:
                            tammy_lynn.c "OH OH OH OOOOOO!!"
                        elif tammy_lynn.temporary_count < 20:
                            tammy_lynn.c "OOOOOO OOOWWWWW!!!"
                            "She's no long half-groaning.  She's now screaming at the top of her lungs, as much from the terror of where she's being strapped, as from the pain itself."
                        elif tammy_lynn.temporary_count == 20:
                            tammy_lynn.c "OOOOOO OOOWWWWW!!!"
                            "As uncomfortable as each blow is, it isn't doing her any actual harm.  With her pain tolerance, you could probably stand here strapping her pussy all day, if you wanted to."
                        else:
                            tammy_lynn.c "OOOOOO OOOWWWWW!!!"
                        wt_image ttf_bondage_1_14
                        jump menu_tammy_lynn_bondage_strapping_menu
                    "That's enough":
                        wt_image ttf_bondage_1_4
                        "Her head rolls to her side.  She's lost in a daze, her thoughts dominated by the raw, throbbing pain between her legs."
                        if tammy_lynn.temporary_count < 15:
                            change player energy by -energy_very_short
                        else:
                            change player energy by -energy_short
                        $ tammy_lynn.temporary_count = 0
                        jump menu_tammy_lynn_bondage_menu
        "Fuck her" if tammy_lynn.has_tag('threesomes_with_you') and not tammy_lynn.has_tag('clamped_now'):
            if tammy_lynn.has_tag('gagged_now'):
                if tammy_lynn.has_tag('bondage_flogged'):
                    wt_image ttf_bondage_1_17
                    "Heat radiates from [tammy_lynn.name]'s sex, an after-effect of the beating you gave her.  Her labia are bruised and raw and sensitive."
                    wt_image ttf_bondage_1_18
                    "Some women would find that enhances the sensation of being penetrated.  For [tammy_lynn.name], it just makes the no-[becky_sue.name] sex even more of a punishment than it otherwise would be."
                    wt_image ttf_bondage_1_19
                    "It's only a punishment for her, though."
                    player.c "[player.orgasm_text]"
                else:
                    wt_image ttf_bondage_1_17
                    "[tammy_lynn.name] accepts sexual contact with you in these circumstances as just another way for you to discipline her."
                    wt_image ttf_bondage_1_18
                    "Without [becky_sue.name]'s presence to arouse her, it feels very much like a form of punishment."
                    wt_image ttf_bondage_1_19
                    "Only for her, though."
                    player.c "[player.orgasm_text]"
            else:
                if tammy_lynn.has_tag('bondage_flogged'):
                    wt_image ttf_bondage_1_20
                    "Heat radiates from [tammy_lynn.name]'s sex as you press your cock against her, an after-effect of the beating you gave her.  Her labia are bruised and raw and sensitive."
                    wt_image ttf_bondage_1_21
                    "Some women would find that enhances the sensation of being penetrated.  For [tammy_lynn.name], it just makes the no-[becky_sue.name] sex even more of a punishment than it otherwise would be."
                    wt_image ttf_bondage_1_22
                    "It's only a punishment for her, though."
                    wt_image ttf_bondage_1_23
                    player.c "[player.orgasm_text]"
                else:
                    wt_image ttf_bondage_1_20
                    "[tammy_lynn.name] accepts sexual contact with you in these circumstances as just another way for you to discipline her."
                    wt_image ttf_bondage_1_21
                    "Without [becky_sue.name]'s presence to arouse her, it feels very much like a form of punishment."
                    wt_image ttf_bondage_1_22
                    "Only for her, though."
                    wt_image ttf_bondage_1_23
                    player.c "[player.orgasm_text]"
            wt_image ttf_bedroom_1_30
            "A [tammy_lynn.name] dresses sullenly after you untie her."
            tammy_lynn.c "I don't think I'd been bad enough to deserve that."
            wt_image ttf_bedroom_1_26
            player.c "Who decides when and how you're disciplined?"
            tammy_lynn.c "You do.  I'm sorry, [tammy_lynn.your_respect_name].  I didn't mean to back talk.  Of course you can do that to me.  I just hope you won't feel the need to, too often."
            $ tammy_lynn.sex_count += 1
            orgasm
        "That's enough" if tammy_lynn.has_tag('bondage_left') or tammy_lynn.has_tag('bondage_flogged') and not tammy_lynn.has_tag('clamped_now'):
            if tammy_lynn.has_tag('bondage_flogged'):
                wt_image ttf_bedroom_1_30
                "A still shaken [tammy_lynn.name] dresses after you untie her."
                tammy_lynn.c "My Daddy never whooped me that way when I was a girl, that's for sure!"
            else:
                wt_image ttf_bedroom_1_19
                "A sheepish [tammy_lynn.name] dresses after you untie her."
                tammy_lynn.c "I'll try to be good, [tammy_lynn.your_respect_name], so you don't feel the need to discipline me again in the future.  Except when you want to, I guess."
        "She can stay like that" if tammy_lynn.has_tag('bondage_left') and not tammy_lynn.has_tag('clamped_now'):
            add tags 'posing_now' 'posing_tied' to tammy_lynn
            $ tammy_lynn.change_image('ttf_bondage_1_1')
            wt_image tammy_lynn.image
            "She looks comfortable enough.  She can stay like that for a while."
    rem tags 'gagged_now' 'clamped_now' 'bondage_flogged' 'bondage_left'from tammy_lynn
    return

label tammy_lynn_check_on_her_machine:
    player.c "Follow me."
    wt_image ttf_bedroom_1_29
    tammy_lynn.c "Yes, [tammy_lynn.your_respect_name]."
    call forced_movement(dungeon) from _call_forced_movement_530
    summon tammy_lynn no_follows
    wt_image ttf_machine_1_1
    "You instruct her to undress while you set up the fuck machine."
    # first session
    if not tammy_lynn.has_tag('used_fuck_machine'):
        add tags 'used_fuck_machine' to tammy_lynn
        tammy_lynn.c "What is that?"
        player.c "A form of discipline, though one might even enjoy."
        wt_image ttf_machine_1_2
        "She gasps as you insert the business end of the machine inside her."
        wt_image ttf_machine_1_3
        tammy_lynn.c "No offense, but I don't like having a phallus inside me."
        "She might feel differently if [becky_sue.name] was the one inserting the phallus, and she may also feel differently once it starts running."
        wt_image ttf_machine_1_4
        "You turn the machine on ...  *thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "OH!!  What's it doing??!"
        player.c "Fucking you."
        wt_image ttf_machine_1_5
        "*thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "Does it cum inside me, too?"
        player.c "No.  That's just a dildo it's fucking you with, [tammy_lynn.name].  It works the same as any dildo, except for the moving in and out on it's own."
        wt_image ttf_machine_1_3
        "*thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "I've never had a dildo."
        player.c "What do you masturbate with?  Your fingers?"
        wt_image ttf_machine_1_5
        "*thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "What??  No!  That's gross."
        wt_image ttf_machine_1_3
        "She doesn't seem to be responding to the machine, so you increase the speed ..."
        wt_image ttf_machine_1_4
        "*thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "OH!"
        wt_image ttf_machine_1_3
        "Other than the gasp when the speed increased, the machine doesn't seem to be having much effect on her ...  *thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_6
        "She watches, curiously, as the machine pistons in-and-out of her, but it takes some time before she even starts to squirm her hips under it's assault ...  *thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_5
        "*thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "If the intent of this discipline is to make my pussy very sore, it's working, [tammy_lynn.your_respect_name]."
        wt_image ttf_machine_1_6
        "*thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        player.c "Do you want me to turn it off?"
        tammy_lynn.c "Yes, please, [tammy_lynn.your_respect_name].  I'll be good, I promise.  Please don't hurt my pussy any more."
        wt_image ttf_machine_1_4
        "She gasps one more time, this time in relief, as you shut the machine off and extract the dildo-head."
        tammy_lynn.c "OH!"
        wt_image ttf_machine_1_1
        tammy_lynn.c "Thank you for stopping that when I asked, [tammy_lynn.your_respect_name].  That was really feeling uncomfortable."
    # subsequent sessions
    else:
        tammy_lynn.c "That again?!"
        wt_image ttf_machine_1_2
        player.c "Yes, this again."
        wt_image ttf_machine_1_3
        tammy_lynn.c "I'm sorry, [tammy_lynn.your_respect_name].  I didn't mean to back talk.  It's just this device is so weird."
        wt_image ttf_machine_1_2
        "You start the machine on slow today ...  *thummmppp  thummmppp*"
        wt_image ttf_machine_1_4
        tammy_lynn.c "OH!"
        "... and gradually build up the speed ...  *thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_3
        "... watching for a reaction ...  *thummmppp  thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_2
        "... that never comes, even at top speed ...  *thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_6
        "... it's only after it's been running at top speed for almost fifteen minutes that she starts to squirm ...  *thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        wt_image ttf_machine_1_5
        "*thummmppp  thummmppp  thummmppp  thummmppp  thummmppp*"
        tammy_lynn.c "Please, [tammy_lynn.your_respect_name].  I don't think my pussy can take any more.  It's really hurting right now."
        wt_image ttf_machine_1_4
        "She sighs in relief as the machine stops."
        tammy_lynn.c "OH!  Finally!!"
        wt_image ttf_machine_1_1
        tammy_lynn.c "That is one nefarious device.  I'm going to be sore between my legs for a week, [tammy_lynn.your_respect_name]."
    change player energy by -energy_very_short
    return

label tammy_lynn_check_on_her_suspension:
    player.c "Follow me."
    wt_image ttf_bedroom_1_29
    tammy_lynn.c "Yes, [tammy_lynn.your_respect_name]."
    call forced_movement(dungeon) from _call_forced_movement_531
    summon tammy_lynn no_follows
    wt_image ttf_suspension_1_1
    "You lead her into your dungeon, where you have her undress ..."
    wt_image ttf_suspension_1_2
    "... and then tie and suspend her above the floor."
    $ title = "What now?"
    menu menu_tammy_lynn_suspension_menu:
        "Leave her there" if not tammy_lynn.has_tag('suspension_left'):
            add tags 'suspension_left' to tammy_lynn
            wt_image ttf_suspension_1_3
            "With [tammy_lynn.name] safely trussed up, you leave."
            call forced_movement(living_room) from _call_forced_movement_532
            wt_image current_location.image
            "You leave her hanging there for about an hour."
            call forced_movement(dungeon) from _call_forced_movement_533
            wt_image ttf_suspension_1_3
            "She barely reacts when you re-enter the dungeon.  She seems calm, even serene, in her bondage."
            wt_image ttf_suspension_1_2
            $ title = "What now?"
            jump menu_tammy_lynn_suspension_menu
        "Flog her" if dungeon.has_item(floggers) and not tammy_lynn.has_tag('suspension_flogged'):
            add tags 'suspension_flogged' to tammy_lynn
            wt_image ttf_suspension_1_4
            "Picking up a flogger, you move into position behind her."
            $ title = "How are you going to do this?"
            menu:
                "Make her count":
                    add tags 'sub_counting' to tammy_lynn
                "Just flog her":
                    pass
            $ tammy_lynn.temporary_count = 0
            while tammy_lynn.temporary_count < 3:
                $ tammy_lynn.temporary_count += 1
                wt_image ttf_suspension_1_5
                "**thwaappp**"
                wt_image ttf_suspension_1_6
                if tammy_lynn.has_tag('sub_counting'):
                    tammy_lynn.c "OOOO!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                else:
                    tammy_lynn.c "OOOO!!"
            wt_image ttf_suspension_1_7
            $ title = "Flog her again?"
            menu menu_tammy_lynn_suspension_flogging_menu:
                "Again":
                    $ tammy_lynn.temporary_count += 1
                    wt_image ttf_suspension_1_5
                    "**thwaappp**"
                    wt_image ttf_suspension_1_6
                    if tammy_lynn.has_tag('sub_counting'):
                        tammy_lynn.c "OOOO!!  That's [tammy_lynn.temporary_count.to_s], [tammy_lynn.your_respect_name]."
                    else:
                        tammy_lynn.c "OOOO!!"
                    wt_image ttf_suspension_1_7
                    if tammy_lynn.temporary_count == 10:
                        "You get the sense that hanging suspended in the air like this, rocking gently back and forth from each blow, [tammy_lynn.name] could take a flogging all day."
                    jump menu_tammy_lynn_suspension_flogging_menu
                "That's enough":
                    wt_image ttf_suspension_1_4
                    "You put the flogger away, while [tammy_lynn.name] waits to find out if that's it."
                    if tammy_lynn.temporary_count < 15:
                        change player energy by -energy_very_short
                    else:
                        change player energy by -energy_short
                    rem tags 'sub_counting' from tammy_lynn
                    $ tammy_lynn.temporary_count = 0
                    jump menu_tammy_lynn_suspension_menu
        "Fuck her" if tammy_lynn.has_tag('threesomes_with_you'):
            wt_image ttf_suspension_1_10
            "Even without [becky_sue.name] around, [tammy_lynn.name] doesn't object to you putting your cock in her."
            wt_image ttf_suspension_1_11
            "She understands that this type of sex is intended as a form of discipline, not pleasure."
            wt_image ttf_suspension_1_12
            "And without [becky_sue.name]'s presence to excite her ..."
            wt_image ttf_suspension_1_13
            "... it feels more like a punishment."
            wt_image ttf_suspension_1_12
            "Only for her, though."
            wt_image ttf_suspension_1_14
            player.c "[player.orgasm_text]"
            wt_image ttf_suspension_1_15
            "Relieved that her ordeal is finally over, [tammy_lynn.name] waits silently for your balls to finish pumping your seed into her and for you to let her down from her suspension."
            $ tammy_lynn.sex_count += 1
            orgasm
        "That's enough" if tammy_lynn.has_tag('suspension_left') or tammy_lynn.has_tag('suspension_flogged'):
            wt_image ttf_suspension_1_8
            "After you get her down, [tammy_lynn.name] gives you a goofy grin."
            wt_image ttf_suspension_1_9
            tammy_lynn.c "That was ... interesting, [tammy_lynn.your_respect_name]."
    rem tags 'suspension_flogged' 'suspension_left' from tammy_lynn
    dismiss tammy_lynn
    call forced_movement(living_room) from _call_forced_movement_534
    return

label tammy_lynn_check_on_her_nothing:
    pass
    return

label tammy_lynn_work_options_masseuse:
    add tags 'discussed_masseuse_job' to tammy_lynn
    player.c "How about doing massage work, like [becky_sue.name]?  The two of you could even work together sometimes, on the same client even."
    tammy_lynn.c "YUCK!  Touch somebody who isn't a close friend??  No way!"
    call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_44
    return

label tammy_lynn_work_options_studying:
    add tags 'discussed_studying' to tammy_lynn
    player.c "If you went back to school and finished your diploma, you'd have a lot more options for work."
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "I'm not as smart as Becky Sue, and even she finds the studying hard.  I'd just flunk out for sure."
    call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_45
    return

label tammy_lynn_work_options_avalon:
    add tags 'discussed_avalon_job' 'pizza_job_option_open' to tammy_lynn
    player.c "Some women support themselves selling Avalon products door-to-door.  Would you like to try that?"
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "When trailer trash walks up to some rich person's door, unless we're delivering something, they're more likely to call the cops than to let us in to try and sell them something."
    "Okay, door-to-door sales probably won't work, but maybe delivery work might?"
    call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_46
    return

label tammy_lynn_work_options_pizza:
    player.c "Do you know how to drive?"
    wt_image ttf_bedroom_1_24
    tammy_lynn.c "Totally!  I've been driving my daddy's truck since I was ten, and I couldn't even reach the brake pedal back then."
    "That's good enough for pizza delivery.  Plus you're pretty sure [tammy_lynn.name] won't have any qualms about cutting traffic safety corners to get the pizza there within the the guaranteed time frame."
    "She won't make a lot of money, but it'll be enough that you won't have to support her every week."
    $ title = "What do you think?"
    menu:
        "She should deliver pizzas":
            player.c "If I vouch for you, I can probably get you a job delivering pizzas."
            wt_image ttf_bedroom_1_9
            tammy_lynn.c "Cool!  Can I drive your car when I'm delivering them?"
            player.c "Definitely not.  But the company will supply you with a car for when you're on shift."
            wt_image ttf_bedroom_1_8
            tammy_lynn.c "Okay!  That sounds like fun.  Thanks!!"
            $ tammy_lynn.weekly_cost = 0
            $ tammy_lynn.job = "pizza"
            add tags 'earning_keep' 'pizza_delivery' 'late_night_job' to tammy_lynn
        "Consider other options":
            call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_47
    return

label tammy_lynn_work_options_yoga:
    player.c "What about yoga?"
    wt_image ttf_bedroom_1_6
    tammy_lynn.c "What about it?  You don't make money from doing yoga.  If you did, I'd be rich."
    player.c "You can if you lead classes."
    wt_image ttf_bedroom_1_9
    tammy_lynn.c "No one's going to want to listen to me give instructions.  I wouldn't even know how to teach someone how to do yoga.  Most of the moves I don't even know the names of."
    player.c "You don't need to.  You just lead the class, and everyone else watches you and tries to figure out what you're doing.  And for names, just make them up for each pose."
    wt_image ttf_bedroom_1_8
    tammy_lynn.c "You mean like 'drunken possum' or 'waterlogged snake'?"
    player.c "Sure.  People love to learn exotic yoga poses."
    wt_image ttf_bedroom_1_7
    tammy_lynn.c "These other people in the class, they'd all be watching me?  They wouldn't be allowed to touch me, would they?"
    player.c "Absolutely not!"
    wt_image ttf_bedroom_1_3
    tammy_lynn.c "You know, maybe I could do something like that.  Would people pay me very much to do yoga in front of them?"
    player.c "Probably not, but if I help you get on at a gym, you'd be able to get a class or two going pretty quickly."
    wt_image ttf_bedroom_1_9
    tammy_lynn.c "It sounds like it could be fun.  Do you think I should try it?"
    "She barely knows what she's doing and couldn't instruct at a proper yoga studio, but she could make a bit of money working at a general gym, enough that you won't have to support her every week."
    $ title = "What do you think?"
    menu:
        "She should teach yoga":
            wt_image ttf_bedroom_1_2
            tammy_lynn.c "This is going to be so great!"
            $ tammy_lynn.weekly_cost = 0
            $ tammy_lynn.job = "yoga"
            add tags 'earning_keep' 'yoga_instructor' to tammy_lynn
        "Consider other options":
            player.c "I'm not sure.  Let me think about it."
            call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_48
    return

label tammy_lynn_work_options_retail:
    add tags 'discussed_retail_job' to tammy_lynn
    player.c "What about a job working at a retail store?  Or a coffee shop?"
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "I don't know.  Becky Sue said that when she tried to get a job like that, the stores all told her she had to have a resume, whatever that is."
    wt_image ttf_bedroom_1_9
    tammy_lynn.c "Which is too bad, because if I did work at a store, Becky Sue could visit me and buy stuff, and then I could give my commissions to her so she could buy more stuff from me, and I bet pretty soon we could buy the whole store!"
    player.c "That resume thing is pretty much a showstopper, isn't it?"
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "Yeah, too bad."
    call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_49
    return

label tammy_lynn_work_options_maid:
    add tags 'discussed_maid_job' to tammy_lynn
    player.c "What about working as a maid?  You do a pretty good job when you clean up around here."
    wt_image ttf_bedroom_1_10
    tammy_lynn.c "Oh, no!  Becky Sue and I know girls from home who've worked in the city as maids.  Becky Sue says they all look like wizened apples by age thirty.  That's just her being dramatic, but she's not all wrong.  I don't want to end up like that."
    call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_50
    return

label tammy_lynn_work_options_bar:
    player.c "You spend a lot of time in bars.  What about working at one?"
    wt_image ttf_bedroom_1_24
    tammy_lynn.c "You mean, like as a bartender?"
    player.c "Maybe.  What do you know about different types of drinks?"
    wt_image ttf_bedroom_1_7
    tammy_lynn.c "Let's see, there's beer, whiskey, wine in various colors, shots in even more colors ..."
    player.c "What about mixing cocktails?"
    wt_image ttf_bedroom_1_28
    tammy_lynn.c "That thing people blow stuff up with in the movies?!  Are bartenders allowed to make them??!  COOL!!!"
    player.c "Those are Molotov ... You know what?  Maybe a server at a bar might be a better first step?"
    wt_image ttf_bedroom_1_9
    tammy_lynn.c "You actually think I should spend even more time in bars?  This is so awesome!"
    "If she did, she'd have even more access to booze during and after her shift, so you know darn well where most of her tips will go.  On the other hand, her base pay should at least be enough that you don't have to support her any more."
    if becky_sue.has_tag('virtuous'):
        "[becky_sue.name], however, won't be happy to find out you encouraged [tammy_lynn.name] to spend even more time at a drinking establishment."
    $ title = "What do you think?"
    menu:
        "She should work in a bar":
            wt_image ttf_bedroom_1_2
            tammy_lynn.c "This is so cool!!  I know exactly which bar I want to apply to.  I've been there twice and not gotten into a fight even once, so I think they'll hire me!"
            if becky_sue.has_tag('virtuous'):
                "[becky_sue.name] isn't happy with you, lowering the strength of your relationship with her, but [tammy_lynn.name] seems pretty pleased."
                $ becky_sue.relationship_counter += 1
            $ tammy_lynn.weekly_cost = 0
            $ tammy_lynn.job = "bar"
            add tags 'earning_keep' 'bar_server' 'late_night_job' to tammy_lynn
        "Consider other options":
            call expandable_menu(tammy_lynn_work_options_menu) from _call_expandable_menu_51
    return

label tammy_lynn_work_options_nothing:
    player.c "Let's talk about this later, after I've given it some thought."
    call expandable_menu(tammy_lynn_check_on_her_options_menu) from _call_expandable_menu_52
    return

label tammy_lynn_release_her:
    wt_image tammy_lynn.image
    "She's been here long enough.  Time to release her."
    rem tags 'posing_now' 'posing_discipline' 'posing_tied' 'posing_bedroom' 'posing_living_room' 'posing_outdoors' 'posing_casual' 'posing_challenging' 'posing_lewd' 'posing_yoga' from tammy_lynn
    call tammy_lynn_update_media from _call_tammy_lynn_update_media
    dismiss tammy_lynn
    call forced_movement(living_room) from _call_forced_movement_535
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Character
#label tammy_lynn_contact:  # not needed
#    pass
#    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_tammy_lynn:
    "You should save the butt plug for someone else."
    return

# Give Chastity Belt
label give_cb_tammy_lynn:
    if tammy_lynn.has_tag('no_porn_selfies'):
        "[tammy_lynn.name]'s already great at keeping people from getting between her legs.  It might help her kick her photography habit, but she seems to be controlling that on her own."
    elif tammy_lynn.has_tag('caught_on_phone'):
        "[tammy_lynn.name]'s already great at keeping people from getting between her legs.  All this would do is interfere with her photography."
    else:
        "[tammy_lynn.name]'s already great at keeping people from getting between her legs."
    return

# Give Dildo
label give_di_tammy_lynn:
    "Save this for someone else."
    return

# Use Fetch Toy
label use_ft_tammy_lynn:
    "Even a country hick isn't going to play that game with you."
    return

# Give Jewelry
label give_jwc_tammy_lynn:
    "Save this as a gift for [chelsea.name]."
    return

# Use Leash
label use_le_tammy_lynn:
    "You shouldn't try to take someone for a walk who isn't your pet."
    return

# Give Lingerie
label give_li_tammy_lynn:
    "You should save this for someone else."
    return

# Give Love Potion
label give_lp_tammy_lynn:
    "[tammy_lynn.name] already has a love potion-like infatuation with [becky_sue.name].  You doubt drinking this one would have any effect."
    return

# Give Transformation Potion
label give_tp_tammy_lynn:
    "[becky_sue.name] wouldn't approve."
    return

# Give Ring of Secuality
label give_rs_tammy_lynn:
    "She needs some help, that much is true.  Strangely enough, however, her sexuality is focussed so exclusively on [becky_sue.name], the ring won't change that."
    return


# Use Water Bowl
label use_wb_tammy_lynn:
    "Even country hicks don't drink out of bowls anymore."
    return

# Use Will Tamer
label use_wt_tammy_lynn:
    if tammy_lynn.has_tag('sub_for_you'):
        "Maybe someday, but not in this version of the game."
    else:
        "She'd look good in it, but you can't get her to wear it."
    return

########### TIMERS ###########
## Common Timers
# Start Day
label tammy_lynn_start_day:
    # note: her maintenance is combined with Becky Sue's in Becky Sue's start day label
    # initial move in conversaiton
    if day == 1 and tammy_lynn.has_tag('moving_in_conversation_pending'):
        call forced_movement(living_room) from _call_forced_movement_536
        summon tammy_lynn no_follows
        rem tags 'moving_in_conversation_pending' from tammy_lynn
        add tags 'living_with_you' 'first_day' to tammy_lynn
        wt_image ttf_initial_1
        "A happy looking [tammy_lynn.name] moves in on Monday."
        tammy_lynn.c "Thanks so much for letting me stay here!  This is awesome!!"
        $ tammy_lynn.temporary_count = 1
        while tammy_lynn.temporary_count == 1:
            $ title = "What do you say to her?"
            menu:
                "This is temporary" if not tammy_lynn.has_tag('initial_talk_temporary'):
                    add tags 'initial_talk_temporary' to tammy_lynn
                    wt_image ttf_initial_2
                    tammy_lynn.c "No problem!  I'm sure I'll figure out something I can do as a job soon, and then I'll be out of your hair."
                "Do you have any skills?" if tammy_lynn.has_tag('initial_talk_temporary') and not tammy_lynn.has_tag('initial_talk_skills'):
                    add tags 'initial_talk_skills' to tammy_lynn
                    wt_image ttf_initial_3
                    tammy_lynn.c "You mean like work skills?  Not really.  I dropped out of school a few months before Becky Sue did.  But there's lots of work in the city, right?  I'm sure now that I'm living here, I'll figure out a way to support myself soon."
                "Do you swear much?" if not tammy_lynn.has_tag('initial_talk_swearing'):
                    add tags 'initial_talk_swearing' to tammy_lynn
                    wt_image ttf_initial_4
                    if becky_sue.language < 2:
                        tammy_lynn.c "Are you kidding me?  With Becky Sue around, who could get a swear word in edgewise?"
                    else:
                        tammy_lynn.c "Are you kidding me?  With Becky Sue around, who could get a swear word in edgewise?  Although she seems to have cleaned up her act since she's been hanging out with you."
                "I hear you have the hots for my girlfriend" if not tammy_lynn.has_tag('initial_talk_bs'):
                    call tammy_lynn_initial_talk_bs from _call_tammy_lynn_initial_talk_bs
                "You like [becky_sue.name], don't you?" if not tammy_lynn.has_tag('initial_talk_bs'):
                    wt_image ttf_initial_4
                    tammy_lynn.c "So much!!  She's like my oldest and dearest friend!"
                    $ title = "What do you say?"
                    menu:
                        "You'd like [becky_sue.name] to be more than a friend":
                            call tammy_lynn_initial_talk_bs from _call_tammy_lynn_initial_talk_bs_1
                        "Drop this line of conversation":
                            pass
                "You dropped something" if not tammy_lynn.has_tag('initial_talk_dropped'):
                    add tags 'initial_talk_dropped' to tammy_lynn
                    wt_image ttf_initial_9
                    tammy_lynn.c "Sorry!  That must have fallen out of one of my bags.  I swear, I'm a tidy person.  I wiped my boots and everything before I came inside!  I won't make a mess of your house.  You won't even know I'm around."
                    wt_image ttf_initial_1
                "Make yourself at home" if not tammy_lynn.has_tag('initial_talk_home'):
                    add tags 'initial_talk_home' to tammy_lynn
                    wt_image ttf_initial_8
                    tammy_lynn.c "Thanks!  This is beyond amazing of you!!  I'll try not to get in your hair.  You won't even know I'm around."
                "Nothing more":
                    $ tammy_lynn.temporary_count = 0
                    wt_image ttf_initial_10
                    tammy_lynn.c "Becky Sue's helping move my stuff in.  I'd better go help before she has everything unpacked.  Bye!"
        $ living_room.connection_tlr = living_room.add_connection(tammy_lynn_room, condition = "tammy_lynn.has_tag('living_with_you') and living_room.is_empty", order = 70.35)
        $ tammy_lynn_room.connection_lr = tammy_lynn_room.add_connections(living_room)
        $ tammy_lynn.fixed_location = tammy_lynn_room
        $ tammy_lynn.location = tammy_lynn_room
        # this option added here, now that Becky Sue's name is established
        $ tammy_lynn.choice_check_on_her_becky_sue = tammy_lynn_check_on_her_options_menu.add_choice("Talk about [becky_sue.name]", "tammy_lynn_check_on_her_becky_sue")
        # this option added here so that it's last in the list, after the item above
        $ tammy_lynn.choice_check_on_her_nothing = tammy_lynn_check_on_her_options_menu.add_choice("Nothing else", "tammy_lynn_check_on_her_nothing")
    elif day == 1 and tammy_lynn.has_tag('living_with_you') and tammy_lynn.event_week < week:
        call tammy_lynn_living_with_you_events from _call_tammy_lynn_living_with_you_events
    return

label tammy_lynn_initial_talk_bs:
    add tags 'initial_talk_bs' to tammy_lynn
    wt_image ttf_initial_5
    tammy_lynn.c "What?!  Did Becky Sue say that??"
    player.c "No, [becky_sue.name] seems oblivious.  But it's pretty clear to me that you're in love, or at least in lust, with her."
    tammy_lynn.c "I'm ... that's not ...  I wouldn't ..."
    $ title = "What do you tell her?"
    menu:
        "Stay away from my girlfriend":
            player.c "I'm letting you stay here so I can keep an eye on you.  [becky_sue.name] is mine, and I'm not sharing her with you."
            tammy_lynn.c "Totally!!  I wouldn't ever try to get between you.  I promise!"
        "Relax, I'll help you":
            add tags 'seducing_friend' to tammy_lynn
            tammy_lynn.c "What do you mean, you'll help?  Help with what??"
            player.c "Help [becky_sue.name] to see you as a possible sex partner, not just a childhood friend.  You'd like that, wouldn't you?"
            wt_image ttf_initial_6
            "The look on her face is the only affirmation you need."
            tammy_lynn.c "But why??"
            player.c "I know you're from the country, but you're not that naive, are you?  I just need to know one more thing: if I help you to have a more intimate relationship with [becky_sue.name], you'll be grateful to me, won't you?"
            wt_image ttf_initial_7
            tammy_lynn.c "Well, yeah.  I guess.  But she's not into girls."
            player.c "Between the two of us, we may be able to change that."
        "It's okay, I'm not mad":
            wt_image ttf_initial_3
            tammy_lynn.c "There's really nothing between us.  I mean, other than friendship."
            player.c "I know.  I also know you wish it were otherwise, but [becky_sue.name] doesn't see you the way you see her.  I'm not mad at you.  You can't help the way you feel."
            tammy_lynn.c "Seriously, she's like my oldest and dearest friend.  I'm totally happy with our relationship just the way it is."
            "If that's her coping mechanism, best to let her keep saying that to herself."
    return

label tammy_lynn_living_with_you_events:
    $ tammy_lynn.training_session()
    $ tammy_lynn.event_outfit += 1
    if tammy_lynn.event_outfit > 8:
        $ tammy_lynn.event_outfit = 1
    # NOTE: purposefully all "ifs" to facilitate scrolling past inapplicble events
    # cleaning up
    # food
    if tammy_lynn.event_outfit == 1:
        $ tammy_lynn.food_outfit += 1
        if tammy_lynn.food_outfit > 2:
            $ tammy_lynn.food_outfit = 1
        # banana
        if tammy_lynn.food_outfit == 1:
            wt_image ttf_banana_1_1
            "[tammy_lynn.name] is wandering through the house, eating a banana."
            player.c "Enjoying my food?"
            wt_image ttf_banana_1_2
            if tammy_lynn.has_tag('earning_keep'):
                tammy_lynn.c "Hey, I bought these bananas!  I'm working now, remember?"
            else:
                tammy_lynn.c "Yeah, these bananas are great!  Thanks for buying them."
        # apple
        else:
            wt_image ttf_apple_1_1
            "[tammy_lynn.name] is chowing down on an apple."
            wt_image ttf_apple_1_2
            player.c "Enjoying my food?"
            wt_image ttf_apple_1_3
            if tammy_lynn.has_tag('earning_keep'):
                tammy_lynn.c "Technically I bought it, with the money I'm making.  But you can have a bite, if you want.  It's delicious."
            else:
                tammy_lynn.c "Yeah, it's delicious.  Wanna a bite?"
            $ title = "What do you do?"
            menu:
                "Take a bite":
                    wt_image ttf_apple_1_4
                    tammy_lynn.c "Good, isn't it?  I'd better go get another, since you ate half of this one."
                "Pass":
                    wt_image ttf_apple_1_5
                    tammy_lynn.c "I was only eating from this side, see?  I wasn't trying to give you cooties."

    # NEED consider games night events

    # toilet event chain
    if tammy_lynn.event_outfit == 2:
        if not tammy_lynn.has_tag('no_toilet_events'):
            call forced_movement(bathroom) from _call_forced_movement_537
            summon tammy_lynn
            # first event
            if tammy_lynn.toilet_count == 0:
                wt_image ttf_toilet_1_1
                "You step into your master bathroom, to discover [tammy_lynn.name] using it."
                tammy_lynn.c "SHIT!!  Occupied!"
                player.c "What are you doing in this bathroom???"
                tammy_lynn.c "It was the closest one!"
                $ title = "What's your reaction to seeing her sitting there?"
                menu:
                    "Hot":
                        tammy_lynn.c "Umm, could you leave now??"
                        "You do, but not before she realizes you're taking a good look at her."
                        $ tammy_lynn.caught_you_watching += 1
                        $ tammy_lynn.toilet_count += 1
                    "Gross (shuts off this event)":
                        add tags 'no_toilet_events' to tammy_lynn
                        player.c "Stay out of our bathroom from now on.  There's a guest bathroom you can use."
                        tammy_lynn.c "I will!!  Sorry."
            # subsequent events
            elif tammy_lynn.toilet_count > 0:
                wt_image ttf_toilet_2_1
                "You walk in on [tammy_lynn.name] using your bathroom again.  She's so engrossed in her phone, she doesn't hear you at first."
                wt_image ttf_toilet_2_2
                # intro options
                if tammy_lynn.has_tag('caught_on_phone'):
                    "From the grin on her face, you can guess what she's up to."
                    player.c "Seriously?  In my bathroom?"
                else:
                    "You watch her for a few minutes, until she realizes you're there."
                # her reaction options
                if tammy_lynn.has_tag('no_porn_selfies'):
                    wt_image ttf_toilet_2_3
                    tammy_lynn.c "SHIT!!"
                    wt_image ttf_toilet_2_4
                    tammy_lynn.c "This isn't what it looks like, [tammy_lynn.your_respect_name].  I was only looking at a few photos, not posting any of my own!"
                    player.c "That's still a bad habit.  Stop it."
                    if tammy_lynn.has_tag('accepts_watersports'):
                        tammy_lynn.c "I'll try."
                    else:
                        tammy_lynn.c "I'll try.  Why were you watching me in the bathroom?"
                elif tammy_lynn.has_tag('accepts_watersports'):
                    wt_image ttf_toilet_2_11
                    if tammy_lynn.has_tag('caught_on_phone'):
                        tammy_lynn.c "Oh, hey!  Yeah, I'm being bad."
                    else:
                        tammy_lynn.c "Oh, hey!  Sorry, just finishing up something here."
                else:
                    wt_image ttf_toilet_2_3
                    tammy_lynn.c "SHIT!!  What are you doing there?"
                # your action options
                if tammy_lynn.has_tag('accepts_watersports'):
                    tammy_lynn.c "I haven't done anything, yet, I was busy with my phone.  Do you want to watch me while I pee?"
                    $ title = "Do you?"
                    menu:
                        "Yes":
                            wt_image ttf_toilet_2_6
                            tammy_lynn.c "Lemme put my phone down."
                            wt_image ttf_toilet_2_7
                            "As she does, she squats over the toilet, her legs spread wide to give you a good view."
                            wt_image ttf_toilet_2_8
                            "It only takes a moment for the liquid to begin to flow ..."
                            wt_image ttf_toilet_2_9
                            "... and the pour out of her in a flood."
                            wt_image ttf_toilet_2_6
                            tammy_lynn.c "That's all of it."
                            wt_image ttf_toilet_2_10
                            "She wipes herself off and you go on with your day."
                            change player energy by -energy_very_short
                        "No":
                            wt_image ttf_toilet_2_2
                            if tammy_lynn.has_tag('no_porn_selfies'):
                                tammy_lynn.c "Okay, I'll be done in a moment.  And I'll stay away from those sites, I promise."
                            else:
                                tammy_lynn.c "Okay, I'll be done in a moment."
                else:
                    $ title = "What do you say?"
                    menu:
                        "Watching you":
                            wt_image ttf_toilet_2_5
                            tammy_lynn.c "Why???"
                        "Waiting for you to finish":
                            wt_image ttf_toilet_2_5
                            tammy_lynn.c "You could wait outside!  Why are you standing here watching me?"
                        "Kicking you out (shuts off this event)":
                            add tags 'no_toilet_events' to tammy_lynn
                            wt_image ttf_toilet_2_5
                            tammy_lynn.c "Of the house?!"
                            player.c "Tempting, but for now just out of my bathroom.  There's a bathroom just down the hall for your use.  You can hold it the ten extra steps it takes.  Stay out of my bathroom from now on."
                            wt_image ttf_toilet_2_4
                            tammy_lynn.c "Okay"
                    # continue if not shut off
                    if not tammy_lynn.has_tag('no_toilet_events'):
                        $ title = "Why are you watching her?"
                        menu:
                            "It's hot":
                                if tammy_lynn.has_tag('exhibitionist_for_you') or tammy_lynn.has_tag('hypno_re_watersports'):
                                    wt_image ttf_toilet_2_4
                                    tammy_lynn.c "Really??"
                                    player.c "Yes.  I want to watch you using the toilet."
                                    add tags 'accepts_watersports' to tammy_lynn
                                elif tammy_lynn.has_tag('sub_for_you'):
                                    wt_image ttf_toilet_2_4
                                    tammy_lynn.c "Really, [tammy_lynn.your_respect_name]??"
                                    player.c "Yes.  I want to watch you using the toilet."
                                    add tags 'accepts_watersports' to tammy_lynn
                                else:
                                    $ tammy_lynn.toilet_count = 2
                                    wt_image ttf_toilet_2_3
                                    tammy_lynn.c "It's hot seeing me use the toilet??  Eewww!  Can we NOT be having this conversation!!"
                                    "For now, you leave her alone."
                            "I'm considering peeing on you" if tammy_lynn.has_tag('sub_for_you'):
                                wt_image ttf_toilet_2_3
                                tammy_lynn.c "Oh no!!  I haven't agreed to that type of discipline!"
                                "Maybe not yet, but if you get her used to peeing for you, you may be able to break down that barrier."
                                $ tammy_lynn.toilet_count = 3
                            "No reason":
                                wt_image ttf_toilet_2_4
                                tammy_lynn.c "You're weird sometimes, you know that.  Can I have some privacy now?"
                    # continue further to first peeing if she agreed
                    if tammy_lynn.has_tag('accepts_watersports'):
                        wt_image ttf_toilet_2_4
                        tammy_lynn.c "How do I do that?"
                        player.c "Very naturally.  Pull your pants and panties off all the way and spread your legs wider so I can see.  Then let yourself go."
                        wt_image ttf_toilet_2_6
                        tammy_lynn.c "I can't do this while I'm looking at you."
                        wt_image ttf_toilet_2_7
                        "Turning around to face away from you, she squats over the toilet.  Then you both wait."
                        wt_image ttf_toilet_2_8
                        "Right about when you think she's not going to be able to do anything, there's a trickle ..."
                        wt_image ttf_toilet_2_9
                        "... and then a flood."
                        wt_image ttf_toilet_2_6
                        tammy_lynn.c "I did it!"
                        wt_image ttf_toilet_2_10
                        "She seems pleased with herself as she wipes herself off.  You've taught her a new kink."
                        change player energy by -energy_very_short
        else:
            $ tammy_lynn.event_outfit += 1

    # cleaning or 'cooking'
    if tammy_lynn.event_outfit == 3:
        $ tammy_lynn.kitchen_outfit += 1
        if tammy_lynn.kitchen_outfit > 2:
            $ tammy_lynn.kitchen_outfit = 1
        call forced_movement(kitchen) from _call_forced_movement_538
        summon tammy_lynn
        # cleaning
        if tammy_lynn.kitchen_outfit == 1:
            wt_image ttf_cleaning_1_1
            # first time
            if not tammy_lynn.has_tag('watched_her_do_yoga'):
                $ tammy_lynn.temporary_count = 0
                add tags 'watched_her_clean' to tammy_lynn
                "You spot [tammy_lynn.name] cleaning up the kitchen."
                wt_image ttf_cleaning_1_2
                player.c "That's good of you.  I rarely see [becky_sue.name] cleaning up."
                tammy_lynn.c "Becky Sue??  I don't think she even knows how to use a broom."
                if becky_sue.weekend_cleaning_count > 0:
                    player.c "She does.  I've seen her use it."
                    wt_image ttf_cleaning_1_3
                    tammy_lynn.c "Really? I wouldn't have thought that possible, even if you paid her."
                wt_image ttf_cleaning_1_4
                tammy_lynn.c "Anyway, I don't like using a broom, either, but if you stay out of my way, I'll give the vacuum cleaner a go."
                "Far be it from you to interrupt [tammy_lynn.name] while she's trying to make herself useful for a change.  You leave her alone to do some cleaning."
            # option if watersports active
            elif tammy_lynn.has_tag('accepts_watersports'):
                "[tammy_lynn.name]'s cleaning up in the kitchen."
                $ title = "What do you do?"
                menu:
                    "Let her clean":
                        $ tammy_lynn.temporary_count = 1
                    "Tell her to make a mess":
                        $ tammy_lynn.temporary_count = 0
                        wt_image ttf_cleaning_1_3
                        tammy_lynn.c "Seriously?  Here in the kitchen?"
                        $ title = "What do you tell her?"
                        menu:
                            "Yes":
                                player.c "Yes, up on the counter where I can have a good look."
                                wt_image ttf_toilet_6_1
                                tammy_lynn.c "I can't believe what you've turned me into."
                                wt_image ttf_toilet_6_2
                                "It appears you've turned her into the sort of woman who will flood your kitchen with her urine while you watch."
                                wt_image ttf_toilet_6_3
                                tammy_lynn.c "Tell me what you think I am."
                                $ title = "What do you think she is?"
                                menu:
                                    "An amazing woman":
                                        pass
                                    "A disgusting pig":
                                        pass
                                wt_image ttf_toilet_6_4
                                "She listens to your commentary quietly as finishes doing number one all over your kitchen counter."
                                change player energy by -energy_very_short
                            "Maybe not":
                                wt_image ttf_cleaning_1_2
                                tammy_lynn.c "Yeah, I think that's a good decision."
            # default
            else:
                $ tammy_lynn.temporary_count = 1
                "[tammy_lynn.name]'s cleaning up in the kitchen."
            # main content
            if tammy_lynn.temporary_count == 1:
                $ tammy_lynn.temporary_count = 0
                if tammy_lynn.has_tag('exhibitionist_for_you') and tammy_lynn.has_tag('watched_her_clean'):
                    wt_image ttf_cleaning_1_2
                    "She grins when she sees you ..."
                    wt_image ttf_cleaning_1_5
                    "... and wiggles her hips until her pants slip down."
                    wt_image ttf_cleaning_1_6
                    "It's a bit of a silly sight ..."
                    wt_image ttf_cleaning_1_7
                    "... especially when she finishes washing the dishes, and takes out the vacuum cleaner."
                    wt_image ttf_cleaning_1_8
                    "[tammy_lynn.name] seems to realize that ..."
                    wt_image ttf_cleaning_1_9
                    "... as she pulls up her pants and pulls down her top ..."
                    wt_image ttf_cleaning_1_10
                    "... and finishes the vacuuming like this, while you watch."
                elif tammy_lynn.has_tag('watched_her_clean'):
                    wt_image ttf_cleaning_1_2
                    "She grins when she sees you."
                    wt_image ttf_cleaning_1_3
                    if becky_sue.has_tag('earning_keep'):
                        tammy_lynn.c "I'm trying to still be helpful around here, even though I have a job now."
                    else:
                        tammy_lynn.c "I'm trying to help out around here.  I know I'm still not making any money, but I'm trying to pitch in when I can."
                    wt_image ttf_cleaning_1_4
                    "You try and stay out of her way as she gets the vacuum cleaner out.  You don't want to interrupt her burst of productivity."
        # cupcakes
        else:
            wt_image ttf_cupcakes_1_1
            if not tammy_lynn.has_tag('cupcakes_event'):
                add tags 'cupcakes_event' to tammy_lynn
                "You find [tammy_lynn.name] in the kitchen."
                tammy_lynn.c "I'm making cupcakes for Becky Sue!"
                wt_image ttf_cupcakes_1_2
                player.c "I didn't know you could bake."
                wt_image ttf_cupcakes_1_3
                tammy_lynn.c "Bake??  Why would I need to bake?  I just scrap off the yucky store icing and pour beer on the cupcakes so they taste good.  Then I add canned whipped cream - which is the best! - and color it with shot liqueurs."
                wt_image ttf_cupcakes_1_4
                tammy_lynn.c "Want to try one?"
                player.c "Maybe later."
            else:
                "[tammy_lynn.name]'s in the kitchen again."
                tammy_lynn.c "I'm making more cupcakes for Becky Sue!"
                wt_image ttf_cupcakes_1_5
                player.c "Dressed like that?"
                if becky_sue.has_tag('exhibitionist_for_you'):
                    wt_image ttf_cupcakes_1_6
                    tammy_lynn.c "It is pretty warm to be working in the kitchen."
                    wt_image ttf_cupcakes_1_7
                    tammy_lynn.c "... 'butt' this outfit is pretty cooling."
                    wt_image ttf_cupcakes_1_8
                    tammy_lynn.c "And not just from behind, either."
                    wt_image ttf_cupcakes_1_9
                    tammy_lynn.c "And if ever I still felt too warm, I'm sure I could figure something out."
                    wt_image ttf_cupcakes_1_10
                    "She goes back to preparing her special take on cupcakes, and you go on with your day."
                elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                    wt_image ttf_cupcakes_1_6
                    tammy_lynn.c "It is pretty warm to be working in the kitchen ..."
                    wt_image ttf_cupcakes_1_7
                    tammy_lynn.c "... 'butt' this outfit is pretty cooling."
                    wt_image ttf_cupcakes_1_4
                    tammy_lynn.c "Cupcake?"
                    player.c "Are these made the way you did before?"
                    wt_image ttf_cupcakes_1_2
                    tammy_lynn.c "Of course!  Becky Sue and I love them like this!!"
                    player.c "You two enjoy them, then.  I don't want to take them away from you.  I'll get myself something else for a snack."
                else:
                    wt_image ttf_cupcakes_1_3
                    tammy_lynn.c "What's wrong with the way I'm dressed?"
                    wt_image ttf_cupcakes_1_2
                    player.c "Nothing, I guess."
                    wt_image ttf_cupcakes_1_4
                    tammy_lynn.c "Cupcake?"
                    player.c "Are these made the way you did before?"
                    wt_image ttf_cupcakes_1_2
                    tammy_lynn.c "Of course!  Becky Sue and I love them like this!!"
                    player.c "You two enjoy them, then.  I don't want to take them away from you.  I'll get myself something else for a snack."

    # passed out or jail
    if tammy_lynn.event_outfit == 4:
        if tammy_lynn.has_tag('earning_keep'):
            if tammy_lynn.has_tag('late_night_job'):
                wt_image ttf_drunk_1_1
                "[tammy_lynn.name] is passed out on your sofa, again.  At least this time, it's because she was out all night working a late shift, rather than just getting shit-faced."
                wt_image ttf_drunk_1_2
                "Rather than wake her, you ask [becky_sue.name] to get her off the sofa and into her bedroom.  [tammy_lynn.name] never minds being woken, or man-handled, by [becky_sue.name]."
            else:
                # if she has a job but it doesn't require her to work late nights, this scrolls to the next event, skipping this one
                $ tammy_lynn.event_outfit += 1
        elif tammy_lynn.has_tag('no_more_drunk_nights'):
            $ tammy_lynn.event_outfit += 1
        else:
            if tammy_lynn.has_tag('jail_next'):
                rem tags 'jail_next' from tammy_lynn
                add tags 'jail_before' to tammy_lynn
                wt_image phone_1
                "You receive a call from [tammy_lynn.name].  She was out drinking last night, and ended up in the drunk tank at the local jail."
                "It'll take time and effort to go get her, but [becky_sue.name] will be happy with you for helping out her friend."
                $ title = "What do you do?"
                menu:
                    "Go to the jail (costs [energy_short.value] energy)":
                        $ tammy_lynn.temporary_count = 1
                        call forced_movement(outdoors) from _call_forced_movement_539
                        summon tammy_lynn
                        wt_image ttf_jail_1_1
                        "A sheepish [tammy_lynn.name] is at least sober enough to stand up when you get there."
                        wt_image ttf_jail_1_2
                        tammy_lynn.c "Thanks for coming to get me.  I don't feel well and need to get out of here."
                        $ title = "Talk to her?"
                        menu:
                            "Yes":
                                player.c "Care to tell me why you ended up here in the first place?"
                                wt_image ttf_jail_1_3
                                if becky_sue.has_tag('virtuous'):
                                    tammy_lynn.c "It's Becky Sue's fault!  She rarely wants to get shit-faced with me anymore.  I need her as my wingman to keep me out of trouble when I start drinking.  Otherwise, guys start hitting on me, instead of hitting on her."
                                else:
                                    tammy_lynn.c "It's Becky Sue's fault!  Since she started dating you, she rarely flirts with guys anymore when we're out drinking.  That means they flirt with me, instead of ignoring me and pawing at Becky Sue."
                                player.c "That doesn't explain why you got hauled in to jail.  Did you get so drunk you couldn't find your way home?"
                                wt_image ttf_jail_1_4
                                tammy_lynn.c "I think it had more to do with the guy I clobbered after he got too friendly with me."
                                player.c "Great.  So now you'll be charged with assault."
                                wt_image ttf_jail_1_5
                                tammy_lynn.c "Charged??  Why would I be charged?"
                                player.c "For punching someone."
                                wt_image ttf_jail_1_6
                                tammy_lynn.c "Get real.  Look at me.  What guy is going to testify in public that I floored him after he grabbed my ass?  Can we go now?"
                                "It'd be a waste of time and would accomplish nothing, but on principle you could leave her until the cops decide to let her go.  Or you can earn [becky_sue.name]'s gratitude by talking to the cops and getting them to release [tammy_lynn.name] now."
                                $ title = "Take her home?"
                                menu:
                                    "Yes":
                                        pass
                                    "No":
                                        $ tammy_lynn.temporary_count = 0
                                        wt_image ttf_jail_1_7
                                        tammy_lynn.c "No??  Whadda you mean, no?"
                                        player.c "You need to learn some self-control, [tammy_lynn.name].  Running around all hours of the night, getting shit-faced, starting fights.  It's time to grow up.  Maybe some time in jail will help."
                                        wt_image ttf_jail_1_8
                                        "She's pissed, in both senses of the term.  The cops don't keep her long.  Later that day, aftr confirming the guy she hit did not, in fact, want to press charges, they let her go.  But for now, you at least have the satisfaction of going home, leaving her behind bars to contemplate her life choices."
                            "No, just take her home":
                                pass
                        # if take her home
                        if tammy_lynn.temporary_count == 1:
                            $ tammy_lynn.temporary_count = 0
                            wt_image ttf_jail_1_9
                            tammy_lynn.c "Thanks!  I gotta get to a toilet, first.  I don't wanna puke all over your car on the drive home."
                            "You're thankful for that, [becky_sue.name] is thankful you got [tammy_lynn.name] out of there."
                            $ becky_sue.relationship_counter += 1
                        change player energy by -energy_short
                    "Leave her there":
                        "Some time in the drunk tank might knock some sense into [tammy_lynn.name], but probably not.  Regardless, they let her go later that day anyway, and she slinks home embarassed, but noen the worse for wear."
            else:
                call forced_movement(living_room) from _call_forced_movement_540
                summon tammy_lynn
                add tags 'jail_next' to tammy_lynn
                if tammy_lynn.has_tag('jail_before'):
                    wt_image ttf_drunk_1_1
                    "[tammy_lynn.name] was out drinking last night.  It seems her time in the drunk tank taught her nothing, as she's passed out on your sofa, again."
                else:
                    wt_image ttf_drunk_1_1
                    "It seems [tammy_lynn.name] was out drinking last night, and overdid it.  You find her passed out on the sofa in the morning."
                $ title = "What do you do?"
                menu:
                    "Wake her":
                        wt_image ttf_drunk_1_5
                        tammy_lynn.c "What?  What is it??"
                        player.c "Time for you to get up."
                        wt_image ttf_drunk_1_4
                        tammy_lynn.c "Shit, you scared me."
                        wt_image ttf_drunk_1_6
                        player.c "I'm sure it's a shock, getting woken up before noon."
                        if tammy_lynn.has_tag('exhibitionist_for_you'):
                            wt_image ttf_drunk_1_8
                            tammy_lynn.c "The shock is discovering I fell asleep in this bra and it's been digging into my ribs all night."
                            wt_image ttf_drunk_1_9
                            tammy_lynn.c "Ahhhh ... that feels a bit better."
                            wt_image ttf_drunk_1_10
                            tammy_lynn.c "I hope you have a beer in your fridge.  I need hair of the dog, pronto."
                        else:
                            wt_image ttf_drunk_1_7
                            tammy_lynn.c "The shock will be if I discover there's no beer left in your fridge.  I need hair of the dog, pronto."
                    "Wait for her to wake up":
                        wt_image ttf_drunk_1_2
                        "She's just starting to sober up.  She tosses and turns for a while ..."
                        wt_image ttf_drunk_1_3
                        "... then eventually opens her eyes."
                        wt_image ttf_drunk_1_4
                        tammy_lynn.c "Ugghhh.  I don't feel so good."
                        wt_image ttf_drunk_1_5
                        tammy_lynn.c "What time is it?"
                        $ title = "What time is it?"
                        menu:
                            "Time for her to get a job":
                                wt_image ttf_drunk_1_6
                                tammy_lynn.c "Seriously?  My head's frigging pounding and you want to rag on me now about finding a job?"
                                player.c "Aren't you a bit concerned that you're spending more time partying than you are figuring out how you're going to support yourself?"
                            "Time for her to grow up":
                                wt_image ttf_drunk_1_6
                                tammy_lynn.c "Seriously?  My head's frigging pounding and you want to rag on me 'cus I had a good time last night?"
                                player.c "Aren't you a bit concerned that at your age, you still think getting pass out drunk is a good time?"
                            "10, now tell me if that's am or pm":
                                wt_image ttf_drunk_1_6
                                tammy_lynn.c "Ha ha.  A.m., right?"
                                player.c "Aren't you a bit concerned that even with the sun shining through the window, you're not 100% certain?"
                        if tammy_lynn.has_tag('exhibitionist_for_you'):
                            wt_image ttf_drunk_1_8
                            tammy_lynn.c "What I'm concerned about right now is that I fell asleep in this bra and it's been digging into my ribs all night."
                            wt_image ttf_drunk_1_9
                            tammy_lynn.c "Ahhhh ... that feels a bit better."
                            wt_image ttf_drunk_1_10
                            tammy_lynn.c "I hope you have a beer in your fridge.  I need hair of the dog, pronto."
                        else:
                            wt_image ttf_drunk_1_7
                            tammy_lynn.c "The only thing I'm concerned about is that there may not be any beer in your fridge.  I need hair of the dog, pronto."
                    "Put an end to this late night drinking" if tammy_lynn.has_tag('sub_for_you'):
                        player.c "Wake up!"
                        wt_image ttf_drunk_1_5
                        tammy_lynn.c "What?  What is it??"
                        player.c "The last time you're doing this."
                        wt_image ttf_drunk_1_3
                        tammy_lynn.c "The last time I'm doing what?"
                        player.c "Staying out late, getting drunk, and passing out on my sofa.  It stops now."
                        wt_image ttf_drunk_1_6
                        tammy_lynn.c "I'm just having some fun."
                        player.c "You're drinking your life away, getting into fights, and getting thrown in jail.  I'm not going to let you do that any more."
                        wt_image ttf_drunk_1_8
                        tammy_lynn.c "Look, it's my life ..."
                        player.c "You're grounded."
                        wt_image ttf_drunk_1_7
                        tammy_lynn.c "What?!"
                        player.c "You agreed to accept my discipline.  From now on you're home by 10 pm, and you come home sober."
                        tammy_lynn.c "I'm not a teenager."
                        player.c "You're not an adult, either.  At least you aren't acting like one.  When you start acting like one I'll consider letting you go out at nights again.  Until then, 10 pm's your curfew."
                        wt_image ttf_drunk_1_4
                        "She collapses back on the sofa in disbelief.  Notably, she doesn't argue."
                        add tags 'no_more_drunk_nights' to tammy_lynn
                    "Leave her":
                        "You have better things to do than deal with [tammy_lynn.name] right now.  You ask [becky_sue.name] to get her drunk friend to her bedroom and go on with your day."

    # pool
    if tammy_lynn.event_outfit == 5:
        if not tammy_lynn.has_tag('no_pool_events'):
            call forced_movement(backyard) from _call_forced_movement_541
            summon tammy_lynn
            wt_image ttf_pool_1_1
            "[tammy_lynn.name] doesn't spend much time at the pool, especially not compared to [becky_sue.name], but she's headed there today."
            wt_image ttf_pool_1_2
            $ title = "Approach her?"
            menu:
                "Yes":
                    # full exhibitionism
                    if tammy_lynn.has_tag('exhibitionist_for_you'):
                        wt_image ttf_pool_1_13
                        tammy_lynn.c "Oh, hey!  What a hell of a nice day!  I was just going to do some sunbathing.  Are you staying?"
                        $ title = "Are you?"
                        menu:
                            "Yes":
                                wt_image ttf_pool_1_14
                                tammy_lynn.c "It's hotter than I realized out here."
                                wt_image ttf_pool_1_15
                                "You're not sure how much her apparent solution is going to cool her down ..."
                                wt_image ttf_pool_1_19
                                "... but there's no harm in letting her try."
                                wt_image ttf_pool_1_20
                                "Now naked ..."
                                wt_image ttf_pool_1_21
                                "... [tammy_lynn.name] goes back to her sunbathing ..."
                                wt_image ttf_pool_1_22
                                "... warming her back in the heat of the sun."
                                wt_image ttf_pool_1_23
                                "Then she turns over again ..."
                                wt_image ttf_pool_1_24
                                "... and gives her front the same treatment."
                                wt_image ttf_pool_1_25
                                "When you've seen your fill, you leave her to her sunbathing and go on with your day."
                                change player energy by -energy_very_short
                            "No":
                                wt_image ttf_pool_1_9
                                "You go on with your day and [tammy_lynn.name] goes back to her sunbathing."
                    # partial exhibitionism
                    elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                        if not tammy_lynn.has_tag('watched_at_pool'):
                            wt_image ttf_pool_1_4
                            tammy_lynn.c "Oh, hey!  You have a really awesome place here.  It's really nice of you to let me make use of it."
                            wt_image ttf_pool_1_5
                            tammy_lynn.c "I'm just gonna catch some 'rays."
                            wt_image ttf_pool_1_6
                            "She settles in ..."
                            wt_image ttf_pool_1_7
                            "... then realizes you're still watching her."
                            wt_image ttf_pool_1_12
                            $ title = "Keep watching?"
                            menu:
                                "Yes":
                                    wt_image ttf_pool_1_13
                                    tammy_lynn.c "It's hotter than I realized out here."
                                    wt_image ttf_pool_1_14
                                    "You're not sure how much her apparent solution is going to cool her down ..."
                                    wt_image ttf_pool_1_15
                                    "... but there's no harm in letting her try."
                                    wt_image ttf_pool_1_16
                                    "Now topless ..."
                                    wt_image ttf_pool_1_17
                                    "... [tammy_lynn.name] goes back to her sunbathing."
                                    wt_image ttf_pool_1_18
                                    "As suspected, her solution did little to keep the hot sun from raising a sweat, but it made your day a little brighter before you move on."
                                    add tags 'watched_at_pool' to tammy_lynn
                                    # one-time boost to this
                                    $ tammy_lynn.caught_you_watching += 1
                                    change player energy by -energy_very_short
                                "No":
                                    wt_image ttf_pool_1_10
                                    "You go on with your day and [tammy_lynn.name] goes back to her sunbathing."
                        else:
                            wt_image ttf_pool_1_4
                            tammy_lynn.c "Oh, hey!  What a hell of a nice day!"
                            wt_image ttf_pool_1_13
                            tammy_lynn.c "Are you sticking around for a while?"
                            $ title = "Are you?"
                            menu:
                                "Yes":
                                    wt_image ttf_pool_1_14
                                    tammy_lynn.c "It's hotter than I realized out here."
                                    wt_image ttf_pool_1_15
                                    "You're not sure how much her apparent solution is going to cool her down, but there's no harm in letting her try."
                                    wt_image ttf_pool_1_16
                                    "Now topless ..."
                                    wt_image ttf_pool_1_17
                                    "... [tammy_lynn.name] goes back to her sunbathing."
                                    wt_image ttf_pool_1_18
                                    "As suspected, her solution did little to keep the hot sun from raising a sweat, but it made your day a little brighter before you move on."
                                    change player energy by -energy_very_short
                                "No":
                                    wt_image ttf_pool_1_5
                                    "You go on with your day and [tammy_lynn.name] goes back to her sunbathing."
                    # other first time
                    elif not tammy_lynn.has_tag('watched_at_pool'):
                        wt_image ttf_pool_1_4
                        tammy_lynn.c "Oh, hey!  You have a really awesome place here.  It's really nice of you to let me make use of it."
                        wt_image ttf_pool_1_5
                        tammy_lynn.c "I'm just gonna catch some 'rays."
                        wt_image ttf_pool_1_6
                        "She settles in ..."
                        wt_image ttf_pool_1_7
                        "... then realizes you're still watching her."
                        wt_image ttf_pool_1_8
                        "She looks back at you, quizzically."
                        $ title = "What do you do?"
                        menu:
                            "Move on":
                                wt_image ttf_pool_1_6
                                "You go on with your day and [tammy_lynn.name] goes back to her sunbathing."
                            "Keep watching her":
                                "Once it's clear you're staying put, [tammy_lynn.name] has a decision to make."
                                wt_image ttf_pool_1_9
                                "She opts to turn around ..."
                                wt_image ttf_pool_1_6
                                "... and go back to her sunbathing."
                                wt_image ttf_pool_1_7
                                "She keeps looking back over ther shoulder, though, checking to see if you're still watching."
                                wt_image ttf_pool_1_10
                                "Eventually you think she's going to say something."
                                wt_image ttf_pool_1_6
                                "Then she thinks better of it, and tries to ignore you and concentrate on the warmth of the sun beating down on her.  The show's not going to get any better than this today, so eventually you move on."
                                add tags 'watched_at_pool' to tammy_lynn
                                # one-time boost to this
                                $ tammy_lynn.caught_you_watching += 1
                                change player energy by -energy_very_short
                    # other
                    else:
                        wt_image ttf_pool_1_4
                        tammy_lynn.c "Oh, hey!  What a hell of a nice day!"
                        wt_image ttf_pool_1_11
                        tammy_lynn.c "Are you planning on sticking around?"
                        $ title = "Stay and watch her?"
                        menu:
                            "Yes":
                                wt_image ttf_pool_1_8
                                "[tammy_lynn.name] doesn't look surprised."
                                wt_image ttf_pool_1_10
                                "She looks like she's thinking about saying something ..."
                                wt_image ttf_pool_1_6
                                "... then decides against it."
                                wt_image ttf_pool_1_7
                                "For a while, she keeps looking back over her shoulder as she sunbathes, checking to see if you're still watching her."
                                wt_image ttf_pool_1_6
                                "Eventually she reconciles herself to your presence and concentreates on the warmth of the sun beating down on her.  The show's not going to get any better than this today, so you move on."
                                change player energy by -energy_very_short
                            "No":
                                wt_image ttf_pool_1_5
                                "[tammy_lynn.name] seems happy with that answer."
                                wt_image ttf_pool_1_6
                                "She goes back to sunbathing and you go on with yor day."
                "Yes, and hypnotize her" if player.can_hypno(tammy_lynn):
                    add tags 'hypno_at_pool' to tammy_lynn
                    $ queue_action(tammy_lynn.hypno_action)
                "No, not today":
                    wt_image ttf_pool_1_3
                    "You leave [tammy_lynn.name] to her sunbathing and go on with your day."
                "Never (shuts off this event)":
                    add tags 'no_pool_events' to tammy_lynn
                    wt_image ttf_pool_1_3
                    "You're not interested in ogling [tammy_lynn.name] poolside.  You leave her to her sunbathing and go on with your day."
        else:
            $ tammy_lynn.event_outfit += 1

    # minor yoga event if you've been watching her
    if tammy_lynn.event_outfit == 6:
        # note: test must be great than 1, not 0, to align with major yoga event
        if tammy_lynn.watched_her_do_yoga > 1:
            call forced_movement(living_room) from _call_forced_movement_542
            summon tammy_lynn
            wt_image ttf_yoga_3_1
            "Looks like [tammy_lynn.name] is getting ready to do some more yoga."
            $ title = "What do you do?"
            menu:
                "Watch her":
                    # full exhibitionist
                    if tammy_lynn.has_tag('exhibitionist_for_you'):
                        wt_image ttf_yoga_3_9
                        "When she realizes you're going to watch, [tammy_lynn.name] grins and pulls her shorts up a little higher ..."
                        wt_image ttf_yoga_3_10
                        "... before starting her routine on the floor."
                        wt_image ttf_yoga_3_6
                        if not tammy_lynn.has_tag('waterlogged_snake'):
                            add tags 'waterlogged_snake' to tammy_lynn
                            player.c "What's that pose called?"
                            tammy_lynn.c "'Drunken possum'."
                            wt_image ttf_yoga_3_5
                            tammy_lynn.c "This one's 'waterlogged snake'."
                            wt_image ttf_yoga_3_3
                            "She seems to like this position, as she holds it for a while."
                        else:
                            "After a quick stretch in 'drunken possum' ..."
                            wt_image ttf_yoga_3_4
                            "... she rolls up into 'waterlogged snake' ..."
                            wt_image ttf_yoga_3_3
                            "... and holds it for a while."
                        wt_image ttf_yoga_3_12
                        tammy_lynn.c "My pants may be a little binding for the next position."
                        wt_image ttf_yoga_3_13
                        tammy_lynn.c "Could you adjust them for me?"
                        wt_image ttf_yoga_3_14
                        tammy_lynn.c "Remember, no touching!"
                        wt_image ttf_yoga_3_15
                        "You take hold of her shorts, careful not to make contact with [tammy_lynn.name] herself ..."
                        wt_image ttf_yoga_3_16
                        "... and pull them to the side."
                        tammy_lynn.c "That seems better."
                    # partial
                    elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                        wt_image ttf_yoga_3_9
                        "When she realizes you're going to watch, [tammy_lynn.name] subtly pulls her shorts up a little higher ..."
                        wt_image ttf_yoga_3_10
                        "... and starts her routine on the floor."
                        if not tammy_lynn.has_tag('waterlogged_snake'):
                            add tags 'waterlogged_snake' to tammy_lynn
                            wt_image ttf_yoga_3_4
                            "... before rolling up on the ball."
                            player.c "What's that pose called?"
                            wt_image ttf_yoga_3_5
                            tammy_lynn.c "'Waterlogged snake'."
                            wt_image ttf_yoga_3_6
                            tammy_lynn.c "This one's 'drunken possum'."
                            wt_image ttf_yoga_3_7
                            "Obviously"
                        else:
                            wt_image ttf_yoga_3_6
                            "After a quick stretch in 'drunken possum' ..."
                            wt_image ttf_yoga_3_4
                            "... she rolls up into 'waterlogged snake' ..."
                            wt_image ttf_yoga_3_3
                            "... a position she holds for a while ..."
                            wt_image ttf_yoga_3_11
                            "... while making a noticeable effort to accentuate her stretch."
                    # first time other
                    elif not tammy_lynn.has_tag('waterlogged_snake'):
                        add tags 'waterlogged_snake' to tammy_lynn
                        wt_image ttf_yoga_3_2
                        "She's become familiar enough having you as an audience that, after a moment's hesitation, she ignores you and begins her routine."
                        wt_image ttf_yoga_3_3
                        "The use of the ball adds some interesting elements to her routine."
                        wt_image ttf_yoga_3_4
                        player.c "What's that pose called?"
                        wt_image ttf_yoga_3_5
                        tammy_lynn.c "'Waterlogged snake'."
                        wt_image ttf_yoga_3_6
                        tammy_lynn.c "This one's 'drunken possum'."
                        wt_image ttf_yoga_3_7
                        "Obviously"
                    # other
                    else:
                        wt_image ttf_yoga_3_2
                        "She's become familiar enough having you as an audience that, after a moment's hesitation, she ignores you and begins her routine.  She seems full of energy today ..."
                        wt_image ttf_yoga_3_3
                        "... dare one say, even 'perky'."
                        wt_image ttf_yoga_3_4
                        "She flows smoothly from 'water-logged snake' ..."
                        wt_image ttf_yoga_3_6
                        "... to drunken possum ..."
                        wt_image ttf_yoga_3_7
                        "... and the remainder of her routine."
                    wt_image ttf_yoga_3_8
                    "[tammy_lynn.name] seems refreshed after her yoga.  She leaves you to carry on with your day."
                    change player energy by -energy_very_short
                "Go on with your day":
                    pass
        # skip this event if haven't been watching her
        else:
            $ tammy_lynn.event_outfit += 1

    # walk event
    if tammy_lynn.event_outfit == 7:
        if not tammy_lynn.has_tag('no_walks'):
            summon tammy_lynn
            wt_image ttf_walk_1_1
            tammy_lynn.c "I'm going for a walk.  Did you want to join me?"
            $ title = "What do you say?"
            menu:
                "Sure":
                    call forced_movement(outdoors) from _call_forced_movement_543
                    rem tags 'no_hypnosis' from tammy_lynn
                    wt_image ttf_walk_1_2
                    tammy_lynn.c "Great!  Let's go."
                    wt_image ttf_walk_1_3
                    $ title = "What do you want to do on the walk?"
                    menu menu_tammy_lynn_walk_event_menu:
                        "Talk":
                            wt_image ttf_walk_1_4
                            "Holding [tammy_lynn.name]'s attention long enough to have a serious conversation proves impossible."
                            tammy_lynn.c "Look!  A squirrel!!"
                            jump menu_tammy_lynn_walk_event_menu
                        "Hypnotize her" if player.can_hypno(tammy_lynn):
                            add tags 'hypno_on_walk' to tammy_lynn
                        "Suggest she get more comfortable":
                            # full exhibitionism
                            if tammy_lynn.has_tag('exhibitionist_for_you'):
                                wt_image ttf_walk_1_8
                                tammy_lynn.c "If I get arrested, you totally have to bail me out."
                                wt_image ttf_walk_1_12
                                tammy_lynn.c "Okay, let's go!"
                                wt_image ttf_walk_1_13
                                "Walking with a naked [tammy_lynn.name] isn't that much different than walking with her full clothed."
                                wt_image ttf_walk_1_14
                                "She's still more interested in walking than talking ..."
                                wt_image ttf_walk_1_15
                                "... and she still enjoys looking at the sights ..."
                                wt_image ttf_walk_1_16
                                "... as do you."
                                wt_image ttf_walk_1_17
                                "But you both have more fun this way."
                                wt_image ttf_walk_1_18
                                tammy_lynn.c "Thanks for the great walk!  This was surpringly comfortable."
                            # partial
                            elif tammy_lynn.has_tag('hypno_re_exhibitionism') or tammy_lynn.caught_you_watching > 4:
                                wt_image ttf_walk_1_7
                                "Unbuttoning her shirt, she takes a look around."
                                wt_image ttf_walk_1_8
                                tammy_lynn.c "I guess no one can see me."
                                wt_image ttf_walk_1_9
                                tammy_lynn.c "Come on, let's go!"
                                wt_image ttf_walk_1_10
                                "Walking with a topless [tammy_lynn.name] isn't that much different than walking with her full clothed.  She's still more interested in walking than talking ..."
                                wt_image ttf_walk_1_11
                                "... and you both still enjoy stopping to look at the sights ..."
                                wt_image ttf_walk_1_9
                                "... but you both have more fun this way."
                                tammy_lynn.c "Thanks for the great walk!  This was surpringly comfortable."
                            # none
                            else:
                                tammy_lynn.c "I'm good, thanks!"
                                jump menu_tammy_lynn_walk_event_menu
                        "Just walk":
                            wt_image ttf_walk_1_3
                            "Goofy [tammy_lynn.name]'s not bad company for a walk, as long as you don't want deep conversation."
                            wt_image ttf_walk_1_4
                            "She enjoys the sights, and to the best can, so do you."
                            wt_image ttf_walk_1_1
                            tammy_lynn.c "Thanks for coming along.  I had fun!"
                    call forced_movement(living_room) from _call_forced_movement_544
                    add tags 'no_hypnosis' to tammy_lynn
                    # no extra energy if hypno'd her
                    if tammy_lynn.has_tag('hypno_on_walk'):
                        $ queue_action(tammy_lynn.hypno_action)
                    # else normal walk energy use
                    else:
                        change player energy by -energy_short
                "No, but suggest she have a pee before she goes" if tammy_lynn.has_tag('accepts_watersports'):
                    wt_image ttf_toilet_4_1
                    tammy_lynn.c "That's probably a good idea."
                    wt_image ttf_toilet_4_2
                    "She sits down in front of you, legs spread, so you have a good view."
                    wt_image ttf_toilet_4_3
                    "What begins as a trickle ..."
                    wt_image ttf_toilet_4_4
                    "... soon turns into a flood ..."
                    wt_image ttf_toilet_4_5
                    "... that continues for some time ..."
                    wt_image ttf_toilet_4_7
                    "... and then stops."
                    wt_image ttf_toilet_4_8
                    tammy_lynn.c "You were right."
                    wt_image ttf_toilet_4_9
                    tammy_lynn.c "I really did need to go before I left."
                    change player energy by -energy_very_short
                "Not today":
                    wt_image ttf_walk_1_2
                    tammy_lynn.c "Okay.  See you later!"
                "Never (shuts off this event)":
                    add tags 'no_walks' to tammy_lynn
                    wt_image ttf_walk_1_2
                    tammy_lynn.c "Okay.  Whatever."
        else:
            $ tammy_lynn.event_outfit += 1

    # NOTE: last event in chain has to be one that can't be skipped
    # phone event
    if tammy_lynn.event_outfit == 8:
        $ tammy_lynn.phone_outfit += 1
        if tammy_lynn.phone_outfit > 2:
            $ tammy_lynn.phone_outfit = 1
        # special event re phone
        if tammy_lynn.has_tag('confronted_over_phone') and not tammy_lynn.has_tag('caught_on_phone'):
            if tammy_lynn.phone_outfit == 1:
                $ tammy_lynn.phone_outfit = 0 # so don't get this outfit three times in a row
            wt_image ttf_phone_2_1
            "[tammy_lynn.name] is on her phone again."
            wt_image ttf_phone_2_2
            "She's so engrossed in what she's doing, she doesn't seem to hear you come in."
            $ title = "Investigate?"
            menu:
                "See if you can see what she's doing":
                    wt_image ttf_phone_2_6
                    "Stepping quietly behind her, you can see that she's on some sort of photo-sharing app ..."
                    wt_image ttf_phone_2_4
                    "... the nature of which is soon made clear."
                    wt_image ttf_phone_2_7
                    "Whoever the photos are for, she's framed them to exclude her face."
                    $ title = "What now?"
                    menu:
                        "Confront her":
                            add tags 'caught_on_phone' to tammy_lynn
                            wt_image ttf_phone_2_6
                            "As she uploads the photo, you realize she's not sending it to anyone in particular.  She's posting it for comments.  A host of nasty ones soon flood in."
                            player.c "I'm not sure your genitals really look like the world's ugliest taco.  That seems harsh."
                            wt_image ttf_phone_2_8
                            tammy_lynn.c "SHIT!!!  You're not supposed to see that!!"
                            player.c "Really?  Because that site is open to everyone, and the comments are set to public, too."
                            wt_image ttf_phone_2_9
                            tammy_lynn.c "Yeah, but you're not supposed to know it's me."
                            player.c "What app was that?  It looked like some sort of raunchy hot-or-not forum.  Did you really ask a bunch of anonymous online guys what they think of your pussy?"
                            wt_image ttf_phone_2_10
                            tammy_lynn.c "I guess.  I don't know why.  It's just an urge that comes over me sometimes.  Letting strangers look at my body so I can hear what they think of it.  It's kinda embarrassing.  Can we not be talking about this?"
                            wt_image living_room.image
                            "She answers her own question by getting up and retreating to her room.  If you want to talk about this more, you should give her some time to get over her initial shame at getting caught."
                        "Ignore her (shuts phone mystery events off)":
                            add tags 'phone_events_off' to tammy_lynn
                            wt_image ttf_phone_2_5
                            "Whoever the photos are for is none of your business.  You leave her alone and go on with your day."
                "Ignore her (shuts phone mystery events off)":
                    add tags 'phone_events_off' to tammy_lynn
                    wt_image ttf_phone_2_5
                    "Whatever's she up to is of no interest to you.  You leave her alone and go on with your day."
        # first outfit
        elif tammy_lynn.phone_outfit == 1:
            # exhibitionist
            if tammy_lynn.has_tag('caught_on_phone'):
                wt_image ttf_phone_1_1
                "[tammy_lynn.name] is sprawled out and playing on her phone.  She's so engrossed in what she's doing, you're not sure she hears you come in."
                wt_image ttf_phone_1_2
                tammy_lynn.c "Oh, hey!"
                wt_image ttf_phone_1_4
                "She gives you a mischievous grin before returning her attention to her phone ..."
                wt_image ttf_phone_1_5
                "... having adjusted her top just enough to give you a somewhat obscured view of her breasts and nipples ..."
                wt_image ttf_phone_1_6
                "... as she otherwise goes back to ignoring your presence."
            # vanilla
            else:
                wt_image ttf_phone_1_1
                "[tammy_lynn.name] is sprawled out and playing on her phone.  She's so engrossed in what she's doing, you're not sure she hears you come in."
                wt_image ttf_phone_1_2
                tammy_lynn.c "Oh, hey!"
                wt_image ttf_phone_1_3
                if tammy_lynn.has_tag('no_porn_selfies'):
                    tammy_lynn.c "I'm not sharing photos, [tammy_lynn.your_respect_name], in case you're worried I am.  I'm chatting with real friends."
                    "That's progress."
                elif tammy_lynn.has_tag('caught_on_phone'):
                    player.c "Dare I ask what you're up to?"
                    tammy_lynn.c "Probably not."
                else:
                    "She doesn't pay you much more mind, even once she knows you're there.  Whatever she's doing on her phone has her full attention."
        # second outfit
        elif tammy_lynn.phone_outfit == 2:
            wt_image ttf_phone_2_1
            "[tammy_lynn.name] is on her phone again."
            wt_image ttf_phone_2_2
            "She's so engrossed in what she's doing, she doesn't seem to hear you come in."
            if tammy_lynn.has_tag('no_porn_selfies'):
                wt_image ttf_phone_2_3
                "Stepping quietly behind her, you're pleased to confirm she's just chatting with friends, not sharing intimate photos with strangers."
            elif tammy_lynn.has_tag('caught_on_phone'):
                wt_image ttf_phone_2_4
                "She's taking photos again ..."
                wt_image ttf_phone_2_5
                "... and enjoying the resulting online comments."
            else:
                wt_image ttf_phone_2_5
                "Whatever she's doing, it has her full attention.  You leave her, and go on with your day."
        return

    # it's one to two weeks later for the next event
    $ tammy_lynn.random_number = renpy.random.randint(1, 2)
    $ tammy_lynn.event_week = week + tammy_lynn.random_number - 1
    dismiss tammy_lynn
    call forced_movement(living_room) from _call_forced_movement_545
    notify
    return

# End Day
label tammy_lynn_end_day:
    # set up re her moving in with you
    if tammy_lynn.has_tag('first_day'):
        rem tags 'first_day' from tammy_lynn
        $ tammy_lynn.event_week = week
        $ tammy_lynn.training_regime = 'daily'
    # clear tags and return her if dismissed
    if tammy_lynn.has_tag('living_with_you'):
        if tammy_lynn.has_tag('posing_now'):
            rem tags 'posing_now' 'posing_discipline' 'posing_tied' 'posing_bedroom' 'posing_living_room' 'posing_outdoors' 'posing_casual' 'posing_challenging' 'posing_lewd' 'posing_yoga' from tammy_lynn
            call tammy_lynn_update_media from _call_tammy_lynn_update_media_1
        call character_location_return(tammy_lynn) from _call_character_location_return_298
    return

# End Week
label tammy_lynn_end_week:
    if tammy_lynn.has_tag('living_with_you'):
        $ tammy_lynn.weeks_with_you += 1
    if tammy_lynn.can_be_interacted and tammy_lynn.has_tag('bar_server') and not tammy_lynn.has_tag('visited_her_at_bar') and not tammy_lynn.has_tag('no_visiting_her_at_bar'):
        wt_image tammy_lynn.image
        tammy_lynn.c "I'm working a shift at the bar tonight.  It's the weekend, you should come see where I work!"
        $ title = "What do you want to do?"
        menu:
            "Go see where she works":
                call forced_movement(outdoors) from _call_forced_movement_546
                summon tammy_lynn
                add tags 'visited_her_at_bar' to tammy_lynn
                wt_image ttf_bar_1_1
                "[tammy_lynn.name]'s choice of bar to work at is interesting.  Her 'uniform' is even more interesting!"
                wt_image ttf_bar_1_2
                tammy_lynn.c "Yay!!  You made it!  Isn't this place awesome?"
                player.c "Is this a strip club?"
                wt_image ttf_bar_1_3
                tammy_lynn.c "No!!!  There's no pole here, not even a stage."
                player.c "Who are your customers?"
                wt_image ttf_bar_1_4
                tammy_lynn.c "Mostly guys.  Businessmen from out of town, boys from back home visiting the big city, that sort of thing.  You wanna know the best part, though?"
                wt_image ttf_bar_1_5
                tammy_lynn.c "They're not allowed to touch me!  And if they do, and I punch them out, they get thrown out onto the street, not me!!"
                wt_image ttf_bar_1_6
                tammy_lynn.c "Isn't that awesome!"
                wt_image ttf_bar_1_7
                "Your reply is cut short by the approach of one of her co-workers."
                coworker_tammy_lynn "[tammy_lynn.name], table 7 ordered a double dance."
                wt_image ttf_bar_1_8
                tammy_lynn.c "That's when everyone at the table orders two drinks at once, and instead of serving them normally, we dance around the table before putting the drinks down in front of them."
                wt_image ttf_bar_1_9
                tammy_lynn.c "Guess I better get back to work!"
                wt_image ttf_bar_1_10
                "[tammy_lynn.name] and her co-worker collect their drinks and head to table 7 to deliver them, while you head home."
                dismiss tammy_lynn
                call forced_movement(living_room) from _call_forced_movement_547
            "Maybe some other time":
                pass
            "Never (shuts off this option)":
                add tags 'no_visiting_her_at_bar' to tammy_lynn
    return

## Character Specific Timers
# N/A

# Trigger Used
# NEED cake 1 for deep throat and sex
# NEED posing set: Outside 6 31 outside, Spanking 2 22 bedroom,Trashy 1 living room

label tammy_lynn_trigger_used:
    $ tammy_lynn.training_session()
    player.c "Time for you to be my playtoy, [tammy_lynn.name]."
    wt_image ttf_bedroom_1_6
    tammy_lynn.c "I don't get it?  What do you mean?"
    player.c "I mean you stop talking and just do as I say."
    wt_image ttf_bedroom_1_10
    if tammy_lynn.has_tag('sub_for_you'):
        tammy_lynn.c "You mean you're going to discipline me?"
        player.c "Not exactly.  [tammy_lynn.trigger_phrase]."
    else:
        tammy_lynn.c "That's a bit rude, isn't it?  I mean, I get it's your house and I'm just a guest, but ..."
        player.c "[tammy_lynn.trigger_phrase]."
    wt_image ttf_bedroom_1_5
    tammy_lynn.c "Wh ... what did you say?"
    player.c "[tammy_lynn.trigger_phrase].  Stop talking and take off your clothes while I decide what to do with you."
    wt_image ttf_bedroom_1_27
    $ title = "What do you do with her?"
    menu menu_tammy_lynn_trigger_menu:
        "Have her deep throat you":
            if tammy_lynn.has_tag('posing_outdoors') or tammy_lynn.has_tag('posing_living_room'):
                wt_image ttf_trigger_1_1
                "You bring her back to her bedroom so the two of you won't be disturbed."
            rem tags 'posing_now' 'posing_bedroom' 'posing_living_room' 'posing_outdoors' from tammy_lynn
            call tammy_lynn_update_media from _call_tammy_lynn_update_media_2
            player.c "Kneel down and open your mouth."
            wt_image ttf_trigger_1_2
            player.c "Time to pay your rent.  Since you don't have much money, you want to pay me with your body.  Take my balls into your mouth."
            wt_image ttf_trigger_1_3
            player.c "This is too nice a house to pay for the rent just by sucking my balls.  Take my cock into your mouth."
            wt_image ttf_trigger_1_4
            player.c "You can fit more of my cock than that in your mouth."
            wt_image ttf_trigger_1_5
            player.c "More"
            wt_image ttf_trigger_1_6
            player.c "You want to make me cum as a way to pay your rent."
            wt_image ttf_trigger_1_4
            "Before she decided she wasn't into men, she sucked off enough boys back home to know what she's doing."
            wt_image ttf_trigger_1_5
            $ title = "Where do you want to cum?"
            menu:
                "Down her throat":
                    wt_image ttf_trigger_1_6
                    player.c "[player.orgasm_text]"
                    wt_image ttf_trigger_1_2
                    "After she shows you that she swallowed it all, you have her dress and release her from the trance."
                    $ tammy_lynn.hypno_swallow_count += 1
                "On her face":
                    wt_image ttf_trigger_1_7
                    player.c "[player.orgasm_text]"
                    "It's tempting to leave her like this, but if she sees her, [becky_sue.name] will know where the jizz came from.  You have her clean up and dress and release her from the trance."
                    $ tammy_lynn.hypno_facial_count += 1
            $ tammy_lynn.hypno_blowjob_count += 1
            orgasm notify
        "Fuck her":
            if tammy_lynn.has_tag('posing_outdoors') or tammy_lynn.has_tag('posing_living_room'):
                wt_image ttf_trigger_1_1
                "You bring her back to her bedroom so the two of you won't be disturbed."
            rem tags 'posing_now' 'posing_bedroom' 'posing_living_room' 'posing_outdoors' from tammy_lynn
            call tammy_lynn_update_media from _call_tammy_lynn_update_media_3
            wt_image ttf_trigger_1_8
            player.c "Time to pay your rent.  Since you don't have much money, you want to pay me with your body.  Ask me how I want to fuck your pussy so you can pay your rent."
            tammy_lynn.c "How would you like to fuck my pussy so I can pay my rent?"
            $ title = "What position do you want?"
            menu:
                "On her back":
                    wt_image ttf_trigger_1_9
                    "She spreads herself open so you can enter her ..."
                    wt_image ttf_trigger_1_10
                    "... then stares weirdly at you as you fuck her."
                    $ title = "What do you tell her?"
                    menu:
                        "Act like you enjoy this":
                            wt_image ttf_trigger_1_11
                            "That's better.  You fill her writhing body with your cum before telling her to dress and releasing her from the trance."
                            player.c "[player.orgasm_text]"
                        "Play dead":
                            wt_image ttf_trigger_1_12
                            "That's better.  You fill her lifeless body with your cum before telling her to dress and releasing her from the trance."
                            player.c "[player.orgasm_text]"
                "From behind":
                    wt_image ttf_trigger_1_13
                    "She bends over and lets you enter her from behind ..."
                    wt_image ttf_trigger_1_14
                    "... then awkwardly waits as you fuck her."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image ttf_trigger_1_15
                            player.c "Ask me to fill your cunt with cum."
                            tammy_lynn.c "Please fill my cunt with cum."
                            player.c "[player.orgasm_text]"
                        "On her":
                            wt_image ttf_trigger_1_16
                            "You push her head down and cover her upturned ass with cum."
                            player.c "[player.orgasm_text]"
                    "When your balls finish pumping out their load, you have her pull herself together and then release her from her trance."
                "Have her ride you":
                    wt_image ttf_trigger_1_17
                    "Holding herself open, she impales herself on you ..."
                    wt_image ttf_trigger_1_18
                    "... and then mindlessly rides you ..."
                    wt_image ttf_trigger_1_19
                    "... until you can no longer hold back."
                    wt_image ttf_trigger_1_17
                    player.c "[player.orgasm_text]"
                    wt_image ttf_trigger_1_19
                    player.c "Thank me for filling your cunt with my cum and ask me to pump as much into you as I can."
                    tammy_lynn.c "Thank you for filling my cunt with your cum.  Please pump as much of you cum into me as you can."
                    wt_image ttf_trigger_1_18
                    "When your balls are finally empty, you have her pull herself together and then release her from her trance."
            $ tammy_lynn.hypno_sex_count += 1
            orgasm notify
        "Fuck her ass":
            if tammy_lynn.has_tag('posing_outdoors') or tammy_lynn.has_tag('posing_living_room'):
                wt_image ttf_trigger_1_1
                "You bring her back to her bedroom so the two of you won't be disturbed."
            rem tags 'posing_now' 'posing_bedroom' 'posing_living_room' 'posing_outdoors' from tammy_lynn
            call tammy_lynn_update_media from _call_tammy_lynn_update_media_4
            wt_image ttf_trigger_1_8
            player.c "Time to pay your rent.  Since you don't have much money, you want to pay me with your body.  Roll over."
            wt_image ttf_trigger_1_20
            player.c "Ask me to let you pay your rent by taking my dick up your ass."
            wt_image ttf_trigger_1_21
            tammy_lynn.c "Can I please pay my rent by taking your dick up my ass?"
            $ title = "Who's doing the work?"
            menu:
                "You ass fuck her while she lies there":
                    wt_image ttf_trigger_1_22
                    "She lies there quietly as you stick your cock up her butt ..."
                    wt_image ttf_trigger_1_23
                    "... then stares mindlessly at you as you ream her ..."
                    wt_image ttf_trigger_1_24
                    "... until you fill her bowels with jizz."
                    wt_image ttf_trigger_1_25
                    player.c "[player.orgasm_text]"
                    wt_image ttf_trigger_1_24
                "She rides you with her ass":
                    wt_image ttf_trigger_1_26
                    "She climbs on top of you and impales her ass on your dick."
                    wt_image ttf_trigger_1_27
                    "Then she lets you guide her up and down your shaft ..."
                    wt_image ttf_trigger_1_28
                    "... until you fill her bowels with jizz."
                    wt_image ttf_trigger_1_29
                    player.c "[player.orgasm_text]"
                    wt_image ttf_trigger_1_28
            player.c "The cum dripping out of your ass today will seem normal, even after you're released from your trance.  You'll smile everytime you feel a drip.  Get dressed.  When you're fully clothed, you'll wake from your trance."
            wt_image ttf_bedroom_1_26
            "Wait while she gets dressed."
            wt_image ttf_bedroom_1_2
            player.c "You look happy."
            wt_image ttf_bedroom_1_9
            tammy_lynn.c "I just can't stop smiling!!  It must be that I'm so happy to be able to live her with you and Becky Sue!"
            $ tammy_lynn.hypno_anal_count += 1
            orgasm notify
        "Pose her in her bedroom" if not tammy_lynn.has_tag('posing_bedroom'):
            rem tags 'posing_living_room' 'posing_outdoors' from tammy_lynn
            add tags 'posing_now' 'posing_bedroom' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_1')
            wt_image tammy_lynn.image
            "She looks good on the window sill.  It cheers her room up nicely."
            jump menu_tammy_lynn_trigger_menu
        "Pose her in the living room" if not tammy_lynn.has_tag('posing_living_room'):
            rem tags 'posing_bedroom' 'posing_outdoors' from tammy_lynn
            add tags 'posing_now' 'posing_living_room' 'posing_casual' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_3')
            wt_image tammy_lynn.image
            "That's a visually appealing entrance piece for the room."
            jump menu_tammy_lynn_trigger_menu
        "Something more casual" if tammy_lynn.has_tag('posing_living_room') and not tammy_lynn.has_tag('posing_casual'):
            rem tags 'posing_yoga' 'posing_challenging' 'posing_lewd' from tammy_lynn
            add tags 'posing_casual' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_3')
            wt_image tammy_lynn.image
            "That's a visually appealing entrance piece for the room."
            jump menu_tammy_lynn_trigger_menu
        "Something more yoga-like" if tammy_lynn.has_tag('posing_living_room') and not tammy_lynn.has_tag('posing_yoga'):
            rem tags 'posing_casual' 'posing_challenging' 'posing_lewd' from tammy_lynn
            add tags 'posing_yoga' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_4')
            wt_image tammy_lynn.image
            "She works so hard at her yoga, it'd be a shame not to let her show it off sometimes."
            jump menu_tammy_lynn_trigger_menu
        "Something more challenging" if tammy_lynn.has_tag('posing_living_room') and not tammy_lynn.has_tag('posing_challenging'):
            rem tags 'posing_casual' 'posing_yoga' 'posing_lewd' from tammy_lynn
            add tags 'posing_challenging' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_5')
            wt_image tammy_lynn.image
            "This is doing her a favor, really.  She's always working on her flexibility, but rarely gets to apply for a practical purpose."
            jump menu_tammy_lynn_trigger_menu
        "Something lewder" if tammy_lynn.has_tag('posing_living_room') and not tammy_lynn.has_tag('posing_lewd'):
            rem tags 'posing_casual' 'posing_yoga' 'posing_chal`' from tammy_lynn
            add tags 'posing_lewd' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_6')
            wt_image tammy_lynn.image
            "It's not in her nature to offer a man any of her holes, let alone all three at once, but she's a guest in your house, and under the effect of the trance, she agrees she needs to offer something in lieu of rent."
            jump menu_tammy_lynn_trigger_menu
        "Pose her outdoors" if not tammy_lynn.has_tag('posing_outdoors'):
            rem tags 'posing_living_room' 'posing_bedroom' from tammy_lynn
            add tags 'posing_now' 'posing_outdoors' to tammy_lynn
            $ tammy_lynn.change_image('ttf_posing_1_2')
            wt_image tammy_lynn.image
            "As a countrygirl, she probably doesn't get nearly enough fresh air living in the city.  Some time in your garden might do her well."
            jump menu_tammy_lynn_trigger_menu
        "Leave her there" if tammy_lynn.has_tag('posing_now'):
            player.c "If [becky_sue.name] sees you, tell her you lost your laundry.  When she calls you a 'goofball', your mind will be your own, again, but you won't remember why you're here or why you're naked or where you left your laundry."
    if tammy_lynn.has_tag('posing_now'):
        call character_location_return(tammy_lynn) from _call_character_location_return_299
    else:
        dismiss tammy_lynn
    call forced_movement(living_room) from _call_forced_movement_548
    return

########### ROOMS ###########
# Tammy Lynn's Room
label tlr_examine:
    "[tammy_lynn.name] keeps the spare bedroom she's living in neat and tidy, most of the time."
    return

label tlr_enter:
    if tammy_lynn.location != tammy_lynn_room:
        "[tammy_lynn.name] isn't here right now.  Check again tomorrow."
    return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
