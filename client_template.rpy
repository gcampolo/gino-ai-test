## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: ???

#################### IMPORTANT INSTRUCTIONS ####################
# Please look/copy/paste stuff from on other character's files to understand the code/system
# Don't Forget To Rename This File
# The following Find/Replace are CASE SENSITIVE:
# Find/Replace All client_name with your client's name, e.g. client_name becomes elsa
# Find/Replace All Client_Name_Capital with your client's capitalized name, e.g. Client_Name_Capital becomes Elsa
# Find/Replace All client_title with your client's title, e.g. client_title becomes frigid
# Find/Replace All Client_Title_Capital with your client's title, e.g. Client_Title_Capital becomes Frigid
#################### IMPORTANT INSTRUCTIONS ####################

## Package Register
# This creates a package that can act as a "hub" for any mod that is attached to it. It starts initially disabled and it depends on the core package.
register_package client_name_mod name "Client_Name_Capital Client Mod" author "???" description "Adds the modded client, Client_Name_Capital, and she is available to be trained when the player's reputation is 4 stars" disabled dependencies core
# This registers the modded client to the initialized package above
register client_name_pregame 10 in client_name_mod as "Client_Name_Capital the Client_Title_Capital"

# Pregame
label client_name_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Client_Name_Capital the Client_Title_Capital (NAME OF REAL LIFE MODEL/ACTRESS GOES HERE)")]

    ## Client Definition
    # FFFFFF is the color of the character's text in Hexadecimal
    # Must have an client_name_image.jpg and an client_name_portrait.jpg files associated with this character
    # Note: min_reputation handles at which wave this character can be trained:
      # 0: Chelsea, Elsa, Jasmine
      # 1: Donna, Lauren, Terri
      # 2: Alexis, Becky Sue, Sarah
      # 3: Wife Trainer 3 Planned Clients
      # 4: Unknown
    client_name = Person(Character("Client_Name_Capital", who_color="#FFFFFF", what_color="#FFFFFF"), "client_name", cut_portrait = True, prefix = "", suffix = "the Client_Title_Capital", resistance = 80, training_period = 12, hypno_trigger_resistance_threshold = 20, min_reputation = 4)
    client_name.trigger_phrase = ""

    # Other Characters
    ### Note: When adding tertiary characters, be careful not to use an already existing name
    ### try adding _client_name to the end of their definition as to not conflict with other characters that might share that name

    ### This is left as an example tertiary character definition ###
    ## Navy
    #husband_client_name = Character("Client_Name_Capital's Husband", who_color="#000080", what_color="#000080", window_background=gui.dialogue_background_dark_font_color)
    ### This is left as an example tertiary character definition ###

    ## Actions
    # Hypno Action Definition
    client_name.add_hypno_actions()
    # Training Action Definitions
    client_name.action_talk = client_name.add_action("Talk to her", label = "_talk", condition = "client_name.can_be_interacted")
    ### These are left as example label names and action definitions ###
    #client_name.action_invoke_hypno_trigger = client_name.add_action("Invoke Her Hypno Trigger", label = "_invoke_hypno_trigger", condition = "client_name.can_be_interacted and client_name.has_tag('trigger_implanted')")
    ##client_name.action_closer = None
    ##client_name.action_kiss = None
    ##client_name.action_cuddle = None
    ##client_name.action_touch_herself = None
    ##client_name.action_make_out = None
    ##client_name.action_model = None
    ##client_name.action_sex_training = None
    ##client_name.action_obedience_training = None
    ##client_name.action_discuss_sexuality = None
    ### These are left as example label names and action definitions ###
    client_name.action_end_session = client_name.add_action("Send her home", label = "_end_session", condition = "client_name.can_be_interacted and client_name.status == 'on_training'")

    # Post-Training Action Definitions
    ### These are left as example label names and action definitions ###
    ##client_name.action_girlfriend_sex = None
    ##client_name.action_girlfriend_domme = None
    ##client_name.action_girlfriend_lesbian = None
    ##client_name.action_girlfriend_tv = None
    ##client_name.action_rename = None
    ##client_name.action_slavegirl_position = None
    ##client_name.action_slavegirl_actions = None
    ##client_name.action_slaveboy_actions = None
    ##client_name.action_degraded_actions = None
    #client_name.action_lend_to_master_m = client_name.add_action("Lend to Master M", label="_lend_to_master_m", condition="client_name.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave')")
    #client_name.relationship_action = bedroom.add_action("[client_name.full_name]", label = client_name.short_name + "_relationship_status", context = "_relationship_status", condition = "client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend') or (client_name.has_tag('slavegirl') and not client_name.has_tag('transformed_slavegirl')) or client_name.has_tag('continuing_actions')")
    ### These are left as example label names and action definitions ###

    ######## EXPANDABLE MENUS #######
    ## Weekend Action Definitions
    client_name_weekend_training_menu = ExpandableMenu("What do you have in mind for Client_Name_Capital this weekend?", pre_label = 'client_name_pre_weekend', post_label = 'client_name_post_weekend')
    # Note: these don't have to be defined in pregame, can be added in game
    ### These are left as example label names and action definitions ###
    #client_name.choice_weekend_hypnotize = client_name_weekend_training_menu.add_choice("Hypnosis Time", "client_name_weekend_hypnosis_time", condition = "player.can_hypno(client_name)")
    #client_name.choice_weekend_play = client_name_weekend_training_menu.add_choice("Play Time", "client_name_weekend_play_time")
    #client_name.choice_weekend_nude = client_name_weekend_training_menu.add_choice("Nude Time", "client_name_weekend_nude_time")
    #client_name.choice_weekend_servant = client_name_weekend_training_menu.add_choice("Servant Time", "client_name_weekend_servant_time")
    ### These are left as example label names and action definitions ###

    ## Tags
    # Common Character Tags

    ### Note: The tag 'first_visit' is commonly added to limit actions when you first meet the client, then removed after an initial discusison with her
    ### Note: The tag 'no_hypnosis' prevents all hypnotism until the tag is removed
    ### Note: The tag 'likes_boys' can also be accompanied by 'likes_girls' if the character is bi-sexual
    client_name.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations
    ### This is left as an example location definition ###
    # Lauren's Office
    # Note: Player can't visit this location until connections are added
    #lauren_office = Location("Lauren the Cheater's Office", 'lco', cut_portrait = True, enter_break_labels = ['lco_no_access'], enter_labels = ['lco_enter'], exit_labels = ['lco_exit'], area = 'offices')
    # Note: These connections link the new location to an existing location; in this case, the office_tower
    #lauren_office.add_connections(office_tower)
    #office_tower.add_connections(lauren_office)
    ### This is left as an example location definition ###

    ## Other
    # Note: Lets this character be a Major Client
    client_name.change_status("available_to_be_client")

    # Start Day Events
    start_day_labels.append('client_name_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    client_name.add_stats_with_value('')
    ### These are left as example variable definitions ###
    #client_name.add_stats_with_value('maintain_week_gf', 'maintain_week_sg', 'random_number')
    ### These are left as example variable definitions ###

    # Character Specific Variables
    client_name.add_stats_with_value('')
    ### These are left as example variable definitions ###
    #client_name.add_stats_with_value('cuckold_count', 'cuckold_discussion', 'cuckold_outfit', 'cuckold_week', 'cum_trigger_count', 'doggy_progress', 'domme_lingerie_outfit', 'domme_pain_outfit', 'domme_pain_shock_count', 'domme_workout_outfit', 'domme_you_outfit_count', 'dommed_you', 'enthusiastic_trigger_count', 'fuck_machine', 'gag_state', 'gf_outfit_count')
    #client_name.add_stats_with_value('lesbian_outfit_count', 'lesbian_event_outfit', 'lingerie_event_outfit', 'masturbate_count', 'piss_status', 'piss_trigger_count', 'position','relationship_event_outfit', 'relationship_event_week', 'rough_trigger_count', 'sex_training_count', 'slaveboy_conversation', 'slavegirl', 'slut_lingerie_outfit', 'slut_wear_use_count', 'used_neighbour_ta')
    ### These are left as example variable definitions ###
  return

# Initial Contact Message
label client_name_message:
    ### This is left as an example message that initiates training ###
    wt_image current_location.image
    husband_client_name "{i}Please train my wife, [client_name.name]{/i}"  # Anything within [] evaluates what is inside. If this was [elsa.name], this comes out as: "Hello Elsa."
    call consider_contract(client_name, "Reply to [client_name.full_name]'s Husband")
    if yesno == True:
        sys "You accept the assignment.  You have until the end of week [client_name.training_limit] to complete it."
        if not player.has_tag('tutorial_message'):
            add tag 'tutorial_message' to player
            sys "You may hold one evening session each week to complete her training.  If you have at least [energy_long.value] Energy left on Friday, you may also schedule a weekend session with a client of your choice."
    ### This is left as an example message that initiates training ###
    return

# Client Rejected
label client_name_rejected:
  sys "You can no longer train [client_name.full_name]."
  return

# Arrange Client Session
label client_name_calling:
  # Check if client has already been trained this week
  if not client_name.can_be_interacted:
    "You had an evening session with Client_Name_Capital earlier this week.  You need to wait until the weekend or next week for another session."
  else:
    call forced_movement(living_room)
    summon client_name
    $ client_name.visit_count += 1
    wt_image client_name.image
    if 'first_visit' in client_name.tags:
      ###### Character Specific Content Goes Here ######
      #wt_image client_title_door_1
      #client_name.c "Client_Name_Capital smiles shyly as you greet her at the door."
      #player.c "Please come in."
      ###### Character Specific Content Goes Here ######
      "You show Client_Name_Capital to your living room."
      if not player.has_tag('first_client_visit_message'):
        add tag 'first_client_visit_message' to player
        sys "[player.first_client_visit_message_text]"
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  return

# Display Portrait
label client_name_update_media:
  if client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    #if client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend'):
    #  $ client_name.change_image('client_title_satisfied')
    pass
    ###### Character Specific Content Goes Here ######
  else:
    ###### Character Specific Content Goes Here ######
    #$ client_name.change_image('client_title_portrait_1')
    pass
    ###### Character Specific Content Goes Here ######
  return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Action
label client_name_examine:
    if client_name.has_tag('first_visit'):
        ###### Character Specific Content Goes Here ######
        pass
    elif client_name.status == 'on_training' and current_location in session_locations:
        ###### Character Specific Content Goes Here ######
        pass
    call client_name_description_display
    return

# Description Display
label client_name_description_display:
    if client_name.status == "on_training":
        "You have until the end of week [client_name.training_limit] to complete this engagement."
    elif client_name.has_tag('satisfied'):
        ###### Character Specific Content Goes Here ######
        pass
    "[client_name.statblock]"
    $ items = ", ".join(i.name for i in client_name.get_items()) if client_name.get_items() != [] else ' Nothing'
    "You have given her: [items]"
    return

# Review Files
label client_review_files:
    call client_name_update_media
    wt_image client_name.image
    call client_name_description_display
    wt_image current_location.image
    return


# Talk to Character
label client_name_talk:
  ### This is left as an example interaction based on the player's Trainer Type ###
  player.c "Hello [client_name.name]."   # Anything within [] evaluates what is inside. If this was [elsa.name], this comes out as: "Hello Elsa."
  if player.has_tag('supersexy'):
    client_name.c "Wow, you are so handsome."
  if player.has_tag('dominant'):
    client_name.c "Wow, you seem very foward."
  if player.has_tag('hypnotist'):
    client_name.c "Wow, you seem very intuitive."
  else:                             #Left an else: statement to account for any modified player tags
    client_name.c "Hello."
  ### This is left as an example interaction based on the player's Trainer Type ###
  return

# Hypno Actions
label client_name_hypnosis_start:
  $ client_name.training_session()
  $ client_name.hypno_session()
  if client_name.status == "on_training":
    summon client_name
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  elif client_name.status == "on_training" and is_weekend():
    summon client_name
    ###### Character Specific Content Goes Here ######
    ### These are left as an example hypnosis ###
    # wt_image client_title_weekend_hypno_2
    # "Client_Name_Capital arrives in a more provocative outfit than she normally wears.  Her time with you seems to be having results."
    # wt_image client_title_hypnotized_3
    # player.c "Please look at this for me, Client_Name_Capital.  Look at this and listen to me.  Listen to me.  Listen to my voice and nothing else, Client_Name_Capital.  Only my voice.  Only my voice now."
    # call focus_image
    # "She soon falls under your trance."
    # player.c "Now Client_Name_Capital, I want you to get comfortable for our talk.  Show me your breasts Client_Name_Capital."
    # wt_image client_title_hypnotized_bare_breasts_5
    # "Client_Name_Capital proudly shows you her bare breasts.  There's no doubt now that your work is paying dividends."
    ### These are left as an example hypnosis ###
    pass
    ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training" and client_name.has_tag("continuing_actions"):
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  else:
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  return

label client_name_desire_hypnosis:
  if client_name.status == "on_training":
    if is_weekend():
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  return

label client_name_submission_hypnosis:
  if client_name.status == "on_training":
    if is_weekend():
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  return

label client_name_sos_hypnosis:
  if client_name.status == "on_training":
    if is_weekend():
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  return

label client_name_resistance_hypnosis:
  if client_name.status == "on_training":
    if is_weekend():
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  elif client_name.status == "post_training":
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  return

label client_name_implant_trigger:
    if player.has_tag('hypnotist'):
        # Note: conditional test is against unmodified resistance stat
        if client_name.resistance < client_name.hypno_trigger_resistance_threshold:
            add tag 'trigger_implanted' to client_name
            "Client_Name_Capital's mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
            $ title = "What trigger phrase do you want to use?"
            menu menu_client_name_implant_trigger:
                "[client_name.trigger_phrase]":
                    pass
                "Choose something else":
                    $ client_name.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
                    jump menu_client_name_implant_trigger
            player.c "Client_Name_Capital, I have something important to tell you."
            extend "\nWhen you hear the phrase \"[client_name.trigger_phrase]\" you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you.  Do you understand?"
            client_name.c "When I hear \"[client_name.trigger_phrase]\" I will fall into a trance and do everything I am told."
            player.c "You will not remember anything you do while you are in a trance.  Everything you do in the trance will seem normal, and you will not mind doing it.   You will stay in the trance until the speaker of the phrase releases you.  Do you understand?"
            client_name.c "I will forget everything I do in a trance.  I won't mind doing it because it will seem normal.  I'll stay in the trance until I'm released."
            sys "You can test Client_Name_Capital's trigger on a future visit."
        else:
            "You've been working on implanting a hypnotic trigger in Client_Name_Capital's mind, but she's still too resistant to you. You need to lower her resistance to you before you can implant the trigger."
    return

label client_name_invoke_hypno_trigger:
  ###### Character Specific Content Goes Here ######
  pass
  ###### Character Specific Content Goes Here ######
  return

label client_name_hypnosis_end:
  if client_name.status == "on_training":
    call character_location_return(client_name)
    end_day
  elif client_name.status == "post_training" and client_name.has_tag("continuing_actions"):
    call character_location_return(client_name)
  else:
    # If client is no longer being trained and she is no longer visiting due to being converted to girlfriend, etc. Character does not get dismissed
    pass
  return

## Character Specific Actions
### This is left as an example Training Action ###
# Kiss Action
# label client_name_kiss:
  # $ client_name.training_session()
  # wt_image client_title_kiss_1
  # "As your lips touch, Client_Name_Capital leans backwards, pulling away.  You follow, pressing your mouth against hers."
  # "Her lips are dead and unmoving as you begin to kiss her.  You persevere, and eventually you sense the slightest amount of response from Client_Name_Capital."
  # "It's not much, but it's enough to give you hope that future sessions may be more productive."
  # change client_name desire by 5
  # change player energy by -energy_long
  # end_day
  # return
### This is left as an example Training Action ###

# End Session
label client_name_end_session:
  if client_name.status == "on_training":
    $ client_name.training_session()
    "You're unable to find an activity that both you and Client_Name_Capital are willing to proceed with, so you end today's session here."
    $ player.extra_clients_fee_this_week -= client_name.pay # so you don't get paid for training her this week
    add tag 'failed_regular_training_this_week' to client_name
    dismiss client_name
    end_day
  elif client_name.status == 'continuing_actions':
    $ client_name.training_session()
    "You've spent enough time with Client_Name_Capital for today. You send her home."
    dismiss client_name
  else:
    # If somehow the character still has this action when the action is no longer relevant, remove this action
    if client_name.action_end_session is not None:
      $ client_name.action_end_session = None
      rem action
  return

# Weekend Actions
label client_name_pre_weekend:
    # this is used together with post_weekend to determine if you successfully completed a weekend training
    add tag 'checking_for_weekend' to client_name
    return

label client_name_post_weekend:
    if client_name.has_tag('checking_for_weekend'):
        # if the tag is still on, no training happened
        rem tag 'checking_for_weekend' from client_name
    else:
        # if the tag was removed, training happened; if the regular weekday training was failed, you should now get paid for the visit
        if client_name.has_tag('failed_regular_training_this_week'):
            rem tag 'failed_regular_training_this_week' from client_name
            $ player.extra_clients_fee_this_week += client_name.pay
    return

label client_name_weekend:
  # Example of requirement needed to access Weekend Actions
  if not client_name.has_tag('required_tag_goes_here'):
    call character_location_return(client_name)
    "You need to convince [client_name.name] to accept the required tag before you can get her to visit you on weekends."
  else:
    if player.energy >= energy_long.value:
      call expandable_menu(client_name_weekend_training_menu)
    else:
      sys "You do not have enough energy for this action, choose something else."
  return

### This is left as an example Training Action ###
label client_name_weekend_hypnosis_time:
  # note: this causes the normal weekday Hypnotize Her action to now run; weekend artwork can then be handled in _hypnosis_start, etc.
  $ queue_action(client_name.hypno_action)
  return
### This is left as an example Training Action ###

### This is left as an example Training Action ###
label client_name_weekend_nude_time:
  # if client_name.has_tag("stripped") or client_name.sex_count > 0 or client_name.blowjob_count >= 2:
    # $ client_name.training_session()
    # wt_image client_title_naked_1
    # "As soon as Client_Name_Capital arrives, you have her remove her clothes."
    # wt_image client_title_naked_2
    # player.c "All your clothes, Client_Name_Capital.  Panties, too.  Then lift your leg, I want to be able to inspect you - all of you - this weekend."
    # wt_image client_title_naked_3
    # player.c "Relax, Client_Name_Capital.  Drop your arms.  We're going to be spending quite a bit of time together.  You're going to need to get comfortable with that body of yours, and now is as good a time as any."
    # wt_image client_title_naked_4
    # player.c "That's better.  Now, let's talk."
    # "She spends the rest of her time together with you stark naked and open to your examination.  You spend that time talking to her about her feelings about her body, being touched, and sex.  Being naked physically helps her open up, mentally.  Being naked while you are fully dressed also reinforces your authority over her."
    # change client_name submission by 5
    # change client_name sos by 5
    # call character_location_return(client_name)
    # end_day
  # else:
    # "Client_Name_Capital is not comfortable being completely naked around you yet.  Perhaps you should try something else."
  return
### This is left as an example Training Action ###

## Post-Training Character Actions
### This is left as an example Post-Training Action ###
# # Discuss Sexuality
# label client_name_discuss_sexuality:
  # wt_image client_name.image
  # player.c "Client_Name_Capital, I want to talk to you about your sexuality."
  # client_name.c "Okay."
  # $ title = "What do you suggest to Client_Name_Capital?"
  # menu:
    # "She should try sex with women" if not client_name.has_tag("lesbian"):
      # player.c "I want you to have sex with a woman."
      # client_name.c "But, I'm not a lesbian.  I'm not interested in girls."
      # player.c "You weren't really interested in boys either, when I first met you.  I'd like you to try sex with a woman."
      # if client_name.test('submission', 90) or client_name.test('desire', 100) or client_name.test('resistance', 0):
        # client_name.c "Okay.  For you, I'll try."
        # player.c "Good. I have the perfect girl in mind for you."
        # call client_name_convert_lesbian
      # else:
        # client_name.c "I just can't see me doing that."
        # if client_name.has_tag("trigger_implanted"):
          # "You invoke Client_Name_Capital's trigger."
          # player.c "Listen carefully to me, Client_Name_Capital. '[client_name.trigger_phrase]'. Did you hear me?"
          # client_name.c "Yes, I heard you."
          # player.c "You want to have sex with other women whenever I tell you to."
          # client_name.c "I... I don't think I..."
          # player.c "'[client_name.trigger_phrase]', Client_Name_Capital.  You will have sex with other women whenever I tell you to.  Do you understand?"
          # client_name.c "Yes, I understand.  I will have sex with other women whenever you want."
          # call client_name_convert_lesbian
        # else:
          # "Perhaps if she were more submissive towards you, less resistant to you, or wanted to please you more she would accept your request.  As it is, Client_Name_Capital is sticking exclusively to boys."
    # "She would make a good Domme" if not client_name.has_tag("domme"):
      # player.c "Client_Name_Capital, I think you would make a good Domme."
      # client_name.c "What, me?  Bossing people around?"
      # player.c "Not bossing them around, Client_Name_Capital.  Taking control of their sexual experience.  Making the decisions as to when and how they should be touched,  Being responsible for understanding what they want - and what they need  - in order to feel fulfilled, sexually."
      # if client_name.test('sos', 90):
        # client_name.c "Do you really think I could do that?"
        # player.c "I think you're better suited than most.  You've had to work hard to understand and accept your own sexuality.  Taking charge of understanding other people's sexual needs is a logical next step."
        # client_name.c "Okay.  I guess I could try."
        # player.c "Good.  Let's get you ready with a quick shopping trip.  If you're going to be in charge, you need to look the part.  Then I'll find someone for you to practice on."
        # call client_name_convert_domme
      # else:
        # client_name.c "I still have enough trouble understanding how I'm feeling and what I need sexually.  I don't think I'm ready to start making decisions for other people."
        # "Perhaps if her sense of self were higher, she would be willing to consider your suggestion.  As it is, Client_Name_Capital's not ready to consider being a Domme."
        # if client_name.has_tag("trigger_implanted"):
          # "Even invoking her trigger won't work.  That can break down her resistance to new things, but can't help her be something she's not yet capable of being."
    # "Never mind":
      # player.c "Actually, let's do something else instead."
      # client_name.c "Okay."
  # return
### This is left as an example Post-Training Action ###

########### OBJECTS ###########
## Common Objects
# Contact Former Client
### This is left as an example Post-Training Contact Action ###
label client_name_contact:
  # Determine if Character wants to continue Visiting
  if client_name.status == "post_training" and client_name.has_tag("satisfied") and not client_name.has_tag("continuing_actions"):
    pass
    ###### Character Specific Content Goes Here ######
    # wt_image client_name.image
    # client_name.c "Hi.  I wasn't expecting to hear from you again, now that my training is finished."
    # player.c "Client_Name_Capital, I would like you to continue to visit me.  Without your husband's knowledge."
    # if client_name.test('desire', 70) or client_name.test('submission', 75):
      # "Client_Name_Capital is quiet for a moment before she replies."
      # client_name.c "Okay.  I can do that."
      # add tag 'continuing_actions' to client_name
    # else:
      # client_name.c "I don't think that would be a good idea. Please don't contact me again."
      # if client_name.has_tag("trigger_implanted"):
        # "You invoke Client_Name_Capital's trigger."
        # player.c "Listen carefully to me, Client_Name_Capital. '[client_name.trigger_phrase]'.  Did you hear me?"
        # client_name.c "Yes, I heard you."
        # player.c "You want to visit me."
        # client_name.c "Yes, I want to visit you."
        # player.c "You will not remember this conversation.  From now on, however, when I contact you and ask you to visit, you will do so.  You will not tell your husband.  You will visit me in secret, whenever I ask you to.  Do you understand?"
        # client_name.c "Yes, I understand."
        # add tag 'continuing_actions' to client_name
      # else:
        # rem tag 'continuing_actions' from client_name
        # $ living_room.remove_action(client_name.current_client_action)
    ###### Character Specific Content Goes Here ######
  # Contact Actions Start Here If Character Wants To Continue
  if client_name.status == "post_training" and client_name.has_tag("continuing_actions"):
    $ client_name.training_session()
    summon client_name
    wt_image client_name.image
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######

    # If Character has not been converted, dismiss
    call character_location_return(client_name)
  return
### This is left as an example Post-Training Contact Action ###

## Character Specific Objects
## Items
# Give Butt Plug
label give_bp_client_name:
  if client_name.has_item(butt_plug):
    sys "You've already given her one.  She doesn't need another."
  else:
    if client_name.status == "on_training":
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
      give 1 butt_plug from player to client_name notify
    else:
      ###### Character Specific Content Goes Here ######
      "You should save this for a current client."
      pass
      ###### Character Specific Content Goes Here ######
  return

# Give Chastity Belt
label give_cb_client_name:
  if client_name.has_item(chastity_belt):
    sys "You've already given her one.  She doesn't need another."
  else:
    if client_name.status == "on_training":
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
      give 1 chastity_belt from player to client_name notify
    else:
      ###### Character Specific Content Goes Here ######
      "You should save this for a current client."
      pass
      ###### Character Specific Content Goes Here ######
  return

# Give Dildo
label give_di_client_name:
  if client_name.has_item(dildo):
    sys "You've already given her one.  She doesn't need another."
  else:
    if client_name.status == "on_training":
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
      give 1 dildo from player to client_name notify
    else:
      ###### Character Specific Content Goes Here ######
      "You should save this for a current client."
      pass
      ###### Character Specific Content Goes Here ######
  return

# Use Fetch Toy
label use_ft_client_name:
  if client_name.has_tag('puppygirl'):
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  else:
    "You shouldn't try to play fetch with someone who isn't your pet."
  return

# Give Jewelry
label give_jwc_client_name:
  "Save this as a gift for Chelsea."
  return

# Use Leash
label use_le_client_name:
  if client_name.has_tag('puppygirl'):
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  else:
    "You shouldn't try to take someone for a walk who isn't your pet."
  return

# Give Lingerie
label give_li_client_name:
  if client_name.has_item(lingerie):
    sys "You've already gifted lingerie to Client_Name_Capital.  She has enough for now."
  else:
    if client_name.status == "on_training":
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
      give 1 lingerie from player to client_name notify
    else:
      sys "You should save the lingerie for a current client."
  return

# Give Love Potion
label give_lp_client_name:
  if client_name.has_tag('love_potion_used'):
    "You've already used a love potion on Client_Name_Capital.  Additional ones won't do anything else."
  else:
    if client_name.status == "on_training":
      ###### Character Specific Content Goes Here ######
      pass
      #change client_name desire by 20
      ###### Character Specific Content Goes Here ######
      add tag 'love_potion_used' to client_name
      rem 1 love_potion from player notify
    else:
      ###### Character Specific Content Goes Here ######
      pass
      ###### Character Specific Content Goes Here ######
  return

# Give Transformation Potion
### This is left as an example Transformation Action ###
label give_tp_client_name:
  if client_name.has_tag('transformed'):
    sys "She has already been transformed.  The potion can do nothing more to her."
  else:
    if client_name.status == "post_training" and not client_name.has_tag('unsatisfied'):
      ###### Character Specific Content Goes Here ######
      ""
      $ title = "What do you want the potion to transform her into?"
      menu:
        "Your Girlfriend" if not client_name.has_tag('girlfriend'):
          ""
          $ client_name.training_session() # Prevents more actions taking place that day
          $ client_name.transformed_via_object = True  # Adds tags: transformed, transformed_slavegirl, transformed_whore, etc during conversion call
          call client_name_convert_girlfriend
          change player energy by -energy_long notify
          rem 1 transformation_potion from player
          call character_location_return(client_name)
        "A Bi-sexual" if not client_name.has_tag('lesbian'):
          ""
          $ client_name.training_session() # Prevents more actions taking place that day
          $ client_name.transformed_via_object = True  # Adds tags: transformed, transformed_slavegirl, transformed_whore, etc during conversion call
          call client_name_convert_lesbian
          change player energy by -energy_long notify
          rem 1 transformation_potion from player
          call character_location_return(client_name)
        "Your Slavegirl" if client_name.test('submission', 50) and not client_name.has_tag('slavegirl'):
          ""
          $ client_name.training_session() # Prevents more actions taking place that day
          $ client_name.transformed_via_object = True  # Adds tags: transformed, transformed_slavegirl, transformed_whore, etc during conversion call
          call client_name_convert_slavegirl
          change player energy by -energy_long notify
          rem 1 transformation_potion from player
          call character_location_return(client_name)
        "A Puppygirl" if client_name.test('submission', 90) and not client_name.has_tag('puppygirl'):
          ""
          $ client_name.training_session() # Prevents more actions taking place that day
          $ client_name.transformed_via_object = True  # Adds tags: transformed, transformed_slavegirl, transformed_whore, etc during conversion call
          call client_name_convert_puppygirl
          change player energy by -energy_long notify
          rem 1 transformation_potion from player
          call character_location_return(client_name)
        "Nothing":
          pass
      ###### Character Specific Content Goes Here ######
    else:
      ###### Character Specific Content Goes Here ######
      "You shouldn't try this while Client_Name_Capital is a client.  Her husband knows she's here and may cause trouble."
      ###### Character Specific Content Goes Here ######
  return
### This is left as an example Transformation Action ###

# Use Water Bowl
label use_wb_client_name:
  if client_name.has_tag('puppygirl'):
    ###### Character Specific Content Goes Here ######
    pass
    ###### Character Specific Content Goes Here ######
  else:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
### This is left as an example Will-Tamer Action ###
label use_wt_client_name:
  if client_name.has_tag('transformed'):
    sys "Client_Name_Capital has already been transformed.  The Will-Tamer can do nothing more to her now."
  else:
    if client_name.has_tag('will_tamer_this_week'):
      sys "You have already used the Will-Tamer on Client_Name_Capital this week.  Let its effects continue to work on her brain for a few days; then you can try using it again next week."
    else:
      $ client_name.temporary_count = 0
      if client_name.test('submission', 20):
        if client_name.will_tamer_count == 0:
          ###### Character Specific Content Goes Here ######
          pass
          ###### Character Specific Content Goes Here ######
          "You don't leave her in it for long.  Just enough for it to start to re-wire her brain.  Those changes will become stronger over the coming week, at which point you could put her in it again."
        elif client_name.will_tamer_count == 1:
          ###### Character Specific Content Goes Here ######
          pass
          ###### Character Specific Content Goes Here ######
        elif client_name.will_tamer_count >= 2:
          ###### Character Specific Content Goes Here ######
          pass
          ###### Character Specific Content Goes Here ######
          if client_name.test('resistance',1):
            "Client_Name_Capital sighs contentedly as you snap the Will-Tamer in place around her neck."
            client_name.c "Thank you for collaring me."
            player.c "Is that how you think you should be addressing me?"
            "Client_Name_Capital hesitates for a moment."
            client_name.c "Thank you for collaring me, Master."
            $ client_name.temporary_count = 1
          else:
            ###### Character Specific Content Goes Here ######
            pass
            ###### Character Specific Content Goes Here ######
        if client_name.temporary_count == 1:
          "The Will-Tamer has re-programmed Client_Name_Capital's brain to the point that she's ready to undergo a more complete transformation."
          if client_name.status == "post_training" and (not client_name.has_tag('slavegirl') or not client_name.has_tag('puppygirl') or not client_name.has_tag('degraded')):
            "If you let the Will-Tamer take its full effect, the Client_Name_Capital you know now will be lost, permanently."
            "You will also lose the Will-Tamer, which will become absorbed into Client_Name_Capital's very being."
            $ title = "Do you want the Will-Tamer to transform Client_Name_Capital?"
            menu:
              "Yes":
                ###### Character Specific Content Goes Here ######
                pass
                ###### Character Specific Content Goes Here ######
                $ title = "What do you want to transform Client_Name_Capital into?"
                menu:
                  "Your Slavegirl" if not client_name.has_tag('slavegirl'):
                    ###### Character Specific Content Goes Here ######
                    pass
                    ###### Character Specific Content Goes Here ######
                    $ client_name.training_session() # Prevents more actions taking place that day
                    $ client_name.transformed_via_object = True
                    rem 1 will_tamer from player
                    call client_name_convert_slavegirl
                    call character_location_return(client_name)
                  "A Puppygirl" if not client_name.has_tag('puppygirl'):
                    ###### Character Specific Content Goes Here ######
                    pass
                    ###### Character Specific Content Goes Here ######
                    $ client_name.training_session() # Prevents more actions taking place that day
                    $ client_name.transformed_via_object = True
                    rem 1 will_tamer from player
                    call client_name_convert_puppygirl
                    call character_location_return(client_name)
                  "A Degradedgirl" if not client_name.has_tag('degraded'):
                    ###### Character Specific Content Goes Here ######
                    pass
                    ###### Character Specific Content Goes Here ######
                    $ client_name.training_session() # Prevents more actions taking place that day
                    $ client_name.transformed_via_object = True
                    rem 1 will_tamer from player
                    call client_name_convert_degraded
                    call character_location_return(client_name)
                  "Nothing":
                    pass
              "No":
                pass
            $ client_name.temporary_count = 0
          else:
            ###### Character Specific Content Goes Here ######
            pass
            "You should wait, however, until you complete her assignment before moving on to the next step.  Otherwise, her husband is too likely to cause trouble."
            ###### Character Specific Content Goes Here ######
        $ client_name.will_tamer_count += 1
        add tag 'will_tamer_this_week' to client_name
        ###### Character Specific Content Goes Here ######
        change client_name submission by 10
        change client_name resistance by -15 notify
        pass
        ###### Character Specific Content Goes Here ######
      else:
        client_name.c "A collar?  Really?"
        client_name.c "I don't think I'm ready to be your slavegirl or whatever you're thinking."
        "Perhaps you should wait until her resistance to your instructions is lower."
  return
### This is left as an example Will-Tamer Action ###

########### TIMERS ###########
## Common Timers
# End Training Permanently
### This is left as an example End-Training Action ###
label client_name_end_training:
  ## NOTE: use unmodded stats, not 'test' function, so don't pick up temporary modifiers, etc.
  if client_name.sos >= 50:
    ###### Character Specific Content Goes Here ######
    # wt_image client_name.image
    # "Your engagement to train Client_Name_Capital the Client_Title_Capital has now ended. You receive an email from her husband."
    # husband_client_name "{i}Wow, I can't believe what a change you've made in Client_Name_Capital.  We have sex now!  Sometimes she even initiates things.{/i}"
    # husband_client_name "{i}You've saved our marriage, you really have.  I'll be leaving positive feedback for you online.{/i}"
    # $ client_name.prefix = ""
    # $ client_name.suffix = "the Sexual"
    ###### Character Specific Content Goes Here ######
    call convert(client_name,"satisfied", False, True)
  else:
    ###### Character Specific Content Goes Here ######
    # wt_image client_title_indignant_1
    # "Your engagement to train Client_Name_Capital the Client_Title_Capital has now ended. Unfortunately, Client_Name_Capital never became truly comfortable with sex.  She and her husband will have to look for other solutions."
    ###### Character Specific Content Goes Here ######
    call convert(client_name,"unsatisfied", True, True)
  return
### This is left as an example End-Training Action ###

# Start Day
label client_name_start_day:
  # At Start of Day, Relocate Character to Proper Location if they have been converted or Dismiss
  call character_location_return(client_name)
  ###### Character Specific Content Goes Here ######
  pass
  ###### Character Specific Content Goes Here ######
  return

# End Day
label client_name_end_day:
  ###### Character Specific Content Goes Here ######
  pass
  ###### Character Specific Content Goes Here ######
  # At End of Day, Relocate Character to Proper Location or Dismiss
  call character_location_return(client_name)
  return

# End Week
label client_name_end_week:
  ###### Character Specific Content Goes Here ######
  pass
  ###### Character Specific Content Goes Here ######
  $ client_name.visit_count_total += client_name.visit_count
  $ client_name.visit_count = 0
  return

## Club Labels
label client_name_swingers_room_call:
    if client_name.can_be_interacted:
        add tag 'in_swingers_room_now' to client_name
    else:
        "You can't find Client_Name_Capital right now, or you'd make her join you."
    return

label client_name_swingers_room_send_home:
    rem tag 'in_swingers_room_now' from client_name
    call character_location_return(client_name)
    return

## Client Specific Timers
# Activate Client Actions
### This is left as an example of Action Activation ###
label client_name_activate_client_actions:
  # if player.hypnosis_level > 0 and client_name.has_tag('no_hypnosis'):
    # rem tag 'no_hypnosis' from client_name
  # if client_name.action_closer is None:
    # $ client_name.action_closer = client_name.add_action("Tell her to come closer", label="_closer", condition="client_name.can_be_interacted and not client_name.has_tag('closer') and client_name.status == 'on_training'")
  # if client_name.action_cuddle is None:
    # $ client_name.action_cuddle = client_name.add_action("Cuddle", label="_cuddle", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.status == 'on_training'")
  # if client_name.action_touch_herself is None:
    # $ client_name.action_touch_herself = client_name.add_action("Have Her Touch Herself", label="_touch_herself", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.status == 'on_training'")
  # if client_name.action_make_out is None:
    # $ client_name.action_make_out = client_name.add_action("Make Out", label="_make_out", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.has_tag('kissed') and client_name.status == 'on_training'")
  # if client_name.action_model is None:
    # $ client_name.action_model = client_name.add_action("Have her Model for You", label="_model", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.status == 'on_training'")
  # if client_name.action_sex_training is None:
    # $ client_name.action_sex_training = client_name.add_action("Sex Training", label="_sex_training", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.status == 'on_training'")
  # if client_name.action_obedience_training is None:
    # $ client_name.action_obedience_training = client_name.add_action("Obedience Training", label="_obedience_training", condition="client_name.can_be_interacted and client_name.has_tag('closer') and client_name.status == 'on_training'")
  return
### This is left as an example of Action Activation ###

### IF CONVERTING TO HYPNO-GIRLFRIEND: MUST call convert(client_name,"hypno_girlfriend") and then call this label ###
# Convert Character to Girlfriend
label client_name_convert_girlfriend:
  ###### Character Specific Content Goes Here ######
  #if client_name.has_tag('slavegirl'):
  #  call unconvert(client_name, "slavegirl")
  #$ client_name.maintain_week_gf = week + 1
  #$ client_name.relationship_event_week = week + 2
  #$ client_name.prefix = ""
  #$ client_name.suffix = "the Sexual"
  # if player.hypnosis_level > 0 and client_name.has_tag('no_hypnosis'):
    # rem tag 'no_hypnosis' from client_name
  # if client_name.action_discuss_sexuality is None:
    # $ client_name.action_discuss_sexuality = client_name.add_action("Discuss Her Sexuality", label = "_discuss_sexuality", condition = "(client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend')) and not (client_name.has_tag('lesbian') and client_name.has_tag('domme'))")
  # if client_name.action_girlfriend_sex is None:
    # $ client_name.action_girlfriend_sex = client_name.add_action("Girlfriend - Spend Time with Her", label = "_girlfriend_sex", condition = "client_name.can_be_interacted and (client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend'))")
  # if client_name.action_girlfriend_domme is None:
    # $ client_name.action_girlfriend_domme = client_name.add_action("Domme Session", label = "_girlfriend_domme", condition = "client_name.can_be_interacted and (client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend')) and client_name.has_tag('domme')")
  # if client_name.action_girlfriend_lesbian is None:
    # $ client_name.action_girlfriend_lesbian = client_name.add_action("Lesbian Session", label = "_girlfriend_lesbian", condition = "client_name.can_be_interacted and (client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend')) and client_name.has_tag('lesbian')")
  # if client_name.action_girlfriend_tv is None:
    # $ client_name.action_girlfriend_tv = client_name.add_action("Watch TV with Her", label = "_girlfriend_tv", condition = "client_name.can_be_interacted and (client_name.has_tag('girlfriend') or client_name.has_tag('hypno_girlfriend'))")
  ###### Character Specific Content Goes Here ######

  ### IF CONVERTING TO HYPNO-GIRLFRIEND: MUST call convert(client_name,"hypno_girlfriend") and then call this label ###
  if not client_name.has_tag('hypno_girlfriend'):
    call convert(client_name, "girlfriend")
  $ client_name.fixed_location = bedroom
  $ client_name.location = bedroom
  $ client_name.training_regime = 'daily'
  rem tag 'follows' from client_name
  add tag 'swingers_room_possible' to client_name
  add tag 'post_continuing_actions' to client_name
  rem tag 'continuing_actions' from client_name
  return

# Convert Character to Slavegirl
label client_name_convert_slavegirl:
  ###### Character Specific Content Goes Here ######
  # add tag 'no_hypnosis' to client_name
  # if client_name.has_tag('whore'):
    # call unconvert(client_name, "whore")
  # if client_name.has_tag('girlfriend'):
    # call unconvert(client_name, "girlfriend")
  # if client_name.has_tag('hypno_girlfriend'):
    # call unconvert(client_name, "hypno_girlfriend")
  # if client_name.has_tag('trigger_implanted'):
    # $ client_name.action_invoke_hypno_trigger = None
    # $ client_name.remove_action(client_name.action_invoke_hypno_trigger)
  # if not client_name.has_tag('transformed_slavegirl'):
    # $ client_name.maintain_week_sg = week + 3
  # $ client_name.prefix = "Slave"
  # $ client_name.suffix = ""
  # if client_name.action_slaveboy_actions is None:
    # $ client_name.action_slaveboy_actions = client_name.add_action("Discuss Becoming Her Slaveboy", label = "_slaveboy_actions", condition = "client_name.can_be_interacted and client_name.has_tag('slavegirl') and client_name.slaveboy_conversation == 1")
  # if client_name.action_rename is None:
    # $ client_name.action_rename = client_name.add_action("Rename Her", label = "_rename", condition = "client_name.has_tag('slavegirl')")
  # if client_name.action_slavegirl_position is None:
    # $ client_name.action_slavegirl_position = client_name.add_action("Choose Her Position", label = "_slavegirl_position", condition = "client_name.has_tag('slavegirl')")
  # if client_name.action_slavegirl_actions is None:
    # $ client_name.action_slavegirl_actions = client_name.add_action("Slavegirl - Spend Time with Her", label = "_slavegirl_actions", condition = "client_name.can_be_interacted and client_name.has_tag('slavegirl')")
  ###### Character Specific Content Goes Here ######

  call convert(client_name, "slavegirl")
  $ client_name.training_regime = 'daily'
  $ client_name.fixed_location = bedroom
  $ client_name.location = bedroom
  rem tag 'follows' from client_name
  add tag 'post_continuing_actions' to client_name
  rem tag 'continuing_actions' from client_name
  return

# Convert Character to Degraded
label client_name_convert_degraded:
  ###### Character Specific Content Goes Here ######
  # add tag 'no_hypnosis' to client_name
  # if client_name.has_tag('whore'):
    # call unconvert(client_name, "whore")
  # if client_name.has_tag('slavegirl'):
    # call unconvert(client_name, "slavegirl")
  # if client_name.has_tag('girlfriend'):
    # call unconvert(client_name, "girlfriend")
  # if client_name.has_tag('hypno_girlfriend'):
    # call unconvert(client_name, "hypno_girlfriend")
  # if client_name.has_tag('trigger_implanted'):
    # $ client_name.action_invoke_hypno_trigger = None
    # $ client_name.remove_action(client_name.action_invoke_hypno_trigger)
  # if client_name.action_degraded_actions is None:
    # $ client_name.action_degraded_actions = client_name.add_action("Degraded - Spend Time with Her", label = "_degraded_actions", condition = "client_name.can_be_interacted and client_name.has_tag('degraded')")
  ###### Character Specific Content Goes Here ######

  call convert(client_name,"degraded")
  $ client_name.training_regime = 'daily'
  $ client_name.fixed_location = basement
  $ client_name.location = basement
  rem tag 'follows' from client_name
  add tag 'post_continuing_actions' to client_name
  rem tag 'continuing_actions' from client_name
  return

# Convert Character to Puppygirl
label client_name_convert_puppygirl:
  ###### Character Specific Content Goes Here ######
  # add tag 'no_hypnosis' to client_name
  # if client_name.has_tag('whore'):
    # call unconvert(client_name, "whore")
  # if client_name.has_tag('slavegirl'):
    # call unconvert(client_name, "slavegirl")
  # if client_name.has_tag('girlfriend'):
    # call unconvert(client_name, "girlfriend")
  # if client_name.has_tag('hypno_girlfriend'):
    # call unconvert(client_name, "hypno_girlfriend")
  # if client_name.has_tag('trigger_implanted'):
    # $ client_name.action_invoke_hypno_trigger = None
    # $ client_name.remove_action(client_name.action_invoke_hypno_trigger)
  ###### Character Specific Content Goes Here ######

  call convert(client_name,"puppygirl")
  $ client_name.training_regime = 'daily'
  $ client_name.fixed_location = bedroom
  $ client_name.location = bedroom
  rem tag 'follows' from client_name
  add tag 'post_continuing_actions' to client_name
  rem tag 'continuing_actions' from client_name
  return

# Convert Character to Bimbo
label client_name_convert_bimbo:
  $ client_name.training_regime = 'daily'
  call convert(client_name,"bimbo")
  return

# Convert Character to Domme
label client_name_convert_domme:
  call convert(client_name,"domme")
  return

# Convert Character to Lesbian
label client_name_convert_lesbian:
  call convert(client_name,"lesbian")
  ###add tag 'likes_girls' to client_name        # added automatically in lesbian conversion call
  return

# Convert Character to Showgirl
label client_name_convert_showgirl:
  $ client_name.training_regime = 'daily'
  call convert(client_name, "showgirl")
  return

# Convert Character to Whore
label client_name_convert_whore:
  call convert(client_name,"whore")
  return

########### ROOMS ###########
## Left as placeholders
# label _examine:
  # return

# label _no_access:
  # return

# label _enter:
  # return

# label _exit:
  # return

################################### NOTES ###################################
# Trainer Type: Playboy     is      player.has_tag('supersexy')
# Trainer Type: Hypnotist     is      player.has_tag('hypnotist')
# Trainer Type: Dominant     is      player.has_tag('dominant')


## Client Status
#0 = not yet prospect
#1 = prospect, .status = "available_to_be_client" and .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = client, .status = "on_training"
#4 = unsatisfied former client, add tag 'unsatisfied' and .status = "post_training"
#5 = satisfied former client, add tag 'satisfied' and .status = "post_training"
#6 = continuing_actions, add tag 'continuing_actions' and .status = "post_training"
#7 = satisfied former client not continuing, rem tag 'continuing_actions' and .status = "post_training"
#8 = post continuing actions, add tag 'post_continuing_actions' and .status = "post_training"

## Minor Client Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tag 'continuing_actions' and .status = "post_training"
#5 = dead, rem tag 'continuing_actions' and .status = "post_training"
