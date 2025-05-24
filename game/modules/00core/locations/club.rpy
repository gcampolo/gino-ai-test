## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package club name "Club" description "Adds Club" dependencies core
register club_pregame 1 in core as "The Club"

# Pregame
label club_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('bit', "Club Couple Wife (Alysa Gap)")]
    model_credits += [('bit', "Patricia the Swinger (Samantha Jolie)")]


    ## Character Definition
    club_swingers = Person(Character("Swingers", who_color="#400040", what_color="#400040", window_background = gui.dialogue_background_dark_font_color), "club_swingers", cut_portrait = False, prefix = "", suffix = "", wait_for_message_period = 8, week_available = 4, prospect_min_reputation = -1)

    # 64,0,64
    swinger_h = Character("Pat", who_color="#400040", what_color="#400040", window_background = gui.dialogue_background_dark_font_color)
    # 128,0,255
    swinger_w = Character("Patricia", who_color="#8000FF", what_color="#8000FF")
    # 64,0,0
    rep_from_club = Person(Character("Club Couple Wife", who_color="#400000", what_color="#400000", window_background = gui.dialogue_background_dark_font_color), "rep_from_club", cut_portrait = False, prefix = "", suffix = "")
    # Navy
    husband_rep_from_club = Character("Club Couple Husband", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 128,64,0
    club_ball_woman = Person(Character("Club Ball Woman", who_color="#804000", what_color="#804000", window_background = gui.dialogue_background_dark_font_color), "club_ball_woman", cut_portrait = False, prefix = "", suffix = "")

    # Fuchsia
    club_patron_1 = Character("Club Patron", who_color="#FF00FF", what_color="#FF00FF")
    # 128,128,255
    club_patron_2 = Character("Club Patron", who_color="#8080FF", what_color="#8080FF")
    # 0,128,64
    club_patron_3 = Character("Club Patron", who_color="#008040", what_color="#008040", window_background=gui.dialogue_background_medium_font_color)
    # 128,0,255
    club_patron_4 = Character("Club Patron", who_color="#8000FF", what_color="#8000FF")
    # 0,128,192
    club_patron_5 = Character("Club Patron", who_color="#0080c0", what_color="#0080c0")
    # 255,0,128
    club_patron_6 = Character("Club Patron", who_color="#FF0080", what_color="#FF0080")
    # 0,64,64
    club_patron_7 = Character("Club Patron", who_color="#004040", what_color="#004040", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    club_patron_8 = Character("Club Patron", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 173,173,255
    club_patron_9 = Character("Club Patron", who_color="#adadff", what_color="#adadff")
    # Navy
    club_patron_10 = Character("Club Patron", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 255,128,0
    club_patron_11 = Character("Club Patron", who_color="#FF8000", what_color="#FF8000")
    # Teal
    club_patron_12 = Character("Club Patron", who_color="#008080", what_color="#00c4c4")

    ## Tags
    # Common Character Tags
    club_swingers.add_tags('no_hypnosis')
    rep_from_club.add_tags('can_be_in_club', 'no_hypnosis')
    club_ball_woman.add_tags('no_hypnosis')

    # Character Specific Tags
    # N/A

    ## Locations
    # The Club
    club = Location("The Club", 'tc', cut_portrait = True, enter_break_labels = ['tc_no_access'], enter_labels = ['tc_enter'], exit_labels = ['tc_exit'], area = ['downtown', 'club'], access_count = 0, visit_count = 0, unseen = False)

    # Swingers Room
    swingers_room = Location("Swingers Room", 'sr', cut_portrait = True, enter_break_labels = ['sr_no_access'], enter_labels = ['sr_enter'], exit_labels = ['sr_exit'], area = 'club', unseen = False)
    #note: button replaced by adding to rest of swingers actions
    #swingers_room.button_watch_girlfriend = swingers_room.add_button("Watch Your Girlfriend", label = "watch_girlfriend", condition = "any_client(tagged_with_any = ['girlfriend', 'hypno_girlfriend'])", unseen = False)

    # Stage
    stage = Location("Stage", 'st', cut_portrait = True, area = 'club', enter_break_labels = ['st_no_access'], enter_labels = ['st_enter'], exit_labels = ['st_exit'])

    downtown.connection_tc = downtown.add_connections(club)
    club.connection_sr_st_do = club.add_connections(swingers_room, stage, downtown)
    swingers_room.connection_tc = swingers_room.add_connections(club)
    stage.connection_tc = stage.add_connections(club)

    # Move Club Swingers to Swingers Room
    club_swingers.location = swingers_room

    ## Other
    club_swingers.change_status("prospect")
    rep_from_club.change_status("minor_character")
    club_ball_woman.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('tc_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    rep_from_club.add_stats_with_value('hypno_blowjob_count', 'hypno_swallow_count')

    # Character Specific Variables
    club_swingers.add_stats_with_value('girl_count', 'girl_outfit', 'guy_outfit', 'couple_outfit', 'orgy_count', 'hole_count', 'swingers_room_access')
    club_swingers.wait_on_message = False
    rep_from_club.add_stats_with_value('event_chain', 'pending', 'week')
    # event_chain key: 0: not started, 1: started but not resolved, 2: did not solve their problem, 3: did solve their problem, 4: didn't solve but blackmail opp open, 5: blackmail ignored, 6: blackmailed Club Pres, 7: blackmailed her, 8: spoke to her husband, 9: blackmail complete
    club.friday_event_notice = "There's an event at the Club today."
    club.action_show_message = None

    #Player Examine Phrases
    player.add_examine_phrase("player.has_tag('club_access')", "You are a member of The Club.")


    ## Actions
    club_swingers.action_girl = club_swingers.add_action( "Hook up with a girl", label = "_girl")
    club_swingers.action_guy = club_swingers.add_action( "Hook up with a guy", label = "_guy")
    club_swingers.action_couple = club_swingers.add_action( "Hook up with a couple", label = "_couple")
    club_swingers.action_orgy = club_swingers.add_action( "Check out the orgy", label = "_orgy")
    club_swingers.action_watch_girlfriend = club_swingers.add_action( "Watch your girlfriend", label = "_watch_girlfriend")
    rep_from_club.action_investigate_dalliance = rep_from_club.add_action("Investigate what she's up to", label="_investigate_dalliance", condition = "rep_from_club.can_be_interacted and rep_from_club.event_chain == 4 and club.is_here")


    ######## EXPANDABLE MENUS #######
    ## Club Ball Events
    club_ball_main_menu = ExpandableMenu("What do you want to do?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game
    club.choice_club_ball_find_blonde = club_ball_main_menu.add_choice("Find the blonde woman", "club_ball_blonde_woman")
    club.choice_club_ball_find_dark = club_ball_main_menu.add_choice("Find the dark-haired woman", "club_ball_dark_haired_woman", condition = "not club_ball_woman.has_tag('impregnated')")
    club.choice_club_ball_find_gloria = club_ball_main_menu.add_choice("Find Gloria the Club President's Wife", "club_ball_gloria", condition = "not gloria.has_tag('club_ball_do_something_else')")
    club.choice_club_ball_find_sam = club_ball_main_menu.add_choice("Try and find Sam the Barista", "club_ball_sam", condition = "player.has_tag('barista_ball_event_possible') and not samantha.has_tag('club_ball_do_something_else')")
    club.choice_club_ball_join_line = club_ball_main_menu.add_choice("Join the line up", "club_ball_rep_from_club_bj", condition = "player.has_tag('rep_from_club_bj_possible')")
    club.choice_club_ball_join_couple = club_ball_main_menu.add_choice("Join the couple you helped", "club_ball_rep_from_club_bondage", condition = "player.has_tag('rep_from_club_bondage_possible') and not rep_from_club.has_tag('club_ball_do_something_else')")
    club.choice_club_ball_watch_crowd = club_ball_main_menu.add_choice("Watch the crowd", "club_ball_crowd")
    club.choice_club_ball_leave = club_ball_main_menu.add_choice("Leave", "club_ball_leave")
    club.choice_club_ball_find_hannah = club_ball_main_menu.add_choice("Try and find Hannah the School Principal", "club_ball_hannah", condition = "hannah.has_tag('masquerade_ball_invite') and not hannah.has_tag('masquerade_ball_complete') and not hannah.has_tag('masquerade_ball_watched')")

    ## Rep from Club Blackmail Menu
    rep_from_club_blackmail_menu = ExpandableMenu("Who do you want to talk to about this?", cancelable = False)
    rep_from_club.choice_blackmail_her = rep_from_club_blackmail_menu.add_choice("Her", "rep_from_club_blackmail_her")
    rep_from_club.choice_blackmail_her_husband = rep_from_club_blackmail_menu.add_choice("Her husband", "rep_from_club_blackmail_her_husband", condition = "geri.g_status == 2")
    rep_from_club.choice_blackmail_club_president = rep_from_club_blackmail_menu.add_choice("Club President", "rep_from_club_blackmail_club_president")
    rep_from_club.choice_blackmail_no_one = rep_from_club_blackmail_menu.add_choice("No one", "rep_from_club_blackmail_no_one")

  return

# Initial Contact Message
# OBJECT: Check Messages
label tc_message:
  if gloria.show_or_ball == 1:
    "There's a special event at the Club this Friday.  All members are invited to join us for a Masquerade Ball.  Drop by and enjoy the fun!"
  else:
    "There's a special event at the Club this Friday.  A special Show Extravaganza is being presented for the enjoyment of our members.  Drop by and enjoy the fun!"
  if not gloria.has_tag('club_ball_first_message'):
    extend " Special events at the Club are planned to occur about once a month on Fridays."
    add tags 'club_ball_first_message' to gloria
    $ club.friday_event_notice = "Today is the day of a special event at the Club."
    $ club.show_event_note = add_note((gloria.show_week - 4) * 5, "Club Special Event", exact = True)
    $ club.show_event_note = add_note(gloria.show_week * 5, "Club Special Event", exact = True)
  rem action
  return

label club_swingers_message:
  swinger_h "{i}Hi. My wife and I have an open marriage. Normally we swing with other couples, but sometimes we'll play with just one other person.{/i}"
  swinger_h "{i}My wife saw your profile and wants to hire you for an evening. She says she wants to be fucked by a professional wife fucker!{/i}"
  swinger_h "{i}I'll be there, but I don't have to join in unless you want. Let me know if you're available!{/i}"
  swinger_h "{i}PS my wife has no need for training. She's a perfect hot wife! This is for her enjoyment.{/i}"
  "This may not be your preferred clientèle, but it is a paying gig."
  $ title = "Accept the engagement?"
  menu:
    "Yes (Ends Day)":
      $ club_swingers.change_status("minor_character")
      #call forced_movement(client_house) # not needed
      wt_image swinger_1
      "You meet them at their house."
      swinger_h "Hi, I'm Pat. I'm so glad you could come. Come. Get it? It's an old swingers joke. Come on in."
      wt_image swinger_2
      swinger_h "This is my wife, Patricia."
      swinger_w "Yes, I know. He's Pat, I'm Patricia. We share everything. Why not a name?"
      "The two of them laugh together comfortably. They seem to share a good relationship, along with a bad sense of humor."
      swinger_w "But you're not here to chat. You're here to fuck me. I have to say, I've never been fucked by a professional wife fucker. I'm quite looking forward to it. Where do we start?"
      $ player.swinger_club_access_count = 0
      $ title = "Where do you start?"
      menu:
        "Pleasure her":
          player.c "Normally I deal with women who want to get better at pleasing their man, but I understand from your husband that he has nothing to complain about."
          wt_image swinger_3
          player.c "That being the case, and since this evening is supposed to be about you, how about you lie back and let me pleasure you?"
          swinger_w "Oooooohh!  That sounds like fun!"
          wt_image swinger_4
          "Before long, she's shuddering to an orgasm at the end of your tongue, flooding your mouth with her juices."
          swinger_w "Ooohhhh  gaawwwwdddd!!!"
          swinger_w "That felt incredible.  Please, I have to feel you inside me."
          $ club_swingers.orgasm_count += 1
          $ player.swinger_club_access_count += 1
          $ player.desire_action_count += 1
        "Have her pleasure you":
          player.c "I like to start by finding out what the wife knows about pleasing a man."
          wt_image swinger_5
          player.c "Show me how you suck cock, Patricia."
          swinger_w "Mmmmm.  Yes, Sir."
          wt_image swinger_6
          swinger_w "Pat really loves it when I swirl my tongue around the head of his cock. Don't you honey?"
          swinger_h "I do indeed, sweetie."
          "The rest of the blow job goes much the same way, with Patricia talking to her husband as she blows you. She's pretty good at giving head, but it's hard to instruct her on how to get better while she's maintaining a constant chatter with Pat."
          player.c "Okay, Patricia. That gives me a good sense of your oral skills. Time to show me how you fuck a man."
          swinger_w "Oooooh!  I can't wait to feel you inside me!"
      wt_image swinger_7
      "You sit down and Patricia climbs on top of you. She starts bouncing up and down on your cock as you play with her tits."
      swinger_w "I think my husband is feeling left out. Is it okay if he joins us?"
      $ title = "Let him join in?"
      menu:
        "No way":
          player.c "No way.  I'm here to fuck you only."
          swinger_w "Sorry honey. I tried."
          wt_image swinger_8
          "Patricia's eyes start to close as her pleasure mounts. She rides your cock to an intense orgasm, after which you climax yourself."
          swinger_w "Ooohhhh  gaawwwwdddd!!!"
          player.c "[player.orgasm_text]"
          $ club_swingers.orgasm_count += 1
        "He can only touch Patricia":
          player.c "Okay, but no touching me."
          wt_image swinger_9
          "Pat comes over and starts sucking his wife's tits as you fuck her."
          swinger_w "Gawd.  That feels incredible.  Let's switch.  I want Pat inside me."
          wt_image swinger_10
          "A moment later, Patricia is sucking your cock while her husband fucks her.  Tonight was supposed to be about her, and she sure looks happy as she shudders to an orgasm on her husband's cock with your cock filling her mouth."
          swinger_w "Ooohhhh  gaawwwwdddd!!!"
          "Soon she receives both of your loads as she sighs in contentment."
          player.c "[player.orgasm_text]"
          swinger_h "Nnnnnnnnnn"
          swinger_w "Mmmmm.  Thank you, gentlemen.  That was wonderful!"
          $ club_swingers.orgasm_count += 1
          $ player.swinger_club_access_count += 1
        "Let him touch you":
          player.c "Okay"
          wt_image swinger_9
          "Pat comes over and starts sucking his wife's tits as you fuck her."
          swinger_w "Gawd, that feels incredible.  Pat, you should feel what his cock feels like.  Would you mind fucking my husband?"
          $ title = "Fuck his ass?"
          menu:
            "Yes":
              "This is her night. If she wants to see your cock in her husband's ass, so be it."
              wt_image swinger_11
              "Pat fingers his wife and licks her tits as you push yourself into his ass. This isn't the first time he's taken a dick back there, and he easily relaxes his sphincter enough to give you easy access."
              swinger_w "Mmmmm. That feels so nice, Pat. Doesn't his cock feel great?"
              wt_image swinger_12
              swinger_w "You must need some relief, honey. Shift up here so I can give your cock some attention while he's fucking you."
              wt_image swinger_13
              "Patricia sucks off her husband while you fuck his ass. Just when you think he's about to cum, she pulls off."
              swinger_w "Not yet, honey. My turn now."
              $ player.male_sex_count += 1
              $ player.swinger_club_access_count += 1
            "No":
              player.c "No. I'm okay with him touching me, but I'm not fucking him."
              swinger_w "Okay, but let's switch now. I want to feel Pat inside me."
          wt_image swinger_10
          "Patricia lies down and starts sucking your cock while her husband fucks her."
          swinger_w "Ohhhh his cock is so good.  Pat, you have to taste it!"
          wt_image swinger_14
          "She passes your cock to her husband, who starts sucking on you. This isn't the first time he's sucked cock. He's pretty good, possibly better than his wife."
          $ player.swinger_club_access_count += 1
          $ title = "Where do you cum?"
          menu:
            "Cum on her":
              wt_image swinger_16
              "Patricia orgasms first, followed by her husband, who shoots his seed over her belly."
              swinger_w "Ooohhhh  gaawwwwdddd!!!"
              swinger_h "Nnnnnnnnnn"
              "You pull out of his mouth and deposit your seed with his over his wife's body. Patricia sighs in contentment as she feels the warmth of your loads on her skin."
              player.c "[player.orgasm_text]"
              swinger_w "Mmmmm. Thank you gentlemen. That was wonderful!"
              $ club_swingers.orgasm_count += 1
            "Cum on him":
              wt_image swinger_15
              "Pat seems to like sucking cock, so you assume he'll like your semen too."
              swinger_w "Ooohhhh that is so hot!!!  Oohhh gaaawdddd!!!!"
              "Patricia shudders to an intense orgasm as she watches your seed spill onto her husband's face."
              player.c "[player.orgasm_text]"
              $ club_swingers.orgasm_count += 1
              $ player.swinger_club_access_count += 1
        "Blow him":
          player.c "Come here, Pat."
          wt_image swinger_17
          "As he approaches, you open your mouth. He pulls his already hard dick out of his pants and you wrap your lips around it.  His wife climbs off of you and starts sucking your cock while watching you suck her husband."
          swinger_w "Oh gawd, that is so hot!!  You have to fuck my husband's ass now.  Please?"
          $ player.swinger_club_access_count += 1
          $ player.male_sex_count += 1
          $ title = "Fuck his ass?"
          menu:
            "Yes":
              "This is her night. If she wants to see your cock in her husband's ass, so be it."
              wt_image swinger_11
              "Pat fingers his wife and licks her tits as you push yourself into his ass. This isn't the first time he's taken a dick back there, and he easily relaxes his sphincter enough to give you easy access."
              swinger_w "Mmmmm. That feels so nice, Pat. Doesn't his cock feel great?"
              wt_image swinger_12
              swinger_w "You must need some relief, honey. Shift up here so I can give your cock some attention while he's fucking you."
              wt_image swinger_13
              "Patricia sucks off her husband while you fuck his ass. Just when you think he's about to cum, she pulls off."
              swinger_w "Not yet, honey. My turn now."
              $ player.swinger_club_access_count += 1
            "No":
              player.c "No. I'm okay with getting him excited, but I'm not fucking him."
              swinger_w "Okay, but let's switch now. I want to feel Pat inside me."
          wt_image swinger_10
          "Patricia lies down and starts sucking your cock while her husband fucks her."
          swinger_w "Ohhhh his cock is so good.  Pat, you have to taste it!"
          wt_image swinger_14
          "She passes your cock to her husband, who starts sucking on you. This isn't the first time he's sucked cock. He's pretty good, possibly better than his wife."
          $ player.swinger_club_access_count += 1
          $ title = "Where do you cum?"
          menu:
            "Cum on her":
              wt_image swinger_16
              "Patricia orgasms first, followed by her husband, who shoots his seed over her belly."
              swinger_w "Ooohhhh  gaawwwwdddd!!!"
              swinger_h "Nnnnnnnnnn"
              "You pull out of his mouth and deposit your seed with his over his wife's body. Patricia sighs in contentment as she feels the warmth of your loads on her skin."
              player.c "[player.orgasm_text]"
              swinger_w "Mmmmm. Thank you gentlemen. That was wonderful!"
              $ club_swingers.orgasm_count += 2
            "Cum on him":
              wt_image swinger_15
              "Pat seems to like sucking cock, so you assume he'll like your semen too."
              swinger_w "Ooohhhh that is so hot!!!  Oohhh gaaawdddd!!!!"
              "Patricia shudders to an intense orgasm as she watches your seed spill onto her husband's face."
              player.c "[player.orgasm_text]"
              $ club_swingers.orgasm_count += 1
              $ player.swinger_club_access_count += 1
      wt_image swinger_1
      swinger_h "Thanks for showing my wife such a great time.  You're worth every penny you charge."
      if not player.has_tag('club_access') and player.swinger_club_access_count > 1:
        if player.has_tag('supersexy') or player.swinger_club_access_count > 2:
          swinger_h "My wife and I are members of The Club. It's downtown. Very exclusive. Membership is by invitation only. You'd be perfect. Would you like us to sponsor you for membership?"
          wt_image swinger_18
          swinger_w "Don't bother asking, honey. I'm already calling them. You'll fit in perfectly!"
          add tags 'club_access' to player
      if player.swinger_club_access_count > 1:
        "He gives you a tip, doubling your normal fee for a session.  Their payment will clear at the end of the week."
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        $ player.extra_clients_fee_this_week += 50
      else:
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        "Their payment for your services will clear at the end of the week."
        $ player.extra_clients_fee_this_week += 25
      $ club_swingers.sex_count += 1
      orgasm notify
      $ living_room.remove_action(club_swingers.current_client_action) # note: this could be done with "rem action"
      end_day
    "Not yet":
      "You have until the end of week [club_swingers.accept_limit] to accept this engagement."
      $ club_swingers.current_client_action.name = "Reply to Club Swingers"
      if not club_swingers.wait_on_message:
        $ club_swingers.wait_on_message = True
        $ club_swingers.message_note = add_note((club_swingers.wait_for_message_period + 1) * 5, "{} offer ends".format(club_swingers.name))
    "Never (Deletes Message)":
      $ club_swingers.change_status("rejected")
  return

# Character Rejected
label club_swingers_rejected:
    sys "You may no longer accept this assignment."
    return

# Display Portrait
# Rep from Club
label rep_from_club_update_media:
    $ rep_from_club.change_image('rep_from_club_event_1_2')
    return


########### CHARACTER ACTIONS ###########
# Club Swingers Examine
label club_swingers_examine:
    wt_image sr_orgy_1_1
    "You have access to a wide variety of people who are in various forms of 'exploring' themselves. Be it a woman, a man, a couple, or even an orgy. The choice is yours."
    return

# Club Swinging - Hook Up With Girl
label club_swingers_girl:
    $ club_swingers.girl_count += 1
    $ club_swingers.girl_outfit += 1
    if club_swingers.girl_outfit > 6:
        $ club_swingers.girl_outfit = 1
    if club_swingers.girl_outfit == 1:
        wt_image sr_girl_1_1
        if club_swingers.girl_count == 1:
            club_patron_4 "Hi. I haven't seen you here before. My boyfriend's off playing with someone else. Did you want to hook up?"
        else:
            club_patron_4 "Hi. I haven't seen you for a while. Did you want to hook up again?"
        $ title = "Hook up with her?"
        menu:
            "Yes":
                wt_image sr_girl_1_2
                club_patron_4 "Let's go somewhere a little more private. I hate having other people bump up against me when I'm having sex."
                wt_image sr_girl_1_3
                "Finding a quiet corner of the room, she starts kissing you. One thing leads to another, and soon you're feeling up her pussy. First she loses her panties as you push them to the side ..."
                wt_image sr_girl_1_4
                "... then she loses her inhibitions, too."
                wt_image sr_girl_1_5
                "She smiles up at you as she releases your cock from your pants."
                if club_swingers.girl_count == 1:
                    wt_image sr_girl_1_12
                    club_patron_4 "I love that moment, just before you suck a cock for the first time."
                else:
                    wt_image sr_girl_1_13
                    club_patron_4 "As I recall, you taste pretty good."
                wt_image sr_girl_1_6
                "She can't quite get all of you into her mouth..."
                wt_image sr_girl_1_14
                "... but she does her best with the parts she can fit in."
                wt_image sr_girl_1_15
                "When your dick is hard and throbbing, she lies back and removes her clothes."
                wt_image sr_girl_1_7
                club_patron_4 "Fuck me now."
                wt_image sr_girl_1_8
                club_patron_4 "Ohh, that feels good!"
                wt_image sr_girl_1_9
                club_patron_4 "Damn, that feels really good. Yes, just like that, harder, harder!!"
                wt_image sr_girl_1_16
                club_patron_4 "Oh damn yeeesssss!!!!!!"
                wt_image sr_girl_1_17
                club_patron_4 "Mmmmm.  Your turn now.  Feel free to use my face."
                wt_image sr_girl_1_10
                player.c "[player.orgasm_text]"
                wt_image sr_girl_1_11
                club_patron_4 "I can't wait to tell my boyfriend how much fun I had tonight!  Let's do this again, sometime."
                $ club_swingers.sex_count += 1
                $ club_swingers.orgasm_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.girl_outfit == 2:
        wt_image sr_girl_4_1
        "A pretty Asian woman in a schoolgirl skirt smiles shyly when she catches you looking at her."
        wt_image sr_girl_4_2
        club_patron_3 "Hi.  My husband says this outfit makes me look like a nasty slut.  What do you think?"
        wt_image sr_girl_4_3
        club_patron_3 "A few of my girlfriends and I thought it would be fun if we all dressed up as schoolgirls today.  Do you think it makes me look like the kind of nasty slut who would suck a stranger's cock?"
        wt_image sr_girl_4_4
        club_patron_3 "Tell me what you think I am."
        $ club_swingers_girl_asian_woman = False
        $ title = "What do you think she is?"
        menu menu_club_patron_3_1:
            "A woman who should be sucking your cock" if not club_swingers_girl_asian_woman:
                wt_image sr_girl_4_11
                club_patron_3 "Mmmm.  You're right, Sir.  I'm definitely dressed like the type of woman who should be sucking your cock.  Tell me what I look like to you."
                $ club_swingers_girl_asian_woman = True
                $ title = "What does she look like to you?"
                jump menu_club_patron_3_1
            "A nasty cocksucking slut":
                wt_image sr_girl_4_5
                club_patron_3 "Mmmmmm"
                "Seems that was the right answer."
                wt_image sr_girl_4_6
                club_patron_3 "Nasty little sluts should get fucked, shouldn't they?"
                wt_image sr_girl_4_12
                "You see no reason to say no.  She pulls off her top and skirt and bends over, her wet snatch stretching easily to accept you inside.."
                wt_image sr_girl_4_7
                club_patron_3 "Bang me hard and tell me what a dirty slut I am."
                player.c "You're a nasty little cocksucking slut."
                club_patron_3 "Yes, more!"
                player.c "You're a dirty Asian whore who likes to get on her knees and suck off strangers."
                club_patron_3 "Yes, yes, more! Tell me how bad I am!"
                player.c "You're a horny piece of fuckmeat meant to take dick."
                player.c "You'd like every dick in this place inside you, wouldn't you?"
                player.c "You want every one of your holes dripping with cum so you can show your husband what a filthy piece of meat you really are."
                wt_image sr_girl_4_8
                club_patron_3 "Oh yeesss! Fuuuuccckkk!!!"
                "Her orgasm is so intense, it pulls you over the edge with her."
                player.c "[player.orgasm_text]"
                orgasm notify
                wt_image sr_girl_4_9
                club_patron_3 "Come here and let this dirty piece of meat clean off your cock."
                wt_image sr_girl_4_10
                club_patron_8 "Ann, we have to get going. We need to get the babysitter home and we have to stop at the store first to get the twins the supplies they need for their school project."
                wt_image sr_girl_4_13
                # club_patron_3 "Shit. That's my husband. Time to go."
                club_patron_3 "Sorry, honey. Just let me grab my clothes. I have a sales coupon in my purse for the school supplies. Can you see if you can find it while I get dressed?"
                $ club_swingers.sex_count += 1
                $ club_swingers.orgasm_count += 1
                orgasm notify
            "A bored housewife":
                wt_image sr_girl_4_2
                club_patron_3 "Never mind."
                "She gets up and wanders off. You'll have to keep searching."
                wt_image current_location.image
                change player energy by -energy_very_short notify
            "Too old to be wearing a schoolgirl outfit":
                wt_image sr_girl_4_2
                club_patron_3 "Never mind."
                "She gets up and wanders off. You'll have to keep searching."
                wt_image current_location.image
                change player energy by -energy_very_short notify
    elif club_swingers.girl_outfit == 3:
        wt_image sr_girl_3_1
        "A short blonde woman seems to be searching the room."
        wt_image sr_girl_3_2
        "She looks like she's lost someone."
        wt_image sr_girl_3_3
        player.c "Excuse me. Are you looking for someone? And no, I don't mean that as a pick up line"
        "She laughs."
        club_patron_2 "Yes, I was looking for my husband."
        wt_image sr_girl_3_4
        "Before you can respond, she drops to her knees and takes out your cock."
        club_patron_2 "Do you mind if I just blow you? I don't like to sleep with men without telling my husband first, and I'm not sure where he is."
        $ title = "Let her blow you?"
        menu:
            "Yes":
                wt_image sr_girl_3_5
                "She forms a circle with her fingers and starts stroking the shaft as she licks and sucks the head. Before long she's bobbing swiftly up and down on your cock. It seems she wants to get this blow job over quick."
                wt_image sr_girl_3_6
                "She's pretty good, and she succeeds at bringing you to orgasm fast. She looks up at you as you fill her mouth with your seed."
                player.c "[player.orgasm_text]"
                wt_image sr_girl_3_7
                club_patron_2 "I hope that was okay?  I really need to go find my husband."
                player.c "It was great.  Good luck finding him."
                $ club_swingers.blowjob_count += 1
                $ club_swingers.swallow_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.girl_outfit == 4:
        wt_image sr_girl_2_1
        "A blonde woman is dancing by herself."
        wt_image sr_girl_2_2
        "She may have had too much to drink."
        wt_image sr_girl_2_3
        "She notices you and teeters over."
        club_patron_4 "Want to fuck?"
        $ title = "Fuck her?"
        menu:
            "Yes":
                wt_image sr_girl_2_4
                "She drops to her knees and takes out your cock. She doesn't even take off her shoulder bag."
                wt_image sr_girl_2_5
                club_patron_4 "Mmmm .... hard cock."
                wt_image sr_girl_2_6
                club_patron_4 "I'm horny. Finger fuck me?"
                "At this point, you're in no mood to say no."
                wt_image sr_girl_2_7
                "She pulls your hand to her mouth and starts sucking your fingers as she spreads her legs."
                wt_image sr_girl_2_8
                club_patron_4 "Yes, yes, yes, yes .... yeeeesssss"
                wt_image sr_girl_2_9
                club_patron_4 "You can fuck me now."
                "Her voice is slurred and sleepy sounding.  The orgasm ... and the drinking ... has taken its toll on her."
                wt_image sr_girl_2_10
                "She doesn't completely pass out while you're fucking her.  At least you don't think she does."
                "When you finish, she mumbles something incoherent, that may have involved finding her husband and time to go home.  It was hard to tell."
                player.c "[player.orgasm_text]"
                $ club_swingers.orgasm_count += 1
                $ club_swingers.sex_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.girl_outfit == 5:
        # one time only event
        if club_swingers.girl_count == 5:
            wt_image sr_girl_5_1
            "One of the women in the room doesn't seem to be enjoying herself."
            player.c "Is something wrong?"
            club_patron_2 "It's just my asshole husband. I can't believe he's over there in the corner making out with that skank. Does he think I can't see him? He know what I think of her."
            wt_image sr_girl_5_2
            club_patron_2 "Oh my god! Did she just blow a kiss at me while my husband's fucking her?"
            club_patron_2 "That skanky bitch!! She did that on purpose to piss me off. I can't believe that asshole is putting his cock inside her!"
            wt_image sr_girl_5_3
            "She squats down in front of you and pulls out your cock."
            club_patron_2 "Oh good. It's already hard. Will you do me a favor and fuck me?"
            $ title = "Fuck her?"
            menu:
                "Yes":
                    wt_image sr_girl_5_5
                    club_patron_2 "Fuck me hard. Fuck me harder than he's fucking that skank."
                    "You do your best."
                    wt_image sr_girl_5_4
                    club_patron_2 "That's it. He wants me to be a whore so he can fuck little tramps. All right then, treat me like a whore. Slap my ass as you fuck me."
                    "*smack*"
                    club_patron_2 "Yes. Do it again. Harder."
                    "*SMACK*"
                    club_patron_2 "More!"
                    "*SMACK*  *SMACK*  *SMACK*"
                    wt_image sr_girl_5_6
                    player.c "[player.orgasm_text]"
                    club_patron_2 "Do you hear this, asshole!?  I'm over here getting fucked by a real man!!!"
                    "You have a suspicion that you won't see her or her husband back here again. At least not together."
                    $ club_swingers.sex_count += 1
                    orgasm notify
                "No":
                    wt_image current_location.image
                    "This might be a bit more drama than you need.  You move on."
                    change player energy by -energy_very_short notify
                "No, but leave your dick in her mouth":
                    wt_image sr_girl_5_7
                    "She's so preoccupied her husband and the other woman that she doesn't seem to notice that you didn't answer her.  Instinctively, she continues to pleasure your cock as she watches them ... with predictable results."
                    wt_image sr_girl_5_8
                    player.c "[player.orgasm_text]"
                    "She startles just a moment as you flood her mouth with cum, then wraps her lips tight around your shaft and swallows, her eyes still locked on the other couple in the corner."
                    wt_image sr_girl_5_9
                    club_patron_2 "Hey, asshole!  I just got a mouthful of jizz from a real man!!!  Maybe I'll let all the real men in here cum in my mouth!"
                    "You have a suspicion that you won't see her or her husband back here again. At least not together."
                    $ club_swingers.blowjob_count += 1
                    $ club_swingers.swallow_count += 1
                    orgasm notify
        else:
            $ club_swingers.girl_outfit += 1
    # this is purposefully "if" not "elif" so that advancement past count 5 triggers this event
    if club_swingers.girl_outfit == 6:
        wt_image sr_girl_6_1
        "A dark-haired woman and her partner are surveying the room."
        wt_image sr_girl_6_13
        "He leans in and whispers something in her ear and she turns and she turns and looks at you."
        wt_image sr_girl_6_2
        "A big grin on her face she turns back to him ..."
        wt_image sr_girl_6_3
        "... and gives him a deep, intense kiss."
        wt_image sr_girl_6_4
        club_patron_8 "My boyfriend thinks you should fuck me. How about it?"
        $ title = "Fuck her?"
        menu:
            "Yes":
                wt_image sr_girl_6_5
                "She strips naked and spreads her legs on a bench in the middle of the room. Apparently she's not interested in privacy."
                club_patron_8 "Rub your cock along my cunt. Get my clit excited."
                wt_image sr_girl_6_6
                club_patron_8 "Oh shit yeah, that's it!"
                wt_image sr_girl_6_7
                club_patron_8 "Fuck. I am so wet! Fuck me now."
                wt_image sr_girl_6_14
                club_patron_8 "FUCK Yes! Slam it into me."
                wt_image sr_girl_6_9
                club_patron_1 "Does that feel good, honey? Having his big cock inside you, fucking you?"
                "You have no idea who the other woman is. If your partner knows, she doesn't bother to introduce you. She just starts rubbing her clit."
                club_patron_8 "Yes, FUCK, it feels GREAT!  Aahhh ... Aahhh ..."
                wt_image sr_girl_6_8
                "... aAAAHHH!!"
                wt_image sr_girl_6_15
                "As her orgasm subsides, she sits up and takes you into her mouth ..."
                wt_image sr_girl_6_16
                "... then she lies back, pulling you forward until you're straddling over her."
                club_patron_8 "Cum on me!  Show my boyfriend how much you enjoyed fucking me"
                wt_image sr_girl_6_11
                player.c "[player.orgasm_text]"
                wt_image sr_girl_6_12
                club_patron_8 "Fuck that was good! I hope my boyfriend wants me to fuck you again soon."
                $ club_swingers.orgasm_count += 1
                $ club_swingers.sex_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    return

# Club Swinging - Hook Up With Guy
label club_swingers_guy:
    $ club_swingers.guy_outfit += 1
    if club_swingers.guy_outfit > 3:
        if club_swingers.guy_outfit == 4:
            if club_swingers.has_tag('cock_tease'):
                $ club_swingers.guy_outfit = 1
        else:
            $ club_swingers.guy_outfit = 1
    if club_swingers.guy_outfit == 1:
        wt_image sr_guy_1_1
        "Most of the men in the Swingers Room are straight. After asking around, however, you find a guy who's sufficiently 'hetero-flexible' to offer to jerk you off."
        $ title = "Let him jack you off?"
        menu:
            "Yes":
                wt_image sr_guy_1_5
                "He seems impressed by the size of your member ..."
                wt_image sr_guy_1_3
                "... and you're impressed by his skill with his hands.  He soon coaxes the cum out of your balls ..."
                wt_image sr_guy_1_3
                player.c "[player.orgasm_text]"
                wt_image sr_guy_1_4
                "... and you thank him by depositing the remainder of your load over this chest. Some of the women in the audience are impressed."
                club_patron_1 "Oh wow! That is so hot!!"
                club_patron_4 "Mmmm. I would love to watch my husband do that."
                "Some of the guys are, too."
                club_patron_3 "Can I have a turn?"
                $ club_swingers.handjob_count += 1
                $ player.male_sex_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.guy_outfit == 2:
        wt_image sr_guy_2_1
        "Most of the men in the Swingers Room are straight. After asking around, however, you find a guy who's sufficiently 'hetero-flexible' to offer to suck you off."
        $ title = "Let him blow you?"
        menu:
            "Yes":
                wt_image sr_guy_2_2
                "He starts off teasing your balls with some gentle licks of his tongue ..."
                wt_image sr_guy_2_6
                "... then shifts to teasing the head of your dick."
                wt_image sr_guy_2_3
                "When you've taken as much teasing as you can, you trap his head with his hand and force your dick into his mouth."
                wt_image sr_guy_2_4
                "Once you've asserted control, he begins sucking you in earnest, bobbing his head back and forth along your cock.  After the prolonged teasing, you soon feel your balls start to boil over."
                wt_image sr_guy_2_7
                "Sensing your excitement growing, he positions his face directly underneath you.  The invitation is clear."
                wt_image sr_guy_2_5
                player.c "[player.orgasm_text]"
                wt_image sr_guy_2_8
                club_patron_10 "My wife is going to love seeing your jizz on my face."
                "It seems everyone's going to end up happy."
                $ club_swingers.blowjob_count += 1
                $ club_swingers.facial_count += 1
                $ player.male_sex_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.guy_outfit == 3:
        wt_image sr_guy_3_1
        "Most of the men in the Swingers Room are straight. After asking around, however, you find a guy who's sufficiently 'hetero-flexible' to agree to hook up with you."
        club_patron_8 "You can fuck my ass if you jerk me off while you do so."
        $ title = "Agree?"
        menu:
            "Yes":
                wt_image sr_guy_3_2
                "You lube up your cock and slowly push it into his tight rosebud ..."
                wt_image sr_guy_3_3
                "... then you take hold of his cock and stroke him off as you pump in and out of his ass."
                wt_image sr_guy_3_4
                "As he starts to cum, you point his cock towards him. His load shoots up and over his belly, as you let your own load empty into his butt."
                player.c "[player.orgasm_text]"
                club_patron_8 "Ohhhh! Fuck that feels good!"
                wt_image sr_guy_3_1
                club_patron_8 "If you see me with my girlfriend later, don't tell her what we did. I promised her I'd give up guys."
                $ club_swingers.anal_count += 1
                $ club_swingers.orgasm_count += 1
                $ player.male_sex_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.guy_outfit == 4:
        wt_image sr_guy_4_12
        "Most of the men in the Swingers Room are straight. After asking around, however, you find a guy who's sufficiently 'hetero-flexible' to let you suck him off."
        club_patron_10 "I won't touch you, but I'll let you suck my cock, if you want?"
        $ title = "Suck him off?"
        menu:
            "Yes":
                wt_image sr_guy_4_1
                "He sits down in front of you and spreads his legs."
                club_patron_10 "You're looking forward to having my dick in your mouth, aren't you?  I think you should beg me for the privilege.  Get on your knees and beg for my cock."
                $ title = "What do you do?"
                menu:
                    "Beg for his cock":
                        "You kneel down on the floor between his knees."
                        player.c "May I suck your cock?"
                        club_patron_10 "Beg properly, and show some respect."
                        player.c "Please, Sir, may I be allowed to suck your cock?  I'm so looking forward to taking you into my mouth."
                        wt_image sr_guy_4_2
                        club_patron_10 "Will you do a good job, boy?  If I let you put my cock in your mouth, will you make my cock feel good?"
                        player.c "Yes, Sir.  I'll give you the best blowjob I can."
                        wt_image sr_guy_4_3
                        club_patron_10 "I'm not sure you're properly appreciative of this opportunity, boy.  Prove to me you really want this."
                        player.c "Please, Sir.  Let me taste your cock.  I really, really want to suck you off.  I promise I'll make it feel great for you."
                        wt_image sr_guy_4_4
                        club_patron_10 "Okay, boy.  You've convinced me.  I'll let you taste my cock."
                        "The pre-cum is dripping out of his cock as he presents it to you."
                        wt_image sr_guy_4_13
                        "You lower your head and lick the pre-cum off him, only to have it replaced by a heavier flow as he feels your tongue on him."
                        wt_image sr_guy_4_9
                        "Impatiently, he grips you by the back of the head and forces his cock between your lips."
                        "Your begging has turned him on.  After only a few hard thrusts of his cock, he lets out a loud, deep groan and fills your mouth with cum."
                        club_patron_10 "Aaaaghhh!!!!"
                        wt_image sr_guy_4_10
                        "As he pulls his cock out, you can see it's still covered with his cum."
                        club_patron_10 "Clean up the mess you made, boy."
                        "Obediently, you finish servicing him by licking the cum off his now semi-soft dick while he gently pats you on the head.  As you finish licking off the last of the cum, you feel his cock start to stir back to life."
                        wt_image sr_guy_4_11
                        club_patron_10 "I enjoyed that.  You have my permission to come back and beg for my cock again sometime.  I almost feel like using you again right now, but I need to be able to get it up for my wife later tonight."
                        $ player.male_sex_count += 1
                        change player energy by -energy_short notify
                    "Refuse":
                        wt_image sr_guy_4_2
                        club_patron_10 "That's okay.  You don't have to beg with words."
                        "He stands up, removes his shirt, and pulls down his pants ..."
                        wt_image sr_guy_4_3
                        "... then he presents his hardening cock to you."
                        club_patron_10 "I can see in your eyes how much you want this"
                        wt_image sr_guy_4_4
                        "His cock gets harder as you get close, and pre-cum drips out in excitement as he anticipates the feel of your lips on him."
                        $ title ="What do you do?"
                        menu:
                            "Leave":
                                wt_image sr_guy_4_5
                                "You bail, leaving him hanging ... literally.  He yells after you."
                                club_patron_10 "Cock tease!"
                                add tags 'cock-tease' to club_swingers
                            "Just use your hand":
                                wt_image sr_guy_4_6
                                "He's disappointed when you take him in your hand. You promised him a blow job, and he was looking forward to feeling your mouth on his cock."
                                "His disappointment doesn't last too long, however, as you start stroking his hard shaft, gently at first, then faster and faster as his breathing gets more and more ragged."
                                wt_image sr_guy_4_7
                                "He lets out a deep groan as you pump the cum out of his cock and onto his belly."
                                club_patron_10 "Aaaaghhh!!!!"
                                wt_image sr_guy_4_8
                                club_patron_10 "That was nice.  It would be even better if you could blow me next time."
                                $ club_swingers.orgasm_count += 1
                                $ player.male_sex_count += 1
                                change player energy by -energy_short notify
                            "Suck him off":
                                wt_image sr_guy_4_9
                                "As you lean in to take him into your mouth, he puts his hand on your head.  He guides your head up and down his shaft, moving you faster and faster as his breathing gets more and more ragged."
                                club_patron_10 "Oh yeah. That's fucking good!"
                                "Suddenly he lets out a loud, deep groan as he fills your mouth with cum."
                                club_patron_10 "Aaaaghhh!!!!"
                                wt_image sr_guy_4_10
                                "As he pulls his cock out, you can see it's still covered with his cum."
                                $ title = "What do you do?"
                                menu:
                                    "Lick him clean":
                                        "You clean up the mess you left on his cock while he strokes your head thankfully. As you finish licking off the last of the cum, you feel his cock start to stir back to life."
                                        wt_image sr_guy_4_11
                                        club_patron_10 "Shit. I could almost have another go, but my wife would kill me if I couldn't get it up for her tonight."
                                    "Nothing":
                                        wt_image sr_guy_4_2
                                        "He fumbles around for some tissue to clean himself up before stuffing himself back into his pants."
                                        club_patron_10 "Thanks for that. If you ever want to suck me off again, let me know."
                                $ player.male_sex_count += 1
                                $ club_swingers.orgasm_count += 1
                                change player energy by -energy_short notify
                    "Leave":
                        wt_image current_location.image
                        "You decide to keep searching."
                        change player energy by -energy_very_short notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    return

# Club Swinging - Hook Up With Couple
label club_swingers_couple:
    $ club_swingers.couple_outfit += 1
    if club_swingers.couple_outfit > 3:
        $ club_swingers.couple_outfit = 1
    if club_swingers.couple_outfit == 1:
        wt_image sr_couple_1_1
        "A man and woman are making out near a number of other couples."
        wt_image sr_couple_1_2
        "The woman suddenly sits up."
        club_patron_9 "Let's find another guy to join us."
        club_patron_9 "Hey, you, would you like to join my husband and me in a threesome?"
        $ title = "Join them?"
        menu:
            "Yes":
                wt_image sr_couple_1_3
                club_patron_9 "Come over here and I'll suck you hard while my hubby gets me warmed up."
                wt_image sr_couple_1_4
                club_patron_9 "Oh good. You get hard easy. I want both your cocks inside me."
                wt_image sr_couple_1_5
                "She climbs up on top and straddles you as her husband positions himself behind her. She's wet, and you slide into her easily as she impales herself on your hard shaft."
                wt_image sr_couple_1_6
                "Her husband's entrance is a little more difficult. She groans and grimaces as he shoves himself into her ass."
                wt_image sr_couple_1_11
                club_patron_9 "Oohhhhh!"
                wt_image sr_couple_1_7
                "Once he's inside her, though, her groans take on a different character."
                club_patron_9 "Ooohhh ... yes! Fuck me! Fuck me both of you!! Fuck my ass! Fuck my pussy!"
                wt_image sr_couple_1_8
                club_patron_9 "Ooohhhh FFFFUCCCKKK!!!!"
                "She collapses into a heap on top of you as she's rocked by an intense orgasm, but manages to squeak out a request."
                club_patron_9 "Don't cum yet. I want it on me."
                wt_image sr_couple_1_9
                "Still breathing hard from her orgasm, she kneels down between you. She pumps the first sprays of cum out of her husband's cock and onto her face as she looks up at you and licks her pussy juice off your shaft."
                wt_image sr_couple_1_10
                "A moment later, you finish the process of turning her face into a sticky mess."
                player.c "[player.orgasm_text]"
                club_patron_9 "Thanks, guys. That was fucking amazing!"
                $ club_swingers.orgasm_count += 1
                $ club_swingers.sex_count += 1
                $ club_swingers.facial_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.couple_outfit == 2:
        wt_image sr_couple_2_1
        club_patron_2 "Hi! My husband is looking for another man to help him fuck me hard. Would you like to help him?"
        $ title = "Help him?"
        menu:
            "Yes":
                wt_image sr_couple_2_2
                club_patron_2 "Great! Give him 15 minutes to get me ready, and we'll meet you in the private room over there."
                wt_image sr_couple_2_3
                "When you arrive, he has her stripped to her panties and blindfolded."
                club_patron_10 "She seems like a classy lady when you first meet her, but she's actually a dirty whore who loves the feel of a stranger's cock inside her."
                "He grabs her by the hair and pulls her head back sharply."
                club_patron_10 "Isn't that right, whore?"
                club_patron_2 "Yes, Sir."
                club_patron_10 "Don't leave the man's cock waiting, whore. Get it hard."
                "Unable to see, she fumbles around blindly until her hands find your crotch. As she strokes your stiffening rod, you squeeze her tit."
                club_patron_10 "Don't worry about being gentle. The rougher you are, the more she likes it. Isn't that right, whore?"
                club_patron_2 "Yes, Sir."
                wt_image sr_couple_2_4
                club_patron_10 "Tell him what you want, whore."
                club_patron_2 "I want your dick inside me. I want you to fuck me hard while I suck my husband's cock."
                "He pulls off her panties and turns her around to give you easy access. The smell of her arousal is obvious, and you slide easily into her sopping cunt. As you enter her, he pulls off her blindfold."
                club_patron_10 "Take a look, whore. Take a look at your whore cunt being fucked by another man's cock."
                wt_image sr_couple_2_5
                "She mewls with pleasure as you slam into her. There's no need to warm her up, as she's already soaking wet, so you simply begin jackhammering into her."
                "Her husband takes hold of her hair and holds her head down on his cock as you fuck her. It only takes moments for her to start trembling as an orgasm builds inside her."
                wt_image sr_couple_2_6
                club_patron_10 "Look at me whore. Look at me while another cock fucks you. You're ready to cum now, aren't you whore?"
                club_patron_2 "Mmmm hhmmm"
                club_patron_10 "You're going to cum with your husband's cock in your mouth and another man's dick in your cunt."
                club_patron_2 "Mmmmmm MMMMmmmm!!!!!"
                wt_image sr_couple_2_7
                "As her orgasm subsides, her husband pulls out and empties his load on her face."
                club_patron_10 "Cum on her face, if you don't mind."
                "You don't mind, and it seems she doesn't either."
                player.c "[player.orgasm_text]"
                club_patron_10 "You like cum on your face, don't you whore?"
                club_patron_2 "Yes, Sir."
                wt_image sr_couple_2_8
                "As she pulls her clothes back on she smiles at you."
                club_patron_2 "That was fun! I hope you can join us again sometime soon."
                $ club_swingers.orgasm_count += 1
                $ club_swingers.sex_count += 1
                $ club_swingers.facial_count += 1
                orgasm notify
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    elif club_swingers.couple_outfit == 3:
        wt_image sr_couple_3_1
        "A woman is sipping a glass of wine in a relatively quiet corner of the room."
        club_patron_11 "My husband just went to fill his glass. Would you care to keep me company until he returns?"
        wt_image sr_couple_3_2
        club_patron_11 "As you long as you don't mind him joining us, I'm sure he'd let me thank you for your companionship. I was starting to get bored."
        $ title = "Keep her company?"
        menu:
            "Yes":
                wt_image sr_couple_3_3
                club_patron_11 "Honey, this nice man has been keeping me from getting lonely while you were refilling your drink. He's been a real gentleman. He hasn't grabbed my tits or my ass or my pussy, although I have to admit my pussy is a little disappointed."
                club_patron_11 "And I've been a perfect lady, and haven't felt up his cock or his ass. If we let you join is, is it okay if we fuck?"
                club_patron_7 "Well, since you've both been so good, I don't see why not."
                wt_image sr_couple_3_4
                club_patron_11 "Thank you, honey."
                "As she kisses him, he lifts up the front of her dress, which is your cue to fondle her hairless, and panty-less, pussy."
                wt_image sr_couple_3_5
                "Her husband takes over between her legs, shoving first one, then two fingers into her snatch."
                club_patron_11 "Ooohhh"
                "Breathing deeply, she starts fondling both of you as he finger fucks her."
                wt_image sr_couple_3_6
                "She surprises you with a quick kiss as she pulls out your cock."
                wt_image sr_couple_3_7
                "Then she squats down and takes your cock into her mouth."
                wt_image sr_couple_3_8
                "After a moment she switches to her husband's cock ..."
                wt_image sr_couple_3_9
                "... before standing up and leaning over."
                club_patron_11 "Can he fuck me while I suck you, honey?"
                club_patron_7 "Fucking right he can."
                wt_image sr_couple_3_10
                "It's an arrangement that seems to work for everyone."
                wt_image sr_couple_3_11
                "Turns out, however, that she wants more. She pulls off of you and rolls over, her voice husky with lust as she addresses you."
                club_patron_11 "Will you put it in my ass?"
                $ title = "Fuck her ass?"
                menu:
                    "Absolutely":
                        wt_image sr_couple_3_12
                        club_patron_11 "Oh yes!!  Now both of you at once!"
                        wt_image sr_couple_3_15
                        "She climbs onto her husband's lap and rides his cock as you continu to plow her ass.  It feels great, but it seems it feels even better to her. She grasps her husband tightly as she shudders to orgasm first."
                    "No, you want to stick to her pussy":
                        wt_image sr_couple_3_13
                        club_patron_11 "Okay, let me ride you while my husband reams my ass."
                        wt_image sr_couple_3_14
                        "Apparently DP'ing his wife is thirsty work, as he finishes his wine while plowing her tight asshole. You, on the other hand, have the much easier job of sitting and enjoying her sopping wet cunt riding up and down your shaft."
                        wt_image sr_couple_3_15
                        "It seems she's enjoying things the most, however. She grasps you tightly as she shudders to orgasm first."
                club_patron_11 "Aaaaahhhhhh ggaaawwwwdddd ... that feels good!!!"
                wt_image sr_couple_3_16
                "You don't have to wait long for it to be your turn. She kneels in front of you and offers you her face."
                player.c "[player.orgasm_text]"
                wt_image sr_couple_3_17
                club_patron_11 "Wow, guys. I need a drink after that for sure."
                "As she toys with your cum on her face, you see her husband's cum running down her leg."
                $ club_swingers.orgasm_count += 1
                $ club_swingers.sex_count += 1
                $ club_swingers.facial_count += 1
            "No":
                wt_image current_location.image
                "You decide to keep searching."
                change player energy by -energy_very_short notify
    return

# Club Swinging - Check Out Orgy
label club_swingers_orgy:
    $ club_swingers.orgy_count += 1
    if club_swingers.orgy_count > 4:
        $ club_swingers.orgy_count = 1
    wt_image sr_orgy_[club_swingers.orgy_count]_1
    "It doesn't take long to find the orgy taking place in the back of the Swingers Room."
    wt_image sr_orgy_[club_swingers.orgy_count]_2
    "There's sex taking place at the front of the Swingers Room. There's nothing but sex taking place here in the back."
    wt_image sr_orgy_[club_swingers.orgy_count]_3
    "Through the writhing mass of humanity, it's sometimes hard to tell where one coupling ends and the next one begins."
    $ title = "What do you want to do?"
    menu:
        "Join in":
            $ club_swingers.hole_count += 1
            if club_swingers.hole_count > 3:
                $ club_swingers.hole_count = 1
            if club_swingers.hole_count == 1:
                wt_image sr_hole_[club_swingers.orgy_count]_1
                "She doesn't offer you her name, but she does offer you her mouth. It's an offer you're happy to take her up on."
                "To the sounds of moaning and groaning all around you, you fill her mouth with cum."
                player.c "[player.orgasm_text]"
                $ club_swingers.blowjob_count += 1
                $ club_swingers.swallow_count += 1
                orgasm notify
            elif club_swingers.hole_count == 2:
                wt_image sr_hole_[club_swingers.orgy_count]_2
                "It takes a little bit of searching, but you eventually find an empty orifice."
                player.c "Excuse me, is this hole taken?"
                "When she shakes her head no, you proceed to fill her emptiness."
                player.c "[player.orgasm_text]"
                $ club_swingers.sex_count += 1
                orgasm notify
            elif club_swingers.hole_count == 3:
                wt_image sr_hole_[club_swingers.orgy_count]_3
                "In most places, it takes a lot of time and effort to find even one mouth to put your cock in."
                "At the orgy, a hard cock can often attract the attention of more than one interested party."
                player.c "[player.orgasm_text]"
                $ club_swingers.blowjob_count += 1
                orgasm notify
        "Just watch":
            wt_image sr_orgy_[club_swingers.orgy_count]_4
            "You wander around for a while, picking your way amongst the bewildering variety of human sizes and shapes."
            wt_image sr_orgy_[club_swingers.orgy_count]_5
            "Most seem to be enjoying themselves ..."
            wt_image sr_orgy_[club_swingers.orgy_count]_6
            "...despite - or perhaps partially because of - the other people moaning and groaning around them."
            change player energy by -energy_short notify
        "Leave":
            pass
    return

# Club Swinging - Watch Girlfriend
label club_swingers_watch_girlfriend:
    $ title = "Watch your girlfriend"
    #$ selected_girlfriend = renpy.display_menu(items = [(p.name, p) for p in get_people(tagged_with_any = ['girlfriend', 'hypno_girlfriend'])] + [('Cancel', False)])
    $ selected_girlfriend = renpy.display_menu(items = [(p.name, p) for p in get_people(tagged_with_any = ['in_swingers_room_now'])] + [('Cancel', False)])

    if selected_girlfriend:
        $ current_target = selected_girlfriend
        call expression (current_target.short_name + "_watch") from _call_expression_3
    return

# Rep from Club Examine
label rep_from_club_examine:
    "A married woman from the Club."
    return

########### OBJECTS ###########
# N/A

########### TIMERS ###########
## Common Timers
# Start Day - Club
# note: start labels need to be added manually and can be called anything; this one was added in Pregame above
label tc_start_day:
  ## Tuesday and Club Show this Week?
  if day == 2 and week >= gloria.show_week and gloria.show_week > 0:
    $ gloria.show_week = week + 4
    $ gloria.show_or_ball += 1
    if gloria.show_or_ball > 2:
      $ gloria.show_or_ball = 1
    add tags 'show_friday' to gloria
    if gloria.has_tag('club_ball_first_message'):
      $ club.friday_event_notice = "Today is the day of a special event at the Club."
      $ club.show_event_note = add_note(gloria.show_week * 5, "Club Special Event", exact = True)
    $ club.action_show_message = living_room.add_action("Message from the Club", label = club.short_name + "_message", context = '_check_messages')
    notify "You received a new message today."
    notify
  ## Friday and Club Show this Week?
  if day == 5 and gloria.has_tag('show_friday'):
    "[club.friday_event_notice]"
    $ living_room.remove_action(club.action_show_message)
  return

# End Day
# note: using this for room related end day actions as end_day is auto-added for Persons only
label club_swingers_end_day:
    if player.has_tag('club_visited_today'):
        $ club.visit_count += 1
        rem tags 'club_visited_today' 'stage_visited_today' from player
        # rem tags 'maid' 'showgirl' from diamond ## deal with this in her end_day label
        ## replaced the system below with
        #python:
            #for c in [jasmine, lauren, bree, cassandra, diamond, fairyn, gloria, janice, marilyn, master_m, nicole, rae, samantha, tracy]:
                #c.remove_tag('in_club')
        call club_character_returns_and_dismissals from _call_club_character_returns_and_dismissals  # this is in case day ends without you leaving the club and therefore triggering tc_exit
    if player.has_tag('club_access') and not player.has_tag('club_first_visit_complete') and not player.has_tag('club_first_visit_message'):
        add tags 'club_first_visit_message' to player
        sys "You now have access to the Club, which can be reached from Downtown. You should visit at least once if you want to activate options associated with Club membership."
    return

label rep_from_club_end_day:
    ## Check for New Prospects - Rep 2 and Dom? (Club Couple Event)
    if player.reputation >= 2 and rep_from_club.event_chain == 0 and player.has_tag('dominant') and player.has_tag('club_first_visit_complete'):
        $ rep_from_club.event_chain = 1
    # Timer to pace events
    if rep_from_club.event_chain == 4:
        $ rep_from_club.event_chain = 5
    return

label club_ball_woman_end_day:
    pass
    return

# End Week
# note: using this for room related end day actions as end_week is auto-added for Persons only
label club_swingers_end_week:
    if gloria.has_tag('show_friday'):
        rem tags 'show_friday' from gloria
    return

label rep_from_club_end_week:
    pass
    return

label club_ball_woman_end_week:
    pass
    return

## Club and Stage Labels
label rep_from_club_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if rep_from_club.has_tag('in_club_now'):
            $ rep_from_club.location = club # returns her to club
    else:
        ## Follow up from Club Couple?
        if rep_from_club.pending == 3 and rep_from_club.week < week:
            call rep_from_club_follow_up from _call_rep_from_club_follow_up
        ## Club Couple Event for Dom?
        elif rep_from_club.event_chain < 2 and player.has_tag('dominant') and player.reputation >= 2:
            call rep_from_club_talk_chain from _call_rep_from_club_talk_chain
        ## Blackmail opp after problem not resolved
        elif rep_from_club.event_chain == 2 and rep_from_club.week < week:
            call rep_from_club_dalliance from _call_rep_from_club_dalliance
    return

label rep_from_club_club_send_home:
    call character_location_return(rep_from_club) from _call_character_location_return_730
    return

## Character Specific Timers
# Rep From Club Talk Event
label rep_from_club_talk_chain:
  summon rep_from_club no_follows
  # Initial Conversation
  if rep_from_club.pending == 0:
    $ rep_from_club.event_chain = 1
    wt_image rep_from_club_event_1_1
    "A young couple approach you as you enter the Club."
    rep_from_club.c "Hi. Are you the man they call the Wife Trainer? My husband and I have a problem we thought you may be able to help us with."
    if rep_from_club.has_tag('gave_you_ball_bj'):
      player.c "Don't I know you from somewhere?"
      husband_rep_from_club "Did you line up for one of my wife's blow jobs at the Club Ball? I wasn't keen on the idea at first, but it turned out to be really hot."
      rep_from_club.c "I was right about that, but still haven't been able to convince him to listen to me about this."
    rep_from_club.c "He wants to fuck me in the ass, and the whole idea of that is totally repugnant to me. But I love the idea of him forcing his will on me and making me do what he wants."
    rep_from_club.c "The problem is, he says he loves me too much, and can't stand the idea of hurting me. He wants everything we do together to be consensual, and wants me to voluntarily let him have anal sex with me. Which I won't."
    rep_from_club.c "So we're at a bit of an impasse. Do you think you could help?"
    $ title = "What do you tell them?"
    menu:
      "Okay":
        call rep_from_club_couple_event from _call_rep_from_club_couple_event
      "My standard fees apply":
        player.c "It'll cost you 25 for the session, more if additional sessions are required."
        rep_from_club.c "Oh.  Of course. We'll talk about it, and let you know."
        "Check back next week to see if they're ready to hire you."
        $ rep_from_club.pending = 2
        $ rep_from_club.week = week
      "Not right now":
        $ rep_from_club.pending = 1
      "Tell them to leave you alone":
        "You don't have time for their problems.  You have other things you want to get done."
        $ rep_from_club.pending = 5
        $ rep_from_club.event_chain = 2
        $ rep_from_club.week = week + 1
  # If you told them not yet
  elif rep_from_club.pending == 1:
    "The couple that asked for your help is here."
    $ title = "What do you do?"
    menu:
      "Help them":
        player.c "I've decided I will help you out."
        rep_from_club.c "Great!"
        call rep_from_club_couple_event from _call_rep_from_club_couple_event_1
      "Ask to be paid":
        player.c "I've decided I will help you out. It'll cost you 25 for the session, more if additional sessions are required."
        rep_from_club.c "Oh.  Of course. We'll talk about it, and let you know."
        "Check back next week to see if they're ready to hire you."
        $ rep_from_club.pending = 2
      "Not right now":
        pass
      "Tell them to leave you alone":
        "You tell them to leave you alone. You're not interested in solving their problems."
        $ rep_from_club.pending = 5
        $ rep_from_club.event_chain = 2
        $ rep_from_club.week = week + 1
  # if you asked them to pay you
  elif rep_from_club.pending == 2 and rep_from_club.week < week:
    wt_image rep_from_club_event_1_1
    "The couple that asked for your help is here."
    if not rep_from_club.has_tag('agreed_to_pay'):
      add tags 'agreed_to_pay' to rep_from_club
      rep_from_club.c "Hi. We've talked it over, and we've decided its worth hiring you. Can we get started now?"
    else:
      rep_from_club.c "Are you able to help us now?"
    $ title = "What do you do?"
    menu:
      "Okay":
        call rep_from_club_couple_event from _call_rep_from_club_couple_event_2
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        $ player.extra_clients_fee_this_week += 25
        notify
      "Not right now":
        pass
      "Tell them to leave you alone":
        "You tell them to leave you alone. You're not interested in solving their problems."
        $ rep_from_club.pending = 5
        $ rep_from_club.event_chain = 2
        $ rep_from_club.week = week + 1
  call character_location_return(rep_from_club) from _call_character_location_return_731
  return

# Rep From Club Couple Event
label rep_from_club_couple_event:
  wt_image rep_from_club_event_1_32
  "The Club has a number of private rooms that are well stocked for just these events. You ask the husband to wait and take his wife into the private room."
  player.c "Are you sure you want to do this?  You want me to convince your husband to 'force' himself on you?"
  rep_from_club.c "Yes, I'm sure."
  player.c "What do you think he should to do bend you to his will?"
  rep_from_club.c "Whatever it takes. Tie me up so I can't fight him off. Punish me to the point that I'm afraid to disobey him."
  player.c "Are you sure you can take that?"
  rep_from_club.c "If it's coming from him, yes. I know he loves me, and that I'll always be his precious flower."
  rep_from_club.c "I think that's what makes it so exciting, to think about him taking instead of asking. To have him think only about what he wants for a moment, and not about what I want."
  player.c "Even if it means he rapes your ass?"
  wt_image rep_from_club_event_1_2
  rep_from_club.c "That part scares the hell out of me. I'm trying to focus just on the exciting part, otherwise I'll get cold feet and call all of this off."
  wt_image rep_from_club_event_1_32
  $ title = "What do you do?"
  menu:
    "Hypnotize her" if player.test('hypnosis_level', 0):
      $ rep_from_club.hypno_session() # deducts energy and records she was hypno'd
      player.c "I'll help you, but you need to follow instructions."
      call focus_image from _call_focus_image_3
      player.c "Look at this. Look at this and listen to my words. Only my words now."
      wt_image rep_from_club_event_1_3
      player.c "Let's get comfortable.  Remove your top and show me your breasts while we talk."
      wt_image rep_from_club_event_1_36
      player.c "You should let your husband fuck you in the ass. You don't need him to force you."
      wt_image rep_from_club_event_1_37
      rep_from_club.c "No. I don't want to be fucked in the ass. It'll hurt and I'll hate it."
      player.c "You haven't tried it yet. Trust me, you'll like it."
      wt_image rep_from_club_event_1_4
      rep_from_club.c "No. I did try. Multiple times with another boyfriend. I hate it. I haven't told my husband, because he'd get jealous."
      player.c "He shouldn't have to force you to get what he wants from his wife."
      rep_from_club.c "If he wants this enough, he should take it from me. I love him. I won't mind him taking what he needs from me. But I won't give him this."
      "It seems you're not getting anywhere further on this topic, but at least you learned a tidbit about her past."
      $ title = "What do you do?"
      menu:
        "Have her blow you":
          player.c "I'm going to help you and your husband. I'm going to help you, and in return, you want to compensate me properly."
          if rep_from_club.pending == 2:
            rep_from_club.c "We paid your fee. I think that's fair compensation."
            "Even hypnotized, her sense of fair play is telling her that paying the fee you asked for is appropriate compensation. You're not going to get anywhere further with her on this topic."
          else:
            rep_from_club.c "That's fair. What do you want?"
            "You take out your cock."
            wt_image rep_from_club_event_1_38
            rep_from_club.c "Should my husband suck you too?"
            wt_image rep_from_club_event_1_39
            player.c "I'll discuss that with him. You do the right thing and compensate me fairly for helping you."
            wt_image rep_from_club_event_1_40
            "It's not a particularly enthusiastic blow job, but she maintains adorable, hypnotized eye contact with you the whole time, and you soon fill her mouth with jizz."
            wt_image rep_from_club_event_1_5
            player.c "[player.orgasm_text]"
            $ rep_from_club.hypno_blowjob_count += 1
            $ rep_from_club.hypno_swallow_count += 1
            #add tags 'got_blowjob' to rep_from_club ## disabled because this was while hypnotized so she doesn't remember, plus you have a better way to solve their problem through the 'past_revealed' tag
            orgasm
        "Get her ready for her husband":
          pass
      wt_image rep_from_club_event_1_2
      "You command her to forget being hypnotized and release her from her trance."
      add tags 'past_revealed' to rep_from_club
    "Ask to be compensated":
      if player.has_tag('supersexy'):
        if rep_from_club.pending == 2:
          player.c "I know you and your husband have paid me for my work, but we have a few minutes here alone. Just the two of us."
        else:
          player.c "We have a few minutes here alone.  Just the two of us."
        player.c "I don't suppose you could think of some way to - compensate - me?  Say, in a personal way?  As a way of recognizing how much good I'm going to do for your marriage?"
        wt_image rep_from_club_event_1_33
        "She laughs."
        rep_from_club.c "Women fall all over themselves to sleep with you, don't they?"
        player.c "Some do, yes.  I'm really hoping you fall into that category."
        wt_image rep_from_club_event_1_7
        "She slips out of her clothes and onto her knees in front of you."
        rep_from_club.c "I guess I do. But maybe not for the reason you think? I have NEVER cheated on my husband."
        rep_from_club.c "And I wouldn't be cheating on him now. Except I'm worried that he may need a push to get him willing to treat me the way I want him to treat me."
        rep_from_club.c "So yes, I will blow you. And then you can tell him what a naughty girl I was. And maybe that will convince him to have his way with me?"
        "She wouldn't be the first woman to use faulty logic to justify in her own mind why she needs to have sex with you. You hope she's reading her husband correctly on this topic."
        call rep_from_club_couple_event_compensation from _call_rep_from_club_couple_event_compensation
      else:
        if rep_from_club.pending != 2:
          player.c "I think I should be compensated, for helping you and your husband, don't you?"
          rep_from_club.c "What do you mean? With money?"
          player.c "I was hoping for a more personal show of appreciation. As a way of thanking me for helping your marriage."
          wt_image rep_from_club_event_1_7
          "She thinks for a moment. Then she slips out of her clothes and onto her knees in front of you."
          rep_from_club.c "Okay. I can do that. But maybe not for the reason you think? I have NEVER cheated on my husband."
          rep_from_club.c "And I wouldn't be cheating on him now. Except I'm worried that he may need a push to get him willing to treat me the way I want him to treat me."
          rep_from_club.c "So yes, I will blow you. And then you can tell him what a naughty girl I was. And maybe that will convince him to have his way with me?"
          call rep_from_club_couple_event_compensation from _call_rep_from_club_couple_event_compensation_1
        else:
          player.c "I think I should be compensated, for helping you and your husband, don't you?"
          wt_image rep_from_club_event_1_2
          rep_from_club.c "We've already agreed to pay you. If you're suggesting I compensate you more 'in kind', I wouldn't feel comfortable doing that to my husband without his knowledge."
    "Have her kneel" if player.has_tag('dominant'):
      wt_image rep_from_club_event_1_2
      player.c "Remove your clothes and get on your hands and knees.  Here, in front of me."
      wt_image rep_from_club_event_1_6
      "She doesn't hesitate."
      player.c "How often do you need this? To kneel at a man's feet?"
      rep_from_club.c "Not often. I don't want to be someone's slave. It's just sometimes, I feel this urge to have a strong man take me, you know?"
      player.c "I could train you as my submissive, on a part time basis. Would you like that?"
      wt_image rep_from_club_event_1_2
      rep_from_club.c "I ... I can't believe how wet that thought makes me. But - please don't take offense - I would really prefer to have my husband treat me like this."
      wt_image rep_from_club_event_1_6
      player.c "Good. Then let's work on that."
      add tags 'knelt' to rep_from_club
    "Just get her ready":
      pass
  wt_image rep_from_club_event_1_10
  "You use some of the Club's well stocked playtoys to get her ready to receive her husband. Then you leave her to wait and anticipate what comes next. You return to where her nervous husband has been waiting for you."
  husband_rep_from_club "Is she really going to go through with this?"
  player.c "Yes, she is. She wants this very much. How about you? Are you ready to go through with this?"
  husband_rep_from_club "I don't know. I don't know if I can really do what she wants. Force her, that is."
  player.c "Have you ever dominated a woman?"
  husband_rep_from_club "Never. I've never wanted to hurt someone."
  wt_image rep_from_club_event_1_11
  player.c "So you've never used one of these before?"
  husband_rep_from_club "A riding crop?  No, never."
  "It's a well used crop from the Club's supplies, but it will still do the job."
  player.c "You talked about hurting someone. And this will. But it won't harm them. Not when used properly. And it's designed to cause pain with a purpose. It exerts control, whether you're using it on a horse, or a woman."
  player.c "Not that I would ever use one on a horse. That would be cruel. But on a woman - a woman who's given her consent. That's different."
  wt_image rep_from_club_event_1_12
  "You take back the crop, and demonstrate it's use on the unsuspecting table ... *thwapp*"
  player.c "What do you think happens once you hit her with this?"
  husband_rep_from_club "She hates me? I feel like an abuser?"
  player.c "No. She wants you to do this. What happens is that you're in control. You feel it. She feels it. It hurts her, yes, but she's a strong woman. The pain will recede. What remains is a burning desire to please you."
  husband_rep_from_club "So that I don't hit her again."
  player.c "Eventually. At first she'll want you to hit her again. And again. To show her you mean it. After that, yes, she'll be desperate to do whatever she needs to do to please you. Including letting you fuck her ass."
  husband_rep_from_club "I don't know. I said I'd try and work with you to deal with this impasse in our sex life. But I just can't see me hurting her."
  $ rep_from_club.temporary_count = 1
  if rep_from_club.has_tag('knelt'):
    player.c "Do you know what your wife did, when I took her into the private room? She took off her clothes and knelt at my feet, naked and on all fours. Like a slavegirl waiting for her Master."
    husband_rep_from_club "Why?"
    player.c "Because I told her to."
    husband_rep_from_club "Because you made her!"
    player.c "No. If you want her ass, that you're going to have to make her do. This she did willingly, because it excited her. I could smell her arousal as she waited at my feet."
    player.c "But she didn't want to be at my feet. She wants to be at yours. I know. I checked."
    player.c "I offered to satisfy this need of hers. I told her she could come to me when she feels the need to submit and I'll dominate her, and use her the way she wants to be used."
    player.c "She turned me down, because she doesn't want that from just anyone. She wants it from you. Holding out on you for anal may just be her way of prodding you into giving her what she needs."
    player.c "If I was you - if you love her and value your marriage - I'd give her what she needs."
    husband_rep_from_club "Okay"
    wt_image rep_from_club_event_1_13
    "He takes the crop from you, a hesitant look on his face."
    husband_rep_from_club "Okay. This is important to her.  Let's go give her what she wants."
    $ rep_from_club.temporary_count = 0
  elif rep_from_club.has_tag('past_revealed'):
    player.c "She's had anal sex with other men."
    husband_rep_from_club "What?  Who?"
    player.c "Your wife. Before she married you. She let other boyfriends fuck her in the ass."
    husband_rep_from_club "She never told me that. Why would she let them do that, and not let me? She knows how much I want to try this!"
    player.c "I don't know for sure, but I can guess. Because they insisted. Because they wouldn't take no for an answer. That's what she wants from you. Make her give you her ass. That's what she's been telling you, isn't it?"
    husband_rep_from_club "Yes"
    wt_image rep_from_club_event_1_13
    "He takes the crop from you, a steely, hurt look on his face."
    husband_rep_from_club "Okay. If I have to beat her to get her to offer up to me the ass she's already given to other men, then let's go beat her."
    $ rep_from_club.temporary_count = 0
    add tags 'husband_angry' to rep_from_club
  elif rep_from_club.has_tag('got_blowjob'):
    player.c "She gave me oral sex."
    husband_rep_from_club "What?  Who?"
    player.c "Your wife. Just a moment ago, when we were alone. She dropped down to her knees and blew me while you waited outside."
    husband_rep_from_club "We didn't discuss her doing that! She's a cheater? You're telling me my wife cheats on me!"
    player.c "No, actually, I don't think so. I believe it was completely out of character for her. She knew I was going to tell you. She even told me to tell you."
    husband_rep_from_club "Why???"
    player.c "Because she was worried you wouldn't go through with this. She knows you well. She knew you might get cold feet and back out because you didn't want to hurt her."
    player.c "So I think she did it to give you a push. To make you angry with her. To make you want to punish her."
    husband_rep_from_club "It worked."
    wt_image rep_from_club_event_1_13
    "He takes the crop from you, a steely, slightly angry look on his face."
    husband_rep_from_club "Okay. She wants me to punish her. Let's go punish her. Let's go teach her that sucking off other men is NOT okay with me."
    $ rep_from_club.temporary_count = 0
    add tags 'husband_angry' to rep_from_club
  if rep_from_club.temporary_count == 0:
    wt_image rep_from_club_event_1_14
    "He enters the room and discovers his wife the way you left her, bound and gagged with the Club's equipment. He stops short in shock."
    wt_image rep_from_club_event_1_15
    player.c "How does she look right now? What do you think she's feeling?"
    if rep_from_club.has_tag('husband_angry'):
      "The anger he felt entering the room seems to dissipate instantly. He is a nice guy, and he clearly loves her."
    husband_rep_from_club "She looks vulnerable. Scared. Like she needs me to rescue and protect her."
    player.c "Close. She's feeling very vulnerable, because she knows in this position she can't stop you from doing anything you want to her."
    player.c "She's also scared, terrified actually, because she doesn't know what you're going to do with her now that you have her like this."
    player.c "But she doesn't want you to rescue or protect her. She already knows that you'll protect her. She trusts you. She knows you'll keep her safe, or she wouldn't have given you this gift. You don't have to prove that to her."
    player.c "What she wants is for you to accept the gift of her vulnerability. She wants to be your everything. She wants you to know that you can take what you want from her, for your own pleasure, without worrying about what she wants."
    wt_image rep_from_club_event_1_16
    husband_rep_from_club "So she's ready to have anal sex with me?"
    player.c "Not yet. That would still be her giving you voluntarily something she doesn't want to do."
    player.c "You have to make her give it to you. She's given you permission to do whatever you have to with her to convince her to meet your needs."
    player.c "She doesn't expect you to be gentle. As scared as she is about what's about to happen, she doesn't even want you to be gentle. You've made love to her gently many times, I expect. She wants to see another side of you."
    husband_rep_from_club "So should I start beating her now?"
    wt_image rep_from_club_event_1_17
    player.c "Let's start with that."
    "You direct him on how to use the flogger safely."
    player.c "Avoid the face. Aim for the muscled fleshy areas of her body."
    wt_image rep_from_club_event_1_18
    "*thwapp*"
    rep_from_club.c "Mmmmppphh"
    "She grunts into her gag as the first blow lands."
    player.c "That's it. Now gradually increase the force of the blows."
    wt_image rep_from_club_event_1_19
    "*thwapp* ... *thwapp* ... *thwapp*"
    rep_from_club.c "Mmmmppphh  ... Mmmmppphh"
    player.c "That's it.  How does that feel?"
    husband_rep_from_club "Surprisingly good. I never thought I'd enjoy hurting someone, especially someone I love, but it's kind of fun watching her squirm like this."
    wt_image rep_from_club_event_1_20
    "*THWAPP* ... *THWAPP* ... *THWAPP*"
    rep_from_club.c "MMMPPHH  MMPPHH!!"
    "He rains the blows down on her in steady, consistent pace, each one a little harder than the last."
    husband_rep_from_club "Is this what you've been waiting for?"
    if rep_from_club.has_tag('got_blowjob'):
      husband_rep_from_club "Is this the punishment you were hoping for when you sucked this man's cock?"
    if rep_from_club.has_tag('knelt'):
      husband_rep_from_club "Is this what you were fantasizing about when you knelt down at this man's feet?"
    wt_image rep_from_club_event_1_21
    player.c "I think she's ready to give you what you want now."
    husband_rep_from_club "Is that right?  Are you ready to offer your ass to me?"
    rep_from_club.c "Mmmm  Mmmm  Mmmm"
    wt_image rep_from_club_event_1_22
    "You help guide her to her knees as her husband pulls up her dress. Scooping up some lube, he shoves it roughly into her ass with two fingers as she grunts into the gag."
    rep_from_club.c "Mmmpphh"
    if rep_from_club.has_tag('got_blowjob'):
      husband_rep_from_club "Guess what, honey?"
      husband_rep_from_club "Taking your ass isn't the only thing I want from you right now."
      husband_rep_from_club "You want to be a bad girl and suck another man's cock?  All right then. I have a confession to make. I've always wanted to see you suck off another man."
      husband_rep_from_club "So show me how you did it. Show me how you sucked him off. And while you're doing that, I'm going to fuck you in the ass."
      wt_image rep_from_club_event_1_23
      "You remove the gag from her mouth."
      player.c "Are you going to do as he says? Are you going to suck my cock again?"
      "Very quietly, she responds."
      rep_from_club.c "{size=-5}Yes{/size}"
      wt_image rep_from_club_event_1_24
      "You pull her mouth down over your cock ..."
      wt_image rep_from_club_event_1_25
      "... as her husband shoves himself into her ass."
      rep_from_club.c "Mmmmpppphhhh"
      wt_image rep_from_club_event_1_26
      "She gives a much more enthusiastic blow job this time than her previous effort. Before long, you've filled her mouth with cum."
      player.c "[player.orgasm_text]"
      $ rep_from_club.blowjob_count += 1
      $ rep_from_club.swallow_count += 1
      orgasm
    else:
      wt_image rep_from_club_event_1_27
      "With a grunt from both of them, he pushes himself inside her."
      husband_rep_from_club "Aaahhh"
      rep_from_club.c "MMMPPHH!"
      wt_image rep_from_club_event_1_28
      "You hold her by the head as he leans into her, pounding his cock deep into her anus."
      player.c "It hurts, doesn't it, having his cock pounding away at your sore bottom?"
      "She nods."
      player.c "It feels good, too, doesn't it? Knowing that he's using you the way he wants to use you, taking what he wants from you?"
      "She nods her head meekly."
    wt_image rep_from_club_event_1_29
    "With a sudden motion, he pulls her dress up, exposing her back."
    husband_rep_from_club "Aaahhhh!!!"
    "He pulls his cock out her ass, leaving a pool of semen behind, and shoots the last few spurts of his load up and onto her bare back."
    wt_image rep_from_club_event_1_30
    "She looks shaken from the experience.  He looks a little shaken too."
    if rep_from_club.has_tag('got_blowjob'):
      "You put the ball gag back into place. She could use a little sub space right now, and being gagged will help her experience it."
    wt_image rep_from_club_event_1_31
    player.c "Give her a few minutes bound and gagged to process the experience. Hold her in your arms for part of that. Then you can untie her and talk about things when you're both ready."
    # player.c "I'll check back with you in a week or so to see how you're both making out." ## changed as they actually contact you
    if player.has_tag('rep_needed'):
      sys "Check back with them next week to see if they're ready to recommend your services."
    $ rep_from_club.pending = 3
    $ player.submission_action_count += 1
    $ player.sos_action_count += 1
    change player energy by -energy_long notify
  else:
    "You want to say something to convince him to go proceed. You try the best arguments you can think of, but it isn't enough."
    "Unfortunately, you didn't spend enough time with her, or get the right information from her to figure out how to convince her husband to go ahead."
    $ rep_from_club.pending = 5
    $ rep_from_club.event_chain = 2
  $ rep_from_club.week = week # prevents next event from activating until next week
  return

label rep_from_club_couple_event_compensation:
  wt_image rep_from_club_event_1_8
  "She proceeds to give you a passable, if not overly inspired, blow job."
  wt_image rep_from_club_event_1_9
  player.c "Look at me when I cum in your mouth."
  wt_image rep_from_club_event_1_34
  player.c "[player.orgasm_text]"
  wt_image rep_from_club_event_1_35
  "She held up her end of the bargain.  Now it's your turn to help her marriage."
  add tags 'got_blowjob' to rep_from_club
  $ rep_from_club.blowjob_count += 1
  $ rep_from_club.swallow_count += 1
  orgasm
  return

# Rep From Club Follow Up
label rep_from_club_follow_up:
  wt_image rep_from_club_event_2_1
  "The husband from the young couple you helped approaches you."
  husband_rep_from_club "Can I show you something?"
  $ title = "Go with him?"
  menu:
    "Yes":
      wt_image rep_from_club_event_2_2
      "He leads you to one of the private rooms. Inside, his wife is hanging from the ceiling, trapped in a net."
      wt_image rep_from_club_event_2_3
      husband_rep_from_club "The sex life between my wife and I is really blossoming. We're learning a lot about each other."
      wt_image rep_from_club_event_2_4
      husband_rep_from_club "For example, I've learned that I'm a bit of a sadist."
      "*THWAPP*"
      rep_from_club.c "Ow!"
      husband_rep_from_club "Maybe she always suspected as much? Maybe its even part of what drew her to me?"
      "*THWAPP*"
      rep_from_club.c "Ow!"
      wt_image rep_from_club_event_2_5
      husband_rep_from_club "Regardless, I've discovered it turns me on to whip her."
      "*THWAPP*"
      rep_from_club.c "OW!"
      husband_rep_from_club "We've learned some things about her, too."
      "*THWAPP*"
      rep_from_club.c "OW!!"
      wt_image rep_from_club_event_2_6
      husband_rep_from_club "For starters, she has hyper sensitive feet."
      "*THWAPP*"
      rep_from_club.c "AAARRGGGHHH!!!!"
      "She lets out a scream as the lashes strike her soles."
      rep_from_club.c "PLEASE!!"
      wt_image rep_from_club_event_2_7
      husband_rep_from_club "Please what?"
      rep_from_club.c "Please fuck me in the ass."
      husband_rep_from_club "That's become her safe word - or safe phrase I guess. When she can't take any more, she offers me her ass."
      wt_image rep_from_club_event_2_8
      "He lowers her to the ground and positions her on her knees, still covered in the netting. She groans as he pushes himself into her back door."
      rep_from_club.c "nnnnnnn"
      husband_rep_from_club "One of these days, I'm not going to accept her offer. I'm just going to continue beating her, until I'm tired of hearing her scream in pain."
      wt_image rep_from_club_event_2_9
      husband_rep_from_club "Are you looking forward to that day, my precious flower?"
      "She shakes her head no, but you're not sure she's telling the truth."
      "He finishes inside her with a loud groan."
      husband_rep_from_club "Aaahhhh!!!"
      wt_image rep_from_club_event_2_10
      "As he gets himself re-dressed, she rolls over to look at you, his cum still dripping out of her butt."
      rep_from_club.c "Thank you for helping us."
      $ rep_from_club.event_chain = 3
      $ rep_from_club.pending = 4
      change player energy by -energy_very_short notify
    "Not today":
      wt_image club.image
      $ rep_from_club.week = week # prevents event from re-activating until next week
    "Never":
      wt_image club.image
      $ rep_from_club.event_chain = 3
      $ rep_from_club.pending = 4
  call character_location_return(rep_from_club) from _call_character_location_return_732
  return

# Rep From Club Her with Club President Dalliance
label rep_from_club_dalliance:
    $ rep_from_club.event_chain = 4
    summon rep_from_club no_follows
    add tags 'in_club_now' to rep_from_club
    wt_image rep_from_club_dalliance_1_1
    "In the corner of the Club, you spot the wife from the couple that was looking for your help.  Perhaps she turned to the Club President for assistance, as the two of them are very close?"
    "You may want to investigate while you have the opportunity."
    return

label rep_from_club_investigate_dalliance:
    wt_image rep_from_club_dalliance_1_1
    "It's possible this conversation started with her explaining to the Club President the issue she and her husband are having ..."
    wt_image rep_from_club_dalliance_1_2
    "... but it's taken quite a different turn than your conversation with them."
    wt_image rep_from_club_dalliance_1_3
    "The Club President seems to have a very firm grasp on what he thinks the problem is ..."
    wt_image rep_from_club_dalliance_1_4
    "... and she seems unable ..."
    wt_image rep_from_club_dalliance_1_5
    "... or at least unwilling ..."
    wt_image rep_from_club_dalliance_1_6
    "... to object to his solution."
    wt_image rep_from_club_dalliance_1_7
    "The remainder of the Club President's assistance ..."
    wt_image rep_from_club_dalliance_1_8
    "... unfolds more-or-less as expected."
    wt_image club_pres_3
    "A sheepish looking Club President notices you as he's leaving"
    club_president.c "Oh, hi!  Hey ... don't mention this to Gloria, okay?  She doesn't like me playing with the members on site. 'Sends wrong message, etc etc.' It'll make for a big fight."
    wt_image rep_from_club_dalliance_1_9
    "The woman now also notices you, even though she avoids eye contact as she scurries away."
    wt_image current_location.image
    "What happens in the Club - and what you see in the Club - is meant to be kept private.  You have enough leverage from this situation, though, that you can probably safely have one conversation about it."
    call expandable_menu(rep_from_club_blackmail_menu) from _call_expandable_menu_118
    rem tags 'in_club_now' from rep_from_club
    call character_location_return(rep_from_club) from _call_character_location_return_733
    return

label rep_from_club_blackmail_her:
    $ rep_from_club.event_chain = 7
    sys "Content for this event not yet available.  Try the Club President instead."
    call expandable_menu(rep_from_club_blackmail_menu) from _call_expandable_menu_119
    return

label rep_from_club_blackmail_her_husband:
    $ rep_from_club.event_chain = 8
    sys "Content for this event not yet available.  Try the Club President instead."
    call expandable_menu(rep_from_club_blackmail_menu) from _call_expandable_menu_120
    return

label rep_from_club_blackmail_club_president:
    $ rep_from_club.event_chain = 6
    $ club_president.rewards_pending += 1
    "You leave a note for the Club President that you'd like to see him.  You suspect he'll make himself available soon."
    return

label rep_from_club_blackmail_no_one:
    $ rep_from_club.event_chain = 5
    "You decide to stick to the Club rules and keep your nose out of this."
    return

# Club Show Today
label club_show_today:
  ## change to show or ball needs to be in start day label
  # $ gloria.show_or_ball += 1
  # if gloria.show_or_ball > 2:
  #   $ gloria.show_or_ball = 1
  # Ball
  if gloria.show_or_ball == 1:
    $ gloria.ball_outfit += 1
    if gloria.ball_outfit > 3:
      $ gloria.ball_outfit = 1
    if gloria.ball_outfit == 1:
      summon gloria no_follows
      wt_image club_wife_ball_1_1
      gloria.c "Welcome to the Masquerade.  Please come in and enjoy the party.  And remember, no one is who they seem.  No names tonight, just have fun."
      "From her voice you can tell that it's Gloria the Club President's Wife behind the mask, but in the spirit of the masquerade rules, you don't address her by name."
    elif gloria.ball_outfit == 2:
      summon gloria no_follows
      wt_image club_wife_ball_2_1
      gloria.c "Welcome to the Masquerade.  Please come in and enjoy the party.  And remember, no one is who they seem.  No names tonight, just have fun."
      "From her voice you can tell that it's Gloria the Club President's Wife behind the mask, but in the spirit of the masquerade rules, you don't address her by name."
    elif gloria.ball_outfit == 3:
      wt_image club_wife_ball_3_1
      "Gloria isn't around to greet you as you enter the Club, so you make your own way in.  A Masquerade Ball is in full swing."
    wt_image club_ball_1_1
    "An assorted mix of masked characters seem to be enjoying themselves."
    if gloria.discussed_barista == 4 and tracy.opp == 0:
      summon samantha no_follows
      wt_image barista_masquerade_1
      "Across the floor you think you spot Sam the Barista ... well, former barista now ... but you're not sure."
      add tags 'barista_ball_event_possible' to player
    wt_image club_ball_2_1
    "A young blonde woman gives you a very forward look."
    if not club_ball_woman.has_tag('impregnated'):
      wt_image club_ball_3_1
      "As does a dark-haired woman lurking in the corner."
    # Adding events with club members for rep here
    if rep_from_club.event_chain < 2:
      summon rep_from_club no_follows
      wt_image rep_from_club_ball_1_1
      "And in the corner, men have started to line up in front of a woman on her knees."
      add tags 'rep_from_club_bj_possible' to player
    elif rep_from_club.event_chain == 3:
      summon rep_from_club no_follows
      wt_image rep_from_club_ball_2_1
      "And in the corner, the husband of the couple you helped is trussing up his wife."
      add tags 'rep_from_club_bondage_possible' to player
    if hannah.has_tag('masquerade_ball_invite') and not hannah.has_tag('masquerade_ball_complete'):
      summon hannah no_follows
      wt_image principal_masquerade_1_1
      "As promised, you invite Hannah to join you for the ball.  The school Principal shows up wearing a mask and very little else, and quickly disappears into the crowd of party goers, careful not to cramp your explorations by staying too close to you."
    call expandable_menu(club_ball_main_menu) from _call_expandable_menu_121
  # Show
  elif gloria.show_or_ball == 2:
    # Sam's show
    if gloria.show_count > 0 and not samantha.has_tag('show') and gloria.discussed_barista == 4:
      summon samantha
      add tags 'show' to samantha
      wt_image barista_show_1
      "The Club is shut down for today except for a show taking place at the main stage. You're surprised to see Sam on the stage. It seems her employers' are letting her learn some new skills as a public performer."
      $ title = "Stay for the show?"
      menu:
        "Take a seat and watch":
          wt_image barista_show_2
          "You settle down to see what Sam is going to get up to. From off stage you hear Gloria announce:"
          gloria.c "Ladies and Gentlemen. The hired help at work ... Temptation takes the Maid!"
          wt_image barista_show_4
          "The crowd starts clapping as the women on stage become acquainted."
          wt_image barista_show_3
          "The theme of the show may be temptation takes the maid, but the maid is showing no sign of resisting temptation."
          wt_image barista_show_5
          "The show might have been better titled The Maid Embraces Temptation."
          wt_image barista_show_6
          "Not that anyone in the audience is objecting."
          wt_image barista_show_7
          "They seem much more interested in either just watching the show or debating as to which of the women is going to take charge."
          wt_image barista_show_8
          "You hear bets being placed on whose pussy is going to be licked first."
          if player.money - player.min_money >= 25:
            $ title = "Place a bet?"
            menu:
              "25 on the maid to lick out Sam":
                add tags 'maid_first' to samantha
              "25 on Sam to lick out the maid":
                add tags 'sam_first' to samantha
              "Just watch the show":
                pass
          $ samantha.random_number = renpy.random.randint(1, 10)
          if samantha.random_number > 5:
            wt_image barista_show_9
            if samantha.has_tag('maid_first'):
              "You just place your wager in time to see Sam pull the maid's head between her legs."
              "Sam gets her cunt licked and you win 25.  Everybody's happy."
              change player money by 25
            elif samantha.has_tag('sam_first'):
              "You groan as you see Sam pull the maid's head between her legs."
              "Watching her get her cunt licked is fun, but it costs you 25."
              change player money by -25
            else:
              "You ignore the betting and sit back and watch as Sam pulls the maid's head between her legs."
            wt_image barista_show_10
            "Sam seems very pleased with the maid's service, groaning out an orgasm in near record time as the crowd applauds."
            wt_image barista_show_11
            "Now it's the maid's turn to enjoy temptation. Taking Sam by the hair, she pulls the blonde's mouth onto her waiting pussy."
            wt_image barista_show_12
            "The maid cums as quickly as Sam did, to another round of applause from the crowd."
          else:
            wt_image barista_show_11
            if samantha.has_tag('maid_first'):
              "You groan as you see the maid pull Sam's head between her legs."
              "Watching the blonde lick cunt is fun, but it costs you 25."
              change player money by -25
            elif samantha.has_tag('sam_first'):
              "You just place your wager in time to see the maid pull Sam's head between her legs."
              "Sam gets to lick cunt and you win 25. Everybody's happy."
              change player money by 25
            else:
              "You ignore the betting and sit back and watch as the maid pulls Sam's head between her legs."
            wt_image barista_show_12
            "The maid seems very pleased with the feel of temptation, groaning out an orgasm in near record time as the crowd applauds."
            wt_image barista_show_9
            "Now it's Sam's turn to receive some maid service. Taking the maid by the hair, she pulls the dark-haired woman's mouth onto her waiting pussy."
            wt_image barista_show_10
            "Sam cums as quickly as the maid did, to another round of applause from the crowd."
          wt_image barista_show_13
          "Exhausted from the show, the two performers present their slick and polished pussies to the audience, receiving a standing ovation and more than a few tips from the big gambling winners."
          wt_image barista_show_14
          "After the show, a redressed Sam catches you as you're leaving the Club."
          samantha.c "That was so much fun! I was reluctant to try it when Gloria asked me to be in her show, but then I decided, what the heck! you only live once. I'm so glad I did it. And I can't believe how many tips we got!"
          player.c "You did great up there.  Can I expect to see in you in a new show soon?"
          samantha.c "No, I don't think so. Once was enough. It was really disconcerting when people started clapping as I came. Took me right out of the mood. I'll stick to having sex in private from now on."
          samantha.c "Although having people applaud when I brought Mei to orgasm was a thrill I'll remember the rest of my life."
          $ samantha.sex_count += 1
          $ samantha.orgasm_count += 1
          rem tags 'maid_first' 'sam_first' from samantha
          change player energy by -energy_very_short notify
        "Leave":
          pass
      call club_ball_leave from _call_club_ball_leave
    # Ivy's shows
    elif gloria.show_count == 3 and ivy.has_tag('showgirl') and not ivy.has_tag('show_last_time'):
      add tags 'show_last_time' to ivy
      $ ivy.show_count += 1
      if ivy.show_count > 2:
        $ ivy.show_count = 1
      if ivy.show_count == 1:
        wt_image intro_wife_show_1_1
        "A woman in a hood waits on stage."
        wt_image intro_wife_show_1_3
        "You watch as she slips out of her hood and robe."
        wt_image intro_wife_show_1_4
        "She turns and looks to her left ..."
        summon ivy
        $ ivy.training_session()
        wt_image intro_wife_show_1_2
        "... where to your surprise Ivy walks onto the stage."
        wt_image intro_wife_show_1_5
        "The two women greet each other ..."
        wt_image intro_wife_show_1_6
        "... as a pair of men step forward on either side of them."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image intro_wife_show_1_7
            "Each man takes a woman ..."
            wt_image intro_wife_show_1_8
            "... and kneels down beside them."
            if ivy.has_tag('likes_girls'):
              wt_image intro_wife_show_1_10
            else:
              wt_image intro_wife_show_1_9
            "Which is when the show really begins."
            wt_image intro_wife_show_1_11
            "Other than the costumes, there's nothing to distinguish the performance from your average lick ..."
            wt_image intro_wife_show_1_12
            "... suck ..."
            wt_image intro_wife_show_1_13
            "... and fuck show."
            if ivy.anal_count > 0:
              wt_image intro_wife_show_1_14
              "Although you are perversely proud to see that Ivy is willing to take a dick up her butt in public."
            wt_image intro_wife_show_1_15
            "The most important thing, though, is that the performers are all clearly enjoying themselves, which means the audience does, too."
            if ivy.has_tag('likes_girls'):
              wt_image intro_wife_show_1_17
            else:
              wt_image intro_wife_show_1_16
            "As evidenced by the huge round of applause at the end of the show.  The show complete, you head out to continue your day."
            change player energy by -energy_very_short notify
          "Leave":
            pass
      else:
        wt_image intro_wife_show_2_1
        "A man with red eyes and an impressively large cock sits stroking himself on a chair in the middle of the stage."
        summon ivy
        $ ivy.training_session()
        wt_image intro_wife_show_2_2
        "As she moves around to the front, you realize the woman with him is Ivy."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image intro_wife_show_2_3
            "At first she strikes a defiant pose, as he beckons to her ..."
            wt_image intro_wife_show_2_4
            "... but as he continues to call to her, she turns around ..."
            wt_image intro_wife_show_2_5
            "... and very clearly surrenders ..."
            wt_image intro_wife_show_2_6
            "... to the seemingly irresistable allure of his throbbing erection."
            wt_image intro_wife_show_2_7
            "Perhaps recognizing that the audience's view is obscured from this angle, the devil or demon or whoever the man is intended to be directs Ivy to shift to her right ..."
            wt_image intro_wife_show_2_8
            "... giving the audience a clear view ..."
            wt_image intro_wife_show_2_9
            "... as she sucks his cock with wanton abandon."
            wt_image intro_wife_show_2_10
            "There's regret in her eyes when he eventually pulls her head off his cock ..."
            wt_image intro_wife_show_2_11
            "... but her disappointment is short-lived, as he positions her on the chair ..."
            wt_image intro_wife_show_2_12
            "... and takes her from behind."
            if ivy.anal_count > 0:
              wt_image intro_wife_show_2_14
              "When he lifts her up and puts his cock in her ass, you chuckle."
              wt_image intro_wife_show_2_15
              "The devil may have made her do it, but not without your help."
            else:
              wt_image intro_wife_show_2_13
              "The devil's wand soon overcomes her, and you don't think it's an act."
            wt_image intro_wife_show_2_16
            "As Ivy pumps the devil's seed onto herself, she seems to swoon."
            wt_image intro_wife_show_2_17
            "The devil walks off as Ivy slumps like an empty husk of a well-fucked woman.  You're not sure if the moral of the story was meant to be a cautionary tale against succumbing to the charms of men with big dicks or simply 'don't fuck with the devil', but either way the audience seems to have loved the show.  As you leave, they're still clapping."
            change player energy by -energy_very_short notify
          "Leave":
            pass
      call character_location_return(ivy) from _call_character_location_return_734
      call club_ball_leave from _call_club_ball_leave_1
    else:
      summon gloria
      $ gloria.show_count += 1
      if gloria.show_count > 4:
        $ gloria.show_count = 1
      if gloria.show_count == 1:
        wt_image club_show_1_1
        "The Club is shut down for today except for a show taking place at the main stage. A large crowd has gathered. You see Gloria front and center on the stage. She looks like she's about to make an announcement."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image club_show_1_2
            "You find a seat and watch as Gloria kneels down, folding her hands in front of her as if in prayer."
            gloria.c "Ladies and gentlemen, we've always considered our Club to be a little piece of Heaven here on earth. Today, I invite you to sit back and enjoy as we offer you a closer glimpse..."
            wt_image club_show_1_3
            gloria.c "...of Heaven!!"
            "She's rather overdramatic, but the crowd loves it, breaking into spontaneous applause."
            wt_image club_show_1_4
            "A young woman enters the stage.  Like Gloria, she's dressed in an angel costume."
            wt_image club_show_1_5
            "The crowd cheers as she joins Gloria at the center of the stage..."
            wt_image club_show_1_6
            "...then cheers more loudly as the two angels greet each other."
            wt_image club_show_1_7
            "The angels' revelry is interrupted by the arrival of a devil.  His appearance is booed by some of the audience, and cheered by others."
            wt_image club_show_1_8
            "It's not clear whether the angels are saving him..."
            wt_image club_show_1_9
            "...or whether the devil is corrupting them..."
            wt_image club_show_1_10
            "...but it is clear that he is one lucky devil."
            wt_image club_show_1_11
            "The rest of the show consists of the devil fucking first one angel..."
            wt_image club_show_1_12
            "...then the other..."
            wt_image club_show_1_13
            "...before baptizing them both with his infernal seed. His climax is accompanied by the a rousing applause from the crowd. "
            "You're still not sure whether good or evil prevailed, but you join the crowd as they file out of the Club, all seemingly pleased with the Club's attempt at providing a higher quality of entertainment."
            change player energy by -energy_very_short notify
          "Leave":
            pass
      elif gloria.show_count == 2:
        wt_image club_show_2_1
        "The Club is shut down for today except for a show taking place at the main stage. You hadn't realized it was Halloween already, but the Club is decorated in cobwebs and the macabre."
        "On stage, Gloria is dressed in a scary nurse's costume.  She's just begun an announcement."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image club_show_2_2
            "You take a seat as Gloria completes her announcement."
            gloria.c "This year's Halloween fundraiser is a two part prize available to the highest bidder."
            gloria.c "Our resident mad scientist Igor has mixed up a special cocktail that will allow who ever drinks it to go and go and go ... sexually that is."
            gloria.c "Since us ladies don't need a special potion for that purpose, I'm expecting our male members to be most interested in bidding - especially male members interested in using an enhanced member on a variety of female members over the remainder of the day."
            "The crowd chuckles as Gloria continues."
            gloria.c "The potion only lasts for the day, but I'm sure you'll be able to make the most of it while it does."
            wt_image club_show_2_3
            gloria.c "As an added sweetener - which frankly you may need, because that potion looks awful - I'll be offering myself to the high bidder, as the first subject to try out his enhanced-for-the-day member."
            "A series of cheers and catcalls ring out from the crowd as they hear the second part of the prize."
            wt_image club_show_2_4
            "Any thoughts you had of bidding are soon dismissed as the bids reach 1000 and then 2000 and beyond.  You knew there were some heavy hitters amongst the Club members, but this confirms that some of them at least have money to burn."
            "The eventual winner is dressed as a hunchback.  He pantomimes up to the stage in character as Gloria congratulates him."
            gloria.c "A round of applause and thanks to our high bidder please!"
            wt_image club_show_2_5
            gloria.c "I'll just activate the potion for you."
            "The potion turns from green to blood red as Gloria mixes it."
            gloria.c "Whoa!  I guess it's supposed to do that."
            wt_image club_show_2_6
            "The winner bidder doesn't seem concerned.  He gulps the potion down in one swig."
            wt_image club_show_2_7
            gloria.c "Well ladies, the potion seems to be working."
            wt_image club_show_2_8
            gloria.c "Gloria's commentary ceases temporarily as she puts her mouth to work servicing the member..."
            wt_image club_show_2_9
            "...then it resumes again as she offers him her sex."
            gloria.c "Ladies, I can tell you his member is working perfectly!  oohhhh!"
            wt_image club_show_2_10
            "A few minutes later, he's pumping his seed onto Gloria's substantial assets."
            gloria.c "Oohhh!  That's strangely warm, but it feels good!"
            wt_image club_show_2_11
            gloria.c "Oh!  Ladies!  He's getting hard again already!!"
            wt_image club_show_2_12
            gloria.c "That concludes the formal part of our show, ladies and gentlemen.  Thanks for coming out to support our Club!"
            gloria.c "Ohh, his cum is still tingly on my skin!  Igor, what did you put in that potion?"
            "Many of the women members of the Club rush in unladylike haste to form a queue at the edge of the stage to sample Igor's work.  Whoever Igor is, you spot him chuckling through his rubber mask as he leaves the stage."
            $ title = "What do you want to do?"
            menu:
              "Check on Gloria":
                wt_image club_show_2_13
                player.c "Great show, Gloria. Congratulations on the successful fundraiser."
                gloria.c "Shut up and give me your cock!"
                "She nearly rips the balls off you pulling your cock out of your pants."
                wt_image club_show_2_14
                gloria.c "I don't know what he put in that potion! Some sort of aphrodisiac or sperm compulsion I've absorbed through my skin I think."
                gloria.c "It better wear off soon or I'm going to end up sucking every dick in this Club."
                "With that she stops talking and concentrates on sucking your cock like its the tastiest thing in the world. She savors your dick until you can hold back your orgasm no longer."
                "As you spurt your load in her mouth she swallows every drop like its a precious elixir, then abandons you in search of another hard cock."
                player.c "[player.orgasm_text]"
                "You find your way out of the Club before it gets too unruly with cock obsessed females tainted by the potion drinkers cum."
                "Whatever 'Igor' has done, its not likely to be anything other than a temporary, if elaborate, gag. There are too many powerful people associated with the Club for anyone to try messing with the membership on a permanent basis."
                $ gloria.blowjob_count += 1
                $ gloria.swallow_count += 1
                orgasm
              "Head out":
                "The show complete, you head out to continue your day."
            change player energy by -energy_very_short notify
          "Leave":
            pass
      elif gloria.show_count == 3:
        rem tags 'show_last_time' from ivy
        wt_image club_show_3_1
        "The Club is shut down for today except for a show taking place at the main stage. Gloria has taken center stage, in what looks like it may be a circus performer's, or possibly ringmaster's outfit."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image club_show_3_2
            "You miss Gloria's announcement while you're trying to find a seat. A bunch of women carrying hoops and balls run out on stage and start performing, so you assume today's show is meant to be some sort of circus theme."
            wt_image club_show_3_3
            "The next thing you know, the women are all naked and lying on their backs in a circle, their legs in the air. It's more than a bit baffling, so you whisper to the man sitting beside you,"
            player.c "What is this supposed to be?"
            club_patron_8 "Cirque de Pussy."
            player.c "Oh. That explains it."
            wt_image club_show_3_4
            "In synchronization, the women pull out vibrators one-by-one and start pleasuring themselves and each other."
            wt_image club_show_3_3
            "Then almost as quick as they appeared, the vibrators are put away and their legs are back in the air."
            wt_image club_show_3_5
            "From behind the curtains, a group of naked men appear. They put their cocks in the nearest empty pussy as the round sofa rotates the women in front of them."
            wt_image club_show_3_6
            "One quick thrust and then their cocks come out, ready for insertion in the next pussy to rotate in front of them."
            wt_image club_show_3_7
            "You don't hear the cue, but there must have been one, as suddenly the women all flip over and present themselves doggy style to the waiting cocks."
            wt_image club_show_3_8
            "The men for their part don't miss a beat, thrusting in and then out of each pussy in turn, regardless of whether the women are facing up or down."
            "The sounds of orgasms issuing from the stage are the signal that the formal part of the show has ended."
            wt_image club_show_3_9
            "You assume this is the end of the festivities, but Gloria pops her ringmaster's hat back on her head and makes an announcement."
            gloria.c "For a donation of 25 to the Club, members can have their cocks or pussies serviced by our Cirque de Pussy performers. Yes, I mean all of them ladies and gentlemen. Queue up in an orderly fashion please."
            $ gloria.sex_count += 1
            if player.money - player.min_money >= 25:
              $ title = "Do you want to line up?"
              menu:
                "Yes, enjoy the performers":
                  wt_image club_show_3_11
                  "You're fortunate to get close to the front of one of the lines. You make your donation to the Club and the performers all crowd around as the first one takes your dick in her mouth."
                  wt_image club_show_3_12
                  "After giving you a quick suck, the performer moves on to the cock or cunt at the front of the next line, and another performer takes her place."
                  wt_image club_show_3_13
                  "Even Gloria's taking part."
                  wt_image club_show_3_14
                  "The performers seem to be making a game out of who can trigger the most orgasms when it's their turn at the cock or pussy."
                  wt_image club_show_3_15
                  "That makes each of them super-focused on earning your cum for themselves.  You do your best to hold out until you've had all of the performers' mouths on your dick ..."
                  wt_image club_show_3_16
                  "... but when the last one reaches you, you can hold out no longer."
                  player.c "[player.orgasm_text]"
                  brooklyn.c "Mmmmm ... Thank you for choosing my mouth to cum in!"
                  if chelsea.lesbian_club_count > 0:
                    "You recognize that mouth. It belongs to the woman from the Swingers Room who was interested in [chelsea.name]. It looks cute with your sperm dripping out of it. There's nothing more for you to do at the Club today, so you head out."
                  else:
                    "As she smiles at you, some of your sperm drips out of the corner of her mouth. There's nothing more for you to do at the Club today, so you head out."
                  $ brooklyn.blowjob_count += 1
                  $ brooklyn.swallow_count += 1
                  change player money by -25
                  orgasm notify
                "Head out":
                  "You leave the other Club members to contribute to the Club's social fund.  There are enough of them to keep the performers busy."
                  change player energy by -energy_short
            else:
              "You don't have the funds, so you'll have to pass. You leave the other Club members to contribute to the Club's social fund. There are enough of them to keep the performers busy."
              change player energy by -energy_very_short
          "Leave":
            pass
      elif gloria.show_count == 4:
        wt_image club_show_4_1
        "The Club is shut down for today except for a show taking place at the main stage. Gloria is up on stage, dressed like a warrior queen."
        $ title = "Stay for the show?"
        menu:
          "Take a seat and watch":
            wt_image club_show_4_2
            "Gloria picks up the sword and brandishes it over her head."
            gloria.c "Ladies and gentlemen..."
            wt_image club_show_4_3
            gloria.c "...tonight we slay the dragon!"
            wt_image club_show_4_4
            "A man in a blue plush dragon suit runs onto stage and grabs Gloria by the tit."
            "Most of the crowd laughs, but part of the crowd - presumably those most into furries - get very excited. Or should that be 'scalies' when the animal is a dragon?"
            wt_image club_show_4_5
            "Furry or scaly, Warrior Princess Gloria seems to disarm him with a grip on his dick."
            wt_image club_show_4_7
            "The dragon regains control, however, with a well placed chomp on the tits that causes Gloria to call out."
            gloria.c "Oohhhhh!"
            wt_image club_show_4_8
            "Gloria throws herself at the beast, grabbing him in her mouth. For a moment he seems befuddled, and it looks like our Warrior Princess is going to win the day."
            wt_image club_show_4_6
            "Then the dragon counter-attacks with another fierce chomp on the tits that sends Gloria into a swoon."
            gloria.c "oooohhhhhhh!!"
            wt_image club_show_4_9
            "Seizing the advantage, the dragon grabs her by the hips and pulls the Warrior Princess to him. Desperately she reaches for her sword, but the sword the dragon has impaled her on is too powerful."
            gloria.c "ooohhhhhh   oooohhhhhh!!"
            wt_image club_show_4_10
            gloria.c "Ooohhhh!!!  Ooohhh   OH YESSSSS!!!"
            "The dragon gives a big thumbs up as the Warrior Princess surrenders her body to him."
            "Most of the crowd laughs, but the furry fetishists are desperately pulling their partners' hands or heads into their lap, eager for relief."
            "The show over and there's nothing more for you to do in the Club today, so you head out."
            change player energy by -energy_very_short notify
          "Leave":
            pass
      call club_ball_leave from _call_club_ball_leave_2
  return

# Club Ball Options
label club_ball_blonde_woman:
    wt_image club_ball_2_1
    "The blonde woman hasn't gone far."
    wt_image club_ball_2_2
    "She drops to her knees and smiles up at you as you approach."
    wt_image club_ball_2_3
    "It's a pretty clear invitation.  You take out your cock and she pounces on it.  At first you assume she's just warming you up before the attention turns to her, but the enthusiasm with which she sucks you soon makes it clear that this is the main event for her."
    wt_image club_ball_2_4
    "You lie back and let her work for the load of cum she's so eagerly striving for. You decide to make a game of it, holding back your orgasm as long as you can.  The longer it takes, the harder she works, bobbing her head up and down frantically as she tries to milk the sperm from your balls. Eventually she earns your orgasm."
    wt_image club_ball_2_5
    player.c "[player.orgasm_text]"
    "She pulls out your cock and directs your cum up and over her masked face.  Then she smiles up at you, clearly pleased with herself.  You're pretty happy with her too, but she disappears into the crowd before you can thank her."
    $ club_swingers.blowjob_count += 1
    $ club_swingers.facial_count += 1
    orgasm notify
    call club_ball_leave from _call_club_ball_leave_3
    return

label club_ball_dark_haired_woman:
    wt_image club_ball_3_2
    "As she sees you approach, she pulls off her corset ..."
    wt_image club_ball_3_3
    "... and steps through the curtain, looking back at you as she does."
    wt_image club_ball_3_4
    "The invitation to follow her is quite clear, as is the invitation she offers when you do."
    wt_image club_ball_3_5
    club_ball_woman.c "mmmmmm"
    "She purrs as you push your cock inside her ..."
    wt_image club_ball_3_6
    "... her purrs soon turning to yelps of pleasure as you pound into her."
    club_ball_woman.c "yes  yes  yes   ohhhh  mmmmm  yes"
    wt_image club_ball_3_7
    club_ball_woman.c "yes  yes  yes   ohhhh  mmmmm  oh god yes!!!"
    "You're surprised at how quickly she cums, but perhaps the act of offering herself to a stranger like this had her halfway to orgasm before you even penetrated her. Now its your turn."
    wt_image club_ball_3_6
    "You continue to pound into her until your balls feel like they're going to boil over ..."
    $ title = "Where do you want to cum?"
    menu:
        "Inside her":
            wt_image club_ball_3_11
            "... then you dump your seed deep inside her."
            player.c "[player.orgasm_text]"
            "She purrs again as she feels you cum inside her."
            club_ball_woman.c "mmmmmm"
            "You realize that you didn't ask her whether she was on birth control.  She doesn't seem upset at receiving your sperm, so either she is, or she's trying to get pregnant."
            "For just a moment you wonder if Gloria set up the masquerade to have a dual purpose - party and anonymous sperm donor bank.  That seems far fetched until the woman whispers to you."
            if player.has_tag('dominant'):
              club_ball_woman.c "I hope you're as smart as you are powerful."
            elif player.has_tag('supersexy'):
              club_ball_woman.c "I hope you're as smart as you are handsome."
            elif player.has_tag('hypnotist'):
              club_ball_woman.c "I hope you're as smart as you look."
            add tags 'impregnated' to club_ball_woman
        "On her":
            wt_image club_ball_3_8
            "... then you pull your cock out of her. She looks a little disappointed as she feels you pulling out of her..."
            wt_image club_ball_3_9
            "... but she spins around and offers you her face. You were just going to cum over her ass and back, but this is good too."
            player.c "[player.orgasm_text]"
            wt_image club_ball_3_10
            club_ball_woman.c "mmmmm"
            "She purrs again and smiles up at you as your jizz drips down her face and breasts."
            $ club_swingers.facial_count += 1
    wt_image club_ball_3_3
    "Without another word, she dresses and disappears, throwing you a quick look back as she goes."
    $ club_swingers.sex_count += 1
    orgasm notify
    call club_ball_leave from _call_club_ball_leave_4
    return

label club_ball_gloria:
    summon gloria
    if gloria.ball_outfit == 1:
        wt_image club_wife_ball_1_2
        "You spot Gloria sitting by herself. Another guest has spotted her, too."
        wt_image club_wife_ball_1_3
        "Before you can reach her, he has his hands under her dress, pulling it down and grabbing her breasts in both hands. She gasps in surprise, but makes no move to remove his hands."
        $ title = "What do you want to do?"
        menu:
            "Stay and watch":
                wt_image club_wife_ball_1_6
                "He shows no interest in sharing his capture, so you watch from a distance as he pushes Gloria to her knees."
                wt_image club_wife_ball_1_4
                "She seems happy to be there.  Her hand and mouth are soon wrapped around his cock ..."
                wt_image club_wife_ball_1_7
                "... and you assume she's about to get him off ..."
                wt_image club_wife_ball_1_5
                "... when he bends her over and takes her from behind. Her mask has fallen off, defeating the purpose of the anonymous sex event, but then anyone seeing her breasts swinging free would know who they belonged to, mask or no mask."
                "Everyone else at the ball seems to have teamed up with a partner or partners by now, so you leave them to their revelry and depart."
                change player energy by -energy_very_short notify
                call club_ball_leave from _call_club_ball_leave_5
            "Do something else":
                add tags 'club_ball_do_something_else' to gloria
                call expandable_menu(club_ball_main_menu) from _call_expandable_menu_122
    elif gloria.ball_outfit == 2:
        wt_image club_wife_ball_2_11
        "Gloria shakes her head when she sees you approach."
        gloria.c "No partying for me tonight. I need to make sure everyone else is having fun. Go find yourself a playmate from the crowd."
        if gloria.has_tag('trigger_implanted'):
            player.c "Gloria, you should know better than to try and say no to me. [gloria.trigger_phrase]."
            wt_image club_wife_ball_2_2
            gloria.c "Oh!  Yes, of course.  You're in charge."
            player.c "Now that we've established that, you said you wanted to make sure all the guests are having fun. I'm not having fun yet, Gloria."
            wt_image club_wife_ball_2_3
            gloria.c "What can I do to help?"
            $ title = "What can she do to amuse you?"
            menu:
                "Play with herself":
                    player.c "Get up on the table and play with yourself, Gloria."
                    wt_image club_wife_ball_2_4
                    "She hops up and hikes up her dress, then runs her fingers across her panties.  She's already excited, probably from the sexual tension of the masquerade, and starts moaning immediately."
                    gloria.c "ooohhhhh!"
                    wt_image club_wife_ball_2_5
                    player.c "Tits too, Gloria."
                    "She claws open the top of her dress, squeezing her breasts as she does so ..."
                    wt_image club_wife_ball_2_6
                    "... then resumes rubbing her pussy through her panties.  You're about to tell her to lose the panties when you realize she's already on the brink of orgasm."
                    gloria.c "Ooohhhhh!!   Ooooohhhhh!!!    OOHH!!!   Oh YEESSS!!!"
                    wt_image club_wife_ball_2_7
                    "Gloria's performance has attracted a crowd, and her climax is accompanied by a round of applause."
                    club_patron_11 "Well done!"
                    club_patron_6 "Great show."
                    club_patron_8 "That's the type of responsiveness I like to see in a slut whore."
                    club_patron_3 "Mmmm, I'd love to smell those panties now."
                    "It's not obvious to anyone that Gloria's under your triggered hypnotic control, but she might give that away if you're not careful. You whisper her release phrase and make your way out of the Club before you arouse any suspicion."
                    $ gloria.hypno_masturbation_count += 1
                    $ gloria.hypno_orgasm_count += 1
                    change player energy by -energy_very_short notify
                "Blow you":
                    player.c "I'll be having a much better time once you're pleasuring my cock."
                    wt_image club_wife_ball_2_8
                    gloria.c "Of course."
                    "She seems to assume this includes seeing her tits, as she pulls down the top of her dress ..."
                    wt_image club_wife_ball_2_9
                    "... then drops to her knees and takes out your cock. She pulls off her mask as she starts licking you. Perhaps it was in her way."
                    "Going unmasked defeats the purpose of the anonymous sex event, but then anyone seeing her breasts swinging free would know who they belonged to, mask or no mask, and you don't mind seeing the eyes of the entranced woman pleasuring your dick."
                    wt_image club_wife_ball_2_10
                    "To limit the chance of trouble, you let yourself cum quickly. She keeps her eyes on you and swallows each drop that you spurt down the back of her throat."
                    player.c "[player.orgasm_text]"
                    wt_image club_wife_ball_2_1
                    "Then you bring her out of her trance and send her off to her duties as hostess, as if nothing had happened."
                    gloria.c "How are you enjoying the masquerade? Find anyone interesting to hook up with?"
                    player.c "I certainly did."
                    $ gloria.hypno_blowjob_count += 1
                    $ gloria.hypno_swallow_count += 1
                    orgasm notify
            call club_ball_leave from _call_club_ball_leave_6
        else:
            add tags 'club_ball_do_something_else' to gloria
            call expandable_menu(club_ball_main_menu) from _call_expandable_menu_123
    elif gloria.ball_outfit == 3:
        wt_image club_wife_ball_3_2
        "You go on a hunt for Gloria.  You find her flirting with a masked man who's clearly her husband."
        wt_image club_wife_ball_3_3
        "Based on the location of his hand, they're about to get busy."
        $ title = "What do you want to do?"
        menu:
            "Stay and watch":
                wt_image club_wife_ball_3_4
                "You settle in to watch the show when something catches their attention and distracts them."
                wt_image club_wife_ball_3_5
                "It's a woman in a blue gown.  You can't tell what she's saying to them ..."
                wt_image club_wife_ball_3_6
                "... but the gist of their conversation is quite clear. The Club President shows off his wife's pussy while the woman in blue shows off her own."
                wt_image club_wife_ball_3_7
                "Gloria kneels down to take a closer look, and approves of what she finds."
                wt_image club_wife_ball_3_8
                "After that it's a suck fest ..."
                wt_image club_wife_ball_3_9
                "... and fuck fest ..."
                wt_image club_wife_ball_3_10
                "... with orgasms all around."
                "Everyone else at the ball seems to have teamed up with a partner or partners by now, so you leave them to their revelry and depart."
                change player energy by -energy_very_short notify
                call club_ball_leave from _call_club_ball_leave_7
            "Do something else":
                add tags 'club_ball_do_something_else' to gloria
                call expandable_menu(club_ball_main_menu) from _call_expandable_menu_124
    return

label club_ball_sam:
    wt_image barista_masquerade_1
    "You hunt for the woman in the red mask, and find her in the next room over."
    summon samantha
    wt_image barista_masquerade_12
    "It's Sam alright, and you're not the only one watching her."
    $ title = "What do you want to do?"
    menu:
        "Stay and watch":
            summon tracy no_follows
            wt_image barista_masquerade_13
            "Sam's new employers must have invited her to attend the Club ball, and she's using the opportunity to meet some Club members."
            wt_image barista_masquerade_14
            "This one seems to have caught Sam's attention ..."
            wt_image barista_masquerade_2
            "... and the interest is clearly mutual."
            wt_image barista_masquerade_3
            "The two women look around furtively, as if to make sure that no one is watching.  Either they don't see you, or they're not concerned about putting on a show for you."
            wt_image barista_masquerade_4
            "Sam takes charge, pinning the other woman underneath her and removing both their masks."
            wt_image barista_masquerade_5
            "That's not how sex at a masquerade ball is supposed to work, but the other woman seems in no mood to object to anything Sam chooses to do with her."
            wt_image barista_masquerade_6
            "Her bra soon follows her mask ..."
            wt_image barista_masquerade_7
            "... and her mouth follows Sam's hand to the blonde's waiting breast."
            wt_image barista_masquerade_15
            "Before long Sam has them both stripped ..."
            wt_image barista_masquerade_16
            "... as the brunette waits to find out what Sam intends to do with her."
            wt_image barista_masquerade_17
            "What Sam does isn't that surprising, but the speed with which she climaxes on the brunette's tongue is.  Either Sam was extra horny, or the brunette's an accomplished cunt licker."
            wt_image barista_masquerade_8
            "Either way, Sam seems pleased with the other woman and her tongue ..."
            wt_image barista_masquerade_9
            "... and prepares a suitable thank you."
            wt_image barista_masquerade_18
            "The brunette is soon close to her own climax ..."
            wt_image barista_masquerade_19
            "... but Sam's not finished with her own needs, yet."
            wt_image barista_masquerade_2
            "Eventually Sam relents and allows the other woman to finish what Sam started ..."
            wt_image barista_masquerade_10
            "... while Sam frigs herself to a second orgasm."
            wt_image barista_masquerade_20
            "As the orgasm subsides, a look of panic crosses the brunette's face."
            tracy.c "My husband!"
            wt_image barista_masquerade_11
            "Sam disappears as the other woman scrambles back into her clothes.  She finds everything except her mask."
            tracy.c "Hi honey!  Ready to go?"
            tracy.c "Did I meet anyone interesting?  No, no one interesting."
            tracy.c "My mask?  Ummm, maybe I left it in the ladies room?"
            "Everyone else at the ball seems to have teamed up with a partner or partners by now, so you leave them to their revelry and depart."
            $ tracy.opp = 1
            change player energy by -energy_very_short notify
            call club_ball_leave from _call_club_ball_leave_8
        "Do something else":
            add tags 'club_ball_do_something_else' to samantha
            call expandable_menu(club_ball_main_menu) from _call_expandable_menu_125
    return

label club_ball_rep_from_club_bj:
    wt_image rep_from_club_ball_1_2
    "You take your place in line and watch as the kneeling woman services first one cock ..."
    wt_image rep_from_club_ball_1_3
    "... then another."
    wt_image rep_from_club_ball_1_4
    "You aren't the only one watching her look after the Club members' ... members."
    wt_image rep_from_club_ball_1_5
    "A man you presume to be her partner seems to be finding her performance almost as enjoyable as the men at the front of the line."
    wt_image rep_from_club_ball_1_6
    "Eventually, it's your turn at the front of the line."
    wt_image rep_from_club_ball_1_7
    "If her jaw is getting sore from the continual blow jobs, she does a good job of hiding it.  She worships your cock with enthusiasm, as if it's the first one she's seen today."
    wt_image rep_from_club_ball_1_8
    "Still, she seems happy when you remove your cock from her mouth and let her finish you off by hand."
    player.c "[player.orgasm_text]"
    if player.has_tag('dominant'):
        wt_image rep_from_club_ball_1_9
        "Submissively, she gives your cock a gentle kiss before moving on to the next man in line.  It's hard to tell whether that's a 'thank you' for giving her jaw a short rest, or for the facial itself, or a simple show of obeisance. Or all three."
    elif player.has_tag('supersexy'):
        wt_image rep_from_club_ball_1_10
        rep_from_club.c "You are so hot!"
        "You're used to women throwing themselves at you, but usually they do that before they suck your cock, not after."
    else:
        wt_image rep_from_club_ball_1_11
        "Waiting in line seems to have resulted in you building up a big load.  Still, she gamely wipes herself off, then attends to the next man in queue."
    $ rep_from_club.blowjob_count += 1
    $ rep_from_club.facial_count += 1
    orgasm notify
    add tags 'gave_you_ball_bj' to rep_from_club
    call club_ball_leave from _call_club_ball_leave_9
    return

label club_ball_rep_from_club_bondage:
    wt_image rep_from_club_ball_2_2
    "He's finishing up her bonds as you arrive.  She rolls over to look at you."
    if player.has_tag('dominant'):
        rep_from_club.c "He's letting any man who wants, fuck me.  You don't have to be gentle.  In fact, I hope you won't be."
    elif player.has_tag('supersexy'):
        rep_from_club.c "He's letting any man who wants, fuck me.  I hope you want to."
    else:
        rep_from_club.c "He's letting any man who wants, fuck me."
    wt_image rep_from_club_ball_2_3
    husband_rep_from_club "Just one more tie, then she's ready.  You can go first, if you want, as a thank you for helping us.  Not her ass, though.  That's for me, alone."
    $ title = "What do you want?"
    menu:
        "Fuck her":
            wt_image rep_from_club_ball_2_4
            "You lift her bound legs and push yourself inside as her husband watches.  She's already wet, though it's not clear whether that's from you, from being tied up, or the anticipation of serving the lineup of men queuing up behind you."
            wt_image rep_from_club_ball_2_5
            if player.has_tag('dominant'):
                "She didn't want you to be gentle, so you aren't.  And the rougher you are, the more she moans, until she's suddenly climaxing around your cock."
                rep_from_club.c "Ohhh  ...  ohhh  ...  ohhhh FUCCKK!!"
                $ rep_from_club.orgasm_count += 1
            elif player.has_tag('supersexy'):
                "It's at least partially you, as her excitement builds quickly as you fuck her, and she's soon moaning and talking under her breath, either to you or maybe just to herself."
                rep_from_club.c "Oh, you are so hot!!  I'm so glad you wanted to fuck me.  Ohhh  ...  ohhh ... ohhhh FUCCKK!!"
                $ rep_from_club.orgasm_count += 1
            else:
                "She was already wet when you entered her, and she gets wetter still as you fuck her."
            wt_image rep_from_club_ball_2_6
            player.c "[player.orgasm_text]"
            wt_image rep_from_club_ball_2_7
            "She grins as you empty your load inside her.  From the look of the line up behind you, it's just the first of many she'll receive tonight."
            $ rep_from_club.sex_count += 1
            orgasm notify
            call club_ball_leave from _call_club_ball_leave_10
        "Have her ride you":
            wt_image rep_from_club_ball_2_8
            "Grasping her by the rope her husband so conveniently tied around her neck as a leash, you pull her up on top of you."
            wt_image rep_from_club_ball_2_9
            "She'll be exhausted soon, if the rest of the men lined up behind you want her to ride them, too, but for now she has plenty of energy to buck her hips up and down your cock and milk an orgasm from you."
            wt_image rep_from_club_ball_2_10
            player.c "[player.orgasm_text]"
            wt_image rep_from_club_ball_2_11
            "As she rolls off you, her husband directs the man behind you to take your place.  You leave her to her busy, and cock-filled, evening."
            $ rep_from_club.sex_count += 1
            orgasm notify
            call club_ball_leave from _call_club_ball_leave_11
        "Do something else":
            add tags 'club_ball_do_something_else' to rep_from_club
            call expandable_menu(club_ball_main_menu) from _call_expandable_menu_126
    return

label club_ball_crowd:
    add tags 'watched_club_pissing' to player
    wt_image club_ball_1_1
    "The drinks are flowing, as are the flirtations."
    wt_image club_ball_1_2
    "Two by two ... or sometimes in threes or fours ... the partygoers start to drift off to their own private parties, while those who remain become more and more forward in their flirtations."
    wt_image club_ball_1_3
    "Eventually someone starts sucking a cock in the middle of the Club ballroom."
    wt_image club_ball_1_4
    "Like a dam bursting, this seems like the cue for the rest of the partiers to start fucking their nearest neighbor."
    wt_image club_ball_1_5
    "Emboldened by the anonymity offered by his mask, one of the members takes a piss on the face of his partner."
    wt_image club_ball_1_6
    "Most of the crowd moves away from the smelly mess, but a few join in."
    wt_image club_ball_1_7
    "Soon this part of the floor is a debauched mess of people pissing themselves ..."
    wt_image club_ball_1_8
    "... and pissing on others."
    wt_image club_ball_1_9
    "Most of the members participating seem like hardened golden shower fetishists, but at least one woman is steered reluctantly in their direction by the man holding her by the hips as he fucks her from behind."
    club_patron_12 "No, don't push me over here.  Aaaaahhhhh ... he's pissing on me!!"
    "The other women laugh at her as she recoils from the urine spraying on her face. She's repulsed, but they find it amusing, and her partner seems to find it hot, as he unloads inside her while she tries to keep the piss out of her mouth."
    "You decide to get out of here before someone pees on you, too. Besides, someone's going to need to clean up the mess that's been made, and you don't want to be around when they conscript members for the clean up crew."
    change player energy by -energy_very_short notify
    call club_ball_leave from _call_club_ball_leave_12
    return

label club_ball_leave:
    "You have other things you want to do, so you leave the Club members alone to enjoy their masquerade."
    if hannah.has_tag('masquerade_ball_watched'):
        rem tags 'masquerade_ball_watched' from hannah
        add tags 'masquerade_ball_complete' to hannah
        wt_image principal_masquerade_1_3
        "On your way out, Hannah joins you."
        hannah.c "Thank for inviting me to this.  I was quite an experience, but I don't think I'll be coming back."
        player.c "Too hard finding a suitable partner?"
        wt_image principal_masquerade_1_7
        hannah.c "No!  The opposite.  I wanted to sleep with everyone.  I needed to control myself so I wouldn't get a reputation as a slut."
        player.c "There are worse reputation to have, and besides, no one knows who you are."
        hannah.c "Oh, please.  These masks don't hide anyone.  I recognized half-a-dozen people I know, including two school donors."
        wt_image principal_masquerade_1_1
        hannah.c "I don't dare come back, for fear I'll become known as the Principal who can't keep her hands off any guy with a mask who wants to fuck her without asking her name."
    rem tags 'club_ball_do_something_else' from gloria
    rem tags 'club_ball_do_something_else' from samantha
    rem tags 'club_ball_do_something_else' from rep_from_club
    rem tags 'rep_from_club_bj_possible' 'rep_from_club_bondage_possible' 'barista_ball_event_possible' from player
    call character_location_return(gloria) from _call_character_location_return_735
    call character_location_return(rep_from_club) from _call_character_location_return_736
    call character_location_return(samantha) from _call_character_location_return_737
    call character_location_return(tracy) from _call_character_location_return_738
    call character_location_return(hannah) from _call_character_location_return_739
    call forced_movement(downtown) from _call_forced_movement
    return

label club_ball_hannah:
    summon hannah
    wt_image principal_masquerade_1_2
    "You spot Hannah wandering through the Club, observing."
    wt_image principal_masquerade_1_3
    "She receives lots of expressions of interest, but none she seems willing to accept."
    wt_image principal_masquerade_1_4
    "She takes a seat and you think she's going to simply watch today, when a well-built man catches her eye."
    wt_image principal_masquerade_1_5
    "He notices her attention, and to her shock, immediately takes out his cock."
    club_patron_8 "Don't be shy, beautiful.  Do what comes natural."
    wt_image principal_masquerade_1_6
    "She does, and a few minutes later, so does he."
    club_patron_8 "Oh, that's it!  Swallow it all!!"
    "You leave her to enjoy herself while you look around some more."
    add tags 'masquerade_ball_watched' to hannah
    call expandable_menu(club_ball_main_menu) from _call_expandable_menu_127
    return

########### ROOMS ###########
# Examine Club
label tc_examine:
  "The private members only club is known simply as The Club."
  return

# Prevent Access to Club
label tc_no_access:
  ## Prevent Access If Not A Member
  if not 'club_access' in player.tags:
    "You need to be a member to access The Club."
    break_movement
  else:
    ## Prevent Access If Already Seen Club Show Today
    if player.has_tag('club_visited_today'):
      if day == 5 and gloria.has_tag('show_friday'):
        "The Club is closed to clean up after today's event.  Come back on Monday."
        break_movement
    else:
      $ club.access_count += 1
  return

# Enter The Club, Summon Characters to Club
label tc_enter:
    ## First Club Visit?
    if not player.has_tag('club_first_visit_complete'):
        add tags 'club_first_visit_complete' to player
        add tags 'first_club_visit' to gloria # this and the next command set her image to match the intro photo of her and her husband
        $ gloria.change_image('club_pres_wife_3')
        # Intro from Club President
        wt_image club_pres_1
        club_president.c "Hello.  Welcome to the Club.  I'm the Club President, and this is my wife, Gloria."
        gloria.c "Pleased to meet you."
        club_president.c "I hope you'll consider the Club your home away from home. Every part of the Club is open to our members, except the Swingers Room, which you need a partner to enter."
        club_president.c "We have some well stocked private rooms, should you and another Club member want to make use of them."
        club_president.c "Just remember that anything that happens in the Club stays in the Club. We take the privacy of our members very seriously. If you meet someone here that you see anywhere else, forget you saw them here."
        club_president.c "That's about the extent of our rules. Have fun!"
        # Gloria is always in Club on your first visit
        $ gloria.location = club
        add tags 'in_club_now' to gloria
        # Cassandra is always in Club on your first visit, nobody else
        $ cassandra.location = club
        add tags 'gloria_club_talk_possible' 'in_club_now' to cassandra
        wt_image current_location.image
    ## Club Show Today?
    elif day == 5 and gloria.has_tag('show_friday'):
        call club_show_today from _call_club_show_today
    else:
        ## First check to see if the Club President has anything to say
        if club_president.discussion_pending > 0 and week > club_president.discussion_week:
            call club_president_discussion_pending from _call_club_president_discussion_pending
        elif player.showgirl_count > club_president.showgirl_reward_count or club_president.rewards_pending > 0:
            call club_president_reward_discussion from _call_club_president_reward_discussion
        ## Summon Characters To Club: call the person.club_call label for everyone you can meet at the Club ('can_be_in_club' tag) to check to see if they should be in the club now
        call for_call_labels(label_list = [p.short_name + '_club_call' for p in get_people(tagged_with_all=['can_be_in_club'])]) from _call_for_call_labels_11
        wt_image current_location.image
    ## must add the visited tag last so other summons work correctly
    add tags 'club_visited_today' to player
    return

# Exit The Club
label tc_exit:
    if not player.in_area('club'):
        call club_character_returns_and_dismissals from _call_club_character_returns_and_dismissals_1
    return

# Examine Swingers Room
label sr_examine:
    "The Swingers Room is like its own separate club within a club. As your eyes adjust to the dim light, you see a broad cross section of humanity intertwined in various states of dress and undress."
    return

# Prevent Access to Swingers Room
label sr_no_access:
    # check the label for everyone who could come to the swingers room with you
    call for_call_labels(label_list = [p.short_name + '_swingers_room_call' for p in get_people(tagged_with_all=['swingers_room_possible'])]) from _call_for_call_labels_15
    if any_person(tagged_with_any = ['in_swingers_room_now']):
        if player.sr_visit_count == 0:
            "The Swingers Room is only accessible by couples."
            if lauren.cheated == 2:
                $ title = "Ask a girlfriend to join you (or blackmail Lauren to pose as your girlfriend)?"
            else:
                $ title = "Ask a girlfriend to join you?"
            menu:
                "Yes":
                    wt_image swingers_room.image
                    "The Swingers Room is like its own separate club within a club. As your eyes adjust to the dim light, you see a broad cross section of humanity intertwined in various states of dress and undress."
                    $ player.sr_visit_count += 1
                "No":
                    break_movement
        else:
            $ player.sr_visit_count += 1
            wt_image swingers_room.image
            "The Swingers Room is like its own separate club within the club. As your eyes adjust to the dim light, you see a broad cross section of humanity intertwined in various states of dress and undress."
    else:
        "You need the right sort of partner to be allowed in the Swingers Room.  If you had a girlfriend who wasn't otherwise busy, the two of you would be welcome."
        break_movement
    return

# Enter Swingers Room
label sr_enter:
    return

# Exit Swingers Room
label sr_exit:
    return

# Examine Stage
label st_examine:
    "A large dance stage dominates the north end of The Club's main room."
    return

# Prevent Access to Stage
label st_no_access:
    return

# Enter Stage
label st_enter:
    ## this has been replaced by new system
    ## Summon Showgirls
    #call stage_showgirls_summons # handled when first entered club
    #call jasmine_stage_events
    #call lauren_stage_events
    #if rae.has_tag('waiting_for_club'):
        #"This is the perfect place for Rae to dance. You'll send her here as soon as you get home."
        #rem tags 'waiting_for_club' from rae
        #call convert(rae,'showgirl') # rest of conversion process has already been run
    #if nicole.has_tag('waiting_for_club'):
        #call nicole_activate_dancing

    ## new system
    ## Summon Showgirls To Stage call the person.stage_call label for all current showgirls to check to see if they should be on stage and trigger stage events on entrance
    call for_call_labels(label_list = [p.short_name + '_stage_call' for p in get_people(tagged_with_all=['showgirl'])]) from _call_for_call_labels_16
    ## Summon Notices for people waiting for Club access to become Showgirls
    # note: notice labels must run after stage call labels for proper sequencing
    call for_call_labels(label_list = [p.short_name + '_stage_notice' for p in get_people(tagged_with_all=['waiting_for_club_access'])]) from _call_for_call_labels_17
    ## must add the visited tag last so other summons work correctly
    add tags 'stage_visited_today' to player
    return

# Exit Stage
label st_exit:
    return

# Exit The Club, Return Characters to OG Locations
label club_character_returns_and_dismissals:
    ## Return Current Club Occupants call the person.club_return label for everyone currently in the Club or at the Stage
    call for_call_labels(label_list = [p.short_name + '_club_send_home' for p in get_people(tagged_with_all=['in_club_now'])]) from _call_for_call_labels_12
    call for_call_labels(label_list = [p.short_name + '_stage_send_home' for p in get_people(tagged_with_all=['on_stage_now'])]) from _call_for_call_labels_13
    call for_call_labels(label_list = [p.short_name + '_swingers_room_send_home' for p in get_people(tagged_with_all=['in_swingers_room_now'])]) from _call_for_call_labels_14
    return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
