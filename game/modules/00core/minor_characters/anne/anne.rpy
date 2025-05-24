## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Wife Trainer

# Package Register
register anne_pregame 10 in core as "Anne the Tortured Soul"

label anne_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', 'Anne the Tortured Soul (912)')]

    ## Character Definition
    anne = Person(Character("Tortured Soul", who_color = "#480000", what_color = "480000", window_background = gui.dialogue_background_dark_font_color), "anne", cut_portrait = True, prefix = "", suffix = "", wait_for_message_period = 10, week_available = 20, prospect_min_reputation = 3)

    # Other Characters
    # N/A

    ## Actions
    # Standard Object Actions
    anne.new_message_text = "New Message from the Tortured Soul"
    ## no longer needed under new multiple prospect messages system:
    # living_room.add_action("^ anne.new_message_text", label = anne.short_name + "_follow_up_message", context = '_check_messages', condition = "anne.can_be_interacted and living_room.is_empty and anne.message_follow_up_available")

    # Character Specific Objects
    anne.action_talk = anne.add_action("Talk to her", label="_talk", condition = "anne.can_be_interacted")

    ## Tags
    # Common Character Tags
    anne.add_tags('no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    anne_warehouse = Location ("Warehouse", 'aw', cut_portrait = True, enter_break_labels = ['aw_no_access'], enter_labels = ['aw_enter'], exit_labels = ['aw_exit'])
    anne.location = anne_warehouse
    # anne_warehouse.change_image('ts_location')
    # anne_warehouse.change_portrait('ts_portrait')

    ## Other
    anne.change_status("prospect")

    # Start Day Events
    start_day_labels.append('anne_start_day')

    ########### VARIABLES ###########
    # Common Character Variables (note many are defined in 00-wt-classes.rpy)
    anne.add_stats_with_value('current_message', 'random_number')

    # Character Specific Variables
    anne.add_stats_with_value('next_visit_week', 'hypno_blowjob_count', "hypno_help_count", "hypno_mindfuck_count", 'hypno_swallow_count', "first_session_pain")
    anne.asked_bj_hypno = False
    anne.asked_break_resistance_sex_hypno = False
    anne.asked_clothes = False
    anne.asked_location = False
    anne.asked_name = False
    anne.asked_sex_deal_breaker_hypno = False
    anne.asked_why_doing_this = False
    anne.encouraged_to_get_help = False
    anne.consent_contract = False
    anne.first_message_read = False
    anne.first_session = False
    anne.second_session = False
    anne.third_session = False
    anne.fourth_session = False
    anne.message_follow_up_available = False
  return


# Display Portrait
# CHARACTER: Display Portrait
label anne_update_media:
    $ anne.change_image('ts_2')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label anne_examine:
    if anne.first_session:
        wt_image ts_1
        "A dark-haired woman is waiting for you to talk to her."
    elif anne.second_session or anne.third_session:
        wt_image ts_1
        "[anne.name] is waiting for you to say something."
    else:
        # Need complete once additional content added
        pass
    return

# Talk to Character
label anne_talk:
    if anne.first_session:
        rem tags 'no_hypnosis' from anne # note: this is to allow subsequent test to work properly; it gets added back later
        wt_image ts_1
        $ title = "What do you do?"
        menu menu_anne_first_session:
            "Ask her name" if not anne.asked_name:
                $ anne.asked_name = True
                player.c "What's your name?"
                anne.c "Does it matter?"
                $ title = "Does it matter?"
                menu:
                    "Yes":
                        player.c "Yes, it does."
                        "She hesitates a moment."
                        anne.c "Anne.  My name is Anne."
                        $ anne.name = "Anne"
                        $ anne.suffix = "the Tortured Soul"
                        $ anne.new_message_text = "New Message from Anne the Tortured Soul"

                    "No":
                        player.c "I guess not."

            "Ask why she's doing this" if not anne.asked_why_doing_this:
                $ anne.asked_why_doing_this = True
                player.c "Why are you doing this?"
                anne.c "I don't know.  I just need to."
                player.c "Need to what?"
                anne.c "Need to know what it feels like.  To be tortured.  To suffer pain and know I have no way to make it stop."
                player.c "Does the thought of that excite you?"
                anne.c "Not at all.  It scares me.  Scares me so much I shake and have trouble breathing."
                player.c "Then why?"
                anne.c "It's the planning.  The preparation.  Setting this place up.  Seeking you out.  Getting myself ready to be tortured.  It's hard to explain.  It allows me to - feel.  Feel something."
                player.c "Perhaps you should get help?"
                anne.c "I've had help.  I've seen more psychiatrists than I can count.  Been on more medications and mood boosters than I care to remember.  Tried more self help programs than you could imagine."
                anne.c "And after all that, I've finally figured it out.  I'm not broken.  I'm not wrong.  I'm just me."
                anne.c "I hear news stories of women who've been kidnapped and tortured and I wonder, why her?  Why couldn't that have been me?  Don't bother telling me I'm sick.  I've heard that from professionals."
                anne.c "I'm tired of feeling guilty about who I am.  I accept who I am.  I'm not a danger to anyone.  I'm not a bad person.  I'm kind and generous.  And I've learned to accept what I am and what I need."
                player.c "There are lots of men - and women - who'd be happy to have you."
                anne.c "You're talking about Doms?  I've tried them. I'm not submissive.  I'm certainly not a slave.  I don't want anyone giving me orders.  I won't listen to them.  I don't want to.  This isn't even sexual for me."
                player.c "So find a top then."
                anne.c "I'm not a bottom or a masochist either.  I don't like pain, and I don't like the advance negotiation.  I've tried that, and I've never found a man who was prepared to give me what I want.  I hope you're that man."
                anne.c "I want to be tortured and made to feel things I don't want to feel.  I give you full and complete and informed consent to hurt me in any way you see fit."
                anne.c "My only limit is you can't use me sexually.  If you get off on hurting me, fine, but please just get off from the sounds of my screams.  No gratifying yourself with my body."
                anne.c "I don't want our relationship to be about sex, and I don't want your energy or focus to be on anything other than my suffering."

            "Ask about her clothes" if anne.asked_why_doing_this and not anne.asked_clothes:
                $ anne.asked_clothes = True
                player.c "Why are you dressed like that?  You specified no sex, so why are you showing off your body?"
                anne.c "It makes me feel vulnerable.  Waiting here, alone and exposed, for my torturer to arrive."
                player.c "How long have you been standing here like this, waiting for me to come?"
                anne.c "Quite a while."
                player.c "Are you wet?"
                anne.c "No.  Just scared.  And feeling intensely - alive."

            "Ask about this location" if not anne.asked_location:
                $ anne.asked_location = True
                player.c "What is this place?"
                anne.c "Just a building my family owns.  That I own, now.  I've been modifying it.  Getting it ready.  Waiting for someone to meet me here and give me what I need."
                anne.c "It's completely sound proof. I'm the only one with a key. The security cameras have all been disabled. There's only one camera active. A hidden one, recording to my computer."
                player.c "Why?"
                anne.c "So I can replay what you do to me.  Re-live it, afterwards.  It's recording our conversation, too, in case you're worried I'd use the recording to blackmail you.  I won't."

            "Get started" if anne.asked_why_doing_this:
                $ anne.first_session = False
                player.c "Let's get started."
                wt_image ts_2
                "Her body stiffens and a look of panic crosses her face."
                anne.c "You're going to do it?"
                $ title = "What do you do?"
                menu:
                    "Hypnotize her" if player.can_hypno(anne):
                        call focus_image from _call_focus_image_57
                        player.c "Look at this.  Look at this and listen to me.  Listen to the sound of my voice.  Only my voice now."
                        wt_image ts_3
                        player.c "The only thing you hear, the only thing that matters is the sound of my voice.  Listen to my voice.  Only my voice now."
                        "There's no point in asking her to bare her breasts, as you can see them clearly though her top.  You ask for a show of the rest of her body instead."
                        player.c "Turn around.  You want me to examine your body so I can identify what parts I should torture first."
                        wt_image ts_4
                        "She starts to tremble, but follows your instruction."
                        if not anne.asked_name:
                            $ anne.asked_name = True
                            player.c "Tell me your name."
                            anne.c "Anne.  My name is Anne."
                            $ anne.suffix = "the Tortured Soul"
                            $ anne.full_name = "Anne the Tortured Soul"
                            $ anne.new_message_text = "New Message from Anne the Tortured Soul"
                        $ anne.temporary_count = 1
                        while anne.temporary_count == 1:
                            $ title = "What do you want to do?"
                            menu:
                                "Talk to her like this":
                                    $ anne.temporary_count = 0
                                    call anne_hypno_first_session_talk_to_her_like_this from _call_anne_hypno_first_session_talk_to_her_like_this

                                "Have her face you while you talk":
                                    wt_image ts_3
                                    player.c "Turn around and look at me while we talk, Anne."

                                "Have her blow you while you talk" if not anne.asked_bj_hypno:
                                    $ anne.asked_bj_hypno = True
                                    player.c "We are going to talk and I am going to help you, Anne. You want to thank me for helping you.  You should thank me by bringing me pleasure while we talk."
                                    player.c "Pleasure me while we talk, Anne.  Kneel in front of me and pleasure my cock while we talk, so that you can thank me for helping you."
                                    anne.c "I don't want to have sex with you."
                                    "She seems very firm on this point."

                                "Break her resistance to sex" if anne.asked_bj_hypno and not anne.asked_break_resistance_sex_hypno:
                                    $ anne.asked_break_resistance_sex_hypno = True
                                    player.c "You want me to torture you, Anne."
                                    anne.c "Yes"
                                    player.c "You want me to hurt you and make you suffer."
                                    anne.c "Yes"
                                    player.c "You're asking a lot.  You should be grateful to me for helping you like this.  You should thank me."
                                    anne.c "I'll pay you."
                                    player.c "I want payment in flesh, Anne."
                                    anne.c "I don't want this to be about sex."

                                "Make sex a deal breaker" if anne.asked_break_resistance_sex_hypno and not anne.asked_sex_deal_breaker_hypno:
                                    $ anne.asked_sex_deal_breaker_hypno = True
                                    player.c "Anne, if you don't thank me properly, I'll leave and not give you what you want.  You don't want that Anne.  You want me to stay"
                                    anne.c "Yes, I want you to stay."
                                    player.c "Then come here and thank me for staying."
                                    anne.c "Not with sex."

                                "Look for a way to convince her to blow you" if anne.asked_sex_deal_breaker_hypno:
                                    $ anne.temporary_count = 0
                                    "You look around the room, trying to get a better sense of what's going on in her psyche."
                                    player.c "What's that against the wall?"
                                    anne.c "It's a cage."
                                    player.c "Anne, should you be in that cage?"
                                    "Her voice wavers as she answers."
                                    anne.c "Yes"
                                    player.c "Get in the cage."
                                    wt_image ts_5
                                    "Shakily, she gets on her knees and crawls into the cage.  You close the door behind her."
                                    player.c "You'll stay here until I decide to let you out, Anne."
                                    "She nods."
                                    player.c "Do you like it in the cage?"
                                    anne.c "Yes.  It makes me afraid.  Afraid of the things you're going to do with me."
                                    player.c "You want to stay in that cage, don't you Anne?  You want to feel the dread that comes with anticipating what happens next."
                                    anne.c "Ohhh ... Yesss"
                                    $ title = "What do you want to do?"
                                    menu:
                                        "Talk to her like this":
                                            call anne_hypno_first_session_talk_to_her_like_this from _call_anne_hypno_first_session_talk_to_her_like_this_1

                                        "Take out your cock":
                                            wt_image ts_6
                                            "You offer your cock to Anne through the bars of the cage."
                                            player.c "When my cock gets soft, Anne, I'm going to open this cage and let you out, and this will all come to an end."
                                            player.c "Do you understand, Anne?  If you want to stay in the cage and wait for me to torture you, you need to make sure my cock remains hard."
                                            wt_image ts_7
                                            "She hesitates for a moment, then she leans forward ..."
                                            wt_image ts_8
                                            "... and buries your cock fully in her mouth."
                                            player.c "There.  That's not so bad, Anne.  It feels good to have my cock in your mouth.  You like having my cock in your mouth.  You like keeping my cock hard and happy."
                                            player.c "Keep my cock hard and you'll stay in your cage until I'm ready to torture you."
                                            $ anne.hypno_blowjob_count += 1
                                            $ anne.first_session_pain += 1  # note counts as pain for the fear it causes her later when she realizes you were able to make her do this
                                            call anne_hypno_first_session_talk_to_her_like_this from _call_anne_hypno_first_session_talk_to_her_like_this_2

                                        "Just go, leaving her here":
                                            "You've spent enough time on this crazy woman. She likes it in the cage, so you leave her there. It's not locked, so when the hypnotic trance wears off, she'll be able to get out."
                                            "In the meantime, at least you give her the experience of waiting like a caged beast. And if you're lucky, you'll still have time to do something with your day."
                                            $ anne.change_status("rejected")
                                            call forced_movement(living_room) from _call_forced_movement_107
                        add tags 'hypno_this_session' to anne

                    "Torture her":
                        call anne_first_session_torture from _call_anne_first_session_torture

                    "Leave":
                        player.c "Look at you.  Panicking already and I haven't even touched you.  You say you want this, but I don't think you do.  You're scared."
                        wt_image ts_3
                        anne.c "Her body slumps slightly.  The look on her face is a combination of relief and disappointment."
                        "You head back home while there's still time to do something with your day."
                        $ anne.change_status("rejected")
                        call forced_movement(living_room) from _call_forced_movement_108
                add tags 'no_hypnosis' to anne # this is to keep the standard Hypnosis action from appearing; hypnosis is handled differently for Anne

            "Leave" if anne.asked_why_doing_this:
                player.c "You still haven't found the right man for what you want."
                wt_image ts_3
                anne.c "Her body slumps slightly.  The look on her face is a combination of relief and disappointment."
                "You head back home while there's still time to do something with your day."
                $ anne.change_status("rejected")
                call forced_movement(living_room) from _call_forced_movement_109
    elif anne.second_session:
        rem tags 'no_hypnosis' from anne # temporarily, to allow subsequent test to work correctly
        player.c "What's this on the table?"
        wt_image ts_contract_1
        "She picks up the paper and hands it to you. It's a consent to torture and waiver of legal liability, signed by her and notarized by Janice the Lawyer."
        anne.c "It absolves you of any legal responsibility associated with any harm that might come to me. It also confirms that I've waived any right to withdraw consent once we've started."
        wt_image ts_2
        anne.c "I had it written by a top notch lawyer and she witnessed my signature. She assures me it provides you full protection."
        player.c "Protection from what?"
        anne.c "From playing my game."
        player.c "What game?"
        anne.c "I want you to pick a card.  Just one, at random.  Then you follow the instructions on the card."
        player.c "What's on the cards?"
        anne.c "Things I've written. Things for you to do to me. I've been writing them ever since our last session. Adding new ones, changing my mind and taking some out, going back and modifying others."
        anne.c "You can't imagine how - alive - I've felt these past few weeks. Preparing for this. Getting ready for you to come see me again. Not knowing what card you're going to draw. Not knowing what's about to happen to me."
        $ title = "What do you do?"
        menu menu_anne_second_session_talk:
            "Hypnotize her" if player.can_hypno(anne):
                $ anne.temporary_count = 1
                call focus_image from _call_focus_image_58
                player.c "Look at this.  Look at this and listen to me.  Listen to the sound of my voice.  Only my voice now."
                if anne.hypno_blowjob_count > 0:
                    wt_image ts_2
                    anne.c "Wait!  Stop!!  This is what you did last time, before you put me in the cage.  I remember it from the video."
                    player.c "Yes, and I'm going to put you in the cage again Anne. Listen to my voice, Anne. Only my voice. I am taking control of you, Anne, and you are going to let me."
                    anne.c "No, I just want you to draw a card and do what the card says."
                    if player.hypnosis_level >= 10:
                        call focus_image from _call_focus_image_59
                        player.c "Listen to my voice, Anne. Only my voice. Let everything else slip away. You want to lose control. You want to be helpless. You want to be unable to prevent what happens next."
                        player.c "I am taking away your control, Anne. You will let me have control over you. Let everything else go, Anne. Listen only to my voice.  Listen and obey."
                    else:
                        "You're not a strong enough hypnotist to put her under while she's resisting you."
                        $ anne.temporary_count = 0
                if anne.temporary_count == 1:
                    $ anne.temporary_count = 0
                    wt_image ts_3
                    "She slips into your trance."
                    if anne.hypno_blowjob_count > 0:
                        player.c "Remove your clothes.  Handcuff your hands behind your back, then get in your cage."
                        wt_image ts_51
                        "She has her mouth open to accept your cock before you even get the cage door closed."
                        wt_image ts_8
                        player.c "You remember what happens when my cock goes soft?"
                        "She nods her head, vigorously."
                        player.c "Good. Do a good job of keeping my cock hard while I talk to you, Anne."
                        $ anne.hypno_blowjob_count += 1
                    else:
                        "There's no point in asking her to bare her breasts, as you can see them clearly though her top.  You ask for a show of the rest of her body instead."
                        player.c "Turn around.  You want me to examine your body so I can identify what parts I should torture first."
                        wt_image ts_4
                        "She starts to tremble, but follows your instruction."
                        $ title = "How do you want to talk to her?"
                        menu:
                            "Like this":
                                pass
                            "Have her turn back to face you":
                                player.c "Keep turning.  All the way round to face me again."
                                wt_image ts_3
                        if not anne.asked_name:
                            $ anne.asked_name = True
                            player.c "Tell me your name."
                            anne.c "Anne.  My name is Anne."
                            $ anne.change_full_name("", "Anne", "the Tortured Soul")
                            $ anne.new_message_text = "New Message from Anne the Tortured Soul"
                    $ title = "What do you want to talk to her about?"
                    menu menu_anne_second_session_hypno:
                        "Convince her she doesn't need this" if not anne.has_tag('second_hypno_convince'):
                            add tags 'second_hypno_convince' to anne
                            $ anne.hypno_help_count += 1
                            if anne.hypno_help_count == 1:
                                player.c "Anne, listen to me very carefully. I am your friend. I am here to give you what you need. I know what you need. You don't need to be tortured. You only need the anticipation of torture."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_7
                                anne.c "No.  I need to feel the pain."
                                player.c "You don't want to feel pain."
                                anne.c "No, I don't.  I don't want it.  But I must experience it."
                                player.c "You don't need to experience the pain. The anticipation, the preparation, the dread. It's enough Anne. It's enough for you to feel alive."
                                anne.c "I'm incomplete.  I need to know.  The dread isn't enough."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                "You're not sure if you've done enough, but you can't go further with her on this line today."
                            else:
                                player.c "Anne, listen to me very carefully. I am your friend. I am here to give you what you need. I know what you need."
                                player.c "Remember what I told you before. You don't need to be tortured. You only need the anticipation of torture."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_7
                                anne.c "No.  I need to feel the pain."
                                player.c "You don't need the pain. You need the anticipation of the pain. The time you've spent these past few weeks. Preparing the cards, re-reading the cards, thinking about what will happen to you. That's what you need, Anne."
                                anne.c "Yes, I need that. It makes me feel alive. But I need more. I need to know that it's real. That what I'm preparing for will come true. It needs to be real."
                                player.c "I will make it real for you, Anne. Everything will feel real. The anticipation, the preparation, the dread. It's enough, Anne. It's enough for you to feel alive."
                                anne.c "I ... I don't think it will be the same unless I know the suffering will come."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                "You've taken her as far on this line as you can today. You'll need her to ask you to visit her at least one more time before you can truly help her."
                            jump menu_anne_second_session_hypno

                        "Convince her you're torturing her" if not anne.has_tag('second_hypno_mindfuck'):
                            add tags 'second_hypno_mindfuck' to anne
                            if anne.hypno_blowjob_count > 0:
                                wt_image ts_7
                                "You pull your cock out of her mouth, as you don't want her biting when you convince her she's in pain. Besides, it was straining your ears to understand her while your cock was filling her mouth."
                                "Desperately trying to keep you from getting soft, she licks the head of your cock while you talk."
                            $ anne.hypno_mindfuck_count += 1
                            player.c "I'm going to torture you now, Anne."
                            "She shudders."
                            player.c "Remember our last session together.  Remember the pain."
                            if anne.hypno_mindfuck_count == 1:
                                anne.c "I can't feel it."
                                player.c "Feel it. It hurts. I have you tied up. You can't move. You can't move your arms. You can't move your legs. You're helpless and I'm hurting you. Feel the pain."
                                anne.c "It ... it's not enough.  It's not enough pain."
                                player.c "It's the most pain you've ever felt, Anne."
                                anne.c "Owww!!!  Yes.  Ohhh  ooowwww ooowwww ooowwww!!!!"
                                anne.c "I feel that. I feel the most intense pain I've ever felt. I can bear this pain."
                                anne.c "It's not enough. I want to feel pain that I can't bear. Pain I'd rather die than experience. I haven't felt that much pain. I can't imagine what it feels like to hurt beyond the point of being able to bear it, knowing that you can't make it stop."
                                anne.c "I try and imagine it, but I can't.  I need to know."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                "There are tears in the corners of her eyes.  You've done your best, but you can't go any further with her on this line today."
                            else:
                                anne.c "Ooowwww!!!"
                                player.c "That's right. It hurts. You're suffering. I'm still torturing you, Anne."
                                anne.c "Oowww!!! Oowww!!!  Please ... Stop!"
                                player.c "No. I won't stop, Anne. I'm torturing you, and I'm going to keep torturing you until I tire of you."
                                anne.c "OOOOWWWWW!!!!"
                                "Tears are running down her face."
                                anne.c "Please ... please.  I need more."
                                player.c "I'm still torturing you, Anne."
                                anne.c "OOWWWW!!!! I know!! But I can tolerate this pain. I want it to go away. I don't want to be feeling it, but I know it will stop. I know I'll get through it."
                                anne.c "I need more. I need to feel pain I can't bear. I try to imagine what that will be like, but I can't. I need to know."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                "You're close to being able to give her what she needs without causing any actual harm to her body, but she's not quite there yet, and you've done as much as you can on this line for today.  You'll need her to ask you to visit her at least one more time before you can complete the process."
                            jump menu_anne_second_session_hypno

                        "Nothing, end the trance":
                            jump anne_second_session_end_trance
                else:
                    jump menu_anne_second_session_talk

            "Play her game":
                call anne_second_session_play_her_game from _call_anne_second_session_play_her_game

            "Leave":
                player.c "I'm not playing your sick game."
                wt_image ts_1
                "Her body slumps slightly. The look on her face is a combination of relief and disappointment."
                call forced_movement(living_room) from _call_forced_movement_110
                "You head back home while there may still be time to do something with your day."
                $ anne.change_status("rejected")
                change player energy by -energy_very_short notify
    elif anne.third_session:
        rem tags 'no_hypnosis' from anne # temporarily, to allow subsequent test to work correctly
        wt_image ts_1
        player.c "You have your cards again, I see.  The same ones?"
        anne.c "Nobody knows that I'm here.  Nobody knows that I contacted you."
        player.c "What are you talking about?"
        anne.c "I deleted all records of having contacted you, and the videos of our prior sessions.  Destroyed the computer even.  I'm not taping today's session."
        player.c "That's not the same deck, is it?"
        anne.c "I sold my house. I bought a train ticket to the coast. I got on the train yesterday, got my ticket stamped, then jumped off before it left. The taxes on this building are paid for the next 5 years.  No one will come in here for at least that long."
        player.c "Tell me what's in the deck."
        anne.c "I haven't told anyone I'm here, but I did leave encrypted instructions with Janice the Lawyer. I've covered my tracks well, but if for some reason the police question you, the password is 'Tortured Soul'."
        player.c "Tell me what's in the deck!"
        anne.c "I've left instructions and enough money for her firm to represent you. She'll keep you safe.  Just give her the password, if you need to."
        wt_image ts_2
        "You grab for the deck of cards and she moves to block you."
        anne.c "No!  You can't look."
        "The cards spill over.  Staring at you are the cards that fell face up ... Bleed me to death ... Dissolve me with acid ... Bury me alive"
        "A constant theme runs through them: none of them are a quick death. For all them, she'd know she was dying, be able to struggle against it - struggle, and fail."
        wt_image ts_1
        "She gathers up the cards and re-sorts them into a deck."
        anne.c "You can't look.  You need to pick one at random."
        player.c "Why? Is there an out card?  Do any of those cards end with you walking out of here?"
        anne.c "No. But you can't choose. If you do, you may pick an easy death, to be kind to me."
        anne.c "Some of them ... some of them are very cruel deaths. I need to know that there's a chance they could be chosen, a chance that that could be my fate."
        player.c "Why?  What does it matter?  If you want to die, why does the way you die matter?"
        anne.c "I don't want to die. I'm ... I've been more scared these past few weeks than I've ever been. I've cried myself to sleep each night. These past few nights, I haven't even been able to sleep. I'm so scared now I can barely breath."
        player.c "Then why?  Are you dying of something?"
        anne.c "No. I'm perfectly healthy. And I'm perfectly sane, no matter what you think. I had a loving family, a good life. Nice boyfriends. Wealth. Everything anyone could want."
        anne.c "But its only been these past few weeks that I've truly felt alive. Planning this, getting ready for what's going to happen. It's what I've needed my whole life."
        anne.c "No one is going to miss me. My parents were old when they had me. They both died peacefully of old age. I have no brothers or sisters, no children of my own. I`m not hurting anyone by doing this."
        anne.c "It hasn't been easy to track down the right number, but over there is your payment, in cash. A typical fee for an executioner, as best I can tell. A little on the high side, maybe, but I didn't want to cheat you."
        anne.c "Please. Draw a card. Do what it says. Please, do this for me."
        $ title = "What do you do?"
        menu menu_anne_third_session_talk:
            "Hypnotize her" if player.can_hypno(anne):
                $ anne.temporary_count = 1
                call focus_image from _call_focus_image_60
                player.c "Look at this.  Look at this and listen to me.  Listen to the sound of my voice.  Only my voice now."
                if anne.hypno_count > 0:
                    anne.c "No.  Don't do that.  You've done that before.  I don't want that, whatever it is."
                    if player.hypnosis_level >= 10:
                        call focus_image from _call_focus_image_61
                        player.c "Listen to my voice, Anne. Only my voice. Let everything else slip away. You want to lose control. You want to be helpless. You want to be unable to prevent what happens next."
                        player.c "I am taking away your control, Anne. You will let me have control over you. Let everything else go, Anne. Listen only to my voice.  Listen and obey."
                    else:
                        "You're not a strong enough hypnotist to put her under while she's resisting you."
                        $ anne.temporary_count = 0
                if anne.temporary_count == 1:
                    wt_image ts_3
                    "She slips into your trance."
                    if anne.hypno_blowjob_count > 0:
                        player.c "Remove your clothes.  Handcuff your hands behind your back, then get in your cage."
                        wt_image ts_51
                        "She has her mouth open to accept your cock before you even get the cage door closed."
                        wt_image ts_8
                        "With no hesitation, she plunges your cock into her mouth."
                        $ anne.hypno_blowjob_count += 1
                    else:
                        "There's no point in asking her to bare her breasts, as you can see them clearly though her top."
                    $ title = "What do you want to talk to her about?"
                    menu menu_anne_third_session_hypno:
                        "Convince her she doesn't need this" if not anne.has_tag('third_hypno_convince'):
                            add tags 'third_hypno_convince' to anne
                            $ anne.hypno_help_count += 1
                            player.c "Anne, listen to me very carefully. I am your friend. I am here to give you what you need. I know what you need."
                            if anne.hypno_help_count < 3:
                                player.c "You don't need to die.  You only need the anticipation of dying."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_7
                                anne.c "No.  I need to feel what death is like."
                                player.c "You don't want to die."
                                anne.c "No, I don't. I don't want it. But I must experience it."
                                player.c "You don't need to experience actual death. The anticipation, the preparation, the dread. It's enough Anne. It's enough for you to feel alive."
                                anne.c "I'm incomplete. I need to know. The dread isn't enough."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                player.c "You can't get any further with her."
                            else:
                                player.c "Remember what I told you before. You don't need to go through with these things you dread. You only need the anticipation of them."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_7
                                anne.c "No. I need to feel what it's like to die."
                                player.c "You don't need the death. You need the anticipation of dying. The time you've spent these past few weeks. Preparing the cards, re-reading the cards, thinking about what will happen to you. That's what you need, Anne."
                                anne.c "Yes, I need that. It makes me feel alive. But I need more. I need to know that it's real. That what I'm preparing for will happen. It needs to be real."
                                player.c "I will make it real for you, Anne. Everything will feel real. The anticipation, the preparation, the dread. It's enough, Anne. It's enough for you to feel alive."
                                anne.c "I ... I don't think it will be the same unless I know that actual death will follow."
                                wt_image ts_8
                                "You'll need to convince her she's experiencing death."
                            jump menu_anne_third_session_hypno
                        "Mindfuck her" if not anne.has_tag('third_hypno_mindfuck'):
                            add tags 'third_hypno_mindfuck' to anne
                            $ anne.hypno_mindfuck_count += 1
                            if anne.hypno_blowjob_count > 0:
                                wt_image ts_7
                                "You pull your cock out of her mouth.  Desperately she leans forward, trying to lick you."
                                anne.c "No! I need to keep you hard."
                                player.c "It doesn't matter now.  Get out."
                            wt_image ts_111
                            player.c "I'm going to kill you now, Anne."
                            "She breaks into tears, but makes no move to run or defend herself."
                            wt_image ts_112
                            "You pick up a rope and step behind her. Then you wrap the rope around her neck."
                            player.c "I'm suffocating you, Anne. The rope is biting into your neck, cutting off all access to air. You can no longer breathe."
                            player.c "Feel the rope biting into your skin. The pain as it constricts your windpipe. The panic as your lungs fight for air that won't come."
                            wt_image ts_113
                            if anne.hypno_mindfuck_count > 2:
                                call anne_third_session_mindfuck_success from _call_anne_third_session_mindfuck_success
                            elif anne.hypno_mindfuck_count >1 and player.hypnosis_level > 10:
                                call anne_third_session_mindfuck_success from _call_anne_third_session_mindfuck_success_1
                            else:
                                anne.c "I can't feel it. I feel the rope but not the pain. I can still breathe."
                                player.c "Feel it. It hurts. The rope is pulled tight around your neck. Feel the pain."
                                anne.c "Yes ... I feel the pain.  Owwww  .. it hurts!"
                                player.c "With the pain comes panic. You can't breathe. Your access to air has stopped. You're suffocating, Anne. The rope is choking the life out of you."
                                anne.c "Owww!!!  I feel the pain. But I can still breathe."
                                if anne.hypno_blowjob_count > 0:
                                    wt_image ts_8
                                "You've done your best, but her mind isn't prepared to accept that she's being suffocated without actually suffocating her."
                                jump menu_anne_third_session_hypno
                        "End the trance":
                            call anne_third_session_end_trance from _call_anne_third_session_end_trance
                else:
                    jump menu_anne_third_session_talk
            "Play her game":
                jump menu_anne_third_session_play_her_game
            "Encourage her to get help" if not anne.encouraged_to_get_help:
                $ anne.encouraged_to_get_help = True
                player.c "You need to get help. You need to talk to someone about this. You can't throw your whole life away on a fantasy."
                if anne.asked_why_doing_this:
                    anne.c "I've already told you. I've had help. I'm not broken. I'm not wrong. I'm just me."
                else:
                    anne.c "I've had help. I've seen more psychiatrists than I can count. Been on more medications and mood boosters than I care to remember. Tried more self help programs than you could imagine."
                    anne.c "And after all that, I've finally figured it out. I'm not broken. I'm not wrong. I'm just me."
                    anne.c "I hear news stories of women who've been kidnapped and tortured and killed and I wonder, why her? Why couldn't that have been me?  Don't bother telling me I'm sick. I've heard that from professionals."
                    anne.c "I'm tired of feeling guilty about who I am. I accept who I am. I'm not a danger to anyone. I'm not a bad person. I'm kind and generous. And I've learned to accept what I am and what I need."
                anne.c "These last few weeks, after spending time with you ... it's the life I've always wanted. The life I feared I would never have. Now I need you to help me take the last journey of that life."
                jump menu_anne_third_session_talk
            "Leave" if not anne.has_tag('threatened_to_leave'):
                add tags 'threatened_to_leave' to anne
                player.c "I'm not playing your sick games anymore.  This is insane!"
                wt_image ts_2
                anne.c "If you don't, I'll find someone who will!"
                anne.c "I don't want to find someone else. I want it to be you. These last few weeks ... they've been the best weeks of my life. You've made this possible."
                anne.c "Please. It's the last stage of my journey. I want you to be the one to finish it for me. I want your face to be the last one I see."
                anne.c "Please?"
                "Is this a form of love? Is she really appealing to you to kill her because of her affection for you?"
                jump menu_anne_third_session_talk
            "Just go" if anne.has_tag('threatened_to_leave'):
                "Maybe she'll find someone else to execute her. Maybe she won't. Either way, you won't have her blood on your hands."
                "You go home, leaving her alone with her twisted desires."
                $ anne.change_status("rejected")
                call anne_third_session_end from _call_anne_third_session_end
    return

label anne_hypno_first_session_talk_to_her_like_this:
    $ anne.temporary_count = 1
    while anne.temporary_count == 1:
        $ title = "What do you want to talk to her about?"
        menu:
            "Convince her she doesn't need this" if anne.hypno_help_count == 0:
                player.c "Anne, listen to me very carefully.  I am your friend.  I'm here to give you what you need.  I know what you need."
                player.c "You don't need to be tortured, Anne.  You only need the anticipation of torture."
                if anne.hypno_blowjob_count > 0:
                    wt_image ts_7
                anne.c "No.  I need to feel the pain."
                player.c "You don't want to feel pain."
                anne.c "No, I don't.  I don't want it.  But I need to experience it."
                player.c "You don't need to experience the pain.  The anticipation, the preparation, the dread.  It's enough Anne.  It's enough for you to feel alive."
                anne.c "I'm incomplete.  I need to know.  The dread isn't enough."
                if anne.hypno_blowjob_count > 0:
                    wt_image ts_8
                "You're not sure if you've done enough, but you can't go further with her on this line today."
                $ anne.hypno_help_count += 1

            "Convince her you're torturing her" if anne.hypno_mindfuck_count == 0:
                if anne.hypno_blowjob_count > 0:
                    wt_image ts_7
                    "You pull your cock out of her mouth. You don't want her biting you if she really gets into it."
                    "Besides, it was straining your ears to understand her while your cock was filling her mouth."
                    "Still trying to keep you from getting soft, she licks the head of your cock while you talk."
                player.c "Tell me what you fear, Anne.  Tell me what you're afraid I'll do with you."
                player.c "Everything you tell me, Anne, you will feel.  You'll feel it, because everything you say to me, I'm doing.  Every torture you describe, I do that to you."
                anne.c "I want to be tied up."
                player.c "I'm tying you up."
                anne.c "I want to be helpless and unable to move."
                player.c "Your arms and legs are bound.  You can't move them, no matter how much you try."
                anne.c "Oh!  I want to be whipped."
                player.c "I have the whip in my hand.  It's striking you, cutting into your flesh."
                anne.c "I can't feel it."
                player.c "Feel it.  It hurts.  Feel the pain."
                anne.c "It ... it's not enough.  It's not enough pain."
                player.c "It's the most pain you've ever felt, Anne.  The leather of the whip cutting into your soft skin.  It cuts.  It burns."
                anne.c "Yes. I feel that. I feel the most intense pain I've ever felt."
                anne.c "I can bear this pain. It's not enough. I want to feel pain I can't bear. Pain I'd rather die than experience."
                anne.c "I haven't felt that much pain.  I can't imagine what it feels like to hurt beyond the point of being able to bear it, knowing that you can't make it stop."
                anne.c "I try and imagine it, but I can't.  I need to know."
                if anne.hypno_blowjob_count > 0:
                    wt_image ts_8
                "There are tears in the corners of her eyes.  You've done your best, but you can't go any further with her on this line today."
                $ anne.hypno_mindfuck_count += 1
                $ anne.first_session_pain += 1

            "End the trance":
                $ anne.temporary_count = 0
                if anne.hypno_blowjob_count > 0:
                    $ title = "Cum in her mouth before you go?"
                    menu:
                        "Yes":
                            wt_image ts_7
                            player.c "Are you working hard to keep my cock hard, Anne?"
                            anne.c "Yes"
                            player.c "Work harder"
                            wt_image ts_8
                            "You push yourself fully into her mouth as she does her best to pleasure you.  Eventually, you let yourself go."
                            player.c "[player.orgasm_text]"
                            wt_image ts_9
                            "She swallows your load, then looks up at you, sadly."
                            anne.c "You're going to let me out of the cage now, aren't you?"
                            $ anne.hypno_swallow_count += 1
                            orgasm

                        "No":
                            wt_image ts_6
                            "The oral stimulation was fun, but you've no need to cum right now.  You put your cock back in your pants and bring her out of her trance."
                            anne.c "You're going to let me out of the cage now, aren't you?"
                player.c "You will forget what you and I did here, Anne.  You will remember only that you got what you needed.  You will remember only that I helped you."
                wt_image ts_2
                "You bring her out of the trance.  She looks slightly disoriented."
                anne.c "I ... Thank you.  Thank you for helping me.  Is that all?  Are we done?"
                $ title = "Are you finished with her?"
                menu:
                    "Yes, hopefully the hypnosis was enough":
                        player.c "Yes, we're done.  Surely you don't want to suffer any more today?"
                        anne.c "No, I guess you're right.  What you've done already helped.  I'll get your money."
                        change player money by 50 notify
                        call forced_movement(living_room) from _call_forced_movement_112
                        $ anne.change_status("minor_character")
                        end_day

                    "No, reinforce her experience with at least some actual torture":
                        player.c "No, I think you need to suffer more than that."
                        call anne_first_session_torture from _call_anne_first_session_torture_1
    return

label anne_first_session_torture:
    $ anne.temporary_count = 1
    "You step closer to her."
    anne.c "I'll fight back if I'm not bound. I won't mean to. I just know I won`t be able to let you hurt me without trying to protect myself."
    $ title = "What do you do?"
    menu:
        "Tie her up":
            wt_image ts_10
            "There are ropes conveniently at hand. You bind her arms securely behind her ..."
            wt_image ts_11
            "...  then you push her down on the ground."

        "Rough her up then tie her":
            wt_image ts_145
            "You slap her hard across her left cheek ... *smackkk*"
            wt_image ts_12
            "... then you slap her hard on the right cheek ... *smackkk* ... snapping her head back the other way."
            wt_image ts_13
            "As you move to slap her again, she reaches a hand up instinctively to protect her face.  You reach over her hand and grab her by the hair, pulling her forward and throwing her off balance.  She reaches her hands out towards the ground to steady herself."
            wt_image ts_14
            "As she does, you slap her across the face again, harder than before ... *SMACKKK*"
            anne.c "Owww!!!"
            wt_image ts_15
            "You pull her down onto her knees ..."
            wt_image ts_16
            "... then drag her onto the floor."
            wt_image ts_11
            "There are ropes conveniently at hand, which you use to bind her arms behind her."
            $ anne.first_session_pain += 1
    wt_image ts_cattle_prod_1
    "There's a cattle prod resting against the wall.  It's not hard to guess why it's here."
    $ title = "Use the cattle prod?"
    menu:
        "Yes, use it on her":
            wt_image ts_17
            "You pick up the cattle prod, and circle her.  She trembles, afraid to meet your gaze as you pace steadily around her."
            wt_image ts_18
            "Without warning, you jab it into her bare bottom ... *zzzzzz*"
            anne.c "Aaahhh!!!!"
            wt_image ts_19
            "You wave the cattle prod over her, considering where to use it next."
            anne.c "No.  No, please."
            player.c "Sit up."
            wt_image ts_20
            "She scrambles up to a sitting position, and you zap her on the leg ... *zzzzzzz*"
            anne.c "AAAAHHHH!!!"
            wt_image ts_21
            "You grab her by the hair to steady her as you bring the cattle prod up to her breasts."
            anne.c "No, No, Please!  Stop!!"
            $ title = "What do you do?"
            menu:
                "Stop, she withdrew consent":
                    wt_image ts_22
                    "You let go of her hair and lower the prod."
                    anne.c "What ... What are you doing?"
                    player.c "I'm stopping, just as you asked."
                    anne.c "I ... I don't want you to stop.  I know I'm asking you to stop.  I can't help myself.  I need you to continue, no matter what I say."
                    player.c "I won't continue once you've withdrawn consent."
                    anne.c "Bring me some paper.  I'll sign a contract.  I'll give you written permission to continue, no matter what I say."
                    player.c "Okay, but you need to specify a safe word."
                    wt_image ts_23
                    "You get some paper and write up a contract, confirming that you have her permission to continue regardless of what she says, unless she uses her safe word."
                    "You leave the space blank for her to fill in her safe word.  You untie her long enough for her to complete the contract and sign it, then bind her arms back together."
                    wt_image ts_contract_1
                    "You take a look at what she's written.  Under safe word, she put {nw}"
                    extend '"I waive the right to have any safe word."'
                    wt_image ts_23
                    anne.c "It won't work if I can stop it.  I need to know it will continue until you decide to stop it, not me."
                    $ title = "What do you do?"
                    menu:
                        "Accept her contract":
                            $ anne.consent_contract = True
                            "You fold the contract up and put it in your pocket.  Then you pick up the cattle prod and move closer to her."
                            anne.c "Noooo"
                            player.c "Yes"

                        "End things":
                            player.c "I won't continue without a safe word."
                            anne.c "Okay.  Untie me.  I'll get you your money and you can go."
                            $ anne.first_session_pain == 0
                            change player energy by -energy_short
                            $ anne.temporary_count = 0
                            call anne_first_session_end from _call_anne_first_session_end_5

                "Continue":
                    pass
            if anne.temporary_count == 1:
                wt_image ts_24
                "Pulling her head back by the hair, you touch the prod to her breasts ... *zzzzz* ..."
                "Again, and again, and again ... *zzzzzzz*   *zzzzzzz*   *zzzzzzz*  *zzzzzzz*"
                anne.c "AAHHHH!!!  AAAHHHH!!!!! AAAAAHHH!!!!!!!"
                wt_image ts_25
                "When the screams stop and drools runs out of the side of her mouth, you finally lower the prod."
                "Her face contorted in pain, her body continues to twitch for a few minutes as her brain struggles to deal with the sensation overload you provided."
                $ anne.first_session_pain += 1

        "No, not that":
            pass
    if anne.temporary_count == 1:
        "Looking around, there are two obvious locations to put her: a spanking bench and a suspension beam."
        $ title = "Where do you put her?"
        menu:
            "Beat her over the spanking bench":
                "Her current tie is going to be too restrictive, so you untie her arms."
                wt_image ts_26
                "You use the opportunity to rip her negligee off, then refasten her wrists with handcuffs you find hanging on the wall."
                wt_image ts_27
                "You position her over the bench.  As you do, something catches your eye.  There's some thick rubber hose in the corner."
                "You're not sure how she thought it would be used on her.  It's too short to whip her with it.  Maybe she thought it would make a good gag."
                "After a moment's consideration, you come up with a different idea."
                wt_image ts_28
                "You twist it up into a tight coil and jam one end into her cunt, the other end roughly into her ass."
                anne.c "Ohhh!"
                wt_image ts_29
                "You tie it in place with a rope fitted around her hips, so it can't come out."
                "This may not be sexual for her, but the rough hose stuffed into her nether holes is going to chafe and hurt when she starts moving around.  Which she's about to do, when the beating starts."
                wt_image ts_30
                "You start off spanking her with your bare hand ... *smack*  *smack*  *smack*"
                "You soon have her ass twitching, but it's pretty clear she needs sterner treatment than a spanking."
                "A collection of canes, whips, and floggers are lying on a table.  You pick one up, along with some packing material to fashion into a make shift gag."
                wt_image ts_31
                "As you approach her, you can't help yourself from offering a deal."
                player.c "Suck my cock and maybe I'll go easy on you."
                "She looks at you, then shakes her head."
                player.c "Have it your way."
                wt_image ts_32
                player.c "Since you won't put your mouth to good use, let's take it away.  I want to be able to hear myself think while I beat you, anyway."
                wt_image ts_33
                "The crops and floggers hurt.  A lot.  *thwack*  *thwack*  *thwack*  Soon she's screaming into her gag."
                anne.c "aaaaaahhhhhhh oowowwwww!!!!!"
                wt_image ts_34
                "Eventually, even through her gag you can hear clearly that's she's begging you to stop."
                anne.c "thop ... no mo ... leth me go ... pleathe, you need tho thop"
                $ title = "What do you do?"
                menu:
                    "Stop despite the contract" if anne.consent_contract:
                        wt_image ts_35
                        "You put down the crop, and remove the gag from her mouth."
                        anne.c "Why did you stop?"
                        player.c "Because I'm finished.  You wanted to know what its like to be hurt, to be unable to stop the pain."
                        player.c "Now you know. I beat you until I was tired.  Now I'm letting you go."
                        anne.c "Okay.  Untie me and I'll get your money."
                        change player energy by -energy_long
                        $ anne.temporary_count = 0
                        call anne_first_session_end from _call_anne_first_session_end

                    "Honor the contract" if anne.consent_contract:
                        wt_image ts_36
                        "You take the contract out of your pocket, unfold it, and place it on the ground where she can see it. She starts bawling uncontrollably as you move back behind her."
                        anne.c "mmhhh mmmhhh mmmhhh mmmhhhh"
                        player.c "Yes, Anne.  I'm going to keep hurting you, and you can't stop me.  It's in our contract."

                    "Stop, she withdrew consent" if not anne.consent_contract:
                        wt_image ts_35
                        "You put down the crop, and remove the gag from her mouth."
                        anne.c "What ... What are you doing?"
                        player.c "I'm stopping, just as you asked."
                        anne.c "I ... I don't want you to stop.  I know I'm asking you to stop.  I can't help myself.  I need you to continue, no matter what I say."
                        player.c "I won't continue once you've withdrawn consent."
                        anne.c "Bring me some paper.  I'll sign a contract.  I'll give you written permission to continue, no matter what I say."
                        player.c "Okay, but you need to specify a safe word."
                        "You get some paper and write up a contract, confirming that you have her permission to continue regardless of what she says, unless she uses her safe word."
                        "You leave the space blank for her to fill in her safe word.  You untie her long enough for her to complete the contract and sign it, then bind her arms back together."
                        wt_image ts_contract_1
                        "You take a look at what she's written.  Under safe word, she put {nw}"
                        extend '"I waive the right to have any safe word."'
                        wt_image ts_35
                        anne.c "It won't work if I can stop it.  I need to know it will continue until you decide to stop it, not me."
                        $ title = "What do you do?"
                        menu:
                            "Accept her contract":
                                $ anne.consent_contract = True
                                "You fold the contract up and put it in your pocket.  Then you pick up the gag and bring it back to her mouth."
                                anne.c "Noooo"
                                wt_image ts_36
                                player.c "Yes"

                            "End things":
                                player.c "I won't continue without a safe word."
                                anne.c "Okay.  Untie me.  I'll get you your money and you can go."
                                $ anne.first_session_pain == 0
                                change player energy by -energy_long
                                $ anne.temporary_count = 0
                                call anne_first_session_end from _call_anne_first_session_end_1

                    "Ignore her and continue" if not anne.consent_contract:
                        pass
                if anne.temporary_count == 1:
                    wt_image ts_37
                    "Ignoring her sobs, you position yourself over her and resume torturing her already red bottom."
                    "You use your hands for a while.  When they get sore, you switch back to a crop as she keeps up a steady stream of screams and wails from behind her gag."
                    anne.c "ooooowwwww ooooowwwww ooooowwwww  mmmmhhhhh mmmmhhhhh mmmmhhhh"
                    wt_image ts_38
                    "Eventually the wailing stops, and the only sound escaping her throat is a soft, gentle crying."
                    "She's raw and sore, inside and and out, and your arms are tired from beating her."
                    wt_image ts_39
                    "You unfasten her gag and she looks up at you, trembling."
                    player.c "It's over."
                    wt_image ts_3
                    "You help her get to her feet.  Shakily she dresses and goes and gets your money, handing it over to you silently."
                    player.c "Do you need anything?"
                    "She shakes her head again.  You leave her to recover."
                    $ anne.first_session_pain += 2
                    change player energy by -energy_long
            "Whip her on the suspension beam":
                "You need to untie her arms to fit them to the suspension beam."
                wt_image ts_40
                "You use the opportunity to rip her negligee off, then attach her to the beam.  She left a ball gag sitting out, perhaps as an invitation to hurt her enough to need one."
                "She's going to need one.  You fit it in her mouth, then step back, and pick up a whip."
                wt_image ts_41
                "*thwiippppp*  The first stroke of the whip has her in tears."
                "*thwiippppp*  The second has her screaming into her gag."
                anne.c "aaahhhhhhh aaaahhhhhhhh"
                wt_image ts_42
                "*thwiippppp*  *thwiippppp*  *thwiippppp*"
                "By the fifth stroke, the sounds from behind her gag have changed.  She's no longer screaming, she's pleading, and you can make it out even through her gag."
                anne.c "thop ... no mo ... leth me go ... pleathe you need tho thop"
                $ title = "What do you do?"
                menu:
                    "Stop despite the contract" if anne.consent_contract:
                        wt_image ts_43
                        "You put down the whip, and remove the gag from her mouth."
                        anne.c "Why did you stop?"
                        player.c "Because I'm finished.  You wanted to know what its like to be hurt, to be unable to stop the pain."
                        player.c "Now you know. I beat you until I was tired.  Now I'm letting you go."
                        anne.c "Okay.  Untie me and I'll get your money."
                        $ anne.first_session_pain += 1
                        change player energy by -energy_short
                        $ anne.temporary_count = 0
                        call anne_first_session_end from _call_anne_first_session_end_2

                    "Honor the contract" if anne.consent_contract:
                        wt_image ts_44
                        "You take the contract out of your pocket, unfold it, and place it on the ground where she can see it. She starts bawling uncontrollably as you move back into position to resume the whipping."
                        anne.c "mmhhh mmmhhh mmmhhh mmmhhhh"
                        player.c "Yes, Anne.  I'm going to keep hurting you, and you can't stop me.  It's in our contract."

                    "Stop, she withdrew consent" if not anne.consent_contract:
                        wt_image ts_43
                        "You put down the whip, and remove the gag from her mouth."
                        anne.c "What ... What are you doing?"
                        player.c "I'm stopping, just as you asked."
                        anne.c "I ... I don't want you to stop.  I know I'm asking you to stop.  I can't help myself.  I need you to continue, no matter what I say."
                        player.c "I won't continue once you've withdrawn consent."
                        anne.c "Bring me some paper.  I'll sign a contract.  I'll give you written permission to continue, no matter what I say."
                        player.c "Okay, but you need to specify a safe word."
                        "You get some paper and write up a contract, confirming that you have her permission to continue regardless of what she says, unless she uses her safe word."
                        "You leave the space blank for her to fill in her safe word.  You untie her long enough for her to complete the contract and sign it, then bind her arms back together."
                        wt_image ts_contract_1
                        "You take a look at what she's written.  Under safe word, she put {nw}"
                        extend '"I waive the right to have any safe word."'
                        wt_image ts_43
                        anne.c "It won't work if I can stop it.  I need to know it will continue until you decide to stop it, not me."
                        $ title = "What do you do?"
                        menu:
                            "Accept her contract":
                                $ anne.consent_contract = True
                                "You fold the contract up and put it in your pocket.  Then you pick up the gag and bring it back to her mouth."
                                anne.c "Noooo"
                                wt_image ts_44
                                player.c "Yes"

                            "End things":
                                player.c "I won't continue without a safe word."
                                anne.c "Okay.  Untie me.  I'll get you your money and you can go."
                                $ anne.first_session_pain == 0
                                change player energy by -energy_long
                                $ anne.temporary_count = 0
                                call anne_first_session_end from _call_anne_first_session_end_3

                    "Ignore her and continue" if not anne.consent_contract:
                        pass
                if anne.temporary_count == 1:
                    wt_image ts_45
                    "Ignoring her sobs, you step back and change the angle from which the whip is striking her ... *thwiiipppppp*  *thwiiipppppp*  *thwiiipppppp*"
                    anne.c "aaahhhhhhh aaaahhhhhhhh"
                    wt_image ts_46
                    "Soon she's a slobbery, sobbing pitiful mess."
                    $ title = "End things there?"
                    menu:
                        "Stop now":
                            wt_image ts_44
                            "You move closer to her and she looks up at you, trembling."
                            $ anne.first_session_pain += 2

                        "Keep going":
                            wt_image ts_47
                            "You move to change your angle of approach again, and resume the whipping ... *thwiiippppp*  *thwiiippppp*  *thwiiippppp*"
                            anne.c "aaahhhhhhh aaaahhhhhhhh"
                            wt_image ts_48
                            "Soon her whole body is criss crossed with red welts.  The screams have stopped, replaced by deep, uncontrolled sobbing."
                            anne.c "mmmp  mmmp  mmmp  mmmmpp  mmmp  mmmp  mmmmpp"
                            wt_image ts_49
                            "Her breasts are particularly welted, as they're an easy and accessible target ... *thwiiippppp*  *thwiiippppp*  *thwiiippppp*"
                            wt_image ts_48
                            "After a few more strokes of the whip, even the sobbing stops and her head hangs."
                            player.c "[anne.name], look at me."
                            wt_image ts_50
                            "She raises her head.  Good, she's still conscious, but she's had enough."
                            $ anne.first_session_pain += 3

                    player.c "It's over."
                    wt_image ts_3
                    "You unfasten her and help her get to her feet.  Shakily she dresses and goes and gets your money, handing it over to you silently."
                    player.c "Do you need anything?"
                    "She shakes her head again.  You leave her to recover."
                    change player energy by -energy_long
    if anne.temporary_count == 1:
        call anne_first_session_end from _call_anne_first_session_end_4
    return

label anne_first_session_end:
    $ anne.temporary_count = 0
    $ anne.first_session = False
    change player money by 50 notify
    call character_location_return(anne) from _call_character_location_return_19
    call forced_movement(living_room) from _call_forced_movement_113
    if anne.has_tag('hypno_this_session'):
        # the following deducts energy and tracks that hypnosis happened
        $ anne.hypno_session()
        rem tags 'hypno_this_session' from anne
    if anne.first_session_pain > 2:
        $ anne.second_session = True
        $ anne.next_visit_week = week + 4
        $ anne.change_status("minor_character")
        add tags 'continuing_actions' to anne
        if anne.hypno_blowjob_count > 0:
            wt_image living_room.image
            "When you get home, there's a message from Anne waiting for you."
            anne.c "{i}How did you convince me to blow you?  I had a camera set up to record our session, so I could re-live it afterwards.{/i}"
            anne.c "{i}I don't remember anything about the start of the session.  I don't remember you putting me in the cage.  I don't remember you violating our agreement not to have sex.{/i}"
            anne.c "{i}How did you make me do that?{/i}"
            $ title = "Reply to her?"
            menu:
                "Yes, reply":
                    player.c "{i}I didn't make you do anything.  You wanted to blow me.  You wanted to blow me so I would keep you in the cage and give you what you need.{/i}"
                    player.c "{i}I gave you what you needed, didn't I?  You wanted to be vulnerable and out of control.  You will never be more vulnerable than when you are with me.{/i}"
                    "Her response comes back almost immediately."
                    anne.c "{i}You're right.  I keep re-watching the video, and you didn't rape me.  I didn't want to have sex with you, but you convinced me to do it anyway, and I don't even remember you doing it.{/i}"
                    anne.c "{i}That scares me even more than knowing what you're willing to do to me when I do remember it.{/i}"

                "Ignore her":
                    "You see no reason for further contact with that crazy woman."
                    $ anne.second_session = False
                    $ anne.next_visit_week = 0
                    $ anne.change_status("rejected")
                    rem tags 'continuing_actions' from anne
    else:
        $ anne.change_status("rejected")
    end_day
    return

label anne_second_session_end_trance:
    if anne.hypno_blowjob_count > 0:
        wt_image ts_7
        $ title = "Cum in her mouth before you end the trance?"
        menu:
            "Yes, cum in her mouth before ending the trance":
                wt_image ts_8
                "You push yourself fully into her mouth, then let yourself go."
                player.c "[player.orgasm_text]"
                player.c "Look at me Anne, then swallow my cum."
                wt_image ts_9
                "She swallows your cum, looking up at you sadly."
                anne.c "You're no longer hard.  You letting me go now, aren't you?"
                $ anne.hypno_swallow_count += 1
                orgasm
            "No, put your cock away and end the trance":
                pass
        wt_image ts_3
        "You guide her out of the cage."
    "You will forget what you and I did here, Anne.  You will remember only that you got what you needed.  You will remember only that I helped you."
    wt_image ts_2
    "You bring her out of the trance.  She looks slightly disoriented."
    anne.c "I ... Thank you.  Thank you for helping me.  Is that all?"
    "She looks at the cards."
    anne.c "We haven't played my game yet."
    add tags 'hypno_this_session' 'no_hypnosis' to anne # to keep standard Hypnotize Her action from activating the next time you meet her
    $ title = "Play her game?"
    menu:
        "Yes, draw a card":
            call anne_second_session_play_her_game from _call_anne_second_session_play_her_game_1
        "No, leave":
            player.c "I'm not playing your game.  I've given you what you need."
            anne.c "No. I need you to play the game. Please. I'm not sure what we've been doing. I feel ... different ... but it's not enough."
            "Draw a card for me.  Do whatever it says."
            $ title = "What do you do?"
            menu:
                "Ask for your money":
                    player.c "I've given you as much of my time as you've paid for.  This session is over."
                    "She slumps, deflated and yet relieved."
                    anne.c "Okay.  I'll get you your money."
                    change player money by 50
                    if anne.has_tag('hypno_this_session'):
                        # the following deducts energy and tracks that hypnosis happened
                        $ anne.hypno_session()
                        rem tags 'hypno_this_session' from anne
                    $ anne.second_session = False
                    add tags 'unsatisfied' to anne
                    call forced_movement(living_room) from _call_forced_movement_72
                    change player energy by -energy_very_short notify
                    end_day

                "Play her game":
                    call anne_second_session_play_her_game from _call_anne_second_session_play_her_game_2
    return

label anne_second_session_play_her_game:
    add tags 'no_hypnosis' to anne # to keep standard Hypnotize Her action from activating the next time you meet her
    wt_image ts_1
    "You reach for the cards."
    anne.c "Don't look at them! You need to pick one at random. If you look you may choose one that goes easy on me. Whatever happens to me now, it has to be by chance."
    $ title = "What do you do?"
    menu:
        "Draw a card":
            "[anne.name] looks like she's about to faint as you cut the cards."
            anne.c "Oh gawd!"
            $ title = "Follow the card ?"
            $ anne.random_number = renpy.random.randint(1, 9)
            if anne.random_number < 4:
                menu:
                    "Torture me with electricity":
                        call anne_second_session_electricity from _call_anne_second_session_electricity
                    "Refuse":
                        call anne_second_session_refuse from _call_anne_second_session_refuse
            elif anne.random_number < 7:
                menu:
                    "Tie me to a post and whip my breasts bloody":
                        call anne_second_session_whip from _call_anne_second_session_whip
                    "Refuse":
                        call anne_second_session_refuse from _call_anne_second_session_refuse_1
            else:
                menu:
                    "Torture my tits with wire, a milker, and a metal grate":
                        call anne_second_session_breasts from _call_anne_second_session_breasts
                    "Refuse":
                        call anne_second_session_refuse from _call_anne_second_session_refuse_2
        "Cheat":
            "[anne.name] looks like she's about to faint as you cut the cards."
            anne.c "Oh gawd!"
            "You make it look like you draw one at random, but you actually palm multiple cards. You're able to grab three. You read them while [anne.name] trembles, waiting to hear her fate."
            $ title = "What card do you choose?"
            menu:
                "Torture me with electricity":
                    call anne_second_session_electricity from _call_anne_second_session_electricity_1
                "Tie me to a post and whip my breasts bloody":
                    call anne_second_session_whip from _call_anne_second_session_whip_1
                "Torture my tits with wire, a milker, and a metal grate":
                    call anne_second_session_breasts from _call_anne_second_session_breasts_1
                "Refuse":
                    call anne_second_session_refuse from _call_anne_second_session_refuse_3
    return

label anne_second_session_electricity:
    player.c "It says I'm supposed to torture you with electricity."
    "[anne.name] sounds scared as she explains."
    anne.c "I have a machine set up."
    wt_image ts_2
    "She trembles as she shows it to you."
    anne.c "It's hooked up to the industrial park's electric grid.  It can deliver more voltage than a standard wall plug."
    player.c "That could kill you."
    "She shakes her head."
    anne.c "No. I've been doing a lot of reading and had an expert set it up for me. At the top of the dial, it still won't kill me. Just maybe make me wish I could die."
    player.c "Or really die, if you have a heart defect or other medical condition."
    anne.c "I had a full check up at the doctor three weeks ago, when I was having this built.  I'm healthy. I can tolerate it."
    player.c "Have you tried?"
    anne.c "No.  I've been too much of a wuss to test it."
    player.c "Remove your clothes and sit on the machine."
    wt_image ts_64
    "There's a metal brace for her neck and her head.  As she sits down, you screw them into place, preventing any movement of her head, sideways or back and forth."
    "The rest of the machine holds her other body parts just as securely.  There are bars to hold her torso steady, and metal brackets for her arms and legs."
    "There are four electrical conductors that can be placed anywhere you want.  You put two directly over her breasts, then hold up the other two."
    player.c "These will hurt most if directly on your chest, won't they?"
    "She averts her eyes and is unable to move her head, but you can still perceive an attempt at a nod."
    wt_image ts_65
    "The remaining electrical conduit has one obvious placement.  Its attached to a screw that allows you to raise it into place, until its fully penetrating her."
    "You step back, and reach for the control pad."
    wt_image ts_66
    anne.c "Oh gawd. Please ... Please no! Stop. Stop! I don't want to go through with it!!"
    $ anne.temporary_count = 1
    $ title = "What do you do?"
    menu:
        "Ignore her pleas":
            wt_image ts_67
            "You ignore her. Tears well up as she watches you pick up the controls."
        "Remind her of her contract":
            player.c "That's what the contract you signed with the lawyer is for, isn't it?  So that you can't stop this now, even though you want to."
            player.c "Do you want it to stop?  Have you changed your mind?"
            anne.c "Yes!  Yes, I've changed my mind.  I can't go through with it after all!"
            player.c "Actually, you can go through with it, because you have no way to make it stop."
            wt_image ts_67
            anne.c "Nooooo!!!!"
            "She starts bawling as you pick up the controls."
        "Ignore the contract and stop things":
            $ anne.temporary_count = 0
            wt_image ts_64
            "You step forward and unscrew the bolts binding her head."
            player.c "I don't care what you signed.  I'm not going through with this."
            "Her body slumps slightly.  The look on her face is a combination of relief and disappointment.  You head back home while there may still be time to do something with your day."
            if anne.has_tag('hypno_this_session'):
                # the following deducts energy and tracks that hypnosis happened
                $ anne.hypno_session()
                rem tags 'hypno_this_session' from anne
            call forced_movement(living_room) from _call_forced_movement_82
            $ anne.second_session = False
            $ anne.change_status("rejected")
            change player energy by -energy_very_short notify

    if anne.temporary_count == 1:
        $ anne.temporary_count = 0
        wt_image ts_68
        "At the first shock of electricity, her body jolts and twitches ... *zzzzzzzzzzzttt*"
        anne.c "Aaaawwwww!!!!"
        "Tears run down her face as she screams."
        wt_image ts_69
        "You increase the voltage, and jolt her again ... *zzzzzzzzzzzttt*"
        anne.c "Aaaawwwww!!!!"
        "It has a similar effect, except this time her eyes squeeze shut."
        wt_image ts_70
        "You bump the settings up one more ... *zzzzzzzzzzzttt*"
        anne.c "Aaaawwwww!!!!"
        "This time her head jerks back despite the brackets holding it and her mouth twists into a tight grimace."
        wt_image ts_71
        "You increase the voltage again ... *zzzzzzzzzzzttt*"
        anne.c "AAAAGGHHHH!!!!!!!!"
        "A full throated, primeval scream escapes her."
        wt_image ts_72
        player.c "Have you had enough?"
        "She looks at you, a plea of desperation on her face. She seems unable to form words, only mutter agreement."
        anne.c "Mmmmm  huh"
        $ title = "What now?"
        menu:
            "Stop there, at half voltage":
                wt_image ts_67
                "As you put the control away, she recovers her voice."
                anne.c "Was ... was that maximum voltage?"
                wt_image ts_1
                "She's both relieved and disappointed when she checks the controls and sees that you only took her halfway. She gets your money, and you leave."
                change player money by 50
                if anne.has_tag('hypno_this_session'):
                    # the following deducts energy and tracks that hypnosis happened
                    $ anne.hypno_session()
                    rem tags 'hypno_this_session' from anne
                call forced_movement(living_room) from _call_forced_movement_93
                $ anne.second_session = False
                add tags 'unsatisfied' to anne
                change player energy by -energy_short notify
                end_day

            "Keep going":
                player.c "That's too bad, because we're only half way to maximum voltage. Let's see what this machine you built can really do."
                anne.c "Noooooooo"
                wt_image ts_73
                "Her protest is cut short by the next, higher voltage jolt ... *zzzzzzzzzzzttt*"
                anne.c "AAAAGGHHHH!!!!!!!!"
                wt_image ts_74
                "Again you raise the voltage and zap her ... *zzzzzzzzzzzttt* ... There's no scream this time.  Just a deep throated growl."
                anne.c "mmmmrrrrrrgggghhhhhhh!!!"
                wt_image ts_75
                "She's sobbing uncontrollably now, even between jolts."
                player.c "You'd like it if this were over now, wouldn't you?"
                anne.c "Mmmmm huh!!"
                $ title = "What now?"
                menu:
                    "Stop there, at three quarters voltage":
                        wt_image ts_67
                        "As you put the control away, she recovers her voice."
                        anne.c "Was ... was that maximum voltage?"
                        wt_image ts_1
                        "She's both relieved and disappointed when she checks the controls and sees that you only took her partway. She gets your money, and you leave."
                        change player money by 50
                        if anne.has_tag('hypno_this_session'):
                            # the following deducts energy and tracks that hypnosis happened
                            $ anne.hypno_session()
                            rem tags 'hypno_this_session' from anne
                        call forced_movement(living_room) from _call_forced_movement_111
                        $ anne.second_session = False
                        add tags 'unsatisfied' to anne
                        change player energy by -energy_short notify
                        end_day
                    "Keep going":
                        player.c "It's not."
                        "You send another jolt through her on the next highest setting ... *zzzzzzzzzzzttt*"
                        wt_image ts_76
                        anne.c "mmmmrrrrrrgggghhhhhhh!!!"
                        "She grinds her jaws together tight, and it occurs to you that she could bite her tongue or break a tooth if you're not careful. You put down the controller and step forward, unfastening her head. Through her tears, she manages to squeak out a question."
                        anne.c "Is it over?"
                        $ title = "Is it over?"
                        menu:
                            "Yes, that's enough":
                                wt_image ts_77
                                anne.c "Ohhh thank gawd!!!!  She starts weeping uncontrollably again, her head turned to the side, unable to bring herself to look at you."
                                wt_image ts_2
                                "You give her a few minutes to recover, then unfasten the remaining brackets that hold her in place and help her to her feet. Silently, she brings you your money."
                                player.c "Do you need anything?"
                                wt_image ts_1
                                "She shakes her head no.  You turn to go, when she calls to you."
                                anne.c "Was ... was that maximum voltage?"
                                player.c "That was the maximum voltage you could take without injuring yourself."
                                "She nods.  You leave her alone, to process the experience."
                            "No, protect her mouth and keep going":
                                wt_image ts_77
                                player.c "No, we're just beginning.  Open your mouth."
                                wt_image ts_78
                                "She was the one who bought the dental gag. She's been anticipating this stage. Who knows how many hours she's spent over the past few weeks, picturing the moment when it would need to be used?  With the gag in place, she can't bite down.  You can now finish the job you started."
                                wt_image ts_79
                                "The next jolt hurts, although all that escapes her forced open mouth is another deep groan ... *zzzzzzzzzzzttt*"
                                anne.c "hhhuuugggghhhhh!!!"
                                wt_image ts_80
                                "The jolt after that really hurts ... *zzzzzzzzzzzttt*"
                                anne.c "hhhhhuuuuugggggghhhhhhh!!!"
                                wt_image ts_81
                                "And finally you reach the top setting. You zap her with it ... *zzzzzzzzzzzttt*"
                                anne.c "hhhhhuuuuugggggghhhhhhh!!!"
                                "And then again ... *zzzzzzzzzzzttt*"
                                anne.c "hhhhhuuuuugggggghhhhhhh!!!"
                                "And then an extended blast ... *zzzzzzzzzzzzzzzzzzzzzztttttttttttttt*"
                                "Her body thrashes wildly, her mouth thrown open as if to scream, but no sound escapes."
                                "As you shut off the electricity, the only sound you hear is her soft flesh thrashing against its metal bonds."
                                wt_image ts_82
                                "You wait for her to open her eyes.  Slowly, she forces her lids apart, but she keeps her gaze averted, unable to look at you."
                                player.c "It's over."
                                "You give her a few minutes to recover, then unfasten the brackets that hold her in place and help her to her feet."
                                wt_image ts_2
                                "Silently, she brings you your money."
                                player.c "Do you need anything?"
                                wt_image ts_1
                                "She shakes her head no.  You turn to go, when she calls quietly to you."
                                anne.c "Was ... was that maximum voltage?"
                                player.c "Yes"
                                "She nods.  You leave her alone, to process the experience."
                        call anne_second_session_end from _call_anne_second_session_end
    return

label anne_second_session_whip:
    player.c "It says I'm supposed to tie you to a post and whip your breasts until they bleed."
    wt_image ts_2
    "She nods, sadly."
    anne.c "Just let me change."
    player.c "Why?"
    anne.c "I want to wear the type of underwear I wore when I was younger.  It'll help me remember how vivid this fantasy was when I was a schoolgirl."
    "Her voice partially cracks as she continues, betraying how intensely frightened she is."
    anne.c "The ropes are beside the beam over there. Please make them very secure. I'm going to thrash a lot, so it would be better if I can't move anything."
    wt_image ts_52
    "She pulls on plain white panties and a conservative bra, and meekly lets you truss her up."
    anne.c "You need to secure my head too, so I can't move it."
    wt_image ts_53
    "You place a length of rope in her mouth, loop it twice around the post, and tie it tight, holding her head secure and partially gagging her in the process."
    "Then you wrap another rope around her eyes and tie it to the post, holding her head even more firmly and taking away her sight. Through the rope in her mouth, you can hear her start to panic."
    anne.c "oohhhh oohhhh"
    wt_image ts_54
    "You grab the front of her bra and rip it open, exposing your targets. She starts to shake."
    anne.c "Oh gawd. Please ... Please no! Stop. Stop! I don't want to go through with it!!"
    $ anne.temporary_count = 1
    $ title = "What do you do?"
    menu:
        "Ignore her pleas":
            wt_image ts_56
            "You ignore her and pick up the whip she left carefully coiled in front of the post. Briefly, you wonder whether what she's feeling now is what she imagined she would be feeling when she placed it there."
        "Remind her of her contract":
            player.c "That's what the contract you signed with the lawyer is for, isn't it?  So that you can't stop this now, even though you want to."
            player.c "Do you want it to stop?  Have you changed your mind?"
            anne.c "Yes!  Yes, I've changed my mind.  I can't go through with it after all!"
            player.c "Actually, you can go through with it, because you have no way to make it stop."
            wt_image ts_56
            anne.c "Nooooo!!!!"
            "She starts bawling as you pick up the whip she left carefully coiled in front of the post. Briefly, you wonder whether what she's feeling now is what she imagined she would be feeling when she placed it there."
        "Ignore the contract and stop things":
            $ anne.temporary_count = 0
            wt_image ts_55
            "You step forward and untie her head."
            player.c "I don't care what you signed.  I'm not going through with this."
            "Her body slumps slightly.  The look on her face is a combination of relief and disappointment.  You head back home while there may still be time to do something with your day."
            if anne.has_tag('hypno_this_session'):
                # the following deducts energy and tracks that hypnosis happened
                $ anne.hypno_session()
                rem tags 'hypno_this_session' from anne
            $ anne.change_status("rejected")
            $ anne.second_session = False
            call forced_movement(living_room) from _call_forced_movement_114
            change player energy by -energy_very_short notify

    if anne.temporary_count == 1:
        $ anne.temporary_count = 0
        wt_image ts_57
        "She screams through the rope on the first lash ... *thwaapppppp*"
        anne.c "aaaggghhhh!!!"
        "The screams get louder as you keep whipping her ... *thwaapppppp*"
        anne.c "aaaggghhhh!!!"
        "*thwaapppppp*"
        anne.c "aaaaggghhhhh!!!"
        "*thwaapppppp*"
        anne.c "aaaaaggggghhhhh!!!"
        "*thwaapppppp*"
        wt_image ts_58
        anne.c "aaaaaggggghhhhhh!!!!"
        "*thwaapppppp*"
        anne.c "aaaaaagggggggghhhhhhh!!!"
        "*thwaapppppp"
        anne.c "aaaaggggaaagggaaaggghhhhhh!!!"
        "*thwaapppppp*"
        anne.c "aaagggaaagggaaaaggggaaaaaggghhhhhh!!!"
        wt_image ts_59
        "Then the screams are gone, replaced by a mewling sobbing ... *thwaapppppp*"
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "*thwaapppppp*"
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "*thwaapppppp*"
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "*thwaapppppp*"
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "On the next lash, you draw blood ... *thwaapppppp*"
        wt_image ts_60
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "Perhaps there's some truth to bloodlust, because as you see the blood break the surface of her skin, you lash her again ... *thwaapppppp*"
        wt_image ts_61
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "And then once more ... *thwaapppppp*"
        wt_image ts_62
        anne.c "mmmnnnnn  mmmnnnnn  mmmnnnnn  mmmnnnnn"
        "Finally, you get control of yourself again, and put the whip down."
        wt_image ts_63
        "You untie the ropes from around her eyes."
        player.c "It's over.  Can you hear me?"
        "She nods, weakly."
        player.c "Do you need anything?"
        "She shakes her head, softly. You let her rest in this position for a little while, then you finish untying her and support her as she finds her feet."
        wt_image ts_1
        "Silently, she goes and gets your money, her hands shaking as she passes it to you. You leave her alone to process the experience."
        call anne_second_session_end from _call_anne_second_session_end_1
    return

label anne_second_session_breasts:
    player.c "It says I'm supposed to torture your tits with a wire, milker, and metal grate.  What does that mean?"
    anne.c "I read a story about this scene years ago. It's stayed in my mind. I keep being drawn back to think about it. I had the required equipment built special for it, right over here."
    player.c "This metal contraption?"
    anne.c "That's the first part.  You ..."
    "Her voice falters."
    anne.c "... you put put me in it, to hold me in place so I can't stop what's coming. Then you use that thin wire to whip my tits."
    anne.c "After they're bruised and bloodied, you attach the milker to them. When the milker has pumped them as full as they get, you ..."
    "She chokes up and you're not sure if she can continue.  Then she does."
    anne.c "... you put me on that special table there, with the special metal grate top."
    player.c "And push you down on top of it until it nearly slices your tits open?"
    "She nods."
    player.c "I don't suppose you're supposed to be clothed for this?"
    "She shakes her head no."
    wt_image ts_83
    "Trembling, she removes her clothes and steps over to the metal contraption. Its positioning forces her to lean forward. As she does, you connect the neck bar, preventing her from straightening back up. Then you lock her hands in place behind her back."
    wt_image ts_84
    "The arrangement leaves her breasts hanging and exposed.  It's not hard to see how this focuses all of her attention onto her tits, before you've even touched them."
    player.c "The heroine in your story.  Why is this happening to her?"
    anne.c "Her captor wants her to give him milk, but her milk has dried up. She's no longer lactating. He takes out his frustrations on her tits."
    player.c "Are you lactating?"
    anne.c "No. I've never been pregnant."
    player.c "What happens when you put a milker on dry breasts?"
    wt_image ts_85
    "The words start to choke in her throat."
    anne.c "I'm told its painful."
    wt_image ts_86
    "You pick up the wire resting against the contraption, and touch the cold metal to her breast."
    player.c "As painful as this wire is going to be, do you suppose?"
    anne.c "Oh gawd.  Please ... Please no! Stop. Stop! I don't want to go through with it!!"
    $ anne.temporary_count = 1
    $ title = "What do you do?"
    menu:
        "Ignore her pleas":
            "You ignore her pleas, and bring the wire back ..."
        "Remind her of her contract":
            player.c "That's what the contract you signed with the lawyer is for, isn't it?  So that you can't stop this now, even though you want to."
            player.c "Do you want it to stop?  Have you changed your mind?"
            anne.c "Yes!  Yes, I've changed my mind.  I can't go through with it after all!"
            player.c "Actually, you can go through with it, because you have no way to make it stop."
            wt_image ts_86
            anne.c "Nooooo!!!!"
            "She starts bawling as you bring the wire back ..."
        "Ignore the contract and stop things":
            $ anne.temporary_count = 0
            wt_image ts_87
            "You step forward to unfasten her head."
            player.c "I don't care what you signed.  I'm not going through with this."
            "Her body slumps slightly.  The look on her face is a combination of relief and disappointment.  You head back home while there may still be time to do something with your day."
            if anne.has_tag('hypno_this_session'):
                # the following deducts energy and tracks that hypnosis happened
                $ anne.hypno_session()
                rem tags 'hypno_this_session' from anne
            call forced_movement(living_room) from _call_forced_movement_115
            $ anne.second_session = False
            $ anne.change_status("rejected")
            change player energy by -energy_very_short notify
    if anne.temporary_count == 1:
        $ anne.temporary_count = 0
        wt_image ts_88
        "... then whip it forward ... *wwwhhpppttt*"
        anne.c "AAAGGHHHHH!!!"
        "It hurts, and raises an almost immediate bruise."
        wt_image ts_89
        "Gently you caress the cold metal along her skin, teasing her nipple. It hardens, seemingly oblivious to the discomfort of its owner. Then you lift the wire again ..."
        wt_image ts_90
        "... and whip it forward again ... *wwwhhpppttt*"
        anne.c "AAAGGHHHHH!!!"
        "*wwwhhpppttt*"
        anne.c "AAAAAGGGGHHHHH!!!!!"
        "*wwwhhpppttt*"
        anne.c "oh oh oh oh ohhhh ohhhhhh!!!!"
        wt_image ts_91
        "You've rarely seen anything bring out bruising as quickly as the wire has.  You examine her tits, as [anne.name] moans."
        anne.c "ohhh ohhhhhh"
        "It looks like she's ready for part two."
        player.c "The captor in your story, did he put up with this incipient moaning from the heroine?"
        wt_image ts_87
        "She shakes her head no, but you already knew the answer. There wouldn't be a ring gag lying beside the contraption if she hadn't put it there for you to use on her."
        wt_image ts_92
        player.c "Open up."
        "You lock the ring gag in place behind her head as she sniffles, trying to hold back tears."
        wt_image ts_93
        "You connect the milker to her bruised tits ..."
        wt_image ts_94
        "... then turn on the suction."
        wt_image ts_93
        "The milker begins a steady *whummp whummp whummp whummp* ..."
        wt_image ts_94
        "... steadily ..."
        wt_image ts_93
        "... relentlessly ..."
        wt_image ts_94
        "... trying to suction milk from first one tit ..."
        wt_image ts_95
        "... then the other, back and forth ... *whummp whummp whummp whummp*"
        wt_image ts_96
        "Behind her gag, [anne.name] groans, trying to adjust to the consistent, painful tugs on her tits. It's a losing battle."
        wt_image ts_95
        "*whummp whummp whummp whummp*"
        wt_image ts_96
        anne.c "rrrrrgggghhhhhh!!!"
        "There's no milk to be had, but the milker doesn't know or care. It just keeps pumping ... *whummp whummp whummp whummp*"
        wt_image ts_97
        "... distending her nipples, pulling them deep into the suction cups."
        wt_image ts_98
        player.c "Nothing. Not a single drop of milk. I'm very disappointed in you."
        anne.c "rrrrrgggghhhhhh!!!"
        wt_image ts_99
        "You shut off the milker, take off her ring gag, and disconnect the suction cups. She moans in agony as her nipples are released."
        anne.c "ooooohhhhhhh!!!!"
        wt_image ts_100
        "Her nipples are weeping with fluids pulled forcibly from her breasts through the porous membrane, a counter point to the tears running down her cheek."
        player.c "I think we've established that your tits have no purpose. There's no need to worry about their safety any more, is there?"
        "Her soft moan of a reply isn't meant as agreement, although technically it is."
        anne.c "noooooo"
        wt_image ts_101
        "She's completely placid and defeated as you remove her from the milker and bind her arms together behind her back. To maximize the effect of the next stage, you wrap ropes around her bruised tits, swelling them with blood."
        wt_image ts_102
        "Then you push her forward onto the metal grate. The sharp metal bites into her tender skin, and she struggles to hold her weight back and off of her chest."
        wt_image ts_103
        "At this point, the purpose for the strap and pulley system above the table becomes obvious. You connect her feet to the bar, and lift her legs into the air."
        wt_image ts_106
        anne.c "No!  Noo!  Nooooo!!!!"
        "She struggles to keep the weight off her chest as you lift her legs higher and higher."
        wt_image ts_104
        "It's a losing struggle. Her breasts are soon crushed down onto the metal with the full weight of her body."
        anne.c "AAAAAGGGHHHH!!!!!!"
        wt_image ts_105
        "Now a new struggle begins, as she tries to hold herself steady through the pain, every twitch and movement in her body being transmitted directly through to the metal cutting into her breasts."
        anne.c "NNNNNNNNNNNN"
        $ title = "Feeling sadistic?"
        menu:
            "Yes":
                wt_image ts_104
                "You watch with amusement as she struggles. Then you bring your hand down sharply on her ass ... *smack*."
                wt_image ts_105
                "She jumps as you strike her, the movement transmitting her body weight straight through to her chest."
                wt_image ts_104
                anne.c "Ow!  AAAAGGHHH!!!"
                "*smack*"
                wt_image ts_105
                anne.c "Ow!  AAAAGGHHH!!!"
                wt_image ts_104
                "Eventually she learns to control her movement, letting you hurt her ass more, in order to hurt her tits less ...  *smack*"
                wt_image ts_105
                anne.c "Aaaagghh!!!"
                wt_image ts_104
                "*smack*"
                anne.c "aaagghhhh"
            "No, I'm done":
                pass
        wt_image ts_107
        "You've had your fun, and she's had her fantasy scene fulfilled. You lower her legs and she slumps forward onto the table, her breathing fast and shallow."
        wt_image ts_108
        "She regains her feet, finally relieving her breasts of the pressure of the metal spikes.  She's bleeding slightly on one side ..."
        wt_image ts_109
        "... more so on the other."
        wt_image ts_110
        player.c "It'll take you a while to recover from this."
        anne.c "I know."
        "She nods over towards a dark corner of the warehouse, where a pair of gardening shears and a medical kit sits."
        anne.c "If you'd drawn that card, it would have been much worse."
        "You feel a gnawing sensation in the pit of your stomach."
        player.c "That card?"
        anne.c "Where you cut off my nipples. I'm glad you didn't draw that one."
        "You can't bring yourself to ask what else was in her deck of cards."
        anne.c "Untie me, and I'll get you your money."
        call anne_second_session_end from _call_anne_second_session_end_2
    return

label anne_second_session_refuse:
    player.c "I'm not doing this."
    anne.c "You have to!"
    player.c "No, I don't. I'm not playing your sick game."
    "Her body slumps slightly.  The look on her face is a combination of relief and disappointment.  You head back home while there may still be time to do something with your day."
    if anne.has_tag('hypno_this_session'):
        # the following deducts energy and tracks that hypnosis happened
        $ anne.hypno_session()
        rem tags 'hypno_this_session' from anne
    call forced_movement(living_room) from _call_forced_movement_123
    $ anne.second_session = False
    $ anne.change_status("rejected")
    change player energy by -energy_very_short notify
    return

label anne_second_session_end:
    $ anne.second_session = False
    # shutting off third session
    # if not anne.has_tag('unsatisfied') and not anne.status == 'rejected':
        # $ anne.third_session = True
        # $ anne.next_visit_week = week + 4
    sys "That's all the active content for [anne.full_name] in this version."
    $ anne.change_status("minor_character")
    change player money by 50
    call forced_movement(living_room) from _call_forced_movement_116
    call character_location_return(anne) from _call_character_location_return_20
    if anne.has_tag('hypno_this_session'):
        # the following deducts energy and tracks that hypnosis happened
        $ anne.hypno_session()
        rem tags 'hypno_this_session' from anne
    change player energy by -energy_long notify
    end_day
    return

label anne_third_session_end_trance:
    if anne.hypno_blowjob_count > 0:
        wt_image ts_7
        $ title = "Cum in her mouth before you end the trance?"
        menu:
            "Yes, cum in her mouth before ending the trance":
                wt_image ts_8
                "You push yourself fully into her mouth, then let yourself go."
                player.c "[player.orgasm_text]"
                player.c "Look at me Anne, then swallow my cum."
                wt_image ts_9
                "She swallows your cum, looking up at you sadly."
                anne.c "You're no longer hard.  You letting me go now, aren't you?"
                $ anne.hypno_swallow_count += 1
                orgasm
            "No, put your cock away and end the trance":
                pass
        wt_image ts_3
        "You quide her out of the cage."
    wt_image ts_2
    "You bring her out of the trance.  She looks slightly disoriented."
    wt_image ts_1
    "She looks at the cards."
    anne.c "You haven't picked a card yet."
    add tags 'hypno_this_session' 'no_hypnosis' to anne # to keep standard Hypnotize Her action from activating the next time you meet her
    jump menu_anne_third_session_talk
    return

label anne_third_session_mindfuck_success:
    add tags 'mindfuck_success' to anne
    anne.c "Ow ..."
    player.c "Silence, Anne. You can't make a sound. You try to scream, but there's no air to feed it. The rope is pulled tight around your neck."
    wt_image ts_113
    "Her heads rolls forward and she stops breathing."
    player.c "Your lungs scream for air, but no air comes. Your heart beats madly, erratically, trying to get air to your body, but there's no air for your blood to absorb. The rope has taken it away."
    wt_image ts_114
    player.c "Your throat is crushed and the end is near."
    "She's turning purple and tears stream down her face. Mesmerized by your words, she's still not breathing."
    player.c "Your brain cells are dying. You're feeling faint ... almost euphoric. Sparkles blur your vision ... and then you go blind. Everything is black. Your bowels void and then ... it's over."
    wt_image ts_115
    player.c "You're dead, Anne."
    "She collapses, still not breathing.  You catch her and lay her gently on the ground."
    wt_image ts_116
    "You lean in close and whisper into her ear."
    player.c "Live. You can breathe, Anne."
    "She gulps in a deep breath of air."
    anne.c "Ahhhhhh!"
    wt_image ts_111
    "You remove the rope from her neck and help her sit up.  Her face is stained with tears, and she smells. You guide her away from the pool of urine and feces she's left on the floor."
    anne.c "What happened?  Why I am alive?"
    "She seems to have exited your trance, no doubt the result of the shock of her resurrection."
    player.c "I killed you.  Then I brought you back to life."
    anne.c "Did you draw the 'Garotte me' card?  I don't remember you drawing from the deck."
    player.c "Perhaps dying can affect your memory. But not the memory of dying. You remember that quite vividly, don't you?"
    anne.c "Yes.  But if I died, how could you have brought me back?"
    player.c "It doesn't matter how.  What matters is you wanted to know what death feels like.  Now you do."
    add tags 'hypno_this_session' 'no_hypnosis' to anne # to keep standard Hypnotize Her action from activating the next time you meet her
    $ title = "What now?"
    menu:
        "Offer to help her again when she needs you":
            player.c "You know now what you need, Anne. The dread and anticipation of the preparation. The overwhelming fear of the act."
            player.c "When the hunger comes back  ... when you find yourself writing on your cards ... go with it. Satisfy your morbid need to wallow in the preparation for your own suffering and death."
            player.c "When the preparation is done, come to me. I will make it real. Whatever you write on your cards, it will happen inside your head, indistinguishable from reality itself. And you get to do it all again."
            anne.c "Thank you."
            "You collect your executioner's fees.  500.  Generous payment for one night's work."
            anne.c "I won't be able to afford that much in the future.  Would 100 be okay?"
            "You can live with that."
            sys "Additional content with Anne the Tortured Soul is not yet implemented."
            change player money by 500
            call anne_third_session_end from _call_anne_third_session_end_1
        "Play her game for real":
            player.c "And now that we've played the game my way, it's time to play it your way."
            anne.c "What?"
            player.c "You went through so much trouble to prepare for your death. It would be a shame to waste all that work. You didn't expect to walk out of here alive. I hope my little mindfuck didn't give you false hope?"
            anne.c "Please!  You don't have to anymore."
            player.c "Because now you know what death feels like?"
            anne.c "She nods her head vigorously."
            anne.c "Yes!"
            player.c "I wonder if it will feel the same this time?"
            "You step over to the deck and cut the cards."
            anne.c "Noooo!!"
            $ title = "What do you do?"
            menu:
                "Draw a card at random":
                    call anne_third_session_draw_card from _call_anne_third_session_draw_card
                "Cheat (draw multiple cards)":
                    call anne_third_session_draw_multiple_cards from _call_anne_third_session_draw_multiple_cards
                "Walk away":
                    "You put down the cards."
                    player.c "That completes your mindfuck, Anne. You got to experience death, and then the prospect of another death. Let that be enough. Relive these memories as often as you need, but leave this game behind."
                    "You collect your executioner's fees.  500.  Generous payment for one night's work.  Then you leave her alone with her memories."
                    call anne_third_session_end from _call_anne_third_session_end_2
        "Use a transformation potion" if player.has_item(transformation_potion):
            "You mix the potion with some water and hand it to her."
            player.c "Drink this."
            anne.c "What's in the water?"
            player.c "Possibly its poison, to kill you again. Possibly its medication to complete your return from the dead. Possibly its a transformation potion to convert you into my playtoy."
            player.c "At this point, we should be beyond you questioning me."
            "She brings the water to her lips."
            wt_image ts_117
            "There's no need to spend any energy shaping what the potion does to her. She's been a tortured soul her whole life. The potion races through her, eliminating all other interests, leaving only an all consuming need to suffer."
            player.c "You will come with me.  I will give you pain to last a lifetime."
            "She scrambles after you.  On the way out, you collect your executioner's fees.  500.  Generous payment for one night's work."
            sys "Additional content with Anne the Tortured Soul is not yet implemented."
            $ anne.transformed_via_object = True
            rem 1 transformation_potion from player
            change player money by 500
            call anne_third_session_end from _call_anne_third_session_end_3
        "Use Will-Tamer" if player.has_item(will_tamer) and not anne.has_tag('will_tamer_this_week'):
            add tags 'will_tamer_this_week' to anne
            player.c "Put this on."
            anne.c "What is it?"
            player.c "Possibly its a magic collar, to strangle you to death again. Possibly it helps complete your return from the dead. Possibly it takes away your free will and converts you into my playtoy."
            player.c "At this point, we should be beyond you questioning me."
            "She places the collar around her neck."
            wt_image ts_118
            "If a Will-Tamer can be eager, the Will-Tamer is EAGER to claim Anne. Or perhaps it's Anne's brain that's eager to be claimed by the Will-Tamer?"
            "Normally it takes multiple sessions in the Will-Tamer before it's ready to permanently transform its wearer.  It only takes one session with Anne."
            $ title = "Let the Will-Tamer take her?"
            menu:
                "Yes (Will-Tamer will be used up)":
                    "She's been a tortured soul her whole life. As the Will-Tamer sinks into her skin, becoming one with her psyche, it eliminates all other interests, leaving only an all consuming need to suffer."
                    sys "Additional content with Anne the Tortured Soul is not yet implemented."
                    rem 1 will_tamer from player
                    $ anne.transformed_via_object = True
                    call anne_third_session_end from _call_anne_third_session_end_4
                "No, not yet":
                    wt_image ts_111
                    "Quickly you pull the collar off her before it can claim her."
                    anne.c "What ... what was that?!"
                    player.c "Something you seem to need. I'll let you know when you're allowed to wear it again."
                    anne.c "Please ... please don't make me wait too long??"
                    sys "Additional content with Anne the Tortured Soul is not yet implemented."
            "On the way out, you collect your executioner's fees.  500.  Generous payment for one night's work."
            change player money by 500
            call anne_third_session_end from _call_anne_third_session_end_5
        "Collect your money and go":
            "On the way out, you collect your executioner's fees.  500.  Generous payment for one night's work."
            change player money by 500
            call anne_third_session_end from _call_anne_third_session_end_6
    return

label menu_anne_third_session_play_her_game:
    "You reach for a card."
    wt_image ts_3
    "[anne.name] bursts into tears in anticipation of what comes next."
    $ title = "What do you do?"
    menu:
        "Draw a card at random":
            call anne_third_session_draw_card from _call_anne_third_session_draw_card_1
        "Cheat (draw multiple cards)":
            call anne_third_session_draw_multiple_cards from _call_anne_third_session_draw_multiple_cards_1
        "Walk away":
            "You put down the cards."
            player.c "I'm not doing this."
            wt_image ts_2
            "She nods, her face a mixture of disappointment and relief."
            anne.c "Please ... can you at least pick a card, so I know what it would have been?"
            $ title = "Pick a card for her?"
            menu:
                "Yes, and look at it":
                    "You draw a card and read it:"
                    $ anne.random_number = renpy.random.randint(1, 4)
                    if anne.random_number == 1:
                        extend " Suffocate me with a plastic bag."
                    elif anne.random_number == 2:
                        extend " Skin me alive."
                    elif anne.random_number == 3:
                        extend " Poison me."
                    else:
                        extend " Disembowel me."
                    "You toss the card to her. She sinks to the floor in tears as she reads it. You can guess what she'll be thinking about for the next few days."
                "Yes, but don't look at it":
                    "You pick a card at random and toss it to her. She sinks to the floor in tears as she reads it. You can guess what she'll be thinking about for the next few days."
                "No, just leave":
                    player.c "No.  I'm done with your games."
            "Maybe she'll find someone else to execute her. Maybe she won't. Either way, you won't have her blood on your hands. You go home, leaving her alone with her twisted desires."
            $ anne.change_status("rejected")
            change player energy by -energy_very_short notify
            call anne_third_session_end from _call_anne_third_session_end_7
    return

label anne_third_session_draw_card:
    $ anne.random_number = renpy.random.randint(1, 10)
    if anne.random_number < 6:
        "You look at the card you picked: Hang me"
        add tags 'hang_me_card' to anne
    else:
        "You look at the card you picked: Drown me"
        add tags 'drown_me_card' to anne
    call anne_third_session_play_her_game_decision from _call_anne_third_session_play_her_game_decision
    return

label anne_third_session_draw_multiple_cards:
    "You try to palm as many cards you can, but only come up with two: 'Hang me' and 'Drown me'"
    add tags 'hang_me_card' 'drown_me_card' to anne
    call anne_third_session_play_her_game_decision from _call_anne_third_session_play_her_game_decision_1
    return

label anne_third_session_play_her_game_decision:
    $ title = "What do you do?"
    menu:
        "Hang her" if anne.has_tag('hang_me_card'):
            call anne_third_session_hang_her from _call_anne_third_session_hang_her
        "Drown her" if anne.has_tag('drown_me_card'):
            call anne_third_session_drown_her from _call_anne_third_session_drown_her
        "Leave" if not anne.has_tag('threatened_to_leave') and not anne.has_tag('mindfuck_success'):
            add tags 'threatened_to_leave' to anne
            player.c "I'm not playing your sick games anymore.  This is insane!"
            wt_image ts_2
            anne.c "If you don't, I'll find someone who will!"
            anne.c "I don't want to find someone else. I want it to be you. These last few weeks ... they've been the best weeks of my life. You've made this possible."
            anne.c "Please. It's the last stage of my journey. I want you to be the one to finish it for me. I want your face to be the last one I see."
            anne.c "Please?"
            "Is this a form of love? Is she really appealing to you to kill her because of her affection for you?"
            call anne_third_session_play_her_game_decision from _call_anne_third_session_play_her_game_decision_2
        "Just go" if anne.has_tag('threatened_to_leave') and not anne.has_tag('mindfuck_success'):
            "Maybe she'll find someone else to execute her. Maybe she won't. Either way, you won't have her blood on your hands. You go home, leaving her alone with her twisted desires."
            $ anne.change_status("rejected")
            change player energy by -energy_very_short notify
            call anne_third_session_end from _call_anne_third_session_end_8
    return

label anne_third_session_hang_her:
    player.c "Turn around."
    wt_image ts_4
    "Trembling like a leaf, [anne.name] turns around."
    wt_image ts_119
    "You pull her arms behind her back and tie them firmly together."
    player.c "Step up on the box."
    wt_image ts_120
    "Her legs are shaking too much to lift herself, so you help her climb up. The noose is already tied and hanging from the ceiling. You slip it over her head and tighten it around her neck."
    wt_image ts_121
    anne.c "Please!  Don't do it!  I don't want to go through with it!!"
    $ title = "What do you do?"
    menu menu_anne_hang_her:
        "Kick the box away":
            sys "Content disabled to comply with forum rules.  Choose again."
            jump menu_anne_hang_her
            #wt_image ts_122
            #"The short drop jolts her."
            #wt_image ts_123
            #"The weight of her body pulling down on the rope cuts off her air supply instantly. With her arms bound behind her, she has no way to relieve the pressure on her neck."
            #wt_image ts_124
            #"She starts kicking, twisting, this way ..."
            #wt_image ts_123
            #"... and that way. Slowly suffocating, she tries desperately to regain access to air, but it's no use. There's no way for her to lift her weight off the rope."
            #wt_image ts_124
            #"Her kicks become more and more violent ... "
            #wt_image ts_125
            #"... and then fade away.  Her eyes roll back in her head ..."
            #wt_image ts_126
            #"... and then its over.  She twists slowly in front of you, her now lifeless eyes open but unseeing."
            #$ title = "What do you do now?"
            #menu:
            #    "Leave her there":
            #        wt_image ts_127
            #        "You collect your executioner's fees.  500.  Generous payment for one night's work."
            #        "As you leave, you take one last look at her corpse dangling at the end of the rope. If it is five years before anyone has reason to come back in here, she'll look quite different by then."
            #        "You lock the door behind you and leave."
            #    "Cut her down":
            #        wt_image ts_128
            #        "You cut her down and lay her corpse on the floor.  She looks at peace, a state her fascination with suffering rarely allowed her to experience in life."
            #        $ title = "What now?"
            #        menu:
            #            "Defile her corpse":
            #                "She denied you access to her cunt in life.  She has no say over what you do with her in death."
            #                wt_image ts_129
            #                "You roll her over and pull off her panties, her stockings and shoes coming off with them. Then you fuck her corpse, taking from her in her death the pleasure she denied you in life."
            #                player.c "[player.orgasm_text]"
            #                orgasm
            #            "Go home":
            #                pass
            #        "You collect your executioner's fees.  500.  Generous payment for one night's work.  Then you lock the door behind you and leave."
            #change player money by 500
            #call forced_movement(living_room)
            #change player energy by -energy_short notify
        "End her mindfuck here" if anne.has_tag('mindfuck_success'):
            call anne_third_session_play_her_game_end_mindfuck from _call_anne_third_session_play_her_game_end_mindfuck
        "Release her and go home" if not anne.has_tag('mindfuck_success'):
            call anne_third_session_play_her_game_release_her from _call_anne_third_session_play_her_game_release_her
    return

label anne_third_session_drown_her:
    player.c "Turn around and kneel down."
    wt_image ts_130
    "Shakily, she drops to her knees.  You pull her arms behind her back and tie them together."
    player.c "Get in the tub."
    wt_image ts_131
    "Her legs are rubber, and you need to help her into the large metal tub she's placed along one wall. Forlornly, she looks up at you as you step away ..."
    wt_image ts_132
    "A hose is already connected to a faucet.  You pick it up and start to fill the tub. [anne.name] closes her eyes as the water starts to rise around her."
    wt_image ts_133
    "You push her backward.  Without the use of her arms, she can't keep her balance, and has no leverage to lift herself up."
    anne.c "Please!  Don't do it!  I don't want to go through with it!!"
    $ title = "What do you do?"
    menu menu_anne_drown_her:
        "Hold her head under":
            wt_image ts_134
            "You push her head down under the water. She fights against you, but without the use of her arms, she hasn't a chance."
            wt_image ts_135
            "She holds on to the precious air in her lungs as long as she can, preserving it, drawing every molecule of oxygen out of it as she stares at you, hoping that you'll relent and let her raise her head back above water."
            $ title = "What do you do now?"
            menu menu_anne_hold_her_head_under:
                "Drown her":
                    sys "Content disabled to comply with forum rules.  Choose again."
                    jump menu_anne_hold_her_head_under
                    #"You continue to hold her under, until all trace of oxygen has been exhausted from the air in her lungs."
                    #wt_image ts_136
                    #"Involuntarily, she fights to replace it, releasing the air from her lungs an drawing in only water. Her eyes roll back in her head ..."
                    #wt_image ts_137
                    #"... and then it's over. She stops struggling to lift herself. Water fills her lungs, pulling her body downward, sinking to the bottom of the tub."
                    #"Lifelessly, her eyes stare upwards through the water, unseeing."
                    #$ title = "What now?"
                    #menu:
                    #    "Leave her there":
                    #        "You leave her corpse in the tub.  If it is five years before anyone has reason to come back in here, she'll look quite different by then."
                    #    "Pull her out":
                    #        wt_image ts_144
                    #        "You pull her out of the tub and lay her corpse on the floor. She looks at peace, a state her fascination with suffering rarely allowed her to experience in life."
                    #        $ title = "Now what?"
                    #        menu:
                    #            "Defile her corpse":
                    #                "She denied you access to her cunt in life.  She has no say over what you do with her in death."
                    #                wt_image ts_129
                    #                "You roll her over and pull off her panties, her stockings and shoes coming off with them. Then you fuck her corpse, taking from her in her death the pleasure she denied you in life."
                    #                player.c "[player.orgasm_text]"
                    #                orgasm
                    #            "Go home":
                    #                pass
                    #"You collect your executioner's fees.  500.  Generous payment for one night's work.  You lock the door behind you as you leave."
                    #change player money by 500
                    #call forced_movement(living_room)
                    #change player energy by -energy_short notify
                "End her mindfuck here" if anne.has_tag('mindfuck_success'):
                    call anne_third_session_play_her_game_end_mindfuck from _call_anne_third_session_play_her_game_end_mindfuck_1
                "Release her and go home" if not anne.has_tag('mindfuck_success'):
                    call anne_third_session_play_her_game_release_her from _call_anne_third_session_play_her_game_release_her_1
        "Find a faster and easier way to drown her":
            sys "Content disabled to comply with forum rules.  Choose again."
            jump menu_anne_drown_her
            #"On a table nearby you find a ring gag. She may not have intended it for this purpose, but it will work well."
            #wt_image ts_138
            #anne.c "Nooo!!!"
            #"You force her mouth open and lock the gag in place."
            #wt_image ts_139
            #"She fights to keep her head above water as you push her backwards, but it's a losing fight ..."
            #wt_image ts_140
            #"... without the use of her arms, she has no leverage. You easily push her head below the water line. The water rushes in through her open mouth, forcing the air out of her lungs."
            #wt_image ts_141
            #"She thrashes wildly under the water, but she can't lift herself out, and her body can't make any use of the water that fills her lungs."
            #wt_image ts_142
            #"It's over quickly. The thrashing stops, and she sinks to the bottom of the tub. Lifelessly, her eyes stare upwards through the water, unseeing."
            #$ title = "What do you do now?"
            #menu:
            #    "Leave her there":
            #        "You leave her corpse in the tub.  If it is five years before anyone has reason to come back in here, she'll look quite different by then."
            #    "Pull her out":
            #        wt_image ts_143
            #        "You pull her out of the tub and lay her corpse on the floor. She looks at peace, a state her fascination with suffering rarely allowed her to experience in life."
            #        $ title = "What now?"
            #        menu:
            #            "Defile her corpse":
            #                "She denied you access to her cunt in life.  She has no say over what you do with her in death."
            #                wt_image ts_129
            #                "You roll her over and pull off her panties, her stockings and shoes coming off with them. Then you fuck her corpse, taking from her in her death the pleasure she denied you in life."
            #                player.c "[player.orgasm_text]"
            #                orgasm
            #            "Go home":
            #                pass
            #"You collect your executioner's fees.  500.  Generous payment for one night's work.  You lock the door behind you as you leave."
            #change player money by 500
            #call forced_movement(living_room)
            #change player energy by -energy_short notify
        "End her mindfuck here" if anne.has_tag('mindfuck_success'):
            call anne_third_session_play_her_game_end_mindfuck from _call_anne_third_session_play_her_game_end_mindfuck_2
        "Release her and go home" if not anne.has_tag('mindfuck_success'):
            call anne_third_session_play_her_game_release_her from _call_anne_third_session_play_her_game_release_her_2
    return

label anne_third_session_play_her_game_end_mindfuck:
    "You untie her and release her."
    player.c "That completes your mindfuck, Anne. You got to experience death, and then the prospect of another death. Let that be enough. Relive these memories as often as you need, but leave this game behind."
    "You collect your executioner's fees.  500.  Generous payment for one night's work.  Then you leave her alone with her memories."
    sys "You've earned continuing actions with the Tortured Soul, but it isn't implemented in this version of the game."
    #$ anne.change_status("rejected")
    #add tags 'continuing_actions' to anne
    change player money by 500
    call anne_third_session_end from _call_anne_third_session_end_9
    return

label anne_third_session_play_her_game_release_her:
    wt_image ts_1
    "This is as far as you go. She wants to be released, so you do as she asks, getting her back to the safety of her feet on the floor and untying her."
    "Maybe she'll find someone else to execute her. Maybe she won't. Either way, you won't have her blood on your hands. You go home, leaving her alone with her twisted desires."
    $ anne.change_status("rejected")
    change player energy by -energy_very_short notify
    call anne_third_session_end from _call_anne_third_session_end_10
    return

label anne_third_session_end:
  if anne.status != "rejected":
    $ anne.change_status("minor_character")
  call character_location_return(anne) from _call_character_location_return_21
  call forced_movement(living_room) from _call_forced_movement_117
  if anne.has_tag('hypno_this_session'):
    # the following deducts energy and tracks that hypnosis happened
    $ anne.hypno_session()
    rem tags 'hypno_this_session' from anne
  change player energy by -energy_very_short notify
  notify
  end_day
  return

# Hypno Actions
# note: this is back up code in case you're accidentally able to select the Hypnosis Action for her directly
label anne_hypnosis_start:
  "Talk to her instead.  There may be an opportunity to hypnotize her, but not just yet."
  $ anne.hypno_action.backtrack = True
  $ context = "anne_hypnosis"
  break_sequence
  reset_menu
  return

label anne_hypnosis_end:
  pass
  # break_sequence
  return

# Check prospect label
## note: this converts her from a single message to being able to send multiple messages
## also, this same system can be used to add additional conditionals to getting a new prospect message, other than the standard week and rep conditionals
## the major client equivalent of this is _availability_check
## the existence of this label means the standard prospect check does not fire, so need to include those standard conditions for message 0
label anne_prospect_check:
    # We start with the standard check
    if anne.current_message == 0:
        $ return_value = week + 1 >= anne.week_available and anne.prospect_min_reputation <= player.reputation
    elif anne.current_message == 1:
        $ return_value = anne.second_session and anne.message_follow_up_available
        if anne.second_session and anne.message_follow_up_available:
            add tags 'new_message_today' to anne
        # $ anne.current_client_action.name = "New Message from [anne.full_name]"  ## doesn't work here, needs to be in the prospect check after the action is re-created
    elif anne.current_message == 2:
        $ return_value = anne.third_session and anne.message_follow_up_available
        if anne.third_session and anne.message_follow_up_available:
            add tags 'new_message_today' to anne
        # $ anne.current_client_action.name = "New Message from [anne.full_name]"  ## doesn't work here, needs to be in the prospect check after the action is re-created
    return


# Initial Contact Message

label anne_message:
    ## first message
    if anne.current_message == 0:
        anne.c "{i}I need to be used hard. I'm looking for a man who's willing to hurt me with no consideration to the pain he's inflicting on me. I don't want any sympathy, or compassion, or concern about my welfare.  Just pain and fear.{/i}"
        anne.c "{i}I don't have a husband or boyfriend to hire you to train me. I don't want to be trained, anyway. I just want to be made to suffer. I'll happily pay you to do this to me.{/i}"
        anne.c "{i}I'm not willing to have sex with you under any circumstances. Other than that, you can do anything you want with my body. You don't need to worry about leaving marks, or scars, or permanent damage.  I'd welcome any of them.{/i}"
        anne.c "{i}I'll pay you double your normal fee if you'll give me what I need.  ~ Tortured Soul{/i}"

        $ title = "Accept the engagement?"
        menu:
            "Yes (ends day)":
                $ anne.current_message = 1
                $ living_room.remove_action(anne.current_client_action)
                "She asks you to meet her in an industrial park.  You prefer to meet your clients at home, but she insists on the location she's picked out."
                anne.c "{i}I've set it up with everything you will need.{/i}"
                call forced_movement(anne_warehouse) from _call_forced_movement_133
                wt_image current_location.image
                "The back door is open."
                $ title = "What do you do?"
                menu:
                    "Go in":
                        summon anne no_follows
                        wt_image ts_1
                        "A dark-haired woman is waiting for you."
                        anne.c "You came.  I wasn't sure you would."
                        $ anne.first_session = True

                    "Go home":
                        $ anne.change_status("rejected")
                        "Perhaps this wasn't such a good idea.  Who knows what sort of crazy may be waiting for you in there?  You head back home while there's still time to do something with your day."
                        call forced_movement(living_room) from _call_forced_movement_134

            "Not yet":
                "You have until the end of week [anne.accept_limit] to accept this engagement."
                $ anne.current_client_action.name = "Reply to Tortured Soul"
                if not anne.first_message_read:
                    $ anne.first_message_read = True
                    $ anne.message_note = add_note((anne.wait_for_message_period + 1) * 5, "{} offer ends".format(anne.name))

            "Never (deletes message)":
                $ anne.change_status("rejected")
    ## second message
    elif anne.current_message == 1:
        if anne.hypno_blowjob_count > 0:
            anne.c "{i}I've decided to forgive you for violating my wish not to have sex with you, if for no other reason than I'm still not sure how you managed to do it and that scares me to the core.{/i}"
        anne.c "{i}I need to hire you again.  Please come meet me at the warehouse as soon as you can.{/i}"
        $ title = "Accept the engagement?"
        menu:
            "Yes (ends day)":
                $ anne.current_message = 2
                $ anne.message_follow_up_available = False
                call forced_movement(anne_warehouse) from _call_forced_movement_135
                summon anne no_follows
                wt_image current_location.image
                "You let [anne.name] know you'll be there soon.  When you get to the warehouse, the back door is open again."
                wt_image ts_1
                "She's waiting for you inside. On a table beside her is a deck of cards and a sheet of paper."
            "Not yet":
                "You have the feeling that this offer will remain open for a while."
                $ anne.current_client_action.name = "Reply to [anne.name]"
            "Never (deletes message)":
                $ anne.change_status("rejected")
    ## third message
    elif anne.current_message == 2:
        anne.c "{i}I need to hire you again.  Please come meet me at the warehouse as soon as you can.{/i}"
        $ title = "Accept the engagement?"
        menu:
            "Yes (Ends Day)":
                $ anne.current_message = 3
                $ anne.message_follow_up_available = False
                call forced_movement(anne_warehouse) from _call_forced_movement_136
                wt_image current_location.image
                "You let [anne.name] know you'll be there soon.  When you get to the warehouse, the back door is open again."
                wt_image ts_1
                "She's waiting for you inside. A deck of cards is on the table beside her."
            "Not Yet":
                "You have the feeling that this offer will remain open for a while."
                $ anne.current_client_action.name = "Reply to [anne.name]"
            "Never (Deletes Message)":
                $ anne.change_status("rejected")
    return

## this content replaced by new multiple prospect message system
# label anne_follow_up_message:
#     if anne.second_session:
#         if anne.hypno_blowjob_count > 0:
#             anne.c "{i}I've decided to forgive you for violating my wish not to have sex with you, if for no other reason than I'm still not sure how you managed to do it and that scares me to the core.{/i}"
#         anne.c "{i}I need to hire you again.  Please come meet me at the warehouse as soon as you can.{/i}"
#         $ title = "Accept the engagement?"
#         menu:
#             "Yes (Ends Day)":
#                 $ anne.message_follow_up_available = False
#                 call forced_movement(anne_warehouse) from _call_forced_movement_135
#                 wt_image current_location.image
#                 "You let [anne.name] know you'll be there soon.  When you get to the warehouse, the back door is open again."
#                 wt_image ts_1
#                 "She's waiting for you inside. On a table beside her is a deck of cards and a sheet of paper."
#             "Not Yet":
#                 "You have the feeling that this offer will remain open for a while."
#                 $ anne.current_client_action.name = "Reply to [anne.name]"
#             "Never (Deletes Message)":
#                 $ anne.change_status("rejected")
#     if anne.third_session:
#         anne.c "{i}I need to hire you again.  Please come meet me at the warehouse as soon as you can.{/i}"
#         $ title = "Accept the engagement?"
#         menu:
#             "Yes (Ends Day)":
#                 $ anne.message_follow_up_available = False
#                 call forced_movement(anne_warehouse) from _call_forced_movement_136
#                 wt_image current_location.image
#                 "You let [anne.name] know you'll be there soon.  When you get to the warehouse, the back door is open again."
#                 wt_image ts_1
#                 "She's waiting for you inside. A deck of cards is on the table beside her."
#             "Not Yet":
#                 "You have the feeling that this offer will remain open for a while."
#                 $ anne.current_client_action.name = "Reply to [anne.name]"
#             "Never (Deletes Message)":
#                 $ anne.change_status("rejected")
#     else:
#         sys "You've earned another visit with the Tortured Soul, but it isn't implemented in this version of the game."
#         $ anne.change_status("rejected")
#     return

## Character Specific Actions
# N/A

########### OBJECTS ###########
## Common Objects

# View Relationship Status
# N/A

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_anne:
    "She has issues, but anal sex isn't one of them."
    return

# Give Chastity Belt
label give_cb_anne:
    "She has issues, but promiscuity isn't one of them."
    return

# Give Dildo
label give_di_anne:
    "She has issues, but a lack of masturbation isn't one of them."
    return

# Use Fetch Toy
label use_ft_anne:
    "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_anne:
    "Save this as a gift for [chelsea.name]."
    return

# Use Leash
label use_le_anne:
    "You shouldn't try to take someone for a walk who isn't your pet."
    return

# Give Lingerie
label give_li_anne:
    "That's a nice gesture, but save this for someone who'll appreciate it more."
    return

# Give Love Potion
label give_lp_anne:
    "Save this for someone else."
    return

# Give Transformation Potion
label give_tp_anne:
    "There may be content for this eventually, but not yet."
    return

# Use Water Bowl
label use_wb_anne:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
    return

# Use Will Tamer
label use_wt_anne:
    "There may be content for this eventually, but not yet."
    return


########### TIMERS ###########
## Common Timers
# Start Day
label anne_start_day:
    if anne.has_tag('new_message_today'):
        rem tags 'new_message_today' from anne
        $ anne.current_client_action.name = "New Message from [anne.full_name]"
    return

# End Day
label anne_end_day:
    pass
    return

# End Week
label anne_end_week:
    if anne.next_visit_week > 0 and week > anne.next_visit_week:
        $ anne.change_status("prospect")
        $ anne.message_follow_up_available = True
        # $ anne.current_client_action.name = "New Message from [anne.full_name]" ## doesn't work here, needs to be in start_day after the action is re-created
        $ anne.next_visit_week = 0
    return

## Character Specific Timers
# N/A

########### ROOMS ###########
# Examine Warehouse
label aw_examine:
  "This appears to be a storage warehouse."
  return

label aw_no_access:
  return

label aw_enter:
  return

label aw_exit:
  return

## NOTES
# NEED:
# Will-Tamer transformation content
# Transformation Potion transformation content
# Fund Buf in Third Session Mind-Fuck that crashes game
