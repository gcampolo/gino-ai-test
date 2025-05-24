## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package master_m name "Master M" description "Allows Master M to be a minor character." dependencies core
register master_m_pregame 20 in core as "Master M (Diamond the Slavegirl, Fairyn the Trust Fund Baby)" # note must come after alexis so that talk action re alexis works properly

# Pregame
label master_m_pregame:
  python:
    ## Constants
    ## Credits
    model_credits += [('support', "Diamond the Slavegirl (Skin Diamond)")]
    model_credits += [('support', "Fairyn the Trust Fund Baby (Lily Carter)")]

    ## Character Definition
    master_m = Person(Character("Well Dressed Man", who_color="#0000FF", what_color="#0000FF", window_background=gui.dialogue_background_dark_font_color), "master_m", cut_portrait = True, prefix = "", suffix = "", wait_for_message_period = 1, week_available = 15, prospect_min_reputation = 1)

    # Other Characters
    # 255,0,128
    diamond = Person(Character("Slavegirl", who_color="#FF0080", what_color="#FF0080"), "diamond", cut_portrait = True, prefix = "", suffix = "the Slave Girl")
    # 132,0,226
    #fairyn = Person(Character("Woman M Sent", who_color="#8400E2", what_color="#8400E2", window_background=gui.dialogue_background_medium_font_color), "fairyn", cut_portrait = True, prefix = "", suffix = "")
    # trying lighter share for Fairyn on standard backgroun
    fairyn = Person(Character("Woman M Sent", who_color="#daa7ff", what_color="#daa7ff"), "fairyn", cut_portrait = True, prefix = "", suffix = "")

    ## Actions
    master_m.action_talk = master_m.add_action("Talk to him", label="_talk", condition = "not master_m.has_tag('first_visit')")
    master_m.action_introduce = master_m.add_action("Introduce Yourself", label="_introduce", condition = "master_m.has_tag('first_visit')")
    master_m.action_contact = None
    # master_m.action_lend = master_m.add_action("Lend Him A Slave", label="_lend", condition = "master_m.lent_him_a_slave == 1 and player.slavegirl_count > 0") ## now handled differently
    diamond.action_talk = diamond.add_action("Talk to her", label="_talk", condition = "diamond.can_be_interacted")
    diamond.action_watch_dance = diamond.add_action("Watch Her Dance", label="_watch_dance", condition = "diamond.can_be_interacted and diamond.has_tag('dancing_today') and diamond.location == stage")
    diamond.action_private_show = None
    fairyn.action_talk = fairyn.add_action("Talk to her", label="_talk", condition = "fairyn.can_be_interacted")
    fairyn.action_see_what_up_to = fairyn.add_action("See what she's up to", label="_see_what_up_to", condition = "fairyn.can_be_interacted and not fairyn.has_tag('club_maid_event_happened')")
    fairyn.action_contact = None
    fairyn.action_view_photos = bedroom.add_action("Fairyn's Bondage Photos", label = fairyn.short_name + "_review_photos", context = '_computer_view_images', condition = "player.has_tag('fairyn_gagged_photos')")

    ## Tags
    # Common Character Tags
    master_m.add_tags('first_visit', 'no_hypnosis', 'likes_girls')
    diamond.add_tags('first_visit', 'no_hypnosis', 'likes_boys')
    fairyn.add_tags('first_visit', 'no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A



    ## Other
    master_m.change_status("prospect")
    diamond.change_status("minor_character")
    fairyn.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('master_m_start_day', priority = 10)

    ########### VARIABLES ###########
    # Common Character Variables
    master_m.add_stats_with_value('random_number', 'current_message')
    #diamond.add_stats_with_value('temporary_count')
    diamond.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count')
    #fairyn.add_stats_with_value('temporary_count')
    fairyn.add_stats_with_value('hypno_anal_count', 'hypno_blowjob_count', 'hypno_sex_count', 'hypno_swallow_count', 'random_number')

    # Character Specific Variables
    master_m.add_stats_with_value('encounter_possible', 'lend_diamond_to_school', 'lent_him_a_slave', 'ms1_ms2_joint_event')
    master_m.wait_on_message = False
    master_m.experience_with_your_slave = ""
    # master_m.slave_name_loaned = ""
    master_m.name_of_your_slave_loaned = ""
    diamond.add_stats_with_value('lesbian_training', 'strip_count', 'training_desire_level', 'training_result', 'training_submission_level')
    diamond.training_name = ""
    fairyn.add_stats_with_value('bj_training_status', 'initial_arousal', 'initial_outcome', 'paying_you')
    # keycode for fairyn.initial_outcome: 0: failed outcome; 1: hypnotized and told her to forget (failure); 2: hypnotized and told her she had fun; 3: she masturbated; 4: you Dom'd her but no sex; 5: you had sex w her
    fairyn.wait_on_message = False

    ######## EXPANDABLE MENUES #######
    master_m_club_talk_menu = ExpandableMenu("What would you like to talk to him about?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game; some of these would ideally be in the script for the content that opens them up, rather than here
    master_m.choice_club_talk_nothing = master_m_club_talk_menu.add_choice("Nothing right now", "master_m_club_talk_nothing")
    master_m.choice_club_talk_diamond = master_m_club_talk_menu.add_choice("Discuss difficult truth about Diamond", "master_m_club_talk_difficult_truth", condition = "diamond.training_result > 0 and player.has_tag('dominant') and not master_m.has_tag('discussed_difficult_truth')")
    master_m.choice_club_talk_lend = master_m_club_talk_menu.add_choice("Lending him a slave", "master_m_club_talk_lending_slave", condition = "master_m.lent_him_a_slave == 0 and player.slavegirl_count > 0")
    master_m.choice_club_talk_hannah = master_m_club_talk_menu.add_choice("Principal Hannah's Videos", "master_m_club_talk_principal_videos", condition = "master_m.lend_diamond_to_school == 1")
    master_m.choice_club_talk_sam = master_m_club_talk_menu.add_choice("Someone to train Sam the Barista", "master_m_club_talk_barista_domme", condition = "cassandra.discuss_barista == 3")
    master_m.choice_club_talk_alexis = master_m_club_talk_menu.add_choice("Anal training for [alexis.name] the Personal Assistant", "master_m_discuss_alexis_anal", condition = "alexis.anal_discussion == 1 and not alexis.has_tag('anal_domme_opened')")
    master_m.choice_club_talk_lee = master_m_club_talk_menu.add_choice("Suggest he lend Diamond to your Domme Lee", "master_m_discuss_lee", condition = "lee.has_tag('domme') and player.has_item(lee_collar) and diamond.lesbian_training > 0 and lee.diamond_status == 0")


    fairyn_talk_menu = ExpandableMenu("What would you like to talk to her about?", cancelable = False)
    fairyn.choice_talk_nothing = fairyn_talk_menu.add_choice("Nothing right now", "fairyn_talk_nothing")
    fairyn.choice_talk_photos = fairyn_talk_menu.add_choice("Discuss her photos", "fairyn_talk_photos", condition = "player.has_tag('fairyn_gagged_photos') and fairyn.has_tag('discussed_photos_with_you')")
    fairyn.choice_talk_bj_training = fairyn_talk_menu.add_choice("Discuss training her", "fairyn_talk_bj_training", condition = "fairyn.bj_training_status > 0")
    fairyn.choice_talk_art_show = fairyn_talk_menu.add_choice("Discuss art show", "fairyn_talk_art_show", condition = "elsa.art_show_status > 1 and not fairyn.has_tag('discussed_art_show_with_you')")

  return

# Check prospect label
## note: this converts him from a single message to being able to send multiple messages
## also, this same system can be used to add additional conditionals to getting a new prospect message, other than the standard week and rep conditionals
## the major client equivalent of this is _availability_check
## the existence of this label means the standard prospect check does not fire, so need to include those standard conditions for message 0
label master_m_prospect_check:
    # We start with the standard check
    if master_m.current_message == 0:
        $ return_value = week + 1 >= master_m.week_available and master_m.prospect_min_reputation <= player.reputation
    elif master_m.current_message == 1:
        $ return_value = master_m.lent_him_a_slave == 4 or master_m.lent_him_a_slave == 5
        # $ master_m.current_client_action.name = "New Message from Master M" ## doesn't work here, needs to be in start_day after action is re-created
        if master_m.lent_him_a_slave == 4 or master_m.lent_him_a_slave == 5:
            add tags 'new_message_today' to master_m ## using this to flag to add the name in start_day label
    return


# Initial Contact Message
# OBJECT: Check Messages
label master_m_message:
  # Fairyn
  if master_m.current_message == 1:
    master_m.c "{i}Thanks for sending [master_m.name_of_your_slave_loaned] to spend time with me.{/i}"
    master_m.c "{i}[master_m.experience_with_your_slave]{/i}"
    master_m.c "{i}I've been thinking about how I could reciprocate, and I have someone in mind. If you'd like me to send her your way, let me know.{/i}"
    master_m.c "{i}No rush. Anytime you'd like a visit from her, let me know.  ~ M{/i}"
    $ title = "Tell Master M to send her over?"
    menu:
      "Yes (Ends Day)":
        $ master_m.current_message = 2
        $ master_m.change_status("minor_character")
        $ living_room.remove_action(master_m.current_client_action)
        "You send a message off to Master M, letting him know you're interested."
        add tags 'no_hypnosis' to fairyn
        summon fairyn
        wt_image ms2_car_4
        "Later that evening, a well dressed young woman pulls up in an expensive car.  She looks you over as you step outside to greet her."
        if player.has_tag('supersexy') or player.has_tag('dominant'):
          wt_image ms2_car_1
          fairyn.c "Hmmm.  This must be the right place.  M sent me, hopefully to you."
        elif player.has_tag('wealthy'):
          wt_image ms2_car_1
          fairyn.c "Hmmm.  This place is surprisingly nice.  M sent me, I guess to you?"
        else:
          wt_image ms2_car_5
          fairyn.c "Hmmm.  I'm not sure if I'm in the right place.  M sent me, but surely not to you?"
        player.c "Are you his slave?"
        wt_image ms2_car_6
        "She chuckles."
        fairyn.c "Sometimes.  Can I come in?"
        wt_image ms2_car_7
        if elsa.art_show_status > 0:
          "You recognize her from somewhere, but can't quite place it."
          player.c "Do I know you?"
          wt_image ms2_car_8
          fairyn.c "I doubt it.  Are you letting me in or not?"
        $ title = "Let her in?"
        menu menu_master_message_change:
          "Yes, let her in":
            $ fairyn.training_session()
            # resolved by spending time with Fairyn
            $ master_m.lent_him_a_slave = 7
            player.c "Come on in."
            wt_image ms2_car_3
            if player.has_tag('wealthy'):
                fairyn.c "Thanks!  Be a sweetie and have your maid show me to the nearest bathroom?"
                wt_image ms2_car_10
                player.c "I'll show you myself.  It's this way."
                wt_image ms2_car_9
                fairyn.c "Okay.  Could you get your man to pull my car around back?"
                player.c "It's fine here."
                wt_image ms2_car_11
                fairyn.c "I appreciate you sending your staff away to be discrete, but you needn't have worried.  I don't mind the hired help being around when I play.  It can be fun trying to scandalize them."
                "She disappears into your bathroom."
            else:
                fairyn.c "Thanks!  Be a sweetie and point me to the nearest bathroom?"
                wt_image ms2_car_9
                "She retrieves a bag from her car and disappears into your bathroom."
            $ fairyn.location = living_room
            wt_image living_room.image
            "She's in there for what seems like forever."
            wt_image ms2_visit_1_1
            "Eventually she appears, dressed in an ... 'interesting' outfit."
            fairyn.c "I kept you waiting, didn't I?  I can be such an inconsiderate bitch sometimes."
            wt_image ms2_visit_1_36
            fairyn.c "Don't you just hate spoiled brats who act like the whole world revolves around them?  Sorry to break the news to you, but I'm one of those girls, sweetie."
            wt_image ms2_visit_1_3
            fairyn.c "What do you think of that?"
            call fairyn_initial_conversation from _call_fairyn_initial_conversation
            rem tags 'fairyn_convo_name' 'fairyn_convo_daddy' 'fairyn_convo_father' 'fairyn_convo_father_2' 'fairyn_convo_kneel' 'fairyn_convo_why' 'fairyn_convo_domme' 'fairyn_convo_leave' 'fairyn_convo_touch' 'fairyn_convo_bag' 'fairyn_convo_work' 'fairyn_convo_dont_care' 'fairyn_convo_bag_holes' 'fairyn_convo_bag_tell' from fairyn
            # hypnosis option if she's leaving but not too mad
            if fairyn.temporary_count == 2:
              rem tags 'no_hypnosis' from fairyn # to allow subsequent tests
              if player.can_hypno(fairyn):
                $ title = "Hypnotize her?"
                menu:
                  "Hypnotize her":
                    $ fairyn.hypno_session() #deducts energy and records she was hypnotized
                    wt_image ms2_visit_1_7
                    player.c "Look at this before you go."
                    "Your focus catches her attention."
                    call focus_image from _call_focus_image
                    player.c "We haven't finished chatting.  You came here to listen to me.  Listen to me now."
                    player.c "Master M said you should spend time with me.  You want to spend time with me.  Spend some time with me and listen to me.  Listen to my voice. Only my voice now. Only my voice."
                    wt_image ms2_visit_1_8
                    "No point asking for a view of her breasts.  You already have one."
                    $ title = "What do you do with her?"
                    menu menu_master_m_message_fairyn_hypno:
                      "Ask her name" if not fairyn.has_tag('know_name'):
                        player.c "What's your name?"
                        wt_image ms2_visit_1_7
                        fairyn.c "Fairyn.  I know, it's unusual.  It's an old family name on my father's side.   It's the biggest thing he contributed to my upbringing: a name no one's ever heard of.  That and money.  He also contributed a lot of money."
                        $ fairyn.change_full_name("", "Fairyn", "the Trust Fund Baby")
                        wt_image ms2_visit_1_38
                        fairyn.c "After all, if you give your daughter lots of money, even if it's in a trust fund and she's not allowed to touch most of it, then you don't have to worry about little things like calling her on her birthday or coming to watch her in the school play."
                        "Lots of sore points there, which will require more therapy than you have time to provide her to sort out."
                        add tags 'know_name' to fairyn
                        $ fairyn.change_full_name("", "Fairyn", "the Trust Fund Baby")
                        $ title = "What now?"
                        jump menu_master_m_message_fairyn_hypno
                      "Ask what she came here for" if not fairyn.has_tag('hypno_discuss_why_here'):
                        add tags 'hypno_discuss_why_here' 'hypno_treat_her_like_nobody' to fairyn
                        player.c "Why are you here?"
                        wt_image ms2_visit_1_8
                        fairyn.c "To be treated like a nobody. As less than a nobody. M said you might be the sort of guy I could warm up to, if I was in one of my 'moods' again."
                        player.c "You get in the mood to be treated as less than a nobody?"
                        wt_image ms2_visit_1_7
                        fairyn.c "Yes.  I live my life on a pedestal.  It's great. I have everything I could ever want.  Men and women, they fawn over me, either for my beauty or my money or both."
                        wt_image ms2_visit_1_38
                        fairyn.c "But I'm not really happy.  I'm sad, all the time. Sometimes I need something to break that sadness, and shake me up."
                        wt_image ms2_visit_1_8
                        fairyn.c "When I'm in that mood, I like it when people treat me like a cheap whore, and just take what they want from me."
                        fairyn.c "Sometimes I dress like a cheap whore and go to a dive bar and let the first guy who shows an interest in me take me and do what he wants with me.  I especially like to do that when I'm in the mood to be used by someone stupid."
                        fairyn.c "But I've been hurt a few times that way, too, and I like to change it up, and let respectable men like you or M have a go at me, if they're smart enough and confident enough to get me groveling for them."
                        $ fairyn.initial_arousal = 2
                        $ title = "What do you do now?"
                        jump menu_master_m_message_fairyn_hypno
                      "Fuck her mouth" if fairyn.has_tag('hypno_treat_her_like_nobody'):
                        wt_image ms2_visit_1_5
                        player.c "On your knees with your mouth open, you dumb whore.  I need a place to empty my balls."
                        wt_image ms2_visit_1_41
                        "She fairly mewls in excitement as you plunge your cock into her ..."
                        fairyn.c "oooooo"
                        wt_image ms2_visit_1_26
                        "... and holds her head as still as she can while you skull fuck her."
                        wt_image ms2_visit_1_42
                        player.c "[player.orgasm_text]"
                        fairyn.c "oohhhhh"
                        wt_image ms2_visit_1_27
                        "The hypnotized woman gulps down your sperm as you empty it down her throat.  Even as you pull your dick out of her mouth, she follows it with her tongue, lapping up the last of your jizz trailing from your cock head."
                        $ fairyn.hypno_blowjob_count += 1
                        $ fairyn.hypno_swallow_count += 1
                        orgasm notify
                        call master_m_message_fairyn_choice from _call_master_m_message_fairyn_choice
                      "Fuck her pussy" if fairyn.has_tag('hypno_treat_her_like_nobody'):
                        wt_image ms2_visit_1_10
                        player.c "Spread your legs, you dumb whore.  I'm going to use you as a cock sheath."
                        wt_image ms2_visit_1_49
                        "She fairly mewls in excitement as you lift her up and plunge your cock into her, fucking her hard and fast with no preamble."
                        fairyn.c "oooooo"
                        wt_image ms2_visit_1_28
                        "After a few, hard thrusts you let go.  The hypnotized woman groans as she feels the flood of your sperm pumping inside her."
                        wt_image ms2_visit_1_29
                        player.c "[player.orgasm_text]"
                        fairyn.c "oohhhhh"
                        $ fairyn.hypno_sex_count += 1
                        orgasm notify
                        call master_m_message_fairyn_choice from _call_master_m_message_fairyn_choice_1
                      "Fuck her ass" if fairyn.has_tag('hypno_treat_her_like_nobody'):
                        wt_image ms2_visit_1_43
                        player.c "Roll over and offer me your butt, you dumb whore.  I'm going to ream your stupid ass."
                        wt_image ms2_visit_1_44
                        "She fairly mewls in anticipation as she raises her hips ..."
                        fairyn.c "ooooo"
                        wt_image ms2_visit_1_31
                        "... then squeals as you plunge your cock into her."
                        fairyn.c "aaaiiiiii!!"
                        wt_image ms2_visit_1_33
                        "As you fuck her behind, her squeals turn to moans."
                        fairyn.c "ooooooo"
                        wt_image ms2_visit_1_34
                        "You pile drive into her, faster and faster until you cum."
                        wt_image ms2_visit_1_50
                        player.c "[player.orgasm_text]"
                        fairyn.c "ooooooo!!"
                        wt_image ms2_visit_1_35
                        "When your balls have finished pumping your sperm into her bowels, you pull out.  Your cock exits the hypnotized woman's distended ass with a small 'pop' sound ..."
                        wt_image ms2_visit_1_51
                        "... followed by a flow of cum."
                        $ fairyn.hypno_anal_count += 1
                        orgasm notify
                        call master_m_message_fairyn_choice from _call_master_m_message_fairyn_choice_2
                      "Tell her to bark like a dog" if not fairyn.has_tag('hypno_bark'):
                        add tags 'hypno_bark' to fairyn
                        player.c "Bark like a dog."
                        wt_image ms2_visit_1_38
                        fairyn.c "Why?"
                        if not fairyn.has_tag('hypno_treat_her_like_nobody'):
                          player.c "It's relaxing and I enjoy it.  You want to feel relaxed, and you want me to enjoy myself with you.  Bark for me."
                          wt_image ms2_visit_1_7
                          "She gives a tentative bark."
                          fairyn.c "Woof?"
                          player.c "You can do better than that. Bark for me."
                          fairyn.c "Woof?"
                          "She's not opposed to the idea, but you're going to need to spend more time figuring her out to get her to more than this."
                          $ title = "What do you do now?"
                          menu:
                            "Spend some time exploring this":
                              player.c "Don't be shy.  Barking feels good.  Didn't you come here to feel good?"
                              wt_image ms2_visit_1_8
                              fairyn.c "No"
                              player.c "Why did you come here?"
                              wt_image ms2_visit_1_38
                              fairyn.c "To be treated like a nobody.  As less than a nobody.  M said you might be the sort of guy I could warm up to, if I was in one of my 'moods' again."
                              player.c "M was right.  I am going to treat you as a nobody.  What did I tell you to do?"
                              wt_image ms2_visit_1_8
                              fairyn.c "Bark"
                              player.c "Do women bark?"
                              fairyn.c "No"
                              wt_image ms2_visit_1_7
                              player.c "No.  Dirty bitches bark.  Bark for me, bitch."
                              fairyn.c "WOOF  WOOF  WOOF!!"
                              add tags 'hypno_treat_her_like_nobody' to fairyn
                              $ fairyn.initial_arousal = 2
                            "Do something else":
                              jump menu_master_m_message_fairyn_hypno
                            "Send her home":
                              jump master_m_message_fairyn_choice
                        else:
                          player.c "You came here to be treated as a nobody.  Do women bark?"
                          wt_image ms2_visit_1_8
                          fairyn.c "No"
                          player.c "No.  Dirty bitches like you bark.  Bark for me, bitch."
                          wt_image ms2_visit_1_7
                          fairyn.c "WOOF  WOOF  WOOF!!"
                        if fairyn.has_tag('hypno_treat_her_like_nobody'):
                          player.c "On all fours, bitch.  Dogs like you don't get to stand."
                          wt_image ms2_visit_1_22
                          "She drops like a rock to the floor, still barking."
                          fairyn.c "WOOF  WOOF  WOOF  WOOF!!"
                          $ title = "Now what?"
                          menu menu_master_message_fairyn_bark:
                            "Have her follow you around" if not fairyn.has_tag('message_bark_follow') and not fairyn.has_tag('message_bark_sex'):
                              wt_image ms2_visit_1_45
                              player.c "Stay close, you stupid dog."
                              fairyn.c "WOOF  WOOF!!"
                              wt_image ms2_visit_1_23
                              "She follows you around the house, staying close to your ankles. At one point she gets in front of you and almost trips you."
                              player.c "Watch it, you dumb animal. Stay beside me, not in front."
                              wt_image ms2_visit_1_22
                              "You'd never hit a real animal, but this one's a different case.  You punctuate your rebuke with a slap on her nose ... *SMACK*.  She whines pathetically, looking up at you with big puppy dog eyes."
                              fairyn.c "nnnnnnn"
                              add tags 'message_bark_follow' to fairyn
                              jump menu_master_message_fairyn_bark
                            "Fuck your bitch" if not fairyn.has_tag('message_bark_sex'):
                              wt_image ms2_visit_1_45
                              player.c "Put your snout on the floor, bitch, and raise your ass."
                              wt_image ms2_visit_1_34
                              "She whines like a puppy dog as you shove your cock up her ass ..."
                              fairyn.c "nnnnnnn"
                              wt_image ms2_visit_1_31
                              "... but stays obediently in place until you've taken your pleasure from her."
                              wt_image ms2_visit_1_50
                              player.c "[player.orgasm_text]"
                              wt_image ms2_visit_1_51
                              player.c "Clean up that mess on the floor, bitch."
                              wt_image ms2_visit_1_22
                              player.c "Yes, with your tongue, you stupid animal.  That's how dogs clean themselves."
                              $ fairyn.hypno_sex_count += 1
                              orgasm notify
                              add tags 'message_bark_sex' to fairyn
                              jump menu_master_message_fairyn_bark
                            "Do something else" if not fairyn.has_tag('message_bark_sex'):
                              jump menu_master_m_message_fairyn_hypno
                            "Send her home":
                              jump master_m_message_fairyn_choice
                      "Tell her to suck your dick" if not fairyn.has_tag('hypno_treat_her_like_nobody'):
                        player.c "You and I are going to talk.  You want me to comfortable while we talk.  Suck on my cock while we talk. I'll be more comfortable and we'll both enjoy our talk more when you're sucking my dick."
                        wt_image ms2_visit_1_7
                        fairyn.c "No"
                        player.c "You came here to have sex with me.  Sucking my cock gets me ready to have sex with you."
                        wt_image ms2_visit_1_38
                        fairyn.c "Not that kind of sex.  You need to use me."
                        player.c "You came here so that I could use you for my own sexual pleasure."
                        wt_image ms2_visit_1_8
                        fairyn.c "Yes, if you're smart enough and confident enough to treat me as a nobody.  As less than a nobody, actually.  As a piece of meat, not a girlfriend giving a BJ."
                        add tags 'hypno_treat_her_like_nobody' to fairyn
                        $ fairyn.initial_arousal = 2
                        $ title = "What do you do now?"
                        jump menu_master_m_message_fairyn_hypno
                      "Send her home":
                        jump master_m_message_fairyn_choice
                  "Let her go":
                    wt_image current_location.image
                    "She walks out without saying another word.  At least you still have time to do something else with the rest of your day."
              else:
                wt_image current_location.image
                "She walks out without saying another word.  At least you still have time to do something else with the rest of your day."
            # leaving, too mad to hypnotize
            elif fairyn.temporary_count == 3:
              wt_image current_location.image
              "She's gone before you can say another word.  At least you still have time to do something else with the rest of your day."
            # she masturbates for you
            elif fairyn.temporary_count == 4:
              if fairyn.has_tag('kneeling'):
                player.c "Yes, that is what I want. Get on with it."
              else:
                "You take out your cock and start stroking it as she watches you intently."
              wt_image ms2_visit_1_10
              "She pulls off her panties, moaning softly in excitement as she spreads herself open for you."
              fairyn.c "oooooo"
              wt_image ms2_visit_1_11
              "She arouses quickly, moaning as she rubs her hand against her labia and clit."
              fairyn.c "ooooooo!!"
              player.c "Make sure I can see."
              wt_image ms2_visit_1_46
              "Dutifully, she spreads her fingers as she rubs herself, giving you a clear view of the wetness dripping out of her."
              fairyn.c "ooooooo!!"
              wt_image ms2_visit_1_11
              "Before long, her body begins to shake as she cums, her hand pressed hard against her clit, her fingers holding her sex open for you to watch."
              wt_image ms2_visit_1_12
              fairyn.c "OOOOO!!!"
              $ fairyn.masturbation_count += 1
              $ fairyn.orgasm_count += 1
              $ title = "What now?"
              menu:
                "Thank her for the show":
                  wt_image ms2_visit_1_13
                  player.c "Thanks for the show."
                  fairyn.c "Mmmmm.  Thanks yourself.  I'll get going as soon as my legs recover."
                  change player energy by -energy_short
                "Tell her to get out":
                  wt_image ms2_visit_1_13
                  player.c "You've had your fun.  Now get out."
                  fairyn.c "Mmmm, I love a guy who doesn't need to cuddle.  Do I get to change before I go?"
                  player.c "No"
                  wt_image ms2_visit_1_36
                  "She chuckles."
                  fairyn.c "This is going to be a fun drive home in my convertible."
                  change player energy by -energy_short
                "Jerk off on her":
                  wt_image ms2_visit_1_12
                  if fairyn.has_tag('kneeling'):
                    "You remove your hard on from your pants and step closer to her."
                  else:
                    "Still stroking your cock, you step closer to her."
                  wt_image ms2_visit_1_9
                  fairyn.c "Mmmmm.  Is that for me?"
                  player.c "What's coming out of it is."
                  wt_image ms2_visit_1_10
                  fairyn.c "Ooooo, yes.  Cover me with cum like a worthless whore."
                  wt_image ms2_visit_1_14
                  "She opens her mouth and moans as you empty your load on her."
                  player.c "[player.orgasm_text]"
                  fairyn.c "oooooo!!"
                  wt_image ms2_visit_1_15
                  "When your balls finally stop spurting jizz onto her, she gently licks the head of your cock."
                  fairyn.c "I'd have started masturbating as soon as I got here if I'd known you'd use me as a cum dump afterwards."
                  # setting temporary_count to >5 makes you eligible for her gift if otherwise qualify; making it 10 keeps other options from firing in error
                  $ fairyn.temporary_count = 10
                  $ fairyn.facial_count += 1
                  orgasm notify
                  $ title = "What now?"
                  menu:
                    "Thank her for the show":
                      player.c "Thanks for the show."
                      wt_image ms2_visit_1_47
                      fairyn.c "Mmmmm.  Thanks yourself.  I'll get going as soon as my legs recover."
                      change player energy by -energy_short
                    "Tell her to get out":
                      player.c "You've had your fun.  Now get out."
                      wt_image ms2_visit_1_47
                      fairyn.c "Mmmm, I love a guy who doesn't need to cuddle.  Do I get to change before I go?"
                      player.c "No"
                      "She chuckles."
                      fairyn.c "This is going to be a fun drive home in my convertible."
                      change player energy by -energy_short
              $ fairyn.initial_outcome = 3
            # earned her submission but sent her home without dom'ing her
            elif fairyn.temporary_count == 5:
              if fairyn.has_tag('kneeling'):
                wt_image ms2_visit_1_39
              else:
                wt_image ms2_visit_1_40
              "She's not happy at being dismissed. She's clearly not used to rejection, and she doesn't like it, especially not after making it known that you can do anything you want with her."
              wt_image ms2_visit_1_6
              "She came here hoping you would treat her as a nothing, but now that you've really treated her like something that's worthless to you, it's not quite the sensation she had in mind."
              wt_image current_location.image
              "Silent but fuming, she leaves."
            # domination options
            elif fairyn.temporary_count > 5 and fairyn.temporary_count < 10:
              # asked for her gag
              if fairyn.temporary_count == 6:
                wt_image ms2_visit_1_48
                "She brings you the gag and you put it on her.  She took some care in buying it, as it's the perfect fit, stretching her mouth to it's limit."
                wt_image ms2_visit_1_18
                "You leave her kneeling and gagged in the middle of the floor, letting the drool slowly escape from her mouth and drip down her chin."
                $ title = "What now?"
                menu menu_master_m_message_fairyn_dominate_6:
                  "Leave her there" if not fairyn.has_tag('message_dom_6'):
                    wt_image ms2_visit_1_19
                    "You leave her there for a while.  For the most part you ignore her, but once in a while she catches your eye.  When she does, her eyes fairly beg out to you 'Use me!'"
                    add tags 'message_dom_6' to fairyn
                    $ title = "What do you do?"
                    jump menu_master_m_message_fairyn_dominate_6
                  "Take some photos" if not player.has_tag('fairyn_gagged_photos'):
                    add tags 'fairyn_gagged_photos' to player
                    player.c "You don't mind me taking a few photos, do you?  To remember the time a stupid, worthless slut showed up at my house with her own gag?"
                    wt_image ms2_visit_1_18
                    "She hesitates just a moment ..."
                    wt_image ms2_visit_1_19
                    "... then nods in consent."
                    wt_image ms2_visit_1_54
                    "You take a picture of just her body, first, to see how she reacts."
                    wt_image ms2_visit_1_55
                    "Then you make it clear to her that you're about to photograph her face.  When her only response is to breathe more heavily, you snap the pic."
                    wt_image ms2_visit_1_19
                    "She trembles as you put your phone away.  She has no idea who you may share these photos with, but her only reaction to that uncertainty seems to be arousal."
                    $ title = "What now?"
                    jump menu_master_m_message_fairyn_dominate_6
                  "Fuck her mouth":
                    call master_m_message_fairyn_mouth from _call_master_m_message_fairyn_mouth
                  "Fuck her pussy":
                    call master_m_message_fairyn_pussy from _call_master_m_message_fairyn_pussy
                  "Fuck her ass":
                    call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass
                  "Send her home" if fairyn.has_tag('message_dom_6'):
                    wt_image ms2_visit_1_48
                    "When she's at her limit, you unbuckle the gag.  She sighs in relief as you remove it from her mouth."
                    wt_image ms2_visit_1_9
                    fairyn.c "oohhh  ...  Are you going to fuck me now?"
                    player.c "No"
                    wt_image ms2_visit_1_5
                    fairyn.c "No??"
                    player.c "No, I'm not interested in fucking a worthless slut like you.  You're too far beneath me.  Get out."
                    wt_image ms2_visit_1_56
                    "She trembles in humiliation, but accepts your decision.  Chastened, she gets her stuff together and heads home."
                    $ fairyn.initial_outcome = 4
                    change player energy by -energy_very_short
              # asked for her paddle
              elif fairyn.temporary_count == 7:
                wt_image ms2_visit_1_1
                "She retrieves the paddle from her bag and hands it to you."
                fairyn.c "Where do you want me?"
                $ title = "What position to you want to paddle her in?"
                menu:
                  "Bent over":
                    player.c "Bend over and make your ass an easy target for me. I'm not going to waste any more energy on you than I need to."
                    wt_image ms2_visit_1_20
                    "Trembling slightly, she leans against a railing and presents her ass to you."
                    "*smackkk*"
                    fairyn.c "Ow!"
                    "*smackkk*"
                    fairyn.c "Oowww!"
                    "*smackkk*"
                    fairyn.c "Ohh ... Oowww!!"
                    "*smackkk*"
                    fairyn.c "Ohhh ... Oowww Oowww!!"
                    "*smackkk*"
                    fairyn.c "OOWWWW!!!  Oowww  Oowww  Oowwww!!"
                    wt_image ms2_visit_1_21
                    "When you finally finish she looks at you with  ... respect?  It's hard to tell for sure.  What's more obvious is the invitation she sends as she pulls down her panties after rubbing her sore ass."
                  "On the floor":
                    player.c "Get down on the floor like the worthless worm you are."
                    wt_image ms2_visit_1_22
                    "Trembling, she lowers herself to the ground and presents her ass to you."
                    "*smackkk*"
                    fairyn.c "Ow!"
                    "*smackkk*"
                    fairyn.c "Oowww!"
                    "*smackkk*"
                    fairyn.c "Ohh ... Oowww!!"
                    "*smackkk*"
                    fairyn.c "Ohhh ... Oowww Oowww!!"
                    "*smackkk*"
                    fairyn.c "OOWWWW!!!  Oowww  Oowww  Oowwww!!"
                    wt_image ms2_visit_1_23
                    "When you finally finish she looks at you with  ... respect?  It's hard to tell for sure.  What's more obvious is the invitation she sends as she wiggles her sore ass at you."
                $ title = "What do you do?"
                menu:
                  "Fuck her mouth":
                    call master_m_message_fairyn_mouth from _call_master_m_message_fairyn_mouth_1
                  "Fuck her pussy":
                    call master_m_message_fairyn_pussy from _call_master_m_message_fairyn_pussy_1
                  "Fuck her ass":
                    call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass_1
                  "Send her home":
                    player.c "You can go now."
                    wt_image ms2_visit_1_5
                    fairyn.c "Aren't you going to ..."
                    player.c "Fuck you?  No, I'm not interested in fucking a worthless slut like you.  You're too far beneath me.  Get out."
                    wt_image ms2_visit_1_56
                    "She trembles in humiliation, but accepts your decision.  Chastened, she gets her stuff together and heads home."
                    $ fairyn.initial_outcome = 4
                    change player energy by -energy_short
              # asked for both gag and paddle
              elif fairyn.temporary_count == 8:
                wt_image ms2_visit_1_48
                "She brings you the gag and paddle.  You put the gag on her.  She took some care in buying it, as it's the perfect fit, stretching her mouth to it's limit."
                wt_image ms2_visit_1_18
                "You leave her kneeling and gagged in the middle of the floor, letting the drool slowly escape from her mouth and drip down her chin."
                $ title = "Take some photos?"
                menu:
                  "Yes":
                    add tags 'fairyn_gagged_photos' to player
                    player.c "You don't mind me taking a few photos, do you?  To remember the time a stupid, worthless slut showed up at my house with her own gag?"
                    wt_image ms2_visit_1_18
                    "She hesitates just a moment ..."
                    wt_image ms2_visit_1_19
                    "... then nods in consent."
                    wt_image ms2_visit_1_54
                    "You take a picture of just her body, first, to see how she reacts."
                    wt_image ms2_visit_1_55
                    "Then you make it clear to her that you're about to photograph her face.  When her only response is to breathe more heavily, you snap the pic."
                    wt_image ms2_visit_1_19
                    "She trembles as you put your phone away.  She has no idea who you may share these photos with, but her only reaction to that uncertainty seems to be arousal."
                  "No, just use the paddle":
                    pass
                "As she waits, you make a show of examining the paddle she brought you."
                $ title = "Take out your cock?"
                menu:
                  "Yes":
                    wt_image ms2_visit_1_24
                    "You hold the paddle against her face and remove your cock, letting her know you're turned on at the prospect of using it."
                    player.c "I'm going to have fun hurting you with this."
                    wt_image ms2_visit_1_52
                    "The look on her face as she gazes up at you suggests she's looking forward to being hurt."
                  "Not yet":
                    wt_image ms2_visit_1_53
                    "You rub the paddle slowly across her face."
                    player.c "I'm going to have fun hurting you with this."
                    "The look on her face as she gazes up at you suggests she's looking forward to being hurt."
                wt_image ms2_visit_1_48
                player.c "It's not going to be as much fun, though, if I can't hear you scream."
                wt_image ms2_visit_1_5
                "You take the gag out of her mouth and point to the floor in front of you."
                player.c "Get down on the ground like the worthless worm you are and raise your ass so I can hurt you."
                wt_image ms2_visit_1_22
                "Trembling, she presents her ass to you."
                "*smackkk*"
                fairyn.c "Ow!"
                "*smackkk*"
                fairyn.c "Oowww!"
                "*smackkk*"
                fairyn.c "Ohh  Oowww!!"
                "*smackkk*"
                fairyn.c "Ohhh  Oowww Oowww!!"
                "*smackkk*"
                fairyn.c "OOWWWW!!!  Oowww  Oowww  Oowwww!!"
                wt_image ms2_visit_1_23
                "When you finally she looks at you with  ... respect?  It's hard to tell for sure.  What's more obvious is the invitation she sends as she wiggles her sore ass at you."
                $ title = "What do you do?"
                menu:
                  "Fuck her mouth":
                    call master_m_message_fairyn_mouth from _call_master_m_message_fairyn_mouth_2
                  "Fuck her pussy":
                    call master_m_message_fairyn_pussy from _call_master_m_message_fairyn_pussy_2
                  "Fuck her ass":
                    call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass_2
                  "Send her home":
                    player.c "You can go now."
                    wt_image ms2_visit_1_5
                    fairyn.c "Aren't you going to ..."
                    player.c "Fuck you?  No, I'm not interested in fucking a worthless slut like you.  You're too far beneath me.  Get out."
                    wt_image ms2_visit_1_56
                    "She trembles in humiliation, but accepts your decision.  Chastened, she gets her stuff together and heads home."
                    $ fairyn.initial_outcome = 4
                    change player energy by -energy_short
              # dom her with nothing
              elif fairyn.temporary_count == 9:
                player.c "I don't need either of those to deal with a worthless slut like you."
                wt_image ms2_visit_1_9
                fairyn.c "Mmmmm ... Use me whatever way you want.  Make me a toy for your pleasure."
                $ title = "What do you do?"
                menu:
                  "Fuck her mouth":
                    call master_m_message_fairyn_mouth from _call_master_m_message_fairyn_mouth_3
                  "Fuck her pussy":
                    call master_m_message_fairyn_pussy from _call_master_m_message_fairyn_pussy_3
                  "Fuck her ass":
                    call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass_3
            # there are possible jumps above this, but if none taken now need to jump to an ending label
            if fairyn.temporary_count > 0:
                jump master_m_message_fairyn_ending
          "No, she's not your type" if not fairyn.has_tag('message_send_away'):
            player.c "I think there's been a mistake."
            wt_image ms2_car_8
            "She pouts slightly."
            fairyn.c "Nnnnnn, are you going to send me home without even letting me in? I promise I won't bite ... "
            wt_image ms2_car_6
            "... unless you want me to?"
            add tags 'message_send_away' to fairyn
            $ title = "Change your mind?"
            jump menu_master_message_change
          "No, you don't trust her" if not fairyn.has_tag('message_send_away'):
            player.c "I think there's been a mistake."
            wt_image ms2_car_8
            "She pouts slightly."
            fairyn.c "Nnnnnn, are you going to send me home without even letting me in? I promise I won't bite ... "
            wt_image ms2_car_6
            "... unless you want me to?"
            add tags 'message_send_away' to fairyn
            $ title = "Change your mind?"
            jump menu_master_message_change
          "Send her away" if fairyn.has_tag('message_send_away'):
            # resolved without playing with Fairyn
            $ master_m.lent_him_a_slave = 6
            player.c "You'd best go."
            wt_image ms2_car_2
            fairyn.c "Fuck!!! What a waste of time!  Fine.  Piss off!!"
            "She puts on a pair of sunglasses and pulls out of your driveway, tires squealing."
        rem tags 'message_send_away' from fairyn
        add tags 'no_hypnosis' to fairyn
        call character_location_return(fairyn) from _call_character_location_return_195
        wt_image current_location.image
      "Not Yet":
        "This engagement offer will never expire, so you can take your time getting back to Master M."
        $ master_m.current_client_action.name = "Reply to Master M"
        if not master_m.wait_on_message:
          $ master_m.wait_on_message = True
          $ master_m.wait_for_message_period = 10000000
      "Never (Deletes Message)":
        # resolved without playing with Fairyn
        $ master_m.lent_him_a_slave = 6
        $ master_m.change_status("rejected")
  # Diamond
  elif master_m.current_message == 0:
    master_m.c "{i}I'm intrigued by your profile. You say you're skilled at behavior modification. I have a little challenge for you.{/i}"
    master_m.c "{i}My slave girl has been willfully disobedient. My punishments have, of late, been of little effect. She seems to enjoy them too much. I'm not ready to give up on her yet, so I'd like to try something different.{/i}"
    master_m.c "{i}I'd like to send her to you for an evening of punishment. I trust you know the difference between punishment and abuse? I'd like you to send her back to me suitably chastised.{/i}"
    master_m.c "{i}I'll pay you your normal fee, and you may make such use of her as you choose while she is there.{/i}"
    master_m.c "{i}I want her punishment to proceed soon, so if you're going to accept, I need you to do so this week or next.  ~ M{/i}"
    "This may not be your preferred clientèle, but it is a paying gig."
    $ title = "Accept the engagement?"
    menu:
      "Yes (Ends Day)":
        $ diamond.training_session()
        rem tags 'no_hypnosis' from diamond
        wt_image front_door
        "M tells you he'll send his recalcitrant slave girl right over. A few minutes later, there's a knock on your door."
        wt_image ms1_training_1
        "A petite, caramel-skinned girl answers the door."
        wt_image ms1_training_55
        diamond.c "Hello, Sir.  Should I come in?"
        $ title = "Proceed with training her?"
        menu:
          "Yes":
            pass
          "No (ends this opportunity)":
            wt_image ms1_training_53
            player.c "Not interested."
            wt_image front_door
            "You send her away and get on with your day."
            jump master_m_diamond_aborted_training
        call forced_movement(backyard) from _call_forced_movement_396
        summon diamond
        wt_image ms1_training_56
        "You bring her around to your backyard ..."
        wt_image ms1_training_54
        "... where she takes off her clothes ..."
        wt_image ms1_training_3
        "... puts up her hair ..."
        wt_image ms1_training_57
        "... and dons a collar."
        wt_image ms1_training_4
        diamond.c "I'm ready now, Sir."
        if player.has_tag('dominant'):
          wt_image ms1_training_58
          "She looks carefully at you. When you catch her eye, she slowly lowers her head. She's a natural submissive and responds instinctively to your natural dominance."
          wt_image ms1_training_60
          "Meeting you in these circumstances is punishment all on its own, as she would have preferred to have impressed you, rather than being introduced as a bad sub in need of correction."
          sys "She's feeling chastised already."
          $ diamond.training_submission_level += 1
        elif player.has_tag('supersexy'):
          wt_image ms1_training_59
          "She looks more closely at you, then shyly turns away and starts to blush. It seems she likes what she sees."
          sys "She's feeling aroused already."
          $ diamond.training_desire_level += 1
        else:
          "She looks at you, uncertain as to what to make of you."
        player.c "What's your name?"
        wt_image ms1_training_61
        diamond.c "I don't have one right now, Sir. My Master took it away from me as part of my punishment."
        player.c "Really?  What was your name before he took it away?"
        diamond.c "Diamond, Sir."
        player.c "So what is he calling you now? He must have some term to refer to you as?"
        diamond.c "Just slave, Sir."
        $ title = "What are you going to call her?"
        menu:
          "Diamond":
            player.c "Well, I need to call you something, so how about Diamond, since that is your name."
            wt_image ms1_training_4
            $ diamond.name = "Diamond"
            $ diamond.training_name = "Diamond"
            diamond.c "Okay"
            $ diamond.training_submission_level -= 1
            if player.has_tag('dominant'):
              sys "She's feeling less chastised."
          "Slave":
            player.c "Well, I need to call you something, and Slave seems as good as anything."
            $ diamond.name = "Slave"
            $ diamond.training_name = "Slave"
            diamond.c "Yes, Sir."
          "Cunt":
            player.c "Well, I need to call you something. Cunt seems suitable for you. What do you think of that name?"
            wt_image ms1_training_5
            "She cringes at the term."
            $ diamond.name = "Cunt"
            $ diamond.training_name = "Cunt"
            diamond.c "Whatever you say, Sir."
            $ diamond.training_desire_level -= 1
            if player.has_tag('supersexy'):
              sys "Her arousal has decreased"
          "Fucktoy":
            player.c "Well, I need to call you something. How about Fucktoy? That is what you're going to be for me tonight, isn't it? My own personal 3 hole fucktoy?"
            wt_image ms1_training_6
            "She recoils slightly at the term, but her breathing gets a little faster."
            $ diamond.name = "Fucktoy"
            $ diamond.training_name = "Fucktoy"
            diamond.c "Yes, Sir. If that's what you want from me, Sir."
            $ diamond.training_desire_level += 1
            $ diamond.training_submission_level += 1
            if player.has_tag('supersexy'):
              sys "Her arousal has increased."
            if player.has_tag('dominant'):
              sys "She's feeling more chastised."
          "Beautiful":
            player.c "Well, I need to call you something. How about Beautiful, because that's the first thing I think of when I look at you."
            wt_image ms1_training_59
            "She blushes."
            $ diamond.name = "Beautiful"
            $ diamond.training_name = "Beautiful"
            diamond.c "Thank you, Sir. Yes, I'd like that Sir."
            $ diamond.training_desire_level += 1
            $ diamond.training_submission_level -= 1
            if player.has_tag('supersexy'):
              sys "Her arousal has increased."
            if player.has_tag('dominant'):
              sys "She's feeling less chastised."
        player.c "Are you here voluntarily, [diamond.training_name]?"
        wt_image ms1_training_4
        diamond.c "Yes, Sir. My Master ordered me to come here to be punished, but I chose to obey him of my own free will."
        player.c "And you consent to whatever I choose to do with you today?"
        wt_image ms1_training_61
        diamond.c "Yes, Sir. As long as you send me home in one piece and with no injuries, my Master has instructed me to obey you as I would him."
        # if can hypno, choose whether to train her that way or normally
        if player.can_hypno(diamond):
          $ title = "Do you want to hypnotize her?"
          menu:
            "Yes, train her through hypnosis":
              $ diamond.hypno_session() # deletes energy and records she was hypnotized
              add tags 'hypnotized_now' to diamond
              player.c "Look at this, [diamond.training_name]."
              call focus_image from _call_focus_image_1
              player.c "You and I are going to have a chat. I am going to talk and you are going to listen. Listen to me. Only to me now. Only my words."
              wt_image ms1_training_52
              "She came here intending to obey, so it's not surprising that she falls quickly under your trance."
              player.c "Take off your top, [diamond.training_name], so that we can be comfortable for our talk."
              wt_image ms1_training_62
              player.c "In fact, take off everything. You're a slave girl, so you must be used to being naked for your Master's pleasure. Get naked to please me while we talk."
              wt_image ms1_training_63
              "She quickly strips."
              $ title = "Talk to her like this?"
              menu:
                "This is fine":
                  pass
                "Have her blow you while you talk to her":
                  player.c "Your Master told you to obey me tonight, didn't he, [diamond.training_name]?"
                  wt_image ms1_training_7
                  diamond.c "Yes, Sir."
                  player.c "And that includes pleasuring me sexually."
                  wt_image ms1_training_41
                  diamond.c "Yes, Sir."
                  player.c "Get on your knees and suck my cock while we chat, [diamond.training_name]."
                  wt_image ms1_training_66
                  diamond.c "Yes, Sir."
                  wt_image ms1_training_67
                  "She takes out your cock and demonstrates that whatever other training she may require ..."
                  wt_image ms1_training_68
                  "... she's learned how to give a blowjob."
                  diamond.c "Would you like me to use my hands, too?"
                  wt_image ms1_training_69
                  "Why not?  They're soft and she seems to be good with them."
                  add tags 'hypnotized_bj_now' to diamond
            "No, don't hypnotize her":
              pass
        # conversation prior to training
        if diamond.has_tag('hypnotized_bj_now'):
          player.c "Why did your Master send you to me?"
          wt_image ms1_training_70
          diamond.c "I was a brat. I got mad at him and spilled orange juice over his lap."
          wt_image ms1_training_71
          player.c "What was he doing to you?"
          wt_image ms1_training_72
          diamond.c "Nothing. He was ignoring me and trying to read the morning news."
          wt_image ms1_training_71
          player.c "What did you think would happen?"
          wt_image ms1_training_72
          diamond.c "I thought he'd punish me."
          wt_image ms1_training_71
          player.c "Did you want him to punish you?"
          wt_image ms1_training_70
          diamond.c "Yes"
          wt_image ms1_training_71
          player.c "Do you like his punishments?"
          wt_image ms1_training_70
          diamond.c "No, I don't like being punished, but I do like it when he spanks me or hurts my tits or pussy."
          wt_image ms1_training_71
          player.c "Are you a masochist?"
          wt_image ms1_training_70
          diamond.c "No. Pain doesn't turn me on. Having him discipline me does, though, especially when he does it in a way that feels intimate and sexual to me."
          wt_image ms1_training_71
          player.c "What about 'normal' sex. Do you like that, or only D/s?"
          wt_image ms1_training_73
          diamond.c "I love normal sex! When my Master takes me into his bed and makes love to me gently, it's the best! I don't even care if he sticks his dick in my ass partway through to remind me he owns me."
          wt_image ms1_training_69
          diamond.c "Having him treat me like a girlfriend when I'm just his slave is perversely kinky in a totally messed up way."
          wt_image ms1_training_71
          player.c "Maybe you've been acting up because you don't want to be his slave anymore? Maybe you want to be his girlfriend?"
          wt_image ms1_training_70
          diamond.c "No. I'm a slave. I was born to be a slave. I knew it even when I was growing up. People were supposed to order me around. It was my role."
          wt_image ms1_training_72
          diamond.c "I ended up in a few abusive relationships as a teenager because I didn't know enough about who I was, and I mistook the abuse for the type of treatment I need."
          wt_image ms1_training_73
          diamond.c "Eventually I learned about BDSM and found myself. I went through a few Doms until I met my Master and accepted his collar. I'm happy now."
          wt_image ms1_training_71
          player.c "As long as he gives you his attention when you want it?"
          wt_image ms1_training_72
          diamond.c "Yeah. I think that's why he sent me to you. Being forced to serve another man instead of receiving his attention is a new form of punishment he's trying out to see if it'll teach me to not act like a brat."
        elif diamond.has_tag('hypnotized_now'):
          player.c "Why did your Master send you to me?"
          wt_image ms1_training_41
          diamond.c "I was a brat. I got mad at him and spilled orange juice over his lap."
          player.c "What was he doing to you?"
          wt_image ms1_training_63
          diamond.c "Nothing. He was ignoring me and trying to read the morning news."
          player.c "What did you think would happen?"
          wt_image ms1_training_65
          diamond.c "I thought he'd punish me."
          player.c "Did you want him to punish you?"
          wt_image ms1_training_41
          diamond.c "Yes"
          player.c "Do you like his punishments?"
          wt_image ms1_training_65
          diamond.c "No, I don't like being punished, but I do like it when he spanks me or hurts my tits or pussy."
          player.c "Are you a masochist?"
          wt_image ms1_training_63
          diamond.c "No. Pain doesn't turn me on. Having him discipline me does, though, especially when he does it in a way that feels intimate and sexual to me."
          player.c "What about 'normal' sex. Do you like that, or only D/s?"
          wt_image ms1_training_7
          diamond.c "I love normal sex! When my Master takes me into his bed and makes love to me gently, it's the best! I don't even care if he sticks his dick in my ass partway through to remind me he owns me."
          wt_image ms1_training_41
          diamond.c "Having him treat me like a girlfriend when I'm just his slave is perversely kinky in a totally messed up way."
          player.c "Maybe you've been acting up because you don't want to be his slave anymore? Maybe you want to be his girlfriend?"
          wt_image ms1_training_63
          diamond.c "No. I'm a slave. I was born to be a slave. I knew it even when I was growing up. People were supposed to order me around. It was my role."
          wt_image ms1_training_65
          diamond.c "I ended up in a few abusive relationships as a teenager because I didn't know enough about who I was, and I mistook the abuse for the type of treatment I need."
          wt_image ms1_training_63
          diamond.c "Eventually I learned about BDSM and found myself. I went through a few Doms until I met my Master and accepted his collar. I'm happy now."
          player.c "As long as he gives you his attention when you want it?"
          wt_image ms1_training_41
          diamond.c "Yeah. I think that's why he sent me to you. Being forced to serve another man instead of receiving his attention is a new form of punishment he's trying out to see if it'll teach me to not act like a brat."
        else:
          player.c "Why did your Master send you to me?"
          wt_image ms1_training_60
          diamond.c "I was a brat. I got mad at him and spilled orange juice over his lap."
          player.c "What was he doing to you?"
          wt_image ms1_training_61
          diamond.c "Nothing. He was ignoring me and trying to read the morning news."
          player.c "What did you think would happen?"
          wt_image ms1_training_60
          diamond.c "I thought he'd punish me."
          player.c "Did you want him to punish you?"
          wt_image ms1_training_61
          "She hesitates."
          diamond.c "I guess."
          player.c "Do you like his punishments?"
          wt_image ms1_training_58
          "She shakes her head."
          diamond.c "No. No, I don't like being punished, but I do like it when he spanks me or hurts my tits or pussy."
          player.c "Are you a masochist?"
          wt_image ms1_training_61
          diamond.c "I don't think so. Pain doesn't turn me on. Having him discipline me does, though, especially when he does it in a way that feels intimate and sexual to me."
          player.c "What about 'normal' sex. Do you like that, or only D/s?"
          wt_image ms1_training_59
          diamond.c "I love normal sex! When my Master takes me into his bed and makes love to me gently, it's the best! I don't even care if he sticks his dick in my ass partway through to remind me he owns me."
          wt_image ms1_training_6
          diamond.c "Having him treat me like a girlfriend when I'm just his slave is perversely kinky in a totally messed up way, I guess."
          player.c "Maybe you've been acting up because you don't want to be his slave anymore? Maybe you want to be his girlfriend?"
          wt_image ms1_training_61
          diamond.c "No. I'm a slave. I was born to be a slave. I knew it even when I was growing up. People were supposed to order me around. It was my role."
          wt_image ms1_training_60
          diamond.c "I ended up in a few abusive relationships as a teenager because I didn't know enough about who I was, and I mistook the abuse for the type of treatment I need."
          wt_image ms1_training_58
          diamond.c "Eventually I learned about BDSM and found myself. I went through a few Doms until I met my Master and accepted his collar. I'm happy now."
          player.c "As long as he gives you his attention when you want it?"
          wt_image ms1_training_61
          diamond.c "I guess. Yeah. I think that's why he sent me to you. Being forced to serve another man instead of receiving his attention is a new form of punishment he's trying out to see if it'll teach me to not act like a brat."
        # special question just for Natural Dom player type, as it ties to his backstory
        if player.short_name == 'nd':
          $ title = "Tell her a hard truth?"
          menu:
            "Tell her something she doesn't want to hear":
              if diamond.has_tag('hypnotized_bj_now'):
                wt_image ms1_training_71
                player.c "I'm going to tell you something you don't want to hear, but I think it's important for you to know, because you may need to get ready for the idea."
                wt_image ms1_training_72
                diamond.c "What?"
                wt_image ms1_training_71
                player.c "He may need to sell you."
                wt_image ms1_training_70
                diamond.c "What do you mean?"
                wt_image ms1_training_71
                player.c "If he cares for you, if he's a good Master, the day will come when he realizes that he can't give you what you need. Not because there's anything wrong with him. Not because there's anything wrong with you."
                wt_image ms1_training_69
                player.c "But you're in love with him. And he may not be able to give you the experience of being owned that you need."
                wt_image ms1_training_68
                player.c "Maybe you can accept being his submissive and give up the idea of slavery.  But if you need slavery, true slavery, the time will come when he may have to pass you on to someone else."
                wt_image ms1_training_70
                diamond.c "Slaves can love their Masters!"
                wt_image ms1_training_69
                player.c "Yes. They can and often do. I'm talking about you, not all slaves."
                wt_image ms1_training_68
                player.c "He's the first man you've loved and the first man you've served. You're fighting a power struggle with him that he can't win, no matter what approach he takes, because everything he does is filtered through your conflicted views of him."
                wt_image ms1_training_72
                diamond.c "Help me then! Teach me whatever lesson I need to learn so I can stop fighting him and serve him properly."
                wt_image ms1_training_68
                player.c "I'll do my best."
              elif diamond.has_tag('hypnotized_now'):
                player.c "I'm going to tell you something you don't want to hear, but I think it's important for you to know, because you may need to get ready for the idea."
                wt_image ms1_training_63
                diamond.c "What?"
                player.c "He may need to sell you."
                wt_image ms1_training_65
                diamond.c "What do you mean?"
                player.c "If he cares for you, if he's a good Master, the day will come when he realizes that he can't give you what you need. Not because there's anything wrong with him. Not because there's anything wrong with you."
                wt_image ms1_training_7
                player.c "But you're in love with him. And he may not be able to give you the experience of being owned that you need."
                wt_image ms1_training_63
                player.c "Maybe you can accept being his submissive and give up the idea of slavery.  But if you need slavery, true slavery, the time will come when he may have to pass you on to someone else."
                wt_image ms1_training_41
                diamond.c "Slaves can love their Masters!"
                player.c "Yes. They can and often do. I'm talking about you, not all slaves."
                wt_image ms1_training_63
                player.c "He's the first man you've loved and the first man you've served. You're fighting a power struggle with him that he can't win, no matter what approach he takes, because everything he does is filtered through your conflicted views of him."
                wt_image ms1_training_65
                diamond.c "Help me then! Teach me whatever lesson I need to learn so I can stop fighting him and serve him properly."
                player.c "I'll do my best."
              else:
                player.c "I'm going to tell you something you don't want to hear, but I think it's important for you to know, because you may need to get ready for the idea."
                wt_image ms1_training_58
                diamond.c "What?"
                player.c "He may need to sell you."
                wt_image ms1_training_5
                diamond.c "What do you mean?"
                player.c "If he cares for you, if he's a good Master, the day will come when he realizes that he can't give you what you need. Not because there's anything wrong with him. Not because there's anything wrong with you."
                wt_image ms1_training_6
                player.c "But you're in love with him. And he may not be able to give you the experience of being owned that you need."
                wt_image ms1_training_64
                player.c "Maybe you can accept being his submissive and give up the idea of slavery.  But if you need slavery, true slavery, the time will come when he may have to pass you on to someone else."
                wt_image ms1_training_5
                diamond.c "Slaves can love their Masters!"
                player.c "Yes. They can and often do. I'm talking about you, not all slaves."
                wt_image ms1_training_64
                player.c "He's the first man you've loved and the first man you've served. You're fighting a power struggle with him that he can't win, no matter what approach he takes, because everything he does is filtered through your conflicted views of him."
                wt_image ms1_training_6
                diamond.c "Help me then! Teach me whatever lesson I need to learn so I can stop fighting him and serve him properly."
                player.c "I'll do my best."
              add tags 'shared_hard_truth' to diamond # note: tag not used yet but will be when events around Diamond's sale are implemented
              $ diamond.training_submission_level += 1
              if player.has_tag('dominant'):
                sys "She's feeling more chastised."
            "Wait and maybe discuss it with her Master":
              pass
        # Hypno Training
        if diamond.has_tag('hypnotized_now'):
          if diamond.has_tag('hypnotized_bj_now'):
            wt_image ms1_training_69
          else:
            wt_image ms1_training_41
          "You'll never get to a true solution to her acting bratty in one hypnosis session, maybe not even in 10 depending on how irreconcilable her conflicting needs are."
          if diamond.has_tag('hypnotized_bj_now'):
            wt_image ms1_training_71
          else:
            wt_image ms1_training_41 # no change
          "The best you can do is convince her that she received what she came here for: a punishment from you."
          $ title = "How do you want her to feel about her 'punishment'?"
          menu:
            "Feel thoroughly chastised":
              if diamond.has_tag('hypnotized_bj_now'):
                wt_image ms1_training_68
              else:
                wt_image ms1_training_65
              if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                "You convince her that she's been thoroughly chastised at your hands. That's what Master M wanted when he hired you. Who knows? It may even help her overcome her brattiness, at least for a short while."
                $ diamond.training_desire_level = 3
                $ diamond.training_submission_level = 5
              else:
                "You try to convince her that she's been thoroughly chastised at your hands, but it's difficult because you're not that strong a hypnotist, and you're not sure you get the balance between punishment and acceptance quite right. You do your best, though, because that's what Master M wanted when he hired you."
                $ diamond.training_desire_level = 0
                $ diamond.training_submission_level = 3
            "Feel like she enjoyed herself":
              if diamond.has_tag('hypnotized_bj_now'):
                wt_image ms1_training_69
              else:
                wt_image ms1_training_7
              if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                "You convince her that she's been punished in a way she both accepts and enjoys. It's not exactly what Master M asked for when he hired you, but he left it up to you to decide what to do with her, and you think this will be best for her in the long run."
                $ diamond.training_desire_level = 5
                $ diamond.training_submission_level = 3
              else:
                "You try convince her that she's been punished in a way she both accepts and enjoys, but it's difficult because you're not that strong a hypnotist. It's not exactly what Master M asked for when he hired you, but he left it up to you to decide what to do with her, and you think this will be best for her in the long run."
                $ diamond.training_desire_level = 3
                $ diamond.training_submission_level = 0
            "Feel both" if player.test('hypnosis_level', 15):
              if player.has_tag('hypnotist'):
                if diamond.has_tag('hypnotized_bj_now'):
                  wt_image ms1_training_67
                else:
                  wt_image ms1_training_63
                "You convince her that she's been she's been thoroughly chastised at your hands, and yet she still manages to enjoy it. It's not exactly what Master M asked for when he hired you, but he left it up to you to decide what to do with her, and you think this will be best for her in the long run."
                $ diamond.training_desire_level = 5
                $ diamond.training_submission_level = 6
              else:
                if diamond.has_tag('hypnotized_bj_now'):
                  wt_image ms1_training_73
                else:
                  wt_image ms1_training_41
                "You try convince her that she's been thoroughly chastised and yet still enjoys it, but it's difficult because you're not a natural hypnotist. It's not exactly what Master M asked for when he hired you, but he left it up to you to decide what to do with her, and you think this will be best for her in the long run."
                $ diamond.training_desire_level = 2
                $ diamond.training_submission_level = 3
          if diamond.has_tag('hypnotized_bj_now'):
            wt_image ms1_training_71
            "Your work complete, you can relax and focus on enjoying the blow job."
            wt_image ms1_training_72
            "When you're ready, she pulls your dick out of her mouth as let yourself go, spurting your load over the hypnotized woman's upturned face."
            wt_image ms1_training_51
            player.c "[player.orgasm_text]"
            $ diamond.hypno_blowjob_count += 1
            $ diamond.hypno_facial_count += 1
            rem tags 'hypnotized_bj_now' from diamond
            orgasm notify
            $ title = "Tell her to wear the cum on her face home?"
            menu:
              "Yes":
                add tags 'training_show_cum' to diamond
                $ diamond.training_desire_level += 1
                $ diamond.training_submission_level += 1
                player.c "When you get home, show your Master my cum on you, and tell him it's proof that you accepted my punishment and pleased me while doing so."
                wt_image ms1_training_74
                diamond.c "Yes, Sir. Thank you, Sir."
                if player.has_tag('supersexy'):
                  sys "Her arousal has increased."
                if player.has_tag('dominant'):
                  sys "She's feeling more chastised."
              "No, have her clean herself up":
                wt_image ms1_training_66
                "Once she's cleaned up, you leave her with only the memories you want her to have of her time with you, and bring her out of her trance."
                player.c "Time to go home to your Master."
                wt_image ms1_training_7
                diamond.c "Yes, Sir."
                wt_image ms1_training_56
                "She dresses and leaves."
          else:
            wt_image ms1_training_41
            "You leave her with only the memories you want her to have of her time with you, and bring her out of her trance."
            player.c "Time to go home to your Master."
            wt_image ms1_training_7
            diamond.c "Yes, Sir."
            wt_image ms1_training_56
            "She dresses and leaves."
        # Normal Training
        else:
          $ title = "What are you going to do with her?"
          menu:
            "Punish her":
              player.c "So now it falls on me to punish you."
              wt_image ms1_training_60
              diamond.c "Yes, Sir."
              wt_image ms1_training_75
              "She removes her remaining clothes then follows you inside ..."
              call forced_movement(living_room) from _call_forced_movement_397
              summon diamond no_follows
              wt_image ms1_training_76
              "... where she kneels on the sofa, presenting her ass to you."
              wt_image ms1_training_9
              $ title = "She's ready for her punishment"
              menu menu_master_message_punish:
                "Spank her" if not diamond.has_tag('message_spanked'):
                  "*smack*"
                  wt_image ms1_training_76
                  diamond.c "Ouch!"
                  "*smack*"
                  wt_image ms1_training_9
                  diamond.c "Ouch!!"
                  "*smack*"
                  wt_image ms1_training_77
                  diamond.c "Ouch!!!"
                  wt_image ms1_training_10
                  "You begin a rhythmic spanking of her ass, using both hands, and don't stop until her butt is beet red ... *smack* *smack* *smack* *smack* *smack*"
                  diamond.c "ooowwwww"
                  wt_image ms1_training_11
                  "She's moaning and twitching her ass in discomfort, but you can also smell a distinct odor of arousal."
                  if player.has_tag('supersexy'):
                    sys "Her arousal has increased."
                  if player.has_tag('dominant'):
                    sys "She's feeling more chastised."
                  $ diamond.training_desire_level += 1
                  $ diamond.training_submission_level += 1
                  add tags 'message_spanked' to diamond
                  $ title = "What now?"
                  jump menu_master_message_punish
                "Caress her" if not diamond.has_tag('message_carressed'):
                  if diamond.has_tag('message_spanked'):
                    wt_image ms1_training_78
                  else:
                    wt_image ms1_training_13
                  "You slide a finger along her sex and she moistens immediately."
                  diamond.c "oohhhh"
                  if player.has_tag('supersexy'):
                    sys "Her arousal has increased."
                  $ diamond.training_desire_level += 1
                  add tags 'message_carressed' to diamond
                  $ title = "What now?"
                  jump menu_master_message_punish
                "Fuck her" if diamond.has_tag('message_carressed') or diamond.has_tag('message_spanked'):
                  if not diamond.has_tag('message_spanked'):
                    wt_image ms1_training_78
                    "Her pussy looks pretty irresistible, but this was supposed to be a punishment and you haven't even spanked her yet."
                    $ title = "What do you do?"
                    menu:
                      "Just fuck her":
                        add tags 'message_fuck_her' to diamond
                      "Get back to her punishment":
                        wt_image ms1_training_9
                        "You try to get your mind off her pretty pussy and back on why she's here."
                        jump menu_master_message_punish
                  else:
                    wt_image ms1_training_13
                    "Her pussy looks pretty irresistible, and there's no reason to even try and resist it."
                    add tags 'message_fuck_her' to diamond
                  if diamond.has_tag('message_fuck_her'):
                    $ title = "How do you want to fuck her?"
                    menu:
                      "Gently":
                        if not diamond.has_tag('message_spanked'):
                          wt_image ms1_training_96
                        else:
                          wt_image ms1_training_15
                        "She's wet and gasps as you enter her."
                        diamond.c "oohhh"
                        call master_m_message_gently from _call_master_m_message_gently
                      "Roughly":
                        wt_image ms1_training_99
                        "She grimaces and groans as you shove yourself into her."
                        diamond.c "oohhh"
                        call master_m_message_roughly from _call_master_m_message_roughly
                      "In the ass":
                        wt_image ms1_training_81
                        player.c "Head down and ass up.  I presume I don't need to explain which hole this is going in, [diamond.training_name]."
                        wt_image ms1_training_82
                        "You press the head of your cock against her rosebud and slowly push into her.  She gasps as the tip of your cock penetrates her."
                        wt_image ms1_training_83
                        diamond.c "ooh!"
                        wt_image ms1_training_84
                        player.c "You're going to take my entire cock up your ass, [diamond.training_name]."
                        wt_image ms1_training_85
                        diamond.c "Yes, Sir."
                        wt_image ms1_training_86
                        "You shove yourself the rest of the way inside her as she half-screams, half-moans from the sensation."
                        diamond.c "OOHH OOWWWW!!!"
                        wt_image ms1_training_87
                        "Now fully inside her, you can start fucking her properly.  She moves her hips as best she can given the tightness of her hole around your hard shaft, bucking backwards to meet each forward thrust of your own."
                        call master_m_message_ass from _call_master_m_message_ass
                "Take her to the dungeon" if not diamond.has_tag('message_carressed') and not diamond.has_tag('message_spanked'):
                  player.c "Not like that, [diamond.training_name].  Follow me."
                  call forced_movement(dungeon) from _call_forced_movement_398
                  summon diamond no_follows
                  wt_image ms1_training_101
                  "She follows you into the dungeon and allows you to tie her up."
                  wt_image ms1_training_26
                  "She's an experienced submissive, so you put her in suitably challenging and awkward position.  She tries to support her weight on her toes while unable to straighten up."
                  wt_image ms1_training_102
                  "It only takes a few seconds for the muscles in her legs to start aching."
                  diamond.c "Please, Sir!  This is really uncomfortable, Sir!"
                  if player.has_tag('dominant'):
                    sys "She's feeling more chastised."
                  $ diamond.training_submission_level += 1
                  $ title = "What do you do?"
                  menu menu_master_message_dungeon:
                    "Spank her" if not diamond.has_tag('message_spanked'):
                      wt_image ms1_training_33
                      "*smack* ... *smack* ... *smack*"
                      diamond.c "Ouch!  Ohhh .... Ouch!!"
                      if diamond.has_tag('message_suffer'):
                        "Despite her discomfort and the trembling in her legs, you can smell her getting wet."
                      else:
                        "She breaks out in a sweat from the strain of holding this position while you spank her. Despite her discomfort and the trembling in her legs, you can smell her getting wet."
                      if player.has_tag('supersexy'):
                        sys "Her arousal has increased."
                      if player.has_tag('dominant'):
                        sys "She's feeling more chastised."
                      $ diamond.training_desire_level += 1
                      $ diamond.training_submission_level += 1
                      add tags 'message_spanked' to diamond
                      if diamond.has_tag('message_suffer'):
                        wt_image ms1_training_104
                      else:
                        wt_image ms1_training_102
                      $ title = "What now?"
                      jump menu_master_message_dungeon
                    "Let her suffer first" if not diamond.has_tag('message_spanked') and not diamond.has_tag('message_suffer'):
                      wt_image ms1_training_26
                      "You ignore her pleas and watch as her legs tremble."
                      wt_image ms1_training_103
                      "Before long, she breaks out in a sweat from the strain of holding this position"
                      wt_image ms1_training_104
                      diamond.c "Please Sir!! I can't hold myself up like this. I've learned my lesson. I really have! I'll be good. I promise!"
                      "Tears start streaming down her face."
                      if player.has_tag('dominant'):
                        sys "She's feeling more chastised."
                      $ diamond.training_submission_level += 1
                      add tags 'message_suffer' to diamond
                      $ title = "What now?"
                      jump menu_master_message_dungeon
                    "Let her suffer some more" if diamond.has_tag('message_suffer') and not diamond.has_tag('message_suffer_more'):
                      wt_image ms1_training_103
                      "Her pleas turn to wails of desperation."
                      wt_image ms1_training_105
                      diamond.c "PLEAASSSE!!! WHAT DO YOU WANT??? I'LL DO ANYTHING. ANYTHING!!! LET ME DOWN!!! I CAN'T TAKE IT ANYMORE!!!!"
                      if player.has_tag('supersexy'):
                        sys "Her arousal has increased."
                      if player.has_tag('dominant'):
                        sys "She's feeling much more chastised."
                      $ diamond.training_desire_level += 1
                      $ diamond.training_submission_level += 2
                      add tags 'message_suffer_more' to diamond
                      $ title = "What now?"
                      jump menu_master_message_dungeon
                    "Leave her there" if diamond.has_tag('message_suffer_more'):
                      wt_image ms1_training_103
                      "She stops begging and just sobs, tears flowing down her face, her whole body shaking in agony.  You've kept your end of the bargain. The position doesn't cause injury, but it does feels unbearable to her."
                      wt_image ms1_training_106
                      "When you finally release the ropes holding her to the pole, she slumps to the floor in a heap, looking up at you with fear."
                      if player.has_tag('supersexy'):
                        sys "Her arousal has decreased."
                      $ diamond.training_desire_level -= 1
                      $ title = "What do you do with her?"
                      menu:
                        "Jerk off on her":
                          "She's shaking too much to help out, so you pleasure yourself with your own hand as you look at her lying tied and helpless at your feet."
                          wt_image ms1_training_27
                          player.c "Keep your eyes on me, [diamond.training_name]."
                          "If the sight of your hard cock gives her any pleasure, it doesn't show on her face."
                          wt_image ms1_training_28
                          "When you're ready to cum, you grab her by the hair and pull her up to your cock. She closes her eyes and mouth tight as you spurt your load over her."
                          player.c "[player.orgasm_text]"
                          orgasm notify
                          wt_image ms1_training_108
                          diamond.c "May I clean myself up now?"
                          add tags 'cum_from_jerk_off' to diamond
                          call master_m_message_clean from _call_master_m_message_clean
                        "Continue to discipline her":
                          wt_image ms1_training_107
                          "Grabbing her by the throat, you pull her up to her knees and give her something to cry about."
                          wt_image ms1_training_34
                          "*SLAP*"
                          diamond.c "Oowwww!!!!"
                          wt_image ms1_training_30
                          player.c "Have you learned your lesson?"
                          "She hesitates."
                          wt_image ms1_training_34
                          "*SLAP*"
                          diamond.c "Oowwww!!!! YES!! YES, I'll BE GOOD!!! I PROMISE!!!!"
                          wt_image ms1_training_30
                          if player.has_tag('supersexy'):
                            sys "Her arousal has increased."
                          if player.has_tag('dominant'):
                            sys "She's feeling more chastised."
                          $ diamond.training_desire_level += 1
                          $ diamond.training_submission_level += 1
                          player.c "Show me."
                          diamond.c "What do you want me to do, Sir? Anything. Just tell me."
                          $ title = "What do you want her to do?"
                          menu:
                            "Crawl and lick your shoes":
                              wt_image ms1_training_110
                              player.c "Crawl"
                              wt_image ms1_training_111
                              "She drops to all fours and scampers along beside you like an animal."
                              wt_image ms1_training_112
                              "As you lead her around the house, she gets lower and lower, as if to demonstrate her servililty.  Her breathing's also changing, and not necessarily just because of the exercise."
                              $ diamond.training_desire_level += 1
                              if player.has_tag('supersexy'):
                                sys "Her arousal has increased."
                              wt_image ms1_training_113
                              player.c "That's enough.  Show me you know your place by cleaning my shoes, then you can go."
                              wt_image ms1_training_40
                              "Relieved not to be made to do anything more degrading, she licks your shoes clean with her tongue."
                              call forced_movement(living_room) from _call_forced_movement_399
                              if diamond.training_desire_level < 0:
                                "Once she's finished, she scrambles into her clothes and flees as quickly as she can."
                              elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                                "Once she's finished, she gets back into her clothes and leaves, avoiding eye contact with you."
                              elif diamond.training_desire_level < 3:
                                "Once she's finished, she gets back into her clothes and leaves."
                              elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                "Once she's finished, she gets back into her clothes and leaves, head bowed."
                              elif diamond.training_desire_level < 5:
                                "Once she's finished, she gets back into her clothes and leaves, a small smile on her face."
                              elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                "Once she's finished, she gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                              else:
                                "Once she's finished, she gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                              change player energy by -energy_short notify
                            "Suck your cock":
                              wt_image ms1_training_114
                              player.c "Show me how you suck dick, [diamond.training_name]."
                              wt_image ms1_training_115
                              "She starts sucking while working her tongue and her lips."
                              wt_image ms1_training_116
                              "It seems she's used to giving head without the use of her hands.  You let go of her head and let her demonstrate her technique and her devotion, which she does with enthusiasm."
                              if player.has_tag('supersexy'):
                                sys "Her arousal has increased."
                              $ diamond.training_desire_level += 1
                              wt_image ms1_training_35
                              call master_m_message_where_cum from _call_master_m_message_where_cum
                            "Drink your piss":
                              player.c "You're going to drink my piss, [diamond.training_name]."
                              "She hesitates just a second before replying."
                              diamond.c "But ... yes, Sir."
                              wt_image ms1_training_31
                              "She starts crying as she places her open mouth in front of your dick."
                              wt_image ms1_training_120
                              player.c "Why are you crying?"
                              diamond.c "My Master has never done this to me."
                              player.c "Are you afraid?"
                              diamond.c "No, Sir. It's not that. I'm a slave. If my Master wants me to drink his piss, I'll happily do so."
                              wt_image ms1_training_121
                              player.c "But you'd like him to be the first?"
                              diamond.c "Yes, Sir. Please, Sir? I'd like to serve him this way before any other man."
                              $ title = "Let her give this to her Master?"
                              menu:
                                "Send her home to tell him what she wants":
                                  player.c "Go home and tell him what you just told me."
                                  wt_image ms1_training_122
                                  diamond.c "Yes, Sir! Thank you, Sir!!"
                                  if player.has_tag('supersexy'):
                                    sys "Her arousal has increased greatly."
                                  if player.has_tag('dominant'):
                                    sys "She's feeling more chastised."
                                  $ diamond.training_desire_level += 3
                                  $ diamond.training_submission_level += 1
                                  # this makes sure that this action doesn't increase her desire above her submission
                                  if diamond.training_desire_level > diamond.training_submission_level:
                                    $ diamond.training_desire_level = diamond.training_submission_level
                                    $ diamond.training_desire_level -= 1
                                  add tags 'training_ask_for_piss' to diamond
                                  call forced_movement(living_room) from _call_forced_movement_400
                                  wt_image living_room.image
                                  if diamond.training_desire_level < 0:
                                    "She scrambles into her clothes and flees as quickly as she can."
                                  elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                                    "She gets back into her clothes and leaves, avoiding eye contact with you."
                                  elif diamond.training_desire_level < 3:
                                    "She gets back into her clothes and leaves."
                                  elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                    "She gets back into her clothes and leaves, head bowed."
                                  elif diamond.training_desire_level < 5:
                                    "She gets back into her clothes and leaves, a small smile on her face."
                                  elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                    "She gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                                  else:
                                    "She gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                                "Take her piss virginity":
                                  wt_image ms1_training_31
                                  player.c "Too bad.  Today you serve me."
                                  wt_image ms1_training_32
                                  player.c "Drink it all. Don't spill a drop."
                                  wt_image ms1_training_123
                                  "Tears flow down her cheeks as you empty your bladder down her throat ... *pzzzzzzzzzzzzzzzzzzzzzzz*"
                                  if player.has_tag('dominant'):
                                    sys "She's feeling more chastised."
                                  $ diamond.training_submission_level += 1
                                  call forced_movement(living_room) from _call_forced_movement_401
                                  wt_image living_room.image
                                  if diamond.training_desire_level < 0:
                                    "Once she's finished drinking, she scrambles into her clothes and flees as quickly as she can."
                                  elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                                    "Once she's finished drinking, she gets back into her clothes and leaves, avoiding eye contact with you."
                                  elif diamond.training_desire_level < 3:
                                    "Once she's finished drinking, she gets back into her clothes and leaves."
                                  elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                    "Once she's finished drinking, she gets back into her clothes and leaves, head bowed."
                                  elif diamond.training_desire_level < 5:
                                    "Once she's finished drinking, she gets back into her clothes and leaves, a small smile on her face."
                                  elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                                    "Once she's finished drinking, she gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                                  else:
                                    "Once she's finished drinking, she gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                              change player energy by -energy_short notify
                        "Send her home":
                          if diamond.training_name == "Fucktoy" and diamond.training_desire_level > 0:
                            if player.has_tag('supersexy'):
                              "She looks at you, a little confused and a little disappointed. After calling her 'Fucktoy', she wonders what happened to make you not want to use any of her holes?"
                              sys "Her arousal has decreased."
                            else:
                              "She looks at you, a little confused. She's relieved not to have to service you sexually, but after calling her 'Fucktoy' she wonders what happened to make you not want to use any of her holes?"
                            $ diamond.training_desire_level -= 1
                          call forced_movement(living_room) from _call_forced_movement_402
                          wt_image living_room.image
                          if diamond.training_desire_level < 0:
                            "She scrambles into her clothes and flees as quickly as she can."
                          elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                            "She gets back into her clothes and leaves, avoiding eye contact with you."
                          elif diamond.training_desire_level < 3:
                            "She gets back into her clothes and leaves."
                          elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                            "She gets back into her clothes and leaves, head bowed."
                          elif diamond.training_desire_level < 5:
                            "She gets back into her clothes and leaves, a small smile on her face."
                          elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                            "She gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                          else:
                            "She gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                          change player energy by -energy_short notify
                    "Have her blow you" if diamond.has_tag('message_spanked') or diamond.has_tag('message_suffer'):
                      wt_image ms1_training_124
                      "Her legs are shaking as you untie her from the pole and re-tie her on her knees."
                      wt_image ms1_training_125
                      player.c "Show me how you suck dick, [diamond.training_name]."
                      wt_image ms1_training_115
                      "She starts sucking while working her tongue and her lips."
                      wt_image ms1_training_116
                      "It seems she's used to giving head without the use of her hands.  You let go of her head and let her demonstrate her technique and her devotion, which she does with enthusiasm."
                      if player.has_tag('supersexy'):
                        sys "Her arousal has increased."
                      $ diamond.training_desire_level += 1
                      wt_image ms1_training_35
                      call master_m_message_where_cum from _call_master_m_message_where_cum_1
                    "Let her go" if diamond.has_tag('message_spanked') or diamond.has_tag('message_suffer'):
                      player.c "Have you had enough, [diamond.training_name]?"
                      if diamond.has_tag('message_suffer'):
                        wt_image ms1_training_104
                      else:
                        wt_image ms1_training_102
                      diamond.c "Yes, Sir."
                      wt_image ms1_training_101
                      player.c "Go on then, go home to your Master."
                      if diamond.training_name == "Fucktoy" and diamond.training_desire_level > 0:
                        wt_image ms1_training_121
                        if player.has_tag('supersexy'):
                          "She looks at you, a little confused and a little disappointed. After calling her 'Fucktoy', she wonders what happened to make you not want to use any of her holes?"
                          sys "Her arousal has decreased."
                        else:
                          "She looks at you, a little confused. She's relieved not to have to service you sexually, but after calling her 'Fucktoy' she wonders what happened to make you not want to use any of her holes?"
                        $ diamond.training_desire_level -= 1
                      call forced_movement(living_room) from _call_forced_movement_403
                      wt_image living_room.image
                      if diamond.training_desire_level < 0:
                        "She scrambles into her clothes and flees as quickly as she can."
                      elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                        "She gets back into her clothes and leaves, avoiding eye contact with you."
                      elif diamond.training_desire_level < 3:
                        "She gets back into her clothes and leaves."
                      elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                        "She gets back into her clothes and leaves, head bowed."
                      elif diamond.training_desire_level < 5:
                        "She gets back into her clothes and leaves, a small smile on her face."
                      elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                        "She gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                      else:
                        "She gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                      change player energy by -energy_short notify
                "Make it really hurt" if diamond.has_tag('message_spanked') and not diamond.has_tag('message_hurt'):
                  player.c "You like that, do you?"
                  wt_image ms1_training_11
                  diamond.c "No"
                  player.c "Don't lie to me, [diamond.training_name]. I can smell your pussy juices.  Let's see if you like the rest of your punishment as much?"
                  player.c "Let's see if you like the rest of your punishment as much."
                  wt_image ms1_training_12
                  "She screams as you dig your fingers into her ass, squeezing cruelly."
                  diamond.c "OOWWW!!!!"
                  wt_image ms1_training_11
                  player.c "Your Master didn't place any restrictions on my bruising you, did he [diamond.training_name]? I'm allowed to bruise you aren't I?"
                  diamond.c "*snifff*  ... yes"
                  wt_image ms1_training_12
                  "You dig your fingers in deeper."
                  diamond.c "OOOWWWW!!!!"
                  wt_image ms1_training_10
                  "Then you resume spanking her now bruised ass. There's no smell of arousal as you spank her now. ... *smack*"
                  diamond.c "OW!"
                  "*smack*"
                  diamond.c "OWW!!"
                  "*smack*"
                  diamond.c "OOWWW!!!"
                  wt_image ms1_training_11
                  "She's crying softly as you finish the spanking."
                  $ diamond.training_submission_level += 1
                  if player.has_tag('dominant'):
                    sys "She's feeling more chastised."
                  add tags 'message_hurt' to diamond
                  $ title = "What now?"
                  jump menu_master_message_punish
                "Let her go" if diamond.has_tag('message_spanked'):
                  player.c "We're done here."
                  if diamond.has_tag('message_hurt'):
                    wt_image ms1_training_80
                    "She groans in relief, rubbing her sore bum for comfort."
                    diamond.c "ooohhh"
                  else:
                    wt_image ms1_training_79
                    "She rubs her bum, gently, surprised to discover that her punishment is over."
                  player.c "Go home to your Master, [diamond.training_name]."
                  if diamond.training_name == "Fucktoy" and diamond.training_desire_level > 0:
                    wt_image ms1_training_14
                    if player.has_tag('supersexy'):
                      "She looks at you, a little confused and a little disappointed. After calling her 'Fucktoy', she wonders what happened to make you not want to use any of her holes?"
                      sys "Her arousal has decreased."
                    else:
                      "She looks at you, a little confused. She's relieved not to have to service you sexually, but after calling her 'Fucktoy' she wonders what happened to make you not want to use any of her holes?"
                    $ diamond.training_desire_level -= 1
                  wt_image living_room.image
                  if diamond.training_desire_level < 0:
                    "She scrambles into her clothes and flees as quickly as she can."
                  elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                    "She gets back into her clothes and leaves, avoiding eye contact with you."
                  elif diamond.training_desire_level < 3:
                    "She gets back into her clothes and leaves."
                  elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                    "She gets back into her clothes and leaves, head bowed."
                  elif diamond.training_desire_level < 5:
                    "She gets back into her clothes and leaves, a small smile on her face."
                  elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                    "She gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
                  else:
                    "She gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
                  change player energy by -energy_short notify
            "Make love to her":
              player.c "Come here, [diamond.training_name]. I want to make love with you."
              wt_image ms1_training_4
              if diamond.training_desire_level < 0:
                "She hesitates, confused by the change in your behavior."
                diamond.c "I don't understand."
                player.c "Your Master sent you to me to do with you as I see fit. I listened to your story. I've decided that what would be appropriate would be for you to press your soft body against mine while I make love to you."
                wt_image ms1_training_6
                diamond.c "I ... okay."
                $ diamond.training_desire_level += 1
                if player.has_tag('supersexy'):
                  sys "Her arousal has increased."
              else:
                diamond.c "But what about my punishment?"
                player.c "Your Master sent you to me to do with you as I see fit. I listened to your story. I've decided that what would be appropriate would be for you to press your soft body against mine while I make love to you."
                wt_image ms1_training_6
                "She smiles."
                diamond.c "Okay"
              wt_image ms1_training_41
              "Smiling nervously, she slips out of her remaining clothes as you lead her into the house."
              call forced_movement(living_room) from _call_forced_movement_404
              summon diamond no_follows
              wt_image ms1_training_126
              "You move to take her in your arms, but she slips under your embrace and pulls your cock free from your pants."
              wt_image ms1_training_127
              "You watch as she licks you hard ..."
              wt_image ms1_training_42
              "... swirling her tongue over and around your cock as she studies you, looking for confirmation that this is turning you on."
              wt_image ms1_training_128
              "She's a small woman, and you effortlessly pull her up beside you when you've had enough of her teasing."
              wt_image ms1_training_129
              "She pulls back, evading your attempts to kiss her at first."
              wt_image ms1_training_16
              "When she does let you reach her lips, she impales herself on your cock as you kiss her, and tries to wriggle up on top of you."
              $ title = "Let her get on top of you?"
              menu:
                "Yes, let her ride you":
                  wt_image ms1_training_130
                  "She seems to like this position, as it gives her control of the pace and timing of the fuck. She may not get control very often with her Master, as she seems to relish the opportunity with you."
                  if player.has_tag('supersexy'):
                    sys "Her arousal has increased a lot."
                  $ diamond.training_desire_level += 2
                  wt_image ms1_training_43
                  "Faster and faster she rides you, bouncing up and down on your hard cock."
                  if diamond.training_desire_level > 1:
                    wt_image ms1_training_131
                    "She cums just before you do."
                    diamond.c "Oooohhhhh!!!"
                    $ diamond.orgasm_count += 1
                    $ diamond.training_desire_level = 5
                    wt_image ms1_training_130
                  else:
                    wt_image ms1_training_130
                    "She doesn't cum, but you certainly do."
                "No, take control":
                  wt_image ms1_training_17
                  "You pin her in place, making it clear that you're in charge, not her, and begin fucking her properly."
                  $ diamond.training_submission_level += 1
                  if player.has_tag('dominant'):
                    sys "She's feeling more chastised."
                  wt_image ms1_training_97
                  "As her moans intensify, you fuck her faster and faster."
                  diamond.c "oohhh ... ooohhhh"
                  $ diamond.training_desire_level += 1
                  if player.has_tag('supersexy'):
                    sys "Her arousal has increased."
                  if diamond.training_desire_level > 1:
                    wt_image ms1_training_98
                    "She cums just before you do."
                    diamond.c "Oooohhhhh!!!"
                    $ diamond.orgasm_count += 1
                    $ diamond.training_desire_level = 5
                  else:
                    wt_image ms1_training_17
                    "She doesn't cum, but you certainly do."
                    wt_image ms1_training_16
              player.c "[player.orgasm_text]"
              wt_image ms1_training_91
              "When you're finished, she slides down to the floor beside you."
              player.c "I hope you learned your lesson today."
              if diamond.training_desire_level < 0:
                wt_image ms1_training_90
                "She covers herself up as she glares at you."
                diamond.c "I need to go now."
              elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
                wt_image ms1_training_92
                diamond.c "Yes, Sir.  That was fun, but I guess I'd better be going."
              elif diamond.training_desire_level < 3:
                wt_image ms1_training_92
                diamond.c "That was fun, but I guess I'd better be going."
              elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                wt_image ms1_training_92
                diamond.c "Yes, Sir. I know this wasn't what my Master expected, but I appreciated your approach to correcting my behavior. I should be going back to my own Master now, Sir."
              elif diamond.training_desire_level < 5:
                wt_image ms1_training_92
                diamond.c "That was fun, but I guess I'd better be going."
              elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
                wt_image ms1_training_94
                "She blushes."
                diamond.c "Yes, Sir. I know this wasn't what my Master expected, but I enjoyed your approach to correcting my behavior. I should be going back to my own Master now, Sir.  I hope I pleased you, Sir."
              else:
                wt_image ms1_training_93
                "She laughs softly."
                diamond.c "Yes, Sir! You were very hard on me - I mean, in me. Thank you, Sir. I know this wasn't what my Master expected, but I enjoyed your approach to correcting my behavior."
              wt_image living_room.image
              "She dresses and leaves."
              $ diamond.sex_count += 1
              orgasm notify
            "Have her serve you sexually":
              player.c "So now it's up to me to discipline you. I've decided your punishment will be to serve me, sexually."
              wt_image ms1_training_62
              diamond.c "Yes, Sir."
              wt_image ms1_training_41
              "She slips out of her remaining clothes and follows you into the house."
              call forced_movement(living_room) from _call_forced_movement_405
              summon diamond no_follows
              wt_image ms1_training_126
              "Once there, she pulls your cock free from your pants ...."
              wt_image ms1_training_132
              "... and gets you hard."
              wt_image ms1_training_44
              "Then she takes her hand away and looks up at you, seemingly awaiting your instructions.  Perhaps this is how she's been trained."
              $ title = "How do you want her to serve you?"
              menu:
                "With her mouth":
                  wt_image ms1_training_133
                  "Sometimes the simple things in life are best. Like having a woman you just met suck your dick as punishment for disobeying her man, and you getting paid to have her do it.  With a tug on her hair, you let her know to continue."
                  wt_image ms1_training_42
                  diamond.c "Would you like me to use my hands, too?"
                  wt_image ms1_training_132
                  "Why not?  They're soft and she seems to be good with them."
                  wt_image ms1_training_127
                  "She alternates between sucking on and licking your cock, all the time stroking you gently with her hands."
                  wt_image ms1_training_134
                  "This is supposed to be a punishment, so you grab and pull her hair, forcing her off the sofa and onto her knees as she sucks you. She moans softly at the feeling of you taking control."
                  diamond.c "oohhh"
                  if player.has_tag('supersexy'):
                    sys "Her arousal has increased."
                  if player.has_tag('dominant'):
                    sys "She's feeling more chastised."
                  $ diamond.training_desire_level += 1
                  $ diamond.training_submission_level += 1
                  $ title = "How do you want head from her?"
                  menu:
                    "Let her do her thing":
                      wt_image ms1_training_135
                      "She seems to know her way around a cock, so you let her do her thing. As she blows you, you notice her hand sneaking between her legs."
                      $ title = "Let her play with herself?"
                      menu:
                        "Tell her to stop":
                          wt_image ms1_training_45
                          "You grab her by the hair and pull her head back again."
                          wt_image ms1_training_136
                          player.c "Stop that.  This is your punishment, [diamond.training_name].  It's not for your enjoyment."
                          wt_image ms1_training_137
                          "She takes her hand away from her pussy and focuses just on blowing you until you're ready to cum."
                          wt_image ms1_training_138
                        "Let her have her fun":
                          wt_image ms1_training_46
                          "She begins rubbing herself, her eyes rolling back in her head as she pleasures herself while pleasuring you."
                          wt_image ms1_training_139
                          "Suddenly her cheeks blush and her eyes roll back as she cums."
                          diamond.c "ooohhhhh"
                          wt_image ms1_training_138
                          "You're ready to join her."
                          $ diamond.orgasm_count += 1
                          $ diamond.training_desire_level = 5
                    "Face fuck her":
                      wt_image ms1_training_47
                      "Gripping her tightly by the hair, you begin to skull fuck her.  She may not have received this treatment much in the past, as she struggles with her gag reflex."
                      wt_image ms1_training_136
                      player.c "Do not throw up on me, [diamond.training_name]."
                      wt_image ms1_training_140
                      "She controls herself - barely - and you face fuck her until you're ready to cum."
                      if player.has_tag('dominant'):
                        sys "She's feeling more chastised."
                      $ diamond.training_submission_level += 1
                      wt_image ms1_training_47
                  $ diamond.blowjob_count += 1
                  $ title = "Where do you want to cum?"
                  menu:
                    "In her mouth":
                      wt_image ms1_training_141
                      "Holding her firmly by the hair, you thrust your cock deep into the back of her throat and let yourself go.  A low moan escapes from the back of her throat as you flood her mouth with your seed."
                      player.c "[player.orgasm_text]"
                      diamond.c "mmhhhh"
                      if player.has_tag('supersexy'):
                        sys "Her arousal has increased."
                        $ diamond.training_desire_level += 1
                      orgasm notify
                      wt_image ms1_training_139
                      "When you finally remove your cock, she gasps for air ..."
                      diamond.c "oohhh"
                      wt_image ms1_training_138
                      player.c "... then licks your cock clean."
                      $ diamond.swallow_count += 1
                      call master_m_message_sexual_service_ending from _call_master_m_message_sexual_service_ending
                    "On her face":
                      wt_image ms1_training_142
                      player.c "[player.orgasm_text]"
                      orgasm notify
                      wt_image ms1_training_143
                      player.c "You can go home now, [diamond.training_name]."
                      diamond.c "May I clean myself up before I go?"
                      add tags 'cum_from_with_mouth' to diamond
                      call master_m_message_clean from _call_master_m_message_clean_1
                "With her pussy":
                  player.c "I want to see how you fuck a cock, [diamond.training_name]."
                  wt_image ms1_training_9
                  "She turns over onto her knees and presents her ass to you."
                  $ title = "How do you want to fuck her?"
                  menu:
                    "Gently":
                      wt_image ms1_training_96
                      if diamond.training_desire_level > 0:
                        "She's wet as you enter her, and gets wetter as she starts moving her hips back and forth, fucking your cock."
                      else:
                        "She's a little dry as you enter her, but starts to get wet as she moves her hips back and forth, fucking your cock."
                      diamond.c "oohhh"
                      add tags 'from_with_pussy' to diamond
                      call master_m_message_gently from _call_master_m_message_gently_1
                    "Roughly":
                      wt_image ms1_training_99
                      "She grimaces and groans as you shove yourself into her."
                      diamond.c "oohhh"
                      add tags 'from_with_pussy' to diamond
                      call master_m_message_roughly from _call_master_m_message_roughly_1
                "With her ass":
                  player.c "Turn around and bend over, [diamond.training_name]. Your punishment is to serve me with your ass."
                  wt_image ms1_training_81
                  "Trembling slightly, she gets into position."
                  wt_image ms1_training_82
                  "When she feels the head of your cock against her rosebud, she presses backwards, gasping as the tip of your cock penetrates her."
                  wt_image ms1_training_83
                  diamond.c "ooh!"
                  wt_image ms1_training_84
                  player.c "Now fuck me, [diamond.training_name]."
                  wt_image ms1_training_85
                  diamond.c "Yes, Sir."
                  wt_image ms1_training_83
                  "She wriggles her hips back towards you, trying to push more of your cock into her tight ass, but it's slow going."
                  wt_image ms1_training_84
                  player.c "I said pleasure me with your ass.  That means my whole cock, not half my cock."
                  wt_image ms1_training_85
                  diamond.c "Yes, Sir."
                  wt_image ms1_training_86
                  "With a forceful thrust backwards, she half-screams, half-moans, as she impales herself onto you."
                  diamond.c "OOHH OOWWWW!!!"
                  wt_image ms1_training_87
                  "With you now fully inside her, she starts trying to fuck you properly, moving her hips back and forth as best she can given the tightness of her hole around your hard shaft.  It's still not fast enough, so you start thrusting, meeting each backwards buck of her hips with a forward thrust of your own."
                  call master_m_message_ass from _call_master_m_message_ass_1
        # receive Master M's reaction
        if current_location != living_room:
          call forced_movement(living_room) from _call_forced_movement_406
        call character_location_return(diamond) from _call_character_location_return_196
        wt_image living_room.image
        "Before you go to bed, you receive a message from Master M."
        if diamond.training_desire_level < 0:
          # abuse ending
          if diamond.training_submission_level >= 3:
            master_m.c "{i}What exactly did you do to Diamond? I wanted you to discipline her, not abuse her.{/i}"
            $ diamond.training_result = 2
          # dislikes you ending
          else:
            master_m.c "{i}What exactly did you do to Diamond?  She doesn't seem particularly chastised, but she sure dislikes you.{/i}"
            $ diamond.training_result = 1
        elif diamond.training_desire_level < 3:
          # unsuccessful
          if diamond.training_submission_level >= 3:
            master_m.c "{i}Diamond seems chastised by your discipline, but a bit withdrawn. I'm sure you did your best, but her time with you didn't have quite the effect I'd hoped for. She seems a little less happy about her submission to me right now.{/i}"
            $ diamond.training_result = 4
          # did nothing?
          else:
            master_m.c "{i}Did you actually do anything with Diamond? She seems completely indifferent about her time with you.{/i}"
            $ diamond.training_result = 3
        elif diamond.training_desire_level < 5:
          # continuing discipline options
          if diamond.training_submission_level >= 3 and diamond.training_submission_level > diamond.training_desire_level:
            master_m.c "{i}Congratulations on your success with Diamond. She seems suitably chastised and repentant.{/i}"
            if diamond.has_tag('training_show_cum'):
              master_m.c "{i}PS Nice touch on having her show me your dried cum on her skin as proof she had obeyed you.{/i}"
            if diamond.has_tag('training_ask_for_piss'):
              master_m.c "{i}PS I was shocked when she told me you had agreed not to pee in her because she wanted me to take this virginity from her. I'm making plans to make that a memorable evening for both of us.{/i}"
            if player.has_tag('club_access'):
              master_m.c "{i}I understand you're a member of the Club.  I'll look forward to seeing you there.{/i}"
            else:
              master_m.c "{i}I'm a member of an exclusive Club.  I think you'll fit right in.  I'm going to sponsor you for membership.  I'll look forward to seeing you there.{/i}"
              add tags 'club_access' to player
            $ diamond.training_result = 6
          # minor good time, no continuing actions
          else:
            master_m.c "{i}Perhaps I miscommunicated my intention. I expected you to discipline Diamond, not show her a good time.{/i}"
            $ diamond.training_result = 5
        else:
          # full success, continuing discipline + pleasure options
          if diamond.training_submission_level >= 3 and diamond.training_submission_level > diamond.training_desire_level:
            #$ master_m.change_status("prospect")
            master_m.c "{i}Congratulations on your success with Diamond.  She seems suitably chastised and repentant.{/i}"
            if diamond.has_tag('training_show_cum'):
              master_m.c "{i}PS Nice touch on having her show me your dried cum on her skin as proof she had obeyed you.{/i}"
            if diamond.has_tag('training_ask_for_piss'):
              master_m.c "{i}PS I was shocked when she told me you had agreed not to pee in her because she wanted me to take this virginity from her.  I'm making plans to make that a memorable evening for both of us.{/i}"
            if player.has_tag('club_access'):
              master_m.c "{i}I understand you're a member of the Club.  I'll look forward to seeing you there.{/i}"
            else:
              master_m.c "{i}I'm a member of an exclusive Club.  I think you'll fit right in.  I'm going to sponsor you for membership.  I'll look forward to seeing you there.{/i}"
              add tags 'club_access' to player
            $ diamond.training_result = 8
          # continuing pleasure options
          else:
            master_m.c "{i}Perhaps I miscommunicated my intention. I expected you to discipline Diamond, not show her a good time.{/i}"
            $ diamond.training_result = 7
        add tags 'no_hypnosis' to diamond
        rem tags 'hypnotized_now' 'message_carressed' 'message_hurt' 'message_spanked' 'message_suffer' 'message_suffer_more'  from diamond
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        $ player.extra_clients_fee_this_week += 25
        $ diamond.name = "Diamond"
        $ master_m.encounter_possible = 1
        add tags 'can_be_in_club' to master_m
        add tags 'can_be_in_club' to diamond
        $ master_m.current_message = 1
        if diamond.training_submission_level >2 and diamond.training_submission_level > diamond.training_desire_level:
          $ master_m.change_status("prospect")
        else:
          $ master_m.change_status("minor_character")
        rem action
        end_day
      "Not Yet":
        "You have until the end of week [master_m.accept_limit] to accept this engagement."
        $ master_m.current_client_action.name = "Reply to Master M"
        if not master_m.wait_on_message:
          $ master_m.wait_on_message = True
          $ master_m.message_note = add_note((master_m.wait_for_message_period + 1) * 5, "{} offer ends".format(master_m.name))
      "Never (Deletes Message)":
        $ master_m.change_status("rejected")
  return

label master_m_diamond_aborted_training:
    $ master_m.change_status("rejected")
    return

label master_m_message_fairyn_ending:
    if fairyn.initial_outcome > 1:
        add tags 'can_be_in_club' to fairyn # this activates potential for her to be at the Club when you visit
        wt_image phone_1
        "Later that day you receive a message from M."
        master_m.c "{i}Fairyn tells me she had fun.  I trust you did, too.{/i}"
        if fairyn.paying_you == 1:
            master_m.c "{i}Oh, and she wanted me to tell you that your check is in the mail.{/i}"
            $ fairyn.paying_you = 2
            # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
            $ player.extra_clients_fee_this_week += 50
        if fairyn.has_tag('know_name'):
            "You expect this wasn't the last you've seen of Fairyn the Trust Fund Baby"
        else:
            "Fairyn. What an unusual name. I wonder what prompted someone to call her that?  Fond memories of another Fairyn, perhaps?"
            add tags 'know_name' to fairyn
            $ fairyn.change_full_name("", "Fairyn", "the Trust Fund Baby")
        if fairyn.paying_you == 0 and player.has_tag('dominant') and fairyn.temporary_count > 5:
            wt_image gift_box_1
            "A little while later, you get a message from Fairyn as well, in the form of a package delivered to your door."
            wt_image handcuffs_julia_1
            "Inside are a pair of bejeweled handcuffs and a note."
            fairyn.c "{i}M tells me you usually charge women to spend time with you, so I'm flattered you let me have a freebie, *wink*.{i}"
            fairyn.c "{i}I bought these handcuffs in Paris a couple of weeks ago.  They were insanely expensive, so of course I had to use Daddy's money to buy them!{i}"
            fairyn.c "{i}Hopefully you can find the right woman to use them on. ~ F{/i}"
            "Now who do you know who would care what the handcuffs you put on her look like?"
            add 1 handcuffs_julia to player
    if fairyn.initial_outcome > 0:
        rem tags 'message_bark_follow' 'message_bark_sex' 'message_dom_6' from fairyn
        end_day
    else:
        rem tags 'message_send_away' from fairyn
        call character_location_return(fairyn) from _call_character_location_return_197
        wt_image current_location.image
    add tags 'no_hypnosis' to fairyn
    $ fairyn.temporary_count = 0
    return

label master_m_message_fairyn_choice:
    $ title = "How do you send her home?"
    menu:
        "Have her leave believing she got what she wanted" if fairyn.initial_arousal > 1:
            call master_m_message_fairyn_believe from _call_master_m_message_fairyn_believe_2
        "Have her leave forgetting what you did together":
            call master_m_message_fairyn_forget from _call_master_m_message_fairyn_forget_2
    jump master_m_message_fairyn_ending
    return

label master_m_message_fairyn_believe:
  wt_image ms2_visit_1_1
  "She's a little dazed as she leaves, but she's feeling good.  She can't quite remember exactly what it is you did with her, but you convince her she got what she was hoping for out of her visit."
  $ fairyn.initial_outcome = 2
  return

label master_m_message_fairyn_forget:
  if fairyn.initial_arousal > 1:
    sys "Are you sure?  You could probably convince her she had a good time, if you want to leave her with that impression."
    $ title = "What do you want?"
    menu:
      "Have her leave believing she got what she wanted" if fairyn.initial_arousal > 1:
        call master_m_message_fairyn_believe from _call_master_m_message_fairyn_believe
      "Just get rid of her":
        $ fairyn.initial_outcome = 1
  else:
    $ fairyn.initial_outcome = 1
  return

label master_m_message_fairyn_mouth:
  # gagged content
  if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
    # still gagged
    if fairyn.temporary_count == 6:
      wt_image ms2_visit_1_57
      "You rub your cock along her face and nose as you unbuckle her gag."
      wt_image ms2_visit_1_59
      "As you pull the gag out of her mouth, she eagerly replaces it with your cock."
      # changing this variable flags that her gag has been removed from her mouth
      $ fairyn.temporary_count = 10
    # used paddle
    elif fairyn.temporary_count == 8:
      wt_image ms2_visit_1_58
      "Placing the paddle under her chin, you tilt her head up towards you.  She gets the hint, and opens her mouth to accept your cock."
    else:
      wt_image ms2_visit_1_59
      "You present your cock to her, and she eagerly opens her mouth to accept it."
    wt_image ms2_visit_1_25
  # non-gagged
  else:
    wt_image ms2_visit_1_41
    "You present your cock to her, and she opens her mouth to receive it."
    wt_image ms2_visit_1_26
  "She groans, seemingly in satisfaction, as you thrust back and forth between her soft lips."
  fairyn.c "mmmmmm"
  $ title = "What now?"
  menu:
    "Fuck her pussy":
      wt_image ms2_visit_1_60
      "When you pull your cock out of her mouth she grins up at you, waiting to find out what you do with her next."
      call master_m_message_fairyn_pussy from _call_master_m_message_fairyn_pussy_4
    "Fuck her ass":
      wt_image ms2_visit_1_60
      "When you pull your cock out of her mouth she grins up at you, waiting to find out what you do with her next."
      call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass_4
    "Cum in her mouth":
      wt_image ms2_visit_1_41
      "She holds her head as still as she can while you skull fuck her, faster and faster ..."
      wt_image ms2_visit_1_42
      "... before flooding her mouth with your cum"
      player.c "[player.orgasm_text]"
      fairyn.c "oohhhhh"
      wt_image ms2_visit_1_27
      "She gulps down your sperm as you empty it down her throat.  Even as you pull your dick out of her mouth, she follows it with her tongue, lapping up the last of your jizz trailing from your cock head."
      wt_image ms2_visit_1_60
      player.c "You can go now."
      "Smiling in satisfaction, she gets her stuff together and heads home."
      $ fairyn.initial_outcome = 5
      $ fairyn.blowjob_count += 1
      $ fairyn.swallow_count += 1
      orgasm notify
    "Cum on her face":
      wt_image ms2_visit_1_41
      "She holds her head as still as she can while you skull fuck her, faster and faster ..."
      wt_image ms2_visit_1_14
      "... before pulling out and emptying your load on her face."
      player.c "[player.orgasm_text]"
      fairyn.c "oohhhhh"
      wt_image ms2_visit_1_15
      "When your balls finally stop spurting jizz onto her, she gently licks the head of your cock."
      wt_image ms2_visit_1_47
      player.c "You can go now."
      "Smiling in satisfaction, she gets her stuff together and heads home."
      $ fairyn.initial_outcome = 5
      $ fairyn.blowjob_count += 1
      $ fairyn.facial_count += 1
      orgasm notify
  return

label master_m_message_fairyn_pussy:
  wt_image ms2_visit_1_28
  # still gagged
  if fairyn.temporary_count == 6:
    wt_image ms2_visit_1_57
    "You rub your cock along her face and nose as you unbuckle her gag."
    player.c "I want to hear you moan as as I fuck you, bitch."
    wt_image ms2_visit_1_49
    "She complies, emitting a deep, guttural sound as you you lift her up onto the counter and penetrate her ..."
    # changing this variable flags that her gag has been removed from her mouth
    $ fairyn.temporary_count = 10
  # not paddled first
  elif fairyn.temporary_count == 9:
    wt_image ms2_visit_1_61
    player.c "You're wet, whore, and I haven't even shoved my dick in you, yet."
    fairyn.c "ooooo ... yes, please!  Fuck me hard!!"
    wt_image ms2_visit_1_49
    "Grabbing her by the head, you lift her up onto the counter.  She emits a deep, guttural sound as you penetrate her ..."
  else:
    wt_image ms2_visit_1_49
    "Grabbing her by the head, you lift her up onto the counter.  She emits a deep, guttural sound as you penetrate her ..."
  fairyn.c "oooooo"
  wt_image ms2_visit_1_28
  "... then moans louder still as you fuck her."
  fairyn.c "oooooooo"
  wt_image ms2_visit_1_29
  $ title = "What now?"
  menu:
    "Fuck her ass":
      wt_image ms2_visit_1_46
      "As you pull out, she reaches down, trying to entice you back inside her."
      player.c "No, slut.  I'm tired of that hole.  Maybe your next one will be tighter."
      call master_m_message_fairyn_ass from _call_master_m_message_fairyn_ass_5
    "Cum in her pussy":
      wt_image ms2_visit_1_28
      "Her moans get louder as you continue to fuck her."
      fairyn.c "ooooooo!!"
      wt_image ms2_visit_1_29
      $ title = "Wait for her to cum?"
      menu:
        "Yes, wait":
          wt_image ms2_visit_1_28
          "It only takes a few more thrusts for her to climax.  The feeling of her body spasming under you quickly puts you over the edge, too."
          fairyn.c "OOHHHH!!!"
          # previously gagged
          if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
            wt_image ms2_visit_1_62
          else:
            wt_image ms2_visit_1_29
          player.c "[player.orgasm_text]"
          $ fairyn.orgasm_count += 1
        "No, cum before she can":
          wt_image ms2_visit_1_28
          "Quickening your pace, you let yourself go before she can climax."
          # previously gagged
          if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
            wt_image ms2_visit_1_62
          else:
            wt_image ms2_visit_1_29
          player.c "[player.orgasm_text]"
          "She lets out another guttural cry, one borne of frustration mixed with intense satisfaction as she feels your sperm spurting inside her."
          fairyn.c "aaaaaaaa!!!"
      wt_image ms2_visit_1_3
      "When you pull out, she touches herself, running her fingers through your semen as it drips out of her."
      player.c "You can go now."
      wt_image ms2_visit_1_9
      "Smiling, she gets her stuff together and heads home."
      $ fairyn.initial_outcome = 5
      $ fairyn.sex_count += 1
      orgasm notify
    "Cum on her face":
      # previously gagged
      if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
        wt_image ms2_visit_1_60
      else:
        wt_image ms2_visit_1_9
      "Pulling out, you position her face in front of you and empty your load."
      wt_image ms2_visit_1_14
      player.c "[player.orgasm_text]"
      wt_image ms2_visit_1_15
      "When your balls finally stop spurting jizz onto her, she gently licks the head of your cock."
      wt_image ms2_visit_1_47
      player.c "You can go now."
      "Smiling in satisfaction, she gets her stuff together and heads home."
      $ fairyn.initial_outcome = 5
      $ fairyn.sex_count += 1
      $ fairyn.facial_count += 1
      orgasm notify
  return

label master_m_message_fairyn_ass:
  # gagged content
  if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
    # still gagged
    if fairyn.temporary_count == 6:
      wt_image ms2_visit_1_57
      "You rub your cock along her face and nose as you unbuckle her gag."
      player.c "I want to hear you scream as I ream your ass, bitch."
      wt_image ms2_visit_1_30
      "She complies, emitting a high pitched squeal as you penetrate her."
      fairyn.c "aaaiiiiiii"
      # changing this variable flags that her gag has been removed from her mouth
      $ fairyn.temporary_count = 10
    else:
      wt_image ms2_visit_1_44
      "Consciouly or otherwise, she makes her pussy an obvious target as you pull her ass towards you, but you ignore it and focus on her tight rosebud instead."
      wt_image ms2_visit_1_30
      "A high pitched squeal escapes her throat as you penetrate her."
    fairyn.c "aaaiiiiiii"
    wt_image ms2_visit_1_32
  # non-gagged
  else:
    wt_image ms2_visit_1_44
    "Consciouly or otherwise, she makes her pussy an obvious target as you pull her ass towards you, but you ignore it and focus on her tight rosebud instead."
    wt_image ms2_visit_1_31
    "A high pitched squeal escapes her throat as you penetrate her."
    fairyn.c "aaaiiiiiii"
    wt_image ms2_visit_1_33
  $ title = "What now?"
  menu:
    "Cum in her ass":
      # previously gagged
      if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
        wt_image ms2_visit_1_30
        "As you fuck her behind, her squeals turn to moans, and you realize she's enjoying this."
        wt_image ms2_visit_1_32
        fairyn.c "ooooooo!!"
      else:
        wt_image ms2_visit_1_50
        "As you fuck her behind, her squeals turn to moans, and you realize she's enjoying this."
        wt_image ms2_visit_1_33
        fairyn.c "ooooooo!!"
      $ title = "Wait for her to cum?"
      menu:
        "Yes, wait":
          if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
            wt_image ms2_visit_1_30
            "Her moans grow louder and louder.  You hold your own climax back, and are rewarded with the sound and feeling of hers as she cums with your dick up her ass."
            wt_image ms2_visit_1_32
            fairyn.c "ooooooo  ....  ooooooo!!!  ...  OOHHHH!!!"
          else:
            wt_image ms2_visit_1_31
            "Her moans grow louder and louder.  You hold your own climax back, and are rewarded with the sound and feeling of hers as she cums with your dick up her ass."
            wt_image ms2_visit_1_33
            fairyn.c "ooooooo  ....  ooooooo!!!  ...  OOHHHH!!!"
          "Now it's your turn."
          $ fairyn.orgasm_count += 1
        "No, cum before she can":
          pass
      wt_image ms2_visit_1_34
      "Flipping her onto her face, you position yourself above her and pile drive into her.  The fucking you give her is fast and it's hard and it hurts, but she moans through the pain, and the combination of the sensation of her tight ass and the sights and sounds of her enjoying you assfuck her takes you over the edge."
      fairyn.c "ooooooo"
      wt_image ms2_visit_1_50
      player.c "[player.orgasm_text]"
      wt_image ms2_visit_1_35
      "When your balls have finished pumping your sperm into her bowels, you pull out.  Your cock exits her distended ass with a small 'pop' sound ..."
      wt_image ms2_visit_1_51
      "... followed by a flow of cum."
      player.c "You can go now."
      wt_image ms2_visit_1_21
      "It takes a few minutes for her legs to have enough strength to carry her.  When they do, she gets her stuff together and heads home, a smile of satisfaction on her face as she rubs her abused ass."
      orgasm notify
    "Cum on her face":
      # previously gagged
      if fairyn.temporary_count == 6 or fairyn.temporary_count == 8 or fairyn.temporary_count == 10:
        wt_image ms2_visit_1_30
        "You fuck her ass until you feel your balls begin to boil ..."
        wt_image ms2_visit_1_60
      else:
        wt_image ms2_visit_1_50
        "You fuck her ass until you feel your balls begin to boil ..."
        wt_image ms2_visit_1_9
      "... then you pull out, and position her face in front of you and empty your load."
      wt_image ms2_visit_1_14
      player.c "[player.orgasm_text]"
      wt_image ms2_visit_1_15
      "When your balls finally stop spurting jizz onto her, she gently licks the head of your cock."
      player.c "My cock was just up your ass.  You're not going to get it clean with tentative licks."
      wt_image ms2_visit_1_64
      fairyn.c "ooooooo"
      "She moans as she takes your cock into her mouth, cleaning it thoroughly before she gathers her stuff together and heads home."
      $ fairyn.facial_count += 1
      orgasm notify
  $ fairyn.initial_outcome = 5
  $ fairyn.anal_count += 1
  return

label master_m_message_gently:
  wt_image ms1_training_17
  "You roll her over and gently stroke in and out of her pussy ..."
  wt_image ms1_training_16
  "... then pull her close and and kiss her.  She's surprised at first, but eventually warms to your kiss."
  wt_image ms1_training_97
  "As her moans intensify, you fuck her faster and faster."
  diamond.c "oohhh ... ooohhhh"
  $ diamond.training_desire_level += 1
  if player.has_tag('supersexy'):
    sys "Her arousal has increased."
  if diamond.training_desire_level > 1:
    wt_image ms1_training_98
    "She cums just before you do."
    diamond.c "Oooohhhhh!!!"
    $ diamond.orgasm_count += 1
    $ diamond.training_desire_level = 5
  else:
    wt_image ms1_training_17
    "She doesn't cum, but you certainly do."
    wt_image ms1_training_16
  player.c "[player.orgasm_text]"
  if diamond.has_tag('from_with_pussy'):
    call master_m_message_sexual_service_ending from _call_master_m_message_sexual_service_ending_1
  else:
    call master_m_message_floor_ending from _call_master_m_message_floor_ending
  $ diamond.sex_count += 1
  orgasm notify
  rem tags 'from_with_pussy' from diamond
  return

label master_m_message_roughly:
  wt_image ms1_training_100
  "Grabbing her by the hair, you start pounding into her faster and faster.  She's a small woman, and with each hard thrust it almost feels as if you're going to break her."
  wt_image ms1_training_19
  "You know it has to hurt, the grip you have on her hair by itself must be excruciating, but her body still responds to the fucking and you can feel her getting wetter as she groans helplessly."
  diamond.c "oohhh ... ooohhhh"
  if player.has_tag('supersexy'):
    sys "Her arousal has increased."
  if player.has_tag('dominant'):
    sys "She's feeling more chastised."
  $ diamond.training_desire_level += 1
  $ diamond.training_submission_level += 1
  if diamond.training_desire_level > 1:
    wt_image ms1_training_20
    "She cums just before you do."
    diamond.c "Oooohhhhh!!!"
    $ diamond.orgasm_count += 1
    $ diamond.training_desire_level = 5
  else:
    wt_image ms1_training_100
    "She doesn't cum, but you certainly do."
    wt_image ms1_training_19
  player.c "[player.orgasm_text]"
  if diamond.has_tag('from_with_pussy'):
    call master_m_message_sexual_service_ending from _call_master_m_message_sexual_service_ending_2
  else:
    call master_m_message_floor_ending from _call_master_m_message_floor_ending_1
  $ diamond.sex_count += 1
  orgasm notify
  rem tags 'from_with_pussy' from diamond
  return

label master_m_message_ass:
  wt_image ms1_training_88
  "You can tell it's hurting her, but you can also smell her getting turned on by being used in this way.  The discomfort is too much for her to cum, but you're soon ready to."
  if player.has_tag('supersexy'):
    sys "Her arousal has increased."
  if player.has_tag('dominant'):
    sys "She's feeling more chastised."
  $ diamond.training_desire_level += 1
  $ diamond.training_submission_level += 1
  $ title = "Where do you want to cum?"
  menu:
    "In her ass":
      wt_image ms1_training_86
      "She groans as you thrust forward, filling her boweals with your hot seed."
      diamond.c "oohhh"
      player.c "[player.orgasm_text]"
    "In her mouth":
      wt_image ms1_training_44
      "You take your dick out of her ass and grab her by the hair. Roughly you pull her mouth onto your cock."
      wt_image ms1_training_89
      "She wrinkles her nose at the taste of her ass on your cock, then lets out a low moan as she feels your cum fill her mouth."
      diamond.c "mmmhh"
      player.c "[player.orgasm_text]"
      if player.has_tag('supersexy'):
        sys "Her arousal has increased."
      if player.has_tag('dominant'):
        sys "She's feeling much more chastised."
      $ diamond.swallow_count += 1
      $ diamond.training_desire_level += 1
      $ diamond.training_submission_level += 2
  call master_m_message_floor_ending from _call_master_m_message_floor_ending_2
  $ diamond.anal_count += 1
  orgasm notify
  return

label master_m_message_floor_ending:
  if diamond.training_desire_level < 0 and diamond.training_submission_level < 3:
    wt_image ms1_training_90
    "She slides down to the floor and covers herself up as she glares at you."
    diamond.c "I need to go now."
  elif diamond.training_desire_level < 0:
    wt_image ms1_training_91
    "She slides down to the floor, rubbing her sore ass as she glares up at you."
    diamond.c "I need to go now."
  elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
    wt_image ms1_training_91
    "She slides down to the floor, rubbing her sore ass."
    diamond.c "I should be going now."
  elif diamond.training_desire_level < 3:
    wt_image ms1_training_92
    "She slides down to the floor, looking up at you."
    diamond.c "I guess I should be going now."
  elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
    wt_image ms1_training_25
    "She slides down to the floor, head bowed, rubbing her sore ass."
    diamond.c "I should be going back to my own Master now, Sir."
  elif diamond.training_desire_level < 5:
    wt_image ms1_training_93
    "She slides down to the floor, a mischievous grin on her face."
    diamond.c "That was fun, but I guess I'd better be going."
  elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
    wt_image ms1_training_94
    "She slides down to the floor, gazing up at you."
    wt_image ms1_training_25
    "Then she blushes, and looks away, rubbing her sore ass as she avoids eye contact."
    diamond.c "I should be going back to my own Master now, Sir.    I hope I pleased you, Sir."
  else:
    wt_image ms1_training_95
    "She slides down to the floor, a lustful look on her face."
    diamond.c "Thank you for that, Sir.  I guess I should probably be getting back to my Master, now."
  wt_image living_room.image
  "She dresses and leaves."
  return

label master_m_message_sexual_service_ending:
  if diamond.training_desire_level < 0:
    wt_image ms1_training_90
    "She slides down to the floor and covers herself up as she glares at you."
    diamond.c "I need to go now."
  elif diamond.training_desire_level < 3:
    wt_image ms1_training_92
    "She slides down to the floor, looking up at you."
    diamond.c "I guess I should be going now."
  elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
    wt_image ms1_training_25
    "She slides down to the floor, head bowed."
    diamond.c "I should be going back to my own Master now, Sir."
  elif diamond.training_desire_level < 5:
    wt_image ms1_training_93
    "She slides down to the floor, a mischievous grin on her face."
    diamond.c "That was fun, but I guess I'd better be going."
  elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
    wt_image ms1_training_94
    "She slides down to the floor, gazing up at you."
    diamond.c "I should be going back to my own Master now, Sir.  I hope I pleased you, Sir."
  else:
    wt_image ms1_training_95
    "She slides down to the floor, a lustful look on her face."
    diamond.c "Thank you for that, Sir.  I guess I should probably be getting back to my Master, now."
  wt_image living_room.image
  "She dresses and leaves."
  return

label master_m_message_where_cum:
  $ title = "Where do you want to cum?"
  menu:
    "In her mouth":
      wt_image ms1_training_115
      "You hold her head still as you let go.  A low moan escapes from the back of her throat as you fill her mouth with your seed."
      player.c "[player.orgasm_text]"
      diamond.c "mmhhhh"
      if player.has_tag('supersexy'):
        sys "Her arousal has increased."
      $ diamond.training_desire_level += 1
      wt_image ms1_training_35
      if diamond.training_desire_level < 0:
        "Once she's finished swallowing, she scrambles into her clothes and flees as quickly as she can."
      elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
        "Once she's finished swallowing, she gets back into her clothes and leaves, avoiding eye contact with you."
      elif diamond.training_desire_level < 3:
        "Once she's finished swallowing, she gets back into her clothes and leaves."
      elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Once she's finished swallowing, she gets back into her clothes and leaves, head bowed."
      elif diamond.training_desire_level < 5:
        "Once she's finished swallowing, she gets back into her clothes and leaves, a small smile on her face."
      elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Once she's finished swallowing, she gets back into her clothes and leaves, head bowed with a contented smile playing across her face."
      else:
        "Once she's finished swallowing, she gets back into her clothes and leaves, trying, not entirely successfully, to keep a big, mischievous grin off her face as she goes."
      call forced_movement(living_room) from _call_forced_movement_407
      $ diamond.swallow_count += 1
      orgasm notify
    "On her face":
      wt_image ms1_training_117
      "Pulling her head off your cock, you empty your load onto her face."
      wt_image ms1_training_37
      player.c "[player.orgasm_text]"
      orgasm notify
      wt_image ms1_training_38
      diamond.c "May I clean myself up before I go?"
      add tags 'cum_from_where_cum' to diamond
      call master_m_message_clean from _call_master_m_message_clean_2
  $ diamond.blowjob_count += 1
  return

label master_m_message_clean:
  $ title = "Let her clean your cum off?"
  menu:
    "No, it suits you":
      if diamond.has_tag('cum_from_jerk_off'):
        wt_image ms1_training_109
      elif diamond.has_tag('cum_from_where_cum'):
        wt_image ms1_training_118
      elif diamond.has_tag('cum_from_with_mouth'):
        wt_image ms1_training_144
      player.c "No, I think it suits someone of your station. Wear it until you return to your Master. He can decide what to do with you after that."
      if player.has_tag('dominant'):
        sys "She's feeling more chastised."
      $ diamond.training_submission_level += 1
      call forced_movement(living_room) from _call_forced_movement_408
      wt_image living_room.image
      if diamond.training_desire_level < 0:
        "She scrambles into her clothes and flees as quickly as she can, your cum still glistening on her face."
      elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
        "She avoids eye contact with you as she gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 3:
        "She gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 5:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she dresses and leaves, a small smile playing across her cum-smeared face."
      elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets back into her clothes and leaves, a contented smile playing across her cum-smeared face."
      else:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she dresses and leaves, a big smile playing across her cum-smeared face."
    "No, I want your Master to see":
      player.c "No, I want your Master to see it. When you get home, show him my cum on you, and tell him it's proof that you accepted my punishment and pleased me while doing so."
      if diamond.has_tag('cum_from_jerk_off'):
        wt_image ms1_training_29
      elif diamond.has_tag('cum_from_where_cum'):
        wt_image ms1_training_119
      elif diamond.has_tag('cum_from_with_mouth'):
        wt_image ms1_training_145
      "Her demeanor softens."
      diamond.c "Yes, Sir. Thank you, Sir."
      if player.has_tag('supersexy'):
        sys "Her arousal has increased."
      if player.has_tag('dominant'):
        sys "She's feeling more chastised."
      add tags 'training_show_cum' to diamond
      $ diamond.training_desire_level += 1
      $ diamond.training_submission_level += 1
      call forced_movement(living_room) from _call_forced_movement_409
      wt_image living_room.image
      if diamond.training_desire_level < 0:
        "She scrambles into her clothes and flees as quickly as she can, your cum still glistening on her face."
      elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
        "She avoids eye contact with you as she gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 3:
        "She gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets back into her clothes and leaves, your cum still glistening on her face."
      elif diamond.training_desire_level < 5:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she dresses and leaves, a small smile playing across her cum-smeared face."
      elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets back into her clothes and leaves, a contented smile playing across her cum-smeared face."
      else:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she dresses and leaves, a big smile playing across her cum-smeared face."
    "Go ahead":
      call forced_movement(living_room) from _call_forced_movement_410
      wt_image living_room.image
      if diamond.training_desire_level < 0:
        "She scrambles into her clothes and flees as quickly as she can, barely stopping to wipe your cum off her face before she goes."
      elif diamond.training_desire_level < 3 and diamond.training_submission_level > 2:
        "She cleans herself up and heads home, avoiding eye contact with you."
      elif diamond.training_desire_level < 3:
        "She cleans herself up and heads home."
      elif diamond.training_desire_level < 5 and diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets herself cleaned up and leaves."
      elif diamond.training_desire_level < 5:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she cleans up and leaves, a small smile playing across her face."
      elif diamond.training_submission_level > 2 and diamond.training_submission_level > diamond.training_desire_level:
        "Head bowed, she gets herself cleaned up and leaves, a contented smile playing across her face."
      else:
        "She tries, not entirely successfully, to keep a mischievous grin off her face as she cleans herself up and leaves, a big smile playing across her face."
  $ diamond.facial_count += 1
  rem tags 'cum_from_jerk_off' 'cum_from_with_mouth' 'cum_from_where_cum' from diamond
  return

label fairyn_message:
  fairyn.c "{i}Okay. You win!{/i}"
  fairyn.c "{i}I can't get it out of my head that you have the gall to charge me to learn how to suck your dick 'properly'.{/i}"
  fairyn.c "{i}Let me know when I can drop by and pay you 50 for my lesson.  ~ F{/i}"
  $ title = "Accept the engagement?"
  menu:
    "Yes (Ends Day)":
      rem tags 'no_hypnosis' from fairyn
      $ fairyn.change_status("minor_character")
      $ living_room.remove_action(fairyn.action_show_message)
      summon fairyn no_follows
      wt_image ms2_training_1_52
      "It seems Fairyn's schedule is as flexible as ever, as she shows up shortly after you contact her."
      fairyn.c "So, here I am!  Ready for my cock sucking lesson."
      wt_image ms2_training_1_4
      fairyn.c "Out of curiosity, is this course recognized by the local university?  In case I ever decide to go back and finish my degree, will I be able to count this as a credit?"
      player.c "I'll make you up a certificate and you can ask the admissions officer."
      wt_image ms2_training_1_53
      "She giggles."
      fairyn.c "I will, you know!"
      wt_image ms2_training_1_1
      fairyn.c "Okay, how do we do this?"
      sys "How you choose to train her has no impact, as this training doesn't lead anywhere (at least not yet). So choose whatever approach you're most interested in."
      if player.can_hypno(fairyn):
        "Similarly, hypnotizing her doesn't (yet) lead to an opportunity to implant a trigger."
      $ title = "How do you want to do this?"
      menu:
        "Find out what she's interested in":
          wt_image ms2_training_1_54
          player.c "Have a seat and let's talk. What are you hoping to get out of today?"
          fairyn.c "Other than the experience of paying a man so he can tell me how to suck him off?  Gee, I hadn't really thought about it."
          wt_image ms2_training_1_3
          fairyn.c "You're the one who claims I'm not very good at giving head.  What do you think I should be getting out of this?"
          player.c "Improved oral skills, obviously. But how do you want to impress a man with those skills?"
          wt_image ms2_training_1_2
          fairyn.c "Are you asking me what type of cock sucker do I want to be?  You are such a charmer!!"
          wt_image ms2_training_1_3
          fairyn.c "I'm not really sure.  What are the options?"
          player.c "It's like anything else in life, Fairyn.  It's all about what type of impression you want to leave. I think you're pretty tuned into that. You know how to dress and act to get people to react to you the way you want them to react."
          player.c "This is no different.  When you finish blowing a guy, what do you want him to be thinking?"
          player.c "That you'd make a great girlfriend?  That you could give a porn star a run for her money?  That regardless of how you portray yourself the rest of the time, you're a submissive creature for him to enjoy once his cock is out?"
          wt_image ms2_training_1_55
          fairyn.c "Definitely not girlfriend material!  I'm the last woman any guy should think about dating."
          wt_image ms2_training_1_3
          fairyn.c "Not a submissive creature, either.  When I have one of my 'moods', I'll let a guy bang my mouth however he wants, but I just want to kneel there and take it when that's going on, not be the one doing the work."
          wt_image ms2_training_1_2
          fairyn.c "Now, porn star, though.  That sounds good!  I want to be the woman he can't stop thinking about, because I blew him better than any whore he's ever paid for.  Let's do that.  Teach me to suck cock like a porn star."
          wt_image ms2_training_1_19
          player.c "You're going to need to be naked for that."
          wt_image ms2_training_1_20
          fairyn.c "Okay"
          call fairyn_contact_pornstar from _call_fairyn_contact_pornstar
        "Tell her to strip":
          player.c "First, you take your clothes off."
          wt_image ms2_training_1_55
          fairyn.c "Straight to business, huh?  I guess the girls who want to be wined and dined before you stick your dick in their mouth have to pay extra?"
          player.c "Usually it's their husbands who are paying me, and no, I don't charge extra for incidental expenses, although some people feel like I should."
          wt_image ms2_training_1_56
          fairyn.c "I'm amazed you've made a business of this as it is."
          player.c "You're here, aren't you?"
          wt_image ms2_training_1_19
          fairyn.c "Yeah, but I'm filthy rich and love to waste my Daddy's money on things he'd disapprove of.  Think this would be one of them?"
          player.c "I don't know the man."
          wt_image ms2_training_1_20
          fairyn.c "I pretty much don't either, although I do know the number for his secretary who can probably get me an appointment to speak with him as long as I have some free time late in the day on the third Thursday of next month."
          wt_image ms2_training_1_21
          fairyn.c "Okay, I'm naked, and ready to learn all the things about pleasuring cock that I've failed to learn so far in my sheltered, nun-like existence."
          wt_image ms2_training_1_57
          fairyn.c "Please teach me the way of the cock sucker, oh wise and penis-bearing guru."
          $ title = "What technique do you want to teach her?"
          menu:
            "Girlfriend style":
              add tags 'girlfriend_bj' to fairyn
              player.c "The first thing you need is the right attitude. You want to convey the sense that his penis is as precious to you as it is to him, and you cherish the opportunity to be close to it."
              wt_image ms2_training_1_58
              fairyn.c "Umm, that almost sounds like I'd be leading him on. I just want to give him a blow job, not ask him to marry me."
              player.c "If you're really worried about that, you can always blow him off after you ... blow him off. The important thing is that you give him an experience he'll remember."
              wt_image ms2_training_1_57
              player.c "You're not here to give him a quick suck off like a street corner whore or a half-drunk college student. You're going to make his time with you special."
              wt_image ms2_training_1_59
              fairyn.c "Okay. One special time blow job coming up."
              wt_image ms2_training_1_60
              "Tossing her hair back out of the way, Fairyn reaches up to take your cock in her hand."
              wt_image ms2_training_1_36
              fairyn.c "Oh, what a cute cock you have!"
              wt_image ms2_training_1_35
              player.c "Stop.  First, don't ever tell him he has a 'cute' cock.  Second, let your actions convey your emotions.  Don't tell him you like his cock.  Show him through your actions that you adore his cock."
              wt_image ms2_training_1_60
              fairyn.c "You mean something like this?"
              wt_image ms2_training_1_37
              "Fairyn wraps both hands around your cock..."
              wt_image ms2_training_1_38
              "...and plunges it into her mouth."
              player.c "No. That's the half-drunk college student technique. Stop and try again."
              wt_image ms2_training_1_61
              player.c "This cock is special to you. Treat it that way. Show it you adore it. What do you do with someone you love?"
              wt_image ms2_training_1_62
              fairyn.c "I'm not good at forming strong emotional ..."
              player.c "What do normal people do with someone they love?"
              wt_image ms2_training_1_60
              fairyn.c "Kiss them?"
              player.c "Yes"
              wt_image ms2_training_1_29
              "Fairyn leans in and gives the tip of your cock a gentle kiss."
              wt_image ms2_training_1_31
              player.c "Good.  Now take my cock in your mouth again, only this time do it slowly and look at me while you're doing it."
              wt_image ms2_training_1_39
              player.c "That's it.  As your lips close around his cock, close your eyes, as if the sensation of having him inside you is overwhelming you."
              wt_image ms2_training_1_40
              player.c "Take your time.  Savor the taste of his cock entering your mouth."
              wt_image ms2_training_1_43
              player.c "Caress his balls with your hand as you swallow him.  Show him that you love the feel of his balls against your fingers as much as you love the feel of his cock between your lips."
              wt_image ms2_training_1_63
              player.c "Now and only now do you begin the blow job itself. And even now, take it slowly. You're not in a rush. Show him that. Show him that you're happy to spend as long as he wants like this."
              wt_image ms2_training_1_30
              player.c "Let everything else in the world fade away. All there is is this: his cock, your mouth, his balls, your hand. Nothing else matters. Nothing else exists."
              wt_image ms2_training_1_42
              player.c "Every once in a while, open your eyes and look up at him. When his gaze meets yours, smile. Don't stop blowing him, just smile as you continue to pleasure him, so he knows that you love doing this for him."
              wt_image ms2_training_1_43
              player.c "Then close your eyes again and go back to thinking about nothing except his cock and how much you enjoy bringing it pleasure."
              wt_image ms2_training_1_44
              player.c "You might think he'd hold out a long time with such a gentle approach, but he won't. You've sent the message that you'd do this all day for him, and that's all he needs to know to feel intensely turned on."
              wt_image ms2_training_1_45
              player.c "Combine that with the obvious joy you get from pleasuring his cock, and he'll be filling your mouth with cum in no time. Like this ... [player.orgasm_text]"
              wt_image ms2_training_1_63
              player.c "Don't stop blowing him just because he's cumming. Now's your chance to make him feel like a king. Show him you love the cum spurting from his cock as much as you love his cock itself."
              wt_image ms2_training_1_64
              player.c "Then show him you love sucking his cock as much when it's getting flaccid as you do when it's rock hard."
              wt_image ms2_training_1_32
              player.c "Seek out and find every drop of precious fluid and clean it off him before you let him out of your mouth."
              wt_image ms2_training_1_29
              player.c "And when you're finally done and he's completely clean, with every drop of his fluid safely in your belly, give him a last, final gentle kiss to reinforce how much you loved doing that for him."
              wt_image ms2_training_1_65
              fairyn.c "That was the most romantic sex I've ever had, and you were referring to yourself in the third person the whole time.  How fucked up is that?"
              wt_image ms2_training_1_46
              fairyn.c "And I paid for it!!  I should probably re-consider some of my life choices."
              wt_image ms2_training_1_66
              player.c "Lots of people pay me to have sex with them, or their wives. Most of those enjoy it, or at least I hope they do."
              fairyn.c "I expect they do. I expect the next guy I give a blow job to is going to enjoy it, too, even if he doesn't know who to thank."
              player.c "You could always give him my card, afterwards."
              wt_image ms2_training_1_46
              fairyn.c "That would kill the romance fast, wouldn't it? 'This tender blow job brought to you by a pupil of the guru of sex, the Wife Trainer!'"
              wt_image ms2_training_1_66
              fairyn.c "Actually, maybe that's a good idea? That way he won't get the wrong idea and think I was really trying to suggest he's special."
              player.c "What if he actually is special?"
              wt_image ms2_training_1_65
              fairyn.c "Don't be absurd! I'm totally not girlfriend material!! Not for anybody."
              sys "If she keeps saying that, you're going to get the idea that you can turn her into your girlfriend. You can't. At least not in this version of the game."
              $ player.desire_action_count += 1
              $ fairyn.blowjob_count += 1
              $ fairyn.swallow_count += 1
              orgasm notify
            "Porn star style":
              call fairyn_contact_pornstar from _call_fairyn_contact_pornstar_1
            "Submissive style":
              add tags 'submissive_bj' to fairyn
              player.c "What does every man feel when a beautiful woman kneels in front of him, getting ready to suck his cock?"
              wt_image ms2_training_1_58
              fairyn.c "Lucky?"
              player.c "That, too, but I was going for powerful.  Over and above the feeling of your lips and tongue on him, the feeling of power that comes from having you service him is an intense aphrodisiac."
              player.c "If you want to give him a blow job he'll never forget, you need to magnify that feeling and make him feel like the most powerful man in the world."
              wt_image ms2_training_1_57
              fairyn.c "By lowering myself?"
              player.c "By demonstrating that you're subservient to him and his wants. Which is what oral sex is all about - dedicating yourself to the pleasure of another. How you pleasure him, however, can have a big effect on how he feels about the experience."
              player.c "And yes, lowering yourself physically is a good start. Get down on your hands and knees."
              wt_image ms2_training_1_35
              player.c "Lower than that.  You've got four limbs.  Use them all."
              wt_image ms2_training_1_22
              player.c "Better.  Now come here and take my cock into your mouth."
              wt_image ms2_training_1_47
              player.c "No, no.  Not like that.  Every woman who's ever blown him has stroked his shaft as she pops him into her mouth.  Stop."
              wt_image ms2_training_1_61
              player.c "You want this to be a blow job he won't forget. You want to make him feel like the king of the world. Keep your hands to yourself. Even better, place them behind your back."
              wt_image ms2_training_1_48
              player.c "Much better. Now you have his attention. Now he knows this isn't going to be just another blow job."
              player.c "The first thing you'll notice on his face may be curiosity, or even surprise, but soon you'll see some other things - satisfaction, followed by contemplation."
              player.c "He's going to like this, the way you make him feel. And it's going to get him thinking about you, about what manner of creature you are, kneeling there, hands behind your back, pleasuring him with just your mouth."
              wt_image ms2_training_1_67
              player.c "Before long, he'll notice how vulnerable you look with your hands tucked out of the way.  He'll' reach out and caress your face, or caress your hair, exploring your vulnerability."
              wt_image ms2_training_1_49
              player.c "He may take your hair in his hand and start guiding your head, pulling you this way or that, finding out how servile you really are."
              wt_image ms2_training_1_68
              player.c "Your job is to show him that you're accepting of whatever he wants to do with you.  Use your eyes and your body language to send the message that he's in charge, and you like having him in charge."
              wt_image ms2_training_1_67
              player.c "Now follow me. I'm going to back up."
              wt_image ms2_training_1_69
              player.c "There.  See how natural that was?  You went instinctively to all fours."
              player.c "If he's having trouble taking charge, get into this pose on your own.  It sends exactly the right message - he's the master, you're the pet; he's in charge, you're here to serve."
              wt_image ms2_training_1_50
              player.c "Keep following me, pet.  I'm going to back up and make myself comfortable on the sofa.  Keep your mouth on me and follow your master."
              wt_image ms2_training_1_70
              "She follows obediently, led by your cock like it was a leash."
              wt_image ms2_training_1_71
              "You maneuver your way backwards across the room until you feel the coach behind you and settle into it, making yourself comfortable as she works your dick, trying hard to get you to cum."
              wt_image ms2_training_1_51
              "It's a much better effort than her previous attempts at fellatio - more earnest, more dedicated to the sole focus of your pleasure."
              wt_image ms2_training_1_72
              "With only her lips and tongue to pleasure you, she can't hasten the process, can't pump your shaft to speed your orgasm.  She needs to coax the climax out of you, little by little."
              wt_image ms2_training_1_51
              "It takes a while, but eventually she succeeds."
              wt_image ms2_training_1_73
              player.c "[player.orgasm_text]"
              wt_image ms2_training_1_22
              "When she finishes swallowing, she looks at you."
              fairyn.c "If I give a guy a blow job like that, he'll think I want him to control me."
              player.c "You like it when men take control of you."
              wt_image ms2_training_1_62
              fairyn.c "Only when I'm in one of my 'moods'."
              player.c "Were you in that sort of mood when you came over today?"
              "She shakes her head."
              wt_image ms2_training_1_61
              player.c "And yet you're still on all fours, waiting for permission to get up.  Which you don't have yet, by the way."
              "You give her time to sort through what she's feeling, before letting her get dressed and leave."
              sys "Despite what she's feeling, she's not about to become a full-time submissive. Not in this version of the game."
              $ player.submission_action_count += 1
              $ fairyn.blowjob_count += 1
              $ fairyn.swallow_count += 1
              orgasm notify
        "Hypnotize her" if player.can_hypno(fairyn):
          $ fairyn.hypno_session() # deletes energy and records she's been hypnotized
          wt_image ms2_training_1_4
          player.c "First thing we do is that you look at this."
          call focus_image from _call_focus_image_54
          player.c "Look at this and listen to me.  Listen to me now.  Listen to my voice.  Only my voice now.  Only my voice."
          wt_image ms2_training_1_55
          player.c "You came here to learn how to please men. I'm a man and removing your top will please me, Fairyn.  Take it off now so that I can see your breasts."
          wt_image ms2_training_1_56
          "She happily pulls down her top. Fairyn's not shy about her body at the best of times, and certainly not while hypnotized."
          wt_image ms2_training_1_74
          $ title = "What do you have her do?"
          menu:
            "Blow you":
              player.c "I'm going to help you, Fairyn. I'm going to help you improve your oral skills."
              wt_image ms2_training_1_58
              player.c "Kneel down and show me how happy you are for the opportunity to learn how to suck my cock properly."
              wt_image ms2_training_1_10
              "She drops in front of you, takes out your cock, and happily takes it into her mouth."
              wt_image ms2_training_1_11
              "You let her work on your dick for a while.  Despite her enthusiasm, she's really not good at it."
              wt_image ms2_training_1_75
              player.c "Can you at least deep throat properly?"
              wt_image ms2_training_1_13
              "Based on her effort, the answer appears to be 'no'.  Looks like you're going to be teaching her something today after all."
              wt_image ms2_training_1_14
              player.c "When you're sucking a man, Fairyn, you want to take all of his cock in your mouth. The more of his cock you get into your mouth, the more he'll enjoy it, and you want him to enjoy himself when you're sucking him.  You'll help him enjoy himself by taking his whole cock into your mouth."
              wt_image ms2_training_1_15
              player.c "You won't gag taking his cock into your mouth, Fairyn. It feels good feeling his cock filling your mouth. The tip of his cock lodging in the back of your throat doesn't make you gag, it makes you happy.  Happy that you're providing him so much pleasure."
              wt_image ms2_training_1_16
              player.c "Your throat relaxes when you feel his cock reaching the back of your tongue. You feel wet between the legs, excited at the knowledge of how much pleasure you're giving him, and how much more pleasure you're about to give him.  Remove your hand so it's not in the way of bringing him pleasure."
              wt_image ms2_training_1_17
              player.c "Now nothing is the way of you taking him completely inside you.  Your clit throbs, and the excitement makes you ignore your gag reflex. You don't need to gag, not when your mouth and throat are so happy to receive his cock.  You know this is making him feel great, and that makes you feel great, too."
              wt_image ms2_training_1_18
              player.c "When his cock is fully inside your mouth, you feel compelled to look at him. You know he's going to empty his load down your throat, and you want to watch his face as he does.  You want to see how much he's enjoying your mouth.  Watch my face, Fairyn, and see how much I'm enjoying your mouth."
              player.c "[player.orgasm_text]"
              wt_image ms2_training_1_52
              "Turns out you taught her something after all. You bring her out of her trance and send her home believing that she got her money's worth of instructions out of you, which she did."
              add tags 'hypno_taught_deep_throat' to fairyn # does nothing right now
              $ fairyn.hypno_blowjob_count += 1
              $ fairyn.hypno_swallow_count += 1
              orgasm notify
            "Blow an imaginary penis":
              wt_image ms2_training_1_58
              player.c "You want to learn how to please a man with your mouth, Fairyn.  To do that, you need to practice."
              wt_image ms2_training_1_57
              player.c "Open your mouth, Fairyn.  There's a penis right in front of you.  Practice pleasuring it with your mouth."
              wt_image ms2_training_1_6
              "She opens her mouth, but looks at you doubtfully."
              player.c "It's right there, Fairyn.  Turn around and suck it.  A big, beautiful penis just waiting for you to please it."
              wt_image ms2_training_1_7
              player.c "That's it, it's right there.  Open your mouth and take it all inside you."
              wt_image ms2_training_1_8
              player.c "No, not your finger.  The penis in front of you is much bigger than that.  Practice pleasuring the penis, Fairyn.  Practice sucking on the big, beautiful penis in front of you."
              wt_image ms2_training_1_76
              "She works away at the air for some time ..."
              wt_image ms2_training_1_9
              "... before turning and looking at you in frustration."
              player.c "Can't get the penis to cum, Fairyn?  That's because you need more practice.  Keep working at it. Cocks won't cum for you until you learn how to pleasure them properly."
              wt_image ms2_training_1_77
              "You doubt this will actually make her a better cock sucker, but who knows?  Maybe the humility of facing a cock she can't make cum will make her more diligent and attentive the next time she sucks a real penis."
              wt_image ms2_training_1_52
              player.c "When you tire of watching her bob her head back and forth in the air, you bring her out of the trance and send her home, believing that she got her money's worth of instructions out of you."
              notify
        "Never mind (cancel training)":
          wt_image living_room.image
          "Since the training goes nowhere, you skip it. You have better things to spend your Energy on. Find something else to do with your day."
          add tags 'not_trained' to fairyn
      add tags 'no_hypnosis' to fairyn
      call character_location_return(fairyn) from _call_character_location_return_198
      if fairyn.has_tag('not_trained'):
        rem tags 'not_trained' from fairyn
        # finished without training her
        $ fairyn.bj_training_status = 5
      else:
        # finished by training her
        $ fairyn.bj_training_status = 6
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        $ player.extra_clients_fee_this_week += 50
        end_day
    "Not Yet":
      sys "This engagement offer will never expire. you can take your time getting back to her."
      $ fairyn.action_show_message.name = "Reply to Fairyn"
      if not fairyn.wait_on_message:
        $ fairyn.wait_on_message = True
        $ fairyn.wait_for_message_period = 10000000
    "Never (Deletes Message)":
      # finished without training her
      $ fairyn.bj_training_status = 5
      $ fairyn.change_status("rejected")
      $ living_room.remove_action(fairyn.action_show_message)
  return

label fairyn_contact_pornstar:
  add tags 'pornstar_bj' to fairyn
  wt_image ms2_training_1_21
  player.c "If you want to give the man an unforgettable experience, you have to set the mood right from the beginning. Approach him like his cock is the most desirable thing in the whole world, and you can't wait to get your mouth on it."
  wt_image ms2_training_1_75
  fairyn.c "Like this?  Mmmmm ... I can't wait to put your big, fat cock in my mouth!"
  player.c "Not bad.  Maybe wait to see what his cock looks like first, before describing it.  When you do take his cock out, ooh and aahh over it, like it's the most interesting toy you've ever had access to, and provide the compliments then."
  wt_image ms2_training_1_23
  fairyn.c "Ooh!  Aahh!  Your cock looks so good!!  It smells so good!!  I can't wait to taste it."
  player.c "Tasting his cock can wait.  You're going for total oral worship, just like the porn stars do."
  wt_image ms2_training_1_24
  player.c "Begin with his balls.  Taste, lick and suck them first."
  wt_image ms2_training_1_25
  player.c "Don't rush.  Take your time, like you're going to make him cum from pleasuring his balls alone."
  wt_image ms2_training_1_26
  player.c "See how hard and throbbing my cock is now?  That's your cue that it's time to shift your attention to my shaft."
  wt_image ms2_training_1_27
  player.c "Maintain eye contact with him, and let him know how much you're enjoying this.  Lick him up and down, like he's your favorite flavor lolly.  Drool all over him, like you can't control your body's reaction to the taste of him."
  wt_image ms2_training_1_28
  fairyn.c "Mmmm.  You taste so good!  I love getting to suck your cock."
  wt_image ms2_training_1_29
  player.c "Now it's time to get him off.  Take him into your mouth like he's the dessert you've been waiting all day to swallow."
  wt_image ms2_training_1_30
  player.c "Use lots of saliva and lots of tongue. You want to be the woman he'll always remember, the one who sucked him off with wild abandon."
  wt_image ms2_training_1_32
  player.c "He's going to be fighting hard now to keep his composure.  Every fiber in his body will be telling him to cum.  Let him know you want that, too. Tell him how much you want him to cum."
  wt_image ms2_training_1_31
  fairyn.c "Mmmm.  Cum for me!  Fill my mouth with your hot, salty spunk!!"
  wt_image ms2_training_1_44
  player.c "That's almost right. After you tell him you want his cum, take it from him.  Suck and lick and pump him until you break down every last ounce of his self-control, and he has no choice but to shoot his load."
  wt_image ms2_training_1_45
  player.c "But don't shoot it into your mouth.  He's had lots of women do that for him.  Some will swallow and some will spit it out, and some will even take a facial if he asks them to."
  wt_image ms2_training_1_31
  player.c "You're going to be the woman he doesn't have to ask to take a facial.  You're going to be the woman who points his dick at your face and pumps his cum all over you because you love it, because you can't imagine a better place for his sperm than dripping down your cheeks."
  wt_image ms2_training_1_33
  player.c "[player.orgasm_text]"
  wt_image ms2_training_1_34
  fairyn.c "Did I pass?"
  player.c "You did. If you ever want to apply your new skills professionally, I could get you work."
  wt_image ms2_training_1_78
  fairyn.c "You mean I could be a real porn star? or a real whore??  Tempting, but I'm trying to use up all of Daddy's money.  Earning money of my own would be counter productive."
  wt_image ms2_training_1_79
  fairyn.c "I think I'll just practice your technique on the next few guys I pick up at a bar.  Do you think what you taught me will work for a BJ I give in the car?  I don't necessarily want to take them home."
  wt_image ms2_training_1_80
  player.c "Try it out and let me know.  If you make a mess on your car seats, you can spend more of your father's money getting them cleaned."
  wt_image ms2_training_1_81
  "She giggles, then cleans off her face, dresses and heads home."
  $ player.sos_action_count += 1
  $ fairyn.blowjob_count += 1
  $ fairyn.facial_count += 1
  orgasm notify
  return

# Character Rejected
label master_m_rejected:
  sys "You may no longer accept this assignment."
  return

label fairyn_rejected:
  sys "You may no longer accept this assignment."
  return

# Display Portrait
# CHARACTER: Display Portrait
label master_m_update_media:
    if current_location == club:
        $ master_m.change_image('master_club_1')
    return

label diamond_update_media:
  if current_location == club and diamond.has_tag('club_maid_today'):
    $ diamond.change_image('ms1_maid_1')
  elif current_location == stage and diamond.has_tag('dancing_today'):
    $ diamond.change_image('ms1_stripper_2')
  return

label fairyn_update_media:
    if current_location == club:
        if fairyn.has_tag('club_maid_event_happened'):
            $ fairyn.change_image('ms2_club_1_1')
        else:
            $ fairyn.change_image('ms2_club_maid_1_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label master_m_examine:
  ## NOTE: this should be restricted to in Club only
  "A well dressed man is surrounded by a hovering group of women."
  return

label diamond_examine:
  if current_location == club and diamond.has_tag('club_maid_today'):
    "Master M has put Diamond to work tidying up around the Club today."
  elif current_location == stage and diamond.has_tag('dancing_today'):
    "Diamond's owner is making her perform at the Club tonight. She doesn't seem too happy about it, so this must be a punishment, no doubt for another bout of brattiness."
  return

label fairyn_examine:
    if fairyn.in_area('club'):
        if not fairyn.has_tag('club_maid_event_happened'):
            "Fairyn the Trust Fund Baby seems to have her eye on one of the maids assigned to clean the Club.  She's ignoring everyone else, including you."
        elif player.has_tag('fairyn_gagged_photos') and not fairyn.has_tag('discussed_photos_with_you'):
            "Fairyn the Trust Fund Baby looks like she's debating whether to approach you or not."
        else:
            "Fairyn the Trust Fund Baby is wandering around the Club, seemingly bored.  She's ignoring everyone, including you."
            sys "There's no additional content for Fairyn in the Club, at least not yet."
    return

# Talk to Character
label master_m_talk:
    if master_m.in_area('club'):
        wt_image master_m.image
        call master_m_examine from _call_master_m_examine
        if diamond.training_result == 2:
            "He's not interested in talking to you."
        elif diamond.training_result == 6 or diamond.training_result == 8 or master_m.lent_him_a_slave > 1:
            if master_m.encounter_possible == 1:
                $ master_m.encounter_possible = 2
                if diamond.training_result == 6 or diamond.training_result == 8:
                    master_m.c "It's nice to meet you in person. Great job with Diamond."
                    "He shakes your hand."
                else:
                    master_m.c "It's nice to meet you in person."
                    "He shakes your hand."
            else:
                "Master M greets you warmly."
            if master_m.lent_him_a_slave == 2 or master_m.lent_him_a_slave == 4:
                master_m.c "Thanks for sending [master_m.name_of_your_slave_loaned] to spend time with me."
                master_m.c "[master_m.experience_with_your_slave]"
                $ master_m.lent_him_a_slave += 1
            call expandable_menu(master_m_club_talk_menu) from _call_expandable_menu
        else:
            if master_m.encounter_possible == 1:
                master_m.c "It's nice to meet you in person."
                "He's cordial, but not interested in chatting."
                $ master_m.encounter_possible = 2
            else:
                "He's cordial, but not interested in chatting."
            if master_m.lent_him_a_slave == 0 and player.slavegirl_count > 0:
                "You might be able to improve your relationship with Master M if you lend him one of your slaves for the evening."
                $ title = "Try and improve your relationship?"
                menu:
                    "Offer to lend him a slave":
                        player.c "I know things didn't go as well with Diamond's training as you had hoped for. Let me make it up to you. How would you like to have the use of one of my slaves for the night? No charge."
                        master_m.c "Thank you, that's very kind of you. Yes, I'll take you up on that offer."
                        $ master_m.lent_him_a_slave = 1
                        add tags 'm_waiting_for_slave' to player
                        sys "You can choose who to send to him from your bedroom."
                    "Not now":
                        pass
        wt_image current_location.image
    else:
        "The two of you have nothing to talk about right now."
    return

label master_m_club_talk_nothing:
    "You chit chat with him briefly, then move on."
    return

label master_m_club_talk_difficult_truth:
    player.c "There's no easy way to say this, so I'm just going to come out with it, because you may need to start preparing yourself to this idea."
    player.c "If Diamond is truly the person she says she is, you'll need to sell her. Her feelings towards you are too conflicted. If she truly needs to be owned, she'll continue to fight you."
    player.c "She loves you and can't see you as just her owner, but I don't think she'll accept being your submissive because she seems to crave actual ownership, not just domination."
    "Master M is quiet for a moment before replying,"
    master_m.c "I hope it doesn't come to that."
    "You hope not, too, because he seems to care deeply for her."
    add tags 'discussed_difficult_truth' to master_m
    return

label master_m_club_talk_lending_slave:
    player.c "How would you like to have the use of one of my slaves for the night?  No charge."
    master_m.c "Thank you, that's very kind of you.  Yes, I'll take you up on that offer."
    $ master_m.lent_him_a_slave = 1
    add tags 'm_waiting_for_slave' to player
    sys "You can choose who to send to him from your bedroom."
    return

# note: this would fit better in Bethany or Hannah's script, but works here
label master_m_club_talk_principal_videos:
    player.c "Have you seen the school's fund raising videos?"
    master_m.c "The torture ones? Yes, I have. A friend forwarded the link to me."
    if bethany.torture_count == 4 or bethany.torture_count == 6:
        master_m.c "Very brave of you to volunteer as a victim. Our local Principal seems to have a sadistic streak. Then again, I've always suspected most Principals and Vice-Principals were closet sadists."
    player.c "You should lend Diamond to her. It's for a good cause."
    master_m.c "I have been trying to get Diamond used to serving women, but she wouldn't be able to take the torture Principal Hannah dishes out."
    player.c "I'll speak to Hannah, tell her she needs to dial down the physical torment. For a new victim and another round of fundraising, I'm sure she'd be willing to accommodate."
    master_m.c "Okay. Tell her as long as she stays away from the electricity, she can verbally abuse Diamond as much as she wants. Some sexual servitude would be good, too. Diamond needs more experience pleasing women."
    master_m.c "Like you said, it's for a good cause."
    $ master_m.lend_diamond_to_school = 2
    if bethany.torture_week == 0:
        $ bethany.torture_week = week + 1
    return

# note: this would fit better in Samantha's script
label master_m_club_talk_barista_domme:
    player.c "I have a friend who's interested in exploring her Domme side.  She's looking for someone to train her, preferably a woman."
    master_m.c "Have you met Cassandra here at the Club?  She's an experienced Domme.  She may be interested, or may know someone who could help."
    return

# note: this would fit better in Alexis' script
label master_m_discuss_alexis_anal:
    player.c "Have you ever had to train a sub who believed she couldn't do anal sex?  Not just a dislike of anal, but a belief she physically can't do it."
    master_m.c "Hmmm.  No, not personally, but I have heard of that fear."
    player.c "Any thoughts on the best way to overcome it?"
    master_m.c "I think the typical approach is to start with a small anal plug and move up to gradually larger plugs as she becomes used to it."
    "He chuckles."
    master_m.c "Or if you don't mind outsourcing, you could always send her to Angie."
    player.c "Who's Angie?"
    master_m.c "A woman with a great love for all things anal.  She has a fascination with the rear door that is rarely equalled and never exceeded among women."
    master_m.c "We call her Angie the Anal Domme ... though not to her face, of course.  She'd work on your friend's concern with a passion and determination that would be a wonder to observe.  Assuming your friend would accept training from a woman, of course."
    "He digs out Angie's contact information for you."
    master_m.c "She works during the week, but usually has time for playmates on the weekends.  Tell her you have an anal virgin for her and I know she'll make time for you."
    add tags 'anal_domme_opened' to alexis
    sys "Once she's ready to let you work on her anal deficiencies, you can send [alexis.name] to Angie for training on the weekend, if you want."
    return

# should put this in Lee's script, too, but since the others are here, will keep it with them
label master_m_discuss_lee:
    player.c "Are you still trying to train Diamond to serve women more willingly?"
    master_m.c "Sadly, yes.  It's still a difficult subject with her."
    player.c "I've been submitting myself to a wonderful Domme.  She can come across as a bit crazy, frankly, but she knows what she's doing.  I've seen her in action with other women and let's just say she knows how to get her way."
    master_m.c "If you can vouch that she won't harm Diamond, I'd be happy to lend Diamond to her for a session.  The more experience serving women Diamond gets, the easier it should become for her."
    "Now you just need to speak to Lee to find out if she'd be interested.  And remind her about the 'no harm' part, so that hopefully she doesn't let her sadistic streak run wild on poor Diamond."
    $ lee.diamond_status = 1
    return

label diamond_talk:
    if diamond.in_area('club'):
        call diamond_update_media from _call_diamond_update_media
        wt_image diamond.image
        if diamond.training_result < 3:
            "She avoids you as you try to approach her."
        elif diamond.has_tag('club_maid_today'):
            $ diamond.training_session()
            if diamond.training_result >= 6:
                if diamond.training_result >= 7:
                    wt_image ms1_maid_3
                    if diamond.training_result == 8:
                        diamond.c "Hello Sir!  Master wants me to get the Club tidied up."
                        "She sneaks a glance at an occupied private room behind you."
                        diamond.c "You could inspect my work in there, unless there was something else you wanted from me?"
                    else:
                        diamond.c "Hello Sir!  Master wants me to get the Club tidied up."
                        "She sneaks a glance at an occupied private room behind you."
                        diamond.c "Did you want to inspect my work in there?"
                elif diamond.training_result == 6:
                    wt_image ms1_maid_2
                    diamond.c "Hello Sir. I don't have time to talk. Master wants me to get the Club tidied up."
                    "She hesitates, as if unsure as to whether she's dismissed or not."
                $ title = "What do you want to do?"
                menu:
                    "Dismiss her":
                        player.c "That's fine. You can go."
                        wt_image ms1_maid_24
                        diamond.c "Thank you Sir!"
                        "She scurries away."
                    "Compliment her on the work she's doing" if diamond.training_result == 6 or diamond.training_result == 8:
                        player.c "You're doing a great job, [diamond.training_name]."
                        wt_image ms1_maid_24
                        diamond.c "Thank you, Sir. May I continue?"
                        player.c "Go ahead."
                        wt_image ms1_maid_3
                        "She scurries away with a little bounce in her step."
                    "Find fault with the work she's doing" if diamond.training_result == 6 or diamond.training_result == 8:
                        player.c "You're not doing a very good job, [diamond.training_name]."
                        wt_image ms1_maid_4
                        diamond.c "Sir?"
                        player.c "You heard me. There's dust on the underside of that table, those picture frames haven't been straightened, and I just came from the washroom which is a mess."
                        wt_image ms1_maid_23
                        diamond.c "I'm sorry, Sir. I'll do better."
                        wt_image ms1_maid_4
                        $ title = "Let her go?"
                        menu:
                            "Provide her with motivation":
                                player.c "Turn around."
                                wt_image ms1_maid_23
                                diamond.c "Sir?"
                                player.c "You heard me."
                                wt_image ms1_maid_5
                                diamond.c "Yes, Sir."
                                player.c "Bend over."
                                wt_image ms1_maid_6
                                diamond.c "Sir, I'll do better."
                                player.c "Yes, you will.  Do you want people to think your Master's slaves won't even clean properly for him?"
                                diamond.c "No, Sir!"
                                player.c "Then right over with you, hands touching your toes."
                                wt_image ms1_maid_7
                                "She bends over, pulling her panties down as she does, presumably as her Master has trained her to do  ... *smack*"
                                wt_image ms1_maid_26
                                diamond.c "OUCH!"
                                player.c "Keep your crying to a minimum. People are trying to enjoy themselves.  And take your hand away."
                                wt_image ms1_maid_7
                                diamond.c "Sorry, Sir."
                                "*smack*"
                                diamond.c "ouch"
                                "*smack*"
                                diamond.c "ouch!"
                                "*smack*"
                                diamond.c "ouch!!"
                                "*smack*"
                                diamond.c "ouch!!!"
                                wt_image ms1_maid_26
                                player.c "Get back to your work, now.  And put more effort in."
                                diamond.c "Yes, Sir."
                                wt_image ms1_maid_5
                                "She pulls her panties back up over her now sore ass and scurries off to her cleaning."
                            "Let her get back to her cleaning":
                                player.c "See that you do. Get back to your cleaning."
                                wt_image ms1_maid_2
                                diamond.c "Yes, Sir.  Thank you, Sir."
                    "Inspect her uniform" if diamond.training_result == 6 or diamond.training_result == 8:
                        player.c "Let me inspect your uniform."
                        wt_image ms1_maid_23
                        diamond.c "Sir?"
                        player.c "The Club has dress codes and standards for workers. Are you wearing panties?"
                        wt_image ms1_maid_8
                        diamond.c "Yes, Sir. Of course, Sir."
                        player.c "Remove them."
                        diamond.c "But then I'll be offside the dress code."
                        player.c "It doesn't apply when under the direct supervision of a Club member. I want to know you're clean yourself before I let you go back to trying to clean the Club."
                        wt_image ms1_maid_9
                        diamond.c "Yes, Sir."
                        player.c "Just as I expected, you're a little dusty down there. Use your feather duster on it."
                        wt_image ms1_maid_10
                        diamond.c "Yes, Sir."
                        "Hesitantly she strokes the feather duster across her sex."
                        wt_image ms1_maid_22
                        "You can smell her arousal by the time she lifts the duster away."
                        player.c "Keep going."
                        wt_image ms1_maid_10
                        diamond.c "Yes, Sir."
                        "She bites her lip as the sensation of the duster between her legs causes her to moisten."
                        wt_image ms1_maid_22
                        player.c "A little more."
                        wt_image ms1_maid_10
                        "She can't contain a moan as her sex becomes fully wet."
                        diamond.c "oohhh"
                        player.c "That's better. Put your panties back on and get back to work."
                        wt_image ms1_maid_8
                        diamond.c "Yes, Sir."
                        "She pulls her lace panties up. They immediately drench through the thin material as they come in contact with her sex."
                        wt_image ms1_maid_2
                        "She looks at you wistfully, perhaps wishing you'd asked her to dust herself just a couple of minutes more, then scurries off to her work."
                    "Join her in the private room" if diamond.training_result >= 7:
                        wt_image ms1_maid_11
                        "As soon as you're in private together, she removes her clothes and drops to her knees."
                        diamond.c "It's good to see you again, Sir. I need to get back to cleaning the Club, but before I do, I thought perhaps I could clean something of yours first?"
                        wt_image ms1_maid_25
                        player.c "What would your Master say about that, [diamond.training_name]?"
                        wt_image ms1_maid_12
                        diamond.c "He didn't tell me I couldn't suck your dick, Sir."
                        $ title = "What do you want to do?"
                        menu:
                            "Let her suck your dick":
                                add tags 'club_sex' to diamond
                                wt_image ms1_maid_28
                                diamond.c "Let me get this cleaned off for you Sir."
                                wt_image ms1_maid_20
                                "She takes your cock in her hand and starts gently licking it."
                                wt_image ms1_maid_21
                                "She's a bit of a tease, but she does get every part of your cock cleaned, and your balls. She licks them all over until she's satisfied that they've been thoroughly tongue washed ..."
                                wt_image ms1_maid_29
                                "... then she starts bobbing her pretty head up and down on your hard shaft."
                                wt_image ms1_maid_30
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her":
                                        wt_image ms1_ms2_joint_event_3_1
                                        "She kneels at your feet, making obvious swallowing motions as you pump her mouth full of cum."
                                        player.c "[player.orgasm_text]"
                                        $ diamond.swallow_count += 1
                                    "On her":
                                        wt_image ms1_training_48
                                        player.c "[player.orgasm_text]"
                                        "She catches as much as she can in her mouth, making a big show about swallowing it.  The rest she scoops up with her fingers, licking them off while you watch."
                                        $ diamond.facial_count += 1
                                wt_image ms1_maid_3
                                "With a smile on her face, she then dresses and goes back to cleaning, seemingly pleased to have pleased you."
                                $ diamond.blowjob_count += 1
                                orgasm notify
                            "Fuck her instead":
                                add tags 'club_sex' to diamond
                                player.c "I'd rather fuck you, [diamond.training_name]."
                                wt_image ms1_maid_14
                                diamond.c "Okay, Sir."
                                "She leans back and spreads her legs."
                                $ title = "Where do you fuck her?"
                                menu:
                                    "Fuck her pussy":
                                        wt_image ms1_maid_17
                                        "She moans as you push yourself into her bare pussy. She's wet and you slide easily in and out of her, her arousal growing with your own."
                                        diamond.c "oohhh"
                                        wt_image ms1_maid_31
                                        "Her moans grow louder as you fuck her"
                                        diamond.c "ooohhhh  ...  oooohhhh"
                                        if diamond.training_result == 8:
                                            wt_image ms1_maid_17
                                            "Fighting hard to control herself, she looks up at you, hopefully."
                                            diamond.c "Am I allowed to cum, Sir?"
                                            $ title = "What do you tell her?"
                                            menu:
                                                "Not today":
                                                    wt_image ms1_maid_18
                                                    player.c "Not today, [diamond.training_name].  Today is only about my pleasure."
                                                    diamond.c "Yes, Sir."
                                                    wt_image ms1_maid_31
                                                    "She does her best to conceal her disappointment and keep her pleasure in check. It's not easy on her, as she enjoys the feeling of your cock moving in and out of her, but she manages to avoid reaching orgasm."
                                                    wt_image ms1_maid_17
                                                    "You on, the other hand, do not."
                                                    player.c "[player.orgasm_text]"
                                                "Go ahead":
                                                    wt_image ms1_maid_19
                                                    "She reaches a hand between her legs and rubs her clit as you stroke in and out of her. It only takes her a moment to cum, and the sensation of her body shuddering to orgasm around your cock beings you along with her."
                                                    diamond.c "Oooohhhhh!!!"
                                                    player.c "[player.orgasm_text]"
                                                    $ diamond.orgasm_count += 1
                                        else:
                                            wt_image ms1_maid_31
                                            "Her moans grow louder as you fuck her"
                                            diamond.c "ooohhhh  ...  oooohhhh"
                                            wt_image ms1_maid_19
                                            "Before long, she reaches a hand between her legs and rubs her clit as you stroke in and out of her. It only takes her a moment to cum, and the sensation of her body shuddering to orgasm around your cock beings you along with her."
                                            diamond.c "Oooohhhhh!!!"
                                            player.c "[player.orgasm_text]"
                                            $ diamond.orgasm_count += 1
                                        $ diamond.sex_count += 1
                                    "Fuck her ass":
                                        wt_image ms1_maid_32
                                        "It wasn't what she had in mind when she came in here, but she doesn't say 'no' as you press your cock against - and then into - her tight rosebud."
                                        wt_image ms1_maid_33
                                        "This is clearly uncomfortable for her.  The smell from her sex tells you it's also stimulating to her.  She seems to enjoy this form of intimate pain."
                                        wt_image ms1_maid_39
                                        $ title = "What do you do?"
                                        menu:
                                            "Just enjoy yourself":
                                                wt_image ms1_maid_34
                                                "However much she's enjoying this, you enjoy it even more.  You thrust roughly in and out of her as she tries to deal with the intense sensation of being used as your ass slut."
                                                wt_image ms1_maid_35
                                                "When you finally cum, she groans along with you, a combination of arousal and relief on her part, and pure pleasure on yours."
                                            "Try and make it feel good for her":
                                                wt_image ms1_maid_36
                                                "Shoving two fingers inside, you finger fuck her as you ass fuck her."
                                                wt_image ms1_maid_16
                                                diamond.c "oohhh ... thank you for making this feel good, Sir.  Nothing would feel better, though, than being made to focus on pleasing you with my ass."
                                                wt_image ms1_maid_37
                                                player.c "Enough talk, [diamond.training_name].  You want to serve?  Show me.  Use your ass to get me off."
                                                wt_image ms1_maid_38
                                                "She grinds down hard on your cock, fucking you as best she can ..."
                                                wt_image ms1_maid_15
                                                "... then groans in relief as you flip her over and finish the job."
                                        player.c "[player.orgasm_text]"
                                        diamond.c "oohhh"
                                        $ diamond.anal_count += 1
                                wt_image ms1_maid_3
                                "With a smile on her face, she dresses and goes back to cleaning, seemingly pleased to have pleased you."
                                orgasm notify
                            "Have her play with herself":
                                player.c "I just want to watch you play with yourself, [diamond.training_name]."
                                wt_image ms1_maid_11
                                diamond.c "Mmmm.  I have to get some of my clothes back on, in case someone walks in before I finish.  Sometimes it takes us girls a little longer than you boys."
                                wt_image ms1_maid_22
                                "She positions herself, legs spread in front of you, and sighs contentedly as she runs the feather duster down her body ..."
                                wt_image ms1_maid_10
                                "... to between her legs, where she strokes it back and forth across her sex. Despite her comment about girls taking longer, she gets wet quickly, and starts dripping soon after that."
                                diamond.c "ooohhhh! ... ooohhhhh!!"
                                if diamond.training_result == 8:
                                    wt_image ms1_maid_23
                                    "Lifting the duster away from her sex, she looks up at you hopefully."
                                    diamond.c "Am I allowed to cum, Sir?"
                                    $ title = "What do you tell her?"
                                    menu:
                                        "Not today":
                                            wt_image ms1_maid_22
                                            player.c "Not today [diamond.training_name].  Pull yourself together and get back to your cleaning."
                                            wt_image ms1_maid_8
                                            diamond.c "Yes, Sir."
                                            "She pulls her lace panties up. They immediately drench through the thin material as they come in contact with her sex. She looks at you wistfully, then scurries off to her work."
                                        "Go ask her Master":
                                            wt_image ms1_maid_22
                                            player.c "If you want on orgasm, you'll have to go ask your Master for one, [diamond.training_name]. He owns you, not me."
                                            wt_image ms1_maid_8
                                            diamond.c "Yes, Sir."
                                            "She pulls her lace panties up. They immediately drench through the thin material as they come in contact with her sex. She looks at you wistfully, then scurries off to her work."
                                        "Go ahead":
                                            wt_image ms1_maid_10
                                            "A couple of more strokes of the duster along her clit and she's over the edge."
                                            diamond.c "Oooohhhhh!!!"
                                            wt_image ms1_maid_24
                                            diamond.c "Oh! Thank you for that, Sir!!"
                                            wt_image ms1_maid_3
                                            "She pulls her clothes on, gives you a quick peck on the cheek, and dances happily back to her cleaning."
                                            $ diamond.orgasm_count += 1
                                else:
                                    "A couple of more strokes of the duster along her clit and she's over the edge."
                                    diamond.c "Oooohhhhh!!!"
                                    wt_image ms1_maid_3
                                    diamond.c "Oh Thank you for that, Sir!!"
                                    "She pulls her clothes on, gives you a quick peck on the cheek, and dances happily back to her cleaning."
                                    $ diamond.orgasm_count += 1
                                $ diamond.masturbation_count += 1
                            "Tell her to go back to cleaning":
                                player.c "Not today, [diamond.training_name]. You'd best get back to your cleaning."
                                wt_image ms1_maid_12
                                diamond.c "Okay, Sir. Perhaps another time?"
                                "She wantonly flashes you a view of her pussy before getting dressed and going back to cleaning, no doubt hoping to provoke a different response next time."
            else:
                diamond.c "I don't have time to talk. Master wants me to get the Club tidied up."
                "She hurries away before you can say anything more."
        elif diamond.has_tag('dancing_today'):
            wt_image ms1_stripper_2
            "Diamond lowers her eyes as you approach."
            wt_image ms1_stripper_15
            diamond.c "I'm being punished for acting like a brat. I'm not allowed to touch or be touched today, and I can't talk to anybody except to explain that I'm here to take my clothes off."
            if diamond.action_private_show is None:
                $ diamond.action_private_show = diamond.add_action("Ask for a Private Show", label="_private_show", condition = "diamond.can_be_interacted and diamond.has_tag('dancing_today') and diamond.location == stage")
        wt_image current_location.image
    else:
        "The two of you have nothing to talk about right now."
    return

label fairyn_talk:
    if fairyn.in_area('club') and not fairyn.has_tag('club_maid_event_happened'):
        wt_image ms2_club_maid_1_1
        "She's preoccupied with something, or someone, else and is ignoring you."
    elif fairyn.in_area('club') and player.has_tag('fairyn_gagged_photos') and not fairyn.has_tag('discussed_photos_with_you'):
        add tags 'discussed_photos_with_you' to fairyn
        wt_image ms2_club_1_4
        fairyn.c "Hey, I've been meaning to ask you something.  What did you do with those photos you took of me?"
        player.c "Why?  Are you worried I'll blackmail you with them?"
        wt_image ms2_club_1_5
        fairyn.c "Would you blackmail me with them?  That'd be kinda exciting.  'Daddy, I need money or a really bad man will ruin my reputation!'"
        wt_image ms2_club_1_1
        fairyn.c "It's a shame Daddy already thinks I'm a whore.  It makes it almost impossible to disappoint him these days."
        wt_image ms2_club_1_3
        fairyn.c "Anyway, blasting those photos all over the internet would probably be pointless.  If I ever accidently do something to make Daddy proud, though, I'll give you his email and you can send them to him directly."
        wt_image current_location.image
    else:
        if fairyn.in_area('club'):
            wt_image ms2_club_1_2
        call expandable_menu(fairyn_talk_menu) from _call_expandable_menu_32
    return

label fairyn_talk_nothing:
    if fairyn.in_area('club'):
        wt_image ms2_club_1_3
    "The two of you have nothing to talk about right now."
    wt_image current_location.image
    return

label fairyn_talk_photos:
    if fairyn.in_area('club'):
        wt_image ms2_club_1_5
    fairyn.c "It does sort of turn me on knowing that you could send those photos to someone I care about and embarass me."
    if fairyn.in_area('club'):
        wt_image ms2_club_1_3
    fairyn.c "It's almost enough to make me wish I had someone in my life I truly cared about."
    wt_image current_location.image
    return

label fairyn_talk_bj_training:
    if fairyn.bj_training_status == 6:
        if fairyn.in_area('club'):
            wt_image ms2_club_1_2
        player.c "Have you been pracising what I taught you?"
        if fairyn.has_tag('girlfriend_bj'):
            fairyn.c "Have I tried to trick some poor boy into thinking I'm the sort of girl who could care about him?  Sorry, not yet.  I'm still working up to that level of bitchy-ness."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_1
            player.c "If you dropped your guard for a few minutes, you might find you have more to give to a relationship than you give yourself credit for."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_3
            fairyn.c "Oh, I have lots of things I can give to a relationship.  The problem is, they come with me, and I'm not mean enough to inflict that on anyone."
        elif fairyn.has_tag('submissive_bj'):
            fairyn.c "Nope, I haven't been in that type of mood for a while."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_1
            player.c "You don't need to be a in a 'mood' to give up power to a man, Fairyn.  Just admit to yourself that you'd be happy as someone's submissive."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_3
            fairyn.c "Sorry, 'someone'.  M's offered to make me part of his harem, too.  Considering I can say 'no' to both of you, maybe you should re-think your idea that I need a Dom in my life?"
        else:
            if fairyn.in_area('club'):
                wt_image ms2_club_1_5
            fairyn.c "Uh huh.  I can still taste the guy who gave me a lift to the Club."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_2
            fairyn.c "I could have driven myself, but it was more fun to 'pay' for the ride."
            player.c "You really should let me turn you professional.  You could donate your earnings to charity."
            if fairyn.in_area('club'):
                wt_image ms2_club_1_3
            fairyn.c "You want me to make my own money and support good causes, too?  You really don't get this path of self-destruction I'm on, do you?"
    elif fairyn.bj_training_status == 5:
        if fairyn.in_area('club'):
            wt_image ms2_club_1_4
        fairyn.c "Did you get a kick out of that?  Getting me to pay you to teach me how to suck dick and then refusing to train me?"
        if fairyn.in_area('club'):
            wt_image ms2_club_1_2
        player.c "Did you get a kick out of being reminded that I'm completely uninterested in having your mouth around my cock?"
        if fairyn.in_area('club'):
            wt_image ms2_club_1_5
        fairyn.c "Maybe"
    elif fairyn.bj_training_status > 0:
        if fairyn.in_area('club'):
            wt_image ms2_club_1_2
        player.c "When you're ready to learn how to suck cock properly, let me know."
        if fairyn.in_area('club'):
            wt_image ms2_club_1_4
        fairyn.c "I've wasted Daddy's money on a lot of stupid things, but you can't possibly believe that I'd pay you to hear how you like your dick pleasured?"
        if fairyn.in_area('club'):
            wt_image ms2_club_1_2
        player.c "I think you want to be better at sex than you are.  I'm giving you the chance to spend your father's money on something useful for a change."
        if fairyn.in_area('club'):
            wt_image ms2_club_1_3
        fairyn.c "You have a lot of fucking gall."
    wt_image current_location.image
    return

label fairyn_talk_art_show:
    add tags 'discussed_art_show_with_you' to fairyn
    if fairyn.in_area('club'):
        wt_image ms2_club_1_4
    player.c "The art show, that's where I know you from.  You're the painted woman in the gallery.  What's up with that?"
    if fairyn.in_area('club'):
        wt_image ms2_club_1_5
    fairyn.c "Hmmm, let's see.  Sometimes I like to be put on a pedestal, sometimes I like to be objectified.  When I appear in the art show, I get both at the same time.  Plus total strangers do weird sexual things to me without asking my name.  What's not to love?"
    if fairyn.in_area('club'):
        wt_image ms2_club_1_3
    fairyn.c "Oh and Daddy told me my art career would never amount to anything because no one would ever come to a gallery to look at my work.  Guess I showed him!"
    wt_image current_location.image
    return

# Hypno Actions
label master_m_hypnosis_start:
    "This hypnosis action shouldn't be available right now."
    $ ignore_context_change = True
    return

label diamond_hypnosis_start:
    "This hypnosis action shouldn't be available right now."
    $ ignore_context_change = True
    return

label fairyn_hypnosis_start:
    "This hypnosis action shouldn't be available right now."
    $ ignore_context_change = True
    return

## Character Specific Actions
# Introduce Yourself
label master_m_introduce:
  wt_image master_m.image
  if diamond.training_result == 2:
    "Turns out the man is Master M, and he's not interested in talking to you."
  elif diamond.training_result == 6 or diamond.training_result == 8:
    # if master_m.encounter_possible == 1: # redundant
    "Turns out the man is Master M."
    master_m.c "It's nice to meet you in person. Great job with Diamond."
    "He shakes your hand."
    $ master_m.encounter_possible = 2
  else:
    #if master_m.encounter_possible == 1: # redundant
    "Turns out the man is Master M."
    master_m.c "It's nice to meet you in person."
    "He's cordial, but not interested in chatting."
    $ master_m.encounter_possible = 2
  $ master_m.name = "Master M"
  rem tags 'first_visit' from master_m
  return

# Watch Her Dance
label diamond_watch_dance:
    $ diamond.training_session()
    $ diamond.strip_count += 1
    wt_image ms1_stripper_5
    "Diamond steels herself, then starts her routine."
    wt_image ms1_stripper_1
    "She looks at the floor as she dances and fake-fucks the stripping pole. She's embarrassed to be here and to be making this spectacle of herself. It's no wonder M uses this as punishment."
    if diamond.strip_count > 1 and not diamond.has_tag('lesbian_strip_at_club') and not diamond.has_tag('likes_girls'):
        add tags 'lesbian_strip_at_club' to diamond
        wt_image ms1_stripper_18
        "Diamond pauses as she sees another woman approach the stage."
        wt_image ms1_stripper_19
        diamond.c "I'm not allowed to touch or be touched today.  I'm just here to take my clothes off."
        club_patron_12 "That's not quite true, is it slave?  M tells me you're not allowed to touch or be touched by men."
        wt_image ms1_stripper_20
        club_patron_12 "Don't worry.  I'm not going to touch you.  Not even to punish you, although you do deserve a spanking for trying to mislead me.  You are, however, going to touch me."
        wt_image ms1_stripper_19
        diamond.c "Ma'am, please?  That's not something I ..."
        club_patron_12 "Do without complaining?  No, so I've heard from M.  Do you know why you're going to pleasure me here, on this stage, with everyone watching?"
        wt_image ms1_stripper_20
        diamond.c "No, Ma'am."
        club_patron_12 "To show the women of this club that despite your reluctance, you are available to them.  And to show M that you're an obedient slavegirl who'll serve all his friends, not just the ones you feel like serving."
        wt_image ms1_stripper_21
        club_patron_12 "Do we have an understanding, girl?  or do I need to reconsider my decision not to spank you?"
        diamond.c "I understand, Ma'am.  I'll do as I'm told.  For M."
        wt_image ms1_stripper_22
        club_patron_12 "It's a just a nipple.  You don't need to crinkle your nose up.  You can save that for when you're licking my wet, smelly cunt."
        wt_image ms1_stripper_23
        club_patron_12 "You are going to show M and all the women in the Club how wet you can make my cunt, aren't you?"
        wt_image ms1_stripper_24
        diamond.c "Yes, Ma'am."
        wt_image ms1_stripper_25
        club_patron_12 "Not like that.  No one can see what you're doing.  Turn around."
        wt_image ms1_stripper_26
        diamond.c "Yes, Ma'am."
        wt_image ms1_stripper_27
        club_patron_12 "Stay still and no squirming.  I'll let you know when you can make me cum."
        wt_image ms1_stripper_28
        "The dominant woman rides Diamond's face while giving the audience a clear view of her steadily moistening snatch.  She doesn't keep them in that position an overly long time, but it feels like an eterniity to the humiliated slavegirl ..."
        wt_image ms1_stripper_29
        "... before the Club member lies down and allows Diamond to finish her off to a round of applause."
        club_patron_12 "mmmmmm .... yessss!!!"
        wt_image ms1_stripper_30
        "The show is over, but Diamond is required to dress the Club member while listening to her critique her technique with M."
        club_patron_12 "You could see she was obedient enough, after I brought her in line.  Her oral skills leave a lot to be desired, though.  She could really use more practice licking cunt."
        master_m.c "Thank you for the feedback.  I'll take it under advisement."
        $ diamond.lesbian_training += 1
    else:
        wt_image ms1_stripper_6
        "She keeps her eyes down, still not meeting the gaze of the audience as she lowers her top."
        wt_image ms1_stripper_7
        "She may not want to be doing this, but she's a lithe little dancer..."
        wt_image ms1_stripper_8
        "...and eye contact or no, the audience enjoys watching her take her clothes off."
        wt_image ms1_stripper_17
        "Despite her petite frame, she has a nice booty and she's good at shaking it."
        wt_image ms1_stripper_9
        "And she's actually one of the better dancers at making use of the pole."
        wt_image ms1_stripper_10
        "She's athletic enough to pull herself right to the top ..."
        wt_image ms1_stripper_11
        "...and she seems to enjoy herself just a little as she spins down, a small smile crossing her face."
        wt_image ms1_stripper_13
        "When she reaches the bottom, she goes back to being shy ..."
        wt_image ms1_stripper_12
        "... or at least as shy as a woman can be who's displaying her attributes to a room full of strangers."
        wt_image ms1_stripper_14
        "She leaves the stage to a round of applause, hastily re-dressing herself as she goes, her punishment now complete."
    change player energy by -energy_very_short notify
    return

# Ask For A Private Show
label diamond_private_show:
    $ diamond.training_session()
    wt_image ms1_stripper_15
    player.c "If you're here to take your clothes off, does that include private shows?"
    "She sighs and lowers her top."
    wt_image ms1_stripper_3
    diamond.c "I'm not allowed to go into a private room, but yes, I'm to take my clothes off in front of anyone who asks."
    player.c "Are you supposed to show everything?"
    wt_image ms1_stripper_4
    diamond.c "Yes. And I'm supposed to make myself wet to improve the view for you. But I'm not allowed to cum."
    wt_image ms1_stripper_16
    "You spend a few minutes watching the petite slavegirl finger herself for your amusement and her punishment, then move on."
    return

# See What She Is Up To
label fairyn_see_what_up_to:
  $ fairyn.training_session()
  wt_image ms2_club_maid_1_1
  "Fairyn the Trust Fund Baby seems to have her eye on one of the maids assigned to clean the Club. She's ignoring everyone else, including you. You watch her to see what she's up to."
  wt_image ms2_club_maid_1_2
  "Fairyn gets up and makes her way to where the maid is cleaning, standing close behind her and placing her hand on the maid's."
  wt_image ms2_club_maid_1_3
  "Taking the maid by the hand, Fairyn turns her around ..."
  wt_image ms2_club_maid_1_4
  "... and pulls down her top."
  wt_image ms2_club_maid_1_13
  $ title = "Keep watching?"
  menu:
    "Watch the show":
      wt_image ms2_club_maid_1_14
      "Fairyn seems to be in rather a different mood than she was when she visited you."
      wt_image ms2_club_maid_1_5
      "The maid is soon stripped..."
      wt_image ms2_club_maid_1_6
      "... and put to work undressing Fairyn"
      wt_image ms2_club_maid_1_7
      "Then Fairyn leads the maid to the sofa ..."
      wt_image ms2_club_maid_1_8
      "... where she's exposed ..."
      wt_image ms2_club_maid_1_9
      "... probed ..."
      wt_image ms2_club_maid_1_15
      "... and put back to work ..."
      wt_image ms2_club_maid_1_10
      "... this time in a more personal cleaning capacity."
      wt_image ms2_club_maid_1_12
      "For a brief moment, just before she shudders to climax ..."
      wt_image ms2_club_maid_1_17
      "... Fairyn catches your eye across the room, and sees you watching her."
      wt_image ms2_club_maid_1_16
      "Then returns her attention to the sensations inspired by the woman between her legs."
      wt_image ms2_club_maid_1_17
      fairyn.c "ooohhhhh"
      wt_image ms2_club_maid_1_18
      "Even with one orgasm complete, Fairyn seems to be in no mood to let the maid return to her dusting."
      wt_image ms2_club_maid_1_19
      "You can see her providing instructions, and while you can't quite overhear what she's saying, it seems to involve the maid paying closer attention to Fairyn's orgasm-engorged clit."
      wt_image ms2_club_maid_1_20
      "The maid may be here a bit, and you've already watched Fairyn enjoy one orgasm.  Time to go on with the rest of your day."
      rem tags 'in_club_now' from fairyn
      call character_location_return(fairyn) from _call_character_location_return_199
      wt_image club.image
      change player energy by -energy_very_short notify
    "Go on with your day":
      rem tags 'in_club_now' from fairyn
      call character_location_return(fairyn) from _call_character_location_return_200
      wt_image club.image
      "You leave Fairyn to her fun."
  $ master_m.ms1_ms2_joint_event = 1
  add tags 'club_maid_event_happened' to fairyn
  return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
label fairyn_contact:
  ## Invite Fairyn and Diamond Over
  $ diamond.training_session()
  $ fairyn.training_session()
  $ master_m.ms1_ms2_joint_event = 5
  $ diamond.location = living_room
  $ fairyn.location = living_room
  "Fairyn doesn't work and isn't out shopping when you contact her, and Diamond's only responsibility this week is to obey Fairyn, so the two of them are available to come right over as soon as you call."
  wt_image ms1_ms2_joint_event_2_1
  "Fairyn wastes no time on pleasantries when they get there. She whispers seductively to you as she holds Diamond close."
  fairyn.c "So, what do want us to do?"
  $ title = "What do you want?"
  menu menu_fairyn_joint_main:
    "Ask Fairyn what she hoped would happen" if not diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_hoped'):
      fairyn.c "Mmmmm. I was hoping you'd fuck Diamond in the ass, so I could tease her about what an ass whore she is and about how horny and submissive it makes her feel when she has a big, fat cock up her butt."
      add tags 'joint_hoped' to fairyn
      $ title = "What do you want?"
      jump menu_fairyn_joint_main
    "Ask Diamond what she hoped would happen" if not diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_hoped'):
      diamond.c "Fairyn's been bossing me around all week. What I'd really love is if you'd turn the tables and let me spank and dominate her while you watch."
      add tags 'joint_hoped' to diamond
      $ title = "What do you want?"
      jump menu_fairyn_joint_main
    "Ask both of them what they're hoping for" if not diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_hoped'):
      fairyn.c "Mmmmm. I was hoping you'd fuck Diamond in the ass, so I could tease her about what an ass whore she is and about how horny and submissive it makes her feel when she has a big, fat cock up her butt."
      player.c "What about you, [diamond.training_name]? Is that what you were hoping would happen?"
      diamond.c "Fairyn's been bossing me around all week. What I'd really love is if you'd turn the tables and let me spank and dominate her while you watch."
      add tags 'joint_hoped' to diamond
      add tags 'joint_hoped' to fairyn
      $ title = "What do you want?"
      jump menu_fairyn_joint_main
    "Tell them to serve you" if not fairyn.has_tag('joint_fuck_each_other'):
      player.c "Remove your clothes.  Both of you."
      wt_image ms1_ms2_joint_event_2_5
      "They strip, then look at you, awaiting further instructions."
      $ title = "What next?"
      menu menu_fairyn_joint_serve:
        "Pleasure themselves" if not fairyn.has_tag('joint_pleasure') and not fairyn.has_tag('joint_display'):
          player.c "Pleasure yourselves."
          wt_image ms1_ms2_joint_event_2_4
          "The two women look at each other, Diamond a little nervously, Fairyn much more excited at the prospect of what's to come."
          wt_image ms1_ms2_joint_event_2_6
          "They take turns licking nipples ..."
          wt_image ms1_ms2_joint_event_1_34
          "... and then make out, with Fairyn taking the lead."
          add tags 'joint_pleasure' to fairyn
          $ title = "Now what?"
          jump menu_fairyn_joint_serve
        "Fuck each other" if fairyn.has_tag('joint_pleasure') and not fairyn.has_tag('joint_fuck_each_other'):
          player.c "Fuck yourselves while I watch."
          wt_image ms1_ms2_joint_event_1_24
          fairyn.c "You heard the man, my subbie heterosexual friend. I don't suppose that excites you at all? I haven't let you cum this week, which is totally bitchy of me."
          wt_image ms1_ms2_joint_event_1_28
          fairyn.c "Are you going to hate this, or maybe that submissive brain of yours has become so turned on from being forced to service me that your clit is all hot and throbbing?"
          wt_image ms1_ms2_joint_event_1_29
          "Fairyn presses her lips against Diamond's as she grinds her hips into her. It's hard to tell with their lips locked like this, but you're pretty sure the moans you're hearing are from the both of them."
          fairyn.c "mmmmmm"
          diamond.c "nnnnnnnn"
          wt_image ms1_ms2_joint_event_1_30
          "Suddenly, Diamond shudders from head to toe. Fairyn breaks the kiss to look at her."
          diamond.c "Ooooohhh!!"
          wt_image ms1_ms2_joint_event_1_31
          fairyn.c "You slut!!  You just humped yourself to orgasm against my leg! I'm never going to believe you again when you say 'you just want to hang out and chat and I should keep it in my pants 'til M wants to see us together.''"
          wt_image ms1_ms2_joint_event_1_52
          fairyn.c "Now lie there like a good subbie friend while I use you as my personal pussy rubbing post."
          wt_image ms1_ms2_joint_event_1_32
          "Fairyn leans in and kisses her as she thrusts her hips more and more insistently against Diamond's inner thigh."
          wt_image ms1_ms2_joint_event_1_33
          "A moment later, it's Fairyn's turn to orgasm. And if that isn't a second orgasm wracking Diamond's body, it's pretty close, although Fairyn is too caught up in her own climax to notice."
          fairyn.c "OOHHHH!!"
          diamond.c "Oooohhhh!"
          wt_image ms1_ms2_joint_event_1_24
          "Fairyn gloats as the two of them recover from their orgasms."
          fairyn.c "Now that I know how easily I can get you off, you are in for a world of trouble, my friend."
          wt_image ms1_ms2_joint_event_1_14
          "She addresses you briefly before returning her attention to a contemplation of what new games she can play with Diamond."
          fairyn.c "That was fun. I hope you enjoyed the show."
          add tags 'joint_fuck_each_other' to fairyn
          $ title = "Anything else?"
          jump menu_fairyn_joint_main
        "Display themselves" if not fairyn.has_tag('joint_display'):
          player.c "Show me what the two of you have to offer."
          wt_image ms1_ms2_joint_event_2_7
          "Fairyn straddles Diamond, who spreads herself and Fairyn open for you to contemplate your options."
          add tags 'joint_display' to fairyn
          $ title = "What do you choose?"
          jump menu_fairyn_joint_serve
        "Fuck Diamond" if fairyn.has_tag('joint_display'):
          player.c "Lie down, [diamond.training_name].  I'm going to fuck you."
          wt_image ms1_ms2_joint_event_1_14
          fairyn.c "Put it in her ass, please?? She hates that, but it makes her all tingly subbie. Please split her ass wide open with that big cock of yours."
          "It's couched as a request, but you're not entirely certain Fairyn isn't going to insist."
          $ title = "Continue?"
          menu:
            "Yes, fuck Diamond's ass":
              wt_image ms1_ms2_joint_event_1_24
              player.c "You heard your Mistress, [diamond.training_name]. Lie down. I'm going to fuck you in the ass."
              fairyn.c "Such a soft, cute ass you have, Diamond.  I can't wait to see him him split it in two with that big jackhammer of his."
              call fairyn_joint_fuck_diamond_ass from _call_fairyn_joint_fuck_diamond_ass
            "Have them blow you":
              call fairyn_joint_have_them_blow_you from _call_fairyn_joint_have_them_blow_you
        "Fuck Fairyn" if fairyn.has_tag('joint_display'):
          player.c "Lie down, Fairyn.  I'm going to fuck you."
          wt_image ms1_ms2_joint_event_2_4
          diamond.c "Could I make a suggestion? Stick it in her ass. She's been teasing me about making me her ass whore, but I think she's the one who should be taking a dick up her butt."
          diamond.c "She likes it in her pussy. I bet you'll have a lot more fun putting it where she won't like it so much."
          "She's probably right."
          $ title = "Continue?"
          menu:
            "Yes, fuck Fairyn's ass":
              player.c "You heard her. Lie down. I'm going to fuck your ass."
              "Diamond grins."
              diamond.c "Look who's going to be the ass whore now! He's going to split your butt in two with that big cock of his. I can't wait to see your face when he shoves himself inside you."
              call fairyn_joint_fuck_fairyn_ass from _call_fairyn_joint_fuck_fairyn_ass
            "Have them blow you":
              call fairyn_joint_have_them_blow_you from _call_fairyn_joint_have_them_blow_you_1
        "Have them blow you" if fairyn.has_tag('joint_display'):
          call fairyn_joint_have_them_blow_you from _call_fairyn_joint_have_them_blow_you_2
    "Tell them to make out" if not fairyn.has_tag('joint_fuck_each_other'):
      player.c "What I want is to watch the two of you make out with each other."
      wt_image ms1_ms2_joint_event_2_2
      "Fairyn seems pleased with your selection. Diamond less so, but she gamely obeys and offers her mouth and tongue to receive Fairyn's kiss."
      wt_image ms1_ms2_joint_event_2_3
      "The two of them undress each other, making sure to give you a good view as they do."
      wt_image ms1_ms2_joint_event_2_4
      fairyn.c "You realize, this means your tongue is going back inside my pussy."
      diamond.c "Are you sure? I thought it meant your tongue was going into my pussy for a change."
      $ title = "Which is it?"
      menu:
        "Diamond to eat out Fairyn":
          player.c "Fairyn's right, [diamond.training_name]. I understand you need practice pleasuring women. No time like the present to gain experience."
          wt_image ms1_ms2_joint_event_1_7
          "Fairyn lies down and spreads her legs."
          fairyn.c "Don't pout, Diamond. You know he's doing this for your own good. Start with my tits. Make my nipples rock hard before you lick my pussy."
          wt_image ms1_ms2_joint_event_1_8
          fairyn.c "Mmmmm. That has my juices flowing."
          fairyn.c "Be a good subbie friend and work your way down to the pool of wetness you've made between my legs."
          wt_image ms1_ms2_joint_event_1_9
          "Diamond kisses her way down Fairyn's belly."
          wt_image ms1_ms2_joint_event_1_10
          fairyn.c "Look at it, Diamond. See how swollen and wet my sex is? After M takes you back and I can no longer tell you what to do, I hope you'll remember what effect you have on me."
          fairyn.c "When we go shopping together and I tell you how horny I am because I haven't been fucked in ages, I hope you'll be a good friend and offer yourself to me.  As long as M hasn't told you you can't, that is. And he wouldn't do that, would he?"
          "Diamond shakes her head slowly..."
          wt_image ms1_ms2_joint_event_1_11
          "... kisses her friend softly on the inner thigh ..."
          wt_image ms1_ms2_joint_event_1_12
          "... then gets to work providing relief to Fairyn's swollen and wet sex ..."
          fairyn.c "oooooo"
          wt_image ms1_ms2_joint_event_1_13
          "... something she's more clearly more skilled at than you've been led to believe."
          fairyn.c "ooooo ...  OOHHHH!!"
          wt_image ms1_ms2_joint_event_1_14
          fairyn.c "Mmmmm. That was nice. That's enough fun for me, but Diamond will suck you off before we go, if you want?"
          $ title = "Do you want a blow job from Diamond?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck
            "You want Fairyn to suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_very_short notify
        "Fairyn to eat out Diamond":
          player.c "[diamond.training_name]'s right, Fairyn. Her tongue's been getting enough of a work out. Fair's fair."
          wt_image ms1_ms2_joint_event_1_46
          fairyn.c "Oh, okay. I suppose it has been a bit bitchy of me not to let you have at least one orgasm this week."
          wt_image ms1_ms2_joint_event_1_18
          fairyn.c "And it is kind of cute how hard your nipples get when I play with them, especially considering you swear you don't like girls."
          wt_image ms1_ms2_joint_event_1_19
          fairyn.c "I suppose since you don't enjoy sex with women, I'm going to have to work twice as hard to get you off as you have to work to get me off."
          wt_image ms1_ms2_joint_event_1_51
          fairyn.c "Or maybe that submissive brain of yours has become so turned on from being forced to service me that you're ready to cum from the first touch of any sort on your hot, throbbing clit?"
          wt_image ms1_ms2_joint_event_1_21
          "From the sounds Diamond emits as Fairyn's tongue touches her, it's closer to the latter."
          diamond.c "oohhh"
          wt_image ms1_ms2_joint_event_1_22
          fairyn.c "You slut!! You're totally soaked! I'm never going to believe you again when you say you just want to hang out and chat and I should keep it in my pants 'til M wants to see us together."
          wt_image ms1_ms2_joint_event_1_21
          "As if to punctuate her point, Fairyn buries her tongue in Diamond's pussy, quickly bringing M's slavegirl to orgasm."
          wt_image ms1_ms2_joint_event_1_23
          diamond.c "oohhhh ... Oooooohhhh!"
          wt_image ms1_ms2_joint_event_1_24
          "Fairyn gloats as Diamond recovers from her orgasm."
          fairyn.c "Now that I know how easily I can get you off, you are in for a world of trouble, my friend."
          wt_image ms1_ms2_joint_event_1_14
          "She addresses you briefly before returning her attention to a contemplation of what new games she can play with Diamond."
          fairyn.c "That was fun. I hope you enjoyed the show."
          $ title = "Anything else?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_1
            "Yes, have Fairyn suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_1
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_very_short notify
        "They're both right":
          player.c "You're both right."
          fairyn.c "Hmmm. This'll be fun. Since you're the heterosexual one, you go first."
          diamond.c "How does that make sense?"
          fairyn.c "We both know you can get me off quickly, but since you don't like girls, I'm going to have to work a lot harder. I want to be relaxed and feeling good while I'm trying to get you off, so make this a good orgasm."
          wt_image ms1_ms2_joint_event_1_7
          "Fairyn spreads her legs and Diamond kneels between them, a position she's become used to this week."
          wt_image ms1_ms2_joint_event_1_10
          fairyn.c "See? I'm already wet and you haven't even touched me yet. After M takes you back and I can no longer tell you what to do, I hope you'll remember what effect you have on me."
          fairyn.c "When we go shopping together and I tell you how horny I am because I haven't been fucked in ages, I hope you'll be a good friend and offer yourself to me. As long as M hasn't told you you can't, that is. And he wouldn't do that, would he?"
          "Diamond shakes her head slowly..."
          wt_image ms1_ms2_joint_event_1_11
          "... kisses her friend softly on the inner thigh ..."
          wt_image ms1_ms2_joint_event_1_12
          "... then gets to work providing relief to Fairyn's swollen and wet sex..."
          fairyn.c "oooooo"
          wt_image ms1_ms2_joint_event_1_13
          "... something she's more clearly more skilled at than you've been led to believe."
          fairyn.c "ooooo ... OOHHHH!!"
          wt_image ms1_ms2_joint_event_1_46
          fairyn.c "My turn."
          wt_image ms1_ms2_joint_event_1_18
          fairyn.c "Oh, that's so cute! Feel how hard your nipples get when I play with them? And you swear you don't like girls."
          wt_image ms1_ms2_joint_event_1_19
          fairyn.c "I know I haven't let you cum this week, which is totally bitchy of me, but are you sure you aren't at least a little turned on by my body?"
          wt_image ms1_ms2_joint_event_1_20
          fairyn.c "Or is it just that that submissive brain of yours has become so turned on from being forced to service me that you're ready to cum from the first touch of any sort on your hot, throbbing clit?"
          wt_image ms1_ms2_joint_event_1_22
          fairyn.c "You slut!! You're totally soaked! I'm never going to believe you again when you say you just want to hang out and chat and I should keep it in my pants 'til M wants to see us together."
          wt_image ms1_ms2_joint_event_1_23
          "As if to punctuate her point, Fairyn buries her tongue in Diamond's pussy, quickly bringing M's slavegirl to orgasm."
          diamond.c "oohhhh ... Oooooohhhh!"
          wt_image ms1_ms2_joint_event_1_24
          "Fairyn gloats as Diamond recovers from her orgasm."
          fairyn.c "Now that I know how easily I can get you off, you are in for a world of trouble, my friend."
          wt_image ms1_ms2_joint_event_1_14
          "She addresses you briefly before returning her attention to a contemplation of what new games she can play with Diamond."
          fairyn.c "That was fun. I hope you enjoyed the show."
          $ diamond.orgasm_count += 1
          $ fairyn.orgasm_count += 1
          $ title = "Anything else?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_2
            "Yes, have Fairyn suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_2
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_short notify
        "Neither, have them grind together instead":
          player.c "Wrong on both counts. I want to watch the two of you grind yourselves against each other."
          wt_image ms1_ms2_joint_event_1_46
          fairyn.c "Mmmmm. Hear that, my heterosexual friend? You're going to be pressed firmly against my body while I grind myself to orgasm on you. I don't suppose that excites you at all?"
          wt_image ms1_ms2_joint_event_1_24
          fairyn.c "I haven't let you cum this week, which is totally bitchy of me. Considering you asked for my tongue, I'm guessing that submissive brain of yours has become so turned on from being forced to service me that your clit is all hot and throbbing?"
          wt_image ms1_ms2_joint_event_1_28
          fairyn.c "Do you think my thigh pressed against it will feel as nice as my tongue would have?"
          wt_image ms1_ms2_joint_event_1_29
          "Fairyn presses her lips against Diamond's as she begins to grind her hips into her. It's hard to tell with their lips locked like this, but you're pretty sure the moans you're hearing are from the both of them."
          fairyn.c "mmmmmm"
          diamond.c "nnnnnnnn"
          wt_image ms1_ms2_joint_event_1_30
          "Suddenly, Diamond shudders from head to toe. Fairyn breaks the kiss to look at her."
          diamond.c "Ooooohhh!!"
          wt_image ms1_ms2_joint_event_1_31
          fairyn.c "You slut!! You just humped yourself to orgasm against my leg! I'm never going to believe you again when you say 'you just want to hang out and chat and I should keep it in my pants 'til M wants to see us together'."
          wt_image ms1_ms2_joint_event_1_52
          fairyn.c "Now lie there like a good subbie friend while I use you as my personal pussy-rubbing post."
          wt_image ms1_ms2_joint_event_1_32
          "Fairyn leans in and kisses her as she thrusts her hips more and more insistently against Diamond's inner thighs."
          wt_image ms1_ms2_joint_event_1_33
          "A moment later, it's Fairyn's turn to orgasm. And if that isn't a second orgasm wracking Diamond's body, it's pretty close, although Fairyn is too caught up in her own climax to notice."
          fairyn.c "OOHHHH!!"
          diamond.c "Oooohhhh!"
          wt_image ms1_ms2_joint_event_1_24
          "Fairyn gloats as the two of them recover from their orgasms."
          fairyn.c "Now that I know how easily I can get you off, you are in for a world of trouble, my friend."
          wt_image ms1_ms2_joint_event_1_14
          "She addresses you briefly before returning her attention to a contemplation of what new games she can play with Diamond."
          fairyn.c "That was fun. I hope you enjoyed the show."
          $ title = "Anything else?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_3
            "Yes, have Fairyn suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_3
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_very_short notify
    "Fuck Diamond in the ass" if fairyn.has_tag('joint_hoped') and not fairyn.has_tag('joint_fuck_each_other'):
      player.c "You heard your Mistress, [diamond.training_name]. Strip and lie down. I'm going to fuck you in the ass."
      wt_image ms1_ms2_joint_event_2_3
      "To your surprise, Fairyn not only helps Diamond undress, she also strips herself, all the while missing no opportunity to tease Master M's slave girl."
      fairyn.c "Such a soft, cute ass you have, Diamond. I can't wait to see him him split it in two with that big jackhammer of his."
      call fairyn_joint_fuck_diamond_ass from _call_fairyn_joint_fuck_diamond_ass_1
    "Fuck Fairyn in the ass" if fairyn.has_tag('joint_hoped') and not fairyn.has_tag('joint_fuck_each_other'):
      player.c "I have a better idea.  I'm going to fuck you in the ass, Fairyn."
      wt_image ms1_ms2_joint_event_2_11
      "Diamond grins."
      diamond.c "Look who's going to be the ass whore now!"
      player.c "Strip"
      wt_image ms1_ms2_joint_event_2_4
      "You meant Fairyn, but don't object when Diamond misunderstands and disrobes, too. That doesn't prevent her from having fun teasing her Mistress-for-the-week."
      diamond.c "He's going to split your butt in two with that big cock of his. I can't wait to see your face when he shoves himself inside you."
      call fairyn_joint_fuck_fairyn_ass from _call_fairyn_joint_fuck_fairyn_ass_1
    "Tell Diamond to dominate Fairyn" if diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_fuck_each_other'):
      player.c "I didn't realize you were a switch, [diamond.training_name]."
      diamond.c "I'm not. Not usually, anyway. I'm not normally made to serve a friend, either. Especially one who's been taking great pleasure out of making me do things she likes that she knows I don't."
      player.c "You realize once you leave here, she's still going to have control over you for the rest of the week."
      diamond.c "I'll take my chances."
      player.c "Fairyn, you asked me what I want the two of you to do. I think giving her a turn is only fair play. You've been having your fun with your friend. Time for her to have some fun with you."
      fairyn.c "I'm not sure I'm going to like this."
      wt_image ms1_ms2_joint_event_2_11
      diamond.c "I'm going to do everything I can to make sure you don't. You're my bitch now. What do you think of that? Your subbie friend is taking charge. Lie across my lap, and be quick about it."
      wt_image ms1_ms2_joint_event_2_20
      "This wasn't what Fairyn had in mind, and she clearly has some doubts about this turn of events, but she's curious to see where this going to go. No doubt this is a side of Diamond she hasn't seen before."
      fairyn.c "You're seriously going to spank me?? I haven't punished you once."
      diamond.c "No, you've just made me lick your pussy every time some erotic thought pops into your head, which is like always. You're like a total nymphomaniac. Maybe I can spank that out of you?"
      "You seriously doubt that's possible, but Diamond seems determined to give it a good go.  She tattoos Fairyn's ass with some force."
      "*smack*"
      wt_image ms1_ms2_joint_event_2_21
      fairyn.c "OWW!!"
      "*smack*"
      fairyn.c "OOWWW!!"
      "*smack*"
      wt_image ms1_ms2_joint_event_2_20
      fairyn.c "OOWWW!!! What the hell!!! Where did you learn to spank like that????"
      diamond.c "Do you have any idea how many spankings I've taken?"
      "*smack*"
      wt_image ms1_ms2_joint_event_2_21
      fairyn.c "OOWWW!!! I HAVEN'T! I'm not a full time slave."
      diamond.c "All the more reason to catch up on some much needed discipline."
      "*smack*"
      fairyn.c "OOOWWW!!! STOP!! PLEASE!!! I'LL DO WHATEVER YOU SAY!!"
      wt_image ms1_ms2_joint_event_2_20
      diamond.c "Damn straight you will. And I know damn well that the more humiliating the activity, the more you crave it."
      wt_image ms1_ms2_joint_event_2_22
      "Diamond slides Fairyn off her lap and begins to undress. Fairyn opens her own top, too."
      fairyn.c "I'm not really in that type of mood today, thanks, but if what you have in mind involves you being naked, I'm intrigued."
      wt_image ms1_ms2_joint_event_2_23
      diamond.c "You'll be in the mood for whatever I tell you to do, or you'll be back over my lap. Is that understood?"
      fairyn.c "Yes."
      diamond.c "No, no. It's 'yes, Mistress' to you."
      fairyn.c "Yes, Mistress."
      diamond.c "You're intrigued by my body, huh?"
      fairyn.c "You know I am, Mistress."
      diamond.c "Then I'm going to let you taste it."
      wt_image ms1_ms2_joint_event_2_24
      "Fairyn seems pleased by this development, until Diamond turns around."
      diamond.c "Only my ass, though. Get to work worshiping Mistress' booty."
      "Tentatively at first, then with increasing enthusiasm, Fairyn licks Diamond's ass. Every once in a while she glances over at you, as if to confirm that you're a witness to what she's being 'made' to do."
      wt_image ms1_ms2_joint_event_2_23
      "When she's fully relaxed and accepting of the job, Diamond turns up the intensity."
      diamond.c "That's enough of the outside of my ass. Get your tongue inside it now."
      wt_image ms1_ms2_joint_event_2_25
      "Trembling slightly, Fairyn inserts the tip of her tongue into her friend's butt."
      diamond.c "Deeper. Work it right in."
      "Diamond leans over, giving Fairyn better access. Placing both hands on Diamond's cheeks, Fairyn plunges in."
      diamond.c "Mmmmm. That's better. Tell me, what do you think you are, little miss trust fund baby? I mean, I'm a slave, but what are you? Is there a word for the type of woman who'll clean the asses of slaves with her tongue?"
      "There definitely should be such a word, but you're too focused on watching Fairyn humiliate herself to think one up."
      "For her part, Fairyn may not have been in the mood to be humiliated when she came here, but her friend seems to know her well enough to have triggered exactly that feeling in her. Blushing deeply, she buries herself between Diamond's nether cheeks and rims her friend with enthusiasm."
      wt_image ms1_ms2_joint_event_2_26
      "When she tires of this game, Diamond turns around and pushes her friend onto her back."
      diamond.c "Open your mouth. ... *sniff* ... I can smell my behind on you. You're going to be tasting that all day, even after you get control over me again."
      "Diamond looks up at you."
      diamond.c "I've had my fun, thanks. Do you want to use her before I release her? Her mouth stinks, but if you want, you can have it on your cock. Or better yet, why don't you fuck her ass and then have her blow you?"
      $ title = "Do you want to use Fairyn?"
      menu:
        "Yes, fuck Fairyn's ass":
          player.c "You heard her. Turn over. I'm going to fuck your ass."
          "Diamond grins."
          diamond.c "Look who's going to be the ass whore now!  He's going to split your butt in two with that big cock of his.  I can't wait to see your face when he shoves himself inside you."
          call fairyn_joint_fuck_fairyn_ass from _call_fairyn_joint_fuck_fairyn_ass_2
        "You want Fairyn to suck you off":
          call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_4
        "That's enough fun for you, too":
          "You thank the ladies for the show, and send them home."
          change player energy by -energy_very_short notify
    "Ask Diamond to dominate both of you" if diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_fuck_each_other'):
      player.c "I didn't realize you were a switch, [diamond.training_name]."
      diamond.c "I'm not. Not usually, anyway. I'm not normally made to serve a friend, either. Especially one who's been taking great pleasure out of making me do things she likes that she knows I don't."
      player.c "You realize once you leave here, she's still going to have control over you for the rest of the week."
      wt_image ms1_ms2_joint_event_2_11
      diamond.c "I'll take my chances."
      player.c "Will you Domme me, too?"
      diamond.c "Hmmm. Well, if I'm going to switch, why not?"
      wt_image ms1_ms2_joint_event_2_27
      diamond.c "Time to get undressed."
      "Mistress Diamond removes her outer clothes, then notices that Fairyn hasn't yet done so."
      diamond.c "I didn't just mean me. Strip!"
      "As she helps pull off Fairyn's clothes, she looks over at you."
      diamond.c "You, too! And be quick about it."
      wt_image ms1_ms2_joint_event_2_23
      diamond.c "Kneel. Both of you."
      "You get down on the floor and watch Mistress Diamond as she cups Fairyn under the chin."
      diamond.c "Looks like I need something to control two slow witted slaves."
      "She addresses you without looking at you."
      diamond.c "Go to your room and bring back two belts."
      $ title = "Obey Mistress Diamond?"
      menu menu_fairyn_joint_dom:
        "Yes, go get the belts":
          "You turn towards the bedroom."
          diamond.c "On your knees."
          wt_image belt_1
          "It takes a little while to get there and back on all fours, but eventually you return and hand the first belt to her."
          wt_image ms1_ms2_joint_event_2_29
          "Diamond wraps the belt around Fairyn's neck and pulls her to her feet as she turns back towards you."
          diamond.c "Now go get the second belt."
          wt_image ms1_ms2_joint_event_2_32
          "The second belt goes around your cock as she pulls you, too, to your feet."
          wt_image ms1_ms2_joint_event_2_31
          diamond.c "Fairyn was teasing me coming over here about making me her ass whore, but I think she's the one who should be taking a dick up her butt."
          wt_image ms1_ms2_joint_event_2_30
          diamond.c "She likes it in her pussy, but I bet she won't like it so much when you split her in half with this massive jack hammer."
          wt_image ms1_ms2_joint_event_2_31
          diamond.c "Don't you get any ideas, though. You don't get to cum in her ass. Give her a hard ass fucking, though, and I might let you cum in her mouth afterwards."
          wt_image ms1_ms2_joint_event_2_33
          "Tugging firmly on your belts, she leads you both over to the sofa."
          wt_image ms1_ms2_joint_event_2_12
          "Diamond positions Fairyn on her knees, then guides the head of your cock to her butt hole."
          diamond.c "Stick it in her."
          fairyn.c "Oh!"
          diamond.c "That's just the tip of his cock. You think that hurts? It's going to feel like he's ripped you a new one by the time he shoves the rest in."
          wt_image ms1_ms2_joint_event_2_13
          "Maybe not a new one, but a very, very full existing one as you push deeper and deeper inside her."
          fairyn.c "oohhh"
          "Fairyn tries to reach between her legs, but Diamond pulls Fairyn's legs shut, blocking access to her sex."
          diamond.c "Oh no you don't! No touching yourself. Ass whores take it up the butt without any other stimulation. If you're going to cum, you're going to cum from his cock in your ass only, ass whore."
          fairyn.c "oooohhh"
          "As much as her groans include an element of pleasure, it doesn't sound like she's going to cum, at least not anytime soon. You, on the other hand, are getting close, and Diamond senses it."
          diamond.c "Don't you dare let go! You don't get to cum until I say so, if I say so. Right now, your job is to ream her ass. Get at it."
          wt_image ms1_ms2_joint_event_2_14
          "It takes a lot of will power, but you do as she says, fucking Fairyn harder and harder as her ass stretches wider to accommodate you."
          fairyn.c "oooohhh"
          diamond.c "That's it. Make the ass whore groan."
          "She is, louder and louder. Perhaps Fairyn will get off from this after all."
          fairyn.c "oooohhh"
          wt_image ms1_ms2_joint_event_2_31
          diamond.c "That's enough."
          "Unceremoniously, Diamond pulls your cock out of Fairyn's ass while pulling her up off her knees. Fairyn groans again, this time in frustration, a feeling you can relate to."
          fairyn.c "argghh!!"
          diamond.c "Hear how frustrated the ass whore is? Hard to believe she's been the one having orgasms all week, while denying me. Well, turn about's fair play. This time she's the one who gets denied, while giving you an orgasm with her mouth."
          "That sounds good to you, especially as you were worried you were about to be blue balled."
          player.c "Yes, Mistress. Thank you, Mistress."
          wt_image ms1_ms2_joint_event_2_17
          "Tugging on Fairyn's belt once again, Diamond pulls her down onto her knees in front of you, and puts your cock in her mouth."
          diamond.c "Can you taste that? Can you taste your own ass on his cock? Give it a good cleaning, ass whore. Swallow your mess at the same time as you swallow his load."
          "That would be now, as you're unable to restrain your orgasm any longer."
          player.c "[player.orgasm_text]"
          $ fairyn.anal_count += 1
          $ fairyn.swallow_count += 1
          orgasm notify
          wt_image ms1_ms2_joint_event_1_16
          "After she finishes swallowing, Fairyn looks at you with a mischievous grin."
          fairyn.c "Mmmmm. Seems you liked that."
          $ title = "What do you tell her?"
          menu:
            "It was great":
              player.c "It was great. Thank you Mistress Diamond."
              wt_image ms1_ms2_joint_event_1_27
              diamond.c "You can drop the Mistress bit. I'm done switching. I had my fun."
              wt_image ms1_ms2_joint_event_1_16
              fairyn.c "That means it's back to my turn to be in charge."
              fairyn.c "Come on, Diamond, time for us to go. We should grab something to eat. I'm pretty full now, but you must be getting hungry."
            "The ass fucking was great":
              player.c "The ass fucking was great. Thank you, Mistress Diamond."
              wt_image ms1_ms2_joint_event_1_15
              fairyn.c "Drop the Mistress bit. That game's over. The ass fucking was great, and what, my blow job wasn't?"
              player.c "It was okay."
              wt_image ms1_ms2_joint_event_1_47
              fairyn.c "Okay?? I just sucked you off after you had your dick up my butt."
              call fairyn_joint_post_bj from _call_fairyn_joint_post_bj
        "No, disobey" if not fairyn.has_tag('joint_disobey'):
          player.c "No. I don't want to."
          wt_image ms1_ms2_joint_event_2_28
          "She steps over to where you're kneeling and leans down, placing her face close to yours."
          diamond.c "Listen, you ungrateful slug. I don't do brats and I don't let slaves dom from below."
          diamond.c "You asked me to Domme you. You're not going to manipulate me into punishing you when I don't feel like punishing you. Either do as I tell you, or we're leaving."
          add tags 'joint_disobey' to fairyn
          jump menu_fairyn_joint_dom
        "No, continue to disobey" if fairyn.has_tag('joint_disobey'):
          player.c "No, I don't want to."
          wt_image ms1_ms2_joint_event_2_1
          "Fairyn gets up and re-dresses."
          fairyn.c "Come on, Diamond. Don't waste your time. Let's go find a play partner who's more fun."
          wt_image current_location.image
          "The two of them leave."
          $ master_m.ms1_ms2_joint_event = 4
    "Tell Fairyn to dominate Diamond" if diamond.has_tag('joint_hoped') and not fairyn.has_tag('joint_fuck_each_other'):
      player.c "How about you show me how you control this slave, Fairyn."
      fairyn.c "This slave, also known as my friend? The cutely submissive and obedient Diamond, sworn follower of Master M who so wisely decided that she should spend the week under my loving ownership?"
      fairyn.c "She swears she doesn't like girls and has never agreed to play with me until M told her she had to, so that part's fun. Make my nipples hard, slave."
      wt_image ms1_ms2_joint_event_2_3
      "As Diamond fondles Fairyn's breast, Fairyn squeezes her ass."
      fairyn.c "She hasn't yet disobeyed me, so I haven't had to punish her. Do you think I should spank her, just for practice? In case she decides to disobey me later."
      $ title = "What do you think?"
      menu:
        "Watch Fairyn spank her":
          player.c "If you haven't spanked her, she's probably going through withdrawals. Master M punishes you regularly, doesn't he, [diamond.training_name]?"
          diamond.c "Yes"
          wt_image ms1_ms2_joint_event_1_24
          fairyn.c "Hmmm. I hadn't thought about that. You might start acting up just to earn a tail swatting. I'd better punish you before I inadvertently turn you into a brat and M gets mad at me."
          wt_image ms1_ms2_joint_event_1_19
          fairyn.c "Bend over so I have easy access."
          wt_image ms1_ms2_joint_event_1_39
          "*smack*"
          fairyn.c "Can you feel that?"
          wt_image ms1_ms2_joint_event_1_54
          diamond.c "Yes"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_19
          fairyn.c "Not as hard as M spanks you, is it?"
          diamond.c "It's okay."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_54
          fairyn.c "It's okay you like it, or it's okay you know I can't spank any harder?"
          diamond.c "Both"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_20
          fairyn.c "So you do like this?"
          diamond.c "Yes"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_19
          fairyn.c "Which means it's not really a punishment, is it?"
          diamond.c "A bit?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_37
          fairyn.c "I can't spank as hard as M..."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_38
          fairyn.c "... but I bet I can spank you longer."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_53
          fairyn.c "You know what they say about us girls and our endurance."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_38
          fairyn.c "How's your bum feeling now?"
          diamond.c "Warmer"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_37
          fairyn.c "Is that making you wet?"
          diamond.c "You know it is."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_53
          fairyn.c "Even though I'm a girl?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_38
          diamond.c "Apparently."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_53
          fairyn.c "Apparently I'm a girl, or apparently you get off on being spanked by a girl?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_37
          diamond.c "Ow! Apparently I can get off on being spanked by a girl."
          fairyn.c "No getting all the way off."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_38
          diamond.c "Ow!  Okay."
          fairyn.c "This is starting to hurt, isn't it?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_39
          diamond.c "Oww!  Yes!"
          fairyn.c "Is it the pain that gets you off?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_20
          diamond.c "Oww!  No."
          fairyn.c "The humiliation?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_39
          diamond.c "Oww!!  Probably."
          fairyn.c "Thank me for spanking you."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_19
          diamond.c "Oohhh ... thank you ... thank you for the spanking"
          fairyn.c "Tell me what you really want right now."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_54
          diamond.c "Oww!! I want ... I want you to do what you want with me."
          fairyn.c "You want me to have fun with you? Whether that's hurting you or making you eat me out?"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_39
          diamond.c "Owww!!  Yes!"
          fairyn.c "You know, I'm never going to believe you again when you say 'you just want to hang out and chat and I should keep it in my pants 'til M wants to see us together.'"
          "*smack*"
          wt_image ms1_ms2_joint_event_1_20
          diamond.c "Owww!!"
          fairyn.c "Now that I know how easily I can put you into subbie mode, you are in for a world of trouble, my friend.  Anytime I feel horny I may put you across my lap, and you know how often I get horny."
          "*smack*"
          wt_image ms1_ms2_joint_event_1_39
          diamond.c "Ooohhh"
          "That last sound was more moan of excitement than groan of pain. Fairyn notices, too, and stops the spanking.  Apparently she was serious about not letting Diamond get off."
          wt_image ms1_ms2_joint_event_1_46
          fairyn.c "After M takes you back and I can no longer tell you what to do, I hope you'll remember this."
          wt_image ms1_ms2_joint_event_1_24
          fairyn.c "When we go shopping together and I tell you how horny I am because I haven't been fucked in ages, I hope you'll be a good submissive friend and offer yourself to me. As long as M hasn't told you you can't, that is. And he wouldn't do that, would he?"
          "Diamond shakes her head slowly.  "
          wt_image ms1_ms2_joint_event_1_14
          "Fairyn addresses you briefly before returning her attention to a contemplation of what new games she can play with Diamond."
          fairyn.c "That was fun. I hope you enjoyed the show."
          $ title = "Anything else?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_4
            "You want Fairyn to suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_5
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_very_short notify
        "Watch Diamond pleasure Fairyn":
          player.c "She doesn't like playing with women, but she's been servicing your pussy whenever you tell her?"
          fairyn.c "She has."
          player.c "Perhaps you should give her an opportunity to do so again, in order to avoid a punishment?"
          wt_image ms1_ms2_joint_event_1_43
          "Fairyn lies down and spreads her legs."
          fairyn.c "Good idea. You heard the man. Don't think of this as an opportunity to get your mouth filled with my cum, my sweet subbie friend. Think of it as an opportunity to avoid a painful spanking."
          wt_image ms1_ms2_joint_event_1_7
          fairyn.c "Use your mouth to finish what your fingers started with my tits. Make my nipples rock hard before you lick my pussy."
          wt_image ms1_ms2_joint_event_1_8
          fairyn.c "Mmmmm. That has my juices flowing. Be a good subbie friend and work your way down to the pool of wetness you've made between my legs."
          wt_image ms1_ms2_joint_event_1_9
          "Diamond kisses her way down Fairyn's belly."
          wt_image ms1_ms2_joint_event_1_44
          fairyn.c "Look at it, Diamond. See how swollen and wet my sex is? After M takes you back and I can no longer tell you what to do, I hope you'll remember what effect you have on me."
          wt_image ms1_ms2_joint_event_1_45
          fairyn.c "When we go shopping together and I tell you how horny I am because I haven't been fucked in ages, I hope you'll be a good friend and offer yourself to me. As long as M hasn't told you you can't, that is. And he wouldn't do that, would he?"
          wt_image ms1_ms2_joint_event_1_10
          "Diamond shakes her head slowly ..."
          wt_image ms1_ms2_joint_event_1_11
          "... kisses her friend softly on the inner thigh ..."
          wt_image ms1_ms2_joint_event_1_12
          "... then gets to work providing relief to Fairyn's swollen and wet sex ..."
          fairyn.c "oooooo"
          wt_image ms1_ms2_joint_event_1_13
          "... something she's more clearly more skilled at than you've been led to believe."
          fairyn.c "ooooo ...  OOHHHH!!"
          wt_image ms1_ms2_joint_event_1_46
          fairyn.c "Mmmmm. That was nice."
          wt_image ms1_ms2_joint_event_1_14
          fairyn.c "That's enough fun for me, but Diamond will suck you off before we go, if you want?"
          $ fairyn.orgasm_count += 1
          $ title = "Do you want a blow job from Diamond?"
          menu:
            "Yes, have Diamond suck you off":
              call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_5
            "You want Fairyn to suck you off":
              call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_6
            "That's enough fun for you, too":
              "You thank the ladies for the show, and send them home."
              change player energy by -energy_very_short notify
    "Send them home" if not fairyn.has_tag('joint_fuck_each_other'):
      player.c "What I want is for the two of you to go home."
      fairyn.c "What? You just called us over."
      player.c "I know. And you showed up and I took a look at you and I don't feel like doing anything with you. You're dismissed."
      fairyn.c "Sheesh. And people call me flighty. Come on, Diamond, let's go find a play partner who's more fun."
      $ master_m.ms1_ms2_joint_event = 4
    "Yes, have Diamond suck you off" if fairyn.has_tag('joint_fuck_each_other'):
      call fairyn_joint_diamond_suck from _call_fairyn_joint_diamond_suck_6
    "Yes, have Fairyn suck you off" if fairyn.has_tag('joint_fuck_each_other'):
      call fairyn_joint_fairyn_suck from _call_fairyn_joint_fairyn_suck_7
    "That's enough fun for you, too" if fairyn.has_tag('joint_fuck_each_other'):
      "You thank the ladies for the show, and send them home."
      change player energy by -energy_very_short notify
  wt_image living_room.image
  rem tags 'joint_hoped' from diamond
  rem tags 'joint_hoped' 'joint_pleasure' 'joint_fuck_each_other' 'joint_display' 'joint_disobey' from fairyn
  call character_location_return(diamond) from _call_character_location_return_201
  call character_location_return(fairyn) from _call_character_location_return_202
  return

label fairyn_joint_fuck_diamond_ass:
  wt_image ms1_ms2_joint_event_2_8
  "You don't make her wait long."
  fairyn.c "That's a good ass whore. Open wide and take him all the way up your butt hole."
  diamond.c "Ooohh"
  fairyn.c "Mmmm. That hurts doesn't it? And you like it, don't you? Answer me, ass whore."
  diamond.c "Yeessss"
  wt_image ms1_ms2_joint_event_2_9
  fairyn.c "That silly subbie brain of yours loves that you're just a hole for his pleasure, doesn't it?"
  diamond.c "Yes!"
  fairyn.c "But that's not enough to get you off, is it?"
  "Diamond shakes her head forlornly."
  fairyn.c "Good! I'd hate to think my week of denying you an orgasm would be ruined by you getting off on being an ass whore."
  "She may not be able to cum, but you are."
  $ title = "Where do you want to cum?"
  menu:
    "In Diamond's ass":
      wt_image ms1_ms2_joint_event_2_10
      player.c "[player.orgasm_text]"
      "As you pump your load into her backside, Diamond shudders. It isn't an orgasm, not exactly, but it's close."
      "Fairyn looks like she's experiencing something close to a climax, too, leaning over and probing Diamond's mouth as she soaks in the sight, smell and sound of your pleasure."
      diamond.c "oohhhh"
      fairyn.c "Mmmmmmm"
      wt_image ms1_ms2_joint_event_2_4
      fairyn.c "Time for us to go. Thank the man for the ass fucking."
      diamond.c "Thank you for the ass fucking."
      "Her words are addressed to you, but her gaze is firmly on her friend and Mistress-for-the-week."
    "In Diamond's mouth":
      wt_image ms1_ms2_joint_event_3_1
      "You pull your cock out of Diamond's ass and motion to the floor in front of you."
      player.c "Get your mouth over here."
      "She scrambles around kneels in front of you, opening her mouth, which you promptly fill with your cock. If she cares that your dick was just buried in her butthole, she doesn't say anything."
      player.c "[player.orgasm_text]"
      fairyn.c "Mmmmmm. What a good ass whore. When he finishes cumming, make sure you clean every last speck of your shit off his dick before we go. We don't want to leave a bad impression by leaving a mess behind."
      $ diamond.swallow_count += 1
    "In Fairyn's mouth":
      player.c "Fairyn, get your mouth over here."
      wt_image ms1_ms2_joint_event_1_25
      fairyn.c "My mouth??"
      player.c "Yes, your mouth. It was your idea that I use her ass. Come deal with the consequences."
      fairyn.c "It's going to be ..."
      player.c "Dirty from being up Diamond's butt hole? Quite likely, yes. That's part of the consequences."
      wt_image ms1_ms2_joint_event_1_26
      "Diamond watches with interest as you extract your cock from her ass and present it to Fairyn."
      player.c "Finish me off, Fairyn. You can clean up any mess you find at the same time."
      wt_image ms2_bj_1_2
      "You hold off as long as you can, forcing Fairyn to thoroughly clean off every inch of your cock before earning your load."
      player.c "[player.orgasm_text]"
      $ fairyn.swallow_count += 1
      wt_image ms1_ms2_joint_event_1_16
      "Licking her lips, Fairyn looks at you with a mischievous grin."
      fairyn.c "Mmmmm. Seems you liked that."
      $ title = "What do you tell her?"
      menu:
        "It was great":
          player.c "It was great. You, [diamond.training_name]'s ass, and your mouth can drop by anytime."
          fairyn.c "Aw, thanks! You sure know how to sweet talk a lady."
          fairyn.c "Come on, Diamond, time for us to go. We should grab something to eat. I'm pretty full now, but you must be getting hungry."
        "The ass fucking was great":
          player.c "The ass fucking was great."
          wt_image ms1_ms2_joint_event_1_15
          fairyn.c "Oh? And what, my blow job wasn't?"
          player.c "It was okay."
          wt_image ms1_ms2_joint_event_1_47
          fairyn.c "Okay?? I just sucked you off after you had your dick up her butt."
          call fairyn_joint_post_bj from _call_fairyn_joint_post_bj_1
  $ diamond.anal_count += 1
  orgasm notify
  return

label fairyn_joint_fuck_fairyn_ass:
  wt_image ms1_ms2_joint_event_2_12
  "You don't make her wait long."
  fairyn.c "Oh!"
  diamond.c "That's just the tip of his cock. You think that hurts? It's going to feel like he's ripped you a new one by the time he shoves the rest in."
  wt_image ms1_ms2_joint_event_2_13
  "Maybe not a new one, but a very, very full existing one as you push deeper and deeper inside her."
  fairyn.c "oohhh"
  "Fairyn tries to reach between her legs, but Diamond pulls Fairyn's legs shut, blocking access to her sex."
  diamond.c "Oh no you don't!  No touching yourself.  Ass whores take it up the butt without any other stimulation.  If you're going to cum, you're going to cum from his cock in your ass only, ass whore."
  fairyn.c "oooohhh"
  "As much as her groans include an element of pleasure, it doesn't sound like she is going to cum, at least not anytime soon.  You, on the other hand, could let go anytime."
  $ title = "Where do you want to cum?"
  menu:
    "In Fairyn's ass":
      wt_image ms1_ms2_joint_event_2_14
      player.c "[player.orgasm_text]"
      fairyn.c "oooohh"
      "Fairyn groans in some combination of relief and frustration as you empty your load inside her. Diamond, on the other hand, is absolutely ecstatic as she watches your balls pump sperm up Fairyn's backside."
      diamond.c "Oh yes!! Fill that ass whore with your cum!"
      wt_image ms1_ms2_joint_event_2_4
      diamond.c "Maybe I should drive home? You're not going to be able to concentrate on the road the way your butt is going to be burning, ass whore."
      fairyn.c "You do realize I still own you for the rest of the week, right?"
      diamond.c "Yes, Mistress Ass Whore. And I'll obey you the way I would Master M, just like I promised my Master, Mistress Ass Whore."
      fairyn.c "You are so going to pay for that."
      diamond.c "When Mistress Ass Whore? When your butt stops burning?"
      "Fairyn giggles."
      fairyn.c "Let's get out of here before you get yourself in any more trouble. And yes, you should definitely drive."
    "In Diamond's mouth":
      wt_image ms1_ms2_joint_event_2_15
      player.c "[diamond.training_name], get your mouth up here."
      diamond.c "nnnnn"
      "She whimpers softly as she realizes what's about to happen, but dutifully places her mouth close at hand as you pull out of Fairyn's butt."
      wt_image ms1_ms2_joint_event_3_1
      "The fun she was having teasing her friend is replaced by intense humiliation as you extract your cock from Fairyn's butt and place it directly in Diamond's waiting mouth."
      player.c "[player.orgasm_text]"
      fairyn.c "Oh, wow! Has Master M ever made you clean off someone else's shit? Because me, being a silly ass whore, I didn't think to clean my butt out thoroughly before we came over, and I think I probably left a mess on his dick."
      fairyn.c "When he finishes cumming, make sure you clean off every last speck before we go. We don't want to leave a bad impression by leaving a mess behind."
      $ diamond.swallow_count += 1
    "In Fairyn's mouth":
      wt_image ms2_bj_1_2
      "You pull your cock out of Fairyn's ass and motion for her to turn around."
      player.c "Get your mouth over here."
      "She scrambles around and takes your cock into her mouth. If she cares that your dick was just buried in her butthole, she doesn't say anything."
      wt_image ms1_ms2_joint_event_1_26
      "Diamond watches with interest as you direct Fairyn's mouth up and down your shaft."
      player.c "Finish me off, Fairyn. You can clean up any mess you find at the same time."
      wt_image ms2_bj_1_3
      "You hold off as long as you can, forcing Fairyn to thoroughly clean off every inch of your cock before earning your load."
      player.c "[player.orgasm_text]"
      $ fairyn.swallow_count += 1
      wt_image ms1_ms2_joint_event_1_16
      "After she finishes swallowing, Fairyn looks at you with a mischievous grin."
      fairyn.c "Mmmmm. Seems you liked that."
      $ title = "What do you tell her?"
      menu:
        "It was great":
          player.c "It was great. You, your ass, and your mouth can drop by anytime."
          fairyn.c "Aw, thanks! You sure know how to sweet talk a lady."
          fairyn.c "Come on, Diamond, time for us to go. We should grab something to eat. I'm pretty full now, but you must be getting hungry."
        "The ass fucking was great":
          player.c "The ass fucking was great."
          wt_image ms1_ms2_joint_event_1_15
          fairyn.c "Oh? And what, my blow job wasn't?"
          player.c "It was okay."
          wt_image ms1_ms2_joint_event_1_47
          fairyn.c "Okay?? I just sucked you off after you had your dick up my butt."
          call fairyn_joint_post_bj from _call_fairyn_joint_post_bj_2
  $ fairyn.anal_count += 1
  orgasm notify
  return

label fairyn_joint_have_them_blow_you:
  player.c "Now that I've thought about it, I think I'd rather have your mouths on me."
  wt_image ms1_ms2_joint_event_2_16
  "You point at the floor in front of you. They kneel down as you take out your cock."
  wt_image ms1_ms2_joint_event_2_17
  "The two of them get to work pleasuring your dick."
  wt_image ms1_ms2_joint_event_2_18
  "Fairyn takes charge of the blowjob, while Diamond plays more of a supporting role with your shaft and balls."
  wt_image ms1_ms2_joint_event_2_19
  "You make sure they both, however, get an equal amount of the reward for their effort."
  player.c "[player.orgasm_text]"
  call fairyn_joint_fairyn_suck_question from _call_fairyn_joint_fairyn_suck_question
  $ diamond.blowjob_count += 1
  $ diamond.facial_count += 1
  $ fairyn.blowjob_count += 1
  $ fairyn.facial_count += 1
  orgasm notify
  return

label fairyn_joint_diamond_suck:
  wt_image ms1_ms2_joint_event_1_15
  "Fairyn watches with interest as Diamond lowers herself to her knees in front of you..."
  wt_image ms1_ms2_joint_event_3_1
  "... and takes your cock into her mouth ..."
  wt_image ms1_ms2_joint_event_3_2
  "... using her lips ..."
  wt_image ms1_ms2_joint_event_3_3
  "... and tongue ..."
  wt_image ms1_ms2_joint_event_3_6
  "... to extract the cum from your balls."
  wt_image ms1_ms2_joint_event_3_4
  player.c "[player.orgasm_text]"
  wt_image ms1_ms2_joint_event_1_16
  fairyn.c "Mmmmm. That was hot. Time to go, Diamond."
  wt_image ms1_ms2_joint_event_3_5
  fairyn.c "Don't bother to dress. It's a nice day. With the top of the convertible down, the sun will keep you warm."
  fairyn.c "We'll swing through the drive through on the way home and get some coffee. You can ask for extra cream in yours."
  $ diamond.blowjob_count += 1
  $ diamond.facial_count += 1
  orgasm notify
  return

label fairyn_joint_fairyn_suck:
  player.c "Not until you use your mouth to get me off, too."
  wt_image ms1_ms2_joint_event_1_25
  fairyn.c "Seriously? I had no idea my mouth was so popular in these parts."
  fairyn.c "I wonder if you're going to be as quick as my supposedly straight subbie friend?"
  wt_image ms1_ms2_joint_event_1_26
  "Her 'supposedly straight subbie friend' makes herself comfortable and watches with interest as Fairyn lowers herself to her knees in front of you."
  wt_image ms2_bj_1_1
  "Taking your dick in her hand, Fairyn gives it a long lick ..."
  wt_image ms2_bj_1_2
  "... then begins her blow job.  You were already turned on by the show she and Diamond put on for you, so unsurprisingly..."
  wt_image ms2_bj_1_3
  "... it's not long before she coaxes the sperm out of your balls and into her mouth."
  player.c "[player.orgasm_text]"
  call fairyn_joint_fairyn_suck_question from _call_fairyn_joint_fairyn_suck_question_1
  $ fairyn.blowjob_count += 1
  $ fairyn.swallow_count += 1
  orgasm notify
  return

label fairyn_joint_fairyn_suck_question:
  wt_image ms1_ms2_joint_event_1_16
  "Licking her lips, Fairyn looks at you with a mischievous grin."
  fairyn.c "Mmmmm.  Seems you liked my mouth."
  $ title = "What do you tell her?"
  menu:
    "It was great":
      if fairyn.has_tag('joint_display'):
        player.c "It was great. You, your mouth, and [diamond.training_name]'s mouth can drop by anytime."
        fairyn.c "Aw, thanks! You sure know how to sweet talk a lady."
        fairyn.c "Come on, Diamond, time for us to go. We should grab something to eat. I don't know about you, but I thought that made for a nice appetizer. Now I want something sweet to go with it."
      else:
        player.c "It was great. You and your mouth can drop by anytime."
        fairyn.c "Aw, thanks! You sure know how to sweet talk a lady."
        fairyn.c "Come on, Diamond, time for us to go. We should grab something to eat. I'm pretty full now, but you must be getting hungry."
    "It was okay":
      wt_image ms1_ms2_joint_event_1_15
      player.c "It was okay."
      if fairyn.has_tag('joint_display'):
        fairyn.c "Okay??  You just got a blow job from two hot women, and blew a giant load over our faces."
        player.c "It was fun. [diamond.training_name]'s tongue on my shaft and balls felt great, and between the two of you, you got me off."
        wt_image ms1_ms2_joint_event_1_47
        fairyn.c "Between the two of us? And Diamond's tongue felt great? So what?? My blow job wasn't very good??"
      else:
        fairyn.c "Just okay? I have a belly load of sperm that says otherwise."
        player.c "Sure, after watching the two of you got me worked up, I came quickly, but ..."
        wt_image ms1_ms2_joint_event_1_47
        fairyn.c "You came quickly but what? My blow job wasn't very good??"
      call fairyn_joint_post_bj from _call_fairyn_joint_post_bj_3
  return

label fairyn_joint_post_bj:
    $ title = "What do you tell her?"
    menu:
        "You can show her how to be better":
            player.c "Like I said, it was okay. If you want, I can show you how it could be better."
            wt_image ms1_ms2_joint_event_1_15
            fairyn.c "Wow!! What an offer! I can use your dick for practice so I get better at blowing guys? Does that work on any women?"
            player.c "The ones who really want to learn how to please a man with their mouth, yes."
            wt_image ms1_ms2_joint_event_1_49
            fairyn.c "I'll pass. Thanks for the 'kind' offer, but I don't get any complaints."
            wt_image ms1_ms2_joint_event_1_48
            fairyn.c "Come on, Diamond.  Time for us to go."
        "You can train her if she pays you":
            player.c "Like I said, it was okay. If you want to hire me, I can train you how to be better. For you, I'm thinking 50 per session."
            wt_image ms1_ms2_joint_event_1_15
            fairyn.c "Seriously?? You not only want me to blow you again, you want me to pay you for the privilege??"
            wt_image ms1_ms2_joint_event_1_49
            fairyn.c "I admit, I love to waste my money on frivolous things, but no one's every complained about the blow jobs I give."
            player.c "Most men won't tell a woman she's not doing a good job. That tends to lead to them not getting any blow jobs at all."
            wt_image ms1_ms2_joint_event_1_47
            player.c "But if a woman wants to get good at it, she not only has to blow a lot of men, she also has to blow ones who will show her exactly what they like."
            wt_image ms1_ms2_joint_event_1_26
            player.c "[diamond.training_name], how many men has Master M given you to, to teach you how to pleasure them properly?"
            diamond.c "Umm, am I allowed to stay out of this?"
            wt_image ms1_ms2_joint_event_1_25
            fairyn.c "Of course you can stay out of this. Are you trying to say that Diamond sucks cock better than I do?"
            wt_image ms1_ms2_joint_event_1_26
            diamond.c "I don't think that's really keeping me out of this."
            wt_image ms1_ms2_joint_event_1_25
            player.c "Yes, she does. Of course, she does. How could she not? She's been taught how to do it and you're an amateur."
            wt_image ms1_ms2_joint_event_1_26
            diamond.c "Oh wow, see, that's definitely not keeping me out of this."
            wt_image ms1_ms2_joint_event_1_49
            fairyn.c "Well!! I guess I know where I stand in your eyes. Sorry you wasted your stiffy on me when you could have had this expert cocksucker look after it for you."
            wt_image ms1_ms2_joint_event_1_27
            diamond.c "Guys!  Enough!!"
            wt_image ms1_ms2_joint_event_1_48
            fairyn.c "Sorry, Diamond. You're right. Let's you, me, and your professional grade cocksucking mouth get out of here."
            wt_image ms1_ms2_joint_event_1_27
            diamond.c "Fairyn!! Cut it out! This is what he does for a living, remember? He trains women."
            wt_image ms1_ms2_joint_event_1_50
            diamond.c "He's pitching you on his services. You should be used to that. People are always trying to sell you something. Tell him no or hire him or whatever, but don't get pissed at me."
            wt_image ms1_ms2_joint_event_1_16
            fairyn.c "You're right. I'm sorry. Truly this time. I shouldn't have got upset. Let's go to a bar and you can buy me a drink to make me feel better."
            wt_image ms1_ms2_joint_event_1_50
            diamond.c "I can't, remember? You took away my money and said I couldn't have it back until my week of belonging to you was over."
            wt_image ms1_ms2_joint_event_1_25
            fairyn.c "Oh, right. Okay then, let's go to a bar and I'll buy me a drink while you blow the bartender and explain to me what I do wrong when I have a cock in my mouth."
            wt_image ms1_ms2_joint_event_1_27
            diamond.c "Real mature, Fairyn."
            wt_image ms1_ms2_joint_event_1_16
            fairyn.c "Relax, I'm teasing. Probably. Let's go."
            $ fairyn.bj_training_status = 1
    return

label fairyn_review_photos:
    wt_image ms2_visit_1_18
    "She was born into wealth and privilege, but she struggles with a sense of feeling hollow inside."
    wt_image ms2_visit_1_19
    "Some days being treated like this she's worthless helps for a little while, but only a little while."
    wt_image current_location.image
    return

## Character Specific Objects
# Select Who You're Lending to Master M
label master_m_lend:
    ## now handled differently, see below; this is now called at the end of each slavegirl's visit
    # call choose_person_with_tags(['slavegirl'])
    # if current_target is not None:
    #     call safe_call(current_target.short_name + '_lend_to_master_m')
    #     $ master_m.slave_name_loaned = current_target.full_name

    # the conditional is for future use, to allow multiple loans; right now you will always be on 1 when you get here
    if master_m.lent_him_a_slave == 1:
        $ master_m.lent_him_a_slave = 2
        $ master_m.change_status("prospect") ## this allows him to now send a new message re Fairyn
        # $ master_m.current_client_action.name = "New Message from Master M" ## doesn't work here, needs to be in start_day after action is re-created
    rem tags 'm_waiting_for_slave' from player
    return

### Items
## Master M
# Give Butt Plug
label give_bp_master_m:
  "I'm curious about how you'd start this conversation?"
  return

# Give Chastity Belt
label give_cb_master_m:
  "You and he are going to have to become much closer friends before you broach this topic."
  return

# Give Dildo
label give_di_master_m:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_master_m:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_master_m:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_master_m:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_master_m:
  "How is this conversation not going to end awkwardly?"
  return

# Give Love Potion
label give_lp_master_m:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_master_m:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_master_m:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_master_m:
  "You should try this on someone else."
  return

## Diamond
# Give Butt Plug
label give_bp_diamond:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_diamond:
  "Not your decision to make."
  return

# Give Dildo
label give_di_diamond:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_diamond:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_diamond:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_diamond:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_diamond:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_diamond:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_diamond:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_diamond:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_diamond:
  "Not your decision to make."
  return

## Fairyn
# Give Butt Plug
label give_bp_fairyn:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_fairyn:
  "Her man would likely want to put one on her.  Whether she'd let him is another question."
  return

# Give Dildo
label give_di_fairyn:
  "You know she has lots of these, right?"
  return

# Use Fetch Toy
label use_ft_fairyn:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_fairyn:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_fairyn:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_fairyn:
  "Unless you paid way too much for it, she's not going to be impressed."
  return

# Give Love Potion
label give_lp_fairyn:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_fairyn:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_fairyn:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_fairyn:
  "If only the game offered content for this path."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label master_m_start_day:
    if master_m.has_tag('new_message_today'):
        rem tags 'new_message_today' from master_m
        $ master_m.current_client_action.name = "New Message from Master M"
    # if (master_m.lent_him_a_slave == 4 or master_m.lent_him_a_slave == 5) and not master_m.has_tag('message_2'):
    #   add tags 'message_2' to master_m
    #   $ master_m.wait_on_message = False
    #   $ master_m.change_status("waiting_on_message")
    #   notify "You received a new message today."
    #   notify
    # if master_m.has_tag('message_2') and not master_m.status == "waiting_on_message":
    #   rem tags 'message_2' from master_m
    return

#label diamond_start_day: # not needed
#  return

#label fairyn_start_day: # not needed
#  return

# End Day
label master_m_end_day:
    rem tags 'in_club_now' from master_m
    call character_location_return(master_m) from _call_character_location_return_203
    return

label diamond_end_day:
    rem tags 'club_maid_today' 'dancing_today' 'in_club_now' 'on_stage_now' from diamond
    $ diamond.remove_action(diamond.action_private_show)
    $ diamond.action_private_show = None
    call character_location_return(diamond) from _call_character_location_return_204
    return

label fairyn_end_day:
    rem tags 'in_club_now' from fairyn
    call character_location_return(fairyn) from _call_character_location_return_205
    return

# End Week
label master_m_end_week:
  # ## CHECK FOR NEW PROSPECTS: Master M Lent Slave Status 2 or 3
  if master_m.lent_him_a_slave == 2 or master_m.lent_him_a_slave == 3:
    $ master_m.lent_him_a_slave += 2
  #   these changed by new multiple prospect message system
  #   $ master_m.action_show_message = living_room.add_action("New message from Master M", label = master_m.short_name + "_message", context = '_check_messages')
  #   notify "You received a new message today."
  #   notify
  return

label ms1_ms2_joint_event_initiation:
  wt_image ms1_ms2_joint_event_1_2
  if diamond.training_name == "Diamond":
    fairyn.c "It's your old friend, Diamond."
  else:
    fairyn.c "It's your old friend, Diamond. No, what did she say you called her? Oh right, [diamond.training_name]."
    wt_image ms1_ms2_joint_event_1_40
    fairyn.c "Not very imaginative, really.  I like Diamond better."
    wt_image ms1_ms2_joint_event_1_2
  fairyn.c "Don't say hello, Diamond.  Keep your tongue busy in my snatch."
  wt_image ms1_ms2_joint_event_1_1
  fairyn.c "Master M lent her to me for the week, because I was bored and he thought it would be good for both of us."
  wt_image ms1_ms2_joint_event_1_3
  fairyn.c "Diamond and I get along really well together, at least we do when I don't make her eat me out."
  wt_image ms1_ms2_joint_event_1_42
  fairyn.c "She's not really into girls, and I know she'll get me back the first time she has the opportunity, but I get horny a lot and her tongue feels better than my toys, so it'll be tired before the week is out."
  wt_image ms1_ms2_joint_event_1_41
  fairyn.c "I'm used to people doing what I say because they want my business or they want to get into my pants, but it's kind of fun having someone you think of as a friend, and now all of a sudden she has to do everything you say."
  $ diamond.lesbian_training += 1
  if diamond.training_result > 6:
    wt_image ms1_ms2_joint_event_1_1
    fairyn.c "Anyway, before I put her mouth to work dealing with my horniness, Diamond was telling me how much fun she had when M sent her to you. So we got to talking and agreed that I should call you and see if you'd like the two of us to drop over together."
    wt_image ms1_ms2_joint_event_1_3
    fairyn.c "She didn't know she was going to be licking my pussy when I called you, but that's what happens when you're the slave, isn't it Diamond?"
    wt_image ms1_ms2_joint_event_1_4
    fairyn.c "Oh, that feels good! Say yes again with your lips wrapped around my clit. Mmmmmm."
    wt_image ms1_ms2_joint_event_1_41
    fairyn.c "Okay, I have to let Diamond finish what she's started. Let me know if you want us to drop by, but it has to be this week. I only have Diamond until Friday. Bye!"
    sys "Note that this event is only available this week."
    $ fairyn.action_contact = living_room.add_action("Invite Fairyn and Diamond Over", label = fairyn.short_name + "_contact", context = "_contact_other", condition = "fairyn.can_be_interacted and diamond.can_be_interacted and master_m.ms1_ms2_joint_event == 3")
  else:
    if diamond.training_result == 6:
      wt_image ms1_ms2_joint_event_1_1
      fairyn.c "Anyway, before I put her mouth to work dealing with my horniness, Diamond and I were talking about how she found serving you to be a real lesson in obedience."
      wt_image ms1_ms2_joint_event_1_42
      fairyn.c "That made me think that maybe I have you to thank, at least in part, for teaching Diamond to be obedient enough to lick my pussy even though she really doesn't want to."
      wt_image ms1_ms2_joint_event_1_41
      fairyn.c "So as my thank you, I'll let you watch, over the phone, as she eats me out, if you want to?"
    else:
      wt_image ms1_ms2_joint_event_1_40
      fairyn.c "Anyway, I understand that the training session between you and Diamond didn't really go the way M hoped it would, but I thought you should know that Diamond is learning to be a much better slave. Her licking my pussy even though she really doesn't want to is evidence of that."
      wt_image ms1_ms2_joint_event_1_41
      fairyn.c "Did you want to see how obedient she's being? If so, I'll let you watch, over the phone, as she eats me out."
    $ title = "Watch Diamond eat out Fairyn?"
    menu:
      "Yes, watch the show":
        wt_image ms1_ms2_joint_event_1_3
        fairyn.c "Did you hear that, Diamond? He wants to watch you pleasure me. Be a good slave and give me a really powerful orgasm this time."
        wt_image ms1_ms2_joint_event_1_2
        "As Fairyn turns the phone so you can see, it's apparent that Diamond is trying hard to get Fairyn off. The moan that escapes Fairyn suggests it's working."
        wt_image ms1_ms2_joint_event_1_4
        fairyn.c "oooooo"
        wt_image ms1_ms2_joint_event_1_3
        fairyn.c "oooooo ... I'm going to be cumming in your mouth in no time, my little subbie friend."
        wt_image ms1_ms2_joint_event_1_5
        fairyn.c "After you get me off, I'm going to treat you to lunch out at that bistro at the corner of Main and North. Do you remember the cute waiter who was flirting with you the last time we ate there together?"
        wt_image ms1_ms2_joint_event_1_4
        fairyn.c "If he's working today I'm going to ask him if he can guess what you were doing this morning.  If he guesses right, you're going to blow him in the restaurant bathroom while I watch."
        wt_image ms1_ms2_joint_event_1_5
        fairyn.c "If he guesses wrong, I'm going to see what I can do to get him eating your pussy before today is done."
        wt_image ms1_ms2_joint_event_1_13
        "Aroused by her own naughty planning, Fairyn relaxes into her friend's tongue and lets herself go."
        fairyn.c "oooooo  ....  OOHHHH!!"
        wt_image ms1_ms2_joint_event_1_6
        "For her part, the look on Diamond's face as she brings her friend to orgasm suggests Master M may have been on to something in lending her to Fairyn for the week, if part of his objective is to acclimatize Diamond to serve women as enthusiastically as she serves men."
        # Fairyn & Diamond event was watched on the phone
        $ master_m.ms1_ms2_joint_event = 5
        $ fairyn.orgasm_count += 1
        change player energy by -energy_very_short notify
      "No thanks":
        "You have better things to do with your day. You thank Fairyn for the offer, then hang up and leave the two of them to their games."
        # no Fairyn and Diamond event
        $ master_m.ms1_ms2_joint_event = 4
  return

label diamond_end_week:
    pass
    return

label fairyn_end_week:
  ## Fairyn Diamond Event
  if master_m.ms1_ms2_joint_event > 0 and master_m.ms1_ms2_joint_event < 4:
    # advances weekly timer
    $ master_m.ms1_ms2_joint_event += 1
    if master_m.ms1_ms2_joint_event == 3:
      wt_image phone_1
      "Your phone is ringing."
      wt_image ms1_ms2_joint_event_1_1
      fairyn.c "Hi! It's me, Fairyn."
      player.c "So it is."
      fairyn.c "Guess who's eating my pussy?"
      $ title = "Guess?"
      menu:
        "The maid from the Club":
          wt_image ms1_ms2_joint_event_1_40
          fairyn.c "Who?  Oh, her.  Nah."
          call ms1_ms2_joint_event_initiation from _call_ms1_ms2_joint_event_initiation
        "Your latest boytoy":
          wt_image ms1_ms2_joint_event_1_41
          fairyn.c "Mmmmm. I didn't think to call you when he was eating me out. No, not him."
          call ms1_ms2_joint_event_initiation from _call_ms1_ms2_joint_event_initiation_1
        "Your imaginary friend":
          wt_image ms1_ms2_joint_event_1_42
          "She giggles."
          fairyn.c "Nah. I wouldn't bother to call you if I was just playing with myself."
          call ms1_ms2_joint_event_initiation from _call_ms1_ms2_joint_event_initiation_2
        "Good-bye, Fairyn":
          wt_image ms1_ms2_joint_event_1_40
          fairyn.c "Ahhh, are you really going to hang ..."
          wt_image living_room.image
          # no Fairyn and Diamond event
          $ master_m.ms1_ms2_joint_event = 4
    if master_m.ms1_ms2_joint_event == 4:
      # shuts off Fairyn and Diamond event if previously opened
      $ living_room.remove_action(fairyn.action_contact)
  ## Fairyn Training Event
  else:
    if fairyn.bj_training_status > 0 and fairyn.bj_training_status < 3:
      # advances weekly timer
      $ fairyn.bj_training_status += 1
    if fairyn.bj_training_status == 3 and fairyn.status == 'minor_character':
      # shuts off timer as event now activated
      $ fairyn.bj_training_status = 4
      $ fairyn.action_show_message = living_room.add_action("New message from Fairyn", label = fairyn.short_name + "_message", context = '_check_messages')
      notify "You received a new message today."
      notify
  return

## Club and Stage Labels

label master_m_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if master_m.has_tag('in_club_now'):
            $ master_m.location = club
    else:
        $ master_m.random_number = renpy.random.randint(1, 10)
        if master_m.random_number > 5 and master_m.ms1_ms2_joint_event != 3:
            $ master_m.location = club
            add tags 'in_club_now' to master_m
            if not master_m.has_tag('gloria_club_talk_possible'):
                add tags 'gloria_club_talk_possible' to master_m
            if master_m.encounter_possible > 1:
                $ diamond.random_number = renpy.random.randint(1, 10)
                if diamond.random_number < 3:
                    $ diamond.location = club
                    add tags 'in_club_now' 'club_maid_today' to diamond
                elif diamond.random_number > 8:
                    $ diamond.location = stage
                    add tags 'on_stage_now' 'dancing_today' to diamond
    return

label diamond_club_call:
    $ diamond.training_regime = 'daily' # as her call is handled in master_m's label
    if player.has_tag('club_visited_today'):
        if diamond.has_tag('in_club_now'):
            $ diamond.location = club
    return

label fairyn_club_call:
    $ fairyn.training_regime = 'daily'
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if fairyn.has_tag('in_club_now'):
            $ fairyn.location = club
    else:
        $ fairyn.random_number = renpy.random.randint(1, 10)
        if fairyn.random_number < 3:
            $ fairyn.location = club
            add tags 'in_club_now' to fairyn
            if not fairyn.has_tag('gloria_club_talk_possible'):
                add tags 'gloria_club_talk_possible' to fairyn
    return

label master_m_club_send_home:
    call character_location_return(master_m) from _call_character_location_return_206
    return

label diamond_club_send_home:
    # $ diamond.training_regime = 'weekly'
    call character_location_return(diamond) from _call_character_location_return_207
    return

label fairyn_club_send_home:
    # $ fairyn.training_regime = 'weekly'
    call character_location_return(fairyn) from _call_character_location_return_208
    return

label diamond_stage_send_home:
    # $ diamond.training_regime = 'weekly'
    call character_location_return(diamond) from _call_character_location_return_209
    return


## Club President Wife Content

label master_m_gloria_club_talk_option:
    gloria.c "Master M? That's what everyone calls him. He has a real name, of course, but I'd have to check the Club records to remember what it is."
    gloria.c "He's been a Club member a long time. Very popular with the wives of other members. They like to hang around him, hoping he'll pick them out for a spanking."
    gloria.c "Most of them aren't even submissives, they just like the idea of being disciplined by the Club's best looking Dom."
    gloria.c "Not that they could take his real discipline. They think a swat on the rear while bent over his knee is a punishment. They haven't seen the rears of his slavegirls after a real punishment."
    gloria.c "Mostly he ignores them and spends his time chatting with his friends at the Club."
    if master_m.name == "Well Dressed Man":
        $ master_m.name = "Master M"
    return

label fairyn_gloria_club_talk_option:
    gloria.c "I hadn't seen her for a long time, but she seems to be back. Weird name ... Faye-lynn or Flo-anne or something. Apparently her Daddy's loaded."
    gloria.c "She's friends with Master M, though I can't for the life of me I can't remember whether he sponsored her for membership or she met him here."
    return


## Character Specific Timers
# Fairyn Initial Conversation
label fairyn_initial_conversation:
    $ fairyn.temporary_count = 0
    while fairyn.temporary_count == 0:
        $ title = "What do you say to her?"
        menu:
            "What's your name?" if not fairyn.has_tag('know_name'):
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_5
                else:
                    wt_image ms2_visit_1_36
                fairyn.c "Oh?  Are we going to be on a first name basis?  Okay, then.  Mine's Fairyn.  Wait.  Don't tell me yours.  I don't care."
                $ fairyn.change_full_name("", "Fairyn", "the Trust Fund Baby")
                player.c "Fairyn.  That's unusual."
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_4
                fairyn.c "It's an old family name on my father's side. It's the biggest thing he contributed to my upbringing: a name no one's ever heard of."
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_36
                fairyn.c "Oh, that and money.  He also contributed a lot of money."
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_3
                fairyn.c "After all, if you give your daughter lots of money, even if it's in a trust fund and she's not allowed to touch most of it, then you don't have to worry about little things like calling her on her birthday or coming to watch her in the school play."
                add tags 'know_name' to fairyn
            "You have Daddy issues" if not fairyn.has_tag('fairyn_convo_daddy') and fairyn.has_tag('know_name'):
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_1
                fairyn.c "Wow!  Really??  You are so observant!"
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_36
                fairyn.c "Would you like to hear about them?  Normally I have to pay someone 25 an hour to listen to me complain about how my emotionally inaccessible father screwed up my life, but maybe you're so hard up for a view of my tits that you'd stand there and listen to me for free?"
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_3
                fairyn.c "Not that I need the discount.  Daddy at least makes sure that my monthly trust fund distribution can pay for a lot of therapy sessions."
                add tags 'fairyn_convo_daddy' to fairyn
            "Tell me about your father" if not fairyn.has_tag('fairyn_convo_father') and fairyn.has_tag('fairyn_convo_daddy'):
                wt_image ms2_visit_1_40
                fairyn.c "Fuck off.  I didn't come here to talk about my father.  Can we get on with it?"
                add tags 'fairyn_convo_father' to fairyn
            "Not until you talk about your father" if fairyn.has_tag('fairyn_convo_father'):
                wt_image ms2_visit_1_38
                fairyn.c "Seriously?  Clearly this was a mistake.  M's usually a better judge of character."
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_39
                    fairyn.c "See ya!"
                    "She stands up and leaves."
                else:
                    wt_image ms2_visit_1_6
                    fairyn.c "See ya!"
                    "She turns and leaves."
                $ fairyn.temporary_count = 2
            "Kneel" if not fairyn.has_tag('kneeling'):
                wt_image ms2_visit_1_3
                fairyn.c "Seriously?  You expect me to kneel for you??"
                wt_image ms2_visit_1_4
                fairyn.c "Why?"
                $ title = "What do you tell her?"
                menu menu_fairyn_convo_kneel:
                    "So you can put your mouth to proper use":
                        player.c "So you can put your mouth to proper use."
                        wt_image ms2_visit_1_36
                        fairyn.c "Pfffff.  I'm not interested in having your dick in my mouth."
                        $ title = "What now?"
                        menu menu_fairyn_convo_kneel_mouth:
                            "I don't care what you're interested in" if not fairyn.has_tag('fairyn_convo_dont_care'):
                                player.c "I don't care what you're interested in.  I want your mouth on my cock."
                                wt_image ms2_visit_1_3
                                fairyn.c "Guess you're going to have to figure out how to make that happen, then."
                                add tags 'fairyn_convo_dont_care' to fairyn
                                jump menu_fairyn_convo_kneel_mouth
                            "Tell her to kneel" if fairyn.has_tag('fairyn_convo_dont_care'):
                                wt_image ms2_visit_1_4
                                "She rolls her eyes."
                                fairyn.c "Haven't we already been over this?"
                            "Force her to her knees" if fairyn.has_tag('fairyn_convo_dont_care'):
                                wt_image ms2_visit_1_6
                                "She's quick.  She dodges before you can put your hands on her."
                                fairyn.c "Don't you fucking touch me without consent!!  M said you knew how to control women.  Guess he was wrong.  See ya, loser!"
                                $ fairyn.temporary_count = 3
                            "Choose a new approach":
                                pass
                    "All women should kneel":
                        player.c "All women should kneel."
                        fairyn.c "Really??  Before you, or before all men?"
                        $ title = "Which?"
                        menu:
                            "Before you":
                                wt_image ms2_visit_1_36
                                "She laughs."
                                fairyn.c "Full of yourself, aren't you?  Or are you one of those 'gotta catch 'em all' losers who doesn't feel fulfilled until every woman bows before his perceived greatness?"
                                wt_image ms2_visit_1_3
                                fairyn.c "Doesn't matter.  I haven't seen anything from you yet to make me want to kneel for you."
                            "Before all men":
                                wt_image ms2_visit_1_36
                                "She laughs."
                                wt_image ms2_visit_1_3
                                fairyn.c "Do you really believe that??  That all women should be submissive to men?  You're not really familiar with the spectrum of human sexuality, are you sweetie?"
                                $ title = "What now?"
                                menu:
                                    "Women are naturally subordinant, and that's how they should be treated":
                                        player.c "I'm familiar with it.  All women, though, even those who portray themselves as dominant, enjoy the presence of a strong man and are happier when they subordinate themselves to one."
                                        call fairyn_convo_chauvinism_chain from _call_fairyn_convo_chauvinism_chain
                                    "Women are inferior, and that's how they should be treated":
                                        player.c "I'm familiar with it.  Doesn't change human nature.  Women are inferior to men.  It doesn't matter if a few wimps get a kick out of subjugating themselves to their inferiors.  That doesn't change that men are the dominant gender and women are happier when they subordinate themselves."
                                        call fairyn_convo_chauvinism_chain from _call_fairyn_convo_chauvinism_chain_1
                                    "Choose a new approach":
                                        pass
                    "It's where she belongs":
                        fairyn.c "Really??  What gave you that idea?"
                        $ title = "What gave you that idea?"
                        menu:
                            "The way she's dressed":
                                wt_image ms2_visit_1_3
                                fairyn.c "Are you talking about my Domme outfit?  Maybe you're the one who should be kneeling for me?"
                            "Master M sent her":
                                wt_image ms2_visit_1_3
                                fairyn.c "Technically, M suggested I visit you. He didn't 'send' me, and as much as I like him, I wouldn't kneel for you just because he told me to, anyway."
                                player.c "You admitted you're his slave, at least sometimes."
                                fairyn.c "Not now I'm not."
                                player.c "But you must at least be submissive."
                                wt_image ms2_visit_1_36
                                fairyn.c "Must I??  I wonder why that would be?"
                            "It's where spoiled bitches belong":
                                wt_image ms2_visit_1_36
                                fairyn.c "Don't be silly.  Spoiled bitches belong on pedestals, where men can trip over themselves trying to please us, and women can suck up to us to get into our social circle ... or snipe at us behind our back when we turn them out."
                                wt_image ms2_visit_1_3
                                fairyn.c "I have a really high, marble pedestal, because not only am I pretty, my Daddy gave me a trust fund full of money I used to buy the fanciest pedestal I could find to perch on.  I like it up here.  It's fun."
                            "She did" if fairyn.has_tag('discussed_not_special'):
                                player.c "You did.  The way you're trying to push my buttons.  Bragging about how you get to act like a spoiled bitch and get away with it."
                                wt_image ms2_visit_1_3
                                player.c "You do genuinely love being a brat, I can see that.  But the way you're rubbing it in my face tells me you're trying to provoke a reaction in me."
                                wt_image ms2_visit_1_36
                                fairyn.c "Oh yeah?  What reaction??  Envy?  Jealousy?"
                                $ title = "What reaction did she want from you?"
                                menu:
                                    "Anger":
                                        wt_image ms2_visit_1_36
                                        fairyn.c "Anger?  Really??  If me telling you about how great my life is makes you angry, you need therapy even more than me."
                                        wt_image ms2_visit_1_3
                                        fairyn.c "Do you want the name of my therapist?  He's not very good, but he is expensive, and I like to pay for the best ... sorry, I like to pay for the most expensive option whenever I get the chance."
                                    "Arousal":
                                        player.c "Arousal.  This is your version of foreplay.  You want to turn me on, and it succeeded."
                                        wt_image ms2_visit_1_3
                                        fairyn.c "I'm sure it has, but I didn't come here to turn you on.  And I'm not kneeling for you just because you're sporting a boner."
                                    "Contempt":
                                        player.c "Contempt.  You want me to think you look down at everyone else, hoping that would make me look down at you."
                                        wt_image ms2_visit_1_3
                                        fairyn.c "Sweetie, I do look down at everybody else, including you.  Why would I care if you feel contempt for me?"
                                        player.c "So that I'll treat you the way you want to be treated right now."
                                        fairyn.c "And how's that?"
                                        player.c "As if you're beneath me.  Which, frankly, you are."
                                        wt_image ms2_visit_1_36
                                        fairyn.c "You think so, do you?"
                                        player.c "Yes.  And if you stay on your feet, this conversation is over.  You can walk out that door and go back to your perfect trust fund baby life."
                                        wt_image ms2_visit_1_4
                                        player.c "If you want me to pay you a moment's more attention, you'll get down on your knees where you belong, and I'll decide after that whether I'm going to waste any more time on you."
                                        "Her breathing becomes a little more shallow, and you can sense the sexual tension between you increasing."
                                        wt_image ms2_visit_1_37
                                        "Then she lowers herself to her knees."
                                        wt_image ms2_visit_1_5
                                        player.c "Not on a pedestal any more, are you?"
                                        "Slowly she shakes her head."
                                        add tags 'kneeling' to fairyn
                                    "Pity":
                                        wt_image ms2_visit_1_36
                                        fairyn.c "Pity?  What gave you that idea??"
                                        player.c "You're a poor little trust fund baby.  You keep everybody at an emotional distance because you can't handle intimacy.  This little act of yours, it's a cry for help."
                                        wt_image ms2_visit_1_40
                                        player.c "You want to be happy with your life, but you feel hollow inside, and you're desperate for someone to notice and help you."
                                        "She stays silent for a moment, and you can tell she's seething a little under the surface.  You may be on to something, but it's something she's in no mood to admit.  And it's definitely not the reaction she was hoping to get out of you."
                                        wt_image ms2_visit_1_38
                                        "Eventually, she finds her tongue and snaps back a retort."
                                        fairyn.c "Wrong, loser.  Clearly you don't know women as well as you think you do."
                            "Maybe you need to learn more about her" if not fairyn.has_tag('discussed_not_special'):
                                pass
            "Why are you here?" if not fairyn.has_tag('fairyn_convo_why'):
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_3
                fairyn.c "Guess why I'm here."
                $ title = "What's your guess?"
                menu menu_fairyn_convo_why:
                    "You thought I was a tailor" if not fairyn.has_tag('discussed_tailor'):
                        wt_image ms2_visit_1_38
                        fairyn.c "A tailor?  Why would I want a tailor??"
                        player.c "To fix the holes in your outfit."
                        if fairyn.has_tag('kneeling'):
                            wt_image ms2_visit_1_2
                        else:
                            wt_image ms2_visit_1_1
                        "She laughs."
                        fairyn.c "I'm starting to like you.  Can you guess why I'm not wearing a bra?"
                        player.c "A lot of things come to mind."
                        fairyn.c "I meant a funny reason.  It's because Brenda the Bra Fitter wouldn't sell me one."
                        fairyn.c "While my bank account is large enough to pay her, apparently my other 'assets' aren't big enough to attract her services."
                        if chelsea.bra_fitting_status > 1:
                            "You suspect this isn't the first time Brenda's been the butt of a joke amongst the monied ladies around town.  It wasn't really funny, but Fairyn seems to think it's a hoot, as she keeps giggling to herself."
                        else:
                            "You have no idea who Brenda the Bra Fitter is or why that 'joke' is meant to be funny, but Fairyn seems to think it's a hoot, as she keeps giggling to herself."
                        if fairyn.initial_arousal < 1:
                            $ fairyn.initial_arousal = 1
                        add tags 'discussed_tailor' to fairyn
                    "You're looking for no strings sex":
                        if fairyn.has_tag('kneeling'):
                            wt_image ms2_visit_1_2
                        else:
                            wt_image ms2_visit_1_3
                        if player.has_tag('supersexy'):
                            fairyn.c "Hmmm. I bet women come to you looking for that a lot."
                            wt_image ms2_visit_1_9
                            fairyn.c "To be honest, though, I had no idea how hot you were until I showed up, so I guess that's not really why I'm here."
                        else:
                            "She chuckles."
                            fairyn.c "Do you think I have trouble finding that?  No offense, but if that's what I was looking for, I could find a better looking boy toy than you to give it to me."
                    "Master M told you I would dominate you" if not fairyn.has_tag('discussed_m'):
                        if fairyn.has_tag('kneeling'):
                            wt_image ms2_visit_1_2
                        else:
                            wt_image ms2_visit_1_3
                        fairyn.c "Close.  What he actually said is that you may be able to dominate me.  Jury's still out on whether you can."
                        player.c "Has he dominated you?"
                        fairyn.c "Oh, yeah!!  Don't know if you're as much of a man as him, though?"
                        $ title = "What now?"
                        menu:
                            "Brag":
                                player.c "I do this for a living.  Even M had to send one of his slaves to be me for correction."
                                wt_image ms2_visit_1_40
                                fairyn.c "So he's man enough to admit he when he needs help, and you brag about that to try and impress women?  Color me not impressed."
                                if fairyn.initial_arousal > 0:
                                    "The rapport you were starting to build with her has dissipated."
                                    $ fairyn.initial_arousal = 0
                            "Compliment Master M":
                                if player.has_tag('club_access'):
                                    if diamond.training_result == 6 or diamond.training_result == 8:
                                        player.c "From what I hear around the Club, women do seem to enjoy M's company."
                                        if fairyn.has_tag('kneeling'):
                                            wt_image ms2_visit_1_2
                                        else:
                                            wt_image ms2_visit_1_36
                                        fairyn.c "You're a member of the Club?  He didn't mention that.  I haven't been there for a while. I must drop by again someday."
                                        wt_image ms2_visit_1_9
                                        fairyn.c "Maybe I can thank him while I'm there, for sending me to you.  That is, if you're as good as he seems to think you are."
                                    else:
                                        player.c "From what I hear around the Club, women do seem to enjoy M's company."
                                        if fairyn.has_tag('kneeling'):
                                            wt_image ms2_visit_1_2
                                        else:
                                            wt_image ms2_visit_1_36
                                        fairyn.c "You're a member of the Club?  He didn't mention that. I haven't been there for a while. I must drop by again someday."
                                        wt_image ms2_visit_1_9
                                        fairyn.c "Maybe I can thank him while I'm there, for sending me to you.  That is, if you show the potential he thinks you have."
                                else:
                                    if diamond.training_result == 6 or diamond.training_result == 8:
                                        player.c "I don't know much about M, but he seems.to understand women."
                                        fairyn.c "Funny, he said something similar about you."
                                    else:
                                        player.c "I don't know much about M, but he seems.to understand women."
                                        fairyn.c "He said he didn't know much about you either, other than he thinks you're trying to learn how to understand women."
                                if fairyn.initial_arousal < 1:
                                    $ fairyn.initial_arousal = 1
                        add tags 'discussed_m' to fairyn
                    "You want me to treat you like a spoiled brat":
                        if fairyn.has_tag('kneeling'):
                            wt_image ms2_visit_1_2
                        else:
                            wt_image ms2_visit_1_3
                        fairyn.c "I am a spoiled brat, so, by definition, I'm always being treated like one."
                        $ title = "What now?"
                        menu:
                            "You're not treated the way you want to be":
                                player.c "You're not treated the way you want to be."
                                if fairyn.has_tag('kneeling'):
                                    wt_image ms2_visit_1_2
                                else:
                                    wt_image ms2_visit_1_3
                                fairyn.c "That's true.  Not all the time, anyway.  Sometimes women don't bitch behind my back about how pretty I am, even though I wish they would."
                                if fairyn.has_tag('kneeling'):
                                    wt_image ms2_visit_1_2
                                else:
                                    wt_image ms2_visit_1_36
                                fairyn.c "And sometimes men don't grovel before me when I'm out in public or fight over who gets to open the door for me, although they usually do."
                                wt_image ms2_visit_1_9
                                fairyn.c "Sometimes store clerks don't even fawn over me to try and win my business when I'm out shopping, although to be honest, that almost never happens."
                                $ title = "What do you say?"
                                menu:
                                    "Sounds tough":
                                        player.c "Sounds tough. I hope you have a therapist to help you with the emotional anguish."
                                        if fairyn.has_tag('kneeling'):
                                            wt_image ms2_visit_1_2
                                        else:
                                            wt_image ms2_visit_1_1
                                        "She laughs."
                                        fairyn.c "I do, actually!  You might make a good therapist yourself."
                                        if fairyn.initial_arousal < 1:
                                            $ fairyn.initial_arousal = 1
                                    "That's not really how you want to be treated":
                                        player.c "That's not really how you want to be treated."
                                        if fairyn.has_tag('kneeling'):
                                            wt_image ms2_visit_1_2
                                        else:
                                            wt_image ms2_visit_1_36
                                        fairyn.c "Uh yeah, it is!"
                                        $ title = "What now?"
                                        menu:
                                            "Not here it isn't":
                                                player.c "Not here it isn't."
                                                if fairyn.has_tag('kneeling'):
                                                    wt_image ms2_visit_1_2
                                                else:
                                                    wt_image ms2_visit_1_3
                                                fairyn.c "Really?  And why would that be?"
                                                $ title = "What do you say?"
                                                menu:
                                                    "You want to be punished for being bad":
                                                        player.c "You want to be punished for being bad."
                                                        if fairyn.has_tag('kneeling'):
                                                            wt_image ms2_visit_1_2
                                                        else:
                                                            wt_image ms2_visit_1_36
                                                        fairyn.c "No, not really.  It's fun being a pampered bitch.  I don't want to be punished for having fun.  I don't really want to be punished at all."
                                                    "You don't want to be special right now":
                                                        player.c "You don't want to be special right now.  You spend your whole life on a pedestal, and you like it.  Once in a while, though, you want to be taken off the pedestal and put down in the dirt with us regular folk."
                                                        if fairyn.has_tag('kneeling'):
                                                            wt_image ms2_visit_1_5
                                                        else:
                                                            wt_image ms2_visit_1_4
                                                        player.c "Except you don't exactly want to be treated regular, either.  Not right now.  I think while you're here we should aim for a little lower than regular."
                                                        wt_image ms2_visit_1_9
                                                        "Her breathing gets a little more shallow and her nipples stiffen."
                                                        fairyn.c "If you say so."
                                                        if fairyn.initial_arousal < 2:
                                                            $ fairyn.initial_arousal = 2
                                                        else:
                                                            $ fairyn.initial_arousal += 1
                                                        add tags 'discussed_not_special' 'fairyn_convo_why' to fairyn
                                                    "You want a father figure":
                                                        player.c "You want a father figure, and you're hoping to find one here."
                                                        wt_image ms2_visit_1_40
                                                        fairyn.c "Gawd no!  Ewww!!!  I don't even like my father.  I certainly don't fantasize about him.  Gross!!"
                                                        if fairyn.has_tag('kneeling'):
                                                            wt_image ms2_visit_1_5
                                                        else:
                                                            wt_image ms2_visit_1_36
                                                        fairyn.c "And I don't need a strong man to control me, if that's what you're thinking.  I like my life.  I have fun.  I get to do almost anything I want."
                                                        fairyn.c "The last thing I need is some man telling me what to do or expecting me to be home on time and generally messing up my fun."
                                                    "Choose a new approach":
                                                        pass
                                            "Not deep down it isn't":
                                                if fairyn.has_tag('kneeling'):
                                                    wt_image ms2_visit_1_2
                                                else:
                                                    wt_image ms2_visit_1_3
                                                fairyn.c "Yup, it is.  100% shallow, spoiled bitch here, in the flesh and proud of it!"
                                            "Choose a new approach":
                                                pass
                                    "Choose a new approach":
                                        pass
                            "You don't really want to stay a brat":
                                player.c "You don't really want to stay a brat.  You're looking for someone to help you change your ways."
                                if fairyn.has_tag('kneeling'):
                                    wt_image ms2_visit_1_2
                                else:
                                    wt_image ms2_visit_1_3
                                fairyn.c "Au contraire, I'm a spoiled bitch and I love it."
                            "Choose a new approach":
                                pass
            "Will you Domme me?" if not fairyn.has_tag('fairyn_convo_domme') and not fairyn.has_tag('kneeling'):
                wt_image ms2_visit_1_4
                fairyn.c "Is that what you'd like?"
                $ title = "Is that what you'd like?"
                menu:
                    "Yes, I want her to take control":
                        player.c "Yes. I'd love it if you took control."
                        wt_image ms2_visit_1_36
                        fairyn.c "I bet you would.  You want me to make all the decisions, don't you?  All you want to do is follow my instructions."
                        $ title = "Is that what you want?"
                        menu:
                            "Yes, tell me what to do":
                                player.c "Yes. Tell me what to do."
                                wt_image ms2_visit_1_36
                                if player.has_tag('supersexy'):
                                    fairyn.c "No.  When M suggested I should visit you, it wasn't to have you grovel for me.  Men grovel for me all the time.  Even good looking ones, like you."
                                else:
                                    fairyn.c "No.  When M suggested I should visit you, it wasn't to have you grovel for me.  Men grovel for me all the time.  Better looking men than you, frankly."
                                wt_image ms2_visit_1_3
                                fairyn.c "It can be kind of fun, especially when they get those hurt puppy dog eyes when they realize all the attention they've been giving me gets them ... nothing."
                                wt_image ms2_visit_1_36
                                fairyn.c "But I don't need to Domme a guy to wrap him around my baby finger.  And unlike a real Domme, what I enjoy most is breaking their hearts, not their balls."
                                $ title = "What now?"
                                menu:
                                    "Beg her to Domme you":
                                        player.c "Please. I'm begging you. Tell me what you want me to do."
                                        player.c "I'll be a good boy.  I'll do everything you say.  Please, Mistress.  Please??"
                                        wt_image ms2_visit_1_40
                                        fairyn.c "This isn't why I'm here."
                                        wt_image ms2_visit_1_6
                                        "She turns and leaves."
                                        $ fairyn.temporary_count = 2
                                    "Choose a new approach":
                                        pass
                            "No, not really":
                                player.c "No, not really.  I'm just trying to figure out your motivation for being here."
                                wt_image ms2_visit_1_3
                                if player.has_tag('supersexy'):
                                    fairyn.c "It wasn't to have you grovel for me.  Men grovel for me all the time.  Even good looking ones, like you."
                                else:
                                    fairyn.c "It wasn't to have you grovel for me.  Men grovel for me all the time.  Better looking men than you, frankly."
                                fairyn.c "It can be kind of fun, especially when they get those hurt puppy dog eyes when they realize all the attention they've been giving me gets them ... nothing."
                                wt_image ms2_visit_1_36
                                fairyn.c "But I don't need to Domme a guy to wrap him around my baby finger.  And unlike a real Domme, what I enjoy most is breaking their hearts, not their balls."
                    "No, not really":
                        player.c "No, not really. I'm just trying to figure out your motivation for being here."
                        wt_image ms2_visit_1_3
                        if player.has_tag('supersexy'):
                            fairyn.c "It wasn't to have you grovel for me.  Men grovel for me all the time.  Even good looking ones, like you."
                        else:
                            fairyn.c "It wasn't to have you grovel for me. Men grovel for me all the time.  Better looking men than you, frankly."
                        fairyn.c "It can be kind of fun, especially when they get those hurt puppy dog eyes when they realize all the attention they've been giving me gets them ... nothing."
                        wt_image ms2_visit_1_36
                        fairyn.c "But I don't need to Domme a guy to wrap him around my baby finger.  And unlike a real Domme, what I enjoy most is breaking their hearts, not their balls."
                add tags 'fairyn_convo_domme' to fairyn
            "Touch yourself" if not fairyn.has_tag('fairyn_convo_touch'):
                if fairyn.initial_arousal == 0:
                    if fairyn.has_tag('kneeling'):
                        wt_image ms2_visit_1_2
                        fairyn.c "Did you really get me down here just to let me have a good time?  I appreciate the offer, but I'm perfectly happy waiting until I'm at home on my bed tonight before I masturbate."
                        $ title = "What now?"
                        menu:
                            "You didn't mean a pleasurable touch":
                                call fairyn_convo_not_pleasurable_touch from _call_fairyn_convo_not_pleasurable_touch
                            "Choose a new approach":
                                pass
                    else:
                        wt_image ms2_visit_1_3
                        fairyn.c "Gee, thanks for the invitation, but I can do that at home on my bed tonight, thinking about all the losers I met today who would have loved to put their mouths where I'm putting my fingers."
                elif fairyn.initial_arousal == 1:
                    if player.has_tag('supersexy'):
                        wt_image ms2_visit_1_9
                        fairyn.c "Mmmmm.  You're hot, and I kind of like you, and the thought of you watching me touch myself ... it turns me on."
                        if fairyn.has_tag('kneeling'):
                            fairyn.c "This isn't what I had in mind today, but if it's what you want, I'll masturbate for you."
                            $ title = "Is this what you want?"
                            menu:
                                "Yes, watch her to masturbate":
                                    $ fairyn.temporary_count = 4
                                "You didn't mean a pleasurable touch":
                                    call fairyn_convo_not_pleasurable_touch from _call_fairyn_convo_not_pleasurable_touch_1
                                "No, choose a new approach":
                                    pass
                        else:
                            wt_image ms2_visit_1_3
                            fairyn.c "This isn't what I had in mind today, but if it's what you want, I'll make a deal with you."
                            wt_image ms2_visit_1_36
                            fairyn.c "If you take out your cock and stroke it for me, I'll masturbate for you."
                            $ title = "Is this what you want?"
                            menu:
                                "Yes, watch her to masturbate":
                                    $ fairyn.temporary_count = 4
                                "No, choose a new approach":
                                    pass
                    elif fairyn.has_tag('kneeling'):
                        if player.has_tag('dominant'):
                            wt_image ms2_visit_1_9
                            fairyn.c "Is that what you want to do with me?  Watch as you make me pleasure myself?"
                            $ title = "Is this what you want?"
                            menu:
                                "Yes, watch her to masturbate":
                                    $ fairyn.temporary_count = 4
                                "You didn't mean a pleasurable touch":
                                    call fairyn_convo_not_pleasurable_touch from _call_fairyn_convo_not_pleasurable_touch_2
                                "No, choose a new approach":
                                    pass
                        else:
                            wt_image ms2_visit_1_2
                            fairyn.c "Did you really get me down here just to let me have a good time?"
                            fairyn.c "I appreciate the offer, but I'm perfectly happy waiting until I'm at home on my bed tonight before I masturbate."
                            $ title = "What now?"
                            menu:
                                "You didn't mean a pleasurable touch":
                                    call fairyn_convo_not_pleasurable_touch from _call_fairyn_convo_not_pleasurable_touch_3
                                "Choose a new approach":
                                    pass
                    else:
                        wt_image ms2_visit_1_3
                        fairyn.c "I like you, but I'm not going to touch myself while you watch.  I can do that at home on my bed tonight, thinking about all the losers I met today who would have loved to put their mouths where I'm putting my fingers."
                elif fairyn.initial_arousal > 1:
                    wt_image ms2_visit_1_9
                    if fairyn.has_tag('kneeling'):
                        fairyn.c "Is that what you want to do with me?  Watch as you make me pleasure myself?"
                    else:
                        fairyn.c "This isn't what I had in mind today, but if it's what you want, I'll make a deal with you."
                        wt_image ms2_visit_1_36
                        fairyn.c "If you take out your cock and stroke it for me, I'll masturbate for you."
                    $ title = "Is this what you want?"
                    menu:
                        "Yes, watch her to masturbate":
                            $ fairyn.temporary_count = 4
                        "You didn't mean a pleasurable touch":
                            call fairyn_convo_not_pleasurable_touch from _call_fairyn_convo_not_pleasurable_touch_4
                        "No, choose a new approach":
                            pass
            "What do you have in your bag?":
                if fairyn.initial_arousal < 2:
                    if fairyn.has_tag('kneeling'):
                        wt_image ms2_visit_1_2
                    else:
                        wt_image ms2_visit_1_3
                    fairyn.c "Nothing you need right now."
                elif fairyn.initial_arousal == 2 and not fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_3
                    fairyn.c "Nothing I'm ready to let you use on me.  At least not yet."
                else:
                    wt_image ms2_visit_1_9
                    fairyn.c "A gag, in case you're tired of listening to me."
                    fairyn.c "A paddle, in case you want to hurt me."
                    fairyn.c "And condoms, for when you're ready to fuck me."
                    $ title = "What now?"
                    menu menu_fairyn_convo_bag:
                        "Ask what holes you can use" if not fairyn.has_tag('fairyn_convo_bag_holes'):
                            player.c "What holes of yours can I use?"
                            wt_image ms2_visit_1_2
                            fairyn.c "Whichever ones you want.  You don't have to ask my permission for anything for the rest of the time I'm here.  Just don't do anything that would send me to the hospital."
                            add tags 'fairyn_convo_bag_holes' to fairyn
                            jump menu_fairyn_convo_bag
                        "Use the gag":
                            $ fairyn.temporary_count = 6
                        "Use the paddle":
                            $ fairyn.temporary_count = 7
                        "Use both the gag and the paddle":
                            $ fairyn.temporary_count = 8
                        "Just fuck her":
                            $ fairyn.temporary_count = 9
                        "Tell her to go" if not fairyn.has_tag('fairyn_convo_bag_tell_go'):
                            player.c "You can go now."
                            if fairyn.has_tag('kneeling'):
                                wt_image ms2_visit_1_5
                            else:
                                wt_image ms2_visit_1_4
                            fairyn.c "Go?"
                            player.c "You heard me."
                            wt_image ms2_visit_1_38
                            fairyn.c "But, I'm ready to submit to you.  You don't even have to ask my permission.  Do whatever you want to me, if it doesn't send me to the hospital.  Fuck me in whatever hole you want to use."
                            add tags 'fairyn_convo_bag_tell_go' 'fairyn_convo_bag_holes' to fairyn
                            jump menu_fairyn_convo_bag
                        "Send her home" if fairyn.has_tag('fairyn_convo_bag_tell_go'):
                            $ fairyn.temporary_count = 5
                        "Nothing yet":
                            pass
            "I don't work for free" if fairyn.paying_you == 0:
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_2
                else:
                    wt_image ms2_visit_1_3
                fairyn.c "What do you mean?"
                player.c "I mean, I do this for a living.  Help women with their issues.  If you want some of my time, you need to pay me for it."
                wt_image ms2_visit_1_9
                fairyn.c "Hmmmm.  That's kind of exciting.  Okay, I'll make you a deal.  You figure out what I want and give it to me, and I'll pay you 50."
                $ fairyn.paying_you = 1
            "You should leave" if not fairyn.has_tag('fairyn_convo_leave'):
                wt_image ms2_visit_1_38
                fairyn.c "What??  Why?"
                player.c "I've had enough of you.  I'm not wasting one minute more on your bullshit."
                if fairyn.has_tag('kneeling'):
                    wt_image ms2_visit_1_39
                    fairyn.c "Fine!  Fuck you!!"
                    "She stands up and storms off, fuming."
                else:
                    wt_image ms2_visit_1_6
                    fairyn.c "Fine!  Fuck you!!"
                    "She turns and storms off, fuming."
                $ fairyn.temporary_count = 3
                add tags 'fairyn_convo_leave' to fairyn
    # from here we jump to the correct ending scene based on what temporary_count is now
    return

label fairyn_convo_chauvinism_chain:
    wt_image ms2_visit_1_4
    fairyn.c "Do you really believe that?"
    $ title = "Do you?"
    menu:
        "Yes":
            wt_image ms2_visit_1_4
            fairyn.c "Really?  That's completely chauvinistic."
            $ title = "Is it?"
            menu:
                "Yes, it is":
                    wt_image ms2_visit_1_9
                    if fairyn.has_tag('know_name'):
                        fairyn.c "So even though you just met me, you think I belong on my knees in front of you, just because you're a man and I'm a woman?"
                    else:
                        fairyn.c "So even though you just met me, and don't even know my name, you think I belong on my knees in front of you, just because you're a man and I'm a woman?"
                    wt_image ms2_visit_1_4
                    if player.has_tag('wealthy'):
                        fairyn.c "Wouldn't there be something special to you about earning my submission?  I'm not exactly any woman.  I can see you have a bit of money, more than most people, probably, but I bet the money my Daddy gives me would make you look like a pauper."
                    else:
                        fairyn.c "Wouldn't there be something special to you about earning my submission?  I'm not exactly any woman.  I probably have more money than you've ever imagined."
                    $ title = "What now?"
                    menu:
                        "Would you lend some to me?":
                            player.c "In that case, would you lend me some before you kneel?  Or afterwards."
                            wt_image ms2_visit_1_1
                            "She laughs."
                            fairyn.c "I'm starting to like you.  You're still going to need to do better, though, if you want me on my knees."
                            if fairyn.initial_arousal < 1:
                                $ fairyn.initial_arousal = 1
                        "Yes, you would be special":
                            player.c "Of course you'd be special.  Every woman who submits to me is special in her own way."
                            wt_image ms2_visit_1_3
                            "She smiles."
                            fairyn.c "In that case, sweetie, you'd better figure out what you need to do to convince special old me that I should be on my knees in front of you."
                        "You're just another woman":
                            player.c "Actually, you are just another woman.  I don't care about your money, or who you think you are."
                            wt_image ms2_visit_1_4
                            fairyn.c "Really?  So all you need to know is my gender to make you think that my place is on my knees in front of you?"
                            $ title = "Is it?"
                            menu:
                                "Yes, that's all":
                                    wt_image ms2_visit_1_36
                                    fairyn.c "I should laugh at you.  Or slap you.  Maybe both."
                                    player.c "Are you going to do either of those things?"
                                    wt_image ms2_visit_1_9
                                    fairyn.c "If I was anywhere else, yes.  If there was anyone else around, yes.  If knowing that you're a chauvinistic pig who treats all women like a commodity wasn't turning me on, yes."
                                    wt_image ms2_visit_1_3
                                    fairyn.c "But, no, I guess I'm not."
                                    player.c "What are you going to do?"
                                    wt_image ms2_visit_1_37
                                    "She lowers herself to her knees."
                                    player.c "You realize you just proved me right?"
                                    wt_image ms2_visit_1_5
                                    "She says nothing, but you can sense the sexual tension between you increasing."
                                    add tags 'kneeling' 'discussed_not_special' to fairyn
                                "Choose a new approach":
                                    pass
                "No, it isn't":
                    player.c "No, it isn't, it's just..."
                    wt_image ms2_visit_1_6
                    fairyn.c "Okay, I'm not going to stand here and debate the definition of chauvinism with you.  See ya!"
                    $ fairyn.temporary_count = 2
        "No":
            player.c "No, but did it sound good?"
            wt_image ms2_visit_1_1
            "She laughs."
            fairyn.c "I'm starting to like you. You're still going to need to do better, though, if you want me on my knees."
            if fairyn.initial_arousal < 1:
                $ fairyn.initial_arousal = 1
        "Maybe":
            player.c "Maybe.  Did it sound good?"
            wt_image ms2_visit_1_1
            "She laughs."
            fairyn.c "I'm starting to like you. You're still going to need to do better, though, if you want me on my knees."
            if fairyn.initial_arousal < 1:
                $ fairyn.initial_arousal = 1
    return

label fairyn_convo_not_pleasurable_touch:
  player.c "I didn't mean for you to enjoy yourself.  Pinch your nipple."
  wt_image ms2_visit_1_16
  fairyn.c "Mmmm ... this is nice."
  player.c "Pinch harder."
  wt_image ms2_visit_1_9
  fairyn.c "oooo ... sorry to break it to you, sweetie, but this is still pleasurable."
  player.c "Harder"
  wt_image ms2_visit_1_16
  fairyn.c "ouch"
  player.c "Harder"
  wt_image ms2_visit_1_17
  fairyn.c "Ow!"
  wt_image ms2_visit_1_9
  fairyn.c "Wow, this is starting to feel interesting."
  player.c "Do it again, harder still."
  wt_image ms2_visit_1_16
  fairyn.c "Oww!!"
  player.c "I said harder.  Pinch it the way you'd imagine I'd do it to you."
  wt_image ms2_visit_1_17
  fairyn.c "Oowwww!!"
  "She's breathing hard, and not just from the pain in her nipple."
  if fairyn.initial_arousal < 2:
    $ fairyn.initial_arousal = 2
  elif fairyn.initial_arousal == 2:
    $ fairyn.initial_arousal = 3
  add tags 'fairyn_convo_touch' to fairyn
  return

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
