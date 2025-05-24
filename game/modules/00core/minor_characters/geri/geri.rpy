## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Apropos de Nada and wifetrainer

# Package Register
register geri_pregame 10 in core as 'Geri the Real Estate Agent'

# Pregame
label geri_pregame:
  python:
    ## Credits
    model_credits += [('support', 'Geri the Real Estate Agent (Elexis Monroe)')]

  ## Constants
    ## Character Definition
    # 64,0,128
    geri = Person(Character("Geri", who_color="#400080", what_color="#400080", window_background = gui.dialogue_background_dark_font_color), "geri", cut_portrait = True, prefix = "", suffix = "the Real Estate Agent", hypno_trigger_sessions_threshold = 7)

    # Other Characters
    # N/A

    ## Actions
    geri.action_contact = living_room.add_action("Contact " + geri.full_name, label = geri.short_name + "_contact", context = "_contact_other", condition = "geri.can_be_interacted and geri.g_status >= 1")
    geri.action_talk = geri.add_action("Talk to her", label = "_talk", condition = "geri.can_be_interacted")
    # geri.hypno_action.new_context = "" ## this was used to shut off the hypnosis menu, but subsequently trying an approach more consistent with hypnosis of major clients
    geri.background_hypno_action = geri.add_action("Ask about her", label = "_background_hypnosis", context = "_hypnosis", condition = "geri.g_status == 1")
    geri.trust_hypno_action = geri.add_action("Work on her trust issues", label = "_trust_hypnosis", context = "_hypnosis", condition = "geri.g_status == 2")
    geri.office_bj_hypno_action = geri.add_action("Have her blow you", label = "_office_bj_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and geri_office.is_here")
    geri.office_sex_hypno_action = geri.add_action("Have sex with her", label = "_office_sex_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and geri_office.is_here")
    geri.office_just_look_hypno_action = geri.add_action("Just look at her", label = "_office_just_look_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and geri_office.is_here")
    geri.home_bj_hypno_action = geri.add_action("Have her blow you", label = "_home_bj_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and living_room.is_here")
    geri.home_tj_hypno_action = geri.add_action("Have her give you a tit job", label = "_home_tj_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and living_room.is_here")
    geri.home_sex_hypno_action = geri.add_action("Have sex with her", label = "_home_sex_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and living_room.is_here")
    geri.home_pose_hypno_action = geri.add_action("Pose her like a doll", label = "_home_pose_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and living_room.is_here and not geri.has_tag('hypno_look_at_her_today')", backtrack = True)
    geri.home_nothing_else_hypno_action = geri.add_action("Nothing else", label = "_home_nothing_else_hypnosis", context = "_hypnosis", condition = "geri.g_status == 4 and living_room.is_here and geri.has_tag('hypno_look_at_her_today')")
    geri.nothing_hypno_action = geri.add_action("Nothing today", label = "_nothing_hypnosis", context = "_hypnosis", condition = "not geri.has_tag('hypno_look_at_her_today')")

    ## Tags
    # Common Character Tags
    geri.add_tags('likes_boys')

    ## Items
    # Standard Object Actions
    living_room.action_message_docs = living_room.add_action("New Message", label = geri.short_name + "_docs_message", context = '_check_messages', condition = "living_room.is_empty and not geri.has_tag('document_message_received')")

    # Character Specific Tags
    # N/A

    ## Locations
    # Real Estate Agent's Office
    # Note: can't enter Geri's office until after she visits, which activates elevator action
    geri_office = Location("Real Estate Office", 'go', cut_portrait = True, enter_break_labels = ['go_no_access'], enter_labels = ['go_enter'], exit_labels = ['go_exit'], area = 'offices', unseen = False)
    geri_office.connection_ot = geri_office.add_connection(office_tower) # this lets you leave her office to the office_tower lobby, in case you otherwise get stuck there
    geri.location = geri_office
    geri.fixed_location = geri_office

    ## Other
    geri.change_status("minor_character")

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('geri_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    geri.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_sex_count', 'hypno_swallow_count', 'hypno_titfuck_count')

    # Character Specific Variables
    geri.add_stats_with_value('g_status', 'spank_count', 'spank_tally_for_counting')
    #g_status key: # 0: no visit yet; 1: she visited but didn't tell backstory; 2: you know backstory; 3: solved her problem but she hasn't thanked you yet; 4: she's available to you

    ######## EXPANDABLE MENUS #######
    geri_office_talk_menu = ExpandableMenu("What do you want to talk to her about?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game
    geri.choice_office_talk_ask_out = geri_office_talk_menu.add_choice("Ask her out", "geri_office_talk_ask_out", condition = "geri.g_status == 2")
    geri.choice_office_talk_discuss_lauren = geri_office_talk_menu.add_choice("Discuss Lauren", "geri_office_talk_discuss_lauren", condition = "lauren.revenge_count >= 2 and geri.g_status == 2")
    geri.choice_office_talk_blowjob = geri_office_talk_menu.add_choice("Blow job", "geri_office_talk_blowjob", condition = "geri.g_status == 4")
    geri.choice_office_talk_sex = geri_office_talk_menu.add_choice("Sex", "geri_office_talk_sex", condition = "geri.g_status == 4")
    geri.choice_office_talk_pleasure_her = geri_office_talk_menu.add_choice("Pleasure her", "geri_office_talk_pleasure_her", condition = "geri.g_status == 4")
    geri.choice_office_talk_spank = geri_office_talk_menu.add_choice("Spank her", "geri_office_talk_spank_her", condition = "geri.g_status == 4")
    geri.choice_office_talk_nothing = geri_office_talk_menu.add_choice("Nothing", "geri_office_talk_nothing")

    geri_contact_menu = ExpandableMenu("What do you want to talk to her about?")
    # note: these don't have to be defined in pregame, can be added in game
    geri.choice_contact_ask_out = geri_contact_menu.add_choice("Ask her out", "geri_contact_ask_out", condition = "geri.g_status == 2")
    geri.choice_contact_discuss_lauren = geri_contact_menu.add_choice("Discuss Lauren", "geri_contact_discuss_lauren", condition = "lauren.revenge_count >= 2 and geri.g_status == 2")
    geri.choice_contact_visit = geri_contact_menu.add_choice("Have her visit", "geri_contact_visit_you", condition = "geri.g_status == 4")


  return

# Initial Contact Message
# OBJECT: Check Messages

label geri_docs_message:
    geri.c "{i}Hi, this is Geri, your realtor.  There are a few follow up documents related to your house purchase that you should sign.  Nothing urgent, but we should get them out of the way.{/i}"
    geri.c "{i}The paperwork is with a lawyer downtown.  You can find her in the North Office Tower.  You should drop by and sign them when you get a chance.  Hope you're enjoying your beautiful new home!"
    "Doesn't sound like there's any rush, but you should probably visit the lawyer's office at some point.  The North Office Tower sounds like an easy building to find."
    add tags 'document_message_received' to geri
    return


# Character Rejected
#label geri_rejected: #not needed
#  sys "You may no longer accept this assignment."
#  return

# Display Portrait
# CHARACTER: Display Portrait
label geri_update_media:
    if current_location == geri_office:
        $ geri.change_image('real_estate_office_portrait_1')
    elif geri.g_status == 4 and current_location == living_room:
        $ geri.change_image('real_estate_visit_15')
    else:
        $ geri.change_image('real_estate_portrait_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label geri_examine:
    "Your real estate agent, Geri."
    return

# Talk to Character
label geri_talk:
    if current_location == geri_office and geri.can_be_interacted:
        if geri.g_status == 1:
            player.c "Geri, would you like to get together after work?"
            geri.c "For personal matters or professionally?"
            $ title = "Which is it?"
            menu:
                "Personal matters":
                    $ geri.training_session()
                    player.c "Definitely personal."
                    wt_image real_estate_office_1
                    geri.c "I appreciate the offer, but I'm not in a good place right now. I caught my ex husband cheating on me with another woman. I literally caught her in our bed after she just finished fucking my husband."
                    geri.c "I'm angry at her for ruining my life, I'm angry at him for being a jerk, and I'm angry at myself for falling in love with such a jerk."
                    geri.c "I keep obsessing over the moment of walking in on them.  I'm just not in the right frame of mind to trust or open myself up to someone right now."
                    "Sounds like Geri has an issue to sort out.  You'll need a particular set of circumstances, though, to deal with her obsession."
                    $ geri.g_status = 2
                "Professionally":
                    if not player.has_tag('signed_house_docs'):
                        geri.c "You don't need to see me to finish the paperwork on your house purchase.  The documents are with a lawyer in my building, just upstairs."
                    else:
                        if player.has_tag('wealthy'):
                            geri.c "Really?  Are you interested in buying another home?  Maybe something bigger?"
                            player.c "Probably.  Not today, though."
                        else:
                            geri.c "You can't afford to own two homes, and I'd highly recommend you not try to sell your new home so quickly.  People will think there's something wrong with it."
                            player.c "That's fine.  I wasn't looking to sell, anyway."
                        "There isn't really anything to discuss with her, professionally."
        else:
            $ geri.training_session()
            call expandable_menu(geri_office_talk_menu) from _call_expandable_menu_9
        if not player.has_tag('signed_house_docs'):
            geri.c "Don't forget to sign those papers at the lawyer.  We need those to close the file on the purchase of your house."
        call forced_movement(office_tower) from _call_forced_movement_48
    elif current_location == living_room and geri.g_status == 4 and geri.can_be_interacted:
        $ geri.training_session()
        $ title = "What do you want?"
        menu menu_geri_continuing_visits_talk_options:
            "Tell her to kneel like a good sex toy" if geri.has_tag('called_her_sex_toy') and not geri.has_tag('kneeling_today') and not geri.has_tag('masturbated_today'):
                player.c "Have you forgotten that you're my sex toy?"
                wt_image real_estate_visit_1
                geri.c "No"
                player.c "Then be a good sex toy and offer yourself to me.  On your knees."
                "Geri hesitates a moment ..."
                wt_image real_estate_visit_2
                "... then sinks to the floor and begins to undress..."
                wt_image real_estate_visit_3
                if geri.has_tag('sex_toys_stay_slient'):
                    geri.c "Your sex toy ... oh ... am..."
                    player.c "No talking, sex toy."
                else:
                    geri.c "Your sex toy is ready for you."
                add tags 'kneeling_today' to geri
                $ title = "What do you want from your sex toy?"
                jump menu_geri_continuing_visits_talk_options
            "Just look at her" if geri.has_tag('kneeling_today') and not geri.has_tag('masturbated_today'):
                player.c "That's a good sex toy. Just kneel there for me."
                if geri.has_tag('sex_toys_stay_slient'):
                    "You can tell she wants to say something, but she remembers your instructions and holds her tongue."
                else:
                    add tags 'sex_toys_stay_slient' to geri
                    geri.c "Don't you want to play with your sex toy?"
                    player.c "Not today, no. I just want to look at you."
                    geri.c "But you're fully clothed, and I'm kneeling here almost naked. This is kind of humiliating. Can't we do something together?"
                    player.c "We are doing something together. You're kneeling there like a good sex toy and I'm looking at you."
                    geri.c "You're making me feel like an object."
                    player.c "Objects don't talk. Kneel there silently and nod to show me you understand."
                    geri.c "Slowly she nods."
                "You keep her there for a while, kneeling in silence."
                wt_image real_estate_visit_1
                "When you're finished looking at her, you let her stand up and dress."
                geri.c "I don't understand. Wouldn't you have rather had sex with me?"
                player.c "You wanted to have sex with me."
                geri.c "Yes, I did."
                player.c "Unfortunately for objects, they only get played with when their owner wants to play with them."
                geri.c "You're not my owner."
                player.c "Maybe not, but the next time I call you, you'll be willing come over and be my sex toy again, won't you?"
                "She nods quietly, then leaves."
            "Spank her" if geri.spank_count > 1 and not geri.has_tag('masturbated_today'):
                if geri.has_tag('kneeling_today'):
                    player.c "My sex toy needs a spanking. Remove the panties then present your ass to me."
                    wt_image real_estate_visit_18
                    if geri.has_tag('sex_toys_stay_slient'):
                        "She turns around and looks back at you."
                        player.c "How many times should my sex toy be spanked?"
                    else:
                        geri.c "Why do you keep asking me to do things I don't like?"
                        player.c "To watch you do them.  How many times do you think a sex toy should be spanked?"
                    geri.c "Ten?"
                    $ title = "How many times should she be spanked?"
                    menu:
                        "5":
                            $ geri.spank_tally_for_counting = 5
                            player.c "You haven't been that bad.  Five is enough.  Count them."
                        "10":
                            $ geri.spank_tally_for_counting = 10
                            player.c "Ten it is.  Count them."
                        "15":
                            $ geri.spank_tally_for_counting = 15
                            player.c "A sex toy can take more than that.  Let's make it fifteen.  Count them."
                        "20":
                            $ geri.spank_tally_for_counting = 20
                            player.c "A sex toy can take more than that.  Let's make it twenty.  Count them."
                    $ geri.temporary_count = 0
                    while geri.temporary_count < geri.spank_tally_for_counting:
                        $ geri.temporary_count += 1
                        "*SMACK*"
                        geri.c "Ow!  [geri.temporary_count.to_s]"
                else:
                    player.c "Thank you for coming over so promptly for your spanking."
                    wt_image real_estate_visit_1
                    geri.c "Spanking? I don't want to be spanked. Can't we ..."
                    player.c "Turn around and present your bottom to me."
                    wt_image real_estate_visit_19
                    geri.c "Wouldn't it be nicer if we did something we both enjoyed?"
                    player.c "We are doing something we both enjoy. I'll enjoy spanking you, and you'll enjoy knowing that I'm enjoying myself."
                    geri.c "That makes me sound like a wallflower. I'm a successful career woman and a really good realtor, as you know."
                    wt_image real_estate_visit_20
                    player.c "Stick out your ass, career woman. How many times should my realtor let me spank her in order to please me?"
                    geri.c "Ten?"
                    $ title = "How many times should she be spanked?"
                    menu:
                        "5":
                            $ geri.spank_tally_for_counting = 5
                            player.c "I'll be happy with five.  Count them."
                        "10":
                            $ geri.spank_tally_for_counting = 10
                            player.c "Ten it is.  Count them."
                        "15":
                            $ geri.spank_tally_for_counting = 15
                            player.c "I'd rather watch you squirm through fifteen.  Count them."
                        "20":
                            $ geri.spank_tally_for_counting = 20
                            player.c "I'd rather watch you squirm through twenty.  Count them."
                    $ geri.temporary_count = 0
                    while geri.temporary_count < geri.spank_tally_for_counting:
                        $ geri.temporary_count += 1
                        "*SMACK*"
                        geri.c "Ow!  [geri.temporary_count.to_s]"
                wt_image real_estate_visit_19
                geri.c "I can't figure out why I let you treat me in ways I'd never let any other man treat me."
                wt_image real_estate_visit_1
                player.c "The next time I feel like spanking you, you'll come straight over. No making me wait. Understood?"
                geri.c "Yes."
                $ geri.spank_count += 1
                change player energy by -energy_short notify
            "Have her masturbate for you" if not geri.has_tag('masturbated_today'):
                add tags 'masturbated_today' to geri
                if geri.has_tag('kneeling_today'):
                    if geri.has_tag('no_masturbation_last_week'):
                        player.c "Since you were a good girl and didn't touch yourself without permission, I'm going to give you permission to play with yourself now, while I watch."
                    if geri.has_tag('called_her_sex_toy'):
                        player.c "Spread your legs and play with yourself for me, sex toy."
                    else:
                        player.c "Spread your legs and play with yourself for me, Geri."
                else:
                    if geri.has_tag('no_masturbation_last_week'):
                        wt_image real_estate_visit_1
                        player.c "Since you were a good girl and didn't touch yourself without permission, I'm going to give you permission to play with yourself now, while I watch."
                    else:
                        wt_image real_estate_visit_15
                        if geri.has_tag('called_her_sex_toy'):
                            player.c "Take off your clothes."
                        else:
                            player.c "Take off your clothes, Geri."
                        wt_image real_estate_visit_31
                        geri.c "Why?  What are you hoping I'll do once I'm naked?"
                        if geri.has_tag('called_her_sex_toy'):
                            player.c "What I tell you to.  Spread your legs and play with yourself for me, sex toy."
                        else:
                            player.c "I want you to spread your legs and play with yourself for me, Geri."
                wt_image real_estate_visit_13
                "She's nervous at first, but does as you ask, hesitantly pressing her fingers against her sex."
                wt_image real_estate_visit_21
                "After a while, she gets over her shyness, and starts rubbing herself with more conviction."
                geri.c "mmmmmm"
                wt_image real_estate_visit_22
                "You can smell her arousal as she slips a finger inside and combines the clit-rubbing with finger-fucking to bring herself to a small but intense orgasm."
                geri.c "MMMMMMM"
                wt_image real_estate_visit_13
                geri.c "Can I tempt you to join in?"
                $ geri.masturbation_count += 1
                $ geri.orgasm_count += 1
                if geri.has_tag('kneeling_today') and geri.has_tag('sex_toys_stay_slient'):
                    player.c "Are you supposed to be speaking, sex toy?"
                    "She shakes her head 'no'."
                    player.c "Did you disobey me hoping that I'd punish you?"
                    geri.c "No ... shit!"
                    if dungeon.has_item(gags):
                        player.c "When I said sex toys don't get to talk, I meant it."
                        wt_image real_estate_visit_24
                        geri.c "You can't be ... mmpphhh"
                        if dungeon.has_item(floggers):
                            wt_image real_estate_visit_25
                            "If she was shocked by the ballgag, she's even more shocked when you produce a flogger. You don't flog her hard, no worse than her spankings, but her ass jumps and twitches with each blow."
                            "*thwack*  *thwack*  *thwack*  *thwack*"
                            geri.c "mmpphhh  ... mmpphhh"
                            $ geri.spank_count += 1
                        wt_image real_estate_visit_26
                        "She spends the remainder of her visit tied and gagged until you figure she's accepted as much domination as she's willing to allow."
                        wt_image real_estate_visit_16
                        geri.c "I can't believe you did that ... shit!  Am I allowed to talk yet?"
                        add tags 'gagged_before' to geri
                    else:
                        player.c "Turn around.  Ass towards me."
                        wt_image real_estate_visit_18
                        geri.c "You don't have to..."
                        player.c "You're talking again. So clearly, I do."
                        "She takes the spanking in relative silence, with the occasional grunt of displeasure."
                        "*smack*  *smack*  *smack*  *smack*"
                        geri.c "nnnn  ...  ow   ...  ow!"
                        wt_image real_estate_visit_19
                        geri.c "I think you're taking the whole punishment thing too far ... shit!  Am I allowed to talk yet??"
                    wt_image real_estate_visit_1
                    player.c "Would you like me to provide you with stricter and clearer rules of conduct?"
                    geri.c "I ... I'm not into that sort of thing."
                    player.c "I am. When you're ready to admit that you want me to train you properly, let me know."
                else:
                    $ title = "What do you want next?"
                    jump menu_geri_continuing_visits_talk_options
            "Blow job":
                $ geri.temporary_count = 1
                if geri.has_tag('masturbated_today'):
                    player.c "Kneel in front of me and open your mouth."
                elif geri.has_tag('kneeling_today'):
                    player.c "Open your mouth, sex toy."
                    if not geri.has_tag('sex_toys_stay_slient'):
                        geri.c "Why?  Is there something you want me to do for you?"
                        player.c "Put your mouth to better use than talking, sex toy."
                else:
                    wt_image real_estate_visit_15
                    player.c "Take off your clothes and come kneel in front of me, Geri."
                    wt_image real_estate_visit_31
                    geri.c "Why?  Is there something you want me to do for you?"
                    if geri.has_tag('sex_toys_stay_slient'):
                        player.c "Yes, sex toy, I want you to put your mouth to better use than talking."
                    else:
                        player.c "Yes. Open your mouth."
                wt_image real_estate_visit_37
                "As you present your cock to her, she licks it gently..."
                wt_image real_estate_visit_38
                "... then takes it into her waiting mouth.  It's a pleasurable blowjob ..."
                wt_image real_estate_visit_4
                "... and she seems to enjoy it, too, as she places a hand between her legs and rubs herself as she blows you."
                if geri.swallow_count > 0 and player.has_tag('dominant') and geri.spank_count > 0:
                    $ title = "Tell her to remove her hand?"
                    menu:
                        "Yes":
                            wt_image real_estate_visit_39
                            player.c "Stop touching yourself.  Take your hand out of there."
                            if geri.has_tag('sex_toys_stay_slient'):
                                "You can see the struggle on her face.  She wants to say something, but she knows you want her to stay silent."
                                player.c "Sex toys are used for my pleasure, not theirs.  Whatever enjoyment you get should be from serving me.  Remove your hand from between your legs and focus on pleasuring me."
                            else:
                                geri.c "What?  Why??"
                                if geri.has_tag('called_her_sex_toy'):
                                    player.c "Because sex toys are used for my pleasure, not theirs. Whatever enjoyment you get should be from serving me."
                                else:
                                    player.c "Because I want you to focus on giving me pleasure. Whatever enjoyment you get should be from serving me."
                                geri.c "Can't I enjoy both?"
                                player.c "Not today. Today is for serving, only."
                                geri.c "I could stop blowing you."
                                player.c "You could, but I don't want you to. I want you to remove your hand from between your legs and focus on pleasuring me."
                            wt_image real_estate_visit_38
                            "She does as she's told, surprising herself more than she surprises you. Your chastisement doesn't diminish the enthusiasm with which she blows you, and you're soon ready to cum."
                            $ geri.temporary_count = 0
                        "No":
                            pass
                if geri.temporary_count == 1:
                    "She doesn't seem to want to get herself off. Her body's just responding to your excitement with a tingling between her legs that her fingers help relieve."
                    wt_image real_estate_visit_38
                    "She does, however, want to get you off, and with the attention her lips, tongue, and mouth pay to your cock, she soon succeeds."
                wt_image real_estate_visit_37
                "She holds your cock in front of her face and begins stroking you with her soft hand, faster and faster and faster..."
                $ geri.temporary_count = 1
                if geri.swallow_count > 0 and player.has_tag('dominant') and geri.spank_count > 0:
                    $ title = "Have her swallow?"
                    menu:
                        "Yes":
                            $ geri.temporary_count = 0
                        "No":
                            pass
                if geri.temporary_count == 1:
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    if geri.has_tag('sex_toys_stay_slient'):
                        geri.c "Oh!  That's so hot!!  ...  Shit!  Was I allowed to talk yet?"
                        player.c "No.  Lick me clean.  In silence this time."
                    else:
                        geri.c "Oh!  That's so hot!!"
                    wt_image real_estate_visit_5
                    "As your cum drips down her chest and chin, she gives your cock a little kiss, licking the last traces of cum off of it before it goes soft."
                    wt_image real_estate_visit_31
                    if geri.has_tag('sex_toys_stay_slient'):
                        "Still uncertain as to whether she's allowed to talk yet, she remains silent as she dresses, the smile on her face telling you she'll be back the next time you call her."
                    else:
                        geri.c "Let me know the next time you want me to come over."
                    $ geri.temporary_count = 0
                    $ geri.facial_count += 1
                    add tags 'disclosed_likes_facials' to geri
                else:
                    wt_image real_estate_visit_40
                    "You pull her head forward, onto your cock.  She gulps quickly, trying to swallow the stream of jizz you shoot into the back of her throat."
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_36
                    if geri.has_tag('sex_toys_stay_slient') and not geri.has_tag('disclosed_dislikes_swallowing'):
                        player.c "You look like you want to say something, sex toy.  What is it?"
                        geri.c "That's really awkward.  It's easier and more enjoyable for me when you cum on my skin.  Especially a large load like that."
                        player.c "It's easier and more enjoyable for me to use my sex toy however I want.  It feels good to do what I want, doesn't it?  Rather than what you want or what you find easy?"
                    elif geri.has_tag('sex_toys_stay_slient'):
                        player.c "I know.  You don't enjoy swallowing.  It feels good doing what I want, rather than worrying about what you like or don't like, doesn't it?"
                    elif geri.has_tag('disclosed_dislikes_swallowing'):
                        geri.c "That's really awkward.  It's easier and more enjoyable for me when you cum on my skin.  Especially a large load like that."
                        player.c "It feels good to do what I want, doesn't it?  Rather than what you want or what you find easy?"
                    else:
                        player.c "You still don't enjoy swallowing, do you?"
                        geri.c "No"
                        player.c "It feels good doing what I want, rather than worrying about what you like or don't like, doesn't it?"
                    wt_image real_estate_visit_1
                    "She says nothing, just dresses quietly."
                    player.c "I'll let you know when I want you to visit me again."
                    "She nods, then disappears."
                    $ geri.swallow_count += 1
                    add tags 'disclosed_dislikes_swallowing' 'disclosed_likes_facials' to geri
            "Tit job":
                $ geri.temporary_count = 1
                if geri.has_tag('kneeling_today') or geri.has_tag('masturbated_today'):
                    player.c "Hold your tits together for me."
                else:
                    wt_image real_estate_visit_15
                    player.c "Take off your clothes and come kneel in front of me, Geri."
                    wt_image real_estate_visit_31
                    geri.c "Why?  Is there something you want me to do for you?"
                    player.c "Yes.  Hold your tits together."
                wt_image real_estate_visit_17
                "As your real estate agent presses her breasts together with her hands ..."
                wt_image real_estate_visit_6
                "... you insert your cock into the valley she creates and tit-cuck her."
                wt_image real_estate_visit_7
                "From time to time she can't resist giving your cock a little suck on the upstrokes."
                wt_image real_estate_visit_6
                "It's not long before you're ready to cum."
                if geri.swallow_count > 0 and player.has_tag('dominant') and geri.spank_count > 0:
                    $ title = "Tell her to swallow?"
                    menu:
                        "Yes":
                            $ geri.temporary_count = 0
                        "No":
                            pass
                if geri.temporary_count == 1:
                    $ geri.temporary_count = 0
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    geri.c "Oh!  That's so hot!!"
                    wt_image real_estate_visit_5
                    "As your cum drips down her chest and chin, she gives your cock a little kiss, licking the last traces of cum off of it before it goes soft."
                    wt_image real_estate_visit_31
                    geri.c "Let me know the next time you want me to come over."
                    if not geri.has_tag('disclosed_likes_facials'):
                        add tags 'disclosed_likes_facials' to geri
                    $ geri.facial_count += 1
                else:
                    player.c "Swallow my load."
                    wt_image real_estate_visit_7
                    "She dips her head and wraps her lips around your cock as you cum."
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_36
                    geri.c "I would've preferred to feel you on my skin."
                    if not geri.has_tag('disclosed_dislikes_swallowing'):
                        add tags 'disclosed_dislikes_swallowing' to geri
                    if not geri.has_tag('disclosed_likes_facials'):
                        add tags 'disclosed_likes_facials' to geri
                    else:
                        player.c "I know, but I like watching you drink my cum."
                    $ geri.swallow_count += 1
                $ geri.titfuck_count += 1
                orgasm notify
            "Have her ride you":
                $ geri.temporary_count = 1
                if geri.has_tag('masturbated_today'):
                    player.c "Climb up here."
                elif geri.has_tag('kneeling_today'):
                    if geri.has_tag('called_her_sex_toy'):
                        player.c "Climb up here, sex toy.  You're going to ride my cock until I cum."
                    else:
                        player.c "Climb up here.  You're going to ride my cock until I cum."
                else:
                    wt_image real_estate_visit_15
                    player.c "Take off your clothes, Geri."
                    wt_image real_estate_visit_31
                    geri.c "Why?  What are you hoping I'll do once I'm naked?"
                    player.c "Ride my hard cock."
                    geri.c "mmmmm  ...  that sounds fun!"
                wt_image real_estate_visit_10
                "You lie down and Geri climbs up on top of you. As you push the tip of your cock into her, she lets out a soft moan."
                geri.c "ohhh"
                wt_image real_estate_visit_11
                "She's already wet and you slide into her easily. Reaching up, you take one of her nipples into your mouth."
                geri.c "mmmmmm"
                wt_image real_estate_visit_41
                "Her moans get louder and she starts riding you up and down, grinding her hips into your pelvic bone on each downthrust."
                geri.c "mmmmmm ... mmmmmm"
                if geri.has_tag('sex_from_behind') and player.has_tag('dominant'):
                    $ title = "Tell her to turn around?"
                    menu:
                        "Yes, have her ride you reverse cowgirl style":
                            wt_image real_estate_visit_42
                            player.c "Turn around."
                            geri.c "But this is nicer, I can see you."
                            if geri.has_tag('called_her_sex_toy'):
                                player.c "As pretty as your face is, sex toy, it's your ass I want to see."
                                geri.c "I know you want me to be your sex toy, but I could cum like this. I'm not sure I'll be able to cum if I turn around."
                            else:
                                player.c "As pretty as your face is, it's your ass I want to see as you ride me."
                                geri.c "I'm so close. I could cum like this. I'm not sure I'll be able to cum if I turn around."
                            $ title = "Relent?"
                            menu:
                                "Let her stay facing you":
                                    wt_image real_estate_visit_43
                                    player.c "Okay, if you need to cum that badly, let's get you off."
                                    geri.c "Oh!  Thank you!!"
                                "Tell her to turn around":
                                    player.c "You'll have the satisfaction of knowing you did everything you could to make this the best you could for me. Isn't that better than cumming yourself?"
                                    $ geri.temporary_count = 0
                        "No, this is good":
                            pass
                if geri.temporary_count == 1:
                    wt_image real_estate_visit_11
                    geri.c "mmmmm  ...  I'm going to cum!"
                    wt_image real_estate_visit_12
                    "She no sooner announces it than she does it, shuddering to a climax around your cock that takes you over the edge with her."
                    geri.c "MMMMMM"
                    player.c "[player.orgasm_text]"
                    $ geri.orgasm_count += 1
                else:
                    wt_image real_estate_visit_44
                    "Geri turns around and starts riding up and down on your cock, faster and faster."
                    "As she predicted, she's not able to cum in this position, but you have a lovely view of her ass bouncing up and down as she rides your dick, and have no trouble cumming."
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_19
                    geri.c "Do you really think I should prioritize your sexual satisfaction over my own?"
                    player.c "There's more to sexual satisfaction than orgasms, Geri. The question is whether it's more fulfilling for you to have an orgasm, or to sacrifice your own pleasure in order to enhance mine."
                    if geri.has_tag('edged'):
                        add tags 'orgasm_denial_conversation' to geri
                        wt_image real_estate_visit_1
                        geri.c "I don't think I could handle never getting to cum."
                        player.c "I think you respond well to it, actually. We can talk about taking away any right to cum when you're ready for that."
                        sys "The orgasm denial thread doesn't go any further than this in the game. At least not in this version."
                $ geri.sex_count += 1
                orgasm notify
            "Doggy-style sex" if player.has_tag('dominant') and geri.spank_count > 1:
                if geri.has_tag('kneeling_today'):
                    player.c "Turn around, sex toy. I'm going to fuck you from behind."
                    wt_image real_estate_visit_18
                    if geri.has_tag('sex_toys_stay_slient'):
                        player.c "Is there something you want to say, sex toy? Go ahead. Spit it out."
                    if geri.has_tag('no_doggy_objection'):
                        if geri.has_tag('sex_toys_stay_slient'):
                            "She shakes her head."
                        else:
                            "It looks like she's going to object, but perhaps remembering your prior instructions, she doesn't object to you taking her from behind."
                        wt_image real_estate_visit_27
                        player.c "That's a good sex toy.  Stay still while I mount you."
                    else:
                        geri.c "I don't like it this way. Can't we make love with me facing you?"
                        wt_image real_estate_visit_27
                        player.c "I like it this way. And I'm not making love to you today. I'm fucking my sex toy."
                        geri.c "I'm not just a sex toy. I'm a woman. Shouldn't what I want count, too?"
                else:
                    if geri.has_tag('called_her_sex_toy'):
                        player.c "Get on your knees facing away from me and take off your clothes, sex toy. I'm going to fuck you from behind."
                    else:
                        player.c "Get on your knees facing away from me and take off your clothes, Geri. I'm going to fuck you from behind."
                    wt_image real_estate_visit_19
                    if geri.has_tag('no_doggy_objection'):
                        "It looks like she's going to object, but perhaps remembering your prior instructions, she turns around and undresses without objecting."
                        if geri.has_tag('called_her_sex_toy'):
                            wt_image real_estate_visit_18
                            player.c "That's a good sex toy."
                            wt_image real_estate_visit_27
                            player.c "Stay still while I mount you."
                            if not geri.has_tag('discussed_misogyny'):
                                "Geri's unable to hold her tongue any longer."
                                geri.c "I'm not just a sex toy. I'm a woman. You know I don't like it when I'm facing away from you. Shouldn't what I want count, too?"
                                player.c "No. What you need matters, but not what you want."
                        else:
                            wt_image real_estate_visit_18
                            player.c "It's so nice to see you prioritizing my pleasure."
                            wt_image real_estate_visit_27
                            player.c "Stay still while I mount you."
                            if not geri.has_tag('discussed_misogyny'):
                                "Geri's unable to hold her tongue any longer."
                                geri.c "You know I don't like it when I'm facing away from you. Shouldn't what I want count, too?"
                                player.c "No. What you need matters, but not what you want."
                    else:
                        geri.c "I don't like it this way. Can't we make love with me facing you?"
                        wt_image real_estate_visit_18
                        if geri.has_tag('called_her_sex_toy'):
                            player.c "I like it this way."
                            wt_image real_estate_visit_27
                            player.c "And I'm not making love to you today. I'm fucking my sex toy."
                            geri.c "I'm not just a sex toy. I'm a woman. Shouldn't what I want count, too?"
                        else:
                            player.c "I like it this way."
                            wt_image real_estate_visit_27
                            geri.c "But shouldn't what I want count just as much?"
                        player.c "No. What you need matters, but not what you want."
                if not geri.has_tag('discussed_misogyny'):
                    add tags 'discussed_misogyny' to geri
                    wt_image real_estate_visit_8
                    geri.c "That's misogynistic!"
                    player.c "No it's not. It's got nothing to do with you being a woman. It's because I'm sexually dominant and you're submissive to me."
                    wt_image real_estate_visit_29
                    if geri.has_tag('called_her_sex_toy'):
                        geri.c "I'm not submissive! Just because I let you have your fun calling me a 'sex toy' doesn't mean that's what I am."
                        player.c "You are submissive when you're with me. And don't say it like it's a bad thing. I think it's a wonderful thing."
                    else:
                        geri.c "I'm not submissive!"
                        player.c "You are when you're with me. And don't say it like it's a bad thing. I think it's a wonderful thing."
                    geri.c "But ..."
                    player.c "Stop talking, put your head down, and let me enjoy looking at your ass while I finish fucking you."
                else:
                    wt_image real_estate_visit_8
                    "She holds her tongue as you begin to fuc her, but you can tell she's tense."
                    player.c "Put your head down, and let me enjoy looking at your ass while I fuck you. I enjoy taking you this way and I know you want me to enjoy myself."
                wt_image real_estate_visit_9
                "Geri puts her head down and stays quiet and lets you enjoy the rest of your fuck. She's too busy thinking to properly enjoy the sex herself, so you focus on your orgasm and don't worry about hers."
                player.c "[player.orgasm_text]"
                wt_image real_estate_visit_16
                geri.c "I do enjoy having sex with you. I even enjoy playing your games sometimes. I just wish it was more of an equal partnership."
                player.c "Just because I'm the dominant doesn't make you an unequal partner. If you say 'no' I'll respect that. But I'm going to be honest with you and tell you what I want out of our relationship."
                wt_image real_estate_visit_1
                player.c "I'd like you to be honest with me and yourself, and admit that part of the reason you're here is you enjoy the experience of doing things simply because I want you to do them for me."
                player.c "If you can't do that, at least do this. Tell me you'll visit me again the next time I call you."
                geri.c "Yes.  I will."
                add tags 'sex_from_behind' to geri
                $ geri.sex_count += 1
                orgasm notify
            "Pleasure her":
                $ geri.temporary_count = 1
                if geri.has_tag('masturbated_today'):
                    wt_image real_estate_visit_23
                    player.c "Let's see which is better. The orgasm you gave yourself, or the one I give you. Lie back."
                elif geri.has_tag('kneeling_today'):
                    wt_image real_estate_visit_3
                    if geri.has_tag('called_her_sex_toy'):
                        player.c "Take your panties off and lie back. I want to taste my sex toy."
                    else:
                        player.c "Take your panties off and lie back. I want to taste you."
                else:
                    wt_image real_estate_visit_15
                    player.c "Take off your clothes and come lie down in front of me, Geri."
                    wt_image real_estate_visit_31
                    geri.c "Oh?  Why??"
                    player.c "So I can taste you."
                wt_image real_estate_visit_30
                "She moans as your tongue touches her already wet sex."
                geri.c "ohhh ... mmmmmm"
                wt_image real_estate_visit_32
                "You nibble and tease her until her clit is standing up at attention."
                geri.c "mmmmmm"
                wt_image real_estate_visit_33
                if geri.has_tag('kneeling_today') and geri.has_tag('called_her_sex_toy'):
                    "She places her hand on the back of your head, trying to direct you to her needy clit."
                    player.c "Hands down, sex toy. I'll decide if or when I let you cum."
                    wt_image real_estate_visit_32
                    "She removes her hand and lies back as you continue to tease her, squeezing her breast to try and distract herself from her throbbing clit."
                    geri.c "mmmmmm"
                    $ title = "Let her cum?"
                    menu:
                        "Yes":
                            $ geri.temporary_count = 2
                        "No":
                            $ geri.temporary_count = 0
                else:
                    "She places her hand on the back of your head, trying to direct you to her needy clit. You resist for a moment, teasing her as she groans in pleasure and frustration ..."
                    geri.c "mmmmmm"
                if geri.temporary_count > 0:
                    wt_image real_estate_visit_34
                    if geri.temporary_count == 2:
                        "Eventually you relent and let her clit have the attention it's seeking.  With a few hard flicks of your tongue across her engorged nub, you bring her over the edge."
                    else:
                        "... then you flick your tongue across her engorged nub, taking her over the edge."
                    geri.c "MMMMMMM"
                    "You clamp your mouth over her sex and swallow the flood of juices that accompany her orgasm."
                    if geri.has_tag('masturbated_today'):
                        wt_image real_estate_visit_31
                        geri.c "That wasn't even close. It felt so much better having you touch me than touching myself."
                    elif geri.has_tag('kneeling_today') and geri.has_tag('called_her_sex_toy'):
                        wt_image real_estate_visit_23
                        player.c "Show me your clit, sex toy.  How does it feel?"
                        geri.c "A little sensitive. No, a lot sensitive. But amazing."
                        player.c "Is there something you want to say to me?"
                        geri.c "Thank you."
                        player.c "Thank you for what?"
                        geri.c "For the orgasm."
                        player.c "Isn't there something else you're thankful for?"
                        geri.c "You mean ... do you want me to thank you for being your sex toy?"
                        player.c "Are you happy you came over here and served as my sex toy?"
                        "She hesitates for a moment, then nods."
                        player.c "Then why not say it?"
                        geri.c "I ... I enjoyed being your sex toy. Thank you."
                    else:
                        wt_image real_estate_visit_31
                        geri.c "That was amazing! Thank you!!"
                    $ geri.temporary_count = 0
                    $ geri.orgasm_count += 1
                else:
                    "You edge her for as long as you think she can take ..."
                    geri.c "mmmmm"
                    wt_image real_estate_visit_21
                    "... then you remove your mouth."
                    player.c "That's enough stimulation for my sex toy for today."
                    geri.c "But???  I'm so close!"
                    player.c "I told you I wanted to taste my sex toy. I didn't say anything about watching you cum."
                    geri.c "That's mean!"
                    player.c "Why?  Didn't you enjoy my attention?"
                    geri.c "Yes!  A lot!!  I wanted to cum."
                    player.c "And I didn't want you to cum. But I was okay with you enjoying yourself for a little while. Show me your clit, toy."
                    wt_image real_estate_visit_23
                    player.c "How does your clit feel, now that you're back away from the edge?"
                    geri.c "Sensitive"
                    player.c "And how do you feel?"
                    geri.c "I'm not sure."
                    player.c "You have the rest of the day to figure it out. No playing with yourself until the next time I see you."
                    geri.c "What?  Why??"
                    player.c "Because I want you to remember this feeling for as long as possible. Promise me you won't touch yourself, regardless of how horny you feel later."
                    geri.c "I ... I promise."
                    add tags 'no_masturbation_this_week' 'edged' to geri
                $ geri.pleasure_her_count += 1
                change player energy by -energy_short notify
            "Nothing more today":
                if geri.has_tag('masturbated_today'):
                    player.c "Not today. I just wanted to watch you cum."
                    wt_image real_estate_visit_15
                    geri.c "I hope I put on a good show for you. Let me know when you want to see me again."
                elif geri.has_tag('kneeling_today'):
                    player.c "You can go now."
                    wt_image real_estate_visit_3
                    if geri.has_tag('sex_toys_stay_slient'):
                        "She looks at you quizzically."
                        player.c "You're dismissed, sex toy, so you have permission to speak again."
                        geri.c "We didn't do anything."
                    else:
                        geri.c "But we haven't done anything."
                    player.c "You knelt at my feet."
                    geri.c "You called me all the way over here just to have me kneel in front of you for a minute, now you're sending me away?"
                    player.c "Yes. I wanted to see you obey me, and you did. You can dress and go now."
                    wt_image real_estate_visit_2
                    geri.c "That seems like a lot of time on my part just for you to watch me kneel when you asked me to."
                    player.c "You got an experience you enjoyed, too. One that you'll think about for the rest of the day."
                    geri.c "I don't enjoy kneeling for you. I just did it when you asked because I know you like that."
                    player.c "It's okay to admit you like being on the floor in front of me, even if you don't understand why."
                    player.c "Stop. You could have stood up long ago. I'm glad you like being down there, but it would be even nicer if you accepted that you like it, too."
                    wt_image real_estate_visit_1
                    geri.c "I'm standing now."
                    player.c "Good. I wouldn't want you to try crawling all the way home. I might have you crawl for me around here, though, someday."
                    "She's not ready for that, but she'll be thinking about the idea for quite a while."
                else:
                    player.c "I didn't want anything in particular today, Geri. I just wanted to see your smiling face in person."
                    wt_image real_estate_visit_15
                    geri.c "That's sweet! It was a bit of a drive, but I'm glad to get to see you, too! I guess I should get going now. I have a house showing this evening."
        call character_location_return(geri) from _call_character_location_return_227
        wt_image current_location.image
    else:
        "You have nothing to say to her right now."
    return

label geri_office_talk_ask_out:
    player.c "Hi Geri, I just wanted to check in to see if you've changed your mind about getting together with me."
    wt_image real_estate_office_1
    geri.c "It's sweet of you to ask, but no. I'm still in full on obsession mode about that cheating bitch I found in our bed. I'm just not ready to start seeing anyone."
    player.c "That's too bad.  If you change your mind, let me know."
    "You let her get back to her work."
    return

label geri_office_talk_discuss_lauren:
    if not geri.has_tag('discussed_cheater'):
        add tags 'discussed_cheater' to geri
        player.c "Geri, I just wanted to let you know I may have a solution to your problem."
        wt_image real_estate_office_1
        geri.c "My problem?"
        player.c "The issue you've been obsessing over.  I'll be in touch soon."
    else:
        player.c "I haven't forgotten about the solution to your problem. I'll give you a call when it's all set up."
        wt_image real_estate_office_1
        geri.c "What are you up to?"
        player.c "You'll see."
    "You can set up a meeting between Lauren and Geri on a future session with Lauren."
    return

label geri_office_talk_blowjob:
    wt_image real_estate_office_4
    player.c "Time to make it up to me for making me wait, Geri."
    wt_image real_estate_office_5
    "She takes your cock out of your pants ..."
    wt_image real_estate_office_25
    "... then uses her hand, lips, and tongue to pleasure your dick."
    wt_image real_estate_office_26
    if player.has_tag('dominant') and geri.spank_count > 1:
        geri.c "I don't like to swallow. Give me a minute and I'll undress."
        $ title = "Let her undress?"
        menu:
            "No, tell her to swallow":
                player.c "You'll swallow for me."
                wt_image real_estate_office_5
                geri.c "Oh ... okay, I guess I can."
                wt_image real_estate_office_29
                "She puts her mouth back on your dick and strokes your cock faster and faster until you fill her waiting mouth."
                player.c "[player.orgasm_text]"
                geri.c "Oh!"
                wt_image real_estate_office_1
                geri.c "Do you get off on telling other women to do things they don't really enjoy, or is it just me?"
                player.c "Does my cum taste that bad to you?"
                wt_image real_estate_office_12
                geri.c "No, but I don't really like the sensation. I find it hot when your cum lands on my skin, though."
                player.c "Still, you'll swallow my cum the next time I tell you to."
                wt_image real_estate_office_11
                geri.c "Yes"
                $ geri.swallow_count += 1
            "Yes, let her get naked":
                wt_image real_estate_office_27
                "Geri strips, then lies down on her desk and resumes the blow job."
                wt_image real_estate_office_28
                "She strokes your cock faster and faster as she licks the underside of your cock head ..."
                wt_image real_estate_office_8
                "... until your balls release their load. She laughs as your hot jizz spurts on her waiting face."
                player.c "[player.orgasm_text]"
                geri.c "Oh!  I love that feeling!!"
                wt_image real_estate_office_19
                geri.c "Feel free to drop by and see me again anytime."
                $ geri.facial_count += 1
    else:
        geri.c "Give me a minute."
        wt_image real_estate_office_27
        "Geri strips, then lies down on her desk and resumes the blow job."
        wt_image real_estate_office_28
        geri.c "I don't like swallowing, but I think you'll enjoy this."
        "She strokes your cock faster and faster as she licks the underside of your cock head ..."
        wt_image real_estate_office_8
        "... until your balls release their load. She laughs as your hot jizz spurts on her waiting face."
        player.c "[player.orgasm_text]"
        geri.c "Oh!  I love that feeling!!"
        wt_image real_estate_office_19
        geri.c "Feel free to drop by and see me again anytime."
        $ geri.facial_count += 1
    if not geri.has_tag('disclosed_dislikes_swallowing'):
        add tags 'disclosed_dislikes_swallowing' to geri
    if not geri.has_tag('disclosed_likes_facials'):
        add tags 'disclosed_likes_facials' to geri
    $ geri.blowjob_count += 1
    orgasm notify
    return

label geri_office_talk_sex:
    wt_image real_estate_office_4
    player.c "Why don't you make yourself more comfortable?"
    wt_image real_estate_office_30
    geri.c "More comfortable as in less clothing on?"
    wt_image real_estate_office_20
    player.c "Less clothing on and lie down."
    wt_image real_estate_office_31
    "As she lays down on her desk you press yourself against her opening. She's wet, and the head of your cock slips inside easily."
    geri.c "Oh!"
    $ title = "Fuck her like this?"
    menu:
        "Yes, fuck her missionary style":
            wt_image real_estate_office_32
            "You thrust into her, faster and faster as her moans grow louder and louder."
            geri.c "mmmmm  ...  mmmmmmm"
            wt_image real_estate_office_33
            "Suddenly she spasms, bucking up against your cock as she cums."
            geri.c "MMMMMMM  ...  Cum on me!  Cum on me!"
            $ title = "Cum on her?"
            menu:
                "Yes, pull out":
                    wt_image real_estate_office_8
                    "As you pull out, she turns and jerks you off onto her face."
                    player.c "[player.orgasm_text]"
                    geri.c "Oh!  I love that feeling!!"
                    wt_image real_estate_office_19
                    geri.c "Feel free to drop by and see me again anytime."
                    if not geri.has_tag('disclosed_likes_facials'):
                        add tags 'disclosed_likes_facials' to geri
                    $ geri.facial_count += 1
                "No, creampie her":
                    wt_image real_estate_office_34
                    "You thrust into her, burying your shaft to the hilt as your balls unload into her."
                    player.c "[player.orgasm_text]"
                    geri.c "Oh!"
                    wt_image real_estate_office_19
                    geri.c "I guess you were too close, huh? It's okay. I'm on birth control. I just like the feeling of your cum hitting my skin."
                    if not geri.has_tag('disclosed_likes_facials'):
                        add tags 'disclosed_likes_facials' to geri
                    wt_image real_estate_office_10
                    geri.c "Feel free to drop by and see me again anytime."
            $ geri.orgasm_count += 1
        "No, flip her over":
            wt_image real_estate_office_35
            "Grasping her by the ankle, you start to turn her over."
            if not geri.has_tag('no_doggy_objection'):
                geri.c "Wait!  No!  I want to be looking at you."
            if player.has_tag('dominant') and geri.spank_count > 1:
                if not geri.has_tag('no_doggy_objection'):
                    wt_image real_estate_office_36
                    player.c "And I want to look at your ass as I fuck you."
                    wt_image real_estate_office_6
                    geri.c "It feels so impersonal this way."
                    player.c "Like I'm fucking you instead of making love to you?"
                    geri.c "Yes! It's like I'm just serving you."
                    player.c "Good idea. Reach back and spread your ass cheeks."
                    geri.c "What?  Why??"
                    player.c "In order to serve me. I said I wanted to look at your ass while I fuck you. Give me a good show."
                else:
                    wt_image real_estate_office_6
                    "This time, she offers no resistance as you take her from behind."
                    player.c "I want to look at your ass while I fuck you. Give me a good show."
                wt_image real_estate_office_7
                geri.c "Wouldn't it be nicer if we did something we both enjoyed?"
                player.c "Your wet cunt tells me you're enjoying this just fine."
                geri.c "I'd enjoy it more if I were facing you."
                "Maybe, but as you pick up the pace, thrusting into her faster and faster, she begins to moan louder and louder."
                geri.c "mmmmm  ...  mmmmmmm"
                $ title = "Let her cum?"
                menu:
                    "Yes, keep fucking her":
                        wt_image real_estate_office_38
                        "A few more strokes take her over the edge, and you with her."
                        geri.c "MMMMMMM"
                        player.c "[player.orgasm_text]"
                        wt_image real_estate_office_37
                        player.c "You seem to enjoy serving me."
                        geri.c "What?  No!"
                        wt_image real_estate_office_12
                        player.c "You came pretty hard for a woman who wasn't enjoying being of service to me."
                        geri.c "Maybe I was just horny? Besides, you know I enjoy making love with you."
                        player.c "I wasn't making love to you. I was fucking you like a sex toy.{nw}"
                        if geri.has_tag('called_her_sex_toy'):
                            extend " That's what you are. My sex toy, right?"
                            wt_image real_estate_office_11
                            geri.c "Yes"
                        else:
                            extend " "
                            wt_image real_estate_office_11
                            geri.c "Are you trying to make me feel bad?"
                            player.c "No. I just want you to accept that in this relationship, your role is to be my sex toy. And you'll be my sex toy whenever and however I ask. Understood?"
                            geri.c "Yes"
                            add tags "called_her_sex_toy" to geri
                        $ geri.orgasm_count += 1
                    "No, pull out":
                        wt_image real_estate_office_28
                        "You pull out and move around the desk, positioning your cock at her face."
                        player.c "Finish me off."
                        geri.c "What?  I was so close."
                        player.c "Finish me off."
                        wt_image real_estate_office_8
                        "She strokes your cock until you empty your load on her face."
                        player.c "[player.orgasm_text]"
                        geri.c "Oh!"
                        wt_image real_estate_office_37
                        geri.c "We could have both enjoyed that, you know."
                        if geri.has_tag('disclosed_likes_facials'):
                            player.c "I thought you liked it when I cum on your face."
                            wt_image real_estate_office_12
                            geri.c "I do, but you could have waited for me to cum first."
                        else:
                            wt_image real_estate_office_12
                        player.c "You wouldn't have felt so much like you were serving if you got to cum."
                        if not geri.has_tag('no_doggy_objection'):
                            geri.c "What makes you think I want to be serving you?"
                            player.c "I don't know if you do. But the next time I tell you to turn around while I fuck you from behind, you'll obey. Understood?"
                            wt_image real_estate_office_11
                            geri.c "Yes"
                            add tags 'no_doggy_objection' to geri
                        else:
                            wt_image real_estate_office_11
                            geri.c "Do you really think I should enjoy serving you more than I enjoy cumming?"
                            player.c "I don't know, but the next time I want to fuck you, you'll spread your legs for me, regardless of whether you get to cum or not.  Understood?"
                            geri.c "Yes"
                        $ geri.facial_count += 1
                add tags 'sex_from_behind' to geri
            else:
                wt_image real_estate_office_31
                geri.c "This feels so much better for me."
                wt_image real_estate_office_32
                "It feels pretty good to you, too. You thrust into her, faster and faster as her moans grow louder and louder."
                geri.c "mmmmm  ...  mmmmmmm"
                wt_image real_estate_office_33
                "Suddenly she spasms, bucking up against your cock as she cums."
                geri.c "MMMMMMM  ...  Cum on me!  Cum on me!"
                $ title = "Cum on her?"
                menu:
                    "Yes, pull out":
                        wt_image real_estate_office_8
                        "As you pull out, she turns and jerks you off onto her face."
                        player.c "[player.orgasm_text]"
                        geri.c "Oh!  I love that feeling!!"
                        wt_image real_estate_office_19
                        geri.c "Feel free to drop by and see me again anytime."
                        if not geri.has_tag('disclosed_likes_facials'):
                            add tags 'disclosed_likes_facials' to geri
                        $ geri.facial_count += 1
                    "No, creampie her":
                        wt_image real_estate_office_34
                        "You thrust into her, burying your shaft to the hilt as your balls unload into her."
                        player.c "[player.orgasm_text]"
                        geri.c "Oh!"
                        wt_image real_estate_office_19
                        geri.c "I guess you were too close, huh? It's okay. I'm on birth control. I just like the feeling of your cum hitting my skin."
                        if not geri.has_tag('disclosed_likes_facials'):
                            add tags 'disclosed_likes_facials' to geri
                        wt_image real_estate_office_10
                        geri.c "Feel free to drop by and see me again anytime."
                $ geri.orgasm_count += 1
    $ geri.sex_count += 1
    orgasm notify
    return

label geri_office_talk_pleasure_her:
    player.c "I think today I'm going to thank you. Take your clothes off."
    wt_image real_estate_office_19
    geri.c "Thank me?  For what?"
    wt_image real_estate_office_20
    player.c "For helping me find such a great house for one thing."
    wt_image real_estate_office_21
    player.c "For having such a sexy pussy, for another."
    wt_image real_estate_office_22
    geri.c "You like my pussy?"
    player.c "Lie back on your desk and I'll show you how much."
    wt_image real_estate_office_23
    "You're not in a rush, so you can take some time to use your finger ..."
    geri.c "mmmmmm"
    wt_image real_estate_office_24
    "... and your mouth to show your Realtor how much you appreciate her and her pussy."
    geri.c "mmmmmm ... MMMMMMM"
    wt_image real_estate_office_19
    geri.c "I presume this goes without saying, but feel free to drop by and see me anytime!"
    $ geri.orgasm_count += 1
    change player energy by -energy_short
    return

label geri_office_talk_spank_her:
    if geri.spank_count == 0:
        player.c "You know, you did keep me waiting a long time."
        wt_image real_estate_office_portrait_1
        geri.c "I know. But I'm prepared to make that up to you now."
        player.c "Good. Ten hard swats on your ass should be a suitable punishment."
        wt_image real_estate_office_11
        geri.c "What?"
        player.c "You heard me. Get up on your desk. I'm going to spank you for making me wait."
        geri.c "I've never been spanked."
        player.c "Not even as a child?"
        geri.c "Definitely not. My parents were hippies. They didn't believe in corporal punishment."
        player.c "Considering what you did to Lauren, I'd guess you're not of the same belief. You showed you can dish it out. Let's see if you can take it. Up on the desk."
        wt_image real_estate_office_13
        geri.c "Surely there's something else you'd rather do with me while I'm up here?"
        player.c "Turn around and present your bum to me. You're not going to sweet talk your way out of your punishment."
        wt_image real_estate_office_14
        "As she presents her rear, you pull up her skirt and land the fist spank ... *smack*"
        geri.c "Ow!"
        "*smack*"
        geri.c "Ow!"
        "*smack*"
        geri.c "Ow ... do you really enjoy this?"
        wt_image real_estate_office_15
        player.c "I do, but now that you mention it, I'll enjoy it more on your bare ass."
        "*smack*"
        geri.c "Ow!"
        "*smack*"
        wt_image real_estate_office_16
        geri.c "OW!  That really hurts!"
        player.c "It's supposed to. Put your hand down."
        wt_image real_estate_office_15
        "*smack*"
        geri.c "Ow!"
        "*smack*"
        wt_image real_estate_office_16
        geri.c "OW!  I think that's enough."
        player.c "No. That's seven. I said ten. If you reach your back again, I'll add more."
        wt_image real_estate_office_15
        "*smack*"
        geri.c "Ow!"
        player.c "How many was that?"
        geri.c "Eight"
        player.c "Good. Count the rest of them."
        "*smack*"
        geri.c "Ow!  Nine."
        "*SMACK*"
        wt_image real_estate_office_16
        geri.c "OW!!  That was harder."
        "*SMACK*"
        geri.c "HEY!!  You said only ten."
        player.c "Have you counted to ten yet?"
        "*SMACK*"
        geri.c "TEN"
        "*SMACK*"
        geri.c "HEY!! I counted!"
        player.c "You also reached your hand back without permission."
        wt_image real_estate_office_15
        geri.c "You really are getting off on this, aren't you?"
        "*SMACK*"
        geri.c "OW!! TEN! That was ten."
        player.c "Okay. You can get up now."
        wt_image real_estate_office_17
        geri.c "Wow. That really does sting. I might have gone easier on Lauren if I'd known."
        player.c "Would you have?"
        wt_image real_estate_office_10
        geri.c "No. You're right. I wouldn't have. I need to get back to work now. Assuming I can concentrate with a sore bum."
        $ geri.spank_count = 1
        change player energy by -energy_short notify
    elif geri.spank_count > 0:
        player.c "Time for another spanking."
        geri.c "I don't really enjoy that.{nw}"
        if player.has_tag('dominant'):
            extend " "
            player.c "I do. Be a good girl and get back in position for me."
            wt_image real_estate_office_11
            geri.c "Do you convince many women to let you do this with them?"
            player.c "Quit stalling."
            wt_image real_estate_office_18
            geri.c "It's just, I don't let other guys do this to me."
            player.c "I'm not other guys. How many spanks do you think you deserve?"
            wt_image real_estate_office_14
            geri.c "Five?"
            $ title = "How many does she deserve?"
            menu:
                "5":
                    $ geri.spank_tally_for_counting = 5
                    player.c "Okay. Five it is. On your bare bottom. Count them."
                "10":
                    $ geri.spank_tally_for_counting = 10
                    player.c "More than that. Ten, I think. On your bare bottom. Count them."
                "15":
                    $ geri.spank_tally_for_counting = 15
                    player.c "More than that. Fifteen, I think. On your bare bottom. Count them."
                "20":
                    $ geri.spank_tally_for_counting = 20
                    player.c "More than that. Twenty, I think. On your bare bottom. Count them."
            wt_image real_estate_office_15
            $ geri.temporary_count = 0
            while geri.temporary_count < geri.spank_tally_for_counting:
                $ geri.temporary_count += 1
                "*SMACK*"
                geri.c "Ow!  [geri.temporary_count.to_s]"
            wt_image real_estate_office_16
            geri.c "You don't have to spank me so hard, you know."
            wt_image real_estate_office_17
            geri.c "Now my bum's going to be sore the rest of the day.  I hope that was worth it to you?"
            player.c "You having a sore bottom after is part of what I enjoy."
            wt_image real_estate_office_10
            geri.c "I don't understand why I let you do that to me."
            player.c "The important thing is you'll let me do it again the next time I'm in the mood."
            geri.c "I guess so. Yes."
            $ geri.spank_count += 1
            change player energy by -energy_short notify
    else:
        extend "  How about we do something else instead?"
        call geri_talk from _call_geri_talk
    return

label geri_office_talk_nothing:
    if geri.g_status == 4:
        player.c "I just stopped by to see how you are?"
        wt_image real_estate_office_portrait_1
        geri.c "I'm great, thank you!  It's good to be focused on the here and now again, instead of being stuck in the past. I've been making up for lost time. I forgot how much fun a single girl can have!"
    return

# Hypno Actions
label geri_hypnosis_start:
    # the _hypnosis_start label runs when the Hypnotize Her action is selected
    if geri_office.is_here:
        $ geri.training_session()
        wt_image real_estate_office_10
        player.c "Geri, would you please look at this for me?"
        call focus_image from _call_focus_image_25
        player.c "Listen to me, Geri. Listen to me. Listen to my voice and nothing else, Geri. Only my voice. Only my voice now."
        wt_image real_estate_office_11
        "She soon falls under your trance."
        player.c "You and I are going to chat, Geri. I want you to be comfortable for our chat. I want to enjoy our chat. Show me your breasts, Geri, so that you can be comfortable and I can enjoy our chat."
        wt_image real_estate_office_2
        if not player.has_tag('first_hypno_breasts_message'):
            add tags 'first_hypno_breasts_message' to player
            "[player.first_hypno_breasts_message_text]"
    elif current_location == living_room and geri.g_status == 4:
        $ geri.training_session()
        wt_image real_estate_visit_1
        player.c "Geri, would you please look at this for me?"
        call focus_image from _call_focus_image_26
        player.c "Listen to me, Geri. Listen to me. Listen to my voice and nothing else, Geri. Only my voice. Only my voice now."
        wt_image real_estate_visit_16
        "She soon falls under your trance."
        player.c "You and I are going to chat, Geri. I want you to be comfortable for our chat. I want to enjoy our chat. Show me your breasts, Geri, so that you can be comfortable and I can enjoy our chat."
        wt_image real_estate_visit_17
        "She proudly holds up her breasts for your inspection. It seems she came here expecting to show off her body to you. You probably didn't need to hypnotize her to get her to have sex with you, but it's fun to do so anyway."
    else:
        "Not here."
        # this command breaks the hypnosis routine
        $ ignore_context_change = True
    ## if not broken, system now goes on to the hypnotist context menu options
    return

label geri_background_hypnosis:
    if geri_office.is_here:
        player.c "Tell me about yourself, Geri."
        geri.c "I'm alone. I had a man, but he cheated on me. I caught him in bed with another woman. I hate her. I want to punish her for ruining my life. I hate him, too, for being such a jerk. I hate myself for letting myself fall for such a jerk. "
        geri.c "I don't trust men, and I'm too scared of being hurt to let myself get close to another one. I'm too angry, at her, at him, to even try trusting someone new."
        "Wow. It seems Geri's been spending a lot of time psycho analyzing herself. That just flowed out of her like water."
        "The anger is too tough a barrier to get at. You try working on her trust in you, in case that comes in handy down the road, then you have her cover herself up and bring her out of her trance."
        wt_image real_estate_office_portrait_1
        geri.c "Gee, thanks for the chat!  You seem like a really trustworthy guy."
        "You let her get back to her work."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_2
    return

label geri_trust_hypnosis:
    if geri_office.is_here:
        "You try working on Geri's anger and lack of trust. You trace her issues back to the moment she walked in on another woman in her bed, and her regrets about what she did and didn't do at that moment."
        "Despite your best efforts, you're unable to make any further progress with hypnosis. You have her cover herself up and bring her out of her trance."
        wt_image real_estate_office_portrait_1
        geri.c "Thanks for dropping by. You know, I think if I was in a position to trust anyone, it would be you. I'm sorry I'm just not in that position right now."
        player.c "That's too bad.  If you change your mind, let me know."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_3
    return

label geri_office_bj_hypnosis:
    if geri_office.is_here:
        player.c "You want to please me, Geri.  Get on your knees and open your mouth to please me."
        wt_image real_estate_office_39
        player.c "You're going to suck my cock and swallow my cum, Geri. You will do this to make it up to me for making me wait to see you."
        geri.c "Yes. I will suck your cock and swallow your cum. I want to make it up to you for making you wait to see me."
        wt_image real_estate_office_25
        "She'd have sucked your cock even without hypnotizing her."
        wt_image real_estate_office_29
        if geri.has_tag('disclosed_dislikes_swallowing'):
            "Getting her to swallow your jizz might have been more difficult."
        else:
            "But this way is fun, too."
        player.c "[player.orgasm_text]"
        $ geri.hypno_blowjob_count += 1
        $ geri.hypno_swallow_count += 1
        orgasm
        wt_image real_estate_office_19
        "You have her cover herself up and bring her out of her trance."
        wt_image real_estate_office_portrait_1
        geri.c "Thanks for dropping by to chat!  Feel free to come by anytime."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_4
    return

label geri_office_sex_hypnosis:
    if geri_office.is_here:
        player.c "Show me your pussy, Geri. You want me to fuck your pussy."
        wt_image real_estate_office_40
        geri.c "Yes. I want you to fuck my pussy."
        player.c "Remove your clothes and present your rear to me."
        wt_image real_estate_office_41
        "She assumes you mean doggy-style, so she drops to her knees ..."
        wt_image real_estate_office_6
        "... but it's a more comfortable angle for you when she's bent over the desk."
        player.c "You want to please me, Geri. Please me while I fuck you by holding your ass cheeks open for me."
        wt_image real_estate_office_7
        "She would have fucked you even if she wasn't hypnotized, but possibly not like this."
        wt_image real_estate_office_38
        player.c "[player.orgasm_text]"
        geri.c "Oh!  Did I please you?  Did I please you while you were fucking my pussy?"
        player.c "Yes, Geri. You're a very pleasing fuck."
        $ geri.hypno_sex_count += 1
        orgasm
        wt_image real_estate_office_19
        "You have her cover herself up and bring her out of her trance."
        wt_image real_estate_office_portrait_1
        geri.c "Thanks for dropping by to chat!  Feel free to come by anytime."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_5
    return

label geri_office_just_look_hypnosis:
    if geri_office.is_here:
        player.c "You want to please me, Geri. Show me your body, Geri, to please me."
        wt_image real_estate_office_40
        "If you'd wanted to fuck her, you could have done that without hypnotizing her. For today, it's more fun just to have her sit like a mindless manikin."
        "You contemplate leaving her like this for her next home buyer or seller to find her, but she hasn't done anything to deserve that, and as far as you know no one's done anything to deserve her, either."
        wt_image real_estate_office_19
        "When you've looked at her long enough, you have her cover herself up and bring her out of her trance."
        wt_image real_estate_office_portrait_1
        geri.c "Thanks for dropping by to chat!  Feel free to come by anytime."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_6
    return

label geri_home_bj_hypnosis:
    if living_room.is_here:
        if geri.has_tag('hypno_look_at_her_today'):
            wt_image real_estate_visit_17
            "Your mindless sex doll has sexy lips, the sort that would feel good around your cock."
            player.c "Kneel in front of me and suck my cock, sex doll."
            wt_image real_estate_visit_36
            "She presses her soft lips against your cock ..."
            wt_image real_estate_visit_40
            "... then opens her mouth and takes you inside."
            "It's an enthusiastic and single-minded blow job that soon has you ready to cum."
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    wt_image real_estate_visit_36
                    player.c "Look at me, sex doll. You want to please me by swallowing every drop when I cum in your mouth."
                    wt_image real_estate_visit_40
                    "She wraps her lips tight around your dick as she sucks you to orgasm, swallowing each spurt you shoot down her throat."
                    player.c "[player.orgasm_text]"
                    $ geri.hypno_swallow_count += 1
                "On her face":
                    wt_image real_estate_visit_36
                    player.c "Look at me, sex doll. You want to please me by taking my load on your face."
                    "She nods."
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_5
                    player.c "Lick my cock clean, sex doll."
                    "She cleans you up as your sperm drips down her chest and chin."
                    $ geri.hypno_facial_count += 1
        else:
            wt_image real_estate_visit_17
            player.c "You want me to feel good, Geri. Kneel in front of me and use your mouth to make me feel good."
            wt_image real_estate_visit_36
            "She presses her soft lips against your cock ..."
            wt_image real_estate_visit_40
            "... then opens her mouth and takes you inside."
            "It's an enthusiastic and single-minded blow job that soon has you ready to cum."
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    wt_image real_estate_visit_36
                    player.c "You want to please me, Geri. You want to please me by swallowing every drop when I cum in your mouth."
                    wt_image real_estate_visit_40
                    "She wraps her lips tight around your dick as she sucks you to orgasm, swallowing each spurt you shoot down her throat."
                    player.c "[player.orgasm_text]"
                    $ geri.hypno_swallow_count += 1
                "On her breasts":
                    wt_image real_estate_visit_36
                    player.c "You want to please me, Geri. You want to please me by taking my load on your face."
                    "She nods."
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_5
                    player.c "Lick my cock clean, Geri."
                    "She cleans you up as your sperm drips down her chest and chin."
                    $ geri.hypno_facial_count += 1
        $ geri.hypno_blowjob_count += 1
        orgasm
        wt_image real_estate_visit_1
        "You have her cover herself up and bring her out of her trance."
        wt_image real_estate_visit_15
        geri.c "Thanks for inviting me over! I love getting to chat with you and seeing what you've done with your new place. I've got a house viewing coming up, so need to run. Call me again soon!"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_7
    return

label geri_home_tj_hypnosis:
    if living_room.is_here:
        if geri.has_tag('hypno_look_at_her_today'):
            wt_image real_estate_visit_17
            "Your mindless sex doll has nice large tits, the sort that would feel good around your cock."
            player.c "Wrap your tits around my cock, sex doll."
            wt_image real_estate_visit_6
            player.c "Now fuck me with your tits."
            "She strokes her soft breasts up and down your shaft until you're ready to cum."
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    player.c "Wrap your lips around my cock, sex doll, but keep fucking me with your tits."
                    wt_image real_estate_visit_7
                    "She sucks on your cock head as uses her boobs to coax the sperm out of your balls."
                    player.c "[player.orgasm_text]"
                    $ geri.hypno_swallow_count += 1
                "On her breasts":
                    player.c "Keep looking at me, sex doll."
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_5
                    player.c "Lick my cock clean, sex doll."
                    "She cleans you up as your sperm drips down her chest and chin."
                    $ geri.hypno_facial_count += 1
        else:
            wt_image real_estate_visit_17
            player.c "You want me to feel good, Geri. Kneel in front of me and use your tits to make me feel good."
            wt_image real_estate_visit_6
            "She wraps her soft breasts around your cock and strokes them up and down your shaft."
            "It's not long before you're ready to cum."
            $ title = "Where do you want to cum?"
            menu:
                "In her mouth":
                    player.c "You want to please me, Geri. You can please me by wrapping your lips around my cock while you fuck me with your tits."
                    wt_image real_estate_visit_7
                    "She sucks on your cock head as uses her boobs to coax the sperm out of your balls."
                    player.c "[player.orgasm_text]"
                    $ geri.hypno_swallow_count += 1
                "On her breasts":
                    player.c "Keep looking at me, Geri.  You want my cum on you, Geri."
                    "She nods."
                    wt_image real_estate_visit_35
                    player.c "[player.orgasm_text]"
                    wt_image real_estate_visit_5
                    player.c "Lick my cock clean, Geri."
                    "She cleans you up as your sperm drips down her chest and chin."
                    $ geri.hypno_facial_count += 1
        $ geri.hypno_titfuck_count += 1
        orgasm
        wt_image real_estate_visit_1
        "You have her cover herself up and bring her out of her trance."
        wt_image real_estate_visit_15
        geri.c "Thanks for inviting me over! I love getting to chat with you and seeing what you've done with your new place. I've got a house viewing coming up, so need to run. Call me again soon!"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_8
    return

label geri_home_sex_hypnosis:
    if living_room.is_here:
        if geri.has_tag('hypno_look_at_her_today'):
            wt_image real_estate_visit_14
            "Your mindless sex doll looks good enough to fuck, so that's what you do."
            player.c "Get on your hands and knees, sex doll, and I'll use you like a doll should be used."
            wt_image real_estate_visit_18
            player.c "Eyes forward, sex doll.  There's no need for a doll to be looking at me while I fuck it."
        else:
            player.c "You want to have sex with me, Geri. Spread your legs and offer yourself to me."
            wt_image real_estate_visit_23
            "The hypnotized woman makes herself available to you."
            player.c "Get on your hands and knees, Geri, to make it easier for me to fuck you."
            wt_image real_estate_visit_18
            player.c "There's no need to look at me while I fuck you, Geri. Look straight ahead so I can concentrate on enjoying the sight of your ass while I bone you."
        wt_image real_estate_visit_9
        "The hypnotized woman faces forward as you enjoy her pussy. She came here hoping to be fucked. Now she has been, even if she won't remember."
        player.c "[player.orgasm_text]"
        $ geri.hypno_sex_count += 1
        orgasm
        wt_image real_estate_visit_1
        "You have her cover herself up and bring her out of her trance."
        wt_image real_estate_visit_15
        geri.c "Thanks for inviting me over! I love getting to chat with you and seeing what you've done with your new place. I've got a house viewing coming up, so need to run. Call me again soon!"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_9
    return

label geri_home_pose_hypnosis:
    if living_room.is_here:
        add tags "hypno_look_at_her_today" to geri
        player.c "You're so pretty, Geri, you look like a doll. A sexy doll who likes it when I fuck her. You're so pretty you don't need to talk or say anything or do anything for me to enjoy fucking you."
        player.c "I like thinking of you as my sex doll, Geri. You like being my sex doll because then I'm happy and you like making me happy."
        player.c "Make me happy, Geri. Lie back and show me your body like a mindless sex doll, Geri."
        wt_image real_estate_visit_14
        "Your mindless sex doll waits happily as you inspect her. "
    ## note: this action is created with backtrack = True, therefore at the end it will automatically back up to the hypnosis options menu
    return

label geri_home_nothing_else_hypnosis:
    if living_room.is_here:
        "That's nothing else you want to do with your doll today, so you simply enjoy a view of it's body for a while."
        wt_image real_estate_visit_1
        "When you've looked at her long enough, you have her cover herself up and bring her out of her trance."
        wt_image real_estate_visit_15
        geri.c "Thanks for inviting me over! I love getting to chat with you and seeing what you've done with your new place. I've got a house viewing coming up, so need to run. Call me again soon!"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_10
    return

label geri_nothing_hypnosis:
    "That's nothing in particular you want to do with Geri today, so you simply enjoy a view of her tits for a while."
    if geri_office.is_here:
        wt_image real_estate_office_portrait_1
        "When you've looked at her long enough, you have her cover herself up and bring her out of her trance."
        geri.c "Thanks for dropping by to chat!  Feel free to come by anytime."
    if living_room.is_here:
        wt_image real_estate_visit_1
        "When you've looked at her long enough, you have her cover herself up and bring her out of her trance."
        wt_image real_estate_visit_15
        geri.c "Thanks for inviting me over! I love getting to chat with you and seeing what you've done with your new place. I've got a house viewing coming up, so need to run. Call me again soon!"
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_11
    return

label geri_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
    if player.has_tag('hypnotist') and not geri.has_tag('no_hypno_trigger_message'):
        add tags 'no_hypno_trigger_message' to geri
        "You've hypnotized Geri multiple times but are no closer to implanting a hypnotic trigger.  She seems to be immune to receiving a trigger."
    return

label geri_hypnosis_end:
    $ geri.hypno_session() # this deducts energy and tracks that you've hypno'd her
    if geri_office.is_here:
        notify
        "You let her get back to her work."
        call forced_movement(office_tower) from _call_forced_movement_49
    if living_room.is_here:
        call character_location_return(geri) from _call_character_location_return_228
        notify
        wt_image current_location.image
    return


## Character Specific Actions
# N/A

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
label geri_contact:
    wt_image real_estate_phone
    if geri.g_status == 1:
        player.c "Geri, would you like to get together?"
        geri.c "For personal matters or professionally?"
        $ title = "Which is it?"
        menu:
            "Personal matters":
                player.c "Definitely personal."
                geri.c "I appreciate the offer, but I'm not in a good place right now. I caught my ex husband cheating on me with another woman. I literally caught her in our bed after she just finished fucking my husband."
                geri.c "I'm angry at her for ruining my life, I'm angry at him for being a jerk, I'm angry at myself for falling in love with such a jerk. I keep obsessing over that moment of walking in on her."
                geri.c "I'm just not in the right head space to trust or open myself up to someone."
                "Sounds like Geri has an issue to sort out.  You'll need a particular set of circumstances, though, to deal with her obsession."
                $ geri.g_status = 2
            "Professionally":
                if not player.has_tag('signed_house_docs'):
                    geri.c "You don't need to see me to finish the paperwork on your house purchase.  The documents are with a lawyer in my building, the North Office Tower."
                else:
                    if player.has_tag('wealthy'):
                        geri.c "Really?  Are you interested in buying another home?  Maybe something bigger?"
                        player.c "Probably.  Not today, though."
                    else:
                        geri.c "You can't afford to own two homes, and I'd highly recommend you not try to sell your new home so quickly.  People will think there's something wrong with it."
                        player.c "That's fine.  I wasn't looking to sell, anyway."
                    "There isn't really anything to discuss with her, professionally."
        if not player.has_tag('signed_house_docs'):
            geri.c "Don't forget to sign those papers at the lawyer.  We need those to close the file on the purchase of your house."
    elif geri.g_status == 3:
        wt_image real_estate_phone_2
        geri.c "Thanks for calling! I wanted to thank you again for last night. It's helped me more than I could have imagined."
        geri.c "If you ever want me to thank you again properly, just let me know. Or drop by my office."
        geri.c "Bye for now!"
        add tags 'trained_today' to geri ## to delay next contact
        $ geri.g_status = 4
    else:
        call expandable_menu(geri_contact_menu) from _call_expandable_menu_10
        if not player.has_tag('signed_house_docs'):
            geri.c "Don't forget to sign those papers at the lawyer.  We need those to close the file on the purchase of your house."
    if not geri.location == living_room:
        wt_image current_location.image
    return

label geri_contact_ask_out:
    player.c "Hi Geri, it's me. I just wanted to check in to see if you've changed your mind about getting together?"
    geri.c "It's sweet of you to ask, but no. I'm still in full-on-obsession mode about that cheating bitch I found in our bed.  I'm just not ready to start seeing anyone."
    return

label geri_contact_discuss_lauren:
    if not geri.has_tag('discussed_cheater'):
        add tags 'discussed_cheater' to geri
        player.c "Geri, I just wanted to let you know I may have a solution to your problem."
        geri.c "My problem?"
        player.c "The issue you've been obsessing over.  I'll be in touch soon."
    else:
        player.c "I haven't forgotten about the solution to your problem. I'll give you a call when it's all set up."
        geri.c "What are you up to?"
        player.c "You'll see."
    "You can set up a meeting between Lauren and Geri on a future session with Lauren."
    return

label geri_contact_visit_you:
    summon geri to living_room no_follows
    "Geri changes into more comfortable clothes then comes right over."
    wt_image real_estate_visit_15
    if geri.has_tag('contact_kept_waiting_complete'):
        geri.c "I hope I didn't keep you waiting."
    else:
        add tags 'contact_kept_waiting_complete' to geri
        geri.c "I hope I didn't keep you waiting. I kept you waiting too long before I'd agree to see you."
    if geri.has_tag('no_masturbation_this_week'):
        rem tags 'no_masturbation_this_week' from geri
        add tags 'no_masturbation_last_week' to geri
        player.c "Have you masturbated since your last visit?"
        wt_image real_estate_visit_1
        geri.c "No"
        player.c "Why not?"
        geri.c "I don't do that very often, anyway."
        player.c "Except when you're horny, I expect. You left here feeling horny and you've probably felt horny at least once or twice since. Why didn't you play with yourself when you were alone?"
        geri.c "You asked me not to."
        player.c "And you obeyed me. That makes me feel good. How did it feel to you, obeying me even though I wasn't there?"
        geri.c "I ... I promised you I wouldn't.  And I always keep my word."
        "That's not exactly an answer, but it's as much as she's willing to say on the topic."
    elif geri.has_tag('orgasm_denial_conversation'):
        player.c "Did you come over hoping you'd get sexual satisfaction, or to make sure I was sexually satisfied?"
        geri.c "It'd be nice if it was both."
        player.c "And what will satisfy you more, getting to cum or serving me?"
        wt_image real_estate_visit_1
        geri.c "Do I have to choose?"
        player.c "No.  I'll choose for you."
    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_geri:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_geri:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_geri:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_geri:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_geri:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_geri:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_geri:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_geri:
  geri.c "I'm not thirsty, thank you."
  return

# Give Transformation Potion
label give_tp_geri:
  geri.c "I'm not thirsty, thank you."
  return

# Use Water Bowl
label use_wb_geri:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_geri:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label geri_start_day:
  ## End Day - 1st Wednesday? Real Estate Agent
  if day == 3 and geri.g_status == 0:
    call geri_visit_first from _call_geri_visit_first
  ## End Day - Real Estate Agent Thank You
  if geri.g_status == 3:
    call geri_visit_thank_you from _call_geri_visit_thank_you
  return

# End Day - 1st Wednesday? Real Estate Agent
label geri_visit_first:
  wt_image front_door
  "The next morning, there's another knock on your door."
  summon geri
  wt_image real_estate_portrait_1
  "It's your real estate agent, Geri."
  geri.c "Hi!  I just wanted to drop by to make sure you got moved in okay."
  $ geri.g_status = 1
  $ title = "What do you do?"
  menu:
    "Invite her in":
      # rem tags 'no_hypnosis' from geri #to allow subsequent test to function properly and open up hypnosis at her office ## not needed
      player.c "Everything's just fine, thank you.  Please come in and see."
      wt_image real_estate_first_visit_1
      "You show Geri to your living room and she takes a seat."
      geri.c "Wow.  I love what you've done with this place!"
      $ title = "What do you do next?"
      menu:
        "Ask about her story":
          player.c "So what's your story, Geri?"
          geri.c "Oh, I'm just a normal, middle aged woman who walked in on her man fucking another woman in their bed. Now I'm alone, and staying that way, because I don't trust men - or women. "
          geri.c "I'm bitter and angry, and can't let go of the thought of how much I want to punish that bitch for ruining my life. And I can't let go of the thought of what an idiot I was for falling for a jerk who would cheat on me like that."
          "She laughs."
          geri.c "There.  You wanted my story.  That's me in a nutshell."
          $ title = "How do you reply?"
          menu:
            "People are bitches":
              player.c "People can be bitches.  Women and men, both."
              wt_image real_estate_first_visit_6
              geri.c "Indeed they can. It's been nice chatting with you. I'm glad you've settled in nicely. If you need anything, give me a call or come visit me at my office downtown."
            "Anything I can do to ease your pain?":
              player.c "Anything I can do to ease your pain?"
              "She laughs."
              geri.c "Thanks. I'm flattered by the offer. But I'm not looking to be saved from myself, not by you or any other man."
              wt_image real_estate_first_visit_6
              geri.c "I'm glad you've settled in nicely. If you need anything, give me a call or come visit me at my office downtown."
        "Show her the boudoir":
          call forced_movement(boudoir) from _call_forced_movement_429
          wt_image real_estate_first_visit_4
          "You show Geri the boudoir. It's not as well equipped as you'd like just yet, but it still sets a mood."
          geri.c "I'm sure you'll fix this room up nicely. It reminds me of the bedroom my husband and I had, before I walked in on him fucking another woman in our bed."
          player.c "That sounds awkward."
          geri.c "It was. I wanted to kill him. I wanted to kill myself for being such an idiot as to fall for the jerk. Most of all I wanted to kill her, for ruining my life."
          geri.c "Okay, kill is a little strong. But make her pay for what she did, oh yes. I wanted to make her pay. And I still do. Yes, I'm still a little bitter."
          wt_image real_estate_first_visit_6
          "She laughs."
          geri.c "Thanks for the little tour. I really must be going. I'm glad you've settled in nicely. If you ever need anything, give me a call or come visit me at my office downtown."
          call forced_movement(living_room) from _call_forced_movement_430
        "Show her the dungeon":
          call forced_movement(dungeon) from _call_forced_movement_431
          wt_image real_estate_first_visit_5
          "You show Geri the dungeon. It's not as well equipped as you'd like just yet, but it still sets a mood."
          geri.c "Wow. You're the first client I know of to do this with their house."
          player.c "Have I shocked you?"
          wt_image real_estate_first_visit_4
          geri.c "Not at all. I could use one of these at my place. I have the perfect person in mind to show it to."
          player.c "Oh?  Who?"
          geri.c "The little bitch I caught fucking my husband in our bed. I've been obsessing about making her pay for what she did ever since that day."
          geri.c "Of course, I've also been obsessing about what a jerk he was, and what an idiot I was for falling for him. But yes, having my revenge on her has become my number one obsession."
          player.c "I don't suppose I could help you with that?"
          wt_image real_estate_first_visit_6
          "She laughs."
          geri.c "Thanks for the offer, but she's long gone. Skedaddled to parts unknown, some dark dank hole I hope."
          geri.c "Thanks for the little tour. I really must be going. I'm glad you've settled in nicely. If you ever need anything, give me a call or come visit me at my office downtown."
          call forced_movement(living_room) from _call_forced_movement_432
        "Hypnotize her" if player.can_hypno(geri):
          $ geri.hypno_session() # this deducts energy and tracks that you've hypno'd her
          player.c "Geri, would you please look at this for me?"
          call focus_image from _call_focus_image_27
          player.c "Listen to me, Geri. Listen to me. Listen to my voice and nothing else, Geri. Only my voice. Only my voice now."
          wt_image real_estate_first_visit_2
          "She soon falls under your trance."
          player.c "You and I are going to have a conversation, Geri. I want you to be comfortable for our conversation. I want to enjoy our conversation."
          wt_image real_estate_first_visit_6
          player.c "Show me your breasts, Geri, so that you can be comfortable and I can enjoy our chat."
          wt_image real_estate_first_visit_3
          if not player.has_tag('first_hypno_breasts_message'):
            add tags 'first_hypno_breasts_message' to player
            "The suggestion to bare her breasts is a simple one. You find it fascinating how easily women comply with it. Some are just comfortable with their bodies, some are proud of their breasts, others are insecure but hoping for approval. Whatever their reasons, it makes the rest of the session more enjoyable for you."
          player.c "Tell me about yourself, Geri."
          geri.c "I'm alone. I had a man, but he cheated on me. I caught him in bed with another woman. I hate her. I want to punish her for ruining my life. I hate him, too, for being such a jerk. I hate myself for letting myself fall for such a jerk. "
          geri.c "I don't trust men, and I'm too scared of being hurt to let myself get close to another one. I'm too angry, at her, at him, to even try trusting someone new."
          "Wow.  It seems Geri's been spending a lot of time psycho analyzing herself. That just flowed out of her like water."
          "The anger is too tough a barrier to get at. You try working on her trust in you, in case that comes in handy down the road, then you have her cover herself up and bring her out of her trance."
          wt_image real_estate_first_visit_1
          geri.c "Gee, thanks for the chat!  You seem like a really trustworthy guy."
          wt_image real_estate_first_visit_6
          geri.c "I have to go now.  Remember, if you ever need anything, just give me a call or come visit me at my office downtown,"
      $ geri.g_status = 2
    "Send her away" :
      player.c "Everything's just fine, thank you."
      "She waits for a moment to see if you're going to invite her in. When it's obvious you're not, she dismisses herself."
      geri.c "Well, that's great.  If you need anything, give me a call or come visit me at my office downtown."
  if player.has_tag('signed_house_docs'):
    geri.c "Oh, and thanks for signing those documents with the lawyer.  Your file is complete and you have good title to the house now.  Bye!"
  else:
    geri.c "Oh, and don't forget about those documents with the lawyer.  You can find her downtown in the North Office Tower, the same building I'm in.  Bye!"
  $ office_tower.action_visit_geri = office_tower.add_action("Visit Geri the Realtor's Office", context = '_elevator', label = "geri_office_visit")
  call character_location_return(geri) from _call_character_location_return_229
  wt_image current_location.image
  return

# End Day - Real Estate Agent Thank You
label geri_visit_thank_you:
  wt_image phone_1
  "Your phone is ringing."
  wt_image real_estate_phone_2
  geri.c "Hi!  It's Geri. I just wanted to thank you again for last night. It's helped me more than I could have imagined."
  geri.c "If you ever want me to thank you again properly, just let me know. Or drop by my office."
  geri.c "Bye for now!"
  $ geri.g_status = 4
  wt_image current_location.image
  return

# End Day
label geri_end_day:
    rem tags 'masturbated_today' 'kneeling_today' 'hypno_look_at_her_today' 'no_masturbation_last_week' from geri
    return

# End Week
label geri_end_week:
    pass
    return

## Character Specific Timers
# N/A

########### ROOMS ###########
# Real Estate Agent's Office - Examine
label go_examine:
  "Geri the Real Estate Agent's Office."
  return

label go_no_access:
  return

# Real Estate Agent's Office - Prevent Access
# OBJECT: Elevator
label geri_office_visit:
    if geri.can_be_interacted and geri.g_status != 3:
        call move_to(geri_office) from _call_move_to_2
    else:
        "Geri is not in her office."
    return

label go_enter:
  if geri.can_be_interacted:
    if geri.g_status == 1:
      $ geri.location = geri_office
      wt_image real_estate_office_9
      "Geri is working in her office when you walk in."
      geri.c "Oh!  What a lovely surprise."
    elif geri.g_status == 2:
      $ geri.location = geri_office
      wt_image real_estate_office_9
      "Geri is working in her office when you walk in."
      geri.c "Oh!  Hi again!"
    elif geri.g_status == 4:
      $ geri.location = geri_office
      wt_image real_estate_office_9
      "Geri's sitting behind her desk.  Her phone rings just as you walk in."
      wt_image real_estate_office_3
      "She motions for you to wait as she takes the call."
      wt_image real_estate_office_12
      geri.c "I'm so sorry to have kept you waiting."
      wt_image real_estate_office_4
      geri.c "I've done that too often, haven't I?  Kept you waiting when you wanted to spend time with me."
      wt_image real_estate_office_portrait_1
      geri.c "Let me know if there's something I can do to make that up to you."
    else:
      "Geri is not in her office at the moment."
      call forced_movement(office_tower) from _call_forced_movement_50
  else:
    "Geri is not in her office at the moment."
    call forced_movement(office_tower) from _call_forced_movement_51
  return

label go_exit:
  return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
