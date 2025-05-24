## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package lee name allows her to be a minor character
# dependencies core chelsea and core lauren
register lee_pregame 15 in core as "Lee the Psycho"

label lee_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Lee the Psycho (Lorelei Lee)")]

    ## Character Definition
    #Red
    # Dark Olive Green
    lee = Person(Character("Lee", who_color="#445626", what_color="#445626", window_background=gui.dialogue_background_dark_font_color), "lee", cut_portrait = True, prefix = "", suffix = "the Psycho")
    lee.your_name = "bootlick"
    lee.her_respect_name = "Goddess"


    # Other Characters
    # N/A
    principal_lover = Character("Hannah's Lover", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)

    ## Actions
    lee.action_contact = living_room.add_action("Contact " + lee.full_name, label = lee.short_name + "_contact", context = "_contact_other", condition = "lee.can_be_interacted and ((lee.domme_you_status > 1 and not lee.has_tag('domme')) or (lee.has_tag('domme') and (lee.diamond_status == 1 or lee.diamond_status == 4)))")
    lee.action_domme_you = lee.add_action("Have her Domme you", label = "_domme_you", condition = "lee.can_be_interacted and lee.domme_you_status == 4 and lee.in_area('house')")
    lee.action_end_session = lee.add_action("Send her home", label="_end_session", condition = "lee.in_area('house')")

    lee.relationship_action = bedroom.add_action("[lee.full_name]", label = lee.short_name + "_relationship_status", context = "_relationship_status", condition = "lee.domme_you_status == 4 or lee.has_tag('domme')")


    ## Tags
    # Common Character Tags
    lee.add_tags('no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    lee.change_status("minor_character")
    lee_collar = Item("Lee's Collar", 'lpc', with_examine = True, with_give = False)

    # Start Day Events
    start_day_labels.append('lee_start_day', priority = 50) # note: Lee's start priority is later than most, so that hers come in later


    ########### VARIABLES ###########
    # Common Character Variables
    lee.add_stats_with_value('domme_outfit', 'random_number', 'relationship_counter')

    # Character Specific Variables
    lee.add_stats_with_value('ass_worship_count', 'diamond_status','domme_bi_scene','domme_you_status', 'domme_you_count', 'flogged_you_count', 'gagged_you_count','pegged_you_count', 'next_call_countdown')
    # domme_you_status key: 0: not active, 1: shut off, 2: unresolved, 3: will activate ext day, 4: active, 5: now Domme
    # diamond_status key: 0: not active, 1: spoke to M about it, 2: didn't proceed, 3: delaying until end day, 4: can hold the session, 5: scene w M pending, 6: scene with M skipped, 7: scene with M completed, didn't suck his cock, 8: scene with M completed, sucked his cock
  return

# Display Portrait
# CHARACTER: Display Portrait
label lee_update_media:
    if lee.in_area('house') and lee.has_tag('domme_visit'):
        $ lee.change_image('psycho_domme_1_2')
    elif lee.has_tag('domme'):
        $ lee.change_image('psycho_contact_2_1')
    else:
        $ lee.change_image('cheater_revenge_3_10')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label lee_examine:
    if lee.in_area('house') and lee.has_tag('domme_visit'):
        "She's waiting until you're ready to start.  It's hard to tell if she's bored, eager or simply contemptuous."
    else:
        "It's Lee the Psycho."
    return

# Talk to Character
label lee_talk:
    if lee.in_area('house') and lee.has_tag('domme_visit'):
        $ lee.change_image('psycho_domme_1_2')
        "She's not here to talk.  She's here to hurt you."
    else:
        "There's nothing for the two of you to talk about."
    return

# Hypno Actions
label lee_hypnosis_start:
    if lee.has_tag('domme_visit'):
        "She's too focussed on the reason for her visit to be distracted by your focus or your attempts to get her to look at it."
    else:
        "You can't hypnotize her here."
    $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    return


## Character Specific Actions
label lee_domme_you:
    $ lee.training_session()
    $ lee.domme_you_count += 1
    # first session
    if lee.domme_you_count == 1:
        wt_image psycho_domme_1_2
        lee.c "So how exactly do you think this is going to go?"
        $ title = "What do you say?"
        menu:
            "However you want, Mistress":
                pass
            "I want you to hurt me, Mistress":
                pass
            "I want you to use me for your own pleasure, Mistress":
                pass
        lee.c "No!  Shut up!!  Get on your fucking knees before you say a goddamn thing."
        $ title = "Kneel?"
        menu:
            "Yes":
                pass
            "No":
                lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind and really do want me to hurt you."
                $ title = "What now?"
                menu:
                    "Kneel":
                        player.c "Wait, Mistress!  Stop, please.  I'm sorry."
                    "Hypnotize her" if player.can_hypno(lee):
                        "She's too wary of you and this whole situation to be distracted by your focus.  She storms out."
                        jump lee_failed_session # must jump, not call
                    "Let her go":
                        jump lee_failed_session # must jump, not call
        # continue if didn't jump away
        wt_image psycho_domme_1_3
        "You drop to your knees as the biker chick towers over you.  Your attention drifts back and forth between her strong thighs and the cruel look on her face."
        lee.c "Try again, loser.  How exactly do you think this is going to go?"
        $ title = "What do you say?"
        menu:
            "However you want, Mistress":
                pass
            "I want you to hurt me, Mistress":
                pass
            "I want you to use me for your own pleasure, Mistress":
                pass
        wt_image psycho_domme_1_4
        lee.c "No!  Shut up!!  God, did you really think I give a fuck about what you think?"
        $ title = "What do you say?"
        menu:
            "No, Mistress":
                wt_image psycho_domme_1_5
                "Pulling her hand back, she slaps you hard across the cheek ... *SLAP*"
                lee.c "God, you're pathetic."
            "But you asked!":
                wt_image psycho_domme_1_5
                "Pulling her hand back, she slaps you hard across the cheek ... *SLAP*"
                lee.c "God, you're stupid."
        wt_image psycho_domme_1_6
        lee.c "Listen close, because I'm not going to explain it again.  Here's what's going to happen today."
        wt_image psycho_domme_1_5
        "She slaps you again, even harder ... *SLAPPPP*"
        wt_image psycho_domme_1_6
        lee.c "Nothing.  Nothing is going to happen today.  I see you that tiny chubby in your pants, and both you and it can forget it."
        wt_image psycho_domme_1_5
        "*SLAPPPP*"
        wt_image psycho_domme_1_4
        lee.c "I am not here to be your fucking sextoy.  I don't even like you.  I like tough, strong men, not worthless worms like you."
        wt_image psycho_domme_1_5
        "*SLAPPPP*"
        wt_image psycho_domme_1_6
        lee.c "I'll take your fucking money, because you obviously have too much of it.  But I am not your whore, understand?"
        $ title = "What do you say?"
        menu:
            "Yes, Mistress, I understand":
                wt_image psycho_domme_1_4
                lee.c "Good.  I'm glad we understand each other."
            "Ask for permission to speak":
                wt_image psycho_domme_1_4
                lee.c "That's cute.  Okay, speak."
                $ title = "What do you say?"
                menu:
                    "Yes, Mistress, I understand":
                        lee.c "Good.  I'm glad we understand each other."
                    "You set the rules, Mistress, and I'll obey":
                        "Your response throws her for a loop and she's silent for a moment before she responds.  Despite her bluster, she's uncertain about this whole arrangement, yet you get the sense she's more attracted to it than she's letting on."
                        lee.c "Good.  I'm glad we understand each other."
                        sys "Lee's feeling better about your relationship."
                        $ lee.relationship_counter += 1
            "Funny, you look like a whore":
                wt_image psycho_domme_1_1
                lee.c "Fuck you!!"
                "She storms off, and that's the last you see of her."
                $ chelsea.lee_event_status = 0
                $ lee.domme_you_status = 1
                call convert(lee, 'unavailable') from _call_convert_196
                jump lee_failed_session # must jump, not call
        # continue if didn't jump away
        wt_image psycho_domme_1_6
        lee.c "Here are the ground rules.  When I come over, I decide what I do with you, if anything.  Agreed?"
        $ title = "Do you agree?"
        menu:
            "Yes":
                wt_image psycho_domme_1_5
                "*SLAPPPP*"
            "No":
                wt_image psycho_domme_1_1
                lee.c "This isn't a fucking negotiation.  Agree or I'm outta here."
                $ title = "Do you agree?"
                menu:
                    "Yes":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "No":
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
            "Can I at least set limits?":
                lee.c "Limits?  Well, yeah.  I mean I'm not going to castrate you.  But you can't ask me to do something I don't want to do."
                $ title = "What do you say?"
                menu:
                    "Of course, Mistress":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "I'm paying, I should have some say":
                        wt_image psycho_domme_1_4
                        lee.c "You fucking think I'm that hard up for money?  Think again.  I decide what we do, not you."
                        $ title = "What do you say?"
                        menu:
                            "Of course, Mistress":
                                wt_image psycho_domme_1_5
                                "*SLAPPPP*"
                            "No":
                                lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                                jump lee_failed_session
            "I'm paying, I should have some say":
                wt_image psycho_domme_1_4
                lee.c "You fucking think I'm that hard up for money?  Think again.  I decide what we do, not you."
                $ title = "What do you say?"
                menu:
                    "Of course, Mistress":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "No":
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_4
        lee.c "And you don't get to complain that I didn't do enough to earn your money.  I don't fucking work for you, understand?  I decide when you got your money's worth, not you.  Agreed?"
        $ title = "Do you agree?"
        menu:
            "Yes":
                wt_image psycho_domme_1_5
                "*SLAPPPP*"
            "Yes, as long as you hurt me":
                wt_image psycho_domme_1_1
                lee.c "This isn't a fucking negotiation.  Agree or I'm outta here."
                $ title = "Do you agree?"
                menu:
                    "Yes":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "No":
                        wt_image psycho_domme_1_1
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
            "Yes, as long as I get off":
                wt_image psycho_domme_1_1
                lee.c "This isn't a fucking negotiation.  Agree or I'm outta here."
                $ title = "Do you agree?"
                menu:
                    "Yes":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "No":
                        wt_image psycho_domme_1_1
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
            "No":
                wt_image psycho_domme_1_1
                lee.c "This isn't a fucking negotiation.  Agree or I'm outta here."
                $ title = "Do you agree?"
                menu:
                    "Yes":
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "No":
                        wt_image psycho_domme_1_1
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_6
        lee.c "Let's test that.  This is all I'm doing today.  Slapping your stupid ugly face, then I'm taking your money and I'm leaving.  What do you say to that?"
        $ title = "What do you say?"
        menu:
            "As you wish, Mistress":
                wt_image psycho_domme_1_5
                "*SLAPPPP*"
            "I'm disappointed, but whatever you decide, Mistress":
                wt_image psycho_domme_1_4
                lee.c "Disappointed?  I'm not fucking here to earn your goddamn approval."
                $ title = "What do you say?"
                menu:
                    "I'm not disappointed in you, Mistress":
                        player.c "I'm not disappointed in you, Mistress.  I'm happy for whatever attention you give me.  I'm disappointed I don't get to spend more time with you today, is all, but that's your decision to make, not mine."
                        wt_image psycho_domme_1_6
                        if lee.relationship_counter > 0:
                            "For a moment, she's at a loss for words, again."
                        else:
                            "Your response throws her for a loop and she's silent for a moment before she responds.  Despite her bluster, she's uncertain about this whole arrangement, yet you get the sense she's more attracted to it than she's letting on."
                            sys "Lee's feeling better about your relationship."
                            $ lee.relationship_counter += 1
                        lee.c "Okay, well.  My decision stands.  I'm slapping you, then leaving."
                        player.c "Yes, Mistress."
                        wt_image psycho_domme_1_5
                        "*SLAPPPP*"
                    "That's good, because you haven't earned my approval":
                        wt_image psycho_domme_1_1
                        lee.c "Fuck you!  I don't need your approval, you patethic chump"
                        "She storms off, and that's the last you see of her."
                        $ chelsea.lee_event_status = 0
                        $ lee.domme_you_status = 1
                        call convert(lee, 'unavailable') from _call_convert_197
                        jump lee_failed_session # must jump, not call
            "That doesn't seem fair":
                wt_image psycho_domme_1_1
                lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_6
        lee.c "Okay.  Then I think we can come to an arrangement.  I'll come back and hurt you the same way I hurt that stupid tramp, on three conditions."
        lee.c "First, you let me tie you up.  Make sure you have lots of rope on hand so I can truss you up like a stupid pig."
        lee.c "Second, you make sure there's something here I can hit you with.  My hand's fucking stinging from slapping you."
        lee.c "Third, you pay me again.  I'm not doing this because I like you.  It's a business transaction, that's all."
        wt_image psycho_domme_1_6
        if lee.relationship_counter > 0:
            "Lee looks like she's about to leave, then hesitates."
            lee.c "What if I want you to grovel on your belly before I leave?"
            $ title = "What do you do?"
            menu:
                "Grovel for her":
                    wt_image psycho_domme_1_2
                    "It's hard to tell when you're down on the floor on your belly, but you think Lee might be getting a little flushed, watching you."
                    sys "Lee's feeling better about your relationship."
                    $ lee.relationship_counter += 1
                "Ask her to order you to grovel":
                    wt_image psycho_domme_1_1
                    lee.c "Nah.  Now it sounds like you're telling me what to do."
                "Tell her you'd rather she hurt you":
                    wt_image psycho_domme_1_1
                    lee.c "Too bad.  I already told you I'm not doing that until next time."
                    sys "Lee's feeling less good about your relationship."
                    $ lee.relationship_counter -= 1
        else:
            lee.c "Call me sometime if you decide to agree to my terms.  But not until next week.  I want you to think about it, first."
        change player energy by -energy_short notify
    # second session
    elif lee.domme_you_count == 2:
        wt_image psycho_domme_1_7
        "Lee picks up the rope you left out for her."
        lee.c "Take off your clothes and lie down.  I'm going to tie you up."
        $ title = "Let her tie you up?"
        menu:
            "Yes":
                pass
            "No":
                lee.c "You knew the terms.  Either let me tie you up or I leave."
                $ title = "Do you agree?"
                menu:
                    "Yes":
                        pass
                    "No":
                        lee.c "You fucking loser, I'm out of here.  And I'm keeping your money.  Call me if you change your mind."
                        jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_8
        "As finishes trussing you up, Lee looks down at you and leers."
        lee.c "You stupid idiot.  I'm going to give a couple of guys from my bike gang a call.  They'll rape your ass with a broomstick for even talking to me and then we'll clean this beautiful house of yours out."
        $ title = "What do you say?"
        menu:
            "You wouldn't do that":
                wt_image psycho_domme_1_9
                lee.c "No, I wouldnt.  I was just shitting you.  I'm not a cheat, I said I'd hurt you if you paid me and I will.  A nice honest business transaction."
            "I trust you":
                wt_image psycho_domme_1_9
                lee.c "What the fuck do you mean?  Why would you trust me?"
                $ title = "Why do you trust her?"
                menu:
                    "She's a good person":
                        wt_image psycho_domme_1_10
                        lee.c "Fuck, are you a bad judge of character.  I am so not a good person.  But I'm not a cheat, either.  I said I'd hurt you if you paid me and I will.  A nice honest business transaction."
                    "You don't know, you just do":
                        wt_image psycho_domme_1_11
                        lee.c "This better not be where you tell me we have a connection.  I like tough, strong men, not pathetic wimps.  This is just a business transaction."
                        "Lee's trying to convince somebody with her words, but you're not entirely sure it's you."
                        sys "Lee's feeling better about your relationship."
                        $ lee.relationship_counter += 1
            "Marilyn wouldn't like that" if player.marilyn_building_visit_count > 0:
                wt_image psycho_domme_1_9
                lee.c "Fuck that bitch.  An ex pimped me out to Marilyn for a favor once, the fucking dirtbag.  The both of them can go to hell."
                wt_image psycho_domme_1_10
                lee.c "Anyway, don't get your panties in a knot.  I was just shitting you.  I'm not a cheat, I said I'd hurt you if you paid me and I will.  A nice honest business transaction."
        wt_image psycho_domme_1_12
        "As she finishes undressing, Lee puts on her strap-on, then picks out a flogger from your collection of toys."
        lee.c "You said you wanted me to give you the same treatment I gave that cheating tramp.  You're about to get your wish, bitch."
        wt_image psycho_domme_1_13
        lee.c "Are you absolutely sure this is what you want?  I'm pretty strong.  If I start whacking you with this, it'll really fucking hurt."
        $ title = "What do you say?"
        menu:
            "Yes, Mistress, please hurt me":
                pass
            "You decide what happens to me while you're here, Mistress":
                wt_image psycho_domme_1_14
                lee.c "You don't fucking mean that.  I might just leave you tied up while I watch TV until I go.  You don't want to spend your money for that."
                player.c "If that'll make you happy, then yes, Mistress, it is what I want."
                wt_image psycho_domme_1_15
                "Lee's silent for a minute, a look of confusion on her face.  When she finally speaks, she sounds nervous."
                lee.c "I want to hurt you until you scream.  But maybe I'll just walk out of here now and keep your money."
                player.c "Whichever you prefer is okay with me, Mistress.  While you're here, my only role is to make you happy."
                wt_image psycho_domme_1_12
                lee.c "If this is just because you're a fucking masochist, I'm going to try and find a level of pain you can't enjoy."
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
            "Maybe you could just peg me?":
                add tags 'peg_only_today' to lee
            "No, I've changed my mind":
                wt_image psycho_domme_1_10
                lee.c "Probably the smartest choice you made all day.  I'm keeping your money, though.  Call me again sometime if you change your mind."
                jump lee_failed_session
        if not lee.has_tag('peg_only_today'):
            $ lee.flogged_you_count += 1
            wt_image psycho_domme_1_16
            "*THWAPPP* ... You wince in pain as Lee brings the flogger down on your chest."
            wt_image psycho_domme_1_17
            "It takes a lot to make a flogger actually hurt and not just sting, but Lee seems determined to do so, swinging it overhand with all her might ... *THWAPPP* ..."
            wt_image psycho_domme_1_18
            "... while circling you and striking your exposed body from every angle ... *THWAPPP*"
            wt_image psycho_domme_1_19
            "You're trying so hard to tolerate the pain she's causing you ... *THWAPPP* ..."
            wt_image psycho_domme_1_20
            "... that you're surprised to hear screaming, and even more surprised to realize it's coming from you ... *THWAPPP*"
            player.c "OOOWWWWW!!!"
            wt_image psycho_domme_1_21
            lee.c "Fuck, that was pathetic.  That cheating tramp took her punishment so much better than you took yours, you wuss."
            $ title = "What do you say?"
            menu:
                "Keep going":
                    wt_image psycho_domme_1_22
                    lee.c "Fuck that, you got your money's worth of a beating.  Besides, I want to hear if you scream that loud when I ream your pansy ass."
                "I'm sorry, Mistress":
                    wt_image psycho_domme_1_22
                    lee.c "Not yet, you aren't, but maybe you will be.  Lets hear if you scream that loud when I ream your pansy ass."
                "Fuck you":
                    wt_image psycho_domme_1_22
                    lee.c "Actually, no.  Now I fuck you."
        else:
            wt_image psycho_domme_1_23
            lee.c "The sight of my strap-on has you so excited you can't wait, huh?"
        wt_image psycho_domme_1_23
        $ title = "What do you say?"
        menu:
            "Yes, Mistress":
                call lee_first_pegging from _call_lee_first_pegging
            "No, I don't want that in my butt":
                if lee.has_tag('peg_only_today'):
                    wt_image psycho_domme_1_13
                    lee.c "What the fuck is up with you?  First you want me to peg you, then you don't."
                    wt_image psycho_domme_1_19
                    lee.c "Fuck this, loser.  You can play your mind games with some other bitch, I'm going home.  Call me if you change your mind."
                    jump lee_failed_session
                else:
                    wt_image psycho_domme_1_14
                    lee.c "You pathetic loser.  You really can't take what I dished out to that cheating tramp.  I knew you were weak."
                    wt_image psycho_domme_1_10
                    lee.c "Call me again the next time you want to waste your money, preferably sometime when you're not so chickenshit."
                    "She unties you and leaves."
                    if lee.relationship_counter > 0:
                        sys "Lee's feeling less good about your relationship."
                        $ lee.relationship_counter -= 1
                    change player energy by -energy_long notify
    # special sessions go here
    # ass-worship scene
    elif not lee.has_tag('special_session_last_time') and lee.relationship_counter > 5 and not lee.has_any_tag('ass_worship_scene_complete', 'no_ass_worship'):
        add tags 'ass_worship_scene_complete' 'special_session_last_time' to lee
        wt_image psycho_domme_1_2
        lee.c "Get on your fucking knees."
        wt_image psycho_domme_1_3
        lee.c "You're in for a treat, today.  Probably more of a treat than you deserve."
        wt_image psycho_domme_1_32
        "Turning around, she pulls up the hem of her skirt."
        wt_image psycho_domme_1_33
        lee.c "Don't just fucking sit there.  Crawl over here and stick your tongue in my ass."
        wt_image psycho_domme_1_34
        $ title = "Worship her ass?"
        menu:
            "Yes":
                rem tags 'no_ass_worship' from lee
            "No":
                wt_image psycho_domme_1_35
                lee.c "That wasn't a request.  Either stick your tongue in my ass or I'm leaving."
                wt_image psycho_domme_1_34
                $ title = "Obey her?"
                menu:
                    "Yes":
                        rem tags 'no_ass_worship' from lee
                    "Refuse":
                        add tags 'no_ass_worship' to lee
                        wt_image psycho_domme_1_1
                        lee.c "You make it sound like you want to please me, but I guess you just want me to play out your sick fantasies.  Not today, loser.  Call me the next time you want to give me money for us to do nothing together."
                        jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_36
        "Her hand stops you just before your tongue makes contact with her."
        wt_image psycho_domme_1_37
        lee.c "Your tongue goes in here, and only here.  You haven't earned a taste of my snatch."
        wt_image psycho_domme_1_38
        "Her instructions received, you put your tongue to work in the only hole she'll allow you access to, today."
        wt_image psycho_domme_1_39
        "After a few minutes, you feel her hand on your head, pulling you closer."
        wt_image psycho_domme_1_40
        $ title = "How do you feel about what you're doing?"
        menu:
            "You love it":
                wt_image psycho_domme_1_41
                "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
                wt_image psycho_domme_1_42
                "Your eager tongue works frantically inside her butthole, probing and teasing her as best you can."
                wt_image psycho_domme_1_10
                "And then suddenly, she's cumming."
                lee.c "FUUCCKKK!!"
                wt_image psycho_domme_1_41
                lee.c "Jesus, I'm almost tempted to give you your money back after that.  Almost."
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
            "You do it because she wants you to do it":
                wt_image psycho_domme_1_41
                "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
                wt_image psycho_domme_1_42
                lee.c "You're my bitch, aren't you?  My ass-eating, fucking perv of a bitch."
                wt_image psycho_domme_1_41
                "Lee keeps you there for a while, enjoying the sensation of your tongue in her ass."
                wt_image psycho_domme_1_40
                lee.c "That feels so good I'm almost tempted to give you your money back.  Almost."
            "You love it because she wants you to do it":
                wt_image psycho_domme_1_41
                "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
                wt_image psycho_domme_1_42
                "Your eager tongue works frantically inside her butthole, probing and teasing her as best you can."
                wt_image psycho_domme_1_10
                "And then suddenly, she's cumming."
                lee.c "FUUCCKKK!!"
                wt_image psycho_domme_1_41
                lee.c "Jesus, I'm almost tempted to give you your money back after that.  Almost."
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
        wt_image psycho_domme_1_33
        lee.c "Call me the next time you want to pay me to stick your tongue up my ass."
        $ lee.ass_worship_count += 1
        change player energy by -energy_very_short notify
    # gag scene
    elif not lee.has_tag('special_session_last_time') and lee.relationship_counter > 5 and dungeon.has_item(gags) and not lee.has_tag('gag_scene_complete'):
        add tags 'special_session_last_time' 'gag_scene_complete' to lee
        wt_image psycho_domme_1_2
        lee.c "Get on your fucking knees."
        wt_image psycho_domme_1_4
        lee.c "I saw something in your playroom I want to try out on you."
        wt_image psycho_domme_1_43
        "She fumbles a little bit, but not too much, locking the gag into place."
        wt_image psycho_domme_1_44
        lee.c "I like this.  Finally a fool-proof way to make a man shut-the-fuck up.  You just stay there while I watch some TV.  If you'd like to complain about what I'm watching, well - I guess you fucking can't!"
        wt_image psycho_domme_1_45
        "She really does leave you there while she watches TV."
        wt_image psycho_domme_1_44
        "She leaves you there a very long time, until your joints are aching from holding this position."
        wt_image psycho_domme_1_45
        "Finally, she turns her attention back to you."
        $ title = "What are you feeling?"
        menu:
            "Relief":
                pass
            "Gratitude":
                wt_image psycho_domme_1_46
                lee.c "Oh, hey.  Oh, wow!  You're really happy to have my attention, aren't you?  Better be careful, or I'll want to do this to you again."
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
        if not lee.has_tag('no_ass_worship'):
            wt_image psycho_domme_1_47
            lee.c "Other than keeping quiet, you haven't been much use to me today.  I don't want to risk having to hear you talk, so the gag stays in, which means you can't use your tongue."
            wt_image psycho_domme_1_48
            lee.c "But I bet you can get your nose into my ass.  Bet it's going to smeel really good to you, to.  Feel free to tell me all about it."
            wt_image psycho_domme_1_49
            "Lee rubs her ass against your face ..."
            wt_image psycho_domme_1_50
            "... the grinds down on you until your nose is as far up her butthole as it can go."
            wt_image psycho_domme_1_47
            "Just as it's starting to get difficult to breath, she pulls away, grinning."
            lee.c "Let me know if you didn't like that.  What's that?  Nothing to say.  Guess I'll assume you like the smell of my butt."
        wt_image psycho_domme_1_4
        "Lee removes your gag."
        lee.c "That's it.  That's all I feel like doing with you today.  Call me sometime if you want to pay me again to shut you up while I watch TV."
        $ lee.gagged_you_count += 1
        change player energy by -energy_very_short notify
    # masturbation scene
    elif not lee.has_tag('special_session_last_time') and lee.relationship_counter > 6 and lee.flogged_you_count > 1 and not lee.has_tag('masturbation_scene_complete'):
        wt_image psycho_domme_1_7
        lee.c "I'm in the mood to hurt you today, loser.  Take off your clothes and lie down.  I'm going to tie you up and make you suffer."
        $ title = "Let her tie you up?"
        menu:
            "Yes":
                add tags 'special_session_last_time' 'masturbation_scene_complete' to lee
            "No":
                wt_image psycho_domme_1_1
                lee.c "Everytime I think you do want to please me, you go and prove you're only interested in what you want.  Not today, loser.  Call me the next time you want to give me money for us to do nothing together."
                jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_13
        "Lee ties you into position and picks up the flogger ..."
        wt_image psycho_domme_1_15
        "... then she pauses and looks at you."
        wt_image psycho_domme_1_14
        lee.c "It's so fucking hot having you like this.  I've been wet all day thinking about doing this to you."
        wt_image psycho_domme_1_19
        lee.c "Scream, bitch."
        wt_image psycho_domme_1_20
        "*THWAAAPPP*"
        player.c "OOOWWWWW!!"
        wt_image psycho_domme_1_16
        "Unfortunately, her arousal at your vulnerability makes her beat you even harder than normal ... *THWAAAPPP* ..."
        wt_image psycho_domme_1_17
        "... and the next few minutes - hours? - are a red blur of pain ... *THWAAAPPP*"
        wt_image psycho_domme_1_18
        "... which leave your entire body feeling like it's on fire ... *THWAAAPPP*"
        wt_image psycho_domme_1_51
        "When you regain your senses, Lee is sitting on the sofa, watching you."
        lee.c "Touch yourself."
        wt_image psycho_domme_1_52
        "You're surprised to discover she loosened the bonds on your arms while you were out of it, allowing you to reach your cock.  You're even more surprised to see her touch herself as you stroke your cock."
        wt_image psycho_domme_1_53
        "Lee watches intently as you make yourself hard.  It's clear that she's very turned on."
        wt_image psycho_domme_1_54
        lee.c "Keep playing with yourself, but don't cum."
        wt_image psycho_domme_1_55
        "The 'don't cum' part is more easily said than done as Lee lowers her damp, smelly cunt ..."
        wt_image psycho_domme_1_56
        "... onto your waiting mouth and tongue."
        wt_image psycho_domme_1_57
        "You couldn't not get her off, even if you wanted to ..."
        wt_image psycho_domme_1_58
        "... as she grinds her cunt down onto your face ..."
        wt_image psycho_domme_1_59
        "... harder and harder."
        wt_image psycho_domme_1_60
        lee.c "FUUCCKKK!!"
        $ title = "Let yourself cum?"
        menu:
            "No, hold back":
                wt_image psycho_domme_1_58
                "It takes everything you have, but you manage to avoid cumming as Lee spasms on your face."
                wt_image psycho_domme_1_54
                lee.c "Oh, wow!  You're still hard.  You must have wanted to cum.  Did you deny yourself just to please me?"
                player.c "Yes, Mistress"
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
                change player energy by -energy_long notify
            "Yes, let yourself go":
                wt_image psycho_domme_1_59
                "As Lee spasms on your face, you get the relief you so desperately need."
                player.c "[player.orgasm_text]"
                wt_image psycho_domme_1_54
                "In her post-orgasm glow, Lee doesn't seem too upset that you disobeyed her.  Or maybe she never really expected you to be able to hold back."
                lee.c "You loser, you came all over yourself.  You've got my cum on your face and your cum on your belly.  Pathetic.  Sexy, but pathetic."
                orgasm notify
        $ lee.pleasure_her_count += 1
        $ lee.orgasm_count += 1
    # handjob scene
    elif not lee.has_tag('special_session_last_time') and lee.relationship_counter > 7 and lee.pegged_you_count > 1 and lee.has_tag('masturbation_scene_complete') and not lee.has_tag('hj_scene_complete'):
        wt_image psycho_domme_1_7
        lee.c "I'm in the mood to rape your ass today, loser.  Take off your clothes and lie down.  I'm going to truss you up like a pig and then stick you."
        $ title = "Let her tie you up?"
        menu:
            "Yes":
                add tags 'special_session_last_time' 'hj_scene_complete' to lee
            "No":
                wt_image psycho_domme_1_1
                lee.c "Everytime I think you do want to please me, you go and prove you're only interested in what you want.  Not today, loser.  Call me the next time you want to give me money for us to do nothing together."
                jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_24
        "As Lee gets you into position, you can tell from the look on her face that she's debating about something.  Finally, she blurts it out."
        wt_image psycho_domme_1_25
        lee.c "Do you ever masturbate, thinking about me fucking your ass?"
        $ title = "What do you tell her"
        menu:
            "Yes, Mistress":
                wt_image psycho_domme_1_61
                lee.c "That's pathetic.  Also, kinda hot."
            "No, Mistress":
                wt_image psycho_domme_1_26
                lee.c "Really?  Why not?"
                $ title = "What do you say?"
                menu:
                    "I don't enjoy being pegged":
                        wt_image psycho_domme_1_61
                        lee.c "But you let me do it to you anyway.  That's kinda hot."
                    "I masturbate thinking about you touching me":
                        wt_image psycho_domme_1_61
                        lee.c "Hmmm, you may be in luck."
                    "I don't need to masturbate":
                        wt_image psycho_domme_1_61
                        lee.c "If you'd told me that when I first met you, I'd think you were a liar.  But, yeah, I can see how you'd have stupid girls lining up for your loser cock.  I hope that doesn't make what I'm about to do with you any less special."
        wt_image psycho_domme_1_26
        "Lee wets her fingers in your mouth ..."
        wt_image psycho_domme_1_27
        "... and gives your ass as much 'preparation' as she ever does."
        wt_image psycho_domme_1_28
        "She's more gentle today, though, as she pushes her phallus inside you."
        wt_image psycho_domme_1_61
        "Then she leans over you and breathlessly whispers to you."
        lee.c "I want to watch you cum while I fuck you."
        wt_image psycho_domme_1_62
        "Her strap-on still up your ass, she pulls off her bra ..."
        wt_image psycho_domme_1_63
        "... spits on your cock ..."
        wt_image psycho_domme_1_64
        "... and jerks you off as she ass-fucks you."
        wt_image psycho_domme_1_65
        "At first she's slow and gentle, with both the handjob and the ass-fucking ..."
        wt_image psycho_domme_1_64
        "... but true to her nature, she's soon insistently tugging on your cock as she pounds into you ..."
        wt_image psycho_domme_1_66
        "... until it's impossible not to cum for her."
        player.c "[player.orgasm_text]"
        wt_image psycho_domme_1_67
        "Lee looks sheepish as she plays idly with the mess you left on yourself."
        lee.c "I didn't do that because you paid me, understood?  You paid me to hurt you, which I did by sticking this dick up your ass.  I only jerked you off because that was what I wanted."
        player.c "Yes, Mistress."
        wt_image psycho_domme_1_9
        "She's unusually quiet as she dresses, unties you, and leaves."
        $ lee.handjob_count += 1
        orgasm notify
    # sex scene
    elif not lee.has_tag('special_session_last_time') and lee.relationship_counter > 9 and lee.has_tag('hj_scene_complete') and not lee.has_tag('sex_scene_complete'):
        add tags 'sex_scene_last_time' to lee
        wt_image psycho_domme_1_7
        lee.c "I'm going to tie you up."
        "She sounds strangely nervous, and its odd she didn't say what she's planning on doing with you.  She usually announces that."
        $ title = "Let her tie you up?"
        menu:
            "Yes":
                add tags 'sex_scene_complete' to lee
            "No":
                wt_image psycho_domme_1_1
                lee.c "Everytime I think you do want to please me, you go and prove you're only interested in what you want.  Not today, loser.  Call me the next time you want to give me money for us to do nothing together."
                jump lee_failed_session
        # continue if didn't jump away
        wt_image psycho_domme_1_9
        "She ties you up, but leaves your arms free.  Then she undresses as she addresses you."
        lee.c "Play with yourself."
        wt_image psycho_domme_1_52
        "Sitting on the sofa in front of you, she rubs herself as she watches you stroke yourself hard."
        wt_image psycho_domme_1_53
        "She's aroused, but there's also a tension on her face, as if she's trying to make up her mind.  Then finally, she speaks."
        lee.c "You're mine to do what I want with, right?"
        $ title = "What do you say?"
        menu:
            "Yes, Mistress":
                wt_image psycho_domme_1_65
                lee.c "Good.  I want something different from you today."
            "Within reason":
                wt_image psycho_domme_1_65
                lee.c "Don't be scared.  I want something different from you today, but you'll survive it."
        "Replacing your hand with her own, she strokes you hard ..."
        wt_image psycho_domme_1_68
        "... then she rubs herself against your cock as she rolls a condom onto it."
        wt_image psycho_domme_1_69
        "The next thing you know she's climbing on top of you ..."
        wt_image psycho_domme_1_70
        "... and riding you."
        wt_image psycho_domme_1_71
        "You're not sure if you'll be allowed to cum, but you know that even if you are, it won't be until after she does, so you try to ignore how good her warm, wet cunt feels sliding up-and-down your shaft."
        wt_image psycho_domme_1_72
        "Fortunately, it doesn't seem like she'll be able to hold out much longer."
        wt_image psycho_domme_1_73
        "Placing a hand between her legs, she frigs herself to orgasm as she rides you."
        wt_image psycho_domme_1_74
        lee.c "FUUCCKKK!!  Cum for me!"
        wt_image psycho_domme_1_71
        player.c "[player.orgasm_text]"
        wt_image psycho_domme_1_75
        lee.c "Mmmmm.  You're not paying me for today's visit.  I'm in charge, so I decide which visits you pay for, and today's you don't."
        $ lee.sex_count += 1
        $ lee.orgasm_count += 1
        change player money by 10
        orgasm notify
    # talk scene - can convert to Domme
    elif lee.has_tag('sex_scene_last_time'):
        rem tags 'sex_scene_last_time' from lee
        wt_image psycho_domme_1_1
        lee.c "We need to talk."
        player.c "About what, Mistress?"
        lee.c "No, don't 'Mistress' me.  Sit down and lets have a normal conversation."
        wt_image psycho_domme_1_76
        "Although she wants to have a 'normal' conversation, she sits above you and puts her feet in your lap.  It's both an endearingly intimate gesture and a subtle show of dominance."
        lee.c "What the fuck are we doing?  What the hell is this even anymore?"
        $ title = "What do you say?"
        menu menu_lee_domme_talk_menu:
            "A business arrangement":
                wt_image psycho_domme_1_1
                lee.c "Seriously?  Is that all I am to you?  Someone you pay to hurt you?"
                $ title = "What do you say?"
                menu:
                    "Yes, I hope that's enough":
                        wt_image psycho_domme_1_1
                        lee.c "Yeah, of course it fucking is.  You're just a loser who needs to pay someone to hurt him.  I don't know what I was thinking.  I'm not in the mood to make you suffer today, loser.  Call me some other time."
                        jump lee_failed_session
                    "No, you're more than that":
                        lee.c "Really?  Then what the fuck is this we're doing together?  What is this to you?"
                        jump menu_lee_domme_talk_menu
            "Two people who both enjoy what the other can offer them":
                wt_image psycho_smile_1
                lee.c "Yeah, I am enjoying what you offer.  I've never had a man let me take charge the way you do, and let me really be in control.  I like it.  I especially like seeing you in pain and knowing 'I caused that, and I can stop it, or I can make it even worse'."
            "What do you want it to be?":
                wt_image psycho_domme_1_1
                lee.c "More than this.  I feel like we have a connection, but I need to know how you feel.  What is this to you?"
                jump menu_lee_domme_talk_menu
        # continue if didn't jump away
        wt_image psycho_domme_1_76
        lee.c "But I don't want to go on the way we have been.  For starters, I don't want to do this for money.  I want to Domme you because I enjoy domming you, not because you're paying me."
        lee.c "And second, I'm in charge, not you.  That means you don't call me anymore.  I call you when I want you to serve me.  You can continue to play with those other silly girls in your life, but when I want you, I expect you to put me first."
        $ title = "Do you agree?"
        menu:
            "Yes, convert her to your Domme":
                wt_image psycho_domme_1_76
                lee.c "From now on, you call me [lee.her_respect_name], understood?"
                $ title = "What do you say?"
                menu menu_lee_pick_her_name_menu:
                    "Yes, [lee.her_respect_name]":
                        pass
                    "Can I keep calling you 'Mistress'?" if not lee.her_respect_name == 'Mistress':
                        lee.c "You've become attached to that term, have you?  Okay, I've become used to you calling me that, and kinda like it, too.  You can keep calling me Mistress."
                        $ lee.her_respect_name = 'Mistress'
                        jump menu_lee_pick_her_name_menu
                    "May I please call you something else?":
                        $ title = "How would you like to refer to her?"
                        $ lee.her_respect_name = renpy.input(_("How would you like to refer to her?"))
                        lee.c "Hmmm, [lee.her_respect_name].  Yes, I like the sound of that.  That's how you'll refer to me from now on."
                        $ title = "What do you say?"
                        jump menu_lee_pick_her_name_menu
                lee.c "And I'm going to call you [lee.your_name].  What do you think of that?"
                $ title = "What do you say?"
                menu menu_lee_pick_your_name_menu:
                    "[lee.your_name] thanks you, [lee.her_respect_name]":
                        pass
                    "Could you keep calling me 'loser'?" if not lee.your_name == 'loser':
                        lee.c "You've become attached to that term, have you?  It does sorta fit you.  Okay, I'll keep calling you loser, loser."
                        $ lee.your_name = 'loser'
                        jump menu_lee_pick_your_name_menu
                    "May I suggest something else?":
                        $ title = "How would you like her to refer to you?"
                        $ lee.your_name = renpy.input(_("How would you like her to refer to you?"))
                        lee.c "Really, [lee.your_name]?  Yes, I can see how that fits you.  From now on, I'll call you [lee.your_name]."
                        $ title = "What do you say?"
                        jump menu_lee_pick_your_name_menu
                wt_image psycho_domme_1_1
                lee.c "Remember, from now on, [lee.your_name], you won't call me.  I'll call you when I want you to serve me.  Understood?"
                player.c "Yes, [lee.her_respect_name].  I'll eagerly await your call."
                wt_image psycho_domme_1_2
                lee.c "You'd better be eager, and you better be available.  I don't intend to play second-fiddle, understood?"
                player.c "Yes, [lee.her_respect_name]."
                wt_image psycho_domme_1_3
                lee.c "Good.  Get on your knees and kiss my foot and swear obedience to me, [lee.your_name]."
                wt_image psycho_domme_1_2
                player.c "I promise to serve and obey you, [lee.her_respect_name]."
                wt_image psycho_smile_1
                lee.c "I look forward to it, [lee.your_name].  I'll call you when I want you."
                call lee_convert_domme from _call_lee_convert_domme
            "No, maintain your current relationship":
                wt_image psycho_domme_1_1
                lee.c "Seriously?  Don't you want more?"
                player.c "I like what we have, you and I.  I don't want to mess it up."
                lee.c "Okay, sure I get that.  Not only are you a pathetic loser who needs to pay someone to hurt him, you're also a scaredy-cat who's afraid of change.  I don't know what I was thinking.  I'm not in the mood to make you suffer today, loser.  Call me some other time."
                jump lee_failed_session
    # normal on-going sessions
    else:
        rem tags 'special_session_last_time' from lee
        wt_image psycho_domme_1_2
        lee.c "So what are you paying me to do to you today, loser?  Pick one thing, I'm not going to hang out here with you all day."
        $ title = "What do you do?"
        menu menu_lee_domme_you_choice_menu:
            "Kneel before you answer her" if not lee.has_tag('kneeling_now'):
                add tags 'kneeling_now' to lee
                wt_image psycho_domme_1_3
                "You're pretty sure Lee starts breathing a little faster when you kneel down in front of her."
                jump menu_lee_domme_you_choice_menu
            "Ask her to slap you":
                call lee_additional_slapping from _call_lee_additional_slapping
            "Ask her to hurt you":
                call lee_additional_flogging from _call_lee_additional_flogging # note: coding in this label will cover off if this is actually being the first flogging
            "Ask her to peg you":
                if lee.pegged_you_count == 0:
                    wt_image psycho_domme_1_7
                    "Lee ties you into the position she wants you ..."
                    wt_image psycho_domme_1_9
                    "... then removes her top and skirt ..."
                    wt_image psycho_domme_1_22
                    "... and puts on her strap-on."
                    call lee_first_pegging from _call_lee_first_pegging_1
                else:
                    call lee_additional_pegging from _call_lee_additional_pegging
            "Ask to worship her ass again" if lee.has_tag('ass_worship_scene_complete') and not lee.has_tag('no_ass_worship'):
                call lee_additional_ass_worship from _call_lee_additional_ass_worship
            "Ask her to gag you again" if lee.has_tag('gag_scene_complete') and lee.gagged_you_count > 0:
                call lee_additional_gagging from _call_lee_additional_gagging
            "Tell her you just want to obey her" if lee.has_tag('kneeling_now'):
                wt_image psycho_smile_1
                "A smile crosses Lee's face, something half-way between sweet and evil."
                sys "Lee's feeling better about your relationship."
                $ lee.relationship_counter += 1
                if lee.flogged_you_count == 0:
                    lee.c "You might regret that.  I'm going to tie you up and hurt you."
                    $ title = "Accept her decision?"
                    menu:
                        "Yes, obey":
                            call lee_additional_flogging from _call_lee_additional_flogging_1 # works for first flogging, too
                        "No, refuse":
                            wt_image psycho_domme_1_1
                            lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                            jump lee_failed_session
                elif lee.pegged_you_count == 0:
                    lee.c "You might regret that.  I'm going to rape your ass."
                    $ title = "Accept her decision?"
                    menu:
                        "Yes, obey":
                            wt_image psycho_domme_1_7
                            "Lee ties you into the position she wants you ..."
                            wt_image psycho_domme_1_9
                            "... then removes her top and skirt ..."
                            wt_image psycho_domme_1_22
                            "... and puts on her strap-on."
                            call lee_first_pegging from _call_lee_first_pegging_2
                        "No, refuse":
                            wt_image psycho_domme_1_1
                            lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                            jump lee_failed_session
                elif lee.flogged_you_count == 1:
                    lee.c "You might regret that.  I'm going to tie you up and hurt you really bad."
                    $ title = "Accept her decision?"
                    menu:
                        "Yes, obey":
                            call lee_additional_flogging from _call_lee_additional_flogging_2
                        "No, refuse":
                            wt_image psycho_domme_1_1
                            lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                            jump lee_failed_session
                elif lee.pegged_you_count == 1:
                    lee.c "You might regret that.  I'm going to rape your stupid ass, again."
                    $ title = "Accept her decision?"
                    menu:
                        "Yes, obey":
                            call lee_additional_pegging from _call_lee_additional_pegging_1
                        "No, refuse":
                            wt_image psycho_domme_1_1
                            lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                            jump lee_failed_session
                else:
                    $ lee.random_number = renpy.random.randint(1, 4)
                    # ass worship
                    if lee.random_number == 1:
                        if lee.has_tag('ass_worship_scene_complete') and not lee.has_tag('no_ass_worship'):
                            lee.c "In that case, get ready to taste the inside of my ass, again."
                            $ title = "Accept her decision?"
                            menu:
                                "Yes, obey":
                                    call lee_additional_ass_worship from _call_lee_additional_ass_worship_1
                                "No, refuse":
                                    wt_image psycho_domme_1_1
                                    lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                                    jump lee_failed_session
                        else:
                            $ lee.random_number = 3
                    # gagging
                    if lee.random_number == 2:
                        if lee.has_tag('gag_scene_complete') and lee.gagged_you_count > 0:
                            lee.c "That's the last fucking thing I want to hear from you today.  I'm going to relax and enjoy myself, and you're going to kneel there and say nothing."
                            $ title = "Accept her decision?"
                            menu:
                                "Yes, obey":
                                    call lee_additional_gagging from _call_lee_additional_gagging_1
                                "No, refuse":
                                    wt_image psycho_domme_1_1
                                    lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                                    jump lee_failed_session
                        else:
                            $ lee.random_number = 4
                    # pegging
                    if lee.random_number == 3:
                        lee.c "You might regret that.  I'm going to rape your stupid ass, again."
                        $ title = "Accept her decision?"
                        menu:
                            "Yes, obey":
                                call lee_additional_pegging from _call_lee_additional_pegging_2
                            "No, refuse":
                                wt_image psycho_domme_1_1
                                lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                                jump lee_failed_session
                    # flogging
                    if lee.random_number == 4:
                        lee.c "You might regret that.  I'm going to tie you up and hurt you really bad."
                        $ title = "Accept her decision?"
                        menu:
                            "Yes, obey":
                                call lee_additional_flogging from _call_lee_additional_flogging_3
                            "No, refuse":
                                wt_image psycho_domme_1_1
                                lee.c "I should've known you were all fucking talk.  Call me again, loser, if you change your mind.  I'm leaving, and I'm keeping your fucking money."
                                jump lee_failed_session
    rem tags 'domme_visit' 'kneeling_now' 'peg_only_today' from lee
    call character_location_return(lee) from _call_character_location_return_753
    wt_image current_location.image
    return

label lee_first_pegging:
    if lee.relationship_counter > 0:
        wt_image psycho_domme_1_24
        "There's a lustful look on Lee's face as she spreads you open."
        wt_image psycho_domme_1_25
        lee.c "I've never raped a man's ass before.  Don't get any ideas about that making you special or anything."
    else:
        wt_image psycho_domme_1_25
        lee.c "I've never raped a man's ass before, but then you're not much of a man."
    wt_image psycho_domme_1_26
    lee.c "Get my fucking fingers wet."
    wt_image psycho_domme_1_27
    "That doesn't make for much of a lubricant, but given Lee's tendencies, you should be happy you got anything at all ..."
    wt_image psycho_domme_1_28
    "... before she starts working the dildo inside you."
    wt_image psycho_domme_1_29
    lee.c "I'm sure you let all the girls and probably most of the boys put their dicks up you, but I'm going to pretend that I'm taking your anal virginity.  You scream to make me think I'm right."
    wt_image psycho_domme_1_30
    "You don't have any choice but to scream when Lee shoves the entire length of the strap-on inside you without warning."
    player.c "OOOWWWWW!!!"
    wt_image psycho_domme_1_29
    lee.c "Oh, you do have a set of lungs on you!  Make that sound again, you fucking bitch."
    wt_image psycho_domme_1_30
    player.c "OOOWWWWW!!!"
    wt_image psycho_domme_1_31
    "Lee pounds away at your ass until she gets tired of listening to the sounds of your discomfort.  You're sure it's more luck than skill that she manages to avoid doing any serious damage to you."
    wt_image psycho_domme_1_26
    lee.c "You got your fucking money's worth today, you pathetic loser.  If you want to pay me to do this to you again, give me a call sometime.  Not this week, though.  Your ass needs time to recover."
    if lee.relationship_counter > 0:
        "She hesitates a moment before continuing."
        lee.c "I didn't hate doing that to you.  I'm still going to charge you if you want me to do it again, though."
        if lee.relationship_counter == 1:
            $ lee.relationship_counter += 1
    $ lee.pegged_you_count += 1
    change player energy by -energy_long notify
    return

label lee_additional_pegging:
    wt_image psycho_domme_1_7
    "Lee ties you into the position she wants you ..."
    wt_image psycho_domme_1_9
    "... then removes her top and skirt ..."
    wt_image psycho_domme_1_22
    "... puts on her strap-on ..."
    wt_image psycho_domme_1_24
    "... and spreads you open."
    wt_image psycho_domme_1_25
    if lee.relationship_counter > 0:
        "There's a lustful look on Lee's face as she moves into position."
    else:
        "Lee looks at you with contempt as she moves into position."
    wt_image psycho_domme_1_26
    lee.c "I'm going to make you my bitch."
    wt_image psycho_domme_1_27
    "After wetting her fingers in your mouth, Lee shoves them into your butt ..."
    wt_image psycho_domme_1_28
    "... and then replaces them with the head of her phallus."
    # check to see if this will be an additional handjob scene
    if lee.has_tag('hj_scene_complete') and lee.relationship_counter > 2:
        $ lee.random_number = renpy.random.randint(1, 6)
    else:
        $ lee.random_number = 6
    # handjob scene
    if lee.random_number < 5:
        wt_image psycho_domme_1_61
        "As she pushes her dick inside you, Lee leans over and whispers to you."
        lee.c "I want to watch you cum for me."
        wt_image psycho_domme_1_62
        "Then she smiles at you as she exposes her breasts ..."
        wt_image psycho_domme_1_63
        "... wets your cock with her spit ..."
        wt_image psycho_domme_1_64
        "... and jerks you off as she pegs you."
        wt_image psycho_domme_1_65
        "She seems to enjoy watching your face as you deal with the dual sensations of her hand insistently pumping your cock while her strap-on insistently reams your ass."
        wt_image psycho_domme_1_64
        "It becomes a bit of a game as you try to hold out while she tries to make you cum ..."
        wt_image psycho_domme_1_66
        "... a game she always wins."
        player.c "[player.orgasm_text]"
        wt_image psycho_domme_1_67
        lee.c "You have a surprisingly nice cock, considering what a pathetic loser you are.  And that's a flattering amount of cum you spilled for me."
        player.c "Thank you, Mistress."
        $ lee.handjob_count += 1
        orgasm notify
    # pain-only scene
    else:
        wt_image psycho_domme_1_29
        lee.c "Go ahead and scream, bitch, so I know how much you love my cock."
        wt_image psycho_domme_1_30
        "You don't have any choice but to scream as Lee shoves the entire length of the strap-on inside you at once."
        player.c "OOOWWWWW!!!"
        wt_image psycho_domme_1_29
        lee.c "Wow, you must really love my cock.  Listen to you scream for it."
        wt_image psycho_domme_1_30
        "She's shockingly rough with your ass, or perhaps not so shockingly, given her proclivities."
        wt_image psycho_domme_1_31
        "She's also in great shape, and pounds away at your ass while varying the angle of penetration, seemingly just to see what makes you scream loudest."
        wt_image psycho_domme_1_29
        player.c "OOOWWWWW!!!"
        wt_image psycho_domme_1_31
        "Eventually you have no more screams to give her, and she tires of the game and pulls out."
        wt_image psycho_domme_1_28
        "Amazingly, as much as your ass hurts, it's neither torn nor bleeding - barely."
        wt_image psycho_domme_1_26
        lee.c "You got your fucking money's worth today, you pathetic loser.  If you want to pay me to do this to you again, give me a call sometime.  Not this week, though.  Your ass needs time to recover."
        if lee.relationship_counter == 1:
            "She hesitates a moment before continuing."
            lee.c "I didn't hate doing that to you.  I'm still going to charge you if you want me to do it again, though."
            sys "Lee's feeling better about your relationship."
            $ lee.relationship_counter += 1
        change player energy by -energy_long notify
    $ lee.pegged_you_count += 1
    return

label lee_additional_slapping:
    if not lee.has_tag('kneeling_now'):
        wt_image psycho_domme_1_2
        lee.c "Get on your fucking knees."
    wt_image psycho_domme_1_5
    "She doesn't hold back.  She stikes you across the cheek with a full swing of her arm ... *SLAPPPP*"
    wt_image psycho_domme_1_4
    lee.c "That's it.  That's all you get unless you ask pretty."
    $ lee.temporary_count = 1
    $ title = "Ask for another?"
    menu menu_lee_additional_slapping_menu:
        "Please, Mistress, may I have another?":
            wt_image psycho_domme_1_5
            "*SLAPPPP*"
            $ lee.temporary_count += 1
            if lee.temporary_count < 25:
                wt_image psycho_domme_1_4
                jump menu_lee_additional_slapping_menu
            else:
                wt_image psycho_domme_1_6
                lee.c "Jesus, my hand's stinging.  That's as much of my attention as you're getting today, and more than you deserve.  Next time you want to pay me to hurt you, let's use something other than my hand."
        "That's enough":
            wt_image psycho_domme_1_6
            if lee.temporary_count < 10:
                lee.c "You pathetic wuss.  My hand's not even hurting.  That's all you get from me today, though.  Call me again if you want to pay me to give you a couple of love taps and then go home."
            elif lee.temporary_count < 20:
                lee.c "Your cheek's red.  Makes you look like you're wearing blush, or were crying like a schoolgirl.  Call me again if you want to pay me to do that to you again."
            else:
                lee.c "About time.  My fucking hand's hurting.  That's as much of my attention as you're getting today, and more than you deserve.  Next time you want to pay me to hurt you, let's use something other than my hand."
    if lee.temporary_count < 10:
        change player energy by -energy_very_short notify
    else:
        change player energy by -energy_short notify
    $ lee.temporary_count = 0
    return

label lee_additional_flogging:
    wt_image psycho_domme_1_7
    "Lee ties you into the position she wants you ..."
    wt_image psycho_domme_1_9
    "... then removes her top and skirt ..."
    wt_image psycho_domme_1_12
    "... and puts on her strap-on before picking up the flogger."
    wt_image psycho_domme_1_13
    "You're pretty sure the strap-on is just for intimidation, and it works - a very phallic symbol that hurting you is going to turn her on."
    if lee.flogged_you_count == 0:
        wt_image psycho_domme_1_16
        "*THWAPPP* ... You wince in pain as Lee brings the flogger down on your chest."
        wt_image psycho_domme_1_17
        "It takes a lot to make a flogger actually hurt and not just sting, but Lee seems determined to do so, swinging it overhand with all her might ... *THWAPPP* ..."
        wt_image psycho_domme_1_18
        "... while circling you and striking your exposed body from every angle ... *THWAPPP*"
        wt_image psycho_domme_1_19
        "You're trying so hard to tolerate the pain she's causing you ... *THWAPPP* ..."
        wt_image psycho_domme_1_20
        "... that you're surprised to hear screaming, and even more surprised to realize it's coming from you ... *THWAPPP*"
        player.c "OOOWWWWW!!!"
        wt_image psycho_domme_1_21
        lee.c "Fuck, that was pathetic.  That cheating tramp took her punishment so much better than you took yours, you wuss."
        wt_image psycho_domme_1_14
        lee.c "That's as much of my attention as you're getting today, and more than you deserve.  Call me again sometime if you want to pay me to hurt you even more."
    else:
        wt_image psycho_domme_1_14
        lee.c "Remember how much it hurt last time?  It's going to be so much worse today."
        wt_image psycho_domme_1_16
        "*THWAPPP* ... You wince in pain as Lee brings the flogger down on your chest."
        wt_image psycho_domme_1_17
        "*THWAPPP*  ... She wasn't kidding about making it hurt more.  She lays into you with all her might, swinging the flogger overhand in long arcs that hurt like hell when they connect."
        wt_image psycho_domme_1_18
        "*THWAPPP* ... For a little while, you think you can tolerate the pain ..."
        wt_image psycho_domme_1_19
        "... then you realize she was just getting warmed up, and she starts really laying into you ... *THWAAAPPP*"
        wt_image psycho_domme_1_20
        "*THWAAAPPP*"
        player.c "OOOWWWWW!!"
        wt_image psycho_domme_1_19
        lee.c "Scream, bitch."
        wt_image psycho_domme_1_20
        "*THWAAAPPP*"
        player.c "OOOWWWWW!!"
        wt_image psycho_domme_1_19
        lee.c "I said fucking scream!"
        wt_image psycho_domme_1_20
        "*THWAAAPPP*"
        player.c "OOWWWW  OOOOWWWWWWW!!"
        wt_image psycho_domme_1_19
        lee.c "LOUDER!!"
        wt_image psycho_domme_1_16
        "You're pretty sure you do scream louder ... you scream until your voice is hoarse and the only thing that exists is the searing pain emanating from the constant, continual blows inflicted on you by Lee."
        # check to see if this will be an additional face-sitting scene
        if lee.has_tag('masturbation_scene_complete') and lee.relationship_counter > 2:
            $ lee.random_number = renpy.random.randint(1, 6)
        else:
            $ lee.random_number = 6
        # face-sitting
        if lee.random_number < 5:
            wt_image psycho_domme_1_51
            "When you regain your senses, Lee is sitting on the sofa, watching you."
            lee.c "Touch yourself."
            wt_image psycho_domme_1_52
            "She loosened the bonds on your arms while you were out of it, allowing you to reach your cock.  She starts to play with herself as you stroke your cock."
            wt_image psycho_domme_1_53
            lee.c "Make yourself as hard as you can get."
            wt_image psycho_domme_1_54
            lee.c "Don't let youself get soft, but don't cum, either."
            player.c "Yes, Mistress."
            wt_image psycho_domme_1_55
            "There's no chance you could go soft when you're presented with Lee's dripping cunt."
            wt_image psycho_domme_1_56
            "Not cumming while you're lapping at her is a lot more difficult ..."
            wt_image psycho_domme_1_57
            "Especially when she starts to grind back onto your face in excitement."
            wt_image psycho_domme_1_58
            "The taste and sound of her arousal has your balls close to the bursting point ..."
            wt_image psycho_domme_1_60
            "... and it gets even harder to hold back when she grabs your hand and makes you pump yourself faster as she cums."
            lee.c "FUUCCKKK!!"
            $ title = "Let yourself cum?"
            menu:
                "No, hold back":
                    wt_image psycho_domme_1_58
                    "It takes everything you have, but you manage to avoid cumming as Lee spasms on your face."
                    wt_image psycho_domme_1_54
                    lee.c "God, I love that you're still hard.  What do you say for me letting you get and stay hard?"
                    player.c "Thank you, Mistress"
                    sys "Lee's feeling better about your relationship."
                    $ lee.relationship_counter += 1
                    change player energy by -energy_long notify
                "Yes, let yourself go":
                    wt_image psycho_domme_1_59
                    "As Lee spasms on your face, you get the relief you so desperately need."
                    player.c "[player.orgasm_text]"
                    wt_image psycho_domme_1_54
                    "In her post-orgasm glow, Lee doesn't seem too upset that you disobeyed her.  Or maybe she never really expected you to be able to hold back."
                    lee.c "What a pathetic loser you are.  You've got my cum on your face and your cum on your belly.  A pathetic, sexy loser."
                    orgasm notify
            $ lee.pleasure_her_count += 1
            $ lee.orgasm_count += 1
        else:
            wt_image psycho_domme_1_21
            "Then suddenly her face is there in front of yours."
            lee.c "Ahh, you're back with us.  You were gone for a while.  I guess I gave you more than your money's worth today.  You won't want that done to you again."
            $ title = "What do you say?"
            menu:
                "You're right, that was too much":
                    wt_image psycho_domme_1_14
                    lee.c "Well, it's over now.  Call me again sometime if you change your mind and want to pay me to hurt you again."
                "It's okay, I enjoyed it":
                    wt_image psycho_domme_1_14
                    lee.c "If you say so.  That's as much of my attention as you're getting today, and more than you deserve.  Call me again sometime if you want to pay me to hurt you even more."
                "I hope you enjoyed doing that to me":
                    if lee.relationship_counter < 2:
                        wt_image psycho_domme_1_14
                        lee.c "Why?  What would it matter to you if I did??"
                        player.c "I enjoy pleasing you.  If hurting me brings you pleasure, I'm glad."
                        wt_image psycho_domme_1_15
                        "Your response throws Lee for a loop, and she's silent for a moment before she responds."
                        lee.c "Yeah, well, this is a business arrangement, remember?  You're paying me to do this to you, and that's as much of my attention as you're getting today.  Call me again sometime if you want to pay me to hurt you even more."
                        sys "Lee's feeling better about your relationship."
                        $ lee.relationship_counter += 1
                    elif lee.relationship_counter < 6:
                        wt_image psycho_domme_1_26
                        lee.c "Yeah, I kinda did, but playtime's over now.  That's as much of my attention as you're getting today, and more than you deserve.  Call me again sometime if you want to pay me to hurt you even more."
                    elif not lee.has_tag('admitted_your_strong'):
                        add tags 'admitted_your_strong' to lee
                        wt_image psycho_domme_1_26
                        lee.c "Yeah, I did.  I was wrong when I called you pathetic and said you weren't strong or tough.  You're amazingly strong.  It's probably time for me to go, though."
                    else:
                        wt_image psycho_domme_1_26
                        lee.c "Yeah, I did.  When I get home, I'm going to finger-fuck myself thinking about hurting you.  I hope that turns you on."
            change player energy by -energy_long notify
    $ lee.flogged_you_count += 1
    return

label lee_additional_ass_worship:
    if not lee.has_tag('kneeling_now'):
        wt_image psycho_domme_1_2
        lee.c "Get on your fucking knees."
    wt_image psycho_domme_1_32
    "Turning around, she pulls up the hem of her skirt."
    wt_image psycho_domme_1_33
    lee.c "Don't just fucking sit there.  Crawl over here and stick your tongue in my ass."
    wt_image psycho_domme_1_36
    "Her hand stops you just before your tongue makes contact with her."
    wt_image psycho_domme_1_37
    lee.c "Your tongue goes in here, and only here.  You haven't earned a taste of my snatch."
    wt_image psycho_domme_1_38
    "Her instructions received, you put your tongue to work in the only hole she'll allow you access to, today."
    wt_image psycho_domme_1_39
    "After a few minutes, you feel her hand on your head, pulling you closer."
    wt_image psycho_domme_1_40
    $ title = "How do you feel about what you're doing?"
    menu:
        "You love it":
            wt_image psycho_domme_1_41
            "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
            wt_image psycho_domme_1_42
            "Your eager tongue works frantically inside her butthole, probing and teasing her as best you can."
            wt_image psycho_domme_1_10
            "And then suddenly, she's cumming."
            lee.c "FUUCCKKK!!"
            wt_image psycho_domme_1_41
            lee.c "Jesus, I'm almost tempted to give you your money back after that.  Almost."
            sys "Lee's feeling better about your relationship."
            $ lee.relationship_counter += 1
        "You do it because she wants you to do it":
            wt_image psycho_domme_1_41
            "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
            wt_image psycho_domme_1_42
            lee.c "You're my bitch, aren't you?  My ass-eating, fucking perv of a bitch."
            wt_image psycho_domme_1_41
            "Lee keeps you there for a while, enjoying the sensation of your tongue in her ass."
            wt_image psycho_domme_1_40
            lee.c "That feels so good I'm almost tempted to give you your money back.  Almost."
        "You love it because she wants you to do it":
            wt_image psycho_domme_1_41
            "Lee's hips start twitching, and even with your nose pressed hard against her butt you can smell her arousal as she impales herself fully on your tongue."
            wt_image psycho_domme_1_42
            "Your eager tongue works frantically inside her butthole, probing and teasing her as best you can."
            wt_image psycho_domme_1_10
            "And then suddenly, she's cumming."
            lee.c "FUUCCKKK!!"
            wt_image psycho_domme_1_41
            lee.c "Jesus, I'm almost tempted to give you your money back after that.  Almost."
            sys "Lee's feeling better about your relationship."
            $ lee.relationship_counter += 1
    wt_image psycho_domme_1_33
    lee.c "Call me the next time you want to pay me to stick your tongue up my ass."
    $ lee.ass_worship_count += 1
    change player energy by -energy_very_short notify
    return

label lee_additional_gagging:
    if not lee.has_tag('kneeling_now'):
        wt_image psycho_domme_1_2
        lee.c "Get on your fucking knees."
    wt_image psycho_domme_1_4
    lee.c "I don't want to hear another fucking thing from you."
    wt_image psycho_domme_1_43
    lee.c "There, that should shut your stupid mouth up."
    wt_image psycho_domme_1_44
    lee.c "You just stay there while I watch some TV.  If you'd like to complain about what I'm watching, well - I guess you fucking can't!"
    wt_image psycho_domme_1_45
    "She really does leave you there while she watches TV."
    wt_image psycho_domme_1_44
    "She leaves you there a very long time, until your joints are aching from holding this position."
    wt_image psycho_domme_1_45
    "Finally, she turns her attention back to you."
    $ title = "What are you feeling?"
    menu:
        "Relief":
            pass
        "Gratitude":
            wt_image psycho_domme_1_46
            lee.c "Oh, hey.  Oh, wow!  You're really happy to have my attention, aren't you?  Better be careful, or I'll want to do this to you again."
            sys "Lee's feeling better about your relationship."
            $ lee.relationship_counter += 1
    if not lee.has_tag('no_ass_worship'):
        wt_image psycho_domme_1_47
        lee.c "Other than keeping quiet, you haven't been much use to me today.  I don't want to risk having to hear you talk, so the gag stays in, which means you can't use your tongue."
        wt_image psycho_domme_1_48
        lee.c "But I bet you can get your nose into my ass.  Bet it's going to smeel really good to you, to.  Feel free to tell me all about it."
        wt_image psycho_domme_1_49
        "Lee rubs her ass against your face ..."
        wt_image psycho_domme_1_50
        "... the grinds down on you until your nose is as far up her butthole as it can go."
        wt_image psycho_domme_1_47
        "Just as it's starting to get difficult to breath, she pulls away, grinning."
        lee.c "Let me know if you didn't like that.  What's that?  Nothing to say.  Guess I'll assume you like the smell of my butt."
    wt_image psycho_domme_1_4
    "Lee removes your gag."
    lee.c "That's it.  That's all I feel like doing with you today.  Call me sometime if you want to pay me again to shut you up while I watch TV."
    $ lee.gagged_you_count += 1
    change player energy by -energy_very_short notify
    return

label lee_failed_session:
    rem tags 'domme_visit' 'kneeling_now' 'peg_only_today' from lee
    $ lee.domme_you_count -= 1
    if lee.relationship_counter > 0:
        sys "Lee's feeling less good about your relationship."
        $ lee.relationship_counter -= 1
    call character_location_return(lee) from _call_character_location_return_754
    wt_image current_location.image
    return

label lee_end_session:
    $ title = "Really send her away?"
    menu:
        "Yes":
            rem tags 'domme_visit' from lee
            call character_location_return(lee) from _call_character_location_return_755
            wt_image current_location.image
        "No":
            pass
    return

label lee_chelsea_domme_you_question:
    $ title = "Ask Lee to treat you like she treated [chelsea.name]?"
    menu:
        "Yes":
            wt_image chubby_lee_2_30
            player.c "Would you do that to me, sometime?"
            lee.c "Do what?"
            player.c "Punish me, like you just punished her."
            wt_image chubby_lee_2_27
            lee.c "Why would I, I'm not mad at you."
            player.c "But you enjoyed it.  And I'd enjoy you doing the same to me."
            lee.c "You're sick.  That wasn't supposed to be fun for her."
            player.c "And it wasn't.  But it was fun for you, and it'd be fun for me."
            wt_image chubby_lee_2_26
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
                            wt_image chubby_lee_2_2
                            lee.c "It'll cost you 10, but not today.  I'm tired after beating on that stupid whore.  But give me a call sometime and I'll take your money and kick your useless ass."
                        "No, not that pathetic":
                            $ lee.domme_you_status = 2
                            wt_image chubby_lee_2_30
                            "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now.  You can contact her if you change your mind."
                "Forget it":
                    $ lee.domme_you_status = 2
                    wt_image chubby_lee_2_30
                    "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now.  You can contact her if you change your mind."
        "Not now":
            $ lee.domme_you_status = 2
            "You can contact her if you change your mind."
        "Never":
            $ lee.domme_you_status = 1
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label lee_contact:
    if lee.diamond_status == 4:
        $ title = "Set up a session between Lee and Diamond?"
        menu:
            "Yes, have them come over (Ends Day)":
                wt_image psycho_contact_2_6
                player.c "Forgive me for disturbing you, [lee.her_respect_name], but Diamond will be ready to serve you now."
                wt_image psycho_contact_2_3
                lee.c "Are you sure?"
                player.c "I'm positive.  Why don't you speak to M, and then bring her here?"
                wt_image psycho_contact_2_2
                lee.c "If she doesn't let me hurt her, I'll take it out on you, instead."
                player.c "Yes, [lee.her_respect_name].  Thank you."
                call lee_diamond_session from _call_lee_diamond_session
            "Not yet":
                pass
    elif lee.diamond_status == 1:
        wt_image psycho_contact_2_6
        player.c "Forgive me for disturbing you, [lee.her_respect_name], but I have a favor to ask you."
        lee.c "Go on."
        player.c "A friend of mine has a sub who he cares deeply for, but who he's been having trouble with.  One difficulty has been getting her to serve other women willingly.  I thought that if you spent time with her, you might be able to help her overcome her concerns."
        if player.has_any_tag('no_bi_content', 'no_sharing_content'):
            wt_image psycho_contact_2_4
            lee.c "That's rather ironic, coming from a boy who won't serve other men to please me."
            player.c "I know, [lee.her_respect_name], and thank you for respecting my limit on that topic, but this is different.  Diamond wants to serve other women to please Master M, she just finds it difficult to get into a proper submissive frame of mind with them."
        wt_image psycho_contact_2_3
        lee.c "If her Master's okay with me working on her, I suppose I could have a chat with her."
        player.c "I've already spoken to him, [lee.her_respect_name], and he is.  He just asked that you not go to rough on her and harm her."
        wt_image psycho_contact_2_2
        lee.c "Well then, I guess you'd better attend the session, too.  That way if I get carried away and want to get too rough on her, I can hurt you, instead.  Send me her contact details and I'll pick her up and then join you.  I need to have a talk with this girl before we do anything else."
        player.c "Yes, [lee.her_respect_name].  Thank you."
        call lee_diamond_session from _call_lee_diamond_session_1
    else:
        if lee.domme_you_status == 2:
            $ title = "Ask Lee the Psycho to dominate you?"
            menu:
                "Yes":
                    wt_image psycho_contact_1_1
                    lee.c "I wasn't expecting to hear from you again."
                    if chelsea.lee_event_status == 2:
                        player.c "I can't stop thinking about what you did to [chelsea.name].  I want you to do that to me, too."
                    else:
                        player.c "I can't stop thinking about what you did to Lauren.  I want you to do that to me, too."
                    wt_image psycho_contact_1_2
                    lee.c "Why would I, I'm not mad at you."
                    player.c "But you enjoyed it.  And I'd enjoy you doing the same to me."
                    wt_image psycho_contact_1_1
                    lee.c "You're sick.  That wasn't supposed to be fun for her."
                    player.c "And it wasn't.  But it was fun for you, and it'd be fun for me."
                    wt_image psycho_contact_1_2
                    lee.c "What the fuck's wrong with you?  You want me to bust your balls and you think that'd be fun?  You're pathetic."
                    $ title = "What do you do?"
                    menu:
                        "Admit you're pathetic":
                            player.c "Yes, Mistress.  I'm pathetic."
                            wt_image psycho_contact_1_3
                            lee.c "How pathetic are you?  I could use a little spending money.  Are you so pathetic that you'd pay me to bust your balls?"
                            $ title = "Are you that pathetic?"
                            menu:
                                "Yes, Mistress, I'll pay you":
                                    $ lee.domme_you_status = 3
                                    wt_image psycho_contact_1_4
                                    lee.c "It'll cost you 10, but not today.  I need some time to decide if you really mean it.  But give me a call later and if I haven't changed my mind, I'll take your money and kick your useless ass."
                                "No, not that pathetic":
                                    $ lee.domme_you_status = 2
                                    "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                        "Forget it":
                            $ lee.domme_you_status = 2
                            "She doesn't seem to be into the domme thing, only revenge.  You let it go, for now."
                "Not now":
                    pass
                "Never (shuts off option)":
                    $ lee.domme_you_status = 1
            wt_image current_location.image
        elif lee.domme_you_status == 3:
            "She said not today.  Try contacting her tomorrow."
        elif lee.domme_you_count == 1 and not dungeon.has_item(floggers):
            "She told you to make sure she had something she could hit you with.  Better visit The Steel Trap to buy some instruments of pain before you call her again."
        else:
            $ title = "Pay Lee 10 to dominate you?"
            menu:
                "Yes":
                    if player.money - player.min_money >= 10:
                        summon lee no_follows
                        add tags 'domme_visit' to lee
                        if lee.has_tag('sex_scene_last_time'):
                            wt_image psycho_domme_1_1
                            "Lee comes straight over, but she brushes straight past you without collecting your money."
                        else:
                            wt_image psycho_domme_1_1
                            "Lee comes straight over, collecting the money from you at the door."
                            if lee.domme_you_count == 0:
                                rem tags 'no_hypnosis' from lee
                                lee.c "You really are willing to pay me to hurt you.  You are one fucked up pathetic loser."
                            change player money by -10 notify
                    else:
                        "You don't have enough money to pay her."
                "Not now":
                    pass
    return

label lee_relationship_status:
    if lee.has_tag('domme'):
        wt_image psycho_contact_2_1
        "[lee.full_name] is your Domme.  She doesn't live with you, and she lets you play with other women, but she expects you to be there for her when she wants you."
        if lee.relationship_counter == 4:
            "Lee is very happy with your relationship."
        elif lee.relationship_counter == 3:
            "Lee is happy with your relationship."
        elif lee.relationship_counter == 2:
            "Lee is expects you to be there when she calls."
        else:
            "Lee is unhappy with your relationship.  You'd better make time for her the next time she calls, or she may call your arrangement off."
    elif lee.domme_you_status == 4:
        wt_image psycho_contact_1_1
        if lee.relationship_counter > 7:
            "Lee dommes you for money.  She's coming around to accepting that she enjoys the time she spends with you."
        elif lee.relationship_counter > 5:
            "Lee dommes you for money.  She still thinks of this as a business relationship, but she enjoys spending time with you more than she lets on."
        elif lee.relationship_counter > 1:
            "Lee dommes you for money.  This is a business relationship for her, but spending time with you is triggering feelings in her that she hasn't quite come to terms with."
        else:
            "Lee dommes you for money.  This is a business relationship for her."
    wt_image current_location.image
    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_lee:
    if lee.has_tag('need_butt_plug'):
        rem tags 'need_butt_plug' from lee
        lee.c "Good boy.  I'll look forward to using this on you."
        give 1 butt_plug from player to lee notify
    else:
        "You should save the butt plug for a client."
    return

# Give Chastity Belt
label give_cb_lee:
    if lee.has_tag('need_chastity_belt'):
        rem tags 'need_chastity_belt' from lee
        lee.c "Good boy.  I'll look forward to using this on you."
        give 1 chastity_belt from player to lee notify
    else:
        "You should save this for a current client."
    return

# Give Dildo
label give_di_lee:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_lee:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_lee:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_lee:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_lee:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_lee:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_lee:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_lee:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_lee:
  "You should try this on someone else."
  return

# Lee's Collar
label lpc_examine:
    wt_image lpc_image
    if lee.has_tag('domme'):
        "The collar [lee.her_respect_name] gave you and sometimes puts you in."
    else:
        "The collar Lee gave you when she was your Domme."
        $ title = "Keep it?"
        menu:
            "Yes":
                pass
            "No":
                rem 1 lee_collar from player notify
    return


########### TIMERS ###########
## Common Timers
# Start Day
label lee_start_day:
    # count down to next call if not Friday and Lee is your Domme
    if lee.has_tag('domme') and day < 5:
        $ lee.next_call_countdown -= 1
        if lee.next_call_countdown < 0:
            $ lee.temporary_count = 1
            $ lee.next_call_countdown = renpy.random.randint(4, 10)
            wt_image phone_1
            "Your phone is ringing."
            if lee.has_tag('need_butt_plug'):
                wt_image psycho_contact_2_3
                lee.c "I'm in the mood to play, [lee.your_name].  Do you have a butt plug for me to use on you?"
                if player.has_item(butt_plug):
                    $ title = "Give [lee.her_respect_name] the butt plug?"
                    menu:
                        "Yes":
                            rem tags 'need_butt_plug' from lee
                            player.c "Yes, [lee.her_respect_name].  I have it."
                            give 1 butt_plug from player to lee notify
                        "No":
                            wt_image psycho_contact_2_6
                            player.c "I'm sorry, [lee.her_respect_name].  I don't have that, yet."
                            $ lee.temporary_count = 0
                else:
                    wt_image psycho_contact_2_6
                    player.c "I'm sorry, [lee.her_respect_name].  I don't have that, yet."
                    $ lee.temporary_count = 0
                if lee.temporary_count == 0:
                    $ lee.next_call_countdown = 2
                    $ lee.relationship_counter -= 1
                    wt_image psycho_contact_2_2
                    lee.c "I'll call again in a few days, and you better have that butt plug for me then."
            elif lee.has_tag('need_chastity_belt'):
                wt_image psycho_contact_2_3
                lee.c "I'm in the mood to play, [lee.your_name].  Do you have a cock cage for me to use on you?"
                if player.has_item(chastity_belt):
                    $ title = "Give [lee.her_respect_name] the chastity belt?"
                    menu:
                        "Yes":
                            rem tags 'need_chastity_belt' from lee
                            player.c "Yes, [lee.her_respect_name].  I have it."
                            give 1 chastity_belt from player to lee notify
                        "No":
                            wt_image psycho_contact_2_6
                            player.c "I'm sorry, [lee.her_respect_name].  I don't have that, yet."
                            $ lee.temporary_count = 0
                else:
                    wt_image psycho_contact_2_6
                    player.c "I'm sorry, [lee.her_respect_name].  I don't have that, yet."
                    $ lee.temporary_count = 0
                if lee.temporary_count == 0:
                    $ lee.next_call_countdown = 2
                    $ lee.relationship_counter -= 1
                    wt_image psycho_contact_2_2
                    lee.c "I'll call again in a few days, and you better have that cock cage for me then."
            elif lee.has_tag('need_leash'):
                wt_image psycho_contact_2_3
                lee.c "I'm in the mood to play, [lee.your_name].  Did you get a leash for me?"
                if player.has_item(leash):
                    rem tags 'need_leash' from lee
                    player.c "Yes, [lee.her_respect_name].  I have it."
                else:
                    wt_image psycho_contact_2_6
                    player.c "I'm sorry, [lee.her_respect_name].  I don't have that, yet."
                    $ lee.temporary_count = 0
                if lee.temporary_count == 0:
                    $ lee.next_call_countdown = 2
                    $ lee.relationship_counter -= 1
                    wt_image psycho_contact_2_2
                    lee.c "I'll call again in a few days, and you better have that cock cage for me then."
            # standard intro
            else:
                wt_image psycho_contact_2_3
                lee.c "I'm in the mood to play, [lee.your_name]."
            # if visit not cancelled due to lack of item
            if lee.temporary_count == 1:
                $ lee.temporary_count = 0
                $ title = "Make yourself available to her?"
                menu:
                    "Yes":
                        call lee_domme_event from _call_lee_domme_event
                    "Not today":
                        $ lee.relationship_counter -= 1
                        if lee.relationship_counter < 1:
                            sys "You've put her off quite often.  If you do so again, she'll likely break things off."
                            $ title = "Reconsider?"
                            menu:
                                "Yes, make yourself available to her":
                                    $ lee.relationship_counter += 1 # to offset prior loss
                                    call lee_domme_event from _call_lee_domme_event_1
                                "No, let her break things off":
                                    wt_image psycho_contact_2_4
                                    lee.c "This isn't working out for me.  Thank you for helping me understand who I truly am, but now that I know what I want, I also understand I want someone who prioritizes me more than you do.  Good-bye."
                                    $ chelsea.lee_event_status = 0
                                    $ lee.domme_you_status = 1
                                    call unconvert(lee, 'domme') from _call_unconvert_86
                                    call convert(lee, 'unavailable') from _call_convert_198
                        elif lee.relationship_counter < 2:
                            if lee.next_call_countdown > 6:
                                $ lee.next_call_countdown -= 3 # shorten time between calls if you've been putting her off
                            wt_image psycho_contact_2_6
                            lee.c "You've been unavailable a lot lately.  I expect you to serve me when I want to be served, not when you want to serve.  I'll find something else to do today, but don't put me off again, [lee.your_name]."
                        else:
                            if lee.next_call_countdown > 5:
                                $ lee.next_call_countdown -= 2 # shorten time between calls if you've been putting her off
                            wt_image psycho_contact_2_2
                            lee.c "Okay, I understand you're busy.  I'll find something else to do today, but don't make a habit of putting other things ahead of me, [lee.your_name]."
    return

label lee_domme_event:
    $ lee.training_session()
    ## SCENE SELECTION
    $ lee.domme_outfit += 1
    if lee.domme_outfit > 6:
        $ lee.domme_outfit = 1
    # skip chasity device scene if that's a limit
    if lee.domme_outfit == 3 and lee.has_tag('no_chastity_belt'):
        $ lee.domme_outfit = 4
    # skip leash event if that's a limit
    if lee.domme_outfit == 5 and lee.has_tag('no_leash'):
        $ lee.domme_outfit += 1
    # check to see if threesome scene proceeds
    if lee.domme_outfit == 6:
        if lee.has_tag('no_sharing_content'):
            $ lee.domme_outfit = 1
        # requires that you let Hannah torture you
        elif bethany.torture_count == 4 or bethany.torture_count == 6:
            pass
        else:
            $ lee.domme_outfit = 1
    ## INTRODUCTION
    wt_image psycho_contact_2_5
    if lee.domme_outfit == 6 or lee.diamond_status == 5:
        lee.c "I'm not going to you today, you're coming to me.  I'm sending you the address.  Don't keep me waiting."
        player.c "Yes, [lee.her_respect_name].  I'll be there right away"
    elif lee.domme_outfit == 2 and not lee.has_tag('butt_plug_scene_pending'):
        lee.c "Be on your knees in your dungeon with your butt plug in your ass when I get there."
        player.c "Yes, [lee.her_respect_name].  I'll be here and waiting for you on my knees and wearing my butt plug."
        call forced_movement(dungeon) from _call_forced_movement_1027
        summon lee no_follows
    elif lee.domme_outfit == 5:
        lee.c "Put on your collar and leash and wait for me in your dungeon.  And put in a gag, too.  Pets can't talk."
        player.c "Yes, [lee.her_respect_name].  I'll be here and waiting for you like a good pet."
        call forced_movement(dungeon) from _call_forced_movement_1028
        summon lee no_follows
    else:
        lee.c "Be on your knees in your dungeon when I get there."
        player.c "Yes, [lee.her_respect_name].  I'll be here and waiting for you on my knees."
        call forced_movement(dungeon) from _call_forced_movement_1029
        summon lee no_follows
    if lee.relationship_counter < 4: # max level is 4, meaning most times you can put her off is 4 in a row
        $ lee.relationship_counter += 1
        if lee.relationship_counter < 1: # possible if took time getting item for her
            $ lee.relationship_counter = 1
    ## SCENES
    # event with M
    if lee.diamond_status == 5:
        $ lee.domme_outfit -= 1 # so as to stay on regular number rotation despite this extra scene
        if lee.domme_bi_scene > 0:
            "The address she sent you isn't Hannah's this time.  You're not sure whose place this is, but given the expensive neighborhood its located in, you suspect it's not Lee's house."
        else:
            "You don't recognize the address, but given the expensive neighborhood its located in, you suspect it's not Lee's house."
        call forced_movement(outdoors) from _call_forced_movement_1030
        summon diamond no_follows
        summon master_m no_follows
        wt_image psycho_m_1_1
        "It seems to be M's house and Lee is here, sitting on his lap."
        lee.c "After you introduced us through Diamond, I've been chatting with M. He's owned a lot of slaves over the years, and has been telling me about what he's learned. I'm going to thank him for sharing his experience, but since you'll be the one who primarily benefits from him helping make me a better Domme, I thought you should be here to watch my 'thank you'."
        $ title = "Stay?"
        menu:
            "Yes":
                wt_image psycho_m_1_2
                "Your Domme gets down on her knees and starts to provide M with her 'thank you'."
                wt_image psycho_m_1_3
                if lee.has_tag('no_bi_content'):
                    lee.c "I'd have him thank you more directly, M, but he has a thing about not wanting to suck men's dicks."
                    $ lee.diamond_status = 7
                else:
                    lee.c "In fact, you should thank him yourself by getting him hard before he fucks me."
                    $ title = "What do you do?"
                    menu:
                        "Suck his cock":
                            $ lee.diamond_status = 8
                        "Refuse":
                            wt_image psycho_m_1_2
                            if lee.domme_bi_scene > 2 and not lee.has_tag('no_bi_content'):
                                lee.c "That's odd.  He's usually a very obedient cocksucker.  Maybe he's shy because he knows you?  I suppose that could be a type of limit."
                            else:
                                lee.c "Hmmm, it seems maybe this may be one of his limits."
                            $ lee.diamond_status = 7
                # don't suck his cock
                if lee.diamond_status == 7:
                    wt_image psycho_m_1_2
                    master_m.c "Some limits are hard limits, but others can change over time.  If having him serve men is important to you, don't give up on him - he may come around for you over time."
                    wt_image psycho_m_1_4
                    if master_m.lent_him_a_slave > 1:
                        "You might have to have a talk with M about what sort of advice he's giving Lee, but for the moment you're curious to see if he subjects her to the same sort of cocksucking-jaw-torture he inflicted on [master_m.name_of_your_slave_loaned]."
                        wt_image psycho_m_1_5
                        "If he's thinking about doing so, he's interrupted as Lee tries to force the issue."
                    else:
                        "You might have to have a talk with M about what sort of advice he's giving Lee, but in the meantime, you watch jealously as she showers his cock with an affection she rarely gives yours."
                        wt_image psycho_m_1_5
                        "It seems, however, that she intends to give him more than a blowjob."
                    wt_image psycho_m_1_6
                    lee.c "Show [lee.your_name] how a real man fucks a woman."
                    wt_image psycho_m_1_7
                    "*smack*"
                    lee.c "Hey?!"
                    wt_image psycho_m_1_5
                    master_m.c "I didn't give you permission to stop sucking my cock."
                    wt_image psycho_m_1_4
                    "Lee goes back to work on M's dick, and you're surprised to see she's sucking him with greater enthusiasm ..."
                    wt_image psycho_m_1_2
                    "... and seemingly actively seeking signs of his approval."
                    wt_image psycho_m_1_5
                    master_m.c "You want something now, Lee?"
                    lee.c "I want you to fuck me and show [lee.your_name] how a real man fucks a woman."
                    wt_image psycho_m_1_6
                    master_m.c "I will, but you need to accept a spanking as punishment for taking your mouth off my cock without permission."
                    lee.c "Yes, M, I understand.  Please spank me to punish me, then fuck me hard."
                    wt_image psycho_m_1_8
                    "Trying to train Lee not to top from the bottom would likely be a multi-day affair, and M seems content with the opportunity to slap her ass as he enters her ... *smack* ... *smack* ... *smack* ... *smack* ... *smack*"
                    lee.c "Ow!!  Oohhh!"
                    wt_image psycho_m_1_9
                    lee.c "Fuck, [lee.your_name], his cock feels so good inside me!  If you could fuck me like this, I wouldn't need to hurt you so often to get off."
                    wt_image psycho_m_1_10
                    "You're pretty sure her commentary is intended only to humiliate you, but the intensity of her orgasm as she cums is surprisingly strong."
                    lee.c "FUUCCCKKKKK!!!"
                    wt_image psycho_m_1_11
                    "M seems to enjoy his orgasm, too, as he empties his load on Lee's face."
                    lee.c "Mmmmm, come here, [lee.your_name], and make yourself useful.  Clean off my face so I don't make a mess on M when I kiss him."
                    $ title = "Lick his cum off her face?"
                    menu:
                        "Yes, do as [lee.her_respect_name] wants":
                            wt_image psycho_m_1_12
                            lee.c "Thank you so much, M.  I'd have [lee.your_name] kiss you, too, but I'm sure you don't want to be tasting your cum on his mouth."
                        "No, refuse":
                            master_m.c "He's full of limits, this one."
                            lee.c "No kidding.  Oh well, his loss.  Your cum is delicious, M, the way a real man's cum always taste - salty, sexy and powerful."
                # do suck his cock
                else:
                    wt_image psycho_m_1_13
                    if master_m.lent_him_a_slave > 1:
                        "You're a little worried that M might subject you to the same cocksucking-jaw-torture he inflicted on [master_m.name_of_your_slave_loaned]."
                        wt_image psycho_m_1_14
                        "Lee intervenes, however, and saves your jaw from the agony M might otherwise have put it through."
                    else:
                        "M is already hard from Lee's mouth, and doesn't get any softer as he shifts his dick to you."
                        wt_image psycho_m_1_14
                        "You can feel his cock throbbing inside you, and you wonder if you're about to get a mouthful of jizz, when Lee intervenes."
                    wt_image psycho_m_1_6
                    lee.c "He has you hard enough, M.  Show [lee.your_name] how a real man fucks a woman."
                    wt_image psycho_m_1_7
                    "*smack*"
                    lee.c "Hey?!"
                    wt_image psycho_m_1_6
                    master_m.c "If you want my cock, ask politely."
                    lee.c "Please may I have your cock, Master M?  I want you to fuck me and show [lee.your_name] how a real man fucks a woman."
                    wt_image psycho_m_1_7
                    master_m.c "I will, but you need to accept a spanking as punishment for interrupting the blowjob I was receiving from your sub."
                    lee.c "Yes, M, I understand.  Please spank me to punish me, then fuck me hard."
                    wt_image psycho_m_1_8
                    "Trying to train Lee not to top from the bottom would likely be a multi-day affair, and M seems content with the opportunity to slap her ass as he enters her ... *smack* ... *smack* ... *smack* ... *smack* ... *smack*"
                    lee.c "Ow!!  Oohhh!"
                    wt_image psycho_m_1_9
                    lee.c "Fuck, [lee.your_name], his cock feels so good inside me!  If you could fuck me like this, I wouldn't need to hurt you so often to get off."
                    wt_image psycho_m_1_10
                    "You're pretty sure her commentary is intended only to humiliate you, but the intensity of her orgasm as she cums is surprisingly strong."
                    lee.c "FUUCCCKKKKK!!!"
                    wt_image psycho_m_1_11
                    "M seems to enjoy his orgasm, too, as he empties his load on Lee's face."
                    lee.c "Mmmmm, come here, [lee.your_name], and clean off my face so I don't make a mess on M when I kiss him."
                    wt_image psycho_m_1_12
                    lee.c "Thank you so much, M.  I'd have [lee.your_name] kiss you, too, but I'm sure you don't want to be tasting your cum on his mouth."
                    $ player.male_sex_count += 1
            "No":
                $ lee.diamond_status = 6
                player.c "I'm sorry, [lee.her_respect_name], I'm not comfortable with this."
                "She seems disappointed, but let's you go."
        if lee.next_call_countdown > 5:
            $ lee.next_call_countdown -= 2 # shorten time until next visit
        call forced_movement(living_room) from _call_forced_movement_1031
        call character_location_return(master_m) from _call_character_location_return_756
        change player energy by -energy_long notify
    # butt plug introduction scene
    elif lee.has_tag('butt_plug_scene_pending'):
        rem tags 'butt_plug_scene_pending' from lee
        add tags 'butt_plug_scene_complete' to lee
        $ lee.domme_outfit -= 1 # so as to stay on regular number rotation despite this extra scene
        wt_image psycho_domme_3_1
        "Lee marches past you on arrival and takes a seat."
        wt_image psycho_domme_3_2
        lee.c "Well don't just kneel there.  Bring me your butt plug."
        wt_image psycho_domme_3_3
        lee.c "I hope this was the biggest size they had for sale.  I want your ass trained to give me easy access.  Lie over my lap and we'll try it out."
        wt_image psycho_domme_3_4
        "Lee apparently sees no more purpose for lubricant with your butt plugs than she does with her strap-on ..."
        wt_image psycho_domme_3_5
        "... which makes insertion both difficult ..."
        wt_image psycho_domme_3_6
        "... and painful."
        player.c "Oowww!!"
        wt_image psycho_domme_3_7
        "Eventually she gets the plug all the way inside you, while making the process as painful as it could be without actually harming you."
        wt_image psycho_domme_3_8
        lee.c "This better work.  If your ass doesn't become better suited for my enjoyment, I'll be very disappointed in you, [lee.your_name]."
        wt_image psycho_domme_3_9
        lee.c "You need to be punished for having an ass that's so difficult for me to enjoy."
        wt_image psycho_domme_3_10
        "*SMACKKK*"
        player.c "Ooww!  I'm sorry, [lee.her_respect_name]!"
        wt_image psycho_domme_3_11
        lee.c "You're not sorry yet, but you will be soon, [lee.your_name]."
        wt_image psycho_domme_3_12
        "*SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK* ... "
        wt_image psycho_domme_3_13
        "She tattoos your ass until it's a firey shade of red ..."
        wt_image psycho_domme_3_14
        "... then she gives you three more, extra hard ... *SMAACCKKK* ... *SMAACCKKK* ... *SMAACCKKK*"
        wt_image psycho_domme_3_6
        player.c "OOOOWWWWWWW!!!"
        wt_image psycho_domme_3_15
        lee.c "From now on, you wear your butt plug every night while you sleep.  I want your ass stretched to open wide for my amusement."
        wt_image psycho_domme_3_16
        lee.c "Kiss my boot and promise you'll obey me, [lee.your_name]."
        wt_image psycho_domme_3_17
        player.c "Yes, [lee.her_respect_name].  I promise to wear my butt plug for you every night while I sleep."
        wt_image psycho_domme_3_18
        lee.c "Good, but since your ass is still defective, I'll need to use one of your other body parts to amuse myself today."
        wt_image psycho_domme_3_19
        lee.c "Stick out your tongue."
        wt_image psycho_domme_3_20
        "You extend your tongue as far as you can while Lee rubs herself against it while holding your head firmly in place."
        wt_image psycho_domme_3_21
        "All she wants from you is to be a tongue for her to fuck herself with, and a mouth to swallow her juices as she cums."
        wt_image psycho_domme_3_22
        lee.c "FUUCCKKK!!"
        wt_image psycho_domme_3_1
        lee.c "That's all for today, [lee.your_name].  Remember to put your butt plug back in at night.  Your ass is mine, even when I'm not around."
        player.c "Yes, [lee.her_respect_name].  Thank you."
        $ lee.pleasure_her_count += 1
        $ lee.orgasm_count += 1
        change player energy by -energy_long notify
    # worshipping and pegging
    elif lee.domme_outfit == 1:
        wt_image psycho_domme_2_1
        "Lee smiles as she arrives to find you waiting for her on your knees, as you promised."
        if not player.has_item(lee_collar):
            lee.c "I have something for you, to celebrate our new relationship."
            wt_image psycho_domme_2_2
            "She steps behind you and buckles a collar around your neck."
            player.c "Thank you, [lee.her_respect_name]."
            add 1 lee_collar to player notify
        wt_image psycho_domme_2_3
        "Taking a seat, your biker-chick Domme extends her long, powerful legs towards you."
        wt_image psycho_domme_2_4
        lee.c "Worship"
        wt_image psycho_domme_2_5
        if lee.your_name == 'bootlick':
            "From the name she gave you, this is important to her, and you want her to be pleased with you.  You shower her boot with the affection you feel towards her ..."
        else:
            "You shower her boot with the affection you feel towards her ..."
        wt_image psycho_domme_2_6
        "... nuzzling your face against it ..."
        wt_image psycho_domme_2_7
        "... kissing it respectfully ..."
        wt_image psycho_domme_2_8
        "... then licking the soles clean."
        wt_image psycho_domme_2_9
        lee.c "You may lick the side of my boot, but only the boot - don't touch my leg."
        wt_image psycho_domme_2_10
        player.c "Thank you, [lee.her_respect_name]."
        wt_image psycho_domme_2_11
        lee.c "That's far enough.  Spread your legs."
        wt_image psycho_domme_2_12
        "Lee wraps a rope tightly around your cock and balls."
        wt_image psycho_domme_2_13
        lee.c "Is that tight enough to hurt?"
        player.c "Yes, [lee.her_respect_name]"
        wt_image psycho_domme_2_14
        lee.c "What excites you most?  Worshipping me, the touch of my hand on your cock, or when I hurt you?"
        $ title = "What do you tell her?"
        menu menu_lee_domme_event_1_menu:
            "Worshipping you":
                wt_image psycho_domme_2_15
                "*SLAPPPP*"
                lee.c "It excites you when you lick my boots, does it?"
                wt_image psycho_domme_2_16
                "*SLAPPPP*"
                lee.c "I bet it excites you when I let you lick other body parts, too."
            "Your touch":
                wt_image psycho_domme_2_17
                lee.c "You enjoy my hand stroking your cock ..."
                wt_image psycho_domme_2_18
                "... and teasing the pre-cum from your balls?"
                wt_image psycho_domme_2_19
                lee.c "But my hand can also squeeze and hurt your cock ..."
                player.c "Oowww!!"
                wt_image psycho_domme_2_15
                "*SLAPPPP*"
                lee.c "... not to mention hurting your face."
                wt_image psycho_domme_2_16
                "*SLAPPPP*"
                lee.c "And in any event, I'm not interested in touching you right now.  But I will let you touch me, sort of."
            "When you hurt me":
                wt_image psycho_domme_2_15
                "*SLAPPPP*"
                lee.c "Lucky for you, I love seeing you wince in pain."
                wt_image psycho_domme_2_16
                "*SLAPPPP*"
                lee.c "But I also enjoy it when you worship me."
            "Pleasing you":
                wt_image psycho_domme_2_15
                "*SLAPPPP*"
                lee.c "I know that.  Answer the question I asked."
                wt_image psycho_domme_2_14
                lee.c "What excites you most?  Worshipping me, the touch of my hand on your cock, or when I hurt you?"
                jump menu_lee_domme_event_1_menu
        # first time, reconfirm that will ass worship
        if not lee.has_any_tag('no_ass_worship', 'will_ass_worship'):
            wt_image psycho_domme_2_20
            lee.c "Worship my ass."
            $ title = "What do you do?"
            menu:
                "Worship her":
                    add tags 'will_ass_worship' to lee
                "Ask for this to be a limit":
                    add tags 'no_ass_worship' to lee
                    wt_image psycho_domme_2_21
                    lee.c "And here I thought you liked the taste of every part of me?  Okay, I'll respect your limit."
        # else intro to ass worship
        elif lee.has_tag('will_ass_worship'):
            wt_image psycho_domme_2_20
            lee.c "Worship my ass."
        # finish ass worship if open
        if lee.has_tag('will_ass_worship'):
            wt_image psycho_domme_2_22
            "She guides your head into the crack between her asscheeks ..."
            wt_image psycho_domme_2_23
            "... and holds it firmly in place as you lick.  You can't taste her ass through her panties, but you can certainly smell it, and Lee seems to enjoy your attention as she wiggles her butt back-and-forth against your face."
        # if won't ass worship
        else:
            wt_image psycho_domme_2_24
            lee.c "Since you find my ass repugnant, I'll let you worship me here, but you may only lick my thighs.  You can smell my cunt, but no touching."
            wt_image psycho_domme_2_25
            "The heady aroma of her arousal makes the prohibition against touching her sex an ordeal, but you content yourself with the taste of her inner thighs."
        wt_image psycho_domme_2_15
        "*SLAPPPP*"
        lee.c "Enough worship.  Lie down, I want to fuck you now."
        wt_image psycho_domme_2_26
        "As you get into posiiton, Lee gets into her strap-on."
        wt_image psycho_domme_2_27
        if lee.has_item(butt_plug):
            "She's still a believer in minimal lube.  Even with your butt plug training, that makes her entrance more painful than necessary ..."
        else:
            "She's still a believer in minimal lube, which makes her entrance more painful than necessary ..."
        wt_image psycho_domme_2_28
        player.c "Owww!!"
        wt_image psycho_domme_2_29
        "... but Lee seems to prefer it that way."
        wt_image psycho_domme_2_30
        "She reams your ass, hard and rough ..."
        wt_image psycho_domme_2_31
        "... then she grabs your cock and uses it for leverage ..."
        wt_image psycho_domme_2_32
        "... and fucks you even harder ..."
        wt_image psycho_domme_2_33
        "... until she becomes overwhelmed by the need to use your body in a different way."
        $ lee.random_number = renpy.random.randint(1, 8)
        # sex
        if lee.random_number < 5:
            wt_image psycho_domme_2_34
            "Pulling out of your ass, she strokes you fully erect ..."
            wt_image psycho_domme_2_35
            "... then she climbs on top ..."
            wt_image psycho_domme_2_36
            "... settles onto your cock ..."
            wt_image psycho_domme_2_37
            "... and rides you roughly ..."
            wt_image psycho_domme_2_38
            "... to an intense orgasm ..."
            wt_image psycho_domme_2_39
            lee.c "FUUCCKKK!!"
            if lee.random_number < 3:
                wt_image psycho_domme_2_40
                "... which unfortunately, you're not allowed to experience yourself."
                wt_image psycho_domme_2_41
                lee.c "I can feel your cock throbbing against me, but just lie here and be happy I let you be inside me when I came."
                player.c "Thank you, [lee.her_respect_name]."
                change player energy by -energy_long notify
            else:
                wt_image psycho_domme_2_42
                "... which she graciously allows you to experience yourself."
                lee.c "Cum for me, [lee.your_name]!"
                wt_image psycho_domme_2_43
                player.c "[player.orgasm_text]"
                wt_image psycho_domme_2_41
                player.c "Thank you, [lee.her_respect_name]."
                lee.c "You're welcome, [lee.your_name], but don't start thinking I'll let you cum every time.  I might never let you cum inside me again."
        # facesitting
        else:
            wt_image psycho_domme_2_44
            "Pulling out of your ass, she removes the strap-on and her panties ..."
            wt_image psycho_domme_2_45
            "... then she straddles your face ..."
            wt_image psycho_domme_2_46
            "... and grinds herself to orgasm against it."
            wt_image psycho_domme_2_39
            lee.c "FUUCCKKK!!"
            wt_image psycho_domme_2_47
            lee.c "Look how hard and throbbing your cock is.  I think you'd cum if I so much as breathed on your dick.  Thank me for giving you such a nice erection, [lee.your_name]."
            wt_image psycho_domme_2_48
            player.c "Thank you for giving me a painfully-hard erection, [lee.her_respect_name]."
        if not lee.has_tag('butt_plug_scene_complete'):
            add tags 'butt_plug_scene_pending' to lee
            if not lee.has_item(butt_plug):
                add tags 'need_butt_plug' to lee
                "Lee stops and addresses you once more before leaving."
                wt_image psycho_domme_2_1
                lee.c "It's too much work getting my dick into your tight ass.  We need to stretch it out.  Get me a butt plug for me to use on you the next time I visit, [lee.your_name]."
                "If she wanted to penetrate you more easily, she could just start using more lubricant, but she seems to have her mind set on modifying your ass to suit her preferences, so you'd best visit The Steel Trap and buy a butt plug for her to use on you."
    # Note: scene 2 must be a pegging scene and reference butt plug
    elif lee.domme_outfit == 2:
        wt_image psycho_domme_4_1
        "Lee gags you tightly with a rope when she arrives."
        wt_image psycho_domme_4_2
        lee.c "Mmmm, I like you like this, [lee.your_name].  Waiting, kneeling, unable to speak.  I may leave you here all day."
        wt_image psycho_domme_4_3
        "She doesn't actually leave you, but she does ignore you; not for the full day, but long enough for your knees to ache.  When she finally turns back to you, she feigns displeasure."
        wt_image psycho_domme_4_2
        lee.c "You're disappointing me, [lee.your_name]."
        wt_image psycho_domme_4_4
        lee.c "Why is your cock so soft?"
        wt_image psycho_domme_4_5
        lee.c "Is the sight of my body not enough to arouse you?"
        wt_image psycho_domme_4_6
        lee.c "Is the smell of me not enough to excite you?"
        wt_image psycho_domme_4_7
        lee.c "You can't expect me to have fun hurting you while you're in this condition."
        wt_image psycho_domme_4_8
        lee.c "That's better.  Now I feel more appreciated."
        wt_image psycho_domme_4_9
        lee.c "And now I have a more enjoyable target to crop."
        wt_image psycho_domme_4_10
        "*THWAPPP* ... *THWAPPP* ... *THWAPPP*"
        player.c "NNNNNN!!!"
        wt_image psycho_domme_4_11
        lee.c "Fuck, you are so hot when you're in pain.  Get over here and lie across my lap."
        wt_image psycho_domme_4_12
        "As you get into posiiton, Lee confirms you have your butt plug inserted."
        lee.c "Oh, what a good boy you are, [lee.your_name]!  It makes me wet, knowing you do what you're told.  I still have to punish you, though, for making me work to get you hard."
        wt_image psycho_domme_4_13
        "*SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK*"
        wt_image psycho_domme_4_14
        "It's a hard spanking, but it doesn't last long.  Lee seems anxious to get into her strap-on and removes the plug from your ass."
        wt_image psycho_domme_4_15
        "Then after a few more hard slaps on your rump ... *SMACKKK* ... *SMACKKK* ... *SMACKKK* ..."
        wt_image psycho_domme_4_16
        "... she rams her dick into you."
        wt_image psycho_domme_4_17
        "Wearing the plug really did help.  She enters you more easily, with less effort for her and less pain for you ..."
        wt_image psycho_domme_4_18
        "... and not because she's taking it easy on you.  In her excitement, she drives the phallus in as deep as it will go."
        wt_image psycho_domme_4_19
        "She's turned on by fucking you, and grinds herself against you ..."
        wt_image psycho_domme_4_20
        "... and soon brings herself to climax with her dick buried deep in your ass."
        lee.c "FUUCCKKK!!"
        wt_image psycho_domme_4_21
        if lee.has_item(chastity_belt):
            lee.c "Since you were soft when I got here, I'm putting you in your cock cage.  There's no need for you to be hard after I leave."
            wt_image psycho_domme_4_22
            "She locks up your cock ..."
            wt_image psycho_domme_4_23
            "... ties your hands loosely, and shoves her stockings in your mouth ."
            wt_image psycho_domme_4_24
            "Then she rubs your balls with her foot."
            lee.c "You can unlock yourself in two hours.  It should take you less than half that time to get out of those ropes.  Shall I kick you in the balls before I go?"
            $ title = "What do you do?"
            menu menu_lee_domme_event_2_menu:
                "Nod in agreement":
                    wt_image psycho_domme_4_25
                    "She doesn't hold back.  She has strong legs, and the pain as her kick connects with your balls is excruciating."
                    player.c "NNNNNNNNN!!!"
                    lee.c "It's your fault, [lee.your_name].  If you didn't look so hot when you're writhing in pain, I might not enjoy hurting you so much."
                "Shake your head 'no'":
                    if not lee.has_tag('no_once'):
                        add tags 'no_once' to lee
                        lee.c "Are you sure?  I'd love to have a memory of you squirming in pain to think about until the next time I visit.  Wouldn't you be able to put up with the pain to give me that pleasure?  Just one kick, what do you say?"
                        jump menu_lee_domme_event_2_menu
                    else:
                        "She caresses your balls with her foot a little longer, then leaves you be."
                        lee.c "Okay, [lee.your_name].  Maybe another day, then."
            rem tags 'no_once' from lee
        else:
            lee.c "Keep wearing the butt plug each night, [lee.your_name].  I like the improvements it's making in your body."
            player.c "Yes, [lee.her_respect_name].  Thank you."
            if not lee.has_any_tag('no_chastity_belt', 'accepted_chastity_belt'):
                lee.c "You being soft when I wanted you hard made me realize, though, that I want more control over your erection.  I want you to buy a cock cage and have it here for me the next time I visit."
                $ title = "What do you say?"
                menu:
                    "Yes, [lee.her_respect_name]":
                        add tags 'accepted_chastity_belt' 'need_chastity_belt' to lee
                        sys "A cock cage is just another form of chastity belt, which you can buy at The Steel Trap."
                    "Ask for this to be a limit":
                        lee.c "I wouldn't leave you locked in it all the time.  I wouldn't let it interfere with your work or your relationships with those other silly girls.  It would just be for me to control you more when you're serving me."
                        $ title = "What do you say?"
                        menu:
                            "Okay, [lee.her_respect_name]":
                                add tags 'accepted_chastity_belt' 'need_chastity_belt' to lee
                                sys "A cock cage is just another form of chastity belt, which you can buy at The Steel Trap."
                            "I'm not comfortable with that":
                                add tags 'no_chastity_belt' to lee
                                lee.c "Okay, I'll respect your limit."
        change player energy by -energy_long
    # chasity device scene
    elif lee.domme_outfit == 3:
        wt_image psycho_domme_5_1
        "When she arrives, Lee picks up a crop and taps it menacingly against her hand as she looks you over."
        wt_image psycho_domme_5_2
        "Then she takes a seat."
        lee.c "Bring me your cock cage."
        wt_image psycho_domme_5_6
        lee.c "Stand up straight and stop fidgeting."
        wt_image psycho_domme_5_3
        "Warm as Lee's hands may be, the device itself feels cold as she locks your cock inside it."
        wt_image psycho_domme_5_4
        "Preoccupied by the sensation of having your cock locked in a device that makes attaining an erection impossible, you barely notice as your biker-chick Domme binds you in place ..."
        wt_image psycho_domme_5_5
        "... and gags you."
        wt_image psycho_domme_5_7
        lee.c "Now you can't talk until I let you talk ..."
        wt_image psycho_domme_5_8
        lee.c "... and you can't get hard until I let you."
        wt_image psycho_domme_5_9
        lee.c "Even if I rub my body against you, you can't make an erection for me."
        wt_image psycho_domme_5_10
        lee.c "Even if I use my mouth and tongue on you, your cock stays small and useless."
        wt_image psycho_domme_5_5
        lee.c "What use is a man who can't get it up for me?  Who has nothing to say, and no way to amuse me?"
        wt_image psycho_domme_5_11
        lee.c "You need to be punished for being so fucking useless."
        wt_image psycho_domme_5_12
        "*SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK* ... *SMACKKK*"
        wt_image psycho_domme_5_13
        player.c "NNNNN!!"
        wt_image psycho_domme_5_14
        lee.c "Hmmmm, well I suppose that is one way you could amuse me - you could suffer for me."
        "*SMAACCKKK*"
        wt_image psycho_domme_5_15
        lee.c "Giving pleasant sensations to your cock and balls is totally useless right now, so if you're going to suffer, I may as well direct the pain here."
        wt_image psycho_domme_5_16
        lee.c "These clothespins probably don't hurt very much.  Not going on, anyway."
        wt_image psycho_domme_5_17
        lee.c "Coming off may be a different matter.  Would you care to guess how they're coming off?"
        wt_image psycho_domme_5_18
        "*THWAAAPPP*"
        player.c "NNNNNN!!"
        wt_image psycho_domme_5_19
        lee.c "Well that was disappointing.  It's hardly worth the effort to hurt you if that's all the noise you can make."
        wt_image psycho_domme_5_5
        lee.c "I guess I'd better give you back your voice.  If you don't have anything interesting to say to me, you can at least use it to scream properly."
        wt_image psycho_domme_5_20
        $ lee.temporary_count = 1
        $ title = "What do you do?"
        menu menu_lee_domme_event_3_menu:
            "Wait for the next blow":
                $ lee.temporary_count += 1
                wt_image psycho_domme_5_18
                "*THWAAAPPP*"
                wt_image psycho_domme_5_21
                player.c "OOOOWWWWWWW!!!"
                if lee.temporary_count > 9:
                    wt_image psycho_domme_5_4
                    lee.c "No more clothespins.  Pity."
                    wt_image psycho_domme_5_3
                    lee.c "I suppose your balls are so inured to pain, now, you won't even feel it when I squeeze them?"
                    wt_image psycho_domme_5_21
                    player.c "OOOWWWWW!!!"
                    wt_image psycho_domme_5_10
                    lee.c "Ahhh, now you're just trying to make me feel good, screaming so prettily for me.  That's so sweet."
                else:
                    wt_image psycho_domme_5_17
                    if lee.temporary_count == 2:
                        lee.c "That's so much better."
                    elif lee.temporary_count == 3:
                        lee.c "Look, one of the clothespins fell off.  But I guess you could feel that?"
                    elif lee.temporary_count > 7:
                        lee.c "Not many clothespins left.  I'm tempted to add more to make this last longer."
                    else:
                        lee.c "More clothespins came off.  I would have thought you'd be getting used to the sensation, but the way you scream makes me think you're not."
                    wt_image psycho_domme_5_20
                    jump menu_lee_domme_event_3_menu
            "Beg":
                wt_image psycho_domme_5_17
                player.c "Please, [lee.her_respect_name]!  Please don't hurt me anymore!!  Please have mercy on me, please, I'm begging you!!"
                wt_image psycho_domme_5_19
                lee.c "But I enjoy hurting you, and listening to you beg just makes me enjoy it even more."
                jump menu_lee_domme_event_3_menu
            "Use your safe word":
                wt_image psycho_domme_5_22
                lee.c "You're not able to give me my fun today, [lee.your_name]?  Considering your normal pain tolerance, I can only assume you find this just too scary to continue.  Okay, I'll stop there."
        wt_image psycho_smile_1
        lee.c "I'm leaving the key to your cage here.  I loosened your bonds so you'll be able to get out of them and remove the cage.  How quickly you get out of them will depend, I suppose, on whether you want my control over your cock to end or be prolonged.  I'm just going to assume you wear it all day.  Bye!"
    # foot worship and random ooutcomes
    elif lee.domme_outfit == 4:
        wt_image psycho_domme_6_1
        "Your biker-chick Domme takes a seat in front of you when she arrives."
        wt_image psycho_domme_6_2
        lee.c "Do you think you're worthy to lick my boots, [lee.your_name]?"
        $ title = "How do you respond?"
        menu:
            "No, [lee.her_respect_name]":
                wt_image psycho_domme_6_3
                lee.c "No, you're not.  Which is why you're going to worship my smelly, stockinged feet instead."
            "I hope so, [lee.her_respect_name]":
                wt_image psycho_domme_6_3
                lee.c "You're not.  Which is why you're going to worship my smelly, stockinged feet instead."
            "Only if you think I am, [lee.her_respect_name]":
                wt_image psycho_domme_6_3
                lee.c "I don't.  Which is why you're going to worship my smelly, stockinged feet instead."
        wt_image psycho_domme_6_4
        "You nuzzle, kiss and lick at her extended foot.  She must have been wearing the stockings underneath her boots for a while, because they are smelly, and yet incredibly sexy."
        # first determine if she hurts you
        $ lee.random_number = renpy.random.randint(1, 5)
        # flogging
        if lee.random_number < 3:
            wt_image psycho_domme_6_5
            lee.c "That's enough.  Lie down, I'm going to hurt you."
            wt_image psycho_domme_6_6
            "She seems serious about wanting to hurt you, as she maximizes her leverage for the blows ..."
            wt_image psycho_domme_6_7
            "... but she seems also to want to tease you, as she removes her top, giving you a tantalizing view of her bare breasts swaying as she swings the flogger."
            wt_image psycho_domme_6_8
            "*THWACKKK* ... *THWACKKK* ... *THWACKKK* ... *THWACKKK* ... *THWACKKK*"
            player.c "Oowww!"
            wt_image psycho_domme_6_9
            if lee.random_number == 1:
                "As she finishes beating you, she looks at you lustfully."
            else:
                "As she finishes beating you, she looks at you, as if deciding what comes next."
        # ball torture
        elif lee.random_number < 5:
            wt_image psycho_domme_6_10
            lee.c "That's enough.  Lie down, I want to play with your balls."
            wt_image psycho_domme_6_11
            "Her approach to ball-play would not be everyone's cup of tea ..."
            wt_image psycho_domme_6_12
            "... but at least she does take off her top to expose her bare breasts as finishes the painful binding of your testicles ..."
            wt_image psycho_domme_6_13
            "... which at least gives you something pleasant to look like as you try to distract yourself from the even more painful attention that Lee teases by tracing the cane across your balls."
            wt_image psycho_domme_6_14
            lee.c "Count.  And if you'd like to scream, too, I'd enjoy that."
            wt_image psycho_domme_6_15
            "There's absolutely no way for you not to scream as Lee brings the cane down across your balls ... *thwippp*"
            player.c "OOOWWWWW!!  That's one!"
            wt_image psycho_domme_6_14
            $ lee.temporary_count = 1
            $ title = "What do you do?"
            menu menu_lee_domme_event_4_menu:
                "Wait for the next blow":
                    $ lee.temporary_count += 1
                    wt_image psycho_domme_6_15
                    "*thwippp*"
                    player.c "OOOOWWWWWWW!!!  That's [lee.temporary_count.to_s]!!"
                    if lee.temporary_count > 4:
                        wt_image psycho_domme_6_13
                        lee.c "Mmmmm, this is fun, but we'd better stop there, before I break you.  These balls are looking pretty bruised."
                    else:
                        wt_image psycho_domme_6_14
                        jump menu_lee_domme_event_4_menu
                "Beg":
                    player.c "Please, please, please [lee.her_respect_name]!  Please don't hurt me like this!!  Please have mercy on me, I'm begging you!!"
                    lee.c "But I enjoy hurting you, and listening to you beg just makes me enjoy it even more."
                    jump menu_lee_domme_event_4_menu
                "Use your safe word":
                    wt_image psycho_domme_6_13
                    lee.c "That's a shame, these balls could take a few more blows before breaking, but if it scares you that much, [lee.your_name], I'll stop."
            wt_image psycho_domme_6_16
            if lee.random_number == 1:
                "As she removes the bindings from your balls, she looks at you lustfully."
            else:
                "As she removes the bindings from your balls, she looks at you, as if deciding what comes next."
        # no torture (guaranteed to masturbate)
        else:
            wt_image psycho_domme_6_17
            "Removing her foot from your mouth, Lee looks at you lustfully."
            lee.c "Lie down."
            wt_image psycho_domme_6_18
            "You lie down in front of her and watch as Lee rubs herself."
            wt_image psycho_domme_6_19
            "Then she pulls off her top, exposing her hard nipples."
        # if odd number, she masturbates:
        if lee.random_number == 1 or lee.random_number == 3 or lee.random_number == 5:
            add tags 'masturbated_today' to lee
            wt_image psycho_domme_6_20
            lee.c "Squeeze my tits."
            wt_image psycho_domme_6_21
            lee.c "Make yourself hard."
            wt_image psycho_domme_6_22
            lee.c "Good, [lee.your_name].  Stop touching now, and don't you dare cum."
            wt_image psycho_domme_6_23
            "More easily said than done, as she grinds herself against you, using your erection to masturbate herself with."
            wt_image psycho_domme_6_24
            lee.c "FUUCCKKK!!"
            wt_image psycho_domme_6_25
            "Lee looks at you as she rubs her pussy contentedly, as if deciding what comes next."
            $ lee.orgasm_count += 1
        # finally, decide if she provides you with relief:
        $ lee.random_number = renpy.random.randint(1, 6)
        # handjob
        if lee.random_number < 3:
            wt_image psycho_domme_6_26
            if lee.has_tag('masturbated_today'):
                lee.c "Play with yourself again.  Get close to when you'll need to cum, but don't."
            else:
                lee.c "Make yourself hard for me.  Get close to when you'll need to cum, but don't."
            wt_image psycho_domme_6_22
            "You bring yourself right to the edge, and try to stay there."
            lee.c "Good boy.  Take your hand away now, [lee.your_name].  And no cumming unless I tell you you can."
            wt_image psycho_domme_6_27
            "Lee nuzzles and licks your balls and your nard shaft.  Even if she hadn't made you edge yourself first, it would be exquisite torture holding back your orgasm ..."
            wt_image psycho_domme_6_28
            "... and it gets worse when she starts caressing your balls and stroking your cock while she licks and nibbles at you.  Finally, mercifully, she speaks."
            lee.c "Cum for me, [lee.your_name]."
            wt_image psycho_domme_6_29
            player.c "[player.orgasm_text]"
            wt_image psycho_domme_6_30
            lee.c "You made a mess on your belly, which is cute, but you also got some on my hand.  Lick it clean."
            player.c "Yes, [lee.her_respect_name].  Thank you."
            $ lee.handjob_count += 1
            orgasm notify
        # footjob
        elif lee.random_number < 5:
            wt_image psycho_domme_6_26
            if lee.has_tag('masturbated_today'):
                lee.c "Play with yourself again."
            else:
                lee.c "Make yourself hard for me."
            wt_image psycho_domme_6_22
            lee.c "Good boy."
            wt_image psycho_domme_6_31
            lee.c "Take your hand away now, [lee.your_name]."
            wt_image psycho_domme_6_32
            "As you remove your hand, she replaces it with her stockinged foot, crushing your cock underneath it."
            wt_image psycho_domme_6_33
            "Then she slides her foot roughly along your shaft, her heel pressing into your balls as she does so.  It feels wonderful and painful at the same time."
            wt_image psycho_domme_6_34
            "And then suddenly the pain is gone, and she grips your shaft between the soles of both feet and pumps you quickly up-and-down."
            lee.c "Cum for me, [lee.your_name]."
            wt_image psycho_domme_6_35
            player.c "[player.orgasm_text]"
            wt_image psycho_domme_6_36
            lee.c "You made a mess on my stockings, [lee.your_name]."
            wt_image psycho_domme_6_37
            lee.c "Lick them clean."
            player.c "Yes, [lee.her_respect_name].  Thank you."
            $ lee.footjob_count += 1
            orgasm notify
        # no relief
        else:
            wt_image psycho_domme_6_26
            if lee.has_tag('masturbated_today'):
                lee.c "That's enough for today.  I can see you're still rock hard, but I've had my fun.  I'll call you the next time I want you to serve me."
            else:
                lee.c "That's enough for today.  I've had my fun.  I'll call you the next time I want you to serve me."
            change player energy by -energy_long notify
        # set up leash scene if applicable
        if not lee.has_any_tag ('accepted_leash', 'no_leash'):
            wt_image psycho_domme_6_19
            "Before she leaves, Lee turns and addresses you once more."
            lee.c "You make a fun pet, [lee.your_name].  I think we should cement that status.  Have a leash for me to put on you the next time I visit."
            $ title = "What do you say?"
            menu:
                "Yes, [lee.her_respect_name]":
                    add tags 'need_leash' 'accepted_leash' to lee
                    if player.has_item(leash):
                        "Fortunately, you already have a leash she can use on you."
                    else:
                        sys "You can buy one at the Critter Emporium."
                "Ask for this to be a limit":
                    lee.c "I wouldn't take you for a walk in public.  This is just for me to enjoy while we're in private together."
                    $ title = "What do you say?"
                    menu:
                        "Okay, [lee.her_respect_name]":
                            add tags 'need_leash' 'accepted_leash' to lee
                            if player.has_item(leash):
                                "Fortunately, you already have a leash she can use on you."
                            else:
                                sys "You can buy one at the Critter Emporium."
                        "I'm not comfortable with that":
                            add tags 'no_leash' to lee
                            lee.c "Okay, I'll respect your limit."
        rem tags 'masturbated_today' from lee
    # leash event
    elif lee.domme_outfit == 5:
        wt_image psycho_domme_7_1
        "Lee finds you waiting on your knees in a makeshift cage in the corner of your dungeon."
        lee.c "Come, pet.  Time for your walk."
        wt_image psycho_domme_7_2
        "She leads you by the leash around and around the room, making sure you get a good exercise."
        wt_image psycho_domme_7_3
        "Then she gets on your back."
        lee.c "Carry me, boy."
        wt_image psycho_domme_7_4
        "Round and round you go, carrying her around the room on your back ..."
        wt_image psycho_domme_7_5
        "... until you take a turn too fast, and she almost falls off."
        wt_image psycho_domme_7_6
        lee.c "Bad, boy!  Bad!!"
        wt_image psycho_domme_7_7
        "*thwippp*"
        player.c "NNNNN!!"
        wt_image psycho_domme_7_8
        lee.c "You were letting yourself get too excited, pet.  You got carried away and almost hurt me."
        wt_image psycho_domme_7_9
        lee.c "No wonder you got carried away, look how hard you are.  Imagine, a pet like you getting an erection for an actual human being, like me."
        wt_image psycho_domme_7_10
        lee.c "You need discipline, pet, so that you remember your place."
        wt_image psycho_domme_7_11
        lee.c "Kiss the cane I'm going to discipline you with."
        wt_image psycho_domme_7_12
        "At first you think she's going to use the cane on - or in - your ass ..."
        wt_image psycho_domme_7_13
        "... then you realize she has something more painful in mind, and more directly related to your unauthorized erection."
        wt_image psycho_domme_7_14
        "*thwippp* ... *thwippp* ... *thwippp*"
        player.c "NNNNNNNNN!!!"
        wt_image psycho_domme_7_15
        lee.c "Okay, boy, I want you to have an erection now, but I hope you learned your lesson about getting hard before I give you permission."
        if lee.has_tag('no_ass_worship'):
            wt_image psycho_domme_7_17
            lee.c "Worship my feet to thank me for teaching you that I decide when you're hard and when you're not."
        else:
            wt_image psycho_domme_7_16
            lee.c "Worship my ass to thank me for teaching you that I decide when you're hard and when you're not."
            wt_image psycho_domme_7_17
            lee.c "Now come over here and worship my feet."
        wt_image psycho_domme_7_18
        "You clean the soles of her feet with your tongue, then lick between her toes as your biker-chick Domme decides what she's going to do with you next."
        # determine what she does with you
        $ lee.random_number = renpy.random.randint(1, 6)
        # eat her out
        if lee.random_number < 3:
            wt_image psycho_domme_7_19
            lee.c "Here, boy.  Lick here."
            wt_image psycho_domme_7_20
            "She doesn't have to tell you twice.  You bury your tongue in her wet snatch and lick until she fills your mouth with cum."
            wt_image psycho_domme_7_21
            lee.c "FUUCCKKK!!"
            $ lee.pleasure_her_count += 1
            $ lee.orgasm_count += 1
            change player energy by -energy_long
        # fucks you
        elif lee.random_number < 5:
            wt_image psycho_domme_7_22
            lee.c "Lie down and let me check your erection."
            wt_image psycho_domme_7_23
            "Finding the state of your dick to her satisfaction, she climbs up onto you ..."
            wt_image psycho_domme_7_24
            "... and resumes riding you, but this time on your cock, not your back."
            wt_image psycho_domme_7_25
            "You're not sure if you'll be allowed to cum, but even if you are, you know it won't be until Lee's taken her pleasure from you ..."
            wt_image psycho_domme_7_24
            "... you try to ignore how good she feels riding up-and-down your cock."
            wt_image psycho_domme_7_25
            "Fortunately, it seems to feel almost as good to her."
            wt_image psycho_domme_7_26
            lee.c "FUUCCKKK!!"
            wt_image psycho_domme_7_27
            lee.c "Cum for me, [lee.your_name]!"
            wt_image psycho_domme_7_28
            player.c "[player.orgasm_text]"
            lee.c "Good boy!"
            $ lee.sex_count += 1
            $ lee.orgasm_count += 1
            orgasm count
        # handjob
        else:
            wt_image psycho_domme_7_22
            lee.c "Lie down and let me check your erection."
            wt_image psycho_domme_7_29
            lee.c "Good boy, you're still hard for me.  Your cock looks delicious.  I wonder if it will taste as good as it looks?"
            wt_image psycho_domme_7_30
            "If you were hoping to feel her lips on your dick, you're soon disappointed as she bites down hard on you with her teeth."
            player.c "OOWWW!!"
            wt_image psycho_domme_7_31
            lee.c "Stay hard for me, [lee.your_name].  I haven't given you permission to lose your erection."
            wt_image psycho_domme_7_32
            "Despite the pain from her teeth, you're not actually at any risk of losing your erection.  You are, however, at risk of accidentally cumming down her throat without permission, an event which would carry consequences potentially so severe that a quick survey of what they might be suffices to keep your climax in check."
            wt_image psycho_domme_7_29
            lee.c "Good boy, you can exercise some self-restraint.  You can go soft now, after you make a mess on your belly."
            wt_image psycho_domme_7_22
            "Using just the tips of her fingers, she teases the orgasm out of you."
            wt_image psycho_domme_7_33
            player.c "[player.orgasm_text]"
            $ lee.handjob_count += 1
            orgasm notify
        wt_image psycho_domme_7_1
        lee.c "Good boy.  Before I go, I'd better put you back where I found you, pet."
    # sharing and bi-content event
    elif lee.domme_outfit == 6:
        call forced_movement(outdoors) from _call_forced_movement_1032
        summon lee no_follows
        summon hannah no_follows
        $ lee.domme_bi_scene += 1
        if lee.domme_bi_scene > 5:
            $ lee.domme_bi_scene = 3
        # initial discussion
        if lee.domme_bi_scene == 1:
            wt_image psycho_principal_1_1
            "You assumed the address she sent you was to her house, but when you arrive, you realize it's actually Principal Hannah's, and Lee is here visiting with her."
            wt_image psycho_principal_1_2
            lee.c "Kneel, [lee.your_name].  Principal Hannah and I are talking."
            wt_image psycho_principal_1_3
            "You're not quite sure what this is all about, so you decide the prudent thing is to kneel while they finish up their conversation about some TV show you've never heard of."
            wt_image psycho_principal_1_2
            "Finally, Lee turns her attention back to you."
            lee.c "So, movie star, I discovered an interesting video of you online.  Hannah's been good enough to tell me how it came about.  I had no idea you were so charitably-minded."
            wt_image psycho_principal_1_4
            lee.c "Now that I know about his giving-spirit, Hannah, I think he may be able to give you and I an interesting experience."
            wt_image psycho_principal_1_5
            # if you and Hannah are havig booty calls
            if hannah.financial_domination_cost > 0:
                hannah.c "He's only supposed to pay me, I'm not interested in having him touch me, but I do have an idea."
            elif hannah.letter_re_terri == 7:
                hannah.c "That does sound like fun, but I've an idea to make it really fun."
            else:
                hannah.c "I'm not particularly interested in playing with him again, but I do have an idea."
            wt_image psycho_principal_1_6
            hannah.c "I don't have much time for a social life, but there is this guy who I've seen once or twice.  After he saw my videos, he mentioned he'd love to watch me Domme another man while he fucks me.  I bet he'd like it just as much if you were doing the domming, Lee."
            wt_image psycho_principal_1_7
            lee.c "Hmmm, I could do that.  And instead of just serving you and I, I could make him serve your lover, too."
            wt_image psycho_principal_1_2
            lee.c "Did you hear that, [lee.your_name]?  I'm going to tap into your generous spirit by allowing you to serve me, Hannah, and her lover."
            $ title = "What do you say?"
            menu:
                "Thank you, [lee.her_respect_name]":
                    pass
                "As long as I don't need to serve him sexually, [lee.her_respect_name]":
                    wt_image psycho_principal_1_2
                    lee.c "Well, I'm not going to let you just enjoy watching Hannah get fucked by a real man while you kneel there and don't help.  You'll need to at least clean his cum off of her once they're done.  Agreed?"
                    menu:
                        "Yes, thank you, [lee.her_respect_name]":
                            add tags 'no_bi_content' to lee
                        "No, ask to make this a limit (no sharing you)":
                            add tags 'no_sharing_content' to lee
                            wt_image psycho_principal_1_4
                            lee.c "Well that's too bad.  I guess he isn't so giving-minded after all."
                            wt_image psycho_principal_1_1
                            "The two women don't seem to be too upset.  They go back to ignoring you while they discuss their show.  Eventually Lee dismisses you and you go home."
                "Ask to make this a limit (no sharing you)":
                    add tags 'no_sharing_content' to lee
                    wt_image psycho_principal_1_4
                    lee.c "Well that's too bad.  I guess he isn't so giving-minded after all."
                    wt_image psycho_principal_1_1
                    "The two women don't seem to be too upset.  They go back to ignoring you while they discuss their show.  Eventually Lee dismisses you and you go home."
            if not lee.has_tag('no_sharing_content'):
                wt_image psycho_principal_1_6
                hannah.c "You know, I think this is going to be fun!"
                wt_image psycho_principal_1_2
                lee.c "So do I, and so does [lee.your_name], judging from the bulge in his pants."
                wt_image psycho_principal_1_3
                "The two women go back to ignoring you while they discuss their show.  They clearly have no intention of involving you in the planning for the upcoming session, as they can't mention it again while you're there.  Eventually Lee dismisses you and you go home."
                $ lee.domme_outfit -= 1 # so that get scene with Lee and Hannah next
                if lee.next_call_countdown > 6:
                    $ lee.next_call_countdown -= 3 # shorten time before she next calls you
            change player energy by -energy_short notify
        # first session
        elif lee.domme_bi_scene == 2:
            wt_image psycho_principal_2_1
            "As you arrive back at Hannah's house, your biker-chick Domme greets you and leads you to the bedroom ..."
            wt_image psycho_principal_2_2
            "... where Principal Hannah is being fucked."
            wt_image psycho_principal_2_3
            hannah.c "If he's planning on just standing there and gawking, at least bring him closer so we can have some fun with him while he stares."
            wt_image psycho_principal_2_4
            lee.c "You heard the woman, [lee.your_name].  You need to earn your view of Hannah's beautiful body being fucked by a real man."
            wt_image psycho_principal_2_5
            "Lee positions you at the end of the bed and pulls down your pants, while Hannah makes it clear that she's very much enjoying her fucking."
            wt_image psycho_principal_2_6
            hannah.c "oooohhhhh   ...  ooooohhhhhh"
            wt_image psycho_principal_2_7
            principal_lover "Make him suffer.  If I have to be looking at him while I'm having sex with Hannah, I at least want to see him in pain."
            wt_image psycho_principal_2_8
            lee.c "You heard the man, [lee.your_name].  Time for you to earn your front row seat."
            wt_image psycho_principal_2_9
            "It's a bad sign when she grips your balls firmly from behind ..."
            wt_image psycho_principal_2_10
            "... and a worse one when she runs the tip of crop along then."
            wt_image psycho_principal_2_11
            "*THWAPPP*  ...  *THWAPPP*  ...  *THWAPPP*"
            wt_image psycho_principal_2_12
            player.c "OOOWWWWW!!!"
            wt_image psycho_principal_2_13
            "At least Hannah and her lover enjoy what's happening to you, as they both cum."
            wt_image psycho_principal_2_6
            hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
            principal_lover "Aaaaaaaa!"
            wt_image psycho_principal_2_14
            hannah.c "That felt good enough for a second round, but he should help out more this time."
            lee.c "Oh he will, won't you, [lee.your_name]?  This time you're going to earn the right to see them cum."
            if lee.has_tag('no_bi_content'):
                wt_image psycho_principal_2_15
                hannah.c "My friend needs a little help before he can fuck me again.  This should be you sucking him hard, but I understand from Lee you have a thing against that."
            else:
                wt_image psycho_principal_2_15
                hannah.c "My friend needs a little help before he can fuck me again."
                wt_image psycho_principal_2_16
                hannah.c "But why am I doing this when you're right here?"
                lee.c "Thank Hannah for letting you suck a real man's cock, [lee.your_name]."
                wt_image psycho_principal_2_17
                player.c "Thank you for letting me suck his cock, Mistress Hannah."
                hannah.c "Just make sure my friend enjoys himself."
                wt_image psycho_principal_2_18
                hannah.c "Is he doing a good job, sweetie?"
                principal_lover "Not bad.  He's a pretty good cocksucker."
                wt_image psycho_principal_2_19
                hannah.c "Well don't do too good a job.  You're only making him hard.  You don't get his cum, at least, not this way."
                $ player.male_sex_count += 1
            wt_image psycho_principal_2_20
            "When Hannah's friend decides he's hard enough, he starts fucking her again.  Lee brings you in close to observe him giving Hannah a second orgasm."
            wt_image psycho_principal_2_21
            hannah.c "Oooooohhhhhh ooohhhhhhhh FUUCCCKKKKK!!!"
            wt_image psycho_principal_2_22
            "Lee also makes you watch his second orgasm from up close."
            wt_image psycho_principal_2_23
            principal_lover "Aaaaaaaa!"
            wt_image psycho_principal_2_24
            lee.c "Show's over, [lee.your_name], time for you to clean up."
            wt_image psycho_principal_2_25
            if hannah.financial_domination_cost > 0:
                hannah.c "I'm only letting you lick another man's cum off my feet as a favor to Lee.  Don't think for a moment that you've done anything to deserve this honor."
            else:
                hannah.c "You'd better do a good job.  If I find any of my friend's sperm still on my feet after you're gone, I'll call Lee and tell her you need to be punished."
            change player energy by -energy_long notify
        # pegging rotation
        elif lee.domme_bi_scene == 3:
            wt_image psycho_principal_2_3
            "You return to Hannah's house, where she and her lover are having sex again while Lee waits for you."
            wt_image psycho_principal_2_2
            hannah.c "The three of us were talking about how you didn't get fucked the last time all of us got together.  That doesn't seem fair."
            wt_image psycho_principal_2_7
            principal_lover "I offered to do the honors, but Lee said that she'd look after you."
            wt_image psycho_principal_2_26
            "Your biker-chick Domme looks after you all right ..."
            wt_image psycho_principal_2_27
            "... in her usual, lube-free way."
            wt_image psycho_principal_2_28
            player.c "OOWWWW!!"
            wt_image psycho_principal_2_13
            hannah.c "Damn, I'd forgotten how loud he can be.  Don't you have a way to keep your bitch quiet, Lee?"
            if lee.has_tag('no_bi_content'):
                wt_image psycho_principal_2_35
                lee.c "He should be using his mouth for something more productive than screaming, but since he's too proud to suck cock, I guess I'd better gag him so the rest of us can have sex in peace."
                wt_image psycho_principal_2_36
                "Amazingly, once you're gagged, Lee manages to ream you even harder and rougher than before, while the other 3 get off on watching you suffer."
                wt_image psycho_principal_2_31
                "Lee reaches climax first ..."
                lee.c "FUUCCKKK!!"
                wt_image psycho_principal_2_37
                "... followed by Hannah ..."
                hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
                wt_image psycho_principal_2_38
                "... who then looks after the other man ..."
                wt_image psycho_principal_2_39
                "... by getting him ready to cum ..."
                wt_image psycho_principal_2_40
                "... all over your face."
                wt_image psycho_principal_2_41
                principal_lover "Aaaaaaaa!"
                wt_image psycho_principal_2_33
                lee.c "There, everybody got to fuck, and everybody who needed to cum got to cum.  Isn't that right, [lee.your_name]?"
                wt_image psycho_principal_2_42
                lee.c "Oh that's right, you can't talk now.  Just nod your head 'yes', [lee.your_name].  And stop trying to run his cum off onto the bedframe - you'll wear it home with you as a sign of respect."
            else:
                wt_image psycho_principal_2_14
                lee.c "If you're okay with changing positions, we can fill his mouth with your friend's hard cock."
                wt_image psycho_principal_2_17
                hannah.c "That's a great fucking idea!"
                wt_image psycho_principal_2_29
                "While Lee continues to ream you ass, Hannah re-positions herself over her lover's face, then pushes your head down onto his cock."
                wt_image psycho_principal_2_30
                "The four of you fuck in this position, as all of you get closer-and-closer to orgasm."
                wt_image psycho_principal_2_31
                "Lee reaches climax first ..."
                lee.c "FUUCCKKK!!"
                wt_image psycho_principal_2_32
                "... followed by Hannah ..."
                hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
                wt_image psycho_principal_2_19
                "... and then her lover fills your mouth with his sperm."
                principal_lover "Aaaaaaaa!"
                wt_image psycho_principal_2_33
                lee.c "There, everybody got to fuck, and everybody who needed to cum got to cum.  Isn't that right, [lee.your_name]?"
                wt_image psycho_principal_2_14
                player.c "Yes, [lee.her_respect_name]."
                principal_lover "Hey, he left some cum still on my cock."
                wt_image psycho_principal_2_34
                "You finish cleaning him off while Hannah and Lee laugh about your inability to do a simple job right like cleaning a man's cock."
                $ player.male_sex_count += 1
            $ lee.orgasm_count += 1
            change player energy by -energy_long notify
        # foot worship rotation
        elif lee.domme_bi_scene == 4:
            wt_image psycho_principal_2_43
            "Once again, Hannah and her lover are already at it by the time you show up."
            wt_image psycho_principal_2_44
            "Lee buckles your collar into place and gets you into position so you don't miss any more of the action."
            wt_image psycho_principal_2_45
            if hannah.financial_domination_cost > 0:
                hannah.c "You totally don't deserve this privilege, but I'm getting tired of just watching you suffer, so Lee and I have decided that you'll be allowed to worship my feet today while I'm being fucked."
            else:
                hannah.c "I'm getting tired of just watching you suffer, so Lee and I talked it over, and we agreed that you'd be allowed to worship my feet today while I'm being fucked."
            wt_image psycho_principal_2_46
            lee.c "Isn't that generous of us?"
            wt_image psycho_principal_2_47
            player.c "Yes, [lee.her_respect_name], thank you!  Thank you, Mistress Hannah!!"
            wt_image psycho_principal_2_48
            "Lee helps make sure you don't miss worshipping any part of Hannah's foot ..."
            wt_image psycho_principal_2_49
            "... then she pulls you close and whispers in your ear."
            wt_image psycho_principal_2_50
            lee.c "I have another treat for you.  If you think you can, I'll let you cum while you're sucking on her foot.  But if you to do so just by grinding against the bed, you're not allowed to touch yourself."
            wt_image psycho_principal_2_51
            $ title = "Can you cum this way today?"
            menu:
                "Yes":
                    wt_image psycho_principal_2_50
                    "It's not easy to make yourself cum with the bedsheets as the only contact on your cock, but you manage."
                    wt_image psycho_principal_2_52
                    player.c "[player.orgasm_text]"
                    lee.c "Fuck, that's so hot!  Good, [lee.your_name]."
                    wt_image psycho_principal_2_53
                    "Hannah seems to find your display hot, too."
                    orgasm
                "No":
                    wt_image psycho_principal_2_48
                    "As sexy as Hannah's foot may be, the taste of it in your mouth and the bed sheet against your cock isn't enough stimulation for you to be able to cum today."
                    wt_image psycho_principal_2_53
                    "Hannah, on the other hand, isn't having any such trouble."
                    change player energy by -energy_long
            wt_image psycho_principal_2_54
            hannah.c "Oooooohhhhhh ooohhhhhhhh FUUCCCKKKKK!!!"
            wt_image psycho_principal_2_55
            lee.c "That's Mistress Hannah looked after, but somebody else still hasn't cum."
            if lee.has_tag('no_bi_content'):
                wt_image psycho_principal_2_56
                lee.c "Stay right there until he's ready to cum on you."
            else:
                wt_image psycho_principal_2_59
                lee.c "Mistress Hannah's feet are the only part of her you get to lick, [lee.your_name].  Use your tongue on his balls and shaft until he's ready to cum."
                wt_image psycho_principal_2_56
                principal_lover "Okay, I'm ready.  Put him over here so I have access to his face."
                $ player.male_sex_count += 1
            wt_image psycho_principal_2_57
            principal_lover "Aaaaaaaa!"
            wt_image psycho_principal_2_58
            lee.c "Don't even think about cleaning his cum off of anything other than Mistress Hannah's pubic hairs, [lee.your_name]."
            $ hannah.orgasm_count += 1
            notify
        # ball cropping rotation
        else:
            wt_image psycho_principal_2_1
            "You can hear Hannah and her lover fucking as your biker-chick Domme leads you to them."
            wt_image psycho_principal_2_2
            principal_lover "Get in here and watch closely while I show you how a man fucks a woman."
            wt_image psycho_principal_2_4
            lee.c "What do you say to him, [lee.your_name]?"
            wt_image psycho_principal_2_5
            player.c "Thank you, Sir, for showing me how a real man fucks a woman."
            wt_image psycho_principal_2_6
            hannah.c "oooohhhhh   ...  ooooohhhhhh  ...  he is really, really good at this!"
            wt_image psycho_principal_2_7
            hannah.c "There is something you could do, though, that I'd enjoy a little bit ..."
            wt_image psycho_principal_2_8
            hannah.c "... you could scream really loud while Lee hurts you."
            wt_image psycho_principal_2_9
            "You almost scream when Lee pulls and twists your balls ..."
            wt_image psycho_principal_2_10
            "... then you almost scream again, out of fear, when you feel her rub the tip of the crop against them ..."
            wt_image psycho_principal_2_11
            "... then you do scream, at the top of your lungs, as she strikes your balls with the crop ...  *THWAPPP*  ...  *THWAPPP*  ...  *THWAPPP*"
            wt_image psycho_principal_2_12
            player.c "OOOOOWWWWWWW!!!"
            wt_image psycho_principal_2_13
            "At least Hannah and her lover enjoy what's happening to you, as they both cum."
            wt_image psycho_principal_2_6
            hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
            principal_lover "Aaaaaaaa!"
            wt_image psycho_principal_2_14
            hannah.c "That felt good enough for a second round, but he should help out even more this time."
            lee.c "Oh he will, won't you, [lee.your_name]?  This time you're going to earn the right to see them cum."
            if lee.has_tag('no_bi_content'):
                wt_image psycho_principal_2_15
                hannah.c "My friend needs some assistance before he can fuck me again.  This should be you sucking him hard, but I understand from Lee you have a thing against that."
            else:
                wt_image psycho_principal_2_15
                hannah.c "My friend needs some assistance before he can fuck me again."
                wt_image psycho_principal_2_16
                hannah.c "But why am I doing this when you're right here?"
                lee.c "Thank Hannah for letting you suck a real man's cock, [lee.your_name]."
                wt_image psycho_principal_2_17
                player.c "Thank you for letting me suck his cock, Mistress Hannah."
                hannah.c "Just make sure my friend enjoys himself."
                wt_image psycho_principal_2_18
                hannah.c "Is he doing a good job, sweetie?"
                principal_lover "Not bad.  He's a pretty good cocksucker."
                wt_image psycho_principal_2_19
                hannah.c "Well don't do too good a job.  You're only making him hard.  You don't get his cum, at least, not this way."
                $ player.male_sex_count += 1
            wt_image psycho_principal_2_20
            "When Hannah's friend decides he's hard enough, he starts fucking her again.  Lee brings you in close to observe him giving Hannah a second orgasm."
            wt_image psycho_principal_2_21
            hannah.c "Oooooohhhhhh ooohhhhhhhh FUUCCCKKKKK!!!"
            wt_image psycho_principal_2_22
            "Lee also makes you watch his second orgasm from up close."
            wt_image psycho_principal_2_23
            principal_lover "Aaaaaaaa!"
            wt_image psycho_principal_2_24
            lee.c "Show's over, [lee.your_name], time for you to clean up."
            wt_image psycho_principal_2_25
            if hannah.financial_domination_cost > 0:
                hannah.c "I'm only letting you lick another man's cum off my feet as a favor to Lee.  Don't think for a moment that you've done anything to deserve this honor."
            else:
                hannah.c "You'd better do a good job.  If I find any of my friend's sperm still on my feet after you're gone, I'll call Lee and tell her you need to be punished."
            change player energy by -energy_long notify
        call forced_movement(living_room) from _call_forced_movement_1033
        call character_location_return(hannah) from _call_character_location_return_757
    call character_location_return(lee) from _call_character_location_return_758
    wt_image current_location.image
    return

label lee_diamond_session:
    # initial talk
    if lee.diamond_status == 1:
        call forced_movement(kitchen) from _call_forced_movement_1034
        summon diamond no_follows
        summon lee no_follows
        wt_image psycho_diamond_1_1
        "A short while later, you find yourself on your knees in your kitchen, listening while Lee and Diamond talk."
        lee.c "I have to tell you, I have no problem with beating the shit out of a stupid bitch who deserves it, but despite what [lee.your_name] and Master M seem to think, I'm not sure you do deserve it.  Do you think you deserve it?"
        wt_image psycho_diamond_1_2
        diamond.c "No, I don't."
        wt_image psycho_diamond_1_3
        diamond.c "Okay, maybe I do, a little."
        wt_image psycho_diamond_1_4
        lee.c "Explain 'maybe'.  Did you cheat on him?  Because I will gladly whip the shit out of you right now if I find out you're yet another cheating whore that [lee.your_name] seems to like hanging out with."
        wt_image psycho_diamond_1_2
        diamond.c "No!  That's not the problem."
        if diamond.has_tag('club_sex'):
            player.c "You decide to keep quiet about yours and Diamond's little indiscretions at the Club, since she seems to rationalize those as not directly violating any rules she's been given by M.  Plus you're worried that if you did, Lee might really whip the shit out of her here and now."
        wt_image psycho_diamond_1_3
        diamond.c "I just don't like to submit to women.  It's not that I don't want to submit - I do want to, in order to please M.  But the thought of being told to lick someone's cunt out just pisses me off, not because I object to licking cunt, but just because I don't think women deserve my submission the way a strong man does."
        wt_image psycho_diamond_1_5
        lee.c "Well, that makes things simple.  I don't want you licking my cunt, either.  If I felt like having my cunt licked, [lee.your_name] would be doing it now while we talk.  You can tell M we chatted, but I can't really help you."
        wt_image psycho_diamond_1_3
        diamond.c "He'll be mad at me because I didn't find some way to please you."
        wt_image psycho_diamond_1_5
        lee.c "Please me how?  What the fuck are you going to do, my laundry?"
        wt_image psycho_diamond_1_2
        diamond.c "I don't know, I guess.  I hate doing laundry, though."
        wt_image psycho_diamond_1_4
        lee.c "Look, I don't understand what kind of psycho-mumbo-jumbo is going on with you and M.  You want to do what he says, you don't want to do what he says.  I think the two of you need to figure it out."
        wt_image psycho_diamond_1_1
        "Things aren't going to go anywhere unless you interject and help them out."
        $ title = "Help move things along?"
        menu:
            "Yes":
                $ lee.diamond_status = 3
                player.c "[lee.her_respect_name] would enjoy watching you suffer."
                wt_image psycho_diamond_1_2
                diamond.c "Is that true?"
                wt_image psycho_diamond_1_5
                lee.c "Probably.  People keep telling me I'm a sadist for some reason, so I guess maybe I'd enjoy hurting you."
                wt_image psycho_diamond_1_2
                diamond.c "I hate pain.  It'd be so much easier being a submissive if I'd been born a masochist, too."
                wt_image psycho_diamond_1_3
                diamond.c "Mistress Lee, would you please hurt me and make me suffer for your enjoyment?"
                wt_image psycho_diamond_1_4
                lee.c "You don't like to serve women and you dislike pain, but now you're asking me to enjoy myself by hurting you.  You're fucked up, you know that?"
                wt_image psycho_diamond_1_2
                diamond.c "Yes.  Will you do it, please?"
                wt_image psycho_diamond_1_5
                lee.c "Not today, especially not with that fucking attitude.  Go home to M and tell him I think you have a real problem with strong women, and if he wants me to help straighten you out, I will.  But if you come with me again, I'm going to make you my bitch, do you understand?  And I'm not going to give a fuck about what you're feeling while I'm doing so."
                wt_image psycho_diamond_1_2
                "Diamond glares at Lee for a moment, then drops her eyes."
                wt_image psycho_diamond_1_3
                diamond.c "I understand."
                wt_image psycho_diamond_1_1
                lee.c "Try that again, or I may change my mind about waiting until next time."
                wt_image psycho_diamond_1_3
                diamond.c "I understand, Mistress Lee.  I'm sorry, I told you this was hard for me."
                wt_image psycho_diamond_1_4
                lee.c "And I told you I don't give a fuck about whatever weird shit's going on in your head.  All I care about is finding out how loud you can scream."
                wt_image psycho_diamond_1_1
                "The two women awkwardly finish their tea, then leave.  You can set up their next meeting by prompting them though a call to Lee, when Lee's available and willing to take your call."
            "No, this is boring":
                $ lee.diamond_status = 2
                "Lee and Diamond finish their tea then leave, letting you go on with your day."
        call forced_movement(living_room) from _call_forced_movement_1035
        wt_image current_location.image
        call character_location_return(diamond) from _call_character_location_return_759
        call character_location_return(lee) from _call_character_location_return_760
    # actual event
    elif lee.diamond_status == 4:
        $ lee.training_session()
        $ diamond.training_session()
        call forced_movement(boudoir) from _call_forced_movement_1036
        summon diamond no_follows
        summon lee no_follows
        wt_image psycho_diamond_2_1
        "A few hours later, Lee leads a subdued Diamond into your boudoir.  She's carrying a heavy bag, which she sets down on the side table."
        wt_image psycho_diamond_2_2
        lee.c "Remove your clothes."
        wt_image psycho_diamond_2_3
        lee.c "You, too.  I may have a use for you later.  Stay on your knees until I do."
        wt_image psycho_diamond_2_4
        "In a somewhat ego deflating moment, neither of the two women pay any attention as you make yourself naked.  Lee is too busy removing things from the bag, and Diamond is too busy trying to see what they are."
        lee.c "M seems inordinately concerned about me harming you.  I don't know what [lee.your_name] must have told him about me.  Anyway, he gave me some things that he assures me will make you suffer, without putting you in the hospital."
        wt_image psycho_diamond_2_5
        lee.c "If they don't work, I'll grab a stick and hurt you the old-fashioned way.  Didn't I tell you to take off your clothes?  Get them all off and get on the bed, and don't make me repeat myself again."
        wt_image psycho_diamond_2_6
        lee.c "All these wires and clamps, when all we really need is for me to smack your pussy."
        "*SMACKKK*"
        diamond.c "OW!"
        wt_image psycho_diamond_2_7
        lee.c "M went though all this trouble to get this equipment for us, though, I guess we should try it."
        "*bzzzzzttt*"
        diamond.c "OOWWW!!"
        wt_image psycho_diamond_2_8
        lee.c "Oh, that does seem to hurt.  And so little effort on my part.  I think you should work harder to please me, though.  I want to hear you scream, bitch, and I want you to make it loud even with my panties in your mouth."
        wt_image psycho_diamond_2_9
        "Diamond trembles in fear as Lee connects additional batteries to her sex and nipples."
        wt_image psycho_diamond_2_10
        lee.c "M assured me that even if I connect all the batteries at once, there's not enough voltage to fry anything important of yours, but I'm looking forward to testing that theory."
        wt_image psycho_diamond_2_11
        "*bzzzzzttt*"
        diamond.c "NNNNNN!!"
        wt_image psycho_diamond_2_12
        lee.c "Oh, that is fun, but I still don't think you're working hard enough to entertain me.  Let's tie your tongue up so you have to try extra hard to make enough noise to please me."
        wt_image psycho_diamond_2_13
        "Lee cranks up the voltage, and hits Diamond with three shocks in short succession ... *bzzzzzttt* ... *bzzzzzttt* ... *bzzzzzttt*"
        diamond.c "NNNNN!!  NNNNNN!!  NNNNNNNNN!!!"
        wt_image psycho_diamond_2_14
        "Then she sets all the batteries to MAX and hits Diamond with three more ... *bzzzzzttt* ... *bzzzzzttt* ... *bzzzzzttt*"
        diamond.c "NNNNNNNN!!  NNNNNNNNN!!!  NNNNNNNNNNNNN!!!"
        wt_image psycho_diamond_2_15
        lee.c "Oh wow, you're crying!  That's so hot, you taking so much pain just to please me, and not using your safeword."
        wt_image psycho_diamond_2_16
        lee.c "Remember when I told you I wasn't interested in having you lick my cunt?  Well, I'm feeling a little differently now that I'm all worked up from hurting you."
        wt_image psycho_diamond_2_17
        lee.c "Lick my ass and cunt, bitch."
        wt_image psycho_diamond_2_18
        "Even tied in the unusual gag Lee put her in, Diamond has enough range of movement with her tongue to comply ..."
        wt_image psycho_diamond_2_19
        "... and she seems to use it to good effect, as your Domme is soon cumming in her mouth."
        wt_image psycho_diamond_2_20
        lee.c "FUUCCKKK!!"
        wt_image psycho_diamond_2_16
        lee.c "Mmmmm, I know you think you're not good at submitting to women, but I think you obey just fine as long as you're treated with a firm hand.  You just need her to treat you like a piece of meat, the way most men see you."
        wt_image psycho_diamond_2_22
        lee.c "Speaking of almost-men, come over here, [lee.your_name].  Diamond's going to thank you for your part in setting up her lesson today."
        wt_image psycho_diamond_2_23
        lee.c "And while you're thanking him, you can thank me, too, by screaming for me again."
        "As Diamond blows you, Lee inserts an electrified rod into her cunt ..."
        wt_image psycho_diamond_2_24
        "... and turns it on ... *bzzzzzttt*"
        diamond.c "NNNNNNNNN!!!"
        "The electric charge causes Diamond to involuntarily bite down on your cock, which you're sure is no accident on Lee's part."
        player.c "OOWWW!!"
        wt_image psycho_diamond_2_21
        lee.c "Hmmm, it looks like she left teeth marks.  Good thing I only promised M I wouldn't harm her, I didn't say anything about you.  You're still hard anyway, so I guess you'll live."
        wt_image psycho_diamond_2_25
        lee.c "You may want to keep your cock out of her mouth for this part.  I'm told it hurts even more up her ass than it does in her cunt.  When you think she's screaming as loudly as she can, you can cum."
        wt_image psycho_diamond_2_26
        diamond.c "OOOOWWWWWWW!!!"
        player.c "[player.orgasm_text]"
        wt_image psycho_diamond_2_27
        "You thought you'd timed things fairly well, but then Lee attaches an extra battery, and Diamond's screaming finds a new gear."
        diamond.c "AAAIIIIIIIEEEEEEEEEE!!!!!"
        wt_image psycho_diamond_2_28
        "And then suddenly Diamond's not screaming at all, just lying on the bed, twitching."
        wt_image psycho_diamond_2_29
        lee.c "Good girl, you gave me all your screams.  You can wear [lee.your_name]'s cum home so M can see how well you served me.  Clean this off, first, though.  I'm not sending it back to M in this condition, not after it's been up your ass."
        wt_image psycho_diamond_2_2
        "On her way out, Diamond stops and addresses Lee."
        diamond.c "Thank you, Mistress, for showing me how submissive I can be with a woman."
        lee.c "You're welcome.  I enjoyed hurting you, bitch.  If you grow a cock, I'd even do it again."
        sys "Don't get ideas.  Diamond cannot grow a cock in this game.  Not unless someone mods that in."
        $ diamond.blowjob_count += 1
        $ diamond.facial_count += 1
        orgasm notify
        $ diamond.lesbian_training += 1
        $ lee.next_call_countdown += 3 # increase time before she next calls you again
        if lee.has_tag('no_sharing_content'):
            $ lee.diamond_status = 6 # skips the event with M
        else:
            $ lee.diamond_status = 5 # next event will be with M
        call character_location_return(diamond) from _call_character_location_return_761
        call character_location_return(lee) from _call_character_location_return_762
        end_day
    return

# End Day
label lee_end_day:
    if lee.domme_you_status == 3:
        $ lee.domme_you_status = 4
    if lee.diamond_status == 3:
        $ lee.diamond_status = 4
    return

# End Week
label lee_end_week:
    pass
    return

## Character Specific Timers

# convert to Domme
label lee_convert_domme:
    call convert(lee, "domme") from _call_convert_199
    $ lee.suffix = "the Domme"
    $ lee.relationship_counter = 3 # reset to standard setting for Domme
    $ lee.next_call_countdown = 5 # she will first contact you 5 days from now
    rem tags 'no_ass_worship' from lee # this is so that this limit gets re-evaluated now that she's your Domme
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
