## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package janice name "Janice, the Lawyer" description "Allows Janice to be a minor character." dependencies core
register janice_pregame 10 in core as "Janice the Lawyer"

# Pregame
label janice_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Janice the Lawyer (Nina Hartley)")]

    ## Character Definition
    janice = Person(Character("Woman in Club", who_color="#7300A8", what_color="#7300A8", window_background = gui.dialogue_background_dark_font_color), "janice", cut_portrait = True, prefix = "", suffix = "")
    janice.trigger_phrase = "pussy slave pussy slave"

    # Other Characters
    # Green
    #receptionist = Character("Receptionist", who_color="#00FF00", what_color="#00FF00") # replaced by full character
    janicereceptionist = Person(Character("Receptionist", who_color="#00FF00", what_color="#00FF00"), "janicereceptionist", cut_portrait = True, prefix = "The", suffix = "")

    ## Actions
    janice.action_talk = janice.add_action("Talk to her", label="_talk", condition = "janice.can_be_interacted")
    janice.action_suggest = janice.add_action("Suggest you go somewhere private", label="_suggest", condition = "janice.can_be_interacted and current_location == club and player.lawyer_office_visit_count > 0 and not janice.has_tag('in_dog_cage')")
    janicereceptionist.action_wait = janicereceptionist.add_action("Wait for Janice", label="_wait", condition = "player.has_tag('waiting_for_janice')")

    ## Tags
    # Common Character Tags
    janice.add_tags('can_be_in_club', 'no_hypnosis', 'likes_girls')
    janicereceptionist.add_tags('no_hypnosis')

    # Character Specific Tags
    # N/A

    ## Locations
    # Lawyer's Office
    janice_office = Location("The Law Office of Hotspur Barnes LLP", 'jo', cut_portrait = True, enter_break_labels = ['jo_no_access'], enter_labels = ['jo_enter'], exit_labels = ['jo_exit'], area = 'offices')
    office_tower.action_visit_janice = office_tower.add_action("Visit the Law Office of Hotspur Barnes LLP", context = '_elevator', label = "janice_office_visit")
    janice_office.connection_ot = janice_office.add_connections(office_tower)
    # janice.location = janice_office # janice actually isn't in her office from a game perspective at any time
    janicereceptionist.location = janice_office
    janicereceptionist.fixed_location = janice_office

    ## Other

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    #start_day_labels.append('janice_start_day', priority = 5) ## not used so disabled
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    #janice.add_stats_with_value('temporary_count') #auto-added for all characters
    janice.add_stats_with_value('hypno_anal_count', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_orgasm_count', 'hypno_sex_count', 'hypno_swallow_count', 'random_number')

    # Character Specific Variables
    janice.add_stats_with_value('discuss_barista', 'frigid_encounter_status', 'rewards_pending', 'tried_hypnosis')
    player.add_stats_with_value('lawyer_office_visit_count')
    janice_reward_reason_list = ['donna', 'elsa']
    janice_reward_description_list = ['club_access']
    janice_special_reward_description_list = []

    # Player Examine Phrases
    player.add_examine_phrase("player.has_tag('lawyer_on_retainer')", "You have Janice the Lawyer on retainer.")

    ######## EXPANDABLE MENUS #######
    ## Janice Reward Menu
    janice_reward_menu = ExpandableMenu("What do you want?", cancelable = False)
    janice.choice_janice_reward_menu_club_access = janice_reward_menu.add_choice("Club Access", "janice_reward_club_access", condition = "not player.has_tag('club_access')")
    janice.choice_janice_reward_menu_nothing = janice_reward_menu.add_choice("Nothing", "janice_reward_nothing")

  return

# Display Portrait
# CHARACTER: Display Portrait
label janice_update_media:
    if current_location == club:
        if janice.has_tag('in_dog_cage'):
            $ janice.change_image('lawyer_club_12')
        else:
            $ janice.change_image('lawyer_club_1')
    return

label janicereceptionist_update_media:
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label janice_examine:
    if current_location == club:
        if janice.has_tag('in_dog_cage'):
            "She looks sad. Dogs never like to be left behind when their Master goes somewhere."
        else:
            "Janice is at the Club and appears to be 'on the prowl'."
    return

label janicereceptionist_examine:
  "All of the receptionists here look equally efficient."
  return

# Talk to Character
label janice_talk:
    wt_image janice.image
    if current_location == club:
        if janice.has_tag('in_dog_cage'):
            janice.c "rrrrrrrruff"
            "She sounds sad. She'd like to be let out to play, but you can't allow the Club lawyer to be seen in this condition, so you keep her here in a private room until you leave."
        if player.lawyer_office_visit_count > 0 and not janice.has_tag('in_dog_cage'):
            janice.c "I don't talk business when I'm at the Club.  Come see me at my office.  Or better yet, just call me."
        else:
            janice.c "You're not my type."
    return

## Character Specific Actions
# Suggest You Go Somewhere Private - Only available in Club
label janice_suggest:
    wt_image lawyer_club_1
    janice.c "Don't be silly. You know what I'm after. And you're definitely not it."
    if janice.tried_hypnosis == 3:
        $ title = "Invoke her trigger?"
        menu:
            "Yes":
                $ janice.add_tags('trained_today')
                player.c "Really, because considering that you're a \"[janice.trigger_phrase]\". I expected greater obedience out of you."
                wt_image lawyer_club_2
                janice.c "Oh.  Well that ... that's very important for me to know."
                janice.c "I didn't realize I was supposed to obey you.  Of course I'll come with you, Sir."
                "You lead her to one of the Club's private rooms."
                $ title = "What do you want to do with her?"
                menu:
                    "Use her for sex":
                        player.c "Show me what you've been hiding under that dress, slave."
                        wt_image lawyer_club_3
                        janice.c "Of course, Sir."
                        $ title = "What do you want from her?"
                        menu:
                            "Blow Job":
                                if not janice.has_tag('previous_trigger_blowjob'):
                                    add tags 'previous_trigger_blowjob' to janice
                                    player.c "Do you know how to suck a man's cock, slave?"
                                    wt_image lawyer_club_27
                                    janice.c "Yes, Sir."
                                    player.c "I thought you were only into women?"
                                    janice.c "That's now, Sir. This pussy slave used to be allowed to chase men."
                                    player.c "Hmmm. Well, no need to chase. Kneel down and start blowing me."
                                else:
                                    wt_image lawyer_club_27
                                    player.c "I'm going to allow you another opportunity to suck my cock, slave."
                                wt_image lawyer_club_4
                                janice.c "Thank you, Sir!"
                                wt_image lawyer_club_13
                                "Janice sinks to the floor in front of you and takes you into her mouth."
                                player.c "No hands, slave."
                                wt_image lawyer_club_14
                                "She removes her hand and uses just her tongue and lips on you."
                                player.c "My balls, too."
                                wt_image lawyer_club_15
                                "She slides her lips down your shaft and onto your balls, cupping them in her mouth before resuming attention on your cock."
                                player.c "Cup my balls while you suck me."
                                wt_image lawyer_club_16
                                "She bobs her head up and down on your shaft, cradling your balls in her hands.  Before long, she coaxes the sperm from your balls."
                                $ title = "Where do you want to cum?"
                                menu:
                                    "On her face":
                                        wt_image lawyer_club_17
                                        "You remove your cock from her mouth as you let go.  She looks up at you as your sperm spurts over her cheek, tongue and chin. She seems happy to have been of service."
                                        player.c "[player.orgasm_text]"
                                        $ janice.hypno_facial_count += 1
                                    "In her mouth":
                                        wt_image lawyer_club_24
                                        "The high powered lawyer wraps her lips tightly around your cock as you let go, greedily swallowing every drop of cum your balls pump into her mouth."
                                        player.c "[player.orgasm_text]"
                                        $ janice.hypno_swallow_count += 1
                                $ janice.hypno_blowjob_count += 1
                            "Sex":
                                player.c "Lie down on your back, slave.  I'm going to fuck you."
                                wt_image lawyer_club_28
                                janice.c "Yes, Sir.  Thank you, Sir!!"
                                wt_image lawyer_club_18
                                if not janice.has_tag('previous_trigger_sex'):
                                    add tags 'previous_trigger_sex' to janice
                                    "As you slide yourself into her, she's surprisingly wet."
                                    player.c "Do you like having a cock inside you?"
                                    janice.c "Yes, Sir."
                                    player.c "I thought you were only into women?"
                                    janice.c "This pussy slave is only allowed to chase bisexual young blonde women, Sir. I have to reject all other suitors. Except, of course, when I'm serving my proper role as slave."
                                    player.c "Does that leave you sexually frustrated, slave?"
                                    janice.c "Quite often, Sir."
                                else:
                                    player.c "Have you had a cock inside you since the last time I fucked you?"
                                    janice.c "No, Sir."
                                    player.c "Are you happy to have mine inside you again?"
                                    janice.c "Yes, Sir.  Very.  This pussy slave has been very, very horny and not able to get any relief."
                                wt_image lawyer_club_29
                                player.c "Okay then.  Get up on top of me and show me how you like to fuck cock."
                                wt_image lawyer_club_19
                                "She does.  With enthusiasm. It takes a lot of self-control to prevent her from milking an orgasm out of you quickly."
                                wt_image lawyer_club_26
                                "To slow things down, you put her on her knees and re-enter her from behind as she groans happily.  In this position, you're better able to control the pace of the fucking, and prolong your orgasm."
                                wt_image lawyer_club_20
                                "It's clear from her heavy breathing that Janice is close to orgasm herself."
                                player.c "Would you like to cum, slave?"
                                janice.c "Yes, Sir.  Please?"
                                $ title = "Let her cum?"
                                menu:
                                    "Yes":
                                        player.c "When you feel my cum spurt inside you, you may orgasm.  When you do, you will thank me profusely for the orgasm."
                                        janice.c "Oh thank you thank you thank you, Sir!"
                                        wt_image lawyer_club_25
                                        "That thank you was before the orgasm.  When you finally let yourself go, the real thank yous start."
                                        player.c "[player.orgasm_text]"
                                        janice.c "Aahhhhhhh!!!  Thank you for the orgasm, Master! Oh thank you! Thank you for the orgasm, Master!"
                                        "You wonder how long it's been since Marilyn let her cum with a cock inside her?"
                                        $ janice.hypno_orgasm_count += 1
                                    "No":
                                        player.c "Pussy slaves shouldn't cum from having a cock inside them, slave."
                                        janice.c "No, Sir."
                                        wt_image lawyer_club_30
                                        player.c "[player.orgasm_text]"
                                        "You empty your load inside her, leaving the high powered lawyer panting silently, her cunt twitching, desperate to cum but unable to do so without permission."
                            "Anal":
                                player.c "Lie down on your back, slave.  I'm going to fuck you."
                                wt_image lawyer_club_25
                                janice.c "Yes, Sir.  Thank you, Sir!!"
                                wt_image lawyer_club_31
                                player.c "I'm not going to fuck your pussy, though, pussy slave.  I'm putting my dick up your ass."
                                "The disappointment in her voice as she replies is accompanied by a little whimper as push yourself inside her."
                                janice.c "Yes, Sir  ...  nnnn"
                                wt_image lawyer_club_21
                                "Perhaps you should have used more lube. Then again, the fit is comfortable for you. Her comfort isn't relevant. You don't, however, want to look at that grimace on her face the whole time you ream her."
                                player.c "Slave, you enjoy having cock in your ass. Do you understand?"
                                wt_image lawyer_club_22
                                janice.c "Yes, Sir."
                                "That's not a lot better. Humorous in its own right, but not a lot better."
                                wt_image lawyer_club_23
                                "You turn her around and face her away from you. That's better."
                                wt_image lawyer_club_32
                                "In this position, you're able to pleasurably fuck her ass for as long as you like. Towards the end, you think she might genuinely be enjoying it too."
                                player.c "[player.orgasm_text]"
                                $ janice.hypno_anal_count += 1
                        wt_image lawyer_club_33
                        player.c "Get dressed and go home and relax now, slave. You won't remember anything we did here today, but you will remember having a great time at the Club."
                        janice.c "Yes, Sir.  I had a great time at the Club today."
                        rem tags 'in_club_now' from janice
                        call character_location_return(janice) from _call_character_location_return_665
                        wt_image current_location.image
                        orgasm notify
                    "Humiliate her":
                        "As fun as it would be to parade the little lawyer slave around the Club, Marilyn would react poorly to you exposing Janice in that way. You settle for humiliating her in private."
                        wt_image lawyer_club_3
                        "You have her remove her clothes ..."
                        wt_image lawyer_club_4
                        "... and squat down as you prepare her outfit for the evening. The room you're in has a number of play items for the use of patrons."
                        wt_image lawyer_club_5
                        "You have her strip completely and kneel on a rug. From the room's box of toys you select a tiara, because it looks cute on her, and a dog collar and leash, because that looks cuter still."
                        player.c "You're my bitch tonight, Janice. Do you understand?"
                        janice.c "Yes, Sir."
                        player.c "That means you don't get to speak.  Lawyers get to speak.  Bitches only bark.  Understand?"
                        janice.c "Rrrufff"
                        wt_image lawyer_club_6
                        player.c "Come nuzzle my foot and show me how happy you are to be my bitch."
                        janice.c "Ruff, ruff."
                        wt_image lawyer_club_7
                        "You order a bottle from the bar, and have it placed on the table. When the server leaves, you order Janice to get up on the table with it."
                        player.c "Here, girl. Get up here and put this inside you. Get the cover nice and wet and warm."
                        wt_image lawyer_club_8
                        player.c "Now take off the top.  Use your teeth like a good little bitch opens things."
                        wt_image lawyer_club_9
                        player.c "Here's a bowl for you. Drink up."
                        wt_image lawyer_club_10
                        player.c "Now stay right there while I enjoy my drink.  Does it feel good to be of service to your Master?"
                        janice.c "Rrrufff"
                        player.c "More fun than giving legal advice, would you say?"
                        janice.c "Rrufff?"
                        wt_image lawyer_club_11
                        player.c "Unfortunately, I can't stay and play with you all night. I have other people to chat with. Get in here, girl."
                        wt_image lawyer_club_12
                        player.c "Stay here. I'll come let you out before I leave."
                        janice.c "rrrrrrrruff"
                        "She sounds sad. Dogs never like to be left behind when their Master goes somewhere."
                        add tags 'in_dog_cage' to janice
                        change player energy by -energy_short notify
                wt_image current_location.image
            "No":
                pass
    return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Former Character
label janice_contact:
    wt_image lawyer_desk_1
    if janice.rewards_pending > 0:
        call for_call_labels(label_list = [i + '_janice_reward_introduction' for i in janice_reward_reason_list]) from _call_for_call_labels_51
        rem tags 'special_reward' from janice
    if not janice.has_tag('asked_about_marilyn'):
        $ title = "Ask her about the woman in the hall?"
        menu:
            "Yes":
                player.c "Who was that woman who was leaving just as I arrived for my first visit. The rude one."
                "Janice smiles."
                janice.c "We wouldn't be the go to law firm for the city's elite if we shared the names of our clients, would we?"
                janice.c "However, on reflection, I think perhaps my client might want to meet you. So I'll make an exception in this case."
                janice.c "Her name is Marilyn. Don't ask what she does. She's a powerful woman, the type of power that comes from having influence among the ... shall we say less savory elements of society?"
                janice.c "She owns a building downtown. Tell her I sent you, and she'll grant you an interview. Who knows, perhaps you'll be able to offer her something of interest to her."
                add tags 'asked_about_marilyn' to janice
                $ marilyn.change_full_name("", "Marilyn", "")
                # Add Marilyn's Building Connections
                $ marilyn_building.connection_do = marilyn_building.add_connections(downtown)
                $ downtown.connection_mb = downtown.add_connections(marilyn_building)
                $ janice.temporary_count = 0
            "No":
                pass
    # ask for rep gain
    if player.has_tag('rep_needed') and player.has_tag('lawyer_on_retainer'):
        if not player.has_tag('rep_from_lawyer'):
            player.c "Janice, I've run into a bit of a snag in my business. I need a boost to my Reputation. Anything my lawyer could do to help?"
            janice.c "I can place a few calls.  Leave it with me."
            rem tags 'rep_needed' from player
            add tags 'rep_from_lawyer' to player
            change player reputation by 1 notify
        else:
            player.c "Janice, I've run into a another business snag. Can you help boost my Reputation again?"
            janice.c "Sorry.  We're a law office, not a PR firm. I've done as much as I can on that front."
    # ask about Sam: would have been more consistent with new system to move this to Sam's script, but follows the Rags' system  of using janice's variables so left here
    if janice.discuss_barista == 1:
        wt_image lawyer_desk_1
        "You tell Janice about the newly single and very blonde Sam the Barista."
        janice.c "You say she's a lesbian? I have no interest in meeting some gold-digging carpet muncher who's just after me for my money. I'm looking for a nice blonde housewife who's bi-curious."
        player.c "That's a strangely specific compulsion you have, you know?"
        $ janice.discuss_barista = 2
    ## now call all talk options for Janice related to other characters
    call for_call_labels(label_list = [p.short_name + '_janice_talk_option' for p in get_people(tagged_with_all=['janice_talk_option_possible'])]) from _call_for_call_labels_27
    "You have nothing more to discuss with Janice at this time."
    wt_image current_location.image
    return

label donna_janice_reward_introduction:
    if janice.has_tag('donna_reward_pending'):
        $ janice.rewards_pending -= 1
        rem tags 'donna_reward_pending' from janice
        if not player.has_tag('lawyer_on_retainer'):
            janice.c "I had quite a fun time with Donna.  Welcome to the law firm of Hotspur Barnes ... client."
            player.c "So how does this work?  If I need you ..."
            janice.c "You call me, and I sort it out."
            "Congratulations!  You now have a high powered lawyer on retainer."
            add tags 'lawyer_on_retainer' to player
        else:
            janice.c "Thank you for setting me up with [donna.name].  You're proving quite adept at helping me ... locate suitable acquaintances."
            call for_call_labels(label_list = [i + '_janice_reward_description' for i in janice_reward_description_list]) from _call_for_call_labels_52
            if janice.has_tag('reward_possible'):
                rem tags 'reward_possible' from janice
                call expandable_menu(janice_reward_menu) from _call_expandable_menu_115
            else:
                "You already had Janice on retainer and you're already a member of the Club, so Janice had nothing further to offer you as a reward."
    return

label elsa_janice_reward_introduction:
    if janice.frigid_encounter_status == 2:
        $ janice.rewards_pending -= 1
        $ janice.frigid_encounter_status = 3
        if not player.has_tag('lawyer_on_retainer'):
            janice.c "I had quite a fun time with Elsa.  Welcome to the law firm of Hotspur Barnes ... client."
            player.c "So how does this work?  If I need you ..."
            janice.c "You call me, and I sort it out."
            "Congratulations!  You now have a high powered lawyer on retainer."
            add tags 'lawyer_on_retainer' to player
        else:
            janice.c "Thank you for setting me up with [elsa.name].  You're proving quite adept at helping me ... locate suitable acquaintances."
            call for_call_labels(label_list = [i + '_janice_reward_description' for i in janice_reward_description_list]) from _call_for_call_labels_53
            if janice.has_tag('reward_possible'):
                rem tags 'reward_possible' from janice
                call expandable_menu(janice_reward_menu) from _call_expandable_menu_116
            else:
                "You already had Janice on retainer and you're already a member of the Club, so Janice had nothing further to offer you as a reward."
    return

label club_access_janice_reward_description:
    if not player.has_tag('club_access'):
        add tags 'reward_possible' to janice
        janice.c "I'm a member of a very exclusive Club.  I could sponsor you for membership, if you'd like?  I believe you'd fit right in."
    return

label janice_reward_club_access:
    janice.c "I'm so pleased you'll be joining us.  I'll let the Club know to expect you."
    add tags 'club_access' to player
    return

label janice_reward_nothing:
    player.c "Thanks for the offer, but I'll pass."
    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_janice:
  "If she's like many lawyers, her butt may be too tight for it to fit."
  return

# Give Chastity Belt
label give_cb_janice:
  "Even if you did, what good would that do you?"
  return

# Give Dildo
label give_di_janice:
  "It's safe to assume she's looked after her own needs on this front."
  return

# Use Fetch Toy
label use_ft_janice:
  "At the moment, she's not ready to be your puppy dog."
  return

# Give Jewelry
label give_jwc_janice:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_janice:
  "At the moment, she's not ready to be your puppy dog."
  return

# Give Lingerie
label give_li_janice:
  "It's a nice thought, but she earns more in a day than you do in a month.  Your little gift will not impress her."
  return

# Give Love Potion
label give_lp_janice:
  janice.c "Don't buy me drinks.  I'm not going home with you."
  if janice.has_tag('trigger_implanted'):
    "In her trance state, you could likely get her to drink it, but why? At best Marilyn's safeguards prevent the potion from working. At worst it messes with Marilyn's work, after which she messes with you."
  return

# Give Transformation Potion
label give_tp_janice:
  janice.c "Don't buy me drinks.  I'm not going home with you."
  if janice.has_tag('trigger_implanted'):
    "In her trance state, you could likely get her to drink it, but why? At best Marilyn's safeguards prevent the potion from working. At worst it messes with Marilyn's work, after which she messes with you."
  return

# Use Water Bowl
label use_wb_janice:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Give Ring of Secuality
label give_rs_janice:
    "Her sexuality is too weirdly specific for the ring to have any effect on her."
    return


# Use Will Tamer
label use_wt_janice:
  "You're not persuasive enough to argue the lawyer into your collar."
  if janice.has_tag('trigger_implanted'):
    "In her trance state, you could likely get her to wear it, but why?  At best Marilyn's safeguards prevent the Will-Tamer from working. At worst it messes with Marilyn's work, after which she messes with you."
  return

## Receptionist
# Give Butt Plug
label give_bp_janicereceptionist:
    wt_image janicereceptionist.image
    "She's not allowed to accept gifts from clients, not even thoroughly inappropriate gifts."
    return

# Give Chastity Belt
label give_cb_janicereceptionist:
    wt_image janicereceptionist.image
    "What part of her polite, but firm 'no' suggested she has a problem with sleeping around?"
    return

# Give Dildo
label give_di_janicereceptionist:
    wt_image janicereceptionist.image
    "She's not allowed to accept gifts from clients, not even thoroughly inappropriate gifts."
    return

# Use Fetch Toy
label use_ft_janicereceptionist:
    wt_image janicereceptionist.image
    "She may play fetch for the law partners, but sadly she won't do so for you."
    return

# Give Jewelry
label give_jwc_janicereceptionist:
    "Save this as a gift for [chelsea.name]."
    return

# Use Leash
label use_le_janicereceptionist:
    wt_image janicereceptionist.image
    "Who knows what she does after hours. At the office, however, she doesn't seem to be the leash-wearing kind."
    return

# Give Lingerie
label give_li_janicereceptionist:
    wt_image janicereceptionist.image
    "She's not allowed to accept gifts from clients, not even thoroughly inappropriate gifts."
    return

# Give Love Potion
label give_lp_janicereceptionist:
    wt_image janicereceptionist.image
    "No, thank you.  I'm not thirsty."
    return

# Give Transformation Potion
label give_tp_janicereceptionist:
    wt_image janicereceptionist.image
    "No, thank you.  I'm not thirsty."
    return

# Use Water Bowl
label use_wb_janicereceptionist:
    "She has a glass of water beside her on her desk.  Sadly, she prefers to drink out of that rather than a bowl on the floor."
    return

# Use Will Tamer
label use_wt_janicereceptionist:
    wt_image janicereceptionist.image
    "She looks so cute and proper in her business attire, a leather collar would complete her ensemble perfectly.  Sadly, she doesn't see it that way."
    return

########### TIMERS ###########
## Common Timers
# Start Day
#label janice_start_day: ## not used
    #pass
    #return

# End Day
label janice_end_day:
    rem tags 'in_club_now' 'in_dog_cage' from janice
    call character_location_return(janice) from _call_character_location_return_666
    return

label janicereceptionist_end_day:
    call character_location_return(janicereceptionist) from _call_character_location_return_667
    return

# End Week
label janice_end_week:
    pass
    return

label janicereceptionist_end_week:
    pass
    return



## Club and Stage Labels

label janice_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if janice.has_tag('in_club_now'):
            $ janice.location = club
    else:
        $ janice.random_number = renpy.random.randint(1, 10)
        if janice.random_number > 6:
            $ janice.location = club
            add tags 'in_club_now' 'gloria_club_talk_possible' to janice
    return

label janice_club_send_home:
    #if janice.has_tag('in_dog_cage'):
    #    rem tags 'in_club_now' 'in_dog_cage' from janice # note: she won't be in the club if you come back today as you release her when you leave
    call character_location_return(janice) from _call_character_location_return_668 # note don't move her to her office as she's never actually in her office, you just reach her through her receptionist
    return



## Club President Wife Content

label janice_gloria_club_talk_option:
    gloria.c "Our Club lawyer? She's top notch. We never have any problems. Janice makes sure of that."
    gloria.c "And when my husband says that anything that happens here stays here ... well, let's just say that Janice is very good at making sure members understand the consequences of stepping out of line."
    if player.lawyer_office_visit_count == 0:
        gloria.c "You should hire her to be your lawyer, if you can. She's very, very expensive, but well worth it. Her firm's located in the big office tower downtown."
        $ janice.change_full_name("", "Janice", "the Lawyer")
    return


## Character Specific Timers
# N/A

########### ROOMS ###########
# Janice the Lawyer's Office
label jo_examine:
    "The busy reception area at the exclusive Hotspur Barnes law office."
    return

label jo_no_access:
  return

label janice_office_visit:
    call move_to(janice_office) from _call_move_to_5
    return

label jo_enter:
  summon janicereceptionist no_follows
  wt_image jo_image
  "You enter the busy reception area of the exclusive Hotspur Barnes law office.  One of the receptionists greets you."
  wt_image janicereceptionist.image
  janicereceptionist.c "How may I help you?"
  if player.lawyer_office_visit_count == 0:
    $ title = "What do you say?"
    menu menu_jo_1:
      "In many ways, I'm sure" if not player.has_tag('jo_flirt_1'):
        janicereceptionist.c "I'm very busy, Sir. I don't have time to flirt."
        if player.has_tag('supersexy'):
          extend " No matter how good looking you are."
        add tags 'jo_flirt_1' to player
        janicereceptionist.c "So how may I help you?"
        jump menu_jo_1
      "There are some documents here for me to sign":
        player.c "My real estate agent, Geri, told me there's some paperwork here for me to sign."
        janicereceptionist.c "About a house purchase, Sir?  Normally one of our junior lawyers would handle that, but you must be someone special.  Our senior partner, Janice, has those documents.  If you'll just have a seat, Janice will be able to see you shortly."
        add tags 'waiting_for_janice' to player
        wt_image current_location.image
      "I think I'm just lost":
        player.c "I think I'm lost."
        janicereceptionist.c "The elevators to the lobby are over there, Sir.  Have a good day."
        call forced_movement(office_tower) from _call_forced_movement_209
  else:
    $ title = "What do you say?"
    menu menu_jo_2:
      "I'm here to see Janice":
        player.c "I'm here to see Janice."
        if janice.has_tag('in_club_now'):
            janicereceptionist.c "I'm sorry, but she's not here now."
            "She's probably still at the Club. Maybe try again tomorrow. Or just call her when you get home. She may answer her phone."
            call forced_movement(office_tower) from _call_forced_movement_210
        else:
            janicereceptionist.c "I'll let her know you're here. Please have a seat."
            add tags 'waiting_for_janice' to player
            wt_image current_location.image
      "I'm here to see you" if not player.has_tag('jo_flirt_2'):
        janicereceptionist.c "Please don't waste your time or mine, Sir."
        if player.has_tag('supersexy'):
          extend " I'm sure lots of women would appreciate your attention. Perhaps you should visit one of them?"
        add tags 'jo_flirt_2' to player
        janicereceptionist.c "So how may I help you?"
        jump menu_jo_2
      "I keep getting lost":
        player.c "I think I'm lost."
        janicereceptionist.c "The elevators to the lobby are over there, Sir.  Have a good day."
        call forced_movement(office_tower) from _call_forced_movement_211
  return

label janicereceptionist_wait:
  rem tags 'jo_flirt_1' 'jo_flirt_2' 'waiting_for_janice' from player
  rem tags 'no_hypnosis' from janice # to allow subsequent tests
  $ player.lawyer_office_visit_count += 1
  if player.lawyer_office_visit_count == 1:
    $ janice.change_full_name("", "Janice", "the Lawyer")
    wt_image lawyer_office_reception
    "You wait in the reception area for your appointment."
    change player energy by -energy_very_short notify
    "It takes a while."
    wt_image janicereceptionist.image
    "Eventually the receptionist summons you."
    janicereceptionist.c "Janice will see you now."
    summon marilyn
    wt_image marilyn_lawyer_office_2
    "As the receptionist leads you to Janice's office, a haughty looking woman walks briskly down the hall. The receptionist steps deftly out of her way. Too late, you realize the woman expected you to step aside for her too. She bumps into you, then turns back to look at you, clearly annoyed."
    wt_image marilyn_lawyer_office_1
    if player.has_tag('wealthy'):
      marilyn.c "Another example of money and good sense not going together, I see."
    else:
      marilyn.c "Do they take anybody on as clients here now?  I thought this was supposed to be an elite law firm."
    wt_image marilyn_lawyer_office_3
    "As quickly as she arrived, she disappears, with a final sneer in your direction."
    call character_location_return(marilyn) from _call_character_location_return_669
    janicereceptionist.c "I'm sorry, Sir. Some of Janice's clients are very important people and used to getting their way. Janice is right in here, please."
    $ janicereceptionist.dismiss(False)
    summon janice no_follows
    wt_image lawyer_desk_1
    "The receptionist escorts you into a well appointed office, then leaves. The woman sitting behind the desk is presumably Janice."
    janice.c "Hello, Mr. Wife Trainer. How can I help you today?"
    player.c "What did you call me?"
    janice.c "Wife Trainer. That's what you call yourself online, isn't it?"
    player.c "How did you know that?"
    if player.has_tag('wealthy'):
      janice.c "We wouldn't be a very good law firm if we didn't keep tabs on people of means, would we?  Particularly one with as interesting a new business as yours."
    else:
      janice.c "We did a background check on you as part of our standard procedures when completing the paperwork for your realtor.  That's a very interesting new business you've started."
    janice.c  "No legal troubles at the moment, but you might want to be prepared for trouble down the road.  A husband unsatisfied with your work is just the most obvious of many beehives you might stir up."
    $ title = "What do you do?"
    menu menu_wait_1:
      "Hypnotize her" if player.can_hypno(janice) and janice.tried_hypnosis == 0:
        player.c "Janice, would you look at this for me."
        call focus_image from _call_focus_image_83
        player.c "I am going to talk with you, Janice, and you are going to listen to me."
        player.c "Listen to me now, Janice.  Listen to me.  Listen to my voice and nothing else, Janice.  Only my voice.  Only my voice now."
        wt_image lawyer_desk_1
        janice.c "I'm a busy woman, and I'm sure you're a busy man. What was it you wanted to ask me about?"
        "How strange. Janice didn't fall under your trance, but she seems to be completely unaware that you tried to hypnotize her. It's as if someone else has locked her mind, preventing anyone else access, while making her ignore the act of being hypnotized."
        $ janice.tried_hypnosis = 1
        jump menu_wait_1
      "Ask about the woman in the hallway" if not janice.has_tag('asked_about_marilyn'):
        player.c "Who was that woman who was leaving just as I arrived?  The rude one."
        "Janice smiles."
        janice.c "We wouldn't be the go to law firm for the city's elite if we shared the names of our clients, would we?"
        janice.c "However, on reflection, I think perhaps my client might want to meet you?  So I'll make an exception in this case."
        janice.c "Her name is Marilyn.  Don't ask what she does.  She's a powerful woman, the type of power that comes from having influence among the ... shall we say less savory elements of society?"
        janice.c "She owns a building downtown.  Tell her I sent you, and she'll grant you an interview.  Who knows, perhaps you'll be able to offer her something of interest to her?"
        add tags 'asked_about_marilyn' to janice
        $ marilyn.change_full_name("", "Marilyn", "")
        # Add Marilyn's Building Connections
        $ marilyn_building.connection_do = marilyn_building.add_connections(downtown)
        $ downtown.connection_mb = downtown.add_connections(marilyn_building)
        jump menu_wait_1
      "Ask about hiring her" if not janice.has_tag('asked_about_hiring'):
        player.c "So what do I do if I need your services?  Call you?"
        "Janice smiles."
        if player.has_tag('wealthy'):
          janice.c "It would be our honor to represent a man of your means.  I wonder, though, if in return for our services, you might be able to assist me with a ... predilection?"
          player.c "A predilection?"
          janice.c "An appetite for young blonde women, married, straight but bi-curious.  There are hundreds of gold digging carpet munchers in this town that would happily be my sugar baby.  I prefer the innocent, happily married type."
          player.c "That's a very specific appetite."
          janice.c "One I believe you may be uniquely positioned to assist me with.  Send a cute one my way, and I'd be quite grateful.  Though of course we're prepared to represent you and assist you in any future legal difficulties you find yourself inm regardless."
          "Congratulations!  You now have a high powered lawyer on retainer.  One with an unusual request for assistance."
          add tags 'lawyer_on_retainer' to player
        else:
          janice.c "At that point, I suggest you hire the first lawyer who will take your call.  I only work for clients who have us on retainer."
          player.c "And what does that cost?"
          janice.c "Far more than you can afford, I'm afraid.  My hourly wage would bankrupt you very quickly."
          player.c "So why are you handling the paperwork for my house purchase?  Geri can't afford those fees, either."
          janice.c "Selfish reasons.  I have a ... predilection ... that you may be able to assist me with."
          player.c "A predilection?"
          janice.c "An appetite for young blonde women, married, straight but bi-curious.  There are hundreds of gold digging carpet munchers in this town that would happily be my sugar baby.  I prefer the innocent, happily married type."
          janice.c "Send a cute one my way, and I'll waive our retainer and assist you in any future legal difficulties you find yourself in."
          player.c "That's a very specific appetite."
          janice.c "One I believe you may be uniquely positioned to assist me with.  Call me when you're able to help."
        $ janice.frigid_encounter_status = 1
        add tags 'asked_about_hiring' to janice
        # if player.has_tag('temp_content_accepted_elsa'):
        #   "Elsa would have been perfect for Janice the Lawyer."
        #   $ title = "What about Janice the Lawyer?"
        #   menu:
        #     "Pretend you sent Elsa to her":
        #       add tags 'lawyer_on_retainer' to player
        #       "You now have Janice the Lawyer on retainer."
        #     "Find someone else to send to Janice":
        #       pass
        $ janice.action_contact = living_room.add_action("Contact " + janice.full_name, label = janice.short_name + "_contact", context = "_contact_other", condition = "janice.can_be_interacted")
        jump menu_wait_1
      "Sign the documents and leave":
        "You've spent enough time with Janice for today.  You sign the paperwork and leave."
        add tags 'signed_house_docs' to player
        add tags 'no_hypnosis' to janice
        call character_location_return(janice) from _call_character_location_return_670
        call character_location_return(janicereceptionist) from _call_character_location_return_671
        wt_image office_tower.image
        call forced_movement(office_tower) from _call_forced_movement_212
        change player energy by -energy_very_short notify
  else:
    $ janice.temporary_count = 1
    wt_image lawyer_office_reception
    change player energy by -energy_very_short notify
    "You wait in the reception area for your appointment.  It takes a while."
    wt_image janicereceptionist.image
    "Eventually the receptionist summons you and shows you to Janice's office."
    janicereceptionist.c "Janice will see you now."
    $ janicereceptionist.dismiss(False)
    summon janice no_follows
    wt_image lawyer_desk_1
    if janice.rewards_pending > 0:
      $ janice.temporary_count = 0
      call for_call_labels(label_list = [i + '_janice_reward_introduction' for i in janice_reward_reason_list]) from _call_for_call_labels_54
      rem tags 'special_reward' from janice
    else:
      janice.c "I'm a busy woman. What did you want to see me about?"
    if not janice.has_tag('asked_about_marilyn'):
      $ title = "Ask her about the woman in the hall?"
      menu:
        "Yes":
          player.c "Who was that woman who was leaving just as I arrived for my first visit. The rude one."
          "Janice smiles."
          janice.c "We wouldn't be the go to law firm for the city's elite if we shared the names of our clients, would we?"
          janice.c "However, on reflection, I think perhaps my client might want to meet you?  So I'll make an exception in this case."
          janice.c "Her name is Marilyn.  Don't ask what she does.  She's a powerful woman, the type of power that comes from having influence among the ... shall we say less savory elements of society?"
          janice.c "She owns a building downtown. Tell her I sent you, and she'll grant you an interview.  Who knows, perhaps you'll be able to offer her something of interest to her."
          add tags 'asked_about_marilyn' to janice
          $ marilyn.change_full_name("", "Marilyn", "")
          # Add Marilyn's Building Connections
          $ marilyn_building.connection_do = marilyn_building.add_connections(downtown)
          $ downtown.connection_mb = downtown.add_connections(marilyn_building)
          $ janice.temporary_count = 0
        "No":
          pass
    if not janice.has_tag('asked_about_hiring'):
      $ title = "Ask about hiring her?"
      menu:
        "Yes":
          player.c "So what do I do if I need your services?  Call you?"
          "Janice smiles."
          janice.c "At that point, I suggest you hire the first lawyer who will take your call.  We only work for clients who have us on retainer."
          player.c "And what does that cost?"
          janice.c "Far more than you can afford, I'm afraid.  This is an elite law firm.  My hourly wage would bankrupt you very quickly."
          player.c "So why did you agree to see me then?"
          janice.c "Selfish reasons.  I have a ... predilection ... that you may be able to assist me with."
          player.c "A predilection?"
          janice.c "An appetite for young blonde women, married, straight but bi-curious.  There are hundreds of gold digging carpet munchers in this town that would happily be my sugar baby.  I prefer the innocent, happily married type."
          janice.c "Send a cute one my way, and I'll waive our retainer and assist you in any future legal difficulties you find yourself in."
          player.c "That's a very specific appetite."
          janice.c "One I believe you may be uniquely positioned to assist me with.  Call me when you're able to help."
          $ janice.frigid_encounter_status = 1 # note: old Rags coding that predates the 'asked_about_hiring' tag, but still used in Elsa's script
          add tags 'asked_about_hiring' to janice
          $ janice.action_contact = living_room.add_action("Contact " + janice.full_name, label = janice.short_name + "_contact", context = "_contact_other", condition = "janice.can_be_interacted")
          $ janice.temporary_count = 0
        "No":
          pass
    # ask for rep gain
    if player.has_tag('rep_needed') and player.has_tag('lawyer_on_retainer'):
      if not player.has_tag('rep_from_lawyer'):
        player.c "Janice, I've run into a bit of a snag in my business.  I need a boost to my Reputation.  Anything my lawyer could do to help?"
        janice.c "I can place a few calls.  Leave it with me."
        rem tags 'rep_needed' from player
        add tags 'rep_from_lawyer' to player
        change player reputation by 1 notify
      else:
        player.c "Janice, I've run into a another business snag.  Can you help boost my Reputation again?"
        janice.c "Sorry.  We're a law office, not a PR firm.  I've done as much as I can on that front."
      $ janice.temporary_count = 0
    # ask about Sam: would have been more consistent with new system to move this to Sam's script, but follows the Rags' system  of using janice's variables so left here
    if janice.discuss_barista == 1 and janice.has_tag('asked_about_hiring'):
      "You tell Janice about the newly single and very blonde Sam the Barista."
      janice.c "You say she's a lesbian?  I have no interest in meeting some gold-digging carpet muncher who's just after me for my money.  I'm looking for a nice blonde housewife who's bi-curious."
      player.c "That's a strangely specific compulsion you have, you know?"
      $ janice.discuss_barista = 2
    ## now call all talk options for Janice related to other characters
    call for_call_labels(label_list = [p.short_name + '_janice_talk_option' for p in get_people(tagged_with_all=['janice_talk_option_possible'])]) from _call_for_call_labels_28
    # option to try hypnotizing her
    if player.can_hypno(janice) and janice.tried_hypnosis == 0:
      $ title = "Try hypnotizing her?"
      menu:
        "Yes":
          player.c "Janice, would you look at this for me."
          call focus_image from _call_focus_image_84
          player.c "I am going to talk with you, Janice, and you are going to listen to me."
          player.c "Listen to me now, Janice.  Listen to me.  Listen to my voice and nothing else, Janice.  Only my voice.  Only my voice now."
          wt_image lawyer_desk_1
          janice.c "I'm a busy woman, and I'm sure you're a busy man.  What was it you wanted to ask me about?"
          "How strange.  Janice didn't fall under your trance, but she seems to be completely unaware that you tried to hypnotize her.  It's as if someone else has locked her mind, preventing anyone else access, while making her ignore the act of being hypnotized."
          $ janice.tried_hypnosis = 1
          $ janice.temporary_count = 0
        "No":
          pass
    if janice.tried_hypnosis == 3:
      $ title = "Invoke her trigger?"
      menu:
        "Yes":
          player.c "Janice, I'm curious about something."
          janice.c "What's that?"
          player.c "What happens when I call you \"[janice.trigger_phrase]\"?"
          wt_image lawyer_desk_2
          janice.c "Well, that's ... that's something very important you've told me.  I didn't realize."
          player.c "Realize what, Janice?"
          wt_image lawyer_desk_3
          janice.c "That I was supposed to obey you."
          player.c "Of course, you're supposed to obey me.  That's what a pussy slave is for, isn't it?"
          wt_image lawyer_desk_4
          janice.c "Yes, of course.  How may I serve you, Sir?"
          "You're somewhat limited in your options by the locale.  You have privacy in her office, but you can't do anything too noisy that could be heard by passersby in the hallway or in an adjacent office."
          "Mindful of Marilyn's warning not to diminish her value, it would be dangerous to take her out of the office. Someone could notice her trance, and she likely has important work she needs to finish up here after she's finished serving you."
          $ title = "What do you do with your slave lawyer?"
          menu menu_wait_2:
            "Ask her about Marilyn" if not janice.has_tag('asked_about_marilyn_2'):
              player.c "Slave, you are to obey and serve me."
              janice.c "Yes, Sir."
              player.c "Tell me everything you know about Marilyn, slave."
              janice.c "Marilyn is my client.  Solicitor client privilege attaches to all communications with her."
              player.c "Slave, you are not being obedient.  I told you to tell me everything about her."
              janice.c "Sir, I am obeying.  I have told you everything I know about her.  Marilyn is my client.  Solicitor client privilege attaches to all communications with her."
              "It seems you won't get anything out of her about Marilyn.  Make another choice."
              add tags 'asked_about_marilyn_2' to janice
              jump menu_wait_2
            "Poke around in her brain" if not janice.has_tag('explored_mental_block'):
              "Marilyn warned you against doing any damage to Janice.  Probing her brain while she's in this state may carry some risk."
              "On the other hand, the mental block and associated trigger placed in Janice's brain is fascinating.  If you explore it, you may learn a thing or two, as Marilyn put it."
              $ title = "Proceed?"
              menu:
                "Yes":
                  add tags 'explored_mental_block' to janice
                  if player.has_tag('hypnotist'):
                    player.c "Slave, what happens when you hear the words \"[janice.trigger_phrase]\"?"
                    janice.c "I remember my role."
                    player.c "How did you learn that role?"
                    janice.c "It has always been my role."
                    "You continue on this line of exploration, probing to understand how Marilyn created her trigger, and even more interestingly, how she created the mental block against other hypnotists."
                    "You can't get very far.  Marilyn has spent plenty of time with Janice and has been very thorough and effective in the creation of her safeguards."
                    "Having a chance to explore the works of another hypnotist, however, helps you increase the effectiveness of your technique, making this time well spent."
                    "Most importantly, Marilyn's defenses were sufficiently robust that nothing you did today caused any damage to Janice or Marilyn's control over her.  No need to fear the wrath of Marilyn on this account."
                    $ player.hypnosis_level += 2
                    change player energy by -energy_long notify
                  else:
                    "You want to figure out how Marilyn planted a trigger in Janice and how the mental block works, but you soon realize you have no idea how to go about exploring the changes Marilyn has made in Janice's brain."
                    "Perhaps a natural hypnotist would have some success, but you're at a loss as to how to proceed and soon give up on the effort."
                "No":
                  $ title = "What do you do with your slave lawyer?"
                  jump menu_wait_2
            "Have her sit up and beg":
              player.c "You shouldn't be wearing that much clothing."
              janice.c "I'm sorry, Sir."
              wt_image lawyer_desk_5
              "She quickly strips."
              janice.c "Is this better?"
              player.c "You're just a dumb animal.  No more talking.  Keep your mouth open."
              wt_image lawyer_desk_6
              player.c "Animals belong on the floor, at the feet of their master."
              wt_image lawyer_desk_7
              "Mouth still open, she comes out from behind her desk and squats down in front of you."
              player.c "Animals don't wear glasses, either. Sit up and beg to your Master like an obedient pet."
              wt_image lawyer_desk_8
              "She starts panting and giving out small barks."
              janice.c "Rrrooofff ... Rrrooofff"
              player.c "Quiet, girl.  Beg quietly."
              janice.c "{size=-5}rrooff ... rrooff{/size}"
              "Marilyn was right.  This is fun."
              wt_image lawyer_desk_6
            "Have her blow you":
              player.c "Get on your knees.  You're going to blow me."
              wt_image lawyer_desk_2
              janice.c "Yes, Sir."
              wt_image lawyer_desk_20
              "She comes around from behind her desk, lowers herself to the ground and takes your cock out of your pants."
              if not janice.has_tag('previous_trigger_blowjob'):
                add tags 'previous_trigger_blowjob' to janice
                player.c "Have you ever sucked a cock before?"
                wt_image lawyer_desk_21
                janice.c "Yes, Sir."
                player.c "I thought you were only into women?  Young, married, bisexual blonde women, to be exact."
                janice.c "That's now, Sir.  I used to suck cocks."
                player.c "But not any more?  Except when you're ordered to?"
                janice.c "Yes, Sir."
                player.c "Are you looking forward to having my cock in your mouth?"
                janice.c "Yes, Sir."
                player.c "Then do it."
              else:
                player.c "Aren't you forgetting something?"
                wt_image lawyer_desk_21
                janice.c "Sir?"
                player.c "Don't you have something to say to me?"
                janice.c "Thank you for the opportunity to suck your cock, Sir.  May I please pleasure you with my mouth now, Sir?"
                player.c "Go ahead, but do a good job."
              wt_image lawyer_desk_22
              "The lawyer wraps her mouth around you."
              wt_image lawyer_desk_23
              "Her eyes close as she bobs her head up and down your cock, her tongue swirling along the underside of your shaft and cockhead. She looks like she actually is enjoying this."
              player.c "Look at me while I cum on you."
              wt_image lawyer_desk_24
              "She opens her eyes, a look of contentment on her face as you unload onto her."
              player.c "[player.orgasm_text]"
              wt_image lawyer_desk_25
              "She looks so happy wearing your cum, it's tempting to let her go back to work this way, but you're not sure Marilyn would appreciate the gossip about Janice that would ensue."
              $ janice.hypno_blowjob_count += 1
              $ janice.hypno_facial_count += 1
              orgasm
            "Fuck her quietly":
              player.c "Remove your clothes, slave.  I'm going to fuck you on your desk."
              wt_image lawyer_desk_5
              janice.c "Yes, Sir."
              wt_image lawyer_desk_9
              "Janice strips off her clothes and comes around to the front of her desk."
              player.c "Not like that, slave.  Turn around."
              wt_image lawyer_desk_10
              janice.c "I'm sorry, Sir."
              "She turns around and leans over the desk, presenting her rear to you."
              player.c "Don't make a sound while I'm fucking you, slave."
              wt_image lawyer_desk_11
              "She opens her mouth as you push into her, but true to your instructions, no sounds escape her throat."
              if not janice.has_tag('previous_trigger_sex'):
                add tags 'previous_trigger_sex' to janice
                "Janice may be into fair skinned young bi women, but her body responds surprisingly well to your cock inside her. She's soon sopping wet, her cunt instinctively gripping your cock."
                player.c "Do you like cock, slave?"
                wt_image lawyer_desk_19
                janice.c "Yes, Sir."
                player.c "I thought you were only into young women?"
                janice.c "This pussy slave is only allowed to chase bisexual young blonde women, Sir.  I have to reject all other suitors.  Except, of course, when I'm serving my proper role as slave."
                player.c "Does that leave you sexually frustrated, slave?"
                janice.c "Quite often, Sir."
              else:
                player.c "Have you had a cock inside you since the last time I fucked you?"
                wt_image lawyer_desk_19
                janice.c "No, Sir."
                player.c "Are you happy have mine inside you again?"
                janice.c "Yes, Sir.  Very.  This pussy slave has been very, very horny and not able to get any relief."
              player.c "Would you like to cum now?"
              janice.c "Yes, Sir.  Please?"
              $ title = "Let her cum?"
              menu:
                "Yes":
                  player.c "When you feel my cum spurt inside you, you may orgasm, but don't make a sound when you do."
                  janice.c "Oh thank you thank you thank you, Sir!"
                  wt_image lawyer_desk_12
                  "A few minutes later, Janice silently enjoys your orgasm even more than you do.  You wonder how long it's been since Marilyn let her cum with a cock inside her?"
                  player.c "[player.orgasm_text]"
                  $ janice.hypno_orgasm_count += 1
                "No":
                  player.c "Pussy slaves shouldn't cum from having a cock inside them, slave."
                  janice.c "No, Sir."
                  wt_image lawyer_desk_11
                  player.c "[player.orgasm_text]"
                  "You empty your load inside her, leaving the high powered lawyer panting silently, her cunt twitching, desperate to cum but unable to do so without permission."
              $ janice.hypno_sex_count += 1
              orgasm
              wt_image lawyer_desk_6
          player.c "Go back to the way you were, slave, before I reminded you of your proper role."
          wt_image lawyer_desk_2
          player.c "You will not remember anything we did here today.  You will only remember having a pleasant conversation with me."
          $ janice.temporary_count = 0
        "No":
          pass
    wt_image lawyer_desk_1
    if janice.temporary_count == 1:
      "You've run out of things to discuss with Janice."
      janice.c "If there's nothing more for us to talk about, may I suggest you try calling me next time you want to chat?  It'll save both of us some time."
      $ janice.temporary_count = 0
    else:
      janice.c "It's been nice chatting with you.  Now, I must get back to my work."
    $ janice.dismiss(False)
    call character_location_return(janice) from _call_character_location_return_672
    call character_location_return(janicereceptionist) from _call_character_location_return_673
    call forced_movement(office_tower) from _call_forced_movement_213
    "You find your own way back to the office tower lobby."
    add tags 'no_hypnosis' to janice
  return

label jo_exit:
  return

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
