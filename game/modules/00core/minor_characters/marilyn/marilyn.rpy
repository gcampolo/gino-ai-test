## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package marilyn name "Marilyn" description "Allows Marilyn to be a minor character." dependencies core
register marilyn_pregame 10 in core as "Marilyn"

# Pregame
label marilyn_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Marilyn (Monique Alexander)")]

    ## Character Definition
    marilyn = Person(Character("Unknown Woman", who_color="#800000", what_color="#800000", window_background = gui.dialogue_background_dark_font_color), "marilyn", cut_portrait = True, prefix = "", suffix = "")

    # Other Characters
    # Navy
    guard_marilyn = Character("Marilyn's Security Guard", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    marilyn.action_talk = marilyn.add_action("Talk to her", label="_talk", condition = "marilyn.can_be_interacted")

    ## Tags
    # Common Character Tags
    marilyn.add_tags('can_be_in_club', 'no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # Marilyn's Building
    marilyn_building = Location("Marilyn's Building", 'mb', cut_portrait = True, enter_break_labels = ['mb_no_access'], enter_labels = ['mb_enter'], exit_labels = ['mb_exit'], area = 'downtown')
    marilyn.location = marilyn_building
    marilyn.fixed_location = marilyn_building

    ## Other
    marilyn.change_status("minor_character")

    # Start Day Events
    #start_day_labels.append('marilyn_start_day') # not needed

    ########### VARIABLES ###########
    # Common Character Variables
    # marilyn.add_stats_with_value('temporary_count') # not needed as auto-added to all characters
    marilyn.add_stats_with_value('random_number')

    # Character Specific Variables
    marilyn.add_stats_with_value('contact_art_countdown', 'discuss_barista', 'favour', 'frigid_encounter_status', 'fuck_chance', 'independent_encounter_status', 'rewards_pending', 'rewards_given', 'whore_cut_percentage')
    player.add_stats_with_value('marilyn_building_visit_count')
    marilyn_reward_description_list = ['club_access', 'transformation_potion', 'ring_sexuality', 'janice_trigger']
    marilyn_special_reward_description_list = ['will_tamer']
    marilyn_iou_pick_up_list = ['transformation_potion', 'ring_sexuality', 'will_tamer']

    #Player Examine Phrases
    player.add_examine_phrase("marilyn.favour > 0", "Marilyn owes you a favor.", "marilyn.favour > 1", "Marilyn owes you [marilyn.favour.to_s] favors.")

    ######## EXPANDABLE MENUS #######
    ## Reward People
    marilyn_whose_reward_menu = ExpandableMenu("Whose reward do you want to collect?")
    marilyn.choice_marilyn_whose_reward_menu_dee = marilyn_whose_reward_menu.add_choice("Dee", "marilyn_whose_reward_menu_dee", condition = "marilyn.has_tag('dee_reward_pending')")
    marilyn.choice_marilyn_whose_reward_menu_elsa = marilyn_whose_reward_menu.add_choice("Elsa", "marilyn_whose_reward_menu_elsa", condition = "marilyn.has_tag('elsa_reward_pending')")
    marilyn.choice_marilyn_whose_reward_menu_elsa = marilyn_whose_reward_menu.add_choice("Terri", "marilyn_whose_reward_menu_terri", condition = "marilyn.has_tag('terri_reward_pending')")
    marilyn.choice_marilyn_whose_reward_menu_becky_sue = marilyn_whose_reward_menu.add_choice("Becky Sue", "marilyn_whose_reward_menu_becky_sue", condition = "marilyn.has_tag('becky_sue_reward_pending')")

    ## Reward Options
    marilyn_reward_menu = ExpandableMenu("Which reward do you choose?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game
    marilyn.choice_marilyn_reward_menu_club_access = marilyn_reward_menu.add_choice("Club Access", "marilyn_reward_menu_club_access", condition = "not player.has_tag('club_access')")
    marilyn.choice_marilyn_reward_menu_Janice_trigger = marilyn_reward_menu.add_choice("Janice's Trigger", "marilyn_reward_menu_janice_trigger", condition = "janice.tried_hypnosis == 2")
    marilyn.choice_marilyn_reward_menu_transformation_potion = marilyn_reward_menu.add_choice("Transformation Potion", "marilyn_reward_menu_transformation_potion", condition = "not marilyn.has_tag('transformation_potion_granted') and not marilyn.has_tag('iou_transformation_potion_pending')")
    marilyn.choice_marilyn_reward_menu_ring_sexuality = marilyn_reward_menu.add_choice("Ring of Sexuality", "marilyn_reward_menu_ring_sexuality", condition = "not marilyn.has_tag('ring_sexuality_granted') and not marilyn.has_tag('iou_ring_sexuality_pending')")
    marilyn.choice_marilyn_reward_menu_will_tamer = marilyn_reward_menu.add_choice("Will-Tamer", "marilyn_reward_menu_will_tamer", condition = "marilyn.has_tag('special_reward') and not marilyn.has_tag('will_tamer_granted') and not marilyn.has_tag('iou_will_tamer_pending')")
    marilyn.choice_marilyn_reward_menu_her = marilyn_reward_menu.add_choice("Her", "marilyn_reward_menu_her")
    marilyn.choice_marilyn_reward_menu_iou = marilyn_reward_menu.add_choice("Take an IOU", "marilyn_reward_menu_iou")
    ## IOU Options
    marilyn_iou_menu = ExpandableMenu("Do you want to call your IOU in for something?")
    marilyn.choice_marilyn_iou_menu_club_access = marilyn_iou_menu.add_choice("Club Access", "marilyn_iou_menu_club_access", condition = "marilyn.has_tag('club_access_offered') and not player.has_tag('club_access')")
    marilyn.choice_marilyn_iou_menu_janice_retainer = marilyn_iou_menu.add_choice("Janice's Services", "marilyn_iou_menu_janice_retainer", condition = "janice.has_tag('asked_about_hiring') and not player.has_tag('lawyer_on_retainer')")
    marilyn.choice_marilyn_iou_menu_janice_trigger = marilyn_iou_menu.add_choice("Janice's Trigger", "marilyn_iou_menu_janice_trigger", condition = "janice.tried_hypnosis == 2")
    marilyn.choice_marilyn_iou_menu_transformation_potion = marilyn_iou_menu.add_choice("Transformation Potion", "marilyn_iou_menu_transformation_potion", condition = "marilyn.has_tag('transformation_potion_offered') and not marilyn.has_tag('transformation_potion_granted') and not marilyn.has_tag('iou_transformation_potion_pending')")
    marilyn.choice_marilyn_iou_menu_ring_sexuality = marilyn_iou_menu.add_choice("Ring of Sexuality", "marilyn_iou_menu_ring_sexuality", condition = "not marilyn.has_tag('ring_sexuality_granted') and not marilyn.has_tag('iou_ring_sexuality_pending')")
    marilyn.choice_marilyn_iou_menu_will_tamer = marilyn_iou_menu.add_choice("Will-Tamer", "marilyn_iou_menu_will_tamer", condition = "marilyn.has_tag('will_tamer_offered') and not marilyn.has_tag('will_tamer_granted') and not marilyn.has_tag('iou_will_tamer_pending')")
    marilyn.choice_marilyn_iou_menu_whore_cut = marilyn_iou_menu.add_choice("Re-negotiate her cut", "marilyn_iou_menu_whore_cut", condition = "player.has_tag('marilyn_whore_cut') and not marilyn.has_tag('whore_cut_reduced')")
    marilyn.choice_marilyn_iou_menu_rep_gain = marilyn_iou_menu.add_choice("Ask for a Reputation boost", "marilyn_iou_menu_rep_gain", condition = "not player.has_tag('rep_from_marilyn')")

  return

# Display Portrait
# CHARACTER: Display Portrait
label marilyn_update_media:
    if current_location == club:
        $ marilyn.change_image('marilyn_club_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label marilyn_examine:
    if current_location == club:
        "The well dressed woman surveys the Club, two bodyguards trailing her at a discrete distance."
    #"[marilyn.statblock]"
    #$ items = ", ".join(i.name for i in marilyn.get_items()) if marilyn.get_items() != [] else ' Nothing'
    #"You have given her: [items]"
    return

# Talk to Character
label marilyn_talk:
    if current_location == club:
        wt_image marilyn_club_1
        # have you visited her?
        if player.marilyn_building_visit_count == 0:
            marilyn.c "Do they let anyone into the Club now?"
            wt_image marilyn_security_1
            "One of her bodyguards inserts himself between you and the woman.  This conversation is over."
            rem tags 'in_club_now' from marilyn
            call character_location_return(marilyn) from _call_character_location_return_622
            wt_image current_location.image
        # did you bring her somebody?
        elif marilyn.rewards_given > 0:
            # has she had an orgasm with you or let you dominate her? currently this requires bringing her Terri and then choosing "her" as your reward
            if marilyn.orgasm_count > 0 or marilyn.has_tag('dominated_her'):
                # if she didn't want to have sex with you at the Club previously, lower the count down timer
                if marilyn.fuck_chance > 1:
                    $ marilyn.fuck_chance -= 1
                # if the count down timer is at zero, reset it
                elif marilyn.fuck_chance == 0:
                    $ marilyn.random_number = renpy.random.randint(1, 10)
                    if marilyn.random_number > 7:
                        $ marilyn.fuck_chance = 1
                    elif marilyn.random_number > 4:
                        $ marilyn.fuck_chance = 2
                    else:
                        $ marilyn.fuck_chance = 3
            # if fuck chance timer reaches 1, Marilyn offers to have sex with you; note that it never starts if you didn't previously please her
            if marilyn.fuck_chance == 1:
                $ marilyn.fuck_chance = 0
                wt_image marilyn_club_2
                "Marilyn smiles as she sees you approach."
                marilyn.c "My staff have disappointed me.  Not one single interesting prospect for my bed this evening.  So I've decided I'm going to let you fuck me again."
                "Her tone makes it clear she doesn't intend this as a request, but as a demand.  Still, if you have something better to do, you could try putting her off."
                $ title = "What do you do?"
                menu:
                    "Accept":
                        call marilyn_club_sex from _call_marilyn_club_sex
                    "Decline":
                        player.c "I'm sorry, Marilyn, but I have other matters I must attend to today."
                        "There's a flash of anger in her eyes."
                        if player.has_tag('dominant'):
                            wt_image marilyn_club_25
                            "Then she leans in close, and whispers in your ear."
                            marilyn.c "Please accept my body.  I promise to be obedient."
                        elif player.has_tag('supersexy'):
                            wt_image marilyn_club_25
                            "Then her face softens, slightly."
                            marilyn.c "Okay, you made your point.  You don't have trouble getting women to spread their legs for you."
                            marilyn.c "I'm not just any woman, though.  I'm not used to hearing 'no'.  But you aren't on my staff and if you don't want to sleep with me, it's not like that's going to ruin my day."
                            marilyn.c "On the other hand, if you say 'yes', I'll do everything I can to make your day."
                        if player.has_tag('dominant') or player.has_tag('supersexy'):
                            $ title = "Change your mind?"
                            menu:
                                "Yes, accept her offer of sex":
                                    player.c "Well, since you're asking nicely."
                                    call marilyn_club_sex from _call_marilyn_club_sex_1
                                "No":
                                    player.c "An extremely tempting offer I would be pleased to accept on another day.  But today, I truly do have something important I must attend to."
                                    wt_image marilyn_club_1
                                    marilyn.c "Hmmpphh"
                                    "She's annoyed, but respects your decision."
                                    rem tags 'in_club_now' from marilyn
                                    call character_location_return(marilyn) from _call_character_location_return_623
                                    wt_image current_location.image
                        else:
                            marilyn.c "That offer may not be extended again."
                            rem tags 'in_club_now' from marilyn
                            call character_location_return(marilyn) from _call_character_location_return_624
                            wt_image current_location.image
            elif marilyn.fuck_chance == 0:
                marilyn.c "Please don't bother me.  If you find someone new for me, give me a call.  Until then - ta ta."
                if marilyn.sex_count > 0 and marilyn.favour > 0:
                    $ title = "Try to cash in an IOU for sex?"
                    menu:
                        "Yes":
                            player.c "I'd like to sleep with you again.  How about I trade in an IOU for some time with you in a back room."
                            wt_image marilyn_club_2
                            $ marilyn.random_number = renpy.random.randint(1, 10)
                            if marilyn.random_number > 7:
                                marilyn.c "Bold, and marginally flattering that you'd consider another romp as equal payment for the IOU.  As it happens, my staff have disappointed me.  Not one single interesting prospect for my bed this evening.  I suppose I can give you another opportunity.  Follow me."
                                $ marilyn.favour -= 1
                                call marilyn_club_sex from _call_marilyn_club_sex_2
                            else:
                                marilyn.c "Bold, and marginally flattering that you'd consider another romp as equal payment for the IOU.  But my staff have already located a bed warmer for me for this evening."
                                wt_image marilyn_security_1
                                "One of her bodyguards inserts himself between you and Marilyn.  This conversation is over."
                                rem tags 'in_club_now' from marilyn
                                call character_location_return(marilyn) from _call_character_location_return_625
                                wt_image current_location.image
                        "No":
                            wt_image marilyn_security_1
                            "One of her bodyguards inserts himself between you and Marilyn.  This conversation is over."
                            rem tags 'in_club_now' from marilyn
                            call character_location_return(marilyn) from _call_character_location_return_626
                            wt_image current_location.image
            else:
                marilyn.c "Please don't bother me.  My staff have me well looked after for this evening so I don't require your presence.  If you find someone new for me, give me a call.  Until then - ta ta."
                wt_image marilyn_security_1
                "One of her bodyguards inserts himself between you and Marilyn.  This conversation is over."
                rem tags 'in_club_now' from marilyn
                call character_location_return(marilyn) from _call_character_location_return_627
                wt_image current_location.image
        else:
            marilyn.c "If you find someone of interest, call me. Until then, don't presume I'll let you be seen in my presence in public."
            wt_image marilyn_security_1
            "One of her bodyguards inserts himself between you and Marilyn.  This conversation is over."
            rem tags 'in_club_now' from marilyn
            call character_location_return(marilyn) from _call_character_location_return_628
            wt_image current_location.image
    return

label marilyn_club_sex:
  if player.has_tag('dominant') and marilyn.has_tag('dominated_her'):
    wt_image marilyn_club_3
    "Marilyn leads you to one of the Club's private rooms.  You close the door behind you and sit down.  Marilyn undresses quietly, waiting to see if you'll take the lead."
    player.c "Turn around and lean over as you remove your dress."
    wt_image marilyn_club_21
    "Silently she obeys, wiggling her hips a little more than is strictly necessary to remove the dress.  She seems to enjoy letting you take control."
    wt_image marilyn_club_22
    player.c "Stay like that."
    "You leave her bent over for a few minutes as you examine her ass.  When you run a finger along her sex, you're pleased to feel the dampness already soaking through her panties."
    player.c "Stand up and show me your tits."
    wt_image marilyn_club_31
    player.c "Eyes down.  I didn't say you could make eye contact."
    wt_image marilyn_club_23
    "She keeps her eyes on the floor as she holds her breasts up for your inspection."
    player.c "Remove your panties and get on down on all fours, on the bed."
    wt_image marilyn_club_32
    "You can smell her arousal as she gets into position."
    wt_image marilyn_club_6
    "She gasps as you push yourself roughly inside her ..."
    marilyn.c "ohhh"
    wt_image marilyn_club_7
    "... then gasps again when you shove your thumb in her ass, but doesn't object."
    wt_image marilyn_club_27
    $ title = "What do you want to do?"
    menu:
      "Take her anally":
        wt_image marilyn_club_9
        "To Marilyn's surprise, you pull out of her."
        wt_image marilyn_club_28
        "As you guide her up on top of you, she tries to positions her pussy on your cock."
        player.c "Not like that."
        "You move her forward slightly, until the head of your cock is pressing against her rosebud. She groans as you pull her hips down, her ass stretching to accept you inside her."
        wt_image marilyn_club_10
        marilyn.c "ohhhh"
        player.c "Put your finger in your cunt and finger fuck yourself while I fuck your ass."
        wt_image marilyn_club_30
        marilyn.c "Don't cum inside me. I hate the feeling of semen back there."
        wt_image marilyn_club_24
        "Those instructions passed on, she begins to finger fuck herself as instructed.  It's not long before she orgasms with your cock in her butt."
        marilyn.c "Oohhhhhh"
        $ title = "What do you do?"
        menu:
          "Finish inside her anyway":
            call marilyn_finish_inside from _call_marilyn_finish_inside
          "Pull out":
            wt_image marilyn_club_10
            "After she cums, you continue to fuck her ass until you're ready for your own orgasm."
            wt_image marilyn_club_12
            "You pull out and move her head to your cock.  She offers no objection, taking you fully into her mouth despite where your cock just was.  You soon fill her mouth with your load."
            player.c "[player.orgasm_text]"
            $ marilyn.swallow_count += 1
        $ marilyn.anal_count += 1
        $ marilyn.orgasm_count += 1
      "Finish in her mouth":
        wt_image marilyn_club_8
        "Even without any stimulation on her clit, the combination of your cock in her pussy and your thumb in her ass takes Marilyn over the edge.  It would have been nice to have her ask permission to cum, but you get the sense that would be pushing things too far."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_9
        "When you're ready to cum, you pull out of her and guide her head to your cock."
        wt_image marilyn_club_12
        "A moment later, you fill her mouth with your cum."
        player.c "[player.orgasm_text]"
        $ marilyn.swallow_count += 1
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
      "Finish like this":
        wt_image marilyn_club_8
        "This time, even without any stimulation on her clit, the combination of your cock in her pussy and your thumb in her ass takes Marilyn over the edge. It would have been nice to have her ask permission to cum, but she isn't there yet."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_27
        "You finish shortly after her."
        player.c "[player.orgasm_text]"
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
    wt_image marilyn_club_3
    marilyn.c "Mmmmm.  You're surprisingly fun.  Ta ta!"
    call character_location_return(marilyn) from _call_character_location_return_629
    wt_image current_location.image
    rem tags 'in_club_now' from marilyn
    orgasm notify
  elif player.has_tag('supersexy'):
    wt_image marilyn_club_3
    "Marilyn leads you to one of the Club's private rooms.  With a smile, she slips out of her dress."
    wt_image marilyn_club_4
    marilyn.c "Be a doll and help me with this?"
    "You're happy to oblige."
    wt_image marilyn_club_5
    marilyn.c "Thank you.  That's better."
    "As she drops the bra, you agree."
    wt_image marilyn_club_33
    marilyn.c "Mmmmm.  Just looking at you makes my nipples hard, and feeling your tongue on them is even better."
    wt_image marilyn_club_26
    marilyn.c "Get up here and mount me, sexy."
    wt_image marilyn_club_6
    "As you do, she gasps in pleasure."
    marilyn.c "ohhh"
    wt_image marilyn_club_7
    "She gasps again when you shove your thumb in her ass, but doesn't object."
    wt_image marilyn_club_27
    $ title = "What do you want to do?"
    menu:
      "Take her anally":
        wt_image marilyn_club_9
        "To Marilyn's surprise, you pull out of her."
        wt_image marilyn_club_28
        "As you guide her up on top of you, she tries to positions her pussy on your cock."
        player.c "Not like that."
        "You move her forward slightly, until the head of your cock is pressing against her rosebud. She groans as you pull her hips down, her ass stretching to accept you inside her."
        wt_image marilyn_club_10
        marilyn.c "ohhhh"
        wt_image marilyn_club_29
        "You start to strum her clit with her fingers, and you can feel her pleasure building, even though she's still tense."
        marilyn.c "Don't cum inside me.  I hate the feeling of semen back there."
        wt_image marilyn_club_11
        "Those instructions passed on, she relaxes and soon orgasms as you fuck her ass."
        marilyn.c "Oohhhhhh"
        $ title = "What do you do?"
        menu:
          "Finish inside her anyway":
            call marilyn_finish_inside from _call_marilyn_finish_inside_1
          "Pull out":
            wt_image marilyn_club_10
            "After she cums, you continue to fuck her ass until you're ready for your own orgasm."
            wt_image marilyn_club_12
            "You pull out, and to your surprise, she takes you fully into her mouth, seemingly unconcerned about where your cock just was.  You soon fill her mouth with your load."
            player.c "[player.orgasm_text]"
            $ marilyn.swallow_count += 1
        $ marilyn.anal_count += 1
        $ marilyn.orgasm_count += 1
      "Finish in her mouth":
        wt_image marilyn_club_8
        "Between your cock in her pussy and your thumb in her ass, it doesn't take Marilyn long to cum."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_9
        "When her orgasm subsides, she offers no objection as you pull out of her and guide her head to your cock."
        wt_image marilyn_club_12
        "A moment later, you fill her mouth with your cum."
        player.c "[player.orgasm_text]"
        $ marilyn.swallow_count += 1
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
      "Finish like this":
        wt_image marilyn_club_8
        "Between your cock in her pussy and your thumb in her ass, it doesn't take Marilyn long to cum."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_27
        "You finish shortly after her."
        player.c "[player.orgasm_text]"
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
    wt_image marilyn_club_3
    marilyn.c "Mmmmm.  No wonder housewives line up to spread their legs for you.  If you weren't potentially more valuable to me in your current line of work, I'd turn you into a whore and pimp you out.  Ta ta!"
    call character_location_return(marilyn) from _call_character_location_return_630
    wt_image current_location.image
    rem tags 'in_club_now' from marilyn
    orgasm notify
  elif marilyn.orgasm_count > 0:
    wt_image marilyn_club_3
    "Marilyn leads you to one of the Club's private rooms.  With a smile, she slips out of her dress."
    wt_image marilyn_club_4
    marilyn.c "Be a doll and help me with this?"
    "You're happy to oblige."
    wt_image marilyn_club_5
    marilyn.c "Thank you.  That's better."
    "As she drops the bra, you agree."
    wt_image marilyn_club_33
    marilyn.c "Mmmmm.  Your tongue on my nipples feels nice."
    wt_image marilyn_club_26
    marilyn.c "I guess I'll let you mount me now."
    wt_image marilyn_club_6
    "As you do, she gasps in pleasure."
    marilyn.c "ohhh"
    wt_image marilyn_club_7
    "She gasps again when you shove your thumb in her ass, but doesn't object."
    wt_image marilyn_club_27
    $ title = "What do you want to do?"
    menu:
      "Take her anally":
        wt_image marilyn_club_9
        "To Marilyn's surprise, you pull out of her."
        wt_image marilyn_club_28
        "As you guide her up on top of you, she tries to positions her pussy on your cock."
        player.c "Not like that."
        "You move her forward slightly, until the head of your cock is pressing against her rosebud. She groans as you pull her hips down, her ass stretching to accept you inside her."
        wt_image marilyn_club_10
        marilyn.c "ohhhh"
        wt_image marilyn_club_29
        "You start to strum her clit with her fingers, and you can feel her pleasure building, even though she's still tense."
        marilyn.c "Don't cum inside me.  I hate the feeling of semen back there."
        wt_image marilyn_club_11
        "Those instructions passed on, she relaxes and soon orgasms as you fuck her ass."
        marilyn.c "Oohhhhhh"
        $ title = "What do you do?"
        menu:
          "Finish inside her anyway":
            call marilyn_finish_inside from _call_marilyn_finish_inside_2
          "Pull out":
            wt_image marilyn_club_10
            "After she cums, you continue to fuck her ass until you're ready for your own orgasm."
            wt_image marilyn_club_12
            "You pull out, and to your surprise, she takes you fully into her mouth, seemingly unconcerned about where your cock just was.  You soon fill her mouth with your load."
            player.c "[player.orgasm_text]"
            $ marilyn.swallow_count += 1
        $ marilyn.anal_count += 1
        $ marilyn.orgasm_count += 1
      "Finish in her mouth":
        wt_image marilyn_club_8
        "Between your cock in her pussy and your thumb in her ass, it doesn't take Marilyn long to cum."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_9
        "When her orgasm subsides, she offers no objection as you pull out of her and guide her head to your cock."
        wt_image marilyn_club_12
        "A moment later, you fill her mouth with your cum."
        player.c "[player.orgasm_text]"
        $ marilyn.swallow_count += 1
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
      "Finish like this":
        wt_image marilyn_club_8
        "Between your cock in her pussy and your thumb in her ass, it doesn't take Marilyn long to cum."
        wt_image marilyn_club_7
        marilyn.c "Oohhhhhh"
        wt_image marilyn_club_27
        "You finish shortly after her."
        player.c "[player.orgasm_text]"
        $ marilyn.sex_count += 1
        $ marilyn.orgasm_count += 1
    wt_image marilyn_club_3
    marilyn.c "Not the best I've ever had, but not the worst, either.  Ta ta!"
    call character_location_return(marilyn) from _call_character_location_return_631
    wt_image current_location.image
    rem tags 'in_club_now' from marilyn
    orgasm notify
  else:
    wt_image marilyn_club_3
    "Marilyn leads you to one of the Club's private rooms.  With a smile, she slips out of her dress."
    wt_image marilyn_club_4
    marilyn.c "Be a doll and help me with this?"
    "You're happy to oblige."
    wt_image marilyn_club_5
    marilyn.c "Thank you.  That's better."
    "As she drops the bra, you agree."
    wt_image marilyn_club_34
    marilyn.c "Since you seem impressed by these, you can have a short suckle.  Then I want you to sit back."
    wt_image marilyn_club_35
    "As you settle into position, she begins to blow you, although without much enthusiasm."
    $ title = "Settle for a blow job?"
    menu:
      "Yes":
        wt_image marilyn_club_36
        "She may be bored, but she still gives pretty good head and your balls are soon ready to burst.  It's pretty clear that a facial is off the menu, so you settle for holding her head in place as you fill your mouth with cum."
        player.c "[player.orgasm_text]"
        $ marilyn.blowjob_count += 1
        $ marilyn.swallow_count += 1
        wt_image marilyn_club_3
        marilyn.c "You might be surprised at how many powerful men would love to fill my mouth with cum.  You're more privileged than you may suspect.  Ta ta!"
      "No":
        player.c "That feels great, but shouldn't I get more than a blowjob for my IOU?"
        wt_image marilyn_club_26
        "She lets you get up and takes your place on the bed."
        marilyn.c "All right, I'll let you mount me."
        $ title = "What now?"
        menu:
          "Fuck her":
            wt_image marilyn_club_39
            "She's a little dry as you enter her."
            wt_image marilyn_club_6
            marilyn.c "Careful.  I don't carry lube with me.  Normally I only fuck people I'm attracted to."
            wt_image marilyn_club_7
            "She gasps in surprise when you shove your thumb in her ass."
            marilyn.c "Hey!"
            wt_image marilyn_club_27
            player.c "Doesn't that feel good?"
            wt_image marilyn_club_8
            marilyn.c "Just finish up.  You've had my tits in your mouth, my lips on your cock, your cock in my pussy, and now you have your thumb up my ass.  That's as far as this IOU takes you."
            wt_image marilyn_club_27
            "when she puts it that way, it does seem like you got a good deal.  Especially when you add 'put your sperm in my cunt' to the list."
            player.c "[player.orgasm_text]"
            $ marilyn.sex_count += 1
            wt_image marilyn_club_3
            marilyn.c "You've got balls, I'll give you that.  I've removed men's limbs for less offense than sticking a thumb in my ass without asking first.  Ta ta!"
          "Warm her up with your mouth first":
            wt_image marilyn_club_37
            "She gasps in surprise as she feels your mouth on her."
            marilyn.c "ohhh"
            wt_image marilyn_club_38
            marilyn.c "Mmmmm.  Okay, I'm ready for your cock, now."
            wt_image marilyn_club_6
            "She moans in pleasure as you enter her."
            marilyn.c "ohhh"
            wt_image marilyn_club_7
            "Then she gasps in surprise when you shove your thumb in her ass."
            wt_image marilyn_club_27
            marilyn.c "Hey, I didn't say you could ..."
            player.c "Trust me, okay?"
            wt_image marilyn_club_8
            "Between your cock in her pussy and your thumb in her ass, it doesn't take Marilyn long to cum."
            wt_image marilyn_club_7
            marilyn.c "Oohhhhhh"
            wt_image marilyn_club_27
            "You finish shortly after her."
            player.c "[player.orgasm_text]"
            $ marilyn.sex_count += 1
            $ marilyn.orgasm_count += 1
            wt_image marilyn_club_3
            marilyn.c "That was better than I expected.  I think I'm starting to better understand how you're making a go of this whole 'wife training' thing.  Ta ta!"
    call character_location_return(marilyn) from _call_character_location_return_632
    wt_image current_location.image
    rem tags 'in_club_now' from marilyn
    orgasm notify
  return

label marilyn_finish_inside:
  wt_image marilyn_club_10
  "After she cums, you continue to fuck her ass until you're ready for your own orgasm."
  wt_image marilyn_club_30
  "Marilyn's ass feels too good, too tight and warm, to want to pull out, so you fill her rectum with your load."
  player.c "[player.orgasm_text]"
  wt_image marilyn_club_13
  "As she rolls off of you, she looks surprised, but not upset.  Perhaps her protests were just an act, and she secretly loves the feel of semen dripping out of her bowels."
  wt_image marilyn_club_14
  "She stands up and prepares a cup of tea as you recover from your orgasm."
  marilyn.c "Would you like one?"
  $ title = "Do you want some tea?"
  menu menu_marilyn_tea:
    "No thank you" if not marilyn.has_tag('tea_no'):
      wt_image marilyn_club_15
      marilyn.c "It's really quite good. Take a sip."
      add tags 'tea_no' to marilyn
      jump menu_marilyn_tea
    "I said no" if marilyn.has_tag('tea_no') and not marilyn.has_tag('tea_no_again'):
      wt_image marilyn_club_13
      marilyn.c "Really, I must insist."
      add tags 'tea_no_again' to marilyn
      jump menu_marilyn_tea
    "Don't drink it" if marilyn.has_tag('tea_no_again'):
      wt_image marilyn_club_17
      "Somehow, the drink is up to your lips."
      marilyn.c "Go ahead and swallow. I would have for you."
      call marilyn_drink_tea from _call_marilyn_drink_tea
    "Yes":
      call marilyn_drink_tea from _call_marilyn_drink_tea_1
  return

label marilyn_drink_tea:
    wt_image marilyn_club_18
    "The tea tastes .... odd.  Sticky and acrid.  You know you should spit it out, but you can't help yourself from guzzling the whole cup."
    wt_image marilyn_club_19
    "The room starts to swirl around you.  You try to stand, but succeed only in falling to the floor."
    wt_image black_square
    "Your next memories ... your remaining memories ... are of darkness."
    "You can't hear. You can't see."
    "You're fed, but the food has no taste."
    wt_image marilyn_club_20
    "The only sensations that break the monotony are when the cocks enter your ass ... and when they leave their loads there."
    sys "Ignoring what you do and don't have consent for is a bad idea.  Especially with Marilyn.  Bad end."
    ### END THE GAME ###
    jump end_game
    return

## Character Specific Actions
# N/A

## Post-Training Character Actions
# N/A

## Other Character Actions

# Marilyn Reward Person content
label marilyn_whose_reward_menu_dee:
    $ dee.marilyn_event_status = 3
    rem tags 'dee_reward_pending' from marilyn
    marilyn.c "Young, sexually confused university students are so fun. If you find another, please send her my way.  In the meantime, I promised a finder's fee and you've certainly earned one."
    add tags 'reward_chosen' to marilyn
    return

label marilyn_whose_reward_menu_elsa:
    $ marilyn.frigid_encounter_status = 3
    rem tags 'elsa_reward_pending' from marilyn
    marilyn.c "Young, sexually confused housewives are so fun.  If you find another, please send her my way.  In the meantime, I promised a finder's fee and you've certainly earned one."
    add tags 'reward_chosen' to marilyn
    return

label marilyn_whose_reward_menu_terri:
    $ marilyn.independent_encounter_status = 3
    rem tags 'terri_reward_pending' from marilyn
    marilyn.c "I must say, you really impressed me with that messed up little redhead.  It's not very often that someone can offer me a new experience.  I think that deserves a suitable reward."
    add tags 'special_reward' 'reward_chosen' to marilyn
    return

label marilyn_whose_reward_menu_becky_sue:
    $ becky_sue.ready_for_marilyn = 3
    rem tags 'becky_sue_reward_pending' from marilyn
    marilyn.c "That country hick stayed on her knees for me for quite a while.  She clearly didn't want me to be disappointed in her, and I wasn't.  You've definitely earned your finder's fee."
    add tags 'reward_chosen' to marilyn
    return

# Marilyn Reward list description
label marilyn_reward_list:
    call for_call_labels(label_list = [i + '_marilyn_reward_description' for i in marilyn_reward_description_list]) from _call_for_call_labels_47
    if marilyn.has_tag('special_reward'):
        call for_call_labels(label_list = [i + '_marilyn_reward_description' for i in marilyn_special_reward_description_list]) from _call_for_call_labels_48
    return

label club_access_marilyn_reward_description:
    if not player.has_tag('club_access'):
        marilyn.c "I'm a member of a rather exclusive Club.  One for members whose interests are right up your alley.  I think you would fit right in.  I'd choose that as your compensation, if I were you."
        add tags 'club_access_offered' to marilyn
    return

label transformation_potion_marilyn_reward_description:
    if not marilyn.has_tag('transformation_potion_granted'):
        if not player.has_tag('club_access'):
            marilyn.c "Or if you prefer, I have a little potion.  It's one use only, I'm afraid, although that one use is enough to irrevocably change the person you select to drink it."
        else:
            marilyn.c "I have a little potion.  It's one use only, I'm afraid, although that one use is enough to irrevocably change the person you select to drink it."
        add tags 'transformation_potion_offered' to marilyn
    return

label ring_sexuality_marilyn_reward_description:
    if not marilyn.has_tag('ring_sexuality_granted'):
        marilyn.c "Somewhere around here I have a funny little ring you might be interested in.  While wearing it, a woman who used to be only interested in boys will find the female anatomy equally fascinating.  I've used a few of them over the years, but I think I still have one you could have, if you want."
    return

label janice_trigger_marilyn_reward_description:
    if janice.tried_hypnosis == 2:
        marilyn.c "Since you showed an interest in my lawyer, if you want I could share her trigger with you."
    return

label will_tamer_marilyn_reward_description:
    if not marilyn.has_tag('will_tamer_granted'):
        marilyn.c "Considering what a great job you did, I suppose I should offer you a Will-Tamer.  It's one of my more powerful items."
        marilyn.c "It looks like a normal collar, but it does delicious things to the brain of the person who wears it.  These are quite rare, but you've earned it."
        add tags 'will_tamer_offered' to marilyn
    return

# Marilyn Reward content
label marilyn_reward_menu_club_access:
    marilyn.c "An excellent choice.  I'll let them know to expect you."
    add tags 'club_access' to player
    rem tags 'club_access_offered' from marilyn
    return

label marilyn_reward_menu_janice_trigger:
    marilyn.c "Quite fascinated with the affairs of the mind, aren't you? Or perhaps you just want to see a high priced lawyer sit up and beg?"
    wt_image marilyn_office_22
    marilyn.c "Her trigger is '[janice.trigger_phrase]'."
    marilyn.c "That's not her full trigger, of course.  It won't let you rummage around in her mind or find out my secrets.  But it will let you have some fun with her from time to time, if you're so inclined."
    marilyn.c "And perhaps, as a student of the arts, it may help you learn a thing or two.  But be very careful with her.  She's far more valuable to me than you will ever be.  If you break her or do something stupid that lowers her value to me, your life expectancy will become extremely short."
    $ janice.tried_hypnosis = 3
    add tags 'trigger_implanted' to janice
    return

label marilyn_reward_menu_transformation_potion:
    wt_image marilyn_office_22
    marilyn.c "It should go without saying that you do not implicate me in the acquisition of this item, or any trouble you may find yourself in for having used it will get infinitely worse for you."
    add 1 transformation_potion to player notify
    add tags 'transformation_potion_granted' to marilyn
    rem tags 'transformation_potion_offered' from marilyn
    return

label marilyn_reward_menu_ring_sexuality:
    wt_image marilyn_office_22
    marilyn.c "If the person who gets this is young, fair and cute, don't hesitate to send her my way."
    $ ring_sexuality.name = "Ring of Sexuality"
    add 1 ring_sexuality to player notify
    add tags 'ring_sexuality_granted' to marilyn
    return

label marilyn_reward_menu_will_tamer:
    marilyn.c "This is a bit of a tricky item. Perhaps you'd like me to put it on you, to show you how it works?"
    $ title = "What do you think?"
    menu:
        "Okay":
            wt_image marilyn_office_22
            "Marilyn smiles."
            marilyn.c "Excellent.  It's hard to use these things properly if you don't understand how they work."
            wt_image you_collared_1
            "She places the collar around your neck and clasps it in place."
            wt_image you_collared_2
            "It feels good.  Very good.  Warm and snug and comforting around your neck.  It's just so ... right."
            "Marilyn is so powerful.  So very powerful and important.  You're so lucky to have her guidance.  Of all the men out there, she could have placed this collar on any of them.  She chose you."
            "You should show her how greatly you appreciate her trust.  Anything she asks of you, you should do.  It's an honor to be allowed to obey her."
            wt_image marilyn_office_22
            "Suddenly, the warm comfortable feeling is gone, but the woman you're so lucky to have met is still there."
            marilyn.c "Never leave it on too long at one time. It starts out helping your subject come to see you for the important person you are.  Lots of brain re-wiring happening."
            marilyn.c "It's still happening, to you.  It will for a few more days.  Then you'll be ready for another session."
            marilyn.c "For whatever reason, it will only work on someone who willingly lets you put it on them.  Of course, after wearing it once, it's ususally a lot easier to get them to wear it again."
            marilyn.c "After a few sessions, you'll have yourself a nice, obedient slave."
            marilyn.c "Unfortunately, to make the effect permanent, the Will-Tamer itself gets absorbed into the subject. Prior to then you can use it to improve your relationship with multiple people but it will only claim one of them for a permanent lap dog."
            marilyn.c "Watch out you don't keep it in place for too long for one stretch though, or you'll end up with - mush.  It's not pretty.  A blithering, slobbery brainless wreck.  Yuck."
            "Wearing the collar has tired you out, but it was worth to learn how incredible Marilyn truly is."
            change player energy by -energy_long notify
        "I'm sure I can figure it out":
            player.c "I'm sure I can figure it out on my own."
            wt_image marilyn_office_22
            marilyn.c "So untrusting.  I have plenty of lapdogs.  Besides, you're far too old for me.  And you can be much more useful just as you are.  Still, suit yourself."
    "She hands over the collar."
    marilyn.c "Have fun."
    add 1 will_tamer to player notify
    add tags 'will_tamer_granted' to marilyn
    rem tags 'will_tamer_offered' from marilyn
    return

label marilyn_reward_menu_her:
    if marilyn.sex_count > 0:
        player.c "I'd like you as my reward, again."
        if marilyn.has_tag('dominated_her') or marilyn.orgasm_count > 0:
            marilyn.c "Hmmm. You were pretty good, but I'm not big on repeat partners, unless I'm really horny and can't find someone new.  Which isn't the case today."
        else:
            marilyn.c "That was a one time thing.  I'm not big on repeat partners."
        call expandable_menu(marilyn_reward_menu) from _call_expandable_menu_104
    elif marilyn.has_tag('special_reward'):
        marilyn.c "Really? I offer you some rather tantalizing forms of payment, and you'd forego those in order to get between my legs?"
        marilyn.c "I would take that as flattery, if it didn't say more about you than it does about me."
        wt_image marilyn_office_3
        marilyn.c "Very well then."
        "She lowers herself, catlike, to her knees in front of you."
        marilyn.c "You delivered a very interesting experience to me, and I promised a suitable reward."
        wt_image marilyn_office_4
        marilyn.c "There've been a lot of men over the years who wanted to see me on my knees, sucking their cock.  I put more than a few of them on their knees, sucking another man's cock, just to enjoy the humiliation of watching them do it.  So I hope you appreciate this."
        wt_image marilyn_office_5
        "She lowers her mouth over your cock, and starts sucking.  It's nice, but for your payment you should probably ask for more than just a blow job."
        if player.has_tag('dominant'):
            $ title = "Dominate her?"
            menu:
                "Yes":
                    add tags 'dominated_her' to marilyn
                    player.c "That's a good girl. Is it really so humiliating, being down on your knees sucking a man's cock?"
                    if marilyn.independent_encounter_status > 2:
                        player.c "I want you to lose the power woman persona for a few minutes, Marilyn.  There's no one here but you and me.  You enjoyed the experience I gave you with Terri.  I want to give you a new one, equally enjoyable."
                    else:
                        player.c "I want you to lose the power woman persona for a few minutes, Marilyn.  There's no one here but you and me.  I want to give you a new experience, one I think you'll enjoy."
                    player.c "For the next little while, I want you to be my bitch.  It's easy.  You may even enjoy it.  You just let go of the real world for a moment, and all the power, and responsibility, and authority you have."
                    player.c "You let life become incredibly simple. Your role right now is to please me.  Nothing else matters.  You don't have to think about consequences, or angles, or power struggles."
                    player.c "Because you've turned control of your body and your actions over to me, for as long as it takes for me to cum.  Your mind can just come along for the ride, relax, and enjoy the sensation."
                    wt_image marilyn_office_6
                    "She says nothing, but she takes you deeper into her mouth and you know you have her."
                    player.c "Stand up now.  You're going to show your body to me."
                    wt_image marilyn_office_7
                    "She rises to her feet and pulls her dress down."
                    player.c "Turn around and let me examine you."
                    wt_image marilyn_office_8
                    "She's not shy about her body, but your tone sparks a hint of nervousness in her as she turns under your supervision. You expect it's been a very long time since she's felt this way."
                    player.c "On the bench. On your knees. Face away from me."
                    wt_image marilyn_office_9
                    "She lithely moves into position, a questioning look on her face as she tries to anticipate what you'll do next."
                    wt_image marilyn_office_10
                    "*smack*"
                    marilyn.c "Ow"
                    "She cries out in surprise as your hand strikes her ass.  Just once, then she collects herself, and takes the rest of the spanking silently ... *smack* ... *smack* ... *smack*"
                    wt_image marilyn_office_9
                    "She doesn't question why you're spanking her.  She understands it's to show that she's willing to let you hurt her.  Somewhat unexpectedly to her, she is.  She wiggles her butt upwards, seeking the stinging blow from your hand as you continue ... *smack* ... *smack* ... *smack*"
                    wt_image marilyn_office_11
                    "When you're finished, you let her rub her ass for a minute."
                    player.c "That's enough recovery. Back to work."
                    wt_image marilyn_office_12
                    "This time she gobbles your cock down with enthusiasm.  You let her get you nice and hard, then turn her around."
                    wt_image marilyn_office_13
                    "She looks back at you and moans a couple of times as you plow into her from behind."
                    marilyn.c "ohhh  ...  oohhhh"
                    wt_image marilyn_office_26
                    "You're pretty sure she wants your hand - or hers - on her clit.  You're not about to offer, however, and she isn't nearly submissive enough to ask.  This is your payment.  As fun as it would have been to listen to her ask for an orgasm, you're happy having your own inside her."
                    wt_image marilyn_office_27
                    player.c "[player.orgasm_text]"
                    wt_image marilyn_office_2
                    "When you're finished, Marilyn dresses and retrieves her drink."
                    if not player.has_tag('club_access'):
                        marilyn.c "Even though you didn't choose it for your reward, I'm sponsoring you for membership in our Club, anyway.  You'll fit in perfectly."
                        add tags 'club_access' to marilyn
                    marilyn.c "If you tell anybody about what I let you do to me, you're dead.  You understand?"
                    $ player.submission_action_count += 1
                    $ marilyn.sex_count += 1
                    orgasm notify
                "No":
                    call marilyn_no_dominate from _call_marilyn_no_dominate
        else:
            call marilyn_no_dominate from _call_marilyn_no_dominate_1
    else:
        player.c "How about you as my reward?"
        "Marilyn laughs."
        marilyn.c "I'm afraid you're not young enough for my tastes, and as much as I enjoyed the treat you sent my way, you'll need to supply something a bit more special before I spread my legs for you."
        call expandable_menu(marilyn_reward_menu) from _call_expandable_menu_105
    return

label marilyn_no_dominate:
  player.c "Mmmm.  That feels great.  How about we do something else now?"
  wt_image marilyn_office_14
  "Marilyn smiles.  She stands up and removes her dress."
  wt_image marilyn_office_15
  "Then settles back against you, her bare ass nestling against your cock."
  wt_image marilyn_office_16
  "After teasing you for a moment, she lifts up and settles onto your cock."
  marilyn.c "Was this more of what you were looking for?"
  wt_image marilyn_office_17
  marilyn.c "Or perhaps this?"
  "She spins around to face you.  Placing her hands on her chest, she starts riding you up and down."
  if player.has_tag('supersexy'):
    wt_image marilyn_office_19
    "To her surprise, you take hold of her feet and leverage her backwards, changing the angle at which your cock is stroking into her."
    wt_image marilyn_office_20
    "Soon you've worked her onto the floor, on her back.  In this position, you're able to control the pace and intensity of the fucking."
    wt_image marilyn_office_21
    "Marilyn starts stroking her clit as you fuck her.  You control the intensity of your own arousal until she cums, then you let yourself go inside her."
    wt_image marilyn_office_20
    marilyn.c "Oohhhhhh"
    player.c "[player.orgasm_text]"
    wt_image marilyn_office_21
    marilyn.c "Mmmmm. That was unexpectedly pleasurable."
    wt_image marilyn_office_2
    "A moment later, she's off of you and dressed, her drink back in her hand."
    marilyn.c "I hope you enjoyed your finder's fee.  I certainly did."
    if not player.has_tag('club_access'):
      marilyn.c "Even though you didn't choose it as your reward, I'm sponsoring you for membership in our Club, anyway.  You'll fit in perfectly."
      add tags 'club_access' to marilyn
    $ marilyn.orgasm_count += 1
    $ player.desire_action_count += 1
  else:
    wt_image marilyn_office_18
    "It doesn't take long for Marilyn to milk the seed out of you with her cunt.  As she feels you climax, she grinds down hard on you, a look of satisfaction on her face."
    player.c "[player.orgasm_text]"
    wt_image marilyn_office_2
    "A moment later, she's off of you and dressed, her drink back in her hand."
    marilyn.c "I hope you enjoyed your finder's fee."
  wt_image marilyn_office_2
  $ marilyn.sex_count += 1
  orgasm notify
  return

label marilyn_reward_menu_iou:
    player.c "How about I take an IOU?"
    marilyn.c "Sure. Let me know when I can help you out."
    "Marilyn now owes you a favor."
    $ marilyn.favour += 1
    return

# Marilyn IOU content
label marilyn_iou_menu_club_access:
    player.c "You mentioned a private Club.  Could I trade an IOU for membership sponsorship?"
    marilyn.c "An excellent choice.  I'll let them know to expect you."
    add tags 'club_access' to player
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_janice_retainer:
    player.c "I'm having trouble getting Janice to agree to represent me.  Could you convince her to take me on as a client?"
    marilyn.c "Hmmm.  I may be able to persuade her.  Consider it done."
    add tags 'lawyer_on_retainer' to player
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_janice_trigger:
    player.c "Could I trade an IOU for access to Janice's trigger?"
    marilyn.c "Quite fascinated with the affairs of the mind, aren't you? Or perhaps you just want to see a high priced lawyer sit up and beg?"
    marilyn.c "Her trigger is '[janice.trigger_phrase]'."
    marilyn.c "That's not her full trigger, of course.  It won't let you rummage around in her mind or find out my secrets.  But it will let you have some fun with her from time to time, if you're so inclined."
    marilyn.c "And perhaps, as a student of the arts, it may help you learn a thing or two.  But be very careful with her.  She's far more valuable to me than you will ever be.  If you break her or do something stupid that lowers her value to me, your life expectancy will become extremely short."
    $ janice.tried_hypnosis = 3
    add tags 'trigger_implanted' to janice
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_transformation_potion:
    player.c "Could I trade an IOU for that transformation potion you mentioned?"
    marilyn.c "I suppose.  Drop by my office to pick it up."
    add tags 'iou_pickup_pending' 'iou_transformation_potion_pending' to marilyn
    rem tags 'transformation_potion_offered' from marilyn
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_ring_sexuality:
    player.c "Could I trade an IOU for that ring you mentioned?"
    marilyn.c "Sure, I think I know where I put it.  Drop by my office to pick it up."
    add tags 'iou_pickup_pending' 'iou_ring_sexuality_pending' to marilyn
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_will_tamer:
    player.c "Could I trade an IOU for that special collar you mentioned?"
    marilyn.c "I suppose.  You'll need to drop by my office, though, so I can show you how it works."
    add tags 'iou_pickup_pending' 'iou_will_tamer_pending' to marilyn
    rem tags 'will_tamer_offered' from marilyn
    $ marilyn.favour -= 1
    return

label marilyn_iou_menu_whore_cut:
    player.c "In return for an IOU, could I get you to stop taking a cut of my weekly whore income?"
    marilyn.c "Definitely not.  That'd send the wrong message to my other 'managers'."
    player.c "Well, could you at least reduce it?"
    marilyn.c "Fine.  I'll drop my cut to 10%, but that's as low as I go, and only if you don't tell a soul that you're getting a discount."
    $ title = "Accept?"
    menu:
        "Yes (trade IOU for whore income cut reduction)":
            add tags 'whore_cut_reduced' to marilyn
            $ marilyn.whore_cut_percentage = 0.9
            player.c "Deal"
        "No (leave Marilyn's whore income cut at 20 percent)":
            player.c "Never mind."
            call expandable_menu(marilyn_iou_menu) from _call_expandable_menu_106

label marilyn_iou_menu_rep_gain:
    if not player.has_tag('rep_needed'):
        sys "Are you sure you want to ask for this now?  You could wait until you're out of prospective and current clients."
    $ title = "Ask to trade an IOU for a Rep gain now?"
    menu:
        "Yes":
            player.c "Marilyn, I've run into a bit of a snag in my business.  I need a boost to my Reputation.  With your contacts, I was wondering if there's anything you could do to help?"
            marilyn.c "What am I, a PR firm for the small and insignificant?  Find someone else to help you."
            player.c "You owe me one, remember?"
            marilyn.c "Okay, fine.  I'll tell my men it would be a shame if you went out of business.  I'm sure they can fix your reputation issue."
            $ marilyn.favour -= 1
            rem tags 'rep_needed' from player
            add tags 'rep_from_marilyn' to player
            change player reputation by 1 notify
        "No":
            call expandable_menu(marilyn_iou_menu) from _call_expandable_menu_107
    return

label transformation_potion_marilyn_iou_pickup:
    if marilyn.has_tag('iou_transformation_potion_pending'):
        rem tags 'iou_transformation_potion_pending' from marilyn
        call marilyn_reward_menu_transformation_potion from _call_marilyn_reward_menu_transformation_potion
    return

label ring_sexuality_marilyn_iou_pickup:
    if marilyn.has_tag(iou_ring_sexuality_pending):
        rem tags 'iou_ring_sexuality_pending' from marilyn
        call marilyn_reward_menu_ring_sexuality from _call_marilyn_reward_menu_ring_sexuality
    return

label will_tamer_marilyn_iou_pickup:
    if marilyn.has_tag(iou_will_tamer_pending):
        rem tags 'iou_will_tamer_pending' from marilyn
        call marilyn_reward_menu_will_tamer from _call_marilyn_reward_menu_will_tamer
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label marilyn_contact:
    if marilyn.has_tag('contacted_today'):
        if marilyn.contact_art_countdown == 0:
            wt_image marilyn_contact_1
        elif marilyn.contact_art_countdown == 2:
            wt_image marilyn_contact_2
        elif marilyn.contact_art_countdown == 3:
            wt_image marilyn_contact_3
        else:
            wt_image marilyn_contact_4
        marilyn.c "What is it now?"
    else:
        add tags 'contacted_today' to marilyn
        if marilyn.contact_art_countdown == 0:
            $ marilyn.contact_art_countdown = renpy.random.randint(3, 5)
        $ marilyn.contact_art_countdown -= 1
        if marilyn.contact_art_countdown == 0:
            wt_image marilyn_contact_1
            marilyn.c "Make it snappy.  You're interrupting my massage."
        elif marilyn.contact_art_countdown == 2:
            wt_image marilyn_contact_2
            marilyn.c "What do you want?  I'm in the middle of something here, or at least I'm about to be."
        elif marilyn.contact_art_countdown == 3:
            wt_image marilyn_contact_3
            marilyn.c "What is it?"
        else:
            wt_image marilyn_contact_4
            marilyn.c "What is it?"
    # ask for rep gain
    if player.has_tag('rep_needed'):
        if player.has_tag('rep_from_marilyn'):
            player.c "Marilyn, I've run into another snag. Can you tell your men to boost to my Reputation again?"
            marilyn.c "I've put enough of my operation's credibility on the line for you already. You're going to need to start growing your business yourself."
        elif marilyn.orgasm_count >= 1 or marilyn.has_tag('dominated_her'):
            player.c "Marilyn, I've run into a bit of a snag in my business. I need a boost to my Reputation. With your contacts, I was wondering if there's anything you could do to help?"
            marilyn.c "Well, I'm certainly not putting my name behind a recommendation for you, no matter how good I found you."
            marilyn.c "Still, I may be able to help. I'll tell my men it would be a shame if you went out of business. I'm sure they can fix your reputation issue."
            rem tags 'rep_needed' from player
            add tags 'rep_from_marilyn' to player
            change player reputation by 1 notify
        else:
            player.c "Marilyn, I've run into a bit of a snag in my business.  I need a boost to my Reputation.  With your contacts, I was wondering if there's anything you could do to help?"
            marilyn.c "What am I, a PR firm for the small and insignificant?  Find someone else to help you."
            if marilyn.favour > 0:
                $ title = "Call in your favor?"
                menu:
                    "Yes, ask Marilyn for help":
                        player.c "You owe me one, remember?"
                        marilyn.c "Okay, fine.  I'll tell my men it would be a shame if you went out of business.  I'm sure they can fix your reputation issue."
                        $ marilyn.favour -= 1
                        rem tags 'rep_needed' from player
                        add tags 'rep_from_marilyn' to player
                        change player reputation by 1 notify
                    "No, find someone else to help":
                        pass
    # ask about Sam: would have been more consistent with new system to move this to Sam's script, but follows the Rags' system  of using janice's variables so left here
    if marilyn.discuss_barista == 1:
        "You discuss Sam the Barista's new single status with Marilyn."
        marilyn.c "You mean the girl who works in the coffee shop downtown?  I had her once, a long time ago, right after she started working there.  It might have been before she met her current ex."
        marilyn.c "Anyway, she was fine, but frankly, not worth another go at."
        marilyn.c "Let me know when you've found someone new, preferably someone a little more interesting than a woman with no ambition in life other than to sling coffee."
        $ marilyn.discuss_barista = 2
    # now call all talk options for Marilyn related to other characters
    call for_call_labels(label_list = [p.short_name + '_marilyn_talk_option' for p in get_people(tagged_with_all=['marilyn_talk_option_possible'])]) from _call_for_call_labels_49
    # finish by giving an opportunity to cash in an IOU
    if marilyn.favour > 0:
        call expandable_menu(marilyn_iou_menu) from _call_expandable_menu_108
    "You have nothing more to discuss with Marilyn at this time."
    wt_image current_location.image
    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_marilyn:
  "She won't put this in your ass, and you're certainly not putting it in hers."
  return

# Give Chastity Belt
label give_cb_marilyn:
  "The best possible reaction is that she laughs in your face."
  return

# Give Dildo
label give_di_marilyn:
  "That's not going to get you on her good side."
  return

# Use Fetch Toy
label use_ft_marilyn:
  "That's a dangerous game to play."
  return

# Give Jewelry
label give_jwc_marilyn:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_marilyn:
  "You seem to gravely misunderstand the nature of your relationship with her."
  return

# Give Lingerie
label give_li_marilyn:
  "Gifts are not the way to her heart.  Not this type of gift, anyway."
  return

# Give Love Potion
label give_lp_marilyn:
  "There are some people to whom you can safely slip a mind altering drug, and others for whom the risk far outweighs the reward.  Marilyn is firmly amongst the latter, even when her bodyguards aren't watching her."
  return

# Give Transformation Potion
label give_tp_marilyn:
  "There are some people to whom you can safely slip a mind altering drug, and others for whom the risk far outweighs the reward.  Marilyn is firmly amongst the latter, even when her bodyguards aren't watching her."
  return

# Give Ring of Secuality
label give_rs_marilyn:
    "She likes girls already.  And boys.  She does have an extreme lack-of-commitment complex with both, but the ring won't help with that."
    return

# Use Water Bowl
label use_wb_marilyn:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_marilyn:
  "You're not likely to collar her anywhere.{nw}"
  if current_location == club:
    extend "  You're certainly not doing so here, with her bodyguards nearby."
  else:
    extend "  You're certainly not doing so here and now."
  return

########### TIMERS ###########
## Common Timers
# Start Day
#label marilyn_start_day: # not anne_third_session_draw_multiple_cards
#  return

# End Day
label marilyn_end_day:
    rem tags 'in_club_now' 'contacted_today' from marilyn
    call character_location_return(marilyn) from _call_character_location_return_633
    return

# End Week
label marilyn_end_week:
    if player.whore_count > 2 and not player.has_tag('marilyn_whore_cut'):
        $ marilyn.whore_cut_percentage = 0.8
        add tags 'marilyn_whore_cut' to player
        wt_image phone_1
        "Your phone is ringing."
        wt_image marilyn_contact_4
        player.c "Marilyn?"
        marilyn.c "I'm just giving you a ring to let you know about our new business arrangement.  I was willing to overlook your 'hobby' for a while, but you keep adding to your stable of working girls."
        marilyn.c "There are only so many horny men with money looking for companionship every week.  If I let you continue to free lance, that wouldn't be fair to my other 'managers', would it?"
        marilyn.c "So I'm going to give you the same deal I give them.  Twenty percent of everything you make comes to me, and you get to continue your side business."
        $ title = "What do you say?"
        menu:
            "Deal":
                player.c "Understood"
                marilyn.c "Good.  I told Janice I didn't think you were as stupid as you look.  I'm so glad you proved me right.  Ta ta!"
            "What if I say no?":
                player.c "Is this a business arrangement, or a shake down?  What if I say no?"
                marilyn.c "That depends.  Do you have a way to deal with any of my men who happened to pay you a visit?"
                if player.hypnosis_level > 0:
                    marilyn.c "There'll more than one of them, so I don't like your odds of hypnotizing them.  They're fairly robust men, too, so I don't like your odds of physically chasing them away."
                else:
                    marilyn.c "They're fairly robust men, so I don't like your odds of physically chasing them away."
                marilyn.c "You could arm yourself, of course, but that would escalate matters, wouldn't it?  If you use a gun and my men use their guns ... well, I'll be disappointed with that outcome, but not as disappointed as you're likely to be."
                marilyn.c "I guess that leaves the police.  You could explain to them that you're a pimp and someone's muscling in on your racket, and maybe if you're really persuasive they'll post a guard for a little while, and if you're really, really lucky it might even be one of the officers who isn't on my payroll."
                marilyn.c "But even then, how long do you think you'll be put under guard versus how long do you think I can wait?  And if the police were going to come after me, do you think it would be over this conversation?  Janice would have this thrown out of court in a heart beat."
                player.c "You're saying I don't have any choice."
                marilyn.c "Don't sound so glum.  I won't let anyone else start up a competing business to yours without taking a cut from them, too.  I believe in creating a fair economic environment for everyone.  Ta ta!"
        wt_image current_location.image
    return


## Club and Stage Labels

label marilyn_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if marilyn.has_tag('in_club_now'):
            $ marilyn.location = club
    else:
        $ marilyn.random_number = renpy.random.randint(1, 10)
        if marilyn.random_number > 6:
            $ marilyn.location = club
            add tags 'in_club_now' 'gloria_club_talk_possible' to marilyn
    return

label marilyn_club_send_home:
    call character_location_return(marilyn) from _call_character_location_return_634
    return


## Club President Wife Content

label marilyn_gloria_club_talk_option:
    gloria.c "She's an important sponsor of the Club. Without her and a couple of others, the Club wouldn't exist, and my husband wouldn't have his job."
    gloria.c "I'm grateful to her, of course, for helping to create this place and putting my husband in charge."
    gloria.c "Still, if I were you, I'd suggest you not get too close. And whatever you do, don't cross her."
    player.c "But what's her story? What kind of business does she run?"
    gloria.c "Some questions are better left unasked."
    return


## Character Specific Timers
# N/A

########### ROOMS ###########
# Examine Marilyn's Building
label mb_examine:
    if player.marilyn_building_visit_count == 0:
        "You approach the non-descript building.  There are no identifying signs to suggest who owns or occupies it."
    else:
        "A non-descript building with no identifying signs to suggest who owns or occupies it."
    return

# Prevent Access to Marilyn's Building
label mb_no_access:
  if player.marilyn_building_visit_count == 0:
    wt_image marilyn_building.image
    call mb_examine from _call_mb_examine
    $ marilyn_building.unseen = False
    wt_image marilyn_security_1
    "You're stopped as soon as you enter the building."
    guard_marilyn "This is private property."
    player.c "I'm here to see Marilyn. Janice sent me."
    guard_marilyn "Just a moment."
    wt_image marilyn_security_2
    "The security guard confers with someone on his headset."
    guard_marilyn "Okay.  Follow me."
    #$ marilyn_building.unseen = False  ## old coding
    "He leads you to an elevator and takes you to the top floor."
  elif player.marilyn_building_visit_count > 0:
    wt_image marilyn_security_1
    "You're stopped as soon as you enter the building."
    player.c "I have additional business with Marilyn."
    if marilyn.rewards_pending > 0 or marilyn.has_tag('iou_pickup_pending'):
      wt_image marilyn_security_2
      "The security guard confers with someone on his headset."
      guard_marilyn "Okay.  Follow me."
    else:
      guard_marilyn "Just a moment."
      wt_image marilyn_security_2
      "The security guard confers with someone on his headset."
      guard_marilyn "She's not available.  If you have something for her, call ahead.  You need to leave now."
      "He escorts you out of the building."
      break_movement
      wt_image current_location.image
  return

label mb_enter:
    if player.marilyn_building_visit_count == 0:
        wt_image marilyn_office_1
        "The elevator opens onto a large room that seems to occupy the entire top floor. The guard takes the elevator back down, leaving you alone with Marilyn."
        marilyn.c "So you're the famous 'Wife Trainer' Janice told me about."
        "If she remembers bumping into you in the law office, she gives no indication."
        marilyn.c "I'm told you could be useful to me."
        player.c "Useful how?"
        marilyn.c "I want much the same thing Janice wants. Fair-skinned, fair-haired pussy. A virgin preferably. Young definitely. I like mine young."
        player.c "You and Janice have similar interests."
        wt_image marilyn_office_23
        "She smirks."
        marilyn.c "Mine are broader than hers. I'll take fair-skinned, fair-haired hard cock too, if you're able to deliver an appropriate young man. I assume, from your line of work, that pussy is more likely to come under your - persuasion."
        player.c "Surely a woman with your - attributes - doesn't have difficulty acquiring access to pussy, or cock."
        marilyn.c "I don't, but I'm fickle. One tryst and I'm bored. My staff work hard to deliver a steady supply of bedmates, but I always appreciate the efforts of freelancers."
        wt_image marilyn_office_24
        marilyn.c "Send someone interesting my way, and I'll make it worth your while."
        "She hands over a phone number."
        if player.test('hypnosis_level', 0):
            $ title = "Do you want to hypnotize her?"
            menu:
                "Yes":
                    player.c "Marilyn, I'd like you to look at something."
                    "She chuckles."
                    marilyn.c "I'm not going to let you hypnotize me.  Save that for your silly housewives."
                    marilyn.c "And don't try that on any of my staff, either.  It won't work, and some of them may get violent with you."
                    if janice.tried_hypnosis == 1:
                        $ title = "Ask her about Janice's mind block?"
                        menu:
                            "Yes":
                                player.c "Are you responsible for Janice's mental block against hypnosis?"
                                wt_image marilyn_office_25
                                marilyn.c "Very good.  Yes, I am."
                                marilyn.c "She's an excellent lawyer, very useful to me. And such an obedient little puppet. She wouldn't be much use to me, however, without that brilliant brain of hers left free to do its thing."
                                marilyn.c "On the other hand, I couldn't risk someone else taking control of her and using her brain against me. The block is an elegant solution, don't you think?"
                                marilyn.c "Time for you to go now."
                                $ janice.tried_hypnosis = 2
                            "No":
                                pass
                "No":
                    pass
        "The security guard returns and escorts you out of the building."
        $ player.marilyn_building_visit_count += 1
        $ marilyn.frigid_encounter_status = 1
        $ marilyn.independent_encounter_status = 1
        $ marilyn.action_contact = living_room.add_action("Contact " + marilyn.full_name, label = marilyn.short_name + "_contact", context = "_contact_other", condition = "marilyn.can_be_interacted")
        call forced_movement(downtown) from _call_forced_movement_928
    elif marilyn.has_tag('iou_pickup_pending'):
        rem tags 'iou_pickup_pending' from marilyn
        wt_image marilyn_office_22
        "He leads you to an elevator and takes you to the top floor.  Marilyn is waiting for you as you exit the elevator."
        call for_call_labels(label_list = [i + '_marilyn_iou_pickup' for i in marilyn_iou_pick_up_list]) from _call_for_call_labels_50
        wt_image current_location.image
        "Marilyn summons the elevator and the security guard escorts you from the building."
        call forced_movement(downtown) from _call_forced_movement_929
        $ player.marilyn_building_visit_count += 1
    elif marilyn.rewards_pending > 0:
        wt_image marilyn_office_2
        "He leads you to an elevator and takes you to the top floor.  Marilyn is waiting for you as you exit the elevator.  She's enjoying an early libation, but makes no attempt to offer you one."
        marilyn.c "So nice to see you again.  That was good work you did."
        call expandable_menu(marilyn_whose_reward_menu) from _call_expandable_menu_109
        if marilyn.has_tag('reward_chosen'):
            rem tags 'reward_chosen' from marilyn
            call marilyn_reward_list from _call_marilyn_reward_list
            call expandable_menu(marilyn_reward_menu) from _call_expandable_menu_110
            $ marilyn.rewards_pending -= 1
            $ marilyn.rewards_given += 1
            rem tags 'special_reward' from marilyn
        wt_image current_location.image
        "Marilyn summons the elevator, and the security guard escorts you from the building."
        call forced_movement(downtown) from _call_forced_movement_930
        $ player.marilyn_building_visit_count += 1
    else:
        call forced_movement(downtown) from _call_forced_movement_931
    return

label mb_exit:
  return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
