## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: selectivepaperclip

# Package Register
register amy_pregame 10 in core as "Amy the Avalon Lady"

# Pregame
label amy_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', 'Amy the Avalon Lady (Kristal Summers)')]

    ## Character Definition
    # Red
    amy = Person(Character("Amy", who_color="#FF0000", what_color="#FF0000", window_background = gui.dialogue_background_medium_font_color), "amy", cut_portrait = True, prefix = "", suffix = "the Avalon Lady")

    # Other Characters
    # Navy
    amy_husband = Character("Angry Man", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    # N/A

    ## Tags
    # Common Character Tags
    #amy.add_tags('no_hypnosis', 'likes_boys', 'visit_pending')
    amy.add_tags('likes_boys', 'visit_pending')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    amy.change_status("minor_character")
    candles_avon = Item('Candles', 'cda', with_examine = True, desire_mod = 5)

    # Start Day Events
    start_day_labels.append('amy_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    amy.add_stats_with_value('event_count', 'event_week', 'potion_proceed')

    amy.event_week = 2  ## pushes her first visit to the second week

  return

# Initial Contact Message
# OBJECT: Check Messages
# label amy_message: ## commented out as this character does not have
#  return

# Character Rejected
# label amy_rejected:
#  sys "You may no longer accept this assignment." ## commented out as minor character should not have
#  return

# Display Portrait
# CHARACTER: Display Portrait
label amy_update_media:
    $ amy.change_image('avon_house_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label amy_examine:
    "Your local neighborhood Avalon Lady."
    return

# Talk to Character
label amy_talk:
    "You have nothing to talk to her about."
    return

## Character Specific Actions
# N/A

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
# label amy_contact: ## commented out as this character does not have
#    pass
#    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_amy:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_amy:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_amy:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_amy:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_amy:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_amy:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_amy:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_amy:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_amy:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_amy:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_amy:
  "You should try this on someone else."
  return

# Candles - Avon
label cda_examine:
  "The candles help set a nice mood in the room."
  return

########### TIMERS ###########
## Common Timers
# Start Day
# Start Day
label amy_start_day:
  ## End Day - Thursday and Avon Visit?
  if day == 4 and week >= amy.event_week and amy.has_tag('visit_pending'):
    if (amy.event_count == 0): # First visit
      call amy_event_0 from _call_amy_event_0
    elif (amy.event_count == 1): # Brings candles
      call amy_event_1 from _call_amy_event_1
    elif (amy.event_count == 2): # Brings junk order
      call amy_event_2 from _call_amy_event_2
    elif (amy.event_count == 3): # BJ
      call amy_event_3 from _call_amy_event_3
    elif (amy.event_count == 4): # Hypnosis visit
      call amy_event_4 from _call_amy_event_4
    elif (amy.event_count == 5): # Sex
      call amy_event_5 from _call_amy_event_5
    call character_location_return(amy) from _call_character_location_return_740
    wt_image current_location.image
  return

# End Day - Thursday and Avon Visit?
label amy_event_0:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_1
  amy.c "Good morning!  I hope I didn't disturb you.\n\nMy name is Amy and I'm your local Avalon representative."
  amy.c "I know you're new to the neighborhood, so I wanted to drop by and say \"Welcome to the Neighborhood\"!\n\nMay I speak to the lady of the house?"
  player.c "It's just me."
  wt_image avon_door_2
  if player.has_tag('supersexy'):
    amy.c "Really?  That surprises me.  I mean ... look at you.\n\nWell, no matter."
  amy.c "Don't worry. I'm sure that will change soon.\n\nLet me show you one of my catalogs. We have some lovely gifts that would be just right for that special lady in your life."
  $ title = "What do you do?"
  menu menu_amy_event_0:
    "Send her away":
      "She looks a little disappointed, but only a little. Salespeople get used to rejection quickly."
    "Look at her catalog":
      "Most of the catalog is full of junk that wouldn't impress anyone as a gift.\n\nThere is a set of candles, however, that might look nice in your boudoir."
      amy.c "Those candles are one of our best sellers.  They really set a nice, romantic mood."
      if player.has_tag('supersexy'):
        extend "  Not that you need any help with that, of course."
      amy.c "They're only 25, and you don't have to pay until they're delivered. I could have those for you in two weeks."
      $ title = "Order the candles?"
      menu:
        "Yes":
          player.c "Okay, I'll take them."
          amy.c "Wonderful!  I'll be back in a couple of weeks with your order."
          $ amy.event_count = 1
          $ amy.event_week = week + 2
          add tags 'visit_pending' to amy
        "No":
          "She looks a little disappointed, but only a little.  Salespeople get used to rejection quickly."
    "Seduce her" if player.has_tag('supersexy') and not amy.has_tag('event_0_seduced'):
      player.c "I would love to take a look at what you have to offer. Please come in, and you can tell me all about your business, and your products. And I want to hear about you, too. How did you get into this line of work?"
      amy.c "Oh my! Well it's really not that interesting ... but ..."
      amy.c "Goodness. I'd love to come in, I really would. But it's not safe. You understand, I hope? Too many weirdos out there. Not that you are, of course!"
      amy.c "It's just, I need to keep myself safe. And my husband is very jealous. He wouldn't want me spending time alone with another man. Perhaps you could just take a look at my catalog here in the doorway?"
      add tags 'event_0_seduced' to amy
      $ title = "What do you do?"
      jump menu_amy_event_0
    "Hypnotize her" if player.can_hypno(amy) and not amy.has_tag('event_0_hypno'):
      "You didn't have your focus on you when you answered the door, so you try to get her inside."
      player.c "Please come in.  I need to get something first, and then I'd be happy to take a look at your catalog while we chat."
      amy.c "I'm sorry. I'd love to come in, I really would. But it's not safe. You understand, I hope? Too many weirdos out there. Not that you are, of course!\n\nPerhaps you could just take a look at my catalog here in the doorway?"
      add tags 'event_0_hypno' to amy
      $ title = "What do you do?"
      jump menu_amy_event_0
    "Dominate her" if player.has_tag('dominant') and not amy.has_tag('event_0_dom'):
      player.c "It's really quite rude, knocking on people's doors and disturbing their day while you try and sell them something. I didn't give you permission to come here today, did I?"
      amy.c "Well, no ..."
      player.c "I didn't give you permission to disturb me either."
      amy.c "I didn't think ..."
      player.c "And you haven't asked for my permission to try and sell me something."
      amy.c "If you just let me show you a few items in the catalog, I'm sure we can quickly figure out if there's anything here you might like. Then I'll be on my way. I won't take up very much of your time."
      "She's either not submissive by nature, or not attracted to you. Either way, she's not giving any indication of falling for your charms. At least not right now."
      add tags 'event_0_dom' to amy
      $ title = "What do you do?"
      jump menu_amy_event_0
  return

label amy_event_1:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_1
  amy.c "Good morning!  I have your candles."
  $ title = "Pay her for the candles?"
  menu:
    "Yes (costs 25)" if player.money - player.min_money >= 25:
      call amy_event_1_buy_candles from _call_amy_event_1_buy_candles
    "No":
      player.c "I'm sorry.  I don't seem to have the money on me right now."
      amy.c "That's okay.  I'll stop by next week."
      add tags 'visit_pending' to amy
  return

label amy_event_1_buy_candles:
  add 1 candles_avon to boudoir
  ## boudoir image changes re adding the candles
  ## NEED: move these image changes to room_enter label
  $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
  $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
  if boudoir.has_item(silk_sheets):
    if boudoir.added_desire < 20:
      $ boudoir.change_portrait(5)
      $ boudoir.change_image(5)
    elif boudoir.added_desire < 30:
      $ boudoir.change_portrait(6)
      $ boudoir.change_image(6)
    else:
      if boudoir.has_item(ceiling_mirror):
        $ boudoir.change_portrait(8)
        $ boudoir.change_image(8)
      else:
        $ boudoir.change_portrait(7)
        $ boudoir.change_image(7)
  else:
    if boudoir.added_desire < 20:
      $ boudoir.change_portrait(2)
      $ boudoir.change_image(2)
    elif boudoir.added_desire < 30:
      $ boudoir.change_portrait(3)
      $ boudoir.change_image(3)
    else:
      $ boudoir.change_portrait(4)
      $ boudoir.change_image(4)
  change player money by -25 notify
  player.c "Wonderful.  Won't you please come in."
  amy.c "I'm not supposed to go inside when there isn't a woman around."
  player.c "Of course. I understand. Safety first. It's a shame, though. The candles look lovely. I'm sure you have samples of some other items you could show me. Too bad there's no room to do that properly here in the doorway."
  wt_image avon_door_3
  "Amy takes a guilty look around, as if a supervisor or safety consultant was watching her."
  amy.c "Well, you are a customer. I'm sure it would be okay if I just came in for a moment."
  wt_image avon_house_1
  if player.has_tag('wealthy'):
    amy.c "Oh my!  What a beautiful home you have!  I mean, I say that to everyone, but in your case, it's true.  Everything here is quality, real quality, isn't it?  Not just nice, but expensive nice."
  else:
    amy.c "What a beautiful home you have!  I love the way you've decorated it."
  $ title = "Show her the house?"
  menu:
    "Show her the boudoir":
      wt_image boudoir.image
      player.c "Thank you.  Let me show you the room where I'm putting the candles."
      ## I'm sure there's an easier way to test than this
      $ boudoir.desire_total = boudoir.moded_stat('desire_mod')
      $ boudoir.added_desire = boudoir.desire_total - boudoir.desire_mod
      if boudoir.added_desire >= 20:
        if player.has_tag('supersexy'):
          amy.c "This is ... wow  ... the room ... and you."
          wt_image avon_house_2
          "Amy looks flustered, and you wonder if she's going to throw herself at you.  Then she takes a deep breath and gathers herself together."
          amy.c "Let's go back to the living room and I can show you some of my samples.  I'm sure I have something you would like."
          $ amy.potion_proceed = 2
          $ amy.event_count = 3
          add tags 'visit_pending' to amy
          $ amy.event_week = week + 6
        else:
          amy.c "This is very nice. You have a lovely eye. Let's go back to the living room and I can show you some of my samples. I'm sure I have something you'll like."
      else:
        if boudoir.added_desire >= 10:
          if player.has_tag('supersexy'):
            amy.c "Very nice ... this room is quite ... and you."
            wt_image avon_house_2
            "Amy looks a bit flushed.  She takes a deep breath and gathers herself together."
            amy.c "Let's go back to the living room and I can show you some of my samples. I'm sure I have something you would like."
            $ amy.potion_proceed = 1
            $ amy.event_count = 3
            add tags 'visit_pending' to amy
            $ amy.event_week = week + 6
          else:
            if player.has_tag('supersexy'):
              amy.c "Hmmm. The candles help, don't they?  Not that you need any help in that department.  Let's go back to the living room and I can show you some of my samples.  I'm sure I have something you'll like."
            else:
              amy.c "Hmmm. The candles help, don't they?  Let's go back to the living room and I can show you some of my samples.  I'm sure I have something you'll like."
        else:
          amy.c "Well, at least the candles provide some ambience, don't they? Let's go back to the living room and I can show you some of my samples. I'm sure I have something you'll like."
      call amy_event_1_have_a_seat from _call_amy_event_1_have_a_seat
    "Show her the dungeon":
      wt_image dungeon.image
      player.c "Thank you.  Let me show you one of my favorite rooms."
      wt_image avon_house_3
      amy.c "Oh! I'm so glad my husband isn't into this sort of thing. With his temper, I can't imagine what he might do."
      if player.has_tag('dominant'):
        amy.c "You're really into this sort of thing aren't you?  Bossing women around?  It's no wonder you're not married."
        $ amy.potion_proceed = 1
      amy.c "Let's go back to the living room and I can show you some of my samples.  I'm sure I have something you'll like."
      call amy_event_1_have_a_seat from _call_amy_event_1_have_a_seat_1
    "Ask her to have a seat":
      call amy_event_1_have_a_seat from _call_amy_event_1_have_a_seat_2
    "Hypnotize her" if player.can_hypno(amy):
      wt_image avon_house_1
      player.c "Amy, take a look a look at this."
      call focus_image from _call_focus_image_15
      player.c "Look at this and listen to my voice.  Listen to my voice Amy.  Listen to my voice.  Only my voice now.  Only my voice."
      wt_image avon_house_4
      "It doesn't take long for her to fall under your trance."
      player.c "Get comfortable Amy. Take off your top and show me your breasts. Show me your breasts so that you'll be comfortable and I can enjoy our talk."
      wt_image avon_house_5
      if not player.has_tag('first_hypno_breasts_message'):
        add tags 'first_hypno_breasts_message' to player
        "[player.first_hypno_breasts_message_text]"
      "Amy strips out of her suit coat and top ..."
      wt_image avon_house_6
      "... then sits down on your sofa, cupping her breasts in her hands."
      call amy_event_1_hypnosis from _call_amy_event_1_hypnosis
  return

label amy_event_1_have_a_seat:
  wt_image avon_house_7
  "Amy takes a seat on your sofa and takes out her samples."
  amy.c "Some of these would make lovely gifts for the right woman."
  "You pay polite attention to her sales pitch, but there's really nothing here of interest to you."
  $ title = "What do you do?"
  menu menu_amy_event_1_have_a_seat:
    "Send her away":
      "She looks a little disappointed, but only a little.  Salespeople get used to rejection quickly. She gathers up her samples and leaves."
    "Order some junk (cost 25 on delivery)":
      player.c "Perhaps I can order some of this perfume."
      amy.c "Wonderful choice! I'll place the order. I should have it in a couple of weeks."
      "The perfume isn't something you'd give to anyone you like, but it will give you a chance to see Amy again, and perhaps something will come of that."
      $ amy.event_count = 2
      add tags 'visit_pending' to amy
      $ amy.event_week = week + 2
    "Ask if she has anything else" if not amy.has_tag('event_1_asked_anything_else'):
      $ amy.potion_proceed += 1
      player.c "There's nothing here that's quite right.  I don't suppose you have any other products?"
      if player.has_tag('wealthy'):
        "Amy looks around conspiratorially, then pulls another bottle out of her sample bag."
        wt_image avon_house_9
        amy.c "This isn't in our catalog yet, and I'm only supposed to offer this to our best customers.  I can clearly see, however, that that includes you."
        amy.c "It's supposed to help you attract a partner.  With your wealth, I'm sure you don't have trouble with that, but then again, what's the point of money if not to acquire the things that make life more enjoyable?"
        amy.c "It's expensive, of course, but I'm told it's worth every bit of it's 75 price tag."
        $ title = "Buy it?"
        menu menu_amy_event_1_dominate_buy_potion_a:
          "Yes (costs 75)" if player.money - player.min_money >= 75:
            player.c "All right, I'll give it a try."
            "Amy passes the potion over to you."
            amy.c "It's such a pleasure serving customers who understand value when they see it."
            "She gathers her samples back into her handbag and leaves."
            add 1 love_potion to player
            change player money by -75 notify
            $ amy.potion_proceed = 4
          "No thanks":
            player.c "I'll pass."
            wt_image avon_house_1
            amy.c "I understand.  Perhaps one of my other items, then?"
            $ title = "What do you do?"
            jump menu_amy_event_1_have_a_seat
      else:
        "She hesitates for just a moment before replying."
        amy.c "No, I can only sell you the things that are in the catalog."
        add tags 'event_1_asked_anything_else' to amy
        $ title = "What do you do?"
        jump menu_amy_event_1_have_a_seat
    "Seduce her" if player.has_tag('supersexy'):
      $ amy.potion_proceed += 1
      player.c "Perhaps we can put the products aside for the moment, and spend some time on you."
      wt_image avon_house_8
      amy.c "Oh!  My ...  you're just so ... sweet and ... so sexy ... and ..."
      if amy.potion_proceed > 2:
        wt_image avon_house_9
        "Suddenly, Amy pulls herself together and changes the topic.  She grabs one more sample from her handbag."
        amy.c "I'm only supposed to offer this to our best customers. I'm not sure why I didn't think about it earlier, when you asked if I had anything else to show you."
        amy.c "It's not in our catalog yet. It's supposed to help you attract a partner. I don't imagine it actually works. Not for most people, anyway."
        amy.c "But for you ... I mean look at you ... and still single?  Would you like this?  It's only ..."
        "She hesitates."
        amy.c "For you it's free.  For being such a ... good customer."
        add 1 love_potion to player
        player.c "That's very sweet of you, Amy.  Perhaps there's something I could do to show my appreciation?"
        wt_image avon_house_1
        amy.c "I need to leave now!"
        "She hastily gathers her samples back into her handbag and nearly flies out the door."
        $ amy.potion_proceed = 4
      elif amy.potion_proceed == 2:
        wt_image avon_house_9
        "Suddenly, Amy pulls herself together and changes the topic. She grabs one more sample from her handbag."
        amy.c "I'm only supposed to offer this to our best customers. It's not in our catalog yet. It's supposed to help you attract a partner. I don't imagine it actually works. Not for most people, anyway."
        amy.c "But for you ... I mean look at you ... and still single?  Would you like this?  It's only ..."
        "She hesitates."
        amy.c "For you it's only 25."
        $ title = "Buy it?"
        menu menu_amy_event_1_seduce_buy_potion:
          "Yes (costs 25)" if player.money - player.min_money >= 25:
            player.c "If you think it would be useful, then by all means I'd be happy to buy it."
            "Amy smiles as she passes the potion over to you."
            player.c "Perhaps we could get back to discussing you?"
            wt_image avon_house_1
            amy.c "I need to leave now!"
            "She hastily gathers her samples back into her handbag and nearly flies out the door."
            add 1 love_potion to player
            change player money by -25 notify
            $ amy.potion_proceed = 4
          "No":
            player.c "Not today, thank you."
            amy.c "That's okay.  I don't imagine it works anyway."
            player.c "Perhaps we could get back to discussing you?"
            wt_image avon_house_1
            amy.c "I need to leave now!"
            "Amy hastily gathers her samples back into her handbag and nearly flies out the door."
      elif amy.potion_proceed == 1:
        wt_image avon_house_1
        "Suddenly, Amy pulls herself together.  She hastily piles all of her samples back into her handbag."
        amy.c "I really should be going ... my husband you know ..."
        "Before you can stop her, she's out the door."
      $ amy.event_count = 3
      add tags 'visit_pending' to amy
      $ amy.event_week = week + 6
    "Dominate her" if player.has_tag('dominant'):
      player.c "Amy, we need to discuss your disobedience to rules."
      amy.c "What do you mean?"
      player.c "You're not supposed to be here, are you?  Your company's rules forbid you from entering a house alone with a single man."
      amy.c "Yes, but ..."
      player.c "No buts.  You broke the rules.  Girls who break the rules should be punished, don't you think?"
      if amy.potion_proceed > 0:
        amy.c "I think I understand why you're single."
        wt_image avon_house_9
        "She rummages in her bag and comes up with another sample."
        amy.c "This isn't in our catalog yet, and I'm only supposed to offer this to our best customers. For you, however, I'm making an exception. It's supposed to help you attract a partner."
        amy.c "I don't imagine it actually works. I think you, however, need all the help you can get in that department."
        amy.c "Would you like to give it a try?  It's only 50."
        $ title = "Buy it?"
        menu menu_amy_event_1_dominate_buy_potion_b:
          "Yes (costs 50)" if player.money - player.min_money >= 50:
            player.c "All right, I'll give it a try."
            "Amy passes the potion over to you."
            amy.c "I hope it helps you."
            "She gathers her samples back into her handbag and leaves."
            add 1 love_potion to player
            change player money by -50 notify
            $ amy.potion_proceed = 4
          "No thanks":
            player.c "I'll pass."
            wt_image avon_house_1
            amy.c "Well, I tried."
            "Amy gathers her samples back into her handbag and leaves."
      else:
        wt_image avon_house_1
        amy.c "This is getting a little too weird for me.  I think I'd best be going."
        "Amy gathers up her samples and leaves."
    "Hypnotize her" if player.can_hypno(amy):
      player.c "Amy, take a look a look at this."
      call focus_image from _call_focus_image_100
      player.c "Look at this and listen to my voice.  Listen to my voice Amy.  Listen to my voice.  Only my voice now.  Only my voice."
      wt_image avon_house_4
      "It doesn't take long for her to fall under your trance."
      player.c "Get comfortable Amy. Take off your top and show me your breasts. Show me your breasts so that you'll be comfortable and I can enjoy our talk."
      wt_image avon_house_5
      if not player.has_tag('first_hypno_breasts_message'):
        add tags 'first_hypno_breasts_message' to player
        "[player.first_hypno_breasts_message_text]"
      "Amy strips out of her suit coat and top ..."
      wt_image avon_house_6
      "... then sits cupping her breasts in her hands."
      call amy_event_1_hypnosis from _call_amy_event_1_hypnosis_1
  return

label amy_event_1_hypnosis:
    amy.c "Does this give you a good view of my breasts?"
    player.c "Yes, Amy."
    amy.c "Can I show you my samples now?"
    "Being single minded is likely a useful trait for salespeople.  Unfortunately, none of Amy's products samples are of any interest to you."
    player.c "I don't suppose you have any other products?"
    amy.c "The only other item I have isn't in our catalog yet. I'm only supposed to offer it to our best customers."
    player.c "I am a good customer, Amy. I bought candles from you. I am a very good customer. A customer who buys things from you is a very good customer. The best customers buy things from you. I bought things from you. Tell me about the special product Amy."
    amy.c "It's supposed to help you find a partner. I don't expect it actually works. You're a good customer, though. If you want to buy it, I can sell if to you. It only costs 50."
    $ title = "Buy it?"
    menu menu_amy_event_1_hypno_buy_potion:
        "Yes (costs 50)" if player.money - player.min_money >= 50:
            player.c "Yes, I would like to buy that."
            "Amy passes the potion over to you. You're not going to get anything else out of her."
            add 1 love_potion to player
            change player money by -50 notify
            $ amy.potion_proceed = 4
        "No thanks":
            $ title = "Ask her to come back so you can buy it later?"
            menu:
                "Yes come back":
                    player.c "I'm not going to buy that today, Amy, but you are going to come back and offer it to me again. I am one of your best customers, so you will come back and see if I want to buy your special item then."
                    amy.c "Okay."
                    "You're not going to get anything else out of her."
                    $ amy.event_count = 4
                    add tags 'visit_pending' to amy
                    $ amy.event_week = week + 2
                "No don't":
                    "The special product doesn't interest you, and you're not going to get anything else out of her."
    wt_image avon_house_1
    "You have her dress, then bring her out of her trance."
    amy.c "Thank you for your order, and for looking at my samples. You're a really good customer. Bye bye!"
    $ amy.hypno_session()
    return

label amy_event_2:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_1
  amy.c "Good morning!  I have your order."
  if player.money >= 25:
    $ title = "Pay her?"
    menu:
      "Yes" if player.money - player.min_money >= 25:
        change player money by -25 notify
        if player.has_tag('supersexy'):
          $ amy.potion_proceed = 1
          $ amy.event_count = 3
          add tags 'visit_pending' to amy
          $ amy.event_week = week + 6
        wt_image avon_house_7
        player.c "Wonderful.  Please come in."
        "Amy has a seat on your sofa and takes her samples out again."
        amy.c "Would you like to order anything else?"
        $ title = "What do you do?"
        menu menu_amy_event_2:
          "Send her away":
            "She looks a little disappointed, but only a little.  Salespeople get used to rejection quickly.\n\nShe gathers up her samples and leaves."
          "Order some junk (cost 25 on delivery)":
            player.c "Perhaps I could buy some of these scented soap products."
            amy.c "Wonderful choice!  I'll place the order.  I should have it in a couple of weeks."
            "The soap isn't something you'd give to anyone you like, but it will give you a chance to see Amy again, and perhaps something will come of that."
            $ amy.event_count = 2
            add tags 'visit_pending' to amy
            $ amy.event_week = week + 2
          "Ask if she has anything else":
            wt_image avon_house_9
            player.c "I don't suppose you have any other products?"
            "She hesitates for a moment before replying."
            amy.c "I do have one other thing.  It's not in the catalog yet, and I'm only supposed to offer it to out best customers.\n\nI'm not even sure it really works.  It's supposed to help you find a partner."
            amy.c "It only costs 50, which is a real bargain if it does what they say it does.  Since you've placed a couple of orders with me already, I suppose I could sell it to you, if you're interested?"
            $ title = "Buy it?"
            menu:
              "Yes (costs 50)" if player.money - player.min_money >= 50:
                player.c "Okay, I'll try that"
                "Amy passes the potion over to you."
                amy.c "I hope it helps you."
                "She gathers her samples back into her handbag and leaves."
                add 1 love_potion to player
                change player money by -50 notify
                $ amy.potion_proceed = 4
              "No":
                player.c "No thanks."
                amy.c "I understand.  I wouldn't want to spend good money on something that probably wouldn't work."
                jump menu_amy_event_2
          "Seduce her" if player.has_tag('supersexy'):
            $ amy.potion_proceed += 1
            player.c "Perhaps we can put the products aside for the money, and spend some time on you."
            amy.c "Oh!  My ...  you're just so ... sweet and ... so sexy ... and ..."
            if amy.potion_proceed > 2:
              wt_image avon_house_9
              "Suddenly, Amy pulls herself together and changes the topic. She grabs one more sample from her handbag."
              amy.c "I'm only supposed to offer this to our best customers. I'm not sure why I didn't think about it earlier, when you asked if I had anything else to show you. It's not in our catalog yet. It's supposed to help you attract a partner."
              amy.c "I don't imagine it actually works. Not for most people, anyway. But for you ... I mean look at you ... and still single?  Would you like this?  It's only .."
              "She hesitates."
              amy.c "For you it's free.  For being such a ... good customer."
              player.c "That's very sweet of you, Amy.  Perhaps there's something I could do to show my appreciation?"
              wt_image avon_house_1
              amy.c "I need to leave now!"
              "She hastily gathers her samples back into her handbag and nearly flies out the door."
              add 1 love_potion to player notify
              $ amy.potion_proceed = 4
            elif amy.potion_proceed == 2:
              wt_image avon_house_9
              "Suddenly, Amy pulls herself together and changes the topic. She grabs one more sample from her handbag."
              amy.c "I'm only supposed to offer this to our best customers. It's not in our catalog yet. It's supposed to help you attract a partner. I don't imagine it actually works. Not for most people, anyway."
              amy.c "But for you ... I mean look at you ... and still single?  Would you like this?  It's only ..."
              "She hesitates."
              amy.c "For you it's only 25."
              $ title = "Buy it?"
              menu:
                "Yes (costs 25)" if player.money - player.min_money >= 25:
                  player.c "If you think it would be useful, then by all means I'd be happy to buy it."
                  "Amy smiles as she passes the potion over to you."
                  player.c "Perhaps we could get back to discussing you?"
                  wt_image avon_house_1
                  amy.c "I need to leave now!"
                  "She hastily gathers her samples back into her handbag and nearly flies out the door."
                  add 1 love_potion to player
                  change player money by -25 notify
                  $ amy.potion_proceed = 4
                "No":
                  player.c "Not today, thank you."
                  amy.c "That's okay.  I don't imagine it works anyway."
                  player.c "Perhaps we could get back to discussing you?"
                  wt_image avon_house_1
                  amy.c "I need to leave now!"
                  "Amy hastily gathers her samples back into her handbag and nearly flies out the door."
            elif amy.potion_proceed == 1:
              wt_image avon_house_1
              "Suddenly, Amy pulls herself together.  She hastily piles all of her samples back into her handbag."
              amy.c "I really should be going ... my husband you know ..."
              "Before you can stop her, she's out the door."
          "Hypnotize her" if player.can_hypno(amy):
            wt_image avon_house_1
            player.c "Amy, take a look a look at this."
            call focus_image from _call_focus_image_16
            player.c "Look at this and listen to my voice.  Listen to my voice Amy.  Listen to my voice.  Only my voice now.  Only my voice."
            wt_image avon_house_4
            "It doesn't take long for her to fall under your trance."
            player.c "Get comfortable Amy. Take off your top and show me your breasts. Show me your breasts so that you'll be comfortable and I can enjoy our talk."
            wt_image avon_house_5
            if not player.has_tag('first_hypno_breasts_message'):
              add tags 'first_hypno_breasts_message' to player
            "[player.first_hypno_breasts_message_text]"
            "Amy strips out of her suit coat and top ..."
            wt_image avon_house_6
            "... then sits down on your sofa, cupping her breasts in her hands."
            amy.c "Does this give you a good view of my breasts?"
            player.c "Yes, Amy."
            amy.c "Can I show you my samples now?"
            "Being single minded is likely a useful trait for salespeople.  Unfortunately, none of Amy's products samples are of any interest to you."
            player.c "I don't suppose you have any other products?"
            amy.c "The only other item I have isn't in our catalog yet. I'm only supposed to offer it to our best customers."
            player.c "I am a good customer, Amy. I bought candles from you. I am a very good customer. A customer who buys things from you is a very good customer. The best customers buy things from you. I bought things from you. Tell me about the special product Amy."
            amy.c "It's supposed to help you find a partner. I don't expect it actually works. You're a good customer, though. If you want to buy it, I can sell if to you. It only costs 50."
            $ title = "Buy it?"
            menu:
              "Yes (costs 50)" if player.money - player.min_money >= 50:
                player.c "Yes, I would like to buy that."
                "Amy passes the potion over to you. You're not going to get anything else out of her."
                add 1 love_potion to player
                change player money by -50 notify
                $ amy.potion_proceed = 4
              "No thanks":
                $ title = "Ask her to come back so you can buy it later?"
                menu:
                  "Yes, come back":
                    player.c "I'm not going to buy that today, Amy, but you are going to come back and offer it to me again. I am one of your best customers, so you will come back and see if I want to buy your special item then."
                    amy.c "Okay."
                    "You're not going to get anything else out of her."
                    $ amy.event_count = 4
                    add tags 'visit_pending' to amy
                    $ amy.event_week = week + 2
                  "No, don't":
                    "The special product doesn't interest you, and you're not going to get anything else out of her."
            wt_image avon_house_1
            "You have her dress, then bring her out of her trance."
            amy.c "Thank you for your order, and for looking at my samples. You're a really good customer. Bye bye!"
            $ amy.hypno_session()
          "Dominate her" if player.has_tag('dominant'):
            player.c "Amy, we need to discuss your disobedience to rules."
            amy.c "What do you mean?"
            player.c "You're not supposed to be here, are you?  Your company's rules forbid you from entering a house alone with a single man."
            amy.c "Yes, but ..."
            player.c "No buts.  You broke the rules.  Girls who break the rules should be punished, don't you think?"
            if amy.potion_proceed > 0:
              wt_image avon_house_9
              amy.c "I think I understand why you're single."
              "She rummages in her bag and comes up with another sample."
              amy.c "This isn't in our catalog yet, and I'm only supposed to offer this to our best customers. For you, however, I'm making an exception. It's supposed to help you attract a partner. I don't imagine it actually works."
              amy.c "I think you, however, need all the help you can get in that department. Would you like to give it a try?  It's only 50."
              $ title = "Buy it?"
              menu:
                "Yes (costs 50)" if player.money - player.min_money >= 50:
                  player.c "Very well, I'll give it a try."
                  "Amy passes the potion over to you."
                  wt_image avon_house_1
                  amy.c "I hope it helps you"
                  "She gathers her samples back into her handbag and leaves."
                  add 1 love_potion to player
                  change player money by -50 notify
                  $ amy.potion_proceed = 4
                "No":
                  player.c "No thank you."
                  wt_image avon_house_1
                  amy.c "Well, I tried."
                  "Amy gathers her samples back into her handbag and leaves."
            else:
              wt_image avon_house_1
              amy.c "This is getting a little too weird for me.  I think I'd best be going."
              "Amy gathers up her samples and leaves."
      "No":
        player.c "I'm sorry.  I don't seem to have the money on me right now."
        amy.c "That's okay.  I'll stop by next week."
        add tags 'visit_pending' to amy
  return

# Playboy only visit
label amy_event_3:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_2
  amy.c "Good morning!  I ... wow, you look as good as I remembered ... "
  wt_image avon_door_3
  "She takes a quick look around."
  amy.c "Can I come in?"
  $ title = "Let her in?"
  menu menu_amy_event_3:
    "Send her away":
      "She's a married woman. You know how this ends, and it's always messy. Best to put a stop to it before it begins."
      wt_image avon_door_4
      "She's disappointed, but she'll get over it.  Salespeople get used to rejection quickly."
    "Let her in":
      wt_image avon_house_1
      amy.c "I've been trying not to think about you, but it hasn't worked."
      wt_image avon_bj_1
      amy.c "I shouldn't be here. I'm a married woman, and my husband is insanely jealous."
      wt_image avon_bj_2
      amy.c "But I can't help thinking about you being here ... all alone ... and how hard you must get ... I mean how hard it must be for you ... not having a wife to suck you off at night."
      wt_image avon_bj_3
      amy.c "And I thought, just one blow job ... that couldn't hurt, could it? Then I would know what you taste like."
      wt_image avon_bj_4
      "She sits down on your sofa, her head level with your crotch, and eyes the impression of your hard cock pressing against your pants, a dreamy look on her face. One blow job couldn't hurt, could it?"
      $ title = "What do you do?"
      menu menu_amy_event_3_blow:
        "Let her blow you":
          wt_image avon_bj_5
          amy.c "Ohhhh"
          "A little moan of happiness escapes her as you stand in front of her and unzip your pants. She leans in and smells your cock, breathing in deeply as if you smell nicer than the most fragrant rose."
          wt_image avon_bj_6
          "Cupping your balls in her hand, she gently licks the sensitive underside of your cockhead."
          wt_image avon_bj_7
          "Then she lowers her head and starts sucking you in earnest. She knows her way around a cock. Her tongue dances along the underside of your shaft as she bobs her hard up and down, her lips wrapped tight around you."
          "She can't quite get your full member into her mouth, but she tries. The whole time she's sucking you, her fingers tickle and tease your balls."
          wt_image avon_bj_8
          "You hold out as long as you can, but her talented mouth and hands soon have you ready to cum. As she tastes your pre cum on her tongue, she looks up at you, seeking direction on how and where you want to cum."
          $ title = "Where do you want to cum?"
          menu:
            "On her face":
              wt_image avon_bj_9
              "She starts pumping you with her fist, faster and faster, her tongue licking your head as her hand squeezes your balls."
              wt_image avon_bj_12
              "As you begin to spurt, she slides off the sofa and onto her knees in front of you."
              player.c "[player.orgasm_text]"
              "She closes her eyes as your cum shoots over her face."
              wt_image avon_bj_13
              "Only when you've emptied your load on her does she open her eyes again and look up at you."
              wt_image avon_bj_14
              "As your jizz drips off her face and onto her breasts, she squeezes her own nipples - hard."
              amy.c "I don't think that hurt anybody, right?  We both enjoyed ourselves and nobody ever needs to know."
              $ amy.facial_count += 1
            "In her mouth":
              wt_image avon_bj_9
              "She starts pumping you with her fist, faster and faster, her tongue licking your head as her hand squeezes your balls."
              wt_image avon_bj_10
              "As you begin to spurt, she wraps her lips around your cock and resumes sucking."
              player.c "[player.orgasm_text]"
              "She keeps her eyes locked on yours while you fill her mouth with cum."
              wt_image avon_bj_11
              "When you finally stop cumming, she slides off the sofa and onto her knees in front of you. She opens her mouth, as if to show you that she's swallowed it all."
              amy.c "I don't think that hurt anybody, right?  We both enjoyed ourselves and nobody ever needs to know."
              $ amy.swallow_count += 1
          if (amy.potion_proceed < 4):
            $ amy.potion_proceed = 4
            wt_image avon_house_9
            "As she's about to leave the house, Amy stops and pulls a bottle out of her bag."
            amy.c "I almost forgot. I was given this sample of a new product, that isn't in our catalog yet. I'm only supposed to offer it to my best customers ... and you are definitely my best customer."
            amy.c "It's supposed to help you find a partner.  I can't imagine why you would need any help in that, but since you're still single for some inexplicable reason, here - take it."
            add 1 love_potion to player
          add tags 'visit_pending' to amy
          $ amy.blowjob_count += 1
          $ amy.event_count = 5
          $ amy.event_week = week + 6
          orgasm notify
        "Send her away":
          "She's a married woman. You know how this ends, and it's always messy. Best to put a stop to it before it begins."
          wt_image avon_house_3
          "She's disappointed, but she'll get over it.  Salespeople get used to rejection quickly."
  return

# Hypnotist follow up visit to let you but potion
label amy_event_4:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_1
  amy.c "Good morning. I felt I should drop by and see if you wanted to buy this sample item I have. It's not in our catalog yet, and I'm only supposed to offer it to our best customers. But I felt somehow that maybe you might want it. Supposedly it helps you attract a partner. It only costs 50."
  $ title = "What do you do?"
  menu menu_amy_event_4:
    "Invite her in" if not amy.has_tag('event_4_invited'):
      player.c "Please come inside and let me take a look at it."
      wt_image avon_door_4
      amy.c "I'm not allowed.  It's not safe."
      "She looks apprehensive. Your hypnotic suggestion to return worked well enough to get her here, but she's fighting it. She may not know what you did to her, but she's wary of you now, and you're not easily going to be able to hypnotize her again."
      add tags 'event_4_invited' to amy
      jump menu_amy_event_4
    "Buy potion (costs 50)" if player.money - player.min_money >= 50:
      player.c "Yes, I would like to buy that."
      "Amy passes the potion over to you, then hurries away, seemingly happy to be away from you. You doubt you'll ever see her again."
      add 1 love_potion to player
      change player money by -50 notify
      $ amy.potion_proceed = 4
    "Tell her to come back":
      player.c "I don't have the money right now, but I'll happily buy it from you later, when I do."
      wt_image avon_door_2
      "She's wary about returning, but it is a possible sale, and she won't want to pass that up. She'll be back."
      add tags 'visit_pending' to amy
    "Send her away":
      amy.c "Okay.  That's fine.  Bye."
      "She hurries away, seemingly happy to be away from you. You doubt you'll ever see her again."
  return

#Playboy only event
label amy_event_5:
  rem tags 'visit_pending' from amy
  wt_image front_door
  player.c "In the morning, there's a knock on your door."
  summon amy
  wt_image avon_door_2
  amy.c "Hi!"
  "She brushes past you and into your house before you can stop her."
  wt_image avon_bj_1
  amy.c "I've been trying very hard to be good. I've never cheated on my husband and I swore I never would. But I keeping thinking about how good it would feel to have your body pressed against mine."
  wt_image avon_bj_2
  amy.c "I think I need to fuck you, just once. That's all. One good hard fuck so I can stop thinking about how amazing it would be to have your cock inside me."
  "This is going to end badly.  You know it is."
  $ title = "What do you do?"
  menu:
    "Fuck her":
      wt_image avon_sex_1
      "Amy finishes taking off her clothes ..."
      wt_image avon_sex_2
      "... then sits down on your coffee table, her legs spread."
      amy.c "Take me right here."
      call amy_event_5_fuck from _call_amy_event_5_fuck
    "Send her away":
      player.c "No, Amy.  That's a boundary that shouldn't be crossed.  You've never cheated on your husband.  You shouldn't start now."
      wt_image avon_sex_1
      amy.c "Please?  Just once?"
      "She continues to strip out of her clothes ..."
      wt_image avon_sex_2
      "... then sits down on your coffee table, legs spread."
      amy.c "Please ... please, fuck me with your hard cock.  I'll make it feel sooo good for you."
      $ title = "What do you do?"
      menu:
        "Tell her no":
          player.c "No Amy.  Get yourself dressed."
          amy.c "But ..."
          player.c "No buts. I'm not going to be responsible for you messing up your marriage. You're a faithful wife. Stay that way."
          wt_image avon_house_5
          amy.c "You're right."
          "She puts her clothes back on."
          wt_image avon_house_2
          amy.c "You're right, I shouldn't mess up my marriage just for one meaningless fling.  No matter how fucking good that fling would feel ..."
          player.c "Amy ..."
          amy.c "Sorry.  Yes, I know.  It's not worth it.  I'll get going."
        "Fuck her":
          "You should say no, but if her pussy feels half as good as it looks, you hate to miss out on the opportunity."
          player.c "Okay Amy.  But just once."
          amy.c "Ohhhh!  Thank you!!"
          call amy_event_5_fuck from _call_amy_event_5_fuck_1
  return

label amy_event_5_fuck:
  wt_image avon_sex_3
  "You lift her up and carry her over to the sofa.  Then you shed your clothes and position your cock at her entrance."
  amy.c "Ohhh yes ... I've been imaging this for so long now.  Do it ... fuck me."
  wt_image avon_sex_4
  "She's soaking wet, giving your cock easy access.  She closes her eyes and moans as you push inside her."
  amy.c "Ooohhhh yeesssss "
  wt_image avon_sex_5
  amy.c "Ohhh yesss! Just like that ... ohhhh that feels soooo goood!!"
  wt_image avon_sex_6
  amy.c "Oooohhhhh .. I'm CUMMMIINNGGGG!!!!!"
  "The announcement isn't really necessary.  The shuddering and bucking of her body on the sofa as she strokes her clit gives you ample notice of her climax."
  wt_image avon_sex_5
  player.c "Take some deep breaths and get yourself under control, Amy.\n\nLet the next one build up more slowly.  Try to hold off until I'm ready."
  amy.c "What ... what do you mean?  ... ohh!!"
  "As the pleasure starts to build up inside her again, she realizes you're holding off on your own orgasm to let her have another."
  wt_image avon_sex_7
  "Despite your suggestion to let the next one build more slowly, Amy quickly races to another orgasm.\n\nAs she climaxes, you let yourself cum in tandem with her."
  amy.c "Ohhhhh YEESSSSS!!!!!!"
  player.c "[player.orgasm_text]"
  wt_image avon_sex_8
  "As Amy gets herself dressed, her mood starts to change.  The dreamy, post-orgasmic bliss fades, and she starts to look distraught."
  amy.c "I can't believe we did that.  I can't believe I'm an adulteress.  It was good - believe me, it was good!  But I shouldn't have done that.  It was wrong."
  "She leaves without saying anything more, a guilty look on her face as she slinks out the door."
  $ amy.sex_count += 1
  $ amy.orgasm_count += 2
  $ amy.event_count = 6
  orgasm notify
  return

# End Day
label amy_end_day:
    pass
    return

# End Week
label amy_end_week:
  ## End Week - Avon Husband Events
  if amy.event_count == 6:
    call amy_event_6 from _call_amy_event_6
  return

# End Week - Avon Husband Events
label amy_event_6:
  $ amy.event_count = 7
  wt_image phone_1
  player.c "Late Saturday night, your phone rings."
  amy_husband "I'm going to kill you, you little fuck."
  player.c "Who is this?"
  amy_husband "The guy whose wife you fucked. She told me all about it. Confessed everything, the guilty little whore. I'll deal with her in a bit. First I'm going to deal with you. You fucked with me, now I'm going to fuck you. Permanently."
  player.c "That must have been Amy's husband."
  $ title = "What do you do?"
  menu menu_amy_event_6_choice:
    "Flee (ends game)":
      wt_image airport_1
      "Better safe than sorry.  You pack just the essentials you need, and head for the airport.  You'll need to start a new life somewhere else.  You've done it before."
      "Reload or restart.  Next time, stick to your plan of sleeping only with women whose husbands approve of them sleeping with you."
      jump end_game
    "Call the police" if not amy.has_tag('event_6_called_police'):
      wt_image police_interview
      "The police take your call and listen to your suspicions about Amy's husband."
      "You can't tell them very much about him, or her.  You never got her last name, and have no idea where she lives.  You're not sure you even received any receipts for things you bought from her, and he called from a blocked line, so you don't have even a phone number to give them."
      "They promise to look into it, but you're pretty sure you're far down their priority list."
      wt_image current_location.image
      add tags 'event_6_called_police' to amy
      jump menu_amy_event_6_choice
    "Call Janice the Lawyer" if player.has_tag('lawyer_on_retainer'):
      wt_image lawyer_desk_1
      player.c "Janice, remember when you warned me about the occupational hazards of jealous husbands?"
      janice.c "Tell me who he is."
      "You tell her what you know, which isn't very much.  You never got her last name, and have no idea where she lives.  You're not sure you even received any receipts for things you bought from her, and he called from a blocked line, so you don't have even a phone number to give her."
      janice.c "Okay, that's not much to go on, but it should be enough.  Leave this with me."
      player.c "What will you do?"
      janice.c "This won't come back to you, that's all you need to know."
      "There's nothing like having a high priced lawyer on retainer to keep you out of trouble"
      wt_image current_location.image
      "You never hear anything more from Amy or her husband.  You hope she's okay.  You know, except for the part where you tore her marriage apart and caused who-knows-what to happen to her husband."
    "Nothing":
      "Threats are easy. He was probably just blowing off some steam. You tell yourself it's nothing to worry about."
      wt_image black_square
      "In the wee hours of that night, you wake up. Did you just hear something?"
      wt_image gun_shot_1
      "The flash from the gun muzzle is blinding.  So is the pain as the bullet strikes you."
      wt_image hospital_1
      "Fortunately, the bullet passes straight through your upper arm without damaging anything critical.  You're not as pretty as you used to be, but if anything, the scar makes you seem even sexier and more dangerous. You do need an ambulance and a night in the hospital, followed by a week of no strenuous activity."
      "Other than the medical bill and the lost time, though, you're otherwise none the worse for wear. Still, in the future, it may be safer to stick to your plan of not sleeping with women without their partner's consent."
      $ week += 1
      change player money by -200 notify
      if player.money < player.min_money:
          $ player.money = player.min_money
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
