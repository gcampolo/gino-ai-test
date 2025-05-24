## Author
# Questions/Comments/Bugfixes can be directed to: Semeicardia
# Questions/Comments/Suggestions: Haseo


# Package Register
## register_package kagney name "Kagney, the Struggling Student" description "Allows Kagney to be client."
register_package kagney name "Kagney the Struggling Student" author "Semeicardia & Haseo" description "Kagney's father reaches out to the WT being very confused about what he does. His daughter Kagney used to be a straight A student but of late she's fallen into a bad crowd and her grades have fallen. Fearing her College Dreams might vanish if she continues being this way, he reaches out to you thinking you're a Tutor. Upon agreeing to his deal you talk with Kagney where you learn she's only like this because the Quarterback of the football team started to notice her and she just wanted to be popular for once." dependencies core
register kagney_pregame 1 in kagney as "Kagney the Struggling Student"

# Pregame
label kagney_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('full', "Kagney the Struggling Student (Kagney Lynn Karter)")]


    ## Character Definition
    # 0,64,128
    kagney = Person(Character("Kagney", who_color="#004080", what_color="#004080", window_background = gui.dialogue_background_dark_font_color), "kagney", cut_portrait = True, prefix = "", suffix = "the Struggling Student", resistance = 75, sos = 5, training_period = 15, hypno_trigger_resistance_threshold = 50, hypno_trigger_sessions_threshold = 3, min_reputation = 3)
    kagney.trigger_phrase = "Bimbos don't need books"
    
    # Other Characters
    # Navy
    father_kagney = Character("Kagney's Father", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    tommy_kagney = Character("Tommy", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    stepmom_kagney = Character("Stepmom", who_color="#FF69B4", what_color="#FF69B4", window_background = gui.dialogue_background_dark_font_color)  
    chad_kagney = Character("Chad", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    
    ## Tags
    # Common Character Tags
    kagney.add_tags('first_visit', 'no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Locations

 
    ## Actions
    kagney.action_invoke_hypno_trigger = kagney.add_action("Invoke Her Hypno Trigger", label = "_invoke_hypno_trigger", condition = "kagney.can_be_interacted and kagney.has_tag('trigger_implanted')")
    
    # Talk actions
    #kagney.action_debug = kagney.add_action("DEBUG", label = "_seduce", condition = "kagney.can_be_interacted and kagney.status == 'on_training' and kagney.debug_mode == 'true'")
    kagney.action_talk = kagney.add_action("Talk with Kagney", label = "_talk", condition = "kagney.can_be_interacted and kagney.status == 'on_training' and not kagney.has_tag('talk_nothing')")
    kagney.action_seduce = kagney.add_action("Seduce Her", label = "_seduce", condition = "kagney.can_be_interacted and kagney.status == 'on_training'")
    kagney.action_study = kagney.add_action("Help her Study", label = "_study", condition = "kagney.can_be_interacted and kagney.status == 'on_training'")
    kagney.action_school = kagney.add_action("Send Kagney to School", label = "_school", condition = "kagney.can_be_interacted and kagney.status == 'on_training' and kagney.has_tag('slutty_at_school')")
    kagney.action_sex = kagney.add_action("Have Sex", label = "_sex", condition = "kagney.can_be_interacted and kagney.status == 'on_training'")
    kagney.action_home = kagney.add_action("Send Her Home", label = "_end_session", condition = "kagney.status == 'on_training' and not kagney.has_tag('first_visit') and kagney.in_area('house')")
    

    
    ## Expandable Menus
    # Talk
    kagney_talk_menu = ExpandableMenu("What do you want to talk about?")
    kagney.choice_talk_her =  kagney_talk_menu.add_choice("Talk about her", "kagney_talk_her", condition = "not kagney.has_tag('talk_her')")
    kagney.choice_talk_chad =  kagney_talk_menu.add_choice("Talk about Chad", "kagney_talk_chad", condition = "not kagney.has_tag('talk_chad')")
    kagney.choice_talk_father =  kagney_talk_menu.add_choice("Talk about her father", "kagney_talk_father", condition = "not kagney.has_tag('talk_father')")
    kagney.choice_talk_you =  kagney_talk_menu.add_choice("How do feel about me?", "kagney_talk_you", condition = "not kagney.has_tag('talk_you') and kagney.seduce_count >= 1")
    kagney.choice_talk_anal =  kagney_talk_menu.add_choice("Talk about Anal Sex", "kagney_talk_anal", condition = "not kagney.has_tag('talk_anal') and kagney.anal_count >= 1")
    kagney.choice_talk_nothing =  kagney_talk_menu.add_choice("Nothing", "kagney_talk_nothing", condition = "kagney.has_tag('talk_her') and kagney.has_tag('talk_chad') and kagney.has_tag('talk_father') and kagney.has_tag('talk_you') and not kagney.has_tag('talk_nothing')")
    
    # Weekend
    kagney_weekend_training_menu = ExpandableMenu("What do you have in mind for Kagney this weekend?", pre_label = 'kagney_pre_weekend', post_label = 'kagney_post_weekend')
    kagney.choice_weekend_acting =  kagney_weekend_training_menu.add_choice("Focus on her Acting Skills", "kagney_weekend_acting", condition = "kagney.acting_count < 2")
    kagney.choice_weekend_physical =  kagney_weekend_training_menu.add_choice("Focus on her Physical Skills", "kagney_weekend_physical")
    kagney.choice_weekend_date =  kagney_weekend_training_menu.add_choice("Take her on a date", "kagney_weekend_date")
    
    ## Hypnosis
    # Hypno Action Definition
    kagney.add_hypno_actions() # this adds all the standard options
    
    # hypno_trigger_sessions_threshold sets when the _implant_trigger label runs
    kagney.hypno_trigger_sessions_threshold = 1

    ## Other
    kagney.change_status("available_to_be_client")

    # Start Day Events (5 is default priority order, lower numbers run earlier, later numbers run later)
    start_day_labels.append('kagney_start_day_early_events', priority = -25) # runs earlier than other start day events
    start_day_labels.append('kagney_start_day', priority = 5)
    # note end_day and end_week labels do not need this command, only start_day labels

    ########### VARIABLES ###########
    # Common Character Variables
    kagney.add_stats_with_value('sex_count','visit_count','anal_count','hypno_count')

    # Character Specific Variables
    kagney.add_stats_with_value('acting_count','physical_count','study_count','school_count','seduce_count','event_week')
    kagney.fallout_path = "None"
    kagney.debug_mode = "true"
    kagney.mobile_mode = "FALSE"
return

label kagney_debug:
    $ title = "What do you want to do?"
    menu kagney_debug_menu:
        "Stats":
            $ title = "Which Stat?"
            menu kagney_debug_stats_menu:   
                "Desire":
                    "She currently has [kagney.desire] Desire"
                    $title = "Adjust by how much?"
                    menu kagney_stats_desire_menu:
                        "+ 10":
                            $ kagney.desire = kagney.desire + 10
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                    
                        "+ 5":
                            $ kagney.desire = kagney.desire + 5
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                    
                        "+ 1":
                            $ kagney.desire = kagney.desire + 1
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                                
                        "Custom" if kagney.mobile_mode == "FALSE":
                            $ player_value = int(renpy.input("Set to which value?", length=10, allow="-0123456789"))
                            $ kagney.desire = player_value
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                    
                        "- 1":
                            $ kagney.desire = kagney.desire - 1
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                    
                        "- 5":
                            $ kagney.desire = kagney.desire - 5
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                                
                        "- 10":
                            $ kagney.desire = kagney.desire - 10
                            "She now has [kagney.desire] Desire"
                            call kagney_stats_desire_menu
                            
                        "Back to Stats Menu":
                            call kagney_debug_stats_menu
                            
                        "Exit":
                            return

                "Resistance":
                    "She currently has [kagney.resistance] Resistance"
                    $title = "Adjust by how much?"
                    menu kagney_stats_resistance_menu:
                        "+ 10":
                            $ kagney.resistance = kagney.resistance + 10
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                    
                        "+ 5":
                            $ kagney.resistance = kagney.resistance + 5
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                    
                        "+ 1":
                            $ kagney.resistance = kagney.resistance + 1
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                                
                        "Custom" if kagney.mobile_mode == "FALSE":
                            $ player_value = int(renpy.input("Set to which value?", length=10, allow="-0123456789"))
                            $ kagney.resistance = player_value
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                    
                        "- 1":
                            $ kagney.resistance = kagney.resistance - 1
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                    
                        "- 5":
                            $ kagney.resistance = kagney.resistance - 5
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                                
                        "- 10":
                            $ kagney.resistance = kagney.resistance - 10
                            "She now has [kagney.resistance] Resistance"
                            call kagney_stats_resistance_menu
                            
                        "Back to Stats Menu":
                            call kagney_debug_stats_menu
                            
                        "Exit":
                            return

                "Sense of Self":
                    "She currently has [kagney.sos] Sense of Self"
                    $title = "Adjust by how much?"
                    menu kagney_stats_sos_menu:
                        "+ 10":
                            $ kagney.sos = kagney.sos + 10
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                    
                        "+ 5":
                            $ kagney.sos = kagney.sos + 5
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                    
                        "+ 1":
                            $ kagney.sos = kagney.sos + 1
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                                
                        "Custom" if kagney.mobile_mode == "FALSE":
                            $ player_value = int(renpy.input("Set to which value?", length=10, allow="-0123456789"))
                            $ kagney.sos = player_value
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                    
                        "- 1":
                            $ kagney.sos = kagney.sos - 1
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                    
                        "- 5":
                            $ kagney.sos = kagney.sos - 5
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                                
                        "- 10":
                            $ kagney.sos = kagney.sos - 10
                            "She now has [kagney.sos] Sense of Self"
                            call kagney_stats_sos_menu
                            
                        "Back to Stats Menu":
                            call kagney_debug_stats_menu
                            
                        "Exit":
                            return

                "Submission":
                    "She currently has [kagney.submission] Submission"
                    $title = "Adjust by how much?"
                    menu kagney_stats_submission_menu:
                        "+ 10":
                            $ kagney.submission = kagney.submission + 10
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                    
                        "+ 5":
                            $ kagney.submission = kagney.submission + 5
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                    
                        "+ 1":
                            $ kagney.submission = kagney.submission + 1
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                                
                        "Custom" if kagney.mobile_mode == "FALSE":
                            $ player_value = int(renpy.input("Set to which value?", length=10, allow="-0123456789"))
                            $ kagney.submission = player_value
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                    
                        "- 1":
                            $ kagney.submission = kagney.submission - 1
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                    
                        "- 5":
                            $ kagney.submission = kagney.submission - 5
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                                
                        "- 10":
                            $ kagney.submission = kagney.submission - 10
                            "She now has [kagney.submission] Submission"
                            call kagney_stats_submission_menu
                            
                        "Back to Stats Menu":
                            call kagney_debug_stats_menu
                            
                        "Exit":
                            return

                "Training Duration":
                    "She currently has [kagney.training_period] weeks Training Duration"
                    $title = "Adjust by how much?"
                    menu kagney_stats_training_period_menu:
                        "+ 10":
                            $ kagney.training_period = kagney.training_period + 10
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                    
                        "+ 5":
                            $ kagney.training_period = kagney.training_period + 5
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                    
                        "+ 1":
                            $ kagney.training_period = kagney.training_period + 1
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                                
                        "Custom" if kagney.mobile_mode == "FALSE":
                            $ player_value = int(renpy.input("Set to which value?", length=10, allow="-0123456789"))
                            $ kagney.training_period = player_value
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                    
                        "- 1":
                            $ kagney.training_period = kagney.training_period - 1
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                    
                        "- 5":
                            $ kagney.training_period = kagney.training_period - 5
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                                
                        "- 10":
                            $ kagney.training_period = kagney.training_period - 10
                            "She now has [kagney.training_period] weeks Training Duration"
                            call kagney_stats_training_period_menu
                            
                        "Back to Stats Menu":
                            call kagney_debug_stats_menu
                            
                        "Exit":
                            return

                "Back to Debug Menu":
                    call kagney_debug_menu
                
                "Exit":
                    return
        "Variables":
            $ title = "Which variable?"
            menu kagney_debug_var_menu:
                "Sex Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_sex:
                        "0":
                            $ kagney.sex_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.sex_count = 1
                            call kagney_debug_var_menu
                "Anal Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_anal:
                        "0":
                            $ kagney.anal_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.anal_count = 1
                            call kagney_debug_var_menu
                    call kagney_debug_var_menu
                "Hypno Count":
                    call kagney_debug_var_menu
                "Acting Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_acting:
                        "0":
                            $ kagney.acting_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.acting_count = 1
                            call kagney_debug_var_menu
                    call kagney_debug_var_menu         
                "Physical Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_physical:
                        "0":
                            $ kagney.physical_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.physical_count = 1
                            call kagney_debug_var_menu
                        "2":
                            $ kagney.physical_count = 2
                            call kagney_debug_var_menu
                "Seduce Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_seduce:
                        "0":
                            $ kagney.seduce_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.seduce_count = 1
                            call kagney_debug_var_menu
                "Study Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_study:
                        "0":
                            $ kagney.study_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.study_count = 1
                            call kagney_debug_var_menu
                        "2":
                            $ kagney.study_count = 2
                            call kagney_debug_var_menu
                        
                        "3":
                            $ kagney.study_count = 3
                            call kagney_debug_var_menu
                        "4":
                            $ kagney.study_count = 4
                            call kagney_debug_var_menu
                        "5":
                            $ kagney.study_count = 5
                            call kagney_debug_var_menu
                "School Count":
                    $ title = "Which Value?"
                    menu kagney_debug_var_school:
                        "0":
                            $ kagney.school_count = 0
                            call kagney_debug_var_menu
                        "1":
                            $ kagney.school_count = 1
                            call kagney_debug_var_menu
                        "2":
                            $ kagney.school_count = 2
                            call kagney_debug_var_menu
                "Fallout Path":
                    $ title = "Which Value?"
                    menu kagney_debug_var_fallout:
                        "Chad":
                            call kagney_debug_var_menu
                        "Father":
                            call kagney_debug_var_menu
                            
                "Back to Debug Menu":
                    call kagney_debug_menu
                    
                "Exit":
                    return
        "Exit":
            return
return

# NEED add massage set w/ Lauren if masseuse, once Lauren content expanded

# Initial Contact Message
# OBJECT: Check Messages
label kagney_message:
  # this is message you get when the prospective client first becomes available to be a client
  # note: minor character dialogue does not have .c at the end of it, only major characters
  father_kagney "{i}Hello! I'm reaching out to you today because of something my friend said about your services.{/i}"
  father_kagney "{i}He had mentioned that you are a remarkable instructor and you sound perfect for my needs.{/i}"
  father_kagney "{i}I believe you're the perfect match for my daughter! She is in great need of a tutor!{/i}"
  father_kagney "{i}See my daughter Kagney always has and always will be my pride and joy. She's a very bright and passionate girl but... {/i}"
  father_kagney "{i}Of late her grades have been going down... I've heard from her friends that she's now become interested in a young man at her school.{/i}"
  father_kagney "{i}While I do not personally have anything against her dating... I feel as if this might ruin her future after she graduates.{/i}"
  father_kagney "{i}She used to love reading and studying but... Now all she does is hang out on her phone and go visit this... Boy of hers.{/i}"
  father_kagney "{i}Please. I want my daughter to have a good future ahead of her. If she lets this chance slip... I fear she'll never get it again. Please help my daughter!{/i}"
  father_kagney "{i}I believe you're the perfect match for my daughter! She is in great need of a tutor!{/i}"
  player.c "{i}I don't think this man quite understands what I do.{/i}"
  player.c "{i}But I've trained stranger women before. This could be a new experience{/i}"
  call consider_contract(kagney, "Reply to [kagney.full_name]'s Father")
  if yesno == True:
    sys "You accept the assignment.  You have until the end of week [kagney.training_limit] to complete it."
return

# Client Rejected
label kagney_rejected:
  # this is message you get when a client can no longer be trained
  sys "You can no longer train [kagney.full_name]."
return

label kagney_update_media:
    if kagney.has_tag('first_visit'):
        $ kagney.change_image('kagney_student_intro_1_1')
    elif kagney.status == 'on_training' and current_location in session_locations:
        $ kagney.change_image('kagney_student_intro_1_5')
    else:
        $ kagney.change_image('kagney_student_intro_1_14')
return
    
label kagney_description_display:
    if kagney.status == "on_training":
        "You have until the end of week [kagney.training_limit] to complete this engagement."
    elif kagney.has_tag('satisfied'):
        "Satisfied PLACEHOLDER"
    "[kagney.statblock]"
    $ items = ", ".join(i.name for i in kagney.get_items()) if kagney.get_items() != [] else ' Nothing'
    "You have given her: [items]"
return

label kagney_review_files:
    call kagney_update_media
    wt_image kagney.image
    call kagney_description_display
    wt_image current_location.image
return

label kagney_end_training:
    if kagney.desire >= 75 and kagney.sos >= 60 and kagney.study_count >= 4 and kagney.hypno_count == 0 and not kagney.has_tag('talk_you'):
        "At the end of Kagney’s Training Period you get an email from Kagney’s Father."

        father_kagney "Kagney’s Graduating! My baby girl not only graduated but she got accepted into the University of her dreams!"
        father_kagney "She… We couldn’t have gotten this far without you. I owe you so much for getting my baby girl this far."
        father_kagney "I will make sure others know of the great man you are. Thank you from the bottom of my heart."

        "After closing the email you see one from Kagney and you open it."
        wt_image kagney_student_intro_1_2
        kagney.c "I graduated! I’m sure daddy has already told you but I wanted to let you know in case he hadn’t!"
        wt_image kagney_student_intro_1_2
        kagney.c "I’m sorry but it looks as if I’m moving away. I got an offer from a University out of state… I… I just really want to thank you."
        wt_image kagney_student_intro_1_2
        kagney.c "I’m always going to remember what you taught me and maybe in a few years… We’ll meet again? Hopefully."
        wt_image kagney_student_intro_1_3
        kagney.c "Thank you and… I’m going to miss you. XOXOXOXOXOX"

        player.c "She’s a good kid. Hopefully she enjoys herself at University. I’m hoping she makes a strong name for herself. In fact… I know she will."
        call convert(kagney,"satisfied", False, True)
        
    elif kagney.desire >= 75 and kagney.sos >= 60 and kagney.study_count >= 4 and kagney.hypno_count == 0 and kagney.has_tag('talk_you') and kagney.has_tag('love_potion_used'):
        father_kagney "At first I was nervous contacting you but… It was the greatest decision of my life!"
        father_kagney "Kagney graduated and it’s all thanks to you! I got to see my baby walk on stage and receive her diploma… I’ve never been prouder of her."
        father_kagney "She also got an offer letter from a well known University but she turned it down. Said she wanted to go to school locally for a special \"reason\"."
        father_kagney "I won’t pry. She’s going to do amazing things and the University she’s attending is still fantastic!"
        father_kagney "I don’t care how I do it but I will spread your name as far and wide as I can! You sir are a scholar and a gentleman. I owe you… Everything. Thank you!"

        "A few minutes after reading the email, you see another one from Kagney"
        wt_image kagney_student_intro_1_3
        kagney.c "Heya! I’m sure daddy already told you but I graduated! I wanted to invite you to my graduation but my family took all the invites..."
        wt_image kagney_student_intro_1_3
        kagney.c "Anyways… I um… Decided to attend a local university. So I could… No we should talk about this in person. It’ll be fun!"
        wt_image kagney_student_intro_1_3
        kagney.c "My daddy already knows I want to still see you,  so if you ever want to… Hang out or something… Call me okay? See you soon XOXOXOX"

        player.c "I may not be a tutor but this went over well. Kagney staying in town is a plus. I’ll have to call her up soon and find the reason for why she stayed."
        call convert(kagney,"satisfied", False, True)
    elif kagney.desire >= 60 and kagney.sos <= 30 and kagney.submission >= 60 and kagney.school_count == 2 and kagney.has_tag('trigger_implanted') and not kagney.fallout_path == "None":
        "At the end of Kagney’s Training Period you get an email from Kagney’s Father."

        father_kagney "I’m reaching out to let you know that the deal we had in place is now over."
        father_kagney "My baby girl ended up dropping out of school… Part of me regrets not pushing her enough but… It is what it is."
        father_kagney "Thanks for trying I guess... "

        wt_image kagney_student_slutty_2_5
        "As you finish the email, there’s a knock at your door. You open to find the scantily clad Kagney looking sexy as ever." 
        wt_image kagney_student_slutty_2_6
        kagney.c "Hey! So good news! I was kicked out of that lousy school! Now I can focus on doing what I really like to do. Getting my pussy filled with cock!"
        wt_image kagney_student_slutty_2_6
        kagney.c "Dad blew a gasket but whatever… Anyways if you ever need a good little whore… Call me? I’m looking forward to seeing you more hehe."
        wt_image kagney_student_slutty_2_7
        kagney.c "Also a few of my friends kinda know about you now. I gotta spread the word on how sexy you are after all. And your wonderful cock hehe."
        wt_image kagney_student_slutty_2_6
        kagney.c "Hopefully you find other nerdy girls to help out. Well I gotta go but if you ever want to have fun, call me? Take care… Professor"

        "You watch the sexy Kagney walk away with a smile on your face. You look forward to seeing more of your little slut as well..."
        call convert(kagney,"satisfied", False, True)
    else:
        "The training period for Kagney has ended and you’ve failed to live up to Kagney’s Fathers wishes. He sends you a quick email saying he expected better and forbids you from seeing Kagney again..."
        call convert(kagney,"unsatisfied", True, True)
return

label kagney_calling:
    if not kagney.can_be_interacted:
        "You had an evening session with Kagney earlier this week.  You need to wait until the weekend or next week for another session."
    else:
        if kagney.has_tag('first_visit'):
            call forced_movement(living_room)
            "You call the daughter named Kagney and set up a time."
            "You hear your door bell go off and head to open the door expecting a your every day nerd."
            wt_image kagney_student_intro_1_1
            "You open the door and are surprised by the gorgeous blonde in front of you."
            summon kagney no_follows

            "Her large breasts and beautiful body distract you from how nervous she appears on the surface."
            "You welcome her inside and show her to the living room."
            player.c "Am I under the impression you understand why you're here today?"
            wt_image kagney_student_intro_1_2
            kagney.c "I... Think so? My father said you were a tutor. To be honest I kind of... Looked you up online before I arrived."
            player.c "And what did you find?"
            kagney.c "I found an ad that said you were a Wife Trainer... Um I think my father was mistaken when he sent me here"
            player.c "He wasn't lying, I am an instructor. I help women such as yourself find their way in life. It just so happens that I train women as well."
            wt_image kagney_student_intro_1_3
            player.c "Now tell me Kagney. Your father mentioned that you're seeing a boy at your school."
            kagney.c "Y...Yeah. He's the quarterback on the football team."
            player.c "Ah. And he's taken a liking to you?"
            kagney.c "Yes. I don't know why he suddenly paid attention to me but my friends heard him saying I was cute and wanted my number."
            wt_image kagney_student_intro_1_2
            player.c "Interesting. How does your father feel about this boy?"
            kagney.c "He... Said I should date once I graduate..."
            wt_image kagney_student_intro_1_1
            kagney.c "He... Just wants me to get into a good college. To be honest I know my grades have gone down but... Chad's been very distracting of late."
            wt_image kagney_student_intro_1_2
            player.c "I can see two big reasons why he's taken a liking to you. How do you feel about him?"
            kagney.c "I mean he's very popular but... I've heard rumors about him... Seeing other girls. I want to focus on my grades like daddy suggested but Chad's been..."
            player.c "Distracting you. Well Kagney I have plenty of things we can try."
            kagney.c "Like... What?"
            wt_image kagney_student_intro_1_3
            player.c "I can help you gain more focus to study. I could teach you how to flirt with this Chad Or..."
            player.c "I can help you develop ways of passing without really putting in additional effort."
            wt_image kagney_student_intro_1_2
            kagney.c "You mean... Cheat. I don't know... I'm still not sure if I should even stay..."
            wt_image kagney_student_intro_1_1
            player.c "Let me spend some time with you and then you can decide if you want to continue with my services. Fair?"
            wt_image kagney_student_intro_1_3
            "Kagney pauses but soon nods. You rub your hands together as you plan out your courses with Kagney."
            $ kagney.visit_count += 1
            rem tags 'first_visit' 'no_hypnosis' from kagney
            call character_location_return(kagney)
            end_day
        else:
            call forced_movement(living_room)
            summon kagney no_follows
            $ kagney.visit_count += 1
return  

label kagney_examine:
    call kagney_update_media
    wt_image kagney.image
    "Kagney's Father asked you to help his daughter find focus in her school work again."
    call kagney_description_display
return

# Weekend Actions
label kagney_pre_weekend:
    add tag 'checking_for_weekend' to kagney
return

label kagney_post_weekend:
    if kagney.has_tag('checking_for_weekend'):
        rem tag 'checking_for_weekend' from kagney
    else:
        if kagney.has_tag('failed_regular_training_this_week'):
            rem tag 'failed_regular_training_this_week' from kagney
            $ player.extra_clients_fee_this_week += kagney.pay
return

label kagney_weekend:
  if player.energy >= energy_long.value and kagney.has_tag('talk_her'):
    call expandable_menu(kagney_weekend_training_menu)
  else:
    if not kagney.has_tag('talk_her'):
        player.c "The more I think I know what a girl Kagney's age likes to do... The less certain I am she won't enjoy it."
        player.c "Before I get ahead of myself, I should speak with her and learn what her hobbies are. I can plan a weekend after that."
    else:
        sys "You don't have enough energy for this action, choose something else."
return

label kagney_weekend_acting:
    rem tag 'checking_for_weekend' from kagney
    $ kagney.training_session()
    summon kagney
    if kagney.acting_count == 0:
        "You call up Kagney and invite her to an acting course you found online. She sounded very excited which is a good sign." 
        "Upon arriving you look at what roles are available but Kagney is the one who chooses for you."
        wt_image kagney_student_acting_1_1
        "An hour later, Kagney and yourself are dressed as doctor and patient respectively"
        wt_image kagney_student_acting_1_2
        "Kagney was beautiful before but seeing her in a doctor’s coat truly casts a spotlight over her. You almost forget you’re having to pretend as Kagney starts the show quickly."
        wt_image kagney_student_acting_1_3
        "The script you read told you that you’re Kagney’s patient and Kagney is in the middle of waiting for your lab results"
        "You blindly follow along but grow bored. Kagney on the other hand has an excitable air around her."
        wt_image kagney_student_acting_1_4
        "You forget where you are multiple times as Kagney’s outfit continues to distract you from the task at hand. After a while it would seem Kagney is also growing bored."
        wt_image kagney_student_acting_1_5
        "Pulling out the other scenes you can do, she asks you to sit with her. Your eyes start moving towards her breasts."
        wt_image kagney_student_acting_1_6
        "Flipping through the scenes, she takes notice of your gaze and a coy smile appears."
        kagney.c "You know what? Why don’t we use these things? I’ve already seen them on tv but never used one. Come, it’ll be fun!"
        "Kagney spreads her legs and exposes the white panties underneath. She again follows your gaze and begins to blush. You hear her heartbeat which is beating very fast. Is she excited right now?"
        wt_image kagney_student_acting_1_7
        "As you listen to her heartbeat, her hand works on unbuttoning your shirt. You just got the answer to your question."
        wt_image kagney_student_acting_1_8
        "Things begin to grow hot and heavy as Kagney removes her own shirt. With her heart beating rapidly using the tool, you ask one more question."
        player.c "Should I push for more?"
        $ title = "Should I push for more?"
        menu:
            "Yes":
                if kagney.desire > 25:
                    player.c "You know Doctor, I hear bras that are too tight can restrict blood flow. Care to test that?"
                    wt_image kagney_student_acting_1_9
                    "Kagney smiles and gets up to remove her bra. As it falls to the floor she turns around and wiggles her nice round ass in your face."
                    wt_image kagney_student_acting_1_10
                    kagney.c "Now that we got your blood pumping, let’s check your vitals… Oh no! It seems a mass amount of blood is draining elsewhere!"
                    wt_image kagney_student_acting_1_11
                    "Agreeing with the beautiful doctor, you use the stethoscope to locate the source. As it glides over her round ass you find it."       
                    wt_image kagney_student_acting_1_12
                    "Spreading her legs you dive in to lick her wet pussy. Your tongue laps away at every fold as Kagney eagerly gives you your medicine."
                    wt_image kagney_student_acting_1_13
                    kagney.c "Now that the medicine has entered your body, we must now perform oral surgery at the source. As your doctor… I’ll gladly perform this operation hehe."
                    wt_image kagney_student_acting_1_14
                    "Kagney takes out your bulging cock and recoils at its size. She notes that she must work quickly or she might lose you."
                    wt_image kagney_student_acting_1_15
                    "Wrapping her soft lips around your member, she licks and sucks your cock with great care. Every inch is swallowed into her tight little throat."
                    wt_image kagney_student_acting_1_16
                    kagney.c "Mmmmm. There’s an unknown leakage. I’ll have to save it in my slutty mouth for further analysis."
                    wt_image kagney_student_acting_1_17
                    "The blonde bombshell licks every drop of pre-cum from your cock and tries to draw out even more."
                    wt_image kagney_student_acting_1_18
                    "Kagney pushes you on the bed and continues her delicate care for her patient. Smiling up at you, you can tell she’s the best doctor around for this."
                    wt_image kagney_student_acting_1_19
                    kagney.c "So big *Slurp* So thick! It would seem I need more tools to help with the procedure. Can I introduce you to my twin assistants?"
                    wt_image kagney_student_acting_1_20
                    "Pulling herself up she wraps her perfectly round breasts around your hard cock. Her soft mounds further drive you to the brink."
                    wt_image kagney_student_acting_1_21
                    "Minutes later your cock is back inside Kagney’s throat. The room erupts in the sounds of gagging as the king doctor applies lubrication for what comes next."
                    wt_image kagney_student_acting_1_22
                    kagney.c "Mmmm. There’s one more procedure left before you’re eligible for discharge… Now bring that cock over and fuck me!"
                    wt_image kagney_student_acting_1_23
                    "Not wanting to ignore your beautiful doctor’s advice, you thrust your member into her drenched hole. Kagney’s voice desperately tells you to fuck her harder."
                    wt_image kagney_student_acting_1_24
                    "Spreading herself wider, your cock enters her inner depths. Your balls go on to slap her clit, further stimulating Kagney."
                    wt_image kagney_student_acting_1_25
                    kagney.c "You’re doing so good! Ah! Your stamina is… Ah! Incredible! Keep going… Please keep going!"
                    wt_image kagney_student_acting_1_26
                    "The lust drives the two into the bed as your cock thrusts hard into her. Kagney looks up at you and you can see how much devotion reflects in her eyes."
                    wt_image kagney_student_acting_1_27
                    "Moments later, your doctor is bouncing eagerly on your cock. Her fat ass bounces all around as you playfully slap it around."
                    wt_image kagney_student_acting_1_28
                    kagney.c "You’re doing so good! Ah! Fuck! This procedure is going to make me cum… Ah! I’m such a dirty girl! I’m such a naughty doctor!"
                    wt_image kagney_student_acting_1_29
                    "Kagney turns around and soon spots a camera recording the acting session. The fact that they’re being recorded sends chills down her spine… And makes her pussy even wetter."
                    wt_image kagney_student_acting_1_30
                    "With one last bounce, Kagney’s body quivers in delight. Her legs shake and her voice breaks as her orgasm ravages her tight body."
                    wt_image kagney_student_acting_1_31
                    "With a shaky voice she kisses you and soon begs for you to cum on her. Climbing off she soon takes her position."
                    kagney.c "It’s time… You’ve done such a good job as a patient… All that’s left is to dump all your stress on me. Dump it all over your doctor. Do it!"
                    wt_image kagney_student_acting_1_32
                    "Streams of cum land on her gorgeous face. Her hungry tongue laps away any cup that makes contact with it. Soon your load covers your gorgeous doctor."
                    wt_image kagney_student_acting_1_33
                    kagney.c "God.. You did so well today… As your doctor I can confidently tell you that you’re ready to be discharged… Good work..."
                    wt_image kagney_student_acting_1_34
                    "As you recover from the acting session, you also spot the camera nearby. Bringing it closer you zoom in on the exhausted Kagney. With a wink she fingers her pussy and says goodbye."
                    "You pull the memory card out and pocket it… A lovely memento of your weekend together."
                    "Soon you both leave the studio behind and after a gentle kiss goodbye, you drop Kagney off at home. It would seem she really enjoyed the weekend. You know you did…"
                    change player energy by -35
                    change kagney desire by 5
                    change kagney submission by 5
                    change kagney sos by 10
                    notify
                else:
                    wt_image kagney_student_acting_1_8
                    "Despite your best efforts, Kagney’s interests in the scene start to dwindle. You have a feeling that if you were closer, you could get her to have more fun with the role." 
                    "Even if the day ended in a bust, Kagney enjoyed her weekend with you. You hope the next time you do the scene, Kagney’s more on board to try something else..."
            "No":
                wt_image kagney_student_acting_1_6
                "The allure of hearing heartbeats quickly wears off and Kagney doesn’t find anything else they can act in today."
                "You remove the doctor's clothing and you take Kagney home. Next weekend you hope you can try for a little more."
    elif kagney.acting_count == 1:
        "Upon telling Kagney you were going back to the acting course, she screamed happily over the phone. Within the same hour, you both arrive and Kagney again takes point."
        "The scene this time around is of a happily married man and the unruly maid under his current employment."
        wt_image kagney_student_acting_2_1
        "Your costume was very normal but Kagney’s took some time to put on. Soon she walked on set looking absolutely ravishing."
        wt_image kagney_student_acting_2_2
        "Getting into character she begins to walk around and knock things over while also pouring herself some champagne."
        wt_image kagney_student_acting_2_3
        "Noticing the camera in the room, she flips her skirt up and aims her nice round ass towards it. You AND the camera get an eye full…"
        wt_image kagney_student_acting_2_4
        kagney.c "I’m so bored… Ugh I don’t want to clean today… Fuck it, what’s the worst the boss can do?"
        wt_image kagney_student_acting_2_5
        "It’s your cue to enter as you play the role of a man tired of his maid’s laziness and unruly behavior. "
        "Trying to do your best, you lay into Kagney as she rolls her eyes. For a few moments you’re bewildered at her acting skill… She truly has the talent for this.."
        wt_image kagney_student_acting_2_6
        "After a few moments, you decide now might be the best time to improvise… Do you want to truly push this character on kagney.c "
        $ title = "Do you want to truly push this character on Kagney?"
        menu:
            "Yes":
                if kagney.desire > 40 and kagney.submission > 40:
                    wt_image kagney_student_acting_2_6
                    player.c "I’m tired of you being a lazy maid. I have one last task for you and if you fail it… You’re fired!"
                    wt_image kagney_student_acting_2_7
                    kagney.c "But I really need this job… Please I’ll do anything to make you happy. Anything..."
                    wt_image kagney_student_acting_2_8
                    "Kagney moves her hand down and gropes your cock. You smirk at the slutty maid in front of you as you pull her over to the bed."
                    wt_image kagney_student_acting_2_9
                    "Pulling down your pants, your erect member bounces free. Kagney’s face opens in surprise as you’re once again impressed with her acting."
                    wt_image kagney_student_acting_2_10
                    kagney.c "It’s so big! I… I promise to work hard… I’ll stop being a lazy maid… Master."
                    wt_image kagney_student_acting_2_11
                    "Kagney takes your balls in her mouth as your cock grows to full size. She awes at your size and rubs her entire face on your cock."
                    wt_image kagney_student_acting_2_12
                    "Kagney’s tight mouth is soon bobbing and slurping your cock. Getting into the role more, you start calling Kagney your slutty maid."
                    wt_image kagney_student_acting_2_13
                    kagney.c "Yes Master… I promise I’ll clean your cock really well. Anytime you want, I’ll clean it for you Master!!"
                    wt_image kagney_student_acting_2_14
                    "You lay your head on the pillow as your slutty maid services your cock. The sounds that fill the room are music to your ears. Kagney herself is also getting into her new role."
                    wt_image kagney_student_acting_2_15
                    "Despite struggling, Kagney continues to fit your large cock in her mouth. She even forced your cock through her cheek. The sensation further makes your cock quiver in delight."
                    wt_image kagney_student_acting_2_16
                    kagney.c "Oh Master! Your cock is the largest I’ve ever seen! I’m so lucky to serve such a naughty thing. Thank you for being so kind to your slutty Maid. Thank you!"
                    wt_image kagney_student_acting_2_17
                    "When Kagney meant she was happy to serve your cock, she meant it." 
                    wt_image kagney_student_acting_2_18
                    "With one last push into her throat, your maid soon got up and put her feet on your member."
                    wt_image kagney_student_acting_2_19
                    kagney.c "Does that feel good Master? My naughty little feet on this giant thing? Mmmmm yes, my feet will serve your cock too. Mmmmm. It’s so hot on my little toes!"
                    wt_image kagney_student_acting_2_20
                    player.c "Your feet feel good my little slutty maid… But I want something else. Bring that ass over here... It’s time I break it in."
                    wt_image kagney_student_acting_2_21
                    "Feeling as if the persona you’ve created for yourself has taken over, you soon push your cock into Kagney’s tight little asshole."
                    wt_image kagney_student_acting_2_22 
                    "While Kagney did wince and seemed to pull away from you, she soon accepted her role. Soon her moans filled the room while you stretched out her asshole."
                    wt_image kagney_student_acting_2_23
                    kagney.c "AHHHHHH! Master this is… So wrong! I thought you would AH! Want my pussy… Never my poor little ass! Ahhhh!"
                    wt_image kagney_student_acting_2_24
                    player.c "It’s how I punish all the disobedient little maids out there. Now tell me how much you enjoy my cock in your ass. Your master demands it!"
                    wt_image kagney_student_acting_2_25
                    kagney.c "Ah! Master your cock feels so good in my butt! It’s stretching me out but I… but I like it! This is what slutty maids deserve! I’m so sorry Master!"
                    wt_image kagney_student_acting_2_26
                    "You push Kagney to her knees and again thrust your cock into her backdoor. Her moans don’t really tell you if she’s moaning in pain or pleasure." 
                    wt_image kagney_student_acting_2_27
                    "Every thrust soon becomes easier. Her asshole is fully open to your thick member so you speed up to Kagney’s delight." 
                    wt_image kagney_student_acting_2_28
                    kagney.c "Right there! Oh god it feels so FUCKING good! Fuck my ass Master! Fuck your slutty maid stupid!"
                    wt_image kagney_student_acting_2_29
                    "Something in Kagney had finally snapped. Her hand moved to finger her dripping pussy as she begged you for more. The room was soon filled with her hungry voice begging you to fuck her harder."
                    wt_image kagney_student_acting_2_30
                    "Not wanting to do all the work, you commanded your slutty maid to ride your cock. She slipped your large cock back into her tight brown hole and rode you wildly."
                    wt_image kagney_student_acting_2_31
                    "Kagney began to spread her butt cheeks wider to fully take your cock inside. It would seem you had finally awakened something within the blonde bombshell."
                    wt_image kagney_student_acting_2_32
                    kagney.c "I’m going to cum Master! Your… Your fucking cock’s going to make me cum! AHHHHHH! I’m cumming from being fucked in the ass!"
                    wt_image kagney_student_acting_2_33
                    "Wanting to fully embrace her naughty side, you throw Kagney to the side and bring her into a deep kiss. She bites your lower lip as you can feel her orgasm wrecking her body."
                    wt_image kagney_student_acting_2_34
                    "Your cock does not stop as Kagney cums. You continue to destroy her poor little asshole and again make her admit how good it feels."
                    wt_image kagney_student_acting_2_34
                    "Over and over she tells you how much she loves getting fucked in the ass. Eventually her words become slurred and you cannot understand your slutty maid anymore."
                    wt_image kagney_student_acting_2_35
                    "With a few more thrusts you tell Kagney, you’re going to cum. She nods her head and licks her lips as if eagerly anticipating her snack."
                    wt_image kagney_student_acting_2_36
                    "Climbing to her knees she takes your cock in her mouth. Despite it being in her asshole for the past hour, she licks and kisses it lovingly."
                    wt_image kagney_student_acting_2_36
                    "You soon groan and unload your cum all over Kagney’s face and body. Your maid dips her fingers and eats every single drop while keeping eye contact with you. You point to the camera nearby and make Kagney describe what she’s doing."
                    wt_image kagney_student_acting_2_37
                    kagney.c "I’m eating my Master’s yummy cum like a good maid. I made sure his cock was as clean as possible."
                    wt_image kagney_student_acting_2_37
                    player.c "And how did you enjoy getting that tight little asshole spread open by your Master?"
                    wt_image kagney_student_acting_2_38
                    "Kagney smiles and kisses your cock. She licks it playfully and stares up at you with loving eyes."
                    wt_image kagney_student_acting_2_38
                    kagney.c "I can’t wait for Master to fuck my ass again… In fact… I’m looking forward to it hehe."
                    wt_image kagney_student_acting_2_37
                    "Both of you get cleaned up and changed into your regular clothing. You help Kagney to the car as her body begins to feel the after effects of her first anal pounding." 
                    wt_image kagney_student_acting_2_37
                    "You have an awkward talk with her father about why she can’t walk but he soon waves it off. Clutching on to the memory card from the camera, you can’t wait to rewatch your scene.... And the lovely Kagney once again." 
                    change player energy by -40
                    change kagney desire by 10
                    change kagney submission by 10
                    change kagney sos by 10
                    $ kagney.anal_count += 1
                    notify
                else:
                    wt_image kagney_student_acting_2_5
                    "Wanting to have more fun with the scene, you try to guide Kagney to be more naughty. This doesn’t work and you only make Kagney confused about the scenes and the lines." 
                    "On the car ride home she makes fun of your acting abilities but still sneaks in a compliment. You might want to get closer to Kagney before trying that scene again…"
                    $ kagney.acting_count -= 1
            "No":
                wt_image kagney_student_acting_2_6
                "Not knowing if Kagney is truly comfortable with it, you stick to the script. The scene goes on as nothing really happens. The scene ends with the maid learning a valuable lesson about hard work…"
                wt_image kagney_student_acting_2_5
                "Despite boring you, Kagney was ecstatic on the car ride home. She gives you a peck on the cheek and heads inside, leaving you wondering one thing. Improve might be the way to go for next week..."
                change player energy by -35
                change kagney desire by 1
                change kagney sos by 1
                notify
    $ kagney.acting_count += 1
    call character_location_return(kagney)
    end_day
return

label kagney_weekend_physical:
    rem tag 'checking_for_weekend' from kagney
    $ kagney.training_session()
    summon kagney
    if kagney.physical_count == 0:
        "You call up Kagney and tell her the weekend plans. You make sure to also notify her father to which he responds excitedly to it."
        wt_image kagney_student_weekend_2_1
        "You and Kagney soon arrive at your destination, the golf course. Kagney was a bit hesitant to play and you could see why." 
        wt_image kagney_student_weekend_2_2 
        "Everytime Kagney went to hit the ball, her breasts would make it difficult to do so." 
        wt_image kagney_student_weekend_2_2
        "Throughout the day you could sense Kagney was getting more and more frustrated. You soon think golfing was a mistake…"
        wt_image kagney_student_weekend_2_3
        "On the final hole of the day, you started noticing Kagney’s posture was completely off. Should you physically guide her?"
        $ title = "Should you physically guide her?"
        menu:
            "Yes":
                wt_image kagney_student_weekend_2_2
                "You get behind Kagney but she only groans as her grip on her club tightens."
                if kagney.desire > 30 and kagney.sos >50:
                    wt_image kagney_student_weekend_2_2
                    player.c "Kagney relax. Take a deep breath and fix your posture like this."
                    wt_image kagney_student_weekend_2_3
                    "You get behind Kagney and guide her body where it needs to be. Finally you tell her to swing and her ball lands very close to the hole." 
                    wt_image kagney_student_weekend_2_3
                    "She happily jumps up and down before giving you a hug." 
                    wt_image kagney_student_weekend_2_3
                    "After finishing the game, you and her head back to the lodge where you notice she’s still tense." 
                    wt_image kagney_student_weekend_2_1
                    player.c "You know Kagney, I have a few other techniques to relax you. Would you be interested?"
                    wt_image kagney_student_weekend_2_1
                    "Kagney thinks about it and soon you and her find yourselves in an empty room. You soon bend Kagney over and start to massage her thighs."
                    wt_image kagney_student_weekend_2_1
                    "Would you like to push the massage?"
                    $ title = "Would you like to push the massage?"
                    menu:
                        "Yes":
                            if kagney.desire > 30:
                                wt_image kagney_student_weekend_2_1
                                player.c "Kagney you’re so wound up. I have a special massage I could give you. Are you interested?"
                                wt_image kagney_student_weekend_2_4
                                "Kagney bites her lip as you spread her ass. She nods at you as you run your thumb around her pussy." 
                                wt_image kagney_student_weekend_2_5
                                "Moments later, Kagney’s naked with her legs spread for you. You gently lick her pussy as you lap away the juices leaking out."
                                wt_image kagney_student_weekend_2_6
                                "Her pussy is not the only thing you massage as you begin to fondle her perfectly round breasts. After licking her nipple for a few moments, Kagney’s hands begin to fondle your growing erection." 
                                wt_image kagney_student_weekend_2_7
                                kagney.c "You’re so hard… Would… Would you like it if I massaged you as well?"
                                "You can’t say no to the gorgeous blonde and soon enough she’s bobbing up and down on your cock." 
                                wt_image kagney_student_weekend_2_8
                                "Her lips tightly wrap around your member as you force her head to go deeper. After coming up for air she purrs out a simple wish." 
                                wt_image kagney_student_weekend_2_8
                                kagney.c "Fuck me… Please… Fuck me."
                                wt_image kagney_student_weekend_2_9
                                "The sound of skin slapping together and Kagney’s lovely moans fill the room. Your hard cock quickly goes in and out of Kagney’s horny pussy." 
                                wt_image kagney_student_weekend_2_10
                                "She grabs hold of your leg and looks back at you with a lustful gaze. There’s only one thing in the entire world that Kagney wants right now. You."
                                wt_image kagney_student_weekend_2_11
                                "The fun continues as you flip Kagney on her back. Every thrust makes her breasts bounce around. Her eyes are completely glued to your cock filling up her naughty hole."
                                wt_image kagney_student_weekend_2_12
                                "The two of you fuck like animals as she start yelling out your name. Her pussy works hard to squeeze tightly around you."
                                wt_image kagney_student_weekend_2_13
                                "Kagneys wild side seems to come alive and eventually the blonde bombshell is riding your cock for dear life." 
                                wt_image kagney_student_weekend_2_14
                                "Her butt jiggles all around as her hands dig into your chest. Kagney’s moans escalate until you hear those 2 lovely words."
                                wt_image kagney_student_weekend_2_15 
                                kagney.c "I’m cumming!"
                                wt_image kagney_student_weekend_2_16
                                "Kagney starts fucking you in an intense fashion. Her body slams down on your cock as she desperately tries to shove your cock deeper into her."
                                wt_image kagney_student_weekend_2_17
                                kagney.c "I love you cock! Ah! Fuck me baby… Fuck me!"
                                wt_image kagney_student_weekend_2_18
                                "You hold off your orgasm in order to fuck Kagney a bit longer. While on her side you squeeze her beautiful breasts until the time comes for you to submit." 
                                wt_image kagney_student_weekend_2_19
                                "Pushing her to the floor, you douse Kagney in your seed. Hot streams of cum land on her face and hungry tongue." 
                                wt_image kagney_student_weekend_2_20
                                "Even after shooting your last load, Kagney licks and sucks your cock for more." 
                                wt_image kagney_student_weekend_2_21
                                "Her hand grips your cock tightly as she coaxes one final orgasm out of you. Your legs shake as she finally gets her fill of cum."
                                wt_image kagney_student_weekend_2_22
                                kagney.c "Mmmmm. So good. So… Are we always going to do this after golfing?"
                                wt_image kagney_student_weekend_2_22
                                "You chuckle as she gives your cock one final kiss before you get cleaned up." 
                                wt_image kagney_student_weekend_2_22
                                "You drop her off at home and after kissing your cheek goodbye, you see the sexy blonde enter her home. You’re going to have to be careful with this one… Before she sucks you completely dry."
                                change player energy by -40
                                change kagney desire by 5
                                change kagney sos by 10
                                notify
                            else:
                                wt_image kagney_student_weekend_2_1
                                kagney.c "Um… Thanks for the massage but I think we should leave… T… Thanks for taking me out golfing."
                                wt_image kagney_student_weekend_2_1
                                "You pull away and drive Kagney back to her father’s. You hope that next time your bond is close enough to push the massage."
                                change player energy by -35
                                change kagney desire by 1
                                notify

                        "No":
                            wt_image kagney_student_weekend_2_1
                            "While a massage could be helpful, you don’t want to make Kagney uncomfortable. You soon drop her off at her father’s house and plan next weekend’s outing."
                            change player energy by -35
                            change kagney desire by 1
                            notify
                else:
                    wt_image kagney_student_weekend_2_3
                    "Kagney is too tense or not used to you being this close to her. Her ball ends up landing in the sand and she angrily demands you take her home. Looks as if you might want to get closer to her before trying to guide her."
                    $ kagney.physical_count -= 1
            "No":
                wt_image kagney_student_weekend_2_2
                "You decide against putting your hands on Kagney. She seems too frustrated to do much with. You end up finishing the game and drop her back at her father’s home. You hope next time fares better."
                change player energy by -35
                change kagney desire by 1
                change kagney sos by -10
                notify
                $ kagney.physical_count -= 1
    
    elif kagney.physical_count == 1:
        "After seeing how much her bust interferes with learning sports, you decide it might be time to tighten up Kagney’s body." 
        wt_image kagney_student_weekend_excersize_2_1
        "You invite Kagney out to the gym and she comes along looking content. You soon arrive and find most of the gym empty, but it could be a blessing in disguise." 
        wt_image kagney_student_weekend_excersize_2_1
        "Kagney’s work out attire is nothing but a distraction. With Kagney around, nobody would be able to focus on their work out."
        wt_image kagney_student_weekend_excersize_2_2_2
        "Trying to focus on the task at hand, you direct Kagney to the bench as you both start your routines." 
        wt_image kagney_student_weekend_excersize_2_2_2
        "As the day progresses Kagney begins to fidget with her top." 
        wt_image kagney_student_weekend_excersize_2_2_3
        kagney.c "Ugh I hate these things! All they do is get in the way of everything."
        wt_image kagney_student_weekend_excersize_2_2_2
        player.c "Breasts, especially yours, Kagney, should be seen as a blessing."
        wt_image kagney_student_weekend_excersize_2_2_2
        kagney.c "More like a curse… But… Um… You like them right? They’re not too big or?"
        wt_image kagney_student_weekend_excersize_2_2_3
        "Kagney presents her body towards you as you take in how perfect she truly is." 
        wt_image kagney_student_weekend_excersize_2_2_4
        "She seems to notice your hungry eyes as she lifts her legs up into the air." 
        wt_image kagney_student_weekend_excersize_2_2_4
        kagney.c "Can you help me stretch?"
        wt_image kagney_student_weekend_excersize_2_2_5
        "You gulp as Kagney bends over on the bench. Her round ass waves side to side as you become fixed on watching it move." 
        wt_image kagney_student_weekend_excersize_2_2_5
        kagney.c "You know… I don’t like having large breasts but… The way you look at them. I guess maybe it’s… Not all bad."
        wt_image kagney_student_weekend_excersize_2_2_6
        "Kagney pulls up her shirt and exposes her gorgeous breasts."
        wt_image kagney_student_weekend_excersize_2_2_7
        "She removes her shorts and spreads her legs, showcasing her pink pussy." 
        wt_image kagney_student_weekend_excersize_2_3
        "Your cock quivers in your shorts as Kagney smiles at it. You walk over and she eagerly takes it in her mouth. She bobs up and down on your hard cock as she gets it nice and wet for what comes next."
        wt_image kagney_student_weekend_excersize_2_4 
        "Bending Kagney over a work out ball, you spread her pussy open and thrust your cock into her." 
        wt_image kagney_student_weekend_excersize_2_5
        "Kagney soon flips over as you increase your speed. Kagney’s eyes light up in delight as you both agree this workout is much funner."
        wt_image kagney_student_weekend_excersize_2_6 
        "Moving the action to the bench, she spreads herself as much as possible for your member. Her pussy grips your cock all the while dripping on the bench below."
        wt_image kagney_student_weekend_excersize_2_7
        kagney.c "Ah! You’re so big! Ahhhhhh! Yes! Fuck me just like that!"
        wt_image kagney_student_weekend_excersize_2_8
        "Kagney is brought to orgasm but she chases that high as you fuck her on her back once more." 
        wt_image kagney_student_weekend_excersize_2_9
        "The two of you with adrenaline flying high, fuck wildly all over the gym. Her juices get on most of the equipment but neither of you care."
        wt_image kagney_student_weekend_excersize_2_10
        "The action ramps up and Kagney’s body slams down on your cock. Her breasts bounce up and down wildly as she takes your cock deep." 
        wt_image kagney_student_weekend_excersize_2_11
        kagney.c "Yes baby yes! Ah! Your cock is so… Good… Ah… Oh god yes!"
        wt_image kagney_student_weekend_excersize_2_12
        "The minutes pass by as Kagney continues to bounce on top of you. Before long you can sense your balls ready to release." 
        wt_image kagney_student_weekend_excersize_2_13
        "Again Kagney is on her knees ready to receive your seed. She wraps her breasts around your cock as her eyes stare back at you." 
        wt_image kagney_student_weekend_excersize_2_14
        kagney.c "Cum for me baby. Give me that protein shot. Shoot it all over my face."
        wt_image kagney_student_weekend_excersize_2_15
        "She gives your cock a loving kiss and gets her wish as you unload on the blonde bombshell." 
        wt_image kagney_student_weekend_excersize_2_16
        "Kagney is soon covered in your warm seed as her hand remains tight around you." 
        wt_image kagney_student_weekend_excersize_2_17
        "Her body is sweaty and littered with cum but she has a look of satisfaction on her face."
        wt_image kagney_student_weekend_excersize_2_18
        kagney.c "Not the workout I thought we would have… But your cock does motivate me to work on my core haha."
        wt_image kagney_student_weekend_excersize_2_18
        kagney.c "I’ll look forward to the next visit to the gym. Hopefully… We can be alone hehe."
        wt_image kagney_student_weekend_excersize_2_18
        "Tired and sweaty, you soon drop Kagney back home. Your muscles are sore which shows that today’s workout… Went better than you originally thought."
        change player energy by -40
        change kagney desire by 5
        change kagney sos by 10
        notify
    elif kagney.physical_count == 2:
        "Wanting to see if her gym training paid off, you take Kagney to the local tennis courts for a sport she says she does well in." 
        "After jumping in your car you notice that Kagney is all over you. From touching your arm to her repeatedly saying how excited she was for this weekend." 
        wt_image kagney_student_weekend_excersize_3_1
        "Upon arriving at the courts you notice Kagney is staring at you while she twirls her racket around. You smirk wondering if she’s being flirty."
        wt_image kagney_student_weekend_excersize_3_2 
        kagney.c "You know… There’s no one else here… Want to make the game more interesting?"
        wt_image kagney_student_weekend_excersize_3_2
        player.c "Knowing how our weekends have been going of late… I have a guess."
        wt_image kagney_student_weekend_excersize_3_2
        kagney.c "How about, hmmmmm. Every point the loser removes clothing. Deal?"
        wt_image kagney_student_weekend_excersize_3_2
        "You aren’t going to argue with Kagney… But you wonder if winning will really do anything for you. Should you even try to win?"
        $ title  = "Should you even try to win?"
        menu:
            "Try to win":
                wt_image kagney_student_weekend_excersize_3_2
                "You ready yourself and as Kagney serves the first show, you put your all into the swing and score the first point." 
                wt_image kagney_student_weekend_excersize_3_2
                "Kagney looks surprised as she snaps out of her daze. She removes her shirt but that isn’t all she loses."
                wt_image kagney_student_weekend_excersize_3_3
                "Minutes later Kagney slides out of her skirt. Her gorgeous round breasts are exposed to the sunny day. Her panties soon come off and her little pussy is also on full display."
                wt_image kagney_student_weekend_excersize_3_4
                "Swing after swing you completely dominate Kagney. Soon she’s forced to display her body for you."
                wt_image kagney_student_weekend_excersize_3_5
                "The game finally ends with you as the winner… But Kagney looks disappointed. She toys with her racket and congratulates you in a sarcastic tone." 
                wt_image kagney_student_weekend_excersize_3_4
                "Soon she gets dressed and you are back in your car to drop her off. She remains silent the entire ride home. You begin to suspect you ruined some sort of plans for her." 
                wt_image kagney_student_weekend_excersize_3_4
                "Maybe next weekend you allow her to win?"
                change player energy by -35
                change kagney desire by 5
                change kagney sos by -10
                notify
            "Let Kagney win":
                wt_image kagney_student_weekend_excersize_3_2
                "The game goes well at first with you both giving it your all. Soon you land a point as Kagney pouts." 
                wt_image kagney_student_weekend_excersize_3_3
                "She removes her top and exposes her beautiful round breasts. It’s at this point you decide you’ve won a great consolation prize."
                wt_image kagney_student_weekend_excersize_3_3 
                "The rest of the game goes Kagney’s way as you go out of your way to nearly miss everything. The victor is soon announced. Kagney."
                wt_image kagney_student_weekend_excersize_3_3
                kagney.c "Yes! I was nervous playing with my boobs out but the look on your face… Fantastic!"
                wt_image kagney_student_weekend_excersize_3_6
                "Kagney walks up to your ripped body and draws a finger down to your pants." 
                wt_image kagney_student_weekend_excersize_3_6
                kagney.c "Pants off mister. After all I won and we had a deal hehe"
                wt_image kagney_student_weekend_excersize_3_6
                player.c "Sorry. The belt’s a little hard for me. You’re going to need to help me."
                wt_image kagney_student_weekend_excersize_3_7
                "She coyly smiles as she leans in to kiss you. Her tongue playfully licks your lips as her hands work on your buckle." 
                wt_image kagney_student_weekend_excersize_3_8
                "Kagney pulls down your pants and wows to herself. It doesn’t take long to take her trophy for the day, your hard cock." 
                wt_image kagney_student_weekend_excersize_3_9
                "Kagney’s mouth tightens around your cock as her tongue laps away on the tip. Every inch is taken into her hungry mouth with bliss."
                wt_image kagney_student_weekend_excersize_3_9
                "Kissing the tip you note she was planning for this to happen. Just a student and her tutor alone on the court." 
                wt_image kagney_student_weekend_excersize_3_10
                "Taking your cock down her throat you soon carry her off to the side of the court. She moans out a \"Fuck me\" as you slip your cock inside her." 
                wt_image kagney_student_weekend_excersize_3_11
                "Ramming your cock deep into Kagney’s horny pussy, her voice breaks as she backs her large ass against you. Holding her hips you fuck her for all her worth." 
                wt_image kagney_student_weekend_excersize_3_11
                "Spreading her legs wider you glide your hands over her smooth body. Her eyes never leave the sight of the cock defiling her body."
                wt_image kagney_student_weekend_excersize_3_12 
                kagney.c "Yes baby yes! Fuck me like that! Make me cry your name baby. Ah!"
                wt_image kagney_student_weekend_excersize_3_13
                "Her dirty talk combined with her sexy body in your hands is all the motivation you need. Your hard cock quivers in delight inside her completely flooded fuck hole."
                wt_image kagney_student_weekend_excersize_3_14
                "You kiss her lips and down her neck until you see the goosebumps on her body. Her eyes look upon you lovingly but with a deep desire behind them."
                wt_image kagney_student_weekend_excersize_3_15
                kagney.c "I’m going to ride you cock baby. Make me bounce on that hard cock. Fuck me. Fuck me!"
                wt_image kagney_student_weekend_excersize_3_16
                "You watch Kagney’s round ass bounce happily on your meat. Her pussy tightens itself around you and you soon hear those wonderful words."
                wt_image kagney_student_weekend_excersize_3_17
                kagney.c "I’m cuming! Your cock is so good… Fuck! I’m cumming baby! Your cock’s driving me insane!"
                wt_image kagney_student_weekend_excersize_3_17
                "With one hard thrust, Kagney’s body trembles in delight. Her legs wobble as her training allows her to stay up on your cock. She turns back at you and again lights a fire." 
                wt_image kagney_student_weekend_excersize_3_18
                kagney.c "Cum on my face… I want you to cum on my face."
                wt_image kagney_student_weekend_excersize_3_18
                "Kagney’s lips wrap tightly around your cock as her head bobs up and down. You reach your peak and finally give Kagney what she asked for." 
                wt_image kagney_student_weekend_excersize_3_19
                "Streams of cum land all over her face and tongue. She lets out a satisfied moan as cum drips down on her breasts. With one final lick your cock is finished."
                wt_image kagney_student_weekend_excersize_3_20
                kagney.c "Mmmmmmm. Now that… That was a workout… Please tell me we’re doing that next weekend?"
                wt_image kagney_student_weekend_excersize_3_20
                "With a happy smirk, you look down at Kagney as she kisses your cock. Soon you’re both dressed and leave the court behind."
                wt_image kagney_student_weekend_excersize_3_20 
                "Kagney’s Desire is felt the entire drive home. Another weekend may not be such a bad idea…"
                change player energy by -40
                change kagney desire by 10
                change kagney sos by 10
                notify
    $ kagney.physical_count += 1
    if kagney.physical_count > 2:
        $ kagney.physical_count = 0
    call character_location_return(kagney)
    end_day
return

label kagney_weekend_date:
    rem tag 'checking_for_weekend' from kagney
    $ kagney.training_session()
    summon kagney
    $ title = "How would you like to take Kagney out?"
    menu:
        "Go Dancing":
            "Under the guise that it's to further her extracurriculars, Kagney's father accepts and you soon head out to pick up Kagney."
            "After knocking on the door, Kagney opens it as your eyes bulge out at the bombshell in front of you." 
            wt_image kagney_student_date_1_1 
            "Her beautiful make-up, perfectly done hair, and eye-catching blue dress completely overwhelm you."
            wt_image kagney_student_date_1_2
            kagney.c "Hehe... I'm glad you like it... So um I'm ready when you are."
            "You and Kagney head to the club and dance the night away. Many eyes clearly look on in jealousy as you dance and connect with the blinde bombshell." 
            wt_image kagney_student_date_1_2
            "A few hours later Kagney says she's tired as you drive her home. You walk her to her door as she turns around and kisses your cheek."
            wt_image kagney_student_date_1_1
            kagney.c "I had so much fun tonight, I honestly can't wait to tell my friends on monday!"
            "You can tell she's hesitant in heading inside. Do you want to make a move?" 
            $ title = "Do you want to make a move?"
            menu:
                "Yes":
                    if kagney.desire > 25:
                        wt_image kagney_student_date_1_2
                        "You place your hand on her waist as she pulls away... But she begins to look through the door's window. She soon pulls you inside." 
                        wt_image kagney_student_date_1_2
                        "Inside the home is deathly quiet as it appears her father and stepmom are asleep. She escorts you to the living room as she blushes at you."
                        wt_image kagney_student_date_1_3
                        kagney.c "My heart is beating so fast... It might be nerves or... It might be you... Would you... Like to hang out?"
                        wt_image kagney_student_date_1_3
                        player.c "I have a better plan. Turn around and show me that ass under the blue dress. I've been wanting to see it all night."
                        wt_image kagney_student_date_1_4
                        "Kagney giggles as she turns around and slowly hikes her dress. She pulls it up until you see the bare pussy underneath."
                        wt_image kagney_student_date_1_5
                        kagney.c "My friends said I needed to go commando for tonight's date... I'm glad I did hehe."
                        wt_image kagney_student_date_1_5
                        "Kagney bends over and starts showing you her lovely ass. She pulls her dress down to also show her gorgeous round breasts."
                        wt_image kagney_student_date_1_6
                        "She turns over and spreads her legs exposing her little pink pussy to you. Her hand glides down and starts rubbing it." 
                        wt_image kagney_student_date_1_7
                        "Your cock struggles in your pants as she takes notice. She continues to play with her pussy knowing your cock's struggle." 
                        wt_image kagney_student_date_1_9
                        "She gets to her knees and starts moving sensually from side to side. Her smooth skin only proves to make your cock even harder." 
                        wt_image kagney_student_date_1_12
                        "Finally having enough you sit down next to her and start groping her large breasts. She moans out in delight as your rough hands cup each breast." 
                        wt_image kagney_student_date_1_13
                        "Her eyes look down at your touch as a shiver is sent down her spine. The radiant Kagney starts growing hotter as you play with her body." 
                        wt_image kagney_student_date_1_14
                        "You command her to lay back as you start rubbing her little pussy. Her moans audibly escalate in the quiet home but you pay it no mind." 
                        wt_image kagney_student_date_1_15
                        "Before long your wet tongue dances upon her pussy as you lick each and every fold. Kagney's hands move to pinch and play with her breasts."
                        wt_image kagney_student_date_1_16
                        "Things escalate as you pull the honry Kagney to your bulge. She licks and bites it as she slowly pulls out your cock." 
                        wt_image kagney_student_date_1_17
                        "She takes it into her wet mouth and giggles up at you. Her lips tightly cling to your member all the while you stare into her naughty eyes."
                        wt_image kagney_student_date_1_18
                        "Not wanting to blow too early, you pull Kagney up to you and bend her over. Your cock enters her wet hole as she clings close to you." 
                        wt_image kagney_student_date_1_20
                        "You begin fucking her in many positions as the night continues on. Before long she's bouncing happily on your rock hard cock." 
                        wt_image kagney_student_date_1_21
                        "An orgasm rampages through her body as her body slaps hard against yours. Every thrust feels heavenly as her pussy tightens just as well as her lips did."
                        wt_image kagney_student_date_1_22
                        kagney.c "Oh yes... I'm going to cum... Fuck me!"
                        wt_image kagney_student_date_1_22
                        "Your cock sends a wave of pleasure throughout Kagney as she still rides your cock. The little blonde slut is happily rewarding you for the date and you aren't complaining." 
                        wt_image kagney_student_date_1_23
                        "You soon sense you're about to bust as you lay Kagney's soft and gorgeous body down and fuck her as hard as you can. Her eyes flicker happily as you announce your orgasm." 
                        wt_image kagney_student_date_1_24
                        "She begs you to cum on her face as you move up and she cups her lovely tits around your cock. Her tongue happily catches every single drop of cum you release."
                        wt_image kagney_student_date_1_25
                        "You sigh happily as she cleans up your member. You soon hear footsteps upstairs as you scramble to get your clothing on." 
                        wt_image kagney_student_date_1_25
                        "You kiss Kagney good night and sneak out before you're spotted."
                        change player energy by -35
                        change kagney desire by 5
                        change kagney submission by 5
                        change kagney sos by 5
                        change kagney resistance by -5
                        notify
                    else:
                        wt_image kagney_student_date_1_1
                        "You place your hand on her waist but she pulls away. She kisses your cheek goodnight and says she can't wait to see you next week." 
                        wt_image kagney_student_date_1_1
                        "While you were shot down today, that won't always be the case. It's best to try again next weekend." 
                        change player energy by -35
                        change kagney desire by 1
                        notify
                "No":
                    wt_image kagney_student_date_1_1
                    "You kiss Kagney's cheek goodnight and tell her to rest up for next week. A look of disappointment hangs off her face but she heads inside anyways."

        "Cook for her":
            "You invite Kagney to your place under the guise of teaching her to cook. She soon arrives wearing a beautiful dress of which she realizes is a bit too much." 
            wt_image kagney_student_date_2_1 
            "After eating a delicious meal, the two of you retire in the living room. Despite having a full belly... Her eyes seem to hunger for more."
            "Make a move?"

            $ title = "Do you want to make a move?"
            menu:
                "Yes" :
                    if kagney.desire > 25:
                        wt_image kagney_student_date_2_2
                        "You move in to kiss Kagney but she has other plans. Before your lips meet she drops her dress and exposes her round breasts. You smirk as you shift attention to them."
                        wt_image kagney_student_date_2_3
                        "After licking and sucking on her tits, you go further down as she spreads her legs for you. Her eyes flicker with life as she enjoys your tongue on her pussy." 
                        wt_image kagney_student_date_2_4
                        "She glides her hands through your hair and soon she's holding you in place as she cums. You wipe your after dinner snack from your lips and stand Kagney up." 
                        wt_image kagney_student_date_2_5
                        "You pull her dress up to expose her perfect ass as you spank it. She whimpers but doesn't complain. You spank her again before pushing her down on her knees."
                        wt_image kagney_student_date_2_6
                        "She quickly pulls down your pants and finds comfort in seeing your bulge. She licks your underwear before finally pulling those down and sucking on your cock." 
                        wt_image kagney_student_date_2_7
                        "Her lips hold on tightly as her tongue flicks your head. Her tongue wiggles around as her hands move to massage your aching balls." 
                        wt_image kagney_student_date_2_8
                        "Kagney's mouth remains glued to your crotch as her head bobs up and down wildly. You hold off cumming as you decide to make this fun for the both of you." 
                        wt_image kagney_student_date_2_9
                        "Your cock finally enters the tight Kagney as you proceed to show the young school girl your skills. Before long she's yelling your name as your cock fucks her moist pussy."
                        wt_image kagney_student_date_2_10
                        "Before long she's cumming as she spreads herself wide. You spank her ass multiple times until she becomes addicted to feeling. Her ass becomes bright red as she cums a third time to your hard cock."
                        wt_image kagney_student_date_2_11
                        "You decide to make Kagney ride you until she cums again. She happily obliges as the blonde bombshell shakes her hips wildly on your cock." 
                        wt_image kagney_student_date_2_12
                        "Soon her ass is facing you as she rides your cock like a pro. Her body clenches as she has another orgasm that rampages through her horny body." 
                        wt_image kagney_student_date_2_13
                        "You give her no peace of mind as you flip her on her back and start fucking her as deep as you can. Her pussy grows to fall in love with your cock as you completely make the blonde whore yours." 
                        wt_image kagney_student_date_2_14
                        "She leans into your ear and begs for you to cum inside. You smirk as you gladly make her wish come true."
                        wt_image kagney_student_date_2_14
                        "As streams of cum fill Kagney up from deep inside, she shudders in delight. Soon she stares down at the cum leaking out from her pussy and starts licking it up."
                        wt_image kagney_student_date_2_14 
                        "Seems you both got an after dinner snack. Soon Kagney's cleaned up and you send her home. You smile as you notice she's limping a bit. The date looks to have been very successful..."
                        change player energy by -35
                        change kagney desire by 5
                        change kagney sos by 10
                        notify
                    else:
                        wt_image kagney_student_date_2_1
                        "You try to move in to kiss Kagney but she looks down shyly instead. She thanks you for dinner and you decide to see her off for the night. She's still nervous around you but that's easily fixed."
                        change player energy by -35
                        change kagney desire by 1 
                        notify
    call character_location_return(kagney)
    end_day
return
  
# Talk actions  
label kagney_talk:
    if not kagney.has_tag('first_visit'):
        call expandable_menu(kagney_talk_menu)
    else:
        "You can't speak to her right now."
return  

label kagney_talk_her:
    $ kagney.training_session()
    wt_image kagney_student_intro_1_1
    player.c "So Kagney, how about you tell me about yourself?"
    wt_image kagney_student_intro_1_2
    kagney.c "Um... What would you like to know?"
    player.c "Well how is it a beautiful bombshell like yourself isn't like all the other beautiful bombshells"
    wt_image kagney_student_intro_1_3
    kagney.c "Well... I guess daddy always believed I was better than just looks."
    wt_image kagney_student_intro_1_2
    player.c "And do you agree with that outlook?"
    wt_image kagney_student_intro_1_3
    kagney.c "I do. My daddy believed in me so I believe in his goals for me."
    wt_image kagney_student_intro_1_1
    player.c "How do your friends see you? Are you the smart one or the bombshell?"
    kagney.c "My female friends always tell me I'm smart... But my guy friends... I guess all they see is my looks. The speech and debate club look down on me because... I'm smarter than they are... And a woman..."
    wt_image kagney_student_intro_1_2
    player.c "Would you consider yourself popular for your looks or your brain?"
    kagney.c "Um... I guess my brain... Most boys don't talk to me at school. And some of the cheerleaders don't like me because of Chad."
    player.c "We'll come back to Chad later. What do you do on your free time?"
    wt_image kagney_student_intro_1_3
    kagney.c "Well my weekdays are usually spent studying... Daddy says I need to work on my extra curriculars for college. I guess that's usually what I do on the weekends."
    wt_image kagney_student_intro_1_1
    player.c "Such as?"
    wt_image kagney_student_intro_1_3
    kagney.c "Well I like tennis although... My bust... It um... Slows me down. I'm also part of the drama club as well as the acting club. I've always loved acting."
    player.c "Oh really? You know Kagney I think we might be able to explore these extra curriculars further. How about we try one of them this weekend?"
    kagney.c "I... Would honestly love to. Thank you."
    "You make a mental note about her hobbies and start planning for future weekend activities with Kagney."
    wt_image kagney_student_intro_1_2
    player.c "Now Kagney, let me ask you a question that will be just between us. Your father won't hear about it. How sexually active are you?"
    kagney.c "Oh... Um... If you promise not to tell daddy... I um lost my virginity not that long ago to a boy in the speech and debate club... But he... Moved away soon after."
    player.c "Would you say that sex is something you like to do? What would you say if someone used sex as a rewards tool?"
    wt_image kagney_student_intro_1_3
    kagney.c "Well... My friends said sex can sometimes help you focus... As a rewards tool I don't think I would have objections... But only if it worked!"
    "You spend the rest of the day learning more about the young Kagney. She seems to enjoy an older man actually listening and commenting on her life. You can feel her own interest in you growing."
    $ kagney.add_tag('talk_her')
    change player energy by -5
    change kagney desire by 5
    notify
    call character_location_return(kagney)
    end_day 
return

label kagney_talk_chad:
    $ kagney.training_session()
    wt_image kagney_student_intro_1_1
    player.c "So this Chad that has your father worried, why don't you tell me about him."
    wt_image kagney_student_intro_1_3
    kagney.c "Well he's... Cute if that means anything. He's also on the football team and is trying to get a scholarship for college soon."
    wt_image kagney_student_intro_1_2
    player.c "Would you say he's skilled? Do you think he has a chance at going pro?"
    kagney.c "Oh I'm the wrong person to ask... To be honest I don't like football... It's rather violent and the case studies on concussions seems to point in long term brain damage."
    player.c "So how do you feel about your lover Chad risking his brain every game?"
    kagney.c "I'm a little worried but... I won't interfere with his dreams. It's not like we really talk about football though."
    player.c "What do you talk about?"
    wt_image kagney_student_intro_1_3
    kagney.c "Well we're both fans of this tv series right now. We watch it every Sunday and talk about it throughout the week. Other than that I guess we talk about mutual friends and... High school drama."
    wt_image kagney_student_intro_1_2
    player.c "How did you two meet? Did a mutual friend introduce you two?"
    wt_image kagney_student_intro_1_1
    kagney.c "Yeah. I was invited to a pre-game thing and he was there. I barely said anything to him but at the end of the night he asked for my number."
    player.c "Sounds typical for a teenager. Now you had mentioned you had heard rumors about him. What are they?"
    kagney.c "I... don't know why I'm telling you but... Well he's had like 4 girlfriends in the last 9 months. His last relationship ended 2 weeks before we met."
    kagney.c "To be honest... I'm worried my daddy might be right and he's just distracting me... But he's very sweet... I don't know what to believe."
    player.c "Do you see a future with Chad?"
    "Kagney pauses and looks down at your shoes. After a long pause she mutters no." 
    player.c "They why allow him to distract you?"
    wt_image kagney_student_intro_1_2
    kagney.c "I'm... Not sure... My stepmom says that I'm enjoying the attention. I think she's right..."
    "Kagney goes over more things about this Chad. You give her advice on it and she seems to be taking it to heart. Having someone like you around is proving to be beneficial in her eyes. You've bonded well today."
    change kagney desire by 5
    change kagney resistance by -10
    change player energy by -5
    $ kagney.add_tag('talk_chad')
    call character_location_return(kagney)

    notify
    end_day
return

label kagney_talk_father:
    $ kagney.training_session()
    wt_image kagney_student_intro_1_3
    player.c "So Kagney, it seems you very much value your father's hopes of you."
    kagney.c "I do. From a young age he always said I could do anything. Every time I wanted to do something he said \"Do it!\" Even if I quit something... He never really thought I failed."
    player.c "Sounds like he's a very positive influence on you. Do you have a mother?"
    wt_image kagney_student_intro_1_1
    kagney.c "I... No... She... Divorced my daddy and... Ran off to be with another man. It happened when I was young."
    player.c "If I had to guess it would seem your daddy made sure you never left him as well. Like your mother."
    kagney.c "It... Hurt him... But it also made us grow closer. I love my daddy and I honestly wouldn't be where I am without him."
    wt_image kagney_student_intro_1_2
    player.c "You know Kagney, they say the person you most love on a sexual level is your parents. Do you know what the Oedipus Complex is?"
    kagney.c "I do... And I know what you're getting at..."
    player.c "Do you?"
    wt_image kagney_student_intro_1_1
    kagney.c "You think I'm closer to my father because I... Want him sexually..."
    player.c "Parental love takes many forms. He loves you deeply and I think it extends past normal means."
    kagney.c "Can we... Change subjects? This is not... Something I want to speak on..."
    "Despite feeling uncomfortable it would seem that Kagney does love her father more than she lets on. You begin to learn more about where her motivation comes from and make a mental note about her very apparent love of her daddy."
    $ kagney.add_tag('talk_father')
    call character_location_return(kagney)
    change player energy by -5
    change kagney desire by 5
    change kagney submission by 5
    change kagney sos by 10
    notify
    end_day
return

label kagney_talk_you:
    $ kagney.training_session()
    wt_image kagney_student_intro_1_4
    "The question surprises Kagney as her body language becomes flirtacious. She rubs her hands on her knee's and begins to speak."
    wt_image kagney_student_intro_1_3
    kagney.c "You're... Not what I thought about when my daddy sent me here..."
    player.c "That can mean anything Kagney. Tell me what you think honestly."
    wt_image kagney_student_intro_1_4
    kagney.c "Well... You're smarter than you let one. But you also know what to say and when to say it... I guess you're observant?"
    wt_image kagney_student_intro_1_3
    player.c "I can be a lot of things Kagney but that doesn't answer my question."
    wt_image kagney_student_intro_1_4
    "Kagney takes a deep breath and seems to point her cleavage towards you." 
    kagney.c "You're... A great guy... You're cute... You listen to me... You even know how to touch me... As slutty as that sounds."
    wt_image kagney_student_intro_1_5
    player.c "Slut is a term with many uses. When I look at you I don't see a slut. I see a beautiful girl who knows what she wants?"
    wt_image kagney_student_intro_1_3
    kagney.c "And... What do I want?"
    wt_image kagney_student_intro_1_4
    player.c "You already know the answer."
    "Kagney blushes before smiling. She relaxes enough to walk towards you and and sit on your lap. She plants a kiss on your lips before quickly parting." 
    kagney.c "I've... Always liked older men... I just never thought... This would be something that would happen."
    wt_image kagney_student_intro_1_5
    player.c "Life is fickle. Best just roll with it Kagney."
    "She nods silently as you and her begin to make out. You can tell she's still sorting out her feelings but you have at least placed yourself squarly in her life. Time will tell if it continues..." 
    $ kagney.add_tag('talk_you')
    call character_location_return(kagney)
    change player energy by -5
    change kagney desire by 10
    change kagney submission by 10
    notify
    end_day
return

label kagney_talk_anal:
    $ kagney.training_session()
    wt_image kagney_student_intro_1_5
    "Kagney shifts in her seat but you wonder if it’s from nervousness… Or possibly to hide her excitement."
    wt_image kagney_student_intro_1_1
    kagney.c "I… I know what you’re going to ask me… You’re going to ask if I enjoyed um… Having sex through the butt."
    wt_image kagney_student_intro_1_2
    player.c "It’s called anal sex Kagney. There’s no shame in saying you liked it… Albeit the circumstances of why it happened were out of hand."
    wt_image kagney_student_intro_1_1
    kagney.c "*Sigh* I still don’t know why I let you do that to me… I just wanted my character to feel alive… Not become some bimbo who loves butt stuff..."
    wt_image kagney_student_intro_1_4
    player.c "You just said \"Love\". Am I led to believe you enjoyed it?"
    kagney.c "I… I did… Oh god why do I tell you these things!? You’re my tutor! You’re supposed to be teaching me..."
    wt_image kagney_student_intro_1_5
    player.c "Yet isn’t that what I’ve been doing? I’ve taught you to appreciate carnal delights. It just so happens they come in different forms. Anal sex for example."
    wt_image kagney_student_intro_1_3
    kagney.c "I guess… So… What now? Are you going to tell me how good anal sex feels or something?"
    wt_image kagney_student_intro_1_4
    player.c "No. I’m going to show you."
    "Kagney blushes a bright red as a smile appears for a brief moment. Now that the door has been unlocked, it’s time to show Kagney how much pleasure her asshole can bring her."
    $ kagney.add_tag('talk_anal')
    call character_location_return(kagney)
    change player energy by -5
    change kagney desire by 5
    change kagney submission by 10
    change kagney sos by 10
    change kagney resistance by -10
    notify
    end_day
return

label kagney_talk_nothing:
    "You have nothing to talk about"
    $ kagney.add_tag('talk_nothing')    
return

# Other actions
label kagney_seduce:
    $ kagney.training_session()
    if kagney.seduce_count == 0:
        wt_image kagney_student_intro_1_3
        player.c "Kagney you're a very bright young girl but you are also just so beautiful"
        kagney.c "T-Thank you..."
        wt_image kagney_student_intro_1_2
        player.c "Kagney have you ever kissed an older man?"
        wt_image kagney_student_intro_1_3
        kagney.c "N-no... That's something I never really thought about..."
        wt_image kagney_student_intro_1_4
        "You pull Kagney in closer as her eyes match yours. Her lip trembles and she holds her breathe." 
        wt_image kagney_student_intro_kiss
        "You lean in and kiss the beautiful blonde. After a few tender moments, she pulls away with a shaky voice."
        wt_image kagney_student_intro_1_1
        kagney.c "Um, can you help me with this question?"
        "It's going to take more to proceed with Kagney"

        if kagney.desire > 25:
            
            $ title = "Continue further?"
            menu:
                "Yes":
                    wt_image kagney_student_seduce_2_2 
                    "After breaking off the kiss, you lower Kagney's hands down to the bulge in your pants. She eyes the size quietly but you can tell she's on board for more." 
                    player.c "I think we need to have a Biology lesson. Get on your knee's and get a closer look at the subject."
                    wt_image kagney_student_seduce_2_3
                    "Kagney does as you ask and pulls out your cock. She attempts to take it in her mouth but can only take the tip."
                    "The gorgeous blonde looks up at you with hopeful eyes. You cradle her cheek as she smiles and starts to put more effort into sucking your large cock."
                    wt_image kagney_student_seduce_2_4
                    "She loosens her blouse as her breasts start to creep up over her bra. As her mouth lovingly sucks your cock, you decide that it's time to move it somewhere warmer."
                    "You push Kagney over your desk and quickly remove her panties. Her heavy breathing tell you she's nervous about doing this. Should you continue?"
                    change kagney submission by 1
                    change kagney desire by 1
                    if kagney.desire > 30: 
                        wt_image kagney_student_seduce_2_5
                        "Kagney bites her lip and spreads herself for you. Your cock enters her flooded pussy as she moans out loudly." 
                        wt_image kagney_student_seduce_2_6
                        "Her wet pussy tightens itself around your cock as you begin to move your hips and fuck the young student. She pushes herself against your member telling you she's enjoying it as well."
                        wt_image kagney_student_seduce_2_7
                        "Your arm hugs Kagney as she can feel your hot breath on her neck. Her moans become more and more louder as her orgasm is soon approaching."
                        wt_image kagney_student_seduce_2_8
                        "You lay Kagney on the desk as she spreads herself for you. She grabs hold of your arms as if she wants you to be as close as possible to her horny body."
                        wt_image kagney_student_seduce_2_9
                        "As you fuck the tight blonde her breasts jiggle all around. She looks down with wide eyes as if surprised she's able to take your cock."
                        wt_image kagney_student_seduce_2_10
                        "The blonde bombshell begins to cum right as you find the perfect rythm. Her head tilts back as she screams out your name, succumbing to the waves of pleasure filling her body."
                        wt_image kagney_student_seduce_2_11                        
                        "You turn her body and begin to fuck her to the best of your ability. She again looks straight into your eyes as both of you can feelanother orgasm hitting you both."
                        wt_image kagney_student_seduce_2_12
                        "Kagney cums first and moments later you push her to her knee's as her mouth hangs open to accept your hot cum."
                        wt_image kagney_student_seduce_2_13
                        "You shoot your load mostly on to her perfectly round breasts as some enters her mouth. She swallows it without being told as you smile down at the slutty girl."
                        wt_image kagney_student_seduce_2_14                        
                        "You admire how beautiful she is covered in your load for a few minutes as she plays with the cum on her body."
                        "You soon get cleaned up and you see Kagney out. As she walks away she turns back one more time and blushes before finally leaving your sight. You can feel her Desire towards you increasing."
                        
                        $ kagney.seduce_count += 1
                        change kagney submission by 5
                        change kagney desire by 5
                        change kagney resistance by -5
                        change player energy by -15
                        notify
        else:
            "Kagney closes her legs and looks back a you with sad eyes. She isn't ready for the next step and you decide it's best not to push her." 
            "You comfort Kagney and send her home. Being patient with her has allowed her to bond with you a little more..."    
    elif kagney.seduce_count == 1:
        wt_image kagney_student_seduce_1_1
        "Kagney stands in your livingroom in a flirty dress that shows off her body well."
        wt_image kagney_student_seduce_1_3
        "Every time she turns, her skirt shows her red lacy panties underneath." 
        wt_image kagney_student_seduce_1_9
        "You soon cannot hold back as you approach Kagney who's texting on her phone. You take the phone from her and throw it on the couch."
        wt_image kagney_student_seduce_1_10
        "She looks up at you and gulps as you run your powerful hands through her body. They cup her large wonderful breasts as she bites her lip shyly."
        wt_image kagney_student_seduce_1_11
        "You have her turn around as you lift her skirt and take a look at her panties as well as her large white ass. Kagney is silent through all of this."
        wt_image kagney_student_seduce_1_14
        "Wanting her to make the next move, you drop your pants as Kagney reacts to the bulge in your pants. Her mouth opens and she gasps to herself."
        wt_image kagney_student_seduce_1_15
        "She takes a seat as you walk towards her. She looks up at you as if asking for permission and you nod at her. She gulps once more before moving in."
        wt_image kagney_student_seduce_1_16
        "She pulls your boxers and moves her hand inside. She giggles as she starts getting a feel for your erect cock before pulling it out."
        wt_image kagney_student_seduce_1_17
        "Finally she wants to see it. She pulls down your boxers and exposes your hard cock. She opens her mouth in shock but also smiles up at you like a girl who found a piece of candy."
        wt_image kagney_student_seduce_1_18
        "Her mouth quickl moves around your cock as she licks the tip and begins to suck on it slowly. Her mouth tigtens around your member and you moan in approval."
        wt_image kagney_student_seduce_1_19 
        "Kagney pulls down her red blouse and exposes her perfect tits to you. Your hand gropes one for awhile before you pinch her nipple. She winces but doesn't complain further."
        wt_image kagney_student_seduce_1_20
        "Kagney spends a few moments completely sucking on your cock passiontatly. Her tongue glides over the shaft and she moans out every time it goes deeper into her throat."
        wt_image kagney_student_seduce_1_21
        "Pushing your cock into her cheek she continues to lap away at your cock head. Your pre-cum covers her tongue as she goes digging for more. You realize how wet and naughty her mouth truly is."
        wt_image kagney_student_seduce_1_22
        "Wanting to reward the blond cock sucker, you remove her panties and begin licking her tight pink pussy. She cries out in delight as your tongue licks every fold." 
        wt_image kagney_student_seduce_1_23
        "Every time you lick her clit she moans and nods down at you. Kagney's eyes look down at you hungrily as you give her the same gaze in return." 
        wt_image kagney_student_seduce_1_24
        "You quickly get up and bend her over as your cock enters her tight hole. You spank her ass hard as she nods her head back at you. Kagney's submissive side showing off." 
        wt_image kagney_student_seduce_1_25
        "As you continue to fuck the young student, you spread her legs apart and start ramming her at full speed with your hard cock. She responds well as she cries out your name repeatedly."
        wt_image kagney_student_seduce_1_26
        "As your cock is ramming into her tight pussy, she announces she's about to cum. You force the blonde to cum hard all the while she stares longfully at you." 
        wt_image kagney_student_seduce_1_27
        "Before she can even recover from her large orgasm, you move under her and force her to ride you full force. Your dominant voice motivates her to fuck you as best she can." 
        wt_image kagney_student_seduce_1_28
        "As her pussy slams down on your cock, her legs begin to dangle in the air. Her words become slurred as she becomes cock drunk very quickly." 
        wt_image kagney_student_seduce_1_29
        "Anytime Kagney would slow down, you would take control and continue to fuck her with all your strength. Once again she cums as her pussy is glued to your hard cock." 
        wt_image kagney_student_seduce_1_30
        "Not wanting to relent, you pull her legs towards her body and target all the weak points in her pussy. Her moans only serve to tell you it's working." 
        wt_image kagney_student_seduce_1_31
        "On the even of Kagney's 3rd orgasm you again force her to take control as she faces you and rides your cock with haste." 
        wt_image kagney_student_seduce_1_32
        "The sounds of skin slapping together are as loud as ever and only drowned out by Kagney's loud and slurred moaning." 
        wt_image kagney_student_seduce_1_33
        "You pull the tired Kagney towards you as you fuck her pussy to your own completion. Before long you tell the slutty blonde you're going to cum all over her." 
        wt_image kagney_student_seduce_1_34
        "She begs for you to cum as she rushes to her knee's and jerks your cock to completion."
        wt_image kagney_student_seduce_1_35
        "Strands of cum shoot out and land on her gorgeous face as she nods as you with a hungry look." 
        "As the final shot of cum lands on her lip she giggles and takes a deep breath. She licks her lips as you can see her body shiver with delight. She licks again and moans out \"Yummy\"."
        wt_image kagney_student_seduce_1_36
        "The horny blonde spits out a bit of cum on her breasts and starts playing with it. You're amazed at how hard your cock as as you watch this." 
        wt_image kagney_student_seduce_1_8
        "Before long her show ends and she jumps to her feet to clean up. As she cleans up in the bathroom you hear a ring and find her phone you threw earlier." 
        wt_image kagney_student_seduce_1_7
        "On the screen blinks a message \"Sooooooo? Did you fuck your tutor tonight? DEETS GIRL!\" You smile to yourself as you put the phone back." 
        wt_image kagney_student_seduce_1_6
        "Kagney is soon cleaned up and dressed. You see her smiling wide at her phone as she texts a response. You send her home and wonder how her friends are going to gossip about you..."             
        $ kagney.seduce_count += 1
        change kagney submission by 5
        change kagney desire by 5
        change player energy by -15
        notify

    if kagney.seduce_count >= 2:
       $ kagney.seduce_count = 0 
    call character_location_return(kagney)
    end_day
return

label kagney_study:
    $ kagney.training_session()
    wt_image kagney_student_study_1_1
    "Although a new area for you, you decide it's best to do as her father wishes and help Kagney with her grades. She pulls out a pair of glasses that highlight her beautiful face even more." 
    if kagney.study_count == 0:
        wt_image kagney_student_study_1_1
        "You and Kagney do a good job covering her homework and getting a head start on other things for school. She appreciates the effort you're making."
        change player energy by -10
        change kagney desire by 1
        change kagney sos by 5
        notify
    elif kagney.study_count == 1:
        wt_image kagney_student_study_1_4
        "Although Kagney and yourself are able to get through her homework, you find that it takes twice as long as before. Kagney seems flustered."
        wt_image kagney_student_study_1_1
        player.c "You're usually on point Kagney. Why does it seem like your body's here but your mind is elsewhere?"
        wt_image kagney_student_study_1_4
        kagney.c  "It's... It's Chad... I told him about you and he... Got mad... I need to text him once we’re done here."
        wt_image kagney_student_study_1_1 
        player.c "Might be that he considers me a threat and that's why it angered him. What else did you tell him about me?"
        wt_image kagney_student_study_1_1
        kagney.c  "Well... I um... Said you were kind of cute... But I think that's what bothered him the most."
        wt_image kagney_student_study_1_6
        player.c "I find you very attractive as well Kagney. Those glasses have a very sexy allure to them."
        wt_image kagney_student_study_1_1
        "Kagney blushes as you move your hand to cup hers. She gives you a sincere smile as she changes the subject." 
        wt_image kagney_student_study_1_3
        "She eventually finishes her time with you but you can tell she's very grateful for you being so attentive towards her. You then wonder how things will proceed next week... "
        change player energy by -10
        change kagney desire by 3
        change kagney sos by 5
        notify
    elif kagney.study_count == 2:
        wt_image kagney_student_study_1_3
        "As Kagney and you go through her usual course load, you're surprised by a loud agitated groan."
        wt_image kagney_student_study_1_4
        kagney.c "Ugh, stupid network! I can't upload my work and I only have an hour to send it before it's late!"
        wt_image kagney_student_study_1_3
        player.c "Kagney you worry to much. An hour is plenty of time so relax."
        wt_image kagney_student_study_1_7
        "Kagney mutters something as you notice her shirt is open and her bra's in full view. You eye her cleavage and get an idea."
        wt_image kagney_student_study_1_5         
        player.c "You need to wind down Kagney and I have the solution."
        wt_image kagney_student_study_1_8
        "You place a hand on her breast as she looks down and blushes. She says nothing as she allows you to fondle her beautiful breasts."
        wt_image kagney_student_study_1_9
        "As she quirms in her chair, you continue to massage her breasts. Soon her breathing shifts and she leans closer towards you."
        wt_image kagney_student_study_1_10 
        "You ask her to open her shirt fully as she follows your command. Soon her lacy bra is on full display for you."
        wt_image kagney_student_study_1_11
        "Things quickly escalate and before long she's on her knee's sucking your cock. Her tongue darts around as she sucks you excitedly."
        wt_image kagney_student_study_1_12
        "Bobbing her head up and down you let Kagney fill herself with your man meat. YOu begin to wonder if this is a stress reliever for you… Or her..."
        wt_image kagney_student_study_1_13
        "Your student answers that question as she begins to finger herself down below. Both of you revel in the study session all the while bathing in sheer lustful desires."
        wt_image kagney_student_study_1_14
        "Kagney soon gets a taste of your pre-cum and closes her eyes to enjoy it. Her tongue laps away at your tip in order to lure even more out."
        wt_image kagney_student_study_1_15
        "The action moves to your bedroom as her soft lips are still tightly around your cock. She looks up at you with hungry eyes." 
        wt_image kagney_student_study_1_17
        "Moments later, Kagney's clothes are on your floor and she's riding your cock for all it's worth."
        wt_image kagney_student_study_1_18
        "Her moans and body movements show that she needed this. With her assignments now on the back burner, she slams down on your cock happily."
        wt_image kagney_student_study_1_19
        "Reaching out you fondle the breasts that have been the source of your own distractions. Her pointy nipples and perfectly round shape fit snugly in your hands."
        wt_image kagney_student_study_1_20
        "But her breasts aren’t the only thing you’ve been wanting to play with. Turning her around you grope her round ass as she bounces happily on your cock. Her asshole puckers every time she slams down."
        wt_image kagney_student_study_1_21
        "You slap her ass a few times and watch her flesh jiggle. Every slap sends a giggle that escapes her mouth. Her innocent voice only makes you harder as you force her ass down on your cock."
        wt_image kagney_student_study_1_22
        "You decide to take control as she climbs off of you and opens her legs wide. You insert your cock into her tight pussy and continue fucking the bombshell."
        wt_image kagney_student_study_1_23
        "Her eyes are glued to yours as your young student holds herself wide for your cock. Her voice begins to break as you give her a wonderful orgasm."
        wt_image kagney_student_study_1_24
        "After seeing her trembling body enjoy the orgasm you gave her, you ask her to turn around as she offers her fat ass to you."
        wt_image kagney_student_study_1_25        
        "You again continue plowing the young blonde and enjoy her ass shaking at your movements."
        wt_image kagney_student_study_1_26
        "The mezmorising jiggles of her ass soon prove to be too much as you tell her you're about to cum."
        wt_image kagney_student_study_1_27
        "Giving her ass a playful slap once more, she yelps in excitement. She can barely speak as her words slur together. Before long you’re ready to unload upon seeing that beautiful ass jiggle around."
        wt_image kagney_student_study_1_28
        "She climbs off the bed and presents her face towards you. Her hungry eyes continue to stare up at you as cum rains down on her pretty face." 
        wt_image kagney_student_study_1_29
        "Her tongue darts around catching every drop as even more lands on her face. With your balls empty you look down to admire your work."
        wt_image kagney_student_study_1_30
        "She gives you a very cute and happy smile which makes you almost want to fuck her again... But you lose the oppurtunity."
        wt_image kagney_student_study_1_31
        "She quickly gets up and runs into the kitchen. Checking the time it seems the hour is almost up. To your relief she was able to finally submit her work."
        wt_image kagney_student_study_1_31
        "With a happy sigh, she cleans herself up and thanks you for distracting her. She leaves your apartment as you note her gratefullness towards you."
        change player energy by -15
        change kagney desire by 5    
        change kagney sos by -5
        change kagney submission by 5

        notify        
    elif kagney.study_count == 3:
        "You again decide to help Kagney study. Before you begin, she asks if she can change as you point her to the guest room." 
        wt_image kagney_student_study_2_1
        kagney.c "Kagney's Thoughts : My friends didn't believe me when I told them about him... They said I couldn't seduce anyone so I'll show them..."
        wt_image kagney_student_study_2_2
        "Kagney changes into a more revealing wardrobe that highlights her figure."
        wt_image kagney_student_study_2_4        
        "She puts on sexier lingerie that she bought earlier that week."
        wt_image kagney_student_study_2_5
        "She slides up the panties as they perfectly highlight her large butt. She finally pulls the bra out which matches."
        wt_image kagney_student_study_2_6
        "Her bra pushes up her breasts into a perfect cleavage. This will be how she catches his attention."
        wt_image kagney_student_study_2_7
        "With a tight white blouse hugging her breasts and a tighter skirt making her butt look more full, she smiles at her work."
        wt_image kagney_student_study_2_8
        "Fully dolled up she joins you in the kitchen as you gawk at the gorgeous student." 
        wt_image kagney_student_study_2_9
        "Things go as usual as you and Kagney go over her homework. Every so often she would lean in towards you or air out her blouse."
        wt_image kagney_student_study_2_10        
        "As things progress, Kagney begins to get flustered but not at you... At her work."
        wt_image kagney_student_study_2_11
        kagney.c "This doesn't make sense... How is it... No... We didn't even learn about this method!"
        wt_image kagney_student_study_2_12
        "You again try to calm her down as she tilts her glasses down and eyes you."
        wt_image kagney_student_study_2_14
        kagney.c "I need a break... I think we both need a break honestly... Hey can I get your opinion on something?"
        wt_image kagney_student_study_2_15
        "Kagney stands up and shows off her clothing. She turns around making sure you can see every inch of her."
        wt_image kagney_student_study_2_16
        "She rips open her blouse and makes a comment at how cute her bra is. She mentions her panties are even cuter."
        wt_image kagney_student_study_2_17        
        "She slowly strips off her clothing and soon you begin to agree with Kagney. Her lingerie perfectly shows off her body."
        wt_image kagney_student_study_2_18
        "As you shower Kagney in compliments, you can tell she has other skills that will also need to complimented on." 
        wt_image kagney_student_study_2_19
        "Sliding down her panties, she flashes her shaved pussy. She eyes you for a reaction but doesn’t seem content with what she gets. She mutters something and then turns around."
        wt_image kagney_student_study_2_20
        "Sliding her panties further down she flashes her butthole and finally smiles. Licking your lips you hope an oral report is expected today… Lucky for you, it is."
        wt_image kagney_student_study_2_21 
        "She gets on her knees and soon takes your hard cock in your mouth. Her skills have improved but you have no idea who... Or what she's been practicing on."
        wt_image kagney_student_study_2_22
        "Ignoring that you focus back on Kagney as she licks your tip sensually, her eyes again staring back at yours hungrily."
        wt_image kagney_student_study_2_23 
        "Her wet tongue perfectly cleans your cock as she licks every inch.Your groans just further drive you to deepthroat your cock down her tight hole."
        wt_image kagney_student_study_2_25
        "Just like before, she puts focus on drawing out your pre-cum. Her tongue laps away while you can see how desperate she wants what’s hidden inside."
        wt_image kagney_student_study_2_24
        "Finally she plants a loving kiss on the tip before standing up.She removes her panties and drops them in your hand before disappearing into your room. You follow like an obedient puppy."
        wt_image kagney_student_study_2_32
        "On your bed is Kagney calling you over with her finger. Our attention is instantly drawn to her breasts as you give them a quick massage."
        wt_image kagney_student_study_2_26
        "As both of you succumb to your lust, she faces away from you and inserts your hard cock into her drenched pussy."
        wt_image kagney_student_study_2_27 
        "Her ass again mesmorizes you as she bounces happily on your cock. Her moans turn into cries of pleasure as she rides you for dear life."
        wt_image kagney_student_study_2_28
        "You see her asshole pucker as you dream of one day pushing your cock into it. For now her pussy is all you need as you buck your hips into your student." 
        wt_image kagney_student_study_2_29
        "The lust continues to build deep inside you as you flip Kagney over and start fucking her to the best of your abilitiy."
        wt_image kagney_student_study_2_30        
        "Her pussy tightens around your cock as she grabs hold of her ankles and calls out your name. You can tell she's about to cum." 
        wt_image kagney_student_study_2_31
        "Wanting to keep up the momentum, you flip her over one more time and start fucking her doggystyle."
        wt_image kagney_student_study_2_33
        "Her cute toes curl as you hit all of her weak spots in this position. A piercing cry soon announces that she's cumming to your cock."
        wt_image kagney_student_study_2_34 
        "Her body collapses on the bed but you continue to fuck her hard. She submits to your movements as you spank her ass nice and red."
        wt_image kagney_student_study_2_35
        "You force her to take your cock as deep as she can as her cries continue to echo out in the room. The bed violently shakes as you and Kagney fuck like wild animals."
        wt_image kagney_student_study_2_36
        "As Kagney cums to your cock one more time, you sense your own orgasm ready to pain her body white. A few more thrusts is all you can muster but… You enjoy them for every lasting moment."
        wt_image kagney_student_study_2_38
        "You finally pull out and cum all over it. Kagney moans out your name as you paint her lovely ass white."
        wt_image kagney_student_study_2_39
        "Kagney feels every single drop of hot cum sliding down her ass. With a heavy breath she thanks you for making her cum so hard. The comment does wonder for your ego."
        wt_image kagney_student_study_2_40
        "A careful rest later and you realize how late it is. You hand Kagney money for a taxi as she looks offended." 
        wt_image kagney_student_study_2_41
        kagney.c "Can't... Can't I just stay the night... With you?"
        wt_image kagney_student_study_2_42
        player.c "While that thought does sound lovely, I'd rather your father not know about our relationship. At least not yet."
        "Kagney mopes but she takes the money and calls a taxi. A kiss on the cheek goodbye, you watch the blonde bombshell climb into the taxi and leave. "
        "You rub your cheek as you can sense that Kagney's desire for you has increased drastically."
        change player energy by -20
        change kagney sos by 2  
        change kagney desire by 5  
        notify
    elif kagney.study_count == 4:
        "You and Kagney sit down for yet another study session but things quickly grow uncomfortable. Your AC has stopped working and your apartment is now boiling hot." 
        wt_image kagney_student_study_3_1
        "You take the study session outside as your attention is quickly drawn to Kagney's clothing." 
        wt_image kagney_student_study_3_2
        "She borrowed one of your hats and wore a shirt that barely covers her breasts, much less anything else."
        wt_image kagney_student_study_3_3
        "She seems to notice your eyes glued to her, as she begins to find any reason to touch herself." 
        wt_image kagney_student_study_3_4
        "You spend a few minutes staring at Kagney as she teases you over and over again. Your study session is so far... A failure." 
        wt_image kagney_student_study_3_5 
        "Kagney drops her pencil on the floor and announces it. She bends down as you see her blue leggingings perfectly hugging her ass." 
        wt_image kagney_student_study_3_6
        "Your eyes are now glued to her ass as she seats herself on the recliner and presents her ass to you."
        wt_image kagney_student_study_3_7
        "You lick at your lips not knowing how much more teasing you could take."
        wt_image kagney_student_study_3_9        
        "Before long Kagney says she wants to jump in the pool and she pulls up her shirt."
        wt_image kagney_student_study_3_10
        "Her perfectly round breasts are presented as her teasing continues." 
        wt_image kagney_student_study_3_11
        "Dropping her leggings you finally see the thong she's wearing underneath. She pulls up on it as you see it ride up her pussy."
        wt_image kagney_student_study_3_12     
        "Lowering her panties she flashes you her delicious looking pussy. She smiles as if knowing that you’re completely under her lucious spell."        
        wt_image kagney_student_study_3_13
        "Wiggling her perfect ass towards you, you reach out to grab it. She lets out a sultry moan and bends over."
        wt_image kagney_student_study_3_14
        "You pull down her panties and rub her little asshole gently. She lets out another small moan before giving you a better look."
        wt_image kagney_student_study_3_15
        "Spreading her cheeks, you get a better look at her juice pussy and her very tight looking asshole. Before you can dig into both… She pulls away."
        wt_image kagney_student_study_3_16
        "Kagney is very adamant about teasing you and while you would rather play with your student… Curiosity drives you to see how far she’s willing to take it herself."
        wt_image kagney_student_study_3_17
        "Kagney slowly removes her leggings and winks at you seductively. You play with your growing bulge as she bites her lip upon seeing how hard you are." 
        wt_image kagney_student_study_3_18
        "She slowly slides her panties that are visibly stained with her juices. Tossing them over to you, you smell how naughty they are and pocket them for future use."
        wt_image kagney_student_study_3_19
        "Laying down on the recliner, she kicks her legs around as you take in the wonderful curves. Kagney finally waves you closer with a finger. "
        wt_image kagney_student_study_3_20
        "Finally naked, Kagney spreads her pussy wide for you. The teasing is too much as you decide to punish her for ignoring her school work." 
        wt_image kagney_student_study_3_21
        "You begin to kiss and fondle Kagney's body as she lowers your shorts and exposes your hard cock." 
        wt_image kagney_student_study_3_22
        "Her hands grip tightly around your cock as she again giggles. The smug blonde needs to be taught some manners." 
        wt_image kagney_student_study_3_23 
        "You push her down and move your tongue deep into her asshole. She curls her toes and moans out in delight as your tongue wiggles deep inside her asshole."
        wt_image kagney_student_study_3_24
        "You lay down and soon Kagney's bouncing on your face. Your tongue ravages her holes as she tells you how much she loves your tongue." 
        wt_image kagney_student_study_3_25
        "She climbs off and gives you a loving kiss. After making out you move down and give her nipple the same treatment. Sucking tenderly you make sure every inch of Kagney is enjoyed."
        wt_image kagney_student_study_3_26
        "Flipping her over, you lick her pussy with haste. Her fingers glide through your hair as she pushes you towards her shaved box."
        wt_image kagney_student_study_3_27
        "As Kagney begins to cum from you licking her holes, she pushes you down and removes your shorts as your cock springs free. She begins to lustfully tongue the tip." 
        wt_image kagney_student_study_3_28 
        "As her tongue glides down the shaft she jerks you off while never looking away from your eyes. This whore is very much in love with your cock currently." 
        wt_image kagney_student_study_3_29
        kagney.c "Slurp… Mmmmmm. Such a great cock… Mmmmmm. So hard and so big! Fuck… Do you like that? Me sucking on this yummy cock?"
        wt_image kagney_student_study_3_30
        "You simply nod while Kagney worships your hard member. From slapping herself with it to kissing the tip lovingly… Every inch of you is enjoyed by the horny Kagney."
        wt_image kagney_student_study_3_31
        kagney.c "Fuck… I think my tutor needs a reward for helping me study… I see you looking at my titties… How about an even closer look?"
        wt_image kagney_student_study_3_32
        "As the blonde continues to suck on your cock she switches things up by sandwiching her perfectly round breasts around your member."  
        "Her breasts bounce on your cock as she tightens the large mounds of flesh around your erectness." 
        wt_image kagney_student_study_3_33
        "Wanting to enjoy the busty blonde to the best you can, you order her to turn around and finally have her sit on your cock."
        wt_image kagney_student_study_3_34 
        "As it enters her hot and wet pussy, she bites down on her lip while looking back at you."
        wt_image kagney_student_study_3_35
        "The fuck me eyes she gives you just makes you pump her pussy deeper."
        wt_image kagney_student_study_3_36
        "With every thrust, her little butthole puckers as your thoughts begin to wonder if such a small hole could take your large cock? You hope dreams become reality."
        wt_image kagney_student_study_3_37
        "You're called away from your anal dreams by her screaming your name. Her large ass jiggles in place as she slams and impales herself on your cock."
        wt_image kagney_student_study_3_38
        "You throw her to her side and take full control as you ram your cock inside her pussy"
        wt_image kagney_student_study_3_39
        "Wet sounds explode from down below as your hands hold her in place."
        "Before long the bombshell proves too much as you begin to cum all over her perfect ass."
        wt_image kagney_student_study_3_40
        "Streams of white land on her as she lets out a very happy moan." 
        wt_image kagney_student_study_3_41
        "You give her ass a happy slap to which she happily giggles. After cleaning up you decide to send Kagney home. No more studying will be done today."
        wt_image kagney_student_study_3_41
        "Before she leaves she kisses you passionately. Her desires have grown and are very noticeable now." 
        change player energy by -35
        change kagney desire by 5
        change kagney sos by 5
        notify
    else:
        player.c "Kagney's grades won't get any higher. We don't need to have anymore study sessions unless it's just to hang out with Kagney"
        $title = "Would you still like to spend time this week to help Kagney study?" 
        menu: 
            "Yes":
               "PLACEHOLDER Study Past 5"
            "No":
                pass
    $ kagney.study_count += 1
    call character_location_return(kagney)
    end_day
return

label kagney_sex:
    $ kagney.training_session()
    $ title = "What do you want to do?"
    menu kagney_sex_menu:
        "Have Sex":
            if kagney.desire > 35:
                wt_image kagney_student_intro_1_3
                player.c "Tell me Kagney, are you stressed out right now?"
                wt_image kagney_student_intro_1_4
                kagney.c "*Sigh* I think I am… What do you suggest?"
                wt_image kagney_student_intro_1_20
                "You pull Kagney into your bedroom and tell her that you have just the thing to help."
                "While hesitating, you note her body language is becoming overly flirty. A change from her usual reserved state."
                "You tell her to straddle you and suggest she lose the bra for a special massage."
                "A shy giggle leaves her mouth but she soon throws her bra to the side of the bed."
                wt_image kagney_student_intro_1_21
                "You bring your mouth closer and begin licking and sucking her perfect breasts.Kagney’s shyness begins to vanish as you replace stress, with absolute pleasure."
                wt_image kagney_student_intro_1_22
                "After making Kagney moan in delight, you ask if she could help you with your own stress. She smiles and starts to pull down your pants."
                wt_image kagney_student_intro_1_23
                "Her mouth is soon tightly around your cock as the sounds of slurping fill the room. Kagney bobs her head down on your member lovingly."
                wt_image kagney_student_intro_1_24
                "Her tongue licks up the shaft and even proceeds to suck on your balls. Her stress has definitely vanished."
                wt_image kagney_student_intro_1_25
                "Pulling back she eyes your cock with lust in her eyes. Playing with her little nipples you can see sheer devotion on her face. She would worship your cock at this point."
                wt_image kagney_student_intro_1_26
                "Pushing your cock back in her wet mouth she takes it deep. Her hands unbutton her shorts as it seems she wants more of you. You glady pull her up and push her on the bed."
                wt_image kagney_student_intro_1_27
                "Your own mouth is soon lapping away at Kagney’s juices. You bury your head into her pussy and enjoy her sweet and delectable taste. Kagney thanks you for the oral treatment but soon asks for something else…"
                wt_image kagney_student_intro_1_28
                "Your cock is soon slammed deep into Kagney’s hole as she moans out in delight. Her eyes look upon yours as you send her mental notes that she belongs to you right now."
                wt_image kagney_student_intro_1_29
                "Nodding along she moans out your name over and over again. Your hard thrusts soon turn into rhythmic thrusts that drive Kagney wild with lust."
                wt_image kagney_student_intro_1_30
                "Turning her over you busy your cock inside. Her ass bounces with every thrust as she spreads her large ass for you. Kagney is close to cumming so she suggests riding you."
                wt_image kagney_student_intro_1_31
                "The sounds of her ass slapping on your skin are heard throughout your home. Her lustful moans escalate until she finally cums with your hard cock deep inside of her." 
                "She cries out in delight as you hold on for just a little while longer."
                wt_image kagney_student_intro_1_32
                "You soon push her to her knees and unload all over her gorgeous face. Streams of white cover her breasts as she licks your cock clean soon afterwards."
                "The lovely afternoon ends with both of your sweaty bodies sprawled out in your bed. You call her a taxi and she is almost hesitant to leave… It would seem she really enjoyed herself today."
                "You can tell her Desire for you has risen."
                change player energy by -20
                change kagney desire by 5
                change kagney submission by 5
                change kagney sos by 5
                notify
                call character_location_return(kagney)
                end_day
            else:
                "Kagney is not just going to let you hit it and quit it. She’s already timid so forcing yourself on her is just going to make her leave."
                "Let things come naturally and then she might be open to having a fling."
        "Have Anal Sex" if kagney.has_tag('talk_anal'):
            if kagney.desire > 40 and kagney.submission > 40:
                if not kagney.has_item(butt_plug):
                    sys "This activity would go better if you gave Kagney a buttplug."
                    if player.has_item(butt_plug):
                    
                        $ title = " Would you like to give it to her now?"
                        menu:
                            "Yes":
                                give 1 butt_plug from player to kagney notify
                            "No":
                                return
                                
                    else:
                        sys "You have to get a butt plug first."
                        return
                        
                "After your previous talk about anal sex, you tell Kagney that she will need the butt plug you gave her."
                wt_image kagney_student_anal_1_1_1 
                "She appears from the bathroom as you tell her you’re heading outside for a bit. She walks along bow legged the entire short walk outside."
                player.c "Comfortable?"
                kagney.c "No… I… I have a thing up my butt right now and I’d rather not move."
                player.c "Yet despite that, you’re still so sexy Kagney. You have no idea how beautiful you truly are right now."
                "Kagney smiles and blushes as you eye fuck her body. A small groan distracts you as you command Kagney to show you her hidden surprise."
                wt_image kagney_student_anal_1_1
                "It takes a few seconds but she soon gets to her feet and undoes her pants. Pulling them down you see her gorgeous round ass… And the bright blue butt plug coming out from her brown hole."
                wt_image kagney_student_anal_1_1
                "You give it a light slap and soon tell Kagney that the fun will proceed inside now."
                wt_image kagney_student_anal_1_2
                "Kagney crawls on top of a covered seat and presents her beautiful ass to you. Every time she wiggles it around, the butt plug comes in and out."
                wt_image kagney_student_anal_1_3
                "Wanting to make sure Kagney is fully prepared to use her ass in the future, you start to move the small plug in and out. Kagney’s groans transform into beautiful means."
                wt_image kagney_student_anal_1_4
                "Pulling the entire plug out you see her hole close up tightly. Running your finger alongside her pussy you can tell Kagney’s already very turned on by her new toy."
                wt_image kagney_student_anal_1_5
                kagney.c "Is… Is this fine? I… I just can’t believe I’m showing you my butt hole… You really think it’s sexy?"
                wt_image kagney_student_anal_1_6
                "You give her another light spank and kiss her thighs. You ask her to spread her pussy for you and she does so instantly. Pushing the plug in and out you soon cannot contain yourself anymore."
                wt_image kagney_student_anal_1_7
                "You free your cock as Kagney bites her lip. She quickly takes your hard member and shoves it deep into her wet mouth. Her fuck me eyes focus on yours as she finally see’s how sexy you find the blonde bombshell."
                wt_image kagney_student_anal_1_8
                "Cupping your balls in her hand, you fuck her throat for all it’s worth. Saliva litters your shaft and falls down to her exposed legs. Kagney never once peers away from staring at her favorite tutor."
                wt_image kagney_student_anal_1_9
                "The room is soon full of naughty noises full of gagging, slurping, and Kagney’s sultry moans. You pull your cock from her mouth and ask that she bend over. It’s time to return the favor."
                wt_image kagney_student_anal_1_10
                kagney.c "Oh? … Oh! Oh fuck… Ah! Your tongue is inside my butt… Fuck it… It feels so fucking good! Ah! Deeper! Please!"
                wt_image kagney_student_anal_1_11
                "You lap away at her dripping pussy but put most of your focus on lubricating her brown star. Kagney spreads her ass far apart giving you access to all the tasty hole has to offer."
                wt_image kagney_student_anal_1_12
                "Staring down you spread her asshole far apart and tell Kagney you’re going to fuck her ass now. Spitting in her hole and on your cock… You thrust your cock inside Kagney’s ass."
                wt_image kagney_student_anal_1_13
                "Kagney lets out a loud moan as she can feel every inch splitting her lower body in half. Your cock goes deeper and deeper and soon your balls are touching her pussy."
                wt_image kagney_student_anal_1_14
                kagney.c "FUCK! AH fuck! You were right… This does feel good! Ah! FUCK MY ASS! FUCK IT HARD!"
                wt_image kagney_student_anal_1_15
                "Kagney’s fat ass bounces down on your cock as every inch continues to explore her naughty hole. Her moans and quivering body further drive you to pummel her ass into the shape of your cock."
                wt_image kagney_student_anal_1_16
                "Throwing Kagney on her back you make her stare at the cock defiling her asshole. Every thrust is there to communicate the thought this hole belongs to you now. Her moans would have you think she believes it too."
                wt_image kagney_student_anal_1_17
                "Soon Kagney announces she’s cumming. Her body straightens out and her legs shake in place. Her asshole tightly grips your cock as the orgasm ravages her body."
                wt_image kagney_student_anal_1_18
                kagney.c "FUCK! Oh fuck… Ah… Ah… That… Was the best orgasm… I ever had… Please.. Give me a second… I… AH! AH FUCK! YOUR COCK IS TOO BIG!"
                wt_image kagney_student_anal_1_19
                "You give Kagney no break and you continue your assault on her asshole. Minutes pass and Kagney is lustfully bouncing on your cock once more. She kisses your lips happily as another orgasm nears."
                wt_image kagney_student_anal_1_20
                "Kagney had become cock drunk and as the 2nd orgasm made her body weak, you made sure she remembered your cock for a long time."
                wt_image kagney_student_anal_1_21
                "You fucked Kagney hard as her limp body simply took it. Her asshole had become wide and the multiple orgasms had drained her completely. But she still had one task left."
                wt_image kagney_student_anal_1_22
                "The weak Kagney got to her knees as you presented your cock to her eager mouth. Streams of cum landed safely in her mouth and tongue as she gulped it all down hungrily."
                wt_image kagney_student_anal_1_23
                "Both of you breathing hard, you look down at Kagney and tell her what a marvelous job she did today. She simply nods as her mouth is full of your spunk."
                wt_image kagney_student_anal_1_24
                player.c "We’re going to have to do this again Kagney… Or am I mistaken in that regard?"
                kagney.c "No… *Huff* You… *Puff* You can fuck my ass whenever you want… That… Was… Great!"
                "Both of you rested up and soon Kagney left your home again bow legged.  You hope her father doesn’t ask questions especially when you do this… Again."
                change player energy by -35
                change kagney desire by 5
                change kagney submission by 5
                change kagney sos by 10
                notify
                call character_location_return(kagney)
                end_day
            else:
                player.c "This isn’t a good time for this. This will just scare the poor girl. Best try it again when we’re much closer."
return

label kagney_end_session:
    if kagney.status == "on_training":
        $ title = "WARNING: This will end your training session with her."
        menu:
            "Yes, end session":
                $ kagney.training_session()
                "You're unable to find an activity that both you and Ivy are willing to proceed with, so you end today's session here."
                $ player.extra_clients_fee_this_week -= kagney.pay # so you don't get paid for training her this week
                add tag 'failed_regular_training_this_week' to kagney
                call character_location_return(kagney)
                end_day
            "Oops, never mind":
                pass
    elif kagney.has_tag('continuing_actions'):
        $ kagney.training_session()
        "You've spent enough time with Ivy for today. You send her home."
        call character_location_return(kagney)
        wt_image current_location.image
    else:
        # If somehow the character still has this action when the action is no longer relevant, remove this action
        add tag 'shut_off_end_session' to kagney
    end_day
return

# School Stuff
label kagney_school:
    $ kagney.training_session()
    if kagney.school_count == 0:
        wt_image kagney_student_school_blackmail_2_1 
        "Kagney shows off her slutty new school uniform as you look on pleased with it. Her pigtails combined with her really slutty lingerie really show her bimbo look well."
        wt_image kagney_student_school_blackmail_2_2
        "You get her into your car as you go over what her school day will look like. Her first target will be her favorite teacher, Mr. Williams"
        wt_image kagney_student_school_blackmail_2_3
        "Mr. Williams has close ties to her father and it's best he comes around to Kagney first." 
        wt_image kagney_student_school_blackmail_2_5
        "Once Kagney arrives in class she hides her phone and hits record as per your instructions. Class soon begins as Mr. Williams stares at the new Kagney." 
        wt_image kagney_student_school_blackmail_2_9
        "Through the phone you can see Kagney turning towards her friends but not hearing what's being said. Soon all her friends look shocked as you guess that Kagney shared her plan." 
        wt_image kagney_student_school_blackmail_2_10
        "To fully disrupt the class, Kagney removes her tight white blouse and climbs on her desk. She begins to exclaim that Mr. William's has a large cock to the class."
        wt_image kagney_student_school_blackmail_2_11
        "Mr. Williams not being used to the new Kagney, begins to try and clam down the situation but Kagney continues to edge him on." 
        wt_image kagney_student_school_blackmail_2_12
        "Before long Mr. Williams looks completely done as he tells the class to go home. Kagney looks down at her friends and winks." 
        wt_image kagney_student_school_blackmail_2_13
        "Soon everyone but Kagney and Mr. Williams are left along in the class. He looks down at Kagney and asks why she did this." 
        kagney.c "Why? So I can get you along Mr. Williams... I see the way you stare at me at home... I also know what you're packing right here hehe."
        kagney.c "So why don't you let me see it before I tell daddy that you've been jerking off to my dirty laundry"
        wt_image kagney_student_school_blackmail_2_14
        "He looks beaten as Kagney's hand moves to cup his groin. He takes a deep breath and finally allows Kagney to pull his hard cock out of his pants."
        wt_image kagney_student_school_blackmail_2_15
        "Kagney begins to suck his cock very quickly as she turns towards the camera and winks. Her lips are tightly gripped around his cock as she bobs her head rapidly." 
        wt_image kagney_student_school_blackmail_2_17
        "Mr. Williams is quick to fall to her slutty charm as she gets ot her knee's and serves the teaches hard cock." 
        wt_image kagney_student_school_blackmail_2_16
        "Soon he begins to moan and pet the blonde slut's hair. She turns to the camera and giggles as she goes back to worshiping her favorite teacher's cock." 
        wt_image kagney_student_school_blackmail_2_18
        "Wanting to further the fun, she removes her bra and cups her breasts as she tittfucks his cock. As it slides in and out her hungry tongue licks at the pre-cum already leaking out."
        wt_image kagney_student_school_blackmail_2_19
        "She lovingly sucks his cock all the way holding her tits tightly around the teacher's member. With a final kiss on the tip, Kagney gets up and sits at her chair." 
        wt_image kagney_student_school_blackmail_2_20
        "She spreads her legs and calls over the teacher. He bends down and starts licking her juicy pussy. As her juices fall on her chair she looks at the camera and blushes. The show continues." 
        wt_image kagney_student_school_blackmail_2_21
        "Kagney walks Mr. Williams to his desk and bends down as she waves her ass at him. He gets the message and soon his cock is sliding in and out of kagney's tight pussy."
        wt_image kagney_student_school_blackmail_2_22
        "Her pigtails bounce around just like her breasts as she moans out the teacher's name to further his motivation. Before long he's fucking Kagney hard and fast!"
        wt_image kagney_student_school_blackmail_2_23
        "Through multiple positions she accepts the teacher's cock in any way he see's fit. First she's on her back with his hands tightly around her waste." 
        wt_image kagney_student_school_blackmail_2_24
        "He soon picks her up and fucks her standing up. She continues to moan out his name and talk dirty towards him." 
        wt_image kagney_student_school_blackmail_2_25
        "No matter what the teacher wants, Kagney delivers as her pussy wraps tightly around his hard cock. You continue to watch as Kagney's inner slut fully comes out." 
        wt_image kagney_student_school_blackmail_2_26
        "You continue to watch as Kagney's inner slut fully comes out. Her gorgeous body is something you will have to use very soon."
        wt_image kagney_student_school_blackmail_2_27
        "Soon Kagney is bouncing on his cock as her skirt flutters from her movements. Her breasts bounce along as she bites her finger and winks at the camera." 
        wt_image kagney_student_school_blackmail_2_28
        "She continues to dirty talk her teacher saying how she's such a slutty student and need's detention. After a long while he begins to agree with her." 
        wt_image kagney_student_school_blackmail_2_29
        "During the last few moments, his hands push Kagney down on his cock as her face contorts in pleasure. She begins to cum on his cock as he himself soon follows." 
        wt_image kagney_student_school_blackmail_2_30
        "Both climb off the desk as Kagney's face is soon painted white with cum. She accepts his load like a submissive whore and he is happy to do so."
        wt_image kagney_student_school_blackmail_2_30
        "As the last shot hits her face, Kagney's mouth quickly wraps around his cock as she sucks whatever cum remains inside." 
        wt_image kagney_student_school_blackmail_2_31 
        "The teacher's legs begin to shake as she giggles and looks at the camera before mouthing \"You're next\"."
        "With the deed done, Kagney walks over to her phone and takes selfie as she sends it to you. Mr. Williams finds out about her phone as she begins to say her demands." 
        wt_image kagney_student_school_blackmail_2_7
        "As the school day ended and Kagney climbed into your car, she explained the plan went off well. She'll get a letter of recommendation from him and in return, her daddy won't find out he fucked his daughter." 
        wt_image kagney_student_school_blackmail_2_6 
        "You stare at the sexy and slutty selfie she took before she guides your attention back to the real her. Her mouth is soon wrapped around your hard cock as you drive her home. So far..."
        wt_image kagney_student_school_blackmail_2_8
        "You're pleased with the results of her schooling."
        change player energy by -5
        change kagney desire by 5
        change kagney sos by -10
        notify

    elif kagney.school_count == 1:
        wt_image kagney_student_school_blackmail_3_1
        "You pull up to pick up Kagney in her usual slutty clothing and you and her go over the next person she will seduce." 
        wt_image kagney_student_school_blackmail_3_2
        "The plan they both assign is to get Tommy, who is the class president to fall for her charm and also write her a letter of recommendation." 
        "His family is very well off and just his last name will open many doors for him... And soon Kagney as well." 
        "Kagney hops out of your car and you find a quiet place to park while she does what she's told. She ducks into an empty classroom and pulls out her phone." 
        wt_image kagney_student_school_blackmail_3_4
        kagney.c "Hey there Tommy hehe. Come find me in classroom 4C and I'll show you something you'll NEVER forget."
        "Kagney stares down at her phone as she starts taking sexy selfies of herself. She climbs on the desk and uses her alluring voice to further entice Tommy." 
        "Before long she strips down and shows off her naughty lingerie but it doesn't end there." 
        wt_image kagney_student_school_blackmail_3_6
        "Piece by piece she takes pictures from her bare breasts exposed to her again calling out Tommy's name." 
        wt_image kagney_student_school_blackmail_3_7
        "She sends numerous pictures of her shaved pussy to Tommy as he begins to react to her nude body." 
        wt_image kagney_student_school_blackmail_3_8
        "Picture by picture he at first thought it was a prank... But his curiosity builds and builds." 
        wt_image kagney_student_school_blackmail_3_9
        "Finally she spreads her ass for him and winks telling him to hurry... Before long he arrives winded." 
        wt_image kagney_student_school_blackmail_3_6
        tommy_kagney "Huff... Kagney... What's... Why are you sending me these? Why are you naked!?"
        wt_image kagney_student_school_blackmail_3_9
        "Kagney says nothing as she spreads her ass for him. His bulge grows in his pants as she climbs off the desk and struts towards the young man." 
        wt_image kagney_student_school_blackmail_3_10
        "She gets to her knees, free's his cock, and gets to work sucking him off right in the middle of class." 
        wt_image kagney_student_school_blackmail_3_11
        "Her eyes stare deeply into Tommy's as he nervously checks the windows and doors. Kagney nibbles his cock to make sure his focus is on her." 
        wt_image kagney_student_school_blackmail_3_12
        "Her tight mouth works extra hard to get Tommy right where she needs him. With a loud pop she drags him towards the desk." 
        wt_image kagney_student_school_blackmail_3_13
        "Not wanting to pass on her offer he instantly inserts his cock into her tight pussy. Kagney pulls him in closer and begins moaning out his name."
        wt_image kagney_student_school_blackmail_3_14
        "As he fucks her on the desk he becomes memorized by her slutty body. Kagney begins to enjoy the movements of the young man as she cums soon after." 
        wt_image kagney_student_school_blackmail_3_15
        "Getting up against the desk, he allows the young man to fondle her while moving his hips as best he could. She bites her lip at the camera and mutters out \"Professor\" towards you."
        wt_image kagney_student_school_blackmail_3_16
        "Coming off the euphoria Kagney climbs on top of him and rides Tommy's Cock. Her large ass slaps against his skin as her large breasts bounce about freely." 
        wt_image kagney_student_school_blackmail_3_17
        "She looks back and starts laying on the dirty talk she's used before on her teacher. Tommy stands no chance against the horny Kagney..."
        wt_image kagney_student_school_blackmail_3_18
        "It takes every ounce of his being to not fill up the blonde's pussy with cum. But he will not last much longer..."
        wt_image kagney_student_school_blackmail_3_19
        "She looks back at Tommy and begs for his cum. Her purring voice is what drives the young man to the edge as he pushes Kagney off the desk." 
        wt_image kagney_student_school_blackmail_3_20
        "Back on her knees she opens her mouth and accepts his seed. His hot cum lands on her lips and tongue as she swallows every drop she can." 
        "He musters more from his balls as they land on her beautiful round breasts. She presents her semen covered body to him as if showing him his gift." 
        wt_image kagney_student_school_blackmail_3_21
        "But that's when she turns to the camera as Tommy's heart drops. She explains what her demands are before she leaks the sex tape to the rest of school." 
        wt_image kagney_student_school_blackmail_3_21
        "Tommy on the verge of crying... Accepts as Kagney claps her hands happily and hugs the demorilized young man. He leaves the classroom with this head bowed down..." 
        wt_image kagney_student_school_blackmail_3_6
        "Near the end of school, Kagney again climbs into your car and shows you the footage. You hand grips her thigh as she does the same for you." 
        wt_image kagney_student_school_blackmail_3_6
        "You drive your school slut home as you both plan the next person's downfall..."
        change player energy by -5
        change kagney desire by 5
        change kagney submission by 10
        change kagney sos by -10
        notify

    elif kagney.school_count == 2:
        wt_image kagney_student_school_blackmail_2_1
        "Kagney again climbs into your car as you drive her back to school. There's only one person left to make sure Kagney's future is set in stone." 
        wt_image kagney_student_school_blackmail_2_2
        "The school's administrator has access to all the files on students... If she blackmails him, she'll be able to change her overall standing paper wise." 
        wt_image kagney_student_school_blackmail_2_3
        "You again see Kagney to school as she skips up the stairs of school and heads to the admins office." 
        wt_image kagney_student_school_blackmail_1_1
        "Once inside she finds her target as she fixes up her dress and waits until he's looking away. The time comes as he answers the phone."
        "He greets the Principal on the other end and smiles to herself as she enters his office." 
        "Once inside she grabs his phone while he's distracted and starts taking selfies of herself. Before long she's filled his camera roll with her sexy body." 
        "As he turns away to hang up the phone, he see's this and tries to take his phone back. Kagney shoves him back in the chair and giggles." 
        wt_image kagney_student_school_blackmail_1_2
        kagney.c "How are you going to explain why my sexy body is on your phone? An admin fucking a student? Sounds very news worthy right?"
        "The man gulps as she tells him what she wants. It takes quite a while until he loses the battle and starts correcting her school file." 
        "Kagney in the meanwhile needs leverage that he keeps his promise. Propping her phone like before, she soon gets to her knee's and crawls over to the admin." 
        "She paws at his groin all the while he looks down in disbelief. Before long she's gotten his cock free." 
        "She points to her phone that's recording as his heart drops. Another man falls to her ways..." 
        "While Kagney could stop now... His hard cock in her hands makes her pussy quiver in delight. She licks her lips and leans into the man's ear." 
        kagney.c "That doesn't mean we can't still have fun hehe... Now fuck me!"
        wt_image kagney_student_school_blackmail_1_3
        "She quickly wraps her mouth around his cock and begins to suck away. Her head bobs up and down as she fills her mouth with his meat." 
        wt_image kagney_student_school_blackmail_1_4 
        "Minutes later she pulls him by the tied into her spread legs as his cock enters her naughty hole."
        wt_image kagney_student_school_blackmail_1_5
        "She completely guides this man into fucking her senseless. Her body completely falls to her lust as she commands the man to fuck her harder." 
        wt_image kagney_student_school_blackmail_1_6
        "The small office is soon filled with the noices of sex. Kagney rides the man in his chair as she slams her body down on his erect cock." 
        wt_image kagney_student_school_blackmail_1_7 
        "She guides his hands to her hips and continues to command him. Despite his restraint earlier, he has fallen to her slutty body like all the others." 
        "Kagney stares at her phone and moans as if telling you that she's enjoying this. Her eyes return a lustful stare as her eyes begin to flicker." 
        wt_image kagney_student_school_blackmail_1_8
        "As she continues to ride the man's hard cock, she herself begins to cum. Her body hot and bothered makes the man fuck her to his own completion." 
        "The chair they're on bends all the way back and you can feel that it could break any moment now. But both of them continue to fuck like animals." 
        wt_image kagney_student_school_blackmail_1_9
        "The action moves to the desk as she bends over and spreads herself wide."
        wt_image kagney_student_school_blackmail_1_10
        "He enters her pussy again and rams his cock as deep into her slutty pussy as he can." 
        wt_image kagney_student_school_blackmail_1_11 
        "Every thurst makes her body jiggle and she enjoys it fully."
        wt_image kagney_student_school_blackmail_1_12
        "Her moans and cries of enjoyment ring out all around them as the desk shakes underneath." 
        wt_image kagney_student_school_blackmail_1_13
        "With one final thrust she can feels his cock about to cum."
        wt_image kagney_student_school_blackmail_1_4
        "She begs him to cum on her face as she enjoys the fucking for a few more moments." 
        wt_image kagney_student_school_blackmail_1_15
        "He reaches his limit and soon his cum lands all over Kagney's beautiful face. Kagney stares at the camera and winks as she cleans his cock completely." 
        "The footage finally ends and as you watch the black screen in the car, Kagney sucks your cock with no regard to her shame." 
        "You drive her home and give her a good fucking as now... Her future is secured... She might even have a future as a whore if she wishes it. For now her future is secured... All thanks to you..."
        change player energy by -5
        change kagney desire by 5
        change kagney sos by -10
        notify
        call kagney_school_fallout_event
    $ kagney.school_count += 1
    call character_location_return(kagney)
    end_day  
return

label kagney_school_fallout_event:
    "You open up an email from a man who says is Kagney's Father." 
    father_kagney "Hi... I do not know if you remember me but... I'm the man who hired you to watch over my Daughter."
    father_kagney "As it stands... I've gone from being worried to down right panicking about my Daughter!"
    father_kagney "I don't know what you've been teaching her but her clothing... Her speech... EVERYTHING'S changed! That's not my daughter anymore!"
    father_kagney "This... All of this came as soon as you came into the picture... Lawyer up asshole for I am coming for you!"
    father_kagney "You... You did this to my baby girl... And god be damned I'll make sure you pay!"
    
    "You close the email and begin to think about what's to happen. You could reach out to someone for help... But there might be an easier way." 
    "You send Kagney a quick text and ask her to come over. She responds instantly and arrives not that long later." 
    "You show your little school slut the email as she doesn't even blink. She looks at you blankly as if wondering how she should feel right now." 
    "You have two options ahead of you. Both will lesson the burdon off your shoulders."

    $title = "How should you proceed?"
    menu:
        "Have Kagney Seduce her Father" if player.has_item(love_potion):
            wt_image kagney_student_intro_1_19
            player.c "It would seem your father isn't happy with me but I think his dear daughter can fix it."
            wt_image kagney_student_intro_1_14
            kagney.c "You want me to fix daddy? How?"
            player.c "Take this potion Kagney and give it to your dad. Once he drinks it I want you to seduce him. It's time for some father daughter bonding."
            wt_image kagney_student_intro_1_15
            kagney.c "You... Want me to fuck daddy? But... I can't..."
            wt_image kagney_student_intro_1_19
            "You can feel her mind resist your commands as her Hypnosis seems to be coming apart."
            $title = "How should you proceed?"
            menu:
                "Use her Trigger" if kagney.has_tag('talk_father') and kagney.has_tag('trigger_implanted'):
                    wt_image kagney_student_intro_1_16
                    player.c "Bimbos don't need books. Kagney you and I talked about your father. Deep down inside you love your father not as a family figure... But as a man."
                    wt_image kagney_student_intro_1_18
                    kagney.c "Deep down inside... I see my daddy as a man..."
                    wt_image kagney_student_intro_1_19
                    player.c "You know about the Oedipal Complex. There's no man who you love more on a sexual level than your father."
                    kagney.c "There's no man... I love more on a sexual level than my... Daddy..."
                    wt_image kagney_student_intro_1_6
                    player.c "Bimbos don't need books. Kagney you're going to give this potion to your father... And you're going to seduce him." 
                    wt_image kagney_student_intro_1_18
                    kagney.c "I'm going to give... Daddy that potion... Then seduce him."
                    wt_image kagney_student_intro_1_19
                    player.c "Bimbos don't need books. Break through your barriers Kagney... Break them and accept your father as man."
                    "Kagney stares blankly as you reinforce her to go through with the plan. After breaking the hypnosis you send Kagney on her way and wait to hear what happens."
                    $ kagney.fallout_path = "father"
                    
                "Do Nothing":    
                    player.c "I need to think this over more... I'll need a Love Potion but I'll also need deeper insight on how she views her father. I should talk with her to learn more."
        "Set up Chad to take the fall":
            wt_image kagney_student_intro_1_19
            player.c "Seems your father is upset at the life you chose but the answer may be obvious to fix it. Tell me Kagney, how’s Chad doing?"
            kagney.c "Chad is fine… I haven’t had time for him lately but he keeps messaging me."
            player.c "Kagney you like being my slave correct? Being my little slutty schoolgirl?"
            wt_image kagney_student_intro_1_16
            kagney.c "Of course! I love spending time with you. I… I would do anything for you."
            player.c "Excellent. Then my dear first I need you to message Chad and spend some alone time with him. Can you do that?"
            kagney.c "I can Professor. There’s a school dance coming up. Should I tell him I’m interested?"
            wt_image kagney_student_intro_1_16
            player.c "Even better. Now Kagney I need you to follow my instructions perfectly okay? You do this right and we can rid ourselves of this obstacle."
            "You detail what Kagney needs to do as she nods her head to your every word. You see her out and type out an email that’s sent towards Kagney’s Father." 
            "Nothing to do now but wait..."
            $ kagney.fallout_path = "chad"
    $ kagney.add_tag('school_fallout')   
    $ kagney.event_week = week + 1;
    call character_location_return(kagney)    
    end_day            
return

label kagney_school_fallout_followup:
    if kagney.fallout_path == "father":
        "You are woken up by an email notification. Clicking it you find that it’s from Kagney’s Father…"
        father_kagney "Sir... I... I'm deeply sorry for threatening you like how I did... That was very unbecoming of me and I will apologize."
        father_kagney "My daughter and I had... A heart to heart and I couldn't blame you for her own choices... As a father I reacted harshly."
        father_kagney "As it stands I... I'm proud of her and I think our relationship will evolve from here. You're free to continue to tutor her. Again I'm deeply sorry for my previous Email"

        "The email ends with another apology. You pick up your phone and call Kagney. Soon after she arrives at your apartment and gives you a very tight hug." 
        "You ask her how things went with her dad as she goes through everything that occurred." 
        wt_image kagney_student_daddy_1
        "The day you sent her to do the deed, her stepmom was manic on the phone when she arrived." 
        wt_image kagney_student_daddy_2
        stepmom_kagney "No I have no idea... Wait... Oh thank the heavens she just walked in... Yes please come home baby... See you soon. KAGNEY!"
        wt_image kagney_student_daddy_3
        "Kagney turns from the stairs and looks at her upset stepmom."
        wt_image kagney_student_daddy_2
        stepmom_kagney "Where the hell have you been!? Your father is out right now driving like a man mad trying to find you! Tell me you didn't go to that man's house!?"
        wt_image kagney_student_daddy_3
        kagney.c "Calm down.. Geez... No I went out with my friends but I came back when I could... Plus (WifeTrainer) isn't as bad you as two say he is... I'm going to my room..."
        wt_image kagney_student_daddy_5
        "Her stepmom yelled after her but Kagney ignored her. kagney in the mean time got to work."
        wt_image kagney_student_daddy_7
        "She pulled out the Love Potion but also changed into her sexy lingerie." 
        wt_image kagney_student_daddy_4
        "Downstairs her father had arrived as he and her stepmom discussed the WifeTrainer."
        wt_image kagney_student_daddy_8
        "She poured the Love Potion into a glass of wine and grabbed an ice cream for herself." 
        wt_image kagney_student_daddy_9
        "She bounced over to her father and gave him the glass as she sucked on her ice cream. She saw him take a sip of the wine and as it began to have it's effects, Kagney whispered to her father." 
        wt_image kagney_student_daddy_10
        kagney.c "Daddy... I love you and you love me. Fuck what my stepmom thinks... Follow me upstairs so you can show me how much you love me."
        wt_image kagney_student_daddy_8
        "With a kiss on the cheek goodbye, Kagney bounces up to her room. Kagney's father shakes off the effects of the potion as he suddenly feels overwhelemed with desires." 
        wt_image kagney_student_daddy_11
        stepmom_kagney "Hey honey... I thought we were going to have dinner, where are you going?"
        wt_image kagney_student_daddy_12
        "He ignores her and quickly heads upstairs. The stepmom shakes her head looking very much frustrated with everyone today."
        wt_image kagney_student_daddy_13
        "Upstairs, the door opens as Kagney's father enters her room. He looks down at the sensually dressed daughter as she smiles at him." 
        wt_image kagney_student_daddy_14
        "Overwhelemed with the effects of the Love Potion, he pulls his daughter up and gives her a very tender but passionate kiss." 
        wt_image kagney_student_daddy_15
        kagney.c "Oh Daddy... You love me right? More than a daughter... You love me as a woman... I'm your woman daddy."
        wt_image kagney_student_daddy_16
        "Kagney begins to unclip her bra as her father begins to touch her smooth body." 
        wt_image kagney_student_daddy_17
        "Blinded by his absolute lust, he licks her breasts before she can even remove her bra. She cradles his head and finally removes her bra." 
        wt_image kagney_student_daddy_18
        "He moves in and begins to kiss and suckle on her nipples to her joy. She moans out for him as she enjoys her daddy's tongue." 
        "Both of them lick her nipples as his hand moves down to finger her already soaked pussy." 
        wt_image kagney_student_daddy_19 
        kagney.c "Daddy it's my turn. I want to see your cock. Come here daddy."
        wt_image kagney_student_daddy_20
        "She pulls his cock free and moves in to take it in her mouth. He pets her hair as she tries to deepthroat his cock as best she can." 
        wt_image kagney_student_daddy_21
        "As her head bobs up and down, he starts to thrust deeper into her mouth. His mind is completely overwhelemed by desire for his daughter."
        wt_image kagney_student_daddy_22
        "He demands she titfuck him as she moans out \"Yes Daddy\"."
        wt_image kagney_student_daddy_23
        "She wraps her gorgeous mounds around his cock and goes to work to tittyfuck her father." 
        wt_image kagney_student_daddy_24
        "Her tongue dances all over the tip as pre-cum fills her mouth. Every ounce of her body is filled with the desire to fuck her father." 
        wt_image kagney_student_daddy_25
        "Climbing on top of him, she continues to suck his cock with haste as he himself gets his first taste of his little girl." 
        wt_image kagney_student_daddy_26
        "His tongue laps away at her leaking juices as she sucks his cock clean. Soon things escalate..."
        wt_image kagney_student_daddy_27
        kagney.c "Daddy your cock is so yummy. But I want more… I want to fuck you daddy! Now much me… Fuck your little girl hard!"
        wt_image kagney_student_daddy_28
        "Kagney climbs up top and inserts her father's hard cock into her tight snatch. His cock fills her compeltely as she purrs out her delight."
        wt_image kagney_student_daddy_29
        kagney.c  "Your cock is perfect daddy! Mmmmmm Fuck me! Fuck me daddy!"    
        wt_image kagney_student_daddy_30
        "Doing as his little asks he shoves his cock deep into her hole as she bounces down upon his member."
        wt_image kagney_student_daddy_31
        "Both father and daughter moan out together in unison as their bodies enjoy the taboo sex they're having."
        wt_image kagney_student_daddy_32
        "Kagney rides her daddy's cock hard and soon she cums loudly. Her pussy tightened itself over his cock as her body was ravaged by an orgasm."
        "wanting to take his daughter in his arms, he started fucking her on her side. She continued to call out his name as she submitted to her father's naughty wishes." 
        wt_image kagney_student_daddy_33
        "She licked her own nipple and even kissed his lips like a sex starved animal. Kagney did not care as she continued to get fucked by her father's cock." 
        wt_image kagney_student_daddy_34
        "The fun would continue to evolve as he bent her over and fucked her senseless." 
        wt_image kagney_student_daddy_35
        "Every thrusty made her ass jiggle around as he added to it by spanking her." 
        wt_image kagney_student_daddy_36
        "Every inch of his daughter's body was sheer perfection and he made sure to let her know." 
        wt_image kagney_student_daddy_37
        "He didn't want this to end as he fought every urge to cum. All he wanted was to continue fucking his little girl." 
        wt_image kagney_student_daddy_38 
        kagney.c "YES! Daddy, your cock feels so wonderful in my little pussy. Whenever you want to fuck, I’ll do it! You’re the best Daddy in the entire world! AHHHHHH!"
        wt_image kagney_student_daddy_39
        "Kagney eyed her father and saw how much he enjoyed fucking her tight little pussy. Licking her lips she wanted nothing more for this moment to last."
        wt_image kagney_student_daddy_40
        "The father daughter bonding event continued as Kagney yelled for her daddy to fill her pussy with more cock. He couldn’t keep up with his little girl’s needs…"
        wt_image kagney_student_daddy_41
        "He made her turn on her back and she looked up at him with loving eyes. Her breasts continue to bounce from every thrust."
        wt_image kagney_student_daddy_42
        kagney.c  "Daddy Yes! Oh daddy your cock is filling me up so good! Mmmmmmm. Daddy!"
        wt_image kagney_student_daddy_43
        kagney.c  "Cum for me daddy... Give me your yummy cum... Cum for your little girl."
        wt_image kagney_student_daddy_44
        "With that final word he pushed her down and jerked himself over her innocent looking face."
        wt_image kagney_student_daddy_45
        "He covered Kagney's face with the same seed that birthed her but he did not care."
        wt_image kagney_student_daddy_46
        "She ate every single drop but allowed the cum to land on her breasts. Every drop sent a shiver down her spine."
        wt_image kagney_student_daddy_47
        "After emptying his balls, she licked and sucked his cock clean. With a loud pop she smiled at her tired father."
        wt_image kagney_student_daddy_48
        "She looked over near her nightstand and smiled as she looked on at the camera she placed there."
        wt_image kagney_student_daddy_47
        "Playing with the cum she smiled knowing she could get her bonding time with her father on tape. Back in his apartment, he stares down at Kagney's phone."
        wt_image kagney_student_intro_1_19
        kagney.c "We've been fucking all weekend... My daddy has such a great cock but… Yours is still my favorite hehe."
        "This isn't the last you'll hear about this but as it stands... You got her father off your back. For now that's the best news you could get..."
        change player energy by -5
        change kagney desire by 5
        change kagney submission by -20
        change kagney sos by -20
        notify
    elif kagney.fallout_path == "chad":
        father_kagney  "I hope this message finds you well… You were right… It was that boy this entire time..."
        father_kagney  "I lashed out towards you and I’m deeply sorry I did that. Please forgive me..."
        father_kagney  "In the end you were just looking out for her just as I was… That boy is no longer allowed anywhere near Kagney"
        father_kagney  "I also saw the messages you sent trying to plead with her… Words can not express how much of a caring instructor you are. Thank you."
        "The email goes on and on as you lose interest. You close it out and call Kagney. She arrives fairly quickly at your doorstep." 
        wt_image kagney_student_intro_1_3
        kagney.c "I did it! Everything went well and my father said I could still see you. Not like I needed his permission hehe."
        "You sit Kagney down as you command her to regale her last week with Chad. Kagney happily pulls out her phone as she sits in your lap."
        "The following day after giving your orders, Kagney sent Chad a message and they grabbed lunch. It was there that she stole his phone but also invited him to the dance."
        "Throughout the week she sent herself various threats from Chad’s phone as if he was ordering her to be the school slut. All the while you were sending your own encouraging ones."
        wt_image kagney_student_chad_1_1
        "On the day of the dance, Kagney and Chad were the center of attention. Kagney wore a very slutty looking uniform that barely covered anything which made the spotlight even brighter."
        "As the night went on, Kagney teased the poor Chad until he could not take it much longer. They snuck away from the dance and found themselves in the drama classroom… Where Kagney planted Chad’s phone..."
        chad_kagney "Goddamn you’re so fucking hot. I want to fuck you Kagney. These titties have been making me so hard all night."
        wt_image kagney_student_chad_1_2
        "Chad pulls Kagney in for a kiss as he raised her top to expose her beautiful round breasts. They made out tenderly as he felt her up."
        wt_image kagney_student_chad_1_3
        chad_kagney "Get your ass on the couch. I hope your pussy nice and wet… Oh and you better have shaved for me!"
        wt_image kagney_student_chad_1_4
        "He spread her legs and dug in for his meal. His tongue lapped away at her dripping pussy all the while her moans filled the room."
        wt_image kagney_student_chad_1_5
        "Kagney raised her legs high into the air and let Chad drink up all her naughty juices. He would soon grow tired as he got up and pulled Kagney towards his erection."
        wt_image kagney_student_chad_1_6
        chad_kagney "Now suck my cock you slut!"
        kagney.c "Mmmmm. You want me to suck this hard cock baby?"
        chad_kagney "Yeah. And since you’re dressed like a slut you better act like one. Now suck it!"
        wt_image kagney_student_chad_1_7
        "Kagney pushed him into the couch and started licking Chad’s erect member."
        wt_image kagney_student_chad_1_8
        "Her mouth tightly wrapped around his cock as her tongue worked on the tip."
        wt_image kagney_student_chad_1_9
        "With loud slurps, she made sure to be the slut Chad wanted. Every lick made him fall completely in love with her slutty mouth."
        wt_image kagney_student_chad_1_10
        chad_kagney "Fuck… Fuck yeah. You suck cock so well baby… I don’t even care if the rumors are true."
        wt_image kagney_student_chad_1_11
        "The action escalated and Chad pulled the horny Kagney on top of him. His cock soon parted her wet pussy and found its way deep inside."
        wt_image kagney_student_chad_1_12
        "Chad being the demanding jock he was, took control and pushed Kagney off in order to take control."
        wt_image kagney_student_chad_1_13
        "He bent Kagney over and slid his cock into her wet pussy. His thrusts were hard and the slaps to her ass were loud."
        wt_image kagney_student_chad_1_14
        "Kagney’s eyes flickered with delight as she stared towards the camera. Her body was enjoying being used by Chad."
        wt_image kagney_student_chad_1_15 
        "His cock continued to pound away at Kagney until she finally started to cum."
        wt_image kagney_student_chad_1_16
        "With a loud yell, the school slut’s pussy tightly gripped on to Chad as her orgasm rampaged through her body."
        wt_image kagney_student_chad_1_17
        "Chad did not stop and his thrusts became deeper and much more forceful."
        wt_image kagney_student_chad_1_18
        chad_kagney "You like that whore? Huh!? Take my cock in that slutty pussy you bitch!"
        wt_image kagney_student_chad_1_19
        "Kagney pushed her body up as he continued to ram his cock into her."
        wt_image kagney_student_chad_1_20
        kagney.c "Yes! I’m a slut! Fuck me like the slut I am! Fuck me harder!"
        wt_image kagney_student_chad_1_21
        "Kagney slipped off his cock and turned towards Chad. Once his cock re-entered her pussy, she again resumed her slutty sounds."
        wt_image kagney_student_chad_1_22
        "Kagney eagerly spread her ass to make sure Chad’s cock could go as deep as possible."
        wt_image kagney_student_chad_1_23  
        "Her hungry eyes matched with his. His thrusts sped up and Kagney was soon brought to another loud orgasm."
        wt_image kagney_student_chad_1_24
        kagney.c "You fuck me so good! Ahhhhhh! I’m cumming Chad!"
        wt_image kagney_student_chad_1_25
        "Soon after cumming a 2nd time, Kagney climbed back on top of Chad and bounced her ass hard on his cock."
        wt_image kagney_student_chad_1_26
        "The sound of slapping echoed around the room as Kagney rode his cock wildly."
        wt_image kagney_student_chad_1_27
        "With a few more bounces, Chad told Kagney he was going to paint her face with cum."
        wt_image kagney_student_chad_1_28
        "He was soon on his feet, jerking his cock inches away from Kagney’s face. Long streams soon shot out and covered her face."
        wt_image kagney_student_chad_1_29
        kagney.c "Cum on my face Chad! Cum all over your slut!"
        "With the last shot landing in her mouth, she licked away at his cock making sure it was all clean. Chad could be heard breathing very hard."
        wt_image kagney_student_chad_1_30
        "Kagney shot a hungry look at the camera and sucked on his cock for a few seconds. It was then she spoke-"
        kagney.c "Hehe… Yummy. I’m so glad you made me the school slut Chad. It was all for you baby."
        "Chad ignored this comment and the next few moments were of them cleaning up and leaving. Kagney picked up the phone and winked as the video finally ended."
        wt_image kagney_student_chad_1_19
        "Back in your apartment, Kagney was stroking your cock while kissing your neck."
        wt_image kagney_student_chad_1_16
        kagney.c "I showed daddy the video… Well the end and said he had been blackmailing me. Dad talked with the school admins and… Well I’m not sure what will happen to Chad."
        wt_image kagney_student_chad_1_18
        kagney.c "So did I do good? I’m hoping you reward me hehe. We are alone right now hehe..."
        wt_image kagney_student_chad_1_19
        "With her Father AND Chad taken care of, you take your blonde slut to your room and reward her. The future's looking good for you and Kagney. Now nothing will prevent you from making her the best slut around…"
        "You can sense her absolute Devotion towards her Master..."
        change player energy by -5
        change kagney desire by 5
        change kagney resistance by -10
        change kagney sos by -10
        notify
    call character_location_return(kagney)
    end_day
return

# Hypnosis Actions

label kagney_hypnosis_start:
    if kagney.status == "on_training" and current_location in session_locations:
        $ kagney.training_session()
        player.c "Kagney I am going to talk to you now, and you are going to listen to me"
        wt_image kagney_student_intro_1_3
        player.c "Listen to me now, Kagney. Listen to me. Listen to the sound of my voice and nothing else, Kagney. Only my voice. Only my voice now."
        wt_image kagney_student_intro_1_4
        "She falls under your trance"
        player.c "Kagney, I want you to get comfortable. Show me your breasts. Doesn't your shirt feel too tight?"
        wt_image kagney_student_intro_1_5
    else:
        "You can't hypnotize her right now."
        $ ignore_context_change = True
return  

label kagney_desire_hypnosis:
    if kagney.status == "on_training" and current_location in session_locations:
        wt_image kagney_student_intro_1_5
        "You work on raising Kagney's Desire for you."
        # system now applies the stat gain and then goes on to the _desire_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    else:
        sys "How'd you get here?  Coding error in Kagney Hypnosis Desire Action"
return

label kagney_submission_hypnosis:
    if kagney.status == "on_training" and current_location in session_locations:
        wt_image kagney_student_intro_1_5
        "You work on raising Kagney's Submission towards you."
        # system now applies the stat gain and then goes on to the _submisison_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    else:
        sys "How'd you get here?  Coding error in Kagney Hypnosis Submission Action"
return

label kagney_sos_hypnosis:
    if kagney.status == "on_training" and current_location in session_locations:
        wt_image kagney_student_intro_1_5
        "You work on raising Kagney's Sense of Self towards you."
        # system now applies the stat gain and then goes on to the _submisison_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    else:
        sys "How'd you get here?  Coding error in Kagney Hypnosis Sense of Self Action"
return

label kagney_resistance_hypnosis:
    if kagney.status == "on_training" and current_location in session_locations:
        wt_image kagney_student_intro_1_5
        "You work on lowering Kagney's Resistance to your suggestions."
        # system now applies the stat change and then goes on to the _resistance_hypnosis_end label, if there is one, or else to _implant_trigger if there is one
    else:
        sys "How'd you get here?  Coding error in Kagney Hypnosis Resistance Action"
return

label kagney_hypnosis_end:
    if kagney.status == "on_training" and current_location in session_locations:
        $ kagney.hypno_session()
        wt_image kagney_student_intro_1_5
        "When you've taken her as far as you can for this week, you have her dress, release her from your trance, and send her home.  The suggestions you've made will take time to fully affect her thinking."
        call character_location_return(kagney)
        end_day
    elif kagney.status == "post_training" and current_location in session_locations:
        $ kagney.hypno_session()
        kagney.c "Wow!  How'd it get so late?  I need to get going."
        call character_location_return(kagney)
        wt_image current_location.image
        notify
    else:
        sys "How'd you get here?  Coding error in Kagney Hypnosis End label."
return

label kagney_implant_trigger:
# _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust all counts accordingly
    if player.has_tag('hypnotist'):
        # note test is against unmodified stat
        if kagney.resistance <= kagney.hypno_trigger_resistance_threshold:
            add tag 'trigger_implanted' to kagney
            "Kagney's mind is very open to you now. You can implant a hypnotic trigger that may allow you to influence her behavior in the future."
            $ kagney.temporary_count = 1
            while kagney.temporary_count == 1:
                $ title = "What trigger phrase do you want to use?"
                menu menu_kagney_implant_trigger:
                    "[kagney.trigger_phrase]":
                        $ kagney.temporary_count = 0
                    "Choose something else":
                        $ kagney.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
            player.c "Kagney, I want you to listen to what I have to say. "
            player.c "When you hear the phrase, \"[kagney.trigger_phrase]\", you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you. Do you understand?"
            wt_image kagney_student_intro_1_19
            kagney.c "Yes. When I hear, \"[kagney.trigger_phrase]\", I will fall into a trance and do everything I am told."
            player.c "You will not remember anything you do while you are in a trance. Everything you do in the trance will seem normal, and you will not mind doing it. You will stay in the trance until the speaker of the phrase releases you. Do you understand?"
            wt_image kagney_student_intro_1_4
            kagney.c "Yes. I will forget everything I do in a trance. I won't mind doing it because it will seem normal. I'll stay in the trance until I'm released."
            "You can test Kagney's trigger on a future visit. Let her mind rest for now."
            notify "{}'s trigger has been implanted.".format(kagney.name)
            
        else:
            "You've been working on implanting a hypnotic trigger in Kagney's mind, but she's still too resistant to you. You need to lower her resistance to you before you can implant the trigger."
        change player energy by -10
return

label kagney_invoke_hypno_trigger:
  call kagney_trigger_used
  if kagney.status == "on_training":
    end_day
  
return

label kagney_trigger_used: 
    call forced_movement(living_room)
    summon kagney to living_room
    $ kagney.training_session()
    player.c "Kagney. the time for studies is over." 
    wt_image kagney_student_intro_1_19
    kagney.c "Are we going to do something else?"
    player.c "Bimbos don't need books, Kagney. It's time for a different oral test."
    kagney.c "I... Um... I..."
    player.c "Bimbos don't need books. It's time I teach you how to use your slutty body until I release you from your trance."
    wt_image kagney_student_intro_1_14
    kagney.c "But... I can't stop now... My grades..."
    wt_image kagney_student_intro_1_19
    player.c "Bimbos don't need books. You're a slut Kagney. My personal slut."
    wt_image kagney_student_intro_1_16
    player.c "Now my little student... What are you to me?"
    kagney.c "I'm... You're slut professor. Your personal slut."
    change kagney submission by 10
    notify
    menu menu_kagney_trigger_used:
        "Be more slutty at school" if not kagney.has_tag('slutty_at_school'):
            wt_image kagney_student_intro_1_19
            player.c  "Kagney you're wasting your time with school. There's an easy route that's been given to you and you're going to learn it."
            player.c  "I want you to start dressing more slutty and start seducing or blackmailing your professors."
            wt_image kagney_student_intro_1_18
            kagney.c "I will do as you say and seduce my professors."
            wt_image kagney_student_intro_1_16
            "Not wanting to overload Kagney's mental barriers, you snap her out of the hypnosis and tell her to come back next week with her new school uniform." 
            "She excitedly exclaims \"Can't wait!\" As she skips home. Next week... You'll start Kagney's REAL schooling." 
            $ kagney.add_tag('slutty_at_school')   
            change player energy by -10
        "Dress more slutty" if not kagney.has_tag('trigger_dress_slutty'):
            wt_image kagney_student_intro_1_19
            player.c "Kagney I think you’ve hidden away your beauty for too long. I want you to show the world just how much of a slut you are."
            wt_image kagney_student_intro_1_14
            kagney.c "But… I’m not a slut… I… I don’t want to be a slut."
            wt_image kagney_student_intro_1_19
            player.c "Bimbos don't need books. Listen to these words Kagney. Bimbos don't need books."
            wt_image kagney_student_intro_1_16
            kagney.c "I… I will dress slutty… I will show the world what a slut I am."
            "You clap your hands happily as you pull a bag of clothing you already chose for her." 
            "Kagney heads to the bathroom to change and soon comes out looking like a true slut."
            wt_image kagney_student_slutty_2_1
            "Wanting to take it all in, you instruct Kagney to put on a show to showcase her new clothing." 
            wt_image kagney_student_slutty_2_2
            "Her bare skin peeks out from the tight leather pants and she’s more than happy to show her legs for you."
            wt_image kagney_student_slutty_2_4
            "Turning around her tight round ass is perfectly hugging her new pants."
            wt_image kagney_student_slutty_2_5
            "Turning once more to face you, she pulls up her blouse to show off her new sexy bra."
            wt_image kagney_student_slutty_2_6
            "She eyes you with fuck me eyes while you take in how tight her clothing is hugging her body."
            wt_image kagney_student_slutty_2_7
            "Unzipping her pants you finally see her shaved pussy. Pulling up her bra you also get a nice look at her hard little nipples."
            wt_image kagney_student_slutty_2_8
            "She pulls the zipper all the way down and spreads herself wide for you. Her yummy fuckhole looked visably wet."
            wt_image kagney_student_slutty_2_9
            "Bringing  her legs up she made sure you peeked at both of her yummy holes. "
            wt_image kagney_student_slutty_2_10
            "To make sure Kagney accepted her new slutty persona, you bought a dildo to match her new wardrobe. She brought it out and wrapped her soft lips around it."
            wt_image kagney_student_slutty_2_11
            "Sitting on top of it she eyed your crotch as if eagerly waiting for you to fuck her. You waited hoping to starve the slut and enjoy her more when she was truly deprived."
            wt_image kagney_student_slutty_2_12
            "This choice was made difficult as Kagney pressed her round breasts together for you. Twirling her nipples, she bit her lip while still eyeing your crotch."
            wt_image kagney_student_slutty_2_13
            "To end the show you asked her to fuck the dildo a bit more. She happily agreed as she stayed kneeled and shook her ass at you."
            wt_image kagney_student_slutty_2_14
            "Her pussy clung on to the dildo tightly while she wiggled herself towards you. You gulped as Kagney let out a sensual moan."
            wt_image kagney_student_slutty_2_15
            player.c "Enough. This is the new you Kagney. I hope you embrace your new wardrobe, okay slut?"
            kagney.c "I will… Thank you Professor" 
            "With that final say you sent her home to fully distract everyone around her. Her new wardrobe was bound to draw eyes. Something she will grow to like soon enough."
            $ kagney.add_tag('trigger_dress_slutty')
            $ kagney.change_image('kagney_student_slutty_2_5')
            change player energy by -10
            change kagney resistance by -10
            change kagney submission by 10
            notify
        "Give her Slutty Lingerie?" if not kagney.has_tag('trigger_slutty_lingerie'): 
            wt_image kagney_student_intro_1_19
            player.c "I have something for my slut"
            kagney.c "A gift for me?"
            player.c "Yes. It's something all sluts should wear. Go put it on."
            "Kagney returns looking like a blonde pornstar"
            wt_image kagney_student_intro_1_14
            kagney.c  "I can't study in this..."
            wt_image kagney_student_intro_1_19
            player.c "I don't want you to study. I want you to act like the slut you are!"
            "You mutter out her Trigger Word and watch as the gorgeous blonde succumbs to the hypnosis. You hand her the lingerie as she disappears into the bathroom. "
            wt_image kagney_student_slutty_lingerie_1_1
            "She soon comes out looking absolutely radiant. You direct her to the window to get a better look at your little slut."
            wt_image kagney_student_slutty_lingerie_1_2
            "Kagney poses and turns at your every command as you take in how sexy she looks."
            wt_image kagney_student_slutty_lingerie_1_3
            player.c "You look like a real slut in that Kagney. In fact I think you should thank me for the gift."
            wt_image kagney_student_slutty_lingerie_1_5
            "You whip out your cock as Kagney’s eyes flutter with joy. Wrapping her fingers around your member, she jerks you off as you can feel her eyes devouring you." 
            wt_image kagney_student_slutty_lingerie_1_6
            "Kagney is soon bobbing happily on your cock. She looks up at you as you guide her to suck cock like a real slut. She nods, taking your cock deeper into her throat."
            wt_image kagney_student_slutty_lingerie_1_7
            kagney.c "Here Professor… Does this feel better? My titties wrapped around this amazing cock? Hehe, thank you for the gift, Professor."
            wt_image kagney_student_slutty_lingerie_1_8
            "After pulling out your cock from her bosom, she goes back to sucking you off lovingly. Her gagging is profound and her slurps are loud. She truly is a wonderful slut."
            wt_image kagney_student_slutty_lingerie_1_9
            "You soon push her back and dive down to eat out her delectable pussy. Your tongue laps up all her juices as she thanks her favorite Professor for the service."
            wt_image kagney_student_slutty_lingerie_1_10
            "Having filled up on foreplay, you guide Kagney on top of you and force her to impale herself on your man meat. Kagney bounces her fat ass right on your cock as she again thanks you for using her pussy."
            wt_image kagney_student_slutty_lingerie_1_11
            "Awakening to the idea she’s his personal slut, she spreads her legs and screams out to the empty home. You fuck Kagney for all she’s worth and make sure she grows addicted to your member after today."
            wt_image kagney_student_slutty_lingerie_1_12
            "After getting the ride of a lifetime, you bring her in close and continue to pound her tight wet pussy. Every thrust makes her breasts jiggle. Kagney continues to let you defile her body in whatever way you see fit."
            wt_image kagney_student_slutty_lingerie_1_13
            "Soon the sexy lingerie you bought for your slut is on the floor. Your hard cock continues to fuck Kagney into a state of submission."
            wt_image kagney_student_slutty_lingerie_1_14
            "Kagney has completely learned her place around you. Legs spread and eagerly waiting for you to rearrange her insides. She’s truly enjoying being your personal slut."
            wt_image kagney_student_slutty_lingerie_1_15
            kagney.c  "Yes! Oh God Yes! Professor, your cock’s going to make me cum! Fuck your slut harder please! Please… Ah! I just want to cum!"
            wt_image kagney_student_slutty_lingerie_1_16
            "Despite saying please, you pull your cock out and deny her orgasm further. She gives you sheepish eyes and groans for you to fuck her some more. You shake your head at your little slut."
            wt_image kagney_student_slutty_lingerie_1_17
            "Kagney gets up as you commanded and presents her breast to you. You suckle and lick it as she jerks off her favorite cock. Her pussy continues to quiver as it awaits your cock."
            wt_image kagney_student_slutty_lingerie_1_18
            "After enough teasing, you finally decide she’s ready. You completely fuck Kagney stupid as her moans are louder than ever. Before long she’s cumming happily on your cock."
            "You sense your own orgasm drawing near but fight back until it builds further. Kagney is meanwhile, happily taking your cock as her cute toes hang right in front of your face."
            wt_image kagney_student_slutty_lingerie_1_19
            "Your lust finally boils over as Kagney slurps the cum straight from your cock. Every single shot is swallowed as Kagney refuses to let your cock free. After what seems to be an eternity, she releases your cock with a loud pop."
            "She kisses your cock as cum stains her beautiful lips. It would seem breaking in your slut was easier said than done."
            "You quickly send her home and spend the rest of the day recovering from the sexcapade. If not careful, Kagney may end up breaking YOU instead..."
            $ kagney.add_tag('trigger_slutty_lingerie')
            change player energy by -15
            change kagney desire by 5
            change kagney submission by 5
            notify
        "Let’s have sex":
            $title = "What do you want to do?"
            menu menu_trigger_sex_menu:
                "Strip for Me":
                    wt_image kagney_student_slutty_1_1
                    "You direct Kagney to strip for you and hand her very particular clothing to do so in. A leather top and skirt combination should highlight her beauty well."
                    wt_image kagney_student_slutty_1_3
                    "Kagney walks in and poses for you. Moving her hands smoothly through her body.She shifts to the left and presents her ass to you. Images of hiking her skirt and fucking her right there and then flood your mind."
                    wt_image kagney_student_slutty_1_2
                    "She continues to get ever so closer while still rubbing her hands all over her soft and smooth body."
                    wt_image kagney_student_slutty_1_4
                    "She kneels and cups her breasts. She lets out a small moan to further entice you."
                    wt_image kagney_student_slutty_1_5
                    "Standing back up, Kagney slowly unzips her top. She pulls up the skirt almost in the same motion leaving you gulping for more."
                    wt_image kagney_student_slutty_1_6
                    kagney.c  "Do you like that Professor? Having a little slutty girl stripping for you? Mmmmmm. I know you do, Professor."
                    wt_image kagney_student_slutty_1_7
                    "Dropping her top she exposes her perfect breasts. Pinching her nipples ever so slightly, she drags her hands through her lips seductively."
                    wt_image kagney_student_slutty_1_8
                    "Hiking up her skirt you see her bare ass on display. Her lovely curves and long smooth legs again flood debaucherous images into your mind."
                    wt_image kagney_student_slutty_1_9
                    "Your eyes continue to take her the view as Kagney holds the pose. Again she moans out as you consume her radiant beauty."
                    wt_image kagney_student_slutty_1_10
                    kagney.c  "Professor, I feel so naughty… Exposing myself to you… Showing you my little nipples… Mmmmmmm. So naughty"
                    wt_image kagney_student_slutty_1_11
                    kagney.c  "I’m getting so wet for you Professor. Would you like to see how wet you’ve made your little schoolgirl?"
                    wt_image kagney_student_slutty_1_12
                    "You nod in response as Kagney spreads herself. Her pink pussy drips on the couch as a red blush appears on her face."
                    wt_image kagney_student_slutty_1_13
                    kagney.c "Professor… Your eyes. Your horny eyes are making me wet! Mmmmmm. I can’t help it anymore Professor… Watch me play with my innocent little pussy."
                    wt_image kagney_student_slutty_1_14
                    "Kagney moans out as her fingers dance all around her moist fuck hole. She exposes her clit and flicks it but once. Her legs tremble in excitement."
                    wt_image kagney_student_slutty_1_15
                    "Turning around she finger fucks herself while also shaking her large round ass. Kagney stares right into your eyes as she pleasures herself."
                    wt_image kagney_student_slutty_1_16
                    kagney.c "I’m going to cum Professor… I’m going to cum right in front of you… Ah! Professor watch your little slut finger herself! Watch me cum!"
                    wt_image kagney_student_slutty_1_17
                    "A loud cry echoes in your home as Kagney’s body trembles. A wide smile appears on her face as she winks at your general direction."
                    "She continues to play with her body for a while longer before you tell her to go home."
                    "She does as ordered, leaving you alone. Hopefully your little slut is always this passionate. You almost look forward to it."
                    change player energy by -5
                    change kagney desire by 5
                    change kagney submission by 5
                    change kagney sos by -10
                    notify
                "Fuck Her in BDSM":
                    if current_location != dungeon:
                        sys "This type of action may work better in the dungeon, if you've added items to it.  Take her there?"
                        $ title = "Take her to the dungeon?"
                        menu:
                            "Yes":
                                call forced_movement(dungeon)
                            "No, stay here":
                                pass
                    "You bring Kagney to your Dungeon as she looks around curiously. With the Hypnosis still in effect, Kagney is more inclined to have some fun here."
                    wt_image kagney_student_bdsm_1_1
                    "You gaze over at Kagney and see her revealing clothing. More so she still carries those \"fuck me\" eyes. Eyes that will soon change to something else."
                    wt_image kagney_student_bdsm_1_2
                    player.c "Kagney I’m your Professor correct? You would do anything I ask for good grades?"
                    kagney.c "Ye… Yes Professor! I… I’m your little slut so please give me a project to work on."
                    wt_image kagney_student_bdsm_1_3
                    "You drag Kagney into the large cage and handcuff her hands together. You proceed to tell her that she must repeat she’s your little \"Slutty School Girl\" or she fails." 
                    wt_image kagney_student_bdsm_1_4
                    "In complete darkness, Kagney yells out that she’s your little Slutty School Girl. For an hour she does this until her voice begins to break into a rasp." 
                    wt_image kagney_student_bdsm_1_2
                    "Pulling her closer you tell Kagney what a good student she is. She nods along but you soon tell her she’s getting an F. She’ll need to work on extra credit to pass. "
                    wt_image kagney_student_bdsm_1_5
                    "Forcing your cock down her throat, Kagney gags audibly. Her eyes narrow on you but she says nothing as you fill her slutty throat with your cock. "
                    wt_image kagney_student_bdsm_1_6
                    "Growing bored you raise her up and hike up her skirt. Your cock parts her wet pussy lips as you thrust in with no foreplay. Kagney screams out as you fuck her little pussy as hard as you want."
                    wt_image kagney_student_bdsm_1_7
                    "Your hands grip around Kagney’s neck as oxygen leaves her body. Just as her body weakens, you release the grip and see how tight her pussy grips your cock out of desperation."
                    wt_image kagney_student_bdsm_1_8
                    kagney.c "Ah… *Cough Cough* Professor… Am… Am I passing now? Can I tell my... Daddy, I did well on my project today?"
                    wt_image kagney_student_bdsm_1_9
                    "You spank her ass hard as she groans loudly. You bend her over and spread her little fuck hole wide. Her juices leak all over the ground as you taste it and fill your tastebuds with her naughty taste."
                    player.c "You pass when I say you pass. Now be a good little slut and beg me to fuck your pussy."
                    wt_image kagney_student_bdsm_1_10
                    "Loud slaps echo all around the room. Kagney’s voice still a little hearse, desperately repeats for you to fuck her pussy. The loud slapping of skin and her horny voice drown out everything else around you."
                    wt_image kagney_student_bdsm_1_11
                    kagney.c "YES! AH! FUCK… Fuck your little school girl… Fuck her tight pussy professor! Fuck me as much as I need to pass… I want to show daddy I did it!"
                    player.c "You want to show daddy how much of a whore you are? Is that what you want?"
                    kagney.c "Yes! I WANT TO SHOW DADDY HOW MUCH OF A WHORE I AM!"
                    wt_image kagney_student_bdsm_1_12
                    "Removing the rest of her clothes, you tie Kagney onto a cross. Her arms weakly struggle to free themselves all the while you whip her innocent and beautiful body. "
                    wt_image kagney_student_bdsm_1_13
                    "Kagney yells into her gag as red marks appear all over her body. Minutes later and her body is quivering and shaking from your torture. You remove the gag and bring Kagney down."
                    wt_image kagney_student_bdsm_1_14
                    player.c "You did well my little school girl. But I still have to give you a D. How do you plan to raise it?"
                    wt_image kagney_student_bdsm_1_15
                    kagney.c  "No… Please no… I need an A! I… I’ll do anything! Please Professor, I need an A for daddy!"
                    wt_image kagney_student_bdsm_1_16
                    "You slap her ass and soon spit right on your cock. Spreading her ass open you begin to slowly shove your cock into her tight little asshole. Kagney groans as her hole is filled completely with cock."
                    wt_image kagney_student_bdsm_1_17
                    player.c "There we go. I’m going to fuck your ass Kagney… Now beg me and I’ll raise your grade to an A. Beg you little whore."
                    wt_image kagney_student_bdsm_1_16
                    kagney.c "YES! YES! Ah... Of course Professor… Fuck my little asshole… I deserve it for being such a bad school girl. Fill my ass with you cock Professor!"
                    wt_image kagney_student_bdsm_1_18
                    "Minutes pass by as Kagney’s body shivers in delight. Your cock stretches out her asshole but she continues to motivate you to fuck it harder." 
                    wt_image kagney_student_bdsm_1_19
                    "You turn Kagney on her back and again shove your cock deep into her asshole. Her toes curl and the ropes around her body keep her breasts from moving."
                    wt_image kagney_student_bdsm_1_20
                    "Her pussy juices drip all over your cock as you rub her exposed clit. Kagney’s body soon tenses up and the scream that followed echoed out into the room. Kagney’s orgasm completely ravished her body."
                    wt_image kagney_student_bdsm_1_21
                    kagney.c "Look… Ah! Look at this little whore daddy! He made my cum so hard! Ah! Yes… Daddy my poor asshole is being filled up… But it’s for a good grade! Reward me Professor! Reward your little school girl slut!"
                    wt_image kagney_student_bdsm_1_22
                    "Pumping your cock even faster you hold off from cumming as best you can but soon… Your balls need to release on your little slut."
                    wt_image kagney_student_bdsm_1_23
                    "Cum rains down on Kagney as her hungry mouth catches what it can. Her body struggles against the ropes to catch more but it is to no avail. With your balls empty you untie the completely exhausted Kagney."
                    player.c "So… You get an A Kagney… But barely. Make sure to do better next time or else..."
                    wt_image kagney_student_bdsm_1_24
                    kagney.c  "Of course Professor… I’m your favorite student after all hehe. I hope to never disappoint you."
                    "Kagney licks the cum off her fingers and smiles wild at you. After cleaning up you send her home and make sure to hide the bruises and rope marks. You have hopes for the next project… One she’ll need to work for in order to get her A..."
                    change player energy by -30
                    change kagney desire by 5
                    change kagney submission by 20
                    change kagney resistance by -10
                    notify
    call character_location_return(kagney)
    end_day
return   

## Item Actions
# Give Butt Plug
label give_bp_kagney:
  if kagney.has_item(butt_plug):
    sys "You've already given her a butt plug.  She doesn't need another."
  else:
    if kagney.status == "on_training":
        "Kagney stares at the box wide-eyed. She nervously rubs her knees together."
        player.c "Make sure you study how to use it. I expect an oral exam on it soon."
        give 1 butt_plug from player to kagney notify
    else:
        if kagney.status == "post_training":
            "Kagney stares at the box wide-eyed. She nervously rubs her knees together."
            player.c "Make sure you study how to use it. I expect an oral exam on it soon."
            give 1 butt_plug from player to kagney notify  
        else:
            "You should save the butt plug for a current client."
return

# Give Chastity Belt
label give_cb_kagney:
  "You have no idea where to even begin to use this with Kagney. You quickly decide against it."
return

# Give Dildo
label give_di_kagney:
  if kagney.has_item(dildo):
    sys "You've already given her a dildo.  You don't need to give her another."
  else:
    if kagney.status == "post_training":
      if kagney.has_tag('girlfriend') or kagney.has_tag('hypno_girlfriend'):
        player.c "Kagney, you've been studying a little too much. I want you to have this to help alleviate your stress"
        player.c "Feel free to use it as a reward for studying well"
      else:
        sys "You should save this for a current client."
    elif kagney.status == "on_training":
        player.c "Kagney, you've been studying a little too much. I want you to have this to help alleviate your stress"
        player.c "Feel free to use it as a reward for studying well"
        give 1 dildo from player to kagney notify
return

# Use Fetch Toy
label use_ft_kagney:
  if kagney.has_tag('puppygirl'):
    "[kagney.full_name] is a well behaved pet, except when it comes to playing fetch."
    player.c "Sit girl.  Sit."
    "It doesn't work.  As soon as you start to throw the ball, she's off, not waiting for you to give the command to fetch.  You could punish her once again, but you know it won't do any good.  Her eagerness to chase the ball is just too great."
  else:
    "You shouldn't try to take someone for a walk who isn't your pet."
return

# Give Jewelry
label give_jwc_kagney:
  "Save this as a gift for [chelsea.name]."
return

# Use Leash
label use_le_kagney:
  if kagney.has_tag('puppygirl'):
    "[kagney.full_name] has been waiting all day for you to take her for a walk."
    "She eagerly sits up, leash in her mouth, eyes hopeful.  She gives a little bark of pleasure when you speak to her."
    player.c "Okay girl, let's go walksies."
  else:
    "You shouldn't try to take someone for a walk who isn't your pet."
return

# Give Lingerie
label give_li_kagney:
    "Despite looking excited at the present, Kagney returns her gift mainly because she doesn’t want to explain where it came from..."
return

# Give Love Potion
label give_lp_kagney:
  if kagney.has_tag('love_potion_used'):
    "You've already used a love potion on Kagney.  Additional ones won't do anything more."
  else:
    if kagney.status == "post_training":
      if kagney.has_tag('girlfriend'):
        sys "Kagney is already your girlfriend.  Are you sure you want to give her the potion and increase her infatuation with you?"
        $ title = "Use love potion on her?"
        menu:
          "Yes":
            wt_image kagney_student_intro_1_2
            player.c "Here Kagney, drink this.  It will help you relax."
            kagney.c "It's not alcohol, is it?"
            player.c "No, just a herbal tea.  It should help you feel less stressed."
            kagney.c "Wow, what's in this?  You were right, it is relaxing."
            player.c "Have I mentioned how amazingly hot you look today?  You are an incredibly handsome man. I should have told you that long ago."
            #"With a little bit of positive reinforcement during your time together, and you might make a friend for life."
            change kagney desire by 20
            add tag 'love_potion_used' to kagney
            rem 1 love_potion from player notify
          "No, save it for someone else":
            pass
      else:
        if kagney.has_tag('slavegirl') and not kagney.has_tag('transformed'):
          "[kagney.full_name] is already your devoted slavegirl.  Are you sure you want to give her the potion and increase her infatuation with you?"
          $ title = "Use love potion on her?"
          menu:
            "Yes, use it on her":
              wt_image kagney.image
              player.c "Drink this, [kagney.full_name]."
              kagney.c "Yes, [kagney.your_name]."
              wt_image frigid_drink_2
              "A moment later, she looks up at you, a look of pure bliss on her face."
              kagney.c "[kagney.your_name], I am so happy being near you.  I can't wait until the next time you want to fuck me, or spank me, or hurt me, or do anything you want to me."
              change kagney desire by 20
              add tag 'love_potion_used' to kagney
              rem 1 love_potion from player notify
            "No, save it for someone else":
              pass
        else:
          "You should save the love potion for current clients."
          
    elif kagney.status == "on_training":
      wt_image kagney_student_intro_1_2
      player.c "Kagney I picked up an energy drink for you. Should help you with your studies"
      kagney.c "Oh? Well I am feeling a bit groggy. Thank you."
      kagney.c "Oh this is pretty tasty. I should tell my friends about this."
      wt_image kagney_student_intro_1_3
      kagney.c "Um... I can't help but find you cute right now. Er... I guess the better word is handsome. Can... I sit next to you?"
      wt_image kagney_student_intro_1_4
      "Kagney responded well to the potion. All you need now is more positive reinforcement to make a life long friend."
      change kagney desire by 20
      add tag 'love_potion_used' to kagney
      rem 1 love_potion from player notify
      notify
return

# Give Transformation Potion
label give_tp_kagney:
    "You have no idea where to even begin to use this with Kagney. You quickly decide against it."
return

# Use Water Bowl
label use_wb_kagney:
  if kagney.has_tag('puppygirl'):
    "[kagney.full_name] drinks happily, then carefully cleans herself up."
  else:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
return

# Use Will Tamer
label use_wt_kagney:
    "You have no idea where to even begin to use this with Kagney. You quickly decide against it."
return

# Use Ring of Sexuality
label use_rs_kagney:
    "You have no idea where to even begin to use this with Kagney. You quickly decide against it."
return


label kagney_start_day:
    if week == kagney.event_week and day == 1:
        call kagney_school_fallout_followup
return
# Arrange Client Session
# OBJECT: Schedule Client Session

################################### NOTES ###################################
## Character Status
#0 = not yet prospect
#1 = prospect, .status = "available_to_be_client" and .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = client, .status = "on_training"
#4 = unsatisfied former client, add tag 'unsatisfied' and .status = "post_training"
#5 = satisfied former client, add tag 'satisfied' and .status = "post_training"
#6 = continuing_actions, add tag 'continuing_actions' and .status = "post_training"
#7 = satisfied former client not continuing, rem tag 'continuing_actions' and .status = "post_training"
#8 = post continuing actions, add tag 'post_continuing_actions' and .status = "post_training"
