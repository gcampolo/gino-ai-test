## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
register taylor_pregame 10 in core as  "Taylor the Coffee Girl"

# Pregame
label taylor_pregame:
  python:
  ## Constants
    model_credits += [('support', "Taylor the Coffee Girl (Ashley Stone)")]

    ## Character Definition
    # Red
    taylor = Person(Character("Taylor", who_color="#FF0000", what_color="#FF0000", window_background=gui.dialogue_background_medium_font_color), "taylor", cut_portrait = True, prefix = "", suffix = "the Coffee Girl")

    ## Actions
    taylor.action_talk = taylor.add_action("Talk to her", label="_talk", condition = "taylor.can_be_interacted")

    taylor.action_contact = living_room.add_action("Contact Taylor the Coffee Girl", label = taylor.short_name + "_contact", context = "_contact_other", condition = "taylor.can_be_interacted and (taylor.conversation_event == 6 or taylor.conversation_event == 9)")

    ## Tags
    # Common Character Tags
    taylor.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    # Coffee Shop
    # handled in 01-core.rpy

    ## Other

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    # start_day_labels.append('taylor_start_day', priority = 5) # priority 5 is the normal priority so didn't need to be specified # not needed
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables

    # Character Specific Variables
    taylor.add_stats_with_value('conversation_event', 'lose_date', 'week')
    # taylor.conversation_event hey: 0: first coffee, 1: second coffee, 2: holding until ask for date, 3: holding after ask for date if she's not interested, 4:domination conversation, 5:playboy conversation, 6: waiting for you to ask her on date, 7: follow up dom talk if not interested
    # 8: follow up dom talk if interested, 9: positive first date, 10: lost due to not asking her out, 11: conversations over, 12: moneybags conversation

  return

# Initial Contact Message
# OBJECT: Check Messages

# Display Portrait
# CHARACTER: Display Portrait
label taylor_update_media:
    if current_location == coffee_shop:
        $ taylor.change_image('new_barista_coffee_2')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label taylor_examine:
    "A perky, enthusiastic coffee girl."
    return

# Talk to Character
label taylor_talk:
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
                $ title = "Pay 10 to regain 10 Energy?"
                menu:
                    "Pay up (costs 10)":
                        if not player.has_tag('coffee_already_today') and week > taylor.week:
                            add tags 'coffee_already_today' to player
                            call taylor_conversation from _call_taylor_conversation
                        else:
                            wt_image new_barista_coffee_1
                            "Taylor smiles at you as you get another coffee, but doesn't have time to chat."
                        change player energy by 10
                        change player money by -10 notify
                    "No":
                        pass
    else:
        "You have nothing to say to her here."
    return

label taylor_conversation:
  # first meeting with Taylor
  if taylor.conversation_event == 0:
    wt_image new_barista_coffee_1
    "There's a new barista working at the coffee shop today.  Her name tag says her name is 'Taylor'.  She's a little slow getting your drink ready, and you'd guess this is her first week on the job."
    "She smiles at you as she hands over your coffee, then turns immediately to try to deal with the client line up that is backing up as she tries to get through all the orders."
    $ taylor.week = week # note: this makes sure a week passes before next conversation takes place
    $ taylor.conversation_event += 1
  # second meeting, she says hello
  elif taylor.conversation_event == 1:
    wt_image new_barista_coffee_1
    "Taylor's still getting the hang of the coffee pouring, but she's a little quicker than she was the last time you were here."
    taylor.c "I've seen you here before.  You must be a regular."
    "Before you can reply, she moves on to prepare the next order."
    $ taylor.week = week # note: this makes sure a week passes before next conversation takes place
    $ taylor.conversation_event += 1
  # meetings until ask on date
  elif taylor.conversation_event == 2:
    wt_image new_barista_coffee_1
    "Taylor's keeping the orders moving like a veteran now."
    taylor.c "Hi!"
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        pass
      "Ask if she's a lesbian" if samantha.has_tag('revealed_lesbian') and not taylor.has_tag('discussed_lesbian'):
        call taylor_lesbian from _call_taylor_lesbian
      "Ask if she'd like career counseling" if not taylor.has_tag('discussed_career'):
        call taylor_career from _call_taylor_career
      "Ask if she's bi curious" if taylor.has_tag('discussed_lesbian') and not taylor.has_tag('discussed_bi_curious'):
        call taylor_bi from _call_taylor_bi
      "Ask her on a date":
        call taylor_date from _call_taylor_date
      "After today, look for a new barista (Stop going to Taylor)":
        call taylor_look_for_new_barista from _call_taylor_look_for_new_barista
  # meetings after ask on a date if she's not interested
  elif taylor.conversation_event == 3:
    wt_image new_barista_coffee_1
    "Taylor smiles as she hands over your coffee."
    taylor.c "Hi!"
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        pass
      "Ask if she's a lesbian" if samantha.has_tag('revealed_lesbian') and not taylor.has_tag('discussed_lesbian'):
        call taylor_lesbian from _call_taylor_lesbian_1
      "Ask if she's bi curious" if not taylor.has_tag('discussed_bi_curious'):
        call taylor_bi from _call_taylor_bi_1
      "Ask if she'd like career counseling" if not taylor.has_tag('discussed_career'):
        call taylor_career from _call_taylor_career_1
      "After today, look for a new barista (Stop going to Taylor)":
        call taylor_look_for_new_barista from _call_taylor_look_for_new_barista_1
  # meeting after asking for date if you dominated her
  elif taylor.conversation_event == 4:
    wt_image new_barista_coffee_2
    taylor.c "Hi. So, I thought about what you said the last time.  And you're right.  Just because I'm never going to marry you, doesn't mean I shouldn't consider going out on a date with you."
    taylor.c "And even though I am better looking than you, you're kind of sexy in your own, confident way."
    taylor.c "But tell me honestly.  What are you looking for?  Do you want to hang out with a younger woman to make you feel younger?  Are you just trying to get me in the sack?  What is it you're looking for?"
    $ title = "How do you respond?"
    menu:
      "Talk about BDSM":
        player.c "I'd like to spend some time with you to get to know you better. I'd like to know more about what makes you tick. I'm a good connector, and sometimes I help connect people who share a common interest."
        player.c "Like most of the men and many of the women who come in here, I wonder about what you look like naked, and I hope our date will be the first step to finding that out."
        player.c "Unlike most of those other people, my sexual interests aren't exclusively about sex itself. I'm a Dom. I enjoy receiving power and control from other people and having them obey me."
        player.c "If they don't obey, I punish them. If they do obey, sometimes I punish them anyway, but in a different manner. One that I enjoy much more. Ideally they receive some satisfaction from the punishment, or at least from the experience of pleasing me."
        player.c "I have no idea if that appeals to you, but I hope to use our date to find out."
        taylor.c "Wow.  So when you said you've taken other girls over your lap before, you really meant it."
        player.c "Yes"
        "She glances at the line up forming behind you."
        wt_image new_barista_coffee_1
        taylor.c "Thank you for being honest with me.  Here's your coffee.  I really need to get back to work."
        $ taylor.conversation_event = 8
      "Try not to scare her":
        player.c "I'd like to spend some time with you to get to know you better. I'd like to know more about what makes you tick. I'm a good connector, and sometimes I help connect people who share a common interest."
        player.c "Like most of the men and many of the women who come in here, I find you beautiful, and the idea of spending time with you and getting to know you better is very appealing."
        player.c "I'm hopeful that perhaps you and I may share some interests in common. I have no idea whether we do or not yet, but I hope to use our date to find out."
        "She nods and glances at the line up forming behind you."
        wt_image new_barista_coffee_1
        taylor.c "Thanks for being honest with me. Here's your coffee. I really need to get back to work. I'll think about what you said, and give my answer soon. Okay?"
        player.c "Of course."
        $ taylor.conversation_event = 7
    $ taylor.week = week # note: this makes sure a week passes before next conversation takes place
  # meeting after ask for date if have tag 'supersexy'
  elif taylor.conversation_event == 5:
    wt_image new_barista_coffee_3
    "Taylor looks a little nervous as she hands over your coffee."
    taylor.c "Okay.  I've thought things over."
    player.c "About going on a date with me?"
    taylor.c "Yes.  You aren't going to expect me to put out on our first date, are you?"
    $ title = "How do you respond?"
    menu:
      "Honestly":
        player.c "Honestly, yes I do.  Not because I think you're 'easy', though."
        player.c "It's just in my experience, when women get the chance to be alone with me, they usually do want to have sex with me. Sometimes they wait for me to make the first move. Sometimes they don't."
        taylor.c "Wow.  You didn't even sound cocky when you said.  Okay.  Yeah.  I get that.  I'm going to try and control myself, though. Is that okay?"
        player.c "Absolutely"
        taylor.c "Okay.  Good.  So, you'll call me?"
      "Be delicate":
        player.c "Of course not.  I don't expect you to do anything you aren't comfortable with.  Why don't we just go out for dinner, have a chance to get to know each other, and see where things go from there?"
        taylor.c "Okay.  Thanks.  That sounds good.  So, you'll call me?"
    player.c "I will."
    sys "Unfortunately, you can't, as her dates haven't yet been implemented."
    "She hands over her phone number with your coffee."
    $ taylor.conversation_event = 6
  # waiting for you to call her for a date
  elif taylor.conversation_event == 6:
    "Taylor seems to be avoiding you.  You haven't called her yet for a date, so she may be feeling stood up.  Another barista brings you your coffee."
    rem tags 'coffee_already_today' from player # this is to avoid having Taylor serve you if you order a second coffee today
  # second dominate conversation if tried not to scare her first time
  elif taylor.conversation_event == 7:
    wt_image new_barista_coffee_2
    taylor.c "Hi.  I thought over what you were saying."
    taylor.c "I think you're a nice guy and I get that maybe we may have something in common if we spent some time together to try and figure that out."
    taylor.c "It's just that I'm really busy these days with school and work, and I don't have a lot of time to date.  I think it makes more sense for me to spend what time I do have with guys my own age."
    taylor.c "Thanks for asking, even though you really shouldn't bother sales people who have to be nice to you with unsolicited requests for date."
    wt_image new_barista_coffee_1
    taylor.c "Here's your coffee.  Have a great day!"
    $ taylor.conversation_event = 3
  # second dominate conversation if talked about BDSM first time
  elif taylor.conversation_event == 8:
    wt_image new_barista_coffee_3
    "Taylor looks a little nervous as she hands over your coffee."
    taylor.c "Okay.  I've thought things over."
    player.c "About going on a date with me?"
    taylor.c "Yes.  So the thing is, I have no idea how this works, or what you're going to expect of me."
    taylor.c "I'm pretty blunt sometimes, and say things that probably I should keep to myself.  Or should at least be more sensitive about other people's feelings in how I say them. I'm just not a beat around the bush sort of person, and you aren't either, which I like."
    taylor.c "But I could also see that maybe I might say something you think I shouldn't.  So what happens then?  Are you going to try and punish me? Because I don't know how I'll react to that."
    taylor.c "Not to mention that I'm a complete wuss when it comes to pain.  So even the idea of you spanking me scares me.  Plus I'm pretty sure you have things a lot more intense than spanking in mind when you say 'punishments'."
    taylor.c "I might be a huge disappointment to you, because I don't think I can do some of the things you may want to do with me."
    $ title = "How do you respond?"
    menu:
      "We are still talking about a first date, right?":
        "Taylor laughs."
        taylor.c "Yes.  Okay, I guess I'm getting a bit carried away.  I'm just new to this whole thing."
        player.c "Step number one - the most crucial step - is trust.  Hopefully that will come as we get to know each other."
        player.c "For now, I just ask that you obey me when we are out on our date, and trust me to enough to know that I will not do anything to make you regret giving me that authority over you.  Okay?"
        taylor.c "Giving you authority over me.  Wow.  Okay.  Can't believe I'm saying this, but let's give it a try."
      "I require absolute obedience":
        player.c "Taylor, you have to make up your own mind about whether you want to come on a date with me.  If you do come on a date, however, I will demand absolute obedience from you when you are with me."
        taylor.c "Seriously?"
        player.c "Seriously.  You need to trust me.  Trust that I will keep you safe.  Trust that I will be careful with you, and not demand anything more from you than you are capable of giving."
        player.c "Trust also, however, that I will hold you to a high standard, and demand from you everything that you are capable of giving, when you are ready to give it."
        "Taylor holds her breath for a moment, thinking."
        taylor.c "Wow.  Okay.  No guy my age has ever said he was going to hold me accountable like that, let alone ask me for obedience.  Can't believe I'm saying this, but let's give it a try."
    taylor.c "Just one last thing though. You aren't going to spank me on our first date, are you?"
    player.c "Only if I need to. Or if you ask me to. Assuming I give you permission to talk."
    taylor.c "Seriously? Wow. Okay. This is going to be different."
    "She hands you her phone number with your coffee."
    $ taylor.conversation_event = 6
  # for after your first date, if a good result
  elif taylor.conversation_event == 9:
    wt_image new_barista_coffee_3
    taylor.c "I don't have time to chat, but I wanted you to know that I'm looking forward to our next date."
    "Taylor gives you a somewhat goofy flirty look as she turns away to look after the other customers."
  # for after Taylor is lost because you didn't call her for a date
  elif taylor.conversation_event == 10:
    "You don't see Taylor around.  Then you spot her, in the back.  She's avoiding you.  It's been over two weeks since she gave you her number, and you didn't call her.  It seems she's given up on you."
    "Another barista brings you your coffee.   You never see Taylor again."
    sys "Note: you can't avoid this result as dates with Taylor haven't been activated yet."
    $ samantha.new_barista_switch = 3
    $ taylor.conversation_event = 11
    $ taylor.dismiss(False)
  # meeting after asking for date for moneybags
  elif taylor.conversation_event == 12:
    wt_image new_barista_coffee_2
    taylor.c "Okay.  I've thought things over.  Straight up, I'm only contemplating this because you have money, and I'm curious about what your lifestyle's like compared to mine."
    taylor.c "Does that make me shallow?  And if you still agree to take me out knowing that, does that make you shallow, too?"
    $ title = "How do you respond?"
    menu:
      "Let's try one date and see what happens":
        player.c "I'm trying to remember, did I ask you out on a date or ask you to marry me?"
        "Taylor laughs."
        taylor.c "Was I over-thinking things?"
        player.c "Maybe just a bit?  How about we try one date and see whether we enjoy each other's company?"
        wt_image new_barista_coffee_3
        taylor.c "Okay.  But don't expect me to put out on our first date, okay?"
        player.c "Not even if it's a very expensive restaurant?"
        "She laughs again, and there's maybe a hint of nervous excitement to the laugh as she hands over her phone number with your coffee.  The young woman may be more interested in you than she's trying to let on."
        $ taylor.conversation_event = 6
      "Maybe we should drop the idea":
        player.c "Thanks for your honesty, Taylor.  You're right, under the circumstances, it probably doesn't make sense for us to go out."
        wt_image new_barista_coffee_1
        taylor.c "Yeah, you're right.  It's better for me to finish my education, make lots of money, and then experience your lifestyle."
        "You take your coffee and leave."
        $ taylor.conversation_event = 3
  else:
    pass
  return

label taylor_lesbian:
  player.c "Taylor, you're not a lesbian, are you?"
  wt_image new_barista_coffee_2
  if taylor.conversation_event == 2:
    taylor.c "What?  No.  What a weird question."
    player.c "It's just the last barista was a lesbian."
    taylor.c "So that made you think maybe I was a lesbian too? What, did you think this shop has some rule about only hiring lesbians?"
    player.c "I'm not sure I was thinking at all."
    wt_image new_barista_coffee_1
    "She laughs and hands over your coffee."
  else:
    taylor.c "Seriously? I turn you down for a date and you think I must be a lesbian?"
    wt_image new_barista_coffee_1
    taylor.c "Okay. Sure. If that makes you feel better. Yes, I'm a lesbian. See you later, weirdo."
  add tags 'discussed_lesbian' to taylor
  return

label taylor_bi:
  player.c "Taylor, have you ever wondered what it would be like to be with a woman?"
  wt_image new_barista_coffee_2
  if taylor.has_tag('discussed_lesbian'):
    taylor.c "What is it with you and my sex life?  You perving on about me with women, specifically."
  else:
    taylor.c "What? No. What a weird question."
  player.c "I know some women who'd be interested in meeting you. Successful, attractive women, I might add."
  taylor.c "Look.  Whatever weird sex fantasies you've been having, keep me out of them.  Okay?"
  wt_image new_barista_coffee_1
  taylor.c "Here's your coffee. Bye!"
  add tags 'discussed_bi_curious' to taylor
  return

label taylor_career:
  player.c "Taylor, would you be interested in some career counseling?"
  wt_image new_barista_coffee_2
  taylor.c "Well, I'm in my second year of university and I've already picked my major for my commerce degree. I'm going to do accounting."
  taylor.c "I haven't decided if I want to focus on assurance or tax after I graduate, but I know I want to work for one of the big four accounting firms."
  taylor.c "If I keep up my current marks I should have my pick from all of them, and then I can decide between assurance and tax after I do a work rotation with the principals from each of those departments."
  taylor.c "So I don't think I need career counseling just yet, but I appreciate the offer."
  player.c "Sure.  You're welcome."
  add tags 'discussed_career' to taylor
  return

label taylor_date:
  player.c "Taylor, would you like to join me for dinner some evening? My treat. I'd like to get to know you better."
  wt_image new_barista_coffee_2
  if player.has_tag('supersexy'):
    taylor.c "Oh.  Gee.  Well, I'm a lot younger than you.  You are pretty hot, though.  I mean, for a man of your age.  Any age, really, I guess."
    taylor.c "Can I think about it?  I've only ever dated guys my age.  I've never thought about having a fling with an older guy before."
    player.c "How old are you, exactly?"
    taylor.c "Twenty"
    player.c "Sure.  Think it over."
    "You take your coffee and leave her to let her head battle it out with her hormones."
    $ taylor.conversation_event = 5
  elif player.has_tag('wealthy'):
    taylor.c "Oh.  Gee.  Well, I'm a lot younger than you, and most people would consider me better looking."
    taylor.c "Rumor around the coffee shop, though, is that you have a lot of money, so I guess you're probably used to asking out women who are younger and better looking than you, even though it's a bit of a jerk maneuver to do that while they're working."
    taylor.c "I suppose you're going to offer to take me some place really expensive that I couldn't otherwise afford to go to?"
    player.c "Would you like that?"
    taylor.c "I don't know.  I've only ever dated guys my age, and none of them could ever afford to take me any place expensive.  I've never thought about having a fling with a rich guy.  I'm not sure if that's really me?  Can I think about it?"
    player.c "How old are you, exactly?"
    taylor.c "Twenty"
    player.c "Sure.  Think it over."
    "You take your coffee and leave her to her internal debate about what sort of young woman she wants to be."
    $ taylor.conversation_event = 12
  else:
    taylor.c "Oh.  Gee.  Well, I'm a lot younger than you, and most people would consider me better looking."
    taylor.c "I appreciate your confidence in asking me out, even though asking me out while I'm working is a bit of a jerk maneuver.  But I don't think you're really the right guy for me."
    wt_image new_barista_coffee_1
    taylor.c "Here's your coffee.  Enjoy!"
    $ title = "What do you do?"
    menu:
      "Just take your coffee":
        $ taylor.conversation_event = 3
      "Dominate her" if player.has_tag('dominant'):
        player.c "I've taken prettier girls than you over my knee, Taylor, and done so for being far less saucy.  As for your youth, how old are you?"
        wt_image new_barista_coffee_2
        taylor.c "Twenty"
        player.c "Twenty.  So you're an adult.  Old enough to know a date doesn't always have to be about trying to find your life partner.  Young enough that you should respect the opportunity to learn from someone who's seen more of this world than you."
        wt_image new_barista_coffee_1
        taylor.c "I guess."
        "You take your coffee and leave."
        $ taylor.conversation_event = 4
      "After today, look for a new barista (Stop going to Taylor)":
        call taylor_look_for_new_barista from _call_taylor_look_for_new_barista_2
  $ taylor.week = week # note: this makes sure a week passes before next conversation takes place
  return

label taylor_look_for_new_barista:
  "You take your coffee and leave, vowing to find a new person to serve you in the future."
  $ samantha.new_barista_switch = 3
  return

## Character Specific Actions

########### OBJECTS ###########
## Common Objects

# Contact - Taylor
label taylor_contact:
  # Content Not Yet Implemented, which is why the silly 'banana' tag if statement
  if taylor.has_tag('banana'):
    if taylor.conversation_event == 10:
      "You try calling Taylor, but she doesn't take your call. It's been over four weeks since she gave you her number, and you didn't call her. It seems she's given up on you."
      "You don't know if she changes job, or just gets really good at avoiding you, but you never see Taylor at the coffee shop again."
      $ taylor.conversation_event = 11
      $ samantha.new_barista_switch = 3
      $ living_room.remove_action(taylor.action_contact)
    # first date
    elif taylor.conversation_event == 6:
      "It's going to cost a little bit of money to take Taylor out for a nice first date. Between getting ready and taking her out, you won't be able to do anything more today."
      $ title = "Ask her out?"
      menu:
        "Yes (costs 25 and ends day)":
          if player.money - player.min_money >= 25:
            # Content Not Yet Implemented
            $ taylor.training_session()
            $ taylor.conversation_event = 9
            change player money by -25 notify
          else:
            sys "You do not have enough money for the date."
        "Not Yet":
          pass
    # subsequent dates
    elif taylor.conversation_event == 9:
      $ taylor.training_session()
      $ taylor.random_number = renpy.random.randint(1, 10)
      if taylor.random_number >= 7:
        # Content Not Yet Implemented
        pass
      else:
        ## NEED IMAGE
        taylor.c "Hi. Thanks for calling, but I can't go out this week. I have a lot of studying I need to do. I still want to see you again, though, when I have more time. Maybe you could check back again next week?"
    else:
      pass
  else:
    sys "Dates with Taylor the Coffee Girl will have to wait until a later version of the game."
  return

# Review Files

## Character Specific Objects


## Items
# Give Butt Plug
label give_bp_taylor:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_taylor:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_taylor:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_taylor:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_taylor:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_taylor:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_taylor:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_taylor:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_taylor:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_taylor:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_taylor:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
#label taylor_start_day: # not needed
#  pass
#  return

# End Day
label taylor_end_day:
  #rem tags 'coffee_already_today' from player # note: not needed here as this same coding is in samantha's end_day label
  $ taylor.dismiss(False) # this allows coffee_shop to bring her back if appropriate
  return

# End Week
label taylor_end_week:
  ## Reset Weekly Actions - Coffee Girl Not Called
  if taylor.conversation_event == 6:
    $ taylor.lose_date += 1
    if taylor.lose_date == 3:
      $ taylor.conversation_event = 10
  else:
    pass
    # no idea what the following coding is from or why
    #$ taylor.temporary_count = player.desire_mod + player.sos_mod + player.submission_mod
    #if taylor.temporary_count > 10:
    #  $ energy_long -= 10
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
