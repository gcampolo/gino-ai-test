## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou or wifetrainer

# Package Register
# register_package gloria name "Gloria, The Club President's Wife" description "Allows Gloria to be a minor character." dependencies core club
register gloria_pregame 11 in core as "Gloria the Club President's Wife"

# Pregame
label gloria_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Gloria the Club President's Wife (Kelly Madison)")]

    ## Character Definition
    gloria = Person(Character("Gloria", who_color="#804040", what_color="#804040", window_background = gui.dialogue_background_dark_font_color), "gloria", cut_portrait = True, prefix = "", suffix = "the Club President's Wife", resistance = 0, hypno_trigger_sessions_threshold = 3)
    gloria.trigger_phrase = "A life of privilege is best spent on your knees"

    # Other Characters
    # 0,0,160
    club_president = Person(Character("Club President", who_color="#0000A0", what_color="#0000A0", window_background = gui.dialogue_background_dark_font_color), "club_president", cut_portrait = False, prefix = "The", suffix = "")
    # Teal
    maria_gloria = Character("Maria", who_color="#00c4c4", what_color="#00c4c4")

    ## Actions
    gloria.action_talk = gloria.add_action("Talk to her", label="_talk")
    gloria.add_hypno_actions([], implant = False) # note: implant refers to creating a separate implant trigger action, which is not necessary as it happens automatically
    gloria.action_contact = living_room.add_action("Contact the Club President's Wife", label = gloria.short_name + "_contact", context = "_contact_other", condition = "gloria.can_be_interacted and ((gloria.session == 8 or gloria.has_tag('available_for_visit')) or (gloria.session > 4 and gloria.has_tag('something_to_discuss')))")

    ## Tags
    # Common Character Tags
    gloria.add_tags('can_be_in_club', 'no_hypnosis', 'likes_boys', 'likes_girls', 'random_number')
    club_president.add_tags('can_be_in_club', 'no_hypnosis', 'likes_girls')

    ## Locations
    gloria_house = Location ("Gloria's House", 'gh', cut_portrait = True, area = 'house', unseen = True)


    ## Other
    gloria.change_status("minor_character")
    club_president.change_status("minor_character")



    # Start Day Events
    start_day_labels.append('gloria_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    #gloria.add_stats_with_value('temporary_count') # not needed as auto-added
    gloria.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_masturbation_count', 'hypno_orgasm_count', 'hypno_sex_count','hypno_swallow_count', 'random_number')
    gloria.hypno_trigger_sessions_threshold = 3 # change from default of 5; this is the number of times you need to hypnotize her to plant her trigger

    # Character Specific Variables
    gloria.add_stats_with_value('discussed_barista', 'discussed_bimbo', 'discussed_principal', 'session', 'ball_outfit', 'house_outfit', 'first_session_test', 'show_count', 'show_or_ball', 'show_week', 'solution_status')
    # code for gloria.session: 0: not open; 1: sex session only on her visit; 2: training visit; 3: sex or training session failed, not continuing; 4: sex session complete, willing for more; 5: training succeeded, working on solving Club Pres problem
    # 6: training visit after successful sex session; 7: training succeeded, almost solved Club Pres's problem using Gloria as either Teaching Aide or Club Social Coordinator; 8: Club Pres's problem solved
    club_president.add_stats_with_value('discussion_pending', 'discussion_week', 'showgirl_reward_count', 'rewards_pending')
    club_president_discussion_reason_list = ['gloria']
    club_president_reward_reason_list = ['showgirl', 'bree_maid', 'rep_from_club_dalliance', 'sarah_showgirl', 'alexis_serving']
    club_president_reward_description_list = ['love_potion', 'ring_sexuality']
    club_president_special_reward_description_list = ['transformation_potion']

    ######## EXPANDABLE MENUS #######
    ## Club President Reward Menu
    club_president_reward_menu = ExpandableMenu("What do you want?", cancelable = False)
    club_president.choice_club_president_reward_menu_hypnotize_him = club_president_reward_menu.add_choice("Hypnotize Him", "club_president_reward_menu_hypnotize_him", condition = "player.hypnosis_level > 0 and not club_president.has_tag('tried_hypnosis')")
    club_president.choice_club_president_reward_menu_his_wife = club_president_reward_menu.add_choice("His Wife", "club_president_reward_menu_his_wife", condition = "gloria.session == 0 or gloria.session == 4")
    club_president.choice_club_president_reward_menu_love_potion = club_president_reward_menu.add_choice("Love Potion", "club_president_reward_menu_love_potion")
    club_president.choice_club_president_reward_menu_ring_sexuality = club_president_reward_menu.add_choice("Ring of Sexuality", "club_president_reward_menu_ring_sexuality", condition = "not club_president.has_tag('ring_sexuality_granted')")
    club_president.choice_club_president_reward_menu_transformation_potion = club_president_reward_menu.add_choice("Transformation Potion", "club_president_reward_menu_transformation_potion", condition = "club_president.has_tag('special_reward') and not club_president.has_tag('transformation_potion_granted')")
    club_president.choice_club_president_reward_menu_janice_retainer = club_president_reward_menu.add_choice("Ask about getting Janice the Lawyer on retainer", "club_president_reward_menu_janice_retainer", condition = "janice.has_tag('asked_about_hiring') and not player.has_tag('lawyer_on_retainer')")
    club_president.choice_club_president_reward_menu_money = club_president_reward_menu.add_choice("Money (200)", "club_president_reward_menu_money", condition = "club_president.has_tag('special_reward')")

  return

# Display Portrait
# CHARACTER: Display Portrait
label gloria_update_media:
  if current_location == club:
    if gloria.has_tag('first_club_visit'):
      $ gloria.change_image('club_pres_wife_3')
    elif gloria.has_tag('trigger_implanted') or gloria.session > 6:
      $ gloria.change_image('club_pres_wife_2')
    else:
      $ gloria.change_image('club_pres_wife_1')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label gloria_examine:
    "An elegantly - and sexily - dressed woman."
    if gloria.has_tag('trigger_implanted'):
        "You have implanted a hypnotic trigger in her."

    return

label club_president_examine:
    sys "Why, and how, did you summon this character?? - a4hryou"
    return

# Talk to Character
label gloria_talk:
    if current_location == club:
        wt_image gloria.image
        gloria.c "Hello.  I hope you're enjoying your time at the Club."
        $ title = "Ask her about?"
        menu gloria_talk_menu:
            ## this was one option DB suggested for adding conversation topics remotely
            "People in the Club":
                call choose_people([person for person in get_people(tagged_with_any = ['gloria_club_talk_possible']) if person.in_area('club')], "Ask her about whom?") from _call_choose_people
                if current_target is not gloria:
                    call safe_call(current_target.short_name + '_gloria_club_talk_option') from _call_safe_call_4
                    $ current_target = gloria
                else:
                    $ title = "Ask her about?"
                    jump gloria_talk_menu

            # "[cassandra.full_name]" if cassandra.location == club:
            #     if cassandra.independent_encounter_status > 1:
            #         gloria.c "It's so nice to see her happy for a change. Too bad she won't bring her new girlfriend around. I know some of the other Club members would love to meet her, but Cassandra seems rather possessive of her new toy."
            #     if cassandra.has_tag('introduced'):
            #         gloria.c "I'm not sure what I can tell you? I don't know much about her. I just wish she wouldn't mope so much. People come here for a good time, they don't want to see other people unhappy."
            #     else:
            #         gloria.c "That's Cassandra. Nice lady, I suppose. I don't know much about her. I just wish she wouldn't mope so much. People come here for a good time, they don't want to see other people unhappy."
            #         $ cassandra.change_full_name("", "Cassandra", "") # Domme part doesn't open until you introduce yourself
            # "[janice.full_name]" if janice.location == club:
            #     gloria.c "Our Club lawyer? She's top notch. We never have any problems. Janice makes sure of that."
            #     gloria.c "And when my husband says that anything that happens here stays here ... well, let's just say that Janice is very good at making sure members understand the consequences of stepping out of line."
            #     if player.lawyer_office_visit_count == 0:
            #         gloria.c "You should hire her to be your lawyer, if you can. She's very, very expensive, but well worth it. Her firm's located in the big office tower downtown."
            #         $ janice.change_full_name("", "Janice", "the Lawyer")
            # "[marilyn.full_name]" if marilyn.location == club:
            #     gloria.c "She's an important sponsor of the Club. Without her and a couple of others, the Club wouldn't exist, and my husband wouldn't have his job."
            #     gloria.c "I'm grateful to her, of course, for helping to create this place and putting my husband in charge."
            #     gloria.c "Still, if I were you, I'd suggest you not get too close. And whatever you do, don't cross her."
            #     player.c "But what's her story? What kind of business does she run?"
            #     gloria.c "Some questions are better left unasked."
            # "[master_m.full_name]" if master_m.location == club:
            #     gloria.c "Master M? That's what everyone calls him. He has a real name, of course, but I'd have to check the Club records to remember what it is."
            #     gloria.c "He's been a Club member a long time. Very popular with the wives of other members. They like to hang around him, hoping he'll pick them out for a spanking."
            #     gloria.c "Most of them aren't even submissives, they just like the idea of being disciplined by the Club's best looking Dom."
            #     gloria.c "Not that they could take his real discipline. They think a swat on the rear while bent over his knee is a punishment. They haven't seen the rears of his slavegirls after a real punishment."
            #     gloria.c "Mostly he ignores them and spends his time chatting with his friends at the Club."
            #     $ master_m.name = "Master M"

            "How can I help the Club?":
                player.c "You have a great spot here.  Is there any way I could help out?"
                gloria.c "How sweet of you! We could always use new Showgirls or Showboys, if you happen to know of any.  Our patrons love to see new talent perform."
                gloria.c "And some of our members like to provide their - how should I put this? - more {i}subordinate{/i} partners to help keep the Club neat and tidy."
                gloria.c "It's unpaid work, of course, but it gives them something to do when you're out and about or dallying with someone else."
            "How do I get to know you better?" if gloria.session < 3 and gloria.location == club:
                if gloria.session == 1 or gloria.session == 2:
                    if not gloria.has_tag('number_given'):
                        add tags 'number_given' to gloria
                        player.c "I'd love to get to know you better, Gloria."
                        if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                            wt_image club_pres_wife_4
                        gloria.c "How sweet! My husband told me you asked about spending time with me. I have to say I'm quite surprised he agreed, but I'm not disappointed. I'd love to get to know you better, too."
                        gloria.c "Not here though. I can't be seen 'fraternizing' with the membership. It might put my husband in an awkward position, say if you and another member got into some dispute."
                        gloria.c "Here's my number. Call me sometime when you're at home, and I'll be sure to drop by."
                        if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                            wt_image club_pres_wife_5
                        gloria.c "I do hope you're able to impress me.  I've heard interesting things about you, but I do wonder if you have enough class to justify your reputation?"
                        add tags 'available_for_visit' to gloria
                        if gloria.session == 2:
                            "Sounds like Gloria is going to be judging you.  Her husband wants an outcome from this session, too."
                        else:
                            "Sounds like Gloria is going to be judging you."
                    else:
                        if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                            wt_image club_pres_wife_5
                        gloria.c "Don't forget to give me a call.  Don't keep me waiting.  I hate that."
                        if gloria.session == 2:
                            "You already have her number.  Now you need to give her a call from home and ask her to visit you.  Her husband is also waiting to hear the outcome of her visit."
                        else:
                            "You already have her number.  Now you need to give her a call from home and ask her to visit you."
                else:
                    player.c "I'd love to get to know you better, Gloria."
                    if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                        wt_image club_pres_wife_4
                    gloria.c "How sweet!  I'm afraid I don't play with members, though. You understand. What with my husband's position at the Club."
                    if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                        wt_image club_pres_wife_5
                    gloria.c "Of course, if you talk to him and he gives permission, I wouldn't mind spending some time with you. I've heard interesting things about you. I wonder if you've got the right degree of ... 'class' to entertain me?"
                    player.c "How do I get in touch with your husband?"
                    wt_image gloria.image
                    gloria.c "He's so busy.  He never seems to be around except when he has official Club business."
            "Having a little chat" if gloria.session >= 3 and gloria.location == club:
                if gloria.session == 8:
                    gloria.c "Sam is such a doll! She's perfect. My husband's happy, I'm happy. Let me know the next time you want me to make you happy, and I'll be right over."
                    gloria.c "Not here though. I don't want to mix our friendship with the Club's business.  I'm sure you understand."
                elif gloria.session == 7:
                    gloria.c "We shouldn't talk here. If you have something you want to talk to me about, give me a call at home. I don't want to mix our friendship with the Club's business. I'm sure you understand."
                elif gloria.session >= 4 and gloria.session <= 6:
                    if not gloria.has_tag('first_club_visit') and not gloria.has_tag('trigger_implanted') and not gloria.session > 6:
                        wt_image club_pres_wife_5
                    gloria.c "We shouldn't talk here. Give me a call at home when my husband is okay with that. I'm looking forward to seeing you again!"
                elif gloria.session == 3:
                    player.c "How are you Gloria?"
                    gloria.c "I'm fine, thank you.  Enjoy your time at the Club!"
                    player.c "Could we have a little chat?"
                    gloria.c "How sweet.  But no, I'm rather busy now.  Ta ta!"
                if gloria.has_tag('trigger_implanted'):
                    $ title = "Invoke her trigger?"
                    menu:
                        "Yes, make her have sex with you":
                            player.c "I really must insist that you spend some time with me now, Gloria.  I want your close, personal attention."
                            gloria.c "I told you, that's not appropriate here at the Club.{nw}"
                            if gloria.session == 3:
                                extend "  I don't even like you that much."
                            else:
                                extend " I'm the Club President's wife and I can't be seen having a 'special relationship' with one of the Club members."
                            player.c "I know what you said, Gloria, but I'm insisting, \"[gloria.trigger_phrase]\"."
                            gloria.c "What ..."
                            player.c "\"[gloria.trigger_phrase]\", Gloria.  I'm in charge.  Not you."
                            gloria.c "Oh!  Yes.  You're in charge."
                            player.c "Is your husband here?"
                            gloria.c "No"
                            player.c "Good.  Take me to his office."
                            wt_image club_wife_office_hypno_12
                            "Even in her triggered state, she has the good sense to sneak you into her husband's office without anyone seeing the two of you."
                            player.c "Make yourself comfortable, Gloria."
                            wt_image club_wife_office_hypno_1
                            "She takes off her jacket and sits in her husband's chair."
                            player.c "That doesn't look very comfortable."
                            $ title = "What should she do to get comfortable?"
                            menu:
                                "Take off her clothes":
                                    player.c "You'd be much more comfortable without all that clothing on.  Show me your body."
                                    wt_image club_wife_office_hypno_3
                                    "She takes her clothes off ..."
                                    wt_image club_wife_office_hypno_4
                                    "... exposing her giant tits to you."
                                    add tags 'club_sex_clothes' to gloria
                                "Suck your cock":
                                    player.c "You'd be much more comfortable if you were sucking my cock."
                                    wt_image club_wife_office_hypno_2
                                    "She gets down off the chair, kneels at your feet and wraps her lips around your dick."
                                    add tags 'club_sex_suck' to gloria
                            $ title = "What now?"
                            menu menu_gloria_club_sex_2:
                                "Cum in her mouth" if gloria.has_tag('club_sex_suck'):
                                    wt_image club_wife_visit_24
                                    player.c "[player.orgasm_text]"
                                    "You fill her mouth with your hot seed."
                                    wt_image club_pres_wife_2
                                    "After she swallows it all, you send her back to the Club as if nothing had happened."
                                    $ gloria.hypno_blowjob_count += 1
                                    $ gloria.hypno_swallow_count += 1
                                    orgasm notify
                                "Cum on her face" if gloria.has_tag('club_sex_suck'):
                                    wt_image club_wife_visit_31
                                    "You pull her head back and spurt your load over her upturned face."
                                    player.c "[player.orgasm_text]"
                                    "It's tempting to send her back out into the Club with your seed in her hair and dripping down her chin, but that might cause problems and you shouldn't ruin a good thing by losing your access to the Club."
                                    wt_image club_pres_wife_2
                                    $ gloria.hypno_blowjob_count += 1
                                    $ gloria.hypno_facial_count += 1
                                    orgasm notify
                                "Fuck her":
                                    if gloria.has_tag('club_sex_play'):
                                        wt_image club_wife_office_hypno_11
                                        player.c "My turn now."
                                        "She's wet from her orgasm and you slide into her easily.  Her body starts to respond as you fuck her, adding to your pleasure."
                                        gloria.c "ooohhhh"
                                    else:
                                        player.c "Spread your legs."
                                        wt_image club_wife_office_hypno_9
                                        "She lies down on the floor and you push yourself into her. She's not initially wet, but it feels nice anyway, and her body starts to respond as you fuck her, adding to your pleasure."
                                        gloria.c "ooohhhh"
                                    player.c "[player.orgasm_text]"
                                    wt_image club_wife_office_hypno_10
                                    "Watching your cum drip out of her cunt, it's tempting to send her back out into the Club like this and leave her wondering where the sperm came from when it starts dripping down her leg, but that could cause her to investigate and potentially lead to problems."
                                    wt_image club_pres_wife_2
                                    "But shouldn't risk ruining a good thing and losing your access to the Club, so you have her clean herself up and go back out as if nothing has happened."
                                    $ gloria.hypno_sex_count += 1
                                    orgasm notify
                                "Have her play with herself" if gloria.has_tag('club_sex_clothes') and not gloria.has_tag('club_sex_play'):
                                    player.c "You'd be even more comfortable if you had an orgasm, Gloria."
                                    wt_image club_wife_office_hypno_5
                                    "She removes the rest of her clothes and lies down, spreading her legs to give you a good look as she puts her fingers on her sex."
                                    wt_image club_wife_office_hypno_6
                                    "It takes her a little while and it isn't her most earth-shattering orgasm, but she eventually jills herself to orgasm under your watchful eye, licking her licks as she cums."
                                    gloria.c "ooohhhhh  oooohhhhh oooohhhh  yeesssss"
                                    add tags 'club_sex_play' to gloria
                                    $ gloria.hypno_masturbation_count += 1
                                    $ gloria.hypno_orgasm_count += 1
                                    $ title = "What now?"
                                    jump menu_gloria_club_sex_2
                                "Jerk off on her face" if gloria.has_tag('club_sex_play'):
                                    wt_image club_wife_office_hypno_7
                                    "If she's licking her lips, you may as well give her something to lick off. You take out your cock and start stroking it over her face."
                                    wt_image club_wife_office_hypno_8
                                    player.c "[player.orgasm_text]"
                                    "As your seed sprays over her, she starts licking her lips again."
                                    "It's tempting to send her back out into the Club with your seed in her hair and dripping down her chin, but that might cause problems and you shouldn't ruin a good thing by losing your access to the Club."
                                    wt_image club_pres_wife_2
                                    "Instead, you have her clean herself up and go back out as if nothing has happened."
                                    $ gloria.hypno_facial_count += 1
                                    orgasm notify
                                "Show's over" if gloria.has_tag('club_sex_play'):
                                    "Watching Gloria finger fuck herself as your hypno slave was fun, but you have things to do."
                                    wt_image club_pres_wife_2
                                    "You have her clean herself up and go back out as if nothing has happened."
                            rem tags 'club_sex_clothes' 'club_sex_suck' 'club_sex_play' from gloria
                            wt_image current_location.image
                        "No, not right now":
                            pass
            "Nothing right now":
                pass
    else:
        "You have nothing to say to her here."
    return

label fallback_gloria_club_talk_option:
    gloria.c "I have no idea who that is."
    sys "Neither does the game. A _gloria_club_talk_option label is missing."
    return

# Hypno Actions
label gloria_hypnosis_start:
    if current_location == club:
        "Not in the Club. There are too many people here."
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    else:
        "Not here. At least, not now."
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    return

label gloria_custom_hypnosis:
    $ gloria.temporary_count = 1
    if gloria.has_tag('visiting_you'):
        ## CAN GET HERE IF GLORIA.SESSION == 2 IN WHICH CASE IT'S PART OF HER TEST
        ## CAN ALSO GET HERE IF GLORIA SESSION == 5 or 6, IN WHICH CASE IT'S PART OF SOLVING CLUB PRES' PROBLEM
        ## CAN ALSO GET HERE IF GLORIA SESSION == 8, IN WHICH CASE YOU'RE JUST WORKING TOWARDS IMPLANTING A TRIGGER
        ## CAN'T GET HERE ON GLORIA.SESSION == 1 (sex only session) or 3 (no session) or 7 (takes place at her home)
        player.c "Look at this, Gloria."
        call focus_image from _call_focus_image_6
        gloria.c "What is it .... oh."
        player.c "You and I are going to have a talk.  I am going to talk and you are going to listen to me, Gloria."
        wt_image club_wife_visit_2
        gloria.c "You're trying to hypnotize me."
        player.c "I am, but you won't remember that I've hypnotized you, Gloria. Listen to my voice, Gloria. Only my voice. Only my voice matters."
        player.c "You don't have any worries, any concerns, the only thing that matters is the sound of my voice. Let everything else slip away. Only my voice now, Gloria. Only my voice."
        if player.has_tag('hypnotist') or player.hypnosis_level > 10:
            $ gloria.hypno_session() # this subtracts energy and records that sh was hypnotized
            wt_image club_wife_visit_3
            "Despite her attempted resistance, you're able to put her under your trance."
            player.c "You won't remember that you were hypnotized, Gloria. You won't remember anything about our time together except what I tell you to remember."
            gloria.c "Okay"
            player.c "You want to enjoy your time with me. You're going to enjoy your time with me. To enjoy our time together, you should be comfortable. Kneel down and take off your top so you and I are both comfortable."
            wt_image club_wife_visit_4
            "She opens the top of her dress ..."
            wt_image club_wife_visit_5
            "... kneels down in front of you ..."
            wt_image club_wife_visit_6
            "... exposing two of the largest breasts you've ever seen."
            $ title = "What next?"
            menu:
                "Have her blow you while you talk to her":
                    player.c "To be truly comfortable for our talk, you should do what you came here to do, Gloria. Take out my cock and suck on it while we talk."
                    wt_image club_wife_visit_7
                    "Gloria doesn't question your request. It was what she was expecting when she came over here, after all. Her large breasts hanging free, she takes your cock in her mouth and looks up at you, ready for the conversation."
                    if gloria.session == 2 or gloria.session == 5 or gloria.session == 6:
                        player.c "We're going to talk about you and your husband while you blow me, Gloria."
                        "She nods."
                        player.c "He's not happy with your relationship."
                        wt_image club_wife_visit_27
                        gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                        player.c "You should let him hire someone for that."
                        gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help. She'll start working her claws into my husband and he won't even realize it."
                        gloria.c "Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                        wt_image club_wife_visit_7
                        "She's too set against the idea to hypnotize her into accepting it.  You'll have to suggest something else to get her to come around."
                        if gloria.session == 2:
                            "You work on convincing her that she can trust you to help her find a solution."
                            player.c "I am your friend, Gloria. I'll help you. I'll help you get rid of this tension between you and your husband. I'll help you find a solution that will make both you and your husband happy."
                            if player.test('hypnosis_level', 14):
                                $ gloria.first_session_test += 5
                            elif player.test('hypnosis_level', 9):
                                $ gloria.first_session_test += 4
                            else:
                                $ gloria.first_session_test += 3
                            add tags 'gloria_contact_first_session_hypno_blow' to gloria
                            call gloria_contact_first_session_test from _call_gloria_contact_first_session_test
                            rem tags 'gloria_contact_first_session_hypno_blow' from gloria
                        else:
                            wt_image club_wife_visit_27
                            call gloria_solution_options from _call_gloria_solution_options
                    elif gloria.has_tag('something_to_discuss'):
                        player.c "Keep pleasuring my dick while we talk, Gloria."
                        wt_image club_wife_visit_27
                        gloria.c "Okay"
                        call gloria_other_talk_topics from _call_gloria_other_talk_topics
                    else:
                        "You don't actually have anything in particular to talk to Gloria about right now, so you just enjoy watching the hypnotized woman blow you until you're ready to cum."
                    wt_image club_wife_visit_7
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her mouth":
                            wt_image club_wife_visit_29
                            player.c "[player.orgasm_text]"
                            "Gloria slurps down your cum as you fill her mouth."
                            $ gloria.hypno_swallow_count += 1
                        "On her face":
                            player.c "My cum will feel good on your face, Gloria.  Take a nice wet, facial for me."
                            wt_image club_wife_visit_28
                            gloria.c "Okay"
                            wt_image club_wife_visit_30
                            player.c "[player.orgasm_text]"
                            wt_image club_wife_visit_31
                            "You adorn Gloria's face with your sperm."
                            $ gloria.hypno_facial_count += 1
                        "On her tits":
                            player.c "My cum will feel good on your tits, Gloria.  Lean back."
                            wt_image club_wife_visit_27
                            gloria.c "Okay"
                            wt_image club_wife_visit_22
                            player.c "[player.orgasm_text]"
                            "You dump your load on her massive chest."
                    $ gloria.hypno_blowjob_count += 1
                    orgasm notify
                "Talk to her like this":
                    if gloria.session == 2 or gloria.session == 5 or gloria.session == 6:
                        player.c "We're going to talk about you and your husband Gloria."
                        gloria.c "Okay"
                        player.c "He's not happy with your relationship."
                        gloria.c "I think he's happy.  He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                        player.c "You should let him hire someone for that."
                        gloria.c "No.  If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                        "She's too set against the idea to hypnotize her into accepting it.  You'll have to suggest something else to get her to come around."
                        if gloria.session == 2:
                            "You work on convincing her that she can trust you to help her find a solution."
                            player.c "I am your friend, Gloria. I will help you. I will help you get rid of this tension between you and your husband. I will help you find a solution that will make both you and your husband happy."
                            if player.test('hypnosis_level', 14):
                                $ gloria.first_session_test += 5
                            elif player.test('hypnosis_level', 9):
                                $ gloria.first_session_test += 4
                            else:
                                $ gloria.first_session_test += 3
                            call gloria_contact_first_session_test from _call_gloria_contact_first_session_test_1
                        else:
                            call gloria_solution_options from _call_gloria_solution_options_1
                    elif gloria.has_tag('something_to_discuss'):
                        player.c "We're going to have a little talk, Gloria."
                        gloria.c "Okay"
                        call gloria_other_talk_topics from _call_gloria_other_talk_topics_1
                    else:
                        "You don't actually have anything in particular to talk to Gloria about right now, so you just chit chat with the hypnotized woman for a few minutes then wrap things up."
            ## moved to end of the chain, after trigger test
            # wt_image club_wife_visit_1
            # if gloria.session < 3:
            #     "You bring Gloria out of her trance and send her home."
            #     gloria.c "Ta ta!"
            # else:
            #     "You convince Gloria she had a great time with you today, then have her dress and bring her out of the trance."
            #     gloria.c "That was so much fun!  I hope my husband lets me see you again soon!!"
        else:
            $ gloria.temporary_count = 0
            add tags 'no_hypnosis' to gloria
            wt_image club_wife_visit_2
            "Unfortunately, you're not a strong enough hypnotist to put her under your trance."
            if gloria.session == 2:
                if gloria.has_tag('love_potion_used'):
                    gloria.c "First you use a love potion on me, now you try to hypnotize me. If I wasn't so besotten with you, I might think you were insecure about your ability to please me by just being you."
                    jump menu_gloria_contact_first_session
                else:
                    gloria.c "We get all kinds of charlatans through the Club. I didn't realize you were one. That's so disappointing. I was looking forward to our time together."
                    gloria.c "Ta ta!"
                    "She leaves."
                    if gloria.session == 2:
                        $ club_president.discussion_pending = 1
                        $ club_president.discussion_week = week - 1
                    $ gloria.session = 3
            else:
                gloria.c "I'm sure that parlor trick saves you some tedium when you're dealing with the mewling housewives you have to train, but I want the real deal."
                call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce
    elif gloria.has_tag('her_home'):
        ## CAN GET HERE IF GLORIA SESSION == 5, IN WHICH CASE IT'S PART OF SOLVING CLUB PRES' PROBLEM
        ## CAN ALSO GET HERE IF GLORIA SESSION == 7 OR 8, IN WHICH CASE IT'S PART OF TALKING TO HER ABOUT SOMETHING
        if gloria.house_outfit == 1:
            "Although there are other people in the house, you guess that they won't disturb her while she's in here with you, so you take a chance and try and hypnotize her."
            player.c "Look at this, Gloria."
            call focus_image from _call_focus_image_7
            gloria.c "What is it .... oh."
            player.c "You and I are going to have a talk. I am going to talk and you are going to listen to me."
            wt_image club_wife_house_outfit_1_1
            gloria.c "You're trying to hypnotize me."
            player.c "I am, but you won't remember that I've hypnotized you, Gloria. Listen to my voice, Gloria. Only my voice. Only my voice matters."
            player.c "You don't have any worries, any concerns, the only thing that matters is the sound of my voice. Let everything else slip away. Only my voice now, Gloria. Only my voice."
            if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                $ gloria.hypno_session() # this subtracts energy and records that sh was hypnotized
                wt_image club_wife_house_outfit_1_2
                "Despite her attempted resistance, you're able to put her under your trance."
                player.c "You want to enjoy your time with me. You are going to enjoy your time with me. To enjoy our time together, you should be comfortable. Take off your top so you and I are both comfortable."
                gloria.c "It's a one piece."
                wt_image club_wife_house_outfit_1_3
                "She loosens the dress and it falls to the floor. She steps out of it and stands in front of you."
                player.c "That's fine like that, Gloria."
                "It's tempting to have her suck your cock while you talk, but you're worried the sounds might cause someone in the house to come investigate, so you stick to the task at hand."
                if gloria.session == 5:
                    player.c "We're going to talk about you and your husband, Gloria."
                    gloria.c "Okay"
                    player.c "He's not happy with your relationship."
                    gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                    player.c "You should let him hire someone for that."
                    gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                    "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                    call gloria_solution_options from _call_gloria_solution_options_2
                else:
                    call gloria_other_talk_topics from _call_gloria_other_talk_topics_2
                # moved to after trigger test
                # wt_image club_wife_house_outfit_1_1
                # "You have her dress and bring her out of the trance."
                # gloria.c "Thanks for dropping by to chat."
            else:
                $ gloria.temporary_count = 0
                add tags 'no_hypnosis' to gloria
                gloria.c "Don't be silly. I know too much about these types of parlor tricks for you to hypnotize me. Just tell me what you want to talk to me about, without the hocus pocus efforts at influencing me."
                "Unfortunately, you're not a strong enough hypnotist to put her under your trance. You'll need to do this the old-fashioned way."
                call gloria_home_talk from _call_gloria_home_talk
        elif gloria.house_outfit == 2:
            "Although there are other people in the house, you guess that they won't disturb her while she's back here with you, so you take a chance and try and hypnotize her."
            player.c "Look at this, Gloria."
            call focus_image from _call_focus_image_8
            gloria.c "What is it .... oh."
            player.c "You and I are going to have a talk. I am going to talk and you are going to listen to me."
            wt_image club_wife_house_outfit_2_4
            gloria.c "You're trying to hypnotize me."
            player.c "I am, but you won't remember that I've hypnotized you, Gloria. Listen to my voice, Gloria. Only my voice. Only my voice matters."
            player.c "You don't have any worries, any concerns, the only thing that matters is the sound of my voice. Let everything else slip away. Only my voice now, Gloria. Only my voice."
            if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                $ gloria.hypno_session() # this subtracts energy and records that sh was hypnotized
                wt_image club_wife_house_outfit_2_5
                "Despite her attempted resistance, you're able to put her under your trance. She's already naked, so there's not point in telling her to show you her breasts."
                "Originally you didn't plan on having sex with her today, but if you want to change your mind, you'd guess that no one in the household will find it odd after what you just witnessed between Gloria and her pool girl."
                $ title = "What do you want?"
                menu:
                    "Have her pleasure you while you talk to her":
                        player.c "Play with my cock while we talk, Gloria."
                        gloria.c "Absolutely."
                        wt_image club_wife_house_outfit_2_6
                        "She sits on the pool lounger and takes out your cock."
                        if gloria.session == 5:
                            player.c "We're going to talk about you and your husband while you stroke me, Gloria."
                            gloria.c "Okay"
                            player.c "He's not happy with your relationship."
                            gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                            player.c "You should let him hire someone for that."
                            gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                            "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                            call gloria_solution_options from _call_gloria_solution_options_3
                        else:
                            call gloria_other_talk_topics from _call_gloria_other_talk_topics_3
                        wt_image club_wife_house_outfit_2_7
                        "That having been resolved, it's time to attend to more pressing matters.  You shoot your load up over her chest and face, leaving strings of your cum in the hypnotized woman's hair."
                        player.c "[player.orgasm_text]"
                        $ gloria.hypno_facial_count += 1
                        orgasm
                        $ gloria.temporary_count = 2 #sets end of sequence text

                    "Talk to her like this":
                        if gloria.session == 5:
                            player.c "We're going to talk about you and your husband, Gloria."
                            gloria.c "Okay"
                            player.c "He's not happy with your relationship."
                            gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                            player.c "You should let him hire someone for that."
                            gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                            "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                            call gloria_solution_options from _call_gloria_solution_options_4
                        else:
                            call gloria_other_talk_topics from _call_gloria_other_talk_topics_4
                # moved to after trigger test
                # wt_image club_wife_house_outfit_2_4
                # gloria.c "Thanks for dropping by to chat."
            else:
                $ gloria.temporary_count = 0
                add tags 'no_hypnosis' to gloria
                gloria.c "Don't be silly. I know too much about these types of parlor tricks for you to hypnotize me. Just tell me what you want to talk to me about, without the hocus pocus efforts at influencing me."
                "Unfortunately, you're not a strong enough hypnotist to put her under your trance. You'll need to do this the old-fashioned way."
                call gloria_home_talk from _call_gloria_home_talk_1
        elif gloria.house_outfit == 3:
            player.c "Look at this, Gloria."
            call focus_image from _call_focus_image_9
            gloria.c "What is it .... oh."
            player.c "You and I are going to have a talk. I am going to talk and you are going to listen to me."
            wt_image club_wife_house_outfit_3_3
            gloria.c "You're trying to hypnotize me."
            player.c "I am, but you won't remember that I've hypnotized you, Gloria. Listen to my voice, Gloria. Only my voice. Only my voice matters."
            player.c "You don't have any worries, any concerns, the only thing that matters is the sound of my voice. Let everything else slip away. Only my voice now, Gloria. Only my voice."
            if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                $ gloria.hypno_session() # this subtracts energy and records that sh was hypnotized
                "Despite her attempted resistance, you're able to put her under your trance."
                "She's pretty sexed up right now and that has you wondering whether you should have her have her suck your cock or get completely naked for you to look at ."
                $ title = "What do you want?"
                menu:
                    "Have her blow you while you talk to her":
                        player.c "Show me your tits and suck my cock while we talk, Gloria."
                        wt_image club_wife_house_outfit_3_5
                        gloria.c "Absolutely."
                        "She kneels down and starts worshiping your cock."
                        if gloria.session == 5:
                            player.c "We're going to talk about you and your husband, Gloria."
                            wt_image club_wife_house_outfit_3_6
                            gloria.c "Okay"
                            player.c "He's not happy with your relationship."
                            gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                            player.c "You should let him hire someone for that."
                            gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                            "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                            call gloria_solution_options from _call_gloria_solution_options_5
                        else:
                            call gloria_other_talk_topics from _call_gloria_other_talk_topics_5
                        "That having been resolved, it's time to attend to more pressing matters."
                        wt_image club_wife_house_outfit_3_5
                        "She wraps her lips tightly around your cock as you fill her mouth with your sperm."
                        player.c "[player.orgasm_text]"
                        wt_image club_wife_house_outfit_3_6
                        "When she's done swallowing, she looks up at you and smiles."
                        $ gloria.hypno_blowjob_count += 1
                        $ gloria.hypno_swallow_count += 1
                        orgasm
                    "Talk to her while she's naked":
                        player.c "You want to enjoy your time with me. You are going to enjoy your time with me. To enjoy our time together, you should be comfortable. Take off your dress so you and I are both comfortable."
                        wt_image club_wife_house_outfit_3_4
                        "She pulls off her dress and stands naked in front of you."
                        if gloria.session == 5:
                            player.c "We're going to talk about you and your husband, Gloria."
                            gloria.c "Okay"
                            player.c "He's not happy with your relationship."
                            gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                            player.c "You should let him hire someone for that."
                            gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                            "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                            call gloria_solution_options from _call_gloria_solution_options_6
                        else:
                            call gloria_other_talk_topics from _call_gloria_other_talk_topics_6
                # moved to after trigger test
                # wt_image club_wife_house_outfit_3_1
                # "You have her dress and bring her out of the trance."
                # gloria.c "Thanks for dropping by to chat."
            else:
                $ gloria.temporary_count = 0
                add tags 'no_hypnosis' to gloria
                gloria.c "Don't be silly. I know too much about these types of parlor tricks for you to hypnotize me. Just fuck me already and quit it with the childish games."
                "Unfortunately, you're not a strong enough hypnotist to put her under your trance. But you can still fuck her, if you want."
                jump menu_gloria_home_outfit_3
        elif gloria.house_outfit == 4:
            "There are people moving around in and around the house, but none of them are close at the moment, so you take a chance and try and hypnotize her."
            player.c "Look at this, Gloria."
            call focus_image from _call_focus_image_10
            gloria.c "What is it .... oh."
            player.c "You and I are going to have a talk. I am going to talk and you are going to listen to me."
            wt_image club_wife_house_outfit_4_2
            gloria.c "You're trying to hypnotize me."
            player.c "I am, but you won't remember that I've hypnotized you, Gloria. Listen to my voice, Gloria. Only my voice. Only my voice matters."
            player.c "You don't have any worries, any concerns, the only thing that matters is the sound of my voice. Let everything else slip away. Only my voice now, Gloria. Only my voice."
            if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                $ gloria.hypno_session() # this subtracts energy and records that sh was hypnotized
                wt_image club_wife_house_outfit_4_3
                "Despite her attempted resistance, you're able to put her under your trance."
                "You almost tell her to bare her breasts out of habit, when you realise that from where she's sitting, it's easy for people moving around on the lawn below to see her."
                "You're not sure how normal it may or may not be for Gloria to let herself be seen naked with a visitor to the house, so you don't dare ask her to take down her top. There is another body part of hers, however, that she may be able to show you without anyone else seeing."
                player.c "Gloria, you want to be comfortable for our talk. We should both be comfortable for our talk. Spread your legs - discretely - and show me your panties."
                wt_image club_wife_house_outfit_4_4
                gloria.c "I can't.  I'm not wearing any."
                player.c "That's fine, Gloria. Keep your legs spread just like that so I can see your pussy while we chat."
                if gloria.session == 5:
                    player.c "We're going to talk about you and your husband, Gloria."
                    gloria.c "Okay"
                    player.c "He's not happy with your relationship."
                    gloria.c "I think he's happy. He just wants to hire a woman to live with us so we have a bedmate any time we feel like one."
                    player.c "You should let him hire someone for that."
                    gloria.c "No. If we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help.  She'll start working her claws into my husband and he won't even realize it.  Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
                    "She's too set against the idea to hypnotize her into accepting it. You'll have to suggest something else to get her to come around."
                    call gloria_solution_options from _call_gloria_solution_options_7
                else:
                    call gloria_other_talk_topics from _call_gloria_other_talk_topics_7
                # moved to after trigger test
                # wt_image club_wife_house_outfit_4_2
                # "You have her dress and bring her out of the trance."
                # gloria.c "Thanks for dropping by to chat."
            else:
                $ gloria.temporary_count = 0
                add tags 'no_hypnosis' to gloria
                gloria.c "Don't be silly. I know too much about these types of parlor tricks for you to hypnotize me. Just tell me what you want to talk to me about, without the hocus pocus efforts at influencing me."
                "Unfortunately, you're not a strong enough hypnotist to put her under your trance. You'll need to do this the old-fashioned way."
                call gloria_home_talk from _call_gloria_home_talk_2
    if not gloria.has_tag('no_hypnosis') and not gloria.has_tag('trigger_implanted'):
        if gloria.hypno_count >= gloria.hypno_trigger_sessions_threshold:
            call gloria_implant_trigger from _call_gloria_implant_trigger
    if gloria.temporary_count > 0:
        if gloria.has_tag('visiting_you'):
            wt_image club_wife_visit_1
            if gloria.session < 3:
                "You bring Gloria out of her trance and send her home."
                gloria.c "Ta ta!"
            else:
                "You convince Gloria she had a great time with you today, then have her dress and bring her out of the trance."
                gloria.c "That was so much fun!  I hope my husband lets me see you again soon!!"
        elif gloria.has_tag('her_home'):
            if gloria.house_outfit == 1:
                wt_image club_wife_house_outfit_1_1
                "You have her dress and bring her out of the trance."
                gloria.c "Thanks for dropping by to chat."
            elif gloria.house_outfit == 2:
                if gloria.temporary_count == 2:
                    "You have her clean herself off and bring her out of the trance."
                else:
                    "You bring her out of the trance."
                wt_image club_wife_house_outfit_2_4
                gloria.c "Thanks for dropping by to chat."
            elif gloria.house_outfit == 3:
                wt_image club_wife_house_outfit_3_1
                "You have her dress and bring her out of the trance."
                gloria.c "Thanks for dropping by to chat."
            elif gloria.house_outfit == 4:
                wt_image club_wife_house_outfit_4_2
                "You have her dress and bring her out of the trance."
                gloria.c "Thanks for dropping by to chat."
        $ gloria.temporary_count = 0
    #call custom_hypnosis_action_end
    return

label gloria_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust hypno_trigger_sessions_threshold accordingly
    if player.has_tag('hypnotist'):
        add tags 'trigger_implanted' to gloria
        "Despite her awareness when you start hypnotizing her, Gloria falls deep into your trance once you've hypnotized her. You've now hypnotized her enough to plant a trigger that may be useful to you later."
        $ gloria.temporary_count = 1
        while gloria.temporary_count == 1:
            $ title = "What trigger phrase do you want to use?"
            menu menu_gloria_implant_trigger:
                "[gloria.trigger_phrase]":
                    $ gloria.temporary_count = 0
                "Choose something else":
                    $ gloria.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
        player.c "Gloria, I have something important to tell you."
        player.c "When you hear the phrase \"[gloria.trigger_phrase]\" you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
        gloria.c "Yes. When I hear \"[gloria.trigger_phrase]\" I will fall into a trance and do everything I am told."
        player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it. You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
        gloria.c "Yes. I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
        add tags 'trigger_implanted' to gloria
        notify "{}'s trigger has been implanted.".format(gloria.name)
        call gloria_hypnosis_end from _call_gloria_hypnosis_end
    return

label gloria_hypnosis_end:
    return

## Character Specific Actions
# N/A

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label gloria_contact:
  $ gloria.training_session()
  rem tags 'available_for_visit' 'no_hypnosis' from gloria # to allow subsequent tests to work
  if gloria.session >= 3:
    ## opening photo for subsequent contacts after the first
    wt_image club_wife_phone_1
  ## this is a follow up session after the Club Pres' problem has been resolved; you may or may not have anything to talk to her about on this session
  if gloria.session == 8:
    if gloria.has_tag('something_to_discuss'):
      player.c "Hi Gloria, I wonder if we could get together?"
      wt_image club_wife_phone_2
      gloria.c "Sounds good.  Are we going to get naked, or did you just want to talk?"
    else:
      "You don't have anything to talk to Gloria about, but perhaps you have some other reason to want to get together with her?"
    $ title = "What do you want to do with Gloria?"
    menu:
      "Just talk with her" if gloria.has_tag('something_to_discuss'):
        player.c "Let's just chat today."
        gloria.c "That's disappointing. In that case, you can come to my house. I don't feel like driving across town if all I get out of it is a conversation."
        call gloria_contact_later_session_home from _call_gloria_contact_later_session_home
      "Have her visit you":
        add tags 'visiting_you' to gloria
        player.c "Swing by my house. I want to see you again. All of you."
        wt_image club_wife_phone_2
        gloria.c "I'll be right over."
        summon gloria
        wt_image club_wife_visit_1
        gloria.c "Mmmmm ... So good to see you again!  I wonder what you have in store for me today?"
        if player.can_hypno(gloria):
          $ title = "What do you want to do with her?"
          menu:
            "Seduce her":
              call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce_1
            "Hypnotize her" if player.can_hypno(gloria):
              call gloria_custom_hypnosis from _call_gloria_custom_hypnosis
        else:
          call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce_2
        call character_location_return(gloria) from _call_character_location_return_300
        wt_image current_location.image
      "Nothing right now" if not gloria.has_tag('something_to_discuss'):
        rem tags 'trained_today' 'trained_this_week' from gloria
  ## this is a follow up session when you have something else to talk to her about and you have a solution to the Club Pres' problem but it hasn't been resolved yet
  elif gloria.session == 7:
    player.c "Gloria, something's come up that I'd like to discuss with you."
    gloria.c "You're in luck. I'm home today. Feel free to drop by."
    call gloria_contact_later_session_home from _call_gloria_contact_later_session_home_1
  ## this is a follow up session when trying to solve for the Club Pres after you've already had a successful sex session with Gloria
  elif gloria.session == 5:
    player.c "Gloria, you and I need to talk about the unresolved conflict between you and your husband."
    gloria.c "Fine. I suppose we can talk. Are you going to fuck me first?"
    $ title = "What do you want to do with Gloria?"
    menu:
      "Just talk with her":
        player.c "Let's just chat today."
        gloria.c "That's disappointing. In that case, you can come to my house. I don't feel like driving across town if all I get out of it is a conversation."
        call gloria_contact_later_session_home from _call_gloria_contact_later_session_home_2
      "Have her visit you":
        add tags 'visiting_you' to gloria
        player.c "Swing by my house. I definitely want to do something with you first."
        wt_image club_wife_phone_2
        gloria.c "I'll be right over."
        summon gloria
        wt_image club_wife_visit_1
        gloria.c "Mmmmm ... So good to see you again! I wonder what you have in store for me today?"
        if player.can_hypno(gloria):
          $ title = "How do you want to approach her training?"
          menu:
            "Seduce her":
              call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce_3
            "Hypnotize her" if player.can_hypno(gloria):
              call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_1
        else:
          call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce_4
    # add tags 'no_hypnosis' to gloria ## not needed
    call character_location_return(gloria) from _call_character_location_return_301
    wt_image current_location.image
  ## this is a training session for the Club Pres after you've already had a successful sex session with Gloria
  elif gloria.session == 6:
    add tags 'visiting_you' to gloria
    player.c "Swing by my house. I want to see you again."
    wt_image club_wife_phone_2
    gloria.c "I'll be right over."
    summon gloria
    wt_image club_wife_visit_1
    gloria.c "Mmmmm ... So good to see you again! I wonder what you have in store for me today?"
    "Looks like Gloria is excited to see you, but her husband wants an outcome from this session, too."
    $ title = "How do you want to approach her training?"
    menu:
      "Talk about her husband's concerns":
        player.c "How are things between you and your husband, Gloria?"
        wt_image club_wife_visit_3
        gloria.c "Good.  Why do you want to talk about him right now?"
        player.c "I worry about people's marriages.  It's what I do, I help couples."
        gloria.c "My husband and I are fine, thank you."
        player.c "Are you?  I understand there's some tension between you."
        gloria.c "What's he been telling you?  That he wants to hire a woman to live with us so we have a bedmate any time of the day or night that we feel like one?"
        player.c "Yes, and I understand you have concerns."
        gloria.c "Of course I have concerns. You're a guy, so you may not get this, but if we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help."
        gloria.c "She'll start working her claws into my husband and he won't even realize it. Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
        call gloria_solution_options from _call_gloria_solution_options_8
        change player energy by -energy_short notify
      "Seduce her first":
        call gloria_contact_later_session_seduce from _call_gloria_contact_later_session_seduce_5
      "Hypnotize her" if player.can_hypno(gloria):
        call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_2
    # add tags 'no_hypnosis' to gloria ##not needed
    call character_location_return(gloria) from _call_character_location_return_302
    wt_image current_location.image
  ## this is her first session with you
  elif gloria.session < 3:
    summon gloria
    wt_image club_wife_visit_1
    "Gloria comes right over when you call."
    gloria.c "I'm so glad you invited me to visit you!  I always enjoy the opportunity to spend time with members away from the formality of the Club and to really get to know them better."
    if player.has_tag('wealthy'):
      $ gloria.first_session_test += 3
      gloria.c "You're starting to get quite a reputation, you know.  And from the look of your house, I can see it's justified!  This is true quality.  I'm quite impressed.  I wonder if the rest of your house is as nice as the entrance?"
    else:
      gloria.c "You're starting to get quite a reputation, you know. I wonder if it's justified? I must warn you, I'm not easy to impress. Although I do hope that you'll impress me."
    gloria.c "So, show me your love den.  Where's the room where you make all the magic happen?"
    if player.has_tag('supersexy'):
      $ gloria.first_session_test += 1
    $ title = "Where do you want to take her?"
    menu:
      "Show her your boudoir":
        call forced_movement(boudoir) from _call_forced_movement_18
        wt_image boudoir.image
        "Gloria looks around with interest as you show her your boudoir."
        # note boudoir.moded_stat('desire_mod') combines boudoir.desire_mod with the .desire_mod of all the items in the boudoir to get the total impact of the room
        if boudoir.moded_stat('desire_mod') < 5:
          wt_image club_wife_visit_2
          gloria.c "Ewww!  Who do you seduce here?  Drunken university students??  I have to say, this is very disappointing."
          $ gloria.first_session_test -= 4
        elif boudoir.moded_stat('desire_mod') < 20:
          wt_image club_wife_visit_2
          gloria.c "You haven't really done much with this place, have you? Take my advice. If you want to impress a girl, put a little effort into making the bedroom look and feel sexy.  This is just so ... commonplace.  I'd hoped for more from you."
          $ gloria.first_session_test -= 3
        elif boudoir.moded_stat('desire_mod') < 30:
          wt_image club_wife_visit_1
          if player.has_tag('wealthy'):
            gloria.c "Hmmm.  Not bad, though I might have expected more from a man in your income bracket."
          else:
            gloria.c "Hmmm.  Not bad, I suppose, for a man in your income bracket.  Nothing special, but perhaps you have other charms to compensate?"
          # $ gloria.first_session_test -= 1  ## changed to no impact as part of a balance pass
        else:
          wt_image club_wife_visit_1
          gloria.c "Mmmm.  This is impressive.  I bet the girls spread their legs easy for you in here.  I know I'm going to."
          $ gloria.first_session_test += 1
        call forced_movement(living_room) from _call_forced_movement_20
      "Show her your dungeon instead":
        call forced_movement(dungeon) from _call_forced_movement_19
        wt_image dungeon.image
        "You show her your dungeon."
        wt_image club_wife_visit_2
        gloria.c "Oh.  You're one of those whips and chains type guys."
        "She looks around."
        # note dungeon.moded_stat('submission_mod') combines dungeon.submission_mod with the .submission_mod of all the items in the dungeon to get the total impact of the room
        if dungeon.moded_stat('submission_mod') < 30:
          gloria.c "You don't really have a lot in here, do you?  Some of the dungeons serious BDSM players put together are quite elaborate.  This one seems quite boring by comparison.  Anyway, I'm not really into this sort of thing. Let's go back to the living room."
          $ gloria.first_session_test -= 3
        else:
          gloria.c "You've got quite the collection of equipment in here.  I'm not really into this sort of thing, but I can see how some women would be impressed.  Let's go back to the living room."
          # $ gloria.first_session_test -= 2  ## changed to no impact as part of a balane pass
        call forced_movement(living_room) from _call_forced_movement_549
      "Tell her it all happens here in your living room":
        player.c "You're in it."
        wt_image club_wife_visit_2
        gloria.c "Your living room?  Gawd, how disappointing.  Is this what happens when sex is your profession?  You just stop trying?"
        gloria.c "I suppose the overstressed soccer moms and mewling home makers you work with are just happy to have someone inspect between their legs, and don't care where it happens.  Silly me for hoping for better from you."
        $ gloria.first_session_test -= 4
    if gloria.first_session_test > 0:
      wt_image club_wife_visit_1
    else:
      wt_image club_wife_visit_2
    gloria.c "So what now?"
    ## this is if you are supposed to train her for her husband
    if gloria.session == 2:
      add tags 'visiting_you' to gloria
      $ title = "How do you want to approach her training?"
      menu menu_gloria_contact_first_session:
        "Use a love potion" if player.has_item(love_potion) and not gloria.has_tag('love_potion_used'):
          wt_image club_wife_drink_1
          player.c "How about a drink to start?"
          gloria.c "I'd love one!"
          wt_image club_wife_drink_2
          gloria.c "Mmmmmmm"
          "She drinks the potion down."
          wt_image club_wife_drink_3
          gloria.c "Oh!  You amazing, wonderful man!  You used a love potion on me!  You like me so much you would do that ... I'm so happy!"
          gloria.c "My husband will give me an antidote when I get home, but I won't be mad at you even after the effects are worn off. How can you be mad at someone you once loved as much as I now love you?"
          gloria.c "Anyway, that's for later. Right now I'm thoroughly besotten with you, so you may as well do anything you want with me."
          gloria.c "Unless you've thoroughly disappointed me before giving me the potion, it probably doesn't really matter what you do with me now. I'm going to float home anyway, it feels so great just getting to spend time with you!"
          $ gloria.first_session_test += 4
          add tags 'love_potion_used' to gloria
          rem 1 love_potion from player notify
          $ title = "What do you want to do with her?"
          jump menu_gloria_contact_first_session
        "Talk about her husband's concerns" if not gloria.has_tag('gloria_contact_first_session_concerns'):
          if gloria.has_tag('love_potion_used'):
            player.c "How are things between you and your husband, Gloria?"
            gloria.c "Why do you want to talk about him right now?"
            player.c "I worry about people's marriages.  It's what I do, I help couples."
            gloria.c "My husband and I are fine, thank you."
            player.c "Are you?  I understand there's some tension between you."
            gloria.c "Oh. My husband put you up to this didn't he? You bad boy. If I wasn't so infatuated with you right now, I'd be really mad."
            player.c "It's not like that, Gloria."
            gloria.c "Don't worry. I'm not going to stay mad at you. The love potion won't let me. You wanted to talk about my marriage, that's fine. Won't you please fuck me first, though?"
            $ title = "What do you want to do?"
            menu:
              "Fuck her":
                player.c "All right, Gloria.  I'll fuck you."
                wt_image club_wife_visit_13
                gloria.c "Oh good!  Let me get my clothes off!"
                call gloria_contact_first_session_sex_main from _call_gloria_contact_first_session_sex_main
              "Just talk":
                player.c "Let's just talk, Gloria."
                gloria.c "How disappointing. I want to fuck and you just want to chat. I hate that in a man."
                if gloria.first_session_test > 0:
                  wt_image club_wife_visit_1
                  gloria.c "Okay, fine. I'm too besotten by the love potion to care. I'm just happy to spend time with you, even if it is spent talking about my marriage."
                else:
                  wt_image club_wife_visit_2
                  gloria.c "I didn't think it would be possible to disappoint me after besotting me with this love potion, but you seem to have managed it. After some of the things I'd heard about you, I was expecting more."
                change player energy by -energy_very_short notify
                call gloria_contact_first_session_test from _call_gloria_contact_first_session_test_2
          else:
            player.c "How are things between you and your husband, Gloria?"
            wt_image club_wife_visit_2
            gloria.c "Why do you want to talk about him right now?"
            player.c "I worry about people's marriages.  It's what I do, I help couples."
            gloria.c "My husband and I are fine, thank you."
            player.c "Are you?  I understand there's some tension between you."
            gloria.c "Did he put you up to this?  Oh my god!  Did he hire you to spend time with me???"
            player.c "It's not like that, Gloria."
            gloria.c "I came over here to spend time with you, not to have you convince me to agree to what my husband wants."
            player.c "That's not how I work, Gloria.  I'm not here to convince you of anything."
            gloria.c "Good.  Because the only thing you're convincing me of right now is that this was a bad idea."
            "Perhaps you should try something else and try to get on Gloria's good side before you broach this subject again."
            $ gloria.first_session_test -= 1
            add tags 'gloria_contact_first_session_concerns' to gloria
            $ title = "How do you want to approach her training?"
            jump menu_gloria_contact_first_session
        "Seduce her":
          if gloria.has_tag('gloria_contact_first_session_concerns'):
            player.c "You're right, Gloria. I shouldn't have brought up your husband when we haven't even taken the time to get to know each other better. I am looking forward to that."
          call gloria_contact_first_session_seduce from _call_gloria_contact_first_session_seduce
        "Hypnotize her" if player.can_hypno(gloria):
          add tags 'training_hypno' to gloria
          call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_3
    ## this is if you're just playing with her
    else:
      call gloria_contact_first_session_seduce from _call_gloria_contact_first_session_seduce_1
    # add tags 'no_hypnosis' to gloria ## not needed
    call forced_movement(living_room) from _call_forced_movement_21
    call character_location_return(gloria) from _call_character_location_return_303
    wt_image current_location.image
  return

label gloria_contact_first_session_sex_main:
  $ title = "How do you want to treat her?"
  menu:
    "Treat her rough":
      wt_image club_wife_visit_14
      if player.has_tag('dominant'):
        "Slowly you start backing her up across the room."
        gloria.c "Ummm ... what are you doing?"
        "When she reaches the dresser, she can't back up any further. You press your leg between hers and exert a hard pressure on her sex as you take her tits firmly between your hands and start to squeeze."
        gloria.c "Ouch!  Okay, I don't really like ..."
        "You push your leg up harder against her sex."
        gloria.c "Ohhhh ... okay, you're good at this but ..."
        "You squeeze her tits harder, twisting her nipples as you do so."
        gloria.c "Owww ... ohhhh!  Okay, fine, you're in charge.  Take me whatever way you want me.  Please just don't leave too many bruises."
        $ gloria.first_session_test += 1
      else:
        "Pushing her backwards, you grab her by the tits and give them a rough squeeze."
        gloria.c "Ouch!  Hey ... wow, slow down.  Those are attached to me.  Give me a moment to warm up before you start trying to pull them off me."
        $ gloria.first_session_test -= 1
      add tags 'first_session_rough' to gloria
    "Treat her gentle":
      wt_image club_wife_visit_15
      "You step behind her and gently caress her breasts as she nuzzles back into you."
      gloria.c "Ohhhh... that feels nice."
  $ title = "What do you want from her?"
  menu:
    "Tit Job":
      if gloria.has_tag('first_session_rough'):
        wt_image club_wife_visit_16
        "You pick her up and seat her on your lap.  Then you bite her tits, hard."
        gloria.c "Ohhhh ... owwww ... ohhh owww ohhhh!"
        wt_image club_wife_visit_18
        "Then you slide her to her knees and place your cock between her sore breasts."
      else:
        wt_image club_wife_visit_17
        "Turning her around, you kiss and suckle at her tits."
        gloria.c "Ohhhh ... ohhhh"
        wt_image club_wife_visit_18
        "Then you guide her down to her knees and place your cock between her breasts."
      wt_image club_wife_visit_19
      "Forming a valley between her tits, she fucks your cock up and down with her soft mounds. It feels great, and you're close to cumming."
      $ title = "What do you want?"
      menu:
        "Cum on her tits":
          wt_image club_wife_visit_23
          "She lies back as you climax, spurting your load up and over her tits and face."
          player.c "[player.orgasm_text]"
          gloria.c "Mmmm  You liked that, huh?"
          $ gloria.first_session_test -= 1
          $ gloria.titfuck_count += 1
        "Tell her to touch herself":
          player.c "Play with yourself while you're tit fucking me."
          wt_image club_wife_visit_20
          "The attention you've been paying to her breasts has her excited.  She starts pinching her nipples and moaning as she strokes her tits up and down your cock."
          gloria.c "Ohhhhh ... ohhhhh"
          wt_image club_wife_visit_21
          "Turning her around, you're able to snake a finger between her legs and help her finish herself off."
          gloria.c "Oohhhhh!!!  YESSS!!!!"
          wt_image club_wife_visit_22
          "She slumps, exhausted from the orgasm, giving you easy access to deposit your load on her chest."
          player.c "[player.orgasm_text]"
          "She moans as she feels your cum on her skin."
          gloria.c "Mmmmmm"
          $ gloria.titfuck_count += 1
          $ gloria.orgasm_count += 1
          $ gloria.first_session_test += 1
        "Fuck her now":
          call gloria_contact_first_session_sex from _call_gloria_contact_first_session_sex
    "Blow Job":
      if gloria.has_tag('first_session_rough'):
        wt_image club_wife_visit_24
        "Grabbing her by the hair, you pull her head down onto your cock ..."
        wt_image club_wife_visit_25
        "... then you pull her head further down and direct her tongue onto your balls ..."
        wt_image club_wife_visit_26
        "... until you're ready to start fucking her face. It's not long before you're ready to cum."
      else:
        wt_image club_wife_visit_27
        "With a touch on her shoulder, you direct her to her knees.  She takes out your cock and strokes it in her hand ..."
        wt_image club_wife_visit_28
        "... then licks gently around your cock head ..."
        wt_image club_wife_visit_29
        "... before wrapping her lips around your cock and bobbing her head up and down your shaft. It's not long before you're ready to cum."
      $ title = "What do you want?"
      menu:
        "Cum on her face":
          wt_image club_wife_visit_30
          "With a hand on her head, you guide her mouth off of your cock, then hold it there. She understands immediately what you want, and strokes your cock faster and faster until you explode onto her waiting face."
          player.c "[player.orgasm_text]"
          wt_image club_wife_visit_31
          gloria.c "Mmmm ... You liked that, huh?"
          $ gloria.blowjob_count += 1
          $ gloria.facial_count += 1
          $ gloria.first_session_test -= 1
        "Fuck her now":
          call gloria_contact_first_session_sex from _call_gloria_contact_first_session_sex_1
    "Sex":
      call gloria_contact_first_session_sex from _call_gloria_contact_first_session_sex_2
  orgasm notify
  call gloria_contact_first_session_test from _call_gloria_contact_first_session_test_3
  return

label gloria_contact_first_session_seduce:
  player.c "How about we get a little closer?"
  if gloria.first_session_test < 0:
    gloria.c "Okay. I'll give you another chance to impress me. Maybe your fucking skills make up for your other deficiencies."
    wt_image club_wife_visit_13
    "Gloria strips off her clothes."
  else:
    wt_image club_wife_visit_1
    gloria.c "Mmmm.  Sounds good.  I just came from a fundraiser, though, and I'm a bit sticky. Let me use your shower first to clean up.  I want to be at my best for you."
    $ title = "What do you want to do while she showers?"
    menu:
      "Watch her shower":
        call forced_movement(bathroom) from _call_forced_movement_550
        summon gloria
        wt_image club_wife_visit_8
        "Gloria smiles when she hears you enter the bathroom after her."
        gloria.c "Couldn't wait, huh?   That's okay.  You can watch if you want.  But stay there.  I don't intend for our first time to be in a crowded shower stall."
        wt_image club_wife_visit_9
        "Gloria soaps up two of the largest breasts you've ever seen.  She grins when she sees you staring at them."
        wt_image club_wife_visit_10
        "She moves on to cleaning the rest of her, making sure you have a good view while she does so."
        wt_image club_wife_visit_11
        gloria.c "Okay, show's over.  Go wait for me in the living room while I rinse and dry off."
        wt_image club_wife_visit_12
        "You sneak one more peek on your way out, then go wait for her to finish up."
        call forced_movement(living_room) from _call_forced_movement_551
        summon gloria
        wt_image club_wife_visit_13
        "A few minutes later, Gloria returns, in all her glory."
        gloria.c "There!  I feel better now.  It must be time to make you feel better.  That boner you're sporting must be quite uncomfortable."
        $ gloria.first_session_test += 1
      "Wait for her":
        pass
  call gloria_contact_first_session_sex_main from _call_gloria_contact_first_session_sex_main_1
  return

label gloria_contact_first_session_sex:
  if gloria.has_tag('first_session_rough'):
    player.c "I'm going to fuck you now, Gloria."
    gloria.c "Ohhhh yes!"
    wt_image club_wife_visit_32
    "Turning her around, you bend her over and shove yourself inside."
    gloria.c "Ohhhhh!"
    wt_image club_wife_visit_33
    "Taking hold of her wrists, you pull her arms back. The position gives you great leverage, and allows you to control the pace of the fuck."
    gloria.c "Ohhhh! ... Ohhhh! ... Ohhhhhh!!"
    wt_image club_wife_visit_34
    "Keeping your cock inside her, you drag her across the room and push her face down on the sofa."
    gloria.c "Oohhhhh!!! ...  Ooohhhh!!!"
    "You fuck her faster and faster, until you're ready to cum."
    $ title = "What do you do?"
    menu:
      "Wait for her to cum":
        wt_image club_wife_visit_35
        "You hold back your orgasm as you continue to pound into her."
        gloria.c "Oohhhh!!! ...  OOHHHHH!!!! ...  OHHH YEESSSSSS!!!!"
        wt_image club_wife_visit_36
        "Now that she's climaxed, you let yourself go, dumping your load on her upturned ass."
        player.c "[player.orgasm_text]"
        "She moans at the feel of your hot jizz on her skin."
        gloria.c "Mmmhhhhh"
        $ gloria.orgasm_count += 1
        $ gloria.first_session_test += 1
      "Cum on her":
        wt_image club_wife_visit_36
        "You let yourself go, dumping your load on her upturned ass."
        player.c "[player.orgasm_text]"
        "She moans at the feel of your hot jizz on her skin, partially because it feels good, partially in frustration that she didn't cum."
        gloria.c "Mmmm ... You liked that, huh?"
        $ gloria.first_session_test -= 1
  else:
    player.c "I want to fuck you, Gloria."
    gloria.c "Mmmm ... I thought you'd never ask!"
    wt_image club_wife_visit_37
    "Gloria lies back and spreads herself open for you. She's wet, and you slide into her easily."
    wt_image club_wife_visit_38
    "She moans as you fuck her, groaning with every in thrust."
    gloria.c "Oohhhh! ... Oohhhh!"
    wt_image club_wife_visit_39
    gloria.c "Oohhhh! ... Oohhhh!"
    "She's enjoying this, and so are you. You're ready to cum."
    $ title = "What do you do?"
    menu:
      "Wait for her to cum":
        wt_image club_wife_visit_40
        "You hold back your orgasm as you reach out for her tit.  You squeeze it as you pound into her, faster and faster."
        gloria.c "Oohhhh!!! ...  OOHHHHH!!!! ...  OHHH YEESSSSSS!!!!"
        wt_image club_wife_visit_41
        "Now that she's climaxed, you let yourself go. You pull out and she strokes your cock with her fingers as you dump your load on her belly and pussy."
        player.c "[player.orgasm_text]"
        "She moans at the feel of your hot jizz on her skin."
        gloria.c "Mmmhhhhh"
        $ gloria.orgasm_count += 1
        $ gloria.first_session_test += 1
      "Cum on her":
        wt_image club_wife_visit_41
        "You pull out and she strokes your cock with her fingers as you dump your load on her belly and pussy."
        player.c "[player.orgasm_text]"
        "She moans at the feel of your hot jizz on her skin, partially because it feels good, partially in frustration that she didn't cum."
        gloria.c "Mmmm ... You liked that, huh?"
        $ gloria.first_session_test -= 1
  $ gloria.sex_count += 1
  return

label gloria_contact_first_session_test:
  # test if you successfully hypnotized her
  if gloria.has_tag('training_hypno'):
    if gloria.first_session_test > 0:
      call gloria_solution_options from _call_gloria_solution_options_9
      if gloria.has_tag('gloria_contact_first_session_hypno_blow'):
        "Now that that's resolved, it's time for Gloria to finish what she started."
    else:
      "Unfortunately, even under hypnosis you weren't able to overcome the negative impression she had of you from the initial tour of your house."
      "Despite your best efforts, you're not able to convince her that you're enough of 'her type' of a person to be competent to help out her and her husband."
      if gloria.has_tag('gloria_contact_first_session_hypno_blow'):
        "Oh well, at least she's giving your cock a good sucking."
      if gloria.session == 2:
        $ club_president.discussion_pending = 1
        $ club_president.discussion_week = week - 1
      $ gloria.session = 3
  else:
    # success
    if gloria.first_session_test > 0:
      wt_image club_wife_visit_43
      if gloria.has_tag('love_potion_used'):
        gloria.c "Mmmhhhh! That was nice. Maybe this is just the love potion talking, but you're as good as your reputation suggests."
      else:
        gloria.c "Mmmhhhh!  That was nice.  You're as good as your reputation suggests."
      "Seems you were able to impress Gloria with your prowess."
      # if training session, go on to solutions
      if gloria.session == 2:
        player.c "I had fun, too.  You're a hell of a woman.  Your husband says so, too."
        wt_image club_wife_visit_13
        gloria.c "Does he?  That's nice."
        player.c "I understand there's been some tension between the two of you lately."
        wt_image club_wife_visit_44
        gloria.c "What's he been telling you?  That he wants to hire a woman to live with us so we have a bedmate any time of the day or night that we feel like one?"
        player.c "Yes, and I understand you have concerns."
        gloria.c "Of course I have concerns. You're a guy, so you may not get this, but if we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help."
        gloria.c "She'll start working her claws into my husband and he won't even realize it. Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
        call gloria_solution_options from _call_gloria_solution_options_10
      # if sex session, open up future training potential
      else:
        $ gloria.session = 4
      $ player.desire_action_count += 1
    # failure
    else:
      wt_image club_wife_ta_sex_6
      if gloria.has_tag('love_potion_used'):
        gloria.c "I didn't think it would be possible to disappoint me after besotting me with this love potion, but you seem to have managed it. After some of the things I'd heard about you, I was expecting more."
      else:
        gloria.c "That was nice, but after some of the things I'd heard about you, I was expecting more."
      "Seems you weren't able to impress Gloria.  Oh well, there are other women out there you may have better luck with."
      # if training session, set up follow up conversation with Club Pres
      if gloria.session == 2:
        $ club_president.discussion_pending = 1
        $ club_president.discussion_week = week - 1
      $ gloria.session = 3
  return

label gloria_contact_later_session_seduce:
  player.c "I'm looking forward to getting my hands - and other body parts - on you again."
  gloria.c "Mmmm. Sounds good. I just came from a fundraiser, though, and I'm a bit sticky. Let me use your shower first to clean up."
  $ title = "What do you want to do while she showers?"
  menu:
    "Watch her shower":
      call forced_movement(bathroom) from _call_forced_movement_552
      summon gloria
      wt_image club_wife_visit_8
      "Gloria smiles when she hears you enter the bathroom after her."
      gloria.c "Couldn't wait, huh?   That's okay.  You can watch if you want.  But stay there.  I don't want bruises from trying to have sex in a crowded shower stall."
      wt_image club_wife_visit_9
      "Gloria soaps up two of the largest breasts you've ever seen. She grins when she sees you staring at them."
      wt_image club_wife_visit_10
      "She moves on to cleaning the rest of her, making sure you have a good view while she does so."
      wt_image club_wife_visit_11
      gloria.c "Okay, show's over.  Go wait for me in the living room while I rinse and dry off."
      wt_image club_wife_visit_12
      "You sneak one more peek on your way out, then go wait for her to finish up."
      call forced_movement(living_room) from _call_forced_movement_553
      summon gloria
    "Wait for her":
      pass
  wt_image club_wife_visit_13
  "A few minutes later, Gloria returns, in all her glory."
  $ title = "How do you want to treat her?"
  menu:
    "Treat her rough":
      wt_image club_wife_visit_14
      if player.has_tag('dominant'):
        "Slowly you start backing her up across the room."
        gloria.c "Ummm ... what are you doing?"
        "When she reaches the dresser, she can't back up any further. You press your leg between hers and exert a hard pressure on her sex as you take her tits firmly between your hands and start to squeeze."
        gloria.c "Ouch!  Okay, I don't really like..."
        "You push your leg up harder against her sex."
        gloria.c "Ohhhh ... okay, you're good at this but ..."
        "You squeeze her tits harder, twisting her nipples as you do so."
        gloria.c "Owww .. ohhhh!  Okay, fine, you're in charge. Take me whatever way you want me. Please just don't leave too many bruises."
        add tags 'current_session_rough' to gloria
      else:
        "Pushing her backwards, you grab her by the tits and give them a rough squeeze."
        gloria.c "Ouch! Hey ... wow, slow down. Those are attached to me.  How about you just take things gently? You're not that good at rough sex and it's not really my thing anyway."
        if gloria.has_tag('trigger_implanted'):
          player.c "Yes it is, Gloria.  Today it is, and any day I tell you it is."
          gloria.c "Hey, you heard what I said!"
          player.c "I know what you said, Gloria, but I'm insisting, \"[gloria.trigger_phrase]\"."
          gloria.c "What..."
          player.c "\"[gloria.trigger_phrase]\", Gloria.  I'm in charge.  Not you."
          gloria.c "Yes, you're in charge.  Take me whatever way you want me."
          add tags 'current_session_rough' to gloria
    "Treat her gentle":
      wt_image club_wife_visit_15
      "You step behind her and gently caress her breasts as she nuzzles back into you."
      gloria.c "Ohhhh ... that feels nice."
  $ title = "What do you want from her?"
  menu:
    "Tit Job":
      if gloria.has_tag('current_session_rough'):
        wt_image club_wife_visit_16
        "You pick her up and seat her on your lap.  Then you bite her tits, hard."
        gloria.c "Ohhhh ... owwww ... ohhh owww ohhhh!"
        wt_image club_wife_visit_18
        "Then you slide her to her knees and place your cock between her sore breasts."
      else:
        wt_image club_wife_visit_17
        "Turning her around, you kiss and suckle at her tits."
        gloria.c "Ohhhh ... ohhhh"
        wt_image club_wife_visit_18
        "Then you guide her down to her knees and place your cock between her breasts."
      wt_image club_wife_visit_19
      "Forming a valley between her tits, she fucks your cock up and down with her soft mounds. It feels great, and you're close to cumming."
      $ gloria.titfuck_count += 1
      $ title = "What do you want?"
      menu:
        "Cum on her tits":
          wt_image club_wife_visit_23
          "She lies back as you climax, spurting your load up and over her tits and face."
          player.c "[player.orgasm_text]"
          gloria.c "Mmmm ... You liked that, huh?"
        "Tell her to touch herself":
          wt_image club_wife_visit_20
          player.c "Play with yourself while you're tit fucking me."
          "The attention you've been paying to her breasts has her excited.  She starts pinching her nipples and moaning as she strokes her tits up and down your cock."
          gloria.c "Ohhhhh ... ohhhhh"
          wt_image club_wife_visit_21
          "Turning her around, you're able to snake a finger between her legs and help her finish herself off."
          gloria.c "Oohhhhh!!!  YESSS!!!!"
          wt_image club_wife_visit_22
          "She slumps, exhausted from the orgasm, giving you easy access to deposit your load on her chest."
          player.c "[player.orgasm_text]"
          "She moans as she feels your cum on her skin."
          gloria.c "Mmmmmm"
          $ gloria.orgasm_count += 1
      $ gloria.titfuck_count += 1
    "Blow Job":
      if gloria.has_tag('currently_session_rough'):
        wt_image club_wife_visit_24
        "Grabbing her by the hair, you pull her head down onto your cock ..."
        wt_image club_wife_visit_25
        "... then you pull her head further down and direct her tongue onto your balls ..."
        wt_image club_wife_visit_26
        "... until you're ready to start fucking her face. It's not long before you're ready to cum."
      else:
        wt_image club_wife_visit_27
        "With a touch on her shoulder, you direct her to her knees.  She takes out your cock and strokes it in her hand ..."
        wt_image club_wife_visit_28
        "... then licks gently around your cock head ..."
        wt_image club_wife_visit_29
        "... before wrapping her lips around your cock and bobbing her head up and down your shaft. It's not long before you're ready to cum."
      $ gloria.blowjob_count += 1
      $ title = "Where do you want to cum?"
      menu:
        "Cum on her face":
          wt_image club_wife_visit_30
          "With a hand on her head, you guide her mouth off of your cock, then hold it there. She understands immediately what you want, and strokes your cock faster and faster until you explode onto her waiting face."
          player.c "[player.orgasm_text]"
          wt_image club_wife_visit_31
          gloria.c "Mmmm ... You liked that, huh?"
          $ gloria.facial_count += 1
        "Cum in her mouth":
          wt_image club_wife_visit_24
          player.c "[player.orgasm_text]"
          "Gloria slurps down your cum as you fill her mouth."
          $ gloria.swallow_count += 1
      $ gloria.blowjob_count += 1
    "Sex":
      if gloria.has_tag('current_session_rough'):
        player.c "I'm going to fuck you now, Gloria."
        gloria.c "Ohhhh yes!"
        wt_image club_wife_visit_32
        "Turning her around, you bend her over and shove yourself inside."
        gloria.c "Ohhhhh!"
        wt_image club_wife_visit_33
        "Taking hold of her wrists, you pull her arms back. The position gives you great leverage, and allows you to control the pace of the fuck."
        gloria.c "Ohhhh! ... Ohhhh! ... Ohhhhhh!!"
        wt_image club_wife_visit_34
        "Keeping your cock inside her, you drag her across the room and push her face down on the sofa."
        gloria.c "Oohhhhh!!! ...  Ooohhhh!!!"
        "You fuck her faster and faster, until you're ready to cum."
        $ title = "What do you do?"
        menu:
          "Wait for her to cum":
            wt_image club_wife_visit_35
            "You hold back your orgasm as you continue to pound into her."
            gloria.c "Oohhhh!!! ...  OOHHHHH!!!! ...  OHHH YEESSSSSS!!!!"
            wt_image club_wife_visit_36
            "Now that she's climaxed, you let yourself go, dumping your load on her upturned ass."
            player.c "[player.orgasm_text]"
            "She moans at the feel of your hot jizz on her skin."
            gloria.c "Mmmhhhhh"
            $ gloria.orgasm_count += 1
          "Cum on her":
            wt_image club_wife_visit_36
            "You let yourself go, dumping your load on her upturned ass."
            player.c "[player.orgasm_text]"
            "She moans at the feel of your hot jizz on her skin, partially because it feels good, partially in frustration that she didn't cum."
            gloria.c "Mmmm ... You liked that, huh?"
      else:
        player.c "I want to fuck you, Gloria."
        gloria.c "Mmmm ... I thought you'd never ask!"
        wt_image club_wife_visit_37
        "Gloria lies back and spreads herself open for you. She's wet, and you slide into her easily."
        wt_image club_wife_visit_38
        "She moans as you fuck her, groaning with every in thrust."
        gloria.c "Oohhhh! ... Oohhhh!"
        wt_image club_wife_visit_39
        gloria.c "Oohhhh! ... Oohhhh!"
        "She's enjoying this, and so are you. You're ready to cum."
        $ title = "What do you do?"
        menu:
          "Wait for her to cum":
            wt_image club_wife_visit_40
            "You hold back your orgasm as you reach out for her tit.  You squeeze it as you pound into her, faster and faster."
            gloria.c "Oohhhh!!! ...  OOHHHHH!!!! ...  OHHH YEESSSSSS!!!!"
            wt_image club_wife_visit_41
            "Now that she's climaxed, you let yourself go. You pull out and she strokes your cock with her fingers as you dump your load on her belly and pussy."
            player.c "[player.orgasm_text]"
            "She moans at the feel of your hot jizz on her skin."
            gloria.c "Mmmhhhhh"
            $ gloria.orgasm_count += 1
          "Cum on her":
            wt_image club_wife_visit_41
            "You pull out and she strokes your cock with her fingers as you dump your load on her belly and pussy."
            player.c "[player.orgasm_text]"
            "She moans at the feel of your hot jizz on her skin, partially because it feels good, partially in frustration that she didn't cum."
            gloria.c "Mmmm ... You liked that, huh?"
      $ gloria.sex_count += 1
  wt_image club_wife_visit_43
  gloria.c "Mmmhhhh!  That was nice."
  if gloria.session == 5:
    player.c "I had fun, too. But now we have some work to do. We still haven't resolved the tension between you and your husband."
    gloria.c "I've followed your suggestions, but they haven't helped."
    player.c "Then we need to try something else."
    call gloria_solution_options from _call_gloria_solution_options_11
  elif gloria.session == 6:
    player.c "I had fun, too.  You're a hell of a woman.  Your husband says so, too."
    gloria.c "Does he?  That's nice."
    player.c "I understand there's been some tension between the two of you lately."
    gloria.c "What's he been telling you?  That he wants to hire a woman to live with us so we have a bedmate any time of the day or night that we feel like one?"
    player.c "Yes, and I understand you have concerns."
    gloria.c "Of course I have concerns. You're a guy, so you may not get this, but if we put a woman under our roof, it'll only be so long before she starts thinking how great it would be to be the lady of the house instead of the hired help."
    gloria.c "She'll start working her claws into my husband and he won't even realize it. Then I'll need to boot her out before he ditches me for her and he'll be sore at me for a month for getting rid of the amazing sweet little thing who's been turning his head."
    call gloria_solution_options from _call_gloria_solution_options_12
  elif gloria.has_tag('something_to_discuss'):
    player.c "Yeah, it was. I have something I need to talk to you about before you go."
    gloria.c "Okay."
    call gloria_other_talk_topics from _call_gloria_other_talk_topics_8
    "With that resolved, you let Gloria dress and head home."
  else:
    player.c "Yeah, it was."
    "You don't have anything in particular to talk to Gloria about right now, so you let her dress and head home."
  rem tags 'current_session_rough' from gloria
  orgasm notify
  return

label gloria_contact_later_session_home:
  call forced_movement(gloria_house) from _call_forced_movement_22
  summon gloria no_follows
  add tags 'her_home' to gloria
  $ gloria.house_outfit += 1
  # scroll 1 through 4
  if gloria.house_outfit > 4:
    $ gloria.house_outfit = 1
  if gloria.house_outfit == 1:
    wt_image club_wife_house_outfit_1_1
    "When you arrive at Gloria's house, you're shown in by someone you don't know, who you assume is part of her hired help. Gloria is waiting for you in the living room."
    gloria.c "It's nice to see you again, even if you are planning on keeping your clothes on."
    if player.can_hypno(gloria):
      $ title = "What do you want to do with her?"
      menu:
        "Hypnotize her" if player.can_hypno(gloria):
          call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_4
        "Just talk with her":
          call gloria_home_talk from _call_gloria_home_talk_3
    else:
      call gloria_home_talk from _call_gloria_home_talk_4
  elif gloria.house_outfit == 2:
    wt_image club_wife_house_outfit_2_1
    "When you arrive at Gloria's house, you're greeted at the door by someone you don't know, who you assume is part of her hired help. They tell you that Gloria is out back with the pool girl. It doesn't take you long to locate them."
    wt_image club_wife_house_outfit_2_2
    "The pool girl seems to be just finishing up her duties."
    wt_image club_wife_house_outfit_2_3
    maria_gloria "Is there anything else I can do for you, Ma'am?"
    gloria.c "Not today, Maria. This gentleman needs to have a word with me. Shoo along now."
    maria_gloria "Yes, Ma'am."
    "Maria grins at you as she leaves the pool, seemingly tickled that you caught her eating Gloria out. "
    wt_image club_wife_house_outfit_2_4
    gloria.c "So what is it you want to talk to me about?"
    if player.can_hypno(gloria):
      $ title = "What do you want to do with her?"
      menu:
        "Hypnotize her" if player.can_hypno(gloria):
          call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_5
        "Just talk with her":
          call gloria_home_talk from _call_gloria_home_talk_5
    else:
      call gloria_home_talk from _call_gloria_home_talk_6
  elif gloria.house_outfit == 3:
    wt_image club_wife_house_outfit_3_1
    "When you get to her house, Gloria surprises you by answering the door herself."
    gloria.c "Hi!  I've been waiting for you."
    wt_image club_wife_house_outfit_3_2
    gloria.c "I know you just want to talk, but I really need to duck into the bathroom, where we`d have some privacy. Can I convince you to join me?"
    $ title = "What do you want to do with her?"
    menu:
      "Join her in the bathroom":
        wt_image club_wife_house_outfit_3_3
        gloria.c "Oh good!  Nobody knows you're in here with me, so no one will be scandalized by the sight of you fucking my wet, needy pussy."
        gloria.c "You will fuck me, won't you?"
        $ title = "Will you fuck her?"
        menu menu_gloria_home_outfit_3:
          "Hypnotize her" if player.can_hypno(gloria):
            call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_6
          "Fuck her":
            "Gloria's offer is tough to resist, so you don't bother."
            player.c "Spread your legs."
            wt_image club_wife_house_outfit_3_7
            gloria.c "Absolutely!  Can you fuck me up here?"
            player.c "No, you're too high up.  Get down on the floor."
            wt_image club_wife_house_outfit_3_8
            gloria.c "How about like this?"
            player.c "Much better."
            "She moans as you push yourself inside her."
            gloria.c "oooohhhh"
            wt_image club_wife_house_outfit_3_9
            "It doesn't long for her to cum.  Or you."
            gloria.c "Ooohhhh! ... Oooohhhh! ... OOHHH!! ...  Oh YEESSSSS!!!!  Cum on me!  I want to see you spurt all over me!!"
            player.c "[player.orgasm_text]"
            gloria.c "Oooohhhh!!!  That is so hot!  I'm in such a dirty mood today!!"
            wt_image club_wife_house_outfit_3_4
            "She certainly needs a shower, a clean one after the cum shower you just gave her. Fortunately, you're already in a bathroom, so she doesn't have far to go to clean up."
            if gloria.session == 5:
                "First though, you need to deal with the reason for your visit."
                player.c "We still haven't resolved the tension between you and your husband."
                gloria.c "I've followed your suggestions, but they haven't helped."
                player.c "Then we need to try something else."
                call gloria_solution_options from _call_gloria_solution_options_13
                "With that resolved, you leave her to clean up and head home."
            $ gloria.sex_count += 1
            $ gloria.orgasm_count += 1
            orgasm notify
          "Decline" if not gloria.has_tag('home_outfit_3_decline'):
            player.c "Gloria, I told you I was only coming over here to talk."
            gloria.c "I know but now that you're in here with me, let's be naughty. You can already see my pussy is ready for you ..."
            wt_image club_wife_house_outfit_3_6
            "She drops to her knees and takes out your dick, giving it a few gentle licks."
            gloria.c "... and I can see your cock still likes me. Put it in me. Put your dick in me and fuck me till I cum."
            add tags 'home_outfit_3_decline' to gloria
            jump menu_gloria_home_outfit_3
          "Just talk to her" if gloria.has_tag('home_outfit_3_decline'):
            player.c "I told you, Gloria, I'm only here to talk, not fuck."
            gloria.c "I want to fuck and you just want to chat. I hate that in a man. Fine, let's go back out in the hallway. There's no point in cramming ourselves into a little bathroom if all we're doing is talking."
            wt_image club_wife_house_outfit_3_2
            call gloria_home_talk from _call_gloria_home_talk_7
            "With that resolved, you head home."
      "Just talk to her":
        player.c "Not today, Gloria.  I'm just here to talk."
        gloria.c "How disappointing. I want to fuck and you just want to chat. I hate that in a man.  What are we talking about?"
        call gloria_home_talk from _call_gloria_home_talk_8
        "With that resolved, you head home."
  elif gloria.house_outfit == 4:
    wt_image club_wife_house_outfit_4_1
    "When you arrive at Gloria's house, you're shown in by someone you don't know, who you assume is part of her hired help. Gloria is waiting for you at the back of her house, overlooking her lawn."
    wt_image club_wife_house_outfit_4_5
    gloria.c "Ah, you're here."
    wt_image club_wife_house_outfit_4_2
    gloria.c "Please, have a seat.  What did you want to talk about today?"
    if player.can_hypno(gloria):
      $ title = "What do you want to do with her?"
      menu:
        "Hypnotize her" if player.can_hypno(gloria):
          call gloria_custom_hypnosis from _call_gloria_custom_hypnosis_7
        "Just talk with her":
          call gloria_home_talk from _call_gloria_home_talk_9
    else:
      call gloria_home_talk from _call_gloria_home_talk_10
  if gloria.has_tag('home_outfit_3_decline'):
    rem tags 'home_outfit_3_decline' from gloria
  call character_location_return(gloria) from _call_character_location_return_304
  call forced_movement(living_room) from _call_forced_movement_23
  change player energy by -energy_very_short notify
  return

label gloria_home_talk:
  if gloria.session == 5:
    player.c "We still haven't resolved the tension between you and your husband."
    gloria.c "I've followed your suggestions, but they haven't helped."
    player.c "Then we need to try something else."
    call gloria_solution_options from _call_gloria_solution_options_14
  else:
    gloria.c "What did you want to talk to me about?"
    call gloria_other_talk_topics from _call_gloria_other_talk_topics_9
  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_gloria:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_gloria:
  "This should really be between her and her husband."
  return

# Give Dildo
label give_di_gloria:
  "She looks like a woman who would already have a collection of these, don't you think?"
  return

# Use Fetch Toy
label use_ft_gloria:
  "You should speak to her husband first."
  return

# Give Jewelry
label give_jwc_gloria:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_gloria:
  "You should speak to her husband, first."
  return

# Give Lingerie
label give_li_gloria:
  "Based on how sheer her dress is, I'm not she wears any."
  return

# Give Love Potion
label give_lp_gloria:
  gloria.c "How sweet!  But I can't drink at the Club.  It wouldn't look good on my husband if I got tipsy."
  return

# Give Transformation Potion
label give_tp_gloria:
  gloria.c "How sweet!  But I can't drink at the Club.  It wouldn't look good on my husband if I got tipsy."
  return

# Give Ring of Secuality
label give_rs_gloria:
    gloria.c "That looks a lot like a ring my husband gave me, back when we were first going together!"
    return


# Use Water Bowl
label use_wb_gloria:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_gloria:
  "Her husband wouldn't be very happy with you, and that's likely to be a big problem.  Best to use the Will-Tamer on someone else."
  return

# Give Butt Plug
label give_bp_club_president:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_club_president:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_club_president:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_club_president:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_club_president:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_club_president:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_club_president:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_club_president:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_club_president:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_club_president:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_club_president:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label gloria_start_day:
    if player.has_tag('rep_needed') and not player.has_tag('rep_from_club_wife'):
        add tags 'something_to_discuss' to gloria
    return

# End Day
label gloria_end_day:
    # add tags 'no_hypnosis' to gloria
    rem tags 'visiting_you' 'her_home' 'first_club_visit' 'in_club_now' from gloria
    call character_location_return(gloria) from _call_character_location_return_305
    return

# End Week
label gloria_end_week:
    pass
    return

# Start Day
label club_president_start_day:
    pass
    return

# End Day
label club_president_end_day:
    pass
    return

# End Week
label club_president_end_week:
    pass
    return

## Club and Stage Labels
label gloria_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if gloria.has_tag('in_club_now'):
            $ gloria.location = club
    elif gloria.can_be_interacted:
        # Jasmine event
        if jasmine.has_tag('showgirl') and jasmine.club_whore_event_week > 0 and week > jasmine.club_whore_event_week and jasmine.downtown_event_checked_today < 2:
            call jasmine_club_whore_event from _call_jasmine_club_whore_event
        else:
            $ gloria.random_number = renpy.random.randint(1, 10)
            if gloria.random_number > 3:
                $ gloria.location = club
                add tags 'in_club_now' to gloria
    return

label club_president_club_call:
    pass # all of his events current happen first, before the normal c;ub calls
    return

label gloria_club_send_home:
    call character_location_return(gloria) from _call_character_location_return_306
    return

label club_president_club_send_home:
    pass # no other locations and never in club anyway except when he has something to say to you on first arrival
    return

## Frigid Content:
label gloria_elsa_ta_blowjob:
  wt_image club_wife_ta_bj_13
  "You invite Gloria to join you.  She arrives looking stunning.  You hope her confidence rubs off on Elsa and doesn't intimidate her."
  player.c "Gloria, I'd like you to show Elsa how to give a blowjob."
  wt_image club_wife_ta_bj_14
  gloria.c "Oh course!  Blow jobs are a great way to make a man putty in your hands, so to speak."
  wt_image club_wife_ta_bj_3
  gloria.c "The first thing you need to know about a man's cock is that it likes attention of any sort.  As soon as you kneel down in front of him he's likely to be hard, but a few strokes of your hand will make sure you have his full attention."
  wt_image club_wife_ta_bj_4
  gloria.c "Nuzzling up against his cock with your cheek is a great way to be affectionate and dirty at the same time.  It tells him 'I love you' and 'I'm about to fuck your brains out'."
  wt_image club_wife_ta_bj_5
  gloria.c "Give his balls lots of attention.  Men are very proud of their balls, and if you show an interest in them, it will endear you to them."
  wt_image club_wife_ta_bj_6
  gloria.c "Just make sure you make eye contact with him when you're sucking and licking his balls. You want to make sure he knows this isn't some little whore pleasuring his testicles, it's his girl, and if he wants this treatment in the future, he'll make sure he keeps you his girl and treats you right."
  wt_image club_wife_ta_bj_7
  gloria.c "By now his cock should be throbbing.  When you see it start to twitch, it's time to start licking his shaft."
  wt_image club_wife_ta_bj_8
  gloria.c "You probably know the underside of his cock head is his most sensitive area.  That's the part I like to tease last ..."
  wt_image club_wife_ta_bj_15
  gloria.c "... before giving him what he really wants - the feel of your lips wrapped around his cock."
  wt_image club_wife_ta_bj_9
  gloria.c "It doesn't matter how deep you take him in your mouth.  You can use your hand to stroke the part of his shaft you can't reach with your lips."
  wt_image club_wife_ta_bj_10
  gloria.c "What does matter is to make eye contact with him while you're sucking him.  You want him to know exactly whose face is providing him this pleasure. Besides, when you see how excited you're making him, it's a huge turn on.  It gets me wet every time."
  wt_image club_wife_ta_bj_16
  gloria.c "When he's ready to cum, you have a decision to make. You can always swallow his load.  It tastes great, or if there's too much you can just spit it out.  It doesn't matter.  He's already cum, so he should be happy with you regardless."
  wt_image club_wife_ta_bj_17
  gloria.c "Or you can let him shoot it on your skin.  You'd be amazed at how hot that feels.  Play around with him and you'll find out what turns him, and you, on most.  Lots of men like to see their jizz dripping down their girl's face."
  wt_image club_wife_ta_bj_2
  gloria.c "One of my favorites is to deposit his load on my tits."
  "Gloria pulls down the top of her dress ..."
  wt_image club_wife_ta_bj_11
  "... and starts jerking your cock off against her tits."
  wt_image club_wife_ta_bj_12
  "You adorn her breasts with strings of your sticky goo."
  player.c "[player.orgasm_text]"
  wt_image club_wife_ta_bj_1
  gloria.c "There.  I've taken his edge off.  It's your turn to practice now, Elsa.  You can take your time and go slow.  It'll be a while before he's ready to cum again."
  $ gloria.blowjob_count += 1
  orgasm
  add tags 'watched_teaching_aide_blowjob' to elsa
  return

label gloria_elsa_ta_blowjob_first_comment:
    gloria.c "Goodness, girl, don't be so greedy!  I know his cock looks delicious, but take your time and savor the moment.  Try licking him first."
    return

label gloria_elsa_ta_blowjob_second_comment:
    gloria.c "Most women do, even those who are too snooty to want to admit it.  A cock in your mouth may taste funny at first, but if it's the right cock on the right man, it's oddly satisfying, too."
    return

label gloria_elsa_ta_blowjob_third_comment:
    gloria.c "I think you've slathered him up enough.  You can take him into your mouth, now.  Just start with a little bit, though, to get used to it."
    return

label gloria_elsa_ta_blowjob_end:
    gloria.c "You did amazing, Elsa!  It even turned me on."
    wt_image frigid_hypnotized_desire_1_3
    elsa.c "Thanks, Gloria.  I appreciate you teaching me how to do that!  It felt nice to finally be able to do that for a guy."
    player.c "Don't I get to comment on how she did?"
    gloria.c "Don't be silly.  How quickly you came after I'd already blown you was comment enough."
    return

label gloria_elsa_ta_strip:
  if current_target.has_tag('teaching_aide'):
    wt_image club_wife_strip_1
    "You invite Gloria to join you.  She arrives looking stunning.  You hope her confidence rubs off on Elsa and doesn't intimidate her."
    wt_image club_wife_strip_2
    player.c "Gloria, Elsa here is a bit shy.  Could you show her how you take your clothes off?"
    gloria.c "Oh course!  Your body isn't something to be ashamed of, Elsa."
    wt_image club_wife_strip_3
    gloria.c "It's something you should have fun with."
    "Gloria removes her bra from under her dress..."
    wt_image club_wife_strip_4
    "...then pulls it off, popping her giant tits out of the dress as she does so."
    gloria.c "Ta da!"
    wt_image club_wife_strip_5
    gloria.c "Not only is it fun, taking your clothes off is a great way to turn a man into putty in your hands."
    elsa.c "Maybe if my breasts were as big as yours."
    gloria.c "Nobody has tits as big as me.  You don't need to be big to excite a man, you just need to be confident in what you have to offer.  You're beautiful, girl.  Show it off!  Tits, legs, ass.  Here, let me show you."
    wt_image club_wife_strip_6
    "Gloria reaches up under her dress and pulls off her panties."
    gloria.c "You can give him a little sneak peek at what's to come..."
    wt_image club_wife_strip_7
    gloria.c "...then take it away and make him wait for the next look..."
    wt_image club_wife_strip_8
    gloria.c "...and wait..."
    wt_image club_wife_strip_9
    gloria.c "...and wait."
    gloria.c "He's not focused on my tits now, is he?  He's too busy wondering when I'm going to give him another look at my pussy."
    gloria.c "It doesn't hurt to make a man wonder if you're going to ever show him what he wants to see..."
    wt_image club_wife_strip_10
    gloria.c "...ta da!"
    "With a flourish, Gloria pulls off her dress and hops up on the coffee table."
    wt_image club_wife_strip_11
    gloria.c "Personally, I believe in giving him what he's been waiting for.  Especially when he's being a good boy."
    wt_image club_wife_strip_12
    gloria.c "And if you really want to hold his interest, you can give him a closer look at what he can have if he's a really good boy."
    wt_image club_wife_strip_13
    gloria.c "Your turn now!.  You can do this.  You're a strong, sexy woman.  Show us how confident and beautiful you are, and feel it yourself, inside."
    add tags 'watched_teaching_aide_strip' 'ta_strip_bold' 'watched_teaching_aide_strip_gloria' to elsa
  else:
    $ current_target = None
  return

label gloria_elsa_ta_strip_end:
  wt_image club_wife_strip_13
  gloria.c "You were great Elsa!  I'm all wet between my legs myself now."
  elsa.c "Thanks, Gloria!  I really appreciate you teaching me."
  return

## Good Girlfriend Content
label gloria_terri_ta_blowjob:
    if current_target.has_tag('teaching_aide'):
        wt_image club_wife_ta_bj_13
        "You invite Gloria to join you. She arrives looking stunning. You hope her confidence rubs off on Terri and doesn't intimidate her."
        player.c "Gloria, Terri is trying to learn how to be a better girlfriend for her boyfriend. I'd like you to show Terri how to give a proper blow job."
        wt_image club_wife_ta_bj_14
        gloria.c "Oh course! Blow jobs are a great way to make a man putty in your hands, so to speak."
        wt_image club_wife_ta_bj_3
        gloria.c "The first thing you need to know about a man's cock is that it likes attention of any sort. As soon as you kneel down in front of him he's likely to be hard, but a few strokes of your hand will make sure you have his full attention."
        wt_image club_wife_ta_bj_4
        gloria.c "Nuzzling up against his cock with your cheek is a great way to be affectionate and dirty at the same time. It tells him 'I love you' and 'I'm about to fuck your brains out'."
        wt_image club_wife_ta_bj_5
        gloria.c "Give his balls lots of attention. Men are very proud of their balls, and if you show an interest in them, it'll endear you to them."
        wt_image club_wife_ta_bj_6
        gloria.c "Just make sure you make eye contact with him when you're sucking and licking his balls. You want to make sure he knows this isn't some little whore pleasuring his testicles, it's his girl, and if he wants this treatment in the future, he'll make sure he keeps you his girl and treats you right."
        wt_image club_wife_ta_bj_7
        gloria.c "By now his cock should be throbbing. When you see it start to twitch, it's time to start licking his shaft."
        wt_image club_wife_ta_bj_8
        gloria.c "You probably know the underside of his cock head is his most sensitive area. That's the part I like to tease last ..."
        wt_image club_wife_ta_bj_15
        gloria.c "... before giving him what he really wants - the feel of your lips wrapped around his cock."
        wt_image club_wife_ta_bj_9
        gloria.c "It doesn't matter how deep you take him in your mouth. You can use your hand to stroke the part of his shaft you can't reach with your lips."
        wt_image club_wife_ta_bj_10
        gloria.c "What does matter is to make eye contact with him while you're sucking him. You want him to know exactly whose face is providing him this pleasure. Besides, when you see how excited you're making him, it's a huge turn on. It gets me wet every time."
        wt_image club_wife_ta_bj_16
        gloria.c "When he's ready to cum, you have a decision to make. You can always swallow his load. It tastes great, or if there's too much you can just spit it out. It doesn't matter. He's already cum, so he should be happy with you regardless."
        wt_image club_wife_ta_bj_17
        gloria.c "Or you can let him shoot it on your skin. You'd be amazed at how hot that feels. Play around with him and you'll find out what turns him, and you, on most. Lots of men like to see their jizz dripping down their girl's face."
        wt_image club_wife_ta_bj_2
        gloria.c "One of my favorites is to deposit his load on my tits."
        "Gloria pulls down the top of her dress ..."
        wt_image club_wife_ta_bj_11
        "... and starts jerking your cock off against her tits."
        wt_image club_wife_ta_bj_12
        "You adorn her breasts with strings of your sticky goo."
        player.c "[player.orgasm_text]"
        wt_image club_wife_ta_bj_1
        gloria.c "There. I've taken his edge off. It's your turn to practice now, Terri. You can take your time and go slow. It'll be a while before he's ready to cum again."
        $ gloria.blowjob_count += 1
        orgasm
        add tags 'watched_teaching_aide_blowjob' to terri
    else:
        $ current_target = None
    return

label gloria_terri_ta_strip:
    if current_target.has_tag('teaching_aide'):
        wt_image club_wife_strip_1
        "You invite Gloria to join you. She arrives looking stunning. You hope her confidence rubs off on Terri and doesn't intimidate her."
        wt_image club_wife_strip_2
        player.c "Gloria, Terri is trying to learn how to be a better girlfriend for her boyfriend. Could you please show her how you take your clothes off when you're trying to excite a man?"
        gloria.c "Oh course! The sight of your body is the perfect way to please your guy, Terri."
        wt_image club_wife_strip_3
        gloria.c "It's something you should have fun with."
        "Gloria removes her bra from under her dress ..."
        wt_image club_wife_strip_4
        "... then pulls it off, popping her giant tits out of the dress as she does so."
        gloria.c "Ta da!"
        wt_image club_wife_strip_5
        gloria.c "Not only is it fun, taking your clothes off is a great way to turn a man into putty in your hands."
        "Terri watches Gloria closely, her cheeks blushing furiously."
        terri.c "Maybe if my breasts were as big as yours."
        gloria.c "Nobody has tits as big as me. You don't need to be big to excite a man, you just need to be confident in what you have to offer. You're beautiful, girl. Show it off! Tits, legs, ass. Here, let me show you."
        wt_image club_wife_strip_6
        "Gloria reaches up under her dress and pulls off her panties."
        gloria.c "You can give him a little sneak peek at what's to come ..."
        wt_image club_wife_strip_7
        gloria.c "... then take it away and make him wait for the next look ..."
        wt_image club_wife_strip_8
        gloria.c "... and wait ..."
        wt_image club_wife_strip_9
        gloria.c "... and wait. He's not focused on my tits now, is he? He's too busy wondering when I'm going to give him another look at my pussy."
        gloria.c "It doesn't hurt to make a man wonder if you're going to ever show him what he wants to see ..."
        wt_image club_wife_strip_10
        gloria.c "... ta da!"
        "With a flourish, Gloria pulls off her dress and hops up on the coffee table."
        wt_image club_wife_strip_11
        gloria.c "Personally, I believe in giving him what he's been waiting for. Especially when he's being a good boy."
        wt_image club_wife_strip_12
        gloria.c "And if you really want to hold his interest, you can give him a closer look at what he can have if he's a really good boy."
        wt_image club_wife_strip_13
        "You enjoy Gloria's finale, but Terri's turned so red, you're afraid she may catch fire. Perhaps it's embarrassment at witnessing Gloria's display, or perhaps it's something else."
        gloria.c "Your turn now! You can do this. You're a strong, sexy woman. Show us how confident and beautiful you are, and feel it yourself, inside."
        "Terri takes a deep breath as Gloria settles in beside you to watch the show."
        add tags 'watched_teaching_aide_strip' to terri
    else:
        $ current_target = None
    return

## Loving Wife Content
label gloria_sarah_positive_role_talk_teaching_aide:
    if current_target.has_tag('teaching_aide') and not sarah.has_tag(tag_expression):
        wt_image club_wife_ta_visit_1
        "Gloria comes right over."
        wt_image lw_visit_2_2
        if current_target.has_tag('sarah_positive_role_sex_done'):
            player.c "Gloria, you remember Sarah?"
            gloria.c "Of course.  How nice to see you again, dear."
            sarah.c "Hi!"
            wt_image club_wife_ta_visit_1
            player.c "I thought you could tell Sarah about how your relationship with your husband has been since you started having sex with other people."
        else:
            player.c "Gloria, this is Sarah."
            gloria.c "Charmed!"
            sarah.c "Hi!  Nice to meet you."
            wt_image club_wife_ta_visit_1
            player.c "Sarah's husband wants her to have sex with his friends.  I thought you could tell her about how your relationship with your husband has been since the two of you started having sex with other people."
        wt_image lw_visit_2_11
        sarah.c "Your husband doesn't think you're a .. you know, slut?"
        wt_image club_wife_ta_visit_2
        gloria.c "What a terrible word!  Not at all, dear.  I like sex.  It's one of the things my husband loves about me.  And he's rather fond that I let him sleep with other women, too."
        wt_image lw_visit_2_12
        sarah.c "Doesn't that worry you?  I mean, what if he finds someone he wants to be with more than you?"
        wt_image club_wife_ta_visit_1
        if gloria.session == 8:
            gloria.c "I do worry about that, yes.  Less now than I used to, thanks to Mr. Wife Trainer's help.  But what can we do?"
        else:
            gloria.c "I do worry about that, yes.  But what can we do?"
        gloria.c "Be the best possible wives we can, I think.  Do our best to make our husbands happy without letting them walk all over us.  It's not like he couldn't find someone else anyway."
        wt_image lw_visit_2_12
        sarah.c "That's true.  My husband certainly could, if he wanted to."
        wt_image club_wife_ta_visit_2
        gloria.c "Mine, too.  I figure, a little sex on the side, when both parties know about it, helps cement your relationship.  He's reminded that I'm desirable to other men, something it's good not to let him forget. And both of us know when and who we're getting some from, so there's no secrets to undermine trust."
        wt_image club_wife_ta_visit_1
        "The two of them fall into a long conversation about their husbands, their marriages, and extramarital sex."
        wt_image lw_visit_2_4
        "Eventually, it gets late, and Gloria leaves."
        sarah.c "Thanks for asking Gloria to chat with me.  It helped a lot."
        add tags 'positive_teaching_aide_resolution_today' 'met_teaching_aide_gloria' to sarah
    else:
        $ current_target = None
    return

label gloria_sarah_positive_role_sex_teaching_aide:
    if current_target.has_tag('teaching_aide'):
        wt_image club_wife_ta_sex_1
        if not current_target.has_tag('sarah_positive_role_talk_done'):
            player.c "Sarah, this is my friend Gloria."
            wt_image lw_visit_4_8
            sarah.c "Hello"
            gloria.c "How nice to meet you, Sarah."
        else:
            player.c "You remember Gloria?"
            wt_image lw_visit_4_8
            sarah.c "Of course!"
            gloria.c "Hello, again!"
        wt_image club_wife_ta_sex_1
        player.c "Gloria and I are going to have sex together while you watch."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people make love.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image club_wife_ta_sex_6
        "Gloria sheds her clothes and gets on the bed as Sarah watches."
        wt_image lw_visit_4_6
        sarah.c "Isn't this embarrassing, having me here watching?"
        wt_image club_wife_ta_sex_6
        gloria.c "Not at all.  I watch my husband fuck other women all the time, and sometimes they watch him fuck me.  It's quite hot, actually."
        wt_image club_wife_ta_sex_7
        gloria.c "Look how hard his cock is. It's such a thrill when you can get a guy excited so easily. He wants it inside me, and I'm already wet enough that I want him inside me, too."
        wt_image club_wife_ta_sex_8
        gloria.c "Ooohhhh ... that feels good!  Do you want me to teach her how to pleasure you in this position?"
        player.c "Not in detail.  Today's lesson is that it can be fun to watch and be watched.  Just get the two of us off, Gloria, and I'm sure Sarah will pick up some pointers on the way."
        wt_image club_wife_ta_sex_3
        gloria.c "Okay"
        "Gloria bucks her hips back against you, twisting them side to side while gradually increasing the pace at which she thrusts towards you."
        wt_image lw_visit_4_6
        "Sarah watches intently as Gloria's breathing and yours gets faster and faster as you near orgasm."
        sarah.c "Are you sure it's okay for me to be watching?"
        wt_image club_wife_ta_sex_3
        gloria.c "It's better than okay.  Just give me a moment to change position.  I want to feel him deeper inside me than he can get like this."
        wt_image club_wife_ta_sex_4
        "Gloria flips herself around and starts fucking you faster. It doesn't take long for her to cum."
        gloria.c "oooohhhhh ... oooohhhh ... yeesssss"
        wt_image lw_visit_4_5
        sarah.c "You actually came? Even with me here?"
        wt_image club_wife_ta_sex_2
        gloria.c "Mmmm, I sure did, but he hasn't yet.  Do you want to get him off?"
        wt_image lw_visit_4_4
        sarah.c "No!"
        wt_image club_wife_ta_sex_2
        gloria.c "Suit yourself, but I'm going to get him off.  A fuck like that deserves a reward."
        wt_image club_wife_ta_sex_5
        "A moment later, Gloria is milking the jizz out of your cock and onto her face."
        player.c "[player.orgasm_text]"
        wt_image club_wife_ta_sex_9
        gloria.c "Mmmm.  See.  You being here didn't keep him from cumming either."
        player.c "I think Gloria had fun, don't you?"
        wt_image lw_visit_4_5
        "Sarah nods."
        player.c "And she didn't look ridiculous having sex, did she?"
        wt_image lw_visit_4_9
        sarah.c "No.  Not at all.  You've made your point.  For some people, sex doesn't always have to be in private for it to be fun.  I need to go home and think about this."
        wt_image lw_visit_4_10
        "Sarah looks at you with a little more interest than she has before.  You can't help yourself from teasing her."
        player.c "You can take your panties off while you think about it, if you want."
        $ gloria.sex_count += 1
        $ gloria.orgasm_count += 1
        $ gloria.facial_count += 1
        orgasm
        add tags 'met_teaching_aide_gloria_sex' 'watched_teaching_aide_this_weekend' to sarah
    else:
        $ current_target = None
    return

## Trailer Trash Content
label gloria_becky_sue_fix_clothes_message:
    "Gloria has great taste in clothes and while she's a slut at heart, she comes across as pure class. She'd likely help Becky Sue dress to fit in with the moneyed class."
    return

label gloria_becky_sue_fix_clothes_help:
    wt_image club_wife_shopping_3
    player.c "Gloria, Becky Sue needs some new clothes."
    gloria.c "Oh gawd, does she ever."
    wt_image tt_fix_clothes_3
    becky_sue.c "Excuse me?"
    wt_image club_wife_shopping_4
    gloria.c "Oh I don't mean anything bad by that, child. I'm sure everyone dresses like this back in ... wherever it is you come from."
    wt_image club_wife_shopping_1
    gloria.c "But just at how pretty you are! You could be so much more than ... this. Oh yes, I can just picture how nice you'll look with the right ensemble."
    wt_image club_wife_shopping_2
    gloria.c "Come, come. We have a lot of work to do. So many stores to visit. Hurry up!"
    wt_image tt_fix_clothes_1
    "Gloria's not always an easy person to warm up to, and Becky Sue has more than a few reservations as she grabs her handbag and follows the older woman."
    "Whatever else she may be, however, Gloria is clearly comfortable with the upper echelon of society. Her encouragement and approval when dressing Becky Sue in the 'right type of clothes' provides more comfort to the younger woman than anyone else could that she will be accepted in the best social circles as long as she presents herself 'properly'."
    "Gloria's acceptance even means enough to Becky Sue that she'll be a bit more more open to future suggestions from you."
    change becky_sue sos by 20
    change becky_sue resistance by -5
    return

## Character Specific Timers
# Other Talk Topics
label gloria_other_talk_topics:
    ## NOTE: consider changing this to an automated system that will pick up additional conversation options added in new character scripts
    if gloria.discussed_barista == 2:
        player.c "I have a solution to yours and your husband's problem. I've found the ideal person for you. She's beautiful, eager to please, sexually adventurous, and there's absolutely no chance she will try to take your husband away from you."
        gloria.c "How do you know?"
        player.c "Because she's a confirmed lesbian."
        gloria.c "Are you sure?  If she is, she's not going to be much use to my husband."
        player.c "Sam has a special interpretation of her own sexuality. She's only interested in girls, but she'll gladly fuck boys if she feels they need or deserve some sexual relief. Your husband is going to be completely happy with her. You will be, too."
        gloria.c "Bring her by in the morning and we'll check her out for ourselves."
        $ gloria.discussed_barista = 3
    else:
        # ask for rep gain
        if player.has_tag('rep_needed') and not player.has_tag('rep_from_club_wife'):
          player.c "Business has been a bit slow lately, Gloria. Do you think you could put in a good word for me?"
          gloria.c "Well I can't tell people that I'm seeing the wife trainer. That wouldn't be good for my husband or I. But I could spread the word around the Club that I've been hearing good things about your services. That should provide your reputation with a little boost.  Leave it with me."
          add tags 'rep_from_club_wife' to player
          rem tags 'rep_needed' from player
          change player reputation by 1 notify
        ## now call all talk options for Marilyn related to other characters
        call for_call_labels(label_list = [p.short_name + '_gloria_other_talk_option' for p in get_people(tagged_with_all=['gloria_other_talk_option_possible'])]) from _call_for_call_labels_24
        rem tags 'something_to_discuss' from gloria
    return

# Solution Options
label gloria_solution_options:
  $ title = "What do you suggest?"
  menu:
    "She shouldn't be so insecure":
      player.c "Do you really think he'd dump you that easily?"
      gloria.c "No. Maybe. I don't know. He's a successful man. I ... I don't really do much except the occasional fundraiser and meet-and-greet at the Club."
      gloria.c "We've been together a long time. I know he loves me, but men get bored and he could find younger and prettier eye candy to drape on his arm if he wanted to."
      player.c "You're still pretty fine eye candy. But perhaps you need something more in your life. You might be more interesting to him if you had a career of your own."
      gloria.c "Like what?"
      $ title = "What should she do?"
      menu:
        "Work as your teaching aide":
          player.c "How about you work with me?"
          gloria.c "What do you mean?"
          player.c "As my teaching aide. You know your way around a man's body and you're confident in your own. You could help some of the women I work with."
          gloria.c "Do you think I'd be good at that?"
          player.c "I'm sure you would be."
          gloria.c "Okay.  We can try that. I just need to check with my husband, first, to make sure he's okay with it."
          gloria.c "And I'm still not going to let him bring a girl into our house. Not yet anyway."
          "You may need to keep looking for a better long-term solution to meet her husband's objective, but for now you've made some progress, and assuming her husband agrees, you've found yourself a new assistant while you're at it.  You should check in at the Club to get his thoughts on the matter."
          $ club_president.discussion_pending = 2
          $ club_president.discussion_week = week - 1
        "Do more around the Club":
          player.c "Perhaps there's something more you could be doing around the Club?  A more formal role perhaps?"
          gloria.c "Hmmmm  I have been thinking that the Club could use some better entertainment.  More formal and elaborate shows, for example."
          player.c "Perhaps you should create a new Event Coordinator role?"
          gloria.c "That's not a bad idea. We could also have dances and celebrations on special occasions. Make it more of a true social center for our members."
          player.c "That sounds like a great idea to me.  You'll be fabulous at it."
          gloria.c "Okay. I'll talk to my husband about it. But I'm still not going to let him bring a girl into our house.  Not yet anyway."
          "You may need to keep looking for a better long-term solution to meet her husband's objective, but for now you've made some progress."
          $ club_president.discussion_pending = 3
          $ club_president.discussion_week = week - 1
        "Reconsider":
          jump gloria_solution_options
      $ gloria.session = 7
    "She should meet him partway" if not gloria.has_tag('discussed_her_maid') or not gloria.has_tag('discussed_hire_temp') or not gloria.has_tag('discussed_evening_out'):
      player.c "If this is important to your husband, ignoring him may not be the best approach.  Perhaps you should try to meet him partway."
      gloria.c "Hmmmm.  Maybe.  What were you thinking?"
      $ title = "What do you suggest?"
      menu:
        "Be the live in servant" if not gloria.has_tag('discussed_her_maid'):
          player.c "Why don't you pretend to be the live in servant for him?"
          gloria.c "I'm not sure that would work.  He's looking for someone to look after him when I'm not home or am too tired to have sex."
          player.c "Does it hurt to try?  A little role play can be fun and he may appreciate that you're recognizing his interest and trying to accommodate him."
          gloria.c "I suppose.  Okay, I'll give it a try."
          $ club_president.discussion_pending = 4
          $ club_president.discussion_week = week
          add tags 'discussed_her_maid' to gloria
        "Hire a girl on a temporary basis" if not gloria.has_tag('discussed_hire_temp'):
          player.c "What if you try things out on a trial basis?  Hire a girl on a short term contract and see how it works."
          gloria.c "I don't know.  I know what women are like.  This may just be inviting trouble."
          player.c "But if she's on a short-term contract, she'll only be with you for a few weeks and then she'll be gone."
          gloria.c "I suppose.  Okay, I'll give it a try."
          $ club_president.discussion_pending = 5
          $ club_president.discussion_week = week
          add tags 'discussed_hire_temp' to gloria
        "Treat him to an evening out" if not gloria.has_tag('discussed_evening_out'):
          player.c "What if you give him a special treat, so he feels appreciated even you're not able to accommodate him on a live in servant."
          gloria.c "What are you thinking of?"
          player.c "I don't know.  What does he like to do that you haven't done for a while?"
          gloria.c "Hmmmm.  I suppose I could take him for an evening out.  He has been working really hard lately, and it's been a while since I helped him relax.  Okay, I'll give it a try."
          $ club_president.discussion_pending = 6
          $ club_president.discussion_week = week
          add tags 'discussed_evening_out' to gloria
        "Reconsider":
          jump gloria_solution_options
      $ gloria.session = 5
  return

########### ROOMS ###########
# Club - Club President: Discussion Pending
label club_president_discussion_pending:
    call for_call_labels(label_list = [i + '_club_president_discussion_reason' for i in club_president_discussion_reason_list]) from _call_for_call_labels_29
    "He shows you out of his office and disappears."
    wt_image club.image
    $ club_president.discussion_pending = 0
    return

label gloria_club_president_discussion_reason:
  if club_president.discussion_pending == 1:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "Tough luck on the session with my wife. I understand it didn't go so well."
    club_president.c "Don't feel bad. If I haven't been able to convince her, I didn't think you'd be able to do so. I'll send along your payment. I know we agreed you'd be paid only if you had success, but I appreciate you trying."
    change player money by 25 notify
  elif club_president.discussion_pending == 2:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "My wife tells me she wants to work with you. That's fine with me. She's quite excited about it."
    club_president.c "It doesn't really solve my problem, but I think I see where you're going with this. She's got something new and interesting in her life. Maybe that leads to her being more open to a change at home."
    club_president.c "I'll send along your payment."
    if samantha.has_tag('discussed_good_at') and samantha.has_tag('discussed_school'):
      $ gloria.discussed_barista = 1
    $ gloria.solution_status = 2
    $ gloria.session = 7
    call convert(gloria, "teaching_aide") from _call_convert_132
    change player money by 25 notify
  elif club_president.discussion_pending == 3:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "My wife was talking to me about doing more around the Club. She has ideas for some new events and asked me to appoint her Event Coordinator. She tells me it was your idea. She's quite excited about it."
    club_president.c "It doesn't really solve my problem, but I think I see where you're going with this. She's got something new and interesting in her life. Maybe that leads to her being more open to a change at home."
    club_president.c "And if nothing else, maybe the Club benefits if some of her ideas turn out to be any good."
    club_president.c "I'll send along your payment."
    if samantha.has_tag('discussed_good_at') and samantha.has_tag('discussed_school'):
      $ gloria.discussed_barista = 1
    $ gloria.show_week = week + 4
    $ gloria.solution_status = 3
    $ gloria.session = 7
    change player money by 25 notify
  elif club_president.discussion_pending == 4:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "I wanted to thank you for the work you did with Gloria. She surprised me when I got home last Friday and told me it was your idea."
    wt_image club_wife_her_maid_1
    club_president.c "{i}She was dressed up in a maid's outfit and washing the dishes. I can't remember Gloria ever washing dishes!{/i}"
    wt_image club_wife_her_maid_2
    club_president.c "{i}Not only that, but she'd cooked supper. I was a little worried that she'd accidentally poison us both, but she insisted I taste it and it wasn't awful.{/i}"
    club_president.c "{i}Considering she likely hasn't cooked anything for 20 years that didn't involve a microwave, I thought that was pretty good.{/i}"
    wt_image club_wife_her_maid_3
    club_president.c "{i}When I asked her if the new maid was available to perform any other domestic duties, she informed me I was in luck ...{/i}"
    wt_image club_wife_her_maid_4
    club_president.c "{i}... dinner wouldn't be ready for another 20 minutes, and the maid would keep me entertained while I wait.{/i}"
    wt_image club_wife_her_maid_5
    club_president.c "{i}By this time I was too excited to settle for just a blow job from my 'new' serving girl, but I couldn't decide ... whether I wanted to fuck her in or out of the slutty maid's clothes she was wearing.{/i}"
    wt_image club_wife_her_maid_6
    club_president.c "{i}I ended up compromising, taking off the top part of her uniform ...{/i}"
    wt_image club_wife_her_maid_7
    club_president.c "{i}... and fucking her in her stockings and heels.{/i}"
    wt_image club_wife_her_maid_8
    club_president.c "{i}It wasn't the best sex we've had as a couple, but it was probably top 20.{/i}"
    wt_image club_wife_her_maid_9
    club_president.c "{i}And we both came before the supper could burn.{/i}"
    wt_image club_pres_2
    club_president.c "She'll never keep it up. Cleaning and cooking hold no appeal to her, even as a pretend maid, but I had a great time while she tried being my live in serving girl. So good job!"
    club_president.c "I'll send along your fee. Feel free to call my wife up and spend some time with her again whenever you want. Keep delivering results like that and I'm sure she'll be ready to let a serving girl move in with us soon."
    add tags 'available_for_visit' to gloria
    change player money by 25 notify
  elif club_president.discussion_pending == 5:
    wt_image gloria.image
    "Gloria accosts you as soon as you enter the Club."
    gloria.c "Well that was a terrible idea!"
    player.c "What was?"
    gloria.c "Convincing me to hire a live in serving girl on a temporary basis."
    player.c "What happened?"
    wt_image club_wife_temp_maid_1
    gloria.c "{i}For starters, young women today have no idea how to dress. I burst out laughing when I saw the sweat pants and t-shirt she brought with her to clean our house in.{/i}"
    wt_image club_wife_temp_maid_2
    gloria.c "{i}Fortunately I'd anticipated this sort of failure and I'd invested in suitable clothing that better reflects the standards of our household.{/i}"
    wt_image club_wife_temp_maid_3
    gloria.c "{i}She seemed quite happy with the dress.  I don't think she's used to having nice things.  Who knows where the temp agencies get girls from these days.{/i}"
    wt_image club_wife_temp_maid_4
    gloria.c "{i}After she changed she flounced right over to the room where my husband was working to show off her new outfit.{/i}"
    wt_image club_wife_temp_maid_5
    gloria.c "{i}As I was leaving to go to a fundraiser, I saw she was giving him head in front of his desk. I didn't mind that. I knew he had a busy day ahead of him, and that was why she was here: to make life easier for my husband.{/i}"
    gloria.c "{i}If anything, she looked bored while she sucked him, but then girls these days seem bored doing anything.{/i}"
    wt_image club_wife_temp_maid_6
    gloria.c "{i}When I got home later that afternoon, I could hear groans echoing throughout the house.{/i}"
    wt_image club_wife_temp_maid_7
    gloria.c "{i}The guilty look on her face as I walked in on her told me she knew exactly what she was doing.{/i}"
    wt_image club_wife_temp_maid_8
    gloria.c "{i}My husband flipped her over and confirmed what I suspected from the moment I walked in on them. He had his cock buried in her ass.{/i}"
    wt_image club_wife_temp_maid_9
    gloria.c "{i}I was married to my husband for a year before I let him have my ass. This little hussy had offered it up to him in less than a day, and was acting like having his dick in her butt was the best thing since vibrating panties.{/i}"
    wt_image club_wife_temp_maid_10
    gloria.c "{i}It was all an act. Even with my husband's finger in her twat, she wasn't getting off on the butt fucking, not matter how much she moaned and groaned.{/i}"
    wt_image club_wife_temp_maid_11
    gloria.c "{i}My husband enjoyed himself, of course, just like she knew he would.{/i}"
    wt_image club_wife_temp_maid_12
    gloria.c "{i}A quick check after he pulled out, however, confirmed that while her anus was dripping wet from my husband's spunk, her cunt was dry as a bone.{/i}"
    wt_image club_wife_temp_maid_13
    gloria.c "{i}I leaned over her while the sperm was still dripping out of her ass.{/i}"
    gloria.c "You're fired you little gold digger, and if you're not out of my house in 15 minutes, I'm telling the temp agency never to get you work in this town again."
    wt_image gloria.image
    player.c "She was just doing what she was hired to do, looking after your husband."
    "Gloria rolls her eyes."
    gloria.c "Men! She was angling for my husband and she didn't even have the good sense to wait a few days before showing her claws."
    wt_image club_pres_2
    "Gloria storms off. As she leaves, her husband pokes his head out of his office and waves you over."
    club_president.c "Oh hi! There you are!"
    club_president.c "Stay away from Gloria for a few hours. She's a little pissed, but she'll get over it."
    club_president.c "Great job on convincing Gloria to let us bring in a live in serving girl on a temporary basis. It's my fault the experiment got cut short. I should have played things cooler."
    club_president.c "The little tart the temp agency sent over started making googly eyes at me about an hour after Gloria left. She'd been through the house and tidied all the rooms by that point, and must have figured out that we have some money."
    club_president.c "After that she followed me around like a puppy dog. Can I get you a glass of water? Would you like a snack? Did you want your cock sucked again? Maybe I could do something special for you?"
    club_president.c "When she started asking me if there was anything my wife didn't like to do that maybe she could do for me, I knew this arrangement wasn't going to last. But I should have played it out."
    club_president.c "Who knows what I could have got her to do over the next few weeks if I'd taken my time? Sadly I'd been thinking about her skinny little ass, so different from Gloria's."
    club_president.c "When I asked her if she liked it up the butt, I could tell she was lying when she said yes. That should have been enough to tell me I had a gold mine here to be worked slowly over the next few weeks."
    club_president.c "Instead, the thought of burying my cock in her ass was too much. And I didn't think Gloria would be home early enough to catch us. "
    club_president.c "When she walked in, I thought maybe I could make it look like the tart liked it in the butt, but even when I started fingering her pussy she wasn't a good enough actress to convince anyone that anal was something she likes."
    club_president.c "By that point I knew Gloria would see through what was going on, so I just enjoyed my one and only ride in her tight ass. Anyway, despite me screwing things up, you did a good job."
    club_president.c "I'll send along your fee. Feel free to call my wife up and spend some time with her again whenever you want. I know I made our ultimate objective a little more difficult, but I'm interested in finding out what you can convince her to do next."
    add tags 'available_for_visit' to gloria
    change player money by 25 notify
  elif club_president.discussion_pending == 6:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "I wanted to thank you for the work you did with Gloria. She took me out on the weekend and told me it was your idea, that she hasn't been doing enough lately to make me feel appreciated."
    wt_image club_wife_evening_out_1
    club_president.c "{i}She had our limo driver take us out of town, to a nice cozy little place for a dinner and some drinks.{/i}"
    wt_image club_wife_evening_out_2
    club_president.c "{i}After we finished eating, she took me to a private room at the back of the restaurant. She'd hired some university student to give us a private show for 'dessert'.{/i}"
    wt_image club_wife_evening_out_3
    club_president.c "{i}I think I mentioned my wife likes girls? Anyway, the student wasn't much of a dancer, so my wife decided to give her some encouragement.{/i}"
    wt_image club_wife_evening_out_4
    club_president.c "{i}The stripper's dancing didn't really improve, but at least she loosened up ...{/i}"
    wt_image club_wife_evening_out_5
    club_president.c "{i}... which made the rest of the show more enjoyable for all of us.{/i}"
    wt_image club_wife_evening_out_6
    club_president.c "{i}When my wife told her there was a tip available for her back in our hotel room, she readily agreed, and not just because she's a broke college student. Her juices were flowing as much as my wife's.{/i}"
    wt_image club_wife_evening_out_7
    club_president.c "{i}It's been a while since my wife has brought such a young, tight body to our bed as a surprise treat for me.{/i}"
    wt_image club_wife_evening_out_8
    club_president.c "{i}I made sure they were both wet ...{/i}"
    wt_image club_wife_evening_out_9
    club_president.c "{i}... and they both made sure I was hard.{/i}"
    wt_image club_wife_evening_out_10
    club_president.c "{i}Then I fucked my wife to orgasm ...{/i}"
    wt_image club_wife_evening_out_11
    club_president.c "{i}... before moving on to the little bit she'd brought me.{/i}"
    wt_image club_wife_evening_out_12
    club_president.c "{i}When the young thing squeaked out an orgasm, it was awfully tempting to let myself go inside her tight little pussy, but I had no way to be sure she was on birth control.{/i}"
    wt_image club_wife_evening_out_13
    club_president.c "{i}So just in case she was trying to trap me into getting her pregnant, I pulled out and let my wife swallow my load.{/i}"
    wt_image club_pres_2
    club_president.c "That's one of the best times my wife and I have had together for quite a while. I'll send along double your normal fee."
    club_president.c "Feel free to call my wife up and spend some time with her again whenever you want.  Keep delivering results like that and I'm sure she'll be ready to let a serving girl move in with us soon."
    add tags 'available_for_visit' to gloria
    change player money by 50 notify
  elif club_president.discussion_pending == 7:
    wt_image club_pres_2
    club_president.c "Oh hi! There you are!"
    club_president.c "Hey, I have to tell you.  Sam is amazing!"
    wt_image barista_club_job_2_1
    club_president.c "{i}Gloria left really early this morning, and I had to get going as well. I asked Sam if she could brew me a cup of coffee.{/i}"
    wt_image barista_club_job_2_9
    club_president.c "{i}I guess she's used to getting up early for her old job's morning shift, as she didn't complain.  She got right to work.{/i}"
    wt_image barista_club_job_2_2
    club_president.c "{i}Coffee's kind of Sam's thing, and I have to say it was a really good cup of coffee.{/i}"
    wt_image barista_club_job_2_3
    club_president.c "{i}Before I finished the coffee, though, I had to sample those perky morning nipples of hers.  She really does like helping people.  She stood beside me at the kitchen table with her breasts at mouth level while I drank my coffee.{/i}"
    wt_image barista_club_job_2_4
    club_president.c "I have a really busy day ahead. Can I get a quick fuck in before I go?"
    samantha.c "Uh, sure.  How do you want me?"
    wt_image barista_club_job_2_5
    club_president.c "{i}That was probably the toughest decision I've had to make today. I eventually decided to have her ride me.{/i}"
    wt_image barista_club_job_2_6
    club_president.c "{i}For a lesbian, she's amazingly good at riding dick. It took everything I had to keep from cumming watching her bounce up and down on my cock.{/i}"
    wt_image barista_club_job_2_7
    club_president.c "{i}I had to flip her over, though, and pound into that sweet bubble butt of hers before I left.{/i}"
    wt_image barista_club_job_2_8
    if gloria.has_tag('discussed_hire_temp'):
      player.c "{i}You didn't fuck her ass, did you?{/i}"
      club_president.c "{i}Not yet. Not that I wasn't tempted, but I learned my lesson on that one. I'll take it slow and make sure Gloria is comfortable before I sample everything Sam has to offer.{/i}"
      club_president.c "{i}For now I'm just enjoying her pussy. Gloria's monitoring her to make sure she's taking her birth control pills, so I'm able to enjoy her without worry.{/i}"
    else:
      club_president.c "{i}It was tempting to switch to her ass, but I'm saving that for later.{/i}"
      club_president.c "{i}For now I'm just enjoying her pussy. Gloria's monitoring her to make sure she's taking her birth control pills, so I'm able to enjoy her without worry.{/i}"
    wt_image club_pres_2
    club_president.c "I must say, you've gone above and beyond.  You want access to Gloria, anytime, it's fine with me. Have as much fun with her as you want.  I'd also like to give you something as a tip for a job well done."
    $ gloria.session = 8
    add tags 'special_reward' to club_president
    call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_30
    call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_special_reward_description_list]) from _call_for_call_labels_31
    call expandable_menu(club_president_reward_menu) from _call_expandable_menu_53
    rem tags 'special_reward' from club_president
  return

# Club - Club President: Reward
label club_president_reward_discussion:
    wt_image club_pres_2
    club_president.c "Oh hi!  There you are!  Join me for a moment in my office."
    call for_call_labels(label_list = [i + '_club_president_reward_introduction' for i in club_president_reward_reason_list]) from _call_for_call_labels_32
    rem tags 'special_reward' from club_president
    "He shows you out of his office and disappears."
    wt_image club.image
    return

label showgirl_club_president_reward_introduction:
    if player.showgirl_count > club_president.showgirl_reward_count:
        $ club_president.showgirl_reward_count += 1
        club_president.c "I understand you're responsible for sending a new Showgirl our way.  We really appreciate you looking out for ways to improve the Club."
        club_president.c "We have a policy of rewarding members who go above and beyond to improve the quality of the Club."
        call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_33
        call expandable_menu(club_president_reward_menu) from _call_expandable_menu_54
    return

label bree_maid_club_president_reward_introduction:
    if bree.club_reward_counter == 2:
        $ club_president.rewards_pending -= 1
        $ bree.club_reward_counter = 3
        club_president.c "Thanks for sending that dark-haired girl over to help keep the Club neat and tidy."
        player.c "Is she being helpful?"
        club_president.c "Not really.  She's one of the slackest maids we've ever had here."
        club_president.c "Despite that, the main complaint I get from members is that they weren't the first to spot her mistakes.  She's attracted quite the fan base, and it isn't for the high quality of her cleaning."
        club_president.c "We have a policy of rewarding members who go above and beyond to improve the quality of the Club."
        call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_34
        call expandable_menu(club_president_reward_menu) from _call_expandable_menu_55
    return

label alexis_serving_club_president_reward_introduction:
    if alexis.club_reward_counter == 2:
        $ club_president.rewards_pending -= 1
        $ alexis.club_reward_counter = 3
        club_president.c "Thanks for sending that dark-haired girl over to serve at the women's bar."
        player.c "Is she being helpful?"
        club_president.c "The other bartenders say so.  Some of our women members say she isn't as enthusiastic as they'd like, but apparently she takes a spanking rather well."
        club_president.c "We have a policy of rewarding members who go above and beyond to improve the quality of the Club."
        call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_35
        call expandable_menu(club_president_reward_menu) from _call_expandable_menu_56
    return


label rep_from_club_dalliance_club_president_reward_introduction:
    if rep_from_club.event_chain == 6:
        $ club_president.rewards_pending -= 1
        $ rep_from_club.event_chain = 9
        club_president.c "Hey, thanks for keeping quiet about the other day.  Total lack of judgment on my part, but no one needs to know about that, right?  Especially not Gloria."
        club_president.c "Let me give you a token of appreciation for your discretion, okay?"
        add tags 'special_reward' to club_president
        call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_36
        call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_special_reward_description_list]) from _call_for_call_labels_37
        call expandable_menu(club_president_reward_menu) from _call_expandable_menu_57
    return

label sarah_showgirl_club_president_reward_introduction:
    if club_president.has_tag('sarah_reward_pending'):
        $ club_president.rewards_pending -= 1
        rem tags 'sarah_reward_pending' from club_president
        if club_president.has_tag('sarah_bj_received'):
            club_president.c "Thanks for getting Sarah to blow me.  Gloria hates it when I have sex with the members, says it sets a bad precedent.  I appreciate you setting that up in a way that she couldn't say 'no'."
            club_president.c "Sarah's a great addition to the Club.  Her husband, too, I guess.  I'd like to reward you for recruiting her."
            add tags 'special_reward' to club_president
            call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_38
            call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_special_reward_description_list]) from _call_for_call_labels_39
            call expandable_menu(club_president_reward_menu) from _call_expandable_menu_58
            rem tags 'special_reward' from club_president
        else:
            club_president.c "Sarah's a great addition to the Club.  Her husband, too, I guess.  I'd like to reward you for recruiting her."
            call for_call_labels(label_list = [i + '_club_president_reward_description' for i in club_president_reward_description_list]) from _call_for_call_labels_40
            call expandable_menu(club_president_reward_menu) from _call_expandable_menu_59
    return

label love_potion_club_president_reward_description:
    club_president.c "Could I interest you in a love potion?  It'll greatly improve your relationship with just about anyone."
    return

label ring_sexuality_club_president_reward_description:
    if not club_president.has_tag('ring_sexuality_granted'):
        club_president.c "I also have a fun little ring.  It'll make your woman a lot more interested in other women.  They used to be really popular around here, until the guys discovered their partners started to spend all their time at 'girls only' events they weren't invited to.  Still, you might find a use for it."
    return

label transformation_potion_club_president_reward_description:
    if not club_president.has_tag('transformation_potion_granted'):
        club_president.c "Under the circumstances, I can also offer you something a little stronger, if you're inclined?  It's a transformation potion, and that's pretty much what it does."
    return

label club_president_reward_menu_hypnotize_him:
    "You could try that."
    "On the other hand, its possible that the Club President, or the powers behind him, have protected him from attempts at subverting his mind, and may interpret any such attempt as a hostile act."
    "The risks, and the consequences, seem high, and the potential rewards speculative.  Your self-preservation instincts tell you to take a different course.  Or maybe that's the Club defenses, working proactively?  You could get paranoid fast thinking about that."
    "Regardless, you decide to choose a different course of action."
    add tags 'tried_hypnosis' to club_president
    call expandable_menu(club_president_reward_menu) from _call_expandable_menu_60
    return

label club_president_reward_menu_his_wife:
    if gloria.session == 4:
        club_president.c "Really?  You enjoyed your last time enough that you want to see her again?"
        club_president.c "Well, since you do, maybe you could help solve a problem we're having?"
        club_president.c "I've been trying to convince her to bring in a live in servant girl.  Someone who can keep the house clean during the day, and be there for us, sexually, at night."
        club_president.c "Saves trying to find a bedmate on short notice.  My wife loves women, so that's not a one sided proposition on my part."
        club_president.c "She won't go for it, though, and I'm not sure why?  Shuts me down whenever I try to discuss it."
        club_president.c "If you can make some progress, I'll pay you your normal fees."
        player.c "Deal"
        $ gloria.session = 6
        add tags 'available_for_visit' to gloria
    else:
        club_president.c "My wife?  What do you want to do with her?"
        $ title = "What do you want?"
        menu:
            "Have sex with her":
                player.c "Have sex with her, obviously."
                club_president.c "Hmmm.  I don't normally hand out my wife as a party favor."
                club_president.c "We do have an open relationship, but normally its a quid pro quo arrangement, and we avoid Club members if possible.  I don't want to be seen as biased if some conflict comes up."
                club_president.c "Still, work's been busy and I've been leaving her alone a lot.  I'll talk to her.  If she's interested, you can have a go at her."
                club_president.c "But only for one night.  And if word gets around the Club, you'll be out.  Understood?"
                player.c "Understood"
                club_president.c "Something you should know about Gloria ... she's impressed by good taste and nice things."
                club_president.c "Don't get me wrong - she likes sex with anybody who knows what they're doing.  But if you really want to impress and get her engine revved, a little staging wouldn't hurt."
                player.c "Thanks for the advice."
                $ gloria.session = 1
            "Train her":
                player.c "Train her."
                club_president.c "Train her?  What makes you think she needs training?"
                player.c "You tell me.  How is your relationship?"
                club_president.c "Good.  Great even.  Work's been busy, and I've probably left her alone more than I should have. But the sex is great."
                club_president.c "And we have an open relationship so long as we both know about it, so we both get lots of variety, although we avoid Club members if possible.  I don't want to be seen as biased if some conflict comes up."
                player.c "So there isn't anything that's a point of contention between you?  Something that I could help solve?"
                "He hesitates a moment."
                club_president.c "Nothing big.  I've been trying to convince her to bring in a live in servant girl. Someone who can keep the house clean during the day, and be there for us, sexually, at night."
                club_president.c "Saves trying to find a bedmate on short notice.  My wife loves women, so that's not a one sided proposition on my part."
                club_president.c "She won't go for it, though, and I'm not sure why?  Shuts me down whenever I try to discuss it."
                player.c "Convince her to spend some time with me, and if I can make some progress, I want my normal fee for my services."
                club_president.c "Okay.  Deal.  If she's interested, you can have a go at her.  But if word gets around the Club, you'll be out. Understood?"
                player.c "Understood"
                club_president.c "Something you should know about Gloria ... she's impressed by good taste and nice things."
                club_president.c "Don't get me wrong - she likes sex with anybody who knows what they're doing.  But if you really want to impress and get her engine revved, a little staging wouldn't hurt."
                player.c "Thanks for the advice."
                $ gloria.session = 2
    return

label club_president_reward_menu_love_potion:
    player.c "I should be able to put the love potion to good use."
    club_president.c "Great!  Promise not to use it on a Club member, though.  We look after our own here."
    add 1 love_potion to player notify
    return

label club_president_reward_menu_ring_sexuality:
    player.c "I'll take the ring."
    club_president.c "Great!  Hopefully that'll spice up a relationship."
    $ ring_sexuality.name = "Ring of Sexuality"
    add tags 'ring_sexuality_granted' to club_president
    add 1 ring_sexuality to player notify
    return

label club_president_reward_menu_transformation_potion:
    player.c "I think this stronger potion could come in handy.  Thank you."
    club_president.c "Okay, but be careful where and who you use it on.  The Club needs to protect its reputation, and if you do anything that could be traced back to us ... well, there would be serious consequences."
    add tags 'transformation_potion_granted' to club_president
    add 1 transformation_potion to player notify
    return

label club_president_reward_menu_janice_retainer:
    player.c "Maybe you could help me out with a problem?  I've been trying to get Janice the Lawyer on retainer, but with no success.  She's one of your Club members.  Can you convince her to work with me?"
    if club_president.has_tag('special_reward'):
        club_president.c "I don't like to meddle in our members' private business affairs, but considering how you've helped me ... okay.  I'll let her know that I'd like her to take you on as a client.  I'm sure she'll do it as a favor to me."
        add tags 'lawyer_on_retainer' to player
    else:
        club_president.c "Oh, gee.  I'd like to help you out, but I don't like to meddle in our members' private business affairs."
        call expandable_menu(club_president_reward_menu) from _call_expandable_menu_61
    return

label club_president_reward_menu_money:
    player.c "I could use some extra cash."
    club_president.c "Nothing says 'you're appreciated' like an exchange of cash, hey?  I'll send you 200 right away."
    change player money by 200 notify
    return

# Examine Gloria's House
label gh_examine:
    "One of the nicer homes in the area."
    return


################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
