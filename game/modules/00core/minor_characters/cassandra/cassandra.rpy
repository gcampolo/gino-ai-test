## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package cassandra name "Cassandra" description "Allows Cassandra to be a minor character." dependencies core club
register cassandra_pregame 20 in core as 'Cassandra the Domme' # must come after alexis so talk to her action about alexis works correctly

# Pregame
label cassandra_pregame:
  python:
    ## Credits
    model_credits += [('support', 'Cassandra the Domme (Candy Manson)')]

  ## Constants
    ## Character Definition
    cassandra = Person(Character("Woman in the Club", who_color="#408080", what_color="#408080", window_background = gui.dialogue_background_dark_font_color), "cassandra", cut_portrait = True, prefix = "", suffix = "")
    cassandra.trigger_phrase = "Thank me properly for your lesbian playtoy."

    ## Actions
    cassandra.action_introduce = cassandra.add_action("Introduce yourself", label="_introduce", condition = "cassandra.can_be_interacted and not cassandra.has_tag('introduced')")
    cassandra.action_talk = cassandra.add_action("Talk to her", label="_talk", condition = "cassandra.can_be_interacted and cassandra.has_tag('introduced')")

    # Continuing Visits Actions
    cassandra.action_contact = living_room.add_action("Invite [cassandra.name] and her sub for dinner", label = cassandra.short_name + "_contact", context = "_contact_other", condition = "cassandra.can_be_interacted and cassandra.has_tag('contact_open')")

    ## Tags
    # Common Character Tags
    cassandra.add_tags('can_be_in_club', 'no_hypnosis', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    cassandra.change_status("minor_character")

    # Start Day Events
    #start_day_labels.append('cassandra_start_day') # no needed

    ########### VARIABLES ###########
    # Common Character Variables
    #cassandra.add_stats_with_value('temporary_count') #not needed as this is auto-added for characters
    cassandra.add_stats_with_value('hypno_anal_count', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_sex_count', 'hypno_swallow_count', 'random_number')

    # Character Specific Variables
    cassandra.add_stats_with_value('discuss_barista', 'independent_encounter_status')

    ######## EXPANDABLE MENUES #######
    cassandra_club_talk_menu = ExpandableMenu("What do you want to talk to her about?")
    # note: these don't have to be defined in pregame, can be added in game
    cassandra.choice_talk = cassandra_club_talk_menu.add_choice("Just chit chat", "cassandra_chit_chat", condition = "cassandra.independent_encounter_status < 2")
    cassandra.choice_talk = cassandra_club_talk_menu.add_choice("Ask about [terri.name]", "cassandra_terri", condition = "cassandra.independent_encounter_status > 2")
    cassandra.choice_discuss_lauren = cassandra_club_talk_menu.add_choice("Discuss Lauren", "cassandra_discuss_lauren", condition = "lauren.status == 'on_training' and lauren.revenge_count > 1 and not cassandra.has_tag('discussed_cheater')")
    cassandra.choice_discuss_sam = cassandra_club_talk_menu.add_choice("Discuss Sam the Barista", "cassandra_discuss_sam", condition = "cassandra.discuss_barista == 1 or cassandra.discuss_barista == 3")
    cassandra.choice_discuss_alexis = cassandra_club_talk_menu.add_choice("Discuss [alexis.name]' anal issues", "cassandra_discuss_alexis_anal", condition = "alexis.anal_discussion == 1 and not alexis.has_tag('anal_domme_opened')")

  return

# Display Portrait
# CHARACTER: Display Portrait
label cassandra_update_media:
    if current_location == club:
        $ cassandra.change_image('cassandra_club_1')
    else:
        pass
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label cassandra_examine:
    "A casually dressed woman at the Club."
    return

# Talk to Character
label cassandra_talk:
    if current_location == club:
        $ cassandra.temporary_count = 1
        wt_image cassandra.image
        cassandra.c "Hello"
        ## first, check for Terri thank you event
        if cassandra.independent_encounter_status == 2:
            player.c "How are things with you and [terri.name]?"
            wt_image cassandra_hypno_3
            cassandra.c "Amazing! She's at my place now, cleaning. She's quite the little domestic. And such a funny child. She loves to be given chores around the house and treated like a little girl."
            player.c "How's the sex life?"
            wt_image cassandra_hypno_7
            cassandra.c "Incredible. She gets so guilty and so turned on when we have sex, it's hilarious. I've never seen such a repressed lesbian. I have to punish her every time she cums, just to make her feel better."
            wt_image cassandra_club_1
            cassandra.c "I'm so grateful to you for connecting the two of us. Is there anything I can do to thank you?"
            $ title = "Do you want to be thanked?"
            menu:
                "Let's go somewhere private":
                    rem tags 'no_hypnosis' from cassandra #to allow subsequent test to function properly
                    player.c "I can think of one way you can thank me. Would you like to accompany to a private room?"
                    wt_image cassandra_hypno_4
                    "Your suggestion startles [cassandra.name]."
                    cassandra.c "Oh. That wasn't really what I meant. Still, I suppose I could, considering all you've done for me. Just once, though."
                    wt_image cassandra_hypno_7
                    "You lead her to a private room."
                    $ title = "What do you do with her?"
                    menu:
                        "Have sex with her":
                            cassandra.c "I suppose it won't kill me to have sex with a man one more time."
                            wt_image cassandra_bj_1
                            "She drops to her knees and places your cock between her giant breasts. She may be a lesbian, but she knows what men like."
                            if cassandra.has_tag('past_revealed'):
                                pass
                            else:
                                player.c "So you've had sex with men before?"
                                cassandra.c "Oh yes. I was a submissive for a number of men before I realized I had things completely backwards and that what I really wanted was to have a woman who was submissive to me."
                                add tags 'past_revealed' to cassandra
                            wt_image cassandra_bj_8
                            "Sure enough, she gives great head.  She flicks her tongue along the sensitive underside of your cockhead ..."
                            wt_image cassandra_bj_9
                            "... then swirls it around your balls."
                            wt_image cassandra_bj_2
                            "Once she finally takes you inside, her talented mouth soon has your balls screaming for relief."
                            $ title = "Let her finish you with her mouth?"
                            menu:
                                "Yes, a blow job's great":
                                    wt_image cassandra_bj_7
                                    player.c "Take off your clothes, [cassandra.name].  I want to see more of you."
                                    wt_image cassandra_bj_4
                                    "She strips out of her clothes and shows off her tits while you decide where you want to cum."
                                    $ title = "Where do you want to cum?"
                                    menu:
                                        "In her":
                                            wt_image cassandra_bj_10
                                            player.c "[player.orgasm_text]"
                                            wt_image cassandra_hypno_4
                                            cassandra.c "I hope that was okay.  I haven't done that in a while."
                                            $ cassandra.swallow_count += 1
                                        "On her":
                                            wt_image cassandra_bj_3
                                            player.c "[player.orgasm_text]"
                                            wt_image cassandra_bj_6
                                            cassandra.c "I hope that was okay.  I haven't done that in a while."
                                            $ cassandra.facial_count += 1
                                    player.c "It was great, [cassandra.name]!  You should re-think being a lesbian."
                                    wt_image cassandra_hypno_3
                                    cassandra.c "That's hilarious after what [terri.name] tells me you did for her.  I'm glad you enjoyed it.  Thanks again for connecting me with [terri.name]."
                                    $ cassandra.blowjob_count += 1
                                "No, you want to fuck her":
                                    wt_image cassandra_bj_7
                                    player.c "Lie back and spread your legs, [cassandra.name]."
                                    wt_image cassandra_sex_1
                                    cassandra.c "Ohhhh. It's been a while since I've had an actual flesh cock inside me."
                                    player.c "Miss it?"
                                    wt_image cassandra_sex_7
                                    cassandra.c "Not really.  No offense.  What you're doing feels fine.  It's just ..."
                                    player.c "I'm no girl?"
                                    wt_image cassandra_sex_6
                                    cassandra.c "Exactly."
                                    wt_image cassandra_sex_4
                                    player.c "This feels good, but you're not very wet.  Is this hurting you?"
                                    cassandra.c "A little.  Sorry."
                                    wt_image cassandra_sex_3
                                    player.c "What if we try like this?  Maybe my maleness will be less of a distraction if I'm behind you."
                                    wt_image cassandra_sex_2
                                    cassandra.c "Yeah, that is a bit better."
                                    wt_image cassandra_sex_3
                                    "It's actually a lot better, at least for you, as her pussy is wet enough to be able to fuck her quickly without hurting her, but not so wet that you can't enjoy the tight friction of her inner walls against your shaft."
                                    wt_image cassandra_sex_2
                                    cassandra.c "Careful. I'm not on birth control."
                                    wt_image cassandra_bj_3
                                    "Not likely to be too many lesbians who are.  That's okay.  With her attributes, there was never much of a question as to where you were going to cum.  Your cock doesn't care about her sexual orientation. Its happy to receive the suck-and-fuck and shows its appreciation by depositing your load over [cassandra.name]'s giant breasts."
                                    player.c "[player.orgasm_text]"
                                    wt_image cassandra_bj_6
                                    cassandra.c "I hope you enjoyed my 'thank you'.  This is probably the last time I fuck a man."
                                    player.c "It was definitely my pleasure, [cassandra.name]."
                                    $ cassandra.sex_count += 1
                                    orgasm notify
                            $ cassandra.temporary_count = 2
                        "Dominate her" if player.has_tag('dominant'):
                            cassandra.c "I suppose it won't kill me to have sex with a man one more time."
                            wt_image cassandra_bj_1
                            "She drops to her knees and places your cock between her giant breasts."
                            player.c "This is not how we're doing this, girl. You're going to thank me properly. The way a submissive girl shows her gratitude. By submitting to my authority over you for the next hour."
                            if cassandra.has_tag('past_revealed'):
                                cassandra.c "Yes, Sir."
                                player.c "Good girl.  Go dress according to your station."
                            else:
                                cassandra.c "Yes, Sir. How did you know I used to be a submissive? Back before I realized I had things completely backwards and that what I really wanted was to have a woman who was submissive to me."
                                player.c "You're still submissive by nature to men, aren't you [cassandra.name]?"
                                cassandra.c "Only certain men, Sir. It's not really the right path for me, but for you, yes, I acknowledge your authority over me for today."
                                player.c "Thank you, girl.  Go dress according to your station."
                                add tags 'past_revealed' to cassandra
                            wt_image cassandra_sub_1
                            "The Club keeps its private rooms well stocked with toys. You bring out an appropriate selection while [cassandra.name] goes to borrow some clothes from the Club's wardrobe. She returns a few minutes later and changes while you watch."
                            wt_image cassandra_sub_23
                            "She finishes by putting on one of the Club's collars and kneeling beside the table on which you've placed the toys you picked out."
                            wt_image cassandra_sub_2
                            if player.has_item(will_tamer):
                                $ title = "Use Will-Tamer on her?"
                                menu:
                                    "Yes":
                                        wt_image cassandra_sub_14
                                        cassandra.c "Sir, I'll wear the Club's collar for you, but I don't think it's appropriate for me to wear your personal collar.  I am thankful to you for introducing [terri.name] to me and I will submit to you today to show my gratitude, but I'm not your sub and won't wear your collar."
                                        wt_image cassandra_sub_2
                                        "Oh well.  It was worth a try."
                                    "No":
                                        pass
                            $ title = "What do you do with her?"
                            menu:
                                "Discipline her first":
                                    player.c "Bring me the leather paddle."
                                    wt_image cassandra_sub_3
                                    "She picks it up from the table and puts it in her mouth."
                                    wt_image cassandra_sub_4
                                    "She understands what's expected of her. Not surprising for a Domme who was trained as a sub. The paddle in her mouth, she crawls over to you."
                                    wt_image cassandra_sub_5
                                    "The paddle delivered into your hand, she turns and presents her bottom to you."
                                    wt_image cassandra_sub_6
                                    "She doesn't question why you're beating her. She gave you authority over her for today, and she knew that included the authority to hurt her if you feel like it.  And you do."
                                    wt_image cassandra_sub_7
                                    "For a woman of [cassandra.name]'s attributes, however, spanking her ass is just a warm up. Her tits are the main event. She trembles as you caress her chest with the paddle."
                                    wt_image cassandra_sub_8
                                    "You won't get this chance again, and there's no reason to hold back.  You give her tits everything they can handle, striking them from every side and angle, harder and harder as they get redder and redder.  [cassandra.name] tries very hard not to make any noise, but the pain is too much.  The cutest little yelps of pain escape from her after each blow."
                                    cassandra.c "ohhh .... ohhhh .... oohhhhh oh oh oh"
                                    wt_image cassandra_sub_9
                                    "When you think she can't take any more of the paddle, you switch to clamps.  [cassandra.name] can no longer even try to keep the cries of pain from escaping her."
                                    cassandra.c "Owwww ... ow ow ow ow owwwwww!"
                                    change player energy by -energy_short
                                    $ title = "What do you do with her now?"
                                    menu:
                                        "Have sex with her now":
                                            wt_image cassandra_sub_10
                                            "You leave clamps on temporarily as you open her mouth and insert your cock."
                                            player.c "Keep your eyes on me girl."
                                            wt_image cassandra_sub_11
                                            "She screams around your cock as you pull the clamps off, releasing a painful flow of blood into her abused nipples."
                                            cassandra.c "Aaaggggghhh!!!"
                                            call cassandra_dominate_sex from _call_cassandra_dominate_sex
                                        "That's enough":
                                            pass
                                "Have sex with her":
                                    call cassandra_dominate_sex from _call_cassandra_dominate_sex_1
                            wt_image cassandra_sub_14
                            cassandra.c "I hope you enjoyed my thank you, Sir.  May I be released from your service now?"
                            player.c "Yes, [cassandra.name].  I did, and you may."
                            $ cassandra.temporary_count = 2
                        "Hypnotize her" if player.can_hypno(cassandra):
                            wt_image cassandra_hypno_3
                            "Once the two of you are alone, you turn to [cassandra.name]."
                            player.c "[cassandra.name], would you please look at this for me?"
                            call focus_image from _call_focus_image_23
                            player.c "Listen to me now, [cassandra.name]. Listen to me. Listen to my voice and nothing else, [cassandra.name]. Only my voice. Only my voice now."
                            wt_image cassandra_hypno_1
                            "She soon falls under your trance."
                            player.c "[cassandra.name], you are here to thank me. You should be comfortable while thanking me."
                            wt_image cassandra_hypno_4
                            player.c "Take off your top and show me your breasts, [cassandra.name]."
                            wt_image cassandra_hypno_5
                            player.c "That's better, [cassandra.name].  You want to thank me, [cassandra.name]. You want to thank me for introducing [terri.name] to you. You are grateful to me for bringing [terri.name] into your life."
                            wt_image cassandra_hypno_2
                            cassandra.c "Yes, I want to thank you.  I'm very grateful to you."
                            $ title = "What do you want her to do?"
                            menu menu_cassandra_hypno_thank_you:
                                "Have her bark like a dog":
                                    if not cassandra.has_tag('on_knees_now'):
                                        add tags 'on_knees_now' to cassandra
                                        wt_image cassandra_hypno_5
                                        cassandra.c "Rrrufff.  Ruff!"
                                        player.c "Not like that, silly.  Down on the ground like a proper bitch."
                                        wt_image cassandra_bark_1
                                        "[cassandra.name] drops to her hands and knees and starts crawling around you like it's the most natural thing in the world to her.  Perhaps she's been putting [terri.name] through a similar training?"
                                    else:
                                        wt_image cassandra_bark_1
                                    cassandra.c "Rrruufff.  Ruff ruff."
                                    jump menu_cassandra_hypno_thank_you
                                "Have her blow you":
                                    if cassandra.has_tag('on_knees_now'):
                                        wt_image cassandra_bark_1
                                        player.c "Be a grateful lesbian bitch, [cassandra.name], and suck my cock."
                                    else:
                                        player.c "Be a grateful lesbian, [cassandra.name], and get on your knees and suck my cock."
                                        wt_image cassandra_hypno_5
                                    cassandra.c "Yes, Sir."
                                    wt_image cassandra_bj_4
                                    "She shows off her massive breasts as she takes your cock in her mouth. She may be a lesbian, but she knows what men like."
                                    if cassandra.has_tag('past_revealed'):
                                        pass
                                    else:
                                        player.c "Have you sucked a cock before, [cassandra.name]?"
                                        wt_image cassandra_bj_11
                                        cassandra.c "Yes, Sir. I was a submissive for a number of men before I realized I had things completely backwards and that what I really wanted was to have a woman who was submissive to me."
                                        add tags 'past_revealed' to cassandra
                                    wt_image cassandra_bj_12
                                    "Sure enough, she gives great head, paying careful attention to your balls as well as your cock."
                                    wt_image cassandra_bj_4
                                    "How odd is it to get one of the best blow jobs you're had in years from a lesbian Domme you've hypnotized into being your sexual servant?"
                                    wt_image cassandra_bj_5
                                    "Your cock doesn't care about her sexual orientation. It's happy to receive the world class pleasuring, and to show its appreciation by depositing your load into [cassandra.name]'s waiting mouth and over her giant breasts."
                                    wt_image cassandra_bj_6
                                    player.c "[player.orgasm_text]"
                                    $ cassandra.hypno_blowjob_count += 1
                                    $ cassandra.hypno_facial_count += 1
                                    orgasm notify
                                    call cassandra_hypno_enough from _call_cassandra_hypno_enough
                                "That's enough for now":
                                    call cassandra_hypno_enough from _call_cassandra_hypno_enough_1
                            $ cassandra.temporary_count = 2
                        "Change mind":
                            player.c "Actually, maybe we should do this another time."
                            cassandra.c "Okay"
                    add tags 'no_hypnosis' to cassandra
                    if cassandra.temporary_count > 1:
                        $ cassandra.independent_encounter_status = 3
                        $ cassandra.dismiss(False)
                        $ cassandra.temporary_count = 0
                "Perhaps another time":
                    player.c "There may be a way you can thank me, but not right now."
                    wt_image cassandra_hypno_3
                    cassandra.c "Okay"
                "No thanks necessary (shuts off this option)":
                    player.c "No thanks necessary, [cassandra.name]. I'm just glad things are working out for you and [terri.name]."
                    wt_image cassandra_hypno_3
                    cassandra.c "They are, thanks to you!"
                    $ cassandra.independent_encounter_status = 3
        ## then check for possible Terri solution
        elif terri.status == "on_training" and terri.ready_for_domme > 0 and cassandra.independent_encounter_status == 1:
            if not cassandra.has_tag('discussed_terri'):
                player.c "[cassandra.name], I may have found the right woman for you."
                wt_image cassandra_hypno_4
                "You explain the situation with [terri.name]."
                wt_image cassandra_hypno_3
                cassandra.c "Wow. That sounds like an - exciting - opportunity.  Let me know when she's ready to meet me. If she really is the submissive, closet lesbian you think she is, she may be just the person I've been looking for."
                add tags 'discussed_terri' to cassandra
            else:
                wt_image cassandra_hypno_3
                cassandra.c "I can't wait to meet that submissive repressed lesbian you told me about."
            sys "You can set up [cassandra.name] to meet [terri.name] on a future training session."
        ## then go on to talk option if not shut off
        if cassandra.temporary_count == 1:
            $ cassandra.temporary_count = 0
            call expandable_menu(cassandra_club_talk_menu) from _call_expandable_menu_8
    else:
        "You have nothing to say to her here."
    wt_image current_location.image
    return

label cassandra_club_hypno_trigger:
    add tags 'trained_today' to cassandra
    player.c "How are things between you and [terri.name]?"
    wt_image cassandra_hypno_7
    cassandra.c "Amazing.  I can't thank you enough for connecting the two of us."
    player.c "That's true, you can't.  '[cassandra.trigger_phrase]'."
    wt_image cassandra_hypno_1
    player.c "You were saying something about wanting to thank me."
    wt_image cassandra_hypno_4
    cassandra.c "Yes, Sir.  Should I suck your cock, Sir?"
    if cassandra.has_tag('past_revealed'):
        $ title = "What do you want?"
        menu:
            "Blow job":
                call cassandra_thank_bj from _call_cassandra_thank_bj
            "Sex":
                wt_image cassandra_sex_3
                "You have her undress and bend over."
                player.c "Think about [terri.name] and get wet, [cassandra.name]."
                wt_image cassandra_sex_2
                cassandra.c "Oh, yes."
                "Her cunt moistens immediately, and you push yourself into her easily."
                wt_image cassandra_sex_7
                "After a while, you turn her over so you can enjoy the view of her enormous tits."
                wt_image cassandra_sex_4
                "Watching [cassandra.name]'s big jugs bounce back-and-forth as you fuck her gay cunt soon has you ready to cum.  As a lesbian, she's unlikely to be on birth control, so you should probably pull out."
                $ title = "Pull out?"
                menu:
                    "Yes, cum on her":
                        wt_image cassandra_bj_3
                        "You do the gentlemanly thing and deposit your load on her face as she kneels mindlessly in front of you."
                        player.c "[player.orgasm_text]"
                        wt_image cassandra_bj_5
                        "You admire the hypnotized woman in this position for a while, watching as your cum drips down her mouth and onto her breasts ..."
                        wt_image cassandra_bj_6
                        "... then command her to clean herself up and get dressed and forget what happened."
                        $ cassandra.hypno_facial_count += 1
                    "No, cum inside her":
                        wt_image cassandra_sex_5
                        "If this causes a problem for her, that's her issue, not yours.  She's not going to remember you ever had your cock inside her."
                        wt_image cassandra_sex_6
                        player.c "[player.orgasm_text]"
                        wt_image cassandra_hypno_6
                        "When your balls stop pumping your jizz into her womb, you have her dress and send her off, carrying your load inside her, with no memory of what the two of you just did."
                $ cassandra.hypno_sex_count += 1
                orgasm notify
            "Hurt her":
                player.c "You're a Domme and you used to be a submissive, [cassandra.name]. So you know that a submissive can properly thank someone by letting them hurt her."
                wt_image cassandra_hypno_3
                cassandra.c "Yes, Sir.  Did you want to hurt me?"
                player.c "Yes, [cassandra.name].  I do."
                wt_image cassandra_sub_3
                "The Club is well stocked with play items for the use of its patrons.  It doesn't take [cassandra.name] long to locate an outfit suitable for a sub and a leather paddle."
                wt_image cassandra_sub_4
                "She knows the rules of BDSM well, crawling over to you with the paddle in her mouth."
                wt_image cassandra_sub_5
                "She waits on hands and knees beside you as you examine the paddle, then begin spanking her with it ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                wt_image cassandra_sub_6
                "Her ass is soon a pretty shade of red.  But her ass is not [cassandra.name]'s primary attribute."
                wt_image cassandra_sub_7
                "She starts to tremble as you caress her breasts with the paddle."
                player.c "Are your tits sensitive, [cassandra.name]?"
                cassandra.c "Very"
                player.c "So this is going to hurt a lot, isn't it?"
                cassandra.c "Yes"
                player.c "That means you're thanking me a lot.  You are grateful to me and want to thank me a lot, don't you?"
                cassandra.c "Yes, Sir."
                player.c "So what does that mean?"
                cassandra.c "I want you to hurt my tits, Sir. Hurt them a lot, please, so that I can show you how thankful I am to you."
                wt_image cassandra_sub_8
                "It wouldn't be gentlemanly to refuse such a polite request. You strike her tits from every angle. As requested, you make it hurt. A lot."
                cassandra.c "Owww!   Oowwww!!  Ow ow ow oooowwww!!!!"
                wt_image cassandra_sub_9
                "When her tits are a uniform shade of crimson, you give [cassandra.name] a final opportunity to show you how grateful she is. You send her off to find some nipple clamps, then put them to use."
                cassandra.c "Aaaaggghhhhhhh!!!!"
                player.c "You're welcome [cassandra.name]."
                wt_image cassandra_sub_14
                "You admire her in this position for a while as she tries to fight through the pain, then have her dress and release her from her trance."
                change player energy by -energy_short notify
            "Bondage sex":
                player.c "You want to thank me properly, [cassandra.name]. You know how you would want [terri.name] to thank you. You were a submissive to men, so you know how I want you to thank me."
                wt_image cassandra_hypno_6
                cassandra.c "Yes, Sir."
                wt_image cassandra_sub_11
                "She strips off her clothes. The Club's private rooms are well stocked with play toys.  She finds a corset and a collar ..."
                wt_image cassandra_sub_23
                "... and places it around her neck, then kneels in front of you."
                wt_image cassandra_sub_14
                cassandra.c "I am available for your use, Sir, to thank you for making [terri.name] part of my life."
                if player.has_item(will_tamer):
                    $ title = "Use Will-Tamer on her?"
                    menu:
                        "Yes":
                            cassandra.c "Sir, I'll wear the Club's collar for you, but I don't think it's appropriate for me to wear your personal collar. I am thankful to you for introducing [terri.name] to me and I will submit to you today to show my gratitude, but I am not your sub and will not wear your collar."
                            "There's a limit to what a subject will accept when under a trance, and Dommes and submissives put a lot of importance on collars and collarings. Oh well. It was worth a try."
                        "No":
                            pass
                wt_image cassandra_sub_11
                "She's available for your use, so you may as well use her.  You pull her mouth onto your cock. She gives amazingly good head for a lesbian."
                $ title = "What do you do?"
                menu:
                    "Cum in her mouth":
                        wt_image cassandra_sub_12
                        "When the blow job is this good, why have her stop?  Within a few minutes, you fill the lesbian's mouth with your cum."
                        wt_image cassandra_sub_13
                        player.c "[player.orgasm_text]"
                        wt_image cassandra_sub_14
                        "After you've recovered and she's swallowed your load, you have her dress and command her to forget what happened."
                        $ cassandra.hypno_blowjob_count += 1
                        $ cassandra.hypno_swallow_count += 1
                        orgasm notify
                    "Cum in her ass":
                        wt_image cassandra_sub_15
                        "You send her off to collect some rope, then bind her to the bed.  You don't need to have her tied up, but its fun seeing the hypnotized Domme in this position."
                        wt_image cassandra_sub_22
                        "She's been fucked this way before.  She's tight, but she knows how to relax her sphincter muscles, and you've soon buried your cock up to the hilt in her butt."
                        wt_image cassandra_sub_16
                        "When you unload your seed into her, she gasps.  You wonder how long its been since she's had semen inside her, either inside her pussy or inside her bowels."
                        wt_image cassandra_sub_22
                        player.c "[player.orgasm_text]"
                        wt_image cassandra_sub_15
                        "When you've recovered, you untie her and have her dress and rlease her from her trance."
                        $ cassandra.hypno_anal_count += 1
                        orgasm notify
            "Just have her bark like a dog":
                wt_image cassandra_hypno_1
                cassandra.c "Rrrufff.  Ruff!"
                player.c "Not like that, silly.  Down on the ground like a proper bitch."
                wt_image cassandra_bark_1
                "[cassandra.name] strips off her clothes.  Then she drops to her hands and knees and starts crawling around you like it's the most natural thing in the world to her.  Perhaps she's been putting [terri.name] through a similar training?"
                cassandra.c "Rrruufff.  Ruff ruff."
                wt_image cassandra_hypno_6
                "When you've had your fun, you have her dress and release her from her trance."
    else:
        player.c "Have you sucked a cock before, [cassandra.name]?"
        wt_image cassandra_hypno_3
        cassandra.c "Yes, Sir.  I was a submissive for a number of men before I realized I had things completely backwards and that what I really wanted was to have a woman who was submissive to me."
        player.c "Go ahead, then.  Show me how you suck cock."
        add tags 'past_revealed' to cassandra
        call cassandra_thank_bj from _call_cassandra_thank_bj_1
    wt_image current_location.image
    return

label cassandra_chit_chat:
    player.c "How goes the hunt?"
    cassandra.c "Frustrating.  It's so hard to find the right woman."
    player.c "I've heard that."
    if player.slavegirl_count > 0 and not cassandra.has_tag('asked_about_lending_slave'):
        $ title = "Offer her a slavegirl?"
        menu:
            "Yes":
                player.c "I have a pretty slavegirl I can lend you, if you like?"
                cassandra.c "That's nice of you to offer, but I'm looking for the love of my life, not someone who's already taken. Thank you anyway."
                add tags 'asked_about_lending_slave' to cassandra
            "No":
                pass
    return

label cassandra_terri:
    player.c "How are you?  And how is [terri.name]?"
    cassandra.c "We're both great, thank you.  She's at home, cleaning again.  In the nude.  With ben wa balls inside her."
    wt_image cassandra_hypno_7
    cassandra.c "She'll be ready to beg for an orgasm by the time I get home.  Except she won't.  Not directly anyway.  She's still ashamed to have sex with me.  Can you believe it?  That doesn't keep the sex from being incredibly hot.  Shit, maybe it helps."
    wt_image cassandra_club_1
    cassandra.c "Thanks again for connecting us."
    if not cassandra.has_any_tag('contact_open', 'never_contact'):
        $ title = "Suggest [cassandra.name] bring [terri.name] to visit you sometime?"
        menu:
            "Yes, suggest they come for dinner someday":
                add tags 'contact_open' to cassandra
                cassandra.c "I'd like that.  Here's my number.  Call me sometime and we'll get together."
            "Not now":
                pass
            "Never (shuts off question)":
                add tags 'never_contact' to cassandra
    return

label cassandra_discuss_lauren:
    player.c "[cassandra.name], I have someone you may want to meet."
    cassandra.c "Really?  Is she a lesbian?  And a submissive?"
    player.c "Neither, actually.  She's a cheating housewife and I'm punishing her on behalf of her husband and the other people she's hurt.  Part of her punishment is making up for the pain she caused the wife of the man she cheated with."
    player.c "I'm looking for a dominant woman to use her in whatever way you want.  She's quite obedient even if she isn't naturally submissive.  And you can use her to get off in any way you'd like."
    cassandra.c "Wow.  You have an interesting life, don't you?"
    cassandra.c "I'm afraid I'll have to pass.  I'm looking for the love of my life.  I've had enough one night stands.  Not that whatever crazy psycho shit you're talking about counts as a one night stand even."
    "Oh well.  There's always the internet as a way to find a dominant woman to take revenge on Lauren."
    add tags 'discussed_cheater' to cassandra
    return

label cassandra_discuss_sam:
    # discuss Samantha as lesbian
    if cassandra.discuss_barista == 1:
        # if know Sam is not a sub
        if samantha.discussed_submission == 2:
            player.c "[cassandra.name], I have someone you may want to meet."
            cassandra.c "Really?  Is she a lesbian?  And a submissive?"
            player.c "A lesbian, yes. A submissive, not so much. She used to spank her ex girlfriend, but says she has no interest in getting her own tail swatted."
            cassandra.c "That doesn't sound like the right girl for me. I could accept some limits, but I couldn't imagine settling down with someone who didn't enjoy being put over my lap for regular spankings."
            player.c "I'll keep looking for you."
            $ cassandra.discuss_barista = 2
        # otherwise, opens up discussed submission with Sam
        else:
            player.c "[cassandra.name], I have someone you may want to meet."
            cassandra.c "Really?  Is she a lesbian?  And a submissive?"
            player.c "A lesbian, yes.  A submissive, I'm not sure."
            cassandra.c "Well, if she is submissive, then I'd be very happy to meet her."
            player.c "I'll check it out, and let you know."
            $ samantha.discussed_submission = 1
    # discuss Samantha as Domme
    elif cassandra.discuss_barista == 3:
        player.c "[cassandra.name], I have a proposition for you.  How'd you like to train an aspiring young Domme?"
        cassandra.c "Why would I want to do that?"
        player.c "As the first part of her training, you could have her serve you."
        cassandra.c "I'm trying to find the love of my life. I'm not interested in short-term relationships, especially with someone who's not naturally submissive."
        cassandra.c "However, I do know a friend who may be able to help you. She used to be a professional Domme, though she gave that up a few years ago."
        cassandra.c "She likes girls and boys equally, and she was always a bit of a -- slut, but I mean that in a good way, in that she's not hung up like I am on finding love and meaning. She's always been fine with enjoying sex in the moment."
        cassandra.c "The only thing is, is your friend hot? Because Jesse's also a bit of a snob, and would only go for this if your friend's hot enough that Jesse will want to bang her."
        cassandra.c "I'm sure Jesse will be very interested in my friend."
        "[cassandra.name] gives you Jesse's contact information. A quick call to Jesse - complete with a physical description of Sam - confirms that Jesse is eager to help the current barista find more meaningful work."
        "Now you just need to let Sam know you have a training solution for her."
        $ cassandra.discuss_barista = 4
    return

label cassandra_discuss_alexis_anal:
    player.c "Have you ever had to train a sub who believed she couldn't do anal sex?  Not just a dislike of anal, but a belief she physically can't do it."
    cassandra.c "No, but anal has never really been a big thing for me."
    "She starts to laugh."
    cassandra.c "I know! You should talk to Angie the Anal Domme."
    cassandra.c "Oh God! Don't tell her I called her that!!  That's so rude of me."
    player.c "Who's Angie?"
    cassandra.c "A lovely woman who just happens to have a huge fascination with her slaves' butt hole."
    cassandra.c "You should send your friend to her. I'm sure she'd love the opportunity to work out your friend's issue."
    "[cassandra.name] has a hard time stifling her laughter as she digs out Angie's contact information."
    cassandra.c "Here it is. I think Angie works weekdays, but I bet she'd find time on the weekend to assist your friend."
    sys "Once she's ready to let you work on her anal deficiencies, you can send [alexis.name] to Angie for training on the weekend, if you want."
    add tags 'anal_domme_opened' to alexis
    return

## Character Specific Actions
# Introduce Yourself
label cassandra_introduce:
    wt_image cassandra.image
    player.c "Hello"
    cassandra.c "Oh, hello."
    $ title = "What do you ask her?"
    menu:
        "Do you come here often?":
          player.c "Come here often?"
          cassandra.c "Occasionally. It seems as good a place as any to find what I'm looking for."
          player.c "What are you looking for?"
          cassandra.c "A woman."
          player.c "Aren't we all.  Any particular make and model, or would anyone do?"
          "She laughs."
          cassandra.c "A submissive woman. One who's looking for a Domme."
        "Looking for anything in particular tonight?":
          player.c "Are you looking for something in particular tonight?"
          cassandra.c "Yes.  A woman."
          player.c "Aren't we all.  Any particular make and model, or would anyone do?"
          "She laughs."
          cassandra.c "A submissive woman. One who's looking for a Domme."
        "Would you like a drink?":
          player.c "Would you like a drink?"
          cassandra.c "Thank you, but no.  I don't drink.  At least, not here."
          player.c "Oh?  Serious business tonight, have you?"
          cassandra.c "Serious enough, I suppose.  I'm looking for a life partner.  The woman of my dreams, preferably."
          player.c "Aren't we all. Any particular make and model that you have in mind?"
          "She laughs."
          cassandra.c "A submissive woman. One who's looking for a Domme."
        "Would you like to fuck?":
          player.c "Would you like to fuck?"
          cassandra.c "I'd love to.  Only, not you, my dear.  A woman."
          player.c "Wouldn't we all.  Any particular make and model, or would anyone do?"
          "She laughs."
          cassandra.c "A submissive woman. One who's looking for a Domme."
    $ title = "How do you reply?"
    menu:
        "I'll see what I can send your way":
            player.c "I'll see what I can send your way."
            $ cassandra.change_full_name("", "Cassandra", "the Domme")
            cassandra.c "How sweet.  My name's [cassandra.name], by the way."
            player.c "Nice to meet you, [cassandra.name]."
        "You seem more a sub to me than a Domme":
            if player.has_tag('dominant'):
                player.c "How interesting.  I would have pegged you for a submissive woman yourself."
                "She looks closely at you and hesitates a moment before answering."
                cassandra.c "Yes, Sir.  I have been a submissive to a number of men.  That turned out not to be the right path for me.  I'm drawn to other women, and find I am as naturally dominant with them as I was naturally submissive with men.  I'm afraid I don't play with men any more, Sir."
                player.c "My loss, to be sure.  I hope you find the right sub for you."
                $ cassandra.change_full_name("", "Cassandra", "the Domme")
                cassandra.c "Thank you, Sir.  I hope so, too.  My name's [cassandra.name], by the way."
                player.c "Nice to meet you, [cassandra.name]."
                add tags 'past_revealed' to cassandra
            else:
                player.c "Funny, I would have pegged you more as the submissive type yourself, rather than a Domme."
                cassandra.c "Perhaps you're just not good at reading women?"
                player.c "Perhaps not.  Enjoy your day."
                $ cassandra.change_full_name("", "Cassandra", "the Domme")
                cassandra.c "Thanks.  You too.  My name's [cassandra.name], by the way."
                player.c "Nice to meet you, [cassandra.name]."
        "Are all the women here lesbian?":
            player.c "Are all the women in this Club lesbian?"
            cassandra.c "Relatively few of them are, from what I can tell.  But perhaps they've been lying to me.  Or to you."
            $ cassandra.change_full_name("", "Cassandra", "the Domme")
            cassandra.c "My name's [cassandra.name], by the way."
            player.c "Nice to meet you, [cassandra.name]."
        "Good luck":
            player.c "Good luck with that."
            $ cassandra.change_full_name("", "Cassandra", "the Domme")
            cassandra.c "Thanks!  My name's [cassandra.name], by the way."
            player.c "Nice to meet you, [cassandra.name]."
    $ cassandra.independent_encounter_status = 1
    add tags 'introduced' to cassandra
    return

label cassandra_dominate_sex:
  $ title = "How do you want to fuck her?"
  menu:
    "Fuck her on her back":
      wt_image cassandra_sub_15
      "The Club's private rooms are conveniently equipped for sexual activities of all kinds. Even straight missionary sex with a subgirl can be spiced up with a few ropes."
      cassandra.c "Sir, I'm not on birth control."
      $ title = "What do you do?"
      menu:
        "Have her blow you instead":
          wt_image cassandra_sub_11
          "Taking a firm grip of hair, you guide her mouth up and down your cock"
          wt_image cassandra_sub_12
          "Surprisingly for a lesbian, however, you discover she knows her way around a dick.  You're able to loosen your grip and enjoy as she bobs her head back and forth along your shaft."
          wt_image cassandra_sub_13
          "Your cock doesn't care about her sexual orientation. Its happy to show its appreciation for the excellent blow job by depositing your load into [cassandra.name]'s waiting mouth."
          player.c "[player.orgasm_text]"
          $ cassandra.blowjob_count += 1
        "Fuck her ass":
          wt_image cassandra_sub_16
          "She doesn't protest as you push yourself into her ass while you spread her pussy open to enjoy the view."
          wt_image cassandra_sub_22
          "Her ass is tight and warm and after a few minutes, it's filled with your seed.  She lets out a whimper as you pump your load into her. From what she's told you, its been a while since she's had cum inside her anywhere, let alone up her ass."
          player.c "[player.orgasm_text]"
          cassandra.c "ohh"
          $ cassandra.anal_count += 1
    "Fuck her ass from behind":
      wt_image cassandra_sub_17
      "You push a finger into her ass, testing to see how tight she is."
      player.c "You're used to having men fuck your butt, I presume."
      cassandra.c "Yes Sir, but it's been quite a while."
      wt_image cassandra_sub_18
      "You pick up a butt plug from the table. It soon confirms that a trained ass doesn't forget."
      player.c "Just like riding a bicycle, girl. Except, of course, you're the one who's going to be ridden."
      cassandra.c "Yes, Sir."
      wt_image cassandra_sub_19
      "You don't need to tie her up before you fuck her, but its fun. She sucks in her breath but otherwise makes no sound as you push yourself into her ass and past her sphincter."
      wt_image cassandra_sub_20
      "There's nothing like the inside of a tied up lesbian Domme's ass to make your cock feel special.  It soon shows its appreciation by filling her bowels with your hot cum."
      wt_image cassandra_sub_21
      player.c "[player.orgasm_text]"
      "She lets out a whimper as you pump your load into her. From what she's told you, its been a while since she's had cum inside her anywhere, let alone up her ass."
      cassandra.c "ohh"
      $ cassandra.anal_count += 1
    "Just fuck her mouth":
      wt_image cassandra_sub_11
      "Taking a firm grip of hair, you guide her mouth up and down your cock"
      wt_image cassandra_sub_12
      "Surprisingly for a lesbian, however, you discover she knows her way around a dick.  You're able to loosen your grip and enjoy as she bobs her head back and forth along your shaft."
      wt_image cassandra_sub_13
      "Your cock doesn't care about her sexual orientation. Its happy to show its appreciation for the excellent blow job by depositing your load into [cassandra.name]'s waiting mouth."
      player.c "[player.orgasm_text]"
      $ cassandra.blowjob_count += 1
  orgasm notify
  return

label cassandra_hypno_enough:
    if player.has_tag('hypnotist') or player.hypnosis_level > 10:
        "[cassandra.name]'s surprisingly easy to control hypnotically. Choose a trigger phrase for her."
        $ title = "What do you want her trigger phrase to be?"
        menu menu_cassandra_choose_trigger_phrase:
            "[cassandra.trigger_phrase]":
                pass
            "Choose something else":
                $ cassandra.trigger_phrase = renpy.input(_("What is her trigger phrase?"))
                $ title = "Are you sure you want her trigger phrase to be '[cassandra.trigger_phrase]'?"
                menu:
                    "Yes":
                        pass
                    "No, choose something else":
                        jump menu_cassandra_choose_trigger_phrase
        player.c "You are very grateful. You are so grateful, that whenever I say \"[cassandra.trigger_phrase]\", you will follow me to a private room. Do you understand?"
        wt_image cassandra_hypno_5
        cassandra.c "Yes. When you say \"[cassandra.trigger_phrase]\", I will follow you to a private room."
        player.c "Good. You are so grateful to me that you will do anything to please me. I brought you [terri.name] and made you happy. You want me to be happy, too. When you and I are alone in private, you will do whatever I ask of you. Do you understand?"
        wt_image cassandra_hypno_2
        cassandra.c "Yes, when I'm alone in private with you, I will do anything you ask to make you happy. Because you were good to me and brought me [terri.name]."
        player.c "Get dressed now, [cassandra.name]. You will not remember what we talked about today. You will only remember that you are grateful to me and want to thank me. And you will remember what to do when I tell you \"[cassandra.trigger_phrase]\"."
        wt_image cassandra_hypno_1
        cassandra.c "Yes, Sir."
        wt_image cassandra_club_1
        "When she's dressed, you bring her out of her trance."
        cassandra.c "Thank you again for introducing [terri.name] to me. You wouldn't believe how grateful I am to you."
        add tags 'trigger_implanted' to cassandra
        $ cassandra.choice_talk_trigger = cassandra_club_talk_menu.add_choice("Use her trigger", "cassandra_club_hypno_trigger")
    else:
        player.c "Get dressed now, [cassandra.name]."
        wt_image cassandra_hypno_1
        cassandra.c "Yes Sir."
        wt_image cassandra_club_1
        "When she's dressed, you bring her out of her trance. If you were a stronger Hypnotist, you might have been able to convince her that she hadn't thanked you yet, but as it is, all you can do is prevent her from remembering exactly what the two of you did together."
        cassandra.c "Thank you again for introducing [terri.name] to me."
    $ cassandra.hypno_session() # this subtracts energy and records that she was hyno'd
    wt_image current_location.image
    return

label cassandra_thank_bj:
    wt_image cassandra_bj_7
    "[cassandra.name] gives amazingly good head, especially considering she's a lesbian."
    wt_image cassandra_bj_8
    "She flicks her tongue along the sensitive underside of your cockhead ..."
    wt_image cassandra_bj_9
    "... then swirls it around your balls."
    wt_image cassandra_bj_2
    "Once she finally takes you inside, her talented mouth soon has your balls screaming for relief, but you want to see her naked before you cum."
    wt_image cassandra_bj_4
    "She strips out of her clothes and shows off her tits on command while you decide where you want to cum."
    $ title = "Where do you want to cum?"
    menu:
        "In her":
            wt_image cassandra_bj_10
            player.c "[player.orgasm_text]"
            wt_image cassandra_hypno_6
            "When she finishes swallowing your load, you command her to get dressed and forget what just happened."
            $ cassandra.hypno_swallow_count += 1
        "On her":
            wt_image cassandra_bj_3
            player.c "[player.orgasm_text]"
            wt_image cassandra_bj_5
            "You admire the hypnotized woman in this position for a while, watching as your cum drips down her mouth and onto her breasts ..."
            wt_image cassandra_bj_6
            "... then command her to clean herself up and get dressed and forget what happened."
            $ cassandra.hypno_facial_count += 1
    $ cassandra.hypno_blowjob_count += 1
    orgasm notify
    return

label cassandra_contact:
    wt_image cassandra_phone_1
    cassandra.c "Sure, I could bring [terri.name] by your place for dinner.  Did you want to do that today?"
    wt_image cassandra_phone_2
    $ title = "Invite them over now?"
    menu:
        "Yes, come on over":
            call cassandra_terri_visit from _call_cassandra_terri_visit
        "Not right now":
            wt_image cassandra_phone_1
            cassandra.c "Some other time, then."
            wt_image current_location.image
    return

label cassandra_terri_visit:
    $ cassandra.training_session()
    $ terri.training_session()
    summon cassandra no_follows
    summon terri no_follows
    wt_image indy_cassandra_73
    "[cassandra.name] greets you warmly on arrival ..."
    wt_image indy_cassandra_74
    "... while [terri.name] waits with head bowed, a smile on her face."
    wt_image indy_cassandra_75
    cassandra.c "Help your former trainer set the table, child."
    terri.c "Yes, Mistress.  It's good to see you again, [terri.your_respect_name]."
    wt_image indy_cassandra_76
    "With the table set and the food served, the three of you sit down to eat."
    wt_image indy_cassandra_77
    "You and [cassandra.name] chat while you eat.  [terri.name] listens, but doesn't participate in the conversation.  [cassandra.name] seems to be of the opinion that her girl should be seen, but not heard, and [terri.name] seems fine with that."
    wt_image indy_cassandra_78
    cassandra.c "That was delicious.  Thanks so much for inviting us over, and for everything you've done for us."
    $ title = "What do you want before they go?"
    menu:
        "Watch [terri.name] be punished":
            wt_image indy_cassandra_79
            player.c "[terri.name] was awfully noisy while she was eating, don't you think?"
            wt_image indy_cassandra_80
            cassandra.c "Oh, I know!  I don't understand how she can make so much noise chewing her food.  I'll discipline her about it when we get home."
            wt_image indy_cassandra_81
            player.c "Why not here?  She might learn better if the punishment immediately follows the offense."
            wt_image indy_cassandra_82
            cassandra.c "She might at that.  Stand up, child.  You've embarrassed me in front of your former trainer.  You're going across my knee."
            wt_image indy_cassandra_83
            cassandra.c "Remove your dress."
            wt_image indy_cassandra_84
            cassandra.c "And remove my jeans, so I'm comfortable."
            wt_image indy_cassandra_85
            cassandra.c "Since the offense took place in your house, I'll let you decide how long her spanking should be."
            wt_image indy_cassandra_86
            $ title = "How many spanks should she get?"
            menu:
                "Five":
                    rem tags 'counting_now' from terri
                    $ terri.random_number = 5
                    cassandra.c "You're right, the embarassment of being spanked is likely enough.  Up on my lap, child, and be grateful that your former trainer is so kind to you."
                "Ten":
                    rem tags 'counting_now' from terri
                    $ terri.random_number = 10
                    cassandra.c "That seems about right.  Up on my lap, child."
                "Ten and she should count":
                    add tags 'counting_now' to terri
                    $ terri.random_number = 10
                    cassandra.c "That seems about right.  Up on my lap, child."
                "Twenty":
                    rem tags 'counting_now' from terri
                    $ terri.random_number = 20
                    cassandra.c "You're probably right, I should be strict with her.  Otherwise, she won't learn.  Up on my lap, child."
                "Twenty and she should count":
                    add tags 'counting_now' to terri
                    $ terri.random_number = 20
                    cassandra.c "You're probably right, I should be strict with her.  Otherwise, she won't learn.  Up on my lap, child."
                "Fifty":
                    rem tags 'counting_now' from terri
                    $ terri.random_number = 25
                    cassandra.c "That seems overly harsh.  I think twenty-five is more than enough.  Up on my lap, child."
                "Fifty and she should count":
                    add tags 'counting_now' to terri
                    $ terri.random_number = 25
                    cassandra.c "That seems overly harsh.  I think twenty-five is more than enough.  Up on my lap, child."
            wt_image indy_cassandra_87
            "[terri.name] gets into position, her bum twitching slightly in anticipation of the spanking to come."
            $ terri.temporary_count = 0
            # spanking
            while terri.temporary_count < terri.random_number:
                $ terri.temporary_count += 1
                if terri.temporary_count < 5:
                    wt_image indy_cassandra_57
                    "*SMACK*"
                    wt_image indy_cassandra_15
                    if terri.has_tag('counting_now'):
                        terri.c "Ow!  That's [terri.temporary_count.to_s]."
                    else:
                        terri.c "Ow!"
                elif terri.temporary_count < 10:
                    wt_image indy_cassandra_58
                    "*SMACK*"
                    wt_image indy_cassandra_59
                    if terri.has_tag('counting_now'):
                        terri.c "Oww!!  That's [terri.temporary_count.to_s]."
                    else:
                        terri.c "Oww!!"
                elif terri.temporary_count < 20:
                    wt_image indy_cassandra_16
                    "*SMACK*"
                    wt_image indy_cassandra_61
                    if terri.has_tag('counting_now'):
                        terri.c "Oowww!!!  That's [terri.temporary_count.to_s]."
                    else:
                        terri.c "Oowww!!!"
                else:
                    wt_image indy_cassandra_87
                    terri.c "Oh, Mistress, please??  Not another?!"
                    wt_image indy_cassandra_60
                    "*SMACK*"
                    wt_image indy_cassandra_61
                    if terri.has_tag('counting_now'):
                        terri.c "Oww ooowwww!!!  My bum is hurting so much, Mistress!!  That's [terri.temporary_count.to_s]."
                    else:
                        terri.c "Oww ooowwww!!!  My bum is hurting so much, Mistress!!"
            # post-spanking finish
            wt_image indy_cassandra_85
            cassandra.c "Spanking's over, child.  What do you say to our host?"
            if terri.random_number == 5:
                wt_image indy_cassandra_88
                terri.c "Thank you for being kind to me and making that a short spanking.  I promise, it was still effective.  I'm sorry I needed to be punished on my visit.  I'll try very hard to be a better girl if you invite Mistress and I back again."
            elif terri.random_number == 10:
                wt_image indy_cassandra_89
                terri.c "I'm sorry I had to be punished during my visit.  I'll try to be better next time, if you invite Mistress and I back again."
            elif terri.random_number == 20:
                wt_image indy_cassandra_90
                terri.c "I'm sorry I was such a bad girl on my visit that you and Mistress both felt I deserved a severe spanking.  I'll try to be better next time, if I'm allowed back."
            else:
                wt_image indy_cassandra_90
                terri.c "I'm sorry I was such a disappointment to you that you wanted Mistress to spank me so harshly.  I cherish the training you gave me and especailly cherish you introducing me to Mistress.  I hate knowing that I disappointed you.  I'll try to be a better girl next time, if I'm allowed back."
            $ terri.temporary_count = 0
            $ terri.random_number = 0
            change player energy by -energy_very_short notify
        "Watch [terri.name] nurse":
            wt_image indy_cassandra_91
            player.c "[terri.name] hasn't eaten much off her plate."
            wt_image indy_cassandra_92
            cassandra.c "Oh, that's not a reflection of your cooking.  She's probably just nervous.  She can be a noisy eater and probably doesn't want to embarrass herself while she's visiting you, so she's just been picking at her food."
            wt_image indy_cassandra_93
            player.c "Maybe she'd like to nurse?  If she's hungry and nervous, that may soothe her."
            wt_image indy_cassandra_78
            cassandra.c "What do you say, child?  Would you like to nurse before we go home?  Or will you be too embarrassed with your former trainer watching?"
            wt_image indy_cassandra_81
            terri.c "If you think I should nurse, Mistress, I'll try not to be too embarrassed."
            wt_image indy_cassandra_94
            cassandra.c "Take your clothes off and come suckle, then.  It'll put you in the right frame of mind for the drive home."
            wt_image indy_cassandra_95
            "If [terri.name] is feeling embarrassed, she hides it well.  If anything, she's a little too eager to nurse for [cassandra.name]'s preference."
            wt_image indy_cassandra_19
            cassandra.c "Careful with your teeth, child.  I'll tell you when I want you to bite my nipples.  Today, you're just to nurse on them."
            wt_image indy_cassandra_67
            terri.c "I'm sorry, Mistress."
            wt_image indy_cassandra_65
            "[terri.name] does her best to rectify her mistake ..."
            wt_image indy_cassandra_66
            "... taking as much of [cassandra.name]'s boob as she can into her mouth and suckling on it ..."
            wt_image indy_cassandra_9
            "... and paying particular attention to her nipple, but with lips and tongue only, no teeth."
            wt_image indy_cassandra_96
            cassandra.c "That's enough nursing for now.  Did you want to cuddle before you put your clothes back on?"
            terri.c "Yes, Mistress.  I'd like that."
            wt_image indy_cassandra_97
            "'Cuddling' seems to consist of [terri.name] burying her face between [cassandra.name]'s massive mounds ..."
            wt_image indy_cassandra_98
            "... and keeping it there.  Which, come to think of it, does seem like it could be a soothing experience for both of them."
            wt_image indy_cassandra_64
            cassandra.c "Cuddle time's over, child, it's time we head home.  Thank your former trainer for inviting us."
            wt_image indy_cassandra_99
            terri.c "Thank you for letting Mistress and me visit, and for suggesting that I nurse before we go home."
            change player energy by -energy_very_short notify
        "Watch [cassandra.name] give [terri.name] an orgasm":
            wt_image indy_cassandra_100
            player.c "[terri.name]'s been a very good girl during our meal.  Perhaps you should reward her before you go?"
            wt_image indy_cassandra_101
            cassandra.c "By 'reward', I presume you mean sexually?  You're not suggesting I give her a lolly?"
            wt_image indy_cassandra_79
            player.c "Why not sexually?  She's shown she can be obedient.  A little positive reinforcement wouldn't hurt?"
            wt_image indy_cassandra_102
            cassandra.c "Well, I wouldn't normally reward my sub in front of an audience, but considering how much you've done for us, I guess I could make an exception for you."
            wt_image indy_cassandra_94
            cassandra.c "Take your clothes off, child, and join me on the bed.  I'm going to reward you by giving you a chance to please me.  And, apparently, reward your former trainer, too, by letting him watch."
            wt_image indy_cassandra_103
            "As [cassandra.name] licks the redhead's tiny breast ..."
            wt_image indy_cassandra_104
            "... [terri.name]'s nipple immediately stiffens.  She reaches out and cups [cassandra.name]'s boob ..."
            wt_image indy_cassandra_105
            "... squeezing and fondling it as she has her own breast suckled."
            wt_image indy_cassandra_106
            terri.c "Oohhh"
            wt_image indy_cassandra_107
            cassandra.c "You're getting wet between the legs, child.  Lie down."
            wt_image indy_cassandra_108
            cassandra.c "I want to drink every sticky drop you have to give me, so no holding back on me.  Make a big, wet mess between your legs for me."
            wt_image indy_cassandra_109
            terri.c "Yes, Mistress."
            wt_image indy_cassandra_110
            "Focussing [terri.name] on pleasing her, rather than on [terri.name]'s own arousal, may be [cassandra.name]'s way to overcome any lingering guilt [terri.name] has about becoming sexually aroused by another woman."
            wt_image indy_cassandra_111
            "If so, it's an effective one, as the combination of her tongue on [terri.name] ..."
            wt_image indy_cassandra_112
            "... and her fingers inside [terri.name] ..."
            wt_image indy_cassandra_113
            "... soon have the submissive redhead cumming buckets."
            wt_image indy_cassandra_114
            terri.c "Oooohhhhhhhh!!"
            wt_image indy_cassandra_115
            "[cassandra.name] drinks deeply at [terri.name]'s gushing well before helping her to her knees."
            wt_image indy_cassandra_116
            cassandra.c "I hope you enjoyed your reward of being allowed to please me.  Clean my fingers off before we go, child, I don't want to get your stickiness on my clothes or our host's furniture."
            wt_image indy_cassandra_117
            terri.c "Yeth, Mithrethh.  Ith make me happy to be able to pleathe you by making sthicky methheth for you."
            change player energy by -energy_very_short notify
        "Watch [terri.name] give [cassandra.name] an orgasm":
            wt_image indy_cassandra_100
            player.c "I'm glad you were able to visit.  I hope you enjoyed the meal.  Instead of dessert, perhaps you'd like [terri.name] to give you an orgasm before you go?"
            wt_image indy_cassandra_101
            cassandra.c "You mean here, with you watching?"
            wt_image indy_cassandra_118
            cassandra.c "I supposed after everything you've done for us, I could let you watch my sub service me.  Come, child, let's get comfortable."
            wt_image indy_cassandra_119
            "[terri.name] removes first her clothes ..."
            wt_image indy_cassandra_120
            "... then [cassandra.name]'s."
            wt_image indy_cassandra_121
            "Then she puts her head between her Mistress' legs ..."
            wt_image indy_cassandra_70
            "... and starts to lick."
            wt_image indy_cassandra_122
            "It seems likely that she's been spending a lot of her time like this ..."
            wt_image indy_cassandra_71
            "... because she seems practised in bring her Mistress to orgasm."
            wt_image indy_cassandra_72
            cassandra.c "AAHHH!!!!"
            wt_image indy_cassandra_123
            "[terri.name] keeps licking, even after [cassandra.name]'s orgasm subsides, until her blonde Mistress instructs her to stop."
            wt_image indy_cassandra_68
            cassandra.c "You can stop now, child.  One orgasm is enough for today.  It's time for us to get dressed and head home.  Thank me for allowing you to please me."
            terri.c "Thank you, Mistress..."
            wt_image indy_cassandra_88
            terri.c "... and thank you, [terri.your_respect_name], for inviting us over, and especially for introducing me to Mistress."
            change player energy by -energy_very_short notify
        "Watch [cassandra.name] and [terri.name] have sex":
            wt_image indy_cassandra_124
            player.c "Before you go, how about you and [terri.name] put on a show for me?"
            wt_image indy_cassandra_102
            cassandra.c "Hmmm.  I don't suppose you mean a puppet show?  We could do a ventriloquism act where I put words in [terri.name]'s mouth?"
            wt_image indy_cassandra_80
            cassandra.c "Since it's you, and considering what you've done for us, okay.  We'll put on a show for you, and I'll put something else in [terri.name]'s mouth besides words."
            wt_image indy_cassandra_125
            cassandra.c "Go to the car, child, and get my bag out of the trunk.  There's something in there we can use to amuse our host, and the two of us, while we're at it."
            wt_image indy_cassandra_126
            "That 'something' turns out to be a double-headed dildo ..."
            wt_image indy_cassandra_127
            "... that goes first into [terri.name]'s mouth ..."
            wt_image indy_cassandra_128
            "... then into [terri.name]'s pussy for just a moment ..."
            wt_image indy_cassandra_129
            "... before coming back out so the other end can go into [terri.name]'s mouth."
            wt_image indy_cassandra_130
            "Once both ends have been wetted to [cassandra.name]'s satisfaction ..."
            wt_image indy_cassandra_131
            "... she re-inserts the dildo into [terri.name]'s sex ..."
            wt_image indy_cassandra_132
            "... mounts the other end herself ..."
            wt_image indy_cassandra_133
            "... and pushes back until the sex toy is deeply embedded into each of them."
            wt_image indy_cassandra_134
            "Then she very carefully turns herself and [terri.name] onto their backs ..."
            wt_image indy_cassandra_135
            "... making sure not to dislodge the dildo connecting them."
            wt_image indy_cassandra_136
            "[cassandra.name] begins to fuck herself and [terri.name] ..."
            wt_image indy_cassandra_137
            "... while [terri.name] worships her Mistress' feet."
            wt_image indy_cassandra_138
            "Other than sucking on her Domme's toes, [terri.name] just lies there while [cassandra.name] fucks them both ..."
            wt_image indy_cassandra_139
            "... but that proves to be sufficient stimulation for [cassandra.name]."
            wt_image indy_cassandra_140
            cassandra.c "AAHHH!!!!"
            wt_image indy_cassandra_141
            cassandra.c "You need to cum for me, child.  I want to watch you make a sticky mess on the other end of my sex toy."
            wt_image indy_cassandra_142
            "Since she's doing it to please her Mistress, and not because of any 'wrong' feelings she may be having, [terri.name] seems willing to allow her body to comply."
            wt_image indy_cassandra_143
            terri.c "Oooohhhhhhhh!!"
            wt_image indy_cassandra_144
            cassandra.c "Good girl.  Clean up the messes you and I made on my sex toy, then pack it back into my bag and get yourself dressed, it's time to go home.  We put on enough of a show to entertain our host, I think."
            change player energy by -energy_very_short notify
        "Receive a blow job from [terri.name]":
            wt_image indy_cassandra_79
            player.c "Before you go, how about you have [terri.name] blow me?"
            wt_image indy_cassandra_78
            cassandra.c "Hmmm, normally I wouldn't lend her out without asking for something in return, but considering all you've done for us, I suppose blowing you is the least she could do."
            wt_image indy_cassandra_81
            cassandra.c "[terri.name], get on your knees and thank our host for your training and the lovely meal."
            wt_image indy_cassandra_182
            terri.c "Yes, Mistress."
            wt_image indy_cassandra_183
            "While you and [cassandra.name] continue to talk, [terri.name] gets between your knees and looks after your hard-on."
            wt_image indy_cassandra_184
            "She's no more talented at fellatio now than she was when you trained her, which is hardly surprising as [cassandra.name] is unlikely to have given her many opportunities to practise, at least not on a real penis."
            wt_image indy_cassandra_185
            "She keeps at it, though, while you and her Mistress discuss her, the weather, politics, and how frequently a good sub should receive reinforcement punishments, a topic she clearly has an opinion on, but obediently keeps silent about."
            wt_image indy_cassandra_186
            cassandra.c "He looks to be getting close, child.  Suckle his balls while he decides where he wants to cum."
            wt_image indy_cassandra_187
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image indy_cassandra_184
                    player.c "[player.orgasm_text]"
                    cassandra.c "Swallow it all, child."
                    wt_image indy_cassandra_188
                    "[terri.name] dutifully shows off an empty mouth, then she and her Mistress depart."
                    $ terri.swallow_count += 1
                "On her":
                    wt_image indy_cassandra_189
                    player.c "[player.orgasm_text]"
                    wt_image indy_cassandra_190
                    cassandra.c "Good, girl.  It looks like he enjoyed that.  Clean yourself up, now, and we'll get going."
                    $ terri.facial_count += 1
            wt_image indy_cassandra_146
            cassandra.c "Thanks again for the lovely meal.  Come, child, he's not the only one who wants your mouth for an after-dinner treat.  You can lick me out in the car on our drive home."
            $ terri.blowjob_count += 1
            orgasm notify
        "Submit to [cassandra.name]" if not cassandra.has_tag('you_never_submit_to_her'):
            $ cassandra.temporary_count = 0
            wt_image indy_cassandra_101
            cassandra.c "You know I'm not into boys.  I've tried it, but I'm past that stage."
            wt_image indy_cassandra_102
            cassandra.c "On the other hand, you have done a lot for [terri.name] and I.  What do you think, child?"
            wt_image indy_cassandra_145
            terri.c "I'd love to watch him serve you, Mistress."
            wt_image indy_cassandra_80
            cassandra.c "Well, she sounds eager.  Let's find out if you're equally eager.  You'll be naked, on your knees.  You'll call me 'Mistress'.  You'll worship my feet.  If I approve of the job you're doing, I may let you worship other body parts.  Do you agree?"
            $ title = "Do you agree to submit to her?"
            menu:
                "Yes, Mistress":
                    wt_image indy_cassandra_1
                    "The statuesque blonde towers over you as you remove your clothes and kneel at her feet."
                    wt_image indy_cassandra_147
                    cassandra.c "Mouth on feet, now."
                    wt_image indy_cassandra_148
                    "Naked in front of the two women, you worship [cassandra.name]'s feet while [terri.name] watches, first kissing and licking her toes ..."
                    wt_image indy_cassandra_149
                    "... then her heels and the heels and soles of her shoes as she turns around."
                    wt_image indy_cassandra_150
                    cassandra.c "What do you think, child?  Is he doing a good enough job he should be allowed to continue?"
                    wt_image indy_cassandra_151
                    terri.c "Yes, Mistress.  He looks like he's being a very good boy."
                    wt_image indy_cassandra_152
                    cassandra.c "Don't let her compliment go to your head.  She probably just wants to see me naked, something she still can't bring herself to admit that she wants or ask for directly."
                    wt_image indy_cassandra_153
                    cassandra.c "You, on the other hand, can presumably admit that you want to worship my ass."
                    $ title = "What do you say?"
                    menu:
                        "I want to worship your ass, Mistress":
                            wt_image indy_cassandra_154
                            cassandra.c "Then get your mouth up here and do so.  Child, come here and kiss me while he's worshipping me."
                            wt_image indy_cassandra_155
                            "You can hear the two women kissing as you bury your nose between the Domme's buttcheeks and use your lips and tongue to worship the soft skin of her buttocks."
                            wt_image indy_cassandra_94
                            cassandra.c "That's enough of that for now, both of you."
                            wt_image indy_cassandra_156
                            cassandra.c "Are you going to be jealous when I let him worship my boobs, child?"
                            wt_image indy_cassandra_157
                            terri.c "Yes, Mistress, but I need to share Mistress and not get jealous when she wants to be with someone else.  And besides, he's being such a good boy, he deserves an opportunity to nurse."
                            wt_image indy_cassandra_158
                            $ title = "What do you do?"
                            menu:
                                "Ask for permission to nurse":
                                    wt_image indy_cassandra_161
                                    cassandra.c "How did I end up with such needy subs?  Okay, if you need to nurse, you can."
                                    wt_image indy_cassandra_162
                                    "She gets her nipples ready for you and then you latch on ..."
                                    wt_image indy_cassandra_163
                                    "... suckling on the blonde Domme's giant teat, which [terri.name] holds steady for you, no doubt wishing that she was the one getting to nurse, rather than you."
                                "Worship her tits":
                                    wt_image indy_cassandra_160
                                    "You don't need to suckle at her teat like a baby, the way [terri.name] does.  You're happy to bury your face between her massive mounds and kiss and lick her soft boob-flesh."
                                "Stop there (ends session)":
                                    $ cassandra.temporary_count = 1
                                    wt_image indy_cassandra_159
                                    player.c "I've enjoyed submitting to you, Mistress, but [terri.name] probably wants access to your breasts more than I do."
                                    wt_image indy_cassandra_67
                                    "You're right, and while she doesn't say anything, [cassandra.name] prefers having [terri.name] nurse on her over you, too."
                                    wt_image indy_cassandra_9
                                    "After they have a little fun, they head out, leaving you to continue your day."
                            # session continues
                            if cassandra.temporary_count == 0:
                                wt_image indy_cassandra_8
                                cassandra.c "That's enough time on my boobs.  Remember your place, on the floor, worshipping my feet."
                                wt_image indy_cassandra_164
                                "You kiss and suck on her beautiful toes and feet ..."
                                wt_image indy_cassandra_165
                                "... licking into the crack between each toe and along her fragrant soles, still slightly sweaty from her shoes ..."
                                wt_image indy_cassandra_166
                                "... until she spreads her legs."
                                wt_image indy_cassandra_167
                                cassandra.c "You can make me cum, now."
                                $ title = "What do you do?"
                                menu:
                                    "Make her cum":
                                        wt_image indy_cassandra_168
                                        "She may not be into boys, but she is into being served by submissives, and her sexy pussy is already slick with desire even before you run your tongue up and down her slit ..."
                                        wt_image indy_cassandra_169
                                        "... and nibble her throbbing clit, bring her to orgasm."
                                        wt_image indy_cassandra_170
                                        cassandra.c "AAHHH!!!!"
                                        wt_image indy_cassandra_171
                                        cassandra.c "That was nice.  Not as nice as a girl would have been, but still nice.  Did you enjoy watching that, child."
                                        wt_image indy_cassandra_172
                                        terri.c "Yes, Mistress.  It makes me happy, watching you enjoy yourself.  I think my former trainer enjoyed himself, too, and that also makes me happy."
                                        $ title = "Now what?"
                                        menu:
                                            "Get dressed":
                                                wt_image indy_cassandra_146
                                                "As you dress, [cassandra.name] does, too.  Then she and [terri.name] depart, happy with each other and with their visit to you."
                                                change player energy by -energy_short notify
                                            "Ask to pleasure [terri.name], too":
                                                wt_image indy_cassandra_13
                                                terri.c "What?  No, that's not necessary."
                                                wt_image indy_cassandra_152
                                                cassandra.c "But it is a generous offer, and just like you wanted to see him submit to me, I'd like to see him pleasure you.  Take your clothes off and sit on the edge of the bed, legs spread, child."
                                                wt_image indy_cassandra_173
                                                terri.c "Yes, Mistress."
                                                wt_image indy_cassandra_174
                                                cassandra.c "Don't be shy.  There's nothing wrong with letting a boy I approve of lick your pussy.  Take your panties right off so I can see what he's doing in there."
                                                wt_image indy_cassandra_175
                                                cassandra.c "That's better.  I want to see you make a sticky mess, so if you want to please me, you need to cover his face with your juices."
                                                wt_image indy_cassandra_99
                                                terri.c "Yes, Mistress.  I'll try."
                                                wt_image indy_cassandra_176
                                                if terri.pleasure_her_count > 0:
                                                    "You've gone down on [terri.name] before, so you have some idea of the challenge ahead of you."
                                                    wt_image indy_cassandra_177
                                                    "That familiarity, however, doesn't immediately translate into having a plan of how to make the pretty redhead get wet from your touch.  You lick and probe and kiss and nibble, to little effect.  Fortunately, her Domme is there is to lend assistance."
                                                else:
                                                    "You've never gone down on [terri.name] before, so you're somewhat unprepared for the challenge that awaits you."
                                                    wt_image indy_cassandra_177
                                                    "Her anatomy is all perfectly normal, but mentally she struggles to enjoy your touch.  You lick and probe and kiss and nibble, to little effect.  Fortunately, her Domme is there is to lend assistance."
                                                wt_image indy_cassandra_178
                                                cassandra.c "Hold yourself wide open for him, child.  I want a good view of you making a sticky mess on his tongue and face."
                                                wt_image indy_cassandra_179
                                                terri.c "Yes, Mistress.  I'm going to be a good girl and make a mess on him for you."
                                                wt_image indy_cassandra_178
                                                "After a little more attention to her now finally wet pussy, she does just that, flooding your tongue with her cum as she grinds herself forward to smear the rest on your face."
                                                wt_image indy_cassandra_180
                                                terri.c "Oooohhhhhhhh!!"
                                                wt_image indy_cassandra_181
                                                cassandra.c "Well, that was interesting.  I hope you enjoyed your time on your knees.  You're a good sub.  Sorry I'm not interested in taking on a male submissive full time.  Thanks again for the lovely meal.  Hopefully we'll get together again sometime."
                                                change player energy by -energy_short # Note: second deduciton of this, to reflect serving both of them
                                                $ terri.pleasure_her_count += 1
                                                $ terri.orgasm_count += 1
                                        $ cassandra.pleasure_her_count += 1
                                        $ cassandra.orgasm_count += 1
                                    "Refuse":
                                        wt_image indy_cassandra_71
                                        "You may not be interested in tasting [cassandra.name]'s pussy, but [terri.name] certainly is.  She drops down to her knees as soon you get up ..."
                                        wt_image indy_cassandra_70
                                        "... and makes sure that her Domme is not left hanging."
                                        wt_image indy_cassandra_72
                                        cassandra.c "AAHHH!!!!"
                                        wt_image indy_cassandra_68
                                        cassandra.c "Thank you, child.  I'd rather have your mouth between my legs, anyway."
                                        terri.c "Thank you, Mistress."
                                        wt_image indy_cassandra_146
                                        "The two women dress and say their good-byes to you.  They seem very happy together as they leave."
                            else:
                                $ cassandra.temporary_count = 0
                            change player energy by -energy_short notify
                        "I don't want that (ends session)":
                            wt_image indy_cassandra_152
                            cassandra.c "That's fine, I don't really want to be served by a boy, anyway.  Thank you again for dinner, though.  It was lovely.  Let's go, child."
                            wt_image indy_cassandra_13
                            "[terri.name] seems a little disappointed as she leaves.  You get the sense she was looking forward to watching you submit more than [cassandra.name] was."
                            change player energy by -energy_very_short notify
                "Perhaps another time":
                    wt_image indy_cassandra_78
                    cassandra.c "Perhaps.  Thanks again for inviting us over and the lovely meal."
                    wt_image indy_cassandra_146
                    "The two women seem very happy together as they leave."
                "Never (shuts off question)":
                    add tags 'you_never_submit_to_her' to cassandra
                    wt_image indy_cassandra_78
                    cassandra.c "That's fine with me.  You're not my cup of tea, either.  No offense.  Thanks again for inviting us over and the lovely meal."
                    wt_image indy_cassandra_146
                    "The two women seem very happy together as they leave."
        "Nothing else":
            wt_image indy_cassandra_146
            "The two women seem very happy together as they leave."
    call character_location_return(cassandra) from _call_character_location_return_763
    call character_location_return(terri) from _call_character_location_return_764
    wt_image current_location.image
    return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# N/A

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Give Chastity Belt
label give_cb_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Give Dildo
label give_di_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Use Fetch Toy
label use_ft_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Give Jewelry
label give_jwc_cassandra:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Give Lingerie
label give_li_cassandra:
  "You may be able to help her out, but this gift won't do it."
  return

# Give Love Potion
label give_lp_cassandra:
  cassandra.c "No thanks.  I'm not interested in a drink."
  return

# Give Transformation Potion
label give_tp_cassandra:
  cassandra.c "No thanks.  I'm not interested in a drink."
  return

# Give Ring of Secuality
label give_rs_cassandra:
    "If the ring makes heterosexual women appreciate other women, in theory it should make a homosexual woman appreciate men.  In practice, she won't accept a ring from you, so you'll never know."
    return

# Use Water Bowl
label use_wb_cassandra:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_cassandra:
  "She's looking to collar, not be collared."
  return

########### TIMERS ###########
## Common Timers
# Start Day
#label cassandra_start_day: #not needed
#    pass
#    return

# End Day
label cassandra_end_day:
    rem tags 'in_club_now' from cassandra
    call character_location_return(cassandra) from _call_character_location_return_765
    return

# End Week
label cassandra_end_week:
    pass
    return


## Club and Stage Labels

label cassandra_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if cassandra.has_tag('in_club_now'):
            $ cassandra.location = club # returns her to club
    # always in Club if waiting for post-Terri scene
    elif cassandra.independent_encounter_status == 2:
        $ cassandra.location = club
        add tags 'in_club_now' 'gloria_club_talk_possible' to cassandra # opens a dialogue for Gloria
    else:
        $ cassandra.random_number = renpy.random.randint(1, 10)
        if cassandra.random_number > 5:
            $ cassandra.location = club
            add tags 'in_club_now' 'gloria_club_talk_possible' to cassandra # opens a dialogue for Gloria
    return

label cassandra_club_send_home:
    call character_location_return(cassandra) from _call_character_location_return_766 # no other locations can be so only dismissed at end of day, not on club exit
    return


## Club President Wife Content

label cassandra_gloria_club_talk_option:
    if cassandra.independent_encounter_status > 1:
        gloria.c "It's so nice to see her happy for a change. Too bad she won't bring her new girlfriend around. I know some of the other Club members would love to meet her, but [cassandra.name] seems rather possessive of her new toy."
    elif cassandra.has_tag('introduced'):
        gloria.c "I'm not sure what I can tell you? I don't know much about her. I just wish she wouldn't mope so much. People come here for a good time, they don't want to see other people unhappy."
    else:
        gloria.c "That's [cassandra.name]. Nice lady, I suppose. I don't know much about her. I just wish she wouldn't mope so much. People come here for a good time, they don't want to see other people unhappy."
        $ cassandra.change_full_name("", "Cassandra", "") # Domme part doesn't open until you introduce yourself
    return



## Character Specific Timers
# N/A

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
