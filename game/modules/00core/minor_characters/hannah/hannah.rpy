## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
register hannah_pregame 10 in core as "Hannah the School Principal"

# Pregame
label hannah_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Hannah the School Principal (Bobbi Starr)")]

    ## Character Definition
    # 114,34,34
    hannah = Person(Character("Hannah", who_color="#722222", what_color="#722222", window_background = gui.dialogue_background_dark_font_color), "hannah", cut_portrait = True, prefix = "", suffix = "the School Principal")

    # Other Characters
    # 0,0,160
    hannah_whore_client_1 = Character("Hannah's Whore Client #1", who_color="#0000A0", what_color="#0000A0", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    hannah_whore_client_2 = Character("Hannah's Whore Client #2", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 128,64,0
    hannah_whore_client_3 = Character("Hannah's Whore Client #3", who_color="#804000", what_color="#804000", window_background=gui.dialogue_background_medium_font_color)
    # 0,64,128
    hannah_domme_client_1 = Character("Hannah's Domme Client #1", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    hannah_domme_client_2 = Character("Hannah's Domme Client #2", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 0,128,255
    hannah_domme_client_3 = Character("Hannah's Domme Client #3", who_color="#0080FF", what_color="#0080FF", window_background = gui.dialogue_background_dark_font_color)
    # Navy
    hannah_domme_client_4 = Character("Hannah's Domme Client #4", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 0,64,128
    hannah_gangbang_man_1 = Character("Gangbang Man #1", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    hannah_gangbang_man_2 = Character("Gangbang Man #2", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # Navy
    hannah_gangbang_man_3 = Character("Gangbang Man #3", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)


    ## Actions
    hannah.action_pose = hannah.add_action("Have her Pose", label="_pose", condition = "hannah.can_be_interacted and hannah.has_tag('doll')")
    hannah.action_clean = hannah.add_action("Have her Clean", label="_clean", condition = "hannah.can_be_interacted and hannah.has_tag('doll')")
    hannah.action_serve = hannah.add_action("Have her Serve", label="_serve", condition = "hannah.can_be_interacted and hannah.has_tag('doll')")
    hannah.action_test = hannah.add_action("Test her Functionality", label="_test", condition = "hannah.can_be_interacted and hannah.has_tag('doll')")
    hannah.action_booty_call = hannah.add_action("Start Booty Call Visit", label="_booty_call", condition = "hannah.can_be_interacted and hannah.has_tag('booty_call') and not hannah.has_tag('doll')")
    hannah.action_thank_you = hannah.add_action("Start Thank You Visit", label="_thank_you", condition = "hannah.can_be_interacted and hannah.has_tag('thank_you_visit')")
    hannah.action_lawyer_call = hannah.add_action("Start Lawyer Related Visit", label="_lawyer_call", condition = "hannah.can_be_interacted and hannah.has_tag('lawyer_call')")
    hannah.action_contact_pimp = living_room.add_action("Pimp Principal Out", label = hannah.short_name + "_contact_pimp", context = "_contact_other", condition = "hannah.can_be_interacted and hannah.has_tag('whore') and hannah.whore_count < 3 and not hannah.has_tag('domme') and not hannah.has_tag('doll')")
    ## activated later
    # hannah.action_contact_domme = living_room.add_action("Arrange Session for Mistress Hannah", label = hannah.short_name + "_contact_domme", context = "_contact_other", condition = "hannah.can_be_interacted and hannah.domme_outfit_count < 4")
    hannah.action_contact_group_sex = living_room.add_action("Set Up Group Sex With Hannah (Ends Day)", label = hannah.short_name + "_contact_group_sex", context = "_contact_other", condition = "hannah.can_be_interacted and (hannah.group_sex == 1 or hannah.group_sex == 3 or hannah.group_sex == 4) and not hannah.has_tag('doll')")
    # hannah.action_contact_visit = None
    hannah.action_contact_visit = living_room.add_action("Visit Hannah the School Principal", label = hannah.short_name + "_contact_visit", context = "_contact_other", condition = "hannah.can_be_interacted and hannah.has_tag('available_for_school_visit') and not hannah.has_tag('doll')")

    ## Tags
    # Common Character Tags
    hannah.add_tags('no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    # Hannah's Building
    school = Location("School", 'sch', cut_portrait = True, enter_break_labels = ['sch_no_access'], enter_labels = ['sch_enter'], exit_labels = ['sch_exit'])
    hannah.location = school
    hannah.fixed_location = school

    ## Other
    hannah.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('hannah_start_day', priority = 50)

    ########### VARIABLES ###########
    # Common Character Variables
    # hannah.add_stats_with_value('temporary_count') # not needed as auto-added
    hannah.add_stats_with_value('hypno_anal_count', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_handjob_count', 'hypno_sex_count', 'hypno_swallow_count', 'pleasure_her_count', 'random_number')

    # Character Specific Variables
    hannah.add_stats_with_value('anal', 'booty_call_count', 'deepthroat_training', 'domme_outfit_count', 'fin_domme_derandomizer', 'fin_domme_outfit_count', 'financial_domination_cost', 'foot_job', 'fuck_machine_count', 'group_sex', 'letter_re_terri', 'lost_money_and_no_fix', 'marilyn_solution_thank_you', 'spanking_count', 'visit_day', 'visit_week', 'waiting_on_banker', 'whore_count', 'whore_lost_countdown')
    # key for letter_re_terri (which is now also activated by Chelsea:
        #0: not yet; 1: letter ready to send; 2: letter ignored; 3: visited school but left without good resolution; 4: resolved conflict but no booty calls; 5: visited school and humiliated Principal with police; 6: visited school and BJ and agreed to never come back; 7: visited school booty call
        #8: visited and then used Lawyer; 9: used Lawyer without a visit; 10: took the money (removes potential for bank events); 11: punished her (opens torture show option post banker); 12: had sex with her (opens whore option post banker)
        #13: humiliated her without sex; 14: insulted her after Marilyn money solution thank you; 15: had sex with her after Marilyn money solution thank you; 16: punished her after Marilyn money solution thank you
    ## all of the following are used during conversations with Hannah, instead of using tags
    hannah.admit = False
    hannah.ask_for_money = False
    hannah.complain = False
    hannah.convince = False
    hannah.desk = False
    hannah.hypnod = False
    hannah.hypnotize = False
    hannah.money = False
    hannah.relax = False
    hannah.responsibility = False
    hannah.romp = False
    hannah.spread = False
    hannah.strip = False
    bethany.school_torture_ask = False #note assigned to Bethany but used in this script during conversation before her school torture
  return

# Display Portrait
# CHARACTER: Display Portrait
label hannah_update_media:
  if hannah.has_tag('doll'):
    pass #because set in doll content
  elif hannah.has_tag('booty_call'):
    $ hannah.change_image('principal_booty_call_1_1')
  elif school.is_here:
    $ hannah.change_image('principal_office_2')
  else:
    pass
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label hannah_examine:
    if hannah.has_tag('doll'):
        "She used to be a public servant, devoted to her students and her school.  Now she serves you with a single-mindedness that exceeds mere devotion."
    else:
        if hannah.will_tamer_count == 1:
            "The principal of the local school.  You've used the Will-Tamer her on her one time."
        elif hannah.will_tamer_count > 1:
            "The principal of the local school.  You've used the Will-Tamer her on her [hannah.will_tamer_count.to_s] times."
        else:
            "The principal of the local school."
    return

## Character Specific Actions
# Doll Pose
label hannah_pose:
  player.c "Pose for me."
  $ hannah.change_image('principal_doll_2')
  wt_image principal_doll_2
  "The doll stands in front of you, awaiting further instructions."
  $ hannah.temporary_count = 1
  while hannah.temporary_count == 1:
    $ title = "How do you want her to pose?"
    menu:
      "Stand":
        $ hannah.change_image('principal_doll_3')
      "Bend over":
        $ hannah.change_image('principal_doll_9')
      "Show tits":
        $ hannah.change_image('principal_doll_4')
      "Show ass":
        $ hannah.change_image('principal_doll_5')
      "Show pussy":
        $ hannah.change_image('principal_doll_6')
      "Show tits and pussy":
        $ hannah.change_image('principal_doll_7')
      "Show asshole":
        $ hannah.change_image('principal_doll_34')
      "Against the wall":
        $ hannah.change_image('principal_doll_1')
      "Finished":
        "She'll hold her pose until you give her new instructions, then go back to leaning against the wall, as that seems to be her 'rest' mode."
        # note: replaced below as believe she will now hold her pose
        #"She'll hold her current pose for a while, then go back to leaning against the wall, as if she has a reset button you haven't been able to disable."
        $ hannah.temporary_count = 0
    wt_image hannah.image
  return

# Doll Clean
label hannah_clean:
  call forced_movement(living_room) from _call_forced_movement_965
  summon hannah no_follows
  wt_image principal_doll_23
  "Having the doll do the cleaning around the house isn't as much of a time saver as you would expect."
  wt_image principal_doll_25
  "Whether it's putting away the groceries ..."
  wt_image principal_doll_26
  "... washing the dishes ..."
  wt_image principal_doll_24
  "... or dusting the house ..."
  wt_image principal_doll_43
  "... the doll struggles to figure out how to clean properly without constant supervision."
  wt_image principal_doll_44
  "And when it gets completely sidetracked and you have to intervene to re-direct it ..."
  wt_image principal_doll_45
  "... the doll has a habit of interpreting your attention as a desire for more a more personal service."
  wt_image principal_doll_27
  "Not that that's a bad instinct for it to have."
  wt_image principal_doll_46
  "The doll may not be good at keeping your house clean, but it's good at decorating your home until it's time to put it back in the basement."
  call forced_movement(basement) from _call_forced_movement_966
  summon hannah no_follows
  $ hannah.change_image('principal_doll_1')
  return

# Doll Serve
label hannah_serve:
  player.c "Time to serve me."
  wt_image principal_doll_10
  hannah.c "Serve"
  player.c "That's right."
  $ title = "How do you want it to serve you?"
  menu:
    "Mouth":
      wt_image principal_doll_29
      "It's hard to tell if the doll experiences any emotions, but if it's ever happy, it's when it's sucking your cock."
      wt_image principal_doll_31
      "It sucks with an enthusiasm, dedication - even tenderness - that exceeds anything achieved by Hannah when she still had her brain."
      wt_image principal_doll_12
      "Perhaps its that single mindedness - the knowledge that this is what it is for - that makes the doll seem so content with its lips wrapped around your cock. You're pretty happy in this state too, especially knowing the doll will continue to eagerly suck your cock for as long you let it."
      wt_image principal_doll_30
      "Eventually, however, the burning in your balls becomes too much, and its time to decide where to cum."
      $ title = "Where do you want to cum?"
      menu:
        "Face":
          wt_image principal_doll_29
          "Hannah the School Principal was always reluctant to let you make a mess of her hair and make up by splattering your cum across them.  Hannah the Doll has no such concerns."
          wt_image principal_doll_13
          player.c "[player.orgasm_text]"
          $ hannah.facial_count += 1
        "Bib":
          wt_image principal_doll_32
          "The doll holds up its bib as you deposit your load on it."
          player.c "[player.orgasm_text]"
          wt_image principal_doll_14
          "The urge to clean up your sperm is instinctual.  You never have to show it what to do, it starts licking up your jizz as soon as you stop spurting."
          $ hannah.swallow_count += 1
        "Mouth":
          wt_image principal_doll_33
          "You deposit your load in the doll's waiting mouth."
          player.c "[player.orgasm_text]"
          wt_image principal_doll_15
          "It catches as much as it can, letting it pool on its tongue and back of its throat.  It'll stay like that, mouth open, until you tell it to swallow."
          $ hannah.swallow_count += 1
      $ title = "Do you want to piss?"
      menu:
        "That's what it's here for":
          "Its mouth is at crotch level and its only purpose is to serve.  There's no need to look for another toilet."
          wt_image principal_doll_16
          "*pppssssssssssssssss* ... You direct most of the warm, yellow liquid into its mouth, but allow a few streams to sprinkle across its face and breasts to watch it glisten against its skin."
          wt_image principal_doll_17
          "It'll have lots of time to clean itself up while it waits to serve you again."
        "No":
          pass
      $ hannah.blowjob_count += 1
      orgasm
    "Pussy":
      wt_image principal_doll_8
      "It raises its skirt ..."
      wt_image principal_doll_35
      "... and spreads itself open ..."
      wt_image principal_doll_18
      "... providing you easy access."
      wt_image principal_doll_19
      "It's not the most responsive fuck.  In fact, the stare on its expressionless face can be downright creepy.  Fortunately, its tit is still warm in your mouth and its insides are unnaturally wet as you fuck it, and that's enough to elicit an orgasm out of you."
      wt_image principal_doll_36
      player.c "[player.orgasm_text]"
      $ hannah.sex_count += 1
      orgasm
    "Ass":
      wt_image principal_doll_20
      "The doll's asshole has become permanently relaxed, providing easy access whenever desired."
      wt_image principal_doll_38
      "It's not quite like fucking a pussy, because there's no natural lubricant.  On the other hand, there's no need for artificial lubricants either, except to adjust the friction to the level you desire for your own pleasure."
      wt_image principal_doll_39
      "You can even adjust to let the doll do as much or as little of the work as you desire."
      wt_image principal_doll_37
      "Whether it's riding your cock or letting you pump into it at your own pace, the doll's expression barely changes. And if it feels your hot load spurting into its bowels, you'd never know."
      wt_image principal_doll_22
      player.c "[player.orgasm_text]"
      $ hannah.anal_count += 1
      orgasm
    "Toilet":
      player.c "Down"
      wt_image principal_doll_40
      "It squats at your feet, waiting to find out how it will serve."
      $ title = "What do you need to do?"
      menu:
        "Piss":
          wt_image principal_doll_15
          "It opens it's mouth as you take out your cock."
          wt_image principal_doll_16
          "*pppssssssssssssssss* ... You empty your bladder, mostly into it's mouth, but you direct a few streams over it's face to to watch it trickle down it's chin and over it's breasts."
          wt_image principal_doll_17
          "By the time you finish, your doll is a bit of a mess, but it'll instinctually clean itself up once you're finished."
        "Shit":
          wt_image principal_doll_41
          "As you turn around and lower your pants, it positions itself behind you and opens its mouth."
          wt_image principal_doll_42
          "It takes the doll a while to swallow the dump you deposit in it.  It's difficult to know if the look on it's face is residual disapproval from the woman it used to be at being treated like this, or if it's simply concentrating on digesting everything you gave it."
        "Nothing":
          pass
  $ hannah.change_image('principal_doll_1')
  return

# Doll Test
label hannah_test:
    $ title = "Which hole do you want to test?"
    menu:
        "Throat":
            wt_image principal_doll_test_mouth_1_1
            "The doll seems to find it perfectly normal to have a banana inserted in it's mouth."
            wt_image principal_doll_test_mouth_1_2
            "You wanted to know if it's throat is fully functional.  All indications are that it is."
            $ title = "Replace the banana with your cock?"
            menu:
                "Yes":
                    wt_image principal_doll_test_mouth_1_3
                    "If anything, it's even more normal to the doll when you remove the banana ..."
                    wt_image principal_doll_test_mouth_1_4
                    "... and replace it with your cock.  This is the type of service it expects to provide."
                    wt_image principal_doll_test_mouth_1_5
                    "The doll's throat is working perfectly, with no hint of gag reflex.  You just need to decide what to deposit in it."
                    $ title = "What do you deposit?"
                    menu:
                        "Cum":
                            wt_image principal_doll_test_mouth_1_6
                            "There's no risk of your cum spilling, but the doll makes instinctive, lapping motions with it's tongue against your balls as you empty your load down it's throat."
                            player.c "[player.orgasm_text]"
                            $ hannah.blowjob_count += 1
                            orgasm notify
                        "Piss":
                            wt_image principal_doll_test_mouth_1_7
                            "The doll makes instinctive, lapping motions with it's tongue as you empty your bladder down it's throat, preventing any piss from running back down your cock and ensuring it all ends up down the doll's throat, where it belongs."
                        "Both":
                            wt_image principal_doll_test_mouth_1_6
                            "There's no risk of your cum spilling, but the doll makes instinctive, lapping motions with it's tongue against your balls as you empty your load down it's throat."
                            player.c "[player.orgasm_text]"
                            wt_image principal_doll_test_mouth_1_7
                            "It laps even more urgently when you follow that up by emptying your bladder, this time to better effect as it prevents any piss from running back down your cock, ensuring it all ends up down the doll's throat, where it belongs."
                            $ hannah.blowjob_count += 1
                            orgasm notify
                "No":
                    pass
        "Vagina":
            wt_image principal_doll_test_pussy_1_1
            "The doll strips for it's examination ..."
            wt_image principal_doll_test_pussy_1_2
            "... then rolls into a more convenient position for you to explore it."
            wt_image principal_doll_test_pussy_1_3
            "The doll appears to be dry, but otherwise everything seems normal, externally."
            wt_image principal_doll_test_pussy_1_4
            $ title = "Check internal functionality?"
            menu:
                "Yes":
                    wt_image principal_doll_test_pussy_1_5
                    "The doll's sex moistens noticeably as you take out your cock.  Its ass also begins to open, reflecting possible uncertainty as to your attentions."
                    wt_image principal_doll_test_pussy_1_6
                    "You can test its anal functions another time.  For today, your probe confirms that not only is the doll moistening normally, it becomes downright soaked as soon as you enter it."
                    wt_image principal_doll_test_pussy_1_7
                    "Its also surprisingly warm inside, a pleasant sensation that helps you ignore the unnerving stare on its face as you use the doll's pussy to bring yourself to orgasm."
                    wt_image principal_doll_test_pussy_1_8
                    player.c "[player.orgasm_text]"
                    "The doll holds itself open as you cum on it, providing visual confirmation to what you've already ascertained: it's vagina is functioning as intended."
                    $ hannah.sex_count += 1
                    orgasm notify
                "No":
                    pass
        "Rectum":
            wt_image principal_doll_test_ass_1_1
            "Strictly speaking, you don't need to wet the inflatable rubber tube before sticking it up the doll's rectum."
            wt_image principal_doll_test_ass_1_2
            "The doll doesn't seem to care if you shove it in dry, it's just hard to get used to how accommodating the doll's rear hole has become, and how willing it's become to serve by offering all it's holes to you."
            wt_image principal_doll_test_ass_1_3
            "It's equally hard to get used to how no matter how big you pump the tube up, the doll's rectum will stretch as equal amount."
            $ title = "Put your dick up it's ass?"
            menu:
                "Yes":
                    wt_image principal_doll_test_ass_1_4
                    "It occurs to you that you've pumped the doll's asshole open so wide, it's almost too big for you."
                    wt_image principal_doll_test_ass_1_5
                    "Fortunately, the doll instinctively clamps down on your cock as you enter it, giving you a tight, warm hole to fuck until orgasm."
                    player.c "[player.orgasm_text]"
                    $ hannah.anal_count += 1
                    orgasm notify
                "No":
                    pass
    return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
# Contact - Pimp Principal Out
label hannah_contact_pimp:
  $ hannah.training_session()
  $ hannah.whore_count += 1
  if hannah.whore_count == 1:
    wt_image principal_office_19
    player.c "Good news, Hannah.  Your restoration of the school's finances is about to begin."
    hannah.c "You seem very pleased."
    player.c "Why wouldn't I be?  I'm helping you help your school, I'm helping the client have a good time. You will show the client a good time, won't you Hannah?"
    hannah.c "As long as he doesn't want me to do anything perverted."
    player.c "Keep an open mind about perversion, Hannah.  That might be your fastest route to financial security."
    player.c "But today's client isn't looking for anything perverted. He's a businessman in town for the week, staying at an upscale hotel.  He's looking for an attractive, sophisticated lady to show him a good time.  You can play that role, can't you Hannah?"
    wt_image principal_office_1
    "She bristles."
    hannah.c "I would hope so."
    player.c "I would hope so, too.  Try not to be as surly as you were when you were fucking me.  Not everybody gets off on the cranky bitch routine."
    hannah.c "Just tell me where to meet him, and when."
    player.c "I'll send you the details.  Oh, and your professional name is now 'Victoria'.  Unless you'd like something fun like 'Candy'?"
    wt_image principal_office_19
    hannah.c "Victoria is fine, but this isn't my profession.  I'm a teacher, not a whore."
    player.c "Just make him happy, Victoria."
    wt_image principal_whore_count_1_1
    "'Victoria' shows up for her client appointment in a better mood than she was when she fucked you.  Then again, he's not blackmailing her with the threat of financial ruin for her school.  Perhaps she sees him as part of the solution, not part of the problem?"
    hannah_whore_client_1 "{i}Please come in.{/i}"
    wt_image principal_whore_count_1_2
    "Hannah changes in the bathroom while the client waits.  He wanted a sophisticated, classy lady for the night, and that's what he's going to get ..."
    wt_image principal_whore_count_1_3
    "... complete with impeccable, understated lipstick that still screams 'let me suck you'."
    wt_image principal_whore_count_1_11
    hannah_whore_client_1 "{i}Wow.  You look amazing, Victoria.  Come, have a seat beside me and tell me all about you.{/i}"
    wt_image principal_whore_count_1_12
    hannah.c "{i}Oh, there's not much to tell, really.  What about you?  What brings you to town?{/i}"
    wt_image principal_whore_count_1_4
    "To her surprise, he's happy to talk.  They spend the next half hour chatting, and he tells her all about his background and his work ... nothing about his family life though, and she's careful not to pry."
    wt_image principal_whore_count_1_12
    "Eventually, he looks at his watch."
    wt_image principal_whore_count_1_11
    hannah_whore_client_1 "{i}I've really enjoyed our little chat, Victoria.  If you don't mind, I'd like to take you to the bed and fuck you now.{/i}"
    hannah.c "{i}Of course.{/i}"
    wt_image principal_whore_count_1_5
    "She follows him to the bedroom and lies down."
    wt_image principal_whore_count_1_6
    "He pulls her towards him and lifts her leg, and she thinks he's going to enter her missionary style ..."
    wt_image principal_whore_count_1_13
    "... when he flips her over ..."
    wt_image principal_whore_count_1_14
    "... and starts ramming into her doggy style."
    wt_image principal_whore_count_1_7
    "You'd advised her to apply lubricant before her visit.  Despite the lube, she still grimaces and bites her lip at the speed and force of his entry and the enthusiasm of his fucking, as his ardor is well ahead of her body's response to it."
    wt_image principal_whore_count_1_13
    "The fucking doesn't last long.  Almost as soon as it starts, he pulls out."
    hannah_whore_client_1 "Turn around, please."
    wt_image principal_whore_count_1_15
    hannah_whore_client_1 "{i}Face, hair or mouth.  Which do you prefer?{/i}"
    hannah.c "{i}Mouth?{/i}"
    hannah_whore_client_1 "{i}Open up.{/i}"
    wt_image principal_whore_count_1_8
    "As she does, he fills it with his seed."
    hannah_whore_client_1 "{i}Ooohhhhhhh{/i}"
    wt_image principal_whore_count_1_9
    hannah_whore_client_1 "{i}You are one classy, sexy lady, Victoria.  Thanks for coming to visit me.{/i}"
    wt_image principal_whore_count_1_16
    "After she rinses our her mouth, she dresses.  Then she checks in with you as you instructed."
    wt_image principal_whore_count_1_10
    player.c "How did it go?  Did he want anything 'perverted'?"
    hannah.c "Not at all.  He was a perfect gentleman."
    player.c "Did you get your money?"
    hannah.c "Yes"
    player.c "50 of that is mine."
    hannah.c "No, 30.  This is a fund raising operation, remember?  The school needs this money more than you.  I'll cover your costs, nothing more.  I'll send your cut to you by the end of the week."
    $ player.whore_income += 30
  elif hannah.whore_count == 2:
    wt_image principal_face_5
    player.c "I have a new client for you, Hannah."
    hannah.c "Do you know what he wants?"
    player.c "Nothing perverted.  Just the normal suck, fuck and anal."
    hannah.c "Anal?  Should I charge more for that?"
    player.c "It depends.  Is there anything special about your ass?"
    wt_image principal_face_9
    hannah.c "What do you mean?  I have a normal ass, I think."
    player.c "Then a normal fee would seem appropriate.  I'll send you his address."
    wt_image principal_whore_count_2_15
    "'Victoria' arrives punctually at the client's house."
    hannah_whore_client_2 "{i}Mmmm, change into something sexy for me, will you sweetheart?{/i}"
    wt_image principal_whore_count_2_1
    hannah.c "{i}Of course.{/i}"
    wt_image principal_whore_count_2_16
    "She ducks into the client's bathroom, returning a few minutes later dressed in classy yet slutty lingerie, to her client's obvious satisfaction."
    wt_image principal_whore_count_2_2
    hannah_whore_client_2 "{i}My, you are a sexy one, aren't you?{/i}"
    hannah.c "{i}I'm glad you think so.{/i}"
    wt_image principal_whore_count_2_3
    hannah_whore_client_2 "{i}I do. Got some nice booty on you, too.  Daddy likes that.  I'm going to have some fun with that later.  You cool with that?{/i}"
    hannah.c "{i}I ... I guess.{/i}"
    wt_image principal_whore_count_2_16
    hannah_whore_client_2 "{i}Don't you worry, pretty mama.  Daddy'll be real careful with you.  I've always got to be careful with the ladies, 'cus, you know, I'm swinging a pretty big load down there.  Why don't you take me out and have a look?{/i}"
    wt_image principal_whore_count_2_17
    hannah.c "{i}Woah!{/i}"
    hannah_whore_client_2 "{i}Yeah, I know.  It's a little intimidating at first.  Start with my balls.  They're normal size.  Give them a good suckle.{/i}"
    wt_image principal_whore_count_2_4
    hannah_whore_client_2 "{i}Mmmmm, that's nice.  Yeah, run your tongue all over them, just like that.  That makes Daddy feel real good.{/i}"
    wt_image principal_whore_count_2_5
    hannah_whore_client_2 "{i}Time to play a little game.  Let's see how much of Daddy you can get inside that hot sexy mouth of yours?{/i}"
    wt_image principal_whore_count_2_18
    hannah_whore_client_2 "{i}Don't be nervous, pretty lady.  Take your time and look at me while you swallow Daddy.  There's no rush.  We got all day.{/i}"
    wt_image principal_whore_count_2_6
    hannah_whore_client_2 "{i}That's it, you're doing real good.  That's as far as most ladies can go on Daddy.{/i}"
    wt_image principal_whore_count_2_7
    "Hannah's never been happy doing only as well as 'most' other people.  Closing her eyes and concentrating hard on controlling her gag reflex, she wills the back of her throat to relax and slides further onto her client's hard shaft.  When she feels his balls against her chin, she opens her eyes again."
    hannah_whore_client_2 "{i}Mmmmmm mmmmmm.  You are one special, sexy mama!  If I hadn't seen how fine that ass of yours was, I'd stay right here and let you give Daddy some tender loving care with this amazing mouth of yours.{/i}"
    wt_image principal_whore_count_2_19
    hannah_whore_client_2 "{i}But I got to get to know the rest of you better.  Climb on up here and let me give you a reward for doing such a good job at swallowing Daddy.{/i}"
    wt_image principal_whore_count_2_8
    "Hannah lubed herself up before coming over, but finds to her surprise that she needn't have worried.  Her body is responding to today's client, and she feels a little tremor of pleasure pass through her as she slides onto his long, hard cock."
    hannah.c "{i}ooohhh{/i}"
    hannah_whore_client_2 "{i}Yeah, that feels real good to Daddy, too.  But that's just a little treat for being such a good girl and taking Daddy up to your chin.  It's this big white booty of yours that Daddy's gotta tap.{/i}"
    wt_image principal_whore_count_2_20
    hannah_whore_client_2 "{i}Turn around and let's see if your ass can give Daddy as nice a home as your mouth did.{/i}"
    wt_image principal_whore_count_2_9
    hannah.c "{i}I don't know ... You're so big.{/i}"
    wt_image principal_whore_count_2_10
    hannah_whore_client_2 "{i}Daddy's just long, I'm not too wide for you.  Lots of ladies have taken Daddy all the way up their poop hole.  Just relax.  I'm not going to hurt you. We're going to take this nice and slow.{/i}"
    "Her body's arousal can't help her prepare for this penetration. Fortunately, the client uses a generous amount of lube, and true to his word, he takes his time, placing firm and steady pressure on her rosebud, not forcing things."
    wt_image principal_whore_count_2_11
    "When she feels her sphincter relax enough for the head of his cock to pass it, Hannah gasps in surprise, and maybe just a bit of pleasure."
    hannah.c "{i}Ooohhh!!{/i}"
    hannah_whore_client_2 "{i}There you go, pretty lady.  You're ready for Daddy now.  Going to put all of me up you now.{/i}"
    wt_image principal_whore_count_2_21
    hannah_whore_client_2 "{i}Feels good, doesn't it, felling Daddy's long snake going deeper and deeper inside you?{/i}"
    hannah.c "{i}Y ... yes?{/i}"
    wt_image principal_whore_count_2_23
    hannah_whore_client_2 "{i}Sure it does.  You don't need to be bashful.  It's just you and I here.  It feels good taking Daddy's long cock up your poop hole.  Makes you feel like a slutty little whore, don't it?{/i}"
    wt_image principal_whore_count_2_12
    hannah_whore_client_2 "{i}Come on, don't be shy.  You got all of Daddy up your butt now, there's no need to act coy.  Tell the Daddy the truth.  You like taking Daddy's hard cock in your ass like a slutty whore, don't you?{/i}"
    hannah.c "{i}Yes{/i}"
    wt_image principal_whore_count_2_22
    hannah_whore_client_2 "{i}There you go!  Nothing to be ashamed of.  You and I can have some fun now.  Climb back on top of me tell Daddy where you want his cock?{/i}"
    hannah.c "{i}I want it up my ass.  Put your long cock back up my ass, Daddy!{/i}"
    wt_image principal_whore_count_2_13
    hannah_whore_client_2 "{i}Get on up here and give Daddy a good ride.  Go ahead, play with your little clitty while you're riding me.  That's it!  Give your little man a good rub down while you ride Daddy's hard cock.{/i}"
    hannah.c "{i}Oh oohhh oooohh FUUCCCKKK!{/i}"
    hannah_whore_client_2 "{i}Mmmmm ... yeaahhhh ... Aaaahhhhhh!!!!  You are one hot sexy lady.{/i}"
    wt_image principal_whore_count_2_24
    "A hot sexy lady now complete with a load of her client's cum in her ass and a beet red face as she realizes she just came from anal sex with a total stranger ... and that she's reluctant to get off his dick."
    wt_image principal_whore_count_2_15
    "Hannah checks in with you again before heading home."
    player.c "How did it go?  Did you have fun?"
    wt_image principal_whore_count_2_14
    hannah.c "What do you mean?  Why would you ask me that?  It was a job, that's all."
    player.c "A job, huh, not a fund raiser?  Handled professionally I'm sure."
    wt_image principal_whore_count_2_1
    hannah.c "You know what I mean!  I'll send you your cut later."
    "From the bright red blush that crosses her face, you're not exactly sure what she means, and she seems to be in no mood to fill you in on what happened."
    $ player.whore_income += 30
  elif hannah.whore_count == 3:
    wt_image principal_face_10
    player.c "I have another client for 'Victoria'. He wants you to meet him at his house."
    wt_image principal_face_11
    hannah.c "Can you send me the directions?"
    player.c "Sending them now."
    "If you didn't know better, you'd think she sounded excited about her upcoming 'date'."
    wt_image principal_face_11
    "She cleans herself up and arrives promptly for her appointment."
    hannah_whore_client_3 "{i}Please come in, Victoria.  The bedroom's right in there. Make yourself at home.{/i}"
    wt_image principal_whore_count_3_18
    "The client doesn't seem to be interested in small talk, so 'Victoria' changes into the new lingerie she brought ..."
    wt_image principal_whore_count_3_1
    "... then lies down on the bed that the client has romantically strewn with flowers."
    wt_image principal_whore_count_3_19
    hannah.c "{i}Okay, I'm ready.{/i}"
    wt_image principal_whore_count_3_2
    hannah_whore_client_3 "{i}Wow ... you look really good!{/i}"
    wt_image principal_whore_count_3_20
    hannah.c "{i}Thank you.  That's sweet of you to say.{/i}"
    wt_image principal_whore_count_3_21
    hannah_whore_client_3 "{i}And you're so soft.{/i}"
    wt_image principal_whore_count_3_3
    "'Victoria' purrs as he strokes his hand along her sex."
    hannah.c "{i}Mmmmhhhh{/i}"
    wt_image principal_whore_count_3_4
    hannah_whore_client_3 "{i}Do you like having your clit played with?{/i}"
    hannah.c "{i}Mmmhhhh ... yes.{/i}"
    wt_image principal_whore_count_3_5
    hannah_whore_client_3 "{i}And do you like having your pussy finger fucked?{/i}"
    hannah.c "{i}Ohhhh yes!{/i}"
    wt_image principal_whore_count_3_6
    hannah_whore_client_3 "{i}You're quite the responsive whore, aren't you Victoria? ... or should I say, Hannah?{/i}"
    hannah.c "{i}Wait ... what?{/i}"
    wt_image principal_whore_count_3_22
    hannah_whore_client_3 "{i}Don't play innocent with me, I have your pussy juice all over my fingers.  Here, taste.  I would never have guessed you were such a slut.{/i}"
    wt_image principal_whore_count_3_7
    hannah_whore_client_3 "{i}You don't remember me.  There's no reason you should. I only came to one school function, and sat in the audience during my son's recital you MC'd.  My wife went to all the parent teacher nights.{/i}"
    wt_image principal_whore_count_3_8
    "Grabbing her by the hair, he pulls her head to the side of the bed."
    hannah_whore_client_3 "{i}But I remember you.  I remember how hot you looked in your buttoned up conservative suit.  I spent half the recital wondering if you sucked cock like a repressed cocktease or a wanton slut?  I guess now I get to find out.{/i}"
    wt_image principal_whore_count_3_23
    hannah_whore_client_3 "{i}Oh, don't look so scared. Your secret's safe with me.{/i}"
    wt_image principal_whore_count_3_9
    hannah_whore_client_3 "{i}I can't exactly go around telling the world that my son's Principal is a dirty whore, without also admitting that I'm having whores over to my house to fuck while my wife and son are away visiting her parents.{/i}"
    wt_image principal_whore_count_3_24
    hannah_whore_client_3 "{i}On the other hand, you can't exactly complain if I rough you up a bit, either.  Not unless you want to explain to the cops why you're turning tricks.{/i}"
    wt_image principal_whore_count_3_25
    "Hannah groans into the jammed into her mouth as he spanks her ... *SMACK* *SMACK* *SMACK*"
    hannah.c "{i}nnnnnnn{/i}"
    wt_image principal_whore_count_3_26
    hannah_whore_client_3 "{i}That's enough fun for you.  Put that dirty whore mouth of yours to work sucking my cock, Principal Hannah.{/i}"
    wt_image principal_whore_count_3_27
    hannah_whore_client_3 "{i}Do a good job and I might even stop wondering about whether your ass is as tight as I pictured it when you were up there on the school stage.{/i}"
    wt_image principal_whore_count_3_10
    hannah_whore_client_3 "{i}Your ass really is tight.  I can barely get a finger in there.{/i}"
    wt_image principal_whore_count_3_11
    hannah_whore_client_3 "{i}Feel how it's gripping my finger?  That's nice.{/i}"
    wt_image principal_whore_count_3_28
    hannah_whore_client_3 "{i}You don't mind if I replace my finger with my cock, do you Hannah?  I mean considering that I've bought and paid for you for the hour like the dirty whore you are, I'm sure you know there are worse things I could make you do than take my cock up your shitter.{/i}"
    wt_image principal_whore_count_3_12
    hannah_whore_client_3 "{i}Mmpphhhh ... there you go.  You take cock in your ass like a pro, you know that?  Which I guess isn't surprising, since you are a pro.  Do you like it like this?  Do you like having a hard cock shoved up your ass?{/i}"
    wt_image principal_whore_count_3_13
    hannah_whore_client_3 "{i}Going all sullen and silent are you?  That's okay.  I'll tell you what I like.{/i}"
    wt_image principal_whore_count_3_14
    "*slap*"
    hannah.c "{i}Owww!{/i}"
    wt_image principal_whore_count_3_29
    hannah_whore_client_3 "{i}I like slapping a bitch's face while I fuck her in the ass.{/i}"
    wt_image principal_whore_count_3_14
    "*slap*"
    hannah.c "{i}Owww!{/i}"
    wt_image principal_whore_count_3_29
    hannah_whore_client_3 "{i}Go on, bitch.  Tell me that you like it.{/i}"
    wt_image principal_whore_count_3_14
    "*slap*"
    wt_image principal_whore_count_3_15
    hannah.c "{i}I do.  I love it.  You're a big, strong, powerful man and I'm just your little dirty whore.  Fuck me like a real man.  Fill this dirty whore with your cum.{/i}"
    hannah_whore_client_3 "{i}Ohhhh yeah.  Now you're talking.  Get on your knees, whore.{/i}"
    wt_image principal_whore_count_3_30
    hannah_whore_client_3 "{i}Uggghhhhh{/i}"
    "His cum streaks Hannah's face as she kneels in front of him."
    wt_image principal_whore_count_3_31
    hannah_whore_client_3 "{i}Clean me off, bitch.{/i}"
    hannah.c "{i}But ...{/i}"
    wt_image principal_whore_count_3_32
    hannah_whore_client_3 "{i}Yes, my cock was up your dirty whore butt.  Open your whore mouth and clean me off.{/i}"
    wt_image principal_whore_count_3_16
    hannah_whore_client_3 "{i}You look pretty good like that.  You should go to school wearing that look.{/i}"
    wt_image principal_whore_count_3_17
    hannah.c "{i}Just get me my money.{/i}"
    hannah_whore_client_3 "{i}What, no sense of humor?  Hold your horses, I'll get you your money.  I'm an asshole, not a cheat.{/i}"
    wt_image principal_face_11
    hannah.c "Time for a change of plans."
    player.c "Is everything all right?  Was there a problem?"
    hannah.c "No problem.  Nothing I couldn't handle anyway.  Today's client just made me realize that I can handle this now, and I don't need you.  Not to set up clients for me at any rate.  Victoria's getting lots of interest online, and I can screen new clients myself."
    hannah.c "I'll keep paying you a share, for the infrastructure you set up, but after tonight I'm cutting your fee in half."
    player.c "You've already cut my fee."
    hannah.c "The less for you, the more for the school.  Be happy I'm not cutting you out altogether."
    player.c "Why aren't you?"
    hannah.c "Because somehow I get the sense that if I actually needed you, you'd be there to help me out.  Physically."
    player.c "I'd like to think you were talking about me getting you off, but I'm guessing you're thinking more in the lines of muscle."
    hannah.c "I knew you weren't as stupid as you usually look."
    $ hannah.whore_lost_countdown = 8
    $ player.whore_income += 15
  change player energy by -energy_short notify
  return

# Contact - Arrange Session for Mistress Hannah
label hannah_contact_domme:
  if hannah.has_tag('domme'):
    $ hannah.training_session()
    $ hannah.domme_outfit_count += 1
    change player energy by -energy_short
  else:
    wt_image principal_face_4
    if player.has_tag('club_access'):
      hannah.c "Have you found a place where I could work yet?  Some place that isn't going to cut into the money I raise for the kids?"
      player.c "I have. I can get you access on an as-needs basis to our local Club.  It's fully equipped, so you'll have access to everything you need to 'entertain' properly."
      player.c "They don't normally allow professionals to use the Club, but when I explain that it's really a school fundraiser, I'm sure they'll give you access for a reasonable fee."
      wt_image principal_face_3
      hannah.c "Okay. I'll try it. But if it cuts into the quality of the work I can do for the school or the children, I'm stopping. Understood?"
      player.c "Yes, Ma'am.  I'll set things up for you."
      hannah.c "Give me a few days.  I need to mentally prepare myself for this."
      $ hannah.training_session()
      call convert(hannah, "domme") from _call_convert_17
    else:
      hannah.c "Have you found a place where I could work yet?  Some place that isn't going to cut into the money I raise for the kids?"
      player.c "Not yet, but I'll keep you posted."
  if hannah.domme_outfit_count == 1:
    wt_image principal_face_2
    player.c "Ready to start your career as a Professional Domme?"
    wt_image principal_face_1
    hannah.c "Amateur Domme.  My profession is teaching.  I'm just doing this to raise more money for the school."
    player.c "Of course, Mistress.  I have your first client lined up.  I'll meet you at the Club."
    wt_image principal_face_2
    hannah.c "Okay"
    call forced_movement(club) from _call_forced_movement_967
    summon hannah to club
    wt_image principal_domme_outfit_1_1
    "Hannah is waiting when you arrive with her client.  She's changed into a frilly outfit that's a bit over-the-top, but she can carry it off."
    wt_image principal_domme_outfit_1_7
    hannah.c "So this is the degenerate worm who wants my attention?  What do you want from me, worm?"
    hannah_domme_client_1 "Please let me worship you, Mistress.  You're right, I am a worthless worm, fit only to suffer and serve you."
    wt_image principal_domme_outfit_1_8
    hannah.c "Get your clothes off. I didn't give you permission to be dressed in my presence."
    wt_image principal_domme_outfit_1_9
    "Hannah doesn't seem to require much assistance in taking on the Domme role. Either it comes natural at it, or she's done her research, or both. You do help her with the rope work on her client, helping her put him in a chest harness in a relatively quick and efficient fashion ..."
    wt_image principal_domme_outfit_1_4
    "... but the cock trap she found in the Club's supplies, she's comfortable applying herself."
    wt_image principal_domme_outfit_1_11
    "After that, you can step back and observe, as she's running this show, and she doesn't mind letting you or the client know it."
    wt_image principal_domme_outfit_1_12
    hannah.c "You want to serve?  Show me.  Lick my shoes.  Show me you know your proper place, you sick little worm."
    wt_image principal_domme_outfit_1_2
    hannah_domme_client_1 "Yes, Mistress.  Thank you, Mistress."
    wt_image principal_domme_outfit_1_13
    hannah.c "Now my feet.  I've been on my feet in heels all day, and they're sore and tired and sweaty.  Do you like the taste of Mistress' smelly feet?."
    wt_image principal_domme_outfit_1_3
    hannah_domme_client_1 "Yes, Mistress. Thank you, Mistress, for letting me taste them."
    wt_image principal_domme_outfit_1_14
    hannah.c "Shut up and lick, worm."
    wt_image principal_domme_outfit_1_15
    hannah.c "Your tongue is boring me, worm. Perhaps I'll be able to have more fun with we have you locked into this interesting contraption.  Come over here and make yourself useful and help me to get him in position."
    wt_image principal_domme_outfit_1_16
    "You finish locking her client in place while Hannah gags him."
    hannah.c "Can you guess why I put you in that ballgag?"
    wt_image principal_domme_outfit_1_17
    "Her client nods vigorously."
    hannah.c "You can?  You're such a smart, pathetic worm.  Does that excite you?  Knowing that I'm about to hurt you?"
    wt_image principal_domme_outfit_1_18
    "Her client nods again as Hannah picks up a cane."
    hannah.c "Let's see if you can amuse me with your pain, worm.  You have my permission to make as much sound as that gag allows."
    wt_image principal_domme_outfit_1_19
    "You try to help Hannah again, this time to figure out where and how to strike her client to cause pain without injuring him ..."
    wt_image principal_domme_outfit_1_20
    "... but it turns out she used to teach anatomy, and she already has a firm grasp of that subject ... *thwaapp*"
    hannah_domme_client_1 "Urrggh"
    wt_image principal_domme_outfit_1_21
    "Time and gain she whips the cane hard against his innher thighs ... *thwaapp*"
    hannah_domme_client_1 "Urrgghhh!!!"
    wt_image principal_domme_outfit_1_22
    "*thwapp*"
    hannah_domme_client_1 "URRGGHHH"
    wt_image principal_domme_outfit_1_6
    "*thwappp*"
    hannah_domme_client_1 "URRGGHHHH!!!!"
    wt_image principal_domme_outfit_1_16
    hannah.c "Those are nice sounds, worm, but not exactly what I wanted to hear.  Those are screams of pain.  I want to hear screams of sheer agony and terror."
    wt_image principal_domme_outfit_1_19
    hannah.c "Do you think you can guess how I'll be able to get you to scream like that, worm?"
    "He starts panting hard and straining against his bonds."
    wt_image principal_domme_outfit_1_23
    hannah_domme_client_1 "You can guess, can't you?"
    "Gently she rubs his bound balls with the cane ... "
    wt_image principal_domme_outfit_1_5
    "... then pulls the cane back.  He breaks out in tears, sobbing before the cane even hits him."
    hannah_domme_client_1 "Nnn Nnn Nnn"
    wt_image principal_domme_outfit_1_23
    "*thwaappp*"
    hannah_domme_client_1 "UUUUUURRRRGGGGHHHHHH!!!!!!!!"
    wt_image principal_domme_outfit_1_21
    "Without the gag, his screams would have been loud enough to disturb the whole Club, but you can tell Hannah wants to hear more.  You get up and place your hand over his mouth, stifling his screams even more as she alternates between beating his thighs and beating his balls."
    "*thwaappp*"
    hannah_domme_client_1 "eerrrgggghh"
    "*thwaappp*"
    hannah_domme_client_1 "eerrrrrgggggghggh"
    "*thwaappp*"
    hannah_domme_client_1 "eerrrrrgggggghggh!!!"
    "*thwaappp*"
    hannah_domme_client_1 "eerrrrrgggggghggh!!!!!"
    wt_image principal_domme_outfit_1_15
    "Eventually Hannah stops, and you help her untie her client. As he dresses, you offer her some advice."
    wt_image principal_domme_outfit_1_7
    player.c "You may want to tone the sadism down a bit, at least until you get to know the client better.  Mix some sexual humiliation in instead, unless he specifically asks for something different."
    hannah.c "He told me he wanted to suffer."
    player.c "I know, but you should check in on his definition of suffering, to make sure its similar to yours."
    wt_image principal_domme_outfit_1_8
    "The client comes back, now dressed."
    hannah_domme_client_1 "Thank you, Mistress."
    "He hands over his payment and leaves."
    wt_image principal_domme_outfit_1_1
    player.c "50 of that is mine."
    hannah.c "20. This is a fund raising operation, remember?  That's what you told the Club to get us access to their facilities, and I'm turning my profits over to the school.  You can do the same.  I'll let you keep your costs."
    $ player.domme_income += 20
    call forced_movement(living_room) from _call_forced_movement_968
    call character_location_return(hannah) from _call_character_location_return_674
  elif hannah.domme_outfit_count == 2:
    wt_image principal_face_3
    player.c "I have your next client lined up. He watched some of your fund raiser reviews, and he specifically asked for electricity play."
    hannah.c "I'll bring some of my equipment to the Club."
    call forced_movement(club) from _call_forced_movement_969
    summon hannah to club
    wt_image principal_domme_outfit_2_9
    "Mistress Hannah is a little more down dressed today, greeting you and her new client wearing a more classic Dominatrix look."
    wt_image principal_domme_outfit_2_1
    hannah.c "Come in and remove your clothes."
    wt_image principal_domme_outfit_2_10
    "Hannah says nothing when he returns to her, still wearing his underwear.  She ties him in a standing spreadeagle position ..."
    wt_image principal_domme_outfit_2_11
    "... then once he's helpless, cuts a hole in his underwear and wraps a rope around his cock and balls, binding them firmly to the floor as he winces in pain."
    wt_image principal_domme_outfit_2_12
    hannah.c "Does that feel nice?  Do you like what Mistress has done with your cock?"
    hannah_domme_client_2 "Ye .. yes, Mistress."
    wt_image principal_domme_outfit_2_13
    hannah.c "It hurts of course, and will hurt more as I tighten up this rope tugging on your balls."
    hannah_domme_client_2 "Aawwwww!"
    wt_image principal_domme_outfit_2_15
    hannah.c "You don't mind that, do you, you pathetic worm?  I like watching you hurt, and you don't mind me having some fun causing you pain, do you?"
    hannah_domme_client_2 "N .. n .. no, Mistress."
    wt_image principal_domme_outfit_2_14
    hannah.c "That's good.  I'm glad we're on the same page.  I understand you want to help me have some fun with electricity?  Is that true?"
    hannah_domme_client_2 "Yes, Mistress."
    wt_image principal_domme_outfit_2_16
    hannah.c "Let me just hook these electrodes up."
    wt_image principal_domme_outfit_2_4
    hannah.c "There.  Are your balls still hurting?"
    hannah_domme_client_2 "Ye .. yes Mistress."
    wt_image principal_domme_outfit_2_17
    hannah.c "Good.  Now watch what happens now."
    "*zzzzttttt*"
    wt_image principal_domme_outfit_2_4
    hannah_domme_client_2 "Urrgghhh AAWWWW!!!"
    hannah.c "Isn't that fun?  If you tense up when the electricity hits, you're going to pull on your balls.  So try to relax when the jolts hit you."
    wt_image principal_domme_outfit_2_18
    hannah.c "Oh, one more thing.  Each jolt is going to be a little stronger than the last."
    "*zzzzttttt*"
    hannah_domme_client_2 "Uuurrrrgghhh"
    wt_image principal_domme_outfit_2_19
    "*zzzzttttt*"
    hannah_domme_client_2 "UURRGHH AAWWWW!!!"
    wt_image principal_domme_outfit_2_2
    "*zzzzttttt*"
    hannah_domme_client_2 "URRRGGHHH!!!! AAAWWWWW!!!"
    wt_image principal_domme_outfit_2_20
    hannah.c "As fun as this is, I think we'd better stop with the electricity for now.  I don't know your medical history, and we don't want to overdo it."
    wt_image principal_domme_outfit_2_21
    hannah.c "Fortunately, there are other fun ways I can hurt you."
    "Mistress Hannah slips a blindfold over his eyes ..."
    wt_image principal_domme_outfit_2_22
    "... then attaches clothes pins across his body ..."
    hannah_domme_client_2 "Nnnnnnn"
    wt_image principal_domme_outfit_2_3
    "... including his cock and balls."
    hannah_domme_client_2 "AAWWW!!"
    wt_image principal_domme_outfit_2_23
    "Then she starts circling him, striking him with the flogger as she goes ... *thwackkk*"
    hannah_domme_client_2 "URRGHH!"
    wt_image principal_domme_outfit_2_5
    "Unable to see where she is or where the next blow is coming from, her client can only wait, trying not to move too much when the blow lands, for fear of inflicting even more pain on his stretched testicles ... *thwackkk*"
    hannah_domme_client_2 "URRRGHH!!!  AAWWW!!"
    wt_image principal_domme_outfit_2_24
    "*thwackkk*"
    hannah_domme_client_2 "URRRGGHH!!!  AAAAWWW!!!!"
    wt_image principal_domme_outfit_2_25
    hannah.c "My assistant tells me I need to be careful not to be too sadistic.  Do you think you've had enough pain for now?"
    "The client can't seem to verbalize an answer, but nods his head vigorously."
    wt_image principal_domme_outfit_2_34
    "Hannah lets him down ..."
    wt_image principal_domme_outfit_2_6
    "... then shoves a strap on dildo into his mouth."
    hannah.c "Get this nice and wet for me.  You may think you've had enough pain, but I have a bit more planned for you."
    wt_image principal_domme_outfit_2_26
    "Once soaking wet, the dildo is replaced with a ball gag ..."
    wt_image principal_domme_outfit_2_27
    "... then Mistress Hannah straps him into position ..."
    wt_image principal_domme_outfit_2_28
    "... and re-attaches the rope to his balls, adding weights to them."
    hannah_domme_client_2 "NNNNNNNNNN!!!"
    wt_image principal_domme_outfit_2_29
    hannah.c "Your balls are really hurting now, aren't they, you pathetic worm?"
    "He nods frantically."
    wt_image principal_domme_outfit_2_30
    hannah.c "Better hold yourself still,then.  I'm going to fuck your ass, and if you let me get you rocking back and forth, you know where you're going to feel it, don't you?"
    wt_image principal_domme_outfit_2_8
    "The sound of panic from behind his ball gag is soon replaced by the sound of full throated screams as Mistress Hannah shoves the strap on inside him and starts riding his ass."
    hannah_domme_client_2 "NNNNNNN!!   NNNNNNN!!!   NNNNNNN!!!!!"
    wt_image principal_domme_outfit_2_31
    hannah.c "That's it.  Squeal like a stuck pig for me.  You'd like to use your ass and your tears to get Mistress off, wouldn't you?"
    wt_image principal_domme_outfit_2_32
    "You're not sure Hannah actually cums while fucking his ass, but then you're not sure she doesn't either.  What is certain is that she pounds into him as enthusiastically as any groom ever fucked his bride on their wedding night, and for longer than most grooms would be able to last."
    wt_image principal_domme_outfit_2_33
    "When she's finally had her fill of fun, Hannah lets her shaking and trembling client up and sends him to get dressed."
    wt_image principal_domme_outfit_2_35
    "He returns a few minutes later, seemingly none the worse for wear.  After she collects her fee and shows the client out, she turns to look at you."
    hannah.c "How was that?  Any better?"
    player.c "Moving in the right direction.  Try to remember: more humiliation, a little less pure torture, unless you're dealing with a true masochist."
    wt_image principal_domme_outfit_2_36
    player.c "It's good that you're really getting into it, though.  Clients will pick up on that, and enjoy their sessions more."
    hannah.c "I'm not sure what you're talking about.  I'm only doing this to raise money for the school, remember?"
    player.c "Of course, Mistress.  Whatever you say."
    $ player.domme_income += 20
    call forced_movement(living_room) from _call_forced_movement_970
    call character_location_return(hannah) from _call_character_location_return_675
  elif hannah.domme_outfit_count == 3:
    wt_image principal_face_5
    player.c "I have another client for you. He's asked if you could visit him at his office."
    hannah.c "Should I go alone?"
    player.c "That's up to you.  I told him I might be there with you."
    wt_image principal_face_9
    hannah.c "It'd be best if you come with me.  I'm a bit nervous about meeting someone I don't know all alone at his office.  I remember what you did to me when you got me in that position."
    wt_image principal_domme_outfit_3_1
    "She need not have worried. Her client is a pleasant, unassuming fellow who greets you both happily at the door."
    hannah_domme_client_3 "Hello, Mistress. Thank you for coming to visit me."
    wt_image principal_domme_outfit_3_13
    hannah.c "You should thank me.  It's not often I take time out of my busy day to visit sniveling little worms like you."
    wt_image principal_domme_outfit_3_2
    hannah.c "Is that a hard on you're sporting already?"
    hannah_domme_client_3 "Yes, Mistress."
    wt_image principal_domme_outfit_3_3
    hannah.c "Don't start getting any ideas, worm.  I'm not interested in that little thing in your pants.  I'm here to have you serve me, assuming I can find a use for a sniveling worm like you.  Do you have a problem with that?"
    hannah_domme_client_3 "No, Mistress.  Thank you, Mistress."
    wt_image principal_domme_outfit_3_14
    hannah.c "Besides, what good would a little worm dick like yours be to me?"
    hannah_domme_client_3 "None, Mistress."
    wt_image principal_domme_outfit_3_15
    hannah.c "I think the only way a tiny-dicked worm like you could please me would be by suffering for me.  Do you like to suffer, worm?"
    hannah_domme_client_3 "Yeth, Mithress.  If that pleathees you."
    wt_image principal_domme_outfit_3_4
    hannah.c "Does it hurt when I squeeze your silly little man tits?"
    hannah_domme_client_3 "Aaagghh  ... Yes, yes it does Mistress."
    wt_image principal_domme_outfit_3_16
    hannah.c "How about when I squeeze these ridiculous balls of yours?"
    hannah_domme_client_3 "AAAGGHH"
    wt_image principal_domme_outfit_3_5
    hannah.c "Still sporting a hard on, I see.  Do you think I'm impressed by that?"
    hannah_domme_client_3 "N ..."
    wt_image principal_domme_outfit_3_15
    hannah.c "Shut up worm, I don't want to listen to you after all."
    wt_image principal_domme_outfit_3_6
    hannah.c "There.  That's dealt with that silly little hard on.  What do you think Mistress should do to you now, now that I've got you focused on me and no longer thinking about your own pleasure?"
    "He hesitates, uncertain as to whether to reply or not."
    hannah.c "Go ahead, worm.  Spit it out."
    hannah_domme_client_3 "Whatever you want to do to me, Mistress."
    hannah.c "Good answer, worm."
    wt_image principal_domme_outfit_3_17
    "With a single, smooth motion, she kicks him hard on his exposed balls while shoving her fingers in his mouth to stifle his cry."
    hannah_domme_client_3 "NNNNNNNNNN!!!!!"
    hannah.c "You know how to scream.  Good.  If I get bored of using you in other ways, I can always just listen to you scream for the rest of our session.  But for now, shut up before your receptionist wonders what we're up to in here.  Unless you want her to see you like this?"
    "He shakes his head 'no' as best he can with Hannah's hand in his mouth."
    wt_image principal_domme_outfit_3_18
    hannah.c "Well today's your lucky day, worm.  I'm going to give you an opportunity to please me in other ways.  Do a good job and I might not feel like hurting you much more."
    wt_image principal_domme_outfit_3_7
    hannah.c "That's it, worm.  Stick your tongue all the way up inside Mistress' ass."
    wt_image principal_domme_outfit_3_19
    "This is a new element in Hannah's routine, but what she does next is even more out of character."
    wt_image principal_domme_outfit_3_20
    hannah.c "Greedy worm!  I told you to stick your tongue up my ass, not my pussy."
    hannah_domme_client_3 "I'm sorry, Mistress, but your pussy is so sexy.  Please, may I serve you by licking your pussy?  Please, Mistress??"
    wt_image principal_domme_outfit_3_21
    hannah.c "Okay, worm.  Since you want it that badly, I'm going to let you lick my pussy.  But you're going to be punished for tasting me before you had permission."
    hannah_domme_client_3 "Yes, Mistress.  Thank you, Mistress!!"
    wt_image principal_domme_outfit_3_8
    "Greedily he laps at her labia and clit. You can smell her wetness from across the room, and hope that she can't see the hard on it inspires in you, for fear of getting the same ball bondage treatment as her client."
    wt_image principal_domme_outfit_3_22
    "Perhaps Mistress Hannah has finally come to terms with her inner sadist, as she makes no effort to hide her growing arousal as she pushes her client's face more and more firmly into her snatch."
    wt_image principal_domme_outfit_3_9
    "Scissoring her legs tightly around his head, she pulls a crop out of her bag and starts beating him across the shoulders, arms, and back as he eats her out.  Before long, she's shuddering to climax against his face."
    hannah.c "Oooohhhhhh FUCCCKKK!!!"
    wt_image principal_domme_outfit_3_21
    hannah.c "Did you like that, worm?  Did you like Mistress letting you have her cum all over your face?"
    hannah_domme_client_3 "Yes, Mistress!  Thank you, Mistress!!"
    wt_image principal_domme_outfit_3_25
    hannah.c "I'm not finished with you yet, worm.  Let's get you face down over your desk.  I'm going to fuck you before I go."
    wt_image principal_domme_outfit_3_26
    "With the rope no longer binding his balls, his hard on reappears as he feels Hannah spread open his ass and apply lube."
    wt_image principal_domme_outfit_3_27
    "A moment later he spills his seed all over the floor underneath his desk as Mistress Hannah plows his ass with a dildo."
    wt_image principal_domme_outfit_3_11
    hannah_domme_client_3 "Ooohhhhhh"
    wt_image principal_domme_outfit_3_23
    hannah.c "Look at the mess your tiny dick made over you and your desk.  You liked that didn't you, worm?  You liked being Mistress' little fuck toy."
    hannah_domme_client_3 "Yes, Mistress!!  Thank you, Mistress!!!"
    wt_image principal_domme_outfit_3_24
    hannah.c "Your pathetic little worm dick is hard again already.  How hard do I need to squeeze your balls to make it go away, worm?"
    hannah_domme_client_3 "AAAGGHH ... I don't think it will, Mistress!!"
    hannah.c "Too bad the receptionist is just down the hall and I forgot to bring a gag, or I'd keep squeezing until we found out, worm."
    wt_image principal_domme_outfit_3_12
    hannah.c "I thought that went well today. Was that a better mix of humiliation and torture?"
    player.c "I'd say so, yes. The client certainly seemed happy."
    hannah.c "He asked me if I would allow him to see me again, so yes, I think he was."
    player.c "Be careful with the small dick humiliation, though.  Not every guy will appreciate that."
    hannah.c "Give me some credit.  The guy was clearly turned on when I referred to his little package.  It didn't take much to figure out that was a kink of his."
    "Hannah is definitely growing into this role."
    $ player.domme_income += 20
  elif hannah.domme_outfit_count == 4:
    wt_image principal_face_6
    player.c "I have another client looking to spend time with Mistress Hannah."
    hannah.c "At the Club this time, or somewhere else?"
    player.c "The Club.  I'll bring him by."
    call forced_movement(club) from _call_forced_movement_971
    summon hannah to club
    wt_image principal_domme_outfit_4_1
    "As she watches you and the client come in, Hannah looks more regal and confident than you're ever seen her.  She's really growing into her Domme persona."
    wt_image principal_domme_outfit_4_14
    hannah.c "Remove your clothes and kneel in front of me."
    "She's speaking to the client, but some part of you wishes the command was directed to you.  The client, for his part, looks ecstatic."
    wt_image principal_domme_outfit_4_15
    hannah_domme_client_4 "Yes, Mistress.  Thank you!"
    wt_image principal_domme_outfit_4_16
    "As the client gets into position, Mistress Hannah pretends to ignore him, focussing instead on her already impeccable lipstick.  She leaves him there for a few minutes before addressing him again."
    wt_image principal_domme_outfit_4_25
    hannah.c "Why are you here?"
    hannah_domme_client_4 "To serve you."
    wt_image principal_domme_outfit_4_18
    hannah.c "And how do you think you can do that?"
    hannah_domme_client_4 "In whatever way Mistress wishes."
    wt_image principal_domme_outfit_4_19
    hannah.c "You're not fit to serve me.  You're a useless, ridiculous male.  A pathetic worm who's lucky to be allowed in my presence."
    hannah_domme_client_4 "I know, Mistress.  I'm sorry.  I'll do anything you want for you."
    wt_image principal_domme_outfit_4_2
    hannah.c "Anything?  Unconditionally?  Do you know what they call someone who serves a Mistress unconditionally?"
    hannah_domme_client_4 "Yes, Mistress.  A slave, Mistress."
    wt_image principal_domme_outfit_4_3
    "Hannah pulls out her lipstick and starts writing across her client's chest in bright red letters."
    hannah.c "And do you know what they call someone who'll serve a Mistress he just met?  Someone who'd serve any Mistress who gives him the time of day?"
    hannah_domme_client_4 "I'm not sure, Mistress."
    hannah.c "A slave slut.  That's what you are, aren't you?  A worthless little slave slut with nothing to offer, hoping against hope that some Mistress will take pity on him and put him to use."
    hannah_domme_client_4 "Yes, Mistress.  I'm a slave slut."
    wt_image principal_domme_outfit_4_20
    "Mistress Hannah slips a blindfold over his eyes, then surprises him by licking up his face."
    hannah.c "You don't need to see me.  You'll serve anyone who'll take you.  You're lucky to receive any contact at all."
    hannah_domme_client_4 "Ohhh yes!!  Thank you, Mistress."
    wt_image principal_domme_outfit_4_21
    hannah.c "Even a painful touch, like these nipple clamps, is more than a pathetic worm like you deserves."
    hannah_domme_client_4 "Nnnnnn ... Yes, Mistress!  Thank you, Mistress."
    wt_image principal_domme_outfit_4_21
    hannah.c "I'm going to find out whether you can amuse me.  You're going to kneel there in the darkness and scream for me.  What's wrong, slave slut?  Are you scared?  Is this too much for you?  Maybe you can't serve me in this way?"
    hannah_domme_client_4 "Yes, Mistress.  I mean, no Mistress.  I mean  ...  Yes, Mistress, I'm scared, but I do want to serve you.  I'm a worthless, pathetic slave slut and if hearing me scream will amuse you, I'll do it."
    wt_image principal_domme_outfit_4_4
    "The client seems scared to death as Hannah gets into position.  Blindfoled, he can't see the paddle, and isn't sure what's in store for him ..."
    wt_image principal_domme_outfit_4_23
    "*smack*"
    hannah_domme_client_4 "Nnnnnnn!!!"
    wt_image principal_domme_outfit_4_4
    hannah.c "I told you to scream, not hold it in.  Are you trying to be brave for me?"
    hannah_domme_client_4 "Yes, Mistress."
    wt_image principal_domme_outfit_4_23
    "*smack*"
    hannah_domme_client_4 "Nnnnnnn!!!"
    wt_image principal_domme_outfit_4_4
    hannah.c "Don't be.  I want you to amuse me with your screams."
    wt_image principal_domme_outfit_4_24
    hannah.c "Or maybe to get you screaming I need to paddle you somewhere else, instead?"
    hannah_domme_client_4 "NO!!  NO PLEASE, MISTRESS!!!  Not there, please!!!  I'll scream for you if you beat my chest.  I will, Mistress!!!"
    wt_image principal_domme_outfit_4_23
    "*smack*"
    wt_image principal_domme_outfit_4_4
    hannah_domme_client_4 "AAAAGGGHHH!!!"
    hannah.c "Hmmpphh.  You can scream okay, I suppose.  Once you're suitably terrified.  I wonder if you can amuse me in other ways, too?"
    wt_image principal_domme_outfit_4_17
    "Hannah takes a seat in front of the blindfolded man as she considers how to proceed.  She's noticed his lack of erection from the physical punishment alone, so changes tack."
    wt_image principal_domme_outfit_4_26
    hannah.c "Can you guess what that is, slave slut?"
    hannah_domme_client_4 "Yes, Mistress.  It's your shoe.  May I please worship it?"
    wt_image principal_domme_outfit_4_5
    hannah.c "You want the opportunity to worship me?"
    "His reply is a little muffled by her heel pressing down on his tongue, but still intelligible."
    hannah_domme_client_4 "Yeth, Mithreth."
    wt_image principal_domme_outfit_4_27
    "She removes her shoe from his mouth and slips it off."
    hannah.c "No.  I'm not interested in watching you show me what a worthless boot-licker you are."
    wt_image principal_domme_outfit_4_6
    hannah.c "Now my feet are a different story.  My feet are sore and hot and tired after a long day in heels.  Are they smelly, slave slut?"
    hannah_domme_client_4 "No, Mistress."
    wt_image principal_domme_outfit_4_7
    hannah.c "Are you sure?  Get your nose and tongue right in there.  Take a big whiff."
    hannah_domme_client_4 "I love the smell of your feet, Mistress."
    wt_image principal_domme_outfit_4_28
    hannah.c "Slae sluts don't get to to what they love, though, do they?  They have to do what their Mistress loves.  And I love hurting you."
    hannah_domme_client_4 "Oh yes, Mistress!!  Make me serve you the way you love having me serve you!"
    wt_image principal_domme_outfit_4_29
    "*thwippp* ... Hannah brings the whip down lightly on her client's back.  You know how she actually prefers to make clients suffer, and this is a love tap compared to that.  Her client doesn't know that, however, and starts licking her feet even more enthusiastically, thinking that Hannah is using him the way she wants."
    wt_image principal_domme_outfit_4_18
    "After a couple of more light blows, Hannah removes her client's blindfold."
    hannah.c "That's enough fun for you.  Now I'm going to use my slave slut the way he deserves to be used.  I'm going to fuck your ass, slave."
    hannah_domme_client_4 "Oh yes, Mistress!  Thank you!!"
    hannah.c "I'm going to make you suffer while I fuck you, though."
    hannah_domme_client_4 "Yes, Mistress.  Anything to please you!"
    wt_image principal_domme_outfit_4_30
    "The clothespins Mistress Hannah adds up and down his side are probably more suffering than the client wants ..."
    wt_image principal_domme_outfit_4_31
    "... and the ones she adds to his testicles are definitely more suffering than he'd ever voluntarily ask for."
    wt_image principal_domme_outfit_4_10
    "But the suffering is replaced by the satisfaction of having his limits pushed when he feels Mistress Hannah penetrate him with the strap-on ..."
    wt_image principal_domme_outfit_4_11
    "... and he feels how enthusiastically she reams his ass."
    hannah.c "Go on, slave slut.  Show me how well you can fuck Mistress' big hard dick.  Faster, slave slut!  Faster!!"
    hannah_domme_client_4 "aaaagghhhhh"
    wt_image principal_domme_outfit_4_12
    "Recognizing the sign of his impending orgasm, Hannah pulls out and finishes him off into a glass with a few flicks of her fingernails against his cock and balls."
    hannah_domme_client_4 "ooohhhhh!!!"
    wt_image principal_domme_outfit_4_32
    hannah.c "Were you planning on making a mess all over Mistress' floor, slave slut?"
    hannah_domme_client_4 "No, Mistress.  I'm sorry, Mistress."
    wt_image principal_domme_outfit_4_13
    hannah.c "Mistress caught your disgusting man juice in a glass.  It's a good thing for you that I did, or you'd be down on the floor cleaning it up with your tongue.  As it is, you can dispose of it down your useless throat.  Open up."
    wt_image principal_domme_outfit_4_33
    "After he's finished swallowing his own cum, the client is allowed to dress.  He pays Hannah, then pretty much floats out of the Club, still riding a submissive high."
    wt_image principal_domme_outfit_4_14
    player.c "He seemed happy."
    hannah.c "I think he was."
    wt_image principal_domme_outfit_4_17
    hannah.c "That brings us to something I wanted to talk to you about.  I don't need your direct involvement any longer.  I appreciate your help in getting me started, but I can take it from here."
    hannah.c "I've been getting lots of direct inquiries for my services, and I know what type of client I'm looking for now. I've made arrangements with another Domme to space share with her, so I won't need to impose on your Club any further either."
    hannah.c "I'll keep paying you a cut weekly, for the use of the infrastructure you set up for me, but I'm cutting it in half.  That way there's more left for the school."
    hannah.c "You're dismissed."
    "At least you won't need to use any Energy in the future arranging sessions for her."
    $ player.domme_income += 10
    $ title = "Ask if you can be one of her clients?"
    menu:
      "Yes":
        player.c "Could I be one of your clients, Mistress?"
        wt_image principal_domme_outfit_4_25
        hannah.c "Funny you should ask that.  I've been thinking that you should submit to me, but not like these other clients."
        hannah.c "We have a special relationship, you and I, one built on money.  I'll accept your submission.  It begins with you paying me 25 now, and again at the end of every week."
        player.c "What do I get for that, Mistress?"
        hannah.c "Nothing.  Just the financial suffering that comes from giving your money to someone who truly deserves it."
        player.c "When will you Domme me?"
        hannah.c "Physically, never.  You're not worth my time and effort, worm.  All I want from you is your money.  If you want to submit to me, you'll give it to me."
        $ title = "What do you say?"
        menu menu_hannah_fin_domme_choice:
          "Yes, Mistress":
            player.c "Yes, Mistress.  I'll send you the 25."
            wt_image principal_domme_outfit_4_1
            hannah.c "Good.  Go now."
            player.c "Is that all?"
            hannah.c "Until the end of the week, yes."
            $ hannah.financial_domination_cost += 25
            change player money by -25
          "Nice try" if not hannah.has_tag('nice_try'):
            add tags 'nice_try' to hannah
            player.c "Nice try, but I like my domination to be of the physical sort."
            wt_image principal_domme_outfit_4_14
            hannah.c "Too bad.  The only submission I want from you is financial.  I've already had enough physical contact with you to last a lifetime."
            $ title = "Submit to financial domination?"
            jump menu_hannah_fin_domme_choice
          "No" if hannah.has_tag('nice_try'):
            player.c "I'll pass."
      "No":
        pass
    rem tags 'nice_try' from hannah
    add tags 'whore' to hannah # Added to make check_whore label get called correctly
    call forced_movement(living_room) from _call_forced_movement_972
    call character_location_return(hannah) from _call_character_location_return_676
  notify
  return

# Contact - Visit Hannah the School Principal
label hannah_contact_visit:
  if hannah.lost_money_and_no_fix == 1:
    # $ hannah.training_session() ## no: no need to shut off visits to Hannah for the rest of the day
    # add tags 'discussed_bethany' to hannah
    call forced_movement(school) from _call_forced_movement_973
    wt_image school.image
    "A trip to the School Principal's office is in order to discuss Bethany the Banker.  You make your way to the local school."
    wt_image principal_office_19
    summon hannah
    if hannah.letter_re_terri < 2:
      hannah.c "Hello. My name is Hannah.  I'm the principal of this school.  You wanted to see me?"
    elif hannah.letter_re_terri == 2:
      hannah.c "Hello. My name is Hannah. I'm the principal of this school."
      wt_image principal_office_1
      "She bristles as she recognizes you from your prior, unauthorized and rather inappropriate trip to the school."
      hannah.c "Are you here about the letter I sent you?"
      player.c "No, I have something more important to discuss with you."
    elif hannah.letter_re_terri > 2 and hannah.letter_re_terri < 9 and hannah.letter_re_terri != 7:
      wt_image principal_office_1
      "Hannah bristles when she sees you come in."
      hannah.c "I asked you not to come back here."
      player.c "I know, but I have something important to discuss with you."
    elif hannah.letter_re_terri == 7:
      wt_image principal_office_2
      "Hannah blushes slightly when she sees you come in."
      if hannah.has_tag('ready_for_sex_at_school'):
        hannah.c "It's nice to see you, but now isn't really a good time."
        player.c "I know.  That's what I'm here to discuss with you."
      else:
        hannah.c "You're not supposed to be here. I thought we agreed to ... you know, only see each other at your house."
        player.c "I know, but I have something important to discuss with you."
    elif hannah.letter_re_terri > 8:
      wt_image principal_office_1
      "Hannah bristles when she sees you come in."
      hannah.c "You shouldn't be here."
      player.c "I have something important to discuss with you."
    if player.has_tag('hypnotist'):
      $ title = "Do you want to hypnotize her?"
      menu:
        "Yes, hypnotize her":
          wt_image principal_office_19
          player.c "Principal Hannah, please look at this."
          call focus_image from _call_focus_image_19
          player.c "You and I are going to have a talk.  You are going to listen to me.  Listen to me now.  Listen to me.  Only me.  Only my words now.  Only my words."
          wt_image principal_office_2
          "She soon falls under your trance."
          player.c "Let's be comfortable for our talk, Hannah. You want to be comfortable around me.  You want me to be comfortable around you."
          wt_image principal_office_20
          player.c "Remove your blouse, Principal, so that you and I will be comfortable for our talk."
          wt_image principal_office_3
          add tags 'hypnotized_now' to hannah
        "No, just talk with her":
          pass
    player.c "I understand you lost some money?"
    "Hannah starts to fume."
    hannah.c "I didn't lose the money! The bank lost the money. We needed that money, to keep the school going. I don't know how we'll be able to keep classes open until the end of the term now."
    player.c "Perhaps I could help you out."
    # if bethany.ready_to_help_school == 1 or bethany.ready_to_help_school == 2:  ## not needed
    #  $ bethany.action_contact_getting_back = living_room.add_action("Get Back to Bethany the Banker", label = bethany.short_name + "_contact_getting_back", context = "_contact_other", condition = "bethany.can_be_interacted")
    $ title = "What do you suggest?"
    menu:
      "She could make the money back":
        $ title = "How should she make back the money?"
        menu:
          "Get it from the Club President" if gloria.session > 6:
            call hannah_contact_visit_get_money_from_gloria from _call_hannah_contact_visit_get_money_from_gloria
          "Work for it" if hannah.letter_re_terri == 12:
            player.c "I could help you earn your lost money back."
            hannah.c "And how could I do that, while I'm trying to keep the school going?"
            player.c "By working part time in the evenings."
            hannah.c "At what? Do you think I'm going to take a part time job as a waitress to keep the school financed? I love the children, but that's asking too much."
            hannah.c "And besides, its not likely to be enough money anyway to replace what's been lost."
            player.c "I was thinking of more lucrative work."
            hannah.c "More lucrative?  What are you ..."
            hannah.c "Are you suggesting I sell myself to make the money back?"
            player.c "That's exactly what I'm suggesting."
            hannah.c "You're insane.  I'm not that type of woman."
            player.c "Yes you are.  You had sex with me to keep the school from being financially ruined before.  An effort that turned out to be a complete waste, as you lost that money anyway I might point out."
            player.c "This is just the same.  Only hopefully this time you won't place the funds you earn back somewhere you might lose them."
            hannah.c "No, I won't.  I'll need them for operational expenses each week anyway."
            player.c "So that's decided.  I'll make arrangements to line up some clients for you.  You won't have to do anything other than show up when I tell you to, and make the clients happy."
            hannah.c "But ..."
            player.c "Do you have any other alternatives, Hannah?  Other than shutting the school's doors?"
            hannah.c "I guess not."
            player.c "I'll be in touch soon."
            "It may take you a few days to line up her first client, but it shouldn't be too hard to find her some paying customers."
            $ hannah.lost_money_and_no_fix = 3
            call hannah_convert_whore from _call_hannah_convert_whore
          "Need to work on a solution":
            call hannah_contact_visit_need_solution from _call_hannah_contact_visit_need_solution
      "Bethany the Banker may be able to help" if bethany.ready_to_help_school == 1 or bethany.ready_to_help_school == 2:
        call hannah_discuss_bethany from _call_hannah_discuss_bethany
      "You could help her":
        $ title = "How are you going to get the money to help her?"
        menu:
          "Get it from the Club President" if gloria.session > 6:
            call hannah_contact_visit_get_money_from_gloria from _call_hannah_contact_visit_get_money_from_gloria_1
          "Need to work on a solution":
            call hannah_contact_visit_need_solution from _call_hannah_contact_visit_need_solution_1
    if hannah.has_tag('hypnotized_now'):
      $ hannah.hypno_session() # deducts energy and records hypnosis
      rem tags 'hypnotized_now' from hannah
      "You're not going to be able to do anything more with the hypnotized woman, so you release her from her trance, letting her remember what she needs to remember, and then go."
      notify
    else:
      change player energy by -energy_very_short notify
    call character_location_return(hannah) from _call_character_location_return_677
    call forced_movement(living_room) from _call_forced_movement_974
  elif hannah.lost_money_and_no_fix == 2:
    if gloria.session > 6 or bethany.ready_to_help_school == 1  or bethany.ready_to_help_school == 2:
      $ title = "Suggest a solution to Hannah?"
      menu:
        "The Club President and his wife could be donors" if gloria.session > 6:
          # $ hannah.training_session()  ## no, not needed
          wt_image principal_office_19
          call hannah_contact_visit_get_money_from_gloria from _call_hannah_contact_visit_get_money_from_gloria_2
        "Bethany the Banker may be able to help" if bethany.ready_to_help_school == 1 or bethany.ready_to_help_school == 2:
          wt_image principal_office_19
          call hannah_discuss_bethany from _call_hannah_discuss_bethany_1
        "Wait for another solution":
          pass
          # $ hannah.remove_tags('trained_today', 'trained_this_week')
    else:
      "You don't have a solution for Hannah's problem yet. You should wait to visit her until you do."
  elif hannah.has_tag('ready_for_sex_at_school'):
    call forced_movement(school) from _call_forced_movement_975
    summon hannah
    $ hannah.training_session()
    wt_image principal_office_2
    "Hannah blushes as she sees you enter her office."
    hannah.c "I'm very busy right now."
    player.c "That's okay.  It only takes you a moment to flash that pretty pussy of yours at me.  Go ahead, no one can see you."
    wt_image principal_office_27
    "With a flush look on her face, Principal Hannah raises her leg and lifts the front of her skirt."
    wt_image principal_office_28
    hannah.c "Did you come all the way over here just to see this?"
    $ title = "What next?"
    menu:
      "Finger fuck her":
        wt_image principal_office_12
        player.c "That and to finger fuck you.  Lean back."
        wt_image principal_office_29
        hannah.c "The staff! ... students!"
        player.c "Could come looking for you at any time.  I know.  Let's hope you can cum quickly ... and quietly."
        wt_image principal_office_14
        "With one hand on her breast and the other finger fucking her moist pussy, you soon bring her to an orgasm she struggles hard not to vocalize."
        wt_image principal_office_30
        hannah.c "mmm mmmmhhhhh"
        wt_image principal_office_31
        player.c "Happy I dropped by now?"
        hannah.c "Yes.  Now go, quick, before someone finds us."
        player.c "Not until you tell me how hot that was."
        wt_image principal_office_15
        hannah.c "It was crazy hot.  You're amazing, a true sex god!  Satisfied?  Get going already!"
        player.c "Can I hear that part about being a sex god again?"
        wt_image principal_office_32
        hannah.c "Go!"
        $ hannah.pleasure_her_count += 1
        $ hannah.orgasm_count += 1
        $ hannah.visit_week += 1
        change player energy by -energy_short notify
      "Blow job":
        player.c "Nope. I came over here to receive a blow job from my favorite Principal."
        wt_image principal_office_12
        hannah.c "Someone could come looking for me any minute."
        player.c "Then you'd better start sucking me off."
        wt_image principal_office_7
        hannah.c "Make this quick."
        player.c "That's up to you.  The better you blow me the faster I'll cum."
        wt_image principal_office_9
        "She wraps her lips around your cock and bobs her head up and down as her hand plays with your balls.  It's a full on, enthusiastic assault."
        player.c "Mmmm.  Nice.  Keep your eyes on me if you really want to get me off fast.  I love watching you watch me as you suck me off."
        wt_image principal_office_8
        "Her beautiful eyes locked on yours, she bobs her head faster and faster, coaxing the cum out of your balls."
        wt_image principal_office_33
        "You remember to stay quiet as you cum, letting out only a soft moan as you fill her mouth with your load."
        player.c "[player.orgasm_text]"
        wt_image principal_office_34
        player.c "Very nice, Principal Hannah."
        wt_image principal_office_35
        hannah.c "I'm glad you liked it.  If you ever want another one, you'll get out of here, now, before someone catches us."
        player.c "I'm going."
        $ hannah.blowjob_count += 1
        $ hannah.swallow_count += 1
        orgasm notify
      "Sex":
        player.c "Nope, not just to see it.  To fuck it."
        wt_image principal_office_12
        hannah.c "Be serious.  One of the students or a staff member could come looking for me any minute now."
        player.c "Then let's make this a quickie.  You're already wet, I can see it.  Turn around."
        wt_image principal_office_16
        "Against her better judgment, she does."
        wt_image principal_office_17
        "You slide inside her easily, eliciting a deep moan"
        hannah.c "ohhhh"
        wt_image principal_office_36
        player.c "Shhh.  Quiet, Principal.  You don't want anyone coming in to see if you're all right."
        wt_image principal_office_37
        hannah.c "Shut up and just fuck me!"
        wt_image principal_office_18
        "You happily oblige her, thrusting in and out of her rapidly wetting pussy."
        wt_image principal_office_38
        "It only takes a few hard strokes for her to climax, stifling her groans as best she can when she does."
        wt_image principal_office_11
        hannah.c "mmm mmmmhhhhh"
        wt_image principal_office_39
        "The feel of her cumming on your cock is enough to take you over the edge too.  You do your best to stay quiet as you empty your load inside her."
        player.c "[player.orgasm_text]"
        wt_image principal_office_16
        player.c "Happy I dropped by?"
        wt_image principal_office_32
        hannah.c "Yes, that was crazy hot.  Get going now, though, before someone comes looking for me."
        $ hannah.sex_count += 1
        $ hannah.orgasm_count += 1
        $ hannah.visit_week += 1
        orgasm notify
      "That's all":
        wt_image principal_office_12
        player.c "Yup.  That's all.  Thanks for the show, Principal!"
        change player energy by -energy_very_short notify
    call character_location_return(hannah) from _call_character_location_return_678
    call forced_movement(living_room) from _call_forced_movement_976
  wt_image current_location.image
  return

label hannah_discuss_bethany:
    player.c "Was Bethany your banker?"
    hannah.c "That stupid bitch?  Yes, she was.  She was the one who recommended we put the school's funds into their crooked investment fund.  Why?"
    player.c "She's ready to embark on a new career, and she's not too choosy about the type of work she does. I thought perhaps she might be able to help you out, and make amends for the financial harm she did the school."
    "Hannah thinks for a moment."
    if hannah.letter_re_terri == 11:
        hannah.c "Do you think she's really ready to make amends?  If so, I know a way I can use her to raise the money needed to keep the school going."
    else:
        hannah.c "How flexible is she ready to be?  I can think of a way I can use her to save money, maybe even enough to keep the school going, but she won't like it.  And I won't be able to pay her anything more than subsistence wages."
    sys "If you send Bethany to Hannah, she won't be available for any other work you might have had in mind for her."
    $ title = "What do you say?"
    menu:
        "I'll send Bethany to you" if bethany.ready_to_help_school == 2:
            if hannah.letter_re_terri == 11:
                player.c "I'll let her know you have a great opportunity for her to fix her past mistakes and start anew."
                "You head home and send Bethany a message letting her know you found her a new gig at the school.  Hopefully Hannah will keep you informed of how she's doing."
                $ bethany.torture_week = week
            else:
                player.c "Don't worry about her pay.  Just tell her there will be opportunities for promotion down the road."
                "You head home and send Bethany a message letting her know you found her a new gig at the school.  In a week or so you should check in and see how she's doing."
                $ bethany.ready_for_visit_at_school = 1
                if hannah.letter_re_terri == 7:
                    $ hannah.visit_week = week + 2
                    add tags 'need_bethany_thank_you' to hannah
            $ bethany.ready_to_help_school = 3
            $ hannah.lost_money_and_no_fix = 3
            rem tags 'available_for_school_visit' from hannah
            $ hannah.waiting_on_banker = 2

        "I'll get back to you":
            player.c "Let me investigate a bit further, and I'll get back to you."
            "If you don't find Bethany another type of work, you can send her to Hannah the next time you talk to her."
            $ hannah.waiting_on_banker = 1
            $ hannah.lost_money_and_no_fix = 2
            $ hannah.visit_week = 0
            add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to hannah
    return

label hannah_contact_visit_get_money_from_gloria:
  player.c "I have an idea on how you can make the money back, Hannah."
  hannah.c "How?"
  player.c "A friend of mine and her husband are big philanthropists.  Always going to fundraisers, that sort of thing."
  "Hannah sighs."
  hannah.c "I was never any good at raising money from donors.  They always want something in return."
  player.c "My friend and her husband will likely want something too, but if they cut a big cheque to the school afterwards, it would be worth it, wouldn't it?"
  hannah.c "I suppose."
  player.c "Let me set it up with them.  I'll get you in front of them, then you show them how grateful you are for their generosity, and afterwards you can go back to running the school the way you want to run it, with your money problems solved."
  hannah.c "All right.  Whatever it takes, I'll do it."
  $ hannah.lost_money_and_no_fix = 3
  rem tags 'available_for_school_visit' from hannah
  $ gloria.discussed_principal = 1
  add tags 'something_to_discuss' to gloria
  add tags 'gloria_other_talk_option_possible' to hannah
  return

label hannah_contact_visit_need_solution:
  player.c "I don't have a solution yet, but I'll try to work on one."
  hannah.c "Okay, please let me know when you do.  I won't have time to solve it myself, I don't think.  I'm not going to have time for anything right now.  Trying to keep the school going with no money is going to take all my energy."
  "If you could make friends with a generous patron willing to donate to the school, that could be a solution to Hannah's problem."
  $ hannah.lost_money_and_no_fix = 2
  $ hannah.visit_week = 0
  add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to hannah
  # $ hannah.remove_tags('trained_today', 'trained_this_week')
  return

# Contact - Set Up Group Sex with Hannah (Ends Day)
label hannah_contact_group_sex:
  if hannah.lost_money_and_no_fix == 1:
    "Hannah's not available for this sort of extra-curricular activity while she's trying to keep the school going during its money troubles."
  else:
    if hannah.group_sex == 3:
      "To set up a safe 'forced' scene for Hannah, you need to find a burly group of men you can trust.  I wonder who would have a gang like that?"
    # group sex with Marilyn's men
    elif hannah.group_sex == 4:
      $ hannah.training_session()
      wt_image principal_face_1
      player.c "Feeling feisty?"
      hannah.c "What do you mean?"
      player.c "You're going to need some spunk if you plan on fighting off a half dozen men intent on having their way with you."
      wt_image principal_face_2
      hannah.c "Are you serious?  Have you set it up?"
      player.c "Tonight at my house.  Get some rest if you can.  You'll need it."
      summon hannah
      wt_image principal_booty_call_1_1
      "Hannah shows up with a big grin on her face."
      wt_image principal_group_2_1
      hannah.c "I can't believe this is going to happen."
      player.c "Did you bring your running shoes?"
      wt_image principal_group_2_2
      hannah.c "No.  I came directly from work.  Why?"
      player.c "Because in less than 60 seconds, a group of men are going to come through that door and have their way with you, and they're not going to be gentle about it.  If you're still here when they get here, your pussy and a few other parts are going to be sore for a week.  If you want any chance at saving yourself, you'd better get out here fast."
      wt_image principal_group_2_3
      hannah.c "What?  You think I should run?"
      player.c "You have about 30 seconds now."
      wt_image principal_group_2_4
      "Principal Hannah hesitates for just a moment, then bolts for the door."
      wt_image principal_group_2_5
      "Too late.  Marilyn's men are here, and they're not going to let the 'bonus' they were promised get away that easily.  They grab her ..."
      wt_image principal_group_2_6
      "... carry her across the room ..."
      wt_image principal_group_2_7
      "... and deposit her in the center of a sea of masculinity."
      wt_image principal_group_2_8
      "Hannah struggles to get up, but Marilyn's men are having none of it."
      wt_image principal_group_2_9
      "Her clothes are unceremoniously ripped off.  It looks like she'll be wearing one of your long coats home."
      wt_image principal_group_2_10
      "As they finish stripping her naked, the men prepare to make use of her."
      wt_image principal_group_2_19
      "No one asks her permission, nor is she given any chance to object as the first cock enters her."
      wt_image principal_group_2_20
      "The men simply take turns using her cunt ..."
      wt_image principal_group_2_12
      "... mouth ..."
      wt_image principal_group_2_21
      "... and ass."
      wt_image principal_group_2_22
      "Or all three holes at once."
      if hannah.has_tag('forgot_dp'):
        wt_image principal_group_2_23
        "At least Hannah doesn't need to worry about remembering to ask them to DP her, unlike the last group."
      wt_image principal_group_2_24
      "Hannah loses track of how many men have cum inside her ..."
      wt_image principal_group_2_25
      "... or on her."
      wt_image principal_group_2_16
      "One by one the men take their pleasure from her then depart, leaving her a sticky mess, jizz coating her skin and seeping out of every hole."
      wt_image principal_group_2_17
      player.c "Are you okay Hannah?"
      wt_image principal_group_2_18
      hannah.c "Fuck that was crazy.  Hot, but crazy."
      player.c "Hot enough to do again?"
      if day == 5:
        hannah.c "Never!  I'll just savor the memory of tonight, thanks.  I'm exhausted and sore everywhere.  Thank god it's Friday!  I think I'll sleep the entire weekend."
      else:
        hannah.c "Never!  I'll just savor the memory of tonight, thanks.  I'm exhausted and sore everywhere.  If I didn't have work in the morning, I think I'd sleep for a week."
      $ title = "Let her go home?"
      menu:
        "No, she still has one more dick to service":
          player.c "There's one man left who hasn't had his way with you."
          wt_image principal_group_2_26
          hannah.c "I'm really tired and every part of me hurts right now."
          player.c "Then you'd better use your mouth to get me off quick, before I decide to use your ass and pussy, too."
          wt_image principal_group_2_27
          "That motivated her.  Tired as she is, she attacks your cock with enthusiasm ..."
          wt_image principal_group_2_28
          "... and soon earns her final cum shot of the night."
          player.c "[player.orgasm_text]"
          $ hannah.blowjob_count += 1
          $ hannah.facial_count += 1
          orgasm
        "Yes, let her go home":
          change player energy by -energy_very_short
      wt_image principal_group_2_18
      "Hannah seems happy.  The men seemed happy, that means Marilyn should be happy.  Marilyn now owes you a favor, which makes you happy.  Everybody's happy."
      $ hannah.visit_week += 1
      $ hannah.group_sex = 5
      $ marilyn.favour += 1
      call character_location_return(hannah) from _call_character_location_return_679
      end_day notify
    # first group sex
    elif hannah.group_sex == 1:
      $ hannah.training_session()
      wt_image principal_office_1
      "It's not hard to find volunteers to have sex with a beautiful woman, even when they know there's going to be other guys around.  You consider charging them for the privilege, but realize you're not sure how Hannah will react when her fantasy is made reality."
      wt_image principal_face_1
      player.c "Ready for a play date?"
      hannah.c "A what?"
      player.c "A play date.  Just you, me and three other men."
      wt_image principal_face_2
      hannah.c "Tonight?"
      player.c "At my house.  See you soon."
      summon hannah
      wt_image principal_booty_call_1_1
      player.c "Come on in and take your clothes off."
      wt_image principal_group_1_17
      hannah.c "You want me to be naked when the others show up?"
      player.c "Almost.  Have a seat, spread your legs and remove your panties."
      wt_image principal_group_1_1
      hannah.c "Are you serious?  What will that make me look like when the others come in?"
      player.c "A horny slut.  Specifically, a horny slut who's ready to have sex with all comers.  That's your fantasy, isn't it?"
      wt_image principal_group_1_2
      hannah.c "Yes.  It just sounds even dirtier when you say it that way."
      wt_image principal_group_1_3
      hannah.c "Now what?"
      player.c "Now you wait for the hard cocks to arrive, and when they do, you satisfy them.  Until then, you can touch yourself, but no cumming until the hard cocks get here."
      wt_image principal_group_1_4
      "She doesn't have to wait long for the men to arrive.  As you show them in, she understandably becomes shy about the spectacle she's making of herself."
      wt_image principal_group_1_18
      "Fortunately, the men respond in a way that fuels her fantasy, and her excitement overcomes her nervousness."
      wt_image principal_group_1_5
      "A strong hand on her arm lifting her to her feet reminds her that tonight isn't just for her fun.  She has some responsibilities to look after."
      wt_image principal_group_1_6
      "Her remaining clothes are soon shed ..."
      wt_image principal_group_1_7
      "... as are the men's, so that she can get down to business."
      wt_image principal_group_1_8
      "Hannah's always been an accomplished, hard-working woman ..."
      wt_image principal_group_1_9
      "... and her multi-tasking skills prove invaluable as she tries to satisfy three hard cocks at once."
      wt_image principal_group_1_10
      "Eventually the men help her out by bringing more of her holes into use ..."
      wt_image principal_group_1_11
      "... rotating through the positions so that everyone gets a turn at each location."
      wt_image principal_group_1_12
      "One by one they reach the point where they've experienced enough of Hannah's body, and are ready to cum.  Hannah's finished at the school for today, so makes no objection to receiving the show of their appreciation over her face and hair."
      hannah_gangbang_man_1 "Uuhhhhhhhhh"
      wt_image principal_group_1_19
      hannah_gangbang_man_2 "Aaaaahhhhhh"
      wt_image principal_group_1_20
      hannah_gangbang_man_3 "Mmmmmmhhh"
      wt_image principal_group_1_13
      "As the men leave, Hannah gazes up at you with a goofy, happy grin on her face."
      hannah.c "Oh my fuck, that was amazing!!"
      player.c "Any regrets?"
      wt_image principal_group_1_21
      if hannah.anal_count > 0:
        add tags 'forgot_dp' to hannah
        hannah.c "Only that they didn't DP me.  I was so caught up in trying to get them all off, I didn't think of it while they were here.  I'm sure they would have if I'd asked."
      else:
        hannah.c "None!"
      $ title = "Take your turn?"
      menu:
        "Why not?":
          player.c "You're not done yet, you horny slut.  There's still one more cock for you to service."
          wt_image principal_group_1_23
          hannah.c "I was hoping you'd ask."
          wt_image principal_group_1_15
          "You pull her head onto your hard cock, making her take you deeper than she took the other men.  Far from objecting, she responds enthusiastically to your act of possession.  Although it's a struggle to suck you properly in this position, she works hard to pleasure you ..."
          wt_image principal_group_1_16
          "... until you're ready to deposit your cum on her face alongside that of her other gentlemen callers."
          player.c "[player.orgasm_text]"
          wt_image principal_group_1_21
          hannah.c "Mmmmmm.  Well that completes the night perfectly!"
          $ hannah.facial_count += 1
          $ hannah.blowjob_count += 1
          orgasm
        "Pass":
          change player energy by -energy_very_short
      player.c "I'm glad you enjoyed yourself."
      wt_image principal_group_1_22
      hannah.c "I did!  Thanks so much for setting that up!"
      $ hannah.visit_week += 1
      $ hannah.group_sex = 2
      call character_location_return(hannah) from _call_character_location_return_680
      end_day notify
  return

# Contact - Check on Whore
label hannah_check_whore:
  ## Principal Whore
  if hannah.whore_count > 2:
    wt_image principal_office_19
    player.c "How's my favorite professional?"
    hannah.c "The only thing I'm a professional at is teaching.  And things are going fine at the school now, thank you."
    player.c "Professional fundraiser, then?  It is your fund raising efforts that are getting the school back on its feet, isn't it?"
    hannah.c "Yes"
    player.c "Ironic, considering you're not on your feet when you raise the money.  Not often anyway.  Not holding out on me, are you?  The cut you send me each week sure is skinny."
    wt_image principal_office_1
    hannah.c "I'm selling my body to raise money to keep our school going, and you're worried about your fee?"
    player.c "That, and making sure you're okay.  If you get into trouble, you let me know.  I'll look out for you."
    hannah.c "Such service."
    player.c "Just looking after my favorite professional."
    $ hannah.whore_lost_countdown = 8
  elif not hannah.has_tag('domme') and hannah.whore_count <= 2:
    wt_image principal_office_19
    player.c "How's my favorite professional?"
    hannah.c "The only thing I'm a professional at is teaching.  I don't know if I'm ready for this yet."
    player.c "I was just making sure you're okay.  If you get into trouble, you let me know.  I'll look out for you."
    hannah.c "Such service."
    player.c "Just looking after my favorite professional."
  ## Principal Domme
  if hannah.has_tag('domme') and hannah.domme_outfit_count > 3:
    wt_image banker_school_2_18
    player.c "How's life as a Domme, Principal Hannah?"
    hannah.c "Good, thank you.  I do find I enjoy this work, and of course I love the extra money its bringing in. Our school recreational programs have never been better funded."
    player.c "Perhaps you could start paying me my normal management fee?"
    hannah.c "No.  This is fund raising work, so you'll have to settle for what I'm willing to share, to cover your administrative costs."
  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_hannah:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_hannah:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_hannah:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_hannah:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_hannah:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_hannah:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_hannah:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_hannah:
  if hannah.in_area('house') and not hannah.has_tag('doll') and not hannah.has_tag('offered_potion'):
    player.c "Let me pour you something to drink."
    hannah.c "No thanks.  I don't have time.  I need to get to the school.  Once you and I ... you know."
    player.c "Something to relax you perhaps?  Or perk you up?"
    hannah.c "Really, no."
    add tags 'offered_potion' to hannah
  else:
    "Best to save this for someone else."
  return

# Give Transformation Potion
label give_tp_hannah:
  if hannah.in_area('house') and not hannah.has_tag('doll') and not hannah.has_tag('offered_potion'):
    player.c "Let me pour you something to drink."
    hannah.c "No thanks.  I don't have time.  I need to get to the school.  Once you and I ... you know."
    player.c "Something to relax you perhaps?  Or perk you up?"
    hannah.c "Really, no."
    add tags 'offered_potion' to hannah
  else:
    "Best to save this for someone else."
  return

# Give Ring of Secuality
label give_rs_hannah:
    "That may work, but there's no content for it, so you're better off saving this for someone else."
    return


# Use Water Bowl
label use_wb_hannah:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_hannah:
    if hannah.has_tag('doll'):
        "You should try this on someone else.  Someone who still has a mind for it to tame."
    elif hannah.has_tag('transformed'):
        "Hannah has already been transformed.  There's nothing more the Will-Tamer can do to her now."
    elif hannah.will_tamer_count == 0:
        "Wait until she's ready."
    elif hannah.has_tag('will_tamer_this_week'):
        "You've already used the Will-Tamer her on this week.  The re-wiring of her brain it has started will take some time to complete.  Try again next week."
    elif current_location in session_locations:
        "You'll need to talk to her to find out if she's willing to let you use it on her."
    else:
        "Not here."
    return

########### TIMERS ###########
## Common Timers
# Start Day
label hannah_start_day:
  if gloria.discussed_principal == 2:
    call hannah_visit_gloria from _call_hannah_visit_gloria
  ## End Day - Principal Event
  elif day == hannah.visit_day and week > hannah.visit_week and hannah.visit_week > 0 and hannah.can_be_interacted:
    # End Day - Principal Event: Booty call? (must precede Letter event)
    if hannah.letter_re_terri == 7:
      wt_image front_door
      "There's a knock at your front door."
      summon hannah
      wt_image principal_booty_call_1_1
      if hannah.booty_call_count == 0:
        "It's Hannah, the School Principal.  The large sunglasses are presumably an attempt to arrive at your house without being recognized.  As you open the door, she pushes them up into her hair and smiles at you."
        hannah.c "Hi.  I just dropped by because ... well, I was wondering if you meant it when you said I was welcome to come by and see you from time to time?"
      else:
        if hannah.marilyn_solution_thank_you == 1:
          hannah.c "Hi!  It's me.  I don't know how you did it, but the government has increased our budget substantially!"
          "That was fast."
          hannah.c "We finally have enough money to run the school properly. Thank you so much!"
          hannah.c "Ummm, maybe I could come in and we could celebrate before I need to go to school?"
          add tags 'thank_you_visit' to hannah
        elif hannah.has_tag('need_bethany_thank_you'):
          rem tags 'need_bethany_thank_you' from hannah
          hannah.c "Hi!  It's me.  Bethany's working out really well. The school's finances are back in better shape and ... well ... I thought maybe we could celebrate before I need to go to school?"
        else:
          hannah.c "Hi!  It's me. I was just on my way to work and thought I'd drop to see you.  That is, if you have a few minutes for me?"
      $ title = "Let her in?"
      menu:
        "Of course":
          player.c "Come on in."
          summon hannah to living_room
          add tags 'booty_call' to hannah
        "I was just messing with you" if hannah.booty_call_count == 0:
          player.c "I was just being polite, Hannah.  I didn't mean it."
          hannah.c "Oh.  I ... Okay.  Fine then.  Good bye."
          $ hannah.letter_re_terri = 4
          $ hannah.visit_week = 0
          call character_location_return(hannah) from _call_character_location_return_681
        "Today's not a good day" if hannah.booty_call_count != 0:
          player.c "Today's not a good day, Hannah."
          hannah.c "No problem. I understand. Maybe some other time?"
          $ title = "Ask her to come back?"
          menu:
            "Sure, another time would be fine":
              player.c "Another time would be great, Hannah."
              hannah.c "Okay. Have a good day."
              $ hannah.random_number = renpy.random.randint(1, 10)
              if hannah.random_number < 5:
                $ hannah.visit_week += 1
              else:
                $ hannah.visit_week += 2
            "I don't think that's a good idea":
              player.c "I don't think that's a good idea, Hannah."
              hannah.c "Oh. I see. Well, alright. I guess this is good-bye then."
              player.c "Good bye."
              $ hannah.letter_re_terri = 4
              $ hannah.visit_week = 0
              rem tags 'ready_for_sex_at_school' from hannah
          call character_location_return(hannah) from _call_character_location_return_682
    # End Day - Principal Event: Thank you post Marilyn and not continuing actions yet?
    elif hannah.marilyn_solution_thank_you == 1 and hannah.letter_re_terri != 7:
      wt_image front_door
      "There's a knock at your front door."
      summon hannah
      wt_image principal_apology_1
      "It's Hannah the School Principal."
      hannah.c "Hi, I just wanted to stop by to thank you.  I don't know how you did it, but the government has increased our budget substantially!"
      "That was fast."
      hannah.c "We finally have enough money to run the school properly. I can't tell you how much I appreciate your help."
      $ title = "Invite her in?"
      menu:
        "Please come in":
          player.c "You're very welcome, Hannah. Won't you please come in?"
          # bad experience before?
          if hannah.letter_re_terri > 9:
            hannah.c "No thank you. I remember what happened the last time I was here, and I'm not interested in a repeat."
            hannah.c "Despite that, I am grateful for your assistance and I wanted you to know that.  Good bye."
            "You're not likely to see her again."
            # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
            # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
            # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
            #call convert(hannah, "unavailable")
            $ hannah.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with the school may not be needed going forward; should ideally be cleaned up
            call character_location_return(hannah) from _call_character_location_return_683
          else:
            hannah.c "Okay, but just for a minute. I need to get to the school."
            wt_image principal_apology_2
            "She comes in and takes a seat."
            summon hannah to living_room
            add tags 'thank_you_visit' to hannah
        "Send her on her way":
          "You accept her thanks and send her on her way. Now you can get on with your day."
          wt_image current_location.image
          call character_location_return(hannah) from _call_character_location_return_684
    # End Day - Principal Event: Lawyer call?
    elif hannah.letter_re_terri == 8 or hannah.letter_re_terri == 9:
      wt_image front_door
      "There's a knock at your front door."
      summon hannah
      wt_image principal_apology_1
      if hannah.letter_re_terri == 8:
        "It's Hannah the School Principal."
        hannah.c "Can I come in? I need to speak to you about the letter I sent you."
      else:
        hannah.c "My name is Hannah. I'm the Principal at the local school.  Can I come in?  I need to speak to you about the letter I sent you."
      wt_image principal_apology_2
      "You show her in and she takes a seat."
      summon hannah to living_room
      add tags 'lawyer_call' to hannah
    # End Day - Principal Event: Letter event?
    elif hannah.letter_re_terri == 1 and hannah.lost_money_and_no_fix == 0:
      call hannah_first_school_visit from _call_hannah_first_school_visit
  ## End Day - Principal Visit to Club Pres?
  if not hannah.has_tag('no_hypnosis'):
      add tags 'no_hypnosis' to hannah
  return

# End Day - Principal Event: Booty call? (must precede Letter event)
label hannah_booty_call:
  $ hannah.add_tags('trained_today', 'trained_this_week', 'booty_call_in_progress')
  $ hannah.booty_call_count += 1
  # follow up on foot job promise or else scroll from 1 to 2 and continue with normal visit
  if hannah.booty_call_count > 2:
    if hannah.foot_job == 3:
      $ hannah.foot_job = 1
      wt_image principal_booty_call_2_1
      "Hannah drops down in front of you and takes out your cock."
      wt_image principal_booty_call_2_14
      hannah.c "So, last time you said you'd let me give you a foot job. Remember?"
      $ hannah.footjob_reject = False
      $ title = "What do you tell her?"
      menu menu_hannah_booty_call_footjob:
        "Yes, a foot job is fine":
          call hannah_booty_call_footjob from _call_hannah_booty_call_footjob
        "How about another blow job instead" if not hannah.footjob_reject:
          player.c "How about another blow job instead?"
          hannah.c "No. You said last time you'd let me try this. This is supposed to be about both of us, not just what you want."
          $ hannah.footjob_reject = True
          jump menu_hannah_booty_call_footjob
        "Not interested" if hannah.footjob_reject:
          player.c "Suck me or fuck me Hannah, but keep your dirty feet out of this. I'm not interested in you putting them on me."
          wt_image principal_booty_call_1_11
          hannah.c "Why didn't you say that before, instead of telling me we'd do that this time.  Jerk!"
          wt_image current_location.image
          "Hannah dresses and storms off. At least the silly woman won't be bothering you at your house any more."
          $ hannah.foot_job = 4
          $ hannah.visit_week = 0
          $ hannah.letter_re_terri = 4
    else:
      $ hannah.booty_call_count = 1
  if hannah.booty_call_count == 1:
    wt_image principal_booty_call_1_38
    if hannah.will_tamer_count > 1:
      wt_image principal_booty_call_1_11
      "Hannah excuses herself and ducks into your washroom.  She reappears wearing very little.  She smiles at you, and then a wave of confusion seems to cross her face."
      wt_image principal_booty_call_1_37
      hannah.c "Did you ... did you plan on putting the collar on me again?"
      player.c "Do you want me to put the collar on you?"
      wt_image principal_booty_call_1_2
      hannah.c "No!"
      player.c "If I wanted you to wear it, to make me happy, would you do so?"
      wt_image principal_booty_call_1_21
      hannah.c "I ..."
      "She seems unable to answer."
    else:
      wt_image principal_booty_call_1_11
      "Hannah immediately excuses herself and ducks into your washroom.  She reappears wearing very little."
      wt_image principal_booty_call_1_2
      hannah.c "This outfit is a little slutty, I know.  But, well, this is a booty call, so slutty didn't seem inappropriate."
      "She looks at you, waiting for you to make the first move."
    $ title = "What do you want?"
    menu menu_hannah_booty_call_outfit_1:
      "Blow job":
        wt_image principal_booty_call_1_3
        "As you remove your cock from your pants, Hannah smiles and drops to her knees in front of you."
        hannah.c "I suppose I can guess what you want me to do with this?"
        if not hannah.has_tag('instructed_to_lick_balls'):
          wt_image principal_booty_call_1_4
          "She leans in and gently licks the underside of your cock ..."
          wt_image principal_booty_call_1_5
          "... then takes you into her mouth for a nice, gentle suck session."
        else:
          wt_image principal_booty_call_1_4
          "She leans in and gently licks the underside of your cock."
          wt_image principal_booty_call_1_7
          "Then remembering what you told her before, she gives your balls a thorough washing with her tongue ..."
          wt_image principal_booty_call_1_5
          "... before popping you into her mouth for a nice, gentle suck session."
        wt_image principal_booty_call_1_6
        hannah.c "I want to feel you inside me.  This is nice but I'm horny, too, and want to cum."
        $ hannah.blowjob_count += 1
        $ title = "What do you do?"
        menu menu_hannah_booty_call_blowjob:
          "Tell her to lick your balls first" if not hannah.has_tag('instructed_to_lick_balls'):
            wt_image principal_booty_call_1_39
            player.c "I like to have my balls licked when my cock is being sucked."
            hannah.c "Oh.  Okay.  Like this?"
            wt_image principal_booty_call_1_40
            "She gives your balls a nice tongue bath.  She makes no move to continue sucking you, however, and its clear she wants you to do something to get her off now."
            add tags 'instructed_to_lick_balls' to hannah
            jump menu_hannah_booty_call_blowjob
          "Missionary":
            call hannah_booty_call_outfit_1_missionary from _call_hannah_booty_call_outfit_1_missionary
          "Take her from behind":
            call hannah_booty_call_outfit_1_behind from _call_hannah_booty_call_outfit_1_behind
          "Tell her it's all about you today" if not hannah.has_tag('insist'):
            player.c "Let's make this all about me today, Hannah.  You go back to sucking me off properly and I'll reward you with a nice, hot load of my cum."
            if hannah.will_tamer_count > 0:
              wt_image principal_booty_call_1_4
              "You can see the struggle inside of Hannah.  She's not a submissive woman by nature, and while she's happy to serve those that she cares about like the children at her school, she came here today because she's horny and has her own needs she wanted met."
              wt_image principal_booty_call_1_41
              "The influence of the Will-Tamer, however, is amplifying her willingness to serve.  You give her a psyche a little nudge towards submission, running your hand gently over her head, stroking her hair as you speak to her."
              wt_image principal_booty_call_1_42
              player.c "You don't mind serving me, do you Hannah?  Dropping by my house to suck me off before you go to work. You know how happy it'll make me to have you do that.  Work your mouth up and down my cock and suck me off, Hannah."
              wt_image principal_booty_call_1_8
              "To her own surprise, she puts her own desires aside and focuses exclusively on yours.  She keeps her eyes locked on your face, searching for signs that you're enjoying the blow job.  She doesn't have to wait long for proof that you are indeed enjoying this."
              wt_image principal_booty_call_1_43
              player.c "Take my cock out, Hannah, and keep stroking it.  I'm going to cum on you."
              wt_image principal_booty_call_1_9
              player.c "[player.orgasm_text]"
              wt_image principal_booty_call_1_10
              player.c "Wasn't that nice, Hannah?  Aren't you glad you dropped by to see me?"
              hannah.c "Y ... yes?"
              player.c "Better get cleaned up now.  You don't want to be late for school, do you?"
              hannah.c "No"
              $ hannah.blowjob_count += 1
              $ hannah.facial_count += 1
              orgasm notify
            else:
              wt_image principal_booty_call_1_3
              hannah.c "What?  Are you joking?  Don't be a jerk.  Let's do something we'll both enjoy."
              add tags 'insist' to hannah
              jump menu_hannah_booty_call_blowjob
          "Insist that she suck you off" if hannah.has_tag('insist'):
            player.c "No, Hannah.  I said I want this to be all about me today."
            wt_image principal_booty_call_1_11
            hannah.c "Jerk!"
            wt_image current_location.image
            "Hannah dresses and storms off.  At least the silly woman won't be bothering you at your house any more."
            $ hannah.visit_week = 0
            $ hannah.letter_re_terri = 4
          "Tell her you first then her":
            player.c "Your mouth feels so good.  Suck me off first, Hannah, then I'll get you off."
            wt_image principal_booty_call_1_12
            hannah.c "Okay, I guess we could do that."
            wt_image principal_booty_call_1_13
            "She goes back to sucking your cock, with greater intensity now that her objective is to get you off rather than just to tease you to hardness.  It doesn't take her long to succeed."
            $ title = "Where do you want to cum?"
            menu:
              "On her face":
                wt_image principal_booty_call_1_8
                player.c "Take me out.  I want to cum on your face."
                wt_image principal_booty_call_1_14
                hannah.c "What?  No.  I have to go to the school after this.  Just cum in my mouth."
                if hannah.will_tamer_count > 0:
                  "Despite her words, you see a slight hesitation as she looks at you.  Hannah's not a submissive woman by nature, but she is happy to serve those that she cares about like the children at her school."
                  wt_image principal_booty_call_1_41
                  "The influence of the Will-Tamer is amplifying her willingness to serve. You give her a psyche a little nudge towards submission, running your hand gently over her head, stroking her hair as you speak to her."
                  player.c "My cum will feel good against your skin, Hannah.  More importantly, it'll make me happy to see you finish me off like that.  Take my cock out of your mouth and stroke it with your hand, Hannah."
                  wt_image principal_booty_call_1_43
                  player.c "Keep stroking my cock, Hannah.  Hold it there in front of your face and keep stroking."
                  wt_image principal_booty_call_1_12
                  player.c "That's it, Hannah, keep stroking me just like that.  I'm going to cum on you."
                  wt_image principal_booty_call_1_9
                  player.c "[player.orgasm_text]"
                  wt_image principal_booty_call_1_10
                  player.c "That was nice, wasn't it Hannah?  Pleasuring me like that, it was exciting for you, wasn't it?"
                  hannah.c "Y ... yes?"
                  player.c "Being able to serve me like that was it's own reward, wasn't it? You don't even need me to get you off now, do you? That was fulfilling enough just as it was. Better get cleaned up now. You don't want to be late for school, do you?"
                  hannah.c "No"
                  $ hannah.facial_count += 1
                else:
                  call hannah_booty_call_outfit_1_cum_in_mouth from _call_hannah_booty_call_outfit_1_cum_in_mouth
              "In her mouth":
                call hannah_booty_call_outfit_1_cum_in_mouth from _call_hannah_booty_call_outfit_1_cum_in_mouth_1
            $ hannah.blowjob_count += 1
            orgasm notify
      "Eat her out":
        call hannah_booty_call_outfit_1_eat from _call_hannah_booty_call_outfit_1_eat
      "Missionary":
        call hannah_booty_call_outfit_1_missionary from _call_hannah_booty_call_outfit_1_missionary_1
      "Take her from behind":
        call hannah_booty_call_outfit_1_behind from _call_hannah_booty_call_outfit_1_behind_1
      "Anal" if hannah.anal == 1:
        player.c "Bend over, Principal Hannah. I'm going to fuck you in the ass again."
        wt_image principal_booty_call_1_30
        hannah.c "Oohhh"
        "She seems simultaneously scared and excited at the prospect."
        wt_image principal_booty_call_1_31
        "She trembles as the lubricant lands on her skin. You're pretty sure its from the thought of where the lube is going, rather than the coolness of the liquid itself ..."
        wt_image principal_booty_call_1_32
        "...a suspicion that's confirmed when she starts to shake as you push the lube into her ass with your finger."
        player.c "Nervous?"
        hannah.c "Yes"
        player.c "But you want me to continue, don't you?"
        hannah.c "Oh yes!"
        player.c "Tell me you want my big cock in your ass."
        hannah.c "I do.  I want to feel your big cock filling my ass again."
        wt_image principal_booty_call_1_33
        player.c "Climb on up then.  Put me inside you."
        hannah.c "Oohhh  ... Ooohhhhhh!!!"
        "Her moan as she lowers herself onto you is replaced by a much louder groan as she feels the head of your cock pass through her sphincter ring."
        wt_image principal_booty_call_1_34
        player.c "Ride me now, Hannah.  Fuck my cock with your ass."
        hannah.c "Oohhh  ...  ooohhh ...  ooohhh  ...  ooohhh  ...  ooohhh ..."
        "Up and down she rides you, raising herself up with her legs, then letting gravity pull her down on your cock, each downstroke penetrating a little deeper and eliciting a new groan out of her."
        wt_image principal_booty_call_1_35
        "When the trembling in her tired legs slows the speed of her strokes, you turn her around so you can use your arms to steady her and guide her pace."
        hannah.c "Oooohhhhh   ...  ooooohhhhhh  ...  oooooohhhhhhhh  ..."
        wt_image principal_booty_call_1_36
        "Hannah reaches down with her hand and rams a finger into herself as she rubs her clit, bringing herself to orgasm. The feel of her body climaxing with your cock in her ass brings you over the edge too."
        hannah.c "Oooooohhhhhh ooohhhhhhhh FUUCCCKKKKK!!!"
        player.c "[player.orgasm_text]"
        wt_image principal_booty_call_1_21
        hannah.c "Wow. That was naughty and dirty and sexy and nice all at the same time."
        if hannah.lost_money_and_no_fix != 1:
          "Hannah dresses and heads to the school, seemingly happy."
        $ hannah.anal_count += 1
        $ hannah.orgasm_count += 1
        orgasm
      "Use the Will-Tamer on her" if hannah.will_tamer_count > 0 and player.has_item(will_tamer) and not hannah.has_tag('will_tamer_this_week'):
        call hannah_will_tamer_timer from _call_hannah_will_tamer_timer_1
  elif hannah.booty_call_count == 2:
    if hannah.foot_job == 0:
      wt_image principal_booty_call_2_1
      "Hannah's in a take charge mood this morning.  She drops to her knees in front of you, pulls off her top, and takes out your cock."
      hannah.c "You have a beautiful cock. I really like the look of it."
      wt_image principal_booty_call_2_2
      "She seems to like the taste of it, too."
      wt_image principal_booty_call_2_3
      hannah.c "There's something I've always wanted to try with a guy.  Is it okay if I tell you what it is?"
      "You nod.  With her soft hand and softer tongue on your cock and her big eyes looking up at you, if she'd asked if it was okay if you both jumped off a bridge, you'd have nodded."
      wt_image principal_booty_call_2_4
      hannah.c "This is a little weird, but I've often wondered what it would be like to get a guy off with just my feet. Do you mind if we experiment with that?"
      $ title = "What do you say?"
      menu:
        "Yes, a foot job is fine":
          $ hannah.foot_job = 1
          call hannah_booty_call_footjob from _call_hannah_booty_call_footjob_1
        "No, just blow me":
          wt_image principal_booty_call_2_11
          player.c "Don't be weird, Hannah.  Just blow me."
          wt_image principal_booty_call_2_2
          "She says nothing, just wraps her lips back around your cock and finishes the blow job.  It's nice, and you soon cum."
          player.c "[player.orgasm_text]"
          wt_image principal_booty_call_2_5
          "She swallows your load, then looks up at you.  The pout on her face is even cuter with the traces of your cum glistening her lips."
          hannah.c "I'd hoped you'd be a little more adventurous."
          $ hannah.blowjob_count += 1
          $ hannah.swallow_count += 1
          orgasm
          $ title = "What do you tell her?"
          menu:
            "We'll do a foot job next time":
              player.c "We'll do a foot job next time, Hannah.  You just caught me off guard.  Besides, your mouth felt so good, I didn't want you to stop what you were doing."
              wt_image principal_happy_1
              hannah.c "Okay.  Next time will be fine!"
              $ hannah.foot_job = 3
            "I just don't like foot jobs":
              player.c "I'm happy to experiment with you, Hannah.  I just don't like foot jobs."
              hannah.c "So if I wanted to try something else, you'd be okay with that?"
              player.c "Maybe, depending on what it is.  What did you have in mind?"
              hannah.c "I'm not sure.  But you're okay if I suggest doing new things with you?"
              player.c "Yes.  Just don't bring up feet again, okay?"
              wt_image principal_happy_1
              hannah.c "Okay"
              $ hannah.foot_job = 2
            "I'm only interested in straight fucking and sucking":
              player.c "I'm only interested in straight fucking and sucking, Hannah.  Nothing kinky."
              hannah.c "Okay. I get that. I think I was expecting that maybe you might be a bit more adventurous. Maybe this was a mistake. I should go."
              $ hannah.foot_job = 4
              $ hannah.visit_week = 0
              $ hannah.letter_re_terri = 4
    elif hannah.anal == 0:
      wt_image principal_booty_call_3_1
      "Hannah starts pulling off her clothes as soon as she steps inside."
      hannah.c "There's something I'd like to do with you today.  Something new."
      wt_image principal_booty_call_3_10
      hannah.c "As long as you don't think its too weird or disgusting ..."
      wt_image principal_booty_call_3_2
      hannah.c "... I'd really like it if you'd put your cock in my ass.  I know that's really dirty and nasty, but that's probably why the thought of it excites me."
      $ title = "What do you tell her?"
      menu:
        "Of course I'll fuck your ass":
          player.c "Of course I'll fuck your ass, Hannah."
          wt_image principal_booty_call_3_11
          hannah.c "Oh good!  I brought some lube."
          wt_image principal_booty_call_3_12
          "Even with the lube, it's a slow process to work your cock into her tight ass."
          wt_image principal_booty_call_3_13
          hannah.c "Ohhh ... is it going to fit?"
          wt_image principal_booty_call_3_14
          player.c "Just take a moment.  Relax your sphincter.  Let it take me inside."
          wt_image principal_booty_call_3_3
          "She groans as the head of your cock slips through her tight ring."
          hannah.c "Oh ....  oooohhhh!"
          wt_image principal_booty_call_3_16
          "As she slowly stretches to accommodate you, a continual moan escapes her throat."
          hannah.c "ooohhhhhhh"
          wt_image principal_booty_call_3_15
          "Eventually, her ass opens enough to let you start fucking her gently."
          hannah.c "Oohhh  oohhh  oohhh"
          wt_image principal_booty_call_3_17
          player.c "Touch yourself, Hannah.  Cum for me with my cock in your ass."
          wt_image principal_booty_call_3_18
          "She reaches down and caresses herself ..."
          wt_image principal_booty_call_3_19
          "... then slips two fingers inside and finger fucks herself as you ream her.  It doesn't take long for the combination of sensations to take her over the edge."
          wt_image principal_booty_call_3_20
          hannah.c "Ooohhhh Oohhh FUUCCCKKKK!!!"
          "There's no reason to hold back your own orgasm.  You let yourself go, flooding her bowels with your cum."
          wt_image principal_booty_call_3_21
          player.c "[player.orgasm_text]"
          wt_image principal_booty_call_3_22
          hannah.c "Thanks for doing that with me. I love that I can be adventurous with you and tell you the dirty things I'd like to try, without being judged."
          $ hannah.anal_count += 1
          $ hannah.orgasm_count += 1
          $ hannah.anal = 1
          orgasm
        "No way":
          player.c "Don't be disgusting, Hannah.  I'm not putting my cock in your dirty shithole."
          wt_image principal_booty_call_3_10
          hannah.c "Sorry, I didn't mean to turn you off.  Some guys like that, I think."
          player.c "I'm sure they do, Hannah.  What I'd like is for you to get me hard, then let's have sex the regular way."
          wt_image principal_booty_call_3_7
          "Principal Hannah takes out your cock ..."
          wt_image principal_booty_call_3_23
          "... and sucks you hard."
          wt_image principal_booty_call_3_24
          "Then she leans back ..."
          wt_image principal_booty_call_3_25
          "... and lets you fuck her."
          wt_image principal_booty_call_3_8
          "She seems preoccupied, likely still thinking about opening up to you about her sexual wants and being rejected.  It's clear she's not going to cum today"
          wt_image principal_booty_call_3_26
          "You're not going to have any such problem.  You pull out before you do, though ..."
          wt_image principal_booty_call_3_27
          "... and finish by depositing your load over her pretty pussy."
          player.c "[player.orgasm_text]"
          wt_image principal_booty_call_3_9
          if hannah.foot_job == 2:
            hannah.c "That was nice, but I think I was expecting that maybe you might be a bit more adventurous.  Maybe this was a mistake.  I should go."
            $ hannah.visit_week = 0
            $ hannah.letter_re_terri = 4
          else:
            hannah.c "Sorry I grossed you out by suggesting anal.  I get how that wouldn't be for everybody."
            wt_image principal_booty_call_3_28
            hannah.c "At least you did let me experiment by giving you a foot job before.  Hopefully we can find some other fun things we'll both enjoy trying together."
          $ hannah.sex_count += 1
          $ hannah.anal = 2
          orgasm
    else:
      $ hannah.temporary_count = 1
      wt_image principal_booty_call_1_1
      hannah.c "Maybe we could do something naughty today?"
      while hannah.temporary_count >= 1:
        # preliminary conversation before choice menu, if applicable
        if hannah.group_sex == 0 or hannah.group_sex == 2:
          # this test is so you only get the preliminary conversation once
          if hannah.temporary_count == 1:
            $ hannah.temporary_count = 2
            if hannah.group_sex == 0:
              hannah.c "I have a dirty confession to make. I've been thinking about how hot it would be to have sex with more than one man."
              hannah.c "I know we can't do that today, but I would love it if sometime you could get together a group of men who wanted to all fuck me at the same time."
            else:
              hannah.c "I have to tell you, I loved the group sex you set up for me."
              hannah.c "Can I tell you something even dirtier?  I'd love to try that again, but this time, I'd like it to be a fake 'forced' scene."
              hannah.c "I don't really want to be hurt, of course, and I don't know if there would be any way for you to set it up so that I'd be safe. But the idea of a rough gang of burly men having their way with me is insanely hot."
        $ title = "What do you suggest?"
        menu:
          "Set up a group sex scene for her" if hannah.group_sex == 0 or hannah.group_sex == 2:
            if hannah.group_sex == 0:
              player.c "I could set up a group scene for you."
              hannah.c "Would you really?"
              player.c "Sure. You'll just need to give me a few days."
              hannah.c "I can't wait! But what should we do today?"
              $ hannah.group_sex = 1
            else:
              player.c "Let me see what I can put together for you."
              hannah.c "Really?  You're going to try and set that up?"
              player.c "Sure. You'll just need to give me a few days."
              "Now you just need to find someone with a group of burly men you can be sure will stay under control."
              hannah.c "I can't wait! But what should we do today?"
              add tags 'marilyn_talk_option_possible' to hannah
              $ hannah.group_sex = 3
          "Invite her to the next Club Masquerade Ball" if gloria.ball_outfit > 0 and hannah.group_sex > 0 and not hannah.has_tag('masquerade_ball_invite'):
            player.c "How would you like to join me for a sex party at my private Club?"
            hannah.c "I couldn't.  Someone might recognize me."
            player.c "Not during one of the Club's Masquerade Balls, they wouldn't.  And besides, it's all very hush hush.  No one will know it's you, and even if they did, no one would say anything.  There are some pretty important people at the Club and the confidentiality rules are strictly enforced."
            hannah.c "Well, anonymous sex does sound kind of naughty, and kind of hot.  If you think it's safe, I wouldn't mind joining you sometime.  But what are we going to do today?"
            add tags 'masquerade_ball_invite' to hannah
          "Sex at her school" if not hannah.has_tag('ready_for_sex_at_school'):
            player.c "I'll tell you what I think would be hot. I drop by your school while you're working and fuck you in your office."
            hannah.c "We couldn't! There's too many children, and other staff members."
            player.c "You have a private office, right?"
            hannah.c "Yes, but ..."
            player.c "So you close the door and we do things really quick and quietly, and then you go back to work."
            hannah.c "That seems so..."
            player.c "Naughty?  Dirty?"
            hannah.c "Yes ... and hot.  Okay, I'll think about it.  But what should we do today?"
            add tags 'ready_for_sex_at_school' 'available_for_school_visit' to hannah
          "Watch her masturbate":
            if hannah.masturbation_count == 0:
              player.c "Take your clothes off and have a seat."
              wt_image principal_booty_call_8_3
              hannah.c "Okay.  What are you going to do with me when I'm naked?"
              wt_image principal_booty_call_8_4
              player.c "Just watch you."
              wt_image principal_booty_call_8_1
              hannah.c "Watch me?  Watch me do what?"
              wt_image principal_booty_call_8_5
              player.c "Touch yourself."
              wt_image principal_booty_call_8_2
              hannah.c "You want me to play with myself?"
              wt_image principal_booty_call_8_6
              player.c "While I watch you, yes."
              wt_image principal_booty_call_8_7
              hannah.c "I don't think I can."
              player.c "Of course you can.  You've been doing it since you were a schoolgirl, haven't you?"
              wt_image principal_booty_call_8_8
              hannah.c "Not with an audience I haven't!"
              wt_image principal_booty_call_8_9
              player.c "It's even more fun with an audience.  Spread your legs."
              wt_image principal_booty_call_8_10
              player.c "Don't be shy.  Open up."
              wt_image principal_booty_call_8_11
              player.c "That doesn't count."
              hannah.c "But I'm touching myself, just like you asked."
              wt_image principal_booty_call_8_12
              player.c "You've been spending too much time on the school playground, resorting to that type of logic.  Wet your finger, then touch yourself properly."
              wt_image principal_booty_call_8_13
              hannah.c "This is embarrassing."
              wt_image principal_booty_call_8_14
              player.c "Also hot.  It's turning me on, seeing you play with yourself."
              hannah.c "Really?"
              wt_image principal_booty_call_8_15
              player.c "Really.  You're incredibly sexy, Hannah.  Keep your legs open wide and give me a good show."
              wt_image principal_booty_call_8_16
              player.c "Tell me what you're doing, Hannah, and let me see you as you do it."
              wt_image principal_booty_call_8_17
              hannah.c "ooohhhhh ... I'm rubbing my pussy and my clit while you watch me."
              player.c "Is that how you get yourself off when you're alone?"
              wt_image principal_booty_call_8_18
              hannah.c "ooohhhhh ... to get myself excited, yes.  Then I finger-fuck myself while I rub my clit, like this."
              wt_image principal_booty_call_8_19
              hannah.c "ooohhhhh ... ooohhhh ..."
              wt_image principal_booty_call_8_20
              hannah.c "... oohhhh FUUCCKKKKK!!!!"
              wt_image principal_booty_call_8_8
              hannah.c "Well, that was different!  You're full of surprises, aren't you?"
            else:
              player.c "I want to watch you play with yourself again.  Get your clothes off and have a seat in front of me."
              wt_image principal_booty_call_8_3
              hannah.c "Oh, come on!  Not again?"
              wt_image principal_booty_call_8_5
              hannah.c "I could have stayed home and played with myself."
              wt_image principal_booty_call_8_6
              player.c "What fun would that be, without an audience?"
              wt_image principal_booty_call_8_21
              hannah.c "It is more fun when you're watching, that's true.  But it's even more fun when you're touching me."
              wt_image principal_booty_call_8_9
              hannah.c "If I give you a good show today, will you touch me the next time I come over?"
              wt_image principal_booty_call_8_10
              player.c "Maybe, if it's a really good show."
              wt_image principal_booty_call_8_12
              hannah.c "I'll do my best."
              wt_image principal_booty_call_8_16
              "With little hint of shyness this time, she begins rubbing herself as you watch."
              wt_image principal_booty_call_8_17
              "Before long you can see she's getting wet."
              wt_image principal_booty_call_8_18
              "Not long after that, she slips a finger inside ..."
              wt_image principal_booty_call_8_19
              "... and begins finger-fucking herself as she moans."
              hannah.c "ooohhhhh ... ooohhhh ..."
              wt_image principal_booty_call_8_20
              hannah.c "... oohhhh FUUCCKKKKK!!!!"
              wt_image principal_booty_call_8_24
              hannah.c "I think that counts as a pretty good show.  I don't let just any guy watch me do that."
            player.c "Aren't you going to clean your finger?"
            if hannah.will_tamer_count == 0:
              wt_image principal_booty_call_8_21
              hannah.c "Of course, I will.  In the bathroom, before I go."
            else:
              wt_image principal_booty_call_8_13
              hannah.c "You mean ..."
              player.c "Yes, Hannah.  Make a nice show of it."
              wt_image principal_booty_call_8_22
              "She puts her finger in her mouth ..."
              wt_image principal_booty_call_8_23
              "... and licks her juices off for your entertainment before she leaves."
            $ hannah.masturbation_count += 1
            change player energy by -energy_very_short
            $ hannah.temporary_count = 0
          "Tit job":
            player.c "How about a tit job?"
            hannah.c "I'm not very big up top, but I could try."
            wt_image principal_booty_call_4_1
            "Hannah removes her clothes and takes out your cock."
            wt_image principal_booty_call_4_7
            "She strokes her hand up and down your shaft ..."
            wt_image principal_booty_call_4_6
            "... before putting you in her mouth and sucking you fully hard."
            wt_image principal_booty_call_4_3
            "Then she squeezes you between her breasts, her tits just barely forming a large enough valley to wrap around your cock."
            wt_image principal_booty_call_4_10
            hannah.c "Does this feel good?"
            player.c "Yes.  Keep going like that."
            wt_image principal_booty_call_4_4
            "Up and down Hannah pumps your cock with her soft tits."
            hannah.c "Don't make a mess.  I need to go to work from here.  I'll take you in your mouth when you're ready to cum."
            $ title = "Where do you want to cum?"
            menu:
              "In her mouth":
                wt_image principal_booty_call_4_8
                "As you start to cum, Hannah leans forward and wraps her soft lips around your cock, taking your jizz into her mouth."
                player.c "[player.orgasm_text]"
                wt_image principal_booty_call_4_9
                hannah.c "Mmmmm.  That was fun!  I need to get going now."
                wt_image principal_booty_call_4_12
                "Hannah dresses and leaves, seemingly happy with the morning protein supplement you provided."
                $ hannah.swallow_count += 1
              "On her face":
                wt_image principal_booty_call_4_10
                player.c "Just keep going like that, I'm going to cum on your face."
                if hannah.will_tamer_count > 0:
                  wt_image principal_booty_call_4_3
                  "You can see her hesitating. Hannah's not a submissive woman by nature, but she is happy to serve those she cares about, like the children at her school. The influence of the Will-Tamer is amplifying her willingness to serve you, too.  You give her a psyche a little nudge towards submission, running your hand gently over her head, stroking her hair as you speak to her."
                  player.c "This is how a tit job is supposed to end, Hannah, with my cum on your face.  It'll feel good against your skin.  More importantly, it'll make me happy to see you finish me off like that.  Just keep pumping my cock with your tits, Hannah.  When I tell you I'm about to cum, lean down in front of my cock."
                  wt_image principal_booty_call_4_10
                  player.c "That's it.  I'm going to cum now, Hannah."
                  wt_image principal_booty_call_4_5
                  "She surprises herself by leaning forward to receive your hot jizz.  She didn't want a mess on her before school, but couldn't resist the need to please you."
                  player.c "[player.orgasm_text]"
                  wt_image principal_booty_call_4_11
                  "Hannah cleans herself up as best she can, then leaves for work.  She seems a little subdued, as if trying to understand her actions."
                  $ hannah.facial_count += 1
                else:
                  hannah.c "Don't be silly.  I just said I have to go to work right after this."
                  wt_image principal_booty_call_4_8
                  "As you start to cum, Hannah leans forward and wraps her soft lips around your cock, taking your jizz into her mouth."
                  player.c "[player.orgasm_text]"
                  wt_image principal_booty_call_4_9
                  hannah.c "Mmmmm.  That was fun!  I need to get going now."
                  wt_image principal_booty_call_4_12
                  "Hannah dresses and leaves, seemingly happy with the morning protein supplement you provided."
                  $ hannah.swallow_count += 1
            $ hannah.titfuck_count += 1
            orgasm
            $ hannah.temporary_count = 0
          "More anal" if hannah.anal == 1:
            player.c "More anal would be fun."
            hannah.c "Okay.  I could go for that."
            wt_image principal_booty_call_1_30
            player.c "Bend over, Principal Hannah. I'm going to fuck you in the ass again."
            hannah.c "Oohhh"
            "She seems simultaneously scared and excited at the prospect."
            wt_image principal_booty_call_1_31
            "She trembles as the lubricant lands on her skin. You're pretty sure its from the thought of where the lube is going, rather than the coolness of the liquid itself ..."
            wt_image principal_booty_call_1_32
            "... a suspicion that's confirmed when she starts to shake as you push the lube into her ass with your finger."
            player.c "Nervous?"
            hannah.c "Yes"
            player.c "But you want me to continue, don't you?"
            hannah.c "Oh, yes."
            player.c "Tell me you want my big cock in your ass."
            hannah.c "I do.  I want to feel your big cock filling my ass again."
            wt_image principal_booty_call_1_33
            player.c "Climb on up then.  Put me inside you."
            hannah.c "Oohhh  ... Ooohhhhhh!!!"
            "Her moan as she lowers herself onto you is replaced by a much louder groan as she feels the head of your cock pass through her sphincter ring."
            wt_image principal_booty_call_1_34
            player.c "Ride me now, Hannah.  Fuck my cock with your ass."
            hannah.c "Oohhh  ...  ooohhh ...  ooohhh  ... ooohhh .... ooohhh ..."
            "Up and down she rides you, raising herself up with her legs, then letting gravity pull her down on your cock, each downstroke penetrating a little deeper and eliciting a new groan out of her."
            wt_image principal_booty_call_1_35
            "When the trembling in her tired legs slows the speed of her strokes, you turn her around so you can use your arms to steady her and guide her pace."
            hannah.c "Oooohhhhh  ...  ooooohhhhhh  ...  oooooohhhhhhhh  ..."
            wt_image principal_booty_call_1_36
            "Hannah reaches down with her hand and rams a finger into herself as she rubs her clit, bringing herself to orgasm. The feel of her body climaxing with your cock in her ass brings you over the edge too."
            hannah.c "Oooooohhhhhh ooohhhhhhhh FUUCCCKKKKK!!!"
            player.c "[player.orgasm_text]"
            wt_image principal_booty_call_1_21
            hannah.c "Wow.  That was naughty and dirty and sexy and nice all at the same time."
            "Hannah dresses and heads to the school, seemingly happy."
            $ hannah.anal_count += 1
            $ hannah.orgasm_count += 1
            orgasm
            $ hannah.temporary_count = 0
          "Rough sex" if hannah.anal == 1:
            player.c "How about we get a little more physical?"
            hannah.c "What do you mean?"
            player.c "I mean I fuck your ass again, but not gentle this time.  This time I hold you down and make you my bitch."
            wt_image current_location.image
            "Hannah doesn't say anything, but she steps into your bathroom to change."
            wt_image principal_booty_call_5_1
            "She returns a moment later wearing nothing but her underwear.  Still quiet, she just watches you, wondering what you're going to do."
            player.c "Get on your knees and show me your ass.  I'm going to fuck you in the butt hole."
            wt_image principal_booty_call_5_8
            "Hannah stays silent for a moment, then replies quietly."
            hannah.c "Make me."
            wt_image principal_booty_call_5_9
            "Grabbing her by the back of the head, you push her down onto her knees."
            wt_image principal_booty_call_5_2
            player.c "Stay there while I mount you."
            hannah.c "I'm not your bitch."
            player.c "You are my bitch, and you're going to take my cock in your ass."
            wt_image principal_booty_call_5_3
            "Hannah watches you circle her, but doesn't move as you take up position behind her and remove your clothes."
            player.c "You're going to take my cock in your ass now, bitch."
            hannah.c "Make me."
            wt_image principal_booty_call_5_4
            "As you position your cock at her rosebud, she lurches forward, trying to escape. You grab her around the waist and pull her back onto your cock."
            hannah.c "Ohhh"
            wt_image principal_booty_call_5_10
            "She lurches forward again and extracts herself from you.  She almost escapes, but you grab her be the arm and pull her back."
            player.c "Trying to go somewhere?"
            wt_image principal_booty_call_5_5
            "You wrestle her onto the bed and pin her roughly beneath you with a hand around her neck."
            player.c "Stay still like a good little bitch and let me fuck your ass."
            wt_image principal_booty_call_5_11
            hannah.c "Make me."
            player.c "Okay.  Have it your way."
            wt_image principal_booty_call_5_12
            "Grabbing your belt, you wrap it around her neck to hold in her place as you shove your cock fully up her ass."
            hannah.c "Owwwww!"
            player.c "That's it.  Take my cock like the good little bitch you are."
            wt_image principal_booty_call_5_6
            "Still holding the belt tight around her neck, you use your free hand to squeeze and twist her tit painfully."
            hannah.c "Ooowww!!!"
            player.c "Go ahead.  Cry out for me.  My bitch likes it when she's fucked rough."
            wt_image principal_booty_call_5_7
            "After a couple more twists of her tit, Hannah stops fighting you, letting you settle into a proper rhythm fucking her ass."
            player.c "Who's my bitch?  Say it."
            if hannah.will_tamer_count > 0:
              "You can see her trying not to say it.  You can almost picture the influence of the Will-Tamer inside her brain, undermining her ability to resist you."
              wt_image principal_booty_call_5_13
              hannah.c "I'm your bitch ... oh!"
              "The shock of surprise on her face as she hears her own words is priceless."
              player.c "Yes, you are my bitch.  And my bitch wants my cum in her ass, doesn't she?"
              hannah.c "Yes, yes I want your cum in my ass."
              player.c "Who wants my cum in her ass?  Say it."
              hannah.c "I ..."
              player.c "No, use the right term."
              wt_image principal_booty_call_5_7
              "The struggle is back on her face.  You know the word she wants to say, but by now even she knows the words she's going to say."
              hannah.c "Your bitch.  Your bitch wants your cum in her ass."
              wt_image principal_booty_call_5_14
              player.c "[player.orgasm_text]"
              hannah.c "Ohhh ... Yes ... FUUCCCKKKK!!!"
              wt_image principal_booty_call_5_16
              "When you're done, Hannah dresses silently, then leaves for work.  She seems subdued, as if trying to understand her actions."
            else:
              wt_image principal_booty_call_5_13
              hannah.c "I'm not your bitch.  Ohhhh fuccckkkk"
              wt_image principal_booty_call_5_7
              player.c "You say you're not my bitch, but you're about to cum from me fucking your ass, aren't you bitch?"
              wt_image principal_booty_call_5_14
              hannah.c "Ohhh ... Yes ... FUUCCCKKKK!!!"
              wt_image principal_booty_call_5_13
              player.c "That orgasm earns you my cum in your ass, bitch."
              wt_image principal_booty_call_5_14
              player.c "[player.orgasm_text]"
              wt_image principal_booty_call_5_15
              hannah.c "Mmmmm. That was scary and fun at the same time. Thanks for the experience!"
            $ hannah.orgasm_count += 1
            $ hannah.anal_count += 1
            orgasm
            $ hannah.temporary_count = 0
          "Have her sit on your face":
            player.c "How about you come sit on my face?"
            wt_image principal_booty_call_3_1
            "She blushes."
            hannah.c "I guess I wouldn't say no to you pleasuring me."
            wt_image principal_booty_call_6_4
            "As you help Principal Hannah finish undress undressing, a quick check between her legs confirms that she's excited at the thought of what comes next."
            wt_image principal_booty_call_6_5
            "The smell of her arousal greets you as you lower your head between her legs."
            wt_image principal_booty_call_6_7
            "Soon she's moaning with pleasure as her sex oozes liquid onto your lapping tongue."
            wt_image principal_booty_call_6_6
            hannah.c "oohhhhhh"
            $ title = "Get her off like this?"
            menu:
              "Yes":
                wt_image principal_booty_call_6_2
                "She presses your head firmly against her sex as you lick and suckle her to climax."
                hannah.c "ooohhhhh ... ooohhhh ... oohhhh FUUCCKKKKK!!!!"
              "No, have her sit on your face":
                wt_image principal_booty_call_6_8
                player.c "I meant it when I said sit on my face.  Get up here."
                wt_image principal_booty_call_6_9
                "She lowers her wet sex onto your waiting mouth ..."
                wt_image principal_booty_call_6_3
                "... and begins bucking her hips against your face as you work your tongue deep inside her."
                wt_image principal_booty_call_6_10
                hannah.c "ooohhhhh ... ooohhhh ... oohhhh FUUCCKKKKK!!!!"
            wt_image principal_booty_call_3_6
            "As she gets herself dressed, Hannah smiles at you."
            hannah.c "That was hot!  Thanks!!"
            $ hannah.pleasure_her_count += 1
            $ hannah.orgasm_count += 1
            change player energy by -energy_short
            $ hannah.temporary_count = 0
          "Put her on the machine" if dungeon.has_item(fuck_machine):
            $ hannah.fuck_machine_count += 1
            if hannah.fuck_machine_count == 1:
              player.c "I know something we can do that will be fun and dirty.  Come on in."
              wt_image fm_image
              "You lead her to the fuck machine."
              player.c "Take off your clothes and have a seat."
              wt_image principal_booty_call_7_1
              hannah.c "What is that thing?"
              player.c "Your new best friend.  Lie down."
              wt_image principal_booty_call_7_2
              hannah.c "Are you going to put that inside me?"
              player.c "That's how it works."
              wt_image principal_booty_call_7_3
              hannah.c "Oh! That feels ... weird."
              player.c "Give me a moment.  I'm still getting it adjusted.  I haven't turned it on yet."
              wt_image principal_booty_call_7_4
              "You turn the machine on and it starts systematically moving back and forth inside Principal Hannah's rapidly wetting sex ... *whumppp* ... *whumppp* ... *whumppp*"
              hannah.c "OH!  That feels ... even weirder."
              player.c "Lie back.  Relax.  The machine is just getting started."
              wt_image principal_booty_call_7_5
              "*whumppp* ... *whumppp* ... *whumppp* ... *whumppp* ... *whumppp* ... Systematically, the machine moves in and out. Hannah's breathing becomes a bit heavier, and small moans escape her throat."
              hannah.c "ohh ... ohh ... That ... I don't know what that feels like now."
              player.c "Yes you do.  It feels exciting.  Reach down, touch yourself.  Play with yourself while the machine fucks you, Principal Hannah."
              wt_image principal_booty_call_7_6
              "*whumppp* ... *whumppp* ... *whumppp* ... *whumppp* ... *whumppp* ... The machine steadily pounds into her as she rubs her clit with her hand."
              hannah.c "Ooohhhh ... oooohhhhh ... I'm going to ..."
              player.c "You're going to what, Hannah?  Cum?  Try to hold back.  If you cum, I'll bump up the speed of the machine."
              wt_image principal_booty_call_7_7
              hannah.c "Oohhhh FUCCKKKK!!!"
              "Either she doesn't heed your advice, or she can't control herself from climaxing. Either way, as the tremors pass through her body, you bump up the speed of the machine."
              wt_image principal_booty_call_7_8
              "*whumpp* *whumpp* *whumpp*"
              hannah.c "Ohhh!  What's it doing?"
              player.c "Going faster.  What's your body doing?"
              hannah.c "I ... I don't know."
              player.c "Are you sure you don't know?  Because from here it looks like it's building up to another orgasm."
              wt_image principal_booty_call_7_9
              "*whumpp* *whumpp* *whumpp*"
              hannah.c "Ooohhhh ... FUUUCCKKKKK!!!!"
              "Barely finished recovering from her orgasm, her body shudders to another, even more intense climax, her juices running down her skin and pooling on the table beneath her."
              wt_image principal_booty_call_7_10
              player.c "Turn over."
              hannah.c "Wh ... what?"
              "Neither her mind nor her legs are functioning all that well at the moment, so you help her turn over onto her belly."
              wt_image principal_booty_call_7_11
              "Her pussy juice continue to flow out of her, soaking the table as you adjust the machine to an even faster speed ... *whump whump whump whump whump whump*"
              hannah.c "ooohhhhhhhh"
              wt_image principal_booty_call_7_12
              "She doesn't need her hand on her clit to reach the next orgasm. The relentless pounding of the machine into her sore and sensitive pussy is enough ... *whump whump whump whump whump whump*"
              hannah.c "Fuck Fuck Fuck Fuck FUUCCCKKKKKK!!!!!"
              wt_image principal_booty_call_7_13
              "As her third orgasm recedes, you shut off the machine and she slumps to the table."
              player.c "Still with us, Hannah?"
              hannah.c "Mmmmmmm"
              player.c "Did you like that?"
              hannah.c "Mmmmmmm"
              player.c "Time for you to head to school, I think."
              hannah.c "Mmmmmmm.  Just give me a moment, 'kay?"
              "Eventually she dresses and floats off to school."
              $ hannah.orgasm_count += 3
            else:
              player.c "How about another turn on the fucking machine?"
              hannah.c "Oh!  I think my pussy is still aching from the last session."
              player.c "Aching in soreness or aching in anticipation?"
              hannah.c "A bit of both."
              wt_image fm_image
              "She pushes past you and heads to the machine."
              wt_image principal_booty_call_7_1
              "Hannah has her clothes off in record speed and jumps up on the table."
              hannah.c "I want to start off with it fucking me from behind."
              wt_image principal_booty_call_7_10
              player.c "Why?"
              hannah.c "I like not being able to see what's fucking me. It helps my imagination run wild."
              wt_image principal_booty_call_7_14
              "You position the dildo inside her and switch the machine on ... *whumppp* ... *whumppp* ... *whumppp*"
              player.c "Like it could be a stranger with the stamina of a bull pounding into you?"
              hannah.c "Yes!  Oohhhhh"
              wt_image principal_booty_call_7_11
              "*whumppp* ... *whumppp* ... *whumppp* ... The juices flow freely out of her as she reaches her first climax."
              wt_image principal_booty_call_7_12
              hannah.c "Ohhhh .... Ohhhh ... Ohhh FUCCKKK!!!"
              wt_image principal_booty_call_7_10
              player.c "Faster?"
              hannah.c "Yes, please!"
              wt_image principal_booty_call_7_5
              "She flips herself over onto her back as you increase the speed ... *whumpp* *whumpp* *whumpp*"
              wt_image principal_booty_call_7_4
              "*whumpp* *whumpp* *whumpp*"
              hannah.c "Ohhhhh"
              wt_image principal_booty_call_7_8
              hannah.c "Oohhh FUCCKKKK!!!"
              wt_image principal_booty_call_7_6
              "Breathing hard, through clenched lips she barks out."
              hannah.c "Faster!"
              wt_image principal_booty_call_7_9
              "You turn the dial to maximum ... *whump whump whump whump whump whump*"
              wt_image principal_booty_call_7_7
              hannah.c "Fuck Fuck Fuck Fuck Fuuucckkkkk!!  Fuck Fuck Fuuucckkkkk!!  Fuuucckkkk!!!!"
              "Hannah dissolves into a pool of continuous orgasms, the next one starting almost as soon as the previous one subsides, as the machine maintains a constant pounding in her sex ... *whump whump whump whump whump whump*"
              wt_image principal_booty_call_7_13
              "When the sounds of orgasm die down, you flip the machine off.  After a moment, Hannah rolls onto her side, a dreamy look on her face."
              player.c "Had enough?"
              hannah.c "Mmmmmmmm"
              player.c "Ready to start the school day?"
              hannah.c "Mmmmm.  In a minute, 'kay?"
              "Eventually she dresses and floats off to school."
              $ hannah.orgasm_count += 3
            $ hannah.temporary_count = 0
            change player energy by -energy_very_short
          "Spank her":
            if hannah.spanking_count == 0:
              $ hannah.temporary_count = 0
              player.c "Take your clothes off and bend over.  I'm going to spank you."
              hannah.c "Spank me?  Why would I let you do that?"
              player.c "Lots of women enjoy getting spanked.  It'll be fun."
              wt_image principal_booty_call_8_3
              hannah.c "Well, I guess we can try."
              player.c "That's the spirit.  Turn around and bend over, Principal.  It's time you were punished for your naughty behavior."
              wt_image principal_booty_call_8_25
              hannah.c "What naughty behavior?  I've been good!"
              wt_image principal_booty_call_8_26
              player.c "Then in that case, you've earned a 'good girl' spanking.  You can take your underwear off for that, even though I'm sure that's not how you do it in school."
              wt_image principal_booty_call_8_5
              hannah.c "We don't spank kids any way in school these days.  That's barbaric.  There are better ways to discipline a child than hitting them."
              wt_image principal_booty_call_8_6
              player.c "There's no better way to warm up a recalcitrant woman, though.  Or reward a good one.  Turn back around and present your butt for your spanking, Principal."
              wt_image principal_booty_call_8_27
              hannah.c "I'm sure there are better ways you could reward me."
              player.c "No back talk.  Head down and butt up."
              wt_image principal_booty_call_8_28
              "She looks back at you with curiousity as you lift your hand and bring it down sharply, though not too hard, onto her nearest cheek ... *smack*"
              wt_image principal_booty_call_8_29
              hannah.c "Ouch!  That hurt."
              player.c "Nonsense.  That was just a love tap.  Remove your hand so I can warm up the rest of your butt."
              wt_image principal_booty_call_8_28
              "She takes her hand away, but looks back with disapproval as you apply a relatively gentle, steady spanking across the whole of her ass, with a particular focus on the soft, bottom part of her cheeks ... *smack* *smack* *smack* *smack* *smack*"
              wt_image principal_booty_call_8_30
              hannah.c "I think that's enough.  My entire butt is sore, now."
              player.c "Sore or just warm?  And what about between your legs?  Any warmth there?"
              wt_image principal_booty_call_8_2
              hannah.c "No.  The only thing I can feel is the stinging in my ass, and that's not fun."
              wt_image principal_booty_call_8_4
              hannah.c "Sorry this isn't something I can do for you.  I get that it's something you'd enjoy, but it just isn't for me.  Maybe we can try something different next time?  I've got to get to school now."
              $ hannah.spanking_count += 1
              change player energy by -energy_short
            elif hannah.will_tamer_count == 0:
              player.c "I want to spank you again."
              hannah.c "No way!  I tried that once and didn't like it.  Let's do something else."
            else:
              $ hannah.temporary_count = 0
              player.c "I want to spank you again."
              hannah.c "But you know I don't enjoy that."
              player.c "I know, but I want you to do it anyway, to please me."
              wt_image principal_booty_call_8_3
              hannah.c "Shouldn't we stick to things we both enjoy?"
              wt_image principal_booty_call_8_4
              player.c "We both enjoy this.  I enjoy spanking you, and you enjoy pleasing me."
              wt_image principal_booty_call_8_5
              hannah.c "That makes me sound like a doormat."
              player.c "Nonsense.  You're nobody's doormat, are you?  You just enjoy pleasing me, don't you?"
              wt_image principal_booty_call_8_6
              hannah.c "I guess I must."
              player.c "Of course, you do.  Turn around and ask me to spank you."
              wt_image principal_booty_call_8_27
              "Under the lingering impact of the Will-Tamer, Hannah finds herself asking for the spanking she doesn't really want, without truly understanding why she's doing so."
              hannah.c "I guess if you'd enjoy doing so, I'd like you to spank me."
              player.c "I'd be happy to spank you, Hannah.  Stick out your butt to make it easier for me."
              wt_image principal_booty_call_8_28
              "There's no need to be gentle with today's spanking ... *SMACK*"
              wt_image principal_booty_call_8_29
              hannah.c "OW!"
              player.c "Remove your hand.  No touching your butt until I'm done."
              wt_image principal_booty_call_8_28
              "*SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*  ... you spank her ass until she's twitching and shifting back and forth on her feet, trying to deal with the pain."
              wt_image principal_booty_call_8_30
              "When you finally stop, she rubs her sore rear forlornly."
              hannah.c "That was really uncomfortable.  I hope you enjoyed it."
              $ title = "What now?"
              menu:
                "Have her blow you":
                  player.c "I did.  Now you can complete your visit by getting down on your knees and deal with the hard on I got from spanking you."
                  wt_image principal_booty_call_8_7
                  "Hannah's sure she doesn't want your relationship to be this one-sided, but changes made by the Will-Tamer prevent her from articulating an objection that makes sense even to her."
                  wt_image principal_booty_call_8_31
                  "It's a lot easier simply to drop to her knees and take your cock in her mouth"
                  if hannah.deepthroat_training > 1:
                    wt_image principal_booty_call_8_32
                    "Thanks to her deepthroat training, she's even able to get your entire cock in her mouth before you let go."
                  else:
                    wt_image principal_booty_call_8_33
                    "It's also surprisingly easy to relinguish all control and let you face-fuck her however you want until you cum."
                  player.c "[player.orgasm_text]"
                  wt_image principal_booty_call_8_9
                  hannah.c "Next time, how about we do something we both like?"
                  $ hannah.blowjob_count += 1
                  $ hannah.swallow_count += 1
                  orgasm
                "She can go":
                  player.c "I did.  You can go to school now."
                  wt_image principal_booty_call_8_27
                  hannah.c "Next time, how about we do something we both like?"
                  change player energy by -energy_short
              wt_image principal_booty_call_8_25
              player.c "We just did.  You enjoy coming over here to please me, remember?"
              $ hannah.spanking_count += 1
          "Work on her deep throat skills":
            if hannah.deepthroat_training == 0:
              $ hannah.temporary_count = 0
              player.c "I think today we should work on your sex skills."
              hannah.c "What do you mean?  My sex skills are fine, aren't they?"
              player.c "Not your deep throat skills.  At least, not that you've shown me."
              hannah.c "Deep throat?  Isn't that just a porn thing?  Nobody actually does that."
              player.c "Sure they do.  Haven't you ever tried?"
              wt_image principal_booty_call_9_1
              if hannah.whore_count > 1:
                "Hannah blushes, recalling her visit with her former, well-endowed john, but bites her tongue."
                hannah.c "If that's something you'd like me to try with you, I guess I can."
              else:
                hannah.c "No, but if that's something you'd like me to try with you, I guess I can."
              wt_image principal_booty_call_9_2
              hannah.c "If I'd known I'd end up trying this, I might've picked a booty call partner who wasn't quite so big."
              wt_image principal_booty_call_9_3
              player.c "Where would the fun have been in that?  You're up for the challenge, aren't you?"
              wt_image principal_booty_call_9_4
              hannah.c "I guess.  Here goes."
              wt_image principal_booty_call_9_5
              "She starts to work her way down your shaft ..."
              wt_image principal_booty_call_9_6
              "... then she starts to gag."
              wt_image principal_booty_call_9_4
              hannah.c "Sorry.  You're both long and thick.  This isn't easy.  Let me try again."
              wt_image principal_booty_call_9_5
              "She slides down your shaft again, trying her best to relax her throat and ignore the gag reflex."
              wt_image principal_booty_call_9_7
              "She gets almost all of you inside her this time, before she starts to panic and backs off."
              wt_image principal_booty_call_9_4
              hannah.c "It's hard to breathe with you all the way in like that.  How was that?  Was that good?"
              wt_image principal_booty_call_9_3
              player.c "You're not going to settle for 90%, are you Principal?  I'm sure you were a better student than that."
              wt_image principal_booty_call_9_8
              "Hannah's always been a determined, driven woman, and she takes your goading to heart."
              wt_image principal_booty_call_9_7
              "She panics again when she feels the tip of your cock reach the back of her throat, but gets herself under control."
              wt_image principal_booty_call_9_9
              "After a brief pause, she continues.  She's able to open the back of throat enough to get almost to the end of your shaft."
              wt_image principal_booty_call_9_6
              hannah.c "I think that's as much as I ..."
              wt_image principal_booty_call_9_10
              "You stop her with a hand at the back of her head."
              player.c "No, it isn't.  I know you can get to 100%.  Nod when you're ready to try again."
              wt_image principal_booty_call_9_11
              "After a moment she nods, and begins to slide forward onto your shaft.  You don't need to push her, but your hand in her hair at the back of her head reminds her that she can only go forward, not back."
              wt_image principal_booty_call_9_7
              "She slides past her gag point, pausing only a second ..."
              wt_image principal_booty_call_9_9
              "... then moves forward again, until she's tantalizingly close to having you completely inside her."
              player.c "Almost there, Hannah.  Collect your breath and nod when you're ready.  I'm going to push you the rest of the way on."
              wt_image principal_doll_test_mouth_1_5
              "With steady pressure on the back of her head, you move her all the way onto your cock, until her nose is pressed against your belly and strange, muffled gurgling sounds come out of her."
              player.c "Look at me, Hannah.  Can you breathe?"
              wt_image principal_booty_call_9_12
              "She nods, pulling back almost imperceptively as she does."
              player.c "Good.  Back all the way onto my cock, balls on your chin, nose into my belly.  When you're in position, I'm going to cum straight down the back of your throat."
              wt_image principal_booty_call_9_13
              player.c "Almost there.  You can get there on your own this time, you don't need me to push your head down again, do you?"
              "She shakes her head slowly and wills herself forward as your balls reach their breaking down."
              wt_image principal_doll_test_mouth_1_5
              player.c "[player.orgasm_text]"
              wt_image principal_booty_call_9_2
              hannah.c "I guess I can check that off my bucket list, after I add it under the category of 'things I wasn't really interesting in trying'.  Considering how long it took you to stop cummming, I'm guessing you enjoyed it, though."
              player.c "I did.  Thank you."
              wt_image principal_booty_call_1_1
              hannah.c "You're welcome!  We'll try something else next time, maybe something we'll both enjoy.  Bye!"
              $ hannah.blowjob_count += 1
              $ hannah.swallow_count += 1
              $ hannah.deepthroat_training += 1
              orgasm
            elif hannah.will_tamer_count == 0:
              player.c "I'd like you to deep throat me, again."
              hannah.c "No way!  I tried that once.  Let's do something fun for both of us."
            else:
              $ hannah.temporary_count = 0
              player.c "I'd like you to deep throat me, again."
              hannah.c "But you know I didn't enjoy it."
              player.c "And you know that I did, and I think you'll enjoy making me happy by doing it again."
              wt_image principal_booty_call_9_1
              hannah.c "I want to do something new, or at least something that lets me get off, not just you."
              wt_image principal_booty_call_9_2
              player.c "It's okay with me if you get off while you deep throat me.  Lie down with your head hanging over the edge of the sofa."
              wt_image principal_booty_call_9_14
              hannah.c "Why like this?"
              wt_image principal_booty_call_9_15
              player.c "So that after you use your hands to warm up my balls, you can use them to play with your pussy while you deep throat me."
              wt_image principal_booty_call_9_16
              "That's one reason.  Another is that you're in complete control in this position, able to shove your cock deeper ..."
              wt_image principal_booty_call_9_17
              "... and deeper into her throat, without her having any easy means to pull away."
              wt_image principal_booty_call_9_18
              "You do need to be careful and pace yourself, especially when she starts to retch.  She's already coughing and drooling out a ton of saliva, and if she throws up in this position she could asphyxiate herself."
              wt_image principal_booty_call_9_19
              "Once she gets the hang of taking your entire shaft down her throat without choking, though, you can abuse her face to your heart's content."
              wt_image principal_booty_call_9_20
              player.c "[player.orgasm_text]"
              wt_image principal_booty_call_9_21
              player.c "Clean off the excess drool you left on my cock before you go, Hannah.  Did you cum with my cock down your throat?"
              hannah.c "No!"
              player.c "Why not?  Didn't you remember to play with your pussy?"
              hannah.c "I was too busy trying not to choke to worry about anything else."
              player.c "Always prioritizing my pleasure over your own, aren't you, Hannah?  I think that's what I like best about you.  What would you like to say to me for giving you the opportunity to focus on my pleasure?"
              if hannah.will_tamer_count == 2:
                hannah.c "Thank you?"
                player.c "You're welcome.  I may give you another opportunity to please me the next time you drop by, too.  I know you'd like that."
                "She stares at you wide-eyed, confused by her own behavior and reactions.  After a moment, she gets up and heads to school quietly, trying to sort out her own feelings."
              else:
                "She just stares at you and says nothing.  After a moment, she gets up and heads to school quietly, confused by her own behavior."
              $ hannah.blowjob_count += 1
              $ hannah.swallow_count += 1
              $ hannah.deepthroat_training += 1
              orgasm
          "Use Will-Tamer" if player.has_item(will_tamer) and not hannah.has_tag('will_tamer_this_week'):
            call hannah_will_tamer_timer from _call_hannah_will_tamer_timer_2
  if hannah.letter_re_terri != 4:
    if hannah.lost_money_and_no_fix == 1 and hannah.will_tamer_count < 3:
      "As she's leaving, Hannah suddenly looks serious."
      hannah.c "I'm probably not going to be able to see you again. There's been some money problems at the school. It's going to take everything I have - maybe more - to try and keep the school going. I'm afraid I'm not going to have the time or energy for our little visits anymore."
      "You could consider visiting her at the school to see if you could help her with her troubles."
      $ hannah.visit_week = 0
      if not hannah.has_tag('available_for_school_visit'):
        add tags 'available_for_school_visit' to hannah
    else:
      $ hannah.random_number = renpy.random.randint(1, 10)
      if hannah.random_number < 3:
        $ hannah.visit_week = week + 1
      elif hannah.random_number < 8:
        $ hannah.visit_week = week + 2
      else:
        $ hannah.visit_week = week + 3
  rem tags 'booty_call' 'insist' 'booty_call_in_progress' from hannah
  call character_location_return(hannah) from _call_character_location_return_685
  notify
  wt_image current_location.image
  return

label hannah_booty_call_footjob:
  player.c "Okay, Hannah.  Let's see what you can do with those feet of yours."
  wt_image principal_booty_call_2_6
  hannah.c "All right.  Here goes.  I hope this doesn't feel stupid to you."
  "Tentatively, she starts to caress your hard on with her feet."
  wt_image principal_booty_call_2_7
  "As she feels your body respond, she becomes a little bolder, stroking your cock with her toes and soft soles."
  wt_image principal_booty_call_2_8
  "Soon she's pumping your cock up and down, gripping it between her feet as the pressure builds in your balls ..."
  wt_image principal_booty_call_2_9
  "... until you can't hold it back and you let yourself go, spraying her feet and your belly with your seed."
  player.c "[player.orgasm_text]"
  "She smears your cum around with her feet ..."
  wt_image principal_booty_call_2_10
  "... then sits up and licks your cock clean."
  hannah.c "Did that feel okay?"
  player.c "It did.  How about for you?"
  wt_image principal_booty_call_2_12
  "She laughs."
  hannah.c "I don't think my legs have ever been so tired after sex! Thanks for doing that with me. I can now tick that off my 'to do' list."
  wt_image principal_booty_call_2_13
  player.c "We could do it again sometime, if you want."
  hannah.c "I'll pass. It was fun, but that was hard work! And it turns out feeling your cock with my feet wasn't as exciting as feeling it inside me. I'm sure we can find some other fun things to do instead."
  $ hannah.footjob_count += 1
  orgasm
  return

label hannah_booty_call_outfit_1_cum_in_mouth:
    wt_image principal_booty_call_1_15
    "Hannah starts stroking and sucking you faster, then opens her mouth slightly as you cum, so you can see your seed enter her."
    player.c "[player.orgasm_text]"
    wt_image principal_booty_call_1_44
    hannah.c "Mmmmm. That was a big load.  I think you enjoyed that.  My turn now."
    $ hannah.swallow_count += 1
    $ title = "What do you want to do?"
    menu:
        "Eat her out":
            call hannah_booty_call_outfit_1_eat from _call_hannah_booty_call_outfit_1_eat_1
        "Tell her to go":
            player.c "Aren't you late for school? You should probably be going."
            wt_image principal_booty_call_1_16
            hannah.c "I have time to ... you know.  You said that after I blew you, you'd get me off."
            player.c "I changed my mind.  Time for you to go."
            wt_image principal_booty_call_1_11
            hannah.c "Jerk!"
            wt_image current_location.image
            "Hannah dresses and storms off.  At least the silly woman won't be bothering you at your house any more."
            $ hannah.visit_week = 0
            $ hannah.letter_re_terri = 4
    return

label hannah_booty_call_outfit_1_eat:
  player.c "Lie back, Principal Hannah."
  wt_image principal_booty_call_1_17
  "She spreads her legs and gives you open access to her beautiful pussy."
  wt_image principal_booty_call_1_18
  "She moans when you slip a finger insider her."
  hannah.c "Ohhh"
  "She moans louder when you lick your tongue along her open sex."
  hannah.c "Oohhhh"
  wt_image principal_booty_call_1_19
  "Then you get down to some serious pussy licking."
  hannah.c "Ooohhhh ... Yes!  That feels sooo good ... Oooohhhhh"
  wt_image principal_booty_call_1_20
  hannah.c "Ooohhhh FUUUCKKKK!!"
  "Hannah floods your mouth with her juices as she cums."
  wt_image principal_booty_call_1_21
  if hannah.lost_money_and_no_fix != 1:
    hannah.c "Mmmmm.  That was nice."
    "Hannah dresses and heads to the school, seemingly happy."
  $ hannah.pleasure_her_count += 1
  $ hannah.orgasm_count += 1
  change player energy by -energy_short
  return

label hannah_booty_call_outfit_1_missionary:
  wt_image principal_booty_call_1_22
  player.c "Lie back and spread your legs, Principal Hannah. Open yourself up for me."
  wt_image principal_booty_call_1_23
  hannah.c "Oohhh"
  "She groans as you push yourself inside her. She's warm, wet, and tight, and you groan a little yourself at the feel of her around your hard cock."
  wt_image principal_booty_call_1_24
  hannah.c "Oohhh oooohhhh oooohhhh ... That feels good!  Faster!  Fuck me faster!!"
  wt_image principal_booty_call_1_25
  "Hannah rubs her clit, bringing herself to orgasm as you fuck her. The feel of her body climaxing around your cock soon brings you over the edge too."
  hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
  player.c "[player.orgasm_text]"
  wt_image principal_booty_call_1_21
  if hannah.lost_money_and_no_fix != 1:
    hannah.c "Mmmmm. That was nice."
    "Hannah dresses and heads to the school, seemingly happy."
  $ hannah.sex_count += 1
  $ hannah.orgasm_count += 1
  orgasm
  return

label hannah_booty_call_outfit_1_behind:
  player.c "Turn around, Principal Hannah. I'm going to fuck you from behind."
  wt_image principal_booty_call_1_26
  hannah.c "Okay"
  wt_image principal_booty_call_1_27
  hannah.c "Oohhh"
  "She groans as you push yourself inside her. She's warm, wet, and tight, and you groan a little yourself at the feel of her around your hard cock."
  wt_image principal_booty_call_1_28
  hannah.c "Oohhh oooohhhh oooohhhh ... That feels good!  Faster!  Fuck me faster!!"
  wt_image principal_booty_call_1_29
  hannah.c "Oohhh ooohhhhh FUUCCCKKKKK!!!"
  "Hannah reaches down with her hand and rubs her clit, bringing herself to orgasm as you fuck her."
  "The feel of her body climaxing around your cock soon brings you over the edge too."
  player.c "[player.orgasm_text]"
  wt_image principal_booty_call_1_21
  if hannah.lost_money_and_no_fix != 1:
    hannah.c "Mmmmm. That was nice."
    "Hannah dresses and heads to the school, seemingly happy."
  $ hannah.sex_count += 1
  $ hannah.orgasm_count += 1
  orgasm
  return

# End Day - Principal Event: Thank you post Marilyn and not continuing actions yet?
label hannah_thank_you:
  $ hannah.training_session()
  $ hannah.visit_week = 0
  rem tags 'no_hypnosis' from hannah
  $ title = "What do you do?"
  menu:
    "Hypnotize her" if player.can_hypno(hannah):
      player.c "Principal Hannah, please look at this."
      call focus_image from _call_focus_image_20
      player.c "You and I are going to have a talk.  You are going to listen to me."
      player.c "Listen to me now.  Listen to me.  Only me.  Only my words now.  Only my words."
      wt_image principal_apology_29
      "She soon falls under your trance."
      player.c "Let's be comfortable for our talk, Hannah.  You're grateful that I accepted your apology and want me to be comfortable around you."
      player.c "Pull down the top of your dress, Principal, so that you and I will be comfortable for our talk."
      wt_image principal_apology_30
      hannah.c "Of course I'm very grateful for your kind help."
      wt_image principal_apology_31
      hannah.c "Is this better?"
      player.c "Having your dress hanging open is very awkward, Principal. Take the whole dress off so that we can be more comfortable."
      wt_image principal_apology_32
      hannah.c "This is awkward. I'll take my dress off completely."
      player.c "Take the rest of your clothes off too, Hannah. Everything will feel so much more open and relaxed between us once you are naked. All the tension will be gone and we can relax and talk like friends."
      wt_image principal_apology_33
      hannah.c "Is this better?  Do you feel less tense and more comfortable?"
      player.c "It seems like you're hiding something, Hannah. Sitting with your legs crossed like that make it seem like you don't want to be open with me."
      player.c "You want to be open with me, Principal Hannah. You want me to know that you have nothing to hide."
      wt_image principal_apology_34
      hannah.c "I don't want you to think I'm hiding anything. I want you to see me as an open book."
      add tags 'hypnotized_now' to hannah
      $ title = "What do you do?"
      menu:
        "Ask her to complete her thank you":
          player.c "You want me to know how grateful you are now, Hannah. You want me to know how thankful you are for my help."
          hannah.c "I already told you how grateful I am."
          if player.has_tag('hypnotist') or player.hypnosis_level > 10:
            player.c "You're very grateful to me for my help, Hannah. You want me to know how thankful you are that I saved your school from financial ruin. You don't want me to think that you are not grateful. You want to complete your apology in a way that will let me know how grateful you are."
            player.c "You want to take my cock and suck it so that I will know how grateful you are."
            wt_image principal_apology_35
            "She accepts your cock as you offer it to her."
            hannah.c "I want you to know how thankful I am that you accepted my apology."
            player.c "If you're truly grateful, Hannah, you will lick my balls before you suck my cock. You are truly grateful Hannah and you will show me that by licking my balls before you suck my cock."
            wt_image principal_apology_36
            hannah.c "Of course!"
            wt_image principal_apology_55
            player.c "When I cum, you'll show me how grateful you are for accepting your apology by swallowing my load, Hannah. Keep your eyes on me while I fill your mouth with my jizz, then swallow every drop so that I know how thankful you are."
            wt_image principal_apology_37
            "She watches you intently and makes a big show of swallowing your cum after you let go inside her."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_blowjob_count += 1
            $ hannah.hypno_swallow_count += 1
            orgasm
            $ title = "What do you do now?"
            menu:
              "Chat with her":
                "She seems in no rush to remove your cock from her mouth so you let her kneel there while you chat with her."
                call hannah_thank_you_chat from _call_hannah_thank_you_chat
              "Show her out":
                rem tags 'hypnotized_now' from hannah
                "You enjoy the sight of the school Principal's naked body for a few more minutes, then have her dress, bring her out of her trance, and show her to the door so you can get on with your day."
                $ hannah.hypno_session() # subtracts energy and records that she was hypnotized
          else:
            "You're not a strong enough a hypnotist to convince her to complete her apology."
            $ title = "What do you do now?"
            menu:
              "Chat with her":
                call hannah_thank_you_chat from _call_hannah_thank_you_chat_1
              "Show her out":
                rem tags 'hypnotized_now' from hannah
                "You enjoy the sight of the school Principal's naked body for a few more minutes, then have her dress, bring her out of her trance, and show her to the door so you can get on with your day."
                $ hannah.hypno_session() # subtracts energy and records that she was hypnotized
        "Chat with her":
          call hannah_thank_you_chat from _call_hannah_thank_you_chat_2
    "Ask for a more personal thank you":
      wt_image principal_apology_4
      player.c "I'm glad to hear you appreciated my help, Hannah. Perhaps you could show me just how grateful you are?"
      hannah.c "You can't be implying what that sounds like?"
      player.c "What does it sound like?"
      hannah.c "Like you want me to thank you ... sexually."
      $ title = "What do you tell her?"
      menu:
        "That is what you want":
          wt_image principal_apology_3
          hannah.c "No! Absolutely not! What sort of woman do you think I am?"
          hannah.c "Actually, forget it ... don't answer that. I can see what sort of woman you think I am, and what sort of man you are. Good bye."
          $ title = "What do you do?"
          menu:
            "Threaten to cut off her financing":
              player.c "That financing can disappear as quickly as it appeared."
              hannah.c "You wouldn't!"
              player.c "Why wouldn't I? You're clearly not thankful for the assistance I've given you."
              hannah.c "I am thankful, I just ..."
              player.c "Just what? Don't want to show it?"
              hannah.c "Not like that!"
              player.c "Which means you're not really thankful. Goodbye, Principal Hannah."
              "She hesitates."
              hannah.c "What is it you want, exactly?"
              $ title = "What is it you want from her?"
              menu:
                "Let you punish her":
                  player.c "I was going to settle for a simple blow job, but since you're showing yourself to be an ungrateful brat, I think I'll punish you instead."
                  hannah.c "What?  How?"
                  player.c "I'm going to take you into my dungeon, strip you naked, and discipline you physically."
                  hannah.c "You can't be serious?"
                  player.c "I am. Or you can walk out of here, and find out what happens to your newfound government support."
                  hannah.c "Fine. But no touching me sexually."
                  call hannah_punishment_call from _call_hannah_punishment_call
                "Let you have sex with her":
                  player.c "You say you're thankful. So show me. Start by pulling up your dress."
                  hannah.c "You can't be serious?"
                  player.c "I'm very serious.  If you want me to think you're really grateful, do as you're told."
                  player.c "Lift the dress or get out of my house and live with the consequences."
                  call hannah_forced_sex_call from _call_hannah_forced_sex_call
            "Let her go":
              "She storms off, letting you get on with your day."
              $ hannah.letter_re_terri = 14
        "You were just teasing":
          wt_image principal_apology_2
          player.c "Hmmm, well, that would be a very pleasant thank you to receive from a woman as beautiful as you, Hannah, but I was only teasing you. You can't imagine I would seriously expect something like that?"
          hannah.c "Oh!  Sorry ... you got me."
          "She laughs in relief."
          call hannah_visit_finish_chat from _call_hannah_visit_finish_chat
    "Chat with her":
      call hannah_thank_you_chat from _call_hannah_thank_you_chat_3
  $ hannah.marilyn_solution_thank_you = 2
  rem tags 'thank_you_visit' 'first_visit_partially_undressed' from hannah
  add tags 'no_hypnosis' to hannah
  call character_location_return(hannah) from _call_character_location_return_686
  notify
  return

label hannah_thank_you_chat:
  player.c "I appreciate you taking the time to come here and provide your thank you in person, Principal Hannah. I trust the new financing will make your job easier?"
  hannah.c "It will! I don't know how I could have balanced our expenses without it. Even with the new financing, it's going to be difficult, but if I work hard enough, we can just do it."
  $ hannah.relax = False
  $ title = "What next?"
  menu menu_hannah_thank_you_chat:
    "What about a quick romp?" if hannah.relax:
      player.c "It doesn't take a lot of time to have a lot of fun. I know you're busy. I'm busy, too. We're also human. A little company from time to time, you know, to help out with some natural human needs. There's nothing wrong with that."
      if player.has_tag('supersexy'):
        wt_image principal_apology_4
        hannah.c "You mean like a booty call?  Me, with you?"
        player.c "Whenever you're in the mood."
        hannah.c "I'll have to think about it."
        "You're sure she will."
        $ hannah.letter_re_terri = 7
        $ hannah.visit_week = week
      else:
        hannah.c "No, there isn't anything wrong with that. But I'm not looking for a 'friend with benefits'. I'm really just too busy with the school."
      if hannah.has_tag('hypnotized_now'):
        rem tags 'hypnotized_now' from hannah
        "You enjoy the sight if her naked body for a few more minutes, then bring her out of her trance and send her home."
        $ hannah.hypno_session() # subtracts energy and records that she was hypnotized
      else:
        "You show Hannah to the door and get on with your day."
    "Suggest you could help her relax" if not hannah.relax:
      player.c "Perhaps I could help you take your mind off your responsibilities. Recharge your battery so to speak. When's the last time you did something fun?"
      hannah.c "Fun? I don't really have time for that. The school and its students are my life."
      $ hannah.relax = True
      jump menu_hannah_thank_you_chat
    "Show her out":
      if hannah.has_tag('hypnotized_now'):
        rem tags 'hypnotized_now' from hannah
        "You enjoy the sight of her naked body for a few more minutes, then bring her out of her trance and send her home."
        $ hannah.hypno_session() # subtracts energy and records that she was hypnotized
      elif hannah.has_tag('first_visit_partially_undressed'):
        "You enjoy the sight of her body for a few more minutes, then let her dress and send her home."
      else:
        "You show Hannah to the door and get on with your day."
  wt_image current_location.image
  return

label hannah_forced_sex_call:
    wt_image principal_apology_38
    "She lifts the dress, exposing her pale but shapely legs."
    player.c "Higher. And remove your hand from between your legs."
    wt_image principal_apology_39
    hannah.c "Please don't make me do this."
    if hannah.has_tag('thank_you_visit'):
        hannah.c "Please, just accept my thank you. Haven't I done enough to show you I'm grateful?"
    elif hannah.has_tag('lawyer_call'):
        hannah.c "Please, just accept my apology.  Haven't I done enough to show you I mean it?"
    $ title = "What do you do?"
    menu:
        "Tell her to lose the dress":
            wt_image principal_apology_40
            player.c "Pull down the top of the dress, Principal."
            "She glowers at you, but complies."
            wt_image principal_apology_32
            player.c "Better yet, lose the dress completely."
            wt_image principal_apology_41
            player.c "Spread your legs, Principal."
            if hannah.has_tag('thank_you_visit'):
                hannah.c "Please. Don't take this any further. I've proven that I'm willing to humiliate myself to demonstrate the sincerity of my gratitude."
                hannah.c "Please, just accept my thank you."
            elif hannah.has_tag('lawyer_call'):
                hannah.c "Please.  Don't take this any further. I've proven that I'm willing to humiliate myself to demonstrate the sincerity of my apology."
                hannah.c "Please, just accept my apology."
            add tags 'first_visit_partially_undressed' to hannah
            $ title = "What do you do?"
            menu:
                "Tell her to get naked":
                    wt_image principal_apology_42
                    player.c "I don't think we've proven anything yet.Remove your top and pull down your panties."
                    wt_image principal_apology_43
                    player.c "There's no need for modesty, Principal Hannah. Spread your legs."
                    wt_image principal_apology_34
                    player.c "Don't be coy. Open yourself up so I can see your cunt and your ass."
                    hannah.c "Fine.  Happy?  You've proved your point."
                    hannah.c "I let you know my weakness. I care about the school. You've shown me that you're willing to exploit that weakness."
                    if hannah.has_tag('thank_you_visit'):
                        hannah.c "You're a powerful man. I get that. You got me money, and you're willing to take it away.  So now here I sit, naked and humiliated, opening my body for your inspection."
                    elif hannah.has_tag('lawyer_call'):
                        hannah.c "You're a powerful man. I get that. I messed with the wrong man by sending that ill advised letter. So now here I sit, naked and humiliated, opening my body for your inspection."
                    hannah.c "You win. You have all the power here. I'm just a naked and vulnerable woman."
                    hannah.c "Can I go now, while I have a shred of decency still left?  Please?"
                    $ title = "What do you do?"
                    menu:
                        "Tell her to suck your cock":
                            player.c "A naked and vulnerable woman who's running her mouth when she should be using it to suck my cock. Make yourself useful."
                            wt_image principal_apology_35
                            "With a sigh of resignation she accepts your cock as you offer it to her."
                            player.c "Warm my balls up first, Principal, before you start sucking."
                            wt_image principal_apology_36
                            "It seems she isn't going to argue with you."
                            wt_image principal_apology_44
                            "She proves herself to be an eager little cocksucker.  Perhaps she's hoping to finish you off quickly and bring this ordeal to a fast end."
                            $ title = "What do you do?"
                            menu:
                                "Switch to her cunt":
                                    player.c "Don't be in a rush, Principal.  I appreciate the fine cock sucking job you're doing, but I have more planned for you than that.  Climb on top of me."
                                    wt_image principal_apology_45
                                    "You sit down and pull her up on top of you.  She's not even remotely wet, and she lets out a groan as you push into her. It's not a groan of pleasure."
                                    hannah.c "oowwwww"
                                    $ title = "What do you do?"
                                    menu:
                                        "Switch to her ass":
                                            wt_image principal_apology_57
                                            player.c "That's a little uncomfortable for you, isn't it Principal Hannah?"
                                            hannah.c "Yes"
                                            player.c "You're not really wet, are you?"
                                            hannah.c "No"
                                            player.c "So if your cunt isn't going to get wet for me, I may as well fuck your ass, right?  If I have to plow a dry hole, it might as well be a tight one, don't you agree?"
                                            wt_image principal_apology_47
                                            "She doesn't reply, more a function of shock rather than agreement. You turn her around and position your cock at her rosebud. To your surprise, and likely hers, you're able to push inside her without much difficulty."
                                            $ hannah.anal_count += 1
                                            $ title = "Where do you want to cum?"
                                            menu:
                                                "In her ass":
                                                    wt_image principal_apology_49
                                                    "You roll her onto her side to give you more leverage, and start pounding into her.  You can't go as fast as you'd like or you'd risk tearing her anus. What the fuck lacks in speed, however, it more than makes up for in tightness, as her body struggles to accommodate your girth."
                                                    wt_image principal_apology_60
                                                    "Before long, you fill her ass with your seed."
                                                    player.c "[player.orgasm_text]"
                                                    call hannah_forced_sex_call_cum from _call_hannah_forced_sex_call_cum
                                                "In her mouth":
                                                    wt_image principal_apology_49
                                                    "The School Principal appears to be in an accommodating mood, so you decide to indulge in a little dirty play. You plow her ass until you're ready to cum, then let her know what's expected of her next."
                                                    wt_image principal_apology_59
                                                    player.c "I'm ready to cum now, Principal.  Suck me off."
                                                    hannah.c "But ..."
                                                    player.c "Yes, it was inside your butt.  Suck it anyway."
                                                    wt_image principal_apology_48
                                                    player.c "My cock smells like your ass now, doesn't it Hannah?  Does it taste like your ass too?"
                                                    "She says nothing, and keeps her eyes turned away from you as fill her mouth with your cum."
                                                    player.c "[player.orgasm_text]"
                                                    wt_image principal_apology_60
                                                    player.c "Swallow all of that, Principal.  I don't want any remnants from your ass dripping onto my floor or furniture."
                                                    $ hannah.swallow_count += 1
                                                    call hannah_forced_sex_call_cum from _call_hannah_forced_sex_call_cum_1
                                        "Cum in her cunt":
                                            wt_image principal_apology_57
                                            player.c "I presume you're on birth control, Principal?"
                                            "She nods."
                                            wt_image principal_apology_46
                                            player.c "Good"
                                            "You roll her onto her side. More as a self-defense mechanism than anything else, her body opens up enough to let you pound into her. She's not enjoying it, but it still feels good to you, and before long you're spurting your load inside her."
                                            wt_image principal_apology_58
                                            player.c "[player.orgasm_text]"
                                            $ hannah.sex_count += 1
                                            call hannah_forced_sex_call_cum from _call_hannah_forced_sex_call_cum_2
                                "Cum in her mouth":
                                    wt_image principal_apology_55
                                    player.c "Keep your eyes up here, Principal Hannah. I'm going to fill your mouth with my cum. Be a good girl and swallow it all."
                                    wt_image principal_apology_37
                                    player.c "[player.orgasm_text]"
                                    "She doesn't flinch as you spurt into her. She even makes some pronounced swallowing motions to make it clear that she drank your full offering."
                                    $ hannah.blowjob_count += 1
                                    $ hannah.swallow_count += 1
                                    call hannah_forced_sex_call_cum from _call_hannah_forced_sex_call_cum_3
                                "Cum on her face":
                                    wt_image principal_apology_35
                                    player.c "Take my cock out of your mouth and look at me, Principal Hannah. I'm going to cover your pretty face with my cum."
                                    wt_image principal_apology_56
                                    player.c "[player.orgasm_text]"
                                    "She looks away as you spurt onto her, but otherwise makes no effort to avoid the jizz you splatter on her."
                                    $ hannah.blowjob_count += 1
                                    $ hannah.facial_count += 1
                                    call hannah_forced_sex_call_cum from _call_hannah_forced_sex_call_cum_4

                        "Let her go":
                            player.c "I'm glad we understand each other, Principal Hannah. Is there something you'd like to say to me now."
                            "She hesitates just a moment."
                            if hannah.has_tag('thank_you_visit'):
                                hannah.c "Thank you.  Thank you for helping our school."
                                $ hannah.letter_re_terri = 14
                            player.c "You're very welcome.  Now get yourself dressed and get out of here.  I'm sure we both have better things we could be doing with our day."
                "Accept her thank you" if hannah.has_tag('thank_you_visit'):
                    player.c "Don't change position. Stay like that while we complete our talk. Understood?"
                    "She nods."
                    call hannah_thank_you_chat from _call_hannah_thank_you_chat_4
                "Accept her apology" if hannah.has_tag('lawyer_call'):
                    player.c "Don't change position. Stay like that while we complete our talk. Understood?"
                    "She nods."
                    call hannah_lawyer_call_apology from _call_hannah_lawyer_call_apology
        "Accept her thank you" if hannah.has_tag('thank_you_visit'):
            player.c "Don't change position. Stay like that while we complete our talk. Understood?"
            "She nods."
            call hannah_thank_you_chat from _call_hannah_thank_you_chat_5
        "Accept her apology" if hannah.has_tag('lawyer_call'):
            player.c "Don't change position. Stay like that while we complete our talk. Understood?"
            "She nods."
            call hannah_lawyer_call_apology from _call_hannah_lawyer_call_apology_1
    return

label hannah_forced_sex_call_cum:
  wt_image principal_apology_30
  "Once you've finished cumming, you let her clean up and get herself dressed."
  if hannah.has_tag('thank_you_visit'):
    player.c "That was very nice thank you, Principal Hannah.  I'm glad you finally came around and decided to show me how grateful you are for your new financing."
    "She doesn't seem particularly grateful right now, but she holds her tongue, unwilling to antagonize you again."
  elif hannah.has_tag('lawyer_call'):
    player.c "That was very nice apology, Principal Hannah. I hope you've learned your lesson. If you want to keep your school and yourself safe, consider your actions more carefully in the future."
  hannah.c "Can I go now?"
  "You let her leave and get back to your day."
  if hannah.has_tag('thank_you_visit'):
    $ hannah.letter_re_terri = 15
  elif hannah.has_tag('lawyer_call'):
    $ hannah.letter_re_terri = 12 #opens up potential for her to become a whore post bank events
  orgasm
  return

label hannah_punishment_call:
    player.c "Follow me."
    call forced_movement(dungeon) from _call_forced_movement_977
    wt_image principal_apology_5
    "At first, there's almost a curiosity to Hannah as she watches you fasten her into position for her punishment."
    wt_image principal_apology_6
    "Once you have her fully secured and start circling her, however..."
    wt_image principal_apology_7
    "... curiosity is replaced by nervous apprehension as she waits for the punishment to start."
    if dungeon.has_item(floggers):
        $ title = "What do you do?"
        menu:
            "Warm her up with the flogger?":
                wt_image principal_apology_8
                "She flinches as you whip the flogger across her front."
                "If it doesn't hurt as much as she feared it might, that's giving her false hope. Which is the point of the warm up. To get her ready to take a lot more pain in the very near future."
                wt_image principal_apology_9
                "When you shift to whipping upwards against her bare inner thighs and tender sex, she grimaces as she gets a better sense of what's in store, but still doesn't know how much more intense her punishment is going to become."
            "Strip her down":
                pass
    wt_image principal_apology_10
    "You pull open her bra and squeeze her breasts cruelly. She flinches, but controls herself from crying out."
    wt_image principal_apology_11
    "As you pull off her dress, she starts to tremble."
    wt_image principal_apology_12
    "Principal Hannah seems to find the exposure of her flesh to your eyes humiliating enough to be a punishment in its own right, so you let her experience it unadulterated by any physical distractions as you slowly circle her."
    if dungeon.has_item(floggers):
        wt_image principal_apology_13
        "Eventually, you break the mental torture with some physical torture.  As you whip her ass, again and again and again, she fights to stay silent ... *thwaapppp* ... *thwaappp* ... *thwaappp* ... *thwaappp* ... *thwaappp*"
        wt_image principal_apology_12
        $ title = "Keep going?"
        menu:
            "Keep whipping her":
                wt_image principal_apology_13
                "You don't mind the challenge. You keep whipping her bare back and ass. Eventually, she breaks.  *thwaapppp* ... *thwaappp* ... *thwaappp*"
                wt_image principal_apology_50
                hannah.c "Aaagghhh!"
                "*thwaapppp* ... *thwaappp* ... *thwaappp*"
                hannah.c "Aaagghhh!!!!!"
                "*thwaapppp*"
                wt_image principal_apology_14
                hannah.c "AAAGHHH!!!!"
                $ title = "Keep going?"
                menu:
                    "Tie her into a new position":
                        call hannah_punishment_new_position from _call_hannah_punishment_new_position
                    "She's had enough":
                        call hannah_punishment_enough from _call_hannah_punishment_enough
            "Tie her into a new position":
                call hannah_punishment_new_position from _call_hannah_punishment_new_position_1
            "She's had enough":
                call hannah_punishment_enough from _call_hannah_punishment_enough_1
    else:
        "Without a flogger, this isn't the best position for you to punish her."
        call hannah_punishment_new_position from _call_hannah_punishment_new_position_2
    return

label hannah_punishment_new_position:
    wt_image principal_apology_15
    "You re tie her into a new position on the floor, head down, ass up."
    player.c "Comfortable, Principal Hannah?"
    wt_image principal_apology_16
    hannah.c "No"
    player.c "Good. It's about to get worse."
    "She looks like she's about to say something more, then thinks better of it, no doubt not wanting to antagonize you."
    wt_image principal_apology_17
    "You regret not having some alligator paper clips around the house, the type Principal Hannah likely uses every day at the school, but you find the closest things to them that you have in your dungeon and clamp them on her breasts as she tries, a bit unsuccessfully, to avoid crying out."
    hannah.c "Nnnnnn"
    player.c "How about now Hannah? Comfortable yet?"
    wt_image principal_apology_18
    "She grimaces and holds her tongue."
    player.c "Not talking? That makes sense.  You want to preserve your voice for the screaming."
    wt_image principal_apology_52
    "You don't need any fancy equipment to beat her ass in this position.  Any old stick will work ... and hurt.  Hannah's silence doesn't last long ... *thwaackkk*"
    wt_image principal_apology_19
    hannah.c "Aaaghhh"
    "*thwaackkk*"
    wt_image principal_apology_51
    hannah.c "Aaaghhh!!!"
    "*thwaackkk*"
    wt_image principal_apology_19
    hannah.c "AAAAGGHHH!!!!"
    wt_image principal_apology_20
    "As fun as this is, you need to stop when the skin on her ass is threatening to break. Hurting her is one thing., beating her until she bleeds is something else entirely."
    if dungeon.has_item(fuck_machine) and dungeon.has_item(gags):
        $ title = "Give her a new experience?"
        menu:
            "Put her on the fuck machine":
                wt_image principal_apology_21
                "You promised her no sex with you. You didn't say anything about sex with a machine. You sit her upright and harness a ballgag in position to reinforce her helplessness..."
                wt_image principal_apology_22
                "... then you reposition the clamps on her sore nipples ..."
                wt_image principal_apology_23
                "... and place her on the fuck machine."
                wt_image principal_apology_24
                "In theory, being fucked by an impersonal, unwavering, continually thrusting and vibrating machine has the potential to be enjoyable."
                wt_image principal_apology_25
                "Principal Hannah's contortions, however, make it clear that when you are not even remotely turned on by the situation, and are placed on the machine by a man you don't particularly like, the pounding of the machine inside you is truly just another form of torture."
                "*whumpp* *whumpp* *whumpp* *whumpp* *whumpp* *whumpp*"
                wt_image principal_apology_26
                hannah.c "aaaaaagggggghhhhhhhh"
                "When the sound of her screaming can be heard clearly through the ballgag, you know she's taken as much as she can."
                call hannah_punishment_enough from _call_hannah_punishment_enough_2
            "She's had enough":
                call hannah_punishment_enough from _call_hannah_punishment_enough_3
    else:
        call hannah_punishment_enough from _call_hannah_punishment_enough_4
    return

label hannah_punishment_enough:
  wt_image principal_apology_27
  "The now disheveled school Principal has been shaken by your punishment, but retains her fiery spirit. She looks up at you with disgust as you release her from her bonds."
  hannah.c "You're sick.  I suppose hurting me turned you on?"
  $ title = "What do you do?"
  menu:
    "Take out your cock":
      add tags 'took_out_cock_punishment_call' to hannah
      "You remove your hard on from your pants."
      player.c "Yes, it seems it did."
      hannah.c "You're disgusting.  And I said no sex."
      $ title = "What do you do?"
      menu:
        "Jerk off on her":
          player.c "I agreed to no touching you. I didn't say anything about not touching me. If I were you, I'd pull your hair back. This is going to be easier to clean off your face than out of your hair."
          wt_image principal_apology_53
          "She looks on in revulsion as you jerk off, your cock inches from her face."
          wt_image principal_apology_54
          player.c "[player.orgasm_text]"
          wt_image principal_apology_28
          player.c "You should have saved the 'that's disgusting' comment, Principal Hannah.  Now you've got nothing to come back with."
          $ hannah.facial_count += 1
          orgasm
        "Let her go":
          "You put your cock back in your pants."
          player.c "You wanted to know if I was turned on. I was showing you I was."
          hannah.c "I've heard about people like you. I hoped I'd never meet one."
          player.c "You've met us before.  You've just never before done anything stupid enough to fall under the control of one of us."
    "Admit you're turned on":
      player.c "Yes, it did."
      hannah.c "I've heard about people like you. I hoped I'd never meet one."
      player.c "You've met us before. You've just never before done anything stupid enough to fall under the control of one of us."
    "Ignore her comment":
      pass
  if hannah.has_tag('thank_you_visit'):
    player.c "I hope you've learned your lesson, Principal Hannah. If you want to keep your school and yourself safe, be more grateful to your benefactors in the future."
  elif hannah.has_tag('lawyer_call'):
    player.c "I hope you've learned your lesson, Principal Hannah. If you want to keep your school and yourself safe, consider your actions more carefully in the future."
  hannah.c "You've made your point. Can I go now?"
  "You let her leave and get back to your day."
  if hannah.has_tag('thank_you_visit'):
    $ hannah.letter_re_terri = 16
  elif hannah.has_tag('lawyer_call'):
    $ hannah.letter_re_terri = 11 # opens up potential for her to torture Bethany post bank events
  change player energy by -energy_short
  return

# End Day - Principal Event: Lawyer call? (must precede Letter event)
label hannah_lawyer_call:
  $ hannah.training_session()
  $ hannah.visit_week = 0
  rem tags 'no_hypnosis' from hannah
  hannah.c "I'm here to apologize."
  hannah.c "I heard from your lawyer. I understand how hurtful the allegations I made were. That wasn't my intention."
  hannah.c "I was just trying to protect my students. I'm sorry I suggested that you might have been a corrupting influence on them."
  hannah.c "As your lawyer pointed out, I have no legally acceptable evidence you were even at my school, let alone that you were doing anything wrong. I should never have made defamatory statements about you in my letter."
  hannah.c "I really am very sorry."
  hannah.c "Please, can you call off your lawyer? She's threatening to sue. We're a very poor school. It's everything I can do to keep things running as it is. We can't afford to fight you in court. We couldn't pay what your lawyer is asking for anyway."
  $ hannah.hypnotize = False
  $ hannah.ask_for_money = False
  $ title = "What do you do?"
  menu menu_hannah_lawyer_call:
    "Hypnotize her" if player.can_hypno(hannah) and not hannah.hypnotize and not hannah.ask_for_money:
      "Principal Hannah is too agitated for you to hypnotize right now."
      $ hannah.hypnotize = True
      $ title = "What do you do?"
      jump menu_hannah_lawyer_call
    "Accept her apology" if not hannah.ask_for_money:
      call hannah_lawyer_call_apology from _call_hannah_lawyer_call_apology_2
    "Ask for money" if not hannah.ask_for_money:
      player.c "How much can you afford?"
      hannah.c "I told you, we're a poor school. Anything I pay you would reduce the quality of the education we can provide to the children."
      player.c "If my lawyer sues you, there'll be a lot of money coming out of your budget. What are you offering me to avoid that?"
      "Principal Hannah hesitates for a moment."
      hannah.c "200. I could pay you 200, but I really couldn't pay any more. You might as well go ahead and sue us."
      $ hannah.ask_for_money = True
      $ title = "What do you do?"
      jump menu_hannah_lawyer_call
    "Accept 200" if hannah.ask_for_money:
      wt_image principal_apology_3
      player.c "Fine. I'll take the 200."
      hannah.c "You'd really take that away from the children's education?"
      player.c "Deduct it from your own salary. Consider it a penalty for issuing imprudent threats."
      hannah.c "I'll have the money credited it to you. Good day."
      "She leaves, unhappy."
      $ hannah.letter_re_terri = 10
      change player money by 200 notify
    "Ask for other compensation":
      wt_image principal_apology_4
      player.c "I'll let you keep your money, Principal. You'll pay for insulting me another way."
      hannah.c "What do you mean?"
      $ title = "How should she pay?"
      menu:
        "Let you punish her":
          player.c "You're going to let me punish you."
          hannah.c "What?  How?"
          player.c "I'm going to take you into my dungeon, strip you naked, and discipline you physically."
          hannah.c "You can't be serious?  Why would I let you do that?"
          player.c "Because you're the one at fault here. You brought this on yourself and your school. If you don't want your students to pay for your transgression, you'll agree to take your punishment like a big girl, and save your students the financial consequences of your actions."
          hannah.c "Fine. But no touching me sexually."
          call hannah_punishment_call from _call_hannah_punishment_call_1
        "Let you have sex with her":
          player.c "You say you're sorry and you want to make it up to me. So show me. Start by pulling up your dress."
          hannah.c "You can't be serious?"
          player.c "I'm very serious. If you want me to call off my lawyer, you need to provide me with alternative compensation."
          player.c "Lift the dress or get out of my house."
          call hannah_forced_sex_call from _call_hannah_forced_sex_call_1
  rem tags 'lawyer_call' 'first_visit_partially_undressed' from hannah
  call character_location_return(hannah) from _call_character_location_return_687
  add tags 'no_hypnosis' to hannah
  notify
  return

label hannah_lawyer_call_apology:
  $ hannah.letter_re_terri = 4 #successful conclusion, but no booty calls; can be amended later for Playboy
  player.c "I accept your apology, Principal Hannah. I appreciate you taking the time to come here and deliver it in person."
  "A visible wave of relief washes over her."
  hannah.c "Oh thank you!"
  hannah.c "You have no idea how difficult it is keeping the school running on our current budget. I don't know how I would have balanced our expenses if we had to make an unexpected payment."
  $ hannah.hypnod = False
  $ hannah.money = False
  $ hannah.relax = False
  $ hannah.romp = False
  $ title = "What do you do?"
  menu menu_hannah_lawyer_call_apology:
    "Hypnotize her" if player.can_hypno(hannah) and not hannah.hypnod and not hannah.money and not hannah.relax:
      $ hannah.hypnod = True
      $ hannah.hypno_session() # deducts energy and records she was hypnotized
      "She seems relaxed enough now that she should be open to hypnosis."
      player.c "Principal Hannah, please look at this."
      call focus_image from _call_focus_image_21
      player.c "You and I are going to have a talk, Hannah.  We are going to talk and you are going to listen to me.  Listen to me now.  Listen to me.  Only to me.  Only my words now.  Only my words."
      if hannah.has_tag('first_visit_partially_undressed'):
        wt_image principal_apology_32
      else:
        wt_image principal_apology_29
      "She soon falls under your trance."
      player.c "Let's be comfortable for our talk, Hannah. You're grateful that I accepted your apology and want me to be comfortable around you."
      if not hannah.has_tag('first_visit_partially_undressed'):
        extend " Pull down the top of your dress, so that you and I will be comfortable for our talk."
        wt_image principal_apology_30
      hannah.c "Of course!  I didn't like the tension of sending that letter and then having to come here to apologize. I had no idea what sort of a man you were."
      hannah.c "I'm so glad that you're a reasonable person and that you accepted my apology."
      if hannah.has_tag('first_visit_partially_undressed'):
        player.c "Take the rest of your clothes off, Hannah. Everything will feel so much more open and relaxed between us once you are naked. All the tension will be gone and we can relax and talk like friends."
      else:
        wt_image principal_apology_31
        hannah.c "Is this better?"
        player.c "Having your dress hanging open is very awkward, Principal. Take the whole dress off so that we can be more comfortable."
        wt_image principal_apology_32
        hannah.c "This is awkward.  I'll take my dress off completely."
        player.c "Take the rest of your clothes off too, Hannah. Everything will feel so much more open and relaxed between us once you are naked. All the tension will be gone and we can relax and talk like friends."
      wt_image principal_apology_33
      hannah.c "Is this better? Do you feel less tense and more comfortable?"
      player.c "It seems like you're hiding something, Hannah. Sitting with your legs crossed like that make it seem like you don't want to be open with me. You want to be open with me, Principal Hannah. You want me to know that you have nothing to hide."
      wt_image principal_apology_34
      hannah.c "I don't want you to think I'm hiding anything. I want you to see me as an open book."
      $ title = "What do you do?"
      menu:
        "Ask her to complete her apology":
          player.c "You want to complete your apology now, Hannah. You want to complete your apology so that I know you are sorry for what you did."
          hannah.c "I already offered my apology and you accepted it. You already know that I'm sorry."
          if player.has_tag('hypnotist') or player.hypnosis_level > 10:
            player.c "You're grateful to me for accepting your apology, Hannah.  You want me to know how thankful you are that I accepted your apology and saved your school from financial ruin. You don't want me to think that you are not grateful. You want to complete your apology in a way that will let me know how grateful you are."
            player.c "You want to suck my cock so that I will know how grateful you are."
            wt_image principal_apology_35
            "She accepts your cock as you offer it to her."
            hannah.c "I want you to know how thankful I am that you accepted my apology."
            player.c "If you're truly grateful, Hannah, you will lick my balls before you suck my cock. You are truly grateful Hannah and you will show me that by licking my balls before you suck my cock."
            wt_image principal_apology_36
            hannah.c "Of course!"
            wt_image principal_apology_55
            player.c "When I cum, you'll show me how grateful you are for accepting your apology by swallowing my load Hannah.  Keep your eyes on me while I fill your mouth with my jizz, then swallow every drop so that I know how thankful you are."
            wt_image principal_apology_37
            "She watches you intently and makes a big show of swallowing your cum after you let go inside her."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_blowjob_count += 1
            $ hannah.hypno_swallow_count += 1
            orgasm
            $ title = "What do you do now?"
            menu:
              "Finish your chat":
                jump menu_hannah_lawyer_call_apology
              "Show her out":
                "You enjoy the sight of the school Principal's naked body for a few more minutes, then have her dress, bring her out of her trance, and show her to the door so you can get on with your day."
          else:
            "You're not a strong enough a hypnotist to convince her to complete her apology."
            jump menu_hannah_lawyer_call_apology
        "Finish your chat":
          jump menu_hannah_lawyer_call_apology
    "What about a quick romp?" if hannah.relax and not hannah.romp:
      player.c "We don't have to make it a big formal date to spend some time together, you know. I know you're busy. I'm busy too."
      player.c "We're also human. A little company from time to time, you know, to help out with some natural human needs.  There's nothing wrong with that."
      if player.has_tag('supersexy'):
        if hannah.hypnod:
          pass
        elif hannah.has_tag('first_visit_partially_undressed'):
          wt_image principal_apology_32
        else:
          wt_image principal_apology_4
        hannah.c "You mean like a booty call?  Me, with you?"
        player.c "Whenever you're in the mood."
        hannah.c "I'll have to think about it."
        "You're sure she will."
        $ hannah.letter_re_terri = 7 # opens booty calls
        $ hannah.visit_week = week
      else:
        hannah.c "No, there isn't anything wrong with that. As long as you're not doing it at my school. But I'm not looking for a 'friend with benefits'. "
      $ hannah.romp = True
      jump menu_hannah_lawyer_call_apology
    "Suggest you could help with the money" if not hannah.money:
      player.c "Perhaps I could help you find a solution to your money problems?"
      hannah.c "I have it under control, thank you. As long as nothing unexpected arises, we can manage."
      add tags 'first_visit_discussed_money' to hannah
      $ hannah.money = True
      jump menu_hannah_lawyer_call_apology
    "Suggest you could help her relax" if not hannah.relax:
      player.c "Perhaps I could help you take your mind off your responsibilities.  Recharge your battery so to speak.  When's the last time you did something fun?"
      hannah.c "Don't you already have a girlfriend?  The woman you brought to the school."
      player.c "I'm not committed to anybody right now."
      hannah.c "Neither am I, but I'm not looking to become committed either.  The school and its students are my life."
      if player.has_tag('supersexy'):
        hannah.c "You're really good looking, but I'm not at a point in my life where I want to be dating anyone right now."
      else:
        hannah.c "I'm not at a point in my life where I want to be dating anyone right now."
      $ hannah.relax = True
      $ title = "What do you do?"
      jump menu_hannah_lawyer_call_apology
    "Show her out":
      "You show Hannah to the door and get on with your day."
  return

# End Day - Principal Event: First School Visit
label hannah_first_school_visit:
  wt_image letter
  "A letter comes for you in today's mail."
  hannah.c "{i}Dear Sir, A man matching your description was recently spotted entering school property with a young woman and engaging in inappropriate behavior on school grounds.{/i}"
  hannah.c "{i}Your actions have the potential to be a corrupting influence on our children. I will not tolerate lewd or lascivious proceedings on school grounds. Nor will I allow you to undermine the moral development of our young people.{/i}"
  hannah.c "{i}Full legal action shall be brought against you as necessary to protect the students under our care. ~ Principal Hannah{/i}"
  $ title = "What do you do?"
  menu:
    "Go visit the Principal":
      rem tags 'no_hypnosis' from hannah
      $ hannah.training_session()
      call forced_movement(school) from _call_forced_movement_978
      wt_image school.image
      "You decide it might be best to clear this up with a visit to the Principal's office."
      summon hannah
      wt_image principal_office_19
      "Principal Hannah is in her office when you arrive."
      hannah.c "You wanted to see me?"
      player.c "It's about this letter."
      wt_image principal_office_1
      "She bristles when she realizes who you are."
      hannah.c "What about it? I think I made myself clear. I don't want you anywhere near our students."
      $ hannah.complain = False
      $ hannah.admit = False
      $ hannah.convince = False
      $ hannah.money = False
      $ hannah.relax = False
      $ hannah.responsibility = False
      while hannah.letter_re_terri == 1:
        $ title = "What do you do?"
        menu:
          "Hypnotize her" if player.can_hypno(hannah):
            player.c "Principal Hannah, please look at this."
            call focus_image from _call_focus_image_22
            player.c "You and I are going to have a talk.  You are going to listen to me.  Listen to me now.  Listen to me.  Only me.  Only my words now.  Only my words."
            wt_image principal_office_2
            "She soon falls under your trance."
            player.c "Let's be comfortable for our talk, Hannah.  You want to be comfortable around me.  You want me to be comfortable around you."
            wt_image principal_office_20
            player.c "Remove your blouse, Principal, so that you and I will be comfortable for our talk."
            wt_image principal_office_3
            "As Hannah pulls off her top, she starts talking to you."
            hannah.c "Of course I want you to be comfortable for our talk, but you shouldn't be here.  You're a corrupting influence on our children and you shouldn't be on our school grounds."
            $ hannah.strip = False
            $ hannah.desk = False
            $ hannah.spread = False
            $ title = "How do you respond?"
            menu menu_hannah_visit_school_hypnotize:
              "Ask her to strip completely" if not hannah.strip:
                player.c "I can see this is a difficult conversation for you Principal Hannah.  It's a difficult conversation for me, too."
                player.c "I am your friend.  I don't want there to be conflict between us.  You don't want there to be conflict between us."
                player.c "You want to make this conversation as comfortable as possible between us.  You want to be open and non-threatening to me."
                player.c "Show me that you are open and non-threatening, Principal Hannah.  Remove the rest of your clothes to make the rest of this conversation less difficult for both of us."
                if player.has_tag('hypnotist') or player.hypnosis_level > 10:
                  wt_image principal_office_4
                  "Hannah removes her clothes and lays them neatly on the chair and desk beside her."
                  hannah.c "I don't want to be threatening, but I have a responsibility to the children. As the Principal of this school I need to do whatever it takes to keep the students safe."
                  hannah.c "You should not be on our school grounds.  If you don't leave, I may be forced to call the police and have you removed."
                  $ hannah.strip = True
                else:
                  hannah.c "No"
                  "You're not a strong enough hypnotist to convince her to go any further on this path."
                jump menu_hannah_visit_school_hypnotize
              "Ask her to get on her desk" if hannah.strip and not hannah.desk:
                player.c "You're tense, Hannah.  I can see it in your body language.  This is difficult for you.  It's difficult for me, too.  I am your friend.  I don't want you to feel tense around me."
                player.c "Relax.  Climb up on your desk and make yourself comfortable.  You'll feel more comfortable.  I'll feel more comfortable.  Then we can have a friendly chat and resolve this conflict so that no one needs to feel tense."
                wt_image principal_office_5
                "She crawls up on the desk and faces you."
                hannah.c "If this helps you to feel less tense, then of course we can talk like this.  My tension isn't going away, though, as long as you're here.  I have a duty to the students to protect their moral character and keep them safe from negative influences."
                hannah.c "You're a negative influence, and I need you to leave the school grounds and not come back.  If you don't do that, I will call the police and have you arrested."
                $ hannah.desk = True
                $ title = "How do you respond?"
                jump menu_hannah_visit_school_hypnotize
              "Tell her to spread her legs" if hannah.desk and not hannah.spread:
                player.c "It's so difficult to relax and feel comfortable with you, Hannah, when you keep yourself so closed up.  Open yourself up for me and make yourself comfortable.  You'll feel more comfortable.  I'll feel more comfortable.  Then we can have a friendly chat and resolve this conflict."
                wt_image principal_office_13
                hannah.c "I hope this makes you more comfortable.  This is as open as I can be with you.  I need you to leave now and promise never to come back, otherwise I'll have no choice but to call the police and have you arrested."
                $ hannah.spread = True
                $ title = "How do you respond?"
                jump menu_hannah_visit_school_hypnotize
              "Instruct her to call the police like this" if hannah.desk:
                player.c "You're right, Principal Hannah.  You need to protect the children."
                player.c "Call the police to warn them about a negative influence in the school.  Stay right where you are when you call them."
                player.c "Stay right where you are while you wait for them to arrive.  This is the best vantage point in the school to keep an eye out for possible threats to the students."
                player.c "Keep your clothes off.  You want the police to feel welcome when they arrive.  They are going to help you protect the students.  You want them to feel welcomed and comfortable when they come to help you."
                player.c "You should thank the police for coming to help protect the school.  You want the police to feel thanked.  Offer to thank them when the arrive.  Make sure they know that you're willing to do anything they'd like to thank them for protecting the school."
                player.c "I'm going to leave now.  You don't remember who I am or what I look like.  You don't remember anything we talked about.  All you remember is that there is a threat to the school and that's why you called the police."
                player.c "Do you understand, Principal Hannah?"
                wt_image principal_office_22
                hannah.c "Yes.  I will call the police.  They will come and protect the school.  I will stay here and keep a look out until they arrive."
                hannah.c "When they arrive, I'll make sure they are comfortable and offer to thank them for protecting the school."
                hannah.c "I don't remember who you are or what you look like or what we talked about.  I just know there is a threat and I need the police."
                "They don't know it, but the police owe you one.  At least any future threats by Principal Hannah won't be taken seriously."
                $ hannah.letter_re_terri = 5
              "Convince her you're not a threat":
                player.c "I am not a threat to the students, Principal Hannah.  I am your friend.  I care about the students.  I am not a danger to them."
                hannah.c "You had sex in the school while the children were here.  You are a corrupting influence.  You should not be here.  You need to go and never come back."
                $ title = "How do you respond?"
                menu:
                  "You were doing research":
                    player.c "That was research for a new sex education program, Principal Hannah.  It was very professional.  It was not a threat to the students.  Young adults need to learn about safe sex."
                    hannah.c "No one told me about any research taking place in my school."
                    player.c "You should have been told. I understand why you are upset. I didn't know you had not been told about my research.  I didn't want to upset you.  I only want what's best for the students."
                    hannah.c "You can't do that research here while school is in.  If the children's parents found out they would be very upset."
                    player.c "I won't do sex research in your school without your knowledge, Principal Hannah.  You'll be informed of any future research."
                    hannah.c "Okay.  Thank you for clearing up this misunderstanding."
                    $ title = "How do you respond?"
                    menu:
                      "Ask her to participate in your research":
                        player.c "You should participate in my research, Principal Hannah.  You would be helping the students by improving the quality of the sex education they receive."
                        hannah.c "Thank you for the offer.  That's very kind, but I don't have the time.  The school's finances are in such bad shape, it's everything I can do to keep the school running as it is."
                        player.c "That's too bad.  Perhaps I could help?"
                        hannah.c "No, you should focus on your research.  As long as nothing unexpected happens, I have a plan to keep the school running properly. I just need to make that my focus.  That and keeping the students safe from corrupting influences, of course."
                        player.c "You're doing an excellent job, Principal Hannah."
                        if hannah.desk:
                          wt_image principal_office_22
                        hannah.c "Thank you!"
                        "You shouldn't have any future problems with Principal Hannah."
                        $ hannah.letter_re_terri = 4
                      "Leave":
                        "You shouldn't have any future problems with Principal Hannah."
                        $ hannah.letter_re_terri = 4
                  "You need sex":
                    player.c "I will go, Principal Hannah.  I just need your help first.  The sight of your beautiful body has made me horny. I need an orgasm, Hannah. Once you and I have had sex, I'll leave and you will have done your job.  You will have removed me from the school and kept the children safe."
                    hannah.c "You should have sex with your girlfriend.  You shouldn't be coming here for sex."
                    player.c "You're the one who's made me horny, Principal Hannah.  You should be the one to have sex with me."
                    hannah.c "No, I won't have sex with you.  If you have sex with me, you'll want to come back and have sex with me again."
                    hannah.c "I need you to leave the school.  I can't do something that'll encourage you to come back."
                    $ title = "How do you respond?"
                    menu:
                      "Promise never to come back":
                        call hannah_first_school_visit_promise from _call_hannah_first_school_visit_promise
                      "Convince her she wants to have sex":
                        player.c "You want to have sex with me, Hannah.  You enjoy the thought of having sex with me. You know that when I'm having sex with you, I'm not threat to the moral fiber of the students."
                        hannah.c "No.  No, I don't want to have sex with you.  I'm not interested in sex.  I only care about the school and the students."
                        $ title = "How do you respond?"
                        menu:
                          "Promise never to come back":
                            call hannah_first_school_visit_promise from _call_hannah_first_school_visit_promise_1
                          "Agree to go":
                            player.c "You're a good Principal, Hannah.  You care about the students.  I respect that. I'm your friend. I care about the children, too. I needed to test you, to make sure that you were a strong moral person who would keep the students safe."
                            player.c "I know now that you are doing a good job.  I can go now.  The school is safe.  The students are safe.  I'm not a threat.  I'm your friend."
                            if hannah.desk:
                              wt_image principal_office_22
                            hannah.c "Oh, good!"
                            "You shouldn't have any future problems with Principal Hannah."
                            $ hannah.letter_re_terri = 4
            $ hannah.hypno_session() # deducts energy and records she was hypnotized
          "Take this to Janice the Lawyer" if player.has_tag('lawyer_on_retainer') and hannah.complain and not hannah.admit:
            wt_image principal_office_21
            "You decide to let Janice look after this.  That's what she's for.  You leave, with Hannah glaring after you."
            $ hannah.visit_week = week
            $ hannah.letter_re_terri = 8
          "Convince her to lighten up" if hannah.admit and not hannah.convince:
            player.c "Oh come on Hannah.  Lighten up.  The woman I was with has a bit of a schoolgirl fantasy.  I indulged her.  She had fun.  I had fun.  No one got hurt."
            player.c "I'm not a threat to anyone, certainly not to your students.  I help people.  Women in particular."
            player.c "Don't you have fantasies from time to time?  Surely you can understand how nice it is to share them with someone who's non-judgmental.  Someone who can help spice up your life with a little harmless fun?"
            hannah.c "I'm not sharing my fantasies with you, sexual or otherwise.  I'm certainly not looking for anyone to spice up my life."
            hannah.c "This school and its students are my life.  I have a hard enough time keeping everything running on the limited resources we have."
            hannah.c "I don't have time to worry about perverts running around my school indulging their fantasies over our teaching supplies."
            $ hannah.convince = True
          "Apologize":
            player.c "I understand.  I want to apologize for putting you in an awkward situation.  I didn't intend to cause problems for you or your students"
            player.c "In fact, I'm quite certain that I didn't cause any problems for any of your students.  But I do regret causing you anxiety."
            wt_image principal_office_19
            hannah.c "Thank you.  It was good of you to come here and say that."
            hannah.c "I'm sorry about the tone of the letter.  It's just that I care deeply about this school and the students.  Perhaps I can be overly protective sometimes."
            $ title = "How do you respond?"
            menu menu_hannah_visit_school_apologize:
              "That's a big responsibility" if not hannah.responsibility:
                player.c "That's a big responsibility."
                hannah.c "It is, and our precarious financial situation doesn't make it any easier."
                $ hannah.responsibility = True
                jump menu_hannah_visit_school_apologize
              "Perhaps I could help with the money" if hannah.responsibility and not hannah.money:
                player.c "Perhaps I could help you find a solution to your money problems?"
                hannah.c "I have it under control, thank you.  As long as nothing unexpected arises, we can manage."
                add tags 'first_visit_discussed_money' to hannah
                $ hannah.money = True
                jump menu_hannah_visit_school_apologize
              "Perhaps I could help you relax" if hannah.responsibility and not hannah.relax:
                player.c "Perhaps I could help you take your mind off your responsibilities.  Recharge your battery so to speak.  When's the last time you did something fun?"
                hannah.c "Don't you already have a girlfriend?  That woman you brought to the school?"
                player.c "I'm not committed to anybody right now."
                hannah.c "Neither am I, but I'm not looking to become committed either.  This school and its students are my life."
                if player.has_tag('supersexy'):
                  hannah.c "You're really good looking, but I'm not at a point in my life where I want to be dating anyone right now."
                else:
                  hannah.c "I'm not at a point in my life where I want to be dating anyone right now."
                $ hannah.relax = True
                jump menu_hannah_visit_school_apologize
              "What about a quick romp?" if hannah.relax:
                player.c "We don't have to make it a big formal date to spend some time together, you know.  I know you're busy.  I'm busy, too."
                player.c "We're also human.  A little company from time to time, you know - to help out with some natural human needs.  There's nothing wrong with that."
                if player.has_tag('supersexy'):
                  wt_image principal_office_2
                  hannah.c "You mean like a booty call?  Me, with you?"
                  player.c "Whenever you're in the mood."
                  hannah.c "Not here.  It could never be here."
                  player.c "At my house then.  When the urge strikes you."
                  hannah.c "I'll think about it."
                  "You're sure she will."
                  $ hannah.letter_re_terri = 7 # opens up booty calls
                  $ hannah.visit_week = week
                else:
                  hannah.c "No, there isn't anything wrong with that.  As long as you're not doing it here at my school.  But I'm not looking for a 'friend with benefits'."
                  wt_image principal_office_21
                  hannah.c "If you'll excuse me, I have a lot of work to do.  Can I trust you to find your way out of here?"
                  "You shouldn't have any more trouble with Principal Hannah."
                  $ hannah.letter_re_terri = 4 # resolves issue but no booty calls
              "That's settled then":
                wt_image principal_office_21
                hannah.c "If you'll excuse me, I have a lot of work to do.  Can I trust you to find your way out of here?"
                "You shouldn't have any more trouble with Principal Hannah."
                $ hannah.letter_re_terri = 4 # resolves issue but no booty calls
          "Complain about the threat" if not hannah.complain and not hannah.admit:
            player.c "You made yourself very clear, and I don't take kindly to threats."
            hannah.c "I wasn't threatening you."
            player.c "You were, actually.  You accused me of morally reprehensible acts and threatened to bring legal action against me."
            hannah.c "Well, if you pose a threat to the moral upbringing of my students, then I'll take whatever action is required to protect them."
            player.c "And if you bring legal action against me for unsubstantiated claims that demean my reputation I'll not only defend myself but bring counterclaim against you and your school for defamation."
            hannah.c "I'm not going to be bullied out of doing my job and protecting my students."
            $ hannah.complain = True
          "Admit you did it" if not hannah.admit:
            player.c "You're right. I brought a woman here and I fucked her in one of your classrooms.  What's the big deal?  The classroom was empty.  There weren't any students around to see us."
            hannah.c "Why would you do that?"
            player.c "I'm a sexual person.  I like to fuck.  It's fun."
            hannah.c "But why here?  In a school?  You had no right to be here and do that.  If I ever catch you on the grounds of this school again, I'll call the police."
            $ hannah.admit = True
          "Go" if hannah.convince:
            player.c "I'm sorry you feel that way.  We could have had some fun together, you and I."
            player.c "Anyway, I'm not a threat.  I hope you can see that now."
            wt_image principal_office_21
            hannah.c "Just stay away from my school."
            "You shouldn't have any more trouble with Principal Hannah, but you should probably stay away from her school in the future."
            $ hannah.letter_re_terri = 4
          "Leave things at that" if hannah.complain and not hannah.admit:
            player.c "And I'm not going to stand around and let you diminish my standing in this community with derogatory statements about me.  Do you understand me?"
            wt_image principal_office_21
            hannah.c "I understand you.  Now get out of my school and don't ever let me see you here again or I'll call the police. Do you understand me?"
            "Well, that's a resolution of sorts."
            $ hannah.letter_re_terri = 3
      add tags 'no_hypnosis' to hannah
      call character_location_return(hannah) from _call_character_location_return_688
      call forced_movement(living_room) from _call_forced_movement_47
    "Have Janice the Lawyer handle it" if player.has_tag('lawyer_on_retainer'):
      "You decide to let Janice look after this.  That's what she's for."
      $ hannah.visit_week = week
      $ hannah.letter_re_terri = 9
    "Wait until you can get legal advice" if not player.has_tag('lawyer_on_retainer'):
      add tags 'principal_event_postponed' to hannah
      "Despite the threatening tone of the letter, it doesn't sound like they have any grounds to take action against you."
      "Still, it may be best to review this with a lawyer, if you can get a good one on retainer.  In the meantime, it'd be prudent to avoid the school."
      $ hannah.letter_re_terri = 2
    "Ignore it":
      "Despite the threatening tone of the letter, it doesn't sound like they have any grounds to take action against you."
      "Still, it may be prudent to avoid the school in the future."
      $ hannah.letter_re_terri = 2
  wt_image current_location.image
  return

label hannah_first_school_visit_promise:
  player.c "I'll go, Principal Hannah, and I'll never come back.  I promise never to come back here, but you need to do something for me."
  player.c "You need to have sex with me, so that I'm no longer horny.  Once you have sex with me, I'll leave and not come back."
  hannah.c "I'm not going to have sex with you."
  if player.has_tag('hypnotist') or player.hypnosis_level > 10:
    hannah.c "I will, however, give you a hand job, if you agree to never come back here again.  Otherwise, I'll need to call the police."
  else:
    "You're not a strong enough hypnotist to get her to go down this path."
  $ title = "How do you respond?"
  menu:
    "Agree to a hand job" if player.has_tag('hypnotist') or player.hypnosis_level > 10:
      player.c "I accept, Principal Hannah, but we shouldn't make a mess on your office floor.  What would the cleaning staff think?  Jerk me off onto your face instead and I'll leave and not come back."
      wt_image principal_office_23
      hannah.c "Okay, but you can only cum on my face and in my mouth, not in my hair.  Once you're not longer horny and leave, I need to go back to protecting the school, and the students shouldn't see me with cum in my hair."
      wt_image principal_office_10
      "Between the sight of the naked, hypnotized woman kneeling on her office floor in front of you, and the feeling of her soft hand pumping up and down you shaft, you soon shoot your load on her.  Surprisingly, none actually ends up in her hair."
      player.c "[player.orgasm_text]"
      wt_image principal_office_24
      hannah.c "I don't think you're horny anymore.  You need to leave now and never come back."
      wt_image principal_office_25
      "You shouldn't have any future trouble with Principal Hannah, but it would be best to stay away from the school."
      $ hannah.hypno_handjob_count += 1
      $ hannah.hypno_facial_count += 1
      $ hannah.letter_re_terri = 6
      orgasm notify
    "Insist on sex":
      player.c "That's not good enough, Hannah.  I need you to have sex with me."
      hannah.c "No.  No, you should only be having sex with your girlfriend.  You're trying to corrupt me just like you're corrupting the students."
      wt_image principal_office_26
      "She moves towards the phone, your hold over her having been broken.  You leave before she can complete her call to the police."
      wt_image current_location.image
      "Hopefully, she'll be confused enough by the trance and her naked state not to have a coherent story to tell them, and you didn't commit any crimes in any event.  It would likely be best, however, if you stay away from the school in the future."
      $ hannah.letter_re_terri = 3
    "Agree to go":
      player.c "You're a good Principal, Hannah. You care about the students. I respect that. I'm your friend. I care about the children, too. I needed to test you, to make sure that you were a strong moral person who would keep the students safe."
      player.c "I know now that you are doing a good job. I can go now. The school is safe. The students are safe. I am not a threat. I'm your friend."
      hannah.c "Oh good!"
      "You shouldn't have any future problems with Principal Hannah."
      $ hannah.letter_re_terri = 4
  return

# End Day - Principal Visit to Club Pres & Gloria
label hannah_visit_gloria:
  summon hannah
  wt_image principal_club_pres_16
  "Hannah the School Principal wakes you with a knock on your door early in the morning."
  hannah.c "Come on.  Let's go see these donor friends of yours."
  player.c "It's early."
  wt_image principal_club_pres_1
  hannah.c "I know. I have a full day of school ahead once we secure the donation from your friends and the financing back in order. Let's go."
  call forced_movement(gloria_house) from _call_forced_movement_979
  summon hannah
  wt_image principal_club_pres_2
  "You're surprised to see the Club President answer his door himself."
  club_president.c "Oh, hi!  I was just getting back from my morning jog."
  hannah.c "Hello!  My name is Hannah.  I'm so pleased that you've agreed to support our school.  Your generous donation is going to secure a quality education for our pupils not only this year, but in the years to come."
  wt_image principal_club_pres_3
  hannah.c "I've brought a copy of our budget for the remainder of the year. I've updated it to reflect the impact of your donation in the shaded column here."
  hannah.c "You can quickly see what an impact your money is going to have. We'll be able to restore basic functions like maintenance services to normal operating levels, return school supplies to recommended standards, and invest in enhanced extracurricular activities to benefit the development of our student's social and creative skills."
  club_president.c "Yes, great.  I like the colored bar graphs."
  hannah.c "They really show the impact you're making in visual terms, don't they?"
  club_president.c "Yeah, look, I haven't had my morning coffee yet.  Why don't you have a word with my wife while I get some.  Gloria!"
  summon gloria
  wt_image principal_club_pres_4
  gloria.c "You must be Hannah. How nice to meet you."
  "Gloria moves in close to Hannah.  Very close.  Too close for the principal's comfort."
  hannah.c "Oh, uh ... hello Gloria.  I'm very pleased to meet you, too.  I can't tell you how grateful I am to you and your husband for helping out our school."
  gloria.c "Don't tell me, sweetie.  Show me.  Let's see your pitch."
  hannah.c "I was just showing your husband the numbers.  If you let me just grab my materials."
  gloria.c "I'm sure your numbers all add up. We'll show them to our accountant and let you know if she has any questions."
  wt_image principal_club_pres_5
  gloria.c "The only materials you need to grab right now are mine, and the only figures my husband is interested in is yours and mine."
  "Gloria takes Hannah's hand and places it on her breast. Instinctively, Hannah pulls her hand away from the unexpected contact with the older woman's private parts."
  wt_image principal_club_pres_6
  "Gloria spins the brunette around and bends her over, revealing her bare bottom."
  gloria.c "Principal Hannah, are you trying to waste our time?  Oh!  You're not wearing any panties.  Is that for the benefit of your students, or me and my husband?"
  hannah.c "For the two for you."
  gloria.c "So you are ready to make a personal pitch for why we should donate to your school?"
  hannah.c "Yes"
  gloria.c "Then why are you wasting our time with numbers?  What do you do with naughty students who waste your time, Principal Hannah?  Do you spank them?"
  hannah.c "No, we don't use corporal punishment any more ... "
  wt_image principal_club_pres_17
  "Gloria's hand lands with a *smack* on Hannah's ass."
  hannah.c "Oww!!"
  wt_image principal_club_pres_6
  gloria.c "I'm not a big believer in spanking either, but sometimes it focuses the wayward on the errors of their ways and gets them started on a better approach."
  wt_image principal_club_pres_17
  "*SMACK*"
  hannah.c "Owwww!!"
  wt_image principal_club_pres_6
  hannah.c "I think I understand the approach you want me to take."
  wt_image principal_club_pres_7
  "Hannah drops down and lifts Gloria's dress, burying her face between the blonde's legs."
  wt_image principal_club_pres_18
  gloria.c "That's better.  Honey!  The Principal's starting her sales pitch!"
  wt_image principal_club_pres_9
  "Hannah is hesitant about how she should proceed ..."
  wt_image principal_club_pres_10
  "... but a guiding hand at the back of her head soon shows her where to concentrate her attention."
  wt_image principal_club_pres_19
  "Gloria helps by directing her husband to the most interesting parts of the principal's presentation ..."
  wt_image principal_club_pres_11
  "... which he seems to enjoy even more than the colored graphs."
  wt_image principal_club_pres_12
  "To convince them to go through with the donation, Hannah has to satisfy the interests of both her patrons ..."
  wt_image principal_club_pres_14
  "... but it's her intervention when they turn their attention to each other ..."
  wt_image principal_club_pres_13
  "... that really closes the deal for her."
  wt_image principal_club_pres_15
  hannah.c "So assuming that met your expectations, I'll take your signature here confirming that you agree to the general terms of the donation, and we'll be able to work with your accountant to confirm the details."
  gloria.c "Yes, that's perfectly fine.  Great presentation, Hannah.  My wife and I were both quite impressed."
  call forced_movement(living_room) from _call_forced_movement_980
  wt_image living_room.image
  "With that looked after, Hannah heads to the school and you head home, your good deed done for the day."
  $ gloria.discussed_principal = 3
  $ hannah.lost_money_and_no_fix = 3
  rem tags 'available_for_school_visit' from hannah
  if hannah.letter_re_terri == 7:
    $ hannah.visit_week = week
  call character_location_return(hannah) from _call_character_location_return_689
  call character_location_return(gloria) from _call_character_location_return_690
  return

# End Day
label hannah_end_day:
    # shut off school visits
    if hannah.has_tag('available_for_school_visit'):
        if not hannah.has_tag('ready_for_sex_at_school') and hannah.lost_money_and_no_fix != 1 and hannah.lost_money_and_no_fix != 2:
            rem tags 'available_for_school_visit' from hannah
    # restore school visits
    else:
        if hannah.has_tag('ready_for_sex_at_school') or hannah.lost_money_and_no_fix == 1 or hannah.lost_money_and_no_fix == 2:
            add tags 'available_for_school_visit' to hannah
    # follow up on letter
    if hannah.has_tag('principal_event_postponed') and player.has_tag('lawyer_on_retainer') and hannah.letter_re_terri == 2:
        wt_image letter
        rem tags 'principal_event_postponed' from hannah
        "Now that you have a lawyer on retainer, you need to decide what to do about the threatening letter the school principal sent you."
        $ title = "What do you do?"
        menu:
            "Have Janice the Lawyer handle it" if player.has_tag('lawyer_on_retainer'):
                "You send the letter to Janice and ask her to look after this.  That's what she's for."
                $ hannah.visit_week = week
                $ hannah.letter_re_terri = 9
            "Ignore it":
                "Better just to drop it, rather than stir up trouble.  Still, to be prudent, you should likely avoid the school in the future."
    return

# End Week
label hannah_end_week:
  ## Whores Lost
  if hannah.has_tag('whore') and hannah.whore_count > 2:
    $ hannah.whore_lost_countdown -= 1
    if hannah.whore_lost_countdown <= 0:
      "You haven't checked on Hannah for quite a while.  She didn't send your cut this week and there's no news from her at the school.  Whether she left town or got into trouble, you never find out."
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      #call convert(hannah, "unavailable")
      $ hannah.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with school may not be needed going forward; should ideally be cleaned up
      call unconvert(hannah, 'whore') from _call_unconvert_39
    else:
      $ player.whore_income += 15
  ## Domme
  if hannah.has_tag('domme') and hannah.domme_outfit_count > 3:
    $ player.domme_income += 10
  ## Principal Financial Domination?
  if hannah.financial_domination_cost > 0:
    call hannah_financial_domination_event from _call_hannah_financial_domination_event
  ## School Torture Session
  if week >= bethany.torture_week and bethany.torture_week > 0:
    call hannah_school_torture_session from _call_hannah_school_torture_session
  # if hannah.has_tag('ready_for_sex_at_school'):
  #   if hannah.action_contact_visit is not None:
  #     $ hannah.action_contact_visit.condition = "hannah.can_be_interacted and hannah.has_tag('ready_for_sex_at_school')"
  #   elif hannah.action_contact_visit is None:
  #     $ hannah.action_contact_visit = living_room.add_action("Visit Hannah the School Principal", label = hannah.short_name + "_contact_visit", context = "_contact_other", condition = "hannah.can_be_interacted and hannah.has_tag('ready_for_sex_at_school')")
  return

# Hannah Financial Domination Event
label hannah_financial_domination_event:
  wt_image phone_1
  "Your phone is ringing."
  if not hannah.has_tag('first_financial_domination'):
    add tags 'first_financial_domination' to hannah
    $ hannah.random_number = 0
  else:
    $ hannah.random_number = renpy.random.randint(1, 10)
    $ hannah.random_number += hannah.fin_domme_derandomizer
  if hannah.random_number > 6:
    $ hannah.fin_domme_derandomizer = 0
    $ hannah.financial_domination_cost += 5
    $ hannah.fin_domme_outfit_count += 1
    if hannah.fin_domme_outfit_count > 5:
      $ hannah.fin_domme_outfit_count = 1
    if hannah.fin_domme_outfit_count == 1:
      wt_image principal_fin_domme_1_1
      hannah.c "Hi, worm."
      wt_image principal_fin_domme_1_2
      hannah.c "Do you like my new boots?  You paid for them.  Well, technically I gave your money to the school, but then since the school is doing better these days, so I paid myself a bonus and bought these boots with them."
      wt_image principal_fin_domme_1_3
      hannah.c "Nice boots are expensive, worm.  I can't keep buying nice things for the school and myself on the pathetic funds you're sending me."
      wt_image principal_fin_domme_1_2
      hannah.c "So, we're changing our arrangement, worm. From now on, you send me [hannah.financial_domination_cost] each week, starting now.  Understood?"
    elif hannah.fin_domme_outfit_count == 2:
      wt_image principal_fin_domme_2_1
      hannah.c "Hi, worm."
      wt_image principal_fin_domme_2_2
      hannah.c "Do you like the new pants I bought?  You paid for them.  They hug my body nice and tight.  My legs look good in them, don't you agree?"
      wt_image principal_fin_domme_2_2
      hannah.c "My ass looks even better in them, but you're not worthy of getting a look at my ass."
      wt_image principal_fin_domme_2_3
      hannah.c "Nice pants are expensive, worm.  With the pathetic funds you're sending me, I can't keep buying nice things to help me look sexy for the men who are worthy of getting to look at my ass."
      hannah.c "So, we're changing our arrangement, worm.  From now on, you send me [hannah.financial_domination_cost] each week, starting now.  Understood?"
    elif hannah.fin_domme_outfit_count == 3:
      wt_image principal_fin_domme_3_1
      hannah.c "Hi, worm."
      wt_image principal_fin_domme_3_2
      hannah.c "Do you like the new whip I bought?  You paid for it.  It's going to cause somebody a lot of pain when I use it on them."
      wt_image principal_fin_domme_3_3
      hannah.c "Not you, of course.  You're not worth the effort it would take to swing this whip and bring it down on your pathetic ass."
      wt_image principal_fin_domme_3_4
      hannah.c "Buying instruments of pain is expensive, worm.  I need more than the pathetic funds you're sending me to keep myself equipped with the things I need to torture the people who are worthy of my attention."
      wt_image principal_fin_domme_3_5
      hannah.c "So, we're changing our arrangement, worm.  From now on, you send me [hannah.financial_domination_cost] each week, starting now.Understood?"
    elif hannah.fin_domme_outfit_count == 4:
      wt_image principal_face_7
      hannah.c "Hi, worm."
      wt_image principal_fin_domme_4_1
      hannah.c "Do you like my lingerie?  You paid for it."
      wt_image principal_fin_domme_4_2
      hannah.c "This is as much of it as you get see.  Someone's going to get to see me wear it in person, though.  Then they're going to get to take it off me.  Then they're going to get to fuck me."
      wt_image principal_fin_domme_4_3
      hannah.c "Doesn't it make you happy to be buying me clothes so I look sexy for my lovers?"
      wt_image principal_fin_domme_4_4
      hannah.c "Problem is, sexy clothes are expensive, worm.  I can't dress nicely for my lovers on the pathetic funds you're sending me."
      wt_image principal_fin_domme_4_5
      hannah.c "So, we're changing our arrangement, worm. From now on, you send me [hannah.financial_domination_cost] each week, starting now. Understood?"
    elif hannah.fin_domme_outfit_count == 5:
      wt_image principal_face_4
      hannah.c "Hi, worm."
      wt_image principal_fin_domme_5_1
      hannah.c "I was just getting ready to clean the dirt out from between my toes, and it reminded me of you."
      wt_image principal_fin_domme_5_2
      hannah.c "I bet you wish you could be cleaning my feet, don't you, worm?  You'd put your tongue right in there and lick between each toe until I told you to stop."
      wt_image principal_fin_domme_5_3
      hannah.c "Don't get too excited, worm.  This is as close to my feet as you're going to get.  I'm not letting a loser like you touch me, not even to clean my feet with your tongue."
      wt_image principal_fin_domme_5_4
      hannah.c "I'm being very generous to you, letting you have a glimpse of my body like this, worm.  It's more than a loser like you deserves."
      wt_image principal_fin_domme_5_3
      hannah.c "Since I'm being so good to you, you're going to do something from me.  From now on, you send me [hannah.financial_domination_cost] each week, starting now.  Understood?"
    $ title = "Pay her?"
    menu menu_hannah_fin_domme_pay_1:
      "Yes, Mistress" if player.money - player.min_money >= hannah.financial_domination_cost:
        player.c "Yes, Mistress."
        if hannah.fin_domme_outfit_count == 1:
          wt_image principal_fin_domme_1_3
        elif hannah.fin_domme_outfit_count == 2:
          wt_image principal_fin_domme_2_1
        elif hannah.fin_domme_outfit_count == 3:
          wt_image principal_fin_domme_3_1
        elif hannah.fin_domme_outfit_count == 4:
          wt_image principal_fin_domme_4_6
        elif hannah.fin_domme_outfit_count == 5:
          wt_image principal_fin_domme_5_4
          hannah.c "Good worm.  Send that along and I'll send you ... nothing.  It's what you deserve."
          change player money by -hannah.financial_domination_cost
      "I can't afford that much" if not hannah.has_tag('fin_domme_cant_afford'):
        if hannah.financial_domination_cost > 50:
          player.c "I can't afford that much."
          if hannah.fin_domme_outfit_count == 1:
            wt_image principal_fin_domme_1_3
          elif hannah.fin_domme_outfit_count == 2:
            wt_image principal_fin_domme_2_1
          elif hannah.fin_domme_outfit_count == 3:
            wt_image principal_fin_domme_3_2
          elif hannah.fin_domme_outfit_count == 4:
            wt_image principal_face_7
          elif hannah.fin_domme_outfit_count == 5:
            wt_image principal_face_4
          hannah.c "You pathetic loser. Real men know how to make money, worm.  If you were a real man you could afford to send me what I need."
          hannah.c "But since you're not a real man, since you're a sad laughingstock of a man, go ahead and send me what you've been sending so far."
          hannah.c "Know this, though, worm.  Every time I see how little you can afford, I'm going to laugh and be reminded of how useless you are."
          $ hannah.financial_domination_cost -= 5
        else:
          player.c "I can't afford that much."
          if hannah.fin_domme_outfit_count == 1:
            wt_image principal_fin_domme_1_1
          elif hannah.fin_domme_outfit_count == 2:
            wt_image principal_fin_domme_2_1
          elif hannah.fin_domme_outfit_count == 3:
            wt_image principal_fin_domme_3_2
          elif hannah.fin_domme_outfit_count == 4:
            wt_image principal_face_7
          elif hannah.fin_domme_outfit_count == 5:
            wt_image principal_face_4
          hannah.c "You pathetic loser. Real men know how to make money, worm.  If you were a real man you could afford to send me what I need."
          hannah.c "You're not even worth my time, worm.  Did you know that?  The sad little contribution you send, it just reminds me of how useless you are and how little you have to contribute."
          hannah.c "You need to make a decision, worm.  Pay me what I told you to pay, worm, or crawl away and never hear from me again."
        add tags 'fin_domme_cant_afford' to hannah
        jump menu_hannah_fin_domme_pay_1
      "Refuse to pay":
        player.c "I'm sorry, I can't afford to keep paying you."
        if hannah.fin_domme_outfit_count == 1:
          wt_image principal_fin_domme_1_1
        elif hannah.fin_domme_outfit_count == 2:
          wt_image principal_fin_domme_2_1
        elif hannah.fin_domme_outfit_count == 3:
          wt_image principal_fin_domme_3_3
        elif hannah.fin_domme_outfit_count == 4:
          wt_image principal_fin_domme_4_7
        elif hannah.fin_domme_outfit_count == 5:
          wt_image principal_face_3
        hannah.c "You're even more pathetic than I realized."
        wt_image phone_1
        "She hangs up in disgust."
        $ hannah.principal.financial_domination_cost = 0
  else:
    $ hannah.fin_domme_derandomizer += 1
    wt_image principal_fin_domme_0_1
    hannah.c "Hi, worm."
    wt_image principal_fin_domme_0_2
    hannah.c "Are you ready to show me how pathetic you are, by sending me [hannah.financial_domination_cost]?"
    $ title = "Pay her?"
    menu menu_hannah_fin_domme_pay_2:
      "Yes, Mistress" if player.money - player.min_money >= hannah.financial_domination_cost:
        player.c "Yes, Mistress."
        wt_image principal_fin_domme_0_1
        hannah.c "Good worm.  Send that along and I'll send you ... nothing.  It's what you deserve."
        change player money by -hannah.financial_domination_cost
      "I can't afford that much" if not hannah.has_tag('fin_domme_cant_afford'):
        if hannah.financial_domination_cost > 50:
          player.c "I can't afford that much."
          wt_image principal_fin_domme_0_1
          hannah.c "You pathetic loser.  Real men know how to make money, worm.  If you were a real man you could afford to send me what I need."
          wt_image principal_fin_domme_0_3
          hannah.c "But since you're not a real man, since you're a sad laughingstock of a man, I'll lower your tribute."
          hannah.c "Know this, though, worm.  Every time I see how little you can afford, I'm going to laugh and be reminded of how useless you are."
          $ hannah.financial_domination_cost -= 5
        else:
          player.c "I can't afford that much."
          wt_image principal_fin_domme_0_1
          hannah.c "You pathetic loser.  Real men know how to make money, worm.  If you were a real man you could afford to send me what I need."
          wt_image principal_fin_domme_0_3
          hannah.c "You're not even worth my time, worm.  Did you know that?  The sad little contribution you send, it just reminds me of how useless you are and how little you have to contribute."
          hannah.c "You need to make a decision, worm.  Pay me what I told you to pay, worm, or crawl away and never hear from me again."
        add tags 'fin_domme_cant_afford' to hannah
        jump menu_hannah_fin_domme_pay_2
      "Refuse to pay":
        player.c "I'm sorry, I can't afford to keep paying you."
        wt_image principal_fin_domme_0_4
        hannah.c "You're even more pathetic than I realized."
        wt_image phone_1
        "She hangs up in disgust."
        $ hannah.principal.financial_domination_cost = 0
  rem tags 'fin_domme_cant_afford' from hannah
  wt_image current_location.image
  return

# School Torture Session - Hannah, Bethany, Alexis
label hannah_school_torture_session:
  # if not Alexis Torture Session ## note: no real reason for the if else chain to be written this way other than it's the old Rags format, which hasn't been cleaned up
  if alexis.principal_torture_status != 2:
    $ bethany.torture_week = 0
    $ hannah.temporary_count = 0
    # Bethany's second torture session
    if master_m.lend_diamond_to_school != 2 and (bethany.torture_count == 3 or bethany.torture_count == 4):
      $ hannah.temporary_count = 1
      wt_image phone_1
      "Your phone is ringing."
      wt_image banker_school_2_18
      "It's Hannah, the School Principal."
      hannah.c "I wanted to let you know that our next show is tonight.  Today's victim will be Bethany, again.  I hope you're not getting bored with watching her suffer?"
      wt_image banker_school_2_19
      if bethany.torture_count == 4:
        hannah.c "Since you were good enough to donate your time - and pain - to our last show, I'll let you tune into this one for free."
      else:
        hannah.c "Assuming the answer is no, it'll only cost you 10 to watch me hurt her again."
      $ title = "What do you do?"
      menu:
        "Watch the show" if bethany.torture_count == 4:
          call hannah_school_torture_session_watch_bethany_2_show from _call_hannah_school_torture_session_watch_bethany_2_show
        "Tune in to the show (costs 10)" if bethany.torture_count != 4:
          if player.money - player.min_money < 10:
            "You don't have enough money.  You'll have to pass."
          else:
            change player money by -10
            call hannah_school_torture_session_watch_bethany_2_show from _call_hannah_school_torture_session_watch_bethany_2_show_1
        "Ignore":
          pass
    # Diamond's Torture Session
    elif master_m.lend_diamond_to_school == 2 and (bethany.torture_count == 0 or bethany.torture_count > 2):
      $ hannah.temporary_count = 1
      $ master_m.lend_diamond_to_school = 3
      wt_image phone_1
      "Your phone is ringing."
      wt_image principal_face_4
      "It's Principal Hannah."
      hannah.c "Just a friendly reminder that our show for this week is about to start.  Since you helped set up this week's show, you're allowed to watch it for free."
      wt_image principal_face_3
      "The show opens with a shot of Hannah."
      hannah.c "Welcome.  Our session today differs from our normal format."
      wt_image ms1_school_12
      hannah.c "Today's victim is apparently a frail little thing, as her Master considers her unsuited to the hard use we prefer to put our volunteers through.  Since her Master has been kind enough to donate her services for free to assist in our fund raising efforts, however, it would have been poor manners of me to refuse his kind offer."
      wt_image ms1_school_13
      hannah.c "During discussions with her Master, I discovered that this dainty princess prefers men, and has been giving her Master a hard time about providing sexual service to women.  Is that true, princess?  Does your Master have to punish you regularly to get you to serve his female friends the way you serve him?"
      "Diamond stares at the camera for a moment, then sheepishly nods."
      wt_image ms1_school_12
      hannah.c "You know what your Master and I agreed, don't you, princess?  I don't torture you on condition that you service me sexually, but if you hesitate or fail to please me in any way, I'm free to strap you down and put you through the same treatment Bethany got.  You've seen a replay of that, haven't you?"
      wt_image ms1_school_13
      "Diamond nods again, a touch of fear washing across her face."
      wt_image principal_face_7
      hannah.c "So that's the nature of today's show.  I'm not into girls, myself, so I'm really hoping that this princess gives me a reason to bring out my toys.  If she doesn't, hopefully the sight of her servicing me will be of sufficient interest that you won't regret sending along your donations in return for access to today's show."
      $ diamond.lesbian_training += 1
      $ title = "Keep watching the show?"
      menu:
        "Keep watching":
          wt_image ms1_school_1
          "The camera pans back to where a now naked Hannah is sitting, waiting."
          wt_image ms1_school_14
          hannah.c "Remove your top and get down on your hands and knees, princess."
          wt_image ms1_school_15
          hannah.c "I'm over here, princess.  Don't keep me waiting."
          wt_image ms1_school_16
          "The camera follows Diamond as she makes the long crawl to where Principal Hannah is waiting for her with open legs."
          wt_image ms1_school_2
          hannah.c "I understand from your Master that this is how you spent most of your school years, before you met him.  On your knees.  Show our audience the only skill you practised when you were a schoolgirl.  You can use my shoe to demonstrate."
          wt_image ms1_school_3
          hannah.c "Your Master wouldn't use these terms, but I know your type.  You were a free-for-use blowjob princess in school.  Not for the nice boys, of course.  But any jerk willing to slap your face and drag you to your knees was guaranteed a good time, wasn't he?"
          wt_image ms1_school_4
          "The video feed switches to the camera Hannah is holding."
          hannah.c "What I don't understand is why now, after you've been lucky enough to find a smart, sexy man to take control of you and steer you away from your worst tendencies, are you risking that relationship with a stupid hang up like servicing women?"
          wt_image ms1_school_17
          hannah.c "Licking cunt is just as easy as sucking cock, or sucking on my shoe.  Go on.  Practise licking my shoe."
          wt_image ms1_school_5
          "Tentatively, Diamond starts nuzzling and kissing the tip of the school principal's boot."
          hannah.c "Oh how cute!  What are you, a silly schoolgirl trying to tease the clit out of your roommate's pussy for the first time?  I'm not some mincing schoolgirl.  I'm a woman with a woman's big, hairy smelly cunt and if you're going to lick me you're going to work your tongue over and into every inch of it."
          wt_image ms1_school_6
          "Diamond starts licking Hannah's boot with long broad strokes of her tongue."
          hannah.c "See how easy that is?  Why do you make such a big deal of it?  Do you just naturally rebel when confronted with a confident woman, even though you swoon for confident men?  Or is some self-destructive part of you trying to sabotage your relationship because deep down you feel like you don't deserve to be happy?"
          wt_image ms1_school_7
          "That hits a little too close for Diamond.  She tries to pull away, but Hannah grabs her by the hair."
          hannah.c "Change your mind about servicing me?  That's fine by me.  My batteries are all charged and I have my toys out waiting for you."
          diamond.c "No!  No, I'll service you.  I'm sorry."
          wt_image ms1_school_6
          "Diamond goes back to licking Hannah's shoe."
          hannah.c "Why?  Your Master balked at me torturing you, but I don't believe you're really that fragile a princess.  Are you truly that scared of the pain I'll inflict on you?"
          diamond.c "No.  I don't like pain, but I can take it."
          wt_image ms1_school_18
          hannah.c "Then why?  You don't like the taste of cunt.  I don't blame you.  I don't particularly care for women between my knees.  Let's do something else.  Something that's easier for you.  I'll tie you up and hurt you and our audience will all be very happy to watch you suffer."
          diamond.c "My Master won't be happy.  I don't want to disappoint him again.  And I really don't want to sabotage our relationship.  I just get ... I'm not sure what.  I want to service you and make him happy.  I love that he puts me in my place, and I want to show him that."
          wt_image ms1_school_6
          hannah.c "As touching as that is, I'm not sure you can.  I'm not gay.  I don't like girls between my legs, and you're not all that skilled at pleasuring girls anyway."
          wt_image ms1_school_8
          diamond.c "Please?  Let me try.  I can make you wet.  See?"
          hannah.c "Nobody in our audience is donating their good money to see you put your fingers in me, princess.  If you're not going to suffer for them, they at least want to see you humiliate yourself."
          wt_image ms1_school_19
          hannah.c "Does my hairy, smelly cunt taste good, princess?"
          "Diamond shakes her head 'no'."
          wt_image ms1_school_11
          hannah.c "Are you sure?  Work your tongue deeper into me.  Maybe it's an acquired taste?"
          wt_image ms1_school_20
          hannah.c "Mmmm ... that's starting to feel good, princess.  Maybe you do have potential as a carpet muncher.  Are you sure you're not enjoying this?"
          "Diamond shakes her head again, but continues to work her tongue back and forth, across and into Hannah's pussy."
          wt_image ms1_school_21
          hannah.c "Maybe you're not focussed on the right aspect of this situation.  I'm going to tell your Master you need to spend more time eating out straight women, princess."
          "Even with her mouth buried between Hannah's legs, the camera picks up the sound of Diamond groaning in frustration."
          wt_image ms1_school_10
          hannah.c "He's been sending you to service lesbians, but a lesbian will take one look at your pretty face and want to cum all over it.  You'd hardly have to work at all, and unlike me, a lesbian isn't going to be thinking how silly you look flondering around down there."
          wt_image ms1_school_22
          hannah.c "What I'm enjoying most about this is how humiliating it is for you, a straight girl being made to eat out another straight girl.  What's going to be even more humiliating is when I send you back to your Master to tell him you weren't able to make me cum on your face."
          wt_image ms1_school_19
          diamond.c "No, please!  Please, I can make you cum."
          hannah.c "I doubt it.  You just look like a stupid slut down there, trying to make me cum when I'm not remotely interested in you."
          wt_image ms1_school_11
          diamond.c "Please, Mistress.  Please cum on my stupid slut face.  Maybe if you close your eyes and pretend I'm a boy it'll feel better?"
          wt_image ms1_school_22
          hannah.c "I'm not going to close my eyes, you worthless whore.  The only fun thing about this situation is seeing how far you'll humiliate yourself."
          wt_image ms1_school_19
          diamond.c "Yes, Mistress.  I'm a worthless whore.  Thank you for letting this worthless whore lick your cunt."
          wt_image ms1_school_11
          diamond.c "Please cum on this worthless whore's stupid slut face, Mistress.  Please send me back to my Master with your smelly cunt juices smeared all over my stupid face."
          wt_image ms1_school_20
          hannah.c "Oh shit!  That's it, you stupid cunt.  Suck my clit!!"
          wt_image ms1_school_9
          hannah.c "Ooohhhh FUUUCKKKK!!"
          "Principal Hannah holds the sub girl's face firmly against her sex as she bucks to an intense, loud orgasm."
          wt_image ms1_school_11
          hannah.c "How long does a worthless whore like you lick cunt, princess?"
          diamond.c "Until you're satisfied with me and ready to send me back to my Master, Mistress."
          wt_image ms1_school_21
          hannah.c "Then don't bother saying 'good bye' to our audience.  Just keep licking until you swallow everything my cunt has to give you."
          wt_image ms1_school_10
          hannah.c "I hope you all enjoyed our show.  Even if we didn't get to make this stupid slut suffer, I think we still got some fun out of her.  She's going to stay here between my legs until the donations stop coming in, so don't be afraid to send in a second or third contribution."
          change player energy by -energy_very_short notify
        "Pass":
          pass
      if bethany.torture_count < 5:
        $ bethany.torture_week = week + 3
    # Your Torture Session
    elif hannah.temporary_count == 0 and (bethany.torture_count == 1 or bethany.torture_count == 2):
      wt_image phone_1
      "Your phone is ringing."
      wt_image principal_face_8
      "It's Hannah, the School Principal."
      hannah.c "It's time.  I'm all ready for you.  The lights and camera are set up in the school basement, and an audience is lined up to watch you suffer.  I hope you're not going to wimp out on me."
      $ title = "What do you do?"
      menu:
        "Go to the school":
          call forced_movement(school) from _call_forced_movement_981
          summon hannah to school
          wt_image principal_torture_you_2_1
          hannah.c "Undress"
          wt_image principal_torture_you_2_2
          "You're not sure what type of welcome you were expecting from Hannah, but not this.  There's no small talk, no 'thank you' for helping the school.  Just a length of rope wrapped quickly into a chest harness that binds your arms behind your back."
          wt_image principal_torture_you_2_3
          "Having the attention of a beautiful woman is usually a turn on.  This is just - scary.  Once you're trussed up, Hannah sits down and checks her watch.  After a few minutes, she turns on the camera."
          hannah.c "Hello audience.  Thanks again for tuning in to help with our school fund raising.  This is going to be a special treat for me.  Not that long ago the man tied up beside me took advantage of me and my love for our school, and coerced me into accepting his punishment under threat of financially ruining us."
          wt_image principal_torture_you_2_4
          hannah.c "He's a sadistic, sick man, and I had nothing but contempt for him.  But then he showed me a different side of him."
          wt_image principal_torture_you_2_5
          hannah.c "Today he's here to make amends for his wrong, and help us secure the school's financial position.  Out of respect for his having the courage to make things right, I'm going to keep his name and profession confidential.  I still remember the torment he put me through, however, and today I'm going to have my revenge while you watch."
          wt_image principal_torture_you_2_2
          hannah.c "You'll notice how smooth and unmarked his skin looks. That's about to change."
          wt_image principal_torture_you_2_6
          hannah.c "Since our volunteer has seen the light, I'm going to welcome him back into the community of good and decent people with a special cleansing ceremony."
          wt_image principal_torture_you_2_7
          hannah.c "Of course, passing from darkness into the light doesn't come without some suffering to purify the soul from past sins."
          "The first few drips of the candle don't really hurt ..."
          wt_image principal_torture_you_2_8
          "... but as she moves the candle closer and closer, the wax becomes hotter and hotter as it strikes your skin."
          player.c "Ow!"
          wt_image principal_torture_you_2_9
          if hannah.has_tag('took_out_cock_punishment_call'):
            hannah.c "What happened to your erection?  You were so proud to show it to me after you tortured me.  Aren't you enjoying being on the other side?"
          else:
            hannah.c "You don't seem to be as turned on as you looked when you were torturing me."
          wt_image principal_torture_you_2_10
          hannah.c "I think I can help with that."
          wt_image principal_torture_you_2_11
          hannah.c "There.  Now I have a nice target so your dick can participate in the cleansing ceremony, too."
          wt_image principal_torture_you_2_12
          "You try your best to stay tough, but the intensity of the heat as the wax drips from ever shorter distances eventually overwhelms you."
          player.c "nnnnnnnnn ... ooowwwwww!!"
          wt_image principal_torture_you_2_13
          hannah.c "Too intense?  This should distract you from the pain in your dick."
          "She doesn't drip this time, she pours ... two large pools of melted wax splash onto your chest simultaneously."
          wt_image principal_torture_you_2_14
          player.c "OOOWWWWWWW!!!!"
          wt_image principal_torture_you_2_15
          hannah.c "Feeling cleansed of your past transgressions?"
          "Through gritted teeth, you try your best to answer her, but it's hard to think when your chest and shoulders feel like they're on fire."
          player.c "Mmmm hhhmmmmm"
          wt_image principal_torture_you_2_16
          hannah.c "I'm not sure your dick agrees.  It seems to be shirking me, which is a problem, as I'm pretty confident your dick is the reason you acted like a ... well, 'dick' to me and no doubt others."
          wt_image principal_torture_you_2_17
          hannah.c "Bad, dick!  Bad!!"
          "She addresses your dick, but it's your balls that receive the punishment ... *smack* ... *smack* ... *smack*"
          player.c "OWWW!  OOWWWW!!  OOOWWWW!!!"
          wt_image principal_torture_you_2_18
          hannah.c "It's okay, dick.  You, too, are forgiven as part of the cleansing ceremony."
          player.c "OOOWWWWWWW!!!!"
          wt_image principal_torture_you_2_19
          hannah.c "Only one step left in the ceremony."
          wt_image principal_torture_you_2_20
          "*whooosshhhh* ... against your wax-burned skin, the water feels ice cold, though it's likely only room-temperature"
          player.c "nnnnnnnnnn"
          wt_image principal_torture_you_2_21
          hannah.c "Now that you've been cleansed, I'm ready to start torturing you."
          player.c "Start?!?"
          wt_image principal_torture_you_2_22
          "You're too sapped by the 'ceremony' to offer any resistance as Hannah re-ties you into a bending over position.  Then she leaves you and addresses your viewing audience."
          wt_image principal_torture_you_2_23
          hannah.c "I'm sure you'd all be disappointed if we didn't subject today's volunteer to the same electrical experiments we put poor Bethany through."
          wt_image principal_torture_you_2_24
          hannah.c "Fear not.  I wouldn't want to miss this opportunity to answer that age old question - who's really tougher, women or men?"
          wt_image principal_torture_you_2_25
          hannah.c "A few wires around his penis and one inserted in the opening should give today's volunteer ample opportunity to demonstrate that he can take pain as well as, or better than, Bethany."
          wt_image principal_torture_you_2_26
          "The first jolt goes through you with no warning ... *zzzztttt*"
          player.c "ARGHH!!!"
          wt_image principal_torture_you_2_27
          hannah.c "Oh my, that's a loud scream for the first zap."
          "*zzzztttt*"
          wt_image principal_torture_you_2_29
          player.c "AARRGHHH!!!"
          wt_image principal_torture_you_2_28
          hannah.c "Come on, I'm only up to level 7.  It can't hurt that much?"
          "*zzzztttt*"
          wt_image principal_torture_you_2_30
          player.c "EEEERRRRRRR"
          hannah.c "Really?  Going non-verbal at level 8?  Maybe its true what they say about men having a lower pain threshold than women."
          wt_image principal_torture_you_2_31
          hannah.c "As I recall, it was the internal shocks that really had poor Bethany jumping."
          wt_image principal_torture_you_2_32
          hannah.c "Let's see if you do better with internal voltage than you did with external voltage."
          wt_image principal_torture_you_2_34
          "She doesn't lubricate the probe, she just shoves it up your ass roughly.  You guess that the pain of entry is nothing compared to what the pain will be like when she switches it on."
          wt_image principal_torture_you_2_35
          "Sadly, you're right ...  *zzzztttt*"
          player.c "AAARRRGGHHHH!!!!"
          wt_image principal_torture_you_2_36
          hannah.c "Goodness, that's loud.  And only level 5.  I'm ready to call it, audience.  The electricity hurts more when it's delivered internally, for both boys and girls.  All that's left is to find out if boys can take more than girls, or not?"
          "*zzzztttt*"
          wt_image principal_torture_you_2_29
          "Every muscle in your body feels like its clenching up involuntarily.  Your throat is so tight that while it feels like you're screaming inside, only the faintest squeak escapes ... *zzzztttt*"
          wt_image principal_torture_you_2_37
          "Your entire existence is reduced to pain and sharp flashes of light behind your tightly squeezed eyes ... *zzzztttt*"
          wt_image principal_torture_you_2_38
          "You don't exactly lose consciousness, but you do slip into a more detached form of awareness.  You couldn't say how long or how often she uses the electricity on you ... *zzzztttt*"
          wt_image principal_torture_you_2_33
          "... nor could you say when she starts thrusting her hips, reaming your ass as she shocks you ... *zzzztttt*"
          wt_image principal_torture_you_2_39
          "It's only the feel of electricity coursing through your body, radiating outwards from your ass and cock, along with a vague sense of being violated ... *zzzztttt*"
          wt_image principal_torture_you_2_40
          "... and an even vaguer sense of someone besides you groaning behind you as you suffer ... *zzzztttt*"
          wt_image principal_torture_you_2_41
          "You never lose consciousness, although it would have been a mercy if you had.  Somewhere you hear Hannah thank the audience again for their financial contributions and switch the camera off.  Then you hear her again, closer, and realize she's talking to you."
          hannah.c "I wonder if this is how you felt when you had me helpless and suffering under your control?  You're sick, perverted, and damn if you haven't brought out a sickness in me, too."
          wt_image principal_torture_you_2_42
          hannah.c "I'll let you go now."
          wt_image principal_torture_you_2_43
          "*SLAAPPPP*"
          player.c "OWWW!"
          wt_image principal_torture_you_2_44
          hannah.c "I just needed to see you wince in pain one more time before I do."
          "She unties you, none too gently, and lets you dress to go home."
          if bethany.torture_count == 1:
            $ bethany.torture_count = 4
            $ bethany.torture_week = week + 3
          else:
            $ title = "Ask Hannah to Domme you again?"
            menu:
              "Yes, you'd like to serve her":
                wt_image principal_torture_you_2_45
                call hannah_school_torture_session_serve_her from _call_hannah_school_torture_session_serve_her
              "Suggest she become a professional Domme":
                wt_image principal_torture_you_2_45
                call hannah_school_torture_session_suggest_become_domme from _call_hannah_school_torture_session_suggest_become_domme
              "No thanks":
                pass
          change player energy by -energy_short notify
          call character_location_return(hannah) from _call_character_location_return_691
          call forced_movement(living_room) from _call_forced_movement_982
        "Wimp out":
          "Who knows what that crazy woman might do to you, or who might be watching her broadcast?"
          wt_image current_location.image
          "You decide to spend the rest of the weekend not being tortured by the local school principal."
    # Bethany's first torture session
    elif hannah.temporary_count == 0 and bethany.torture_count == 0:
      wt_image phone_1
      "Your phone is ringing."
      "It's Hannah the School Principal."
      hannah.c "I thought you might be interested in dropping by the school this evening.  Bethany is going to be helping us recover the money she lost."
      player.c "What will she be doing?"
      hannah.c "Something inspired by you."
      $ title = "Go to the school?"
      menu:
        "Yes, let's see what's going on":
          call forced_movement(school) from _call_forced_movement_983
          wt_image school.image
          "It's a Saturday evening and the school looks empty, but the side door is unlocked.  Inside, you see nobody.  As you wander the corridors, a voice calls to you from a stairwell."
          summon hannah to school
          hannah.c "We're down here. In the basement."
          wt_image banker_school_2_1
          "It's Hannah, but she's dressed far differently than she normally does."
          hannah.c "Let me show you what we've set up."
          summon bethany to school
          wt_image banker_school_2_2
          "The school basement has been turned into a make shift video studio. In the corner is a camera and lights.  In the center of the room, Bethany is tied to a metal frame."
          hannah.c "When you told me that Bethany was ready to make amends, I started to think about what she could do to restore the financial loss she inflected on your school."
          wt_image banker_school_2_20
          hannah.c "Then I started to think about my experience with you, and in particular your comment about how there are lots more sickos like you out there, I just hadn't had the misfortune to fall under the control of them."
          wt_image banker_school_2_18
          hannah.c "So I decided to broadcast a little show for all those sickos, and charge them 10 a piece to watch me torture Bethany, the way you tortured me."
          wt_image banker_school_2_19
          hannah.c "When I posted online that the victim will be our former banker, the subscriptions poured in.  I think even you'd be surprised by how many of her former clients want to watch her suffer."
          $ bethany.school_torture_ask = False
          wt_image banker_school_2_2
          $ title = "What do you do?"
          menu menu_hannah_school_torture_bethany_1:
            "Ask Bethany if she's okay" if not bethany.school_torture_ask:
              player.c "Bethany, are you okay?"
              wt_image banker_school_2_3
              "She raises her head. Her voice is shaky, but clear."
              bethany.c "I'm okay. Just a bit scared."
              player.c "Have you consented to this?"
              "She nods."
              bethany.c "Principal Hannah has explained how this is the best way for me to make amends to the school. And she's going to share a portion of the revenues with me, once the school's losses are made whole, so I can start to rebuild my personal finances.  It's not the career I expected to have, but it's honest work."
              wt_image banker_school_2_2
              $ bethany.school_torture_ask = True
              jump menu_hannah_school_torture_bethany_1
            "Ask when the show starts":
              player.c "When does the show start?"
              wt_image banker_school_2_4
              hannah.c "In just a minute.  I just need to finish hooking up the last of the external wires."
              wt_image banker_school_2_5
              player.c "And those other items?"
              hannah.c "I'll insert them once we're broadcasting."
              wt_image banker_school_2_6
              hannah.c "Okay that should just about do it."
              wt_image banker_school_2_18
              "Hannah shoos you over to a side wall, out of the way, and turns on the video.  You think you hear a forlorn moan escape Bethany just before the video starts running."
              hannah.c "Hello everyone.  Thank you for contributing to our fund raising efforts by subscribing to today's show."
              wt_image banker_school_2_19
              hannah.c "I'm happy to have Bethany with me today.  Bethany is formerly of Global Trust Bank and a big reason why our school needed to resort to innovative fundraising methods like this."
              wt_image banker_school_2_2
              hannah.c "I know a lot of you are looking forward to seeing Bethany again.  Bethany, could you please say hello to our audience?"
              wt_image banker_school_2_3
              "In a wavering voice, Bethany quietly replies."
              bethany.c "Hello"
              wt_image banker_school_2_6
              hannah.c "That wasn't very convincing, Bethany.  Say hello like you mean it."
              wt_image banker_school_2_7
              "*zzzzttttt*"
              bethany.c "aaarrgghhh  ...  Hello!  Hello!"
              hannah.c "That's better.  As you can hear, Bethany is wired for sound today.  I'm sure you're all looking forward to hearing more from her as our show proceeds."
              wt_image banker_school_2_21
              hannah.c "To get us started, I've added electrodes to both sides of Bethany's torso.  These are a lot like the TENS machines you might use at physiotherapy, except, of course, they're a lot more painful and a lot less therapeutic."
              wt_image banker_school_2_22
              hannah.c "They do hurt, don't they Bethany?"
              bethany.c "Yes"
              wt_image banker_school_2_23
              hannah.c "I couldn't hear that."
              wt_image banker_school_2_8
              "*zzzztttttt* *zzzzztttttt"
              bethany.c "Yes!  Yes, they hurt!!  Super hurt!!!"
              wt_image banker_school_2_22
              hannah.c "I'm sure you mean that Bethany, but I wonder if you'll still feel that way by the time we're finished?"
              wt_image banker_school_2_23
              hannah.c "Electrodes on your skin do stimulate the nervous system, but I know our audience is looking forward to hearing from you after some more intense and more personal stimulation."
              wt_image banker_school_2_24
              hannah.c "I understand from our chat about your past work experience that some of your clients got to experience your ass when you were their banker."
              wt_image banker_school_2_25
              hannah.c "I guess that explains why you're so accommodating back here."
              wt_image banker_school_2_26
              hannah.c "I'm sure all of your past clients, as well as the rest of our audience, would like to share that experience of fucking you in the ass.  Since that isn't possible, I'm going to try and do my best to recreate the experience with this electrified butt plug."
              wt_image banker_school_2_27
              "Bethany groans as Hannah slowly but steadily forces the dildo up her rear."
              bethany.c "nnnnnnnnn"
              wt_image banker_school_2_28
              hannah.c "I purposefully chose the widest didlo I had, since you have work experience in the area.  Do you think this one is big enough to fill you up?"
              bethany.c "nnnnnnnn ... yes!!"
              wt_image banker_school_2_9
              hannah.c "Good, I wouldn't want to assign you a project that was below your experience level.  It's all the way inside you, now.  Shall we see what happens when we run electricity through it?"
              wt_image banker_school_2_10
              "Bethany's only reply is a series of small whimpers that aren't really a yes or a no."
              bethany.c "nn nn nn nn"
              wt_image banker_school_2_11
              "*zzzzzttttt*"
              bethany.c "AAARRGGHHH!!"
              wt_image banker_school_2_30
              hannah.c "Does that hurt, Bethany?  Taking electric shocks through this giant dildo shoved right up your ass?"
              bethany.c "YESSS!!!"
              wt_image banker_school_2_10
              hannah.c "How much?"
              wt_image banker_school_2_8
              "*zzzzttttt*"
              bethany.c "A FUCKING LOT!!"
              wt_image banker_school_2_29
              hannah.c "Don't swear, Bethany.  This may be the basement, but it's still a school.  Just tell our audience how much this hurts."
              wt_image banker_school_2_7
              "*zzzzzttttt*"
              bethany.c "AAARRGGHHH!! It hurts a crazy insane amount!!!"
              hannah.c "Would you say it hurts a wicked smart amount?"
              wt_image banker_school_2_11
              "*zzzzzttttt*"
              bethany.c "YEESSS!!!! IT HURTS A WICKED SMART AMOUNT!!!"
              wt_image banker_school_2_12
              hannah.c "Take a little rest, Bethany. I'm sure your ass is really hurting by now."
              "Some deep moaning sobs are the only reply."
              bethany.c "nnnnn  nnnnn  nnnnn"
              wt_image banker_school_2_31
              hannah.c "It's time for some other body parts to share the suffering, don't you think?"
              wt_image banker_school_2_32
              "You're not sure if Hannah is addressing the audience, or Bethany, or both.  Regardless, the former banker groans as Hannah slides a second dildo into her pussy."
              wt_image banker_school_2_33
              bethany.c "nnnnnn"
              wt_image banker_school_2_34
              hannah.c "How do you think that's going to feel, once electricity is running through both the plug and the dildo?"
              bethany.c "I don't know!"
              wt_image banker_school_2_13
              hannah.c "But you suspect that it's going to hurt, don't you?"
              bethany.c "Yes!!"
              wt_image banker_school_2_14
              hannah.c "Let's see if you're right."
              wt_image banker_school_2_11
              "*zzzttttt*"
              bethany.c "AAARRRGGHHH!!!!"
              wt_image banker_school_2_35
              bethany.c "How much is it hurting now, Bethany?  Now that you're taking electric shocks straight up your cunt and ass both?"
              wt_image banker_school_2_15
              "*zzzzttttt*"
              bethany.c "AAARRRGGHHH!!! WICKED SMART! WICKED SMART! WICKED SMART!"
              wt_image banker_school_2_16
              hannah.c "I'm not sure that's really a coherent answer, Bethany, but I'll accept it under the circumstances, as I can see that the electricity has your insides jumping around like you've got a gopher running through your intestines."
              wt_image banker_school_2_36
              hannah.c "Have a little rest while I fill our audience in on a secret.  Those last shocks were delivered with the controller set to 8, but the settings can be adjusted up to 10."
              wt_image banker_school_2_37
              hannah.c "Is there anybody at home who'd like to see me bump the settings up to 10?  Oh, I can see the messages pouring in on the monitor from way over here."
              wt_image banker_school_2_22
              hannah.c "Isn't that good news, Bethany?  The audience is fully engaged in your experience.  You don't want to cheat them out of their fun, do you?"
              "Amazingly, Bethany manages a small shake of her head."
              wt_image banker_school_2_4
              hannah.c "Do I need to go read the messages, Bethany, or is it safe to assume that at least one person wants to see what happens when the setting is at 10?"
              "That might have been a small nod.  Whether it was or not, Hannah has adjusted the controller."
              wt_image banker_school_2_38
              hannah.c "Let's not keep the audience in suspense, Bethany.  Let's show them what setting 10 does to you."
              wt_image banker_school_2_8
              "*zzzzzttttttt*"
              "Bethany's face screws up. It looks like she's trying to scream, but little sound escapes the tightness of her throat."
              bethany.c "eeerrrkkkk"
              wt_image banker_school_2_17
              hannah.c "What's wrong, Bethany? is that hurting too much even to scream?"
              "*zzzzzttttttt*"
              "Bethany nods her head up and down in near silence."
              bethany.c "rrrrkkk"
              hannah.c "You're not trying to cheat our audience, are you Bethany?  Do you have anything more to give?"
              wt_image banker_school_2_8
              "*zzzzzttttttt*"
              "She shakes her head back and forth as quickly as her tightening neck muscles allow"
              bethany.c "rrrrr"
              hannah.c "Just one more zap then, okay?"
              wt_image banker_school_2_17
              "*zzzzzttttttt*"
              "The former banker shakes and trembles from head to foot, her face contorted in agony, her fingers and toes curled tightly."
              wt_image banker_school_2_22
              hannah.c "That's the end of our show.  Bethany's given us as much as she has to give for today."
              wt_image banker_school_2_18
              hannah.c "If you'd like to be informed of future shows, please send your contact information and a small donation we'll add you to our notice list."
              wt_image banker_school_2_39
              "Hannah switches off the video, then turns to look at you."
              hannah.c "I hope I was sadistic enough to satisfy the sickos like you in the audience. I'd like this one to be well received enough to get a bigger audience for our next show."
              wt_image banker_school_2_19
              hannah.c "Speaking of which, I let you watch this show as a freebie, but you'll need to make a contribution to the school for our next show."
              player.c "You want me to pay to watch the next show?"
              wt_image banker_school_2_20
              hannah.c "I want you to be the next show.  I want to do to you what you did to me at your house.  I want you to let me hurt you for the amusement of our audience."
              $ title = "What do you do?"
              menu menu_hannah_domme_you_choice:
                "Okay, I'll be your next victim":
                  player.c "Okay, I'll be your next victim."
                  wt_image banker_school_2_19
                  hannah.c "Really? I didn't think you'd have the balls to take what you dish out."
                  player.c "I'm sure I can take anything you can dish out."
                  wt_image banker_school_2_18
                  hannah.c "Be back here in 4 weeks and we'll find out.  I'll call you when it's time for you to come over.  You have no idea how much I'm looking forward to it."
                  $ bethany.torture_count = 1
                "How about I Dom you and Bethany instead":
                  player.c "You'd get a much bigger audience if you let me Dom you and Bethany."
                  wt_image banker_school_2_20
                  hannah.c "Ha!  I'm not letting you touch me again.  You had your fun once.  The next time one of us is suffering its going to be you."
                  jump menu_hannah_domme_you_choice
                "Forget it":
                  player.c "Forget it.  Maybe I'll pay to watch your next show if it looks interesting, but I'm not letting you torture me."
                  wt_image banker_school_2_39
                  hannah.c "Too big a wimp are you?"
                  "You leave her insult alone and head home."
                  $ bethany.torture_count = 3
              $ master_m.lend_diamond_to_school = 1
              $ bethany.torture_week = week + 3
              change player energy by -energy_short notify
            "Leave":
              wt_image banker_school_2_1
              player.c "Very entrepreneurial of you, but I'm leaving."
              wt_image banker_school_2_20
              hannah.c "Really?  You took pleasure in torturing me, but you don't want to watch Bethany suffer?"
              "You shrug and leave.  You have your reasons, but don't have to share them with her."
              change player energy by -energy_very_short
              $ bethany.torture_week = 0
          call character_location_return(bethany) from _call_character_location_return_692
          call character_location_return(hannah) from _call_character_location_return_693
          call forced_movement(living_room) from _call_forced_movement_984
          wt_image current_location.image
        "No, not interested":
          pass
    $ hannah.temporary_count = 0
  # Alexis Torture Session
  else:
    wt_image phone_1
    "Your phone is ringing."
    wt_image pa_school_torture_19
    "It's Hannah, the School Principal."
    hannah.c "I understand you have a volunteer for our fundraiser.  It's time.  Bring her to the school."
    call forced_movement(school) from _call_forced_movement_985
    summon alexis to school
    wt_image pa_school_torture_1
    if alexis.revealed_past > 0:
      "Alexis seems a bit despondent when you pick her up."
      alexis.c "I can't believe you volunteered me for torture.  You know my past.  Now you're sending me to another woman to abuse me?"
      player.c "This is different.  You're in control.  You could walk away, but you've chosen to do your duty as a good corporate employee."
    else:
      "Alexis seems a bit despondent when you pick her up."
      alexis.c "I can't believe you volunteered me for torture."
    player.c "You should be feeling good about this.  You get to donate your time for a good cause."
    if bethany.torture_count == 4 or bethany.torture_count == 6:
      player.c "Besides, it's not that bad.  I've done it myself."
      wt_image pa_school_torture_2
      alexis.c "You have?"
      player.c "I wouldn't lie to you."
      wt_image pa_school_torture_20
      "She looks at you with newfound respect."
      alexis.c "Is it really not that bad?"
      player.c "That part I was lying about.  It's horrible, but you'll get through it and eventually it will be over."
      change alexis resistance by -5
    elif bethany.torture_count == 1 or bethany.torture_count == 2:
      player.c "I've volunteered, too."
      wt_image pa_school_torture_2
      alexis.c "You have?"
      player.c "I have.  I'll be doing the next session after you."
      wt_image pa_school_torture_20
      "She looks at you with newfound respect."
      change alexis resistance by -5
    else:
      "She's not convinced.  You're clearly not her favorite person right now."
      change alexis desire by -5
    summon hannah to school
    wt_image pa_school_torture_18
    "Principal Hannah is taken aback when she sees who her latest 'volunteer' is."
    hannah.c "Alexis?  Are you the corporate volunteer for our fundraiser?"
    wt_image pa_school_torture_21
    alexis.c "Yes, Principal Hannah.  Are you going to be torturing me personally?"
    wt_image pa_school_torture_22
    hannah.c "Yes, I will be.  You wore your school jacket?  That's probably not a good idea.  Best take it off, before someone thinks I'm abusing a current student."
    wt_image pa_school_torture_23
    alexis.c "I guess this can't be worse than that biology final exam you gave us, huh?"
    wt_image pa_school_torture_24
    hannah.c "It can't be worse than that dress, that's for sure.  You used to wear that when you were a student, too.  I'd hoped your fashion sense might have improved by now.  I think it may be best if we start you off naked."
    wt_image pa_school_torture_25
    hannah.c "Actually, you can keep the leggings on.  They'll add some color to the proceedings until I can bring some red to your skin."
    wt_image pa_school_torture_3
    hannah.c "Follow me, Alexis.  Let's get you ready for your volunteer duty."
    wt_image pa_school_torture_26
    "You look on with interest as Hannah gets Alexis ready.  Even Alexis seems clinically interested in what Principal Hannah is up to.  Eventually, Hannah is satisfied with her preparations and starts the show."
    wt_image pa_school_torture_22
    "It takes a while, but eventually Hannah has Alexis trussed up the way she wants her, and starts the show.  You get a first hand view from the corner of the school's basement as Hannah starts broadcasting."
    hannah.c "Hello everyone.  Thanks for joining us again for another fund raiser.  Today's show is made possible by the generosity of the good folks at SelectaCorp, who have graciously offered the services of their employee, Alexis, for your viewing amusement."
    wt_image pa_school_torture_4
    hannah.c "Say hello to our audience, Alexis."
    "Alexis trembles silently as Hannah runs the cattle prod along her bare skin, unable to answer."
    wt_image pa_school_torture_26
    hannah.c "Alexis didn't used to shy about speaking up.  She was one of the brightest students we've ever had come through our school.  She graduated top of her class and went on to university on a full scholarship."
    wt_image pa_school_torture_27
    hannah.c "I admit I'm quite surprised to see her in this position.  I can only assume she's very civic minded and wanted to give back to her school for the quality education she received.  Is that why you're here, Alexis?"
    "Again, Alexis is shaking too much to bring herself to respond."
    wt_image pa_school_torture_5
    hannah.c "Alexis, are you scared?  Is that why you're not answering me?  Are you terrified by the prospect of how much this is going to hurt?"
    "The frightened young woman manages a small nod."
    wt_image pa_school_torture_28
    hannah.c "See?  I told you she was smart.  Everything we do today is going to hurt, Alexis. Take this cattle prod for example."
    wt_image pa_school_torture_6
    "*zzzzzzttt*"
    alexis.c "Ooooo!"
    hannah.c "Did that hurt, Alexis?"
    wt_image pa_school_torture_29
    alexis.c "Yes!!!"
    hannah.c "Oh good, you can talk!  I bet you can scream prettily for our audience, too.  Don't bother bending over to hide from the prod.  That's not going to help when I turn on the wires wrapped around your nipples."
    wt_image pa_school_torture_30
    "*zzzzzzzz*"
    alexis.c "nnnnnnn"
    hannah.c "See?  That wasn't really a scream, though.  Maybe if I bump the settings up?"
    wt_image pa_school_torture_31
    "*zzzzzzzz*"
    alexis.c "aaaaaaa"
    wt_image pa_school_torture_7
    hannah.c "Getting closer.  Sit up.  Small as your tits are, I'm sure the audience would enjoy seeing them bounce around when the electricity runs through them."
    wt_image pa_school_torture_32
    hannah.c "Just to make sure you give them a good show, let's bump the settings up to 80."
    wt_image pa_school_torture_33
    "*zzzzzzzz*"
    alexis.c "Oowwwww!!!"
    hannah.c "There!  That's a proper scream.  Did setting 80 hurt, Alexis?"
    wt_image pa_school_torture_29
    alexis.c "Yes!"
    hannah.c "Would you like me to disconnect the wires from your nipples?"
    alexis.c "Yes, please!!"
    hannah.c "But, Alexis, that was only an 80.  Were you ever satisified with only getting an 80 at school?"
    alexis.c "ooooo  ...  nooooo"
    wt_image pa_school_torture_7
    hannah.c "What did you always want to get on your projects at school, Alexis?"
    alexis.c "One ... one ...  oooooo  ...  one hundred!"
    hannah.c "That's right.  See, this is getting an 80 ..."
    wt_image pa_school_torture_33
    "*zzzzzzzzz*"
    alexis.c "Oowwwww!!!"
    hannah.c "Lots of girls get 80s, Alexis.  You were never satisfied with that.  You always wanted a 100.  Here's a 100, reserved for ambitious, hard-working girls like you, Alexis ..."
    wt_image pa_school_torture_34
    "*zzzzzzzzz*"
    alexis.c "OOOWWWWWWW!!!"
    wt_image pa_school_torture_35
    hannah.c "Now that you're earned a 100, Alexis, should we move on to the next test, or would you like to try for extra credit?"
    alexis.c "No!  No extra credit, thank you!!  Please, please let's move on???"
    wt_image pa_school_torture_36
    "Hannah disconnects the wires from Alexis' nipples and re-ties her into a standing position."
    wt_image pa_school_torture_8
    hannah.c "Is the feeling in your nipples returning to normal?"
    alexis.c "I ... I think so."
    wt_image pa_school_torture_37
    hannah.c "Good.  I'd hate to waste electricity on nipples that weren't able to feel it properly."
    wt_image pa_school_torture_38
    "*zzzaapppp*"
    alexis.c "nnnnnnnn!!"
    wt_image pa_school_torture_39
    "*zzzaapppp*"
    alexis.c "ooooooo!!"
    wt_image pa_school_torture_9
    hannah.c "You're quite good at holding back your screams.  You don't need to, you know.  Our audience would love to hear you really letting go."
    wt_image pa_school_torture_40
    hannah.c "Perhaps if I zap both nipples at once?"
    wt_image pa_school_torture_10
    "*zzzaapppp*"
    alexis.c "Ooowwwww!!!!"
    wt_image pa_school_torture_41
    hannah.c "That's better!  Your poor nipples look sore again.  Would you like me to give them a break from the zapper?"
    alexis.c "Y ... yes, please!"
    wt_image pa_school_torture_11
    hannah.c "Good.  Because I can make your whole breasts hurt as badly as your nipples hurt currently."
    wt_image pa_school_torture_12
    "*thwappp*"
    alexis.c "ooooooooo"
    wt_image pa_school_torture_13
    "*thwappp*"
    alexis.c "NNNNNNNNN"
    hannah.c "Don't hold back, Alexis.  Our audience donated good money to watch you suffer.  They want to hear you suffer, too."
    wt_image pa_school_torture_14
    "*thwappp*"
    alexis.c "Ooowwww!!!!!!"
    hannah.c "Better, but I know it hurts even more than you're letting on.  Drop the stoic act and let yourself go, Alexis.  Let the audience know what you're really feeling right now."
    wt_image pa_school_torture_15
    "The dam bursts, and Alexis devolves into a screaming, mindless beast, surrendering to the pain coursing through her chest ... *thwappp*"
    alexis.c "OOOOOWWWWWWW!!!!!!!!"
    wt_image pa_school_torture_42
    "Hannah switches on the electrical current, and begins alternating between electrical zaps and hits with the cane ... *zzzztttt*"
    alexis.c "OOOOOWWWWWWW!!!!!!!!"
    wt_image pa_school_torture_15
    "*thwappp*"
    alexis.c "OOOOOOOOWWWWWWWWWW!!!!!!!!"
    wt_image pa_school_torture_42
    "*zzzztttt*"
    alexis.c "OOOOOOOOWWWWWWWWWW!!!!!!!!"
    wt_image pa_school_torture_16
    "And then the screaming stops, and Alexis hangs limply in her bonds, unable to fully vocalize the pain that continues to rip through her ... *thwappp* ... *zzzztttt* ... *thwappp*"
    alexis.c "nnnnn ... rrrrrr .... uuuuuu"
    wt_image pa_school_torture_22
    hannah.c "That's the end of our show for today.  Poor Alexis doesn't seem to have any more screams to give us.  Thank you again to Selectacorp for making Alexis available for your entertainment.  I'm sure you'll agree she was worth an extra donation to the school that made her the woman she is today."
    wt_image pa_school_torture_17
    "You and Hannah get Alexis down from her bonds and give her some time to recover.  When she does, Hannah smiles at her."
    hannah.c "You did very well."
    alexis.c "Did I?"
    wt_image pa_school_torture_43
    hannah.c "You did.  Today's fund raiser was our most successful ever.  You've raised a lot of money for the school, Alexis."
    player.c "Doesn't it feel good, when you truly give of yourself?"
    alexis.c "I guess, yes.  I'm glad I was able to do some good for the school.  I wasn't sure I'd be able to get through it."
    wt_image pa_school_torture_24
    player.c "How does it feel, knowing that you did?"
    alexis.c "That feels good, too.  Like I really accomplished something."
    wt_image pa_school_torture_18
    hannah.c "You did.  And now we both know that I can be harder on you next time."
    wt_image pa_school_torture_20
    alexis.c "Next time??!"
    player.c "She's teasing, Alexis.  I think.  Let's get you home."
    wt_image pa_school_torture_23
    alexis.c "You know, as a kid, you always sort of suspect your teachers are sadists.  I wasn't expecting to find out one of mine really is."
    if bethany.torture_count < 5 or master_m.lend_diamond_to_school == 2:
      $ bethany.torture_week = week + 2
    $ alexis.principal_torture_status = 3
    change alexis sos by 5
    change alexis submission by 10
    change alexis resistance by -5
    change player energy by -energy_short notify
    call character_location_return(alexis) from _call_character_location_return_694
    call character_location_return(hannah) from _call_character_location_return_695
    call forced_movement(living_room) from _call_forced_movement_986
  return

# School Torture Session - Watch Show
label hannah_school_torture_session_watch_bethany_2_show:
  wt_image banker_school_2_1
  "You tune in and settle back to watch the show.  You don't have to wait too long for it to get started."
  hannah.c "Hello everyone.  Thanks for joining us for our latest fund raiser."
  wt_image banker_school_2_18
  hannah.c "I'm happy to announce that as of this session, thanks to Bethany's fine work and your generosity, we'll have fully repaired the school's financial situation.  That means a quality education for all of our children."
  wt_image banker_school_3_12
  hannah.c "Bethany, would you like to say hello to our audience and thank them for their generosity?"
  "A frightened looking Bethany nervously addresses the camera."
  bethany.c "Thank you for tuning in to help me fix the financial harm I did to the school."
  wt_image banker_school_3_13
  hannah.c "Bethany, do you think a quality education is important?"
  bethany.c "I think so, yes."
  wt_image banker_school_3_1
  hannah.c "Should it help our boys and girls avoid ending up in your situation right now?"
  wt_image banker_school_3_14
  bethany.c "I hope so."
  wt_image banker_school_3_15
  hannah.c "I hope so, too, but don't be too hard on yourself.  You've shown your merit by doing the right thing and making amends for your past wrongs.  You're not going to backslide on us and go back to the world of banking again after this, are you?"
  wt_image banker_school_3_13
  bethany.c "Never.  Only honest work for me from now on."
  hannah.c "We're all glad to hear that, Bethany."
  wt_image banker_school_3_16
  hannah.c "Audience members, I'd like you to know that after our last session, we had Bethany thoroughly checked out by a doctor.  Not only did she receive a clean bill of health to participate in this new session, but the doctor helped us clarify exactly how much electricity we could run through her, and how to do so safely."
  wt_image banker_school_3_2
  hannah.c "You'll notice that for today, we have her feet resting in pails of water.  Bethany, can you tell the audience what water is vis-a-vis electricity?"
  wt_image banker_school_3_14
  "Shaking slightly, she replies."
  bethany.c "A conductor."
  hannah.c "That's right! I can see you did do well in school.  And as a conductor, its going to help us spread the pain you experience today through a wider part of your nervous system. Isn't science great!"
  wt_image banker_school_3_16
  hannah.c "In the spirit of science, this time around we're going to do a formal count up, incrementally increasing the voltage Bethany is subjected to. Those of you at home who like to take notes can record and share your observations regarding the changes in our subject's demeanor after each incremental increase.  Let's start at level 1 for our base case."
  wt_image banker_school_3_17
  "*zzzzttttt*"
  bethany.c "nnnnnnnnn"
  hannah.c "Did that hurt or was it just a tickle?"
  wt_image banker_school_3_18
  bethany.c "It hurt!"
  hannah.c "Are you sure?  Let's compare to level 2."
  wt_image banker_school_3_19
  "*zzzztttt*"
  bethany.c "nnnnnnnnn!!"
  hannah.c "Now would you say level 1 really hurt, or was it just a tickle compared to level 2?"
  wt_image banker_school_3_20
  bethany.c "They both hurt!"
  hannah.c "But did level 2 hurt more or less than level 1?"
  wt_image banker_school_3_3
  bethany.c "More"
  wt_image banker_school_3_4
  hannah.c "Okay, with that established, who would like to hypothesize what will happen at level 3?  Bethany, what would you say?"
  wt_image banker_school_3_21
  bethany.c "It's going to hurt more."
  hannah.c "Let's see if you're right?"
  wt_image banker_school_3_23
  "*zzzztttt*"
  bethany.c "NNNNNNNNN!!"
  wt_image banker_school_3_22
  hannah.c "That did sound like more pain.  So what do we think level 4 will do?  more, less or the same?"
  wt_image banker_school_3_21
  "Bethany fights back tears through her tightly shut eyes as she replies."
  bethany.c "More"
  wt_image banker_school_3_5
  "*zzzztttt*"
  bethany.c "Aaarrgghhh!!"
  hannah.c "I think we've established a pattern, so I'm going to guess that level 5 is even worse."
  wt_image banker_school_3_8
  "*zzzzttttt*"
  bethany.c "Aaarrrggghhhh!!!"
  wt_image banker_school_3_25
  hannah.c "I think we have enough evidence to conclude that Bethany's hypothesis was correct.  The higher the setting, the more pain the electricity is causing her."
  wt_image banker_school_3_26
  hannah.c "Let's move on to another experiment.  So far, the electricity has passed into her body through the electrodes on her skin and the water around her feet."
  wt_image banker_school_3_6
  hannah.c "What if we pass some of the electricity through her internally?"
  wt_image banker_school_3_27
  hannah.c "I'm going to stay at level 5 for the moment, because it's important to change only one variable at a time when you're doing experiments.  So the amount of electricity Bethany receives is going to be the same, but some of it is going to be discharged directly into her pussy."
  wt_image banker_school_3_7
  hannah.c "Bethany, your memory of the details of our last session is a little foggy isn't it?"
  bethany.c "Ye .. yes."
  wt_image banker_school_3_28
  hannah.c "I understand severe pain can do that.  So you probably don't know the answer to this, but I bet some of our audience members do.  Keeping the total electric current the same, but discharging it internally rather than externally, is Bethany going to hurt more, less, or the same on the next zap?  Keep your answers to yourself and let's find out if you were right."
  wt_image banker_school_3_24
  "*zzzztttt*"
  bethany.c "AAARRRGGHHH!!!"
  wt_image banker_school_3_27
  hannah.c "What do you think Bethany, did that hurt more, less or the same?"
  "The ex banker pants, trying to collect her thoughts and find her voice."
  wt_image banker_school_3_29
  hannah.c "Hard to tell is it?  Let's try again.  Does this hurt more, less or the same?"
  wt_image banker_school_3_9
  "*zzzztttt*"
  bethany.c "AAAAAARRRRRRGGHHH!!!  MORE!!  MORE!!!"
  wt_image banker_school_3_30
  hannah.c "Bethany, are you asking for more?  You're not turning into a pain slut and starting to enjoy this, are you?"
  "The bound woman shakes her head frantically."
  wt_image banker_school_3_28
  hannah.c "That's good, because I'm sure many in our audience would be disappointed if they thought you were enjoying this on any level.  They paid their money to watch you suffer.  Are you suffering, Bethany?"
  "She nods her head up and down, perhaps hoping for mercy.  None is coming."
  wt_image banker_school_3_27
  hannah.c "And now that I've adjusted the setting to 6, you're going to suffer more, aren't you?"
  bethany.c "nn nn nn"
  wt_image banker_school_3_31
  "*zzzztttt*"
  bethany.c "Eeeerrrkkkkk"
  hannah.c "Oh, that's a new sound!  Have we hit a new threshold?  When I go to level 7, do we stay with this sound or go back to the full throated screams?"
  wt_image banker_school_3_9
  "*zzzztttt*"
  bethany.c "EEEERRRRKKKKK"
  wt_image banker_school_3_20
  hannah.c "Bethany, your mouth is open, but you're not screaming properly.  Can't you articulate your pain anymore?"
  "It takes a moment, but eventually Bethany shakes her head."
  wt_image banker_school_3_10
  hannah.c "Last session you were still screaming at level 8, Bethany.  Maybe when I adjust the level up one more, you can give us one more scream?"
  wt_image banker_school_3_31
  "*zzzztttt*"
  bethany.c "RRRRKKKK"
  hannah.c "No?  Well, I guess the doctor's advice was correct.  Using the water on your feet is increasing the amount of pain you experience relative to the amount of electricity flowing through you."
  wt_image banker_school_3_32
  hannah.c "However, he also told us not to worry about bumping the voltage up, because even though it will hurt like hell, it won't harm you.  So here goes level 9."
  wt_image banker_school_3_33
  "*zzzzttttt*"
  bethany.c "RRRRKKKK"
  "Bethany's head falls back, her fingers curling into tight fists."
  hannah.c "And of course, level 10."
  wt_image banker_school_3_31
  "*zzzzzttttt*"
  "Bethany just shakes, silently, no sound escaping her clenched throat."
  hannah.c "Which I'm told you can take again ...  "
  wt_image banker_school_3_23
  "*zzzzzttttt*"
  hannah.c "... and again ..."
  wt_image banker_school_3_31
  "*zzzzztttt*"
  hannah.c "... and again. "
  wt_image banker_school_3_33
  "*zzzzttttt*"
  wt_image banker_school_3_11
  hannah.c "Are you still with us Bethany?"
  "It takes a moment, but she eventually nods her head, her fingers still curled up like claws."
  hannah.c "Say good bye to our audience now, Bethany, and thank them again for their financial contribution."
  wt_image banker_school_3_21
  hannah.c "Bethany?  Bethany can't you speak at the moment?"
  "She shakes her head softly."
  wt_image banker_school_3_32
  hannah.c "I guess we'll just have to settle for a silent thank you."
  wt_image banker_school_3_33
  "*zzzzztttttt*"
  "Bethany's whose body tenses and clenches up again in agony."
  wt_image banker_school_3_20
  hannah.c "Have a good evening everyone."
  wt_image living_room.image
  if bethany.torture_count == 4:
    $ bethany.torture_count = 6
    $ title = "Ask Hannah to Domme you again?"
  else:
    $ bethany.torture_count = 5
    $ title = "Reconsider Hannah's request to torture you?"
  menu:
    "Yes, you'd like to serve her" if bethany.torture_count == 6:
      wt_image banker_school_2_39
      call hannah_school_torture_session_serve_her from _call_hannah_school_torture_session_serve_her_1
    "Let her torture you" if bethany.torture_count == 5:
      wt_image banker_school_2_18
      player.c "I've thought it over, and on second thought I am willing to volunteer to be your victim for a future fund raising session."
      wt_image banker_school_2_19
      hannah.c "Good.  I'm looking forward to hurting you.  I'll be in touch when I'm ready."
      $ bethany.torture_count = 2
      $ bethany.torture_week = week + 3
    "Suggest she become a professional Domme":
      wt_image banker_school_2_39
      call hannah_school_torture_session_suggest_become_domme from _call_hannah_school_torture_session_suggest_become_domme_1
    "No thanks":
      pass
  change player energy by -energy_very_short notify
  return

# School Torture Session - Ask her to Domme you again?
label hannah_school_torture_session_serve_her:
  "When you're able to collect your breathe, you ask her for a repeat performance."
  player.c "Would you be able to do that to me again?  I'd love to serve you."
  "She's taken aback."
  hannah.c "Really?  Did you somehow manage to enjoy me torturing you?"
  player.c "I did.  Not all of it.  Not much of it, actually.  But being under your control, yes, that I enjoyed."
  hannah.c "You're even more sick that I realized.  No, I don't have time for ... whatever it would be if you and I were doing this on a regular basis."
  $ title = "Make another suggestion?"
  menu:
    "Suggest she become a professional Domme":
      call hannah_school_torture_session_suggest_become_domme from _call_hannah_school_torture_session_suggest_become_domme_2
    "You'll pay her":
      call hannah_school_torture_session_youll_pay_her from _call_hannah_school_torture_session_youll_pay_her
    "No thanks":
      pass
  return

# School Torture Session - Suggest she become a professional Domme?
label hannah_school_torture_session_suggest_become_domme:
  player.c "You're good at this. Sadistic and aloof.  You shouldn't stop with these fund raisers.  You could do this professionally."
  hannah.c "I already have a profession.  I'm a teacher, and now a Principal.  That's enough responsibility."
  player.c "I'm sure it is, but you could supplement your income, perhaps even help the school financially by doing this in your spare time.  Besides, you enjoy it."
  "She thinks for a few minutes before replying."
  hannah.c "If I did want to do this professionally, I suppose you'd help me with the logistics?"
  player.c "I would."
  if player.has_tag('club_access'):
    hannah.c "Where would I work?  I've been pushing my luck using our school basement for these fundraisers.  I don't want to be responsible for bringing a group of degenerates into my school."
    player.c "Clients.  The word you're looking for is clients, not degenerates.  Don't worry.  I can get you access on an as-needs basis to our local Club.  It's fully equipped, so you'll have access to everything you need to 'entertain' properly."
    player.c "They don't normally allow professionals to use the Club, but when I explain that its really a school fundraiser, I'm sure they'll give you access for a reasonable fee."
    hannah.c "Okay. I'll try it.  But if it cuts into the quality of the work I can do for the school or the children, I'm stopping. Understood?"
    player.c "Yes, Ma'am.  I'll set things up for you."
    call convert(hannah, "domme") from _call_convert_18
  else:
    hannah.c "Where would I work?  I've been pushing my luck using our school basement for these fundraisers.  I don't want to be responsible for bringing a group of degenerates into my school."
    player.c "Clients.  The word you're looking for is clients, not degenerates.  How about your house?"
    hannah.c "There's no way I'm letting my degenerate clients know where I live."
    player.c "Okay, my house then?"
    hannah.c "I am never going back to your house.  I remember what you did to me the last time I was there."
    player.c "Well, we could rent a space, if you think you can work enough shifts to make that worthwhile?"
    hannah.c "I'm the principal for a busy school.  I'll be lucky if I can find time for one client a week."
    player.c "Alright.  Leave it with me.  I'll see if I can find a suitable and inexpensive location."
  $ hannah.action_contact_domme = living_room.add_action("Arrange Session for Mistress Hannah", label = hannah.short_name + "_contact_domme", context = "_contact_other", condition = "hannah.can_be_interacted and hannah.domme_outfit_count < 4 and not hannah.has_tag('doll')")
  return

# School Torture Session - You'll pay her?
label hannah_school_torture_session_youll_pay_her:
  player.c "I'll pay you."
  hannah.c "You'll pay me to hurt you?"
  player.c "Yes.  I know you could use the extra money for the school."
  hannah.c "That's true.  Why don't you just give me the money.  That would hurt you, wouldn't it?  Financially, I mean."
  player.c "What would I get out of that?"
  hannah.c "You'd be helping out the school, for starters.  Maybe more to your taste, you'd be doing exactly what I want you to do: giving me your money."
  $ title = "What now?"
  menu:
    "Suggest she become a professional Domme":
      call hannah_school_torture_session_suggest_become_domme from _call_hannah_school_torture_session_suggest_become_domme_3
    "Agree to financial domination":
      player.c "How much do you want, Mistress?"
      hannah.c "Let's start with 25 a week, beginning today."
      player.c "Yes, Mistress."
      $ hannah.financial_domination_cost = 25
      change player money by -hannah.financial_domination_cost notify
    "No thanks":
      pass
  return

## Club President Wife Content
label hannah_gloria_other_talk_option:
    if gloria.discussed_principal == 1:
        player.c "A friend of mine is the principal of a local school. The school's run into some money problems and needs a generous donor to help them out."
        gloria.c "Ugghh. Schools. My husband and I don't have any children. Why would we want to contribute to the education of someone else's brats?"
        player.c "Don't be like that. Children are precious. They're the future, don't you know. Besides, my friend is very good looking lady, and will make sure you and your husband feel very appreciated for your donation."
        gloria.c "How appreciated?"
        player.c "Completely appreciated."
        gloria.c "Okay. Bring her by and the morning and we'll listen to her pitch. If she's not willing to close the deal though, our money stays in our pocket. We don't give away our donations to charity cases."
        $ gloria.discussed_principal = 2
    return

## Lawyer Content
label hannah_janice_talk_option:
    if hannah.lost_money_and_no_fix == 2 and not janice.has_tag('discussed_school_money_woes'):
        "Janice, the local school seems to have fallen on hard times, financially. Would you be willing to help them out?"
        janice.c "A public school? What would be the point? The kids would get as good an education living on the streets as urchins."
        add tags 'discussed_school_money_woes' to janice
        $ janice.temporary_count = 0
    return

## Marilyn Content
label hannah_marilyn_talk_option:
    if hannah.lost_money_and_no_fix == 2:
        player.c "Marilyn, the local school seems to have fallen on hard times, financially.  Would you be willing to help them out?"
        marilyn.c "A school?  Seriously?  Half of my organization didn't even make it through school, the rest have no fond memories of their time there.  A school would be the last place I'd give money to."
        if marilyn.favour > 0:
            $ title = "Call in your favor?"
            menu:
                "Yes, ask Marilyn for help":
                    player.c "You owe me one, remember?"
                    marilyn.c "Fine.  I'll arrange for the school to get the financing it needs."
                    player.c "You'll cut them a check?"
                    marilyn.c "Don't be silly.  It's a public school.  I'll make sure someone finds some public money to support it."
                    "Nothing to do now but wait until you hear from Hannah about whether this solved her problem."
                    $ marilyn.favour -= 1
                    $ hannah.lost_money_and_no_fix = 3
                    rem tags 'available_for_school_visit' from hannah
                    $ hannah.visit_week = week
                    $ hannah.marilyn_solution_thank_you = 1
                    if hannah.visit_day == 0:
                        if day == 1:
                            $ hannah.visit_day = 2
                        elif day == 5:
                            $ hannah.visit_day = 4
                        else:
                            $ hannah.visit_day = day
                "No, find someone else to help":
                    pass
    if hannah.group_sex == 3:
        player.c "Marilyn, do you have any men who've earned a 'bonus'?"
        marilyn.c "What do you mean?"
        player.c "I mean I know a pretty lady who's looking for a group of burly men to have their way with her.  I thought you might want to offer her to some of your men, as an employee thank you for doing good work."
        marilyn.c "And what do you want from me in return?"
        player.c "An IOU.  And a promise that your men will keep her safe, even when they're 'forcing' their way with her."
        marilyn.c "Deal"
        $ hannah.group_sex = 4
    return

## Character Specific Timers
# Convert Character to Doll
label hannah_convert_doll:
  call convert(hannah, "doll") from _call_convert_19
  $ hannah.suffix = "the Maid Doll"
  $ hannah.training_regime = 'daily'
  $ hannah.fixed_location = basement
  $ hannah.location = basement
  $ hannah.visit_week = 0
  $ hannah.letter_re_terri = 4
  $ hannah.lost_money_and_no_fix = 3
  $ bethany.torture_week = 0
  $ master_m.lend_diamond_to_school = 0
  rem tags 'follows' from hannah
  rem tags 'ready_for_sex_at_school' 'available_for_school_visit' 'masquerade_ball_invite' from hannah
  if hannah.has_tag('domme'):
    rem tags 'whore' from hannah #needed as this tag gets added to her when she's a Domme to allow check on her to work properly
    call unconvert(hannah,'domme') from _call_unconvert_40
  elif hannah.has_tag('whore'):
    call unconvert(hannah,'whore') from _call_unconvert_41
  if hannah.group_sex == 0 or hannah.group_sex == 5:
    pass
  else:
    $ hannah.group_sex = 0
    $ living_room.remove_action(hannah.action_contact_group_sex)
  $ living_room.remove_action(hannah.action_contact_visit)
  $ hannah.action_contact_visit = None
  $ living_room.remove_action(bethany.action_contact_check_school)
  return

# Convert Character to Whore
label hannah_convert_whore:
  call convert(hannah, "whore") from _call_convert_20
  $ hannah.training_regime = 'weekly'
  $ hannah.visit_week = 0
  $ hannah.letter_re_terri = 4
  $ hannah.lost_money_and_no_fix = 3
  $ bethany.torture_week = 0
  $ master_m.lend_diamond_to_school = 0
  rem tags 'ready_for_sex_at_school' 'available_for_school_visit' from hannah
  if hannah.group_sex == 0 or hannah.group_sex == 5:
    pass
  else:
    $ hannah.group_sex = 0
    $ living_room.remove_action(hannah.action_contact_group_sex)
  $ living_room.remove_action(hannah.action_contact_visit)
  $ hannah.action_contact_visit = None
  $ living_room.remove_action(bethany.action_contact_check_school)
  return

# Will-Tamer Timers
label hannah_will_tamer_timer:
  $ hannah.will_tamer_count += 1
  if hannah.will_tamer_count == 1:
    add tags 'will_tamer_this_week' to hannah
    $ hannah.training_session()
    player.c "How about we do some role playing?"
    hannah.c "What sort of role playing?"
    player.c "You put this collar on and be the obedient slave and I'll be your Master."
    hannah.c "That's silly.  Besides, I'm nobody's slave."
    player.c "Okay, then how about you be the disobedient, headstrong slave who won't listen to her Master?"
    "She laughs."
    hannah.c "And I suppose my 'Master' wants to do naughty things to me?  You're going to have to be quite persuasive if you expect me to go along with your naughty plans, 'Master'."
    player.c "We'll see.  Come on in and get changed into your collar, slavegirl."
    wt_image principal_wt_20
    "She laughs again as she undresses and turns around to let you collar her.  As you put the Will-Tamer on her, however, she stiffens up."
    wt_image principal_wt_16
    "You can see the conflict in her eyes as they glaze over and shut.  Hannah's not a submissive woman, and the Will-Tamer is a bad fit for her psyche. She's strong and she fights it, but its strong, too, and seeks out any point of weakness."
    wt_image principal_wt_14
    "It eventually latches onto her sense of duty and willingness to be of service to those she cares about.  Normally, this manifests itself in the sacrifices she will make for the school and her students."
    wt_image principal_wt_1
    "The Will-Tamer tries to warp that, turning it into a more general need to please and serve.  It's not entirely successful, but it does render Hannah more pliant than she typically is.  You can take advantage of that, if you want?"
    $ title = "Make use of her?"
    menu:
      "Have some fun":
        player.c "Down, slave.  Provide your Master with pleasure."
        wt_image principal_wt_3
        "Without a word, she sinks down and takes you into her mouth.  So far so good."
        $ title = "Where do you want to fuck her?"
        menu:
          "In her mouth":
            wt_image principal_wt_4
            "Grabbing her by the hair, you pull her forward."
            player.c "Open wide, slave.  Take your all of your Master's cock."
            wt_image principal_wt_5
            "Under the influence of the Wll-Tamer, she's in no condition to object.  She opens her mouth wide as you shove your cock forward, until the head of your cock reaches the back of her throat."
            wt_image principal_wt_17
            player.c "No gagging, slave.  Relax your throat.  Take all of me inside."
            wt_image principal_wt_6
            "Pulling her head forward, you're soon able to bury your cock into her mouth to your balls, the head of your cock nestled into the back of your throat.  It's as good a position as any to cum in a slave."
            wt_image principal_wt_18
            "Lost to the Will-Tamer, she doesn't even react as your hot load spurts down the back of her throat."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_blowjob_count += 1
            $ hannah.hypno_swallow_count += 1
          "In her pussy":
            player.c "Turn around, slave, your Master wants to fuck you."
            wt_image principal_wt_21
            "A look of anguish crosses her face, which you're pretty sure is her fighting the Will-Tamer, rather than an objection to fucking you.  You reach out and take her by the hair to steady her."
            player.c "Relax, slavegirl, and enjoy being fucked by your Master.  Focus on how good my cock feels and forget about everything else."
            wt_image principal_wt_22
            "That calmed her.  It's difficult for her to fight the collar while she's distracted by the pleasure between her legs as you fuck you her."
            wt_image principal_wt_7
            "Before long her face glazes over completely.  While you'd like to think it was your fucking skills, you know that's the Will-Tamer re-wiring her.  The thought her being claimed while your cock is inside of her brings you over the edge."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_sex_count += 1
          "In her ass" if hannah.anal_count > 0:
            player.c "Turn around, slave, your Master wants to fuck you in the ass."
            wt_image principal_wt_9
            "She says nothing as she turns over, but she stares, open-eyed, at you as push into her, as if to ask, 'Why are you fucking my ass instead of helping me?'"
            wt_image principal_wt_24
            "It's kind of cute, watching her look for help she can't articulate the words to ask for.  She's fighting hard against the collar, but it's as inevitable that she'll lose that battle as it is that her tight butthole will coax you to flood her bowels with jizz."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_anal_count += 1
        wt_image principal_wt_16
        "You've left the Will-Tamer on as long as is safe for a first wearing.  You slip it off and watch the life come back into her eyes as she hangs her head and blinks."
        orgasm notify
      "Just let the Will-Tamer work":
        wt_image principal_wt_16
        "You leave the Will-Tamer on for as long as seems safe for a first wearing, which in her case seems a little shorter than for others, she's fighting it so much.  When you remove the collar, she hangs her head and seems confused."
    wt_image principal_wt_2
    hannah.c "What happened?  Did we ... do things?"
    player.c "We had a little fun as slavegirl and Master, yes.  I think you really got into it."
    hannah.c "Did I?  I'm feeling a little off.  I should probably get going."
    if hannah.has_tag('booty_call_in_progress'):
      if hannah.booty_call_count > 1:
        $ hannah.temporary_count = 0 # breaks menu choice cycle
    elif hannah.has_tag('booty_call'):
      $ hannah.random_number = renpy.random.randint(1, 10)
      if hannah.random_number < 3:
        $ hannah.visit_week = week + 1
      elif hannah.random_number < 8:
        $ hannah.visit_week = week + 2
      else:
        $ hannah.visit_week = week + 3
      call character_location_return(hannah) from _call_character_location_return_696
    else:
      call character_location_return(hannah) from _call_character_location_return_697
  elif hannah.will_tamer_count == 2:
    $ hannah.training_session()
    add tags 'will_tamer_this_week' to hannah
    player.c "How about we do some more role playing?"
    wt_image principal_booty_call_1_37
    "She hesitates.  Before she can respond, you jump back in."
    player.c "I really had fun last time, and I think you did too."
    hannah.c "Did I?  All I really remember is you putting the collar on me."
    wt_image principal_booty_call_1_11
    player.c "And making me happy.  You remember that, don't you?  You're wearing too many clothes for a slavegirl.  Turn around and pull down your top.  You look really hot in the collar.  I'm going to put it on you again."
    wt_image principal_wt_20
    "She doesn't look convinced, but she can't seem to bring herself to refuse.  A worried look on her face, she turns and lets you collar her.  As you lock it in place, she stiffens up again."
    wt_image principal_wt_16
    "The conflict inside her is, if anything, worse this time around. You can almost see her brain trying to resist the changes the Will-Tamer wants to make. Her eyes glaze over, and you're not entirely sure she's still with you."
    wt_image principal_wt_14
    player.c "Slave, can you hear?  Hannah, are you in there?"
    wt_image principal_wt_1
    "She opens her eyes, but is otherwise unable to respond."
    $ title = "Make use of her?"
    menu:
      "Have some fun":
        player.c "Down, slave.  Provide your Master with pleasure."
        wt_image principal_wt_10
        "Her eyes are lifeless, but her body does as she's told.  A bead of sweat runs down her face, tangible evidence of the struggle taking place in her brain as her mouth opens wide to accept your cock."
        $ title = "Where do you want to fuck her?"
        menu:
          "In her mouth":
            wt_image principal_wt_5
            "There's no need to give her instructions.  She's putty in your hands.  You grab her by the hair and shove your cock deeper into her mouth."
            wt_image principal_wt_6
            "She doesn't react as you bury your cock into her mouth to your balls, the head of your cock nestling into the back of your throat as you thrust forward."
            wt_image principal_wt_19
            "She just squats there, unmoving, her eyes open but unseeing as you fuck her mouth."
            wt_image principal_wt_18
            "She doesn't even react as your hot load spurts down the back of her throat."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_blowjob_count += 1
            $ hannah.hypno_swallow_count += 1
          "In her pussy":
            wt_image principal_wt_11
            "There's no need to give her instructions, and she likely couldn't follow them if you did.  You simply pull her legs apart and shove your cock inside."
            wt_image principal_wt_12
            "If she's aware that you're fucking her, she shows no sign.  She simply stares, open jawed, the strain on her face gradually relaxing as she slowly loses the battle being waged in her brain."
            wt_image principal_wt_23
            "As fun as it is to watch her lose the fight against the collar, there's only so long you can fuck her soft, warm pussy before your balls need to fill it with your jizz."
            player.c "[player.orgasm_text]"
            $ hannah.hypno_sex_count += 1
          "In her ass":
            "There's no need to give her instructions, and she likely couldn't follow them if you did.  She's putty in your hands, and you can use her however you want."
            wt_image principal_wt_13
            "She pays you no heed as you roll her over and push yourself into her backdoor.  If she's aware that you're fucking her ass, she shows no sign.  She simply stares, open jawed as she slowly loses the battle being waged in her brain."
            wt_image principal_wt_13
            "As fun as it is to watch her lose the fight against the collar, there's only so long you can fuck her tight rosebud before your balls need to fill it with your jizz.  Just as you let go, she turns her head to look at you.  Maybe it's a final plea for help, or maybe it's simply a reaction to the cum enema you're delivering."
            player.c "[player.orgasm_text]"
        wt_image principal_wt_2
        "You've left the Will-Tamer on as long as is safe for one session. You slip it off and watch the life slowly come back into her eyes, leaving her totally disoriented."
        orgasm notify
      "Just let the Will-Tamer work":
        "You leave the Will-Tamer on for as long as seems safe for one session, which in her case seems a little shorter than for others, she's fighting it so much."
        wt_image principal_wt_2
        "When you remove the collar, she's totally disoriented."
    hannah.c "I ... I'm feeling a little woozy.  I need to go."
    "Hannah is not responding well to the Will-Tamer.  If you use it on her again, the Hannah you know will be gone.  What would replace her you don't know, but it's unlikely to be an obedient slavegirl, considering how hard her brain is fighting to resist the Will-Tamer's influence."
    if hannah.has_tag('booty_call_in_progress'):
      if hannah.booty_call_count > 1:
        $ hannah.temporary_count = 0 # breaks menu choice cycle
    elif hannah.has_tag('booty_call'):
      $ hannah.random_number = renpy.random.randint(1, 10)
      if hannah.random_number < 3:
        $ hannah.visit_week = week + 1
      elif hannah.random_number < 8:
        $ hannah.visit_week = week + 2
      else:
        $ hannah.visit_week = week + 3
      call character_location_return(hannah) from _call_character_location_return_698
    else:
      call character_location_return(hannah) from _call_character_location_return_699
  elif hannah.will_tamer_count > 2:
    sys "If you put the collar on her again, both it - and Hannah - will be lost, fusing into ... something else."
    $ title = "Do you want to use the Will-Tamer on her?"
    menu:
      "Yes, convert her":
        player.c "You fill a need for me, Hannah.  Having you serve me in your collar makes me intensely happy.  Kneel down for me, Hannah, and make it easy for me to attach your collar."
        wt_image principal_wt_25
        hannah.c "Do you really ... do you really need to do this?"
        "Even as she says the words, she sinks to her knees, pulling her top down without being asked and looking up at you forlornly."
        wt_image principal_wt_15
        $ title = "Do you really need to do this?"
        menu:
          "Need, want, whatever ... convert her":
            $ hannah.training_session()
            player.c "What I need is not important.  What I want is your only concern.  That's why you're kneeling, isn't it?  Because it's what I want, to make life easier for me."
            hannah.c "I ... I'm not sure.  I'm so confused right now.  I can't seem to think straight."
            wt_image principal_wt_26
            player.c "It's okay, Hannah.  Life is about to become a lot simpler.  Look at your collar.  Where should it be?"
            hannah.c "It ... it should be around my neck, but I don't understand why, because I don't think it's safe for me to have it there.  What do you mean things are going to become simpler?  What's happening to me?  Why can I hear the collar in my head, telling me to give in and let go?  I can't listen to it.  I need to fight it."
            wt_image principal_wt_20
            "You gently stroke her hair as you attach the collar."
            player.c "Shhhh.  No worries now.  Just say goodbye, Hannah."
            hannah.c "G ... goodbye?"
            wt_image principal_wt_16
            "Hannah's eyes go lifeless, then they shut."
            wt_image principal_wt_14
            "Her body shakes, as an epic, final battle is waged for control of her mind."
            wt_image principal_wt_1
            "It takes a while, but eventually her eyes open again.  The Will-Tamer has won, absorbing itself into her as it claims her, but it's a pyrrhic victory.  Her mind is a scorched earth, bereft of intelligence or higher functions.  She opens her mouth and utters a single word."
            hannah.c "Serve"
            player.c "Is that what you're for now, to serve?"
            hannah.c "Serve"
            "You can get nothing more from her.  Fortunately, she kept her relationship with you a secret.  No one knows she was here, so no one knows to come looking for her."
            call forced_movement(basement) from _call_forced_movement_987
            summon hannah
            $ hannah.change_image('principal_doll_1')
            wt_image principal_doll_28
            "Still, she can't be seen like this around your house, so you take her down to the basement, and find some clothing more suited to her current status."
            wt_image principal_doll_1
            "Then you lean her up against a padded part of the wall.  She'll wait there until you're ready to use her."
            rem 1 will_tamer from player
            add tags 'transformed' to hannah
            $ hannah.transformed_via_object = True
            call hannah_convert_doll from _call_hannah_convert_doll
            if hannah.booty_call_count > 1:
              $ hannah.temporary_count = 0 # breaks menu choice cycle
          "No, not now":
            player.c "Let's do something else today."
            wt_image principal_wt_25
            "Relief washes over Hannah as she stand back up."
            hannah.c "Oh good!  What are you in the mood for?"
            wt_image principal_booty_call_1_2
            if hannah.booty_call_count == 1:
              jump menu_hannah_booty_call_outfit_1 # returns to correct place in this session
      "No, not now":
        player.c "Let's do something else today."
        "Relief washes over Hannah."
        hannah.c "Oh good!  What are you in the mood for?"
        if hannah.booty_call_count == 1:
          jump menu_hannah_booty_call_outfit_1 # returns to correct place in this session
  return

########### ROOMS ###########
# Examine School
label sch_examine:
    "A local school."
    return

# Prevent Access to School
label sch_no_access:
    "You shouldn't be able to access the school this way."
    return

label sch_enter:
  return

label sch_exit:
  return

################################### NOTES ###################################
##################### TODO #####################
# need to restore booty calls after solving money problems

## NEED Add:
# Restaurant Date w Moneybags
# she Dommes you fantasy (Domme 14 set)
# rape fantasy (Rough 1)
# degraded state (incl Rough 1 BJ plus Degraded sets)
# transformed whore state (Whore 6 set)

## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
