## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
register tracy_pregame 20 in core as "Tracy the Club Member" #Note: must load after all other clients re action names

# Pregame
label tracy_pregame:
  python:
  ## Constants
    model_credits += [('support', "Tracy the Club Member (Celeste Star)")]
    model_credits += [('bit', "Tracy's Asian Date (Sophie Jade)")]
    model_credits += [('bit', "Tracy's Black Date (Jade Nacole)")]
    model_credits += [('bit', "Tracy's Blonde Date (Lily Labeau)")]
    model_credits += [('bit', "Tracy's Tomboy Date (Alani Pi)")]
    model_credits += [('bit', "Tracy's Young Date (Krystal Banks)")]

    ## Character Definition
    # Red
    tracy = Person(Character("Club Member", who_color="#FF0000", what_color="#FF0000", window_background=gui.dialogue_background_medium_font_color), "tracy", cut_portrait = True, prefix = "", suffix = "", wait_for_message_period = 8, prospect_min_reputation = 2, available_on_weekends = False)

    # Other Characters
    # Navy
    husband_tracy = Character("Tracy's Husband", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    tracy_lesbian_blonde = Character("Blonde Girl", who_color="#0000FF", what_color="#0000FF", window_background=gui.dialogue_background_dark_font_color)
    # Teal
    tracy_lesbian_asian = Character("Asian Girl", who_color="#00c4c4", what_color="#00c4c4")
    # 128,0,255
    tracy_lesbian_brunette = Character("Brunette Girl", who_color="#8000FF", what_color="#8000FF")
    # Dark Brown
    tracy_lesbian_black = Character("Black Girl", who_color="#401A00", what_color="#401A00", window_background = gui.dialogue_background_dark_font_color)
    # Wine
    tracy_lesbian_tomboi = Character("Tomboi", who_color="#800040", what_color="#800040", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    tracy.action_talk = tracy.add_action("Talk to her", label="_talk", condition = "tracy.can_be_interacted and not tracy.has_tag('initial_talk_complete')")
    tracy.action_calling = living_room.add_action("Arrange lesbian session For Tracy", label = tracy.short_name + "_calling", context = "_contact_other", condition = "tracy.can_be_interacted and tracy.has_tag('arrangement')")

    ######## EXPANDABLE MENUS #######
    ## Dates
    tracy_session_date_menu = ExpandableMenu("Who do you want Tracy to spend time with?", cancelable = False)
    tracy.choice_session_date_menu_bring_her_own = tracy_session_date_menu.add_choice("Bring her own date", "tracy_calling_bring_own_date")
    tracy.choice_session_date_menu_chelsea = tracy_session_date_menu.add_choice("[chelsea.name]", "tracy_calling_chelsea", condition = "chelsea.lesbian_status > 1 and not tracy.has_tag('considered_chelsea')")
    tracy.choice_session_date_menu_diamond = tracy_session_date_menu.add_choice("Diamond", "tracy_calling_diamond", condition = "diamond.lesbian_training > 0")
    tracy.choice_session_date_menu_elsa = tracy_session_date_menu.add_choice("Elsa", "tracy_calling_elsa", condition = "elsa.has_tag('likes_girls') and (elsa.has_tag('girlfriend') or elsa.has_tag('hypno_girlfriend') or elsa.has_tag('continuing_actions')) and elsa.can_be_interacted")
    tracy.choice_session_date_menu_janice = tracy_session_date_menu.add_choice("Janice", "tracy_calling_janice", condition = "janice.has_tag('asked_about_hiring') and not tracy.has_tag('considered_janice')")
    tracy.choice_session_date_menu_marilyn = tracy_session_date_menu.add_choice("Marilyn", "tracy_calling_marilyn", condition = "player.marilyn_building_visit_count > 0 and not tracy.has_tag('considered_marilyn')")
    tracy.choice_session_date_menu_sam = tracy_session_date_menu.add_choice("Sam", "tracy_calling_sam", condition = "not tracy.has_tag('considered_sam')")
    tracy.choice_session_date_menu_sarah = tracy_session_date_menu.add_choice("Sarah", "tracy_calling_sarah", condition = "sarah.has_tag('girlfriend') and sarah.has_tag('likes_girls') and sarah.college_friend_outfit > 0 and sarah.can_be_interacted")

    ## Tags
    # Common Character Tags
    tracy.add_tags('can_be_in_club', 'no_hypnosis', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    tracy.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('tracy_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    tracy.add_stats_with_value('hypno_orgasm_count')

    # Character Specific Variables
    tracy.add_stats_with_value('diamond_outfit', 'elsa_outfit', 'event_week', 'lesbian_outfit', 'lose_her_countdown', 'frigid_scene', 'opp', 'reference')
    # guide to tracy.opp:  0: Tracy events not activated yet, 1: saw Tracy with Sam, 2: Tracy's husband will contact you, 3: Tracy events shut off, 4: blackmailed her with follow up, 5: blackmailed her one time
    tracy.week_available = tracy.event_week
    tracy.wait_on_message = False
  return

# Initial Contact Message
# OBJECT: Check Messages
label tracy_message:
  # note: only triggers when you have Club access, hence Club references below
  $ tracy.change_full_name("", "Tracy", "the Former Club Member")
  husband_tracy "{i}I'm having trouble with my wife, Tracy. She's afflicted with desire for women. She swears to me that she fights it and that she isn't giving in to these urges, but I can see that they are eating away at her.{/i}"
  husband_tracy "{i}We used to be members of the Club, but I had to get her out of there. I thought an environment where she could have normal male-to-female sex with attractive men of her choosing in a safe place where she wasn't running around behind my back would help her fight her demons, but I was wrong.{/i}"
  husband_tracy "{i}We met too many women there who didn't have her willpower and were bad role models. Even taking her out of there, though, she keeps slipping. Her demons keep getting the better of her, and I find evidence of her letting these women with bad morals take advantage of her.{/i}"
  if tracy.has_tag('sex_with_sam'):
    husband_tracy "{i}Tracy remembers meeting you at the Club. When I suggested we get her some help, she asked me to check out your profile. From what I've read, it seems like perhaps you might be able to help. Would you have an exploratory session with her and let me know if you think you could be able to help her?{/i}"
  else:
    husband_tracy "{i}Tracy remembers hearing about you when we were at the Club. From what I've read from your online profile, it seems like perhaps you might be able to help. Would you have an exploratory session with her and let me know if you think you could be able to help her?{/i}"
  $ title = "Accept the engagement?"
  menu:
    "Yes (ends day)":
      #$ tracy.change_status("minor_character") # this is done in pregame
      rem tags 'no_hypnosis' from tracy # to allow subsequent tests to work correctly
      $ living_room.remove_action(tracy.current_client_action)
      summon tracy
      wt_image club_blackmail_visit_1_15
      if tracy.has_tag('sex_with_sam'):
        "Tracy arrives looking rather frazzled."
        wt_image club_blackmail_visit_1_12
        tracy.c "Thank you, thank you so much for accepting my husband's proposal."
        wt_image club_blackmail_visit_1_13
        tracy.c "I didn't know what to do.  He's hell bent on 'curing' me of my interest in girls and I didn't know what he was going to come up with."
        wt_image club_blackmail_visit_1_14
        tracy.c "Then I remembered you and how kind you were to me at the Club.  Before my husband took us out of there I'd heard how you ran a business helping couples, so I suggested your name to my husband.  Then when he looked you up he told me you were exactly what I need."
      else:
        "Tracy arrives looking rather frazzled."
        if tracy.has_tag('sex_with_elsa'):
          player.c "I know you from somewhere, don't I?  I remember now!  You're the woman Elsa hooked up with."
          wt_image club_blackmail_visit_1_1
          "She nods."
        player.c "Why are you here?"
        wt_image club_blackmail_visit_1_13
        tracy.c "It's my husband! He's hell bent on 'curing' me of my interest in girls. I didn't know what he was going to come up with."
        wt_image club_blackmail_visit_1_14
        tracy.c "Before my husband took us out of the Club, I'd heard how you ran a business helping couples, so I suggested your name to my husband.  Then when he looked you up he told me you were exactly what I need."
      wt_image club_blackmail_visit_1_15
      player.c "What do you think you need?"
      wt_image club_blackmail_visit_1_1
      tracy.c "I don't know!"
      $ title = "What do you ask her?"
      menu:
        "Do you want to be cured?":
          player.c "Do you want to be cured?"
          wt_image club_blackmail_visit_1_2
          "She lowers her head."
          tracy.c "I dunno.  I don't really think I'm sick.  I mean, my husband does, but ..."
          player.c "But you haven't bought into the idea that you need to be cured of your interest in women?"
          wt_image club_blackmail_visit_1_13
          "She shakes her head."
          tracy.c "No, I guess I haven't."
        "Do you want to keep seeing women?":
          player.c "Do you want to keep seeing women?"
          wt_image club_blackmail_visit_1_3
          tracy.c "I dunno.  I guess ... I mean, yeah, if I could.  If there was a way that my husband wouldn't find out."
          player.c "So you haven't bought into his idea that you need to be cured of your interest in women?"
          wt_image club_blackmail_visit_1_14
          "She shakes her head."
          tracy.c "No, I guess I haven't."
      $ title = "What do you suggest?"
      menu menu_tracy_message_options:
        "Try hypnosis" if player.can_hypno(tracy) and not tracy.has_tag('hypno_cure_possible'):
          $ tracy.hypno_session() # deducts energy and records she was hypno'd
          player.c "Look at this, Tracy."
          call focus_image from _call_focus_image_32
          player.c "Look at this and listen to me.  Listen to me, Tracy.  Listen to my words.  Only my words, Tracy.  Only my words now."
          wt_image club_blackmail_visit_1_4
          player.c "You want to be comfortable for our talk, Tracy. You want me to be comfortable for our talk. I'm helping you and you want me to be comfortable while I'm helping you, so that I keep helping you."
          wt_image club_blackmail_visit_1_12
          player.c "You will be more comfortable if you take down your dress, Tracy. You'll be more comfortable and I'll be more comfortable. You want me to be comfortable while I'm helping you. Take down your dress so we'll both be more comfortable."
          wt_image club_blackmail_visit_1_5
          "She pulls down her top, exposing her breasts."
          wt_image club_blackmail_visit_1_16
          player.c "We're going to do an experiment, Tracy.  An experiment to help you.  Spread your legs. "
          wt_image club_blackmail_visit_1_6
          player.c "It's okay, you don't need to be nervous.  I'm not going to touch you.  This is an experiment.  An experiment to help you."
          wt_image club_blackmail_visit_1_18
          player.c "Good girl. Now, I want you to think of the sexiest man you can think of. Maybe it's your husband, or an ex boyfriend, or a movie star you like. Whoever he is, he's the sexiest man you know.  What do you want to do when you think of him?"
          wt_image club_blackmail_visit_1_7
          "She pulls her knees together and clutches herself tight."
          player.c "It's okay, don't be scared.  He's not here.  He's not going to touch you.  Is this how you feel when your husband wants to touch you?"
          wt_image club_blackmail_visit_1_10
          "She nods."
          player.c "But you let him touch you anyway, because he's your husband?"
          "She nods again."
          player.c "Do you ever like it when he touches you?"
          "She shakes her head."
          wt_image club_blackmail_visit_1_6
          player.c "Relax, Tracy.  Your husband isn't here.  No man is going to touch you.  Spread your legs again."
          wt_image club_blackmail_visit_1_18
          if tracy.has_tag('sex_with_elsa') and tracy.has_tag('sex_with_sam'):
            player.c "This time I want you to think of the sexiest woman you can think of.  Maybe it's Sam or Elsa or one of your other lovers, or a female movie star you like.  Whoever she is, she's the sexiest woman you know."
          elif tracy.has_tag('sex_with_elsa'):
            player.c "This time I want you to think of the sexiest woman you can think of.  Maybe it's Elsa or one of your other lovers, or a female movie star you like.  Whoever she is, she's the sexiest woman you know."
          elif tracy.has_tag('sex_with_sam'):
            player.c "This time I want you to think of the sexiest woman you can think of.  Maybe it's Sam or one of your other lovers, or a female movie star you like.  Whoever she is, she's the sexiest woman you know."
          else:
            player.c "This time I want you to think of the sexiest woman you can think of.  Maybe it's one of your lovers or a female movie star you like.  Whoever she is, she's the sexiest woman you know."
          wt_image club_blackmail_visit_1_17
          player.c "What do you want to do when you think of her?  Spread your legs and show me."
          wt_image club_blackmail_visit_1_8
          "She reaches between her legs and starts rubbing herself vigorously.  The scent of her arousal fills the room as she quickly brings herself to climax."
          tracy.c "ooooo  ....  OHHH!!"
          $ tracy.hypno_orgasm_count += 1
          if terri.has_tag('assistant'):
            wt_image indy_assistant_11
            "As usual when you hypnotize someone at your house, Terri your assistant has been watching and observing.  Normally she stays quiet and says nothing, keeping her thoughts about your approach to herself. Today, though, she can't hold her tongue."
            terri.c "This poor woman.  You have to help her!  She's sick, so very sick and she doesn't even know it.  You need to cure her of her perversion."
            player.c "I don't know that I can.  You can see how deeply ingrained her sexual response to women is, and how little interest she has in men. It's a core part of who she is. I don't think hypnosis can 'cure' her of this."
            wt_image indy_assistant_10
            terri.c "It has to be able to!  It has to!!  Otherwise, why am I ..."
            player.c "Why are you what?"
            wt_image indy_assistant_22
            terri.c "Nothing. Just ... we need to do something for her. The hell she's living through, you can't ...  You just need to cure her, okay?"
          wt_image club_blackmail_visit_1_17
          if player.test('hypnosis_level', 14):
            "She's too exclusively and strongly oriented towards women for you to change her sexuality through hypnosis.  The best you could do to 'cure' her would be to implant an aversion to the idea of acting on her sexual instincts."
            "She'd still desire women, but you might be able to build on her husband's insistence that this is a 'perversion' to get her to the point that she's unwilling to act on her desires.  Her husband would be happy with that solution. She'd no longer run around on him with women, and she'd still fake interest in him whenever he's in the mood to have sex with her."
            "Tracy herself, however, would be even more miserable than she is now. She'd keep her marriage, but at the cost of any chance of sexual happiness.  She'd still hate it when her husband mounts her. She'll still lust for any beautiful woman she sees. The only thing that would change is that she would hate herself for feeling that lust, and be unwilling to act on it."
            add tags 'hypno_cure_possible' to tracy # so that don't test twice, which would lose one-time impacts
          elif player.has_tag('hypnotist'):
            "You're not a strong enough hypnotist to adjust her sexuality through hypnosis.  Perhaps someday you will be, but for now, she's too strongly oriented towards women only for you to help her through hypnosis."
          else:
            "You're not a strong enough hypnotist to impact her sexuality through hypnosis.  She's too strongly oriented towards women only.  Perhaps there's some other way that you could help 'cure' her, or perhaps you should suggest another arrangement that would help her."
          wt_image club_blackmail_visit_1_1
          "Perhaps there's some other way that you could help 'cure' her or perhaps you should suggest another arrangement that would help her?  You bring her out of her trance while you decide."
          jump menu_tracy_message_options
        "'Cure' her through hypnosis" if tracy.has_tag('hypno_cure_possible'):
          wt_image club_blackmail_visit_1_2
          "It'll take at least eight more sessions, but eventually, you'll teach her to loath her own sexual urges enough that she's unable to act on them.  There's nothing much fun to see during those sessions, just Tracy learning to distrust her own feelings and becoming more and more unhappy with herself, convinced that saving her marriage is paramount and that her demon lust is ruining her life and her husband's."
          player.c "No more pussy, right Tracy?"
          wt_image club_blackmail_visit_1_12
          tracy.c "No more pussy, Sir.  I get sick to my stomach even thinking about acting on my sinful thoughts and letting another woman touch me."
          player.c "You still let your husband touch you, though?"
          wt_image club_blackmail_visit_1_13
          tracy.c "Yes, Sir.  He's my husband and for the sake of our marriage I need to look after his needs."
          wt_image club_blackmail_visit_1_2
          sys "In a later version, when Terri the Hypnotist's Assistant's story is more fully fleshed out, these sessions with Tracy may appear in the game.  For now, we'll just skip them and credit you with the 400 you would have collected from conducting those sessions. And if you need a Reputation boost, her husband will be willing to act as a reference for you."
          if player.has_tag('rep_needed'):
            "Since you're in need of a reputation boost now, you take him up on the offer to provide a reference."
            $ tracy.reference = 2
            rem tags 'rep_needed' from player
            change player reputation by 1
          else:
            $ tracy.reference = 1
          $ tracy.change_status("minor_character")
          $ player.extra_clients_fee_this_week += 175
        "Suggest a possible cure":
          call tracy_message_possible_cure from _call_tracy_message_possible_cure
        "Suggest an arrangement":
          call tracy_message_arrangement from _call_tracy_message_arrangement
      # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
      $ player.extra_clients_fee_this_week += 25
      add tags 'no_hypnosis' to tracy
      change player energy by -energy_short notify
      rem action
      call character_location_return(tracy) from _call_character_location_return_486
      end_day
    "Not yet":
      "You have until the end of week [tracy.accept_limit] to accept this engagement."
      $ tracy.current_client_action.name = "Reply to Tracy's Husband"
      if not tracy.wait_on_message:
        $ tracy.wait_on_message = True
        $ tracy.message_note = add_note((tracy.wait_for_message_period + 1) * 5, "{} offer ends".format(tracy.name))
    "Never (deletes message)":
      $ tracy.change_status("rejected")
  return

label tracy_message_possible_cure:
  player.c "I may be able to help you, Tracy."
  wt_image club_blackmail_visit_1_1
  tracy.c "Help me?  How?"
  player.c "By finding a cure to your lesbianism."
  wt_image club_blackmail_visit_1_2
  "She hangs her head.  That wasn't what she was hoping to hear."
  tracy.c "What cure?"
  $ tracy.temporary_count = 1
  if player.has_item(love_potion):
    "The love potion could be a solution, sort of. If her husband gave it to her, it wouldn't make her want women any less, but it may make her sufficiently smitten with her husband that she wouldn't dare act on her urges, for fear of losing him."
    $ tracy.temporary_count = 0
  if player.has_tag('das_access'):
    if player.has_item(love_potion):
      "If you sent her husband to Lilian, you're pretty sure Lilian would let him fill a 'prescription' to buy his own love potion, rather than using yours."
    else:
      "If you sent her husband to Lilian, you're pretty sure Lilian would let him fill a 'prescription' for a love potion he could give to her.  It wouldn't make her want women any less, but it may make her sufficiently smitten with her husband that she wouldn't dare act on her urges, for fear of losing him."
    $ tracy.temporary_count = 0
  if player.has_item(transformation_potion):
    $ tracy.temporary_count = 0
    "The transformation potion could be a solution, but it would be risky.  You don't know her well enough to know what it might change her into.  Maybe it would transform her into the loving, heterosexual wife her husband wants, but somehow you doubt that things would work out that cleanly."
  if tracy.temporary_count == 1:
    $ tracy.temporary_count = 0
    "As much as you'd love to find a solution that would make her husband happy, you have no idea how to 'cure' her."
  call tracy_cure_options from _call_tracy_cure_options
  return

label tracy_cure_options:
  $ title = "Suggest a possible cure"
  menu:
    "Give her a love potion" if player.has_item(love_potion):
      player.c "Do you want to save your marriage, Tracy?"
      wt_image club_blackmail_visit_1_9
      tracy.c "Yes"
      player.c "Take this.  Give it to your husband.  Tell him to add it to a drink and then serve it to you."
      wt_image club_blackmail_visit_1_4
      tracy.c "What does it do?"
      player.c "After you drink it, you'll find it much easier to be the wife your husband wants."
      wt_image club_blackmail_visit_1_3
      tracy.c "I will?   Will I still want ... you know, will I still like girls?   It won't take that away from me, will it?"
      player.c "No, you'll still be you."
      wt_image club_blackmail_visit_1_9
      tracy.c "Then I don't see how ..."
      player.c "Are you sure you want to save your marriage?"
      wt_image club_blackmail_visit_1_2
      tracy.c "Yes. We have a daughter and, well ..."
      player.c "And he has a lot of money and you don't want to lose that?"
      wt_image club_blackmail_visit_1_13
      "She nods."
      player.c "Take the potion, Tracy.  Save your marriage."
      wt_image current_location.image
      "She takes it and leaves."
      add tags 'husband_message_love_potion_pending' to tracy
      $ tracy.change_status("minor_character")
      rem 1 love_potion from player notify
    "Write her a 'prescription'" if player.has_tag('das_access'):
      player.c "Do you want to save your marriage, Tracy?"
      wt_image club_blackmail_visit_1_9
      tracy.c "Yes"
      player.c "Take this.  It's a prescription.  Give it to your husband.  There's a shop downtown where he can get it filled.  Once he's filled it, he'll give you something to drink."
      wt_image club_blackmail_visit_1_4
      tracy.c "What does it do?"
      player.c "After you drink it, you'll find it much easier to be the wife your husband wants."
      wt_image club_blackmail_visit_1_3
      tracy.c "I will?  Will I still want ... you know, will I still like girls?  It won't take that away from me, will it?"
      player.c "No, you'll still be you."
      wt_image club_blackmail_visit_1_9
      tracy.c "Then I don't see how ..."
      player.c "Are you sure you want to save your marriage?"
      wt_image club_blackmail_visit_1_2
      tracy.c "Yes.  We have a daughter and, well ..."
      player.c "And he has a lot of money and you don't want to lose that?"
      wt_image club_blackmail_visit_1_13
      "She nods."
      player.c "Take the prescription, Tracy.  Save your marriage."
      wt_image current_location.image
      "She takes it and leaves."
      add tags 'husband_message_prescription_pending' to tracy
      $ tracy.change_status("minor_character")
    "Use the transformation potion on her anyway" if player.has_item(transformation_potion):
      player.c "You're stressed. Let me get you something to drink."
      wt_image club_blackmail_visit_1_9
      tracy.c "What is it?"
      player.c "An herbal tea."
      wt_image club_blackmail_visit_1_4
      tracy.c "Is it supposed to relax me?"
      player.c "Sort of. Drink up."
      wt_image club_blackmail_visit_1_19
      "The potion hits her quickly, worming its way into her brain, probing her memories and reactions.  She seems happy at first, as it explores her desire for other women ..."
      wt_image club_blackmail_visit_1_13
      "... then stressed as it explores the conflict her urges have brought into her marriage."
      wt_image club_blackmail_visit_1_19
      "Eventually, the potion hits upon the thoughts she's had, lying crying in her bedroom after fights with her husband, fleeting wishes that she didn't feel lust towards women."
      wt_image club_blackmail_visit_1_20
      "The potion amplifies those thoughts, expanding them, until the idea of lust is completely removed from her brain.  She no longer wants women, but in destroying it, any vestigial desire she may have ever had for her husband is destroyed as well.  She stares off into the distance, unseeing."
      player.c "How do you feel?"
      tracy.c "Okay.  A little ... flat."
      player.c "Can you look at me?"
      wt_image club_blackmail_visit_1_12
      tracy.c "Yes.  Why?"
      player.c "I wanted to make sure you wre okay.  You should go home to your husband.  Lie down and rest when you get there."
      tracy.c "Okay.  Did you help me?"
      if tracy.has_tag('sex_with_sam'):
        player.c "I hope so.  Would you like me to take to you to the Club before you go home?  There may be women there you haven't seen for a while?  Maybe even Sam?"
      else:
        player.c "I hope so.  Would you like me to take to you to the Club before you go home?  There may be women there you haven't seen for a while?"
      wt_image club_blackmail_visit_1_15
      "She shakes her head."
      tracy.c "No, why would I want to do that?"
      player.c "Perhaps after you're rested, you could get 'friendly' with your husband?"
      "She shrugs."
      tracy.c "If that's something he wants, I guess I could put up with it."
      wt_image current_location.image
      "After she leaves, you send a message to her husband.  Hopefully you'll hear back from him soon."
      player.c "{i}Tracy's been through a lot tonight. Let her rest when she gets home. By tomorrow, you should start to see a new her. Her situation was very challenging, and required an extreme and frankly very costly treatment. I'll require 700 to reimburse for the cost of materials I used.{i}"
      $ tracy.change_status("minor_character")
      add tags 'husband_message_transformation_potion_pending' 'transformed' to tracy
      rem 1 transformation_potion from player
    "Suggest an arrangement instead":
      player.c "You're right. It's not a cure you need. I think I have a better solution."
      call tracy_message_arrangement from _call_tracy_message_arrangement_1
    "Try to think of something else":
      jump menu_tracy_message_options
    "Tell her you can't help her":
      player.c "Will power."
      wt_image club_blackmail_visit_1_9
      tracy.c "Will power?"
      player.c "Yes, yours. I can't help you, Tracy. I doubt anyone can. But you can. You can save your marriage by exercising some will power and not acting on your urges."
      wt_image club_blackmail_visit_1_1
      tracy.c "Don't you think I've tried?"
      player.c "I have no idea.  If you have, then try harder."
      wt_image club_blackmail_visit_1_9
      tracy.c "That's your solution?"
      player.c "I wish I could do more for you and your husband, Tracy, but that's the only solution I see."
      wt_image club_blackmail_visit_1_15
      "She stares at you, as if she can't believe this is all you could come up with, then nods and leaves.  You're pretty sure you won't hear from her or her husband again."
      $ tracy.change_status("rejected")
  return

label tracy_message_arrangement:
  player.c "There may be a way to get you what you want while still making your husband happy."
  wt_image club_blackmail_visit_1_3
  tracy.c "Really?  How?"
  player.c "It'll require being dishonest with your husband."
  "Unsurprisingly considering how often it seems she's cheated on him, that doesn't seem to bother her, so you continue."
  player.c "We'll tell him that I'm working on your issue. When you visit, however, what I'll really do is let you have sex with women here at my house. Your husband will pay me my normal fees for the privilege of you getting a safe place to have your affair."
  player.c "For this to work, however, he'll have to believe that the training is making progress. That means you have to avoid giving him any indication that you're still interested in women."
  player.c "No making googly eyes at women when you're out in public, and definitely no fooling around on him other than during our weekly sessions."
  tracy.c "Absolutely! I can do that!! This sounds amazing. Would you really do that for me??"
  $ title = "Would you really do that?"
  menu:
    "Yes, let's do it":
      "Sometimes dishonesty is the best policy. This is the only path you can see that might allow both Tracy and her husband to be happy."
      "It does require you to accept continuing payments from her husband for the equivalent of running a flop house for his wife, but if it makes him feel better about his marriage, you're sure he won't mind paying you."
      wt_image club_blackmail_visit_1_11
      player.c "Yes, let's do this. I'll be in touch when it's time for your next 'session'."
      tracy.c "Thank you! Thank you so much! I'll be waiting eagerly to hear from you."
      "You're sure she will be. Just make sure you don't keep her waiting too long. This won't work if she backslides and fools around with him where she can get caught again."
      $ tracy.lose_her_countdown = 4
      $ tracy.change_status("minor_character")
      add tags 'arrangement' to tracy
      $ tracy.review_client_action = None
    "No, get out":
      player.c "No, of course I wouldn't. I just wanted to see how far you'd go to deceive your husband."
      wt_image club_blackmail_visit_1_2
      player.c "I can't help him or your marriage if you're that willing to lie to him and that eager run around behind his back. My advice to him will be to divorce you. My advice to you is get out."
      "She hangs her head in shame before breaking out in tears and leaving your house, sobbing."
      $ tracy.change_status("rejected")
  return

label tracy_husband_message:
    if tracy.has_tag('husband_message_transformation_potion_pending'):
        husband_tracy "{i}Sorry it took me a while to get back to you. 700 is a lot of money, but from what I've seen, it was worth it.{/i}"
        husband_tracy "{i}Tracy seems completely uninterested in other women. I've even taken to pointing out good looking women when they pass us in public, and she doesn't react in the least.{/i}"
        husband_tracy "{i}She's a little reserved in the bedroom these days, but she was never the most enthusiastic lover at the best of times. And because she's no longer running around behind my back, I always know where to find her when I'm feeling frisky.{/i}"
        husband_tracy "{i}I've never been happier with our marriage, and I'm so glad that Tracy is no longer afflicted by her perversion. I've sent you your expense reimbursement, as you requested.{/i}"
        husband_tracy "{i}If you ever need a reference, let me know.{/i}"
        "The money may not completely make up for the loss of the transformation potion, but at least you have a satisfied client."
        change player money by 700 notify
    else:
        if tracy.has_tag('husband_message_love_potion_pending'):
            husband_tracy "{i}I don't know what was in that potion you had me give Tracy, but whatever it was, it worked wonders!{/i}"
        elif tracy.has_tag('husband_message_prescription_pending'):
            husband_tracy "{i}I don't know what that prescription was you gave me or what other things that store was selling, but whatever it was, it worked wonders!{/i}"
        husband_tracy "{i}I've never seen Tracy like this, not even when we were first dating. She says she only has eyes for me now, and I believe her.{/i}"
        husband_tracy "{i}Every once in a while, when we're out in public, I'll still see her looking at pretty girls but the way she reacts now when I catch her, it's precious.{/i}"
        husband_tracy "{i}She swears she'd never again do anything to make me want to leave her and you know what? For the first time in years, I really believe her.{/i}"
        husband_tracy "{i}If you ever need a reference, let me know.{/i}"
    if player.has_tag('rep_needed'):
        "Since you're in need of a reputation boost now, you take him up on the offer to provide a reference."
        $ tracy.reference = 2
        rem tags 'rep_needed' from player
        change player reputation by 1 notify
    else:
        $ tracy.reference = 1
    rem action
    return

# Character Rejected
label tracy_rejected:
  sys "You may no longer accept this assignment."
  return

# Arrange Client Session
# OBJECT: Schedule Client Session
label tracy_calling:
    # Check if client has already been trained this week
    if not tracy.can_be_interacted:
        "You had an evening session with Tracy earlier this week. You need to wait until the weekend or next week for another session."
    else:
        $ tracy.training_session()
        call expandable_menu(tracy_session_date_menu) from _call_expandable_menu_65
        $ tracy.visit_count += 1
        $ tracy.lose_her_countdown = 4
        # this increases the minor client and similar fees received at the end of the week when major client fees are also collected
        $ player.extra_clients_fee_this_week += 25
        if tracy.has_tag('go_on_with_day'):
            wt_image current_location.image
            "You leave Tracy and her play partner to have their fun, while you continue with your day."
            rem tags 'go_on_with_day' from tracy
        else:
            change player energy by -energy_very_short notify
            end_day
    return

label tracy_calling_bring_own_date:
  call forced_movement(living_room) from _call_forced_movement_138
  summon tracy
  $ tracy.lesbian_outfit += 1
  # scroll 1 through 5
  if tracy.lesbian_outfit > 5:
    $ tracy.lesbian_outfit = 1
  if tracy.lesbian_outfit == 1:
    wt_image club_blackmail_lesbian_outfit_1_1
    "Tracy arrives just before her date rings the doorbell."
    tracy_lesbian_blonde "Hi!  Is Tracy here?"
    player.c "Come on in."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        wt_image club_blackmail_lesbian_outfit_1_2
        tracy.c "There you are!  You have no idea how much I've been looking forward to this."
        tracy_lesbian_blonde "Oh!  Me, too!!"
        wt_image club_blackmail_lesbian_outfit_1_3
        tracy.c "Can I kiss you?"
        tracy_lesbian_blonde "You'd better!"
        wt_image club_blackmail_lesbian_outfit_1_4
        "Neither of them seem to care - or even be aware - that you're watching them."
        wt_image club_blackmail_lesbian_outfit_1_5
        tracy.c "You have too many clothes on."
        wt_image club_blackmail_lesbian_outfit_1_6
        tracy_lesbian_blonde "So do you."
        wt_image club_blackmail_lesbian_outfit_1_7
        "Their attempts to fix the problem are slowed, somewhat ..."
        wt_image club_blackmail_lesbian_outfit_1_8
        "... by their fascination with each other's mouth ..."
        wt_image club_blackmail_lesbian_outfit_1_9
        "... but eventually they have it sorted out, except for a pair of seemingly unimportant knee-highs."
        wt_image club_blackmail_lesbian_outfit_1_10
        tracy_lesbian_blonde "I want you on your back."
        tracy.c "Yes, please."
        wt_image club_blackmail_lesbian_outfit_1_11
        "You can smell Tracy's arousal as soon as she spreads her legs."
        wt_image club_blackmail_lesbian_outfit_1_12
        "It's no wonder that her play partner is drawn to the aroma like a bee to a flower."
        wt_image club_blackmail_lesbian_outfit_1_13
        "The 'flower' looks like it's about to unleash a gusher of nectar into her partner's waiting mouth ..."
        tracy.c "ooooooo"
        wt_image club_blackmail_lesbian_outfit_1_14
        "... but her partner has other ideas, shifting position to bring her sex into contact with Tracy's ..."
        tracy.c "oooooo!!"
        wt_image club_blackmail_lesbian_outfit_1_15
        "... and getting the brunette off from the friction of their cunts rubbing together."
        tracy.c "ooooo  ....  OHHH!!"
        wt_image club_blackmail_lesbian_outfit_1_16
        "It seems that position was mostly for Tracy, as the blonde re-positions her sex over Tracy's waiting mouth ..."
        wt_image club_blackmail_lesbian_outfit_1_17
        "... and grinds it against Tracy's lips and tongue..."
        tracy_lesbian_blonde "mmmmmm"
        wt_image club_blackmail_lesbian_outfit_1_18
        "... until it's her turn to gush nectar."
        tracy_lesbian_blonde "mmmmm  ...  YEESSSS!!!!"
        wt_image club_blackmail_lesbian_outfit_1_19
        "You assumed they'd be finished, but it seems they're just getting started. Maybe there is something to that female endurance thing? Regardless, you've had a show and 'earned' the easiest 25 you'll ever make. You leave them to round two and make your way to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.lesbian_outfit == 2:
    wt_image club_blackmail_lesbian_outfit_2_1
    "Tracy's date arrives before she does."
    tracy_lesbian_asian "Hi?  Is Tracy here?"
    player.c "She isn't yet, but she'll be here soon.  Come in."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        wt_image club_blackmail_lesbian_outfit_2_2
        "The woman takes a seat, looking a little nervous."
        tracy_lesbian_asian "Maybe I should ..."
        player.c "There's Tracy now."
        wt_image club_blackmail_lesbian_outfit_2_3
        "A flustered looking Tracy blusters in and sits beside her friend."
        tracy.c "Sorry I'm late!"
        tracy_lesbian_asian "I was worried something had come up, or maybe you'd changed your mind?"
        tracy.c "Never!"
        wt_image club_blackmail_lesbian_outfit_2_4
        tracy_lesbian_asian "It'd be okay if you have."
        tracy.c "I haven't!  Have you?"
        "Tracy's friend lowers her eyes and shyly shakes her head."
        wt_image club_blackmail_lesbian_outfit_2_5
        tracy.c "Then you don't mind if I kiss you, do you?"
        "Again, her friend shyly shakes her head ..."
        wt_image club_blackmail_lesbian_outfit_2_6
        "... before opening her lips to receive ..."
        wt_image club_blackmail_lesbian_outfit_2_7
        "... and reciprocate Tracy's kiss."
        wt_image club_blackmail_lesbian_outfit_2_8
        tracy.c "I'm going to undress you now."
        "Her friend just nods ..."
        wt_image club_blackmail_lesbian_outfit_2_9
        "... as Tracy kisses her again, pulling down her top ..."
        wt_image club_blackmail_lesbian_outfit_2_10
        "... and fondling her breast."
        wt_image club_blackmail_lesbian_outfit_2_11
        tracy.c "I've been looking forward to seeing you naked."
        tracy_lesbian_asian "Have you really?"
        tracy.c "Yes, really.  Haven't you been wanting to see me naked?"
        wt_image club_blackmail_lesbian_outfit_2_12
        "Her friend's reply is as much a sigh as it is a word, as Tracy pulls down her top, baring her breasts."
        tracy_lesbian_asian "Yeesssss"
        tracy.c "Don't be shy, touch them."
        wt_image club_blackmail_lesbian_outfit_2_13
        "Tracy brings her friend's hand to her breast."
        tracy_lesbian_asian "Oohhh"
        tracy.c "Do they feel good?"
        wt_image club_blackmail_lesbian_outfit_2_14
        tracy_lesbian_asian "Yeessss"
        tracy.c "Would you like to do more?"
        "Unable to formulate a response, her friend only nods."
        wt_image club_blackmail_lesbian_outfit_2_15
        "Tracy spreads her legs and pulls her panties to the side."
        tracy.c "Come closer."
        wt_image club_blackmail_lesbian_outfit_2_16
        tracy.c "I know what you want to do.  It's okay.  It's what I want, too."
        wt_image club_blackmail_lesbian_outfit_2_17
        "It seems that is what her friend wants ..."
        tracy_lesbian_asian "mmmm"
        wt_image club_blackmail_lesbian_outfit_2_18
        "... and also what Tracy wants ..."
        tracy.c "ooooo  ...   oooooo"
        wt_image club_blackmail_lesbian_outfit_2_19
        "... very much."
        tracy.c "ooooo  ....  OHHH!!"
        wt_image club_blackmail_lesbian_outfit_2_20
        tracy.c "Mmmmm.  My turn."
        tracy_lesbian_asian "You don't have to ..."
        wt_image club_blackmail_lesbian_outfit_2_21
        tracy.c "I want to.  Don't you want me to do this?"
        tracy_lesbian_asian "Ohhh"
        wt_image club_blackmail_lesbian_outfit_2_22
        tracy.c "And this?"
        tracy_lesbian_asian "Ohhhh!"
        wt_image club_blackmail_lesbian_outfit_2_23
        tracy.c "And this?"
        tracy_lesbian_asian "OHH ... OHHHH!!!"
        wt_image club_blackmail_lesbian_outfit_2_24
        "They may be at this for a while.  You leave them to their mutual exploration and head to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.lesbian_outfit == 3:
    wt_image club_blackmail_lesbian_outfit_3_1
    "Today it's Tracy's turn to sit and wait for her date to arrive."
    wt_image club_blackmail_lesbian_outfit_3_2
    "When the other woman arrives, you let her in.  She looks much younger than Tracy, and seems a little uncertain about the situation."
    tracy_lesbian_brunette "Who's he?"
    tracy.c "Just a friend.  He's helping me out.  This is his house."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        wt_image club_blackmail_lesbian_outfit_3_3
        tracy_lesbian_brunette "He's staying?"
        tracy.c "He just likes to watch sometimes."
        tracy_lesbian_brunette "Is he some kinda perv?"
        wt_image club_blackmail_lesbian_outfit_3_4
        tracy.c "How about you look at me instead of him, okay?  I'm the one who's about to be kissing you, assuming that's still okay?"
        "She hesitates, then nods her head shyly."
        wt_image club_blackmail_lesbian_outfit_3_5
        "Tracy's lips seem to do the trick of getting the younger woman's full attention."
        wt_image club_blackmail_lesbian_outfit_3_6
        "Lost in the moment, they kiss with wild abandon ..."
        wt_image club_blackmail_lesbian_outfit_3_7
        "... and shed each other of their clothes."
        wt_image club_blackmail_lesbian_outfit_3_8
        "Tracy's date hasn't completely forgotten about you, however."
        wt_image club_blackmail_lesbian_outfit_3_9
        "She looks back at you as Tracy caresses her sex."
        wt_image club_blackmail_lesbian_outfit_3_10
        tracy_lesbian_brunette "Are you going to let him watch us fuck?"
        tracy.c "Just look at me, okay?  Don't worry about him."
        wt_image club_blackmail_lesbian_outfit_3_11
        "Tracy places her date's hand against her pussy ..."
        wt_image club_blackmail_lesbian_outfit_3_12
        "... and promptly loses all interest in anything other than the feel of the younger woman's fingers against her sex."
        tracy.c "ooooo"
        "Her date, on the other hand, keeps a close eye on you ..."
        wt_image club_blackmail_lesbian_outfit_3_13
        "... until Tracy directs her attention between her legs."
        wt_image club_blackmail_lesbian_outfit_3_14
        tracy.c "oooooo"
        "You seem to be forgotten again ..."
        wt_image club_blackmail_lesbian_outfit_3_15
        "... until Tracy's lover looks back at you and gives you a look that seems to say 'watch this' ..."
        wt_image club_blackmail_lesbian_outfit_3_16
        "... and promptly takes Tracy over the edge."
        tracy.c "ooooo  ....  OHHH!!"
        wt_image club_blackmail_lesbian_outfit_3_14
        tracy.c "Mmmm.  That was amazing.  My turn to make you feel good."
        wt_image club_blackmail_lesbian_outfit_3_17
        "Tracy licks her way from her date's nipples ..."
        tracy_lesbian_brunette "nnn"
        wt_image club_blackmail_lesbian_outfit_3_18
        "... to between her legs ..."
        tracy_lesbian_brunette "nnnn"
        wt_image club_blackmail_lesbian_outfit_3_19
        "... where she succeeds in her mission of reciprocity."
        tracy_lesbian_brunette "nnnnn ...  Aaaahhh!!"
        wt_image club_blackmail_lesbian_outfit_3_20
        "The two women engage in an extended make out session as they recover their energy ..."
        wt_image club_blackmail_lesbian_outfit_3_21
        "... before the younger woman looks up at you."
        tracy_lesbian_brunette "I still think he's a perv."
        wt_image club_blackmail_lesbian_outfit_3_22
        tracy.c "Turn around and I'll help you forget he's here."
        "They could be at this all night.  Time for you to go to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.lesbian_outfit == 4:
    wt_image club_blackmail_lesbian_outfit_4_1
    "Tracy's date rings your doorbell just as Tracy is rushing up the driveway."
    tracy_lesbian_black "Hi.  I'm looking for Tracy."
    wt_image club_blackmail_lesbian_outfit_4_2
    tracy.c "Here I am!"
    "She plants a big, sloppy kiss on the darker skinned woman."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        wt_image club_blackmail_lesbian_outfit_4_3
        "Tracy's hands are everywhere.  She seems in a frenzy to get both her and her date naked."
        wt_image club_blackmail_lesbian_outfit_4_4
        tracy_lesbian_black "Shit!  He's still here."
        wt_image club_blackmail_lesbian_outfit_4_5
        tracy.c "So am I, and I need your mouth on me so bad!"
        wt_image club_blackmail_lesbian_outfit_4_6
        "Tracy guides her date to the sofa ..."
        wt_image club_blackmail_lesbian_outfit_4_7
        "... and then guides her head between her legs."
        tracy.c "ooooo"
        wt_image club_blackmail_lesbian_outfit_4_8
        "Her date may not share her sense of urgency, but she's no doubt flattered by the intensity of Tracy's response ..."
        tracy.c "oooooo"
        wt_image club_blackmail_lesbian_outfit_4_9
        "... an intensity that soon reaches its climax."
        tracy.c "ooooo  ....  OHHH!!"
        wt_image club_blackmail_lesbian_outfit_4_10
        "The orgasm seems to have done nothing for Tracy's sense of urgency ..."
        tracy.c "Lie down.  I need to taste you!"
        wt_image club_blackmail_lesbian_outfit_4_11
        "... and she attacks her lover's pussy with the same enthusiasm that she received her lover's oral attention ..."
        tracy_lesbian_black "Oh!"
        wt_image club_blackmail_lesbian_outfit_4_12
        "... with similar results."
        tracy_lesbian_black "Oh!   Oh!   OH!!"
        wt_image club_blackmail_lesbian_outfit_4_13
        tracy.c "Mmmm.  Let's do that again."
        wt_image club_blackmail_lesbian_outfit_4_14
        "Her lover rolls her over, pinning Tracy beneath her."
        tracy_lesbian_black "Okay, but we're doing it slower this time."
        tracy.c "ooooo ... yeessss"
        "They may be at this for a while.  Time for you to go to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.lesbian_outfit == 5:
    wt_image club_blackmail_lesbian_outfit_5_1
    "Tracy arrives just before her date, a tomboy-ish looking young woman."
    tracy_lesbian_tomboi "Oh, hey!  Is Tracy in?"
    wt_image club_blackmail_lesbian_outfit_5_2
    "You usher her inside and Tracy races up to her."
    tracy.c "There you are!"
    tracy_lesbian_tomboi "Hey."
    tracy.c "Hey to you, too."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends eay)":
        tracy_lesbian_tomboi "So, um ... whadda you want to do?"
        wt_image club_blackmail_lesbian_outfit_5_16
        tracy.c "You"
        tracy_lesbian_tomboi "Me?"
        wt_image club_blackmail_lesbian_outfit_5_3
        tracy.c "Uh huh."
        "You have to hand it to Tracy.  She has eclectic taste in women ..."
        wt_image club_blackmail_lesbian_outfit_5_4
        "... and seems equally attracted to all of them."
        wt_image club_blackmail_lesbian_outfit_5_5
        "You're pretty sure it's not just an act to flatter her lovers ..."
        wt_image club_blackmail_lesbian_outfit_5_6
        "... she just loves to be touched by ..."
        wt_image club_blackmail_lesbian_outfit_5_7
        "... and to touch the female body, in all it's forms ..."
        wt_image club_blackmail_lesbian_outfit_5_8
        "... and all it's interesting places."
        tracy_lesbian_tomboi "Oh, fuck!"
        tracy.c "You like that?"
        wt_image club_blackmail_lesbian_outfit_5_17
        tracy_lesbian_tomboi "Uh huh"
        tracy.c "Cum in my mouth so I know you mean it."
        wt_image club_blackmail_lesbian_outfit_5_9
        tracy_lesbian_tomboi "Oh ... Oh ... Oh FUUCCKKK!!"
        wt_image club_blackmail_lesbian_outfit_5_10
        tracy.c "Lie down."
        tracy_lesbian_tomboi "Do you want me to ..."
        wt_image club_blackmail_lesbian_outfit_5_18
        tracy.c "Lie down first."
        wt_image club_blackmail_lesbian_outfit_5_19
        tracy.c "Get that butch tongue of yours right up into my cunt"
        wt_image club_blackmail_lesbian_outfit_5_20
        tracy.c "Deeper!"
        wt_image club_blackmail_lesbian_outfit_5_11
        tracy.c "ooooo"
        wt_image club_blackmail_lesbian_outfit_5_12
        tracy.c "ooooo  ....  OHHH!!"
        wt_image club_blackmail_lesbian_outfit_5_13
        "As Tracy gets off her, her date kisses her on the ass."
        tracy_lesbian_tomboi "That's kinda kinky, having a femme take charge."
        wt_image club_blackmail_lesbian_outfit_5_21
        tracy.c "Are you used to being on top?"
        tracy_lesbian_tomboi "Usually, yeah."
        wt_image club_blackmail_lesbian_outfit_5_21
        tracy.c "Then get on top of me."
        tracy_lesbian_tomboi "Doncha wanna rest?  Or talk?"
        wt_image club_blackmail_lesbian_outfit_5_23
        tracy.c "No.  Get your head between my legs."
        wt_image club_blackmail_lesbian_outfit_5_14
        "The younger woman may be on top, but Tracy's still in charge, and she has no intention of making this 'date' be about anything other than sex."
        wt_image club_blackmail_lesbian_outfit_5_15
        "You leave the two of them to their mutual cunnilingus.  It's going to be a long night for the young tomboy, but you're confident Tracy's tongue will make it a worthwhile one."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  call character_location_return(tracy) from _call_character_location_return_487
  return

label tracy_calling_becky_sue:
    add tags 'dated_becky_sue' to tracy
    wt_image tt_club_blackmail_1_1
    tracy.c "Thank you for doing this.  Your boyfriend told me you're not normally comfortable helping him in his work.  I'm glad you made an exception for me."
    if becky_sue.language == 0:
        becky_sue.c "That's okay.  I understand your husband's a big fucking asshole."
    elif becky_sue.language == 1:
        becky_sue.c "That's okay.  I understand your husband's a big damn asshole."
    else:
        becky_sue.c "That's okay.  I understand your husband's a big jerk."
    tracy.c "He can be, yes.  Your boyfriend's trying to help me, though."
    wt_image tt_club_blackmail_1_2
    if becky_sue.language == 0:
        becky_sue.c "Yeah, my boyfriend can be really fucking helpful, especially when it involves women getting naked.  But just so you know, I'm not into cheating on your fucking partner.  I've got a long history with that, and I just no longer think that's right."
    elif becky_sue.language == 1:
        becky_sue.c "Yeah, my boyfriend can be really damn helpful, especially when it involves women getting naked.  But just so you know, I'm not into cheating on your damn partner.  I've got a long history with that, and I just no longer think that's right."
    else:
        becky_sue.c "Yeah, my boyfriend can be really helpful, especially when it involves women getting naked.  But just so you know, I'm not into cheating on your partner.  I've got a long history with that, and I just no longer think that's right."
    wt_image tt_club_blackmail_1_3
    tracy.c "Does that mean you're not going to sleep with me?"
    becky_sue.c "I will, but just this once.  If you're having trouble with your husband, you need to either dump him or figure out a way to live without this.  One or the other has to be more important to you."
    wt_image tt_club_blackmail_1_4
    tracy.c "I know, but it's really hard.  You're lucky.  Your boyfriend doesn't mind you touching women."
    if becky_sue.language == 0:
        becky_sue.c "Yeah, lucky me.  My fucking perv boyfriend insists I do so."
    elif becky_sue.language == 1:
        becky_sue.c "Yeah, lucky me.  My damn perv boyfriend insists I do so."
    else:
        becky_sue.c "Yeah, lucky me.  My perv boyfriend insists I do so."
    wt_image tt_club_blackmail_1_5
    tracy.c "If you don't want to touch me, you could just lie down and let me touch you?"
    if becky_sue.has_tag('sleeping_with_friend'):
        becky_sue.c "You sound like a friend of mine."
    elif becky_sue.has_tag('likes_girls'):
        becky_sue.c "You're cute.  I don't mind touching you."
    else:
        becky_sue.c "I said I'd try to help you, so I should."
    wt_image tt_club_blackmail_1_6
    if becky_sue.language == 0:
        becky_sue.c "You've got it fucking bad, don't you?  You're soaked."
    elif becky_sue.language == 1:
        becky_sue.c "Hell, you've got it bad, don't you?  You're soaked."
    else:
        becky_sue.c "Wow, you've got it bad, don't you?  You're soaked."
    tracy.c "Uh huh ... please kiss me?"
    wt_image tt_club_blackmail_1_7
    "When she's finished kissing Tracy's mouth, [becky_sue.name] moves on to kiss her in a more intimate location."
    wt_image tt_club_blackmail_1_8
    "She seems to do a good job."
    tracy.c "ooooo  ....  OHHH!!"
    wt_image tt_club_blackmail_1_6
    tracy.c "Mmmm ... your turn."
    if becky_sue.has_tag('likes_girls'):
        wt_image tt_club_blackmail_1_9
        "[becky_sue.name] doesn't hesitate, straddling Tracy's face ..."
        wt_image tt_club_blackmail_1_10
        "... as Tracy does at least as good a job of pleasuring [becky_sue.name] and [becky_sue.name] did pleasuring her."
        becky_sue.c "OOHHHH FUUCCCKKKKK!!!"
    else:
        wt_image tt_club_blackmail_1_5
        becky_sue.c "I'm okay, thanks."
        tracy.c "Please?  Let me serve you."
        if becky_sue.has_tag('accepts_domestic_discipline'):
            becky_sue.c "You want to serve me?"
            tracy.c "Yes, Mistress.  Let me make you feel good."
            becky_sue.c "Mistress??"
            tracy.c "Mistress, Ma'am, Goddess ... I'll call you whatever you want.  Just please let me use my mouth to make you feel good."
            wt_image tt_club_blackmail_1_9
            becky_sue.c "I think I get why my boyfriend likes to put me in place sometimes."
            wt_image tt_club_blackmail_1_10
            "Tracy certainly seems happy to be in this place.  Soon, [becky_sue.name] is, too."
            becky_sue.c "OOHHHH FUUCCCKKKKK!!!"
        else:
            becky_sue.c "Seriously, it would feel like cheating, even with my boyfriend watching and wanting this.  I wanted to help you, that's all."
            tracy.c "You did, you seriously did."
    wt_image tt_club_blackmail_1_5
    if becky_sue.language == 0:
        becky_sue.c "You really fucking need this, don't you?  It's not just a little thing, it's fucking who you are.  Lose your husband if he can't accept that.  Like, fucking seriously."
    elif becky_sue.language == 1:
        becky_sue.c "You really damn well need this, don't you?  It's not just a little thing, it's who the hell you are.  Lose your damn husband if he can't accept that.  Like, seriously."
    else:
        becky_sue.c "You really need this, don't you?  It's not just a little thing, it's who you are.  Lose your husband if he can't accept that.  Like, seriously."
    tracy.c "I ... I'll think about it.  Can I see you again?  We can talk about it more then?"
    becky_sue.c "Nope.  This was a one time thing to help my guy.  He's the trainer, not me.  I'm just telling you what I think."
    "Tracy's disappointed, but [becky_sue.name] seems firm about making this a once only event.  She dispensed not only a great orgasm, but some pretty good advice, too.  You're pretty sure, however, that Tracy will only remember the first of those."
    $ becky_sue.lesbian_experience += 1
    return

label tracy_calling_elsa:
  call forced_movement(living_room) from _call_forced_movement_139
  summon tracy no_follows
  summon elsa no_follows
  $ elsa.training_session()
  $ tracy.elsa_outfit += 1
  # scroll 2 through 6 (1 is used only for first session)
  if tracy.elsa_outfit > 6:
    $ tracy.elsa_outfit = 2
  if tracy.elsa_outfit == 1:
    wt_image frigid_club_blackmail_1_1
    if tracy.has_tag('sex_with_elsa'):
      "Elsa and Tracy seem very happy to renew their acquaintance."
      tracy.c "I didn't think I'd get to see you again."
      elsa.c "Miss me?"
      wt_image frigid_club_blackmail_1_2
      tracy.c "Yes!  A lot."
      elsa.c "Good answer."
    else:
      if elsa.has_tag('girlfriend') or elsa.has_tag('hypno_girlfriend'):
        player.c "Tracy, this is my girlfriend, Elsa."
      else:
        player.c "Tracy, this is Elsa."
      tracy.c "Oh my gawd, you are so beautiful!"
      wt_image frigid_club_blackmail_1_2
      elsa.c "Thanks. You're pretty hot yourself."
    wt_image frigid_club_blackmail_1_3
    if elsa.has_tag('girlfriend') or elsa.has_tag('hypno_girlfriend'):
      elsa.c "It's so nice that you're working with my boyfriend. Did you know that before I met him, I didn't enjoy sex?"
    else:
      elsa.c "I think you've come to the right place for help. Did you know that before he trained me, I didn't enjoy sex?"
    tracy.c "Really?"
    wt_image frigid_club_blackmail_1_4
    elsa.c "Really.  So I would never have wanted to undress you ..."
    wt_image frigid_club_blackmail_1_5
    elsa.c "... or do this ..."
    tracy.c "oooo"
    wt_image frigid_club_blackmail_1_6
    elsa.c "... or this."
    tracy.c "Mmmm"
    wt_image frigid_club_blackmail_1_7
    if elsa.has_tag('girlfriend') or elsa.has_tag('hypno_girlfriend'):
      tracy.c "Thank goodness for your boyfriend."
    else:
      tracy.c "Thank goodness for your training."
    elsa.c "Thank goodness."
    if tracy.has_tag('sex_with_elsa'):
      "Apparently they still like each other."
    else:
      add tags 'sex_with_elsa' to tracy
      "Well, they seem to have hit it off just fine."
    $ tracy.elsa_outfit = 2
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        call tracy_calling_elsa_outfit_2 from _call_tracy_calling_elsa_outfit_2
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.elsa_outfit == 2:
    wt_image frigid_club_blackmail_1_3
    "Elsa seems as happy to see Tracy as Tracy is to see Elsa."
    elsa.c "Miss me?"
    tracy.c "Always."
    wt_image frigid_club_blackmail_1_2
    elsa.c "Not tired of me yet?"
    tracy.c "Hmmm.  I don't think so."
    wt_image frigid_club_blackmail_1_7
    elsa.c "Can I change that into a 'definitely not'?"
    tracy.c "Hmmm.  Probably."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        call tracy_calling_elsa_outfit_2 from _call_tracy_calling_elsa_outfit_2_1
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.elsa_outfit == 3:
    wt_image frigid_club_blackmail_2_1
    "Elsa is already in her lingerie when Tracy shows up. Tracy quickly strips to join her."
    tracy.c "This is pretty."
    elsa.c "Thank you."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        if elsa.has_tag('domme'):
          wt_image frigid_club_blackmail_2_21
          elsa.c "I'm glad you like my outfit, but I'm not impressed with yours at all."
          tracy.c "What's wrong?"
          wt_image frigid_club_blackmail_2_22
          elsa.c "For starters, you're wearing entirely too much clothes."
          tracy.c "I am?"
          wt_image frigid_club_blackmail_2_23
          "*SMACK*"
          tracy.c "OW!!"
          wt_image frigid_club_blackmail_2_24
          elsa.c "Yes, you are.  Am I going to have to take you over my knee or are you going to start trying harder to please me?"
          tracy.c "What can I do to please you?"
          wt_image frigid_club_blackmail_2_61
          elsa.c "You can start by removing my panties.  Do you like my ass?"
          tracy.c "Yes.  Very much."
          wt_image frigid_club_blackmail_2_25
          elsa.c "Good, because you're going to be spending the next little while worshipping it.  And no teeth today. The only thing you use your teeth for is to finish removing my panties, understood?"
          wt_image frigid_club_blackmail_2_26
          tracy.c "Yeth"
          elsa.c "Your tongue, on the other hand, is going to be very busy, starting with my asshole."
          wt_image frigid_club_blackmail_2_10
          tracy.c "Your asshole?"
          elsa.c "You heard me.  You're going to rim me.  Is that a problem?"
          wt_image frigid_club_blackmail_2_27
          "Tracy hesitates, but only for a moment."
          tracy.c "No"
          elsa.c "Good.  Do a good job on my butt hole and I might let your tongue taste my pussy later."
          wt_image frigid_club_blackmail_2_28
          "Tracy tentatively licks circles around Elsa's rosebud."
          elsa.c "Don't be shy.  You say you like girls.  This is your chance to get this girl off with your tongue."
          wt_image frigid_club_blackmail_2_29
          "Tracy begins to lick Elsa's rosebud itself."
          elsa.c "That's it.  Pretend my ass is a super tight cunt you're getting to taste for the first time."
          wt_image frigid_club_blackmail_2_30
          "More boldly, Tracy presses her tongue firmly against Elsa's rear entry, until the tip of it begins to penetrate her."
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_2_31
          elsa.c "Ooohhhh!  Yes, just like that!!  Fuck my ass with your tongue!  Oohhhhh!!"
          wt_image frigid_club_blackmail_2_32
          elsa.c "OOHHHHH!!!"
          "Elsa's body shakes all over as the orgasm hits her.  Tracy's body seems to shudder as well, as she brings your girlfriend to climax using her tongue in her ass."
          wt_image frigid_club_blackmail_2_7
          elsa.c "Mmmm.  Good girl.  Would you like a reward for bring so obedient? "
          tracy.c "Yes, please."
          wt_image frigid_club_blackmail_2_11
          elsa.c "Okay, you can use your tongue on my pussy now."
          tracy.c "Your pussy?"
          wt_image frigid_club_blackmail_2_33
          elsa.c "That's what you came here for, wasn't it?  To have sex with a woman?"
          tracy.c "Yes, but you just came and I'm ..."
          elsa.c "Horny?"
          tracy.c "Yes!"
          wt_image frigid_club_blackmail_2_34
          elsa.c "You have my permission to cum while you're eating me out, if you can."
          tracy.c "You really like being in charge, don't you?"
          elsa.c "Some days.  Today's one of those days."
          tracy.c "Can I at least play with myself while I'm eating you?"
          elsa.c "No.  Not yet anyway.  I want to see if you're horny enough to cum just from the taste of my pussy.  Enough chit chat.  When I told you I had plans for your tongue, talking wasn't one of the things I wanted you to use it for."
          wt_image frigid_club_blackmail_2_38
          elsa.c "Keep both hands on my ass so I know you're not playing with yourself.  And if you cum without touching yourself, groan loud enough for me to hear you despite your mouth being muffled by my pussy."
          wt_image frigid_club_blackmail_2_35
          "You decide to head to bed.  There's no point in waiting up for Elsa.  It sounds like she's going to be keeping Tracy busy for a while."
        elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
          wt_image frigid_club_blackmail_2_2
          "Tracy turns and looks at you."
          tracy.c "Does she want to be submissive today?"
          player.c "I don't know.  You'll need to ask her."
          wt_image frigid_club_blackmail_2_3
          tracy.c "Should I be telling you what to do today?"
          elsa.c "If that's what you want to do."
          wt_image frigid_club_blackmail_2_4
          tracy.c "I guess that's a clear enough answer.  Remove my panties."
          wt_image frigid_club_blackmail_2_5
          tracy.c "Do you like my ass?"
          elsa.c "Yes"
          wt_image frigid_club_blackmail_2_6
          tracy.c "I like your ass, too.  Bend over."
          wt_image frigid_club_blackmail_2_7
          tracy.c "It's very spankable."
          wt_image frigid_club_blackmail_2_8
          "*smack* ... *smack* ... *smack* ... *smack*"
          elsa.c "Ow ... Ow! ... Oww! ... OW!!"
          wt_image frigid_club_blackmail_2_7
          tracy.c "Sore now?"
          elsa.c "Yes!"
          wt_image frigid_club_blackmail_2_9
          tracy.c "Wet too?"
          elsa.c "Oooo ... yes!"
          wt_image frigid_club_blackmail_2_10
          if elsa.has_tag('girlfriend') or elsa.has_tag('hypno_girlfriend'):
            tracy.c "Your ass is kind of fuckable, too.  Does your boyfriend ever stick his dick inside it?"
          else:
            tracy.c "Your ass is kind of fuckable, too.  Does your friend ever stick his dick inside it?"
          # if elsa.has_tag('anal')
          if elsa.anal_count > 0:
            elsa.c "Yes"
            tracy.c "I bet he does. I bet you cum when he sticks it up there, too, don't you, slut?"
            if elsa.rough_trigger_count > 2:
              elsa.c "Sometimes, especially if he spanks me."
              tracy.c "Cumming from being spanked with a cock up your ass?  You are a submissive slut, aren't you?"
              elsa.c "Sometimes"
              tracy.c "This conversation is making you wetter and wetter, isn't it, slut?"
            else:
              elsa.c "No"
              tracy.c "No?  You take it up the ass even though you don't like it?  You are a submissive slut, aren't you?"
              elsa.c "Sometimes"
              tracy.c "This conversation is making you wetter and wetter, isn't it, slut?"
          else:
            "Elsa shakes her head."
            tracy.c "No?  Guess you aren't as much of a submissive slut as I thought you were.  Although me talking about you taking it up the ass is getting you wetter and wetter, isn't it, slut?"
          wt_image frigid_club_blackmail_2_11
          elsa.c "That's your fingers."
          wt_image frigid_club_blackmail_2_12
          tracy.c "Just my fingers, huh?  In that case, I guess you're not submissive enough to cum when I bite you on your well spanked ass?"
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_2_13
          elsa.c "OOHHHHH!!!"
          tracy.c "Hmmm, seems you are that submissive after all."
          wt_image frigid_club_blackmail_2_14
          tracy.c "Don't worry, I have the perfect place for a submissive bi-sexual woman.  Right here kneeling between my legs while your boyfriend watches you eat me out."
          wt_image frigid_club_blackmail_2_15
          "Tracy smiles and sighs contentedly as Elsa licks her."
          tracy.c "Mmmmm"
          wt_image frigid_club_blackmail_2_16
          "[elsa.name] glances back, every once in a while, to where you're seated watching them."
          wt_image frigid_club_blackmail_2_17
          tracy.c "Don't look at him.  He sees you licking my cunt, slut.  Keep your attention on making me cum."
          wt_image frigid_club_blackmail_2_18
          "Elsa gives Tracy's sex her full attention."
          wt_image frigid_club_blackmail_2_19
          tracy.c "ooooo ... Yes, just like that.  Right on my clit ..."
          wt_image frigid_club_blackmail_2_20
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_2_17
          tracy.c "Don't try and get up.  You're staying right there until you give me at least one more orgasm than you did on my last visit."
          wt_image frigid_club_blackmail_2_14
          "You decide to head to bed.  There's no point in waiting up for Elsa.  She's going to be a while."
        else:
          wt_image frigid_club_blackmail_2_36
          elsa.c "I like yours, too, but I think you'd look even better with nothing on."
          wt_image frigid_club_blackmail_2_37
          tracy.c "Funny.  I was just thinking the same thing about you."
          elsa.c "You're not tired of seeing me naked?"
          wt_image frigid_club_blackmail_2_25
          tracy.c "Let's check ..."
          tracy.c "Nope.  Definitely not tired."
          elsa.c "Are you sure?  Maybe you should take a closer look?"
          wt_image frigid_club_blackmail_2_12
          tracy.c "Good idea.  Let me see ..."
          wt_image frigid_club_blackmail_2_11
          tracy.c "Mmmm ... this still looks good."
          elsa.c "Oohhh ...  How good?"
          tracy.c "Are you asking me if you look good enough to eat?"
          elsa.c "Umm, yeah,  Do I?"
          wt_image frigid_club_blackmail_2_38
          tracy.c "Definitely."
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_2_35
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_2_33
          tracy.c "Wow!  You're hair-triggered today."
          elsa.c "I guess I was looking forward to seeing you.  You should be flattered."
          tracy.c "I am!"
          elsa.c "Think I can get you off as quickly?"
          tracy.c "I can't wait to find out."
          wt_image frigid_club_blackmail_2_14
          "Elsa kneels between Tracy's legs and begins to lick her ..."
          wt_image frigid_club_blackmail_2_15
          "... as Tracy smiles and sighs contentedly."
          tracy.c "Mmmmm"
          wt_image frigid_club_blackmail_2_19
          "Elsa quickly converts those sighs into moans ..."
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_2_18
          "... and while she has to work a little harder than Tracy did ..."
          tracy.c "oooooo"
          wt_image frigid_club_blackmail_2_20
          "... it's not long before she takes Tracy over the edge."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_2_39
          tracy.c "Now that the edge is off, want to try that again?"
          elsa.c "Absolutely.  This time, let's see how long we can keep each other on the brink without actually cumming?"
          tracy.c "Okay.  Lie down."
          "You decide to head to bed.  There's no point in waiting up for Elsa.  It sounds lie she's going to be a while."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.elsa_outfit == 4:
    wt_image frigid_club_blackmail_1_3
    "No words are needed as Elsa and Tracy embrace on the sofa and undress each other."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        if elsa.has_tag('domme'):
          wt_image frigid_club_blackmail_1_26
          "Elsa traps Tracy's hands in her top and grins."
          elsa.c "Ready to be a good girl for me?"
          wt_image frigid_club_blackmail_1_27
          tracy.c "Yes"
          "Elsa leans in and Tracy opens her mouth, expecting a kiss ..."
          wt_image frigid_club_blackmail_1_28
          "... only to be shoved roughly onto her back."
          wt_image frigid_club_blackmail_1_45
          elsa.c "Good, because I have something very important you need to do for me."
          tracy.c "What?"
          wt_image frigid_club_blackmail_1_29
          elsa.c "Cum in my mouth."
          "Tracy moans as Elsa spits on her cunt ..."
          tracy.c "oooo"
          wt_image frigid_club_blackmail_1_30
          "... and moans again, more loudly, as Elsa licks and teases her labia, circling closer and closer to her cllt ..."
          tracy.c "oooooo"
          wt_image frigid_club_blackmail_1_31
          "... before complying with Elsa's demand as Elsa's tongue flicks back and forth across her engorged clit."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_1_48
          elsa.c "Mmmm.  Good girl.  You earned a reward."
          wt_image frigid_club_blackmail_1_23
          "Tracy moans again as Elsa licks her way up her body to her neck."
          wt_image frigid_club_blackmail_1_6
          tracy.c "oooo ... what is it?"
          elsa.c "You get to taste my pussy."
          wt_image frigid_club_blackmail_1_32
          "Tracy quickly scrambles between Elsa's legs to claim her reward."
          wt_image frigid_club_blackmail_1_52
          "From her efforts, it seems Tracy is trying to make Elsa cum as quickly as Elsa made her cum ..."
          wt_image frigid_club_blackmail_1_33
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_1_43
          "... and she very nearly succeeds."
          wt_image frigid_club_blackmail_1_34
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_1_42
          tracy.c "Now I have a reward for you, Madame Domme."
          elsa.c "Mistress.  I prefer to be called Mistress."
          wt_image frigid_club_blackmail_1_18
          tracy.c "Whatever.  Don't you want to know what it is, 'Mistress'?"
          elsa.c "Okay, what is it?"
          wt_image frigid_club_blackmail_1_35
          tracy.c "A pool of your cum in my mouth for you to taste."
          "Tracy leans down and kisses Elsa ..."
          wt_image frigid_club_blackmail_1_36
          "... letting Elsa's cum roll down her tongue and into Elsa's mouth.  The message is clear: I'll let you take control, but don't forget that I can take charge, too.  Elsa seems fine with that.  You leave the two of them to figure out who's going to be on top next and head to bed."
        elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
          tracy.c "What do you want to do today?"
          elsa.c "Whatever you want."
          wt_image frigid_club_blackmail_1_19
          "Tracy squeezes Elsa's breast as Elsa close her eyes."
          tracy.c "Whatever I want?"
          elsa.c "Mmmm.  Yes."
          wt_image frigid_club_blackmail_1_23
          tracy.c "Lick your way to my cunt, but take your time getting there."
          "Elsa starts at Tracy's nipples ..."
          wt_image frigid_club_blackmail_1_37
          "... circling and tracing them with the tip of her tongue ..."
          tracy.c "oooo"
          wt_image frigid_club_blackmail_1_38
          "... before moving to her legs ..."
          wt_image frigid_club_blackmail_1_39
          "... and down her thigh ..."
          wt_image frigid_club_blackmail_1_30
          "... where she reaches her intended destination."
          wt_image frigid_club_blackmail_1_40
          "Tracy holds her head in place, making sure Elsa knows she's supposed to stay at this destination ..."
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_1_31
          "... until Tracy reaches hers."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_1_41
          elsa.c "Did that feel good?"
          tracy.c "Mmmm.  Yes."
          elsa.c "Is there anything else I can do for you?"
          tracy.c "Are you really willing to do anything for me?"
          elsa.c "If it will make you feel good, yes.  Just tell me what you want."
          wt_image frigid_club_blackmail_1_42
          tracy.c "In that case, lay back and spread your legs ..."
          wt_image frigid_club_blackmail_1_43
          tracy.c "... because what I want more than anything else in the world right now is to taste you."
          wt_image frigid_club_blackmail_1_33
          "It wasn't what Elsa was expecting ..."
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_1_34
          "... but like the good girl she is, she soon gives Tracy plenty to taste."
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_1_18
          "Tracy grins at [elsa.name] as the blonde woman recovers from having been of 'service'."
          elsa.c "Mmmmm, is there anything else I can do for you?"
          wt_image frigid_club_blackmail_1_42
          tracy.c "Still eager to please me?"
          elsa.c "Even more eager."
          wt_image frigid_club_blackmail_1_35
          tracy.c "In that case, lie here and be my fuck doll for the night."
          wt_image frigid_club_blackmail_1_36
          "You leave Tracy to make out with your girlfriend / her fuck doll for the night, and head to bed."
        else:
          wt_image frigid_club_blackmail_1_4
          "In lieu of words, there's only the sound of clothing being unhooked ..."
          wt_image frigid_club_blackmail_1_44
          "... and removed."
          wt_image frigid_club_blackmail_1_28
          "Who needs words, anyway, when eyes can say so much?"
          wt_image frigid_club_blackmail_1_46
          "And mouths have other, more interesting ways of communicating."
          tracy.c "oooo"
          wt_image frigid_club_blackmail_1_47
          "Even breathing sends a message, as it becomes faster and shallower ..."
          wt_image frigid_club_blackmail_1_48
          "... and then seems to stop entirely, along with time itself, in anticipation of a touch that is so close ... so close ..."
          wt_image frigid_club_blackmail_1_30
          "... and then finally here ..."
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_1_49
          "... as their worlds shrink to a single point of contact, where soft wet flesh meets soft wet flesh ..."
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_1_31
          "... and the only sounds are of licking and lapping and moaning and finally, intense, almost unbearable pleasure."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_1_50
          "For a moment everything is smiling and the catching of breath ..."
          wt_image frigid_club_blackmail_1_36
          "... then positions are reversed ..."
          wt_image frigid_club_blackmail_1_43
          "... and their worlds are again reduced to a single point of contact, where soft wet flesh meets soft wet flesh ..."
          wt_image frigid_club_blackmail_1_33
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_1_52
          "... and the only sounds are of licking and lapping and moaning and finally, intense, almost unbearable pleasure."
          wt_image frigid_club_blackmail_1_34
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_1_18
          "Bringing us back to a moment where everything is smiling and the catching of breath ..."
          wt_image frigid_club_blackmail_1_35
          "... before the cycle begins again.  This may go on a while.  Quietly, you head to bed, being careful not to interrupt the silence."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.elsa_outfit == 5:
    if elsa.has_tag('domme') and elsa.has_item(dildo):
      wt_image frigid_club_blackmail_2_21
      elsa.c "I have something for you."
      wt_image frigid_club_blackmail_2_60
      tracy.c "For me?"
      elsa.c "Well, something for you to use on me."
    elif elsa.has_tag('domme'):
      jump tracy_calling_elsa
    elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
      wt_image frigid_club_blackmail_2_3
      tracy.c "I brought something for you."
      elsa.c "For me?"
      wt_image frigid_club_blackmail_2_60
      tracy.c "Mm hmmm.  Lie down and spread your legs and I'll show you where it goes."
    else:
      wt_image frigid_club_blackmail_2_1
      tracy.c "I brought something for you."
      elsa.c "For me?"
      wt_image frigid_club_blackmail_2_60
      tracy.c "Mm hmmm.  Lie down and I'll show you where it goes."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        if elsa.has_tag('domme') and elsa.has_item(dildo):
          wt_image frigid_club_blackmail_2_40
          elsa.c "I know you like to have your mouth on me, but you'll need to make do with getting the toy wet for me, until I decide you can use it somewhere else."
          "Tracy dutifully licks the head of the dildo Elsa givs her, getting as close to Elsa's pussy as she can while doing so."
          wt_image frigid_club_blackmail_2_41
          elsa.c "Once it's good and wet, put it inside me  ...  Mmmmm, now fuck me with it."
          wt_image frigid_club_blackmail_2_42
          "An attentive Tracy begins stroking the toy in and out of Elsa's rapidly lubricating pussy."
          elsa.c "Oohhh ... You can use your mouth on me now, but not on my pussy yet."
          wt_image frigid_club_blackmail_2_43
          "Tracy licks the inside of Elsa's leg while continuing to fuck her with the dildo."
          elsa.c "Ooohhhhh ... Okay, you can lick my cunt now."
          wt_image frigid_club_blackmail_2_44
          "Tracy smiles and gives Elsa's sex one quick lick ..."
          wt_image frigid_club_blackmail_2_45
          "... before clamping her mouth down on Elsa's clit, sending her squealing over the edge."
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_2_44
          tracy.c "Did you like that, Missy Domme?"
          wt_image frigid_club_blackmail_2_42
          elsa.c "The term is 'Mistress'.  Am I going to have to spank you so you remember?"
          wt_image frigid_club_blackmail_1_18
          tracy.c "Mmmm.  Threatening me with a good time, are you?  Do your worst, Missy Domme."
          wt_image frigid_club_blackmail_1_35
          "You might have been tempted to stick around and watch, but they both break out giggling like schoolgirls as they kiss.  You expect that Tracy is going to end up across Elsa's lap before the night is out, but you have no idea how long that may take and the two of them are in no rush to do anything but kiss each other at the moment.  Better simply to head to bed."
        elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
          wt_image frigid_club_blackmail_2_40
          "Tracy produces a dildo from her bag and licks it wet."
          tracy.c "Do you ever use one of these?"
          if elsa.has_item(dildo):
            elsa.c "Sometimes"
            wt_image frigid_club_blackmail_2_41
            tracy.c "And have you ever had someone else use a dildo on you?"
            wt_image frigid_club_blackmail_2_42
            if elsa.fuck_machine_count > 0:
              elsa.c "Does being fucked by a machine count?"
              tracy.c "Kinky.  Hopefully you'll prefer my personal touch"
            else:
              elsa.c "No"
              tracy.c "You're in for a treat, then.  It's a whole different experience when someone else is fucking you with it, compared to when you're fucking yourself.  You have a lot less control, which I think you'll like."
            wt_image frigid_club_blackmail_2_41
            "As Tracy moves the toy in and out, [elsa.name] groans."
          else:
            elsa.c "No"
            wt_image frigid_club_blackmail_2_41
            tracy.c "Your boyfriend hasn't bought you one?  Maybe he'll get you one for your birthday.  Or maybe he doesn't want the competition??  Well, you're in for a treat.  This dick won't get soft, no matter how long I fuck you with it."
            "Tracy slowly inserts the dildo into Elsa, then begins to move it in and out as [elsa.name] groans."
          wt_image frigid_club_blackmail_2_42
          elsa.c "nnnnn"
          tracy.c "Not fully wet yet, are you?"
          "Elsa shakes her head."
          wt_image frigid_club_blackmail_2_46
          tracy.c "Maybe this will help?"
          "Tracy lets her drool roll off the tip of her tongue and drip down Elsa's sex."
          wt_image frigid_club_blackmail_2_47
          elsa.c "Ohh"
          "Elsa is getting wetter, but that has more to do with the dildo that Tracy is slowly working in and out of her than it does with the spittle that Tracy continues to drizzle over the dildo and Elsa's sex ..."
          wt_image frigid_club_blackmail_2_48
          elsa.c "Oohhh"
          "... and when Tracy replaces the spit from her tongue with direct contact from her tongue, Elsa gets wetter still."
          wt_image frigid_club_blackmail_2_49
          "In fact, Elsa starts moaning and trembling to the point that her climax seems imminent ..."
          elsa.c "Ooohhhhh"
          wt_image frigid_club_blackmail_2_42
          "... when Tracy pulls her tongue away."
          elsa.c "Oh!"
          tracy.c "Nah nah nah ... No cumming until I'm finished having my fun and I'm not done, yet."
          wt_image frigid_club_blackmail_2_41
          "Tracy continues to fuck Elsa, using just the dildo ... thrusting it in and out, first faster, then slower ... varying the pace to keep Elsa aroused, but unable to adjust enough to reach climax."
          elsa.c "Oohhh"
          wt_image frigid_club_blackmail_2_42
          "Then Elsa surprises Tracy and you, and maybe even herself, by begging for release."
          elsa.c "Oh, please!  Let me cum???  Please, please, let me cum!!"
          tracy.c "Wow!  Do you need it that bad?"
          elsa.c "Yes, please!  Please, let me cum!!"
          wt_image frigid_club_blackmail_2_44
          tracy.c "Well, okay, since you asked so nicely."
          wt_image frigid_club_blackmail_2_49
          "Tracy smiles and gives Elsa's sex a quick lick ..."
          wt_image frigid_club_blackmail_2_45
          "... then clamps her mouth down on Elsa's clit, sending her squealing over the edge."
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_2_41
          elsa.c "Thank you.  Thank you for that."
          tracy.c "Feeling grateful that I let you cum?"
          wt_image frigid_club_blackmail_2_42
          elsa.c "Very"
          wt_image frigid_club_blackmail_1_42
          tracy.c "Ready to do something to show me how grateful you are?"
          elsa.c "Absolutely"
          wt_image frigid_club_blackmail_1_18
          tracy.c "It's going to take you a while."
          elsa.c "That's okay.  As long as you enjoy it."
          wt_image frigid_club_blackmail_1_35
          tracy.c "Oh, I will.  Get your strength back, then we'll begin."
          wt_image frigid_club_blackmail_1_40
          "Sounds like Elsa's going to be busy a while.  You head to bed without her."
        else:
          wt_image frigid_club_blackmail_2_37
          elsa.c "Where it goes?  What do you mean?"
          tracy.c "Nah nah nah, I'm not going to ruin the surprise.  And quit trying to distract me by undressing me.  Sit down and spread your legs if you want your surprise."
          wt_image frigid_club_blackmail_2_40
          elsa.c "What are you doing down there?  I can't see."
          tracy.c "That's kind of the point."
          "Elsa can't see, but you can.  You watch with interest as Tracy wets the head of the dildo she pulls out of her handbag ..."
          wt_image frigid_club_blackmail_2_41
          "... and slowly inserts it into Elsa."
          elsa.c "Oh!"
          tracy.c "Like it?"
          wt_image frigid_club_blackmail_2_42
          elsa.c "Umm?"
          tracy.c "Need a little more lubrication?"
          elsa.c "I think so."
          wt_image frigid_club_blackmail_2_46
          tracy.c "Maybe this will help?"
          "Tracy lets her drool roll off the tip of her tongue and drip down Elsa's sex."
          wt_image frigid_club_blackmail_2_47
          elsa.c "Ohh"
          "Elsa is getting wetter, but that has more to do with the dildo that Tracy is slowly working in and out of her than it does with the spittle that Tracy continues to drizzle over the dildo and Elsa's sex ..."
          wt_image frigid_club_blackmail_2_48
          elsa.c "Oohhh"
          "... and when Tracy replaces the spit from her tongue with direct contact from her tongue, Elsa gets wetter still."
          wt_image frigid_club_blackmail_2_49
          "Before long, Elsa starts trembling all over ..."
          elsa.c "Ooohhhhh"
          wt_image frigid_club_blackmail_2_44
          "... as a smiling Tracy redoubles her attention to Elsa's clit, sending her over the edge."
          elsa.c "OOHHHHH!!!"
          wt_image frigid_club_blackmail_2_41
          tracy.c "Did you like your surprise?"
          wt_image frigid_club_blackmail_2_42
          elsa.c "Mmmmm, did I ever.  And here I forgot to get anything for you.  All I have with me are my fingers, and my lips, and my tongue ..."
          wt_image frigid_club_blackmail_1_18
          tracy.c "That's all, huh?"
          elsa.c "Uh huh"
          tracy.c "So I guess I'm going to have to make do with those?"
          elsa.c "I'm afraid so."
          wt_image frigid_club_blackmail_1_42
          tracy.c "Well, I don't know.  I suppose you may be able to use those to surprise me."
          elsa.c "Hmmm, I may be able to manage that."
          wt_image frigid_club_blackmail_1_35
          "The two of them start giggling together like school girls, then make out.  They're going to be a while.  You head to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.elsa_outfit == 6:
    if elsa.has_tag('domme'):
      wt_image frigid_club_blackmail_2_21
      elsa.c "I have something for you."
      tracy.c "Do you really?"
      wt_image frigid_club_blackmail_2_60
      elsa.c "I really do. Lie down and I'll show you."
    elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
      wt_image frigid_club_blackmail_2_3
      tracy.c "I brought another toy today."
      wt_image frigid_club_blackmail_2_60
      elsa.c "For me?"
      tracy.c "Sort of. It's something for you to use on me."
    else:
      wt_image frigid_club_blackmail_2_1
      elsa.c "Guess what I have."
      tracy.c "A smoking hot body?"
      wt_image frigid_club_blackmail_2_60
      elsa.c "Well, thank you very much.  I'm glad you think so, but I meant guess what I have to use on you."
      tracy.c "I'm still hoping the answer is your smoking hot body."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        if elsa.has_tag('domme'):
          wt_image frigid_club_blackmail_2_55
          elsa.c "Wet yet?"
          wt_image frigid_club_blackmail_2_53
          tracy.c "You can see I am."
          elsa.c "I just want to hear you admit it."
          tracy.c "Yes, I'm wet."
          wt_image frigid_club_blackmail_2_50
          elsa.c "Wet for me?"
          tracy.c "Yes"
          elsa.c "Say, 'Yes, Mistress.'"
          wt_image frigid_club_blackmail_2_53
          tracy.c "Are you onto that again?"
          wt_image frigid_club_blackmail_2_51
          elsa.c "Tsk tsk, such an attitude!  And after I brought this lovely present for you."
          "Elsa slides the vibrator inside Tracy and turns it on, then follows up by licking Tracy's clit ... *bzzzzzzzzzzz*"
          tracy.c "Oh!  OHH!"
          wt_image frigid_club_blackmail_2_52
          "*bzzzzzzzzzzz*"
          tracy.c "ooooo"
          elsa.c "Mmmm, you like what Mistress is doing for you now, don't you?"
          wt_image frigid_club_blackmail_2_50
          elsa.c "Thing is though, I can stop at any time."
          "Elsa removes her mouth and the dildo."
          tracy.c "Oh!"
          wt_image frigid_club_blackmail_2_53
          tracy.c "Wh ... what is it?  Why'd you stop?"
          elsa.c "Do you want me to continue?"
          tracy.c "Yes!"
          elsa.c "I want you to call me Mistress."
          tracy.c "Elsa, I ..."
          wt_image frigid_club_blackmail_2_54
          elsa.c "Don't think you want to?  Let me remind you of the reward for obedience."
          "Elsa returns the vibrator and her mouth to Tracy's sex ... *bzzzz*"
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_2_55
          elsa.c "Ooops, you're getting too worked up.  I'd better cool you down."
          "Elsa removes the vibrator and spits on Tracy's hot, throbbing sex as Tracy groans in frustration."
          tracy.c "Arrr!"
          wt_image frigid_club_blackmail_2_51
          elsa.c "I can do this all day, but do you know what you can't do?  You can't cum if I keep pulling the stimulation away right before you reach that sweet spot."
          "*bzzzzzzzzzzz*"
          wt_image frigid_club_blackmail_2_56
          tracy.c "nnnnn"
          "Tracy bites her tongue and tries to ignore the pleasure building up inside her, as she knows ..."
          wt_image frigid_club_blackmail_2_50
          "... Elsa's just going to pull it away again."
          tracy.c "Arrrr!!"
          elsa.c "That must be frustrating.  If only there was some way you could convince me to keep the vibrator inside you and to keep my mouth on your clit?"
          wt_image frigid_club_blackmail_2_53
          "Tracy looks angry, and for a moment you think she's going to snap at Elsa ..."
          wt_image frigid_club_blackmail_2_56
          "... then she's back to trying not to enjoy the sensation of Elsa and the dildo between her legs too much ... *bzzzzzzzzzzz*"
          tracy.c "nnnnnn"
          wt_image frigid_club_blackmail_2_50
          "... and finally she just ends up desperate."
          tracy.c "Arrr!!  Elsa, what do you want???"
          if elsa.has_item(dildo):
            elsa.c "I told you what I want. I want you to call me 'Mistress'. Not Madame Domme. Definitely not Missy Domme. Call me Mistress and say it like you mean it."
          else:
            elsa.c "I told you what I want. I want you to call me 'Mistress'. Call me Mistress and say it like you mean it."
          wt_image frigid_club_blackmail_2_53
          tracy.c "Okay, Mistress, you win."
          elsa.c "You're going to be obedient the rest of tonight, Tracy?"
          tracy.c "Yes, Mistress."
          elsa.c "That means no back talking, no glib remarks, and no trying to take back control."
          tracy.c "Yes, Mistress.  You're in charge tonight.  Only you."
          wt_image frigid_club_blackmail_2_54
          elsa.c "Good girl. I'm going to let you cum now, but you need to thank me afterwards or it's the last orgasm you get from me."
          tracy.c "Yes, Mistress."
          wt_image frigid_club_blackmail_2_57
          "*bzzzzzzzzzzz*"
          tracy.c "ooooo .... OHHH!!  THANK YOU, MISTRESS!!"
          wt_image frigid_club_blackmail_2_39
          tracy.c "That was ..."
          wt_image frigid_club_blackmail_2_34
          elsa.c "Shush.  You don't get to speak for the rest of the night, except to say 'Yes, Mistress'.  Understood?"
          tracy.c "Yes, Mistress."
          wt_image frigid_club_blackmail_2_38
          "It's going to be a long night for Tracy. You head to bed."
        elif elsa.test('submission', 79) and elsa.has_tag('submissive_with_tracy'):
          wt_image frigid_club_blackmail_2_6
          tracy.c "Get out of these clothes."
          wt_image frigid_club_blackmail_2_14
          tracy.c "Now kneel in front of me."
          "Elsa gets into position on the floor in front of Tracy.  As soon as Tracy spreads her legs, Elsa leans in and starts licking."
          wt_image frigid_club_blackmail_2_15
          tracy.c "Mmmm ... that's nice."
          wt_image frigid_club_blackmail_2_58
          tracy.c "Here.  This is what I brought you.  Use this, too."
          "Tracy hands Elsa a vibrator.  Without stopping her licking, Elsa slides it inside Tracy ..."
          wt_image frigid_club_blackmail_2_59
          "... and turns it on ... *bzzzzzzzzzzz*"
          tracy.c "Oh wow!  That feels amazing!!  Keep doing exactly that, with your tongue and the vibrator ... ooooo"
          wt_image frigid_club_blackmail_2_52
          "*bzzzzzzzzzzz*"
          wt_image frigid_club_blackmail_2_57
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_2_50
          elsa.c "You liked that."
          wt_image frigid_club_blackmail_2_53
          tracy.c "Mmmm.  You know what else I like?"
          elsa.c "What?"
          wt_image frigid_club_blackmail_2_51
          tracy.c "I like that with the vibrator doing most of the work, you can stay between my legs for the whole night without getting tired.  Can't you?"
          elsa.c "Yes"
          wt_image frigid_club_blackmail_2_59
          "*bzzzzzzzzzzz* ... Elsa's going to be here a while. You head to bed to the sounds of what is likely to be only the second of many orgasms for Tracy tonight."
          tracy.c "ooooo  ....  OHHH!!"
        else:
          wt_image frigid_club_blackmail_2_14
          elsa.c "Spread your legs and I'll show you."
          "Tracy undresses at lightning speed and offers her sex to Elsa, who playfully licks it."
          wt_image frigid_club_blackmail_2_15
          elsa.c "Ready for your surprise?"
          tracy.c "Mmmmm,  I'm happy just like this."
          wt_image frigid_club_blackmail_2_51
          elsa.c "So you're not interested in this?"
          "Without stopping her licking, Elsa slides a vibrator inside Tracy ..."
          tracy.c "Oh!"
          wt_image frigid_club_blackmail_2_52
          "... and turns it on ... *bzzzzzzzzzzz*"
          tracy.c "ooooo"
          wt_image frigid_club_blackmail_2_50
          elsa.c "Maybe I should put it away?"
          "Elsa removes the vibrator."
          wt_image frigid_club_blackmail_2_53
          tracy.c "Oh!  What??  No!"
          elsa.c "Don't you just want my smoking hot body?"
          tracy.c "Both!  I want both!"
          wt_image frigid_club_blackmail_2_51
          elsa.c "Okay, but my body's gong to want some attention when you're finished ... *bzzzzzzzzzzz*"
          wt_image frigid_club_blackmail_2_59
          tracy.c "oooooo ... gladly!"
          wt_image frigid_club_blackmail_2_52
          "Between [elsa.name]'s tongue and the buzzing sex toy, 'finishing' doesn't take Tracy long ... *bzzzzzzzzzzz*"
          wt_image frigid_club_blackmail_2_57
          tracy.c "ooooo  ....  OHHH!!"
          wt_image frigid_club_blackmail_2_58
          "... but the mischievous look on Elsa's face as she keeps toying her friend, getting her ready for a second orgasm while she's still recovering from her first, tells you it's going to be a long time before they're done ... *bzzzzzzzzzzz*"
          wt_image frigid_club_blackmail_2_52
          "You head to bed and leave the women to their fun."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  call character_location_return(elsa) from _call_character_location_return_488
  call character_location_return(tracy) from _call_character_location_return_489
  return

label tracy_calling_elsa_outfit_2:
  wt_image frigid_club_blackmail_1_8
  tracy.c "ooooo ... Ow!  You caught me with your teeth."
  if elsa.has_tag('domme'):
    wt_image frigid_club_blackmail_1_9
    elsa.c "Don't be silly.  I didn't 'catch' you, I bit you.  I'll bite you whenever I want to, won't I?"
    tracy.c "OW!!  oooo ... yeessss"
    wt_image frigid_club_blackmail_1_10
    elsa.c "Just like you'll suck my tits when I tell you to, won't you?"
    tracy.c "Yes"
    wt_image frigid_club_blackmail_1_11
    elsa.c "Do a good job and I may let you lick between my legs, too."
    wt_image frigid_club_blackmail_1_12
    "You're not sure Tracy needed the incentive, but it doesn't hurt.  Elsa plays with herself as Tracy sucks submissively at her teat."
    elsa.c "Oohhhh"
    wt_image frigid_club_blackmail_1_13
    elsa.c "Okay, you can lick my pussy now."
    "Elsa lowers herself onto Tracy's waiting tongue ..."
    wt_image frigid_club_blackmail_1_14
    "... which works its way up and down her sex ..."
    wt_image frigid_club_blackmail_1_15
    "... before concentrating on her clit."
    elsa.c "Oohhhh"
    wt_image frigid_club_blackmail_1_16
    "Just as you think Elsa's about to cum, Tracy takes her most tender flesh into her mouth ..."
    wt_image frigid_club_blackmail_1_17
    "... and suck-bites her to orgasm."
    elsa.c "OOHHHHH!!!"
    wt_image frigid_club_blackmail_1_18
    tracy.c "You're not the only one with teeth."
    elsa.c "So I discovered."
    wt_image frigid_club_blackmail_1_42
    tracy.c "Time for you to put your mouth between my legs, or are you only interested in being in charge?"
    wt_image frigid_club_blackmail_1_45
    elsa.c "I haven't decided.  I guess you'll find out after I start licking you."
    wt_image frigid_club_blackmail_1_48
    "This may go on a while.  You leave them to their games and make your way to bed."
  elif elsa.test('submission', 79):
    add tags 'submissive_with_tracy' to elsa
    wt_image frigid_club_blackmail_1_23
    elsa.c "I'm so sorry!!"
    tracy.c "It's okay.  It was an accident, wasn't it?"
    elsa.c "Yes!  I'm so very sorry.  What do I need to do to make it up to you?"
    wt_image frigid_club_blackmail_1_19
    tracy.c "Hmmm, close your eyes while I decide.  Maybe I'll hurt your nipple the same way you hurt mine.  What do you think of that?"
    elsa.c "If ... if you want to."
    wt_image frigid_club_blackmail_1_20
    tracy.c "I didn't realize you had a submissive streak.  Bend over and present your ass to me.  If I spank you, will that be a reward or punishment?  I can never figure submissives out."
    elsa.c "I ... I don't like to be spanked."
    wt_image frigid_club_blackmail_1_21
    tracy.c "I don't like having my nipple hurt from your carelessness, so I think I should spank you anyway.  Don't you agree?"
    elsa.c "Y ... yes."
    wt_image frigid_club_blackmail_1_22
    tracy.c "Let's see if I can make this hurt as much your teeth did."
    wt_image frigid_club_blackmail_1_53
    "*smack* ... *smack* ... *smack* ... *smack* ... *smack*"
    elsa.c "Ow.  Ow!  Oww!!  OWW!!"
    wt_image frigid_club_blackmail_1_22
    tracy.c "Does that sting?"
    elsa.c "Yes!"
    wt_image frigid_club_blackmail_1_21
    tracy.c "Good.  Enough punishment, let's see if I can make that stinging sensation go away."
    wt_image frigid_club_blackmail_1_13
    "Tracy guides Elsa over her and lowers her onto her waiting tongue ..."
    elsa.c "Oohhh"
    wt_image frigid_club_blackmail_1_14
    "... which works its way up and down her sex ..."
    wt_image frigid_club_blackmail_1_15
    ".. before concentrating on her clit."
    elsa.c "Oohhhh"
    wt_image frigid_club_blackmail_1_16
    "Just as you think Elsa's about to cum, Tracy takes her most tender flesh into her mouth ..."
    wt_image frigid_club_blackmail_1_17
    "... and suck-bites her to orgasm."
    elsa.c "OOHHHHH!!!"
    wt_image frigid_club_blackmail_1_18
    tracy.c "In case you were wondering, my bite wasn't an accident."
    elsa.c "I could tell."
    wt_image frigid_club_blackmail_1_42
    tracy.c "Just like it's not an accident that you're going to spend the next hour with your head between my legs, while I count how many times your submissive tongue can bring me to orgasm."
    elsa.c "Okay"
    wt_image frigid_club_blackmail_1_40
    "This is going to go on a while.  You leave them to their games and make your way to bed."
  else:
    wt_image frigid_club_blackmail_1_7
    elsa.c "Ooops.  Did I make your nipple all sore and throbby?  Let me make that up to you."
    tracy.c "ooooo"
    wt_image frigid_club_blackmail_1_19
    tracy.c "Oh, look!  I'm not the only one with throbbing nipples.  Are yours sore, too?"
    elsa.c "Mmmm.  Uh huh."
    wt_image frigid_club_blackmail_1_11
    tracy.c "Does this make them better ..."
    elsa.c "Oohhh"
    wt_image frigid_club_blackmail_1_12
    tracy.c "... or worse?"
    elsa.c "OH!"
    wt_image frigid_club_blackmail_1_24
    tracy.c "Why are you touching yourself down here?"
    wt_image frigid_club_blackmail_1_25
    tracy.c "Nobody bit you here by mistake, did they?"
    elsa.c "OH!"
    wt_image frigid_club_blackmail_1_13
    tracy.c "Maybe the throbbing is coming from between here?"
    "Tracy guides Elsa over her and lowers her onto her waiting tongue ..."
    elsa.c "Oohhh"
    wt_image frigid_club_blackmail_1_14
    "... which works its way up and down her sex ..."
    wt_image frigid_club_blackmail_1_15
    ".. before concentrating on her clit."
    elsa.c "Oohhhh"
    wt_image frigid_club_blackmail_1_16
    "Just as you think Elsa's about to cum, Tracy takes her most tender flesh into her mouth ..."
    wt_image frigid_club_blackmail_1_17
    "... and suck-bites her to orgasm."
    elsa.c "OOHHHHH!!!"
    wt_image frigid_club_blackmail_1_18
    tracy.c "Ooops.  I accidentally bit your clit.  Do you need me to make it feel better?"
    elsa.c "Mmmm, you already did."
    wt_image frigid_club_blackmail_1_42
    tracy.c "Oh good!  You know, my clit is rather sore and throbby right now, too."
    wt_image frigid_club_blackmail_1_28
    elsa.c "Uh oh.  Should I take a look at it?"
    wt_image frigid_club_blackmail_1_45
    tracy.c "Yes, please!"
    wt_image frigid_club_blackmail_1_48
    "This may go on a while.  You leave them to their games and make your way to bed."
  return

label tracy_calling_diamond:
  call forced_movement(living_room) from _call_forced_movement_140
  summon tracy
  summon diamond
  if not tracy.has_tag('sex_with_diamond'):
    add tags 'sex_with_diamond' to tracy
    "You send a quick note to Master M, explaining that you have a lesbian client in need of a play partner, and that this could be a great opportunity for him to further Diamond's experience with women.  It doesn't take him long to reply."
    master_m.c "Is she dominant? I'm not sure Diamond will respond well if your client isn't able to control her."
    "I think she'll be quite capable of taking charge."
    master_m.c "Okay. I'll tell Diamond to drop by your house after she finishes work today."
    wt_image ms1_club_blackmail_1_1
    "Diamond arrives later that day, but she doesn't look happy about it."
    player.c "You seem to have a problem."
    diamond.c "May I speak freely?"
    $ title = "Hear what she has to say?"
    menu:
      "Go ahead":
        player.c "Go ahead."
        wt_image ms1_club_blackmail_1_2
        diamond.c "Why are you getting involved in my training?  He's an experienced Dom, he doesn't need you planting ideas in his head, or encouraging him to lend me out to women."
        player.c "Which are you really mad about, me being involved or the prospect of serving another woman?"
        wt_image ms1_club_blackmail_1_4
        diamond.c "Both!"
        $ title = "What do you tell her?"
        menu:
          "M wants you to serve women":
            player.c "M is the one who wants you to serve women.  I'm just pointing out opportunities for you to get experience.  Like with my client, today.  Have a seat.  She'll be here in a moment."
          "M loves you":
            player.c "M loves you.  That gets in the way of him giving you what you truly need."
            wt_image ms1_club_blackmail_1_1
            diamond.c "Oh, and you know what I truly need?"
            player.c "Maybe not completely, but I can still point out to M things he should be doing differently.  Like getting you used to women.  He wants that, but he's not pushing it the way you need to be pushed."
            wt_image ms1_club_blackmail_1_4
            player.c "Unfold your arms and have a seat.  My client will be here soon."
          "You love M":
            player.c "You love M.  It's sweet, but I'm worried it's a different type of love than is really appropriate in a D/S relationship.  It's messing up your reactions to normal things."
            wt_image ms1_club_blackmail_1_1
            diamond.c "You think I'm messing things up?"
            player.c "I think M wants to do what's best for you and his relationship with you.  It's perfectly normal for a Dom to talk to other people and take advice regarding his slave's training, just like it's perfectly normal for him to want her to be comfortable serving women.   All I've done is point out opportunities for you to get experience.  Like with my client, today."
            wt_image ms1_club_blackmail_1_4
            player.c "Unfold your arms and have a seat.  She'll be here in a moment."
          "That's none of her concern":
            wt_image ms1_club_blackmail_1_1
            player.c "M's conversations with me are none of your concern, [diamond.training_name].  M's your Dom.  If he wants to talk about you with other people and take advice on how you should be trained, that's his business, not yours.  He decided he wanted you to get used to serving women, all you need to concern yourself with is doing a good job and pleasing him."
            wt_image ms1_club_blackmail_1_4
            player.c "Unfold your arms and have a seat.  My client will be here soon."
      "No":
        player.c "No.  You're not here to talk, you're here to serve.  And not me, this time, my client.  She doesn't need this attitude.  Unfold your arms."
        wt_image ms1_club_blackmail_1_4
        player.c "Now have a seat.  She'll be here in a moment."
    wt_image ms1_club_blackmail_1_3
    "She sits, but she's all attitude about it."
    wt_image ms1_club_blackmail_1_5
    "Diamond's still frustrated when Tracy arrives.  Tracy picks up the vibe quickly."
    tracy.c "Hi!  You must be Diamond.  I'm Tracy."
    diamond.c "Hi"
    wt_image ms1_club_blackmail_1_65
    tracy.c "You don't seem too happy to see me."
    diamond.c "Didn't they tell you why I'm here?"
    wt_image ms1_club_blackmail_1_6
    tracy.c "Because you wanted to gain experience having sex with a woman."
    diamond.c "I'm required to gain experience having with sex with women."
    wt_image ms1_club_blackmail_1_7
    tracy.c "Required?  Well, sweetie, I'm not here to rape you!  Do I look dangerous to you?"
    diamond.c "No, of course not."
    wt_image ms1_club_blackmail_1_8
    tracy.c "Good!  So can we agree I'm not the bad guy here?"
    diamond.c "Yes.  Of course, you're not."
    wt_image ms1_club_blackmail_1_6
    tracy.c "Is it your boyfriend who's the bad guy?  Is he making you do this?"
    diamond.c "Yes, I mean, no.  He's not the bad guy either.  Yes, he's making me do this, but I kinda gave him permission.  He's not my boyfriend.  He's my Dom."
    wt_image ms1_club_blackmail_1_5
    tracy.c "So, you told him he could give you orders, but you don't like this order?"
    diamond.c "Not really.  No."
    tracy.c "Has he told you to be with a woman before?"
    diamond.c "Yes"
    wt_image ms1_club_blackmail_1_65
    tracy.c "Is it me, then?"
    diamond.c "No!  You're beautiful.  And you seem sweet."
    wt_image ms1_club_blackmail_1_8
    tracy.c "Whew!  Thanks!  I was worried there for a moment that maybe it was just me."
    diamond.c "No, you seem great."
    wt_image ms1_club_blackmail_1_9
    tracy.c "Look, you may not want to hear this, but I have to be honest with you.  You're really beautiful and really sexy, and when I walked in and saw you sitting here, it turned me on."
    wt_image ms1_club_blackmail_1_8
    diamond.c "Thanks.  You're beautiful, too.  Really!  I'm just not ... I'm just not into girls."
    tracy.c "I know.  And I'm not really into domination and submission.  But maybe we can try something and see if we both like it?"
    wt_image ms1_club_blackmail_1_9
    tracy.c "I'm not going to force you to do anything.  If this doesn't feel good, I'll send you home with a hand written note that says you were my best lesbian lover ever, so you don't get into trouble with your boyfriend."
    wt_image ms1_club_blackmail_1_65
    diamond.c "My Dom."
    tracy.c "Right, sorry.  Your Dom."
    diamond.c "What did you want to try?"
    wt_image ms1_club_blackmail_1_10
    tracy.c "I want you to uncross your legs so I can put my hand on your knee."
    wt_image ms1_club_blackmail_1_11
    tracy.c "How does that feel?"
    diamond.c "Um, okay, I guess.  Weird."
    wt_image ms1_club_blackmail_1_65
    tracy.c "Weird because I'm a girl or because I'm not your boyfr ... I mean, because I'm not your Dom?"
    diamond.c "Because you're a girl.  He ..."
    wt_image ms1_club_blackmail_1_11
    tracy.c "He lends you out to other people a lot?"
    diamond.c "Not a lot, but, sometimes, yes."
    tracy.c "You like it when he tells you what to do?"
    wt_image ms1_club_blackmail_1_12
    diamond.c "Yes"
    tracy.c "And these guys he lends you to, do you also like it when they tell you what to do?"
    diamond.c "Usually, yes."
    wt_image ms1_club_blackmail_1_66
    tracy.c "Okay, last question, I promise."
    "Tracy leans in and whispers in Diamond's ear."
    wt_image ms1_club_blackmail_1_13
    tracy.c "Will you be offended if I tell you what I want you to do for me?"
    "Diamond slowly shakes her head 'no'."
    wt_image ms1_club_blackmail_1_66
    tracy.c "In that case, I want you to rub my leg with your hand."
    wt_image ms1_club_blackmail_1_14
    "Tracy smiles as Master M's slave does as she's told."
    wt_image ms1_club_blackmail_1_15
    tracy.c "Can you see without your glasses?"
    diamond.c "Yes.  They're only for reading.  I usually only wear them for work."
    wt_image ms1_club_blackmail_1_67
    tracy.c "Hmmm.  That's too bad."
    diamond.c "Too bad?  Why?"
    wt_image ms1_club_blackmail_1_68
    tracy.c "I thought maybe if I took your glasses off, you wouldn't be able to tell I was a woman, and I might fool you into thinking I'm a man."
    wt_image ms1_club_blackmail_1_16
    "Diamond laughs."
    diamond.c "I'm pretty sure even a blind person could tell you're all woman."
    wt_image ms1_club_blackmail_1_17
    tracy.c "Thanks!  What about a Domme, then?  Not enough whips and chains, I guess, to fool you into thinking I'm one of those?"
    diamond.c "Honestly, I sometimes react badly to Dommes.  You seem to be doing a preety good job of taking control without the whips and chains."
    wt_image ms1_club_blackmail_1_18
    tracy.c "In that case, I order you to kiss me."
    diamond.c "Kissing?  That's ... you're a girl.  It just seems ..."
    tracy.c "That was an order, not a request."
    wt_image ms1_club_blackmail_1_19
    "Tracy seems to have the situation well in hand."
    $ diamond.lesbian_training += 1
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        wt_image ms1_club_blackmail_1_20
        "Pushing up Diamond's shirt, Tracy tweaks her nipple, eliciting a small yelp that's only partly surprise and clearly partly pleasure."
        diamond.c "Oh!"
        wt_image ms1_club_blackmail_1_46
        "Tracy smiles briefly before addressing Diamond sternly."
        wt_image ms1_club_blackmail_1_69
        tracy.c "Remove your top and mine."
        wt_image ms1_club_blackmail_1_21
        "Her next order is as much sigh as instruction."
        wt_image ms1_club_blackmail_1_38
        tracy.c "Make my nipples hard."
        wt_image ms1_club_blackmail_1_22
        tracy.c "ooooo"
        wt_image ms1_club_blackmail_1_23
        "Clearly enjoying the feel of Diamond suckling on her teat, Tracy reaches down and caresses the sub-girls's breast ..."
        wt_image ms1_club_blackmail_1_70
        "... before tweaking her nipple again, harder this time."
        diamond.c "OH!"
        wt_image ms1_club_blackmail_1_24
        tracy.c "Whose nipple is harder?"
        diamond.c "Umm, they both seem to be really hard."
        wt_image ms1_club_blackmail_1_71
        tracy.c "Then I better check to see which of us is wetter."
        wt_image ms1_club_blackmail_1_25
        "Tracy is, but Diamond's not completely dry."
        wt_image ms1_club_blackmail_1_72
        tracy.c "Lie down."
        wt_image ms1_club_blackmail_1_26
        "Tracy kisses Diamond again as she guides her backwards ..."
        wt_image ms1_club_blackmail_1_27
        "... then takes her breast into her mouth ..."
        wt_image ms1_club_blackmail_1_28
        "... and suck-bites it, generating another pain-pleasure yelp."
        diamond.c "OH!!"
        wt_image ms1_club_blackmail_1_29
        "Then she lowers her mouth to between Diamond's legs ..."
        wt_image ms1_club_blackmail_1_30
        "... and does the same to the tender folds of the sub-girl's sex."
        diamond.c "OH!!   OHHH!!!"
        wt_image ms1_club_blackmail_1_31
        "Tracy grins as she looks up at Diamond and licks away the soreness from her love bite."
        tracy.c "You're going to cum in my mouth."
        wt_image ms1_club_blackmail_1_32
        "It's more prediction than order ..."
        diamond.c "oohhh"
        wt_image ms1_club_blackmail_1_73
        "... one that takes little time to come true."
        wt_image ms1_club_blackmail_1_33
        diamond.c "Oooohhhhh!!!"
        wt_image ms1_club_blackmail_1_31
        tracy.c "Go home to your boy-Dom, Dom-friend, whatever he is, and tell him I had a great time playing with you."
        wt_image ms1_club_blackmail_1_74
        diamond.c "Do you want me to ... before I go, I mean ..."
        tracy.c "Next time, if there is a next time, you're going to go down on me."
        wt_image ms1_club_blackmail_1_34
        tracy.c "But I only want there to be a next time if you're doing it not just because your man told you to, but because you genuinely want to make me feel the way I just made you feel."
        wt_image ms1_club_blackmail_1_35
        "With a final, quick kiss, Tracy is gone before Diamond can respond."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  elif tracy.has_tag('sex_with_diamond') and not tracy.has_tag('second_session_with_diamond'):
    add tags 'second_session_with_diamond' to tracy
    "You send another note to Master M, asking about Diamond's availability.  M lets you know she'll be there as soon as she finishes work."
    wt_image ms1_club_blackmail_1_45
    "There's no hint of attitude when Diamond arrives and immediately strips."
    wt_image ms1_club_blackmail_1_36
    player.c "Aren't you going to wait for Tracy?"
    wt_image ms1_club_blackmail_1_37
    diamond.c "I assume she'll want me naked when she gets here."
    wt_image ms1_club_blackmail_1_76
    tracy.c "Good guess.  Catch me up to where you are."
    wt_image ms1_club_blackmail_1_77
    "You hadn't heard Tracy come in, and she seems too interested in Diamond to even say hello to you."
    $ diamond.lesbian_training += 1
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        tracy.c "You remember what I said last time, about if there's a next time?"
        diamond.c "Yes"
        wt_image ms1_club_blackmail_1_78
        tracy.c "So, since you're here, can I take it you don't mind the idea of making love to me?"
        "Diamond shakes her head."
        diamond.c "I don't mind.  Not if that's what you want me to do for you."
        wt_image ms1_club_blackmail_1_79
        tracy.c "Does that mean I don't have to order you around today?"
        diamond.c "Umm, actually ..."
        wt_image ms1_club_blackmail_1_80
        tracy.c "It would be easier for you if I took control?"
        diamond.c "Yes"
        wt_image ms1_club_blackmail_1_34
        "Tracy pulls Diamond down onto the sofa with her ..."
        tracy.c "Then in that case, I claim you as my slave for the remainder of the evening."
        wt_image ms1_club_blackmail_1_35
        "... and gives her newly acquired slave a sweet, gentle kiss ..."
        wt_image ms1_club_blackmail_1_74
        "... before pulling her head back."
        tracy.c "Eat my cunt, slavegirl."
        wt_image ms1_club_blackmail_1_38
        "Tracy pushes Diamond's head downwards ..."
        wt_image ms1_club_blackmail_1_39
        "... and directs her between her legs ..."
        wt_image ms1_club_blackmail_1_40
        "... where Diamond sets to work, lapping at her pussy."
        tracy.c "ooooo"
        wt_image ms1_club_blackmail_1_81
        "She's there for some time.  Tracy seems intent on delaying her orgasm as long as possible as she enjoys the submissive girl's attention."
        wt_image ms1_club_blackmail_1_82
        "As her jaw and tongue begin to tire, Diamond intensifies her efforts."
        wt_image ms1_club_blackmail_1_41
        "Remembering the trick Tracy used on her, Diamond suck-bites at Tracy's sex ..."
        tracy.c "Oh!!"
        wt_image ms1_club_blackmail_1_42
        "... then runs a thumb roughly over the tender flesh ..."
        tracy.c "nnnn"
        wt_image ms1_club_blackmail_1_43
        "... before pushing the thumb inside ..."
        tracy.c "oooooo"
        wt_image ms1_club_blackmail_1_44
        "... and bringing her to orgasm."
        tracy.c "ooooo  ....  OHHH!!"
        wt_image ms1_club_blackmail_1_34
        tracy.c "Are you sure you're not bisexual?"
        diamond.c "I'm sure.  But I'm glad you liked that."
        "You leave the two of them alone to chat, and head to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  else:
    wt_image ms1_club_blackmail_1_45
    "Master M seems happy to have Diamond continue to spend time with Tracy, and Diamond seems quite comfortable with the idea herself."
    diamond.c "Hi!"
    player.c "Come on in.  Tracy's waiting for you."
    $ title = "Stay and watch?"
    menu:
      "Watch them (ends day)":
        $ tracy.diamond_outfit += 1
        # scroll 1 through 3
        if tracy.diamond_outfit > 3:
          $ tracy.diamond_outfit = 1
        if tracy.diamond_outfit == 1:
          wt_image ms1_club_blackmail_1_12
          tracy.c "There's my favorite slavegirl.  Kiss me."
          wt_image ms1_club_blackmail_1_19
          tracy.c "Mmmmm"
          wt_image ms1_club_blackmail_1_46
          tracy.c "You did such a good job the other day with your thumb inside me, I want you to use your fingers to get me off today."
          diamond.c "Okay"
          wt_image ms1_club_blackmail_1_47
          "Diamond pulls off Tracy's panties ..."
          wt_image ms1_club_blackmail_1_48
          "... wets her finger ..."
          wt_image ms1_club_blackmail_1_49
          "... and slides it along Tracy's equally wet sex."
          tracy.c "ooooo"
          wt_image ms1_club_blackmail_1_50
          "Tracy may have only told her to use her fingers, but she doesn't object as Diamond laps at the nipple in front of her ..."
          tracy.c "oooooo"
          wt_image ms1_club_blackmail_1_51
          "... and soon she's too busy climaxing to complain of anything at all."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image ms1_club_blackmail_1_83
          tracy.c "Mmmm.  Keep rubbing.  I want to feel your fingers on my pussy while we chat."
          "You leave Diamond to Tracy's unique form of domination and head to bed."
        elif tracy.diamond_outfit == 2:
          wt_image ms1_club_blackmail_1_12
          tracy.c "Hello, slavegirl.  Ready to please me?"
          diamond.c "Yes.  Did you want my mouth on you, or my fingers again?"
          wt_image ms1_club_blackmail_1_13
          "Tracy leans in and licks Diamond's ear playfully before responding."
          wt_image ms1_club_blackmail_1_52
          tracy.c "Neither.  Get your clothes off, lie back, and spread your legs."
          wt_image ms1_club_blackmail_1_84
          "Tracy stands up and undresses, a big grin on her face as she watches Diamond do the same."
          wt_image ms1_club_blackmail_1_72
          "When they're both naked, she straddles M's slavegirl, pressing their sexes together."
          wt_image ms1_club_blackmail_1_53
          diamond.c "Oh!"
          wt_image ms1_club_blackmail_1_54
          tracy.c "You like that?"
          diamond.c "Umm, it feels ... weird."
          wt_image ms1_club_blackmail_1_55
          "Clearly it doesn't feel weird to Tracy.  It feels hot, and she moans as she grinds herself against Diamond ..."
          tracy.c "ooooo"
          wt_image ms1_club_blackmail_1_56
          "... bringing herself to orgasm."
          tracy.c "ooooo  ....  OHHH!!"
          wt_image ms1_club_blackmail_1_57
          "Then to your surprise, and possibly her own, Diamond joins her."
          diamond.c "Oooohhhhh!!!"
          wt_image ms1_club_blackmail_1_85
          tracy.c "When are you going to admit to me that you do like girls?"
          diamond.c "It's not that!  It was just the feel of you cumming against me."
          wt_image ms1_club_blackmail_1_80
          tracy.c "You don't like girls, you just cum when they press their bodies against you?"
          diamond.c "Against my clit and start trembling and moaning from their own climax, yeah."
          tracy.c "That sounds gay to me."
          diamond.c "Quit it!  Maybe I just like you?"
          wt_image ms1_club_blackmail_1_86
          tracy.c "Oh, now the slavegirl is going to try flattery?  Forget it.  I'm still going to boss you around.  Kiss me, slavegirl."
          diamond.c "Okay"
          "You leave the two of them to their bossing and being bossed and head to bed."
        elif tracy.diamond_outfit == 3:
          wt_image ms1_club_blackmail_1_67
          tracy.c "Hello totally-not-bisexual-but-digs-me-anyway slavegirl.  Guess what I have planned for us today?"
          diamond.c "I don't know."
          wt_image ms1_club_blackmail_1_66
          tracy.c "Hmmm.  Kiss me and I'll tell you."
          wt_image ms1_club_blackmail_1_19
          "There's not even a hint of hesitation from Diamond."
          wt_image ms1_club_blackmail_1_20
          tracy.c "Mmmm.  You're getting good at that.  Do you think you're also getting good at getting me off?"
          diamond.c "Umm, I guess so."
          wt_image ms1_club_blackmail_1_46
          tracy.c "I hope so, because today we're going to play a little game, to see which of us can get the other off first.  If you cum before I do, you lose."
          diamond.c "What happens if I lose?"
          wt_image ms1_club_blackmail_1_25
          tracy.c "So you admit that you may get so excited you cum before I do?  Hmmm, you are a little wet between the legs already."
          diamond.c "No, it's just ... it sounded like there were going to be consequences."
          wt_image ms1_club_blackmail_1_71
          tracy.c "Of losing?  Don't worry.  I'm not going to spank you if you cum first.  Or would that be a reward, not a punishment?  I've never really understood how that works for submissives."
          wt_image ms1_club_blackmail_1_74
          tracy.c "Are you wet because you like me, or because you were thinking about consequences?"
          diamond.c "Maybe both?"
          wt_image ms1_club_blackmail_1_34
          tracy.c "Then it wouldn't be fair to threaten you with consequences.  I want you to cum first because you're driven to distraction by the feel of me playing with your body, not because you're imagining me locking you up in a cage."
          wt_image ms1_club_blackmail_1_72
          tracy.c "The only thing that will happen if you cum first is that I'll know you really do like girls, no matter what you say."
          wt_image ms1_club_blackmail_1_58
          "Tracy guides the two of them into position, her head underneath Diamond and her legs spread open, exposing her sex to Diamond's attention.  That Tracy puts Diamond on top of her makes it clear that she doesn't want to get Diamond off by dominating her."
          wt_image ms1_club_blackmail_1_59
          "The grin on Diamond's face as she traces her fingers across Tracy's sex, however, makes you think she probably is thinking about Tracy imposing consequences like locking her up in a cage if she orgasms ..."
          wt_image ms1_club_blackmail_1_60
          "... which is the wrong thing for her to be thinking if she really wants to win Tracy's little contest."
          diamond.c "oohhh"
          wt_image ms1_club_blackmail_1_61
          "An even worse decision was starting off by using her fingers on Tracy, when Tracy is diving right in with lips and tongue ..."
          diamond.c "oohhhh"
          wt_image ms1_club_blackmail_1_62
          "... outgunning her and bringing the contest to a surprisingly quick end, just as Diamond's probing fingers are starting to set Tracy's hips a-twitching."
          diamond.c "Oooohhhhh!!!"
          wt_image ms1_club_blackmail_1_63
          "Tracy doesn't stop to gloat over her victory, and Diamond, realizing her error, switches to using her mouth, as well, for round two."
          wt_image ms1_club_blackmail_1_64
          "It's clear Tracy doesn't intend that to be Diamond's only orgasm for the night, and you're pretty sure that eventually she'll allow herself to enjoy a few of her own, as well."
          wt_image ms1_club_blackmail_1_87
          "You leave the two of them to their competition and head to bed."
      "Go on with your day":
        add tags 'go_on_with_day' to tracy
  call character_location_return(diamond) from _call_character_location_return_490
  call character_location_return(tracy) from _call_character_location_return_491
  return

label tracy_calling_chelsea:
    add tags 'considered_chelsea' to tracy
    if chelsea.has_tag('likes_girls'):
        "Considering the difficulties her attraction to women is causing Tracy, she may be exactly the wrong woman to set [chelsea.name] up with.  Better choose someone else for Tracy."
    else:
        "You want [chelsea.name] to feel comfortable admitting a sexual attraction to women, not remind her about the social consequences that can come from this 'perversion'.  Better choose someone else for Tracy."
    call expandable_menu(tracy_session_date_menu) from _call_expandable_menu_66
    return

label tracy_calling_janice:
    add tags 'considered_janice' to tracy
    "Janice's kink is for bi-curious blondes only.  Tracy is way beyond bi-curious.  Better choose someone else for Tracy."
    call expandable_menu(tracy_session_date_menu) from _call_expandable_menu_67
    return

label tracy_calling_marilyn:
    add tags 'considered_marilyn' to tracy
    "Considering how long Tracy's been dogging around behind her husband's back, including at the Club, no doubt Tracy's already come to Marilyn's attention.  Better choose someone else."
    call expandable_menu(tracy_session_date_menu) from _call_expandable_menu_68
    return

label tracy_calling_sam:
    add tags 'considered_sam' to tracy
    if samantha.has_tag('maid'):
        sys "As soon as I get appropriate photos, I'll put this in place. ~ WT"
    elif samantha.has_tag('married_girlfriend'):
        "Sam's happy with her current wife."
    elif samantha.conversation_event <= 3:
        "Sam's happy with her current girlfriend."
    elif samantha.conversation_event <= 16:
        "Meaningless sex isn't going to help Sam sort herself out."
    else:
        "Sam's not available."
    return

label tracy_calling_sarah:
    call forced_movement(living_room) from _call_forced_movement_717
    summon tracy no_follows
    summon sarah no_follows
    $ sarah.training_session()
    wt_image lw_club_blackmail_1_1
    "Sarah's not entirely sure what to make of being offered to one of your clients."
    wt_image lw_club_blackmail_1_2
    "Tracy, however, pays that no heed, and barrels through Sarah's hesistancy like a bull in a china shop ..."
    wt_image lw_club_blackmail_1_3
    "... by-passing Sarah's brain with a purely physical approach to her seduction."
    wt_image lw_club_blackmail_1_4
    "Sarah's still not 100% certain she wants to be doing this, when she finds her face being pushed into the more experienced lesbian's pussy ..."
    wt_image lw_club_blackmail_1_5
    "... so that Tracy can use her tongue as a creaming post."
    tracy.c "ooooo  ....  OHHH!!"
    $ sarah.temporary_count = 1
    if sarah.has_tag('controlled_orgasms'):
        $ title = "Stop things there?"
        menu:
            "Yes":
                $ sarah.temporary_count = 0
                wt_image lw_club_blackmail_1_6
                "Sarah looks at you uncertainly as she leaves, a bit put off at having been nearly raped and then discarded."
                wt_image lw_club_blackmail_1_7
                tracy.c "I would have looked after her, too.  She seemed a little nervous, but I know her type.  A little aggression, a little teasing, and she's butter in my hands.  Or on my fingers.  Didn't you think she'd want an orgasm?"
                player.c "I think she's happier without one.  Or, at least, I am."
            "No, let Tracy get Sarah off, too.":
                pass
    if sarah.temporary_count == 1:
        $ sarah.temporary_count = 0
        wt_image lw_club_blackmail_1_8
        "Tracy leads Sarah over to the sofa, places Sarah's hand on her pussy, and then uses both of her own hands to begin probing and teasing Sarah."
        wt_image lw_club_blackmail_1_9
        "Tracy's good with her fingers, and a still-reluctant Sarah finds her body responding despite her reservations."
        wt_image lw_club_blackmail_1_10
        "As Sarah's arousal grows ..."
        sarah.c "Oooohhhh!"
        wt_image lw_club_blackmail_1_11
        "... Tracy grins at you ..."
        sarah.c "Oooohhhh!  Ooooohhhhhh!!"
        wt_image lw_club_blackmail_1_12
        "... and with some hard, fast thrusts of her hand, frigs your girlfriend to climax."
        sarah.c "Oooohhhhh  Gaawwwdddd!!!!"
        wt_image lw_club_blackmail_1_13
        "There's nothing romantic about the 'kiss' that follows.  It's lewd and animalistic as Tracy licks Sarah's mouth, like a prize she's claimed, rather than a lover she's wooed."
        wt_image lw_club_blackmail_1_14
        "Sarah responds in kind, finally accepting that Tracy sees her as nothing more than a warm body to take and fuck, and happy at least that Tracy knew what she was doing with her body while she had it."
        call sarah_gf_orgasm from _call_sarah_gf_orgasm_151
        $ sarah.orgasm_count -= 1
    call character_location_return(sarah) from _call_character_location_return_492
    call character_location_return(tracy) from _call_character_location_return_493
    return

# Display Portrait
# CHARACTER: Display Portrait
label tracy_update_media:
    if current_location == club:
        if tracy.has_tag('hypnotized_now'):
            $ tracy.change_image('club_blackmail_initial_55')
        else:
            $ tracy.change_image('club_blackmail_initial_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label tracy_examine:
    if current_location == club:
        if tracy.has_tag('hypnotized_now'):
            tracy.c "I like girls, not boys!  I only stay with my husband for his money!"
            "It seems Tracy's husband hasn't yet discovered the spectacle she's making of herself."
        else:
            "You recognize this woman.  You saw her with Sam at the masquerade ball."
    return

# Talk to Character
# NEED finish from here down
label tracy_talk:
  add tags 'initial_talk_complete' 'sex_with_sam' to tracy
  wt_image club_blackmail_initial_1
  tracy.c "Do I know you?"
  player.c "I saw you with my friend at the masquerade ball."
  wt_image club_blackmail_initial_56
  "She blushes."
  tracy.c "Oh.  Ummm, I didn't think anyone would recognize me."
  player.c "You probably shouldn't have let Sam pull off your mask."
  wt_image club_blackmail_initial_1
  tracy.c "I guess not.  Please, don't mention what you saw to anybody."
  if tracy.has_tag('sex_with_elsa'):
    player.c "I know you from somewhere else, too, don't I? I remember now  You're the woman Elsa hooked up with. You seem to be sleeping your way through all my female friends."
    "Her blush deepens."
    tracy.c "Please, don't tell anyone."
  $ title = "What type of person are you?"
  menu:
    "Kind":
      player.c "Don't tell anybody, or don't tell your husband?  I take it he doesn't know about your interest in women? Or does he know, and not approve?"
      wt_image club_blackmail_initial_56
      "Her blush deepens."
      tracy.c "He doesn't approve. Please, if he found out I was doing this again ..."
      player.c "It'll be our little secret."
      wt_image club_blackmail_initial_1
      "She sighs a sigh of relief."
      tracy.c "Thank you!  My name's Tracy, by the way."
      "You're pretty sure this isn't the last you'll hear from Tracy."
      $ tracy.opp = 2
      $ tracy.event_week = week + 3
      $ tracy.week_available = tracy.event_week
      $ tracy.change_full_name("", "Tracy", "the Club Member")
    "Manipulative":
      player.c "Does your husband not know of your interest in women, or does he know and not approve?"
      wt_image club_blackmail_initial_1
      "Her blush deepens."
      tracy.c "He doesn't approve.  What does it matter?"
      player.c "It doesn't matter to me.  It seems it does matter to him, however.  I suppose I should go tell him.  I don't like carrying around secrets, it makes me feel dirty."
      wt_image club_blackmail_initial_45
      tracy.c "No!!  Don't.  What do you want?"
      $ title = "What do you want?"
      menu:
        "Money":
          player.c "I'll make it easy for you.  You send me money and I'll forget what I saw."
          wt_image club_blackmail_initial_44
          tracy.c "This is totally against the rules of the Club.  What happens here isn't supposed to leave this Club. They're very strict on that.  They won't take it well when I tell them you tried to extort me over an incident at the masquerade ball."
          "She has a point.  The Club would be pretty pissed if they knew what you were doing."
          $ title = "What do you do?"
          menu:
            "Back off":
              player.c "Jeez, I was just making a little joke.  Don't get so serious.  I'm not going to tell anybody what I saw."
              wt_image club_blackmail_initial_46
              "She leaves, breathing a sigh of relief."
              $ tracy.opp = 3
            "Call her bluff":
              player.c "That would definitely get me in trouble.  Of course, the reason why I was extorting you would come out, too.  I'd lose access to the Club.  What would you lose?"
              wt_image club_blackmail_initial_56
              player.c "That's right, a lot more.  I'm thinking a little bit of money to make this go away would be a lot less painful for you."
              wt_image club_blackmail_initial_45
              tracy.c "You're an asshole.  A complete asshole."
              "She fumes for a moment, then continues."
              wt_image club_blackmail_initial_44
              tracy.c "I'll pay you 100."
              $ title = "What do you do?"
              menu:
                "Take 100":
                  player.c "There.  See how easy that was?  Send me the money and I'll be on my way."
                  "Fuming, she provides instructions to have the money transferred to you."
                  wt_image club_blackmail_initial_46
                  tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                  "She probably means it.  You smile at her as she leaves, which makes her even more infuriated."
                  player.c "Pleasure doing business with you.  Have a good day."
                  $ tracy.opp = 4
                  change player money by 100 notify
                  $ tracy.dismiss(False)
                "Demand more":
                  player.c "Not enough."
                  tracy.c "That's all I have!"
                  wt_image club_blackmail_initial_45
                  player.c "You can't expect me to believe that a rich society lady like you doesn't have access to a lot more money than that."
                  tracy.c "My husband controls all our finances."
                  wt_image club_blackmail_initial_56
                  player.c "Then I'd suggest you not do anything to get him mad at you.  Or let him find out about anything that would get him mad at you."
                  tracy.c "The only other money I have access to is 100 I set aside to buy a birthday present for our 6 year old daughter.  You can't expect me to give you that?"
                  $ title = "What do you do?"
                  menu:
                    "Settle for 100":
                      player.c "Oh fine.  Buy your daughter her damn present.  Just send me the 100 and I'll be on my way."
                      "Relieved, she provides instructions to have the money transferred to you."
                      wt_image club_blackmail_initial_46
                      tracy.c "Thanks, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                      "She probably means it.  You smile at her as she leaves, which makes her even more infuriated."
                      player.c "Pleasure doing business with you.  Have a good day."
                      $ tracy.opp = 4
                      change player money by 100 notify
                      $ tracy.dismiss(False)
                    "Take 200":
                      player.c "200 it is."
                      wt_image club_blackmail_initial_45
                      tracy.c "You're going to take my daughter's birthday money!"
                      player.c "I'm sure you can find something of yours to sell.  You're showing off a few items right now that men would pay for access to.  Would you like me to arrange some part-time work for you?"
                      wt_image club_blackmail_initial_44
                      tracy.c "No thank you!"
                      "Fuming, she provides instructions to have the money transferred to you."
                      wt_image club_blackmail_initial_46
                      tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                      "She probably means it.  You smile at her as she leaves, which makes her even more infuriated."
                      player.c "Pleasure doing business with you.  Have a good day.  Remember to look me up the next time you need money.  That employment offer stands."
                      $ tracy.opp = 4
                      change player money by 200 notify
                      $ tracy.dismiss(False)
        "Her":
          player.c "Feeling dirty like this, it's a new sensation for me, but you're used to feeling dirty, aren't you?  All those secrets you keep from your husband.  I bet you enjoy being a dirty girl.  Do you get off on it?"
          wt_image club_blackmail_initial_44
          "She glares at you, saying nothing."
          player.c "I'll make it easy for you, dirty girl.  You give me you and I'll forget what I saw."
          wt_image club_blackmail_initial_45
          tracy.c "This is totally against the rules of the Club.  What happens here isn't supposed to leave this Club. They're very strict on that.  They won't take it well when I tell them you tried to blackmail me over an incident at the masquerade ball."
          "She has a point. The Club would be pretty pissed if they knew what you were doing."
          $ title = "What do you do?"
          menu:
            "Back off":
              player.c "Jeez, I was just making a little joke.  Don't get so serious.  I'm not going to tell anybody what I saw."
              wt_image club_blackmail_initial_46
              "She leaves, breathing a sigh of relief."
              $ tracy.opp = 3
            "Call her bluff":
              player.c "That would definitely get me in trouble.  Of course, the reason why I was blackmailing you would come out.  I'd lose access to the Club.  What would you lose?"
              wt_image club_blackmail_initial_56
              player.c "That's right, a lot more.  I'm thinking a couple of hours with me would be a lot less painful for you.  I won't even leave any awkward bruises for you to explain."
              wt_image club_blackmail_initial_45
              tracy.c "You're an asshole. A complete asshole."
              "She fumes for a moment, then continues."
              wt_image club_blackmail_initial_44
              tracy.c "What do I have to do?"
              player.c "Spread your legs."
              wt_image club_blackmail_initial_45
              tracy.c "My husband is right over there on the other side of the room!"
              wt_image club_blackmail_initial_1
              player.c "I'm not going to touch you here, you stupid slut.  I'll tell you when and where to join me.  Right now we're just establishing who's in charge, so that I know we both understand the situation.  Spread your legs and don't make a habit of making me tell you things twice."
              wt_image club_blackmail_2
              "Slowly she opens her legs."
              player.c "Better.  Pull up your dress so I can see your pussy."
              tracy.c "My husband could come over any minute!"
              player.c "Then you'd better act quick."
              wt_image club_blackmail_3
              player.c "Panties.  Hmmpph, none of those when you come to visit me.  Pull them aside and show me your pussy."
              wt_image club_blackmail_4
              player.c "Not wet.  Oh well, I'm hard, so at least I'm enjoying this.  Give me your contact details.  Once I have them, you can cover yourself up.  I'd hurry if I were you.  I think your husband might be looking this way."
              wt_image club_blackmail_initial_46
              tracy.c "Bastard!"
              "She hurriedly scribbles them down for you, then covers herself up and flees."
              $ tracy.opp = 4
              $ tracy.change_full_name("", "", "The Club Member")
              $ tracy.action_contact = living_room.add_action("Contact " + tracy.full_name, label = tracy.short_name + "_contact", context = "_contact_other", condition = "tracy.can_be_interacted and not tracy.has_tag('blackmail_complete')")
        "Nothing, her husband should simply know":
          player.c "I don't want anything other than to get this dirty secret off my chest."
          wt_image club_blackmail_initial_56
          tracy.c "You're going to fuck up our marriage!!"
          player.c "With what?  The truth?  If him knowing you were banging Sam fucks up your marriage, who's to blame here?"
          wt_image club_blackmail_initial_46
          tracy.c "Stop!  I'll tell him."
          "You don't know exactly what she tells him, but there's yelling and screaming and they go home with him looking very, very angry.  If she didn't tell the truth, she told him something nearly as unpleasant for him to hear."
          $ tracy.opp = 4
        "Nothing, stop tormenting her":
          player.c "Is it that important to you to keep this lie a secret?"
          wt_image club_blackmail_initial_56
          tracy.c "Yes.  Please!  You don't understand.  I'm not a bad person, really.  It's just ... please don't tell him."
          player.c "Okay, I won't.  I don't necessarily approve, but I guess this is between you and him."
          wt_image club_blackmail_initial_1
          "She sighs a sigh of relief."
          tracy.c "Thank you!  My name's Tracy, by the way."
          "You're pretty sure this isn't the last you'll hear from Tracy."
          $ tracy.opp = 2
          $ tracy.event_week = week + 3
          $ tracy.week_available = tracy.event_week
          $ tracy.change_full_name("", "Tracy", "the Club Member")
    "Cruel" if player.hypnosis_level > 0:
      player.c "Don't tell anybody? That sounds like you're trying to keep secrets. Why would you be wanting to keep secrets?"
      wt_image club_blackmail_initial_56
      "Her blush deepens."
      tracy.c "My husband doesn't approve of ..."
      player.c "Go on, spit it out.  What doesn't he approve of?"
      wt_image club_blackmail_initial_1
      tracy.c "Me being with women.  Please don't tell him."
      $ title = "What do you do?"
      menu:
        "Hypnotize her and have her share her secrets with the Club":
          $ tracy.hypno_session() #deducts energy and records she was hypnotized          $
          "There's no one nearby and the woman has been trying to keep anybody from noticing your conversation.  You can likely safely hypnotize her as long as you're quick about it."
          player.c "Tell you what, look at this while I think about it.  What did you say your name was?"
          wt_image club_blackmail_initial_56
          tracy.c "Tracy ..."
          call focus_image from _call_focus_image_33
          player.c "Listen to me, Tracy.  Look at this and listen to me.  Listen to me.  I am going to talk and you are going to listen.  Listen to me, Tracy.  Only to me.  Only my words now."
          wt_image club_blackmail_initial_56
          player.c "You shouldn't be keeping so many secrets, Tracy.  You shouldn't be keeping your breasts secret from me.  Stop being bad, Tracy, and bare your secrets to me."
          wt_image club_blackmail_initial_58
          player.c "It will feel good to get your secrets off your chest.  It will feel good to reveal your secrets.  Start with your breasts, Tracy.  Reveal them to me and you'll start to feel better."
          wt_image club_blackmail_initial_48
          player.c "That feels better, doesn't it, Tracy?  It feels good to reveal secrets."
          tracy.c "Yes"
          wt_image club_blackmail_initial_49
          player.c "It doesn't just feel good.  It feels great.  It feels great to show the world the secret things you've kept bottled up inside."
          tracy.c "Yeesss"
          wt_image club_blackmail_initial_48
          player.c "What have you been keeping bottled up inside, Tracy?  What secret has left you feeling bad inside because you can't tell the world?"
          wt_image club_blackmail_initial_59
          tracy.c "I'm gay.  I only married my husband because I was young and stupid and I didn't understand what I wanted and now I only stay with him because of my daughter and his money."
          player.c "Do you like having that secret bottled up inside you, Tracy?"
          wt_image club_blackmail_initial_49
          tracy.c "Noooo"
          wt_image club_blackmail_initial_60
          player.c "You're going to shed your secrets with your clothes, Tracy.  Remove your dress."
          wt_image club_blackmail_initial_61
          player.c "Your pussy is the source of your secrets, Tracy.  When you reveal your pussy, you're going to feel a sense of relief.  A sense of freedom.  You'll be able to share the terrible secrets you've kept locked up inside."
          wt_image club_blackmail_initial_52
          player.c "Look at your pussy, Tracy.  Open it and let your secrets out.  It feels so good to let your secrets out."
          tracy.c "Ohhh ... yeesss!!"
          wt_image club_blackmail_initial_62
          player.c "You can share your secrets with the world now, Tracy.  Share your secrets and your pussy with the world.  It will feel so good to you every time you do."
          tracy.c "I like to fuck girls, not boys.  I only stay with my husband for his money."
          wt_image club_blackmail_initial_53
          player.c "That feels good, doesn't it?  It feels so good to open yourself up and let your secrets out."
          tracy.c "Yeesss"
          wt_image club_blackmail_initial_63
          player.c "The wider you open yourself up, the better it will feel, Tracy.  Open yourself wide and let your secrets free.  It will feel so good when you do."
          wt_image club_blackmail_initial_55
          tracy.c "I like girls, not boys!  I only stay with my husband for his money!"
          "You leave Tracy alone to unburden herself of the secrets that are undermining her marriage.  Her willingness to do so after such simple hypnosis suggests she's been wanting to let her feelings out, though perhaps not quite like this."
          $ tracy.change_full_name("", "Tracy", "the Club Member")
          add tags "hypnotized_now" to tracy
          $ tracy.opp = 4
        "Nothing, let her keep her secret":
          player.c "Is it that important to you to keep this lie a secret?"
          wt_image club_blackmail_initial_56
          tracy.c "Yes.  Please!  You don't understand.  I'm not a bad person, really.  It's just ... please don't tell him."
          player.c "Okay, I won't.  I don't necessarily approve, but I guess this is between you and him."
          wt_image club_blackmail_initial_1
          "She sighs a sigh of relief."
          tracy.c "Thank you!  My name's Tracy, by the way."
          "You're pretty sure this isn't the last you'll hear from Tracy."
          $ tracy.opp = 2
          $ tracy.event_week = week + 3
          $ tracy.week_available = tracy.event_week
          $ tracy.change_full_name("", "Tracy", "the Club Member")
  rem tags 'in_club' from tracy
  return

## Character Specific Actions
# N/A

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
label tracy_contact:
  if player.has_item(dildo) and dungeon.has_item(gags):
    call tracy_contact_proceed from _call_tracy_contact_proceed
  else:
    if player.has_item(dildo) and not dungeon.has_item(gags):
      sys "If you owned a ballgag, you'd have more options about what to do with her. Then again, you have some options now."
    elif not player.has_item(dildo) and dungeon.has_item(gags):
      sys "If you had a dildo, you'd have more options about what to do with her. Then again, you have some options now."
    elif not player.has_item(dildo) and not dungeon.has_item(gags):
      sys "If you had a dildo or a ballgag, you'd have more options about what to do with her. Then again, you could always just fuck her."
      $ title = "Do you want to proceed?"
      menu:
        "Proceed":
          call tracy_contact_proceed from _call_tracy_contact_proceed_1
        "Wait until you have more equipment":
          pass
  return

label tracy_contact_proceed:
  $ tracy.training_session()
  "Turns out the Club member you blackmailed is named Tracy.  Not that her name matters.  Out of prudence, you decide it's best she not know where you live.  So you book a hotel room under her name for her to pay for and send her instructions on where and when to meet you."
  $ tracy.change_full_name("", "Tracy", "the Club Member")
  call forced_movement(outdoors) from _call_forced_movement_141
  summon tracy no_follows
  wt_image club_blackmail_coerce_5
  "She arrives wearing a plain, almost drab sundress.  She's clearly not dressing to impress you.  She may even be trying to dissuade you from taking an interest in her.  You watch her from the lobby as she heads up to the room.  You've left instructions for her on the bed."
  wt_image club_blackmail_coerce_6
  if player.hypnosis_level > 0:
    "She finds your letter to her, opens it up and reads it.  She's too resistant and on her guard about you to even attempt to hypnotize her, so you'll need to do something else with her."
  else:
    "She finds your letter to her, opens it up and reads it."
  $ title = "What are your instructions to her?"
  menu:
    "Dildo show" if player.has_item(dildo):
      player.c "{i}Remove your clothes and go to the bathroom. There's a vibrator there. You'll use it to pleasure yourself while I watch you. Climb up on the counter in front of the mirror so I can see you from every angle. You can start without me or wait for me to get there. Your choice.{i}"
      wt_image club_blackmail_coerce_7
      "She sits on the bed to finish reading your instructions.  She slips her dress off, then heads to the bathroom."
      wt_image club_blackmail_coerce_8
      "She's naked and waiting on the counter as you instructed when you arrive, doing her best to maintain her modesty in the circumstances."
      tracy.c "We don't have to do this.  I have money, I could pay you."
      call tracy_contact_proceed_ask_dildo from _call_tracy_contact_proceed_ask_dildo
      if tracy.has_tag('contact_forget_it'):
        wt_image club_blackmail_coerce_70
        player.c "Forget it. I don't want your money. I want to see your pussy, lowered onto that vibrator."
        "You give her a sharp swat on the ass ... *smack*"
        wt_image club_blackmail_coerce_64
        tracy.c "Ow!  Okay."
        wt_image club_blackmail_coerce_11
        "She lowers herself onto the sex toy as best she can ..."
        wt_image club_blackmail_coerce_12
        "... then pushes it in more firmly with her hand."
        wt_image club_blackmail_coerce_13
        "She stays like that, face turned away from you in shame."
        wt_image club_blackmail_coerce_71
        player.c "Cute, but turn around and hold your legs open so I have a better view."
        wt_image club_blackmail_coerce_14
        "She glares at you defiantly, but does as you say."
        wt_image club_blackmail_coerce_72
        tracy.c "Happy now?"
        wt_image club_blackmail_coerce_73
        $ title = "Happy now?"
        menu:
          "She still hasn't pleasured herself":
            wt_image club_blackmail_coerce_72
            player.c "Not yet.  Remember my instructions?  You're going to use the vibrator to pleasure yourself.  All the way to climax."
            wt_image club_blackmail_coerce_66
            tracy.c "You're kidding?  I can't cum with you watching me."
            wt_image club_blackmail_coerce_65
            player.c "Then we're going to be here a while. Just close your eyes and think of our mutual friend, Sam. And no trying to fake it. I saw the real thing when you were with Sam, remember? I know what your cums look and sound like, and I'm looking forward to finding out what they smell like."
            wt_image club_blackmail_coerce_74
            tracy.c "Fine. Try not to make any noise. If I can't pretend you're not here we really will be here all night."
            wt_image club_blackmail_coerce_15
            "She switches the vibrator on and runs it over her nipples ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_16
            "Before long, her little nubs have stiffened nicely."
            wt_image club_blackmail_coerce_17
            "Leaning back, she runs the vibrator across her sex ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_75
            "... before settling her attention on her clit.  Her breathing quickens and she starts to moan."
            wt_image club_blackmail_coerce_76
            tracy.c "mmmmmm  mmmm  oohhhhhh  mmmm"
            wt_image club_blackmail_coerce_77
            "Around, over and against her clit, she presses the buzzing sex toy as her body starts to tremble ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_19
            "When her orgasm hits, it hits quickly.  If its a fake, it's a good one, as her skin flushes and her stomach muscles twitch as cries out."
            wt_image club_blackmail_coerce_78
            tracy.c "mmmmm  ooohhh  ohhhh oh oh! oh!!  ohhhhhhhhhh"
            wt_image club_blackmail_coerce_74
            player.c "You can say 'thank you' now."
            wt_image club_blackmail_coerce_79
            tracy.c "For what?"
            player.c "For letting you have such a good time while we were together."
            wt_image club_blackmail_coerce_66
            tracy.c "Fuck you!"
            player.c "That's what I was thinking, although I'll settle for a hand job."
            wt_image club_blackmail_coerce_67
            tracy.c "No!"
            player.c "50 then, so I can get one from one of the working girls in the lobby.  You have me a bit worked up."
            wt_image club_blackmail_coerce_67
            tracy.c "Fine, but that's it.  You're not getting anything more from me."
            $ tracy.masturbation_count += 1
            $ tracy.orgasm_count += 1
          "You've seen enough":
            wt_image club_blackmail_coerce_72
            player.c "Yeah, I've seen enough.  Since you've been trying to buy me off, give me 50 and this is over."
            tracy.c "What?  Oh, fine!"
        wt_image club_blackmail_coerce_68
        "Fuming, she gets down off the counter, hands the dildo back, then dresses and provides instructions to have the money transferred to you."
        tracy.c "Asshole. If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
        wt_image club_blackmail_coerce_69
        "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
        player.c "Pleasure doing business with you. Have a good day. Think of me the next time you and a girlfriend play hide-the-dildo."
        "You'll clean the dildo off thoroughly and sanitize it when you get home, so it'll be clean to give to someone else."
        change player money by 50
        change player energy by -energy_short notify
    "Strip tease and then fuck":
      player.c "{i}I'll be up in a few minutes, and you're going to show me a good time. You're a whore and you're going to act like one. You'll tease me with a strip show to get me hard and then I'm going to fuck you. Make me happy and this is all over.{/i}"
      wt_image club_blackmail_coerce_69
      "She can't meet your eyes as you enter the room."
      tracy.c "Fine, I'm your whore for the evening.  This is a one time deal, understood?  Here's your strip show."
      wt_image club_blackmail_coerce_21
      "She finds the courage to glare at you as she turns around and lifts the back of her dress."
      wt_image club_blackmail_coerce_80
      player.c "Are you starting here because this is what you like to see when the showgirls dance at the Club, or did someone once tell you you have a nice ass and you think this is going to impress me?"
      wt_image club_blackmail_coerce_81
      tracy.c "I have absolutely no interest in 'impressing' you."
      wt_image club_blackmail_coerce_68
      player.c "You should.  The deal is you need to turn me on enough to be able to fuck your scrawny ass.  What else have you got to flash at me?"
      wt_image club_blackmail_coerce_82
      "Still glaring, she pulls down the top of her dress."
      player.c "Angry's a good look on you.  I think it's making your nipples hard.  Just as well, too.  You don't have much up to to look at otherwise.  Is that why you're attracted to Sam and other women, boob-envy?"
      wt_image club_blackmail_22
      tracy.c "Fuck you!"
      player.c "We'll get to that soon enough, assuming you're able to get me interested in you.  More teasing, less attitude."
      wt_image club_blackmail_coerce_83
      "She throws you a look of pure hate as she lifts a leg ..."
      wt_image club_blackmail_coerce_23
      "... then pulls her panties aside to expose her pussy."
      wt_image club_blackmail_coerce_84
      player.c "You forgot what I told you at the Club about not wearing panties when you came to see me.  Apparently you're not just my whore tonight, you're my stupid whore."
      wt_image club_blackmail_coerce_85
      "She's about to say something - probably another 'fuck you' - but bites her tongue."
      wt_image club_blackmail_coerce_86
      "Insted, she closes her eyes and pulls off the sundress ..."
      wt_image club_blackmail_coerce_24
      "... and sorta, kinda, almost offers her small breasts out to you in a way that might have been an attempt to look sexy."
      wt_image club_blackmail_coerce_87
      "Then before you have a chance to say anything, her clothes off except for the offending panties being back in place, she looks at you uncertainly.  It seems she's getting cold feet."
      tracy.c "You don't have to say it.  You don't need to comment on my tiny tits or my flat ass or my skinny legs.  I get what you're doing, you're humiliating me and it's worked.  We ... We don't have to go through with this.  You don't have to humiliate me more by ... doing anything with me.  I have money.  I could pay you."
      call tracy_contact_proceed_ask_strip from _call_tracy_contact_proceed_ask_strip
      if tracy.has_tag('contact_forget_it'):
        wt_image club_blackmail_coerce_89
        player.c "Forget it.  Your reluctant little ass is worth more than money.  Since that seems to be your best feature, get those panties off then bend over and hold yourself open for me."
        wt_image club_blackmail_coerce_26
        "Tracy sighs in frustration and helplessness, then holds herself open for your inspection."
        wt_image club_blackmail_coerce_90
        $ title = "Which hole do you want?"
        menu menu_club_blackmail_hole_menu:
          "Cunt":
            wt_image club_blackmail_coerce_91
            player.c "Let me take a closer look at your cunt."
            wt_image club_blackmail_coerce_92
            "She pulls herself wide open for inspection."
            $ title = "Fuck this hole?"
            menu:
              "Yes":
                wt_image club_blackmail_coerce_93
                player.c "Okay, I guess that hole will do.  Tell me how much better I am than your husband while I'm fucking you."
                wt_image club_blackmail_coerce_94
                "She winces as you mount her, but holds herself open to receive you anyway.  You get the sense she's used to being fucked when not excited herself, which makes you wonder about her marriage and why she's putting up with this to save it."
                wt_image club_blackmail_coerce_95
                "You don't wonder for long, though.  You're not able to convince her to comment on your performance versus her husband, either, but the sensation of fucking a woman who clearly despises you is too enjoyable to think about anything else.  She avoids eye contact as you rut her, her only active participation being to continue to hold herself open until you fill her with your seed."
                wt_image club_blackmail_coerce_96
                player.c "[player.orgasm_text]"
                wt_image club_blackmail_coerce_91
                player.c "That'll be a while before it all drips out of you, I left a big load in there.  Is that why you prefer fucking women, less clean up with your lesbian lovers?"
                wt_image club_blackmail_coerce_68
                tracy.c "You're not my lover, asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                wt_image club_blackmail_coerce_69
                "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
                player.c "Pleasure getting to know you.  Have a good day.  Remember me the next time your husband fucks you."
                $ tracy.sex_count += 1
                orgasm notify
              "Not yet":
                wt_image club_blackmail_coerce_93
                player.c "I can't decide.  Turn over and show me the options again."
                wt_image club_blackmail_coerce_90
                $ title = "Which hole do you want?"
                jump menu_club_blackmail_hole_menu
          "Anus":
            wt_image club_blackmail_coerce_97
            if not tracy.has_tag('hates_anal'):
              add tags 'hates_anal' to tracy
              player.c "Do you like anal, Tracy?"
              tracy.c "No, I hate it."
            else:
              player.c "Do you despise anal so much, you'd rather I defile your marriage by fucking the hole you should only use to make love to your husband?"
              tracy.c "Yes, I'd prefer you fuck my pussy, not my ass.  Is that what you wanted to hear me say?"
            $ title = "Fuck her ass?"
            menu:
              "Yes":
                wt_image club_blackmail_coerce_98
                player.c "Perfect.  Get down on the floor and lean forward onto the chair and I'll make this as long and unpleasant for you as I can."
                wt_image club_blackmail_coerce_27
                "She looks so nervous, you can't begrudge her the pillow she uses to kneel on.  You did, after all, promise that you were going to make this last."
                wt_image club_blackmail_coerce_99
                "As you prepare to violate her tight anus, you realize it'll be difficult to actually make this last very long, as her butt if going to feel too good gripping your cock.  You console yourself with the knowledge that however long you last, it'll feel like an eternity to Tracy."
                player.c "Open yourself up.  I can't even get the head of my cock inside you, the way you're clenched up rihgt now."
                wt_image club_blackmail_coerce_100
                "Tracy tries, but fails, to relax her sphincter.  She has a little more success in physically opening hr rosebudup, spreading her cheeks just enough to let you get started."
                wt_image club_blackmail_coerce_101
                "The fuck is hard and painful and although Tracy tries to fight back her tears, eventually they start to flow and the sight of that is enough to put you over the edge."
                player.c "[player.orgasm_text]"
                wt_image club_blackmail_coerce_102
                tracy.c "I think I'm bleeding!"
                player.c "A little bit.  You're good at keeping secrets from your husband, though.  I'm sure you'll be able to hide that from him until you heal."
                wt_image club_blackmail_coerce_68
                tracy.c "If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                wt_image club_blackmail_coerce_69
                "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
                player.c "Pleasure getting to know you.  Have a good day.  Remember me the next time you sit down."
                $ tracy.anal_count += 1
                orgasm notify
              "Not yet":
                wt_image club_blackmail_coerce_26
                player.c "I suppose it wouldn't seem as much like cheating on your husband if you didn't let me use your cunt.  Let me think about it some more."
                wt_image club_blackmail_coerce_90
                $ title = "Which hole do you want?"
                jump menu_club_blackmail_hole_menu
    "Tie herself to the bed" if dungeon.has_item(gags):
      player.c "{i}Remove your clothes and lie on the bed. There are ties for your legs and arms. Bind your legs first, then lie down and fasten your arms. I'll be there to use you soon. If you're not bound and helpless when I get there, I'll turn around and go straight to your husband.{/i}"
      wt_image club_blackmail_coerce_7
      "She sits on the bed to finish reading your instructions.  With trembling hands, she slips out of her dress."
      wt_image club_blackmail_coerce_31
      "She connects the first tie to her left foot ..."
      wt_image club_blackmail_coerce_32
      "... then she pauses and reads your instructions again, uncertain as to whether she can go through with this."
      wt_image club_blackmail_coerce_33
      "Eventually she sighs in frustration and helplessness, convincing herself that maybe it won't be that bad and that she can put up with whatever you have planned for her.  She ties her second foot and lies back to fasten her wrists."
      wt_image club_blackmail_coerce_34
      "That's the position you find her in when you walk in: tied spread-eagled to the bed like Nastassja Kinski in 'Cat People'."
      player.c "What a good obedient whore you are.  Does it excite you to be helpless like this, dirty girl?"
      wt_image club_blackmail_coerce_103
      "She ignores your question, choosing to plead with you instead, with her eyes and her words."
      tracy.c "Please!  Please, we don't have to go through with this.  I have money, I could pay you."
      call tracy_contact_proceed_ask_tied from _call_tracy_contact_proceed_ask_tied
      if tracy.has_tag('contact_forget_it'):
        wt_image club_blackmail_coerce_105
        player.c "Forget it.  Your tied up little pussy is worth more than money to me."
        wt_image club_blackmail_coerce_104
        tracy.c "No, please ..."
        wt_image club_blackmail_coerce_35
        player.c "Enough chit chat.  The only hole of yours you need open is the one between your legs and I'm going to fill that one soon, too."
        "She begins to panic as you push the ballgag into her mouth, but tied spreadeagled as she is, there's nothing she can do about it."
        tracy.c "mmppphhhh!!"
        wt_image club_blackmail_coerce_36
        player.c "That's right, screaming is useless now, but go ahead and try.  If you want, I can give you something to really scream about?"
        "Desperately she shakes her head 'no' back and forth."
        wt_image club_blackmail_coerce_107
        player.c "Going to be a good dirty whore for me then?"
        "She nods vigorously as tears start to stream down her face."
        if player.has_item(dildo):
          $ title = "Do you want to dildo her first or just fuck her?"
        else:
          $ title = "What now?"
        menu:
          "Give her a forced orgasm" if player.has_item(dildo):
            wt_image club_blackmail_coerce_40
            player.c "Good.  Good dirty whores get rewarded."
            "Tracy watches in disbelief as you strap the vibrator in place against her sex and turn it on ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_41
            "She doesn't want the infernal machine buzzing and throbbing against her sex. She doesn't want to be here, and she certainly isn't interested in having mechanical stimulation applied to her body ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_42
            "The continual, buzzing, vibrating throbbing against her sex, however, soon increases the bloodflow to her labia, and the moisture rises unbidden between her legs.  Her body's betrayal increases Tracy's shame at the position she finds herself in, making her hate the situation even more. She curses you under her breath and wills herself not to respond even as her hips start to twitch involuntarily ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_43
            "The hatred and resolve to deny you the sight of her responding can only take Tracy so far.  The vibrator continues to throb unrelentingly against her sex, stimulating her increasingly sensitive lips and clit.  When the orgasm hits her, she sits up as far as her bonds allow and screams into her gag, every muscle in her body tensing up as the climax is ripped from her unwilling body ... *bzzzzzzzzzzz*"
            wt_image club_blackmail_coerce_108
            tracy.c "mmmhhhhhhhhh!!"
            $ tracy.orgasm_count += 1
            wt_image club_blackmail_coerce_41
            $ title = "What now?"
            menu:
              "Fuck her now":
                wt_image club_blackmail_coerce_109
                "Her cunt is wet from the orgasm as you mount her.  She has absolutely no interest in having you between her legs, but the stimulation from the vibrator has her body ready for sex regardless of what her mind is thinking."
                wt_image club_blackmail_coerce_36
                "She tries to lie back and ignore you thrusting in and out of her, but you pull her head up and force her to acknowledge what's happening to her."
                player.c "Look at me while I fuck you, you dirty whore.  You're not fooling anyone.  You can feel my cock inside you, just like youre going to feel me fill your dirty whore cunt with my seed ... [player.orgasm_text]"
                wt_image club_blackmail_coerce_106
                "When you've finished filling her cunt with semen, you release her hands.  She avoids looking at you as she finishes untying herself, her emotions teetering between anger and shame."
                wt_image club_blackmail_coerce_68
                "Her voice is shaky as she dresses and finally works up the nerve to address you."
                tracy.c "If you ever approach me again, I'll sic the Club and the police on you and to hell with the consequences!"
                wt_image club_blackmail_coerce_69
                "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
                player.c "Pleasure getting to know you.  Have a good day.  Think of me the next time your husband fucks you."
                $ tracy.sex_count += 1
                orgasm notify
              "Release her":
                wt_image club_blackmail_coerce_35
                "You take out her gag and remove the vibrator."
                player.c "You can say 'thank you' now."
                wt_image club_blackmail_coerce_104
                tracy.c "For what?"
                player.c "For letting you have such a good time while we were together."
                wt_image club_blackmail_coerce_105
                tracy.c "Fuck you!"
                player.c "That's what I was thinking, but then I decided I'll settle for a hand job."
                wt_image club_blackmail_coerce_103
                tracy.c "No!"
                player.c "50 then, so I can get one from one of the working girls in the lobby.  You have me a bit worked up."
                wt_image club_blackmail_coerce_105
                tracy.c "Fine, but that's it.  You're not getting anything more from me."
                wt_image club_blackmail_coerce_106
                "Fuming, she finishes untying herself after you release her hands, then provides instructions to have the money transferred to you and dresses."
                wt_image club_blackmail_coerce_68
                tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
                wt_image club_blackmail_coerce_69
                "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
                player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide the dildo."
                change player money by 50
                change player energy by -energy_short notify
          "Fuck her":
            wt_image club_blackmail_coerce_109
            "She's scared, helpless and crying, and her cunt is dry as you shove yourself into her, which only makes her cry harder."
            wt_image club_blackmail_coerce_36
            "As you thrust yourself in and out of her, her body moistens slightly in self-defense, but she hates what you're doing to her with every fiber in her body.  Being unable to prevent you - knowing she has herself to blame for giving you this power over her - only makes her hate herself almost as much as she hates you. She tries to lie back and ignore you thrusting in and out of her, but you pull her head up and force her to acknowledge what's happening to her."
            player.c "Look at me while I fuck you, you dirty whore.  You're not fooling anyone.  You can feel my cock inside you, just like youre going to feel me fill your dirty whore cunt with my seed ... [player.orgasm_text]"
            wt_image club_blackmail_coerce_106
            "When you've finished filling her cunt with semen, you release her hands.  She avoids looking at you as she finishes untying herself, her emotions teetering between anger and shame."
            wt_image club_blackmail_coerce_68
            "Her voice is shaky as she dresses and finally works up the nerve to address you."
            tracy.c "If you ever approach me again, I'll sic the Club and the police on you and to hell with the consequences!"
            wt_image club_blackmail_coerce_69
            "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
            player.c "Pleasure getting to know you.  Have a good day.  Think of me the next time your husband fucks you."
            $ tracy.sex_count += 1
            orgasm notify
          "Let her go":
            wt_image club_blackmail_coerce_35
            "To her shock, you remove the ballgag."
            player.c "I think you've learned your lesson.  Are you going to cheat on your husband again?"
            wt_image club_blackmail_coerce_104
            tracy.c "No, never!  I promise."
            player.c "Good.  I'm going to let you up then you're going to send me 50 for this training session, then this is over."
            wt_image club_blackmail_coerce_103
            tracy.c "Yes, absolutely!  Thank you!"
            wt_image club_blackmail_coerce_185
            "She scrambles back into her clothes after you untie her, then provides instructions to have the money transferred to you."
            tracy.c "Thank you for not going through with this.  I learned my lesson.  I really did."
            wt_image club_blackmail_coerce_81
            "She probably means it.  At the vert least, she looks contrite as she leaves."
            player.c "Pleasure doing business with you.  Have a good day.  And thanks for the view."
            $ tracy.opp = 5
            change player money by 50
            change player energy by -energy_short notify
  rem tags 'contact_forget_it' from tracy
  add tags 'blackmail_complete' to tracy
  call character_location_return(tracy) from _call_character_location_return_494
  call forced_movement(living_room) from _call_forced_movement_142
  return

label tracy_contact_proceed_ask_dildo:
  $ title = "What do you say?"
  menu:
    "How much money?":
      tracy.c "I'll pay you 100."
      $ title = "What do you say?"
      menu:
        "Take 100":
          player.c "Okay, 100 it is."
          wt_image club_blackmail_coerce_68
          "Relieved, she gets down off the counter and dresses, then provides instructions to have the money transferred to you."
          tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
          wt_image club_blackmail_coerce_69
          "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
          player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
          change player money by 100
          change player energy by -energy_short notify
        "Demand more":
          player.c "Not enough."
          wt_image club_blackmail_coerce_64
          tracy.c "That's all I have!"
          player.c "You can't expect me to believe that a rich society lady like you doesn't have access to a lot more money than that."
          wt_image club_blackmail_coerce_65
          tracy.c "My husband controls all our finances."
          player.c "Then I'd suggest you not do anything to get him mad at you.  Or let him find out about anything that would get him mad at you."
          wt_image club_blackmail_coerce_67
          tracy.c "The only other money I have access to are 100 I set aside to buy a birthday present for our 6 year old daughter.  You can't expect me to give you that?"
          $ title = "What do you say?"
          menu:
            "Settle for 100":
              player.c "Oh fine. Buy your daughter her damn present.  Just send me the 100 and I'll be on my way."
              wt_image club_blackmail_coerce_68
              "Relieved, she gets down off the counter and dresses, then provides instructions to have the money transferred to you."
              tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
              change player money by 100
              change player energy by -energy_short notify
            "Take 200":
              player.c "200 it is."
              wt_image club_blackmail_coerce_66
              tracy.c "You're going to take my daughter's birthday money??"
              player.c "I'm sure you can find something of yours to sell.  You're showing off a few items right now that men would pay for access to. Would you like me to arrange some part time work for you?"
              wt_image club_blackmail_coerce_67
              tracy.c "No thank you!"
              wt_image club_blackmail_coerce_64
              "Fuming, she gets down off the counter, then dresses and provides instructions to have the money transferred to you."
              wt_image club_blackmail_coerce_68
              tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Remember to look me up the next time you need money.  That employment offer stands."
              change player money by 200
              change player energy by -energy_short notify
            "Forget it":
              add tags 'contact_forget_it' to tracy
        "Forget it":
          add tags 'contact_forget_it' to tracy
    "Forget it":
      add tags 'contact_forget_it' to tracy
  return

label tracy_contact_proceed_ask_strip:
  $ title = "What do you say?"
  menu:
    "How much money?":
      tracy.c "I'll pay you 100."
      $ title = "What do you say?"
      menu:
        "Take 100":
          player.c "Okay, 100 it is."
          wt_image club_blackmail_coerce_68
          "Relieved, she dresses then provides instructions to have the money transferred to you."
          tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
          wt_image club_blackmail_coerce_69
          "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
          player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
          change player money by 100
          change player energy by -energy_short notify
        "Demand more":
          player.c "Not enough."
          wt_image club_blackmail_coerce_25
          tracy.c "That's all I have!"
          player.c "You can't expect me to believe that a rich society lady like you doesn't have access to a lot more money than that."
          wt_image club_blackmail_coerce_87
          tracy.c "My husband controls all our finances."
          player.c "Then I'd suggest you not do anything to get him mad at you.  Or let him find out about anything that would get him mad at you."
          wt_image club_blackmail_coerce_25
          tracy.c "The only other money I have access to are 100 I set aside to buy a birthday present for our 6 year old daughter.  You can't expect me to give you that?"
          $ title = "What do you say?"
          menu:
            "Settle for 100":
              player.c "Oh fine. Buy your daughter her damn present.  Just send me the 100 and I'll be on my way."
              wt_image club_blackmail_coerce_68
              "Relieved, she dresses then provides instructions to have the money transferred to you."
              tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
              change player money by 100
              change player energy by -energy_short notify
            "Take 200":
              player.c "200 it is."
              wt_image club_blackmail_coerce_88
              tracy.c "You're going to take my daughter's birthday money??"
              player.c "I'm sure you can find something of yours to sell.  You're showing off a few items right now that men would pay for access to. Would you like me to arrange some part time work for you?"
              wt_image club_blackmail_coerce_87
              tracy.c "No thank you!"
              wt_image club_blackmail_coerce_68
              "Fuming, she dresses then provides instructions to have the money transferred to you."
              tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Remember to look me up the next time you need money.  That employment offer stands."
              change player money by 200
              change player energy by -energy_short notify
            "Forget it":
              add tags 'contact_forget_it' to tracy
        "Forget it":
          add tags 'contact_forget_it' to tracy
    "Forget it":
      add tags 'contact_forget_it' to tracy
  return

label tracy_contact_proceed_ask_tied:
  $ title = "What do you say?"
  menu:
    "How much money?":
      tracy.c "I'll pay you 100."
      $ title = "What do you say?"
      menu:
        "Take 100":
          wt_image club_blackmail_coerce_34
          player.c "Okay, 100 it is."
          wt_image club_blackmail_coerce_106
          "Relieved, she finishes untying herself after you release her hands, then provides instructions to have the money transferred to you and dresses."
          wt_image club_blackmail_coerce_68
          tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
          wt_image club_blackmail_coerce_69
          "She probably means it. You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
          player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
          change player money by 100
          change player energy by -energy_short notify
        "Demand more":
          player.c "Not enough."
          wt_image club_blackmail_coerce_104
          tracy.c "That's all I have!"
          player.c "You can't expect me to believe that a rich society lady like you doesn't have access to a lot more money than that."
          wt_image club_blackmail_coerce_34
          tracy.c "My husband controls all our finances."
          player.c "Then I'd suggest you not do anything to get him mad at you.  Or let him find out about anything that would get him mad at you."
          wt_image club_blackmail_coerce_103
          tracy.c "The only other money I have access to are 100 I set aside to buy a birthday present for our 6 year old daughter.  You can't expect me to give you that?"
          $ title = "What do you say?"
          menu:
            "Settle for 100":
              wt_image club_blackmail_coerce_34
              player.c "Oh fine.  Buy your daughter her damn present.  Just send me the 100 and I'll be on my way."
              wt_image club_blackmail_coerce_106
              "Relieved, she finishes untying herself after you release her hands, then provides instructions to have the money transferred to you and dresses."
              wt_image club_blackmail_coerce_68
              tracy.c "Thank you, I guess.  But if you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Think of me the next time you and a girlfriend play hide-the-dildo."
              change player money by 100
              change player energy by -energy_short notify
            "Take 200":
              player.c "200 it is."
              wt_image club_blackmail_coerce_104
              tracy.c "You're going to take my daughter's birthday money??"
              player.c "I'm sure you can find something of yours to sell.  You're showing off a few items right now that men would pay for access to.  Would you like me to arrange some part time work for you?"
              wt_image club_blackmail_coerce_105
              tracy.c "No thank you!  Let me go and I'll give you the damn money"
              wt_image club_blackmail_coerce_106
              "Fuming, she finishes untying herself after you release her hands, then provides instructions to have the money transferred to you and dresses."
              wt_image club_blackmail_coerce_68
              tracy.c "Asshole.  If you ever approach me again, I'll sic the Club on you and to hell with the consequences."
              wt_image club_blackmail_coerce_69
              "She probably means it.  You smile at her, which makes her even more infuriated.  She turns her head, refusing to meet your gaze."
              player.c "Pleasure doing business with you.  Have a good day.  Remember to look me up the next time you need money.  That employment offer stands."
              change player money by 200
              change player energy by -energy_short notify
            "Forget it":
              add tags 'contact_forget_it' to tracy
        "Forget it":
          add tags 'contact_forget_it' to tracy
    "Forget it":
      add tags 'contact_forget_it' to tracy
  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_tracy:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_tracy:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_tracy:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_tracy:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_tracy:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_tracy:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_tracy:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_tracy:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_tracy:
  "Best to save this for a paying client."
  return

# Give Ring of Secuality
label give_rs_tracy:
    "Really?  That's what you think her issue is?  You think she's not interested enough in other women?"
    return

# Use Water Bowl
label use_wb_tracy:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_tracy:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Client Engagement Ends
label tracy_end_training:
  pass
  return

# Start Day
label tracy_start_day:
    if day == 1 and not tracy.has_tag('husband_message_given') and (tracy.has_tag('husband_message_love_potion_pending') or tracy.has_tag('husband_message_prescription_pending') or tracy.has_tag('husband_message_transformation_potion_pending')):
        add tags 'husband_message_given' to tracy
        notify "You received a new message today."
        notify
        $ tracy.action_husband_message = living_room.add_action("Message from Tracy's Husband", label = tracy.short_name + "_husband_message", context = '_check_messages')
    elif tracy.reference == 1 and player.has_tag('rep_needed'):
        "Remembering that Tracy's husband agreed to act as a reference for you, you contact him."
        "He leaves a glowing review for you, boosting your reputation."
        $ tracy.reference = 2
        rem tags 'rep_needed' from player
        change player reputation by 1 notify
    return

# End Day
label tracy_end_day:
    rem tags 'in_club_now' 'hypnotized_now' from tracy
    call character_location_return(tracy) from _call_character_location_return_495 # no other locations she can be but Club
    return

# End Week
label tracy_end_week:
  ## Check for New Prospects - Rep 2 and Tracy Event? (Club Blackmail Woman)
  if player.reputation >= 2 and week > tracy.event_week and tracy.opp == 2 and player.has_tag('club_first_visit_complete'):
    $ tracy.opp = 3
    $ tracy.change_status("prospect")  ## this should now cause the normal check for possible minor clients to fire
    #$ tracy.action_show_message = living_room.add_action("Message from Tracy's Husband", label = tracy.short_name + "_message", context = '_check_messages')
    #notify "You received a new message today."
    #notify
  ## Relationship Maintenance - Club Blackmail Arrangement?
  if tracy.has_tag('arrangement'):
    $ tracy.lose_her_countdown -= 1
    if tracy.lose_her_countdown == 1:
      "You haven't had a session with Tracy recently.  Her resolve to stay away from other women may not last if she doesn't get a regular 'fix' at your place."
      "Better set up a session with her soon."
    elif tracy.lose_her_countdown < 0:
      "Oops.  You went too long between sessions with Tracy, and her husband caught her in an indiscretion."
      "He's not too happy about it, and cancels all future 'training' with you."
      $ tracy.change_status("rejected")
      #$ living_room.remove_action(tracy.action_contact)
      rem tags 'arrangement' from tracy
  return

## Club and Stage Labels
label tracy_club_call:
    # note: doesn't need to be restricted by whether player has been in club today yet or not; she'll be there until you talk to her
    if tracy.opp == 1:
        $ tracy.location = club
        add tags 'in_club_now' to tracy
    return

label tracy_club_send_home:
    call character_location_return(tracy) from _call_character_location_return_496 # she'll get called back when you return if you haven't yet spoken to her and event is still active
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
