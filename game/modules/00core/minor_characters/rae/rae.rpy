## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: wifetrainer

# Package Register
# register_package rae name "Rae Store Clerk" description "Allows Rae as Eros Store Clerk" dependencies core
register rae_pregame 10 in core as "Rae the Eros Store Clerk"

label rae_pregame:
  # Start Day Events
  day_label add to start rae_start_day_normal_events

  python:
  ## Constants
    model_credits += [('support', "Rae the Eros Store Clerk (Victoria Rae Black)")]

    ## Character Definition
    rae = Person(Character("Store Clerk", who_color="#00FFFF", what_color="#00FFFF"), "rae", cut_portrait = True, prefix = "The", suffix = "")
    rae.trigger_phrase = "Good clerks know the customer is always right"

    ## Other Characters
    # None

    ## Items
    # Rae's Photos
    photos_of_rae = Item('Photos of Rae', 'por', with_examine = True)
    rae.action_date_item = photos_of_rae.add_action("Go on a date with Rae", label = rae.short_name + "_start_date_check", condition = "rae.can_be_interacted and (rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'))")
    rae.action_look_boudoir_photos = photos_of_rae.add_action("Look at her Boudoir Photos", label = rae.short_name + "_review_files_boudoir_photos", condition = "rae.boudoir_photos_sent")
    #rae.action_look_selfies = photos_of_rae.add_action("Look at her Selfies", label = rae.short_name + "_review_files_selfies", condition = "rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend')") ##not needd because Examine does this
    rae.action_view_selfies = bedroom.add_action("Rae's Selfies", label = rae.short_name + "_review_files_selfies", context = '_computer_view_images', condition = "player.has_tag('rae_photos_received')")
    rae.action_view_boudoir_photos = bedroom.add_action("Rae's Boudoir Photos", label = rae.short_name + "_review_files_boudoir_photos", context = '_computer_view_images', condition = "rae.boudoir_photos_sent")


    ## Locations
    rae.location = eros_store

    ## Actions
    rae.action_talk = rae.add_action("Talk to her", label = "_talk", condition = "rae.can_be_interacted and rae.has_tag('examined') and not rae.has_tag('flirting') and rae.location == eros_store")
    rae.action_flirt = rae.add_action("Flirt with her", label = "_flirt", condition = "rae.can_be_interacted and rae.has_tag('flirting') and rae.location == eros_store")
    rae.action_date_talk = rae.add_action("Go on a date", label = "_start_date_check", condition = "rae.can_be_interacted and (rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend')) and not rae.has_tag('on_date')")
    rae.action_date = rae.add_action("Start the date", label = "_date", condition = "rae.has_tag('on_date') and (rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend')) and rae.location == living_room")
    rae.action_dance = rae.add_action("Watch her dance", label = "_dance", condition = "rae.can_be_interacted and rae.has_tag('showgirl') and rae.location == stage and not rae.has_tag('watched_today')")
    rae.action_bimbo = rae.add_action("Check on your bimbo", label = "_bimbo_actions", condition = "rae.can_be_interacted and rae.has_tag('bimbo') and rae.location == bedroom")

    rae.action_date_phone = living_room.add_action("Go on a date with Rae", label = rae.short_name + "_start_date_check", context = "_contact_other", condition = "rae.can_be_interacted and (rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'))")
    rae.relationship_action = bedroom.add_action("[rae.full_name]", label = rae.short_name + "_relationship_status", context = "_relationship_status", condition = "rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend')")

    # Rae's Photos
    ## all replaced by photos_of_rae object
    #rae.action_view_photos = bedroom.add_action("Rae the Store Clerk's Photos", context = '_computer_view_images', new_context = "_rae_photos", condition = "bedroom.has_action_of_context('_rae_photos')") #replaced below
    #rae.action_view_boudoir_photos = bedroom.add_action("Rae the Store Clerk's Boudoir Photos", label = rae.short_name + "_review_files_boudoir_photos", context = '_rae_photos', condition = "rae.boudoir_photos_sent")
    #rae.action_view_selfies = bedroom.add_action("Rae the Store Clerk's Selfies", label = rae.short_name + "_review_files_selfies", context = '_rae_photos', condition = "rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend')")

    ## Tags
    # Common Character Tags
    rae.add_tags('es_store_content', 'no_hypnosis', 'likes_boys', 'swingers_room_possible')
    # note: swingers room access not actually possible for Rae, but it is possible to get a message about it.

    # Character Specific Tags
    rae.add_tags('exclusive_girlfriend', 'working_at_store')

    ## Other
    rae.change_status("minor_character")

    ########### VARIABLES ###########
    # Common Character Variables
    rae.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_masturbation_count', 'hypno_orgasm_count', 'hypno_sex_count', 'hypno_swallow_count', 'hypno_titfuck_count', 'maintain_week_gf', 'random_number')

    # Character Specific Variables
    rae.add_stats_with_value('date_count', 'hypno_date_count', 'flirt_count', 'date_outfit', 'dance_outfit', 'forgiveness_count', 'strike_count', 'girlfriend_reward_week', 'girlfriend_reward_count', 'bimbo_outfit', 'bimbo_joke_count', 'bimbo_set_1_countdown')
    rae.boudoir_photos_sent = False
    rae.selfies_sent = False
    rae.date_spank = False
    rae.dildo_reward_triggered = False
    rae.first_date_complete = False
    rae.fluffy_cuffs_reward_triggered = False
    rae.hypno_girlfriend_tried_breakup = False
    rae.wants_to_be_girlfriend_message_not_given = True
    rae.dancing_at_club = False
  return

# Display Portrait
# CHARACTER: Display Portrait
label rae_update_media:
    if rae.location == eros_store and rae.has_tag('working_at_store'):
        $ rae.change_image('store_clerk_working')
    elif rae.location == stage:
        if rae.has_tag('watched_today'):
            if rae.dance_outfit == 1:
                $ rae.change_image('store_clerk_stripper_image')
            elif rae.dance_outfit == 2:
                $ rae.change_image('store_clerk_strip_outfit_2_8')
            else:
                $ rae.change_image('store_clerk_strip_outfit_3_1')
        else:
            # note: image references are offset by one so she shows the next dance outfit she will wear
            if rae.dance_outfit == 1:
                $ rae.change_image('store_clerk_strip_outfit_2_8')
            elif rae.dance_outfit == 2:
                $ rae.change_image('store_clerk_strip_outfit_3_1')
            else:
                $ rae.change_image('store_clerk_stripper_image')
    elif rae.has_tag('bimbo'):
        # set initial Bimbo image in conversion label, changes as you conduct Bimbo actions
        pass
    elif rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'):
        pass # set in start date check
    else:
        pass
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label rae_examine:
    if 'talked' in rae.tags and rae.has_tag('working_at_store') and rae.location == eros_store:
        "It's [rae.name], the friendly store clerk for the Eros Store."
    elif rae.has_tag('working_at_store') and rae.location == eros_store:
        "[rae.full_name] smiles at you."
        add tags 'examined' to rae
    elif rae.location == stage:
        "When you met her, she worked retail. Now Rae the Showgirl is the hardest working dancer at The Club. All those years working with lingerie have really paid off. Her outfits are as nice as any dancer in the joint."
    elif rae.has_tag('bimbo'):
        "Rae the Bimbo worked in a retail store when you first met her. It's hard to imagine her being able to handle such a big responsibility now."
    elif rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'):
        call rae_relationship_status from _call_rae_relationship_status
        wt_image rae.image
    else:
        pass
    return

# Talk to Character
label rae_talk:
    wt_image store_clerk_working
    if rae.has_tag('talked'):
        rae.c "Let me know if I can help you with anything."
    else:
        rae.c "Hi! My name is Rae. If I can help you with anything, just let me know."
        #"She's friendly and pretty, but her nasally voice makes you think of Fran Drescher. It's a bit grating, sort of like trying to read aqua blue on white." ## not needed now that her font is very easy to read
        $ rae.change_full_name("", "Rae", "the Store Clerk")
        add tags 'talked' to rae
        rem tags 'no_hypnosis' from rae
    if not rae.has_tag('no_flirting') and not rae.has_tag('flirting'):
        call rae_initial_flirt from _call_rae_initial_flirt
    return

label rae_initial_flirt:
    $ title = "Flirt with her?"
    menu:
        "Flirt with her":
            player.c "You'd best be careful, Rae.  A guy could get the wrong idea."
            rae.c "What do you mean?"
            player.c "A beautiful woman like you.  A man's mind starts to reel at the thought of your help."
            if player.has_tag('supersexy'):
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                wt_image store_clerk_working_5
                "She blushes and laughs."
                rae.c "Oh, please.  I'm sure women are more than happy to help you any chance they get."
                wt_image store_clerk_working_2
                "Rae makes herself scarce, but every now and then you catch her looking at you, a big smile on her face. She may be a bit smitten with you."
                $ player.desire_action_count += 1
                add tags 'flirting' to rae
            else:
                wt_image store_clerk_working_5
                rae.c "Ah, that's sweet of you.  I'll be working over here if you need anything."
                wt_image store_clerk_working_7
                "Rae makes herself scarce.  She doesn't seem to be the flirty type.  Not with you, anyway."
                add tags 'no_flirting' to rae
        "Just shop":
            pass
    return

# Hypnosis
label rae_hypnosis_start:
    $ ignore_context_change = True # this breaks the hypno sequence; note: this also means the normal hypno trigger implant sequence doesn't work, as Rae's trigger gets implanted differently
    if rae.location == eros_store and rae.can_be_interacted:
        $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
        $ rae.hypno_session() # this deducts energy and records that she's been hypno'd
        # Start Scene Dialog
        wt_image rae.image
        "You're alone in the store with Rae.  You decide to make use of this opportunity."
        player.c "Rae, could you please look at this for me."
        call focus_image from _call_focus_image_34
        player.c "Rae, you want to help me. I'm a customer, and it's your job to help the customers."
        wt_image store_clerk_hypnotized_1
        player.c "It's your job to please the customers, Rae, and you're good at your job. You're good at pleasing the customers. It's good to please the customers. It's right to please the customers."
        wt_image store_clerk_hypnotized_2
        player.c "Please me now, Rae. Lower your top so that I can see your breasts. That will please me. You want to please the customers."
        wt_image store_clerk_hypnotized_bare_breasts_5
        # First session
        if rae.hypno_count == 0:
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            player.c "Good girl, Rae.  That pleases me very much."
            wt_image store_clerk_hypnotized_bare_breasts_1
            "That's enough for her first session. You work on lowering her resistance to your suggestions, then have her cover herself up before you bring her out of her trance."
            wt_image store_clerk_working_3
            rae.c "Ummm ... I need to go re-stock these."
            wt_image eros_store.image
            "Rae wanders off to another corner of the store."
        # Second session
        elif rae.hypno_count == 1:
            # only progress if hypnosis level high enough or playboy
            if player.test('hypnosis_level', 9) or player.has_tag('supersexy'):
                "Rae is quickly accepting the idea that as a customer in her store, it's important for her to please you.\n"
                "Do you want to see how far she's willing to go to please you?"
                $ title = "What do you do?"
                menu:
                    "That's enough for today":
                        "Rae's acceptance of your control is coming along nicely. You work on lowering her resistance to your suggestions even further, then have her cover herself up before you bring her out of her trance."
                        wt_image store_clerk_working_3
                        rae.c "Ummm ... I need to go re-stock these."
                        "Rae wanders off to another corner of the store."
                    "Push her":
                        call rae_store_hypno_naked from _call_rae_store_hypno_naked
            else:
                "Rae takes off her top to show you her breasts, but she's not attracted to you, and she's unwilling to go any further to please you."
                wt_image store_clerk_hypnotized_bare_breasts_1
                "Perhaps if you were a stronger hypnotist or if she were more attracted to you, you could break down her resistance, but as it is you'll have to settle for a view of her pretty tits."
                wt_image store_clerk_working_3
                "When you're finished admiring her assets, you have her cover herself up and bring her out of her trance."
                rae.c "Ummm ... I need to go re-stock these."
                wt_image eros_store.image
                "Rae wanders off to another corner of the store."
                $ rae.hypno_count -= 1
        # Third session
        elif rae.hypno_count == 2:
            "Rae now accepts the idea that as a customer in her store, it's important for her to please you. Do you want to see how far she's willing to go to please you?"
            wt_image store_clerk_hypnotized_bare_breasts_1
            $ title = "What do you do?"
            menu:
                "Tell her to get naked":
                    call rae_store_hypno_naked from _call_rae_store_hypno_naked_1
                "Push her further":
                    call rae_store_hypno_bj from _call_rae_store_hypno_bj
        # Fourth+ Session
        else:
            "Rae now fully accepts the idea that as a customer in her store, it's important for her to please you."
            wt_image store_clerk_hypnotized_bare_breasts_1
            $ title = "How do you want her to please you?"
            menu:
                "Store discount" if eros_store.discount_ratio > 0.8:
                    player.c "I'm a good customer, Rae. I'm a good customer, and you work very hard to satisfy me. I'm a very good customer, but you don't give me your best prices."
                    player.c "You will remember this when I bring you out of your trance, Rae. You'll remember that I'm a very good customer, and should get your best prices."
                    wt_image store_clerk_hypnotized_2
                    player.c "You'll provide me with a preferred customer discount, Rae.  Now cover yourself up, and on the count of 1, you will wake up.  10, 9, 8, ..."
                    wt_image store_clerk_working
                    rae.c "Oh, I almost forgot!  On behalf of the store, I wanted to thank you for being such a good customer."
                    wt_image store_clerk_working_5
                    rae.c "I'm going to go arrange for a store discount card for you.  As a preferred customer, it'll give you 20% off all of our regular priced items."
                    wt_image store_clerk_working_7
                    "Rae gets your discount card set up as you finish your shopping."
                    $ eros_store.discount_ratio = 0.8
                "Just get naked":
                    call rae_store_hypno_naked from _call_rae_store_hypno_naked_2
                "Blowjob":
                    call rae_store_hypno_bj from _call_rae_store_hypno_bj_1
                "Sex" if rae.hypno_blowjob_count > 2:
                    player.c "Rae, I'm not a satisfied customer. I'm not happy. There's something in the changing room I'm not happy about."
                    wt_image store_clerk_hypnotized_bare_breasts_3
                    "Rae follows you into the changing room, a concerned look on her face."
                    wt_image store_clerk_hypnotized_bare_breasts_6
                    "When you get to the change room, Rae looks down at your bulging pants."
                    if rae.hypno_sex_count > 0:
                        wt_image store_clerk_hypnotized_bare_breasts_4
                        player.c "I'm not a happy customer, Rae. I'm not satisfied. I cannot be satisfied while you deny me the use of your body."
                        wt_image store_clerk_bj_5
                        "Rae trembles as she kneels in front of you and takes your cock into her mouth."
                        wt_image store_clerk_bj_4
                        player.c "No, Rae. You putting your mouth on me is not going to satisfy me today. To satisfy me today, you need to let me put my cock inside you. Spread your legs, Rae, to take my cock inside you and make your customer happy."
                        wt_image store_clerk_hypnotized_sex_2
                        "She wants to object, but all she can hear in her head is {i}'Make your customer happy'{/i}."
                        $ title = "Take her like this?"
                        menu:
                            "Fuck her like this":
                                wt_image store_clerk_hypnotized_sex
                                "She watches your face as you fuck her, looking for confirmation that you'll be a satisfied customer after this."
                                wt_image store_clerk_sex_3
                                "She takes the look of pleasure on your face as you fill her with cum as confirmation that she's done the right thing."
                            "Tell her to turn over":
                                wt_image store_clerk_hypnotized_sex_3
                                "Rae flips over to accept your cock from behind, hoping that she's doing the right thing and that you'll be a satisfied customer after this."
                                wt_image store_clerk_hypnotized_sex_4
                                "She takes the sound of pleasure that you make as you fill her with cum as confirmation that she's done the right thing."
                    else:
                        player.c "Rae, I've been a good customer. I've shopped here many times. However, not once have you offered me your body for my pleasure."
                        wt_image store_clerk_hypnotized_bare_breasts_4
                        player.c "I'm not a happy customer, Rae. I'm not satisfied. I cannot be satisfied while you deny me the use of your body."
                        wt_image store_clerk_bj_5
                        "Rae trembles as she kneels in front of you and takes your cock into her mouth."
                        wt_image store_clerk_bj_4
                        player.c "No, Rae. You putting your mouth on me is not going to satisfy me today."
                        player.c "You want to make me happy. You want to satisfy me. You can make me happy by letting me put my cock inside you."
                        player.c "Lie back and spread your legs for me. Let me put my cock inside you, and I'll be a happy customer. Then you'll have succeeded at satisfying your customer."
                        wt_image store_clerk_bj_1
                        "Rae shakes as she struggles with your instructions. She knows this is wrong, knows that she shouldn't have your cock in her mouth, let alone be having sex with customers."
                        "But your voice keeps pounding in her head ... {i}'Make your customer happy. Make me happy.'{/i}"
                        wt_image store_clerk_hypnotized_sex_2
                        "To make the pounding in her head go away, she lies back and spreads her legs, hoping that maybe if she does this just once, maybe you'll be quick and happy with her service."
                        wt_image store_clerk_hypnotized_sex
                        "She watches your face as you fuck her, looking for confirmation that you'll be a satisfied customer after this."
                        wt_image store_clerk_sex_3
                        "She takes the look of pleasure on your face as you fill her with cum as confirmation that she's done the right thing."
                    player.c "[player.orgasm_text]"
                    orgasm notify
                    $ rae.hypno_sex_count += 1
                    wt_image store_clerk_working_6
                    "When you're done, you command her to forget what happened, and she goes back to her work elsewhere in the store."
                "Date" if rae.hypno_count > 4:
                    player.c "Rae, I want you to come on a date with me."
                    if rae.hypno_date_count == 0:
                      "You can see the struggle in Rae. She's accepted the idea that as her customer, she should work hard while you are in the store to make sure you are happy. Outside of the store, however, she sees no obligation towards you."
                      rae.c "I ... I'm sorry.  You're not my type."
                      if rae.hypno_sex_count == 0:
                          "She doesn't see you as boyfriend material. Perhaps you should do something with Rae that she'll associate as boyfriend-girlfriend behavior?"
                          $ rae.temporary_count = 0
                      else:
                          player.c "Rae, I want you to remember, just until I bring you out of this trance, something that I asked you to forget about before.\n"
                          player.c "Rae, do you remember now that you and I have had sex?"
                          rae.c "No, we ... Oh!  Yes, I guess we did ... but ..."
                          player.c "Rae, are you a slut?"
                          rae.c "No! No ... I'm not a slut!"
                          player.c "If you're not a slut, Rae, and you had sex with me, you must see me as boyfriend material.  Why would you sleep with me unless you saw me as someone you could date?"
                          rae.c "I ... I'm not sure ... I guess, maybe.  Maybe you're right."
                          player.c "I am right, Rae. You're not a slut, so if you slept with me, you must want to date me."
                          player.c "In a moment, I'll tell you to come out of this trance temporarily. When your shift ends this afternoon, you will look for me outside. When you see me, you will go back into this trance, and then you'll come on a date with me."
                          $ rae.temporary_count = 1
                    else:
                        "You can see the struggle in Rae. She's accepted the idea that as her customer, she should work hard while you are in the store to make sure you are happy. Outside of the store, however, she sees no obligation towards you."
                        rae.c "I ... I'm sorry.  You're not my type."
                        player.c "Don't be silly, Rae. You want to go on another date with me. We've dated before, and I've been good to you. I want you to remember that now."
                        rae.c "No, we ... Oh!  Yes, I guess we did ... but ..."
                        player.c "Remember what we did at the end of our last date, Rae. You wouldn't have done that if you didn't enjoy our date and want to date me again."
                        rae.c "I ... I'm not sure ... I guess, maybe.  Maybe you're right."
                        player.c "I am right, Rae. When your shift ends this afternoon, you will look for me outside.  When you see me, you will go back into this trance, and then you'll come on a date with me."
                        $ rae.temporary_count = 1
                    # proceed
                    if rae.temporary_count == 1:
                        $ rae.temporary_count = 0
                        $ rae.hypno_date_count += 1
                        if rae.hypno_date_count == 1:
                            call forced_movement(outdoors) from _call_forced_movement_4
                            summon rae
                            wt_image store_clerk_hypno_date_1
                            "Later that day, when her shift is over, Rae steps out of the store. She's changed her clothes. That explains why she's always dressed in the same turquoise outfit in the store - it's her store uniform!"
                            "As soon as she steps outside, she feels compelled to look around.  When she sees you, she falls back into a trance and comes over to your car."
                            wt_image store_clerk_restaurant_1
                            "You take her to a restaurant. Not the nicest restaurant in town, but they serve a good meal."
                            wt_image store_clerk_hypno_date_6
                            "Rae isn't the best conversationalist, even when she isn't hypnotized.  Under the effect of your trance, over dinner she offers nothing other than what you tell her to say."
                            wt_image store_clerk_cinema_1
                            "After the restaurant, you take her to a movie."
                            wt_image store_clerk_hypno_date_5
                            "She sits quietly beside you, pulling away when you try to touch her in the dark. In the quiet of the theater, you can't talk her into being more affectionate, so you bide your time."
                            wt_image store_clerk_garage_1
                            "When the movie's over, you drive her to a parking garage."
                            wt_image store_clerk_hypno_date_2
                            player.c "Rae, after a date, it's normal to thank your date."
                            rae.c "Thank you for the date."
                            player.c "Not just with words, Rae. Thank me properly. You want your date to be happy. You want him to like spending time with you."
                            player.c "You don't go on dates so that men will spend money on you, do you? Did you go out with me just so I would buy you a meal and pay for you to watch a movie?"
                            rae.c "No"
                            player.c "It's not difficult to make me happy, Rae. You just need to suck my cock, the way you do at the store."
                            player.c "I took you on a date. You want me to enjoy our date. You don't want me to go home unhappy. You'll suck my cock at the store, so why shouldn't you suck my cock after a date, too?"
                            wt_image store_clerk_hypno_date_15
                            "Under the weight of your words, Rae kneels down beside the car in the parking garage and frees your member.  You take her by the hair ..."
                            wt_image store_clerk_hypno_date_3
                            "... and guide her head back and forth as she blows you."
                            if rae.hypno_facial_count > 0:
                                wt_image store_clerk_hypno_date_7
                                $ rae.hypno_facial_count += 1
                            else:
                                $ rae.hypno_swallow_count += 1
                            player.c "[player.orgasm_text]"
                            $ rae.hypno_blowjob_count += 1
                            orgasm
                        else:
                            $ rae.temporary_count = 1
                            call forced_movement(outdoors) from _call_forced_movement_6
                            summon rae
                            wt_image store_clerk_hypno_date_1
                            "When her shift is over, Rae steps out of the store, feeling compelled to look around. When she sees you, she falls back into a trance and comes over to your car."
                            wt_image store_clerk_cinema_1
                            "Skipping the restaurant this time, you take her straight to a movie."
                            wt_image store_clerk_hypno_date_5
                            "Sitting quietly in the dark, you try to touch her, but she's still disinterested in being affectionate."
                            if rae.has_tag('trigger_implanted'):
                                $ title = "Convince her to be affectionate?"
                                menu:
                                    "Yes, use her trigger":
                                        $ rae.temporary_count = 0
                                        player.c "[rae.trigger_phrase].  Do you understand, Rae?"
                                        rae.c "Yes"
                                        player.c "I want to enjoy the rest of the movie, Rae."
                                        wt_image store_clerk_hypno_date_8
                                        "With her lips wrapped around your cock, you're able to enjoy the movie just fine."
                                        if rae.hypno_facial_count > 0:
                                            wt_image store_clerk_hypno_date_9
                                            player.c "[player.orgasm_text]"
                                            "The walk out of the theatre is fun, too."
                                            $ rae.hypno_facial_count += 1
                                        else:
                                            player.c "[player.orgasm_text]"
                                            $ rae.hypno_swallow_count += 1
                                        $ rae.hypno_blowjob_count += 1
                                        orgasm
                                    "No, wait until after the movie":
                                        pass
                            if rae.temporary_count == 1:
                                $ rae.temporary_count = 0
                                wt_image store_clerk_garage_1
                                "After the movie, you drive her to a parking garage."
                                wt_image store_clerk_hypno_date_2
                                player.c "Rae, after a date, it's normal to thank your date."
                                rae.c "Thank you for the date."
                                player.c "Not just with words, Rae. Thank me properly. You want your date to be happy. You want him to like spending time with you."
                                rae.c "Do you want me to suck your cock?"
                                $ title = 'Do you want her to suck your cock?'
                                menu:
                                    "Yes, a blowjob would be nice":
                                        player.c "That would be very nice, Rae."
                                        wt_image store_clerk_hypno_date_15
                                        "Rae kneels down beside the car in the parking garage and frees your member.  You take her by the hair ..."
                                        wt_image store_clerk_hypno_date_3
                                        "... and guide her head back and forth as she blows you."
                                        if rae.hypno_facial_count > 0:
                                            wt_image store_clerk_hypno_date_7
                                            $ rae.hypno_facial_count += 1
                                        else:
                                            $ rae.hypno_swallow_count += 1
                                        player.c "[player.orgasm_text]"
                                        orgasm
                                        $ rae.hypno_blowjob_count += 1
                                    "No, she should fuck you":
                                        if rae.has_tag('trigger_implanted'):
                                            player.c "A blow job would be nice, but you'd rather fuck me."
                                            rae.c "I would?"
                                            player.c "Of course. You've been going on dates with me, and having sex with me. You wouldn't do that if you didn't want to, would you?"
                                            rae.c "I guess not."
                                            wt_image store_clerk_hypno_date_4
                                            "She bends herself over the hood of the car and lets you fuck her. She's actually wet as you enter her ..."
                                            rae.c "oohhh"
                                            wt_image store_clerk_hypno_date_13
                                            "... and only gets wetter as you plow her. You continue until she climaxes hard around your dick."
                                            rae.c "ooohhhhh ... yeesss!"
                                            wt_image store_clerk_hypno_date_11
                                            "She enjoyed her orgasm, and she seems to enjoy feeling you have yours inside her."
                                            rae.c "mmmmmmm"
                                            player.c "[player.orgasm_text]"
                                            $ rae.hypno_orgasm_count += 1
                                            "She's in a vulnerable state. If you want, you can use her trigger to make her your hypno-girlfriend."
                                            $ title = "Make her your hypno-girlfriend?"
                                            menu:
                                                "Yes":
                                                    "Rae's not going to be easy to maintain as your girlfriend. It's not in her nature to be with a man who has other lovers."
                                                    "You won't be able to have her live in your house, as she'd never understand or accept your work."
                                                    "So the more relationships that you retain with other women, the more effort it will be to allay Rae's suspicions about them."
                                                    $ title = "Proceed anyway?"
                                                    menu:
                                                        "Make her your hypno-girlfriend":
                                                            player.c "You're my girlfriend, Rae."
                                                            rae.c "I'm not sure I want to ..."
                                                            player.c "[rae.trigger_phrase], Rae.  You are my girlfriend."
                                                            rae.c "Yes.  I'm your girlfriend."
                                                            call convert(rae, 'hypno_girlfriend') from _call_convert_42
                                                            call rae_convert_girlfriend from _call_rae_convert_girlfriend_1
                                                        "Not now":
                                                            pass
                                                "Not now":
                                                    pass
                                        else:
                                            player.c "We've been going on dates, Rae. You let me fuck you at the store. You should let me fuck you after a date, too. That's what a girl does with a boy she likes.  "
                                            player.c "You're not a girl who goes out just so her date can spend money on her, and who only fucks men in her store. You're the type of girl who saves herself for the boy she dates, aren't you?"
                                            "Rae is full of conflict. She doesn't think she should be having sex with you, but your words in her head keep battering at her, making her doubt herself."
                                            "Maybe she should be having sex with you after your date. The things she's done already, they would make more sense if it was because she liked you and wanted you to be her boyfriend."
                                            "She gives a small nod and you know her resistance has crumbled."
                                            rae.c "Should we go back to your place?"
                                            player.c "Maybe later. Here will do for now. Get out of the car."
                                            wt_image store_clerk_hypno_date_10
                                            player.c "Bend over, Rae."
                                            wt_image store_clerk_hypno_date_4
                                            "She offers no resistance as you guide her over the hood of the car and pull her pants and panties down. You fuck her roughly from behind, taking joy in the feeling of her tight hot pussy around you."
                                            wt_image store_clerk_hypno_date_11
                                            "She's barely wet when you start, but her body soon reacts to the hard pounding.  She doesn't cum, but she enjoys it more than she thought she would. You, of course, enjoy it even more."
                                            player.c "[player.orgasm_text]"
                                            wt_image store_clerk_hypno_date_12
                                            "You've fucked the last of her resistance out of her. You can now implant a hypnotic trigger that may allow you to influence her behavior in the future."
                                            $ title = "What trigger phrase do you want to use?"
                                            menu menu_rae_choose_trigger_phrase:
                                                "[rae.trigger_phrase]":
                                                    pass
                                                "Choose something else":
                                                    $ rae.trigger_phrase = renpy.input(_("What trigger phrase do you give Rae?"))
                                                    jump menu_rae_choose_trigger_phrase
                                            player.c "Rae, when you hear the phrase, '[rae.trigger_phrase]' you will obey the speaker of the phrase, and do everything that they tell you.  Do you understand?"
                                            rae.c "Yes. When I hear, '[rae.trigger_phrase]', I will do as I'm told."
                                            add tags 'trigger_implanted' to rae
                                        orgasm
                                        $ rae.hypno_sex_count += 1
                        "After you've had your fun, you take Rae back to her place, and then you drive yourself home."
                        call forced_movement(living_room) from _call_forced_movement_143
                        call character_location_return(rae) from _call_character_location_return
                        notify
                    else:
                        "You're unable to do anything more with her today, so you bring her out of her trance."
                        wt_image store_clerk_working_3
                        rae.c "Ummm ... I need to go re-stock these."
                        wt_image eros_store.image
                        "Rae wanders off to another corner of the store."
    elif rae.has_tag('hypno_girlfriend'):
        "She's already hypnotized."
    elif rae.has_tag('on_date'):
        sys "She's here for your date.  Why spoil that?  (Plus Wife Trainer hasn't added any content since hypnotizing her in your house became possible.)"
    else:
        "You can't hypnotize her right now."
    # normally hypnosis would now go on to hypnosis menu followed by trigger implant test and hypnosis end, but these are all disable for Rae
    return

label rae_store_hypno_naked:
    player.c "Your breasts are very nice, Rae, but I'm not satisfied. It's important that your customers be satisfied. Fully satisfied."
    player.c "You're a good clerk and you make sure all your customers are satisfied. You want customers to leave happy, don't you? You'll do anything you need to make your customers happy."
    player.c "I'm not satisfied with the clothes you're wearing, Rae. They're distracting me from the lingerie you're selling in the store."
    player.c "I'm not happy that you're wearing clothes that distract me from the clothes you want to sell me."
    wt_image store_clerk_hypnotized_bare_breasts_2
    player.c "You want your customers to be happy, don't you? I'm a customer, and you want me to be happy. You want to do what it takes to make me happy, Rae."
    wt_image store_clerk_hypnotized_naked_1
    "Rae removes her clothes and squats down to give you a better view of the lingerie for sale."
    wt_image store_clerk_hypnotized_naked_3
    "Not that you're looking at the lingerie right now. You work on lowering her resistance while she stares up at you."
    wt_image store_clerk_hypnotized_naked_2
    "She makes no move to cover herself up until you tell her to. You leave her like this for a while before bringing her out of her trance."
    wt_image store_clerk_working_3
    rae.c "Ummm ... I need to go re-stock these."
    "Rae wanders off to another corner of the store."
    return

label rae_store_hypno_bj:
    player.c "Rae, I'm not a satisfied customer. I'm not happy. There's something in the changing room that I'm not happy about."
    player.c "You're a good clerk. You make sure all of your customers are satisfied. You want customers to leave happy, don't you? You'll do anything you need to make the customers happy."
    player.c "You want to make me happy, Rae. You want to please me and satisfy me. You'll come into the changing room, Rae. You'll come into the changing room and make sure that I'm happy."
    wt_image store_clerk_hypnotized_bare_breasts_3
    "Rae follows you into the changing room, a concerned look on her face."
    wt_image store_clerk_hypnotized_bare_breasts_4
    player.c "Rae, the sight of your breasts has made me excited. You've teased me, Rae, and made my cock hard. But you haven't tried to relieve my hard cock. You haven't done anything to make me feel better."
    wt_image store_clerk_hypnotized_bare_breasts_6
    player.c "I'm not a happy customer, Rae. I'm not satisfied. I can't be fully satisfied while my cock is hard."
    wt_image store_clerk_bj_10
    player.c "You want to make me happy. You want to satisfy me. Satisfy me now, Rae. Deal with my problem so that I leave here a happy customer."
    wt_image store_clerk_bj_5
    "Rae trembles as she takes your cock into her mouth."
    wt_image store_clerk_bj_1
    "She knows this isn't something she should be doing, but she's happy that your concern is one she can deal with, and she rationalizes her behavior as taking the initiative."
    if rae.hypno_blowjob_count > 0:
        $ title = "Where do you want to cum?"
        menu:
            "In her":
                wt_image store_clerk_bj_4
                "She pays close attention to you as she blows you, watching to make sure she's making you happy, until you fill her mouth with confirmation that you are."
                player.c "[player.orgasm_text]"
                wt_image store_clerk_bj_11
                player.c "Did you swallow it all, Rae?"
                "She nods ..."
                wt_image store_clerk_bj_9
                "... and demonstrates that she did."
                $ rae.hypno_swallow_count += 1
            "On her":
                if rae.facial_count == 0:
                    wt_image store_clerk_bj_4
                    player.c "Cumming in your mouth isn't going to be enough to make me happy today, Rae. To make me a satisfied customer, I need to cum on you. Understood?"
                    wt_image store_clerk_bj_11
                    "She nods and removes your cock from her mouth."
                wt_image store_clerk_bj_8
                player.c "[player.orgasm_text]"
                $ rae.hypno_facial_count += 1
    else:
        wt_image store_clerk_bj_4
        "She pays close attention to you as she blows you, watching to make sure she's making you happy, until you fill her mouth with confirmation that you are."
        player.c "[player.orgasm_text]"
        $ rae.hypno_swallow_count += 1
    $ rae.hypno_blowjob_count += 1
    orgasm notify
    wt_image store_clerk_working_6
    "When you release her from her trance, she starts working elsewhere in the store as if nothing has happened."
    return

label rae_hypnosis_end:
    # note: don't think you ever reach this
    pass
    return

### Character Specific Actions
## Store Actions
label rae_flirt:
    $ rae.flirt_count += 1
    wt_image store_clerk_working
    if rae.flirt_count == 1:
        $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
        rae.c "Hello!"
        player.c "Hi, Rae.  How's your day going?"
        wt_image store_clerk_working_1
        rae.c "Okaaay.  I mean, it's a bit boring, but it's nice to see you again.  How's your day?"
        player.c "Not bad, but I'm sure you could help make it a little brighter."
        wt_image store_clerk_working_2
        "Rae bites her lip for a moment as if debating what to do."
        rae.c "I ... I'd like to help you, but I don't think I know what you like."
        "You give her a big smile."
        player.c "I like you, Rae.  I'm sure that could help give you some ideas."
        wt_image store_clerk_working_18
        "She blushes. It looks like she wants to say something more to you, but she's too shy, and simply walks away."
        wt_image store_clerk_working_5
        "She gives you some space while you browse, but every now and then you catch her looking at you, a big smile on her face."
    if rae.flirt_count == 2:
        $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
        rae.c "Hello!"
        player.c "Hi, Rae.  How's your day going?"
        wt_image store_clerk_working_1
        rae.c "Okaaay.  I mean, it's a bit boring, but it's nice to see you again.  How's your day?"
        player.c "Not bad, but I'm sure you could help make it a little brighter."
        rae.c "Well, how could I do that?"
        player.c "Perhaps you could show me something in the store I might be interested in?"
        wt_image store_clerk_working_6
        rae.c "Well, the last time you said maybe I could give you some ideas, so I was looking around."
        wt_image store_clerk_working_8
        rae.c "I really love the color of this. Depending on your girlfriend's shape, it might look really good on her."
        wt_image store_clerk_working_19
        rae.c "Or if she looks better in richer colors, this is nice."
        player.c "Why did you think I had a girlfriend?"
        rae.c "You're shopping for lingerie."
        player.c "That's part of my work."
        wt_image store_clerk_working_9
        rae.c "You shop for lingerie as part of your work?"
        player.c "I help married couples with their relationships. Sometimes gifts of lingerie help. That outfit looks nice. I wonder what it looks like while someone is wearing it?"
        rae.c "Well, ummm.  You're not shopping for a girlfriend?"
        player.c "No.  It's business."
        wt_image store_clerk_working_19
        rae.c "I could ... ummm, if you want ..."
        player.c "That'd be great, Rae."
        wt_image eros_store.image
        "Rae ducks into the changing room.  After a few minutes, she opens the door."
        wt_image store_clerk_working_20
        rae.c "I'm ready, I guess."
        wt_image store_clerk_working_10
        player.c "That looks nice."
        rae.c "Thaaanks!  It's a bit revealing."
        wt_image store_clerk_working_11
        player.c "Not at all.  I'd like to see more."
        rae.c "More?  I'm not sure there's anything more I can show you."
        player.c "Sure there is.  Come out and let me have a good view."
        wt_image store_clerk_working_12
        "She steps out and lets you turn her around. She's breathing heavy and it's clear she's appreciating the attention you're showing her."
        wt_image eros_store.image
        "Perhaps embarrassed by her boldness, she runs away and hides after the show is over."
        call character_location_return(rae) from _call_character_location_return_1
    if rae.flirt_count == 3:
        $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
        rae.c "Hello!"
        player.c "Hi, Rae.  How's your day going?"
        rae.c "Okaaay.  I mean, it's a bit boring, but it's nice to see you again.  How's your day?"
        player.c "Not bad, but I'm sure you could help make it a little brighter."
        rae.c "Well, how could I do that?"
        player.c "Perhaps you could show me something in the store I might be interested in?"
        wt_image store_clerk_working_2
        "Rae bites her lip for a moment as if debating what to do.  Then she takes a quick look around the store ..."
        wt_image store_clerk_flashing_4
        "... and pulls down her top."
        wt_image store_clerk_flashing_1
        rae.c "I was thinking after your last visit that, maybe ... possibly these were more of what you were hoping to see? Do they help make your day brighter?"
        player.c "They certainly do.  You certainly do, Rae."
        "Rae lets you stare for just a moment ..."
        wt_image store_clerk_working_2
        "... then laughs and covers herself. She ducks into the next aisle and busies herself with refolding and organizing the lingerie, perhaps a little embarrassed at her boldness."
        "Every now and then you catch her staring at you as you browse."
    if rae.flirt_count == 4:
        player.c "Hi, Rae.  How are you today?"
        "She smiles brightly, happy to see you but a little nervous. Perhaps she's embarrassed by the memory of her prior boldness."
        rae.c "Good ... and how are you?"
        player.c "Very good, thank you. I've been thinking about what you showed me all week."
        "Rae laughs."
        rae.c "Have you now, and is that why you're back? They can't be that special."
        player.c "You shared them with me. That makes them very special to me, Rae."
        wt_image store_clerk_working_5
        "Rae laughs again. She starts to go back to her work ..."
        wt_image store_clerk_working_16
        "... then nervously turns to face you."
        rae.c "I suppose you were hoping to get another look?"
        $ title = "How do you respond?"
        menu:
            "Yes, please":
                wt_image store_clerk_flashing_1
                "Rae lets you stare as long as you want today.  She seems to be enjoying your attention."
                player.c "Thank you, Rae.  You truly are beautiful."
                wt_image store_clerk_working_5
                "She laughs again and disappears to another corner of the store."
                $ rae.flirt_count -= 1
            "Actually, I was hoping to see something else":
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                player.c "Perhaps you could show me something else?"
                rae.c "Ummm ... What exactly are you asking for?"
                player.c "For you to help show me some lingerie, Rae.  Why, what did you think I meant?"
                wt_image store_clerk_working_17
                "She laughs, nervously."
                rae.c "Oh, sorry.  Of course.  I'm sure seeing my breasts again would bore you."
                wt_image store_clerk_working_6
                "You leave that comment lie for the moment as she looks through more of the store's items."
                wt_image store_clerk_working_15
                "The review of her store's inventory allows you to talk to Rae about what you find attractive in a woman. You make sure that Rae can interpret all of your comments as approval of her body shape."
                wt_image store_clerk_working_4
                "You get closer and closer to her as she shows you more and more items. Eventually, you're close enough to whisper in her ear softly."
                wt_image store_clerk_hypnotized_1
                player.c "I have a confession, Rae. I did come here today to see you. I do want to see your body again. In fact, I want to do more than just see your body."
                wt_image store_clerk_working_5
                "Rae takes a deep breath, then smiles at you and silently leads you to the changing room."
                wt_image store_clerk_bj_3
                "She closes the changing room door behind you and strips out of her clothes."
                wt_image store_clerk_bj_5
                "A moment later she's on her knees in front of you, your cock in her mouth."
                wt_image store_clerk_bj_1
                rae.c "I've been thinking about you since your first visit."
                player.c "I've been thinking of you, too, Rae.  I am really enjoying this."
                "The rest of the blow job takes place in silence. As you get close to cumming, she removes your cock from her mouth ..."
                wt_image store_clerk_bj_8
                player.c "[player.orgasm_text]"
                "... and lets you cum all over her chest."
                wt_image store_clerk_bj_2
                rae.c "I hope you know I don't normally do this with customers."
                player.c "Which?  The blow job, or letting them cum on you?"
                rae.c "Both. You're probably the sort of guy who has women throwing themselves at you all the time. I wanted to do something you'd remember. Did you like it?"
                player.c "I did, Rae.  Thank you."
                "It seems Rae likes you."
                $ rae.blowjob_count += 1
                $ rae.facial_count += 1
                $ player.desire_action_count += 1
                orgasm notify
        call character_location_return(rae) from _call_character_location_return_2
    if rae.flirt_count == 5:
        "Rae smiles brightly. She's totally smitten with you."
        rae.c "Hiii!  I was hoping you would drop by."
        player.c "It's nice to see you again, too, Rae."
        "You wait, and allow the silence to hang between you.  Finally, Rae breaks it."
        wt_image store_clerk_working_2
        rae.c "Sooo ... I have something else I'd like to show you."
        wt_image store_clerk_flashing_2
        "Rae pulls up her skirt, providing a view of her pussy through her see-through underwear. She waits nervously, wondering if you'll accept her obvious offer."
        $ title = "What do you say?"
        menu:
            "Just show me your breasts again, Rae":
                $ rae.flirt_count -= 1
                call rae_flirt_breasts from _call_rae_flirt_breasts
            "Lovely, but I want you on your knees, Rae":
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                $ rae.flirt_count -= 1
                call rae_flirt_bj from _call_rae_flirt_bj
            "I think I should have a closer look, don't you?":
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                wt_image store_clerk_flashing_3
                rae.c "I was hoping that might be something that interests you."
                wt_image store_clerk_working_13
                "Rae practically dances as she leads you into the changing room ..."
                wt_image store_clerk_bj_3
                "... where she trembles so much, that she can barely get her clothes off."
                wt_image store_clerk_sex_4
                "Your efforts to lay her back so you can examine her properly are hampered - in a good way - by her eagerness to kiss you."
                wt_image store_clerk_sex_5
                "Eventually you're able to disentangle yourself from her mouth and take a closer look at her pussy."
                player.c "Is this what you wanted to show me, Rae?"
                rae.c "yeesss"
                player.c "It's wet, Rae. Very wet."
                rae.c "Uh huh ... I know."
                $ title = "What do you do?"
                menu:
                    "Lick her":
                        wt_image store_clerk_sex_6
                        "She's literally shaking as your tongue touches her, and writhing in orgasmic bliss after only a few licks."
                        rae.c "ooohhhhh ... yeesss!"
                        $ rae.orgasm_count += 1
                        wt_image store_clerk_sex_7
                        rae.c "You don't have to stop there."
                        player.c "You want me to keep licking you?"
                        rae.c "I want you to fuck me."
                        $ title = "Fuck her?"
                        menu:
                            "Yes":
                                wt_image store_clerk_sex_1
                                "As soon as you have your clothes off, she literally throws herself at you. You're used to women wanting you, but rarely have you seen a woman look so thoroughly happy to have you enter her."
                                wt_image store_clerk_sex_28
                                "She seems to be in bliss from the mere experience of having you inside her, but she makes sure you enjoy things on a more physical level."
                                wt_image store_clerk_sex_27
                                player.c "[player.orgasm_text]"
                                $ rae.sex_count += 1
                                add tags 'sex_today' to rae
                                orgasm notify
                            "Not today":
                                player.c "Not today, Rae."
                                rae.c "What?  But ... why not?"
                                player.c "Perhaps another time."
                                "She doesn't argue, but she's worried she did something wrong, or that maybe you're just not that interested in her."
                                change player energy by -energy_short notify
                    "Fuck her":
                        wt_image store_clerk_sex_1
                        "As soon as you have your clothes off, she literally throws herself at you. You're used to women wanting you, but rarely have you seen a woman look so thoroughly happy to have you enter her."
                        wt_image store_clerk_sex_28
                        "You're not sure she even cums. She seems to be in bliss from the mere experience of having you inside her, but she makes sure you enjoy things on a more physical level."
                        wt_image store_clerk_sex_27
                        player.c "[player.orgasm_text]"
                        $ rae.sex_count += 1
                        orgasm notify
                        add tags 'sex_today' to rae
                    "Leave her":
                        wt_image store_clerk_sex_7
                        player.c "Is that because of me, or are you always this wet?"
                        rae.c "It's because of you, silly."
                        player.c "I'm afraid I don't have time to deal with that today, Rae."
                        wt_image store_clerk_sad
                        rae.c "Oh.  Of course.  I'm sure you're busy.  Maybe ..."
                        player.c "Some other time?  Perhaps."
                        $ rae.flirt_count -= 1
                if rae.has_tag('sex_today'):
                    rem tags 'sex_today' from rae
                    wt_image store_clerk_working_14
                    "Rae looks like she's glowing as she shyly dresses."
                    rae.c "I hope you liked that as much as I did."
                    "She runs off before you can answer."
                    $ player.desire_action_count += 1
        call character_location_return(rae) from _call_character_location_return_3
    if rae.flirt_count > 5:
        if eros_store.discount_ratio > 0.5:
            rae.c "Hiii! I have big news! I spoke to my manager and told him what a great customer you are. He's agreed that I can give you a 50% discount on any future purchases you make here."
            player.c "Wow, that's very nice of you, Rae.  Thank you."
            rae.c "Perhaps we could do something to celebrate?"
            $ eros_store.discount_ratio = 0.5
        elif rae.has_any_tag('girlfriend', 'hypno_girlfriend'):
            rae.c "Hiii!  Does my boyfriend need anything today?"
        else:
            "Rae smiles brightly as you approach.  She's totally smitten with you."
            rae.c "Hiii ... I was hoping you'd drop by. So, ummm. Did you want to do anything?"
            if rae.sex_count > 1 and rae.wants_to_be_girlfriend_message_not_given:
                $ rae.wants_to_be_girlfriend_message_not_given = False
                "She won't come out and say it - she wants you to be the one to ask her - but Rae would like to be your girlfriend."
        $ title = "What do you suggest?"
        menu:
            "Just shop today":
                player.c "I'm only here to shop today."
                wt_image store_clerk_hypnotized_1
                rae.c "Oh, okay."
            "Flash me":
                call rae_flirt_breasts from _call_rae_flirt_breasts_1
                call character_location_return(rae) from _call_character_location_return_4
            "Blow me":
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                call rae_flirt_bj from _call_rae_flirt_bj_1
                call character_location_return(rae) from _call_character_location_return_5
            "Let's have sex":
                $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                call rae_flirt_sex from _call_rae_flirt_sex
                call character_location_return(rae) from _call_character_location_return_6
            "Ask her to be your girlfriend" if rae.sex_count > 1 and not rae.has_any_tag('girlfriend', 'hypno_girlfriend'):
                "Rae isn't what you would call a 'deep' person.  She won't be the best conversationalist, or surprise you very often with new perspectives on life."
                wt_image store_clerk_working_2
                "On the other hand, there's something very appealing about the way she looks adoringly at you with those big brown puppy dog eyes."
                if rae.has_tag('exclusive_girlfriend'):
                    "Rae would never understand or accept what you do for your work. So, you'd need to keep that a secret from her, something that wouldn't be too hard as long as she doesn't move in with you."
                    "Rae also would never accept the idea of being just one of the women in your life. You wouldn't be able to keep her as your girlfriend if you have or take another partner."
                    $ title = "Ask her anyway?"
                else:
                    $ title = "Ask her to be your girlfriend?"
                menu:
                    "Yes, ask her to be your girlfriend":
                        if bedroom.is_empty or not rae.has_tag('exclusive_girlfriend'):
                            $ rae.training_session() ## this adds the 'trained_today' and 'trained_this_week' tags
                            wt_image store_clerk_working_13
                            rae.c "Really? You want me to be your girlfriend?? Oh my gawd, yes! I thought you'd never ask. Let's celebrate!"
                            wt_image store_clerk_sex_29
                            "Rae practically drags you into the change room where she rips off her clothing and yours..."
                            wt_image store_clerk_sex_28
                            "... before impaling herself on you and riding you both to climax."
                            wt_image store_clerk_sex_1
                            rae.c "ooohhhhh ... yeesss!"
                            wt_image store_clerk_sex_27
                            player.c "[player.orgasm_text]"
                            rae.c "That was so amazing ... boyfriend."
                            $ rae.orgasm_count += 1
                            $ rae.sex_count += 1
                            orgasm
                            call rae_convert_girlfriend from _call_rae_convert_girlfriend
                            call character_location_return(rae) from _call_character_location_return_7
                        else:
                            "You already have someone sharing your bedroom. You could hide your work from Rae, but not your other relationships. Better to just leave your relationship with Rae the way it is."
                    "Maybe later":
                        pass
    $ player.desire_action_count += 1
    return

label rae_flirt_breasts:
    wt_image store_clerk_flashing_4
    "Rae tries not to show her disappointment as she gamely drops her top again for your inspection."
    wt_image store_clerk_flashing_1
    "She still enjoys your attention, even if she was hoping for something more today.  You examine her assets for a few minutes, then dismiss her and return to your shopping."
    return

label rae_flirt_bj:
    wt_image store_clerk_bj_10
    "Rae leads you to the changing room and drops to her knees, happy for the chance to please you."
    wt_image store_clerk_bj_5
    "Before long, she's doing exactly that."
    wt_image store_clerk_bj_1
    $ title = "Where do you want to cum?"
    menu:
        "On her again":
            wt_image store_clerk_bj_8
            player.c "[player.orgasm_text]"
            wt_image store_clerk_bj_2
            rae.c "I'm glad this is something you like. I haven't let other boys do this with me. Not that I'm giving any other boys blow jobs right now other than you. I'm a one guy type of girl."
            $ rae.facial_count += 1
        "In her mouth":
            wt_image store_clerk_bj_11
            "As she starts to pull your cock out, you hold her head in place. She looks up at you, watching your face as you fill her mouth with your jizz."
            wt_image store_clerk_bj_4
            player.c "[player.orgasm_text]"
            $ rae.swallow_count += 1
    $ rae.blowjob_count += 1
    wt_image store_clerk_bj_3
    if rae.has_any_tag('girlfriend', 'hypno_girlfriend'):
        rae.c "I hope my boyfriend enjoyed that."
    else:
        "Without looking at you, Rae shyly addresses you as she gets dressed."
        if rae.sex_count == 0:
            rae.c "You knooow ... if you want to go further, it's okay. I wouldn't say no if you wanted to, you know. Next time."
        else:
            rae.c "That was fun, but I don't mind fucking you. If, you know, you wanted to fuck me again. Next time, I mean."
    return

label rae_flirt_sex:
    $ rae.temporary_count = 1
    wt_image store_clerk_working_13
    rae.c "I was hoping you were going to say that!"
    "Rae practically dances as she leads you into the changing room."
    wt_image store_clerk_sex_29
    "There's no warm-up required.  She's ready for you."
    $ title = "How do you want to do this?"
    menu:
        "Missionary style":
            wt_image store_clerk_hypnotized_sex_2
            "She moans as you run the head of your cock along her wet labia ..."
            rae.c "oohhh"
            wt_image store_clerk_sex_3
            "... and then moans even louder in orgasm as you fuck her."
            wt_image store_clerk_sex_23
            rae.c "ooohhhhh ... yeesss!"
            wt_image store_clerk_sex_24
            "You save your moans ..."
            wt_image store_clerk_sex_22
            "... until you're shooting your cum on her."
            wt_image store_clerk_sex_8
            player.c "[player.orgasm_text]"
        "Doggy style":
            wt_image store_clerk_hypnotized_sex_4
            "She moans as the head of your cock penetrates her ..."
            rae.c "oohhh"
            wt_image store_clerk_sex_25
            "... and soon you're both moaning as you cum in quick succession, with Rae looking back over her shoulder so she can watch as you fuck her."
            wt_image store_clerk_sex_2
            rae.c "ooohhhhh ... yeesss!"
            wt_image store_clerk_sex_26
            player.c "[player.orgasm_text]"
        "Have her ride you":
            wt_image store_clerk_sex_9
            "Rae happily climbs up on top of you ..."
            wt_image store_clerk_sex_10
            "... and starts riding up and down on your hard dick."
            wt_image store_clerk_sex_17
            rae.c "oohhh"
            wt_image store_clerk_sex_18
            $ title = "Is this right?"
            menu:
                "This is great":
                    wt_image store_clerk_sex_11
                    "She was going to cum quickly anyway, but a little tickle at her backdoor ..."
                    rae.c "ooohhhhh"
                    wt_image store_clerk_sex_12
                    "... followed by a slap on her ass sends her crashing over the edge, and you with her ... *smack*"
                    rae.c "ooohhhhh ... yeesss!"
                    wt_image store_clerk_sex_19
                    player.c "[player.orgasm_text]"
                "Tell her to turn around":
                    wt_image store_clerk_sex_13
                    rae.c "Can't I face you?"
                    wt_image store_clerk_sex_21
                    player.c "Not today.  Today I want to watch your ass bounce as you ride me."
                    wt_image store_clerk_sex_14
                    "She gets over her disappointment and resumes riding you ..."
                    wt_image store_clerk_sex_20
                    "... her tight pussy sliding up and down your shaft soon milking an orgasm out of you."
                    wt_image store_clerk_sex_15
                    player.c "[player.orgasm_text]"
                    wt_image store_clerk_sex_16
                    "The realization that she's brought you pleasure seems to be enough to trigger her orgasm."
                    rae.c "ooohhhhh ... yeesss!"
        "Let her tackle you":
            wt_image store_clerk_sex_1
            "You don't have to do anything but take your clothes off. As soon as you're naked, she literally throws herself at you."
            wt_image store_clerk_sex_28
            "There's no doubt that she cums today, riding herself to an orgasm on your cock, and bringing you along with her."
            wt_image store_clerk_sex_1
            rae.c "ooohhhhh ... yeesss!"
            wt_image store_clerk_sex_27
            player.c "[player.orgasm_text]"
        "Eat her out":
            wt_image store_clerk_sex_4
            "Rae moans as you caress her sex ..."
            wt_image store_clerk_sex_5
            "... and starts trembling as your fingers probe her wet snatch."
            wt_image store_clerk_sex_6
            "It takes only a few licks of your tongue to have her writhing in orgasmic bliss."
            wt_image store_clerk_sex_30
            rae.c "ooohhhhh ... yeesss!"
            wt_image store_clerk_sex_7
            rae.c "You don't have to stop there."
            player.c "You want me to keep licking you?"
            rae.c "I want you to fuck me."
            $ title = "Fuck her?"
            menu:
                "Yes":
                    wt_image store_clerk_sex_1
                    "As soon as you have your clothes off, she literally throws herself at you.  You're used to women wanting you, but rarely have you seen a woman look so thoroughly happy to have you enter her."
                    wt_image store_clerk_sex_28
                    "She seems to be in bliss from the mere experience of having you inside her, but she makes sure you enjoy things on a more physical level."
                    wt_image store_clerk_sex_27
                    player.c "[player.orgasm_text]"
                "Not today":
                    player.c "Not today, Rae."
                    rae.c "But ... why not?"
                    player.c "Perhaps another time."
                    "She doesn't argue, but she's disappointed.  You putting your cock in her makes her feel special."
                    $ rae.temporary_count = 0
                    change player energy by -energy_short notify
    $ rae.orgasm_count += 1
    if rae.temporary_count == 1:
        $ rae.temporary_count = 0
        $ rae.sex_count += 1
        orgasm notify
        wt_image store_clerk_working_14
        if rae.has_any_tag('girlfriend', 'hypno_girlfriend'):
            rae.c "I'm always happy when my boyfriend drops by to see me."
        else:
            rae.c "I'm always happy when you drop by to see me."
            "Especially when you want to have sex with her, and you're pretty sure that's not just because she came."
    return

## Girlfriend Actions
label rae_start_date_check:
    $ rae.date_outfit += 1
    # note maintenance week change precede the dates to better adjust the week for dates she doesn't enjoy
    $ rae.maintain_week_gf = week + 4
    # scroll from 1 through 6
    if rae.date_outfit > 6:
        $ rae.date_outfit = 1
    # check for other relationships
    if (bedroom.number_of_people < 1 and rae.has_tag('girlfriend') and not terri.has_tag('assistant')) or rae.has_tag('hypno_girlfriend') or not rae.has_tag('exclusive_girlfriend'):
        add tags 'on_date' to rae
        summon rae to living_room no_follows
        call forced_movement(living_room) from _call_forced_movement_144
        if rae.date_outfit == 1:
            $ rae.change_image('store_clerk_date_1_10')
        elif rae.date_outfit == 2:
            $ rae.change_image('store_clerk_date_2_9')
        elif rae.date_outfit == 3:
            $ rae.change_image('store_clerk_date_5_1')
        elif rae.date_outfit == 4:
            $ rae.change_image('store_clerk_date_6_1')
        elif rae.date_outfit == 5:
            $ rae.change_image('store_clerk_date_4_7')
        else:
            $ rae.change_image('store_clerk_date_3_8')
        wt_image rae.image
        "Rae arrives for your date. She's looking forward to it."
    # if any, lose Rae
    else:
        wt_image store_clerk_phone_angry
        rae.c "I can't believe you have the nerve to ask me on a date!"
        rae.c "I know about the other woman who's living in your house.  I'm not stupid!"
        if terri.has_tag('assistant'):
            player.c "Terri's my assistant, and besides, she's really not ..."
            rae.c "Your 'assistant'?  I can image what she 'assists' you with!  I can't believe you would two time me!!"
        else:
            rae.c "I can't believe you would two time me!!"
        if rae.has_tag('love_potion_used'):
            rae.c "We were meant to be together. You were the one! I know it, in every fiber of my body. I'm supposed to be with you!!"
            rae.c "I don't know how I can live like this. Wanting you. Wanting a cheater. Knowing that I wasn't enough for you ..."
            "Rae hangs up, half crying, half screaming. You won't be able to patch this up. You just hope she doesn't do anything stupid in her love potion enhanced grief."
        else:
            "Rae hangs up, half crying, half screaming.  You won't be able to patch this up."
        call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status
    return

label rae_date:
    $ rae.training_session()
    if rae.date_outfit == 1:
        wt_image store_clerk_date_1_10
        if rae.first_date_complete:
            "Rae smiles sweetly at you as she sits down for the home cooked dinner you've arranged."
        else:
            "For for your first date as boyfriend - girlfriend, you arrange a nice home cooked meal. Rae's adorably shy but radiant as she sits down at the table."
            $ rae.first_date_complete = True
        wt_image store_clerk_date_1_1
        "The dinner is nice, but Rae looks even nicer. You have a hard time keeping your hands off of her."
        wt_image store_clerk_date_1_2
        "In fact, you can't keep your hands off of her ... and she doesn't want you to."
        $ title = "What do you want?"
        menu:
            "Blow job":
                wt_image store_clerk_date_1_13
                "You undress Rae ..."
                wt_image store_clerk_date_1_14
                "... and guide her to her knees ..."
                wt_image store_clerk_date_1_3
                "... where she happily sucks your cock until you're ready to cum."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image store_clerk_date_1_14
                        player.c "[player.orgasm_text]"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_swallow_count += 1
                        else:
                            $ rae.swallow_count += 1
                        wt_image store_clerk_date_1_19
                        rae.c "I hope you invite me out again soon,"
                    "On her face":
                        wt_image store_clerk_date_1_4
                        player.c "[player.orgasm_text]"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_facial_count += 1
                            wt_image store_clerk_date_1_16
                            "Rae seems dazed by the experience. Facials weren't something she's offered to past boyfriends."
                            "The experience of having you feed her and then shower her with your jizz leaves her a bit disoriented."
                        else:
                            $ rae.facial_count += 1
                            wt_image store_clerk_date_1_17
                            rae.c "Oh!"
                            player.c "It's okay if I continue to cum on you, isn't it?"
                            wt_image store_clerk_date_1_7
                            rae.c "Yes.  If you like this, I'm glad to do it for you."
                            wt_image store_clerk_date_1_18
                            rae.c "I hope you invite me out again soon."
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_blowjob_count += 1
                else:
                    $ rae.blowjob_count += 1
                orgasm notify
            "Missionary":
                wt_image store_clerk_date_1_13
                "You undress Rae ..."
                wt_image store_clerk_date_1_20
                "... and lay her on her back."
                wt_image store_clerk_date_1_21
                "She gasps as you enter her."
                rae.c "Oh!"
                wt_image store_clerk_date_1_11
                "Fucking her feels heavenly, and she seems to feel the same way."
                rae.c "oohhhh"
                wt_image store_clerk_date_1_5
                rae.c "ooohhhhh ... yeesss!"
                player.c "[player.orgasm_text]"
                wt_image store_clerk_date_1_19
                rae.c "I hope you invite me out again soon."
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_orgasm_count += 1
                    $ rae.hypno_sex_count += 1
                else:
                    $ rae.orgasm_count += 1
                    $ rae.sex_count += 1
                orgasm notify
            "Doggy style":
                wt_image store_clerk_date_1_13
                "You undress Rae ..."
                wt_image store_clerk_date_1_22
                "... and position her on the sofa, facing away from you."
                wt_image store_clerk_date_1_23
                "She gasps as you enter her."
                rae.c "Oh!"
                wt_image store_clerk_date_1_24
                "She doesn't get off today.  She seems more interested in twisting around to watch and make sure you're enjoying yourself.  Which you are."
                player.c "[player.orgasm_text]"
                wt_image store_clerk_date_1_22
                rae.c "I hope you invite me out again soon."
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_sex_count += 1
                else:
                    $ rae.sex_count += 1
                orgasm notify
            "Cowgirl":
                wt_image store_clerk_date_1_13
                "You undress Rae ..."
                wt_image store_clerk_date_1_12
                "... and direct her on top of you."
                rae.c "Oh!"
                wt_image store_clerk_date_1_25
                "She rides happily up and down on you ..."
                rae.c "oohhhh"
                wt_image store_clerk_date_1_6
                "... until she reaches her climax ..."
                rae.c "ooohhhhh ... yeesss!"
                wt_image store_clerk_date_1_8
                ".. and you reach yours."
                player.c "[player.orgasm_text]"
                wt_image store_clerk_date_1_9
                rae.c "I hope you invite me out again soon."
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_orgasm_count += 1
                    $ rae.hypno_sex_count += 1
                else:
                    $ rae.orgasm_count += 1
                    $ rae.sex_count += 1
                orgasm notify
            "Just look at her" if rae.first_date_complete:
                wt_image store_clerk_date_1_13
                "You undress Rae ..."
                wt_image store_clerk_date_1_19
                "... and she lets you spend the rest of the evening admiring her beauty."
                rae.c "I hope you invite me out again soon."
        $ rae.first_date_complete = True
    elif rae.date_outfit == 2:
        call forced_movement(outdoors) from _call_forced_movement_8
        summon rae
        wt_image store_clerk_restaurant_2
        "You take Rae out for lunch."
        wt_image store_clerk_date_2_1
        "In the parking lot after the meal, you let her know how nice she looks."
        rae.c "Thaaanks!  That's so sweet of you to say."
        player.c  "It's true.  You look so nice I don't think I can wait till.  I need to have you right here."
        wt_image store_clerk_date_2_2
        "She laughs."
        rae.c "I'm glad I have that effect on you, but I need to get home.  Come on, let's go."
        $ title = "What do you tell her?"
        menu:
            "Flash me":
                wt_image store_clerk_date_2_10
                player.c "At least show me your tits."
                rae.c "You're not serious?"
                player.c "I am"
                wt_image store_clerk_date_2_11
                "She takes a look around to make sure no one can see her ..."
                wt_image store_clerk_date_2_3
                "... then pulls down her top."
                rae.c "I can't believe I'm doing this.  You are so bad!"
                wt_image store_clerk_date_2_12
                rae.c "C'mon, let's go before someone sees me like this."
                player.c "Okay.  I'll give you a lift back to your place, but you need to ride in the car like that."
                wt_image store_clerk_date_2_13
                rae.c "You're joking, right?  Oh my gawd, you're not!  You are so bad!!"
                change player energy by -energy_very_short notify
            "Blow me":
                wt_image store_clerk_date_2_10
                player.c "I'm not joking, Rae.  I'm serious.  Come on, take me in your mouth.  Right here."
                wt_image store_clerk_date_2_11
                "She takes a look around to make sure no one can see her ..."
                rae.c "I can't believe I'm doing this."
                wt_image store_clerk_date_2_4
                "... then leans over and takes you into her mouth."
                wt_image store_clerk_date_2_5
                "As you stiffen, she kneels down to have easier access to your full shaft"
                wt_image store_clerk_date_2_6
                "Hiding between the cars, she pleasures your dick as quickly as she can."
                $ title = "Let her swallow your load?"
                menu:
                    "Yes, swallowing is fine":
                        wt_image store_clerk_date_2_14
                        player.c "[player.orgasm_text]"
                        $ rae.swallow_count += 1
                        wt_image store_clerk_date_2_15
                        rae.c "You are so bad!  C'mon, let's go before someone sees us."
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_swallow_count += 1
                        else:
                            $ rae.swallow_count += 1
                    "No, spray her face":
                        wt_image store_clerk_date_2_16
                        "Rae resists as you start to take your cock out of her mouth."
                        rae.c "What are you doing?"
                        player.c "That thing you like to do for me."
                        wt_image store_clerk_date_2_17
                        rae.c "Not here!"
                        player.c "Yes, here."
                        wt_image store_clerk_date_2_18
                        player.c "[player.orgasm_text]"
                        rae.c "C'mon, let's go before someone sees us!"
                        player.c "Why the rush?  You're not embarrassed to be wearing my cum, are you?"
                        rae.c "You are so bad!!!  Let's go already!"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_facial_count += 1
                        else:
                            $ rae.facial_count += 1
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_blowjob_count += 1
                else:
                    $ rae.blowjob_count += 1
                orgasm notify
            "I need to fuck you":
                wt_image store_clerk_date_2_10
                player.c "I'm not joking, Rae. I'm serious. Turn around, I need to have you right here."
                wt_image store_clerk_date_2_11
                "She takes a look to make sure no one can see the two of you ..."
                rae.c "I can't believe I'm doing this."
                wt_image store_clerk_date_2_19
                "... then turns around, letting you lift her skirt."
                rae.c "You are so bad!"
                wt_image store_clerk_date_2_20
                player.c "I'm not the only one being bad.  Look who's not wearing panties."
                rae.c "That was a surprise for when we got back to your place."
                wt_image store_clerk_date_2_8
                player.c "Surprise.  That just makes me want to fuck you here in the parking lot even more."
                rae.c "oohhh"
                wt_image store_clerk_date_2_7
                "She's too worried about being caught to relax enough to cum herself, but she holds you as best she can given the awkward angle as you empty your load inside her."
                player.c "[player.orgasm_text]"
                wt_image store_clerk_date_2_21
                rae.c "You are so bad!"
                player.c "Says the siren tempting me with her panty-less bottom."
                rae.c "You wanted me even before you knew I wasn't wearing panties."
                player.c "I wanted you even more once I knew how bad you were."
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_sex_count += 1
                else:
                    $ rae.sex_count += 1
                orgasm notify
            "Okay, we can go":
                wt_image store_clerk_date_2_1
                rae.c "Thaaanks!  I'll fuck you some other time, I promise."
        call forced_movement(living_room) from _call_forced_movement_10
    elif rae.date_outfit == 3:
        call forced_movement(outdoors) from _call_forced_movement_17
        summon rae
        wt_image store_clerk_cinema_1
        "You take Rae out for a movie."
        wt_image store_clerk_date_5_2
        "The film is boring, but your date looks nice."
        $ title = "What do you do?"
        menu:
            "Start something":
                wt_image store_clerk_hypno_date_5
                player.c "Rae, suck me off while we're watching the film."
                rae.c "What!  Here??  Someone may see me."
                player.c "No they won't.  It's dark."
                wt_image store_clerk_date_5_3
                "It makes it more difficult for her to follow the plot, but you enjoy the movie much more this way."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image store_clerk_hypno_date_8
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_5_2
                        rae.c "Can we go back to watching the movie, now?"
                        player.c "Sure.  It's almost over."
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_swallow_count += 1
                        else:
                            $ rae.swallow_count += 1
                    "On her face":
                        wt_image store_clerk_hypno_date_9
                        player.c "[player.orgasm_text]"
                        rae.c "Oh my gawd!  What am I supposed to clean myself up with?"
                        player.c  "There'll be tissues in the washrooms."
                        rae.c "I have to walk through the theatre to get to them!  What will people think?"
                        player.c "That you really liked the movie?  Or at least, that I did."
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_facial_count += 1
                        else:
                            $ rae.facial_count += 1
                if rae.has_tag('hypno_girlfriend'):
                    $ rae.hypno_blowjob_count += 1
                else:
                    $ rae.blowjob_count += 1
                orgasm notify
            "Wait until you're back in the car":
                wt_image store_clerk_date_5_4
                rae.c "Thanks for the date! I had a really great time, even if the movie wasn't that great."
                player.c "Maybe you'd like to say thank you for the date?"
                wt_image store_clerk_date_5_5
                rae.c "Maaaybe ... what did you have in mind?"
                $ title = "What do you have in mind?"
                menu:
                    "Blow job":
                        wt_image store_clerk_date_5_6
                        rae.c "We'll have to be quick, or someone may see us."
                        player.c "I guess that depends on how good a job you do."
                        wt_image store_clerk_date_5_7
                        "She does a pretty good job, first getting your dick hard ..."
                        wt_image store_clerk_date_5_8
                        "... and then sucking on it ..."
                        wt_image store_clerk_date_5_9
                        "... until you're ready to cum."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her mouth":
                                wt_image store_clerk_date_5_10
                                player.c "[player.orgasm_text]"
                                wt_image store_clerk_date_5_11
                                if rae.has_tag('hypno_girlfriend'):
                                    $ rae.hypno_swallow_count += 1
                                else:
                                    $ rae.swallow_count += 1
                            "On her face":
                                wt_image store_clerk_hypno_date_15
                                player.c "Face, Rae."
                                "She nods and prepares herself."
                                wt_image store_clerk_date_5_12
                                player.c "[player.orgasm_text]"
                                wt_image store_clerk_date_5_13
                                if rae.has_tag('hypno_girlfriend'):
                                    $ rae.hypno_facial_count += 1
                                else:
                                    $ rae.facial_count += 1
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_blowjob_count += 1
                        else:
                            $ rae.blowjob_count += 1
                    "Sex":
                        wt_image store_clerk_date_5_14
                        player.c "Get your clothes off.  I want you to fuck me."
                        rae.c "Here?"
                        player.c "Why not?"
                        wt_image store_clerk_date_5_15
                        rae.c "Someone will see us."
                        player.c "Then you'd better be quick."
                        wt_image store_clerk_date_5_16
                        "She is quick, climbing up on your shaft despite the cramped quarters ..."
                        wt_image store_clerk_date_5_17
                        "... and riding you to a quick but intense ..."
                        wt_image store_clerk_date_5_18
                        "... and thoroughly pleasurable orgasm."
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_5_19
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_sex_count += 1
                        else:
                            $ rae.sex_count += 1
                rae.c "Hopefully that was a good enough thank you that you'll ask me out again soon!"
                orgasm notify
            "Just watch the movie then take her home":
                wt_image store_clerk_date_5_4
                rae.c "Thanks for the date!  I had a really great time, even if the movie wasn't that great."
                change player energy by -energy_very_short notify
        call forced_movement(living_room) from _call_forced_movement_24
    elif rae.date_outfit == 4:
        wt_image store_clerk_date_6_1
        rae.c "Instead of going out today, could we maybe stay in instead?"
        player.c "What did you have in mind?"
        if rae.has_item(lingerie):
            rae.c "I thought maybe you'd like to see me in that lingerie you bought me again?"
            $ title = "Do you want to watch her in her lingerie?"
            menu:
                "Yes":
                    $ rae.temporary_count = 0
                    wt_image living_room.image
                    "Rae goes and changes ..."
                    wt_image store_clerk_lingerie_1_1
                    "... reappearing a few minutes later, wearing less and yet somehow seeming better dressed."
                    wt_image store_clerk_lingerie_1_3
                    "She immediately starts to dance ..."
                    wt_image store_clerk_lingerie_1_4
                    "... turning and swaying ..."
                    wt_image store_clerk_lingerie_1_6
                    "... as she strips."
                    wt_image store_clerk_lingerie_1_8
                    "The bra goes first ..."
                    wt_image store_clerk_lingerie_1_9
                    "... and then the panties ..."
                    wt_image store_clerk_lingerie_1_11
                    "... until she's naked, her labia swollen with excitement at exposing herself to you."
                    wt_image store_clerk_lingerie_1_12
                    rae.c "I hope you still like looking at my body?"
                    $ title = "What do you tell her?"
                    menu:
                        "It was a lovely dance":
                            player.c "I love looking at your body, Rae.  Thanks for the dance."
                            wt_image store_clerk_lingerie_1_2
                            rae.c "Thaaanks!  I'm glad you liked it.  This lingerie really is nice."
                            "She dresses and heads home, pleased with herself for having pleased you."
                        "I'd like to see you touch yourself":
                            if rae.has_tag('masturbated'):
                                player.c "Play with yourself, Rae."
                                rae.c "Again?"
                                player.c "Yes.  I love looking at your body, especially when you're pleasuring yourself."
                                wt_image store_clerk_lingerie_1_13
                                rae.c "Okay"
                                "She wets her fingers ..."
                            else:
                                add tags 'masturbated' to rae
                                player.c "I love looking at your body.  I'd like to watch you play with your body."
                                rae.c "What?"
                                player.c "I want to see you touch yourself.  Play with yourself while I watch, Rae."
                                rae.c "I don't know if I can ..."
                                player.c "Sure you can.  You're excited from dancing for me.  Masturbating for me will be even more exciting."
                                wt_image store_clerk_lingerie_1_13
                                "Despite her misgivings, she wets her fingers ..."
                            wt_image store_clerk_lingerie_1_14
                            "... and starts rubbing herself."
                            wt_image store_clerk_lingerie_1_15
                            "Her excitement builds quickly ..."
                            rae.c "mmmmmm"
                            wt_image store_clerk_lingerie_1_16
                            "... and as she pushes a finger into herself ..."
                            rae.c "ooohhhhh"
                            wt_image store_clerk_lingerie_1_17
                            "... she frigs herself over the edge."
                            rae.c "ooohhhhh ... yeesss!"
                            wt_image store_clerk_lingerie_1_18
                            rae.c "It's a little scary sometimes how just having you watch me can turn me on like that.  But I'm glad it does."
                            wt_image store_clerk_lingerie_1_2
                            player.c "I enjoyed it, too."
                            rae.c "Thank goodness!  I'd really feel like an idiot if you didn't."
                            if not rae.has_item(dildo):
                                "If she liked using her fingers while you watched, she might really like using a dildo.  You should get her one."
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_masturbation_count += 1
                                $ rae.hypno_orgasm_count += 1
                            else:
                                $ rae.masturbation_count += 1
                                $ rae.orgasm_count += 1
                            "She dresses and heads home, pleased with herself for having pleased you."
                        "Use your vibrator" if rae.has_item(dildo) and rae.has_tag('masturbated'):
                            player.c "Use your vibrator on yourself, Rae."
                            rae.c "With you watching?"
                            player.c "Of course."
                            wt_image store_clerk_lingerie_1_19
                            "She places the vibrator directly against her clit, proof that the dance did arouse her.\n"
                            "*bzzzzz*"
                            rae.c "ooohhhh"
                            wt_image store_clerk_lingerie_1_20
                            "Then she slides it inside her ... *bzzzzz*"
                            rae.c "oooohhhhh"
                            wt_image store_clerk_lingerie_1_21
                            "... using the vibrator ... *bzzzzz*"
                            rae.c "ooohhhh ... oooohhhhh"
                            wt_image store_clerk_lingerie_1_22
                            "... she fucks herself over the edge. *bzzzzz*"
                            rae.c "ooohhhhh ... yeesss!"
                            wt_image store_clerk_lingerie_1_23
                            rae.c "I must look like a tramp doing that."
                            $ title = "What do you say?"
                            menu:
                                "In the best possible way":
                                    wt_image store_clerk_lingerie_1_2
                                    rae.c "I didn't know that was possible, but I'm glad you think so."
                                    "She dresses and heads home, pleased with herself for having pleased you."
                                "My tramp, and a sexy one":
                                    wt_image store_clerk_lingerie_1_12
                                    rae.c "I hope you don't really think of me as a tramp, even a sexy one."
                                    "She dresses and heads home, wondering what you really thought of the spectacle she made of herself."
                                "The word you're looking for is 'slut'":
                                    wt_image store_clerk_lingerie_1_18
                                    rae.c "That's a terrible thing to say!  I'm not a slut.  I was only trying to do something special for you."
                                    $ rae.strike_count += 1
                                    sys "Rae's less happy with your relationship."
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_masturbation_count += 1
                                $ rae.hypno_orgasm_count += 1
                            else:
                                $ rae.masturbation_count += 1
                                $ rae.orgasm_count += 1
                    change player energy by -energy_short notify
                "No, I'd rather just have you naked":
                    $ rae.temporary_count = 1
                    wt_image store_clerk_date_6_2
                    player.c "How about you just get naked?"
                    wt_image store_clerk_date_6_3
                    rae.c "Okay, and then what?"
        else:
            $ rae.temporary_count = 1
            wt_image store_clerk_date_6_2
            rae.c "I'm not sure ..."
            wt_image store_clerk_date_6_3
            rae.c "... but I bet you can think of something."
        if rae.temporary_count == 1:
            $ rae.temporary_count = 0
            $ title = "What do you want?"
            menu:
                "Tit job":
                    player.c "I want to fuck your tits."
                    wt_image store_clerk_date_6_9
                    if not rae.has_tag('titfucked'):
                        add tags 'titfucked' to rae
                        rae.c "My tits?  I'm more than just my tits, you know."
                        player.c "Of course I know that."
                        rae.c "A lot of guys don't. They see big tits on a girl who didn't finish high school and think ' 'bimbo', I bet she's an easy lay.'"
                        player.c "I'm not a lot of guys. I'm your boyfriend. I just want to put my dick between your beautiful breasts."
                        rae.c "I've never let a guy do that. It seems like you want to fuck my tits, not me."
                        player.c "I want to fuck the whole package. Can't you do this for me?"
                        rae.c "I suppose if you really want to, we can try it."
                        wt_image store_clerk_date_6_10
                        "She lies down and lets you take her breast-virginity."
                        wt_image store_clerk_date_6_11
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_6_12
                        rae.c "Is it special to you that I let you cum on me?"
                        $ title = "What do you tell her?"
                        menu:
                            "You're special to me, Rae":
                                rae.c "You're special to me, too."
                            "Who else would I cum on?":
                                rae.c "No one, I hope.  I'm not the type to share.  I'm sure you know that."
                                $ rae.maintain_week_gf -= 1
                            "There's no place I'd rather shoot my load":
                                rae.c "I'm not sure how to take that."
                                $ rae.maintain_week_gf -= 2
                            "You make a great cum dump":
                                add tags 'called_her_cumdump' to rae
                                rae.c "Don't say things like that.  It makes me sound cheap."
                                $ rae.strike_count += 2
                                $ rae.maintain_week_gf -= 3
                                sys "Rae's a lot less happy with your relationship."
                    else:
                        rae.c "Again?"
                        player.c "They're part of your body, Rae.  You like using your body to please me, don't you?"
                        if rae.has_tag('called_her_cumdump'):
                            rae.c "I don't like you treating my body like a cum dump.  That's something special I do for you.  You cheapened it when you called me that."
                            $ title = "What do you say to her?"
                            menu:
                                "I'm sorry, I shouldn't have called you that":
                                    rem tags 'called_her_cumdump' from rae
                                    rae.c "I'm glad to hear you say that.  It was really hurtful."
                                "I like that you do special things for me":
                                    add tags 'no_strike_this_time' to rae
                                    rae.c "I hope you do."
                                "Don't be a silly cum dump":
                                    player.c "That's enough nonsense.  You say like to do special things for me.  Lie back and show me by being my cum dump."
                        else:
                            rae.c "Yes, but men never seem to see me when they're ogling my tits."
                            player.c "I'll be looking right at you when I fuck your tits, Rae."
                        wt_image store_clerk_date_6_10
                        "Despite her concerns, she presses her mounds together, creating a soft valley for your cock to slide back and forth in."
                        wt_image store_clerk_date_6_11
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_6_12
                        if rae.has_tag('called_her_cumdump'):
                            if rae.has_tag('no_strike_this_time'):
                                rem tags 'no_strike_this_time' from rae
                                rae.c "I can tell you enjoyed that.  I hope it was because you appreciated what I letting you do, and not because you were thinking of me as a stupid cum dump."
                            else:
                                $ rae.strike_count += 1
                                sys "Rae's less happy with your relationship."
                        else:
                            rae.c "You're the first boyfriend I've let do that with me. I hope you understand how special you are to me."
                        $ rae.maintain_week_gf -= 1
                    if rae.has_tag('hypno_girlfriend'):
                        $ rae.hypno_titfuck_count += 1
                    else:
                        $ rae.titfuck_count += 1
                    orgasm notify
                "Sex":
                    player.c "How about we fuck?"
                    rae.c "It's so nice dating a smart guy with great ideas!"
                    wt_image store_clerk_date_6_4
                    "Rae climbs onto your dick ..."
                    wt_image store_clerk_date_6_5
                    "... and rides you ..."
                    rae.c "oohhh"
                    wt_image store_clerk_date_6_6
                    "... until first she cums ..."
                    rae.c "ooohhhhh ... yeesss!"
                    wt_image store_clerk_date_6_7
                    "... and then you do."
                    player.c "[player.orgasm_text]"
                    $ rae.sex_count += 1
                    $ rae.orgasm_count += 1
                    wt_image store_clerk_date_6_8
                    rae.c "You always come up with the best ideas for our dates!"
                    if rae.has_tag('hypno_girlfriend'):
                        $ rae.hypno_sex_count += 1
                        $ rae.hypno_orgasm_count += 1
                    else:
                        $ rae.sex_count += 1
                        $ rae.orgasm_count += 1
                    orgasm notify
                "Nothing today":
                    player.c "Not today I can't. I'm happy just looking at you naked."
                    wt_image store_clerk_date_6_9
                    rae.c "That's boring."
                    $ rae.maintain_week_gf -= 2
    elif rae.date_outfit == 5:
        summon rae
        wt_image store_clerk_date_4_8
        rae.c "It's such a beautiful day!  Thanks for inviting me out for a walk."
        call forced_movement(outdoors) from _call_forced_movement_26
        summon rae
        wt_image store_clerk_date_4_9
        "The two of you take a stroll through the neighborhood ..."
        wt_image store_clerk_park_1
        "... and around the park.  There are a lot of other people outside enjoying the great weather."
        wt_image store_clerk_date_4_10
        rae.c "That was fun.  Thank you!"
        $ title = "Invite her in?"
        menu:
            "Yes, continue the date":
                player.c "Would you like to come in?"
                call forced_movement(living_room) from _call_forced_movement_29
                summon rae
                wt_image store_clerk_date_4_7
                rae.c "Sure.  I'll just get changed out of my walking clothes."
                wt_image store_clerk_date_4_1
                rae.c "I hope you don't mind me making myself comfortable?"
                $ title = "What did you have in mind?"
                menu:
                    "Blow job":
                        wt_image store_clerk_date_4_11
                        "Rae licks your cock hard ..."
                        wt_image store_clerk_date_4_12
                        "... then blows you until you're ready to cum."
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her mouth":
                                wt_image store_clerk_date_4_13
                                player.c "[player.orgasm_text]"
                                wt_image store_clerk_date_4_11
                                rae.c "You taste good today.  I wonder if it was something you ate?"
                                if rae.has_tag('hypno_girlfriend'):
                                    $ rae.hypno_swallow_count += 1
                                else:
                                    $ rae.swallow_count += 1
                            "On her face":
                                wt_image store_clerk_date_4_2
                                player.c "[player.orgasm_text]"
                                wt_image store_clerk_date_4_3
                                rae.c "You like me like this, don't you?"
                                if rae.has_tag('hypno_girlfriend'):
                                    $ rae.hypno_facial_count += 1
                                else:
                                    $ rae.facial_count += 1
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_blowjob_count += 1
                        else:
                            $ rae.blowjob_count += 1
                        orgasm notify
                    "Missionary":
                        wt_image store_clerk_date_4_4
                        "You lie Rae back on the bed. She bites her lip as you enter her."
                        rae.c "oohhh"
                        wt_image store_clerk_date_4_14
                        "She rubs her clit as you fuck her and her excitement builds quickly ..."
                        rae.c "oooohhhhh"
                        wt_image store_clerk_date_4_5
                        ".. so to slow her down you roll her onto her side."
                        rae.c "Oh!"
                        wt_image store_clerk_date_4_15
                        "She still cums before you do, but not by much."
                        rae.c "ooohhhhh ... yeesss!"
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_4_14
                        rae.c "Oh my gawd ... I love what you do with my body!"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_sex_count += 1
                            $ rae.hypno_orgasm_count += 1
                        else:
                            $ rae.sex_count += 1
                            $ rae.orgasm_count += 1
                        orgasm notify
                    "Cowgirl":
                        wt_image store_clerk_date_4_16
                        "Rae climbs on top of you ..."
                        wt_image store_clerk_date_4_17
                        "... and starts riding up and down on your hard shaft."
                        wt_image store_clerk_date_4_6
                        rae.c "oohhh"
                        wt_image store_clerk_date_4_18
                        rae.c "ooohhhh"
                        wt_image store_clerk_date_4_19
                        rae.c "ooohhhhh ... yeesss!"
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_date_4_20
                        rae.c "Oh my gawd ... I love what you do with my body!"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_sex_count += 1
                            $ rae.hypno_orgasm_count += 1
                        else:
                            $ rae.sex_count += 1
                            $ rae.orgasm_count += 1
                        orgasm notify
                    "Just pleasure her":
                        wt_image store_clerk_date_4_21
                        "You undress Rae and turn her around ..."
                        wt_image store_clerk_date_4_22
                        "... then pleasure her with your mouth ..."
                        rae.c "oohhh"
                        wt_image store_clerk_date_4_23
                        "... licking her wet and dripping pussy ..."
                        rae.c "ooohhhh"
                        wt_image store_clerk_date_4_24
                        "... until it floods your mouth with her cum juice."
                        rae.c "ooohhhhh ... yeesss!"
                        wt_image store_clerk_date_4_25
                        rae.c "Oh my gawd ... I love what you do with my body!"
                        if rae.has_tag('hypno_girlfriend'):
                            $ rae.hypno_orgasm_count += 1
                        else:
                            $ rae.orgasm_count += 1
                        change player energy by -energy_short notify
                        $ rae.maintain_week_gf += 1
            "No, go on with your day":
                "Rae had fun and so did you.  Time to get on with the rest of your day."
                call forced_movement(living_room) from _call_forced_movement_31
                change player energy by -energy_very_short notify
    elif rae.date_outfit == 6:
        $ rae.temporary_count = 0
        call forced_movement(bedroom) from _call_forced_movement_40
        summon rae
        wt_image store_clerk_date_3_8
        rae.c "Sooo, where are we going for our date today?"
        player.c "I thought we'd stay in today."
        rae.c "Oh come on!  It's a beautiful day.  Let's go do something."
        $ title = "What do you say?"
        menu:
            "Okay, how about a bite to eat":
                $ rae.maintain_week_gf += 1
                player.c "Okay.  Let's go grab some food."
                wt_image store_clerk_date_3_7
                rae.c "Great!"
                call forced_movement(outdoors) from _call_forced_movement_41
                summon rae
                wt_image store_clerk_restaurant_2
                "The two of you grab a bite to eat ..."
                call forced_movement(bedroom) from _call_forced_movement_42
                summon rae
                wt_image store_clerk_date_3_1
                "... then you head back to your place."
                rae.c "Thanks for taking me out when you wanted to stay in.  You are so sweet!  I really enjoyed our date."
                $ title = "What do you say?"
                menu:
                    "Date's not over":
                        $ rae.temporary_count = 1
                        player.c "Do you need to rush home?"
                        rae.c "Nooo ... what did you have in mind?"
                    "I did, too":
                        player.c "So did I, Rae."
                        rae.c "I hope you invite me out again soon!"
                        change player energy by -energy_very_short notify
            "If we stay here, I have more time to play with your body":
                player.c "I won't have as much time I'd like to enjoy your body if we go out first."
                $ rae.temporary_count = 1
                wt_image store_clerk_date_3_1
                rae.c "Awwww ... I guess I need to be flattered by that."
            "I said we're staying in" if rae.has_tag('trigger_implanted') or not rae.date_spank:
                player.c "I make the decisions, Rae, and we're staying in."
                wt_image store_clerk_date_3_9
                rae.c "Yeah, right.  Let's at least go for a walk or something."
                wt_image store_clerk_date_3_10
                player.c "No, we're staying here."
                rae.c "Or what?  You don't get to decide what we do all the time, you know.  I have a brain, too!"
                $ title = "What now?"
                menu:
                    "Trigger her" if rae.has_tag('trigger_implanted'):
                        player.c "[rae.trigger_phrase], Rae.  You do what I tell you to do.  Sit down."
                        wt_image store_clerk_date_3_1
                        rae.c "I do what you tell me to!"
                        $ title = "What do you do with her?"
                        menu:
                            "Have sex with her":
                                $ rae.temporary_count = 1
                            "Turn her into art":
                                player.c "Remove your clothes."
                                wt_image store_clerk_date_3_11
                                rae.c "I do what you tell me to!"
                                wt_image store_clerk_date_3_12
                                player.c "For our date today, you're going to be artwork, and you're going to enjoy it."
                                rae.c "I do what you tell me to!"
                                $ title = "How do you want to position her?"
                                menu:
                                    "Sitting up":
                                        wt_image store_clerk_date_3_14
                                        player.c "Stay like that until I decide you can go home."
                                        rae.c "I do what you tell me to!"
                                        wt_image living_room.image
                                        "You spend the afternoon getting a few things done before you return to Rae."
                                        wt_image store_clerk_date_3_14
                                    "Lying down":
                                        wt_image store_clerk_date_3_13
                                        player.c "Stay like that until I decide you can go home."
                                        rae.c "I do what you tell me to!"
                                        wt_image living_room.image
                                        "You spend the afternoon getting a few things done before you return to Rae."
                                        wt_image store_clerk_date_3_13
                                player.c "Did you enjoy our date?"
                                rae.c "Yes!  I do you what you tell me to!"
                                "Rae will remember that she enjoyed your date, even if she doesn't remember why."
                    "Spank her" if not rae.date_spank:
                        $ rae.date_spank = True
                        player.c "I'm the man and you're the woman, so yes, I do get to decide."
                        rae.c "What does that mean?"
                        player.c "It means when you don't obey me, you get punished.  Turn around."
                        wt_image store_clerk_date_3_15
                        rae.c "Is this a joke?"
                        player.c "No, it's domestic discipline. When a girlfriend doesn't listen to her boyfriend, she gets spanked."
                        rae.c "You can't be serious???"
                        wt_image store_clerk_date_3_16
                        "*smack*"
                        rae.c "Ouch!"
                        wt_image store_clerk_date_3_17
                        "*smack*  *smack*  *smack*  *smack*  *smack*"
                        rae.c "Ow!  Ow!  Ow!!  Oww!!  Owww!!"
                        wt_image store_clerk_date_3_18
                        rae.c "I don't like domestic discipline.  Let's not do that again."
                        player.c "Then in the future I suggest you listen to me."
                        $ rae.spank_count += 1
                        $ rae.maintain_week_gf -= 2
                        change player energy by -energy_short notify
                    "Relent":
                        player.c "Okay, fine.  You're right, Rae.  How about we go grab some food?"
                        wt_image store_clerk_date_3_7
                        rae.c "Thank you! That'd be nice."
                        wt_image store_clerk_restaurant_2
                        "The two of you grab a bite to eat ..."
                        wt_image store_clerk_date_3_1
                        "... then you head back to your place."
                        rae.c "Thanks for taking me out when you wanted to stay in.  You are so sweet!  I really enjoyed our date."
                        $ title = "What do you say?"
                        menu:
                            "Date's not over":
                                $ rae.temporary_count = 1
                                player.c "Do you need to rush home?"
                                rae.c "Nooo ... what did you have in mind?"
                            "I did, too":
                                player.c "So did I, Rae."
                                rae.c "I hope you invite me out again soon!"
                                change player energy by -energy_very_short notify
            "That earned you another spanking" if rae.date_spank:
                wt_image store_clerk_date_3_19
                player.c "That earned you another spanking."
                rae.c "Seriously???  Just because I questioned you?"
                wt_image store_clerk_date_3_20
                "Rae isn't into domestic discipline and doesn't understand why you feel the need to punish her, but despite that ..."
                wt_image store_clerk_date_3_16
                "... she lets you spank her anyway ...  *smack*"
                rae.c "Ouch!"
                wt_image store_clerk_date_3_17
                "*smack*  *smack*  *smack*  *smack*  *smack*"
                rae.c "Ow!  Ow!  Ow!!  Oww!!  Owww!!"
                wt_image store_clerk_date_3_18
                rae.c "I don't really think it's okay for a boyfriend to spank his girlfriend."
                player.c "I do, or I wouldn't have spanked you."
                $ rae.spank_count += 1
                $ rae.strike_count += 1
                sys "Rae's less happy with your relationship."
                $ rae.maintain_week_gf -= 2
                change player energy by -energy_short notify
        if rae.temporary_count == 1:
            $ rae.temporary_count = 0
            $ title = "What did you have in mind?"
            menu:
                "Blow job":
                    wt_image store_clerk_date_3_21
                    "Rae takes off her clothes ..."
                    wt_image store_clerk_date_3_22
                    "... and takes out your dick, licks it hard ..."
                    wt_image store_clerk_date_3_23
                    "... and then sucks on you until you're ready to cum."
                    $ title = "Where do you want to cum?"
                    menu:
                        "In her":
                            wt_image store_clerk_date_3_3
                            player.c "[player.orgasm_text]"
                            wt_image store_clerk_date_3_11
                            rae.c "I like blowing you, but maybe next time we can do something that gets me off, too?"
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_swallow_count += 1
                            else:
                                $ rae.swallow_count += 1
                        "On her":
                            wt_image store_clerk_date_3_4
                            player.c "[player.orgasm_text]"
                            wt_image store_clerk_date_3_24
                            rae.c "I like blowing you, but maybe next time we can do something that gets me off, too?"
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_facial_count += 1
                            else:
                                $ rae.facial_count += 1
                    if rae.has_tag('hypno_girlfriend'):
                        $ rae.hypno_blowjob_count += 1
                    else:
                        $ rae.blowjob_count += 1
                    orgasm notify
                "Sex":
                    wt_image store_clerk_date_3_21
                    "Rae takes off her clothes ..."
                    wt_image store_clerk_date_3_25
                    "... and impales herself on your cock."
                    rae.c "oohhh"
                    $ title = "Have her fuck you this way?"
                    menu:
                        "Yes, this is nice":
                            wt_image store_clerk_date_3_5
                            "Facing this way, you're able to suckle her breasts as she rides you both to climax."
                            rae.c "ooohhhhh"
                            wt_image store_clerk_date_3_26
                            rae.c "ooohhhhh ... yeesss!"
                            player.c "[player.orgasm_text]"
                            wt_image store_clerk_date_3_11
                            rae.c "Now that was a great date!"
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_sex_count += 1
                                $ rae.hypno_orgasm_count += 1
                            else:
                                $ rae.sex_count += 1
                                $ rae.orgasm_count += 1
                            $ rae.maintain_week_gf += 1
                            orgasm notify
                        "No, turn her around":
                            wt_image store_clerk_date_3_26
                            player.c "Turn around."
                            rae.c "But I like to look at you."
                            player.c "And I like to look at your butt."
                            wt_image store_clerk_date_3_6
                            "She's inclined to argue or make a fuss, but your cock feels too good sliding in and out of her ..."
                            rae.c "ooohhhhh"
                            wt_image store_clerk_date_3_28
                            "... and it's hard to pout when you're having an orgasm."
                            rae.c "ooohhhhh ... yeesss!"
                            player.c "[player.orgasm_text]"
                            wt_image store_clerk_date_3_11
                            rae.c "I guess it felt okay facing that way, but I still prefer to see my boyfriend's face when we're having sex."
                            if rae.has_tag('hypno_girlfriend'):
                                $ rae.hypno_sex_count += 1
                                $ rae.hypno_orgasm_count += 1
                            else:
                                $ rae.sex_count += 1
                                $ rae.orgasm_count += 1
                            orgasm notify
                "Pleasure her":
                    wt_image store_clerk_date_3_2
                    "You strip her naked and pull her onto your lap, your hands wrapping around and squeezing her incredible tits."
                    rae.c "oohhh"
                    wt_image store_clerk_date_3_29
                    "Then you lay her on her back as you suckle her erect nipples ..."
                    rae.c "ooohhhh"
                    wt_image store_clerk_date_3_30
                    "... and kiss your way down her belly to her sex ..."
                    rae.c "oooohhhhh"
                    wt_image store_clerk_date_3_31
                    "... where you lap her to an intense, body wracking orgasm."
                    rae.c "ooohhhhh ... yeesss!"
                    wt_image store_clerk_date_3_11
                    rae.c "Wow!  That was amazing.  You take me on the best dates!"
                    if rae.has_tag('hypno_girlfriend'):
                        $ rae.hypno_orgasm_count += 1
                    else:
                        $ rae.orgasm_count += 1
                    $ rae.maintain_week_gf += 1
                    change player energy by -energy_short notify
    rem tags 'on_date' from rae
    call character_location_return(rae) from _call_character_location_return_8
    return

## Showgirl Actions
label rae_dance:
    $ rae.dance_outfit += 1
    # scroll 1 to 3
    if rae.dance_outfit > 3:
        $ rae.dance_outfit = 1
    if rae.dance_outfit == 1:
        wt_image store_clerk_strip_outfit_1_1
        "A hush falls over the audience when Rae steps onto the stage."
        wt_image store_clerk_strip_outfit_1_9
        "She's part dancer ..."
        wt_image store_clerk_strip_outfit_1_2
        "... part animal ..."
        wt_image store_clerk_strip_outfit_1_3
        "... and all woman."
        wt_image store_clerk_strip_outfit_1_4
        "She captivates her audience ..."
        wt_image store_clerk_strip_outfit_1_5
        "... draws them into her ..."
        wt_image store_clerk_strip_outfit_1_6
        "... mesmerising them ..."
        wt_image store_clerk_strip_outfit_1_7
        "... offering them a glimpse of heaven ..."
        wt_image store_clerk_strip_outfit_1_10
        "... only to leave them wanting more."
    elif rae.dance_outfit == 2:
        wt_image store_clerk_strip_outfit_2_1
        "Rae looks stunning, as always, as she steps on to the stage."
        wt_image store_clerk_strip_outfit_2_2
        "She quickly grabs the audience's attention ..."
        wt_image store_clerk_strip_outfit_2_3
        "... and makes sure she holds it."
        wt_image store_clerk_strip_outfit_2_9
        "Rumor at the Club is ..."
        wt_image store_clerk_strip_outfit_2_4
        "... all she's ever wanted to be was a showgirl ..."
        wt_image store_clerk_strip_outfit_2_5
        "... and that she's thankful for every opportunity to be on stage."
        wt_image store_clerk_strip_outfit_2_10
        "Part of that rumor is true."
        wt_image store_clerk_strip_outfit_2_6
        "She is thankful for the opportunity to be on stage."
        wt_image store_clerk_strip_outfit_2_7
        "Her audience is thankful, too ..."
        wt_image store_clerk_strip_outfit_2_11
        "... even if she always leaving them wanting more."
    else:
        wt_image store_clerk_strip_outfit_3_2
        "Like all the best showgirls ..."
        wt_image store_clerk_strip_outfit_3_3
        "... Rae seems both completely oblivious to her audience ..."
        wt_image store_clerk_strip_outfit_3_4
        "... and completely in tune with them at the same time."
        wt_image store_clerk_strip_outfit_3_5
        "Their wants are her wants."
        wt_image store_clerk_strip_outfit_3_6
        "They want to see her body ..."
        wt_image store_clerk_strip_outfit_3_7
        "... she wants them to see her body."
        wt_image store_clerk_strip_outfit_3_8
        "And like all good performers, she knows that when the audience has been entertained and is still enjoying themselves ..."
        wt_image store_clerk_strip_outfit_3_9
        "... that's the time to end the show, and send them home wanting just a little bit more."
    change player energy by -energy_very_short notify
    #add tags 'trained_today' to rae
    add tags 'watched_today' to rae
    return

## Bimbo Actions
label rae_bimbo_actions:
    add tags 'trained_today' to rae
    $ rae.bimbo_outfit += 1
    if rae.bimbo_outfit > 3:
        $ rae.bimbo_set_1_countdown -= 1
        if rae.bimbo_set_1_countdown < 1:
            $ rae.bimbo_outfit = 1
        else:
            $ rae.bimbo_outfit = 2
    if rae.bimbo_outfit == 1:
        $ rae.bimbo_set_1_countdown = 3
        wt_image store_clerk_bimbo_1_1
        "You find Rae standing alone in front of the mirror."
        wt_image store_clerk_bimbo_1_2
        "She does know that's her reflection, doesn't she? Perhaps she's just admiring her own beauty?"
        wt_image store_clerk_bimbo_1_3
        "Uh oh.  Now she's kissing the mirror."
        wt_image store_clerk_bimbo_1_4
        "You leave her alone to spend some quality time with her own reflection"
        $ rae.change_image('store_clerk_bimbo_1_4')
    elif rae.bimbo_outfit == 2:
        wt_image store_clerk_bimbo_2_1
        $ rae.bimbo_joke_count += 1
        if rae.bimbo_joke_count > 3:
            $ rae.bimbo_joke_count = 1
        if rae.bimbo_joke_count == 1:
            rae.c "Hiii ... Do you know why I'm wearing clothes?"
            player.c "No.  Why are you wearing clothes?"
            rae.c "Silly!!  I asked you first!  Are we going to have sex now?"
        if rae.bimbo_joke_count == 2:
            rae.c 'Hiii ... How does that joke go?  The one that starts "knock knock"?'
            player.c "Who's there?"
            rae.c "It's just you and me, silly!!  Are we going to have sex now?"
        else:
            rae.c "Hiii ... I just had a thought."
            player.c "What was it?"
            rae.c "What was what?  Are we going to have sex now?"
        $ rae.change_image('store_clerk_bimbo_2_1')
        $ title = "What do you want?"
        menu:
            "Blow Job":
                wt_image store_clerk_bimbo_2_7
                player.c "Just blow me, Rae."
                rae.c "Okay"
                wt_image store_clerk_bimbo_2_8
                rae.c "I like sucking cock."
                wt_image store_clerk_bimbo_2_11
                "She's good at it, too."
                wt_image store_clerk_bimbo_2_9
                "And patient. She'll happily pleasure your dick for hours, or at least until you can't hold out any longer."
                $ title = "Where do you want to cum?"
                menu:
                    "In her mouth":
                        wt_image store_clerk_bimbo_2_10
                        player.c "[player.orgasm_text]"
                        $ rae.swallow_count += 1
                        wt_image store_clerk_bimbo_2_9
                        player.c "You need to stop sucking my cock now, Rae."
                        wt_image store_clerk_bimbo_2_11
                    "On her face":
                        wt_image store_clerk_bimbo_2_11
                        player.c "I'm going to cum now, Rae."
                        wt_image store_clerk_bimbo_2_12
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_bimbo_2_13
                        player.c "You need to stop sucking my cock now, Rae."
                        wt_image store_clerk_bimbo_2_14
                        $ rae.facial_count += 1
                rae.c "I like sucking cock."
                player.c "I know.  I'll let you suck it again, later."
                rae.c "Okay"
                $ rae.blowjob_count += 1
                orgasm notify
            "Tit Job":
                wt_image store_clerk_bimbo_2_7
                player.c "I'm going to fuck your tits, Rae."
                rae.c "Okay"
                player.c "You don't mind me treating you like just a pair of tits, do you?"
                wt_image store_clerk_bimbo_2_15
                rae.c "I'm just a pair of titties to you??  That makes me so happy!!!"
                wt_image store_clerk_bimbo_2_3
                rae.c "Thank you for fucking me.  It feels sooo good being a pair of titties for you."
                wt_image store_clerk_bimbo_2_4
                player.c "[player.orgasm_text]"
                rae.c "Since I'm just a pair of titties, let me know if you want me to wear a bra over my whole body."
                $ rae.titfuck_count += 1
                orgasm notify
            "Doggy Style":
                wt_image store_clerk_bimbo_2_16
                player.c "Turn around, Rae. I'm going to fuck you doggy style."
                rae.c "Okay"
                wt_image store_clerk_bimbo_2_17
                rae.c "Wait.  Does that mean you want me to make sounds like a dog while you're fucking me?"
                $ title = "Should she bark for you?"
                menu:
                    "Yes, be a dog for me":
                        wt_image store_clerk_bimbo_2_18
                        rae.c "Meow ... meow ... Oh wait!  You said dog."
                        wt_image store_clerk_bimbo_2_19
                        rae.c "Oink ... oink ... No, that's not it either."
                        wt_image store_clerk_bimbo_2_5
                        rae.c "I remember!  Quack .... quack ... quack ..."
                        "Duck, dog, whatever ..."
                        wt_image store_clerk_bimbo_2_20
                        "... her pussy still feels good."
                        player.c "[player.orgasm_text]"
                        rae.c "Quack ... quack ..."
                        player.c "You can stop barking now, Rae.  I already came."
                        rae.c "Okay"
                    "No, just get your clothes off":
                        wt_image store_clerk_bimbo_2_18
                        player.c "That's not necessary, Rae.  Just undress."
                        rae.c "Okay.  Good!  I'm not good with animals.  I had a gerbil once that tried to bite me."
                        wt_image store_clerk_bimbo_2_19
                        player.c "That's not ... never mind."
                        "She may not be good with animals, but she's good at fucking ..."
                        wt_image store_clerk_bimbo_2_5
                        "... and she comes on a hair trigger when her brain's not distracted with having to think.  Which is pretty much always, these days."
                        rae.c "ooohhhhh ... yeesss!"
                        wt_image store_clerk_bimbo_2_20
                        player.c "[player.orgasm_text]"
                        rae.c "Was I a good doggy?"
                        player.c "That's just a ... never mind."
                        $ rae.orgasm_count += 1
                $ rae.sex_count += 1
                orgasm notify
            "Missionary":
                wt_image store_clerk_bimbo_2_21
                player.c "Yes, Rae.  We're going to have sex now."
                rae.c "Yay!!!  Sex is like my favoritest thing ever!"
                wt_image store_clerk_bimbo_2_22
                "She does love sex. She must be perpetually horny, as she climaxes almost the instant your cockhead penetrates her."
                rae.c "ooohhhhh ... yeesss!"
                wt_image store_clerk_bimbo_2_6
                rae.c "Oh my gaaawd!!  You must be the best at sex ever!"
                player.c "I've just started, Rae."
                rae.c "I'm sorry.  Should I have waited for you?"
                player.c "Just be quiet for a minute while I fuck you."
                rae.c "Okay!  Take your time.  I like it when you fuck me!!"
                wt_image store_clerk_bimbo_2_23
                "She is indeed content to lie there and let you fuck her as long as you like."
                wt_image store_clerk_bimbo_2_24
                "You take your time and enjoy yourself, but eventually your balls need release."
                $ title = "Where do you want to cum?"
                menu:
                    "In her":
                        wt_image store_clerk_bimbo_2_25
                        player.c "[player.orgasm_text]"
                        rae.c "ooohhhhh ... yeesss!"
                        wt_image store_clerk_bimbo_2_6
                        rae.c "Oh my gaaawd!!  Your cum made me cum!  You really are the best at sex ever!!!  Will you fuck me again?"
                        player.c "Not right now, Rae."
                        rae.c "Soon?  Please??  Pretty please???  I like sex!"
                        $ rae.orgasm_count += 2
                    "On her":
                        wt_image store_clerk_date_6_11
                        player.c "[player.orgasm_text]"
                        rae.c "Oh! Your cum is so pretty!!"
                        wt_image store_clerk_bimbo_2_4
                        rae.c "Cum on me again.  I like it when you cum on me!"
                        player.c "Not right now, Rae."
                        rae.c "Soon?  Please??  Pretty please???  I like being a cum dump!"
                        $ rae.orgasm_count += 1
                $ rae.sex_count += 1
                orgasm notify
            "Cowgirl":
                wt_image store_clerk_bimbo_2_21
                player.c "Get your clothes off, Rae.  You're going to ride my dick."
                rae.c "Yay!!!  I like having your dick inside me!"
                wt_image store_clerk_bimbo_2_26
                "She undresses, and you pull her down on top of you."
                wt_image store_clerk_bimbo_2_27
                rae.c "Wait ... I have to turn around."
                player.c "Don't you want to face me?"
                rae.c "If I face you, you won't be able to watch my ass bouncing up and down as I ride you, silly!"
                wt_image store_clerk_bimbo_2_28
                "No sooner than she's turned around ..."
                wt_image store_clerk_bimbo_2_29
                "... she's already cumming."
                rae.c "ooohhhhh ... yeesss!"
                wt_image store_clerk_bimbo_2_30
                "You don't take much longer."
                player.c "[player.orgasm_text]"
                rae.c "I knew you'd like watching my ass!  I can almost be smart sometimes."
                $ rae.orgasm_count += 1
                $ rae.sex_count += 1
                orgasm notify
            "Just examine her":
                wt_image store_clerk_bimbo_2_21
                player.c "Are you horny again, Rae?"
                rae.c "Uh huh!  I'll show you!!"
                wt_image store_clerk_bimbo_2_31
                rae.c "My pussy is all tingly and warm."
                wt_image store_clerk_bimbo_2_32
                rae.c "Please look at it for me.  Maybe it just needs something inside it?"
                wt_image store_clerk_bimbo_2_2
                "The smell of her arousal assaults your nose as she takes her panties off. She's wet. She's always wet, and she cums as soon as you put a digit in her."
                rae.c "ooohhhhh ... yeesss!"
                if rae.has_item(dildo):
                    player.c "Have you been remembering to fuck your dildo, Rae?"
                    rae.c  "Uh huh. At least, I think so. I have trouble with time sometimes. Is today Wednesday?"
                else:
                    "The poor thing needs more sex than any man could possibly give her. You should get her something to relieve herself with."
                $ rae.orgasm_count += 1
            "Just have her undress":
                $ rae.change_image('store_clerk_bimbo_image_2')
                player.c "You shouldn't be wearing clothes, Rae."
                if rae.bimbo_joke_count == 1:
                    wt_image store_clerk_bimbo_2_15
                    rae.c "I wondered about that!  I don't know how these got on me."
                else:
                    wt_image store_clerk_bimbo_2_7
                    rae.c "Okay.  Should I take them off?"
                    wt_image store_clerk_bimbo_2_21
                    player.c "Yes, Rae."
                wt_image store_clerk_bimbo_2_33
                rae.c "What do I do once I'm naked?"
                player.c "Just stand there."
                wt_image store_clerk_bimbo_image_2
                rae.c "Do I look stupid, standing here naked?"
                player.c "A bit."
                rae.c "Oh, good!  I am stupid and naked.  I just wanted to make sure I was doing it right."
                player.c "You're doing fine, Rae."
    elif rae.bimbo_outfit == 3:
        wt_image store_clerk_bimbo_3_1
        "Rae appears to be in a bad way when you check in on her.  Surely it hasn't been that long since she's had sex?"
        wt_image store_clerk_bimbo_3_10
        rae.c "Please fuck me.  I need your cock in my cunt soooo bad!"
        $ title = "What do you do?"
        menu:
            "Fuck her":
                wt_image store_clerk_bimbo_3_2
                player.c "Okay, Rae. I'll fuck you."
                rae.c "Yay!!!"
                wt_image store_clerk_bimbo_3_11
                rae.c "Please put your cock right here!  Please?  Please??  Please???"
                wt_image store_clerk_bimbo_3_12
                rae.c "ooohhhhh ... yeesss!"
                $ rae.orgasm_count += 1
                wt_image store_clerk_bimbo_3_13
                player.c "Did you just cum that quickly?"
                rae.c "Uh huh"
                wt_image store_clerk_bimbo_3_9
                rae.c "ooohhhhh ... yeesss!"
                $ rae.orgasm_count += 1
                wt_image store_clerk_bimbo_3_13
                rae.c "Are you going to cum too?"
                $ title = "Are you going to cum?"
                menu:
                    "In her":
                        wt_image store_clerk_bimbo_3_15
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_bimbo_3_14
                        rae.c "Mmmm. I like to be full of cum. I hope that's not dumb. Oh wait! I am dumb! I'm not old, dumb, and full of cum!!"
                        "She starts giggling uncontrollably, amused by what passes for cleverness, by bimbo standards."
                        $ rae.change_image('store_clerk_bimbo_3_14')
                        orgasm notify
                    "On her":
                        wt_image store_clerk_bimbo_3_16
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_bimbo_3_17
                        rae.c "Do my tits look bigger with cum on them? I think they must be bigger, because now they have cum on them."
                        $ rae.change_image('store_clerk_bimbo_3_2')
                        orgasm notify
                    "Not today":
                        wt_image store_clerk_bimbo_3_14
                        player.c "Not today, Rae.  Let's make this just about you today."
                        rae.c "Why?  Doesn't my pussy feel good?"
                        player.c "It does, but I have other things I want to do right now."
                        rae.c "Why?  Cumming is good."
                        player.c "It is, but I need to go now."
                        rae.c "Why?"
                        player.c "This conversation is over, Rae."
                        rae.c "Why?"
                        $ rae.change_image('store_clerk_bimbo_3_14')
                        change player energy by -player.energy_short notify
            "Tell her to blow you":
                player.c "You can put my cock in your mouth, Rae."
                wt_image store_clerk_bimbo_3_24
                rae.c "Yes!!!"
                wt_image store_clerk_bimbo_3_25
                rae.c "I like cock in my mouth almost as much as I like cock in my cunt."
                wt_image store_clerk_bimbo_3_26
                rae.c "Did you know that cock in my mouth makes my cunt all tingly?"
                player.c "Don't talk, Rae.  Just suck me off."
                wt_image store_clerk_bimbo_3_5
                rae.c "Okay.  Are you going to cum in my mouth or on my face?"
                $ title = "Which is it?"
                menu:
                    "In her mouth":
                        wt_image store_clerk_bimbo_3_6
                        player.c "[player.orgasm_text]"
                        $ rae.swallow_count += 1
                        wt_image store_clerk_bimbo_3_18
                        rae.c "Am I more likely to get pregnant if you cum in my mouth or in my pussy?"
                        player.c "Neither, if you take your birth control pills."
                        wt_image store_clerk_bimbo_3_2
                        rae.c "Are those the ones that come in the colored containers with the different funny heads on the top of them?"
                        $ rae.change_image('store_clerk_bimbo_3_2')
                    "On her face":
                        wt_image store_clerk_bimbo_2_12
                        player.c "[player.orgasm_text]"
                        $ rae.facial_count += 1
                        wt_image store_clerk_bimbo_3_7
                        rae.c "Am I a good cum dump?"
                        $ title = "What do you tell her?"
                        menu:
                            "Sure":
                                wt_image store_clerk_bimbo_3_27
                                rae.c "Yay!!  I'm the bestest cum dump!  I'm the bestest cum dump!"
                                $ rae.change_image('store_clerk_bimbo_3_27')
                            "Not really":
                                rae.c "Maybe with practice, I could learn to be a good cum dump? Do you think bimbos can get better at it, if they try?"
                                $ rae.change_image('store_clerk_bimbo_3_7')
                $ rae.blowjob_count += 1
                orgasm notify
            "Tell her to play with herself":
                wt_image store_clerk_bimbo_3_18
                player.c "Use your fingers, Rae."
                rae.c "My fingers aren't a cock, silly!"
                wt_image store_clerk_bimbo_3_19
                player.c "No, but if you rub them on your clit, you'll feel better."
                rae.c "I will?"
                wt_image store_clerk_bimbo_3_20
                rae.c "oohhh ... that does feel good."
                wt_image store_clerk_bimbo_3_21
                rae.c "ooohhhh  ... wow!"
                wt_image store_clerk_bimbo_3_22
                rae.c "ooohhhhh ... yeesss!"
                wt_image store_clerk_bimbo_3_23
                rae.c "Do other women know about this??"
                player.c "Most of them figure it out, yes."
                $ rae.masturbation_count += 1
                $ rae.orgasm_count += 1
                $ rae.change_image('store_clerk_bimbo_3_20')
            "Remind her to use her sex toy" if rae.has_item(dildo):
                player.c "Have you been using your sex toy, Rae?"
                wt_image store_clerk_bimbo_3_2
                rae.c "I forgot!"
                wt_image store_clerk_dildo_1_2
                rae.c "How do I use it again?"
                $ title = "How should she use it?"
                menu:
                    "Spread her legs":
                        player.c "Do what you do best, Rae.  Spread your legs."
                        wt_image store_clerk_dildo_1_3
                        player.c "Don't forget the other part."
                        "She thinks hard ..."
                        wt_image store_clerk_dildo_1_18
                        "... then remembers the second part of her toy."
                        wt_image store_clerk_dildo_1_19
                        player.c "Turn the vibrators on."
                        wt_image store_clerk_dildo_1_20
                        "*bzzzzzt*"
                        rae.c "oohhhh"
                        wt_image store_clerk_dildo_1_21
                        rae.c "ooohhhhh ... yeesss!"
                        $ rae.orgasm_count += 1
                        player.c "Get it right on your clit, Rae."
                        wt_image store_clerk_dildo_1_22
                        rae.c "OOOOHHHHHHH!!!!!"
                        "That should hold her for a while."
                        $ rae.change_image('store_clerk_dildo_1_7')
                    "Bend over":
                        wt_image store_clerk_bimbo_3_28
                        player.c "Get in an awkward position."
                        rae.c "Why?"
                        player.c "You cum too easy.  Try to make it a challenge."
                        wt_image store_clerk_dildo_1_13
                        player.c "Maybe not that awkward.  Just bend over with your ass towards me."
                        wt_image store_clerk_dildo_1_14
                        player.c "Turn the vibrators on."
                        wt_image store_clerk_dildo_1_15
                        "*bzzzzzt*"
                        rae.c "oohhhh"
                        wt_image store_clerk_dildo_1_16
                        rae.c "ooohhhhh ... yeesss!"
                        $ rae.orgasm_count += 1
                        player.c "Get it right on your clit, Rae."
                        wt_image store_clerk_dildo_1_17
                        rae.c "OOOOHHHHHHH!!!!!"
                        "That should hold her for a while."
                        $ rae.change_image('store_clerk_dildo_1_16')
                    "Kneel in front of the mirror":
                        wt_image store_clerk_dildo_1_8
                        player.c "Kneel down in front of the mirror.  Bum up and face me."
                        wt_image store_clerk_bimbo_3_4
                        rae.c "I can't see myself in the mirror this way."
                        wt_image store_clerk_dildo_1_9
                        player.c "That's okay.  I can.  Turn the vibrators on."
                        wt_image store_clerk_dildo_1_10
                        "*bzzzzzt*"
                        rae.c "oohhhh"
                        wt_image store_clerk_dildo_1_11
                        rae.c "ooohhhhh ... yeesss!"
                        $ rae.orgasm_count += 1
                        player.c "Get it right on your clit, Rae."
                        wt_image store_clerk_dildo_1_12
                        rae.c "OOOOHHHHHHH!!!!!"
                        "That should hold her for a while."
                        $ rae.change_image('store_clerk_dildo_1_11')
                $ rae.masturbation_count += 1
                $ rae.orgasm_count += 1
    # set her image at the end of each scene, which she'll hold until next day
    return

## Character Specific Objects
# Watch Rae Fuck In Club
# OBJECT: Watch Your Girlfriend
label rae_watch:
    "You'll never convince Rae to join you at a swingers event."
    return

## Items
# Review Boudoir Photos
label rae_review_files_boudoir_photos:
    wt_image store_clerk_reward_5_1
    rae.c "{i}I wanted to make something special for you.{/i}"
    wt_image store_clerk_reward_5_2
    rae.c "{i}I hired a professional photographer to take some photos of me.{/i}"
    wt_image store_clerk_reward_5_3
    rae.c "{i}I hope you don't mind me letting another man look at my body.  The photographer was very professional.  He didn't try to touch me or anything.{/i}"
    wt_image store_clerk_reward_5_4
    rae.c "{i}I thought it would be okay, in order to make a gift for you of the way I look.{/i}"
    wt_image store_clerk_reward_5_5
    rae.c "{i}I won't always be this young and ... well, you say I'm beautiful, so I'll say it too.  This young and beautiful.{/i}"
    wt_image store_clerk_reward_5_7
    rae.c "{i}The photo shoot was expensive, but I think it was worth it.  Now you'll always have these photos to look at, if you want to.{/i}"
    wt_image store_clerk_reward_5_6
    rae.c "{i}In case, who knows, maybe we grow old and grey together someday, but want to remember me in my youth.{/i}"
    return

# Review Selfies
label rae_review_files_selfies:
    wt_image store_clerk_gf_selfie_1
    "Rae sent you some pictures of herself."
    wt_image store_clerk_gf_selfie_2
    "You saved them on your computer to remind you of her."
    wt_image store_clerk_gf_selfie_3
    "The selfies are so Rae."
    if rae.girlfriend_reward_count > 0:
        wt_image store_clerk_reward_1_1
        "With Rae, what you see is what you get."
    return

# Give Butt Plug
label give_bp_rae:
    "She's not that sort of gal.  There's no good reason for that.  She just isn't."
    return

# Give Chastity Belt
label give_cb_rae:
    if rae.has_tag('bimbo'):
        "She's already stupid.  Do you want to drive her insane as well?"
    else:
        "You should save this for someone who has trouble keeping her legs together."
    return

# Give Dildo
label give_di_rae:
    if rae.has_item(dildo):
        "She has enough dildos now."
    elif rae.has_tag('masturbated'):
        if rae.date_outfit == 1:
            wt_image store_clerk_date_1_10
        elif rae.date_outfit == 2:
            wt_image store_clerk_date_2_9
        elif rae.date_outfit == 3:
            wt_image store_clerk_date_5_1
        elif rae.date_outfit == 4:
            wt_image store_clerk_date_6_1
        elif rae.date_outfit == 5:
            wt_image store_clerk_date_4_7
        else:
            wt_image store_clerk_date_3_8
        rae.c "What's this for?  I'd rather spend time with you."
        player.c "You can save it for times when I'm around to watch, if you want."
        give 1 dildo from player to rae
    elif rae.has_tag('bimbo'):
        wt_image store_clerk_dildo_1_1
        rae.c "What is that?"
        player.c "It's a toy for you.  This part works like a dick, except it vibrates."
        wt_image store_clerk_dildo_1_2
        rae.c "Do I suck on it to get it to work?"
        player.c "It's not like a dick in that way.  Just give the end of it a twist."
        wt_image store_clerk_dildo_1_3
        "*bzzzzzt*"
        rae.c "Oh!  It's buzzing!!  And it's making my pussy all wet."
        player.c "Your pussy's always wet, Rae.  That's why you need one of these.  Put it in your pussy."
        wt_image store_clerk_dildo_1_4
        rae.c "oohhh ... this is perfect!  Thank you!"
        wt_image store_clerk_dildo_1_5
        player.c "There's a second part, too."
        rae.c "What do I need anything else for?"
        wt_image store_clerk_bimbo_3_3
        rae.c "It looks complicated."
        player.c "Just turn it on and press it against your sex as you fuck yourself."
        wt_image store_clerk_dildo_1_6
        "*bzzzzzt*"
        rae.c "Like this?"
        player.c "Get it right on your clit."
        wt_image store_clerk_dildo_1_7
        rae.c "OOOOHHHHHHH!!!!!"
        "Now she's got the hang of it.  That should keep her occupied."
        $ rae.orgasm_count += 1
        give 1 dildo from player to rae
    elif rae.has_tag('showgirl'):
        "Some dancers would incorporate this into their show, but Rae doesn't need props."
    else:
        "You should save this for another time or another woman."
    return

# Use Fetch Toy
label use_ft_rae:
    "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_rae:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_rae:
    "You shouldn't try to take someone for a walk who isn't your pet."
    return

# Give Lingerie
label give_li_rae:
    if rae.has_item(lingerie):
        "You've already gifted lingerie to Rae.  She has enough for now."
    elif rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'):
        if rae.first_date_complete:
            if rae.location == living_room:
                # note: image references are offset by one so she always shows the next date outfit she will wear when you Start the Date
                if rae.date_outfit == 1:
                    wt_image store_clerk_date_2_9
                elif rae.date_outfit == 2:
                    wt_image store_clerk_date_5_1
                elif rae.date_outfit == 3:
                    wt_image store_clerk_date_6_1
                else:
                    wt_image store_clerk_date_1_10
                player.c "I bought you something."
                rae.c "A gift!  For meee??  What is it???"
                "Her eyes light up when she sees the lingerie."
                rae.c "Oh my gawd!  Let's skip the date and let me try this on!"
                wt_image living_room.image
                "She disappears into the bathroom to change before you can respond."
                wt_image store_clerk_lingerie_1_1
                "When she reappears, she looks both shy and radiant."
                rae.c "It's beautiful.  I hope I look okay in it?"
                player.c "You look amazing, Rae.  How does it feel?"
                wt_image store_clerk_lingerie_1_2
                rae.c "Sexy.  Like I'm a movie star ... or a princess ... or a new bride."
                "She blushes and looks away from you.  It's not hard to guess which of those three she's really thinking about."
                wt_image store_clerk_lingerie_1_1
                player.c "Show it off for me, Rae.  Give me a little dance."
                rae.c "I couldn't!  I'm not a dancer.  I could never cut it as a showgirl.  I have no rhythm whatsoever!"
                player.c "How would you know until you try?  Anyway, I don't care about that.  I just want to watch my girlfriend dance for me in her sexy new lingerie."
                wt_image store_clerk_lingerie_1_3
                "When you put it that way, she hasn't the heart to deny you.  She sways back and forth ..."
                wt_image store_clerk_lingerie_1_4
                "... slowly gyrating her hips ..."
                wt_image store_clerk_lingerie_1_5
                "... and chest."
                wt_image store_clerk_lingerie_1_1
                rae.c "Sorry.  That probably wasn't a very good dance."
                player.c "It was great, Rae.  But lingerie dances normally involve the lingerie coming off at the end."
                rae.c "You want me to strip for you?  I've never done that.  I'll probably be bad at it."
                player.c "I don't think you will, Rae."
                wt_image store_clerk_lingerie_1_6
                "She pulls the bra straps down ..."
                wt_image store_clerk_lingerie_1_7
                "... freeing her breasts ..."
                wt_image store_clerk_lingerie_1_8
                "... as she resumes swaying."
                wt_image store_clerk_lingerie_1_9
                "Then she slips her hands into her panties ..."
                wt_image store_clerk_lingerie_1_10
                "... and pulls them down as she dances ..."
                wt_image store_clerk_lingerie_1_11
                "... giving you a view of her labia, swollen in excitement from stripping for you."
                wt_image store_clerk_lingerie_1_12
                rae.c "That was really bad, wasn't it?"
                $ title = "What do you tell her?"
                menu:
                    "You did great":
                        player.c "You were great.  You'd make an amazing stripper!"
                        rae.c "That's a terrible thing to say!! I don't want to be a stripper, you know! I worked hard to get a job so I wouldn't end up on a stage being ogled by dirty old men."
                    "It was pretty bad":
                        player.c "Yeah, it was pretty bad. I don't think you'd make it as a stripper."
                        rae.c "Well, I don't want to be a stripper, you know! I worked hard to get a job so I wouldn't end up on a stage being ogled by dirty old men."
                        player.c "Whoa.  Did you actually think of stripping once?"
                rae.c "No!! I mean ... I just ... I never finished high school, okay? There aren't a lot of options for teenage girls who aren't good at school."
                player.c "Were you a stripper?"
                rae.c "No!!! Never! But ... okay, I thought about it. It would've been a lot better than the alternative, you know? But I managed to get better jobs, instead."
                rae.c "I've never taken my clothes off for money. I never will! Can we drop this conversation?"
                wt_image living_room.image
                "Rae disappears to get back into her clothes."
                wt_image store_clerk_sad
                "A contrite looking Rae emerges a few minutes later."
                rae.c "I'm sorry. I don't mind dancing for you. You're my boyfriend. I'm glad you like looking at my body."
                rae.c "And I really do love the lingerie you bought me. Forgive me? I'm looking forward to seeing you again soon. I love you!"
                wt_image living_room.image
                "She disappears, perhaps to avoid having to hear whether you say those same three words back to her."
                $ player.desire_action_count += 1
                give 1 lingerie from player to rae notify
                add tags 'trained_today' to rae
                $ rae.maintain_week_gf = week + 4
                call character_location_return(rae) from _call_character_location_return_9
                change player energy by -energy_very_short
            else:
                "Wait until a date to give this to her."
        else:
            "Wait until the two of you have at least one normal date together before you start plying her with lingerie. She's a girlfriend, not a client."
    elif rae.has_tag('showgirl'):
        "She prefers to pick out her own dance outfits. She's good at it. She used to work retail."
    elif rae.has_tag('bimbo'):
        "She'd never remember to wear it."
    else:
        "You should save this for another time."
    return

# Give Love Potion
label give_lp_rae:
    if rae.has_tag('love_potion_used'):
        "You've already used a love potion on her.  Another one won't have any effect."
    elif rae.has_tag('bimbo'):
        "She's not going anywhere. You can save the potion for somebody who could come up with the idea that they could be with someone other than you."
    elif rae.location == eros_store:
        "Rae doesn't drink when she's working."
    elif rae.location == stage:
        "Rae doesn't drink when she's dancing."
    elif rae.has_tag('girlfriend') or rae.has_tag('hypno_girlfriend'):
        "Rae's already your girlfriend. Giving her the love option may increase her infatuation with you, which may lead her to stay around when she would otherwise leave. It's not likely, however, to overcome her aversion to sharing you with other women."
        $ title = "Use the love potion anyway?"
        menu:
            "Not yet":
                pass
            "Yes, give her the love potion":
                wt_image store_clerk_transformation_1
                player.c "How about a glass of wine?"
                rae.c "I'm not a big drinker."
                wt_image store_clerk_transformation_2
                rae.c "But since this is a date, I guess I could have one."
                wt_image store_clerk_transformation_12
                rae.c "Mmmm.  This is amazing. You're amazing."
                rae.c "I'm the luckiest girl in the world, to have you for my boyfriend!"
                "Her eyes glaze over as she stares at you, lost in the revelry of basking in your presence. She's too dazed by the potion to have a proper date today, but you're confident she'll take your call the next time you want a date with her."
                add tags 'love_potion_used' to rae
                rem 1 love_potion from player notify
    else:
        "Best to save this for a paying client."
    return

# Give Transformation Potion
label give_tp_rae:
    if rae.has_tag('transformed'):
        "Rae's already been transformed.  The potion can do nothing more to her now."
    elif rae.has_tag('waiting_for_club_access'):
        "Rae's already been transformed.  You just need to find her a place where she can safely take her clothes off."
    elif rae.location == eros_store:
        "Rae doesn't drink when she's working."
    elif rae.location == stage:
        "Rae doesn't drink when she's dancing."
    elif rae.location == living_room or rae.location == bedroom:
        $ rae.temporary_count = 1
        if rae.has_tag('love_potion_used'):
            wt_image store_clerk_transformation_2
            player.c "How about a glass of wine?"
            rae.c "Another one? Sure! The last one was amazing."
        else:
            wt_image store_clerk_transformation_1
            player.c "How about a glass of wine?"
            rae.c "I'm not a big drinker."
            wt_image store_clerk_transformation_2
            rae.c "But since this is a date, I guess I could have one."
        wt_image store_clerk_transformation_3
        "The potion takes effect quickly. You see her eyes and mind shutting down as the potion opens her up to the possibility of great change."
        "Rae's not a complicated person. What you see is what you get. In fact, you could say that she has realized every potential she has within her."
        "Every positive potential, in any event. But perhaps she need not have done as much with herself as she has?"
        "The potion seeks out and identifies the positive changes Rae has made in herself, and readies itself to shut some of them down."
        "You now need to focus and devote some energy into sculpting the changes the potion will make in Rae. What do you want to turn her into?"
        $ title = "What to you want to transform her into?"
        menu:
            "Bimbo" if not rae.has_tag('bimbo'):
                "Growing up, Rae was called stupid many times."
                extend '"I'
                extend "'m not stupid,"
                extend '" she would tell herself.  "I'
                extend "'ll show them."
                extend '".'
                "But deep down, the hurtful words planted more than just a seed of doubt. Perhaps she isn't smart enough to make it in this world?"
                "The potion latches on to this doubt, and helps it grow and blossom inside Rae's brain."
                "She is stupid. She's always been stupid. She should embrace it and accept it. It's who she is."
                wt_image store_clerk_bimbo
                "Every thought and worry is pushed out of Rae's head. Except for sex. The potion embraces and stimulates her love of sex. After all, even as a young girl, men loved to stare at her developing body."
                "She has to be good at something, and since she's stupid, it must be sex. That explains how adults treated her when she was growing up. She's too dumb to think, but she's hot enough to be a great fuck."
                "Soon, the only thing she can think about is how good her body feels, how nice it would be to have someone touching her, and how wonderful it would be to use her body to please someone else."
                wt_image store_clerk_transformation_4
                "She's a stupid bimbo. It was who she was born to be. She's happy. She'd be happier if she had your cock inside her."
                $ title = "What do you do with her?"
                menu:
                    "Let her live with you":
                        player.c "Do you like it here?"
                        wt_image store_clerk_transformation_5
                        rae.c "Uh huh.  Can I suck your cock?"
                        wt_image store_clerk_transformation_14
                        "Sucking cocks are what bimbos are for, and Rae's determined to be the best bimbo her brainless self can be."
                        wt_image store_clerk_transformation_15
                        player.c "[player.orgasm_text]"
                        $ rae.blowjob_count += 1
                        $ rae.facial_count += 1
                        wt_image store_clerk_transformation_11
                        player.c "I'm going to let you stay in my bedroom."
                        rae.c "Goody!  Will we have sex there?"
                        player.c "Maybe.  If you're good."
                        rae.c "I'll be the bestest bimbo ever!!"
                        wt_image store_clerk_transformation_7
                        player.c "Rae, you can't keep sucking my cock.  You need to go to the bedroom now."
                        rae.c "mmpphh mmpphh"
                        'Presumably that was "okay", as she reluctantly removes your cock from her mouth and wanders off to find the bedroom.'
                        "Rae won't raise the level of intellectual conversations in your house. On the other hand, the simple joy she gets from sucking your cock is something you could get used to."
                        "In her current state, she also won't object to you being with other women."
                        $ rae.transformed_via_object = True
                        call rae_convert_bimbo from _call_rae_convert_bimbo
                        orgasm
                    "Kick her out":
                        wt_image store_clerk_transformation_13
                        player.c "No, Rae.  That cock's not for you."
                        wt_image store_clerk_bimbo_image_2
                        "She's confused.  If she's not supposed to be sucking your cock, what is she supposed to be doing?"
                        player.c "You can't stay here.  You need to go find some place to live."
                        "You'd tell her to dress, but she's more likely to find someone to take her in if she wanders off like this."
                        $ rae.dismiss(False)
                        wt_image living_room.image
                    "Let her suck you off, then kick her out":
                        wt_image store_clerk_transformation_5
                        "She wants your cock so much, it would be cruel to deny her."
                        wt_image store_clerk_transformation_14
                        "Sucking cocks are what bimbos are for, and Rae's determined to be the best bimbo her brainless self can be."
                        wt_image store_clerk_transformation_15
                        player.c "[player.orgasm_text]"
                        $ rae.blowjob_count += 1
                        $ rae.facial_count += 1
                        wt_image store_clerk_transformation_11
                        $ title = "Reconsider?"
                        menu:
                            "Keep her after all":
                                player.c "I'm going to let you stay in my bedroom."
                                rae.c "Goody!  Will we have sex there?"
                                player.c "Maybe.  If you're good."
                                rae.c "I'll be the bestest bimbo ever!!"
                                wt_image store_clerk_transformation_7
                                player.c "Rae, you can't keep sucking my cock.  You need to go to the bedroom now."
                                rae.c "mmpphh mmpphh"
                                'Presumably that was "okay", as she reluctantly removes your cock from her mouth and wanders off to find the bedroom.'
                                "Rae won't raise the level of intellectual conversations in your house. On the other hand, the simple joy she gets from sucking your cock is something you could get used to."
                                "In her current state, she also won't object to you being with other women."
                                $ rae.transformed_via_object = True
                                call rae_convert_bimbo from _call_rae_convert_bimbo_1
                            "Kick her out":
                                player.c "Show your cum coated tits to all the men you see outside. One of them will take you home with him."
                                rae.c "Goody!"
                                $ rae.dismiss(False)
                                wt_image current_location.image
                        orgasm
            "Showgirl" if not rae.has_tag('showgirl'):
                "As a teenager, Rae realized that if she wasn't careful, she'd end up as a stripper. She didn't want to be a stripper, taking her clothes off for the amusement of men she didn't know."
                "Still, with no education and no money, she recognized that she might have to rely on this as a backup plan if she wasn't able to find a better job for herself, and she steeled her mind for the possibility of subjecting herself to that humiliation."
                "The potion latches on to this mental preparation. Soon stripping isn't a backup plan, it's her main career ambition.  Shedding her clothes for strange men isn't something to tolerate, it's her main ambition in life."
                wt_image store_clerk_transformation_8
                "It's the thing she was meant to be. A showgirl. An entertainer. The best damn stripper anyone in the audience has every seen."
                wt_image store_clerk_transformation_9
                "Still woozy from the effect of the potion, Rae can't manage a proper dance. She stumbles over to the bed, and tries to give you the best show she can in her groggy state."
                $ title = "What do you do?"
                menu menu_rae_showgirl_conversation:
                    "Compliment her":
                        player.c "You're a great dancer, Rae.  You should dance full time."
                        wt_image store_clerk_transformation_16
                        "Rae smiles happily, then passes out, exhausted by the effect of the potion."
                        if player.has_tag('club_access') and player.has_tag('club_first_visit_complete'):
                            "When she wakes up, you'll give her directions to the Club.  She should do well there."
                        else:
                            "You'll need to keep an eye out for somewhere she can safely take her clothes off.  Without an outlet for her urges, who knows where she'll get naked."
                        $ rae.transformed_via_object = True
                        call rae_convert_showgirl from _call_rae_convert_showgirl
                    "Tell her she's terrible dancer":
                        player.c "That was the worst attempt at a strip show I've ever seen."
                        "You're being honest, but a tad unfair, given that the girl can hardly stand until she recovers from the effect of the potion."
                        wt_image store_clerk_sad
                        "Rae bursts into tears. This is the worst fate she ever imagined. She wants to be a showgirl so bad, but she's no good at it. Still sobbing, she staggers to her feet and leaves."
                        wt_image current_location.image
                        "You never see her again.  You assume she leaves town, but where she goes and what she does, you never find out."
                        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
                        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
                        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
                        call convert(rae, "unavailable") from _call_convert_38
                    "Take advantage of her groggy state and fuck her" if not rae.has_tag('fucked_after_showgirl_conversion'):
                        add tags 'fucked_after_showgirl_conversion' to rae
                        wt_image store_clerk_transformation_16
                        "Rae knows that strippers aren't supposed to let their audience touch them, but with her dance finished, she passes out, exhausted by the effect of the potion."
                        wt_image store_clerk_transformation_10
                        "She offers no resistance as you undress her and only a mild protest as you mount her before passing out completely."
                        wt_image store_clerk_transformation_17
                        "In her unconscious state, you're able to fuck her as long and as roughly as you want, before depositing her first stripper tip deep inside her."
                        player.c "[player.orgasm_text]"
                        wt_image store_clerk_transformation_18
                        "When she comes to, she's more concerned about the state of her dancing than the state of her well fucked pussy."
                        rae.c "Was I any good?"
                        orgasm
                        $ title = "She's talking about her dancing"
                        jump menu_rae_showgirl_conversation
                dismiss rae
            "Nothing (undo)":
                $ rae.temporary_count = 0
                "Let's just pretend that didn't happen.  That's easier than reloading an old save."
        wt_image current_location.image
        if rae.temporary_count == 1:
            $ rae.temporary_count = 0
            # note: need the following commands as you may send her off without calling the convert to bimbo or showgirl labels
            rem tags 'flirting' 'working_at_store' from rae
            if not rae.has_tag('bimbo') and not rae.has_tag('showgirl') and not rae.has_tag('waiting_for_club_access'):
                call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_1
            rem 1 transformation_potion from player
            change player energy by -energy_long notify
    else:
        "Not here.  Not now."
    return

# Give Ring of Secuality
label give_rs_rae:
    "That may work, but there's no content for it, so you're better off saving this for someone else."
    return

# Use Water Bowl
label use_wb_rae:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
    return

# Use Will Tamer
label use_wt_rae:
    if rae.has_tag('transformed'):
        "Rae has already been transformed.  The Will_Tamer can do nothing more to her now."
    else:
        "There's no topic of conversation you could raise that would end with [rae.name] agreeing to let you collar her."
    return

########### TIMERS ###########
## Common Timers
# Start Day Timers
label rae_start_day_normal_events:
    # hypnosis maintenance
    if day == 1 and rae.has_tag('hypno_girlfriend'):
        $ rae.temporary_count = player.girlfriend_count + player.bimbo_count + player.slavegirl_count
        if rae.temporary_count > 0:
            "You need to spend energy renewing Rae's hypnosis. Maintaining her will be more difficult, as you need to deal with her concerns about the women who share your bedroom."
        else:
            "You need to spend energy renewing Rae's hypnosis. Maintaining her will cost the same as a normal hypnosis session."
        $ title = "Maintain [rae.full_name] as your hypno-girlfriend?"
        menu:
            "Yes, maintain her":
                wt_image store_clerk_working_7
                "You call [rae.name] and spend some energy maintaining your hypnotic control over her."
                change player energy by -energy_hypnosis notify
                while rae.temporary_count > 0:
                    $ rae.temporary_count -= 1
                    change player energy by -energy_very_short notify
                wt_image current_location.image
            "No, let her go":
                sys "Are you sure? If you don't maintain the hypnotic spell, you'll lose her and be unable to get her back."
                $ title = "Are you sure you want to lose [rae.full_name] as your hypno-girlfriend?"
                menu:
                    "Change your mind and maintain her":
                        wt_image store_clerk_working_7
                        "You call [rae.name] and spend some energy maintaining your hypnotic control over her."
                        change player energy by -energy_hypnosis notify
                        while rae.temporary_count > 0:
                            $ rae.temporary_count -= 1
                            change player energy by -energy_very_short notify
                    "I'm sure, let her go":
                        sys "By not maintaining your hypnotic trance, your control over [rae.name] is lost. She disappears, and you never see her again."
                        $ rae.dismiss(False)
                        call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_6
                        wt_image current_location.image
    if rae.has_tag('bimbo'):
        # set image to match her next Bimbo action scene
        if rae.bimbo_outfit == 1:
            $ rae.change_image('store_clerk_bimbo_3_1')
        elif rae.bimbo_outfit == 2:
            $ rae.change_image('store_clerk_bimbo_2_1')
        else:
            $ rae.change_image('store_clerk_bimbo_1_5')
    if rae.has_tag('waiting_for_club_access') and player.has_tag('club_first_visit_complete') and rae.dancing_at_club:
        "Now that Rae knows about a place where she can safely take her clothes off, perhaps you should pay her a visit."
        rem tags 'waiting_for_club_access' from rae
        call rae_convert_showgirl from _call_rae_convert_showgirl_1
    call character_location_return(rae) from _call_character_location_return_10
    return

# End Day Timers
label rae_end_day:
    if rae.has_tag('on_stage_now'):
        rem tags 'on_stage_now' 'watched_today' from rae
    rem tags 'on_date' from rae
    call character_location_return(rae) from _call_character_location_return_11
    return

# End Week Timers
label rae_end_week:
    # lose her as girlfriend for mistreatment test
    if rae.strike_count > 2 and rae.has_tag('girlfriend'):
        wt_image phone_1
        "Your phone is ringing."
        wt_image store_clerk_working_7
        rae.c "Hi, it's me.  I'm not sure exactly how to say it, so I'll just spit it out."
        rae.c "I don't think you're the right boyfriend for me. I don't like how you treat me sometimes. I think I'd be better off finding someone else."
        wt_image living_room.image
        "You never see her again."
        call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_2
    # she tries to break up if hypno_girlfriend test
    if rae.strike_count > 2 and rae.has_tag('hypno_girlfriend') and not rae.hypno_girlfriend_tried_breakup:
        $ rae.hypno_girlfriend_tried_breakup = True
        wt_image phone_1
        "Your phone is ringing."
        wt_image store_clerk_working_7
        rae.c "Hi, it's me.  I'm not sure exactly how to say it, so I'll just spit it out."
        rae.c "I don't think you're the right boyfriend for me.  I don't like how you treat me sometimes.  I think I'd be better off finding someone else."
        player.c "Rae, listen to me. [rae.trigger_phrase], Rae.  I am your boyfriend and you like how I treat you."
        rae.c "Of course!  You're my boyfriend.  I like the way you treat me.  I hope you'll ask me out again soon."
    # she breaks up if lack of relationship maintenance
    if rae.has_tag('girlfriend') and week >= rae.maintain_week_gf:
        # warning week
        if week == rae.maintain_week_gf:
            wt_image phone_1
            "Rae called while you were out and left a message on your phone."
            rae.c "{i}Hiii, It's me. Do you think maybe we could do something together soon? I miss you! ~ XOXO{/i}"
        $ rae.temporary_count = rae.maintain_week_gf + 2
        # leave week
        if week >= rae.temporary_count:
            if rae.has_tag('love_potion_used'):
                wt_image phone_1
                "Rae called while you were out and left a message on your phone."
                rae.c "{i}Hiii, it's me again. I guess you've been too busy to see me. I understand, I guess, but I miss you. I hope you'll call soon! ~ XOXO{/i}"
            else:
                wt_image phone_1
                "There's a new message on your phone from Rae."
                rae.c "{i}Hi.  It's me again.{/i}"
                rae.c "{i}I guess you're too busy to see me. I wish it could have worked out between us. I'll miss you, but I need to move on and find a new boyfriend. One who has more time to spend with me.  Bye.{/i}"
                "You never see her again."
                call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_3
    # if relationship is strong enough, start earning 'forgiveness' points
    elif rae.strike_count > 1 and rae.has_any_tag('girlfriend', 'hypno_girlfriend'):
        $ rae.forgiveness_count += 1
        if rae.forgiveness_count > 7:
            $ rae.forgiveness_count = 0
            $ rae.strike_count -= 1
            sys "Rae has gotten over some misgivings she had about how you treat her."
    # girlfriend rewards
    if week > rae.girlfriend_reward_week and rae.maintain_week_gf > week and rae.has_tag('girlfriend'):
        $ rae.girlfriend_reward_week = week + renpy.random.randint(4,5)
        $ rae.girlfriend_reward_count += 1
        if rae.girlfriend_reward_count == 1:
            if rae.first_date_complete:
                wt_image phone_1
                "You receive a message from Rae with a photo attached."
                wt_image store_clerk_reward_1_1
                rae.c"{i}Hi! I just wanted to tell you how happy I am being your girlfriend. I can't wait for our next date.{/i}"
                rae.c "{i}All of me is waiting for you.  Kisses and hugs!{/i}"
                wt_image living_room.image
            else:
                $ rae.girlfriend_reward_count = 0
                $ rae.girlfriend_reward_week = week + 2
        elif rae.girlfriend_reward_count == 2:
            wt_image front_door
            "Sunday morning there's a knock on your door."
            summon rae
            wt_image store_clerk_reward_2_10
            rae.c "Hiii ...  Do you like my new hair color?"
            wt_image store_clerk_reward_2_1
            rae.c "Don't worry.  It's not a permanent change."
            wt_image store_clerk_reward_2_2
            rae.c "I just thought you might be getting tired of fucking your girlfriend, and might want some variety."
            wt_image store_clerk_reward_2_3
            rae.c "Do you like seeing a dark-haired woman licking your cock?"
            wt_image store_clerk_reward_2_4
            rae.c "Or sucking on it?"
            wt_image store_clerk_reward_2_5
            rae.c "How about having a dark-haired woman bouncing on your cock?"
            wt_image store_clerk_reward_2_6
            rae.c "That's no good, silly.  It'll still look like me in this position"
            wt_image store_clerk_reward_2_7
            rae.c "That's better.  Fuck this dark-haired stranger!"
            wt_image store_clerk_reward_2_11
            rae.c "ooohhhhh ... yeesss!"
            wt_image store_clerk_reward_2_8
            player.c "[player.orgasm_text]"
            wt_image store_clerk_reward_2_9
            rae.c "So what did you think?  Was it fun fucking your girlfriend while she looked like someone else?"
            player.c "It's a lovely way to start a Sunday, Rae."
            rae.c "I thought it would be a nice way to spice things up.  I wouldn't want you to get bored, sleeping only with me."
            $ rae.orgasm_count += 1
            $ rae.sex_count += 1
            orgasm notify
            call character_location_return(rae) from _call_character_location_return_12
            wt_image living_room.image
        elif rae.girlfriend_reward_count == 3:
            wt_image front_door
            "Sunday morning there's a knock on your door."
            summon rae
            wt_image store_clerk_reward_3_1
            rae.c "Hiii ... Your girlfriend sent me."
            wt_image store_clerk_reward_3_7
            rae.c "She thought you'd like to watch ..."
            wt_image store_clerk_reward_3_2
            rae.c "... a nasty little stripper ..."
            wt_image store_clerk_reward_3_3
            rae.c "... take her clothes off."
            wt_image store_clerk_reward_3_4
            rae.c "Just a slutty little tease ..."
            wt_image store_clerk_reward_3_5
            rae.c "... showing off her body to turn you on."
            wt_image store_clerk_reward_3_8
            rae.c "Remember, you don't get to touch the strippers.  But your girlfriend told me to tell you that if you call her for a date this week ..."
            wt_image store_clerk_reward_3_6
            rae.c "... she promises that she won't play hard to get!"
            "And with that she throws her clothes on and races out the door.  She doesn't even wait long enough for you to give her a tip"
            call character_location_return(rae) from _call_character_location_return_13
            wt_image living_room.image
        elif rae.girlfriend_reward_count == 4:
            if boudoir.has_item(fluffy_cuffs) and not rae.fluffy_cuffs_reward_triggered:
                # reset to allow other rewards at this level if applicable
                $ rae.girlfriend_reward_count -= 1
                call rae_fluffy_cuff_reward from _call_rae_fluffy_cuff_reward
            elif rae.has_item(dildo) and not rae.dildo_reward_triggered:
                # reset to allow other rewards at this level if applicable
                $ rae.girlfriend_reward_count -= 1
                call rae_dildo_reward from _call_rae_dildo_reward
            else:
                wt_image phone_1
                "Saturday afternoon the phone rings."
                wt_image store_clerk_working_7
                rae.c "Hiii.  I hope you don't have plans, because I have reservations at a restaurant for us this evening."
                summon rae
                wt_image store_clerk_reward_7_1
                "When Rae picks you up later, she's dressed to the nines."
                rae.c "Ready for our date?"
                call forced_movement(outdoors) from _call_forced_movement_56
                summon rae
                wt_image recept_date_2
                "She takes you to one of the city's finest restaurants."
                wt_image store_clerk_reward_7_2
                player.c "This place is expensive."
                rae.c "It's okay. I've been saving up my money for a treat for us. You're worth it."
                wt_image store_clerk_hotel_1
                "After your meal, she takes you to a hotel. It's a bit dated and the rooms are small, but the entrance and lobby are quite elegant."
                wt_image store_clerk_reward_7_3
                rae.c "Now that I've wined you and dined you ..."
                wt_image store_clerk_reward_7_4
                rae.c "... will you have sex with me?"
                wt_image store_clerk_reward_7_6
                "If you had any thoughts of saying no ..."
                wt_image store_clerk_reward_7_5
                "... they're vetoed by your dick as soon as she wraps her lips around it."
                wt_image store_clerk_reward_7_7
                "Besides, she's gone through so much trouble to show you a good time ..."
                wt_image store_clerk_reward_7_8
                "... how can you not show her one in return?"
                rae.c "oohhh"
                wt_image store_clerk_reward_7_9
                rae.c "ooohhhhh ... yeesss!"
                wt_image store_clerk_reward_7_10
                player.c "[player.orgasm_text]"
                wt_image store_clerk_reward_7_11
                rae.c "I know I don't make much money, but I'll always chip in and contribute. I'd never expect anyone to look after me, financially."
                $ rae.orgasm_count += 1
                $ rae.sex_count += 1
                orgasm notify
                call forced_movement(living_room) from _call_forced_movement_58
                call character_location_return(rae) from _call_character_location_return_14
        elif rae.girlfriend_reward_count == 5:
            $ rae.boudoir_photos_sent = True
            wt_image phone_1
            "A new message came in from Rae. There are photos attached."
            call rae_review_files_boudoir_photos from _call_rae_review_files_boudoir_photos
        else:
            if boudoir.has_item(fluffy_cuffs) and not rae.fluffy_cuffs_reward_triggered:
                call rae_fluffy_cuff_reward from _call_rae_fluffy_cuff_reward_1
            elif rae.has_item(dildo) and not rae.dildo_reward_triggered:
                call rae_dildo_reward from _call_rae_dildo_reward_1
    return

## Club and Stage Labels
label rae_stage_notice:
    if rae.dancing_at_club == False and rae.has_tag('waiting_for_club_access'):
        "This is the perfect place for Rae to express her 'newfound' interest in dancing. You decide to call Rae to let her know about the Club and to give her the address. She should start working here tomorrow."
        $ rae.dancing_at_club = True
    return

label rae_stage_call:
    # this runs when has tag 'showgirl' and you visit the Club
    if player.has_tag('stage_visited_today'):
        if rae.has_tag('on_stage_now'):
            $ rae.location = stage
    else:
        $ rae.location = stage
        add tags 'on_stage_now' to rae
    return

label rae_stage_send_home:
    call character_location_return(rae) from _call_character_location_return_15
    return

label rae_swingers_room_call:
    if rae.has_tag('girlfriend'):
        "You know better than to ask Rae to join you in the Swingers Room.  This is exactly the sort of place she would never go to."
        rem tags 'swingers_room_possible' from rae
    return

## Loving Wife Content
label rae_sarah_positive_role_talk_bimbo:
    if current_target.has_tag('bimbo') and not sarah.has_tag(tag_expression):
        wt_image store_clerk_lw_visit_1
        "You ask Rae to join you."
        rae.c "Yay! I like meeting your friends.  Do you think she'll like me?"
        wt_image lw_visit_2_2
        player.c "I'm sure she will, Rae.  This is Sarah."
        sarah.c "Hi.  Nice to meet you."
        wt_image store_clerk_lw_visit_8
        rae.c "Hiii!  Do you like me?  I like you."
        player.c "Rae, Sarah's not here to have sex with us, but her husband does wants her to have sex with his friends.  She has concerns.  I thought speaking to another woman could help her."
        wt_image store_clerk_lw_visit_1
        rae.c "Goodie!  Sex is fun!  Do you like to have sex?  What's your favorite part?  I think I like sucking cocks best, but I'm not very smart so I could be wrong."
        wt_image store_clerk_lw_visit_8
        rae.c "Do you like sucking cocks?  I bet your husband's friends would like it if you sucked their cocks.  Do you like me?  You probably don't have a cock, but I'll suck something else for you if you want?"
        ## remainder of transformed_bimbo content is back in sarah's script
        add tags 'transformed_bimbo_resolution_today' 'met_bimbo_rae' to sarah
    #elif current_target.has_tag('girlfriend') or current_target.has_tag('hypno_girlfriend'):
    #    "You could never explain to Rae why you want her to talk to Sarah about your love life. Better choose someone else."
    #    jump sarah_introduce_menu
    else:
        $ current_target = None
    return

label rae_sarah_positive_role_sex_bimbo:
    if current_target.has_tag('bimbo'):
        player.c "Rae, Sarah's here. Come join us."
        wt_image store_clerk_bimbo_2_7
        rae.c "Hiii!  Have we met?"
        player.c "You remember Sarah.  She's worried about having her husband watch her have sex."
        rae.c "Tee hee.  Silly!  You know I don't remember anything these days."
        player.c "Well, it's hard for Sarah to imagine what it would be like to have someone watch her have sex, in part because she's never even seen two people have sex together.  So you and I are going to have sex, while Sarah watches us."
        wt_image store_clerk_bimbo_2_15
        rae.c "Yay!  I'll take my clothes off!  We take clothes off for sex, don't we?"
        wt_image store_clerk_bimbo_2_16
        player.c "Yes, Rae. At least some of them."
        wt_image store_clerk_bimbo_2_21
        rae.c "Goodie!"
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image store_clerk_lw_visit_7
        rae.c "I took off all my clothes, so that I made sure to take off the right ones!"
        wt_image store_clerk_bimbo_2_11
        "Rae gets down on her knees and takes out your cock, then looks over at Sarah."
        rae.c "Am I supposed to be sucking his cock while you watch, or were you going to suck his cock while I watch?"
        wt_image lw_visit_4_4
        sarah.c "No, thank you!"
        wt_image store_clerk_bimbo_2_11
        rae.c "I don't mind if you want to do it.  I would have once, but I don't worry about those silly things any more.  We could suck it together, if you want?"
        rae.c "I mean, not together together.  There's only one cock and we each have one mouth.  But I could put it in your mouth and then you could put it in my mouth?"
        wt_image lw_visit_4_4
        sarah.c "Really, no."
        wt_image store_clerk_bimbo_2_26
        rae.c "Okay.  His cock is hard now, so we can ride it, instead.  He still only has one cock and I think we each have one pussy, so we'll probably need to take turns."
        wt_image lw_visit_4_8
        sarah.c "No thank you, and I'm leaving now.  I don't want to intrude on your personal time together."
        wt_image store_clerk_bimbo_2_27
        rae.c "Go? But you just got here. I do that all the time, too. Come when I'm supposed to go. Tee hee! Come when I'm supposed to go. That's funny! I hope I don't go when I'm supposed to cum. That would make a real mess!"
        $ rae.sex_count += 1
        orgasm
        ## rest of content is back in sarah's script
        add tags 'watched_transformed_bimbo_this_weekend' to sarah
    else:
        $ current_target = None
    return

label rae_sarah_positive_role_talk_girlfriend:
    sys "[rae.name] is designed to be an exclusive girlfriend, and no content was created to allow her to talk to Sarah about your relationship."
    $ current_target = None
    jump sarah_introduce_menu
    return


label rae_fluffy_cuff_reward:
    $ rae.fluffy_cuffs_reward_triggered = True
    wt_image phone_1
    "Sunday morning the phone rings."
    wt_image store_clerk_working_7
    rae.c "Hiii.  I've been thinking about how we could maybe spice up our sex life, and I've been looking around the store."
    rae.c "What do you think about a little role playing? I saw those cuffs you have stashed in the spare bedroom, and we have a sexy little squaw's outfit here in the store."
    rae.c "I know this is totally culturally inappropriate, but what if I dressed up as a squaw and came over to your place? You could be the cowboy and capture me and do anything you want with me."
    $ title = "What do you say?"
    menu:
        "Give me an hour":
            player.c "Give me an hour. And remember, once I capture you, I get to do anything I want with you."
            rae.c "Absolutely! Tie me up. Make me your little Indian sex slave. Oh ... should I say little Native American sex slave instead?"
            player.c "You won't get to say very much once I capture you, because I'm going to tie you up and gag you."
            rae.c "Ummm ... okay. But we'll still talk afterwards, right?"
            player.c "Maybe"
            wt_image living_room.image
            "The hour gives you more than enough time to pick out the toys you want and to put together a cheesy cowboy outfit."
            summon rae
            wt_image store_clerk_reward_4_1
            "Rae laughs when she sees you, but she shouldn't talk. The squaw's outfit she has on is silly, and yet sexy as hell."
            "You pull down her top as you pull her in for a kiss. She turns away, giving you only her cheek."
            rae.c "Wait.  I have to put the headdress on."
            wt_image store_clerk_reward_4_15
            "She puts on the headdress and pulls out a toy tomahawk. You're not sure if she's meant to be a squaw, a Chief, or a Warrior Princess."
            'Either way, she makes some silly "whooping" sounds and pretends to attack you.'
            wt_image store_clerk_reward_4_16
            "She came over to be captured, so that's exactly what you do."
            wt_image store_clerk_reward_4_2
            "Pinching and twisting her nipple you force her to her knees ..."
            wt_image store_clerk_reward_4_4
            "... and attach the cuffs to her wrists behind her back."
            wt_image store_clerk_reward_4_17
            "If you're going to go culturally inappropriate, you may as well go all the way."
            player.c "What were you planning on doing with this?  Were you planning on scalping me?"
            wt_image store_clerk_reward_4_18
            rae.c "No, no!  I swear! I wasn't going to hurt you. I just wanted to frighten you off my land."
            player.c "I think you were. I think you came here to raid me. Well, you're the one who's about to get plundered."
            wt_image store_clerk_reward_4_3
            "You start spanking her with the toy tomahawk ... *smack*  ... *smack*  ... *smack*"
            rae.c "Ouch!  No.  I wasn't.  Really.  Ouch!!  Ooowww!!"
            wt_image store_clerk_reward_4_18
            player.c "Did that hurt, my little Indian maiden?"
            rae.c "Yes.  A little."
            player.c "I don't think a big, rough cowboy would shy away from hurting a pretty squaw silly enough to come to his house and let herself get captured, would he?"
            rae.c "No"
            wt_image store_clerk_reward_4_5
            player.c "That's all I need to hear from you, my new Indian sex slave ... sorry, Native American sex slave."
            "You untie the scarf from around your neck and use it to gag Rae ..."
            wt_image store_clerk_reward_4_24
            "... then you pin her in place, keeping her from being able to move as you undress."
            wt_image store_clerk_reward_4_24
            "She's sopping wet ..."
            wt_image store_clerk_reward_4_19
            "... allowing you to slide into her easily."
            wt_image store_clerk_reward_4_7
            "She grimaces as you use her cuffed wrists as leverage, pulling her head and shoulders up as you fuck her."
            wt_image store_clerk_reward_4_26
            "With your weight on top of her she can't move. You use your grip on her wrists like reins, and starts bucking into her like she's a pony and you're ... well, a cowboy."
            $ title = "Where do you want to cum?"
            menu:
                "Inside her sex":
                    wt_image store_clerk_reward_4_8
                    "With a sharp slap on her ass, you release your seed inside her ... *SMACK*"
                    wt_image store_clerk_reward_4_7
                    rae.c "mmpphhh"
                "In her mouth":
                    wt_image store_clerk_reward_4_9
                    "Rolling her over and removing her gag, you feed your captured squaw your load."
                    wt_image store_clerk_reward_4_27
                    $ rae.swallow_count += 1
                "On her":
                    wt_image store_clerk_reward_4_20
                    "Rolling her over and removing her gag, you straddle her face. She suckles your balls as you launch your load over her."
                    wt_image store_clerk_reward_4_21
                    $ rae.facial_count += 1
            player.c "[player.orgasm_text]"
            wt_image store_clerk_reward_4_14
            rae.c "I hope you liked that. The cuffs are starting to hurt. Take them off now, please."
            $ title = "What do you do?"
            menu:
                "Uncuff her":
                    wt_image store_clerk_reward_4_22
                    player.c "That was great, Rae.  A lot of fun."
                    "You kiss her gently on the neck as you uncuff her."
                    rae.c "Oh good!  We've been going out a long time, now. I think it's important that we spice things up from time to time. I don't ever want you to get bored with me!!"
                "Leave her tied up until you're finished with her":
                    wt_image store_clerk_reward_4_5
                    player.c "I'm not done with you yet."
                    "You slip the gag back into her mouth."
                    $ title = "What now?"
                    menu:
                        "Make her suffer for a bit":
                            $ rae.strike_count += 2
                            wt_image store_clerk_reward_4_10
                            "You remove the cuffs and tie her on a bench, on her back, her beautiful big breasts facing up at you.  Then you proceed to cover her breasts with clothes pins."
                            "She groans into her gag as you fasten the last couple to her nipples."
                            rae.c "nnnnn"
                            wt_image store_clerk_reward_4_11
                            "You leave her like that as you go get yourself a drink, watching her tortured breasts rise and fall as she breathes deeply, trying to acclimatize to the pain."
                            wt_image store_clerk_reward_4_14
                            "When she's taken as much as you think she can, you let her go."
                            rae.c "Those clothes pins hurt!!"
                            player.c "You were my captive. Where's the fun in capturing you if I can't have fun with you after?"
                            rae.c "And you didn't untie me when I asked you to."
                            player.c "I don't let my captives go just because they ask. But I did take the cuffs off like you asked. I just tied you up with ropes instead."
                            rae.c "Well, let me go now or I won't be your captive or your girlfriend any more."
                            player.c "Are you mad at me?"
                            rae.c "Yes!  I don't like it when you hurt me."
                            sys "Rae's a lot less happy with your relationship."
                        "Make her suffer for a bit, then fuck her again":
                            $ rae.strike_count += 1
                            wt_image store_clerk_reward_4_10
                            "You remove the cuffs and tie her on a bench, on her back, her beautiful big breasts facing up at you.  Then you proceed to cover her breasts with clothes pins."
                            "She groans into her gag as you fasten the last couple to her nipples."
                            rae.c "nnnnn"
                            wt_image store_clerk_reward_4_11
                            "You leave her like that as you go get yourself a drink, watching her tortured breasts rise and fall as she breathes deeply, trying to acclimatize to the pain."
                            "When she's taken as much as you think she can, you start fucking her again."
                            rae.c "nnnnnn"
                            wt_image store_clerk_reward_4_10
                            "You remove the clothes pins to the sound of the cutest little yelps from Rae while you fuck her, squeezing her sore tits hard as you do."
                            rae.c "NNN ... NNN ... NNN"
                            wt_image store_clerk_reward_4_12
                            "Then her eyes glaze over, and she cums hard, screaming around the gag."
                            rae.c "MMMMMMMMMMM"
                            wt_image store_clerk_reward_4_23
                            player.c "[player.orgasm_text]"
                            wt_image store_clerk_reward_4_14
                            rae.c "Those clothes pins hurt!!"
                            player.c "You came like a banshee after I used them on you. The pain was worth it, admit it."
                            rae.c "And you didn't untie me when I asked you to."
                            player.c "You're my captive. I don't let my captives go just because they ask. But I did take the cuffs off like you asked. I just tied you up with ropes instead."
                            rae.c "Well, let me go now or I won't be your captive or your girlfriend any more."
                            player.c "Are you mad at me?"
                            rae.c "A little.  I don't like it when you hurt me."
                            player.c "Even though I know you'll get off on it?"
                            "She doesn't answer. She just dresses and leaves. You're not sure what bothers her more, that her boyfriend hurt her, or that she'd orgasmed from the experience."
                            sys "Rae's less happy with your relationship."
                            $ rae.orgasm_count += 1
                            $ rae.sex_count += 1
                            orgasm
                        "Fuck her again":
                            wt_image store_clerk_reward_4_23
                            "You remove the cuffs and retie her on a bench, on her back, her beautiful big breasts facing up at you.  Then you slip back inside her still wet pussy as she moans through her gag."
                            rae.c "nnnnn"
                            wt_image store_clerk_reward_4_12
                            "It doesn't take long before she shakes to orgasm."
                            rae.c "mmmmmmmmm ... MMMMMMM"
                            $ title = "Where do you want to cum this time?"
                            menu:
                                "In her pussy":
                                    wt_image store_clerk_reward_4_23
                                    player.c "[player.orgasm_text]"
                                "In her mouth":
                                    wt_image store_clerk_reward_4_13
                                    "Removing her gag, you replace it with your cock and your hot load."
                                    player.c "[player.orgasm_text]"
                                    $ rae.swallow_count += 1
                            wt_image store_clerk_reward_4_14
                            rae.c "Wow, that was incredible!  I love you!!"
                            rae.c "Shit.  Did I just say that out loud?"
                            $ rae.orgasm_count += 1
                            $ rae.sex_count += 1
                            $ player.desire_action_count += 1
                            $ rae.maintain_week_gf += 1
                            if rae.strike_count > 0:
                                $ rae.strike_count -= 1
                                sys "Rae's gotten over some reservations she had about your relationship."
                            orgasm
            $ rae.sex_count += 1
            orgasm notify
            call character_location_return(rae) from _call_character_location_return_16
        "No way":
            player.c "You're right, Rae. That is completely culturally inappropriate and I want no part of it."
            rae.c "Oh. Sorry. I didn't mean to offend anybody. It was just a silly idea. Forget I suggested it."
    wt_image living_room.image
    return

label rae_dildo_reward:
    $ rae.dildo_reward_triggered = True
    wt_image front_door
    "Sunday morning there's a knock on your door."
    summon rae
    wt_image store_clerk_reward_6_1
    rae.c "Hiii.  I've been trying to think of something new and special to do for you."
    player.c "So you decided to wear your shortest shorts?"
    rae.c "Yes, because you need to be turned on for this to work."
    player.c "For what to work?"
    wt_image store_clerk_reward_6_2
    rae.c "Sit down, and I'll show you."
    wt_image store_clerk_reward_6_3
    rae.c "Are you hard?  This only works when you're hard."
    player.c "With you in those shorts?  Very.  And what will only work?"
    wt_image store_clerk_reward_6_4
    rae.c "The gift I bought you. I was thinking about the sex toy you bought me, and I thought maybe you'd like one, too."
    player.c "A vibrator.  No thanks."
    wt_image store_clerk_reward_6_5
    rae.c "Not a vibrator, silly. A fleshlight. It's a toy for boys. We've been selling a ton of them at the store."
    player.c "Keep stroking me like that, and I won't need anything other than your hand."
    wt_image store_clerk_reward_6_6
    rae.c "Then I guess you're ready for your gift."
    wt_image store_clerk_reward_6_7
    "Rae produces the sex toy ..."
    wt_image store_clerk_reward_6_8
    "... and slides it over your hard shaft."
    wt_image store_clerk_reward_6_9
    "Then she starts pumping it up and down."
    wt_image store_clerk_reward_6_10
    rae.c "Is it working?"
    player.c "Yes.  Keep going."
    wt_image store_clerk_reward_6_11
    rae.c "Are you going to be able to cum like this?"
    $ title = "What do you tell her?"
    menu:
        "Yes, keep going.":
            wt_image store_clerk_reward_6_9
            "Just a couple of more strokes ..."
            wt_image store_clerk_reward_6_7
            "... up ..."
            wt_image store_clerk_reward_6_8
            "... and down ..."
            wt_image store_clerk_reward_6_9
            "... and ..."
            wt_image store_clerk_reward_6_8
            player.c "[player.orgasm_text]"
            wt_image store_clerk_reward_6_16
            rae.c "Oh, wow!!  That really worked!"
            wt_image store_clerk_reward_6_17
            rae.c "I'd better clean up this mess."
            wt_image store_clerk_reward_6_18
            "She licks you completely clean, an experience as enjoyable as the sex toy."
        "No, take your top off":
            wt_image store_clerk_reward_6_19
            rae.c "Is this better?"
            player.c "You topless is always better."
            wt_image store_clerk_reward_6_20
            rae.c "Are you going to be able to cum now?"
            $ title = "What do you tell her?"
            menu:
                "Take a look and see":
                    wt_image store_clerk_reward_6_23
                    "Rae removes the toy just as you release your load."
                    player.c "[player.orgasm_text]"
                    wt_image store_clerk_reward_6_24
                    rae.c "Oh, wow!!  This thing really worked!"
                    wt_image store_clerk_reward_6_25
                    rae.c "I'm going to have to recommend these to all our store customers."
                    $ rae.facial_count += 1
                "No, I need your mouth on me":
                    wt_image store_clerk_reward_6_7
                    "Rae removes the toy ..."
                    wt_image store_clerk_reward_6_21
                    "... and replaces it with her mouth."
                    wt_image store_clerk_reward_6_22
                    player.c "[player.orgasm_text]"
                    wt_image store_clerk_reward_6_15
                    rae.c "It's too bad the toy didn't work better, but I'm glad my mouth can still get you off."
                    $ rae.blowjob_count += 1
                    $ rae.swallow_count += 1
        "No, I need your mouth on me":
            wt_image store_clerk_reward_6_7
            "Rae removes the toy."
            wt_image store_clerk_reward_6_12
            rae.c "That's too bad ..."
            wt_image store_clerk_reward_6_13
            rae.c "... I was hoping it would feel good enough to get you off."
            wt_image store_clerk_reward_6_14
            player.c "[player.orgasm_text]"
            wt_image store_clerk_reward_6_15
            rae.c "I'm glad my mouth can still get you off."
            $ rae.swallow_count += 1
            $ rae.blowjob_count += 1
    wt_image store_clerk_reward_6_1
    rae.c "I know it's not easy for a guy like you, only being with one woman."
    rae.c "I want you to know that as long as we're together, I will never stop looking for new ways to please you and keep our relationship fresh."
    wt_image living_room.image
    "With that, she's gone, and you can go on with your day."
    orgasm notify
    call character_location_return(rae) from _call_character_location_return_17
    return

## Store Content
label rae_es_store_enter:
    if rae.has_tag('exclusive_girlfriend') and rae.has_tag('girlfriend'):
        "You time your visits to the store for when Rae isn't working.  Otherwise, she'd get suspicious."
    elif rae.has_tag('working_at_store') and not rae.has_tag('trained_this_week'):
        $ rae.location = eros_store
        rem tags 'follows' from rae
        "There's no one in the store except you and [rae.full_name]."
        if rae.has_tag('talked'):
            rem tags 'no_hypnosis' from rae
    elif rae.has_tag('working_at_store'):
        "Rae doesn't appear to be working in the store right now."
    elif not rae.has_tag('working_at_store') and not rae.has_tag('no_longer_working_message'):
        add tags 'no_longer_working_message' to rae
        "[rae.name] no longer works here."
    return

label rae_es_store_exit:
    if rae.location == eros_store:
        add tags 'no_hypnosis' to rae
        call character_location_return(rae) from _call_character_location_return_18
    return


## Character Specific Timers
# Custom Slaver Trade Dialogue
label rae_slaver_trade_custom:
    if current_target.has_tag('girlfriend') or current_target.has_tag('hypno_girlfriend'):
        wt_image store_clerk_working_7
        player.c "Rae, how about I pick you up and we go do some shopping together at the mall?"
        rae.c "Like a shopping date?"
        player.c "Exactly.  I'll pick you up after you finish work."
        $ samantha.temporary_count = 1
    else:
        # use standard content if not GF or hypno-GF
        $ samantha.temporary_count = 3
    return

# Convert to Girlfriend
label rae_convert_girlfriend:
    if not rae.has_tag('hypno_girlfriend'):
        call convert(rae,"girlfriend") from _call_convert_40
        $ rae.maintain_week_gf = week + 4
        $ rae.girlfriend_reward_week = week + 2
    $ rae.training_regime = 'daily'
    add 1 photos_of_rae to bedroom
    rem tags 'flirting' 'follows' from rae
    add tags 'no_hypnosis' to rae ## notes that she won't accept other relationships; other GFs with same restriction should get same tag
    add tags 'rae_photos_received' to player
    return

# Lose Girlfriend
label rae_lose_girlfriend_status:
    if rae.has_tag('girlfriend'):
        call unconvert(rae,'girlfriend') from _call_unconvert_44
    if rae.has_tag('hypno_girlfriend'):
        call unconvert(rae,'hypno_girlfriend') from _call_unconvert_45
    if not rae.has_tag('bimbo') and not rae.has_tag('showgirl') and not rae.has_tag('waiting_for_club_access'):
        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
        call convert(rae, "unavailable") from _call_convert_41
    rem tags 'on_date' 'follows' from rae
    rem 1 photos_of_rae from bedroom
    return

# Convert to Bimbo
label rae_convert_bimbo:
    call convert(rae,"bimbo") from _call_convert_44
    $ rae.training_regime = 'daily'
    rem tags 'flirting' 'working_at_store' 'follows' from rae
    add tags 'no_hypnosis' to rae
    $ rae.change_image('store_clerk_bimbo_1_5')
    $ rae.location = bedroom
    call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_4
    $ rae.fixed_location = bedroom # must be after unconvert call
    return

# Convert to Showgirl
label rae_convert_showgirl:
    $ rae.training_regime = 'daily'
    if player.has_tag('club_access') and player.has_tag('club_first_visit_complete'):
        $ rae.dancing_at_club = True
        call convert(rae, "showgirl") from _call_convert_45
    else:
        add tags 'waiting_for_club_access' to rae
    rem tags 'flirting' 'working_at_store' from rae
    add tags 'no_hypnosis' to rae
    call rae_lose_girlfriend_status from _call_rae_lose_girlfriend_status_5
    return

########### ROOMS ###########


########### ITEMS ###########
## Common Item Actions
# Examine Character
label por_examine:
    call rae_review_files_selfies from _call_rae_review_files_selfies
    #"Photos your girlfriend Rae has sent to you."
    return

label rae_relationship_status:
    if rae.has_tag('girlfriend'):
        if current_location == bedroom:
            wt_image store_clerk_date_2_9
        $ rae.temporary_count = rae.maintain_week_gf - week
        if rae.temporary_count > 2:
            if rae.strike_count > 1:
                "Rae has serious doubts about your relationship and whether you're the right boyfriend for her."
            else:
                "Rae is happy with your relationship."
        elif rae.temporary_count > 0:
            if rae.strike_count > 1:
                "Rae wishes you would spend more time with her doing things you both enjoy.  She also has serious doubts about your relationship and whether you're the right boyfriend for her."
            else:
                "Rae wishes you would spend more time with her doing things you both enjoy."
        elif rae.has_tag('love_potion_used'):
            "Rae feels like she never gets to spend enough time with you, but the lingering effects of the love potion make it impossible for her to contemplate leaving you."
        elif rae.temporary_count > -2:
            "Rae's unhappy with your lack of attention and is considering leaving you."
        else:
            "Rae feels ignored and plans to leave you unless you do something with her soon."
        $ rae.temporary_count = 0
    elif rae.has_tag('hypno_girlfriend'):
        if current_location == bedroom:
            wt_image store_clerk_date_1_19
        if rae.strike_count > 1:
            "Rae has serious doubts about your relationship and whether you're the right boyfriend for her. Even hypnotized, she has standards you're falling short of."
        else:
            "You've convinced her she's your girlfriend.  As you long as you invest energy each week on maintaining that belief and don't do anything too contrary to her view of how a boyfriend should treat her, she'll continue to believe you."
    wt_image current_location.image
    return

################################### NOTES ###################################
##################### TODO #####################
# Check How rae.action_view_selfies is activated
# Check if Item Album is needed

## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
