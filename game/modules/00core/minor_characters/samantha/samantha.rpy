## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou and wife trainer

# Package Register
register samantha_pregame 10 in core as "Sam the Barista"

## NOTE: not sure how character ended up being called "samantha" in game engine, but no big deal
## for clarity, though, the character is Sam and should always be referred to as such; 'Samantha'is only used as her whore and domme name


# Pregame
label samantha_pregame:
  python:
  ## Constants
    model_credits += [('support', "Sam the Barista (Samantha Saint)")]
    model_credits += [('bit', "Sam's Ex (Emmanuelle London)")]
    model_credits += [('bit', "Daisy the Secretary (Mia Malkova)")]
    model_credits += [('bit', "Jesse the Domme (Jesse Jane)")]

    ## Character Definition
    # 0,64,0
    samantha = Person(Character("Sam", who_color="#004000", what_color="#004000", window_background = gui.dialogue_background_dark_font_color), "samantha", cut_portrait = True, prefix = "", suffix = "the Barista")

    # Other Characters
    # Navy
    samantha_slaver = Character("Slaver", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # Gray
    # samantha_slaver_contact = Character("Slaver Contact", who_color="#808080", what_color="#808080") # not needed as same person as samantha_whore_client_3
    # Wine
    samantha_ex = Character("Sam's Ex", who_color="#800040", what_color="#800040", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    police_officer = Character("Police Officer", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 128,64,0
    samantha_buyer = Character("Doll Buyer", who_color="#804000", what_color="#804000", window_background = gui.dialogue_background_dark_font_color)
    # 128,0,255
    samantha_jesse = Character("Jesse the Domme", who_color="#8000FF", what_color="#8000FF")
    # Teal
    samantha_domme_client_1_1 = Character("Sam's Domme Client #1-1", who_color="#005656", what_color="#00c4c4")
    # 255,0,128
    samantha_domme_client_1_2 = Character("Sam's Domme Client #1-2", who_color="#FF0080", what_color="#FF0080")
    # 0,0,64
    samantha_domme_client_2 = Character("Sam's Domme Client #2", who_color="#000040", what_color="#000040", window_background = gui.dialogue_background_dark_font_color)
    # Navy
    samantha_domme_client_3 = Character("Sam's Domme Client #3", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    samantha_whore_client_1 = Character("Sam's Whore Client #1", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # Navy
    samantha_whore_client_2 = Character("Sam's Whore Client #2", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # Dark Brown
    samantha_whore_client_3 = Character("Sam's Whore Client #3", who_color="#401A00", what_color="#401A00", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    samantha.action_talk = samantha.add_action("Talk to her", label="_talk", condition = "current_location == coffee_shop")
    samantha.action_maid_talk = samantha.add_action("Talk to her", label="_maid_talk", condition = "samantha.can_be_interacted and samantha.has_tag('maid') and not samantha.has_tag('first_maid_chat') and current_location == club")
    samantha.action_put_to_work = samantha.add_action("Put her to work", label="_put_to_work", condition = "samantha.can_be_interacted and samantha.has_tag('doll_examine_initial')")
    samantha.action_sell_her = samantha.add_action("Sell her", label="_sell_her", condition = "samantha.can_be_interacted and samantha.has_tag('doll_examine_initial')")
    samantha.action_take_her_out_to_play = samantha.add_action("Take her out to play", label="_take_her_out_to_play", condition = "samantha.can_be_interacted and samantha.has_tag('doll_examine_initial') and current_location == basement")
    samantha.action_check_outfit = samantha.add_action("Check her outfit", label="_check_outfit", condition = "samantha.can_be_interacted and samantha.has_tag ('maid') and samantha.has_tag('first_maid_chat') and current_location == club")
    samantha.action_thank = samantha.add_action("Discuss how she can thank you", label="_thank", condition = "samantha.can_be_interacted and samantha.has_tag ('maid') and samantha.has_tag('first_maid_chat') and not samantha.has_tag('maid_thank_complete') and current_location == club")
    samantha.action_contact_you_train_her_domme = living_room.add_action("Contact Sam to train her to be a Domme", label = samantha.short_name + "_contact_you_train_her_domme", context = "_contact_other", condition = "samantha.can_be_interacted and samantha.domme_status == 2 and samantha.discussed_domme_train_you_dom == 2 and samantha.domme_you_train_outfit == 0")
    samantha.action_contact_practice_on_you = living_room.add_action("Contact Sam to Domme practice on you", label = samantha.short_name + "_contact_practice_on_you", context = "_contact_other", condition = "samantha.can_be_interacted and samantha.domme_status == 2 and samantha.discussed_domme_train_you_sub == 2")
    samantha.action_contact_domme_actions = living_room.add_action("Contact Sam for Domme actions", label = samantha.short_name + "_contact_domme_actions", context = "_contact_other", condition = "samantha.can_be_interacted and samantha.domme_status == 3 and samantha.has_tag('domme')")
    samantha.action_contact_pimp = living_room.add_action("Contact Sam to pimp her out", label = samantha.short_name + "_contact_pimp", context = "_contact_other", condition = "samantha.can_be_interacted and samantha.whore_status == 3 and samantha.has_tag('whore')")
    samantha.action_view_selfies = bedroom.add_action("Sam the Barista's Selfies", label = samantha.short_name + "_review_files_selfies", context = '_computer_view_images', condition = "samantha.has_tag('selfies_available')")
    samantha.action_view_wedding_photo = bedroom.add_action("Sam the Barista's Wedding Photo", label = samantha.short_name + "_review_files_wedding", context = '_computer_view_images', condition = "samantha.has_tag('wedding_photos_available')")
    samantha.action_contact_make_trade = living_room.add_action("Make a trade", label = samantha.short_name + "_contact_make_trade", context = "_contact_other", condition = "samantha.slaver_events == 9 and not samantha.has_any_tag('no_trade', 'trade_complete')")

    ## Tags
    # Common Character Tags
    samantha.add_tags('first_visit', 'no_hypnosis', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # Coffee Shop
    # handled in 01-core.rpy and coffee_shop.rpy

    ## Other

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('samantha_start_day_early_events', priority = -20) # runs earlier than other start day events
    start_day_labels.append('samantha_start_day', priority = 5) # note: no need for priority = 5 here as it's the default
    start_day_labels.append('samantha_start_day_late_events', priority = 100) # runs later than other start day events, as it should be the last one to run before the normal day starts
    # note end_day and end_week labels do not need this command, only start_day labels; end_day and end_week are added automatically

    ########### VARIABLES ###########
    # Common Character Variables
    #samantha.add_stats_with_value('temporary_count') #auto-added
    samantha.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_masturbation_count', 'hypno_orgasm_count', 'hypno_sex_count', 'hypno_swallow_count', 'random_number')

    # Character Specific Variables
    samantha.add_stats_with_value('avalon_sales_status', 'club_presence', 'conversation_event', 'discussed_boys', 'discussed_domme_train_you_dom', 'discussed_domme_train_you_sub', 'discussed_submission', 'doll_return_week', 'domme_outfit', 'domme_status', 'domme_you_train_outfit')
    samantha.add_stats_with_value('slaver_doll_week', 'slaver_events', 'slaver_payment_week', 'slaver_plan', 'slaver_police_week', 'wedding_week', 'week', 'whore_outfit', 'whore_photos_sent', 'whore_status', 'whore_test_level', 'whore_train_day', 'whore_train_week')
    samantha.add_stats_with_value('breakup_week',value=8)
    samantha.add_stats_with_value('slaver_fee',value=600)

    # Barista Switch Variable
    samantha.add_stats_with_value('new_barista_switch')

  return

# Initial Contact Message
# OBJECT: Check Messages
# Messages - Message from Sam the Barista
label samantha_wedding_message:
  wt_image barista_wedding_announcement
  samantha.c "{i}Hi, it's me.  Sam.{/i}"
  samantha.c "{i}I just wanted you to know that my girlfriend and I are getting married!{/i}"
  samantha.c "{i}We're probably rushing it a bit, but after spending so much time apart when we were broken up, we never want to be apart again.{/i}"
  samantha.c "{i}We're doing the wedding at a resort, and its just for family and close friends, so no invitation. Sorry.{/i}"
  samantha.c "{i}But we both wanted to let you know, because your help is a big part of the reason we got back together. So thank you! I hope you're well.{/i}"
  samantha.c "{i}PS It was my idea to take our tops off for the photo I've attached. She's never been naked in front of a man, and the idea of me sending a topless photo of her to a man she's never met is totally humiliating her.  I've discovered that humiliating her turns her on even more than spanking her does, and I'm having lots of fun exploring that little kink of hers.{/i}"
  "You save the photo to your files.  You can always delete it later."
  # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
  # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
  # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
  # $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
  call convert(samantha, 'unavailable') from _call_convert_183
  add tags 'wedding_photos_available' 'married_girlfriend' to samantha
  return

# Messages - Photo from Sam the Barista
label samantha_message_photo:
  wt_image phone_1
  "You received a message from Sam."
  if samantha.whore_test_level == 0:
    wt_image barista_selfie_1
    samantha.c "{i}Hi.  It's me, Sam.  Here's the photo you asked for of what I look like under my clothes.  Let me know if you think I'm cut out for sexual concierge work or not.{/i}"
    $ samantha.whore_photos_sent = 1
    add tags 'selfies_available' to samantha
  elif samantha.whore_test_level == 1:
    wt_image barista_selfie_2
    samantha.c "{i}It's me, Sam, again.  I thought it over and I guess I can trust you with these.  Here's what my tits look like.{/i}"
    wt_image barista_selfie_3
    samantha.c "{i}Here's what my ass looks like.{/i}"
    wt_image barista_selfie_4
    samantha.c "{i}This is the best I could do to get a picture of my pussy for you.  So do you think I've got what it takes for sexual concierge work?{/i}"
    $ samantha.whore_photos_sent = 2
  $ title = "What do you tell her?"
  menu:
    "I'm certain you can do this work":
      "You send a quick response to her."
      player.c "Thanks for the photo, Sam.  I'm certain you can do this work.  I'll look after the marketing and logistics for you for a small cut."
      player.c "What do you want to call yourself, professionally?  It's typical in this line of business to use a pseudoname, something different than your real name. Something that inspires confidence in the client."
      "A few minutes later, she replies back."
      samantha.c "If you could look after the marketing, that would be great! Just let me know where I should be and when. I'm nervous about this whole thing, and not sure if I'll be any good at it, but I'm willing to give it a try."
      samantha.c "As for a professional name, how about, \"Samantha\"?"
      "It may take you a day or so to line up \"Samantha\"'s first client. You now have her contact information so you can reach her when you're ready for her."
      add tags 'trained_today' 'trained_this_week' to samantha # to keep whore events from triggering until next week
      $ samantha.whore_status = 3
      $ samantha.conversation_event = 13
      call convert(samantha, "whore") from _call_convert_8
    "I'll need to see more of you to know for sure":
      if samantha.whore_test_level == 0:
        "You send off a quick reply."
        player.c "{i}Thanks for the photo, Sam, but I still need to see more. I need to see what you look like naked, Sam. All of you.{/i}"
      elif samantha.whore_test_level == 1:
        "You send off a quick reply."
        player.c "{i}Thanks for the photos, Sam, but photos aren't enough. I need to see you naked in person, Sam. It's the only way I can tell for sure whether you're going to be suited for this type of work.{/i}"
      "A few minutes later, she replies."
      samantha.c "{i}Okay.  Let me think about it.{/i}"
      $ samantha.whore_test_level += 1
      $ samantha.whore_train_week = week
    "Maybe you're not cut out for this after all":
      "You send a quick response to her."
      player.c "{i}Hi Sam. I'm not sure you're really cut out for this work after all. Perhaps we should try and find a different career for you.{/i}"
      "A few minutes later, she replies back."
      samantha.c "{i}I was worried about that. I probably look too much like a lesbian to appeal to most guys. Maybe we could chat more, at the coffee shop, after we both have a chance to think of some new ideas?{/i}"
      $ samantha.whore_status = 5
      $ samantha.conversation_event = 7
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  return

# Client Rejected
#label samantha_rejected: # not needed
#  sys "You can no longer train [samantha.full_name]."
#  return

# Display Portrait
# CHARACTER: Display Portrait
label samantha_update_media:
    if samantha.has_tag('doll') and current_location == basement:
        $ samantha.change_image('barista_doll_2')
    elif samantha.has_tag('maid') and current_location == club:
        $ samantha.change_image('barista_club_job_3_26')
    elif current_location == coffee_shop and samantha.conversation_event >=2:
        if week >= samantha.breakup_week and samantha.conversation_event == 4:
            $ samantha.change_image('barista_coffee_1')
        else:
            $ samantha.change_image('barista_coffee_3')
    elif current_location == coffee_shop:
        $ samantha.change_image('barista_coffee_1')
    return


########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label samantha_examine:
  if samantha.has_tag('doll') and current_location == basement:
    if not samantha.has_tag('doll_examine_initial'):
      wt_image barista_doll_2
      "Alone in the basement, you can take your time examining Sam. There's no indication of who sent her. The only identifying mark you can find is on the back of her neck, where 'Bodywerks' is etched in the skin like a kind of trademark."
      "Her skin feels lifelike. Her nipples even swell with blood when you caress them, but she shows no other signs of life."
      player.c "Sam, can you hear me?"
      "There's no response.  You try again, a little louder."
      player.c "Can you hear me?"
      samantha.c "Unit 12639 can hear you, Sir."
      player.c "Sam, is that you?"
      "*silence*"
      player.c "Unit, repeat your designation."
      samantha.c "Unit 12639, Sir."
      $ title = "What do you want to call her?"
      menu menu_samantha_rename:
        "Sam the Pleasure Doll":
          $ samantha.change_full_name("", "Sam", "the Pleasure Doll")
          player.c "Unit 12639, from now on I will refer to you as Sam, and you will reply when I address you that way."
          samantha.c "Yes, Sir.  Unit 12639 will respond when you call Unit 12639 'Sam'."
        "Unit 12639":
          $ samantha.change_full_name ("","Unit 12639","")
        "Something else":
          $ title = "What do you want to call her?"
          $ samantha.name = renpy.input(_("What is [samantha.name]'s new name?"))
          $ samantha.suffix = renpy.input(_("What is [samantha.name]'s new title, if you want to give her one?"))
          $ samantha.change_full_name("", samantha.name, samantha.suffix)
          $ title = "Are you sure you want her new name to be '[samantha.full_name]'?"
          menu:
            "Yes":
              pass
            "No, choose something else":
              $ samantha.change_full_name("", "Sam", "the Pleasure Doll")
              $ title = "What do you want to call her?"
              jump menu_samantha_rename
          player.c "Unit 12639, from now on I will refer to you as [samantha.full_name], and you will reply when I address you that way."
          samantha.c "Yes, Sir.  Unit 12639 will respond when you call Unit 12639 '[samantha.full_name]'."
      add tags 'doll_examine_initial' to samantha
    else:
      "When you first met her, she served coffee. She serves more basic needs now."
  elif samantha.has_tag('maid') and current_location == club:
    "Sam's working at the Club, helping to tidy up.  She smiles when she sees you."
  elif current_location == coffee_shop:
    if week >= samantha.breakup_week and samantha.conversation_event >= 4 and samantha.conversation_event < 7:
      wt_image barista_coffee_4
      "Your normally perky neighborhood barista seems down serving coffee."
    else:
      "Your friendly neighborhood barista is busy serving coffee."
  return

# Talk to Character
label samantha_talk:
    if current_location == coffee_shop:
        if player.energy == player.max_energy:
            "You don't need another coffee."
        else:
            if player.money - player.min_money < 10:
                "You can't afford their overpriced swill."
            else:
                if not player.has_tag('first_coffee_message'):
                    add tags 'first_coffee_message' to player
                    "[player.first_coffee_message_text]"
                $ title = "Pay 10 to Regain 10 Energy?"
                menu:
                    "Pay up (costs 10)":
                        if not player.has_tag('coffee_already_today') and week > samantha.week:
                            add tags 'coffee_already_today' to player
                            call samantha_conversation from _call_samantha_conversation
                        else:
                            if week >= samantha.breakup_week:
                                if samantha.conversation_event == 5 or samantha.conversation_event == 6:
                                    wt_image barista_coffee_4
                                    "A glum looking Sam is busy with other customers as you get another coffee, and doesn't have time to chat."
                                elif samantha.conversation_event == 4:
                                    wt_image barista_coffee_1
                                    "Sam gets you another coffee, but doesn't have time to chat."
                                else:
                                    wt_image barista_coffee_3
                                    "Sam smiles at you as you get another coffee, but doesn't have time to chat."
                            else:
                                if samantha.conversation_event >= 2:
                                    wt_image barista_coffee_3
                                    "Sam smiles at you as you get another coffee, but doesn't have time to chat."
                                else:
                                    wt_image barista_coffee_1
                                    "Sam gets you another coffee, but doesn't have time to chat."
                        change player energy by 10
                        change player money by -10 notify
                    "No":
                        pass
        wt_image current_location.image
    else:
        "You have nothing to say to her here."
    return

label samantha_maid_talk:
    wt_image barista_club_job_3_1
    samantha.c "Hi!  There wasn't much to do around the house today, so Gloria asked if I could help tidy up the Club."
    wt_image barista_club_job_3_22
    samantha.c "She bought me this nice new uniform to wear so I would fit in, but I think the skirt is too short for me."
    player.c "It looks fine to me, Sam."
    wt_image barista_club_job_3_23
    samantha.c "Oh good!  Gloria said I didn't need to wear panties with it, but when I saw how short the skirt was, I put these on.  I think they go okay with the rest of the outfit."
    player.c "You should listen to Gloria, Sam."
    wt_image barista_club_job_3_24
    samantha.c "I know. I'm learning so much from her and her husband. Being in their house and in their bed, I get to hear how they handle negotiations, business contracts, staff issues, just about everything involved in the running of the Club."
    wt_image barista_club_job_3_25
    samantha.c "I don't think I could have got this experience from any other job.  I don't know how I could ever thank you for setting this up for me!"
    add tags 'first_maid_chat' to samantha
    return

label samantha_conversation:
  # first coffee
  if samantha.conversation_event == 0:
    wt_image barista_coffee_1
    "A busy barista gets you your coffee to go.  Her name tag says her name is 'Sam'."
    samantha.c "Here you go."
    wt_image barista_coffee_4
    "She quickly hands the coffee to you and moves on to the next customer."
    $ samantha.conversation_event += 1
  # second coffee
  elif samantha.conversation_event == 1:
    wt_image barista_coffee_1
    "Sam prepares your order without making eye contact."
    samantha.c "Here's your coffee."
    wt_image barista_coffee_4
    "She hands the drink over to you and moves on to the next customer before you have a chance to say anything."
    $ samantha.conversation_event += 1
  # third coffee, now regular
  elif samantha.conversation_event == 2:
    wt_image barista_coffee_1
    "Sam fills your order again today."
    wt_image barista_coffee_2
    samantha.c "You're becoming a regular."
    "She gives you a quick smile, then wipes her hands on her apron and moves on to the next customer."
    $ samantha.conversation_event += 1
  # fourth coffee, conversation options
  elif samantha.conversation_event == 3:
    wt_image barista_coffee_3
    "Sam smiles at you as she hands you your coffee."
    call samantha_conversation_chat_initial from _call_samantha_conversation_chat_initial
    $ samantha.conversation_event += 1
  # on-going up to and including break up week, with conversation options if not yet revealed lesbian
  elif samantha.conversation_event == 4:
    if week >= samantha.breakup_week:
      wt_image barista_coffee_4
      "Sam seems down. She isn't her normal, perky self as she prepares your coffee."
      call samantha_conversation_chat_breakup from _call_samantha_conversation_chat_breakup
    else:
      wt_image barista_coffee_3
      if not samantha.has_tag('revealed_lesbian'):
        "Sam smiles at you as she hands you your coffee."
        call samantha_conversation_chat_initial from _call_samantha_conversation_chat_initial_1
      else:
        "Sam smiles as she hands you your coffee."
        player.c "How are you today?"
        samantha.c "Great!"
        player.c "How's your girlfriend?"
        wt_image barista_coffee_2
        samantha.c "She's amazing. I don't want to jinx things, but I think she may be 'the one', if you know what I mean? Thanks for asking."
  # opportunity to investigate helping her out post break up
  elif samantha.conversation_event == 5:
    wt_image barista_coffee_4
    "Sam still seems really down."
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        pass
      "Offer to set her up with someone" if not samantha.has_tag('discussed_setting_her_up_with_a_girl'):
        call samantha_setup_with_someone from _call_samantha_setup_with_someone
      "Ask her for a date" if samantha.discussed_boys == 0 and not samantha.has_tag('asked_for_date_after_break_up'):
        call samantha_ask_for_date from _call_samantha_ask_for_date
      "Ask about her ambitions":
        player.c "Still down about the break up?"
        samantha.c "Yeah"
        player.c "Still thinking about what your ex said?"
        wt_image barista_coffee_5
        samantha.c "I have a hard time thinking about anything else these days."
        player.c "So what do you want to do, Sam? If you don't want to be a barista forever, what are your ambitions? Sounds like you've been thinking about it a lot."
        samantha.c "I have. But I don't have a good answer. I want a better job. Something that could lead somewhere, maybe pay better than this job. But I don't know what that is."
        player.c "Maybe I could help you figure that out?"
        samantha.c "What are you, a guidance counselor?"
        player.c "Sort of."
        samantha.c "Well, I can't pay for professional help, I'm afraid. As my ex pointed out, I'm working minimum wage for tips and barely covering expenses, with nothing saved for a rainy day."
        player.c "Perhaps I can still help."
        samantha.c "That's sweet of you. I'll think about it."
        wt_image barista_coffee_1
        "Sam gets you your coffee then moves on to the next customer."
        $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
        $ samantha.conversation_event += 1
      "After today, look for a new barista (Stop going to Sam)":
        call samantha_look_for_new_barista from _call_samantha_look_for_new_barista
  # opp to help her out after discussing ambitions
  elif samantha.conversation_event == 6:
    wt_image barista_coffee_4
    "Sam still seems really down."
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        pass
      "Offer to set her up with someone" if not samantha.has_tag('discussed_setting_her_up_with_a_girl'):
        call samantha_setup_with_someone from _call_samantha_setup_with_someone_1
      "Ask her for a date" if samantha.discussed_boys == 0 and not samantha.has_tag('asked_for_date_after_break_up'):
        call samantha_ask_for_date from _call_samantha_ask_for_date_1
      "Talk about her sex life" if samantha.discussed_submission == 1 or samantha.discussed_boys < 3:
        call samantha_sex_life from _call_samantha_sex_life
      "Ask how her thinking is going":
        call samantha_ask_how_thinking_going from _call_samantha_ask_how_thinking_going
      "After today, look for a new barista (Stop going to Sam)":
        call samantha_look_for_new_barista from _call_samantha_look_for_new_barista_1
  # opp to suggest new careers after discussing school and what good at through her thinking conversation
  elif samantha.conversation_event == 7:
    wt_image barista_coffee_3
    "Sam seems to be getting back to her old self."
    samantha.c "Hi!"
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        pass
      "Offer to set her up with someone" if not samantha.has_tag('discussed_setting_her_up_with_a_girl'):
        call samantha_setup_with_someone from _call_samantha_setup_with_someone_2
      "Ask her for a date" if samantha.discussed_boys == 0 and not samantha.has_tag('asked_for_date_after_break_up'):
        call samantha_ask_for_date from _call_samantha_ask_for_date_2
      "Talk about her sex life" if samantha.discussed_submission == 1 or samantha.discussed_boys < 3:
        call samantha_sex_life from _call_samantha_sex_life_1
      "Suggest a new career":
        call samantha_suggest_new_career from _call_samantha_suggest_new_career
      "After today, look for a new barista (Stop going to Sam)":
        call samantha_look_for_new_barista from _call_samantha_look_for_new_barista_2
  # follow up on Avalon Lady
  elif samantha.conversation_event == 8:
    wt_image barista_coffee_2
    samantha.c "I was thinking about what you suggested, about becoming an Avalon Lady. Do you really think I could make a career of that? I mean, would the money be good enough to support me? Is it something I could do long term?"
    player.c "You won't know until you try, Sam. But can you make more money doing that than slinging coffee? Yes. Can you make a long term career out of it? I expect you can, if you like it. Or maybe it leads to another sales job down the road."
    player.c "What's the worst that could happen? It doesn't work out and you have to go back to being a barista. Do you think you'd have any trouble getting another barista job if you had to?"
    wt_image barista_coffee_3
    samantha.c "No. You're right. I'm going to go for it!"
    "An excited Sam turns back to finish up one of her last shifts at the coffee shop. "
    $ samantha.new_barista_switch = 1
    $ samantha.avalon_sales_status = 1
  # first follow up on Domme
  elif samantha.conversation_event == 9:
    wt_image barista_coffee_2
    if samantha.domme_status == 0:
      samantha.c "I've been thinking about what you suggested to me.  About being a Domme."
      samantha.c "I just wouldn't know what to do. I've spanked my ex, but I wouldn't know the first thing about really dominating someone."
      player.c "You just need some training."
      samantha.c "Where would I get that?"
      $ samantha.temporary_count = 1
      while samantha.temporary_count == 1:
        $ title = "What do you suggest?"
        menu:
          "You could practice on me" if samantha.discussed_domme_train_you_sub == 0:
            player.c "You could practice on me. I'll tell you what you're doing right, what you're doing wrong. Explain to you what a submissive it looking for."
            samantha.c "I don't know. If I'm supposed to be in charge, I'm not sure how well it would work, constantly checking with you about whether I'm doing things right.  Plus I might hurt you ... not in a good way, I mean really hurt you while I'm learning."
            $ samantha.discussed_domme_train_you_sub = 1
          "I could train you" if samantha.discussed_domme_train_you_dom == 0:
            player.c "I could train you. You submit to me, and I'll show you how submissives like to be treated. I'll show you what to do and how to do it, and you'll experience what your future clients will experience.  That way, you'll have a proper understanding of what you're doing for them."
            samantha.c "I don't know. Is this something you have much experience in? I'm guessing most of my clients would be men. Do you know how to dominate men properly?"
            if player.has_tag('dominant'):
              "You don't say anything. You just give her a look. Your good look. After a moment, she continues."
              samantha.c "You're really sure you'll be able to teach me what I need to know?"
              "You continue to hold her eyes with yours."
              wt_image barista_coffee_3
              samantha.c "Okay. I guess we could try."
              player.c "Give me your phone number. I'll call you when I'm ready to begin your training."
              wt_image barista_coffee_2
              "She hands over her number with your coffee."
              $ samantha.temporary_count = 0
              $ samantha.conversation_event = 10
              $ samantha.discussed_domme_train_you_dom = 2
              $ samantha.domme_status = 2
            else:
              player.c "I have quite a bit of experience in training women, Sam."
              samantha.c "Really? But training like this? Wouldn't it be better if I learned from a woman? Someone who already knows what these men are looking for. Someone who can show me, as a woman, what I should be doing with them."
              $ samantha.discussed_domme_train_you_dom = 1
          "I have a slavegirl you can practice on" if not samantha.has_tag('discussed_domme_train_your_slavegirl') and player.slavegirl_count > 0:
            player.c "I have a slavegirl you can practice on. I'll show you how to dominate her, then I'll let you try your hand with her."
            samantha.c "I don't know. That sounds like I'd be butting in on your relationship with her. I'm not interested in getting into some kinky threesome with you and your girlfriend."
            add tags 'discussed_domme_train_your_slavegirl' to samantha
          "I know a Domme" if not samantha.has_tag('discussed_domme_train_your_dommme') and player.domme_count > 0:
            player.c "I know a Domme who would be able to 'show you the ropes', so to speak."
            wt_image barista_coffee_3
            samantha.c "Oh? Does she have a lot of experience at this?"
            player.c "Not a lot of experience yet, no. She's just recently discovered her Domme side."
            samantha.c "Is she a professional? I mean, has she helped clients for money, the way you think maybe I could?"
            player.c "Not that I know of, no."
            wt_image barista_coffee_2
            samantha.c "I'm not sure that working with her would give me the confidence I need to try this line of work."
            add tags 'discussed_domme_train_your_dommme' to samantha
          "I can find someone to train you":
            player.c "I could find you someone. Someone to train you, and show you what your clients are going to want."
            wt_image barista_coffee_3
            samantha.c "An experienced Domme? Someone who knows what they're doing? I'd really rather learn from a woman, someone who can show me, as a woman, what will be expected of me. Someone who's done this professionally themselves."
            player.c "I'll see what I can do."
            wt_image barista_coffee_2
            samantha.c "But wouldn't an experienced Domme be worried about more competition? I mean, why would they help me, if they could just look after these people themselves?"
            $ title = "What do you say?"
            menu:
              "I'm sure I'll find someone":
                player.c "I'm sure I can find you someone."
                samantha.c "Okay.  Let me know if you do."
                "She hands over your coffee and goes back to her current job."
                $ samantha.temporary_count = 0
                $ samantha.domme_status = 1
                $ cassandra.discuss_barista = 3
              "Maybe this wasn't such a good idea":
                player.c "Maybe this wasn't such a good idea."
                wt_image barista_coffee_1
                samantha.c "Maybe not. I'm not confident that I'd be good at this type of work."
                player.c "Perhaps we can find something better for you."
                wt_image barista_coffee_2
                "She smiles and hands over your coffee."
                $ samantha.temporary_count = 0
                $ samantha.conversation_event = 7
          "Maybe this wasn't such a good idea":
            player.c "Maybe this wasn't such a good idea."
            wt_image barista_coffee_1
            samantha.c "Maybe not. I'm not confident that I'd be good at this type of work."
            player.c "Perhaps we can find something better for you."
            wt_image barista_coffee_2
            "She smiles and hands over your coffee."
            $ samantha.temporary_count = 0
            $ samantha.conversation_event = 7
    else:
      samantha.c "Hi. Have you found someone to train me?"
      $ title = "What do you suggest?"
      menu:
        "I have the perfect solution" if cassandra.discuss_barista == 4:
          player.c "I have the perfect solution for you, Sam. A woman named Jesse. She used to help out clients with these issues, but is now out of that business. She'd love to 'show you the ropes', so to speak. In fact, I told her a bit about you, and she's very eager to help teach you what you need to know."
          wt_image barista_coffee_3
          samantha.c "Wow. That sounds great. How much will I need to pay her?"
          player.c "Nothing. She's more than happy to help out someone new trying to break into the profession. The only thing is, you will need to listen to her, and follow her instructions."
          samantha.c "Of course."
          player.c "She needs to show you what it means to be a sub, first. You can't properly help the clients who come to you until you understand what they are going to experience. So she'll show you how to be a Domme by using you as her pretend client."
          samantha.c "Okay. That makes sense. Will you set the training up?"
          player.c "Give me your number, and I'll call you when Jesse is ready."
          wt_image barista_coffee_2
          "Sam hands over her number with your coffee."
          $ samantha.domme_status = 2
          $ samantha.conversation_event = 10
          $ samantha.action_contact_jesse_trains_her_domme = living_room.add_action("Contact Jesse To Train Samantha To Be A Domme", label = samantha.short_name + "_contact_jesse_trains_her_domme", context = "_contact_other", condition = "samantha.can_be_interacted and samantha.domme_status == 2 and cassandra.discuss_barista != 5")
        "Not yet" if cassandra.discuss_barista != 4:
          player.c "Not yet, but I'm still looking."
          "She smiles and hands over your coffee."
        "Maybe this wasn't such a good idea":
          player.c "Maybe this wasn't such a good idea."
          wt_image barista_coffee_1
          samantha.c "Maybe not. I'm not confident that I'd be good at this type of work."
          player.c "Perhaps we can find something better for you."
          wt_image barista_coffee_2
          "She smiles and hands over your coffee."
          $ samantha.conversation_event = 7
  # holding pattern on Domme when haven't finished training yet
  elif samantha.conversation_event == 10:
    player.c "How are you today Sam?"
    wt_image barista_coffee_5
    samantha.c "Still nervous about this whole Domme thing. I'm not sure its going to be right for me."
    player.c "Let's give it a try and see how it works out, okay?"
    wt_image barista_coffee_1
    samantha.c "Okay"
    "She hands over your coffee and moves on to the next customer."
  # resolution after successful Domme training
  elif samantha.conversation_event == 11:
    wt_image barista_coffee_3
    "An excited looking Sam brings over your coffee."
    samantha.c "There you are! I have great news!"
    wt_image barista_domme_ex_1
    samantha.c "I did a lot of thinking about the Domme sessions you set up for me, and how I felt about them and myself and the clients.  Then I went to my ex's and asked her if she was seeing anyone."
    samantha_ex "{i}No{/i}"
    samantha.c "{i}Good. I've been working on improving myself and doing something with my life.{/i}"
    samantha_ex "{i}What?{/i}"
    samantha.c "{i}Trying out a new career. Getting more confident in myself and my abilities. Getting better at being the right girlfriend for you.{/i}"
    samantha_ex "{i}What do you mean?{/i}"
    samantha.c "{i}You're going to let me in, and then you're going to go to the bedroom and take off your clothes. I've missed you.{/i}"
    samantha.c "{i}I've missed not having you to hold at night. I've missed not having you around to fuck when I get horny.{/i}"
    samantha.c "{i}I'm going to punish you for leaving me and leaving me horny and missing you. Then I'm going to fuck you. Then we're going to talk about our future together.{/i}"
    samantha_ex "{i}Sam, you can't be serious.{/i}"
    samantha.c "{i}I'm very serious. Lower your eyes and do what you're told. You don't get to look at me again until I'm finished punishing you. Do you understand?{/i}"
    wt_image barista_domme_ex_2
    samantha_ex "{i}Yes{/i}"
    samantha.c "{i}It's 'Yes, Mistress' from now on when we're playing. Understood?{/i}"
    samantha.c "She only hesitated a moment before answering."
    samantha_ex "{i}Yes, Mistress.{/i}"
    wt_image barista_domme_ex_3
    samantha.c "I followed her to the bedroom and watched her as she undressed. She tried to keep her eyes lowered, but she couldn't help herself from sneaking a quick peek at me as she started to take off her bra."
    samantha.c "{i}Did I tell you you could look at me yet?{/i}"
    samantha_ex "{i}No{/i}"
    wt_image barista_domme_ex_4
    samantha.c "{i}No what?{/i}"
    samantha_ex "{i}No, Mistress. I'm sorry, Mistress.{/i}"
    wt_image barista_domme_ex_5
    samantha.c "{i}Were you looking to see if I was drooling over your tits? Did you think the sight of your naked tits would excite me?{/i}"
    samantha_ex "{i}No, Mistress. I mean, yes Mistress, I hope so, Mistress.{/i}"
    samantha.c "{i}Lie back. Let's get these panties off of you.{/i}"
    wt_image barista_domme_ex_6
    samantha.c "{i}They're soaked! I think you're the excited one. Are you happy to see me again?{/i}"
    samantha_ex "{i}Yes, Mistress. Very happy!{/i}"
    wt_image barista_domme_ex_7
    samantha.c "{i}I'm happy to see you again, too. But I'm still going to punish you for keeping us apart. I'm going to hurt you now, and you're going to let me. Just nod to agree.{/i}"
    "She nodded as best she could with my hand pinning her head down against the bed."
    wt_image barista_domme_ex_8
    samantha.c "{i}Such a pretty pussy. All those times you asked me to spank your ass, were you ever hoping inside that I'd spank your pussy instead?{/i}"
    wt_image barista_domme_ex_9
    samantha.c "*SMACK* *SMACK* *SMACK* I starting whacking her bare sex."
    samantha_ex "{i}Aarrgggh!!{/i}"
    samantha.c "{i}That hurts, doesn't it? And that's only 3. Imagine how much it's going to hurt by the time I get to 20 ... and 30.{/i}"
    wt_image barista_domme_ex_10
    samantha.c "I kept at her for quite a long time. Maybe longer than I should have, because I don't think she's a masochist, she just has a submissive streak. When I finally stopped, she was pretty out of it."
    samantha.c "{i}Awwww. Is that little pussy of yours sore now? Would you like Mistress to make it feel better?{/i}"
    "She made a few guttural sounds behind her panties, but I couldn't tell you exactly what they meant."
    wt_image barista_domme_ex_11
    samantha.c "She started to come back to me when I shoved a finger in her twat. She'd dried up during the pussy spanking, but she got wet again really fast as I finger fucked her."
    wt_image barista_domme_ex_12
    samantha.c "I wanted to listen to her cum, so I pulled the panties out of her mouth. A couple of sharp pinches to her nipples and she came like a fountain all over my fingers."
    samantha_ex "{i}Oooohhhhhh  AAAHHHH!!!!{/i}"
    wt_image barista_domme_ex_13
    samantha.c "Then it was my turn. I laid back and pulled her head down between my legs."
    wt_image barista_domme_ex_14
    samantha.c "I kept her there for at least three orgasms. To be honest, I lost count. It'd been so long since I felt her talented tongue against my clit, I didn't want the sensation to ever end."
    wt_image barista_domme_ex_15
    samantha.c "When I finally felt like I didn't have another orgasm left in me, I pulled her up and kissed her. Kissed her both hard and soft, gently and like an animal, the way I'd wanted to kiss her when I first saw her standing there as she opened the door for me."
    samantha.c "The taste of my own pussy juice on her lips. The adoring way she looked at me between half closed eyes. It all made for the best kiss I'd ever had in my whole life."
    wt_image barista_domme_ex_16
    "A long line up has built up behind you. Sam hasn't lowered her voice, so they're all listening to her tale with a mix of fascination and awkward voyeurism."
    wt_image barista_coffee_3
    samantha.c "Oh, don't worry about them. This is almost my last shift here anyway. My ex is taking a new job in a new city. We reconciled just in time!"
    samantha.c "We talked, and we've decided we both agree that we belong together. So I'm going to join her."
    samantha.c "I don't know yet what I'm going to do career-wise. I don't mind being a Domme with her, but I'm not sure I can do it professionally. It's just so personal and emotionally draining."
    samantha.c "But I'll do something interesting, even if I don't yet know what it'll be. Thanks for helping me to learn that I can be more than a barista!"
    wt_image barista_coffee_2
    "With that, she hands over your now almost cold coffee. You probably won't see her again, but at least she left you an interesting story to remember her by."
    call unconvert(samantha, 'domme') from _call_unconvert
    $ samantha.new_barista_switch = 1
    $ samantha.wedding_week = week + 4
  # follow up on sex work
  elif samantha.conversation_event == 12:
    if samantha.whore_status == 2:
      "Sam seems to be avoiding you. Perhaps she's still debating whether or not to send you visual evidence of her suitability for work as a sexual concierge, and doesn't want to face you until she makes up her mind."
    else:
      wt_image barista_coffee_2
      samantha.c "I've been thinking about what you suggested to me. About being a sexual concierge. Do you think people would really pay me for that? Men I mean. I'm so clearly lesbian. Wouldn't that turn a lot of men off?"
      player.c "I am absolutely certain your sexual orientation will not be an issue."
      samantha.c "Okay. If you think so. But do you really think I'd be qualified to do that work? Would men really want to spend time with me, sexually?"
      $ title = "What do you tell her?"
      menu:
        "I'm certain you can do this work":
          player.c "I'm certain you can do this work, Sam. I can look after the marketing and logistics for you for a small cut."
          wt_image barista_coffee_3
          samantha.c "Could you? That would be great."
          player.c "What do you want to call yourself?  Professionally?"
          samantha.c "What do you mean?"
          player.c "It's typical in this line of business to use a professional name. Something different than your real name. Something that inspires confidence in the client."
          wt_image barista_coffee_2
          samantha.c "Hmmm.  How about 'Samantha'?"
          "You do your best to stifle a reaction."
          player.c "Uh, okay. Sure. Give me your number and I'll let you know when I have your first client lined up. It may take a day or so."
          wt_image barista_coffee_3
          samantha.c "Okay. If you think I can do this. Let's give it a try."
          "She hands over her number with your coffee."
          $ samantha.whore_status = 3
          $ samantha.conversation_event = 13
          call convert(samantha, "whore") from _call_convert_9
        "I'll need to see more of you to know for sure":
          player.c "I'll need to see more of you, Sam, to know for sure."
          samantha.c "What do you mean?"
          player.c "Men are very visual. Before I can help get you clients, I need to know that you're going to appeal to them."
          samantha.c "But you can see what I look like."
          player.c "Not enough of you. I need to see more. Here's my contact information. Contact me when you're ready for an inspection."
          player.c "Don't worry. I'm sure you'll be fine. I just can't represent you in good conscience without knowing for sure what you have to offer to these men."
          player.c "You are a lesbian after all. I need to make sure your looks aren't going to throw prospective clients off."
          wt_image barista_coffee_1
          samantha.c "Okay, I guess that makes sense.  I'll think about it."
          "She hands over your coffee."
          $ samantha.whore_status = 2
          $ samantha.whore_train_day = day + 1
          if samantha.whore_train_day > 4:
            $ samantha.whore_train_day = 1
  # holding pattern on sex work when haven't completed training yet
  elif samantha.conversation_event == 13:
    wt_image barista_coffee_1
    player.c "How are you today Sam?"
    wt_image barista_coffee_5
    samantha.c "Still nervous about this whole sexual concierge thing. I'm not sure its going to be right for me."
    player.c "Let's give it a try and see how it works out, okay?"
    samantha.c "Okay"
    "She hands over your coffee and moves on to the next customer."
  # resolution of sex work and opening of slaver options
  elif samantha.conversation_event == 14:
    wt_image barista_coffee_1
    player.c "Hi, Sam."
    wt_image barista_coffee_5
    samantha.c "Hi. Thanks for giving me some time to think."
    samantha.c "I hope you're not going to be mad, but I can't do the sexual concierge work any more. I appreciate you suggesting it to me and helping me try it, and I do think I could be good at it."
    samantha.c "I just don't feel like it's the right career for me. Maybe if I was straight I could relate more to these men and want to help them out. Because they definitely do need help."
    samantha.c "But I just don't feel right, about myself, after spending time with them."
    player.c "Perhaps we should try finding something else for you?"
    wt_image barista_coffee_2
    samantha.c "I'd like that!"
    "She hands over your coffee and moves on to the next customer."
    add tags 'former_whore' to samantha
    call unconvert(samantha,'whore') from _call_unconvert_16
    $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
    $ samantha.slaver_events = 1
    $ samantha.conversation_event = 7
  # waiting on Gloria
  elif samantha.conversation_event == 15:
    wt_image barista_coffee_3
    samantha.c "Have you spoken to your friend? About that job opportunity?"
    $ title = "What do you tell her?"
    menu:
      "Not yet":
        player.c "Not yet."
        wt_image barista_coffee_2
        samantha.c "Okay. Let me know what you find out.?"
        "Sam hands over your coffee then moves on to the next customer."
      "I've reconsidered":
        player.c "I've been thinking about that. I'm not sure that's the right position for you."
        wt_image barista_coffee_5
        samantha.c "Oh. That's too bad. It sounded interesting."
        player.c "Leave it with me.  We'll find you something."
        wt_image barista_coffee_2
        samantha.c "Okay"
        "Sam hands over your coffee then moves on to the next customer."
        $ samantha.conversation_event = 7
  # Sam lost post slaver
  #elif samantha.conversation_event == 16: # moved to coffee shop
    #wt_image barista_manager_serving
    #"There's no sign of Sam here today. The store manager is handing out the coffee. He notices you come in."
    #barista_manager "Hey, you used to be buddies with Sam. Any idea where she is? She hasn't shown up for her shift and no one can reach her. Probably just left town without giving notice, leaving us short staffed."
    #$ samantha.new_barista_switch = 1
    #call convert(samantha,'unavailable')
    #$ tracy.opp = 2
  else:
    pass
  wt_image current_location.image
  return

label samantha_conversation_chat_initial:
  $ title = "What do you do?"
  menu:
    "Just take your coffee":
      pass
    "Make small talk":
      player.c "How are you today?"
      wt_image barista_coffee_3
      samantha.c "Great! My girlfriend and I went to see the best concert last night. I'm still floating from the excitement of it."
      player.c "Your girlfriend?"
      wt_image barista_coffee_2
      samantha.c "Yes. She's the best!  She's the one who treated me to the concert tickets. I'm so lucky to have met her."
      "Sam drifts away to look after the next customer."
      add tags 'revealed_lesbian' to samantha
    "Ask her on a date":
      player.c "I'd love to be able to take you on a date sometime."
      wt_image barista_coffee_3
      samantha.c "How sweet! But as you can tell, I like girls, and I already have a girlfriend."
      player.c "A girlfriend?"
      wt_image barista_coffee_2
      samantha.c "Yes. She's the best! I'm so lucky to have met her."
      "Sam drifts away to look after the next customer."
      add tags 'asked_on_date_pre_break_up' 'revealed_lesbian' to samantha
  return

label samantha_conversation_chat_breakup:
  $ title = "What do you do?"
  menu:
    "Just take your coffee":
      pass
    "Ask her what's wrong":
      player.c "Is something wrong?"
      wt_image barista_coffee_5
      samantha.c "Not really. I mean, yes. It's my girlfriend. She broke up with me."
      if samantha.has_tag('revealed_lesbian'):
        player.c "I'm sorry to hear that. What happened?"
      else:
        player.c "Your girlfriend?"
        samantha.c "Ex girlfriend now, I guess. I thought she was 'the one', you know? I guess I was wrong."
        add tags 'revealed_lesbian' to samantha
      samantha.c "She said I'm lacking ambition. She doesn't want to be with someone who isn't doing anything with her life."
      samantha.c "It's not like I'm planning on being a barista forever. It's just that I'm not sure what I want to be doing."
      samantha.c "Anyway, we had a big row and she said a lot of hurtful things and now she's gone."
      wt_image barista_coffee_4
      "Sam turns away to serve other customers before you have a chance to talk any more today."
      $ cassandra.discuss_barista = 1
      $ janice.discuss_barista = 1
      $ marilyn.discuss_barista = 1
      $ samantha.conversation_event += 1
    "After today, look for a new barista (Stop going to Sam)":
      call samantha_look_for_new_barista from _call_samantha_look_for_new_barista_3
  return

label samantha_look_for_new_barista:
  if samantha.new_barista_switch == 0:
    "You take your coffee and leave, vowing to find a new person to serve you in the future."
    $ tracy.opp = 2
    $ samantha.new_barista_switch = 1
  return

label samantha_setup_with_someone:
  player.c "I'd be happy to set you up with someone new. I'm sure I could find you some really interesting partners who would love to get to know you better."
  wt_image barista_coffee_5
  samantha.c "Thanks, but finding a date isn't a problem. You'd be surprised at how many women hit on me while I'm working here."
  samantha.c "Even guys sometimes. It's as if they can't tell I'm gay. Which I don't get, because I would think it should be totally obvious."
  samantha.c "Anyway, no, I'm in no mood for dating right now. Or sex even, for that matter."
  wt_image barista_coffee_4
  "Sam gets you your coffee then moves on to the next customer."
  add tags 'discussed_setting_her_up_with_a_girl' to samantha
  return

label samantha_ask_for_date:
  player.c "How about a date, you and I, to help cheer you up?"
  wt_image barista_coffee_5
  samantha.c "Why?  You know I'm gay."
  player.c "Don't you ever date boys?"
  samantha.c "No. I mean, I've been with guys in the past. Don't get me wrong. I'm not morally opposed to it. It's not like I think its a perversion or anything like that. It just doesn't do anything for me."
  wt_image barista_coffee_4
  "Sam gets you your coffee then moves on to the next customer."
  $ samantha.discussed_boys = 1
  add tags 'asked_for_date_after_break_up' to samantha
  return

label samantha_sex_life:
  if samantha.discussed_submission == 1:
    player.c "Sam, have you ever had any interest in exploring submission?"
    wt_image barista_coffee_5
    samantha.c "You mean, like BDSM?"
    player.c "Yes"
    samantha.c "I used to spank my ex sometimes. She used to really get off on that. I've never had any interest in getting my own tail swatted."
    wt_image barista_coffee_4
    "Sam gets you your coffee then moves on to the next customer."
    $ samantha.discussed_submission = 2
  elif samantha.discussed_boys == 0:
    player.c "So have you ever been interested in boys, Sam?"
    wt_image barista_coffee_5
    samantha.c "No. I mean, I've been with guys in the past. Don't get me wrong. I'm not morally opposed to it. It's not like I think it's a perversion or anything like that. It just doesn't do anything for me."
    wt_image barista_coffee_4
    "Sam gets you your coffee then moves on to the next customer."
    $ samantha.discussed_boys = 1
  elif samantha.discussed_boys == 1:
    player.c "When was the last time you had sex with a man, Sam?"
    wt_image barista_coffee_5
    samantha.c "Hmmm. Let me think. It would have been about a year ago, before I got together with my ex."
    samantha.c "I blew an old college buddy because he was totally down and depressed and I wanted to help him feel better."
    player.c "Wow. We would should all have college friends like you."
    wt_image barista_coffee_2
    "She laughs. Sam gets you your coffee then moves on to the next customer."
    $ samantha.discussed_boys = 2
  elif samantha.discussed_boys == 2:
    player.c "What about intercourse, Sam?  When's the last time you had real sex with a man?"
    wt_image barista_coffee_5
    samantha.c "You're really interested in my sexual history, aren't you?  Okay. Let me think. That was quite a while ago."
    samantha.c "It would have been a few years back. It was a friend of my brother. A sweet, awkward geeky guy."
    samantha.c "He was kind of a clueless virgin, the hopeless type you worry are never going to have the confidence or the emotional IQ to be with a woman."
    samantha.c "I figured if I didn't show him how to do it, he was never going to figure it out on his own. You know the type I'm talking about?"
    player.c "I think so, yes. And did you help him?"
    wt_image barista_coffee_2
    samantha.c "He's married now, so maybe I did."
    "Sam gets you your coffee then moves on to the next customer."
    $ samantha.discussed_boys = 3
  return

label samantha_discuss_retail:
  player.c "What about a job at a retail store?"
  wt_image barista_coffee_5
  samantha.c "I have thought about that, but I don't think that's exactly the ambitious career my ex had in mind. It's still low wages, only with no tips. And I'm not sure it offers much in the way of a long term career path."
  "She glances at the line up behind you."
  wt_image barista_coffee_1
  samantha.c "It's super busy in here right now. I don't have time to chat anymore today."
  "Sam gets you your coffee then moves on to the next customer."
  add tags 'discussed_retail' to samantha
  return

label samantha_ask_how_thinking_going:
  player.c "How's the thinking going, Sam?"
  wt_image barista_coffee_5
  samantha.c "Not well. I'm stuck in a rut. Professionally, and in my own head. I can't figure out what I want to do."
  $ title = "How do you respond?"
  menu:
    "What are you able to do?" if not samantha.has_tag('discussed_ability'):
      player.c "What are you able to do?  Career wise."
      samantha.c "That's a problem. Nothing, as far as I can figure out. Pouring coffee seems to be my only employable skill."
      wt_image barista_coffee_4
      samantha.c "I guess I need to think about things some more. Thanks for the chat."
      "Sam gets you your coffee then moves on to the next customer."
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
      add tags 'discussed_ability' to samantha
    "How about retail?" if samantha.has_tag('discussed_ability') and not samantha.has_tag('discussed_retail'):
      call samantha_discuss_retail from _call_samantha_discuss_retail
    "What about going back to school?" if samantha.has_tag('discussed_ability') and not samantha.has_tag('discussed_school'):
      player.c "What about going back to school, to upgrade your skills."
      samantha.c "I've thought about that. The problem is, I'm not really good at school and studying. I went to college for a couple of years, but I didn't get much out of it."
      samantha.c "Plus I need to work, to pay the bills. So I'd have to go to school around my work schedule, which means I'd be really tired when I was supposed to be studying. I can't see me succeeding like that. I think I'd just be throwing the tuition down the drain."
      wt_image barista_coffee_4
      samantha.c "Maybe it's hopeless. Maybe I'm doomed to be a barista forever."
      "Sam gets you your coffee then moves on to the next customer."
      add tags 'discussed_school' to samantha
      if samantha.has_tag('discussed_good_at'):
        if gloria.solution_status > 1:
          $ gloria.discussed_barista = 1
        $ samantha.conversation_event += 1
    "What are you good at?" if not samantha.has_tag('discussed_good_at'):
      player.c "What are you good at, Sam?"
      samantha.c "You mean besides pouring coffee?  Not very much."
      player.c "Not just work wise.  Think more broadly. Overall, what are you good at, compared to other people you know."
      "She stops briefly to think."
      samantha.c "Making small talk.  Putting people at ease."
      samantha.c "Not to go all conceited, but I'm pretty good looking, and I've heard it said that people are sometimes intimidated by beautiful women.  I don't let that happen.  I'm pretty good at helping people to feel comfortable around me."
      "She glances quickly at the line up forming behind you."
      wt_image barista_coffee_1
      samantha.c "I need to get back to serving customers now.  I guess I need to think about things some more.  Thanks for the chat."
      add tags 'discussed_good_at' to samantha
      if samantha.has_tag('discussed_school'):
        if gloria.solution_status > 1:
          $ gloria.discussed_barista = 1
        $ samantha.conversation_event += 1
    "Maybe you're just not very smart":
      player.c "Maybe you're just not very smart."
      wt_image barista_coffee_2
      "She laughs."
      samantha.c "Maybe! That would seem a reasonable conclusion."
      "Well, at least you got her to laugh at herself. Sam gets you your coffee then moves on to the next customer."
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  return

label samantha_suggest_new_career:
  player.c "Are you ready to get started on a new career, Sam?"
  wt_image barista_coffee_5
  samantha.c "Yes, I am. I'm just not sure what that could be. Why, did you have any ideas?"
  $ title = "What do you suggest?"
  menu:
    "How about sales?":
      player.c "I think you would be good at sales. You're personable. You're good looking. You're good at small talk and at putting people at ease."
      wt_image barista_coffee_2
      samantha.c "I suppose. Maybe that could be an option. But what would I sell?  Did you have something in mind?"
      $ title = "What do you suggest?"
      menu:
        "How about retail?" if not samantha.has_tag('discussed_retail'):
          call samantha_discuss_retail from _call_samantha_discuss_retail_1
        "How about being an Avalon Lady?":
          call samantha_being_avalon_lady from _call_samantha_being_avalon_lady
        "Nothing yet":
          player.c "Nothing yet, but I'll let you know when I come up with a good option for you."
          wt_image barista_coffee_3
          samantha.c "Okay!"
          "Sam hands over your coffee and goes back to serving other customers."
    "How about personal services":
      player.c "How about providing personal services?"
      samantha.c "I don't understand. What do you mean?"
      player.c "I mean a career in helping people. In using your natural charm, your ability to put people at ease, your beauty.  All of those things to help people feel better about themselves and solve problems in their life."
      wt_image barista_coffee_2
      samantha.c "That sounds interesting, but what exactly did you have in mind?"
      $ title = "What do you suggest?"
      menu:
        "Discuss sex services" if samantha.whore_status == 0:
          call samantha_sex_services from _call_samantha_sex_services
        "Discuss being a Domme" if samantha.domme_status == 0:
          call samantha_being_domme from _call_samantha_being_domme
        "Discuss the Club President and his wife" if gloria.discussed_barista == 1:
          call samantha_club_pres_and_wife from _call_samantha_club_pres_and_wife
        "Nothing yet":
          player.c "Nothing yet, but I'll let you know when I come up with a good option for you."
          wt_image barista_coffee_3
          samantha.c "Okay!"
          "Sam hands over your coffee and goes back to serving other customers."
    "Nothing yet":
      player.c "Nothing yet, but I'll let you know when I come up with a good option for you."
      wt_image barista_coffee_3
      samantha.c "Okay!"
      "Sam hands over your coffee and goes back to serving other customers."
  return

label samantha_being_avalon_lady:
  player.c "What about working as an Avalon Lady?"
  wt_image barista_coffee_5
  samantha.c "You mean be a door-to-door salesperson?"
  player.c "Why not? You get out and meet people every day. You develop relationships with them. Some of them may even become regular customers. Then the benefits of your good service go back to you, not the coffee shop."
  samantha.c "I don't know if I'd be able to explain all of their products."
  player.c "They'll train you. It's household goods and beauty products, stuff you likely already use around your own house."
  player.c "Besides, look at you. You'd be a walking billboard for the benefits of Avalon products. If you feel morally obligated to insist on truth in advertising, you could even start using some yourself. Either way, women will take one look at you and be ready to buy any beauty product you recommend."
  wt_image barista_coffee_2
  samantha.c "That's an interesting idea. I need to think about it."
  "Sam hands you your coffee and goes back to her work."
  $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  $ samantha.conversation_event = 8
  return

label samantha_sex_services:
  player.c "What about being a sexual concierge, and help out guys like your college buddy or your brother's friend."
  wt_image barista_coffee_5
  samantha.c "You mean have sex with men for money?"
  player.c "Your college buddy isn't the only lonely, depressed guy out there. And your brother's friend isn't the only hopeless geek who needs help learning his way around a woman's body."
  player.c "You could do a lot of good work, help a lot of people, and make good money at it too."
  wt_image barista_coffee_1
  samantha.c "I'll need to think this over. What you're suggesting  makes some sense, but it also sounds an awful lot like being a whore."
  "Sam hands over your coffee and goes back to work, a thoughtful look on her face."
  $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  $ samantha.conversation_event = 12
  return

label samantha_being_domme:
  player.c "Well, take your ex. She liked it when you spanked her behind, right?"
  wt_image barista_coffee_3
  samantha.c "Yes"
  player.c "Not everybody who wants their tail swatted has someone in their life willing to do that."
  wt_image barista_coffee_2
  samantha.c "People would pay me to spank them?"
  player.c "Not just spank them. Dominate them."
  samantha.c "You mean in a sexual way?"
  player.c "Yes, there's a sexual tension involved, but it doesn't mean you have to have sex with them. Some people need a Domme in their life and don't have access to one."
  player.c "You could fill that void in their life, even if you didn't have sex with them."
  wt_image barista_coffee_1
  samantha.c "I'll need to think this over. This isn't something I've ever heard of, let alone thought of."
  "Sam hands over your coffee and goes back to work, a thoughtful look on her face."
  $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  $ samantha.conversation_event = 9
  return

label samantha_club_pres_and_wife:
  player.c "How about being a personal assistant to an executive couple? I have a friend who's looking for a live in assistant to help her and her husband out around the house."
  player.c "They're both very busy people. He's the President of a prestigious local club. Lots of stress. They could use someone like you to make their lives easier."
  wt_image barista_coffee_5
  samantha.c "What would I need to do for them?"
  player.c "Whatever they need to make their lives easier. Helping out around the house. Organizing things for them. Probably doing some chores and running errands."
  player.c "Oh, and sleeping with them when they need sexual release."
  samantha.c "So basically just being an all around help for them?"
  player.c "Exactly"
  wt_image barista_coffee_2
  samantha.c "Hmmm. That could be interesting. Are they nice people?"
  player.c "As nice as rich successful people ever are, I think. Would you like me to talk to them about hiring you?"
  wt_image barista_coffee_3
  samantha.c "Okay. Yes, that sounds like an interesting opportunity."
  "She hands over your coffee and goes on to her next customer."
  add tags 'something_to_discuss' to gloria
  $ gloria.discussed_barista = 2
  $ samantha.conversation_event = 15
  return

## Character Specific Actions
# Doll - Put Her To Work
label samantha_put_to_work:
  $ samantha.training_session()
  wt_image barista_doll_housework_1
  "You take [samantha.full_name] out and have it wear some clothes so it won't look out of place, then take it upstairs to do some chores."
  $ title = "What chores do you want to assign her?"
  menu:
    "Cook":
      call forced_movement(kitchen) from _call_forced_movement_932
      summon samantha
      wt_image barista_doll_housework_4
      "At first, [samantha.full_name] seems comfortable in the kitchen."
      wt_image barista_doll_housework_5
      "Then partway through a measurement, it freezes up."
      wt_image barista_doll_housework_6
      samantha.c "Metric ... Imperial ... Microns ..."
      "Something's not working right, and the cooking comes to an immediate and permanent halt. You'll need to finish the meal on your own."
    "Tidy Up":
      call forced_movement(living_room) from _call_forced_movement_933
      summon samantha
      wt_image barista_doll_housework_2
      "[samantha.full_name] is quite efficient at tidying up the house and putting things away."
      wt_image barista_doll_housework_3
      "Closet doors, however, invariably cause problems."
      player.c "You don't need to knock,  It's a closet.  There's no one in there."
      "It's no use. You'll need to open the door yourself or [samantha.full_name] will keep knocking for the rest of the day."
  call forced_movement(basement) from _call_forced_movement_934
  call character_location_return(samantha) from _call_character_location_return_636
  return

# Doll - Sell Her
label samantha_sell_her:
  if samantha.doll_return_week == 0:
    "You're not sure you want [samantha.full_name] hanging around your house. Besides, she should be worth something to the right buyer."
    "It's going to take a little bit of time to figure out how to sell her safely. You'll investigate over the next few days. If you decide you really do want to sell her, you can do so next week."
    $ samantha.doll_return_week = week
  elif week > samantha.doll_return_week:
    "With time and patience, you're eventually able to locate a secondary market for [samantha.full_name] by searching out forums dedicated to the appreciation and collection of Bodywerks creations."
    "The resale value isn't as much as you'd hoped for. It seems the highest prices are reserved for this year's models rather than used models."
    "However, a potential buyer locally has offered you 500 for her, contingent on him doing an examination to confirm she doesn't need any major repairs, "
    $ title = "What do you do?"
    menu:
      "Sell her for 500":
        wt_image barista_doll_2
        "You make arrangements for a cash sale. When the buyer arrives, you show him to the basement and open [samantha.full_name]'s crate."
        wt_image barista_doll_4
        samantha_buyer "Very nice. Unit, provide your full original designation and function."
        samantha.c "Unit 12639, a three hole pleasure drone."
        samantha_buyer "Perform self diagnosis, short form."
        samantha.c "Skin integrity: intact"
        samantha.c "Motor Functions: All subsections working"
        samantha.c "Hearing: working"
        samantha.c "Speech Functions: working"
        samantha.c "Lubrication Systems: working"
        samantha.c "Programming: errors detected"
        samantha_buyer "Run self-diagnosis on programming functions."
        samantha.c "Spread command: functional"
        samantha.c "Ride command: functional"
        samantha.c "Doggy command: functional"
        samantha.c "Blow command: damaged"
        samantha.c "Anal command: damaged"
        samantha.c "Kiss command: damaged"
        samantha.c "Cum command: functional"
        samantha.c "Clean command: functional"
        samantha.c "Cook command: damaged"
        samantha_buyer "Stop diagnosis. Assess likely reason for command function damage."
        samantha.c "Unit 12639 experienced a fall while in crate during a recent transport."
        samantha_buyer "Perform self repair function on Kiss command."
        samantha.c "Processing ... Processing ... Processing ... Self-repair attempt complete."
        samantha_buyer "Unit 12639, kiss me."
        wt_image barista_doll_5
        "She leans in and opens her mouth, her lips already gleaming with moisture ... then she halts, just short of his lips, as if frozen."
        samantha_buyer "It looks like she suffered some damage before she got to you. I may need to spend some time and money getting her reprogrammed to full functionality. She's a real beauty though, and worth the effort. Here's your 500."
        wt_image barista_doll_1
        "Her new owner packs [samantha.full_name] up in her crate and takes her with him."
        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
        #call convert(samantha, "unavailable")
        $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
        dismiss samantha
        wt_image current_location.image
        change player money by 500 notify
      "Keep her":
        pass
  else:
    "You haven't had time to investigate how to sell her safely yet. Wait until next week before you decide whether to proceed."
  return

# Doll - Take Her Out To Play
label samantha_take_her_out_to_play:
  player.c "Come here, [samantha.full_name]."
  call forced_movement(living_room) from _call_forced_movement_935
  summon samantha no_follows
  wt_image barista_doll_3
  $ title = "Issue a command"
  menu:
    "Kiss me" if not samantha.has_tag('doll_command_kiss'):
      player.c "Kiss me."
      "She makes no response, so you lean in and press your lips against hers, to show you what you want. She still doesn't move.  It seems she doesn't have this functionality."
      add tags 'doll_command_kiss' to samantha
    "Blow me" if not samantha.has_tag('doll_command_blow'):
      player.c "Blow me."
      "She doesn't respond."
      player.c "Suck me. Perform oral sex on me. Kneel down and take out my cock and wrap your lips around it."
      "She doesn't move. It seems she hasn't been equipped with this functionality."
      add tags 'doll_command_blow' to samantha
    "Fuck me":
      player.c "Fuck me."
      samantha.c "Please specify preferred approach. Shall I spread, ride, or doggy?"
      $ title = "Issue a command"
      menu:
        "Spread":
          wt_image barista_doll_6
          "She leans back and opens her legs, her fingers spreading her labia to provide you easy access to her already wet cunt."
          add tags 'doll_spread' to samantha
          call samantha_take_her_out_to_play_extra_commands from _call_samantha_take_her_out_to_play_extra_commands
        "Ride":
          wt_image barista_doll_9
          "She crawls on top of you, her fingers spreading her labia to provide you easy access to her already wet cunt."
          add tags 'doll_ride' to samantha
          call samantha_take_her_out_to_play_extra_commands from _call_samantha_take_her_out_to_play_extra_commands_1
        "Doggy":
          wt_image barista_doll_11
          "She turns around and leans forward, opening her legs to provide you easy access to her already wet cunt."
          add tags 'doll_doggy' to samantha
          call samantha_take_her_out_to_play_extra_commands from _call_samantha_take_her_out_to_play_extra_commands_2
      $ samantha.sex_count += 1
      add tags 'trained_today' to samantha
      rem tags 'doll_spread' 'doll_ride' 'doll_doggy' from samantha
      orgasm notify
    "Anal" if not samantha.has_tag('doll_command_anal'):
      player.c "Let me fuck you in the ass."
      "She doesn't respond."
      player.c "Provide anal. Backdoor sex. Spread your butt cheeks, I'm going to fuck your rosebud."
      "She doesn't move. It seems she hasn't been equipped with this functionality"
      add tags 'doll_command_anal' to samantha
    "Never mind":
      pass
  call forced_movement(basement) from _call_forced_movement_936
  call character_location_return(samantha) from _call_character_location_return_637
  "You take [samantha.full_name] back to her crate."
  return

label samantha_take_her_out_to_play_extra_commands:
  "You enter her easily."
  player.c "What else can you do in this position?"
  if samantha.has_tag('doll_ride'):
    samantha.c "I can cum, ride faster, tighten, talk dirty, or bark."
  else:
    samantha.c "I can cum, tighten, talk dirty, or bark."
  $ title = "Issue a command?"
  menu:
    "Cum":
      if samantha.has_tag('doll_spread'):
        wt_image barista_doll_7
      elif samantha.has_tag('doll_ride'):
        wt_image barista_doll_10
      elif samantha.has_tag('doll_doggy'):
        wt_image barista_doll_12
      samantha.c "Ooohhhhh!!!!  AAAAHHHHH!!!!!"
      "She immediately begins climaxing on your cock, bringing you to orgasm too."
      player.c "[player.orgasm_text]"
    "Ride faster" if samantha.has_tag('doll_ride'):
      "She starts bouncing up and down on your cock faster and faster, until she's moving up and down faster than any human being should be capable of moving."
      "It's like your cock is the piston inside a motor, and her cunt is the piston ring.  An incredibly soft but fast moving piston ring."
      "Her body is almost a blur, it's moving so quickly by the time you cum, releasing your seed inside her."
      player.c "[player.orgasm_text]"
    "Tighten":
      "Her opening immediately shrinks. It's still wet, and you can slide in and out of it pleasurably, but now its like fucking a hole that's one size too small for your cock."
      "Every in stroke becomes like penetrating an asshole for the first time, or entering a virgin. It only takes a few minutes of this sensation to send you over the edge."
      player.c "[player.orgasm_text]"
    "Talk dirty":
      if samantha.has_tag('doll_spread'):
        wt_image barista_doll_8
      elif samantha.has_tag('doll_ride'):
        wt_image barista_doll_10
      elif samantha.has_tag('doll_doggy'):
        wt_image barista_doll_12
      samantha.c "Oh yeah, fuck me. Fuck me with that big, hard cock of yours."
      samantha.c "Ohhh that feels so good. I love the feeling of your hard cock pounding into my soft, tender pussy."
      samantha.c "That's it. Fuck me hard. Make me your bitch. Fuck me until the only thing I can think about is how good your cock feels inside me. Fuck me until my legs are so weak I can't stand."
      "She continues on, until you can't hold back any longer, and release your cum inside her."
      player.c "[player.orgasm_text]"
    "Bark":
      if samantha.has_tag('doll_spread'):
        wt_image barista_doll_8
      elif samantha.has_tag('doll_ride'):
        wt_image barista_doll_10
      elif samantha.has_tag('doll_doggy'):
        wt_image barista_doll_12
      samantha.c "Ruff!  Rrrufff.  Rrruff rrufff rruffff!."
      "She continues on, until you can't hold back any longer, and release your cum inside her."
      player.c "[player.orgasm_text]"
    "Just fuck her":
      "You don't need any additional stimulus. The sight of her body and the feel of her cunt around your cock is more than enough to bring you over the edge."
      player.c "[player.orgasm_text]"
  return

# Maid - Check Outfit
label samantha_check_outfit:
  wt_image barista_club_job_3_22
  player.c "Hi, Sam.  Are you wearing your outfit properly yet?"
  wt_image barista_club_job_3_23
  samantha.c "You mean without panties? No. I know you and Gloria think I should, but it would be really distracting feeling the breeze on my bare pussy while I'm trying to tidy up."
  wt_image barista_club_job_3_24
  samantha.c "Besides, Club members keep interrupting my work as it is."
  wt_image barista_club_job_3_25
  samantha.c "If I start flashing them while I'm dusting, I think it'll just mean more interruptions."
  return

# Maid - Discuss How She Can Thank You
label samantha_thank:
  wt_image barista_club_job_3_1
  samantha.c "Hi! I was just cleaning up around the Club."
  wt_image barista_club_job_3_22
  player.c "I've been giving some thought to how you can thank me properly for helping you find this job, Sam, and there is something you can do for me."
  wt_image barista_club_job_3_25
  samantha.c "Really?  That's great.  What is it?"
  $ title = "How can she thank you?"
  menu:
    "With her body":
      $ samantha.add_tags('trained_today')
      rem tags 'no_hypnosis' from samantha # so subsequent tests work
      player.c "I've been horny lately, and could use a good orgasm."
      wt_image barista_club_job_3_24
      samantha.c "Oh.  Gloria and her husband keep me so busy with that type of work, too.  I don't have much time to help other people out with that sort of problem."
      wt_image barista_club_job_3_25
      samantha.c " I really am grateful to you, though, so okay. Just this once."
      wt_image barista_club_job_3_1
      samantha.c "Let's go into the President's office. He's not here right now, but I have the key."
      wt_image barista_club_job_3_27
      "Sam props herself up on the President's desk and removes her top and panties."
      wt_image barista_club_job_3_28
      samantha.c "Are you horny enough that you just want to fuck me, or do you want me to give you a blow job first?"
      $ title = "What do you want?"
      menu menu_samantha_thank_first:
        "I'll just fuck you":
          wt_image barista_club_job_3_29
          player.c "Lie back, Sam. I don't need a blow job. I'm already hard and ready to fuck you."
          wt_image barista_club_job_3_30
          "She's not really wet when you push into her, but she's not dry either."
          wt_image barista_club_job_3_19
          "It occurs to you that the Club President has been using her often enough that she may have taken to pre-applying lube to herself on a regular basis.  It's enough to make this fun for you without it being uncomfortable for her."
          wt_image barista_club_job_3_20
          "After a bit you flip her over ..."
          wt_image barista_club_job_3_8
          "... and fuck her from behind as she bends over the desk."
          call samantha_thank_fuck_now from _call_samantha_thank_fuck_now
        "I want a blow job first":
          player.c "A blow job first would be great."
          wt_image barista_club_job_3_31
          samantha.c "Okay"
          "Sam drops down in front of you, takes out your cock ..."
          wt_image barista_club_job_3_32
          "... and wraps her lips around it."
          wt_image barista_club_job_3_7
          "She proceeds to provide a serviceable if uninspired blow job, made nevertheless thoroughly enjoyable by the sight of Sam in her maid's outfit."
          $ title = "Fuck her now?"
          menu:
            "Yes, fuck her now":
              wt_image barista_club_job_3_32
              player.c "Bend over the desk, Sam.  I'm ready to fuck you now."
              wt_image barista_club_job_3_33
              "She's not really wet, but she's not dry either."
              wt_image barista_club_job_3_9
              "It occurs to you that the Club President has been using her often enough that she may have taken to pre-applying lube to herself on a regular basis."
              wt_image barista_club_job_3_8
              "It's enough to make this fun for you without it being uncomfortable for her."
              call samantha_thank_fuck_now from _call_samantha_thank_fuck_now_1
            "No, cum on her":
              wt_image barista_club_job_3_32
              player.c "Take my cock out of your mouth, Sam."
              wt_image barista_club_job_3_31
              samantha.c "Are you ready to fuck me now?"
              player.c "No need.  Just keep stroking my cock with your hand."
              wt_image barista_club_job_3_36
              player.c "[player.orgasm_text]"
              samantha.c "Oh!  It's a good thing I have my cleaning supplies with me."
              wt_image barista_club_job_3_37
              samantha.c "Did that feel good?  Is your horniness gone now?"
              player.c "For the time being."
              samantha.c "Oh good!"
              wt_image barista_club_job_3_1
              if samantha.has_tag('hypnotized_now'):
                "You have her dress then send her back to the Club, not remembering what you've done or that she's 'thanked you'."
                $ samantha.hypno_blowjob_count += 1
                $ samantha.hypno_facial_count += 1
              else:
                "She goes back to cleaning up around the Club."
                add tags 'maid_thank_complete' to samantha
                $ samantha.blowjob_count += 1
                $ samantha.facial_count += 1
        "I want to spank you first":
          player.c "I want to spank you first, Sam."
          wt_image barista_club_job_3_38
          samantha.c "I don't like to be spanked."
          player.c "I thought you were grateful to me for getting you this job?"
          wt_image barista_club_job_3_39
          samantha.c "I am grateful."
          player.c "Good.  Then you won't mind letting me redden your ass.  It'll really turn me on."
          wt_image barista_club_job_3_12
          "She turns and presents her ass to you."
          samantha.c "I suppose not.  If that's really what you want."
          player.c "It is.  Bend over."
          wt_image barista_club_job_3_13
          samantha.c "Is this going to ..."
          wt_image barista_club_job_3_14
          "*smack*"
          samantha.c "Ow!"
          wt_image barista_club_job_3_15
          player.c "Is this going to hurt? Of course it is, Sam.   How else can I turn your bum a lovely shade of red."
          wt_image barista_club_job_3_16
          "*smack* ... *smack* ... *smack* ... *smack* ... *smack*"
          samantha.c "Ow!   Ow!   OW!  OWW!!  OWWW!!!  Damn that does hurt!!!"
          wt_image barista_club_job_3_40
          samantha.c "Ohhh, my poor bum!  I hope you enjoyed that."
          $ title = "What now?"
          menu:
            "Fuck her now":
              player.c "I did, but now I'm even more horny.  Bend over the desk."
              wt_image barista_club_job_3_33
              "She's not really wet, but she's not dry either."
              wt_image barista_club_job_3_9
              "It occurs to you that the Club President has been using her often enough that she may have taken to pre-applying lube to herself on a regular basis."
              wt_image barista_club_job_3_8
              "It's enough to make this fun for you without it being uncomfortable for her."
              change player energy by -energy_very_short
              call samantha_thank_fuck_now from _call_samantha_thank_fuck_now_2
            "The spanking was enough":
              player.c "I did.  Your tail is great for swatting."
              samantha.c "If you say so.  I'll never understand why my ex enjoyed me doing that to her.  Are you going to ..."
              player.c "Remember spanking you?  Yes, for quite some time."
              wt_image barista_club_job_3_17
              if samantha.has_tag('hypnotized_now'):
                "You let her rub the soreness out of her ass, then have her dress then send her back to the Club, not remembering what you've done or that she's 'thanked you'."
                change player energy by -energy_very_short notify
              else:
                "You leave Sam alone to try and rub the soreness out of her ass before she goes back to cleaning up around the Club."
                add tags 'maid_thank_complete' to samantha
                change player energy by -energy_short notify
              wt_image club.image
        "Hypnotize her" if player.can_hypno(samantha):
          add tags 'hypnotized_now' to samantha
          $ samantha.hypno_session() # deducts energy and record hypnotized
          player.c "Look at this for me, Sam."
          samantha.c "What is it?"
          call focus_image from _call_focus_image_17
          player.c "Just look at it. Look at it. Listen to me as you look at it. Only to me. Only my words. Only my words now, Sam."
          wt_image barista_club_job_3_41
          "She falls under your trance. Her boobs are already out, so there's no need to instruct her to expose them."
          player.c "You are going to forget everything we do here today, Sam. You're going to thank me for getting you this good job, but you will not remember thanking me."
          wt_image barista_club_job_3_11
          samantha.c "Okay.  How should I thank you?"
          if not samantha.has_tag('no_trigger_message'):
            add tags 'no_trigger_message' to samantha
            sys "Don't bother hypnotizing her multiple times to try and plant a trigger. There isn't one in the game right now. But you now can have sex with her whenever you spot her in the Club, as long as you hypnotize her each time."
          $ title = "How do you want her to thank you?"
          jump menu_samantha_thank_first
    "Wait for something else":
      "Your self-restraint is admirable, but there's nothing in the game right now that Sam can help you with. You may was well go ahead and enjoy her body the next time you have a little energy to spare."
  rem tags 'hypnotized_now' from samantha
  add tags 'no_hypnosis' to samantha
  return

label samantha_thank_fuck_now:
  wt_image barista_club_job_3_34
  "She's oddly silent as you fuck her ..."
  wt_image barista_club_job_3_9
  "... though she does keep looking back at you as her eyes search your face, looking for confirmation that you're enjoying this. That's kind of cute and sexy in its own right."
  wt_image barista_club_job_3_35
  "She finally breaks her silence as you cum."
  samantha.c "Oh!"
  player.c "[player.orgasm_text]"
  wt_image barista_club_job_3_10
  samantha.c "It's a good thing I went on birth control when I took this job."
  wt_image barista_club_job_3_21
  samantha.c "Did that feel good?  Is your horniness gone now?"
  player.c "For the time being."
  samantha.c "Oh good!"
  wt_image barista_club_job_3_1
  if samantha.has_tag('hypnotized_now'):
    "You have her dress then send her back to the Club, not remembering what you've done or that she's 'thanked you'."
    $ samantha.hypno_sex_count += 1
  else:
    "She goes back to cleaning up around the Club."
    add tags 'maid_thank_complete' to samantha
    $ samantha.sex_count += 1
  orgasm notify
  return

########### OBJECTS ###########
## Common Objects
# Contact Character
# Contact - Barista You Train Her To Be A Domme
label samantha_contact_you_train_her_domme:
  $ samantha.training_session()
  $ samantha.domme_you_train_outfit += 1 # this is to distinguish between Jesse training her
  if samantha.domme_you_train_outfit == 1: # this 'if' isn't really needed as Jess's training is in a different label so this can only ever be "1"
    wt_image barista_phone_1
    player.c "Sam, are you ready to begin training for your new career?"
    samantha.c "I guess. I'm really nervous."
    player.c "Don't be. I'll take things slow. Here's my address."
    samantha.c "Okay. I going to tell my co-worker where I'm going, so no funny business. I'll be there in an hour. I just need to fix myself up."
    call forced_movement(dungeon) from _call_forced_movement_44
    summon samantha
    wt_image current_location.image
    "You greet Sam at the door and escort her directly to your dungeon."
    wt_image barista_domme_you_train_1_1
    samantha.c "What is this place?"
    player.c "Does it make you nervous?"
    samantha.c "A little."
    player.c "Good. Consider this lesson number one. Domination and submission is less about the physical, and far more about the mental."
    player.c "Set the stage when meeting your clients to make them a little nervous. They want to be nervous. It's part of what they need from you."
    player.c "Turn around now. Face away from me and take off your top."
    wt_image barista_domme_you_train_1_2
    "Nervously, Sam turns and slides the coat off her shoulders."
    player.c "Offer yourself to me, girl."
    samantha.c "What?"
    player.c "You heard me. Offer me your submission. Ask me to take control over you and use you however I see fit."
    samantha.c "I ... is this necessary?"
    player.c "Lesson two. Let the client know that you're in charge. They want you to take control of them. That's why they came to you."
    player.c "Some will relinquish their power easily. Others will need you to demand it from them. All of them want to give it to you. Show them you want it, and that you're comfortable receiving their submission."
    player.c "Pull down your pants and offer me your submission.  Don't make me ask you again."
    wt_image barista_domme_you_train_1_3
    samantha.c "I offer you my submission."
    player.c "You will obey me and follow my instructions, exactly and immediately."
    samantha.c "Yes"
    player.c "You will refer to me as 'Sir'. Repeat your agreement to my authority over you, completely and with appropriate deference."
    samantha.c "Yes, I will obey you and follow your instructions. Sir."
    player.c "Lesson three. Make them acknowledge your control over them. Verbalizing their submission to you will make it more real to them."
    player.c "Lean over and show me your ass."
    wt_image barista_domme_you_train_1_4
    player.c "For the remainder of our time together, you belong to me. I can do anything I want with you. Does that make you nervous, girl?"
    samantha.c "Yes, Sir."
    player.c "Lesson four. Some clients want to remain nervous throughout their time with you. Keep those ones guessing, wondering worrying - and hoping - about what you may have in store for them."
    player.c "Others will feel safe and secure as soon as they've given up power to you, knowing they have no more cares or responsibilities in the world than to do as you tell them. Find out what type your client is, and structure your demands of them accordingly."
    wt_image barista_domme_you_train_1_17
    player.c "Remove the rest of your clothes and climb up on the bench.  Kneel there and wait while I decide what I want to do with you."
    wt_image barista_domme_you_train_1_5
    "Sam waits nervously as you circle her, taking in every inch of her body with your eyes."
    player.c "This is the trickiest part of the process. You want them to feel like whatever you do with them, you're doing it because its what you want to do. What you're actually doing, however, are the things they need. The things they came to you to receive."
    player.c "Lesson five. Figure out what they need, then give it to them, but make it seem like its your decision because it's what you want."
    player.c "To get this right, you need to communicate with them before meeting them, to learn what it is that's drawing them to you. You'll charge them for that time. It's part of your service to them."
    player.c "Your problem right now is that you're not paying me for my time. I'm giving you my time for free, to help you get ready for your new career. So with you, I really am going to do whatever I want with you. Is that understood?"
    samantha.c "Yes, Sir."
    player.c "Lean forward. Hands in front of you, head down."
    wt_image barista_domme_you_train_1_6
    player.c "I'm going to spank you, and it's going to hurt."
    "Sam trembles slightly, but moves into position as instructed."
    wt_image barista_domme_you_train_1_7
    "You raise your hand and bring it down sharply on her butt ... *smack*"
    samantha.c "Oww!!"
    player.c "To exercise control, sometimes you need to show the client you're willing to punish them for disobedience. Sometimes you need to show them that you're willing to punish them just because you feel like punishing them."
    player.c "Either way, you have to be prepared to hurt people to succeed in this business. Are you willing to hurt people?"
    samantha.c "I think so."
    "You slap Sam's ass again, harder ... *SMACK*"
    samantha.c "OWW!!!!"
    player.c "Lesson six. There will be lots of time as a Domme when you're not sure about the best way to handle a client or what to do next. No matter what debates you're having in your own head, never let the client hear uncertainty."
    player.c "I'm going to ask you again.  Are you willing to hurt people?"
    samantha.c "Yes, I think I can do that."
    wt_image barista_domme_you_train_1_8
    "You bring your hand down hard on Sam's ass again ... once, twice, three times, four times, five ... *SMACK* *SMACK* *SMACK* *SMACK* *SMACK*"
    samantha.c "OWW!!  OWWW!!!  OWWWW!!!!!  OWW OWWW OWWWWW OWWW OHHHHHHH THAT HURTS!!!"
    player.c "Make a decision. Be decisive in your decision. Change your mind later and be decisive in that, too. Make it seem like it was all part of the plan, or that you just like changing your mind."
    player.c "Whatever you do, don't be wishy washy. They're hiring you to be an authority figure. Act authoritative. Are you willing to hurt people?"
    samantha.c "Yes! I'm willing to hurt people."
    player.c "Much better."
    wt_image barista_domme_you_train_1_11
    "The spanking over, you let Sam sit up and rub her sore ass."
    player.c "Final lesson. Your body. Your clients want it. They want to see it, smell it, touch it, be touched by it."
    player.c "Use their desire for your body to reinforce your control over them. Show it to them. Tease them with it. Offer it to them as a reward or take it away as punishment"
    player.c "You are their goddess, and they will happily worship at the shrine of your body. As their goddess, you set the terms on whether they get any favors from you."
    samantha.c "As soon as they meet me, they're going to know right away that I'm a lesbian. Won't that make the guys less interested in my body?"
    "It takes you a moment to figure out how to respond to that."
    player.c "They'll still be interested. Your sexual orientation is irrelevant. You're their Domme, not their lover. Let all of your clients know up front that sex with you is not on the menu. That's not what they're paying you for."
    player.c "You can decide later whether to let them experience sexual pleasure while they're with you or not. Whether you do or don't, your body is an instrument of their submission. Don't be afraid to use it."
    samantha.c "I used to tease my ex sometimes. Strip in front of her and then go to bed and not let her touch me until she asked nicely. Is that the type of thing you mean?"
    player.c "Yes, exactly."
    $ title = "What do you do next?"
    menu:
      "Demand the use of her mouth":
        player.c "That ends your lessons, Sam.  Lie forward and open your mouth."
        wt_image barista_domme_you_train_1_15
        samantha.c "Why?"
        player.c "You're going to thank me for the training."
        wt_image barista_domme_you_train_1_14
        "You move in front of her and take down your pants, exposing your hard cock.  She makes no objection as you insert it into her open mouth."
        $ title = "What do you want?"
        menu:
            "Have her blow you":
                wt_image barista_domme_you_train_1_9
                "If she's uncomfortable giving you a blow job, the only sign is that she doesn't make eye contact with you as she sucks you."
                "You can live with that. She's neither submissive nor into boys. You content yourself with the access to her mouth she's provided. Gripping her head in your hands, you stroke yourself into her, faster and faster."
            "Face fuck her":
                wt_image barista_domme_you_train_1_12
                "If she's uncomfortable with you using her body to relieve yourself, the only sign is that she doesn't make eye contact with you as you thrust your cock in and out of her open mouth."
                "You can live with that. She's neither submissive nor into boys. You content yourself with the access to her mouth she's provided. Gripping her head in your hands, you stroke yourself into her, faster and faster."
        wt_image barista_domme_you_train_1_16
        player.c "[player.orgasm_text]"
        wt_image barista_domme_you_train_1_10
        "As you fill her mouth with your cum, she rolls over on her back and spits it out."
        player.c "Don't you like the taste?"
        wt_image barista_domme_you_train_1_13
        samantha.c "Not really.  Do straight girls?"
        player.c "Some of them, yes."
        $ samantha.blowjob_count += 1
        orgasm
      "End things there":
        wt_image barista_domme_you_train_1_5
        player.c "That ends your lessons, Sam."
    samantha.c "So is that all I need to know, do you think?"
    $ title = "What do you think?"
    menu:
      "She's ready":
        player.c "You've learned the basics. The rest will come with experience. I think you're ready to start your new career, Sam. I can look after the logistics and the marketing, for a small fee."
        samantha.c "Okay"
        player.c "What are you going to call yourself?"
        wt_image barista_domme_you_train_1_11
        samantha.c "Call myself?"
        player.c "Your professional name. Something different than your real name."
        samantha.c "I'm not sure.  'Samantha', maybe?"
        "You stifle your reaction as best you can."
        player.c "Uh, okay. Mistress Samantha it is. I'll start looking for your first client."
        $ samantha.domme_status = 3
        call convert(samantha, "domme") from _call_convert_10
      "She needs to Domme you for practice":
        player.c "You've learned the basics. I think, however, you should gain some experience as a Domme yourself, before you take on your first client."
        wt_image barista_domme_you_train_1_11
        samantha.c "Okay. Who should I get experience with?"
        player.c "Me. I'll let you practice on me, to build up your confidence. And I can offer constructive criticism afterwards, as necessary."
        samantha.c "That makes sense. Thank you. But I can't practice on you tonight. I'm too worn out."
        player.c "We'll do it later. I'll be in touch."
        $ samantha.discussed_domme_train_you_sub = 2
    $ player.submission_action_count += 1
    change player energy by -energy_long notify
    call character_location_return(samantha) from _call_character_location_return_638
  else:
    pass
  return

# Contact - Barista Jesse Trains Her To Be A Domme
label samantha_contact_jesse_trains_her_domme:
  $ samantha.training_session()
  wt_image barista_phone_1
  player.c "Sam, are you ready to begin training for your new career?"
  samantha.c "I guess. I'm really nervous."
  player.c "Don't be. I'll be there beside you the whole time. Jesse knows what she's doing, and I'll be there to support you."
  samantha.c "Okay. Thanks. I appreciate that."
  summon samantha
  wt_image barista_domme_training_1
  "You and Sam meet up with Jesse at the address she gives you.  Jesse opens the door to let you in.  A large mural with intense BDSM scenes adorns the wall behind her."
  samantha_jesse "Welcome to my lair. Please come in."
  wt_image barista_nervous_1
  samantha.c "What's with the artwork?"
  "Sam nervously fingers her necklace as she looks around, uncertain as to whether she should go in or not."
  wt_image barista_domme_training_15
  samantha_jesse "Does it make you nervous?"
  samantha.c "A little."
  wt_image barista_domme_training_2
  samantha_jesse "Good. That's the point. This is my old dungeon. It doesn't get much use these days. I could let you use it, if you want, when you're ready to entertain your own customers here."
  samantha_jesse "For now, consider this lesson one. Domination and submission starts in the mind. You want your clients to be a little nervous. They want to be a little nervous. It's part of the service you're providing to them."
  wt_image barista_domme_training_15
  samantha_jesse "Now, stop fidgeting like a nervous schoolgirl and come in. Go into that room over there and get changed."
  wt_image barista_nervous_1
  samantha.c "Changed?"
  wt_image barista_domme_training_2
  samantha_jesse "Remove the clothes you're wearing. Put on the articles I've laid out there for you. Then sit on that table until I'm ready for you."
  wt_image barista_domme_training_16
  "A nervous Sam does as she's told, changing into the 'clothes' that have been left out for her and having a seat."
  wt_image barista_domme_training_17
  "Jesse reappears a moment later.  She's changed too, and is wearing not much more than Sam.  Despite the crop in Jesse's hand, Sam seems as impressed by the sight as you at first ..."
  wt_image barista_domme_training_3
  "... then distinctively more nervous, as Jesse clips a leash to the collar on Sam's outfit."
  samantha_jesse "I own you. For the rest of our time together, you belong to me. Is that clear?"
  samantha.c "Yes"
  samantha_jesse "Good. It's important to let the client know, right up front, that you're ready and willing to take charge of them. They won't be able to truly let go until they know that you accept them as the submissive, obedient little slaves they long to be."
  samantha_jesse "Down on your knees, lean forward, hands on the floor."
  wt_image barista_domme_training_4
  "As Sam complies, Jesse strikes her with the crop ... *thwack*"
  samantha.c "Oww!!"
  wt_image barista_domme_training_18
  samantha_jesse "Sometimes showing the client that you're willing to take control requires physical reinforcement. You need to be willing to hurt people to be in this business. Are you willing to hurt people?"
  samantha.c "I think so."
  wt_image barista_domme_training_4
  "Jesse strikes Sam again, harder ... *THWACKK*"
  samantha.c "OWW!!!!"
  wt_image barista_domme_training_18
  samantha_jesse "Self doubt comes with the territory. You may spend a good deal of your time wondering whether you're handling a scene properly. But regardless of whatever doubts you may have internally, you never let the client see them. Are you willing to hurt people?"
  samantha.c "Yes, I think I can do that."
  wt_image barista_domme_training_4
  "Again Jesse brings the crop down on Sam ... *THWACKK*"
  samantha.c "OWWWW!!!!!"
  wt_image barista_domme_training_18
  samantha_jesse "They're paying you to be an authority figure. They want decisiveness. Go with your gut reaction, don't namby pampy around."
  wt_image barista_domme_training_4
  "Another stroke of the crop ... *THWACKK*"
  samantha.c "OWWWW!!!!!  Yes, I'm willing to hurt people."
  wt_image barista_domme_training_18
  samantha_jesse "Lie down on your back.  Look at me."
  wt_image barista_domme_training_5
  samantha_jesse "What are you right now?"
  samantha.c "Yours"
  samantha_jesse "What can I do with you?"
  samantha.c "Whatever you want."
  samantha_jesse "Good. You're getting the hang of this."
  samantha_jesse "Don't just accept control from them, make them acknowledge that they've given up control to you. Let them know that now that you have control over them, you're going to do whatever you want to them. Does that thought make you nervous?"
  samantha.c "Very"
  samantha_jesse "Your client may feel that way too, the ones who want to feel nervous. Keep those ones off balance. Some won't feel nervous at all. They'll feel totally content, knowing that whatever happens now depends on you, and that they have no responsibility other than to obey."
  wt_image barista_domme_training_6
  "Jesse fastens cuffs to Sam's wrists, then slips a blindfold on her and climbs on top."
  samantha_jesse "Now comes the tricky part. You have to make them think you're doing exactly what you want to do with them, while you actually do the things they want you to do with them."
  samantha_jesse "You'll need to spend time figuring out what it is they need from you, before you start. Make sure you charge them for that consultation time, as its an integral part of the service you provide."
  samantha_jesse "You, on the other hand, aren't paying me. I'm doing this for free, to help out an aspiring new Domme ... and to get my hands on this sexy body of yours."
  samantha_jesse "So with you, I really am going to do what I want with you, now that I have you tied up and helpless. And what I want, is to see this sexy body of yours writhe in more pain."
  wt_image barista_domme_training_7
  samantha_jesse "Lick the crop."
  "Sam opens her mouth and wets the leather with her tongue, twitching nervously in anticipation of a continued cropping."
  wt_image barista_domme_training_8
  "A moment later, Sam is groaning in pain, but not from the crop. While Sam kissed the crop, Jesse quietly lit a candle, and starts dripping the wax over the blindfolded woman's bare skin ... *drip* *drip*"
  samantha.c "Oooohhh Ohhhh!!!"
  wt_image barista_domme_training_19
  samantha_jesse "See what I did there? Made you think one thing was coming, then surprised you with something else. It's a fun game you can play when you have someone helpless. Helps make sure they stay nervous and off balance around you."
  samantha_jesse "Just don't overuse the technique, or it ruins the surprise. Still hurts, though, doesn't it?"
  samantha.c "Yes!"
  samantha_jesse "I can make it hurt more by getting the candle closer to your skin.  Then the wax has less time to cool before it lands ... *drip* *drip*"
  wt_image barista_domme_training_8
  samantha.c "OWWW!!!!"
  samantha_jesse "Mmmmm, that's the type of helpless writhing I was hoping to see."
  samantha.c "Ooohhhhhh ... That really hurts!!"
  wt_image barista_domme_training_19
  samantha_jesse "Poor baby. Would you like relief from the hot stinging wax?"
  samantha.c "Yes, please!"
  samantha_jesse "Well, since you asked so nicely."
  wt_image barista_domme_training_9
  "Jesse puts away the candle and lowers herself between Sam's legs.  As her tongue touches Sam's pussy, Sam cries out, in surprise, relief and pleasure all at once."
  samantha.c "Oh GAWD!"
  samantha_jesse "Tsk tsk, silly. I'm not your god. Just your Mistress for this evening. And don't get too excited. I'm not going to let you cum. I just wanted to know what you taste like.  Delicious, by the way."
  wt_image barista_domme_training_20
  samantha_jesse "That's enough for today."
  "Jesse removes Sam's blindfold and cuffs, and helps her sit up right."
  samantha_jesse "Time to thank me properly for the lesson."
  wt_image barista_domme_training_21
  "Sam looks up at her uncertainly for the moment.  As she hesitates, Jesse bring the crop down hard on her ass  ... *THWACK*"
  samantha.c "OWW!!!!"
  samantha_jesse "I told you to thank me properly.  Get to it or I'll take the opportunity away."
  wt_image barista_domme_training_22
  "Jesse pushes her breast forward.  Sam gets the hint and removes the covering straps ..."
  wt_image barista_domme_training_10
  "... then starts licking."
  wt_image barista_domme_training_22
  "After a few minutes, Jesse pushes Sam's head away."
  samantha_jesse "Down on the floor."
  wt_image barista_domme_training_11
  "As Sam looks up at her, Jesse strips."
  samantha_jesse "You have something else your clients' want. Whether or not you choose to give it to them, make sure you remind them it exists - aloof and unattainable, or as a possible reward for good behavior, either way it reinforces your control over them."
  samantha_jesse "You want to lick my cunt, don't you?"
  "Sam nods."
  samantha_jesse "Don't let them get away without speaking when you ask a question. It's important to make them verbalize, to reinforce their submission. You want to lick my cunt, don't you?"
  samantha.c "Yes, I want to lick your cunt."
  samantha_jesse "Titles are important, too. I'm not just any woman right now. I'm your Mistress. You will address me as such."
  samantha.c "Yes, Mistress. I want to lick your cunt, Mistress."
  wt_image barista_domme_training_23
  samantha_jesse "Lucky for you, I'm in an accommodating mood.  Do have experience licking a woman's cunt?"
  samantha.c "Yes, Mistress."
  samantha_jesse "Go ahead then, lick my cunt. But do a good of it, or I'll get the crop out again."
  wt_image barista_domme_training_12
  "Despite her cool demeanor, Jesse has been turned on from the moment Sam and you showed up at her door, and the experience of dom'ing the would-be Domme has left her intensely horny."
  wt_image barista_domme_training_24
  "The feel of Sam's soft tongue on her sex soon has Jesse on the brink of cumming. She abandons all pretext of this being something that only Sam wants, and pushes the other woman back onto her back."
  wt_image barista_domme_training_13
  "Once she has her in position, Jesse hauls Sam's head up by the leash as she simultaneously grinds down on her face."
  samantha_jesse "Ohhh FUCCKKK!!!  YESSS!!!  Keep going.  Don't you stop!  Don't you dare stop!!!  Awwww YEESSSSS!!!!  FUCCKKKK!!!!!"
  "You're not sure exactly how many orgasms Jesse has, but you're confident that she's been fully compensated for her time and effort in training Sam."
  wt_image barista_domme_training_25
  samantha_jesse "So what do you think, sexy?  Do you think you're ready to try being a Domme?  You can even borrow my dungeon if you want.  I don't use it very often anymore."
  samantha.c "Mmmmm ... could you get me off first?  I can't think straight right now."
  "Jesse chuckles."
  samantha_jesse "No, silly.  I told you I'm not going to let you cum today."
  wt_image barista_domme_training_26
  "Sam looks confused."
  samantha.c "You really aren't going to let me cum? I just ate you out. I thought maybe ..."
  samantha_jesse "You thought I'd return the favor? Sorry, sexy. Domme's prerogative. As fun as it would be to see this sexy body of yours twitch in orgasm, I prefer the thought of you going home horny as hell and frigging yourself to sleep tonight thinking about me."
  wt_image barista_domme_training_14
  samantha_jesse "Consider that your final lesson. Give them what they paid for, but always leave them wanting a little bit more.  Just like you want my tongue flicking across your clit instead of your nipple. Now, back to my question. Do you think you're ready to try being a Domme?"
  samantha.c "I don't know. I can't think straight right now. What do you think?"
  "They both turn to look at you."
  $ title = "What do you think?"
  menu:
    "She's ready":
      player.c "You've taught her very well, Jesse. And you made the experience memorable enough that I know she'll spend a lot of time re-living the lessons and thinking about what she's learned. The rest will come with experience. I think you're ready to start your new career, Sam. I can look after the logistics and the marketing, for a small fee."
      samantha.c "Okay"
      wt_image barista_domme_training_2
      samantha_jesse "I have a client in mind. Someone I know would love to meet you. I'll tell him to look for your profile online. What are you going to call yourself?"
      wt_image barista_domme_training_16
      samantha.c "Call myself?"
      samantha_jesse "Yes. Your professional name.  Something intimidating, different than your real name."
      wt_image barista_domme_training_15
      samantha.c "I'm not sure.  'Samantha', maybe?"
      "You and Jesse both stifle your reactions as best you can."
      samantha_jesse "Well, okay sexy. Sure, that'd be fine. I'll tell him to look for Mistress Samantha."
      wt_image barista_domme_training_16
      samantha.c "Okay. But I can't see him tonight. There's something I need to do at home first."
      $ samantha.domme_status = 3
      call convert(samantha, "domme") from _call_convert_11
    "She needs to Domme you for practice":
      player.c "You've taught her very well, Jesse. And you made the experience memorable enough that I know she'll spend a lot of time re-living the lessons and thinking about what she's learned."
      player.c "I think, however, you should gain some experience as a Domme yourself, before you take on your first client, Sam."
      wt_image barista_domme_training_16
      samantha.c "Thanks. Who should I get experience with first, though?"
      player.c "Me. I'll let you practice on me, to build up your confidence. And I can offer constructive criticism afterwards, as necessary."
      samantha.c "Okay. That makes sense. Thank you for volunteering. But I can't practice on you tonight. There's something I need to do at home first."
      $ samantha.discussed_domme_train_you_sub = 2
  wt_image barista_domme_training_1
  "Jesse grins and leans into Sam. You can't hear what she whispers to her, but Sam moans quietly. You've got a pretty good idea what the 'something' is that Sam needs to do at home tonight."
  $ cassandra.discuss_barista = 5
  change player energy by -energy_short notify
  call character_location_return(samantha) from _call_character_location_return_639
  return

# Contact - Barista Domme Practice On You
label samantha_contact_practice_on_you:
  $ samantha.training_session()
  wt_image barista_phone_1
  player.c "Ready to continue your Domme training, Sam?"
  samantha.c "I guess so. I'm still nervous about whether I'll be any good at this."
  player.c "Don't be. I'm sure you'll be fine. I want you to remember your lessons, and use them on me today, as your sub."
  "Sam takes a deep breath."
  samantha.c "Okay. I've been thinking about how to do that, and doing some reading about what some submissive men like. I hope you enjoy what I've come up with for you."
  player.c "I'm sure I will."
  if samantha.domme_you_train_outfit == 1:
    samantha.c "I found a spot I think I can use, to meet with clients.  Meet me there in 30 minutes."
    "She gives you the address. Sam seems to be taking this new career seriously."
  else:
    samantha.c "Meet me at Jesse's dungeon in 30 minutes."
  summon samantha
  wt_image barista_domme_train_you_1
  "Sam greets you at the door wearing essentially nothing and carrying a dog chain."
  wt_image barista_domme_train_you_2
  if samantha.domme_you_train_outfit == 1:
    samantha.c "This is Jesse. This is her place. She's letting me borrow it."
    samantha_jesse "Hi."
  else:
    samantha.c "Jesse's here too."
    samantha_jesse "Hi."
  wt_image barista_domme_train_you_1
  samantha.c "Jesse's just going to watch, and only help me out if I get in trouble."
  samantha.c "Come in. Remove your clothes. There's a cage in the center of the room.  When you're naked, get in it and close the door. Do not speak."
  $ title = "What do you do?"
  menu:
    "Do as you're told":
      call samantha_contact_practice_on_you_continue from _call_samantha_contact_practice_on_you_continue
    "Decide maybe this isn't the right career for her":
      player.c "Sam"
      samantha.c "Didn't I tell you not to speak?"
      player.c "You did, but I'm not sure this is working out."
      samantha.c "Oh. Aren't I doing it right? I'm sorry. I was worried that this wasn't something I'd be good at. Maybe I should try and find another career?"
      $ title = "What do you say?"
      menu:
        "You'll be fine, let's continue":
          call samantha_contact_practice_on_you_continue from _call_samantha_contact_practice_on_you_continue_1
        "Yes, let's find something else for you":
          call samantha_contact_practice_on_you_find_something_else from _call_samantha_contact_practice_on_you_find_something_else
  change player energy by -energy_short notify
  call character_location_return(samantha) from _call_character_location_return_640
  return

label samantha_contact_practice_on_you_continue:
  wt_image barista_domme_train_you_2
  "You take off your clothes and get into the cage. You have to squat down and crawl to enter the cage, and once you're inside, you can't stand or sit up, forcing you to stay on all fours. You pull the cage door closed behind you. It clicks as it closes. You're not sure if its actually locked, or just hasped shut. While you're deciding whether to test it, Sam kneels down."
  samantha.c "Well, well. Look at what I have here. A naughty little slaveboy waiting for his Mistress."
  wt_image barista_domme_train_you_3
  samantha.c "I bet you've been looking forward to this. Looking forward to seeing your Mistress. Wondering if I would come and let you out of your cage? Wondering if you would get to see my pussy? Wondering if you'd get to touch my pussy?"
  wt_image barista_domme_train_you_4
  "Instinctively, you reach out your hand."
  samantha.c "Bad boy. No touching without permission. Keep your hands to yourself, or I'll keep you locked up in this cage for the rest of our time together. Do you want that? Do you want to just sit there in that cage all day?"
  "You shake your head."
  samantha.c "You have permission to speak when I ask you a question.  Do you want to sit in there all day?"
  player.c "No"
  samantha.c "Bad boy! Show your Mistress some respect, or you'll be in the cage blindfolded for the rest of today.  Last chance to answer me properly."
  player.c "No, Mistress. I don't want to be in this cage all day."
  wt_image barista_domme_train_you_5
  "Mistress opens the cage and points to the floor at her feet."
  samantha.c "Crawl out.  Wait here on all fours with your head down down."
  wt_image barista_domme_train_you_6
  "As you get into position, at first all you can see are Mistress' feet.  Then she bends squats down in from of you. You feel the cold metal being looped around your neck as your eyes are drawn to her beautiful pussy, exposed in front of you."
  samantha.c "I told you to keep your head down."
  "She brings her hand down hard on your ass ... *SMACK*"
  wt_image barista_domme_train_you_7
  "Mistress kneels in front of you, putting her bare pussy directly in front of your face."
  samantha.c "Is this the reason you disobeyed me? Were you so desperate to get a look at my pussy that you disobeyed me and raised your head?"
  player.c "Yes, Mistress."
  samantha.c "Yes, Mistress what?"
  player.c "Yes, Mistress, I disobeyed you because I couldn't help myself from looking at your beautiful pussy."
  samantha.c "Does it make you horny, looking at my pussy?"
  player.c "Yes, Mistress, looking at your beautiful pussy is making me very horny."
  wt_image barista_domme_train_you_5
  samantha.c "Stand up and show me."
  wt_image barista_domme_train_you_8
  "As you stand up, Mistress wraps the cold chain around your hard cock."
  samantha.c "Is this hard on for me?"
  player.c "Yes, Mistress."
  samantha.c "Mistress' pussy is only for girls, silly boy. Don't you know that?"
  player.c "Yes, Mistress."
  samantha.c "What do you know?"
  player.c "Mistress' beautiful pussy is only for girls, not for silly boys."
  samantha.c "But you have a hard on for Mistress anyway, don't you?"
  player.c "Yes, Mistress, I have a hard on for you, Mistress."
  "Mistress starts rolling the cold metal of the dog chain back and forth along your cock."
  samantha.c "What do you think Mistress will do with this hard on, silly boy?"
  player.c "I don't know, Mistress."
  "Mistress pulls on the chain, tightening it painfully around your cock."
  player.c "Owww!!"
  samantha.c "Wrong answer, silly boy."
  "You try and think, then realize what she's getting at."
  player.c "This hard on is yours, Mistress. I think Mistress will do whatever she wants with this hard on."
  samantha.c "Better answer, you silly boy. That's right. This is my hard on, and I'll do whatever I want with it."
  "She resumes rolling the metal chain back and forth along your shaft. After a few minutes of this treatment, you feel your balls start to tense, and realize you're close to coming."
  "Mistress realizes it too, and grips the base of your shaft tightly with her gloved hand, denying you both the sensation of her skin and the sensation of the chain, and keeping you from climaxing."
  samantha.c "You don't have permission to cum, silly boy, but if you beg nicely, I may let you cum. Otherwise, I'm going to start squeezing you tighter until I ruin this orgasm."
  $ title = "What do you do?"
  menu:
    "Beg for an orgasm":
      player.c "Please, Mistress. May I please have an orgasm, Mistress? May I please offer you my cum, Mistress? Please?"
      wt_image barista_domme_train_you_10
      "Mistress slips off one glove and starts stroking your shaft gently with her bare hand. As you quickly climax, she lets go of the death grip at the base of your cock, allowing your cum to spurt up and over her, landing on her face, her hair, and the floor behind her."
      player.c "[player.orgasm_text]"
      wt_image barista_domme_train_you_11
      samantha.c "I wouldn't have let you cum like that if you'd really been a client. But you've been helping me so much, I thought I owed it to you."
      player.c "Thank you, Mistress."
      samantha.c "You don't have to call me that anymore.  I think we're done with the training today, if that's okay with you?"
      player.c "Of course."
      $ samantha.handjob_count += 1
      $ samantha.facial_count += 1
      orgasm
    "Stay silent":
      "Mistress smiles as she realizes you're staying silent. Still holding the base of your cock tightly, she squeezes your balls with her other hand. Your body tries to orgasm, but can't properly, leaving a frustrating, unsatisfied feeling behind."
      $ samantha.temporary_count = energy_long.value - energy_short.value
      change player energy by -samantha.temporary_count notify
  samantha.c "So what did you think? I know I should have spent more time before our session, finding out what you wanted, and preparing accordingly. I'll make sure I do that for real clients. But other than that, what do you think?"
  $ samantha.discussed_domme_train_you_sub = 3
  $ title = "What do you think?"
  menu:
    "She's ready to be a Domme":
      player.c "I think you're ready to start your new career, Sam."
      wt_image barista_domme_training_2
      samantha_jesse "I agree! You did great."
      "It's Jesse, piping up from the shadows in a corner of a room. You'd almost forgotten she was there."
      wt_image barista_domme_train_you_1
      samantha.c "Thanks! What do I do now?"
      player.c "We get you some clients. I can look after the logistics and the marketing, for a small fee."
      samantha.c "Okay"
      wt_image barista_domme_training_2
      samantha_jesse "And I have a client in mind for you already. Someone I know would love to meet you. I'll tell him to look for your profile online. What are you going to call yourself?"
      wt_image barista_domme_training_1
      samantha.c "Call myself?"
      samantha_jesse "Yes. Your professional name. Something intimidating, different than your real name."
      samantha.c "'Samantha', maybe?"
      wt_image barista_domme_training_15
      "You and Jesse both stifle your reactions as best you can."
      samantha_jesse "Well, okay sexy. Sure, that' woul'd be fine. I'll tell him to look for Mistress Samantha."
      player.c "And I'll get started finding you your first client.  I'll let you know when I have it arranged."
      wt_image barista_domme_training_1
      samantha.c "Okay.  Thanks."
      $ samantha.domme_status = 3
      call convert(samantha, "domme") from _call_convert_12
    "This isn't the right career for her":
      player.c "I'm not sure this is the right career for you."
      samantha.c "I didn't do it right, did I? I'm sorry. I was worried that this wasn't something I'd be good at."
      wt_image barista_domme_training_2
      samantha_jesse "Don't listen to him! You did great."
      "It's Jesse, piping up from the shadows in a corner of a room.  You'd almost forgotten she was there."
      wt_image barista_domme_training_1
      samantha.c "No, he's on to something. He's right. I'm going through the motions, but I'm not really feeling it inside. Maybe I should try and find another career?"
      call samantha_contact_practice_on_you_find_something_else from _call_samantha_contact_practice_on_you_find_something_else_1
  return

label samantha_contact_practice_on_you_find_something_else:
  player.c "I think that would be best.  Let's chat more at the coffee shop, after we both have a chance to think of something that may be a better fit for you."
  samantha.c "Okay"
  $ samantha.conversation_event = 7
  $ samantha.domme_status = 5
  $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  return

# Contact - Barista Domme Actions
label samantha_contact_domme_actions:
  $ samantha.training_session()
  $ samantha.domme_outfit += 1
  # first client
  if samantha.domme_outfit == 1:
    "Against absolutely all odds, the first clients to ask about Mistress Samantha's services are a young lesbian couple looking to spice up their relationship on their anniversary."
    wt_image barista_phone_1
    samantha.c "Wow. I can't believe that. I was worried that only guys would be interested in my services."
    player.c "And they're both newbies, too, looking to experiment with submission, so they shouldn't be into anything more intense than you're ready to handle."
    samantha.c "When and where do I meet them?"
    player.c "Follow up with them first, to find out what they're interested in. I'll look after the rest of the logistics."
    wt_image boudoir.image
    "You set Sam up to meet her first clients in your boudoir. They're not looking for anything intense, so Sam doesn't need access to any heavy equipment. Holding the session in your boudoir should help of them relax. And by having the visit in your house, you'll be close if Sam needs any help. After you get Sam set up, you make yourself scarce."
    wt_image barista_domme_outfit_1_1
    "When her clients arrive, she directs them to the bathroom to change, and waits on the bed for them. They eventually emerge wearing skimpy lingerie and giggling nervously."
    samantha.c "Come here."
    wt_image barista_domme_outfit_1_2
    samantha.c "You are not to speak, not to touch, not to move without my permission. Is that understood?"
    samantha_domme_client_1_1 "Yes"
    samantha_domme_client_1_2 "Yes"
    samantha.c "The correct response is yes, Mistress."
    samantha_domme_client_1_1 "Yes, Mistress."
    samantha_domme_client_1_2 "Yes, Mistress."
    wt_image barista_domme_outfit_1_3
    samantha.c "Lie down, I'm going to undress your girlfriend."
    samantha_domme_client_1_1 "Yes, Mistress."
    samantha.c "This was your idea, wasn't it?  To hire me?"
    samantha_domme_client_1_2 "Yes, Mistress."
    wt_image barista_domme_outfit_1_4
    samantha.c "Is this what you were hoping for? To see your girlfriend lying submissively underneath you, ordered to use her tongue to please you?"
    samantha_domme_client_1_2 "Yes, Mistress."
    wt_image barista_domme_outfit_1_5
    samantha.c "Or maybe you were secretly hoping that I'd put you here, behind your girlfriend, and make you eat out her ass until her pussy juices are running down her cunt and soaking your chin?"
    samantha_domme_client_1_2 "Oh yes, Mistress!"
    wt_image barista_domme_outfit_1_6
    samantha.c "I think you've both enjoyed far too much of each other's tongues. Time to put you to proper work, the sort of work two slutty lesbians like you are best suited for."
    wt_image barista_domme_outfit_1_7
    samantha.c "Both of you start rocking your hips, now. The first one of you to stop is going to get a red ass. And if either of you cum before I do, I'm putting you both over my knee and you'll both be leaving here with a red ass."
    wt_image barista_domme_outfit_1_8
    "When the clients have left, you ask Sam how it went."
    samantha.c "Okay, I guess. They seemed happy.  It was just ... I don't know, awkward? They were both very much in love. I felt like a third wheel."
    player.c "They wanted you there. You gave them something they couldn't get on their own. You helped them."
    samantha.c "I guess. Helped them tick something off their bucket list, anyway."
    player.c "And they paid you. Remember that. Work isn't always about helping people."
    samantha.c "I know."
    player.c "50 of their fees are for me."
    samantha.c "I remember. Here you go."
    if not player.has_tag('whores_once'):
      add tags 'whores_once' to player  # note: this is because the end_week label in bethany's script won't capture these Domme sessions
    $ title = "What do you tell her?"
    menu:
      "Keep at it":
        call samantha_contact_domme_actions_keep_at_it from _call_samantha_contact_domme_actions_keep_at_it
      "Maybe this isn't for you":
        call samantha_contact_domme_actions_maybe_isnt from _call_samantha_contact_domme_actions_maybe_isnt
  # second client if Jesse trained her or you let her domme you, otherwise skips to final client
  elif samantha.domme_outfit == 2:
    if samantha.discussed_domme_train_you_sub == 3 or cassandra.discuss_barista == 5:
      "The next client to contact Mistress Samantha appears to be the man referred by Jesse. You pass his details on to Sam."
      samantha_domme_client_2 "{i}Dear Mistress Samantha, My former Mistress suggested I contact you. I am a lowly dog. I'm not worthy to be your pet. If you choose to accept me as your pet, even for a couple of hours, you will find me faithful, obedient, grateful, and generous. ~ dog boy{/i}"
      wt_image barista_phone_1
      samantha.c "Do you think I'm ready for a hard core BDSM player?"
      player.c "I do. So does Jesse."
      samantha.c "Okay. I'll try. Perhaps I should meet him at Jesse's dungeon? I think she has all the equipment, and it sounds like he enjoyed meeting her there."
      player.c "That's a good idea."
      wt_image barista_domme_outfit_2_1
      "'dog boy' knows the location well, having previously served Jesse in the same spot. Mistress Samantha finds him lying on his side in the cage as she enters."
      wt_image barista_domme_outfit_2_2
      samantha.c "Wake up boy. Are you ready to play?"
      samantha_domme_client_2 "Rruufff!!!"
      "He's wearing a special hood he brought with him, shaped like a dog's head. He's definitely a hard core player. Perhaps Jesse let Sam know what to expect, because she takes it in stride."
      wt_image barista_domme_outfit_2_3
      samantha.c "Let's get your leash on."
      samantha_domme_client_2 "Rruff!!  Rruff!!"
      "dog boy barks eagerly as Mistress Samantha fastens the leash to his collar."
      wt_image barista_domme_outfit_2_4
      samantha.c "Whoa!  Down boy!  Sit.  Stay."
      samantha.c "If you want me to take you for a walk, you need to listen. No moving until Mistress says you can move. And no jumping up on me, ever!"
      samantha_domme_client_2 "Rrrrmmmm"
      "dog boy whimpers, waiting for Mistress Samantha's permission to move."
      samantha.c "Okay, let's go.  No pulling on the chain."
      samantha_domme_client_2 "Rruff!!!"
      "dog boy barks excitedly, and follows Mistress Samantha as she leads him on his walk."
      wt_image barista_domme_outfit_2_5
      samantha.c "Heel boy. We're going to do that again. This time, no straining on the leash. You walk beside me, not in front of me, when I'm taking you for a walk. Do you understand boy?"
      samantha_domme_client_2 "Rrruff!"
      samantha.c "Okay.  Let's go boy."
      "Mistress Samantha walks him around the room a few more times, disciplining him when he pulls on the leash, complimenting him when he crawls obediently at her side."
      wt_image barista_domme_outfit_2_6
      "When she's finished, she squats down and starts petting him, rubbing his head, chest, and under his chin."
      samantha.c "Good boy.  Did you enjoy your walk?"
      samantha_domme_client_2 "Rruff!!"
      samantha.c "Are you ready for your treat now?"
      samantha_domme_client_2 "Rrufff!!!!  Rrufff!!!!  Rrufff!!!!"
      wt_image barista_domme_outfit_2_7
      samantha.c "Okay boy.  Here's your treat. Wait! Wait boy. No eating it until Mistress says you can."
      samantha_domme_client_2 "Rrrrmmmm"
      "dog boy whines, desperately sniffing and snuffling at Mistress Samantha's exposed pussy, but not daring to touch it until allowed, for fear that the treat will be taken away."
      wt_image barista_domme_outfit_2_8
      samantha.c "Okay boy.  Go ahead."
      "Mistress Samantha closes her eyes and pets the back of dog boy's head as he begins frantically licking and snuffling into her sex. She doesn't cum from the experience, but she gets wet enough to satisfy dog boy's desperate attempts to lap up all the liquid her pussy can produce for him."
      wt_image barista_domme_train_you_1
      "Afterwards, you check in on her?"
      player.c "How did that go?"
      samantha.c "I don't know. I get how I helped him, I do. I understand how he can't get that from just anyone. It's just a little intense. And weird."
      player.c "And profitable. Drop my cut off on your way home, okay?"
      samantha.c "Okay"
      $ title = "What do you tell her?"
      menu:
        "Keep at it":
          call samantha_contact_domme_actions_keep_at_it from _call_samantha_contact_domme_actions_keep_at_it_1
        "Maybe this isn't for you":
          call samantha_contact_domme_actions_maybe_isnt from _call_samantha_contact_domme_actions_maybe_isnt_1
    else:
      jump samantha_contact_domme_actions
  # final client
  elif samantha.domme_outfit == 3:
    "The next client to contact Mistress Samantha is looking for some simple tease and denial.  Pretty tame stuff as far as kinks go."
    wt_image barista_phone_1
    samantha.c "Okay, I should be able to handle that."
    wt_image barista_domme_outfit_3_1
    "The client is already there and waiting for Sam when she arrives."
    samantha.c "Oh. You're early."
    samantha_domme_client_3 "I couldn't wait."
    wt_image barista_domme_outfit_3_2
    "Fortunately Mistress Samantha is already dressed for the session, so she starts it right there."
    samantha.c "Couldn't wait for this, naughty boy? Tsk tsk. If you want to see more, you're going to need to learn how to follow instructions better."
    samantha_domme_client_3 "Yes, Mistress."
    wt_image barista_domme_outfit_3_3
    "Mistress Samantha takes him inside, sits him on a chair, ties a red gag around his mouth, then begins her tease routine.  Against instructions, he reaches out and grabs her ass as she wiggles it in front of him."
    samantha.c "Hey!  No touching!"
    wt_image barista_domme_outfit_3_4
    samantha.c "If you want to keep looking at this, you look with your eyes only. Is that understood?"
    "He replies through the gag,"
    samantha_domme_client_3 "Yeth, Mithtreth."
    wt_image barista_domme_outfit_3_5
    "Mistress Samantha goes back to her teasing, including a short lap dance."
    samantha.c "Do you like feeling Mistress' soft ass against you, naughty boy?  Hey!  Hands off the tits!"
    wt_image barista_domme_outfit_3_6
    samantha.c "You can have one quick lick, since you find my tits so irresistible, but then you have to promise. No more touching or Mistress is going to leave you."
    samantha_domme_client_3 "Yes, Mistress. I promise. Thank you!"
    wt_image barista_domme_outfit_3_7
    "After the nipple lick, Mistress Samantha re-applies the gag and unzips his fly, exposing his hard on."
    samantha.c "Tsk tsk. What a naughty boy. Sporting a big hard on like that. Naughty boys aren't supposed to get hard ons for their Mistress. Naughty boys are supposed to control themselves."
    wt_image barista_domme_outfit_3_8
    "Mistress Samantha kneels down and lightly strokes her fingers along the hard cock."
    samantha.c "Naughty boys need to control themselves, or Mistress will take her body away and not let the naughty boy look at it anymore. You want to keep looking at Mistress, don't you naughty boy?"
    "The client nods vigorously as Mistress Samantha teases him with the tips of her fingers and gentle scratches with her finger nails."
    wt_image barista_domme_outfit_3_9
    "Unfortunately, Sam doesn't have a lot of experience with men, and even less with recognizing the onset of a male orgasm. As she leans in to scratch her nails along the underside of his cock, he lets himself go, his cum spurting up and onto her face."
    samantha.c "Aggg! You weren't supposed to cum!  You were supposed to control yourself!!"
    samantha_domme_client_3 "Thorry, Mithtreth."
    wt_image barista_domme_outfit_3_10
    "After she's cleaned up and sent the client home, she calls you from the car."
    player.c "How did it go?"
    samantha.c "Not well.  He was a bit of a jerk. I need to take a break and think things over. I think I may actually be able to get pretty good at this. Even despite the jerks."
    samantha.c "But its so intense and so personal. Each of these sessions is taking a lot out of me, emotionally. I need to reflect on whether I really want to keep with this or not."
    player.c "How about we catch up at the coffee shop, after I have a chance to think about things?"
    samantha.c "Okay. I'll drop your cut off on my way home."
    $ samantha.conversation_event = 11
    $ samantha.domme_status = 4
    $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  $ player.domme_income += 50
  change player energy by -energy_short notify
  return

label samantha_contact_domme_actions_keep_at_it:
  player.c "You did good work today. It'll get easier as you get more experience."
  samantha.c "Maybe. I hope so."
  return

label samantha_contact_domme_actions_maybe_isnt:
  player.c "Maybe this work isn't for you, Sam."
  samantha.c "I'm thinking probably it isn't. Maybe I should try and find another career?"
  player.c "Let's chat more at the coffee shop, after we both have a chance to think of something that may be a better fit for you."
  samantha.c "Okay"
  $ samantha.conversation_event = 7
  $ samantha.domme_status = 4
  $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  call unconvert(samantha, 'domme') from _call_unconvert_17
  return

# Contact - Check On Whore
label samantha_check_whore:
  wt_image barista_phone_1
  player.c "How’s the sexual concierge work going?"
  samantha.c "I’m not sure it’s going to be right for me."
  player.c "Let’s give it a bit and see how it works out."
  return

# Contact - Pimp Barista Out
label samantha_contact_pimp:
  $ samantha.training_session()
  $ samantha.whore_outfit += 1
  # first client
  if samantha.whore_outfit == 1:
    "You screen requests for 'Samantha' until you find one you think Sam will respond well to."
    wt_image barista_phone_1
    player.c "Hi, Sam. Or should I say, 'Samantha'. I have your first client lined up. He's a young man with little experience with women. You should be perfect to help him out."
    samantha.c "Okay. I'll see what I can do."
    wt_image barista_whore_outfit_1_1
    samantha_whore_client_1 "Hi, Samantha?"
    samantha.c "Yes, I guess that's me. I understand you were looking for some help?"
    samantha_whore_client_1 "Come in."
    wt_image barista_whore_outfit_1_2
    samantha.c "So what were you hoping for help with?"
    samantha_whore_client_1 "Just, you know ... sex."
    samantha.c "Have you been with many women?"
    samantha_whore_client_1 "No. Not many."
    samantha.c "Is there anything in particular you want to learn?"
    samantha_whore_client_1 "I don't know. I was just hoping, maybe you could blow me? And then let me fuck you?"
    wt_image barista_whore_outfit_1_3
    samantha.c "That's simple enough. Sure, I can do that."
    samantha_whore_client_1 "Here's your money. Your manager said this should cover your time."
    wt_image barista_whore_outfit_1_4
    samantha.c "Thanks. What about kissing? Do have much practice with that?  Did you want me to show you how to do it?"
    samantha_whore_client_1 "Uh. Okay. Would you mind changing first? Maybe into something a bit sexier?"
    samantha.c "Okay. Sure. That'll probably help me look more like a straight woman. Just let me duck into the bathroom and change."
    wt_image barista_whore_outfit_1_5
    "You told Sam that men often feel more comfortable, sexually, around a woman wearing lingerie, so she came prepared with some black silk stockings."
    wt_image barista_whore_outfit_1_6
    "When she returns, her client is sitting in his chair with his hard on out."
    samantha_whore_client_1 "I got so excited thinking about you. I really need you to touch me."
    samantha.c "Oh, okay."
    samantha_whore_client_1 "That feels nice. Did you say you weren't straight?"
    samantha.c "I guess you really don't have much experience with women if you couldn't tell."
    samantha_whore_client_1 "That is so hot! Could you blow me now?"
    wt_image barista_whore_outfit_1_7
    samantha.c "This isn't going to teach you a lot about women. Would you like me to show you some other things, first?"
    samantha_whore_client_1 "I really don't think I could concentrate on anything else right now. I really need to feel your mouth on me."
    samantha.c "Oh. All right, then."
    wt_image barista_whore_outfit_1_8
    samantha_whore_client_1 "Ohh gawd. That feels really good. Ohh, yes! Just like that! Wait .. wait. Stop."
    samantha.c "Is something wrong?"
    samantha_whore_client_1 "No.  It's just if you keep doing that, I'm going to cum, and I really want to fuck you first. Could you stand up?"
    wt_image barista_whore_outfit_1_9
    samantha_whore_client_1 "You are so beautiful, Samantha. I just have to be inside you."
    samantha.c "Thanks. This isn't really the best position. It's a little awkward for me. How about we go to the bedroom and I'll show you how to make love?"
    wt_image barista_whore_outfit_1_10
    "When they get to the bedroom, he pushes her down onto the bed and thrusts himself inside her."
    samantha.c "Whoa!  Not so fast."
    samantha_whore_client_1 "Don't women like it when a guy takes charge?"
    samantha.c "Sometimes, but you need to make sure she's ready for you first."
    samantha_whore_client_1 "I'm just so hot for you baby, I couldn't hold myself back."
    wt_image barista_whore_outfit_1_11
    "He literally can't hold himself back."
    samantha_whore_client_1 "Aahhhhh!!!!"
    samantha.c "Shit! Did you just cum in me?"
    samantha_whore_client_1 "Yeah. Aren't you on protection?"
    samantha.c "Yes, but that's not the point. You need to tell a woman you're going to do that."
    samantha_whore_client_1 "I thought you knew that would happen once I put my thing in you?"
    samantha.c "No. You need to talk about that with your partner."
    samantha_whore_client_1 "Sorry. You're so damn beautiful, I wasn't thinking straight. "
    wt_image barista_whore_outfit_1_2
    samantha.c "It's okay. You're just learning. You still have a few minutes of my time. Can I help you learn more about girls?"
    samantha_whore_client_1 "Not right now. I'm pretty tired after that. I think I'm just going to go to bed."
    wt_image barista_whore_outfit_1_12
    "After she leaves, Sam checks in with you."
    player.c "How did it go?"
    samantha.c "I'm not sure. He certainly needs help, but I don't think I was able to do much for him. He wasn't really listening to me, and I'm not sure he learned anything. Maybe I'm not well suited for this work?"
    $ title = "What do you tell her?"
    menu:
      "Keep at it":
        call samantha_contact_pimp_keep_at_it from _call_samantha_contact_pimp_keep_at_it
      "Maybe this isn't for you":
        call samantha_contact_pimp_maybe_isnt from _call_samantha_contact_pimp_maybe_isnt
  # second client
  elif samantha.whore_outfit == 2:
    "There are lots of requests for 'Samantha's' services, but it takes a while before you get one you think she's ready for."
    wt_image barista_phone_1
    player.c "Hi Sam. I have your next client lined up. He's a lonely man who needs companionship."
    samantha.c "Is he a widower?"
    player.c "No, but his wife travels a lot on business, leaving him alone in their house."
    samantha.c "Is this really appropriate? Should he be seeing a sexual professional on his own while she's away? Does she even know he's doing this?"
    player.c "You don't want to break up their marriage, do you? If he needs companionship while she's away, what are his options? Find a girlfriend and cheat on his wife with her? Don't you think it's better for him to stay faithful to his marriage and make use of your services to deal with his problem?"
    samantha.c "I suppose."
    player.c "I'll send you his address."
    wt_image barista_whore_outfit_2_1
    samantha_whore_client_2 "Wow. You're just what the doctor ordered!"
    samantha.c "Awww. How sweet! Are you sure my sexuality isn't going to be a problem?"
    samantha_whore_client_2 "Your sexuality looks amazing to me. Come on in. Here's your money. The bathroom is right over there. Go change into something sexy for me. I'll be waiting for you in the kitchen."
    wt_image barista_whore_outfit_2_2
    "'Samantha' checks her payment ..."
    wt_image barista_whore_outfit_2_3
    "... then changes into her working clothes."
    wt_image barista_whore_outfit_2_4
    samantha_whore_client_2 "Wow. You really are some sexy medicine!  Turn around so I can see all of you."
    wt_image barista_whore_outfit_2_19
    samantha.c "Thanks. I understand you've been lonely, because your wife isn't around?"
    samantha_whore_client_2 "I sure have, but I don't want to talk about her right now. Just turn around, slowly, so I can get a good look at you."
    samantha.c "Oh, okay."
    wt_image barista_whore_outfit_2_20
    samantha_whore_client_2 "Lean forward.  I want to check out your ass."
    samantha.c "I guess your wife hasn't been able to do this for you for a while?"
    samantha_whore_client_2 "Not the way you are, sweetheart."
    wt_image barista_whore_outfit_2_21
    samantha_whore_client_2 "Come here and let me get a good look at those sweet titties."
    samantha.c "Do you miss your wife's breasts?"
    wt_image barista_whore_outfit_2_5
    samantha_whore_client_2 "I'd miss them a lot more if they looked like yours."
    wt_image barista_whore_outfit_2_14
    samantha_whore_client_2 "Too bad her ass doesn't feel like yours, either"
    wt_image barista_whore_outfit_2_22
    samantha_whore_client_2 "I'll tell you what I really miss. I miss the lap dances I used to get when I was the one traveling out of town a lot."
    samantha.c "Oh? Would your wife welcome you home with a lap dance?"
    wt_image barista_whore_outfit_2_6
    samantha_whore_client_2 "I sure wanted her to. Let me show you want I like. That's it. Just wiggle your hips around like that. Make it slow and seductive for me. Do you know how I always wanted the lap dances to end?"
    samantha.c "How?"
    wt_image barista_whore_outfit_2_23
    samantha_whore_client_2 "With the dancer on her knees in front of me."
    wt_image barista_whore_outfit_2_7
    samantha.c "Like this?"
    samantha_whore_client_2 "Close"
    wt_image barista_whore_outfit_2_15
    "He pulls down his pants, exposing his hard on."
    samantha_whore_client_2 "I prefer it with her hand on my cock."
    samantha.c "Like this?"
    wt_image barista_whore_outfit_2_8
    samantha_whore_client_2 "Yeah. Spit on it to get it wet, and start stroking me."
    samantha.c "Has it been a long time since you've had any attention?"
    samantha_whore_client_2 "Too long."
    samantha.c "That must be frustrating."
    samantha_whore_client_2 "I'll tell you what else is frustrating."
    samantha.c "What?"
    samantha_whore_client_2 "Looking at that beautiful mouth of yours, and not seeing it wrapped around my cock. Don't be a tease, Samantha."
    samantha.c "Oh. Sorry. I wasn't meaning to ..."
    wt_image barista_whore_outfit_2_16
    "He takes her by the head and guides her on to his cock."
    samantha_whore_client_2 "Less talking. More sucking."
    wt_image barista_whore_outfit_2_10
    "She does her best to pleasure him, using her mouth and tongue on his cock ..."
    wt_image barista_whore_outfit_2_24
    "... and balls ..."
    wt_image barista_whore_outfit_2_9
    "... but he's not completely satisfied with her technique."
    samantha_whore_client_2 "Can't you take me deeper?"
    wt_image barista_whore_outfit_2_11
    samantha.c "I'm sorry.  I'm probably not as good at this as your wife, but I'll try."
    wt_image barista_whore_outfit_2_17
    "Slowly and carefully, Sam gets as much of his member inside her as she can, until her gag reflex kicks in."
    wt_image barista_whore_outfit_2_11
    samantha_whore_client_2 "Was that it?"
    samantha.c "I didn't want to choke."
    wt_image barista_whore_outfit_2_16
    samantha_whore_client_2 "I'd love to see you choke."
    wt_image barista_whore_outfit_2_18
    "Holding her firmly by the back of the head, he pulls her head down and holds it there as Sam struggles to not throw up."
    wt_image barista_whore_outfit_2_25
    "When he finally lets her up, Sam gasps for air."
    wt_image barista_whore_outfit_2_11
    samantha.c "I'm sorry, I don't think I can do this as well as your wife can.  Maybe I can help you out in some other way?"
    wt_image barista_whore_outfit_2_26
    samantha_whore_client_2 "How about you lean over this chair and I'll fuck you silly?"
    samantha.c "Okay"
    wt_image barista_whore_outfit_2_12
    "He starts fucking her. Slowly at first, then faster. Then slow again, taking his time. It's the longest fucking Sam's ever had, in her admittedly limited experience with men."
    "The lubricant she applied before the session is almost worn off, and she worries she might be getting too dry for him. He doesn't seem to notice, or if he does, he doesn't care. Sam closes her eyes and tries to relax, waiting for him to finish."
    "She's not sure how much time goes by, but eventually she feels his grip on her hips tighten, and a very quiet groan escape his throat."
    wt_image barista_whore_outfit_2_13
    "He pulls her up and sits down on the chair."
    samantha.c "We're a bit over my time, but did you want to talk about anything? About feeling lonely? About whether that helped?"
    samantha_whore_client_2 "You helped great, beautiful. You need to get out of here now. My wife will be home from the airport soon."
    samantha.c "But ... if she was coming home today, why didn't you just wait for her?"
    samantha_whore_client_2 "Don't worry. You've got me nicely riled up. When she gets home, I'll give her the best fuck she's had this year, thinking about your sweet body the whole time."
    wt_image barista_whore_outfit_1_12
    "After she leaves, Sam checks in with you."
    player.c "How did it go?"
    samantha.c "He seemed really happy with me, and said it helped his marriage. I'm not sure it was really healthy for his relationship, though. I didn't feel good about it. Maybe I'm not well suited for this work?"
    $ title = "What do you tell her?"
    menu:
      "Keep at it":
        call samantha_contact_pimp_keep_at_it from _call_samantha_contact_pimp_keep_at_it_1
      "Maybe this isn't for you":
        call samantha_contact_pimp_maybe_isnt from _call_samantha_contact_pimp_maybe_isnt_1
  # slaver client
  elif samantha.whore_outfit == 3:
    "After her discomfort with the previous client, you screen new requests carefully until you find one 'Samantha' should be able to look after without any qualms."
    wt_image barista_phone_1
    player.c "Hi Sam. I have a new client for you. He's single. He's a traveling businessman. Never stays in one place too long, and doesn't have the opportunity to form a proper relationship."
    player.c "He's very interested in meeting you as he says you sound potentially quite special. The sort of woman he always hopes to find on his travels."
    samantha.c "He knows I'm a lesbian, right?"
    player.c "He's not looking for a girlfriend, Sam. He doesn't have the lifestyle for one anyway. He's looking for a companion for a few hours, to help him meet some basic human needs."
    samantha.c "Okay. I'll see him."
    wt_image barista_whore_outfit_3_1
    "Taking a cue from her previous clients, 'Samantha' puts on her lingerie before meeting her new client. She figures that'll also help distract him from her sexual orientation."
    samantha_whore_client_3 "Ahhhh. You are a fine specimen. You're every bit as exquisite as I hoped you'd be."
    samantha.c "Thank you. My sexuality's not a problem for you, is it?"
    samantha_whore_client_3 "Your sexuality?"
    samantha.c "Me being a lesbian. It's not off-putting, is it?"
    samantha_whore_client_3 "Interesting. No, that's not off-putting at all."
    samantha.c "Oh good! Was there anything in particular you wanted today?"
    wt_image barista_whore_outfit_3_2
    samantha_whore_client_3 "Just to get to know you better. What are your measurements?"
    samantha.c "I'm sorry?"
    samantha_whore_client_3 "Your height. How tall are you?"
    samantha.c "5 foot 8."
    samantha_whore_client_3 "And your bra size?"
    samantha.c "34 double D."
    samantha_whore_client_3 "Weight?"
    samantha.c "Maybe 120 pounds?"
    samantha_whore_client_3 "Hips and waist?"
    samantha.c "I've never measured."
    samantha_whore_client_3 "Guess"
    samantha.c "Maybe 24 36?"
    samantha_whore_client_3 "That looks about right."
    wt_image barista_whore_outfit_3_3
    samantha.c "I was told you were looking for a companion?"
    samantha_whore_client_3 "Indeed I am. Sit here with me. May I kiss you?"
    samantha.c "Okay"
    wt_image barista_whore_outfit_3_4
    samantha.c "Mmmm. That was nice. You don't seem to need any help with kissing."
    samantha_whore_client_3 "Neither do you. Are these your only piercings?"
    samantha.c "What?"
    samantha_whore_client_3 "Your nipples."
    samantha.c "Ohhh"
    "Sam exhales in surprise when he pinches one."
    samantha_whore_client_3 "Are they the only part of you that's been pierced?"
    samantha.c "No, I also pierced my clit hood."
    wt_image barista_whore_outfit_3_5
    samantha_whore_client_3 "Ah, yes. That should be fine. Did your owner order the piercings?"
    samantha.c "My owner? No. I don't have an owner. I did them myself. A girlfriend recommended it. I'm so glad she did. It makes everything extra sensitive."
    samantha_whore_client_3 "Good, good. Sensitive is definitely a bonus. I need to taste you."
    samantha.c "Oh, okay."
    wt_image barista_whore_outfit_3_6
    samantha_whore_client_3 "Mmmm. Very good. You taste very healthy. Do you always get wet this easily?"
    samantha.c "Uhhh ... well, with my ex I did. It's been a while since I've been with anyone, so I was sort of imagining that you were her. I hope you don't mind?"
    samantha_whore_client_3 "That's fine.  You say she was your ex.  Do you have any current relationships?"
    samantha.c "Not right now. I'm not cheating on anyone, if that's what you're worried about. This is just a career change I'm trying out. My friend is the only one who knows I'm doing this so far."
    samantha_whore_client_3 "You mean your agent? The man who set up our meeting?"
    samantha.c "Yes"
    samantha_whore_client_3 "Very good."
    wt_image barista_whore_outfit_3_7
    samantha_whore_client_3 "Can you show me what you know about sex now?"
    samantha.c "Okay, sure. Would you like a blow job to start?"
    samantha_whore_client_3 "Yes, let's start with that."
    wt_image barista_whore_outfit_3_8
    "As 'Samantha' leans in to take him into her mouth, he gathers up her hair in his hand."
    wt_image barista_whore_outfit_3_9
    samantha_whore_client_3 "Keep your eyes on me while you're blowing me, Samantha. That personal connection is very important."
    samantha.c "Okay, sorry. I know women like that. I forgot some guys do, too."
    wt_image barista_whore_outfit_3_10
    "He watches as she pleasures his cock, evaluating her technique. Then he pulls her head forward, pinning it in place with his cock as fully lodged in her throat as her gag reflex will let her take."
    samantha_whore_client_3 "You don't have much experience with this, do you?"
    "She shakes her head no, unable to answer orally with his cock in her mouth."
    samantha_whore_client_3 "That's okay. You have a natural willingness to please. You'll learn. You just need more training and more practice. Get up on the sofa for me, please. I'd like to try out your pussy."
    wt_image barista_whore_outfit_3_11
    samantha_whore_client_3 "Ahhh. That's good. You feel very nice."
    samantha.c "Thank you. I'm sorry I wasn't better at giving you a blow job. Pleasuring men is still new to me."
    samantha_whore_client_3 "Don't worry about it. Turn over please. I want you to do the work now."
    wt_image barista_whore_outfit_3_12
    samantha.c "Like this?"
    samantha_whore_client_3 "That's good. Now fuck my cock for me."
    samantha.c "It's a little awkward in this position."
    samantha_whore_client_3 "Put your hands right down on the floor."
    wt_image barista_whore_outfit_3_13
    samantha.c "Like this?"
    samantha_whore_client_3 "Yes. Try it now."
    "'Samantha' closes her eyes and rocks her hips back and forth on his hard member."
    wt_image barista_whore_outfit_3_14
    samantha.c "Ummm ... My arms are getting a little tired in this position."
    samantha_whore_client_3 "Three minutes, thirty seconds - not bad. You need a bit of strength conditioning, but you did okay. Get up here on top of me and show me how fast and hard you can ride my cock."
    wt_image barista_whore_outfit_3_15
    "'Samantha' does her best cowgirl imitation, riding him up and down as fast as her soon-tired legs will allow her."
    samantha.c "Sorry, this isn't a position I've ever used with a girlfriend. I don't think I can go any faster."
    samantha_whore_client_3 "That's fine, Samantha. Your top speed was as good as most straight girls. We just need to firm up your thighs, but your joints all work great. You can finish me off with your hand."
    wt_image barista_whore_outfit_3_16
    "'Samantha' pumps the jizz out of his balls and onto her waiting tits."
    samantha.c "Was that what you were hoping for? When you called looking for companionship?"
    samantha_whore_client_3 "You're every bit what I was looking for. Clean off my cock, please."
    wt_image barista_whore_outfit_3_17
    samantha.c "Did you want me to get a cloth?"
    samantha_whore_client_3 "No, your tongue is fine."
    samantha.c "Okay. Did you want to talk at all? I understand you've been traveling, and not had much time to develop a relationship. I have a bit of time left, if there's anything else you wanted us to do together?"
    samantha_whore_client_3 "I'll take a few measurements for my records, if you don't mind.  Then you can go.  Are you sure you're a double D?  I think you may be a cup size larger."
    wt_image barista_whore_outfit_1_12
    "After she leaves, Sam checks in with you."
    player.c "How did it go?"
    samantha.c "Not great."
    player.c "Were you able to help him?"
    samantha.c "I think so. He said he was happy with me, anyway."
    player.c "Was he mean to you?"
    samantha.c "No, not at all. He was a perfect gentleman. He was also knew a lot more about my body than most guys do, even if he was weirdly specific about how he evaluated parts of it."
    player.c "So what was the problem?"
    samantha.c "I don't know. It just left me feeling like - a piece of meat somehow. Like I was some product he was evaluating. He was nice enough, it was mostly the way he looked at me, and talked about my body. The other clients were the same, frankly. He was just more confident and open about his appraisal."
    samantha.c "I need to take a break from this while i figure out my thoughts. I think I can be good at it. I'm just not sure I want to be. I'm not getting any satisfaction from helping these men."
    player.c "Well, it is a job. You're getting paid."
    samantha.c "I know. And I'll send you your cut. I haven't forgotten. Just let me figure some stuff out, before you book any more clients for me. Maybe we can chat again at the coffee shop, once I've had a chance to think?"
    $ samantha.conversation_event = 14
    $ samantha.whore_status = 4
    $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  $ player.whore_income += 50
  change player energy by -energy_short notify
  return

label samantha_contact_pimp_keep_at_it:
    player.c "You can't solve all their problems in one session.  It'll get easier as you get more experience."
    samantha.c "Maybe. I hope so."
    player.c "Don't forget to send me my cut."
    samantha.c "I won't."
    return

label samantha_contact_pimp_maybe_isnt:
    player.c "Maybe this work isn't for you, Sam."
    samantha.c "I'm thinking probably it isn't. Maybe I should try and find another career?"
    player.c "Let's chat more at the coffee shop, after we both have a chance to think of something that may be a better fit for you."
    samantha.c "Okay"
    player.c "Don't forget to send me my cut for today's session, though."
    samantha.c "I won't."
    $ samantha.conversation_event = 7
    $ samantha.whore_status = 4
    $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
    call unconvert(samantha,'whore') from _call_unconvert_20
    return

# Contact - Make A Trade
label samantha_contact_make_trade:
    wt_image barista_slaver_1
    "You dial the contact information Sam's slaver gave you. It doesn't connect you directly, but after a number of automated transfers, he answers."
    samantha_whore_client_3 "Ready to have your friend back?"
    player.c "What kind of shape is she in?"
    samantha_whore_client_3 "Excellent shape, physically."
    player.c "And mentally?"
    samantha_whore_client_3 "There's not much left, I'm afraid. I won't lie to you, she's no conversationalist anymore. She also doesn't say 'no'."
    $ title = "What do you tell him?"
    menu:
        "I'm ready to trade":
            player.c "I'm ready to make a trade."
            samantha_whore_client_3 "I'll let my men know. I'm sending a number. Only use it once, when you've chosen the product you're going to deliver to me."
            samantha_whore_client_3 "You'll take the product to this mall, by car. Go to the underground parking, bottom level. You don't even need to get out of the car. Just stop when you're waved over, and ask the product to get out. They'll collect the delivery, and you can drive away."
            player.c "When will I get Sam back?"
            samantha_whore_client_3 "After we examine your product, make sure it's healthy and fully functional, and get it out of the country. Then I'll have your friend delivered back to you."
            if dee.dom_discussion_count > 2:
                sys "If you want to trade [dee.name], you'll need to wait until she's visiting you.  Choose not to proceed with trading anyone in the next menu if you want to wait and trade [dee.name] instead."
            call samantha_trade from _call_samantha_trade
            # if made valid trade, delete the contact option
            if samantha.temporary_count == 4:
                $ samantha.temporary_count = 0
                add tags 'trade_complete' to samantha
        "I'll get back to you":
            player.c "I'll get back to you."
            samantha_whore_client_3 "Sure, take your time. She's not going anywhere. Find someone nice to trade me."
        "I'm not interested":
            player.c "I'm not interested."
            samantha_whore_client_3 "No problem. There's no problem moving her on the secondary market. I just thought I'd check with you first, in case you wanted her for sentimental reasons."
            add tags 'no_trade' to samantha
    return

# Review Files
## Barista's Selfies
label samantha_review_files_selfies:
  wt_image barista_selfie_1
  "A selfie Sam sent you."
  if samantha.whore_photos_sent == 2:
    wt_image barista_selfie_2
    "First of a set of selfies Sam sent you."
    wt_image barista_selfie_3
    "Second of a set of selfies Sam sent you."
    wt_image barista_selfie_4
    "Third of a set of selfies Sam sent you."
  $ title = "Keep the album?"
  menu:
    "Yes, keep it":
      pass
    "No, delete it":
      rem tags 'selfies_available' from samantha
  return

## Barista's Wedding Photo
label samantha_review_files_wedding:
  wt_image barista_wedding_announcement
  "Sam's wedding announcement photo. Part of her reason for sending it to you was to humiliate her bride-to-be, so it wouldn't be polite not to take it out and stare at it once in a while."
  $ title = "Keep the photo?"
  menu:
    "Yes, keep it":
      pass
    "No, delete it":
      rem tags 'wedding_photos_available' from samantha
  return

## Character Specific Objects
# Decide What To Do About Sam
label samantha_decide_what_to_do:
  $ title = "What do you do about Sam?"
  menu:
    "Talk to Sam":
      if samantha.has_tag('slaver_working_on_a_plan'):
        wt_image barista_phone_1
        player.c "Sam. It's me again."
        samantha.c "Have you figured out a plan? What should I do? Should I go to the police?"
        call samantha_slaver_suggest from _call_samantha_slaver_suggest
      else:
        wt_image barista_phone_1
        player.c "Sam.  It's me."
        samantha.c "What's up?"
        $ title = "What do you tell her?"
        menu:
          "Warn her (figure out a way to save Sam)":
            wt_image barista_phone_1
            player.c "Sam, you're in trouble.  You remember your last client?   He called me.   He threatened you."
            samantha.c "What?  What should I do?  Should we go to the police?"
            call samantha_slaver_suggest from _call_samantha_slaver_suggest_1
          "Convince her to join you at the docks":
            player.c "Sam, I need your help."
            samantha.c "What's up?"
            player.c "I've gotten involved with some dangerous men, and I need your help to resolve it."
            samantha.c "My help?  How?"
            player.c "I need you to come with me to meet them.  If you can use your - charms - then they will leave me be, and it will solve a big financial problem for me."
            samantha.c "Oh. It sounds like you really are in trouble.  But ... I don't want to sound like a wuss, but if these men are dangerous, is it safe to leave me with them?"
            player.c "I'll be there too, Sam, to watch over you."
            samantha.c "This is a big ask, you know?"
            player.c "I know it is.  It's just you're the only one who can help me with this."
            samantha.c "Okay.  I'll do it.  As a friend, as thanks for all the help you've given me."
            player.c "Thanks Sam!  You're the best.  Wear something sexy.  We want them to be happy with you."
            samantha.c "Okay"
            "You make arrangements to meet her at the waterfront. You can't do anything more with your day. You're too nervous, worried about whether this deal may go wrong."
            call forced_movement(outdoors) from _call_forced_movement_45
            summon samantha
            wt_image barista_slaver_2
            "You get to the waterfront just before Sam. She arrives wearing a bikini. It's a warm night, and the women frequenting the numerous private yachts on the waterfront often dress in swim wear, so Sam blends right in."
            "As much as she can blend in, considering how good she looks in a bikini."
            samantha.c "Okay.  I'm here.  What do we do now?"
            player.c "We wait to be contacted."
            wt_image barista_slaver_3
            "It doesn't take long. A man you don't recognize comes up to you and waves you into a waterside building. When you enter, another man is cleaning one of an impressive collection of guns."
            player.c "Are these weapons necessary?"
            samantha_slaver "Sometimes. I hope they won't be today. I see you brought the girl. Step closer, please."
            wt_image barista_slaver_4
            samantha_slaver "Turn around. Let me have a good look at you."
            samantha.c "Whatever this is about, I'm sure I can resolve it to your satisfaction."
            wt_image barista_slaver_5
            samantha_slaver "Perhaps you can. Come closer. Let me examine the goods."
            samantha.c "Whatever you need."
            samantha_slaver "Whatever I need, huh? I like a woman who's acting of her own accord. I don't get that often enough. How about you suck on my cock, sunshine?"
            wt_image barista_slaver_6
            samantha.c "Of course!"
            "Sam smiles at you before she pops his cock in her mouth, happy that the plan to have her please them seems to be going well."
            wt_image barista_slaver_7
            samantha_slaver "That's really nice. Would you ride my cock for me, too?"
            samantha.c "If that's what you want."
            "Sam looks back at you as she climbs on top of him, as if to say 'look how much I'm willing to help you'."
            wt_image barista_slaver_8
            samantha_slaver "I have to say, you're really quite something, sunshine. How does it feel, knowing that you're spending your last few minutes of freedom riding my cock?"
            samantha.c "What? I don't think I understand?"
            "Sam looks over at you in confusion, uncertain as to what exactly she just heard."
            samantha_slaver "Don't worry about it, sunshine. I'm almost ready to cum. Turn around so I can look at this beautiful ass of yours as I do."
            wt_image barista_slaver_9
            "Sam turns around and starts to ride him faster, trying to bring him to climax. Facing away from him, she can't see him bring out a needle."
            samantha_slaver "Mmmhhhhhh"
            "He groans as he cums, then inserts the needle into the back of Sam's neck. Her eyes shut and she slumps backwards against him."
            samantha_slaver "Sweet dreams, sunshine. You were a special one. I'll always remember collecting you. I hope you enjoyed having the feeling of my cock inside you as your last real memory."
            player.c "I doubt it. She's a lesbian."
            wt_image barista_slaver_10
            samantha_slaver "No shit???  Well, she'll be what we want her to be, now."
            samantha_slaver "This won't take long. If you want to say good bye to her before she goes, you're welcome to stick around. Help yourself to a drink, and there's some food over there."
            "He gathers up the guns, and takes them and the unconscious Sam into the next room, closing the door behind him."
            $ title = "What do you want to do?"
            menu:
              "Stay and see what happens":
                "You've come this far. You may as well see it out. Besides. You haven't been paid yet."
                wt_image barista_slaver_11
                "A couple of hours later, Sam's former client appears, walking the former barista beside him on a leash."
                samantha_whore_client_3 "Ahh. You're still here. Good. You can witness the unit's final pre shipment tests, to confirm she's ready for transport."
                player.c "Unit?"
                samantha_whore_client_3 "That's what her new owner likes to call his specimens. I've no idea what number unit she'll be, so I'm just referring to her as 'unit', to ease her into the transition to her new life."
                player.c "What was she injected with?"
                samantha_whore_client_3 "A special serum. It doesn't so much transform her as erase her, leaving the body available for reprogramming. There's only so much of that I can do here in the field. The real programming takes place when she's received by my buyer."
                samantha_whore_client_3 "He only provides a small sample of the serum to me at once, enough to prepare one specimen at a time for shipment. And before you ask, no, I'm not going to put you in contact with him. I don't need more competition as a procurement agent."
                samantha_whore_client_3 "Now, is there anything you would like to see in the way of final tests before I ship her off?"
                $ samantha.temporary_count = 1
                while samantha.temporary_count == 1:
                  $ title = "What do you say?"
                  menu:
                    "Offer to get him more specimens" if not samantha.has_tag('slaver_offer_more_girls'):
                      player.c "I could get you more specimens your buyer may be interested in."
                      samantha_whore_client_3 "Thanks, but I don't like to fish in the same pool too often. Plus I want to limit contact with you, for everyone's safety."
                      samantha_whore_client_3 "I'll let you know if I'm looking for something new. Until then, don't try and reach me."
                      add tags 'slaver_offer_more_girls' to samantha
                    "Is she responsive?" if not samantha.has_tag('slaver_test_responsiveness'):
                      player.c "Is she responsive in this state?"
                      samantha_whore_client_3 "Only to direct commands and sexual stimulation. She's a little too responsive to sexual stimulation, right now. Come here, unit."
                      wt_image barista_slaver_14
                      "He pinches her nipple, and she moans as if she were instantly on the brink of orgasm."
                      samantha.c "OOOHHHHHH!!!!!"
                      samantha_whore_client_3 "See what I mean? Back on your knees, unit."
                      wt_image barista_slaver_15
                      samantha_whore_client_3 "Look at me and open your mouth."
                      "As she does so, he slips a ball gag inside and fastens it with a full head harness."
                      samantha_whore_client_3 "I haven't tried bringing her to orgasm yet, for fear of the whole waterfront showing up to investigate. It may be safe now, though, with her wearing a gag."
                      wt_image barista_slaver_16
                      samantha_whore_client_3 "Let's see if that keeps the moaning down to a dull roar."
                      "He attaches clamps to her nipples. Sure enough, the gag mutes the sounds escaping from her throat."
                      samantha.c "ooohhhhh!!!!!"
                      wt_image barista_slaver_17
                      samantha_whore_client_3 "Part of the problem are these body modifications the unit pre-installed on herself. They seem to make both her nipples and clit excessively sensitive."
                      samantha_whore_client_3 "The serum does that anyway. It overwrites almost all other nerve functions except the pleasure nerves, leaving the unit's brain - such as it is - highly attuned to sexual stimulation."
                      samantha_whore_client_3 "Combine the two and I'm guessing this unit will reach orgasm almost instantly with direct clitoral stimulation."
                      wt_image barista_slaver_18
                      "Sure enough, the former Sam starts cumming almost as soon as the vibrator touches her. She keeps cumming, in a seemingly endless wave, as he holds the vibrator against her."
                      "She makes no effort to pull back from the sensation, although it must be excruciating by the time the third or fourth orgasm rips through her. She just sits there, cumming and moaning as the drool rolls out from around her gag and coats the front of her body."
                      samantha.c "ooohhhhh!!!!!  ooohhhhh!!!!!  ooohhhhh!!!!!   ooohhhhh!!!!!  ooohhhhh!!!!!"
                      wt_image barista_slaver_19
                      samantha_whore_client_3 "That's enough of that. I think we've established that the unit is more than adequately responsive to sexual stimulation."
                      "He removes the nipples clamps, then unbuckles the straps holding the gag in place. You try and interpret the look she gives him as he removes the gag. Is it gratitude? disappointment that the orgasms have stopped? mindless devotion? You're not sure."
                      add tags 'slaver_test_responsiveness' to samantha
                    "Is she sexually available?" if not samantha.has_tag('slaver_test_sex'):
                      player.c "Is she prepared to have sex on command?"
                      wt_image barista_slaver_13
                      samantha_whore_client_3 "Stand up and kiss me, unit."
                      "The former Sam looks at him with adoration and leans in for a passionate, unrestrained kiss. You doubt her ex- ever received a more unconditional expression of sexual lust from her."
                      samantha_whore_client_3 "Unfortunately, that's as far as we're allowed to go with her. One of her buyer's conditions is that the post-serum specimen be treated as a virgin. No one is allowed to use any of the new unit's holes until he does."
                      player.c "How would he know? She looks ready to blow both of us right now. Or one of us could take her ass and the other her mouth."
                      samantha_whore_client_3 "He'd know. I don't know how, but I know he will."
                      add tags 'slaver_test_sex' to samantha
                    "Does she accept punishment?" if not samantha.has_tag('slaver_test_punishment'):
                      player.c "Does she accept punishment willingly?"
                      samantha_whore_client_3 "Unit, stand up and bend over. Present your ass for correction."
                      wt_image barista_slaver_12
                      samantha_whore_client_3 "Hold the leash in your mouth, unit."
                      "As the former Sam grips her leash between her teeth, he starts to beat her with a flogger. He's not gentle."
                      "*WWWHAAAAPPPP*  *WWWWHAAAAPPPPP*  *WWWHAAAAPPPPPP*"
                      "Despite the severity of the blows, she barely responds."
                      samantha_whore_client_3 "As you can see, her pain nerves aren't really working properly yet. The signals are being sent, but her brain hasn't figured out what they're supposed to mean."
                      samantha_whore_client_3 "I have no idea if she'll be left in this state, or re-wired to feel pain normally, or even re-wired to find even the slightest touch touch excruciating. I guess it depends on the specifications her new owner has provided for her."
                      wt_image barista_slaver_22
                      samantha_whore_client_3 "He might even re-wire her to cum from pain. Lie over my lap, unit."
                      "The creature that used to be Sam climbs on top of him, and he begins spanking her ... *smack*  *smack*  *smack*  *smack*  *smack*"
                      samantha_whore_client_3 "As far as I can tell, she's only responding to the feel of my lap under her, and not to the spanking itself, but it shouldn't take much to fix that, if her buyer's into that."
                      add tags 'slaver_test_punishment' to samantha
                    "Ask for your money" if not samantha.has_tag('slaver_ask_for_money'):
                      player.c "Where's my money?"
                      samantha_whore_client_3 "You'll get it as soon as she makes it to her end buyer without trouble and without anyone coming after us."
                      add tags 'slaver_ask_for_money' to samantha
                    "Just Leave" if samantha.has_tag('slaver_ask_for_money'):
                      "You've seen enough.  It's time to go home to bed and bring this day to an end."
                      $ samantha.temporary_count = 0
                $ samantha.dismiss(False)
                change player energy by -energy_long
              "Go home":
                player.c "When do I get my money?"
                samantha_slaver "As soon as she's safely out of the country, without anyone following us."
                "You leave Sam to her new owners. You're not needed for whatever more they have planned for her. Better just to go home and go to bed. It's been a long day."
                $ samantha.dismiss(False)
                change player energy by -energy_short
            $ samantha.slaver_payment_week = week + 2
            $ samantha.slaver_events = 7
            end_day
    "Talk to Janice the Lawyer first" if player.has_tag('lawyer_on_retainer') and not samantha.has_tag('talked_to_janice'):
      wt_image lawyer_desk_1
      $ title = "What do you ask her about?"
      menu menu_samantha_decide_janice:
        "Protecting you" if not janice.has_tag('discussed_barista_protect_you'):
          player.c "Janice, hypothetically, if I come into some money ... a gift if you would for a favor rendered ... and the people who provided the gift are potentially involved with a less than legal operation ... you'd be able to keep me out of trouble, right?"
          janice.c "Is there going to be anything directly connecting you to an illegal act?"
          player.c "Nothing direct, no."
          janice.c "Then yes, I should be able to protect you from any indirect connections."
          add tags 'discussed_barista_protect_you' to janice
        "Protecting Sam" if not janice.has_tag('discussed_barista_protect_her'):
          player.c "Janice, I have a situation."
          "You describe the threat to Sam."
          player.c "Should I take this to the police?"
          janice.c "If you do, it only takes one dirty cop to tip them off, or one stupid cop to slip up, and either Sam or you - or both of you - could end up dead or on a slave boat out of the country."
          if player.marilyn_building_visit_count > 0:
            janice.c "If you want to protect her, I suggest you speak to Marilyn."
            player.c "Are you sure her organization isn't behind this?"
            janice.c "No, I'm not.  But if she is behind it, and you do go to the cops, it won't end well for you."
            # if samantha.slaver_plan == 0:
            #   jump samantha_decide_what_to_do
          else:
            player.c "So it might be safer if she fled?"
            janice.c "I don't know.  Sorry, I can't help."
          add tags 'discussed_barista_protect_her' to janice
        "Nothing else right now":
          jump samantha_decide_what_to_do
      if janice.has_tag('discussed_barista_protect_you') and janice.has_tag('discussed_barista_protect_her'):
        "There's nothing more for you to discuss with Janice about this."
        add tags 'talked_to_janice' to samantha
        jump samantha_decide_what_to_do
      else:
        $ title = "What do you ask her about?"
        jump menu_samantha_decide_janice
    "Talk to Marilyn first" if player.marilyn_building_visit_count > 0 and not samantha.has_tag('talked_to_marilyn'):
      wt_image marilyn_office_22
      if not marilyn.has_tag('discussed_barista_slaver'):
        player.c "Marilyn, are you involved in human trafficking?"
        marilyn.c "What a stupid question. You call me, where I can't see who might be there with you or whether you're taping this, to ask me if I'm involved in something illegal? If I'm not, I'm going to say no. If I am, I'm still going to say no."
        marilyn.c "Call me when you have someone interesting for me.  Until then, stop wasting my time."
        $ title = "What do you do?"
        menu:
          "Rephrase the question":
            player.c "You're right. That was I a stupid question I asked. Let me re-phrase it."
            call samantha_marilyn_solution from _call_samantha_marilyn_solution
          "Stop wasting her time":
            "That was a pretty evasive answer, followed by a clear threat. You hang up before she gets really annoyed."
        add tags 'discussed_barista_slaver' to marilyn
      else:
        player.c "You're right, Marilyn. That was a stupid question I asked earlier. Let me re-phrase it."
        call samantha_marilyn_solution from _call_samantha_marilyn_solution_1
      jump samantha_decide_what_to_do
    "Ignore the whole mess":
      "Whatever this guy has planned for Sam, perhaps it would be best if you don't get involved."
      "On the other hand, if you don't at least warn her, he may not stop pursuing her just because you don't deliver her to him."
      $ title = "Ignore the offer for Sam?"
      menu:
        "Yes, ignore it":
          "You decide to take a hands off approach. It's not like you're responsible for either of them."
          $ samantha.slaver_events = 3
          $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
        "No, do something":
          jump samantha_decide_what_to_do
  return

label samantha_marilyn_solution:
    player.c "I've been approached by a man about a woman under my influence. He wants to buy her. Not for himself. He plans to take her out of the country and resell her. He has a client already lined up who wants her."
    player.c "If you don't have a problem with him conducting this business here, then I don't either. If you do have a problem with it, then let me know, because maybe together we can stop him."
    marilyn.c "This woman, is she a willing slave?"
    player.c "Definitely not."
    marilyn.c "Then he's not working for me. And yes, I have a problem with him operating in my town. Where are you supposed to meet him?"
    player.c "On the waterfront, tonight."
    marilyn.c "How many men are involved?"
    player.c "I don't know. Only one contacted me, but he said a man working with him would contact me when I bring her to the waterfront."
    marilyn.c "Is she willing to go along?"
    player.c "I don't know. Guarantee me she won't get hurt?"
    marilyn.c "I can't guarantee anything. This will be resolved with bullets, not negotiations. Somebody's likely to die. It could be her. It could be you."
    marilyn.c "If she's willing to take the risk, let me know and my men will be there. Discretely, and at a distance. You and she will have to play along until we're able to scout out the situation and determine the best way to neutralize them and extract you."
    marilyn.c "If she isn't willing to take that risk, tell her to get lost. Well lost, and fast. If he has a buyer lined up for her, he's going to keep looking for her. He's not going to want to miss out on a potential sale."
    player.c "Can I get a reward?"
    marilyn.c "For me helping your friend?"
    player.c "For me alerting you to someone operating on your turf, and helping you get rid of them."
    marilyn.c "Sounds like an even trade to me."
    player.c "Except that my friend and I are the ones at risk of getting killed, not you."
    marilyn.c "My men will be at risk too. That's what happens to pawns."
    "Marilyn hangs up. You now have a plan, if you want to take the chance and use it."
    $ samantha.slaver_plan = 1
    add tags 'talked_to_marilyn' to samantha
    return

label samantha_slaver_suggest:
  $ title = "What do you suggest?"
  menu:
    "Go to the police":
      player.c "Yes, go to the police. They should be able to keep you safe. I'll give them a statement telling them everything I know."
      samantha.c "Okay. Thanks for looking out for me!"
      $ samantha.slaver_events = 4
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
    "Get out of town":
      player.c "I'm not sure the police will be able to protect you, Sam. Get out of town. Disappear. Don't let anyone know where you're going - not even me. I'll let the coffee shop know you've quit to take a better job. You need to go. Now."
      samantha.c "Oh! Okay. If you think that's best. Thank you for taking care of me!"
      "You never find out if she got away. Perhaps you should have told her to check in with you when she got some place safe. But then, if you didn't hear from her, you'd know she wasn't free. This way, you can at least hope that she escaped."
      $ samantha.slaver_events = 5
      $ samantha.conversation_event = 16
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      #call convert(samantha, "unavailable")
      $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
    "Let me figure out a plan" if samantha.slaver_plan == 0:
      player.c "Give me a few minutes to think.  Perhaps I can figure out a plan."
      add tags 'slaver_working_on_a_plan' to samantha
      jump samantha_decide_what_to_do
    "I have a plan" if samantha.slaver_plan == 1:
      call samantha_slaver_i_have_plan from _call_samantha_slaver_i_have_plan
  return

label samantha_slaver_i_have_plan:
  player.c "I have a plan, but it's risky. We play along. I deliver you to them. You pretend like you don't know what's happening. In the meantime, friends of mine will get into position to neutralize these men and get us out of there."
  samantha.c "Neutralize?  You mean kill them?"
  player.c "Yes."
  samantha.c "Shouldn't we just go to the police? If people start shooting, it sounds like I could get killed."
  player.c "Yes, I think you could. So could I. I'm not sure you'd be any safer, however, with the police."
  samantha.c "I'm scared. I don't know what to do. I feel like I should go to the police, but I don't know. What do you think I should do?"
  $ title = "What do you tell her?"
  menu:
    "Go to the police":
      player.c "Yes, go to the police. They should be able to keep you safe. I'll give them a statement telling them everything I know."
      samantha.c "Okay.  Thanks for looking out for me!"
      $ samantha.slaver_events = 4
    "Get out of town":
      player.c "I'm not sure the police will be able to protect you, Sam. Get out of town. Disappear. Don't let anyone know where you're going - not even me. I'll let the coffee shop know you've quit to take a better job. You need to go. Now."
      samantha.c "Oh! Okay. If you think that's best. Thank you for taking care of me!"
      "You never find out if she got away. Perhaps you should have told her to check in with you when she got some place safe. But then, if you didn't hear from her, you'd know she wasn't free. This way, you can at least hope that she escaped."
      $ samantha.slaver_events = 5
      $ samantha.conversation_event = 16
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      #call convert(samantha, "unavailable")
      $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
    "Proceed with the plan":
      call samantha_slaver_proceed_with_plan from _call_samantha_slaver_proceed_with_plan
  return

label samantha_slaver_proceed_with_plan:
  player.c "As dangerous as it is, I think my plan is your best chance. If we don't stop them, they're going to keep coming after you. I don't think the police can protect you. You could run, but I don't know if you can shake them. This is the only way we can be sure that you're safe."
  samantha.c "Okay. If you think this is best, I'll trust you. What do I do?"
  player.c "Meet me at the waterfront this evening. Wear something sexy to distract them and play along with my lead. I need to act like I'm bringing you to them, and you need to act like you're just there as a favor to me, with no idea about what's going on."
  "You can't do anything more with your day. You're too nervous, worried about whether this plan may go wrong."
  call forced_movement(outdoors) from _call_forced_movement_46
  summon samantha
  wt_image barista_slaver_2
  "You get to the waterfront just before Sam. She arrives wearing a bikini. It's a warm night, and the women frequenting the numerous private yachts on the waterfront often dress in swim wear, so Sam blends right in. As much as she can blend in, considering how good she looks in a bikini."
  samantha.c "Okay. I'm here. What do we do now?"
  player.c "We wait to be contacted."
  wt_image barista_slaver_3
  "It doesn't take long. A man you don't recognize comes up to you and waves you into a waterside building. When you enter, another man is cleaning one of an impressive collection of guns."
  player.c "Are these weapons necessary?"
  samantha_slaver "Sometimes. I hope they won't be today. I see you brought the girl. Step closer, please."
  wt_image barista_slaver_4
  samantha_slaver "Turn around. Let me have a good look at you."
  samantha.c "Whatever this is about, I'm sure I can resolve it to your satisfaction."
  "Sam looks nervous, but the man doesn't seem to find that suspicious."
  wt_image barista_slaver_5
  samantha_slaver "Perhaps you can. Come closer. Let me examine the goods."
  samantha.c "Whatever you need."
  samantha_slaver "Whatever I need, huh? I like a woman who's acting of her own accord. I don't get that often enough. How about you suck on my cock?"
  wt_image barista_slaver_6
  "Sam looks at you and you nod your approval. She lowers her head and pops his cock in her mouth."
  wt_image barista_slaver_7
  samantha_slaver "That's really nice. Would you ride my cock for me, too?"
  samantha.c "If that's what you want."
  "Sam looks back at you as she climbs on top of him, likely wondering how far this is going to go before the cavalry arrives."
  wt_image barista_slaver_9
  samantha_slaver "I have to say, you're really quite something. How does it feel, knowing that you're spending your last few minutes of freedom riding my cock?"
  "Sam looks over at you in fear, a thousand thoughts racing through her mind. Is help going to arrive? Will it be too late? Did you betray her? He sees her fear, but it doesn't make him suspicious. If anything, it seems to turn him on."
  samantha_slaver "Don't worry about it. Your new owner will take good care of you. I'm almost ready to cum. Turn around so I can look at this beautiful ass of yours as I do."
  wt_image gun_shot_2
  "As Sam turns around, bullets ring out."
  $ samantha.random_number = renpy.random.randint(1, 10)
  if samantha.random_number > 7:
    wt_image barista_slaver_21
    "The slaver is dead. So is Sam, hit by a stray bullet. Her eyes stare at you half open but vacant, as the blood runs out of the hole in her back."
    wt_image marilyn_security_3
    "Marilyn's bodyguard is here, and seems to be in charge."
    guard_marilyn "I'm sorry about your friend, but please step back. We need to make it look like you weren't here. Like none of us were here."
    player.c "Should we take her to the hospital?"
    guard_marilyn "It won't help. You need to leave her with us now."
    add tags 'dead' to samantha
    $ samantha.conversation_event = 16
  else:
    wt_image barista_slaver_20
    "The slaver's dead. Sam's unharmed, but shaken. In the confusion, she grabbed one of the guns the slaver had been cleaning."
    player.c "Sam, do you know how to use that?"
    samantha.c "No"
    player.c "Put it down before you hurt yourself or someone else."
    wt_image marilyn_security_3
    "Her hand shaking, she gently lays the gun down. Marilyn's bodyguard is here, and seems to be in charge."
    guard_marilyn "Please step back.  We need to make it look like you weren't here.  Like none of us were here."
  player.c "There's another man."
  guard_marilyn "Two actually. We got them, too. Go."
  player.c "Who were they?"
  guard_marilyn "Hard to say. They're all carrying multiple IDs, multiple passports."
  player.c "Who were they working for?"
  guard_marilyn "Themselves, I'd guess. Their phones are locked, but one of them had a handful of business cards from around the world in his wallet. Potential buyers most likely."
  player.c "Anyone I'd recognize?"
  guard_marilyn "None I recognize. Foreign names mostly. One corporation, Bodywerks I think it was called. Nothing I've ever heard of."
  player.c "Did they have my money on them?"
  guard_marilyn "No money. Just pocket change. You have to go now. The police can only give us so much time to clean up before they have to respond to the reports of gunfire."
  if samantha.has_tag('dead'):
    $ samantha.dismiss(False)
    wt_image bedroom.image
    "You go home and crawl into bed, hoping that sleep will erase the look on Sam's face from your memory. You can't even tell anyone what occurred. You're pretty sure Marilyn expects you to stay silent."
    $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
  else:
    call character_location_return(samantha) from _call_character_location_return_641
    wt_image barista_phone_1
    "You go home.  Before you can get into bed, Sam calls you."
    samantha.c "Thanks for getting me out of that trouble."
    player.c "Are you okay?"
    samantha.c "I think so, yeah.  Just a little shook up.  It all seems like a dream somehow.  I can't wait to get back to the coffee shop tomorrow, and have life back to normal again.  Isn't that weird?"
    player.c "Not really.  I'll chat with you at the coffee shop."
    samantha.c "I'd like that.  I still need you to help me find a new career."
    player.c "I'd like that too.  Sam, you know we have to stay silent about this."
    samantha.c "I guessed as much.  Whoever your friends were, I assume it's best not to tell anybody about what happened?"
    player.c "I think that's best, yes."
    $ samantha.conversation_event = 7
  $ samantha.slaver_events = 6
  change player energy by -energy_long notify
  end_day
  return

# Select Who You're Trading For Sam
label samantha_trade:
    $ samantha.temporary_count = 0
    $ current_target = None
    call choose_person_with_tags(['girlfriend', 'bimbo', 'slavegirl', 'adult_baby', 'hypno_girlfriend']) from _call_choose_person_with_tags_9
    if current_target == None:
        $ samantha.temporary_count = 2
        $ current_target = player.location
    else:
        $ title = "Trade [current_target.full_name] to the slaver?"
        menu:
            "Yes":
                if renpy.has_label(current_target.short_name + "_slaver_trade_custom"):
                    call expression current_target.short_name + "_slaver_trade_custom" from _call_expression_39
                    # note: the customized labels should return:
                        # temporary_count = 3 if to be handled completely normally, such as when only one state is to be handled in a special manner (i.e. girlfriend customized but bimb standard so comes back as 3)
                        # temporary_count = 2 if intro was customized but now choose again
                        # temporary_count = 1 if intro was cutomized but now standard effects of trade apply
                        # temporary count = 0 if entire content is handled in customized label and trade not completed
                        # temporary count = 4 if entire content is handled in customized label and trade was completed
                else:
                    # default content if not handled via character specific label
                    $ samantha.temporary_count = 3
            "No":
                $ title = "What now?"
                menu:
                    "Choose again":
                        jump samantha_trade
                    "Wait and think this through":
                        pass
    # standardized introduction, i.e. if selection content not handled throuh customized label
    if samantha.temporary_count == 3:
        # note: converted to a label so it can be called from customized labels when you nly want to change how the outcome plays out, rather than the intro; Jasmine is an example of this
        call samantha_standard_slaver_trade_introduction from _call_samantha_standard_slaver_trade_introduction_2
        # note: will return temporary_count = 1 if proceed or 2 if choose again
    # outcomes
    # made a valid selection and proceeded with default art
    if samantha.temporary_count == 1:
        wt_image slaver_trade_1
        "You spot him as you pull into the garage."
        wt_image slaver_trade_2
        player.c "This space is narrow.  Get out here while I park."
        "As she does so, she doesn't see him approaching from behind."
        wt_image slaver_trade_3
        "Her scream dies in her throat as he shows her the knife. She stares helplessly at you, waiting for you to come to her aid, until he pulls the sack over her head and everything goes dark."
        samantha_slaver "Keep your mouth shut. Nobody wants you hurt. Come with me and everything will be fine. You'll forget about all of this, even your boyfriend, soon enough."
        "She slumps to her knees as he injects her with something. He looks at you for just a moment."
        samantha_slaver "Get out of here. If she's healthy and functional you'll get your payment soon enough. Now get lost."
        "Then he turns his attention back to the disoriented hooded woman at his feet."
        samantha_slaver "Come on, unit. Follow my voice. Time to start your training."
        wt_image living_room.image
        "You head home. You've completed your side of the trade. Now you just need to wait for Sam to be returned to you."
        call convert(current_target, 'unavailable') from _call_convert_184
        $ current_target = samantha
        $ samantha.slaver_events = 10
        $ samantha.doll_return_week = week + 1
        change player energy by -energy_short notify
        $ samantha.temporary_count = 4
        # note: temporary_count set to 4 so that option to make a trade is disabled on return to the action label
    # made an invalid selection
    elif samantha.temporary_count == 2:
        $ title = "What now?"
        menu:
            "Choose again":
                jump samantha_trade
            "Wait and think this through":
                $ samantha.temporary_count = 0
    # passed on making a selection or outcome was handled through customized label
    else:
        pass
    # note: now returns to slaver trade action where if trade completed, i.e. temporary_count == 4, the action is removed
    return

label samantha_standard_slaver_trade_introduction:
    if current_target.has_tag('degraded'):
        "She's no longer in a state that they would take her as a trade."
        $ samantha.temporary_count = 2
    elif current_target.has_tag('doll') and current_target.has_tag('transformed'):
        "She's no longer in a state that they would take her as a trade."
        $ samantha.temporary_count = 2
    elif current_target.has_tag('petgirl') and current_target.has_tag('transformed'):
        "She's no longer in a state that they would take her as a trade."
        $ samantha.temporary_count = 2
    elif current_target.has_tag('bimbo'):
        wt_image current_target.image
        player.c "[current_target.name], let's go to the mall."
        current_target.c "Yay!!"
        $ samantha.temporary_count = 1
    elif current_target.has_tag('adult_baby'):
        wt_image current_target.image
        player.c "Come on baby girl, Daddy's going to take you shopping."
        current_target.c "Ga ga!"
        player.c "Put on your big girls clothes and meet me at the car."
        current_target.c "'Kay. Will Daddy buy me a treat at the store?"
        player.c "You are the treat, baby girl."
        current_target.c "Ahhh!  Daddy is so good to me!!"
        $ samantha.temporary_count = 1
    elif current_target.has_tag('slavegirl'):
        wt_image current_target.image
        player.c "[current_target.name], put on some clothes. We're going for a drive."
        current_target.c "Sir?"
        player.c "You heard me. Meet me at the car."
        $ samantha.temporary_count = 1
    elif current_target.has_tag('girlfriend') or current_target.has_tag('hypno_girlfriend'):
        wt_image current_target.image
        player.c "[current_target.name], let's go to the mall."
        current_target.c "Do you have some shopping to do?"
        player.c "There's something I need to trade in."
        $ samantha.temporary_count = 1
    else:
        "Not sure how you got here, but she's not ready to accompany you to a dark parking garage."
        $ samantha.temporary_count = 2
    return

## Items
# Give Butt Plug
label give_bp_samantha:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_samantha:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_samantha:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_samantha:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_samantha:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_samantha:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_samantha:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_samantha:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_samantha:
  "Best to save this for a paying client."
  return

# Give Ring of Secuality
label give_rs_samantha:
    "If the ring makes heterosexual women appreciate other women, in theory it should make a homosexual woman appreciate men.  In practice, she won't accept a ring from you, so you'll never know."
    return

# Use Water Bowl
label use_wb_samantha:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_samantha:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label samantha_start_day_early_events:
  ## Monday and Barista Doll Return
  if day == 1 and week > samantha.doll_return_week and samantha.doll_return_week > 0 and samantha.slaver_events == 10:
    call samantha_doll_return from _call_samantha_doll_return
  return

label samantha_start_day:
  ## Reset Session Actions - Barista Escort Training
  if samantha.whore_status == 2 and samantha.whore_train_day == day and samantha.whore_train_week < week:
    if samantha.whore_test_level < 2:
      call samantha_message_photo from _call_samantha_message_photo
    elif samantha.whore_test_level == 2:
      call samantha_whore_test_2 from _call_samantha_whore_test_2
  ## Friday and Barista Avalon Thank You
  elif day == 5 and samantha.avalon_sales_status == 3:
    call samantha_avalon_thank_you from _call_samantha_avalon_thank_you
  ## Barista Visit To Club Pres
  elif gloria.discussed_barista == 3:
    call samantha_visit_gloria from _call_samantha_visit_gloria
  return

label samantha_start_day_late_events:
  if samantha.slaver_events == 1 and day == 1:
    call samantha_slaver_event from _call_samantha_slaver_event
    call samantha_decide_what_to_do from _call_samantha_decide_what_to_do
  return

# End Day
label samantha_end_day:
  ## trigger Sam missing shift if unavailable for whatever reason
  if samantha.status == 'unavailable' and samantha.new_barista_switch == 0:
    $ samantha.conversation_event = 16 #triggers manager serving you coffee next time
  ## change images in coffee shop from manager once have had him serve you once post Sam missing
  if samantha.conversation_event == 17:
    $ samantha.conversation_event = 18
  ## New Barista?
  if samantha.new_barista_switch == 1:
    $ samantha.new_barista_switch = 2
  rem tags 'in_club_now' from samantha
  rem tags 'coffee_already_today' from player
  call character_location_return(samantha) from _call_character_location_return_642
  return

label samantha_whore_test_2:
  $ samantha.whore_test_level == 3
  rem tags 'no_hypnosis' from samantha # so subsequent tests function propery
  wt_image front_door
  "Bright and early in the morning, there's a knock on your door."
  summon samantha
  wt_image barista_test_3_1
  "Sam brushes her way in as you open the door."
  samantha.c "Sorry to wake you so early, but I have the early shift at the coffee shop, and wanted to get this over with before I went in."
  player.c "Get what over with?"
  samantha.c "Letting you examine my body. To decide if sexual concierge work is something I'm cut out for or not. I told my co-worker I was coming over here to see you. So no monkey business."
  if player.can_hypno(samantha):
    $ title = "Hypnotize her?"
    menu:
      "Yes, hypnotize her":
        $ samantha.hypno_session() # deducts energy and records she was hypno'd
        player.c "Let's talk first."
        call focus_image from _call_focus_image_18
        player.c "Actually, I'll do the talking. You listen. Listen to me Sam. Listen to me. Only me. Only my words Sam. Only my words now."
        wt_image barista_test_3_14
        "It doesn't take long for her to fall under your trance."
        player.c "Remove your clothes now, Sam, so that I can inspect your body while we talk."
        wt_image barista_test_3_15
        player.c "That's better. I finally get to see what you look like. Why are you pierced? Are you a submissive? Did a Domme choose those piercings for you?"
        samantha.c "No! A girlfriend recommended it. She was pierced and said it made her more sensitive. I pierced my nipples first, and liked it so much I pierced my clit hood too. Vibrators feel especially good now."
        player.c "Would you like me to use a vibrator on you?"
        samantha.c "No, thank you. I only like to play with girls."
        wt_image barista_test_3_16
        player.c "Open your pussy so I can see it better. Do you have a lot of experience fucking men?"
        samantha.c "No, not really."
        player.c "You need to be good at pleasing men to be a sexual concierge, Sam."
        samantha.c "Yes, I know. I don't think it's as hard to pick up as learning to please women."
        $ title = "What do you do?"
        menu menu_samantha_whore_test_hypno:
          "Have her blow you":
            player.c "Let's have you practice giving a blow job, Sam. Come over here and take out my cock."
            wt_image barista_test_3_20
            player.c "Have you given many blow jobs?"
            samantha.c "Only a few."
            player.c "You have great tits. Spit on my cock and rub it between your tits."
            wt_image barista_test_3_21
            player.c "Men will enjoy this. Remember that."
            samantha.c "Okay"
            player.c "Lick my cock now. The whole length, like it was a popsicle."
            wt_image barista_test_3_22
            player.c "The underside of the cock head is particularly sensitive. Spend lots of time in that area with your tongue."
            samantha.c "Okay"
            player.c "Start sucking now. Gentle pressure. Make a soft seal with your lips as you bob your head up and down on the shaft."
            wt_image barista_test_3_23
            player.c "Keep working your tongue, too. I should be licking the underside of my cock the whole time you're sucking me."
            "You think she responds 'Okay', but its hard to tell for sure with your cock muffling her mouth."
            player.c "Try to get the whole thing into your mouth on the down strokes."
            wt_image barista_test_3_24
            player.c "It takes practice. Try working on bananas at home, to learn how to control the gag reflex. The objective is to get the man's full shaft inside you, so that your tongue and lips are right down to his balls."
            "With this much of your cock in her mouth, there's no way to know what meaning the gurgling sounds she emits were intended to convey."
            player.c "At this point, men will have different preferences. Some will want to hold your head still and fuck your mouth until they orgasm. Others will want you to pump their shaft with their hand while you suck them. Some will want to fill your mouth with their sperm. Others will want to watch their sperm spurt all over your pretty face."
            $ title = "What do you want?"
            menu:
              "Cum in her mouth":
                player.c "Hold your head still while I face fuck you for a few minutes, Sam."
                wt_image barista_test_3_25
                player.c "That's good. Keep yourself just like that. I'm going to fill your mouth with cum in a moment. A lot of its going to spurt against the back of your throat. Try not to swallow it. Keep as much of it in your mouth as you can."
                player.c "Here it comes ... [player.orgasm_text]"
                player.c "Tilt your head back and show me how you did."
                wt_image barista_test_3_13
                player.c "Good. You caught a lot of it. Swallow it now, and get yourself dressed."
                $ samantha.hypno_swallow_count += 1
                $ samantha.hypno_blowjob_count += 1
                orgasm
                call samantha_whore_test_2_dress from _call_samantha_whore_test_2_dress
              "Cum on her face":
                wt_image barista_test_3_26
                player.c "Take my cock out of your mouth now Sam, and hold it in front of you. Pump it with your fist.  Keep your grip soft, just a gentle sensation, but pump fast.  That's it.  That's it."
                player.c "[player.orgasm_text]"
                player.c "Next time, open your mouth and stick out your tongue, and see if you can catch some of the sperm on it."
                wt_image barista_test_3_27
                player.c "Okay, it's too late for today, but yes, like that.  Go to the bathroom and clean my cum off your face and hair, Sam, then get yourself dressed."
                $ samantha.hypno_facial_count += 1
                $ samantha.hypno_blowjob_count += 1
                orgasm
                call samantha_whore_test_2_dress from _call_samantha_whore_test_2_dress_1
              "Fuck her first":
                call samantha_whore_test_hypno_fuck from _call_samantha_whore_test_hypno_fuck
          "Have her fuck you":
            call samantha_whore_test_hypno_fuck from _call_samantha_whore_test_hypno_fuck_1
            # "Why pass up the opportunity to fuck genuine lesbian pussy?"
            # player.c "Let's have you practice fucking a cock, Sam. Turn over."
            # wt_image barista_test_3_28
            # "As she turns her ass towards you, you gently slide the tip of your cock inside her."
            # wt_image barista_test_3_29
            # player.c "Start fucking me, Sam. You're the professional, so you're going to need to take charge of these poor men and help them overcome their sexual difficulties. That means you're going to have to do most of the work."
            # player.c "That's it, move your hips forward and back. Rock them them too, up and down. Change the angle of pressure on my cock for every stroke."
            # wt_image barista_test_3_30
            # player.c "Climb up on top of me now. Let's see you ride me. That's it, Sam. Use your legs to lift yourself up and down."
            # wt_image barista_test_3_31
            # player.c "Turn around so I can see you better, Sam."
            # wt_image barista_test_3_32
            # player.c "Fuck me to climax, Sam. Faster. Faster. That's it. Faster!"
            # wt_image barista_test_3_33
            # "At the last minute, it occurs to you that as a lesbian, she may not be on birth control yet. You pull her off of your cock just as your ejaculation starts."
            # player.c "[player.orgasm_text]"
            # "You admire the sight of your jizz dripping down her pretty pussy until the pace of your breathing returns to normal."
            # player.c "Clean yourself up in the bathroom, Sam. Then get dressed."
            # player.c "And remember to get yourself started on birth control, if you aren't already."
            # samantha.c "Okay"
            # $ samantha.hypno_sex_count += 1
            # orgasm
            # call samantha_whore_test_2_dress
          "Have her practice on a dildo" if not samantha.has_tag('whore_test_hypno_dildo'):
            player.c "Do you have a dildo with you, Sam?"
            samantha.c "I have a vibrator. In my purse."
            player.c "You said you're on your way to work. Do you always bring that with you to work?"
            samantha.c "Yes. I use it at the coffee shop sometimes. In the washroom, when I'm having a bad day, to perk me up."
            player.c "Get it. Show me how you use it on yourself.  Then show me how you would fuck a man, pretending the vibrator is his cock."
            wt_image barista_test_3_17
            "Sam keeps her pussy open for your inspection as she uses the vibrator on herself. She starts with her nipples, which are soon standing at attention as the vibrator makes a quiet, super fast tapping sound against her piercings."
            wt_image barista_test_3_18
            "Then she switches to her clit. The vibrator against her hood piercing takes her over the edge quickly.  She stays remarkably silent as she cums, only deep soft sighs escaping her throat as her body twitches. It must be the practice from jilling herself in the coffee shop washroom."
            wt_image barista_test_3_19
            "When she finishes cumming, she starts using the vibrator as if it was a cock.  She can't really practice with it, as its not attached to a body, but she does her best."
            $ samantha.hypno_masturbation_count += 1
            $ samantha.hypno_orgasm_count += 1
            add tags 'whore_test_hypno_dildo' to samantha
            $ title = "What do you do?"
            jump menu_samantha_whore_test_hypno
          "You're finished, have her get dressed":
            call samantha_whore_test_2_dress from _call_samantha_whore_test_2_dress_2
      "No, don't":
        call samantha_whore_test_2_dont_hypno from _call_samantha_whore_test_2_dont_hypno
  else:
    call samantha_whore_test_2_dont_hypno from _call_samantha_whore_test_2_dont_hypno_1
  add tags 'no_hypnosis' to samantha
  call character_location_return(samantha) from _call_character_location_return_643
  return

label samantha_whore_test_hypno_fuck:
    "Why pass up the opportunity to fuck genuine lesbian pussy?"
    player.c "Let's have you practice fucking a cock, Sam. Turn over."
    wt_image barista_test_3_28
    "As she turns her ass towards you, you gently slide the tip of your cock inside her."
    wt_image barista_test_3_29
    player.c "Start fucking me, Sam. You're the professional, so you're going to need to take charge of these poor men and help them overcome their sexual difficulties. That means you're going to have to do most of the work."
    wt_image barista_test_3_34
    player.c "That's it, move your hips forward and back. Rock them them too, up and down. Change the angle of pressure on my cock for every stroke."
    wt_image barista_test_3_30
    player.c "Climb up on top of me now. Let's see you ride me. That's it, Sam. Use your legs to lift yourself up and down."
    wt_image barista_test_3_31
    player.c "Turn around so I can see you better, Sam."
    wt_image barista_test_3_32
    player.c "Fuck me to climax, Sam. Faster. Faster. That's it. Faster!"
    wt_image barista_test_3_33
    "At the last minute, it occurs to you that as a lesbian, she may not be on birth control yet. You pull her off of your cock just as your ejaculation starts."
    player.c "[player.orgasm_text]"
    "You admire the sight of your jizz dripping down her pretty pussy until the pace of your breathing returns to normal."
    player.c "Clean yourself up in the bathroom, Sam. Then get dressed."
    player.c "And remember to get yourself started on birth control, if you aren't already."
    samantha.c "Okay"
    $ samantha.hypno_sex_count += 1
    orgasm
    call samantha_whore_test_2_dress from _call_samantha_whore_test_2_dress_3
    return

label samantha_whore_test_2_dress:
  wt_image barista_test_3_1
  "You have Sam dress, instruct her to forget what happened, and bring her out of the trance. All she'll remember is that she had an enjoyable chat with you."
  player.c "I don't need to see anything more, Sam."
  samantha.c "Really?  I was ready to take my clothes off for you.  That's why I came over."
  player.c "That won't be necessary."
  $ title = "What do you tell her?"
  menu:
    "I'm certain you can do this work":
      player.c "I'm now confident that you can do this work, Sam. I can look after the marketing and logistics for you for a small cut."
      samantha.c "Could you?  That would be great."
      player.c "What do you want to call yourself?  Professionally?"
      samantha.c "What do you mean?"
      player.c "It's typical in this line of business to use a professional name.  Something different than your real name.  Something that inspires confidence in the client."
      samantha.c "How about 'Samantha'?"
      "You do your best to stifle a reaction."
      player.c "Uhh, okay. Sure. I'll let you know when I have your first client lined up.  It may take a day or so."
      samantha.c "Okay.  Great.  Let's give it a try.  I need to go now.   My shift at the coffee shop starts soon."
      $ samantha.whore_status = 3
      $ samantha.conversation_event = 13
      call convert(samantha, "whore") from _call_convert_13
    "Maybe you're not cut out for this after all":
      player.c "I'm not sure you're really cut out for this work after all, Sam."
      samantha.c "I was worried about that. I'm probably just too much of a lesbian to appeal to most guys."
      player.c "Perhaps we should try and find a different career for you. We can chat more, at the coffee shop, after we've both had a chance to think some more."
      samantha.c "Okay. I need to go now. My shift at the coffee shop starts soon."
      $ samantha.whore_status = 5
      $ samantha.conversation_event = 7
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  rem tags 'whore_test_hypno_dildo' from samantha
  return

label samantha_whore_test_2_dont_hypno:
  wt_image barista_test_3_2
  samantha.c "This is what my tits look like.  In person."
  wt_image barista_test_3_3
  samantha.c "This is what my ass looks like."
  wt_image barista_test_3_4
  samantha.c "And this is what my pussy looks like."
  wt_image barista_test_3_1
  samantha.c "So what do you think?  Will I appeal to straight men enough that you think I can do sexual concierge work?"
  $ title = "What do you tell her?"
  menu:
    "I'm certain you can do this work":
      player.c "I'm now confident that you can do this work, Sam. I can look after the marketing and logistics for you for a small cut."
      samantha.c "Could you?  That would be great."
      player.c "What do you want to call yourself?  Professionally?"
      samantha.c "What do you mean?"
      player.c "It's typical in this line of business to use a professional name.  Something different than your real name.  Something that inspires confidence in the client."
      samantha.c "How about 'Samantha'?"
      "You do your best to stifle a reaction."
      player.c "Uhh, okay. Sure. I'll let you know when I have your first client lined up.  It may take a day or so."
      samantha.c "Okay. Great. Let's give it a try. I need to go now. My shift at the coffee shop starts soon."
      $ samantha.whore_status = 3
      $ samantha.conversation_event = 13
      call convert(samantha, "whore") from _call_convert_14
    "I need to test your sex skills to know for sure":
      player.c "You pass the visual inspection, Sam. Now I just need to test your sex skills, to be certain I can recommend you to potential clients."
      samantha.c "Really?"
      player.c "Really. You're a lesbian. I don't know whether you know enough about pleasing men? Take blow jobs for example. It's a pretty basic skill. Are you any good at them?"
      samantha.c "I think I'm okay."
      player.c "Show me."
      wt_image barista_test_3_5
      "Sam drops to her knees and opens your pants."
      samantha.c "I don't think it's too complicated with men, is it?  The guys I've blown have never complained."
      player.c "Men don't often complain when they have a woman's mouth wrapped around their cock. We're talking about making you a sexual professional. You'll be held to a higher standard when men are paying you to help them with their problems. Show me how you suck a cock, Sam."
      wt_image barista_test_3_6
      "She closes her eyes and takes you into her mouth."
      player.c "That's what I was worried about. That's amateurish, Sam. Do you want me to tell you how to do it correctly?"
      wt_image barista_test_3_7
      "She nods slightly, her lips still wrapped around your cock."
      player.c "Start with the balls. Think of them like you would a woman's labia. You want them warmed up and excited before you go further."
      wt_image barista_test_3_8
      player.c "Once you have his balls warmed up, you can move on to the shaft. Try to get the whole thing into your mouth."
      wt_image barista_test_3_9
      "Sam starts to gag as she tries to fit your entire length inside her."
      player.c "I know. It takes practice. Try working on bananas at home, to learn how to control the gag reflex. The objective is to get his full shaft inside you, so that your tongue and lips are right down to his balls."
      wt_image barista_test_3_10
      player.c "After that, you want to vary the sensations on his cock. Use your lips. Use your fingers. Use your tongue."
      player.c "Just like you would with a woman, you want to tease him in different ways, letting the pleasure build up slowly, until he's almost ready to explore."
      player.c "Keep your eyes on him while you're sucking him. That personal contact will turn him on too, just like it does for a woman."
      wt_image barista_test_3_11
      player.c "As his pleasure builds, you can spend more time on the head of his cock, especially the underside. That's his closest equivalent to the clit on a woman."
      player.c "You don't need to stimulate the underside of his cock head to get him to cum, but you can make his eventual orgasm more intense by spending time on that very sensitive region."
      player.c "At this point, men will have different preferences. Some will want to hold your head and fuck your mouth until they orgasm. Others will want you to pump their shaft while you suck on their cock head until they cum."
      wt_image barista_test_3_12
      player.c "I want you to pump my cock without sucking on it, so that my cum shoots up and lands on your face. Open your mouth while you're pumping me. Let's see how much you can catch on your tongue. You need to get familiar with the trajectory of men's sperm, if you want to avoid getting it in your hair or your eyes."
      wt_image barista_test_3_13
      player.c "[player.orgasm_text]"
      player.c "Good job catching it."
      samantha.c "I used to play softball."
      $ samantha.blowjob_count += 1
      $ samantha.swallow_count += 1
      orgasm
      wt_image barista_test_3_14
      samantha.c "So what do you think? Will I be able to please straight men enough that you think I can do sexual concierge work?"
      $ title = "What do you tell her?"
      menu:
        "I'm certain you can do this work":
          player.c "I'm now confident that you can do this work, Sam. I can look after the marketing and logistics for you for a small cut."
          wt_image barista_test_3_1
          samantha.c "Could you?  That'd be great."
          player.c "What do you want to call yourself?  Professionally?"
          samantha.c "What do you mean?"
          player.c "It's typical in this line of business to use a pseudoname.  Something different than your real name.  Something that inspires confidence in the client."
          samantha.c "How about 'Samantha'?"
          "You do your best to stifle a reaction."
          player.c "Uhh, okay. Sure. I'll let you know when I have your first client lined up. It may take a day or so."
          samantha.c "Okay. Great. Let's give it a try. I need to go now. My shift at the coffee shop starts soon."
          $ samantha.whore_status = 3
          $ samantha.conversation_event = 13
          call convert(samantha, "whore") from _call_convert_15
        "Maybe you're not cut out for this after all":
          player.c "I'm not sure you're really cut out for this work after all, Sam."
          wt_image barista_test_3_1
          samantha.c "I was worried about that. I'm probably just too much of a lesbian to appeal to most guys. Thanks for testing me, before I made a fool of myself with some stranger."
          player.c "You're welcome.  Perhaps we should try and find a different career for you?  We can chat more, at the coffee shop, after we've both had a chance to think some more."
          samantha.c "Okay.  I need to go now.  My shift at the coffee shop starts soon."
          $ samantha.whore_status = 5
          $ samantha.conversation_event = 7
          $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
    "Maybe you're not cut out for this after all":
      player.c "I'm not sure you're really cut out for this work after all, Sam."
      samantha.c "I was worried about that. I'm probably just too much of a lesbian to appeal to most guys."
      player.c "Perhaps we should try and find a different career for you?  We can chat more, at the coffee shop, after we've both had a chance to think some more."
      samantha.c "Okay.  I need to go now.  My shift at the coffee shop starts soon."
      $ samantha.whore_status = 5
      $ samantha.conversation_event = 7
      $ samantha.week = week # note: this makes sure a week passes before next conversation takes place
  return

label samantha_doll_return:
  wt_image barista_doll_1
  "You wake up to the sound of a large crate being delivered to your back porch. Whoever dropped it off is gone by the time you get outside."
  summon samantha no_follows
  wt_image barista_doll_2
  "Inside the crate you find Sam ... or at least what used to be Sam. She seems to be alive, although you're not sure how, as she shows no sign of breathing."
  call forced_movement(basement) from _call_forced_movement_937
  summon samantha no_follows
  "You can't leave her outside or around the house for someone to stumble upon, so you take her down into the basement, where you can examine her more closely later."
  $ samantha.doll_return_week = 0
  $ samantha.slaver_events = 11
  call convert(samantha, "doll") from _call_convert_16
  $ samantha.change_full_name("", "Sam", "the Pleasure Doll")
  add tags 'transformed' 'post_continuing_actions' to samantha
  $ samantha.training_regime = 'daily'
  $ samantha.fixed_location = basement
  $ samantha.location = basement
  call forced_movement(living_room) from _call_forced_movement_938
  return

label samantha_avalon_thank_you:
  wt_image front_door
  "Friday morning, there's a knock on your door."
  summon samantha
  wt_image barista_avalon_1
  samantha.c "Hi! It's me. Sorry to drop by your house unannounced like this. I just wanted to thank you for all your help. I'm really loving this new job with Avalon. I think I'm good at it, too!"
  samantha.c "This might be the perfect career for me. I can't wait to tell my ex about what I'm doing now. She's going to be so proud of me."
  player.c "Would you like to come in?"
  samantha.c "I'd love to, but I can't. I need to get at my prospecting for the day. I just wanted to drop something off to you, as a little token of my appreciation."
  samantha.c "It's a special product that's not in our catalog yet. I'm supposed to only offer it to my best customers. I can't take you on as a customer because you live in another saleswoman's territory. Amy, I think she said her name was. So I can't sell it to you."
  samantha.c "But I can give it to you for free. It's supposed to help you win over the person of your dreams. I don't imagine it actually works. And I'm sure you don't really need any help in that area."
  if samantha.has_tag('asked_on_date_pre_break_up') or samantha.has_tag('asked_for_date_after_break_up'):
    samantha.c "Then again, you did ask me out, and I'm blatantly gay, so maybe you could use some help on the relationship front? You know, to help you figure out who might actually be attracted to you?"
  samantha.c "Anyway, here it is.  I hope its useful to you. Bye!  And thanks again!!"
  "Sam disappears before you can say anything more."
  $ samantha.avalon_sales_status = 4
  $ tracy.opp = 2
  add 1 love_potion to player notify
  # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
  # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
  # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
  #call convert(samantha, "unavailable")
  $ samantha.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with coffee shop may not be needed going forward; should ideally be cleaned up
  call character_location_return(samantha) from _call_character_location_return_644
  return

label samantha_visit_gloria:
  call forced_movement(club) from _call_forced_movement_939
  summon samantha
  summon gloria
  wt_image barista_club_job_1_1
  "As promised, in the morning you bring Sam to meet the Club President and his wife. Gloria is working at her desk. She seems preoccupied."
  if gloria.solution_status == 3:
    gloria.c "Trying to get the materials for our next event is driving me up the wall! Go see my husband, he'll check her out and I'll join you in a bit."
  else:
    gloria.c "All these requests to attend fundraisers is driving me up the wall! There are only so many vacuous social events I can do in a week. Go see my husband, he'll check her out and I'll join you in a bit."
    $ tracy.opp = 2
  wt_image barista_club_job_1_2
  "Her husband, on the other, seems in a great mood. The prospect of getting his live in serving girl has him in high spirits."
  club_president.c "You're the new girl?"
  samantha.c "Yes, I guess.  I'm Sam.  Oh!"
  "She cries out in surprise as he picks her up."
  club_president.c "Hi, Sam.  You're very pretty."
  samantha.c "Thank you.  You're very ... friendly."
  club_president.c "I'm feeling friendly.  May I kiss you?"
  wt_image barista_club_job_1_3
  samantha.c "Sure, I guess.  Ohmmpph"
  "He smothers her lips in his.  Despite being caught by surprise, Sam tries her best to kiss him back."
  wt_image barista_club_job_1_4
  club_president.c "You're a nice kisser."
  samantha.c "Thanks. You're ..."
  club_president.c "Can I check you out?"
  samantha.c "Oh, okay."
  "He pulls up the front of her dress."
  club_president.c "Nice!  You're pierced."
  samantha.c "Thanks, I ...."
  club_president.c "Do you like to be spanked?"
  samantha.c "Not really."
  club_president.c "That's okay. My wife and I aren't into that either. We're the straight fuck and suck types. Well, she's not straight. She likes boys and girls. I only like girls. Can I taste you?"
  wt_image barista_club_job_1_5
  samantha.c "Uh, okay.  Oh!"
  "She startles as he spins her around and licks her from behind."
  samantha.c "Um, I only like girls, too.  Is that going to be a problem?"
  club_president.c "Will you suck my cock and let me fuck you when I'm horny?"
  samantha.c "Sure. I mean, if its keeping you from getting your work done, I'll help out however I can."
  club_president.c "Then I don't think your sexual orientation will be an issue."
  samantha.c "Oh, good!"
  wt_image barista_club_job_1_6
  "From the other room, you hear Gloria call out."
  gloria.c "Finally!  Almost finished.  I'll be with you in a minute."
  club_president.c "No rush!  Sam was just about to give me a kiss and a blow job."
  samantha.c "Oh, okay."
  wt_image barista_club_job_1_7
  samantha.c "Mmmpphhh"
  club_president.c "That's it. Show me how deep you can take me."
  wt_image barista_club_job_1_8
  club_president.c "Nice. My turn now."
  "He pulls down Sam's top and licks her nipple."
  samantha.c "Oh!"
  wt_image barista_club_job_1_9
  "Then he pushes her back onto the sofa."
  club_president.c "Lie back.  Do you like this?"
  samantha.c "It's a little weird."
  "Gloria finally arrives, having wrapped up her work."
  gloria.c "Let me take a look. Oh, you're barely wet. My husband's usually a better pussy licker than that. Don't you like oral?"
  samantha.c "I do, it's just ..."
  wt_image barista_club_job_1_10
  samantha.c "... oohhh!"
  gloria.c "There.  Sometimes it just takes a woman's touch."
  wt_image barista_club_job_1_11
  club_president.c "Do you like my wife's tongue?"
  samantha.c "Uh huh!"
  wt_image barista_club_job_1_10
  gloria.c "Okay, you've established your lesbian credentials, my dear.  And thank you for the flattering flood of pussy juice.  But are you going to be able to do this job?"
  gloria.c "My husband is a very important and busy man. Sometimes he just needs a quick fuck between meetings or when he gets home from a difficult day. Are you going to be able to do that, when I'm not around to warm you up?"
  wt_image barista_club_job_1_11
  samantha.c "I think so.  Yes."
  gloria.c "Let's see. Try to pretend I'm not here. His cock is hard and he needs you to look after it. Can you do that?"
  wt_image barista_club_job_1_13
  gloria.c "Well, if she lubes herself up first, she seems to be okay at that."
  club_president.c "Is she ever! My wife has a busy stressful life too, though. You're going to need to keep her relaxed, as well as me."
  wt_image barista_club_job_1_14
  "Sam doesn't waste time replying. She just repositions herself to look after the open pussy Gloria offers her."
  wt_image barista_club_job_1_15
  "Sam seems to be fitting in very well with the Club President and his wife. Gloria offers approval of her service first ..."
  gloria.c "Oooohhh  Ooohhh  Oh!  YEESSSSS!!"
  wt_image barista_club_job_1_16
  "... followed by her husband, who unloads into Sam as his wife pumps his balls."
  club_president.c "Aaaaahhhh!!!!"
  wt_image barista_club_job_1_17
  club_president.c "So what do you think, Gloria?  Can we keep her?"
  gloria.c "All right. We'll put you on a short term contract, and see how it works out.  Can you start today?"
  samantha.c "Sure"
  gloria.c "I'll have a bedroom set up for you at the top of the stairs. You can move your stuff in this afternoon. For now, help me get his cock clean. He has a meeting in 20 minutes and he can't be going to it with the smell of your pussy juices on him."
  samantha.c "Okay! Thank you so much! I'm really looking forward to this new career. I've never had a chance to work with successful people before. I'm sure I'll learn a lot."
  "Everything seems to be working out fine here, so you leave them to their business and head home. You should check in with them at the Club in a few days and see how things are going."
  $ gloria.discussed_barista = 4
  $ club_president.discussion_pending = 7
  $ club_president.discussion_week = week
  $ samantha.new_barista_switch = 1
  $ samantha.change_full_name("", "Sam", "the Club Maid")
  $ samantha.training_regime = 'daily'
  add tags 'maid' 'can_be_in_club' to samantha
  call forced_movement(living_room) from _call_forced_movement_940
  call character_location_return(samantha) from _call_character_location_return_645
  call character_location_return(gloria) from _call_character_location_return_646
  return

# End Week
label samantha_end_week:
  ## Whores or Prof Domme
  if samantha.whore_status == 4:
    $ samantha.whore_status = 6 # just for consistency with Rags coding, where unconvert from whore status happened here rather than at the time status was changed to 4
  ## Barista Wedding Announcement
  if samantha.wedding_week == week:
    call samantha_wedding_announcement from _call_samantha_wedding_announcement
  ## Barista Slaver Events Goes missing
  if samantha.slaver_events == 3 or samantha.slaver_events == 4:
    $ samantha.conversation_event = 16
  ## Barista Slaver Payment
  if week > samantha.slaver_payment_week and samantha.slaver_events == 7:
    call samantha_slaver_payment from _call_samantha_slaver_payment
  ## Barista Slaver Doll Event
  if week > samantha.slaver_doll_week and samantha.slaver_events == 8:
    call samantha_slaver_doll_event from _call_samantha_slaver_doll_event
  ## Barista Slaver Police Visit
  if week > samantha.slaver_police_week and samantha.slaver_police_week > 0:
    call samantha_slaver_police_visit from _call_samantha_slaver_police_visit
  ## Barista Avalon Lady Timer
  if samantha.avalon_sales_status == 1 or samantha.avalon_sales_status == 2:
    $ samantha.avalon_sales_status += 1
  return

label samantha_slaver_event:
  wt_image barista_slaver_1
  "You receive an urgent message from 'Samantha's' last client."
  player.c "I'm sorry. Samantha's taking a break right now, and not available to see clients."
  samantha_whore_client_3 "That's fine. I wasn't looking to hire her. I want to buy her."
  player.c "Her contract? If you're interested in becoming her new manager, you need to know that she's not sure she's going to be able to continue in this business."
  samantha_whore_client_3 "Not her contract. Her. I have a customer overseas, a collector of interesting female specimens. I've discussed Samantha with him, and he's placed an order for her."
  samantha_whore_client_3 "Procuring her would be much faster and simpler if you could deliver her to me. Bring her to the docks tonight, with her guard down, and I'll pay you 600. My man will contact you when they see you and her - and just the two of you - arrive."
  $ title = "What do you do?"
  menu:
    "Agree":
      player.c "I'll ..."
      "He cuts you off."
      samantha_whore_client_3 "Just bring her to the docks tonight."
    "Ask for 1000":
      player.c "1000"
      samantha_whore_client_3 "Pardon?"
      player.c "I'll do it for 1000."
      samantha_whore_client_3 "That's too much. Forgetting about the heightened risk of detection the more money we move around, my profit margins aren't that big. 600 is as much as I'll share, to make this a quick transaction."
      $ title = "What do you say?"
      menu:
        "Accept 600":
          player.c "600 it is."
          samantha_whore_client_3 "Just bring her to the docks tonight."
        "Insist on more":
          player.c "That's not enough."
          "There's silence on the other end for a moment."
          samantha_whore_client_3 "750.  That's my best offer."
          $ title = "What do you say?"
          menu:
            "Accept 750":
              player.c "750 it is."
              samantha_whore_client_3 "Just bring her to the docks tonight."
              $ samantha.slaver_fee = 750
            "Insist on more":
              player.c "That's not ..."
              "He hangs up."
    "Object":
      player.c "I ..."
      "He cuts you off."
      samantha_whore_client_3 "Just bring her to the docks tonight."
    "Need time to think":
      player.c "I ..."
      "He cuts you off."
      samantha_whore_client_3 "Just bring her to the docks tonight."
  $ samantha.slaver_events = 2
  # $ samantha_whore_client_3.change_name = ("Slaver") # probably more confusing than it's worth
  return

label samantha_slaver_payment:
  "You received a transfer of funds. There's no source provided, but it appears that the unit formally known as Sam has made it to her new owner, and you've been rewarded accordingly."
  change player money by samantha.slaver_fee notify
  $ samantha.slaver_events = 8
  $ samantha.slaver_doll_week = week + 11
  if samantha.slaver_fee > 600:
    $ samantha.slaver_police_week = week + 1
  return

label samantha_slaver_doll_event:
    "You have a voice message from the man who bought Sam the Barista from you, which is odd as you're sure your phone didn't ring."
    samantha_whore_client_3 "The buyer of your friend is finished with her, and ready to play with some new toys.  If you're interested in having her back, I'm willing to make a trade with you."
    samantha_whore_client_3 "You bring me another woman, and I'll send you back your friend."
    samantha_whore_client_3 "Just so you're aware, however, there's been substantial modification of your friend since the last time you saw her."
    samantha_whore_client_3 "I'm sending you details on how you can contact me.  Let me know when you're ready to make a trade."
    $ samantha.slaver_events = 9
    return

label samantha_slaver_police_visit:
  wt_image police_door
  "There's a knock on your door.  It's the police."
  police_officer "Sir.  We need you to come down to the station for questioning."
  call forced_movement(outdoors) from _call_forced_movement_941
  wt_image police_interview
  if player.has_tag('lawyer_on_retainer'):
    player.c "My lawyer would be happy to explain it to you."
    police_officer "There's no reason to bring lawyers into this yet."
    player.c "I'm sitting in a police station being questioned.  I think there is.  I want to speak to Janice."
    "They let you speak to Janice."
    "She speaks to them."
    call forced_movement(living_room) from _call_forced_movement_942
    wt_image current_location.image
    "They let you go home."
  else:
    player.c "Why?  I've done nothing wrong."
    police_officer "We believe the money came from a known felon. A trafficker of people. A very unsavory character. Do you recognize this woman?"
    "They pass over a photo of Sam."
    player.c "Yes. She used to serve coffee downtown."
    police_officer "She also used to whore for you.  Do you know where she is?"
    player.c "No"
    police_officer "The man we're looking for contacted you about her. We searched your communications records and it looks like he set up a visit with her, when you were pimping her as your whore."
    player.c "She was a sexual concierge, not a whore. And a free woman. She gave up that work. Then she left. If you're worried about her, why don't you find her and ask if she's okay? If you're worried about him, why don't you catch him?"
    police_officer "So far, we haven't been able to find either of them. But we have found you, and we think you're connected. We're charging you with criminal conspiracy."
    if player.money - player.min_money >= 200:
      "It takes a week and costs you 200 in legal bills, but you're finally able to get a lawyer to get them to drop their flimsy case against you."
      call forced_movement(living_room) from _call_forced_movement_943
      wt_image current_location.image
      "Time to try and pick up your life where you left off, only one week later."
      change player money by -200
      #$ total_days += 5 - day # no idea when or why total_days is ever used, but it increases each day
      #$ day = 5  # skip this methodology as we're already on a week end
      #end_day
      $ week += 1 # use this to advance week instead
    else:
      wt_image jail_1
      "The police have a flimsy case, and a decent lawyer would have gotten you out of jail reasonably fast."
      "Unfortunately, you didn't have access to enough money to hire a decent lawyer. You end up rotting in jail for six months until they finally decide they can't get to the men they want through you. Then they drop the charges and release you."
      "It's too late now to pick up the pieces of your old life. Time to move on to new things. Your career as the Wife Trainer is over."
      ### END THE GAME ###
      jump end_game
  $ samantha.slaver_police_week = 0
  return

label samantha_wedding_announcement:
  notify "You received a new message today."
  notify
  $ samantha.action_show_wedding_message = living_room.add_action("Message from Sam the Barista", label = samantha.short_name + "_wedding_message", context = '_check_messages', condition = "not samantha.has_tag('married_girlfriend')")
  $ tracy.opp = 2
  return

## Club and Stage Labels
label samantha_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if samantha.has_tag('in_club_now'):
            $ samantha.location = club
    elif samantha.has_tag('maid') and samantha.can_be_interacted:
        if samantha.club_presence > 1:
            $ samantha.club_presence -= 1
        elif samantha.club_presence == 1:
            $ samantha.club_presence = 0
            $ samantha.location = club
            add tags 'in_club_now' to samantha
        else:
            $ samantha.random_number = renpy.random.randint(1, 10)
            if samantha.random_number > 8:
                $ samantha.club_presence = 1
            elif samantha.random_number > 6:
                $ samantha.club_presence = 2
            elif samantha.random_number > 4:
                $ samantha.club_presence = 3
            elif samantha.random_number > 2:
                $ samantha.club_presence = 4
            else:
                $ samantha.club_presence = 5
    return

label samantha_club_send_home:
    call character_location_return(samantha) from _call_character_location_return_647
    return

## Character Specific Timers
# N/A

########### ROOMS ###########
# Coffee Shop
# see coffee_shop.rpy

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
