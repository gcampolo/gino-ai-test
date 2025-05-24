## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package brenda name "Brenda the Bra Fitter" description "Allows Brenda the Bra Fitter to be a minor character" dependencies core chelsea
register brenda_pregame 15 in core as "Brenda the Bra Fitter"

label brenda_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', 'Brenda the Bra Fitter (Jelena Jensen)')]

    ## Character Definition
    brenda = Person(Character("Brenda", who_color="#BABA5D", what_color="#BABA5D"), "brenda", cut_portrait = True, prefix = "", suffix = "the Bra Fitter")

    # Other Characters
    # N/A

    ## Actions
    brenda.action_contact_brenda = living_room.add_action("Contact " + brenda.full_name, label = brenda.short_name + "_contact", context = "_contact_other", condition = "brenda.can_be_interacted and chelsea.bra_fitting_status == 2")
    # N/A

    ## Tags
    # Common Character Tags
    brenda.add_tags('no_hypnosis', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    brenda.change_status("minor_character")

    # Start Day Events
    # N/A

    ########### VARIABLES ###########
    # Common Character Variables
    # N/A

    # Character Specific Variables
    # N/A
  return

# Display Portrait
# CHARACTER: Display Portrait
label brenda_update_media:
  $ brenda.change_image('chubby_bra_1_4')
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label brenda_examine:
  "Brenda the Bra Fitter"
  #""
  #"[brenda.statblock]"
  #$ items = ", ".join(i.name for i in brenda.get_items()) if brenda.get_items() != [] else ' Nothing'
  #"You have given her: [items]"
  return

# Talk to Character
label brenda_talk:
    "You have nothing to say to her."
    return

## Character Specific Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label brenda_contact:
  wt_image chubby_bra_1_35
  brenda.c "This is Brenda's bra fitting services.  How can I help you?"
  player.c "I'm trying to help my girlfriend.  She has a hard time finding bras that fit her."
  wt_image chubby_bra_1_34
  brenda.c "Is she a large breasted woman?"
  player.c "Yes"
  brenda.c "What cup size does she normally buy?"
  player.c "I'm not sure.  A big one?"
  wt_image chubby_bra_1_3
  brenda.c "I think I can help.  My services cost 300.  For that I'll come to your house, properly measure and size your girlfriend, and provide her with a high quality bra that will show off her attributes to their best effect."
  brenda.c "It will also be completely comfortable, because for the first time in her life she'll have a bra that's exactly right for her body."
  brenda.c "If needed, I'll provide follow up visits to confirm the bra fits and help her adjust it as needed to account for any weight fluctuation she may experience."
  player.c "That's a lot for a bra."
  wt_image chubby_bra_1_34
  brenda.c "It's a service, not a product.  How much money has your girlfriend wasted on bras that aren't comfortable?"
  "You have no idea.  You prefer [chelsea.name] with her tits out, and this is a lot of money to cover them up."
  "On the other hand, it is a service, and you can't help but wonder exactly how Brenda would go about servicing [chelsea.name]'s breasts?"
  $ title = "What do you tell her?"
  menu:
    "I'll pay (costs 300)":
      if player.money - player.min_money >= 300:
        $ chelsea.training_session()
        $ brenda.training_session()
        call forced_movement(bedroom) from _call_forced_movement_998
        summon chelsea
        summon brenda
        wt_image chubby_bra_1_4
        "Brenda arrives later that day. [chelsea.name] and you are both waiting for her."
        brenda.c "No.  No no no.  That'll never do.  Even through your dress I can see that bra is a terrible fit for you.  Get it off."
        wt_image chubby_bra_1_5
        brenda.c "I'm not even sure you're wearing the right cup size?  It certainly isn't the right shape for you."
        wt_image chubby_bra_1_6
        brenda.c "This is what a properly fitted bra looks like. The cups match the natural shape of my breasts and provide support without binding. The straps have been fitted to match the size of my rib cage and hold me in comfortably without being too tight or too loose anywhere. I could wear this bra all day and never even be aware I have it on."
        wt_image chubby_bra_1_7
        brenda.c "Lets get some measurements. First around your rib cage."
        wt_image chubby_bra_1_8
        brenda.c "And also around the widest part of your chest."
        if chelsea.lesbian_status == 1 or chelsea.lesbian_status >= 7:
          wt_image chubby_bra_1_9
          "You've taught [chelsea.name] to recognize and accept when her body responds to another woman, and it seems she's responding to Brenda's touch. She surprises Brenda, and maybe even herself, by leaning in for a kiss."
          brenda.c "Oh!  Naughty."
          chelsea.c "Do you want me to stop?"
          brenda.c "No, but I'm supposed to be getting your breast measurements."
          wt_image chubby_bra_1_10
          chelsea.c "Wouldn't you prefer to do that using your hands?"
          brenda.c "Yes"
          wt_image chubby_bra_1_11
          brenda.c "Wait ...  What about your boyfriend?"
          chelsea.c "Do you want him to join us?"
          brenda.c "No!!  I don't like to be touched by men."
          wt_image chubby_bra_1_10
          chelsea.c "Can he watch?"
          brenda.c "I ... I suppose so."
          wt_image chubby_bra_1_30
          chelsea.c "I don't think you've got a good enough impression of the shape and size of my breasts, yet.  Perhaps you should explore them some more, while I check out yours?"
          wt_image chubby_bra_1_16
          "The two women lick and suckle each others breasts until the excitement becomes too much for [chelsea.name], and she tells Brenda she wants more."
          wt_image chubby_bra_1_17
          "The dark-haired woman hesitates, looking over at you."
          wt_image chubby_bra_1_18
          chelsea.c "Don't worry about him.  Come here and fuck me."
          wt_image chubby_bra_1_19
          "Brenda does, scissoring her legs around [chelsea.name]'s ..."
          wt_image chubby_bra_1_20
          "... then grinding her pussy back and forth against your girlfriend's until they both explode."
          chelsea.c "Aahhhhhh"
          brenda.c "Oooooooohh"
          wt_image chubby_bra_1_37
          "After they both recover, a sheepish looking Brenda takes a few measurements, then beats a hasty retreat, promising to send [chelsea.name] a perfectly comfortable bra customized to her exact shape."
          wt_image chubby_bra_1_21
          chelsea.c "I think I embarrassed her."
          "You think [chelsea.name] fulfilled a fantasy Brenda's been having about every woman she's every fitted.  Having your fantasy fulfilled unexpectedly can often be embarrassing, especially when there's someone else there to witness it."
        else:
          wt_image chubby_bra_1_36
          brenda.c "Now we need to assess the shape of your breasts.  I've brought a variety of different cup shapes.  Try this one first."
          wt_image chubby_bra_1_12
          brenda.c "It'll be a little small.  Your boyfriend didn't know what cup size you were, and when that happens I err on the side of bringing smaller sample sizes. I wouldn't want to embarrass the client by leaving the impression her chest is undersized. I see I didn't need to worry about that with you, though. You have lovely, large breasts."
          if chelsea.lesbian_status >= 4:
            wt_image chubby_bra_1_14
            "Brenda gets a good feel of those lovely, large breasts, kneading and squeezing them more than is strictly necessary to size them. [chelsea.name] leans back into Brenda, her body responding to the stimulation the other woman is providing to her chest. Unfortunately, she's not quite ready to accept those sensations, and the moment passes"
          else:
            wt_image chubby_bra_1_13
            "Brenda gets a good feel of those lovely, large breasts. If [chelsea.name] is aware that Brenda is kneading and squeezing her tits more than is strictly necessary to size them, she's too shocked or confused to say anything."
          brenda.c "That's going to work.  The shape matches your breasts perfectly.  Once I adjust the cup size, this'll be just right for you."
          wt_image chubby_bra_1_36
          brenda.c "That's everything I need for now. I'll get a customized bra prepared for you that will fit you perfectly."
          if chelsea.has_tag('bbw'):
            brenda.c "Once we have it, if you need me to come over and fit it, just let me know. Sometimes as our weight fluctuates, the straps on our bras need to be adjusted. No offense, but that's particularly true for larger women like yourself."
          else:
            brenda.c "Once we have it, if you need me to come over and fit it, just let me know. Sometimes as our weight fluctuates, the straps on our bras need to be adjusted. No offense, but even though I see you're keeping yourself in great shape, I can tell you probably need to work at it to keep the weight off."
          wt_image chubby_bra_1_15
          brenda.c "Depending on your exact weight each week, I may need to make small adjustments to keep the bra fitting comfortably.  But don't worry, I don't mind.  Once I show you how a couple of times, you'll be able to make those adjustments yourself as needed."
          "Brenda takes one more long, lingering look at your girlfriend's chest before departing."
          if not chelsea.lesbian_status >= 2:
            "[chelsea.name] had to be aware of, but chose to ignore, Brenda's obvious attraction to her. If you're interested in encouraging [chelsea.name] to act on those opportunities, you should discuss her feelings about women with her."
            $ chelsea.lesbian_status = 1
          else:
            "[chelsea.name] didn't get much out of this first visit from Brenda. She was a little too surprised by the situation to let herself react to Brenda's obvious attraction to her. Inviting Brenda over again to adjust the fitting of the new bra, however, may help accustom [chelsea.name] to the idea that she can enjoy the attention of women."
        $ chelsea.bra_fitting_status = 4
        change player money by -300
        change player energy by -energy_short notify
        call character_location_return(chelsea) from _call_character_location_return_728
        call character_location_return(brenda) from _call_character_location_return_729
        call forced_movement(living_room) from _call_forced_movement_999
      else:
        sys "You don't have enough money to pay Brenda right now. You could get back to her when you do."
    "I'll think about it":
      pass
    "Never":
      wt_image chubby_bra_1_35
      "That's too much money to spend to watch [chelsea.name] get felt up. You let Brenda know her services aren't required after all."
      $ chelsea.bra_fitting_status = 3
  wt_image current_location.image
  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_brenda:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_brenda:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_brenda:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_brenda:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_brenda:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_brenda:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_brenda:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_brenda:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_brenda:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_brenda:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_brenda:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
#label brenda_start_day:
  #return

# End Day
label brenda_end_day:
    pass
    return

# End Week
label brenda_end_week:
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
