## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: who did the original conversion???

# Package Register
register kitty_pregame 10 in core as "Kitty the Pet Store Clerk"

# Pregame
label kitty_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Kitty the Pet Store Clerk (Lexi Belle)")]

    ## Character Definition
    # 255,128,192
    kitty = Person(Character("Pet Store Clerk", who_color="#FF80C0", what_color="#FF80C0"), "kitty", cut_portrait = True, prefix = "", suffix = "")

    # Other Characters
    # N/A

    ## Actions
    kitty.action_talk = kitty.add_action("Talk to her", label="_talk", condition = "kitty.can_be_interacted and kitty.has_tag('first_talk') and current_location == pet_store")
    kitty.action_ask_name = kitty.add_action("Ask her for her name", label="_ask_name", condition = "kitty.can_be_interacted and not kitty.has_tag('first_talk') and kitty.has_tag('ask_name') and current_location == pet_store")
    kitty.action_ask_date = kitty.add_action("Ask her on a date", label="_ask_date", condition = "kitty.can_be_interacted and not kitty.has_tag('first_talk') and not kitty.has_tag('ask_name') and not kitty.has_tag('date_talk_closed') and current_location == pet_store")
    kitty.action_ask_help = kitty.add_action("Ask her for help", label="_ask_help", condition = "kitty.can_be_interacted and not kitty.has_tag('first_talk') and current_location == pet_store")

    ## Tags
    # Common Character Tags
    kitty.add_tags('no_hypnosis', 'first_talk', 'ask_name', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    kitty.location = pet_store

    ## Other
    kitty.change_status("minor_character")

    # Start Day Events
    #start_day_labels.append('kitty_start_day') # not needed as no content

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    kitty.add_stats_with_value('pet_disclosed', 'top_shelf_status')
  return

# Initial Contact Message
# OBJECT: Check Messages
#label kitty_message: # not needed
#    return

# Character Rejected
#label kitty_rejected: # not needed
#    sys "You may no longer accept this assignment."
#    return

# Display Portrait
# CHARACTER: Display Portrait
label kitty_update_media:
    if current_location == pet_store:
        $ kitty.change_image('pet_clerk_store_1')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label kitty_examine:
    if current_location == pet_store:
        "A young blonde lady wearing a company t-shirt waits on the customers."
    return

# Talk to Character
label kitty_talk:
    # initial conversation only at pet store
    wt_image pet_clerk_store_3
    kitty.c "Hi.  Can I help you?"
    rem tags 'first_talk' from kitty
    return

## Character Specific Actions
# Ask Her for Her Name
label kitty_ask_name:
    # only active at pet_store
    player.c "What's your name?"
    wt_image pet_clerk_store_3
    kitty.c "Kitty. Yes, I know. My name is Kitty and I work at a pet store. I guess this was my destiny!"
    wt_image pet_clerk_store_2
    "She laughs."
    kitty.c "We're pretty busy. Is there anything I can do for you?"
    $ kitty.change_full_name("", "Kitty", "the Pet Store Clerk")
    rem tags 'ask_name' from kitty
    return

# Ask Her for a Date
label kitty_ask_date:
    # only active at pet_store
    wt_image pet_clerk_store_3
    player.c "Kitty, would you like to go on a date with me?"
    if player.has_tag('supersexy'):
        wt_image pet_clerk_store_4
        kitty.c "A date?  But we don't even know each other.  I mean, do we even have anything in common?"
        "If that's her attempt to play hard to get, it's a feeble one, as her stiffening nipples betray her excitement at you showing an interest in her."
    elif player.has_tag('wealthy'):
        wt_image pet_clerk_store_4
        kitty.c "A date?  But we don't even know each other.  I'm just a clerk at a pet store and you look like you could own the store.  I mean, do we even have anything in common?"
        "She looks like a stray cat who's been offered a bowl of milk by a stranger, her face showing equal parts interest and distrust."
    elif player.has_tag('dominant'):
        wt_image pet_clerk_store_5
        kitty.c "A date?  But we don't even know each other.  I mean, do we even have anything in common?"
        "She's showing about the same enthusiasm to your suggestion as a housecat shows to the prospect of a bath.  It seems this Kitty isn't looking for a collar."
    elif player.has_tag('hypnotist'):
        wt_image pet_clerk_store_5
        kitty.c "A date?  But we don't even know each other.  I mean, do we even have anything in common?"
        "She's showing about the same enthusiasm to your suggestion as a housecat shows to the prospect of a bath.  And with other people in the store, there's no immediate opportunity to try and change her mind."
    else:
        wt_image pet_clerk_store_5
        kitty.c "A date?  But we don't even know each other.  I mean, do we even have anything in common?"
        "She's showing about the same enthusiasm to your suggestion as a housecat shows to the prospect of a bath."
    $ title = "What do you have in common?"
    menu menu_kitty_date_1:
        "I have a pet, you look like a pet" if player.petgirl_count > 0:
            wt_image pet_clerk_store_3
            kitty.c "What is that supposed to mean?"
            if player.has_tag('supersexy'):
                player.c "It's a term of endearment.  It means you're really cute."
                wt_image pet_clerk_store_7
                kitty.c "You think I'm cute?"
                player.c "Very much so."
                wt_image pet_clerk_store_4
                kitty.c "That's sweet.  But we should probably have something beyond physical attraction between us.  I mean, shouldn't we?"
                jump menu_kitty_date_1
            elif player.has_tag('dominant'):
                player.c "It means I've been fortunate enough to have had the opportunity to dominate many women, and you'd look as nice in a collar as any of them.  I think we'd both enjoy exploring whether you'd like to become my pet."
                wt_image pet_clerk_store_5
                kitty.c "Ewwww.  No thank you.  I work in a pet store because I love animals, not because I want to be treated like one."
                add tags 'date_talk_closed' to kitty
            else:
                player.c "It's a term of endearment.  It means you're really cute."
                wt_image pet_clerk_store_5
                kitty.c "It doesn't sound like a term of endearment.  It sounds creepy."
                jump menu_kitty_date_1
        "We both love animals" if player.petgirl_count > 0:
            if player.has_tag('supersexy') or player.has_tag('wealthy'):
                wt_image pet_clerk_store_2
                if kitty.pet_disclosed == 2:
                    kitty.c "Oh that's right!  You have a pet.  I'd love to meet her."
                else:
                    kitty.c "You're an animal lover?  Do you have a pet?  What kind?"
                    player.c "I do.  She's a larger pet."
                    wt_image pet_clerk_store_3
                    kitty.c "Like a dog?  Neat.  I bet she's really happy you're giving her a good home.  I'd love to meet her."
                player.c "Maybe not on the first date."
                wt_image pet_clerk_store_7
                kitty.c "That's smart!  Having people come and go can be confusing for pets.  It makes sense you wouldn't want to introduce someone until you knew it was serious."
                wt_image pet_clerk_store_2
                kitty.c "You're a really thoughtful owner."
                player.c "I try to be.  Maybe we could talk pet care tips at a restaurant?"
                wt_image pet_clerk_store_3
                kitty.c "Okay!"
                add tags 'date_talk_closed' to kitty
                sys "Unfortunately, there's no more content to explore here yet.  You'll need to wait for a newer version of the game for your date."
            else:
                wt_image pet_clerk_store_5
                kitty.c "Well, yeah.  Everybody who comes in here loves animals.  It's a pet shop."
                jump menu_kitty_date_1
        "I like food, do you like food?":
            if player.has_tag('supersexy') or player.has_tag('wealthy'):
                wt_image pet_clerk_store_2
                "She laughs."
                kitty.c "Well, yeah.  Doesn't everybody?"
                player.c "Most people, in my experience.  Lots of them like to eat food at restaurants.  Do you like restaurants?"
                wt_image pet_clerk_store_3
                kitty.c "I suppose.  Some of them are quite nice."
                player.c "Could I take you to one of the nice ones?  Possibly one that has food?"
                wt_image pet_clerk_store_4
                kitty.c "Shouldn't we have something in common other than liking food?"
                player.c "Maybe we do?  How about I take you out to one of those nice restaurants with food and we can talk and figure out if we have anything in common?"
                wt_image pet_clerk_store_7
                kitty.c "Okay!"
                add tags 'date_talk_closed' to kitty
                sys "Unfortunately, there's no more content to explore here yet. You'll need to wait for a newer version of the game for your date."
            else:
                wt_image pet_clerk_store_5
                kitty.c "Seriously?"
                jump menu_kitty_date_1
        "I'll get back to you":
            sys "Don't bother.  There's no date content in this version of the game anyway."
            if not player.has_tag('supersexy') and not player.has_tag('wealthy'):
                extend " You'll need to wait for a newer version of the game to see if you can overcome her complete ambivalence to you."
    return

# Ask Her for Help
label kitty_ask_help:
  player.c "Could you help me with something?"
  wt_image pet_clerk_store_6
  kitty.c "Sure.  What do you need help with?"
  $ title = "What do you want help with?"
  menu:
    "Water bowl":
      player.c "Can you help me with the water bowls?"
      if kitty.pet_disclosed == 0:
        kitty.c "Sure.  What type of pet do you have?"
        if player.petgirl_count > 0:
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes.  A good size one.  About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat.  I bet she's really happy you're giving her a good home. One of these larger bowls would likely be best for her."
          wt_image pet_clerk_store_3
          kitty.c "We have a variety of patterns, so you can pick one that fits your decor, if you're into that.  Or just grab a stainless steel one. You can't go wrong with that. It'll last forever."
          $ kitty.pet_disclosed = 2
        else:
          player.c "I don't have a pet, but I'm thinking about getting one."
          wt_image pet_clerk_store_7
          kitty.c "Oh, that's great! You should definitely do that. Pets really make a home feel like a home."
          wt_image pet_clerk_store_3
          kitty.c "Well, you'll definitely need a water bowl, but you should get one that's the right size for your pet.  Until you pick out your pet, I don't think there's much point in looking at water bowls."
          $ kitty.pet_disclosed = 1
      elif kitty.pet_disclosed == 1:
        kitty.c "You said you didn't have a pet, right?  What do you need with a water bowl?"
        if player.petgirl_count > 0:
          player.c "I have a pet now."
          kitty.c "You do?  That's great!  What type of animal is it?"
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes.  A good size one.  About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat.  I bet she's really happy you're giving her a good home.  One of these larger bowls would likely be best for her."
          wt_image pet_clerk_store_3
          kitty.c "We have a variety of patterns, so you can pick one that fits your decor, if you're into that.  Or just grab a stainless steel one.  You can't go wrong with that.  It'll last forever."
          $ kitty.pet_disclosed = 2
        else:
          player.c "I'm thinking about getting a pet."
          wt_image pet_clerk_store_7
          kitty.c "Oh, that's great!  You should definitely do that.  Pets really make a home feel like a home."
          wt_image pet_clerk_store_3
          kitty.c "Well, you'll definitely need a water bowl, but you should get one that's the right size for your pet.  Until you pick out your pet, I don't think there's much point in looking at water bowls."
      elif kitty.pet_disclosed == 2:
        wt_image pet_clerk_store_7
        kitty.c "Sure.  You said your pet was pretty big, right?  One of these larger bowls would likely be best for her."
        wt_image pet_clerk_store_3
        kitty.c "We have a variety of patterns, so you can pick one that fits your decor, if you're into that.  Or just grab a stainless steel one.  You can't go wrong with that.  It'll last forever."
    "Fetch toys":
      player.c "Can you help me with the pet toys?"
      if kitty.pet_disclosed == 0:
        kitty.c "Sure. What type of pet do you have?"
        if player.petgirl_count > 0:
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes.  A good size one.  About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat.  I bet she's really happy you're giving her a good home.  Do you play with her at the park?"
          player.c "Not often.  I usually play with her at home."
          wt_image pet_clerk_store_3
          kitty.c "Okay.  Well, I hope you make sure she's getting a lot of exercise.  If she doesn't get lots of walks and playtime, she could get overweight and unhealthy."
          wt_image pet_clerk_store_9
          kitty.c "Since you want something for around the house, one of these might be suitable.  This soft toy can be thrown and fetched without breaking anything in your house."
          wt_image pet_clerk_store_6
          kitty.c "Or maybe this tug-of-war toy?  She might like trying to pull that away from you and you would both be getting exercise."
          player.c "Thanks.  I'll think about it."
          $ kitty.pet_disclosed = 2
        else:
          player.c "I don't have a pet."
          kitty.c "Then what do you need with a pet toy?"
          player.c "I'm thinking about getting it as a gift for a friend."
          wt_image pet_clerk_store_7
          kitty.c "How thoughtful! Pet toys make a wonderful gift."
          wt_image pet_clerk_store_9
          kitty.c "So, obviously you need to know what type of pet your friend has.  The cat toys are here.  We've also got dog toys in this section."
          wt_image pet_clerk_store_7
          kitty.c "As long as you get the right type of toy for the type of pet it is, you can't go wrong.  Everything in our store has been selected to be safe and fun for the animal.  Why don't you take a look through and pick out something that looks like a suitable gift to you?"
          $ kitty.pet_disclosed = 1
      elif kitty.pet_disclosed == 1:
        kitty.c "You said you didn't have a pet, right?  What do you need with a pet toy?"
        if player.petgirl_count > 0:
          player.c "I have a pet now."
          kitty.c "You do? That's great! What type of animal is it?"
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes. A good size one. About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat.  I bet she's really happy you're giving her a good home.  Do you play with her at the park?"
          player.c "Not often.  I usually play with her at home."
          wt_image pet_clerk_store_3
          kitty.c "Okay.  Well, I hope you make sure she's getting a lot of exercise.  If she doesn't get lots of walks and playtime, she could get overweight and unhealthy."
          wt_image pet_clerk_store_9
          kitty.c "Since you want something for around the house, one of these might be suitable.  This soft toy can be thrown and fetched without breaking anything in your house."
          wt_image pet_clerk_store_6
          kitty.c "Or maybe this tug-of-war toy?  She might like trying to pull that away from you and you would both be getting exercise."
          player.c "Thanks.  I'll think about it."
          $ kitty.pet_disclosed = 2
        else:
          player.c "I'm thinking about getting it as a gift for a friend."
          wt_image pet_clerk_store_7
          kitty.c "How thoughtful!   Pet toys make a wonderful gift."
          wt_image pet_clerk_store_9
          kitty.c "So, obviously you need to know what type of pet your friend has.  The cat toys are here.  We've also got dog toys in this section."
          wt_image pet_clerk_store_7
          kitty.c "As long as you get the right type of toy for the type of pet it is, you can't go wrong.  Everything in our store has been selected to be safe and fun for the animal.  Why don't you take a look through and pick out something that looks like a suitable gift to you?"
      elif kitty.pet_disclosed == 2:
        kitty.c "Sure.  You said your pet was a big girl, right?  Do you play with her at the park?"
        player.c "Not often.  I usually play with her at home."
        wt_image pet_clerk_store_3
        kitty.c "Okay.  Well, I hope you make sure she's getting a lot of exercise.  If she doesn't get lots of walks and playtime, she could get overweight and unhealthy."
        wt_image pet_clerk_store_9
        kitty.c "Since you want something for around the house, one of these might be suitable.  This soft toy can be thrown and fetched without breaking anything in your house."
        wt_image pet_clerk_store_6
        kitty.c "Or maybe this tug-of-war toy?  She might like trying to pull that away from you and you would both be getting exercise."
        player.c "Thanks.  I'll think about it."
    "Collar and leash":
      player.c "Can you help me pick out a collar and leash?"
      if kitty.pet_disclosed == 0:
        kitty.c "Sure. What type of pet do you have?"
        if player.petgirl_count > 0:
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes.  A good size one.  About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat.  I bet she's really happy you're giving her a good home.  Do you know how big around her neck is?"
          player.c "About the same as yours, I'd say."
          wt_image pet_clerk_store_9
          kitty.c "Okay, so not that big.  Not like a Great Dane or a Saint Bernard.  You don't need an extra large."
          wt_image pet_clerk_store_7
          kitty.c "One of this size, a large dog collar, should be just about perfect."
          player.c "Have you tried it to check?"
          wt_image pet_clerk_store_2
          "She laughs."
          kitty.c "No, I don't normally go around trying on dog collars.  But yes, it would fit me.  I can tell from the sizing. So it should fit your girl, too."
          $ kitty.pet_disclosed = 2
        elif lee.has_tag('need_leash'):
          player.c "A big one.  About my size."
          wt_image pet_clerk_store_9
          kitty.c "That is a big dog.  We have one over here that should fit him, though."
        else:
          player.c "I don't have a pet."
          kitty.c "Then what do you need with a collar and leash?"
          player.c "I'm thinking about getting it as a gift for a friend."
          wt_image pet_clerk_store_8
          kitty.c "Really?  I don't think a collar and leash would make a very nice gift.  Most people only need one collar for their pet, and they usually get it at the same time they get the pet."
          player.c "If you were a pet, wouldn't you want to have more than one collar?"
          wt_image pet_clerk_store_6
          "She laughs."
          kitty.c "Ummm.  I'm not really sure how to answer that."
          wt_image pet_clerk_store_9
          kitty.c "What about a toy instead?  We have a great selection of toys for all types of animals.  And a pet can never have too many toys."
          $ kitty.pet_disclosed = 1
      elif kitty.pet_disclosed == 1:
        kitty.c "You said you didn't have a pet, right?  What do you need with a collar and leash?"
        if player.petgirl_count > 0:
          player.c "I have a pet now."
          kitty.c "You do? That's great! What type of animal is it?"
          player.c "She's a larger pet."
          kitty.c "Like a dog?"
          player.c "Yes. A good size one. About your size, actually."
          wt_image pet_clerk_store_7
          kitty.c "Neat. I bet she's really happy you're giving her a good home. Do you know how big around her neck is?"
          player.c "About the same as yours, I'd say."
          wt_image pet_clerk_store_9
          kitty.c "Okay, so not that big. Not like a Great Dane or a Saint Bernard. You don't need an extra large."
          wt_image pet_clerk_store_7
          kitty.c "One of this size, a large dog collar, should be just about perfect."
          player.c "Have you tried it to check?"
          wt_image pet_clerk_store_2
          "She laughs."
          kitty.c "No, I don't normally go around trying on dog collars.  But yes, it would fit me.  I can tell from the sizing. So it should fit your girl, too."
          $ kitty.pet_disclosed = 2
        elif lee.has_tag('need_leash'):
          player.c "It's for my friend.  She just got a pet.  A big one, about my size."
          wt_image pet_clerk_store_9
          kitty.c "That is a big dog.  We have one over here that should fit him, though."
        else:
          player.c "I'm thinking about getting it as a gift for a friend."
          wt_image pet_clerk_store_8
          kitty.c "Really?  I don't think a collar and leash would make a very nice gift.  Most people only need one collar for their pet, and they usually get it at the same time they get the pet."
          player.c "If you were a pet, wouldn't you want to have more than one collar?"
          wt_image pet_clerk_store_6
          "She laughs."
          kitty.c "Ummm.  I'm not really sure how to answer that."
          wt_image pet_clerk_store_9
          kitty.c "What about a toy instead?  We have a great selection of toys for all types of animals.  And a pet can never have too many toys."
      elif kitty.pet_disclosed == 2:
        kitty.c "Sure.  You said your pet was a big girl, right?  Do you know how big around her neck is?"
        player.c "About the same as yours, I'd say."
        wt_image pet_clerk_store_9
        kitty.c "Okay, so not that big.  Not like a Great Dane or a Saint Bernard.  You don't need an extra large."
        wt_image pet_clerk_store_7
        kitty.c "One of this size, a large dog collar, should be just about perfect."
        player.c "Have you tried it to check?"
        wt_image pet_clerk_store_2
        "She laughs."
        kitty.c "No, I don't normally go around trying on dog collars. But yes, it would fit me. I can tell from the sizing. So it should fit your girl, too."
    "Something on the top shelf" if not kitty.has_tag('top_shelf_today'):
      if kitty.top_shelf_status == 0:
        player.c "What's that on the top shelf there?"
        kitty.c "In those bottles? That's a special type of pet shampoo. It really helps their coats stay nice and glossy."
        kitty.c "Did you want me to get one down for you?"
      elif kitty.top_shelf_status == 1:
        player.c "Could I get another bottle of that shampoo?"
        kitty.c "Did you go through the last bottle that quickly? You probably shouldn't be washing an animal that often. This shampoo is amazing, but you don't want to be taking out too many of their natural oils."
        kitty.c "But if you do want another bottle, I can get one down for you."
      elif kitty.top_shelf_status == 2:
        player.c "Could I get another look at that bottle of shampoo?"
        kitty.c "Sure. I'll need to go get the ladder again."
      else:
        wt_image pet_clerk_store_8
        if kitty.top_shelf_status == 3:
          player.c "Could I get another look at that bottle of shampoo?"
          kitty.c "Really? Haven't you looked at it enough? It hasn't changed."
        elif kitty.top_shelf_status == 4:
          player.c "Could I get another look at that bottle of shampoo?"
          kitty.c "No. It's obvious you're not going to buy it. I've got a store full of paying customers to look after. I don't have time to keep running up and down a ladder for you."
      $ title = "What do you say?"
      menu:
        "Please get it for me":
          if kitty.top_shelf_status == 4:
            kitty.c "Not unless you pay me for it first. That'll be 25."
            $ title = "Buy It?"
            menu:
              "Pay 25":
                call kitty_ask_help_buy from _call_kitty_ask_help_buy
              "Never mind":
                pass
          else:
            wt_image pet_clerk_store_9
            if kitty.top_shelf_status < 2:
              kitty.c "Okay. Let me go get a ladder."
            else:
              kitty.c "You're making me get my exercise, you know that?"
            wt_image pet_clerk_store_10
            "She brings out the ladder and climbs up to the top shelf."
            wt_image pet_clerk_store_11
            "Even with the ladder, she has to stretch to reach it..."
            wt_image pet_clerk_store_12
            "... providing you with a view of [kitty.full_name]'s panties-covered ... kitty."
            wt_image pet_clerk_store_13
            "Gallantly, you help her back down."
            wt_image pet_clerk_store_14
            "She hands the bottle over to you for your inspection."
            kitty.c "So what do you think? Did you want to buy it? It's great stuff, and only costs 25."
            $ title = "Buy It?"
            menu:
              "Pay 25":
                call kitty_ask_help_buy from _call_kitty_ask_help_buy_1
              "Not today":
                call kitty_ask_help_not_today from _call_kitty_ask_help_not_today
          add tags 'top_shelf_today' to kitty
        "Never mind":
          pass
    "Never mind":
      player.c "Never mind, I'm okay."
      kitty.c "Okay."
  return

label kitty_ask_help_buy:
  if player.money - player.min_money >= 25:
    if kitty.top_shelf_status == 4:
      wt_image pet_clerk_store_2
      kitty.c "Great!"
      "She pulls a bottle out from behind the counter and smirks at you."
      kitty.c "I had this one tucked away, just for you."
    else:
      wt_image pet_clerk_store_15
      kitty.c "Great!"
      "She rings your order through."
      kitty.c "Thanks for shopping with us. Hope we see you back here again soon. Bye!"
    sys "No doubt the shampoo is as amazing as she says, but there's no use for it in the game - at least at this point - so you avoid cluttering up your inventory by selling it second hand, recouping your 25."
    $ kitty.top_shelf_status = 1
  else:
    "You don't have enough money."
    if kitty.top_shelf_status == 4:
      pass
    else:
      call kitty_ask_help_not_today from _call_kitty_ask_help_not_today_1
  return

label kitty_ask_help_not_today:
  player.c "Not today. Perhaps another time."
  if kitty.top_shelf_status < 2:
    kitty.c "No problem!"
    $ kitty.top_shelf_status = 2
  else:
    $ kitty.top_shelf_status += 1
    if kitty.top_shelf_status == 3:
      kitty.c "Oh. When you asked to see it again, I thought for sure you'd want to buy it this time."
    else:
      $ kitty.top_shelf_status = 4
      wt_image pet_clerk_store_16
      kitty.c "Really? You make me go through all that trouble again and you still don't want to buy it? Fine. Hand it back and I'll restock it later."
  return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
#label kitty_contact: # not needed yet
#    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_kitty:
  "That's just a really difficult topic to bring up with her while she's working."
  return

# Give Chastity Belt
label give_cb_kitty:
  "She's not ready. Seriously, this is way too soon."
  return

# Give Dildo
label give_di_kitty:
  "That might be a nice thought in other circumstances, but not these circumstances."
  return

# Use Fetch Toy
label use_ft_kitty:
    if kitty.has_tag('asked_name'):
        "You shouldn't try to play fetch with someone who isn't your pet. Besides, her name is Kitty. What are the odds she'd fetch even if she was your pet?"
    else:
        "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_kitty:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_kitty:
    if kitty.has_tag('asked_name'):
        "You shouldn't try to take someone for a walk who isn't your pet. Besides, her name is Kitty. What are the odds she'll let you walk her even if she was your pet?"
    else:
        "She sells leashes, there's nothing to suggest she wants to wear one."
    return

# Give Lingerie
label give_li_kitty:
  "You won't accomplish anything by giving her lingerie."
  return

# Give Love Potion
label give_lp_kitty:
  "She's not thirsty."
  return

# Give Transformation Potion
label give_tp_kitty:
  "She's not thirsty."
  return

# Use Water Bowl
label use_wb_kitty:
    if kitty.has_tag('asked_name'):
        "Kitty isn't thirsty right now."
    else:
        "She sells water bowls, she's not looking to drink out of one."
    return

# Use Will Tamer
label use_wt_kitty:
    if kitty.has_tag('asked_name'):
        "Kitty's not ready to wear your collar."
    else:
        "As a pet store clerk, she's familiar with collars, but she's not ready to wear yours."
    return

########### TIMERS ###########
## Common Timers
# Start Day
# N/A

# End Day
label kitty_end_day:
  rem tags 'top_shelf_today' from kitty
  return

# End Week
label kitty_end_week:
    pass
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
