## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package bethany name "Bethany, The Banker" description "Allows Bethany to be a minor character." dependencies core
register bethany_pregame 10 in core as 'Bethany the Banker'

# Pregame
label bethany_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', 'Bethany the Banker (Phoenix Marie)')]

    ## Character Definition
    bethany = Person(Character("Bethany", who_color="#808080", what_color="#808080"), "bethany", cut_portrait = True, prefix = "", suffix = "the Banker")

    # Other Characters
    # Navy
    businessman = Character("Business Man", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # 64,0,64
    bethany_client_2 = Character("Client #2", who_color="#400040", what_color="#400040", window_background = gui.dialogue_background_dark_font_color)
    # Blue
    bethany_client_3 = Character("Client #3", who_color="#0000FF", what_color="#0000FF", window_background = gui.dialogue_background_dark_font_color)
    # 0,64,128
    mr_lang = Character("Mr. Lang", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color)
    # 128,64,0
    bethany_gus = Character("Gus", who_color="#804000", what_color="#804000", window_background = gui.dialogue_background_dark_font_color)

    ## Actions
    bethany.action_talk = bethany.add_action("Speak to the Account Manager", label = "_talk", condition = "bethany.can_be_interacted")
    bethany.action_contact_getting_back = living_room.add_action("Get back to Bethany the Banker", label = bethany.short_name + "_contact_getting_back", context = "_contact_other", condition = "bethany.ready_to_help_school == 1 or bethany.ready_to_help_school == 2")
    bethany.action_contact_check_school = None
    bethany.action_contact_demonstrate = living_room.add_action("Have Bethany the Banker demonstrate her skills", label = bethany.short_name + "_contact_demonstrate", context = "_contact_other", condition = "bethany.can_be_interacted and bethany.has_tag('demonstrate_contact_open')")
    # N/A

    ## Tags
    # Common Character Tags
    bethany.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    # Bank
    # note: can't enter bank until event creates connection to office tower
    bank = Location("Global Trust Bank", 'bank', cut_portrait = True, enter_break_labels = ['bank_no_access'], enter_labels = ['bank_enter'], exit_labels = ['bank_exit'], area = 'offices')
    bank.connection_ot = bank.add_connections(office_tower)
    bethany.location = bank
    bethany.fixed_location = bank

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('bank_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    # bethany.add_stats_with_value('temporary_count') #disabled as this is auto-added to all characters

    # Character Specific Variables
    bethany.add_stats_with_value('bj_week', 'disclosed_pimping', 'hypno_blowjob_count', 'hypno_bj_request_count', 'hypno_swallow_count', 'ready_for_visit_at_school', 'ready_to_help_school', 'torture_count', 'torture_week', 'whore_count', 'whore_departure_count', 'whore_lost_countdown', 'whore_name_number')
    # note re bethany.whore_name_number:  1: her real name, 2: a custom name
    # note re bethany.ready_to_help_school:  1: activates Get Back to Bethany action, 2: allows you to finalize sending her to school by talking to Hannah, 3: she's been sent to Hannah, 4: this has been shut off

    bethany.whore_name = 'Bethany'

    # Location Variables
    bank.add_stats_with_value('foreclosure_warning', 'investment_total_income_to_date', 'investment_weeks_paid', 'loan_interest', 'notice_about_investments', 'status')
    # bank.status == 1: bank.name = "Global Trust Bank"
    # bank.status == 2: bank.name = "First Nationalized Bank"
  return

# Display Portrait
# CHARACTER: Display Portrait
label bethany_update_media:
    if current_location == bank:
        $ bethany.change_image('banker_office_1')
    elif bethany.has_tag('whore'):
        $ bethany.change_image('banker_test_1')
    else:
        pass
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label bethany_examine:
    if current_location == bank:
        "A very cheerful bank account manager."
    elif bethany.has_tag('whore'):
        if bethany.disclosed_pimping == 1:
          player.c "One of your escorts."
        elif bethany.disclosed_pimping == 2:
          player.c "One of your sexual concierges."
        elif bethany.disclosed_pimping == 3:
          player.c "One of your 'hoes."
    else:
        pass
    return

label bethany_talk:
  if not bethany.has_tag('already_visited_today') and bethany.location == bank:
    $ title = "Do you want to speak to an account manager?"
    menu:
      "Yes":
        wt_image banker_office_1
        if bethany.has_tag('first_visit'):
          "A very cheerful account manager comes out to greet you and ushers you into her office."
          bethany.c "Hello!!   My name is Bethany.  What a pleasure to meet you!"
          bethany.c "Here at Global Trust Bank our clients are our most precious assets.  We treat each and every one with the care and attention they deserve.  I so hope that you will become one of our precious clients."
          bethany.c "Could I interest you in one of our loan or investment options?  Our motto is 'Service with a Smile'.  How could I be of service to you today?"
          rem tags 'first_visit' from bethany
        else:
          "Bethany brings you back to her office."
          bethany.c "So nice to see you again!! How can I be of service to you today?"
        $ bethany.bank_sex_act_today = False
        if player.hypnosis_level > 0 or not bethany.has_tag('asked_for_date'):
          $ title = "What do you want to discuss with her?"
          menu menu_banker_enter:
            "Hypnotize her" if player.hypnosis_level > 0:
              call bethany_hypno_bank from _call_bethany_hypno_bank
            "Ask her on a date" if not bethany.has_tag('asked_for_date'):
              player.c "I'd like to get to know you better, Bethany.  Would you like to go on a date with me sometime?"
              bethany.c "Oh, I'm pretty much married to the bank!  I mean, not really married of course.  That would be silly.  But between looking after the customers, and the corporate executives, and making sure I meet my key performance indicators each month.  I just don't have time to date anyone.  I'm sure you understand."
              add tags 'asked_for_date' to bethany
              jump menu_banker_enter
            "Just discuss her bank's services":
              pass
        while bethany.temporary_count == 0:
          $ title = "What do you want to discuss?"
          menu menu_bethany_bank_discuss:
            "Elite Status" if bank.loan_interest == 5 and not bethany.has_tag('hypnotized_now') and not bethany.has_tag('pen_gifted') and week > bethany.bj_week:
              if not bethany.has_tag('bj_in_office'):
                player.c "Now that I'm elite status, does that come with any perks?"
                bethany.c "Well, you're already getting a lower interest rate than our other customers, and you have access to our super smart portfolio managers to make you a lot of money."
                $ title = "You were hoping for:"
                menu:
                  "Something a little more personal":
                    wt_image banker_office_2
                    player.c "I was hoping for a more personal show of appreciation, from my personal banker."
                    bethany.c "Oh!  I see.  Wouldn't it be better if we kept our relationship on a purely professional basis?"
                    add tags 'personal_service' to bethany
                  "Service with a Smile":
                    player.c "Your bank's motto is Service with a Smile.  I was hoping to get some of that."
                    bethany.c "I always try to smile when I'm with my customers."
                    player.c "I was thinking more of the service part.  Personal service specifically, from my personal banker."
                    bethany.c "I see.  Wouldn't it be better if we kept our relationship on a purely professional basis?"
                    add tags 'personal_service' to bethany
                  "A nice pen":
                    wt_image banker_office_1
                    player.c "Don't banks sometimes provide gifts to their best customers?  A nice pen, perhaps?"
                    bethany.c "Oh yes!  I'd be happy to give you one of our special fountain pens for elite customers only.  It works super great!  Thanks for dropping by."
                    "She provides you a very expensive looking fountain pen then shows you to the door."
                    add tags 'pen_gifted' to bethany
                    add 1 bank_pen to player notify
                if bethany.has_tag('personal_service'):
                  $ title = "What do you say?"
                  menu:
                    "Yes, keep this professional":
                      wt_image banker_office_1
                      player.c "You're right, Bethany.  That was inappropriate of me."
                      bethany.c "No worries!  And I do have something for you!  It's one of our special fountain pens for elite customers only.  It works super great!  Thanks for dropping by."
                      "She provides you a very expensive looking fountain pen then shows you to the door."
                      add tags 'pen_gifted' to bethany
                      add 1 bank_pen to player notify
                    "I thought personal service was your profession":
                      player.c "I thought personal service was your profession?"
                      if bank.has_tag('investments_in_place') and bank.has_tag('loan_in_place') and player.money >= 500 and not bethany.bank_sex_act_today:
                        "She sighs."
                        bethany.c "I am required to keep our best customers satisfied, that's true."
                        wt_image banker_office_12
                        bethany.c "Just let me get this blouse off so you don't make a mess on it. I have other customers I need to look after today, and I don't want to look unprofessional."
                        wt_image banker_office_5
                        "Bethany kneels down in front of you and takes out your cock."
                        bethany.c "Do you just want a quickie, or do you want to lie down and I'll give you our full elite customer attention?"
                        $ title = "Do you want a quickie or more thorough attention?"
                        menu:
                          "Lie back and relax":
                            wt_image banker_office_7
                            "You make yourself comfortable as Bethany leans over you.  She starts off with long, leisurely licks up and down your shaft."
                            wt_image banker_office_8
                            "She pays particular attention to the underside of your cock head, tickling and teasing it with her tongue."
                            wt_image banker_office_9
                            "When she senses your arousal building, she shifts to a more energetic pace, pumping your shaft with her fist as she sucks and licks with her lips and tongue.  You hold back as long as you can, enjoying her service even if it isn't technically with a smile."
                            wt_image banker_office_10
                            "Eventually, you can hold back no longer.  She cups your balls in her hand and massages them as you start to cum, filling her throat with your jizz."
                            player.c "[player.orgasm_text]"
                          "Just use her like this":
                            wt_image banker_office_6
                            "A quickie is fine, Bethany. Just hold your head still while I fuck your mouth."
                            bethany.c "mmmppphhh"
                            "That might have been an 'okay', but it was hard to tell with your cock halfway down her throat.  You face fuck her quickly, shooting your load down her throat as you cum."
                            player.c "[player.orgasm_text]"
                        wt_image banker_office_12
                        "Bethany gets back to her feet, swallowing your cum as she does, and puts her clothes back on."
                        bethany.c "I hope you don't mind me swallowing it.  It makes too much of a mess if I let my clients cum anywhere else but in my mouth.  If you wouldn't mind seeing yourself out, I have other customers to see now."
                        $ bethany.blowjob_count += 1
                        $ bethany.swallow_count += 1
                        $ bethany.bank_sex_act_today = True
                        add tags 'bj_in_office' to bethany
                        orgasm notify
                      elif bethany.bank_sex_act_today:
                        wt_image banker_office_11
                        bethany.c "I know you were granted elite status, but you're not currently doing enough business with the bank to qualify for more of my personal attention right now.  If you'll be going, I have more valuable clients to attend to."
                        "She escorts you to the door."
                        call forced_movement(office_tower) from _call_forced_movement_698
                      else:
                        wt_image banker_office_11
                        bethany.c "I know you were granted elite status, but you're not currently doing enough business with the bank to qualify for my personal attention right now.  If you'll be going, I have more valuable clients to attend to."
                        "She escorts you to the door."
                        call forced_movement(office_tower) from _call_forced_movement_699
              else:
                bethany.c "Do you need personal attention again, to prove that you're a valuable customer?"
                $ title = "Do you want a blow job from Bethany?"
                menu menu_bethany_elite_blow:
                  "Yes, I want a blow job":
                    if bank.has_tag('investments_in_place') and bank.has_tag('loan_in_place') and player.money >= 500 and not bethany.bank_sex_act_today:
                      wt_image banker_office_12
                      bethany.c "Just let me get this blouse off so you don't make a mess on it.  I have other customers I need to look after today, and I don't want to look unprofessional."
                      wt_image banker_office_5
                      "Bethany kneels down in front of you and takes out your cock."
                      bethany.c "Do you just want a quickie, or do you want to lie down and I'll give you our full elite customer attention?"
                      $ title = "Do you want a quickie or more thorough attention?"
                      menu:
                        "Lie back and relax":
                          wt_image banker_office_7
                          "You make yourself comfortable as Bethany leans over you.  She starts off with long, leisurely licks up and down your shaft."
                          wt_image banker_office_8
                          "She pays particular attention to the underside of your cock head, tickling and teasing it with her tongue."
                          wt_image banker_office_9
                          "When she senses your arousal building, she shifts to a more energetic pace, pumping your shaft with her fist as she sucks and licks with her lips and tongue.  You hold back as long as you can, enjoying her service even if it isn't technically with a smile."
                          wt_image banker_office_10
                          "Eventually, you can hold back no longer.  She cups your balls in her hand and massages them as you start to cum, filling her throat with your jizz."
                          player.c "[player.orgasm_text]"
                        "Just use her like this":
                          wt_image banker_office_6
                          "A quickie is fine, Bethany. Just hold your head still while I fuck your mouth."
                          bethany.c "mmmppphhh"
                          "That might have been an 'okay', but it was hard to tell with your cock halfway down her throat.  You face fuck her quickly, shooting your load down her throat as you cum."
                          player.c "[player.orgasm_text]"
                      wt_image banker_office_12
                      "Bethany gets back to her feet, swallowing your cum as she does, and puts her clothes back on."
                      bethany.c "I hope you don't mind me swallowing it.  It makes too much of a mess if I let my clients cum anywhere else but in my mouth.  If you wouldn't mind seeing yourself out, I have other customers to see now."
                      $ bethany.blowjob_count += 1
                      $ bethany.swallow_count += 1
                      $ bethany.bank_sex_act_today = True
                      add tags 'bj_in_office' to bethany
                      orgasm notify
                    elif bethany.bank_sex_act_today:
                      wt_image banker_office_11
                      bethany.c "I know you were granted elite status, but you're not currently doing enough business with the bank to qualify for more of my personal attention right now.  If you'll be going, I have more valuable clients to attend to."
                      "She escorts you to the door."
                      call forced_movement(office_tower) from _call_forced_movement_700
                    else:
                      wt_image banker_office_11
                      bethany.c "I know you were granted elite status, but you're not currently doing enough business with the bank to qualify for my personal attention right now.  If you'll be going, I have more valuable clients to attend to."
                      "She escorts you to the door."
                      call forced_movement(office_tower) from _call_forced_movement_701
                  "I want more than a blow job" if not bethany.has_tag('elite_more_blow'):
                    player.c "Yes, I'd like some personal attention Bethany, and I want more than a blow job."
                    bethany.c "I'm sorry, but elite status only gets you so much."
                    add tags 'elite_more_blow' to bethany
                    jump menu_bethany_elite_blow
                  "Not today, thanks":
                    player.c "Nothing for today, Bethany, thank you."
                    "She seems relieved."
                    bethany.c "Well, you know where to find me when you need something. Preferably something banking related. I really must be going now. I have other customers to look after."
                    "She shows you to the door."
                    call forced_movement(office_tower) from _call_forced_movement_702
                $ bethany.temporary_count = 1
            "Your loan" if bank.has_tag('loan_in_place'):
              $ title = "What do you want to do?"
              menu:
                "Ask about a better loan rate" if bank.loan_interest != 5:
                  if bethany.has_tag('hypnotized_now'):
                    player.c "You want to give me a better rate on my loan, Bethany.  I'm a very valuable customer."
                    if bank.has_tag('investments_in_place') and bank.has_tag('loan_in_place') and player.money >= 500:
                      bethany.c "You certainly do a lot of business with us  I can upgrade you to elite customer status."
                      bethany.c "From now on, if you borrow money, you'll only owe 5 in interest each week."
                      $ bank.loan_interest = 5
                    else:
                      bethany.c "I can only offer a lower rate to elite customers. You're not elite yet. Only the numbers will tell me when you're elite."
                      player.c "What do I need to become elite?"
                      bethany.c "Lots of products with us and more than 500 in savings."
                      player.c "If I had 500 in savings, I wouldn't need the loan."
                      bethany.c "That's why we'd be able to lower your rate!"
                  else:
                    player.c "Can't you get me a better rate on my loan? "
                    if bank.has_tag('investments_in_place') and bank.has_tag('loan_in_place') and player.money >= 500:
                      bethany.c "You certainly do a lot of business with us  I can upgrade you to elite customer status."
                      bethany.c "From now on, if you borrow money, you'll only owe 5 in interest each week."
                      $ bank.loan_interest = 5
                    else:
                      bethany.c "You're already getting a fabulous rate!  Its the best rate we can offer to non-elite customers."
                      player.c "What do I need to become elite?"
                      bethany.c "Lots of products with us and more than 500 in savings."
                      player.c "If I had 500 in savings, I wouldn't need the loan."
                      bethany.c "That's why we'd be able to lower your rate!"
                "Ask to increase your loan limit":
                  player.c "I'd like you to raise the limit on my loan."
                  bethany.c "I can't do that."
                  player.c "But you've secured it against the value of my house, which is worth way more than 500."
                  bethany.c "I know!  That's why we know you'll pay us off.  If we get to foreclose on your house, we'll make off like bandits."
                "Cancel the loan":
                  if not bethany.has_tag('hypnotized_now'):
                    wt_image banker_office_11
                  if player.money < 0:
                    bethany.c "You can't cancel your loan while you have an outstanding balance.  You need to pay it off first."
                  else:
                    bethany.c "Why do you want to cancel your loan?  Its not costing you anything unless you use it."
                    $ title = "How do you respond?"
                    menu:
                      "You're right, I'll keep it":
                        pass
                      "I don't trust myself with credit":
                        player.c "I don't trust myself with credit."
                        if bethany.has_tag('mentioned_lingerie'):
                          bethany.c "Worried you might splurge on too much lingerie and dildos?  I understand.  I'm sure that's a very addictive habit.  I'll cancel the loan arrangement for you."
                        else:
                          bethany.c "Low self control issues?  That's too bad.  Many of our best customers have low self control.  I'll cancel the loan arrangement for you."
                        rem tags 'loan_in_place' from bank
                        $ player.min_money = 0
              $ title = "What do you want to discuss?"
              jump menu_bethany_bank_discuss
            "Your investment" if bank.has_tag('investments_in_place'):
              $ title = "What about your investment?"
              menu:
                "How does it work again?":
                  player.c "How does my investment work again?"
                  bethany.c "It's super easy!  As long as you have 500 at the end of the week, we credit you with 25.  If you have 1000, we credit you with 50."
                  player.c "And you're sure there's no risk?"
                  bethany.c "There couldn't be.  All bank employees are required to put our bonuses in the investment fund.  With our wicked smart portfolio managers, what could go wrong?"
                "Cancel your investment" if not bank.has_tag('agreed_not_to_cancel_investment'):
                  if not bethany.has_tag('hypnotized_now'):
                    wt_image banker_office_11
                  player.c "I'd like to cancel my investment."
                  if bank.investment_total_income_to_date == 0:
                    bethany.c "But you haven't been using our investment fund!  Why don't you give it a try?  All you need to do is make sure you have at least 500 at the end of each week, and you'll get to see the money pour in!"
                  else:
                    bethany.c "But you've already made [bank.investment_total_income_to_date] from our fund!  Isn't that the easiest money you've ever made??  Why would you want to get out?  There's lots more money where that came from."
                  $ title = "Stay with the investment program?"
                  menu:
                    "Okay, I'll stick with it":
                      pass
                    "No, I want to get out":
                      if bank.investment_weeks_paid < 5:
                        call bethany_investment_get_out from _call_bethany_investment_get_out
                      else:
                        if not bethany.has_tag('hypnotized_now'):
                          wt_image banker_office_13
                        bethany.c "This is somewhat embarrassing, but it would be really bad for my performance appraisal this month if I lost you as a customer."
                        if not bethany.has_tag('hypnotized_now'):
                          wt_image banker_office_14
                        bethany.c "Could I convince you to stay in our fund, at least long enough for me to collect my bonus?"
                        $ title = "What do you say?"
                        menu:
                          "What exactly are you offering?" if not bethany.bank_sex_act_today:
                            wt_image banker_office_15
                            "She turns around and unzips her skirt, then pulls it down."
                            bethany.c "I'm offering you my ass, in return for you staying in the fund."
                            wt_image banker_office_16
                            bethany.c "Do we have a deal?"
                            $ title = "What do you say?"
                            menu menu_bethany_offer:
                              "I want a feel of your tits first" if not bethany.has_tag('offer_tits') and not bethany.bank_sex_act_today:
                                wt_image banker_office_17
                                bethany.c "Nudity is not allowed under bank regulations unless it's necessary and required to facilitate allowable sexual contact."
                                "Despite her statement, she doesn't prevent you from pulling down her bra and squeezing her tit."
                                wt_image banker_office_18
                                player.c "Does that mean you're being a bad girl right now, Bethany?"
                                "She bites her lip as you pinch her nipple."
                                bethany.c "It means I can't let you keep doing that unless you're about to put your cock in my ass."
                                add tags 'offer_tits' to bethany
                                $ title = "What do you say?"
                                jump menu_bethany_offer
                              "Turn around and bend over" if not bethany.bank_sex_act_today:
                                player.c "Turn around and bend over, Bethany."
                                wt_image banker_office_19
                                "She kneels on the guest couch in her office and squirts a glob of lubrication onto her rose bud.  It seems she was serious about offering you her ass."
                                player.c "Do you like getting fucked in the ass, Bethany?"
                                bethany.c "Not really, I just find this keeps things on a professional level."
                                wt_image banker_office_20
                                player.c "So if I was fucking your cunt right now, instead of your ass, that would be blurring the lines for you?"
                                bethany.c "Totally. This is just business retention for me. Please don't take offense. I'm sure you're a super cool guy and all."
                                player.c "So you keep your cunt exclusive for your boyfriend?"
                                bethany.c "Oh, I don't have a boyfriend! But yes, I'd like to think sometime when my career is really going well and life's not so hectic at the bank, maybe I will. Do you think you could just stick to fucking my ass and cut the small talk? These personal questions are making me a bit uncomfortable."
                                wt_image banker_office_21
                                "You roll her over and on top of you, letting your cock push further inside her."
                                player.c "The personal questions make you uncomfortable, but my cock in your ass is okay?"
                                bethany.c "Oh yes. That's fine! You can go faster now if you want. I've stretched enough to accommodate your girth, and I have another customer dropping by in a few minutes."
                                "Her next customer doesn't have to worry about being kept waiting.  You hold back your orgasm as long as you can, but the feel of your personal banker's tight ass gripping your cock soon has you ready to explode."
                                $ title = "Where do you want to cum?"
                                menu:
                                  "In her ass":
                                    player.c "[player.orgasm_text]"
                                    "You make your own, very personal deposit into the bowels of your personal banker."
                                    bethany.c "Oh. That felt like a big load! I'm going to have trouble keeping that inside me until my next bathroom break."
                                  "In her mouth":
                                    player.c "I'm ready to cum, Bethany.  Get off of me and onto your knees."
                                    bethany.c "Onto my knees?  Why?"
                                    player.c "So I can cum in your mouth."
                                    bethany.c "But you've been fucking my ass."
                                    player.c "I can pull out and spray all over you and your office if you prefer."
                                    bethany.c "No!  Don't do that.  All right, I'll swallow it."
                                    wt_image banker_office_6
                                    "She scrambles off of you and onto the floor."
                                    player.c "[player.orgasm_text]  That's it, swallow it all, then clean my cock up until it doesn't stink anymore.  You can't expect me to walk out of here with the smell of your ass on me."
                                    bethany.c "I guess not."
                                    "She dutifully cleans up your cock."
                                    player.c "How does it taste?"
                                    bethany.c "Gross, but thank you for asking."
                                    $ bethany.swallow_count += 1
                                if bethany.has_tag('hypnotized_now'):
                                  bethany.c "Thanks for sticking with our investment fund. I'm sure you won't regret it!"
                                  wt_image banker_office_4
                                  "You won't regret it, and she won't remember it after you finish wiping her memory of what happened while she was hypnotized."
                                else:
                                  wt_image banker_office_13
                                  bethany.c "Thanks for sticking with our investment fund. I'm sure you won't regret it!"
                                  add tags 'sex_in_office' to bethany
                                  add tags 'agreed_not_to_cancel_investment' to bank
                                $ bethany.bank_sex_act_today = True
                                $ bethany.anal_count += 1
                                orgasm notify
                                $ bethany.temporary_count = 1
                              "Just get me out":
                                call bethany_investment_get_out from _call_bethany_investment_get_out_1
                                $ bethany.temporary_count = 1
                              "Discuss something else":
                                $ bethany.temporary_count = 0
                          "Just get me out":
                            call bethany_investment_get_out from _call_bethany_investment_get_out_2
                            $ bethany.temporary_count = 1
                          "Discuss something else":
                            $ bethany.temporary_count = 0
              $ title = "What do you want to discuss?"
              jump menu_bethany_bank_discuss
            "Getting a Loan" if not bank.has_tag('loan_in_place'):
              if bethany.has_tag('hypnotized_now'):
                pass
              else:
                wt_image banker_office_1
              player.c "I might be interested in a loan."
              bethany.c "What a great decision!  We have the most flexible loan arrangement imaginable.  It's really a line of credit that integrates seamlessly into your cash flow."
              bethany.c "You go about your day to day business just like you always have, but now, instead of not being able to buy something if it would take you below 0, you can buy things up to -500.  Isn't that amazing!"
              player.c "So basically you'll lend me up to 500?"
              bethany.c "In return for security against your house."
              player.c "What?  My house is worth way more than 500."
              bethany.c "I know!  That's why we're willing to lend to you."
              player.c "What does the loan cost?"
              bethany.c "Nothing if you don't use it.  If your money is below 0 at the end of any week, we charge you a flat 10 for interest.  So simple!"
              player.c "You'll charge me 10 a week?  Even if I only owe you 5 on the loan at the end of the week?  Isn't that usury?"
              bethany.c "Probably, but our regulators can't even spell 'usury', let alone know what it means.  So can I sign you up?"
              if bank.loan_interest == 5:
                player.c "I used to pay only 5 per week, as an elite customer."
                bethany.c "That was before you cancelled your loan.  When you do less business with us, you stop being elite."
                player.c "But I'm signing up for the loan again."
                bethany.c "Fickle aren't you?  We can't classify fickle customers as elite."
                $ bank.loan_interest = 10
              if bethany.has_tag('hypnotized_now'):
                player.c "Can't you get me a better rate?  I'm a very valuable customer, Bethany."
                bethany.c "I can only offer a lower rate to elite customers.  You're not elite yet.  Only the numbers will tell me when you're elite."
              $ title = "Take the loan arrangement?"
              menu:
                "Sign up":
                  player.c "Okay"
                  bethany.c "Great!  Here's the paperwork."
                  if player.has_tag('signed_house_docs'):
                    "The forms are pretty simple.  The only unusual question is:  What do you expect to use the funds for?"
                    $ title = "What do you intend to use the money for?"
                    menu:
                      "Business expenses":
                        bethany.c "Oooh ... you run your own business.  How exciting!"
                        if bank.has_tag('investments_in_place'):
                          pass
                        else:
                          bethany.c "When your business becomes super-profitable, be sure and check back with us about investment options.  We have a special fund that's just perfect for the successful businessman."
                      "Entertainment":
                        bethany.c "How nice!  You should be able to treat your special someone to some fun entertainment with this money."
                      "Lingerie and dildos mostly":
                        bethany.c "You want to use the money to buy lingerie and dildos?"
                        player.c "They're not for me.  I like to give them away as gifts to married women, and then see what happens."
                        bethany.c "Is that a meaningful hobby?"
                        player.c "You'd be surprised."
                        add tags 'mentioned_lingerie' to bethany
                    $ player.min_money = -500
                    $ bank.loan_interest = 10
                    add tags 'loan_in_place' to bank
                  else:
                    "The forms are pretty simple, but you realize the bank's not going to accept them until you finish the paperwork related to the purchase of your house."
                    bethany.c "Didn't your real estate agent tell you how important it is to finalize all the documents related to your home?  We can't lend you money unless we know you have good title we can take away if we need to."
                "Pass":
                  pass
              $ title = "What do you want to discuss?"
              jump menu_bethany_bank_discuss
            "Making an investment" if not bank.has_tag('investments_in_place'):
              player.c "What investment options do you have for me?"
              if player.money < 300:
                if bethany.has_tag('hypnotized_now'):
                  bethany.c "I'm not allowed to let you into our investment fund.  You don't have enough money."
                  player.c "How much do I need?"
                  bethany.c "I can sign you up at 300, but you can't invest until you have 500."
                else:
                  wt_image banker_office_11
                  bethany.c "I don't have anything for you.  Our investments are only for people who can afford them.  You know.  Successful people?  I'm sure you've heard of them."
                  player.c "What's your definition of successful?"
                  bethany.c "You'll need at least 500 to invest, but I can sign you up once you have at least 300."
              else:
                if not bethany.has_tag('hypnotized_now'):
                  wt_image banker_office_1
                if player.money >= 500:
                  bethany.c "I have the perfect solution for a successful person like you!"
                else:
                  bethany.c "You don't have enough money to invest with us yet, but you're close enough that I can tell you about our program and get the paperwork all signed up."
                bethany.c "We have a great investment fund run by wicked smart portfolio managers.  I can sign you up to participate, and the great thing is, your money is never locked up!  You can access it at any time."
                bethany.c "But if you don't spend it, then at the end of the week if you have at least 500, we pay you 25.  If you have at least 1000, we pay you 50.  How cool is that!"
                $ title = "What do you say?"
                menu menu_invesment:
                  "Pass" if bethany.has_tag('risky'):
                    pass
                  "Sign me up!":
                    player.c "Okay, sign me up."
                    bethany.c "Great!  The paperwork's pretty easy.  I just need to know your primary source of income."
                    $ title = "What do you tell her?"
                    menu:
                      "Personal services":
                        bethany.c "Cool!  You mean you help people for a living?"
                        player.c "From time to time."
                      "Training women":
                        bethany.c "Cool!  So you're sort of like a life coach, helping women with their problems?"
                        player.c "You could say that."
                    bethany.c "Any other sources of income?"
                    if player.has_tag('whores_once') or samantha.domme_status == 3 or samantha.domme_status == 4 or player.whore_count > 0:
                      $ title = "What do you tell her?"
                      menu:
                        "Sometimes I connect men and women":
                          player.c "Sometimes I earn some money connecting women to men who want to meet them."
                          bethany.c "Really?  You mean, like an escort service?"
                          $ title = "What do you tell her?"
                          menu:
                            "You could call it that":
                              player.c "You could call it that."
                              $ bethany.disclosed_pimping = 1
                            "Sexual concierge work actually":
                              player.c "It's sexual concierge work, actually."
                              bethany.c "Woooo.  Sounds sophisticated!  Do your whores get to charge more that way?"
                              player.c "Not really, but it adds a touch of class to the whole endeavor."
                              $ bethany.disclosed_pimping = 2
                            "I prefer to call it pimping my 'hoes":
                              player.c "I prefer to call it pimping my 'hoes."
                              $ bethany.disclosed_pimping = 3
                        "Nothing comes to mind":
                          pass
                    else:
                      player.c "None currently."
                    bethany.c "Great!  Well that's all the paperwork done.  Now all you have to do is keep at least 500 available at the end of each week, and watch the money roll in!"
                    $ bank.notice_about_investments = 2
                    add tags 'investments_in_place' to bank
                  "That's a crazy high interest rate" if not bethany.has_tag('crazy_interest'):
                    player.c "That's a crazy high interest rate."
                    bethany.c "I know!  Isn't it great?  Our investment managers are wicked smart."
                    player.c "What do they invest in?"
                    bethany.c "Different things.  Whatever's hot.  Dot.com start ups.  Subprime mortgages.  Right now tulip futures are going through the roof in Holland!  Our managers are leveraged up 10 to 1 to take advantage of this sure fire trend."
                    add tags 'crazy_interest' to bethany
                    $ title = "What do you say?"
                    jump menu_invesment
                  "Too risky" if bethany.has_tag('crazy_interest') and not bethany.has_tag('risky'):
                    player.c "That sounds too risky to me."
                    bethany.c "Oh, it can't be!  Our executives make all us employees put our bonuses in the fund.  My retirement funds are growing like wildfire!  I'm sure they wouldn't let us do that if they didn't know it was 100% safe."
                    add tags 'risky' to bethany
                    $ title = "Reconsider?"
                    jump menu_invesment
              $ title = "What do you want to discuss?"
              jump menu_bethany_bank_discuss
            "Nothing (Leave)":
              $ bethany.temporary_count = 1
        if bethany.has_tag('hypnotized_now'):
          $ bethany.hypno_session() # this command deducts correct energy and records that she's been hypnotized today
          if bethany.hypno_count == 5:
            "You've hypnotized Bethany a number of times now.  Despite your best efforts, you're not able to significantly modify her behavior or implant a trigger.  Her single-minded devotion to the bank's policies - and the key performance indicators that drive her bonus - leaves her disinterested in other motivations or desires, whether introduced by hypnosis or otherwise."
          "You have Bethany cover herself up and bring her out of her trance, then you leave."
          call forced_movement(office_tower) from _call_forced_movement_703
        else:
          "You leave the bank branch."
          call forced_movement(office_tower) from _call_forced_movement_704
        $ bethany.visit_count += 1
        add tags 'already_visited_today' to bethany
        rem tags 'hypnotized_now' 'crazy_interest' 'risky' 'offer_tits' 'personal_service' from bethany
        $ bethany.temporary_count = 0
      "No, just leave":
        call forced_movement(office_tower) from _call_forced_movement_705
  elif bethany.has_tag('already_visited_today') and bethany.location == bank:
    bethany.c "If you'll be going, I have more valuable clients to attend to."
    "She escorts you to the door."
    call forced_movement(office_tower) from _call_forced_movement_706
  else:
    pass
  return

## Character Specific Actions
# Hypnotize Bethany
# OBJECT: Bank Branch
label bethany_hypno_bank:
  add tags 'hypnotized_now' to bethany #special tag to show correct images later in the scene
  player.c "Look at this for me, Bethany."
  call focus_image from _call_focus_image_24
  player.c "You and I are going to have a pleasant chat. I am going to talk. You are going to listen. Listen to the sound of my voice. Only my voice. Only my voice now, Bethany. Only my voice."
  wt_image banker_office_2
  "It doesn't take long for her to fall under your trance."
  if bethany.hypno_count == 1:
    player.c "You want me to feel like a valued customer, Bethany.  You want to provide good service to me.  Remove your top so I feel valued and enjoy our time together."
    wt_image banker_office_3
    "Bethany takes off her suit coat and unbuttons her blouse, exposing her bra."
    bethany.c "I'd like to show you my tits, but I'm not allowed to go any further.  Company policy forbids me from exposing myself to a customer."
    player.c "Your bank created a policy against employees taking off their clothes?"
    bethany.c "Isn't that crazy! Apparently there was trouble at one of our branches a few years ago. Some of the girls there were using inappropriate sales techniques. When the regulators heard about it they came down super hard on the bank."
    player.c "At least unbutton your blouse all the way and lean forward."
    wt_image banker_office_4
    bethany.c "Like this?  Does this help you to feel like a valued customer?"
  else:
    player.c "Treat me like the valuable customer I am, Bethany.  Show me that you appreciate me being here."
    wt_image banker_office_4
    "She takes off her suit coat, unbuttons her blouse, and leans forward, providing you as much of a view of her bosom as her bank's policy allows."
  $ title = "What do you want to discuss with her?"
  menu menu_banker_hypno:
    "Tell her to blow you" if not bethany.bank_sex_act_today:
      if bethany.hypno_bj_request_count == 0:
        player.c "Is it against bank policy for you to get down on your knees and blow me?"
        bethany.c "Surprisingly not! The bank tried to outlaw that, but some of the girls made a big stink about it because it meant they couldn't shag their favorite guys on their lunch break"
        bethany.c "They turned it into a big human rights lawsuit about free sexual expression, and the bank relented."
        bethany.c "So the policy was amended to say we're allowed to blow a customer as long as its someone we like. Everyone knows what that really means is we're allowed to blow our most valuable customers."
        bethany.c "We still have to keep some clothes on so as not to violate the policy against gratuitous exposure, but exposure that is 'necessary and required for the purposes of completing allowable sexual acts' is okay."
        player.c "You seem to know that policy very well."
        bethany.c "I always stay up-to-date on all compliance rules!  I don't want to get a bad audit."
        player.c "Do the rules allow you to do more than blow me?"
        bethany.c "Only if it's necessary to retain a relationship with the person you like. Which everyone knows includes retaining your business."
      player.c "I'm a valuable customer, Bethany. You should make me feel like a valued customer. You want me to feel like a valued customer. You can show me that I'm a valuable customer by blowing me, Bethany."
      if bank.has_tag('investments_in_place') and bank.has_tag('loan_in_place') and player.money >= 500:
        bethany.c "I certainly do appreciate all the business you do here."
        player.c "Show me that, Bethany. Use your mouth for something more interesting than talking and show me some true service with a smile."
        wt_image banker_office_5
        "She drops to her knees in front of you and takes out your cock."
        bethany.c "If you have time, feel free to lie down and I'll give you our elite customer attention."
        $ title = "Do you want a quickie or more thorough attention?"
        menu:
          "Lie back and relax":
            wt_image banker_office_7
            "You make yourself comfortable as Bethany leans over you.  She starts off with long, leisurely licks up and down your shaft."
            wt_image banker_office_8
            "She pays particular attention to the underside of your cock head, tickling and teasing it with her tongue."
            wt_image banker_office_9
            "When she senses your arousal building, she shifts to a more energetic pace, pumping your shaft with her fist as she sucks and licks with her lips and tongue.  You hold back as long as you can, enjoying her service even if it isn't technically with a smile."
            wt_image banker_office_10
            "Eventually, you can hold back no longer. She cups your balls in her hand and massages them as you start to cum, filling her throat with your jizz."
            player.c "[player.orgasm_text]"
          "Just use her like this":
            wt_image banker_office_6
            player.c "No time for that, Bethany. Just hold your head still while I fuck your mouth."
            bethany.c "mmmppphhh"
            "That might have been an 'okay', but it was hard to tell with your cock halfway down her throat. You face fuck her quickly, shooting your load down her throat as you cum."
            player.c "[player.orgasm_text]"
        wt_image banker_office_4
        "Bethany gets back to her feet, swallowing your cum as she does."
        bethany.c "I hope you don't mind me swallowing it. It makes too much of a mess if I let my clients cum anywhere else but in my mouth."
        $ bethany.hypno_blowjob_count += 1
        $ bethany.hypno_swallow_count += 1
        orgasm notify
      else:
        bethany.c "The numbers tell me who a valuable customer is. You don't do enough business here to qualify."
        player.c "You told me your customers were your most precious assets. Didn't you say you treat each and every one with care and attention?"
        bethany.c "The care and attention they deserve, yes. You don't do enough business here to deserve that much attention."
      $ bethany.bank_sex_act_today = True
      $ bethany.hypno_bj_request_count += 1
      $ title = "What do you want to discuss with her?"
      jump menu_banker_hypno
    "Tell her to date you" if not bethany.has_tag('asked_for_date_2'):
      add tags 'asked_for_date_2' to bethany
      player.c "You want to go on a date with me, Bethany. You and I should spend time together outside of the bank."
      bethany.c "Oh, I'm pretty much married to the bank! I mean, not really married of course. That would be silly. But between looking after the customers, and the corporate executives, and making sure I meet my key performance indicators each month. I just don't have time to date anyone. I'm sure you understand."
      $ title = "What do you want to discuss with her?"
      jump menu_banker_hypno
    "Just discuss her bank's services":
      pass
  return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
# Contact - Check In On Bethany at School
label bethany_contact_check_school:
  wt_image principal_office_1
  # $ bethany.training_session() ## no, this has no value
  "You give Hannah the Principal a call to find out how Bethany is working out at the school."
  hannah.c "It's going well. You can drop by if you want, but you'll need to wait until this evening, when her shift starts."
  $ title = "What do you want to do?"
  menu:
    "Go visit the school (Ends Day)":
      call forced_movement(school) from _call_forced_movement_707
      summon hannah
      wt_image banker_school_1_1
      "That evening, you drop by the school.  Hannah the Principal seems in a good mood when she greets you."
      hannah.c "Come to check in on Bethany are you?  I'm pleased to report she's working out well.  Follow me."
      summon bethany
      wt_image banker_school_1_2
      "She leads you to the boys' bathroom. Bethany the former banker is on her knees, scrubbing the floor."
      wt_image banker_school_1_3
      hannah.c "It's amazing how much of a mess boys can make, isn't it Bethany?  Make sure it's spotless for the start of class tomorrow."
      "Hannah turns away from the former banker to address you."
      hannah.c "We've been able to economize on janitorial expenses significantly since Bethany started working here.  Part of the savings, of course, is that Bethany is determined to work herself up starting at the bottom, so she's working long hard hours for significantly less than we used to pay our cleaners."
      wt_image banker_school_1_4
      "You're about to ask why Bethany's working with her breasts hanging out, when you notice the large plug extending from her ass.  Hannah follows your gaze."
      hannah.c "You're probably wondering about the butt plug.  It makes the breaks go more smoothly.  Speaking of which, Bethany, it's almost break time."
      wt_image banker_school_1_10
      "Hannah kneels down and removes the butt plug from her new employee."
      hannah.c "Go get in position, Bethany."
      wt_image banker_school_1_5
      "Bethany places a sign outside toilet stall, then crawls partway under the door."
      hannah.c "As I mentioned, we were able to downsize the cleaning staff significantly after Bethany joined us.  We've also been able to reduce costs for the remaining staff, especially the maintenance staff, by reducing their previous benefits and replacing them with access to Bethany."
      hannah.c "You don't mind offering your ass to help the school and further your career, do you Bethany?"
      bethany.c "No, Ma'am."
      wt_image banker_school_1_6
      hannah.c "The sign isn't strictly needed now that all the current staff know her ass is available to them during work breaks, but I think it sets the right mood.  I don't want anyone worrying about whether relieving themselves is an imposition on Bethany."
      wt_image banker_school_1_7
      "A large rough maintenance worker enters the bathroom.  He stops when he sees you."
      bethany_gus "Shit.  Is there a line up?"
      hannah.c "No, Gus.  I was just showing our visitor how we're coping despite our reduced financial resources.  Bethany's free if you want her."
      wt_image banker_school_1_8
      bethany_gus "Okay.  I'll get right back to fixing those lockers once I'm done."
      hannah.c "Take your time, Gus.  Bethany just started her break so there's no rush."
      "The big man spits on his fingers and jams the saliva into the former banker' waiting ass as he takes out his cock."
      wt_image banker_school_1_9
      "A moment later he's grunting his way to a quick orgasm inside his coworker's waiting bowels."
      bethany_gus "Uugghhhh.  Fuck that's good."
      wt_image banker_school_1_5
      "Gus pulls up his pants and hustles back to work."
      hannah.c "Doesn't look like anybody else needs you today, Bethany.  Seems you'll be able to relax for the rest of your break."
      "Bethany starts to crawl out from the stall, when Hannah turns to you."
      hannah.c "Unless, of course, you'd like a go?  Bethany, offer your former client your ass."
      wt_image banker_school_1_11
      "The former banker rolls over and raises her ass.  Gus has left a bit of a mess in there."
      bethany.c "Would you like my ass, Sir?"
      $ title = "What do you want to do?"
      menu menu_bethany_school:
        "Have a go" if not bethany.has_tag('school_cleaned'):
          wt_image banker_school_1_17
          "You don't mind the mess Gus left behind.  If anything, it may help lubricate her. You position your cock at Bethany's gaping hole, and slide easily inside her."
          if bethany.has_tag('sex_in_office'):
            "It's not your first time fucking her ass, but it's no less enjoyable for that. Hannah's presence, not to mention the circumstances, makes it a unique and pleasurable moment."
          else:
            "You wonder how many of her former clients have dreamed of the opportunity to enter her ass."
          wt_image banker_school_1_18
          "Bethany's clearly experienced at getting men to cum quickly when they're inside her.  She grips and squeezes your cock, milking you to orgasm even when you slow your pace.  Before long, you're emptying yourself inside her."
          player.c "[player.orgasm_text]"
          hannah.c "There, Bethany.  I think you pleased our visitor."
          bethany.c "Will I have to entertain visitors very often, Ma'am?  I thought I was only to entertain the staff?"
          hannah.c "Not often.  Just on special occasions.  Now thank our guest for finding you this great job."
          bethany.c "Thank you, Sir.  I appreciate the opportunity to start a new and more meaningful career."
          $ bethany.anal_count += 1
          orgasm notify
        "Tell her to clean herself out first" if not bethany.has_tag('school_cleaned'):
          player.c "Not with that mess in there.  Clean yourself out first."
          wt_image banker_school_1_12
          hannah.c "You heard the man.  Get over here and let's get you freshened up."
          "To your surprise, Hannah starts washing Bethany out."
          wt_image banker_school_1_13
          "It's not a gentle cleaning, and demonstrates the success the anal plug has had in making Bethany's ass an accommodating sheath for quick and frequent use."
          wt_image banker_school_1_14
          hannah.c "There.  She's all cleaned out for you."
          add tags 'school_cleaned' to bethany
          $ title = "What do you want to do?"
          jump menu_bethany_school
        "Fuck her now" if bethany.has_tag('school_cleaned'):
          wt_image banker_school_1_15
          "You move yourself into position behind her."
          player.c "Is her cunt available too, or just her ass?"
          hannah.c "Just her ass.  That's what we agreed to in your employment contract, wasn't it?"
          bethany.c "Yes, Ma'am."
          wt_image banker_school_1_16
          if bethany.has_tag('sex_in_office'):
            "It's not your first time fucking her ass, but it's no less enjoyable for that.  Hannah's presence, not to mention the circumstances, makes it a unique and pleasurable moment."
          else:
            "You wonder how many of her former clients have dreamed of the opportunity to enter her ass."
          "Bethany's clearly experienced at getting men to cum quickly when they're inside her.  She grips and squeezes your cock, milking you to orgasm even when you slow your pace.  Before long, you're emptying yourself inside her."
          player.c "[player.orgasm_text]"
          hannah.c "There, Bethany.  I think you pleased our visitor."
          bethany.c "Will I have to entertain visitors very often, Ma'am? I thought I was only to entertain the staff?"
          hannah.c "Not often.  Just on special occasions.  Now thank our guest for finding you this great job."
          bethany.c "Thank you, Sir.  I appreciate the opportunity to start a new and more meaningful career."
          $ bethany.anal_count += 1
          orgasm notify
        "No thanks":
          if bethany.has_tag('sex_in_office'):
            "You've had Bethany's ass before.  You're not in the mood for another go right now."
          player.c "No thanks.  I'll pass."
          hannah.c "Seems you'll be able to relax for the rest of your break after all.  What do you say?"
          wt_image banker_school_1_19
          "The former banker sits up and pulls herself together as she replies."
          bethany.c "Thank you, Sir.  I appreciate the opportunity to start a new and more meaningful career."
      "Your check up on Bethany complete, you head home."
      $ bethany.ready_for_visit_at_school = 2
      rem tags 'school_cleaned' from bethany
      change player energy by -energy_short notify
      call character_location_return(bethany) from _call_character_location_return_456
      call character_location_return(hannah) from _call_character_location_return_457
      call forced_movement(living_room) from _call_forced_movement_708
      end_day
    "Don't visit right now":
      pass
  wt_image current_location.image
  return

# Contact - Have Bethany the Banker Demonstrate Her Skills
label bethany_contact_demonstrate:
  # $ bethany.training_session()  ## no, this has no value
  if bethany.disclosed_pimping == 1:
    player.c "Time to show me if you have what it takes to work as one of my escorts, Bethany."
  elif bethany.disclosed_pimping == 2:
    player.c "Time to show me if you have what it takes to be a sexual concierge, Bethany."
  elif bethany.disclosed_pimping == 3:
    player.c "Time to show me if you have what it takes to be one of my 'hoes, Bethany."
  wt_image banker_test_1
  bethany.c "What do you want me to do?"
  player.c "Me.  At my house.  Get over here pronto."
  summon bethany
  wt_image banker_test_2
  "Bethany arrives at your door in no time, and you show her in."
  bethany.c "So, how do you want to do this?"
  player.c "Let's start with your attitude.  If I hire you, I'm your boss.  Is that how you addressed your boss at the bank?"
  bethany.c "No, Sir.  I'm sorry, Sir.  I should have asked how do you want to do this, Sir?"
  player.c "Let's start where every good bank assessment starts, with a review of your assets."
  wt_image banker_test_3
  bethany.c "Yes, Sir."
  "She pulls off her top ..."
  wt_image banker_test_4
  "... followed by her skirt and bra."
  player.c "Panties, too."
  wt_image banker_test_5
  bethany.c "Yes, Sir."
  player.c "Let's move on to the skills assessment.  Show me what you can do with your hands."
  wt_image banker_test_6
  bethany.c "Yes, Sir.  Your cock is beautiful, Sir."
  player.c "Save the flattery for the paying clients."
  bethany.c "Yes, Sir."
  player.c "Now your feet."
  wt_image banker_test_7
  bethany.c "Yes, Sir.  Do you want me to take off my nylons so you can feel my bare feet?"
  player.c "That's okay.  Leave them on."
  bethany.c "Does the nylon feel nice against your balls and cock?"
  player.c "I'll ask the questions, Bethany."
  bethany.c "Yes, Sir."
  player.c "Now your mouth."
  wt_image banker_test_8
  bethany.c "Yes, Sir."
  "Cupping your balls in her hands, she rubs them gently as she softly kisses the head and underside of your shaft."
  wt_image banker_test_9
  "After a bit more teasing, she leans in and takes your cock into her mouth. She alternates between bobbing her head down the full length of your shaft and sucking the tip of your cock as she strokes the shaft with her fist. Back and forth she alternates between the two, and it takes everything you have to keep yourself from cumming in her mouth."
  player.c "Cunt now."
  wt_image banker_test_8
  bethany.c "Do we have to do that, Sir?  I've always kept my pussy free for, you know, a boyfriend someday ... should I ever have time for one.  I'm sure the clients would be happy fucking my ass instead."
  player.c "I'm sure they'll be happy fucking your ass, too, but this job is all about being their girlfriend for a night.  It's not reasonable for you to expect them not to have access to their girlfriend's cunt."
  "Bethany's still sucking your cock, but you can see the hesitation in her eyes."
  player.c "Bethany, is there something you want to tell me?  You're not a virgin, are you?"
  "Her hands and mouth still pleasuring your cock, she nods shyly."
  player.c "You've made it this far in life, and never had intercourse with a man?"
  bethany.c "I've been saving that for someone super special."
  $ title = "Demand her virginity?"
  menu:
    "Yes, deflower her":
      player.c "How much do you want this job, Bethany?"
      bethany.c "A lot, Sir."
      player.c "Then give me your virginity, Bethany."
      bethany.c "Yes, Sir."
      wt_image banker_test_10
      "She lies back and spreads her legs.  A small tear escapes from the corner of one eye as you position the head of your cock at her opening.  You push forward until you encounter resistance."
      player.c "Get ready."
      "Slowly but firmly you push you way inside her, tearing the thin membrane of her hymen."
      bethany.c "Ohh!"
      player.c "It's done, Bethany.  You're a woman now."
      bethany.c "Yes, Sir."
      wt_image banker_test_11
      player.c "Time to learn to ride cock now like a woman, Bethany.  I imagine its different than riding a cock with your ass."
      bethany.c "Yes, Sir."
      player.c "Smile Bethany.  Remember, service with a smile."
      wt_image banker_test_12
      bethany.c "Yes, Sir."
      "It's a rather forced smile, but considering she just gave away the virginity she's been preserving for decades in order to win a job with you, you'll cut her some slack. You had planned on fucking her ass too, but knowing that she's given that away many times, while you're the first inside her cunt, you change your mind."
      wt_image banker_test_13
      "You reposition her onto her hands and knees and start pounding into her.  You're just about to release inside her when a thought occurs to you."
      player.c "Bethany, are you on birth control?"
      bethany.c "No, Sir."
      wt_image banker_test_14
      "Just in time, you pull out and splatter your load on her upturned ass. Bethany smiles as she feels your hot jizz land on her."
      player.c "[player.orgasm_text]"
      bethany.c "So what do you think, Sir?"
      $ player.virgin_count += 1
      $ bethany.sex_count += 1
      add tags 'took_virginity' to bethany
    "No, let her save it":
      player.c "I'm not sure that a virgin is going to make it in this business, Bethany.  Clients have expectations that I don't think you'll be able to fulfill."
      bethany.c "But I can fuck them with my ass.  It's super versatile.  Here, let me show you."
      wt_image banker_test_15
      "She climbs up on you and settles herself down on your hard shaft, sliding it into her ass more easily than you would have thought possible."
      bethany.c "I put some lube in before I came over.  I'm sure I can make the clients happy without having intercourse with them."
      "The feel of her riding her ass up and down your shaft definitely makes you happy."
      wt_image banker_test_14
      "You roll her over and thrust into her ass a few times, before pulling out and splattering your cum over her."
      player.c "[player.orgasm_text]"
      bethany.c "You could have cum in my bum if you'd preferred, Sir.  I don't mind that, other than the run to the toilet to let it out before it runs down my legs.  So what do you think, Sir?"
      $ bethany.anal_count += 1
  $ title = "What do you tell her?"
  menu:
    "Okay, you can work for me":
      call bethany_convert_whore from _call_bethany_convert_whore
    "Maybe she can help out the school" if hannah.lost_money_and_no_fix != 3 and hannah.lost_money_and_no_fix != 0:
      if hannah.waiting_on_banker == 1:
        player.c "Frankly, Bethany, an aging whore with limited experience fucking men isn't really the type of person I want representing my organization."
        player.c "Fortunately for you, I've spoken to Principal Hannah at the school, and she has some meaningful work for you.  Something that lets you make up for some of the trouble you caused."
        bethany.c "But, why did you make me go through with ..."
        player.c "I couldn't very well recommend you to Principal Hannah if I wasn't comfortable with your work ethic, now could I Bethany?"
        bethany.c "I guess not."
        if hannah.letter_re_terri == 11:
          $ bethany.torture_week = week
        else:
          $ bethany.ready_for_visit_at_school = 1
        $ bethany.ready_to_help_school = 3
        $ hannah.lost_money_and_no_fix = 3
        $ hannah.waiting_on_banker = 2
        rem tags 'available_for_school_visit' from hannah
      else:
        "Bethany mentioned losing the local school's money.  Maybe she can do something to help them out?  A visit to the principal may be in order."
        player.c "Frankly, Bethany, an aging whore with limited experience fucking men isn't really the type of person I want representing my organization."
        player.c "That said, I may still be able to get you some work.  Something that let's you make up for some of the trouble you caused.  I'll let you know once I've checked it out."
        $ bethany.ready_to_help_school = 2
    "Goodbye, Bethany":
      if bethany.has_tag('took_virginity'):
        player.c "I think you can leave now."
        bethany.c "But!  I did everything you asked!  I even gave you my ..."
        player.c "Your virginity?  Yes, thank you for that.  You fucked me as my banker, now I've fucked you.  Goodbye, Bethany."
      else:
        player.c "I think you can leave now."
        bethany.c "But!  I did everything you asked!  I ..."
        player.c "You fucked me as my banker, now I've fucked you.  Goodbye Bethany."
      if hannah.lost_money_and_no_fix == 1 or hannah.lost_money_and_no_fix == 2:
        if hannah.letter_re_terri == 12 or gloria.session > 6:
          pass
        else:
          $ hannah.action_contact_visit = None
          $ living_room.remove_action(hannah.action_contact_visit)
      $ bethany.ready_to_help_school = 4
  orgasm notify
  call character_location_return(bethany) from _call_character_location_return_458
  rem tags 'demonstrate_contact_open' from bethany
  return

# Contact - Getting back to her post Principal
label bethany_contact_getting_back:
  # $ bethany.training_session() ## no, not needed
  wt_image banker_test_1
  player.c "Hi Bethany.  I have news for you on the job front."
  $ title = "What do you tell her?"
  menu:
    "Still working on it":
      player.c "I'm still trying to decide if there's anything useful you can do."
      bethany.c "I can!  I promise you.  I can be super useful!"
    "She can help out the school" if hannah.waiting_on_banker == 1 and hannah.lost_money_and_no_fix != 3:
      player.c "Principal Hannah has some meaningful work for you.  Something that let's you make up for some of the trouble you caused."
      bethany.c "Oh thank you!"
      player.c "Don't thank me, thank her.  She's the one who thinks she can find a use for you."
      bethany.c "I'll make sure she knows she made the right choice."
      if hannah.letter_re_terri == 11:
        $ bethany.torture_week = week
      else:
        $ bethany.ready_for_visit_at_school = 1
        if hannah.letter_re_terri == 7:
          $ hannah.visit_week = week + 2
          add tags 'need_bethany_thank_you' to hannah
      $ bethany.ready_to_help_school = 3
      $ hannah.lost_money_and_no_fix = 3
      rem tags 'available_for_school_visit' from hannah
      $ hannah.waiting_on_banker = 2
    "Get her sex work":
      player.c "I've decided you can work for me after all."
      call bethany_convert_whore from _call_bethany_convert_whore_1
    "Goodbye Bethany":
      if bethany.has_tag('took_virginity'):
        player.c "Nobody has a use for a washed up former banker."
        bethany.c "But I did everything you asked!  I even gave you my ..."
        player.c "Your virginity?  Yes, thank you for that.  You fucked me as my banker, now I've fucked you.  Goodbye, Bethany."
      else:
        player.c "Nobody has a use for a washed up former banker."
        bethany.c "But I did everything you asked!  I ..."
        player.c "You fucked me as my banker, now I've fucked you.  Goodbye, Bethany."
      $ bethany.ready_to_help_school = 4
  return

# Contact - Pimp Out Bethany the Banker
label bethany_contact_pimp:
  $ bethany.training_session()
  $ bethany.whore_count += 1
  if bethany.whore_count == 1:
    if bethany.whore_name_number == 1:
      player.c "Ready to start your new career, Bethany?"
    else:
      player.c "Ready to start your new carer, '[bethany.whore_name]'?"
    wt_image banker_test_1
    bethany.c "Yes, Sir.  I'm totally psyched about it!"
    player.c "Good.  Enthusiasm is important in this business.  Your first customer is a visiting businessman.  I'll send you his hotel room.  Remember, service with a smile."
    bethany.c "I'll give it my all, Sir."
    wt_image banker_whore_1_1
    if bethany.whore_name_number == 1:
      "Bethany looks a little nervous as she arrives at the hotel.  The first day on a new job can be a bit nerve wracking."
    else:
      "'[bethany.whore_name]' looks a little nervous as she arrives at the hotel.  The first day on a new job can be a bit nerve wracking."
    wt_image banker_whore_1_2
    businessman "I hope you're not uncomfortable with me?"
    bethany.c "No, I'm super comfortable with you.  This is just a totally wild career change for me, and I don't want to mess up."
    businessman "Would it help if I told you exactly what I want you to do?"
    bethany.c "That would be amazing, yes."
    wt_image banker_whore_1_3
    businessman "Go get yourself changed.  When you're ready, get down on your hands and knees and crawl to me.  Can you do that for me?"
    bethany.c "Yes, of course."
    businessman "Give me a quick kiss first."
    wt_image banker_whore_1_4
    "Before she does anything else, Bethany counts the money the client has left for her.  Old banker habits die hard."
    wt_image banker_whore_1_5
    "Once she's satisfied that the financing is in order, she pulls off her clothes ..."
    wt_image banker_whore_1_6
    "... and puts on something a little more sultry ..."
    wt_image banker_whore_1_7
    "... complete with long black gloves."
    wt_image banker_whore_1_8
    "She looks very sophisticated as she gets down on all fours and crawls out to where her client is waiting for her."
    wt_image banker_whore_1_9
    "Seeing his exposed cock, she assumes she knows what he wants.  She crawls forward and impales her throat on his hard on."
    wt_image banker_whore_1_10
    businessman "Hold on.  Suck my balls before you start working on my cock."
    bethany.c "Sorry"
    wt_image banker_whore_1_11
    businessman "You look very nice, by the way.  It's always a pleasure to have a classy lady sucking my balls."
    bethany.c "Thank you.  You look very nice, too."
    wt_image banker_whore_1_12
    businessman "Let's skip the blow job and get right to the fucking.  Crawl up on the bed and show me your tits."
    wt_image banker_whore_1_13
    businessman "Nice.  Pinch your nipple."
    wt_image banker_whore_1_14
    businessman "Lie back and spread your legs.  I'm going to fuck you now."
    bethany.c "Put it in my ass, please."
    wt_image banker_whore_1_15
    businessman "Are you sure?  I'm not paying extra for that."
    bethany.c "I'm sure.  No extra cost."
    if bethany.has_tag('took_virginity'):
      "She may no longer be a virgin, but it seems Bethany is still more comfortable with strangers putting their cocks in her ass than in her pussy."
    else:
      "Bethany seems to have a preference for anal, and the client is not objecting."
    wt_image banker_whore_1_16
    businessman "Oh, that's nice!  You have a sweet ass for fucking."
    bethany.c "Thank you."
    wt_image banker_whore_1_17
    businessman "Roll over.  I want some leverage to really pound into you."
    wt_image banker_whore_1_18
    "Pinning her arms behind her back, he starts slamming into her ass faster and faster, until she feels the familiar warmth of hot jizz spurting into her bowels."
    businessman "Ohhhh yeaaahhhhhh!!!!!!"
    wt_image banker_whore_1_19
    "As instructed, she checks in with you when she leaves the hotel."
    player.c "How did your first day at the new job go, Bethany?"
    bethany.c "Great!  The client was super nice, and when we were finished, he seemed happy.  That almost never happened at the bank."
    player.c "Time to make me happy, Bethany, by sending me my cut of your take."
    bethany.c "Yes, Sir."
    $ player.whore_income += 50
  elif bethany.whore_count == 2:
    wt_image banker_test_1
    if bethany.whore_name_number == 1:
      player.c "I have your next client lined up, Bethany."
    else:
      player.c "I have your next client lined up, '[bethany.whore_name]'."
    player.c "He wants something special from you."
    bethany.c "What is it?  Do I need to bring anything with me?"
    player.c "Just a willing attitude and a sunny smile."
    bethany.c "Service with a smile.  Yes, Sir, I can do that."
    wt_image banker_whore_2_1
    if bethany.whore_name_number == 1:
      "As promised, Bethany arrives at his door with a smile on her face."
    else:
      "As promised, '[bethany.whore_name]' arrives at his door with a smile on her face."
    bethany_client_2 "Oh hey, you look nice.  Come on in and take off your clothes.  Leave the shoes on."
    wt_image banker_whore_2_2
    bethany_client_2 "Lie down on the sofa.  Relax.  Hey, these are nice sexy shoes."
    bethany.c "Thank you."
    wt_image banker_whore_2_3
    bethany_client_2 "I bet your feet are real tired from walking around in these.  Can I take them off?"
    bethany.c "Sure, go ahead."
    wt_image banker_whore_2_4
    bethany_client_2 "Oh yeah, your feet are warm and a little sweaty. I like that."
    "The client starts tonguing her feet, licking her sole, her toes, and between the toes.  Bethany starts to giggle."
    bethany.c "That tickles!"
    wt_image banker_whore_2_5
    bethany.c "How about I put my feet where you really want them?"
    bethany_client_2 "Oh yeah, that's hot!"
    wt_image banker_whore_2_6
    bethany_client_2 "Put your feet together. I want to fuck them."
    wt_image banker_whore_2_7
    "The client thrusts his cock back and forth between her soft soles, his breathing getting heavier and heavier."
    bethany_client_2 "Quick, get your bra off."
    wt_image banker_whore_2_8
    "The client leans forward, bending her knees back with his weight as he continues to thrust his cock back and forth between her soles."
    wt_image banker_whore_2_9
    bethany_client_2 "Aahhhhhh!!!!"
    "His jizz spurts out from between her feet, splattering over her tits and belly."
    wt_image banker_test_1
    "She calls you on her way home."
    player.c "Did you help the client with his special needs?"
    bethany.c "I think so!  He seemed very happy.  I love how in this job I don't have to worry if the client makes a mess.  I'll send your percentage to you."
    $ player.whore_income += 50
  elif bethany.whore_count == 3:
    wt_image banker_test_1
    if bethany.whore_name_number == 1:
      player.c "Another special client request, Bethany.  And this time you do need to bring something."
    else:
      player.c "Another special client request, '[bethany.whore_name]'.  And this time you do need to bring something."
    bethany.c "What will I need?"
    player.c "A bikini."
    wt_image banker_whore_3_1
    bethany_client_3 "Oh great!  You're already dressed.  Come on in."
    wt_image banker_whore_3_2
    if bethany.whore_name_number == 1:
      "The client shows Bethany into a room with a big mat on the floor."
    else:
      "The client shows '[bethany.whore_name]' into a room with a big mat on the floor."
    bethany_client_3 "Have you ever done any wrestling?"
    bethany.c "No"
    bethany_client_3 "Don't worry, its really easy.  We just need to get you oiled up first."
    wt_image banker_whore_3_3
    bethany_client_3 "Kneel down."
    if bethany.whore_name_number == 1:
      "The client empties a full bottle of oil over Bethany, lifting up her swim suit to make sure it coats her entire skin, even the little bit that's covered by her bikini."
    else:
      "The client empties a full bottle of oil over '[bethany.whore_name]', lifting up her swim suit to make sure it coats her entire skin, even the little bit that's covered by her bikini."
    bethany_client_3 "Now we wrestle.  I try to pin you and you try to pin me."
    wt_image banker_whore_3_4
    if bethany.whore_name_number == 1:
      "Bethany spins around, catching the client by surprise as she pulls down his pants and runs her mouth along his cock."
    else:
      "'[bethany.whore_name]' spins around, catching the client by surprise as she pulls down his pants and runs her mouth along his cock."
    bethany_client_3 "No fair!  You're supposed to try and pin me, not distract me."
    wt_image banker_whore_3_5
    "Flipping onto her back, she strokes his erect cock with her oiled feet."
    bethany_client_3 "Oh, you're a dirty fighter you are.  That's it, I'm taking you down."
    wt_image banker_whore_3_6
    "True to his word, he grabs her by the legs and pushes her backwards, pinning her shoulders against the mat with his weight."
    wt_image banker_whore_3_7
    "Then grabbing her breast in one hand, he worms his other arm around her torso and flips her over ..."
    wt_image banker_whore_3_8
    "... pulling her up to her knees once he has her face down."
    bethany_client_3 "Go ahead, try to escape."
    "As she tries to move away he pulls her hips backwards, pinning her in place by shoving his cock in her ass."
    wt_image banker_whore_3_9
    "He leans forward, pushing her flat against the mat with his weight as he pins her arms behind her back."
    bethany_client_3 "Good try, but you lose.  I wouldn't normally fuck your ass, but you were fighting dirty, so I think it's only fair that I get to play dirty too, don't you agree?"
    bethany.c "Yes, go ahead."
    wt_image banker_whore_3_10
    bethany_client_3 "Roll over so I have a better view of my cock moving in and out of your ass.  Oh, that's nice.  Fuck, yeah.  Oh ... Ohhh ... Ohhhhh!!!!"
    wt_image banker_whore_3_11
    player.c "How did it go?  Does your new career still remind you of working in the bank?"
    bethany.c "Yes, except this time instead of the bank making up rules the client can't understand, the client was making up rules I didn't understand."
    player.c "That doesn't sound very fun."
    bethany.c "It was fine.  The client was super sweet and he was happy that he won his game.  The clients never used to win at the bank.  This was a nice change."
    if bethany.whore_name_number == 1:
      $ player.whore_income += 50
    else:
      "Bethany knows what's she's doing, and is generating a steady stream of interest online. There's no longer any need for you to spend time managing her schedule."
      "You can afford to reduce your take as you won't need to spend any energy after this, you can just collect your percentage from her at the end of each week.Just make sure to check in on her every once in a while, to make sure she doesn't get into any trouble."
      $ bethany.whore_count = 5
      $ player.whore_income += 25
  elif bethany.whore_count == 4:
    wt_image banker_test_1
    player.c "Ready for your next assignment?"
    bethany.c "Absolutely!  Where is it?"
    player.c "My house."
    bethany.c "Your house?"
    player.c "I'll explain when you get here."
    summon bethany
    wt_image banker_whore_4_17
    player.c "Come in Bethany.  You might be interested to know that your online profile attracted a lot of attention from a particular type of client."
    wt_image banker_whore_4_1
    bethany.c "What type of client?"
    player.c "Ones who knew you in your previous line of work. As you can imagine, the financial condition you left most of those former clients in didn't provide them the means to afford your services in your new work.  Its taken a few weeks for them to get back on their feet to the point where we could arrange this reunion.  Follow me."
    wt_image banker_whore_4_2
    bethany.c "Curtis?"
    mr_lang "Don't Curtis me, bitch.  Show some respect.  It's Mr. Lang to you.  That's the least you can do after you cost me my life savings."
    wt_image banker_whore_4_3
    bethany.c "Mr. Lang, I'm..."
    mr_lang "You're what?  A whore?  Yes, I know that.  That's why I'm here."
    wt_image banker_whore_4_4
    mr_lang "To spend some time with the woman who cost me the shirt off my back."
    wt_image banker_whore_4_5
    mr_lang "Yet here you stand in all these fancy clothes."
    bethany.c "I lost everything too!  I've had to rebuild, to get new work."
    wt_image banker_whore_4_6
    mr_lang "Work as what?"
    bethany.c "As an honest woman!"
    mr_lang "As a whore."
    bethany.c "Yes, as an honest, hard working whore!  I'm trying to be a better person.  I'm sorry for the harm I did before."
    wt_image banker_whore_4_7
    mr_lang "Are you sorry?  Show it."
    bethany.c "Mr. Lang, I'm so very, very sorry that I recommended you put your money with our bank. I'm sorry that I cost you your life savings. I'm sorry that I ever worked for that horrible, evil organization."
    bethany.c "Let me make it up to you.  Let me give you some honest value for your hard earned money."
    wt_image banker_whore_4_8
    player.c "I'm afraid it's not just Mr. Curtis, Bethany."
    player.c "You recognize Mr. Harris, Mr. Bukowski, and Mr. Everton. They all lost their life savings in your fund as well."
    player.c "In fact, all of them are still struggling so much that they had to pool their resources in order to afford your services for the night."
    player.c "In light of your heartfelt apology to Mr. Curtis, however, I presume you won't have any problem in providing these gentlemen with 4 for 1 pricing for today?"
    bethany.c "No, of course not."
    player.c "Good. Then gentlemen, she's all yours. Do with her as you please for the next hour."
    wt_image banker_whore_4_9
    "At first they wait their turns for Bethany's attention."
    wt_image banker_whore_4_10
    "Then growing impatient with waiting, they encourage her to pick up her pace."
    wt_image banker_whore_4_11
    "Soon they're all clamoring for a piece of her at once."
    wt_image banker_whore_4_12
    "When two cocks arrive at her ass at the same time, they discover to their surprise that they don't need to take turns there either..."
    wt_image banker_whore_4_13
    "...her ass stretches wide enough to allow them both simultaneous entrance."
    if bethany.has_tag('took_virginity'):
      wt_image banker_whore_4_14
      "You're particularly pleased to see the recent virgin allow her cunt to be used to get through the backlog of waiting cocks more quickly."
    wt_image banker_whore_4_15
    "Before long, the backlog has been worked through, and all the cocks have been looked after."
    wt_image banker_whore_4_16
    player.c "It's not easy, sometimes, putting in an honest day of hard work."
    bethany.c "I didn't mind.  Those men deserved some fair value for their money, after what they've been through."
    player.c "That's the spirit. No more group discounts, though.  That was a one time special, a way for me to test that you really are a changed woman. We charge full price per customer for the use of your body going forward."
    bethany.c "Thank you Sir.  That makes me feel like a valued employee."
    $ player.whore_income += 25
    call character_location_return(bethany) from _call_character_location_return_459
  change player energy by -energy_short notify
  return

# Contact - Check on Whore
label bethany_check_whore:
  #if bethany.has_tag("whore") and bethany.whore_count > 3:
  wt_image banker_test_1
  if bethany.disclosed_pimping == 1:
    player.c "How's my favorite professional escort?"
  elif bethany.disclosed_pimping == 2:
    player.c "How's my favorite sexual concierge?"
  elif bethany.disclosed_pimping == 3:
    player.c "How's my favorite professional 'ho?"
  bethany.c "Am I really your favorite?  I'm sure you say that to all your employees."
  player.c "You know I mean it when I say it to you.  How's business?"
  if bethany.whore_name == 1:
    bethany.c "I wish you hadn't used my real name.  I keep getting hired by former clients from the bank."
    player.c "So you're getting lots of work and you're making amends.  Isn't that a good thing?"
    bethany.c "I guess, but my ass is super sore.  I can't even sit down."
  else:
    bethany.c "Super great!  Clients are always so much happier than when I worked at the bank."
  player.c "Just make sure you send me my percentage, '[bethany.whore_name]'."
  bethany.c "I'm keeping a full accounting.  I'll send you my spreadsheet each week."
  player.c "Good.  If you get into trouble, you let me know. I'll look out for you."
  bethany.c "Thank you!  You always make me feel like a valued employee."
  $ bethany.whore_lost_countdown = 7
  return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_bethany:
  "You should save the butt plug for a client."
  return

# Give Chastity Belt
label give_cb_bethany:
  "You should save this for a current client."
  return

# Give Dildo
label give_di_bethany:
  "You should save this for a current client."
  return

# Use Fetch Toy
label use_ft_bethany:
  "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_bethany:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_bethany:
  "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_bethany:
  "You should save this for a current client."
  return

# Give Love Potion
label give_lp_bethany:
  "Best to save this for a paying client."
  return

# Give Transformation Potion
label give_tp_bethany:
  "Best to save this for a paying client."
  return

# Use Water Bowl
label use_wb_bethany:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_bethany:
  "You should try this on someone else."
  return

########### TIMERS ###########
## Common Timers
# Start Day
label bank_start_day:
  ## Bank Opens
  if week >= 12 and day == 1 and bank.status == 0:
    wt_image bank_flyer
    "{i}Monday morning, there's a flyer left at your door.{/i}"
    "{i}Now open!  Global Trust Bank is pleased to announce the opening of our newest branch.  Ask us about our loan and investment options!  Conveniently located on the lobby level of the North Office Tower.{/i}"
    $ bank.status = 1
    $ office_tower.name = "Bank Office Tower"
    $ office_tower.connection_bank = office_tower.add_connections(bank)
    wt_image current_location.image
  ## Bank Loan Weekly Checks
  if day == 1:
    ## Loan Interest Owed
    if player.money < 0 and bank.has_tag('loan_in_place'):
      "You were charged [bank.loan_interest] interest for your outstanding loan at the end of the week."
      $ player.money -= bank.loan_interest
    ## Foreclosure Warning
    if player.money < -500 and bank.has_tag('loan_in_place'):
      $ bank.foreclosure_warning += 1
      if bank.foreclosure_warning == 1:
        wt_image letter
        "You receive a letter in the mail. It's from the bank."
        "{i}Dear Sir, It has come to our attention that your income last week was insufficient to pay the interest on your loan.  As a result, you are overdrawn on your loan.  If you do not rectify this, we will be forced to foreclose on your house.{/i}"
      elif bank.foreclosure_warning == 2:
        wt_image letter
        "You receive a letter in the mail. It's from the bank."
        "{i}Dear Sir, You are still overdrawn on your loan.  Please rectify this immediately or we will take the necessary steps to foreclose on your house.{/i}"
      elif bank.foreclosure_warning == 3:
        wt_image letter
        "You receive a letter in the mail. It's from the bank."
        "{i}{b}FINAL WARNING{/b}  Financial regulations require us to issue three warnings prior to foreclosing on the security provided against your loan.  If you do not bring your loan balance back under -500 by the end of the week, we will seize your house.{/i}"
        sys "You won't be able to continue your career as the Wife Trainer if you don't have a house to operate out of.  You had better rectify this quickly."
      elif bank.foreclosure_warning == 4:
        wt_image police_door
        "There's a knock on your door.  It's the Sheriff."
        wt_image moving_van
        "You try to talk the Sheriff out of it, but a court has issued a foreclosure notice against your house in favor of the bank.  The moving van packs up your things and carts them off.  You're sent packing after it."
        sys "{b}Your career as the Wife Trainer has ended ignominiously with you being kicked out of your own house.  Next time, try not to over do it on the debt.{/b}"
        ### END THE GAME ###
        jump end_game
    else:
      $ bank.foreclosure_warning = 0
  return

# End Day
label bethany_end_day:
  rem tags 'already_visited_today' from bethany
  return

# End Week
label bethany_end_week:
  ## Whores or Prof Domme
  if player.whore_count > 0 or hannah.has_tag('domme'):
    if not player.has_tag('whores_once'):
      add tags 'whores_once' to player
  ## Whores Lost
  if bethany.has_tag('whore') and bethany.whore_count > 3:
    $ bethany.whore_lost_countdown -= 1
    $ bethany.whore_departure_count += 1
    if bethany.whore_name_number == 1 and bethany.whore_departure_count >= 4:
      wt_image banker_test_1
      "There's a message for you from Bethany."
      bethany.c "Hi Sir!  I'm going away for a year. Isn't that super surprising news!"
      bethany.c "One of our bank executives saw my online profile and recognized me.  Somehow it seems he escaped our bank crash without losing all his money."
      bethany.c "He's hiring me to go overseas for a year and look after our portfolio managers.  Apparently they've set up some sort of offshore hedge fund and it's crazy stressful work.  So he wants me to help keep them relaxed and entertained."
      bethany.c "Don't worry, I remember our deal. I'm sending you 250 as your cut of my fees.  Bye bye!"
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all chararacter name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      # call convert(bethany, 'unavailable')
      $ bethany.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with bank closure and investments may not be needed going forward; should ideally be cleaned up
      call unconvert(bethany,"whore") from _call_unconvert_42
      $ bethany.whore_name_number = 0
      $ player.whore_income += 250
    elif bethany.whore_lost_countdown <= 0:
      "You haven't checked on Bethany for quite a while. She didn't send your cut this week and she's nowhere to be found. Whether she skipped town or got into trouble, you never find out."
      # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all chararacter name actions before setting status to 'unavailable'
      # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
      # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
      #call convert(bethany, 'unavailable')
      $ bethany.status = 'unavailable' # went this route as uncertain as to whether some of her tags associated with bank closure and investments may not be needed going forward; should ideally be cleaned up
      call unconvert(bethany,"whore") from _call_unconvert_43
      $ bethany.whore_name_number = 0
    else:
      $ player.whore_income += 25
  ## Investment Fund Bankruptcy
  if bank.investment_weeks_paid >= 8 and bank.has_tag('investments_in_place'):
    wt_image phone_1
    "Your phone is ringing."
    wt_image banker_phone_1
    "It's your personal banker, Bethany."
    bethany.c "I'm so sorry. I hate to bother you at home, but we have a bit of a problem."
    player.c "What sort of problem?"
    bethany.c "A tulip problem. Right out of the blue, it seems like prices for tulips in Amsterdam started to go down."
    bethany.c "Anyway, our investment fund was fully invested in tulips and heavily leveraged and it turns out falling tulip prices were not good for the fund."
    player.c "I thought your fund managers were smart?"
    bethany.c "Oh, they are!  Wicked smart!  They got out just in time."
    player.c "Oh, good. So my capital was saved?"
    bethany.c "Well, no. They didn't get the fund's money out. They got themselves out. Out of the country. No one knows where they are now."
    player.c "How much did I lose?"
    bethany.c "Everything"
    player.c "Everything???"
    bethany.c "I know! It sucks. I lost all my money too, because all my bonuses went in there. So did all my other customers besides you."
    if hannah.letter_re_terri != 10 and not hannah.has_tag('doll'):
      bethany.c "Even the local school lost all its money."
      $ hannah.lost_money_and_no_fix = 1
      if hannah.letter_re_terri == 12 or hannah.letter_re_terri == 7:
        "Sounds like Hannah the School Principal may have gotten herself into some financial trouble.  Perhaps you should consider visiting her to discuss her money woes."
      else:
        "Sounds like the School Principal may be in some financial troubles.  Perhaps you should pay the school a visit."
      add tags 'available_for_school_visit' to hannah
    bethany.c "And it gets worse."
    player.c "I doubt it."
    bethany.c "Our board of directors put all the bank's capital in the fund too. So now our bank is bankrupt, and I'm out of a job."
    if bethany.disclosed_pimping > 0:
      bethany.c "So since I no longer have a job, and all my life savings went 'poof' with our fund, I was wondering.{nw}"
      if bethany.disclosed_pimping == 1:
        extend "  Do you think I could work as one of your escorts?"
      elif bethany.disclosed_pimping == 2:
        extend "  Do you think I could work as one of your sexual concierges?"
      else:
        extend "  Do you think I could work as one of your 'hoes?"
      player.c "What makes you think you could do this sort of work?"
      bethany.c "I've worked for the bank since I graduated university, so I've pretty much been a whore my entire working life."
      $ title = "What do you say?"
      menu menu_bank_bankrupt:
        "I don't work with your type" if not bethany.has_tag('bank_bankrupt_dont_work'):
          wt_image banker_phone_2
          player.c "I run a class operation.  I don't work with your type."
          bethany.c "It's not my fault!  I didn't want to work for a bank.  I was young and naive.  When I finished university, I had no work skills and a giant student debt.  I needed to do something - anything! - to make money."
          bethany.c "You have no idea how hard this has been on me.  I didn't know anything about the real world until I started working here."
          bethany.c "The bank executives, they're ... they're monsters!   When they look at you, it's like they're seeing straight through your clothes ... and into your wallet."
          add tags 'bank_bankrupt_dont_work' to bethany
          $ title = "What do you say?"
          jump menu_bank_bankrupt
        "I couldn't trust you" if bethany.has_tag('bank_bankrupt_dont_work') and not bethany.has_tag('bank_bankrupt_cant_trust'):
          player.c "I'd never be able to trust someone who comes from your background."
          bethany.c "Please!  I'm tired of feeling dirty every time I cash my paycheck.  I'm ready for honest work."
          bethany.c "I promise, I won't cheat you or your customers.  I'll let them have everything they pay for."
          bethany.c "Please, give me a second chance to do something good with my life.  I promise I won't mess it up."
          add tags 'bank_bankrupt_cant_trust' to bethany
          $ title = "What do you say?"
          jump menu_bank_bankrupt
        "No":
          player.c "No, I won't have someone like you bringing down the reputation of my whole organization."
          bethany.c "Don't judge me!!  You don't know what it's been like for me!"
          player.c "I know no matter how bad things got, I would never stoop so low as to work for a bank."
        "You'll have to prove you have the skills" if not bethany.has_tag('bank_bankrupt_prove'):
          player.c "You'll need to prove to me you have the skills necessary to satisfy my clients."
          if bethany.has_tag('bj_in_office'):
            if bethany.has_tag('sex_in_office'):
              bethany.c "But I already blew you in the office.  And let you fuck me in the ass.  Remember?  So you've seen my skills in action."
            else:
              bethany.c "But I already blew you in the office.  Remember?  So you've seen my skills in action."
            add tags 'bank_bankrupt_prove' to bethany
            $ title = "What do you say?"
            jump menu_bank_bankrupt
          else:
            if bethany.has_tag('sex_in_office'):
              bethany.c "But I already let you fuck me in the ass.  Remember?  So you've seen my skills in action."
              add tags 'bank_bankrupt_prove' to bethany
              $ title = "What do you say?"
              jump menu_bank_bankrupt
            else:
              bethany.c "Okay.  I understand.  Let me know when you want me to demonstrate what I know."
              $ bethany.ready_to_help_school = 1
              add tags 'demonstrate_contact_open' to bethany
        "I need to see more" if bethany.has_tag('bank_bankrupt_prove'):
          player.c "I'm going to need to see a lot more than that, Bethany, before I can be sure you won't disappoint my clients."
          bethany.c "Okay.  I understand.  Let me know when you want me to demonstrate what I know."
          $ bethany.ready_to_help_school = 1
          add tags 'demonstrate_contact_open' to bethany
        "Okay, you can work for me":
          player.c "Okay, Bethany, I'll let you work."
          call bethany_convert_whore from _call_bethany_convert_whore_2
        "Maybe she can help out the school" if hannah.letter_re_terri != 10 and not hannah.has_tag('doll'):
          "Bethany mentioned losing the local school's money.  Maybe she can do something to help them out?  A visit to the principal may be in order."
          player.c "I may be able to get you some work, Bethany.  Something that let's you make up for some of the trouble you caused.  I'll let you know once I've checked it out."
          $ bethany.ready_to_help_school = 2
        "I need to think about it":
          $ bethany.ready_to_help_school = 1
      rem tags 'bank_bankrupt_dont_work' 'bank_bankrupt_cant_trust' 'bank_bankrupt_prove' from bethany
    else:
      bethany.c "Anyway, sorry to bother you at home about this, but it couldn't wait until I get into the office on Monday, because apparently I don't have an office to go to anymore."
      bethany.c "I hope you have a great weekend!"
    $ bethany.fixed_location = None
    $ bank.status = 2
    $ bank.name = "First Nationalized Bailout Bank"
    $ player.money = 0
    $ player.min_money = 0
    rem tags 'investments_in_place' 'loan_in_place' from bank
  ## Investments
  if player.money >= 500:
    if bank.has_tag('investments_in_place'):
      if player.money >= 1000:
        $ bank.investment_weeks_paid += 1
        $ player.investment_income += 50
        $ bank.investment_total_income_to_date += 50
      elif player.money >= 500:
        $ bank.investment_weeks_paid += 1
        $ player.investment_income += 25
        $ bank.investment_total_income_to_date += 25
    else:
      if bank.notice_about_investments == 0 and bank.status == 1:
        wt_image letter
        "A letter arrives for you. It's from the Global Trust Bank."
        "{i}Dear Sir, You have been pre-qualified to participate in our exclusive investment fund, available only to successful people like yourself.{/i}"
        "{i}To learn more, please speak to one of our account managers at your local branch.  We are conveniently located at the main level of the north Office Tower downtown.{/i}"
        "{i}From, Your Service with a Smile team!{/i}"
        $ bank.notice_about_investments = 1
  ## Open up checking on her at school
  if bethany.ready_for_visit_at_school == 1 and bethany.action_contact_check_school is None:
    $ bethany.action_contact_check_school = living_room.add_action("Check in on Bethany at the School", label = bethany.short_name + "_contact_check_school", context = "_contact_other", condition = "bethany.can_be_interacted and bethany.ready_for_visit_at_school == 1")
  return

## Character Specific Timers
# Convert Character to Whore
label bethany_convert_whore:
  call convert(bethany,"whore") from _call_convert_21
  bethany.c "That's great!  What should I use for my new professional name?"
  $ title = "What do you think?"
  menu menu_bethany_rename:
    "Pick a name for her":
      $ bethany.whore_name = renpy.input(_("What should her working name be?"))
      $ title = "Are you sure you want her to call herself '[bethany.whore_name]'?"
      menu:
        "Yes":
          pass
        "No, pick something else":
          $ title = "What should her working name be?"
          jump menu_bethany_rename
      $ bethany.whore_name_number = 2
    "Make her use her real name":
      player.c "We're going to use your real name, Bethany."
      bethany.c "But don't people normally adopt a professional name, to hide their identity?"
      player.c "Often that's the case, yes.  But you're trying to turn over a new leaf and become an honest woman.  Let's start with truth in advertising.  How does this sound for an online profile?"
      player.c "'Bethany. Former banker. Past her prime physically. Mediocre sex skills. Desperate for money. No requests too humiliating. Service with a Smile.'"
      player.c "You can deliver on that, right Bethany?  The service with a smile part, I mean."
      bethany.c "I guess so."
      player.c "I'm your boss now, Bethany.  Is that how you responded to your boss at the bank?"
      bethany.c "No, Sir.  I should have said yes, I can do that."
      player.c "That's better."
      $ bethany.whore_name_number = 1
  if bethany.whore_name_number == 2:
    player.c "I'll let you know when I have your first customer lined up, '[bethany.whore_name]'."
  else:
    player.c "I'll let you know when I have your first customer lined up"
  "It shouldn't take you more than few days to generate some business for her new career."
  $ bethany.action_contact_pimp = living_room.add_action("Pimp Out Bethany the Banker", label = bethany.short_name + "_contact_pimp", context = "_contact_other", condition = "bethany.can_be_interacted and bethany.has_tag('whore') and bethany.whore_count < 4")
  $ bethany.whore_lost_countdown = 7
  $ bethany.ready_to_help_school = 4
  return

########### ROOMS ###########
# BANK
label bank_examine:
  "The new Global Trust Bank branch is clean and modern.  Their slogan is 'Service with a Smile'.  Who wouldn't want to bank here?"
  return

# OBJECT - BANK BRANCH
# Enter Bank
label bank_no_access:
  if bank.status == 1:
    if bethany.has_tag('already_visited_today'):
      "You've already spoken to Bethany today.  She's busy now with other clients.  Perhaps you could try dropping back tomorrow."
      break_movement
      wt_image office_tower.image
  elif bank.status == 2:
      "The door is locked. The old bank signs have been taken down and a new one put up. It reads 'First Nationalized Bailout Bank ... Reopening in a later version of this game'."
      break_movement
      wt_image office_tower.image
  return

label bank_enter:
  call bethany_talk from _call_bethany_talk
  return

label bank_exit:
  return

label bethany_investment_get_out:
  if bethany.has_tag('hypnotized_now'):
    wt_image banker_office_4
  else:
    wt_image banker_office_11
  bethany.c "That's so disappointing."
  "She hands you over some paperwork for you to sign, canceling your involvement with her bank's investment fund, then she shows you to the door."
  rem tags 'investments_in_place' from bank
  # $ bank.investments_in_place = 0
  return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
