## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou & The Fiduciary

# Package  Register
# register_package julia name "Julia" description "Adds Julia to the Jewelry Store" dependencies core
register julia_pregame 11 in core as "Julia the Jewelry Store Clerk" # NOTE: must load after Chelsea otherwise action with Chelsea's name in it will cause a crash

label julia_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Julia the Jewelry Store Clerk (Sophie Dee)")]

    ## Character Definition
    julia = Person(Character("Julia", who_color="#FF0080", what_color="#FF0080"), "julia", cut_portrait = True, prefix = "", suffix = "the Jewelry Store Clerk")

    # Other Characters
    # 0,64,128
    husband_julia = Character("Julia's Husband", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    julia.action_contact = living_room.add_action("Visit Julia the Jewelry Clerk at home", label = julia.short_name + "_contact", context = "_contact_other", condition = "julia.can_be_interacted and julia.home_visits_active and not jewelry_store.visited_today")
    julia.action_talk = julia.add_action("Talk to her", label = "_talk", condition = "julia.can_be_interacted and current_location == jewelry_store")


    ## Tags
    # Common Character Tags
    julia.add_tags('no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    # Julia's House
    julia_house = Location("Julia's House", 'jh', cut_portrait = False, enter_break_labels = ['jh_no_access'], enter_labels = ['jh_enter'], exit_labels = ['jh_exit']) # disabled as dealt with through contact visit, you never actually go there

    # Jewelry Store
    # Note: can't access jewelry_store until proper event opens connection with office tower
    jewelry_store = Location("Jewelry Store", 'js', cut_portrait = True, enter_break_labels = ['js_no_access'], enter_labels = ['js_enter'], exit_labels = ['js_exit'], area = 'offices')
    #jewelry_store.add_store_item(jewelry_chelsea, available_quantity = 1, price = 2000, send_to = player)
    jewelry_store.connection_ot = jewelry_store.add_connections(office_tower) # connection to office tower starts open; connection from office tower to jewelry_store only opens in the start_day label for julia
    julia.location = jewelry_store
    julia.fixed_location = jewelry_store

    ## Other
    julia.change_status("minor_character")
    handcuffs_julia = Item('Handcuffs', 'hcj', with_examine = True, with_give = True)
    handcuffs_julia.action_throw_away = handcuffs_julia.add_action("Throw It Away", label = '_throw_away')

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('julia_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    julia.add_stats_with_value('bikini_outfit', 'discussed_pride', 'handcuff_discussion', 'home_visit_outfit', 'husband_outfit', '', '')
    julia.discussed_bimbo = False
    julia.discussed_bra = False
    julia.discussed_date = False
    julia.discussed_her = False
    julia.discussed_panties = False
    julia.discussed_store = False
    julia.home_visits_active = False
    julia.hypno_bj = False
    julia.naked_now = False
    julia.look_pretty = False
    julia.look_naked = False
    julia.look_sexy = False
    julia.pose_sexy = False
    julia.this_is_fine = False
    julia.get_on_knees = False
    julia.done_foreplay = False

    # Location Variables
    jewelry_store.add_stats_with_value('visit_count')
    jewelry_store.initial_message = False
    jewelry_store.visited_today = False

    ######## EXPANDABLE MENUES #######
    julia_store_talk_menu = ExpandableMenu("What do you want to talk about?", cancelable = False)
    julia_store_purchase_menu = ExpandableMenu("Do you want to buy anything?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game
    julia.choice_store_talk_nothing = julia_store_talk_menu.add_choice("Nothing at this time", "julia_talk_nothing")
    julia.choice_store_talk_bimbo = julia_store_talk_menu.add_choice("Why do you act like a bimbo?", "julia_talk_why_bimbo", condition = "not julia.discussed_bimbo")
    julia.choice_store_talk_date = julia_store_talk_menu.add_choice("Would you like to go on a date?", "julia_talk_date", condition = "not julia.discussed_date")
    julia.choice_store_talk_bra = julia_store_talk_menu.add_choice("Ask where she gets her bras", "julia_talk_bras", condition = "chelsea.bra_fitting_status == 1")
    julia.choice_store_talk_donna = julia_store_talk_menu.add_choice("Ask her to help train Donna", "julia_talk_donna", condition = "donna.ready_for_julia == 1 and julia.discussed_bimbo")
    julia.choice_store_talk_handcuffs = julia_store_talk_menu.add_choice("Discuss the handcuffs", "julia_jewelry_store_discuss_handcuffs", condition = "julia.discussed_date and player.has_item(handcuffs_julia) and player.has_tag('dominant')")
    julia.choice_store_buy_leave = julia_store_purchase_menu.add_choice("No, just leave", "julia_no_buy_leave")
    julia.choice_store_buy_nipple_clips = julia_store_purchase_menu.add_choice("Ask her about nipple clips", "julia_nipple_clips", condition = "jasmine.whore_play_status == 7")
    julia.choice_store_buy_gift_chelsea = julia_store_purchase_menu.add_choice("Ask about a gift for [chelsea.name]", "julia_chelsea_gift", condition = "chelsea.status == 'post_training' and chelsea.has_tag('continuing_actions') and chelsea.has_item(lingerie) and not chelsea.has_item(jewelry_chelsea) and not player.has_item(jewelry_chelsea)")


  return

# Display Portrait
# CHARACTER: Display Portrait
label julia_update_media:
    if current_location == jewelry_store:
        $ julia.change_image('julia_store_33')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label julia_examine:
    if julia.discussed_store:
        "The owner of the jewelry store.{nw}"
    else:
        "A clerk at the jewelry store.{nw}"
    if julia.discussed_her:
        extend " She used to be a partner in an accounting firm, before deciding she wanted a different type of life."
    else:
        extend " "
    return

# Talk to Character
label julia_talk:
    if current_location == jewelry_store:
        $ jewelry_store.visited_today = True
        rem tags 'no_hypnosis' from julia # allows subsequent tests to run correctly
        $ jewelry_store.visited_today = True # closes store after you leave
        $ jewelry_store.visit_count += 1
        if jewelry_store.visit_count == 1:
            call julia_jewelry_store_first_visit from _call_julia_jewelry_store_first_visit
        elif jewelry_store.visit_count == 2:
            call julia_jewelry_store_second_visit from _call_julia_jewelry_store_second_visit
        elif jewelry_store.visit_count > 2:
            call julia_jewelry_store_third_visit from _call_julia_jewelry_store_third_visit
        add tags 'trained_today' 'no_hypnosis' to julia # to shut off normal hypnosis actions
        call forced_movement(office_tower) from _call_forced_movement_174
    else:
        "You have nothing to say to her here."
    return

## Character Specific Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label julia_contact:
  $ julia.add_tags('trained_today', 'trained_this_week', 'home_visit_today')
  $ julia.home_visit_outfit += 1
  call forced_movement(outdoors) from _call_forced_movement_175
  summon julia
  if julia.home_visit_outfit > 4:
    $ julia.home_visit_outfit = 1
  if julia.home_visit_outfit == 1:
    wt_image julia_husband_1
    # first visit
    if julia.bikini_outfit == 0:
      husband_julia "Hi, you must be here to see Julia?"
      player.c "Yes"
      husband_julia "I'm her husband. Come on in. She's out back in the pool."
      husband_julia "Feel free to look all you want, but look with your eyes, not your hands. We're trying to start a family so don't go starting any funny stuff with her. Sometimes she gets carried away and forgets she's not on birth control."
      call julia_contact_outfit_1 from _call_julia_contact_outfit_1
    # subsequent visits
    else:
      husband_julia "Hi. Julia's out back in the pool."
      husband_julia "You can only look today. We're getting closer to her expected ovulation date, so no touching her today. Do you still want to come in?"
      $ title = "Do you still want to go in?"
      menu:
        "Yes, go see what she's wearing today":
          call julia_contact_outfit_1 from _call_julia_contact_outfit_1_1
        "No, come back some other week":
          "You head home. You can visit Julia again some other time."
  elif julia.home_visit_outfit == 2:
    wt_image julia_house_2_1
    julia.c "Hi! I was just about to get in the pool!"
    julia.c "Oh! I almost forgot."
    julia.c "My husband isn't home today because he's traveling for work, but he told me not to let any men touch me while he's away. It's close to the time when he's supposed to breed me, so if you come in, you have to promise not to touch me."
    julia.c "Do you want to come in and watch me?"
    $ title = "Do you still want to go in?"
    menu:
      "Yes, join Julia at the pool":
        call julia_contact_outfit_2_pool from _call_julia_contact_outfit_2_pool
      "Yes, but stay in the house":
        wt_image julia_house_2_27
        player.c "Yes, but let's stay here in the house Julia."
        julia.c "Oh. Okay. Do you like my outfit?  It's meant for the pool."
        $ title = "What do you tell her?"
        menu:
          "It looks good here":
            wt_image julia_house_2_28
            player.c "It looks good on you in here, too, Julia."
            julia.c "Yay! I'd hoped you'd like it. It looks good at the pool, too. Because, you know, it's for the pool."
            $ title = "What now?"
            menu:
              "You should take it off":
                call julia_contact_outfit_2_take_off from _call_julia_contact_outfit_2_take_off
              "In that case, let's go to the pool":
                call julia_contact_outfit_2_pool from _call_julia_contact_outfit_2_pool_1
              "Head Home":
                "It's a short visit, but you've seen enough of Julia and her bikini for today. Time to head home while you still have the energy to do something else."
          "You should take it off":
            call julia_contact_outfit_2_take_off from _call_julia_contact_outfit_2_take_off_1
          "In that case, let's go to the pool":
            call julia_contact_outfit_2_pool from _call_julia_contact_outfit_2_pool_2
      "No, come back some other week":
        "You head home.  You can visit Julia again some other time."
  elif julia.home_visit_outfit == 3:
    wt_image julia_husband_1
    if gloria.discussed_bimbo == 2:
      wt_image julia_husband_1
      husband_julia "Hi. Hey! Thank you for arranging the dinner date with Gloria and her husband. That was quite the surprise."
      husband_julia "Julia was so excited when she heard about the invitation. She knows Gloria and her husband from back when they were her clients."
      husband_julia "Gloria's always so well dressed and perfectly made up, she's been a bit of a role model for Julia. Julia was so nervous about seeing them in a social setting, she even wondered whether she should drop the bimbo routine for the evening."
      husband_julia "I told her no, she's a bimbo and she's staying that way."
      wt_image julia_club_pres_1
      husband_julia "{i}The afternoon of our dinner date, Julia booked herself into the beauty salon for a full make over.{/i}"
      wt_image julia_club_pres_2
      husband_julia "{i}She was so proud of how she looked as we drove over to their house.{/i}"
      julia.c "I hope they like me! The new me, I mean."
      husband_julia "Just keep your head shut off, bimbo brain. You're not their accountant anymore. Nobody wants to hear thoughts from you tonight."
      julia.c "Okay"
      wt_image julia_husband_1
      husband_julia "Over dinner, Gloria quietly filled me in on what you and she had discussed. I got so hard I could barely wait for the meal to end. It was only after we retired to the sitting room for an after dinner drink that I could get things started."
      wt_image julia_club_pres_3
      husband_julia "Bimbo brain, your make up isn't as nice as Gloria's. Let her and her husband fix it for you."
      julia.c "Uh, okay?"
      club_president.c "Hmmmm. Your husband's right. This doesn't really suit you."
      gloria.c "I know what the problem is. You've put on make up like a sophisticated business woman, but that's not who you are anymore. You're a stupid bimbo slut. Let me show you the type of make up that's appropriate for you now."
      julia.c "But will I still look pretty?"
      gloria.c "You'll look fuckable, which is all a bimbo can hope for. Your husband is going to have you fuck us before you go home. You want us to like the way you look while we fuck you, don't you?"
      julia.c "Uh, I guess."
      club_president.c "Don't guess. Don't think at all. Your husband is right, thinking doesn't suit you. When my wife tells you something, just say yes."
      julia.c "Okay.  Yes."
      club_president.c "Yes what?"
      julia.c "I don't remember."
      club_president.c "Perfect"
      wt_image julia_club_pres_4
      gloria.c "The biggest problem is your lipstick. You need a lot more, and a lot brighter. When a man looks at your face, the first thing he should see shouldn't be those big doe eyes of your you like to bat around. He should see your mouth. A nice round, juicy red mouth for sticking his cock into."
      julia.c "Won't that look trashy?"
      gloria.c "I hope so.  How does that look, honey?"
      club_president.c "Better, but it's too neat. When I look at a stupid slut, I want to see the lipstick all over her face. That way I know she's ready to fuck however I want to fuck her, and won't worry if I mess her up a bit while I'm doing so.  Let me show you.  Lie down."
      wt_image julia_club_pres_5
      julia.c "But lipstick is to make my lips pretty!  It shouldn't go on my face."
      husband_julia "Stop thinking, bimbo brain and let Gloria and her husband fix you up so you look nice and trashy so they feel like fucking you."
      julia.c "But ..."
      club_president.c "Shut up, bimbo, and let me get this lipstick all over your face. There. How does she look now, Gloria?"
      gloria.c "Like a trashy whore. It suits her."
      club_president.c "I agree. And trashy whores get cocks put inside them. Open up."
      wt_image julia_club_pres_6
      julia.c "Mmpphhhh"
      husband_julia "{i}Despite her humiliation - or maybe partly because of it - Julia laid there willingly and let him throat fuck her as he held her head still.{/i}"
      wt_image julia_club_pres_7
      gloria.c "Remember to put your lipstick back on after you suck cock. I'll hold it here for you and you put it on your lips. No hands."
      julia.c "But I'll ..."
      husband_julia "Just listen to her, bimbo brain."
      julia.c "Okay"
      husband_julia "Don't forget to thank Gloria for the make up tips, bimbo brain."
      wt_image julia_club_pres_8
      "{i}Julia wraps her lips around her former client's nipple and suckles her.{/i}"
      gloria.c "Mmmmm.  This is so much more enjoyable than listening to you prattle on about tax savings techniques."
      wt_image julia_club_pres_11
      gloria.c "Something else to remember is that lipstick isn't just for your face. You should put it everywhere you want a man to stick his cock."
      julia.c "Uh huh.  Lipstick goes where cocks go."
      gloria.c "I think this is finally getting through your thick skull."
      wt_image julia_club_pres_9
      gloria.c "Get my husband ready now. He wants to fuck me."
      wt_image julia_club_pres_10
      husband_julia "Make yourself useful, bimbo brain.  Show our hosts you're thankful for the nice dinner and the make up tips."
      wt_image julia_club_pres_12
      husband_julia "{i}Gloria and her husband seemed pretty happy with my wife.{/i}"
      wt_image julia_club_pres_13
      husband_julia "{i}I was pretty happy with her, too.{/i}"
      husband_julia "Come suck me off now, bimbo brain, and then we'll go home. I think our hosts will want to watch your trashy face taking my cock."
      julia.c "Okay"
      wt_image julia_husband_1
      husband_julia "She was so cute on the drive home, so humiliated at her treatment by Gloria and her husband but so pleased that I had enjoyed seeing her like that."
      husband_julia "I bent her over the hood of the car when we got into the driveway and fucked her where anyone in the neighborhood could watch if they wanted to, the lipstick still smeared over her face,  She came like a cat in heat and that only embarrassed her more."
      husband_julia "Anyway, I'm just about to fuck her again, as its around the time when she should be ovulating.  Did you want to come in and watch?"
      $ gloria.discussed_bimbo = 3
    else:
      husband_julia "Hi. I didn't know you were coming over. I was just about to have sex with my wife. We're trying to start a family and she's ovulating. Did you want to come in and watch?"
    $ title = "Do you still want to go in?"
    menu:
      "Yes, watch him fuck her":
        $ julia.husband_outfit += 1
        if julia.husband_outfit > 2:
          $ julia.husband_outfit = 1
        if julia.husband_outfit == 1:
          wt_image julia_husband_sex_1_1
          husband_julia "Come here bimbo brain. Your friend came to visit. He's going to watch while I breed you."
          julia.c "Oh!  Goodie!!"
          wt_image julia_husband_sex_1_9
          "The two of them ignore you as they strip down and Julia positions herself between her husband's legs."
          wt_image julia_husband_sex_1_2
          "That gives you the freedom to move around observe the mating from different angles."
          wt_image julia_husband_sex_1_3
          "Sucking her husband's cock has made Julia as wet as she's made him hard."
          wt_image julia_husband_sex_1_4
          "When she climbs up on top of him and he starts kissing her breasts, it's clear she's on the brink of cumming."
          julia.c "Ohhhh!  Oohhhhh!!"
          wt_image julia_husband_sex_1_5
          "One hard thrust of his cock combined with his tongue on her nipple and she's over the edge."
          julia.c "Ohhh!  OH!  I'm Cumminnnggg!!!"
          wt_image julia_husband_sex_1_6
          husband_julia "Turn around, bimbo brain. This position's best for making babies."
          "You're sure that's not true, but you can hardly blame him for wanting to look at her ass while he fucks her."
          wt_image julia_husband_sex_1_7
          husband_julia "Mmmhhhhhh!"
          julia.c "Oh yes!!  Fill me with your sperm!"
          wt_image julia_husband_sex_1_8
        elif julia.husband_outfit == 2:
          wt_image julia_husband_sex_2_8
          husband_julia "Come join me in my office, bimbo brain."
          julia.c "Is it time for me to be bred?"
          husband_julia "Yes.  Your friend is going to watch us."
          wt_image julia_husband_sex_2_1
          julia.c "Goodie!"
          "She drops to her knees and starts licking her husband's cock."
          wt_image julia_husband_sex_2_2
          "It doesn't take her long to get him ready for action."
          wt_image julia_husband_sex_2_3
          husband_julia "Ready to take my sperm, bimbo brain?"
          julia.c "Uh huh!"
          "She is, too.  Her pussy is glistening."
          wt_image julia_husband_sex_2_4
          "She moans as he enters her."
          julia.c "Ohhhhh"
          wt_image julia_husband_sex_2_5
          "A few hard strokes combined with his mouth on her nipple and she climaxes hard."
          julia.c "Ohhh  Oohhhhh!  OHH!  Oh!  OH!  I'm Cumminnnggg!!!"
          wt_image julia_husband_sex_2_6
          "Now it's his turn. He flips her over and pounds into her from behind. It doesn't take him long to cum."
          husband_julia "Mmmhhhhhhh"
          julia.c "Oh yes!!  Fill me with your sperm!"
          wt_image julia_husband_sex_2_7
        husband_julia "So what do you think of my pretty, bimbo brained Julia?"
        $ title = "What do you think of her?"
        menu:
          "She's too proud":
            if julia.discussed_pride == 0:
              player.c "She's too proud."
              husband_julia "How so?"
              player.c "Her hair, her make up. She's too pleased with herself for looking good."
              husband_julia "That's what I want from her. To make herself beautiful for me."
              player.c "Yeah, but she's also doing it for herself. She enjoys looking pretty. She shouldn't care so much about that, she should only care about making you happy."
              julia.c "I should be pretty! That's what I'm for. To be the most prettiest!"
              husband_julia "Hmmmmm. I get what you're saying, but she's right. I do want her to be the prettiest."
              julia.c "Yay!  I want that too!"
              "Her husband's not convinced, but you've planted a seed in his mind."
              # opens this conversation up again
              $ julia.discussed_pride = 1
            elif julia.discussed_pride == 1:
              player.c "I still think she's too proud."
              husband_julia "You said that before. I'm not sure I follow you."
              player.c "A bimbo shouldn't have airs. She's too full of herself. All that should matter to her is whether she's making you happy."
              player.c "Say you wanted to muss up her hair or smear her make up over her face. Just go ahead and do it. She shouldn't care."
              julia.c "No! Don't listen to him!! He's being a big meanie!! Don't make me unpretty! I should be the most prettiest girl ever!!"
              "Her husband says nothing, but you can see he's thinking."
              # opens up messing her up on a subsequent visit
              $ julia.discussed_pride = 2
            elif julia.discussed_pride == 2:
              player.c "I still think she's too proud. She could use a good messing up once in a while."
              husband_julia "You may be right. She is unduly concerned about looking good for its own sake."
              julia.c "Nuh huh! I'm supposed to be pretty all the time so that when you look at me you think good things about me. You don't want to see me unpretty! You might not like me."
              husband_julia "Bimbo brain, I will always love you. If I smear up your make up to see you messed up a bit, as long as it's what I want, that's all that should matter."
              julia.c "No! Don't make me unpretty!!"
            elif julia.discussed_pride == 3:
              # this is unlocked once you've messed her up once
              # this is if you subsequently had her play with Gloria and the Club President
              if gloria.discussed_bimbo == 3:
                player.c "I still think she's too proud."
                husband_julia "Maybe she should get another lesson on how to wear make up around other women."
                julia.c "Noooo. I'll look any way you want me to make you happy, but please don't make me look unpretty around other women again."
              # this is if the scene with Gloria and the Club President hasn't yet happened
              else:
                player.c "I still think she's too proud."
                husband_julia "I'm working on that. She's learning to put her make up on in a special way for me around the house."
                julia.c "Uh huh. Because I want to make you happy. Even if I have to look unpretty to do so."
                if gloria.session > 6:
                  "Her husband might enjoy watching Julia made 'unpretty' around a well dressed sophisticated woman. You could speak to Gloria the Club President's Wife about this sometime."
                  $ gloria.discussed_bimbo = 1
                  add tags 'something_to_discuss' to gloria
                  add tags 'gloria_other_talk_option_possible' to julia
                else:
                  "Her husband might enjoy watching Julia made 'unpretty' around a well dressed sophisticated woman, if you could find the right woman."
          "She needs obedience training":
            player.c "She needs obedience training."
            husband_julia "I know. She's a ditzy airhead and she does naughty things some times. She doesn't mean to. She's just so pretty and so stupid, sometimes she gets herself into trouble."
            player.c "I could train her for you."
            husband_julia "Nah.  For me, she's perfect just the way she is."
            julia.c "Ahhh .... You're so sweet!"
          "She thinks too much":
            player.c "She thinks too much."
            husband_julia "See, bimbo brain. He agrees with me. That's what I've been telling you. You need to stop thinking so much."
            julia.c "Uh huh. But sometimes I forget that I'm not supposed to think, and then I think of it."
            julia.c "And I'm not sure if I'm supposed to be thinking that I'm supposed to remember to not think, or not. It gets confusing."
            husband_julia "Just let your mind go blank, bimbo brain. When it gets confusing, just shut your head off. A vacant stare is your best look."
            julia.c "Okay!"
          "She's perfect":
            player.c "She's perfect."
            husband_julia "I think so too! Hear that, bimbo brain? Your friend likes you."
            julia.c "Ahhh .... You're both so sweet!"
        "You see your way out and head home."
        change player energy by -energy_short notify
      "No, come back some other week":
        "You head home. You can visit Julia again some other time."
  elif julia.home_visit_outfit == 4:
    wt_image julia_husband_1
    # this is if you've messed her up before
    if julia.discussed_pride == 3:
      husband_julia "Hi. Come on in."
      husband_julia "Julia's no longer ovulating, so you can go ahead and fool around with her today, if you want. Do you want me to send her to the bedroom or would you rather mess her up again?"
      $ title = "Do you want to go in?"
      menu:
        "Yes, mess her up again":
          player.c "Send her to me in the bathroom."
          wt_image julia_house_4_52
          "Julia enters the bathroom apprehensively."
          julia.c "Hi ... are you, ummmm ... are you going to adjust my make up again?  Because I think it looks really good just as it is!"
          wt_image julia_house_4_30
          "She bats her big doe eyes at you, but you're not having any of it."
          player.c "Off with your clothes.  On your knees.  Hands behind your back."
          wt_image julia_house_4_38
          "She gets into position and you push her head into the toilet."
          wt_image julia_house_4_36
          player.c "What are you?"
          julia.c "Ummm ... pretty?"
          wt_image julia_house_4_46
          player.c "No, you're a fucking mess, you dumb cunt."
          "You shove her head back into the toilet."
          wt_image julia_house_4_39
          player.c "What are you?  Your husband went back to his office, so he's not around to hear you.  Tell me what you are."
          julia.c "A fucking mess of a dumb cunt that's only good for sucking cock!"
          wt_image julia_house_4_47
          player.c "Pretty smart for an airhead, aren't you?  But you don't like being treated smart, so I'm going to treat you like the dumb cunt you want to be."
          player.c "Say it again so I know you've got it through your thick skull.  What are you?"
          julia.c "A fucking mess of a dumb cunt that's only good for sucking cock!"
          wt_image julia_house_4_48
          player.c "Once more, and this time show me that you mean it."
          julia.c "I'm a fucking mess of a dumb cunt that's only good for sucking cock!"
          wt_image julia_house_4_49
          player.c "Okay then, make yourself useful."
          "She attacks your cock like an animal."
          wt_image julia_house_4_50
          "She soon earns herself a face full of your cum."
          player.c "[player.orgasm_text]"
          wt_image julia_house_4_51
          julia.c "I don't like this game as much as the stupid and pretty bimbo game, but my husband likes the idea of me seeing me degraded once in a while."
          julia.c "He'd never really degrade me the way I can see you'd like to, but he has fun now smearing my make up around once in a while, so thanks for introducing this to him."
          player.c "I could degrade you for real if you wanted me to."
          julia.c "Nuh huh!  A stupid bimbo like me just wants to be pretty!  Even if sometimes my husband says pretty means being all messy."
          "You let her clean up and head for home."
          $ julia.blowjob_count += 1
          $ julia.facial_count += 1
          orgasm notify
        "Yes, wait for her in the bedroom":
          call julia_contact_outfit_4_wait_in_bedroom from _call_julia_contact_outfit_4_wait_in_bedroom
        "No, come back some other week":
          "You head home.  You can visit Julia again some other time."
    # this is if you haven't yet messed her up but he's ready to do so
    elif julia.discussed_pride == 2:
      husband_julia "Hi. Come on in."
      husband_julia "I've been thinking about what you've said. I would like to see Julia with her make up smeared and her hair askew for a change."
      husband_julia "Thing is, I'm not up to doing it myself. She looks at me with those big doe eyes and I can't bear to ruin her perfect appearance."
      husband_julia "I'd love to watch you do, it though. She's no longer ovulating, so you can have whatever fun with her you want, so long as you're okay with me joining in."
      husband_julia "What do you say?"
      $ title = "Do you want to go in?"
      menu:
        "Yes, take Julia down a peg":
          player.c "I'm going to go to the bathroom. Send her to me in there."
          wt_image julia_house_4_52
          "Julia arrives a few minutes later."
          julia.c "Ummm. Why are we in here?"
          player.c "To help you make your husband happy."
          wt_image julia_house_4_30
          julia.c "Oh. But, he's already happy with me. He says I'm perfect!"
          "She fixes her big doe eyes at you and bats them seductively."
          julia.c "How about we go to the bedroom and I can show you how perfect I am?"
          $ title = "Do those big doe eyes win you over?"
          menu:
            "Yes, wait for her in the bedroom":
              "You see what her husband means. It's impossible to say no to those eyes."
              player.c "Okay, Julia. Join me in the bedroom."
              wt_image julia_house_4_52
              julia.c "Yay! I'll go change to look even more pretty for you!"
              call julia_contact_outfit_4_wait_in_bedroom from _call_julia_contact_outfit_4_wait_in_bedroom_1
            "No, you're in the mood to be cruel":
              player.c "Perfect, huh? You think a silly little airhead like you knows what perfect is?"
              julia.c "Uh huh! Perfect is looking like the most prettiest girl ever!"
              player.c "What about the water in the toilet, is it perfect?"
              wt_image julia_house_4_52
              julia.c "Huh?  What do you mean."
              player.c "Kneel down.  Feel it.  Does it feel perfect."
              wt_image julia_house_4_53
              "She gets down in front of the toilet and tentatively touches the water with her hand."
              wt_image julia_house_4_31
              julia.c "Ewww. It's all dirty gross."
              player.c "No it's not, it's clean water."
              julia.c "Nuh huh. It's in a toilet."
              player.c "Don't you clean your toilet?"
              julia.c "Ummm. I think my husband gets someone to do that for us."
              player.c "So you don't clean the toilet yourself?"
              julia.c "Nuh huh! I'm supposed to be pretty! Not doing gross things like that."
              player.c "I hope your cleaners have done a good job for you. You think your job is to be pretty? Show me how you're doing."
              julia.c "I'll go put something pretty on!"
              player.c "No need. Just show me what you look like."
              julia.c "Ummm, you mean take my clothes off?"
              player.c "Yes"
              wt_image julia_house_4_32
              julia.c "Okay!"
              wt_image julia_house_4_33
              julia.c "If looking at my titties is making you all bothered, my husband said it's okay if I provide you some relief today."
              player.c "That's not needed, Julia. I'm not excited looking at you like this."
              julia.c "You're not?"
              player.c "No. Your husband and I have been talking. We both want to see you look pretty in a different way sometimes."
              julia.c "Oh? Ummm ... what do you mean?"
              player.c "Do you want to turn your husband and me on?"
              julia.c "By looking pretty! Yes!"
              wt_image julia_house_4_54
              player.c "Take off your pants, then kneel down and take a look at the toilet water again."
              julia.c "Ummm ... why?"
              player.c "Does it look pretty to you?"
              julia.c "No! It's toilet water, it's all gross."
              player.c "I don't agree. Take a closer look."
              wt_image julia_house_4_34
              "Taking her firmly by the head, you push her face into the toilet."
              wt_image julia_house_4_35
              julia.c "Nooo!!!!  My hair!!!  My make up!!!"
              player.c "Are starting to look a little better."
              wt_image julia_house_4_34
              "You shove her head back into the toilet."
              wt_image julia_house_4_36
              "When you pull her head up the second time, she's no longer screaming, just sobbing."
              julia.c "I want my husband!"
              wt_image julia_house_4_37
              husband_julia "I'm right here, bimbo brain."
              "Her husband steps into the doorway form the hallway where he's been monitoring your activities."
              julia.c "Don't let him do this! He's making me unpretty!!"
              husband_julia "He's doing exactly what I asked him to do. Showing you how a man likes you to wear your make up sometimes."
              julia.c "No! This isn't pretty."
              husband_julia "It's what I want, bimbo brain. Now put your arms behind your back so your friend can finish fixing up your make up the way I want to see you."
              wt_image julia_house_4_38
              julia.c "Nooo oh oh oohh"
              "Despite her mournful sobs, she puts her arms behind her back as her husband instructed, and you shove her face back in the toilet."
              wt_image julia_house_4_39
              player.c "Open your mouth. Ready to suck cock?"
              julia.c "Uh huh! Yes!"
              wt_image julia_house_4_40
              player.c "Good. Because now you're pretty enough to want relief from."
              julia.c "No. I'm not pretty now!"
              husband_julia "Yes, bimbo brain. You are. Look at your friend's hard cock."
              husband_julia "Stop trying to use your brain to think. You're too stupid for that."
              husband_julia "I say you look pretty like this, so you look pretty. Now suck your friend's cock to thank him for fixing your make up."
              wt_image julia_house_4_41
              julia.c "Are you sure I look pretty?"
              husband_julia "Stop thinking, bimbo brain, and do something you're good at. Suck his cock."
              wt_image julia_house_4_42
              "Julia starts sucking your cock with a sloppy enthusiasm that matches her current dishevelled state."
              player.c "Look, Julia. It isn't just me. Your husband likes you like this, too. You'd better suck his cock, too."
              wt_image julia_house_4_43
              "Between your cock and her husband's, she has her hands full ..."
              wt_image julia_house_4_44
              "...but she proves up to the challenge."
              player.c "[player.orgasm_text]"
              husband_julia "Mmmhhhhhhhh!"
              wt_image julia_house_4_45
              julia.c "Do I really look pretty?"
              husband_julia "Yes, bimbo brain, I like your make up and hair like this."
              "You leave Julia to her husband and head home."
              $ julia.blowjob_count += 2
              $ julia.facial_count += 2
              $ julia.discussed_pride = 3
              orgasm notify
        "No, come back some other week":
          "You head home.  You can visit Julia again some other time."
    # this is if you haven't advanced the pride storyline yet
    else:
      husband_julia "Hi. Come on in. You can head over to the bedroom there. I'll send Julia in."
      husband_julia "She's no longer ovulating, so you can go ahead and fool around with her today, if you want. Or just look at her. Whatever you prefer."
      $ title = "Do you want to go in?"
      menu:
        "Yes, wait for her in the bedroom":
          call julia_contact_outfit_4_wait_in_bedroom from _call_julia_contact_outfit_4_wait_in_bedroom_2
        "No, come back some other week":
          "You head home.  You can visit Julia again some other time."
  call character_location_return(julia) from _call_character_location_return_635
  call forced_movement(living_room) from _call_forced_movement_176
  return

label julia_contact_outfit_1:
  $ julia.bikini_outfit += 1
  if julia.bikini_outfit > 3:
    $ julia.bikini_outfit = 1
  if julia.bikini_outfit == 1:
    wt_image julia_bikini_1_1
    julia.c "Hi! You came to visit! Yay!!"
    wt_image julia_bikini_1_2
    julia.c "Do you like this bikini? I bought it special so you could see me in it."
    player.c "It's very nice, Julia."
    wt_image julia_bikini_1_3
    julia.c "So do you want to get in the water with me, or do you just want to look at me?"
    player.c "I didn't bring a bathing suit."
    julia.c "Normally that would be okay. You could just jump in the water starkers."
    julia.c "But you might get a hard on looking at me and that would be embarrassing for both of us, especially because my hubbie says I'm not supposed to touch any men right now, because I might get carried away and its almost time for him to breed me."
    wt_image julia_bikini_1_4
    julia.c "I'll just get out of the pool and join you up here where you can see me better. Is this okay?"
    $ title = "Is this good?"
    menu:
      "The bikini is a bit distracting":
        player.c "The bikini is a bit distracting, Julia."
        wt_image julia_bikini_1_6
        julia.c "Is that because my nipples are showing?"
        wt_image julia_bikini_1_7
        julia.c "I could just take the top off. Is this better?"
        $ title = "Is this better?"
        menu:
          "The bottoms are distracting too":
            player.c "The bottoms are distracting too, Julia."
            julia.c "Are they?  I just shaved my pussy so that the hairs wouldn't show through, but I guess you can still see my pretty pussy through them."
            wt_image julia_bikini_1_9
            julia.c "I'll take them off, but is seeing my bare pussy going to make you want to fuck me?"
            $ title = "Do you want to fuck her now?"
            menu:
              "Yes, I do want to fuck you":
                player.c "Yes, Julia. Your pretty pussy is so hot I do want to fuck you."
                wt_image julia_bikini_1_10
                julia.c "You should probably go, then."
                julia.c "Fucking would be fun but I can't let you put your thingie inside me right now, because then I might have your baby instead of my husband's, and he would be mad if that happened."
                "You take a last look at her body, then head for home."
              "I'll be able to control myself":
                player.c "Your pussy is really hot, Julia, but I'll be able to control myself."
                wt_image julia_bikini_1_14
                julia.c "My pussy does feel hot. Maybe I should put some water on it?"
                wt_image julia_bikini_1_11
                julia.c "Oh! That feels nice!"
                wt_image julia_bikini_1_12
                julia.c "Ohhh  Ohhhhh  OH!  I'm cumminnnggg!!!"
                wt_image julia_bikini_1_13
                julia.c "That wasn't very nice of me, making you watch that. You probably have a hard on now and I'm not allowed to even suck you off today."
                julia.c "If we had a conversation it might distract you, but I shouldn't talk because I just say silly things and it makes me use my brain, which I shouldn't do."
                julia.c "How about I just lie here and sunbathe and you can watch me until you're ready to go home and jerk off?"
                "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them. You watch Julia for a little while, then head home."
                $ julia.orgasm_count += 1
          "Yes, perfect":
            player.c "Yes, that's perfect Julia."
            wt_image julia_bikini_1_8
            julia.c "Oh goodie!"
            julia.c "You'll probably get a hard on looking at my titties like this.  I feel bad about that, especially because I'm not supposed to touch you or let you touch me right now."
            julia.c "If we had a conversation it might distract you, but I shouldn't talk because I just say silly things and it makes me use my brain, which I shouldn't do."
            julia.c "How about I just lie here and sunbathe and you can watch me until you're ready to go home and jerk off?"
            "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them.  You watch Julia for a little while, then head home."
      "This is perfect":
        player.c "This is perfect, Julia."
        wt_image julia_bikini_1_5
        julia.c "Oh goodie!"
        julia.c "I shouldn't talk because I just say silly things and it makes me use my brain, which I shouldn't do."
        julia.c "How about I just lie here and sunbathe and you can watch me until you're ready to go home and jerk off?"
        "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them.  You watch Julia for a little while, then head home."
  elif julia.bikini_outfit == 2:
    wt_image julia_bikini_2_1
    julia.c "Hi!  Do you like this bikini? It's yellow!"
    $ title = "Do you like her bikini?"
    menu:
      "It's very see through":
        player.c "It's very see through, Julia."
        wt_image julia_bikini_2_6
        julia.c "Oh. You can see too much of my nipples, can't you?"
        wt_image julia_bikini_2_7
        julia.c "I'll take the top off so it doesn't look so silly."
        $ title = "Is this good?"
        menu:
          "The bottoms look silly too":
            player.c "The bottoms look silly too, Julia."
            wt_image julia_bikini_2_9
            julia.c "Do they? I thought they looked nice."
            wt_image julia_bikini_2_10
            julia.c "Silly me. What do I know? I'll take them off so I look prettier and not so silly."
            wt_image julia_bikini_2_11
            julia.c "Now you won't be distracted by that silly bikini. You can watch me sun bathe like this until you need to go home and jerk off."
            "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them."
            "You watch Julia for a little while, then head home."
          "That looks good":
            player.c "That looks good, Julia."
            wt_image julia_bikini_2_8
            julia.c "Oh goodie! I'll sun bathe like this. You can look at me until you need to go home and jerk off."
            "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them."
            "You watch Julia for a little while, then head home."
      "It's very nice":
        player.c "It's very nice, Julia."
        wt_image julia_bikini_2_2
        julia.c "Oh goodie! I like it too! Do you want to watch me sunbathe face up ..."
        wt_image julia_bikini_2_3
        julia.c "... or face down?"
        $ title = "What do you prefer?"
        menu:
          "Face up":
            player.c "Face up is nice."
            wt_image julia_bikini_2_4
          "Face down":
            player.c "Face down is nice."
            wt_image julia_bikini_2_5
        julia.c "Okay! I'll just lie here and close my eyes. You can look at me until you need to go home and jerk off."
        "A lot of temptations cross your mind as you watch Julia soak up the sun, but with her husband working in his office inside, you decide its best not to act on them."
        "You watch Julia for a little while, then head home."
  elif julia.bikini_outfit == 3:
    wt_image julia_bikini_3_1
    julia.c "Hi! I was just about to get in the pool."
    wt_image julia_bikini_3_2
    julia.c "Oh no!"
    player.c "What's wrong?"
    wt_image julia_bikini_3_3
    julia.c "I forgot to put on a bathing suit! See?"
    $ title = "What do you tell her?"
    menu:
      "You can bathe in the nude":
        player.c "That's okay, Julia, you can bathe in the nude."
        wt_image julia_bikini_3_6
        julia.c "Yay!  Great idea!"
        wt_image julia_bikini_3_7
        julia.c "I don't even have to get in the pool! I'll just lie like this and bathe in the sun."
        "Hopefully Julia remembered to put sun block on literally all over. You watch her for a while, then head home."
      "You're very stupid":
        player.c "You're very stupid, Julia."
        wt_image julia_bikini_3_5
        julia.c "Thank you! But don't go making me all wet inside, because I'm not allowed to have you touch me today."
        wt_image julia_bikini_3_4
        julia.c "Maybe if I hold my leg up like this, the sun will dry out my wet, tingly insides."
        "Hopefully Julia remembered to put sun block on literally all over. You watch her for a while, then head home."
      "Wrap the towel around you":
        player.c "Wrap the towel around you, Julia."
        julia.c "Tee hee. Then how will I enjoy the sun, silly?"
        wt_image julia_bikini_3_8
        julia.c "Oh!  You mean like this."
        wt_image julia_bikini_3_9
        julia.c "Goodie! Now I can feel the sun on my titties, but I'm still covered up so you won't think I'm trying to tease you on a day that I'm not allowed to touch you."
        "You watch her for a while, then head home."
  change player energy by -energy_short notify
  return

label julia_contact_outfit_2_pool:
  player.c "Let's go to the pool."
  julia.c "Okay, but you have to promise not to touch me."
  player.c "I promise."
  wt_image julia_house_2_2
  julia.c "This water is really nice. Do you like seeing me in the water?"
  $ title = "Do you like her in the water?"
  menu:
    "You look great in the water":
      player.c "You look great in the water, Julia."
      wt_image julia_house_2_3
      julia.c "It feels great too! I could splash around all day!"
      wt_image julia_house_2_4
      julia.c "Ummm , you seem to have a big boner. This isn't exciting you too much, is it?"
      $ title = "What do you tell her?"
      menu:
        "I won't touch you, but come closer":
          player.c "I won't touch you, Julia, but come closer."
          wt_image julia_house_2_5
          julia.c "Why?  What are you going to do?"
          $ title = "What do you do?"
          menu:
            "Take out your cock":
              julia.c "I can't touch you, remember?"
              player.c "You don't have to. Just lie there."
              wt_image julia_house_2_7
              julia.c "Oh!"
              "She watches in fascination as you stroke your shaft. She even arches herself up out of the water, trying to get her face as close to your cock as possible as you approach climax."
              player.c "[player.orgasm_text]"
              julia.c "Ohhh!!"
              wt_image julia_house_2_8
              "Julia pulls herself up out of the pool, your jizz dripping down her face and hair."
              julia.c "You're smart! You got relief and we didn't even need to touch each other!"
              "You let her clean up and head for home."
              $ julia.facial_count += 1
              orgasm notify
            "Just watch her":
              player.c "I just want to watch you up close."
              wt_image julia_house_2_6
              julia.c "Oh!  Okay. When you've seen enough you can go home and jerk off."
              "You watch her for a bit, then head home."
              change player energy by -energy_short notify
        "I'll be fine, you just keep playing":
          player.c "I'll be fine, Julia, you just keep playing."
          wt_image julia_house_2_3
          julia.c "Okay. When you seen enough you can go home and jerk off."
          "You watch her for a bit, then head home."
          change player energy by -energy_short notify
    "You'd look nicer out of the water":
      player.c "You'd look nicer out of the water, Julia."
      wt_image julia_house_2_10
      julia.c "Would I?  This bikini is very see through when it gets wet."
      $ title = "What do you tell her?"
      menu:
        "She should take it off":
          player.c "You're right, Julia. That's distracting.  you should take it off."
          wt_image julia_house_2_12
          julia.c "Okay, but is this going to make you excited? Because I'm not supposed to touch you."
          $ title = "What do you tell her?"
          menu:
            "You're excited too Julia":
              player.c "You're excited too, Julia."
              julia.c "Am I?"
              player.c "Yes. Touch yourself between your legs. Do you feel how wet you are?"
              wt_image julia_house_2_17
              julia.c "Ohhh I am wet! Umm, is that just because of the water in the pool?"
              player.c "No. Your nipples are hard, too. Pinch them and see."
              wt_image julia_house_2_18
              julia.c "Ohhh! They are hard, and the more I pinch them, the harder they get!"
              wt_image julia_house_2_19
              julia.c "Ummm ... This is embarrassing because I'm not supposed to let you touch me. But I seem to have become horny."
              $ title = "What should she do?"
              menu:
                "Offer her your cock":
                  player.c "You could use my cock to relieve your horniness."
                  julia.c "But I'm not supposed to touch you or let you touch me."
                  player.c "Did your husband know you were horny when he told you that?"
                  julia.c "No, I don't think so."
                  player.c "Maybe he would have told you something else if he knew you were horny."
                  julia.c "Maybe. I am a stupid bimbo, so really, how can he expect me to understand all his rules?"
                  julia.c "He doesn't want me to think hard anyway. If he's going to tell me complicated things, he should be around to supervise me and make sure I don't get them wrong."
                  wt_image julia_house_2_23
                  julia.c "Could you put your cock right here please?"
                  player.c "Get out of the pool. I'm not going to get into the pool to fuck you."
                  wt_image julia_house_2_24
                  "She scrambles up onto a towel and you push yourself inside her. She's dripping wet, and already on the verge of cumming."
                  "It only takes a few strokes of your hard cock to take her over the edge."
                  julia.c "Ohh!!  Ohhh!!!!  OH!!  Oh I'm cumminngggg!!!!"
                  "Now it's your turn."
                  $ title = "Where do you want to cum?"
                  menu:
                    "Pull out":
                      wt_image julia_house_2_26
                      player.c "[player.orgasm_text]"
                      "As you cum, you pull out and deposit your load on top of her."
                      julia.c "Yay! You remembered to pull out. I got so excited I almost forgot I'm being bred this week. I'm glad you're not a stupid bimbo and remember the important things."
                    "Cum inside her":
                      wt_image julia_house_2_25
                      player.c "[player.orgasm_text]"
                      julia.c "Oh!  Why did you do that! You should have pulled out."
                      player.c "I forgot."
                      julia.c "Ooops. I forget things all the time too, but you shouldn't forget important things. If I have your baby instead of my husband's, he's going to be really mad with both of us."
                      julia.c "Especially you, because - well, I'm just a stupid bimbo."
                  "You let Julia pull herself together and head for home."
                  $ julia.sex_count += 1
                  $ julia.orgasm_count += 1
                  orgasm notify
                "Tell her to play with herself":
                  player.c "You should play with yourself, Julia."
                  wt_image julia_house_2_20
                  julia.c "Oh! Good idea!"
                  "She grabs her bikini and starts rubbing it between her legs."
                  wt_image julia_house_2_21
                  "Soon she's breathing hard as pinches her nipple and rubs her clit."
                  julia.c "Ohhh  Ohhhhhh  Oohhhhhhh"
                  wt_image julia_house_2_22
                  julia.c "Oh!  I'm cumminnnggg!!"
                  julia.c "Ohhh!!!  Wow!  That felt great!!"
                  julia.c "Thank you for reminding me what to do when I get horny.  I'm so silly, I forgot."
                  $ julia.masturbation_count += 1
                  $ julia.orgasm_count += 1
                  change player energy by -energy_short notify
            "I won't touch you, but come closer":
              player.c "I won't touch you, Julia, but come closer."
              wt_image julia_house_2_14
              julia.c "Why? What are you going to do?"
              $ title = "What do you do?"
              menu:
                "Take out your cock":
                  julia.c "I can't touch you, remember?"
                  player.c "You don't have to. Just lie there."
                  wt_image julia_house_2_16
                  julia.c "Oh!"
                  "She watches in fascination as you stroke your shaft. She even arches herself up out of the water, trying to get her face as close to your cock as possible as you approach climax."
                  player.c "[player.orgasm_text]"
                  julia.c "Ohhh!!"
                  wt_image julia_house_2_8
                  "Julia pulls herself up out of the pool, your jizz dripping down her face and hair."
                  julia.c "You're smart!  You got relief and we didn't even need to touch each other!"
                  "You let her clean up and head for home."
                  $ julia.facial_count += 1
                  orgasm notify
                "Just watch her":
                  player.c "I just want to watch you up close."
                  wt_image julia_house_2_15
                  julia.c "Oh!  Okay.  When you've seen enough you can go home and jerk off."
                  "You watch her for a bit, then head home."
                  change player energy by -energy_short notify
            "I'll be fine, you just play in the water":
              wt_image julia_house_2_13
              julia.c "Goodie! I can strike poses for you until you need to go home and jerk off."
              "You watch Julia for a bit and then head home."
              change player energy by -energy_short notify
        "That's okay":
          player.c "That's okay, Julia.  It looks nice like that."
          wt_image julia_house_2_9
          julia.c "Goodie!  Do just want to see me stand around like this?"
          $ title = "Is that what you want?"
          menu:
            "Yes, you look great":
              player.c "Yes, you look great."
              wt_image julia_house_2_11
              julia.c "You can look at my ass, too, if you want."
              "You watch Julia for a while, then head home."
              change player energy by -energy_short notify
            "No, have her lie down in front of you":
              player.c "No, lie down in front of me."
              wt_image julia_house_2_5
              julia.c "Why?  What are you going to do?"
              $ title = "What do you do?"
              menu:
                "Take out your cock":
                  julia.c "I can't touch you, remember?"
                  player.c "You don't have to. Just lie there."
                  wt_image julia_house_2_7
                  julia.c "Oh!"
                  "She watches in fascination as you stroke your shaft. She even arches herself up out of the water, trying to get her face as close to your cock as possible as you approach climax."
                  player.c "[player.orgasm_text]"
                  julia.c "Ohhh!!"
                  wt_image julia_house_2_8
                  "Julia pulls herself up out of the pool, your jizz dripping down her face and hair."
                  julia.c "You're smart! You got relief and we didn't even need to touch each other!"
                  "You let her clean up and head for home."
                  $ julia.facial_count += 1
                  orgasm notify
                "Just watch her":
                  player.c "I just want to watch you up close."
                  wt_image julia_house_2_6
                  julia.c "Oh! Okay. When you've seen enough you can go home and jerk off."
                  "You watch her for a bit, then head home."
                  change player energy by -energy_short notify
  return

label julia_contact_outfit_2_take_off:
  player.c "You're right. That really is a pool outfit. Since we're not at the pool, you should take it off."
  wt_image julia_house_2_29
  julia.c "Okay!"
  wt_image julia_house_2_30
  julia.c "I'll get these bottoms off and go change into something better."
  wt_image julia_house_2_31
  "She runs off to her bedroom. After a few minutes she reappears and jumps on the sofa."
  julia.c "These are better clothes for the house. They're not as pretty as the clothes I wear to the store, but my husband says I look nice in them."
  wt_image julia_house_2_32
  julia.c "Ummm ... I'm not good at talking, because it makes me use my brain. And there's no sun in the house, so you can't watch me sun bathe."
  julia.c "Do you just want to look at me in my clothes? Or should I take some of my clothes off?"
  julia.c "The only thing is I can't show you my titties, because that would get you all bothered and excited and I'm not supposed to touch a man when my husband says it's almost time to breed me."
  player.c "You already showed me your tits today, Julia."
  julia.c "I did?"
  player.c "Yes, when you took your bikini off."
  julia.c "Oh. You're probably horny now then, huh?"
  player.c "I am, so you may as well take your clothes off."
  wt_image julia_house_2_33
  julia.c "Okay. Can you help me with these jeans? They're really tight."
  player.c "Sure"
  wt_image julia_house_2_34
  julia.c "Thanks! I can get the top off myself!"
  wt_image julia_house_2_35
  player.c "And the panties."
  julia.c "Ummm. This is probably making you extra horny now."
  $ title = "What do you tell her?"
  menu:
    "I'm sure you can help with that":
      player.c "I'm sure you can help with that, Julia."
      julia.c "Nuh huh. My husband said not to touch any men or let any men touch me, because I'm getting fertile and sometimes I get carried away."
      player.c "I don't think he meant that you should leave a friend feeling badly."
      "You take out your cock."
      player.c "Look at my cock. See how hard and throbbing it is?"
      julia.c "Wow. Yeah, you are in a bad way."
      player.c "I'm sure your husband would want you to help me out, after the sight of your sexy body got me all hot and bothered."
      julia.c "I don't know. I'd have to think about that. I don't like thinking."
      player.c "Let me do the thinking for you, Julia. I'm a man. I know what your husband would want you to do."
      $ title = "What would her husband tell her?"
      menu:
        "Give me a tit job":
          player.c "Give me a tit job, Julia. I can't get you pregnant that way."
          wt_image julia_house_2_36
          julia.c "Okay!"
          "Julia takes off her top and kneels down in front of you, placing your cock between her soft breasts."
          wt_image julia_house_2_37
          "She pushes her tits together, burying your cock between them, and happily strokes up and down on your hard shaft."
          wt_image julia_house_2_38
          player.c "[player.orgasm_text]"
          "She smiles at you as you deposit your load on her chest."
          julia.c "Feel better now?"
          player.c "Much."
          "You let her clean herself up and head for home."
          $ julia.titfuck_count += 1
          orgasm notify
        "Give me a blow job":
          player.c "Give me a blow job, Julia. I can't get you pregnant that way."
          wt_image julia_house_2_39
          julia.c "Okay!"
          "Julia takes off her top and steps out of her pants and panties to come over and kneel in front of you, taking your cock between her soft lips."
          wt_image julia_house_2_40
          "She's a bit of a tease, licking and nibbling at the head of your cock and playing with your balls for a long time."
          wt_image julia_house_2_41
          "Eventually she gets around to some deep throated sucking."
          wt_image julia_house_2_42
          "You have her kneel up and reward her with a mouth of hot jizz."
          player.c "[player.orgasm_text]"
          wt_image julia_house_2_43
          julia.c "Feel better now?"
          player.c "Much."
          "She smiles and gives your cock a kiss. Then you head for home."
          $ julia.blowjob_count += 1
          orgasm notify
        "Give me your ass":
          player.c "Give me your ass, Julia. I can't get you pregnant that way."
          julia.c "Oh!  Good idea!"
          wt_image julia_house_2_44
          "She pulls off her top and steps out of her pants and panties. Then she kneels down and presents her ass to you, reaching back with her hands to pull her cheeks apart to give you easier access."
          wt_image julia_house_2_45
          "She's had men back here before. Her body quickly relaxes, letting you push deep inside her. She pushes her ass back against you, fucking your cock as much as you're fucking her."
          wt_image julia_house_2_46
          julia.c "Oohhhh"
          "She likes this, and she's not the only one. You're soon ready to cum."
          $ title = "Where do you want to cum?"
          menu:
            "In her ass":
              wt_image julia_house_2_47
              player.c "[player.orgasm_text]"
              "She moans as she feels your hot load filling her bowels."
              julia.c "Ohhhhhh!"
              wt_image julia_house_2_48
              julia.c "Feel better now?"
              player.c "Much."
              "She runs to the bathroom as your jizz starts to drip out of her ass, and you head for home."
            "In her mouth":
              wt_image julia_house_2_42
              "You pull your cock out of her ass."
              player.c "Turn around Julia."
              "She understand immediately what you want. Seemingly unconcerned that your cock was just in her shithole, she wraps her lips around your shaft as you empty your load into her."
              player.c "[player.orgasm_text]"
              wt_image julia_house_2_43
              julia.c "Feel better now?"
              player.c "Much."
              "She smiles and gives your cock a kiss.  Then you head for home."
              $ julia.swallow_count += 1
          $ julia.anal_count += 1
          orgasm notify
        "Let me fuck you":
          player.c "He'd want you to fuck me."
          julia.c "Ummm ... really?"
          player.c "Sure. It's the fastest way to relieve my horniness. As long as I pull out before I cum, you can't get pregnant."
          julia.c "I'm pretty sure this is something he wouldn't want me to do."
          player.c "Julia, hasn't your husband told you not to think so much?"
          julia.c "Uh huh"
          player.c "So are you trying to think your way through this situation?"
          julia.c "It is complicated."
          player.c "I know, but look at my cock. See how excited it is at the sight of your sexy body? You don't have to think to know what needs to be done to make me feel better."
          julia.c "I guess. I am a stupid bimbo, so really, how can he expect me to understand all his rules?"
          julia.c "He doesn't want me to think hard anyway. If he's going to tell me complicated things, he should be around to supervise me and make sure I don't get them wrong."
          wt_image julia_house_2_49
          "Julia pulls off her top and steps out of her pants and panties, then lies down and spreads her legs. You push yourself into her quickly, before she has a chance to change her mind, but you didn't need to worry about that. "
          "She's soaking wet. Looking at your cock while you listening to you treat her like the stupid bimbo she aspires to be has her eager for the feel of your cock inside her. She moans as you enter her."
          julia.c "Oohhhh"
          wt_image julia_house_2_50
          "It only takes few hard thrusts to bring her to climax."
          julia.c "Oohhh!  Ooohhhh!!  OH!  Oh!  OHH!  I'm cumminnnggggg!!"
          "Now it's your turn."
          $ title = "Where do you want to cum?"
          menu:
            "Pull out":
              wt_image julia_house_2_26
              player.c "[player.orgasm_text]"
              "As you cum, you pull out and deposit your load on top of her."
              julia.c "Yay! You remembered to pull out. I got so excited I almost forgot I'm being bred this week. I'm glad you're not a stupid bimbo and remember the important things."
            "Cum inside her":
              wt_image julia_house_2_51
              player.c "[player.orgasm_text]"
              julia.c "Oh! Why did you do that! You should have pulled out."
              player.c "I forgot."
              julia.c "Ooops. I forget things all the time too, but you shouldn't forget important things. If I have your baby instead of my husband's, he's going to be really mad with both of us."
              julia.c "Especially you, because - well, I'm just a stupid bimbo."
          $ julia.sex_count += 1
          $ julia.orgasm_count += 1
          orgasm notify
    "I'm fine.  I'll be going now.":
      player.c "I'm fine, Julia. I'll be heading home now."
      julia.c "Okay. Thanks for visiting! I hope you come back soon!"
      change player energy by -energy_short notify
  return

label julia_contact_outfit_4_wait_in_bedroom:
  wt_image julia_house_4_1
  julia.c "Hi!  My husband says I can do whatever you want me to do today."
  julia.c "What do you want me to do?  Please don't ask me to chat. I don't like conversations because I have to think."
  julia.c "Maybe I could look pretty for you?"
  $ julia.look_pretty = False
  $ julia.look_naked = False
  $ julia.look_sexy = False
  $ julia.pose_sexy = False
  $ julia.this_is_fine = False
  $ julia.get_on_knees = False
  $ title = "What do you want her to do?"
  menu menu_julia_contact_outfit_4_bedroom:
    "Look sexy" if not julia.look_sexy and julia.look_pretty:
      wt_image julia_house_4_7
      julia.c "Goodie! I can look sexy like this..."
      wt_image julia_house_4_8
      julia.c "... or like this. What look do you want?"
      $ julia.look_sexy = True
      jump menu_julia_contact_outfit_4_bedroom
    "Look pretty" if not julia.look_pretty:
      player.c "Yes, Julia. Show me how pretty you are."
      wt_image julia_house_4_2
      julia.c "Yay! I have nice undies on. I'll show you."
      wt_image julia_house_4_3
      julia.c "See how pretty they are!"
      julia.c "The bra is see through so you can see my nipples. I thought the underwear was see through too, but it isn't. Silly me! It's still pretty, though, even if you can't see my pussy."
      julia.c "Do you want to see me look sexy for you?"
      $ julia.look_pretty = True
      jump menu_julia_contact_outfit_4_bedroom
    "Like this is fine" if not julia.this_is_fine and julia.look_sexy:
      player.c "Like this is fine."
      julia.c "Okay. Are you just going to look at me, or did you want me to ... you know."
      $ julia.this_is_fine = True
      jump menu_julia_contact_outfit_4_bedroom
    "Get back on her knees" if not julia.get_on_knees and julia.look_sexy:
      player.c "Get back on your knees."
      wt_image julia_house_4_7
      julia.c "Okay. Are you just going to look at me, or did you want me to ... you know."
      $ julia.get_on_knees = True
      jump menu_julia_contact_outfit_4_bedroom
    "Look naked" if not julia.look_naked:
      player.c "I'd rather you looked naked for me."
      if julia.look_pretty:
        wt_image julia_house_4_4
      elif julia.look_sexy:
        wt_image julia_house_4_9
      else:
        wt_image julia_house_4_5
      julia.c "Oh. Okay. I'll just get this off."
      wt_image julia_house_4_6
      julia.c "Is this better? Or if you want, I can pose sexy for you."
      $ julia.look_naked = True
      jump menu_julia_contact_outfit_4_bedroom
    "Pose sexy for me" if not julia.pose_sexy and julia.look_naked:
      player.c "Sure, pose sexy for me, Julia."
      wt_image julia_house_4_10
      julia.c "Goodie! I can look sexy like this ..."
      wt_image julia_house_4_11
      julia.c "... or this ..."
      wt_image julia_house_4_12
      julia.c "... or this ..."
      wt_image julia_house_4_13
      julia.c "... or this!"
      julia.c "Ummm ... do you need some relief now, after watching me be all sexy?"
      $ title = "What do you want?"
      $ julia.pose_sexy = True
      jump menu_julia_contact_outfit_4_bedroom
    "Use your tits on my cock" if julia.look_naked or julia.this_is_fine or julia.get_on_knees:
      player.c "What I'd really like is to see your tits rubbing against my cock."
      julia.c "Oh! I suppose I have made your cock all hard and bothered, huh?"
      if not julia.look_naked:
        wt_image julia_house_4_9
        "She rolls over and pulls off her clothes."
      wt_image julia_house_4_17
      "Leaning over, Julia brushes her tits against the tip of your cock."
      wt_image julia_house_4_18
      "Then she leans over further and wraps her breasts around your cock, stroking them up and down the length of your shaft."
      wt_image julia_house_4_19
      "When she senses you're close to cumming, she bites her lip and wraps her hand around your cock ..."
      wt_image julia_house_4_20
      "... and pumps your load out of your balls and into her waiting mouth."
      player.c "[player.orgasm_text]"
      julia.c "Mmmm.  Does that feel better?"
      player.c "Much"
      "You let Julia get redressed and head for home."
      $ julia.titfuck_count += 1
      $ julia.swallow_count += 1
      orgasm notify
    "Suck my cock" if julia.look_naked or julia.this_is_fine or julia.get_on_knees:
      player.c "What I'd really like is to see you suck my cock."
      julia.c "Oh! I suppose I have made your cock all hard and bothered, huh?"
      if not julia.look_naked:
        wt_image julia_house_4_9
        "She rolls over and pulls off her clothes."
      wt_image julia_house_4_14
      "Julia drops own on all fours and takes your cock into her mouth."
      wt_image julia_house_4_15
      "Closing her eyes, she proceeds to give you a slow, sexy blowjob."
      wt_image julia_house_4_16
      "When you're ready to cum, she looks up at you, watching you as you unload into her mouth."
      player.c "[player.orgasm_text]"
      julia.c "Mmmm.  Does that feel better?"
      player.c "Much."
      "You let Julia get redressed and head for home."
      $ julia.blowjob_count += 1
      $ julia.swallow_count += 1
      orgasm notify
    "Fuck me doggy style" if julia.look_naked or julia.this_is_fine or julia.get_on_knees:
      player.c "What I'd really like is to fuck you from behind."
      julia.c "Oh!  I suppose I have made your cock all hard and bothered, huh?"
      if not julia.look_naked:
        wt_image julia_house_4_9
        "She rolls over and pulls off her clothes."
      wt_image julia_house_4_13
      "Julia gets down on all fours and presents her behind to you."
      julia.c "Is this how you want me?"
      player.c "Perfect"
      wt_image julia_house_4_21
      "She's already wet. You push yourself into her easily, eliciting a deep moan."
      julia.c "Oohhhh"
      wt_image julia_house_4_22
      "Grabbing her by the hips, you start pounding into her, faster and faster, as her moans grow louder."
      julia.c "oohhh  ooohhhh!   ooohhhh!!   oooohhhhh!!!"
      wt_image julia_house_4_23
      julia.c "Ohhh!!  OH!  Oh I'm cumminnggg!!"
      "She's not the only one. You unload your sperm deep inside her."
      player.c "[player.orgasm_text]"
      wt_image julia_house_4_24
      julia.c "Ummm ... Were you supposed to pull out?"
      player.c "It's okay.  Your husband says you're not ovulating now."
      julia.c "Oh. Goodie! That was fun!"
      "You let her dress and head for home."
      $ julia.sex_count += 1
      $ julia.orgasm_count += 1
      orgasm notify
    "Spread your legs" if julia.look_naked or julia.this_is_fine or julia.get_on_knees:
      player.c "What I'd really like is for you to spread your legs."
      julia.c "So you can look at my pussy?"
      player.c "So I can fuck your pussy."
      julia.c "Oh! I suppose I have made your cock all hard and bothered, huh?"
      if not julia.look_naked:
        wt_image julia_house_4_9
        "She rolls over and pulls off her clothes."
      wt_image julia_house_4_12
      "Julia spreads her legs and her pussy."
      julia.c "Is this how you want me?"
      player.c "Almost.  Lie back"
      wt_image julia_house_4_25
      "She's already wet.  You push yourself into her easily, eliciting a deep moan."
      julia.c "Oohhhh"
      player.c "Lift your legs."
      wt_image julia_house_4_26
      julia.c "Okay"
      "You start thrusting into her, faster and faster, as her moans grow louder."
      julia.c "oohhh  ooohhhh!   ooohhhh!!   oooohhhhh!!!"
      wt_image julia_house_4_27
      julia.c "Ohhh!!  OH!  Oh I'm cumminnggg!!"
      "Now it's your turn."
      $ title = "Where do you want to cum?"
      menu:
        "Inside her":
          wt_image julia_house_4_28
          player.c "[player.orgasm_text]"
          "You unload your seed deep inside her."
          julia.c "Ummm ... Were you supposed to pull out?"
          player.c "It's okay. Your husband says you're not ovulating now."
          julia.c "Oh. Goodie! That was fun!"
          "You let her dress and head for home."
        "On her":
          wt_image julia_house_4_29
          player.c "[player.orgasm_text]"
          "You pull out and spurt your load over her."
          julia.c "Yay! You remembered to pull out."
          player.c "It would have been okay. Your husband says you're not ovulating now."
          julia.c "Oh. Well, that was fun anyway. And you didn't get any cum in my hair or make up!"
          "You let her dress and head for home."
      $ julia.sex_count += 1
      $ julia.orgasm_count += 1
      orgasm notify
    "I've seen enough" if julia.look_naked or julia.this_is_fine or julia.get_on_knees:
      player.c "That's okay. I've seen enough, Julia."
      julia.c "Oh. Okay. I hope you like what you've seen!"
      "You take another close look then head for home."
      change player energy by -energy_short
  return

## Character Specific Objects
# Jewelry Store
# OBJECT: Jewelry Store
label julia_jewelry_store_first_visit:
    $ title = "What do you want to talk to her about?"
    menu:
        "Hypnotize her" if player.can_hypno(julia):
            call julia_jewelry_store_hypnotize_her from _call_julia_jewelry_store_hypnotize_her
            $ title = "What do you want to talk to her about?"
            menu:
                "Ask about the store":
                    call julia_jewelry_store_about_store from _call_julia_jewelry_store_about_store
                "Ask about her":
                    call julia_jewelry_store_about_her from _call_julia_jewelry_store_about_her
        "Ask about seeing her bra":
            player.c "Well could I at least see your bra?"
            julia.c "Hmmm"
            julia.c "Okay. But only because my bra is covering up my nipples. If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
            julia.c "The building management has already warned me about that."
            wt_image julia_store_4
            "She steps out from around the counter and pulls down the top of her dress, giving you a good look at her bra."
            $ julia.discussed_bra = True
            $ title = "What do you want to talk to her about?"
            menu:
                "Ask about the store":
                    call julia_jewelry_store_about_store from _call_julia_jewelry_store_about_store_1
                "Ask about her":
                    call julia_jewelry_store_about_her from _call_julia_jewelry_store_about_her_1
        "Ask what she can show you":
            player.c "Well what can you show me?"
            julia.c "Hmmm"
            julia.c "I could show you my panties"
            wt_image julia_store_5
            "She steps out from around the counter."
            julia.c "This is okay because they're not see through."
            wt_image julia_store_6
            julia.c "I did remember not to wear see through panties, didn't I?"
            player.c "Yes, it's okay. Those aren't see through."
            wt_image julia_store_7
            julia.c "Okay, good. Because the building management got mad at me for showing off my see through panties."
            $ julia.discussed_panties = True
            $ title = "What do you want to talk to her about?"
            menu:
                "Ask about the store":
                    call julia_jewelry_store_about_store from _call_julia_jewelry_store_about_store_2
                "Ask about her":
                    call julia_jewelry_store_about_her from _call_julia_jewelry_store_about_her_2
        "Ask about the store":
            call julia_jewelry_store_about_store from _call_julia_jewelry_store_about_store_3
        "Ask about her":
            call julia_jewelry_store_about_her from _call_julia_jewelry_store_about_her_3
    $ julia.temporary_count = 1
    while julia.temporary_count == 1:
        call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_15
    return

label julia_jewelry_store_second_visit:
    wt_image julia_store_10
    if julia.hypno_count > 0:
        julia.c "Hi! Are you going to use your hypno-thingie on me again?"
        player.c "I told you to forget that I had hypnotized you."
        julia.c "Did you?  I must have forgotten you told me that. I forget a lot of things! So, are you going to use your hypno-thingie on me again?"
        if not player.can_hypno(julia):
            player.c "I can't. I can only hypnotize you once per week. Additional sessions aren't effective."
            julia.c "Oh. Okay. Did you come back to look at me or to buy something?"
            $ title = "What do you want?"
        else:
            $ title = "What do you do?"
        $ julia.talk_again = False
        menu menu_julia_jewelry_store_second_visit:
            "Hypnotize her again" if player.can_hypno(julia) and not julia.talk_again:
                call focus_image from _call_focus_image_66
                julia.c "Ooooo  it's still so pretty!"
                player.c "Listen to me, Julia. Listen to my words. Only my words, now, Julia. Only my words."
                wt_image julia_store_8
                player.c "We are going to chat, Julia. We should be comfortable when we chat. Show me your breasts so we are both comfortable while we chat."
                julia.c "Okay. You like looking at my tits, don't you?"
                wt_image julia_store_9
                "She pulls off her dress and pulls down her bra, displaying her breasts."
                player.c "Yes, Julia, I like looking at your tits. It makes me horny. Your body is so sexy, Julia, it's very frustrating. You feel bad for me. You want to make me feel better."
                julia.c "Nuh huh. You're not tricking me like that. I'm showing you my tits because of you and your hypno-thingie. You shouldn't be using that to get women to show you your breasts. If you're horny now, that's your fault."
                "You can't get any further with Julia on this path today. You may as well ask her some questions."
                $ julia.hypno_session()
                $ julia.talk_again = True
                $ title = "What do you want?"
                jump menu_julia_jewelry_store_second_visit
            "Look at her":
                player.c "I'd love to take a look at you."
                julia.c "Oh goodie! I like showing my body off. The only thing is, I can't show you too much, because the building management gets mad at me."
                wt_image julia_store_5
                "She steps out from around the counter."
                julia.c "But I can show you my panties. This is okay because they're not see through."
                wt_image julia_store_6
                player.c "I did remember not to wear see through panties, didn't I?"
                player.c "Yes, it's okay. Those aren't see through."
                wt_image julia_store_7
                julia.c "Okay, good. Because the building management got mad at me for showing off my see through panties."
                julia.c "I can show you my bra too, but only because my bra is covering up my nipples."
                wt_image julia_store_11
                "She steps out of her dress and stands in front of you in just her bra and panties."
                julia.c "If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
                julia.c "The building management has already warned me about that."
                $ julia.discussed_bra = True
                $ julia.discussed_panties = True
            "Just talk with her":
                pass
    else:
        if julia.discussed_bra:
            julia.c "Hi! Did you want to see my bra again or are you just here to buy something?"
        if julia.discussed_panties:
            julia.c "Hi! Did you want to see my panties again or are you just here to buy something?"
        else:
            julia.c "Hi! Did you come back to look at me or to buy something"
        $ title = "What do you want?"
        menu:
            "Ask to see her bra" if not julia.discussed_bra:
                player.c "I'd love to see your bra."
                julia.c "Okay!"
                wt_image julia_store_4
                "She steps out from around the counter and pulls down the top of her dress, giving you a good look at her bra."
                julia.c "I can show you my panties, too.  This is okay because they're not see through."
                wt_image julia_store_11
                "She steps out of her dress and stands in front of you in just her bra and panties."
                julia.c "I did remember not to wear see through panties, didn't I?"
                player.c "Yes, it's okay. Those aren't see through."
                julia.c "Okay, good. Because the building management got mad at me for showing off my see through panties."
                $ julia.discussed_bra = True
            "Ask to see her panties" if not julia.discussed_panties:
                player.c "I'd love to see your panties."
                julia.c "Okay!"
                wt_image julia_store_7
                "She steps out from behind the counter and pulls up her dress."
                julia.c "I can show you my bra too, but only because my bra is covering up my nipples."
                wt_image julia_store_11
                "She steps out of her dress and stands in front of you in just her bra and panties."
                julia.c "If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
                julia.c "The building management has already warned me about that."
                $ julia.discussed_panties = True
            "Look at her" if not julia.discussed_bra and not julia.discussed_panties:
                player.c "I'd love to take a look at you."
                julia.c "Oh goodie! I like showing my body off. The only thing is, I can't show you too much, because the building management gets mad at me."
                wt_image julia_store_5
                "She steps out from around the counter."
                julia.c "But I can show you my panties. This is okay because they're not see through."
                wt_image julia_store_6
                player.c "I did remember not to wear see through panties, didn't I?"
                player.c "Yes, it's okay.  Those aren't see through."
                wt_image julia_store_7
                julia.c "Okay, good.  Because the building management got mad at me for showing off my see through panties."
                julia.c "I can show you my bra too, but only because my bra is covering up my nipples."
                wt_image julia_store_11
                "She steps out of her dress and stands in front of you in just her bra and panties."
                julia.c "If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
                julia.c "The building management has already warned me about that."
                $ julia.discussed_bra = True
                $ julia.discussed_panties = True
            "Hypnotize her" if player.can_hypno(julia):
                call julia_jewelry_store_hypnotize_her from _call_julia_jewelry_store_hypnotize_her_1
                "You may as well ask her some questions."
            "Just talk with her":
                pass
    $ title = "What do you want to talk to her about?"
    menu:
        "Ask about her" if not julia.discussed_her:
            call julia_jewelry_store_about_her from _call_julia_jewelry_store_about_her_4
        "Ask about store" if not julia.discussed_store:
            call julia_jewelry_store_about_store from _call_julia_jewelry_store_about_store_4
    $ julia.temporary_count = 1
    while julia.temporary_count == 1:
        call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_16
    return

label julia_jewelry_store_third_visit:
    wt_image julia_store_10
    if julia.hypno_count > 0:
        if julia.hypno_count == 1:
            julia.c "Hi! Are you going to use your hypno-thingie on me again?"
            player.c "I told you to forget that I had hypnotized you."
            julia.c "Did you? I must have forgotten you told me that. I forget a lot of things! So, are you going to use your hypno-thingie on me again?"
            if not player.can_hypno(julia):
                player.c "I can't. I can only hypnotize you once per week.  Additional sessions aren't effect."
                julia.c "Oh. Okay. So did you just want to look at me or did you want to buy something?"
                $ title = "What do you want?"
            else:
                $ title = "What do you do?"
            $ julia.talk_again = False
            menu menu_julia_jewelry_store_third_visit:
                "Hypnotize her again" if player.can_hypno(julia) and not julia.talk_again:
                    # this is always second hypnosis session
                    call focus_image from _call_focus_image_67
                    julia.c "Ooooo  it's still so pretty!"
                    player.c "Listen to me, Julia. Listen to my words. Only my words, now, Julia. Only my words."
                    wt_image julia_store_8
                    player.c "We are going to chat, Julia. We should be comfortable when we chat. Show me your breasts so we are both comfortable while we chat."
                    julia.c "Okay. You like looking at my tits, don't you?"
                    wt_image julia_store_9
                    "She pulls off her dress and pulls down her bra, displaying her breasts."
                    player.c "Yes, Julia, I like looking at your tits. It makes me horny. Your body is so sexy, Julia, it's very frustrating. You feel bad for me. You want to make me feel better."
                    julia.c "Nuh huh. You're not tricking me like that. I'm showing you my tits because of you and your hypno-thingie. You shouldn't be using that to get women to show you your breasts. If you're horny now, that's your fault."
                    "You can't get any further with Julia on this path today. You may as well ask her some questions."
                    $ julia.hypno_session()
                    $ julia.talk_again = True
                    $ title = "What do you want?"
                    jump menu_julia_jewelry_store_third_visit
                "Look at her":
                    call julia_jewelry_store_third_visit_look from _call_julia_jewelry_store_third_visit_look
                "Just talk with her":
                    call julia_jewelry_store_third_visit_talk from _call_julia_jewelry_store_third_visit_talk
        else:
            if donna.ready_for_julia >= 3:
                julia.c "Hi!  I like Donna!"
                julia.c "Are you going to use your hypno-thingie on me again?"
            else:
                julia.c "Hi! Are you going to use your hypno-thingie on me again?"
            if not player.can_hypno(julia):
                player.c "I can't. I can only hypnotize you once per week. Additional sessions aren't effective."
                julia.c "Oh. Okay. So did you just want to look at me or did you want to buy something?"
                $ title = "What do you want?"
            else:
                $ title = "What do you do?"
            menu:
                "Hypnotize her some more" if player.can_hypno(julia):
                    # this is her third+ hypnosis
                    $ julia.hypno_session()
                    player.c "Yes, Julia, I am."
                    julia.c "Okay. Let me get my tits out."
                    wt_image julia_store_9
                    "She comes around from behind the counter and presents her bare breasts to you."
                    julia.c "Oh! Was I supposed to wait until you hypnotized me before I showed you my tits?"
                    player.c "That's okay, Julia. Look at this now."
                    call focus_image from _call_focus_image_68
                    julia.c "It's so shiny!"
                    player.c "Listen to me, Julia. Listen to me. Only me now. Only my words."
                    wt_image julia_store_9
                    $ title = "What do you want to do with her?"
                    menu menu_julia_hypnotized_some_more:
                        "Have her undress completely" if not julia.naked_now:
                            player.c "You're wearing too much clothing, Julia."
                            julia.c "You're right. That's because I'm in the store."
                            player.c "I want to see your naked body and you want to show me your naked body. Take the rest of your clothes off Julia."
                            julia.c "I'll get in trouble."
                            player.c "You're thinking too much, Julia. Don't think. Just do what feels good. It will feel good to show me your naked body."
                            julia.c "You're right!  I overthink things a lot. My husband says I need to stop thinking so much."
                            wt_image julia_store_12
                            "She removes her bra and panties and stands naked in front of you."
                            $ julia.naked_now = True
                            $ title = "What do you want to do with her?"
                            call menu_julia_hypnotized_some_more from _call_menu_julia_hypnotized_some_more
                        "Have sex with her":
                            player.c "The sight of your body is turning me on, Julia. My cock is very hard. You feel bad for me. Your sexy body is exciting me and making me horny. You should do something to help me feel better."
                            julia.c "That's your fault for hypnotizing me and making me show you my body."
                            player.c "You showed me your tits before I hypnotized you, Julia."
                            julia.c "I did? I don't remember that."
                            player.c "Yes, you did. You got excited when I said I was going to hypnotize you again and you took out your tits before I could hypnotize you."
                            julia.c "That's because I knew you would make me show them to you once I was hypnotized."
                            player.c "That doesn't matter. You're the one who showed me your beautiful tits and I didn't make you do it. Now I have a hard on, Julia, and its because you're such a sexy tease."
                            julia.c "Oh. Do you want me to give you a blow job to relieve the pressure in your cock?"
                            if julia.hypno_bj:
                                $ title = "What do you want?"
                                menu:
                                    "A blow job":
                                        player.c "A blow job would be very nice, Julia."
                                        if julia.naked_now:
                                            wt_image julia_store_14
                                        else:
                                            wt_image julia_store_13
                                        "She kneels down and takes out your cock."
                                        if julia.naked_now:
                                            "Naughtily, she sneaks a hand between her legs and plays with herself while she's blowing you."
                                            wt_image julia_store_16
                                        else:
                                            wt_image julia_store_15
                                        "She proceeds to give you a sloppy, enthusiastic blow job, low on technique but high on energy."
                                        if julia.naked_now:
                                            wt_image julia_store_18
                                        else:
                                            wt_image julia_store_17
                                        "When you're ready to cum, she looks up at you and prepares to receive your load."
                                        player.c "[player.orgasm_text]"
                                        wt_image julia_store_19
                                        julia.c "Do you feel better now?"
                                        player.c "Yes, Julia. Much better."
                                        julia.c "Oh goodie!  "
                                        julia.c "That was tiring. I have to go now. Bye bye!"
                                        $ julia.blowjob_count += 1
                                        $ julia.facial_count += 1
                                        $ julia.hypno_bj = True
                                        orgasm notify
                                    "Something more" if julia.hypno_bj:
                                        player.c "Your blow jobs are nice, Julia, but your sexy body has made my cock extra hard today."
                                        player.c "I want something more than a blow job."
                                        julia.c "Oh. I can't fuck you because my husband is breeding me right now."
                                        "She thinks for a minute. The act of doing so seems to cause her a pain."
                                        julia.c "I know! You could fuck my ass!"
                                        wt_image julia_store_20
                                        if julia.naked_now:
                                            "She kneels down on the floor of the store, presenting her ass to you."
                                        else:
                                            "She pulls off her remaining clothing and kneels on the floor of the store, presenting her ass to you."
                                        julia.c "Oh! You're so big!"
                                        wt_image julia_store_21
                                        "Her butt hole is tight, but she relaxes her sphincter quickly, giving you easy access. She's had cocks back here before."
                                        "She closes her eyes as you begin to thrust in and out of her butthole. She likes this."
                                        julia.c "Ohhh!  Ohhhh!!"
                                        wt_image julia_store_22
                                        "Her hot, tight anal chute gripping your cock soon brings you over the edge. You release your seed inside her on a hard downthrust."
                                        player.c "[player.orgasm_text]"
                                        wt_image julia_store_23
                                        "The feel of your jizz filling her bowels takes Julia over the edge."
                                        julia.c "Oh!  Oh I'm cummmiinnnnggg!!!"
                                        wt_image julia_store_24
                                        julia.c "Do you feel better now?"
                                        player.c "Yes, Julia.  Much better."
                                        julia.c "Oh goodie! That was tiring. I have to go now, before your cum dripping out of my ass makes a mess on the carpet. Bye bye!"
                                        $ julia.anal_count += 1
                                        orgasm notify
                            else:
                                player.c "A blow job would be very nice, Julia."
                                if julia.naked_now:
                                    wt_image julia_store_14
                                else:
                                    wt_image julia_store_13
                                "She kneels down and takes out your cock."
                                if julia.naked_now:
                                    "Naughtily, she sneaks a hand between her legs and plays with herself while she's blowing you."
                                    wt_image julia_store_16
                                else:
                                    wt_image julia_store_15
                                "She proceeds to give you a sloppy, enthusiastic blow job, low on technique but high on energy."
                                if julia.naked_now:
                                    wt_image julia_store_18
                                else:
                                    wt_image julia_store_17
                                "When you're ready to cum, she looks up at you and prepares to receive your load."
                                player.c "[player.orgasm_text]"
                                wt_image julia_store_19
                                julia.c "Do you feel better now?"
                                player.c "Yes, Julia.  Much better."
                                julia.c "Oh goodie!  "
                                julia.c "That was tiring.  I have to go now.  Bye bye!"
                                $ julia.blowjob_count += 1
                                $ julia.facial_count += 1
                                $ julia.hypno_bj = True
                                orgasm notify
                        "Talk with her":
                            call julia_jewelry_store_third_visit_talk from _call_julia_jewelry_store_third_visit_talk_1
                        "Buy something":
                            $ julia.temporary_count = 1
                            while julia.temporary_count == 1:
                                call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_17
                "Look at her":
                    call julia_jewelry_store_third_visit_look from _call_julia_jewelry_store_third_visit_look_1
                "Talk with her":
                    call julia_jewelry_store_third_visit_talk from _call_julia_jewelry_store_third_visit_talk_2
                "Buy something":
                    $ julia.temporary_count = 1
                    while julia.temporary_count == 1:
                        call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_18
    else:
        if donna.ready_for_julia >= 3:
            julia.c "Hi!  I like Donna!"
            julia.c "Did you come back to look at me or to buy something?"
        else:
            julia.c "Hi!  Did you come back to look at me or to buy something?"
        $ title = "What do you want?"
        menu:
            "Hypnotize her" if player.can_hypno(julia):
                call julia_jewelry_store_hypnotize_her from _call_julia_jewelry_store_hypnotize_her_2
            "Look at her":
                call julia_jewelry_store_third_visit_look from _call_julia_jewelry_store_third_visit_look_2
            "Talk with her":
                call julia_jewelry_store_third_visit_talk from _call_julia_jewelry_store_third_visit_talk_3
            "Buy something":
                $ julia.temporary_count = 1
                while julia.temporary_count == 1:
                    call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_19
    return

label julia_jewelry_store_third_visit_look:
    if julia.discussed_bra and julia.discussed_panties:
        player.c "I'd love to take another look at you."
        julia.c "Oh goodie! I like showing my body off."
        wt_image julia_store_11
        "She steps out from around the counter and pulls off her dress."
    elif julia.discussed_bra:
        player.c "I'd love to see your bra again."
        julia.c "Okay!"
        wt_image julia_store_4
        "She steps out from around the counter and pulls down the top of her dress, giving you a good look at her bra."
        julia.c "I can show you my panties too. It's okay because they're not see through."
        wt_image julia_store_11
        "She steps out of her dress and stands in front of you in just her bra and panties."
        julia.c "I did remember not to wear see through panties, didn't I?"
        player.c "Yes, it's okay. Those aren't see through."
        julia.c "Okay, good. Because the building management got mad at me for showing off my see through panties."
        $ julia.discussed_panties = True
    elif julia.discussed_panties:
        player.c "I'd love to see your panties again."
        julia.c "Okay!"
        wt_image julia_store_7
        "She steps out from behind the counter and pulls up her dress."
        julia.c "I can show you my bra too, but only because my bra is covering up my nipples."
        wt_image julia_store_11
        "She steps out of her dress and stands in front of you in just her bra and panties."
        julia.c "If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
        julia.c "The building management has already warned me about that."
        $ julia.discussed_bra = True
    else:
        player.c "I'd love to take a look at you."
        julia.c "Oh goodie! I like showing my body off. The only thing is, I can't show you too much, because the building management gets mad at me."
        wt_image julia_store_5
        "She steps out from around the counter."
        julia.c "But I can show you my panties. This is okay because they're not see through."
        wt_image julia_store_6
        player.c "I did remember not to wear see through panties, didn't I?"
        player.c "Yes, it's okay. Those aren't see through."
        wt_image julia_store_7
        julia.c "Okay, good.  Because the building management got mad at me for showing off my see through panties."
        julia.c "I can show you my bra too, but only because my bra is covering up my nipples."
        wt_image julia_store_11
        "She steps out of her dress and stands in front of you in just her bra and panties."
        julia.c "If I showed you my nipples you'd get excited and then I would feel guilty and need to give you a blow job, and I shouldn't give blow jobs here at the store."
        julia.c "The building management has already warned me about that."
        $ julia.discussed_panties = True
        $ julia.discussed_bra = True
    call julia_jewelry_store_third_visit_talk from _call_julia_jewelry_store_third_visit_talk_4
    return

label julia_jewelry_store_third_visit_talk:
    # first, call expandable talk options
    call expandable_menu(julia_store_talk_menu) from _call_expandable_menu_20
    # then, call expandable purchase options
    $ julia.temporary_count = 1
    while julia.temporary_count == 1:
        call expandable_menu(julia_store_purchase_menu) from _call_expandable_menu_21
    return

label julia_talk_nothing:
    pass
    return

label julia_talk_why_bimbo:
    player.c "Why do you act like this, Julia?"
    julia.c "Like what?  A bimbo?"
    player.c "Yes, a bimbo."
    julia.c "It's fun! I get all the time in the world to spend on my makeup and my hair. I don't have to think about anything except how to make myself look pretty for boys."
    player.c "I think you could do more with your life."
    julia.c "Nuh huh. I've done lots of things. I was never happy until I met my husband. He told me to stop thinking and spend my time on silly girly things."
    julia.c "At first I thought he was stupid and crazy, but now I know he's the most brilliantest man in the whole world!"
    julia.c "He knew I was a ditzy airhead trying to be smart and successful. That was silly. I'm dumb. I'm so dumb I didn't know I was dumb until I met him."
    julia.c "He taught me to stop thinking and just be a happy airhead."
    julia.c "Talking is tiring.  Would you like to buy something?"
    $ julia.discussed_bimbo = True
    return

label julia_talk_date:
    player.c "Would you like to go on a date with me sometime, Julia?"
    if player.has_tag('supersexy'):
        julia.c "Really? You'd like to spend time with me?"
        julia.c "You're so handsome, I'd like to be able to look at you some more."
        julia.c "I know!! Why don't you come to my house! We can hang out in my pool together."
        player.c "Sure, we could do that."
        julia.c "Great! Not this week, though, because I need to buy a new bathing suit to show you when you visit."
        add tags 'home_visits_pending' to julia
        # $ julia.home_visits_active = True  ## no, not 'til end_week label'
    elif player.has_tag('dominant'):
        julia.c "Nuh huh.  You're a Mister Bossy Pants."
        player.c "Excuse me?"
        julia.c "You're a Mister Bossy Pants. You like to tell girls what to do. I don't like men who tell me what to do."
        julia.c "Except my husband. And that's just because when he tells me what to do, I don't need to think as often. I don't like thinking."
        player.c "What do you like?"
        julia.c "I like shiny things! I have lots of nice shiny things here. Would you like to buy one of them?"
        if not player.has_item(handcuffs_julia):
            sys "If you had the right shiny thing, you might be able to change her mind about spending time with you. Perhaps a wealthy woman with a fondness for dominant men might give you something appropriate someday, if you impress her and it's not a business arrangement."
    else:
        julia.c "No. My husband lets me hang out with special friends sometimes, but they're all really, really good looking guys, and you're just average."
        if julia.hypno_count > 0:
            julia.c "I like when you come to the store and it's fun when you use that hypno-thingie, but I don't want to go on a date."
        else:
            julia.c "I like when you come to the store, but I don't want to go on a date."
    $ julia.discussed_date = True
    return

label julia_talk_bras:
    player.c "Can I ask you about your bras?"
    julia.c "My bras? Why, is there something wrong with them? Did I forget to wear a bra to work again?"
    player.c "No, I mean, where do you get your bras? My girlfriend has trouble finding a bra to fit and she's shaped similarly to you."
    julia.c "Does she have big titties like me?"
    player.c "Yes"
    julia.c "Lucky you!! I know exactly what's wrong. She can't shop retail! Even the lingerie shops can't fit big titty women like your girlfriend and me properly."
    julia.c "I don't know why. You'd think the store clerks would like to get their hands on big titties."
    julia.c "Anyway, you need to call Brenda. She loves to get her hands on big titties!  All very professional, of course ... most of the time. Your girlfriend may have to tell her 'down girl' once in a while."
    julia.c "But don't worry! Brenda will fit your girlfriend right up in the best fitting bras money can buy! I'll get you her contact information."
    if chelsea.bra_fitting_status == 1:
        "Brenda the Bra Fitter. That should be easy to remember. And she's a lesbian to boot. Might be fun to send her [chelsea.name]'s way."
        $ chelsea.bra_fitting_status = 2
    else:
        "That's the same name you got previously. It seems Brenda the Bra Fitter's client list includes a lot of the town's wealthy and well-endowed clients."
    return

label julia_talk_donna:
    player.c "Julia, I have a friend who could use your help."
    julia.c "My help?  How?"
    player.c "She's having trouble with her make up, and can't seem to get her hair quite right.  And she spends too much time thinking."
    julia.c "Is she using her brain instead of doing her nails?"
    player.c "Sometimes, yes."
    julia.c "That's not good!  I bet she's unhappy.  I can help her!"
    player.c "I knew you could."
    julia.c "This is exciting.  I need to go fix my hair and get ready to meet a new friend!"
    "Julia will be available to help train Donna on a future weekend."
    $ donna.ready_for_julia = 2
    return

# Jewelry Store Purchases
label julia_no_buy_leave:
    "You don't need any jewelry right now, and you explain that to Julia."
    julia.c "That's okay!  I'm tired now.  This was a long chat.  Bye bye!"
    $ julia.temporary_count = 0
    return

label julia_nipple_clips:
    player.c "I need some nipple jewelry, like some nice nipple rings. The clip on type, though. She's not ready for a piercing yet."
    julia.c "Oouuu!! Sounds slutty! Is she a slut?"
    player.c "Yes, when I tell her to be. Which is why these need to come on and off, at least for now."
    julia.c "I have just the thing!!"
    wt_image nipple_rings_1
    "She ducks behind the counter and produces two silver, clip on nipples rings. She blushes slightly when she hands them over."
    if not julia.naked_now:
        wt_image julia_store_10
    else:
        wt_image julia_store_25
    julia.c "I don't really like the Mister Bossy Pants types who put thingies through their girls' sensitive bits, but sometimes a guy just wants his girl to look a little extra slutty. I saw these in a catalog and just had to get a pair.  For the store, of course."
    "She blushes some more."
    julia.c "They're only 200."
    $ title = "Buy them?"
    menu:
        "Yes (costs 200)" if player.money - player.min_money >= 200:
            player.c "I'll take them."
            julia.c "Goody!!"
            wt_image gift_box_1
            "She wraps them up for you in a fancy box, like they were a special gift for a special lady. Which in a way, they are, though not in the ear rings or necklace sort of way."
            if not julia.naked_now:
                wt_image julia_store_10
            else:
                wt_image julia_store_25
            julia.c "Thanks for shopping here! Finding you the right gift was exhausting. I'm going to go home and rest now."
            $ julia.temporary_count = 0
            $ jasmine.whore_play_status = 8
            change player money by -200 notify
            add 1 nipple_rings_jasmine to player
        "No":
            player.c "I'll think about it."
            julia.c "Okay!"
    return

label julia_chelsea_gift:
    player.c "Do you have anything that would help me convince a girl she's special and I want a more serious relationship with her?"
    julia.c "Awww!! Luvvy duvvy stuff!!! That's so sweet. Let me think ... wait, no, I'm not supposed to do that anymore."
    julia.c "Oh! I know!! I have just the thing!!"
    wt_image chubby_jewelry_1
    "She ducks behind the counter and produces a silver necklace with a heart shaped pendant. She beams as she hands it over."
    julia.c "This would be perfect, and I didn't even have to think about it!"
    if not julia.naked_now:
        wt_image julia_store_10
    else:
        wt_image julia_store_25
    julia.c "It's pretty and classy. She can wear it with anything - or nothing - and every time she sees it she'll think of you and your love of her."
    julia.c "Oh, and your good taste, too."
    julia.c "Oh, and also your money. Looking at this will remind her that you have money and you're willing to spend it on her. That's why these things cost so much. If they were cheaper, they wouldn't send the right message."
    julia.c "That's why this one costs 400."
    $ title = "Buy it?"
    menu:
        "Yes (costs 400)" if player.money - player.min_money >= 400:
            player.c "I'll take it."
            julia.c "Goody!!"
            wt_image gift_box_1
            "She wraps the necklace up for you in a fancy box and sends you on your way."
            if not julia.naked_now:
                wt_image julia_store_10
            else:
                wt_image julia_store_25
            julia.c "Thanks for shopping here! Finding you the right gift was exhausting.  I'm going to go home and rest now."
            $ julia.temporary_count = 0
            add 1 jewelry_chelsea to player
            change player money by -400 notify
        "No":
            player.c "I'll think about it."
            julia.c "Okay!"
    return

# Jewelry Store Discussions
label julia_jewelry_store_about_store:
    player.c "This is a nice store."
    julia.c "Thank you! My husband told me to open it."
    julia.c "He told me I can't spend all day in our pool. Well, I can spend all day in our pool, but he told me I shouldn't, because then nobody would get to see me."
    julia.c "So when the bank opened up next door, I thought 'Hey! This would be a good place to sell expensive stuff to people who have money!'"
    julia.c "Then my husband reminded me I shouldn't be thinking, so I went and sat in our pool for the rest of the day."
    julia.c "But the next day I couldn't help myself and I thought again, and I thought 'Hey! I could sell pretty things because I like pretty things, and I could sell expensive beauty products because I like expensive beauty products!'"
    julia.c "Then my husband reminded me again that I wasn't supposed to be thinking so much, so I went back to the pool."
    julia.c "And the next day he signed a lease and we opened this store and I bought lots of pretty things and here they are!"
    julia.c "Do you want to buy something?"
    $ julia.discussed_store = True
    return

label julia_jewelry_store_about_her:
  player.c "Do you like working at this store?"
  julia.c "Yes! I used to work upstairs in one of the offices, but my husband told me I was using my brain too much."
  player.c "Were you a secretary?"
  julia.c "No, I was an accountant. I am an accountant, I guess, because I still have the education and qualifications and all that sort of stuff."
  julia.c "And I still have a partnership interest in my old firm, but they only send me money from my old clients that I passed on to the other partners."
  player.c "You were a partner in an accounting firm?"
  julia.c "I still am! My name is still in the firm name. I just don't work there right now because I have to use my brain to be an accountant and my husband tells me I'm happier when I don't have to think very much."
  julia.c "This store is much better because now all I do is sell pretty things! My former clients like to stop in and see me when I'm here. They often buy things."
  julia.c "Do you want to buy something?"
  $ julia.discussed_her = True
  return

label julia_jewelry_store_hypnotize_her:
    # this is always the first hypnosis session
    player.c "Julia, look at this for me."
    call focus_image from _call_focus_image_69
    julia.c "Ooooo  that's pretty!"
    player.c "Listen to me, Julia. Listen to my words. Only my words, now, Julia. Only my words."
    wt_image julia_store_8
    player.c "We are going to chat, Julia. We should be comfortable when we chat. You should show me your breasts so we're both comfortable while we chat."
    julia.c "Okay"
    wt_image julia_store_9
    "She pulls off her dress and pulls down her bra, displaying her breasts."
    julia.c "Are you a hypnotist?  Am I hypnotized now?"
    player.c "Yes, Julia, I've hypnotized you, but you will not remember that I hypnotized you. When I leave here, you will forget that you were hypnotized."
    julia.c "Okay. I've never been hypnotized before. Can you make me do anything you want now? Do you want me to quack like a duck? Quack! Quack!"
    player.c "No, Julia, I don't want you to quack like a duck. And no, I can't make you do anything I want."
    player.c "I can only convince you to do things you're willing to do, but I can influence you so that you're more willing to do those things even in circumstances where you normally wouldn't."
    julia.c "Like show you my tits at the store? I like showing men my tits, but I'm not supposed to do it here at the store because the building management gets mad at me."
    julia.c "But because you told me to do it while I was hypnotized, I did it anyway."
    player.c "That's right."
    julia.c "Okay, but just so you know, I'm not going to give you a blow job."
    player.c "You like giving men blow jobs Julia. You would like to give me a blow job."
    julia.c "I only give men blow jobs when I tease them and they get all horny and then I feel bad for them. Or sometimes I let them fuck me in the ass or if my husband isn't breeding me and I'm on birth control then I let them fuck me in the pussy."
    julia.c "But its not my fault if you're get horny because you were the one who made me show you my breasts."
    player.c "You do feel sorry for me, though, Julia. And it is your fault that your body is so sexy that I'm getting very horny. You want to make me feel better."
    julia.c "Nuh huh. That's because of you and your hypno-thingie. You shouldn't be using that to get women to show you your breasts. If you're horny now that's your fault."
    "You can't get any further with Julia on this path today."
    $ julia.hypno_session() # deletes energy and records she was hypnotized
    return

# Handcuff conversation
label julia_jewelry_store_discuss_handcuffs:
    if julia.handcuff_discussion == 0:
        $ julia.handcuff_discussion = 1
        player.c "What do you think of these handcuffs?  Are these real gems?"
        wt_image handcuffs_julia_1
        julia.c "Ooouuu!!  Where did you get these???"
        player.c "A friend gave them to me.  I'm not sure about them.  I don't think a woman would want to wear these."
        wt_image julia_store_26
        julia.c "Yes!!! Yes, I wou ... I mean, yes, yes she would! Any woman would want to wear these!! Any woman who wants to look pretty would."
        julia.c "These are real gems! Diamonds!! Beautiful, lovely diamonds."
        player.c "I know, but they're on a pair of handcuffs."
        wt_image julia_store_27
        julia.c "That's okay!! They'd still look pretty!"
        $ title = "What now?"
        menu:
            "Ask if she really thinks they're pretty":
                call julia_jewelry_store_discuss_handcuffs_pretty from _call_julia_jewelry_store_discuss_handcuffs_pretty
            "Leave":
                player.c "Okay. Thanks for your opinion. Maybe I'll find the right woman to try them on sometime."
                wt_image julia_store_28
                "A disappointed Julia looks like she wants to say something, but can't get control of her tongue before you leave."
    elif julia.handcuff_discussion > 0:
        if julia.handcuff_discussion == 1:
            wt_image handcuffs_julia_1
            player.c "I still can't decide what I think about these handcuffs."
            julia.c "Ooouuu!! I forgot how pretty they are!"
            player.c "But they're handcuffs."
            wt_image julia_store_27
            julia.c "Beautiful, pretty, sparkily handcuffs!!"
            $ title = "What now?"
            menu:
                "Ask if she really thinks they're pretty":
                    call julia_jewelry_store_discuss_handcuffs_pretty from _call_julia_jewelry_store_discuss_handcuffs_pretty_1
                "Leave":
                    player.c "Okay. Thanks for your opinion. Maybe I'll find the right woman to try them on sometime."
                    wt_image julia_store_28
                    "A disappointed Julia looks like she wants to say something, but can't get control of her tongue before you leave."
        else:
            wt_image handcuffs_julia_1
            player.c "I still haven't found the right woman to use these handcuffs on."
            julia.c "Ooouuu!! I forgot how pretty they are!"
            wt_image julia_store_26
            julia.c "Ummm, maybe it would help if you saw them being modeled again?  Maybe??  Maybe???"
            player.c "I'm not sure that's a good idea. You know what can happen when I put these on you. It may be the wrong time of month for you. What has your husband told you?"
            wt_image julia_store_27
            julia.c "I'm sure it isn't! And if I don't think about it I won't remember what he said and then there won't be any reason for you not to let me model them again."
            $ title = "Ask her to model them?"
            menu:
                "Ask her to put them on":
                    call julia_jewelry_store_discuss_handcuffs_put_them_on from _call_julia_jewelry_store_discuss_handcuffs_put_them_on
                "Leave":
                    player.c "Okay. Thanks for your opinion. Maybe I'll find the right woman to try them on sometime."
                    wt_image julia_store_28
                    "A disappointed Julia looks like she wants to say something, but can't get control of her tongue before you leave."
    return

label julia_jewelry_store_discuss_handcuffs_pretty:
    player.c "Do you really think so?"
    wt_image julia_store_26
    julia.c "Yes!!! I know all about pretty things! These would look super extra beautiful on me ... I mean, on a woman."
    player.c "It would probably help if I could see a woman wearing them."
    wt_image julia_store_27
    julia.c "Maybe I could ..."
    player.c "Oh, but there's a problem with that. As you know, I'm a Mr. Bossy Pants type of guy. If I put these handcuffs on a woman, I'd probably start telling her what to do."
    wt_image julia_store_29
    julia.c "Ummm ... That's probably okay. I mean, I'd still get ... I mean, she'd still get to wear them, right?"
    player.c "Of course. In fact, she wouldn't get to take them off until I was finished doing things with her."
    julia.c "Why would I want .. why would she want to take them off?"
    player.c "Well, possibly on account of the things I would be doing with her."
    julia.c "Oh! You mean you'd want to do \"things things\" with me ... with her, while I was ... while she was wearing them?"
    player.c "Yes, I think that's what would happen if I put these on a woman."
    wt_image julia_store_26
    "She looks at the handcuffs wistfully, then back up at you."
    julia.c "Yeah, I can see how a Mr. Bossy Pants would start doing that. They do look like the sort of thing that a Mr. Bossy Pants would put on a woman before getting all bossy with her."
    wt_image julia_store_30
    julia.c "But ... if they looked really, really pretty, maybe I ... I mean maybe a woman would be okay with being bossed around? Because, you know, she'd be looking so pretty?"
    $ title = "Ask her to model them?"
    menu:
        "Ask her to put them on":
            player.c "It's so hard to know. You're probably right. The handcuffs probably would look pretty on the right woman, and that would make her feel good. "
            player.c "But then I'd start telling her what to do, and I wouldn't let her out of the handcuffs until she did them. And if she had a husband or a boyfriend, he would be mad because of what she did while she was in the handcuffs."
            wt_image julia_store_27
            julia.c "Not as long as it isn't that time of month! I mean, as long I .. as long as she couldn't get pregnant, probably her husband wouldn't mind. Especially if he knew how pretty she looked."
            player.c "Is it that time of month for you?"
            wt_image julia_store_26
            julia.c "Ummm, I don't want to think about that, because if I think about it the answer may be yes and then you wouldn't be able to put the handcuffs on me."
            player.c "On you?  Would you really want to model them for me, so I could see how pretty they look on you?"
            wt_image julia_store_29
            julia.c "YES!!! PLEASE! I mean ... yes, if you want ... if you thought that could be of help?"
            call julia_jewelry_store_discuss_handcuffs_put_them_on from _call_julia_jewelry_store_discuss_handcuffs_put_them_on_1
        "Leave":
            player.c "Okay. Thanks for your opinion. Maybe I'll find the right woman to try them on sometime."
            wt_image julia_store_28
            "A disappointed Julia looks like she wants to say something, but can't get control of her tongue before you leave."
    return

label julia_jewelry_store_discuss_handcuffs_put_them_on:
    player.c "Well, if you ..."
    if julia.naked_now == True:
        wt_image julia_store_32
    else:
        wt_image julia_store_31
    julia.c "I don't mind!!! Let me close the store!"
    wt_image closed_sign
    "The \"closed\" sign goes up, and Julia leads you into the back room ..."
    if julia.handcuff_discussion == 1:
        $ julia.handcuff_discussion = 2
        wt_image julia_handcuffs_1
        "... where she changes into a leather and mesh outfit."
        player.c "Why do you have this back here?"
        julia.c "In case a Mr. Bossy Pants is bossing me around. This is a perfect \"I'm being bossed by a Mr. Bossy Pants\" type outfit."
        player.c "But you don't like to be ..."
        julia.c "I need to be pretty!! A bimbo has to be prepared for any opportunity to look pretty, and you can't look pretty without the right outfit."
        julia.c "Or the right accessories. Try them on! Try them on!! I need to see what the handcuffs look like on me!"
        wt_image julia_handcuffs_2
        julia.c "Awwww!! I can't see them when you put them on like this!"
        wt_image julia_handcuffs_3
        julia.c "Do they look pretty on me?? Do I look good wearing them??? Oh! There's a mirror. I can see them now!! They do look pretty!!!"
        player.c "Julia, don't look at the mirror, look at me."
        julia.c "But I want to see what I look like wearing them!"
        player.c "You look like the sort of woman who should be doing what I tell her."
        wt_image julia_handcuffs_4
        julia.c "Oh, yeah. I guess I do sorta look like that now, don't I?"
        $ julia.done_foreplay = False
        $ title = "What do you do with her first?"
        menu:
            "Kiss her":
                player.c "Kiss me, Julia."
                wt_image julia_handcuffs_5
                "She offers no resistance as you press your lips to hers ..."
                wt_image julia_handcuffs_6
                "... and is soon kissing you back ..."
                wt_image julia_handcuffs_7
                "... as you fondle her ass."
                $ julia.done_foreplay = True
                $ title = "Have sex with her now?"
                jump menu_julia_handcuffs_sex
            "Grope her":
                wt_image julia_handcuffs_8
                "You pull up what passes for a skirt in this outfit as Julia examines herself in the mirror."
                wt_image julia_handcuffs_9
                "*smack*"
                julia.c "Ow!"
                player.c "Pay attention to me, not the mirror."
                wt_image julia_handcuffs_10
                "Despite the rebuke, she continues to sneak glances at herself in the mirror as you fondle her ass ..."
                wt_image julia_handcuffs_11
                "... something that becomes much easier as you turn her around to fondle ..."
                wt_image julia_handcuffs_12
                "... and then expose her tits ..."
                wt_image julia_handcuffs_13
                "... an experience she doesn't seem to mind."
                julia.c "Oohhh"
                $ julia.done_foreplay = True
                $ title = "Have sex with her now?"
                jump menu_julia_handcuffs_sex
    else:
        wt_image julia_handcuffs_1
        "... where she changes back into her leather and mesh outfit as you fit the handcuffs back on her."
        wt_image julia_handcuffs_2
        julia.c "Awwww!!  You put them on where I can't see them again! What do you think? Do they still look pretty on me??"
        player.c "You look like you should be doing what I tell you."
        julia.c "Oh, yeah. I guess I do look like that again, huh?"
        $ julia.done_foreplay = False
        $ title = "What do you want to do with with her?"
        menu menu_julia_handcuffs_sex:
            "Kiss her" if not julia.done_foreplay:
                player.c "Kiss me, Julia."
                wt_image julia_handcuffs_5
                "She offers no resistance as you press your lips to hers ..."
                wt_image julia_handcuffs_6
                "... and is soon kissing you back ..."
                wt_image julia_handcuffs_7
                "... as you fondle her ass."
                $ julia.done_foreplay = True
                $ title = "Have sex with her now?"
                jump menu_julia_handcuffs_sex
            "Grope her" if not julia.done_foreplay:
                wt_image julia_handcuffs_8
                "You pull up what passes for a skirt in this outfit as Julia examines herself in the mirror."
                wt_image julia_handcuffs_9
                "*smack*"
                julia.c "Ow!"
                player.c "Pay attention to me, not the mirror."
                wt_image julia_handcuffs_10
                "Despite the rebuke, she continues to sneak glances at herself in the mirror as you fondle her ass ..."
                wt_image julia_handcuffs_11
                "... something that becomes much easier as you turn her around to fondle ..."
                wt_image julia_handcuffs_12
                "... and then expose her tits ..."
                wt_image julia_handcuffs_13
                "... an experience she doesn't seem to mind."
                julia.c "Oohhh"
                $ julia.done_foreplay = True
                $ title = "Have sex with her now?"
                jump menu_julia_handcuffs_sex
            "Blow job":
                player.c "I want you to blow me, Julia."
                wt_image julia_handcuffs_14
                julia.c "Okay.  I will.  I'll do a better job if I can have my hands free, though.  I promise, I'll still suck you off, even if you let me out of the handcuffs.  Because, you know, I'm kinda the sort of woman who takes orders right now."
                $ title = "Take them off?"
                menu:
                    "Yes, let her use her hands":
                        wt_image julia_handcuffs_20
                        "You remove the cuffs and Julia gently strokes your cock before kneeling down and taking you into her mouth."
                        wt_image julia_handcuffs_21
                        "She seems to pay as much attention to watching herself blow you in the mirror as she does to actually blowing you ..."
                        wt_image julia_handcuffs_22
                        "... requiring you to redirect her attention.  Bimbos are so easily distracted."
                        wt_image julia_handcuffs_23
                        "Once redirected to the \"task in hand\", so to speak, it doesn't take long for the combination of her fingers, lips, and tongue to have you ready to cum."
                    "No, have her use just her mouth":
                        player.c "You don't need your hands. You can blow me fine with just your mouth."
                        julia.c "Okay."
                        wt_image julia_handcuffs_15
                        "She kneels down in front of you ..."
                        wt_image julia_handcuffs_16
                        "... and takes you into her mouth."
                        wt_image julia_handcuffs_17
                        "Without the use of her hands, she has to work a lot harder ..."
                        wt_image julia_handcuffs_18
                        "... but eventually you're ready to cum."
                wt_image julia_handcuffs_19
                player.c "[player.orgasm_text]"
                $ julia.blowjob_count += 1
                $ julia.swallow_count += 1
                orgasm notify
            "Tit job":
                wt_image julia_handcuffs_14
                player.c "I want to fuck your tits, Julia."
                julia.c "Okay."
                wt_image julia_handcuffs_24
                "She kneels down in front of you and you remove her cuffs so she can use her hands to form a valley in her chest ..."
                wt_image julia_handcuffs_25
                "... which you fill with your cock. She seems to pay as much attention to watching you tit fuck her in the mirror as she does to the actual tit fuck ..."
                wt_image julia_handcuffs_26
                "... requiring you to redirect her attention.  Bimbos are so easily distracted."
                player.c "Eyes forward, Julia."
                wt_image julia_handcuffs_27
                "Once you have her full attention, your orgasm follows quickly ..."
                player.c "[player.orgasm_text]"
                wt_image julia_handcuffs_28
                "... coating her chest, neck, and even her chin with your jizz ..."
                wt_image julia_handcuffs_29
                "... a look that Julia seems to find as interesting as you do."
                $ julia.titfuck_count += 1
                $ julia.facial_count += 1
                orgasm notify
            "Cowgirl":
                wt_image julia_handcuffs_14
                player.c "I want to fuck you, Julia."
                julia.c "Okay."
                wt_image julia_handcuffs_30
                "You lift her up and place the tip of your cock against her. She's already wet and wriggles forward, impaling herself on you, an experience she seems to enjoy as much as you do."
                julia.c "Oohhh"
                wt_image julia_handcuffs_31
                "As you guide her up and down your shaft, however, she gets a frustrated look on her face."
                julia.c "Awww. I can't touch my pussy with these handcuffs on. I won't cum if I can't touch my pussy while your hard cock is inside me."
                $ title = "Uncuff her?"
                menu:
                    "Yes, let her play with herself":
                        wt_image julia_handcuffs_33
                        "You uncuff her and she wastes no time moving her hand between her legs and rubbing herself."
                        julia.c "Ohhh  Ohhhhh  OH! I'm cumminnnggg!!!"
                        "She's not the only one."
                        player.c "[player.orgasm_text]"
                        wt_image julia_handcuffs_34
                        julia.c "That felt like a lot of cum. Did it feel like a lot of cum to you?"
                        player.c "Yes, I suppose it did."
                        $ julia.orgasm_count += 1
                    "No, just fuck her":
                        wt_image julia_handcuffs_32
                        "You ignore her. You can still enjoy yourself and you do, guiding her up and down your dick until you fill her with your seed."
                        player.c "[player.orgasm_text]"
                        wt_image julia_handcuffs_31
                        julia.c "Hmmphh. This is why I don't like Mr. Bossy Pants types. I had a hard cock inside me and didn't get to cum."
                        wt_image julia_handcuffs_1
                        "You uncuff her and help her to stand up."
                        player.c "You can always play with yourself after I go."
                        julia.c "Oh yeah!! I forgot! Okay, that's not too bad, then."
                $ julia.sex_count += 1
                orgasm notify
            "Doggy style":
                wt_image julia_handcuffs_14
                player.c "I want you to fuck you, Julia."
                julia.c "Okay. But only if you let me out of the handcuffs first so I can look at them while you fuck me."
                wt_image julia_handcuffs_35
                "You remove the handcuffs and place them in front of her ..."
                julia.c "Ooouuu!! They really are pretty!"
                wt_image julia_handcuffs_36
                "... then you push yourself into her already wet snatch."
                julia.c "Oohhh! That feels almost as good as the handcuffs look."
                wt_image julia_handcuffs_37
                player.c "\"Almost as good\"?"
                "You thrust into her, gently at first, then with more and more force."
                julia.c "Oohhh!  Ummm, maybe as good??  Ooohhhh!"
                wt_image julia_handcuffs_38
                player.c "Try \"better\" or I take my cock away."
                julia.c "REALLY REALLY REALLY WAY BETTER GOOD!!  OH! I'm cumminnnggg!!!"
                "She's not the only one."
                player.c "[player.orgasm_text]"
                wt_image julia_handcuffs_36
                julia.c "Your cum inside me feels almost as good as the handcuffs look, too."
                julia.c "Wait, no, as good."
                julia.c "Wait wait, no, way better good!"
                $ julia.sex_count += 1
                $ julia.orgasm_count += 1
                orgasm notify
            "Eat her out":
                wt_image julia_handcuffs_39
                "Burying your face in her ample bosom, you lick and suckle her tits as she moans."
                julia.c "Oohhh"
                wt_image julia_handcuffs_40
                "Then you remove her handcuffs and her panties ..."
                wt_image julia_handcuffs_41
                "... and spread her legs, lowering your tongue to her sex ..."
                wt_image julia_handcuffs_42
                "... which soon drenches your tongue with her juices ..."
                julia.c "Oohhh  ...  Ooohhhh"
                wt_image julia_handcuffs_43
                "... before her hips suddenly buck up to press her sex against your face as her whole body shudders."
                julia.c "OH!  I'm cumminnnggg!!!"
                wt_image julia_handcuffs_44
                julia.c "I would like Mr. Bossy Pants types a lot better if they made me do that more often!"
                $ julia.pleasure_her_count += 1
                $ julia.orgasm_count += 1
                change player energy by -energy_short notify
            "End things there" if julia.done_foreplay:
                wt_image julia_handcuffs_1
                "That's enough fun with her for today. You let her out of the handcuffs."
    player.c "Thank you, Julia. That certainly gives me a better appreciation of how the handcuffs look on a woman, as well as the sort of woman I should use them on."
    julia.c "A pretty one! You should definitely use them on a pretty woman."
    julia.c "Ummm, if you're having trouble figuring out who that is, you could always ask me to model them for you again. You know, in case it helps you figure things out?"
    return


## Items
# Give Butt Plug
label give_bp_julia:
  "You should save the butt plug for a client."
  return

# Chastity Belt
label give_cb_julia:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_julia:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_julia:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

label give_hcj_julia:
    "You should talk to her about them."
    return

# Give Jewelry
label give_jwc_julia:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_julia:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_julia:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_julia:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_julia:
  "Best to save this for a paying client."
  return

# Give Ring of Secuality
label give_rs_julia:
    "It's shiny, so she'd probably take it and wear it.  But she has no content for this, so you're better off saving it for someone else."
    return

# Use Water Bowl
label use_wb_julia:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_julia:
  "You should try this on someone else."
  return

# Handcuffs
label hcj_examine:
  wt_image handcuffs_julia_1
  "An expensive pair of handcuffs elaborately decorated with jewels."
  return

label hcj_throw_away:
  $ title = "Do you really want to throw these away?"
  menu:
    "Yes (item will be permanently lost)":
      rem 1 handcuffs_julia from player notify
    "No":
      pass
  return

label give_hcj_fallback:
  "Save this for someone who likes shiny things."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label julia_start_day:
  ## Jewelry Store Opens
  if week >= 14 and day == 1 and jewelry_store.visit_count == 0 and jewelry_store.initial_message == False:
    wt_image bank_flyer
    "You receive a flyer announcing the opening of a new jewelry store on the main floor of the office tower, across from the bank branch."
    $ jewelry_store.initial_message = True
    $ office_tower.connection_js = office_tower.add_connections(jewelry_store)
    wt_image current_location.image
  return

# End Day
label julia_end_day:
  $ julia.naked_now = False
  $ jewelry_store.visited_today = False
  rem tags 'home_visit_today' from julia
  return

# End Week
label julia_end_week:
    if julia.has_tag('home_visits_pending'):
        rem tags 'home_visits_pending' from julia
        $ julia.home_visits_active = True
    return


## Club President Wife Content

label julia_gloria_other_talk_option:
    if gloria.discussed_bimbo == 1:
        player.c "What do you think about bimbos?"
        gloria.c "Not much. We don't even let them in the swingers room at the Club. They make the other women uncomfortable."
        player.c "Do you know the one who works at the jewelry store across from the bank downtown?"
        gloria.c "Julia? Yeah, she used to be our accountant if you can believe it. She was a tightly wound, sexually repressed number cruncher, then all of a sudden she changed. I'd have thought someone had slipped a potion into her, except she did a flawless job of transitioning our file to a new partner."
        player.c "I think it was just her new husband. He seems to have unlocked the key to her sexuality. The two of them are a good fit. Secretly, however, he likes to see her humiliated, he just can't bring himself to do it himself.  Nothing extreme.  He just likes seeing her perfect looks transformed to street walker whore trashy. You should invite the two of them over for dinner sometime. It would give you and your husband a new toy to play with."
        gloria.c "Our former accountant acting like a stupid ditz and forced to look trashy? Hmmmm. That might be a nice treat for our husband the next time we have a free evening. Let me have their number."
        "You provide the contact details for Julia's husband. He'll likely fill you in on how the evening goes once Gloria gets around to inviting them over."
        $ gloria.discussed_bimbo = 2
    return


## Character Specific Timers

########### ROOMS ###########
# Examine Julia's House
label jh_examine:
  return

# Prevent Access to Julia's House
label jh_no_access:
  return

label jh_enter:
  return

label jh_exit:
  return

# Examine Jewelry Store
label js_examine:
    "A small and cozy jewelry store."
    return

# Enter the Jewelry Store
label js_no_access:
    if julia.has_tag('home_visit_today'):
        wt_image closed_sign
        "The store's closed. Presumably Julia's still at home."
        break_movement
        wt_image current_location.image
    elif jewelry_store.visited_today:
        wt_image closed_sign
        "Mentally exhausted from the tiring conversation with you earlier, Julia has closed up shop for the day and gone home to relax in her pool."
        break_movement
        wt_image current_location.image
    return

label js_enter:
    # $ jewelry_store.visited_today = True  ## no: add after talking or hypnotizing
    # $ jewelry_store.visit_count += 1
    if jewelry_store.visit_count == 0:
        wt_image current_location.image
        "The jewelry store is small. Just a couple of cases of jewelry and some high end beauty products. A dark-haired woman in a low cut dress is behind the counter."
        wt_image julia_store_33
        julia.c "Hi! My name is Julia. Would you like to see something pretty?"
        wt_image julia_store_2
        "She holds a diamond necklace up to her chest."
        player.c "Those really are spectacular."
        julia.c "Tee hee. Not my tits, silly. The necklace."
        wt_image julia_store_3
        julia.c "I'm glad you like my tits, but I can't show you any more of them. The building manager has been getting mad at me for taking my clothes off."
    return

label js_exit:
  return

################################### NOTES ###################################
##################### TODO #####################
# WHERE IS THE MESS HER UP CONTENT?

## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
