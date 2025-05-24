## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou & Subli & Wifetrainer

# Package  Register
# register_package lauren name "Lauren, The Cheater" description "Allows Lauren to be client." dependencies core
register sophie_pregame 10 in core as 'Sophie the Receptionist'

label sophie_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', 'Sophie the Receptionist (Capri Cavanni)')]

    ## Character Definition
    sophie = Person(Character("Receptionist", who_color="#424284", what_color="#424284", window_background = gui.dialogue_background_dark_font_color), "sophie", cut_portrait = True, prefix = "", suffix = "")

    # Other Characters
    # Blue
    sophie_whore_client_1 = Character("Mike", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 0,0,160
    sophie_whore_client_2 = Character("John", who_color="#0000A0", what_color="#0000A0", window_background = gui.dialogue_background_medium_font_color)
    # 0,64,128
    sophie_whore_client_3 = Character("Sophie's Whore Client #3", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    # Sophie Actions
    sophie.action_talk = sophie.add_action("Talk to her", label = '_talk', condition = "sophie.location == lauren_office and not sophie.has_tag('first_visit') and sophie.relationship_status == 2 and not sophie.has_tag('spoke_to_her_today')")
    sophie.action_ask_name = sophie.add_action("Ask her name", label = '_ask_name', condition = "sophie.location == lauren_office and not sophie.has_tag('first_visit') and sophie.relationship_status == 0")
    sophie.action_ask_lauren = sophie.add_action("Ask for Lauren", label = '_ask_lauren', condition = "sophie.location == lauren_office and sophie.relationship_status < 2 and not sophie.has_tag('spoke_to_her_today')")
    sophie.action_wait = sophie.add_action("Wait for Lauren", label = '_wait', condition = "sophie.location == lauren_office and sophie.has_tag('spoke_to_her_today')")
    sophie.action_contact = living_room.add_action("Contact Sophie", label = sophie.short_name + '_contact', context = "_contact_other", condition = "sophie.can_be_interacted and (sophie.relationship_status == 3 or sophie.relationship_status == 5)")
    sophie.action_contact_help = living_room.add_action("Help Sophie", label = sophie.short_name + '_contact_help', context = "_contact_other", condition = "sophie.can_be_interacted and sophie.relationship_status == 7")
    sophie.action_contact_pimp = living_room.add_action("Pimp Sophie out", label = sophie.short_name + '_contact_pimp', context = "_contact_other", condition = "sophie.can_be_interacted and sophie.relationship_status == 8 and sophie.whore_count <= 1")
    #sophie.action_ = sophie.add_action("", label = '_', condition = "sophie.can_be_interacted and sophie.")

    ## Tags
    # Common Character Tags
    sophie.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    ## Locations
    sophie.location = lauren_office

    ## Other
    sophie.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('sophie_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    sophie.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_swallow_count')

    # Character Specific Variables
    sophie.add_stats_with_value('fin_dom_amount', 'fin_dom_outfit', 'fire_week', 'kneel_count', 'relationship_status', 'spank_count', 'thank_you_week', 'whore_count', 'whore_lost_countdown')
    # note: relationship_status code: 0: no relationship; 1: rejected; 2: got name; 3: got phone number but not called; 4: dated; 5: called but no date; 6: not helped, left town; 7: fired and not yet resolved; 8: whore; 9: thanked still in town; 10: financially dominating you, 11: helped her left town
    sophie.your_fin_dom_name = "Pay Pig"
  return

# Display Portrait
label sophie_update_media:
    if sophie.has_tag('whore'):
        $ sophie.change_image('recept_whore_portrait')
    elif current_location == lauren_office:
        $ sophie.change_image('recept_desk_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label sophie_examine:
    if sophie.has_tag('whore'):
        "She used to be Sophie the Receptionist, before you helped her find a more lucrative profession, one for which she's ideally suited."
        "Now she's better known as 'Madison', and when she's not working, she can often be found treating herself to a shopping trip or a meal out at the city's finest restaurants. "
    elif current_location == lauren_office:
        "A pretty young woman sits at the reception desk."
    return

# Talk to Character
label sophie_talk:
    wt_image recept_desk_1
    "Sophie is on the phone when you enter the office."
    wt_image recept_desk_6
    "She smiles when she sees you and indicates that she'll just be a minute.  She rolls her chair back as she motions for you to have a seat."
    if sophie.has_tag('charmed'):
        wt_image recept_desk_12
        "She turns to look at you as she hangs up the phone."
        player.c "Hello, Sophie."
        sophie.c "Hi.  I'm glad to see you."
        player.c "I'm glad to see you, too."
        sophie.c "I have a confession to make."
        "You lean in close to her."
        player.c "A confession?  That sounds exciting.  Do tell."
        "She laughs."
        sophie.c "Not that exciting.  It's just ... I lied to you last time.  I don't really have a boyfriend."
        player.c "Not from a lack of offers, I don't imagine.  So I suppose 'pretend boyfriend' is a good way to keep unwanted attention away?"
        sophie.c "I guess.  Yes."
        $ sophie.relationship_status = 3
    elif sophie.has_tag('chastised'):
        wt_image recept_desk_5
        "She turns to look at you as she hangs up the phone."
        player.c "Hello, Sophie."
        sophie.c "Hello"
        "She hesitates, and her head lowers slightly before continuing."
        sophie.c "I have a confession to make."
        player.c "Oh?"
        sophie.c "I lied to you last time.  I don't really have a boyfriend."
        player.c "So not only were you rude to me, you also lied."
        sophie.c "I guess.  Yes."
        player.c "I presume you lie frequently about having a boyfriend, to keep unwanted attention away?"
        sophie.c "Yes"
        player.c "No more lying to me, Sophie."
        "She nods."
        $ sophie.relationship_status = 3
    call sophie_wait from _call_sophie_wait
    return

# First visit ask for Lauren
label sophie_ask_lauren:
    wt_image recept_desk_1
    player.c "Is Lauren in?"
    sophie.c "She's just finishing up a meeting.  Was she expecting you?"
    player.c "No, but she'll see me."
    sophie.c "Have a seat.  I'll let you know when she's available."
    add tags 'spoke_to_her_today' to sophie
    rem tags 'first_visit' from sophie
    return

# Ask Her Name
label sophie_ask_name:
    $ sophie.relationship_status = 1
    player.c "What's your name?"
    wt_image recept_desk_2
    "The receptionist sneers at you before answering curtly."
    sophie.c "I have a boyfriend."
    "So much for small talk."
    if player.has_tag('hypnotist'):
        "You might try changing her relationship status if you were alone with her, but this is a busy office, with people moving through and by the reception area regularly.  There's no opportunity to hypnotize her.  You'll just need to wait for Lauren."
    if player.has_tag('supersexy') or player.has_tag('dominant'):
        $ title = "What do you do?"
        menu:
            "Charm her" if player.has_tag('supersexy'):
                "You smile at her.  Your good smile.  The one women lose themselves in."
                player.c "I hope he knows how lucky he is to have you as his girlfriend."
                "She hesitates a moment before responding."
                sophie.c "That's a corny line."
                "Your smile gets even broader, a hint of a laugh at the edge of your mouth and a twinkle in your eye as you lean in slightly."
                player.c "You're right.  It is a corny line, but it's also very sincere ... uh, I'm sorry.  I still don't know your name."
                wt_image recept_desk_12
                sophie.c "Sophie.  My name is Sophie."
                player.c "Sophie, I hope your boyfriend appreciates having a girlfriend like you."
                "Sophie tilts her head slightly and looks like she's about to say something, when a call comes in through the switchboard."
                $ sophie.relationship_status = 2
                $ sophie.change_full_name("", "Sophie", "the Receptionist")
                add tags 'charmed' to sophie
                call sophie_wait from _call_sophie_wait_1
            "Chastise her" if player.has_tag('dominant'):
                "You fix a look at her.  Your good look.  The one even non-submissive women get a shiver from.  When you speak, your voice is very quiet, but very stern."
                player.c "I hope you're never as rude to him as you just were to me.  Let's try that again, civilly this time.  What is your name?"
                wt_image recept_desk_5
                "She hesitates a moment.  Then her head lowers slightly and she answers, quietly."
                sophie.c "Sophie.  My name is Sophie."
                player.c "It's nice to meet you, Sophie.  If you're ever rude to me like that again, I'll take you over my knee and spank you."
                "Sophie looks like she's about to say something, when a call comes in through the switchboard."
                $ sophie.relationship_status = 2
                $ sophie.change_full_name("", "Sophie", "the Receptionist")
                add tags 'chastised' to sophie
                call sophie_wait from _call_sophie_wait_2
            "Wait for Lauren":
                call sophie_wait from _call_sophie_wait_3
    else:
        call sophie_wait from _call_sophie_wait_4
    return

# Wait for Lauren
label sophie_wait:
    wt_image recept_desk_1
    "You wait as the receptionist handles a series of incoming calls."
    "Eventually, the intercom buzzes and she stands up."
    wt_image recept_desk_3
    sophie.c "Lauren will see you now.  Follow me, please."
    wt_image cheater_office_door
    "The receptionist leads you to Lauren's office."
    if sophie.relationship_status == 3:
        wt_image recept_desk_13
        "As she turns to leave, she places a slip of paper in your hand.  It's her phone number."
        wt_image cheater_office_door
        "Before you can say anything, Sophie's gone, leaving you outside Lauren's office."
    call lauren_in_office from _call_lauren_in_office
    return

# Lauren upset you did not Call
# note: this is triggered by the entering Lauren's Office script in lauren.rpy
label sophie_upset_no_call:
    wt_image recept_desk_1
    "Sophie spots you as you enter."
    wt_image recept_desk_8
    "She gives you the cold shoulder as she stands up and goes to the side desk. She makes a bit of a spectacle of herself as she gathers some paperwork and takes a peek over her shoulder, as if to see if you've noticed."
    player.c "Is something wrong, Sophie?"
    sophie.c "No"
    "The tone of her voice makes it clear something is wrong."
    wt_image recept_desk_5
    sophie.c "I just thought you might call, is all."
    $ title = "What do you tell her?"
    menu:
        "I've been busy, but I will call":
            player.c "I've been very busy lately, Sophie.  I will call you.  Things have just been very hectic."
            "She brightens."
            wt_image recept_desk_12
            sophie.c "Of course.  I'm being silly.  Lauren's free now.  I'll take you to her."
        "I'm not available":
            player.c "I'm not available for dating, Sophie.  I'm sorry if I gave you that impression."
            sophie.c "Oh.  Of course.  My mistake."
            wt_image recept_desk_3
            sophie.c "Lauren's available now.  I'll take you to her."
            $ sophie.relationship_status = 1
        "I don't date receptionists":
            player.c "I don't date receptionists, Sophie.  I'm not sure what gave you the impression that I would."
            wt_image recept_desk_2
            sophie.c "I see.  My mistake then.  How stupid of me."
            sophie.c "Lauren's available now.  I'll take you to her.  I assume that's something you're okay with from a lowly receptionist."
            $ sophie.relationship_status = 1
    call lauren_in_office from _call_lauren_in_office_1
    return

# Lauren greeting you at office after date
# note: this is triggered by the entering Lauren's Office script in lauren.rpy
label sophie_post_date_office_events:
    wt_image recept_desk_6
    "Sophie smiles as she sees you come in."
    if sophie.has_tag('orgasm_from_sex'):
        wt_image recept_desk_12
        sophie.c "Can I show you something really quick?"
        wt_image recept_desk_14
        sophie.c "My nipples get hard every time I think about our date."
        sophie.c "I don't think I'm the sort to ever want to settle down with a guy, but if I did, it would have to be with someone who can fuck like you."
        wt_image recept_desk_12
        sophie.c "Come on, I'll take you to Lauren."
    elif sophie.has_tag('worshipped_her'):
        wt_image recept_desk_2
        sophie.c "I suppose you want to see Lauren again?"
        wt_image recept_desk_8
        sophie.c "I think there's something you need to do first, don't you?"
        wt_image recept_desk_22
        sophie.c "Make it quick.  Someone could walk by any moment and you don't want to have to explain why you're on your knees kissing my ass."
        wt_image recept_desk_12
        sophie.c "Okay.  You've earned a pass."
    elif sophie.spank_count == 1 and not sophie.has_tag('came_on_her_face'):
        $ sophie.kneel_count += 1
        if sophie.kneel_count == 1:
            wt_image recept_desk_12
            sophie.c "I've been reading about guys like you."
            player.c "Guys like me?"
            sophie.c "You know.  Men who like to spank women.  Do you have a moment?"
            "You nod."
            wt_image recept_desk_3
            sophie.c "We have to be quick.  I can't leave the front desk very long."
            "She leads you to an empty office ..."
            wt_image recept_desk_15
            "... where she quickly pulls off her clothes ..."
            wt_image recept_desk_18
            "... and kneels on the floor."
            wt_image recept_desk_11
            sophie.c "I thought you might like to see me like this.  Kneeling for you, I mean."
            player.c "Sophie, are you developing a submissive streak?"
            "She laughs."
            sophie.c "I just wanted to thank you a little more for the date.  Letting you spank me didn't seem like enough, when I thought about it some more."
            player.c "There are other things men like me enjoy, things you could do down there that would ensure I feel thoroughly thanked."
            "She laughs again."
            wt_image recept_desk_15
            sophie.c "It wasn't that expensive a date.  Besides, I need to dress and get back to the desk.  I'll take you to Lauren on the way."
        else:
            wt_image recept_desk_12
            sophie.c "I don't have a lot of time, but I could kneel for you again, if you want?"
            $ title = "What do you want?"
            menu:
                "See how far you can take her while she's kneeling":
                    wt_image recept_desk_3
                    "Sophie leads you back to the spare office ..."
                    wt_image recept_desk_15
                    "...where she strips ..."
                    wt_image recept_desk_18
                    "... and kneels in front of you."
                    wt_image recept_desk_11
                    player.c "Spread your knees."
                    wt_image recept_desk_16
                    sophie.c "Does this make me look even more submissive?"
                    player.c "No talking until I give you permission."
                    $ title = "What now?"
                    menu:
                        "Enjoy the view":
                            "You can't keep her here for long, but you thoroughly enjoy examining here while she's here."
                            player.c "Okay, Sophie.  You can go now."
                            wt_image recept_desk_11
                            sophie.c "I guess I can see why some women would find that hot.  Weird, but hot."
                            player.c "You are becoming submissive."
                            wt_image recept_desk_15
                            sophie.c "I don't think so.  It's just I know it's getting you excited, and that's kind of fun.  We'd better get moving."
                        "Jerk off on her":
                            "As you remove your cock, Sophie reacts."
                            sophie.c "Hey!  I told you it wasn't that expensive a date."
                            player.c "And I said no talking until I gave you permission.  You don't need to do anything.  Just kneel there."
                            wt_image recept_facial_1
                            sophie.c "This isn't fair.  You haven't done enough to earn this."
                            player.c "Consider it a lesson in submission and understanding dominant men.  Look at me and open your mouth while I cum on you."
                            wt_image recept_facial_2
                            player.c "[player.orgasm_text]"
                            wt_image recept_facial_3
                            sophie.c "Aren't you supposed to get a sub's permission before doing something like that?"
                            player.c "Sometimes pushing boundaries isn't about getting a 'yes', it's about finding out what she won't say 'no' to.  D/s relationships can be complicated."
                            sophie.c "I wasn't trying to start a D/s relationship by kneeling for you.  And that was worth way more to you than our date cost."
                            "Sophie cleans herself up and gets dressed.  She's upset with you, but less in a 'you just came on my face without permission way' than a 'you ripped me off way'."
                            add tags 'came_on_her_face' to sophie
                "Have her display her breasts":
                    wt_image recept_desk_3
                    "Sophie leads you back to the spare office."
                    wt_image recept_desk_12
                    player.c "No need to kneel today, Sophie.  I don't have time for that, but I do want you to bare your breasts and hold them out for me to examine."
                    wt_image recept_desk_14
                    sophie.c "I guess this is a form of submission, too, isn't it?"
                    player.c "No talking while I'm examining your body.  I'll tell you when you have permission to speak."
                    "You can't keep her here for long, but you thoroughly enjoy examining here while she's here."
                    player.c "Okay, Sophie.  You can go now."
                    wt_image recept_desk_5
                    sophie.c "I guess I can see why some women would find that hot.  Weird, but hot."
                    player.c "You are becoming submissive."
                    wt_image recept_desk_12
                    sophie.c "I don't think so.  It's just I know it's getting you excited, and that's kind of fun.  We'd better get moving."
                "Spank her again (ends kneeling content)":
                    wt_image recept_desk_3
                    "Sophie leads you back to the spare office ..."
                    wt_image recept_desk_15
                    "...where she strips."
                    player.c "No need to kneel today, Sophie.  Just turn around.  I'm going to spank you again."
                    sophie.c "Hey!  We already did that."
                    wt_image recept_desk_19
                    player.c "Relax.  I don't have time to give you a proper spanking.  Just a couple of quick swats.  Turn around."
                    wt_image recept_desk_20
                    sophie.c "I don't know.  It was only one date.  Why should you get two spankings out of it?"
                    player.c "For starters, because your wimpy virgin ass couldn't take a proper spanking the first time.  And because we only have time now to give you a couple of quick swats.  Bend over."
                    wt_image recept_desk_21
                    "*smack* ... *smack* ... *smack*"
                    sophie.c "Ow!  That stings."
                    player.c "Sadly, it only stings.  We don't have time for me to give you a spanking you'd feel for the rest of today."
                    wt_image recept_desk_15
                    sophie.c "You haven't really earned that, anyway.  I think I'm finished giving you kneeling freebies.  Come on, I'll take you to Lauren."
                    $ sophie.spank_count += 1
                "Nothing today":
                    player.c "It's sweet of you to ask, but I'm okay for today."
                    sophie.c "Okay.  Lauren's free.  I'll take you to her."
    wt_image cheater_office_door
    "Sophie leads you to Lauren's office, where she leaves you alone with her boss."
    call lauren_in_office from _call_lauren_in_office_2
    return

########### OBJECTS ###########
## Common Objects
# Contact
label sophie_contact:
  # rem no hypnosis tag to allow subsequent tests to work; it will get added back when you return to Lauren's office
  rem tags 'no_hypnosis' from sophie
  wt_image recept_desk_1
  sophie.c "Oh hi! I was wondering if you would call."
  $ sophie.contact_quiet_night = False
  $ title = "What do you suggest?"
  menu menu_sophie_contact_1:
    "Fake night out (Hypnotize her)" if player.can_hypno(sophie):
      $ sophie.training_session()
      wt_image recept_desk_6
      player.c "How about a nice restaurant and then we take in a show?"
      sophie.c "That sounds like fun. Tonight?"
      player.c "Why not."
      if sophie.has_tag('chastised'):
        $ title = "What do you want from her?"
        menu:
          "Spank her after the date":
              player.c "The offer comes with a condition, however."
              sophie.c "Oh?"
              player.c "You recall I told you if you were rude to me again, I'd spank you."
              sophie.c "Yes"
              player.c "That was before I knew you hadn't just been rude.  You also lied to me, about having a boyfriend.  Lying is worse than being rude, don't you agree?"
              sophie.c "I guess."
              player.c "After our date, I'm going to spank you, Sophie.  Is that understood?"
              wt_image recept_desk_1
              "She pauses just a moment before replying."
              sophie.c "If that's what you want.  Okay."
              add tags 'will_spank_her' to sophie
          "Make it a normal date":
              rem tags 'will_spank_her' from sophie
      "Standing Sophie up wouldn't be good.  You rest for the remainder of the day, to make sure you have enough energy for your date."
      summon sophie
      wt_image recept_date_23
      "Sophie arrives dressed to the nines.  She had her hair done, and whether or not that dress is new, it's expensive.  She's happy to show both of them off, but only for a minute."
      wt_image recept_date_1
      sophie.c "Let's go!  We don't want to be late for our reservation."
      player.c "Just look at this for me before we go."
      wt_image recept_date_25
      sophie.c "I don't want to be late. I'm really looking forward to this show. None of the girls at the office have been able to get tickets."
      player.c "This won't take long, Sophie.  Just look at this for me."
      call focus_image from _call_focus_image_40
      player.c "Look and listen.  Listen to me, Sophie.  Only to me.  Only to the sound of my voice, Sophie.  I am going to talk and you are going to listen, Sophie."
      wt_image recept_date_26
      "You soon have her under your trance."
      player.c "You want to be comfortable while we talk, Sophie.  You want to be comfortable and you want me to be comfortable.  Lower your dress so we can both be comfortable, Sophie."
      wt_image recept_date_29
      if not player.has_tag('first_hypno_breasts_message'):
        add tags 'first_hypno_breasts_message' to player
        "[player.first_hypno_breasts_message_text]"
      player.c "You and I are going on the most amazing date, Sophie.  We're going to the best restaurant in the city, then we're going to the most expensive show in the city."
      player.c "You're so happy to be going on this date.  You're so thankful to be going on this date.  You want me to know how thankful you are.  You want to show me how thankful you are."
      wt_image recept_date_27
      player.c "Show me how thankful you are, Sophie.  Show me everything."
      wt_image recept_date_15
      "She lets the dress slip the rest of the way off of her."
      wt_image recept_date_30
      player.c "You're so thankful for the wonderful, expensive date I'm taking you on, that you don't want anything to get in the way of showing me how thankful you are."
      wt_image recept_date_28
      player.c "You are so grateful for the date, Sophie.  Show me how grateful you are."
      wt_image recept_date_31
      "Her panties follow her dress to the floor."
      wt_image recept_date_32
      player.c "That's good, Sophie. Now that I can see how much you're looking forward to this, we can go on our date.  Pose pretty for me during our date, Sophie."
      wt_image recept_date_33
      "You've read enough reviews of both the restaurant and the show to make the suggestion that the two of you are actually there plausible."
      "Even at that, this would never work if Sophie wasn't so eager for the opportunity to go on this expensive outing.  An eagerness highlighted by both her physical and mental openness to you."
      wt_image recept_date_14
      "When a suitable time has passed and you've convinced her she's finished both her dinner and the following show, you have her dress then bring her out of the trance."
      call sophie_date from _call_sophie_date
      # the following command keeps track of how often you've hypnotized the person and subtracts the required energy
      $ sophie.hypno_session()
      $ sophie.relationship_status = 4
      $ sophie.fire_week = week + 3
      call character_location_return(sophie) from _call_character_location_return_741
      notify
      end_day
    "Expensive night out (cost 100)":
      # note money tests should be written in the following format
      if player.money - player.min_money >= 100:
        $ sophie.training_session()
        wt_image recept_desk_6
        player.c "How about a nice restaurant and then we take in a show?"
        sophie.c "That sounds like fun. Tonight?"
        player.c "Why not."
        if sophie.has_tag('chastised'):
          $ title = "What do you want from her?"
          menu:
            "Spank her after the date":
              player.c "The offer comes with a condition, however."
              sophie.c "Oh?"
              player.c "You recall I told you if you were rude to me again, I'd spank you."
              sophie.c "Yes"
              player.c "That was before I knew you hadn't just been rude.  You also lied to me, about having a boyfriend.  Lying is worse than being rude, don't you agree?"
              sophie.c "I guess."
              player.c "After our date, I'm going to spank you, Sophie.  Is that understood?"
              wt_image recept_desk_1
              "She pauses just a moment before replying."
              sophie.c "If that's what you want.  Okay."
              add tags 'will_spank_her' to sophie
            "Make it a normal date":
              rem tags 'will_spank_her' from sophie
        "Standing Sophie up wouldn't be good.  You rest for the remainder of the day, to make sure you have enough energy for your date."
        summon sophie
        wt_image recept_date_23
        "Sophie arrives dressed to the nines.  She had her hair done, and whether or not that dress is new, it's expensive.  She's happy to show both of them off, but only for a minute."
        wt_image recept_date_1
        sophie.c "Let's go!  We don't want to be late for our reservation."
        call forced_movement(outdoors) from _call_forced_movement_1000
        summon sophie
        wt_image recept_date_2
        "You take Sophie to one of the most popular restaurants in the city.  The food is great, but there's no time for dessert as you need to get to the show."
        wt_image recept_date_3
        "The theater is fully booked, but you were able to get good tickets, close to the stage. The show is every bit as good as the reviews, and Sophie and you both have a great time."
        call sophie_date from _call_sophie_date_1
        $ sophie.relationship_status = 4
        $ sophie.fire_week = week + 3
        change player money by -100
        call character_location_return(sophie) from _call_character_location_return_742
        notify
        end_day
      else:
        "You don't have enough money to go on this date at the moment."
        jump menu_sophie_contact_1
    "Quiet night at home" if not sophie.contact_quiet_night:
      player.c "How about a quiet evening at my house. Just the two of us?"
      wt_image recept_desk_1
      sophie.c "Oh.  That doesn't sound all that interesting, frankly."
      $ sophie.contact_quiet_night = True
      $ title = "What do you suggest now?"
      jump menu_sophie_contact_1
    "Perhaps another time":
      player.c "Perhaps we could get together next week?  Maybe a nice restaurant and then a show?"
      sophie.c "That sounds nice.  I'll look forward to your call."
      $ sophie.relationship_status = 5
  return

label sophie_date:
    call forced_movement(living_room) from _call_forced_movement_1001
    summon sophie
    if sophie.has_tag('will_spank_her'):
        wt_image recept_date_4
        sophie.c "That was a great night out!  Now I guess it's time for me to keep my end of the bargain."
        player.c "Indeed it is.  On your knees."
        wt_image recept_date_5
        sophie.c "Yes, Sir, Mr. Bossy Pants."
        player.c "Not like that.  On all fours."
        wt_image recept_date_6
        sophie.c "Is this better?"
        player.c "Yes, now turn around and tell me, when was the last time you were spanked?"
        wt_image recept_date_52
        sophie.c "You were serious about the spanking??  I've never been spanked.  Even my parents didn't spank me."
        player.c "Maybe that explains the rudeness and the lying.  And the not listening to instructions.  Get back on all fours."
        wt_image recept_date_53
        sophie.c "Is this what you expect from all of your dates?"
        player.c "The ones who've been bad, yes.  Sometimes the ones who've been good, too, but you need to take your punishment spanking first before you'll earn a good girl spanking."
        sophie.c "So you just like spanking women, regardless of how they've behaved?"
        player.c "I spank them harder when they don't listen.  Present your ass to me."
        wt_image recept_date_54
        "She watches curiously as you move into position behind her"
        wt_image recept_date_8
        "*smack*"
        sophie.c "Ouch!  That stings."
        player.c "Of course it stings.  It wouldn't be much of a punishment if it didn't.  Put your hand down."
        wt_image recept_date_54
        "*smack*"
        sophie.c "Ouch"
        "*smack*"
        sophie.c "Ouch"
        "*smack*"
        wt_image recept_date_55
        sophie.c "OUCHH!  That one hurt!"
        player.c "As the spanking goes on, I'm going to make it more intense, yes.  Get back in position."
        wt_image recept_date_56
        "You take it easy on her, but she reacts to your lightest swats almost as much as she does to the more serious ones, and keeps reaching her hand back."
        "*smack*  ...  *smack*  ...  *smack*"
        sophie.c "OUCH  ...  OUCH  ...  OUCH"
        wt_image recept_date_57
        "Eventually she uses both hands to protect her sore cheeks, and while it's tempting to spank her on the obvious target she's left you, she's not ready for that yet."
        wt_image recept_date_9
        "When you finish, she stands up and rubs her bottom vigorously."
        sophie.c "You're the first man to take me on a date and want to spank me afterwards instead of fuck me."
        player.c "Who said I didn't want to fuck you?"
        sophie.c "I think we're even now, don't you?  My bum is going to be sore for a week."
        wt_image recept_date_58
        "More like an hour, you expect.  Perhaps you should have asked for 'the usual'.  On the other hand, it isn't every day you get to spank a virgin ass."
        $ sophie.spank_count += 1
        change player energy by -energy_short
    else:
        wt_image recept_date_24
        sophie.c "That was a great night out!  Now I guess it's time for me to keep my end of the bargain."
        player.c "What bargain was that?"
        wt_image recept_date_11
        sophie.c "You take me out for a date, and afterwards I let you fuck me."
        wt_image recept_date_12
        "She unclasps the top of her dress ..."
        player.c "Did we make that bargain?"
        wt_image recept_date_13
        "... then lets the top of her dress fall loose."
        sophie.c "Isn't that why you asked me out?"
        wt_image recept_date_34
        sophie.c "I thought that was always the reason guys ask me out."
        wt_image recept_date_35
        "You should probably talk to her about that cynical attitude towards men, but it's hard to pay attention to the conversation as she lowers her dress, exposing her ass."
        wt_image recept_date_28
        sophie.c "Now that my dress is out of the way, how about you come closer?"
        wt_image recept_date_36
        "As you approach, she squats down and takes out your cock, giving the head a little lick..."
        wt_image recept_date_17
        "... then wraps her lips around you and starts to suck as her hand strokes your shaft."
        wt_image recept_date_16
        "After a few minutes, she looks up at you."
        sophie.c "You seem hard now.  Do you want to fuck me now?"
        $ title = "What do you want?"
        menu:
            "Just a blow job is fine":
                player.c "Just keep sucking me, Sophie."
                sophie.c "Are you sure?  It was an expensive date.  It's worth more than a blow job."
                player.c "A blow job's fine."
                wt_image recept_date_36
                sophie.c "Okay, if that's all you want."
                wt_image recept_date_37
                "She goes back to using her tongue ..."
                wt_image recept_date_17
                "... lips and hand to worship your cock."
                wt_image recept_date_16
                sophie.c "I don't let a guy cum on my face on a first date, but you can cum on my tits if you want?"
                $ title = "Where do you want to cum?"
                menu:
                    "On her tits":
                        wt_image recept_date_37
                        "Sophie licks the underside of your cock as she pumps, pulling back just as you start to spurt."
                        wt_image recept_date_39
                        player.c "[player.orgasm_text]"
                        "She's a little slow pulling back, and takes a few spurts across the chin before she can direct the remainder onto her bosom."
                        $ sophie.facial_count += 1
                    "In her mouth":
                        player.c "I'd rather watch you swallow my cum, Sophie."
                        wt_image recept_date_37
                        sophie.c "Okay"
                        wt_image recept_date_38
                        player.c "[player.orgasm_text]"
                        wt_image recept_date_16
                        $ sophie.swallow_count += 1
                sophie.c "Was that okay?  I had a great evening.  Did I do enough to be fair to you?"
                player.c "You were great, Sophie."
                sophie.c "Thanks!  I didn't want to seem ungrateful."
                player.c "You didn't."
                $ sophie.blowjob_count += 1
                orgasm
            "Pleasure her then fuck her":
                wt_image recept_date_31
                "You stand her up ..."
                wt_image recept_date_40
                "... and she exposes herself to you."
                wt_image recept_date_18
                "Then you surprise her by licking and nibbling at her sex."
                sophie.c "Ooouuuu .... that's nice."
                wt_image recept_date_41
                "When she's sopping wet you turn her around"
                call sophie_date_sex_finish from _call_sophie_date_sex_finish
            "Eat her out":
                wt_image recept_date_31
                "You stand her up ..."
                wt_image recept_date_40
                "... and she exposes herself to you."
                wt_image recept_date_18
                "Then you surprise her by licking and nibbling at her sex."
                sophie.c "Ooouuuu .... that's nice."
                wt_image recept_date_32
                "After a few minutes, she pushes your head away."
                sophie.c "I'm really wet.  You should fuck me now."
                $ title = "Fuck her now?"
                menu:
                    "Fuck her":
                        wt_image recept_date_41
                        "You turn her around as she smiles at you."
                        call sophie_date_sex_finish from _call_sophie_date_sex_finish_1
                    "Just eat her":
                        player.c "I just want to eat you."
                        sophie.c "Are you sure?  It was a nice date.  Don't you want something more?"
                        player.c "Just your juices."
                        wt_image recept_date_40
                        "The smell of her arousal is thick and pungent as you return your face to her sticky sex."
                        wt_image recept_date_18
                        "With only a few more licks of your tongue, she floods your mouth with the juices you wanted."
                        sophie.c "Oh .. oh ... oh ... ohhhh .... ohhhhh myyy Gaawwwddd!"
                        wt_image recept_date_31
                        sophie.c "You're a rare breed.  Most guys want to get orgasms, not give them.  Do you get off on serving women?"
                        $ title = "What do you tell her?"
                        menu:
                            "Yes, I enjoy serving a beautiful woman":
                                player.c "Yes, I enjoy being of service.  Especially to a beautiful woman like you."
                                wt_image recept_date_44
                                sophie.c "Oh. I'm not good at bossing guys around. But if that's what you're into, I guess I could make you worship my ass."
                                $ title = "What do you say?"
                                menu:
                                    "Yes, please":
                                        player.c "I would love the opportunity to worship your ass."
                                        wt_image recept_date_45
                                        sophie.c "Then get on your knees and bury your nose in my ass before I get very cross with you."
                                        wt_image recept_date_46
                                        "She's better at this than she let on.  She keeps you there for quite some time, tongue buried in her pussy, face between her ass cheeks, nose against her back hole."
                                        "She doesn't cum again, but you get throbbing hard, and she won't let you touch yourself."
                                        wt_image recept_date_41
                                        sophie.c "I think that's enough ass worship for one date, don't you?"
                                        player.c "Yes, thank you.  May I ..."
                                        sophie.c "Touch yourself?  No way.  You wanted this to be about my pleasure, didn't you?"
                                        wt_image recept_date_34
                                        sophie.c "I hope that was okay?  I don't have much experience with guys who want to be made to do things, instead of me ding things for them."
                                        player.c "You did fine."
                                        wt_image recept_date_1
                                        sophie.c "Thanks!  As long as you feel like I've done enough to be fair.  I enjoyed our date and don't want to seem ungrateful."
                                        player.c "You didn't."
                                        add tags 'worshipped_her' to sophie
                                    "That's okay":
                                        player.c "That's okay.  I enjoyed eating you out."
                                        sophie.c "Are you sure?  I had a great evening.  I don't want to seem ungrateful."
                                        player.c "You don't.  We're good."
                                        wt_image recept_date_34
                                        sophie.c "Well, okay.  As long as you feel like I've done enough to be fair."
                                sophie.c "I don't want to seem ungrateful.  I had a great evening"
                            "I just wanted to make you feel good today":
                                player.c "I just wanted to make you feel good today."
                                wt_image recept_date_15
                                sophie.c "But you paid for the date."
                                player.c "Can't I pay for the date and make you feel good, both?"
                                sophie.c "I guess.  If that's what you want.  I had a great evening.  I don't want to seem ungrateful."
                                player.c "You don't.  We're good."
                                wt_image recept_date_34
                                sophie.c "Well, okay.  As long as you feel like I've done enough to be fair."
                            "I just felt like swallowing your cum today":
                                player.c "You taste good.  I just wanted to taste more of you today."
                                wt_image recept_date_15
                                sophie.c "That's cool.  Do you want me to return the favour before I go?"
                                $ title = "Do you want her to suck you off?"
                                menu:
                                    "Yes":
                                        wt_image recept_date_36
                                        "Sophie drops back down to her knees ..."
                                        wt_image recept_date_17
                                        "... and begins to suck you off, eagerly"
                                        wt_image recept_date_37
                                        "... soon earning her own flood of juices."
                                        wt_image recept_date_38
                                        player.c "[player.orgasm_text]"
                                        wt_image recept_date_16
                                        sophie.c "Was that okay?  I had a great evening.  Did I do enough to be fair to you?"
                                        player.c "You were great, Sophie."
                                        sophie.c "Thanks!  I didn't want to seem ungrateful."
                                        player.c "You didn't."
                                        $ sophie.blowjob_count += 1
                                        orgasm
                                    "No":
                                        player.c "No need."
                                        sophie.c "Are you sure?  I had a great evening.  I don't want to seem ungrateful."
                                        player.c "You don't.  We're good."
                                        wt_image recept_date_34
                                        sophie.c "Well, okay.  As long as you feel like I've done enough to be fair."
                        $ sophie.orgasm_count += 1
                        change player energy by -energy_short
            "Just fuck her":
                wt_image recept_date_31
                "You stand her up ..."
                wt_image recept_date_40
                "... and she exposes herself to you."
                wt_image recept_date_47
                "You're able to enter her, but she's a little dry."
                sophie.c "Wait.  Lie down.  I know how to make this easier."
                wt_image recept_date_48
                "As you lie down, she positions you at her opening, and slowly lowers herself onto you."
                wt_image recept_date_49
                "Then as her body adapts, she starts riding you, up and down, faster and faster ..."
                wt_image recept_date_50
                "... until you can hold back no longer."
                wt_image recept_date_51
                player.c "[player.orgasm_text]"
                wt_image recept_date_35
                sophie.c "Was that okay?  I had a great evening.  Did I do enough to be fair to you?"
                player.c "You were great, Sophie."
                sophie.c "Thanks!  I didn't want to seem ungrateful."
                player.c "You didn't."
                $ sophie.sex_count += 1
                orgasm
            "Nothing more":
                player.c "That's enough, Sophie."
                wt_image recept_date_15
                sophie.c "But you haven't even cum.  Was I doing something wrong?"
                player.c "You were fine.  I just don't feel like sex today."
                sophie.c "Are you sure?  I had a great evening.  I don't want to seem ungrateful."
                player.c "You don't.  We're good."
                wt_image recept_date_14
                sophie.c "Well, if you say so.  But I don't feel like I've done enough to be fair to you."
                change player energy by -energy_short
    return

label sophie_date_sex_finish:
    wt_image recept_date_19
    "She purrs softly as you enter her."
    sophie.c "Mmmmm"
    wt_image recept_date_20
    "With your cock still inside her from behind, you surprise her by lying both yourself and her on the floor."
    wt_image recept_date_42
    "In this position, you start guiding her up and down on your shaft, her back rubbing against your chest as your hands play with her ample breasts."
    wt_image recept_date_43
    "After a few minutes, she wriggles out of your grasp and sits upright.  She starts riding you up and down, faster and faster, as her orgasm builds."
    sophie.c "Oh .. oh ... oh ... ohhhh .... ohhhhh  ....."
    wt_image recept_date_21
    sophie.c ".... ohhhhh  .....   oh myyy Gaawwwddd!"
    "As she's enjoying her climax, you let yourself go and enjoy your own."
    wt_image recept_date_42
    player.c "[player.orgasm_text]"
    wt_image recept_date_22
    sophie.c "Was that okay?  I had a great evening, and you're really good at sex!  Did I do enough to be fair to you?"
    player.c "You were great, Sophie."
    sophie.c "Thanks!  I didn't want to seem ungrateful."
    player.c "You didn't."
    $ sophie.sex_count += 1
    $ sophie.orgasm_count += 1
    add tags 'orgasm_from_sex' to sophie
    orgasm
    return

# Contact - Help Receptionist
label sophie_contact_help:
  # $ sophie.training_session() ## no only when happens
  $ title = "How do you help Sophie?"
  menu:
    "Start her on a more lucrative career (costs 50 and ends day)":
      if player.money - player.min_money >= 50:
        $ sophie.training_session()
        wt_image recept_post_fire_2
        player.c "Sophie, I think I may have a solution for you.  Let's discuss it over dinner out.  My treat."
        wt_image recept_post_fire
        sophie.c "Okay"
        wt_image living_room.image
        "You make reservations at a nice restaurant, then rest until dinner.  You're going to need your energy tonight."
        call forced_movement(outdoors) from _call_forced_movement_1002
        summon sophie
        wt_image recept_whore_prep_1
        player.c "How's the job search coming?"
        sophie.c "Okay. I won't have any trouble getting work. It just may take a few days, and I have these big bills coming up."
        player.c "Do you eat out at restaurants like this very often?"
        sophie.c "Not often. Sometimes if I go on a date with a generous guy. It's hard to afford to eat out on a receptionist's salary."
        player.c "You have good taste, Sophie. You wear nice clothes, some of the best I've ever seen on a receptionist. Your hair is always perfect."
        player.c "Perhaps you should consider a different career?"
        sophie.c "I don't know how to do anything else. I was never great at school. I'm not stupid, I'm just not good at studying."
        player.c "But you are good with men. You read them well, and when you want to, you're good at making them happy. That's a talent not everyone has."
        player.c "Perhaps you should consider putting it to work for you."
        wt_image recept_whore_prep_2
        sophie.c "You're talking about selling my body."
        "Like she said, she's not stupid. You let her think about that in silence for a few minutes while the two of you eat, then you change the topic, slightly."
        player.c "Why don't you have a boyfriend?"
        wt_image recept_whore_prep_16
        sophie.c "I don't know.  'Get yourself a nice rich man.'  That's what my Mom says every time she calls."
        player.c "So why haven't you?"
        "She shrugs."
        sophie.c "I don't want to be tied down to someone, I guess.  Especially if he controls the money."
        player.c "Independence requires a good source of income, Sophie, especially if you want to enjoy the finer things in life."
        wt_image recept_whore_prep_2
        sophie.c "I should be insulted you'd think that's something I would do."
        player.c "It's not the type of work just anyone can do. I think you could. You could make a lot of money. Enough to at least tide you over."
        "As she eats in silence, you use your cell phone to place a few posts online."
        call forced_movement(living_room) from _call_forced_movement_1003
        summon sophie
        wt_image recept_whore_prep_3
        "After dinner, you invite her back to your place to watch a movie.  She sits quietly on the sofa, picking at the popcorn.  She's lost in thought, likely thinking about your dinner conversation."
        wt_image recept_whore_prep_17
        "That gives you time to reply to the messages coming in on your phone."
        wt_image recept_whore_prep_4
        "Just before the movie ends, there's a knock on the door."
        player.c "Come in."
        sophie_whore_client_1 "Hi, I'm Mike.  I replied to your ad."
        player.c "Come in, Mike. This is Madison."
        wt_image recept_whore_prep_5
        sophie.c "Madison?  What's this about?"
        player.c "This is Mike, Madison.  He's your first client for your new career.  Mike as the ad mentioned, Madison is new to this, and may be a bit shy."
        wt_image recept_whore_prep_6
        sophie_whore_client_1 "That's okay. There's no need to be nervous, Madison. Let me help you relax."
        "Sophie startles as he suddenly kisses her neck, one hand caressing the side of her breast."
        wt_image recept_whore_prep_7
        sophie_whore_client_1 "Sit up here, Madison.  It'll give me easier access."
        wt_image recept_whore_prep_8
        "Mike pulls open her top and resumes kissing her neck."
        wt_image recept_whore_prep_18
        sophie_whore_client_1 "You're incredibly beautiful, Madison, and you've got great tits.  I'll be really generous if you suck my cock."
        wt_image recept_whore_prep_20
        "This is the moment of truth.  After a moment to collect herself, Sophie responds exactly as you expected she would."
        wt_image recept_whore_prep_9
        "She kneels on the sofa and removes Mike's cock from his pants."
        wt_image recept_whore_prep_19
        "For just a moment she hesitates, looking up at him..."
        wt_image recept_whore_prep_21
        "...then she pops his cock in her mouth and starts sucking her first dick for cash, instead of for services rendered."
        wt_image recept_whore_prep_10
        "So far so good.  Now it's time to reinforce that she's a whore."
        wt_image recept_whore_prep_11
        "Mike knew from your ad that this would be a threesome situation. He holds on to Sophie's head as you pull her panties aside. She doesn't object as you stroke her sex, not that it would be easy to do so with her head held firmly on Mike's cock."
        wt_image recept_whore_prep_12
        "Mike continues to hold 'Madison' in position as you enter her from behind. She has a moment of panic as she feels your cock pressed against her, but you hold her steady by the hips and push yourself inside."
        wt_image recept_whore_prep_22
        player.c "She's good isn't she Mike?  A good little cock sucker."
        sophie_whore_client_1 "She is.  You're doing a great job, Madison.  That feels really good."
        wt_image recept_whore_prep_23
        player.c "Roll onto your back now, Madison.  It's time to let Mike fuck you for a bit."
        wt_image recept_whore_prep_13
        "As she does as she's told, you place your cock in her mouth. She looks up at you in surprise. Possibly its the first time she's ever tasted her own pussy juices on a man's cock.  Or possibly she's just surprised that your invitation to dinner ended up like this."
        wt_image recept_whore_prep_24
        "When you're ready to climax, you pull your cock out of her mouth and shoot your jizz over her face."
        player.c "[player.orgasm_text]"
        wt_image recept_whore_prep_14
        "Mike decides that's a great idea, and pulls himself out from between her legs, depositing his cum with yours as Sophie watches."
        wt_image recept_whore_prep_15
        "Mike leaves his payment on the coffee table on his way out. Sophie sits staring at the money in front of her.  She seems to be in a bit of shock at what just transpired."
        player.c "50 of that is mine, to cover the cost of our dinner earlier.  The rest is yours."
        "Sophie nods."
        player.c "I'll call you when I've arranged your next date.  You'll go solo on that one."
        "She nods again."
        $ sophie.sex_count += 1
        $ sophie.facial_count += 1
        $ sophie.relationship_status = 8
        change player energy by -energy_short
        call character_location_return(sophie) from _call_character_location_return_743
        orgasm
        if day < 5:
          end_day
        else:
          notify
      else:
        "You'll likely be able to recover your money later, but you'll need 50 to spend on another nice dinner with Sophie if you want this plan to work."
    "Hire her to be your maid (costs 50)":
      if player.money - player.min_money >= 50:
        $ sophie.training_session()
        # rem no hypnosis tag to allow subsequent tests to work
        rem tags 'no_hypnosis' from sophie
        wt_image recept_post_fire_2
        player.c "Sophie, I have an idea on how we can help each other.  I'll pay you 50 to clean my house."
        wt_image recept_post_fire
        sophie.c "You could get a professional maid to clean your house for less than that."
        player.c "Come over and I'll explain more."
        summon sophie
        wt_image recept_thank_you_1
        "Sophie arrives within the hour."
        sophie.c "So explain this idea of yours."
        player.c "Come in.  I have something for you."
        wt_image recept_thank_you_7
        sophie.c "You want me to clean your house wearing that?"
        player.c "Yes, try it on."
        wt_image recept_maid_20
        "She returns a few minutes later, dressed a little different than she did for her last job."
        wt_image recept_maid_1
        sophie.c "Is this really about me cleaning your house?"
        player.c "While I watch you, yes."
        wt_image recept_maid_15
        sophie.c "And that's worth 50 to you?"
        player.c "Yes"
        wt_image recept_maid_16
        sophie.c "Okay, but all you get to do is look."
        wt_image recept_maid_17
        "To her credit, she actually does clean ..."
        wt_image recept_maid_18
        "... and she puts on a show while she does it."
        wt_image recept_maid_2
        "That she does a good job of entertaining you doesn't surprise you."
        wt_image recept_maid_3
        "That she actually gets the house cleaned, too, is even more impressive."
        wt_image recept_maid_19
        "After a few hours, exhausted, she sits down."
        sophie.c "That's everything cleaned.  I think I earned my money."
        $ title = "What now?"
        menu menu_sophie_maid_1:
          "Offer a tip (costs 50)":
            # note: calc also need to reflect the cost of the original maid service
            if player.money - player.min_money >= 100:
              wt_image recept_maid_22
              sophie.c "A tip?  What would I have to do to earn that?"
              player.c "Use your imagination."
              # content if you spanked her after her date
              if sophie.spank_count > 0:
                if sophie.has_tag('came_on_her_face'):
                  wt_image recept_maid_19
                  sophie.c "I'd be okay with you jerking off on me again.  Do you want to do it like this?"
                  wt_image recept_maid_23
                  player.c "Let's get you naked, first."
                  wt_image recept_maid_24
                  sophie.c "How's this?"
                  player.c "Good.  Make a pretty target for me."
                  wt_image recept_maid_25
                  "She sits demurely in front of you as you remove your cock and start stroking it in front of her face."
                  wt_image recept_maid_26
                  player.c "Lie back and look at me while I cum on you, Sophie."
                  wt_image recept_maid_14
                  player.c "[player.orgasm_text]"
                  wt_image recept_maid_28
                  sophie.c "Was that good?  Did I earn my tip?"
                  player.c "It was, and you did."
                  sophie.c "Oh good!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                  change player money by -100
                  $ sophie.facial_count += 1
                  orgasm
                # content for Dom if didn't jerk off on her before
                else:
                  wt_image recept_maid_22
                  "She thinks for a minute ..."
                  wt_image recept_maid_38
                  "... then demurely lowers her eyes and removes her top."
                  sophie.c "I probably did a really bad job at the cleaning."
                  wt_image recept_maid_39
                  sophie.c "I understand if you need to punish me."
                  wt_image recept_maid_40
                  sophie.c "If you want to leave me here on my knees to wait until you're ready to punish me, that's okay. I understand you Doms like your women to do that sort of thing, sometimes."
                  player.c "You've been doing research."
                  sophie.c "A little."
                  player.c "Thinking about becoming a sub?"
                  sophie.c "Definitely not.  It's just in case another Dom asks me out sometime.  I like to make sure the men who date me get their money's worth."
                  $ title = "What do you want for your money's worth from your tip?"
                  menu menu_sophie_maid_2:
                    "Fuck her":
                      player.c "In that case you should know that sometimes we want our women to shut their mouths and spread their legs.  Without panties on, getting in the way."
                      wt_image recept_maid_41
                      "Silently she removes the offending article."
                      wt_image recept_maid_7
                      "As she gets back into position, she understands that your expectations of her are of the more normal, garden-variety male wants."
                      wt_image recept_maid_42
                      "You position yourself behind her and tease the head of your cock up and down along her entrance until she's ready to receive you."
                      wt_image recept_maid_43
                      "After a while, she's not just receiving you, but enjoying it, too."
                      sophie.c "oh"
                      $ title = "Wait for her to cum?"
                      menu:
                        "Yes":
                          wt_image recept_maid_42
                          "She seems to be getting into this, so you slow your pace ..."
                          sophie.c "oh ... ohh"
                          wt_image recept_maid_43
                          "... and control your own excitement as hers builds."
                          sophie.c "oh ... ohhhh .... ohhhhh"
                          wt_image recept_maid_8
                          "Fortunately, she doesn't take too long."
                          sophie.c "oh ... ohhhh .... ooohhhh ... I'm going to ..."
                          player.c "No talking."
                          wt_image recept_maid_43
                          sophie.c "Sorry!  oh ... ohhhh ...."
                          wt_image recept_maid_44
                          sophie.c "Oh .. oh ... oh ...  ohhhhh  .....  oh myyy Gaawwwddd!"
                          wt_image recept_maid_8
                          "You can't hold out any longer after that display."
                          player.c "[player.orgasm_text]"
                          wt_image recept_maid_45
                          sophie.c "Wow, that was great!  Did I earn my tip?  Oh!  Am I allowed to talk yet?"
                          $ sophie.orgasm_count += 1
                          add tags 'orgasm_from_sex' to sophie
                        "No":
                          wt_image recept_maid_42
                          "You're paying for this fuck, not her.  You quicken your pace ..."
                          wt_image recept_maid_8
                          "... and soon empty your balls inside her."
                          player.c "[player.orgasm_text]"
                          wt_image recept_maid_45
                          sophie.c "Did I earn my tip?  Oh!  Am I allowed to talk yet?"
                      player.c "You did, and you are."
                      wt_image recept_maid_46
                      sophie.c "Oh good!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                      $ sophie.sex_count += 1
                      change player money by -100
                      orgasm
                    "Spank her":
                      player.c "You're going to have a very red ass before I'll have my money's worth."
                      sophie.c "I know.  I'm ready for it this time."
                      wt_image recept_maid_47
                      "She may feel she's ready, but she still howls like a banshee almost from the first swat."
                      "*smack*  ...  *smack*  ...  *smack*  ...  *smack*  ...  *smack*"
                      sophie.c "OUCH  ...  OUCH  ...  OUCH!  ...  OUCH!!  ...  OUCH!!!"
                      wt_image recept_maid_39
                      sophie.c "Wow, you're right.  My ass is sore."
                      player.c "We're just getting started.  Lose the panties."
                      wt_image recept_maid_41
                      sophie.c "I'm only letting you spank me."
                      player.c "I want to make sure you aren't holding out on me and getting wet while I do so."
                      wt_image recept_maid_48
                      sophie.c "Do some women really get wet from being spanked?"
                      player.c "The lucky ones can even cum just from a spanking."
                      sophie.c "You're kidding!"
                      player.c "Nope.  Let's see if you're one of them."
                      wt_image recept_maid_33
                      sophie.c "Sorry.  Completely dry as you can see.  I'm guessing you still want to keep spanking me, anyway?"
                      wt_image recept_maid_49
                      "That was a pretty safe guess.  *smack*  ...  *smack*  ...  *smack*  ...  *smack*  ...  *smack*"
                      sophie.c "OUCH  ...  OUCH  ...  OUCH!  ...  OUCH!!  ...  OUCH!!!"
                      wt_image recept_maid_50
                      sophie.c "My ass really is going to be sore for a week this time.  You sure make a girl earn her tip."
                      wt_image recept_maid_23
                      sophie.c "Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                      change player money by -100
                      $ sophie.spank_count += 1
                      change player energy by -energy_short
                    "Spank her then fuck her":
                      player.c "Then you'll understand that for my tip I'm going to fuck you after I turn your ass a pretty shade of red to look at while I'm doing so."
                      sophie.c "That sounds like two tips, not one."
                      $ title = "What do you say?"
                      menu:
                        "Double the tip to 100":
                          if player.money - player.min_money >= 150:
                            player.c "Deal.  You're going to have a very red ass before I'll have my money's worth."
                            sophie.c "I know.  I'm ready for it this time."
                            wt_image recept_maid_47
                            "She may feel she's ready, but she still howls like a banshee almost from the first swat."
                            "*smack*  ...  *smack*  ...  *smack*  ...  *smack*  ...  *smack*"
                            sophie.c "OUCH  ...  OUCH  ...  OUCH!  ...  OUCH!!  ...  OUCH!!!"
                            wt_image recept_maid_39
                            sophie.c "Wow, you're right.  My ass is sore."
                            player.c "We're just getting started.  Lose the panties."
                            wt_image recept_maid_41
                            sophie.c "Where do you want me?"
                            player.c "I'm not fucking you yet.  I want that ass red and sore first.  Plus the longer I spank you, the wetter you may get."
                            wt_image recept_maid_48
                            sophie.c "From you spanking me?  No way!  Does that actually work for some women?"
                            player.c "The lucky ones can even cum just from being spanked."
                            sophie.c "You're kidding!"
                            player.c "Nope.  Let's see if you're one of them."
                            wt_image recept_maid_33
                            sophie.c "Sorry.  Completely dry as you can see.  I'm guessing you still want to keep spanking me, anyway?"
                            wt_image recept_maid_49
                            "That was a pretty safe guess.  *smack*  ...  *smack*  ...  *smack*  ...  *smack*  ...  *smack*"
                            sophie.c "OUCH  ...  OUCH  ...  OUCH!  ...  OUCH!!  ...  OUCH!!!"
                            wt_image recept_maid_7
                            sophie.c "Holy shit, are you ready to fuck me yet???"
                            player.c "So turned on you can't wait?"
                            sophie.c "What??  No!  It's just my ass really is going to be sore for a week this time.  Can't you just start fucking me now?"
                            player.c "Well, since you asked so politely ... spread your legs and shut your mouth."
                            wt_image recept_maid_42
                            "You position yourself behind her and tease the head of your cock up and down along her entrance until she's ready to receive you."
                            wt_image recept_maid_43
                            "After a while, she's not just receiving you, but enjoying it, too."
                            sophie.c "oh"
                            player.c "And you said you didn't like getting spanked."
                            wt_image recept_maid_42
                            sophie.c "That's not the ..."
                            "You bring a hand turn on her rump, hard ... *SMACK*"
                            sophie.c "OUCH!!!!"
                            player.c "I said shut your mouth, and I meant it."
                            wt_image recept_maid_43
                            "She clams up, but she's still enjoying this, regardless of whether it's because of or despite the spanking."
                            $ title = "Wait for her to cum?"
                            menu:
                              "Yes":
                                wt_image recept_maid_42
                                "She seems to be getting into this, so you slow your pace ..."
                                sophie.c "oh  ...  ohh"
                                wt_image recept_maid_43
                                "... and control your own excitement as hers builds."
                                sophie.c "oh ... ohhhh .... ohhhhh"
                                wt_image recept_maid_8
                                "Fortunately, she doesn't take too long."
                                sophie.c "oh ... ohhhh .... ooohhhh ... I'm going to ..."
                                "*SMACK*"
                                player.c "I said no talking."
                                wt_image recept_maid_43
                                sophie.c "Sorry!  oh ... ohhhh ...."
                                wt_image recept_maid_44
                                sophie.c "Oh .. oh ... oh ...  ohhhhh  .....  oh myyy Gaawwwddd!"
                                wt_image recept_maid_8
                                "You can't hold out any longer after that display."
                                player.c "[player.orgasm_text]"
                                wt_image recept_maid_45
                                sophie.c "Wow, that felt great, even with a sore ass.  Did I earn my tip?  Oh!  Am I allowed to talk yet?"
                                $ sophie.orgasm_count += 1
                                add tags 'orgasm_from_sex' to sophie
                              "No":
                                wt_image recept_maid_42
                                "You're paying for this fuck, not her.  You quicken your pace ..."
                                wt_image recept_maid_8
                                "... and soon empty your balls inside her."
                                player.c "[player.orgasm_text]"
                                wt_image recept_maid_45
                                sophie.c "Did I earn my tip?  Oh!  Am I allowed to talk yet?"
                            player.c "You did, and you are."
                            wt_image recept_maid_46
                            sophie.c "Oh good!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                            change player money by -150
                            $ sophie.spank_count += 1
                            $ sophie.sex_count += 1
                            orgasm
                          else:
                            "You can't afford to.  Choose something else."
                            jump menu_sophie_maid_2
                        "Select something else":
                          jump menu_sophie_maid_2
              # content if you worshipped her after her date
              elif sophie.has_tag('worshipped_her'):
                wt_image recept_maid_51
                sophie.c "You naughty, naughty boy.  Did you think you could get access to my body by offering money?"
                player.c "No, I just ..."
                wt_image recept_maid_52
                sophie.c "Shut up.  If I want to hear you talk, I'll tell you.  You want to pay me money to get a look under my skirt, don't you?"
                "You nod."
                wt_image recept_maid_2
                sophie.c "Get on your knees.  Eyes down.  I'll tell you when you can look up."
                wt_image carpet_1
                "You stare at the carpet in front of you, waiting to be spoken to."
                wt_image recept_maid_11
                sophie.c "This is what you wanted to see?  Well, you don't get to see it like that.  Get right down on the floor, on your belly."
                wt_image recept_maid_53
                sophie.c "That's better. Now you can look at me. This is what you want, isn't it? You want to lick it until I flood your worthless mouth with my cum, don't you."
                "You nod again."
                wt_image recept_maid_33
                sophie.c "I don't know if I'm going to let you have my juices today, but if I do, you're going to have to earn them with your nose buried in my ass."
                wt_image recept_maid_49
                sophie.c "Don't look so eager, you pathetic cuntlicker. No tasting me until your nose is all the way up my ass. Then you start working your tongue into me and don't stop till I say you can."
                wt_image recept_maid_54
                "You must do a good job, as she eventually decides to reward you, grinding down hard on your face and riding it to climax, flooding your mouth with her cum."
                sophie.c "Oh .. oh ... oh ... ohhhh .... ohhhhh myyy Gaawwwddd!"
                wt_image recept_maid_50
                sophie.c "Was that good?  Did I earn my tip?"
                "You nod."
                wt_image recept_maid_23
                sophie.c "It's okay.  You can talk now."
                player.c "That was great.  May I ..."
                wt_image recept_maid_20
                sophie.c "Touch yourself?  Definitely not!"
                wt_image recept_maid_1
                sophie.c "But you can crawl over here and give me my money."
                wt_image recept_maid_15
                sophie.c "Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                change player money by -100
                change player energy by -energy_short
              # default content
              else:
                wt_image recept_maid_23
                sophie.c "Hmmmm.  Well, I expect while I've been cleaning you've been thinking about these ..."
                wt_image recept_maid_32
                sophie.c "... because guys seem to find them interesting."
                wt_image recept_maid_55
                sophie.c "And maybe you've been hoping to have a peek back here, too?"
                wt_image recept_maid_56
                sophie.c "And possibly you've even been imagining what this would feel like."
                wt_image recept_maid_57
                "She unzips your pants ..."
                wt_image recept_maid_58
                "... gives your cock a playful lick ..."
                wt_image recept_maid_12
                "... then pops it into her mouth."
                wt_image recept_maid_60
                sophie.c "Is a blow job enough, or do I need to do more to earn my tip?"
                $ title = "What do you tell her?"
                menu:
                  "A blow job's fine":
                    wt_image recept_maid_12
                    "A hand on the back of her head let's her know you want her mouth right where it is."
                    wt_image recept_maid_59
                    "She stays there until she's finished the task at hand."
                    wt_image recept_maid_61
                    "The only remaining question is where to cum?"
                    $ title = "Where do you want to cum?"
                    menu:
                      "In her":
                        wt_image recept_maid_59
                        player.c "[player.orgasm_text]"
                        wt_image recept_maid_12
                        "She swallows it all ..."
                        wt_image recept_maid_58
                        "... then licks your cock clean."
                        wt_image recept_maid_23
                        $ sophie.swallow_count += 1
                      "On her":
                        wt_image recept_maid_60
                        player.c "I know you've spent the day cleaning, but you'll need to make a mess to get your tip."
                        wt_image recept_maid_37
                        "She leans back and pumps you until you shoot your jizz all over her."
                        player.c "[player.orgasm_text]"
                        wt_image recept_maid_23
                        "After she's finished with her last clean up of the day, she looks at you."
                        $ sophie.facial_count += 1
                    sophie.c "Was that good?  Did I earn my tip?"
                    player.c "It was, and you certainly did."
                    wt_image recept_maid_16
                    sophie.c "Oh good!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                    $ sophie.blowjob_count += 1
                  "You want to fuck her":
                    wt_image recept_maid_62
                    "You roll Sophie over, onto her back."
                    if sophie.has_tag('orgasm_from_sex'):
                      wt_image recept_maid_63
                      "She's already wet, and you slide into her easily."
                      sophie.c "Mmmmm"
                      wt_image recept_maid_64
                      "You start fucking her, slowly at first, then faster and faster, as she moans."
                      sophie.c "oh ... ohh"
                      wt_image recept_maid_65
                      "You consider controlling your own arousal, when you realize it's not needed."
                      sophie.c "oh ... ohhhh .... ohhhhh ....."
                      wt_image recept_maid_66
                      sophie.c "oh myyy Gaawwwddd!"
                      wt_image recept_maid_64
                      "Now it's your turn."
                      wt_image recept_maid_13
                      player.c "[player.orgasm_text]"
                      sophie.c "Oh!"
                      wt_image recept_maid_41
                      sophie.c "Wow!  That was great.  Did I earn my tip?"
                      $ sophie.orgasm_count += 1
                    else:
                      wt_image recept_maid_13
                      "It takes a bit of time, but eventually you work your way into her."
                      wt_image recept_maid_63
                      "Gradually, you're able to start pumping into her, slowly at first, then faster and faster as her body acclimatizes to having you inside her."
                      wt_image recept_maid_64
                      "Before long, you're pounding into her hard as the pressure in your balls builds past the breaking point."
                      wt_image recept_maid_63
                      player.c "[player.orgasm_text]"
                      sophie.c "Oh!"
                      wt_image recept_maid_41
                      sophie.c "Was that good?  Did I earn my tip?"
                    player.c "It was, and you certainly did."
                    wt_image recept_maid_16
                    sophie.c "Oh good!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                    $ sophie.sex_count += 1
                change player money by -100
                orgasm
          "Hypnotize her" if player.can_hypno(sophie):
            wt_image recept_maid_4
            player.c "Before you go, Sophie, look at this for me."
            call focus_image from _call_focus_image_41
            player.c "Look and listen.  Listen to me, Sophie.  Only to me.  Only to the sound of my voice, Sophie.  I am going to talk and you are going to listen, Sophie."
            wt_image recept_maid_19
            "You soon have her under your trance."
            player.c "You want to be comfortable while we talk, Sophie.  You want to be comfortable and you want me to be comfortable.  Remove your top so we can both be comfortable, Sophie."
            wt_image recept_maid_29
            if not player.has_tag('first_hypno_breasts_message'):
              add tags 'first_hypno_breasts_message' to player
              "[player.first_hypno_breasts_message_text]"
            wt_image recept_maid_26
            $ title = "What now?"
            menu:
              "Have her blow you":
                player.c "You're very thankful to me for giving you this work.  You want to show me how thankful you are.  Get on your knees and show me how thankful you are, Sophie."
                wt_image recept_maid_27
                "It takes very little encouragement to get her to open her mouth to receive your dick."
                wt_image recept_maid_34
                "Thanking men in this way seems to come natural to her ..."
                wt_image recept_maid_35
                "... and she bobs her head back and forth along your shaft until you're feeling fully thanked."
                wt_image recept_maid_31
                $ title = "Where do you want to cum?"
                menu:
                  "In her":
                    wt_image recept_maid_35
                    player.c "[player.orgasm_text]"
                    wt_image recept_maid_31
                    "You don't need to tell her to swallow.  She does so instinctively as your balls pump your semen down her throat."
                    $ sophie.hypno_swallow_count += 1
                  "On her":
                    wt_image recept_maid_36
                    player.c "A truly grateful woman let's a man shower her with his cum, Sophie."
                    wt_image recept_maid_37
                    "The hypnotized woman leans back and pumps you until you shoot your jizz all over her."
                    player.c "[player.orgasm_text]"
                    $ sophie.hypno_facial_count += 1
                wt_image recept_maid_20
                sophie.c "Did I get everything done you wanted looked after?  I really appreciate you giving me this work.  I don't want to seem ungrateful."
                player.c "You a great job, Sophie, and you didn't seem ungrateful at all."
                wt_image recept_maid_16
                sophie.c "Thanks!  This job was exactly what I needed to tide me through.  I'm sure a new position will come up soon."
                $ sophie.hypno_blowjob_count += 1
              "Just have her pose prettily":
                wt_image recept_maid_30
                "Sophie spends the rest of the day as an ornament."
                wt_image recept_maid_11
                "It's a role she seems quite comfortable in.  Not surprising, I guess."
                wt_image recept_maid_32
                "With her attributes, no doubt men have been treating her as eye candy since puberty."
                wt_image recept_maid_33
                "Her hypnotized self finds it normal for you to do the same."
                wt_image recept_maid_24
                "You leave her in various locations as a cheerful backdrop to your newly cleaned house."
                wt_image recept_maid_20
                "Eventually you need to have her dress and release her."
                sophie.c "Wow!  Look at the time.  You sure made me earn that money."
                wt_image recept_maid_16
                sophie.c "Thanks for the work, though.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
           # the following command keeps track of how often you've hypnotized the person and subtracts the required energy
            $ sophie.hypno_session()
            change player money by -50 notify
          "Just thank her":
            player.c "Thank you, Sophie. You did a great job, and you looked great doing it."
            wt_image recept_maid_21
            sophie.c "No problem!  Thanks for the work.  It's exactly what I needed to tide me through.  I'm sure a new position will come up soon."
            change player energy by -energy_very_short
            change player money by -50 notify
        $ sophie.relationship_status = 11
        call character_location_return(sophie) from _call_character_location_return_744
      else:
        "You don't have the money for this."
    "Give her 50 (costs 50)":
      if player.money - player.min_money >= 50:
        $ sophie.training_session()
        wt_image recept_post_fire_2
        player.c "Sophie, I'm sending you 50 to get you through the week."
        wt_image recept_post_fire
        sophie.c "You are?  I really appreciate it!!  I'll pay you back as soon as I get a new job, I promise!"
        $ title = "What do you tell her?"
        menu:
          "No need, it's a gift":
            sophie.c "Really?  That's really sweet of you!  Thanks so much!!"
            add tags 'gave_gift' to sophie
            $ sophie.thank_you_week = week + 2
            $ sophie.relationship_status = 9
          "I'd like the opportunity to keep sending you money" if sophie.has_tag('worshipped_her'):
            player.c "I like being able to send you money.  Maybe we can make this a permanent arrangement?"
            sophie.c "A permanent arrangement where you send me money?  And what do I have to do?"
            player.c "Just call me up and demand it.  That's all."
            "There's silence for a bit before she responds."
            sophie.c "Send me the first 50, and I'll think about it."
            $ sophie.relationship_status = 10
            $ sophie.fin_dom_amount = 25
            add tags 'first_financial_domination' to sophie
          "Pay me back as soon as you can":
            sophie.c "I will!  I promise.  Thanks so much!!"
            $ sophie.thank_you_week = week + 2
            $ sophie.relationship_status = 9
        change player money by -50 notify
      else:
        "You don't have enough money to lend her some."
    "Nothing right now":
      pass
  notify
  wt_image current_location.image
  return

# Contact - Pimp Out Receptionist
label sophie_contact_pimp:
  $ sophie.training_session()
  $ sophie.whore_count += 1
  if sophie.whore_count == 1:
    wt_image recept_post_fire
    player.c "Sophie, your next date will be waiting for you at his hotel this evening at 8."
    player.c "Bring my cut of the money to me afterwards.  You can keep any tips."
    sophie.c "Okay"
    wt_image recept_whore_count_1_1
    "'Madison' arrives promptly on time."
    sophie.c "Hello."
    sophie_whore_client_2 "Hi, I'm John.  Please come in."
    wt_image recept_whore_count_1_11
    sophie.c "So John, what can I do to help make this a special night for you?"
    wt_image recept_whore_count_1_2
    sophie_whore_client_2 "Just having you here makes it special, sweetheart.  But it would be nice to see more of you.  And perhaps a nice blowjob and fuck before you go?"
    wt_image recept_whore_count_1_12
    "She counts his payment in the bathroom.  She's fucked men after dates that cost a lot less than her fee, even after your cut."
    wt_image recept_whore_count_1_3
    "She reminds herself of that as she gets a queasy feeling in her gut about what she's about to do."
    wt_image recept_whore_count_1_4
    "She takes a deep breath, and removes the clothes she wore to the hotel ..."
    wt_image recept_whore_count_1_5
    "... changing into some sexy lingerie ..."
    wt_image recept_whore_count_1_6
    "... for her grand re-entrance."
    wt_image recept_whore_count_1_13
    sophie_whore_client_2 "You're very beautiful, Madison."
    "She's more nervous than she lets on, or she'd let him look at her for longer."
    wt_image recept_whore_count_1_14
    "Instead she takes the initiative.  Not that he minds."
    sophie_whore_client_2 "Eager for my cock, Madison?"
    wt_image recept_whore_count_1_15
    "She doesn't answer him.  She just takes out his cock and puts it in her mouth."
    wt_image recept_whore_count_1_7
    "As his excitement builds, his language gets cruder."
    sophie_whore_client_2 "I like eager whores, Madison. That's what you are, aren't you?  An eager cock sucking whore."
    wt_image recept_whore_count_1_8
    sophie_whore_client_2 "You're a great cock sucker, Madison, but now I want to fuck your pretty whore cunt."
    wt_image recept_whore_count_1_16
    "He pulls her to her feet and bends her over one of the pillows."
    wt_image recept_whore_count_1_17
    "She's not really ready for him yet, and she didn't think to apply lube when she was in the bathroom, but he doesn't notice.  He shoves himself in."
    wt_image recept_whore_count_1_18
    "She's surprised to find her body responding to the rough treatment.  After a few strokes, she's wet enough that it no longer hurts."
    wt_image recept_whore_count_1_19
    "With a shock, she realizes that with a little more contact on her clit, she might cum.  Even without the contact, she feels a climax growing."
    wt_image recept_whore_count_1_9
    "Then it's cut short when he orgasms with a deep groan."
    sophie_whore_client_2 "Uuuggghhhh"
    wt_image recept_whore_count_1_10
    "'Shit!' she thinks, as she cleans herself up in the bathroom. 'Is it possible I can actually do this and even enjoy it??'"
    $ player.whore_income += 50
  elif sophie.whore_count == 2:
    wt_image recept_post_fire
    player.c "Sophie, your date tonight asked for a slut.  Buy yourself an appropriate outfit.  Consider it an investment towards your future earnings."
    wt_image recept_whore_count_2_1
    "Sophie has good, if expensive, taste.  When she buys her slut outfit, she manages to make it high-class and low-class in equal measures."
    wt_image recept_whore_count_2_8
    "Her 'date' circles her, an approving look on his face."
    sophie_whore_client_3 "Well, well.  You're quite the slut, aren't you?"
    wt_image recept_whore_count_2_9
    sophie_whore_client_3 "I throw a few bills your way and I bet a slut like you will do anything she's told.  Show me how hard your nipples get when a man gives you money, slut."
    wt_image recept_whore_count_2_2
    "Sophie removes her top and leans forward, pinching her own nipples as he watches her.  This time, she's not surprised when her body responds to the situation.  Her nipples stand up at attention for him."
    sophie_whore_client_3 "You've got big tits, don't you slut?  Big slutty tits with hard slutty nipples.  Shake 'em for me.  Shake those big slutty boobs of yours."
    wt_image recept_whore_count_2_10
    "'Madison' shakes her boobs as the wetness between her legs grows."
    sophie_whore_client_3 "Come here and sit on my lap, slut."
    wt_image recept_whore_count_2_11
    sophie_whore_client_3 "That's right, slut.  I'm giving you a chance to feel my hard cock against your ass, just the way a slut like you likes it."
    wt_image recept_whore_count_2_12
    "Sophie wiggles her butt against him as she sits down."
    sophie_whore_client_3 "You like that.  You like having a hard cock pressed against your ass.  You're going to like this even more when I give these big slutty tits of yours a squeeze."
    wt_image recept_whore_count_2_3
    "She doesn't have to fake the purr that escapes her throat as he squeezes her breasts roughly."
    sophie.c "Mmmmmm"
    wt_image recept_whore_count_2_4
    sophie_whore_client_3 "Get on your knees, slut.  I want to see how a slut like you sucks cock."
    wt_image recept_whore_count_2_13
    sophie_whore_client_3 "Show off your tits as you suck me, slut.  You like this, don't you?  You like it when a man recognizes and treats you like the slut you are."
    "She doesn't actually like being called a slut.  Not really.  But her cunt is wet, and she decides not to think too hard about why that is.  She just goes with the flow."
    "He's happy, and she's always been fine with making men happy, as long as she's properly compensated for what she's giving them back in return."
    wt_image recept_whore_count_2_14
    sophie_whore_client_3 "Eyes on me, slut.  I want to see how much you like it when I face fuck you.  This is what you love best, isn't it?  Being a cock sheath"
    wt_image recept_whore_count_2_15
    sophie_whore_client_3 "Get on the bed, cock sheath.  I'm going to try one of your other slut holes."
    "'Cock sheath' is a new one to her, but it's exactly what she wants to be right now.  She just hopes it's the hole between her legs that he wants, as she realizes she forgot to specify extra for her back door."
    wt_image recept_whore_count_2_16
    "To her relief, her cunt is exactly what he wants to fuck.  She lets out a moan as he enters her."
    sophie.c "Oh!"
    wt_image recept_whore_count_2_17
    sophie_whore_client_3 "Do your friends know you like to be treated this way? Do your girlfriends know you love being a cocksheath? I bet your male friends wish they knew how easily you'd spread your legs for them if they treated you like a slut."
    wt_image recept_whore_count_2_5
    "She fights back a surge of anger. She wants to tell him to 'go fuck himself', but her cunt is soaked and her nipples are hard, and she's scared he'll laugh at her if she tries to deny it."
    wt_image recept_whore_count_2_16
    "Instead, she focuses on controlling her building excitement, a task made more difficult by the burning need in her nipples to be pinched."
    wt_image recept_whore_count_2_18
    "She grits her teeth and tries not to moan, even as her fingers ease the throbbing in her nipples."
    "She doesn't want him to see her cum.  Partly because he hasn't paid her enough for that, but mostly because she fears what he'll call her if she does."
    wt_image recept_whore_count_2_5
    "To her relief, he stops talking while he fucks her, and a few minutes later pulls himself out of her."
    wt_image recept_whore_count_2_6
    sophie_whore_client_3 "Thanks for the fuck, slut.  You can have my cum now, as a reward."
    "As he points his throbbing cock at her, she pinches her nipple hard without realizing it."
    wt_image recept_whore_count_2_19
    "A moment later, he empties a surprisingly large load over her tits and belly."
    wt_image recept_whore_count_2_7
    sophie_whore_client_3 "Thanks for that, Madison. You were a really great sport. And a good actor, too! You made it seem like you were really enjoying me calling you those names."
    sophie.c "Oh ... no problem!  As long as you had fun and got your money's worth, that's all that matters."
    sys "'Madison' knows what she's doing, and has developed a nice reputation online.  The website you set up for her will provide a steady stream of customers."
    sys "You no longer need to spend any time or Energy to pimp her out.  She'll keep working tricks for you and provide your cut at the end of each week.  You can take a smaller cut now that you no longer need to spend any Energy arranging dates for her."
    sys "You should check in with her, however, every once and a while to make sure she's doing okay."
    $ sophie.whore_lost_countdown = 5
    $ player.whore_income += 25
    $ sophie.change_full_name("", "'Madison'", "the Whore")
    call convert(sophie, "whore") from _call_convert_53
  change player energy by -energy_short notify
  return

# Contact - Check On Whore
label sophie_check_whore:
  wt_image recept_whore_portrait
  player.c "How's my favorite professional cock sucker?"
  sophie.c "I hate when you call me that."
  player.c "Do you really?  Not holding out on me, are you?"
  "She hesitates just long enough to let you know she probably is, but not too much, based on the income she's bringing in for you."
  sophie.c "Of course not!"
  player.c "Good.  If you get into trouble, you let me know. I'll look out for you."
  sophie.c "Okay.  I will."
  $ sophie.whore_lost_countdown = 6
  return

## Items
## Sophie
# Give Butt Plug
label give_bp_sophie:
    if current_location == lauren_office:
        "Aren't you Mister Charming?"
    else:
        "She's not willing to let you train her ass (at least not in this version of the game)."
    return

# Chastity Belt
label give_cb_sophie:
  "She's not going to take that well."
  return

# Give Dildo
label give_di_sophie:
  "This could be a thoughtful gift in some circumstances, but I'm not sure she'll take it that way."
  return

# Use Fetch Toy
label use_ft_sophie:
  "It would be easier just to ask her if she has - or is - a pet."
  return

# Give Jewelry
label give_jwc_sophie:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_sophie:
  "She'd look lovely wearing this for a walk, but she likely has other plans for her break today."
  return

# Give Lingerie
label give_li_sophie:
  if sophie.location == lauren_office:
    "She might like it, but giving it to her here while her co-workers are coming and going is just going to make her the subject of office gossip."
  else:
    "There may be a time when she'll accept this gift from you, but it's now now (or anytime during this version of the game)."
  return

# Give Love Potion
label give_lp_sophie:
  sophie.c "No thanks.  I'm not thirsty."
  return

# Give Transformation Potion
label give_tp_sophie:
  sophie.c "No thanks.  I'm not thirsty."
  return

# Use Water Bowl
label use_wb_sophie:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_sophie:
  if sophie.location == lauren_office:
    "The thought of her in the Will-Tamer is appealing, but you're not getting it on her here."
  else:
    "Collaring her would be fun, but isn't something that can be done in this version of the game."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label sophie_start_day:
  ## Wed and Receptionist Thank You
  if day == 3 and sophie.thank_you_week > 0 and sophie.thank_you_week <= week:
    rem tags 'no_hypnosis' from sophie
    wt_image front_door
    "There's a knock at your door first thing in the morning."
    summon sophie
    wt_image recept_thank_you_1
    player.c "Sophie.  So nice to see you."
    sophie.c "I have good news!  I got a new job."
    player.c "That's great to hear."
    if sophie.has_tag('gave_gift'):
      sophie.c "It's out of town, so I won't see you again. I just dropped by to say 'thank you' again for the money. I know you said it was a gift, but are you sure I can't pay you back?"
      player.c "I'm sure."
      sophie.c "Well, if you don't want my money, maybe I could thank you another way?"
    else:
      sophie.c "It's out of town, so I won't see you again.  I just dropped by to return the money you lent me.  Thanks again for this, it really helped me out."
      player.c "You're welcome."
      change player money by 50 notify
      if sophie.has_tag('orgasm_from_sex'):
        sophie.c "If you want, I can come in and show you how thankful I am?"
    $ title = "What now?"
    menu:
      "Hypnotize her" if player.can_hypno(sophie):
        player.c "Come in for a minute, Sophie.  There's something I want to show you."
        wt_image recept_thank_you_7
        sophie.c "I have a thousand things I need to do today to finish packing before I leave."
        player.c "This won't take long.  I want you to look at this."
        call focus_image from _call_focus_image_42
        player.c "Look and listen.  Listen to me, Sophie.  Only to me.  Only to the sound of my voice, Sophie.  I am going to talk and you are going to listen, Sophie."
        wt_image recept_thank_you_19
        "You soon have her under your trance."
        player.c "I did you a favor and you want to thank me for it, Sophie. You don't want to seem ungrateful. You're going to thank me for doing you a favor."
        player.c "You want to thank me by giving me a blow job, Sophie, and you want me to enjoy the sight of your tits while you blow me."
        wt_image recept_thank_you_3
        "The hypnotized woman pulls open the top of her dress, freeing her breasts.  Then she drops to her knees in front of you ..."
        wt_image recept_thank_you_20
        "... and takes your cock into her mouth."
        wt_image recept_thank_you_21
        "She has a busy day ahead and may even have friends who come looking if she's gone to long, so you can't make too much of her day 'disappear'."
        wt_image recept_thank_you_5
        "Fortunately it's not too long before you're ready to cum."
        $ title = "Where do you want to cum?"
        menu:
          "In her":
            wt_image recept_thank_you_22
            player.c "[player.orgasm_text]"
            wt_image recept_thank_you_23
            "Some of your cum dribbles out of her mouth and drips onto her tits and leg.  You have her clean up and re-arrange her dress before bringing her out of the trance."
            $ sophie.hypno_swallow_count += 1
          "On her":
            wt_image recept_thank_you_24
            "On your instructions, the hypnotized woman undresses, then watches as you point your dick at her."
            wt_image recept_thank_you_25
            player.c "[player.orgasm_text]"
            wt_image recept_thank_you_26
            "When the last of your jizz has finished spurting onto her chest, you have her clean up and re-arrange her dress before bringing her out of the trance."
            $ sophie.hypno_facial_count += 1
        wt_image recept_thank_you_2
        sophie.c "Thanks again for the money.  I have to go now and finish packing for my move.  I hope you have a great life!  Bye bye!!"
        $ sophie.hypno_blowjob_count += 1
        # the following command keeps track of how often you've hypnotized the person and subtracts the required energy
        $ sophie.hypno_session()
        orgasm notify
      "Take her up on her offer" if sophie.has_tag('gave_gift') or sophie.has_tag('orgasm_from_sex'):
        if sophie.has_tag('worshipped_her'):
          wt_image recept_thank_you_7
          sophie.c "I have a thousand things I need to do today to finish packing before I leave, but I could dominate you quickly, if you want?"
          sophie.c "Or if you prefer, I could just blow you?"
          $ title = "What do you want?"
          menu:
            "Have her dominate you":
              player.c "I'd love to worship you again, Mistress."
              wt_image recept_thank_you_12
              sophie.c "Then get down on the floor, where you belong."
              wt_image recept_thank_you_13
              sophie.c "Look at the treat I brought you.  My hot, sticky pussy.  You'd love to lick it, wouldn't you?"
              player.c "Yes, Mistress.  Please?"
              wt_image recept_thank_you_14
              sophie.c "You can lick it, but only over my panties, not under them.  Understood?"
              player.c "Yes, Mistress.  Thank you!"
              wt_image recept_thank_you_15
              "You must do a good job, because she's soon moaning from the lapping of your tongue along her pantied sex ..."
              sophie.c "oh  ...  oh  ....  ohhh  .....  oohhhhh"
              wt_image recept_thank_you_16
              "... and when you take liberties with her instructions and lick the skin on the side of her panties, she doesn't punish you ..."
              wt_image recept_thank_you_17
              "... she rewards you by pulling her panties aside..."
              wt_image recept_thank_you_18
              "... and holds your head in place as she fills your mouth with her cum."
              sophie.c "Oh .. oh ... oh ... ohhhh .... ohhhhh myyy Gaawwwddd!"
              wt_image recept_thank_you_7
              sophie.c "I wasn't planning on letting you get me off.  I hope I didn't ruin the whole domination thing for you?"
              player.c "It was flattering."
              wt_image recept_thank_you_2
              sophie.c "Oh good! I'm glad you liked it. You're good at licking pussy. I have to finish packing for my move.  Have a good life!"
              $ sophie.orgasm_count += 1
              change player energy by -energy_short notify
            "Have her blow you":
              player.c "I'd love to feel your lips on me."
              wt_image recept_thank_you_4
              sophie.c "That's only fair, considering you've used your lips on me."
              "She pulls open her dress, exposing her breasts, then drops to her knees and unzips your pants."
              wt_image recept_thank_you_21
              "Then she takes you into her mouth and starts sucking you ..."
              wt_image recept_thank_you_5
              "... while her hand plays with your balls."
              wt_image recept_thank_you_22
              "It's a hard, assertive blow job, intended to get you off quickly ..."
              wt_image recept_thank_you_6
              "... and it succeeds."
              player.c "[player.orgasm_text]"
              wt_image recept_thank_you_27
              sophie.c "That was a big load.  I couldn't even swallow it all."
              player.c "That was a great blow job."
              wt_image recept_thank_you_2
              sophie.c "Oh good!  I'm glad you liked it.  I have to go now and finish packing for my move.  Have a good life!"
              orgasm notify
        else:
          #3 preamble text for Dom
          if sophie.spank_count > 0:
            wt_image recept_thank_you_7
            sophie.c "I'd let you spank me, but I have a thousand things I need to do today and I don't need a sore bum distracting me while I do them."
            sophie.c "If I had more time, I'd let you boss me around for a while, maybe crawl for you or something like that.  Is it okay if I just give you a normal blow job?"
            player.c "I guess that will do."
          wt_image recept_thank_you_4
          "She pulls open the top of her dress, exposing her ample breasts, then drops to her knees and unzips your pants."
          if not sophie.has_tag('gave_gift'):
            wt_image recept_thank_you_3
            sophie.c "If the idea of taking this as a thank you gift makes you uncomfortable, you can consider it repayment of interest on your loan instead."
            player.c "I'm not uncomfortable at all Sophie."
            sophie.c "Oh, good!"
          wt_image recept_thank_you_21
          "She takes you into her mouth and starts sucking you ..."
          wt_image recept_thank_you_5
          "... while her hand plays with your balls."
          wt_image recept_thank_you_22
          "She's in a bit of a rush, and it shows, but it feels good regardless."
          if sophie.has_tag('orgasm_from_sex'):
            wt_image recept_thank_you_28
            sophie.c "I really don't have much time, but I don't think it would take either of us very long if you wanted to fuck me now?"
            $ title = "What do you want?"
            menu:
              "Fuck her":
                "She could have just come out and told you she wanted to get in your pants one more time before she left, but that doesn't seem to her style."
                wt_image recept_thank_you_32
                "Fortunately, her other peculiarities don't affect how wet her pussy is ..."
                sophie.c "Oh"
                wt_image recept_thank_you_33
                "... or how good it feels as you start to fuck her."
                sophie.c "oh  ...  ohh"
                wt_image recept_thank_you_34
                "You're not the only one enjoying this ..."
                sophie.c "ohh  ...  oohhh"
                wt_image recept_thank_you_35
                "... as her rapidly increasing moans attest."
                sophie.c "oh ... oh ... ohhhh .... ohhhhh"
                wt_image recept_thank_you_36
                sophie.c "Oh .. oh ... oh ...  ohhhhh  .....  oh myyy Gaawwwddd!"
                wt_image recept_thank_you_34
                "Your turn."
                wt_image recept_thank_you_33
                player.c "[player.orgasm_text]"
                wt_image recept_thank_you_28
                sophie.c "I'm going to miss having the opportunity to say 'thank you' to you."
                player.c "You can always come visit."
                sophie.c "If I was the sort to settle down, I'd think about that."
                $ sophie.orgasm_count += 1
                $ sophie.sex_count += 1
              "Have her finish her blow job":
                player.c "Just suck me off, Sophie."
                wt_image recept_thank_you_20
                "She's a bit disappointed, but goes back to blowing you."
                wt_image recept_thank_you_22
                "It's not long before you're ready to cum."
                $ title = "Where do you want to cum?"
                menu:
                  "In her":
                    wt_image recept_thank_you_6
                    player.c "[player.orgasm_text]"
                    wt_image recept_thank_you_27
                    sophie.c "That was a big load.  I couldn't even swallow it all."
                    player.c "That was a great blow job."
                    $ sophie.swallow_count += 1
                  "On her":
                    wt_image recept_thank_you_29
                    "She just smiles and pulls her dress all the way off when you removed you cock from her mouth and point it at her."
                    wt_image recept_thank_you_30
                    player.c "[player.orgasm_text]"
                    wt_image recept_thank_you_31
                    sophie.c "That was a big load."
                    player.c "That was a great blow job."
                    $ sophie.facial_count += 1
                sophie.c "Oh good!  I'm glad you liked it."
                $ sophie.blowjob_count += 1
          else:
            $ title = "Where do you want to cum?"
            menu:
              "In her":
                wt_image recept_thank_you_6
                player.c "[player.orgasm_text]"
                wt_image recept_thank_you_27
                sophie.c "That was a big load.  I couldn't even swallow it all."
                player.c "That was a great blow job."
                $ sophie.swallow_count += 1
              "On her":
                wt_image recept_thank_you_29
                "She just smiles and pulls her dress all the way off when you removed you cock from her mouth and point it at her."
                wt_image recept_thank_you_30
                player.c "[player.orgasm_text]"
                wt_image recept_thank_you_31
                sophie.c "That was a big load."
                player.c "That was a great blow job."
                $ sophie.facial_count += 1
                sophie.c "Oh good!  I'm glad you liked it."
            $ sophie.blowjob_count += 1
          wt_image recept_thank_you_2
          sophie.c "I have to go now and finish packing for my move.  It was really fun meeting you.  I hope you have a great life!  Bye bye!"
          orgasm notify
      "That won't be necessary" if sophie.has_tag('gave_gift') or sophie.has_tag('orgasm_from_sex'):
        wt_image recept_thank_you_2
        player.c "That won't be necessary, Sophie."
        if sophie.has_tag('gave_gift'):
          wt_image recept_thank_you_2
          sophie.c "Okay, well.  I tried.  Thanks again.  I hope you have a great life!  Bye bye!"
        else:
          extend "  I don't suppose the interest for a couple of weeks warrants a special thank you."
          "She laughs."
          wt_image recept_thank_you_2
          sophie.c "I guess not.  Okay then, bye bye!  I hope you have a great life!"
      "Wish her well" if not sophie.has_tag('gave_gift') and not sophie.has_tag('orgasm_from_sex'):
        player.c "Good luck with the new job, Sophie."
        wt_image recept_thank_you_2
        sophie.c "Thanks.  I hope you have a great life!  Bye!"
    $ sophie.relationship_status = 11
    $ sophie.thank_you_week = 0
    call character_location_return(sophie) from _call_character_location_return_745
  ## Wed and Receptionist Financial Domination
  elif day == 3 and sophie.relationship_status == 10:
    wt_image phone_1
    "Your phone is ringing."
    if sophie.has_tag('first_financial_domination'):
      rem tags 'first_financial_domination' from sophie
      wt_image recept_post_fire_2
      sophie.c "So I've been doing some research, and I guess this is a thing.  Women allowing men to send them money.  So I guess I could let you do that."
      sophie.c "We need to set some ground rules, though.  First, you'll call me Mistress.  Second, what should I call you?  Pay Pig, or something else?"
      $ title = "What do you tell her?"
      menu:
        "Pay Pig is fine":
          player.c "I'm looking forward to being your pay pig, Mistress."
        "I want to be called something else":
          $ sophie.your_fin_dom_name = renpy.input(_("What should she call you?"))
          sophie.c "Okay.  I guess I can call you [sophie.your_fin_dom_name]"
        "I've changed my mind":
          player.c "Actually, Sophie.  I've had a change of heart."
          sophie.c "That's okay.  The whole thing seemed weird anyway."
          $ sophie.relationship_status = 11
      # check to see if still continuing
      if sophie.relationship_status == 10:
        sophie.c "Third, you send me 25 each week, [sophie.your_fin_dom_name], but that doesn't buy you anything."
        sophie.c "Maybe if I'm feeling generous I might show you something I bought with the money, but probably I won't.  Understood?"
        player.c "Yes, Mistress.  That's fine."
        sophie.c "You can send me the first 25 now."
        $ title = "Send her the money?"
        menu menu_sophie_fin_dom_1:
          "Pay up (costs 25)":
            if player.money - player.min_money >= 25:
              player.c "I'm sending it right now, Mistress."
              sophie.c "Good boy.  If you're lucky, I'll be back to collect more from you next week."
              player.c "I'll look forward to it, Mistress."
              change player money by -25 notify
            else:
              "You don't have the money."
              jump menu_sophie_fin_dom_1
          "Decline":
            player.c "I can't this week, Mistress."
            sophie.c "We're not off on a very good start, are we, [sophie.your_fin_dom_name]?  Have money for me next week or the whole deal's off."
            add tags 'missed_payment' to sophie
    elif sophie.has_tag('missed_payment'):
      wt_image recept_post_fire_2
      sophie.c "You'd better have my money this week, [sophie.your_fin_dom_name]."
      $ title = "Send her the money?"
      menu menu_sophie_fin_dom_2:
        "Pay up (costs [sophie.fin_dom_amount])":
          if player.money - player.min_money >= sophie.fin_dom_amount:
            player.c "I'm sending it right now, Mistress."
            sophie.c "Good boy.  If you're lucky, I'll be back to collect more from you next week."
            player.c "I'll look forward to it, Mistress."
            change player money by -sophie.fin_dom_amount notify
            rem tags 'missed_payment' from sophie
          else:
            "You don't have the money."
            jump menu_sophie_fin_dom_2
        "Decline":
          player.c "I still can't afford to send it this week, Mistress."
          sophie.c "You pathetic slug.  You're not even fit to be a pay pig."
          wt_image phone_1
          "She hangs up on you."
          $ sophie.relationship_status = 11
    else:
      $ sophie.fin_dom_outfit += 1
      if sophie.fin_dom_outfit > 4:
        $ sophie.fin_dom_outfit = 1
      if sophie.fin_dom_outfit == 1:
        wt_image recept_post_fire_2
        sophie.c "Hello, [sophie.your_fin_dom_name]."
        wt_image recept_post_fire_3
        sophie.c "Look what I bought with the money you sent me.  New shoes."
        wt_image recept_thank_you_8
        sophie.c "I bet you wish you could touch them.  Even lick them.  Better yet feel them pressed against your face or crushing your balls."
        player.c "Yes, Mistress."
        wt_image recept_post_fire_2
        sophie.c "Too bad you're too pathetic to earn those privileges, [sophie.your_fin_dom_name].  Where's my money for this week?"
      elif sophie.fin_dom_outfit == 2:
        wt_image recept_post_fire_2
        sophie.c "Hello, [sophie.your_fin_dom_name].  Do you know what I bought with your money?"
        player.c "What, Mistress?"
        wt_image recept_thank_you_9
        sophie.c "New panties. See how tightly they snug up against my warm, wet snatch? Don't you wish you could put you face this close to my pussy?"
        player.c "Yes, Mistress."
        wt_image recept_post_fire_2
        sophie.c "Too bad you're only fit to send me money. At least these panties will look nice for some other guy when he gets to take them off me."
      elif sophie.fin_dom_outfit == 3:
        wt_image recept_post_fire_2
        sophie.c "Hello, [sophie.your_fin_dom_name].  I have something to show you."
        wt_image recept_thank_you_10
        sophie.c "These are old panties. Ones I don't need anymore since I bought new ones with the money you sent me."
        sophie.c "I haven't washed them. They smell like my pussy.  And my ass.  What should I do with these nasty panties?"
        $ title = "Do you want them?"
        menu:
          "Yes":
            player.c "Can I have them, Mistress?"
            sophie.c "You want my nasty, smelly old panties, [sophie.your_fin_dom_name]."
            player.c "Yes, Mistress."
            wt_image recept_post_fire_2
            sophie.c "Maybe if you're lucky I'll send them to you.  Where's my money for this week?"
          "No":
            wt_image recept_post_fire_2
            sophie.c "Where's my money for this week?"
      else:
        wt_image recept_post_fire_2
        sophie.c "Hello, [sophie.your_fin_dom_name].  I bought something special with the money you sent me."
        wt_image recept_thank_you_11
        sophie.c "Can you see what this is?  Can you guess where I'm going to put it?  What I'm going to do with it?"
        sophie.c "Of course, if you were a real man, I might let you put your dick in there instead.  But we both know that's never going to happen."
        wt_image recept_post_fire_2
        sophie.c "At least the toy your money paid for will her me cum tonight, [sophie.your_fin_dom_name].  Where's my money for this week?"
      $ title = "Send her the money?"
      menu menu_sophie_fin_dom_3:
        "Pay up (costs [sophie.fin_dom_amount])":
          if player.money - player.min_money >= sophie.fin_dom_amount:
            player.c "I'm sending it right now, Mistress."
            sophie.c "Good boy.  If you're lucky, I'll be back to collect more from you next week."
            player.c "I'll look forward to it, Mistress."
            change player money by -sophie.fin_dom_amount notify
            rem tags 'missed_payment' from sophie
          else:
            "You don't have the money."
            jump menu_sophie_fin_dom_3
        "I want to pay more" if player.money - player.min_money >= sophie.fin_dom_amount + 5:
          $ sophie.fin_dom_amount += 5
          player.c "Can I send you more money, Mistress?"
          sophie.c "Maybe you're not as pathetic as I thought you were, [sophie.your_fin_dom_name].  Okay, starting today, from now on you send me [sophie.fin_dom_amount] each week."
          player.c "Thank you, Mistress!"
          change player money by -sophie.fin_dom_amount notify
        "Decline":
          player.c "I can't this week, Mistress."
          sophie.c "That's not what I want to hear, [sophie.your_fin_dom_name].  Have money for me next week or the whole deal's off."
          add tags 'missed_payment' to sophie
    wt_image current_location.image
  ## Wed and Receptionist Fired
  elif day == 3 and sophie.relationship_status == 4 and sophie.fire_week <= week and not sophie.has_tag('transformed'):
    wt_image phone_1
    "Your phone is ringing."
    wt_image recept_post_fire
    "It's Sophie."
    sophie.c "You won't believe what that bitch did!"
    player.c "Who?"
    sophie.c "Lauren.  She fired me!"
    player.c "Fired you?  Why?"
    wt_image recept_post_fire_2
    sophie.c "She overheard me talking in the staff room about our date. The next thing I know, she's calling me into her office and telling me she has to let me go."
    player.c "What are you going to do?"
    wt_image recept_post_fire
    sophie.c "Oh, I'll be fine. I'll get another job soon. It's just ..."
    player.c "Yes?"
    sophie.c "I kind of have some bills coming due. I need to figure out a way to get some cash before the end of the week."
    player.c "I'll get back to you if I can think of a way to help."
    sophie.c "Thanks!"
    sys "If you want to help her out, you'll need to do so before the week is up."
    if (lauren.status == "post_training" and lauren.has_tag('unsatisfied')) or (lauren.status == "post_training" and lauren.has_tag('satisfied') and not lauren.has_tag('continuing_actions')) or (lauren.status == "unavailable"):
      pass
    else:
      $ lauren.action_contact_fire_sophie = living_room.add_action("Ask Lauren about Firing Sophie", label = lauren.short_name + '_contact_fire_sophie', context = "_contact_other", condition = "lauren.can_be_interacted and sophie.relationship_status == 7 and not lauren.has_tag('shut_off_fire_receptionist')")
    $ sophie.relationship_status = 7
    summon new_receptionist_lauren to lauren_office no_follows
    $ sophie.dismiss(False)
    wt_image current_location.image
  return

# End Day
label sophie_end_day:
    rem tags 'spoke_to_her_today' from sophie
    add tags 'no_hypnosis' to sophie
    if sophie.relationship_status < 6:
        summon sophie to lauren_office no_follows
    else:
        summon new_receptionist_lauren to lauren_office no_follows
    return

# End Week
label sophie_end_week:
  ## Whores Lost
  if sophie.has_tag('whore') and sophie.whore_count > 1:
    $ sophie.whore_lost_countdown -= 1
    if sophie.whore_lost_countdown <= 0:
      "You haven't checked on Sophie for quite a while. She didn't send your cut this week and you can't track her down. Whether she skipped town or got into trouble, you never find out."
      $ sophie.relationship_status = 6
      call unconvert(sophie, 'whore') from _call_unconvert_46 # not needed as covered off under convert('unavailable'), but also doesn't hurt to remove this tag first
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      call convert(sophie, "unavailable") from _call_convert_54
    else:
      $ player.whore_income += 25
  ## Receptionist Not Helped
  if sophie.relationship_status == 7:
    $ sophie.relationship_status = 6
  return


## Character Specific Timers
# N/A

########### ROOMS ###########
# Lauren's Office
# see lauren.rpy

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
